# CVF Agent Work Order - MSEA-R13-T1 MinerU Legal Policy Sample Corpus Candidate Qualification

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work_order

Date: 2026-07-03

Batch ID: MSEA-R13-T1

Dispatch base head: 79a0569c

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker role

Reviewer/closer: reviewer/closer

Worker return path: `docs/reviews/CVF_MSEA_R13_T1_MINERU_LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_WORKER_RETURN_2026-07-03.md`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA-R13-T1.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R13_T1_MINERU_LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_2026-07-03.md`

Paired GC-018 baseline:
`docs/baselines/CVF_GC018_MSEA_R13_T1_MINERU_LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_2026-07-03.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-03. Treat relative dates as
unsafe; record concrete dates in the worker return.

Do-not-misread notes: this is candidate qualification only. It does not
authorize document import, corpus population, MinerU runtime, OCR/parser/VLM
execution, provider/live proof, RAG write, schema implementation,
receipt-writer code, checker implementation, adapter implementation,
public-sync, document-truth, extraction-accuracy, legal advice quality, or
production-readiness claims.

Required first actions: read `CVF_SESSION_MEMORY.md`,
`CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`,
`CVF_SESSION/ACTIVE_SESSION_STATE.json`, `AGENT_HANDOFF_V33_2026-07-03.md`,
`docs/reference/guard_orientation/README.md`,
`docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`,
this work order, the paired GC-018 baseline, all Source Verification Block
owner surfaces, and every checker source listed below before writing worker
outputs.

Return contract: create the worker return artifact and companion qualification
ledger, run required gates, leave changes uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Create a CVF-owned qualification ledger that evaluates existing legal-policy
data inputs against the accepted MSEA-R12-T1 MinerU sample-corpus policy.

The worker must not copy or import documents into this repository. The worker
must not execute MinerU. The worker's job is to verify the recorded evidence,
re-check availability/hash where safe, map candidates to sample slots, list
provenance gaps, and recommend the next governed route.

## Authority Chain

| Authority | Evidence |
|---|---|
| Operator request | operator named a legal-policy data analysis use case with existing data input on 2026-07-03 |
| Active session state | mode routes to operator next MinerU route decision after MSEA-R12-T1 acceptance |
| Accepted sample policy | `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md` |
| Legal-policy corpus evidence | LPCI2-T4S/T4/T5/T11/T11B governed artifacts cited in the Source Verification Block |
| Paired baseline | `docs/baselines/CVF_GC018_MSEA_R13_T1_MINERU_LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_2026-07-03.md` |

## Agent Roles

| Role | Assignment | Boundary |
|---|---|---|
| Dispatcher | dispatch author | authors and commits dispatch packet only |
| Worker | delegated worker role | creates pending worker return and companion reference ledger only |
| Reviewer/closer | reviewer/closer role | reviews, repairs allowed-scope defects, commits material if accepted |
| Operator | operator | required for corpus population, file import, runtime execution, provider/live proof, public-sync, schema/writer/checker/adapter work, or legal-advice/product claims |

## Required First Reads

| Order | Required read |
|---|---|
| 1 | `CVF_SESSION_MEMORY.md` |
| 2 | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| 3 | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| 4 | `AGENT_HANDOFF_V33_2026-07-03.md` |
| 5 | `docs/reference/guard_orientation/README.md` |
| 6 | `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` |
| 7 | paired GC-018 baseline and this work order |
| 8 | `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md` |
| 9 | LPCI2-T4S/T4/T5/T11/T11B evidence cited in Source Verification |
| 10 | checker source listed in the dispatch and worker-output read-ahead blocks |

## Pre-Flight Checks

| Check | Command or evidence |
|---|---|
| Capture base | `git rev-parse --short HEAD` |
| Capture worktree | `git status --short` |
| Confirm output paths absent | `Test-Path` for named worker return and ledger |
| Confirm external bundle availability | `Test-Path -LiteralPath 'D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\Law use case_Codex'` |
| Read output checkers | worker records checker paths and literal tokens before writing outputs |

## Write Ownership

| Actor | Owned paths |
|---|---|
| Worker | `docs/reviews/CVF_MSEA_R13_T1_MINERU_LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_WORKER_RETURN_2026-07-03.md`; `docs/reference/CVF_MSEA_R13_T1_MINERU_LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_LEDGER_2026-07-03.md` |
| Reviewer/closer | allowed-scope repair to worker-owned material artifacts and optional completion review only if required |
| Session-sync steward | active session and handoff surfaces only after accepted material commit |

Forbidden worker changes:

- any files under the operator-local data-input bundle;
- sample documents, generated corpus files, source mirror files, external repo
  clones, legacy folders, package/runtime/checker files, generated aggregates,
  public-sync files, Web/MCP/model-router files, session state, handoff, or
  active front-door files;
- schema implementation, receipt-writer code, adapter code, tests that imply
  runtime behavior, provider/live proof, S3 credentials, Docker build/run, RAG
  index write, package activation, or production-readiness evidence.

## Review Gate

Reviewer/closer must run worker-return fast gate and reviewer-return steward
preflight before accepting material closure. Worker output with failed required
gates must be repaired in allowed scope or returned as `BLOCKED_WITH_REASON`.

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly by reading the
failing checker source and matching the literal required shape. Worker should
return to orchestrator only for a source contradiction, missing data path,
forbidden-scope need, or missing authority that makes completion impossible.

