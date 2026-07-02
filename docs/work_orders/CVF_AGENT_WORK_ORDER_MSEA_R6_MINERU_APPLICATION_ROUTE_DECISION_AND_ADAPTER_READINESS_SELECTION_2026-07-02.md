# CVF Agent Work Order - MSEA-R6 MinerU Application Route Decision And Adapter Readiness Selection

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-07-02

docType: work_order

Batch ID: MSEA-R6

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: 088fdcb4

External knowledge intake routing: REQUIRED

External absorption core: REQUIRED

## Dispatch Prompt Envelope

Role: no-commit worker for MSEA-R6 MinerU application route decision and
adapter-readiness selection.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_AND_ADAPTER_READINESS_SELECTION_2026-07-02.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

Base: capture `executionBaseHead` with `git rev-parse --short HEAD` before
edits. Expected dispatch base is `088fdcb4` or the reviewer-provided current
dispatch commit if this packet is committed first.

Current-time notes: current date is 2026-07-02; upstream MinerU is pinned at
`3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`.

Required first actions: read startup surfaces, this work order, the paired
GC-018 baseline, MSEA-R4 and MSEA-R5 accepted artifacts, MSEA-T2/T3 owner
surfaces, external absorption references, the source mirror index, and checker
source paths listed below before writing conclusions.

Return contract: create the worker return and route decision matrix, run the
listed gates, leave changes uncommitted, and return `COMPLETE_PENDING_REVIEW`,
`COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, or `BLOCKED_WITH_REASON`.

Do-not-misread notes: this work order selects or holds the next MinerU route.
It does not authorize MinerU install, parser run, OCR/VLM/hybrid execution,
API/router/Gradio service, Docker, model download, provider/live proof,
OpenAI-compatible endpoint call, S3 connection, credential storage, RAG index
write, source import, checker implementation, package activation, public-sync,
Web/MCP/model-router/action-authority, automatic invocation, benchmark, or
production-readiness claims.

## Purpose

Use MSEA-R4 and MSEA-R5 source-backed evidence to decide the next MinerU route
for detailed document/layer scan use cases. The worker must produce a compact
route decision, not another full-corpus replay and not an implementation.

## Mission

Create:

1. `docs/reviews/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_AND_ADAPTER_READINESS_SELECTION_WORKER_RETURN_2026-07-02.md`
2. `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md`

The worker must evaluate all allowed route outcomes and select exactly one
final outcome unless blocked by source contradiction.

Allowed routing outcomes:

- `OPEN_RECEIPT_SCHEMA_CONTRACT_DRAFT`
- `OPEN_LOCAL_PARSER_ADAPTER_VALUE_PROBE`
- `OPEN_RAG_HANDOFF_ROUTE_PROBE`
- `OPEN_PROVIDER_ASSISTED_TITLE_CORRECTION_PROBE`
- `OPEN_STORAGE_CREDENTIAL_BOUNDARY_PROBE`
- `OPEN_CHECKER_CANDIDATE_VALUE_PROBE`
- `HOLD_ALL_IMPLEMENTATION_LANES`
- `BLOCKED_SOURCE_CONTRADICTION`

## Authority Chain

| Authority | Path or source | Disposition |
|---|---|---|
| Operator instruction | chat request on 2026-07-02 to issue the next MinerU work order after MSEA-R5 | ACCEPT |
| GC-018 baseline | `docs/baselines/CVF_GC018_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_AND_ADAPTER_READINESS_SELECTION_2026-07-02.md` | ACCEPT |
| Active session front door | `CVF_SESSION_MEMORY.md` | ACCEPT |
| Bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | ACCEPT |
| Active state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V32_2026-07-02.md` | ACCEPT |
| MSEA-R5 worker return | `docs/reviews/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_WORKER_RETURN_2026-07-02.md` | ACCEPT |
| MSEA-R5 owner delta | `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` | ACCEPT |
| MSEA-R4 worker return | `docs/reviews/CVF_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_WORKER_RETURN_2026-07-02.md` | ACCEPT |
| MSEA-T2 advisory | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | ACCEPT |
| MSEA-T3 closeout | `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | ACCEPT |
| Source mirror index | `.private_reference/source_mirrors/INDEX.md` | ACCEPT |
| Conditional reopen index | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md` | ACCEPT |

