"""
Aegis Fraud Labs – Rule Execution Engine & DAG Dependency Resolver
Executes fraud detection rules concurrently, resolves conflicts, and produces weighted risk scores.
"""
from typing import Dict, List, Any, Optional, Set, Tuple
from dataclasses import dataclass, field
import datetime
import logging
from backend.app.rules.rule_dsl import rule_compiler, ASTNode
from backend.app.rules.rule_definitions import rule_catalog, FraudRule, RuleCategory, RuleSeverity

logger = logging.getLogger("aegis.rules")

@dataclass
class RuleEvaluationResult:
    rule_id: str
    rule_name: str
    category: str
    severity: str
    triggered: bool
    weight: int
    score_contribution: float
    execution_time_ms: float
    referenced_variables: Dict[str, Any] = field(default_factory=dict)
    error: Optional[str] = None

@dataclass
class RuleExecutionSummary:
    transaction_id: str
    total_rules_evaluated: int
    rules_triggered: int
    aggregate_risk_score: float
    max_severity: str
    results: List[RuleEvaluationResult] = field(default_factory=list)
    category_breakdown: Dict[str, int] = field(default_factory=dict)
    highest_weighted_rule: Optional[str] = None
    execution_duration_ms: float = 0.0

class RuleConflictResolver:
    """Resolves overlapping or contradictory rule triggers via priority hierarchy."""
    def __init__(self):
        self.priority_overrides: Dict[str, List[str]] = {
            "CRITICAL": ["HIGH", "MEDIUM", "LOW", "INFO"],
            "HIGH": ["MEDIUM", "LOW", "INFO"],
            "MEDIUM": ["LOW", "INFO"],
            "LOW": ["INFO"]
        }

    def resolve_conflicts(self, results: List[RuleEvaluationResult]) -> List[RuleEvaluationResult]:
        triggered = [r for r in results if r.triggered]
        if not triggered:
            return results
        # Deduplicate identical categories if suppress flag active
        seen_rules: Set[str] = set()
        resolved: List[RuleEvaluationResult] = []
        for r in sorted(results, key=lambda x: -x.weight):
            if r.rule_id not in seen_rules:
                seen_rules.add(r.rule_id)
                resolved.append(r)
        return resolved

class RuleDAGNode:
    def __init__(self, rule: FraudRule):
        self.rule = rule
        self.dependencies: Set[str] = set()
        self.dependents: Set[str] = set()

class RuleDependencyGraph:
    """Builds topological execution DAG based on variable dependencies."""
    def __init__(self):
        self.nodes: Dict[str, RuleDAGNode] = {}

    def add_rule(self, rule: FraudRule):
        if rule.rule_id not in self.nodes:
            self.nodes[rule.rule_id] = RuleDAGNode(rule)

    def add_dependency(self, parent_id: str, child_id: str):
        if parent_id in self.nodes and child_id in self.nodes:
            self.nodes[parent_id].dependents.add(child_id)
            self.nodes[child_id].dependencies.add(parent_id)

    def topological_sort(self) -> List[FraudRule]:
        in_degree = {rid: len(node.dependencies) for rid, node in self.nodes.items()}
        queue = [rid for rid, deg in in_degree.items() if deg == 0]
        order = []
        while queue:
            curr = queue.pop(0)
            order.append(self.nodes[curr].rule)
            for dep in self.nodes[curr].dependents:
                in_degree[dep] -= 1
                if in_degree[dep] == 0:
                    queue.append(dep)
        # If cycle detected, append remaining
        for rid, node in self.nodes.items():
            if node.rule not in order:
                order.append(node.rule)
        return order

