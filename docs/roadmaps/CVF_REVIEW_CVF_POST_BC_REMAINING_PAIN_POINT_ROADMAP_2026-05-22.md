# CVF Review-CVF Post-B/C Remaining Pain Point Roadmap

Memory class: FULL_RECORD

Status: ACTIVE_ROADMAP_PENDING_REBUTTAL_AND_OPERATOR_TRANCHE_SELECTION

docType: roadmap

Date: 2026-05-22

## Purpose

Define the next roadmap after Review CVF Problem B and Problem C were closed
at the certified-pack product-outcome runtime and package-level CLI gateway
baseline.

The roadmap keeps `.private_reference/legacy/CVF 17.05/Review CVF.md` as the
source oracle for original deliverable fit, but it does not treat that file as
implementation authorization. Each implementation tranche still requires a
fresh GC-018 baseline and any required blocked-work override.

## Authorization or Decision

Decision: file this roadmap as the active post-B/C steering candidate.

Authorization status:

- This document authorizes planning only.
- No implementation is authorized by this roadmap.
- Any next tranche requires operator selection, a candidate-specific GC-018,
  a work order, and normal governance checks.
- Roadmap rebuttal is recommended before dispatch because the sequence touches
  runtime actor identity, provider semantics, operational benchmarking, memory
  hierarchy, and product UX.

Predecessor assessment:

- `docs/reviews/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINTS_ASSESSMENT_2026-05-22.md`

Predecessor evidence:

- `docs/reviews/CVF_BC_PRODUCT_OUTCOME_RUNTIME_AND_CLI_DISTRIBUTION_COMPLETION_2026-05-22.md`
- `docs/audits/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_GAP_AUDIT_2026-05-22.md`
- `docs/roadmaps/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_V2_2026-05-22.md`

## Why This Tranche / Purpose

CVF has now moved B/C from "contract closed" to a real private-baseline
implementation: certified packs, packaged workflows, outcome runtime plans,
and package-level CLI gateway semantics exist.

The useful next work is not another broad audit of Review CVF.md. The useful
next work is a sequenced delivery program for the remaining original pain
points that are still real after B/C:

- G - execution identity runtime;
- D - provider gateway maturity;
- E - operational benchmark suite;
- H - memory hierarchy beyond the task-tier slice;
- F - noncoder outcome UX hardening;
- A - optional coherence equivalence audit only.

## Scope

In scope:

- sequence the remaining pain-point work after B/C;
- define each candidate tranche with acceptance criteria and claim boundary;
- preserve Review CVF.md as the deliverable-fit oracle;
- prevent closure-by-rejection, closure-by-redefinition, and contract-only
  closure for runtime tranches;
- keep blocked-work overrides explicit.

Out of scope:

- reopening B/C without new evidence of material nonfunctionality;
- public npm or global CLI distribution;
- public-sync update;
- hosted readiness or public deployment claim;
- Maika child-data/photo/vision proof;
- broad provider stability or all-provider parity claim;
- durable memory, organizational memory, or database persistence without a
  separate GC-018;
- freeze release, global freeze lift, or kernel-owner replacement.

## Non-Goals

- This roadmap is not a release plan.
- This roadmap is not a marketing plan.
- This roadmap does not invalidate prior bounded closure reviews.
- This roadmap does not authorize code changes.
- This roadmap does not claim all Review CVF.md pain points are now solved.

## Work Plan

### Sequencing Rule

Default sequence:

1. G1 - Execution Identity Runtime Minimum Viable Gate.
2. D2 - Provider Capability Matrix And Method Contract Hardening.
3. E2 - Operational Benchmark Suite.
4. H2 - Runtime Memory Hierarchy Phase 2.
5. F2 - Noncoder Outcome UX Hardening.
6. A2 - Coherence Equivalence Audit, only if requested or triggered.

Rationale:

- G comes first because actor identity controls authority, context scope, and
  receipt ownership for every later runtime path.
- D comes before E because benchmark fairness depends on explicit provider
  capability and unsupported-method behavior.
