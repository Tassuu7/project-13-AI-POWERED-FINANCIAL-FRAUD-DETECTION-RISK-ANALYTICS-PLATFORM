"""Feature engineering endpoints generating domain-specific fraud indicators."""

from fastapi import APIRouter, HTTPException
from backend.app.models.schemas import FeatureEngineeringResponse
from backend.app.services.feature_service import feature_service
from backend.app.services.storage_service import storage_service
from backend.app.services.history_service import history_service

router = APIRouter(prefix="/features", tags=["Feature Engineering"])


@router.post("/{filename}/generate", response_model=FeatureEngineeringResponse)
def generate_features(filename: str):
    """Compute financial fraud engineered features and persist enhanced dataset."""
    try:
        df = storage_service.load_dataset(filename)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Dataset '{filename}' not found.")

    engineered_df, response = feature_service.engineer_features(df)

    # Save engineered version
    feat_filename = f"featured_{filename}"
    storage_service.save_dataset(feat_filename, engineered_df)

    history_service.record_action(
        action=f"Engineered features for '{filename}'",
        category="DATASET",
        details={
            "initial_features": response.original_feature_count,
            "total_features": response.new_feature_count,
            "created_count": len(response.created_features)
        }
    )

    return response
