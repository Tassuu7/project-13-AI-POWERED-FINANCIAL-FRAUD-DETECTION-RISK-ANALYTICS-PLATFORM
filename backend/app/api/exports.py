"""Export center endpoints for CSV, JSON, and audit data package downloads."""

from typing import List, Dict, Any, Optional
from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import FileResponse
from config.settings import settings
from backend.app.services.export_service import export_service
from backend.app.services.storage_service import storage_service
from backend.app.services.suspicious_service import suspicious_service
from backend.app.services.history_service import history_service

router = APIRouter(prefix="/exports", tags=["Exports"])


@router.post("/suspicious")
def export_suspicious_csv():
    """Export all current suspicious queue records to CSV."""
    items = suspicious_service.get_all()
    if not items:
        raise HTTPException(status_code=400, detail="No suspicious records found to export.")

    data = [item.model_dump() for item in items]
    filename = export_service.export_csv("suspicious_transactions", data)

    history_service.record_action(
        action=f"Exported suspicious transactions to {filename}",
        category="EXPORT",
        details={"record_count": len(items)}
    )

    return {"message": "Export completed", "filename": filename}


@router.post("/model_metrics")
def export_metrics_json():
    """Export all model benchmarks and metadata to JSON."""
    models = storage_service.list_trained_models()
    filename = export_service.export_json("model_evaluation_benchmarks", models)
    return {"message": "Export completed", "filename": filename}


@router.get("/files")
def list_export_files() -> List[Dict[str, Any]]:
    """List all available exports in export center."""
    exports = []
    for p in settings.EXPORTS_DIR.glob("*.*"):
        stat = p.stat()
        exports.append({
            "filename": p.name,
            "size_bytes": stat.st_size,
            "created_time": stat.st_mtime,
            "extension": p.suffix.upper().replace(".", "")
        })
    return exports


@router.get("/download/{filename}")
@router.get("/{filename}")
def download_export_file(filename: str):
    """Download export file."""
    path = settings.EXPORTS_DIR / filename
    if not path.exists():
        raise HTTPException(status_code=404, detail="Export file not found.")
    return FileResponse(path=path, filename=filename)
