# CVF Agent Work Order - MSEA-R12-T1 MinerU Sample Corpus Expected Receipt Policy

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work_order

Date: 2026-07-03

Batch ID: MSEA-R12-T1

Dispatch base head: c376ff33

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker role

Reviewer/closer: reviewer/closer

Worker return path: `docs/reviews/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_WORKER_RETURN_2026-07-03.md`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA-R12-T1.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md`

Paired GC-018 baseline:
`docs/baselines/CVF_GC018_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-03. Treat relative dates as unsafe; record concrete dates in the worker return.

Do-not-misread notes: this is policy-definition work only. It does not authorize sample document import, sample corpus population, MinerU install, model download, runtime execution, parser/OCR/VLM/hybrid/API/router/Gradio/Docker action, provider/live call, credentials/S3, RAG write, source import, package activation, checker implementation, Web/MCP/model-router/action-authority, benchmark, document-truth, extraction-accuracy, schema implementation, receipt-writer code, adapter implementation, public-sync, or production-readiness claims.

Required first actions: read `CVF_SESSION_MEMORY.md`, `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`, `CVF_SESSION/ACTIVE_SESSION_STATE.json`, `AGENT_HANDOFF_V33_2026-07-03.md`, `docs/reference/guard_orientation/README.md`, `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`, this work order, the paired GC-018 baseline, and every checker source listed below before writing worker-created artifacts.

Return contract: create the worker return artifact and companion reference, run required gates, leave changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Create a CVF-owned documentation/reference policy for MinerU sample-corpus
selection and expected receipt evidence, using accepted MSEA owner surfaces.

The worker must produce only the named worker return and named policy reference.
The worker must not create or import sample documents, populate a corpus, run
MinerU, implement schema or writer code, implement an adapter or checker, or
claim runtime/provider/live/public/package/production readiness.

## Authority Chain

| Authority | Evidence |
|---|---|
| Operator request | operator asked for the next work order after R11-T1 selected the R12 route |
| Active session state | mode routes to MSEA-R12-T1 GC-018/work-order authoring after session-sync commit `c376ff33` |
| Roadmap source | MSEA-R12 roadmap at material commit `072c15f1` |
| Paired baseline | `docs/baselines/CVF_GC018_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md` |

## Agent Roles

| Role | Assignment | Boundary |
|---|---|---|
| Dispatcher | dispatch author | authors and commits dispatch packet only |
| Worker | delegated worker role | creates pending worker return and companion reference only |
| Reviewer/closer | reviewer/closer role | reviews, repairs allowed-scope defects, commits material if accepted |
| Operator | operator | required for scope expansion, sample document intake, runtime/provider/live proof, public-sync, or implementation |

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
| 8 | Source Verification Block owner surfaces |
| 9 | checker source listed in the dispatch and worker-output read-ahead blocks |

## Pre-Flight Checks

| Check | Command or evidence |
|---|---|
| Capture base | `git rev-parse --short HEAD` |
| Capture worktree | `git status --short` |
| Confirm worker output paths | `Test-Path` for named worker return and policy reference |
| Read output checkers | worker records checker paths and literal tokens before writing outputs |

## Write Ownership

| Actor | Owned paths |
|---|---|
| Worker | `docs/reviews/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_WORKER_RETURN_2026-07-03.md`; `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md` |
| Reviewer/closer | allowed-scope repair to worker-owned material artifacts and optional completion review only if required |
| Session-sync steward | active session and handoff surfaces only after accepted material commit |

## Review Gate

Reviewer/closer must run worker-return fast gate and reviewer-return steward
preflight before accepting material closure. Worker output with failed required
gates must be repaired in allowed scope or returned as `BLOCKED_WITH_REASON`.

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly by reading the
failing checker source and matching the literal required shape. Worker should
return to orchestrator only for a source contradiction, forbidden-scope need,
or missing authority that makes completion impossible.