Authority boundary:

- External MinerU source is advisory input only.
- The pinned source mirror is preferred for current upstream facts.
- MSEA-R4/R5 and MSEA-T2/T3 are CVF-owned comparison surfaces.
- Any selected implementation route still requires a later fresh GC-018 and
  source-verified work order before execution.

## Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | author source-verified dispatch packet and run pre-dispatch gates |
| Worker | no-commit worker role | produce worker return and route decision matrix without committing |
| Reviewer/closer | Codex | review returned artifacts, repair allowed-scope defects, and commit if accepted |
| Session-sync steward | Codex after material acceptance | update continuity after accepted material commit if next move changes |
| Operator checkpoint | operator | required for any runtime, provider/live proof, credentials, S3, package activation, checker implementation, public-sync, or scope expansion |

## Intake Role Routing Decision

- Intake summary: operator requested the next MinerU work order after MSEA-R5
  deep document/layer absorption completed.
- Scope classification: bounded no-commit documentation/reference route
  decision.
- Risk sensitivity: no public-sync, provider/live run, secret, credential,
  package activation, runtime implementation, checker implementation,
  production, or readiness claim.
- Selected role route: routeMode=SINGLE_AGENT_MULTI_ROLE.
- Role separation basis: dispatcher authors packet, worker produces
  uncommitted artifacts, reviewer/closer owns acceptance and commit.
- Escalation condition: stop for operator checkpoint if scope/risk changes or
  if any runtime/provider/S3/RAG/checker/package/public action becomes needed.

## Single-Agent Multi-Role Control Block

- Role separation ledger: dispatcher, worker, reviewer/closer, and
  session-sync steward duties are recorded separately in this packet.
- Evidence basis: review must use git diff, source paths, route-decision
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

- `docs/reviews/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_AND_ADAPTER_READINESS_SELECTION_WORKER_RETURN_2026-07-02.md`
- `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md`

Allowed read scope:

- startup surfaces and current active handoff;
- this work order and paired GC-018 baseline;
- MSEA-T0/T2/T3/R4/R5 governed artifacts;
- external absorption references and source mirror index;
- the pinned MinerU source mirror only for route-specific spot checks:
  `docs/en/reference/output_files.md`, `docs/zh/usage/plugin/RagFlow.md`,
  `mineru/utils/llm_aided.py`, `mineru/data/io/s3.py`, and source files named
  by R5 if needed to verify a route candidate.

Forbidden scope:

- no edits to source mirror payload, `.private_reference/legacy/`, `EXTENSIONS/`,
  runtime source, `governance/compat/`, hooks, CI, scripts, active session
  state, active handoff, or public-sync files;
- no MinerU install, parser execution, OCR/VLM/hybrid/backend/API/router/Gradio
  execution, Docker run, model download, provider/live proof,
  OpenAI-compatible endpoint call, S3 connection, credential storage, RAG index
  write, benchmark, source import, checker implementation, package activation,
  Web/MCP/model-router/action-authority, automatic invocation, or production
  claim;
- no commit by the worker.

Risk ceiling: R0 documentation/reference and route decision only.

## Write Ownership

| Path | Owner | Permission |
|---|---|---|
| `docs/reviews/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_AND_ADAPTER_READINESS_SELECTION_WORKER_RETURN_2026-07-02.md` | worker | create or repair inside allowed scope; leave uncommitted |
| `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md` | worker | create or repair inside allowed scope; leave uncommitted |
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
- MSEA-R4 and MSEA-R5 accepted artifacts
- MSEA-T2 advisory and MSEA-T3 closeout
- `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md`

## Pre-Flight Checks

Before implementation, the worker must capture:

```powershell
git rev-parse --short HEAD
git status --short
git -C .private_reference/source_mirrors/opendatalab__MinerU rev-parse HEAD
```

Expected source mirror commit:

`3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`

