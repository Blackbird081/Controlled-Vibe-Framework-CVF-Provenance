<!-- Memory class: FULL_RECORD -->
# CVF W137 Continuation Decision — Post-Hardening Full Matrix

**Date:** 2026-05-07  
**Tranche:** W137-T1 — Post-Hardening Full Matrix Re-Run  
**Decision:** CONTINUE_TO_W138_PROVIDER_COOLDOWN_MATRIX

## Evidence

| Lane | Evidence | Result |
|---|---|---|
| Alibaba 12-journey matrix | `docs/reviews/CVF_W137_RUNTIME_STABILITY_ALIBABA_EVIDENCE_2026-05-07.json` | FAIL target: 10/12 accepted, target >=11/12 |
| DeepSeek 6-journey confirmatory | `docs/reviews/CVF_W137_RUNTIME_STABILITY_DEEPSEEK_EVIDENCE_2026-05-07.json` | PASS: 6/6 accepted |

## What Stayed Closed

- W134 pre-AI HTTP 400 did not recur.
- W135 `competitor_review` HTTP 422 output-validation false positive did not recur.
- Browser context cascade did not recur.
- Route misses did not recur.

## Remaining Blocker

Alibaba still showed two sequential UI-matrix `execute_route_timeout` rows:

- `documentation`, journey 9, no `/api/execute` response captured before the
  browser evidence deadline.
- `strategy_analysis`, journey 12, no `/api/execute` response captured before
  the browser evidence deadline.

This is narrower than W134:

- Accepted journeys improved from 9/12 to 10/12.
- The post-AI HTTP 422 class is gone.
- The residual is now isolated to sequential Alibaba browser/UI matrix pacing.

## Continuation

Proceed to W138 with a provider-cooldown full matrix. W138 should not change
runtime product behavior unless the cooldown evidence still fails and points to
a route lifecycle bug. The immediate hypothesis is provider pacing/rate pressure
under back-to-back 12-journey Alibaba UI proof, not a trusted-form schema or
guard rejection.
