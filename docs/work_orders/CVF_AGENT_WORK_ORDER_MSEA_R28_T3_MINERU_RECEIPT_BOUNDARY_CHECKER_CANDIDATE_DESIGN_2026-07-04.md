# CVF Agent Work Order - MSEA-R28-T3 MinerU Receipt Boundary Checker Candidate Design

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: MSEA-R28-T3-CHECKER-CANDIDATE-DESIGN

rawMemoryReleased: false

Dispatch base head: 606043f5

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker role

Reviewer/closer: reviewer/closer

Worker return path: `docs/reviews/CVF_MSEA_R28_T3_MINERU_RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_WORKER_RETURN_2026-07-04.md`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA-R28-T3.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T3_MINERU_RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_2026-07-04.md`

Paired GC-018 baseline: `docs/baselines/CVF_GC018_MSEA_R28_T3_MINERU_RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_2026-07-04.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-04.

Do-not-misread notes: this packet authorizes only docs-only
checker-candidate design. It does not authorize checker implementation, hook
wiring, source/test edits, MinerU runtime, memory/RAG write, standalone app
work, private content read, generated output read, legal/use-case deep dive, or
production workflow-chain claims.

Required first actions: read startup front door, active state, active handoff,
guard orientation, literal gotchas, this work order, paired GC-018 baseline,
all source files in the Source Verification Block, and checker source for the
worker-created output artifacts before writing any artifact.

Return contract: create the worker return and companion design matrix, run
required gates, leave changes uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| Intake source | operator request to continue from accepted R28-T2 route selection while keeping MinerU work focused on the CVF foundation plane |
| Intake role | worker performs docs-only checker-candidate design for receipt-boundary protection |
| Reviewer role | reviewer/closer validates source evidence, held-lane boundaries, output shape, and no-commit discipline |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; docs-only design matrix plus worker return |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | worker return to reviewer/closer closure conversion |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if completion would require checker code, hook wiring, source/test edits, MinerU runtime, private content read, generated output read, memory/RAG write, provider/live proof, public-sync, standalone app work, legal/use-case deep dive, session-sync by worker, or forbidden path scope |

## Purpose

