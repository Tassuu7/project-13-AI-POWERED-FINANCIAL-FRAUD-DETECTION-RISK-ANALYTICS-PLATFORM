"""Suspicious transaction investigation desk endpoints."""

from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query, Depends
from backend.app.models.schemas import SuspiciousItem, ReviewUpdateRequest
from backend.app.services.suspicious_service import suspicious_service
from backend.app.services.history_service import history_service
from backend.app.core.auth import require_role, RoleEnum

router = APIRouter(prefix="/suspicious", tags=["Suspicious Transactions"])


@router.get("", response_model=List[SuspiciousItem])
def list_suspicious(status: Optional[str] = Query(None, description="Filter by review status")):
    """List all transactions flagged for fraud investigation."""
    return suspicious_service.get_all(status)


@router.put("/{tx_id}/review", response_model=SuspiciousItem)
def update_review(
    tx_id: str,
    req: ReviewUpdateRequest,
    current_user = Depends(require_role([RoleEnum.ADMIN, RoleEnum.ANALYST]))
):
    """Update analyst investigation status and append audit notes."""
    item = suspicious_service.update_review(tx_id, req)
    if not item:
        raise HTTPException(status_code=404, detail=f"Suspicious transaction '{tx_id}' not found in review queue.")

    history_service.record_action(
        action=f"Updated investigation for {tx_id}",
        category="REVIEW",
        user=req.analyst_name or current_user.username,
        details={"status": req.review_status.value, "notes_appended": bool(req.review_notes)}
    )

    return item