If workload feels large, execute the full policy-definition scope rather than
asking whether to sample less. This tranche is intentionally documentation-only
and bounded to two output artifacts.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R12-T1 --title "MinerU Sample Corpus Expected Receipt Policy" --date 2026-07-03 --base c376ff33 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced generic placeholders with source-verified MSEA-R12 scope, concrete output paths, policy-definition task list, worker-output checker read-ahead mandate, and held-lane boundaries. |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`; `docs/reference/guard_orientation/README.md`; `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` |
| docOnlyNewFields | sample-corpus slot taxonomy; sample intake and provenance policy; expected receipt assertion classes; expected receipt non-assertions; held-lane reopen routing; operator handoff requirements |
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
| Dispatch impact | No mandatory ADIF defectIds apply. Worker still must obey guard-orientation output-artifact checker read-ahead and literal-format gotchas. |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | Dispatch Prompt Envelope; Status: DISPATCH_READY; Source Verification Block columns; ACCEPT; REJECT; Negative Search And Collision Discipline; Roadmap-to-Work-Order Trace Matrix; Agent Handoff Contract Control Block; Reviewer Closure Conversion; WORKER_MUST_NOT_COMMIT; WORKER_RETURN_FULL_GATE_V1; CHECKER_SAFE_SKELETON_REQUIRED; External Knowledge Intake Routing field labels; ledger_terminal=; DOCTRINE_ADAPTED, RUNTIME_CANDIDATE, PACKAGE_CANDIDATE, CHECKER_CANDIDATE, REJECT_DIRECT_IMPORT, NO_PACKAGE_OR_RUNTIME_VALUE; Corpus verdict bullet; Rescan intelligence verdict; Delta Execution Claim Boundary Control Block fields; DEFERRED_PRIVATE_ONLY |
| gateRunPurpose | Confirmation evidence after dispatcher checker read-ahead; not first discovery. |
| claimBoundary | Read-ahead covers this dispatch packet only. Worker-created review/reference outputs must perform their own checker-source read-ahead by docType before writing. |

## Worker Output Checker Read-Ahead Mandate

Before writing the worker return or companion reference, worker must read the
checker source as applied to each output file's docType, path family, and
conditional content class.

Minimum worker output read-ahead:

| Output artifact | Required checker source read-ahead before writing |
|---|---|
| Worker return under the reviews area | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_agent_operation_trace.py` |
| Reference policy under the reference area | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_agent_operation_trace.py` |

The worker return must state that this read-ahead happened before writing the
outputs, list the exact literal headings/tokens reviewed, and use gate runs as
confirmation evidence, not first discovery.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| MSEA-R12 opens R12-T1 GC-018 and work-order authoring | VALUE_SET | `docs/roadmaps/CVF_MSEA_R12_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_ROADMAP_2026-07-03.md` | `Status:`; `## Work Plan` | `ROADMAP_READY_FOR_MSEA_R12_T1_GC018_AND_WORK_ORDER_AUTHORING` | MSEA-R12 roadmap | ACCEPT |
| R11-T1 selected sample-corpus and expected-receipt-policy route | VALUE_SET | `docs/reference/CVF_MSEA_R11_T1_MINERU_PRODUCTIZATION_READINESS_ROUTE_SELECTION_DECISION_MATRIX_2026-07-03.md` | `## Selected Route`; `## Rationale` | `OPEN_SAMPLE_CORPUS_AND_EXPECTED_RECEIPT_POLICY_ROADMAP` | MSEA-R11-T1 decision matrix | ACCEPT |
| R11-T1 did not define the sample corpus or receipt policy | VALUE_SET | `docs/reference/CVF_MSEA_R11_T1_MINERU_PRODUCTIZATION_READINESS_ROUTE_SELECTION_DECISION_MATRIX_2026-07-03.md` | `## Rationale`; `## Explicit Non-Claims` | sample corpus or expected receipt policy has not been defined | MSEA-R11-T1 decision matrix | ACCEPT |
| R7 owns receipt artifact and field-family vocabulary | EXISTS | `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` | `## Receipt Artifact Family Map`; `## Field Family Map` | Receipt Artifact Family Map; Field Family Map | MSEA-R7 reference | ACCEPT |
| R10 keeps schema and writer implementation unauthorized | VALUE_SET | `docs/reference/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md` | `## Explicit Non-Claims`; `## Claim Boundary` | schema implementation; receipt-writer code | MSEA-R10 reference | ACCEPT |
| R9 keeps runtime/provider/RAG/S3/checker routes held behind concrete conditions | VALUE_SET | `docs/reference/CVF_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_2026-07-02.md` | `## Source-Backed Hold Conditions`; `## Adapter Contract Readiness Matrix` | runtime/provider/RAG/S3/checker hold conditions | MSEA-R9 reference | ACCEPT |
| R8 preserves runtime/package candidates without execution | VALUE_SET | `docs/reference/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md` | `## Candidate And No-Value Ledger`; `## Claim Boundary` | `RUNTIME_CANDIDATE`; `PACKAGE_CANDIDATE` | MSEA-R8 residual ledger | ACCEPT |
| Source mirror is pinned and preferred over legacy copied folder facts | VALUE_SET | `.private_reference/source_mirrors/INDEX.md` | row `opendatalab__MinerU` | `.private_reference/source_mirrors/opendatalab__MinerU/` | source mirror index | ACCEPT |
| WORKER_MUST_NOT_COMMIT work orders require handoff control and reviewer conversion | EXISTS | `governance/compat/check_agent_handoff_boundary.py` | `REQUIRED_BLOCK_FIELDS`; `REVIEWER_CONVERSION`; `WORKER_MUST_NOT_COMMIT` | Agent Handoff Contract Control Block; Reviewer Closure Conversion | handoff boundary checker | ACCEPT |
| Worker-return full-gate profile is a dispatch-quality recognized contract | EXISTS | `governance/compat/check_work_order_dispatch_quality.py` | `WORKER_RETURN_FULL_GATE_PROFILE`; `WORKER_RETURN_FULL_GATE_REQUIRED_TERMS` | `WORKER_RETURN_FULL_GATE_V1` | work-order dispatch-quality checker | ACCEPT |

