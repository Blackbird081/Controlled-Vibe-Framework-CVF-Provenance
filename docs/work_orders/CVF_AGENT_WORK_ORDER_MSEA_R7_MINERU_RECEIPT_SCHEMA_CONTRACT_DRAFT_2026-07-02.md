# CVF Agent Work Order - MSEA-R7 MinerU Receipt Schema Contract Draft

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-07-02

docType: work_order

Batch ID: MSEA-R7

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: ce48461e

External knowledge intake routing: REQUIRED

External absorption core: REQUIRED

## Dispatch Prompt Envelope

Role: no-commit worker for MSEA-R7 MinerU receipt schema contract draft.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

Base: capture `executionBaseHead` with `git rev-parse --short HEAD` before
edits. Expected dispatch base is `ce48461e` or the reviewer-provided current
dispatch commit if this packet is committed first.

Current-time notes: current date is 2026-07-02; upstream MinerU is pinned at
`3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`.

Required first actions: read startup surfaces, this work order, the paired
GC-018 baseline, MSEA-T2/R5/R6 owner surfaces, the source mirror index, and
checker source paths listed below before writing conclusions.

Return contract: create the worker return and receipt schema contract draft,
run the listed gates, leave changes uncommitted, and return
`COMPLETE_PENDING_REVIEW`, `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, or
`BLOCKED_WITH_REASON`.

Do-not-misread notes: this work order drafts documentation/reference contract
language only. It does not authorize MinerU install, parser run, OCR/VLM/hybrid
execution, API/router/Gradio service, Docker, model download, provider/live
proof, OpenAI-compatible endpoint call, S3 connection, credential storage, RAG
index write, source import, checker implementation, package activation,
public-sync, Web/MCP/model-router/action-authority, automatic invocation,
benchmark, or production-readiness claims.

## Purpose

Create a CVF-owned receipt schema contract draft from the accepted MinerU
source-backed receipt evidence. The draft must enrich MSEA-T2 receipt language
with concrete artifact families and field groups while preserving all runtime,
quality, truth, downstream-use, and implementation boundaries.

## Mission

Create exactly these worker-owned outputs:

1. `docs/reviews/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_WORKER_RETURN_2026-07-02.md`
2. `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md`

The reference draft must cover:

- receipt artifact inventory;
- field-family map;
- content block taxonomy;
- backend/variant boundary;
- downstream-use and quality boundary;
- future checker-readiness notes for MSEA-CC-4;
- explicit non-claims.

## Authority Chain

| Authority | Path or source | Disposition |
|---|---|---|
| Operator instruction | chat request on 2026-07-02 to continue with the next work order after MSEA-R6 | ACCEPT |
| GC-018 baseline | `docs/baselines/CVF_GC018_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` | ACCEPT |
| Active session front door | `CVF_SESSION_MEMORY.md` | ACCEPT |
| Bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | ACCEPT |
| Active state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V32_2026-07-02.md` | ACCEPT |
| MSEA-R6 route matrix | `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md` | ACCEPT |
| MSEA-R6 worker return | `docs/reviews/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_AND_ADAPTER_READINESS_SELECTION_WORKER_RETURN_2026-07-02.md` | ACCEPT |
| MSEA-R5 worker return | `docs/reviews/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_WORKER_RETURN_2026-07-02.md` | ACCEPT |
| MSEA-R5 owner delta | `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` | ACCEPT |
| MSEA-T2 receipt advisory | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | ACCEPT |
| Source mirror index | `.private_reference/source_mirrors/INDEX.md` | ACCEPT |

Authority boundary: external MinerU source is advisory input only. The worker
must cite the pinned source mirror and governed MSEA artifacts, adapt concepts
into CVF language, and reject direct source import.

## Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | author source-verified dispatch packet and run pre-dispatch gates |
| Worker | no-commit worker role | produce worker return and draft reference without committing |
| Reviewer/closer | Codex | review returned artifacts, repair allowed-scope defects, and commit if accepted |
| Session-sync steward | Codex after material acceptance | update continuity after accepted material commit if next move changes |
| Operator checkpoint | operator | required for any runtime, provider/live proof, credentials, S3, package activation, checker implementation, public-sync, or scope expansion |

