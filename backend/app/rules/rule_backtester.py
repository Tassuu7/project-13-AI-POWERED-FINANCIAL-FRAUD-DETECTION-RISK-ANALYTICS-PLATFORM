"""
Aegis Fraud Labs – Rule Backtesting & Simulation Engine
Evaluates fraud rules across historical transaction ledgers to calculate precision, recall, and false positive ratios.
"""
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
import pandas as pd
import numpy as np
import datetime
from backend.app.rules.rule_definitions import rule_catalog, FraudRule
from backend.app.rules.rule_dsl import rule_compiler

@dataclass
class RulePerformanceMetrics:
    rule_id: str
    rule_name: str
    total_samples: int
    true_positives: int
    false_positives: int
    true_negatives: int
    false_negatives: int
    precision: float
    recall: float
    f1_score: float
    trigger_rate: float
    dollar_volume_flagged: float
    dollar_volume_prevented: float

@dataclass
class BacktestReport:
    dataset_name: str
    total_transactions: int
    fraud_prevalence: float
    evaluated_rules_count: int
    rule_metrics: List[RulePerformanceMetrics] = field(default_factory=list)
    overall_precision: float = 0.0
    overall_recall: float = 0.0
    overall_f1: float = 0.0
    total_execution_time_sec: float = 0.0

class RuleBacktester:
    def __init__(self):
        self.compiler = rule_compiler
        self.catalog = rule_catalog

    def run_backtest(self, df: pd.DataFrame, target_column: str = "is_fraud") -> BacktestReport:
        t_start = datetime.datetime.now()
        n = len(df)
        actual_fraud = df[target_column].astype(bool).values if target_column in df.columns else np.zeros(n, dtype=bool)
        fraud_count = int(np.sum(actual_fraud))
        prevalence = fraud_count / n if n > 0 else 0.0
        records = df.to_dict(orient="records")
        metrics_list: List[RulePerformanceMetrics] = []

        global_tp = 0
        global_fp = 0
        global_tn = 0
        global_fn = 0

        for rule in self.catalog.rules.values():
            if not rule.enabled:
                continue
            tp = fp = tn = fn = 0
            flagged_vol = 0.0
            prevented_vol = 0.0

            try:
                ast = self.compiler.compile(rule.expression)
                for idx, row in enumerate(records):
                    is_actual = actual_fraud[idx]
                    amt = float(row.get("amount", 0.0))
                    is_pred = bool(ast.evaluate(row))
                    if is_pred and is_actual:
                        tp += 1
                        prevented_vol += amt
                        flagged_vol += amt
                    elif is_pred and not is_actual:
                        fp += 1
                        flagged_vol += amt
                    elif not is_pred and is_actual:
                        fn += 1
                    else:
                        tn += 1
            except Exception:
                continue

            prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0
            rec = tp / (tp + fn) if (tp + fn) > 0 else 0.0
            f1 = 2 * (prec * rec) / (prec + rec) if (prec + rec) > 0 else 0.0
            trig_rate = (tp + fp) / n if n > 0 else 0.0

            metrics_list.append(RulePerformanceMetrics(
                rule_id=rule.rule_id,
                rule_name=rule.name,
                total_samples=n,
                true_positives=tp,
                false_positives=fp,
                true_negatives=tn,
                false_negatives=fn,
                precision=round(prec, 4),
                recall=round(rec, 4),
                f1_score=round(f1, 4),
                trigger_rate=round(trig_rate, 4),
                dollar_volume_flagged=round(flagged_vol, 2),
                dollar_volume_prevented=round(prevented_vol, 2)
            ))

        dur = (datetime.datetime.now() - t_start).total_seconds()
        return BacktestReport(
            dataset_name="in_memory_dataframe",
            total_transactions=n,
            fraud_prevalence=round(prevalence, 4),
            evaluated_rules_count=len(metrics_list),
            rule_metrics=sorted(metrics_list, key=lambda x: -x.f1_score),
            total_execution_time_sec=round(dur, 2)
        )

rule_backtester = RuleBacktester()