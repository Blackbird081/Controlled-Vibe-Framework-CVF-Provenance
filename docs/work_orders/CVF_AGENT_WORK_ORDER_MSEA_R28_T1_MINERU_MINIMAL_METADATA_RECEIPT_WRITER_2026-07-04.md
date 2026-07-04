# CVF Agent Work Order - MSEA-R28-T1 MinerU Minimal Metadata Receipt Writer

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: MSEA-R28-T1

rawMemoryReleased: false

Dispatch base head: 0892f634

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker role

Reviewer/closer: reviewer/closer

Worker return path: `docs/reviews/CVF_MSEA_R28_T1_MINERU_MINIMAL_METADATA_RECEIPT_WRITER_WORKER_RETURN_2026-07-04.md`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA-R28-T1.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T1_MINERU_MINIMAL_METADATA_RECEIPT_WRITER_2026-07-04.md`

Paired GC-018 baseline: `docs/baselines/CVF_GC018_MSEA_R28_T1_MINERU_MINIMAL_METADATA_RECEIPT_WRITER_2026-07-04.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-04.

Do-not-misread notes: this packet authorizes only a deterministic
metadata-only receipt writer helper plus focused tests and worker return. It
does not authorize MinerU execution, PDF parsing, output-content reading,
checker implementation, memory/RAG write, adapter work, product app work, or
legal/use-case deep dive.

Required first actions: read startup front door, active state, active handoff,
guard orientation, literal gotchas, this work order, paired GC-018 baseline,
and checker source for the worker-created output artifacts before writing any
artifact.