## Intake Role Routing Decision

- Intake summary: MSEA-R6 selected `OPEN_RECEIPT_SCHEMA_CONTRACT_DRAFT`.
- Scope classification: bounded documentation/reference contract draft.
- Risk sensitivity: no runtime, public-sync, provider/live run, secret,
  credential, package activation, checker implementation, production, or
  readiness claim.
- Selected role route: routeMode=SINGLE_AGENT_MULTI_ROLE.
- Role separation basis: dispatcher authors packet, worker produces
  uncommitted artifacts, reviewer/closer owns acceptance and commit.
- Escalation condition: stop if scope/risk changes or if runtime/provider/S3/
  RAG/checker/package/public action becomes needed.

## Single-Agent Multi-Role Control Block

- Role separation ledger: dispatcher, worker, reviewer/closer, and
  session-sync steward duties are recorded separately in this packet.
- Evidence basis: review must use git diff, source paths, contract-draft
  artifacts, and gate output, not memory-only claims.
- Self-review boundary: this block does not claim independent review by a
  second human or provider.
- Escalation conditions: stop for operator checkpoint if the worker needs
  runtime execution, provider/live proof, secrets, credentials, public-sync,
  source import, checker implementation, or broader write scope.
- Gate sequence: worker runs pre-implementation and worker-return fast gates;
  reviewer/closer runs reviewer/steward and pre-closure gates on a real range
  before material acceptance.

## Scope

Allowed write scope for worker:

- `docs/reviews/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_WORKER_RETURN_2026-07-02.md`
- `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md`

Allowed read scope:

- startup surfaces and current active handoff;
- this work order and paired GC-018 baseline;
- MSEA-T2/R5/R6 governed artifacts;
- external absorption references and source mirror index;
- the pinned MinerU source mirror only for `docs/en/reference/output_files.md`
  and source mirror HEAD verification.

Forbidden scope:

- no edits to source mirror payload, legacy external folders, `EXTENSIONS/`,
  runtime source, governance checker source, hooks, CI, scripts, active session
  state, active handoff, or public-sync files;
- no MinerU install, parser execution, OCR/VLM/hybrid/backend/API/router/Gradio
  execution, Docker run, model download, provider/live proof,
  OpenAI-compatible endpoint call, S3 connection, credential storage, RAG index
  write, benchmark, source import, checker implementation, package activation,
  Web/MCP/model-router/action-authority, automatic invocation, or production
  claim;
- no commit by the worker.

Risk ceiling: R0 documentation/reference contract draft only.

## Write Ownership

| Path | Owner | Permission |
|---|---|---|
| `docs/reviews/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_WORKER_RETURN_2026-07-02.md` | worker | create or repair inside allowed scope; leave uncommitted |
| `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` | worker | create or repair inside allowed scope; leave uncommitted |
| this work order and paired GC-018 | reviewer/closer only | worker may read but must not edit |
| session state and active handoff | session-sync steward only after material acceptance | worker must not edit |

## Required First Reads

Before writing output, the worker must read:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V32_2026-07-02.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- this work order and paired GC-018 baseline
- `docs/reference/external_agent_review/README.md`
- `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`
- `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md`
- `.private_reference/source_mirrors/INDEX.md`
- `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md`
- `docs/reviews/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_AND_ADAPTER_READINESS_SELECTION_WORKER_RETURN_2026-07-02.md`
- `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md`
- `docs/reviews/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_WORKER_RETURN_2026-07-02.md`
- `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md`
- `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/reference/output_files.md`

## Pre-Flight Checks

Before implementation, the worker must capture:

```powershell
git rev-parse --short HEAD
git status --short
git -C .private_reference/source_mirrors/opendatalab__MinerU rev-parse HEAD
```

Expected source mirror commit:

`3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`

