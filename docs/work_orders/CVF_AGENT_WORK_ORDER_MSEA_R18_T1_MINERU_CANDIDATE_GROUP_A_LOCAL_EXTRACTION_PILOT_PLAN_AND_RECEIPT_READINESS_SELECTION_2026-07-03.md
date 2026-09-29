# CVF Agent Work Order - MSEA-R18-T1 MinerU Candidate Group A Local Extraction Pilot Plan And Receipt Readiness Selection

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: MSEA_R18_T1

Dispatch base head: 37bcd147

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: reviewer/closer

Worker return path: `docs/reviews/CVF_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_SELECTION_WORKER_RETURN_2026-07-03.md`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA_R18_T1.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_SELECTION_2026-07-03.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: worker must capture `git rev-parse --short HEAD` before edits.

Current-time notes: artifact date is 2026-07-03; use current repository state and source mirror, not stale chat memory.

Do-not-misread notes: this packet opens planning and route selection only; it does not authorize running MinerU, installing models, starting a local service, reading full document content, producing extraction outputs, public-sync, schema/writer/adapter/checker implementation, document-truth, extraction-accuracy, legal advice, current-law, production, or workflow-chain claims.

Required first actions: read startup files, guard orientation, literal gotchas, this work order, the paired GC-018 baseline, source references, and checker source listed in the Checker Source Read-Ahead Block before writing worker outputs.

Return contract: create the worker return and companion readiness matrix, run required gates, leave changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Create a source-verified local extraction pilot plan and receipt readiness
selection matrix for the two accepted Candidate Group A DOCX files. The worker
must decide whether the next governed move should open a future MSEA-R19 local
runtime pilot work order, open a receipt-schema work order first, or hold
runtime because environment/model/privacy prerequisites remain unresolved.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind source-intake --batch-id MSEA_R18_T1 --title "MinerU Candidate Group A Local Extraction Pilot Plan And Receipt Readiness Selection" --date 2026-07-03 --base 37bcd147 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | source-intake plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Completed placeholders, set DISPATCH_READY, source-verified MinerU CLI/backend/output facts, added evidence-reuse plan, output-shape mandate, route tokens, and runtime hold boundaries. |
| checkerReadAheadConfirmation | Read `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_source_intake_decision_packet_preflight.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`. |
| docOnlyNewFields | selectedRouteToken; pilotCommandEnvelope; quarantineOutputRoot; receiptReadinessMatrixPath; runtimePrerequisiteDisposition |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly by reading the
failing checker source and matching the literal required shape. Worker should
return to orchestrator only for a source contradiction, forbidden-scope need,
missing local file, missing source mirror, or missing authority that makes
completion impossible.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 10 |
| Returned defects | ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006 |
| Disclosed defectIds | ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0006 |
| Dispatch impact | Worker output checker read-ahead is mandatory; provider-local authority is excluded; runtime candidates are classified without execution; source verification symbol cells use real symbols or sections only. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_source_intake_decision_packet_preflight.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| literalTokensReviewed | Dispatch Prompt Envelope fields; Scaffold Provenance Block fields; Source Verification Block columns; Evidence Reuse And Encoding Plan fields; ADIF resolver query exactness; Agent Handoff Contract Control Block fields; Reviewer Closure Conversion fields; Worker Return Packet Shape Contract fields; Source-Intake Decision Packet Fields; Public Export Disposition token `DEFERRED_PRIVATE_ONLY`; Target / Source; Scope / Applies To; Rescan Intelligence Hardening; ledger terminal marker; `CHECKER_CANDIDATE`; `REMOVED_OR_REJECTED`; `RESOLVED_BY_DESIGN`; Delta block field labels; Agent Operation Trace labels. |
| gateRunPurpose | Confirmation evidence after checker source read-ahead, not first discovery; gates confirm this work order's dispatch shape and source-fidelity evidence. |
| claimBoundary | Read-ahead covers this work order and paired baseline only; worker output artifacts must perform their own checker-source read-ahead before writing. |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: R18-T1 must re-read current CVF-governed sources and pinned MinerU source mirror files before selecting a runtime route; Candidate Group A metadata may be recomputed without reading document body content.

unicodePathHandling: Use LiteralPath and UTF-8-safe command output for local paths; do not normalize or rewrite filenames.

extractedTextAuthority: N/A with reason

