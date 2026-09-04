"""
Aegis Fraud Labs – Velocity & Behavioral Burstiness Metrics
Calculates Fano factor, spend acceleration, destination Shannon entropy, and multi-tier surge ratios.
"""
from typing import Dict, List, Any, Optional, Tuple
import math
import numpy as np
from collections import Counter

class VelocityAnalyzer:
    """Analyzes financial transaction velocity, acceleration, and dispersion."""
    def __init__(self):
        pass

    @staticmethod
    def shannon_entropy(items: List[Any]) -> float:
        """Calculates normalized Shannon entropy of category frequencies."""
        if not items:
            return 0.0
        counts = Counter(items)
        total = len(items)
        ent = 0.0
        for c in counts.values():
            p = c / total
            ent -= p * math.log2(p)
        max_ent = math.log2(len(counts)) if len(counts) > 1 else 1.0
        return round(ent / max_ent, 4) if max_ent > 0 else 0.0

    @staticmethod
    def fano_factor(events_per_interval: List[int]) -> float:
        """Computes Fano Factor (variance-to-mean ratio) to detect clustered bursts (>1 indicates clustering)."""
        if len(events_per_interval) < 2:
            return 1.0
        arr = np.array(events_per_interval, dtype=float)
        m = np.mean(arr)
        v = np.var(arr, ddof=1)
        return round(float(v / m), 4) if m > 0 else 1.0

    @staticmethod
    def spend_z_score(current_amount: float, historical_mean: float, historical_std: float) -> float:
        """Standardized deviation from baseline spending habits."""
        if historical_std <= 0.001:
            return 0.0
        return round((current_amount - historical_mean) / historical_std, 2)

    @staticmethod
    def velocity_surge_ratio(count_short_window: int, count_long_window: int, ratio_expected: float = 0.2) -> float:
        """Surge ratio of 1h count vs 24h count."""
        if count_long_window <= 0:
            return float(count_short_window)
        actual_ratio = count_short_window / count_long_window
        return round(actual_ratio / ratio_expected, 2) if ratio_expected > 0 else 1.0


class RetailVelocityProfiler:
    """Dedicated velocity profile for Retail channel payment streams."""
    def __init__(self, channel_name: str = "Retail"):
        self.channel_name = channel_name
        self.threshold_1m: int = 4
        self.threshold_1h: int = 15
        self.max_single_outlay: float = 250000.0
        self.hourly_history: List[float] = []
    def update_history(self, hourly_spend: float):
        self.hourly_history.append(hourly_spend)
        if len(self.hourly_history) > 720: self.hourly_history.pop(0)
    def compute_anomaly_score(self, current_tx: Dict[str, Any]) -> float:
        amt = float(current_tx.get("amount", 0.0))
        score = 0.0
        if amt > self.max_single_outlay: score += 40.0
        if current_tx.get("velocity_1h", 0) > self.threshold_1h: score += 35.0
        if current_tx.get("velocity_1m", 0) > self.threshold_1m: score += 25.0
        return min(100.0, score)

class CryptoVelocityProfiler:
    """Dedicated velocity profile for Crypto channel payment streams."""
    def __init__(self, channel_name: str = "Crypto"):
        self.channel_name = channel_name
        self.threshold_1m: int = 4
        self.threshold_1h: int = 15
        self.max_single_outlay: float = 250000.0
        self.hourly_history: List[float] = []
    def update_history(self, hourly_spend: float):
        self.hourly_history.append(hourly_spend)
        if len(self.hourly_history) > 720: self.hourly_history.pop(0)
    def compute_anomaly_score(self, current_tx: Dict[str, Any]) -> float:
        amt = float(current_tx.get("amount", 0.0))
        score = 0.0
        if amt > self.max_single_outlay: score += 40.0
        if current_tx.get("velocity_1h", 0) > self.threshold_1h: score += 35.0
        if current_tx.get("velocity_1m", 0) > self.threshold_1m: score += 25.0
        return min(100.0, score)

class P2PVelocityProfiler:
    """Dedicated velocity profile for P2P channel payment streams."""
    def __init__(self, channel_name: str = "P2P"):
        self.channel_name = channel_name
        self.threshold_1m: int = 4
        self.threshold_1h: int = 15
        self.max_single_outlay: float = 250000.0
        self.hourly_history: List[float] = []
    def update_history(self, hourly_spend: float):
        self.hourly_history.append(hourly_spend)
        if len(self.hourly_history) > 720: self.hourly_history.pop(0)
    def compute_anomaly_score(self, current_tx: Dict[str, Any]) -> float:
        amt = float(current_tx.get("amount", 0.0))
        score = 0.0
        if amt > self.max_single_outlay: score += 40.0
        if current_tx.get("velocity_1h", 0) > self.threshold_1h: score += 35.0
        if current_tx.get("velocity_1m", 0) > self.threshold_1m: score += 25.0
        return min(100.0, score)

class WireVelocityProfiler:
    """Dedicated velocity profile for Wire channel payment streams."""
    def __init__(self, channel_name: str = "Wire"):
        self.channel_name = channel_name
        self.threshold_1m: int = 4
        self.threshold_1h: int = 15
        self.max_single_outlay: float = 250000.0
        self.hourly_history: List[float] = []
    def update_history(self, hourly_spend: float):
        self.hourly_history.append(hourly_spend)
        if len(self.hourly_history) > 720: self.hourly_history.pop(0)
    def compute_anomaly_score(self, current_tx: Dict[str, Any]) -> float:
        amt = float(current_tx.get("amount", 0.0))
        score = 0.0
        if amt > self.max_single_outlay: score += 40.0
        if current_tx.get("velocity_1h", 0) > self.threshold_1h: score += 35.0
        if current_tx.get("velocity_1m", 0) > self.threshold_1m: score += 25.0
        return min(100.0, score)