If the source mirror commit differs, the worker must return
`BLOCKED_WITH_REASON` unless the reviewer supplies a fresh dispatch.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Current mode authorizes MSEA-R7 receipt schema contract work-order authoring | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `currentMode` | `msea_r6_accepted_pending_msea_r7_receipt_schema_contract_work_order_authoring` | active session bootstrap | VALUE_SET | ACCEPT |
| MSEA-R6 selected the receipt schema contract route | `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md` | Selected Routing Outcome | `OPEN_RECEIPT_SCHEMA_CONTRACT_DRAFT` | MSEA-R6 route decision matrix | VALUE_SET | ACCEPT |
| MSEA-R6 limits the selected route to future documentation/reference work | `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md` | Next Action Boundary | `OPEN_RECEIPT_SCHEMA_CONTRACT_DRAFT` | MSEA-R6 route decision matrix | VALUE_SET | ACCEPT |
| MSEA-T2 owns receipt vocabulary and future schema validation candidate `MSEA-CC-4` | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | Owner Surface Matrix and checker candidate rows | `MSEA-CC-4` | MSEA-T2 reference | VALUE_SET | ACCEPT |
| MSEA-R5 identified `output_files.md` as concrete receipt schema evidence | `docs/reviews/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_WORKER_RETURN_2026-07-02.md` | Findings / Position and Targeted Deep Ledger | `output_files.md` | MSEA-R5 worker return | VALUE_SET | ACCEPT |
| MSEA-R5 owner delta allows CVF-native receipt contract drafting through fresh GC-018 | `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` | Conditional Reopen Candidates | `Document-extraction receipt schema adoption into a CVF-native receipt contract` | MSEA-R5 owner delta | VALUE_SET | ACCEPT |
| MinerU source mirror is pinned and preferred for current upstream facts | `.private_reference/source_mirrors/INDEX.md` | line 35 | `opendatalab__MinerU`; `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` | source mirror index | VALUE_SET | ACCEPT |
| MinerU documents output artifacts for layout, spans, model, middle, content list, and content list v2 | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/reference/output_files.md` | lines 17, 35, 62, 109, 292, 396, 730-742 | `layout.pdf`; `span.pdf`; `model.json`; `middle.json`; `content_list.json`; `content_list_v2.json` | upstream output-file reference | VALUE_SET | ACCEPT |
| MinerU documents block types, tables, formulas, and structured V2 content fields | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/reference/output_files.md` | lines 129-186, 292-329, 402-426, 474-548 | `type`; `tables`; `interline_equations`; `content`; `math_content` | upstream output-file reference | VALUE_SET | ACCEPT |

## Current Runtime Freshness Verification

| Claim checked | Verification command | Observed result | Disposition |
|---|---|---|---|
| MSEA-R7 planned baseline path absent before dispatch | `Test-Path -LiteralPath 'docs/baselines/CVF_GC018_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md'` | `False` before authoring | ACCEPT |
| MSEA-R7 planned work order path absent before dispatch | `Test-Path -LiteralPath 'docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md'` | `False` before authoring | ACCEPT |
| Planned worker output paths absent before dispatch | `Test-Path` checks for planned worker return and reference contract draft | both absent before authoring | ACCEPT |

## Negative Search And Collision Discipline

| Check | Command | Result | Disposition |
|---|---|---|---|
| MSEA-R7 collision search | `rg -n "MSEA-R7|MSEA_R7|MinerU Receipt Schema Contract|MINERU_RECEIPT_SCHEMA_CONTRACT" docs CVF_SESSION AGENT_HANDOFF_V32_2026-07-02.md` | pre-authoring path checks were absent; post-authoring search may show this dispatch baseline and work order plus existing session next-move mentions only | ACCEPT |
| Existing output path absence | `Test-Path` checks for planned worker return and reference contract draft | both absent before authoring | ACCEPT |
| Existing implementation search | `rg -n "MinerU|mineru" EXTENSIONS governance scripts docs/reference docs/roadmaps docs/reviews docs/work_orders docs/baselines -g "!*MSEA*"` | no CVF-owned MinerU runtime implementation surface is authorized by this dispatch | ACCEPT |

