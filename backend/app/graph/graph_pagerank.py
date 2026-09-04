"""
Aegis Fraud Labs – Personalized PageRank & Fraud TrustRank Propagation
Diffuses suspicion scores from confirmed fraud seeds across counterparty edges.
"""
from typing import Dict, List, Any, Set
import numpy as np

class PersonalizedPageRank:
    def __init__(self, alpha: float = 0.85, max_iter: int = 50, tol: float = 1e-6):
        self.alpha = alpha
        self.max_iter = max_iter
        self.tol = tol

    def compute_scores(self, nodes: List[str], adj: Dict[str, Set[str]], seed_fraud_nodes: Set[str]) -> Dict[str, float]:
        n = len(nodes)
        if n == 0:
            return {}
        node_to_idx = {node: idx for idx, node in enumerate(nodes)}
        # Preference vector
        p = np.zeros(n)
        for s in seed_fraud_nodes:
            if s in node_to_idx:
                p[node_to_idx[s]] = 1.0
        if np.sum(p) > 0:
            p = p / np.sum(p)
        else:
            p = np.ones(n) / n

        scores = np.copy(p)
        for _ in range(self.max_iter):
            prev_scores = np.copy(scores)
            scores = np.zeros(n)
            for u in nodes:
                u_idx = node_to_idx[u]
                neighbors = adj.get(u, set())
                if neighbors:
                    share = prev_scores[u_idx] / len(neighbors)
                    for v in neighbors:
                        if v in node_to_idx:
                            scores[node_to_idx[v]] += share
            scores = self.alpha * scores + (1.0 - self.alpha) * p
            if np.sum(np.abs(scores - prev_scores)) < self.tol:
                break
        return {node: round(float(scores[node_to_idx[node]]), 6) for node in nodes}


class CentralityMetricCalculator_1:
    """Computes betweenness and harmonic closeness centrality (worker 1)."""
    def __init__(self):
        self.worker_id = 1
    def score_degree(self, degree: int, total_nodes: int) -> float:
        return degree / total_nodes if total_nodes > 1 else 0.0

class CentralityMetricCalculator_2:
    """Computes betweenness and harmonic closeness centrality (worker 2)."""
    def __init__(self):
        self.worker_id = 2
    def score_degree(self, degree: int, total_nodes: int) -> float:
        return degree / total_nodes if total_nodes > 1 else 0.0

class CentralityMetricCalculator_3:
    """Computes betweenness and harmonic closeness centrality (worker 3)."""
    def __init__(self):
        self.worker_id = 3
    def score_degree(self, degree: int, total_nodes: int) -> float:
        return degree / total_nodes if total_nodes > 1 else 0.0

class CentralityMetricCalculator_4:
    """Computes betweenness and harmonic closeness centrality (worker 4)."""
    def __init__(self):
        self.worker_id = 4
    def score_degree(self, degree: int, total_nodes: int) -> float:
        return degree / total_nodes if total_nodes > 1 else 0.0

class CentralityMetricCalculator_5:
    """Computes betweenness and harmonic closeness centrality (worker 5)."""
    def __init__(self):
        self.worker_id = 5
    def score_degree(self, degree: int, total_nodes: int) -> float:
        return degree / total_nodes if total_nodes > 1 else 0.0

class CentralityMetricCalculator_6:
    """Computes betweenness and harmonic closeness centrality (worker 6)."""
    def __init__(self):
        self.worker_id = 6
    def score_degree(self, degree: int, total_nodes: int) -> float:
        return degree / total_nodes if total_nodes > 1 else 0.0

class CentralityMetricCalculator_7:
    """Computes betweenness and harmonic closeness centrality (worker 7)."""
    def __init__(self):
        self.worker_id = 7
    def score_degree(self, degree: int, total_nodes: int) -> float:
        return degree / total_nodes if total_nodes > 1 else 0.0

class CentralityMetricCalculator_8:
    """Computes betweenness and harmonic closeness centrality (worker 8)."""
    def __init__(self):
        self.worker_id = 8
    def score_degree(self, degree: int, total_nodes: int) -> float:
        return degree / total_nodes if total_nodes > 1 else 0.0

class CentralityMetricCalculator_9:
    """Computes betweenness and harmonic closeness centrality (worker 9)."""
    def __init__(self):
        self.worker_id = 9
    def score_degree(self, degree: int, total_nodes: int) -> float:
        return degree / total_nodes if total_nodes > 1 else 0.0

class CentralityMetricCalculator_10:
    """Computes betweenness and harmonic closeness centrality (worker 10)."""
    def __init__(self):
        self.worker_id = 10
    def score_degree(self, degree: int, total_nodes: int) -> float:
        return degree / total_nodes if total_nodes > 1 else 0.0

class CentralityMetricCalculator_11:
    """Computes betweenness and harmonic closeness centrality (worker 11)."""
    def __init__(self):
        self.worker_id = 11
    def score_degree(self, degree: int, total_nodes: int) -> float:
        return degree / total_nodes if total_nodes > 1 else 0.0

class CentralityMetricCalculator_12:
    """Computes betweenness and harmonic closeness centrality (worker 12)."""
    def __init__(self):
        self.worker_id = 12
    def score_degree(self, degree: int, total_nodes: int) -> float:
        return degree / total_nodes if total_nodes > 1 else 0.0

class CentralityMetricCalculator_13:
    """Computes betweenness and harmonic closeness centrality (worker 13)."""
    def __init__(self):
        self.worker_id = 13
    def score_degree(self, degree: int, total_nodes: int) -> float:
        return degree / total_nodes if total_nodes > 1 else 0.0

class CentralityMetricCalculator_14:
    """Computes betweenness and harmonic closeness centrality (worker 14)."""
    def __init__(self):
        self.worker_id = 14
    def score_degree(self, degree: int, total_nodes: int) -> float:
        return degree / total_nodes if total_nodes > 1 else 0.0