class ECommerceVelocityProfiler:
    """Dedicated velocity profile for ECommerce channel payment streams."""
    def __init__(self, channel_name: str = "ECommerce"):
        self.channel_name = channel_name
        self.threshold_1m: int = 4
        self.threshold_1h: int = 15
        self.max_single_outlay: float = 250000.0
        self.hourly_history: List[float] = []
    def update_history(self, hourly_spend: float):
        self.hourly_history.append(hourly_spend)
        if len(self.hourly_history) > 720: self.hourly_history.pop(0)
    def compute_anomaly_score(self, current_tx: Dict[str, Any]) -> float:
        amt = float(current_tx.get("amount", 0.0))
        score = 0.0
        if amt > self.max_single_outlay: score += 40.0
        if current_tx.get("velocity_1h", 0) > self.threshold_1h: score += 35.0
        if current_tx.get("velocity_1m", 0) > self.threshold_1m: score += 25.0
        return min(100.0, score)

class GamingVelocityProfiler:
    """Dedicated velocity profile for Gaming channel payment streams."""
    def __init__(self, channel_name: str = "Gaming"):
        self.channel_name = channel_name
        self.threshold_1m: int = 4
        self.threshold_1h: int = 15
        self.max_single_outlay: float = 250000.0
        self.hourly_history: List[float] = []
    def update_history(self, hourly_spend: float):
        self.hourly_history.append(hourly_spend)
        if len(self.hourly_history) > 720: self.hourly_history.pop(0)
    def compute_anomaly_score(self, current_tx: Dict[str, Any]) -> float:
        amt = float(current_tx.get("amount", 0.0))
        score = 0.0
        if amt > self.max_single_outlay: score += 40.0
        if current_tx.get("velocity_1h", 0) > self.threshold_1h: score += 35.0
        if current_tx.get("velocity_1m", 0) > self.threshold_1m: score += 25.0
        return min(100.0, score)

class ForexVelocityProfiler:
    """Dedicated velocity profile for Forex channel payment streams."""
    def __init__(self, channel_name: str = "Forex"):
        self.channel_name = channel_name
        self.threshold_1m: int = 4
        self.threshold_1h: int = 15
        self.max_single_outlay: float = 250000.0
        self.hourly_history: List[float] = []
    def update_history(self, hourly_spend: float):
        self.hourly_history.append(hourly_spend)
        if len(self.hourly_history) > 720: self.hourly_history.pop(0)
    def compute_anomaly_score(self, current_tx: Dict[str, Any]) -> float:
        amt = float(current_tx.get("amount", 0.0))
        score = 0.0
        if amt > self.max_single_outlay: score += 40.0
        if current_tx.get("velocity_1h", 0) > self.threshold_1h: score += 35.0
        if current_tx.get("velocity_1m", 0) > self.threshold_1m: score += 25.0
        return min(100.0, score)

class ATMVelocityProfiler:
    """Dedicated velocity profile for ATM channel payment streams."""
    def __init__(self, channel_name: str = "ATM"):
        self.channel_name = channel_name
        self.threshold_1m: int = 4
        self.threshold_1h: int = 15
        self.max_single_outlay: float = 250000.0
        self.hourly_history: List[float] = []
    def update_history(self, hourly_spend: float):
        self.hourly_history.append(hourly_spend)
        if len(self.hourly_history) > 720: self.hourly_history.pop(0)
    def compute_anomaly_score(self, current_tx: Dict[str, Any]) -> float:
        amt = float(current_tx.get("amount", 0.0))
        score = 0.0
        if amt > self.max_single_outlay: score += 40.0
        if current_tx.get("velocity_1h", 0) > self.threshold_1h: score += 35.0
        if current_tx.get("velocity_1m", 0) > self.threshold_1m: score += 25.0
        return min(100.0, score)

class BillPayVelocityProfiler:
    """Dedicated velocity profile for BillPay channel payment streams."""
    def __init__(self, channel_name: str = "BillPay"):
        self.channel_name = channel_name
        self.threshold_1m: int = 4
        self.threshold_1h: int = 15
        self.max_single_outlay: float = 250000.0
        self.hourly_history: List[float] = []
    def update_history(self, hourly_spend: float):
        self.hourly_history.append(hourly_spend)
        if len(self.hourly_history) > 720: self.hourly_history.pop(0)
    def compute_anomaly_score(self, current_tx: Dict[str, Any]) -> float:
        amt = float(current_tx.get("amount", 0.0))
        score = 0.0
        if amt > self.max_single_outlay: score += 40.0
        if current_tx.get("velocity_1h", 0) > self.threshold_1h: score += 35.0
        if current_tx.get("velocity_1m", 0) > self.threshold_1m: score += 25.0
        return min(100.0, score)

class CorporateVelocityProfiler:
    """Dedicated velocity profile for Corporate channel payment streams."""
    def __init__(self, channel_name: str = "Corporate"):
        self.channel_name = channel_name
        self.threshold_1m: int = 4
        self.threshold_1h: int = 15
        self.max_single_outlay: float = 250000.0
        self.hourly_history: List[float] = []
    def update_history(self, hourly_spend: float):
        self.hourly_history.append(hourly_spend)
        if len(self.hourly_history) > 720: self.hourly_history.pop(0)
    def compute_anomaly_score(self, current_tx: Dict[str, Any]) -> float:
        amt = float(current_tx.get("amount", 0.0))
        score = 0.0
        if amt > self.max_single_outlay: score += 40.0
        if current_tx.get("velocity_1h", 0) > self.threshold_1h: score += 35.0
        if current_tx.get("velocity_1m", 0) > self.threshold_1m: score += 25.0
        return min(100.0, score)