If the external bundle is unavailable at execution time, worker must not ask
whether to proceed with runtime or import. Worker should return
`BLOCKED_WITH_REASON` or create a bounded ledger using governed LPCI evidence
only, explicitly marking filesystem re-verification as blocked.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R13-T1 --title "MinerU Legal Policy Sample Corpus Candidate Qualification" --date 2026-07-03 --base 79a0569c --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced placeholders with R12-T1 policy, LPCI legal-policy corpus evidence, T11 real-use-case bundle evidence, bounded qualification outputs, and no-runtime/no-import boundaries. |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_agent_operation_trace.py` |
| docOnlyNewFields | legal-policy candidate set; sample-slot fit; intake-provenance gap; future corpus-population readiness class; MinerU route implication |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | No mandatory ADIF defectIds apply. Worker still must obey output-artifact checker read-ahead and literal-format gotchas. |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | Dispatch Prompt Envelope; Status: DISPATCH_READY; Source Verification Block columns; ACCEPT; REJECT; BLOCKED_SOURCE_NOT_FOUND; Roadmap-to-Work-Order Trace Matrix; Negative Search And Collision Discipline; Agent Handoff Contract Control Block; Reviewer Closure Conversion; WORKER_MUST_NOT_COMMIT; WORKER_RETURN_FULL_GATE_V1; CHECKER_SAFE_SKELETON_REQUIRED; External Knowledge Intake Routing field labels; external repo or copied folder; External Absorption Core field labels; ledger_terminal=; DOCTRINE_ADAPTED, RUNTIME_CANDIDATE, CHECKER_CANDIDATE, REJECT_DIRECT_IMPORT, NO_PACKAGE_OR_RUNTIME_VALUE; Corpus verdict bullet; Rescan intelligence verdict; Delta Execution Claim Boundary Control Block fields; DEFERRED_PRIVATE_ONLY |
| gateRunPurpose | Confirmation evidence after dispatcher checker read-ahead; not first discovery. |
| claimBoundary | Read-ahead covers this dispatch packet only. Worker-created review/reference outputs must perform their own checker-source read-ahead by docType before writing. |

## Worker Output Checker Read-Ahead Mandate

Before writing the worker return or companion ledger, worker must read the
checker source as applied to each output file's docType, path family, and
conditional content class.

| Output artifact | Required checker source read-ahead before writing |
|---|---|
| Worker return under the reviews area | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_agent_operation_trace.py` |
| Reference ledger under the reference area | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_agent_operation_trace.py` |

The worker return must state that this read-ahead happened before writing the
outputs, list exact literal headings/tokens reviewed, and use gate runs as
confirmation evidence, not first discovery.

## Evidence Reuse And Encoding Plan

verificationMode: REUSE_PRIOR_VERIFICATION
priorVerificationArtifact: docs/reference/CVF_LPCI2_T11B_SOURCE_VERIFICATION_REPORT_2026-06-07.md
priorVerificationAnchor: HASH_MATCH verification rows plus LPCI2-T4S/T4/T5 legal-policy evidence
freshRecomputeRequired: NO
unicodePathHandling: use literal paths and UTF-8-safe readers for any existing filename evidence
extractedTextAuthority: AUXILIARY_ONLY

| Field | Value |
|---|---|
| verificationMode | REUSE_PRIOR_VERIFICATION |
| Prior verification mode | REUSE_PRIOR_VERIFICATION plus worker re-check of external bundle availability and hashes where safe |
| Prior evidence sources | LPCI2-T4S/T4/T5/T11/T11B governed artifacts cited in the Source Verification Block |
| Recompute requirement | Worker must recompute `Test-Path` and may recompute hash/size for T11B target source files without mutating files |
| unicodePathHandling | Use existing-filename exception only for source evidence; use `-LiteralPath` for filesystem calls; prefer artifact IDs or ASCII labels in agent-authored prose |
| extractedTextAuthority | AUXILIARY_ONLY |
| Unicode evidence boundary | Existing Vietnamese filenames are source evidence only; agent-authored prose should use artifact IDs or ASCII labels where possible |
| Encoding mitigation | Worker must use `-LiteralPath` for PowerShell filesystem calls and UTF-8 safe output for any script printing filenames |
| Claim boundary | Reused evidence supports candidate qualification only; it does not prove document truth, extraction accuracy, legal advice quality, runtime behavior, or corpus-population readiness |

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
|---|---|
| Applicability | NOT_APPLICABLE_WITH_REASON: this is not legacy absorption coverage work and does not reopen a legacy coverage index item |
| Coverage index row evidence | N/A with reason: no legacy coverage row is accepted, modified, or closed by this dispatch |
| Claim boundary | no legacy copied folder, historical adapter, or prior absorption source is promoted to current authority |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Storage layout change | NOT_APPLICABLE_WITH_REASON: dispatch creates documentation packets only |
| Durable governance foundation file change | none authorized for worker |
| Generated aggregate change | none authorized for worker |
| External bundle storage | read-only operator-local evidence; no copy/import/move/write authorized |
| Claim boundary | no corpus storage, source import, generated aggregate mutation, RAG index, S3, package, runtime storage, or production storage claim |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| R12-T1 requires operator-supplied documents meeting intake/provenance policy before sample corpus population | VALUE_SET | `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md` | `## Sample Intake And Provenance Policy`; `## Operator Handoff Requirements`; `## Held-Lane Reopen Routing` | Sample Intake And Provenance Policy | MSEA-R12-T1 policy reference | ACCEPT |
| R12-T1 defines sample slots but no sample files | VALUE_SET | `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md` | `## Sample Corpus Slot Taxonomy`; `## Explicit Non-Claims` | Sample files present now | MSEA-R12-T1 policy reference | ACCEPT |
| LPCI2-T4S recorded two operator-supplied DOCX legal-policy files with hashes | VALUE_SET | `docs/reviews/CVF_LPCI2_T4S_POLICYLOCAL_DATA_INPUT_SMOKE_TEST_COMPLETION_2026-06-04.md` | `## Evidence Trace Block`; `## Completion Summary` | Source hashes | LPCI2-T4S completion review | ACCEPT |
| LPCI2-T4 extracted and classified the two PolicyLocal DOCX files as legal-policy corpus evidence | VALUE_SET | `docs/reviews/CVF_LPCI2_T4_CORPUS_INTELLIGENCE_IMPORT_CLASSIFICATION_EVIDENCE_COMPLETION_2026-06-04.md` | `## Classification Ledger`; `## Corpus Intelligence Classification` | LEGAL_POLICY_CORPUS | LPCI2-T4 completion review | ACCEPT |
| LPCI2-T5 deep scan upgraded the two DOCX files to READ_DEEP and confirmed effectiveDate | VALUE_SET | `docs/reviews/CVF_LPCI2_T5_POLICYLOCAL_DEEP_CLASSIFICATION_COMPLETION_2026-06-04.md` | `## Corpus Intelligence Classification`; `## Knowledge System Reconciliation`; `## Findings` | READ_DEEP | LPCI2-T5 completion review | ACCEPT |
| LPCI2-T11 real use-case bundle inventory records 16 artifacts, including source inputs and ungoverned derived outputs | VALUE_SET | `docs/reference/CVF_LPCI2_T11_REAL_USE_CASE_BUNDLE_INVENTORY_2026-06-07.md` | `## Bundle Inventory Table`; `## Role Counts`; `## Lineage Map` | Bundle Artifact Role | LPCI2-T11 bundle inventory | ACCEPT |
| LPCI2-T11B verified seven target files by path, hash, size, role, and lineage | VALUE_SET | `docs/reference/CVF_LPCI2_T11B_SOURCE_VERIFICATION_REPORT_2026-06-07.md` | `## Verification Summary`; `## Four-Gate Result Table` | HASH_MATCH | LPCI2-T11B source verification report | ACCEPT |
| T11 ungoverned extracted text and rendered variants must not be promoted without separate authorization | VALUE_SET | `docs/reference/CVF_LPCI2_T11_REAL_USE_CASE_BUNDLE_INVENTORY_2026-06-07.md` | `## Ungoverned Codex Baseline Summary`; `## Claim Boundary` | ungovernedCodexBaseline | LPCI2-T11 bundle inventory | ACCEPT |
| Worker-return full-gate profile is a dispatch-quality recognized contract | EXISTS | `governance/compat/check_work_order_dispatch_quality.py` | `WORKER_RETURN_FULL_GATE_PROFILE`; `WORKER_RETURN_FULL_GATE_REQUIRED_TERMS` | WORKER_RETURN_FULL_GATE_V1 | work-order dispatch-quality checker | ACCEPT |
| WORKER_MUST_NOT_COMMIT requires handoff control and reviewer conversion | EXISTS | `governance/compat/check_agent_handoff_boundary.py` | `REQUIRED_BLOCK_FIELDS`; `REVIEWER_CONVERSION`; `WORKER_MUST_NOT_COMMIT` | Agent Handoff Contract Control Block | handoff boundary checker | ACCEPT |