## New Doc-Only Fields

| Field | Required worker treatment |
|---|---|
| sample-corpus slot taxonomy | define as policy categories only; do not create sample files |
| sample intake and provenance policy | define operator-provided evidence requirements only; do not ingest documents |
| expected receipt assertion classes | define allowed future receipt claims only; do not implement schema |
| expected receipt non-assertions | define forbidden future receipt claims including document truth and extraction accuracy |
| held-lane reopen routing | carry concrete reopen conditions only; do not reopen implementation |
| operator handoff requirements | define future intake checklist only; do not collect documents |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Baseline path existence before authoring | `Test-Path docs\baselines\CVF_GC018_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md` returned `False` | PASS |
| Work-order path existence before authoring | `Test-Path docs\work_orders\CVF_AGENT_WORK_ORDER_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md` returned `False` | PASS |
| Planned worker-return path existence before authoring | `Test-Path docs\reviews\CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_WORKER_RETURN_2026-07-03.md` returned `False` | PASS |
| Planned reference path existence before authoring | `Test-Path docs\reference\CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md` returned `False` | PASS |
| Collision search for R12-T1 dispatch path tokens | `rg -n "CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY|MSEA-R12-T1" docs\baselines docs\work_orders docs\reviews docs\reference docs\roadmaps` with roots `docs\baselines docs\work_orders docs\reviews docs\reference docs\roadmaps` returned only the existing R12 roadmap seed rows before these files were written | PASS |
| Collision decision | Existing roadmap seed is the governing predecessor; this dispatch path is new | DISPATCH_ALLOWED |

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Worker instruction | Required output evidence |
|---|---|---|
| Define sample-corpus slots | Create a slot taxonomy grounded in MinerU document-extraction needs and CVF receipt vocabulary | reference section plus worker-return summary |
| Define intake/provenance requirements | Specify source, permission, privacy, redaction, naming, and provenance facts future operator-provided samples must carry | reference section |
| Define expected receipt assertions | List what a future receipt may assert about artifact existence, backend identity, page/block evidence, quality disposition, and downstream-use status | reference section |
| Define expected receipt non-assertions | List forbidden claims: document truth, extraction accuracy, benchmark pass, runtime proof, provider proof, production readiness | reference section |
| Preserve held implementation lanes | Create held-lane table for schema, writer, runtime, RAG, provider, S3, Docker/package, checker | reference section |
| Keep worker no-commit | Leave worker return and reference uncommitted | worker return git status and no-commit statement |

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake summary | Operator asked for the next work order after MSEA-R12 roadmap readiness. |
| Scope classification | documentation/reference policy-definition worker dispatch |
| Risk sensitivity | R1 documentation policy; no runtime/provider/live/source import or implementation |
| Selected route mode | MULTI_AGENT_MULTI_ROLE |
| Intake role | Worker drafts policy only; operator supplies any future sample documents in a later tranche |
| Worker authority | READ accepted owner surfaces and source mirror index; WRITE only the named review and reference artifacts |
| Reviewer authority | Reviewer/closer may repair allowed-scope shape defects and commit material outputs if accepted |
| Operator checkpoint | Required before any actual sample document intake, corpus population, runtime execution, schema/writer implementation, or public/provider/live proof |

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
|---|---|
| Legacy coverage applicability | NOT_APPLICABLE_WITH_REASON: R12-T1 uses the pinned MinerU source mirror and accepted MSEA owner surfaces; it is not a legacy coverage sweep |
| Coverage action | none |
| Claim boundary | no legacy copied folder is promoted to source authority |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Storage layout change | NOT_APPLICABLE_WITH_REASON: documentation/reference-only policy tranche |
| Generated aggregate change | none authorized |
| Runtime storage change | none authorized |
| Claim boundary | no S3, RAG index, corpus storage, generated state, package, or runtime storage mutation |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher -> delegated worker -> reviewer/closer |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=c376ff33; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | Dispatch owns this baseline and work order only. Worker owns only the named worker return and policy reference. Reviewer/closer owns material commit and optional allowed-scope repair. |
| traceScope(phase, actor) | Dispatcher records dispatch AOT. Worker records worker-return AOT. Reviewer/closer records closure AOT if accepted. |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer owns material commit |
| crossBatchIsolation | R12-T1 must not edit session-sync, handoff, runtime, package, checker, public-sync, source mirror, generated aggregate, Web, MCP, model-router, or unrelated MSEA artifacts. |
| nextMoveSurfaces | Worker must not edit next-move surfaces. Reviewer/closer and session-sync steward update them only after accepted material closure. |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_COMPLETION_2026-07-03.md` optional; prefer repairing evidence in the worker return unless a separate completion review is needed |
| reviewerOwnedClosurePaths | worker return and policy reference, with optional completion review only if required by closure evidence |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| `docs/reviews/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_WORKER_RETURN_2026-07-03.md` | CREATE worker return with `COMPLETE_PENDING_REVIEW`, executionBaseHead, output-artifact checker read-ahead evidence, command evidence, git status, no-commit statement, and claim boundary |
| `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md` | CREATE policy reference defining sample slots, intake/provenance rules, expected receipt assertions, expected receipt non-assertions, held-lane reopen routing, and operator handoff requirements |

Forbidden worker changes:

- sample documents or corpus files;
- source mirror, external repo, legacy folder, package, runtime, checker,
  generated aggregate, public-sync, Web/MCP/model-router, session state,
  handoff, or active front-door files;
- schema implementation, receipt-writer code, adapter code, tests that imply
  runtime behavior, provider/live proof, S3 credentials, Docker build/run, RAG
  index write, package activation, or production-readiness evidence.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_WORKER_RETURN_2026-07-03.md`
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
epistemic process block or N/A line, machine-closure N/A line, git status, and
no-commit statement.

