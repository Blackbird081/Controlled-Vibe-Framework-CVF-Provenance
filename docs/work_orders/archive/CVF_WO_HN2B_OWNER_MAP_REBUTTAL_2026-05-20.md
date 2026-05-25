# CVF Work Order — HN2.b Governance Kernel Owner Map Rebuttal

Memory class: SUMMARY_RECORD

Status: READY_FOR_REBUTTAL_EXECUTION

GC-018 required: No — reviewer rebuttal only. Any later implementation needs a
fresh HN2.b-specific GC-018 and a separate implementation work order that
produces the owner map artifact.

## Authority Chain

- Active session state:
  `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- Active review queue item: `hn2b-owner-map-roadmap`
- Target roadmap:
  `docs/roadmaps/CVF_HN2B_GOVERNANCE_KERNEL_OWNER_MAP_ROADMAP_2026-05-20.md`
- Predecessor inventory (CLOSED):
  `docs/reviews/CVF_HN2A_GOVERNANCE_KERNEL_OWNER_INVENTORY_2026-05-20.md`
- Original HN2 split direction:
  `docs/reviews/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_CLAUDE_REBUTTAL_2026-05-20.md`

## Agent Roles

- Operator: selected HN2.b as the kernel-hardening next move.
- Codex reviewer: performs the read-only HN2.b rebuttal and files the rebuttal
  packet.
- Orchestrator: may file a later GC-018 only if the rebuttal returns a
  non-blocking disposition.
- Worker: must not implement anything from this work order.

## Purpose

Produce the reviewer-role rebuttal for the HN2.b owner map roadmap.

The rebuttal must decide whether the roadmap may proceed to a slice-specific
GC-018 and implementation work order for producing the authoritative kernel
owner map artifact, while preserving the FROZEN doctrine/authority chain and
the closed classification set.

## Scope

Allowed scope:

- Read-only review of the HN2.b roadmap.
- Read-only review of HN2.a inventory and closure review.
- Read-only review of the 12 kernel surface evidence paths cited in HN2.a.
- Read-only review of the post-pain-point hardening rebuttal (HN2 split
  direction).
- Filing one rebuttal packet at:
  `docs/reviews/CVF_HN2B_GOVERNANCE_KERNEL_OWNER_MAP_CODEX_REBUTTAL_2026-05-20.md`
- Updating `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` and
  `CVF_SESSION/ACTIVE_SESSION_STATE.json` after the rebuttal is filed.
- Updating `AGENT_HANDOFF_V10_2026-05-19.md` only if needed for continuity.

Forbidden scope:

- No implementation of the owner map artifact.
- No GC-018 baseline for implementation.
- No new classification class beyond the 11 declared in the roadmap.
- No new kernel surface added beyond the 12 in HN2.a.
- No new role taxonomy, policy/risk/guard engine, receipt envelope, memory
  tier, method contract, or phase.
- No doctrine modification.
- No freeze posture lift.
- No public-sync or public claim update.
- No code/runtime/provider/memory/Maika changes.

## Required First Reads

1. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
2. `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
3. `docs/roadmaps/CVF_HN2B_GOVERNANCE_KERNEL_OWNER_MAP_ROADMAP_2026-05-20.md`
4. `docs/reviews/CVF_HN2A_GOVERNANCE_KERNEL_OWNER_INVENTORY_2026-05-20.md`
5. `docs/reviews/CVF_HN2A_GOVERNANCE_KERNEL_OWNER_INVENTORY_CLOSURE_REVIEW_2026-05-20.md`
6. `docs/reviews/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_CLAUDE_REBUTTAL_2026-05-20.md`
7. `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md`
8. `ECOSYSTEM/doctrine/CVF_DOCTRINE_RULES.md`
9. Sample owner-candidate sources from HN2.a (at least 3 of the 12 surfaces —
   reviewer's choice — to spot-check whether owner candidates resolve).

## Pre-Flight Checks

Before writing the rebuttal, Codex must verify:

- `hn2b-owner-map-roadmap` is `READY_FOR_REBUTTAL` in the queue.
- HN2.a inventory is CLOSED and lists 12 surfaces.
- The roadmap names all 12 HN2.a surfaces with per-surface decision sections.
- The roadmap declares a closed 11-class classification set.
- The roadmap forbids new role/engine/receipt/tier/method/phase.
- The roadmap defers HN2.c authoring (does not write freeze-release rule).
- The roadmap claims no freeze lift.

## Write Ownership

Codex reviewer may create:

- `docs/reviews/CVF_HN2B_GOVERNANCE_KERNEL_OWNER_MAP_CODEX_REBUTTAL_2026-05-20.md`

Codex reviewer may update:

- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V10_2026-05-19.md`

Codex reviewer must not modify:

- `docs/roadmaps/CVF_HN2B_GOVERNANCE_KERNEL_OWNER_MAP_ROADMAP_2026-05-20.md`
- `docs/reviews/CVF_HN2A_*` (closed inventory)
- Any code/runtime/provider/memory/Maika file.
- `ECOSYSTEM/doctrine/*`
- `governance/toolkit/05_OPERATION/*`
- Public-sync repo.

## Execution Plan

1. Confirm queue order and HN2.b scope.
2. Read the roadmap end-to-end.
3. Read HN2.a inventory and closure review.
4. Spot-check at least 3 surfaces by reading their owner-candidate source files.
5. Verify the 11-class classification set is closed and non-overlapping.
6. Verify per-surface decision sections cover all 12 surfaces.
7. Decide one of:
   - `NON_BLOCKING_WITH_SCOPE_REFINEMENT`
   - `NON_BLOCKING_WITH_EXISTING_EVIDENCE`
   - `BLOCKING`
8. File the rebuttal packet with findings, risks, required corrections, and
   explicit claim boundary.
9. Update active review queue/state/handoff routing.
10. Run JSON parse and active-session state checks.
11. Run docs governance and Markdown structural checks if new docs were filed.

## Tasks

- [ ] Confirm queue status for `hn2b-owner-map-roadmap`.
- [ ] Verify all 12 HN2.a surfaces appear in the roadmap with per-surface
  decision.
- [ ] Verify 11 classification classes are named, non-overlapping, and cover
  the alias space.
- [ ] Verify Guard model declares two parallel canonical owners (runtime +
  repository).
- [ ] Verify Delegation/handoff declares two adjacent surfaces, not one.
- [ ] Verify Receipt envelope keeps one canonical root with lane-receipts as
  `adapter_required`.
- [ ] Verify Memory tier model keeps audit-memory-receipt as capture observer
  (not a tier).
- [ ] Verify forbidden-expansion register names: no new role / engine /
  receipt / tier / method / phase.
- [ ] Verify HN2.c authoring is NOT done inside HN2.b.
- [ ] Verify Phase 2.B work is NOT done inside HN2.b.
- [ ] Spot-check 3 owner-candidate source files for resolvability.
- [ ] File rebuttal at
  `docs/reviews/CVF_HN2B_GOVERNANCE_KERNEL_OWNER_MAP_CODEX_REBUTTAL_2026-05-20.md`.
- [ ] Update active queue/state routing.
- [ ] Run required verification.

## Acceptance Criteria

The rebuttal is acceptable only if it:

- Names the disposition clearly.
- Confirms all 12 HN2.a surfaces are covered by the roadmap.
- Confirms the 11-class classification set is closed and unambiguous.
- States explicitly whether any surface's per-surface decision needs
  refinement before GC-018.
- Preserves FROZEN doctrine and `governance_kernel_freeze_recommended`
  posture.
- Does not authorize implementation by itself.
- Requires a later HN2.b-specific GC-018 before the owner map artifact is
  produced.
- Names HN2.c as separate downstream work that depends on HN2.b LOCKED.
- Names Phase 2.B as separate downstream work that depends on HN2.b LOCKED.

## Evidence Requirements

The rebuttal must cite:

- HN2.b roadmap (per-surface decision sections quoted where the rebuttal
  refines them).
- HN2.a inventory (verify each surface mapped).
- Post-pain-point hardening rebuttal HN2 finding (split direction).
- At least 3 owner-candidate source files spot-checked (path + symbol or
  line reference).
- Doctrine FROZEN reference.

If the rebuttal recommends continuation, it must list seed acceptance
criteria for the later HN2.b GC-018, including:

- owner map artifact path under `docs/reference/`;
- closed 11-class classification set;
- every HN2.a alias classified;
- forbidden-expansion register;
- citation rule for future work orders;
- change protocol (updates require fresh GC-018 with rebuttal).

## Review Gate

Stop and return `BLOCKING` if any of these are true:

- The roadmap introduces a new kernel surface beyond the 12.
- The roadmap introduces a new classification class beyond the declared 11.
- The roadmap introduces a new role taxonomy, engine, receipt envelope,
  tier, method, or phase.
- The roadmap rewrites doctrine vocabulary.
- The roadmap lifts the freeze posture.
- The roadmap bundles HN2.c rule-making or Phase 2.B migration work.
- The roadmap rewrites runtime contracts or imports any code change.

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

- HN2.a inventory cannot be reconciled with the roadmap's per-surface
  sections;
- the 11-class set has overlapping or missing classes for HN2.a aliases;
- the roadmap implies a code change at filing time;
- the roadmap implies a doctrine change;
- the roadmap implies a freeze lift;
- the roadmap bundles HN2.c or Phase 2.B work.

## Claim Boundary

This work order authorizes only a reviewer-role rebuttal. It does not
authorize implementation, GC-018 filing, owner map artifact creation,
doctrine modification, freeze lift, public claims, or kernel-coherence
closure.
