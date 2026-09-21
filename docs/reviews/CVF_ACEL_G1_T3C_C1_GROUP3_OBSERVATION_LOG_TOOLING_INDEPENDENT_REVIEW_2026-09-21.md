# CVF ACEL G1 T3C-C1 Group 3 Observation-Log Tooling Independent Review

Memory class: governed-review

docType: review

Status: REWORK_REQUIRED

Date: 2026-09-21

Batch ID: ACEL-G1-T3C-C1-GROUP3-OBSERVATION-LOG-TOOLING-REVIEW

Review base head: `2b171c8c57a7d7e7646711ae47e04f59736ed94d`

providerExecutionAuthority: FORBIDDEN

successorTrancheOpened: NO

## Purpose

Record Local's independent review of the four uncommitted T3C-C1 worker
outputs and define one consolidated R1 correction. The review consumes valid
worker evidence but tests the contract-sensitive append, transaction, chain
and exact-manifest seams separately. It does not run as Party B, read the real
Group 1 registry or create the real Group 3 log.

## Target / Source

| Source | Identity / role |
|---|---|
| governing work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3C_C1_GROUP3_OBSERVATION_LOG_TOOLING_2026-09-21.md` |
| worker return | `docs/reviews/CVF_ACEL_G1_T3C_C1_GROUP3_OBSERVATION_LOG_TOOLING_WORKER_RETURN_2026-09-21.md` |
| operational source contract | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md`; Source Group 3 |
| returned code | `scripts/acel_g1_party_b_group3_observation_writer.ps1`; `governance/compat/check_acel_g1_registry_observation_log.py`; focused test |
| worker evidence | 38/38 Python tests, checker self-test, 21/21 PowerShell self-test and worker-return fast gate all reported passing |

## Scope / Methodology

Local retained the worker's passing evidence for unaffected canonicalization,
strict decoding, identity and hash checks. Review then inspected the durable
append boundary, lock placement, rollback path, checker/parser correspondence
and exact output manifest. This is a bounded contradiction-driven review, not
a broad duplicate rerun. No credentials, alternate-user execution or real
source path were used.

## Findings / Position

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| T3C-C1-RV-1 | CRITICAL | `Add-ObservationLogLine` builds `combined = existingBytes + newLineBytes`, seeks to end of the existing file, then writes all of `combined`. Every non-genesis append therefore produces `existingBytes + existingBytes + newLineBytes`, duplicating the prior chain and making the durable log invalid. | EXACT_APPEND_CORRECTION_REQUIRED |
| T3C-C1-RV-2 | CRITICAL | the writer appends and flushes before `Protect-ObservationLog`. If ownership/DACL hardening fails, the appended/new file remains; there is no restoration of prior bytes or removal of a newly created file. This contradicts transactional and fail-closed requirements. | TRANSACTION_ROLLBACK_REQUIRED |
| T3C-C1-RV-3 | HIGH | chain validation and `priorEntryHashHex` selection happen before the exclusive file lock. The lock checks only length, so a same-length replacement is undetected and any concurrent content change can make the new row bind stale state. The full existing chain is not revalidated from the exact locked bytes before append. | LOCKED_COMPARE_AND_APPEND_REQUIRED |
| T3C-C1-RV-4 | HIGH | `_parse_log_records` documents blank-line rejection but executes `continue` for every blank/whitespace line. A JSONL source with non-record lines is silently normalized instead of rejected. | STRICT_JSONL_LINE_REJECTION_REQUIRED |
| T3C-C1-RV-5 | HIGH | the append self-test asserts only growth and prefix preservation, so the duplication defect passes. Separately, the original dispatch says exact four paths but also declares `evidenceReadinessContract: REQUIRED_V1`; the return created three unauthorized support paths and still called the manifest `MATCH`. | REGRESSION_AND_PACKET_RECONCILIATION_REQUIRED |

## Risk / Corrective Action

