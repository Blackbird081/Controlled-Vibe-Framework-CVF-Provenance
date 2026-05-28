# CVF D5 Qwen3 Hosted Safe Payload Rerun Blocker Review — 2026-05-23

Memory class: FULL_RECORD

Status: RETURNED_BLOCKED_QWEN3_235B_MODEL_ACCESS

## Purpose

Record the D5 hosted safe-payload rerun outcome without claiming the two-model
Qwen3 matrix as pass.

## Authority

- GC-018:
  `docs/baselines/CVF_GC018_D5_QWEN3_HOSTED_SAFE_PAYLOAD_RERUN_2026-05-23.md`
- Work order:
  `docs/work_orders/CVF_WO_D5_QWEN3_HOSTED_SAFE_PAYLOAD_RERUN_2026-05-23.md`
- D4 blocker:
  `docs/reviews/CVF_D4_QWEN3_ENABLE_THINKING_ADAPTER_BLOCKER_REVIEW_2026-05-23.md`
- Hosted target: `https://vibcode.netlify.app/api/execute`

## Target / Source

Target validation surface:

- hosted `/api/execute` protected workflow path;
- Alibaba provider lane;
- Qwen3 models `qwen3-32b` and `qwen3-235b-a22b-thinking`;
- D4 adapter behavior already committed in
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.ts`.

Evidence sources:

- safety-filter preflight using the current local `applySafetyFilters()` and
  `buildExecutionPrompt()` path;
- focused provider adapter tests;
- `cvf-web` TypeScript check;
- private provenance push to `origin/main`;
- two signed hosted service-token calls, one per allowed model order.

## Scope / Methodology

Method:

1. File fresh D5 GC-018 and work order.
2. Build a concrete `strategy_analysis` payload without known safety-filter
   trigger tokens.
3. Preflight the exact generated prompt text locally.
4. Re-run focused D4 provider adapter tests and `cvf-web` check.
5. Push private provenance `main` after confirming the remote is the private
   provenance repository, allowing the hosted deployment path to receive D4.
6. Run one hosted proof for `qwen3-32b`.
7. Run one hosted proof for `qwen3-235b-a22b-thinking` only after the first
   model passed.
8. Stop on the first non-pass and file this blocker.

## Local Verification

Safety preflight:

- Command class: local `npx tsx` one-shot script importing current
  `applySafetyFilters()` and `buildExecutionPrompt()`.
- Payload class: concrete `strategy_analysis`.
- `qwen3-32b`: PASS, `blocked=false`, prompt length `4814`.
- `qwen3-235b-a22b-thinking`: PASS, `blocked=false`, prompt length `4859`.

Focused D4 provider adapter test:

- Command: `npm run test:run -- src/lib/ai/providers.test.ts`
- Directory: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`
- Result: PASS
- Test files: 1/1 PASS
- Tests: 42/42 PASS
- Depth classification: T1 unit/provider-adapter request-body regression
  coverage, Meaningful for the D4 `enable_thinking=false` condition.

`cvf-web` check:

- Command: `npm run check`
- Directory: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`
- Result: PASS

Deployment posture:

- `git remote -v` confirmed private provenance remote:
  `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF-Provenance.git`
- `git push origin main` succeeded from provenance `main`.
- Pushed head for D5 authorization/deploy freshness: `6f0fbcd2`.
- Raw keys, service token, HMAC signature, and signed headers were not printed
  or recorded.

## Hosted Proof Results

The first hosted call passed, proving the hosted endpoint could execute the D4
adapter path for `qwen3-32b`.

| Criterion | Required | `qwen3-32b` observed |
| --- | --- | --- |
| HTTP status | 200 | 200 |
| `success` | `true` | `true` |
| Decision | `ALLOW` | `ALLOW` |
| Routing decision | `ALLOW` | `ALLOW` |
| Enforcement status | `ALLOW` | `ALLOW` |
| Evidence mode | `live` | `live` |
| Provider | `alibaba` | `alibaba` |
| Model | `qwen3-32b` | `qwen3-32b` |
| Receipt id | present | `rcpt-env-mpidzqv4-ysriei` |
| Trace id | present | `env-mpidzqv4-ysriei` |
| Policy snapshot | present | `pol-20260523-0001` |
| Output length | non-zero on pass | `5323` |
| Raw secret printed | `false` | `false` |

The second hosted call did not pass. Governance and routing were ALLOW/live,
but provider execution returned `success=false` because the named model is not
available to the hosted account or does not exist under that identifier.

| Criterion | Required | `qwen3-235b-a22b-thinking` observed |
| --- | --- | --- |
| HTTP status | 200 | 200 |
| `success` | `true` | `false` |
| Decision | `ALLOW` | `ALLOW` |
| Routing decision | `ALLOW` | `ALLOW` |
| Enforcement status | `ALLOW` | `ALLOW` |
| Evidence mode | `live` | `live` |
| Provider | `alibaba` | `alibaba` |
| Model | `qwen3-235b-a22b-thinking` | `qwen3-235b-a22b-thinking` |
| Receipt id | present | `rcpt-env-mpie0q8c-zn6jku` |
| Trace id | present | `env-mpie0q8c-zn6jku` |
| Policy snapshot | present | `pol-20260523-0002` |
| Error | none | model unavailable or no account access |
| Output length | non-zero on pass | `0` |
| Raw secret printed | `false` | `false` |

## Findings / Position

Finding: D5 resolves the D4 safety-filter payload blocker for the first Qwen3
model but does not close the two-model matrix.

Position:

- `qwen3-32b` is proven on the hosted governed path for this bounded payload.
- `qwen3-235b-a22b-thinking` is not proven because provider execution returned
  `success=false` for model availability/access.
- The next action is not a payload retry; it is model identifier/access
  verification under fresh authorization.

Sanitized second-call error:

```json
{
  "model": "qwen3-235b-a22b-thinking",
  "httpStatus": 200,
  "success": false,
  "decision": "ALLOW",
  "routingDecision": "ALLOW",
  "enforcementStatus": "ALLOW",
  "evidenceMode": "live",
  "provider": "alibaba",
  "responseModel": "qwen3-235b-a22b-thinking",
  "receiptId": "rcpt-env-mpie0q8c-zn6jku",
  "traceId": "env-mpie0q8c-zn6jku",
  "policySnapshotId": "pol-20260523-0002",
  "errorMessage": "The model `qwen3-235b-a22b-thinking` does not exist or you do not have access to it.",
  "outputLength": 0,
  "rawSecretPrinted": false
}
```

## Disposition

D5 cannot close as a full pass because the required second model did not return
`success=true`.

This blocker is not the D4 safety-filter problem. The D5 payload preflighted
clean and `qwen3-32b` passed the hosted matrix. The remaining blocker is model
availability/access for `qwen3-235b-a22b-thinking` on the hosted Alibaba lane.

## Risk / Corrective Action

Risk:

- The two-model P3/D5 Qwen3 matrix remains incomplete.
- The hosted account can execute `qwen3-32b`, but not the requested
  `qwen3-235b-a22b-thinking` identifier.

Corrective action:

- Stop D5.
- Require fresh GC-018/work order before any next hosted attempt.
- The next bounded move should verify the correct DashScope model identifier
  or provision hosted-account access for the intended thinking model, then run
  a single hosted proof call for that corrected/authorized model.

## Scope / Target / Owner Boundary

Owner boundary: CVF hosted proof / provider model availability tranche only.

Target boundary: two named Qwen3 hosted proof calls against the protected
`/api/execute` path.

Out of scope:

- safety-filter changes;
- route/auth/receipt-schema changes;
- provider registry or capability metadata changes;
- public-sync work;
- broad Qwen3 stability or hosted-readiness claims.

## Evidence Trace Block

Claim: D5 safe-payload rerun proved hosted `qwen3-32b` pass but returned
blocked for the two-model matrix because `qwen3-235b-a22b-thinking` did not
return `success=true`.

Evidence:

- safety preflight PASS for both model payloads (`blocked=false`);
- focused provider test PASS `42/42`;
- `cvf-web` check PASS;
- private provenance remote confirmed before push;
- private provenance push `6f0fbcd2` succeeded;
- hosted `qwen3-32b` returned HTTP `200`, `success=true`, `ALLOW`,
  `evidenceMode=live`, receipt `rcpt-env-mpidzqv4-ysriei`, trace
  `env-mpidzqv4-ysriei`, `rawSecretPrinted=false`;
- hosted `qwen3-235b-a22b-thinking` returned HTTP `200`, `success=false`,
  `ALLOW`, `evidenceMode=live`, receipt `rcpt-env-mpie0q8c-zn6jku`, trace
  `env-mpie0q8c-zn6jku`, error that the model does not exist or the account
  lacks access, `rawSecretPrinted=false`.

Independent checkability:

- Re-run the D5 work order only after fresh authorization.
- Inspect hosted account/model access for the exact model id before any next
  proof.

Falsification condition:

- A fresh authorized hosted call for the intended thinking model returns HTTP
  `200`, `success=true`, `ALLOW`, `evidenceMode=live`, matching model,
  receipt/trace present, and `rawSecretPrinted=false`.

## Claim Boundary

No claim is made that P3/D5 fully passes. No broad Qwen3 stability, production
readiness, hosted SaaS readiness, thinking-mode governance completeness,
all-provider parity, public-sync update, receipt-envelope change, route/auth
change, safety-filter change, vision/reasoning contract change, or freeze
release is claimed.

## Next Allowed Move

Stop under the D5 work order.

A fresh GC-018/work order is required before any further hosted attempt,
payload change, model-id correction, hosted account access change, deployment
step, or completion claim.
