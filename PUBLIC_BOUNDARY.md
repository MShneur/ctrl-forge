# Public Boundary Policy

`MShneur/ctrl-forge` is the **public template/system repository**. It must never contain the owner's personal project files, manuscripts, research, private prompts, private settings, client/user data, or other personal work product.

## Public upstream rule

The public upstream may contain only reusable system files plus deliberately public examples/templates. Under `mine/`, the only tracked content allowed in the public upstream is:

- `mine/README.md`
- `mine/settings.yaml` as the generic template/default
- `mine/projects/example-project/**`

Any other tracked path under `mine/` is a policy violation and must fail CI.

## Copies and forks

CTRL-FORGE is designed to be copied into a **private** repository for real use. In a private copy, users may keep their personal work under `mine/` and track it normally.

Before making a copy/fork public, publishing it, or contributing changes back upstream, remove all personal `mine/` content and verify that only the public template/example allowlist remains. If personal material was committed to a public copy by mistake, remove it from the public tree immediately and assess whether Git history also needs rewriting.

## Agent and automation rule

Agents, bots, scheduled workers, Repo Nanny, scripts, and maintainers must treat this boundary as fail-closed:

- never copy project payloads from Personal Forge or any other private repo into public `ctrl-forge`;
- never use `mine/` in public upstream as a project handoff destination;
- never push generated manuscripts, research corpora, private prompts, or project artifacts here;
- when uncertain whether material is personal, stop and require human approval before publication;
- public examples must be synthetic/generic and intentionally designated as examples.

## Enforcement

`tools/public_boundary_check.py` is run by GitHub Actions for the canonical public upstream and fails if tracked `mine/` paths exceed the explicit allowlist.

This policy is a publication boundary, not a statement that private copies should stop tracking their own work.