## Execution Plan

| Step | Worker action | Evidence |
|---|---|---|
| 1 | Capture executionBaseHead and git status before edits | worker return |
| 2 | Read startup surfaces, baseline, work order, source owner surfaces, and output-artifact checkers | worker return Checker Source Read-Ahead Block |
| 3 | Draft policy reference with required sections | reference artifact |
| 4 | Draft worker return with command evidence and no-commit statement | worker return |
| 5 | Run pre-implementation and worker-return gates; repair allowed-scope defects | command evidence |
| 6 | Return COMPLETE_PENDING_REVIEW without committing, staging, pushing, or session-sync editing | worker return and git status |

## Required Reference Sections

The policy reference must include these sections or equivalent clearer
headings:

| Required section | Content boundary |
|---|---|
| Scope / Applies To | policy only; no corpus population |
| Source Basis | accepted MSEA owner surfaces and source mirror index |
| Sample Corpus Slot Taxonomy | document-class slots and selection goals only |
| Sample Intake And Provenance Policy | operator-provided evidence requirements only |
| Expected Receipt Assertion Policy | allowed future receipt claims |
| Expected Receipt Non-Assertions | forbidden claims and overclaim prevention |
| Held-Lane Reopen Routing | concrete conditions for later schema, writer, runtime, RAG, provider, S3, Docker/package, checker lanes |
| Operator Handoff Requirements | checklist for later operator-provided sample tranche |
| External Knowledge Intake Routing | machine-shaped field/value table |
| External Absorption Core | machine-shaped field/value table and ledger_terminal markers |
| Corpus Completeness And Report Integrity | honest policy-scope verdict |
| External Absorption Value Conversion Matrix | required lanes including DOCTRINE_ADAPTED, RUNTIME_CANDIDATE, PACKAGE_CANDIDATE, CHECKER_CANDIDATE, REJECT_DIRECT_IMPORT, NO_PACKAGE_OR_RUNTIME_VALUE |
| Overlap And Novelty Classification | compare against R7/R8/R9/R10/R11/R12 owner surfaces |
| Source Mirror Migration Control | pinned source mirror and legacy-reference disposition |
| Rescan Intelligence Hardening | verdict and reason |
| Delta Execution Claim Boundary Control Block | reject execution/runtime/control claims |
| Public Export Disposition | DEFERRED_PRIVATE_ONLY |
| Agent Operation Trace Block | full trace label set |
| Claim Boundary | explicit no-runtime/no-corpus/no-production boundary |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | accepted MSEA owner surfaces plus pinned MinerU source mirror -> R11-T1 selected route -> R12 roadmap -> R12-T1 policy-definition work order |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py` |
| Owner surface | this work order |
| Disposition | ADAPT: dispatch a CVF-owned policy-definition tranche from accepted MinerU route evidence |
| Claim boundary | dispatch-only; no runtime/provider/live/S3/RAG/Docker/package/checker/source-import/schema/receipt-writer/adapter implementation/public-sync/production claim |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | `https://github.com/opendatalab/MinerU.git` at `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`; local mirror `.private_reference/source_mirrors/opendatalab__MinerU/`; accepted MSEA owner surfaces |
| Enumeration command | `rg --files --hidden --no-ignore .private_reference/source_mirrors/opendatalab__MinerU -g '!**/.git/**'` returned `425` during R12 roadmap authoring |
| Manifest artifact or inline manifest | `.private_reference/source_mirrors/INDEX.md` row `opendatalab__MinerU` |
| Processing ledger artifact or inline ledger | `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md` |
| Ledger terminal statuses | READ, SOURCE_VERIFIED, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, SKIPPED_WITH_REASON, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | MSEA-R7/R8/R9/R10/R11/R11-T1/R12 owner surfaces |
| Unresolved items | none for dispatch authoring; policy details are assigned to R12-T1 worker |
| Completion claim boundary | dispatch only; no runtime/provider/public/package/checker/source-import/schema/receipt-writer/adapter expansion |

