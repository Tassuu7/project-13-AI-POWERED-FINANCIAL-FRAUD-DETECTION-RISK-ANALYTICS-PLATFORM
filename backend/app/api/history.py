"""Processing history and audit log endpoints."""

from typing import List, Optional
from fastapi import APIRouter, Query
from backend.app.models.schemas import AuditLogItem
from backend.app.services.history_service import history_service

router = APIRouter(prefix="/history", tags=["History"])


@router.get("", response_model=List[AuditLogItem])
def get_history(category: Optional[str] = Query(None, description="Filter by activity category")):
    """Fetch audit history records for dataset actions, model training, and predictions."""
    return history_service.get_history(category)
