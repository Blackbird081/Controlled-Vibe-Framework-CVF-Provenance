# GC-018 Authorization — Phase 2.A Contract Sketch

Memory class: SUMMARY_RECORD

Status: AUTHORIZED FOR LOCAL IMPLEMENTATION

Date: 2026-05-18

```text
GC-018 Continuation Candidate
- Candidate ID: CVF-17.05-PHASE-2A
- Date: 2026-05-18
- Parent roadmap / wave: .private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_REVIEW_CVF_FINAL_CONVERGED_REMEDIATION_ROADMAP_2026-05-17.md
- Proposed scope: Define provisional GovernedCapability and OutcomeWorkflow
  contracts. Bind both to placeholder canonical owners identified by Phase 1.0.
  Make the missing capability chain explicit in doc form. No web execute route
  integration. No runtime behavior change.
- Continuation class: STRUCTURAL
- Active quality assessment: docs/reviews/CVF_17_05_STABILIZATION_DRIFT_INVENTORY_2026-05-17.md
- Assessment date: 2026-05-17
- Weighted total: 7.5/10 (Phase 1.0 inventory complete; GovernedCapability and
  OutcomeWorkflow contract homes absent is the primary gap)
- Lowest dimension: Machine enforceability (1/2 — contract sketch exists at
  doc/type level only until Phase 2.B runtime wire-up)
- Quality-first decision: EXPAND_NOW
- Why expansion is still the better move now: Phase 1.0 inventory confirmed
  that OutcomeWorkflow has zero active implementation match across EXTENSIONS,
  governance, and docs. GovernedCapability as a composition of certified skill
  refs + policy + runtime + validation + receipt is also absent as a typed
  contract. skill.meta.json is already present (CVF_v1.2.1_EXTERNAL_INTEGRATION)
  confirming the partial productization baseline. Defining the contract sketch
  requires no mutation of existing paths — it creates the missing top-level
  composition contract.
- Quality protection commitments: (1) No existing skill, policy, or runtime
  surface renamed or deleted. (2) No web execute route changed. (3) Existing
  partial productization wording preserved in the contract sketch. (4) The
  sketch is explicitly marked provisional and not a runtime claim. (5) Phase
  2.B runtime wire-up and Phase 2.C vertical slice remain blocked until the
  relevant Phase 1 owners (1.P, 1.I, 1.R) are complete.
- Why now: Roadmap explicitly permits Phase 2.A after Phase 1.0, independent
  of Phase 1.P/1.I/1.R completion. The contract sketch's placeholder canonical
  owners reference Phase 1.0 inventory findings — exactly what is now available.
- Active-path impact: NONE — provisional contract definition only; no execution
  path changed, no web route integration, no runtime behavior change.
- Risk if deferred: The capability chain
  (outcome -> workflow -> capability refs -> policy -> runtime -> validation ->
  receipt -> deliverable) remains implicit prose. Phase 2.B and Phase 2.C must
  then define the contract under time pressure while also wiring runtime.
- Lateral alternative considered: YES
- Why not lateral shift: Defining GovernedCapability and OutcomeWorkflow inline
  during Phase 2.B would couple contract definition with runtime integration —
  two distinct risks that are safer to separate.
- Real decision boundary improved: YES — contract sketch makes the missing
  chain explicit and gives Phase 2.B a typed target rather than prose
  description. skill.meta.json is acknowledged as already present; the
  sketch closes the gap from metadata to full product workflow composition.
- Expected enforcement class: GOVERNANCE_DECISION_GATE (contract acceptance)
  → CI_REPO_GATE (capability chain integration tests, Phase 2.B)
- Required evidence if approved:
  - Provisional GovernedCapability contract specified (TypeScript interface
    or Python abstract class)
  - Provisional OutcomeWorkflow contract specified
  - Both contracts bound to placeholder canonical owners from Phase 1.0
    owner map
  - Missing chain made explicit:
    outcome -> workflow -> capability refs -> policy -> runtime ->
    validation -> receipt -> deliverable
  - Existing partial productization preserved in wording
  - skill.meta.json acknowledged as the existing capability metadata baseline
  - Contracts explicitly marked provisional; runtime wire-up deferred to 2.B

Depth Audit
- Risk reduction: 2 (makes the capability chain gap explicit and bounded;
  without this sketch Phase 2.B must discover and define the gap simultaneously
  with runtime integration)
- Decision value: 2 (contract sketch is the required typed target for Phase
  2.B wire-up and Phase 2.C vertical slice — deferring blocks both)
- Machine enforceability: 1 (provisional contract is a type definition;
  runtime enforcement requires Phase 2.B)
- Operational efficiency: 1 (eliminates per-feature "how does a governed
  capability compose?" analysis; placeholder owners reference canonical homes
  already confirmed by Phase 1.0)
- Portfolio priority: 2 (Phase 2.A is explicitly listed as permitted after
  Phase 1.0 in the roadmap authorization sequence, independently of 1.P/1.I/1.R)
- Total: 8/10
- Decision: CONTINUE
- Reason: Phase 1.0 gate passed, OutcomeWorkflow has zero active runtime
  implementation, GovernedCapability composition is absent as typed contract,
  sketch is zero active-path risk, Phase 2.B and 2.C are gated on this output.

Authorization Boundary
- Authorized now: YES
- Next batch name: CVF-17.05-PHASE-2A implementation
- Permitted implementation:
  - Provisional GovernedCapability contract (type definition only)
  - Provisional OutcomeWorkflow contract (type definition only)
  - Placeholder canonical owner bindings from Phase 1.0 owner map
  - Explicit documentation of the outcome -> deliverable chain
  - Acknowledgment of skill.meta.json as existing capability metadata baseline
  - Provisional marking on all 2.A contracts
- Not permitted:
  - Web execute route integration
  - Runtime behavior changes (Phase 2.B)
  - Certified capability enforcement at runtime (Phase 2.B)
  - Noncoder vertical slice (Phase 2.C)
  - Changes to public claims or release gates
  - Any work that requires Phase 1.P/1.I/1.R completion before Phase 2.A
    is authorized (placeholder owners suffice for the sketch)
```

