# CVF S1/S2/S3 Next-Value Roadmap

Memory class: SUMMARY_RECORD

Status: ACTIVE

docType: roadmap

Date: 2026-05-24

---

## Scope / Target / Owner Boundary

Scope: four bounded tranches covering route quality hardening, memory write
path through `/api/execute`, provider soak hardening, and governance benchmark
public claim.

Target: cvf-web governed execution route, LPF durable memory store, provider
stability probe scripts, and the public technical catalog.

Owner: Codex (implementation); Claude (dispatch and quality assessment).

Out of scope: autonomous memory reinjection, `canReinject=true`, raw-memory
prompt injection, hosted/cloud persistence, provider procurement, enterprise
SaaS/GA readiness, broad production readiness, global freeze lift.

---

## Authorization / Decision

Operator authorized on 2026-05-24:

- R4-fix (receipt-id determinism in durable-memory-route.ts): authorized as
  Fast Lane corrective — localized to one helper function, no behavior change.
- S1 (durable memory write path via `/api/execute`): authorized. Requires
  fresh GC-018 because it adds a new route-level write behavior.
- S2 (provider coverage hardening — extended soak): authorized. Requires fresh
  GC-018 because it extends the bounded provider stability claim.
- S3 (governance benchmark public claim): authorized. Requires fresh GC-018
  because it produces a new public catalog row backed by live benchmark
  evidence.

Authority chain baselines:

- R4-fix: Fast Lane audit (no GC-018 required — localized corrective).
- S1: `docs/baselines/CVF_GC018_S1_DURABLE_MEMORY_WRITE_ROUTE_2026-05-24.md`
- S2: `docs/baselines/CVF_GC018_S2_PROVIDER_SOAK_HARDENING_2026-05-24.md`
- S3: `docs/baselines/CVF_GC018_S3_GOVERNANCE_BENCHMARK_PUBLIC_CLAIM_2026-05-24.md`

---

## Purpose

Close four gaps identified in the post-R1/R2/R3 quality audit:

1. R4-fix: `emptyReceipt()` in `durable-memory-route.ts` uses
   `Date.now() + Math.random()` for `receiptId` instead of the `randomUUID()`
   pattern adopted in R1. Makes receipt ids consistent and assertable in tests.

2. S1: `/api/execute` currently only *reads* durable memory. A non-coder
   running through the web UI cannot accumulate cross-session skill memory
   without an explicit write path. S1 adds a policy-gated durable memory
   write step that fires after a successful governed execution.

3. S2: C4 proved 2 journeys × 3 providers (6/6). The current claim is narrow.
   S2 extends to a longer soak window per provider to support a stronger — but
   still bounded — repeatability claim.

4. S3: `operational-benchmark-suite.ts` (E2 deliverable) has 9 metrics defined
   but no live public evidence. S3 runs the benchmark against the live hosted
   target, records evidence, and adds a public catalog row.

---

## Scope

| Tranche | Title | Depends On | Status | Work Order |
| --- | --- | --- | --- | --- |
| R4-fix | Route receipt-id determinism | R2 CLOSED_PASS | WORK_ORDER_READY | `docs/work_orders/CVF_WO_R4FIX_ROUTE_RECEIPT_ID_DETERMINISM_2026-05-24.md` |
| S1 | Durable memory write path via `/api/execute` | R2 CLOSED_PASS | WORK_ORDER_READY | `docs/work_orders/CVF_WO_S1_DURABLE_MEMORY_WRITE_ROUTE_2026-05-24.md` |
| S2 | Provider soak hardening | C4 CLOSED_PASS | WORK_ORDER_READY | `docs/work_orders/CVF_WO_S2_PROVIDER_SOAK_HARDENING_2026-05-24.md` |
| S3 | Governance benchmark public claim | E2 CLOSED_PASS | WORK_ORDER_READY | `docs/work_orders/CVF_WO_S3_GOVERNANCE_BENCHMARK_PUBLIC_CLAIM_2026-05-24.md` |

All four tranches may begin immediately in parallel. R4-fix and S1 touch
overlapping files (`durable-memory-route.ts`) — Codex must apply R4-fix first
or apply the fix as part of the S1 diff to avoid conflict.

---

## Non-Goals

- Autonomous memory reinjection.
- `canReinject=true`.
- Raw-memory prompt injection.
- Hosted/cloud persistence.
- Provider account procurement.
- Enterprise SaaS or hosted GA readiness.
- Broad production availability claims.
- Global freeze lift.
- New memory tiers.
- New governance kernel surface modifications beyond what M2 already authorized.

---

## Work Plan

R4-fix:

- Replace `Date.now().toString(36) + Math.random()` in `emptyReceipt()` inside
  `durable-memory-route.ts` with `randomUUID()` from `node:crypto`.
- Update any route test assertions that were skipping receiptId to now assert
  the UUID pattern (`/^[0-9a-f-]{36}$/`).
- TypeScript check PASS.
- Fast Lane audit filed.

S1:

