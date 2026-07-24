#!/usr/bin/env python3
"""Validate a CTRL-FORGE repo. Stdlib only. Enforces forge/rules/forge-rules.yaml.

Falls back gracefully if PyYAML is absent — the structural checks still run.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "LICENSE",
    "forge/VERSION",
    "forge/forge-config.yaml",
    "forge/agents/librarian.md",
    "forge/rules/forge-rules.yaml",
    "tools/new_project.py",
    "tools/privacy_scan.py",
]

DEFAULT_PROJECTS_DIR = "mine/projects"
DEFAULT_BUCKETS = ["research", "decisions", "deliverables"]


def projects_dir(repo: Path) -> Path:
    cfg = repo / "forge" / "forge-config.yaml"
    if cfg.is_file():
        m = re.search(r"^projects_dir:\s*(\S+)", cfg.read_text(encoding="utf-8"), re.MULTILINE)
        if m:
            return repo / m.group(1)
    return repo / DEFAULT_PROJECTS_DIR


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    errors: list[str] = []
    warnings: list[str] = []

    for rel in REQUIRED_FILES:
        if not (repo / rel).is_file():
            errors.append(f"Missing required file: {rel}")

    # forge/ and mine/ must both exist and stay separate.
    if not (repo / "forge").is_dir():
        errors.append("Missing forge/ directory.")
    if not (repo / "mine").is_dir():
        errors.append("Missing mine/ directory.")

    # Every project needs a HANDOFF (rule: every-project-has-a-handoff).
    pdir = projects_dir(repo)
    if pdir.is_dir():
        for project in sorted(p for p in pdir.iterdir() if p.is_dir()):
            if not (project / "HANDOFF.md").is_file():
                errors.append(f"Project '{project.name}' missing HANDOFF.md")
            if not (project / "PROJECT_STATE.yaml").is_file():
                warnings.append(f"Project '{project.name}' missing PROJECT_STATE.yaml")
            # rule: final-work-stays-out-of-research
            research = project / "research"
            if research.is_dir():
                for f in research.rglob("*"):
                    if f.is_file() and f.suffix in {".md", ".yaml", ".yml", ".txt"}:
                        try:
                            if re.search(r"status:\s*final", f.read_text(encoding="utf-8"), re.I):
                                warnings.append(f"'{f.relative_to(repo)}' marked final but sits in research/")
                        except (OSError, UnicodeDecodeError):
                            pass

    # Privacy scan gate.
    scan = subprocess.run(
        [sys.executable, str(repo / "tools" / "privacy_scan.py"), str(repo)],
        text=True, capture_output=True, check=False,
    )
    if scan.returncode != 0:
        errors.append(scan.stderr.strip() or "Privacy scan failed")

    for w in warnings:
        print(f"warning: {w}")
    if errors:
        print("Validation failed:", file=sys.stderr)
        for e in errors:
            print(f"- {e}", file=sys.stderr)
        return 1

    print(f"CTRL-FORGE validation passed. ({len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