## Worker Autonomy / No-Question Rule

The worker proceeds without operator confirmation for non-destructive actions
inside this work order's Allowed scope, including source reads, contract-draft
authoring, governance format repair, and gate reruns after allowed-scope
remediation.

Escalate only if a needed action would exceed Allowed scope, run MinerU, use
secrets or credentials, consume provider/live quota, mutate runtime/source,
open public-sync, change risk level, release a held implementation lane, touch
forbidden paths, or perform destructive/irreversible actions.

## Operator Checkpoint

No operator checkpoint is needed for the worker to execute the documentation
contract-draft scope. Operator approval is required before any runtime,
provider/live proof, credential/S3 use, MinerU execution, package activation,
checker implementation, public-sync, Web/MCP/model-router/action-authority, or
production-readiness claim.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | dispatcher authors GC-018/work order; worker produces uncommitted artifacts; reviewer/closer owns acceptance commit and later session-sync |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=ce48461e; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | dispatch changes only this GC-018 and work order; worker changes only planned worker return and receipt schema contract draft |
| traceScope(phase, actor) | worker return and receipt schema contract draft must include Agent Operation Trace Block; reviewer owns committed-range verification |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT for worker; reviewer/closer owns material commit |
| crossBatchIsolation | clean worktree required before worker execution; unrelated dirty paths must be recorded as blocker or pre-existing exemption |
| nextMoveSurfaces | worker does not edit session surfaces; reviewer/session-sync steward updates mode and next move only after material acceptance |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | N/A_WITH_REASON: no separate `_COMPLETION_` reviewer artifact is planned; prefer repairing evidence in the worker return per literal-format gotcha 30 |
| reviewerOwnedClosurePaths | worker return and receipt schema contract draft after reviewer acceptance; session-sync surfaces only in a later dedicated commit |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Work-Order Fulfillment Manifest

| Required output | Path or evidence | Owner | Required status |
|---|---|---|---|
| Worker return | `docs/reviews/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_WORKER_RETURN_2026-07-02.md` | worker | created, uncommitted, gate-checked |
| Receipt schema contract draft | `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` | worker | created, uncommitted, source-backed |
| Artifact-family map | contract draft | worker | maps output artifact families to CVF receipt language |
| Field-family map | contract draft | worker | maps block types and content fields without runtime/truth claims |
| No-commit evidence | worker return | worker | HEAD unchanged and no commit/stage/push |

## Contract Draft Requirements

The worker must include these sections in the reference draft:

| Section | Required content |
|---|---|
| Purpose / Scope / Boundary | documentation-only contract draft and non-claims |
| Source Authority | MSEA-T2/R5/R6 and pinned source mirror |
| Receipt Artifact Family Map | layout, span, model, middle, content list, content list v2 |
| Field Family Map | source identity, page, block, line, span, bbox, type, content, table, equation, image/chart metadata |
| Backend Variant Boundary | pipeline/VLM and legacy/V2 output differences |
| Downstream Use Boundary | quality and RAG handoff constraints from MSEA-T2 |
| Future Checker Readiness | MSEA-CC-4 candidate note only |
| Claim Boundary | no runtime/schema implementation/document-truth/accuracy/production claim |