ledger_terminal=READ for accepted MSEA owner surfaces; ledger_terminal=SOURCE_VERIFIED for source mirror commit/count; ledger_terminal=ADAPTED for R12-T1 policy-definition dispatch; ledger_terminal=DEFERRED for corpus population and implementation-facing lanes; ledger_terminal=REJECTED for direct upstream import; ledger_terminal=NO_NEW_VALUE for already-owned absorption facts.

## Corpus Completeness And Report Integrity

- Corpus task class: dispatch authoring for a policy-definition tranche.
- Corpus root: `.private_reference/source_mirrors/opendatalab__MinerU/` plus accepted MSEA owner surfaces.
- Snapshot time: 2026-07-03 dispatch authoring.
- Enumeration command: `rg --files --hidden --no-ignore .private_reference/source_mirrors/opendatalab__MinerU -g '!**/.git/**'`.
- Manifest artifact or inline manifest: `.private_reference/source_mirrors/INDEX.md` row `opendatalab__MinerU`.
- Manifest hash: source mirror commit `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`.
- Processing ledger artifact or inline ledger: this work order.
- Allowed terminal statuses: READ | SOURCE_VERIFIED | ADAPTED | DEFERRED | REJECTED | NO_NEW_VALUE | SKIPPED_WITH_REASON | BLOCKED_UNREADABLE.
- Reconciliation: manifest=source mirror index row plus accepted MSEA owner surfaces; ledger_terminal=READ/SOURCE_VERIFIED/ADAPTED/DEFERRED/REJECTED/NO_NEW_VALUE/SKIPPED_WITH_REASON/BLOCKED_UNREADABLE for cited artifacts; exclusions=sample document import/corpus population/runtime execution/source import/schema implementation/receipt-writer code/adapter implementation/production-readiness claims; unresolved=0 for dispatch scope.
- Unresolved files: none for dispatch authoring.
- Declared exclusions: sample document import, corpus population, full reabsorption, runtime execution, package activation, provider/live proof, source import, schema implementation, receipt-writer code, adapter implementation, production-readiness claims.
- Unreadable or unsupported files: none identified for dispatch authoring.
- Aggregation check: accepted MSEA owner surfaces are cited instead of regenerated into a new corpus aggregate.
- Drift check: R12 roadmap recomputed source mirror HEAD and file count.
- Output traceability: this work order routes only to the two named worker-owned artifacts.
- Adversarial verification: dispatch rejects actual corpus population, runtime execution, schema implementation, receipt-writer code, adapter implementation, document truth, extraction accuracy, and production readiness.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| MSEA-R11-T1 selected route | sample corpus and expected receipt policy should be first | DOCTRINE_ADAPTED | R12-T1 reference | define policy | no implementation |
| MSEA-R7 receipt vocabulary | artifact and field families need concrete policy grounding | DOCTRINE_ADAPTED | R12-T1 reference | define expected receipt assertions and non-assertions | no schema implementation |
| MSEA-R9/R10 runtime holds | implementation lanes need concrete reopen conditions | RUNTIME_CANDIDATE | R12-T1 held-lane routing | keep demand-gated | no runtime/provider/RAG/S3 action |
| MSEA-R8 Docker/package evidence | deployment/package candidates remain held | PACKAGE_CANDIDATE | R12-T1 held-lane routing | keep deployment/package work held | no Docker build/run or package activation |
| MSEA-T3/R6/R9/R10 checker notes | overclaim checker remains condition-gated | CHECKER_CANDIDATE | R12-T1 held-lane routing | defer checker work | no checker implementation |
| Direct upstream files | advisory input only | REJECT_DIRECT_IMPORT | source mirror control | reject direct import | no source import |
| Prior MSEA absorption facts | already-owned evidence | NO_PACKAGE_OR_RUNTIME_VALUE | predecessor owner surfaces | cite only | no runtime/package behavior |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| Sample-corpus and expected-receipt-policy route | `docs/roadmaps/CVF_MSEA_R12_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_ROADMAP_2026-07-03.md` | ENRICH_EXISTING | converts roadmap seed into executable worker dispatch | dispatch R12-T1 |
| Receipt vocabulary | `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` | CONFIRMED_EXISTING | R12-T1 uses vocabulary without implementing schema | cite |
| Runtime/provider/S3/Docker/RAG/package/checker holds | `docs/reference/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md`; `docs/reference/CVF_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_2026-07-02.md`; `docs/reference/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md` | CONFIRMED_EXISTING | no held lane is reopened by dispatch | defer |
| Direct upstream implementation | `.private_reference/source_mirrors/INDEX.md` | REJECT_DIRECT_IMPORT | direct import remains forbidden | reject |

