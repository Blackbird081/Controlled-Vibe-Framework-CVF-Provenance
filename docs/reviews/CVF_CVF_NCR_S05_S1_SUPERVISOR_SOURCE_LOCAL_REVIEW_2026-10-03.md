# NCR S05 S1 Supervisor Source - Local Consolidated Review

Memory class: reviewer-evidence
docType: review
Status: BLOCKED_WITH_REASON
reviewDisposition: REVIEW_COMPLETE_SOURCE_NOT_ACCEPTED
rootCauseClusterId: s05-s1-source-contract-validation-custody
recurrenceDisposition: FIRST_OCCURRENCE
priorRelatedFinding: NOT_APPLICABLE_WITH_REASON - first Local consolidated source-contract review; old C1 is a different stopped problem.
operatorNoticeDisposition: NOT_APPLICABLE_WITH_REASON - current operator relay already acknowledges the full finding set; no additional notice event required.
successorFreezeDisposition: NOT_APPLICABLE_WITH_REASON - no feature or runtime successor; only one bounded source repair is proposed.
Date: 2026-10-03
Batch ID: CVF-NCR-S05-S1-SUPERVISOR-SOURCE
Reviewed work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_S05_S1_SUPERVISOR_SOURCE_2026-10-03.md`
reviewedWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_S05_S1_SUPERVISOR_SOURCE_2026-10-03.md`

## Purpose

Evaluate returned evidence, preserve actual first-write/process deviations and consolidate one source-only repair. No implementation recreated, no source execution or closure readiness granted.

## Target / Source

`docs/reviews/CVF_CVF_NCR_S05_S1_SUPERVISOR_SOURCE_WORKER_RETURN_2026-10-03.md` and `docs/reviews/evidence/cvf-ncr-s05-s1-supervisor-source-worker-2026-10-03.json`; fourteen frozen external files identified by `docs/reviews/evidence/cvf-ncr-s05-s1-supervisor-source-local-findings-2026-10-03.json`. Operator relay accepts F-01..F-07 and confirms overwrite-capable plain writes/no historical writer log. Relay is advisory process input; Local verifies actual source independently.

## Scope / Methodology

Startup acknowledged: mode cvf_ncr_p10_closed_p11_parked; active handoff AGENT_HANDOFF_V63_2026-09-18.md; role INTERNAL_AGENT Local reviewer; phase returned-source review and consolidated repair admission; decision owner Local; parked S2/install/render/P11/public/deploy.

Local actual-source oracle inspected ten Python ASTs and rejoined fourteen raw file hashes (44,080 bytes); 44/44 narrow checks and five AST-only mutation sensitivity checks. Retained oracle `docs/reviews/evidence/cvf-ncr-s05-s1-supervisor-source-local-static-oracle-2026-10-03.py`; raw identity/evidence `docs/reviews/evidence/cvf-ncr-s05-s1-supervisor-source-local-findings-2026-10-03.json`. No worker source execution/import/evaluation/compilation. One local-scanner correction distinguished benign re.compile from Python compile; first scan was overbroad and not a source finding. Structural reviewer-fast 69/69 and commit-steward preflight PASS are recorded observations; these prove structure only.

## Findings / Position

| ID | Finding | Local disposition |
|---|---|---|
| DV-STARTUP | Worker says AGENTS.md and guard orientation were not fully read; prompt surfaces and a previous return template were used. | Process deviation. The prompt already routed progressive startup through AGENTS.md; omission of a full checklist from the copy prompt did not waive the work-order or orientation requirement. Progressive continuity reading is allowed; skipping required role/task guards is different. Later gate PASS does not cure the earlier omission. |
| DV-READ-AHEAD | Worker reports first fast gate failed on five literal defects; checker reads and fixes came after writing. Return Read-Ahead and Learning disclose this. | Preserve first FAIL and later PASS as separate outcomes. The original five messages/log and detailed diff were not retained in this return, so the count/cause is WORKER_REPORTED, not independently reconstructed. Local confirms only the current 69/69 structural PASS. No checker or rule changed. |
| DV-CREATION | Return methodology says exclusive file creation, but retrospective says only manifest used exclusive open and plain files relied on root absence. | Actual contract violation disclosed by worker; confirmed inconsistency between the two descriptions. Root absence does not implement per-file exclusive creation. No collision/overwrite is proven to have occurred, and no historical check is invented. Preserve bytes; require exact actual writer modes/commands and explicit deviation, not a retroactive compliance claim. |
| DV-EVIDENCE | acceptance block uses PROOF-RETURN, but evidence JSON proofIds omits it; first-write owner/command/mode details and first FAIL messages are not retained. | Evidence gap despite structural PASS. Add exact proof join and qualify historical claims under a later admitted correction. Do not fabricate historical command evidence. |

