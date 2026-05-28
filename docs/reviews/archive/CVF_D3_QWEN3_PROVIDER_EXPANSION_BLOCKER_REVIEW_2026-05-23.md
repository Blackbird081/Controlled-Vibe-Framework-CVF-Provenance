# CVF D3 Qwen3 Provider Expansion Blocker Review

Memory class: FULL_RECORD

Status: RETURNED_BLOCKED_PROVIDER_PARAMETER

docType: review

Reviewer: Codex

Date: 2026-05-23

---

## Purpose

Record the D3 Qwen3 provider expansion result.

The additive Model Gateway registry work and tests passed, but the first hosted
Qwen3 proof did not satisfy the required P3 pass/fail matrix. Per the work
order, Codex stopped and did not run the second hosted proof call.

---

## Scope / Target / Owner Boundary

Target:

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/alibaba/capability.json`
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-capability-registry.test.ts`
- hosted endpoint: `https://vibcode.netlify.app/api/execute`

Owner boundary:

- additive provider registry extension only;
- no `/api/execute` route change;
- no provider adapter behavior change;
- no receipt envelope change;
- no vision or reasoning contract change;
- no public-sync.

---

## Authority Chain

- GC-018:
  `docs/baselines/CVF_GC018_D3_QWEN3_PROVIDER_EXPANSION_2026-05-23.md`
- Work order:
  `docs/work_orders/CVF_WO_D3_QWEN3_PROVIDER_EXPANSION_2026-05-23.md`
- P3 hosted proof predecessor:
  `docs/reviews/CVF_P3_HOSTED_PROTECTED_WORKFLOW_PROOF_RERUN_COMPLETION_2026-05-23.md`

---

## Target / Source Under Review

Primary source changes under review:

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/alibaba/capability.json`
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-capability-registry.test.ts`

Evidence sources:

- `npm test` in `EXTENSIONS/CVF_MODEL_GATEWAY`;
- one signed hosted service-token POST to
  `https://vibcode.netlify.app/api/execute`.

---

## Scope / Methodology

1. Added `qwen3-32b` and `qwen3-235b-a22b-thinking` to the Alibaba entry in
   `PROVIDER_CAPABILITY_REGISTRY`.
2. Added matching entries to Alibaba `capability.json`.
3. Added provider capability registry assertions for both models.
4. Ran `npm test` in `EXTENSIONS/CVF_MODEL_GATEWAY`.
5. Ran one signed hosted service-token `/api/execute` call for `qwen3-32b`.
6. Stopped before the `qwen3-235b-a22b-thinking` call because the first call
   failed the acceptance matrix.

---

## Registry Change Summary

Additive-only registry changes:

- `qwen3-32b` under provider `alibaba`
  - supported methods: `complete`, `chat`
  - default method: `complete`
- `qwen3-235b-a22b-thinking` under provider `alibaba`
  - supported methods: `complete`, `chat`, `reasoning`
  - default method: `complete`

No existing provider/model entries were modified.

---

## Test Evidence

Command:

```powershell
npm test
```

Working directory:

```text
EXTENSIONS/CVF_MODEL_GATEWAY
```

Result:

- test files: `20 passed / 20`;
- tests: `81 passed / 81`;
- provider capability registry tests: `7 passed / 7`.

---

## Hosted Proof Evidence

Sanitized hosted response facts for the first and only attempted hosted model:

| Field | Value |
| --- | --- |
| Requested model | `qwen3-32b` |
| HTTP status | `200` |
| Duration | `6892ms` |
| `success` | `false` |
| Error | `parameter.enable_thinking must be set to false for non-streaming calls` |
| Decision | `ALLOW` |
| Routing decision | `ALLOW` |
| Enforcement status | `ALLOW` |
| Evidence mode | `live` |
| Provider | `alibaba` |
| Model | `qwen3-32b` |
| Receipt id | `rcpt-env-mpi67ivg-pdduob` |
| Trace id | `env-mpi67ivg-pdduob` |
| Policy snapshot id | `pol-20260523-0001` |
| Output length | `0` |
| Raw secret printed | `false` |

Assertions:

- HTTP `200`: pass;
- `success=true`: fail;
- `ALLOW` decision: pass;
- routing `ALLOW`: pass;
- live evidence: pass;
- receipt present: pass;
- trace present: pass;
- provider `alibaba`: pass;
- model matches requested: pass.

The `qwen3-235b-a22b-thinking` call was not attempted because the work order
requires stopping on a hosted proof failure instead of retrying or continuing.

---

## Findings / Position

Position: `RETURNED_BLOCKED_PROVIDER_PARAMETER`.

Findings:

- D3 registry and tests are ready.
- Hosted signed service-token auth reached governance.
- The governance runtime returned live evidence and `ALLOW`.
- Provider completion failed for `qwen3-32b` because the hosted non-streaming
  call path did not set `enable_thinking=false`.
- Fixing that parameter would require provider adapter or route behavior work,
  which is outside this D3 registry-only work order.

---

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Overclaiming D3 as fully closed | Keep D3 status blocked; do not claim Qwen3 hosted proof pass. |
| Treating governance `ALLOW` as full provider success | Record `success=false` and provider parameter failure separately from governance decision. |
| Retrying into free-tier quota or variance | Stop after first failing hosted proof; no retry loop and no second model call. |
| Fixing provider behavior under registry-only scope | Require a fresh GC-018/work order if `enable_thinking=false` should be added for non-streaming Qwen3 calls. |
| Secret leakage | Evidence records sanitized facts only and `rawSecretPrinted=false`. |

---

## Decision

D3 returns blocked after partial implementation.

Completed:

- additive Model Gateway registry entries;
- Alibaba `capability.json` entries;
- test assertions;
- Model Gateway `npm test` PASS.

Blocked:

- hosted Qwen3 proof did not pass for `qwen3-32b`;
- `qwen3-235b-a22b-thinking` proof was not attempted after first hosted proof
  failure.

---

## Evidence Trace Block

Claim: D3 registry expansion is implemented and tested, but hosted Qwen3 proof
does not pass because the first hosted provider call returned `success=false`.

Evidence:

- `npm test` in `EXTENSIONS/CVF_MODEL_GATEWAY`: `20/20` files and `81/81`
  tests passed;
- signed hosted service-token POST to
  `https://vibcode.netlify.app/api/execute`;
- requested model `qwen3-32b`;
- HTTP `200`;
- `success=false`;
- error `parameter.enable_thinking must be set to false for non-streaming calls`;
- `decision=ALLOW`;
- `routingDecision=ALLOW`;
- `enforcementStatus=ALLOW`;
- `evidenceMode=live`;
- receipt `rcpt-env-mpi67ivg-pdduob`;
- trace `env-mpi67ivg-pdduob`;
- `rawSecretPrinted=false`.

Verdict:

- D3 hosted proof is blocked at provider parameter compatibility.

---

## Claim Boundary

This review does not claim broad Qwen3 stability, Qwen3 production readiness,
hosted SaaS readiness, thinking-mode governance completeness, all-provider
parity, receipt-envelope readiness, provider-runtime readiness, public-sync, or
freeze release.
