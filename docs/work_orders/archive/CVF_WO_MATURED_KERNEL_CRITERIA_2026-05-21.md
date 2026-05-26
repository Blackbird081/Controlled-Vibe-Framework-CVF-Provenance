# CVF Work Order Matured Kernel Criteria

Memory class: FULL_RECORD

Status: CLOSED

docType: work_order

Date: 2026-05-21

---

## Purpose

Execute the matured-kernel criteria roadmap as a bounded governance
infrastructure tranche.

---

## Authority Chain

- Operator instruction: 2026-05-21 approval to proceed.
- Active state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- Roadmap:
  `docs/roadmaps/CVF_MATURED_KERNEL_CRITERIA_ROADMAP_2026-05-21.md`
- GC-018:
  `docs/baselines/CVF_GC018_MATURED_KERNEL_CRITERIA_2026-05-21.md`
- HN2.b owner map:
  `docs/reference/archive/CVF_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-20.md`
- HN2.c freeze-release rule:
  `governance/toolkit/05_OPERATION/CVF_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE.md`
- Active handoff: `AGENT_HANDOFF_V10_2026-05-19.md`

---

## Agent Roles

Codex performs all roles for this bounded tranche:

- Orchestrator: constrain the tranche to criteria only.
- Implementer: file roadmap, baseline, work order, reference, and completion.
- Reviewer: verify that no freeze release or owner replacement is implied.
- Auditor: run governance checks and sync session continuity.

---

## Scope / Target / Owner Boundary

Allowed scope:

- Matured-kernel criteria reference.
- Criteria vocabulary.
- Per-surface maturity criteria.
- Permanent-freeze recommendation criteria.
- HN2.c release-candidate bridge.
- Completion review and session sync.

Forbidden scope:

- Changing `freezePosture`.
- Releasing any kernel surface.
- Updating HN2.b owner map classifications.
- Replacing a kernel owner.
- Global freeze lift.
- Mechanical guard implementation.
- Runtime/provider/database/memory/Maika/public-sync changes.

Risk ceiling: R2.

---

## Operator Checkpoint

Checkpoint source: operator approval on 2026-05-21 after Codex recommended
criteria filing without freeze lift.

Interpretation: proceed with documentation-only criteria. Any release,
owner-map update, guard implementation, or public claim requires a new
operator checkpoint and fresh GC-018.

---

## Write Ownership

Owned by this work order:

- `docs/roadmaps/CVF_MATURED_KERNEL_CRITERIA_ROADMAP_2026-05-21.md`
- `docs/baselines/CVF_GC018_MATURED_KERNEL_CRITERIA_2026-05-21.md`
- `docs/work_orders/CVF_WO_MATURED_KERNEL_CRITERIA_2026-05-21.md`
- `docs/reference/CVF_MATURED_KERNEL_CRITERIA_2026-05-21.md`
- `docs/reviews/CVF_MATURED_KERNEL_CRITERIA_COMPLETION_2026-05-21.md`
- active session continuity files

Not owned:

- HN2.b owner map;
- HN2.c release rule;
- doctrine;
- runtime source;
- public-sync repository.

---

## Target / Source Under Review

Primary target:

- `docs/reference/CVF_MATURED_KERNEL_CRITERIA_2026-05-21.md`

---

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `docs/reference/archive/CVF_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-20.md`
- `governance/toolkit/05_OPERATION/CVF_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE.md`
- `docs/roadmaps/CVF_MATURED_KERNEL_CRITERIA_ROADMAP_2026-05-21.md`

---

## Pre-Flight Checks

Commands:

```powershell
git status --short
git remote -v
```

---

## Evidence Requirements

- Criteria reference file exists.
- Completion review records no-lift disposition.
- Active state remains `freezePosture: governance_kernel_freeze_recommended`.
- JSON parse for active state and review queue.
- Active session state compatibility.
- Docs governance compatibility.
- Markdown structural completeness.
- Git whitespace check.
- Local governance hook chain.

---

## Execution Plan

1. File roadmap and GC-018.
2. File this work order.
3. File criteria reference.
4. File completion review.
5. Sync active state, review queue, and handoff.
6. Run governance checks.
7. Commit and push provenance changes.

---

## Acceptance Criteria

- Criteria reference defines posture vocabulary and criteria.
- No surface is released.
- No owner map is superseded.
- HN2.c release process remains mandatory for any future one-surface release.
- Global freeze lift remains prohibited.
- Governance checks pass.

---

## Review Gate

Required checks before provenance commit:

- JSON parse for active state and review queue.
- Active session state compatibility.
- Docs governance gate.
- Markdown structural completeness gate.
- Git whitespace check.
- Local governance hook chain.

---

## Closure Checklist

- [x] Roadmap filed.
- [x] GC-018 accepted.
- [x] Work order filed.
- [x] Criteria reference filed.
- [x] Completion review filed.
- [x] Active session continuity synced.
- [x] Governance checks run before commit.

---

## Return-To-Orchestrator Conditions

Return for a new GC-018/work order before starting:

- one-surface freeze release;
- global freeze lift;
- kernel-owner replacement;
- HN2.b owner-map supersession;
- HN2.c rule change;
- mechanical guard implementation;
- public-sync claim.

---

## Claim Boundary

This work order closes only matured-kernel criteria filing. It does not release
any frozen surface, mature the full kernel, replace owners, change doctrine,
change runtime behavior, or publish a public claim.