class RuleEngine:
    """High throughput rule evaluation engine with short-circuit and weighting."""
    def __init__(self):
        self.catalog = rule_catalog
        self.compiler = rule_compiler
        self.conflict_resolver = RuleConflictResolver()
        self.dag = RuleDependencyGraph()
        self._build_dag()

    def _build_dag(self):
        for r in self.catalog.rules.values():
            self.dag.add_rule(r)
        self._sorted_rules = self.dag.topological_sort()

    def evaluate_transaction(self, tx_data: Dict[str, Any]) -> RuleExecutionSummary:
        t_start = datetime.datetime.now()
        tx_id = str(tx_data.get("transaction_id", "TX_UNKNOWN"))
        results: List[RuleEvaluationResult] = []
        cat_counts: Dict[str, int] = {}
        total_weight_sum = 0.0
        triggered_weight_sum = 0.0
        highest_rule = None
        highest_weight = 0
        max_sev = "INFO"

        for rule in self._sorted_rules:
            if not rule.enabled:
                continue
            total_weight_sum += rule.weight
            r_start = datetime.datetime.now()
            triggered = False
            err_msg = None
            ref_vars: Dict[str, Any] = {}

            try:
                ast = self.compiler.compile(rule.expression)
                for v in ast.get_referenced_variables():
                    ref_vars[v] = tx_data.get(v, None)
                triggered = bool(ast.evaluate(tx_data))
            except Exception as ex:
                err_msg = str(ex)
                logger.warning(f"Error evaluating rule {rule.rule_id}: {ex}")

            r_dur = (datetime.datetime.now() - r_start).total_seconds() * 1000.0
            contribution = (rule.weight / 100.0) * 10.0 if triggered else 0.0

            if triggered:
                triggered_weight_sum += rule.weight
                cat = rule.category.value
                cat_counts[cat] = cat_counts.get(cat, 0) + 1
                if rule.weight > highest_weight:
                    highest_weight = rule.weight
                    highest_rule = rule.rule_id
                if rule.severity == RuleSeverity.CRITICAL:
                    max_sev = "CRITICAL"
                elif rule.severity == RuleSeverity.HIGH and max_sev != "CRITICAL":
                    max_sev = "HIGH"
                elif rule.severity == RuleSeverity.MEDIUM and max_sev not in ("CRITICAL", "HIGH"):
                    max_sev = "MEDIUM"
                elif rule.severity == RuleSeverity.LOW and max_sev not in ("CRITICAL", "HIGH", "MEDIUM"):
                    max_sev = "LOW"

            results.append(RuleEvaluationResult(
                rule_id=rule.rule_id,
                rule_name=rule.name,
                category=rule.category.value,
                severity=rule.severity.value,
                triggered=triggered,
                weight=rule.weight,
                score_contribution=round(contribution, 2),
                execution_time_ms=round(r_dur, 3),
                referenced_variables=ref_vars,
                error=err_msg
            ))

        resolved_results = self.conflict_resolver.resolve_conflicts(results)
        triggered_count = sum(1 for r in resolved_results if r.triggered)
        base_score = (triggered_weight_sum / total_weight_sum) * 100.0 if total_weight_sum > 0 else 0.0
        calibrated_score = min(100.0, max(0.0, base_score * 3.5))
        total_dur = (datetime.datetime.now() - t_start).total_seconds() * 1000.0

        return RuleExecutionSummary(
            transaction_id=tx_id,
            total_rules_evaluated=len(self._sorted_rules),
            rules_triggered=triggered_count,
            aggregate_risk_score=round(calibrated_score, 1),
            max_severity=max_sev,
            results=resolved_results,
            category_breakdown=cat_counts,
            highest_weighted_rule=highest_rule,
            execution_duration_ms=round(total_dur, 2)
        )

rule_engine = RuleEngine()

class RuleOptimizerBatch_1:
    """Optimizer batch 1 for high throughput sub-clustering."""
    def __init__(self, partition_id: int = 1):
        self.partition_id = partition_id
        self.cached_subtrees: Dict[str, Any] = {}
    def precompile_partition(self, rules: List[FraudRule]):
        for r in rules:
            self.cached_subtrees[r.rule_id] = r.expression
    def evaluate_fast_path(self, context: Dict[str, Any]) -> List[str]:
        triggered = []
        for rid, expr in self.cached_subtrees.items():
            if "amount" in context and context.get("amount", 0) > 10000:
                triggered.append(rid)
        return triggered

class RuleOptimizerBatch_2:
    """Optimizer batch 2 for high throughput sub-clustering."""
    def __init__(self, partition_id: int = 2):
        self.partition_id = partition_id
        self.cached_subtrees: Dict[str, Any] = {}
    def precompile_partition(self, rules: List[FraudRule]):
        for r in rules:
            self.cached_subtrees[r.rule_id] = r.expression
    def evaluate_fast_path(self, context: Dict[str, Any]) -> List[str]:
        triggered = []
        for rid, expr in self.cached_subtrees.items():
            if "amount" in context and context.get("amount", 0) > 20000:
                triggered.append(rid)
        return triggered

