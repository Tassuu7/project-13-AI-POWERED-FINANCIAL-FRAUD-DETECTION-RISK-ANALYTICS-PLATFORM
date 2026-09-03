"""Tests for data preprocessing service."""

import pytest
import pandas as pd
import numpy as np
from backend.app.models.schemas import PreprocessingRequest
from backend.app.services.preprocessing_service import preprocessing_service


def test_preprocessing_handles_nulls_and_duplicates():
    df = pd.DataFrame({
        "transaction_id": ["T1", "T1", "T2", "T3"],  # T1 duplicate
        "customer_id": ["C1", "C1", "C2", "C3"],
        "timestamp": ["2025-01-01 10:00:00", "2025-01-01 10:00:00", "2025-01-01 11:00:00", "2025-01-01 12:00:00"],
        "amount": [100.0, 100.0, np.nan, 300.0],  # NaN in T2
        "transaction_type": ["Online", "Online", "POS", "UPI"],
        "merchant_category": ["Food", "Food", "Tech", "Food"],
        "location": ["Mumbai", "Mumbai", "Pune", "Goa"],
        "device_type": ["Mobile", "Mobile", "Desktop", "Web"],
        "account_age_days": [100, 100, 200, 300],
        "transaction_frequency": [1, 1, 2, 3],
        "distance_from_usual_location": [5.0, 5.0, 10.0, 15.0]
    })

    req = PreprocessingRequest(
        filename="test_mock.csv",
        handle_missing="median_mode",
        handle_duplicates=True,
        test_size=0.33
    )

    processed_df, result = preprocessing_service.preprocess(df, req)

    assert result.duplicates_removed == 1
    assert result.missing_values_handled == 1
    assert processed_df["amount"].isnull().sum() == 0
    assert len(processed_df) == 3
