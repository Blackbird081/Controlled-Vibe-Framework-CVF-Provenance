# CVF NCR HTML B2a Synthetic Acceptance Worker Return

Memory class: worker-return-evidence

docType: review

Status: COMPLETE_PENDING_REVIEW

Self-declared worker-return artifact: yes

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_CONTRACT_2026-09-30.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_CONTRACT_2026-09-30.md`

executionBaseHead: `ddfda8ab9fddee75b7c9c65dc537503ed3fa945a`

contractProfile: WORKER_RETURN_FULL_GATE_V1

## Rework Convergence Self-Proof

rootCauseClusterId: NOT_APPLICABLE_INITIAL_DISPATCH
reworkGeneration: 0
consolidatedDefectClassSweep: COMPLETE_ALL_KNOWN_DEPENDENCIES
productionBindingEvidence: BOUNDED_SYNTHETIC_PURE_FUNCTION_TESTS_ONLY
adversarialRegressionDisposition: PASS_TARGETED_DEFECT_CLASS
successorTrancheOpened: NO
implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY
internalAgentInvocationCount: 1
externalAgentInvocationCount: 0
providerCallCount: 0
tokenOrQuotaUsage: NOT_AVAILABLE_WITH_REASON: local agent usage meter was not exposed to this worker
terminalReadinessVerdict: READY_FOR_REVIEW

## Semantic Convergence Outcome

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"cvf-ncr-html-b2a-synthetic-acceptance","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":[],"reopened":[],"current":[]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INITIAL_BOUNDED"}
```

## Purpose

Return the isolated B2a synthetic candidate: a pure exact-byte identity helper for rendered HTML, focused synthetic tests, and a proposal-only reference contract for a later single-host, one-writer acceptance store. This is worker evidence pending independent Local review. It is not artifact acceptance.

## Target / Source

