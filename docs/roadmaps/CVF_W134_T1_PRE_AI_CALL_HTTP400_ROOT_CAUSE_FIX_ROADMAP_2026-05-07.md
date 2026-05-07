# CVF W134-T1 Pre-AI-Call HTTP 400 Root Cause Fix Roadmap

> Authorization: `docs/baselines/CVF_GC018_W134_T1_PRE_AI_CALL_HTTP400_ROOT_CAUSE_FIX_AUTHORIZATION_2026-05-07.md`  
> Wave ID: W134  
> Status: CLOSED

## Problem

W133 resolved the browser/session cascade but exposed
`noncoder_pre_ai_call_http400_non_documentation_forms`. The documentation
template reaches live execution; trusted non-documentation forms return HTTP 400
before a useful AI result is observed.

## Checkpoints

| CP | Status | Work |
|---|---:|---|
| CP0 | COMPLETE | GC-018 authorization and scope lock |
| CP1 | COMPLETE | Capture HTTP 400 response body in targeted E2E evidence |
| CP2 | COMPLETE | Run one targeted `email_template` probe and identify exact route path |
| CP3 | COMPLETE | Fix root cause with narrow regression coverage |
| CP4 | COMPLETE | Alibaba 12-journey stability matrix: 9/12 accepted |
| CP5 | COMPLETE | DeepSeek 6-journey confirmatory matrix: 6/6 accepted |
| CP6 | COMPLETE | Continuation decision: proceed to CP7 |
| CP7 | COMPLETE | Release gate bundle with live governance E2E: PASS |

## Candidate Root Causes

- Guard/action mismatch: `/api/execute` may pass generated form intent as the
  guard action when no explicit action is supplied.
- Form field mismatch: UI-filled values may not match required template fields.
- Enforcement policy path: `evaluateEnforcement()` may block a subset before AI.
- Template category policy mismatch: category/risk mapping may be case-sensitive.

## Evidence Rules

Response bodies must be captured as bounded diagnostic snippets, with raw API
keys excluded. Live proof must use operator-supplied environment variables only.

## Closure Evidence

- Targeted root-cause probe:
  `docs/reviews/CVF_W134_HTTP400_EMAIL_TEMPLATE_PROBE_2026-05-07.json`
- Root-cause finding:
  `docs/reviews/CVF_W134_HTTP400_ROOT_CAUSE_FINDING_2026-05-07.md`
- Alibaba stability evidence:
  `docs/reviews/CVF_W134_RUNTIME_STABILITY_ALIBABA_EVIDENCE_2026-05-07.json`
- DeepSeek confirmatory evidence:
  `docs/reviews/CVF_W134_RUNTIME_STABILITY_DEEPSEEK_EVIDENCE_2026-05-07.json`
- Continuation decision:
  `docs/reviews/CVF_W134_CONTINUATION_DECISION_2026-05-07.md`

W134 closes the pre-AI HTTP 400 root cause. It does not claim perfect runtime
stability; residual post-AI output-validation and timeout issues are explicitly
left for later scoped work.
