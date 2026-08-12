#!/usr/bin/env python3
"""Create a new project folder in a deliberate private CTRL-FORGE copy."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

DEFAULTS = {
    "projects_dir": "mine/projects",
    "buckets": ["research", "decisions", "deliverables"],
    "handoff_file": "HANDOFF.md",
    "state_file": "PROJECT_STATE.yaml",
}


def repo_mode(repo: Path) -> str:
    mode_path = repo / "REPO_MODE.yaml"
    if not mode_path.is_file():
        return ""
    for raw in mode_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("mode:"):
            return line.split(":", 1)[1].strip().strip('"\'')
    return ""


def load_config(repo: Path) -> dict:
    """Best-effort config read. Never raises; falls back to DEFAULTS."""
    cfg = dict(DEFAULTS)
    config_path = repo / "forge" / "forge-config.yaml"
    if not config_path.is_file():
        return cfg
    text = config_path.read_text(encoding="utf-8")
    try:
        import yaml  # type: ignore
        data = yaml.safe_load(text) or {}
        if isinstance(data.get("projects_dir"), str):
            cfg["projects_dir"] = data["projects_dir"]
        buckets = data.get("buckets")
        if isinstance(buckets, dict):
            cfg["buckets"] = [str(v) for v in buckets.values()]
        elif isinstance(buckets, list):
            cfg["buckets"] = [str(v) for v in buckets]
        if isinstance(data.get("handoff_file"), str):
            cfg["handoff_file"] = data["handoff_file"]
        if isinstance(data.get("state_file"), str):
            cfg["state_file"] = data["state_file"]
        return cfg
    except ImportError:
        pass
    for key in ("projects_dir", "handoff_file", "state_file"):
        m = re.search(rf"^{key}:\s*(\S+)\s*$", text, re.MULTILINE)
        if m:
            cfg[key] = m.group(1)
    block = re.search(r"^buckets:\s*$((?:\n[ \t]+\S.*)+)", text, re.MULTILINE)
    if block:
        vals = re.findall(r"^\s+\w+:\s*(\S+)", block.group(1), re.MULTILINE)
        if vals:
            cfg["buckets"] = vals
    return cfg


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    slug = re.sub(r"-{2,}", "-", slug)
    if not slug:
        raise ValueError("Project name must contain at least one letter or digit.")
    return slug[:64].rstrip("-")


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a CTRL-FORGE project in a private copy.")
    parser.add_argument("name", help="Human-readable project name")
    parser.add_argument("--slug", help="Optional project ID")
    args = parser.parse_args()

    repo = Path(__file__).resolve().parents[1]
    mode = repo_mode(repo)
    if mode != "private-copy":
        print(
            "Refusing to create a real project because REPO_MODE.yaml is not set to 'private-copy'.\n"
            "Canonical/public CTRL-FORGE is template-only. First create a PRIVATE copy, verify its visibility, "
            "then change REPO_MODE.yaml to 'mode: private-copy'.",
            file=sys.stderr,
        )
        return 2

    cfg = load_config(repo)
    project_id = slugify(args.slug or args.name)
    projects_root = (repo / cfg["projects_dir"]).resolve()
    destination = (projects_root / project_id).resolve()

    if projects_root != destination.parent:
        print("Refusing unsafe project path.", file=sys.stderr)
        return 2
    if destination.exists():
        print(f"Project already exists: {destination}", file=sys.stderr)
        return 2

    created_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    name = args.name.strip()

    destination.mkdir(parents=True)
    (destination / cfg["state_file"]).write_text(
        f"id: {project_id}\n"
        f"name: {name}\n"
        f"status: active\n"
        f"created_at: {created_at}\n"
        f"summary: >\n"
        f"  One or two lines on what this project is. Keep it short.\n",
        encoding="utf-8",
    )
    (destination / cfg["handoff_file"]).write_text(
        f"# Handoff — {name}\n\n"
        f"**Last updated:** {created_at}\n\n"
        f"## Done\n- Project created.\n\n"
        f"## Open\n- Say what needs doing next.\n\n"
        f"## Pick up first\n- The one thing the next session should start with.\n",
        encoding="utf-8",
    )
    (destination / "README.md").write_text(
        f"# {name}\n\n"
        f"A CTRL-FORGE project.\n\n"
        f"- `PROJECT_STATE.yaml` — what this is, in a few lines.\n"
        f"- `HANDOFF.md` — what's open. Read this first when you come back.\n"
        f"- `research/` — inputs and sources.\n"
        f"- `decisions/` — settled calls, with reasoning.\n"
        f"- `deliverables/` — finished output.\n",
        encoding="utf-8",
    )
    for bucket in cfg["buckets"]:
        b = destination / bucket
        b.mkdir(exist_ok=True)
        (b / ".gitkeep").write_text("", encoding="utf-8")

    print(f"Created {destination.relative_to(repo)}")
    print(f'Next prompt: Read AGENTS.md and continue project "{project_id}".')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
