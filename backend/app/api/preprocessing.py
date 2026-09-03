"""Data preprocessing endpoints handling cleaning, encoding, scaling, and splitting."""

from fastapi import APIRouter, HTTPException
from backend.app.models.schemas import PreprocessingRequest, PreprocessingResult
from backend.app.services.preprocessing_service import preprocessing_service
from backend.app.services.storage_service import storage_service
from backend.app.services.history_service import history_service

router = APIRouter(prefix="/preprocessing", tags=["Preprocessing"])


@router.post("/run", response_model=PreprocessingResult)
def run_preprocessing(req: PreprocessingRequest):
    """Execute complete preprocessing pipeline and persist preprocessed dataset."""
    try:
        df = storage_service.load_dataset(req.filename)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Dataset '{req.filename}' not found.")

    processed_df, result = preprocessing_service.preprocess(df, req)

    # Save preprocessed version
    clean_name = f"preprocessed_{req.filename}"
    storage_service.save_dataset(clean_name, processed_df)

    history_service.record_action(
        action=f"Preprocessed dataset '{req.filename}'",
        category="DATASET",
        details={
            "original_shape": result.original_shape,
            "processed_shape": result.processed_shape,
            "duplicates_removed": result.duplicates_removed,
            "missing_handled": result.missing_values_handled
        }
    )

    return result
