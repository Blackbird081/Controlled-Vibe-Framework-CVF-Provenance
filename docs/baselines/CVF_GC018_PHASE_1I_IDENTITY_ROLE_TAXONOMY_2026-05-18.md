# GC-018 Authorization — Phase 1.I Identity And Role Taxonomy

Memory class: SUMMARY_RECORD

Status: AUTHORIZED FOR LOCAL IMPLEMENTATION

Date: 2026-05-18

```text
GC-018 Continuation Candidate
- Candidate ID: CVF-17.05-PHASE-1I
- Date: 2026-05-18
- Parent roadmap / wave: .private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_REVIEW_CVF_FINAL_CONVERGED_REMEDIATION_ROADMAP_2026-05-17.md
- Proposed scope: Separate the four role axes (agent function, operator/team,
  auth/RBAC, governance actor) that are currently conflated across AgentRole,
  CVFRole, ActorRole, and operator role surfaces. Map each Phase 1.0 role
  surface to one axis. Plan adapter path before any runtime role migration.
- Continuation class: STRUCTURAL
- Active quality assessment: docs/reviews/CVF_17_05_STABILIZATION_DRIFT_INVENTORY_2026-05-17.md
- Assessment date: 2026-05-17
- Weighted total: 7.5/10 (Phase 1.0 inventory complete; axis separation absent
  is the primary gap addressed by this phase)
- Lowest dimension: Machine enforceability (1/2 — axis taxonomy lives at doc
  level until Phase 2.B runtime wire-up enforces it)
- Quality-first decision: EXPAND_NOW
- Why expansion is still the better move now: Phase 1.0 inventory found 20
  distinct AgentRole/ActorRole/CVFRole surfaces with no canonical axis map.
  The owner map (docs/reviews/CVF_17_05_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-17.md)
  confirms kernel surface #2 (Agent/actor roles) is partially_owned and a
  freeze_blocker. Defining role axes requires reading existing role strings,
  not changing them — active-path impact is zero until Phase 2.B.
- Quality protection commitments: (1) No role enum renamed or deleted.
  (2) No runtime role check changed. (3) Each axis is a classification
  layer only — existing strings remain valid until adapters migrate them.
  (4) Multi-tenant or organizational role scopes remain out of scope.
- Why now: Phase 1.0 gate passed. Owner map confirms CVF_CONTROL_PLANE_FOUNDATION
  has partial agent-function role coverage; RBAC axis lives in NextAuth
  (Owner/Admin/Developer/Reviewer/Viewer); governance actor axis is in
  CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL. The four axes can be named and
  mapped without kernel owner ambiguity.
- Active-path impact: NONE — axis taxonomy definition only; no runtime role
  check changed until Phase 2.B.
- Risk if deferred: Each new feature or absorption continues introducing role
  strings that mix function, auth, and governance concerns. Drift inventory
  grows. Phase 2.B wire-up must then reconcile conflated roles under
  time pressure.
- Lateral alternative considered: YES
- Why not lateral shift: Defining role axes inline during Phase 2.B wire-up
  would require runtime changes and axis definition simultaneously —
  higher risk than separating the taxonomy work now.
- Real decision boundary improved: YES — axis map enables Phase 1.I adapter
  plan and Phase 2.B role enforcement to reference typed axes rather than
  prose descriptions.
- Expected enforcement class: GOVERNANCE_DECISION_GATE (axis acceptance)
  → CI_REPO_GATE (role conformance tests, Phase 2.B)
- Required evidence if approved:
  - Four role axis definitions exist in canonical doc form
  - Each Phase 1.0 AgentRole/ActorRole/CVFRole surface (20 files) is
    classified into one primary axis
  - Adapter plan states how existing role strings migrate to typed axes
  - New canonical taxonomy avoids mixing agent function with RBAC permissions
  - Conformance test stubs exist for each axis boundary

Depth Audit
- Risk reduction: 2 (directly addresses kernel surface #2 freeze_blocker;
  axis conflation causes silent policy/auth errors at runtime)
- Decision value: 2 (axis map is required input for Phase 2.B role
  enforcement — without it the authority chain cannot close)
- Machine enforceability: 1 (axis is a classification doc; hard enforcement
  requires Phase 2.B typed interfaces)
- Operational efficiency: 1 (eliminates per-feature "which role type?"
  analysis; adapter plan sets migration order)
- Portfolio priority: 2 (Phase 1.I is listed alongside 1.P/1.R/1.M as
  first implementation wave in the converged roadmap)
- Total: 8/10
- Decision: CONTINUE
- Reason: Phase 1.0 gate passed, 20 role surfaces inventoried without axis,
  no existing runtime changed, axis taxonomy is safe structural expansion,
  Phase 2.B is gated on this output.

Authorization Boundary
- Authorized now: YES
- Next batch name: CVF-17.05-PHASE-1I implementation
- Permitted implementation:
  - Four role axis definitions (agent function / operator-team / auth-RBAC /
    governance actor) in canonical doc form
  - Classification of each Phase 1.0 role surface (20 files) to one primary axis
  - Adapter plan for role string migration
  - Conformance test stubs per axis boundary
  - legacy_reference marking for role surfaces that are starter templates only
- Not permitted:
  - Renaming or deleting any existing role enum or type
  - Runtime role check changes (Phase 2.B)
  - Multi-tenant or organizational role scopes
  - Changes to RBAC provider configuration (NextAuth)
  - Changes to public claims or release gates
```

