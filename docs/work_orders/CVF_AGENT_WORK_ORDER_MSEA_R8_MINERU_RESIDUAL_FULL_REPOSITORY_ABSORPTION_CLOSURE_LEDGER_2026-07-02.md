# CVF Agent Work Order - MSEA-R8 MinerU Residual Full Repository Absorption Closure Ledger

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-07-02

docType: work_order

Batch ID: MSEA-R8

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: 825c454d

External knowledge intake routing: REQUIRED

External absorption core: REQUIRED

## Dispatch Prompt Envelope

Role: no-commit worker for MSEA-R8 MinerU residual full-repository absorption
closure ledger.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

Base: capture `executionBaseHead` with `git rev-parse --short HEAD` before
edits. Expected dispatch base is `825c454d` or the reviewer-provided current
dispatch-sync commit if this packet is committed first.

Current-time notes: current date is 2026-07-02; upstream MinerU is pinned at
`3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`.

Required first actions: read startup surfaces, this work order, the paired
GC-018 baseline, accepted MSEA-T0/T2/T3/R4/R5/R6/R7 artifacts, the external
absorption references, the source mirror index, and checker source paths listed
below before writing conclusions.

Return contract: create the worker return and residual absorption ledger
reference, run the listed gates, leave changes uncommitted, and return
`COMPLETE_PENDING_REVIEW`, `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, or
`BLOCKED_WITH_REASON`.

Do-not-misread notes: this work order performs documentation/reference
absorption only. It does not authorize MinerU install, parser run, OCR/VLM/
hybrid execution, API/router/Gradio service, Docker build/run, model download,
provider/live proof, OpenAI-compatible endpoint call, S3 connection, credential
storage, RAG index write, source import, checker implementation, package
activation, public-sync, Web/MCP/model-router/action-authority, automatic
invocation, benchmark, extraction-accuracy, document-truth, or
production-readiness claims.

## Purpose

Close the remaining MinerU source-mirror read-depth gaps left visible by
MSEA-R4 and MSEA-R5. The worker must reconcile the pinned 425-file mirror,
inherit already-accepted coverage where prior MSEA artifacts are sufficient,
and produce a residual ledger for groups not yet read deeply enough, without
activating runtime or implementation lanes.

## Mission

Create exactly these worker-owned outputs:

1. `docs/reviews/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_WORKER_RETURN_2026-07-02.md`
2. `docs/reference/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md`

The residual ledger must cover:

- full 425-file mirror reconciliation against the source mirror index;
- a prior-coverage reconciliation table for MSEA-T0/T2/T3/R4/R5/R6/R7;
- residual group closure for `.github`, root files, root `demo`, `projects`,
  `tests`, `mineru/model/utils`, Docker China hardware variants, and docs
  asset/image/chemical demo binaries;
- source-backed value conversion and overlap/novelty classification;
- explicit non-claims and conditional reopen handling.

## Authority Chain

| Authority | Path or source | Disposition |
|---|---|---|
| Operator instruction | chat request on 2026-07-02 to continue and absorb the remaining MinerU repository deeply | ACCEPT |
| GC-018 baseline | `docs/baselines/CVF_GC018_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md` | ACCEPT |
| Active session front door | `CVF_SESSION_MEMORY.md` | ACCEPT |
| Bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | ACCEPT |
| Active state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V32_2026-07-02.md` | ACCEPT |
| MSEA-R7 receipt schema contract draft | `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` | ACCEPT |
| MSEA-R5 worker return | `docs/reviews/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_WORKER_RETURN_2026-07-02.md` | ACCEPT |
| MSEA-R5 owner delta | `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` | ACCEPT |
| MSEA-R4 owner delta | `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md` | ACCEPT |
| MSEA-T2 receipt/RAG advisory | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | ACCEPT |
| MSEA-T3 checker decision | `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | ACCEPT |
| Conditional reopen index | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md` | ACCEPT |
| Source mirror index | `.private_reference/source_mirrors/INDEX.md` | ACCEPT |

Authority boundary: external MinerU source is advisory input only. The worker
must cite the pinned source mirror and governed MSEA artifacts, adapt concepts
into CVF language, reject direct source import, and keep candidate value parked
behind concrete reopen conditions.

## Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | author source-verified dispatch packet and run pre-dispatch gates |
| Worker | no-commit worker role | produce worker return and residual ledger without committing |
| Reviewer/closer | Codex | review returned artifacts, repair allowed-scope defects, and commit if accepted |
| Session-sync steward | Codex after material acceptance | update continuity after accepted material commit if next move changes |
| Operator checkpoint | operator | required for runtime, provider/live proof, credentials, S3, Docker, package activation, checker implementation, public-sync, or scope expansion |

## Intake Role Routing Decision

- Intake summary: operator requested continued deep absorption of the remaining
  MinerU repository following material commit `074144c9`.
- Scope classification: bounded external repository residual absorption ledger.
- Risk sensitivity: no runtime, public-sync, provider/live run, secret,
  credential, package activation, checker implementation, production, or
  readiness claim.
- Selected role route: routeMode=SINGLE_AGENT_MULTI_ROLE.
- Role separation basis: dispatcher authors packet, worker produces
  uncommitted artifacts, reviewer/closer owns acceptance and commit.
- Escalation condition: stop if scope/risk changes or if runtime/provider/S3/
  RAG/Docker/checker/package/public action becomes needed.

## Single-Agent Multi-Role Control Block

- Role separation ledger: dispatcher, worker, reviewer/closer, and
  session-sync steward duties are recorded separately in this packet.
- Evidence basis: review must use git diff, source paths, residual ledger
  artifacts, and gate output, not memory-only claims.
- Self-review boundary: this block does not claim independent review by a
  second human or provider.
- Escalation conditions: stop for operator checkpoint if the worker needs
  runtime execution, provider/live proof, secrets, credentials, public-sync,
  source import, Docker execution, checker implementation, or broader write
  scope.
- Gate sequence: worker runs pre-implementation and worker-return fast gates;
  reviewer/closer runs reviewer/steward and pre-closure gates on a real range
  before material acceptance.

## Scope

Allowed write scope for worker:

- `docs/reviews/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_WORKER_RETURN_2026-07-02.md`
- `docs/reference/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md`

Allowed read scope:

- startup surfaces and current active handoff;
- this work order and paired GC-018 baseline;
- accepted MSEA-T0/T2/T3/R4/R5/R6/R7 governed artifacts;
- external absorption references, conditional reopen index, and source mirror
  index;
- the pinned MinerU source mirror for read-only file inspection and manifest
  reconciliation.

Forbidden scope:

- no edits to source mirror payload, legacy external folders, `EXTENSIONS/`,
  runtime source, governance checker source, hooks, CI, scripts, active session
  state, active handoff, or public-sync files;
- no MinerU install, parser execution, OCR/VLM/hybrid/backend/API/router/Gradio
  execution, Docker build/run, model download, provider/live proof,
  OpenAI-compatible endpoint call, S3 connection, credential storage, RAG index
  write, benchmark, source import, checker implementation, package activation,
  Web/MCP/model-router/action-authority, automatic invocation, document-truth,
  extraction-accuracy, or production claim;
- no commit, staging, push, or public export by the worker.

Risk ceiling: R0 documentation/reference residual absorption ledger only.

## Write Ownership

| Path | Owner | Permission |
|---|---|---|
| `docs/reviews/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_WORKER_RETURN_2026-07-02.md` | worker | create or repair inside allowed scope; leave uncommitted |
| `docs/reference/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md` | worker | create or repair inside allowed scope; leave uncommitted |
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
- `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md`
- `.private_reference/source_mirrors/INDEX.md`
- `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md`
- `docs/reviews/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_WORKER_RETURN_2026-07-02.md`
- `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md`
- `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md`
- `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md`
- `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md`
- `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md`

## Pre-Flight Checks

Before implementation, the worker must capture:

```powershell
git rev-parse --short HEAD
git status --short
git -C .private_reference/source_mirrors/opendatalab__MinerU rev-parse HEAD
rg --files --hidden --no-ignore .private_reference/source_mirrors/opendatalab__MinerU -g '!**/.git/**'
```

