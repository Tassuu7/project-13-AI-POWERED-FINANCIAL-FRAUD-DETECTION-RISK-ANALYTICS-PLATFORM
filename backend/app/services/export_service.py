"""Export service generating local CSV, JSON, and artifact packages."""

from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List
import pandas as pd
from config.settings import settings
from backend.app.services.storage_service import storage_service


class ExportService:
    def export_csv(self, filename: str, data: List[Dict[str, Any]]) -> str:
        """Export tabular records to local CSV file."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        export_filename = f"{filename}_{timestamp}.csv"
        target_path = settings.EXPORTS_DIR / export_filename
        
        df = pd.DataFrame(data)
        df.to_csv(target_path, index=False)
        return export_filename

    def export_json(self, filename: str, data: Any) -> str:
        """Export structured data to local JSON file."""
        import json
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        export_filename = f"{filename}_{timestamp}.json"
        target_path = settings.EXPORTS_DIR / export_filename
        
        with open(target_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        return export_filename


export_service = ExportService()
