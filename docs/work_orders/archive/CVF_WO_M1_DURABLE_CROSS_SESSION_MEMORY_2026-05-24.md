# CVF Work Order: M1 — Durable Cross-Session Memory

Memory class: FULL_RECORD

Status: CLOSED_PASS

docType: work_order

Date: 2026-05-24

Tranche: M1

Roadmap: `docs/roadmaps/CVF_M1_M2_P1_NEXT_VALUE_ROADMAP_2026-05-24.md`

---

## STOP — Demand Gate

This work order was `DEMAND_GATED`. Do not begin implementation until M2
(`docs/work_orders/CVF_WO_M2_D06_MEMORY_TIER_FREEZE_RELEASE_2026-05-24.md`)
has status `CLOSED_PASS`.

Verify M2 status before proceeding. If M2 is not `CLOSED_PASS`, stop here and
return to operator.

M2 status verified on 2026-05-24:

- `docs/reviews/CVF_M2_D06_MEMORY_TIER_FREEZE_RELEASE_COMPLETION_2026-05-24.md`
  is `CLOSED_PASS`.
- Owner map records `freeze_released: true` for the memory tier classifier
  surface.

---

## Purpose

Wire durable storage for skill-tier and long-term-tier memory using the
`memory-tier-classifier.contract.ts` (unfrozen by M2) as the policy gate.
Enable cross-session memory reads and writes with receipt evidence, preserving
the `canReinject=false` invariant and routing all reinjection through the AIF
C2 summary-only gate.

---

## Authority Chain

- GC-018: `docs/baselines/CVF_GC018_M1_DURABLE_CROSS_SESSION_MEMORY_2026-05-24.md`
- M2 GC-018: `docs/baselines/CVF_GC018_M2_D06_MEMORY_TIER_FREEZE_RELEASE_2026-05-24.md`
- Roadmap: `docs/roadmaps/CVF_M1_M2_P1_NEXT_VALUE_ROADMAP_2026-05-24.md`
- Freeze-release rule: `governance/toolkit/05_OPERATION/CVF_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE.md`

---

## Scope / Target / Owner Boundary

Target surfaces:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-tier-classifier.contract.ts` (read-only — unfrozen by M2, not modified here)
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-lifecycle-policy.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts`
- New: durable store implementation file(s) (Codex to name per convention)

Out of scope:

- Hosted/cloud persistence.
- Autonomous memory write.
- Modifying `canReinject` to `true` in `runtime-memory-hierarchy.ts`.
- Broad memory authority claim.
- Working, task, audit, and receipt tier persistence (no change).

---

## Agent Roles

| Role | Responsibility |
| --- | --- |
| Planner | Read legacy spec absorption registry and relevant legacy specs; confirm no design conflict. |
| Implementer | Build durable store interface; wire tier classifier as policy gate; add receipt evidence. |
| QA | Run LPF + cvf-web targeted tests; confirm `canReinject=false` binding test still PASS. |
| Governance Reviewer | Confirm no reinjection bypass, no raw memory in prompt, no unauthorized tier persistence. |
| Release Manager | File completion review; run release gate; commit. |

