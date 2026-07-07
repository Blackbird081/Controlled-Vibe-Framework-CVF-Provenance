# CVF Agent Work Order - MSEA-R10 MinerU Adapter Contract Draft

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Date: 2026-07-03

Batch ID: MSEA-R10

Dispatch base head: 7c19b587

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: reviewer/closer role for the worker return handoff

Worker return path: `docs/reviews/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_WORKER_RETURN_2026-07-03.md`

Companion reference path: `docs/reference/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA-R10.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md`

Paired GC-018 baseline: `docs/baselines/CVF_GC018_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-03.

Do-not-misread notes: this work order authorizes a documentation/reference-only
adapter contract draft. It does not authorize schema implementation,
receipt-writer code, adapter implementation, MinerU install/runtime, model
download, parser/OCR/VLM/hybrid/API/router/Gradio/Docker execution,
provider/live call, credentials/S3, RAG write, source import, package
activation, checker implementation, public-sync, Web/MCP/model-router,
action-authority, benchmark, document-truth, extraction-accuracy, or
production-readiness work.

Required first actions: read startup files, guard orientation, literal gotchas,
ADIF-0023, this work order, the paired GC-018 baseline, source files named in
Source Verification, and checker source for each output artifact's `docType`,
path family, and conditional content class before writing any artifact.

Return contract: create only the worker return and companion reference, run
required gates, leave changes uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Draft a CVF-owned MinerU adapter contract reference that binds the accepted
MSEA-R7 receipt artifact/field vocabulary and MSEA-R9 application-route
blueprint into a documentation/reference contract for future CVF use. The
contract should make clear what a future adapter would need to exchange,
record, and refuse to claim, while preserving all runtime/provider/S3/RAG/
Docker/checker lanes as held behind fresh authorization.

## Authority Chain

| Authority | Path | Role |
|---|---|---|
| Active next move | `CVF_SESSION/ACTIVE_SESSION_STATE.json` and `CVF_SESSION_MEMORY.md` | authorizes fresh MSEA-R10 GC-018/work-order authoring for docs-only adapter contract draft |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md` | source verification and dispatch boundary |
| MSEA-R9 accepted route | `docs/reviews/CVF_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_SELECTION_WORKER_RETURN_2026-07-02.md`; `docs/reference/CVF_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_2026-07-02.md` | selected and accepted `OPEN_ADAPTER_CONTRACT_DRAFT_ONLY` |
| Receipt vocabulary | `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` | artifact families, field families, backend variant boundary |
| Route and boundary surfaces | MSEA-T2/R4/R5/R6/R8 owner surfaces | receipt, RAG, runtime, provider, S3, Docker, checker, and corpus boundaries |
| Source mirror | `.private_reference/source_mirrors/INDEX.md`; `.private_reference/source_mirrors/opendatalab__MinerU/` | pinned upstream authority input, not runtime dependency |

## Agent Roles

| Role | Owner | Boundary |
|---|---|---|
| Dispatcher | dispatcher role | created this work order and paired GC-018; does not execute worker task |
| Worker | delegated worker | creates only planned worker return and companion reference; must not commit, stage, or push |
| Reviewer/closer | reviewer/closer role | validates pending artifacts, repairs only allowed-scope defects, commits if accepted |
| Session-sync steward | session-sync steward role | updates session state only once an accepted material commit exists |

## Scope

Allowed:

- Read accepted MSEA-T2/R4/R5/R6/R7/R8/R9 artifacts and the source mirror index.
- Recompute source mirror commit and file count.
- Draft one CVF-owned adapter contract reference under `docs/reference`.
- Create one worker return under `docs/reviews`.
- Include source-backed sections for contract scope, receipt family mapping,
  field-family obligations, backend variant boundary, application route
  bindings, non-claim language, held-lane reopen conditions, and future
  implementation prerequisites.

Forbidden:

- MinerU install, runtime execution, model download, parser/OCR/VLM/hybrid run,
  API/router/Gradio/Docker execution, provider/live call, credentials/S3,
  RAG write, source import, package activation, checker implementation,
  public-sync, Web/MCP/model-router/action-authority, automatic invocation,
  benchmark, document-truth, extraction-accuracy, schema implementation,
  receipt-writer code, adapter implementation, or production-readiness claims.

## Write Ownership

| Path | Worker disposition |
|---|---|
| `docs/reviews/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_WORKER_RETURN_2026-07-03.md` | create only; leave uncommitted |
| `docs/reference/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md` | create only; leave uncommitted |

No other file is worker-owned. If another file appears necessary, return
`BLOCKED_WITH_REASON`.

## Worker Autonomy / No-Question Rule

The worker should execute the docs-only draft using the source-backed packet
without asking the operator to choose between full or sampled work. If a runtime
or implementation decision appears necessary, record the missing authorization
and return `BLOCKED_WITH_REASON` or preserve it as a held lane; do not execute
runtime work.

## Intake Role Routing Decision

