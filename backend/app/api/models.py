"""Machine learning model training, evaluation, and registry endpoints."""

from typing import List, Dict, Any
from fastapi import APIRouter, HTTPException, Depends
from backend.app.models.schemas import ModelTrainRequest, ModelComparisonResponse
from backend.app.services.ml_service import ml_service
from backend.app.services.storage_service import storage_service
from backend.app.services.history_service import history_service
from backend.app.core.auth import require_role, RoleEnum

router = APIRouter(prefix="/models", tags=["Models"])


@router.post("/train", response_model=ModelComparisonResponse)
def train_models(
    req: ModelTrainRequest,
    current_user = Depends(require_role([RoleEnum.ADMIN]))
):
    """Train multiple ML algorithms on dataset, evaluate metrics, and select best model."""
    try:
        df = storage_service.load_dataset(req.dataset_name)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Dataset '{req.dataset_name}' not found.")

    if "is_fraud" not in df.columns:
        raise HTTPException(status_code=400, detail="Selected dataset lacks 'is_fraud' ground-truth labels for training.")

    comparison = ml_service.train_models(df, req)

    history_service.record_action(
        action=f"Trained {len(req.models_to_train)} models on '{req.dataset_name}'",
        category="MODEL",
        user=current_user.username,
        details={
            "models": [m.value for m in req.models_to_train],
            "best_model": comparison.best_model_name,
            "train_samples": comparison.total_train_samples,
            "test_samples": comparison.total_test_samples
        }
    )

    return comparison


@router.get("", response_model=List[Dict[str, Any]])
def list_trained_models():
    """List all trained model artifacts and performance metadata."""
    return storage_service.list_trained_models()


@router.post("/{model_name}/select")
def select_active_model(
    model_name: str,
    current_user = Depends(require_role([RoleEnum.ADMIN]))
):
    """Set model as active production scoring engine."""
    res = ml_service.set_active_model(model_name)
    history_service.record_action(
        action=f"Changed active scoring model to '{model_name}'",
        category="MODEL",
        user=current_user.username
    )
    return res