Perform the R28-T3 checker-candidate design tranche. The worker must produce a
source-verified design matrix for a future receipt-boundary checker by mapping
R26 candidate checks and R28-T1 receipt writer behavior into candidate check
families, inputs, failure dispositions, and non-goals.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | current request asks to continue by creating the next work order while preserving CVF foundation-plane focus | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` at HEAD `606043f5` routes next allowed move to R28-T3 GC-018/work-order authoring only | ACCEPT |
| R28-T2 closure | material commit `3e230445` selected `SELECT_RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_ONLY` and held memory-route release | ACCEPT |
| Paired GC-018 | `docs/baselines/CVF_GC018_MSEA_R28_T3_MINERU_RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_2026-07-04.md` | ACCEPT |

## Agent Roles

| Role | Responsibility | Commit authority |
| --- | --- | --- |
| Dispatcher | author paired GC-018 and this work order, then run pre-dispatch gates | may commit dispatch after gates pass |
| Worker | create allowed docs-only worker return and design matrix | WORKER_MUST_NOT_COMMIT |
| Reviewer/closer | review worker return, repair allowed defects, commit material closure if accepted | may commit closure |
| Session-sync steward | update front door, generated state, and active handoff when material closure exists | may commit session-sync only |

## Write Ownership

| Path group | Owner | Disposition |
| --- | --- | --- |
| paired GC-018 and this work order | dispatcher | dispatch material commit only |
| worker return and companion design matrix | worker creates, reviewer commits if accepted | WORKER_MUST_NOT_COMMIT |
| session state, front door, and active handoff | session-sync steward | only when material closure exists |
| source, tests, checkers, hook catalogs, runtime outputs, private documents, generated outputs, public-sync clone | none for R28-T3 worker | forbidden |

## Operator Checkpoint

No additional operator checkpoint is required for the bounded docs-only design
tranche if the worker stays inside allowed scope. Operator checkpoint is
required before checker implementation, hook wiring, runtime execution,
source/output content read, memory/RAG write, adapter work, protected
governance mutation, public-sync, provider/live proof, standalone app work,
legal/use-case deep dive, production workflow-chain claim, worker commit, or
push.

## Scope

Allowed scope:

- create worker return at the path named above;
- create companion design matrix at
  `docs/reference/CVF_MSEA_R28_T3_MINERU_RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_MATRIX_2026-07-04.md`;
- source-verify R28-T2 selected route, R28-T1 writer source/tests, R24/R26/R27
  owner surfaces, and current Extraction Foundation quality/chunk/storage
  owners;
- design candidate check families and evidence inputs for receipt-boundary
  validation, privacy/no-content-read protection, downstream-release hold,
  source-slot metadata, output filename-only evidence, and memory-route hold;
- state what a future implementation work order would need without dispatching
  it;
- run required governance gates.

Forbidden scope:

- no source or test edits;
- no checker implementation, hook wiring, or protected governance mutation;
- no MinerU command, model/cache mutation, ModelScope, VLM, OCR, parser,
  router, Gradio, Docker, WSL, or runtime smoke;
- no private source document body read and no generated output content read,
  quotation, copy, import, stage, or commit;
- no Candidate Group A source or output import into governed repo;
- no memory-layer write, RAG write, adapter implementation, S3, Web, MCP,
  model-router, package lifecycle, action-authority, public-sync,
  provider/live proof, standalone PDF app, legal/use-case deep dive,
  extraction-accuracy claim, document-truth claim, legal advice quality claim,
  current-law correctness claim, production workflow-chain claim, stage by
  worker, commit by worker, or push.

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
| checker source for worker return and companion reference docType/path family | READ_BEFORE_WRITING_OUTPUTS |

## Preflight Checks

| Check | Command or evidence | Required result |
| --- | --- | --- |
| Capture execution base | `git rev-parse --short HEAD` | record in worker return |
| Confirm worktree status | `git status --short --untracked-files=all` | record exact pending paths |
| Confirm planned paths | `Test-Path` for worker return and design matrix paths | no conflicting existing R28-T3 output paths |
| Read checker source | direct file reads of worker-return, reference-doc, quality, trace, delta, corpus/value, and rescan checkers | record exact headings/tokens in worker return before writing outputs |

## Execution Plan

| Step | Action | Evidence |
| --- | --- | --- |
| 1 | Re-read startup/state/handoff and capture executionBaseHead | worker return trace |
| 2 | Re-read checker source before writing worker return or design matrix | Checker Source Read-Ahead Block |
| 3 | Reconcile R28-T2 route evidence against R28-T1 writer source/tests and R24/R26/R27 owner surfaces | Source Verification Block in worker return |
| 4 | Build checker-candidate design matrix with candidate check family, source evidence, input fields, failure disposition, non-goal, and future implementation prerequisite | companion reference |
| 5 | State selected design disposition and keep implementation/memory/runtime lanes held | worker return Decision / Disposition |
| 6 | Run required verification commands and leave changes uncommitted | command evidence and git status |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T3 --title "MinerU Receipt Boundary Checker Candidate Design" --date 2026-07-04 --base 606043f5 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled source verification, design-only scope, worker output manifest, checker-output read-ahead mandate, handoff control, and R28 boundaries |
| checkerReadAheadConfirmation | dispatch-quality, handoff-boundary, lifecycle-hygiene, checker-read-ahead, operation-trace, delta-boundary, ADIF-disclosure, public-export, structural-completeness, and protected-guard-scope checker surfaces were read or compared before authoring |
| docOnlyNewFields | `RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_ONLY`; `CHECKER_IMPLEMENTATION_HELD_PENDING_ACCEPTED_DESIGN`; `MEMORY_ROUTE_HELD_PENDING_ACTUAL_CHECKER_AND_QUALITY` |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly by reading the
failing checker source and matching the literal required shape. Worker should
return to orchestrator only for a source contradiction, forbidden-scope need,
or missing authority that makes completion impossible.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order-authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class work-order-authoring --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | No ADIF-specific extra instruction is required beyond active guard orientation, literal-format gotchas, scaffold output, and worker-output checker read-ahead. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_core_guard_self_protection.py` |
| literalTokensReviewed | Status: DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Dispatch Prompt Envelope; Required First Reads; Preflight Checks; Execution Plan; Evidence Requirements; Acceptance Criteria; Review Gate; Closure Checklist; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Work-Order Fulfillment Manifest; Worker Return Packet Shape Contract; applicableCheckersRead; literalTokensReviewed; gateRunPurpose; Resolver query; Returned defects: NONE_RETURNED; Delta Execution Claim Boundary Control Block; Public Export Disposition; source-not-found disposition spelling |
| gateRunPurpose | Confirmation evidence after checker read-ahead; gates confirm dispatch shape and do not define implementation scope. |
| claimBoundary | This read-ahead covers this dispatch packet only; worker-created output artifacts require their own checker-source read-ahead before writing. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Current session state releases R28-T3 packet authoring after accepted R28-T2 route selection. | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `nextAllowedMove` field | `MSEA-R28-T3`; `SELECT_RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_ONLY` | active session bootstrap read model | ACCEPT |
| R28-T2 selected a bounded checker-candidate design route and held memory release pending checker plus quality/source-pointer prerequisites. | VALUE_SET | `docs/reviews/CVF_MSEA_R28_T2_MINERU_RECEIPT_BOUNDARY_CHECKER_AND_MEMORY_ROUTE_RELEASE_SELECTION_WORKER_RETURN_2026-07-04.md` | Decision / Disposition | `SELECT_RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_ONLY`; `HOLD_MEMORY_ROUTE_RELEASE_PENDING_RECEIPT_CHECKER_AND_QUALITY` | MSEA-R28-T2 worker return | ACCEPT |
| R28-T2 companion matrix marks receipt-boundary checker candidate design as selected and memory-route release as held. | VALUE_SET | `docs/reference/CVF_MSEA_R28_T2_MINERU_RECEIPT_BOUNDARY_CHECKER_AND_MEMORY_ROUTE_RELEASE_DECISION_MATRIX_2026-07-04.md` | Route Decision Matrix | `SELECT_RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_ONLY`; `HOLD_MEMORY_ROUTE_RELEASE_PENDING_RECEIPT_CHECKER_AND_QUALITY` | MSEA-R28-T2 decision matrix | ACCEPT |
| R26 records checker candidate status and criteria without authorizing checker implementation. | VALUE_SET | `docs/reference/CVF_MSEA_R26_T1_MINERU_RECEIPT_SCHEMA_WRITER_CONTRACT_AND_CHECKER_CANDIDATE_DESIGN_2026-07-04.md` | Checker Candidate Design | `checkerCandidateStatus`; `CHECKER_CANDIDATE`; `NOT_AUTHORIZED_BY_R26` | MSEA-R26 receipt contract | ACCEPT |
| R24-T4 defines private receipt envelope fields and private output class vocabulary that the design must protect. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md` | Receipt Envelope and Private Output Class Matrix | `outputContentRead`; `downstreamRelease`; `PRIVATE_INPUT_ONLY`; `PRIVATE_RUNTIME_COPY`; `PRIVATE_GENERATED_OUTPUT` | MSEA-R24-T4 private-output policy | ACCEPT |
| R28-T1 writer source exposes a held downstream-release constant and rejects output-content-read true. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 18, 66-76, 112-138, 160-178 | `DOWNSTREAM_RELEASE_HELD`; `MineruMetadataReceipt`; `build_mineru_metadata_receipt`; `render_mineru_metadata_receipt_json` | Extraction Foundation metadata receipt writer | ACCEPT |
| R28-T1 writer tests prove stable payload, held downstream release, and false output-content-read behavior. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` | lines 59, 63-64, 90-112 | `render_mineru_metadata_receipt_json`; `output_content_read`; `DOWNSTREAM_RELEASE_HELD` | Extraction Foundation metadata receipt writer tests | ACCEPT |
| R27 scan-to-memory route matrix requires receipt, quality, source pointer, allowed downstream use, and claim boundary before memory-safe candidate readiness. | VALUE_SET | `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md` | Scan-To-Memory Intake Route Matrix | `MEMORY_SAFE_CANDIDATE_READY`; `MEMORY_WRITE_AUTHORIZED`; `NOT_AUTHORIZED_BY_R27` | MSEA-R27 decision ledger | ACCEPT |
| Extraction Foundation pipeline owns quality, chunk, source-hash, and storage-boundary primitives for future memory-safe routing. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | lines 101-157 and 372-489 | `ExtractionQualityReport`; `ExtractionChunk`; `ExtractionStorageBoundary` | Extraction Foundation pipeline | ACCEPT |

