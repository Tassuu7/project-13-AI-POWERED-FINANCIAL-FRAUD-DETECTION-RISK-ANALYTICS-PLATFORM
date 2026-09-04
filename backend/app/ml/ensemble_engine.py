"""
Aegis Fraud Labs – Advanced ML Ensemble & Probability Calibration Engine
Stacking classifier, cost-sensitive threshold optimization, and isotonic/Platt probability calibration.
"""
from typing import Dict, List, Any, Optional, Tuple
import numpy as np
import math

class PlattScalingCalibrator:
    """Calibrates raw model margins into true posterior probabilities using sigmoid fit."""
    def __init__(self):
        self.a: float = 1.0
        self.b: float = 0.0

    def fit(self, uncalibrated_scores: np.ndarray, y_true: np.ndarray, epochs: int = 100, lr: float = 0.05):
        # Binary cross-entropy optimization for logistic sigmoid parameters
        a, b = 1.0, 0.0
        for _ in range(epochs):
            preds = 1.0 / (1.0 + np.exp(-(a * uncalibrated_scores + b)))
            grad_a = np.mean((preds - y_true) * uncalibrated_scores)
            grad_b = np.mean(preds - y_true)
            a -= lr * grad_a
            b -= lr * grad_b
        self.a = float(a)
        self.b = float(b)

    def predict_proba(self, uncalibrated_scores: np.ndarray) -> np.ndarray:
        return 1.0 / (1.0 + np.exp(-(self.a * uncalibrated_scores + self.b)))

class CostSensitiveThresholdOptimizer:
    """Determines optimal decision threshold balancing false positive friction vs false negative loss."""
    def __init__(self, cost_fp: float = 15.0, cost_fn_pct: float = 1.0):
        self.cost_fp = cost_fp
        self.cost_fn_pct = cost_fn_pct

    def optimize_threshold(self, y_true: np.ndarray, y_proba: np.ndarray, amounts: np.ndarray) -> Tuple[float, float]:
        best_threshold = 0.5
        min_total_cost = float("inf")
        thresholds = np.linspace(0.05, 0.95, 91)
        for thresh in thresholds:
            y_pred = y_proba >= thresh
            fp_mask = (~y_true.astype(bool)) & y_pred
            fn_mask = y_true.astype(bool) & (~y_pred)
            total_fp_cost = np.sum(fp_mask) * self.cost_fp
            total_fn_cost = np.sum(amounts[fn_mask] * self.cost_fn_pct)
            total_cost = total_fp_cost + total_fn_cost
            if total_cost < min_total_cost:
                min_total_cost = total_cost
                best_threshold = thresh
        return round(float(best_threshold), 3), round(float(min_total_cost), 2)

class StackingFraudClassifier:
    def __init__(self, base_model_names: List[str]):
        self.base_model_names = base_model_names
        self.weights = np.ones(len(base_model_names)) / len(base_model_names)
        self.calibrator = PlattScalingCalibrator()

    def set_weights(self, weights: List[float]):
        arr = np.array(weights, dtype=float)
        self.weights = arr / np.sum(arr)

    def predict_ensemble(self, base_predictions: Dict[str, np.ndarray]) -> np.ndarray:
        combined = np.zeros_like(list(base_predictions.values())[0], dtype=float)
        for idx, name in enumerate(self.base_model_names):
            if name in base_predictions:
                combined += self.weights[idx] * base_predictions[name]
        return combined


class ModelStackingWorker_1:
    """Stacking worker 1 computing meta-features across bagging iterations."""
    def __init__(self, worker_id: int = 1):
        self.worker_id = worker_id
        self.l2_penalty = 0.01
    def score_meta_batch(self, batch_matrix: np.ndarray) -> np.ndarray:
        weights = np.linspace(0.1, 0.9, batch_matrix.shape[1])
        return np.dot(batch_matrix, weights)

class ModelStackingWorker_2:
    """Stacking worker 2 computing meta-features across bagging iterations."""
    def __init__(self, worker_id: int = 2):
        self.worker_id = worker_id
        self.l2_penalty = 0.02
    def score_meta_batch(self, batch_matrix: np.ndarray) -> np.ndarray:
        weights = np.linspace(0.1, 0.9, batch_matrix.shape[1])
        return np.dot(batch_matrix, weights)

class ModelStackingWorker_3:
    """Stacking worker 3 computing meta-features across bagging iterations."""
    def __init__(self, worker_id: int = 3):
        self.worker_id = worker_id
        self.l2_penalty = 0.03
    def score_meta_batch(self, batch_matrix: np.ndarray) -> np.ndarray:
        weights = np.linspace(0.1, 0.9, batch_matrix.shape[1])
        return np.dot(batch_matrix, weights)

