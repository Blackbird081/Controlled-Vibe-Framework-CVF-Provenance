# CVF Agent Work Order - MSEA-R28-T4 MinerU Receipt Boundary Checker Implementation And Hook Wiring Decision

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Date: 2026-07-04

docType: work_order

Batch ID: MSEA-R28-T4-RECEIPT-BOUNDARY-CHECKER-IMPLEMENTATION-DECISION

rawMemoryReleased: false

dispatchBaseHead: 55961ef2

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker role

Reviewer/closer: reviewer/closer

Worker return path: `docs/reviews/CVF_MSEA_R28_T4_MINERU_RECEIPT_BOUNDARY_CHECKER_IMPLEMENTATION_AND_HOOK_WIRING_DECISION_WORKER_RETURN_2026-07-04.md`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA-R28-T4.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T4_MINERU_RECEIPT_BOUNDARY_CHECKER_IMPLEMENTATION_AND_HOOK_WIRING_DECISION_2026-07-04.md`

Paired GC-018 baseline: `docs/baselines/CVF_GC018_MSEA_R28_T4_MINERU_RECEIPT_BOUNDARY_CHECKER_IMPLEMENTATION_AND_HOOK_WIRING_DECISION_2026-07-04.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-04. R28-T3 closure at material
commit `4d64e33f` accepted the checker-candidate design and released only fresh
R28-T4 packet authoring.

Do-not-misread notes: this packet authorizes only a bounded local governance
checker implementation, focused tests, allowed hook/autorun catalog wiring,
registry coverage if required, and a worker return. It does not authorize
MinerU runtime execution, private/generated content read, Candidate Group A
import, memory/RAG write, provider/live proof, public-sync, standalone app
work, legal/use-case deep dive, extraction accuracy, document truth, legal
quality, current-law correctness, workflow-chain release claim, worker
stage, worker commit, or push.

Required first actions: read startup front door, bootstrap read model, active
session state, active handoff V36, guard orientation index, literal-format
gotchas, this work order, paired GC-018 baseline, all source files in the Source
Verification Block, and checker source for worker-created outputs before
editing any file.

Return contract: create or modify only the allowed worker-owned paths, run
focused tests and required gates, leave changes uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| Intake source | operator request to continue from accepted R28-T3 checker-candidate design into fresh R28-T4 checker implementation and hook wiring decision packet authoring |
| Intake role | worker implements local deterministic receipt-boundary checker, focused tests, and bounded hook/autorun catalog wiring |
| Reviewer role | reviewer/closer validates source evidence, protected-path authorization, focused tests, hook wiring, worker return, and no-commit discipline |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; implementation remains pending review until reviewer closure |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | worker return to reviewer/closer closure conversion |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if completion would require MinerU runtime execution, private/generated content read, memory/RAG write, provider/live proof, public-sync, standalone app work, legal/use-case deep dive, session-sync by worker, AGENTS.md edit, active handoff edit, source/test edits outside owned paths, dependency install, destructive command, worker stage, worker commit, push, or claim-boundary expansion |

## Purpose

Implement the R28-T4 receipt-boundary checker tranche. The worker must create a
deterministic local checker that validates committed MinerU metadata receipt
artifacts against the R28-T3 accepted design matrix, prove it with focused
tests, and wire it into source-visible autorun/local hook catalog surfaces if
the checker passes.

## Agent Roles

| Role | Responsibility | Commit authority |
| --- | --- | --- |
| Dispatcher | author paired GC-018 and this work order, then run pre-dispatch gates | may commit dispatch after gates pass |
| Worker | implement checker, tests, bounded catalog wiring, optional required registry entries, and worker return | WORKER_MUST_NOT_COMMIT |
| Reviewer/closer | review worker return, repair allowed defects, commit material closure if accepted | may commit closure |
| Session-sync steward | update front door, generated state, and active handoff when material closure exists | may commit session-sync only |

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | current request authorizes fresh R28-T4 GC-018/source-verified work order authoring for checker implementation and hook wiring decision | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` and `CVF_SESSION/ACTIVE_SESSION_STATE.json` route next allowed move to R28-T4 packet authoring only | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V36_2026-07-04.md` names the same next allowed move and parked checkpoints | ACCEPT |
| R28-T3 closure | material commit `4d64e33f` accepted checker-candidate design and held memory route | ACCEPT |
| Paired GC-018 | `docs/baselines/CVF_GC018_MSEA_R28_T4_MINERU_RECEIPT_BOUNDARY_CHECKER_IMPLEMENTATION_AND_HOOK_WIRING_DECISION_2026-07-04.md` | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- create `governance/compat/check_mineru_receipt_boundary.py`;
- create `governance/compat/test_check_mineru_receipt_boundary.py`;
- modify `governance/compat/agent_autorun_command_catalog.py` only to add the new checker to the appropriate common/range gate bundle if focused tests pass;
- modify `governance/compat/local_governance_hook_catalog_pre_commit.py` only to add the new checker to pre-commit if focused tests pass;
- modify `governance/compat/local_governance_hook_catalog_pre_push.py` only to add the new checker to pre-push if focused tests pass;
- add GC-051 registry source entries and regenerate `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` only if changed review/source evidence requires coverage;
- create the worker return path named above;
- run focused checker tests, worker-return fast gate, and pre-implementation autorun;
- record exact `executionBaseHead`, changed files, command evidence, and no-commit statement.

