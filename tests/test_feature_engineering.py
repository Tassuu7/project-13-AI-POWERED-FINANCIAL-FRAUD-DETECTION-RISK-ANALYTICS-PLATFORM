"""Tests for feature engineering service."""

import pytest
import pandas as pd
from backend.app.services.feature_service import feature_service


def test_feature_engineering_creates_expected_indicators():
    df = pd.DataFrame({
        "transaction_id": ["T1", "T2"],
        "customer_id": ["C1", "C2"],
        "timestamp": ["2025-01-01 03:15:00", "2025-01-01 14:30:00"],
        "amount": [185000.0, 450.0],
        "previous_transaction_amount": [1000.0, 500.0],
        "transaction_type": ["Online", "POS / In-Store"],
        "merchant_category": ["Luxury Goods & Jewelry", "Dining & Food"],
        "location": ["Mumbai", "Hyderabad"],
        "device_type": ["Unknown Device", "Trusted Mobile App (iOS)"],
        "account_age_days": [20, 450],
        "transaction_frequency": [7, 1],
        "distance_from_usual_location": [240.0, 5.0]
    })

    engineered_df, response = feature_service.engineer_features(df)

    # T1 is high risk (night, high amount, distant location, unknown device, rapid velocity)
    t1 = engineered_df.iloc[0]
    assert t1["is_night_transaction"] == 1
    assert t1["is_high_value"] == 1
    assert t1["distance_anomaly"] == 1
    assert t1["suspicious_device_flag"] == 1
    assert t1["high_velocity_flag"] == 1
    assert t1["account_youth_risk"] == 1
    assert t1["compound_risk_index"] > 3

    # T2 is low risk
    t2 = engineered_df.iloc[1]
    assert t2["is_night_transaction"] == 0
    assert t2["is_high_value"] == 0
    assert t2["distance_anomaly"] == 0
    assert t2["suspicious_device_flag"] == 0
    assert t2["high_velocity_flag"] == 0
