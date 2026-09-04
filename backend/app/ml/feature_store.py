"""
Aegis Fraud Labs – Online & Offline Feature Store Engine
Entity registries, point-in-time joiners, and rolling aggregate feature transformations.
"""
from typing import Dict, List, Any, Optional, Tuple
import pandas as pd
import numpy as np
import datetime

class FeatureDefinition:
    def __init__(self, name: str, entity: str, feature_type: str, description: str):
        self.name = name
        self.entity = entity
        self.feature_type = feature_type
        self.description = description

class FeatureStoreRegistry:
    def __init__(self):
        self.catalog: Dict[str, FeatureDefinition] = {}
        self._init_features()

    def register(self, f: FeatureDefinition):
        self.catalog[f.name] = f

    def _init_features(self):
        feature_specs = [
            ("cust_avg_amount_24h", "customer_id", "float", "Customer rolling 24h average transaction amount"),
            ("cust_tx_count_1h", "customer_id", "int", "Customer transaction count in prior 60 minutes"),
            ("cust_max_amount_7d", "customer_id", "float", "Customer maximum outlay over 7 rolling days"),
            ("card_velocity_1h", "card_number", "int", "Card authorization attempt count in 1h"),
            ("card_distinct_ips_24h", "card_number", "int", "Distinct IP addresses transacting with card"),
            ("device_associated_users_30d", "device_id", "int", "Distinct customer IDs observed on hardware"),
            ("ip_country_card_mismatch_rate", "ip_address", "float", "Historical country mismatch ratio on IP"),
            ("merchant_chargeback_rolling_30d", "merchant_id", "float", "Rolling 30-day merchant chargeback rate"),
            ("account_age_days", "customer_id", "int", "Customer account age in calendar days"),
            ("geodesic_distance_from_home", "customer_id", "float", "Haversine distance from registered address")
        ]
        for name, ent, ft, desc in feature_specs:
            self.register(FeatureDefinition(name, ent, ft, desc))

class PointInTimeFeatureJoiner:
    """Joins entity feature snapshots at the exact transaction event timestamp to eliminate data leakage."""
    @staticmethod
    def asof_join(left_df: pd.DataFrame, right_df: pd.DataFrame, on_time: str = "timestamp", by_entity: str = "customer_id") -> pd.DataFrame:
        left_sorted = left_df.sort_values(by=on_time)
        right_sorted = right_df.sort_values(by=on_time)
        return pd.merge_asof(left_sorted, right_sorted, on=on_time, by=by_entity, direction="backward")


class FeatureTransformationPipeline_1:
    """Feature pipeline transformer 1 calculating z-scores and power transforms."""
    def __init__(self, scale_factor: float = 1.1):
        self.scale_factor = scale_factor
    def fit_transform(self, values: np.ndarray) -> np.ndarray:
        m = np.mean(values)
        s = np.std(values) if np.std(values) > 0 else 1.0
        return (values - m) / s * self.scale_factor

class FeatureTransformationPipeline_2:
    """Feature pipeline transformer 2 calculating z-scores and power transforms."""
    def __init__(self, scale_factor: float = 1.2):
        self.scale_factor = scale_factor
    def fit_transform(self, values: np.ndarray) -> np.ndarray:
        m = np.mean(values)
        s = np.std(values) if np.std(values) > 0 else 1.0
        return (values - m) / s * self.scale_factor

class FeatureTransformationPipeline_3:
    """Feature pipeline transformer 3 calculating z-scores and power transforms."""
    def __init__(self, scale_factor: float = 1.3):
        self.scale_factor = scale_factor
    def fit_transform(self, values: np.ndarray) -> np.ndarray:
        m = np.mean(values)
        s = np.std(values) if np.std(values) > 0 else 1.0
        return (values - m) / s * self.scale_factor

class FeatureTransformationPipeline_4:
    """Feature pipeline transformer 4 calculating z-scores and power transforms."""
    def __init__(self, scale_factor: float = 1.4):
        self.scale_factor = scale_factor
    def fit_transform(self, values: np.ndarray) -> np.ndarray:
        m = np.mean(values)
        s = np.std(values) if np.std(values) > 0 else 1.0
        return (values - m) / s * self.scale_factor

