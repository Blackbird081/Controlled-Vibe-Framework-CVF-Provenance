# CVF ACEL G1 T3C Group 3 Source Readiness Route

Memory class: governed-local-audit

docType: audit

Status: OPERATOR_CHECKPOINT_REQUIRED

Date: 2026-09-21

Owner: Local orchestrator/reviewer

successorTrancheOpened: NO

## Purpose

Audit whether ACEL G1 T3C can be dispatched after Group 2 became uniquely
active, select the safest Group 3 route, and expose one concrete principal
checkpoint without claiming an observation source or consumer binding.

## Target / Source

| Source | Decision-relevant authority |
|---|---|
| `docs/audits/CVF_ACEL_G1_T3B_GROUP2_ACTIVATION_LOCAL_VERIFICATION_2026-09-21.md` | Group 2 v1 is uniquely active and Local-verified; no successor tranche opened automatically. |
| `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Group 3 schema, immutable snapshot identity, append-only chain, principal separation, exact path and establishment checklist. |
| `docs/reviews/CVF_ACEL_G1_T2E_PARTY_B_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | Party B role and two-registry scope are appointed, but concrete principal and permission proof remain pending. |
| `docs/reviews/CVF_ACEL_G1_T2E_PARTY_C_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | Party C role is appointed, but concrete issuer-governance principal remains pending. |
| `docs/reviews/CVF_ACEL_G1_T2H_PARTY_B_IMMUTABLE_OBSERVATION_RECONCILIATION_WORKER_RETURN_2026-09-18.md` | Local-accepted documentation reconciliation preserves write-once, new-ID observations and rejects same-ID correction. |
| Windows local account inventory, 2026-09-21 | Party A and Approver exist; no concrete Party B or Party C account exists. |

## Scope / Methodology

Local consumed the accepted Group 3 contract and Party B reconciliation,
checked the proposed log path and current account inventory, compared the
identity boundary against existing Party A and Approver SIDs, and evaluated
whether tooling, principal provisioning and real source creation could safely
be combined.

No external research, worker execution, principal creation, credential use,
registry read, observation append or consumer call occurred.

## Current Evidence Matrix

| Requirement | Current evidence | Disposition |
|---|---|---|
| Party B accountable role | dedicated separate audit identity appointed for both registries | SATISFIED_ROLE_ONLY |
| concrete Party B principal | no `cvf-g1-party-b` or equivalent account exists | MISSING_OPERATOR_ACTION |
| separation from Party A | Party A is concrete SID suffix `-1006`; proposed Party B account is a distinct name but has no SID yet | PENDING_PROVISIONING_PROOF |
| separation from Party C | Party C is still role-only; no concrete principal/SID exists | PENDING_T3D_PRINCIPAL_PROOF |
| Group 3 path | `governance/sources/registry_observation_log/LOG.jsonl` absent | EXPECTED_NOT_CREATED |
| observable Group 1 registry | Local-verified Group 1 source exists | AVAILABLE_FOR_LATER_BOUND_READ |
| observable Group 4 registry | issuer registry absent | PENDING_T3D |
| active freshness policy | Group 2 v1 active with `freshnessThresholdSeconds=86400` | AVAILABLE |
| consumer binding | T3E unopened | PENDING_T3E |

## Findings / Position

The Group 3 data model, immutable identity rule, canonical hash chain and
future path are sufficiently specified for a bounded tooling tranche. The
operational identity boundary is not: Party B is appointed only as a role,
and neither Party B nor Party C has a concrete Windows principal in the
current account store.

The missing Party B principal blocks dispatch because the work order must
bind real-mode guards and DACL tests to an observed SID rather than an
invented placeholder. The absent Party C principal does not prevent later
hermetic tooling once Party B is concrete, but it prevents any claim that
the two-registry independence requirement or full Group 3 establishment has
already been proven.

Accordingly, Local selects a principal-first route and keeps implementation,
real observation and consumer binding closed.

## Route Options

| Option | Description | Risk / value | Disposition |
|---|---|---|---|
| A | dispatch tooling and real source creation immediately under Local or Party A | violates Party B separation and fabricates principal evidence | REJECT |
| B | provision a dedicated Party B standard account, then dispatch hermetic tooling; later execute only after Local acceptance and explicit Party C-bound limitations | preserves credential separation and permits machine-first implementation without premature source claims | SELECTED |
| C | provision Party B and Party C together before any T3C tooling | stronger final separation evidence but unnecessarily couples T3C readiness to T3D content/principal design | DEFER |
| D | keep T3C fully parked until T3D and T3E are complete | safe but blocks useful independent log-tooling work without reducing current design risk | NOT_SELECTED |

## Route Selection

Decision: `SELECT_T3C_C0_PARTY_B_PRINCIPAL_THEN_HERMETIC_TOOLING`.

The selected sequence is:

1. Operator confirms and provisions exact local standard account
   `cvf-g1-party-b`, with password required, enabled, non-admin and a bounded
   expiry.
2. Local verifies its exact SID and separation from Party A, the Approver and
   Local. This is principal evidence only.
3. Local authors a GC-018 T3C-C1 worker packet for hermetic observation-log
   writer/checker tooling. The worker must not use credentials, run as Party B
   or create the real log.
4. Local independently reviews the tooling and only then opens a separate
   Party B execution checkpoint for an observation of the existing Group 1
   registry.
5. Any Group 3 claim involving the issuer registry remains pending until a
   concrete Party C principal and Group 4 source exist. Full Group 3
   establishment and T3E consumer binding remain withheld.

## Selected Principal Contract

| Field | Required value |
|---|---|
| local account name | `cvf-g1-party-b` |
| role | Party B / `RegistryObservationOwner` |
| account type | standard local user, never local Administrator |
| password | operator-held; never committed, logged or pasted into chat |
| password required | `True` |
| enabled | `True` |
| expiry | bounded; recommended 30 days from provisioning |
| allowed future write surface | only `governance/sources/registry_observation_log/LOG.jsonl` through reviewed tooling |
| observed-registry rights | read-only; no create, append, write, delete, ownership or DACL mutation rights |
| forbidden identities | Party A SID `S-1-5-21-1644666849-912006174-747199667-1006`; Approver SID `S-1-5-21-1644666849-912006174-747199667-1008`; Local SID suffix `-1001`; future Party C principal |

The selected name is 14 characters and fits the Windows local SAM account
limit. The SID is intentionally not predicted; Local must read it from the OS
after provisioning.

## T3C-C1 Dispatch Boundary

After Local verifies the account, the tooling work order may authorize only:

- a Party B-bound writer with default self-test mode and explicit real mode;
- an independent read-only Python checker;
- disposable fixtures covering canonical bytes, hash chain, duplicate
  `snapshotId`, malformed base64url/JSON, wrong observer and registry-writer
  self-observation;
- a secret-free `runas` launcher created or finalized by Local after review;
- a worker return with `WORKER_MUST_NOT_COMMIT`.

It must not authorize credentials, alternate-user execution, the real log,
Party C provisioning, issuer-registry observation, T3E wiring, admission,
provider/live work, public sync or deployment.

## Risk / Corrective Action

| Risk | Control |
|---|---|
| role label mistaken for a usable principal | require exact OS SID and account-posture evidence before dispatch |
| Party B can mutate the registry it observes | require read-only registry ACL and reject any write/delete/ownership/permission right |
| T3C is blocked unnecessarily on absent Group 4 | permit hermetic tooling and later Group 1-only first observation; keep issuer coverage explicitly pending T3D |
| Group 1-only observation is called complete Group 3 establishment | retain `PENDING_PARTY_C_T3D_AND_T3E` qualifiers until both-registry separation and consumer evidence exist |
| existing snapshot is corrected in place | every changed observation receives a fresh random `snapshotId`; duplicate IDs fail before append |

## Decision / Disposition

Decision: `PARTY_B_PRINCIPAL_CHECKPOINT_REQUIRED_BEFORE_T3C_TOOLING`.

T3B disposition: `ACTIVATED_LOCAL_VERIFIED_PENDING_CONSUMER_BINDING`.

T3C disposition: `ROUTE_SELECTED_PRINCIPAL_NOT_PROVISIONED`.

Group 3 source disposition: `SOURCE_NOT_CREATED`.

Candidate evaluation disposition: `UNVERIFIED`.

The next governed action is operator provisioning of exactly
`cvf-g1-party-b`, followed by Local read-only verification. No worker work
order is dispatchable before the SID and account posture are known.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Group 3 record and immutable identity | schema/invariant | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Source Group 3; Immutable Snapshot Identity | `cvf.observationLogEntry`; `snapshotId` | operational source contract | ACCEPT |
| Party B two-registry role and independence | role authority | `docs/reviews/CVF_ACEL_G1_T2E_PARTY_B_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | Party B Appointment Contract | `RegistryObservationOwner` | operator appointment | ACCEPT_ROLE_ONLY |
| no same-ID correction semantics | reconciliation | `docs/reviews/CVF_ACEL_G1_T2H_PARTY_B_IMMUTABLE_OBSERVATION_RECONCILIATION_WORKER_RETURN_2026-09-18.md` | Local Reviewer Completion Disposition | T2H-01 through T2H-08 | Local-accepted T2H result | ACCEPT |
| concrete Party B account absent | OS observation | Windows local account inventory, 2026-09-21 | bounded local read | `Get-LocalUser` | Windows account store | BLOCKS_DISPATCH |
| proposed real log absent | filesystem observation | repository workspace, 2026-09-21 | exact path probe | `governance/sources/registry_observation_log/LOG.jsonl` | future Group 3 source | EXPECTED_ABSENT |

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_work_order_dispatch_quality.py` |
| literalTokensReviewed | `successorTrancheOpened: NO`; Source Verification columns; operation trace labels; `DEFERRED_PRIVATE_ONLY` |
| gateRunPurpose | confirm bounded readiness decision shape before recording the operator checkpoint |
| claimBoundary | checker conformity is not principal, permission, log, observation or consumer evidence |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: accepted design evidence would make the Group 3
schema/tooling route clear, while the concrete Party B principal and Party C
separation proof would still be missing.

Evidence Comparison: confirmed. The exact log contract and immutable-ID model
are settled, Group 1 is observable, but Windows contains no Party B or Party C
account and the real log path is absent.

Contradiction Or Gap Disposition: split principal provisioning from hermetic
tooling and real execution. Do not encode an invented SID or conflate a role
appointment with operational identity proof.

Claim Update: T3C is route-selected only; it is not dispatched and Group 3
remains `SOURCE_NOT_CREATED`.

## Finding-To-Governance Learning Disposition

Disposition: APPLY_EXISTING_RULE.

The missing concrete Party B principal is the expected checkpoint already
named by T2E/T2F, not a new defect. The selected route applies the existing
principal-before-operational-use rule and creates no new governance surface.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer |
| Provider or surface | private CVF workspace and read-only Windows account inventory |
| Session or invocation | `acel-g1-t3c-group3-readiness-route-20260921` |
| Working directory | repository root |
| Command or tool surface | governed reads, exact-path probes, Get-LocalUser, local Administrators membership inspection, apply_patch and governance gates |
| Target paths | this readiness audit only |
| Allowed scope source | T3B activation closure and T2F rule that successor tranches require separate Local readiness decisions |
| Before status evidence | material HEAD `f85cdf68c`; continuity `c57ae1d61`; Group 3 path absent; thirteen parked paths unchanged |
| After status evidence | one T3C route and exact Party B checkpoint recorded; no account or source changed |
| Diff evidence | this audit is the only intended material path beyond the unchanged thirteen parked paths |
| Approval boundary | Local readiness analysis and principal recommendation only |
| Claim boundary | no principal provisioning, tooling dispatch, source creation, observation, consumer, admission, live/runtime/public effect |
| Agent type | Local reviewer/dispatcher |
| Invocation ID | `acel-g1-t3c-readiness-route-local-20260921` |
| Expected manifest | this audit only |
| Actual changed set | this audit only plus thirteen unchanged parked paths |
| Manifest delta | MATCH |
| Deletion or rename disposition | none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private principal and operational-source planning with no public-sync
authority or public artifact.

## Claim Boundary

This audit selects a principal-first T3C route and recommends the exact local
account name `cvf-g1-party-b`. It does not create or verify that account,
dispatch tooling, create the observation log, observe either registry, bind a
consumer, establish Group 3, admit a candidate, call a provider, public-sync
or deploy.