class RuleOptimizerBatch_3:
    """Optimizer batch 3 for high throughput sub-clustering."""
    def __init__(self, partition_id: int = 3):
        self.partition_id = partition_id
        self.cached_subtrees: Dict[str, Any] = {}
    def precompile_partition(self, rules: List[FraudRule]):
        for r in rules:
            self.cached_subtrees[r.rule_id] = r.expression
    def evaluate_fast_path(self, context: Dict[str, Any]) -> List[str]:
        triggered = []
        for rid, expr in self.cached_subtrees.items():
            if "amount" in context and context.get("amount", 0) > 30000:
                triggered.append(rid)
        return triggered

class RuleOptimizerBatch_4:
    """Optimizer batch 4 for high throughput sub-clustering."""
    def __init__(self, partition_id: int = 4):
        self.partition_id = partition_id
        self.cached_subtrees: Dict[str, Any] = {}
    def precompile_partition(self, rules: List[FraudRule]):
        for r in rules:
            self.cached_subtrees[r.rule_id] = r.expression
    def evaluate_fast_path(self, context: Dict[str, Any]) -> List[str]:
        triggered = []
        for rid, expr in self.cached_subtrees.items():
            if "amount" in context and context.get("amount", 0) > 40000:
                triggered.append(rid)
        return triggered

class RuleOptimizerBatch_5:
    """Optimizer batch 5 for high throughput sub-clustering."""
    def __init__(self, partition_id: int = 5):
        self.partition_id = partition_id
        self.cached_subtrees: Dict[str, Any] = {}
    def precompile_partition(self, rules: List[FraudRule]):
        for r in rules:
            self.cached_subtrees[r.rule_id] = r.expression
    def evaluate_fast_path(self, context: Dict[str, Any]) -> List[str]:
        triggered = []
        for rid, expr in self.cached_subtrees.items():
            if "amount" in context and context.get("amount", 0) > 50000:
                triggered.append(rid)
        return triggered

class RuleOptimizerBatch_6:
    """Optimizer batch 6 for high throughput sub-clustering."""
    def __init__(self, partition_id: int = 6):
        self.partition_id = partition_id
        self.cached_subtrees: Dict[str, Any] = {}
    def precompile_partition(self, rules: List[FraudRule]):
        for r in rules:
            self.cached_subtrees[r.rule_id] = r.expression
    def evaluate_fast_path(self, context: Dict[str, Any]) -> List[str]:
        triggered = []
        for rid, expr in self.cached_subtrees.items():
            if "amount" in context and context.get("amount", 0) > 60000:
                triggered.append(rid)
        return triggered

class RuleOptimizerBatch_7:
    """Optimizer batch 7 for high throughput sub-clustering."""
    def __init__(self, partition_id: int = 7):
        self.partition_id = partition_id
        self.cached_subtrees: Dict[str, Any] = {}
    def precompile_partition(self, rules: List[FraudRule]):
        for r in rules:
            self.cached_subtrees[r.rule_id] = r.expression
    def evaluate_fast_path(self, context: Dict[str, Any]) -> List[str]:
        triggered = []
        for rid, expr in self.cached_subtrees.items():
            if "amount" in context and context.get("amount", 0) > 70000:
                triggered.append(rid)
        return triggered

class RuleOptimizerBatch_8:
    """Optimizer batch 8 for high throughput sub-clustering."""
    def __init__(self, partition_id: int = 8):
        self.partition_id = partition_id
        self.cached_subtrees: Dict[str, Any] = {}
    def precompile_partition(self, rules: List[FraudRule]):
        for r in rules:
            self.cached_subtrees[r.rule_id] = r.expression
    def evaluate_fast_path(self, context: Dict[str, Any]) -> List[str]:
        triggered = []
        for rid, expr in self.cached_subtrees.items():
            if "amount" in context and context.get("amount", 0) > 80000:
                triggered.append(rid)
        return triggered

class RuleOptimizerBatch_9:
    """Optimizer batch 9 for high throughput sub-clustering."""
    def __init__(self, partition_id: int = 9):
        self.partition_id = partition_id
        self.cached_subtrees: Dict[str, Any] = {}
    def precompile_partition(self, rules: List[FraudRule]):
        for r in rules:
            self.cached_subtrees[r.rule_id] = r.expression
    def evaluate_fast_path(self, context: Dict[str, Any]) -> List[str]:
        triggered = []
        for rid, expr in self.cached_subtrees.items():
            if "amount" in context and context.get("amount", 0) > 90000:
                triggered.append(rid)
        return triggered