## New Doc-Only Fields

| Field or token | Purpose | Source fact type | Worker rule |
| --- | --- | --- | --- |
| `RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_ONLY` | selected R28-T3 route token | DOC_ONLY_NEW | use for design readiness only, not checker code |
| `CHECKER_IMPLEMENTATION_HELD_PENDING_ACCEPTED_DESIGN` | downstream implementation hold token | DOC_ONLY_NEW | use if design is complete but implementation remains unauthorized |
| `MEMORY_ROUTE_HELD_PENDING_ACTUAL_CHECKER_AND_QUALITY` | memory route hold token for R28-T3 | DOC_ONLY_NEW | preserve R28-T2 memory hold until actual checker and quality/source-pointer prerequisites exist |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Planned artifact paths absent before authoring | `Test-Path` returned `False` for the planned GC-018, work order, worker return, and companion design matrix paths. | PASS |
| Token search for R28-T3 lane before authoring | `rg -n "MSEA-R28-T3\|R28_T3\|RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN\|CHECKER_CANDIDATE_DESIGN_ONLY" docs CVF_SESSION EXTENSIONS governance` returned only current session next-move references and no existing R28-T3 packet. | PASS |
| Collision decision | No existing R28-T3 dispatch or output artifact exists; this work order may create the first packet. | PASS |

