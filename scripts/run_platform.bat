@echo off
echo =====================================================================
echo Starting AI-Powered Financial Fraud Detection & Risk Analytics Platform
echo =====================================================================

start "Fraud Detection API (FastAPI)" cmd /k "uvicorn backend.app.main:app --host 127.0.0.1 --port 8000 --reload"

start "Fraud Detection UI (Vite)" cmd /k "cd frontend && npm run dev"

echo Services launched!
echo API Documentation: http://127.0.0.1:8000/docs
echo Web Application:  http://localhost:5173
echo =====================================================================
