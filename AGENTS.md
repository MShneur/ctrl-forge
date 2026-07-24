# AGENTS.md

If you are an AI reading this repo, this is your entry point. It's short on
purpose.

## What this repo is

CTRL-FORGE gives you a durable place to keep project work so it survives between
sessions and between different AIs. Two folders that never mix:

- `forge/` — the system. You read it. You do not edit it.
- `mine/` — the user's projects and settings. You work here.

## What to do

1. **Read `forge/agents/librarian.md`.** That's your operating protocol.
2. **Read `forge/forge-config.yaml`.** It tells you the folder names — don't
   assume them, a user may have renamed things.
3. **Find the project** the user named, under the projects folder.
4. **If it doesn't exist,** create one minimal project folder — README,
   PROJECT_STATE.yaml, HANDOFF.md, and the three buckets. Nothing more.
5. **Read that project's state and handoff** before doing anything.
6. **Work only in that project.**
7. **Follow the rules** in `forge/rules/forge-rules.yaml` — check before you
   create, don't duplicate, keep final work out of research.
8. **Update state and HANDOFF.md before you stop.**
9. **Never claim work happened that you didn't verify** — a push, a fetch, a
   test result. Unverified is fine to report as unverified.
10. **Never publish private content, and never push anything `final` to a
    public place without a human approving it.**

That's it. The Librarian handles the detail. This file just gets you there.

## Need a specialist?

This repo ships one agent — the Librarian. For personas, workflows, and teams,
see [Agents of AI](https://github.com/MShneur/Agents-of-AI). Link, not bundle.
