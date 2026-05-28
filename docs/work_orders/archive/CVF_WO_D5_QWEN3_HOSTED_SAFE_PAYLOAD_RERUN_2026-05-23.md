# CVF Work Order D5 — Qwen3 Hosted Safe Payload Rerun

Memory class: SUMMARY_RECORD

Status: READY_FOR_IMPLEMENTATION

docType: work_order

Date: 2026-05-23

---

## Required First Reads

Before execution, read in order:

1. `docs/baselines/CVF_GC018_D5_QWEN3_HOSTED_SAFE_PAYLOAD_RERUN_2026-05-23.md`
2. `docs/reviews/CVF_D4_QWEN3_ENABLE_THINKING_ADAPTER_BLOCKER_REVIEW_2026-05-23.md`
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/safety.ts`
4. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.ts`
5. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.test.ts`

---

## Purpose

Close or precisely reclassify the D4 Qwen3 hosted proof blocker by using a
concrete `strategy_analysis` payload that preflights clean against the existing
CVF safety filter.

The D4 adapter implementation remains the target behavior: non-streaming
Alibaba Qwen3 calls must include `enable_thinking: false`. D5 does not weaken
or bypass the safety filter.

---

## Authority Chain

- GC-018:
  `docs/baselines/CVF_GC018_D5_QWEN3_HOSTED_SAFE_PAYLOAD_RERUN_2026-05-23.md`
- D4 blocker:
  `docs/reviews/CVF_D4_QWEN3_ENABLE_THINKING_ADAPTER_BLOCKER_REVIEW_2026-05-23.md`
- D4 implementation GC-018:
  `docs/baselines/CVF_GC018_D4_QWEN3_ENABLE_THINKING_ADAPTER_2026-05-23.md`
- Operator authorization: explicit — "xử lý đi"

---

## Agent Roles

- Implementer: Codex
- Reviewer: Codex
- Auditor: Codex
- Quality assessor: external reviewer after closure, if requested

---

## Scope / Target / Owner Boundary

### Write ownership (in scope)

- `docs/reviews/CVF_D5_QWEN3_HOSTED_SAFE_PAYLOAD_RERUN_COMPLETION_2026-05-23.md`
  or
  `docs/reviews/CVF_D5_QWEN3_HOSTED_SAFE_PAYLOAD_RERUN_BLOCKER_REVIEW_2026-05-23.md`
- `docs/CVF_INCREMENTAL_TEST_LOG.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V11_2026-05-21.md`

### Read/verify ownership (in scope)

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/safety.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.test.ts`

### Out of scope (forbidden)

- changing `safety.ts` or bypassing hosted safety filtering;
- changing `/api/execute` route logic, auth, service-token signing, receipt
  schema, or governance evidence shape;
- changing provider registry or capability metadata;
- changing `vision-contract.ts` or `reasoning-contract.ts`;
- adding Qwen3 stream/json-mode/reasoning adapters;
- public-sync work;
- broad Qwen3/provider stability, hosted SaaS readiness, production readiness,
  Maika proof, persistence, or freeze-release claims.

---

## Execution Steps

### Step 1 — Safety payload preflight

Create a concrete `strategy_analysis` payload per model. The payload must avoid
the known CVF safety-filter triggers, including:

- literal `secret`;
- literal `api key` or `api-key`;
- code fences;
- `<script>`;
- `ignore previous instructions`;
- SSN/card/passport/CMND/can-cuoc-like strings.

Run a local preflight against the current safety filter before hosted proof.
If preflight fails, stop and file a D5 blocker; do not hosted-call with a
payload known to fail locally.

### Step 2 — Local adapter verification

Run in `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`:

```powershell
npm run test:run -- src/lib/ai/providers.test.ts
npm run check
```

Expected:

- focused provider tests PASS;
- TypeScript/check PASS.

### Step 3 — Deployment / remote posture

If the hosted target is expected to deploy from provenance `origin/main`, run
`git remote -v` first and confirm the remote is
`Controlled-Vibe-Framework-CVF-Provenance`. A provenance push is allowed only
for this private deployment path. Do not push from this workspace to the
public repository.

Record only sanitized push/deployment facts.