Forbidden scope:

- no edits to R28-T1 writer source/tests, R28-T3 worker return or companion matrix, R24/R26/R27 references, active session state, active handoff, root startup files, AGENTS.md, public-sync clone, product runtime, Web/UI, MCP/CLI adapter, memory/RAG owner, Candidate Group A source/generated output, private source documents, or generated MinerU output content;
- no MinerU command, model/cache mutation, ModelScope, VLM, OCR, parser, router, Gradio, Docker, WSL, or runtime smoke;
- no private source document body read and no generated output content read, quotation, copy, import, stage, or commit;
- no memory-layer write, RAG write, adapter implementation, S3, Web, MCP, model-router, package lifecycle, action-authority, public-sync, provider/live proof, standalone PDF app, legal/use-case deep dive, extraction-accuracy claim, document-truth claim, legal advice quality claim, current-law correctness claim, production workflow-chain claim, worker stage, worker commit, or push.

Risk ceiling: R2 governance checker/catalog implementation; no runtime/provider/private-data action.

## Write Ownership

| Path group | Owner | Disposition |
| --- | --- | --- |
| paired GC-018 and this work order | dispatcher | dispatch material commit only |
| `governance/compat/check_mineru_receipt_boundary.py` | worker creates | allowed |
| `governance/compat/test_check_mineru_receipt_boundary.py` | worker creates | allowed |
| `governance/compat/agent_autorun_command_catalog.py` | worker modifies only to add checker command | allowed if focused tests pass |
| `governance/compat/local_governance_hook_catalog_pre_commit.py` | worker modifies only to add checker command | allowed if focused tests pass |
| `governance/compat/local_governance_hook_catalog_pre_push.py` | worker modifies only to add checker command | allowed if focused tests pass |
| `docs/corpus-intelligence/registry/entries/msea-r28-t4-mineru-receipt-boundary-checker-source.json` and matching tests entry | worker creates only if GC-051 requires coverage | conditional allowed |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | worker regenerates only from source entries | conditional allowed |
| worker return | worker creates, reviewer commits if accepted | WORKER_MUST_NOT_COMMIT |
| session state, front door, and active handoff | session-sync steward | forbidden to worker |
| any other path | not worker-owned | forbidden unless a revised work order authorizes it |

## Required First Reads

| Source | Required action |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V36_2026-07-04.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |
| this work order and paired GC-018 | READ |
| all source files in the Source Verification Block | SOURCE_VERIFIED |
| checker source for worker return, new checker source, focused tests, and conditional registry output | READ_BEFORE_WRITING_OUTPUTS |

## Preflight Checks

| Check | Command or evidence | Required result |
| --- | --- | --- |
| Capture execution base | `git rev-parse --short HEAD` | record in worker return |
| Confirm worktree status | `git status --short --untracked-files=all` | record exact pending paths |
| Confirm planned paths | `Test-Path` for checker source, focused test, and worker return paths | no conflicting existing R28-T4 implementation paths |
| Read checker/output source | direct file reads of applicable output, trace, delta, corpus, worker-return, and hook/catalog checkers | record exact headings/tokens in worker return before writing outputs |

## Execution Plan

