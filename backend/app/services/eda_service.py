"""Exploratory Data Analysis (EDA) service computing statistics, distributions, and correlations."""

from typing import Dict, List, Any, Optional
import numpy as np
import pandas as pd
from config.logging_config import logger


class EdaService:
    def compute_summary(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Compute full statistical summary for EDA dashboard."""
        total_records = len(df)
        if total_records == 0:
            return {"error": "Dataset is empty"}

        has_fraud = "is_fraud" in df.columns
        fraud_count = int(df["is_fraud"].sum()) if has_fraud else 0
        normal_count = total_records - fraud_count
        fraud_rate = round((fraud_count / total_records) * 100.0, 2) if total_records > 0 else 0.0

        # Numeric Stats
        num_stats = {}
        for col in ["amount", "distance_from_usual_location", "transaction_frequency", "account_age_days"]:
            if col in df.columns and pd.api.types.is_numeric_dtype(df[col]):
                series = df[col].dropna()
                num_stats[col] = {
                    "mean": round(float(series.mean()), 2),
                    "median": round(float(series.median()), 2),
                    "std": round(float(series.std()), 2) if len(series) > 1 else 0.0,
                    "min": round(float(series.min()), 2),
                    "max": round(float(series.max()), 2),
                    "q25": round(float(series.quantile(0.25)), 2),
                    "q75": round(float(series.quantile(0.75)), 2)
                }

        # Amount Distribution Buckets
        amount_buckets = [
            {"range": "₹0 - ₹1,000", "min": 0, "max": 1000},
            {"range": "₹1,000 - ₹5,000", "min": 1000, "max": 5000},
            {"range": "₹5,000 - ₹25,000", "min": 5000, "max": 25000},
            {"range": "₹25,000 - ₹1,00,000", "min": 25000, "max": 100000},
            {"range": "₹1,00,000+", "min": 100000, "max": float("inf")}
        ]
        amount_dist = []
        for b in amount_buckets:
            subset = df[(df["amount"] >= b["min"]) & (df["amount"] < b["max"])]
            b_total = len(subset)
            b_fraud = int(subset["is_fraud"].sum()) if has_fraud else 0
            amount_dist.append({
                "bucket": b["range"],
                "total": b_total,
                "normal": b_total - b_fraud,
                "fraud": b_fraud,
                "fraud_rate": round((b_fraud / b_total * 100.0), 2) if b_total > 0 else 0.0
            })

        # Breakdown by Transaction Type
        by_tx_type = []
        if "transaction_type" in df.columns:
            for tx_type, group in df.groupby("transaction_type"):
                tot = len(group)
                frd = int(group["is_fraud"].sum()) if has_fraud else 0
                by_tx_type.append({
                    "category": str(tx_type),
                    "total": tot,
                    "normal": tot - frd,
                    "fraud": frd,
                    "fraud_rate": round((frd / tot) * 100.0, 2) if tot > 0 else 0.0,
                    "avg_amount": round(float(group["amount"].mean()), 2) if "amount" in group.columns else 0.0
                })

        # Breakdown by Location
        by_location = []
        if "location" in df.columns:
            for loc, group in df.groupby("location"):
                tot = len(group)
                frd = int(group["is_fraud"].sum()) if has_fraud else 0
                by_location.append({
                    "location": str(loc),
                    "total": tot,
                    "normal": tot - frd,
                    "fraud": frd,
                    "fraud_rate": round((frd / tot) * 100.0, 2) if tot > 0 else 0.0,
                    "total_amount": round(float(group["amount"].sum()), 2) if "amount" in group.columns else 0.0
                })
            by_location = sorted(by_location, key=lambda x: x["fraud_rate"], reverse=True)

        # Breakdown by Device Type
        by_device = []
        if "device_type" in df.columns:
            for dev, group in df.groupby("device_type"):
                tot = len(group)
                frd = int(group["is_fraud"].sum()) if has_fraud else 0
                by_device.append({
                    "device": str(dev),
                    "total": tot,
                    "normal": tot - frd,
                    "fraud": frd,
                    "fraud_rate": round((frd / tot) * 100.0, 2) if tot > 0 else 0.0
                })
            by_device = sorted(by_device, key=lambda x: x["fraud_rate"], reverse=True)

        # Breakdown by Hour of Day
        by_hour = []
        if "timestamp" in df.columns:
            try:
                temp_dt = pd.to_datetime(df["timestamp"], errors="coerce")
                hours = temp_dt.dt.hour.fillna(12).astype(int)
                temp_df = df.copy()
                temp_df["hour"] = hours
                for h in range(24):
                    h_group = temp_df[temp_df["hour"] == h]
                    tot = len(h_group)
                    frd = int(h_group["is_fraud"].sum()) if has_fraud else 0
                    by_hour.append({
                        "hour": f"{h:02d}:00",
                        "total": tot,
                        "normal": tot - frd,
                        "fraud": frd,
                        "fraud_rate": round((frd / tot) * 100.0, 2) if tot > 0 else 0.0
                    })
            except Exception as e:
                logger.warning(f"Error computing hourly distribution: {e}")

        # Correlation Analysis (Key numeric factors with is_fraud)
        correlations = []
        if has_fraud:
            num_cols = df.select_dtypes(include=[np.number]).columns
            for col in num_cols:
                if col != "is_fraud":
                    corr_val = df[col].corr(df["is_fraud"])
                    if not np.isnan(corr_val):
                        correlations.append({
                            "feature": col,
                            "correlation": round(float(corr_val), 3),
                            "relationship": "Positive" if corr_val > 0 else "Negative",
                            "strength": "Strong" if abs(corr_val) > 0.5 else ("Moderate" if abs(corr_val) > 0.2 else "Weak")
                        })
            correlations = sorted(correlations, key=lambda x: abs(x["correlation"]), reverse=True)

        return {
            "total_transactions": total_records,
            "normal_count": normal_count,
            "fraud_count": fraud_count,
            "fraud_rate": fraud_rate,
            "total_volume_inr": round(float(df["amount"].sum()), 2) if "amount" in df.columns else 0.0,
            "avg_amount_inr": round(float(df["amount"].mean()), 2) if "amount" in df.columns else 0.0,
            "numeric_stats": num_stats,
            "amount_distribution": amount_dist,
            "by_transaction_type": by_tx_type,
            "by_location": by_location,
            "by_device": by_device,
            "by_hour": by_hour,
            "correlations": correlations
        }


eda_service = EdaService()
