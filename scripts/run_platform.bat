@echo off
echo =====================================================================
echo Starting Aegis Fraud Labs -- Fraud Detection & Risk Analytics Platform
echo =====================================================================

start "Fraud Detection API (FastAPI)" cmd /k "uvicorn backend.app.main:app --host 0.0.0.0 --port 8013 --reload"

start "Fraud Detection UI (Vite)" cmd /k "cd frontend && npx vite --port 5193"

echo Services launched!
echo API Documentation: http://127.0.0.1:8013/docs
echo Web Application:  http://localhost:5193
echo =====================================================================