Expected source mirror commit:

`3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`

Expected full mirror count: `425`.

If the source mirror commit or full count differs, the worker must return
`BLOCKED_WITH_REASON` unless the reviewer supplies a fresh dispatch.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Current mode permits operator lane selection following MSEA-R7 material acceptance | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | line 3 | `msea_r7_receipt_schema_contract_draft_accepted_pending_operator_next_lane_selection` | active session bootstrap | VALUE_SET | ACCEPT |
| Source mirror is pinned to upstream MinerU commit and 425 files | `.private_reference/source_mirrors/INDEX.md` | line 35 | `opendatalab__MinerU`; `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` | source mirror index | VALUE_SET | ACCEPT |
| Full mirror groups total 425 files | `docs/reviews/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_WORKER_RETURN_2026-07-02.md` | lines 146-160 | `Full Mirror Manifest`; `425` | MSEA-R5 worker return | VALUE_SET | ACCEPT |
| MSEA-R5 explicitly left `mineru/model/utils` at listing depth | `docs/reviews/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_WORKER_RETURN_2026-07-02.md` | lines 252, 417-424, 593-602 | `mineru/model/utils`; `PARTIAL` | MSEA-R5 worker return | VALUE_SET | ACCEPT |
| MSEA-R5 routed deeper `mineru/model/utils` read as a future explicit tranche | `docs/reviews/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_WORKER_RETURN_2026-07-02.md` | lines 527-528 | `mineru/model/utils` | MSEA-R5 follow-up routing matrix | VALUE_SET | ACCEPT |
| MSEA-R5 owner delta records the same read-depth limitation | `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` | lines 109-117 | `Read-Depth Limitation` | MSEA-R5 owner delta | VALUE_SET | ACCEPT |
| MSEA-T2 owns receipt, quality, and RAG-handoff boundaries | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | sections `Receipt Advisory`; `Quality And RAG Handoff Advisory`; `Checker Candidate Ledger` | `MSEA-CC-4` | MSEA-T2 reference | VALUE_SET | ACCEPT |
| MSEA checker candidates remain parked behind concrete conditions | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md` | rows `MSEA-document-truth-overclaim-checker`; `MSEA-runtime-readiness-overclaim-checker`; `MSEA-rag-handoff-checker` | `PARKED_UNTIL_CONDITION` | conditional reopen index | VALUE_SET | ACCEPT |

## Current Runtime Freshness Verification

| Claim checked | Verification command | Observed result | Disposition |
|---|---|---|---|
| Planned MSEA-R8 baseline path absent before dispatch | `Test-Path -LiteralPath 'docs/baselines/CVF_GC018_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md'` | `False` before authoring | ACCEPT |
| Planned MSEA-R8 work order path absent before dispatch | `Test-Path -LiteralPath 'docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md'` | `False` before authoring | ACCEPT |
| Planned worker output paths absent before dispatch | `Test-Path` checks for planned worker return and residual ledger | both absent before authoring | ACCEPT |

## Negative Search And Collision Discipline

| Check | Command | Result | Disposition |
|---|---|---|---|
| MSEA-R8 collision search | `rg -n "MSEA-R8|MSEA_R8|MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION|Residual Full Repository Absorption" docs CVF_SESSION AGENT_HANDOFF_V32_2026-07-02.md` | no pre-existing governed artifact collisions before authoring | ACCEPT |
| Existing output path absence | `Test-Path` checks for planned worker return and residual ledger reference | both absent before authoring | ACCEPT |
| Existing implementation search | `rg -n "MinerU|mineru" EXTENSIONS governance scripts docs/reference docs/roadmaps docs/reviews docs/work_orders docs/baselines -g "!*MSEA*"` | no CVF-owned MinerU runtime implementation surface is authorized by this dispatch | ACCEPT |

## Worker Autonomy / No-Question Rule

The worker proceeds without operator confirmation for non-destructive actions
inside this work order's Allowed scope, including source reads, residual ledger
authoring, governance format repair, and gate reruns after allowed-scope
remediation.

Escalate only if a needed action would exceed Allowed scope, run MinerU, use
secrets or credentials, consume provider/live quota, mutate runtime/source,
open public-sync, change risk level, release a held implementation lane, touch
forbidden paths, or perform destructive/irreversible actions.

## Operator Checkpoint

No operator checkpoint is needed for the worker to execute the documentation
residual-ledger scope. Operator approval is required before any runtime,
provider/live proof, credential/S3 use, MinerU execution, Docker execution,
package activation, checker implementation, public-sync, Web/MCP/model-router/
action-authority, or production-readiness claim.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | dispatcher authors GC-018/work order; worker produces uncommitted artifacts; reviewer/closer owns acceptance commit and later session-sync |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=825c454d; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | dispatch changes only this GC-018 and work order; worker changes only planned worker return and residual ledger reference |
| traceScope(phase, actor) | worker return and residual ledger reference must include Agent Operation Trace Block; reviewer owns committed-range verification |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT for worker; reviewer/closer owns material commit |
| crossBatchIsolation | clean worktree required before worker execution; unrelated dirty paths must be recorded as blocker or pre-existing exemption |
| nextMoveSurfaces | worker does not edit session surfaces; reviewer/session-sync steward updates mode and next move only after material acceptance |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | N/A_WITH_REASON: no separate `_COMPLETION_` reviewer artifact is planned; prefer repairing evidence in the worker return per literal-format gotcha 30 |
| reviewerOwnedClosurePaths | worker return and residual ledger reference after reviewer acceptance; session-sync surfaces only in a later dedicated commit |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Work-Order Fulfillment Manifest

| Required output | Path or evidence | Owner | Required status |
|---|---|---|---|
| Worker return | `docs/reviews/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_WORKER_RETURN_2026-07-02.md` | worker | created, uncommitted, gate-checked |
| Residual absorption ledger reference | `docs/reference/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md` | worker | created, uncommitted, source-backed |
| Full mirror reconciliation | worker return and ledger reference | worker | source mirror commit and 425-file count verified |
| Residual target closure | worker return and ledger reference | worker | each residual group terminally dispositioned |
| No-commit evidence | worker return | worker | HEAD unchanged and no commit/stage/push |

## Residual Ledger Requirements

The worker must include these sections in the reference ledger:

| Section | Required content |
|---|---|
| Purpose / Scope / Boundary | documentation-only residual absorption ledger and non-claims |
| Source Authority | MSEA-T0/T2/T3/R4/R5/R6/R7 and pinned source mirror |
| Prior Coverage Reconciliation | which parts of 425-file mirror are already sufficiently absorbed by prior MSEA artifacts |
| Residual Target Manifest | recomputed counts for the residual groups named by this work order |
| Residual Processing Ledger | terminal status for each residual group and all file-level rows where text/source value is present |
| Candidate And No-Value Ledger | package/runtime/checker/reject/no-value classification with concrete reopen conditions where applicable |
| Overlap And Novelty Classification | comparison against existing MSEA owner surfaces |
| Blind-Spot Verdict | `CLEAR_WITH_DECLARED_BINARY_LIMITS`, `PARTIAL`, or `BLOCKED_WITH_REASON` with reason; do not claim clear if any source/text group remains unread |
| Claim Boundary | no runtime/schema implementation/document-truth/accuracy/production claim |

The worker must not ask the operator whether to do full per-file work. This
work order already authorizes file-content reading for residual text/source
files and metadata-level ledgering for binary/asset files inside Allowed scope.

## Residual Target Manifest

| Residual group | Dispatch count evidence | Required worker action |
|---|---|---|
| `.github` source-control workflow/config files | 8 files under the pinned mirror | read or group-disposition by file, identify CI/release/package value, reject direct import |
| root-level files | 11 files at mirror root | read each text/config file or classify binary/metadata with reason |
| root `demo` folder | 8 files under mirror root `demo` | read each file or group-disposition generated/binary samples with reason |
| `projects` folder | 2 files | read each file and classify project/example value |
| `tests` folder | 4 files | read each file and classify fixture/testing/checker value |
| `mineru/model/utils` | 57 files | read at file-content depth, not listing-only; group only tightly related utility subfamilies with explicit per-file coverage |
| Docker China hardware variants | 9 hardware-variant Dockerfiles | read/diff content enough to classify hardware/package value; no Docker execution |
| docs assets/images/chemical demo binaries | 92 files | file-level manifest with extension/role metadata or grouped binary ledger; do not claim semantic content read unless opened/rendered |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | external repo or copied folder -> pinned source mirror -> residual file/group ledger -> owner-surface comparison -> value conversion matrix -> future work only by fresh authorization |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py`; `governance/compat/check_corpus_completeness_report_integrity.py` |
| Owner surface | this work order and paired MSEA-R8 GC-018 baseline |
| Disposition | DISPATCH residual documentation/reference absorption ledger from accepted MinerU source-mirror evidence |
| Claim boundary | dispatch fulfillment only; no runtime, package activation, checker wiring, provider/live proof, public-sync, MCP server, API/router/Gradio, Docker, model download, OCR/VLM/hybrid execution, RAG write, benchmark, or production-readiness claim |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md |
| Input root or repository | `https://github.com/opendatalab/MinerU.git` at `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`; local mirror `.private_reference/source_mirrors/opendatalab__MinerU/`; accepted MSEA-T0/T2/T3/R4/R5/R6/R7 evidence |
| Enumeration command | `rg --files --hidden --no-ignore .private_reference/source_mirrors/opendatalab__MinerU -g '!**/.git/**'` plus worker recomputation of residual target groups |
| Manifest artifact or inline manifest | inline `## Residual Target Manifest` table |
| Processing ledger artifact or inline ledger | planned `docs/reviews/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_WORKER_RETURN_2026-07-02.md` and `docs/reference/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md` |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | MSEA-T2/T3/R4/R5/R6/R7 owner surfaces plus `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md` |
| Unresolved items | residual ledger pending worker execution |
| Completion claim boundary | documentation-only residual absorption closure ledger; no runtime/provider/public/package/checker expansion |

