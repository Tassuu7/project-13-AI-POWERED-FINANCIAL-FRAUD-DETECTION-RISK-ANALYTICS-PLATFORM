"""Integration tests for FastAPI REST endpoints and Role-Based Access Control (RBAC)."""

import pytest
from starlette.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_health_check_endpoint():
    res = client.get("/health")
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "healthy"


def test_auth_login_success_and_failure():
    # Admin login
    res = client.post("/api/auth/login", json={"username": "admin", "password": "Admin@2026", "role": "Administrator"})
    assert res.status_code == 200
    data = res.json()
    assert data["role"] == "Administrator"
    assert "token" in data

    # Analyst login
    res = client.post("/api/auth/login", json={"username": "analyst", "password": "Analyst@2026", "role": "Fraud Analyst"})
    assert res.status_code == 200
    assert res.json()["role"] == "Fraud Analyst"

    # Viewer login
    res = client.post("/api/auth/login", json={"username": "viewer", "password": "Viewer@2026", "role": "Management / Viewer"})
    assert res.status_code == 200
    assert res.json()["role"] == "Management / Viewer"

    # Wrong password failure
    res_bad = client.post("/api/auth/login", json={"username": "admin", "password": "WrongPassword!", "role": "Administrator"})
    assert res_bad.status_code == 401


def test_rbac_role_permissions():
    # 1. Admin can access settings
    res_admin = client.get("/api/settings", headers={"X-User-Role": "Administrator"})
    assert res_admin.status_code == 200

    # 2. Analyst CANNOT access settings -> 403 Forbidden
    res_analyst = client.get("/api/settings", headers={"X-User-Role": "Fraud Analyst"})
    assert res_analyst.status_code == 403

    # 3. Viewer CANNOT access settings -> 403 Forbidden
    res_viewer = client.get("/api/settings", headers={"X-User-Role": "Management / Viewer"})
    assert res_viewer.status_code == 403

    # 4. Viewer CANNOT modify suspicious transactions -> 403 Forbidden
    res_viewer_mod = client.put(
        "/api/suspicious/TXN-100000/review",
        json={"review_status": "Cleared", "review_notes": "Attempted viewer modification"},
        headers={"X-User-Role": "Management / Viewer"}
    )
    assert res_viewer_mod.status_code == 403


def test_role_tailored_dashboard_telemetry():
    # Admin dashboard telemetry
    res_admin = client.get("/api/auth/dashboard-telemetry", headers={"X-User-Role": "Administrator"})
    assert res_admin.status_code == 200
    assert res_admin.json()["role"] == "Administrator"
    assert "active_model" in res_admin.json()["stats"]

    # Analyst dashboard telemetry
    res_analyst = client.get("/api/auth/dashboard-telemetry", headers={"X-User-Role": "Fraud Analyst"})
    assert res_analyst.status_code == 200
    assert res_analyst.json()["role"] == "Fraud Analyst"
    assert "cases_requiring_review" in res_analyst.json()["stats"]

    # Viewer dashboard telemetry
    res_viewer = client.get("/api/auth/dashboard-telemetry", headers={"X-User-Role": "Management / Viewer"})
    assert res_viewer.status_code == 200
    assert res_viewer.json()["role"] == "Management / Viewer"
    assert "prevented_fraud_inr" in res_viewer.json()["stats"]


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
    assert data["risk_score"] >= 70
    assert data["risk_level"] == "HIGH"