| Field | Value |
| --- | --- |
| verificationMode | RECOMPUTE_REQUIRED |
| priorVerificationArtifact | `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md` |
| priorVerificationAnchor | `## Current Path/Hash/Size Verification` |
| recomputeReason | R18-T1 must re-read current CVF-governed sources and pinned MinerU source mirror files before selecting a runtime route; Candidate Group A metadata may be recomputed without reading document body content |
| freshRecomputeRequired | true for path/hash/size metadata only; no document body read and no MinerU extraction |
| unicodePathHandling | Use `-LiteralPath` and UTF-8-safe command output for local paths; do not normalize or rewrite filenames |
| extractedTextAuthority | N/A with reason: R18-T1 must not read document body text or treat extracted text as authority |

## Operator Authorization And Privacy Boundary

Candidate Group A source documents are authorized for local private CVF testing
only. Original documents must not be public-synced or redistributed. Derived
outputs may be planned for governed internal receipts/evaluation, but this
tranche may not create extraction outputs; committed artifacts must use
metadata, redaction, or excerpt-minimal evidence unless the operator separately
approves fuller inclusion.

## Source Verification Block

| Claimed item | Claim type | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MinerU upstream authority is the pinned source mirror | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/INDEX.md` | row `opendatalab__MinerU` | `opendatalab__MinerU` | source mirror index | ACCEPT |
| Pinned MinerU mirror commit is recorded | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/INDEX.md` | row `opendatalab__MinerU` | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` | source mirror index | ACCEPT |
| Mirror boundary forbids install, model download, runtime/parser execution, provider/live proof, public-sync, and direct import | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/INDEX.md` | row `opendatalab__MinerU` | `opendatalab__MinerU` | source mirror index | ACCEPT |
| R17 accepted two Candidate Group A DOCX files for local private testing | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md` | `## Current Path/Hash/Size Verification`; `## Claim Boundary` | Candidate Group A | MSEA-R17-T1 intake ledger | ACCEPT |
| R17 marks artifact existence, page or block locator evidence, and content type classification as not producible without an authorized extraction pass | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md` | `## Receipt Dry-Run Readiness` | Receipt Dry-Run Readiness | MSEA-R17-T1 intake ledger | ACCEPT |
| R12 requires sample source identity, permission or license basis, privacy/redaction disposition, slot, format/size, and proof-use confirmation | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md` | `## Sample Intake And Provenance Policy`; `## Operator Handoff Requirements` | Sample Intake And Provenance Policy | MSEA-R12-T1 policy reference | ACCEPT |
| R12 receipt policy may assert artifact existence, page/block locator evidence, backend identity, quality disposition, and downstream-use status | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md` | `## Expected Receipt Assertion Policy` | Expected Receipt Assertion Policy | MSEA-R12-T1 policy reference | ACCEPT |
| R12 local parser runtime pilot row requires a concrete downstream use case and fresh GC-018 authorization | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md` | runtime pilot gating table | Local parser runtime pilot | MSEA-R12-T1 policy reference | ACCEPT |
| R10 keeps runtime/parser adapter held behind concrete downstream use case and fresh authorization | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md` | `## Held Lanes And Reopen Conditions` | Runtime/parser adapter | MSEA-R10 contract draft | ACCEPT |
| R7 owns receipt artifact-family and field-family vocabulary, not executable schema | VALUE_SET | VALUE_SET | `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` | `## Receipt Artifact Family Map`; `## Field Family Map`; `## Explicit Non-Claims` | Receipt Artifact Family Map | MSEA-R7 receipt schema contract draft | ACCEPT |
| MinerU CLI entry point is `mineru` | EXISTS | EXISTS | `.private_reference/source_mirrors/opendatalab__MinerU/pyproject.toml` | project scripts section | `mineru` | project scripts | ACCEPT |
| MinerU model-download, API, router, and Gradio scripts exist and remain forbidden here | EXISTS | EXISTS | `.private_reference/source_mirrors/opendatalab__MinerU/pyproject.toml` | project scripts section | `mineru-models-download` | project scripts | ACCEPT |
| MinerU README states DOCX is a supported input format | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/README.md` | overview and usage sections | `DOCX` | upstream README | ACCEPT |
| MinerU README shows the base CLI command envelope | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/README.md` | usage command section | `mineru -p <input_path> -o <output_path>` | upstream README | ACCEPT |
| MinerU README shows the pipeline backend command option | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/README.md` | usage command section | `-b pipeline` | upstream README | ACCEPT |
| MinerU README warns `mineru` can automatically start a local temporary service when no API URL is provided | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/README.md` | CLI architecture note | `mineru` | upstream README | ACCEPT |
| Pipeline backend constant exists | EXISTS | EXISTS | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/backend_options.py` | backend constants | `BACKEND_PIPELINE` | backend options module | ACCEPT |
| Default backend constant exists and must be considered because a safe pilot cannot rely on implicit defaults | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/backend_options.py` | backend constants | `DEFAULT_BACKEND` | backend options module | ACCEPT |
| HTTP-client backend choices exist and must remain out of scope | EXISTS | EXISTS | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/backend_options.py` | backend choices | `HTTP_CLIENT_BACKEND_CHOICES` | backend options module | ACCEPT |
| Allowed parse methods are auto, txt, and ocr | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/api_request.py` | parse method constant | `ALLOWED_PARSE_METHODS` | API request module | ACCEPT |
| API request module exposes server URL and client-side output generation surfaces requiring runtime planning | EXISTS | EXISTS | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/api_request.py` | request option definitions | `server_url` | API request module | ACCEPT |
| CLI output path function creates backend-specific output directories | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/output_paths.py` | output path function | `build_parse_dir` | output path module | ACCEPT |
| MinerU output docs say generated files depend on backend and input document type | VALUE_SET | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/reference/output_files.md` | output overview | output_files | upstream output documentation | ACCEPT |
| MinerU output docs define `middle.json`, `content_list.json`, and `content_list_v2.json` families | EXISTS | EXISTS | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/reference/output_files.md` | output file sections | `content_list_v2.json` | upstream output documentation | ACCEPT |

