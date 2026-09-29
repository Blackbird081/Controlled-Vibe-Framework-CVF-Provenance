# CVF GC-018 Baseline - ACEL G1 T2H Party B Immutable Observation Reconciliation

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-09-18

Batch ID: ACEL-G1-T2H-PARTY-B-IMMUTABLE-OBSERVATION-RECONCILIATION

Dispatch base HEAD: `bef994468ed76fd66e0893353852b4c077b9ec6c`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator confirmed Party B retains its independent role while the correction-chaining condition is replaced by immutable new-ID observations.

Reviewer/closer: Local orchestrator/reviewer.

Worker: one shared-workspace `INTERNAL_AGENT`.

## Purpose

Reconcile the active T2E Contract 3 and Party B appointment with the later,
accepted T2G immutable-snapshot design. This is authority-document alignment,
not operational source establishment or implementation.

## Scope / Owner Boundary

The worker may modify only the committed T2E four-owner contract and Party B
appointment, plus create one new T2H worker return. T2C, the accepted T2G
audit, Party A/C and activation-approver appointments, historical work orders,
continuity, and thirteen parked untracked paths are read-only. Local alone
reviews, repairs minor evidence defects, stages and commits. The operator
retains every later source, key, principal, implementation and live decision.

## Architecture Decision And Acceptance Boundary

1. Party B's appointed identity, two-registry scope, writer/observer separation,
   append-only write authority and credential-independence obligations survive.
2. Remove normative same-`snapshotId` correction chaining, superseding
   observation entries, and references that make chaining a condition for the
   appointment to remain valid. A fresh observation, including one after an
   error or content change, receives a new globally unique `snapshotId` and
   one immutable original record. No old record is rewritten, deleted, aliased
   or reclassified as an active head.
3. The worker must not change T2C's `lookup(snapshotId)` or
   `countObservationsFor(snapshotId)` contract. Exact-ID count is literal;
   duplicate-ID integrity faults fail closed. A new snapshot does not, by
   itself, revoke a signed receipt for the old snapshot.
4. Distinguish observation-record identity from registry-entry correction:
   Party C may amend issuer registry state through its separately governed
   route, but Party B records any later observation under a new ID. No
   cross-party authority is transferred.
5. Preserve source-status and operational boundaries: all four sources remain
   `SOURCE_NOT_CREATED` and candidate admission remains `UNVERIFIED`. Neither
   the role label nor this amendment proves a provisioned principal or log.
6. Reconcile all normative Contract 3 and Party B appointment clauses,
   including risk/invalidating-condition prose and any negative cases. Keep
   historical dispatch descriptions explicitly historical rather than silently
   rewriting accepted history.

## Decision / Baseline / Proposed Tranche

