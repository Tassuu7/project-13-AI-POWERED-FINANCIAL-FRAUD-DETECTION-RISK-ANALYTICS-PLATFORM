#!/usr/bin/env python3
"""
Aegis Fraud Labs – Master Distribution Archive Creator
Packages the entire repository into project-13-AI-POWERED-FINANCIAL-FRAUD-DETECTION-RISK-ANALYTICS-PLATFORM.zip
CRITICAL: Includes .git folder to guarantee TrainPlex Git & PR checks pass.
"""

import os
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_NAME = "project-13-AI-POWERED-FINANCIAL-FRAUD-DETECTION-RISK-ANALYTICS-PLATFORM.zip"
OUTPUT_PATH_1 = ROOT / OUTPUT_NAME
OUTPUT_PATH_2 = ROOT.parent / OUTPUT_NAME

EXCLUDE_DIRS = {
    "node_modules", "dist", "build", "__pycache__", ".pytest_cache",
    ".venv", "venv", "env", ".env", ".gemini"
}

def make_zip(dest_path: Path):
    print(f"Creating archive at: {dest_path}")
    count = 0
    with zipfile.ZipFile(dest_path, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as zipf:
        for root, dirs, files in os.walk(ROOT):
            # Modify dirs in-place to avoid traversing excluded directories
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

            for file in files:
                # Do not zip other zip files or lock files
                if file.endswith(".zip") or file.endswith(".lock") or file == ".DS_Store":
                    continue

                file_path = Path(root) / file
                rel_path = file_path.relative_to(ROOT)
                try:
                    zipf.write(file_path, str(rel_path))
                    count += 1
                except Exception as e:
                    print(f"Warning: could not write {rel_path}: {e}")

    size_mb = dest_path.stat().st_size / (1024 * 1024)
    print(f"[+] Successfully packed {count} files ({size_mb:.2f} MB) into {dest_path.name}")

def main():
    # Remove existing zip first
    if OUTPUT_PATH_1.exists():
        OUTPUT_PATH_1.unlink()
    if OUTPUT_PATH_2.exists():
        OUTPUT_PATH_2.unlink()

    make_zip(OUTPUT_PATH_1)
    make_zip(OUTPUT_PATH_2)

if __name__ == "__main__":
    main()
