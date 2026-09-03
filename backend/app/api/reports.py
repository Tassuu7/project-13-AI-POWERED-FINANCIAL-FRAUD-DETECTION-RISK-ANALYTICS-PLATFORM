"""Report generation and download endpoints."""

from typing import List, Dict, Any
from pathlib import Path
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from backend.app.models.schemas import ReportRequest
from backend.app.services.report_service import report_service
from backend.app.services.history_service import history_service
from config.settings import settings

router = APIRouter(prefix="/reports", tags=["Reports"])


@router.post("/generate")
def generate_report(req: ReportRequest):
    """Generate professional HTML or PDF risk and performance reports."""
    result = report_service.generate_report(req)

    r_type_name = req.report_type.value if hasattr(req.report_type, "value") else str(req.report_type)
    history_service.record_action(
        action=f"Generated report '{r_type_name}'",
        category="EXPORT",
        details={"format": req.format, "file": result["filename"]}
    )

    return result


@router.get("")
def list_reports() -> List[Dict[str, Any]]:
    """List all previously generated reports."""
    reports = []
    for p in settings.REPORTS_DIR.glob("*.*"):
        if p.suffix.lower() in [".html", ".pdf"]:
            stat = p.stat()
            reports.append({
                "filename": p.name,
                "format": p.suffix.replace(".", "").upper(),
                "size_bytes": stat.st_size,
                "created_time": stat.st_mtime
            })
    return reports


@router.get("/download/{filename}")
@router.get("/{filename}/download")
@router.get("/{filename}")
def download_report(filename: str):
    """Download generated report document."""
    target_path = settings.REPORTS_DIR / filename
    if not target_path.exists():
        raise HTTPException(status_code=404, detail=f"Report file '{filename}' not found.")

    media = "application/pdf" if filename.endswith(".pdf") else "text/html"
    return FileResponse(path=target_path, media_type=media, filename=filename)
