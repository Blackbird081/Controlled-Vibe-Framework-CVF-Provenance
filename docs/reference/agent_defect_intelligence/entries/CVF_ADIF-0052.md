# ADIF-0052 - Continuity Dispatch Omits Transitive Pins And Post-Mode Literal

Memory class: POINTER_RECORD

Status: ACTIVE

```text
defectId: ADIF-0052
title: Continuity dispatch omits transitive pins and post-mode literal
defectCategory: SOURCE_FIDELITY
defectClass: ORCHESTRATOR_PACKET_GAP
defectRole: dispatcher
severity: HIGH
lifecycleState: ACTIVE
taskClasses: Work-order authoring / dispatch; Continuity migration; Reviewer closure
roles: dispatcher; worker; reviewer; closer
lifecyclePhases: pre-dispatch; pre-implementation; pre-closure
surfaceSelectors: exact changed-set contracts, Project Knowledge pins, canonical state, bootstrap and mirror projections
detectionSignals: an authorized carrier edit changes multiple source-pinned files but the packet names only one pin; a required mode transition has no exact post-mode literal or equality assertion
enforcementLevel: GUIDANCE_ONLY
checkerBindings: governance/compat/check_project_knowledge.py; target-local session consistency tests
promotionState: MACHINE_CHECK_CANDIDATE
supersedes: NONE
lastVerifiedCommit: 9c4f8ecd1
roadmapSeedId: NONE
```

## Purpose

Prevent a continuity work order from freezing a changed set before tracing all
transitive source pins and from asking for a new lifecycle mode without naming
the exact post-transition value that every projection must share.

## Scope / Applies To

Applies when a dispatch edits source files tracked by a Project Knowledge or
similar source-hash registry, or when canonical state, a compatibility mirror,
a bootstrap model, memory, and handoff must agree on a newly introduced mode.

## Bad Example

Authorize edits to AGENTS, a manifest, and implementation status, but authorize
refreshing only the implementation-status pin. Separately require a "new T3
mode" while allowing the worker to preserve the preceding parked mode because
no exact new literal or negative assertion was specified.

## Good Example

Compute the full reverse-pin closure before freezing the manifest. List every
pin whose source bytes will change. For a lifecycle transition, provide the
exact post-mode literal and require equality across canonical state, bootstrap,
mirror, memory, status, and handoff, plus an assertion that the prior mode is
absent from active projections.

## Canonical Sources

- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`.
- `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md`.
- `governance/compat/check_project_knowledge.py`.

## Remediation

Dispatchers must inspect the source-pin registry and its checker before
approving an exact scope. State-transition acceptance criteria must bind both
field equality and the exact target value. Reviewers must treat a preserved
pre-tranche mode as a semantic failure even when projection-equality tests pass.

## Epistemic Process Block

### Expected Result / Prediction

The exact changed set should contain every required pin refresh, and a required
new lifecycle mode should be visibly distinct from the preceding mode.

### Evidence Comparison

ACRC-T3 changed three source-pinned files while its Work Order authorized only
one pin refresh. The worker correctly refreshed all three and disclosed the
scope contradiction. It also kept the preceding P4-A1 parked mode consistently
across all projections; structural tests passed, but AC-07's semantic transition
did not. The reviewer repaired both issues under explicit closure-conversion
authority and committed target closure at `0b835be3f`.

### Contradiction Or Gap Disposition

The first finding was a transitive-scope omission, not unrelated worker scope
growth. The second showed that equality across projections does not prove the
requested state transition when the expected target literal is unspecified.

### Claim Update

Exact-scope continuity dispatch requires reverse-pin closure and exact semantic
postconditions, not only file lists and cross-projection equality.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | independent reviewer/closer |
| Provider or surface | local private provenance Core and downstream target |
| Session or invocation | ACRC-T3 independent closure, 2026-08-11 |
| Working directory | Core repository root and sibling shift-operations-workspace target |
| Command or tool surface | Git inspection, SHA-256 recomputation, focused tests, repository validator, workspace doctor, and apply_patch |
| Target paths | ADIF-0052; entries README row; ACRC-T3 Core closure evidence |
| Allowed scope source | operator-delegated orchestrator/reviewer authority and Work Order reviewer closure conversion |
| Before status evidence | worker disclosed two additional pin refreshes; active projections retained the prior mode |
| After status evidence | all pins exact; all active projections use the bounded post-T3 closure mode; reusable defect recorded |
| Diff evidence | downstream exact-15 reviewer closure and Core closure packet |
| Approval boundary | bounded continuity closure and governance learning only |
| Claim boundary | guidance and machine-check candidate; no generalized prevention claim |
| Agent type | reviewer/closer |
| Invocation ID | `active-continuity-t3-adif-0052-20260811` |
| Expected manifest | ADIF-0052; entries README row; T3 Core closure evidence |
| Actual changed set | ADIF-0052; entries README row; T3 Core closure evidence |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance learning. No public-sync action is
authorized.

## Claim Boundary

This entry records one bounded dispatch and review defect. It does not prove a
general reverse-dependency engine, universal mode-transition enforcement, or
runtime, provider, public, deployment, push, or production behavior.
