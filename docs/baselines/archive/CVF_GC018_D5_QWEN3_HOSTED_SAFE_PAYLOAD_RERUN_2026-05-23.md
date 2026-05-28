# CVF GC-018 D5 Qwen3 Hosted Safe Payload Rerun

Memory class: SUMMARY_RECORD

Status: AUTHORIZED_READY_FOR_IMPLEMENTATION

Date: 2026-05-23

## Purpose

Authorize a narrow follow-up to the D4 hosted blocker. D4 implemented the
local Alibaba Qwen3 `enable_thinking: false` adapter fix, but the first hosted
proof request returned HTTP `400` with `Safety filter triggered` before a
successful model execution could be proven.

D5 is limited to a safety-filter-safe hosted proof rerun using a concrete
`strategy_analysis` payload, plus deployment confirmation for the already
committed D4 adapter work if the hosted target still needs the provenance
branch update.

## Scope

In scope:

- prepare one concrete `strategy_analysis` proof payload per Qwen3 model that
  avoids the known hosted safety-filter trigger tokens;
- locally preflight the payload text against the existing CVF safety-filter
  patterns before any hosted call;
- verify the already implemented D4 adapter assertions still pass;
- confirm the target deployment can receive the D4 adapter commit, including a
  private provenance `origin/main` push if required by the hosted deployment
  path;
- run at most one signed hosted proof call for `qwen3-32b`;
- only if the first call passes the matrix, run at most one signed hosted
  proof call for `qwen3-235b-a22b-thinking`;
- file a completion or blocker review with sanitized evidence.

Out of scope:

- changing `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/safety.ts`;
- changing `/api/execute` route logic, auth, receipt schema, or governance
  evidence fields;
- changing provider capability registry, `capability.json`, vision contract,
  or reasoning contract;
- changing the D4 adapter implementation unless local focused tests reveal a
  regression;
- public-sync work;
- claiming broad Qwen3 stability, hosted SaaS readiness, production readiness,
  thinking-mode governance completeness, or provider parity.

## Source / Predecessor Evidence

- D4 blocker:
  `docs/reviews/CVF_D4_QWEN3_ENABLE_THINKING_ADAPTER_BLOCKER_REVIEW_2026-05-23.md`
- D4 GC-018:
  `docs/baselines/CVF_GC018_D4_QWEN3_ENABLE_THINKING_ADAPTER_2026-05-23.md`
- D4 work order:
  `docs/work_orders/CVF_WO_D4_QWEN3_ENABLE_THINKING_ADAPTER_2026-05-23.md`
- P3 concrete-payload hosted proof pass:
  `docs/reviews/CVF_P3_HOSTED_PROTECTED_WORKFLOW_PROOF_RERUN_COMPLETION_2026-05-23.md`

## GC-018 Candidate Screening

| Candidate | Class | Score | Decision | Rationale |
| --- | ---: | ---: | --- | --- |
| Safety-filter-safe hosted rerun for D4 Qwen3 matrix | VALIDATION_TEST | 9/10 | CONTINUE | D4 failed before model dispatch because the submitted proof payload tripped safety filtering. A sanitized concrete strategy payload is the smallest valid next move. |
| Change safety filter to allow the D4 payload | POLICY_RUNTIME_CHANGE | 2/10 | REJECT | The filter is an active governance/safety boundary; no evidence supports weakening it. |
| Retry D4 payload unchanged | RETRY_LOOP | 0/10 | REJECT | D4 stop rule explicitly forbids retry loops after the first non-pass. |
| Broader Qwen3 provider soak | BROAD_TEST | 3/10 | DEFER | Two named proof calls must pass first; soak requires a separate tranche. |

## Depth Audit

Candidate: `D5_QWEN3_HOSTED_SAFE_PAYLOAD_RERUN`

- Risk reduction: 2 (distinguishes payload safety-filter block from adapter or provider failure)
- Decision value: 2 (can close or precisely reclassify the two-model hosted matrix)
- Machine enforceability: 2 (preflight, focused tests, and hosted matrix are deterministic pass/fail checks)
- Operational efficiency: 2 (no source-code change expected; bounded to two hosted calls)
- Portfolio priority: 1 (Qwen3 free-tier quota expires 2026-06-02)
- Total: 9
- Decision: CONTINUE

## Authorization Boundary

- Authorized now: YES
- Tranche name: `D5_QWEN3_HOSTED_SAFE_PAYLOAD_RERUN`
- Blocked-work override required: NO
- Expected enforcement class: HOSTED_PROOF_RERUN_WITH_SAFE_PAYLOAD
- Required evidence:
  - safety preflight PASS for the hosted payload text;
  - focused provider adapter tests still PASS;
  - deployment/remote posture recorded without raw token values;
  - hosted `qwen3-32b` matrix PASS before attempting the second model;
  - hosted `qwen3-235b-a22b-thinking` matrix PASS only if the first model passes;
  - sanitized completion or blocker review filed.

## Pass / Stop Matrix

Per hosted call:

| Criterion | Required value |
| --- | --- |
| HTTP status | 200 |
| `success` | true |
| `decision` or equivalent final decision | ALLOW |
| `routingDecision` or equivalent route decision | ALLOW |
| `enforcementStatus` | ALLOW |
| `evidenceMode` | live |
| `provider` | alibaba |
| `model` | requested model |
| Receipt id | present |
| Trace id | present |
| Raw secret printed | false |

Stop immediately and file a blocker review if the first hosted call returns
non-200, `success=false`, non-`ALLOW`, missing live evidence, or another
provider/runtime error. Do not attempt the second model after a first-call
failure.

## Decision / Baseline / Proposed Tranche

Decision: AUTHORIZED.

Baseline: D4 local adapter code exists and focused tests passed, but D4 could
not close because the hosted request body triggered safety filtering. D5
therefore changes only the proof payload and deployment confirmation posture.

Proposed tranche: `D5_QWEN3_HOSTED_SAFE_PAYLOAD_RERUN` — one safety-filter-safe
hosted proof sequence over the two named Qwen3 models.

## Evidence / Verification

Required before closure:

- payload safety preflight result;
- `npm run test:run -- src/lib/ai/providers.test.ts` result in `cvf-web`;
- `npm run check` result in `cvf-web`;
- remote/deployment action facts, if a provenance push is used;
- sanitized hosted proof facts for each attempted model;
- local governance hook chain PASS before commit.

## Claim Boundary

D5 can only close the bounded two-model hosted Qwen3 proof matrix if both
single-call hosted executions pass. It does not claim broad Qwen3 stability,
hosted SaaS readiness, production readiness, thinking-mode governance
completeness, public deployment readiness, persistence readiness, Maika proof,
public-sync update, or freeze release.

Free-tier quota note: evidence remains bounded to Alibaba free-tier quota
expiring 2026-06-02 and does not extend to paid-tier behavior, rate limits, or
production load.
