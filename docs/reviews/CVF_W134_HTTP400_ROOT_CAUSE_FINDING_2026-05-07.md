# CVF W134 CP2/CP3 — HTTP 400 Root Cause Finding

**Tranche:** W134-T1 — Pre-AI-Call HTTP 400 Root Cause Fix  
**Date:** 2026-05-07  
**Status:** ROOT CAUSE FIXED FOR TARGETED EMAIL TEMPLATE PROBE

## CP2 Finding

The targeted `email_template` probe captured the exact `/api/execute` response
body before the fix.

Observed pre-fix result:

- HTTP status: `400`
- Elapsed: `2453ms`
- Route path: `guard_block`
- `guardResult.blockedBy`: `authority_gate`
- `enforcement.status`: `ALLOW`
- `specGate.status`: `PASS`

The body showed that `/api/execute` passed the full generated form intent as the
Guard Runtime `action` when no explicit request action was supplied.

Authority gate then evaluated a Vietnamese email intent as the action:

```text
INTENT:
Tôi muốn soạn email Email giới thiệu dịch vụ tư vấn.
...
```

For `HUMAN` in `INTAKE`, the allowed actions were:

```text
approve, reject, scope, read, ask, analyze
```

Because the generated email intent did not contain an allowed English action
verb, Authority Gate returned `BLOCK` before provider execution.

This explains why documentation was the outlier: the documentation intent
pattern contains an English `Analyze the subject...` success criterion, so it
accidentally satisfied the authority action allow-list.

## CP3 Fix

Two narrow changes were made:

- `ProcessingScreen` now sends `action: "analyze template execution request"`
  with governed non-build form executions. Build-phase executions retain a
  build action (`"build template execution request"`) so mutation-oriented
  guard checks are not weakened.
- `/api/execute` now falls back to the same normalized action when callers omit
  `action` (`analyze...` for non-build, `build...` for BUILD/file-scope/skill
  preflight requests), instead of using the full generated user intent as the
  authority verb.

The original `intent` remains present for prompt construction, enforcement,
safety checks, and evidence. Only the Guard Runtime authority action is
normalized.

## Targeted Post-Fix Evidence

`tests/e2e/w134-http400-root-cause.live.spec.ts` was re-run after the fix.

Observed post-fix result:

- HTTP status: `200`
- Route path: `success`
- Provider: Alibaba / `qwen-plus`
- `guardResult.finalDecision`: `ALLOW`
- `authority_gate`: `ALLOW`
- `governanceEvidenceReceipt.decision`: `ALLOW`

Evidence JSON:

- `docs/reviews/CVF_W134_HTTP400_EMAIL_TEMPLATE_PROBE_2026-05-07.json`

## Boundary

This fixes the targeted pre-AI 400 authority-gate blocker for the
`email_template` probe. W134 is not closed until CP4 Alibaba 12-journey, CP5
DeepSeek 6-journey, CP6 continuation decision, and CP7 release gate pass.
