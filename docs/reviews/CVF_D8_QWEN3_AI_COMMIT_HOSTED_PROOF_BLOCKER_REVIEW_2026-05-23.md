# CVF D8 Qwen3 AI Commit Hosted Proof Blocker Review - 2026-05-23

Memory class: FULL_RECORD

Status: RETURNED_BLOCKED_QWEN3_THINKING_ENABLE_THINKING_PARAMETER

## Purpose

Record the D8 hosted proof result after adding both Skill Preflight and
`aiCommit` metadata to the corrected Qwen3 thinking model payload.

## Authority

- GC-018:
  `docs/baselines/CVF_GC018_D8_QWEN3_AI_COMMIT_HOSTED_PROOF_2026-05-23.md`
- Work order:
  `docs/work_orders/CVF_WO_D8_QWEN3_AI_COMMIT_HOSTED_PROOF_2026-05-23.md`
- D7 blocker:
  `docs/reviews/CVF_D7_QWEN3_SKILL_PREFLIGHT_HOSTED_PROOF_BLOCKER_REVIEW_2026-05-23.md`
- Hosted target: `https://vibcode.netlify.app/api/execute`

## Scope / Target / Owner Boundary

Owner boundary: Qwen3 hosted proof payload contract only.

Target boundary: one hosted proof for `qwen3-235b-a22b-thinking-2507` with
Skill Preflight and `aiCommit`.

## Target / Source

Target: hosted signed `/api/execute` proof for the corrected Qwen3 thinking
model.

Source: D7 blocker and local guard-runtime simulation.

## Scope / Methodology

Method:

1. Add `aiCommit` metadata to the D7 proof payload.
2. Run local safety/enforcement/guard preflight.
3. Run exactly one hosted proof.
4. Stop on provider non-pass.

## Local Verification

Local preflight:

- Safety: PASS, `blocked=false`, `detailsCount=0`.
- Enforcement: PASS, `status=ALLOW`.
- Skill Preflight: `required=true`, `declared=true`, `source=explicit`.
- Guard runtime: PASS, `finalDecision=ALLOW`.
- Prompt length: `4736`.
- Depth classification: T1 local route-gate preflight, Meaningful for proving
  Skill Preflight and `aiCommit` satisfy pre-provider route guards.

Depth boundary:

- T2 integration coverage: hosted route proof was used as the integration
  surface.
- T3 browser/end-to-end coverage: not run; no browser behavior changed.
- T4 release-gate coverage: not run; D8 returned blocked.

## Hosted Proof Result

D8 reached the provider adapter and returned live governance evidence, but the
provider rejected the request parameter.

| Criterion | Required | Observed |
| --- | --- | --- |
| HTTP status | 200 | 200 |
| `success` | `true` | `false` |
| Decision | `ALLOW` | `ALLOW` |
| Routing decision | `ALLOW` | `ALLOW` |
| Enforcement status | `ALLOW` | `ALLOW` |
| Skill Preflight declared | `true` | `true` |
| Evidence mode | `live` | `live` |
| Provider | `alibaba` | `alibaba` |
| Requested model | `qwen3-235b-a22b-thinking-2507` | `qwen3-235b-a22b-thinking-2507` |
| Response model | requested model | `qwen3-235b-a22b-thinking-2507` |
| Receipt id | present | `rcpt-env-mpigd0wj-a8su8o` |
| Trace id | present | `env-mpigd0wj-a8su8o` |
| Policy snapshot | present | `pol-20260523-0002` |
| Error | none | `enable_thinking` restricted to true |
| Raw secret printed | false | false |

Sanitized hosted facts:

```json
{
  "httpStatus": 200,
  "durationMs": 2715,
  "success": false,
  "decision": "ALLOW",
  "routingDecision": "ALLOW",
  "enforcementStatus": "ALLOW",
  "skillPreflightDeclared": true,
  "evidenceMode": "live",
  "provider": "alibaba",
  "responseModel": "qwen3-235b-a22b-thinking-2507",
  "receiptId": "rcpt-env-mpigd0wj-a8su8o",
  "traceId": "env-mpigd0wj-a8su8o",
  "policySnapshotId": "pol-20260523-0002",
  "errorMessage": "<400> InternalError.Algo.InvalidParameter: The value of the enable_thinking parameter is restricted to True.",
  "rawSecretPrinted": false
}
```

## Findings / Position

Finding: D8 retired the pre-provider route blockers. The remaining blocker is
provider-adapter parameter selection. D4 applied `enable_thinking=false` to all
non-streaming Qwen3 models, but `qwen3-235b-a22b-thinking-2507` requires
`enable_thinking=true`.

Position: `RETURNED_BLOCKED_QWEN3_THINKING_ENABLE_THINKING_PARAMETER`.

## Decision / Recommendation / Disposition

Decision: return D8 blocked.

Recommendation: open D9 to split Qwen3 `enable_thinking` adapter behavior.

Disposition: no D8 retry allowed.

## Risk / Corrective Action

- Open D9.
- Split adapter behavior:
  - standard Qwen3 non-streaming models retain `enable_thinking=false`;
  - Qwen3 thinking model ids use `enable_thinking=true`.
- Add focused provider tests for both branches.
- Run one hosted proof after local checks pass.

## Evidence Trace Block

Claim: D8 reached the Alibaba provider path with live governance evidence, but
failed because the thinking model requires `enable_thinking=true`.

Evidence:

- local safety/enforcement/guard preflight PASS;
- hosted HTTP 200;
- hosted `success=false`;
- hosted decision/routing/enforcement all `ALLOW`;
- hosted `evidenceMode=live`;
- hosted receipt `rcpt-env-mpigd0wj-a8su8o`;
- hosted trace `env-mpigd0wj-a8su8o`;
- sanitized provider error states `enable_thinking` is restricted to true;
- `rawSecretPrinted=false`.

Verdict:

- D8 is blocked.
- D9 must correct adapter parameter branching.

## Claim Boundary

D8 does not claim corrected-model pass, broad Qwen3 stability, hosted SaaS
readiness, production readiness, or freeze release.