If the source mirror commit differs, the worker must record
`BLOCKED_SOURCE_CONTRADICTION` unless the reviewer supplies a fresh dispatch.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Current mode is pending next MinerU route decision | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `currentMode` | `msea_r5_accepted_pending_next_mineru_route_decision` | active session bootstrap | VALUE_SET | ACCEPT |
| MSEA-R5 reconciled 425/425 full mirror and 373/373 target subset | `docs/reviews/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_WORKER_RETURN_2026-07-02.md` | Full Mirror Manifest and R5 Target Subset Manifest | `425/425`; `373/373` | MSEA-R5 worker return | VALUE_SET | ACCEPT |
| MSEA-R5 requires follow-on scope naming a specific pain point before any implementation | `docs/reviews/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_WORKER_RETURN_2026-07-02.md` | Risk / Corrective Action and Follow-Up Routing Matrix | `follow-on MSEA-R6+`; `STRATEGIC_OPERATOR_DECISION` | MSEA-R5 worker return | VALUE_SET | ACCEPT |
| Receipt-schema route has source-backed upstream evidence | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/reference/output_files.md` | lines 17, 35, 62, 109, 292, 396, 730-742 | `layout.pdf`; `span.pdf`; `model.json`; `middle.json`; `content_list.json`; `content_list_v2.json` | upstream output-file reference | VALUE_SET | ACCEPT |
| RagFlow route has source-backed integration evidence | `.private_reference/source_mirrors/opendatalab__MinerU/docs/zh/usage/plugin/RagFlow.md` | lines 1-68 | `RagFlow`; `MINERU_EXECUTABLE` | upstream RagFlow plugin guide | VALUE_SET | ACCEPT |
| Provider-assisted title route has source-backed provider-call evidence | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/llm_aided.py` | lines 6; 164-166 | `OpenAI`; `api_key`; `base_url` | MinerU LLM-aided title utility | EXISTS | ACCEPT |
| Storage route has source-backed credential and S3 evidence | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/data/io/s3.py` | lines 6-15; 18-45; 90-113 | `S3Reader`; `ak`; `sk`; `endpoint_url`; `boto3` | MinerU S3 IO layer | EXISTS | ACCEPT |
| Checker route already has parked MSEA candidate rows | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md` | rows `MSEA-document-truth-overclaim-checker`, `MSEA-runtime-readiness-overclaim-checker`, `MSEA-rag-handoff-checker` | `PARKED_UNTIL_CONDITION` | external absorption conditional reopen index | VALUE_SET | ACCEPT |

## Current Runtime Freshness Verification

| Claim checked | Verification command | Observed result | Disposition |
|---|---|---|---|
| No current CVF-owned MinerU runtime adapter implementation is visible outside governed MSEA/reference evidence | `rg -n "MinerU|mineru" EXTENSIONS governance scripts docs/reference docs/roadmaps docs/reviews docs/work_orders docs/baselines -g "!*MSEA*"` | returned only external absorption conditional-reopen index rows for MSEA checker candidates | ACCEPT |
| Provider registry surfaces are accounted for as out of scope | `Test-Path EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts`; `rg -n "PROVIDER_CAPABILITY_REGISTRY" EXTENSIONS/CVF_MODEL_GATEWAY/src -g "*.ts"` | provider registry exists; `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` declares `PROVIDER_CAPABILITY_REGISTRY`; MSEA-R6 makes no provider registry absence, provider-routing, hardcoded-provider, or live-governance claim | ACCEPT |
| Planned worker return path absent before dispatch | checked by dispatcher before authoring | absent before authoring | ACCEPT |
| Planned route decision matrix path absent before dispatch | checked by dispatcher before authoring | absent before authoring | ACCEPT |

## Negative Search And Collision Discipline

| Check | Command | Result | Disposition |
|---|---|---|---|
| MSEA-R6 collision search | `rg -n "MSEA-R6|MSEA_R6|MinerU Application Route Decision|MINERU_APPLICATION_ROUTE_DECISION|MinerU Route Decision" docs CVF_SESSION AGENT_HANDOFF_V32_2026-07-02.md` | only R5 future-route mentions before authoring | ACCEPT |
| Existing runtime adapter search | `rg -n "MinerU|mineru" EXTENSIONS governance scripts docs/reference docs/roadmaps docs/reviews docs/work_orders docs/baselines -g "!*MSEA*"` | no implementation surface outside governed conditional-reopen/reference evidence | ACCEPT |
| Optional completion review absence | no separate completion review path is planned in this dispatch | absence is intentional; reviewer should repair the worker return if accepted | ACCEPT |