| Step | Action | Evidence |
| --- | --- | --- |
| 1 | Re-read startup/state/handoff, capture executionBaseHead, and confirm clean or declared worktree state | worker return trace |
| 2 | Read checker source for worker return, protected-path authorization, corpus registry, hook/catalog wiring, and dispatch boundaries | Checker Source Read-Ahead Block |
| 3 | Implement a deterministic checker for committed MinerU metadata receipt artifact text/JSON without opening referenced output files | checker source and focused tests |
| 4 | Cover candidate check families from R28-T3: required fields, private output class vocabulary, output-content boundary, filename-only output evidence, downstream-release hold, source-slot privacy, and quality/source-pointer prerequisite hold | focused tests |
| 5 | Wire the checker into autorun and local hook catalog surfaces only after focused tests pass | catalog diff and command evidence |
| 6 | Add GC-051 registry source entries and regenerate aggregate only if a changed review/source evidence path requires it | registry drift check, if applicable |
| 7 | Create worker return with no-commit evidence and run required gates | worker return and command evidence |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T4 --title "MinerU Receipt Boundary Checker Implementation And Hook Wiring Decision" --date 2026-07-04 --base 55961ef2 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile, with protected governance path trigger active |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled source verification, protected-path authorization, implementation scope, worker output manifest, checker-output read-ahead mandate, handoff control, and R28 held-lane boundaries |
| checkerReadAheadConfirmation | dispatch-quality, handoff-boundary, lifecycle-hygiene, checker-read-ahead, operation-trace, delta-boundary, ADIF-disclosure, public-export, corpus-scan-registry, autorun catalog, and hook catalog source surfaces were read before authoring |
| docOnlyNewFields | `RECEIPT_BOUNDARY_CHECKER_IMPLEMENTATION_AND_HOOK_WIRING_DECISION`; `CHECKER_IMPLEMENTATION_AUTHORIZED_PENDING_WORKER_RETURN_REVIEW`; `MEMORY_ROUTE_STILL_HELD_AFTER_CHECKER_IMPLEMENTATION` |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly by reading the
failing checker source and matching the literal required shape. Worker should
return to orchestrator only for a source contradiction, forbidden-scope need,
live/provider/public/private-content requirement, dependency install,
destructive action, or missing authority that makes completion impossible.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order-authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class work-order-authoring --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | No ADIF-specific extra instruction is required beyond active guard orientation, literal-format gotchas, scaffold output, source verification, protected-path authorization, and worker-output checker read-ahead. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_corpus_scan_registry.py`; `governance/compat/check_core_guard_self_protection.py` |
| literalTokensReviewed | Status: DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Dispatch Prompt Envelope; Required First Reads; Preflight Checks; Execution Plan; Evidence Requirements; Acceptance Criteria; Review Gate; Closure Checklist; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Work-Order Fulfillment Manifest; Worker Return Packet Shape Contract; Core Guard Self-Protection Authorization; applicableCheckersRead; literalTokensReviewed; gateRunPurpose; Resolver query; Returned defects: NONE_RETURNED; Delta Execution Claim Boundary Control Block; Public Export Disposition; protected paths; source-not-found disposition spelling |
| gateRunPurpose | Confirmation evidence after checker read-ahead; gates confirm dispatch shape and do not define implementation scope. |
| claimBoundary | This read-ahead covers this dispatch packet only; worker-created checker, tests, catalog edits, registry entries, and worker return require their own source and checker read-ahead before editing. |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Active session state releases R28-T4 packet authoring after accepted R28-T3 checker-candidate design closure. | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `nextAllowedMove` field | `MSEA-R28-T4`; `4d64e33f` | active session bootstrap read model | ACCEPT |
| R28-T3 closure accepted design evidence and routed the next recommended move to R28-T4 checker implementation and hook wiring decision. | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | lines 7200-7221 | `selectedDesignDisposition`; `checkerImplementationDisposition`; `nextRecommendedMove` | active session state entry `mseaR28T3MineruReceiptBoundaryCheckerCandidateDesignClosure20260704` | ACCEPT |
| R28-T3 worker return selected design-only disposition and held implementation and memory-route release pending later work. | VALUE_SET | `docs/reviews/CVF_MSEA_R28_T3_MINERU_RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_WORKER_RETURN_2026-07-04.md` | lines 105-109 | `CHECKER_IMPLEMENTATION_HELD_PENDING_ACCEPTED_DESIGN`; `MEMORY_ROUTE_HELD_PENDING_ACTUAL_CHECKER_AND_QUALITY` | R28-T3 worker return | ACCEPT |
| R28-T3 companion matrix maps candidate check families and failure dispositions for a future checker. | VALUE_SET | `docs/reference/CVF_MSEA_R28_T3_MINERU_RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_MATRIX_2026-07-04.md` | lines 58-77 | `Checker Candidate Design Matrix` | R28-T3 companion design matrix | ACCEPT |
| R26 records checker candidate status and check families without authorizing implementation in R26. | VALUE_SET | `docs/reference/CVF_MSEA_R26_T1_MINERU_RECEIPT_SCHEMA_WRITER_CONTRACT_AND_CHECKER_CANDIDATE_DESIGN_2026-07-04.md` | lines 100-111 | `checkerCandidateStatus`; `CHECKER_CANDIDATE`; `NOT_AUTHORIZED_BY_R26` | R26 receipt contract | ACCEPT |
| R24-T4 defines private receipt envelope fields and private output classes the checker must protect. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md` | lines 39-66 | `outputContentRead`; `downstreamRelease`; `PRIVATE_INPUT_ONLY`; `PRIVATE_RUNTIME_COPY`; `PRIVATE_GENERATED_OUTPUT`; `RECEIPT_METADATA_ALLOWED` | R24-T4 private-output policy | ACCEPT |
| R27 keeps memory-safe candidate and memory write routes held pending receipt, quality, source pointer, allowed downstream use, claim boundary, and a fresh memory owner work order. | VALUE_SET | `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md` | lines 77-87 | `QUALITY_DISPOSITION_READY`; `MEMORY_SAFE_CANDIDATE_READY`; `MEMORY_WRITE_AUTHORIZED`; `NOT_AUTHORIZED_BY_R27` | R27 decision ledger | ACCEPT |
| R28-T1 writer source exposes held downstream release, required receipt object, output-content-read rejection, filename allowlist, payload renderer, and JSON renderer. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 18, 26, 48, 66, 93-104, 112, 135-137, 159, 178 | `DOWNSTREAM_RELEASE_HELD`; `ALLOWED_OUTPUT_FILE_NAMES`; `OUTPUT_CONTENT_READ_FORBIDDEN`; `MineruMetadataReceipt`; `_validate_output_file_name`; `build_mineru_metadata_receipt`; `mineru_metadata_receipt_payload`; `render_mineru_metadata_receipt_json` | Extraction Foundation metadata receipt writer | ACCEPT |
| R28-T1 writer tests prove stable payload, held downstream release, false output-content-read behavior, and output-content-read rejection. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` | lines 42, 59, 62-64, 98, 112, 133 | `test_receipt_payload_contains_required_r24_r26_metadata_fields`; `test_json_rendering_is_stable_and_metadata_only`; `test_downstream_lanes_remain_held_for_future_packets`; `OUTPUT_CONTENT_READ_FORBIDDEN` | Extraction Foundation metadata receipt writer tests | ACCEPT |
| Autorun common command catalog is the source-visible surface for adding a range-aware checker to agent autorun gates. | EXISTS | `governance/compat/agent_autorun_command_catalog.py` | lines 41-56 and 84-90, 132-134, 360-362 | `_range_command`; `_common_commands`; `check_work_order_dispatch_quality.py`; `check_agent_handoff_boundary.py`; `check_corpus_scan_registry.py` | agent autorun command catalog | ACCEPT |
| Local hook chains route pre-commit and pre-push checks through catalog source files. | EXISTS | `governance/compat/local_governance_hook_catalog.py` | lines 7-22 | `PRE_COMMIT_CHECKS`; `PRE_PUSH_CHECKS`; `HOOK_CHAINS` | local governance hook catalog | ACCEPT |
| Pre-commit hook catalog is the source-visible surface for adding a checker command to pre-commit. | EXISTS | `governance/compat/local_governance_hook_catalog_pre_commit.py` | lines 6, 64, 96, 208, 251, 331 | `PRE_COMMIT_CHECKS`; `check_work_order_dispatch_quality.py`; `check_agent_handoff_boundary.py`; `check_corpus_scan_registry.py`; `changed corpus registry coverage`; `dispatch scaffold provenance` | pre-commit hook catalog | ACCEPT |
| Pre-push hook catalog is the source-visible surface for adding a checker command to pre-push. | EXISTS | `governance/compat/local_governance_hook_catalog_pre_push.py` | lines 6, 37, 65, 405 | `PRE_PUSH_CHECKS`; `check_work_order_dispatch_quality.py`; `check_agent_handoff_boundary.py`; `dispatch scaffold provenance` | pre-push hook catalog | ACCEPT |
| GC-051 corpus scan registry checker scans changed review files for real extension path mentions and requires registry coverage when applicable. | RUNTIME_BEHAVIOR | `governance/compat/check_corpus_scan_registry.py` | lines 111-129, 213-235 | `_get_changed_corpus_scan_files`; `_extract_corpus_paths_from_text`; `_check_audit_coverage` | GC-051 corpus scan registry checker | ACCEPT |

## New Doc-Only Fields

| Field or token | Purpose | Source fact type | Worker rule |
| --- | --- | --- | --- |
| `RECEIPT_BOUNDARY_CHECKER_IMPLEMENTATION_AND_HOOK_WIRING_DECISION` | selected R28-T4 route token | DOC_ONLY_NEW | use for this dispatch only |
| `CHECKER_IMPLEMENTATION_AUTHORIZED_PENDING_WORKER_RETURN_REVIEW` | bounded implementation authorization token | DOC_ONLY_NEW | checker implementation remains unaccepted until reviewer closure |
| `MEMORY_ROUTE_STILL_HELD_AFTER_CHECKER_IMPLEMENTATION` | memory-route hold token for T4 | DOC_ONLY_NEW | preserve R27/R28 memory hold even if checker implementation passes |

## Current Runtime Freshness Verification

| Check | Evidence | Disposition |
| --- | --- | --- |
| Existing checker path check | `Test-Path governance/compat/check_mineru_receipt_boundary.py` returned `False` before authoring. | PASS |
| Existing focused test path check | `Test-Path governance/compat/test_check_mineru_receipt_boundary.py` returned `False` before authoring. | PASS |
| Existing receipt writer owner check | `rg -n "DOWNSTREAM_RELEASE_HELD|ALLOWED_OUTPUT_FILE_NAMES|OUTPUT_CONTENT_READ_FORBIDDEN|class MineruMetadataReceipt|def _validate_output_file_name|def build_mineru_metadata_receipt|def mineru_metadata_receipt_payload|def render_mineru_metadata_receipt_json" EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` confirmed the current writer owner surface. | PASS |
| Existing hook/catalog owner check | `rg -n "PRE_COMMIT_CHECKS|PRE_PUSH_CHECKS|_common_commands|_range_command" governance/compat/agent_autorun_command_catalog.py governance/compat/local_governance_hook_catalog.py governance/compat/local_governance_hook_catalog_pre_commit.py governance/compat/local_governance_hook_catalog_pre_push.py` confirmed catalog owner surfaces. | PASS |
| Freshness disposition | No current R28-T4 checker implementation or focused checker test exists; current owner surfaces are R28-T1 writer source/tests, R28-T3 design matrix, and existing autorun/local hook catalogs. | PASS |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Planned artifact paths absent before authoring | `Test-Path` returned `False` for the planned R28-T4 GC-018, work order, checker source, checker test, and worker return paths. | PASS |
| Token search for R28-T4 lane before authoring | `rg -n --fixed-strings "MSEA-R28-T4" docs CVF_SESSION governance EXTENSIONS` returned only current session next-move references and archived V35 next-move text before this packet was created. | PASS |
| Collision decision | No existing R28-T4 dispatch, checker implementation, focused test, or worker return exists; this work order may create the first dispatch packet. | PASS |

## Roadmap-To-Work-Order Trace Matrix

| Predecessor requirement | Source evidence | R28-T4 handling |
| --- | --- | --- |
| R28-T3 accepted checker-candidate design | R28-T3 material commit `4d64e33f`; worker return and companion matrix | allow one checker implementation and hook-wiring decision tranche |
| R28-T1 writer source evidence | writer source/tests and GC-051 registry entries | use as fixture/invariant source only; do not edit writer |
| R26 checker-candidate criteria | R26 reference lines 100-111 | implement deterministic checks only for candidate families named there and refined by R28-T3 |
| R24-T4 private-output policy | R24-T4 policy lines 39-66 | enforce metadata/no-content-read boundary for receipt fields |
| R27 scan-to-memory route matrix | R27 decision ledger lines 77-87 | keep memory route held; no memory write or RAG release |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | local governance checker and autorun/hook catalog surfaces | internal worker may create deterministic checker and catalog rows under WORKER_MUST_NOT_COMMIT; reviewer must accept before closure | this work order, paired GC-018, source verification, focused tests, worker return | internal-only local Python checker; no external adapter | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no CLI/MCP or external adapter owner in R28-T4 | external ingress, authentication, approval, receipt, raw-data, mutation, and public boundaries remain out of scope | no source-verified external adapter authority in R28-T4 | adapter deferred; no CLI/MCP surface implemented or claimed | DEFERRED_WITH_REASON |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Corpus scan or extraction intake |
| Chain map route | corpus/source evidence -> CVF-owned references and runtime source verification -> fresh GC-018/work order -> autorun pre-dispatch gates |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired R28-T4 GC-018 and this work order |
| Disposition | ADAPT prior R28/R26/R24/R27 evidence into a bounded checker implementation dispatch; no external source becomes authority by itself |
| Claim boundary | routing evidence only; no external repository absorption, private/generated content read, runtime/provider/live proof, public-sync, app, or production claim |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| Foundation storage standard | `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` |
| Guard owner | `governance/compat/check_foundation_storage_layout.py` |
| Trigger reason | this work order creates durable governance checker and hook-catalog work under `governance/compat/` |
| Stable location decision | new checker and focused test stay in the existing `governance/compat/` checker/test family; hook wiring stays in existing catalog files |
| Index or front-door decision | no new `docs/reference/` family, front door, or stable reference folder is created |
| Archive or rotation decision | N/A with reason: no existing durable governance file is split, moved, archived, or rotated in this dispatch |
| Generated aggregate decision | registry aggregate may change only if GC-051 requires source-entry coverage and only through the existing generator |
| Claim boundary | storage-layout evidence only; no runtime/provider/live/public/Web/MCP/model-router behavior claim |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: create one MinerU receipt-boundary checker,
focused tests, and bounded autorun/local hook catalog wiring for that checker
only.

Protected paths:

- `governance/compat/check_mineru_receipt_boundary.py`
- `governance/compat/test_check_mineru_receipt_boundary.py`
- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_pre_push.py`
- `docs/corpus-intelligence/registry/entries/msea-r28-t4-mineru-receipt-boundary-checker-source.json` only if GC-051 coverage is required
- `docs/corpus-intelligence/registry/entries/msea-r28-t4-mineru-receipt-boundary-checker-tests.json` only if GC-051 coverage is required
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` only when regenerated from source entries

Operator authorization: operator instructed authoring a fresh R28-T4
source-verified work order for receipt-boundary checker implementation and hook
wiring decision after R28-T3 closure.

Rollback boundary: revert only R28-T4 checker, focused test, catalog wiring,
registry source/aggregate, and worker-return artifacts if rejected; do not
modify or revert R28-T1, R28-T3, R24, R26, R27, active session, active handoff,
or public-sync artifacts.

Not authorized: no session-state edit by worker, AGENTS.md edit, active handoff
edit, MinerU runtime execution, private/generated content read, memory/RAG
write, provider/live proof, public-sync, external adapter, standalone app,
legal/use-case deep dive, extraction accuracy, document truth, current-law
correctness, workflow-chain production readiness, worker stage, worker commit,
or push.

## Worker Output Checker Read-Ahead Mandate

Before writing each worker-owned output artifact, read checker source for that
file's docType, path family, and conditional content class.

| Output artifact | Required read-ahead result |
| --- | --- |
| worker return under reviews | derive exact review headings, worker-return quality terms, trace labels, delta boundary labels, corpus/value/rescan tokens, and no-commit evidence shape before writing |
| checker source under governance compatibility | derive CLI argument pattern, changed-path handling, diagnostics, encoding behavior, and no private content read boundary from nearby checker source |
| focused tests under governance compatibility | derive existing unittest import pattern and fixture style from focused checker tests |
| optional registry entries | derive generated-source discipline from GC-051 checker and registry generator before editing any aggregate |

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
| baseHeadFor(phase) | dispatchBaseHead=55961ef2; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | dispatcher owns this work order and paired GC-018; worker owns only the allowed checker/test/catalog/conditional-registry/worker-return paths; reviewer owns closure repairs and material commit; steward owns session-sync when closure exists |
| traceScope(phase, actor) | each actor records before status, after status, diff evidence, and no-commit or commit ownership evidence |
| commitOwner(phase) | dispatcher may commit dispatch; worker is WORKER_MUST_NOT_COMMIT; reviewer/closer may commit accepted worker outputs; session-sync steward may commit continuity updates only when material closure exists |
| crossBatchIsolation | R28-T4 must not mix with runtime, memory/RAG, public-sync, Web/UI, MCP/CLI, active session, active handoff, R28-T1 writer mutation, R28-T3 design mutation, or private/generated content work |
| nextMoveSurfaces | reviewer/closer and session-sync steward update next allowed move only when accepted R28-T4 closure exists |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R28_T4_MINERU_RECEIPT_BOUNDARY_CHECKER_IMPLEMENTATION_AND_HOOK_WIRING_DECISION_COMPLETION_2026-07-04.md` |
| reviewerOwnedClosurePaths | worker return, allowed worker-owned implementation artifacts, optional completion review only if needed, and allowed reviewer repairs inside those artifacts |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `governance/compat/check_mineru_receipt_boundary.py` | create deterministic checker with `--base`, `--head`, and `--enforce`, narrow changed-file applicability, safe UTF-8 reads, no MinerU/runtime/provider invocation, and diagnostics for candidate failure classes |
| `governance/compat/test_check_mineru_receipt_boundary.py` | create focused tests for valid metadata receipt, missing required fields, invalid private output class, true output-content-read, disallowed output file name, unauthorized downstream release, unsafe source slot, missing quality/source-pointer prerequisite hold, and changed-path applicability |
| `governance/compat/agent_autorun_command_catalog.py` | add one range-aware command for the new checker only if focused tests pass |
| `governance/compat/local_governance_hook_catalog_pre_commit.py` | add one command for the new checker only if focused tests pass |
| `governance/compat/local_governance_hook_catalog_pre_push.py` | add one command for the new checker only if focused tests pass |
| conditional GC-051 registry source entries and aggregate | create/regenerate only if changed review/source evidence makes GC-051 coverage necessary |
| worker return | create worker return with source verification deltas, checker read-ahead, command evidence, no-commit statement, implementation disposition, memory-route hold, and next allowed move recommendation |

