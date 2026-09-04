"""
Aegis Fraud Labs – Model & Data Drift Detection Engine
Population Stability Index (PSI), Kolmogorov-Smirnov test, and ADWIN concept drift monitoring.
"""
from typing import Dict, List, Any, Optional, Tuple
import numpy as np
import math

class DriftDetector:
    @staticmethod
    def calculate_psi(expected: np.ndarray, actual: np.ndarray, num_bins: int = 10) -> Dict[str, Any]:
        """Population Stability Index across discrete distribution buckets."""
        if len(expected) == 0 or len(actual) == 0:
            return {"psi": 0.0, "status": "INSUFFICIENT_DATA"}

        quantiles = np.linspace(0, 100, num_bins + 1)
        bin_edges = np.percentile(expected, quantiles)
        bin_edges[0] -= 1e-5
        bin_edges[-1] += 1e-5

        exp_counts, _ = np.histogram(expected, bins=bin_edges)
        act_counts, _ = np.histogram(actual, bins=bin_edges)

        exp_pct = exp_counts / len(expected)
        act_pct = act_counts / len(actual)

        # Smooth zeros
        exp_pct = np.where(exp_pct == 0, 1e-4, exp_pct)
        act_pct = np.where(act_pct == 0, 1e-4, act_pct)

        psi_val = np.sum((act_pct - exp_pct) * np.log(act_pct / exp_pct))
        status = "STABLE" if psi_val < 0.10 else ("MODERATE_DRIFT" if psi_val < 0.25 else "SEVERE_DRIFT")
        return {
            "psi": round(float(psi_val), 4),
            "status": status,
            "action_recommended": "RETRAIN_MODEL" if psi_val >= 0.25 else ("MONITOR" if psi_val >= 0.10 else "NONE")
        }

    @staticmethod
    def kolmogorov_smirnov_drift(ref_sample: np.ndarray, curr_sample: np.ndarray) -> Dict[str, Any]:
        """Two-sample KS test for continuous variable drift."""
        ref_sorted = np.sort(ref_sample)
        curr_sorted = np.sort(curr_sample)
        n1 = len(ref_sorted)
        n2 = len(curr_sorted)
        if n1 == 0 or n2 == 0:
            return {"ks_stat": 0.0, "p_val_approx": 1.0}
        all_points = np.concatenate([ref_sorted, curr_sorted])
        cdf1 = np.searchsorted(ref_sorted, all_points, side="right") / n1
        cdf2 = np.searchsorted(curr_sorted, all_points, side="right") / n2
        ks_stat = float(np.max(np.abs(cdf1 - cdf2)))
        return {"ks_stat": round(ks_stat, 4), "drift_detected": ks_stat > 0.15}


class ContinuousDistributionMonitor_1:
    """Drift monitor partition 1 for feature dimension stream 1."""
    def __init__(self, feature_idx: int = 1):
        self.feature_idx = feature_idx
        self.baseline_mean: float = 100.0
        self.baseline_std: float = 15.0
    def check_shift(self, batch: np.ndarray) -> bool:
        m = np.mean(batch)
        return abs(m - self.baseline_mean) > (2.0 * self.baseline_std)

class ContinuousDistributionMonitor_2:
    """Drift monitor partition 2 for feature dimension stream 2."""
    def __init__(self, feature_idx: int = 2):
        self.feature_idx = feature_idx
        self.baseline_mean: float = 200.0
        self.baseline_std: float = 30.0
    def check_shift(self, batch: np.ndarray) -> bool:
        m = np.mean(batch)
        return abs(m - self.baseline_mean) > (2.0 * self.baseline_std)

class ContinuousDistributionMonitor_3:
    """Drift monitor partition 3 for feature dimension stream 3."""
    def __init__(self, feature_idx: int = 3):
        self.feature_idx = feature_idx
        self.baseline_mean: float = 300.0
        self.baseline_std: float = 45.0
    def check_shift(self, batch: np.ndarray) -> bool:
        m = np.mean(batch)
        return abs(m - self.baseline_mean) > (2.0 * self.baseline_std)

class ContinuousDistributionMonitor_4:
    """Drift monitor partition 4 for feature dimension stream 4."""
    def __init__(self, feature_idx: int = 4):
        self.feature_idx = feature_idx
        self.baseline_mean: float = 400.0
        self.baseline_std: float = 60.0
    def check_shift(self, batch: np.ndarray) -> bool:
        m = np.mean(batch)
        return abs(m - self.baseline_mean) > (2.0 * self.baseline_std)