## New Doc-Only Fields

| Field | Meaning | Disposition |
| --- | --- | --- |
| selectedRouteToken | Worker-selected next-route token for reviewer/closer consideration | DOC_ONLY_NEW |
| pilotCommandEnvelope | Documentation-only later command envelope, not an executed command | DOC_ONLY_NEW |
| quarantineOutputRoot | Private output area proposal for a later runtime tranche | DOC_ONLY_NEW |
| receiptReadinessMatrixPath | Companion reference path produced by this worker | DOC_ONLY_NEW |
| runtimePrerequisiteDisposition | Worker classification of runtime prerequisites | DOC_ONLY_NEW |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Existing MSEA-R18 artifacts | `rg -n "MSEA_R18_T1|MSEA-R18-T1|LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_SELECTION|Local Extraction Pilot Plan And Receipt Readiness" docs CVF_SESSION CVF_SESSION_MEMORY.md` found only current next-move references before authoring | NO_PRIOR_ARTIFACT_COLLISION |
| Dispatch packet path check | No existing baseline or work order with these exact R18 names existed before this add operation | ABSENT_BEFORE_AUTHORING |
| Collision decision | MSEA-R18-T1 is a new child tranche after accepted MSEA-R17-T1 private corpus intake | SAFE_TO_CREATE |

## Authority Chain

- Operator instruction: proceed with the next source-verified MSEA-R18-T1 work order.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V34_2026-07-03.md`.
- Paired GC-018 baseline: `docs/baselines/CVF_GC018_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_SELECTION_2026-07-03.md`.
- Accepted private intake: `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md`.
- Sample and receipt policy: `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md`.
- MinerU source authority: `.private_reference/source_mirrors/opendatalab__MinerU/`.

Authority boundary: if any source contradicts this packet, stop and return
`BLOCKED_WITH_REASON`. The worker may not upgrade planning language into
runtime authority.

## Agent Roles

| Role | Owner | Responsibility |
| --- | --- | --- |
| Operator | operator | owns future runtime/full-content/public decisions |
| Dispatcher | dispatcher role | authors this GC-018/work order and runs pre-dispatch gates |
| Worker | delegated worker role | creates only the named worker return and companion readiness matrix, without commit |
| Reviewer/closer | reviewer/closer | reviews returned artifacts, repairs allowed-scope shape defects if needed, commits material if accepted |
| Session-sync steward | reviewer/closer after material acceptance | updates active session state only after accepted material closure |

## Pre-Flight Checks

Required before worker execution:

```powershell
git rev-parse --short HEAD
git status --short
Test-Path 'docs\reviews\CVF_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_SELECTION_WORKER_RETURN_2026-07-03.md'
Test-Path 'docs\reference\CVF_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_MATRIX_2026-07-03.md'
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

