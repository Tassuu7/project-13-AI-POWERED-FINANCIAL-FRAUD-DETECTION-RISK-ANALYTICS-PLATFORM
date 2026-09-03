"""Model explainability endpoints for global and local fraud factor insights."""

from typing import List, Dict, Any, Optional
from fastapi import APIRouter, Query
from backend.app.services.explainability_service import explainability_service
from backend.app.models.schemas import SingleTransactionInput

router = APIRouter(prefix="/explainability", tags=["Explainability"])


@router.get("/global", response_model=List[Dict[str, Any]])
def get_global_importance(model_name: Optional[str] = Query(None)):
    """Retrieve global model feature importance rankings."""
    return explainability_service.get_global_importance(model_name)


@router.post("/local", response_model=List[Dict[str, Any]])
def explain_transaction(tx: SingleTransactionInput):
    """Explain specific positive and negative risk contributors for an individual transaction."""
    return explainability_service.explain_local_transaction(tx.model_dump())