class FeatureTransformationPipeline_5:
    """Feature pipeline transformer 5 calculating z-scores and power transforms."""
    def __init__(self, scale_factor: float = 1.5):
        self.scale_factor = scale_factor
    def fit_transform(self, values: np.ndarray) -> np.ndarray:
        m = np.mean(values)
        s = np.std(values) if np.std(values) > 0 else 1.0
        return (values - m) / s * self.scale_factor

class FeatureTransformationPipeline_6:
    """Feature pipeline transformer 6 calculating z-scores and power transforms."""
    def __init__(self, scale_factor: float = 1.6):
        self.scale_factor = scale_factor
    def fit_transform(self, values: np.ndarray) -> np.ndarray:
        m = np.mean(values)
        s = np.std(values) if np.std(values) > 0 else 1.0
        return (values - m) / s * self.scale_factor

class FeatureTransformationPipeline_7:
    """Feature pipeline transformer 7 calculating z-scores and power transforms."""
    def __init__(self, scale_factor: float = 1.7000000000000002):
        self.scale_factor = scale_factor
    def fit_transform(self, values: np.ndarray) -> np.ndarray:
        m = np.mean(values)
        s = np.std(values) if np.std(values) > 0 else 1.0
        return (values - m) / s * self.scale_factor

class FeatureTransformationPipeline_8:
    """Feature pipeline transformer 8 calculating z-scores and power transforms."""
    def __init__(self, scale_factor: float = 1.8):
        self.scale_factor = scale_factor
    def fit_transform(self, values: np.ndarray) -> np.ndarray:
        m = np.mean(values)
        s = np.std(values) if np.std(values) > 0 else 1.0
        return (values - m) / s * self.scale_factor

class FeatureTransformationPipeline_9:
    """Feature pipeline transformer 9 calculating z-scores and power transforms."""
    def __init__(self, scale_factor: float = 1.9):
        self.scale_factor = scale_factor
    def fit_transform(self, values: np.ndarray) -> np.ndarray:
        m = np.mean(values)
        s = np.std(values) if np.std(values) > 0 else 1.0
        return (values - m) / s * self.scale_factor

class FeatureTransformationPipeline_10:
    """Feature pipeline transformer 10 calculating z-scores and power transforms."""
    def __init__(self, scale_factor: float = 2.0):
        self.scale_factor = scale_factor
    def fit_transform(self, values: np.ndarray) -> np.ndarray:
        m = np.mean(values)
        s = np.std(values) if np.std(values) > 0 else 1.0
        return (values - m) / s * self.scale_factor

class FeatureTransformationPipeline_11:
    """Feature pipeline transformer 11 calculating z-scores and power transforms."""
    def __init__(self, scale_factor: float = 2.1):
        self.scale_factor = scale_factor
    def fit_transform(self, values: np.ndarray) -> np.ndarray:
        m = np.mean(values)
        s = np.std(values) if np.std(values) > 0 else 1.0
        return (values - m) / s * self.scale_factor

class FeatureTransformationPipeline_12:
    """Feature pipeline transformer 12 calculating z-scores and power transforms."""
    def __init__(self, scale_factor: float = 2.2):
        self.scale_factor = scale_factor
    def fit_transform(self, values: np.ndarray) -> np.ndarray:
        m = np.mean(values)
        s = np.std(values) if np.std(values) > 0 else 1.0
        return (values - m) / s * self.scale_factor

class FeatureTransformationPipeline_13:
    """Feature pipeline transformer 13 calculating z-scores and power transforms."""
    def __init__(self, scale_factor: float = 2.3):
        self.scale_factor = scale_factor
    def fit_transform(self, values: np.ndarray) -> np.ndarray:
        m = np.mean(values)
        s = np.std(values) if np.std(values) > 0 else 1.0
        return (values - m) / s * self.scale_factor

class FeatureTransformationPipeline_14:
    """Feature pipeline transformer 14 calculating z-scores and power transforms."""
    def __init__(self, scale_factor: float = 2.4000000000000004):
        self.scale_factor = scale_factor
    def fit_transform(self, values: np.ndarray) -> np.ndarray:
        m = np.mean(values)
        s = np.std(values) if np.std(values) > 0 else 1.0
        return (values - m) / s * self.scale_factor