Expected result: clean worktree at execution start, planned worker outputs
absent before writing, and pre-implementation gate passing after worker output
authoring and allowed-scope repairs.

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| intakeRole | dispatcher-authored private pilot-planning work order |
| scope classification | bounded private planning and source-verification tranche; changed paths limited to the two worker outputs |
| workerRole | no-commit source verifier, readiness matrix author, and route selector |
| reviewerRole | reviewer/closer validates worker return and companion readiness matrix |
| operatorRole | owns any later runtime, fuller-content, public-sync, provider, or production decision |
| route mode | MULTI_AGENT_SINGLE_ROLE |
| routeDecision | proceed with Candidate Group A pilot planning; hold all runtime execution |
| escalationCondition | source contradiction, missing Candidate Group A metadata authority, need to execute MinerU, need to quote fuller content, or need to edit forbidden paths |
| claimBoundary | role routing only; no automatic execution, provider routing, public export, or production claim |

## Route Decision Menu

Worker must select exactly one `selectedRouteToken`:

| Token | Meaning |
| --- | --- |
| OPEN_MSEA_R19_LOCAL_EXTRACTION_PILOT_WORK_ORDER | A future local pilot work order can be authored, still requiring fresh runtime authorization before execution |
| OPEN_RECEIPT_SCHEMA_IMPLEMENTATION_WORK_ORDER_FIRST | Receipt schema/writer groundwork should precede any runtime pilot |
| HOLD_RUNTIME_PENDING_ENVIRONMENT_OR_MODEL_PLAN | Runtime cannot open until environment, model lifecycle, local service, and storage constraints are planned |
| HOLD_PENDING_OPERATOR_FULLER_CONTENT_APPROVAL | Fuller content or derived-output inclusion is needed before useful runtime planning can proceed |
| HOLD_ALL_IMPLEMENTATION_LANES | No source-backed next implementation lane is ready |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher authors packet; delegated worker executes under no-commit; reviewer/closer accepts or rejects |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=37bcd147; executionBaseHead=worker captures at start; closureBaseHead=reviewer/closer sets before material commit |
| changedSetScope(phase) | dispatch may add only this work order and paired GC-018 baseline; worker may add only the named worker return and companion readiness matrix |
| traceScope(phase, actor) | dispatcher trace in this work order; worker trace in worker return and companion reference; reviewer trace in commit/steward evidence |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer owns any material commit after review |
| crossBatchIsolation | clean worktree required before worker execution; worker must not touch session, handoff, runtime, public, source-mirror, package, or checker paths |
| nextMoveSurfaces | reviewer/closer updates active session state only after accepting material closure; worker must not edit session state |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_SELECTION_COMPLETION_2026-07-03.md` (optional; prefer reviewer repair inside the worker return unless a separate completion artifact is necessary) |
| reviewerOwnedClosurePaths | worker return and companion reference named in Work-Order Fulfillment Manifest; session-sync surfaces only after material acceptance |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Output Checker Read-Ahead Mandate

Before writing each worker-owned output artifact, read checker source for that
file's docType, path family, and conditional content class.

| Output artifact | Required read-ahead result |
| --- | --- |
| worker return under reviews | derive exact review headings, worker-return quality terms, trace labels, delta boundary labels, corpus/value/rescan tokens, no-commit evidence shape, and current `git status --short` finality before writing |
| companion reference under reference | derive exact reference headings such as Scope / Applies To, Target / Source, source verification, corpus/value routing, Rescan Intelligence Hardening, trace, Public Export Disposition, and claim-boundary labels before writing |

Literal-shape reminders: list section names without heading prefixes in any
checklist, avoid bare missing optional artifact path evidence rows, and do not
use broad dependency phrasing unless the row cites accepted artifact path and
commit evidence.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/reviews/CVF_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_SELECTION_WORKER_RETURN_2026-07-03.md` | create uncommitted worker return with `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`, command evidence, git status, no-commit statement, selected route token, and checker read-ahead evidence |
| `docs/reference/CVF_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_MATRIX_2026-07-03.md` | create uncommitted local extraction pilot plan and receipt readiness matrix; no runtime outputs |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_SELECTION_WORKER_RETURN_2026-07-03.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Shape-list rule: when listing required worker-output sections, write section
names without the heading prefix. Reserve actual heading syntax for real
sections so structural checkers do not treat this checklist as the artifact
section body.