## New Doc-Only Fields

| Field | Required worker treatment |
|---|---|
| legal-policy candidate set | define candidate groups from governed LPCI evidence; do not create or copy files |
| sample-slot fit | map each source candidate to R12-T1 slot taxonomy |
| intake-provenance gap | record missing source identity, permission/license, privacy/redaction, slot, size/format, or proof-use confirmation evidence |
| future corpus-population readiness class | classify whether candidate can proceed to a later corpus-population work order or remains blocked |
| MinerU route implication | recommend next route without releasing held runtime/schema/writer/checker lanes |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Baseline path existence before authoring | `Test-Path docs\baselines\CVF_GC018_MSEA_R13_T1_MINERU_LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_2026-07-03.md` returned `False` | PASS |
| Work-order path existence before authoring | `Test-Path docs\work_orders\CVF_AGENT_WORK_ORDER_MSEA_R13_T1_MINERU_LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_2026-07-03.md` returned `False` | PASS |
| Planned worker-return path existence before authoring | `Test-Path docs\reviews\CVF_MSEA_R13_T1_MINERU_LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_WORKER_RETURN_2026-07-03.md` returned `False` | PASS |
| Planned ledger path existence before authoring | `Test-Path docs\reference\CVF_MSEA_R13_T1_MINERU_LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_LEDGER_2026-07-03.md` returned `False` | PASS |
| Collision search for R13-T1 dispatch tokens | search roots: `docs\baselines docs\work_orders docs\reviews docs\reference docs\roadmaps CVF_SESSION`; search command/query: `rg -n "MSEA-R13|LEGAL_POLICY_SAMPLE_CORPUS|MINERU_LEGAL_POLICY_SAMPLE" docs\baselines docs\work_orders docs\reviews docs\reference docs\roadmaps CVF_SESSION`; coverage: source/tests/docs/JSON/external evidence were represented by these governed roots plus cited external manifests; same-token collision result: `DOC`, `literalTokensReviewed`, `CHECKER_SAFE_SKELETON`, `WORKER_MUST_NOT_COMMIT`, and `WORKER_RETURN_FULL_GATE_V1` have non-authoritative repo occurrences and are not treated as absent; absent-versus-collision disposition: R13 path tokens absent, generic governance tokens are collisions with different meaning | PASS |
| Collision decision | No existing R13 artifact found; dispatch path is new | DISPATCH_ALLOWED |

