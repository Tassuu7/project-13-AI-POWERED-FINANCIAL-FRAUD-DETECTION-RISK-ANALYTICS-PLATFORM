"""Platform configuration and path resolution for AI-Powered Financial Fraud Detection."""

import os
from pathlib import Path
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI-Powered Financial Fraud Detection & Risk Analytics Platform"
    PROJECT_VERSION: str = "1.0.0"
    API_PREFIX: str = "/api"
    
    # Storage Paths (Local-first, strictly database-free)
    DATA_DIR: Path = BASE_DIR / "data"
    UPLOADS_DIR: Path = BASE_DIR / "data" / "uploads"
    MODELS_DIR: Path = BASE_DIR / "models"
    REPORTS_DIR: Path = BASE_DIR / "reports"
    EXPORTS_DIR: Path = BASE_DIR / "exports"
    LOGS_DIR: Path = BASE_DIR / "logs"
    CONFIG_DIR: Path = BASE_DIR / "config"
    
    # Risk Engine Default Thresholds
    RISK_LOW_MAX: int = 30
    RISK_MEDIUM_MAX: int = 70
    
    # CORS
    ALLOWED_ORIGINS: list[str] = [
        "http://localhost:5193",
        "http://127.0.0.1:5193",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:8013",
        "http://127.0.0.1:8013",
        "http://localhost:8000",
        "http://127.0.0.1:8000"
    ]
    
    # Audit trail file
    AUDIT_FILE: Path = BASE_DIR / "data" / "audit_history.json"
    REVIEWS_FILE: Path = BASE_DIR / "data" / "suspicious_reviews.json"
    SYSTEM_CONFIG_FILE: Path = BASE_DIR / "config" / "system_config.json"

    model_config = {
        "env_file": ".env",
        "extra": "ignore"
    }

settings = Settings()

# Ensure critical directories exist
for directory in [
    settings.DATA_DIR,
    settings.UPLOADS_DIR,
    settings.MODELS_DIR,
    settings.REPORTS_DIR,
    settings.EXPORTS_DIR,
    settings.LOGS_DIR,
    settings.CONFIG_DIR,
]:
    directory.mkdir(parents=True, exist_ok=True)
