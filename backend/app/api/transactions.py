"""Transaction explorer endpoints offering search, multi-filter, and pagination."""

from typing import Optional, Dict, Any
from fastapi import APIRouter, Query, HTTPException
from backend.app.services.transaction_service import transaction_service

router = APIRouter(prefix="/transactions", tags=["Transactions"])


@router.get("")
def get_transactions(
    filename: str = Query(..., description="Target dataset name"),
    search: Optional[str] = Query(None, description="Search term for ID"),
    risk_level: Optional[str] = Query(None, description="Risk level filter"),
    transaction_type: Optional[str] = Query(None, description="Transaction type filter"),
    location: Optional[str] = Query(None, description="Location filter"),
    device_type: Optional[str] = Query(None, description="Device filter"),
    min_amount: Optional[float] = Query(None, description="Minimum amount"),
    max_amount: Optional[float] = Query(None, description="Maximum amount"),
    sort_by: str = Query("timestamp", description="Sort field"),
    sort_order: str = Query("desc", description="Sort order: asc or desc"),
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(15, ge=1, le=100, description="Page size")
):
    """Retrieve filtered, sorted, paginated transactions."""
    try:
        return transaction_service.query_transactions(
            filename=filename,
            search=search,
            risk_level=risk_level,
            transaction_type=transaction_type,
            location=location,
            device_type=device_type,
            min_amount=min_amount,
            max_amount=max_amount,
            sort_by=sort_by,
            sort_order=sort_order,
            page=page,
            page_size=page_size
        )
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Dataset '{filename}' not found.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