## Roadmap-to-Work-Order Trace Matrix

| Requirement source | Requirement | Worker instruction | Required output evidence |
|---|---|---|---|
| R12-T1 Sample Intake And Provenance Policy | source identity, permission/license, privacy/redaction, slot assignment, format/size, and proof-use confirmation must be present before future sample intake | evaluate both legal-policy candidate sets against these fields | ledger intake-provenance table |
| R12-T1 Sample Corpus Slot Taxonomy | future samples should cover varied document classes | map each source candidate to one or more slots | ledger sample-slot fit matrix |
| R12-T1 Held-Lane Reopen Routing | sample corpus population still requires fresh GC-018 and operator-supplied documents | recommend future route and held lanes without implementing anything | ledger route recommendation |
| LPCI2-T11/T11B evidence | bundle source inputs and request are hash/lineage verified; derived outputs are ungoverned | separate source inputs from ungoverned outputs | ledger source-classification table |
| MSEA claim boundary | no document truth, extraction accuracy, legal advice quality, or production claim | keep explicit non-claims | worker return and ledger claim boundary |

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake summary | Operator named a concrete legal-policy data analysis use case with existing data input after MSEA-R12-T1 policy acceptance. |
| Scope classification | documentation/reference candidate qualification worker dispatch |
| Risk sensitivity | R1 documentation qualification; legal-policy subject matter is high-risk, so all legal advice/current-law/document-truth claims are forbidden |
| Selected route mode | MULTI_AGENT_MULTI_ROLE |
| Intake role | Worker qualifies candidates only; operator owns any later corpus-population authorization |
| Worker authority | READ accepted owner surfaces and operator-local bundle metadata; WRITE only the named review and reference artifacts |
| Reviewer authority | Reviewer/closer may repair allowed-scope shape defects and commit material outputs if accepted |
| Operator checkpoint | Required before actual corpus population, file import, runtime execution, schema/writer/checker/adapter work, provider/live proof, or public-sync |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher -> worker -> reviewer/closer -> session-sync steward |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=79a0569c; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | dispatch owns paired GC-018/work order; worker owns named worker return and reference ledger only; reviewer owns material closure; session-sync steward owns active state/handoff only after accepted material commit |
| traceScope(phase, actor) | dispatcher AOT in this work order and baseline; worker AOT in worker return and ledger; reviewer/closer records reviewer decision before commit |
| commitOwner(phase) | dispatcher commits dispatch; worker must not commit; reviewer/closer commits material; session-sync steward commits session-sync separately |
| crossBatchIsolation | do not modify prior MSEA, LPCI, runtime, source, public, package, checker, session, or handoff files during worker execution |
| nextMoveSurfaces | reviewer/closer and session-sync steward update next allowed move only after accepted material closure |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | optional; prefer adding reviewer decision to worker return unless a separate completion review is required by defects |
| reviewerOwnedClosurePaths | worker return and companion qualification ledger; optional completion review if created by reviewer |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| `docs/reviews/CVF_MSEA_R13_T1_MINERU_LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_WORKER_RETURN_2026-07-03.md` | CREATE worker return with executionBaseHead, output-artifact checker read-ahead evidence, command evidence, git status, no-commit statement, and claim boundary |
| `docs/reference/CVF_MSEA_R13_T1_MINERU_LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_LEDGER_2026-07-03.md` | CREATE reference ledger with candidate sets, source verification summary, sample-slot fit, intake-provenance gaps, rejected derived-output boundary, route recommendation, and claim boundary |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R13_T1_MINERU_LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_WORKER_RETURN_2026-07-03.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Worker return must include review structural headings, `## Target / Source`,
`## Scope / Methodology`, `## Findings / Position`, `## Risk / Corrective Action`,
`## Decision / Recommendation`, checker read-ahead, AOT, Delta block, public
export disposition, external-intake routing, external-absorption core,
value-conversion matrix, overlap classification, corpus completeness,
rescan-intelligence disposition, finding-to-governance learning disposition,
epistemic process block, machine-closure N/A line, git status, and no-commit
statement.

## Execution Plan