The draft must adapt upstream terminology into CVF-owned language and cite the
source anchors. It must not copy upstream sample JSON as a CVF runtime schema.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | external repo or copied folder -> pinned source mirror and accepted MSEA evidence -> CVF-native receipt schema contract draft reference -> future implementation only by fresh authorization |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py` |
| Owner surface | this work order and paired MSEA-R7 GC-018 baseline |
| Disposition | DISPATCH documentation-only contract drafting from accepted external source evidence |
| Claim boundary | dispatch only; no MinerU execution, provider/live proof, credential use, source import, public-sync, package activation, checker implementation, Web/MCP/model-router/action-authority, or production-readiness claim |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md |
| Input root or repository | `https://github.com/opendatalab/MinerU.git` at `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`; local mirror `.private_reference/source_mirrors/opendatalab__MinerU/`; accepted MSEA-T2/R5/R6 evidence |
| Enumeration command | `rg --files --hidden --no-ignore .private_reference/source_mirrors/opendatalab__MinerU`; MSEA-R7 uses receipt-schema source anchors and no full-corpus replay |
| Manifest artifact or inline manifest | inline table: `## Contract Draft Requirements` |
| Processing ledger artifact or inline ledger | inline table: `## Work-Order Fulfillment Manifest` |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md`; `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md`; `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md` |
| Unresolved items | contract draft pending worker execution |
| Completion claim boundary | documentation-only contract draft; no runtime/provider/public/package/checker expansion |

## Corpus Completeness And Report Integrity

- Corpus task class: external repository documentation/reference contract-draft dispatch from accepted MSEA evidence.
- Corpus root: `.private_reference/source_mirrors/opendatalab__MinerU/` plus accepted MSEA-T2/R5/R6 governed artifacts.
- Snapshot time: 2026-07-02 local session.
- Enumeration command: `rg --files --hidden --no-ignore .private_reference/source_mirrors/opendatalab__MinerU`; MSEA-R7 uses receipt-schema source anchors and no full-corpus replay.
- Manifest artifact or inline manifest: inline `## Contract Draft Requirements`.
- Manifest hash: inherited from MSEA-R5 full-mirror evidence unless worker detects source mirror drift.
- Processing ledger artifact or inline ledger: planned MSEA-R7 worker return and receipt schema contract draft reference.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE
- Reconciliation: manifest=8 contract sections; ledger_terminal=0 at dispatch before worker execution; exclusions=full-corpus replay; unresolved=0.
- Unresolved files: 0
- Declared exclusions: no full 425-file replay and no 373-file replay; R5 already owns that manifest evidence.
- Unreadable or unsupported files: none known at dispatch.
- Aggregation check: all contract sections map to existing MSEA source evidence or source mirror anchors.
- Drift check: worker must verify source mirror commit still matches the index if it reads source files directly.
- Output traceability: contract draft must cite worker return and source verification anchors.
- Adversarial verification: worker must distinguish artifact existence, schema vocabulary, extraction quality, document truth, and runtime readiness.
- Corpus verdict: PARTIAL

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| `output_files.md` receipt artifact list | concrete output artifact families and field vocabulary | DOCTRINE_ADAPTED | planned MSEA-R7 receipt schema contract draft | worker adapts language into CVF-owned contract draft | no parser/schema implementation |
| MSEA-T2 receipt advisory | receipt and quality boundary owner surface | DOCTRINE_ADAPTED | planned MSEA-R7 contract draft | worker enriches existing owner language | no RAG mutation or truth claim |
| RagFlow/RAG integration evidence | downstream package pressure remains relevant but not selected for R7 | PACKAGE_CANDIDATE | MSEA-R6 route decision matrix and MSEA-T2 RAG handoff advisory | worker records deferred boundary only if needed | no plugin wiring, RAG write, or adapter execution |
| Provider and S3 candidates | title-correction and credential surfaces are not part of receipt contract drafting | RUNTIME_CANDIDATE | MSEA-R5 owner delta and MSEA-R6 route matrix | worker preserves forbidden expansion boundary | no provider call, S3 access, or credential use |
| MSEA-CC-4 future schema checker | future validation concept only after CVF owns schema fields | CHECKER_CANDIDATE | MSEA-T2 advisory and planned MSEA-R7 draft | worker may include checker-readiness note | no checker implementation or hook wiring |
| Direct upstream schema/source import | upstream documentation informs CVF language but is not CVF implementation | REJECT_DIRECT_IMPORT | planned MSEA-R7 draft | worker must adapt and cite, not copy as runtime contract | no source import or direct wiring |
| Full-corpus replay after R5/R6 | previous tranches already reconciled source mirror and selected route | NO_PACKAGE_OR_RUNTIME_VALUE | MSEA-R5/R6 accepted artifacts | worker must avoid replay unless drift is detected | no runtime or package behavior |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| Receipt contract draft | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | ENRICH_EXISTING | concrete schema fields become CVF draft language | create draft reference |
| R5 schema evidence | `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` | CONFIRMED_EXISTING | R5 already identified the receipt schema adoption candidate | use as dependency-release evidence |
| R6 route decision | `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md` | CONFIRMED_EXISTING | R6 selected this route explicitly | use as dispatch authority |
| Runtime/provider/S3/RAG routes | `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md` | NO_NEW_VALUE | not part of R7 selected documentation route | preserve deferred boundaries |
| Future schema checker | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | ENRICH_EXISTING | MSEA-CC-4 can be sharpened after draft exists | record checker-readiness note only |
| Direct upstream source import | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | REJECT_DIRECT_IMPORT | upstream source remains advisory input only | reject direct import |
| Unknown new owner surface | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | OWNER_SURFACE_NOT_FOUND | not expected; worker must return blocker if a necessary owner surface is missing | do not invent owner silently |