## Purpose

Authorize Phase 2.A provisional contract definition for GovernedCapability and
OutcomeWorkflow, making the missing capability chain explicit without touching
any runtime path. This packet is the gating authorization record that must
exist before any Phase 2.A implementation work begins.

## Decision / Baseline / Proposed Tranche

- Decision: CONTINUE
- Candidate ID: CVF-17.05-PHASE-2A
- Depth Audit total: 8/10
- Authorized scope: provisional GovernedCapability contract (type definition
  only), provisional OutcomeWorkflow contract (type definition only), placeholder
  canonical owner bindings from Phase 1.0 owner map, explicit documentation of
  the outcome→deliverable chain, acknowledgment of skill.meta.json as existing
  capability metadata baseline, provisional marking on all 2.A contracts
- Not authorized: web execute route integration, runtime behavior changes,
  certified capability enforcement at runtime, noncoder vertical slice,
  changes to public claims or release gates

## Evidence / Required Evidence / Verification

Phase 1.0 gate evidence:
- Commit `daa97429` (2026-05-18) delivered all four required Phase 1.0
  extended scope artifacts
- Drift inventory: `docs/reviews/CVF_17_05_STABILIZATION_DRIFT_INVENTORY_2026-05-17.md`
  (OutcomeWorkflow: zero active matches confirmed)
- Owner map: `docs/reviews/CVF_17_05_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-17.md`
  (placeholder owners available for Phase 2.A contract bindings)
- Source matrix: `docs/reviews/CVF_17_05_UNABSORBED_KERNEL_SOURCE_MATRIX_2026-05-17.md`
  (Problem B — skill system not yet product capability system: not_absorbed)
- Roadmap authorization sequence: Phase 2.A explicitly permitted after Phase 1.0,
  independent of Phase 1.P/1.I/1.R completion

Required evidence for Phase 2.A completion:
- Provisional GovernedCapability contract specified
- Provisional OutcomeWorkflow contract specified
- Both contracts bound to placeholder canonical owners from Phase 1.0 owner map
- Missing chain documented: outcome → workflow → capability refs → policy →
  runtime → validation → receipt → deliverable
- skill.meta.json acknowledged as existing capability metadata baseline
- All contracts explicitly marked provisional; runtime wire-up deferred to 2.B

## Source Authorization

Parent roadmap phase definition:
```
Phase 2.A - Contract Sketch
Can begin after Phase 1.0.
Scope: Define provisional GovernedCapability. Define provisional
OutcomeWorkflow. Bind both to placeholder canonical owners identified by
Phase 1.0. No web execute route integration. No runtime behavior change.
```

Phase 1.0 gate passed: commit `daa97429` (2026-05-18) delivered all four
required Phase 1.0 extended scope artifacts.

## Claim Boundary

This packet authorizes Phase 2.A provisional contract definition only. It does
not authorize runtime wire-up, vertical slice, public claim changes, or Phase
2.B/2.C work. Phase 2.B remains blocked until Phase 1.P, 1.I, and 1.R owners
are complete.