- E comes before larger H/F expansion because operational measurement should
  detect governance regressions created by runtime maturity work.
- H follows after actor identity to avoid memory scope drifting without actor
  ownership.
- F hardening follows after the runtime surfaces are less ambiguous.
- A remains audit-only because extra kernel-law docs risk duplicating existing
  guard-chain authority.

### G1 - Execution Identity Runtime Minimum Viable Gate

Original pain point: Problem G.

Objective:

Turn execution actor identity from reference/catalog language into a bounded
runtime gate that connects actor, authority, context scope, execution boundary,
and receipt ownership on the existing governed execution path.

Candidate deliverables:

- A runtime actor identity contract using existing CVF role vocabulary where
  possible.
- A policy resolver that maps an execution actor to allowed authority,
  permitted context scope, execution boundary, and receipt ownership.
- A pre-provider gate on `/api/execute` or the existing route owner that denies
  execution when actor identity does not satisfy the selected governed pack or
  outcome runtime plan.
- Receipt or audit readout that records the actor identity decision without
  changing the governance evidence receipt envelope unless separately
  authorized.
- Tests proving allowed, denied, and unknown actor cases.

Acceptance criteria:

- Denied actor path returns before provider dispatch.
- Allowed actor path preserves existing successful execution behavior.
- Audit payload exposes actor gate result.
- No new role taxonomy unless explicitly authorized.
- No background job queues, planner/worker orchestration, auth redesign, or
  public-sync change.

Blocked-work override:

- Required if the tranche introduces new role taxonomy or new governance
  actor semantics.
- Not required if the tranche stays within existing `CVFRole` values and
  existing governed-pack policy fields.

Claim boundary:

- Closes only the minimum viable runtime actor identity gate.
- Does not claim a full multi-agent operating system.

### D2 - Provider Capability Matrix And Method Contract Hardening

Original pain point: Problem D.

Objective:

Move provider abstraction from scattered method support into a machine-readable
capability matrix and deterministic unsupported-method behavior.

Candidate deliverables:

- Provider capability registry for the methods named by Review CVF.md:
  `complete`, `stream`, `tool_call`, `reasoning`, `json_mode`, `vision`,
  `embedding`, `receipt`, plus owner references for `retry`, `cost`, and
  `risk`.
- A single method-contract boundary that all provider adapters can be checked
  against.
- Negative gate behavior for methods a provider does not support.
- Live proof only for the methods explicitly selected by GC-018.

Acceptance criteria:

- Existing provider behavior remains compatible.
- Unsupported methods fail deterministically before ambiguous provider calls.
- At least one selected method has live proof if the tranche claims runtime
  behavior.
- Release-quality provider claims use the mandatory live release gate or a
  narrower live proof packet with raw keys redacted.

Blocked-work override:

- Required for any new provider execution semantics.

Claim boundary:

- Does not claim all-provider parity unless every provider/method pair has
  evidence.
- `retry`, `cost`, and `risk` remain at their existing owner surfaces unless a
  separate roadmap changes ownership.

### E2 - Operational Benchmark Suite

Original pain point: Problem E.

Objective:

Create a first-class benchmark suite for CVF governance reliability rather
than raw provider output quality.

Candidate deliverables:

- A benchmark schema for the Review CVF.md operational metrics:
  task completion rate, retry count, policy violation rate, human correction
  count, cross-session continuity, long-horizon stability, receipt integrity,
  deterministic consistency, and rollback success.
- A runner that can ingest existing evidence receipts and live gate outputs.
- A report format that separates live, offline, and fixture-backed metrics.
- Clear treatment of hallucination recovery: either implemented with a
  bounded definition or explicitly deferred with a named replacement metric.

Acceptance criteria:

- Benchmark reports distinguish provider failure from governance failure.
- Receipt integrity and policy-violation metrics are computed from evidence,
  not prose.
- Live-condition metrics identify their provider lane, model, and evidence
  mode.
- No claim of broad reliability unless sample size and provider lanes support
  it.

Blocked-work override:

- Required only if new policy/risk guard semantics are added.

Claim boundary:

