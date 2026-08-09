# AGENTS.md

If you are an AI reading this repo, this is your entry point.

## Public/private boundary first

Before doing any project work, determine whether this checkout is the canonical public `MShneur/ctrl-forge` repository or a user's private copy.

- **Canonical public upstream:** `mine/` is template/example space only. Never write personal project content there. Follow `PUBLIC_BOUNDARY.md` and run `python tools/public_boundary_check.py` before any public push.
- **Private user copy:** `mine/` is the user's project area and may contain private work.

Never copy project payloads from Personal Forge, another private repo, private chat context, or user files into public `ctrl-forge`. If publication intent is uncertain, stop at a human gate.

## What this repo is

CTRL-FORGE gives a durable place to keep project work so it survives between sessions and different AIs:

- `forge/` — the reusable system.
- `mine/` — user projects/settings in a private copy; public templates only in canonical upstream.

## What to do in a private copy

1. Read `forge/agents/librarian.md`.
2. Read `forge/forge-config.yaml` rather than assuming paths.
3. Find the named project under the configured projects folder.
4. If it does not exist, create only the minimal project structure.
5. Read project state and handoff before working.
6. Work only in that project.
7. Follow `forge/rules/forge-rules.yaml`.
8. Update state and `HANDOFF.md` before stopping.
9. Never claim unverified pushes, fetches, or tests.
10. Never publish private content without explicit human approval.

## Need a specialist?

This repo ships the Librarian. For reusable personas, workflows, and teams, see [Agents of AI](https://github.com/MShneur/Agents-of-AI).