## Worker Autonomy / No-Question Rule

The worker proceeds without operator confirmation for non-destructive actions
inside this work order's Allowed scope, including source reads, route-candidate
comparison, governance format repair, and gate reruns after allowed-scope
remediation.

Escalate only if a needed action would exceed Allowed scope, run MinerU, use
secrets or credentials, consume provider/live quota, mutate runtime/source,
open public-sync, change risk level, release a held implementation lane, touch
forbidden paths, or perform destructive/irreversible actions.

## Operator Checkpoint

No operator checkpoint is needed for the worker to execute the documentation
route-decision scope. Operator approval is required before any runtime,
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
| baseHeadFor(phase) | dispatchBaseHead=088fdcb4; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | dispatch changes only this GC-018 and work order; worker changes only planned worker return and route decision matrix |
| traceScope(phase, actor) | worker return and route decision matrix must include Agent Operation Trace Block; reviewer owns committed-range verification |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT for worker; reviewer/closer owns material commit |
| crossBatchIsolation | clean worktree required before worker execution; unrelated dirty paths must be recorded as blocker or pre-existing exemption |
| nextMoveSurfaces | worker does not edit session surfaces; reviewer/session-sync steward updates mode and next move only after material acceptance |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | N/A_WITH_REASON: no separate `_COMPLETION_` reviewer artifact is planned; prefer repairing evidence in the worker return per literal-format gotcha 30 |
| reviewerOwnedClosurePaths | worker return and route decision matrix after reviewer acceptance; session-sync surfaces only in a later dedicated commit |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Work-Order Fulfillment Manifest

| Required output | Path or evidence | Owner | Required status |
|---|---|---|---|
| Worker return | `docs/reviews/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_AND_ADAPTER_READINESS_SELECTION_WORKER_RETURN_2026-07-02.md` | worker | created, uncommitted, gate-checked |
| Route decision matrix | `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md` | worker | created, uncommitted, source-backed |
| Selected routing outcome | worker return and route matrix | worker | exactly one allowed outcome or `BLOCKED_SOURCE_CONTRADICTION` |
| Route evidence table | worker return | worker | all 7 non-blocker route candidates dispositioned |
| No-commit evidence | worker return | worker | HEAD unchanged and no commit/stage/push |

## Route Evaluation Requirements

The worker must evaluate every route below and select exactly one outcome:

| Route candidate | Required evaluation |
|---|---|
| `OPEN_RECEIPT_SCHEMA_CONTRACT_DRAFT` | decide whether CVF should next draft a receipt contract informed by `output_files.md`, without implementing parser/runtime behavior |
| `OPEN_LOCAL_PARSER_ADAPTER_VALUE_PROBE` | decide whether a later local parser value probe is warranted, with explicit live/runtime proof boundary |
| `OPEN_RAG_HANDOFF_ROUTE_PROBE` | decide whether RagFlow/RAG handoff evidence justifies a later RAG route probe |
| `OPEN_PROVIDER_ASSISTED_TITLE_CORRECTION_PROBE` | decide whether `llm_aided.py` warrants a later provider/live proof route |
| `OPEN_STORAGE_CREDENTIAL_BOUNDARY_PROBE` | decide whether `s3.py` warrants a later credential-boundary route |
| `OPEN_CHECKER_CANDIDATE_VALUE_PROBE` | decide whether existing MSEA checker reopen conditions are met |
| `HOLD_ALL_IMPLEMENTATION_LANES` | choose only if no route has source-backed value sufficient for a next governed tranche |

