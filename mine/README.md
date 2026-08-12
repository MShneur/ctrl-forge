# mine/ — private work in your copy, templates only upstream

Read `../REPO_MODE.yaml` first.

## Canonical public upstream

If `REPO_MODE.yaml` says:

```yaml
mode: public-template-upstream
```

then this repository is public template/system space. **Do not put real work here.** The only tracked `mine/` content allowed upstream is:

- `mine/README.md`;
- `mine/settings.yaml` as generic/default template data;
- `mine/projects/example-project/**` as a synthetic worked example.

Anything else under `mine/` must stay out of the public upstream. Real project content is also forbidden elsewhere in canonical public CTRL-FORGE, including top-level `projects/**`.

## In your private copy

After you create your own repository from this template:

1. verify the repository visibility is **Private**;
2. edit `REPO_MODE.yaml` to `mode: private-copy`;
3. then use `mine/` for your real projects and settings.

Typical private-copy contents are:

- `settings.yaml` — your version, agents, rules, and preferences;
- `projects/` — your actual work, one folder per project;
- `agents/` — optional private personas.

Start a project in a private copy:

```bash
python tools/new_project.py "My Project"
```

The `example-project` folder shows the expected structure.

## Before publishing or contributing upstream

Remove all personal/project material and return the public shape to template/example-only. Never publish manuscripts, research, private prompts, project handoffs, client/user data, personal settings, or real project artifacts.

Run:

```bash
python tools/public_boundary_check.py
python tools/privacy_scan.py .
```

See `PUBLIC_BOUNDARY.md` for the canonical policy.
