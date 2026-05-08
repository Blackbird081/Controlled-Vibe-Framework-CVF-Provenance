<!-- Memory class: FULL_RECORD -->
# CVF WPR-4 Public RC Tag Binding Closure Decision

Date: 2026-05-08

Status: CLOSED DELIVERED

## Decision

WPR-4 closes as the public release-candidate tag binding tranche.

The repository is prepared for annotated tag `v4.0.0-rc.1`.

## Updates

- `CHANGELOG.md` now contains the `v4.0.0-rc.1` entry.
- `README.md` version badge now uses `4.0.0-rc.1`.
- `docs/reference/CVF_RELEASE_NOTES_V4_0_0_RC_1_2026-05-08.md` created as the
  in-repo GitHub Release notes draft.
- `AGENT_HANDOFF.md` now records `RC1 TAGGED` posture and WPR-4 closure.

## Verification

- WPR-3 prerequisite:
  - PASS: public exposure audit has no unresolved blocker.
- `git diff --check`
  - PASS.
- `python scripts/run_cvf_release_gate_bundle.py --json`
  - PASS: Web build, TypeScript guard contract, provider readiness, secrets
    scan, docs governance, UI mock Playwright, and live governance Playwright.
- Annotated tag:
  - `v4.0.0-rc.1` is created after this closure packet is committed.

## Boundary

This is a release candidate, not GA.

WPR-4 changes no runtime behavior, provider behavior, deploy config, governance
policy, trusted-form corpus, RC truth packet, live evidence packet, or known
limitations packet.

GitHub Release publication remains operator/CLI-token dependent. The in-repo
release notes are the canonical draft for that publication step.
