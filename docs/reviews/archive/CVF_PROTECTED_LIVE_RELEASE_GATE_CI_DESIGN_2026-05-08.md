<!-- Memory class: FULL_RECORD -->
# CVF Protected Live Release Gate CI Design

**Date:** 2026-05-08
**Workflow:** `.github/workflows/cvf-protected-live-release-gate.yml`

## Design

| Control | Design |
|---|---|
| Not default PR CI | `workflow_dispatch` only; no `pull_request` trigger. |
| Operator confirmation | Requires input `confirm_live_provider_cost=RUN_LIVE_GATE`. |
| Protected execution | Uses environment `cvf-live-release-gate` for repository-side approval/secret policy. |
| Secret source | Repository/organization secrets only; no committed `.env`. |
| Canonical proof | Runs `python scripts/run_cvf_release_gate_bundle.py --json`. |
| Artifact | Uploads `cvf-protected-live-release-gate-result.json`. |

## Boundary

CI1 remains the default no-secret guardrail. CI2 is a protected/manual live
lane for release-quality proof and must fail without configured live provider
secrets.
