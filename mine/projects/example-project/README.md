# Example Project

This folder exists so you can see what a project looks like without building one
first. Nothing here is special — copy the shape, then delete it.

## The layout

Every project has the same small skeleton:

- **`PROJECT_STATE.yaml`** — what this project is, in a few lines.
- **`HANDOFF.md`** — what's open right now. The next session reads this first.
- **`research/`** — inputs, sources, things you're still figuring out.
- **`decisions/`** — calls you've made, written down *with the reasoning* so you
  don't relitigate them in three weeks.
- **`deliverables/`** — finished output that's meant to leave the project.

## Why three buckets and not thirty

Because you can inherit three buckets in thirty seconds. If a project genuinely
needs more structure, add it — but nothing gets created by default that you
didn't ask for. That's the whole idea: no sprawl, no ceremony, no forty folders
you're scared to touch.

## What usually goes where

- A half-read paper, a screenshot, a link dump → `research/`
- "We're using Postgres, not Mongo, because X" → `decisions/`
- The actual finished thing → `deliverables/`
- "Next person: the auth flow is half-done" → `HANDOFF.md`

Do whatever you want with it. This is just what we found works best.
