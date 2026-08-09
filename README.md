# CTRL-FORGE

**A repo that remembers what your AI forgot.**

CTRL-FORGE is a durable folder your AI reads at the start of each session so work carries over across days, chats, and AI systems.

> **Public/privacy boundary:** this repository is the public template/system upstream. Real personal work belongs only in a **private copy**. The canonical upstream must never contain personal projects, manuscripts, research, private prompts, or other private project payloads. See [PUBLIC_BOUNDARY.md](PUBLIC_BOUNDARY.md).

---

## The whole idea in three lines

- Your projects live in a repo, not in a chat window that evaporates.
- A small agent — **the Librarian** — knows where things go and what's still open.
- Any AI picks up where the last one stopped by reading the durable project state.

---

## Two folders. That's the trick.

```text
forge/   ← the reusable system
mine/    ← your private work in your private copy; templates/examples only upstream
```

They stay separated so system updates do not overwrite project work.

---

## Start in 60 seconds

1. Click **Use this template** → make your copy **Private**.
2. Clone your private copy.
3. Make a project:

```bash
python tools/new_project.py "My First Project"
```

Open `mine/projects/example-project/` to see the public example structure.

---

## Public copies and forks

If you publish a copy/fork or contribute back to this public upstream, remove all personal `mine/` content first. The canonical upstream CI permits only the documented template/example allowlist under `mine/`. Private copies may track their real project work normally.

Run:

```bash
python tools/public_boundary_check.py
```

before publishing an upstream-shaped copy.

---

## What the Librarian does

The Librarian routes work, catches duplicates, checks readiness, points to specialists, and writes handoffs. More in [`forge/agents/librarian.md`](forge/agents/librarian.md).

---

## Keeping it private, keeping it fresh

The normal setup is a private copy linked conceptually to this public template. See **[UPDATING.md](UPDATING.md)**. Nothing auto-updates.

---

## Honest limits

- Folders are not encryption. Private means a private repository with appropriate access controls.
- Nothing private or final should go public without human review.
- CI reduces accidental publication risk but cannot undo data that was already copied, cloned, cached, or published elsewhere.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Public contributions must contain no personal project data.

MIT licensed.
