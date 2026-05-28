# CVF D6 Qwen3 Thinking Model ID Correction Blocker Review - 2026-05-23

Memory class: FULL_RECORD

Status: RETURNED_BLOCKED_HOSTED_SKILL_PREFLIGHT_GATE

## Purpose

Record the D6 result after correcting the Alibaba Qwen3 thinking model id from
`qwen3-235b-a22b-thinking` to `qwen3-235b-a22b-thinking-2507`.

D6 does not close the hosted Qwen3 matrix because the single authorized hosted
proof call stopped at the route-level Skill Preflight gate before provider
execution.

## Authority

- GC-018:
  `docs/baselines/CVF_GC018_D6_QWEN3_THINKING_MODEL_ID_CORRECTION_2026-05-23.md`
- Work order:
  `docs/work_orders/CVF_WO_D6_QWEN3_THINKING_MODEL_ID_CORRECTION_2026-05-23.md`
- D5 blocker:
  `docs/reviews/CVF_D5_QWEN3_HOSTED_SAFE_PAYLOAD_RERUN_BLOCKER_REVIEW_2026-05-23.md`
- Hosted target: `https://vibcode.netlify.app/api/execute`

## Target / Source

Target validation surface:

- Model Gateway Alibaba capability metadata;
- `cvf-web` Alibaba Qwen3 provider adapter assertion coverage;
- hosted signed service-token `/api/execute` path for
  `qwen3-235b-a22b-thinking-2507`.

Evidence sources:

- source diff replacing the old model id with the official `-2507` id;
- Model Gateway focused test and check;
- `cvf-web` focused provider test and check;
- local safety preflight of the hosted proof prompt text;
- one signed hosted service-token call.

## Scope / Methodology

Method:

1. File fresh D6 GC-018 and work order.
2. Replace local registry, Alibaba capability JSON, and tests from
   `qwen3-235b-a22b-thinking` to `qwen3-235b-a22b-thinking-2507`.
3. Re-run focused Model Gateway and `cvf-web` provider assertions.
4. Run TypeScript checks for Model Gateway and `cvf-web`.
5. Preflight the hosted prompt text through current local `applySafetyFilters()`.
6. Run exactly one hosted proof call for `qwen3-235b-a22b-thinking-2507`.
7. Stop on first non-pass and file this blocker.

## Local Verification

Model Gateway targeted registry test:

- Command: `npm test -- tests/provider-capability-registry.test.ts`
- Directory: `EXTENSIONS/CVF_MODEL_GATEWAY`
- Result: PASS
- Test files: 1/1 PASS
- Tests: 7/7 PASS
- Depth classification: T1 unit/registry contract coverage, Meaningful for
  the corrected Alibaba capability metadata.

`cvf-web` targeted provider adapter test:

- Command: `npm run test:run -- src/lib/ai/providers.test.ts`
- Directory: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`
- Result: PASS
- Test files: 1/1 PASS
- Tests: 42/42 PASS
- Depth classification: T1 unit/provider-adapter request-body coverage,
  Meaningful for preserving Qwen3 non-streaming adapter behavior with the
  corrected model id.

TypeScript checks:

- `npm run check` in `EXTENSIONS/CVF_MODEL_GATEWAY` -> PASS
- `npm run check` in `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web` -> PASS
- Depth classification: T1 static type coverage, Meaningful for the touched
  TypeScript surfaces.

Governance hook chain:

- Command: `python governance/compat/run_local_governance_hook_chain.py --hook pre-push --parallel --max-workers 8`
- Result: PASS, 43/43 checks.

Safety preflight:

- Command class: local `npx tsx` one-shot script importing current
  `applySafetyFilters()`.
- Payload class: concrete strategy analysis prompt text.
- Result: PASS, `blocked=false`, `detailsCount=0`.
- Depth classification: T1 local guard preflight, Meaningful for confirming
  the one hosted proof payload was not locally safety-blocked before dispatch.

Depth boundary:

- T2 integration coverage: not run; D6 touched metadata/tests and the hosted
  route was exercised as live proof instead of adding a new local integration
  path.
- T3 browser/end-to-end coverage: not run; D6 did not change UI or browser
  workflow behavior.
- T4 release-gate coverage: not run; D6 is a narrow model-id correction and
  returned blocked before a release-quality claim could be made.

Source correction:

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/alibaba/capability.json`
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-capability-registry.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.test.ts`

All local references in the implementation/test target scope now use
`qwen3-235b-a22b-thinking-2507`.

## Hosted Proof Result

The single authorized hosted proof did not pass.

| Criterion | Required | Observed |
| --- | --- | --- |
| HTTP status | 200 | 400 |
| `success` | `true` | `false` |
| Decision | `ALLOW` | `BLOCK` |
| Routing decision | `ALLOW` | not reached |
| Enforcement status | `ALLOW` | `BLOCK` |
| Evidence mode | `live` | `live` |
| Provider | `alibaba` | `alibaba` |
| Requested model | `qwen3-235b-a22b-thinking-2507` | `qwen3-235b-a22b-thinking-2507` |
| Response model | requested model | `blocked` |
| Receipt id | present | `rcpt-env-mpifpjmo-1csbdv` |
| Trace id | present | `env-mpifpjmo-1csbdv` |
| Policy snapshot | present | `pol-20260523-0001` |
| Error | none | Skill Preflight declaration required |
| Output length | non-zero on pass | 0 |
| Raw secret printed | false | false |

Sanitized hosted response facts:

```json
{
  "httpStatus": 400,
  "durationMs": 5043,
  "success": false,
  "decision": "BLOCK",
  "enforcementStatus": "BLOCK",
  "evidenceMode": "live",
  "provider": "alibaba",
  "requestedModel": "qwen3-235b-a22b-thinking-2507",
  "responseModel": "blocked",
  "receiptId": "rcpt-env-mpifpjmo-1csbdv",
  "traceId": "env-mpifpjmo-1csbdv",
  "policySnapshotId": "pol-20260523-0001",
  "errorMessage": "Skill Preflight declaration is required before Build/Execute actions.",
  "outputLength": 0,
  "rawSecretPrinted": false
}
```

## Findings / Position

Finding 1: the D6 local model-id correction is implemented and locally covered.

Finding 2: the hosted proof did not reach provider execution. The route blocked
the request at the Skill Preflight declaration gate, so D6 cannot prove or
disprove hosted access to `qwen3-235b-a22b-thinking-2507`.

Position: `RETURNED_BLOCKED_HOSTED_SKILL_PREFLIGHT_GATE`.

## Disposition

D6 is blocked, not passed.

The previous D5 model-id/access blocker is narrowed but not fully retired:
local metadata now uses the corrected model id, but hosted provider execution
for that corrected id has not been observed because the request failed an
earlier route gate.

## Risk / Corrective Action

Risk:

- The two-model Qwen3 hosted matrix remains incomplete.
- A hosted proof payload that lacks the route-required Skill Preflight
  declaration can produce a governance `BLOCK` before the provider is called.

Corrective action:

- Stop D6.
- Require fresh GC-018/work order before any next hosted attempt.
- The next bounded move should build or reuse a hosted proof payload that
  satisfies the existing Skill Preflight declaration contract, then run one
  signed hosted proof call for `qwen3-235b-a22b-thinking-2507`.
- Do not weaken the route gate, safety filter, service-token auth, receipt
  schema, or provider adapter to make the proof pass.

## Scope / Target / Owner Boundary

Owner boundary: Qwen3 hosted proof / model-id correction tranche only.

Target boundary: local model-capability metadata and one hosted proof call for
`qwen3-235b-a22b-thinking-2507`.

Out of scope:

- route/auth/safety/receipt changes;
- bypassing Skill Preflight declaration;
- hosted retry loops;
- public-sync work;
- provider-runtime semantic changes beyond the already delivered D4
  `enable_thinking=false` adapter behavior;
- broad Qwen3 stability, hosted-readiness, production-readiness, or
  freeze-release claims.

## Evidence Trace Block

Claim: D6 corrected the local Qwen3 thinking model id but did not close the
hosted proof matrix because the single hosted proof returned a Skill Preflight
gate block before provider execution.

Evidence:

- Model Gateway focused registry test PASS 7/7;
- `cvf-web` focused provider test PASS 42/42;
- Model Gateway TypeScript check PASS;
- `cvf-web` TypeScript check PASS;
- safety preflight PASS with `blocked=false`;
- local governance hook chain PASS 43/43;
- hosted call HTTP 400, `success=false`, `decision=BLOCK`,
  `enforcementStatus=BLOCK`, `evidenceMode=live`;
- hosted receipt `rcpt-env-mpifpjmo-1csbdv`;
- hosted trace `env-mpifpjmo-1csbdv`;
- `rawSecretPrinted=false`.

Verdict:

- D6 local correction is complete.
- D6 hosted proof is blocked at Skill Preflight declaration.
- Full P3/D6 Qwen3 hosted matrix is not passed.

## Claim Boundary

This review claims only a local model-id correction plus a precisely classified
hosted proof blocker. It does not claim hosted access to the corrected thinking
model, full P3 pass, broad Qwen3 stability, thinking-mode governance
completeness, hosted SaaS readiness, production readiness, public deployment
readiness, public-sync readiness, Maika proof, persistence readiness, or freeze
release.

## Next Allowed Move

Default next move: stop.

Any next hosted proof for `qwen3-235b-a22b-thinking-2507` requires fresh
GC-018/work-order authorization. That work order must include the exact
Skill Preflight declaration payload shape or a route-level preflight proof
before making the single hosted call.