## Roadmap-To-Work-Order Trace Matrix

| Predecessor route item | Source evidence | R28-T3 handling |
| --- | --- | --- |
| Receipt writer implementation | R28-T1 material commit `23177f27` and source/tests | accept as concrete receipt-shape evidence |
| Receipt checker candidate design | R28-T2 material commit `3e230445`; R26 checker candidate reference | design candidate matrix only |
| Memory-safe candidate contract | R27 sequence and R28-T2 held memory route | keep held until actual checker and quality/source-pointer prerequisites exist |
| Memory write adapter | R27 held lane | keep held |
| Runtime workflow and standalone app | R27/R28 held route and operator CVF-foundation instruction | keep held |

## Core Guard Self-Protection Authorization

| Field | Value |
| --- | --- |
| Authorized guard-maintenance scope | none |
| Protected paths | no `governance/compat/*.py`, hook catalog, autorun catalog, AGENTS.md, or session-state path is authorized for worker edits |
| Operator authorization | operator authorized next work-order creation for design-only checker-candidate packet, not checker implementation |
| Rollback boundary | if design evidence requires checker source changes, return BLOCKED_WITH_REASON instead of editing protected paths |
| Not authorized | no checker implementation, hook wiring, generated-state mutation, protected governance mutation, or session-sync by worker |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | MSEA source-mirror learning -> R27 plane route -> R28 writer and R28-T2 route selection -> R28-T3 checker-candidate design |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py` |
| Owner surface | paired GC-018 baseline and this work order |
| Disposition | ADAPT: convert accepted receipt and route evidence into a bounded checker-candidate design packet |
| Claim boundary | no source import, runtime execution, private output content read, memory/RAG write, public-sync, provider/live proof, checker implementation, or product-app claim |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| R28-T1 metadata writer | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py`; R28-T1 tests | CONFIRMED_EXISTING | concrete receipt shape and validation behavior | use as candidate-design input |
| R26 checker candidate criteria | R26 receipt contract reference | ENRICH_EXISTING | R28-T3 can organize criteria into a design matrix | design only |
| R28-T2 selected route | R28-T2 worker return and companion matrix | ENRICH_EXISTING | turns route decision into worker-dispatchable design work | dispatch design packet |
| Memory-safe candidate route | R27 decision ledger and Extraction Foundation quality owners | CONFIRMED_EXISTING | no new release evidence yet | keep held |
| Runtime, app, use-case, memory-write lanes | R27/R28 held surfaces and operator instruction | REJECT_DIRECT_IMPORT | useful later but outside current CVF-foundation step | keep held |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact: `docs/reviews/CVF_MSEA_R28_T2_MINERU_RECEIPT_BOUNDARY_CHECKER_AND_MEMORY_ROUTE_RELEASE_SELECTION_WORKER_RETURN_2026-07-04.md`