- Intake summary: operator asked the dispatcher to handle MSEA-R10, following MSEA-R9
  acceptance of `OPEN_ADAPTER_CONTRACT_DRAFT_ONLY`.
- Scope classification: bounded external repository evidence synthesis into a
  documentation/reference adapter contract draft.
- Risk sensitivity: no runtime, public-sync, provider/live run, secret,
  credential, package activation, checker implementation, production, adapter
  execution, schema implementation, receipt-writer code, document-truth, or
  extraction-accuracy claim.
- Selected role route: routeMode=SINGLE_AGENT_MULTI_ROLE.
- Role separation basis: dispatcher authors packet, worker produces
  uncommitted artifacts, reviewer/closer owns acceptance and commit.
- Escalation condition: stop if scope/risk changes or if runtime/provider/S3/
  RAG/Docker/checker/package/public/schema/adapter action becomes needed.

## Single-Agent Multi-Role Control Block

- Role separation ledger: dispatcher, worker, reviewer/closer, and
  session-sync steward duties are recorded separately in this packet.
- Evidence basis: review must use git diff, source paths, worker return,
  companion reference, and gate output, not memory-only claims.
- Self-review boundary: this block does not claim independent review by a
  second human or provider.
- Escalation conditions: stop for operator checkpoint if the worker needs
  runtime execution, provider/live proof, secrets, credentials, public-sync,
  source import, Docker execution, checker implementation, schema
  implementation, adapter implementation, or broader write scope.
- Gate sequence: worker runs pre-implementation and worker-return fast gates;
  reviewer/closer runs reviewer/steward and pre-closure gates on a real range.

## Dependency Release Evidence

| Dependency | Evidence | Release disposition |
|---|---|---|
| R9 selected docs-only adapter contract route | MSEA-R9 worker return `## Reviewer Decision` accepted `OPEN_ADAPTER_CONTRACT_DRAFT_ONLY`; R9 reference `## Selected Routing Outcome` records the same token | SATISFIED |
| R7 receipt vocabulary exists | R7 reference records `## Receipt Artifact Family Map`, `## Field Family Map`, and `## Backend Variant Boundary` | SATISFIED |
| Runtime/provider/S3/RAG/Docker/checker holds remain parked | R4/R5/R8 owner surfaces record candidate and hold conditions; active next move forbids implementation | SATISFIED |
| Worker-output checker-shape learning recorded | ADIF-0023 and literal gotcha item 38 exist; guard orientation worker row requires output-artifact checker read-ahead | SATISFIED |

## Pre-Flight Checks

| Check | Evidence | Disposition |
|---|---|---|
| Worktree clean before dispatch authoring | `git status --short` returned no changes before MSEA-R10 authoring | ACCEPT |
| Planned artifact paths absent | `Test-Path` returned `False` for planned baseline, work order, worker return, and reference paths before authoring | ACCEPT |
| Source mirror current | `git -C .private_reference/source_mirrors/opendatalab__MinerU rev-parse HEAD` returned `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`; file count command returned `425` | ACCEPT |
| ADIF dispatcher resolver | dispatcher query returned `NONE_RETURNED` | ACCEPT |
| Scaffold helper consulted | `build_dispatch_packet_scaffold.py` generic-worker-dispatch profile reviewed | ACCEPT |

## Required First Reads

