# CVF Agent Work Order - MSEA-R28-T2 MinerU Receipt Boundary Checker And Memory Route Release Selection

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: MSEA-R28-T2-ROUTE-SELECTION

rawMemoryReleased: false

Dispatch base head: 95734097

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker role

Reviewer/closer: reviewer/closer

Worker return path: `docs/reviews/CVF_MSEA_R28_T2_MINERU_RECEIPT_BOUNDARY_CHECKER_AND_MEMORY_ROUTE_RELEASE_SELECTION_WORKER_RETURN_2026-07-04.md`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA-R28-T2.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T2_MINERU_RECEIPT_BOUNDARY_CHECKER_AND_MEMORY_ROUTE_RELEASE_SELECTION_2026-07-04.md`

Paired GC-018 baseline: `docs/baselines/CVF_GC018_MSEA_R28_T2_MINERU_RECEIPT_BOUNDARY_CHECKER_AND_MEMORY_ROUTE_RELEASE_SELECTION_2026-07-04.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-04.

Do-not-misread notes: this packet authorizes only source-verified docs-only
route selection following the metadata receipt writer. It does not authorize
checker implementation, MinerU runtime, memory/RAG write, standalone app work,
private content read, generated output read, legal/use-case deep dive, or
production workflow-chain claims.

Required first actions: read startup front door, active state, active handoff,
guard orientation, literal gotchas, this work order, paired GC-018 baseline,
all source files in the Source Verification Block, and checker source for the
worker-created output artifacts before writing any artifact.

Return contract: create the worker return and companion decision matrix, run
required gates, leave changes uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| Intake source | operator request to audit and create the next move while keeping MinerU work focused on CVF foundation planes |
| Intake role | worker performs docs-only route selection for receipt-boundary checker design readiness and memory-route release prerequisites |
| Reviewer role | reviewer/closer validates source evidence, held-lane boundaries, output shape, and no-commit discipline |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; docs-only route decision and companion matrix |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | worker return to reviewer/closer closure conversion |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if completion would require checker code, hook wiring, source/test edits, MinerU runtime, private content read, generated output read, memory/RAG write, provider/live proof, public-sync, standalone app work, legal/use-case deep dive, session-sync by worker, or forbidden path scope |

## Purpose

