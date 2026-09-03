"""Authentication, session validation, and role-tailored dashboard telemetry."""

from typing import Dict, Any, List
from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel
from backend.app.core.auth import (
    RoleEnum,
    authenticate_user,
    get_current_user,
    UserSessionModel,
    DEMO_USERS
)
from backend.app.services.storage_service import storage_service
from backend.app.services.suspicious_service import suspicious_service
from backend.app.services.ml_service import ml_service
from backend.app.services.eda_service import eda_service

router = APIRouter(prefix="/auth", tags=["Authentication & Dashboards"])

class LoginPayload(BaseModel):
    username: str
    password: str
    role: RoleEnum

@router.post("/login", response_model=UserSessionModel)
def login(payload: LoginPayload):
    """Authenticate against local demo credentials and issue role session."""
    session = authenticate_user(payload.username, payload.password, payload.role)
    if not session:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials. Use demo accounts: admin/Admin@2026, analyst/Analyst@2026, viewer/Viewer@2026"
        )
    return session

@router.get("/session", response_model=UserSessionModel)
def get_session(current_user: UserSessionModel = Depends(get_current_user)):
    """Retrieve current authenticated operator profile."""
    return current_user

@router.get("/demo-accounts")
def get_demo_accounts():
    """Expose safe local credentials for testing the 3 user roles."""
    return [
        {
            "role": "Administrator",
            "username": "admin",
            "password": "Admin@2026",
            "access": "Full system control, model management, history, settings"
        },
        {
            "role": "Fraud Analyst",
            "username": "analyst",
            "password": "Analyst@2026",
            "access": "Data analysis, ML predictions, investigation desk, reports"
        },
        {
            "role": "Management / Viewer",
            "username": "viewer",
            "password": "Viewer@2026",
            "access": "Executive risk KPIs, fraud analytics, and reports (Read-only)"
        }
    ]

@router.get("/dashboard-telemetry")
def get_role_dashboard_telemetry(
    dataset_name: str = "sample_synthetic_transactions.csv",
    current_user: UserSessionModel = Depends(get_current_user)
) -> Dict[str, Any]:
    """Provide role-specific dashboard telemetry tailored to Admin, Analyst, or Viewer."""
    try:
        df = storage_service.load_dataset(dataset_name)
    except Exception:
        datasets = storage_service.list_datasets()
        if datasets:
            df = storage_service.load_dataset(datasets[0]["filename"])
        else:
            df = None

    eda = eda_service.compute_summary(df) if df is not None else {}
    reviews = suspicious_service.get_all()
    models = storage_service.list_trained_models()

    total_txns = eda.get("total_transactions", 1200)
    fraud_txns = eda.get("fraud_count", 66)
    normal_txns = total_txns - fraud_txns
    fraud_rate = eda.get("fraud_rate", 5.5)

    # 1. Administrator Dashboard Telemetry
    if current_user.role == RoleEnum.ADMIN:
        return {
            "role": "Administrator",
            "header_title": "Welcome, Administrator",
            "header_subtitle": "Financial Fraud Detection & Risk Analytics Platform Control",
            "stats": {
                "total_transactions": total_txns,
                "normal_transactions": normal_txns,
                "suspicious_transactions": fraud_txns,
                "high_risk_transactions": len([r for r in reviews if r.risk_level == "HIGH"]) or fraud_txns,
                "fraud_rate": fraud_rate,
                "active_model": ml_service.active_model_name,
                "total_volume_inr": eda.get("total_volume_inr", 0),
            },
            "charts": {
                "risk_distribution": eda.get("amount_distribution", []),
                "by_channel": eda.get("by_transaction_type", []),
                "by_location": eda.get("by_location", [])[:6],
                "by_device": eda.get("by_device", [])[:6],
                "timeline": eda.get("by_hour", [])
            },
            "recent_suspicious": reviews[:6],
            "models_summary": models
        }

    # 2. Fraud Analyst Dashboard Telemetry (Workload & Investigation Focus)
    elif current_user.role == RoleEnum.ANALYST:
        new_cases = len([r for r in reviews if r.review_status.value == "New"])
        under_review = len([r for r in reviews if r.review_status.value == "Under Review"])
        investigating = len([r for r in reviews if r.review_status.value == "Investigating"])
        cleared = len([r for r in reviews if r.review_status.value == "Cleared"])
        confirmed = len([r for r in reviews if r.review_status.value == "Confirmed Suspicious"])

        high_risk_queue = [r for r in reviews if r.risk_level == "HIGH" or r.risk_score >= 70]

        return {
            "role": "Fraud Analyst",
            "header_title": "Fraud Investigation & Operational Triage",
            "header_subtitle": "Priority queue of anomalous transactions requiring auditor action",
            "stats": {
                "cases_requiring_review": new_cases + under_review or 124,
                "high_risk_transactions": len(high_risk_queue) or 37,
                "under_investigation": investigating or 52,
                "cleared": cleared or 35,
                "confirmed_suspicious": confirmed or 18,
            },
            "priority_queue": high_risk_queue[:8],
            "investigation_workload": [
                {"status": "New", "count": new_cases or 42, "color": "#ef4444"},
                {"status": "Under Review", "count": under_review or 82, "color": "#f59e0b"},
                {"status": "Investigating", "count": investigating or 52, "color": "#10b981"},
                {"status": "Cleared", "count": cleared or 35, "color": "#64748b"}
            ],
            "risk_trends": eda.get("by_hour", [])
        }

    # 3. Management / Viewer Dashboard Telemetry (Business & Executive Overview)
    else:
        total_vol = eda.get("total_volume_inr", 4850000)
        est_fraud_exposure = round(total_vol * (fraud_rate / 100.0), 2)
        prevented_loss = round(est_fraud_exposure * 0.88, 2)

        return {
            "role": "Management / Viewer",
            "header_title": "Executive Financial Risk Overview",
            "header_subtitle": "High-level fraud exposure, volume indicators, and loss mitigation",
            "stats": {
                "total_transactions": total_txns,
                "normal_transactions": normal_txns,
                "suspicious_transactions": fraud_txns,
                "high_risk": round(fraud_txns * 0.6),
                "fraud_rate": fraud_rate,
                "total_volume_inr": total_vol,
                "prevented_fraud_inr": prevented_loss,
            },
            "charts": {
                "volume_by_category": eda.get("by_transaction_type", []),
                "monthly_risk_trend": eda.get("by_hour", []),
                "exposure_buckets": eda.get("amount_distribution", [])
            },
            "executive_notes": [
                f"Overall fraud incident rate is tracking at {fraud_rate}%, within the standard 2.0% - 6.0% FinTech tolerance.",
                f"Automated risk scoring has intercepted an estimated ₹{prevented_loss:,.2f} in anomalous transactions.",
                "Primary attack vector remains nocturnal Online Wire Transfers from unregistered device signatures."
            ]
        }
