# Getting your own private copy, and keeping it fresh

You want CTRL-FORGE, but you want it **private** — your projects are nobody's
business. GitHub won't let you fork a public repo into a private one, so here's
the way that actually works. Two options, pick one.

## Option A — the easy button (recommended)

1. Go to the [CTRL-FORGE repo](https://github.com/MShneur/ctrl-forge).
2. Click the green **Use this template** button → **Create a new repository**.
3. Set it to **Private**. Name it whatever you like.

Done. You now have your own private copy. It is not a fork — nobody can see it,
and it's fully yours. Your work goes in `mine/`. You never edit `forge/`.

## Option B — the command-line way

```bash
git clone --bare https://github.com/MShneur/ctrl-forge.git
cd ctrl-forge.git
git push --mirror https://github.com/YOU/your-private-repo.git
cd .. && rm -rf ctrl-forge.git
```

Same result: a private repo of your own.

## Staying linked (so you know when there's an update)

Your copy doesn't auto-update — and that's on purpose. Nothing reaches out and
changes your files behind your back. Instead, one command tells you if there's a
newer version:

```bash
python tools/check_update.py
```

It reads a version number and prints one line. That's the whole thing — it
downloads nothing and runs nothing. If it says there's an update and you want
it, then (and only then):

```bash
git remote add upstream https://github.com/MShneur/ctrl-forge.git   # first time only
git fetch upstream
git checkout upstream/main -- forge/                                 # updates ONLY forge/
```

That last line replaces the `forge/` folder and leaves `mine/` untouched. Your
projects and settings don't move.

## A small ask

CTRL-FORGE is free and always will be. If it saves your work from vanishing
between chats:

- **Star** [the original](https://github.com/MShneur/ctrl-forge) so other people
  can find it.
- **Keep the credit** — the MIT license just needs the notice left in. That's the
  only actual requirement.
- **Send improvements home** instead of letting them disappear into a renamed
  copy nobody else can use.

Free means free. A star and a link back is the whole tab.