Return contract: create the worker return artifact, implement allowed source
and tests only, run required gates, leave changes uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Implement the first R28 foundation step: a deterministic local MinerU
metadata-only receipt writer in Extraction Foundation. The output must be a
safe receipt object or stable payload built from caller-supplied metadata, not
from document bodies or generated output content.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | current request asks Codex to complete according to the selected roadmap | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` at HEAD `0892f634` routes next move to R28-T1 GC-018/work-order authoring | ACCEPT |
| R28 selection | `docs/reviews/CVF_MSEA_R28_FOUNDATION_IMPLEMENTATION_SEQUENCE_AUDIT_AND_SELECTION_2026-07-04.md` at material commit `e2bb6b61` selected writer first | ACCEPT |
| Paired GC-018 | `docs/baselines/CVF_GC018_MSEA_R28_T1_MINERU_MINIMAL_METADATA_RECEIPT_WRITER_2026-07-04.md` | ACCEPT |

## Agent Roles

| Role | Responsibility | Commit authority |
| --- | --- | --- |
| Dispatcher | author paired GC-018 and this work order, then run pre-dispatch gates | may commit dispatch after gates pass |
| Worker | implement allowed source/test/worker-return paths only | WORKER_MUST_NOT_COMMIT |
| Reviewer/closer | review worker return, repair allowed defects, commit material closure if accepted | may commit closure |
| Session-sync steward | update front door, generated state, and active handoff when material closure exists | may commit session-sync only |

## Write Ownership

| Path group | Owner | Disposition |
| --- | --- | --- |
| paired GC-018 and this work order | dispatcher | dispatch material commit only |
| allowed source/test/worker-return paths | worker creates, reviewer commits if accepted | WORKER_MUST_NOT_COMMIT |
| session state, front door, and active handoff | session-sync steward | only when material closure exists |
| all other paths | none for R28-T1 | forbidden |

## Operator Checkpoint

No additional operator checkpoint is required for the bounded metadata-only
writer if the worker stays inside allowed scope. Operator checkpoint is required
before any runtime run, source/output content read, memory/RAG write, adapter,
checker, public-sync, provider/live proof, product app, legal/use-case deep
dive, production claim, worker commit, or push.

## Scope

Allowed scope:

- add `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py`;
- add `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py`;
- add worker return at the path named above;
- run focused Python tests and governance gates.

Forbidden scope:

- no MinerU command, model/cache mutation, ModelScope, VLM, OCR, parser,
  router, Gradio, Docker, WSL, or runtime smoke;
- no private source document body read and no generated output content read,
  quotation, copy, import, stage, or commit;
- no Candidate Group A source or output import into governed repo;
- no checker implementation, hook wiring, memory-layer write, RAG write,
  adapter implementation, S3, Web, MCP, model-router, package lifecycle,
  action-authority, public-sync, provider/live proof, standalone PDF app,
  legal/use-case deep dive, extraction-accuracy claim, document-truth claim,
  legal advice quality claim, current-law correctness claim, production
  workflow-chain claim, stage by worker, commit by worker, or push.

## Required First Reads

| Source | Required action |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V35_2026-07-03.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |
| this work order and paired GC-018 | READ |
| all source files in the Source Verification Block | SOURCE_VERIFIED |
| checker source for worker return and changed source/test artifacts | READ |

## Preflight Checks

| Check | Command or evidence | Required result |
| --- | --- | --- |
| Capture execution base | `git rev-parse --short HEAD` | record in worker return |
| Confirm worktree status | `git status --short --untracked-files=all` | record exact pending paths |
| Confirm planned paths | `Test-Path` for source, test, and worker return paths | no conflicting existing R28-T1 writer paths unless reviewer created them |
| Read checker source | direct file reads of worker-return and governance checkers | record exact headings/tokens in worker return |

## Execution Plan

| Step | Action | Evidence |
| --- | --- | --- |
| 1 | Re-read source authority and capture executionBaseHead | worker return trace |
| 2 | Implement a small frozen/dataclass or equivalent receipt model and writer/render helper | source diff |
| 3 | Validate required fields, safe output filename families, privacy class, false output-content flag, and held downstream release | focused tests |
| 4 | Reject unsafe values without reading files or content | focused tests |
| 5 | Create worker return with output-artifact checker read-ahead and exact git status | worker return |
| 6 | Run required verification commands | command evidence in worker return |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T1 --title "MinerU Minimal Metadata Receipt Writer" --date 2026-07-04 --base 0892f634 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled authority chain, source verification, no-commit handoff control, worker output manifest, narrow implementation instructions, and R28 boundaries |
| checkerReadAheadConfirmation | dispatch-quality, handoff-boundary, lifecycle-hygiene, checker-read-ahead, operation-trace, delta-boundary, ADIF-disclosure, public-export, and structural-completeness checker sources were read before authoring |
| docOnlyNewFields | none; implementation symbols are worker-owned additions |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly by reading the
failing checker source and matching the literal required shape. Worker should
return to orchestrator only for a source contradiction, forbidden-scope need, or
missing authority that makes completion impossible.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order-authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class work-order-authoring --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | No ADIF-specific extra instruction is required beyond active guard orientation and literal-format gotchas. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | Status: DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Dispatch Prompt Envelope; Required First Reads; Preflight Checks; Execution Plan; Evidence Requirements; Acceptance Criteria; Review Gate; Closure Checklist; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Work-Order Fulfillment Manifest; Worker Return Packet Shape Contract; applicableCheckersRead; literalTokensReviewed; gateRunPurpose; Resolver query; Returned defects: NONE_RETURNED; Delta Execution Claim Boundary Control Block; Public Export Disposition; source-not-found disposition spelling |
| gateRunPurpose | Confirmation evidence after checker read-ahead; gates confirm dispatch shape and do not define implementation scope. |
| claimBoundary | This read-ahead covers this dispatch packet only; worker-created output artifacts require their own checker-source read-ahead before writing. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R28 selected minimal metadata receipt writer first and did not authorize implementation until fresh dispatch exists. | VALUE_SET | `docs/reviews/CVF_MSEA_R28_FOUNDATION_IMPLEMENTATION_SEQUENCE_AUDIT_AND_SELECTION_2026-07-04.md` | Decision / Disposition and R28 Selection Matrix | `SELECT_MINIMAL_METADATA_RECEIPT_WRITER_FIRST`; `AUTHOR_MSEA_R28_T1_GC018_AND_SOURCE_VERIFIED_WORK_ORDER_FOR_METADATA_RECEIPT_WRITER` | MSEA-R28 selection review | ACCEPT |
| R27 route sequence says receipt writer is a candidate next packet; checker, memory, runtime, and app lanes are held or later. | VALUE_SET | `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md` | implementation sequence matrix | `Receipt writer implementation`; `Receipt checker implementation`; `Memory-safe candidate contract`; `MinerU runtime workflow` | MSEA-R27 decision ledger | ACCEPT |
| R26 defines the required metadata receipt fields and writer rules. | VALUE_SET | `docs/reference/CVF_MSEA_R26_T1_MINERU_RECEIPT_SCHEMA_WRITER_CONTRACT_AND_CHECKER_CANDIDATE_DESIGN_2026-07-04.md` | Receipt Schema Draft and Writer Contract Draft | `receiptId`; `sourceInputSlot`; `inputSha256`; `outputFileNames`; `outputContentRead`; `downstreamRelease` | MSEA-R26 receipt contract | ACCEPT |
| R24-T4 defines private output classes and committed metadata-only evidence rules. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md` | Receipt Envelope and Private Output Class Matrix | `PRIVATE_INPUT_ONLY`; `PRIVATE_RUNTIME_COPY`; `PRIVATE_GENERATED_OUTPUT`; `RECEIPT_METADATA_ALLOWED`; `EXCERPT_MINIMAL_SEPARATE_AUTHORITY` | MSEA-R24-T4 private-output policy | ACCEPT |
| MinerU source mirror documents output filename families allowed only as metadata names in this tranche. | VALUE_SET | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/reference/output_files.md` | output file sections and summary list | `layout.pdf`; `span.pdf`; `model.json`; `middle.json`; `content_list.json`; `content_list_v2.json`; `*.md` | MinerU source mirror output docs | ACCEPT |
| Extraction Foundation scan route source is deterministic and already uses supplied signals rather than runtime file reads. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | module contract and `decide_scan_route` | `decide_scan_route`; `DocumentScanSignals`; `ScanRouteDecision` | Extraction Foundation scan route | ACCEPT |
| Extraction Foundation metadata evidence source rejects raw-content evidence pointers. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/metadata_evidence.py` | validation and failure token definitions | `MetadataEvidenceRecord`; `evaluate_metadata_evidence`; `RAW_CONTENT_FORBIDDEN` | Extraction Foundation metadata evidence | ACCEPT |
| Extraction Foundation scan outcome report source renders bounded metadata reports without extracted chunks or OCR text. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | module contract and render helpers | `ScanOutcomeReport`; `build_scan_outcome_report`; `render_scan_outcome_report_json` | Extraction Foundation scan outcome report | ACCEPT |
| Extraction Foundation pipeline source owns quality, chunk, and storage-boundary primitives; R28-T1 must not mutate these unless necessary for import exposure. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | dataclasses and storage-boundary builder | `ExtractionQualityReport`; `ExtractionChunk`; `ExtractionStorageBoundary`; `build_extraction_storage_boundary` | Extraction Foundation pipeline | ACCEPT |