## Purpose

Authorize Phase 1.I role axis taxonomy definition and adapter mapping for the
20 AgentRole/ActorRole/CVFRole surfaces identified in Phase 1.0. This packet
is the gating authorization record that must exist before any Phase 1.I
implementation work begins.

## Decision / Baseline / Proposed Tranche

- Decision: CONTINUE
- Candidate ID: CVF-17.05-PHASE-1I
- Depth Audit total: 8/10
- Authorized scope: four role axis definitions (agent function / operator-team /
  auth-RBAC / governance actor), classification of each Phase 1.0 role surface
  (20 files) to one primary axis, adapter plan for role string migration,
  conformance test stubs per axis boundary, legacy_reference marking for
  starter template role surfaces
- Not authorized: renaming or deleting any existing role enum or type, runtime
  role check changes, multi-tenant or organizational role scopes, RBAC provider
  configuration changes, changes to public claims or release gates

## Evidence / Required Evidence / Verification

Phase 1.0 gate evidence:
- Commit `daa97429` (2026-05-18) delivered all four required Phase 1.0
  extended scope artifacts
- Drift inventory: `docs/reviews/CVF_17_05_STABILIZATION_DRIFT_INVENTORY_2026-05-17.md`
  (20 AgentRole/ActorRole/CVFRole surfaces inventoried)
- Owner map: `docs/reviews/CVF_17_05_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-17.md`
  (kernel surface #2 agent/actor roles: partially_owned, freeze_blocker)
- Source matrix: `docs/reviews/CVF_17_05_UNABSORBED_KERNEL_SOURCE_MATRIX_2026-05-17.md`
  (Orchestrator authority model not_absorbed — role axis conflation confirmed)

Required evidence for Phase 1.I completion:
- Four role axis definitions exist in canonical doc form
- Each Phase 1.0 role surface (20 files) classified into one primary axis
- Adapter plan states how existing role strings migrate to typed axes
- New taxonomy avoids mixing agent function with RBAC permissions
- Conformance test stubs exist for each axis boundary

## Source Authorization

Parent roadmap phase definition:
```
Phase 1.I - Identity And Role Taxonomy
Opens only after Phase 1.0.
Scope: Separate role axes instead of forcing one role enum:
  - agent function axis;
  - operator/team axis;
  - auth/RBAC axis;
  - governance actor axis where needed.
Map existing AgentRole, CVFRole, operator roles, team roles, and auth
roles to one axis.
```

Phase 1.0 gate passed: commit `daa97429` (2026-05-18) delivered all four
required Phase 1.0 extended scope artifacts.

## Claim Boundary

This packet authorizes Phase 1.I role axis taxonomy definition and adapter
mapping only. It does not authorize runtime role changes, public claim changes,
or Phase 2 work.
