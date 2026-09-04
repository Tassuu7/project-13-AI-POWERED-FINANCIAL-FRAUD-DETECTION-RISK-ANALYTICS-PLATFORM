.PHONY: help install run server frontend test measure build clean

help:
	@echo "Aegis Fraud Labs Automation Commands:"
	@echo "  make install    - Install python and node dependencies"
	@echo "  make run        - Run FastAPI backend and Vite frontend"
	@echo "  make server     - Run FastAPI backend server on port 8013"
	@echo "  make frontend   - Run Vite frontend on port 5193"
	@echo "  make test       - Execute automated pytest test suite"
	@echo "  make measure    - Run codebase line count and audit"
	@echo "  make build      - Build production frontend distribution"
	@echo "  make clean      - Clean temporary artifacts and caches"

install:
	pip install -r backend/requirements.txt
	cd frontend && npm install

run:
	python main.py serve --port 8013

server:
	uvicorn backend.app.main:app --host 0.0.0.0 --port 8013 --reload

frontend:
	cd frontend && npx vite --port 5193

test:
	pytest -v tests/

measure:
	python measure.py

build:
	cd frontend && npm run build

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
