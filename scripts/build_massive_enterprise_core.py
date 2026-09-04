#!/usr/bin/env python3
"""
Master script to construct the complete enterprise architecture for Aegis Fraud Labs.
Generates comprehensive Python modules across CEP, ML, Graph, Compliance, and Protocols.
"""

import sys
import os
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

def write_module(rel_path: str, content: str):
    target = ROOT_DIR / rel_path
    target.parent.mkdir(parents=True, exist_ok=True)
    with open(target, "w", encoding="utf-8") as f:
        f.write(content)
    lines = len(content.splitlines())
    code_lines = len([l for l in content.splitlines() if l.strip() and not l.strip().startswith(("#", "//", "/*"))])
    print(f"[+] {rel_path} -> {code_lines} code LOC ({lines} total lines)")

print("[*] Starting Enterprise Architecture Builder...")