## New Implementation Symbols To Create

| Symbol or file | Purpose | Source fact type | Worker rule |
| --- | --- | --- | --- |
| `mineru_metadata_receipt_writer.py` | deterministic metadata receipt writer helper | NEW_SOURCE_AUTHORIZED_BY_THIS_WORK_ORDER | keep local and metadata-only |
| `MineruMetadataReceipt` or equivalent | receipt data model | NEW_SOURCE_AUTHORIZED_BY_THIS_WORK_ORDER | must include required R24/R26 fields |
| writer/render helper | stable payload builder | NEW_SOURCE_AUTHORIZED_BY_THIS_WORK_ORDER | must not read files or content |
| focused test file | boundary proof | NEW_SOURCE_AUTHORIZED_BY_THIS_WORK_ORDER | must cover privacy, required fields, safe output names, held downstream release |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Planned artifact paths absent before authoring | `Test-Path` returned `False` for planned GC-018, work order, and worker return paths. | PASS |
| Token search for R28-T1 writer lane before authoring | `rg -n "MSEA-R28-T1\|MINERU_MINIMAL_METADATA_RECEIPT_WRITER\|Minimal Metadata Receipt Writer\|mineru_metadata_receipt_writer" docs CVF_SESSION EXTENSIONS\CVF_EXTRACTION_FOUNDATION` returned only existing R28 next-move continuity references, not an existing dispatch or implementation. | PASS |
| Collision decision | No existing R28-T1 writer implementation or dispatch exists; worker may create the allowed new source/test/return paths. | PASS |

## Roadmap-To-Work-Order Trace Matrix

