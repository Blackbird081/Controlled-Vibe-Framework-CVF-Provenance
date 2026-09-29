# CVF ACEL G1 T3C-C1 R1 Group 3 Observation Transaction Correction Completion Review

Memory class: governed-review

docType: review

Status: REWORK_REQUIRED

Date: 2026-09-21

Batch ID: ACEL-G1-T3C-C1-R1-GROUP3-OBSERVATION-TRANSACTION-CORRECTION-REVIEW

Review base head: `dcba5f7f017af96ae2f61c1ddc5cbf54fe69945d`

providerExecutionAuthority: FORBIDDEN

successorTrancheOpened: NO

## Purpose

Record Local's independent disposition of the R1 return. R1 closes the five
original findings, but the returned transaction still releases exclusivity
before DACL hardening and final validation, can leak newly created artifacts
on pre-write failure, and does not verify the security descriptor after it is
applied. One consolidated R2 is required before any real Party B execution.

## Target / Source

| Source | Identity / role |
|---|---|
| R1 work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3C_C1_R1_GROUP3_OBSERVATION_TRANSACTION_CORRECTION_2026-09-21.md`; SHA-256 `319dfe6a61973640833f8897d8c1ff239924ef6da5848473ebfed052abcb9e05` |
| R1 worker return | `docs/reviews/CVF_ACEL_G1_T3C_C1_GROUP3_OBSERVATION_LOG_TOOLING_WORKER_RETURN_2026-09-21.md`; SHA-256 `f9b1232c44fe2e91adbe750b58f2fbead03e6922bf491d976a73863ad1fa95d8` |
| reviewed implementation | the exact four uncommitted T3C-C1 worker paths |
| Local evidence | Python `42/42`; checker self-test PASS; PowerShell `31/31`; worker-return fast gate COMPLIANT; real log absent; direct transaction-boundary inspection |

## Scope / Methodology

Local consumed the valid returned suites and did not recreate canonicalization
or record semantics. Review focused on the R1 claims that one exclusive guard
covers the complete transaction, every created artifact is rolled back, and
owner/DACL hardening is verified. The probe was static and contradiction-led:
control-flow ordering and state transitions were inspected directly. No
credentials, alternate principal, real Group 1 read or real Group 3 write was
used.

## Findings / Position

The original findings T3C-C1-RV-1 through RV-5 are accepted as repaired. The
following residual findings block acceptance:

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| T3C-C1-R1-RV-1 | CRITICAL | `Append-ObservationTransaction` disposes the `FileShare.None` stream at line 670, before DACL hardening and full-log validation at lines 676-682. A peer writer can mutate after lock release; a later failure then performs an unlocked rollback and can overwrite that peer's valid append. This contradicts the documented single exclusive transaction. | TRANSACTION_WIDE_GUARD_REQUIRED |
| T3C-C1-R1-RV-2 | HIGH | directory creation occurs before the `try`, while `OpenOrCreate` may create an empty file before `$mutationStarted` becomes true. Any failure before the first append bypasses rollback, leaving a new empty directory or file despite a failed operation. | CREATION_ROLLBACK_BOUNDARY_REQUIRED |
| T3C-C1-R1-RV-3 | HIGH | prior security capture includes only `Access`, and `Protect-ObservationLog` returns immediately after `SetAccessControl` without reading back owner, inheritance protection and exact allowed ACEs. The implementation therefore claims owner/DACL verification without proving the applied postcondition or retaining the full owner/DACL state needed for exact restoration. | SECURITY_POSTCONDITION_AND_RESTORE_REQUIRED |

## Risk / Corrective Action

The current code can lose a concurrent valid append during rollback, leave an
empty source artifact after a failed attempt, or report success without
proving the actual ACL. These are durable-source transaction defects, not
minor documentation issues, so Local will not patch them as reviewer. R2 must
use a transaction-wide exclusion guard that remains held across data write,
security hardening/read-back verification and final chain validation, and
must define rollback ownership from the first filesystem mutation.

## Independent Probe Evidence

| Probe | Observation | Result |
|---|---|---|
| returned Python suite | `42 passed in 0.37s` | RETAINED_PASS |
| checker self-test | published vector/genesis PASS | RETAINED_PASS |
| writer self-test | `31/31 passed` | RETAINED_PASS_BUT_INCOMPLETE_ORACLE |
| worker-return fast gate | COMPLIANT | RETAINED_STRUCTURAL_PASS |
| real source absence | `Test-Path .../LOG.jsonl` -> `False` | PASS |
| lock-order probe | `$stream.Dispose()` precedes `Protect-ObservationLog` and final checker | CONTRADICTION_FOUND |
| creation-boundary probe | directory/OpenOrCreate precede `$mutationStarted = $true`; catch rollback is conditional on that flag | CONTRADICTION_FOUND |
| ACL proof probe | only Access is captured; no post-`SetAccessControl` read-back exists | CONTRADICTION_FOUND |

## Decision / Disposition

`REWORK_REQUIRED`.

One consolidated internal R2 is authorized. The four implementation outputs
remain unaccepted and uncommitted. Party B execution, the real Group 3 source,
Party C/Group 4 and T3E remain closed.

## Semantic Convergence Outcome

Standard: `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-g1-t3c-c1-group3-observation-log-tooling-problem","chainMode":"SUCCESSOR","chainOrdinal":3,"predecessor":{"path":"docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3C_C1_R1_GROUP3_OBSERVATION_TRANSACTION_CORRECTION_2026-09-21.md","sha256":"319dfe6a61973640833f8897d8c1ff239924ef6da5848473ebfed052abcb9e05"},"blockerDelta":{"prior":["REAL_OBSERVATION_PENDING","PARTY_C_AND_GROUP4_PENDING","T3E_PENDING","T3C_C1_R1_NOT_ACCEPTED"],"resolved":["T3C_C1_R1_NOT_ACCEPTED"],"retained":["REAL_OBSERVATION_PENDING","PARTY_C_AND_GROUP4_PENDING","T3E_PENDING"],"new":["transaction-wide-exclusion-gap","pre-write-artifact-rollback-gap","security-postcondition-proof-gap"],"reopened":[],"current":["REAL_OBSERVATION_PENDING","PARTY_C_AND_GROUP4_PENDING","T3E_PENDING","transaction-wide-exclusion-gap","pre-write-artifact-rollback-gap","security-postcondition-proof-gap"]},"resolutionEvidence":{"T3C_C1_R1_NOT_ACCEPTED":{"evidenceClass":"ACCEPTED_REVIEW","evidencePath":"docs/reviews/CVF_ACEL_G1_T3C_C1_GROUP3_OBSERVATION_LOG_TOOLING_WORKER_RETURN_2026-09-21.md","sha256":"f9b1232c44fe2e91adbe750b58f2fbead03e6922bf491d976a73863ad1fa95d8","locator":"## Findings / Position"}},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":2,"nonDecreasingBlockerTransitions":1},"claims":[{"claimId":"ACEL-G1-T3C-C1-R1-COMPLETION-REVIEW","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"docs/reviews/CVF_ACEL_G1_T3C_C1_R1_GROUP3_OBSERVATION_TRANSACTION_CORRECTION_COMPLETION_2026-09-21.md"}],"requiredDisposition":"ROOT_CONTRACT_REQUIRED","successorScope":"INTEGRATED_ROOT_CONTRACT"}
```

## Finding-To-Governance Learning Disposition

| Finding group | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| incomplete transaction lifetime and artifact ownership | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | R2 names transaction start/end, guard lifetime and failure-before-first-write tests explicitly; include in the already parked CVF foundation-learning tranche after tooling acceptance |
| ACL set-without-read-back proof | WORKER_EXECUTION_ERROR | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | require exact security descriptor read-back oracle in R2; promote on confirmed recurrence |

## Epistemic Process Block

### Expected Result / Prediction

R1 was expected to hold one exclusive transaction from locked-state selection
through DACL verification and final validation, and to leave no artifact on
any failed new-file attempt.

### Evidence Comparison

The returned suites validate exact append and injected rollback after the
first write. Direct control-flow evidence instead shows the lock ends before
the last two transaction phases and rollback ownership begins too late.

### Contradiction Or Gap Disposition

The five original repairs and their evidence are retained. The broader
transaction-completeness claim is rejected pending R2.

### Claim Update

The tooling is corrected at record level but is not yet safe for durable
multi-process source creation or real Party B use.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_acel_g1_registry_observation_log.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | review status; finding class/lane/disposition; epistemic comparison; trace; no-commit and public disposition |
| gateRunPurpose | preserve a bounded evidence-backed R1 rejection and issue one coherent R2 |
| claimBoundary | machine PASS does not prove transaction-wide mutual exclusion or applied ACL state |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | R1 work order and worker return | exact hashes above | PASS |
| Completion or reviewer artifact | this review | `REWORK_REQUIRED` | PASS |
| Roadmap state | current ACEL continuity | no tranche closure | N/A with reason |
| Registry JSON | real Group 3 log absent | `False` probe | N/A with reason |
| Registry Markdown | no registry owner change | no mutation | N/A with reason |
| External evidence digest | local bounded review only | no external evidence | N/A with reason |
| System loop interlock | Party B observation checkpoint | remains closed | PASS |
| Session continuity | active handoff/state | separate dispatch sync | PENDING_SEPARATE_SYNC |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | CVF Local orchestrator/reviewer |
| Provider or surface | local private provenance repository |
| Session or invocation | ACEL G1 T3C-C1 R1 completion review, 2026-09-21 |
| Working directory | repository root |
| Command or tool surface | governed reads, retained test execution, direct source-order inspection, git and apply_patch |
| Target paths | exact four R1 outputs; this review; paired R2 dispatch artifacts |
| Allowed scope source | committed R1 work order and operator's standing review/delegation authority |
| Before status evidence | HEAD `dcba5f7f017af96ae2f61c1ddc5cbf54fe69945d`; thirteen parked paths plus four worker paths; staging empty |
| After status evidence | R1 rejected; R2 packet prepared; worker and parked paths otherwise untouched |
| Diff evidence | three residual transaction/security findings consolidated |
| Approval boundary | review and corrective dispatch only |
| Claim boundary | no credentials, Party B, real source, provider/live/public/deployment effect |
| Agent type | independent Local reviewer/orchestrator |
| Invocation ID | `acel-g1-t3c-c1-r1-completion-review-2026-09-21` |
| Expected manifest | this review plus paired R2 baseline/work order |
| Actual changed set | this review plus paired R2 baseline/work order |
| Manifest delta | MATCH before dispatch commit |
| Deletion or rename disposition | none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private implementation review and corrective dispatch; no public-sync
authority or artifact is claimed.

## Claim Boundary

This review accepts only the five narrow R1 repairs and rejects R1 completion.
It authorizes one bounded R2 correction, not credentials, alternate-user
execution, a real registry read, real Group 3 creation, Party C/Group 4, T3E,
candidate admission, worker commit or provider/live/public/deployment effects.
