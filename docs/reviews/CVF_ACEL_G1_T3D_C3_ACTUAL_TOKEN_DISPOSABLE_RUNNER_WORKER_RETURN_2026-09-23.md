# CVF ACEL G1 T3D-C3 Actual-Token Disposable Runner Worker Return

Memory class: FULL_RECORD

docType: review

Status: COMPLETE_PENDING_REVIEW

Date: 2026-09-23

Batch ID: ACEL-G1-T3D-C3-ACTUAL-TOKEN-DISPOSABLE-RUNNER

Self-declared worker-return artifact: yes

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C3_ACTUAL_TOKEN_DISPOSABLE_RUNNER_2026-09-23.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C3_ACTUAL_TOKEN_DISPOSABLE_RUNNER_2026-09-23.md`

executionBaseHead: `edcf63a45d0fd51339a1c4527468d7fab5803a91`

rawMemoryReleased=false

providerExecutionAuthority: FORBIDDEN

contractProfile: WORKER_RETURN_FULL_GATE_V1

independentProbeDisposition: PENDING_REVIEWER_EXECUTION

terminalReadinessVerdict: READY_FOR_REVIEW

## Rework Convergence Self-Proof

rootCauseClusterId: acel-g1-t3d-c3-actual-token-disposable-runner

reworkGeneration: 1

consolidatedDefectClassSweep: COMPLETE_ALL_KNOWN_DEPENDENCIES

productionBindingEvidence: scripts/acel_g1_group4_actual_token_coordinator.ps1 sha256 11b449af03b8504682add9cb39c77fe03b9be4b2ac65c9069810358418f3290f; scripts/acel_g1_group4_actual_token_principal_probe.ps1 sha256 8a3ab4acfe62ed9eb02194279a836e08b53251e63a07e87ee03b0ebc4a3c28d9; scripts/acel_g1_group4_actual_token_local_finalizer.ps1 sha256 a35726e6f5bbd922f0af4c07f036a10ca669de6d4acee163c7dc4f34e8e5b43d

adversarialRegressionDisposition: PASS_TARGETED_DEFECT_CLASS

successorTrancheOpened: NO

implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY

internalAgentInvocationCount: 1

externalAgentInvocationCount: 0

providerCallCount: 0

tokenOrQuotaUsage: NOT_AVAILABLE_WITH_REASON: the local worker surface exposes no provider meter; usage is unknown, not zero

## Purpose

Implement the committed four-path T3D-C3 runner manifest. The result prepares
a disposable-root packet, a principal-bound probe surface and a Local-only
finalizer. It does not run Party B/C, request credentials, touch the real Group
4 source or claim actual-token proof.

## Target / Source

Authority is the committed baseline and work order at dispatch commit
`4b68fa465`, with execution continuity at `edcf63a45`. Controlling semantics
remain the C0-R1 matrix, the static proof packet, the C1-R2 accepted hermetic
transaction primitives and the post-closure readiness audit named by the work
order.

## Scope / Methodology

Role: same-thread Local implementation role, classified `INTERNAL_AGENT`.
This role switch is disclosed and is not an independent reviewer actor.
Mutation is limited to the exact four required paths. After the initial
return, the same Local actor switched to a reviewer/fixer phase, found
executable contradictions, corrected them inside the allowed manifest, and
ran a separate execution/assertion path. That activity is correction evidence,
not independent-actor acceptance. The implementation was tested only with the current Windows token under
`%TEMP%\cvf-g4-actual-token-test-*`; no Party B/C process was started.

Method:

1. run the clean execution-base pre-implementation gate;
2. implement strict disposable containment and reparse/real-source rejection;
3. generate 22 hash-bound envelopes with one isolated fixture per role/action;
4. bind exact role/name/SID/non-elevated checks in the principal probe;
5. make TestPolicy permanently inadmissible to the public finalizer;
6. validate missing, duplicate, altered-binding and residue failures;
7. run a real second `pwsh` child with a six-event barrier and hard-terminate
   another child after guard acquisition, then prove successor acquisition;
8. have the Local finalizer recompute postconditions and compare live fixture
   state rather than trusting the evidence's boolean claim.

## Findings / Position

| ID | Result | Evidence |
|---|---|---|
| T3D-C3-01 | Coordinator creates one direct `%TEMP%` child only, rejects repo/home/real-source ancestors, pre-existing roots and reparse traversal. | coordinator self-test 9/9 |
| T3D-C3-02 | Matrix is closed at 22 unique role/action rows; every row owns an isolated fixture and exact prestate, and every envelope has a SHA-256 receipt. | `G4-COORDINATOR-MATRIX-22`, `UNIQUE`, `PRESTATE`, `ENVELOPE-HASHES` |
| T3D-C3-03 | Probe rejects envelope tampering, wrong SID, elevation and real-source paths; actual adversarial fixtures cover reparse, hardlink, sibling and security drift; TestPolicy records cannot become actual proof. | principal 7/7; finalizer 6/6; reviewer execution 22/22 |
| T3D-C3-04 | Principal surface has no password parameter and coordinator emits no credential field or automatic account switch. | parameter/source inspection; `G4-COORDINATOR-NO-CREDENTIALS` |
| T3D-C3-05 | A real child attempts the same guard behind the six-event barrier; a separate real child is hard-terminated after acquisition and a successor acquires the abandoned guard. | reviewer-observed 22/22 execution; `READY`, `START_ATTEMPT`, `ATTEMPTING`, `PARENT_RELEASE`, `ENTERED`, `COMPLETE` |
| T3D-C3-06 | Finalizer accepts only the complete unique matrix with exact envelope/evidence bindings, exact identity/outcome, recomputed action postconditions, live-state equality, link count one, security equality and no residue. | finalizer 6/6; altered binding independently rejected |
| T3D-C3-07 | Actual-token evidence remains absent. | `independentProbeDisposition: PENDING_REVIEWER_EXECUTION`; all executed packets were `testPolicy=true` |

Initial reviewer contradiction: only 14/22 generated commands succeeded. The
positive publication read an overbroad security section, four adversarial rows
used no actual fixtures, concurrency had no contending peer, crash used a
catchable exception, and finalization trusted `postconditionsVerified`.
Reviewer/fixer corrections produced a fresh 22/22 packet, a public
`INCONCLUSIVE_OR_FAILED` verdict with only
`TEST_POLICY_EVIDENCE_INADMISSIBLE`, and an altered-binding rejection. This is
same-actor correction evidence and must not be relabelled independent review.

## Risk / Corrective Action

The principal and ACL paths are high-risk Windows tooling. Current-token
self-tests and the separate reviewer execution path validate structure,
containment and fail-closed adjudication, not the effective rights of Party
B/C and not independent-actor review. A distinct reviewer actor must run the
admitted probe before accepting the implementation. Any mismatch, missing matrix row,
unexpected success, token elevation, residue or inability to reproduce the
exact candidate DACL keeps the result `INCONCLUSIVE_OR_FAILED` and keeps the
operator checkpoint closed.

## Decision / Disposition

`COMPLETE_PENDING_REVIEW`. Implementation is ready for Local review. It is not
actual-token proof and does not open the operator checkpoint.

## Operator Role-Switch Authorization

On 2026-09-23 the operator explicitly authorized the existing Codex
implementation to be retained and the same actor to switch into the Local
reviewer/closer role for this material result. This one-time authorization
permits material commit ownership; it does not convert the same-thread probe
into independent-actor evidence, does not change
`independentProbeDisposition: PENDING_REVIEWER_EXECUTION`, and does not open
Party B/C execution, actual-token proof, Group 4 source creation or T3E.

Accepted risk: same-actor confirmation bias remains possible despite the
separate 22-command execution/assertion path. Compensating evidence is the
22/22 fresh packet, tamper rejection, fail-closed TestPolicy verdict,
reviewer-fast gate and full pre-commit gate. Follow-up owner: Local
orchestrator must obtain distinct-actor review before any terminal
actual-token acceptance or source-authority claim.

## Claim Boundary

Claimed: bounded implementation plus 22 current-token hermetic self-tests.
Not claimed: independent actor review, Party B/C execution, password handling,
actual Windows shared-parent feasibility, real Group 4 source creation, issuer
observation, lookup response, T3E, provider/live/runtime/public/deployment or
production readiness.

## Changed Files

| Path | Status | SHA-256 | Purpose |
|---|---|---|---|
| `scripts/acel_g1_group4_actual_token_coordinator.ps1` | NEW | `11b449af03b8504682add9cb39c77fe03b9be4b2ac65c9069810358418f3290f` | setup, isolated fixtures, matrix and command packet |
| `scripts/acel_g1_group4_actual_token_principal_probe.ps1` | NEW | `8a3ab4acfe62ed9eb02194279a836e08b53251e63a07e87ee03b0ebc4a3c28d9` | exact-token bounded probe |
| `scripts/acel_g1_group4_actual_token_local_finalizer.ps1` | NEW | `a35726e6f5bbd922f0af4c07f036a10ca669de6d4acee163c7dc4f34e8e5b43d` | Local fail-closed adjudication with recomputed postconditions |
| `docs/reviews/CVF_ACEL_G1_T3D_C3_ACTUAL_TOKEN_DISPOSABLE_RUNNER_WORKER_RETURN_2026-09-23.md` | NEW | detached hash captured immediately before and after final required gate | this return |

## Command Evidence

| Command | Result |
|---|---|
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base edcf63a45 --head HEAD` before edits | PASS 85/85 |
| coordinator `-SelfTest` | PASS 9/9; 22 planned matrix rows; no principal process |
| principal probe `-SelfTest` | PASS 7/7; real child process; TestPolicy only |
| Local finalizer `-SelfTest` | PASS 6/6; public TestPolicy disposition `INCONCLUSIVE_OR_FAILED` |
| fresh same-actor reviewer packet | PASS 22/22 commands; zero failed rows; no Party B/C token |
| public finalizer on fresh packet | `INCONCLUSIVE_OR_FAILED`; sole reason `TEST_POLICY_EVIDENCE_INADMISSIBLE` |
| altered evidence binding | `INCONCLUSIVE_OR_FAILED`; envelope binding mismatch detected for Party C publication |
| reviewer disposable-root cleanup | exact target verified and removed; post-cleanup `Test-Path=False` |
| `python governance/compat/check_governed_file_size.py --enforce` | COMPLIANT |
| `git diff --check` | PASS |