---

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `docs/reference/archive/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md`
- `.private_reference/legacy/CVF 16.5/agentmemory/` — ALL files (required by legacy spec scan block in GC-018)
- `docs/reviews/archive/CVF_LEGACY_SPEC_ABSORPTION_BLINDSPOT_CODEX_REVIEW_2026-05-23.md`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-tier-classifier.contract.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-lifecycle-policy.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/aif-memory-reinjection.ts`
- M2 completion review (read before design to confirm what was actually unfrozen)

---

## Write Ownership

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/` — durable store implementation
  file(s).
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` —
  if wiring changes are needed.
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` —
  if read path changes are needed.
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/` — unit tests for new paths.
- `docs/reviews/CVF_M1_DURABLE_CROSS_SESSION_MEMORY_COMPLETION_2026-05-24.md`
- `docs/roadmaps/CVF_M1_M2_P1_NEXT_VALUE_ROADMAP_2026-05-24.md` — update M1
  row status to `CLOSED_PASS`.

---

## Pre-Flight Checks

- Confirm M2 work order status is `CLOSED_PASS`.
- Confirm owner map shows `freeze_released: true` for `memory-tier-classifier.contract.ts`.
- Confirm `canReinject=false` is still present in `runtime-memory-hierarchy.ts` for all tiers.
- Confirm live provider keys are loaded from approved local env files without printing values.
- Check GC-023 line counts on all target files before adding code.

---

## Allowed / Forbidden Scope

Allowed:

- Durable store interface for skill-tier and long-term-tier.
- Cross-session write path with privacy filter (containsSecret, lifecycle,
  provenance score).
- Cross-session read path with receipt (memory ids, scope, policy decision).
- Summary-only reinjection via existing `evaluateAifMemoryReinjection()` gate.
- File-system or SQLite backend for durable store.
- Unit tests for write/read/receipt paths.
- Live proof: one governed cross-session retrieve with live receipt.

Forbidden:

- Setting `canReinject=true` in any tier.
- Raw memory in provider prompt.
- Autonomous memory write (all durable writes require policy gate).
- Persisting working, task, audit, or receipt tiers.
- Hosted/cloud persistence backend.
- Any modification to `vision-contract.ts` or `reasoning-contract.ts`.

---

## Execution Plan

1. Read legacy spec absorption registry and ALL agentmemory legacy files.
   Note any design decisions that should influence the durable store interface.
2. Read all target source files and M2 completion review.
3. Design durable store interface for skill-tier and long-term-tier.
4. Implement durable store with privacy filters at write time.
5. Wire tier classifier as policy gate (classifyMemoryTier → decides persistence
   path).
6. Add cross-session read path with receipt output.
7. Add unit tests for write, read, receipt, and filter paths.
8. Add live proof: one governed cross-session memory retrieve producing a live
   receipt via `/api/execute` or equivalent.
9. Confirm `canReinject=false` binding test still PASS.
10. Run TypeScript check (LPF + cvf-web).
11. Run release gate.
12. File completion review.
13. Commit all artifacts.

---

## Evidence Requirements

- Durable store interface: at least one write receipt and one read receipt.
- Privacy filter: at least one test for secret/lifecycle/provenance exclusion.
- `canReinject=false` binding test: PASS.
- Live proof receipt: one governed cross-session retrieve, `evidenceMode=live`.
- TypeScript check: PASS (LPF + cvf-web).
- Release gate: PASS.
- Completion review filed.

---

## Acceptance Criteria

- [ ] M2 CLOSED_PASS confirmed before start.
- [ ] Legacy agentmemory files read and noted.
- [ ] Durable store for skill and long-term tiers implemented.
- [ ] Write path with privacy filters.
- [ ] Read path with receipt output.
- [ ] Summary-only reinjection via AIF C2 gate proven.
- [ ] `canReinject=false` binding test PASS.
- [ ] Unit tests PASS (LPF + cvf-web).
- [ ] Live proof receipt filed.
- [ ] TypeScript check PASS.
- [ ] Release gate PASS.
- [ ] Completion review filed.

---

## Review Gate

The completion review must confirm:

- M2 CLOSED_PASS was verified before implementation began.
- Legacy agentmemory spec files were read (cite at least two file names).
- Durable store is limited to skill and long-term tiers.
- `canReinject=false` binding test result is recorded.
- No raw memory reached provider prompt.
- Live proof receipt is present and `rawSecretPrinted=false`.
- TypeScript check and release gate PASS recorded.

---

## Operator Checkpoint

Operator authorized M1 on 2026-05-24, conditional on M2 CLOSED_PASS.
Codex must self-execute and return the final result after tranche completion.

---

## Closure Checklist

- [ ] M2 CLOSED_PASS confirmed.
- [ ] Legacy spec scan block completed.
- [ ] Durable store implemented.
- [ ] Tests PASS.
- [ ] Live proof receipt filed.
- [ ] TypeScript check PASS.
- [ ] Release gate PASS.
- [ ] Completion review filed and committed.

---

## Return-To-Orchestrator Conditions

Return blocked if: M2 not CLOSED_PASS, `canReinject=false` test fails,
TypeScript check fails, live proof fails, or any attempt to persist tiers
beyond skill and long-term.

---

## Tasks

| Task | Status | Output |
| --- | --- | --- |
| M2 pre-flight check | DONE | M2 completion review confirmed CLOSED_PASS. |
| Legacy spec read | DONE | Notes filed in completion review. |
| Durable store implementation | DONE | `src/durable-memory-store.ts`. |
| Write path + privacy filters | DONE | Tested in `durable-memory-store.test.ts`. |
| Read path + receipt | DONE | Tested in `durable-memory-store.test.ts`. |
| AIF C2 reinjection proof | DONE | Live receipt `rcpt-env-mpjb6x9o-552qp0`. |
| `canReinject=false` test | DONE | PASS in runtime hierarchy + durable store tests. |
| TypeScript check | DONE | LPF and cvf-web checks PASS. |
| Release gate | DONE | PASS recorded in roadmap closure. |
| Completion review | DONE | `docs/reviews/CVF_M1_DURABLE_CROSS_SESSION_MEMORY_COMPLETION_2026-05-24.md`. |

---

## Claim Boundary

M1 claims bounded durable memory for skill and long-term tiers with receipt
evidence. It does not claim autonomous reinjection, broad memory authority,
privacy bypass, hosted/cloud persistence, or enterprise production readiness.
