# Contributing

Thank you for helping CTRL-FORGE become more useful instead of merely more complicated.

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
3. Do not include private project data, credentials, copied paid material, or confidential prompts.
4. Disclose when a substantial part of the contribution was AI-generated.
5. Human-review every line you submit.
6. Run:

```bash
python tools/validate_forge.py
python tools/privacy_scan.py .
```

## Recommendations

Use the **Recommendation** issue form for improvements that do not yet need code. Explain:

- the problem;
- who encounters it;
- the smallest useful change;
- any privacy or migration risk.

## Pull requests

A useful pull request says what changed, why, how it was verified, and what remains uncertain. One feature or fix per pull request is strongly preferred.

By contributing, you agree that your contribution is licensed under the repository's MIT License.
