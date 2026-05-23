# CVF 17.05 Phase 2.C Vertical Slice Preflight - 2026-05-18

Memory class: FULL_RECORD

Status: PHASE 2.C PREFLIGHT - SUPERSEDED BY BOUNDED COMPLETION

## Purpose

Evaluate whether Phase 2.C "Create Product Brief" vertical slice can proceed
immediately after bounded Phase 2.B, without silently expanding into unresolved
web runtime, noncoder UX, live-provider, ORCHESTRATOR, role-permission, or
legacy absorption scope.

## Scope / Target / Owner Boundary

Target: Phase 2.C vertical slice from the 17.05 converged roadmap.

Owner: CVF session-continuity and noncoder runtime governance surfaces.

In scope:

- Phase 2.C readiness assessment;
- candidate vertical slice selection;
- blocker list before GC-018;
- live governance proof requirement;
- relationship to deferred legacy GAPs.

Out of scope:

- implementing web route or UI changes;
- changing `/api/execute`;
- live provider proof execution;
- adding public claims;
- absorbing ORCHESTRATOR or role catalog permissions.

## Target / Source Under Review

Sources checked:

- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_REVIEW_CVF_FINAL_CONVERGED_REMEDIATION_ROADMAP_2026-05-17.md`
- `docs/reviews/CVF_17_05_PHASE_2B_BOUNDED_WIREUP_COMPLETION_2026-05-18.md`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/phase2b-wireup.contract.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/deliverable-pack.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/`
- `.private_reference/legacy/CVF Edit/Review CVF_1.md`
- `.private_reference/legacy/CVF Edit/De_xuat.md`

## Scope / Methodology

Method:

1. Compare Phase 2.C acceptance criteria with delivered Phase 2.B output.
2. Identify whether an existing noncoder route can host "Create Product Brief"
   without broad runtime changes.
3. Identify live proof requirements before any public claim.
4. Classify blockers as implementation blockers or claim blockers.

## Findings / Position

Phase 2.C should not be implemented in the same batch as bounded Phase 2.B.

Reason: Phase 2.C crosses from local contract proof into product runtime:
noncoder trigger, web `/api/execute`, deliverable pack generation, receipt
visibility, and live governance proof. That is a materially wider scope than
the Phase 2.B fixture path and needs its own GC-018 plus a precise slice plan.

Addendum 2026-05-18: the required fresh GC-018 was filed in
`docs/baselines/CVF_GC018_PHASE_2C_CREATE_PRODUCT_BRIEF_VERTICAL_SLICE_2026-05-18.md`.
The bounded `Create Product Brief` slice was implemented and live-proven in
`docs/reviews/CVF_17_05_PHASE_2C_VERTICAL_SLICE_COMPLETION_2026-05-18.md`.

## Candidate Slice

Recommended candidate remains:

`Create Product Brief`

Minimum acceptable slice:

1. Noncoder trigger path is named and feature-flag posture is explicit.
2. Workflow references a certified/bounded capability ref.
3. Policy/risk/guard check uses canonical or adapter path.
4. Output validation produces a structured result.
5. Deliverable pack is generated.
6. Receipt envelope captures trace.
7. Live governance proof runs before any public claim.

## Blockers Before GC-018

| Blocker | Why it blocks Phase 2.C | Disposition |
|---|---|---|
| Web/runtime scope selection | `/api/execute` is broad and already carries many governance behaviors | Needs a named, minimal path |
| Live provider proof | Public/noncoder governance behavior must use real provider API calls | Required before claim, not optional |
| Legacy role permissions | Role catalog `allowed_outputs` / `default_permissions` are not absorbed | Must be out of scope or separately authorized |
| ORCHESTRATOR semantics | Vertical slice must not imply scheduler/orchestrator maturity | Must be out of scope or separately authorized |
| Output validation contract | Phase 2.B validates contract chain, not product output structure | Needs specific validation criterion |
| Evidence receipt compatibility | Phase 2.B receipt is local `Receipt<OutcomeDeliverable>`; web receipt shape differs | Needs adapter plan |

## Risk / Corrective Action

Risk:

- Implementing Phase 2.C immediately would turn a local contract proof into
  product runtime modification without a fresh authorization boundary.

Corrective action:

- Open a separate Phase 2.C GC-018 only after selecting the exact noncoder
  trigger path and receipt adapter plan.
- Load operator-supplied live keys from
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.env.local` for proof commands
  without printing values.
- Keep ORCHESTRATOR and role catalog permissions deferred unless the Phase 2.C
  packet explicitly authorizes them.

## Decision / Recommendation / Disposition

Decision: This preflight block is resolved for the bounded `Create Product
Brief` implementation.

Recommendation: do not widen beyond the completed slice without fresh GC-018.

Disposition: `phase_2c_bounded_slice_complete`.

## Claim Boundary

This preflight does not authorize Phase 2.C implementation, does not modify web
runtime, does not make a public claim, does not run live provider proof, and
does not lift `system_reconvergence_stop`.
