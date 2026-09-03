"""Tests for transparent risk scoring engine."""

import pytest
from backend.app.services.risk_service import risk_service


def test_normal_transaction_low_risk():
    normal_tx = {
        "amount": 750.0,
        "previous_transaction_amount": 700.0,
        "distance_from_usual_location": 3.5,
        "device_type": "Trusted Mobile App (iOS)",
        "merchant_category": "Grocery & Supermarkets",
        "timestamp": "2025-03-01 14:30:00",
        "transaction_frequency": 1,
        "account_age_days": 320
    }
    result = risk_service.calculate_risk(normal_tx, ml_probability=0.08, model_name="Random Forest")
    assert result.risk_level == "LOW"
    assert result.risk_score <= 30
    assert result.is_suspicious is False


def test_suspicious_transaction_high_risk():
    suspicious_tx = {
        "amount": 185000.0,
        "previous_transaction_amount": 1200.0,
        "distance_from_usual_location": 280.0,
        "device_type": "Unknown Device",
        "merchant_category": "Crypto & Digital Assets",
        "timestamp": "2025-03-01 03:15:00",
        "transaction_frequency": 8,
        "account_age_days": 25
    }
    result = risk_service.calculate_risk(suspicious_tx, ml_probability=0.96, model_name="Random Forest")
    assert result.risk_level == "HIGH"
    assert result.risk_score >= 71
    assert result.is_suspicious is True
    assert len(result.contributing_factors) >= 3