priorVerificationAnchor: R28-T2 selected checker-candidate design route and held memory-route evidence

freshRecomputeRequired: yes, worker must re-read the work order, GC-018,
current writer source/tests, and current R24/R26/R27/R28 owner surfaces before
writing outputs.

unicodePathHandling: ASCII-only artifact paths in this dispatch.

extractedTextAuthority: no private document text or generated output content is
authorized.

## Worker Output Checker Read-Ahead Mandate

Before writing each worker-owned output artifact, read checker source for that
file's docType, path family, and conditional content class.

| Output artifact | Required read-ahead result |
| --- | --- |
| worker return under `docs/reviews/` | derive exact review headings, worker-return quality terms, trace labels, delta boundary labels, corpus/value/rescan tokens, and no-commit evidence shape before writing |
| companion reference under `docs/reference/` | derive exact reference headings such as Scope / Applies To, Target / Source, source verification, corpus/value/rescan, trace, and claim-boundary labels before writing |

Literal-shape reminders: when listing required section names, write section
names without heading prefixes. Do not write never-created optional artifact
paths as parseable path tokens inside negative evidence rows. If a Findings row
exists, use a real defect-class enum token in the learning disposition.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher -> no-commit worker -> reviewer/closer -> session-sync steward |
| phase | pre-dispatch |
| baseHeadFor(phase) | dispatchBaseHead=606043f5; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | dispatcher owns this work order and paired GC-018; worker owns only worker return and companion design matrix; reviewer owns closure repairs and material commit; steward owns session-sync when closure exists |
| traceScope(phase, actor) | each actor records before status, after status, diff evidence, and no-commit or commit ownership evidence |
| commitOwner(phase) | dispatcher may commit dispatch; worker is WORKER_MUST_NOT_COMMIT; reviewer/closer may commit accepted worker outputs; session-sync steward may commit continuity updates only when material closure exists |
| crossBatchIsolation | R28-T3 must not edit source/tests, checker code, hook catalogs, R27/R26/R24 owner surfaces, runtime outputs, private source documents, generated output content, public-sync clone, protected governance code, or generated session state |
| nextMoveSurfaces | reviewer/closer and session-sync steward update next allowed move only when accepted R28-T3 closure exists |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R28_T3_MINERU_RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_COMPLETION_2026-07-04.md` |
| reviewerOwnedClosurePaths | worker return, companion design matrix, optional completion review, and allowed reviewer repairs inside those artifacts only |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/reviews/CVF_MSEA_R28_T3_MINERU_RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_WORKER_RETURN_2026-07-04.md` | create worker return with source verification, checker read-ahead, command evidence, no-commit statement, selected design disposition, and next allowed move recommendation |
| `docs/reference/CVF_MSEA_R28_T3_MINERU_RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_MATRIX_2026-07-04.md` | create companion reference with candidate check families, inputs, failure dispositions, non-goals, future implementation prerequisites, and claim boundary |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R28_T3_MINERU_RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_WORKER_RETURN_2026-07-04.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Shape-list rule: when listing required worker-output sections, write section
names without the heading prefix. Reserve actual heading syntax for real
sections so structural checkers do not treat checklist text as the artifact
section body.

## Foundation Storage Layout Block

| Field | Disposition |
| --- | --- |
| Storage layout change | N/A with reason: this work order creates one dated companion reference artifact in the existing reference root and does not create, split, relocate, or refactor a durable governance foundation folder. |
| New durable foundation directory | N/A with reason: no new directory is created. |
| Generated aggregate impact | N/A with reason: no generated aggregate is edited by the worker. |
| INDEX impact | N/A with reason: this is not an INDEX artifact or storage-layout tranche. |
| Guard owner | reviewer/closer verifies no durable storage layout mutation during closure. |

## Evidence Requirements

