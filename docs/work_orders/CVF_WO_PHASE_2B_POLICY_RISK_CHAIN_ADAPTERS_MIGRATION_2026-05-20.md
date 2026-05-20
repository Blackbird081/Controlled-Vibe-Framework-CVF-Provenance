# CVF Work Order - Phase 2.B Policy Risk Chain Adapters Migration

Memory class: FULL_RECORD

Status: CLOSED

docType: work_order

Date: 2026-05-20

---

## Purpose

Implement the grouped but bounded Phase 2.B policy/risk adapter tranche:

- `P-01 -> P-06 -> P-05`
- `P-01 -> P-02 + P-03 -> P-04`
- `R-02 -> R-03 -> R-13 / R-14`

---

## Authority Chain

- `docs/baselines/CVF_GC018_PHASE_2B_POLICY_RISK_CHAIN_ADAPTERS_MIGRATION_2026-05-20.md`
- `docs/reference/CVF_PHASE_2B_MIGRATION_PLAN_2026-05-20.md`
- `docs/reviews/CVF_PHASE_2B_POLICY_RISK_CHAIN_ADAPTERS_MIGRATION_CODEX_REBUTTAL_2026-05-20.md`
- `docs/reviews/CVF_PHASE_2B_AUDIT_TRACE_TASK_RECEIPT_CHAINS_MIGRATION_COMPLETION_2026-05-20.md`

---

## Agent Roles

Codex performed all roles in a self-contained CVF chain:

- Operator proxy: apply user's explicit authorization to finish the grouped
  chains.
- Proposer: bound the tranche to policy/risk adapter surfaces.
- Reviewer: file Codex rebuttal and scope gate.
- Implementer: make source/test changes.
- Verifier: run package and compile checks.
- Closure reviewer: file completion review.

Claude did not participate.

---

## Scope / Target / Owner Boundary

Targets:

- `EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/core/policy_engine.py`
- `EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/api/server.py`
- `EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/core_orchestrator.py`
- `EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/main.py`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`
- `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/policy/risk.engine.ts`
- `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/kernel-architecture/kernel/03_contamination_guard/risk_detector.ts`
- `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/kernel-architecture/kernel/03_contamination_guard/risk_propagation_engine.ts`
- `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/kernel-architecture/kernel/03_contamination_guard/risk_scorer.ts`
- focused tests adjacent to those surfaces.

---

## Allowed / Forbidden Scope

Allowed:

- additive adapter snapshots;
- index type/function exports;
- focused tests;
- docs/state/handoff updates.

Forbidden:

- provider runtime behavior;
- Maika changes;
- persistent memory store;
- database schema migration;
- kernel owner replacement;
- rows outside the listed chains;
- Claude review dependency;
- global freeze lift.

---

## Required First Reads

- `docs/reference/CVF_PHASE_2B_MIGRATION_PLAN_2026-05-20.md`
- `docs/reference/CVF_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-20.md`
- `governance/toolkit/05_OPERATION/CVF_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE.md`
- `docs/reviews/CVF_PHASE_2B_AUDIT_TRACE_TASK_RECEIPT_CHAINS_MIGRATION_COMPLETION_2026-05-20.md`

---

## Pre-Flight Checks

- Confirm requested rows are in the locked Phase 2.B plan.
- Confirm prior receipt-chain slices are closed.
- Confirm existing policy/risk decisions are preserved.

---

## Write Ownership

Write ownership is limited to target source/test files and this tranche's
governance docs/continuity pointers.

---

## Execution Plan

1. Add P-01 policy-engine adapter snapshot.
2. Add P-02 API response adapter helper.
3. Add P-03 orchestrator snapshot.
4. Add P-04 main local execution summary adapter.
5. Add P-06 routing-policy contract snapshot.
6. Add P-05 model-gateway index exports.
7. Add R-02 risk-engine adapter snapshot.
8. Add R-03/R-13/R-14 Safety Runtime adapter snapshots.
9. Add tests.
10. Run package, compile, and docs checks.
11. File completion review.

---

## Evidence Requirements

- Tests/checks for Governance Engine and Model Gateway.
- TypeScript compile checks for Safety Runtime touched policy/kernel surfaces.
- Docs governance and structural checks.
- Completion review records boundaries and no Claude participation.

---

## Acceptance Criteria

- Existing policy/risk behavior remains readable and unchanged.
- Snapshots carry explicit version/source metadata.
- Routing-policy adapter does not perform provider fallback execution.
- Safety Runtime adapters preserve existing return contracts.
- No provider/Maika/persistent-memory behavior is introduced.

---

## Review Gate

Close only after tests/checks pass or any package-environment limitation is
recorded precisely in the completion review.

---

## Closure Checklist

- [x] GC-018 filed.
- [x] Code implemented.
- [x] Tests added.
- [x] Verification run.
- [x] Completion review filed.

---

## Return-To-Orchestrator Conditions

Return if implementation requires provider runtime changes, persistence-store,
database schema migration, kernel owner replacement, Claude review, or any row
outside the listed chains.

---

## Claim Boundary

This work order closes the grouped policy/risk adapter tranche only. It does
not prove broad runtime coherence or live governance behavior.
