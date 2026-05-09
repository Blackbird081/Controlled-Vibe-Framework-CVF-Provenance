<!-- Memory class: FULL_RECORD -->
# CVF DeepSeek Post-RC2 Confirmation Attempt 1 Failure

**Date:** 2026-05-09
**Status:** FAIL-CLOSED
**Provider lane:** DeepSeek
**Model:** `deepseek-chat`
**Test:** `tests/e2e/ds-confirmation-under-cq.live.spec.ts`

## Summary

| Field | Value |
|---|---|
| Target | N>=14 confirmation, 7 families with >=2 PASS each |
| Result | 13/14 PASS |
| Families with >=2 PASS | 6/7 |
| Failing family | `trusted_form` |
| Failing case | `ds-trusted-form-risk` |
| HTTP status | 400 |
| Failure class | `pre_ai_safety_filter_triggered` |

## Failure Detail

The run made live DeepSeek-governed calls for 14 confirmation cases under the
cost/quota preflight estimate. Thirteen cases returned HTTP 200 with governance
receipts. One case failed before provider execution because the local safety
filter rejected the generated prompt:

```text
success=false error=Safety filter triggered
```

The rejected prompt contained the literal word `secret` in the phrase
`secret redaction`, which matches the route-level sensitive-data filter.

## Boundary

- This attempt does not satisfy DeepSeek N>=14 confirmation wording.
- The failure does not prove a DeepSeek provider regression because the request
  was blocked before AI execution.
- A corrected rerun may replace the blocked wording with neutral credential
  terminology, then record a separate PASS/FAIL evidence artifact.