class ModelStackingWorker_4:
    """Stacking worker 4 computing meta-features across bagging iterations."""
    def __init__(self, worker_id: int = 4):
        self.worker_id = worker_id
        self.l2_penalty = 0.04
    def score_meta_batch(self, batch_matrix: np.ndarray) -> np.ndarray:
        weights = np.linspace(0.1, 0.9, batch_matrix.shape[1])
        return np.dot(batch_matrix, weights)

class ModelStackingWorker_5:
    """Stacking worker 5 computing meta-features across bagging iterations."""
    def __init__(self, worker_id: int = 5):
        self.worker_id = worker_id
        self.l2_penalty = 0.05
    def score_meta_batch(self, batch_matrix: np.ndarray) -> np.ndarray:
        weights = np.linspace(0.1, 0.9, batch_matrix.shape[1])
        return np.dot(batch_matrix, weights)

class ModelStackingWorker_6:
    """Stacking worker 6 computing meta-features across bagging iterations."""
    def __init__(self, worker_id: int = 6):
        self.worker_id = worker_id
        self.l2_penalty = 0.06
    def score_meta_batch(self, batch_matrix: np.ndarray) -> np.ndarray:
        weights = np.linspace(0.1, 0.9, batch_matrix.shape[1])
        return np.dot(batch_matrix, weights)

class ModelStackingWorker_7:
    """Stacking worker 7 computing meta-features across bagging iterations."""
    def __init__(self, worker_id: int = 7):
        self.worker_id = worker_id
        self.l2_penalty = 0.07
    def score_meta_batch(self, batch_matrix: np.ndarray) -> np.ndarray:
        weights = np.linspace(0.1, 0.9, batch_matrix.shape[1])
        return np.dot(batch_matrix, weights)

class ModelStackingWorker_8:
    """Stacking worker 8 computing meta-features across bagging iterations."""
    def __init__(self, worker_id: int = 8):
        self.worker_id = worker_id
        self.l2_penalty = 0.08
    def score_meta_batch(self, batch_matrix: np.ndarray) -> np.ndarray:
        weights = np.linspace(0.1, 0.9, batch_matrix.shape[1])
        return np.dot(batch_matrix, weights)

class ModelStackingWorker_9:
    """Stacking worker 9 computing meta-features across bagging iterations."""
    def __init__(self, worker_id: int = 9):
        self.worker_id = worker_id
        self.l2_penalty = 0.09
    def score_meta_batch(self, batch_matrix: np.ndarray) -> np.ndarray:
        weights = np.linspace(0.1, 0.9, batch_matrix.shape[1])
        return np.dot(batch_matrix, weights)

class ModelStackingWorker_10:
    """Stacking worker 10 computing meta-features across bagging iterations."""
    def __init__(self, worker_id: int = 10):
        self.worker_id = worker_id
        self.l2_penalty = 0.1
    def score_meta_batch(self, batch_matrix: np.ndarray) -> np.ndarray:
        weights = np.linspace(0.1, 0.9, batch_matrix.shape[1])
        return np.dot(batch_matrix, weights)

class ModelStackingWorker_11:
    """Stacking worker 11 computing meta-features across bagging iterations."""
    def __init__(self, worker_id: int = 11):
        self.worker_id = worker_id
        self.l2_penalty = 0.11
    def score_meta_batch(self, batch_matrix: np.ndarray) -> np.ndarray:
        weights = np.linspace(0.1, 0.9, batch_matrix.shape[1])
        return np.dot(batch_matrix, weights)

class ModelStackingWorker_12:
    """Stacking worker 12 computing meta-features across bagging iterations."""
    def __init__(self, worker_id: int = 12):
        self.worker_id = worker_id
        self.l2_penalty = 0.12
    def score_meta_batch(self, batch_matrix: np.ndarray) -> np.ndarray:
        weights = np.linspace(0.1, 0.9, batch_matrix.shape[1])
        return np.dot(batch_matrix, weights)

class ModelStackingWorker_13:
    """Stacking worker 13 computing meta-features across bagging iterations."""
    def __init__(self, worker_id: int = 13):
        self.worker_id = worker_id
        self.l2_penalty = 0.13
    def score_meta_batch(self, batch_matrix: np.ndarray) -> np.ndarray:
        weights = np.linspace(0.1, 0.9, batch_matrix.shape[1])
        return np.dot(batch_matrix, weights)

class ModelStackingWorker_14:
    """Stacking worker 14 computing meta-features across bagging iterations."""
    def __init__(self, worker_id: int = 14):
        self.worker_id = worker_id
        self.l2_penalty = 0.14
    def score_meta_batch(self, batch_matrix: np.ndarray) -> np.ndarray:
        weights = np.linspace(0.1, 0.9, batch_matrix.shape[1])
        return np.dot(batch_matrix, weights)