Final worker-return fast-gate and detached pre/post return-hash equality are
recorded after this artifact becomes byte-final; no edit is permitted between
those two hash captures.

## No-Commit Statement

WORKER_MUST_NOT_COMMIT honored. The implementation role staged and committed
nothing. Commit ownership remains Local reviewer/closer.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/run_worker_return_fast_gate.py`; `governance/compat/check_high_risk_local_transaction_proof.py`; `governance/compat/check_forbidden_filesystem_state.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | worker-return headings and scalars, exact manifest, high-risk JSON echo, trace labels, TestPolicy claim boundary, independent probe pending |
| gateRunPurpose | confirm byte-final returned evidence, not create source or actual-token proof |
| claimBoundary | bounded local tooling implementation only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | same-thread Local implementation role |
| Provider or surface | private CVF shared workspace; local shell only |
| Session or invocation | ACEL G1 T3D-C3 runner implementation, 2026-09-23 |
| Working directory | repository root |
| Command or tool surface | governed source reads, apply_patch, PowerShell self-tests, Python governance gates and read-only Git |
| Target paths | exact four Required Artifact Manifest paths |
| Allowed scope source | committed dispatch `4b68fa465` and continuity `edcf63a45` |
| Before status evidence | clean worktree at execution base `edcf63a45d0fd51339a1c4527468d7fab5803a91`; staged set empty |
| After status evidence | exact four create-only paths pending; staged set empty |
| Diff evidence | `git diff --name-status` plus `git status --short --untracked-files=all`; exact four-path manifest |
| Approval boundary | current-token hermetic implementation and tests only |
| Claim boundary | no Party B/C, credential, real source, T3E or provider effect |
| Agent type | INTERNAL_AGENT implementation role |
| Invocation ID | `acel-g1-t3d-c3-local-worker-20260923` |
| Expected manifest | three scripts plus this worker return |
| Actual changed set | same four paths |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | disposable setup packet, principal probe contract and Local finalizer |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: three JSON self-test summaries, exact script hashes and final gate receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT: current-token disposable fixture mutations only |
| invocationBoundary | cooperative PowerShell scripts under the current Local token |
| interceptionBoundary | no account-switch, password, shell interception, provider or runtime claim |
| claimLanguage | hermetic tooling ready for Local review; actual-token proof pending |
| forbiddenExpansion | Party B/C execution, real source, T3E, provider/live/public/deployment and automatic successor |

