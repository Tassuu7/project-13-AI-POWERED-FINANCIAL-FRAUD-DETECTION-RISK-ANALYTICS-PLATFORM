"""Dataset upload, generation, preview, and download endpoints."""

from typing import List, Dict, Any
from pathlib import Path
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from fastapi.responses import FileResponse
from datetime import datetime
import pandas as pd

from backend.app.models.schemas import SyntheticGenerateRequest, DatasetInfo
from backend.app.services.synthetic_generator import synthetic_generator
from backend.app.services.storage_service import storage_service
from backend.app.services.history_service import history_service
from backend.app.core.auth import require_role, RoleEnum
from config.settings import settings
from config.logging_config import logger

router = APIRouter(prefix="/datasets", tags=["Datasets"])


@router.post("/upload")
async def upload_dataset(
    file: UploadFile = File(...),
    current_user = Depends(require_role([RoleEnum.ADMIN, RoleEnum.ANALYST]))
):
    """Upload CSV dataset locally."""
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV format datasets are permitted.")

    content = await file.read()
    if len(content) > 50 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File exceeds maximum size limit (50 MB).")

    target_path = settings.UPLOADS_DIR / file.filename
    with open(target_path, "wb") as f:
        f.write(content)

    try:
        df = pd.read_csv(target_path)
    except Exception as e:
        target_path.unlink(missing_ok=True)
        raise HTTPException(status_code=400, detail=f"Failed to parse CSV: {str(e)}")

    history_service.record_action(
        action=f"Uploaded dataset '{file.filename}'",
        category="DATASET",
        details={"rows": len(df), "cols": len(df.columns), "size": len(content)}
    )

    return {
        "message": "Dataset uploaded successfully",
        "filename": file.filename,
        "rows": len(df),
        "columns": list(df.columns),
        "size_bytes": len(content)
    }


@router.post("/generate")
def generate_dataset(
    req: SyntheticGenerateRequest,
    current_user = Depends(require_role([RoleEnum.ADMIN, RoleEnum.ANALYST]))
):
    """Generate reproducible synthetic financial transaction dataset."""
    df = synthetic_generator.generate(req)
    timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"synthetic_transactions_{len(df)}_seed{req.random_seed}_{timestamp_str}.csv"
    storage_service.save_dataset(filename, df)

    history_service.record_action(
        action=f"Generated synthetic dataset '{filename}'",
        category="DATASET",
        details={"records": len(df), "fraud_pct": req.fraud_percentage, "seed": req.random_seed}
    )

    records = df.head(25).to_dict(orient="records")
    return {
        "message": "Synthetic dataset generated successfully",
        "filename": filename,
        "rows": len(df),
        "records_count": len(df),
        "total_rows": len(df),
        "total_records": len(df),
        "columns": list(df.columns),
        "fraud_count": int(df["is_fraud"].sum()) if "is_fraud" in df.columns else 0,
        "sample_preview": records,
        "data": records,
        "preview": records
    }


@router.get("", response_model=List[Dict[str, Any]])
def list_datasets():
    """List all available datasets in data storage."""
    return storage_service.list_datasets()


@router.get("/{filename}/preview")
def preview_dataset(filename: str, rows: int = 25):
    """Get preview rows and column statistics for a dataset."""
    try:
        df = storage_service.load_dataset(filename)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Dataset '{filename}' not found.")

    has_fraud = "is_fraud" in df.columns
    fraud_cnt = int(df["is_fraud"].sum()) if has_fraud else 0
    records = df.head(rows).to_dict(orient="records")

    return {
        "filename": filename,
        "total_rows": len(df),
        "total_records": len(df),
        "total_columns": len(df.columns),
        "columns": list(df.columns),
        "has_fraud_label": has_fraud,
        "fraud_count": fraud_cnt,
        "fraud_rate": round(fraud_cnt / len(df) * 100.0, 2) if len(df) > 0 else 0.0,
        "data": records,
        "preview": records
    }


@router.get("/{filename}/download")
def download_dataset(filename: str):
    """Download dataset CSV file."""
    data_path = settings.DATA_DIR / filename
    if not data_path.exists():
        data_path = settings.UPLOADS_DIR / filename
    if not data_path.exists():
        raise HTTPException(status_code=404, detail="File not found.")

    return FileResponse(
        path=data_path,
        media_type="text/csv",
        filename=filename
    )