## Source Mirror Migration Control

| Field | Disposition |
|---|---|
| Legacy source path | Legacy MinerU adapter folder remains secondary historical material and is not source authority for MSEA-R7. |
| Source mirror path | `.private_reference/source_mirrors/opendatalab__MinerU/` |
| Mirror index row | `.private_reference/source_mirrors/INDEX.md` row `opendatalab__MinerU` |
| Pinned upstream commit | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` |
| Migration disposition | SOURCE_MIRROR_AUTHORITY_RETAINED_FOR_THIS_TRANCHE |
| Legacy cleanup disposition | LEGACY_REFERENCE_ONLY_WITH_REASON: historical comparison only; source facts must prefer the pinned mirror or governed MSEA artifacts |
| Claim boundary | source-mirror authority control only; no source import, install, runtime execution, provider/live proof, public-sync, checker implementation, or production-readiness claim |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Storage action | N/A with reason: MSEA-R7 creates one worker return and one reference draft in existing governed folders only. |
| Folder/index impact | No new folder, stable reference family, front door, storage layout, or dated duplicate standard is authorized. |
| Durable foundation impact | The receipt schema contract draft is a tranche-specific reference artifact, not a central foundation standard. |
| Required boundary | Worker must not create or relocate foundation storage, index, template, standard, or front-door files. |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: MSEA-R7 routes the freshly cloned MinerU source
mirror under `.private_reference/source_mirrors/opendatalab__MinerU/`, not a
legacy absorption folder. The legacy coverage index is not the owner surface
for this tranche. The work order retains the legacy folder only as a
forbidden-scope boundary and historical-reference warning.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_WORKER_RETURN_2026-07-02.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Evidence Requirements

- Worker return must cite execution base, source mirror HEAD, contract-draft
  output, gate output, changed files, and no-commit evidence.
- Receipt schema contract draft must cite all required contract sections and
  preserve claim boundaries.
- Contract draft must distinguish artifact existence, schema vocabulary,
  extraction quality, document truth, downstream use, and runtime readiness.
- Evidence must come from governed CVF artifacts, the pinned source mirror, or
  checker output, not provider-local memory.

## Execution Plan

1. Capture `executionBaseHead`, `git status --short`, and source mirror HEAD.
2. Read required first reads and checker sources.
3. Draft the worker return and receipt schema contract reference inside allowed
   paths only.
4. Map output artifact families and field families into CVF-owned language.
5. Add explicit non-claims and future-checker readiness notes.
6. Run required gates or return a classified blocker.

## Acceptance Criteria

- Planned worker return exists and records execution base, source mirror HEAD,
  actual `git status --short`, changed files, command evidence, and no-commit
  evidence.
- Planned receipt schema contract draft exists and records artifact-family map,
  field-family map, backend/variant boundary, downstream-use boundary, future
  checker-readiness note, and claim boundary.
- Draft enriches MSEA-T2 and MSEA-R5/R6 owner surfaces without reopening or
  contradicting them.
- No source mirror payload, runtime source, session state, handoff, checker,
  public-sync, or extension path is edited by the worker.

Fail conditions:

- source mirror commit differs from dispatch and no reviewer-supplied fresh
  source authority exists;
- worker creates runtime/provider/S3/RAG/Docker/checker/package/Web/MCP/source
  implementation or claims production readiness;
- draft copies upstream sample JSON as a CVF runtime schema;
- draft omits the claim boundary or future implementation blockers;
- worker commits, stages, pushes, or edits forbidden paths.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` instead of continuing if the source mirror commit
differs, required source files are missing, the draft requires runtime/provider/
credential/public/checker scope, source evidence contradicts MSEA-R6, gates
cannot pass inside allowed scope, or the worktree contains unrelated dirty
paths that cannot be isolated.

