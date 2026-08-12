# CTRL-FORGE

**A repo that remembers what your AI forgot.**

CTRL-FORGE is a durable project-memory system you copy into a private repository for real work.

> **IMPORTANT: THIS REPOSITORY IS PUBLIC.** `MShneur/ctrl-forge` is the reusable template/system upstream, not a place for anyone's real projects. Do not put personal projects, manuscripts, research, private prompts, handoffs, production files, user/client data, or other private work anywhere in this repository.

Read [`REPO_MODE.yaml`](REPO_MODE.yaml) and [`PUBLIC_BOUNDARY.md`](PUBLIC_BOUNDARY.md) before writing.

---

## Public upstream vs. your private copy

The canonical upstream ships in:

```yaml
mode: public-template-upstream
```

That mode stays locked here.

To use CTRL-FORGE for real work:

1. Click **Use this template** and create a **Private** repository.
2. Confirm the new repository is actually private.
3. In your private copy, edit `REPO_MODE.yaml` to:

```yaml
mode: private-copy
```

4. Then keep your real work under `mine/` in that private copy.

If your copy will be public, **do not switch modes**. Keep it template/example-only.

---

## The basic layout

```text
forge/   <- reusable system files
mine/    <- real work only in a private copy; synthetic examples only upstream
```

The public repository deliberately contains only reusable system material and explicitly allowlisted dummy/example content.

---

## Start a private copy

After switching your private copy to `mode: private-copy`:

```bash
python tools/new_project.py "My First Project"
```

`mine/projects/example-project/` is a synthetic worked example.

---

## Public boundary enforcement

Canonical public CTRL-FORGE uses a repository-wide fail-closed allowlist. Arbitrary new root files/directories and real project paths such as `projects/**` are rejected unless intentionally reviewed as public system/template content.

Before any public contribution, run:

```bash
python tools/public_boundary_check.py
python tools/privacy_scan.py .
```

If either check is uncertain, do not publish the material.

---

## What the Librarian does

The Librarian routes work, catches duplicates, checks readiness, points to specialists, and writes handoffs. More in [`forge/agents/librarian.md`](forge/agents/librarian.md).

---

## Keeping a private copy updated

See **[UPDATING.md](UPDATING.md)**. Nothing auto-updates.

---

## Honest limits

- Folders are not encryption. Real work belongs in a repository whose visibility is actually private.
- CI reduces accidental-publication risk but cannot recall data already copied, cloned, cached, or indexed.
- Never contribute private project content back to this public upstream.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Public contributions must contain reusable system/template material only.

MIT licensed.
