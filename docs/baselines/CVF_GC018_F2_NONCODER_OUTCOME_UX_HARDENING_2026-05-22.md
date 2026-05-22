# CVF GC-018 F2 Noncoder Outcome UX Hardening

Memory class: SUMMARY_RECORD

Status: AUTHORIZED_F2_NONCODER_OUTCOME_UX_HARDENING

Date: 2026-05-22

## Source or Predecessor Evidence

- `.private_reference/legacy/CVF 17.05/Review CVF.md`
- `docs/reviews/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINTS_ASSESSMENT_2026-05-22.md`
- `docs/roadmaps/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINT_ROADMAP_2026-05-22.md`
- `docs/reviews/CVF_H2_RUNTIME_MEMORY_HIERARCHY_PHASE2_COMPLETION_2026-05-22.md`
- `DESIGN.md`

## Purpose / Decision / Baseline

Authorize F2, the noncoder outcome UX hardening phase after G1, D2, E2, and
H2 closure.

Decision: proceed with bounded UI hardening over existing home/outcome routes
and existing certified outcome workflows. Do not add new routes, template
categories, auth/RBAC behavior, provider behavior, or governance semantics.

## Decision / Baseline / Proposed Tranche

Baseline:

- B/C closed the product outcome runtime and CLI distribution baseline.
- Home already had six `OutcomeQuickActions`, but they were below hero/setup
  surfaces and the first-screen framing still led with templates.

Gap: Review CVF.md expects noncoders to see outcomes before skills, templates,
and governance machinery. F2 should make that visible on first screen and
verify at least one outcome journey.

Proposed tranche:

- move six outcomes to the top of the home browse surface;
- change first-screen copy from template-first to outcome-first;
- keep governance evidence visible but secondary;
- verify all six outcomes remain reachable;
- verify one browser outcome journey opens an existing workflow form.

## Scope / Proposed Tranche

In scope:

- `OutcomeQuickActions` presentation and copy;
- home page first-screen ordering and topbar copy;
- generic DynamicForm helper copy that currently overfits to websites;
- focused component/unit proof;
- browser mock proof for outcome-first ordering and one outcome workflow form.

Out of scope:

- new template categories or outcome definitions;
- new routes, auth/RBAC, provider calls, receipt envelopes, governance
  semantics, or live governance claims;
- public-sync, hosted readiness, Maika proof, freeze release, or public
  marketing update.

## Blocked-Work Override

Blocked-work override: not required.

Reason: F2 is UI hardening over existing routes, existing six outcomes,
existing certified packs, and existing workflow/form surfaces.

## Evidence / Required Evidence / Verification

Required evidence:

- focused `OutcomeQuickActions` tests pass;
- cvf-web TypeScript check passes;
- browser proof confirms outcome-first ordering and one outcome journey.

Live provider proof:

- Not required because F2 makes no live governance behavior claim. Browser mock
  proof is sufficient for UI ordering and existing form reachability.

## Claim Boundary / Approval Gate

F2 closes noncoder outcome UX hardening for the six current outcomes only. It
does not claim all future noncoder workflows are complete, does not prove live
provider execution, and does not update public-facing CVF claims.
