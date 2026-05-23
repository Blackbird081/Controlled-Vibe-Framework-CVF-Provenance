# CVF D4 Qwen3 Enable Thinking Adapter Blocker Review — 2026-05-23

Memory class: FULL_RECORD

Status: RETURNED_BLOCKED_HOSTED_SAFETY_FILTER

## Purpose

Record the D4 implementation outcome and the hosted proof blocker without
claiming D4/P3 completion.

## Authority

- GC-018: `docs/baselines/CVF_GC018_D4_QWEN3_ENABLE_THINKING_ADAPTER_2026-05-23.md`
- Work order: `docs/work_orders/CVF_WO_D4_QWEN3_ENABLE_THINKING_ADAPTER_2026-05-23.md`
- Predecessor blocker: `docs/reviews/CVF_D3_QWEN3_PROVIDER_EXPANSION_BLOCKER_REVIEW_2026-05-23.md`
- Hosted target: `https://vibcode.netlify.app/api/execute`

## Target / Source

Target source files:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.test.ts`

Evidence sources:

- focused provider test output;
- full `cvf-web` suite attempts;
- one signed hosted proof call to the protected `/api/execute` endpoint.

## Scope / Methodology

Method:

1. Apply only the authorized additive Alibaba Qwen3 adapter parameter change.
2. Add focused unit assertions for the new Qwen3 request body behavior and the
   qwen-turbo negative case.
3. Run local verification.
4. Run the hosted proof sequence and stop immediately on the first non-200 or
   `success=false` result.

## Implementation Completed Before Blocker

Implemented the bounded provider adapter change in:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.test.ts`

Code change:

- added additive `isQwen3Model(model)` helper matching `^qwen3-`;
- injected `enable_thinking: false` only for Alibaba non-streaming Qwen3 calls;
- left streaming-only QVQ handling unchanged;
- left `qwen-turbo` and other non-Qwen3 model request bodies unchanged.

Test assertions added:

- `qwen3-32b` non-streaming request includes `enable_thinking: false`;
- `qwen3-235b-a22b-thinking` non-streaming request includes `enable_thinking: false`;
- `qwen-turbo` non-streaming request does not include `enable_thinking`.

## Local Verification

Focused D4 provider test:

- Command: `npm run test:run -- src/lib/ai/providers.test.ts`
- Directory: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`
- Result: PASS
- Test files: 1/1 PASS
- Tests: 42/42 PASS
- Depth classification: T1 unit/provider-adapter assertions, Meaningful for
  request-body regression coverage; T2 integration, T3 E2E, and T4 release-gate
  all-pass are not claimed by this focused run.

Full `cvf-web` suite did not produce a clean all-pass run during D4 due to
pre-existing live/test-order variance outside the D4 adapter surface:

- First full run: 218/219 files PASS, 2748/2751 tests PASS, one live retrieval
  test returned HTTP 400; isolated rerun of
  `src/app/api/execute/route.retrieval.live.test.ts` PASS 4/4.
- Second full run: 218/219 files PASS, 2748/2751 tests PASS, one
  `ProcessingScreen.test.tsx` analytics assertion failed; isolated rerun PASS
  21/21.
- Third full run with reduced file parallelism: 218/219 files PASS, 2748/2751
  tests PASS, one DeepSeek live-output regex assertion failed while the returned
  content was a structured operational handoff. This is provider-output
  variance and not caused by the D4 Qwen3 adapter change.

Because the D4 work order required `npm test:run` all PASS, that acceptance
criterion is not claimed as met.

## Findings / Position

Finding: the local D4 adapter change is implemented and focused tests pass, but
D4 cannot close because hosted proof did not pass and full-suite all-pass was
not achieved.

## Hosted Proof Attempt

Per work order stop rule, exactly one hosted proof call was attempted first for
`qwen3-32b`. The second model was not attempted after the first hosted proof
returned non-200 / `success=false`.

| Criterion | Required | Observed |
| --- | --- | --- |
| Model attempted | `qwen3-32b` first | `qwen3-32b` |
| HTTP status | 200 | 400 |
| `success` | `true` | `false` |
| Provider | `alibaba` | `alibaba` |
| Response model | requested model | `blocked` |
| Error | none | `Safety filter triggered` |
| Receipt present | required on pass | not returned in sanitized body |
| Trace present | required on pass | not returned in sanitized body |
| Raw secret printed | `false` | `false` |

Sanitized hosted result:

```json
{
  "model": "qwen3-32b",
  "httpStatus": 400,
  "success": false,
  "provider": "alibaba",
  "responseModel": "blocked",
  "errorMessage": "Safety filter triggered",
  "rawSecretPrinted": false
}
```

## Disposition

D4 cannot be closed as a completion packet.

The local adapter fix is implemented and focused unit evidence passes, but the
hosted proof matrix did not pass because the hosted `/api/execute` request was
blocked by safety filtering before a successful governed model execution could
be recorded.

Per work order, no retry loop was run and `qwen3-235b-a22b-thinking` was not
attempted.

## Risk / Corrective Action

Risk:

- The hosted protected workflow remains unable to prove the two-model D4/P3
  matrix under this work order.
- The current hosted safety filter blocks the attempted `qwen3-32b` payload
  before a successful receipt-backed model execution is returned.

Corrective action:

- Stop D4.
- Require a fresh GC-018/work order to decide whether the next bounded move is
  payload reframing, hosted safety-filter inspection, deployment confirmation,
  or blocked closure with no further hosted attempt.

## Scope / Target / Owner Boundary

Owner boundary: CVF provider adapter / hosted proof tranche only.

Target boundary: Alibaba Qwen3 non-streaming request-body parameter behavior
and one hosted protected proof sequence.

Out of scope:

- route/auth/receipt schema changes;
- provider capability registry changes;
- vision/reasoning contract changes;
- public-sync work;
- broad Qwen3 stability or production-readiness claims.

## Claim Boundary

No claim is made that P3/D4 fully passes. No broad Qwen3 stability, production
readiness, hosted SaaS readiness, thinking-mode governance completeness,
all-provider parity, public-sync update, receipt-envelope change, route/auth
change, vision/reasoning contract change, or freeze release is claimed.

## Next Allowed Move

Stop under the D4 work order.

A fresh GC-018/work order is required to decide whether the next move is:

- sanitize/reframe the hosted proof payload to avoid hosted safety-filter block;
- inspect hosted safety-filter policy/configuration;
- deploy the adapter fix before a new hosted proof attempt, if deployment was
  not already active;
- or close D4 as blocked with no further retry.