## Corpus Completeness And Report Integrity

- Corpus task class: external repository residual absorption dispatch from accepted MSEA evidence.
- Corpus root: `.private_reference/source_mirrors/opendatalab__MinerU/` plus accepted MSEA governed artifacts.
- Snapshot time: 2026-07-02 local dispatch session.
- Enumeration command: `rg --files --hidden --no-ignore .private_reference/source_mirrors/opendatalab__MinerU -g '!**/.git/**'` with PowerShell path normalization for residual groups.
- Manifest artifact or inline manifest: inline `## Residual Target Manifest`.
- Manifest hash: inherited from accepted MSEA-R5 full-mirror evidence unless worker detects source mirror drift; worker must recompute commit and count.
- Processing ledger artifact or inline ledger: planned `docs/reviews/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_WORKER_RETURN_2026-07-02.md` and `docs/reference/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md`.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE
- Reconciliation: manifest=8 residual groups; ledger_terminal=0 at dispatch before worker execution; exclusions=0; unresolved=0.
- Unresolved files: 0
- Declared exclusions: none at dispatch; binary assets may be metadata-ledgered with reason but must remain visible.
- Unreadable or unsupported files: none known at dispatch.
- Aggregation check: residual groups map to accepted MSEA-R4/R5 declared limitations and remaining non-target root folders.
- Drift check: worker must verify source mirror commit and full count still match the source mirror index before source reads.
- Output traceability: residual ledger must cite accepted MSEA artifacts, the pinned source mirror, and conditional reopen rows for any candidate value.
- Adversarial verification: worker must distinguish source-file presence, documentation value, package candidate value, runtime candidate value, checker candidate value, direct-import rejection, extraction quality, document truth, and readiness.
- Corpus verdict: PARTIAL

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| Residual source/read-depth ledger | closes the remaining source-mirror blind-spot evidence gap | DOCTRINE_ADAPTED | planned MSEA-R8 residual ledger reference | worker creates CVF-owned residual absorption ledger | no runtime behavior |
| Docker hardware variants and acceleration/deployment configs | deployment recipes may preserve package/deployment candidate evidence | PACKAGE_CANDIDATE | MSEA-R4/R5 owner deltas and conditional reopen index if worker finds new candidate value | preserve or update candidate classification only in worker output; implementation needs fresh authorization | no Docker build/run or package activation |
| `mineru/model/utils` internals and demo/test/project files | may reveal runtime, model-pre/post-processing, fixture, or adapter-readiness candidate value | RUNTIME_CANDIDATE | MSEA-R5 owner delta or new MSEA-R8 residual ledger row | park with concrete reopen condition if value is real | no model execution, parser run, provider call, or source import |
| Possible checker lessons from tests/fixtures or overclaim boundaries | may sharpen MSEA checker candidates if repeated gap evidence is found | CHECKER_CANDIDATE | MSEA-T3 closeout and conditional reopen index | worker may record candidate evidence only; no checker implementation | no checker source edits or hook wiring |
| Direct upstream code, CI, Docker, tests, assets, or sample import | upstream artifacts remain advisory input only | REJECT_DIRECT_IMPORT | planned MSEA-R8 residual ledger | reject direct copy/import; adapt only CVF-native doctrine/candidate evidence | no direct wiring or copied implementation |
| Binary/assets or duplicate metadata with no CVF delta | may have no independent package/runtime/checker value after manifesting | NO_PACKAGE_OR_RUNTIME_VALUE | existing MSEA owner surfaces or MSEA-R8 ledger | close with explicit reason and file/count evidence | no runtime or package behavior |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| `mineru/model/utils` residual gap | `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` | ENRICH_EXISTING | R5 explicitly left this folder at listing depth; R8 may close the gap by file-content ledger | create residual ledger |
| Docker hardware variants | `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md` | ENRICH_EXISTING | R4/R5 recorded deployment candidate value but not every variant file body | read/classify without Docker execution |
| Root, demo, projects, tests, and `.github` groups | `docs/reviews/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_WORKER_RETURN_2026-07-02.md` | NEW_FINDING | these groups were counted in the 425-file manifest but were not the R5 deep target | ledger residual value or close as no-new-value |
| Binary docs assets/images/chemical demo material | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | NO_NEW_VALUE | expected to support documentation/examples unless worker finds source-backed delta | manifest visibly with reason |
| MSEA checker candidates | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md` | CONFIRMED_EXISTING | current checker rows remain parked unless worker finds concrete repeated-miss evidence | cite or preserve parked rows |
| Direct upstream source import | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | REJECT_DIRECT_IMPORT | direct import remains blocked even if CVF-native value remains | adapt or park, do not copy |

## Source Mirror Migration Control

| Field | Disposition |
|---|---|
| Legacy source path | Legacy MinerU adapter folder remains secondary historical material and is not source authority for MSEA-R8. |
| Source mirror path | `.private_reference/source_mirrors/opendatalab__MinerU/` |
| Mirror index row | `.private_reference/source_mirrors/INDEX.md` row `opendatalab__MinerU` |
| Pinned upstream commit | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` |
| Migration disposition | MIGRATED_TO_SOURCE_MIRROR |
| Legacy cleanup disposition | LEGACY_REFERENCE_ONLY_WITH_REASON: historical comparison only; source facts must prefer the pinned mirror or governed MSEA artifacts |
| Claim boundary | source-mirror authority control only; no runtime, install, package activation, provider/live proof, public-sync, checker implementation, or production-readiness claim |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Storage action | N/A with reason: MSEA-R8 creates one worker return and one reference ledger in existing governed folders only. |
| Folder/index impact | No new folder, stable reference family, front door, storage layout, or dated duplicate standard is authorized. |
| Durable foundation impact | The residual ledger is a tranche-specific reference artifact, not a central foundation standard. |
| Required boundary | Worker must not create or relocate foundation storage, index, template, standard, or front-door files. |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: MSEA-R8 routes the freshly cloned MinerU source
mirror under `.private_reference/source_mirrors/opendatalab__MinerU/`, not a
legacy absorption folder. The legacy coverage index is not the owner surface
for this tranche. The work order retains the legacy folder only as a
forbidden-scope boundary and historical-reference warning.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_WORKER_RETURN_2026-07-02.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Evidence Requirements