All outcomes below are static deductions or plans, NOT_EXECUTED_PLANNED. No behavioural repro was run.

| ID | Priority / location | Finding and bounded corrective requirement |
|---|---|---|
| F-01 | Blocking; src/supervisor.py:11-18 | Broad except ImportError changes sibling-relative dependencies to unqualified absolute imports. An ImportError inside a dependency can trigger the fallback, which may resolve an ambient sys.path module. Sibling identity and import-side-effect claims are therefore unproved. Select one sibling/package import posture and fail closed when unavailable; do not mask dependency ImportError or claim that every possible import path is inert. |
| F-02 | Blocking; src/supervisor.py:132-145 | record_phase_elapsed only checks type and seconds<0. NaN and +Infinity lack rejection, and two individually finite increments can overflow the sum; mutation occurs before any aggregate validation. Require finite input and aggregate, no state mutation on rejection, and an explicit aggregate deadline/accounting policy. Negative/NaN/Infinity/overflow and repeated-phase plans are required. This is caller-data accounting, not monotonic-clock or elapsed-time enforcement proof. |
| F-03 | Blocking; src/envelope_contract.py:148,196,204 | envelope_version, stage and effect use frozenset membership before string/type validation. JSON-shaped [] or {} values are unhashable and are predicted to raise TypeError instead of structured rejection. Validate field and element types before membership; return stable reason IDs for malformed caller data. Also qualify math.isfinite on very large Python integers rather than asserting every int is handled safely. |
| F-04 | Identity-policy gap; src/envelope_contract.py:165-178 | Output paths are casefold-deduplicated, but hash keys are not; empty hash mappings and missing/extra output/hash associations are not checked. Choose and document the required association policy, then validate it. SHA regex uses match with a terminal $; a trailing newline is a planned malformed-digest counterexample. Require exact 64-hex digest matching in both envelope and boundary proof validation. |
| F-05 | State correspondence; src/supervisor.py:103-120 | validate stores a new envelope before checking whether the transition is legal. A second validate can change the envelope then raise at _move. seal_source_plan revalidates mutable stored data but ignores a NO_GO decision when moving to SOURCE_PLAN_ONLY. Require legal-state checks before mutation and align sealing with the validation result, or explicitly document a rejected-plan representation. No runtime backend activation is shown here. |
| F-06 | Path policy gap; src/envelope_contract.py:89-124 | casefold catches ordinary case-colliding output strings, so that part meets the literal source requirement. It is not a proof of Windows filesystem equivalence. Reserved device names (CON/NUL.txt), file-versus-descendant conflicts (a and a/b), hash-key case collisions, and owned-root trailing dot/space lack policy/guards. Define a conservative lexical policy; keep host/custody/reparse checks in the separately admitted effect boundary. |
| F-07 | Policy clarification; src/envelope_contract.py:47,79-87; src/boundary_admission.py:89-92 | UNKNOWN scan rejects any string containing the substring, including dictionary keys or a legitimate owner/path containing unknown. This is conservative over-rejection, not an OS-authority bypass. Decide/document sentinel-only versus substring policy; source and claims must agree. Do not assume a broader policy is required by the current contract. |

## Risk / Corrective Action

Single consolidated R1 source repair under a fresh root/admission, not changes to frozen original bytes. Mandatory native/disk/network backend refusal, static counterexample plans, full hash/write-custody evidence and independent Local review remain necessary. Missing historical logs cannot be recovered by inventing them. Source source-only constraints do not prove runtime, containment or costs.

## Decision / Disposition

