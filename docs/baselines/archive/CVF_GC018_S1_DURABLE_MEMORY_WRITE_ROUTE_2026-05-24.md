# CVF GC-018 - S1: Durable Memory Write Path via /api/execute

Memory class: SUMMARY_RECORD

Status: OPEN

docType: baseline

Date: 2026-05-24

---

## Scope

Authorize one bounded S1 tranche adding a policy-gated durable memory write
step to the `/api/execute` governed execution route.

This extends R2 (read path) with a write path. Write fires only after a
successful governed execution (decision ALLOW, success true) and only when the
request explicitly opts in with `durableMemoryWrite.enabled=true` and
`durableMemoryWrite.policy.actorAuthorized=true`.

---

## Purpose

R2 wired the durable memory read path. Without a write path, each execution
starts with no accumulated memory even when the user opts in. S1 closes that
gap so non-coder and small-team operators can accumulate governed skill memory
across sessions through the same explicit policy gate.

---

## Source / Predecessor Evidence

- R2 completion: `docs/reviews/CVF_R2_EXECUTE_ROUTE_DURABLE_MEMORY_WIRING_COMPLETION_2026-05-24.md`
- M1 durable store: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts`
- Route durable memory helper: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/durable-memory-route.ts`
- AIF C2 summary-only gate: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/aif-memory-reinjection.ts`
- Roadmap: `docs/roadmaps/CVF_S1_S2_S3_NEXT_VALUE_ROADMAP_2026-05-24.md`

---

## Decision / Baseline / Proposed Tranche

Decision: execute one bounded S1 tranche adding an opt-in policy-gated durable
write step to the governed execution route.

Baseline: `/api/execute` currently reads durable memory (R2) but does not
write. Cross-session skill accumulation requires an explicit write path under
the same double-gate pattern.

Proposed tranche:

- Add `durableMemoryWrite` optional request field to `ExecutionRequest`.
- After ALLOW + success, evaluate policy gate and write a governed summary to
  the durable store.
- Emit `durableMemoryWriteReceipt` in `governanceEvidenceReceipt`.
- No autonomous write. `canReinject=false` preserved.

---

## Guardrails

- Write fires only when `durableMemoryWrite.enabled=true` AND
  `durableMemoryWrite.policy.actorAuthorized=true`. Both required.
- Write is skipped if the execution decision is not ALLOW or `success=false`.
- Write content is a governed summary of the output — truncated to a
  configurable max length (default ≤500 chars). Full raw output must not be
  written to the durable store.
- `canReinject=false` must remain binding in both the store receipt and the
  route receipt. No reinjection path is opened by S1.
- No raw API key, secret, or signed header in any artifact.
- `rawMemoryReleased: false` must be present in the write receipt.
- GC-023 pre-flight check required on all modified files before adding code.

---

## Pass Conditions

- `durableMemoryWrite` optional request field typed and validated.
- Policy double-gate enforced: write denied if not enabled or not authorized.
- Write skipped on BLOCK or failed execution.
- Write content is summary-only, max-length enforced.
- `durableMemoryWriteReceipt` emitted in `governanceEvidenceReceipt`.
- Route tests: policy-gated write allowed, unauthorized denied, write after
  BLOCK skipped, summary truncation enforced.
- `canReinject=false` binding test PASS.
- Live proof: one governed execution producing both an execution receipt and a
  durable write receipt, `evidenceMode=live`, `rawMemoryReleased=false`.
- TypeScript check PASS (cvf-web + LPF).
- Release gate PASS.
- Completion review filed.

---

## Evidence / Verification

Required evidence:

- Route tests PASS.
- `canReinject=false` test PASS.
- Live proof receipt: `evidenceMode=live`, `rawMemoryReleased=false`,
  `durableMemoryWriteReceipt.decision=allowed`.
- TypeScript check PASS.
- Release gate PASS.
- Completion review: `docs/reviews/CVF_S1_DURABLE_MEMORY_WRITE_ROUTE_COMPLETION_2026-05-24.md`

---

## Claim Boundary

S1 claims one bounded route-level opt-in durable write path for skill/long-term
tiers after successful governed execution. It does not claim autonomous memory
write, `canReinject=true`, raw-memory release, hosted/cloud persistence, or
enterprise SaaS readiness.

---

## Disposition

Open. Closed by work order completion review.
