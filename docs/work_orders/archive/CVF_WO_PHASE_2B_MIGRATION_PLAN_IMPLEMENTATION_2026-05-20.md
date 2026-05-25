# CVF Work Order - Phase 2.B Migration Plan Implementation

Memory class: FULL_RECORD

Status: CLOSED

docType: work_order

Date: 2026-05-20

Implementer: Codex

---

## Purpose

Produce the authoritative Phase 2.B static migration plan after HN2.b and HN2.c
closure. The plan must enumerate 46 primary migration targets and assign
order, owner, reviewer, done tier, dependency, freeze-release posture, and
adapter target path.

---

## Authority Chain

- `docs/baselines/CVF_GC018_PHASE_2B_MIGRATION_PLAN_2026-05-20.md`
- `docs/reference/CVF_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-20.md`
- `governance/toolkit/05_OPERATION/CVF_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE.md`
- `docs/reviews/CVF_PHASE_2B_MIGRATION_PLAN_CODEX_REBUTTAL_2026-05-20.md`

---

## Agent Roles

- Implementer: Codex in Worker role.
- Reviewer: Codex review posture for static artifact closure.
- Operator: user authorization to proceed after Claude accepted the work
  orders.

---

## Scope / Target / Owner Boundary

Target output:

- `docs/reference/CVF_PHASE_2B_MIGRATION_PLAN_2026-05-20.md`

Owner boundary: static migration-plan authoring only. Future adapters remain
owned by per-surface work orders.

---

## Authorized Inputs

- `docs/baselines/CVF_GC018_PHASE_2B_MIGRATION_PLAN_2026-05-20.md`
- `docs/reference/CVF_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-20.md`
- `governance/toolkit/05_OPERATION/CVF_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE.md`
- `docs/roadmaps/CVF_PHASE_2B_MIGRATION_PLAN_ROADMAP_2026-05-20.md`
- `docs/reviews/CVF_PHASE_2B_MIGRATION_PLAN_CODEX_REBUTTAL_2026-05-20.md`
- Phase 1 adapter maps under
  `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/`

---

## Allowed / Forbidden Scope

Allowed:

- static documentation artifacts;
- queue/state/handoff pointer updates;
- static docs checks.

Forbidden:

- adapter implementation;
- runtime source edits;
- provider, memory, or Maika behavior changes;
- public-sync work;
- broad runtime-coherence claims.

---

## Required First Reads

- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
- `docs/reference/CVF_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-20.md`
- `governance/toolkit/05_OPERATION/CVF_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE.md`
- `docs/roadmaps/CVF_PHASE_2B_MIGRATION_PLAN_ROADMAP_2026-05-20.md`

---

## Pre-Flight Checks

- Confirm HN2.b status is locked.
- Confirm HN2.c status is binding.
- Confirm no existing Phase 2.B plan file with the same date exists.
- Confirm target count rule totals 46.

---

## Write Ownership

Write ownership is limited to:

- `docs/baselines/CVF_GC018_PHASE_2B_MIGRATION_PLAN_2026-05-20.md`
- `docs/work_orders/CVF_WO_PHASE_2B_MIGRATION_PLAN_IMPLEMENTATION_2026-05-20.md`
- `docs/reference/CVF_PHASE_2B_MIGRATION_PLAN_2026-05-20.md`
- `docs/reviews/CVF_PHASE_2B_MIGRATION_PLAN_COMPLETION_2026-05-20.md`
- continuity pointers in queue/state/session memory/handoff

---

## Execution Plan

1. Create the Phase 2.B migration plan artifact:
   `docs/reference/CVF_PHASE_2B_MIGRATION_PLAN_2026-05-20.md`
2. Use the GC-018 target selection rule to list exactly 46 primary targets.
3. Add stage table, per-target table, dependency graph, critical path, stage
   gates, freeze-release posture, citation rule, and change protocol.
4. Create completion review:
   `docs/reviews/CVF_PHASE_2B_MIGRATION_PLAN_COMPLETION_2026-05-20.md`
5. Update continuity pointers after completion.

---

## Evidence Requirements

- Plan contains exactly 46 target rows.
- JSON state/queue parse succeeds after updates.
- Markdown structural completeness check is run.
- Completion review records that no live governance proof was run.

---

## Acceptance Criteria

- GC-018 baseline filed.
- Migration plan filed with status `MIGRATION_PLAN_AUTHORITATIVE`.
- 46 rows present.
- Per-row stage, owner, reviewer, done tier, dependency, freeze posture, and
  path present.
- Completion review filed.

---

## Review Gate

This work closes only after static checks are run and any structural failures
from files in this tranche are corrected.

---

## Closure Checklist

- [x] Baseline filed.
- [x] Work order filed.
- [x] Plan artifact filed.
- [x] Completion review filed.
- [x] Continuity pointers updated.

---

## Return-To-Orchestrator Conditions

Return instead of closing if:

- HN2.b owner map is missing;
- HN2.c rule is missing;
- target count cannot be reconciled to 46;
- implementation would be required to satisfy the request.

---

## Explicit Non-Authorization

This work order does not authorize:

- adapter implementation;
- runtime source edits;
- provider or Maika changes;
- public-sync edits;
- live governance proof claims;
- new role, engine, receipt, tier, method, phase, or kernel surface;
- bulk migration across multiple targets.

---

## Done

Closed by:

- `docs/reference/CVF_PHASE_2B_MIGRATION_PLAN_2026-05-20.md`
- `docs/reviews/CVF_PHASE_2B_MIGRATION_PLAN_COMPLETION_2026-05-20.md`

---

## Claim Boundary

This work order closes only static migration planning. It does not implement or
authorize any adapter, runtime behavior, provider behavior, memory behavior,
Maika behavior, public-sync change, or global freeze lift.
