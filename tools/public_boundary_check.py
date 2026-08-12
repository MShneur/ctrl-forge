#!/usr/bin/env python3
"""Fail closed on non-template content in canonical public CTRL-FORGE."""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import subprocess
import sys

CANONICAL_REPOSITORY = "MShneur/ctrl-forge"
MODE_FILE = Path("REPO_MODE.yaml")
PUBLIC_MODE = "public-template-upstream"
PRIVATE_MODE = "private-copy"

ALLOWED_EXACT = {
    ".gitignore",
    "AGENTS.md",
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "NOTICE",
    "PUBLIC_BOUNDARY.md",
    "README.md",
    "REPO_MODE.yaml",
    "SECURITY.md",
    "UPDATING.md",
    "mine/README.md",
    "mine/settings.yaml",
}

ALLOWED_PREFIXES = (
    ".github/",
    "forge/",
    "tools/",
    "mine/projects/example-project/",
)


def tracked_files() -> list[str]:
    out = subprocess.check_output(["git", "ls-files"], text=True)
    return [line.strip() for line in out.splitlines() if line.strip()]


def allowed(path: str) -> bool:
    if path in ALLOWED_EXACT:
        return True
    return any(path.startswith(prefix) for prefix in ALLOWED_PREFIXES)


def read_mode() -> str:
    if not MODE_FILE.exists():
        return ""
    for raw in MODE_FILE.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("mode:"):
            return line.split(":", 1)[1].strip().strip('"\'')
    return ""


def remote_identity() -> str:
    env_repo = os.getenv("GITHUB_REPOSITORY", "").strip()
    if env_repo:
        return env_repo
    try:
        remote = subprocess.check_output(
            ["git", "config", "--get", "remote.origin.url"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except subprocess.CalledProcessError:
        return ""
    normalized = remote.removesuffix(".git")
    for marker in ("github.com/", "github.com:"):
        if marker in normalized:
            return normalized.split(marker, 1)[1]
    return normalized


def self_test() -> None:
    assert allowed("README.md")
    assert allowed("forge/agents/librarian.md")
    assert allowed("mine/projects/example-project/README.md")
    assert not allowed("projects/private-project/README.md")
    assert not allowed("mine/projects/real-project/HANDOFF.md")
    assert not allowed("private-notes.md")
    assert not allowed("research/raw-private-data.json")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        print("Public boundary self-test: PASS")
        return 0

    mode = read_mode()
    identity = remote_identity()

    if not mode:
        print("PUBLIC BOUNDARY VIOLATION: REPO_MODE.yaml is missing or has no mode.", file=sys.stderr)
        return 1

    if identity == CANONICAL_REPOSITORY and mode != PUBLIC_MODE:
        print(
            f"PUBLIC BOUNDARY VIOLATION: canonical {CANONICAL_REPOSITORY} must remain in {PUBLIC_MODE} mode.",
            file=sys.stderr,
        )
        return 1

    if mode == PRIVATE_MODE:
        print("Private-copy mode: canonical public allowlist is not applied in this private copy.")
        return 0

    if mode != PUBLIC_MODE:
        print(f"PUBLIC BOUNDARY VIOLATION: unknown repository mode: {mode}", file=sys.stderr)
        return 1

    violations = sorted(path for path in tracked_files() if not allowed(path))
    if violations:
        print("PUBLIC BOUNDARY VIOLATION: non-allowlisted content is tracked:", file=sys.stderr)
        for path in violations:
            print(f"- {path}", file=sys.stderr)
        print(
            "\nCanonical public CTRL-FORGE is template/system-only. Review and explicitly allowlist intentional public system/template paths; never allowlist real project data.",
            file=sys.stderr,
        )
        return 1

    print("Public boundary OK: repository contains only explicit public system/template allowlist paths.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
