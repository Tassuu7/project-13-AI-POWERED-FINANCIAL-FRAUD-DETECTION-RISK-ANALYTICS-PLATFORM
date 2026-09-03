"""Tests for data validation engine."""

import pytest
import pandas as pd
from backend.app.services.validation_service import validation_service


def test_validation_clean_dataset():
    df = pd.DataFrame({
        "transaction_id": ["TXN-1", "TXN-2", "TXN-3"],
        "customer_id": ["C1", "C2", "C3"],
        "timestamp": ["2025-01-01 10:00:00", "2025-01-01 11:00:00", "2025-01-01 12:00:00"],
        "amount": [500.0, 1200.0, 800.0],
        "transaction_type": ["Online", "POS / In-Store", "UPI Transfer"],
        "merchant_category": ["Dining & Food", "Grocery & Supermarkets", "Utilities & Bills"],
        "location": ["Mumbai", "Delhi", "Bengaluru"],
        "device_type": ["Desktop Web Browser", "Trusted Mobile App (iOS)", "Trusted Mobile App (Android)"],
        "is_fraud": [0, 0, 1]
    })
    report = validation_service.validate(df)
    assert report.valid is True
    assert report.total_records == 3
    assert report.failed_checks == 0


def test_validation_detects_negative_amounts():
    df = pd.DataFrame({
        "transaction_id": ["TXN-1", "TXN-2"],
        "customer_id": ["C1", "C2"],
        "timestamp": ["2025-01-01 10:00:00", "2025-01-01 11:00:00"],
        "amount": [500.0, -250.0],  # Negative amount!
        "transaction_type": ["Online", "POS"],
        "merchant_category": ["Dining", "Retail"],
        "location": ["Mumbai", "Delhi"],
        "device_type": ["Mobile", "Desktop"]
    })
    report = validation_service.validate(df)
    assert report.valid is False
    amount_check = next(c for c in report.checks if c.name == "Amount Integrity Check")
    assert amount_check.passed is False


def test_validation_detects_missing_required_columns():
    df = pd.DataFrame({
        "amount": [100.0],
        "location": ["Mumbai"]
    })
    report = validation_service.validate(df)
    assert report.valid is False
    req_check = next(c for c in report.checks if c.name == "Required Columns Verification")
    assert req_check.passed is False
