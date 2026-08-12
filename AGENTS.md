# AGENTS.md

If you are an AI reading this repo, this is your entry point.

## STOP: identify repository mode first

Read `REPO_MODE.yaml` before doing any work.

### If mode is `public-template-upstream`

You are in a public template/system repository. **Do not place real project work anywhere in this repository.**

- no personal projects;
- no manuscripts, research, notes, roadmaps, handoffs, production rules, private prompts, private settings, or user/client data;
- no payloads copied from Personal Forge, chats, uploads, or another private repository;
- no real project directory under `mine/`, `projects/`, or any other path.

Only reusable system files and explicitly allowlisted synthetic examples belong here. Follow `PUBLIC_BOUNDARY.md` and run:

```bash
python tools/public_boundary_check.py
python tools/privacy_scan.py .
```

If a requested write contains real project material, stop and route it to the correct private repository instead.

### If mode is `private-copy`

This must be a separately created **private** copy of CTRL-FORGE. Real user work may live under `mine/` in that private copy.

A copied repository should switch to `private-copy` only after its owner has verified that repository visibility is private. Never switch canonical `MShneur/ctrl-forge` out of public mode.

## What CTRL-FORGE is

CTRL-FORGE provides durable project memory across sessions and AI systems:

- `forge/` — reusable system files;
- `mine/` — real user projects/settings only in a private copy; public templates/examples in canonical upstream.

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

This repo ships the Librarian. For reusable personas, workflows, and teams, use an appropriate external/private source rather than copying private project payloads into public CTRL-FORGE.