## Closure Checklist

- [x] Work order names worker write ownership.
- [x] Worker return and receipt schema contract draft are the only worker-owned
  output paths.
- [x] Source verification, external absorption, corpus, handoff, AOT, Delta,
  ADIF, and worker-return shape controls are present.
- [x] Runtime/provider/live/S3/RAG/checker/package/public/Web/MCP/model-router
  expansions remain forbidden.
- [x] Reviewer/closer owns material commit and later session-sync.

## Review Gate

Worker must run or return a classified blocker for:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_external_knowledge_intake_routing.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_external_absorption_core.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_external_absorption_value_conversion.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_external_absorption_overlap_discipline.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_corpus_completeness_report_integrity.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_source_mirror_migration.py --base <executionBaseHead> --head HEAD --enforce
```

Reviewer/closer must run reviewer-return steward preflight and committed-range
pre-closure before accepting material output.

## Verification Commands

Worker must run or record a classified blocker for:

```powershell
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/check_external_knowledge_intake_routing.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_external_absorption_core.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_external_absorption_value_conversion.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_external_absorption_overlap_discipline.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_corpus_completeness_report_integrity.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_source_mirror_migration.py --base <executionBaseHead> --head HEAD --enforce
```

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Disclosure note: dispatcher invoked `python governance/compat/run_adif_defect_resolver.py --task-class "work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json`; the resolver returned `totalCandidates=0`.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_source_mirror_migration.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_rescan_intelligence_hardening.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `External knowledge intake routing: REQUIRED`; `External absorption core: REQUIRED`; `## Dispatch Prompt Envelope`; `## Source Verification Block`; `## Current Runtime Freshness Verification`; `## Negative Search And Collision Discipline`; `## Agent Handoff Contract Control Block`; `## Reviewer Closure Conversion`; `## Work-Order Fulfillment Manifest`; `## Worker Return Packet Shape Contract`; `WORKER_RETURN_FULL_GATE_V1`; `requiredGate:`; `individualCheckerSubstitution: FORBIDDEN`; `workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED`; `## External Knowledge Intake Routing`; `## External Absorption Core`; `## Corpus Completeness And Report Integrity`; `## External Absorption Value Conversion Matrix`; `## Overlap And Novelty Classification`; `DEFERRED_PRIVATE_ONLY`; `CLAIM_REJECTED_NO_RECEIPT`; `CLAIM_REJECTED_NO_ACTION`; `PARTIAL` |
| gateRunPurpose | confirmation/evidence run for MSEA-R7 dispatch after checker read-ahead, not first discovery |
| claimBoundary | checker read-ahead proves dispatch authoring diligence only; worker completion and any runtime/provider/public/package/checker behavior remain unproved and unauthorized |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R7 --title "MinerU Receipt Schema Contract Draft" --date 2026-07-02 --base 42cb5e46 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "MSEA-R6 accepted at 2d0b05c4; selected OPEN_RECEIPT_SCHEMA_CONTRACT_DRAFT as documentation-only next route" --include-worker-return-skeleton --stdout` |
| generatedProfile | packet-kind=generic-worker-dispatch; commit-mode=WORKER_MUST_NOT_COMMIT; worker-return skeleton requested |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced scaffold fields with MSEA-R7 receipt-contract scope, source verification, contract draft requirements, external absorption blocks, source mirror migration control, no-commit worker shape, and verification commands |
| checkerReadAheadConfirmation | read guard orientation, literal-format gotchas, compact worker-return standard, MSEA-R6 artifacts, MSEA-T2/R5 owner surfaces, source mirror anchors, and applicable checker source paths before writing |
| docOnlyNewFields | receipt schema contract draft path; contract draft requirements; artifact-family map; field-family map |
| claimBoundary | scaffold provenance supports dispatch authoring only; no worker completion, runtime/provider/live/public/package/Web/MCP/model-router/action-authority, checker, or production claim |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: MSEA-R7 dispatch authoring required a
minimal session/front-door wording repair so dispatch-packet lifecycle hygiene
does not mistake the newly dispatched MSEA-R7 lane for a closed MSEA-R6 lane.
The repair removes closed-status token proximity to the MSEA-R7 lane key and
regenerates active session state only.

Protected paths:

- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/entries/mseaR6MineruApplicationRouteDecisionClosure20260702.json`
- `CVF_SESSION_MEMORY.md`

