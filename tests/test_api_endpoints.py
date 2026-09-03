"""Integration tests for FastAPI REST endpoints using TestClient."""

import pytest
from starlette.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_health_check_endpoint():
    res = client.get("/health")
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "healthy"


def test_auth_login_endpoint():
    res = client.post("/api/auth/login", json={"username": "sarah_analyst", "role": "Analyst"})
    assert res.status_code == 200
    data = res.json()
    assert data["authenticated"] is True
    assert data["role"] == "Analyst"


def test_list_datasets_endpoint():
    res = client.get("/api/datasets")
    assert res.status_code == 200
    assert isinstance(res.json(), list)


def test_preview_dataset_endpoint():
    res = client.get("/api/datasets/sample_synthetic_transactions.csv/preview")
    assert res.status_code == 200
    data = res.json()
    assert data["total_rows"] > 0
    assert len(data["data"]) > 0


def test_validation_endpoint():
    res = client.get("/api/validation/sample_synthetic_transactions.csv")
    assert res.status_code == 200
    data = res.json()
    assert "valid" in data
    assert len(data["checks"]) > 0


def test_risk_score_endpoint():
    payload = {
        "amount": 185000.0,
        "transaction_type": "Online",
        "merchant_category": "Crypto & Digital Assets",
        "location": "Mumbai",
        "device_type": "Unknown Device",
        "timestamp": "2025-03-01 03:15:00",
        "account_age_days": 20,
        "transaction_frequency": 7,
        "previous_transaction_amount": 1000.0,
        "distance_from_usual_location": 320.0
    }
    res = client.post("/api/risk/score", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["risk_level"] == "HIGH"
    assert data["risk_score"] >= 71


def test_suspicious_queue_endpoint():
    res = client.get("/api/suspicious")
    assert res.status_code == 200
    assert isinstance(res.json(), list)


def test_settings_endpoint():
    res = client.get("/api/settings")
    assert res.status_code == 200
    data = res.json()
    assert data["theme"]["avoid_blue"] is True