## Source Mirror Migration Control

| Field | Disposition |
|---|---|
| Legacy source path | Legacy MinerU adapter folder remains secondary historical material only |
| Source mirror path | `.private_reference/source_mirrors/opendatalab__MinerU/` |
| Mirror index row | `.private_reference/source_mirrors/INDEX.md` row `opendatalab__MinerU` |
| Pinned upstream commit | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` |
| Migration disposition | MIGRATED_TO_SOURCE_MIRROR |
| Legacy cleanup disposition | LEGACY_REFERENCE_ONLY_WITH_REASON: historical comparison only; source facts prefer pinned mirror or governed MSEA artifacts |
| Claim boundary | source-mirror authority control only; no runtime, install, package activation, provider/live proof, public-sync, checker implementation, source import, schema implementation, receipt-writer code, adapter implementation, or production-readiness claim |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: this dispatch creates a policy-definition work order from an accepted
roadmap. It is not a rescan, intake-refresh, source-backed reassessment, or
residual repository absorption output.

## Evidence Requirements

| Evidence | Required shape |
|---|---|
| executionBaseHead | worker captures `git rev-parse --short HEAD` before edits |
| git status before/after | worker return includes actual `git status --short`, not a clean claim if output files are untracked |
| checker read-ahead | worker return lists output-artifact checker sources and literal tokens read before writing |
| source basis | policy reference cites R12/R11-T1/R10/R9/R8/R7 and source mirror index |
| gate evidence | worker return lists exact command results for pre-implementation and worker-return fast gate |
| no-commit evidence | worker return states HEAD unchanged and no commit/stage/push |

## Acceptance Criteria

| Criterion | Evidence |
|---|---|
| Policy reference exists and is bounded | named reference artifact with required sections |
| Worker return exists and is checker-shaped | named worker return artifact and worker-return fast gate PASS |
| No sample corpus claim | reference and worker return explicit non-claims |
| No implementation claim | reference and worker return claim boundaries |
| Held lanes preserved | reference held-lane table with concrete conditions |
| Worktree handoff is no-commit | git status shows only worker-owned artifacts pending |

## Fail Conditions

| Failure | Required result |
|---|---|
| Sample documents are imported or created | BLOCKED_WITH_REASON |
| Corpus population or corpus-existence claim appears | BLOCKED_WITH_REASON |
| Runtime/schema/writer/adapter/checker/package/provider/live/public implementation appears | BLOCKED_WITH_REASON |
| Worker output omits docType-specific checker read-ahead | repair before return |
| Worker commits, stages, pushes, or edits session-sync surfaces | BLOCKED_WITH_REASON |
| Source verification contradicts R12/R11/R10/R9/R8/R7 evidence | BLOCKED_WITH_REASON |

## Verification Commands

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base c376ff33 --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git status --short
```

