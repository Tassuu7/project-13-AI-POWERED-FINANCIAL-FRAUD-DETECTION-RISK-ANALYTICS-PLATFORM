"""Platform settings and configuration endpoints."""

import json
from typing import Dict, Any
from fastapi import APIRouter, Depends
from config.settings import settings
from backend.app.services.ml_service import ml_service
from backend.app.services.history_service import history_service
from backend.app.core.auth import require_role, RoleEnum

router = APIRouter(prefix="/settings", tags=["Settings"])


@router.get("")
def get_settings(current_user = Depends(require_role([RoleEnum.ADMIN]))):
    """Retrieve platform configuration, risk thresholds, and active model status."""
    return {
        "project_name": settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION,
        "active_model": ml_service.active_model_name,
        "risk_thresholds": {
            "low_max": settings.RISK_LOW_MAX,
            "medium_max": settings.RISK_MEDIUM_MAX,
            "high_min": settings.RISK_MEDIUM_MAX + 1
        },
        "storage": {
            "data_dir": str(settings.DATA_DIR),
            "models_dir": str(settings.MODELS_DIR),
            "reports_dir": str(settings.REPORTS_DIR),
            "exports_dir": str(settings.EXPORTS_DIR),
            "database_connected": False,
            "persistence_mode": "Local File System (JSON/CSV/Joblib)"
        },
        "theme": {
            "palette": "Dark Obsidian & Slate",
            "accent": "Emerald Green",
            "avoid_blue": True
        }
    }


@router.post("/thresholds")
def update_thresholds(
    payload: Dict[str, int],
    current_user = Depends(require_role([RoleEnum.ADMIN]))
):
    """Update risk scoring threshold boundaries."""
    if "low_max" in payload:
        settings.RISK_LOW_MAX = payload["low_max"]
    if "medium_max" in payload:
        settings.RISK_MEDIUM_MAX = payload["medium_max"]

    config_path = settings.BASE_DIR / "config" / "risk_thresholds.json"
    with open(config_path, "w") as f:
        json.dump({
            "low_max": settings.RISK_LOW_MAX,
            "medium_max": settings.RISK_MEDIUM_MAX,
            "high_min": settings.RISK_MEDIUM_MAX + 1
        }, f, indent=2)

    history_service.record_action(
        action=f"Updated risk thresholds: Low Max={settings.RISK_LOW_MAX}, Medium Max={settings.RISK_MEDIUM_MAX}",
        category="SETTINGS",
        user=current_user.username,
        details=payload
    )

    return {
        "message": "Risk thresholds updated successfully",
        "low_max": settings.RISK_LOW_MAX,
        "medium_max": settings.RISK_MEDIUM_MAX
    }
