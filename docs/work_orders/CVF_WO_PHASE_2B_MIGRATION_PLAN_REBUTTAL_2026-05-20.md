# CVF Work Order — Phase 2.B Migration Plan Rebuttal

Memory class: SUMMARY_RECORD

Status: READY_FOR_REBUTTAL_EXECUTION

GC-018 required: No — reviewer rebuttal only. Any later implementation needs a
fresh Phase 2.B-specific GC-018 (filed only after HN2.b LOCKED and HN2.c
BINDING) and a separate implementation work order that produces the migration
plan artifact.

## Authority Chain

- Active session state:
  `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- Active review queue item: `phase-2b-migration-plan-roadmap`
- Target roadmap:
  `docs/roadmaps/CVF_PHASE_2B_MIGRATION_PLAN_ROADMAP_2026-05-20.md`
- Prerequisite roadmap (LOCKED required before GC-018):
  `docs/roadmaps/CVF_HN2B_GOVERNANCE_KERNEL_OWNER_MAP_ROADMAP_2026-05-20.md`
- Prerequisite roadmap (BINDING required before GC-018):
  `docs/roadmaps/CVF_HN2C_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE_ROADMAP_2026-05-20.md`
- GAP discovery anchor (memory):
  `project_gap_discovery_method_2026-05-18.md` — "Phase 2.B migration plan
  still missing owner/order/done-criterion"

## Agent Roles

- Operator: selected Phase 2.B planning as a strategic harden move.
- Codex reviewer: performs the read-only Phase 2.B rebuttal and files the
  rebuttal packet.
- Orchestrator: may file a later Phase 2.B GC-018 only after HN2.b is LOCKED
  AND HN2.c is BINDING AND this rebuttal returns non-blocking.
- Worker: must not implement anything from this work order.

## Purpose

Produce the reviewer-role rebuttal for the Phase 2.B migration plan roadmap.

The rebuttal must decide whether the roadmap may proceed (after HN2.b LOCKED
and HN2.c BINDING) to a slice-specific GC-018 and implementation work order
for producing the Phase 2.B migration plan artifact, while preserving the
"per-surface slice work order" model and prohibiting bulk migration.

## Scope

Allowed scope:

- Read-only review of the Phase 2.B roadmap.
- Read-only review of HN2.b and HN2.c roadmaps (to verify prerequisite
  framing is honest).
- Read-only review of HN2.a inventory.
- Read-only review of Phase 1.x adapter map artifacts (sample 2–3 to verify
  46-surface claim is grounded).
- Read-only review of `GovernedCapability.availableFrom: 'Phase-2B'`
  placeholder in `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/` to confirm the
  wire-up target.
- Read-only review of GAP discovery memory direction.
- Filing one rebuttal packet at:
  `docs/reviews/CVF_PHASE_2B_MIGRATION_PLAN_CODEX_REBUTTAL_2026-05-20.md`
- Updating `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` and
  `CVF_SESSION/ACTIVE_SESSION_STATE.json` after the rebuttal is filed.
- Updating `AGENT_HANDOFF_V10_2026-05-19.md` only if needed for continuity.

Forbidden scope:

- No enumeration of the 46 surfaces.
- No implementation of the migration plan artifact.
- No GC-018 baseline for implementation.
- No per-surface adapter authoring.
- No new role taxonomy, policy/risk/guard engine, receipt envelope, memory
  tier, method contract, or phase.
- No bulk migration authorization.
- No freeze lift.
- No doctrine modification.
- No public-sync or public claim update.
- No code/runtime/provider/memory/Maika changes.
- No Phase 2.C or later phase planning.

## Required First Reads

1. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
2. `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
3. `docs/roadmaps/CVF_PHASE_2B_MIGRATION_PLAN_ROADMAP_2026-05-20.md`
4. `docs/roadmaps/CVF_HN2B_GOVERNANCE_KERNEL_OWNER_MAP_ROADMAP_2026-05-20.md`
5. `docs/roadmaps/CVF_HN2C_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE_ROADMAP_2026-05-20.md`
6. `docs/reviews/CVF_HN2A_GOVERNANCE_KERNEL_OWNER_INVENTORY_2026-05-20.md`
7. `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/` (read enough to confirm
   GovernedCapability `availableFrom: 'Phase-2B'` placeholder is present).
