"""Local file-based storage manager for datasets, models, reports, and history."""

import json
import os
import shutil
from pathlib import Path
from typing import Dict, List, Any, Optional
import pandas as pd
import joblib

from config.settings import settings
from config.logging_config import logger


class StorageService:
    def __init__(self):
        self.data_dir = settings.DATA_DIR
        self.uploads_dir = settings.UPLOADS_DIR
        self.models_dir = settings.MODELS_DIR
        self.reports_dir = settings.REPORTS_DIR
        self.exports_dir = settings.EXPORTS_DIR
        self.audit_file = settings.AUDIT_FILE
        self.reviews_file = settings.REVIEWS_FILE
        self.system_config_file = settings.SYSTEM_CONFIG_FILE
        
        self._init_files()

    def _init_files(self):
        """Initialize required local json files if not present."""
        if not self.audit_file.exists():
            with open(self.audit_file, "w", encoding="utf-8") as f:
                json.dump([], f, indent=2)
                
        if not self.reviews_file.exists():
            with open(self.reviews_file, "w", encoding="utf-8") as f:
                json.dump([], f, indent=2)

    # --- Dataset Operations ---
    def save_dataset(self, filename: str, df: pd.DataFrame) -> Path:
        target_path = self.data_dir / filename
        df.to_csv(target_path, index=False)
        logger.info(f"Saved dataset '{filename}' with shape {df.shape}")
        return target_path

    def load_dataset(self, filename: str) -> pd.DataFrame:
        target_path = self.data_dir / filename
        if not target_path.exists():
            upload_path = self.uploads_dir / filename
            if upload_path.exists():
                target_path = upload_path
            else:
                raise FileNotFoundError(f"Dataset '{filename}' not found in data or uploads directory.")
        return pd.read_csv(target_path)

    def list_datasets(self) -> List[Dict[str, Any]]:
        datasets = []
        for path in list(self.data_dir.glob("*.csv")) + list(self.uploads_dir.glob("*.csv")):
            try:
                df = pd.read_csv(path, nrows=50)
                file_stat = path.stat()
                has_label = "is_fraud" in df.columns
                datasets.append({
                    "filename": path.name,
                    "filepath": str(path),
                    "size_bytes": file_stat.st_size,
                    "modified_time": file_stat.st_mtime,
                    "columns": list(df.columns),
                    "has_fraud_label": has_label
                })
            except Exception as e:
                logger.warning(f"Could not read dataset info for {path.name}: {e}")
        return datasets

    # --- Model Operations ---
    def save_model_artifact(self, model_name: str, model_object: Any, metadata: Dict[str, Any]):
        safe_name = model_name.lower().replace(" ", "_")
        model_path = self.models_dir / f"{safe_name}.joblib"
        meta_path = self.models_dir / f"{safe_name}_meta.json"
        
        joblib.dump(model_object, model_path)
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2)
        logger.info(f"Saved model artifact '{safe_name}' and metadata")

    def load_model_artifact(self, model_name: str):
        safe_name = model_name.lower().replace(" ", "_")
        model_path = self.models_dir / f"{safe_name}.joblib"
        meta_path = self.models_dir / f"{safe_name}_meta.json"
        
        if not model_path.exists():
            raise FileNotFoundError(f"Model '{model_name}' artifact not found at {model_path}")
        
        model_obj = joblib.load(model_path)
        meta = {}
        if meta_path.exists():
            with open(meta_path, "r", encoding="utf-8") as f:
                meta = json.load(f)
        return model_obj, meta

    def list_trained_models(self) -> List[Dict[str, Any]]:
        models = []
        for meta_file in self.models_dir.glob("*_meta.json"):
            try:
                with open(meta_file, "r", encoding="utf-8") as f:
                    meta = json.load(f)
                models.append(meta)
            except Exception as e:
                logger.warning(f"Failed to read model meta {meta_file}: {e}")
        return models

    # --- Audit Log Operations ---
    def get_audit_logs(self) -> List[Dict[str, Any]]:
        if not self.audit_file.exists():
            return []
        try:
            with open(self.audit_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []

    def append_audit_log(self, entry: Dict[str, Any]):
        logs = self.get_audit_logs()
        logs.insert(0, entry)  # Most recent first
        # Limit to 500 records
        logs = logs[:500]
        with open(self.audit_file, "w", encoding="utf-8") as f:
            json.dump(logs, f, indent=2)

    # --- Suspicious Reviews Operations ---
    def get_suspicious_reviews(self) -> List[Dict[str, Any]]:
        if not self.reviews_file.exists():
            return []
        try:
            with open(self.reviews_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []

    def save_suspicious_reviews(self, items: List[Dict[str, Any]]):
        with open(self.reviews_file, "w", encoding="utf-8") as f:
            json.dump(items, f, indent=2)


storage_service = StorageService()
