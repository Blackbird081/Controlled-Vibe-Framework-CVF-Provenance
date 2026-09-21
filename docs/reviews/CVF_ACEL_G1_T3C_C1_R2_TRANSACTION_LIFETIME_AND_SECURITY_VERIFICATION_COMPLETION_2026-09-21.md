# CVF ACEL G1 T3C-C1 R2 Transaction Lifetime And Security Verification Completion Review

Memory class: governed-review

docType: review

Status: STOP_REASSESS_ARCHITECTURE

Date: 2026-09-21

Batch ID: ACEL-G1-T3C-C1-R2-TRANSACTION-LIFETIME-AND-SECURITY-VERIFICATION-REVIEW

Review base head: `c16cc15ca6a52244d52383f2b41d8439e2cce5de`

providerExecutionAuthority: FORBIDDEN

successorTrancheOpened: NO

## Purpose

Record Local's independent disposition of the R2 integrated root-contract
return. Valid record/checker evidence is retained, but R2 does not prove the
transaction-wide concurrency claim, leaves an acquisition-to-try exception
window, does not verify restored DACL semantics, and violates the exact return
manifest while overstating its final gate. No bounded R3 is authorized.

## Target / Source

| Source | Identity / role |
|---|---|
| R2 work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3C_C1_R2_TRANSACTION_LIFETIME_AND_SECURITY_VERIFICATION_2026-09-21.md`; SHA-256 `1f333bcb14f75272b466e29ab1e8a4f650fdc806ecd3db5aa2bf52e0befcf6d9` |
| worker-declared R2 return | unauthorized fifth path reviewed at SHA-256 `907d47e02d4b0861cb39eae27ce8dbfa70532427c0caa91f46513d060f380177`, then removed by Local as manifest-excess packaging cleanup |
| canonical worker return path | `docs/reviews/CVF_ACEL_G1_T3C_C1_GROUP3_OBSERVATION_LOG_TOOLING_WORKER_RETURN_2026-09-21.md`; remains bound to R1 rather than R2 |
| implementation | `scripts/acel_g1_party_b_group3_observation_writer.ps1`; checker and focused Python test |
| Local execution | Python 42/42 PASS; checker self-test PASS; writer 45/45 PASS; R2 worker-return fast gate FAIL; real log absent |

## Scope / Methodology

Local retained the valid R1 record-level tests and reran the declared R2
suites. Review then compared every R2 acceptance oracle with the executable
self-tests and inspected guard acquisition/release, pre-state snapshot,
rollback verification and output-manifest control flow. No credential,
alternate-user execution, real Group 1 read or real Group 3 write occurred.

## Findings / Position

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| T3C-C1-R2-RV-1 | CRITICAL | The required deterministic peer-transaction probe is absent. T3C-C1-16 only recomputes mutex names and confirms an acquired object is a `Mutex`; it never starts a peer, blocks it across DACL/final validation, or proves rollback cannot erase peer data. The return's concurrency proof claim is unsupported. | ADVERSARIAL_CONCURRENCY_PROOF_MISSING |
| T3C-C1-R2-RV-2 | HIGH | `New-TransactionGuard` acquires the mutex before the outer `try`, while directory/file existence checks, prior-byte reads and owner/DACL capture also occur before that `try`. Any exception in this window escapes the release `finally`, leaving the process holding the named mutex until termination. | GUARD_LIFETIME_EXCEPTION_WINDOW |
| T3C-C1-R2-RV-3 | HIGH | Rollback writes the captured DACL and then proves only bytes and owner. It never re-reads and semantically compares the restored DACL/protection/ACE state, despite the root contract requiring proof of exact prior owner/DACL semantics. | ROLLBACK_SECURITY_PROOF_INCOMPLETE |
| T3C-C1-R2-RV-4 | HIGH | Required security adversaries are incomplete: the suite covers wrong owner and inheritance, but not an extra allow ACE or deny ACE. The claimed 14-case matrix therefore does not satisfy the explicit R2 acceptance set. | SECURITY_NEGATIVE_MATRIX_INCOMPLETE |
| T3C-C1-R2-RV-5 | HIGH | The worker created an unauthorized fifth return instead of updating the canonical return path. The new packet omits mandatory review/trace/epistemic/SCEC blocks, uses malformed double-backtick work-order links and says the fast gate is COMPLIANT. Local's exact rerun fails that gate on the new packet. This is both manifest drift and final-evidence sequencing failure. | RETURN_AND_EVIDENCE_INTEGRITY_FAILED |

## Risk / Corrective Action

The code is materially improved, but acceptance would treat mutex existence as
concurrency proof and leave a real release gap before the protected `try`.
Rollback could also claim security restoration without checking the restored
DACL. Because R2 was already the required integrated root contract and the
same transaction claim has now failed again, Local stops bounded redispatch.
A future reopen requires an architecture reassessment that redesigns the
transaction harness and evidence production together, not an R3 patch list.

## Independent Probe Evidence

| Probe | Observed result | Disposition |
|---|---|---|
| Python checker suite | `42 passed in 0.39s` | RETAINED_PASS |
| checker self-test | published vector/genesis PASS | RETAINED_PASS |
| writer self-test | `45/45 passed` | RETAINED_PASS_BUT_NON_DISCRIMINATING_FOR_CONCURRENCY |
| R2 worker-return fast gate | FAIL on new return: missing mandatory packet blocks plus reviewer-fast failures | CONTRADICTS_RETURN |
| transaction source order | mutex acquired at line 764; protected `try` begins at line 783 after state reads | FAILURE_WINDOW_CONFIRMED |
| rollback source order | DACL applied at lines 683-684; read-back checks bytes and owner only | DACL_PROOF_GAP_CONFIRMED |
| real source absence | `Test-Path governance/sources/registry_observation_log/LOG.jsonl` -> `False` | PASS |
| manifest | worker returned five T3C-C1 paths; Local removed only the unauthorized fifth return after preserving its hash and findings | EXACT_FOUR_PATH_CONTRACT_FAILED_AND_CLEANED |

## Decision / Disposition

`STOP_REASSESS_ARCHITECTURE`.

R2 is rejected and no R3 work order is issued. The uncommitted implementation
remains non-authoritative evidence only. Real Party B execution, Group 3
establishment, Party C/Group 4 and T3E remain closed.

## Semantic Convergence Outcome

Standard: `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-g1-t3c-c1-group3-observation-log-tooling-problem","chainMode":"SUCCESSOR","chainOrdinal":5,"predecessor":{"path":"docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3C_C1_R2_TRANSACTION_LIFETIME_AND_SECURITY_VERIFICATION_2026-09-21.md","sha256":"1f333bcb14f75272b466e29ab1e8a4f650fdc806ecd3db5aa2bf52e0befcf6d9"},"blockerDelta":{"prior":["REAL_OBSERVATION_PENDING","PARTY_C_AND_GROUP4_PENDING","T3E_PENDING","R2_NOT_ACCEPTED"],"resolved":[],"retained":["REAL_OBSERVATION_PENDING","PARTY_C_AND_GROUP4_PENDING","T3E_PENDING","R2_NOT_ACCEPTED"],"new":["adversarial-concurrency-proof-missing","guard-lifetime-exception-window","rollback-security-proof-incomplete","security-negative-matrix-incomplete","return-and-evidence-integrity-failed"],"reopened":[],"current":["REAL_OBSERVATION_PENDING","PARTY_C_AND_GROUP4_PENDING","T3E_PENDING","R2_NOT_ACCEPTED","adversarial-concurrency-proof-missing","guard-lifetime-exception-window","rollback-security-proof-incomplete","security-negative-matrix-incomplete","return-and-evidence-integrity-failed"]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":3,"nonDecreasingBlockerTransitions":1},"claims":[{"claimId":"ACEL-G1-T3C-C1-R2-COMPLETION-REVIEW","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"docs/reviews/CVF_ACEL_G1_T3C_C1_R2_TRANSACTION_LIFETIME_AND_SECURITY_VERIFICATION_COMPLETION_2026-09-21.md"}],"requiredDisposition":"STOP_REASSESS_ARCHITECTURE","successorScope":"NO_SUCCESSOR"}
```

## Finding-To-Governance Learning Disposition

| Finding group | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| mutex-presence test substituted for peer-exclusion proof | WORKER_EXECUTION_ERROR | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | future durable transaction packets must require an actual second process/runspace plus deterministic barriers; carry into the parked CVF foundation-learning tranche |
| gate claimed before the final return existed | WORKER_EVIDENCE_INTEGRITY_ERROR | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | bind worker-return fast-gate receipt to the exact final return path/hash and reject later packet mutation or alternate return paths |
| repeated durable-transaction miss | REPEATED_ROOT_CONTRACT_FAILURE | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | SCEC stop/reassess rule applied; no bounded R3 |

## Epistemic Process Block

### Expected Result / Prediction

R2 was expected to supply an actual peer-exclusion experiment, hold cleanup
authority across every exception path and prove exact DACL restoration.

### Evidence Comparison

The aggregate suites pass, but their test bodies do not exercise a peer and
the source order exposes an acquisition-to-try gap. The final return gate also
fails despite the return claiming COMPLIANT.

### Contradiction Or Gap Disposition

Record/hash/checker and creation-cleanup evidence is retained narrowly. The
transaction-wide exclusion, rollback-security and review-ready return claims
are invalidated.

### Claim Update

T3C-C1 tooling is not safe or review-ready for real Party B use. The chain is
stopped for architectural reassessment with no successor authorized.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_independent_review_probe_admission.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | review status; stop disposition; no-successor scope; learning fields; epistemic sections; trace and public disposition |
| gateRunPurpose | preserve an evidence-backed terminal rejection without recreating implementation |
| claimBoundary | structural checks and retained suites do not prove transaction safety |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | committed R2 work order | root-contract hash above | PASS |
| Completion or reviewer artifact | this review | `STOP_REASSESS_ARCHITECTURE` | PASS |
| Roadmap state | active ACEL continuity | no tranche closure | N/A with reason |
| Registry JSON | real Group 3 log absent | `False` probe | N/A with reason |
| Registry Markdown | no registry owner change | no mutation | N/A with reason |
| External evidence digest | local bounded review only | no external evidence | N/A with reason |
| System loop interlock | Party B execution | CLOSED | PASS |
| Session continuity | active handoff/state | separate sync commit | PENDING_SEPARATE_SYNC |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | CVF Local orchestrator/reviewer |
| Provider or surface | local private provenance repository |
| Session or invocation | ACEL G1 T3C-C1 R2 completion review, 2026-09-21 |
| Working directory | repository root |
| Command or tool surface | governed reads, focused suites, source inspection, exact active-work-order fast gate, git and apply_patch |
| Target paths | five returned T3C-C1 paths; this terminal review |
| Allowed scope source | committed R2 work order and standing Local review authority |
| Before status evidence | HEAD `c16cc15ca`; thirteen parked paths plus five returned paths; staging empty |
| After status evidence | unauthorized fifth return removed; four implementation paths remain unaccepted; terminal review prepared; real source absent |
| Diff evidence | five consolidated findings with exact source/test contradictions |
| Approval boundary | independent review and terminal disposition only |
| Claim boundary | no credentials, Party B, real source, provider/live/public/deployment effect |
| Agent type | independent Local reviewer/orchestrator |
| Invocation ID | `acel-g1-t3c-c1-r2-completion-review-2026-09-21` |
| Expected manifest | this terminal review only |
| Actual changed set | this terminal review only; worker/parked paths remain uncommitted |
| Manifest delta | MATCH before review commit |
| Deletion or rename disposition | removed only the untracked unauthorized fifth R2 return after recording SHA-256 and review findings; canonical four worker paths preserved |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private terminal review; no public-sync authority or artifact.

## Claim Boundary

This review rejects R2 and stops the same problem chain. It accepts no worker
implementation path, does not authorize an R3, and does not authorize
credentials, alternate-user execution, real Group 1 reads, Group 3 creation,
Party C/Group 4, T3E, candidate admission, provider/live/public/deployment or
production effects.
