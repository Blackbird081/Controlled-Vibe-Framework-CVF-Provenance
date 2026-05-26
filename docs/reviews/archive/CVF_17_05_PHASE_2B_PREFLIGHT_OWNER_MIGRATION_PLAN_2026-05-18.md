# CVF 17.05 Phase 2.B Preflight Owner And Migration Plan - 2026-05-18

Memory class: FULL_RECORD

Status: PHASE 2.B PREFLIGHT REVIEW. Runtime wire-up is NOT authorized by this
artifact.

## Purpose

Prepare the next roadmap move after the delivered 17.05 sequence by defining
the owner confirmations, migration order, done criteria, and legacy-audit gates
required before a Phase 2.B GC-018 packet can authorize runtime wire-up.

## Scope / Target / Owner Boundary

Target: Phase 2.B "Runtime Wire-Up" from the final 17.05 converged roadmap.

Owner: CVF session-continuity and governance-kernel reconvergence surface.

In scope:

- Phase 2.B preflight only;
- owner confirmation checklist for Phase 1.P / 1.I / 1.R dependencies;
- migration order for a bounded runtime path;
- done criteria required before runtime implementation;
- legacy absorption audit gate before GC-018.

Out of scope:

- web execute route integration;
- runtime behavior changes;
- new role taxonomy, permission model, receipt envelope, memory tier, or
  provider execution semantics;
- public claim changes or release-gate changes;
- claiming live governance proof.

## Target / Source Under Review

Primary sources:

- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_REVIEW_CVF_FINAL_CONVERGED_REMEDIATION_ROADMAP_2026-05-17.md`
- `AGENT_HANDOFF_V9_2026-05-18.md`
- `docs/reviews/archive/CVF_17_05_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-17.md`
- `docs/reviews/archive/CVF_17_05_STABILIZATION_DRIFT_INVENTORY_2026-05-17.md`
- `docs/reviews/archive/CVF_17_05_LEGACY_ABSORPTION_GAP_LEDGER_2026-05-18.md`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/`

## Scope / Methodology

Method:

1. Read the final roadmap Phase 2.B gate.
2. Compare it with delivered Phase 1.P / 1.I / 1.R / 1.M / 2.A contracts.
3. Identify the minimum runtime path that could wire
   `GovernedCapability -> OutcomeWorkflow -> policy/risk/guard -> validation -> Receipt -> deliverable`.
4. Separate "must resolve before GC-018" from "may defer after GC-018".
5. Record any newly discovered gap in the legacy absorption gap ledger.

## Findings / Position

Phase 2.B is not ready for direct runtime implementation yet.

The delivered contracts create a useful target shape, but Phase 2.B still needs
an owner-confirmed migration plan before GC-018 can safely authorize runtime
wire-up. The critical missing item is not another broad contract sketch; it is
a bounded execution path with explicit owners and done criteria.

## Phase 2.B Entry Gate

Before writing Phase 2.B GC-018, the following must be true:

| Gate | Required state | Current state | Disposition |
|---|---|---|---|
| Bounded runtime path selected | One existing execution path named | Not selected | BLOCKER |
| Phase 1.P owners confirmed | Policy/risk/guard adapter owners confirmed for selected path | Contracts exist; runtime owners not confirmed for selected path | BLOCKER |
| Phase 1.I owners confirmed | Role/authority minimum needed by selected path confirmed | Role axes exist; legacy role permission model unresolved | BLOCKER |
| Phase 1.R owners confirmed | Receipt producer/reader migration target confirmed | Receipt envelope exists; producer migration order not selected | BLOCKER |
| Legacy absorption audit scoped | Legacy folders to audit and pass/fail rule named | Ledger created; audit not run | BLOCKER |
| Done criteria defined | Tests/checks prove each migration step | Defined in this artifact as proposed criteria | REVIEW |

## Proposed Bounded Runtime Path

The recommended Phase 2.B target should be one existing non-public-claim path,
not a new product surface.

Preferred candidate:

`GovernedCapability fixture -> OutcomeWorkflow fixture -> guard-contract policy/risk/guard evaluation -> Receipt<OutcomeDeliverable> wrapper -> conformance test`

Rationale:

- It uses the delivered `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/` surface.
- It avoids web route integration.
- It does not require public claim changes.
- It can prove the contract chain without creating a new noncoder vertical
  slice, which belongs to Phase 2.C.