- Closes operational benchmark foundation, not all future longitudinal
  measurement.

### H2 - Runtime Memory Hierarchy Phase 2

Original pain point: Problem H.

Objective:

Extend beyond T5's ephemeral task-memory slice only after actor identity and
benchmarking are in place.

Candidate deliverables:

- A memory hierarchy runtime map for working, task, skill, audit, receipt, and
  long-term memory tiers.
- Injection, retrieval, privacy, and contamination-boundary rules per tier.
- Runtime proof for one additional tier only, selected by operator demand.
- Audit readout preserving `canReinject=false` unless a separate reinjection
  tranche is authorized.

Acceptance criteria:

- Tier access is actor-aware after G1.
- No durable persistence unless separately authorized.
- No cross-session reinjection unless separately authorized.
- Rejected memory actions produce deterministic reasons.

Blocked-work override:

- Required for any memory tier beyond the already authorized ephemeral
  task-memory slice.

Claim boundary:

- Does not claim organizational memory, durable long-term memory, or automatic
  reinjection unless those are explicitly delivered and proven.

### F2 - Noncoder Outcome UX Hardening

Original pain point: Problem F.

Objective:

Harden the outcome-first surface now that six outcomes, workflow composition,
certified packs, and CLI runtime plans exist.

Candidate deliverables:

- First-screen outcome-first layout review against the six named outcomes.
- Reduced governance jargon on noncoder entry surfaces.
- Usage-driven bug list from manual and automated journeys.
- Copy/export/receipt affordance checks for the six outcomes.

Acceptance criteria:

- Noncoder first screen shows outcomes before skills and governance controls.
- All six named outcomes remain reachable.
- Existing governance evidence remains visible but not dominant.
- At least one browser proof covers a full outcome journey.

Blocked-work override:

- Not required if this remains UI hardening over existing routes and outcomes.
- Required if it adds new routes, auth/RBAC changes, or new template
  categories.

Claim boundary:

- Closes noncoder UX hardening for the six named outcomes, not all future
  noncoder workflows.

### A2 - Coherence Equivalence Audit

Original pain point: Problem A.

Objective:

Audit whether existing guard-chain and owner-map artifacts are equivalent to
the original requested freeze artifacts.

Candidate deliverables:

- A five-point equivalence table for authority hierarchy, execution lifecycle,
  governance ownership, policy scope, and runtime semantics.
- A no-new-docs recommendation if equivalence is sufficient.
- A narrow gap list if equivalence is not sufficient.

Acceptance criteria:

- No new kernel-law docs are created unless the audit proves a concrete gap.
- The audit names the existing owner surface for each freeze point.

Blocked-work override:

- Required if the audit proposes new governance semantics.

Claim boundary:

- Audit-only unless separately authorized.

## Acceptance Criteria

The roadmap is acceptable when:

- the post-B/C assessment is filed;
- B/C remains closed and is not reopened by roadmap wording;
- G, D, E, H, F, and A are sequenced with clear boundaries;
- every candidate names its blocked-work override condition;
- implementation remains blocked until operator selection and fresh GC-018;
- Review CVF.md remains the deliverable-fit oracle.

## Verification or Evidence

Planning verification:

- source assessment filed at
  `docs/reviews/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINTS_ASSESSMENT_2026-05-22.md`;
- B/C closure evidence retained at
  `docs/reviews/CVF_BC_PRODUCT_OUTCOME_RUNTIME_AND_CLI_DISTRIBUTION_COMPLETION_2026-05-22.md`;
- active session state must point to this roadmap before future agents treat it
  as current steering material.

Future implementation verification:

- each tranche must define targeted tests before coding;
- runtime/governance claims must use live proof when they assert provider,
  receipt, policy, routing, or execution behavior;
- docs-only or UI-only checks must not be used to claim live governance
  behavior.

## Claim Boundary

This roadmap is a planning and steering artifact only. It does not authorize
implementation, does not claim any remaining pain point is closed, does not
change public claims, does not update public-sync, does not release frozen
surfaces, and does not alter provider, route, receipt, actor, or memory
runtime behavior.
