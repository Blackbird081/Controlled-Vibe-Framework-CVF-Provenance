# CVF GC-018 Baseline - ACEL G1 T3C-C1 Group 3 Observation Log Tooling

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: ACEL-G1-T3C-C1-GROUP3-OBSERVATION-LOG-TOOLING

Dispatch base head: `cf7872810`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner and reviewer: Local orchestrator/reviewer

Worker target: shared-workspace `INTERNAL_AGENT`

## Purpose

Authorize one bounded worker to implement and hermetically test Party B-bound
Group 3 observation-log tooling. The worker must not use credentials, run as
Party B, read a private key, append the real log, or claim source establishment.

## Decision / Baseline / Proposed Tranche

Decision: dispatch a tooling-only tranche. Baseline: Group 1 is
`SOURCE_CREATED_LOCAL_VERIFIED`; Group 2 v1 is
`ACTIVATED_LOCAL_VERIFIED_PENDING_CONSUMER_BINDING`; Group 3 remains
`SOURCE_NOT_CREATED`. Party B now exists as an enabled, password-required,
non-admin local account with SID
`S-1-5-21-1644666849-912006174-747199667-1009`. Proposed tranche: create one
writer, one independent checker, focused disposable-fixture tests and a worker
return, then stop for Local review.

## Evidence / Verification

Local queried the Windows account store on 2026-09-21. Party B is
`LAM-RUBY\cvf-g1-party-b`, SID ending `-1009`, expires
`2026-10-21T04:54:12Z`, is not a local Administrator, and differs from Party A
SID ending `-1006`, approver SID ending `-1008`, and Local SID ending `-1001`.
The real Group 3 path and all four worker outputs were absent before dispatch.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-G1-T3C-C1-GROUP3-OBSERVATION-LOG-TOOLING --title "ACEL G1 T3C-C1 Group 3 Observation Log Tooling" --date 2026-09-21 --base cf7872810 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with the accepted immutable-observation contract, exact Party B identity, four-path manifest and operator-only execution boundary |
| checkerReadAheadConfirmation | work-order dispatch quality, gate-to-role closeability, worker-return quality, scaffold provenance and operation-trace checker sources read before authoring |
| docOnlyNewFields | none |
| claimBoundary | dispatch provenance only; no observation, source, consumer, runtime, provider, public or deployment behavior exists from this baseline |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| T2F Group 3 contract | accepted immutable-ID schema, byte encoding, canonical preimage and chain | exact contract remains current | RELEASED |
| T3B active policy | Local-verified unique v1 activation with freshness 86400 | authority and freshness remain available for later validation | RELEASED |
| Party B identity | read-only Local OS verification on 2026-09-21 | exact name/SID, enabled, password-required, non-admin, distinct | RELEASED |
| Group 1 registry input | Local-verified snapshot version 1 exists | tooling may model exact-byte input; worker must use fixtures | RELEASED_FOR_HERMETIC_TOOLING |
| real Group 1 observation | Local acceptance of tooling and separate operator execution | Party B acts later | PARKED_OPERATOR_EXECUTION |
| issuer-registry observation | Party C and Group 4 source do not yet exist | T3D must establish both | PARKED_T3D |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | four exact worker artifacts in the paired work order | tooling and disposable fixtures only; no credentials, alternate-principal execution, real source, staging or commit | T2F contract and T3C readiness route | local PowerShell/Python only | IMPLEMENTED |
| `EXTERNAL_AGENT_CLI_MCP` | no external adapter owner in this tranche | no external ingress, authentication, mutation, receipt, runtime or public claim | no accepted source authorizes it | fresh governed packet required | DEFERRED_WITH_REASON |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`CODE_CHANGE`, role=`dispatcher`, lifecyclePhase=`dispatch`.

Command: `python governance/compat/run_adif_defect_resolver.py --task-class CODE_CHANGE --role dispatcher --lifecycle-phase dispatch`.

Returned defects: NONE_RETURNED. Dispatch impact: none.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | dispatch-ready status, Source Verification columns, Scaffold Provenance fields, Gate-To-Role graph, trace labels and no-commit return terms |
| gateRunPurpose | confirmation after source-driven authoring, not first discovery |
| claimBoundary | packet structure and owned-path compatibility only; not implementation correctness |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Group 3 schema and immutable identity | contract invariant | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Source Group 3; Closed Preimage Field Lists; Immutable Snapshot Identity | `cvf.observationLogEntry`; `snapshotId` | Group 3 operational-source contract | ACCEPT |
| Party B role | role authority | `docs/reviews/CVF_ACEL_G1_T2E_PARTY_B_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | Party B Appointment Contract | `RegistryObservationOwner` | operator appointment | ACCEPT |
| principal-first route | Local decision | `docs/audits/CVF_ACEL_G1_T3C_GROUP3_SOURCE_READINESS_ROUTE_2026-09-21.md` | Route Selection; T3C-C1 Dispatch Boundary | `SELECT_T3C_C0_PARTY_B_PRINCIPAL_THEN_HERMETIC_TOOLING` | Local orchestrator/reviewer | ACCEPT |
| Party B concrete SID/posture | recorded dispatch evidence | `docs/baselines/CVF_GC018_ACEL_G1_T3C_C1_GROUP3_OBSERVATION_LOG_TOOLING_2026-09-21.md` | Evidence / Verification | `cvf-g1-party-b` | Windows account store evidence captured by Local | ACCEPT |
| Group 1 snapshot input | operational source | `governance/sources/verifier_key_registry/REGISTRY.json` | top-level registry envelope | `registrySnapshotVersion` | Group 1 registry | ACCEPT |

## Negative Search And Collision Discipline

Exact `Test-Path` probes returned false for the two dispatch artifacts before
authoring, all four worker outputs, and the real Group 3 log. Exact batch and
tool-name searches found no predecessor. Existing T2F/T3C prose is authority,
not a path collision.

## Finding-To-Governance Learning Disposition

Disposition: APPLY_EXISTING_RULE.

The route applies the existing principal-before-operational-use and
machine-first independent-review controls. No new recurring defect is raised.

## Claim Boundary

This baseline authorizes hermetic tooling only. It does not authorize Party B
credentials or execution, real registry reads or observation writes, issuer
coverage, Group 3 establishment, T3E wiring, admission, provider/live work,
public sync, deployment, staging or commit.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private operational-source preparation with no public-sync authority.