Required dispatcher pre-dispatch command before commit:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base c376ff33 --head HEAD
```

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author |
| Provider or surface | local workspace |
| Session or invocation | MSEA-R12-T1 dispatch authoring, 2026-07-03 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, `rg`, source reads, dispatch scaffold helper, `apply_patch`, governance gates |
| Target paths | paired baseline; this work order |
| Allowed scope source | MSEA-R12 roadmap material commit `072c15f1`; session-sync commit `c376ff33` |
| Before status evidence | clean worktree; `git status --short` empty after MSEA-R12 roadmap session-sync |
| After status evidence | baseline and work order pending pre-dispatch gates |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | operator asked for next work order after R11-T1 selected route and R12 roadmap readiness |
| Claim boundary | dispatch only; no runtime/provider/live/public/package/checker/source-import/schema/receipt-writer/adapter/Web/MCP/model-router/action-authority claim |
| Agent type | dispatcher |
| Invocation ID | `msea-r12-t1-dispatch-2026-07-03` |
| Expected manifest | paired baseline; this work order |
| Actual changed set | paired baseline; this work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename; two new dispatch artifacts |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | MSEA-R12-T1 work-order dispatch |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, provider, parser, adapter, schema, receipt-writer, or production behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed |
| invocationBoundary | local governed dispatch authoring only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, Web runtime, adapter, package, watcher, daemon, parser, RAG index, or production route interception claim |
| claimLanguage | dispatch authorization for documentation/reference policy only |
| forbiddenExpansion | no sample document import, corpus population, MinerU runtime, install, model download, parser/OCR/VLM/hybrid/API/router/Gradio/Docker execution, provider/live call, credentials/S3, RAG write, source import, package activation, checker implementation, public-sync, Web/MCP/model-router/action-authority, automatic invocation, benchmark, document-truth, extraction-accuracy, schema implementation, receipt-writer code, adapter implementation, or production-readiness claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order. No public-sync export is authorized.

## Operator Checkpoint

Required after reviewer/closer acceptance if the next route would involve any
actual sample document intake, corpus population, runtime execution, schema or
writer implementation, adapter implementation, checker implementation,
provider/live proof, S3 credentials, Docker/package work, RAG write, public
sync, or production-readiness claim.

## Closure Checklist

| Item | Required closeout disposition |
|---|---|
| Worker return created | PASS or BLOCKED_WITH_REASON |
| Policy reference created | PASS or BLOCKED_WITH_REASON |
| Worker-return fast gate run | PASS or BLOCKED_WITH_REASON |
| Pre-implementation autorun run | PASS or BLOCKED_WITH_REASON |
| No forbidden paths changed | PASS or BLOCKED_WITH_REASON |
| No worker commit/stage/push | PASS or BLOCKED_WITH_REASON |
| Reviewer/closer material commit | reviewer/closer owned |
| Session-sync update | session-sync steward owned after accepted material commit |

## Claim Boundary

This work order authorizes only a WORKER_MUST_NOT_COMMIT documentation/reference
policy-definition worker tranche. It does not authorize or claim sample corpus
population, MinerU installation, parser execution, OCR/VLM/hybrid routing,
remote backend processing, model download, API/router/Gradio service, Docker
deployment, provider/live proof, S3 access, credential handling, RAG indexing,
source import, checker enforcement, package activation, schema implementation,
receipt-writer code, adapter implementation, public-sync export, document
truth, extraction accuracy, benchmark, certification, generated aggregate
mutation, production readiness, model-router behavior, action authority,
automatic invocation, or universal document intelligence.
