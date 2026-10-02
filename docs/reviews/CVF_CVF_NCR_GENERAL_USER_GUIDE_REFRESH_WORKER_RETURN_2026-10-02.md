# CVF NCR General User Guide Refresh Worker Return

Memory class: worker-return-evidence

docType: review

Status: COMPLETE_PENDING_REVIEW

Self-declared worker-return artifact: yes

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_GENERAL_USER_GUIDE_REFRESH_2026-10-02.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_GENERAL_USER_GUIDE_REFRESH_2026-10-02.md`

executionBaseHead: `e2107ca24a15e6f7101a048591eaf5325ca8bd65`

contractProfile: WORKER_RETURN_FULL_GATE_V1

## Rework Convergence Self-Proof

rootCauseClusterId: GENERAL_CVF_USER_GUIDE_SCOPE_AND_PRACTICE_GAP
recurrenceDisposition: FIRST_OCCURRENCE
priorRelatedFinding: NOT_APPLICABLE_WITH_REASON - initial dispatch
operatorNoticeDisposition: NOT_APPLICABLE_WITH_REASON - no operator decision is involved
successorFreezeDisposition: NOT_APPLICABLE_WITH_REASON - no successor tranche is opened
reworkGeneration: 0
consolidatedDefectClassSweep: COMPLETE_ALL_KNOWN_DEPENDENCIES
productionBindingEvidence: NOT_APPLICABLE_WITH_REASON - documentation only; no code, route or runtime surface was edited or executed
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
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"cvf-ncr-general-user-guide-refresh","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":["GENERAL_CVF_USER_GUIDE_SCOPE_AND_PRACTICE_GAP"],"reopened":[],"current":["GENERAL_CVF_USER_GUIDE_SCOPE_AND_PRACTICE_GAP"]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INITIAL_BOUNDED"}
```

## Purpose

Return the refreshed general CVF orientation: the existing short guide now explains, for a newcomer handing AI a coding task, what CVF does, who does what, the seven governed decisions, and one illustrative unexecuted coding example, with dated April 2026 status removed from the current-status position. Worker evidence for Local, not acceptance.

## Target / Source

Bound work order and paired baseline `docs/baselines/CVF_GC018_CVF_NCR_GENERAL_USER_GUIDE_REFRESH_2026-10-02.md`. Modified: `docs/guides/CVF_QUICK_ORIENTATION.md`, plus link-only insertions in `docs/GET_STARTED.md` and `docs/reference/CVF_INTERNAL_USER_GUIDE.md`. Read only: the VOM Quick Start, HOW_TO_APPLY_CVF, the three named doctrine files, the lifecycle standard, the execution SOP headings, AGENTS.md and the roadmap general-guide section. Created: the evidence JSON and this return.

## Scope / Methodology

Startup acknowledged: mode `cvf_ncr_p10_closed_p11_parked`; handoff `AGENT_HANDOFF_V63_2026-09-18.md`; next allowed move: execute the released general user guide refresh; role INTERNAL_AGENT worker; decision owner Local. At clean HEAD `e2107ca24` the two output paths were absent, the three guide hashes and line counts were recorded, and the bound pre-implementation gate passed before any edit.

Named files were read directly; no whole-repository scan is claimed. No test, browser, HTTP, provider, build or store was used. The static cross-check script is stored in the evidence JSON so it can be rerun.

## Findings / Position

