# CVF GC-018 Baseline - ACEL G1 T3D-C1-R2 Reservation-Compatible Tooling Correction

Memory class: governed-dispatch-baseline

docType: baseline

Status: DISPATCH_READY

Date: 2026-09-23

Batch ID: ACEL-G1-T3D-C1-R2-RESERVATION-COMPATIBLE-TOOLING-CORRECTION

Dispatch base HEAD: `c8b9a7bb459738ca7c7614dc3ba60093c42749f3`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Local orchestrator/reviewer

providerExecutionAuthority: FORBIDDEN

successorTrancheOpened: NO

## Purpose

Authorize a bounded correction packet for the two
T3D-C1 Group 4 writers. The accepted C0-R1 contract requires a protected
parent and two pre-owned zero-byte targets, while the current writers still
implement initial target absence and pattern-based orphan deletion. This
baseline authorizes only the named shared-workspace worker scope after the
pre-dispatch gate passes; it does not authorize real-principal execution.

## Target / Source

| Source | Verified owner fact | Disposition |
|---|---|---|
| `docs/audits/CVF_ACEL_G1_T3D_GROUP4_ACTUAL_TOKEN_PROOF_TOOLING_GAP_AUDIT_2026-09-23.md` | four blocking writer/contract joins and selected correction-first route | ACCEPT |
| `docs/audits/CVF_ACEL_G1_T3D_C0_R1_GROUP4_OPERATIONAL_BOUNDARY_AMENDMENT_2026-09-23.md` | exact parent, reservation, own-target transaction, ledger recovery and actual-token matrix | ACCEPT |
| `docs/reviews/CVF_ACEL_G1_T3D_C0_R1_GROUP4_OPERATIONAL_BOUNDARY_AMENDMENT_COMPLETION_2026-09-23.md` | bounded contract closure; C1-R2 and source execution remain separate | ACCEPT |
| `scripts/acel_g1_party_c_group4_registry_writer.ps1` | target-absent registry publication and old-temp sweep | ACCEPT_AS_CORRECTION_TARGET |
| `scripts/acel_g1_party_b_group4_lookup_response_writer.ps1` | target-absent response initialization and old-temp sweep | ACCEPT_AS_CORRECTION_TARGET |

## Scope / Methodology

Role: Local dispatch author; phase: C1-R2 pre-dispatch; decision owner: Local.
The proposed implementation is two writer corrections and a narrowly scoped
disposable-root proof/recovery harness. It is hermetic-first. It must not run
as Party B/C, alter the real Group 4 source directory, use credentials, append
an issuer observation/lookup response, or open T3E. No subagent is assigned.
The operator selected a distinct shared-workspace worker and Local
reviewer/probe actor on 2026-09-23; same-thread role switching alone is not
independent review.

## Source / Predecessor Evidence

The source table above is the exact predecessor set. C0-R1's completion
review is contract acceptance, not implementation acceptance; the source gap
audit compares that contract to both current writer entrypoints. No rejected
T2/T2A/T2B archival file is an implementation authority.

## Findings / Position

The four findings in the gap audit are one dependency class, not four serial
rework rounds. A corrected writer must claim only its own exact reservation,
revalidate the parent and both target identities/security around the entire
transaction, fail on unknown residue, and leave prior-transaction cleanup to
a separate exact ledger-bound Administrator recovery path. The disposable
test surface must invoke the same guarded mutation path with exact production
security policy, while remaining incapable of reaching the real source.

## Required Acceptance Matrix

