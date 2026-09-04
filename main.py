#!/usr/bin/env python3
"""
AEGIS FRAUD LABS – AI-POWERED FINANCIAL FRAUD DETECTION & RISK ANALYTICS PLATFORM
Unified Command-Line Interface & Application Entry Point.
"""

import sys
import os
import argparse
import subprocess
from pathlib import Path

# Ensure root is in python path
ROOT_DIR = Path(__file__).resolve().parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))


def run_server(host: str = "0.0.0.0", port: int = 8013, reload: bool = False):
    """Start the FastAPI backend server."""
    import uvicorn
    print(f"[*] Starting Aegis Fraud Labs Backend on http://{host}:{port}...")
    uvicorn.run("backend.app.main:app", host=host, port=port, reload=reload)


def run_measure():
    """Run production codebase LOC measurement."""
    measure_script = ROOT_DIR / "measure.py"
    if measure_script.exists():
        subprocess.run([sys.executable, str(measure_script)])
    else:
        print("[!] measure.py not found.")


def run_tests():
    """Execute pytest test suite."""
    print("[*] Running automated test suite...")
    subprocess.run([sys.executable, "-m", "pytest", "-v", "tests/"])


def run_synthetic_data(records: int = 1500, fraud_pct: float = 3.5, seed: int = 42):
    """Generate synthetic fraud transaction dataset."""
    from backend.app.services.synthetic_generator import synthetic_generator
    print(f"[*] Generating {records} synthetic transactions with {fraud_pct}% fraud ratio (seed={seed})...")
    df = synthetic_generator.generate_dataset(num_records=records, fraud_ratio=fraud_pct/100, random_seed=seed)
    filename = f"synthetic_transactions_{records}_seed{seed}.csv"
    filepath = ROOT_DIR / "data" / filename
    df.to_csv(filepath, index=False)
    print(f"[+] Successfully saved {len(df)} transactions to {filepath}")


def run_train_models():
    """Train and evaluate baseline ML models."""
    from backend.app.services.ml_service import ml_service
    print("[*] Training baseline machine learning models...")
    res = ml_service.train_all_models("sample_synthetic_transactions.csv")
    print(f"[+] Training completed. Best performing model: {res.get('best_model_name')}")


def run_generate_report(report_type: str = "Executive Summary", fmt: str = "html"):
    """Compile regulatory compliance risk report."""
    from backend.app.services.report_service import report_service
    print(f"[*] Compiling {report_type} in {fmt.upper()} format...")
    meta = report_service.generate_report(report_type, fmt)
    print(f"[+] Generated report {meta['report_id']} saved to {meta['filename']}")


def main():
    parser = argparse.ArgumentParser(
        description="Aegis Fraud Labs – AI-Powered Financial Fraud Detection & Risk Analytics Platform"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # Serve command
    serve_parser = subparsers.add_parser("serve", help="Start the FastAPI backend server")
    serve_parser.add_argument("--host", default="0.0.0.0", help="Host interface (default: 0.0.0.0)")
    serve_parser.add_argument("--port", type=int, default=8013, help="Port number (default: 8013)")
    serve_parser.add_argument("--reload", action="store_true", help="Enable live auto-reload")

    # Measure command
    subparsers.add_parser("measure", help="Run codebase LOC measurement audit")

    # Test command
    subparsers.add_parser("test", help="Run automated test suite")

    # Generate synthetic data
    synth_parser = subparsers.add_parser("generate-data", help="Generate synthetic transaction data")
    synth_parser.add_argument("--records", type=int, default=1500, help="Number of records")
    synth_parser.add_argument("--fraud-pct", type=float, default=3.5, help="Fraud percentage")
    synth_parser.add_argument("--seed", type=int, default=42, help="Random seed")

    # Train models
    subparsers.add_parser("train-models", help="Train and benchmark ML models")

    # Compile report
    report_parser = subparsers.add_parser("compile-report", help="Compile risk compliance report")
    report_parser.add_argument("--type", default="Executive Summary", help="Report scope")
    report_parser.add_argument("--format", default="html", choices=["html", "pdf"], help="Output format")

    args = parser.parse_args()

    if args.command == "serve" or args.command is None:
        if args.command is None:
            # Default: start server
            run_server()
        else:
            run_server(host=args.host, port=args.port, reload=args.reload)
    elif args.command == "measure":
        run_measure()
    elif args.command == "test":
        run_tests()
    elif args.command == "generate-data":
        run_synthetic_data(records=args.records, fraud_pct=args.fraud_pct, seed=args.seed)
    elif args.command == "train-models":
        run_train_models()
    elif args.command == "compile-report":
        run_generate_report(report_type=args.type, fmt=args.format)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