Bound work order `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_CONTRACT_2026-09-30.md` (sha256 recorded by Local at review) and paired baseline `docs/baselines/CVF_GC018_CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_CONTRACT_2026-09-30.md`. Source read for shape only, and unmodified: the export route (`buildHtml` embeds generated time and source hash; `sourceHash` is a SHA-256 of source text only) and the pending-execution SQLite store header as a single-node precedent. Created: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-acceptance-candidate.ts`, its adjacent `.test.ts`, `docs/reference/CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_CONTRACT_2026-09-30.md` and this return.

## Scope / Methodology

Startup acknowledged: mode `cvf_ncr_p10_closed_p11_parked`; active handoff `AGENT_HANDOFF_V63_2026-09-18.md`; next allowed move: execute the bound B2a worker packet; role INTERNAL_AGENT worker; phase worker execution; decision owner Local. At clean committed HEAD `ddfda8ab9` the four create paths were absent, a scoped search found no import of the candidate under the Web source tree, and the bound pre-implementation gate passed before any edit.

Candidate. `computeHtmlBytesIdentity` hashes the UTF-8 bytes of the exact string with SHA-256 and records the byte length; there is no trimming, newline conversion, BOM handling or Unicode normalization. A string with a lone surrogate, or an empty or non-string value, is refused because it has no exact encoding. `createHtmlArtifactCandidate` takes the exact HTML, explicit attempt metadata (attempt ID, positive integer build number), an optional `sourceHash` (checked as 64 lowercase hex) and optional receipt evidence, and returns a frozen object whose state is always `DRAFT_UNACCEPTED`. `withReceiptEvidence` copies with new evidence and a fixed state. `verifyHtmlArtifactCandidate` checks well-formedness, state, then recomputes over the string given (length first, then hash); it never rebuilds HTML and never consults `sourceHash`, attempt or receipt. The only import is `node:crypto`. No exported name accepts, approves, persists or commits.

Tests use synthetic strings only, a render helper that mirrors the route's embedded fields, and digests computed independently with Python hashlib for `abc`, a non-ASCII string (30 bytes), NFC and NFD forms of the same word, and a whitespace string. The contract states Part 1 (implemented identity rules) apart from Part 2 (proposed actor, immutable record model, transaction, commit-before-acknowledge, readback, unknown-outcome reconciliation, recovery owner), marks Part 2 `PROPOSAL_NOT_IMPLEMENTED`, and lists nine open operator decisions.

## Findings / Position

Focused tests: 13 pass. They cover independent SHA-256 vectors, stable identity across calls, non-ASCII determinism with no normalization, changed title, boundary or generated time each changing identity while the source hash stays put, four separate identifier values, one-character, same-length whitespace, trailing-newline, line-ending, BOM and truncation mutations all rejected, stored-identity tampering (hash, length, format, schema), refused encodings, metadata validation, receipt decisions `ALLOW`, `APPROVED`, `ACCEPTED`, `DENY` and others leaving state unchanged, forged states rejected, frozen non-aliased output, and a source scan showing only `node:crypto` is imported and no acceptance-like export exists.

Discrimination checks, each reverted and the file diff-verified as restored: removing the hash comparison failed 4 tests; removing the state check failed 1; hashing whitespace-collapsed text initially passed all 13. That was a real test gap, because every earlier mutation also changed the byte length and the length check caught it. I added a whitespace vector and two same-length whitespace mutations, and the collapsed-text mutant now fails 2 tests. `npx tsc --noEmit` and `npx eslint --max-warnings=0` on both code paths exited 0.

Scoped search of the Web source tree for the candidate name finds only the test file. Not covered: real route output, browser rendering, disk or database behavior, actor authority, and anything in Part 2.

## Risk / Corrective Action

Disclosed limits for Local disposition. The identity is over a JavaScript string encoded as UTF-8; if a later caller hashes bytes that were decoded and re-encoded elsewhere, identity is only as exact as that hand-off, and the contract does not specify the transport. `node:crypto` ties the helper to server-side or Node test use. A supplied `sourceHash` is format-checked only; it is not recomputed. The source-scan test reads the module from the working directory and assumes Vitest runs from the Web package. The Part 2 proposal contains design choices such as append-only versions and a duplicate-identity rule that the operator has not chosen. No route, storage or auth change was needed and none was made.

## Decision / Disposition

Disposition: COMPLETE_PENDING_REVIEW. The worker claims tested exact-byte identity, tamper rejection and acceptance separation on synthetic strings, and a labeled proposal. Acceptance, any durable store, and the open operator decisions remain with Local and the operator.

## Work-Order Acceptance Evidence

```acceptance-evidence-json
{
  "schemaVersion": "cvf.workOrderAcceptanceEvidence@1.0.0",
  "executionBaseHead": "ddfda8ab9fddee75b7c9c65dc537503ed3fa945a",
  "results": [
    {"requirementId":"REQ-CANDIDATE","actualArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-acceptance-candidate.ts"],"proofRefs":["PROOF-BYTES","PROOF-SEPARATION"],"status":"PASS"},
    {"requirementId":"REQ-TEST","actualArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-acceptance-candidate.test.ts"],"proofRefs":["PROOF-MUTATION","PROOF-RECEIPT"],"status":"PASS"},
    {"requirementId":"REQ-CONTRACT","actualArtifacts":["docs/reference/CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_CONTRACT_2026-09-30.md"],"proofRefs":["PROOF-BOUNDARY"],"status":"PASS"},
    {"requirementId":"REQ-RETURN","actualArtifacts":["docs/reviews/CVF_CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_WORKER_RETURN_2026-09-30.md"],"proofRefs":["PROOF-RETURN"],"status":"PASS"}
  ],
  "parkedCheckpoints": ["real GitHub-ledger cutover","real accepting actor and account","artifact store location and writer model","backup location and key custody","retention and deletion schedule","RPO and RTO","cost budget","P08","artifact acceptance","pilot or live effect","P11","deployment","Q001 and Q004 exit"]
}
```

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_equivalence_claim_evidence.py` |
| literalTokensReviewed | `COMPLETE_PENDING_REVIEW`; `acceptance-evidence-json`; `WORKER_MUST_NOT_COMMIT honored`; `run_worker_return_fast_gate.py`; `git diff --name-status`; `COMPLETE_ALL_KNOWN_DEPENDENCIES`; `PENDING_REVIEWER_EXECUTION` |
| gateRunPurpose | Confirm the observed test evidence, the exact four-path ledger join and reviewer-pending status |
| claimBoundary | Structural gates cannot substitute for the Local byte-mutation probe or prove behavior beyond the synthetic cases. |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Internal worker |
| Provider or surface | Shared private CVF workspace; Node Vitest with synthetic strings, no I/O in the candidate |
| Session or invocation | NCR HTML B2a synthetic candidate worker, 2026-09-30 |
| Working directory | Repository root and `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web` |
| Command or tool surface | bound pre-implementation autorun gate; Vitest; eslint; tsc; ripgrep import search; worker fast gate |
| Target paths | Exact four-path worker acceptance ledger |
| Allowed scope source | Bound B2a work order and paired GC-018 baseline, released at HEAD `ddfda8ab9` |
| Before status evidence | `git status --short --untracked-files=all` empty at HEAD `ddfda8ab9` before worker edit |
| After status evidence | Four untracked worker paths, no modified tracked path, no staged path and no worker commit |
| Diff evidence | `git diff --name-status` prints nothing because every worker path is new; `git status --short --untracked-files=all` lists the four paths as untracked |
| Approval boundary | Worker evidence only; Local reviewer owns the independent probe, acceptance and commit |
| Claim boundary | Synthetic identity helper and proposal only; no artifact acceptance, Q001 or Q004 closure, or live assertion |
| Agent type | INTERNAL_AGENT worker |
| Invocation ID | cvf-ncr-html-b2a-synthetic-worker-20260930 |
| Expected manifest | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-acceptance-candidate.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-acceptance-candidate.test.ts`; `docs/reference/CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_CONTRACT_2026-09-30.md`; `docs/reviews/CVF_CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_WORKER_RETURN_2026-09-30.md` |
| Actual changed set | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-acceptance-candidate.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-acceptance-candidate.test.ts`; `docs/reference/CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_CONTRACT_2026-09-30.md`; `docs/reviews/CVF_CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_WORKER_RETURN_2026-09-30.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | Isolated synthetic exact-byte HTML identity helper and proposal-only design contract |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: tested on synthetic strings; reviewer pending |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no receipt is created or consumed; synthetic receipt objects are test data only |
| actionEvidence | ACTION_EVIDENCE_PRESENT: focused Vitest results and mutation runs recorded above |
| invocationBoundary | Pure local tests; no route, database, provider, network or file writes |
| interceptionBoundary | No proxy, wrapper or runtime gate is claimed and nothing imports the helper |
| claimLanguage | Tested exact-byte identity and acceptance separation of an unconnected candidate, reviewer pending |
| forbiddenExpansion | No route, ledger, database, provider, real data, artifact acceptance, public sync or deployment |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Input type | internal governed input (no external intake) |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Internal source | `docs/reviews/CVF_CVF_NCR_HTML_B2_ACCEPTANCE_OWNER_STORAGE_AUDIT_2026-09-30.md` |
| Chain map route | Local source-derived owner correction |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` |
| Disposition | INTERNAL_ONLY_NO_EXTERNAL_PROMOTION |
| Claim boundary | No external advisory is private CVF proof. |

