"""FastAPI application entry point for AI-Powered Financial Fraud Detection & Risk Analytics Platform."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from config.settings import settings
from config.logging_config import logger

# Import API routers
from backend.app.api.auth import router as auth_router
from backend.app.api.datasets import router as datasets_router
from backend.app.api.validation import router as validation_router
from backend.app.api.preprocessing import router as preprocessing_router
from backend.app.api.features import router as features_router
from backend.app.api.eda import router as eda_router
from backend.app.api.models import router as models_router
from backend.app.api.predictions import router as predictions_router
from backend.app.api.risk import router as risk_router
from backend.app.api.transactions import router as transactions_router
from backend.app.api.suspicious import router as suspicious_router
from backend.app.api.explainability import router as explainability_router
from backend.app.api.reports import router as reports_router
from backend.app.api.exports import router as exports_router
from backend.app.api.history import router as history_router
from backend.app.api.settings import router as settings_router

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f"Started {settings.PROJECT_NAME} (v{settings.PROJECT_VERSION})")
    yield

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    description="Enterprise-grade local-first platform for financial fraud detection, explainable risk scoring, and investigation analytics.",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# CORS Middleware for React frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Local development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount Routers under both /api and /api/v1
all_routers = [
    auth_router,
    datasets_router,
    validation_router,
    preprocessing_router,
    features_router,
    eda_router,
    models_router,
    predictions_router,
    risk_router,
    transactions_router,
    suspicious_router,
    explainability_router,
    reports_router,
    exports_router,
    history_router,
    settings_router
]

for router_item in all_routers:
    app.include_router(router_item, prefix="/api")
    app.include_router(router_item, prefix="/api/v1")


@app.get("/health")
def health_check():
    """System health check endpoint."""
    return {
        "status": "healthy",
        "platform": settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION,
        "database": "none (file-based persistence)",
        "security": "local-only / no-external-keys"
    }


@app.get("/")
def root():
    """Root endpoint summarizing active services."""
    return {
        "platform": settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION,
        "api_documentation": "/docs",
        "status": "online"
    }