8. At least 2 Phase 1.x adapter map review files (search `docs/reviews/` for
   `PHASE_1` or `ADAPTER_MAP`) to verify the 46-surface direction.
9. `ECOSYSTEM/doctrine/CVF_DOCTRINE_RULES.md`

## Pre-Flight Checks

Before writing the rebuttal, Codex must verify:

- `phase-2b-migration-plan-roadmap` is `READY_FOR_REBUTTAL` in the queue.
- The roadmap declares HN2.b LOCKED as a hard prerequisite for Phase 2.B
  GC-018.
- The roadmap declares HN2.c BINDING as a hard prerequisite for Phase 2.B
  GC-018.
- The roadmap declares 4 inputs (order, owner, done, dependency) with
  schemas, NOT a list of 46 surfaces.
- The roadmap declares a tiered done-criterion table.
- The roadmap forbids bulk migration.
- The roadmap requires per-surface slice work orders.
- The roadmap forbids new role / engine / receipt / tier / method / phase.
- The roadmap does NOT enumerate the 46 surfaces (that is Phase 2.B GC-018's
  job).
- The roadmap does NOT lift the freeze.

## Write Ownership

Codex reviewer may create:

- `docs/reviews/CVF_PHASE_2B_MIGRATION_PLAN_CODEX_REBUTTAL_2026-05-20.md`

Codex reviewer may update:

- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V10_2026-05-19.md`

Codex reviewer must not modify:

- `docs/roadmaps/CVF_PHASE_2B_*` (target roadmap)
- `docs/roadmaps/CVF_HN2B_*`, `docs/roadmaps/CVF_HN2C_*` (sibling
  prerequisite roadmaps)
- `docs/reviews/CVF_HN2A_*` (closed inventory)
- Phase 1.x adapter map review files.
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/*` or any other code.
- `ECOSYSTEM/doctrine/*`
- `governance/toolkit/05_OPERATION/*`
- Public-sync repo.

## Execution Plan

1. Confirm queue order and Phase 2.B scope.
2. Read the Phase 2.B roadmap end-to-end.
3. Read HN2.b and HN2.c roadmaps to verify Phase 2.B's prerequisite framing.
4. Read at least 2 Phase 1.x adapter map review files to verify the
   46-surface direction is grounded.
5. Read `GovernedCapability.availableFrom: 'Phase-2B'` to confirm placeholder.
6. Verify the four input schemas (order, owner, done, dependency) are each
   complete and independent.
7. Verify the tiered done-criterion table is consistent.
8. Verify the "per-surface slice work order" model is required and "bulk
   migration" is forbidden.
9. Verify kernel-touching adapter tier requires HN2.c-compliant freeze
   release citation.
10. Decide one of:
    - `NON_BLOCKING_WITH_SCOPE_REFINEMENT`
    - `NON_BLOCKING_WITH_EXISTING_EVIDENCE`
    - `BLOCKING`
11. File the rebuttal packet with findings, risks, required corrections, and
    explicit claim boundary.
12. Update active review queue/state/handoff routing.
13. Run JSON parse and active-session state checks.
14. Run docs governance and Markdown structural checks if new docs were filed.

## Tasks

- [ ] Confirm queue status for `phase-2b-migration-plan-roadmap`.
- [ ] Verify roadmap names HN2.b LOCKED AND HN2.c BINDING as hard
  prerequisites for Phase 2.B GC-018.
- [ ] Verify the four input schemas (order, owner, done, dependency) are
  named with explicit schema requirements.
- [ ] Verify the tiered done-criterion table covers contract-only / pack-
  local / runtime / kernel-touching tiers.
- [ ] Verify kernel-touching tier requires HN2.c-compliant freeze release
  citation.
