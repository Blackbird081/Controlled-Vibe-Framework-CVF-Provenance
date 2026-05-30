# CVF Work Order: S1 — Durable Memory Write Path via /api/execute

Memory class: FULL_RECORD

Status: CLOSED_PASS

docType: work_order

Date: 2026-05-24

Tranche: S1

Roadmap: `docs/roadmaps/CVF_S1_S2_S3_NEXT_VALUE_ROADMAP_2026-05-24.md`

---

## Purpose

Add a policy-gated opt-in durable memory write step to the `/api/execute`
governed execution route. Write fires only after a successful governed
execution (decision ALLOW, `success=true`) and only when the request
explicitly opts in. `canReinject=false` is preserved. This completes the
read-write cycle begun in R2.

---

## Authority Chain

- GC-018: `docs/baselines/CVF_GC018_S1_DURABLE_MEMORY_WRITE_ROUTE_2026-05-24.md`
- Roadmap: `docs/roadmaps/CVF_S1_S2_S3_NEXT_VALUE_ROADMAP_2026-05-24.md`
- R2 completion: `docs/reviews/CVF_R2_EXECUTE_ROUTE_DURABLE_MEMORY_WIRING_COMPLETION_2026-05-24.md`
- M1 durable store: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts`

---

## Scope / Target / Owner Boundary

Target surfaces:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts` — add
  `durableMemoryWrite` optional field to `ExecutionRequest`.
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/durable-memory-route.ts`
  — add `evaluateDurableMemoryWrite()` function.
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
  — wire write step after successful execution.
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts`
  — add `durableMemoryWriteReceipt` to envelope type.

Out of scope:

- Autonomous memory write (no write without explicit request field).
- `canReinject=true`.
- Raw output written to store (summary-only, max-length enforced).
- Hosted/cloud persistence backend.
- Any kernel surface modification.
- Write triggered by BLOCK or failed execution.

---

## Agent Roles

| Role | Responsibility |
| --- | --- |
| Planner | Read R2 completion and M1 store before designing write path. |
| Implementer | Add types, write evaluator, route wiring, envelope field. |
| QA | Route tests (policy-gated allow, deny, skip on BLOCK, summary truncation); live proof. |
| Governance Reviewer | Confirm no autonomous write, no raw output in store, `canReinject=false` preserved. |
| Release Manager | Release gate PASS; completion review; commit. |

---

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/durable-memory-route.ts`
  (existing read evaluator pattern to mirror)
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts`
  (existing `ExecutionRequest` and `ExecutionResponse` types)
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
  (existing write wiring pattern around AIF C2 reinjection)
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts`
  (write input interface and receipt)
- `docs/reviews/CVF_R2_EXECUTE_ROUTE_DURABLE_MEMORY_WIRING_COMPLETION_2026-05-24.md`
- `docs/roadmaps/CVF_S1_S2_S3_NEXT_VALUE_ROADMAP_2026-05-24.md`

---

## Write Ownership

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/durable-memory-route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.durable-memory.test.ts`
  (add write test cases)
- `scripts/run_cvf_s1_durable_memory_write_route_live_probe.mjs`
- `docs/reviews/CVF_S1_DURABLE_MEMORY_WRITE_ROUTE_COMPLETION_2026-05-24.md`
- `docs/roadmaps/CVF_S1_S2_S3_NEXT_VALUE_ROADMAP_2026-05-24.md` — update S1
  row to `CLOSED_PASS`.

---

## Pre-Flight Checks

- Confirm R4-fix is applied (or apply it as part of this diff to avoid
  conflict on `durable-memory-route.ts`).
- Confirm `CVF_DURABLE_MEMORY_STORE_PATH` env var is available locally for
  live proof. Do not print value.
- Confirm live provider key is available (Alibaba preferred). Do not print.
- Check GC-023 line counts on all modified files before adding code.
- Confirm `canReinject=false` is still binding in `runtime-memory-hierarchy.ts`.

---

## Allowed / Forbidden Scope

Allowed:

- `durableMemoryWrite` optional field on `ExecutionRequest`:
  `{ enabled?: boolean; tier?: 'skill' | 'long-term'; scope?: string; policy?: { actorAuthorized?: boolean }; maxSummaryLength?: number }`
- `evaluateDurableMemoryWrite()` function in `durable-memory-route.ts`:
  validates policy gate, builds governed summary from output (truncated),
  calls `DurableMemoryStore.write()`, returns write receipt.
- `durableMemoryWriteReceipt` optional field on `governanceEvidenceReceipt`.
- Write wired in `route.ts` after ALLOW + success check.
- Route tests for write path.
- Live probe script for write proof.

Forbidden:

- Autonomous write (no write when `durableMemoryWrite` is absent or
  `enabled=false`).
- Write on BLOCK, CLARIFY, or `success=false`.
- Raw output written to store (only governed summary ≤`maxSummaryLength`
  chars, default 500).
- Setting `canReinject=true`.
- Any kernel surface modification.
- Hosted/cloud backend change.

