# CVF ACEL G1 T3B R2 Atomic Rotation Contract Correction Completion Review

Memory class: governed-review

docType: completion_review

Status: CLOSED_PASS_BOUNDED

Date: 2026-09-20

Post-closure correction date: 2026-09-21

executionBaseHead: `d87a01115f1d37991bf90d2ac0cbcbf9c4e27362`

closureBaseHead: `d87a01115f1d37991bf90d2ac0cbcbf9c4e27362`

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3B_R2_ATOMIC_ROTATION_CONTRACT_CORRECTION_2026-09-20.md`

Reviewer: Local orchestrator/reviewer

independentProbeRequired: YES

independentProbeDisposition: PASS_INDEPENDENT_PROBE

probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER

implementationWorkerActor: shared-workspace-internal-agent-worker-r2

probeExecutorActor: local-orchestrator-reviewer-codex-2026-09-20

workerInvocationId: acel-g1-t3b-r2-worker-return-20260920

probeInvocationId: acel-g1-t3b-r2-local-atomic-probe-20260920

workerTestCommand: python governance/compat/test_check_acel_g1_verification_authority_spec.py

probeCommandOrMethod: three named unittest methods for positive atomic convergence, replacement-field tamper rejection and cross-language replay convergence

probeObservedResult: all three reviewer-selected probes passed; final active set was replacement-only and both durable replacement fields were digest-bound

oracleSeparationBasis: Local selected three decision-changing methods and independently interpreted their state/digest outcomes after detecting a worker count contradiction; actor, invocation and evidence binding differ from the worker return

workerOracleSha256: 2f2ca393526983c13c5bfe91127e03ba24b6086919ca724c9860ee5d7e9f70df

probeOracleSha256: 73cbce6418a4ca27a9d2838c9f02ebe8dbfe0f8c7b29105ec5e0ec6d7191b670

workerEvidenceRef: docs/reviews/CVF_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_WORKER_RETURN_2026-09-20.md

probeEvidenceRef: governance/compat/test_check_acel_g1_verification_authority_spec.py

Review-Cost Telemetry: REQUIRED

## Purpose

Close the bounded R2 correction after evaluating the returned evidence,
independently probing the atomic-rotation seam, and applying two localized
reviewer repairs that do not change the accepted design or authority boundary.
This review also records the later standard-principal DACL correction exposed
by the first real Party A execution attempt.

## Scope / Methodology

Role: Local orchestrator/reviewer. Phase: R2 completion review. Decision owner:
Local for acceptance, bounded repair, material commit and continuity routing.
The shared-workspace worker is an `INTERNAL_AGENT`; the operator is transport
only and no provider identity supplies authority.

The review reused the worker's complete 48/48 spec-writer and 74/74
decision-writer evidence. A reported Python count contradiction admitted one
focused rerun, which proved 58/58 rather than 65/65. The reviewer then ran the
worker-return fast gate and three decision-changing atomic-rotation probes:
positive sole-active convergence, durable replacement-field tamper rejection,
and cross-language PowerShell/Python convergence. No credential, `runas`,
alternate principal, real Group 2 path, provider, live, public or deployment
action occurred.

## Target / Source

| Artifact | SHA-256 at review | Disposition |
|---|---|---|
| controlling T2F contract | `b7162d6dabd901e047db63b8dbca2a21504c2c5548f327587ef8cac0bcfc85e4` | ACCEPT |
| decision writer | `9176407dcd879f6f1b1159ae85d8c0bce05700857a3cd660f44da712b811cc61` | ACCEPT_WITH_POST_CLOSURE_DACL_REPAIR |
| Python checker | `f696de73068567b372633a2b7745495261a7fb61d21facb7eeb34e7e72b6f6a2` | ACCEPT |
| Python focused tests | `73cbce6418a4ca27a9d2838c9f02ebe8dbfe0f8c7b29105ec5e0ec6d7191b670` | ACCEPT |
| corrected worker return | `2f2ca393526983c13c5bfe91127e03ba24b6086919ca724c9860ee5d7e9f70df` | ACCEPT_WITH_REVIEWER_EVIDENCE_REPAIR |
| spec writer | `039e7f3b0f870a17e9b82270c813919aee8f716697245455937ff17c62160dbc` | ACCEPT_WITH_POST_CLOSURE_DACL_REPAIR |

## Findings / Position

No implementation-blocking finding remains.

| ID | Severity | Finding | Reviewer action | Final disposition |
|---|---|---|---|---|
| T3B-R2-RV-01 | LOW | Worker return reported Python 65/65, while direct execution produced 58/58. | Corrected all five count claims, elapsed time, and delta from +18 to +11. | CLOSED_LOCAL_REPAIR |
| T3B-R2-RV-02 | LOW | Two decision-writer comments retained the obsolete R1 statement that a replacement required prior activation. | Updated comments to the implemented rule: prior approval plus inactive/non-superseded state. | CLOSED_LOCAL_REPAIR |
| T3B-R2-RV-03 | HIGH | The first real standard-principal Party A run failed at DACL hardening because both writers redundantly called `SetOwner`, which can require `WRITE_OWNER` or `SeRestorePrivilege`. | Verified failure-atomic rollback, removed owner mutation from both writers, added exact-owner verification and a machine regression in each self-test. | CLOSED_LOCAL_REPAIR_PENDING_REAL_RETRY |

The first two repairs are localized evidence/comment corrections. The third is
a shared Windows authorization correction: it preserves the required owner and
DACL policy while removing an unnecessary privilege demand. It does not change
the record algorithm, schema, allowed paths, authority ceiling or accepted
atomic-rotation design.

## Post-Closure Standard-Principal DACL Correction

The first real Party A execution reached exclusive creation and then failed
closed with `DACL_HARDENING_FAILED` / unauthorized `SetAccessControl`. Local
confirmed that both `SPEC_v1.json` and its newly-created directory were removed;
no partial Group 2 source remained.

Root cause: the DACL helper created a fresh security descriptor and explicitly
called `SetOwner` even though the newly-created file was already owned by the
current standard principal. Windows may require `WRITE_OWNER` or
`SeRestorePrivilege` for that redundant owner-section write. The corrected
helper reads and verifies the existing owner SID, constructs only the DACL
section, disables inheritance, adds the bounded ACE set and persists only that
modified access section. It never weakens the non-elevated principal boundary.

The same helper defect existed in the Approver writer, so Local corrected both
surfaces before any Approver execution. Hermetic results after correction:

- Party A spec writer: 49/49 PASS;
- Approver decision writer: 75/75 PASS;
- Python verification-authority suite: 58/58 PASS;
- real Group 2 spec and decision paths: absent before retry.

The new source-level regression fails if `.SetOwner(` reappears. A real
standard-principal retry remains necessary to prove the host authorization
boundary; until then Group 2 is not established and Approver execution remains
closed.

## Independent Probe Evidence

### Returned evidence consumed

- spec writer self-test: 48/48 PASS;
- decision writer self-test: 74/74 PASS;
- corrected Python suite: 58/58 PASS, exit 0;
- worker-return fast gate: COMPLIANT;
- frozen spec-writer hash: MATCH;
- staging: empty;
- real `SPEC_v1.json` and `ACTIVATION_DECISIONS.jsonl`: both absent.

Post-closure correction evidence supersedes only the writer self-test counts:
spec writer 49/49 and decision writer 75/75. The original 48/48 and 74/74 rows
remain historical evidence for the pre-correction closure commit.

### Reviewer probe

The reviewer invoked only three named unittest methods because they directly
answer the work order's admitted decision question.

```text
AtomicRotationTests.test_required_regression_1_atomic_rotation_ends_with_replacement_sole_active
AtomicRotationTests.test_mutating_either_replacement_field_invalidates_digest
PowerShellWriterHermeticSelfTestCrossCheckTests.test_cross_language_atomic_rotation_replay_converges

Ran 3 tests in 0.592s
OK
```

The positive fixture uses exactly `APPROVED(v1) -> ACTIVATED(v1) ->
APPROVED(v2) -> SUPERSEDED(v1,replacement=v2)` and ends with v2 as the sole
active version. Mutation of either durable replacement field fails digest or
closed-schema validation. Independent PowerShell and Python replay converge on
the same final active set.

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| closed event schema | bind replacement version and recomputed hash | T2F contract, writer preimage and Python validator agree | PASS |
| non-supersession fields | both replacement fields explicit null | PowerShell 74/74 and Python 58/58 | PASS |
| atomic swap | one SUPERSEDED event changes old to replacement | reviewer positive probe ends with replacement sole active | PASS |
| ordinary activation | cannot create a second active version | returned negative suite and writer replay reject it | PASS |
| replacement eligibility | greater, approved, inactive, not superseded and hash-matched | returned negative matrix enforces all cases | PASS |
| chained rotation | rotated replacement may later be superseded | PowerShell and Python regressions pass | PASS |
| tamper resistance | either replacement-field mutation invalidates evidence | reviewer tamper probe rejects | PASS |
| cross-language result | PowerShell and Python derive same final state | reviewer cross-language probe converges | PASS |
| real source absence | both operational paths absent | direct `Test-Path` returned false for both | PASS |
| ownership/no commit | exact allowed paths and empty staging | Git reconciliation matches | PASS |

## Risk / Corrective Action

The accepted tooling still controls a privileged local source-establishment
step. Keep real creation and activation outside this commit; execute only under
the already provisioned Party A and Approver principals, preserve exact SID
checks, and perform Local verification before any promotion or admission. If
principal posture, source absence or hash expectations differ at execution
time, stop fail-closed rather than adapting the durable files manually.

## Decision / Disposition

Reviewer verdict: `CLOSED_PASS_BOUNDED`.

The R2 atomic-rotation correction is accepted for repository-local tooling.
The earlier R1 blockers `unreachable-supersession-state`,
`unbound-durable-replacement`, `supersession-entry-gap`, and
`group2-tooling-r2-not-accepted` are resolved.

This acceptance authorizes the next separately controlled Group 2 principal
execution step only after continuity synchronization. It does not itself create
or activate Group 2, and it grants no key promotion, candidate admission,
consumer wiring, provider/live, runtime, public-sync or deployment authority.

## Return-Time Closeability Recheck

closeabilityDisposition: CLOSEABLE

outsideAuthorityBlockers: NONE

nextRepairRoute: N/A with reason: no repair route remains; both localized reviewer repairs are complete and independently verified

workerRedispatchAllowed: NO

## Semantic Convergence Control

Standard: `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-g1-t3b-r2-accepted-atomic-rotation-tooling","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":["acel_g1_group2_real_source_not_created"],"reopened":[],"current":["acel_g1_group2_real_source_not_created"]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[{"claimId":"ACEL-G1-T3B-R2-ATOMIC-ROTATION-CLOSURE","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"governance/compat/test_check_acel_g1_verification_authority_spec.py"}],"requiredDisposition":"READY_WITH_EXECUTABLE_PROOF","successorScope":"EXECUTABLE_IMPLEMENTATION"}
```

## Review Cost Telemetry And Stop Disposition

reviewRoundCount: 2

workerRepairTurnCount: 1

newRootCauseCountThisRound: 0

dependentFindingCountThisRound: 2

providerCallCount: 0

materialCommitCount: 1

continuityCommitCount: 1

elapsedReviewMinutes: NOT_AVAILABLE_WITH_REASON: no trusted reviewer timer is bound to this artifact

tokenOrQuotaUsage: NOT_AVAILABLE_WITH_REASON: no provider-neutral token meter is exposed

valueDelta: independently proved atomic convergence and durable replacement binding while correcting one count claim and two stale comments without another worker round

stopDisposition: COMPLETE_REVIEW

preRepairAuditDisposition: COMPLETE_BEFORE_FIRST_REPAIR

commitPlanDisposition: DEFAULT_ONE_MATERIAL_ONE_CONTINUITY

latencyDisposition: WITHIN_FAST_PATH_TARGET

avoidableDelayClass: NONE

reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| inaccurate Python test count | `WORKER_EXECUTION_ERROR` | `GOVERNANCE_CONTROL_PLANE` | `RULE_EXISTS` | reviewer must bind reported counts to direct command output before closure |
| obsolete R1 comments after R2 algorithm correction | `WORKER_EXECUTION_ERROR` | `GOVERNANCE_CONTROL_PLANE` | `RULE_EXISTS` | keep comments aligned with the same executable state-machine contract |

Machine-check elevation is not justified: both defects are localized and the
existing evidence-integrity/reviewer-local-repair rules already govern them.

Runtime/provider/cost learning lane: N/A_WITH_REASON: local deterministic
tooling review with zero provider calls and no runtime or cost signal.

## Epistemic Process Block

### Expected Result / Prediction

R2 should make the valid replacement only approved before rotation, bind both
replacement identity fields inside the durable event digest, and atomically
end with exactly one active version.

### Evidence Comparison

The returned PowerShell and Python suites pass. The reviewer positive, tamper
and cross-language probes confirm all three decision-changing claims. The only
contradiction was the reported Python count, corrected from 65 to 58 without
changing test behavior.

### Contradiction or Gap Disposition

No material contradiction remains. The count and comment defects were safe
reviewer-local repairs under the accepted design and exact path boundary.

### Claim Update

R2 tooling is accepted bounded. Group 2 operational source establishment is
still absent and remains a separate principal-execution checkpoint.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_review_cost_control.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_independent_review_probe_admission.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | completion-review declaration and telemetry fields, exact independent-probe disposition, SCEC evidence/hash shape, finding defect classes, epistemic labels, machine-closure and export dispositions |
| gateRunPurpose | confirmation after review authoring, not first discovery of required shape |
| claimBoundary | checker conformance cannot replace semantic acceptance or principal execution |

## External/Local Coordination Binding

Role: `LOCAL_REVIEWER`; phase: R2 completion review; decision owner: Local.
External research is closed and supplies no authority in this lane.

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Corpus Completeness And Report Integrity

- Corpus task class: bounded exact-manifest completion review.
- Corpus root: R2 work order, worker return, exact five worker paths and frozen spec writer.
- Snapshot time: 2026-09-20 at closure base `d87a01115`.
- Enumeration command: filesystem-backed direct reads plus exact Git status reconciliation.
- Manifest artifact or inline manifest: exact five-path work-order manifest plus this review and reviewer-owned work-order closure transition.
- Manifest hash: N/A with reason: bounded governed path list; no standalone corpus manifest is created.
- Processing ledger artifact or inline ledger: Target / Source and Acceptance Matrix.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=all named review inputs; ledger_terminal=READ; exclusions=all paths outside this bounded review; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: all paths outside the named bounded review.
- Unreadable or unsupported files: none.
- Aggregation check: exact worker five-path manifest plus reviewer review/work-order transition reconciled.
- Drift check: frozen spec writer hash matches; staging was empty before reviewer closure.
- Output traceability: Target / Source, Independent Probe Evidence and Agent Operation Trace Block.
- Adversarial verification: positive atomic swap, replacement-field tamper and cross-language convergence probes.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: accept and commit the R2 read-only
verification-authority checker/test, and update only the current-authority hash
projection required because the active R2 work order closes in this material
batch.

Protected paths:

- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `governance/compat/check_acel_g1_verification_authority_spec.py`
- `governance/compat/test_check_acel_g1_verification_authority_spec.py`
- `governance/compat/check_task_class_calibration_owner_evidence.py`
- `governance/compat/test_check_task_class_calibration_owner_evidence.py`

The last two paths are pre-existing parked untracked evidence listed only for
changed-set accounting; this batch does not mutate, stage or commit them.

Operator authorization: standing Local orchestrator/reviewer authority plus
the operator's instruction to continue without stopping after the R2 worker
return. Rollback boundary: revert only this R2 tooling closure batch and its
current-authority hash projection if rejected; preserve Group 1 source,
principal provisioning, prior dispatch commits and every parked path.

Not authorized: no real Group 2 source creation, principal execution, key
promotion, candidate admission, provider/live call, public sync, deployment,
or mutation/staging of the thirteen parked paths.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer |
| Provider or surface | private CVF workspace |
| Session or invocation | ACEL-G1-T3B-R2 completion review, 2026-09-20; standard-principal DACL correction, 2026-09-21 |
| Working directory | repository root |
| Command or tool surface | governed reads, direct Python suite, both PowerShell self-tests, three focused independent probes, real-failure rollback inspection, apply_patch, reviewer-fast, Git and closure gates |
| Target paths | exact five R2 worker paths, spec writer, decision writer, R2 work order and this completion review |
| Allowed scope source | R2 work order Review Gate and standing Local reviewer/closer authority |
| Before status evidence | R2 return accepted; first real Party A attempt failed closed at redundant owner rewrite; both real Group 2 paths absent after rollback |
| After status evidence | R2 accepted bounded with count/comment repairs plus shared DACL owner-verification correction; operational retry remains separate |
| Diff evidence | exact three-path post-closure correction, 49/49 and 75/75 PowerShell, 58/58 Python, reviewer-fast 68/68 and pre-commit gate before material commit |
| Approval boundary | tooling closure and next principal-execution routing only |
| Claim boundary | failed principal attempt rolled back completely; no durable Group 2 source, activation, key promotion, admission, provider/live/runtime/public/deployment effect |
| Agent type | Local reviewer/closer |
| Invocation ID | `acel-g1-t3b-r2-atomic-rotation-review-20260920`; `acel-g1-t3b-standard-principal-dacl-correction-20260921` |
| Expected manifest | original R2 closure manifest; post-closure correction limited to both Group 2 writers and this review |
| Actual changed set | exact post-closure three-path material batch reconciled before commit |
| Manifest delta | MATCH |
| Deletion or rename disposition | none |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3B_R2_ATOMIC_ROTATION_CONTRACT_CORRECTION_2026-09-20.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | this completion review | terminal status and `PASS_INDEPENDENT_PROBE` bindings | PASS |
| Roadmap state | active ACEL program continuity | T3B R2 accepted; real Group 2 source remains next | PASS |
| Registry JSON | no registry mutation in scope | exact worker manifest | BLOCKED with reason: GC-051 registry mutation is outside this bounded tooling correction |
| Registry Markdown | no registry mutation in scope | exact worker manifest | BLOCKED with reason: GC-051 registry mutation is outside this bounded tooling correction |
| External evidence digest | no external evidence admitted | internal/local coordination binding | N/A with reason: local repository evidence only |
| System loop interlock | T2F contract, both writers and independent checker | 49/49 spec writer, 75/75 decision writer, 58/58 Python, 3/3 reviewer probes | PASS |
| Session continuity | active handoff and generated session state | separate post-material synchronization | BLOCKED with reason: pending material commit SHA |

## MFRP P4-C1 Observation Disposition

Eligibility: `NO`

Reason: this is a local tooling correction with reviewer-local evidence repair,
not an eligible natural provider-backed phase return. No sample, receipt,
counter, checkpoint or collector mutation is authorized.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance tooling and principal-bound execution preparation;
no public-sync action is authorized.

## Claim Boundary

This review accepts the repository-local R2 atomic-rotation contract and
tooling only. It does not establish or activate the Group 2 source, execute the
approver principal, promote the Party A key, admit a candidate, wire a consumer,
or authorize provider/live/runtime/public/deployment behavior.