- Five-entry reconciliation: Quick Orientation stays the single short owner. VOM Quick Start and HOW_TO_APPLY_CVF were not edited; GET_STARTED and the compatibility guide received link-only insertions. No parallel guide was created.
- Quick Orientation (128 to 130 physical lines, cap 180): rewritten in Vietnamese. It states CVF is governance infrastructure and not an IDE, coding tool or agent builder; gives the Human, agent and CVF roles; lists the seven governed decisions as decisions, not documents or per-stage approvals; and walks through one illustrative expense-filter assignment with synthetic data, allowed files, edge cases, evidence and the reviewer decision. The example is labelled unexecuted. A copyable request is included.
- Removed from the current-status position: the Phase 0 to 6 dashboard, Release Candidate and provider certification text, the 62-skill and 84-scenario counts. The April 2026 packets are linked only as dated history. Retained sensitive claims are mapped to source and limit in the evidence JSON.
- Preservation: GET_STARTED grew by 2 lines (538 to 540) and the compatibility guide by 1 (8 to 9). Removing the insertions reproduces the original text exactly, and the original mix of CRLF and LF endings was kept.
- Higher-owner contradictions disclosed, not amended: C-1 (VOM says CVF "automatically enforces" and an IDE agent complies by itself, against doctrine's control at integrated points), C-2 (62 versus 141 skills), C-3 (four-phase versus seven-decision flows), C-4 (R3 wording). Each has its handling in the evidence JSON.
- Advisory reader cases Q1 to Q6 answered with section anchors. This is agent reading, not a human usability study.
- One claim lacks a located canonical sentence: "approval continues for already-authorized reversible work" comes from the work order itself (Implementation Contract item 4). Flagged for Local. The R0 to R3 table is the previous Quick Orientation text carried unchanged and not re-verified in this task.

## Work-Order Acceptance Evidence

```acceptance-evidence-json
{
  "schemaVersion": "cvf.workOrderAcceptanceEvidence@1.0.0",
  "executionBaseHead": "e2107ca24a15e6f7101a048591eaf5325ca8bd65",
  "results": [
    {"requirementId":"REQ-1","actualArtifacts":["docs/guides/CVF_QUICK_ORIENTATION.md","docs/GET_STARTED.md","docs/reference/CVF_INTERNAL_USER_GUIDE.md"],"proofRefs":["PROOF-OWNER","PROOF-AUTHORITY","PROOF-IDENTITY","PROOF-RECOVERY","PROOF-BOUNDARY"],"status":"PASS"},
    {"requirementId":"REQ-2","actualArtifacts":["docs/reviews/evidence/cvf-ncr-general-user-guide-refresh-2026-10-02.json"],"proofRefs":["PROOF-CASE-PLAN","PROOF-SOURCE"],"status":"PASS"},
    {"requirementId":"REQ-3","actualArtifacts":["docs/reviews/CVF_CVF_NCR_GENERAL_USER_GUIDE_REFRESH_WORKER_RETURN_2026-10-02.md"],"proofRefs":["PROOF-RETURN"],"status":"PASS"}
  ],
  "parkedCheckpoints": ["Q001 and Q004 exit","real accepting actor and account","artifact store location and writer model","retention and deletion schedule","cost budget","P08","artifact acceptance","pilot or live effect","P11","video","public sync","deployment"]
}
```

## Risk / Corrective Action

The guide is documentation only; static checks show consistency, not that a newcomer understands it or that CVF controls any external IDE. The coding example was never run. The approval-continuity sentence and the risk table need Local confirmation of their source. VOM Quick Start still contains the enforcement wording described in C-1; it is outside this write scope and is left for a separately authorized change. Link targets resolve today; the April packets were not re-read.

## Decision / Disposition

Disposition: COMPLETE_PENDING_REVIEW. Acceptance, commit, roadmap, continuity and any video lane remain with Local.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_experience_retrospective.py` (field values follow the accepted prior returns, which passed the same gate) |
| literalTokensReviewed | `COMPLETE_PENDING_REVIEW`; `acceptance-evidence-json`; `WORKER_MUST_NOT_COMMIT honored`; `run_worker_return_fast_gate.py`; `git diff --name-status`; `PENDING_REVIEWER_EXECUTION` |
| gateRunPurpose | Confirm the exact five-path ledger join and reviewer-pending status |
| claimBoundary | Structural gates cannot show reader understanding or runtime enforcement. |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Internal worker |
| Provider or surface | Shared private CVF workspace; document reading, Git and static scripts |
| Session or invocation | NCR general user guide refresh worker, 2026-10-02 |
| Working directory | Repository root |
| Command or tool surface | pre-implementation gate; file reads; byte-level insertion; static cross-check; worker fast gate |
| Target paths | the five paths of the work order |
| Allowed scope source | Bound work order and paired GC-018 baseline |
| Before status evidence | clean worktree at HEAD `e2107ca24`; two output paths absent |
| After status evidence | three modified tracked paths and two new paths, nothing staged, no commit |
| Diff evidence | `git diff --name-status` lists the three modified guides; `git status --short --untracked-files=all` lists all five |
| Approval boundary | Worker evidence only; Local owns review and commit |
| Claim boundary | Document consistency only |
| Agent type | INTERNAL_AGENT worker |
| Invocation ID | cvf-ncr-general-user-guide-refresh-worker-20261002 |
| Expected manifest | `docs/guides/CVF_QUICK_ORIENTATION.md`; `docs/GET_STARTED.md`; `docs/reference/CVF_INTERNAL_USER_GUIDE.md`; `docs/reviews/evidence/cvf-ncr-general-user-guide-refresh-2026-10-02.json`; `docs/reviews/CVF_CVF_NCR_GENERAL_USER_GUIDE_REFRESH_WORKER_RETURN_2026-10-02.md` |
| Actual changed set | `docs/guides/CVF_QUICK_ORIENTATION.md`; `docs/GET_STARTED.md`; `docs/reference/CVF_INTERNAL_USER_GUIDE.md`; `docs/reviews/evidence/cvf-ncr-general-user-guide-refresh-2026-10-02.json`; `docs/reviews/CVF_CVF_NCR_GENERAL_USER_GUIDE_REFRESH_WORKER_RETURN_2026-10-02.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | Documentation consistency of the refreshed orientation and two link insertions |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: static checks; reviewer pending |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no governance receipt is created or consumed |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: the coding example was not executed; static checks only |
| invocationBoundary | file reads, Git and local scripts only |
| interceptionBoundary | no runtime, route or provider was invoked |
| claimLanguage | Illustrative guide pending Local review |
| forbiddenExpansion | No code, doctrine, operating model, runtime, provider, video, public sync or deployment |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Input type | internal governed input (no external intake) |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Internal source | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` |
| Chain map route | Local general-guide consolidation |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `docs/guides/CVF_QUICK_ORIENTATION.md` |
| Disposition | INTERNAL_ONLY_NO_EXTERNAL_PROMOTION |
| Claim boundary | No external advisory is private CVF proof. |

## External/Local Coordination Binding

Role: shared-workspace `INTERNAL_AGENT`. Phase: bounded general guide refresh. Decision owner: Local.

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: named source files were read directly; no external-source rescan occurred.

## Corpus Completeness And Report Integrity

N/A with reason: five exact worker paths are the bounded set; no all-files inventory is claimed.

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - the task makes no corpus completeness claim.

## Finding-To-Governance Learning Disposition

| Field | Value |
|---|---|
| Defect class | OPERATOR_SCOPE_CLARITY_GAP (documentation claim drift): the old orientation presented dated status as current and a sibling guide uses stronger enforcement wording than the doctrine it cites |
| Learning lane | DOCUMENTATION_ONLY_LEARNING |
| Finding | C-1 to C-4 in the evidence JSON |
| Disposition | N/A_WITH_REASON: the contradictions are disclosed for Local and no rule or checker change is proposed |
| Next control action | Local decides whether VOM Quick Start needs a separately authorized wording change |

## Epistemic Process Block

### Expected Result / Prediction

Reconciling the five entries would show Quick Orientation as the natural short owner, with dated status and some enforcement wording elsewhere needing disclosure rather than edits.

### Evidence Comparison

That held: the old orientation carried April dashboard and count claims, VOM carried stronger enforcement wording than doctrine, and the compatibility and setup guides needed only links.

### Contradiction Or Gap Disposition

Four higher-owner or sibling contradictions (C-1 to C-4) are disclosed and not amended. Two claim sources are flagged for Local: approval continuity and the risk table.

### Claim Update

The guide is a consistent, scoped orientation pending Local review. It proves nothing about runtime behavior or reader understanding.

## Return-Time Closeability Recheck

closeabilityDisposition: CLOSEABLE
outsideAuthorityBlockers: NONE
nextRepairRoute: NONE
workerRedispatchAllowed: NO

The five-path worker manifest is complete and no forbidden path was edited.

independentProbeDisposition: PENDING_REVIEWER_EXECUTION
probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER

## Worker Experience Retrospective

WORKER_EXPERIENCE_RETRO:
frictionLevel: LOW
frictionType: HELPER_GAP
observedStep: the guides mix CRLF and LF line endings, so a naive split-and-join insertion failed its own length assertion and had to be redone with line-ending-preserving splitting
preventiveControlCandidate: HELPER_DIAGNOSTIC

## Claim Boundary

The worker return is `COMPLETE_PENDING_REVIEW`; it is not acceptance, a usability study, a runtime or enforcement proof, a provider readiness claim, a send or B2 closure, a Q001 or Q004 exit, a video or public catalog admission or a deployment claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## git status --short

Three modified tracked guides and two untracked worker-owned files, zero staged. Exact path list follows.

## Changed Files

- `docs/guides/CVF_QUICK_ORIENTATION.md`
- `docs/GET_STARTED.md`
- `docs/reference/CVF_INTERNAL_USER_GUIDE.md`
- `docs/reviews/evidence/cvf-ncr-general-user-guide-refresh-2026-10-02.json`
- `docs/reviews/CVF_CVF_NCR_GENERAL_USER_GUIDE_REFRESH_WORKER_RETURN_2026-10-02.md`

## Command Evidence

- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --head HEAD --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_GENERAL_USER_GUIDE_REFRESH_2026-10-02.md`: PASS (exit 0) before any edit.
- Static cross-check stored in the evidence JSON: PASS_STATIC_ONLY, exit 0, no failures (8 read-only input hashes, 3 final hashes, local links, line caps, preservation against git HEAD, required and stale content tokens, dated April lines, exact five-path set). The first run failed on a content token that did not match the guide's bold markup; the token was corrected, not the guide.
- Line counts, `len(text.splitlines())`: Quick Orientation 130 (cap 180), GET_STARTED 540 (cap 541), compatibility guide 9 (cap 11).
- `git diff --check`: exit 0 (only the line-ending conversion notice from Git).
- `python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_GENERAL_USER_GUIDE_REFRESH_2026-10-02.md`: first run exit 1 only because the worker-return quality check requires PASS evidence of this same fast gate, which cannot exist before this line. Later reruns also failed on the learning-disposition fields (lane, defect class and disposition values); those were corrected. Final rerun: PASS, exit 0, `COMPLIANT: worker-return fast gate passed`. The quality-gate check passed on this disclosure text, so that one check is a literal-text match; the other checks passed on their own.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`worker_execution`, role=`worker`, lifecyclePhase=`worker-return`.

Command: `python governance/compat/run_adif_defect_resolver.py --task-class worker_execution --role worker --lifecycle-phase worker-return --json`; 0 items, `truncated=false`.

Returned defects: NONE_RETURNED

## No-Commit Statement

WORKER_MUST_NOT_COMMIT honored. All five worker outputs are uncommitted, and Local owns review and any commit.
