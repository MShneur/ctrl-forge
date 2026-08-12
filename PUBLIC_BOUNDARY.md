# Public Boundary Policy

`MShneur/ctrl-forge` is the **canonical public template/system repository**. It is not a project workspace.

## Hard rule

**No personal or project-specific material belongs in this repository.**

That includes, without limitation:

- real project files or project directories;
- manuscripts, books, artwork production rules, research, notes, plans, roadmaps, or handoffs;
- private prompts, settings, credentials, client/user data, or generated artifacts derived from private work;
- payloads copied from Personal Forge or any other private repository;
- project-specific content placed anywhere in the repository, not only under `mine/`.

The canonical public upstream may contain only reusable CTRL-FORGE system files plus deliberately synthetic public templates/examples that are explicitly allowlisted by `tools/public_boundary_check.py`.

## Repository mode

`REPO_MODE.yaml` ships with:

```yaml
mode: public-template-upstream
```

That value is intentional for this public repository and must remain unchanged here.

### When someone makes a private copy

CTRL-FORGE is designed to be copied into a **private repository** for real use. After making a copy:

1. verify the new repository is private;
2. change `REPO_MODE.yaml` to `mode: private-copy`;
3. only then place real personal/project work under `mine/` in that private copy.

If the copy will remain public, leave it in `public-template-upstream` mode and keep it template/example-only.

## Public upstream allowlist

The public boundary is repository-wide and fail-closed. `tools/public_boundary_check.py` permits only explicitly listed reusable system paths and synthetic example paths. A new arbitrary root file or directory is rejected until it is deliberately reviewed and added to the public allowlist.

Under `mine/`, public upstream allows only:

- `mine/README.md`;
- `mine/settings.yaml` as generic/default template data;
- `mine/projects/example-project/**` as synthetic example content.

Real `mine/projects/<project>/**` content is forbidden upstream.

Top-level `projects/**` is also forbidden. There is no public project-workspace directory in canonical CTRL-FORGE.

## Agents and automation

Agents, bots, scheduled workers, Repo Nanny, scripts, and maintainers must treat this boundary as fail-closed:

- never copy project payloads from Personal Forge or another private source into public `ctrl-forge`;
- never use public `ctrl-forge` as a handoff destination for real work;
- never infer that a path is safe merely because it sits outside `mine/`;
- when uncertain whether material is personal or project-specific, do not publish it;
- before every public push, run `python tools/public_boundary_check.py` and `python tools/privacy_scan.py .`.

## Accidental publication

If personal/project material reaches the public repository:

1. preserve any needed private copy in the appropriate private repository first;
2. remove the material from the public tree immediately;
3. assess and, when appropriate, rewrite reachable Git history;
4. strengthen the boundary test that failed to catch it;
5. assume copies, caches, clones, or indexes may already exist and do not claim deletion can recall them.

This policy governs the canonical public upstream. Private copies may track their owners' real work after they deliberately switch `REPO_MODE.yaml` to `private-copy`.
