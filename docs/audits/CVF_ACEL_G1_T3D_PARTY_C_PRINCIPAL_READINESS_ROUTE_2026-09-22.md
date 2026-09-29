# CVF ACEL G1 T3D Party C Principal Readiness Route

Memory class: governed-audit

docType: audit

Status: OPERATOR_PROVISIONING_READY

Date: 2026-09-22

Batch ID: ACEL-G1-T3D-PARTY-C-PRINCIPAL-READINESS

Decision base HEAD: `6a0866cb9`

providerExecutionAuthority: FORBIDDEN

successorTrancheOpened: NO

## Purpose

Select the smallest source-verified next step after T3C-C2 closure: provision
the concrete Party C principal required before any Group 4 issuer-registry
tooling or source creation can be authorized.

## Target / Source

| Source | Verified fact |
|---|---|
| `docs/reviews/CVF_ACEL_G1_T2E_PARTY_C_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | Party C is appointed as a dedicated issuer-governance identity, but the concrete principal remains pending |
| `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Group 4 registry and lookup-response sources require exclusive Party C write authority |
| `docs/audits/CVF_ACEL_G1_T3C_C2_GROUP3_SOURCE_LOCAL_VERIFICATION_2026-09-22.md` | Group 3 first observation is Local verified; Group 4 remains closed |
| Windows local-account inventory, 2026-09-22 | Party A, Party B and Approver exist; `cvf-g1-party-c` is absent; none of the three is an Administrators member |

## Scope / Methodology

Local compared the remaining G1 dependency chain and selected principal-first
provisioning rather than Group 4 implementation. The exact local account name
is `cvf-g1-party-c`; it must be enabled, password-required, non-admin,
time-bounded and SID-distinct from Local, Party A, Party B and the activation
Approver.

The supplied launcher has a read-only `--check` mode and an elevated execution
mode. Execution requires an exact confirmation and accepts the password only
as a SecureString. It writes a secret-free result receipt and removes only the
newly created account if a post-create invariant fails.

## Findings / Position

| Dependency | State | Decision |
|---|---|---|
| Group 1 verifier-key registry | Local verified | RETAIN |
| Group 2 active authority specification | Local verified pending consumer binding | RETAIN |
| Group 3 first observation | Local verified | CLOSED |
| Party C conceptual appointment | accepted | RETAIN |
| concrete Party C principal | absent | SELECT |
| Group 4 registry/lookup implementation | absent | PARK_UNTIL_PRINCIPAL_VERIFIED |
| T3E consumer binding | absent | PARK |

Decision: `SELECT_ACEL_G1_T3D_PARTY_C_PRINCIPAL_PROVISIONING`.

## Execution Boundary

The operator may run
`scripts/run_provision_cvf_g1_party_c_as_admin.cmd`, approve UAC, type exactly
`CREATE CVF G1 PARTY C`, and enter a new strong password at the secure prompt.
The password is not printed, persisted in the repository or included in the
receipt.

Success token:
`PARTY_C_PRINCIPAL_CREATED_PENDING_LOCAL_VERIFICATION`.

Any error ends authority for that attempt. Local must inspect account and
receipt state before retry. Do not manually add Party C to Administrators.

## Risk / Corrective Action

| Risk | Control |
|---|---|
| account collides with another authority | exact new name plus post-create SID collision check |
| account gains administrative authority | explicit Administrators-membership rejection |
| password becomes evidence | SecureString input; no password or derived secret in receipt/output |
| partial provisioning | exact absence precondition and targeted rollback of only the newly created account |
| principal creation mistaken for Group 4 | pending-verification token and explicit Group 4/T3E hold |

## Decision / Disposition

`OPERATOR_PROVISIONING_READY`.

This decision authorizes one bounded Party C principal provisioning attempt.
It does not authorize issuer-registry tooling, registry creation, lookup
response writes, Party B observation of Group 4, consumer binding or candidate
admission.

## Finding-To-Governance Learning Disposition

No new cross-case defect is asserted. This route reuses the accepted
principal-first pattern from Party A, Approver and Party B. The launcher adds
the already-learned controls: password-required verification, non-admin
posture, bounded expiry, secret-free receipt and targeted rollback.

## Epistemic Process Block

### Expected Result / Prediction

The nearest unresolved dependency after Group 3 closure should be the concrete
Party C identity, because exclusive Group 4 write authority cannot be tested
against a conceptual role.

### Evidence Comparison

The T2E appointment and T2F operational contract require a distinct Party C,
while Windows inventory confirms that the proposed account does not exist.

### Contradiction Or Gap Disposition

No contradiction. The conceptual appointment is retained and operationalized
through a separately verifiable local principal.

### Claim Update

Party C provisioning is ready for operator execution; Party C is not yet an
accepted concrete principal and Group 4 remains unimplemented.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_core_guard_self_protection.py` |
| literalTokensReviewed | audit headings, bounded status, learning disposition, epistemic comparison, trace, public disposition and claim boundary |
| gateRunPurpose | confirm the source-derived selection and provisioning boundary; gates are evidence, not first discovery |
| claimBoundary | tooling readiness does not prove account creation or Group 4 readiness |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: read-only changed-set accounting for the
two pre-existing parked protected checker paths. No checker mutation is
authorized.

Protected paths: `governance/compat/check_task_class_calibration_owner_evidence.py`;
`governance/compat/test_check_task_class_calibration_owner_evidence.py`.

Operator authorization: standing instruction to continue G1-G6 and Local
orchestrator/reviewer authority. Rollback boundary: revert only this decision
and its two provisioning helpers if rejected; preserve T3C-C2 and all parked
paths.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | CVF Local orchestrator/reviewer |
| Provider or surface | local private provenance workspace |
| Session or invocation | ACEL G1 T3D Party C principal-first selection, 2026-09-22 |
| Working directory | repository root |
| Command or tool surface | governed reads, Windows account inventory, apply_patch, syntax/check mode, governance gates and Git |
| Target paths | this audit and two Party C provisioning helpers |
| Allowed scope source | operator-directed G1-G6 continuation and accepted T2E/T2F contracts |
| Before status evidence | T3C-C2 closed at `820aae3ec`; Party C account absent; thirteen parked paths preserved |
| After status evidence | exact provisioning route ready; no account or Group 4 source created |
| Diff evidence | exact three-path material manifest; parked paths excluded |
| Approval boundary | one operator-mediated Party C provisioning attempt only |
| Claim boundary | no issuer registry, lookup response, observation, T3E, admission, provider/live, public or deployment effect |
| Agent type | Local orchestrator/reviewer |
| Invocation ID | `acel-g1-t3d-party-c-principal-readiness-20260922` |
| Expected manifest | this audit; `scripts/provision_cvf_g1_party_c.ps1`; `scripts/run_provision_cvf_g1_party_c_as_admin.cmd` |
| Actual changed set | this audit; `scripts/provision_cvf_g1_party_c.ps1`; `scripts/run_provision_cvf_g1_party_c_as_admin.cmd` |
| Manifest delta | MATCH |
| Deletion or rename disposition | none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: machine-specific local-principal provisioning; no public-sync authority.

## Claim Boundary

This audit selects and prepares one concrete Party C principal. It does not
claim the principal exists, establish Group 4, perform a lookup, create a
response receipt or observation, wire a consumer, promote a key, admit a
candidate, call a provider, export publicly, deploy or claim production
readiness.