Acceptance would authorize a first real append that appears successful, while
the second append corrupts the chain and a DACL failure can leave an
unauthorized durable mutation behind. One R1 must repair all findings together
and add regressions that fail on the returned implementation. The three
manifest-excess support files are removed by Local as reviewer packaging
cleanup; the worker must keep the exact original four-path implementation
manifest and correct the existing return in place.

## Consolidated Correction Contract

1. Preserve the exact four worker-owned paths from the initial work order.
2. Under one exclusive transaction, obtain the exact current bytes, validate
   the exact locked chain, derive the current last hash, reject duplicate IDs,
   append exactly one UTF-8-no-BOM JSON line, harden and verify ownership/DACL,
   then report success.
3. A non-empty file's bytes may change only from `oldBytes` to
   `oldBytes + newLineBytes`; never rewrite or duplicate `oldBytes`.
4. On any failure after mutation begins, restore exact prior bytes and prior
   security descriptor for an existing file, or remove the new file and any
   newly created empty directory. If rollback itself fails, emit a distinct
   terminal rollback-failure taxonomy and never claim success.
5. Detect same-length replacement and every other stale-read race by comparing
   content identity, not length alone. Chain selection and append must use the
   same locked byte snapshot.
6. Reject every interior or leading blank/whitespace JSONL line. A single
   optional terminal newline is framing, not an extra line. Checker docs,
   behavior and tests must agree.
7. Add tests for exact two-line byte equality, three sequential appends,
   same-length concurrent replacement, DACL failure rollback for both new and
   existing files, post-write validation failure rollback, blank-line reject,
   and no mutation for every negative.
8. Remove the invalid Evidence Readiness Binding from the worker return. State
   `NOT_APPLICABLE_WITH_REASON` because this is bounded implementation review,
   not a discovery/corpus audit. Report exactly four outputs and retain
   `independentProbeDisposition: PENDING_REVIEWER_EXECUTION`.

## Decision / Disposition

`REWORK_REQUIRED`.

One consolidated internal R1 dispatch is authorized. Current implementation
outputs remain unaccepted and uncommitted. Real Party B execution, Group 3
source establishment, Party C provisioning, Group 4 and T3E remain closed.

## Semantic Convergence Outcome

Standard: `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-g1-t3c-c1-group3-observation-log-tooling-problem","chainMode":"SUCCESSOR","chainOrdinal":1,"predecessor":{"path":"docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3C_C1_GROUP3_OBSERVATION_LOG_TOOLING_2026-09-21.md","sha256":"8d387360b55bed3b1367536ed037218cd4e79d048537bcb19bb73ba94e0fd607"},"blockerDelta":{"prior":["REAL_OBSERVATION_PENDING","PARTY_C_AND_GROUP4_PENDING","T3E_PENDING"],"resolved":[],"retained":["REAL_OBSERVATION_PENDING","PARTY_C_AND_GROUP4_PENDING","T3E_PENDING"],"new":["exact-append-corruption","transaction-rollback-gap","locked-chain-race-gap","strict-jsonl-gap","return-manifest-gap"],"reopened":[],"current":["REAL_OBSERVATION_PENDING","PARTY_C_AND_GROUP4_PENDING","T3E_PENDING","exact-append-corruption","transaction-rollback-gap","locked-chain-race-gap","strict-jsonl-gap","return-manifest-gap"]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":1,"nonDecreasingBlockerTransitions":1},"claims":[{"claimId":"ACEL-G1-T3C-C1-INDEPENDENT-REVIEW","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"docs/reviews/CVF_ACEL_G1_T3C_C1_GROUP3_OBSERVATION_LOG_TOOLING_INDEPENDENT_REVIEW_2026-09-21.md"}],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INITIAL_BOUNDED"}
```

## Finding-To-Governance Learning Disposition