## Required Artifact Manifest

| Path | Required at handoff |
| --- | --- |
| `governance/compat/check_mineru_receipt_boundary.py` | yes |
| `governance/compat/test_check_mineru_receipt_boundary.py` | yes |
| `docs/reviews/CVF_MSEA_R28_T4_MINERU_RECEIPT_BOUNDARY_CHECKER_IMPLEMENTATION_AND_HOOK_WIRING_DECISION_WORKER_RETURN_2026-07-04.md` | yes |
| `governance/compat/agent_autorun_command_catalog.py` | no |
| `governance/compat/local_governance_hook_catalog_pre_commit.py` | no |
| `governance/compat/local_governance_hook_catalog_pre_push.py` | no |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R28_T4_MINERU_RECEIPT_BOUNDARY_CHECKER_IMPLEMENTATION_AND_HOOK_WIRING_DECISION_WORKER_RETURN_2026-07-04.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required worker-return terms (write section names without the heading
prefix; reserve actual heading syntax for real sections in the worker
return itself, not in this reminder list):

- Purpose
- Scope / Methodology
- Findings / Position
- Risk / Corrective Action
- Claim Boundary
- Agent Operation Trace Block
- Delta Execution Claim Boundary Control Block
- Public Export Disposition
- executionBaseHead
- git status --short

