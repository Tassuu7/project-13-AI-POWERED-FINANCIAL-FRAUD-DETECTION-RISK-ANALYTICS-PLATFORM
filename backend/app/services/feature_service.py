"""Feature engineering pipeline computing domain-specific fraud indicators and explaining their logic."""

from typing import Dict, List, Tuple, Any
import numpy as np
import pandas as pd
from backend.app.models.schemas import FeatureSummary, FeatureEngineeringResponse
from config.logging_config import logger

FEATURE_DEFINITIONS = [
    {
        "name": "amount_to_prev_ratio",
        "type": "Numerical Ratio",
        "description": "Ratio of current transaction amount to customer's previous transaction amount. Surges above 3.0x signal potential account takeover."
    },
    {
        "name": "amount_deviation",
        "type": "Numerical Currency",
        "description": "Absolute difference between transaction amount and customer baseline mean. Highlights anomalous spending spikes."
    },
    {
        "name": "is_night_transaction",
        "type": "Binary Indicator",
        "description": "Flag for transactions between 01:00 AM and 05:00 AM, hours statistically associated with unauthorized automated card drains."
    },
    {
        "name": "is_high_value",
        "type": "Binary Indicator",
        "description": "Flags transactions exceeding ₹50,000 requiring higher authorization scrutiny."
    },
    {
        "name": "high_velocity_flag",
        "type": "Binary Indicator",
        "description": "Flags elevated transaction frequency within a short time window (frequency >= 5), characteristic of card testing or automated bots."
    },
    {
        "name": "distance_anomaly",
        "type": "Binary Indicator",
        "description": "Flags transactions occurring more than 100 km away from the customer's typical geographic baseline."
    },
    {
        "name": "suspicious_device_flag",
        "type": "Binary Indicator",
        "description": "Identifies unfamiliar, newly emulated, or unverified browser/device fingerprints."
    },
    {
        "name": "account_youth_risk",
        "type": "Binary Indicator",
        "description": "Highlights accounts less than 60 days old, which historically exhibit higher bust-out and identity fraud rates."
    },
    {
        "name": "compound_risk_index",
        "type": "Composite Score",
        "description": "Heuristic combination of high value, night hours, distance, and suspicious device to capture multi-vector attacks."
    }
]


class FeatureEngineeringService:
    def engineer_features(self, df: pd.DataFrame) -> Tuple[pd.DataFrame, FeatureEngineeringResponse]:
        original_count = df.shape[1]
        engineered_df = df.copy()

        # 1. Amount to previous ratio
        if "amount" in engineered_df.columns and "previous_transaction_amount" in engineered_df.columns:
            prev = engineered_df["previous_transaction_amount"].replace(0, 100.0)
            engineered_df["amount_to_prev_ratio"] = (engineered_df["amount"] / prev).round(2)
        else:
            engineered_df["amount_to_prev_ratio"] = 1.0

        # 2. Amount deviation from customer mean
        if "amount" in engineered_df.columns and "customer_id" in engineered_df.columns:
            cust_means = engineered_df.groupby("customer_id")["amount"].transform("mean")
            engineered_df["amount_deviation"] = (engineered_df["amount"] - cust_means).round(2)
        elif "amount" in engineered_df.columns:
            mean_amt = engineered_df["amount"].mean()
            engineered_df["amount_deviation"] = (engineered_df["amount"] - mean_amt).round(2)
        else:
            engineered_df["amount_deviation"] = 0.0

        # 3. Night hour indicator (01:00 AM - 05:00 AM)
        if "hour" in engineered_df.columns:
            engineered_df["is_night_transaction"] = engineered_df["hour"].apply(lambda h: 1 if 1 <= h <= 5 else 0)
        elif "timestamp" in engineered_df.columns:
            dt = pd.to_datetime(engineered_df["timestamp"], errors="coerce")
            engineered_df["is_night_transaction"] = dt.dt.hour.apply(lambda h: 1 if 1 <= h <= 5 else 0)
        else:
            engineered_df["is_night_transaction"] = 0

        # 4. High Value Transaction
        if "amount" in engineered_df.columns:
            engineered_df["is_high_value"] = (engineered_df["amount"] >= 50000.0).astype(int)
        else:
            engineered_df["is_high_value"] = 0

        # 5. High Velocity Flag
        if "transaction_frequency" in engineered_df.columns:
            engineered_df["high_velocity_flag"] = (engineered_df["transaction_frequency"] >= 5).astype(int)
        else:
            engineered_df["high_velocity_flag"] = 0

        # 6. Distance Anomaly
        if "distance_from_usual_location" in engineered_df.columns:
            engineered_df["distance_anomaly"] = (engineered_df["distance_from_usual_location"] >= 100.0).astype(int)
        else:
            engineered_df["distance_anomaly"] = 0

        # 7. Suspicious Device Flag
        if "device_type" in engineered_df.columns:
            suspicious_devices = {"Unknown Device", "New Emulated Device", "Mobile Web Browser"}
            engineered_df["suspicious_device_flag"] = engineered_df["device_type"].apply(
                lambda d: 1 if str(d) in suspicious_devices else 0
            )
        else:
            engineered_df["suspicious_device_flag"] = 0

        # 8. Account Youth Risk
        if "account_age_days" in engineered_df.columns:
            engineered_df["account_youth_risk"] = (engineered_df["account_age_days"] < 60).astype(int)
        else:
            engineered_df["account_youth_risk"] = 0

        # 9. Compound Risk Index (Heuristic 0-4)
        engineered_df["compound_risk_index"] = (
            engineered_df["is_high_value"] * 2 +
            engineered_df["is_night_transaction"] +
            engineered_df["distance_anomaly"] +
            engineered_df["suspicious_device_flag"]
        )

        created_features = [
            FeatureSummary(
                feature_name=f["name"],
                feature_type=f["type"],
                description=f["description"],
                importance_rank=idx + 1
            )
            for idx, f in enumerate(FEATURE_DEFINITIONS)
        ]

        # Preview of created features
        sample_cols = [f["name"] for f in FEATURE_DEFINITIONS if f["name"] in engineered_df.columns]
        sample_records = engineered_df[sample_cols].head(5).to_dict(orient="records")

        response = FeatureEngineeringResponse(
            original_feature_count=original_count,
            new_feature_count=engineered_df.shape[1],
            created_features=created_features,
            sample_preview=sample_records
        )

        logger.info(f"Engineered {len(created_features)} financial fraud features.")
        return engineered_df, response


feature_service = FeatureEngineeringService()