## External/Local Coordination Binding

Role: shared-workspace `INTERNAL_AGENT`. Phase: bounded B2a synthetic worker. Decision owner: Local.

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: the named route and store header were read directly; no external-source rescan or intake reassessment occurred.

## Corpus Completeness And Report Integrity

N/A with reason: four exact worker outputs are the bounded set; no all-files inventory is claimed.

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - the tranche makes no corpus completeness claim.

## Finding-To-Governance Learning Disposition

| Field | Value |
|---|---|
| Defect class | WORKER_EXECUTION_ERROR: my first test set let a whitespace-normalizing hash pass because a length check masked it; caught by my own mutation run and repaired |
| Learning lane | RUNTIME_BEHAVIOR_LEARNING |
| Finding | Byte-identity tests need at least one mutation that keeps the byte length, or a length guard hides a normalizing hash |
| Disposition | RUNTIME_LEARNING_CANDIDATE: Local decides whether to keep this as a review-probe template |
| Next control action | Local reviewer runs its own byte pair with one changed rendered field |

## Epistemic Process Block

### Expected Result / Prediction

Every rendered-field change and every one-byte mutation should fail verification; a receipt decision of any text should leave the candidate unaccepted; removing the hash check, the state check or byte exactness should make tests fail.

### Evidence Comparison