| Path | Purpose |
|---|---|
| `CVF_SESSION_MEMORY.md` | active front door and next move |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | compact current state |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | canonical state registry |
| `AGENT_HANDOFF_V32_2026-07-02.md` | active handoff |
| `docs/reference/guard_orientation/README.md` | role and artifact-shape orientation |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | literal-format traps |
| `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0023.md` | worker-output checker-shape lesson |
| `docs/baselines/CVF_GC018_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md` | paired source-verified baseline |
| `docs/reference/CVF_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_2026-07-02.md` | accepted R9 blueprint/readiness reference |
| `docs/reviews/CVF_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_SELECTION_WORKER_RETURN_2026-07-02.md` | accepted R9 route and reviewer decision |
| `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` | receipt artifact/field/backend vocabulary |
| `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md` | predecessor route decision |
| `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | receipt/quality/RAG boundary |
| `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md` | runtime/API/Docker candidate boundaries |
| `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` | deep document, provider, S3, RAG candidate boundaries |
| `docs/reference/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md` | residual corpus closure and held candidate enrichment |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order-authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class work-order-authoring --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | ADIF-0023 is still a worker Required First Read because this work order creates worker output artifacts subject to checker-shape traps |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | `## Dispatch Prompt Envelope`; `## Source Verification Block`; `## Negative Search And Collision Discipline`; `## Agent Handoff Contract Control Block`; `## Reviewer Closure Conversion`; `## Work-Order Fulfillment Manifest`; `## Worker Output Artifact Checker-Shape Plan`; `## Worker Return Packet Shape Contract`; `WORKER_RETURN_FULL_GATE_V1`; `requiredGate:`; `individualCheckerSubstitution: FORBIDDEN`; `workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED`; `## External Knowledge Intake Routing`; `## External Absorption Core`; `## Corpus Completeness And Report Integrity`; `## External Absorption Value Conversion Matrix`; `## Overlap And Novelty Classification`; `## Source Mirror Migration Control`; `## Target / Source`; `## Scope / Applies To`; `ledger_terminal=`; `CHECKER_CANDIDATE`; `REMOVED_OR_REJECTED`; `RESOLVED_BY_DESIGN`; `DEFERRED_PRIVATE_ONLY`; `CLAIM_REJECTED_NO_RECEIPT`; `CLAIM_REJECTED_NO_ACTION`; `PARTIAL` |
| gateRunPurpose | Confirmation evidence for dispatch packet readiness, not first discovery |
| claimBoundary | Dispatch authoring read-ahead only; worker must perform output-artifact checker read-ahead before writing worker return or companion reference |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| R10 is authorized by current next move | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | `nextAllowedMove` | `MSEA-R10 documentation/reference-only MinerU adapter contract draft` | active session state | ACCEPT |
| R9 selected the docs-only adapter contract route | VALUE_SET | `docs/reference/CVF_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_2026-07-02.md` | lines 103-114, `## Selected Routing Outcome` | `OPEN_ADAPTER_CONTRACT_DRAFT_ONLY` | MSEA-R9 reference | ACCEPT |
| R9 reviewer accepted the route | VALUE_SET | `docs/reviews/CVF_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_SELECTION_WORKER_RETURN_2026-07-02.md` | lines 470-480, `## Reviewer Decision` | `ACCEPT_FOR_MATERIAL_COMMIT` | MSEA-R9 worker return | ACCEPT |
| R7 receipt families exist | VALUE_SET | `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` | lines 63-76, `## Receipt Artifact Family Map` | `layout.pdf`; `span.pdf`; `model.json`; `middle.json`; `content_list.json`; `content_list_v2.json` | MSEA-R7 reference | ACCEPT |
| R7 field and backend sections exist | EXISTS | `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` | lines 79-116 | `Field Family Map`; `Backend Variant Boundary`; `Downstream Use Boundary` | MSEA-R7 reference | ACCEPT |
| R6 predecessor route selected receipt-contract drafting | VALUE_SET | `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md` | lines 38-52 and 88-108 | `OPEN_RECEIPT_SCHEMA_CONTRACT_DRAFT` | MSEA-R6 route matrix | ACCEPT |
| T2 owns receipt/quality/RAG boundary | EXISTS | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | `## Receipt Advisory`; `## Claim Boundary` | `Receipt Advisory` | MSEA-T2 reference | ACCEPT |
| Runtime/provider/S3/Docker/RAG/package routes remain held | VALUE_SET | `docs/reference/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md` | lines 217-229 and 282-315 | `RUNTIME_CANDIDATE`; `PACKAGE_CANDIDATE`; `REJECT_DIRECT_IMPORT` | MSEA-R8 residual ledger | ACCEPT |
| Source mirror is preferred current MinerU source input | VALUE_SET | `.private_reference/source_mirrors/INDEX.md` | row `opendatalab__MinerU` | `.private_reference/source_mirrors/opendatalab__MinerU/` | source mirror index | ACCEPT |

## New Doc-Only Fields

| Field | Purpose |
|---|---|
| adapterContractSection | Section name in the planned R10 reference |
| receiptFamilyMapping | Mapping from MSEA-R7 receipt family vocabulary to adapter contract obligations |
| applicationRouteBinding | Mapping from MSEA-R9 blueprint layers to contract sections |
| nonRuntimeHoldCondition | Held-lane condition carried into the contract draft |

## Current Runtime Freshness Verification