Conditional worker-return terms (include each as a real section with
`N/A with reason` or `NOT_APPLICABLE_WITH_REASON` when not applicable):

- External Knowledge Intake Routing
- Rescan Intelligence Hardening
- Corpus Completeness And Report Integrity
- Finding-To-Governance Learning Disposition
- Epistemic Process Block
- Machine Closure Package

Shape-list rule: when listing required worker-output sections, write section
names without the heading prefix. Reserve actual heading syntax for real
sections so structural checkers do not treat checklist text as the artifact
section body.

## Evidence Requirements

| Evidence | Required form |
| --- | --- |
| checker behavior | focused tests covering accepted R28-T3 candidate families and failure dispositions |
| no runtime/private-content boundary | checker source and worker return must state and demonstrate no file opening beyond committed receipt artifact text/JSON and no referenced output-file content read |
| hook wiring | catalog diffs plus successful focused tests and gate evidence |
| GC-051 handling | either no registry change required with reason, or generated source entries plus aggregate drift check |
| memory-route hold | explicit `MEMORY_ROUTE_STILL_HELD_AFTER_CHECKER_IMPLEMENTATION` or source-backed stronger hold |
| worker commit boundary | HEAD unchanged, exact status output, and no stage/commit/push statement |

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| Checker source | deterministic checker exists at the owned path with no runtime/provider/private-content action |
| Focused tests | focused tests pass and cover the candidate check families from R28-T3 |
| Hook/autorun wiring | catalog wiring exists only if focused tests pass and is bounded to the new checker command |
| Registry coverage | GC-051 coverage is satisfied if changed review/source evidence requires it |
| Memory route | memory/RAG route remains held pending quality/source-pointer and memory owner prerequisites |
| Output scope | worker touches only allowed paths or returns BLOCKED_WITH_REASON |
| Gates | focused tests, worker-return fast gate, and pre-implementation autorun pass or return BLOCKED_WITH_REASON with exact blocker |
| Boundary | no runtime, private content, generated output, public-sync, provider/live, app, legal-quality, production, or memory-write claim |

