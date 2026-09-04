"""Model explainability endpoints for global and local fraud factor insights."""

from typing import List, Dict, Any, Optional
from fastapi import APIRouter, Query, Body
from backend.app.services.explainability_service import explainability_service

router = APIRouter(prefix="/explainability", tags=["Explainability"])


@router.get("/global", response_model=List[Dict[str, Any]])
def get_global_importance(model_name: Optional[str] = Query(None)):
    """Retrieve global model feature importance rankings."""
    return explainability_service.get_global_importance(model_name)


@router.post("/local", response_model=List[Dict[str, Any]])
def explain_transaction(payload: Dict[str, Any] = Body(...)):
    """Explain specific positive and negative risk contributors for an individual transaction."""
    tx_data = payload.get("transaction_data", payload) if isinstance(payload, dict) else {}
    return explainability_service.explain_local_transaction(tx_data)

