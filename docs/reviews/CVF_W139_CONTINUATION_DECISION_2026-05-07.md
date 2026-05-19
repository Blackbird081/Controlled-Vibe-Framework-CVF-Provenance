<!-- Memory class: FULL_RECORD -->
# CVF W139 Continuation Decision — Direct API Matrix Diagnostic

**Date:** 2026-05-07  
**Tranche:** W139-T1 — Direct API Matrix Diagnostic  
**Decision:** CONTINUE_TO_W140_UI_BROWSER_LIFECYCLE_DIAGNOSTIC

## Evidence

| Lane | Evidence | Result |
|---|---|---|
| Alibaba direct API matrix | `docs/reviews/archive/CVF_W139_DIRECT_API_MATRIX_ALIBABA_EVIDENCE_2026-05-07.json` | PASS diagnostic: 12/12 accepted |
| DeepSeek direct API matrix | `docs/reviews/archive/CVF_W139_DIRECT_API_MATRIX_DEEPSEEK_EVIDENCE_2026-05-07.json` | PASS diagnostic: 6/6 accepted |

## Finding

The direct `/api/execute` matrix does not reproduce the W137/W138 late Alibaba
timeouts.

This narrows the remaining blocker:

- Not a trusted-form schema gap.
- Not W134 pre-AI authority gate regression.
- Not W135 `competitor_review` output-validation false positive.
- Not a general server/provider inability to process the 12-form sequence.
- Most likely in the browser/UI execution lifecycle used by
  `DynamicForm`/`ProcessingScreen` during repeated isolated-context journeys.

## Continuation

Proceed to W140 with browser/UI lifecycle diagnostics:

- capture request-fired/request-finished/request-failed events for
  `/api/execute`
- capture ProcessingScreen visible state and error state
- distinguish "request never sent" from "request sent but response not observed"
- keep direct API evidence separate from browser UI stability claims

W139 is diagnostic, not a release gate.
