"""Exploratory Data Analysis (EDA) endpoints."""

from typing import Dict, Any
from fastapi import APIRouter, HTTPException
from backend.app.services.eda_service import eda_service
from backend.app.services.storage_service import storage_service

router = APIRouter(prefix="/eda", tags=["EDA"])


@router.get("/{filename}", response_model=Dict[str, Any])
@router.get("/{filename}/summary", response_model=Dict[str, Any])
def get_eda_summary(filename: str):
    """Retrieve statistical distributions, aggregations, and correlations for dataset."""
    try:
        df = storage_service.load_dataset(filename)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Dataset '{filename}' not found.")

    return eda_service.compute_summary(df)