Selection rule: if multiple routes are valuable, choose the route with the
lowest risk and highest immediate CVF value for detailed document/layer scan
use cases. In this dispatch, documentation/receipt-contract work is lower risk
than runtime/provider/S3/Docker/checker implementation.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | external repo or copied folder -> pinned source mirror and accepted MSEA evidence -> route decision matrix -> future GC-018/work order only if a route is selected |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py` |
| Owner surface | this work order and paired GC-018 baseline |
| Disposition | DISPATCH decision-only source-backed route selection |
| Claim boundary | dispatch only; no MinerU execution, provider/live proof, credential use, source import, public-sync, package activation, checker implementation, Web/MCP/model-router/action-authority, or production-readiness claim |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md |
| Input root or repository | `https://github.com/opendatalab/MinerU.git` at `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`; local mirror `.private_reference/source_mirrors/opendatalab__MinerU/`; accepted MSEA-R5 evidence |
| Enumeration command | MSEA-R5 verified full mirror 425/425 and target subset 373/373; MSEA-R6 worker must spot-check route-specific source anchors rather than replay the full corpus |
| Manifest artifact or inline manifest | inline table: paired GC-018 `## Route Candidate Manifest`; planned route decision matrix |
| Processing ledger artifact or inline ledger | inline table: planned worker return route-evaluation ledger |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | inline table: planned MSEA-R6 route decision matrix |
| Unresolved items | route selection pending worker evaluation |
| Completion claim boundary | decision-only route selection; no runtime/provider/public/package/checker expansion |

## Corpus Completeness And Report Integrity

- Corpus task class: external repository route-decision worker dispatch from accepted MSEA evidence.
- Corpus root: `.private_reference/source_mirrors/opendatalab__MinerU/` plus accepted MSEA-R4/R5 artifacts.
- Snapshot time: 2026-07-02 local session.
- Enumeration command: `rg --files --hidden --no-ignore .private_reference/source_mirrors/opendatalab__MinerU`; MSEA-R5 accepted the source-mirror manifest evidence, so MSEA-R6 uses route-specific source-anchor spot checks and no full-corpus replay.
- Manifest artifact or inline manifest: paired GC-018 route candidate manifest.
- Manifest hash: inherited from MSEA-R5 worker return evidence; worker may recompute if using source mirror facts beyond listed anchors.
- Processing ledger artifact or inline ledger: planned MSEA-R6 worker return route-evaluation ledger.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE
- Reconciliation: manifest=7 route candidates; ledger_terminal=0 at dispatch before worker execution; exclusions=R5 full-corpus replay; unresolved=0.
- Unresolved files: 0
- Declared exclusions: no full 425-file replay and no 373-file replay; R5 already owns that manifest evidence.
- Unreadable or unsupported files: none known at dispatch.
- Aggregation check: all route candidates map to existing MSEA source evidence or source mirror anchors.
- Drift check: worker must verify source mirror commit still matches the index if reading source files directly.
- Output traceability: selected route must cite the worker return and route decision matrix.
- Adversarial verification: worker must compare route selection against R5 limits and MSEA-T3 parked checker conditions.
- Corpus verdict: PARTIAL

## Mandatory Blind-Spot Control Block