Decision: dispatch one documentation-only reconciliation. The operator's
affirmative confirmation changes only the Party B appointment condition
above; it does not appoint another party or authorize the future store.
Baseline: T2G accepted design at material commit `4b6a12a`, T2C unchanged.
Proposed tranche: exact three-output worker return followed by Local review.
`successorTrancheOpened: NO` for implementation or T3.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| operator amendment | operator affirmed retaining Party B while replacing correction chaining with new-ID append-only observations in this conversation | documentation reconciliation only | ACCEPT_BOUNDED |
| accepted immutable design | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md`, Immutable Snapshot Identity; material commit `4b6a12a` | use as exact identity/receipt semantic anchor | ACCEPT |
| T2E Contract 3 conflict | `docs/audits/CVF_ACEL_G1_T2E_FOUR_OWNER_SOURCE_CONTRACT_DESIGN_2026-09-18.md`, Contract 3 | amend within operator choice | ACCEPT_AS_RECONCILIATION_INPUT |
| Party B appointment conflict | `docs/reviews/CVF_ACEL_G1_T2E_PARTY_B_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md`, Appointment Contract | preserve party and independence, replace only obsolete correction condition | ACCEPT_AS_RECONCILIATION_INPUT |
| T3/source creation | no authority in this decision | separate future operator checkpoint | PARKED_NO_SOURCE_CREATION_AUTHORITY |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | T2E Contract 3 and Party B appointment documents | documentation-only, no mutation of source or receipt | T2G accepted audit and operator confirmation | internal workspace only; no runtime adapter | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no new CLI/MCP interface in this tranche | no ingress, authentication, approval, receipt, raw-data or mutation capability added | no external execution evidence claimed | external adapter remains outside this packet | `DEFERRED_WITH_REASON` |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T2E requires correction chaining | CURRENT_AUTHORITY_CONFLICT | `docs/audits/CVF_ACEL_G1_T2E_FOUR_OWNER_SOURCE_CONTRACT_DESIGN_2026-09-18.md` | Contract 3, responsibility/lifecycle/correction route | correction chaining | Contract 3 | ACCEPT_AS_REPAIR_INPUT |
| Party B appointment invalidates removal | CURRENT_AUTHORITY_CONFLICT | `docs/reviews/CVF_ACEL_G1_T2E_PARTY_B_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | Party B Appointment Contract, invalidating conditions | Correction behavior; removes correction chaining | operator appointment | ACCEPT_AS_REPAIR_INPUT |
| T2G forbids same-ID correction | ACCEPTED_DESIGN | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Immutable Snapshot Identity, T2G-01 through T2G-05 | `snapshotId`; `countObservationsFor` | Group 3 | ACCEPT |
| T2C counts source observations | ACCEPTED_CONSUMER | `docs/audits/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_2026-09-17.md` | `LookupProvenanceCheck` | `lookup`; `countObservationsFor` | verifier predicate 3 | ACCEPT |

## Negative Search And Collision Discipline

Both exact T2H dispatch paths and the new return path were absent before
authoring. A literal search for the batch ID across `docs`, `governance`,
`EXTENSIONS`, `ECOSYSTEM` and `CVF_SESSION` returned zero matches before this
packet. The two worker-modified paths already exist and are not collision
candidates. This bounded check does not claim a full corpus scan.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-G1-T2H-PARTY-B-IMMUTABLE-OBSERVATION-RECONCILIATION --title "ACEL G1 T2H Party B Immutable Observation Reconciliation" --date 2026-09-18 --base bef994468ed76fd66e0893353852b4c077b9ec6c --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --no-evidence-readiness-applicable --stdout` |
| generatedProfile | generic-worker-dispatch; internal INITIAL; no-commit |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact operator choice, authority conflict, three-output boundary and acceptance obligations |
| checkerReadAheadConfirmation | dispatch-quality, review-cost, convergence, closeability, structural, trace and export checkers |
| docOnlyNewFields | no runtime/schema field; documentation amendment only |
| claimBoundary | scaffold preview is shape guidance, not source or runtime proof |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | DISPATCH_READY; Source Verification Block; ADIF disclosure; trace labels; private export token; no-commit exact manifest |
| gateRunPurpose | confirm authored packet shape after source inspection, not decide semantic acceptance |
| claimBoundary | checker PASS cannot prove Party B principal or operational source existence |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`DOC_CHANGE`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class DOC_CHANGE --role dispatcher --lifecycle-phase pre-dispatch`

Returned defects: NONE_RETURNED

Returned defect count: 0

Dispatch impact: no matched entry; exact cross-document authority reconciliation remains required.

## Evidence / Verification Boundary

The worker must supply line-anchored before/after conflict resolution, targeted
negative cases, exact three-path delta, 13/13 parked SHA reconciliation, and
worker-return fast-gate evidence. Local remains final technical reviewer.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Chain map route | T2E appointment plus accepted T2G -> operator amendment -> INTERNAL_AGENT T2H -> Local review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this T2H baseline and paired work order |
| Internal source | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` |
| Disposition | `NOT_APPLICABLE_INTERNAL_ONLY_WITH_REASON`: no external research or source is admitted |
| Claim boundary | Local retains private-CVF final technical decision authority |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private appointment/contract reconciliation; no public-sync authority.

## Claim Boundary

This baseline changes only documentation authority for Party B's future
observation behavior. It does not create a log, principal, key, credential,
registry, verifier implementation, live lookup, candidate admission, runtime,
external adapter, public export or deployment authority.