| Predecessor route item | Source evidence | Work-order instruction |
| --- | --- | --- |
| Minimal metadata receipt writer | R28 selected first | implement now |
| Receipt checker | R28 second lane | do not implement |
| Memory-safe candidate and memory write | R27/R28 held sequence | do not implement |
| MinerU runtime workflow | R27/R28 held sequence | do not run or implement |
| App/legal use case | R27/R28 held or rejected route | do not deepen |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | Extraction Foundation metadata receipt helper | local deterministic helper only; no file read, runtime command, memory write, or action authority | this work order and paired GC-018 source verification | internal-only helper; no external adapter | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | none in R28-T1 | no external ingress, auth, approval, mutation, raw-data release, or public claim | forbidden scope in this work order | deferred adapter owner requires future GC-018 | DEFERRED_WITH_REASON |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | accepted MinerU source mirror plus MSEA owner surfaces -> R27 plane route -> R28 selection -> R28-T1 metadata writer dispatch |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py` |
| Owner surface | this work order |
| Disposition | ADAPT: authorize a bounded local writer using accepted filename-family and receipt-policy evidence |
| Claim boundary | no source import, runtime execution, private output content read, memory/RAG write, public-sync, provider/live proof, or product-app claim |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| Receipt field doctrine | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md`; `docs/reference/CVF_MSEA_R26_T1_MINERU_RECEIPT_SCHEMA_WRITER_CONTRACT_AND_CHECKER_CANDIDATE_DESIGN_2026-07-04.md` | CONFIRMED_EXISTING | worker will implement local payload shape | implement narrowly |
| MinerU output family names | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/reference/output_files.md`; `docs/reference/CVF_MSEA_R26_T1_MINERU_RECEIPT_SCHEMA_WRITER_CONTRACT_AND_CHECKER_CANDIDATE_DESIGN_2026-07-04.md` | ENRICH_EXISTING | worker will validate names as metadata only | implement validation |
| Extraction Foundation deterministic style | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py`; `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_scan_outcome_report.py` | ENRICH_EXISTING | worker adds adjacent helper and tests | implement |
| Checker/memory/RAG/runtime/app lanes | `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md`; `docs/reviews/CVF_MSEA_R28_FOUNDATION_IMPLEMENTATION_SEQUENCE_AUDIT_AND_SELECTION_2026-07-04.md` | REJECT_DIRECT_IMPORT | not released by this packet | defer |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact: `docs/reviews/CVF_MSEA_R28_FOUNDATION_IMPLEMENTATION_SEQUENCE_AUDIT_AND_SELECTION_2026-07-04.md`

priorVerificationAnchor: R28 selected route plus R24/R26/R27 owner surfaces

freshRecomputeRequired: yes, worker must re-read all cited current files before implementation

unicodePathHandling: use literal UTF-8 paths and PowerShell-safe commands; do not normalize or rewrite source-mirror paths

extractedTextAuthority: no extracted document text authority exists in R28-T1; document text and generated output content remain forbidden

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | dispatcher authors packet; worker executes without commit; reviewer/closer owns material commit and session-sync |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=0892f634; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | dispatch changes are limited to paired GC-018 baseline and this work order; worker changes are limited to allowed source/test/worker-return paths |
| traceScope(phase, actor) | dispatcher trace in this work order; worker trace in worker return; reviewer trace in closure evidence if accepted |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | no unrelated MSEA, runtime, checker, memory, RAG, public-sync, app, or session-sync paths in worker batch |
| nextMoveSurfaces | session-sync steward updates front door, state, and handoff only when reviewer material commit exists |

## Intake Role Routing Decision

- Intake summary: operator request is bounded CVF foundation-plane work for
  a metadata-only receipt writer.
- Scope classification: bounded allowed scope with low blast radius and no
  runtime execution.
- Risk sensitivity: no public-sync, provider, live, secret, legal, production,
  memory write, RAG write, or readiness claim.
- Selected role route: routeMode=SINGLE_AGENT_MULTI_ROLE.
- Role separation basis: dispatcher, worker, reviewer/closer, and session-sync
  steward duties remain separately recorded; independent external review is
  not claimed.
- Escalation condition: stop for operator checkpoint or external reviewer if
  scope, risk, public, provider/live, runtime, memory/RAG, checker, adapter, or
  product-app work changes.