| Check | Evidence | Disposition |
|---|---|---|
| Source mirror commit | Dispatcher observed `git -C .private_reference/source_mirrors/opendatalab__MinerU rev-parse HEAD` returned `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`; worker must recompute | ACCEPT |
| Source mirror file count | Dispatcher observed `git -C .private_reference/source_mirrors/opendatalab__MinerU ls-files` returned `425` files; worker must recompute | ACCEPT |
| Runtime scope | Active next move and this work order forbid runtime/provider/live/package/checker/public/schema/adapter implementation work | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Planned baseline path | `Test-Path docs/baselines/CVF_GC018_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md` returned `False` before authoring | ACCEPT |
| Planned work-order path | `Test-Path docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md` returned `False` before authoring | ACCEPT |
| Planned worker return path | `Test-Path docs/reviews/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_WORKER_RETURN_2026-07-03.md` returned `False` before authoring | ACCEPT |
| Planned reference path | `Test-Path docs/reference/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md` returned `False` before authoring | ACCEPT |
| Token search | `rg -n "MSEA-R10|MinerU Adapter Contract Draft|CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT" docs CVF_SESSION AGENT_HANDOFF_V32_2026-07-02.md` found only current next-move references before this dispatch | ACCEPT |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | dispatcher authored baseline/work order; delegated worker creates pending artifacts; reviewer/closer owns material commit; session-sync steward updates state only once an accepted material commit exists |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=7c19b587; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | worker may create only the planned worker return and planned reference output |
| traceScope(phase, actor) | worker records operation trace in worker return; reviewer validates and commits material artifacts if accepted |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT for worker; reviewer/closer owns material commit |
| crossBatchIsolation | no unrelated artifacts, session-sync, protected paths, runtime/source, checker, package, public-sync, or Web/MCP paths may be edited by worker |
| nextMoveSurfaces | worker must not edit next-move surfaces; reviewer/session-sync steward updates them only once an accepted material commit exists |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | N/A_WITH_REASON: no separate `_COMPLETION_` reviewer artifact is planned; prefer repairing evidence in the worker return per literal-format gotcha 30 |
| reviewerOwnedClosurePaths | worker return and reference output during reviewer acceptance; session-sync surfaces only in a later dedicated commit |
| closureOwner | reviewer/closer role |
| workerCommitPermission | FORBIDDEN |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| `docs/reviews/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_WORKER_RETURN_2026-07-03.md` | create from worker-return scaffold, fill evidence, include completion status, run worker-return fast gate, leave uncommitted |
| `docs/reference/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md` | create CVF-owned adapter contract draft with `## Scope / Applies To`, source-backed contract sections, hold conditions, non-claims, and claim boundary |

## Worker Output Artifact Checker-Shape Plan

The worker must not treat this dispatch packet checklist as sufficient for the
files the worker creates. Before writing long prose, derive an output-artifact
shape checklist from checker source and record it in the worker return.

| Output artifact | Required pre-write action | Minimum literal requirements to confirm |
|---|---|---|
| worker return under reviews folder | run `python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_WORKER_RETURN_2026-07-03.md --title "CVF MSEA-R10 MinerU Adapter Contract Draft Worker Return"`; run fast gate while skeleton is short | `## Target / Source`; `## Scope / Methodology`; `## Findings / Position`; `## Risk / Corrective Action`; `## External Knowledge Intake Routing`; `## Corpus Completeness And Report Integrity`; `## Finding-To-Governance Learning Disposition`; `## Epistemic Process Block`; `ledger_terminal=` if corpus claims are made; `CHECKER_CANDIDATE` if checker value is discussed; `REMOVED_OR_REJECTED` and `RESOLVED_BY_DESIGN` if a real rescan matrix is included |
| companion reference under reference folder | read structural and external-absorption checkers before writing | `## Scope / Applies To`; source authority; contract section matrix; receipt family mapping; overlap classification; value conversion matrix; source mirror control; claim boundary; public export disposition; no runtime claim language |

If any requirement appears inapplicable, keep the heading and record `N/A with
reason` or the checker-accepted not-applicable token rather than omitting the
section.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_WORKER_RETURN_2026-07-03.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | MinerU source mirror plus accepted MSEA owner surfaces -> CVF adapter contract draft reference -> future implementation only by fresh authorization |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py` |
| Owner surface | MSEA-R10 worker return and companion reference draft |
| Disposition | ADAPT: convert accepted receipt and route vocabulary into a CVF-owned adapter contract draft |
| Claim boundary | documentation/reference-only draft; no runtime, provider/live, S3, RAG, Docker, package, checker, source import, schema implementation, adapter implementation, public-sync, or production claim |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | `https://github.com/opendatalab/MinerU.git` at `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`; local mirror `.private_reference/source_mirrors/opendatalab__MinerU/`; accepted MSEA-T2/R4/R5/R6/R7/R8/R9 evidence |
| Enumeration command | worker must run `git -C .private_reference/source_mirrors/opendatalab__MinerU rev-parse HEAD` and `git -C .private_reference/source_mirrors/opendatalab__MinerU ls-files` before citing mirror facts |
| Manifest artifact or inline manifest | `.private_reference/source_mirrors/INDEX.md` row `opendatalab__MinerU` |
| Processing ledger artifact or inline ledger | `docs/reviews/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_WORKER_RETURN_2026-07-03.md` and `docs/reference/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md` |
| Ledger terminal statuses | READ, SOURCE_VERIFIED, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, SKIPPED_WITH_REASON, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | MSEA-T2/R4/R5/R6/R7/R8/R9 owner surfaces |
| Unresolved items | none expected; worker must block on missing MSEA owner surface or source mirror drift |
| Completion claim boundary | draft contract only; no runtime/provider/public/package/checker/source-import/schema/adapter expansion |

## Corpus Completeness And Report Integrity