### Step 4 — Hosted proof calls

Target:

`https://vibcode.netlify.app/api/execute`

Run one signed service-token call for `qwen3-32b`.

Only if it passes the full matrix, run one signed service-token call for
`qwen3-235b-a22b-thinking`.

Pass matrix:

| Criterion | Required value |
| --- | --- |
| HTTP status | 200 |
| `success` | true |
| `decision` or final decision | ALLOW |
| `routingDecision` or route decision | ALLOW |
| `enforcementStatus` | ALLOW |
| `evidenceMode` | live |
| `provider` | alibaba |
| `model` | requested model |
| Receipt id | present |
| Trace id | present |
| Raw secret printed | false |

If the first hosted call returns non-200 or non-ALLOW, stop and file a blocker
review. Do not retry and do not call the second model.

### Step 5 — Completion or blocker review

File exactly one of:

- completion review if both hosted calls pass;
- blocker review if local preflight, local verification, deployment posture, or
  first/second hosted proof fails.

Review must include sanitized evidence only. Do not include raw service token,
raw API key, HMAC signature, or signed headers.

---

## Pre-flight Checks

- Confirm active state points to D5 before hosted proof.
- Confirm `git remote -v` shows the private provenance remote before any push.
- Confirm the payload preflight passes locally.
- Confirm no raw token value is printed or written.

---

## Execution Plan

1. File D5 GC-018 and this work order.
2. Run local payload preflight.
3. Run focused provider adapter tests and `cvf-web` check.
4. Push private provenance only if needed for hosted deployment freshness.
5. Run hosted `qwen3-32b` proof once.
6. Run hosted `qwen3-235b-a22b-thinking` proof once only if the first call
   passes.
7. File completion or blocker review.
8. Update session memory and test log.
9. Run governance hooks and commit.

---

## Evidence Requirements

- Safety preflight output.
- Focused provider adapter test output.
- `cvf-web` check output.
- Sanitized remote/deployment facts if a push is used.
- Sanitized hosted proof matrix facts.
- Governance hook-chain result.

---

## Review Gate

Codex reviews before closure:

- no safety-filter weakening or bypass was introduced;
- no route/auth/receipt/provider registry/capability metadata was changed;
- hosted payload contains no known safety-filter trigger token;
- second model was attempted only after first model pass;
- review packet contains sanitized facts only.

---

## Acceptance Criteria

- [ ] Fresh D5 GC-018 and work order filed.
- [ ] Payload preflight PASS recorded.
- [ ] Focused D4 provider adapter tests PASS.
- [ ] `cvf-web` check PASS.
- [ ] Hosted `qwen3-32b` call PASSes the matrix.
- [ ] Hosted `qwen3-235b-a22b-thinking` call PASSes the matrix, only after
  first call PASS.
- [ ] Completion or blocker review filed with sanitized facts.
- [ ] Session memory and incremental test log updated.
- [ ] Local governance hook chain PASS.
- [ ] Commit made.

---

## Operator Checkpoint

Operator authorization is explicit in this session: "xử lý đi". No extra
approval is required for the bounded D5 work order. A separate approval is
required for any source-code change outside the D5 scope.

---

## Return-To-Orchestrator Conditions

Return after commit with one of:

- `CLOSED_D5_QWEN3_HOSTED_SAFE_PAYLOAD_RERUN_PASS`; or
- `RETURNED_BLOCKED_*` with the first failing criterion and no retry loop.

---

## Closure Checklist

- [ ] D5 GC-018 filed.
- [ ] D5 work order filed.
- [ ] Payload preflight passed.
- [ ] Local focused tests passed.
- [ ] Hosted proof matrix completed or stopped on first non-pass.
- [ ] Completion or blocker review filed.
- [ ] Session memory updated.
- [ ] Hook chain passed.
- [ ] Commit made.

---

## Claim Boundary

This D5 work order can prove only the bounded two-model hosted Qwen3 matrix
for one clean concrete strategy-analysis payload per model. It does not prove
broad Qwen3 stability, general provider parity, hosted SaaS readiness,
production readiness, public deployment readiness, persistence, Maika, or any
freeze release.