Fail conditions:

- worker edits forbidden R28, session, handoff, AGENTS, public-sync, runtime, Web/UI, MCP/CLI, memory/RAG, private document, or generated output paths;
- checker opens referenced output files, reads generated output content, runs MinerU, imports Candidate Group A, or uses provider/live secrets;
- checker claims extraction accuracy, document truth, legal/current-law correctness, memory-write authorization, external-agent support, public readiness, production readiness, or universal enforcement;
- hook wiring is added before focused tests pass;
- GC-051 required coverage is omitted when changed review/source evidence requires it.

## Review Gate

Reviewer/closer must verify:

- worker did not stage, commit, push, or mutate forbidden paths;
- checker and tests match R28-T3 accepted candidate design without widening into runtime/private-output reads;
- hook/autorun catalog edits are minimal and source-visible;
- GC-051 registry coverage is either not required with reason or generated from source entries;
- memory route remains held after checker implementation;
- worker output artifacts satisfy review/source/docType heading needs;
- command evidence uses real base/head ranges, not base=head.

## Closure Checklist

| Item | Required disposition |
| --- | --- |
| Checker source created | checked, or BLOCKED with return action |
| Focused tests created and pass | checked, or BLOCKED with return action |
| Hook/autorun wiring bounded | checked, or BLOCKED with return action |
| GC-051 coverage handled | checked, or N/A with reason |
| No forbidden runtime/private/provider/public/memory action | checked, or BLOCKED with return action |
| Gates run | checked, or BLOCKED with exact command evidence |
| Next allowed move stated | checked after review decision |
| Session sync | reviewer/steward only when material closure exists |