All mutations and forged states were rejected and all receipt decisions left state fixed. Removing the hash check failed 4 tests and removing the state check failed 1. Hashing whitespace-collapsed text initially failed none.

### Contradiction Or Gap Disposition

The surviving whitespace mutant contradicted the prediction. Every earlier mutation changed the byte length, so the length guard caught it. Adding a whitespace vector and two same-length whitespace mutations made that mutant fail 2 tests. The independent Local probe remains pending.

### Claim Update

The worker claims tested exact-byte identity, tamper rejection and acceptance separation on synthetic strings, with reviewer acceptance pending. Q001 and Q004 remain open and nothing is accepted.

## Return-Time Closeability Recheck

closeabilityDisposition: CLOSEABLE
outsideAuthorityBlockers: NONE
nextRepairRoute: INDEPENDENT_LOCAL_REVIEW
workerRedispatchAllowed: NO

The four-path worker manifest is complete and no forbidden path was edited. The distinct reviewer retains the independent probe and disposition.

independentProbeDisposition: PENDING_REVIEWER_EXECUTION
probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER

## Worker Experience Retrospective

WORKER_EXPERIENCE_RETRO:
frictionLevel: LOW
frictionType: NONE
observedStep: shell heredocs turned backslash escapes in patch text into raw tab and newline characters once, which broke two test lines until repaired
preventiveControlCandidate: NONE

## Claim Boundary

The worker return is `COMPLETE_PENDING_REVIEW`. It is not acceptance, artifact approval, a durable store, an operator decision, proof of route, browser or live behavior, provider proof, Q001 or Q004 exit, P11 release or a public claim. Undecided operator checkpoints remain: real accepting actor, real data and store profile, store location and writer model, backup and key custody, retention, RPO and RTO, cost, P08 scope, artifact acceptance, pilot or live effect, P11 and deployment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## git status --short

Four untracked worker-owned files, no modified tracked file, zero staged files. Exact path list follows.

## Changed Files

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-acceptance-candidate.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-acceptance-candidate.test.ts`
- `docs/reference/CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_CONTRACT_2026-09-30.md`
- `docs/reviews/CVF_CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_WORKER_RETURN_2026-09-30.md`

## Command Evidence

- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --head HEAD --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_CONTRACT_2026-09-30.md`: PASS (exit 0) before any worker edit.
- `npm exec vitest run src/lib/html-artifact-acceptance-candidate.test.ts`: PASS, 13/13.
- `npx eslint --max-warnings=0` on the candidate and its test: PASS, exit 0.
- `npm run check` (`tsc --noEmit`): PASS, exit 0.
- `rg -n "html-artifact-acceptance-candidate" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src`: PASS, only the adjacent test file matches (its import, describe title and source-scan path).
- `python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_CONTRACT_2026-09-30.md --pytest-target EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-acceptance-candidate.test.ts`: first run before this line was written failed only on the missing-PASS-evidence check; final rerun after it was written: PASS (exit 0).

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`worker_execution`, role=`worker`, lifecyclePhase=`worker-return`.

Command: `python governance/compat/run_adif_defect_resolver.py --task-class worker_execution --role worker --lifecycle-phase worker-return --json`; 0 items, `truncated=false`.

Returned defects: NONE_RETURNED

## No-Commit Statement

WORKER_MUST_NOT_COMMIT honored. All four worker outputs are uncommitted, and the distinct Local reviewer owns acceptance and material commit.