| Field | Disposition |
|---|---|
| Blind-spot control applicability | REQUIRED because this work order references source-mirror and legacy-reference boundaries. |
| Prior coverage basis | MSEA-R5 accepted 425/425 full mirror and 373/373 target subset evidence with declared PARTIAL limits. |
| MSEA-R6 coverage boundary | route-decision spot checks only; no full-corpus replay and no silent `NO_NEW_VALUE` conclusion. |
| Declared blind spot | worker must carry forward R5 model/utils and Docker hardware-variant limitations if relevant to route selection. |
| Required worker action | evaluate every route candidate and record selected outcome or blocker with source-backed evidence. |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| `output_files.md` and MSEA-T2/MSEA-R5 receipt evidence | concrete layer/output receipt vocabulary | DOCTRINE_ADAPTED | planned MSEA-R6 route decision matrix and existing MSEA-T2 advisory | worker may select receipt-schema contract drafting as a later documentation lane | no schema implementation or parser claim |
| RagFlow and other plugin integration evidence | shipped integration evidence and RAG handoff pressure | PACKAGE_CANDIDATE | planned route decision matrix and MSEA-T2 RAG-handoff owner surface | worker may recommend a later RAG handoff value probe | no plugin wiring, RAG write, or adapter execution |
| `llm_aided.py` title-correction provider surface | OpenAI-compatible client with caller-supplied credentials | RUNTIME_CANDIDATE | planned route decision matrix and MSEA-R5 owner delta | worker may park or recommend later provider/live-proof probe | no provider call or credential use |
| `s3.py` S3 reader storage surface | credential-requiring remote IO | RUNTIME_CANDIDATE | planned route decision matrix and MSEA-R5 owner delta | worker may park or recommend later credential-boundary probe | no S3 connection or credential storage |
| MSEA-T3 and conditional reopen index checker rows | document-truth, runtime-readiness, and RAG-handoff checker candidates | CHECKER_CANDIDATE | conditional reopen index and planned route decision matrix | worker may hold unless concrete reopen conditions are met | no checker implementation or hook wiring |
| Direct upstream implementation source | source informs CVF-native decisions but is not CVF implementation | REJECT_DIRECT_IMPORT | planned route decision matrix | worker rejects direct copy/import | no source import or direct wiring |
| Full-corpus replay after R5 | R5 already reconciled the full mirror and target subset | NO_PACKAGE_OR_RUNTIME_VALUE | MSEA-R5 accepted worker return | worker avoids replay unless drift is detected | no runtime or package behavior |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| Receipt schema route | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md`; `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` | ENRICH_EXISTING | route is concrete enough for decision but not implementation | evaluate as route option |
| RAG handoff route | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | ENRICH_EXISTING | RagFlow evidence strengthens earlier generic RAG value | evaluate as route option |
| Provider-assisted title route | `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` | NEW_FINDING | provider-call surface exists outside CLI entry points | park or recommend later live-proof probe |
| S3 storage route | `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` | NEW_FINDING | credential-handling surface exists | park or recommend later credential-boundary probe |
| Checker route | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md` | CONFIRMED_EXISTING | parked checker rows remain current unless reopen evidence is found | evaluate conditions, do not duplicate rows |
| Direct source import | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | REJECT_DIRECT_IMPORT | external source remains advisory input only | reject direct import |
| Full R5 replay | `docs/reviews/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_WORKER_RETURN_2026-07-02.md` | NO_NEW_VALUE | replay adds no decision value unless drift exists | avoid replay |

## Source Mirror Migration Control

