# Contributing

Thank you for helping CTRL-FORGE become more useful instead of merely more complicated.

## Non-negotiable public boundary

The canonical `MShneur/ctrl-forge` repository is public. **Never contribute personal project data.** This includes manuscripts, research corpora, project handoffs, private prompts, private settings, client/user information, private Personal Forge material, or generated artifacts derived from private work.

Under `mine/`, upstream accepts only the explicit template/example allowlist documented in `PUBLIC_BOUNDARY.md`.

If you work from a real private copy of CTRL-FORGE, delete personal `mine/` content before making that copy public or contributing upstream. When uncertain, do not publish it.

## Good contributions

- clearer onboarding;
- safer privacy checks;
- better cross-AI handoffs;
- fixes to the project generator or validator;
- useful schemas;
- documentation that prevents repeated confusion;
- optional integrations that do not create vendor lock-in.

## Before opening a pull request

1. Search existing issues and pull requests.
2. Keep the change narrow.
3. Remove private/personal project content.
4. Disclose when a substantial part of the contribution was AI-generated.
5. Human-review every line you submit.
6. Run:

```bash
python tools/public_boundary_check.py
python tools/validate_forge.py
python tools/privacy_scan.py .
```

## Pull requests

A useful pull request says what changed, why, how it was verified, and what remains uncertain. One feature or fix per pull request is strongly preferred.

By contributing, you agree that your contribution is licensed under the repository's MIT License.
