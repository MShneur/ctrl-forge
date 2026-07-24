# Security Policy

## Reporting a vulnerability

Do not open a public issue containing an exploit, credential, private data, or a reproducible vulnerability that puts users at risk.

Use GitHub private vulnerability reporting when available. Otherwise contact the maintainer privately through the GitHub profile with:

- affected version or commit;
- impact;
- reproduction steps;
- suggested mitigation, if known.

## Scope

CTRL-FORGE is primarily a file-based workflow. The highest-risk failures are:

- secrets committed to Git;
- private project history published accidentally;
- unsafe automation or shell execution;
- path traversal in project creation;
- public release files copied from private zones without review.

Run `python tools/privacy_scan.py .` before release. It is a guardrail, not proof of safety.
