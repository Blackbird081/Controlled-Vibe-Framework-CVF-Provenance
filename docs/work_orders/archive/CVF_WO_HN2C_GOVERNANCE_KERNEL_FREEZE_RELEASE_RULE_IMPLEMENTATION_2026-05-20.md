# Work Order - HN2.c Governance Kernel Freeze-Release Rule Implementation

Memory class: FULL_RECORD

Status: CLOSED

docType: work_order

Worker role: Codex

Date dispatched: 2026-05-20

---

## Purpose

Produce the HN2.c freeze-release rule authorized by GC-018 after HN2.b owner
map closure.

---

## Scope / Target / Owner Boundary

In scope:

- `docs/baselines/CVF_GC018_HN2C_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE_2026-05-20.md`
- `governance/toolkit/05_OPERATION/CVF_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE.md`
- `docs/reviews/CVF_HN2C_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE_COMPLETION_2026-05-20.md`
- active queue/state/handoff updates

Out of scope:

- HN2.b owner-map changes.
- Phase 2.B migration plan.
- Mechanical repository guard.
- Freeze release or global freeze lift.
- Runtime/code/provider/memory/Maika edits.
- Doctrine edits.
- Public-sync update.

---

## Target / Source Under Review

Baseline:

- `docs/baselines/CVF_GC018_HN2C_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE_2026-05-20.md`

Predecessors:

- `docs/reference/CVF_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-20.md`
- `docs/reviews/CVF_HN2C_FREEZE_RELEASE_RULE_CODEX_REBUTTAL_2026-05-20.md`

---

## Authority Chain

- HN2.b owner map:
  `docs/reference/CVF_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-20.md`
- HN2.c rebuttal:
  `docs/reviews/CVF_HN2C_FREEZE_RELEASE_RULE_CODEX_REBUTTAL_2026-05-20.md`
- HN2.c GC-018:
  `docs/baselines/CVF_GC018_HN2C_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE_2026-05-20.md`

---

## Agent Roles

- Implementer: Codex in Worker role.
- Reviewer: Codex completion-review posture.
- Operator: user authorization to proceed after HN2.b closure.

---

## Required First Reads

- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
- `docs/reference/CVF_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-20.md`
- `docs/roadmaps/CVF_HN2C_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE_ROADMAP_2026-05-20.md`
- `docs/reviews/CVF_HN2C_FREEZE_RELEASE_RULE_CODEX_REBUTTAL_2026-05-20.md`

---

## Pre-Flight Checks

- Confirm HN2.b owner map is locked.
- Confirm HN2.c rebuttal is non-blocking with prerequisite satisfied.
- Confirm mechanical guard and actual release packets remain out of scope.

---

## Write Ownership

Write ownership is limited to the HN2.c baseline, work order, rule artifact,
completion review, control-matrix pointer, and continuity pointers.

---

## Execution Plan

1. File GC-018 baseline.
2. Produce freeze-release rule under `governance/toolkit/05_OPERATION/`.
3. File completion review.
4. Update active review queue/state/handoff.
5. Run JSON, active-session, docs governance, and Markdown structural checks.

---

## Evidence Requirements

- Rule cites the locked HN2.b owner map.
- Rule has a change-class table and five release conditions.
- Rule explicitly prohibits global lift and mechanical enforcement claims.

---

## Acceptance Criteria

- [x] GC-018 baseline filed.
- [x] Rule artifact filed under `governance/toolkit/05_OPERATION/`.
- [x] Rule names HN2.b owner map as prerequisite.
- [x] Rule includes closed change-class table.
- [x] Rule includes five release conditions.
- [x] Rule includes authority chain and doctrine supremacy clause.
- [x] Rule prohibits global lift.
- [x] Rule records mechanical guard as separate follow-on.
- [x] Completion review filed.

---

## Review Gate

Close only after the rule artifact exists and the completion review records the
policy-only boundary.

---

## Closure Checklist

- [x] Baseline filed.
- [x] Work order filed.
- [x] Rule artifact filed.
- [x] Control matrix pointer added.
- [x] Completion review filed.

---

## Return-To-Orchestrator Conditions

Return instead of closing if HN2.b is not locked, if a mechanical guard becomes
necessary, or if any release/global lift is requested.

---

## Claim Boundary

This work order implements only the freeze-release rule artifact. It does not
authorize any surface release, runtime behavior, doctrine change, public claim,
or Phase 2.B implementation.