| Finding group | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| weak append oracle and post-write rollback gap | WORKER_EXECUTION_ERROR | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | require exact-byte multi-append and forced-failure rollback regressions in R1; promote only on recurrence |
| contradictory four-path/evidence-readiness dispatch | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | R1 fixes evidence readiness to not applicable and makes exact-manifest reconciliation explicit |

## Epistemic Process Block

### Expected Result / Prediction

The worker's broad hermetic suite was expected to validate record semantics;
the highest-risk independent seam was whether the durable append transaction
preserved exact old bytes and rolled back all later failures.

### Evidence Comparison

Returned tests passed, but direct source inspection contradicts the append
claim: the code writes the old bytes a second time. The same control flow has
no rollback around later DACL hardening. Parser prose also says blank lines are
rejected while its executable branch skips them.

### Contradiction Or Gap Disposition

Passing canonicalization and checker evidence is retained. Durable append,
fail-closed transaction and strict JSONL claims are rejected pending R1.

### Claim Update

The tooling is substantially implemented but not safe for real Party B use.
No source readiness or establishment claim is made.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_machine_closure_package.py` |
| literalTokensReviewed | governed review headings; finding class/lane/disposition; epistemic comparison/gap/update; trace; public disposition; closure rows |
| gateRunPurpose | preserve one evidence-backed consolidated rejection without recreating implementation |
| claimBoundary | structural PASS cannot accept tooling or authorize real source execution |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | initial T3C-C1 order plus R1 | five consolidated findings | PASS |
| Completion or reviewer artifact | this review | `REWORK_REQUIRED` | PASS |
| Roadmap state | current ACEL continuity | no tranche closure | N/A with reason |
| Registry JSON | real Group 3 log remains absent | no mutation | N/A with reason |
| Registry Markdown | no registry owner change | no mutation | N/A with reason |
| External evidence digest | local bounded review only | no external evidence | N/A with reason |
| System loop interlock | Party B observation checkpoint | remains closed | PASS |
| Session continuity | active continuity surfaces | separate dispatch sync | PENDING_SEPARATE_SYNC |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | CVF Local orchestrator/reviewer |
| Provider or surface | local private provenance repository |
| Session or invocation | ACEL G1 T3C-C1 independent review, 2026-09-21 |
| Working directory | repository root |
| Command or tool surface | governed reads, focused test consumption, source inspection, git and apply_patch |
| Target paths | four uncommitted T3C-C1 outputs; this review; paired R1 dispatch artifacts |
| Allowed scope source | operator authorized Local review and correction dispatch; initial work order assigns independent review |
| Before status evidence | HEAD `2b171c8c57a7d7e7646711ae47e04f59736ed94d`; 13 parked paths; four intended worker outputs plus three unauthorized support outputs; staging empty |
| After status evidence | four worker outputs remain pending; three unauthorized support files removed; R1 packet prepared separately |
| Diff evidence | exact append, lock, DACL rollback, blank-line and manifest contradictions reconciled |
| Approval boundary | review and corrective-dispatch preparation only |
| Claim boundary | no credentials, Party B execution, real Group 1 read, Group 3 source, provider/live/public/deploy effect |
| Agent type | independent Local reviewer/orchestrator |
| Invocation ID | `acel-g1-t3c-c1-group3-observation-tooling-review-2026-09-21` |
| Expected manifest | this review plus paired R1 baseline/work order |
| Actual changed set | this review plus paired R1 baseline/work order; three unauthorized untracked support paths deleted |
| Manifest delta | MATCH after R1 packet authoring |
| Deletion or rename disposition | delete only the three untracked manifest-excess support files created by the returned worker |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private implementation review and corrective dispatch; no public-sync
authority or artifact is claimed.

## Claim Boundary

This review rejects the current T3C-C1 return and authorizes one bounded R1
correction only. It does not use credentials, execute as Party B, read the real
registry for testing, create or establish Group 3, provision Party C, create
Group 4, wire T3E, admit a candidate, commit worker output or authorize
provider/live/network/public/deployment effects.