- Corpus task class: source-backed adapter contract drafting from accepted MinerU absorption evidence.
- Corpus root: `.private_reference/source_mirrors/opendatalab__MinerU/` plus accepted MSEA governed artifacts.
- Snapshot time: 2026-07-03 dispatch authoring session.
- Enumeration command: `rg --files --hidden --no-ignore .private_reference/source_mirrors/opendatalab__MinerU -g '!**/.git/**'` returned `425` files; `git -C .private_reference/source_mirrors/opendatalab__MinerU rev-parse HEAD` returned `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`.
- Manifest artifact or inline manifest: `.private_reference/source_mirrors/INDEX.md` plus MSEA-R8 residual closure ledger.
- Manifest hash: source mirror commit `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`.
- Processing ledger artifact or inline ledger: planned worker return and R10 reference draft.
- Allowed terminal statuses: READ, SOURCE_VERIFIED, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, SKIPPED_WITH_REASON, BLOCKED_UNREADABLE, BLOCKED_WITH_REASON.
- ledger_terminal=READ for accepted MSEA owner surfaces; ledger_terminal=SOURCE_VERIFIED for source mirror commit/count; ledger_terminal=ADAPTED for R10 contract drafting; ledger_terminal=DEFERRED for held runtime/provider/RAG/S3/Docker/checker routes; ledger_terminal=REJECTED for direct upstream import; ledger_terminal=NO_NEW_VALUE for already-owned evidence.
- Reconciliation: manifest=425 source-mirror files; ledger_terminal=READ/SOURCE_VERIFIED/ADAPTED/DEFERRED/REJECTED/NO_NEW_VALUE/SKIPPED_WITH_REASON/BLOCKED_UNREADABLE for cited artifacts; exclusions=0 expected; unresolved=0 expected.
- Unresolved files: 0 expected for dispatch authoring; worker must block if an owner surface is missing or mirror drift appears.
- Declared exclusions: no new source files are excluded by dispatch; worker must not claim a new full-file corpus pass.
- Unreadable or unsupported files: none known at dispatch time; binary/content limits remain owned by MSEA-R8.
- Aggregation check: PASS: R10 uses accepted MSEA owner surfaces and source mirror index rather than directly importing upstream source.
- Drift check: PASS at dispatch: mirror commit/count match `.private_reference/source_mirrors/INDEX.md`.
- Output traceability: planned worker return and reference must trace contract sections to MSEA owner surfaces or source mirror facts.
- Adversarial verification: contract draft must distinguish docs-only contract vocabulary from runtime readiness, schema implementation, adapter implementation, document truth, extraction accuracy, and production readiness.
- Corpus verdict: PARTIAL

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| MSEA-R7 receipt artifact and field vocabulary | source-backed receipt families and field-family prose | DOCTRINE_ADAPTED | MSEA-R10 adapter contract draft | map receipt vocabulary into adapter contract sections | no schema implementation or receipt writer |
| MSEA-R9 blueprint/readiness route | accepted docs-only adapter contract route | DOCTRINE_ADAPTED | MSEA-R10 adapter contract draft | draft route-binding and non-claim sections | no adapter implementation |
| R4/R5/R8 runtime/provider/S3/Docker/RAG evidence | held candidate surfaces and concrete reopen conditions | RUNTIME_CANDIDATE | MSEA-R10 hold-condition section | preserve holds, do not execute | no install, model download, parser run, provider call, S3, Docker, RAG write, or package activation |
| R4/R8 Docker and deployment evidence | held deployment recipes and package-lane preconditions | PACKAGE_CANDIDATE | MSEA-R10 hold-condition section | preserve package/deployment hold conditions only | no Docker build/run or package activation |
| MSEA-T3/R6 checker candidate evidence | possible overclaim guard remains condition-gated | CHECKER_CANDIDATE | MSEA-R10 non-claim and future-checker note only | preserve no-checker-now unless repeated misses appear | no checker implementation or hook wiring |
| Direct MinerU upstream code | source mirror remains advisory input only | REJECT_DIRECT_IMPORT | MSEA source mirror control | reject direct copy/import; adapt CVF-native doctrine only | no direct import |
| Already-owned evidence | prior MSEA artifacts already own route and receipt facts | NO_PACKAGE_OR_RUNTIME_VALUE | prior MSEA owner surfaces | cite owner surfaces rather than duplicate full scans | no runtime or package behavior |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| Receipt artifact and field vocabulary | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md`; `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` | ENRICH_EXISTING | R10 turns vocabulary into adapter-contract obligations and non-claims | adapt into R10 reference |
| Application route readiness | `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md`; `docs/reference/CVF_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_2026-07-02.md` | ENRICH_EXISTING | R10 binds route readiness to adapter contract sections | adapt into R10 reference |
| Runtime/provider/S3/Docker/RAG candidates | `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md`; `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md`; `docs/reference/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md` | CONFIRMED_EXISTING | R10 preserves hold conditions rather than reopening execution | defer |
| Direct upstream implementation | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md`; `.private_reference/source_mirrors/INDEX.md` | REJECT_DIRECT_IMPORT | no direct code import remains allowed | reject import |
| Checker route | `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md`; `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md`; `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0023.md` | CONFIRMED_EXISTING | output-shape read-ahead required; no new checker implementation authorized | require worker read-ahead only |