| Step | Worker action | Evidence |
|---|---|---|
| 1 | Capture executionBaseHead and git status before edits | worker return |
| 2 | Read startup surfaces, baseline, work order, source owner surfaces, and output-artifact checkers | worker return Source Inventory and Checker Source Read-Ahead Block |
| 3 | Re-check operator-local bundle root availability and, if safe, hash/size target source files against T11B evidence | worker return and ledger source verification summary |
| 4 | Evaluate the two LPCI candidate sets: T4S/T4/T5 two-DOCX law set and T11/T11B real-use-case bundle | qualification ledger |
| 5 | Map source candidates to R12-T1 sample slots and mark missing slot coverage | qualification ledger slot-fit matrix |
| 6 | Evaluate intake/provenance readiness and identify operator-owned gaps | qualification ledger |
| 7 | Reject direct promotion of ungoverned extracted text and rendered variants | qualification ledger |
| 8 | Recommend next governed route: corpus-population work order, additional provenance collection, or hold | worker return Decision / Recommendation |
| 9 | Run pre-implementation and worker-return gates; repair allowed-scope defects | command evidence |
| 10 | Return COMPLETE_PENDING_REVIEW without committing, staging, pushing, or session-sync editing | worker return and git status |

## Required Reference Ledger Sections

The companion ledger must include these sections or equivalent clearer
headings:

| Required section | Content boundary |
|---|---|
| Scope / Applies To | qualification only; no corpus population |
| Source Basis | R12-T1 policy and LPCI evidence |
| Candidate Set Inventory | distinguish T4/T5 two-DOCX law set and T11 real-use-case bundle |
| Source Verification Summary | cite T4S/T4/T5/T11/T11B and any execution-time path/hash recheck |
| Sample Slot Fit Matrix | map candidates to R12-T1 sample slots |
| Sample Intake Provenance Gap Matrix | source identity, permission/license, privacy/redaction, slot, format/size, proof-use confirmation |
| Rejected Derived Output Boundary | ungoverned extracted text and rendered variants are not source samples |
| MinerU Route Implication | recommend next route without opening runtime/schema/writer/checker now |
| External Knowledge Intake Routing | machine-shaped field/value table |
| External Absorption Core | machine-shaped field/value table and ledger_terminal markers |
| External Absorption Value Conversion Matrix | required lanes including DOCTRINE_ADAPTED, RUNTIME_CANDIDATE, CHECKER_CANDIDATE, REJECT_DIRECT_IMPORT, NO_PACKAGE_OR_RUNTIME_VALUE |
| Overlap And Novelty Classification | compare against R12-T1 and LPCI owner surfaces |
| Corpus Completeness And Report Integrity | honest qualification-scope verdict |
| Rescan Intelligence Hardening | verdict and reason |
| Delta Execution Claim Boundary Control Block | reject execution/runtime/control claims |
| Public Export Disposition | DEFERRED_PRIVATE_ONLY |
| Agent Operation Trace Block | full trace label set |
| Claim Boundary | explicit no-runtime/no-import/no-production boundary |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | operator-named legal-policy data input plus accepted LPCI evidence -> accepted MSEA-R12-T1 sample-corpus policy -> R13-T1 candidate qualification ledger |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_corpus_completeness_report_integrity.py` |
| Owner surface | this work order |
| Disposition | ADAPT: dispatch a CVF-owned candidate qualification tranche from accepted legal-policy and MinerU sample-corpus evidence |
| Claim boundary | dispatch-only; no runtime/provider/live/S3/RAG/Docker/package/checker/source-import/schema/receipt-writer/adapter implementation/public-sync/production claim |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | existing governed LPCI evidence plus operator-local legal-policy use-case bundle recorded by LPCI2-T11; no source copy into this repository |
| Enumeration command | `Test-Path -LiteralPath 'D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\Law use case_Codex'` returned `True` during dispatch authoring |
| Manifest artifact or inline manifest | `docs/reference/CVF_LPCI2_T11_REAL_USE_CASE_BUNDLE_INVENTORY_2026-06-07.md`; `docs/reference/CVF_LPCI2_T11B_SOURCE_VERIFICATION_REPORT_2026-06-07.md` |
| Processing ledger artifact or inline ledger | this work order |
| Ledger terminal statuses | READ, SOURCE_VERIFIED, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, SKIPPED_WITH_REASON, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | MSEA-R12-T1 policy; LPCI2-T4S/T4/T5/T11/T11B evidence |
| Unresolved items | actual permission/license and privacy/redaction confirmation may remain operator-owned until a later corpus-population tranche |
| Completion claim boundary | dispatch only; no corpus population, document import, runtime execution, source import, provider/live proof, RAG write, schema/writer/adapter/checker work |

ledger_terminal=READ for accepted MSEA and LPCI owner surfaces; ledger_terminal=SOURCE_VERIFIED for source-verification evidence cited from LPCI2-T11B and external path availability; ledger_terminal=ADAPTED for the R13-T1 qualification route; ledger_terminal=DEFERRED for corpus population and implementation-facing lanes; ledger_terminal=REJECTED for direct promotion of ungoverned extracted text/rendered outputs; ledger_terminal=NO_NEW_VALUE for already-owned legal-policy evidence.

## Corpus Completeness And Report Integrity

- Corpus task class: dispatch authoring for legal-policy candidate qualification.
- Corpus root: governed LPCI evidence plus operator-local bundle recorded by LPCI2-T11.
- Snapshot time: 2026-07-03 dispatch authoring.
- Enumeration command: `Get-ChildItem -LiteralPath 'D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\Law use case_Codex' -Recurse -File` returned filesystem-backed evidence for the operator-local bundle during dispatch authoring; T11 records 16 artifacts and T11B verifies 7 target files.
- Manifest artifact or inline manifest: `docs/reference/CVF_LPCI2_T11_REAL_USE_CASE_BUNDLE_INVENTORY_2026-06-07.md`; `docs/reference/CVF_LPCI2_T11B_SOURCE_VERIFICATION_REPORT_2026-06-07.md`.
- Manifest hash: T11B hash rows for seven target files; T4S hash rows for two PolicyLocal DOCX files.
- Processing ledger artifact or inline ledger: this work order.
- Allowed terminal statuses: READ | SOURCE_VERIFIED | ADAPTED | DEFERRED | REJECTED | NO_NEW_VALUE | SKIPPED_WITH_REASON | BLOCKED_UNREADABLE.
- Reconciliation: manifest=T11/T11B/T4S/T4/T5 governed evidence; ledger_terminal=READ/SOURCE_VERIFIED/ADAPTED/DEFERRED/REJECTED/NO_NEW_VALUE/SKIPPED_WITH_REASON/BLOCKED_UNREADABLE for dispatch scope; exclusions=corpus population, document import, MinerU runtime execution, provider/live proof, source import, schema implementation, receipt-writer code, adapter implementation, production-readiness claims; unresolved=0 for dispatch scope.
- Unresolved files: none for dispatch authoring; worker must record any filesystem/hash drift found during execution.
- Declared exclusions: sample document import, corpus population, full body extraction, MinerU runtime, provider/live proof, RAG write, source import, schema implementation, receipt-writer code, adapter implementation, checker implementation, production-readiness claims.
- Unreadable or unsupported files: none identified for dispatch authoring.
- Aggregation check: accepted LPCI and MSEA owner surfaces are cited instead of regenerated into a new corpus aggregate.
- Drift check: external bundle root existed during dispatch authoring; worker must re-check at execution start.
- Output traceability: this work order routes only to the two named worker-owned artifacts.
- Adversarial verification: dispatch rejects direct promotion of ungoverned extracted text, generated petition variants, document-truth, extraction-accuracy, legal advice quality, and production readiness.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Knowledge System Reconciliation

- Knowledge task class: LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_DISPATCH
- Source manifest: `docs/reference/CVF_LPCI2_T11_REAL_USE_CASE_BUNDLE_INVENTORY_2026-06-07.md`; `docs/reference/CVF_LPCI2_T11B_SOURCE_VERIFICATION_REPORT_2026-06-07.md`; LPCI2-T4S/T4/T5 completion evidence.
- Source manifest hash: T11B SHA-256 rows for 7 target files and T4S SHA-256 rows for 2 PolicyLocal DOCX files.
- Enumeration safety: SAFE - filesystem-backed `Get-ChildItem -LiteralPath` evidence plus governed T11/T11B/T4S/T4/T5 manifests; no dynamic source import.
- Intake registry or ledger: future R13-T1 qualification ledger assigned to worker output.
- Authority assets: assets=3 candidate groups: T4/T5 two-DOCX law set, T11 source-input bundle, T11 ungoverned derived-output group.
- Derived views: none created by dispatch; worker may create only the reference qualification ledger.
- Semantic region ledger: LEGAL_POLICY_CORPUS/VN_NATIONAL for T4/T5 law evidence; LEGAL_POLICY_USE_CASE_CANDIDATE for T11 source-input bundle; REJECT_DIRECT_IMPORT for ungoverned derived outputs.
- Region reconciliation: assets=3; mapped=1; deferred=2; unmapped=0
- Orphan or unmapped assets: none
- Cross-region links: none; all candidate groups remain legal-policy/document-extraction qualification inputs.
- Drift check: PASS
- Rebuildability check: PASS - dispatch cites governed manifests and requires worker re-check of external availability.
- Retrieval boundary: no retrieval, search, vector, RAG, or runtime query is authorized.
- Adversarial verification: legal advice, current-law correctness, document-truth, extraction-accuracy, and runtime claims are explicitly rejected.
- Knowledge-map verdict: RECONCILED_WITH_DECLARED_GAPS

## Corpus Intelligence Classification

- Classification task class: LEGAL_POLICY_SAMPLE_CORPUS_CANDIDATE_QUALIFICATION_DISPATCH
- Source corpus evidence: LPCI2-T4S/T4/T5 two-DOCX law evidence plus LPCI2-T11/T11B real-use-case bundle evidence.
- Knowledge map evidence: RECONCILED_WITH_DECLARED_GAPS - qualification dispatch only; corpus population remains deferred.
- Classification ledger: inline Corpus Intelligence Classification Ledger below.
- Legal/policy corpus: YES - legal-policy candidate evidence only; no legal advice quality or current-law correctness claim.
- Domain fields: jurisdiction=VN_NATIONAL where source evidence supports it; authorityLevel=law or source_input_candidate; effectiveDate=2026-07-01 for T4/T5 law set and unknown for T11 bundle; sourceAuthority=Quoc Hoi for T4/T5 and operator-local bundle evidence for T11; answerBoundary=SUMMARY_WITH_SOURCE and ESCALATE_OR_ABSTAIN only.
- Response Boundary: DIRECT_CITED_ANSWER blocked; SUMMARY_WITH_SOURCE candidate only; PROCEDURAL_GUIDANCE blocked until later review; ESCALATE_OR_ABSTAIN required for legal advice/current-law/applicability requests.
- Adversarial sampling plan: deferred to worker qualification ledger and any later corpus-population/runtime tranche; dispatch rejects answer behavior.
- Classification verdict: DEEP_CLASSIFIED_WITH_DECLARED_GAPS

### Corpus Intelligence Classification Ledger

| sourcePath | processingStatus | knowledgeRegion | ownerSurface | disposition | answerClass | domainFields | evidencePointer |
|---|---|---|---|---|---|---|---|
| LPCI2-T4T5-two-DOCX-law-set | READ_DEEP | LEGAL_POLICY_CORPUS | GOVERNANCE_LAYER | ACCEPT_SUMMARY_ONLY | SUMMARY_WITH_SOURCE | jurisdiction=VN_NATIONAL; authorityLevel=law; effectiveDate=2026-07-01; sourceAuthority=Quoc Hoi; answerBoundary=SUMMARY_WITH_SOURCE | LPCI2-T4/T5 completion evidence; qualification only |
| LPCI2-T11-source-input-bundle | DEFERRED | LEGAL_POLICY_CORPUS | GOVERNANCE_LAYER | DEFER | ESCALATE_OR_ABSTAIN | jurisdiction=unknown; authorityLevel=source_input_candidate; effectiveDate=unknown; sourceAuthority=operator-local bundle evidence; answerBoundary=ESCALATE_OR_ABSTAIN | T11/T11B evidence; worker must qualify provenance gaps |
| LPCI2-T11-ungoverned-derived-outputs | DEFERRED | LEGAL_POLICY_CORPUS | GOVERNANCE_LAYER | REJECT | ESCALATE_OR_ABSTAIN | jurisdiction=unknown; authorityLevel=derived_output; effectiveDate=unknown; sourceAuthority=ungoverned baseline only; answerBoundary=ESCALATE_OR_ABSTAIN | T11 ungoverned baseline summary; direct promotion rejected |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| R12-T1 sample-corpus policy | intake/provenance and slot taxonomy requirements | DOCTRINE_ADAPTED | R13-T1 qualification ledger | apply policy to legal-policy candidates | no corpus population |
| LPCI2-T4S/T4/T5 two-DOCX law evidence | existing legal-policy law corpus evidence with hashes and READ_DEEP classification | DOCTRINE_ADAPTED | R13-T1 qualification ledger | classify sample-slot fit and provenance gaps | no MinerU execution |
| LPCI2-T11/T11B real-use-case bundle | source PDFs/DOCX plus agent request with hash/lineage verification | DOCTRINE_ADAPTED | R13-T1 qualification ledger | classify candidate readiness and gaps | no source import |
| MSEA runtime/parser/RAG/provider lanes | legal-policy use case may satisfy operator-named-use-case condition only after qualification | RUNTIME_CANDIDATE | future route decision | defer to fresh GC-018 after qualification | no runtime/provider/RAG action now |
| Overclaim checker lane | legal use case is high-risk for document-truth and legal-advice overclaims | CHECKER_CANDIDATE | future route decision | defer until repeated misses or authorized ingestion | no checker implementation |
| Ungoverned extracted text/rendered outputs | prior outputs are comparison evidence only | REJECT_DIRECT_IMPORT | R13-T1 qualification ledger | reject direct promotion | no source import |
| Existing LPCI evidence | already-owned data-input and classification facts | NO_PACKAGE_OR_RUNTIME_VALUE | predecessor owner surfaces | cite only | no runtime/package behavior |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| R12-T1 sample policy | `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md` | ENRICH_EXISTING | applies policy to a concrete operator-named legal-policy use case | dispatch R13-T1 |
| LPCI2 T4S/T4/T5 two-DOCX law evidence | LPCI2 completion reviews and corpus evidence | CONFIRMED_EXISTING | reused as candidate sample evidence without copying files | cite and qualify |
| LPCI2 T11/T11B real-use-case bundle | T11 bundle inventory and T11B verification report | ENRICH_EXISTING | maps real source inputs to MinerU sample slots and provenance gaps | qualify |
| MSEA runtime/provider/RAG/checker holds | MSEA-R9/R10/R12 held-lane routing | CONFIRMED_EXISTING | legal use case may inform future route but does not release held lanes now | defer |
| Ungoverned extracted text/rendered outputs | T11 ungoverned baseline summary | REJECT_DIRECT_IMPORT | derived outputs are not proof-grade sample source | reject direct promotion |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: this dispatch creates a candidate qualification work order from an
accepted policy and existing LPCI evidence. It is not a broad rescan or
residual repository absorption pass.

## Evidence Requirements

| Evidence | Required shape |
|---|---|
| executionBaseHead | worker captures `git rev-parse --short HEAD` before edits |
| git status before/after | worker return includes actual `git status --short`, not a clean claim if output files are untracked |
| checker read-ahead | worker return lists output-artifact checker sources and literal tokens read before writing |
| source basis | ledger cites R12-T1 policy and LPCI2-T4S/T4/T5/T11/T11B evidence |
| external path check | worker records Test-Path result and any hash/size recheck that does not mutate files |
| gate evidence | worker return lists exact command results for pre-implementation and worker-return fast gate |
| no-commit evidence | worker return states HEAD unchanged and no commit/stage/push |

## Acceptance Criteria

| Criterion | Evidence |
|---|---|
| Qualification ledger exists and is bounded | named reference artifact with required sections |
| Worker return exists and is checker-shaped | named worker return artifact and worker-return fast gate PASS |
| Candidate sets are separated | ledger distinguishes source inputs from ungoverned extracted/rendered outputs |
| R12 slot fit is recorded | ledger maps candidates to sample slots and gaps |
| Intake/provenance gaps are explicit | ledger includes source identity, permission/license, privacy/redaction, slot, format/size, proof-use confirmation status |
| No import/runtime/legal-advice claim | reference and worker return claim boundaries |
| Worktree handoff is no-commit | git status shows only worker-owned artifacts pending |

## Fail Conditions

| Failure | Required result |
|---|---|
| Documents are copied/imported into this repository | BLOCKED_WITH_REASON |
| Corpus population or corpus-existence claim appears | BLOCKED_WITH_REASON |
| MinerU/runtime/schema/writer/adapter/checker/package/provider/live/public implementation appears | BLOCKED_WITH_REASON |
| Document-truth, extraction-accuracy, legal advice quality, or production claim appears | BLOCKED_WITH_REASON |
| Ungoverned extracted text/rendered outputs are promoted as source samples | BLOCKED_WITH_REASON |
| Worker output omits docType-specific checker read-ahead | repair before return |
| Worker commits, stages, pushes, or edits session-sync surfaces | BLOCKED_WITH_REASON |

## Verification Commands

```powershell
git rev-parse --short HEAD
git status --short
Test-Path -LiteralPath 'D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\Law use case_Codex'
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 79a0569c --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git status --short
```

Required dispatcher pre-dispatch command before commit:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 79a0569c --head HEAD
```

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author |
| Provider or surface | local workspace |
| Session or invocation | MSEA-R13-T1 dispatch authoring, 2026-07-03 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, `rg`, source reads, dispatch scaffold helper, external path preflight, `apply_patch`, governance gates |
| Target paths | paired baseline; this work order |
| Allowed scope source | operator-named legal-policy use case; MSEA-R12-T1 accepted policy; LPCI2 legal-policy evidence |
| Before status evidence | clean worktree; `git status --short` empty after MSEA-R12-T1 acceptance session-sync |
| After status evidence | baseline and work order pending pre-dispatch gates |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | operator named a legal-policy data analysis use case with existing data input |
| Claim boundary | dispatch only; no runtime/provider/live/public/package/checker/source-import/schema/receipt-writer/adapter/Web/MCP/model-router/action-authority claim |
| Agent type | dispatcher |
| Invocation ID | `msea-r13-t1-legal-policy-sample-corpus-candidate-qualification-dispatch-2026-07-03` |
| Expected manifest | paired baseline; this work order |
| Actual changed set | paired baseline; this work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename; two new dispatch artifacts |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | MSEA-R13-T1 work-order dispatch |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, provider, parser, adapter, schema, receipt-writer, or production behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed |
| invocationBoundary | local governed dispatch authoring only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, Web runtime, adapter, package, watcher, daemon, parser, RAG index, or production route interception claim |
| claimLanguage | dispatch authorization for documentation/reference candidate qualification only |
| forbiddenExpansion | no document import, corpus population, MinerU runtime, install, model download, parser/OCR/VLM/hybrid/API/router/Gradio/Docker execution, provider/live call, credentials/S3, RAG write, source import, package activation, checker implementation, public-sync, Web/MCP/model-router/action-authority, automatic invocation, benchmark, document-truth, extraction-accuracy, legal advice quality, schema implementation, receipt-writer code, adapter implementation, or production-readiness claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order referencing operator-local legal-policy
data-input evidence. No public-sync export is authorized.

