<!-- Memory class: FULL_RECORD -->
# CVF W134 Continuation Decision — CP4/CP5 Stability Re-Run

**Date:** 2026-05-07  
**Tranche:** W134 — Pre-AI-Call HTTP 400 Root Cause Fix  
**Decision:** PROCEED_TO_CP7_RELEASE_GATE

## Evidence

| Checkpoint | Evidence | Result |
|---|---|---|
| CP4 Alibaba 12-journey matrix | `docs/reviews/archive/CVF_W134_RUNTIME_STABILITY_ALIBABA_EVIDENCE_2026-05-07.json` | PASS: 9/12 accepted, target >=8/12 |
| CP4 Alibaba markdown packet | `docs/reviews/archive/CVF_W134_RUNTIME_STABILITY_ALIBABA_EVIDENCE_2026-05-07.md` | PASS: complete |
| CP5 DeepSeek 6-journey confirmatory | `docs/reviews/archive/CVF_W134_RUNTIME_STABILITY_DEEPSEEK_EVIDENCE_2026-05-07.json` | PASS: 6/6 accepted, target >=3/6 |
| CP5 DeepSeek markdown packet | `docs/reviews/archive/CVF_W134_RUNTIME_STABILITY_DEEPSEEK_EVIDENCE_2026-05-07.md` | PASS: complete |

## CP4 Alibaba Result

- Attempted journeys: 12
- Accepted with receipt: 9
- Target: >=8/12 accepted
- Live proof status: HTTP 200
- Live proof decision: ALLOW
- Outcome breakdown:
  - `accepted_with_exports`: 9
  - `mock_fallback_no_receipt`: 1
  - `api_timeout`: 2
  - `route_miss`: 0
  - `provider_error`: 0
  - `ui_flow_error`: 0

## CP5 DeepSeek Result

- Attempted journeys: 6
- Accepted with receipt: 6
- Target: >=3/6 accepted
- Outcome breakdown:
  - `accepted_with_exports`: 6
  - all other outcomes: 0

## Root Cause Closure

The W134 pre-AI HTTP 400 blocker is closed for this tranche.

The matrix exercised documentation and non-documentation trusted forms after the route-level guard action normalization fix. The previously failing non-documentation forms no longer reject immediately with HTTP 400 before provider execution. In the Alibaba matrix, accepted forms included `email_template`, `risk_assessment`, `user_persona`, `strategy_analysis`, `feature_prioritization`, and `pricing_strategy`. DeepSeek accepted all six confirmatory journeys.

## Remaining Boundary

W134 does not claim perfect multi-form runtime stability.

Residual Alibaba failures:

- `competitor_review`: HTTP 422 after enforcement ALLOW; response body reports generated response failed output validation after retry attempts. This is post-AI output validation, not the W134 pre-AI authority gate rejection.
- `documentation`: no `/api/execute` response captured before UI timeout.
- `strategy_analysis`: no `/api/execute` response captured before UI timeout.

These residuals are outside the closed root cause and should be treated as a future stability/output-validation hardening tranche if product posture requires a higher acceptance target than W134's release gate.

## Continuation Decision

Proceed to CP7 release gate because both W134 runtime targets passed:

- Alibaba: 9/12 accepted, target >=8/12
- DeepSeek: 6/6 accepted, target >=3/6

The CP7 gate must use live governance proof per CVF governance instructions.
