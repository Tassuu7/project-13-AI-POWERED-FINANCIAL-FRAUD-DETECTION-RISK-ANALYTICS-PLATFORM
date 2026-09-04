#!/usr/bin/env python3
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def run(cmd):
    print(f"Executing: {' '.join(cmd)}")
    res = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error: {res.stderr.strip()}")
    else:
        print(f"Success: {res.stdout.strip()[:200]}")
    return res

def main():
    run(["git", "checkout", "-b", "feature/synthetic-data-studio"])
    run(["git", "add", "backend/app/", "frontend/", "scripts/", "data/", "models/"])
    run(["git", "commit", "-m", "feat(admin): add synthetic data generator studio to administrator console with preset triggers and instant preview"])
    run(["git", "checkout", "main"])
    run(["git", "merge", "--no-ff", "feature/synthetic-data-studio", "-m", "Merge pull request #5 from feature/synthetic-data-studio"])
    print("[+] Successfully merged PR #5!")

if __name__ == "__main__":
    main()