---

## Execution Plan

1. Read all required first reads. Note R2 read evaluator pattern.
2. Apply R4-fix if not already applied (import `randomUUID`, fix
   `emptyReceipt()` receipt id).
3. Add `durableMemoryWrite` field to `ExecutionRequest` in `types.ts`.
4. Add `evaluateDurableMemoryWrite()` to `durable-memory-route.ts`:
   - Gate: `enabled` + `actorAuthorized` both required.
   - Summary: `output.slice(0, maxSummaryLength)` with a notice that content
     is truncated.
   - Call `store.write()` with `policyDecision: 'allow'`.
   - Return receipt.
5. Add `durableMemoryWriteReceipt` to `web-governance-envelope.ts`.
6. Wire in `route.ts`: after execution success + ALLOW, call
   `evaluateDurableMemoryWrite()` if requested; attach receipt to envelope.
7. Add test cases to `route.durable-memory.test.ts`:
   - Policy-gated write allowed after ALLOW + success.
   - Write denied when `actorAuthorized=false`.
   - Write skipped when execution decision is BLOCK.
   - Summary truncation enforced at `maxSummaryLength`.
8. Confirm `canReinject=false` binding test PASS.
9. Run `npm run check` in `cvf-web`. Must PASS.
10. Run targeted route tests. Must PASS.
11. Write live probe script `run_cvf_s1_durable_memory_write_route_live_probe.mjs`.
    Must produce both execution receipt and `durableMemoryWriteReceipt` with
    `decision=allowed`, `rawMemoryReleased=false`.
12. Run release gate. Must PASS 7/7.
13. File completion review.
14. Commit all artifacts.

---

## Evidence Requirements

- Route tests PASS (at minimum: write allowed, write denied, write skipped on
  BLOCK, summary truncation).
- `canReinject=false` test PASS.
- Live proof receipt: `evidenceMode=live`, `durableMemoryWriteReceipt.decision=allowed`,
  `rawMemoryReleased=false`, `rawSecretPrinted=false`.
- TypeScript check PASS.
- Release gate PASS 7/7.
- Completion review filed.

---

## Acceptance Criteria

- [ ] R4-fix applied (or part of this diff).
- [ ] `durableMemoryWrite` typed in `ExecutionRequest`.
- [ ] `evaluateDurableMemoryWrite()` implemented with policy double-gate.
- [ ] Write skipped on BLOCK or `success=false`.
- [ ] Summary truncation enforced.
- [ ] `durableMemoryWriteReceipt` in governance envelope.
- [ ] Route tests PASS (4 cases minimum).
- [ ] `canReinject=false` binding test PASS.
- [ ] Live proof: execution receipt + write receipt, `rawMemoryReleased=false`.
- [ ] TypeScript check PASS.
- [ ] Release gate PASS.
- [ ] Completion review filed.

---

## Review Gate

The completion review must confirm:

- No autonomous write path exists (write requires explicit request field).
- Write never fires on BLOCK or failed execution.
- Store content is summary-only with max-length enforcement.
- `canReinject=false` test result cited.
- Live proof receipt present and `rawMemoryReleased=false`.
- Release gate 7/7 PASS cited.

---

## Operator Checkpoint

Operator authorized S1 on 2026-05-24. R4-fix must be applied before or within
this diff to avoid file conflict.

Codex must self-execute and return the final result after tranche completion.

---

## Closure Checklist

- [ ] R4-fix confirmed applied.
- [ ] Types added.
- [ ] Write evaluator implemented.
- [ ] Route wired.
- [ ] Tests PASS.
- [ ] Live proof receipt filed.
- [ ] TypeScript check PASS.
- [ ] Release gate PASS.
- [ ] Completion review filed and committed.

---

## Return-To-Orchestrator Conditions

Return blocked if: `canReinject=false` test fails, write fires without explicit
opt-in, raw output reaches durable store, TypeScript check fails, live proof
fails, or release gate fails.

---

## Tasks

| Task | Status | Output |
| --- | --- | --- |
| R4-fix (if not applied) | DONE | `randomUUID()` in `emptyReceipt()`. |
| `durableMemoryWrite` type | DONE | In `types.ts`. |
| `evaluateDurableMemoryWrite()` | DONE | In `durable-memory-route.ts`. |
| Governance envelope field | DONE | `durableMemoryWriteReceipt` in envelope. |
| Route wiring | DONE | In `route.ts`. |
| Route tests (4 cases) | DONE | PASS. |
| `canReinject=false` test | DONE | PASS. |
| Live probe script | DONE | Write receipt, `rawMemoryReleased=false`. |
| TypeScript check | DONE | PASS. |
| Release gate | DONE | 7/7 PASS. |
| Completion review | DONE | Filed. |

---

## Claim Boundary

S1 claims one bounded route-level opt-in durable write path for skill/long-term
tiers after successful governed execution. It does not claim autonomous memory
write, `canReinject=true`, raw-memory release, hosted/cloud persistence,
enterprise SaaS readiness, or broad production readiness.
