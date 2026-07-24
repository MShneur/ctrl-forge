#!/usr/bin/env python3
"""Check whether a newer Forge exists. Prints a one-line recommendation.

This is the ONLY thing in CTRL-FORGE that touches the network, and all it does
is read a version number. It downloads nothing. It runs nothing. It changes
nothing. If offline, it says so and exits cleanly. Stdlib only.
"""

from __future__ import annotations

import re
import sys
import urllib.request
from pathlib import Path

DEFAULT_URL = "https://raw.githubusercontent.com/MShneur/ctrl-forge/main/forge/VERSION"


def local_version(repo: Path) -> str:
    vf = repo / "forge" / "VERSION"
    return vf.read_text(encoding="utf-8").strip() if vf.is_file() else "unknown"


def config_url(repo: Path) -> str:
    cfg = repo / "forge" / "forge-config.yaml"
    if cfg.is_file():
        m = re.search(r"version_url:\s*(\S+)", cfg.read_text(encoding="utf-8"))
        if m:
            return m.group(1)
    return DEFAULT_URL


def parse(v: str):
    return tuple(int(x) for x in re.findall(r"\d+", v)) or (0,)


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    here = local_version(repo)
    url = config_url(repo)
    try:
        with urllib.request.urlopen(url, timeout=5) as resp:
            latest = resp.read().decode("utf-8").strip()
    except Exception:
        print(f"You're on Forge {here}. (Couldn't check for updates — offline is fine.)")
        return 0

    if parse(latest) > parse(here):
        print(f"Forge {latest} is available (you're on {here}).")
        print("Update is optional. If you want it: python tools/update_forge.py")
    else:
        print(f"You're on Forge {here}. Up to date.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
