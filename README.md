# CTRL-FORGE

**A repo that remembers what your AI forgot.**

Your AI forgot everything. Again. You close the tab, come back tomorrow, and
it's a stranger — "what project? what decision? who are you?" You re-explain the
same context for the fourth time this week.

CTRL-FORGE is the repo that didn't forget. It's a durable folder your AI reads at
the start of every session so the work actually carries over — across days,
across chats, across different AIs entirely.

Free. Because the parts that hold your work together shouldn't cost $20 a month.

---

## The whole idea in three lines

- Your projects live in a repo, not in a chat window that evaporates.
- A small agent — **the Librarian** — knows where things go and what's still open.
- Any AI picks up exactly where the last one stopped, by reading two files.

---

## Two folders. That's the trick.

```
forge/   ← the system. You don't touch it. Updates replace it.
mine/    ← your stuff. Projects and settings. Updates never touch it.
```

They never mix, so updates never break your work and your work never breaks the
system. Update = "replace forge/, leave mine/ alone." No merge conflicts, ever.

---

## Start in 60 seconds

1. Click **Use this template** (green button, top right) → make it **Private**.
2. Clone your new private copy.
3. Make a project:

```bash
python tools/new_project.py "My First Project"
```

That's it. Open `mine/projects/example-project/` first to see what a project
looks like. Then tell any AI: *"Read AGENTS.md and continue my project."*

No Python? Everything still works — the Librarian is a set of instructions an AI
follows by hand. The scripts just make it faster and add safety checks.

---

## What the Librarian does

It's one small agent with one job that splits five ways: decide **where** work
goes, catch **duplicates** before they pile up, flag whether something's **done**,
point you at a **specialist** when you need one, and **write the handoff** before
you stop. Three buckets per project — `research/`, `decisions/`, `deliverables/` —
plus a `HANDOFF.md`. Not thirty folders. Three.

More in [`forge/agents/librarian.md`](forge/agents/librarian.md).

---

## Keeping it private, keeping it fresh

Want it private but still linked so you know when there's an update? That's the
normal case, and it's covered step-by-step in **[UPDATING.md](UPDATING.md)**.
Short version: use the template button, and run `python tools/check_update.py`
when you feel like checking. Nothing auto-updates. Nothing phones home except a
one-line version check you have to run yourself.

---

## The AI Duct Tape Collection

The future showed up early and forgot the manual. Everything's brilliant, nothing's
finished, and half of it forgets your name between Tuesday and Wednesday. These
are the strips of duct tape — free, because the parts that hold your work
together shouldn't cost a subscription.

They work on their own. Use one, or tape a few together:

- **[CTRL-FORGE](https://github.com/MShneur/ctrl-forge)** — Your AI forgot
  everything. Again. This is the repo that didn't.
- **[CTRL-AI](https://github.com/MShneur/CTRL-AI)** — Teaches your AI to say "I'm
  not sure" instead of confidently inventing a citation.
- **[R-Duck](https://github.com/MShneur/R-Duck)** — Autopilot. You mumble an idea,
  it hands back a plan with a straight face.
- **[Agents of AI](https://github.com/MShneur/Agents-of-AI)** — A cast of
  specialists. No coffee, no PTO, no LinkedIn updates.
- **[Ghost in the Loop](https://github.com/MShneur/ghost-in-the-loop)** — Moves
  work between AIs without dropping it down the stairs. Full chat export, handoffs.

---

## Honest limits

- Folders are not encryption. Private means *your private repo*, not "safe to put
  secrets in."
- Nothing marked final should go public without a human looking at it first. The
  Librarian reminds you; it doesn't decide for you.
- Stale is fine. Most people never update their tools and that's okay — the base
  keeps working. Updates are a recommendation, never forced.

---

## Contributing

Forks and remixes welcome — send the good stuff back upstream so it doesn't
vanish into a renamed copy. See [CONTRIBUTING.md](CONTRIBUTING.md). Bugs →
Issues. Ideas → Discussions. Private project data → never, please.

MIT licensed. Star it if it helps someone find it.