| Field | Disposition |
|---|---|
| Legacy source path | Legacy adapter folder remains secondary historical material and is not source authority for MSEA-R6. |
| Source mirror path | `.private_reference/source_mirrors/opendatalab__MinerU/` |
| Mirror index row | `.private_reference/source_mirrors/INDEX.md` row `opendatalab__MinerU` |
| Pinned upstream commit | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` |
| Migration disposition | SOURCE_MIRROR_AUTHORITY_RETAINED_FOR_THIS_TRANCHE |
| Legacy cleanup disposition | LEGACY_REFERENCE_ONLY_WITH_REASON: historical comparison only; source facts must prefer the pinned mirror or governed MSEA artifacts |
| Claim boundary | source-mirror authority control only; no source import, install, runtime execution, provider/live proof, public-sync, checker implementation, or production-readiness claim |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Storage action | N/A with reason: MSEA-R6 creates one worker return and one route decision matrix in existing governed folders only. |
| Folder/index impact | No new folder, stable reference family, front door, storage layout, or dated duplicate standard is authorized. |
| Durable foundation impact | The route decision matrix is a tranche-specific reference artifact, not a central foundation standard. |
| Required boundary | Worker must not create or relocate foundation storage, index, template, standard, or front-door files. |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: MSEA-R6 routes the freshly cloned MinerU source
mirror under `.private_reference/source_mirrors/opendatalab__MinerU/`, not a
legacy absorption folder. The legacy coverage index
`docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` is not the
owner surface for this tranche. The work order retains the legacy folder only
as a forbidden-scope boundary and historical-reference warning.

## Work-Order Fulfillment Manifest

| Required output | Path or evidence | Owner | Required status |
|---|---|---|---|
| Worker return | `docs/reviews/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_AND_ADAPTER_READINESS_SELECTION_WORKER_RETURN_2026-07-02.md` | worker | created, uncommitted, gate-checked |
| Route decision matrix | `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md` | worker | created, uncommitted, source-backed |
| Selected routing outcome | worker return and route matrix | worker | exactly one allowed outcome or `BLOCKED_SOURCE_CONTRADICTION` |
| No-commit evidence | worker return | worker | HEAD unchanged and no commit/stage/push |

## Worker Return Packet Shape Contract

| Field | Requirement |
|---|---|
| workerReturnPath | `docs/reviews/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_AND_ADAPTER_READINESS_SELECTION_WORKER_RETURN_2026-07-02.md` |
| contractProfile | WORKER_RETURN_FULL_GATE_V1 |
| requiredGate | `python governance/compat/run_worker_return_fast_gate.py` |
| individualCheckerSubstitution | FORBIDDEN |
| workerReturnSkeleton | CHECKER_SAFE_SKELETON_REQUIRED |
| requiredSections | Purpose; Scope / Methodology; Findings / Position; Risk / Corrective Action; Claim Boundary; Checker Source Read-Ahead Block; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; External Knowledge Intake Routing; Corpus Completeness And Report Integrity; Finding-To-Governance Learning Disposition; Epistemic Process Block; git status --short; Changed Files; Command Evidence; No-Commit Statement |
| literalTrapAvoidance | do not cite never-created optional review paths as parseable path evidence; use prose for optional reviewer decisions |

contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Evidence Requirements

- Worker return must cite execution base, source mirror HEAD, selected route,
  route-candidate evidence, gate output, changed files, and no-commit evidence.
- Route decision matrix must cite all seven route candidates and exactly one
  selected outcome or `BLOCKED_SOURCE_CONTRADICTION`.
- Any held or future implementation route must include concrete reopen
  conditions and forbidden-expansion boundaries.
- Evidence must come from governed CVF artifacts, the pinned source mirror, or
  checker output, not provider-local memory.

## Execution Plan

1. Capture `executionBaseHead`, `git status --short`, and source mirror HEAD.
2. Read required first reads and compare R5 route candidates against current
   session next move and MSEA-T3 parked checker conditions.
3. Evaluate all seven route candidates with a source-backed score or
   disposition.
4. Create the worker return with selected routing outcome, evidence table,
   claim boundary, command evidence, no-commit evidence, and all required
   worker-return sections.
5. Create the route decision matrix with exactly one selected route and
   concrete next-action boundary.
6. Run required gates or return a classified blocker.

## Acceptance Criteria

- Planned worker return exists and records `executionBaseHead`, source mirror
  HEAD, route-candidate evaluation, exactly one selected outcome, actual
  `git status --short`, and no-commit evidence.
- Planned route decision matrix exists and records selected outcome,
  alternatives, reopen conditions, and forbidden expansions.
- The worker evaluates all seven non-blocker route candidates and does not
  silently drop provider/S3/RAG/checker candidates.
- Any implementation-looking route remains future-only with fresh GC-018,
  source verification, and live/provider proof where behavior is claimed.
- No source mirror payload, runtime source, session state, handoff, checker,
  public-sync, or extension path is edited by the worker.

Fail conditions:

- source mirror commit differs from dispatch and no reviewer-supplied fresh
  source authority exists;
- worker creates runtime/provider/S3/RAG/Docker/checker/package/Web/MCP/source
  implementation or claims production readiness;
- selected outcome is not one of the allowed routing outcomes;
- route decision matrix omits a concrete next-action boundary;
- worker commits, stages, pushes, or edits forbidden paths.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` instead of continuing if the source mirror commit
differs, required source files are missing, a route requires runtime/provider/
credential/public/checker scope, source evidence contradicts MSEA-R5, gates
cannot pass inside allowed scope, or the worktree contains unrelated dirty
paths that cannot be isolated.

## Closure Checklist

- [x] Work order names worker write ownership.
- [x] Worker return and route decision matrix are the only worker-owned output
  paths.
