# CVF GC-018 — W136-T1 Authorization

> Date: 2026-05-07  
> Tranche: W136-T1 — Execute Route Timeout Budget Hardening  
> Status: AUTHORIZED

## Decision

**AUTHORIZED.** W136-T1 may begin immediately.

W136 is authorized because W134/W135 closed the pre-AI HTTP 400 and targeted
post-AI `competitor_review` 422 blockers, leaving a narrower residual:
occasional Alibaba trusted-form journeys can exceed the browser evidence
deadline with no `/api/execute` response captured.

## Scope Lock

W136 is limited to:

- Bounding trusted noncoder template generation size.
- Preventing output-validation retry from starting when the route no longer has
  enough response budget to finish before the browser evidence deadline.
- Adding unit coverage for the latency-budget helpers and execute route provider
  options.
- Running targeted tests and live governance proof.

W136 must not:

- Disable provider calls, output validation, or governance receipts.
- Treat provider/model availability as changed without live evidence.
- Claim perfect multi-journey stability unless a full matrix proves it.
- Print or commit raw provider keys.

## Closure Criteria

W136 can close as delivered only when:

- Trusted noncoder forms pass a bounded `maxTokens` value into `executeAI`.
- Validation retry budget logic is covered by unit tests.
- Targeted route tests pass.
- Live governance release gate passes.
