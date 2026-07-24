#!/usr/bin/env python3
"""Conservative secret scanner for CTRL-FORGE text files."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\b(?:ghp|github_pat)_[A-Za-z0-9_]{20,}\b"),
    "OpenAI-style secret": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "generic bearer token": re.compile(r"(?i)\bAuthorization:\s*Bearer\s+[A-Za-z0-9._~+/=-]{16,}"),
}

SKIP_DIRS = {".git", ".venv", "venv", "__pycache__", "node_modules"}
SKIP_SUFFIXES = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".pdf", ".zip",
    ".gz", ".tar", ".woff", ".woff2", ".ttf", ".otf"
}


def scan(root: Path) -> list[str]:
    findings: list[str] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() in SKIP_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for label, pattern in PATTERNS.items():
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                findings.append(f"{path}:{line}: possible {label}")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.path).resolve()
    findings = scan(root)
    if findings:
        print("\n".join(findings), file=sys.stderr)
        print(f"Privacy scan failed with {len(findings)} finding(s).", file=sys.stderr)
        return 1
    print("Privacy scan: no known secret patterns found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
