# CVF GC-018 — W137-T1 Authorization

> Date: 2026-05-07  
> Tranche: W137-T1 — Post-Hardening Full Matrix Re-Run  
> Status: AUTHORIZED

## Decision

**AUTHORIZED.** W137-T1 may begin immediately.

W137 is authorized because W134, W135, and W136 each closed a bounded blocker:

- W134: pre-AI HTTP 400 for non-documentation trusted forms.
- W135: post-AI `competitor_review` output-validation false positive.
- W136: targeted `/api/execute` timeout-budget hardening for the residual
  `documentation` and `strategy_analysis` timeout forms.

The next necessary step is a fresh full matrix that records whether the combined
hardening improves the end-to-end trusted-form lane.

## Scope Lock

W137 is limited to:

- Re-running the Alibaba 12-journey trusted-form matrix under the combined
  W134/W135/W136 fixes.
- Re-running the DeepSeek 6-journey confirmatory matrix.
- Publishing evidence and a continuation decision.
- Running the live release gate if the matrix reaches the target threshold.

W137 must not:

- Add new trusted forms.
- Change provider routing or safety policy unless the matrix identifies a new
  root cause that requires a separate tranche.
- Claim perfect stability unless the evidence shows it.
- Print or commit raw provider keys.

## Closure Criteria

W137 can close as delivered only when:

- Alibaba reaches at least 11 accepted journeys out of 12.
- DeepSeek reaches 6 accepted journeys out of 6.
- No pre-AI HTTP 400 regression appears.
- The W135 `competitor_review` HTTP 422 false-positive class does not recur.
- The W136 residual `documentation` / `strategy_analysis` execute-route timeout
  class does not recur.
