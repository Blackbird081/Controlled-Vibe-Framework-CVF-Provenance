# CVF GC-018 — W138-T1 Authorization

> Date: 2026-05-07  
> Tranche: W138-T1 — Provider Cooldown Full Matrix  
> Status: AUTHORIZED

## Decision

**AUTHORIZED.** W138-T1 may begin immediately.

W138 is authorized because W137 proved combined hardening improved the matrix but
did not meet the Alibaba full-matrix target. The remaining failures are
sequential `execute_route_timeout` rows with no route response body, recurring
late in the Alibaba 12-journey browser/UI proof.

## Scope Lock

W138 is limited to:

- Re-running the same W137 trusted-form matrix with a longer inter-journey
  provider cooldown/backoff.
- Capturing whether the residual timeout class disappears under paced provider
  use.
- Publishing a continuation decision and release gate only if the target passes.

W138 must not:

- Add new trusted forms.
- Change product runtime behavior based only on test-harness pacing evidence.
- Claim perfect stability if the evidence does not show it.
- Print or commit raw provider keys.

## Closure Criteria

W138 can close as delivered only when:

- Alibaba reaches at least 11 accepted journeys out of 12.
- DeepSeek reaches 6 accepted journeys out of 6.
- No pre-AI HTTP 400 regression appears.
- No `competitor_review` HTTP 422 false-positive regression appears.
- No W137 residual `documentation` / `strategy_analysis` execute-route timeout
  regression appears.