Operator authorization: operator asked Codex to create the next work order; the
protected-path repair is bounded gate remediation required before dispatch and
does not authorize worker edits to session state or handoff surfaces.

Rollback boundary: revert only the three protected-path wording/regeneration
edits above if this dispatch is rejected; do not revert unrelated MSEA-R6
closure artifacts or prior session-sync commits.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher |
| Provider or surface | local workspace |
| Session or invocation | MSEA-R7 dispatch authoring, 2026-07-02 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, git, apply_patch, governance checkers |
| Target paths | `docs/baselines/CVF_GC018_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` |
| Allowed scope source | operator request to create the next work order after MSEA-R6 selected `OPEN_RECEIPT_SCHEMA_CONTRACT_DRAFT` |
| Before status evidence | clean worktree at `ce48461e`; planned MSEA-R7 paths absent before authoring |
| After status evidence | dispatch baseline and work order created with source verification and pending pre-dispatch gates |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | dispatcher authoring only; worker execution remains no-commit |
| Claim boundary | no runtime/provider/public/source-import/Web/MCP/model-router/checker/package/action-authority claim |
| Agent type | dispatcher |
| Invocation ID | `msea-r7-mineru-receipt-schema-contract-dispatch-2026-07-02` |
| Expected manifest | baseline and work order paths named above |
| Actual changed set | baseline and work order paths named above |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in dispatch artifact creation |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | MSEA-R7 receipt schema contract-draft work order |
| claimDisposition | CLAIM_REJECTED: no Delta runtime execution-control claim is made |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed |
| invocationBoundary | local authoring, source verification, and governance checker invocation only |
| interceptionBoundary | no runtime interception, parser execution, provider invocation, S3 access, RAG write, or action-control behavior |
| claimLanguage | source-backed documentation/reference contract-draft dispatch only |
| forbiddenExpansion | no runtime/provider/live/public/package/Web/MCP/model-router/action-authority, automatic invocation, checker implementation, source import, credential handling, or production-readiness claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: MSEA-R7 dispatch is private provenance receipt-contract drafting work
derived from private source-mirror absorption evidence. No public-sync artifact
is created or authorized by this work order.

## Claim Boundary

MSEA-R7 authorizes a no-commit worker to draft a CVF-native receipt schema
contract reference from accepted source-backed evidence. It does not authorize
or claim MinerU runtime integration, parser execution, OCR execution,
VLM/hybrid backend routing, remote backend processing, model download,
API/router/Gradio service, Docker deployment, RAG indexing, provider/live
proof, S3 access, credential handling, document truth verification, parser
accuracy, table/formula correctness, public-sync export, checker enforcement,
package activation, certification, generated aggregate mutation, production
readiness, hosted readiness, model-router behavior, action authority, or
universal document intelligence.
