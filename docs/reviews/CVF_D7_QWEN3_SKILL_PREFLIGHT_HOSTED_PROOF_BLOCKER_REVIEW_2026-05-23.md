# CVF D7 Qwen3 Skill Preflight Hosted Proof Blocker Review - 2026-05-23

Memory class: FULL_RECORD

Status: RETURNED_BLOCKED_HOSTED_AI_COMMIT_GUARD

## Purpose

Record the D7 result after adding the route-required Skill Preflight
declaration to the corrected Qwen3 hosted proof payload.

## Authority

- GC-018:
  `docs/baselines/CVF_GC018_D7_QWEN3_SKILL_PREFLIGHT_HOSTED_PROOF_2026-05-23.md`
- Work order:
  `docs/work_orders/CVF_WO_D7_QWEN3_SKILL_PREFLIGHT_HOSTED_PROOF_2026-05-23.md`
- D6 blocker:
  `docs/reviews/CVF_D6_QWEN3_THINKING_MODEL_ID_CORRECTION_BLOCKER_REVIEW_2026-05-23.md`
- Hosted target: `https://vibcode.netlify.app/api/execute`

## Target / Source

Target: hosted signed `/api/execute` proof for
`qwen3-235b-a22b-thinking-2507`.

Source: D6 blocker and the existing Skill Preflight contract in
`enforcement.ts`.

## Scope / Methodology

Method:

1. Built one hosted proof payload for `qwen3-235b-a22b-thinking-2507`.
2. Added explicit Skill Preflight fields:
   - `skillPreflightPassed: true`;
   - `skillPreflightDeclaration` containing `SKILL PREFLIGHT PASS`;
   - `skillPreflightRecordRef` pointing to the D6 blocker;
   - `skillIds` containing `CVF_D7_HOSTED_QWEN3_PROOF`.
3. Ran local safety and enforcement preflight.
4. Ran exactly one signed hosted proof call.
5. Stopped on non-pass.

## Local Verification

Local preflight:

- Safety: PASS, `blocked=false`, `detailsCount=0`.
- Enforcement: PASS, `status=ALLOW`.
- Skill Preflight: `required=true`, `declared=true`, `source=explicit`.
- Prompt length: `4736`.
- Depth classification: T1 local route-gate preflight, Meaningful for the
  Skill Preflight blocker retired by D7.

Local guard simulation after hosted failure:

- Result: BLOCK without `aiCommit`.
- Blocking guard: `ai_commit`.
- Reason: missing `ai_commit` metadata for a modifying action.
- Depth classification: T1 local guard-runtime contract inspection,
  Meaningful for identifying the next exact payload field.

Depth boundary:

- T2 integration coverage: not run; hosted route proof was the integration
  surface.
- T3 browser/end-to-end coverage: not run; no UI workflow changed.
- T4 release-gate coverage: not run; D7 returned blocked.

## Hosted Proof Result

The single D7 hosted call did not pass.

| Criterion | Required | Observed |
| --- | --- | --- |
| HTTP status | 200 | 400 |
| `success` | `true` | `false` |
| Decision | `ALLOW` | `BLOCK` |
| Routing decision | `ALLOW` | not reached |
| Enforcement status | `ALLOW` | `ALLOW` |
| Skill Preflight declared | `true` | `true` |
| Evidence mode | `live` | not reached |
| Provider | `alibaba` | `alibaba` |
| Requested model | `qwen3-235b-a22b-thinking-2507` | `qwen3-235b-a22b-thinking-2507` |
| Response model | requested model | `guard-blocked` |
| Receipt id | present | absent |
| Trace id | present | absent |
| Error | none | guard adjustment required |
| Raw secret printed | false | false |

Sanitized hosted facts:

```json
{
  "httpStatus": 400,
  "durationMs": 1787,
  "success": false,
  "decision": "BLOCK",
  "enforcementStatus": "ALLOW",
  "skillPreflightDeclared": true,
  "provider": "alibaba",
  "requestedModel": "qwen3-235b-a22b-thinking-2507",
  "responseModel": "guard-blocked",
  "errorMessage": "We need to adjust your request for better results.",
  "rawSecretPrinted": false
}
```

## Findings / Position

Finding: D7 retired the Skill Preflight blocker but exposed the next route
guard requirement. Hosted execution is blocked by the guard runtime because a
BUILD-class request with Skill Preflight is treated as a modifying action and
requires `aiCommit` metadata.

Position: `RETURNED_BLOCKED_HOSTED_AI_COMMIT_GUARD`.

## Decision / Recommendation / Disposition

Decision: return D7 blocked.

Recommendation: open D8 with explicit `aiCommit` metadata.

Disposition: no D7 retry allowed.

## Risk / Corrective Action

Risk:

- The corrected Qwen3 thinking model still has not reached provider execution
  on the hosted route.

Corrective action:

- Open a fresh D8 authorization.
- Use the same Skill Preflight-compliant payload plus explicit `aiCommit`
  metadata.
- Do not weaken the guard runtime.

## Evidence Trace Block

Claim: D7 proved Skill Preflight declaration is accepted, but hosted proof is
blocked before provider dispatch by missing `aiCommit` metadata.

Evidence:

- local safety preflight PASS;
- local enforcement preflight PASS with Skill Preflight declared;
- hosted HTTP 400;
- hosted `success=false`;
- hosted `enforcementStatus=ALLOW`;
- hosted `skillPreflightDeclared=true`;
- hosted `responseModel=guard-blocked`;
- local guard simulation identifies blocking guard `ai_commit`;
- `rawSecretPrinted=false`.

Verdict:

- D7 is blocked.
- Next exact payload requirement is `aiCommit`.

## Claim Boundary

D7 does not claim corrected-model hosted access, P3 pass, Qwen3 stability,
hosted SaaS readiness, production readiness, or freeze release.