- Worker return must cite execution base, source mirror HEAD, full mirror
  count, residual target counts, residual ledger output, gate output, changed
  files, and no-commit evidence.
- Residual ledger must cite prior MSEA coverage, source mirror reads, terminal
  status ledger, value conversion matrix, overlap classification, and claim
  boundaries.
- Residual ledger must distinguish source-file presence, source-read depth,
  documentation value, package candidate value, runtime candidate value,
  checker candidate value, direct-import rejection, extraction quality,
  document truth, downstream use, and runtime readiness.
- Evidence must come from governed CVF artifacts, the pinned source mirror, or
  checker output, not provider-local memory.

## Execution Plan

1. Capture `executionBaseHead`, `git status --short`, source mirror HEAD, and
   the full mirror file count.
2. Read required first reads and checker sources.
3. Recompute the residual target manifest using filesystem-backed source mirror
   enumeration.
4. Create the worker return and residual ledger reference inside allowed paths
   only.
5. Read residual text/source files at file-content depth; metadata-ledger
   binary/assets with explicit reason.
6. Fill prior coverage reconciliation, processing ledger, value conversion,
   overlap/novelty, conditional reopen, and claim-boundary sections.
7. Run required gates or return a classified blocker.

## Acceptance Criteria

- Planned worker return exists and records execution base, source mirror HEAD,
  actual `git status --short`, changed files, command evidence, and no-commit
  evidence.