- [ ] Verify "no new role IDs" rule in owner-assignment input.
- [ ] Verify DAG/no-cycle rule in dependency input.
- [ ] Verify bulk migration is explicitly forbidden.
- [ ] Verify per-surface slice work orders are required.
- [ ] Verify the roadmap does NOT enumerate the 46 surfaces.
- [ ] Verify the roadmap does NOT lift the freeze.
- [ ] Verify GovernedCapability `availableFrom: 'Phase-2B'` placeholder is
  the wire-up target.
- [ ] File rebuttal at
  `docs/reviews/CVF_PHASE_2B_MIGRATION_PLAN_CODEX_REBUTTAL_2026-05-20.md`.
- [ ] Update active queue/state routing.
- [ ] Run required verification.

## Acceptance Criteria

The rebuttal is acceptable only if it:

- Names the disposition clearly.
- Confirms HN2.b LOCKED AND HN2.c BINDING as hard prerequisites for any
  Phase 2.B GC-018.
- Confirms the four input schemas are complete and independent.
- Confirms the tiered done-criterion table is consistent.
- Confirms the per-surface slice work order model is required.
- Confirms bulk migration is forbidden.
- Confirms the roadmap does NOT enumerate 46 surfaces.
- Does not authorize implementation by itself.
- Requires a later Phase 2.B-specific GC-018 (filed only after HN2.b LOCKED
  and HN2.c BINDING) before the migration plan artifact is produced.
- Names per-surface migration work orders as separate downstream work after
  Phase 2.B plan is LOCKED.

## Evidence Requirements

The rebuttal must cite:

- Phase 2.B roadmap (quoted where rebuttal refines).
- HN2.b roadmap (prerequisite linkage).
- HN2.c roadmap (prerequisite linkage).
- HN2.a inventory.
- At least 2 Phase 1.x adapter map files (verify 46-surface grounding).
- `GovernedCapability.availableFrom: 'Phase-2B'` placeholder location.
- GAP discovery memory direction (filed gap that this work answers).

If the rebuttal recommends continuation, it must list seed acceptance
criteria for the later Phase 2.B GC-018, including:

- migration plan artifact path under `docs/reference/`;
- four-input schema honored (order, owner, done, dependency);
- per-surface table covers all 46 surfaces (Phase 2.B GC-018's enumeration
  job);
- tiered done-criterion table;
- stage gate conditions;
- freeze release callouts for kernel-touching surfaces;
- citation rule for per-surface work orders;
- bulk migration prohibition.

## Review Gate

Stop and return `BLOCKING` if any of these are true:

- The roadmap enumerates the 46 surfaces (overreaches scope; that is
  Phase 2.B GC-018's job).
- The roadmap allows Phase 2.B GC-018 to file before HN2.b LOCKED.
- The roadmap allows kernel-touching adapter work order before HN2.c
  BINDING.
- The roadmap permits bulk migration.
- The roadmap introduces a new role taxonomy / engine / receipt / tier /
  method / phase / doctrine layer.
- The roadmap adds a kernel surface beyond HN2.a's 12.
- The roadmap lifts the freeze.
- The roadmap implies a code change at filing time.
- The roadmap plans Phase 2.C or later phases.

## Closure Checklist

- [ ] Rebuttal packet filed.
- [ ] Queue item status updated.
- [ ] State registry next move updated.
- [ ] Handoff updated if continuity needs it.
- [ ] JSON parse passes for changed registry files.
- [ ] `python governance/compat/check_active_session_state.py --enforce`
  passes.
- [ ] `python governance/compat/check_docs_governance_compat.py` passes.
- [ ] `python governance/compat/check_markdown_structural_completeness.py`
  passes.

## Return-To-Orchestrator Conditions

Return without filing a non-blocking rebuttal if:

- HN2.b or HN2.c prerequisite framing is missing or weakened;
- the four input schemas are incomplete or overlapping;
- the roadmap enumerates the 46 surfaces;
- the roadmap permits bulk migration;
- the roadmap implies a code change at filing time;
- the roadmap lifts the freeze;
- the roadmap plans phases beyond 2.B.

## Claim Boundary

This work order authorizes only a reviewer-role rebuttal. It does not
authorize implementation, GC-018 filing, migration plan artifact creation,
per-surface adapter authoring, doctrine modification, freeze lift, public
claims, kernel-coherence closure, or runtime-maturity closure.