## Source Mirror Migration Control

| Field | Disposition |
|---|---|
| Legacy source path | Legacy MinerU adapter folder remains secondary historical material only |
| Source mirror path | `.private_reference/source_mirrors/opendatalab__MinerU/` |
| Mirror index row | `.private_reference/source_mirrors/INDEX.md` row `opendatalab__MinerU` |
| Pinned upstream commit | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` |
| Migration disposition | MIGRATED_TO_SOURCE_MIRROR |
| Legacy cleanup disposition | LEGACY_REFERENCE_ONLY_WITH_REASON: historical comparison only; source facts must prefer pinned mirror or governed MSEA artifacts |
| Claim boundary | source-mirror authority control only; no runtime, install, package activation, provider/live proof, public-sync, checker implementation, source import, schema implementation, adapter implementation, or production-readiness claim |

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| storageClass | governed documentation/reference artifact |
| foundationSurface | MSEA MinerU absorption owner surfaces under `docs/reference` and worker-return review surface under `docs/reviews` |
| plannedPaths | `docs/reviews/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_WORKER_RETURN_2026-07-03.md`; `docs/reference/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md` |
| generatedAggregateImpact | NONE: worker must not edit generated session state or corpus registry aggregates |
| relocationOrSplit | N/A_WITH_REASON: no existing durable governance foundation file is relocated, split, or refactored |
| claimBoundary | storage-layout accounting only; no runtime/provider/live/public/package/checker/schema/adapter implementation claim |

## Mandatory Blind-Spot Control Block

| Field | Value |
|---|---|
| disposition | NOT_APPLICABLE_WITH_REASON |
| reason | MSEA-R10 is not a new full source absorption pass; it drafts a contract from accepted MSEA owner surfaces and recomputed source mirror commit/count |
| coverageBasis | MSEA-R8 residual ledger remains the corpus closure owner for 425/425 source mirror accounting |
| workerRequirement | worker must not silently claim full source coverage; any new source-depth gap must be recorded as `BLOCKED_WITH_REASON` or a declared limitation |
| claimBoundary | blind-spot control only; no source import, runtime execution, package activation, checker implementation, schema implementation, adapter implementation, or production claim |

## Legacy Absorption Coverage Index Disposition

| Field | Value |
|---|---|
| disposition | NOT_APPLICABLE_WITH_REASON |
| coverageIndexEvidence | MSEA-R10 cites accepted MSEA owner surfaces and the source mirror index; it does not reopen the legacy external repo clone as an authority source |
| legacyPath | `.private_reference/legacy/CVF 28.06/CVF_MinerU_Structured_Extraction_Adapter/` remains secondary historical material only |
| sourceMirrorPreferred | `.private_reference/source_mirrors/opendatalab__MinerU/` |
| claimBoundary | no legacy-source import, no runtime execution, no package activation, no checker implementation |

## Adapter Contract Draft Requirements

The companion reference must be a draft contract, not a route-selection packet.
It should include at minimum:

| Contract section | Required source basis | Required boundary |
|---|---|---|
| Scope and non-applicability | MSEA-R9 `## Scope / Applies To`; active next move | explicitly excludes runtime, schema implementation, receipt writer, adapter implementation |
| Source authority | MSEA-T2/R4/R5/R6/R7/R8/R9 and source mirror index | source mirror is advisory input, not imported source |
| Receipt family obligations | MSEA-R7 receipt artifact family map | no JSON schema implementation |
| Field-family obligations | MSEA-R7 field family map | no document-truth or extraction-accuracy claim |
| Backend variant boundary | MSEA-R7 backend variant boundary; R4/R5/R8 runtime candidates | no runtime/backend execution |
| Application route bindings | MSEA-R9 application blueprint layers | no automatic invocation or RAG write |
| Held lanes and reopen conditions | MSEA-R4/R5/R8 and R9 hold conditions | fresh GC-018 required for runtime/provider/S3/RAG/Docker/checker routes |
| Claim boundary and public export disposition | Delta claim-boundary checkers and public export standard | private provenance only |

## Rescan Intelligence Hardening

- Original source artifact: `https://github.com/opendatalab/MinerU.git` at `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`, mirrored at `.private_reference/source_mirrors/opendatalab__MinerU/`
- Predecessor intake artifact: `docs/reference/CVF_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_2026-07-02.md`
- Delta ledger status: REQUIRED
- Routing matrix status: REQUIRED
- Semantic sampling status: REQUIRED
- Rescan intelligence verdict: PARTIAL

### Original-Intake Delta Ledger