SOURCE_NOT_ACCEPTED_CONSOLIDATED_REPAIR_REQUIRED. Preserve original worker artifacts as unaccepted evidence. No bootstrap/install/render admission. Old C1 STOP/ordinal2/key/blocker/counters retained. Local may author a bounded R1 packet; a worker can receive it only after committed hash-bound continuity and actual pre-dispatch PASS.

independentProbeDisposition: FAIL_INDEPENDENT_PROBE
probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER
probeExecutorActor: local-s05-s1-static-reviewer
probeCommandOrMethod: separately authored read/hash/AST oracle; no worker-source evaluation
probeObservedResult: source identity/shape checks pass but F-01..F-07 and evidence/process deviations withhold acceptance
oracleSeparationBasis: distinct source oracle and five AST-only mutations, not worker assertions or runtime fixtures

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_dispatch_release_readiness.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_independent_review_probe_admission.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | first-section envelope; acceptance ledger; gate-role graph; SCEC predecessor/retained counters/escalation; trace/delta fields; standalone independent-probe declaration |
| gateRunPurpose | Validate Local review and consolidated repair evidence before release |
| claimBoundary | Declaration/static evidence only; not runtime enforcement |

Additional current source reads: check_review_cost_control.py REWORK fields; check_semantic_convergence_control.py predecessor/streak; check_dispatch_scaffold_provenance.py required fields; check_independent_review_probe_admission.py FAIL disposition. Previous reviewed source/literal contracts reused within this session, no invented read acknowledgment.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local reviewer/dispatcher |
| Provider or surface | private shared CVF workspace |
| Session or invocation | CVF-NCR-S05-S1-SUPERVISOR-SOURCE |
| Working directory | repository root |
| Command or tool surface | returned-source read/hash/AST oracle, operator relay reconciliation and bounded structural review |
| Target paths | `docs/baselines/CVF_GC018_CVF_NCR_S05_S1_SUPERVISOR_SOURCE_R1_2026-10-03.md`; `docs/reference/CVF_NCR_S05_SUPERVISOR_SOURCE_CONTRACT_R1_2026-10-03.md`; `docs/reviews/CVF_CVF_NCR_S05_S1_SUPERVISOR_SOURCE_LOCAL_REVIEW_2026-10-03.md`; `docs/reviews/CVF_CVF_NCR_S05_S1_SUPERVISOR_SOURCE_WORKER_RETURN_2026-10-03.md`; `docs/reviews/evidence/cvf-ncr-s05-s1-supervisor-source-local-findings-2026-10-03.json`; `docs/reviews/evidence/cvf-ncr-s05-s1-supervisor-source-local-static-oracle-2026-10-03.py`; `docs/reviews/evidence/cvf-ncr-s05-s1-supervisor-source-r1-inputs-2026-10-03.json`; `docs/reviews/evidence/cvf-ncr-s05-s1-supervisor-source-worker-2026-10-03.json`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_S05_S1_SUPERVISOR_SOURCE_R1_2026-10-03.md` |
| Allowed scope source | operator explicitly instructed orchestrator/reviewer to create work order |
| Before status evidence | HEAD `c8864ba03df504e7a8aa991f4bd14d7ef37b7a52`; two untracked original worker outputs, zero tracked modifications |
| After status evidence | review/findings/oracle added; original source and worker return byte hashes preserved |
| Diff evidence | git diff --name-status; git diff --check; git status --short --untracked-files=all |
| Approval boundary | manual worker relay after actual bound gate; no dispatcher worker/provider invocation |
| Claim boundary | source contract/admission only, no native proof |
| Agent type | INTERNAL_AGENT dispatcher |
| Invocation ID | cvf-ncr-s05-s1-source-dispatch-20261003 |
| Expected manifest | `docs/baselines/CVF_GC018_CVF_NCR_S05_S1_SUPERVISOR_SOURCE_R1_2026-10-03.md`; `docs/reference/CVF_NCR_S05_SUPERVISOR_SOURCE_CONTRACT_R1_2026-10-03.md`; `docs/reviews/CVF_CVF_NCR_S05_S1_SUPERVISOR_SOURCE_LOCAL_REVIEW_2026-10-03.md`; `docs/reviews/CVF_CVF_NCR_S05_S1_SUPERVISOR_SOURCE_WORKER_RETURN_2026-10-03.md`; `docs/reviews/evidence/cvf-ncr-s05-s1-supervisor-source-local-findings-2026-10-03.json`; `docs/reviews/evidence/cvf-ncr-s05-s1-supervisor-source-local-static-oracle-2026-10-03.py`; `docs/reviews/evidence/cvf-ncr-s05-s1-supervisor-source-r1-inputs-2026-10-03.json`; `docs/reviews/evidence/cvf-ncr-s05-s1-supervisor-source-worker-2026-10-03.json`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_S05_S1_SUPERVISOR_SOURCE_R1_2026-10-03.md` |
| Actual changed set | `docs/baselines/CVF_GC018_CVF_NCR_S05_S1_SUPERVISOR_SOURCE_R1_2026-10-03.md`; `docs/reference/CVF_NCR_S05_SUPERVISOR_SOURCE_CONTRACT_R1_2026-10-03.md`; `docs/reviews/CVF_CVF_NCR_S05_S1_SUPERVISOR_SOURCE_LOCAL_REVIEW_2026-10-03.md`; `docs/reviews/CVF_CVF_NCR_S05_S1_SUPERVISOR_SOURCE_WORKER_RETURN_2026-10-03.md`; `docs/reviews/evidence/cvf-ncr-s05-s1-supervisor-source-local-findings-2026-10-03.json`; `docs/reviews/evidence/cvf-ncr-s05-s1-supervisor-source-local-static-oracle-2026-10-03.py`; `docs/reviews/evidence/cvf-ncr-s05-s1-supervisor-source-r1-inputs-2026-10-03.json`; `docs/reviews/evidence/cvf-ncr-s05-s1-supervisor-source-worker-2026-10-03.json`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_S05_S1_SUPERVISOR_SOURCE_R1_2026-10-03.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | independent supervisor source contract |
| claimDisposition | CLAIM_REJECTED: no runtime behavior proven |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: source will be authored only under bound release; no OS action or source execution |
| invocationBoundary | source writing and static local evidence only |
| interceptionBoundary | no implemented enforcement |
| claimLanguage | proposals, UNKNOWN or NO_GO, cases planned |
| forbiddenExpansion | payload/install/build/upstream import/control mutation/voice/render/provider/public/deploy |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map | docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md |
| Input source | current operator relay recorded in `docs/reviews/evidence/cvf-ncr-s05-s1-supervisor-source-local-findings-2026-10-03.json` |
| Chain map route | operator relay -> Local source comparison -> bounded repair admission |
| Matching local-view guard | governance/compat/check_external_knowledge_intake_routing.py |
| Owner surface | `docs/reference/CVF_NCR_S05_SUPERVISOR_SOURCE_CONTRACT_2026-10-03.md` and Local reviewer |
| Disposition | SOURCE_COMPARISON_RUNTIME_PENDING |
| Claim boundary | operator agreement is input, not runtime proof |

## Finding-To-Governance Learning Disposition

Defect class: WORKER_EXECUTION_ERROR
Learning lane: DOCUMENTATION_ONLY_LEARNING
Next control action: one consolidated R1 source/evidence admission; no new reusable rule needed.

N/A_WITH_REASON: startup/read-ahead/exclusive-creation requirements already exist; exact deviations retained and enforced in R1. No new checker/rule or recursive learning artifact needed.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - named returned-source task, no corpus/all-files-read claim.

## Epistemic Process Block

Expected: static identities and mandatory source refusal seams are present. Observed: identity/AST shape checks pass, semantic/evidence flaws remain. Contradiction disposition: one consolidated finding set, source acceptance withheld. All behavioural counterexamples and OS cases NOT_EXECUTED_PLANNED; costs UNKNOWN.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

Local static review only; no source acceptance, runtime-ready proof, provider effect or public export. Original raw bytes preserved; no worker rewrite or commit. The new repair packet is a separate dispatch artifact.

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Local Authoring Gate Disclosure

First R1 authoring gate found missing/duplicated shape fields in the new Local review/packet before commit and release. Local repaired its own documentary fields; no worker/source changes. Release binding is expected to fail while packet remains uncommitted. This is separate from the worker-reported original five-literal first FAIL.
