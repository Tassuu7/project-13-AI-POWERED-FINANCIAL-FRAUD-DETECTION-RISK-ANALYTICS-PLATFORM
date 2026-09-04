#!/usr/bin/env python3
"""
Aegis Fraud Labs – WSGI/ASGI Application Entry Point
Exposes the FastAPI application instance for production ASGI servers.
"""

import sys
from pathlib import Path

# Add root directory to sys.path
ROOT_DIR = Path(__file__).resolve().parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from backend.app.main import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8013)
