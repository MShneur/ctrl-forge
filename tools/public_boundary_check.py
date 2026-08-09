#!/usr/bin/env python3
"""Fail closed if the canonical public upstream tracks personal mine/ content."""
from __future__ import annotations

import subprocess
import sys

ALLOWED_EXACT = {
    "mine/README.md",
    "mine/settings.yaml",
}
ALLOWED_PREFIXES = (
    "mine/projects/example-project/",
)


def tracked_files() -> list[str]:
    out = subprocess.check_output(["git", "ls-files"], text=True)
    return [line.strip() for line in out.splitlines() if line.strip()]


def allowed(path: str) -> bool:
    if not path.startswith("mine/"):
        return True
    if path in ALLOWED_EXACT:
        return True
    return any(path.startswith(prefix) for prefix in ALLOWED_PREFIXES)


def main() -> int:
    violations = sorted(path for path in tracked_files() if not allowed(path))
    if violations:
        print("PUBLIC BOUNDARY VIOLATION: personal/non-template files are tracked under mine/:")
        for path in violations:
            print(f"- {path}")
        print("\nPublic ctrl-forge may contain only the explicit mine/ template allowlist.")
        return 1
    print("Public boundary OK: no non-template mine/ content is tracked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
