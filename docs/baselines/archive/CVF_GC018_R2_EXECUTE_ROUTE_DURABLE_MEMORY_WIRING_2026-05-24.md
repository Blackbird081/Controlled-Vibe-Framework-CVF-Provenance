# CVF GC-018 - R2: Execute Route Durable Memory Wiring

Memory class: SUMMARY_RECORD

Status: AUTHORIZED

docType: baseline

Date: 2026-05-24

---

## Scope

Authorize one bounded route-level wiring tranche for `/api/execute` to read
M1 durable `skill` / `long-term` memory summaries from a file-backed store
under explicit request policy and receipt evidence.

---

## Purpose

M1 delivered a durable memory store but did not connect it to the governed web
execution route. R2 closes that gap without changing the memory hierarchy:
durable records may provide summary-only context to `/api/execute` when a
request explicitly asks for it, the actor is authorized, and the route emits
durable-memory read evidence.

---

## Source / Predecessor Evidence

- M1 completion:
  `docs/reviews/CVF_M1_DURABLE_CROSS_SESSION_MEMORY_COMPLETION_2026-05-24.md`
- R1 completion:
  `docs/reviews/CVF_R1_DURABLE_MEMORY_STORE_RESILIENCE_COMPLETION_2026-05-24.md`
- R2 work order:
  `docs/work_orders/CVF_WO_R2_EXECUTE_ROUTE_DURABLE_MEMORY_WIRING_2026-05-24.md`
- Mandatory live governance proof rule in root `AGENTS.md`.

---

## Decision / Baseline / Proposed Tranche

Decision: authorize R2 with a narrow request opt-in field and file-backed
store path. The route may read durable memory summaries and attach receipt
evidence, but must not auto-write durable memories or treat memory as approval
authority.

Baseline: before R2, `/api/execute` has knowledge retrieval and C2 explicit
AIF memory reinjection, but no route-local durable store read path.

---

## Guardrails

- Request opt-in is required.
- Only `skill` and `long-term` tiers are eligible.
- Durable records are summary-only.
- `canReinject=false` remains binding in the durable store receipt.
- No raw memory payload may be accepted or released to provider prompts.
- Corrupt or missing durable store must degrade safely.
- No autonomous durable writes.
- No hosted/cloud persistence claim.
- Live proof must use a real provider call and must not print raw secrets.

---

## Pass Conditions

- `/api/execute` can read an authorized durable memory summary from the M1
  file-backed store.
- `governanceEvidenceReceipt` carries durable-memory read evidence.
- Route response exposes a safe durable-memory read receipt.
- Unit tests prove allowed, malformed/corrupt, and denied policy paths.
- One live `/api/execute` proof passes with a real provider key.
- TypeScript check passes.
- Release gate passes.
- Completion review filed.

---

## Evidence / Verification

Required evidence:

- Route unit tests.
- Live route durable-memory proof.
- TypeScript check.
- Release gate.
- Completion review:
  `docs/reviews/CVF_R2_EXECUTE_ROUTE_DURABLE_MEMORY_WIRING_COMPLETION_2026-05-24.md`

---

## Claim Boundary

R2 may claim bounded `/api/execute` durable-memory read wiring with
summary-only receipt evidence. It does not claim autonomous memory
reinjection, durable writes through the route, hosted/cloud persistence, broad
memory authority, or production-grade memory availability.