## Operator Checkpoint

Required after reviewer/closer acceptance if the next route would involve any
actual sample document intake, corpus population, runtime execution, schema or
writer implementation, adapter implementation, checker implementation,
provider/live proof, S3 credentials, Docker/package work, RAG write,
public-sync, or production-readiness claim.

## Closure Checklist

| Item | Required closeout disposition |
|---|---|
| Worker return created | PASS or BLOCKED_WITH_REASON |
| Qualification ledger created | PASS or BLOCKED_WITH_REASON |
| Worker-return fast gate run | PASS or BLOCKED_WITH_REASON |
| Pre-implementation autorun run | PASS or BLOCKED_WITH_REASON |
| No forbidden paths changed | PASS or BLOCKED_WITH_REASON |
| No worker commit/stage/push | PASS or BLOCKED_WITH_REASON |
| Reviewer/closer material commit | reviewer/closer owned |
| Session-sync update | session-sync steward owned after accepted material commit |

## Claim Boundary

This work order authorizes only a WORKER_MUST_NOT_COMMIT documentation/reference
candidate qualification worker tranche. It does not authorize or claim sample
document import, corpus population, MinerU installation, parser execution,
OCR/VLM/hybrid routing, remote backend processing, model download,
API/router/Gradio service, Docker deployment, provider/live proof, S3 access,
credential handling, RAG indexing, source import, checker enforcement, package
activation, schema implementation, receipt-writer code, adapter implementation,
public-sync export, document truth, extraction accuracy, legal advice quality,
benchmark, certification, generated aggregate mutation, production readiness,
model-router behavior, action authority, automatic invocation, or universal
document intelligence.
