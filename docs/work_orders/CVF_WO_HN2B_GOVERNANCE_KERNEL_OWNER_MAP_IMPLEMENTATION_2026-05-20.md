# Work Order - HN2.b Governance Kernel Owner Map Implementation

Memory class: FULL_RECORD

Status: CLOSED

docType: work_order

Worker role: Codex

Date dispatched: 2026-05-20

---

## Purpose

Produce the HN2.b owner map artifact authorized by GC-018 and close the owner
map as the routing reference for future kernel-surface work orders.

---

## Scope / Target / Owner Boundary

In scope:

- `docs/baselines/CVF_GC018_HN2B_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-20.md`
- `docs/reference/CVF_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-20.md`
- `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md`
- `docs/reviews/CVF_HN2B_GOVERNANCE_KERNEL_OWNER_MAP_COMPLETION_2026-05-20.md`
- active queue/state/handoff updates

Out of scope:

- HN2.c freeze-release rule.
- Phase 2.B migration plan.
- Runtime/code/provider/memory/Maika edits.
- Doctrine edits.
- Public-sync update.
- Freeze posture lift.

---

## Target / Source Under Review

Baseline:

- `docs/baselines/CVF_GC018_HN2B_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-20.md`

Predecessors:

- `docs/reviews/CVF_HN2A_GOVERNANCE_KERNEL_OWNER_INVENTORY_2026-05-20.md`
- `docs/reviews/CVF_HN2B_GOVERNANCE_KERNEL_OWNER_MAP_CODEX_REBUTTAL_2026-05-20.md`

---

## Authority Chain

- HN2.a inventory:
  `docs/reviews/CVF_HN2A_GOVERNANCE_KERNEL_OWNER_INVENTORY_2026-05-20.md`
- HN2.b rebuttal:
  `docs/reviews/CVF_HN2B_GOVERNANCE_KERNEL_OWNER_MAP_CODEX_REBUTTAL_2026-05-20.md`
- HN2.b GC-018:
  `docs/baselines/CVF_GC018_HN2B_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-20.md`

---

## Agent Roles

- Implementer: Codex in Worker role.
- Reviewer: Codex completion-review posture.
- Operator: user authorization to proceed after Claude accepted the work
  order.

---

## Required First Reads

- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
- `docs/roadmaps/CVF_HN2B_GOVERNANCE_KERNEL_OWNER_MAP_ROADMAP_2026-05-20.md`
- `docs/reviews/CVF_HN2B_GOVERNANCE_KERNEL_OWNER_MAP_CODEX_REBUTTAL_2026-05-20.md`

---

## Pre-Flight Checks

- Confirm the HN2.b rebuttal is non-blocking.
- Confirm no prior owner-map artifact for the same date exists.
- Confirm HN2.c and Phase 2.B remain out of scope until this map is locked.

---

## Write Ownership

Write ownership is limited to the HN2.b baseline, work order, owner map,
completion review, control-matrix pointer, and continuity pointers.

---

## Execution Plan

1. File GC-018 baseline.
2. Produce owner map under `docs/reference/`.
3. Add control-matrix pointer.
4. File completion review.
5. Update active review queue/state/handoff.
6. Run JSON, active-session, docs governance, and Markdown structural checks.

---

## Evidence Requirements

- Owner map covers all 12 HN2.a surfaces.
- Owner map uses the closed classification set and class precedence.
- Completion review records the no-runtime/no-freeze-lift boundary.

---

## Acceptance Criteria

- [x] GC-018 baseline filed.
- [x] Owner map artifact filed under `docs/reference/`.
- [x] Owner map covers all 12 HN2.a surfaces.
- [x] Owner map uses the closed 11-class set and class precedence.
- [x] Forbidden-expansion register included.
- [x] Citation rule and change protocol included.
- [x] Control matrix pointer added.
- [x] Completion review filed.

---

## Review Gate

Close only after the owner map exists and the completion review records the
static-reference boundary.

---

## Closure Checklist

- [x] Baseline filed.
- [x] Work order filed.
- [x] Owner map filed.
- [x] Control matrix pointer added.
- [x] Completion review filed.

---

## Return-To-Orchestrator Conditions

Return instead of closing if the closed classification set must change, if a
new kernel surface is required, or if implementation/runtime behavior is needed.

---

## Claim Boundary

This work order implements only the owner-map documentation artifact. It does
not authorize HN2.c, Phase 2.B, runtime behavior, doctrine changes, public
claims, or freeze release.