## Source-Intake Decision Packet Fields

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | source-mirror absorption follow-on planning |
| Negative search performed | Yes - see Negative Search And Collision Discipline |
| Disposition | ADAPT |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| R17 private Candidate Group A intake | `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md` | CONFIRMED_EXISTING | path/hash/private boundary already owned | reuse and recompute metadata only |
| MinerU CLI/backend/output facts | `.private_reference/source_mirrors/INDEX.md`; `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md`; `docs/reference/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md`; `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md` | ENRICH_EXISTING | converts candidate facts into a pilot planning matrix | source-verify and classify |
| Pipeline local backend candidate | `.private_reference/source_mirrors/opendatalab__MinerU/README.md`; `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/backend_options.py` | ENRICH_EXISTING | safest candidate command envelope for a later local pilot, not executed here | park behind R19 decision |
| HTTP-client, VLM, hybrid, API/router/Gradio/Docker | `.private_reference/source_mirrors/INDEX.md`; `docs/reference/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md` | CONFIRMED_EXISTING | out of scope for private local planning unless a later work order authorizes | preserve hold |
| Receipt schema/writer implementation | `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md`; `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md`; `docs/reference/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md` | ENRICH_EXISTING | may become next work only if selected route says schema first | no implementation here |
| Direct source import or public export | `.private_reference/source_mirrors/INDEX.md`; `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md` | REJECT_DIRECT_IMPORT | private-only documents must not be copied or public-synced | forbid |

## KIOD Runtime-Candidate Parking Checks

| Candidate | Parking decision | Reason |
| --- | --- | --- |
| local pipeline parse | RUNTIME_CANDIDATE | future pilot candidate only; this packet does not authorize execution |
| model download | REMOVED_OR_REJECTED | model lifecycle and storage plan absent |
| local temporary service startup | RUNTIME_CANDIDATE | README shows service behavior; future pilot must decide diagnostic and shutdown plan |
| VLM or hybrid backend | REMOVED_OR_REJECTED | higher-risk runtime/model path without current need |
| HTTP-client backend or provider endpoint | REMOVED_OR_REJECTED | provider/live and server URL boundary not authorized |
| API/router/Gradio/Docker | REMOVED_OR_REJECTED | service/deployment surfaces are outside this private planning tranche |
| RAG/S3/writeback | REMOVED_OR_REJECTED | downstream-use and credential boundaries remain held |

## Scope

Allowed scope:

- Read accepted R17/R12/R10/R7 MSEA owner surfaces.
- Read the pinned MinerU source mirror files named in the Source Verification Block.
- Recompute Candidate Group A path/hash/size metadata if needed; do not read document body content.
- Produce the two worker-owned artifacts named in the manifest.
- Define a documentation-only pilot command envelope using placeholders, a private quarantine output root, expected output families, receipt readiness fields, failure classes, and route token.
- Run pre-implementation autorun and worker-return fast gate, repairing allowed-scope shape failures.

Forbidden scope:

- Do not run `mineru`, `mineru-api`, `mineru-router`, `mineru-gradio`, model-download, Docker, parser/OCR/VLM/hybrid/API, local service startup, provider calls, S3, or RAG.
- Do not install packages, mutate package lifecycle, edit source mirrors, import source files, or implement schema/writer/adapter/checker/runtime code.
- Do not copy, commit, public-sync, redistribute, or quote fuller content from original Candidate Group A documents.
- Do not use Candidate Group B or rejected derived outputs.
- Do not claim document truth, extraction accuracy, legal advice quality, current-law correctness, benchmark result, production readiness, action authority, or workflow-chain completion.
- Do not edit session state, active handoff, front door, or protected governance paths.

Risk ceiling: R1 private planning and route selection.

## Write Ownership

Owned files:

- `docs/reviews/CVF_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_SELECTION_WORKER_RETURN_2026-07-03.md`
- `docs/reference/CVF_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_MATRIX_2026-07-03.md`

Forbidden paths:

- original DOCX source documents;
- Candidate Group B files and rejected derived outputs;
- active session front door, generated session state surfaces, and active handoff files;
- `governance/compat/**`;
- `.private_reference/source_mirrors/**`;
- runtime, package, Web, MCP, schema, writer, adapter, checker, public-sync,
  and generated aggregate paths.

Write mode: create-only for the two owned worker output artifacts.

## Required First Reads

Before writing worker outputs, read:

- `CVF_SESSION_MEMORY.md`.
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- `AGENT_HANDOFF_V34_2026-07-03.md`.
- `docs/reference/guard_orientation/README.md`.
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`.
- this work order and paired GC-018 baseline.
- `.private_reference/source_mirrors/INDEX.md`.
- `.private_reference/source_mirrors/opendatalab__MinerU/pyproject.toml`.
- `.private_reference/source_mirrors/opendatalab__MinerU/README.md`.
- `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/reference/output_files.md`.
- `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/backend_options.py`.
- `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/output_paths.py`.
- `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/api_request.py`.
- `docs/reference/CVF_MSEA_R17_T1_MINERU_CANDIDATE_GROUP_A_PRIVATE_TEST_CORPUS_INTAKE_LEDGER_2026-07-03.md`.
- `docs/reference/CVF_MSEA_R12_T1_MINERU_SAMPLE_CORPUS_EXPECTED_RECEIPT_POLICY_2026-07-03.md`.
- `docs/reference/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md`.
- `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md`.
- applicable worker-output checker source listed in the Worker Output Checker Read-Ahead Mandate.

## Execution Plan

1. Capture `executionBaseHead` and `git status --short`.
2. Read checker source before writing worker outputs and create a checker-safe skeleton first.
3. Verify source mirror commit/count row, MinerU CLI entry points, backend constants, output path function, API request options, and output file documentation.
4. Recompute Candidate Group A path/hash/size metadata only if needed; record that no body content was read.
5. Build a future pilot command envelope that is documentation-only, prefers explicit `-b pipeline`, names a private quarantine output root, and flags local temporary service behavior as a future diagnostic requirement.
6. Map expected receipt fields to R12/R7 vocabulary and MinerU output families without implementing schema or writer code.
7. Select exactly one route token from the Route Decision Menu and justify it with source-backed evidence.
8. Run required gates; repair allowed-scope shape failures; return `COMPLETE_PENDING_REVIEW` if all required checks pass, otherwise `BLOCKED_WITH_REASON`.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap or predecessor requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| R17 accepted Candidate Group A private metadata intake | Source Verification Block; Evidence Reuse And Encoding Plan | receipt readiness matrix corpus rows | worker recomputes metadata or cites no drift | PASS |
| R12 defines expected receipt assertions and non-assertions | Execution Plan; Source Verification Block | receipt readiness matrix fields | worker maps each receipt field to R12/R7 | PASS |
| R10 holds runtime/parser adapter behind fresh authorization | KIOD Runtime-Candidate Parking Checks | selected route token | worker must not execute runtime | PASS |
| MinerU source mirror has CLI/backend/output facts | Source Verification Block | pilot command envelope | worker verifies source files | PASS |
| Operator wants use-case testing without over-absorbing the legal domain | Scope; Claim Boundary | explicit non-claims | reviewer checks no legal/product claim | PASS |

## Evidence Requirements

Worker must record:

- `git rev-parse --short HEAD` before edits.
- `git status --short` before edits and at handoff.
- `rg` or equivalent source-verification commands for required MinerU source facts.
- Candidate Group A metadata drift evidence if recomputed.
- `git diff --name-status`.
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD`.
- `python governance/compat/run_worker_return_fast_gate.py`.
- Explicit no-runtime/no-install/no-output/no-public/no-commit evidence.