## Semantic Convergence Outcome

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-g1-t3d-c3-actual-token-disposable-runner","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":["ACTUAL_TOKEN_ENTRYPOINT_MISSING","ACTUAL_TOKEN_PROOF_PENDING","GROUP4_SOURCE_NOT_CREATED","T3E_NOT_OPEN"],"resolved":["ACTUAL_TOKEN_ENTRYPOINT_MISSING"],"retained":["ACTUAL_TOKEN_PROOF_PENDING","GROUP4_SOURCE_NOT_CREATED","T3E_NOT_OPEN"],"new":[],"reopened":[],"current":["ACTUAL_TOKEN_PROOF_PENDING","GROUP4_SOURCE_NOT_CREATED","T3E_NOT_OPEN"]},"resolutionEvidence":{"ACTUAL_TOKEN_ENTRYPOINT_MISSING":{"evidenceClass":"EXECUTABLE_PROOF","evidencePath":"scripts/acel_g1_group4_actual_token_coordinator.ps1","sha256":"11b449af03b8504682add9cb39c77fe03b9be4b2ac65c9069810358418f3290f","locator":"function New-ProofPacket","claimId":"T3D-C3-HERMETIC-SELFTESTS"}},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":1,"nonDecreasingBlockerTransitions":0},"claims":[{"claimId":"T3D-C3-HERMETIC-SELFTESTS","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"three script -SelfTest receipts, 22/22"},{"claimId":"T3D-C3-SEPARATE-EXECUTION-PATH","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"fresh 22-command packet, TestPolicy fail-closed and tamper rejection"}],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"NO_SUCCESSOR"}
```

The implementation entrypoint now exists. Independent-actor review and actual
Party B/C execution remain separate blockers; no source or T3E claim opens.

## Machine Closure Package

```json
{"schemaVersion":"cvf.machineClosurePackage.v1","batchId":"ACEL-G1-T3D-C3-ACTUAL-TOKEN-DISPOSABLE-RUNNER","status":"COMPLETE_PENDING_REVIEW","executionBaseHead":"edcf63a45d0fd51339a1c4527468d7fab5803a91","changedPathCount":4,"testDisposition":"PASS_22_OF_22_CURRENT_TOKEN_HERMETIC","actualTokenProof":"NOT_EXECUTED","independentProbeDisposition":"PENDING_REVIEWER_EXECUTION","commitDisposition":"WORKER_MUST_NOT_COMMIT"}
```

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Internal source | `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C3_ACTUAL_TOKEN_DISPOSABLE_RUNNER_2026-09-23.md` |
| Chain map route | N/A with reason: direct internal implementation from committed CVF sources |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | C0-R1 contract, T3D-C3 work order and these bounded scripts |
| Disposition | local first-party implementation only |
| Claim boundary | no external source or provider authority |

## External/Local Coordination Binding

Role: `INTERNAL_AGENT`; phase: bounded local implementation; decision owner:
Local reviewer. External research is closed and supplies no private-CVF proof.

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: three bounded scripts can prepare a reproducible
22-row proof packet and fail closed without starting alternate principals.

Evidence Comparison Requirement: the 22 hermetic tests matched that bounded
prediction; actual-token behavior remains unknown.

Contradiction Handling Requirement: any reviewer contradiction blocks
acceptance and leaves the operator checkpoint closed.

Claim Update Requirement: implementation is review-ready; actual-token proof
is still pending.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: machine-specific principal and ACL tooling is private and unreviewed;
no public-sync authority exists.

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: N/A with reason: this return is not a corpus rescan, intake refresh or
source-backed reassessment output.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - this is an exact named-source
  implementation; no corpus enumeration, inventory, or coverage claim is made.

## Finding-To-Governance Learning Disposition

| Observation | Classification | Disposition |
|---|---|---|
| TestPolicy evidence could otherwise look structurally complete | recurring false-assurance risk | machine-blocked in finalizer; candidate for later CVF learning only after review |
| same-thread role switch is not independent actor review | reviewer-independence boundary | explicitly retained; no new rule needed |
| generated commands initially passed only 14/22 | worker execution error plus insufficient first-pass oracle | repaired with isolated adversarial fixtures, real peer/crash children and postcondition recomputation; fresh packet 22/22 |
| evidence-owned `postconditionsVerified` was trusted | false-assurance implementation defect | Local finalizer now recomputes expected postconditions and compares live state |
| failed early self-tests left disposable ACL residue | bounded implementation defect | repaired by keeping TestPolicy on inherited current-token ACLs; exact temp roots were verified and removed; final residue count zero |

No foundation promotion is claimed by this worker return.

## High-Risk Local Transaction Proof Echo

High-Risk Local Transaction Proof Applicability: REQUIRED

```json
{"transactionTarget":"disposable Group 4 reservation publication, denial matrix, evidence capture and exact recovery","productionPathPeer":{"kind":"REAL_SECOND_PROCESS","invocationPath":"scripts/acel_g1_group4_actual_token_principal_probe.ps1","mutationPath":"role-bound disposable reservation transaction and negative operation matrix"},"deterministicBarrierProtocol":{"events":["READY","START_ATTEMPT","ATTEMPTING","PARENT_RELEASE","ENTERED","COMPLETE"],"timeoutRole":"DEADLOCK_SAFETY_ONLY"},"enteredBeforeReleaseOracle":"REJECT_ENTRY_BEFORE_PARENT_RELEASE","postAcquireFailureInjection":{"point":"AFTER_ACQUIRE_BEFORE_MUTATION","cleanupProof":"SUBSEQUENT_PEER_ACQUIRES"},"semanticSecurityTuple":{"fields":["ownerSid","protectionState","inheritanceState","aces"],"aceFields":["sid","rights","accessType","isInherited","inheritanceFlags","propagationFlags"],"normalization":"SORT_COMPLETE_ACE_TUPLES"},"rollbackExactness":{"comparison":"SEMANTIC_PRESTATE_EQUALS_POST_ROLLBACK","adversaries":["EXTRA_ALLOW","DENY","INHERITED","WRONG_OWNER"]},"finalEvidenceHashBinding":{"algorithm":"SHA256","scope":"EXACT_RETURN_BYTES","capture":"BEFORE_AND_AFTER_FINAL_REQUIRED_GATE","equality":"REQUIRED","postGateMutation":"FORBIDDEN"},"independentProbeRequired":{"required":true,"owner":"LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER","workerReturnDisposition":"PENDING_REVIEWER_EXECUTION"}}
```

## Return-Time Closeability Recheck

Worker-owned focused tests pass, and the same actor's separate reviewer path
found and corrected the initial contradictions. Independent-actor probe,
reviewer-fast, pre-commit, terminal completion decision and commits remain
pending. No independent-review blocker is self-closed by this return.

closeabilityDisposition: CLOSEABLE

outsideAuthorityBlockers: NONE

nextRepairRoute: N/A

workerRedispatchAllowed: NO

## Worker Experience Retrospective

WORKER_EXPERIENCE_RETRO:
- frictionLevel: MEDIUM
- frictionType: GATE_SURPRISE
- observedStep: the first worker-return fast gate found required packet-shape fields that were not present in the initial return draft; the three implementation self-tests themselves remained green.
- preventiveControlCandidate: WORK_ORDER_TEMPLATE

## No-Secret / No-Principal Execution Statement

No password, API key, credential prompt, account modification, `runas`, Party B
process or Party C process was used. Provider call count is zero. Token/quota
usage is not available from this local shell and is not represented as zero.

## git status --short

```text
?? docs/reviews/CVF_ACEL_G1_T3D_C3_ACTUAL_TOKEN_DISPOSABLE_RUNNER_WORKER_RETURN_2026-09-23.md
?? scripts/acel_g1_group4_actual_token_coordinator.ps1
?? scripts/acel_g1_group4_actual_token_local_finalizer.ps1
?? scripts/acel_g1_group4_actual_token_principal_probe.ps1
```
