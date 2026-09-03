"""Risk engine configuration and scoring endpoints."""

from typing import Dict, Any
from fastapi import APIRouter
from backend.app.models.schemas import SingleTransactionInput, PredictionResult
from backend.app.services.risk_service import risk_service
from backend.app.services.ml_service import ml_service
from config.settings import settings

router = APIRouter(prefix="/risk", tags=["Risk Engine"])


@router.get("/thresholds")
def get_risk_thresholds():
    """Retrieve platform risk score bands and anomaly criteria."""
    return {
        "bands": {
            "low": {"min": 0, "max": settings.RISK_LOW_MAX, "label": "Low Risk", "action": "Standard Approval"},
            "medium": {"min": settings.RISK_LOW_MAX + 1, "max": settings.RISK_MEDIUM_MAX, "label": "Medium Risk", "action": "Step-up Verification"},
            "high": {"min": settings.RISK_MEDIUM_MAX + 1, "max": 100, "label": "High Risk", "action": "Hold & Route to Review"}
        },
        "weights": {
            "ml_probability": 0.55,
            "heuristic_rules": 0.45
        }
    }


@router.post("/score", response_model=PredictionResult)
def calculate_score(req: SingleTransactionInput):
    """Direct transparent risk scoring calculation."""
    tx_dict = req.model_dump()
    is_suspicious, prob, used_model = ml_service.predict_single(tx_dict)
    return risk_service.calculate_risk(tx_dict, prob, used_model)
