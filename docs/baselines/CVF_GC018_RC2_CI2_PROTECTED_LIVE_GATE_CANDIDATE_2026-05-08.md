<!-- Memory class: FULL_RECORD -->
# CVF GC-018 RC2 CI2 Protected Live Gate Candidate

**Date:** 2026-05-08
**Scope:** Protected/manual live release gate workflow
**Decision:** AUTHORIZED FOR IMPLEMENTATION

## Authorized Work

- Add a manual GitHub Actions workflow for release-quality live proof.
- Require an explicit operator confirmation input before running.
- Use repository or organization secrets only.
- Run the canonical command: `python scripts/run_cvf_release_gate_bundle.py --json`.
- Upload the JSON result artifact.

## Boundary

This does not make live proof part of every PR. Hosted CI success cannot be
claimed until the workflow is pushed and manually run with configured secrets.