| Field | Value |
| --- | --- |
| routeDecision | INTERNAL_WORKER_IMPLEMENTATION |
| workerRole | delegated worker |
| reviewerRole | reviewer/closer |
| intakeBoundary | this is not external source-intake execution; source-mirror facts are already accepted and cited as metadata authority only |
| commitMode | WORKER_MUST_NOT_COMMIT |
| returnCondition | worker returns `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |

## Single-Agent Multi-Role Control Block

- Role separation ledger: Dispatcher, Worker, Reviewer/Closer, and
  Session-sync steward duties are recorded separately.
- Evidence basis: review uses git diff, source paths, focused test output,
  worker return, and gate results, not memory-only claims.
- Self-review boundary: independent review is not claimed; reviewer/closer
  acceptance is bounded to changed files and gate evidence.
- Escalation conditions: stop and ask operator or external reviewer if
  scope/risk/public/provider/live/runtime/checker/memory/RAG/app work changes.
- Gate sequence: pre-dispatch before dispatch commit; pre-implementation and
  worker-return fast gate before worker handoff; reviewer-fast and commit
  steward before material closure; session-state checks before session-sync.

| Field | Value |
| --- | --- |
| selectedRoute | SINGLE_AGENT_MULTI_ROLE |
| dispatchRole | dispatcher owns GC-018/work-order authoring only |
| workerRole | worker owns allowed implementation artifacts but must not commit |
| reviewerRole | reviewer/closer owns acceptance and material commit |
| roleSwitchBoundary | no role may skip worker-return review or commit unreviewed worker output |
| sessionSyncBoundary | session-sync starts only when material closure exists |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R28_T1_MINERU_MINIMAL_METADATA_RECEIPT_WRITER_COMPLETION_2026-07-04.md` |
| reviewerOwnedClosurePaths | worker return plus allowed source/test files; session-sync paths are session-sync steward owned after material commit |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Output Checker Read-Ahead Mandate

Before writing each worker-owned output artifact, read checker source for that
file's docType, path family, and conditional content class.

| Output artifact | Required read-ahead result |
| --- | --- |
| worker return under reviews directory | derive exact review headings, worker-return quality terms, trace labels, delta boundary labels, corpus/value/rescan tokens, and no-commit evidence shape before writing |
| source and test files | derive source/test expectations from existing Extraction Foundation tests and Python test runner |

Literal-shape reminders: list required worker-output section names without the
heading prefix; write source-not-found disposition spelling instead of the
exact blocked enum in literalTokensReviewed; avoid stale dependency wording
unless accepted release evidence is cited.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | create deterministic local metadata-only receipt writer |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` | create focused tests for required fields, privacy defaults, safe filename names, stable rendering, and held downstream release |
| `docs/reviews/CVF_MSEA_R28_T1_MINERU_MINIMAL_METADATA_RECEIPT_WRITER_WORKER_RETURN_2026-07-04.md` | create full worker return with checker read-ahead, command evidence, git status, and `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R28_T1_MINERU_MINIMAL_METADATA_RECEIPT_WRITER_WORKER_RETURN_2026-07-04.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Shape-list rule: when listing required worker-output sections, write section
names without the heading prefix. Reserve actual heading syntax for real
sections so structural checkers do not treat this checklist as the artifact
section body.

## Evidence Requirements

