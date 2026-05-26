# CVF Work Order - Phase 2.B Memory Tail Adapters Migration

Memory class: FULL_RECORD

Status: CLOSED

docType: work_order

Date: 2026-05-21

---

## Purpose

Implement the bounded Phase 2.B memory-tail adapter tranche:

- `E-01 closed -> M-01`
- `M-04` standalone memory-gateway adapter

---

## Authority Chain

- `docs/baselines/CVF_GC018_PHASE_2B_MEMORY_TAIL_ADAPTERS_MIGRATION_2026-05-21.md`
- `docs/reference/archive/CVF_PHASE_2B_MIGRATION_PLAN_2026-05-20.md`
- `docs/reviews/CVF_PHASE_2B_MEMORY_TAIL_ADAPTERS_MIGRATION_CODEX_REBUTTAL_2026-05-21.md`
- `docs/reviews/CVF_PHASE_2B_SAFETY_EXTERNAL_POLICY_RISK_FANOUT_MIGRATION_COMPLETION_2026-05-21.md`

---

## Agent Roles

Codex performed all roles in a self-contained CVF chain:

- Operator proxy: apply user's explicit authorization to finish the memory
  tail.
- Proposer: bound the tranche to additive memory adapter snapshots.
- Reviewer: file Codex rebuttal and scope gate.
- Implementer: make source/test changes.
- Verifier: run package and docs checks.
- Closure reviewer: file completion review.

Claude did not participate.

---

## Scope / Target / Owner Boundary

Targets:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/agent.governed.session.contract.ts`
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.continuation.barrel.ts`
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/phase2b-memory-tail-adapters.test.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled.memory.gateway.contract.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/index.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/phase2b-memory-tail-adapters.test.ts`

---

## Allowed / Forbidden Scope

Allowed:

- additive adapter snapshots;
- focused tests;
- docs/state/handoff updates.

Forbidden:

- persistent memory store;
- new memory tier;
- new reinjection runtime;
- provider runtime behavior;
- Maika changes;
- database schema migration;
- rows outside `M-01` and `M-04`;
- Claude review dependency;
- global freeze lift.

---

## Required First Reads

- `docs/reference/archive/CVF_PHASE_2B_MIGRATION_PLAN_2026-05-20.md`
- `docs/reference/archive/CVF_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-20.md`
- `governance/toolkit/05_OPERATION/CVF_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE.md`
- `docs/reviews/CVF_PHASE_2B_SAFETY_EXTERNAL_POLICY_RISK_FANOUT_MIGRATION_COMPLETION_2026-05-21.md`

---

## Pre-Flight Checks

- Confirm `M-01` depends on already closed `E-01`.
- Confirm `M-04` is standalone in the locked Phase 2.B plan.
- Confirm target files expose existing outputs that can be wrapped without
  semantic changes.

---

## Write Ownership

Write ownership is limited to target source/test files and this tranche's
governance docs/continuity pointers.

---

## Execution Plan

1. Add `M-01` working-memory adapter snapshot.
2. Export `M-01` adapter through continuation barrel.
3. Add `M-04` controlled-memory-gateway adapter snapshot and `WithAdapter`
   helpers.
4. Export `M-04` adapter through Learning Plane index.
5. Add tests.
6. Run package and docs checks.
7. File completion review.

---

## Acceptance Criteria

- Existing behavior remains unchanged.
- Snapshots carry explicit version/source metadata.
- No adapter creates persistence, a new memory tier, or new reinjection
  behavior.
- No live governance proof is claimed.

---

## Evidence Requirements

- Focused tests for CPF and LPF memory-tail adapters.
- Full CPF and LPF package tests.
- CPF and LPF type checks.
- Docs governance and structural checks.
- Completion review records boundaries and no Claude participation.

---

## Review Gate

Close only after tests/checks pass and completion review is filed.

---

## Closure Checklist

- [x] GC-018 filed.
- [x] Code implemented.
- [x] Tests added.
- [x] Verification run.
- [x] Completion review filed.

---

## Return-To-Orchestrator Conditions

Return if implementation requires provider runtime changes, persistent memory,
new memory tiers, database schema migration, new reinjection runtime, Claude
review, or any row outside `M-01` and `M-04`.

---

## Claim Boundary

This work order closes the bounded memory-tail adapter tranche only. It does
not prove broad runtime coherence or live governance behavior.