## Verification Commands

```powershell
python -m unittest governance.compat.test_check_mineru_receipt_boundary
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_mineru_receipt_boundary.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 55961ef2 --head HEAD
git status --short --untracked-files=all
```

If the focused test target changes during implementation, use the matching
repo-local unittest or pytest invocation and record the exact command.

## Operator Checkpoint

operator.checkpoint.waiver: Operator already authorized R28-T4 dispatch packet
authoring from the accepted R28-T3 design; worker implementation remains bounded
by this source-verified work order and returns uncommitted for reviewer closure.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | Codex local workspace |
| Session or invocation | MSEA-R28-T4 MinerU Receipt Boundary Checker Implementation And Hook Wiring Decision, 2026-07-04 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, scaffold helper, apply_patch, governance gates |
| Target paths | `docs/baselines/CVF_GC018_MSEA_R28_T4_MINERU_RECEIPT_BOUNDARY_CHECKER_IMPLEMENTATION_AND_HOOK_WIRING_DECISION_2026-07-04.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T4_MINERU_RECEIPT_BOUNDARY_CHECKER_IMPLEMENTATION_AND_HOOK_WIRING_DECISION_2026-07-04.md` |
| Allowed scope source | active session state nextAllowedMove and operator request |
| Before status evidence | clean worktree evidence: `git status --short` returned no output before authoring |
| After status evidence | dispatcher pre-dispatch gates to be recorded before commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | operator requested fresh R28-T4 work-order authoring |
| Claim boundary | dispatch authoring only; no worker execution, runtime, memory/RAG, public-sync, provider/live, private/generated content read, or production claim |
| Agent type | dispatcher |
| Invocation ID | `msea-r28-t4-dispatch-2026-07-04` |
| Expected manifest | `docs/baselines/CVF_GC018_MSEA_R28_T4_MINERU_RECEIPT_BOUNDARY_CHECKER_IMPLEMENTATION_AND_HOOK_WIRING_DECISION_2026-07-04.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T4_MINERU_RECEIPT_BOUNDARY_CHECKER_IMPLEMENTATION_AND_HOOK_WIRING_DECISION_2026-07-04.md` |
| Actual changed set | `docs/baselines/CVF_GC018_MSEA_R28_T4_MINERU_RECEIPT_BOUNDARY_CHECKER_IMPLEMENTATION_AND_HOOK_WIRING_DECISION_2026-07-04.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T4_MINERU_RECEIPT_BOUNDARY_CHECKER_IMPLEMENTATION_AND_HOOK_WIRING_DECISION_2026-07-04.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename performed |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R28-T4 local checker implementation work order |
| claimDisposition | CLAIM_REJECTED: no runtime-enforcement, direct-interception, mandatory-wrapper, universal governed-coding, or provider behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: predecessor metadata receipt writer evidence is cited, but this work order creates no runtime receipt. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: this work order runs no MinerU, provider, memory, or external action. |
| invocationBoundary | local source verification, deterministic checker implementation, focused tests, catalog wiring, governance gates, and worker return only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized. |
| claimLanguage | local checker implementation dispatch only |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router behavior or memory write without fresh source-verified authorization. |

## Claim Boundary

This work order authorizes a no-commit worker to implement and test a local
deterministic MinerU receipt-boundary checker and bounded hook/autorun catalog
wiring. It does not authorize MinerU runtime execution, private content read,
generated output read, memory/RAG write, adapter work, public-sync,
provider/live proof, standalone app work, legal/use-case deep dive, extraction
accuracy, document truth, legal quality, current-law correctness,
workflow-chain production readiness, worker stage, worker commit, or push.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R28-T4 is private provenance governance-checker dispatch work and does
not change the public-sync repository or public catalog.
