# CVF Work Order D6 — Qwen3 Thinking Model ID Correction

Memory class: SUMMARY_RECORD

Status: READY_FOR_IMPLEMENTATION

docType: work_order

Date: 2026-05-23

---

## Required First Reads

Before implementation, read in order:

1. `docs/baselines/CVF_GC018_D6_QWEN3_THINKING_MODEL_ID_CORRECTION_2026-05-23.md`
2. `docs/reviews/CVF_D5_QWEN3_HOSTED_SAFE_PAYLOAD_RERUN_BLOCKER_REVIEW_2026-05-23.md`
3. `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`
4. `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/alibaba/capability.json`
5. `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-capability-registry.test.ts`
6. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.test.ts`

---

## Purpose

Correct the Qwen3 235B thinking model id from
`qwen3-235b-a22b-thinking` to `qwen3-235b-a22b-thinking-2507`, then run one
hosted proof call for the corrected id.

---

## Authority Chain

- GC-018:
  `docs/baselines/CVF_GC018_D6_QWEN3_THINKING_MODEL_ID_CORRECTION_2026-05-23.md`
- D5 blocker:
  `docs/reviews/CVF_D5_QWEN3_HOSTED_SAFE_PAYLOAD_RERUN_BLOCKER_REVIEW_2026-05-23.md`
- Operator authorization: explicit — "xử lý đi"

---

## Agent Roles

- Implementer: Codex
- Reviewer: Codex
- Auditor: Codex

---

## Scope / Target / Owner Boundary

### Write ownership (in scope)

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/alibaba/capability.json`
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-capability-registry.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.test.ts`
- D6 completion or blocker review under `docs/reviews/`
- session memory and incremental test log

### Out of scope (forbidden)

- `/api/execute` route changes;
- safety/DLP/auth/service-token/receipt/governance-envelope changes;
- provider runtime behavior changes beyond correcting the model id metadata and
  tests;
- public-sync;
- broad Qwen3 soak or production-readiness claim;
- retrying the old model id.

---

## Implementation Steps

1. Replace `qwen3-235b-a22b-thinking` with
   `qwen3-235b-a22b-thinking-2507` in the Model Gateway registry and Alibaba
   capability metadata.
2. Update focused Model Gateway tests for the corrected id.
3. Update `cvf-web` provider tests so `enable_thinking=false` covers the
   corrected id.
4. Run focused tests and checks.
5. Push private provenance if hosted deployment freshness requires it.
6. Run exactly one signed hosted proof call for
   `qwen3-235b-a22b-thinking-2507`.
7. File completion or blocker review.

---

## Pre-flight Checks

- Confirm active state requires fresh authorization after D5.
- Confirm D6 GC-018 and work order are filed before source edits.
- Check `git remote -v` before any push.
- Do not print or commit raw API keys, service tokens, HMAC signatures, or
  signed headers.

---

## Execution Plan

1. File D6 GC-018/work order.
2. Apply model-id correction.
3. Run Model Gateway focused tests.
4. Run `cvf-web` focused provider tests and check.
5. Push private provenance only after remote confirmation.
6. Run one hosted proof call for corrected model id.
7. File review, update memory/logs, run hooks, commit, and push.

---

## Evidence Requirements

- Registry/capability/test diff for corrected model id.
- Model Gateway focused test result.
- `cvf-web` provider test result.
- `cvf-web` check result.
- Sanitized hosted proof result.
- Governance hook-chain result.

---

## Review Gate

Codex self-review must confirm:

- no route/auth/safety/receipt behavior changed;
- old model id is not retained in active registry/capability tests;
- hosted call uses only the corrected model id;
- if hosted call fails, no retry loop is run;
- review packet contains sanitized facts only.

---

## Acceptance Criteria

- [ ] D6 GC-018 and work order filed.
- [ ] Corrected model id present in Model Gateway registry and Alibaba
  capability metadata.
- [ ] Focused Model Gateway tests PASS.
- [ ] Focused `cvf-web` provider tests PASS.
- [ ] `cvf-web` check PASS.
- [ ] Hosted corrected model proof PASS, or blocker review filed on first
  non-pass.
- [ ] Session memory and test log updated.
- [ ] Hook chain PASS.
- [ ] Commit and private provenance push complete.

---

## Operator Checkpoint

Operator authorization is explicit in this session. Any access provisioning in
Alibaba Cloud, billing/quota change, public-sync update, or second hosted
attempt after a non-pass requires fresh authorization.

---

## Return-To-Orchestrator Conditions

Return after commit with one of:

- `CLOSED_D6_QWEN3_THINKING_MODEL_ID_CORRECTION_PASS`; or
- `RETURNED_BLOCKED_*` with the first failing criterion and no retry loop.

---

## Closure Checklist

- [ ] D6 model id correction implemented.
- [ ] Tests/checks complete.
- [ ] Hosted proof complete or stopped on first non-pass.
- [ ] Completion/blocker review filed.
- [ ] Session state updated.
- [ ] Commit and push complete.

---

## Claim Boundary

D6 only corrects and validates the Qwen3 235B thinking model id. It does not
claim broad Qwen3 stability, hosted readiness, production readiness,
provider parity, public deployment readiness, persistence, Maika proof, or
freeze release.