| Prior intake claim | R10 treatment | Delta category | Evidence |
|---|---|---|---|
| MSEA-R8 closed residual repository accounting | reuse accepted corpus closure rather than reopen full scan | UNCHANGED_FROM_INTAKE | MSEA-R8 residual ledger |
| R9 selected docs-only adapter contract route | convert into actual draft reference | CHANGED_DISPOSITION | MSEA-R9 worker return and reference |
| R7 receipt vocabulary exists | adapt into contract obligations | CHANGED_DISPOSITION | MSEA-R7 reference |
| Adapter contract draft does not yet exist as an owner surface | create new docs/reference contract draft | NEW_FINDING | planned R10 reference |
| Runtime/provider/S3/RAG/Docker/checker routes remain held | preserve as held lanes | REMOVED_OR_REJECTED | R4/R5/R8/R9 boundaries |

### Follow-Up Routing Matrix

| Route lane | R10 handling | Boundary |
|---|---|---|
| DO_NOW | create worker return and companion adapter contract draft reference only | docs/reference work only |
| RESOLVED_BY_DESIGN | no runtime route is needed to complete a docs-only contract draft | no runtime proof |
| SEPARATE_RUNTIME_TRANCHE | runtime/provider/RAG/S3/Docker/package/checker routes remain held | fresh GC-018 and live/provider proof if behavior is claimed |
| STRATEGIC_OPERATOR_DECISION | operator may later choose a concrete runtime/product route | outside R10 docs-only contract draft |
| OUT_OF_SCOPE | install, execution, provider call, source import, public-sync, checker implementation | forbidden in this work order |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| R10-S1 | MSEA-R7 receipt family map | receipt artifacts inform contract sections | ENRICH_EXISTING | artifact existence is not schema implementation | worker must verify |
| R10-S2 | MSEA-R9 route decision | adapter contract draft is valuable | ENRICH_EXISTING | route decision must not imply adapter implementation | worker must verify |
| R10-S3 | R4/R5/R8 held candidates | runtime/package/provider lanes remain demand-gated | CONFIRMED_EXISTING | contract must not reopen execution | worker must verify |

## Execution Plan

| Step | Action | Output | Stop condition |
|---|---|---|---|
| 1 | Capture `executionBaseHead`, `git status --short`, mirror commit, and mirror file count | worker return evidence | block on dirty/unexpected state or mirror drift |
| 2 | Read required first reads and checker sources by output artifact | checker read-ahead block | block if required source is missing |
| 3 | Create worker return scaffold and run fast gate while short | worker return skeleton | repair shape before long prose |
| 4 | Draft companion adapter contract reference | R10 reference | block if contract needs runtime/schema/adapter implementation |
| 5 | Fill worker return with evidence, gates, no-commit statement, and claim boundary | COMPLETE_PENDING_REVIEW or BLOCKED_WITH_REASON | block on unrepaired gate failure |

## Verification Commands

```powershell
git rev-parse --short HEAD
git status --short
git -C .private_reference/source_mirrors/opendatalab__MinerU rev-parse HEAD
git -C .private_reference/source_mirrors/opendatalab__MinerU ls-files
python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_WORKER_RETURN_2026-07-03.md --title "CVF MSEA-R10 MinerU Adapter Contract Draft Worker Return"
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_governed_artifact_checker_read_ahead.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_external_knowledge_intake_routing.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_external_absorption_core.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_external_absorption_value_conversion.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_external_absorption_overlap_discipline.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_source_mirror_migration.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_corpus_completeness_report_integrity.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_rescan_intelligence_hardening.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
git diff --name-status
git status --short
```

Individual checker substitution for the final worker-return fast gate is
forbidden.

## Evidence Requirements

| Evidence | Required form |
|---|---|
| Base evidence | `executionBaseHead`, `git status --short`, source mirror commit, mirror enumeration |
| Source evidence | cited MSEA artifacts or source mirror paths for every contract section |
| Gate evidence | worker-return fast gate plus listed external absorption, corpus, and rescan gates |
| Boundary evidence | no-commit statement, changed-file manifest, and explicit forbidden-scope claim boundary |

## Acceptance Criteria

| Criterion | Required evidence |
|---|---|
| Two output artifacts only | `git diff --name-status` and `git status --short` show only planned worker return and companion reference as pending worker changes |
| Source mirror reconfirmed | worker return records mirror commit and 425-file count or stops on drift |
| Adapter contract is source-backed | companion reference maps every contract section to MSEA owner surfaces or source mirror facts |
| Contract remains documentation/reference-only | no schema implementation, receipt-writer code, adapter implementation, runtime/provider/S3/RAG/Docker/checker claim |
| Held lanes remain held | reference names concrete reopen conditions for runtime/provider/S3/RAG/Docker/package/checker lanes |
| Worker output checker-shape plan executed | worker return records output-artifact checker read-ahead and fast-gate evidence |
| WORKER_MUST_NOT_COMMIT honored | worker return records HEAD unchanged and no commit/stage/push by worker |

Fail conditions:

| Condition | Required response |
|---|---|
| Mirror commit or count drifts from source mirror index | `BLOCKED_WITH_REASON` and no contract conclusion from stale source facts |
| Worker needs runtime execution, live/provider proof, credentials, source import, checker implementation, schema implementation, adapter implementation, or public-sync | `BLOCKED_WITH_REASON`; do not execute |
| Any output artifact lacks checker-required headings/tokens | repair inside allowed scope and rerun gate |
| Worker creates extra artifacts outside planned paths | stop and return for reviewer/orchestrator decision |