- [x] Source verification, external absorption, corpus, blind-spot, handoff,
  AOT, Delta, ADIF, and worker-return shape controls are present.
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
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_source_mirror_migration.py`; `governance/compat/check_corpus_completeness_report_integrity.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `External knowledge intake routing: REQUIRED`; `External absorption core: REQUIRED`; `## Dispatch Prompt Envelope`; `## Source Verification Block`; `## Current Runtime Freshness Verification`; `## Negative Search And Collision Discipline`; `## Agent Handoff Contract Control Block`; `## Reviewer Closure Conversion`; `## Work-Order Fulfillment Manifest`; `## Worker Return Packet Shape Contract`; `WORKER_RETURN_FULL_GATE_V1`; `requiredGate:`; `individualCheckerSubstitution: FORBIDDEN`; `workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED`; `## External Knowledge Intake Routing`; `## External Absorption Core`; `## Corpus Completeness And Report Integrity`; `## External Absorption Value Conversion Matrix`; `## Overlap And Novelty Classification`; `DEFERRED_PRIVATE_ONLY`; `CLAIM_REJECTED_NO_RECEIPT`; `CLAIM_REJECTED_NO_ACTION` |
| gateRunPurpose | confirmation/evidence run for MSEA-R6 dispatch after checker read-ahead, not first discovery |
| claimBoundary | checker read-ahead proves dispatch authoring diligence only; worker completion and any runtime/provider/public/package/checker behavior remain unproved and unauthorized |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R6 --title "MinerU Application Route Decision And Adapter Readiness Selection" --date 2026-07-02 --base 088fdcb4 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "MSEA-R5 accepted at 1bac8163; operator selected next MinerU route decision after high-value document/layer scan absorption" --include-worker-return-skeleton --stdout` |
| generatedProfile | packet-kind=generic-worker-dispatch; commit-mode=WORKER_MUST_NOT_COMMIT; worker-return skeleton requested |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced scaffold fields with MSEA-R6 route-decision scope, source verification, route candidate matrix, external absorption blocks, migration control, no-commit worker shape, and verification commands |
| checkerReadAheadConfirmation | read guard orientation, literal-format gotchas, work-order template, external absorption standards, source mirror index, MSEA-R5 artifacts, and applicable checker source paths before writing |
| docOnlyNewFields | selected routing outcome vocabulary; route decision matrix path; route evaluation requirements |
| claimBoundary | scaffold provenance supports dispatch authoring only; no worker completion, runtime/provider/live/public/package/Web/MCP/model-router/action-authority, checker, or production claim |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher |
| Provider or surface | local workspace |
| Session or invocation | MSEA-R6 dispatch authoring, 2026-07-02 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, git, apply_patch, governance checkers |
| Target paths | `docs/baselines/CVF_GC018_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_AND_ADAPTER_READINESS_SELECTION_2026-07-02.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_AND_ADAPTER_READINESS_SELECTION_2026-07-02.md` |
| Allowed scope source | operator request to issue the next MinerU work order after MSEA-R5 acceptance |
| Before status evidence | clean worktree at `088fdcb4`; planned MSEA-R6 paths absent before authoring |
| After status evidence | dispatch baseline and work order created with source verification and pending pre-dispatch gates |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | dispatcher authoring only; worker execution remains no-commit |
| Claim boundary | no runtime/provider/public/source-import/Web/MCP/model-router/checker/package/action-authority claim |
| Agent type | dispatcher |
| Invocation ID | `msea-r6-mineru-application-route-decision-dispatch-2026-07-02` |
| Expected manifest | baseline and work order paths named above |
| Actual changed set | baseline and work order paths named above |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in dispatch artifact creation |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | MSEA-R6 route-decision work order |
| claimDisposition | CLAIM_REJECTED: no Delta runtime execution-control claim is made |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed |
| invocationBoundary | local authoring, source verification, and governance checker invocation only |
| interceptionBoundary | no runtime interception, parser execution, provider invocation, S3 access, or action-control behavior |
| claimLanguage | source-backed decision-route dispatch only |
| forbiddenExpansion | no runtime/provider/live/public/package/Web/MCP/model-router/action-authority, automatic invocation, checker implementation, source import, credential handling, or production-readiness claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: MSEA-R6 dispatch is private provenance route-decision work derived from
private source-mirror absorption evidence. No public-sync artifact is created
or authorized by this work order.

## Claim Boundary

MSEA-R6 authorizes a no-commit worker to select or hold the next MinerU route
from existing source-backed evidence. It does not authorize or claim MinerU
runtime integration, parser execution, OCR execution, VLM/hybrid backend
routing, remote backend processing, model download, API/router/Gradio service,
Docker deployment, RAG indexing, provider/live proof, S3 access, credential
handling, document truth verification, parser accuracy, table/formula
correctness, public-sync export, checker enforcement, package activation,
certification, generated aggregate mutation, production readiness, hosted
readiness, model-router behavior, action authority, or universal document
intelligence.
