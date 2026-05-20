# CVF Work Order - Phase 2.B Safety External Policy Risk Fanout Migration

Memory class: FULL_RECORD

Status: CLOSED

docType: work_order

Date: 2026-05-21

---

## Purpose

Implement the grouped but bounded Phase 2.B safety-tail,
external/ecosystem-risk, and external-policy adapter tranche:

- `R-02 -> R-04 / R-05 / R-15 / R-16`
- `R-01 -> R-06 / R-07 / R-08 / R-09 / R-10 / R-11 / R-12`
- `P-01 -> P-07 / P-08`

---

## Authority Chain

- `docs/baselines/CVF_GC018_PHASE_2B_SAFETY_EXTERNAL_POLICY_RISK_FANOUT_MIGRATION_2026-05-21.md`
- `docs/reference/CVF_PHASE_2B_MIGRATION_PLAN_2026-05-20.md`
- `docs/reviews/CVF_PHASE_2B_SAFETY_EXTERNAL_POLICY_RISK_FANOUT_MIGRATION_CODEX_REBUTTAL_2026-05-21.md`
- `docs/reviews/CVF_PHASE_2B_IDENTITY_CONTROL_PLANE_ADAPTERS_MIGRATION_COMPLETION_2026-05-21.md`

---

## Agent Roles

Codex performed all roles in a self-contained CVF chain:

- Operator proxy: apply user's explicit authorization to finish the grouped
  chains.
- Proposer: bound the tranche to additive risk/policy adapter snapshots.
- Reviewer: file Codex rebuttal and scope gate.
- Implementer: make source/test changes.
- Verifier: run package and docs checks.
- Closure reviewer: file completion review.

Claude did not participate.

---

## Scope / Target / Owner Boundary

Targets:

- `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/kernel-architecture/internal_ledger/risk_evolution.ts`
- `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/kernel-architecture/kernel/04_refusal_router/refusal.risk.ts`
- `EXTENSIONS/CVF_v1.8_SAFETY_HARDENING/core/risk/risk.lock.ts`
- `EXTENSIONS/CVF_v1.8_SAFETY_HARDENING/core/risk/risk.scorer.ts`
- `EXTENSIONS/CVF_ECO_v1.2_LLM_RISK_ENGINE/src/risk.scorer.ts`
- `EXTENSIONS/CVF_ECO_v1.2_LLM_RISK_ENGINE/src/risk.aggregator.ts`
- `EXTENSIONS/CVF_ECO_v2.0_AGENT_GUARD_SDK/src/risk.module.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/guards/risk-gate.guard.ts`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/risk-gate.guard.ts`
- `EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/governance/guard_runtime/guards/risk.gate.guard.ts`
- `EXTENSIONS/CVF_v1.2.1_EXTERNAL_INTEGRATION/governance_hooks/risk.scoring.hook.ts`
- `EXTENSIONS/CVF_v1.2.1_EXTERNAL_INTEGRATION/policies/policy.decision.engine.ts`
- `EXTENSIONS/CVF_v1.2.1_EXTERNAL_INTEGRATION/certification/certification.state.machine.ts`
- `EXTENSIONS/CVF_v1.2.2_SKILL_GOVERNANCE_ENGINE/skill_system/governance/risk.scorer.ts`
- focused tests adjacent to those surfaces.

---

## Allowed / Forbidden Scope

Allowed:

- additive adapter snapshots;
- focused tests;
- docs/state/handoff updates.

Forbidden:

- provider runtime behavior;
- Maika changes;
- persistent memory store;
- database schema migration;
- new policy/risk/guard engines;
- kernel owner replacement;
- rows outside the listed chains;
- Claude review dependency;
- global freeze lift.

---

## Required First Reads

- `docs/reference/CVF_PHASE_2B_MIGRATION_PLAN_2026-05-20.md`
- `docs/reference/CVF_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-20.md`
- `governance/toolkit/05_OPERATION/CVF_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE.md`
- `docs/reviews/CVF_PHASE_2B_IDENTITY_CONTROL_PLANE_ADAPTERS_MIGRATION_COMPLETION_2026-05-21.md`

---

## Pre-Flight Checks

- Confirm requested rows are in the locked Phase 2.B plan.
- Confirm prior policy/risk and identity/control-plane slices are closed.
- Confirm target files expose existing decisions/scores that can be wrapped
  without semantic changes.

---

## Write Ownership

Write ownership is limited to the target source/test files and this tranche's
governance docs/continuity pointers.

---

## Execution Plan

1. Add R-02/R-04/R-05/R-15/R-16 safety-tail adapter snapshots.
2. Add R-01/R-06/R-07/R-08/R-09/R-10/R-11/R-12 external/ecosystem risk
   fanout adapter snapshots.
3. Add P-01/P-07/P-08 external policy adapter snapshots.
4. Add tests.
5. Run package and docs checks.
6. File completion review.

---

## Acceptance Criteria

- Existing behavior remains unchanged.
- Snapshots carry explicit version/source metadata.
- No adapter performs provider or external runtime execution.
- No live governance proof is claimed.

---

## Evidence Requirements

- Focused tests for each touched package with an available toolchain.
- Build/typecheck for touched packages where available.
- Docs governance and structural checks.
- Completion review records boundaries and no Claude participation.

---

## Review Gate

Close only after focused tests/checks pass or an existing package tooling
boundary is documented, and completion review is filed.

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
database schema migration, new risk/policy/guard engines, kernel owner
replacement, Claude review, or any row outside the listed chains.

---

## Claim Boundary

This work order closes the grouped safety/external-policy risk fanout adapter
tranche only. It does not prove broad runtime coherence or live governance
behavior.
