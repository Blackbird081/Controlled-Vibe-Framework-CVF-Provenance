# CVF Work Order — HN2.c Freeze-Release Rule Rebuttal

Memory class: SUMMARY_RECORD

Status: READY_FOR_REBUTTAL_EXECUTION

GC-018 required: No — reviewer rebuttal only. Any later implementation needs a
fresh HN2.c-specific GC-018 (filed only after HN2.b LOCKED) and a separate
implementation work order that produces the freeze-release rule artifact.

## Authority Chain

- Active session state:
  `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- Active review queue item: `hn2c-freeze-release-rule-roadmap`
- Target roadmap:
  `docs/roadmaps/CVF_HN2C_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE_ROADMAP_2026-05-20.md`
- Prerequisite roadmap (parallel filing):
  `docs/roadmaps/CVF_HN2B_GOVERNANCE_KERNEL_OWNER_MAP_ROADMAP_2026-05-20.md`
- Original HN2 split direction:
  `docs/reviews/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_CLAUDE_REBUTTAL_2026-05-20.md`

## Agent Roles

- Operator: selected HN2.c as next kernel-hardening move (parallel rebuttal
  with HN2.b).
- Codex reviewer: performs the read-only HN2.c rebuttal and files the rebuttal
  packet.
- Orchestrator: may file a later HN2.c GC-018 only after HN2.b is LOCKED AND
  this rebuttal returns non-blocking.
- Worker: must not implement anything from this work order.

## Purpose

Produce the reviewer-role rebuttal for the HN2.c freeze-release rule roadmap.

The rebuttal must decide whether the roadmap may proceed (after HN2.b LOCKED)
to a slice-specific GC-018 and implementation work order for producing the
binding freeze-release rule artifact, while preserving doctrine supremacy,
the existing freeze posture, and the prohibition on global lift.

## Scope

Allowed scope:

- Read-only review of the HN2.c roadmap.
- Read-only review of HN2.b roadmap (to verify HN2.c's dependency framing is
  honest).
- Read-only review of HN2.a inventory.
- Read-only review of the post-pain-point hardening rebuttal (HN2 split
  direction).
- Read-only review of doctrine and current freeze posture in active state.
- Filing one rebuttal packet at:
  `docs/reviews/CVF_HN2C_FREEZE_RELEASE_RULE_CODEX_REBUTTAL_2026-05-20.md`
- Updating `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` and
  `CVF_SESSION/ACTIVE_SESSION_STATE.json` after the rebuttal is filed.
- Updating `AGENT_HANDOFF_V10_2026-05-19.md` only if needed for continuity.

Forbidden scope:

- No implementation of the freeze-release rule artifact.
- No GC-018 baseline for implementation.
- No lifting of the existing freeze posture.
- No release of any kernel surface.
- No new doctrine layer above
  `ECOSYSTEM/doctrine/CVF_DOCTRINE_RULES.md`.
- No new schema field on `freezePosture`.
- No mechanical enforcement guard authored inside HN2.c.
- No new role taxonomy, policy/risk/guard engine, receipt envelope, memory
  tier, method contract, or phase.
- No public-sync or public claim update.
- No code/runtime/provider/memory/Maika changes.

## Required First Reads

1. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
2. `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
3. `docs/roadmaps/CVF_HN2C_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE_ROADMAP_2026-05-20.md`
4. `docs/roadmaps/CVF_HN2B_GOVERNANCE_KERNEL_OWNER_MAP_ROADMAP_2026-05-20.md`
5. `docs/reviews/CVF_HN2A_GOVERNANCE_KERNEL_OWNER_INVENTORY_2026-05-20.md`
6. `docs/reviews/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_CLAUDE_REBUTTAL_2026-05-20.md`
7. `ECOSYSTEM/doctrine/CVF_DOCTRINE_RULES.md`
8. `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_GOVERNANCE_KERNEL_FREEZE_CODEX_RECOMMENDATION_2026-05-17.md`
9. `governance/toolkit/05_OPERATION/` (sample existing guard files to verify
   the target artifact location convention).

## Pre-Flight Checks

Before writing the rebuttal, Codex must verify:

- `hn2c-freeze-release-rule-roadmap` is `READY_FOR_REBUTTAL` in the queue.
- The roadmap declares HN2.b LOCKED as a hard prerequisite for HN2.c GC-018.
- The roadmap names exactly four questions (what is frozen, what frozen
  means, what lifts, who lifts).
- The roadmap declares a closed change-class table mapping BLOCKED ↔
  rebuttal-action.
- The roadmap declares 5 release conditions.
- The roadmap declares a 4-role authority chain (doctrine → operator →
  reviewer → proposer).
- The roadmap prohibits global lift (per-surface only).
- The roadmap defers mechanical enforcement guard to a separate follow-on.
- The roadmap does NOT itself lift the freeze.

## Write Ownership

Codex reviewer may create:

- `docs/reviews/CVF_HN2C_FREEZE_RELEASE_RULE_CODEX_REBUTTAL_2026-05-20.md`

Codex reviewer may update:

- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V10_2026-05-19.md`

Codex reviewer must not modify:

- `docs/roadmaps/CVF_HN2C_*` (target roadmap)
- `docs/roadmaps/CVF_HN2B_*` (sibling prerequisite roadmap)
- `docs/reviews/CVF_HN2A_*` (closed inventory)
- `ECOSYSTEM/doctrine/*`
- `governance/toolkit/05_OPERATION/*`
- Any code/runtime/provider/memory/Maika file.
- Public-sync repo.

## Execution Plan

1. Confirm queue order and HN2.c scope.
2. Read the HN2.c roadmap end-to-end.
3. Read HN2.b roadmap to verify HN2.c's prerequisite framing is consistent.
4. Read HN2.a inventory and doctrine FROZEN reference.
5. Read at least 2 existing files in `governance/toolkit/05_OPERATION/` to
   confirm artifact-location convention is honored by the target path
   `governance/toolkit/05_OPERATION/CVF_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE.md`.
6. Verify all four questions (Q1–Q4) have explicit rule drafts.
7. Verify the closed change-class table is consistent (no overlapping or
   ambiguous rows).
8. Verify the 5 release conditions are independent and verifiable.
9. Verify the 4-role authority chain is non-circular and includes doctrine
   supremacy.
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

- [ ] Confirm queue status for `hn2c-freeze-release-rule-roadmap`.
- [ ] Verify roadmap names HN2.b LOCKED as hard prerequisite for HN2.c GC-018.
- [ ] Verify the four questions Q1–Q4 each have rule drafts.
- [ ] Verify the closed change-class table maps BLOCKED ↔ rebuttal-action.
- [ ] Verify the 5 release conditions are explicit and independent.
- [ ] Verify the 4-role authority chain names doctrine supremacy.
- [ ] Verify global lift is explicitly prohibited.
- [ ] Verify mechanical enforcement guard is deferred to separate follow-on.
- [ ] Verify HN2.c does NOT lift the freeze on filing.
- [ ] Verify target artifact path is under
  `governance/toolkit/05_OPERATION/`.
- [ ] File rebuttal at
  `docs/reviews/CVF_HN2C_FREEZE_RELEASE_RULE_CODEX_REBUTTAL_2026-05-20.md`.
- [ ] Update active queue/state routing.
- [ ] Run required verification.

## Acceptance Criteria

The rebuttal is acceptable only if it:

- Names the disposition clearly.
- Confirms HN2.b LOCKED as hard prerequisite for any HN2.c GC-018.
- Confirms Q1–Q4 rule drafts cover scope, frozen-meaning, release
  conditions, and authority chain.
- Confirms the closed change-class table is non-overlapping.
- Confirms global lift prohibition.
- Confirms doctrine supremacy clause.
- Does not authorize implementation by itself.
- Requires a later HN2.c-specific GC-018 (filed only after HN2.b LOCKED)
  before the rule artifact is produced.
- Names the mechanical enforcement guard as a separate downstream follow-on,
  not part of HN2.c.

## Evidence Requirements

The rebuttal must cite:

- HN2.c roadmap (quoted where rebuttal refines).
- HN2.b roadmap (prerequisite linkage).
- HN2.a inventory.
- Post-pain-point hardening rebuttal HN2 finding.
- Doctrine reference (supremacy).
- Active state freeze posture field.
- At least 2 sample files in `governance/toolkit/05_OPERATION/` (artifact
  location convention).

If the rebuttal recommends continuation, it must list seed acceptance
criteria for the later HN2.c GC-018, including:

- target artifact path under `governance/toolkit/05_OPERATION/`;
- closed change-class table reproduced in the artifact;
- 5 release conditions reproduced;
- 4-role authority chain reproduced;
- doctrine supremacy clause present;
- global lift prohibition present;
- per-surface release recording requirement (GC-018 baseline + owner map
  update + active state freeze field update with text-only semantic change);
- mechanical enforcement guard deferred to a separate follow-on GC-018.

## Review Gate

Stop and return `BLOCKING` if any of these are true:

- The roadmap lifts the existing freeze posture.
- The roadmap permits global lift.
- The roadmap introduces a new doctrine layer or contradicts doctrine.
- The roadmap allows the proposer to self-approve a release.
- The roadmap introduces a new schema field on `freezePosture` (or any
  other schema).
- The roadmap authors the mechanical enforcement guard inside HN2.c.
- The roadmap bundles HN2.b owner map authoring inside HN2.c.
- The roadmap allows HN2.c GC-018 to file before HN2.b is LOCKED.
- The roadmap implies a code change at filing time.

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

- HN2.b prerequisite framing is missing or weakened;
- the closed change-class table has overlapping rows;
- doctrine supremacy clause is absent or weakened;
- global lift is allowed;
- proposer self-approval is allowed;
- the roadmap lifts the freeze on filing;
- the roadmap bundles HN2.b or Phase 2.B work.

## Claim Boundary

This work order authorizes only a reviewer-role rebuttal. It does not
authorize implementation, GC-018 filing, freeze-release rule creation,
doctrine modification, freeze lift, mechanical enforcement guard authoring,
public claims, or kernel-coherence closure.