Non-goals for this path:

- no live provider call;
- no web execute route;
- no new ORCHESTRATOR semantics;
- no new permission model beyond the minimum role-axis check required by the
  fixture.

## Migration Order

Phase 2.B GC-018 should authorize these steps in order, not as a single broad
wire-up:

| Order | Step | Owner surface | Done criterion |
|---:|---|---|---|
| 0 | Run legacy absorption audit for selected path | `docs/reviews/archive/CVF_17_05_LEGACY_ABSORPTION_GAP_LEDGER_2026-05-18.md` | Audit records whether ORCHESTRATOR and role catalog gaps affect selected path |
| 1 | Select runtime path and fixtures | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/` | One fixture capability and one fixture workflow are declared as test-only |
| 2 | Bind policy/risk/guard adapter | Phase 1.P contracts | Fixture imports canonical `PolicyDecision`, `RiskLevel`, and `GuardEngineAdapter` types |
| 3 | Bind role-axis minimum | Phase 1.I contracts | Fixture uses an existing `AgentFunctionRole`; no new role enum or permission model |
| 4 | Bind receipt wrapper | Phase 1.R contracts | Fixture output is wrapped as `Receipt<OutcomeDeliverable>` with schema version `1.R.0` |
| 5 | Bind memory tier annotation | Phase 1.M contracts | Workflow step uses one canonical memory tier ID and does not create runtime storage |
| 6 | Validate deliverable chain | Phase 2.A contract | Test proves the chain order and receipt wrapping invariant |
| 7 | Document non-claim boundary | Handoff + review artifact | Artifact states this is contract wire-up proof, not public/live governance proof |

## Owner Confirmation Checklist

### Phase 1.P - Policy / Risk / Guard

Required before GC-018:

- Confirm `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/` as the Phase 2.B
  TypeScript contract owner for the selected fixture path.
- Confirm whether Python governance engine remains out of scope for this
  specific Phase 2.B slice.
- Confirm no new policy decision values beyond the delivered contract.

Done criterion:

- Tests import canonical contract types from `contracts/index.ts`, not from
  local duplicates.

### Phase 1.I - Identity / Role

Required before GC-018:

- Confirm the selected path does not need ORCHESTRATOR-as-CEO semantics.
- Confirm the selected path can use existing role-axis values without absorbing
  `allowed_outputs` or `default_permissions`.

Done criterion:

- Tests prove no new role axis value is introduced.
- Ledger records any legacy role catalog concept intentionally deferred.

### Phase 1.R - Receipt

Required before GC-018:

- Confirm the selected path uses the delivered `Receipt<TPayload>` envelope.
- Confirm no existing receipt producer or reader is changed in Phase 2.B unless
  explicitly named in GC-018.

Done criterion:

- Fixture output is wrapped in a `Receipt<OutcomeDeliverable>`.
- Existing receipt payload structure remains inside `payload`.

### Phase 1.M - Memory

Required before GC-018:

- Confirm Phase 2.B uses memory tier annotations only unless a runtime storage
  owner is separately authorized.

Done criterion:

- Workflow step references a canonical tier; no runtime memory store is created.

## Risk / Corrective Action

Risk:

- Starting Phase 2.B directly would silently absorb role, permission,
  ORCHESTRATOR, receipt producer, and memory runtime semantics under the label
  "wire-up".

Corrective action:

- Keep Phase 2.B as a bounded fixture-driven contract wire-up first.
- Run legacy absorption audit before GC-018.
- Record deferred concepts in the legacy absorption gap ledger.
- Move noncoder vertical slice work to Phase 2.C only after Phase 2.B passes.

## Decision / Recommendation / Disposition

Decision: Phase 2.B runtime implementation remains blocked.

Recommendation: prepare Phase 2.B GC-018 only after the operator confirms:

1. the bounded fixture-driven runtime path;
2. Phase 1.P / 1.I / 1.R owners for that path;
3. role catalog and ORCHESTRATOR gaps are either out of scope or assigned to a
   separate phase;
4. done criteria in this preflight are accepted.

Disposition: `preflight_required_before_gc018`.

## Claim Boundary

This artifact is a preflight plan. It does not authorize implementation, does
not modify runtime code, does not complete legacy absorption audit, does not
change public claims, does not claim live governance proof, and does not lift
`system_reconvergence_stop`.