- Add a `durableMemoryWrite` optional field to `ExecutionRequest` type.
- After a successful governed execution (decision ALLOW, success true), evaluate
  a policy-gated durable write using the existing `DurableMemoryStore.write()`
  interface.
- Write only if `durableMemoryWrite.enabled=true` and
  `durableMemoryWrite.policy.actorAuthorized=true`.
- Write content is the execution summary (output truncated to a governed
  max length), not the raw full output.
- Emit `durableMemoryWriteReceipt` in `governanceEvidenceReceipt`.
- `canReinject=false` preserved. No autonomous write without explicit request
  field.
- Route tests: policy-gated write allowed, unauthorized write denied, write
  after BLOCK decision skipped.
- Live proof: one governed execution that produces both an execution receipt
  and a durable write receipt.
- Release gate PASS.

S2:

- Extend `run_post_phase2b_provider_stability_probe.mjs` or create a new soak
  script with at least 5 journeys per provider (Alibaba, DeepSeek, OpenAI).
- Inter-journey cooldown preserved.
- Failure classification and partial-pass detection.
- Claim: bounded N-journey-per-provider soak window (exact N per evidence).
- Do not claim universal stability.
- Live receipts required for every journey.
- No raw key printed.

S3:

- Read `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src` `operational-benchmark-suite.ts`
  and `governance-reliability-metrics.ts` (E2 deliverables) fully before
  designing the probe.
- Run the benchmark suite against the live hosted `/api/execute` target.
- Record evidence: at least 3 of the 9 metrics with live values
  (taskCompletionRate, policyViolationRate, receiptIntegrityRate are the
  minimum; others are bonus if available).
- Add a public catalog row: `governance benchmark` capability with bounded
  evidence path.
- Evidence path must be public-safe (no private review content, no raw key).
- Public catalog Test-Path PASS from public-sync clone.

---

## Acceptance Criteria

- [ ] R4-fix: `receiptId` in `emptyReceipt()` uses `randomUUID()`. Route tests
      assert UUID pattern. TypeScript PASS. Fast Lane audit filed.
- [ ] S1: durable write path wired. Policy double-gate (`enabled` +
      `actorAuthorized`) enforced. Write skipped on BLOCK. `canReinject=false`
      preserved. Live proof produces write receipt. Release gate PASS.
- [ ] S2: soak probe run with ≥5 journeys per provider. Live receipts filed for
      all journeys. Claim bounded to proven soak window only.
- [ ] S3: benchmark probe run against live hosted target. ≥3 metrics with live
      values. Public catalog row added. Test-Path PASS from public-sync.
- [ ] No raw secret in any committed artifact across all tranches.
- [ ] R4-fix applied before or within S1 to avoid file conflict.

---

## Verification / Evidence

R4-fix:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/durable-memory-route.ts`
  — `receiptId` uses `randomUUID()`.
- Fast Lane audit: `docs/reviews/CVF_R4FIX_ROUTE_RECEIPT_ID_FAST_LANE_AUDIT_2026-05-24.md`

S1:

- `docs/baselines/CVF_GC018_S1_DURABLE_MEMORY_WRITE_ROUTE_2026-05-24.md`
- `docs/reviews/CVF_S1_DURABLE_MEMORY_WRITE_ROUTE_COMPLETION_2026-05-24.md`
- Live write receipt with `evidenceMode=live`, `rawMemoryReleased=false`.
- Release gate PASS.

S2:

- `docs/baselines/CVF_GC018_S2_PROVIDER_SOAK_HARDENING_2026-05-24.md`
- `docs/reviews/CVF_S2_PROVIDER_SOAK_HARDENING_COMPLETION_2026-05-24.md`
- Live receipts for all soak journeys.

S3:

- `docs/baselines/CVF_GC018_S3_GOVERNANCE_BENCHMARK_PUBLIC_CLAIM_2026-05-24.md`
- `docs/reviews/CVF_S3_GOVERNANCE_BENCHMARK_PUBLIC_CLAIM_COMPLETION_2026-05-24.md`
- Public catalog row with Test-Path PASS from public-sync clone.

---

## Claim Boundary

After all four tranches CLOSED_PASS:

- Route `emptyReceipt()` ids are deterministic UUID format.
- `/api/execute` can perform a policy-gated summary-only durable write after a
  successful governed execution.
- Bounded N-journey-per-provider soak window proven for Alibaba, DeepSeek,
  and OpenAI.
- Governance benchmark capability row in public catalog with live metric
  evidence.

Still not claimed:

- Autonomous memory reinjection.
- `canReinject=true`.
- Raw-memory prompt injection.
- Universal provider stability.
- Full hosted SaaS/GA production readiness.
- Enterprise production readiness.
- Hosted/cloud persistence.
- Provider account procurement.
- Global freeze lift.

---

## Progress Tracker

| Tranche | Status | Completion Review |
| --- | --- | --- |
| R4-fix | WORK_ORDER_READY | — |
| S1 | WORK_ORDER_READY | — |
| S2 | WORK_ORDER_READY | — |
| S3 | WORK_ORDER_READY | — |
