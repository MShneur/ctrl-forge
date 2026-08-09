# mine/ — private work in your copy, templates only upstream

This folder has **two different contexts**:

1. In your own **private CTRL-FORGE copy**, `mine/` is where your real projects and settings live and may be tracked normally.
2. In the canonical public `MShneur/ctrl-forge` repository, `mine/` is **template/example space only**. Personal project files must never be committed there.

The public upstream allowlist is intentionally narrow:

- `mine/README.md`
- `mine/settings.yaml` as the generic/default template
- `mine/projects/example-project/**`

Anything else under `mine/` must stay out of the public upstream.

## In a private copy

Typical contents are:

- **`settings.yaml`** — your version, agents, rules, and preferences.
- **`projects/`** — your actual work, one folder per project.
- **`agents/`** *(optional)* — your own personas.

Start a project:

```bash
python tools/new_project.py "My Project"
```

The `example-project` folder shows the expected structure.

## Before publishing or contributing

If you make your copy/fork public or send changes back upstream, delete personal `mine/` content first. Do not publish manuscripts, research, private prompts, project handoffs, client/user data, or personal settings. Run `python tools/public_boundary_check.py` against the public-upstream shape before publication.

See `PUBLIC_BOUNDARY.md` for the canonical policy.