## Verification Commands

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 37bcd147 --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git status --short
```

## Acceptance Criteria

- [ ] Worker creates exactly the two planned artifacts and leaves them uncommitted.
- [ ] Companion matrix includes a source-verified pilot command envelope but clearly marks it NOT_EXECUTED.
- [ ] Companion matrix selects exactly one route token from the Route Decision Menu.
- [ ] Companion matrix maps expected receipt fields to R12/R7 and MinerU output families without schema/writer implementation.
- [ ] Candidate Group A privacy boundary is preserved; no body content is read or quoted.
- [ ] Runtime/provider/S3/RAG/Docker/package/schema/writer/adapter/checker lanes remain held unless selected only as a future fresh-work-order route.
- [ ] Required worker gates pass or the worker returns `BLOCKED_WITH_REASON`.

Fail conditions:

- [ ] Worker runs MinerU, installs models/packages, starts services, or creates extraction outputs.
- [ ] Worker reads or quotes fuller document content.
- [ ] Worker creates artifacts outside the two owned worker outputs.
- [ ] Worker claims extraction accuracy, document truth, legal advice quality, current-law correctness, production readiness, or workflow-chain completion.
- [ ] Worker edits session state, source mirrors, runtime, package, or checker paths.

## Review Gate

Worker handoff is not closure. Reviewer/closer must review the returned
artifacts, may repair allowed-scope artifact-shape defects, and owns any
material commit plus later session-sync if accepted.

Reviewer validation command:

```powershell
python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return --base <closureBaseHead> --head HEAD --enforce
```

## Operator Checkpoint

Operator checkpoint satisfied for this dispatch: the operator asked to create
the fresh MSEA-R18-T1 GC-018/source-verified work order, and earlier authorized
Candidate Group A for local private CVF testing only. Further operator approval
is required for fuller content inclusion, public-sync, source document import,
runtime execution, model download, provider/live proof, RAG/S3, schema/writer/
adapter/checker implementation, or production/workflow-chain claims.

## Closure Checklist

- [ ] Worker creates exactly the two planned artifacts.
- [ ] Worker records actual `git status --short` at handoff.
- [ ] Worker records source verification for MinerU CLI/backend/output facts.
- [ ] Worker records route token and next-work-order recommendation.
- [ ] Worker return fast gate passes.
- [ ] Reviewer-return commit steward preflight passes before material commit.
- [ ] Committed-range pre-closure gate passes after accepted material commit.
- [ ] Session-sync surfaces are updated separately only if material closure changes next move.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | local workspace |
| Session or invocation | MSEA_R18_T1 MinerU Candidate Group A Local Extraction Pilot Plan And Receipt Readiness Selection, 2026-07-03 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, `rg`, scaffold helper, `apply_patch`, governance gates |
| Target paths | `docs/baselines/CVF_GC018_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_SELECTION_2026-07-03.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_SELECTION_2026-07-03.md` |
| Allowed scope source | operator request, accepted MSEA-R17-T1 private intake, pinned MinerU source mirror, and this paired GC-018 baseline |
| Before status evidence | clean worktree at dispatch start; `git rev-parse --short HEAD` returned `37bcd147` |
| After status evidence | dispatch packet pending pre-dispatch gate and material commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | dispatch authoring only for Candidate Group A local extraction pilot planning |
| Claim boundary | no runtime/provider/live/public/package/source-import/schema/writer/adapter/checker/Web/MCP/model-router/action-authority/legal-domain product claim |
| Agent type | dispatcher |
| Invocation ID | `msea-r18-t1-2026-07-03` |
| Expected manifest | `docs/baselines/CVF_GC018_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_SELECTION_2026-07-03.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_SELECTION_2026-07-03.md` |
| Actual changed set | `docs/baselines/CVF_GC018_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_SELECTION_2026-07-03.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R18_T1_MINERU_CANDIDATE_GROUP_A_LOCAL_EXTRACTION_PILOT_PLAN_AND_RECEIPT_READINESS_SELECTION_2026-07-03.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename is authorized |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | MSEA-R18-T1 Candidate Group A local extraction pilot plan and receipt readiness selection dispatch |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, provider, parser, adapter, schema, receipt-writer, corpus-processing, or production behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt exists; worker may create documentation-only readiness fields |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: dispatch authoring and planning only; worker must not execute MinerU |
| invocationBoundary | local governed documentation and source verification only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized |
| claimLanguage | private planning and route-selection dispatch only |
| forbiddenExpansion | no MinerU runtime, install, model download, parser/OCR/VLM/API/router/Gradio/Docker execution, local temporary service startup, provider/live call, S3/RAG, source document import, public-sync, schema/writer/adapter/checker implementation, benchmark, document-truth, extraction-accuracy, legal advice quality, current-law correctness, production readiness, Web/MCP/model-router behavior, action authority, or workflow-chain completion |

## Claim Boundary

This work order authorizes only a no-commit worker to create a private
planning matrix and route-selection worker return for a future local MinerU
extraction pilot. It does not authorize MinerU install/runtime/parser/OCR/VLM/
hybrid/API/router/Gradio/Docker execution, model download, local temporary
service startup, provider/live proof, RAG write, S3/credential handling,
schema implementation, receipt-writer code, adapter implementation, checker
implementation, source document copy/import, public-sync, benchmark,
document-truth, extraction-accuracy, legal advice quality, current-law
correctness, production readiness, model-router behavior, action authority, or
workflow-chain completion claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: Candidate Group A source documents and any future derived outputs are
authorized only for local private CVF testing. No public-sync export is
authorized.
