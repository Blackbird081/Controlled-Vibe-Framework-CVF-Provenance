# CVF Work Order: M2 — D-06 Memory Tier Model Freeze Release

Memory class: FULL_RECORD

Status: WORK_ORDER_READY

docType: work_order

Date: 2026-05-24

Tranche: M2

Roadmap: `docs/roadmaps/CVF_M1_M2_P1_NEXT_VALUE_ROADMAP_2026-05-24.md`

---

## Purpose

Execute a formal one-surface D-06 kernel freeze release for
`memory-tier-classifier.contract.ts` so that downstream M1 durable memory
wiring can proceed.

This is a governance-only tranche. No runtime wiring, no memory storage, and
no persistence change.

---

## Authority Chain

- GC-018: `docs/baselines/CVF_GC018_M2_D06_MEMORY_TIER_FREEZE_RELEASE_2026-05-24.md`
- Roadmap: `docs/roadmaps/CVF_M1_M2_P1_NEXT_VALUE_ROADMAP_2026-05-24.md`
- Freeze-release rule: `governance/toolkit/05_OPERATION/CVF_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE.md`
- Kernel owner map: `docs/reference/CVF_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-20.md`

---

## Scope / Target / Owner Boundary

Target surface: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-tier-classifier.contract.ts`

One surface only. No other kernel surface is touched, modified, or unfrozen.
D-07 (global freeze lift) is permanently rejected and must not be mentioned as
an outcome.

---

## Agent Roles

| Role | Responsibility |
| --- | --- |
| Planner | Read freeze-release rule; confirm one-surface scope. |
| Implementer | Produce freeze-release packet; update owner map entry. |
| Governance Reviewer | Confirm no scope creep, no D-07 implication, correct owner map update. |
| Release Manager | File completion review; commit closure. |

---

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `governance/toolkit/05_OPERATION/CVF_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE.md`
- `docs/reference/CVF_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-20.md`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-tier-classifier.contract.ts`
- `docs/roadmaps/CVF_M1_M2_P1_NEXT_VALUE_ROADMAP_2026-05-24.md`

---

## Pre-Flight Checks

- Confirm `governance/toolkit/05_OPERATION/CVF_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE.md`
  exists and has been read before designing the packet.
- Confirm owner map entry for `memory-tier-classifier.contract.ts` currently
  shows no `freeze_released` status.
- Confirm no other kernel surface is inadvertently staged for modification.
- Confirm no runtime wiring has been added to `memory-tier-classifier.contract.ts`
  or any downstream memory file in the same commit.

---

## Write Ownership

- `docs/governance/` — freeze-release packet.
- `docs/reference/CVF_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-20.md` — owner map
  entry update for `memory-tier-classifier.contract.ts`.
- `docs/reviews/CVF_M2_D06_MEMORY_TIER_FREEZE_RELEASE_COMPLETION_2026-05-24.md`
- `docs/roadmaps/CVF_M1_M2_P1_NEXT_VALUE_ROADMAP_2026-05-24.md` — update M2
  row status to `CLOSED_PASS`.
- `docs/work_orders/CVF_WO_M1_DURABLE_CROSS_SESSION_MEMORY_2026-05-24.md` —
  update M1 status from `DEMAND_GATED` to `WORK_ORDER_READY`.

---

## Allowed / Forbidden Scope

Allowed:

- Freeze-release packet document for memory tier classifier surface.
- Owner map entry update: add `freeze_released: true`, `freeze_release_date`,
  `freeze_release_rationale`, and link to this work order.
- Completion review and governance sign-off.
- TypeScript check of any modified files.

Forbidden:

- Modifying any other kernel surface.
- Any runtime memory wiring, storage, or persistence change.
- Any mention of D-07 as an outcome or implication.
- Touching `vision-contract.ts`, `reasoning-contract.ts`, or other frozen
  contracts not in scope.
- Public-sync publication (governance-only tranche; public catalog update
  deferred to M1 close).

---

## Execution Plan

1. Read freeze-release rule fully to understand required packet components.
2. Read `memory-tier-classifier.contract.ts` to confirm surface scope.
3. Read owner map entry for this surface.
4. Produce freeze-release packet at:
   `docs/governance/CVF_FREEZE_RELEASE_PACKET_M2_MEMORY_TIER_2026-05-24.md`
   (or equivalent path per freeze-release rule convention).
5. Update owner map entry for `memory-tier-classifier.contract.ts` with
   `freeze_released` status.
6. Run TypeScript check.
7. File completion review at:
   `docs/reviews/CVF_M2_D06_MEMORY_TIER_FREEZE_RELEASE_COMPLETION_2026-05-24.md`
8. Commit all artifacts.
9. Verify M1 work order is unblocked (change its status from `DEMAND_GATED` to
   `WORK_ORDER_READY` and note M2 CLOSED_PASS as the unblock condition met).

---

## Evidence Requirements

- Freeze-release packet: rationale, scope, approver, surface path, evidence
  that only one surface is affected.
- Owner map diff: `freeze_released: true` entry for target surface.
- TypeScript check: PASS.
- Completion review filed.

---

## Acceptance Criteria

- [ ] Freeze-release rule read and respected.
- [ ] Packet filed with all required components.
- [ ] Owner map entry updated.
- [ ] No other kernel surface modified.
- [ ] TypeScript check PASS.
- [ ] Completion review filed.
- [ ] M1 work order status updated to `WORK_ORDER_READY`.

---

## Review Gate

The completion review must confirm:

- One surface only was modified (memory tier model).
- No runtime wiring or memory storage change was introduced.
- Owner map diff is present and correct.
- D-07 is not mentioned as an outcome or implication.
- TypeScript check PASS is recorded.
- M1 work order was unblocked.

---

## Operator Checkpoint

Operator authorized M2 on 2026-05-24. D-06 surface is memory tier model
(`memory-tier-classifier.contract.ts`) as recommended by Claude.

Codex must self-execute and return the final result after tranche completion.

---

## Closure Checklist

- [ ] Freeze-release packet filed.
- [ ] Owner map updated.
- [ ] TypeScript check PASS.
- [ ] Completion review filed and committed.
- [ ] M1 work order unblocked.

---

## Return-To-Orchestrator Conditions

Return blocked if: TypeScript check fails, scope exceeds one surface, or
freeze-release rule requirements cannot be met.

---

## Tasks

| Task | Status | Output |
| --- | --- | --- |
| Read freeze-release rule | PENDING | Confirm required packet components. |
| Read surface + owner map | PENDING | Confirm scope. |
| Produce freeze-release packet | PENDING | `docs/governance/CVF_FREEZE_RELEASE_PACKET_M2_*` |
| Update owner map | PENDING | `freeze_released: true` entry. |
| TypeScript check | PENDING | PASS. |
| Completion review | PENDING | `docs/reviews/CVF_M2_*_COMPLETION_2026-05-24.md` |
| Unblock M1 | PENDING | M1 work order status → `WORK_ORDER_READY`. |

---

## Claim Boundary

This work order closes governance-only. Runtime memory wiring is M1 scope.
D-07 is permanently rejected and is not an outcome of this tranche.
No claim of durable memory, persistent storage, cross-session memory, or any
other kernel surface modification is authorized by this tranche.
