"""Data validation endpoints verifying schema integrity, data types, and nulls."""

from fastapi import APIRouter, HTTPException
from backend.app.models.schemas import ValidationReport
from backend.app.services.validation_service import validation_service
from backend.app.services.storage_service import storage_service
from backend.app.services.history_service import history_service

router = APIRouter(prefix="/validation", tags=["Validation"])


@router.get("/{filename}", response_model=ValidationReport)
def validate_dataset(filename: str):
    """Run comprehensive validation checks against a selected dataset."""
    try:
        df = storage_service.load_dataset(filename)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Dataset '{filename}' not found.")

    report = validation_service.validate(df)

    history_service.record_action(
        action=f"Validated dataset '{filename}'",
        category="DATASET",
        details={
            "valid": report.valid,
            "passed_checks": report.passed_checks,
            "failed_checks": report.failed_checks
        },
        status="SUCCESS" if report.valid else "WARNING"
    )

    return report