## Review Gate

Worker handoff is not closure. Reviewer/closer must inspect the two pending
artifacts, repair only allowed-scope evidence defects, run reviewer-return
preflight, commit material artifacts if accepted, and only then perform
session-sync in a separate commit if mode or next move changes.

## Closure Checklist

| Item | Closure owner |
|---|---|
| Worker artifacts are pending and uncommitted | worker records evidence |
| Reviewer validates artifacts and gates | reviewer/closer |
| Material commit is created only if accepted | reviewer/closer |
| Session-sync is separate if mode or next move changes | session-sync steward |

## Return-To-Orchestrator Conditions

Return without continuing if source mirror drift appears, a required MSEA
artifact is missing, the contract draft requires forbidden runtime/provider/
public/package/checker/schema/adapter implementation work, a gate cannot be
repaired inside allowed scope, or the worker needs to create paths outside Write
Ownership.

## Operator Checkpoint

Operator approval is required before any runtime/provider/live proof,
credential/S3 use, MinerU install/model download/execution, source import,
public-sync, package activation, checker implementation, schema implementation,
receipt-writer code, adapter implementation, Web/MCP/model-router work,
action-authority work, benchmark, document-truth claim, extraction-accuracy
claim, or production-readiness claim.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher role |
| Provider or surface | local workspace |
| Session or invocation | MSEA-R10 dispatch authoring, 2026-07-03 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell; `rg`; source reads; scaffold helper; `apply_patch`; governance gates |
| Target paths | this work order; paired GC-018 baseline |
| Allowed scope source | active next move from MSEA-R9 accepted material commit `2a58322b` and operator instruction to handle MSEA-R10 |
| Before status evidence | clean worktree at HEAD `7c19b587` before authoring |
| After status evidence | dispatch artifacts pending pre-dispatch gates and material commit |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | documentation/reference-only MSEA-R10 dispatch |
| Claim boundary | dispatch authoring only; no worker execution or runtime/provider/public/package/checker/source-import/schema/adapter claim |
| Agent type | dispatcher |
| Invocation ID | `msea-r10-dispatch-authoring-2026-07-03` |
| Expected manifest | paired GC-018 baseline and this work order |
| Actual changed set | paired GC-018 baseline and this work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in this dispatch batch |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | MSEA-R10 work order for documentation/reference MinerU adapter contract draft |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, provider, parser, adapter, schema, receipt-writer, or production behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed |
| invocationBoundary | local governed document authoring and future worker document synthesis only |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | work order authorizes pending worker documentation/reference artifacts only |
| forbiddenExpansion | no MinerU runtime, install, model download, parser/OCR/VLM/hybrid/API/router/Gradio/Docker execution, provider/live call, credentials/S3, RAG write, source import, package activation, checker implementation, public-sync, Web/MCP/model-router/action-authority, automatic invocation, benchmark, document-truth, extraction-accuracy, schema implementation, receipt-writer code, adapter implementation, or production-readiness claim |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R10 --title "MinerU Adapter Contract Draft" --date 2026-07-03 --base 7c19b587 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "MSEA-R9 accepted at material commit 2a58322b; route OPEN_ADAPTER_CONTRACT_DRAFT_ONLY selected for documentation/reference-only adapter contract draft" --include-worker-return-skeleton --stdout` |
| generatedProfile | packet-kind=generic-worker-dispatch; commit-mode=WORKER_MUST_NOT_COMMIT; worker-return skeleton requested |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced scaffold placeholders with MSEA-R10 adapter-contract scope, source verification, external absorption blocks, worker-output checker-shape plan, contract draft requirements, and no-runtime claim boundary |
| checkerReadAheadConfirmation | read guard orientation, literal-format gotchas, worker-return quality gate, work-order dispatch quality checker, R9 dispatch pattern, MSEA owner surfaces, source mirror anchors, and applicable checker source paths before writing |
| docOnlyNewFields | adapterContractSection; receiptFamilyMapping; applicationRouteBinding; nonRuntimeHoldCondition |
| claimBoundary | scaffold provenance supports dispatch authoring only; no worker completion, runtime/provider/live/public/package/Web/MCP/model-router/action-authority, checker, schema, adapter implementation, or production claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order. No public-sync artifact is created or
modified by this tranche.

## Claim Boundary

This work order authorizes only MSEA-R10 worker execution under
`WORKER_MUST_NOT_COMMIT` to create one worker return and one companion reference
draft. It does not authorize worker commits, source import, runtime execution,
provider/live proof, credential use, public-sync, package activation, checker
implementation, schema implementation, receipt-writer code, adapter
implementation, Web/MCP/model-router work, action authority, automatic
invocation, benchmark, document-truth, extraction-accuracy, or
production-readiness claims.