Perform the post-writer R28-T2 audit and selection. The worker must decide,
from current source evidence, whether the next CVF-foundation move should be a
receipt-boundary checker-candidate design and whether memory-route release
remains held pending receipt checker and quality/source-pointer prerequisites.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | current request asks to audit and create the next work order while keeping CVF foundation ahead of use-case depth | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` at HEAD `95734097` routes next allowed move to R28-T2 route-selection and work-order authoring | ACCEPT |
| R28-T1 closure | material commit `23177f27` added the metadata receipt writer and left downstream release held | ACCEPT |
| Paired GC-018 | `docs/baselines/CVF_GC018_MSEA_R28_T2_MINERU_RECEIPT_BOUNDARY_CHECKER_AND_MEMORY_ROUTE_RELEASE_SELECTION_2026-07-04.md` | ACCEPT |

## Agent Roles

| Role | Responsibility | Commit authority |
| --- | --- | --- |
| Dispatcher | author paired GC-018 and this work order, then run pre-dispatch gates | may commit dispatch after gates pass |
| Worker | create allowed docs-only worker return and decision matrix | WORKER_MUST_NOT_COMMIT |
| Reviewer/closer | review worker return, repair allowed defects, commit material closure if accepted | may commit closure |
| Session-sync steward | update front door, generated state, and active handoff when material closure exists | may commit session-sync only |

## Write Ownership

| Path group | Owner | Disposition |
| --- | --- | --- |
| paired GC-018 and this work order | dispatcher | dispatch material commit only |
| worker return and companion decision matrix | worker creates, reviewer commits if accepted | WORKER_MUST_NOT_COMMIT |
| session state, front door, and active handoff | session-sync steward | only when material closure exists |
| source, tests, checkers, hook catalogs, runtime outputs, private documents, generated outputs, public-sync clone | none for R28-T2 worker | forbidden |

## Operator Checkpoint

No additional operator checkpoint is required for the bounded route-selection
audit if the worker stays inside allowed docs-only scope. Operator checkpoint
is required before checker implementation, runtime execution, source/output
content read, memory/RAG write, adapter work, protected governance mutation,
public-sync, provider/live proof, standalone app work, legal/use-case deep dive,
production workflow-chain claim, worker commit, or push.

## Scope

Allowed scope:

- create worker return at the path named above;
- create companion decision matrix at
  `docs/reference/CVF_MSEA_R28_T2_MINERU_RECEIPT_BOUNDARY_CHECKER_AND_MEMORY_ROUTE_RELEASE_DECISION_MATRIX_2026-07-04.md`;
- source-verify R28-T1 writer evidence, R24/R26/R27/R28 owner surfaces, and
  current Extraction Foundation quality/chunk/storage owners;
- classify receipt-boundary checker candidate design readiness and
  memory-route release prerequisites;
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
| Confirm planned paths | `Test-Path` for worker return and decision matrix paths | no conflicting existing R28-T2 output paths |
| Read checker source | direct file reads of worker-return, reference-doc, quality, trace, delta, corpus/value, and rescan checkers | record exact headings/tokens in worker return before writing outputs |

## Execution Plan

| Step | Action | Evidence |
| --- | --- | --- |
| 1 | Re-read startup/state/handoff and capture executionBaseHead | worker return trace |
| 2 | Re-read checker source before writing worker return or decision matrix | Checker Source Read-Ahead Block |
| 3 | Reconcile R28-T1 writer source/tests/return against R24/R26/R27/R28 owner surfaces | Source Verification Block in worker return |
| 4 | Build route decision matrix for checker-design, memory-safe candidate, memory write, runtime workflow, standalone app, and legal/use-case lanes | companion reference |
| 5 | Select one route token and state next allowed move without dispatching it | worker return Decision / Disposition |
| 6 | Run required verification commands and leave changes uncommitted | command evidence and git status |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T2 --title "MinerU Receipt Boundary Checker And Memory Route Release Selection" --date 2026-07-04 --base 95734097 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled source verification, route-selection scope, worker output manifest, checker-output read-ahead mandate, handoff control, and R28 boundaries |
| checkerReadAheadConfirmation | dispatch-quality, handoff-boundary, lifecycle-hygiene, checker-read-ahead, operation-trace, delta-boundary, ADIF-disclosure, public-export, structural-completeness, and protected-guard-scope checker surfaces were read or compared through the R28-T1 accepted packet pattern before authoring |
| docOnlyNewFields | `SELECT_RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_ONLY`; `HOLD_MEMORY_ROUTE_RELEASE_PENDING_RECEIPT_CHECKER_AND_QUALITY`; `HOLD_RUNTIME_AND_APP_LANES_FOR_CVF_FOUNDATION_ONLY` |
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
| Dispatch impact | No ADIF-specific extra instruction is required beyond active guard orientation, literal-format gotchas, and worker-output checker read-ahead. |

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
| Current session state releases R28-T2 route-selection with R28-T1 writer closure evidence. | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `nextAllowedMove` field | `MSEA-R28-T2` | active session bootstrap read model | ACCEPT |
| R28 selection names receipt boundary checker second and memory-safe candidate after receipt and checker. | VALUE_SET | `docs/reviews/CVF_MSEA_R28_FOUNDATION_IMPLEMENTATION_SEQUENCE_AUDIT_AND_SELECTION_2026-07-04.md` | R28 Selection Matrix | `RECEIPT_BOUNDARY_CHECKER`; `NEXT_AFTER_WRITER`; `NEXT_AFTER_RECEIPT_AND_CHECKER` | MSEA-R28 selection review | ACCEPT |
| R28-T1 writer return records downstream release as held pending receipt checker and memory route. | VALUE_SET | `docs/reviews/CVF_MSEA_R28_T1_MINERU_MINIMAL_METADATA_RECEIPT_WRITER_WORKER_RETURN_2026-07-04.md` | worker boundary and downstream release rows | `HELD_PENDING_RECEIPT_CHECKER_AND_MEMORY_ROUTE` | MSEA-R28-T1 worker return | ACCEPT |
| R27 implementation sequence treats receipt checker and memory-safe candidate as candidate next packets while holding memory write and runtime workflow. | VALUE_SET | `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md` | implementation sequence matrix | `Receipt checker implementation`; `Memory-safe candidate contract`; `Memory write adapter`; `MinerU runtime workflow` | MSEA-R27 decision ledger | ACCEPT |
| R26 records checker candidate status and criteria but does not authorize checker implementation. | VALUE_SET | `docs/reference/CVF_MSEA_R26_T1_MINERU_RECEIPT_SCHEMA_WRITER_CONTRACT_AND_CHECKER_CANDIDATE_DESIGN_2026-07-04.md` | Checker Candidate Design | `checkerCandidateStatus`; `CHECKER_CANDIDATE`; `NOT_AUTHORIZED_BY_R26` | MSEA-R26 receipt contract | ACCEPT |
| R24-T4 defines the receipt envelope and private output classes that any checker candidate must protect. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md` | Receipt Envelope and Private Output Class Matrix | `outputContentRead`; `downstreamRelease`; `PRIVATE_INPUT_ONLY`; `PRIVATE_RUNTIME_COPY`; `PRIVATE_GENERATED_OUTPUT` | MSEA-R24-T4 private-output policy | ACCEPT |
| R28-T1 writer source exposes a held downstream-release constant and rejects output-content-read true. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | constants and builder validation | `DOWNSTREAM_RELEASE_HELD`; `OUTPUT_CONTENT_READ_FORBIDDEN`; `build_mineru_metadata_receipt` | Extraction Foundation metadata receipt writer | ACCEPT |
| R28-T1 writer tests prove stable payload, held downstream release, and false output-content-read behavior. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` | writer tests | `render_mineru_metadata_receipt_json`; `output_content_read`; `DOWNSTREAM_RELEASE_HELD` | Extraction Foundation metadata receipt writer tests | ACCEPT |
| Extraction Foundation pipeline owns quality and chunk primitives, so memory-route release must account for quality and source pointers before any memory write. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | dataclasses and builders | `ExtractionQualityReport`; `ExtractionChunk`; `ExtractionStorageBoundary` | Extraction Foundation pipeline | ACCEPT |

## New Doc-Only Fields

| Field or token | Purpose | Source fact type | Worker rule |
| --- | --- | --- | --- |
| `SELECT_RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_ONLY` | possible selected route token | DOC_ONLY_NEW | may select only docs/design readiness, not checker code |
| `HOLD_MEMORY_ROUTE_RELEASE_PENDING_RECEIPT_CHECKER_AND_QUALITY` | possible memory-route hold token | DOC_ONLY_NEW | use when memory candidate/write release lacks checker and quality proof |
| `HOLD_RUNTIME_AND_APP_LANES_FOR_CVF_FOUNDATION_ONLY` | possible runtime/app boundary token | DOC_ONLY_NEW | use to preserve CVF-plane focus and prevent standalone app drift |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Planned artifact paths absent before authoring | `Test-Path` returned `False` for the planned GC-018, work order, worker return, and companion decision matrix paths. | PASS |
| Token search for R28-T2 lane before authoring | `rg -n "MSEA-R28-T2\|MINERU_RECEIPT_BOUNDARY_CHECKER_AND_MEMORY_ROUTE_RELEASE\|SELECT_RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_ONLY\|HOLD_MEMORY_ROUTE_RELEASE_PENDING_RECEIPT_CHECKER_AND_QUALITY" docs CVF_SESSION EXTENSIONS governance` returned only current session next-move references, not an existing R28-T2 packet. | PASS |
| Collision decision | No existing R28-T2 dispatch or output artifact exists; this work order may create the first packet. | PASS |

## Roadmap-To-Work-Order Trace Matrix

| Predecessor route item | Source evidence | R28-T2 handling |
| --- | --- | --- |
| Receipt writer implementation | R28-T1 material commit `23177f27` and worker return | accept as predecessor evidence |
| Receipt checker implementation | R27 future sequence and R28 selection | classify design readiness only |
| Memory-safe candidate contract | R27 sequence and R28 selection | classify release prerequisites and likely hold until checker and quality proof |
| Memory write adapter | R27 held lane | keep held unless source-backed release evidence exists |
| Runtime workflow and standalone app | R27/R28 held route and operator CVF-foundation instruction | keep held |

## Core Guard Self-Protection Authorization

| Field | Value |
| --- | --- |
| Authorized guard-maintenance scope | none |
| Protected paths | no `governance/compat/*.py`, hook catalog, autorun catalog, AGENTS.md, or session-state path is authorized for worker edits |
| Operator authorization | operator authorized route-selection work-order creation and CVF-foundation audit, not checker implementation |
| Rollback boundary | if route-selection evidence requires checker source changes, return BLOCKED_WITH_REASON instead of editing protected paths |
| Not authorized | no checker implementation, hook wiring, generated-state mutation, protected governance mutation, or session-sync by worker |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | source mirror and MSEA owner surfaces -> R27 plane route -> R28 writer closure -> R28-T2 route-selection |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py` |
| Owner surface | paired GC-018 baseline and this work order |
| Disposition | ADAPT: convert accepted receipt and route evidence into a bounded CVF-foundation decision packet |
| Claim boundary | no source import, runtime execution, private output content read, memory/RAG write, public-sync, provider/live proof, or product-app claim |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| R28-T1 metadata writer | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py`; R28-T1 worker return | CONFIRMED_EXISTING | concrete receipt shape is now available | use as predecessor evidence |
| Receipt checker candidate | R26 contract and R28 selection | ENRICH_EXISTING | route-selection can sharpen design readiness | classify, do not implement |
| Memory-safe candidate route | R27 decision ledger and Extraction Foundation quality owners | ENRICH_EXISTING | route-selection can state release prerequisites | classify and hold unless released |
| Runtime, app, use-case, memory-write lanes | R27/R28 held surfaces and operator instruction | REJECT_DIRECT_IMPORT | useful later but outside current CVF-foundation step | keep held |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact: `docs/reviews/CVF_MSEA_R28_T1_MINERU_MINIMAL_METADATA_RECEIPT_WRITER_WORKER_RETURN_2026-07-04.md`

priorVerificationAnchor: R28-T1 writer source and held downstream-release evidence

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
| companion reference under `docs/reference/` | derive exact reference headings, source verification, corpus/value/rescan, trace, and claim-boundary labels before writing |

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
| baseHeadFor(phase) | dispatchBaseHead=95734097; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | dispatcher owns this work order and paired GC-018; worker owns only worker return and companion decision matrix; reviewer owns closure repairs and material commit; steward owns session-sync when closure exists |
| traceScope(phase, actor) | each actor records before status, after status, diff evidence, and no-commit or commit ownership evidence |
| commitOwner(phase) | dispatcher may commit dispatch; worker is WORKER_MUST_NOT_COMMIT; reviewer/closer may commit accepted worker outputs; session-sync steward may commit continuity updates only when material closure exists |
| crossBatchIsolation | R28-T2 must not edit R28-T1 source/tests, R27/R26/R24 owner surfaces, runtime outputs, private source documents, generated output content, public-sync clone, protected governance code, or generated session state |
| nextMoveSurfaces | reviewer/closer and session-sync steward update next allowed move only when accepted R28-T2 closure exists |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R28_T2_MINERU_RECEIPT_BOUNDARY_CHECKER_AND_MEMORY_ROUTE_RELEASE_SELECTION_COMPLETION_2026-07-04.md` |
| reviewerOwnedClosurePaths | worker return, companion decision matrix, optional completion review, and allowed reviewer repairs inside those artifacts only |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/reviews/CVF_MSEA_R28_T2_MINERU_RECEIPT_BOUNDARY_CHECKER_AND_MEMORY_ROUTE_RELEASE_SELECTION_WORKER_RETURN_2026-07-04.md` | create worker return with selected route token, source verification, checker read-ahead, command evidence, no-commit statement, and next allowed move recommendation |
| `docs/reference/CVF_MSEA_R28_T2_MINERU_RECEIPT_BOUNDARY_CHECKER_AND_MEMORY_ROUTE_RELEASE_DECISION_MATRIX_2026-07-04.md` | create companion reference with route matrix, evidence rows, prerequisites, held-lane reasons, and claim boundary |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R28_T2_MINERU_RECEIPT_BOUNDARY_CHECKER_AND_MEMORY_ROUTE_RELEASE_SELECTION_WORKER_RETURN_2026-07-04.md`
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
| Storage layout change | N/A with reason: this work order creates one dated companion reference artifact in the existing `docs/reference/` root and does not create, split, relocate, or refactor a durable governance foundation folder. |
| New durable foundation directory | N/A with reason: no new directory is created. |
| Generated aggregate impact | N/A with reason: no generated aggregate is edited by the worker. |
| INDEX impact | N/A with reason: this is not an INDEX artifact or storage-layout tranche. |
| Guard owner | reviewer/closer verifies no durable storage layout mutation during closure. |

## Evidence Requirements

| Evidence | Required form |
| --- | --- |
| selected route | one explicit route token in worker return Decision / Disposition |
| memory-route release | source-backed release or hold token with prerequisites named |
| checker candidate | design-readiness classification only, unless worker returns blocked |
| forbidden lanes | explicit held/rejected rows for runtime, app, legal/use-case, memory write, RAG write, and provider/live/public claims |
| output artifacts | exact git status and diff evidence |
| worker commit boundary | no-commit statement with HEAD unchanged evidence |

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| Route decision | worker selects design-only checker route or a source-backed hold/block reason |
| Memory route | no memory write or RAG release unless source-backed prerequisites are proven |
| Output scope | only worker return and companion decision matrix are created |
| Checker read-ahead | worker records checker source read-ahead before writing outputs |
| Gates | required pre-implementation and worker-return gates pass or return BLOCKED_WITH_REASON with exact blocker |
| Boundary | no runtime, private content, generated output, public-sync, provider/live, app, legal-quality, production, or checker-code claim |

## Review Gate

Reviewer/closer must verify:

- worker did not stage, commit, push, or mutate forbidden paths;
- selected route is supported by source evidence and does not release memory or
  runtime by implication;
- worker output artifacts satisfy review/reference docType heading needs;
- companion matrix is useful for the next dispatch while staying concise;
- command evidence uses a real changed range, not base=head.

## Closure Checklist

| Item | Required disposition |
| --- | --- |
| Worker return created | checked, or BLOCKED with return action |
| Companion decision matrix created | checked, or BLOCKED with return action |
| No forbidden implementation | checked, or BLOCKED with return action |
| Gates run | checked, or BLOCKED with exact command evidence |
| Next allowed move stated | checked after review decision |
| Session sync | reviewer/steward only when material closure exists |

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 95734097 --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git status --short --untracked-files=all
```

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | Codex local workspace |
| Session or invocation | MSEA-R28-T2 MinerU Receipt Boundary Checker And Memory Route Release Selection, 2026-07-04 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, scaffold helper, apply_patch, governance gates |
| Target paths | this work order and paired GC-018 baseline |
| Allowed scope source | active session state nextAllowedMove and operator request |
| Before status evidence | clean worktree evidence: `git status --short --untracked-files=all` returned no output before authoring |
| After status evidence | dispatcher pre-dispatch gates to be recorded before commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | operator requested audit and next work-order creation |
| Claim boundary | dispatch authoring only; no worker execution, runtime, checker implementation, memory/RAG, public-sync, provider/live, or production claim |
| Agent type | dispatcher |
| Invocation ID | `msea-r28-t2-dispatch-2026-07-04` |
| Expected manifest | GC-018 baseline and work order |
| Actual changed set | to be confirmed by pre-dispatch gate |
| Manifest delta | to be confirmed by pre-dispatch gate |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R28-T2 docs-only dispatch authoring |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, or mandatory-wrapper behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: R28-T1 metadata receipt writer evidence only; no new runtime receipt is created by this dispatch. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed by this dispatch. |
| invocationBoundary | local file reads, searches, scaffold generation, and governance dispatch gates only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized. |
| claimLanguage | route-selection dispatch only |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router behavior without fresh source-verified authorization. |

## Claim Boundary

This work order authorizes a no-commit worker to create a docs-only route
selection and decision matrix. It does not authorize checker code, hook wiring,
MinerU runtime, private content read, generated output read, memory/RAG write,
adapter work, public-sync, provider/live proof, standalone app work,
legal/use-case deep dive, or production workflow-chain claims.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R28-T2 is private provenance dispatch work and does not change the
public-sync repository or public catalog.