| Evidence | Required form |
| --- | --- |
| executionBaseHead | short HEAD captured before worker edits |
| changed set | `git diff --name-status` and `git status --short --untracked-files=all` |
| focused tests | command output for the new test file |
| governance gates | pre-implementation autorun and worker-return fast gate output |
| privacy proof | test assertions and worker-return claim boundary |
| forbidden-scope proof | worker return records no runtime, source/output content read, memory/RAG, public, provider/live, app, or legal-use-case work |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| storageDecision | create one adjacent Extraction Foundation source file and one adjacent test file |
| targetFolder | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/`; `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/` |
| indexDisposition | N/A_WITH_REASON: this tranche does not create a new docs/reference foundation family or stable index folder |
| splitRelocationDisposition | N/A_WITH_REASON: no existing foundation file is split, relocated, or refactored |
| claimBoundary | layout note only; no runtime, checker, memory/RAG, public-sync, provider/live, app, or production claim |

## Verification Commands

```powershell
python -m pytest EXTENSIONS\CVF_EXTRACTION_FOUNDATION\tests\test_mineru_metadata_receipt_writer.py
python governance\compat\run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance\compat\run_worker_return_fast_gate.py
git diff --name-status
git status --short --untracked-files=all
```

## Acceptance Criteria

| Criterion | Required outcome |
| --- | --- |
| Minimal writer implemented | source helper exists and tests pass |
| Metadata-only boundary | writer never reads document files or generated output content |
| Required receipt fields | R24/R26 field set is present or intentionally represented with equivalent names that tests cover |
| Output content flag | R28-T1 receipts keep `outputContentRead` false |
| Output filename safety | unsafe paths, directories, or content-like names are rejected; allowed family names are accepted as metadata |
| Downstream hold | receipt does not release checker, memory, RAG, runtime, adapter, app, legal, public, or production lanes |
| Worker mode | worker leaves all changes uncommitted and records exact status |

## Review Gate

Reviewer must verify the worker return, source/test diff, focused tests, and
governance gates before committing. Reviewer may repair allowed-scope defects
inside the source, test, or worker return. Any runtime, checker, memory/RAG,
adapter, app, public-sync, provider/live, or use-case expansion must return to
orchestrator for a fresh packet.

## Closure Checklist

| Item | Required closeout disposition |
| --- | --- |
| Worker did not commit | PASS required |
| Allowed paths only | PASS required |
| Tests and gates | PASS or BLOCKED_WITH_REASON |
| Worker return accepted | reviewer decision required |
| Material commit | reviewer/closer owned only |
| Session sync | separate steward-owned update when material closure commit exists |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex dispatcher |
| Provider or surface | local PowerShell plus governed markdown authoring |
| Session or invocation | MSEA-R28-T1 MinerU minimal metadata receipt writer dispatch, 2026-07-04 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | startup reads; source reads; scaffold helper; ADIF resolver; negative search; apply_patch; governance gates |
| Target paths | paired GC-018 baseline and this work order |
| Allowed scope source | MSEA-R28 selected `SELECT_MINIMAL_METADATA_RECEIPT_WRITER_FIRST` and active next allowed move permits fresh R28-T1 GC-018/work-order authoring |
| Before status evidence | HEAD `0892f634`; clean worktree before dispatch authoring |
| After status evidence | dispatch artifacts pending pre-dispatch gates |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | dispatch authoring only |
| Claim boundary | no worker execution, runtime, private output read, memory/RAG write, public-sync, provider/live proof, app, legal-use-case deep dive, production claim, or push |
| Agent type | dispatcher |
| Invocation ID | `msea-r28-t1-mineru-minimal-metadata-receipt-writer-dispatch-2026-07-04` |
| Expected manifest | paired GC-018 baseline and this work order |
| Actual changed set | paired GC-018 baseline and this work order pending final gate confirmation |
| Manifest delta | MATCH pending final git status confirmation |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | MSEA-R28-T1 dispatch for a deterministic metadata-only receipt writer |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, provider, public, memory, RAG, or production behavior is claimed by this dispatch |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt or writer output is created by the dispatch packet |
| actionEvidence | ACTION_EVIDENCE_PRESENT: dispatcher created governed dispatch artifacts only |
| invocationBoundary | governed markdown dispatch authoring |
| interceptionBoundary | no direct interception, wrapper/proxy enforcement, runtime gate, provider call, memory store, RAG index, or agent coding control is authorized |
| claimLanguage | dispatch ready for worker execution under WORKER_MUST_NOT_COMMIT; implementation result is not claimed here |
| forbiddenExpansion | no MinerU runtime, checker, adapter, memory/RAG, public-sync, provider/live, app, legal/use-case, Web, MCP, model-router, package lifecycle, action-authority, production, stage by worker, commit by worker, or push |

## Claim Boundary

This work order authorizes only worker execution for the bounded
MSEA-R28-T1 metadata-only receipt writer helper, focused tests, and worker
return. It does not itself implement or claim the writer result, and it does
not authorize runtime extraction, private content inspection, generated output
content read, checker implementation, memory ingestion, RAG write, adapter
implementation, public-sync, provider/live proof, standalone app work,
legal-quality analysis, extraction accuracy, document truth, current-law
correctness, workflow-chain production readiness, action authority, worker
commit, or push.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R28-T1 uses private provenance planning and source-mirror evidence. No
public-sync export is authorized.