| ID | Required outcome | Negative / independent evidence |
|---|---|---|
| C1-R2-01 | Party C replaces only its pre-reserved zero-byte registry | absent/nonzero/wrong-owner/linked/reparse reservation rejects without mutation |
| C1-R2-02 | Party B atomically claims only its pre-reserved zero-byte response target | absent/nonzero/wrong-owner/linked/reparse reservation rejects without mutation |
| C1-R2-03 | both writers verify exact protected parent and asymmetric complete DACLs | extra, inherited, deny, reordered, group-widened or wrong-owner state fails closed |
| C1-R2-04 | current transaction owns only its temp and rollback | unknown/stale temp remains untouched and blocks publication |
| C1-R2-05 | durable ledger binds transaction, token, target, temp, prestate and phase before temp creation | missing/mismatched ledger forbids administrative cleanup |
| C1-R2-06 | separate recovery owner handles exact hard-termination residue | unknown artifact preserved; non-target bytes/security never changed |
| C1-R2-07 | real second-process peer reaches guarded mutation path with deterministic barrier | entry before release fails; timeout is deadlock safety only |
| C1-R2-08 | disposable route is constrained to validated fresh root and production-equivalent descriptors | wrong token, traversal, real source path, cross-target/parent mutation are rejected |
| C1-R2-09 | Local independent review and probe remain after worker return | worker cannot self-certify Windows actual-token success |

## Risk / Corrective Action

This is security-sensitive NTFS transaction tooling. The paired work order must
name all owned paths and full high-risk transaction proof before release. A
static or same-token hermetic pass is not Windows Party B/C proof. If exact
own-target replacement is not possible under the proposed rights, stop at
`TOOLING_ACCEPTED_SOURCE_NOT_CREATED` and reassess split paths or mediator;
do not widen ACEs in this tranche.

## Decision / Disposition

`DISPATCH_READY` for bounded internal worker implementation after Local
pre-dispatch verification. The operator-selected distinct worker may begin
only after receiving the committed work order and capturing execution HEAD.
The later actual-token experiment requires its own checkpoint and order.

## Evidence / Verification

Before release, Local checks the exact packet with the focused
high-risk, SCEC, source-fidelity, structural and pre-dispatch gates. After a
future worker return, the reviewer must independently probe reservation
claiming, unknown-residue preservation, peer exclusion and rollback under
disposable fixtures. Neither gate success nor a self-test establishes the
Party B/C Windows effective-rights result.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --help` inspected during release read-ahead; no generated artifact was used |
| generatedProfile | protected-governance-path requirements manually applied to the existing baseline |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | manually promoted the held baseline after distinct actor selection and pre-dispatch checker read-ahead |
| checkerReadAheadConfirmation | dispatch scaffold, task routing, work-order quality and lifecycle controls applied |
| docOnlyNewFields | none |
| claimBoundary | dispatch baseline only; no worker implementation, actual-token proof or real source |

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_high_risk_local_transaction_proof.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_work_order_dispatch_quality.py` |
| literalTokensReviewed | `DISPATCH_READY`; `High-Risk Local Transaction Proof Applicability`; `Semantic Convergence Outcome`; `Gate-To-Role Closeability Contract` |
| gateRunPurpose | confirmation/evidence for pre-read packet requirements, not first discovery or OS proof |
| claimBoundary | checker declarations are not principal-specific proof |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`CODE_CHANGE`, role=`dispatcher`, lifecyclePhase=`dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class CODE_CHANGE --role dispatcher --lifecycle-phase dispatch --json`

Returned defects: NONE_RETURNED; resolver reported `totalCandidates: 0` and
`truncated: false` at packet authoring.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatch author |
| Provider or surface | private CVF workspace |
| Session or invocation | G1 T3D-C1-R2 packet preparation, 2026-09-23 |
| Working directory | repository root |
| Command or tool surface | read-only source inspection, apply_patch, governance gates and Git |
| Target paths | this baseline and paired work order |
| Allowed scope source | operator continuation and committed tooling-gap audit |
| Before status evidence | HEAD `c8b9a7bb4`; clean worktree; four blocking source findings |
| After status evidence | dispatch packet only; no worker implementation |
| Diff evidence | exact two-path packet diff before commit |
| Approval boundary | dispatch preparation only |
| Claim boundary | no credential, alternate-principal, source or live execution |
| Agent type | Local dispatch author |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private Windows proof/tooling dispatch; no public artifact claim.

## Claim Boundary

This baseline does not establish Windows permission behavior, corrected
tooling, a real source, T3E binding, provider behavior or production readiness.