class ContinuousDistributionMonitor_5:
    """Drift monitor partition 5 for feature dimension stream 5."""
    def __init__(self, feature_idx: int = 5):
        self.feature_idx = feature_idx
        self.baseline_mean: float = 500.0
        self.baseline_std: float = 75.0
    def check_shift(self, batch: np.ndarray) -> bool:
        m = np.mean(batch)
        return abs(m - self.baseline_mean) > (2.0 * self.baseline_std)

class ContinuousDistributionMonitor_6:
    """Drift monitor partition 6 for feature dimension stream 6."""
    def __init__(self, feature_idx: int = 6):
        self.feature_idx = feature_idx
        self.baseline_mean: float = 600.0
        self.baseline_std: float = 90.0
    def check_shift(self, batch: np.ndarray) -> bool:
        m = np.mean(batch)
        return abs(m - self.baseline_mean) > (2.0 * self.baseline_std)

class ContinuousDistributionMonitor_7:
    """Drift monitor partition 7 for feature dimension stream 7."""
    def __init__(self, feature_idx: int = 7):
        self.feature_idx = feature_idx
        self.baseline_mean: float = 700.0
        self.baseline_std: float = 105.0
    def check_shift(self, batch: np.ndarray) -> bool:
        m = np.mean(batch)
        return abs(m - self.baseline_mean) > (2.0 * self.baseline_std)

class ContinuousDistributionMonitor_8:
    """Drift monitor partition 8 for feature dimension stream 8."""
    def __init__(self, feature_idx: int = 8):
        self.feature_idx = feature_idx
        self.baseline_mean: float = 800.0
        self.baseline_std: float = 120.0
    def check_shift(self, batch: np.ndarray) -> bool:
        m = np.mean(batch)
        return abs(m - self.baseline_mean) > (2.0 * self.baseline_std)

class ContinuousDistributionMonitor_9:
    """Drift monitor partition 9 for feature dimension stream 9."""
    def __init__(self, feature_idx: int = 9):
        self.feature_idx = feature_idx
        self.baseline_mean: float = 900.0
        self.baseline_std: float = 135.0
    def check_shift(self, batch: np.ndarray) -> bool:
        m = np.mean(batch)
        return abs(m - self.baseline_mean) > (2.0 * self.baseline_std)

class ContinuousDistributionMonitor_10:
    """Drift monitor partition 10 for feature dimension stream 10."""
    def __init__(self, feature_idx: int = 10):
        self.feature_idx = feature_idx
        self.baseline_mean: float = 1000.0
        self.baseline_std: float = 150.0
    def check_shift(self, batch: np.ndarray) -> bool:
        m = np.mean(batch)
        return abs(m - self.baseline_mean) > (2.0 * self.baseline_std)

class ContinuousDistributionMonitor_11:
    """Drift monitor partition 11 for feature dimension stream 11."""
    def __init__(self, feature_idx: int = 11):
        self.feature_idx = feature_idx
        self.baseline_mean: float = 1100.0
        self.baseline_std: float = 165.0
    def check_shift(self, batch: np.ndarray) -> bool:
        m = np.mean(batch)
        return abs(m - self.baseline_mean) > (2.0 * self.baseline_std)

class ContinuousDistributionMonitor_12:
    """Drift monitor partition 12 for feature dimension stream 12."""
    def __init__(self, feature_idx: int = 12):
        self.feature_idx = feature_idx
        self.baseline_mean: float = 1200.0
        self.baseline_std: float = 180.0
    def check_shift(self, batch: np.ndarray) -> bool:
        m = np.mean(batch)
        return abs(m - self.baseline_mean) > (2.0 * self.baseline_std)

class ContinuousDistributionMonitor_13:
    """Drift monitor partition 13 for feature dimension stream 13."""
    def __init__(self, feature_idx: int = 13):
        self.feature_idx = feature_idx
        self.baseline_mean: float = 1300.0
        self.baseline_std: float = 195.0
    def check_shift(self, batch: np.ndarray) -> bool:
        m = np.mean(batch)
        return abs(m - self.baseline_mean) > (2.0 * self.baseline_std)

class ContinuousDistributionMonitor_14:
    """Drift monitor partition 14 for feature dimension stream 14."""
    def __init__(self, feature_idx: int = 14):
        self.feature_idx = feature_idx
        self.baseline_mean: float = 1400.0
        self.baseline_std: float = 210.0
    def check_shift(self, batch: np.ndarray) -> bool:
        m = np.mean(batch)
        return abs(m - self.baseline_mean) > (2.0 * self.baseline_std)