- Planned residual ledger exists and records prior coverage reconciliation,
  residual target manifest, residual processing ledger, value conversion
  matrix, overlap/novelty classification, conditional reopen handling, and
  claim boundary.
- Full mirror still reconciles to the pinned commit and 425 files, or the
  worker returns `BLOCKED_WITH_REASON`.
- `mineru/model/utils`, Docker hardware variants, root/demo/projects/tests/
  `.github`, and binary asset groups are not silently skipped.
- No source mirror payload, runtime source, session state, handoff, checker,
  public-sync, or extension path is edited by the worker.

Fail conditions:

- source mirror commit or file count differs from dispatch and no reviewer-
  supplied fresh source authority exists;
- worker creates runtime/provider/S3/RAG/Docker/checker/package/Web/MCP/source
  implementation or claims production readiness;
- worker claims file-content absorption for binary/assets without evidence;
- residual ledger omits the claim boundary or future implementation blockers;
- worker commits, stages, pushes, or edits forbidden paths.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` instead of continuing if the source mirror commit
differs, required source files are missing, residual groups cannot be
reconciled, the ledger requires runtime/provider/credential/public/checker
scope, source evidence contradicts accepted MSEA owner surfaces, gates cannot
pass inside allowed scope, or the worktree contains unrelated dirty paths that
cannot be isolated.

## Closure Checklist

- [x] Work order names worker write ownership.
- [x] Worker return and residual ledger reference are the only worker-owned
  output paths.
- [x] Source verification, external absorption, corpus, handoff, AOT, Delta,
  ADIF, and worker-return shape controls are present.
- [x] Runtime/provider/live/S3/RAG/Docker/checker/package/public/Web/MCP/
  model-router expansions remain forbidden.
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
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_source_mirror_migration.py`; `governance/compat/check_corpus_completeness_report_integrity.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `External knowledge intake routing: REQUIRED`; `External absorption core: REQUIRED`; `## Dispatch Prompt Envelope`; `## Source Verification Block`; `## Current Runtime Freshness Verification`; `## Negative Search And Collision Discipline`; `## Agent Handoff Contract Control Block`; `## Reviewer Closure Conversion`; `## Work-Order Fulfillment Manifest`; `## Worker Return Packet Shape Contract`; `WORKER_RETURN_FULL_GATE_V1`; `requiredGate:`; `individualCheckerSubstitution: FORBIDDEN`; `workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED`; `## External Knowledge Intake Routing`; `## External Absorption Core`; `## Corpus Completeness And Report Integrity`; `## External Absorption Value Conversion Matrix`; `## Overlap And Novelty Classification`; `DEFERRED_PRIVATE_ONLY`; `CLAIM_REJECTED_NO_RECEIPT`; `CLAIM_REJECTED_NO_ACTION`; `PARTIAL` |
| gateRunPurpose | confirmation/evidence run for MSEA-R8 dispatch after checker read-ahead, not first discovery |
| claimBoundary | checker read-ahead proves dispatch authoring diligence only; worker completion and any runtime/provider/public/package/checker behavior remain unproved and unauthorized |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R8 --title "MinerU Residual Full Repository Absorption Closure Ledger" --date 2026-07-02 --base 825c454d --commit-mode WORKER_MUST_NOT_COMMIT --dependency "MSEA-R7 accepted at 074144c9; operator requested absorbing the remaining MinerU repository deeply" --include-worker-return-skeleton --stdout` |
| generatedProfile | packet-kind=generic-worker-dispatch; commit-mode=WORKER_MUST_NOT_COMMIT; worker-return skeleton requested |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced scaffold fields with MSEA-R8 residual absorption scope, source verification, residual ledger requirements, external absorption blocks, source mirror migration control, no-commit worker shape, and verification commands |
| checkerReadAheadConfirmation | read guard orientation, literal-format gotchas, external absorption standards, MSEA-R4/R5/R6/R7 artifacts, MSEA-T2/T3 owner surfaces, source mirror anchors, and applicable checker source paths before writing |
| docOnlyNewFields | residual full-repository absorption closure ledger path; residual target manifest; residual ledger requirements; blind-spot verdict vocabulary |
| claimBoundary | scaffold provenance supports dispatch authoring only; no worker completion, runtime/provider/live/public/package/Web/MCP/model-router/action-authority, checker, or production claim |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher |
| Provider or surface | local workspace |
| Session or invocation | MSEA-R8 dispatch authoring, 2026-07-02 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, git, apply_patch, governance checkers |
| Target paths | `docs/baselines/CVF_GC018_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md` |
| Allowed scope source | operator request to continue and absorb the remaining MinerU repository following material commit `074144c9` |
| Before status evidence | clean worktree at `825c454d`; planned MSEA-R8 paths absent before authoring |
| After status evidence | dispatch baseline and work order created with source verification and pending pre-dispatch gates |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | dispatcher authoring only; worker execution remains no-commit |
| Claim boundary | no runtime/provider/public/source-import/Web/MCP/model-router/checker/package/action-authority claim |
| Agent type | dispatcher |
| Invocation ID | `msea-r8-mineru-residual-absorption-dispatch-2026-07-02` |
| Expected manifest | `docs/baselines/CVF_GC018_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md` |
| Actual changed set | `docs/baselines/CVF_GC018_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in dispatch artifact creation |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | MSEA-R8 residual full-repository absorption closure ledger work order |
| claimDisposition | CLAIM_REJECTED: no Delta runtime execution-control claim is made |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed |
| invocationBoundary | local authoring, source verification, and governance checker invocation only |
| interceptionBoundary | no runtime interception, parser execution, provider invocation, S3 access, RAG write, Docker action, or action-control behavior |
| claimLanguage | source-backed documentation/reference residual absorption dispatch only |
| forbiddenExpansion | no runtime/provider/live/public/package/Web/MCP/model-router/action-authority, automatic invocation, checker implementation, source import, credential handling, Docker execution, or production-readiness claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: MSEA-R8 dispatch is private provenance residual source-mirror
absorption work derived from private MinerU source-mirror evidence. No
public-sync artifact is created or authorized by this work order.

## Claim Boundary

MSEA-R8 authorizes a no-commit worker to create a CVF-native residual
full-repository absorption closure ledger from accepted source-backed evidence.
It does not authorize or claim MinerU runtime integration, parser execution,
OCR execution, VLM/hybrid backend routing, remote backend processing, model
download, API/router/Gradio service, Docker deployment, RAG indexing,
provider/live proof, S3 access, credential handling, document truth
verification, parser accuracy, table/formula correctness, public-sync export,
checker enforcement, package activation, certification, generated aggregate
mutation, production readiness, hosted readiness, model-router behavior, action
authority, or universal document intelligence.