| Evidence | Required form |
| --- | --- |
| candidate check families | matrix rows with source evidence, target receipt field, failure disposition, and non-goal |
| source verification | ACCEPT rows against R28-T2, R28-T1 source/tests, R26, R27, R24, and Extraction Foundation owner surfaces |
| implementation hold | explicit `CHECKER_IMPLEMENTATION_HELD_PENDING_ACCEPTED_DESIGN` or stronger blocked disposition |
| memory-route hold | explicit `MEMORY_ROUTE_HELD_PENDING_ACTUAL_CHECKER_AND_QUALITY` or source-backed blocker |
| forbidden lanes | explicit held/rejected rows for runtime, app, legal/use-case, memory write, RAG write, and provider/live/public claims |
| output artifacts | exact git status and diff evidence |
| worker commit boundary | no-commit statement with HEAD unchanged evidence |

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| Design matrix | worker creates a concise checker-candidate design matrix, not code |
| Candidate checks | design covers receipt required fields, private-output vocabulary, output-content-read false boundary, filename-only output evidence, downstream release hold, source-slot privacy, and quality/source-pointer prerequisites |
| Memory route | no memory write or RAG release; prerequisites remain named |
| Output scope | only worker return and companion design matrix are created |
| Checker read-ahead | worker records checker source read-ahead before writing outputs |
| Gates | required pre-implementation and worker-return gates pass or return BLOCKED_WITH_REASON with exact blocker |
| Boundary | no runtime, private content, generated output, public-sync, provider/live, app, legal-quality, production, or checker-code claim |

## Review Gate

Reviewer/closer must verify:

- worker did not stage, commit, push, or mutate forbidden paths;
- design matrix is source-backed and does not implement or imply checker code;
- memory route remains held without an actual checker and quality/source-pointer
  proof;
- worker output artifacts satisfy review/reference docType heading needs;
- companion matrix is concise enough to support a future implementation
  decision without becoming a code spec;
- command evidence uses a real changed range, not base=head.

## Closure Checklist

| Item | Required disposition |
| --- | --- |
| Worker return created | checked, or BLOCKED with return action |
| Companion design matrix created | checked, or BLOCKED with return action |
| No forbidden implementation | checked, or BLOCKED with return action |
| Gates run | checked, or BLOCKED with exact command evidence |
| Next allowed move stated | checked after review decision |
| Session sync | reviewer/steward only when material closure exists |

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 606043f5 --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git status --short --untracked-files=all
```

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | Codex local workspace |
| Session or invocation | MSEA-R28-T3 MinerU Receipt Boundary Checker Candidate Design, 2026-07-04 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, scaffold helper, apply_patch, governance gates |
| Target paths | this work order and paired GC-018 baseline |
| Allowed scope source | active session state nextAllowedMove and operator request |
| Before status evidence | clean worktree evidence: `git status --short --untracked-files=all` returned no output before authoring |
| After status evidence | dispatcher pre-dispatch gates to be recorded before commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | operator requested next work-order creation |
| Claim boundary | dispatch authoring only; no worker execution, runtime, checker implementation, memory/RAG, public-sync, provider/live, or production claim |
| Agent type | dispatcher |
| Invocation ID | `msea-r28-t3-dispatch-2026-07-04` |
| Expected manifest | GC-018 baseline and work order |
| Actual changed set | to be confirmed by pre-dispatch gate |
| Manifest delta | to be confirmed by pre-dispatch gate |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R28-T3 docs-only dispatch authoring |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, or mandatory-wrapper behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: R28-T1 metadata receipt writer evidence is cited as predecessor only; no new runtime receipt is created by this dispatch. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed by this dispatch. |
| invocationBoundary | local file reads, searches, scaffold generation, and governance dispatch gates only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized. |
| claimLanguage | checker-candidate design dispatch only |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router behavior without fresh source-verified authorization. |

## Claim Boundary

This work order authorizes a no-commit worker to create a docs-only
checker-candidate design matrix and worker return. It does not authorize
checker code, hook wiring, MinerU runtime, private content read, generated
output read, memory/RAG write, adapter work, public-sync, provider/live proof,
standalone app work, legal/use-case deep dive, or production workflow-chain
claims.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R28-T3 is private provenance dispatch work and does not change the
public-sync repository or public catalog.
