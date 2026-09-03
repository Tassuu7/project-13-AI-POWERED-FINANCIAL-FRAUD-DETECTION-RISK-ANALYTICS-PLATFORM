"""Tests for synthetic transaction generator."""

import pytest
import pandas as pd
from backend.app.models.schemas import SyntheticGenerateRequest
from backend.app.services.synthetic_generator import synthetic_generator


def test_synthetic_data_generation_reproducibility():
    req1 = SyntheticGenerateRequest(num_records=100, fraud_percentage=5.0, random_seed=99)
    req2 = SyntheticGenerateRequest(num_records=100, fraud_percentage=5.0, random_seed=99)

    df1 = synthetic_generator.generate(req1)
    df2 = synthetic_generator.generate(req2)

    assert len(df1) == 100
    assert len(df2) == 100
    assert df1["amount"].tolist() == df2["amount"].tolist()
    assert df1["is_fraud"].sum() == df2["is_fraud"].sum()


def test_synthetic_data_schema():
    req = SyntheticGenerateRequest(num_records=50, fraud_percentage=8.0, random_seed=42)
    df = synthetic_generator.generate(req)

    expected_cols = [
        "transaction_id", "customer_id", "timestamp", "amount",
        "transaction_type", "merchant_category", "location", "device_type",
        "account_age_days", "transaction_frequency", "previous_transaction_amount",
        "distance_from_usual_location", "is_fraud"
    ]
    for col in expected_cols:
        assert col in df.columns

    # Verify amounts are positive
    assert (df["amount"] > 0).all()
    # Verify fraud label is binary
    assert set(df["is_fraud"].unique()).issubset({0, 1})
