# CVF Agent Work Order - MSEA-R4 MinerU Upstream Source Mirror Absorption

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-07-02

docType: work_order

Batch ID: MSEA-R4

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: 4d6cd237

External knowledge intake routing: REQUIRED

External absorption core: REQUIRED

## Dispatch Prompt Envelope

Role: no-commit worker for MSEA-R4 MinerU upstream source mirror absorption.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-07-02.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

Base: capture `executionBaseHead` with `git rev-parse --short HEAD` before
edits. Expected dispatch base is `4d6cd237` or the reviewer-provided current
dispatch commit if this packet is committed first.

Current-time notes: current date is 2026-07-02; upstream MinerU is pinned at
`3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`; use the fresh source mirror as
upstream authority and do not substitute older local source-copy facts for
current mirror facts.

Required first actions: read startup surfaces, this work order, the GC-018
baseline, external absorption standards, source mirror index, prior MSEA-T0,
MSEA-T1, MSEA-T2, and MSEA-T3 artifacts, then enumerate the pinned upstream
source mirror before writing conclusions.

Return contract: return `COMPLETE_PENDING_REVIEW`,
`COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, or `BLOCKED_WITH_REASON` with
actual changed paths, executionBaseHead, source mirror commit, manifest count,
manifest hash, processing ledger, value-conversion matrix, overlap/novelty
classification, gate results, and HEAD unchanged.

Do-not-misread notes: this work order does not authorize MinerU install, model
download, OCR/VLM/hybrid execution, parser run, API/router/Gradio/WebUI/server,
Docker, REST/API call, remote or OpenAI-compatible server routing, RAG index
write, benchmark, provider/live proof, public-sync, direct source import,
checker implementation, package activation, model-router work, action authority,
automatic invocation, or production-readiness claims.

## Purpose

Run a source-mirror-backed MinerU absorption pass against the current upstream
repository. The worker must produce a worker-return review and CVF-owned
owner-surface delta that compares current upstream value against MSEA-T0/T1/T2/T3
without activating runtime.

## Mission

Read and disposition the pinned upstream mirror:

`.private_reference/source_mirrors/opendatalab__MinerU/`

Pinned commit:

`3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`

Create:

1. `docs/reviews/CVF_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_WORKER_RETURN_2026-07-02.md`
2. `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md`

The worker must not commit.

## Authority Chain

| Authority | Path or source | Disposition |
|---|---|---|
| Operator instruction | chat request on 2026-07-02 to clone MinerU fresh into source mirrors and create the work order | ACCEPT |
| GC-018 baseline | `docs/baselines/CVF_GC018_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-07-02.md` | ACCEPT |
| Active session front door | `CVF_SESSION_MEMORY.md` | ACCEPT |
| Bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | ACCEPT |
| Active state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V31_2026-07-02.md` | ACCEPT |
| Guard orientation | `docs/reference/guard_orientation/README.md` | ACCEPT |
| Literal-format gotchas | `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | ACCEPT |
| External absorption front door | `docs/reference/external_agent_review/README.md` | ACCEPT |
| External absorption chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | ACCEPT |
| External absorption core standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | ACCEPT |
| Source mirror index | `.private_reference/source_mirrors/INDEX.md` | ACCEPT |
| Prior MSEA-T0 roadmap | `docs/roadmaps/CVF_MSEA_T0_MINERU_STRUCTURED_EXTRACTION_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` | ACCEPT |
| Prior MSEA-T1 baseline | `docs/baselines/CVF_GC018_MSEA_T1_SOURCE_VERIFIED_DOCUMENT_EXTRACTION_RECONCILIATION_2026-06-28.md` | ACCEPT |
| Prior MSEA-T2 advisory | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | ACCEPT |
| Prior MSEA-T3 closeout | `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | ACCEPT |

Authority boundary:

- External MinerU source is advisory input only.
- The pinned source mirror is preferred for upstream facts.
- Prior MSEA artifacts are CVF-owned comparison surfaces.
- Any runtime, package activation, checker, resolver, CLI/MCP adapter, public
  output, provider/live proof, parser run, model download, RAG write, or
  benchmark requires a later fresh governed tranche.

## Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | author source-verified dispatch packet and run pre-dispatch gates |
| Worker | no-commit worker role | produce the worker return and owner-surface delta without committing |
| Reviewer/closer | Codex | review returned artifacts, repair allowed-scope defects, and commit if accepted |
| Session-sync steward | Codex after material acceptance | update active continuity only after accepted material commit if next move changes |
| Operator checkpoint | operator | required for runtime, package activation, checker implementation, public-sync, MinerU install/run, model download, benchmark, or live/provider proof |

## Scope

Allowed write scope for worker:

- `docs/reviews/CVF_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_WORKER_RETURN_2026-07-02.md`
- `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md`

Allowed read scope:

- startup files and current handoff;
- this work order and GC-018 baseline;
- external absorption standards and source mirror index;
- the pinned MinerU source mirror;
- prior MSEA-T0/T1/T2/T3 artifacts;
- historical legacy adapter material only if needed for comparison, never as
  upstream source authority.

Forbidden scope:

- no edits to source mirror payload, `.private_reference/legacy/`, `EXTENSIONS/`,
  runtime source, `governance/compat/`, hooks, CI, scripts, active session
  state, active handoff, or public-sync files;
- no MinerU install, model download, OCR/VLM/hybrid execution, parser run,
  API/router/Gradio/WebUI/server, Docker run, REST/API call, remote or
  OpenAI-compatible server routing, RAG index write, benchmark, provider/live
  proof, public-sync, direct source import, package activation, checker
  implementation, model-router work, action authority, automatic invocation, or
  production-readiness claim;
- no commit by the worker.

Risk ceiling: R0 documentation/reference only.

## Required First Reads

Before writing output, the worker must read:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V31_2026-07-02.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- this work order and its GC-018 baseline
- external absorption front door, chain map, and core standard
- `.private_reference/source_mirrors/INDEX.md`
- prior MSEA-T0, MSEA-T1, MSEA-T2, and MSEA-T3 artifacts

## Pre-Flight Checks

Before implementation, the worker must verify the source mirror exists, the
mirror commit matches this packet, the worktree status is captured, and the
pre-implementation autorun gate either passes or returns a classified blocker.

## Write Ownership

Worker write ownership is limited to the two planned output files named in the
Mission section. Reviewer/closer owns any accepted material commit. Session-sync
steward owns later continuity updates only after material acceptance.

## Evidence Requirements

The worker return must include command-backed source mirror commit, remote, file
count, manifest hash, file-level or grouped processing ledger, value conversion
matrix, overlap/novelty classification, owner-surface delta, gate outputs,
actual `git status --short`, and HEAD unchanged evidence.

## Execution Plan

1. Capture `executionBaseHead` and `git status --short`.
2. Verify source mirror remote, pinned commit, tracked count, and manifest hash.
3. Read MSEA-T0/T1/T2/T3 and classify current upstream MinerU value against them.
4. Create the worker return with manifest, processing ledger, value conversion,
   overlap classification, claim boundary, command evidence, and no-commit
   evidence.
5. Create the owner-surface delta with only CVF-owned conclusions and candidate
   reopen conditions.
6. Run required gates or return a classified blocker.

## Acceptance Criteria

- Planned worker return exists and contains source mirror commit, count, hash,
  processing ledger, value conversion, overlap classification, command evidence,
  and no-commit evidence.
- Planned owner-surface delta exists and cites only source mirror or
  CVF-governed authority.
- All runtime, package, checker, public, provider/live, RAG, model-router,
  action-authority, direct-import, and production claims remain rejected or
  candidate-only.
- Worker leaves artifacts uncommitted and records actual `git status --short`.

## Review Gate

Reviewer/closer must run worker-return fast gate, external absorption/corpus
guards, reviewer-fast or pre-closure gates, and commit steward preflight before
accepting or committing the worker output. Gate failure blocks closure until
repaired inside allowed scope or returned with a blocker.

## Closure Checklist

- [x] Dispatch packet names authority, source mirror, scope, and worker outputs.
- [x] Dispatch packet forbids runtime, package, checker, public, provider, direct-import, and production-readiness work.
- [x] Worker must return manifest reconciliation or a classified blocker.
- [x] Reviewer must run review gates before closure or commit.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when all required worker artifacts and
gate evidence are present. Return `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`
only when limitations are explicit and reconciled. Return `BLOCKED_WITH_REASON`
when source, scope, or gate blockers prevent bounded completion.

## Operator Checkpoint

Operator checkpoint is required before any runtime execution, MinerU install or
parser run, model download, package activation, checker implementation,
public-sync, provider proof, benchmark, RAG write, or scope expansion beyond
the two planned worker files.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, surfaceSelector=`docs/work_orders`, riskCeiling=`HIGH`, maxResults=`20`

Returned defects: NONE_RETURNED

Disclosure note: dispatcher invoked `python governance/compat/run_adif_defect_resolver.py --task-class "work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch`; the resolver returned `totalCandidates=0`.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_source_mirror_migration.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `External knowledge intake routing: REQUIRED`; `External absorption core: REQUIRED`; `## Source Verification Block`; `## External Knowledge Intake Routing`; `## External Absorption Core`; `## Corpus Completeness And Report Integrity`; `## External Absorption Value Conversion Matrix`; `## Overlap And Novelty Classification`; `## Source Mirror Migration Control`; `## Agent Handoff Contract Control Block`; `## Reviewer Closure Conversion`; `contractProfile: WORKER_RETURN_FULL_GATE_V1`; `requiredGate:`; `run_worker_return_fast_gate.py`; `individualCheckerSubstitution: FORBIDDEN`; `workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED`; `DEFERRED_PRIVATE_ONLY`; `CLAIM_REJECTED_NO_RECEIPT`; `CLAIM_REJECTED_NO_ACTION` |
| gateRunPurpose | confirmation/evidence run for MSEA-R4 no-commit worker dispatch after checker read-ahead, not first discovery |
| claimBoundary | checker read-ahead proves authoring diligence only; worker completion and runtime/provider/public/package/checker behavior remain unproved and unauthorized |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Active handoff is V31 for this resumed session | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | `activeHandoff` | `AGENT_HANDOFF_V31_2026-07-02.md` | active session state registry | VALUE_SET | ACCEPT |
| MSEA-R4 uses the fresh source mirror rather than older source copies | `.private_reference/source_mirrors/INDEX.md` | Mirror Ledger row | `opendatalab__MinerU` | source mirror index | VALUE_SET | ACCEPT |
| MinerU mirror is pinned to upstream commit | `.private_reference/source_mirrors/INDEX.md` | Mirror Ledger row | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` | source mirror index | VALUE_SET | ACCEPT |
| MinerU mirror contains 425 tracked files at dispatch | `.private_reference/source_mirrors/INDEX.md` | Mirror Ledger row | `Tracked file count` | source mirror index | VALUE_SET | ACCEPT |
| External repo intake must route through manifest, ledger, owner map, and value conversion | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | Central Core; Required Artifact Block; Required Value Conversion Matrix | `External Absorption Core` | external absorption core standard | VALUE_SET | ACCEPT |
| High-value upstream repo absorption should use a source mirror when available | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | Source Mirror Discipline | `.private_reference/source_mirrors/` | external absorption core standard | LITERAL_INVARIANT | ACCEPT |
| MinerU package identity is visible in upstream package metadata | `.private_reference/source_mirrors/opendatalab__MinerU/pyproject.toml` | line 6; line 10 | `name`; `description` | pyproject metadata | VALUE_SET | ACCEPT |
| MinerU declares VLM, pipeline, and Gradio extras | `.private_reference/source_mirrors/opendatalab__MinerU/pyproject.toml` | lines 74-111 | `vlm`; `pipeline`; `gradio` | pyproject optional dependencies | VALUE_SET | ACCEPT |
| MinerU declares CLI/API/router/model-download/server entry points | `.private_reference/source_mirrors/opendatalab__MinerU/pyproject.toml` | lines 129-136 | `mineru`; `mineru-api`; `mineru-router`; `mineru-models-download` | pyproject scripts | VALUE_SET | ACCEPT |
| MinerU README describes document conversion into Markdown and JSON | `.private_reference/source_mirrors/opendatalab__MinerU/README.md` | lines 49-51; lines 164-181 | `Markdown`; `JSON` | upstream README | VALUE_SET | ACCEPT |
| MinerU README describes MCP, RAG framework, CLI, REST API, Docker, and Gradio surfaces | `.private_reference/source_mirrors/opendatalab__MinerU/README.md` | lines 65-68; lines 316-339 | `MCP Server`; `CLI`; `REST API`; `Docker`; `Gradio`; `mineru-router` | upstream README | VALUE_SET | ACCEPT |
| MSEA-T0 closed bounded and forbade runtime, checker, package, provider, public, model download, API/router, VLM/OCR, RAG, and production claims | `docs/roadmaps/CVF_MSEA_T0_MINERU_STRUCTURED_EXTRACTION_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` | Status; Non-Goals; Current Runtime Freshness Verification | `CLOSED_PASS_BOUNDED` | MSEA-T0 roadmap | VALUE_SET | ACCEPT |
| MSEA-T2 is the current document-extraction claim-boundary and RAG handoff advisory | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | Status; External Knowledge Intake Routing | `ACTIVE_REFERENCE` | MSEA-T2 advisory | VALUE_SET | ACCEPT |
| MSEA-T3 closed the prior static-checker lane without building a checker | `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | Status; Claim Boundary; Machine Closure Package | `CLOSED_PASS_BOUNDED` | MSEA-T3 closeout | VALUE_SET | ACCEPT |

## New Doc-Only Fields Table

| New doc-only file | Purpose | Runtime claim blocked? | Validation expectation |
|---|---|---|---|
| `docs/reviews/CVF_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_WORKER_RETURN_2026-07-02.md` | worker-return upstream mirror absorption review with manifest, ledger, value conversion, overlap classification, and gates | Yes | worker-return fast gate plus external absorption/corpus guards |
| `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md` | CVF-owned delta surface for upstream MinerU concepts compared to MSEA-T0/T1/T2/T3 | Yes | reviewer-fast and external intake/value-conversion guards |

## Roadmap-To-Work-Order Trace Matrix

| Prior requirement or operator instruction | Work order response | Output artifact | Status |
|---|---|---|---|
| Operator requested a fresh MinerU clone into source mirrors instead of using old local source | dispatch source-mirror-backed MSEA-R4 worker review | worker return | DISPATCHED_BY_THIS_PACKET |
| MSEA-T0 closed bounded but preserved future work only through fresh GC-018 if reopen conditions are met | create fresh MSEA-R4 GC-018 and work order for upstream mirror reconciliation | this baseline and work order | DISPATCHED_BY_THIS_PACKET |
| MSEA-T2 owns document-extraction claim-boundary and RAG handoff doctrine | require comparison against MSEA-T2 before any new owner surface | owner-surface delta | DISPATCHED_BY_THIS_PACKET |
| MSEA-T3 found no checker now and parked runtime/parser/proof ideas | require candidate-only classification and concrete future reopen conditions | worker return | DISPATCHED_BY_THIS_PACKET |
| Runtime/MCP/package/checker remain parked | forbid implementation and require candidate-only classification | claim boundary and value matrix | DISPATCHED_BY_THIS_PACKET |

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake type | external repo source-mirror absorption |
| Intake summary | operator selected MinerU upstream source after fresh source mirror clone; dispatch pins upstream source mirror before worker absorption |
| Scope classification | bounded documentation/reference worker; source mirror payload is read-only and ignored by git |
| Risk sensitivity | low runtime risk if forbidden scope is obeyed; high governance risk if worker overclaims runtime, MCP, package, checker, provider, public, parser, OCR, RAG, model-download, or production value |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | worker returns uncommitted material artifacts to reviewer/closer; session-sync steward acts only after material acceptance |
| Worker role | no-commit documentation/reference worker |
| Reviewer role | reviewer/closer after worker return |
| Runtime role | NOT_APPLICABLE_WITH_REASON: runtime implementation is forbidden in MSEA-R4 |
| Package role | NOT_APPLICABLE_WITH_REASON: package mutation is forbidden in MSEA-R4; package value is classification only |
| Checker role | NOT_APPLICABLE_WITH_REASON: checker implementation is forbidden in MSEA-R4; checker value is classification only |
| Escalation condition | return `BLOCKED_WITH_REASON` if source mirror is missing, pinned commit drifts, source authority files are missing, or completion would require forbidden scope |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| contractSource | archive `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` ratified contract path used only as AHB central-core authority |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | dispatcher -> worker -> reviewer/closer -> session-sync steward |
| phase | DISPATCH_AUTHORING; EXECUTION; REVIEWER_CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | dispatchBaseHead=`4d6cd237`; executionBaseHead=worker captures with `git rev-parse --short HEAD`; closureBaseHead=reviewer captures before material commit |
| changedSetScope(phase) | worker may change only the planned MSEA-R4 worker return and owner-surface delta |
| traceScope(phase, actor) | worker return must include Agent Operation Trace Block with expected and actual manifest |
| commitOwner(phase) | worker must not commit; reviewer/closer owns material commit if accepted; session-sync steward owns separate session-sync commit if needed |
| crossBatchIsolation | clean worktree before dispatch authoring was confirmed by `git status --short` returning no entries; worker material artifacts must not be mixed with session/handoff sync or runtime/package/checker work |
| nextMoveSurfaces | worker must not edit; reviewer/session-sync steward updates after accepted material commit if next move changes |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_COMPLETION_2026-07-02.md` |
| reviewerOwnedClosurePaths | worker return and owner-surface delta only; session-sync paths remain separate |

## Current Runtime Freshness Verification

| Claim checked | Verification command | Observed result | Disposition |
|---|---|---|---|
| Fresh upstream source mirror exists | `Test-Path '.private_reference/source_mirrors/opendatalab__MinerU/.git'` | `True` | ACCEPT |
| Source mirror remote points to upstream MinerU | `git -C .private_reference/source_mirrors/opendatalab__MinerU remote get-url origin` | `https://github.com/opendatalab/MinerU.git` | ACCEPT |
| Source mirror HEAD is pinned for dispatch | `git -C .private_reference/source_mirrors/opendatalab__MinerU rev-parse HEAD` | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` | ACCEPT |
| CVF did not install or execute MinerU for this dispatch | dispatch command log | only read/enumeration/scaffold/checker commands used | ACCEPT |
| Prior MSEA runtime/checker lanes remain bounded/closed | prior MSEA-T0/T2/T3 artifacts | documentation/reference only; no runtime or checker authorization | ACCEPT |

Freshness boundary: these checks support only source-mirror and negative
runtime claim boundaries for MSEA-R4 dispatch. They do not authorize execution
or prove parsing quality, OCR correctness, document truth, RAG suitability, or
production readiness.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | MSEA-R4 worker return and owner-surface delta | internal CVF agents may read reference output only; no action authority | this work order and baseline | N/A with reason: no internal runtime adapter is implemented | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | future CLI/MCP adapter owner, not MSEA-R4 | external agent use requires separate source-verified adapter/runtime authorization | upstream MinerU advertises MCP and CLI/API surfaces, but CVF has not implemented them | deferred adapter owner; no ingress, auth, mutation, raw-data, receipt, or public boundary is implemented here | DEFERRED_WITH_REASON |

## Worker Autonomy / No-Question Rule

The worker proceeds without operator confirmation for non-destructive actions
inside Allowed scope: reading files, enumerating the mirror, creating the two
planned artifacts, repairing format defects inside those artifacts, and rerun
of applicable gates.

Escalation is reserved for missing mirror, missing authority files, unreadable
source that prevents a bounded conclusion, request to install/run MinerU,
model download, live/provider proof, public-sync, package/checker/runtime
implementation, session-state edits, destructive actions, or scope expansion.

## External Absorption Core

| Field | Value |
|---|---|
| Standard | docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md |
| Input root or repository | `https://github.com/opendatalab/MinerU.git` at `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`; local mirror `.private_reference/source_mirrors/opendatalab__MinerU/` |
| Enumeration command | `Get-ChildItem -LiteralPath ".private_reference/source_mirrors/opendatalab__MinerU" -Recurse -File -Force` excluding `.git` |
| Manifest artifact or inline manifest | inline `## Dispatch Source Mirror Manifest` table in this file; worker must create full manifest in planned worker return |
| Processing ledger artifact or inline ledger | planned worker return under `docs/reviews/CVF_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_WORKER_RETURN_2026-07-02.md` |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | planned `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md` |
| Unresolved items | 425 unresolved at dispatch; worker must reduce to 0 or return with limitations/blocker |
| Completion claim boundary | dispatch and source-mirror intake only; no runtime, provider/live, public, production, OCR/VLM/hybrid execution, model download, API/router/Gradio, Docker, RAG write, checker, package activation, model-router, or action-authority claim |

## Corpus Completeness And Report Integrity

- Corpus task class: upstream external repository absorption dispatch.
- Corpus root: `.private_reference/source_mirrors/opendatalab__MinerU/`.
- Snapshot time: 2026-07-02 local session.
- Enumeration command: `Get-ChildItem -LiteralPath ".private_reference/source_mirrors/opendatalab__MinerU" -Recurse -File -Force` excluding `.git`.
- Manifest artifact or inline manifest: dispatch preflight count and hash recorded here; full manifest required in worker return.
- Manifest hash: `sha256:3a0ad960e1d8fc663c5f099c27f8416a0b2d8147718e9788ee298dd653da6a81`.
- Processing ledger artifact or inline ledger: planned worker return.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE
- Reconciliation: manifest=425; ledger_terminal=0 at dispatch; exclusions=0; unresolved=425.
- Unresolved files: 425 at dispatch.
- Declared exclusions: none at dispatch.
- Unreadable or unsupported files: none known at dispatch.
- Aggregation check: dispatch proves source mirror availability, not absorption completion.
- Drift check: worker must recompute count, commit, and manifest hash before processing.
- Output traceability: worker maps accepted value to CVF owner surfaces or returns blocked source gaps.
- Adversarial verification: prior MSEA-T0/T1/T2/T3 conclusions must be challenged against the current 425-file upstream mirror.
- Corpus verdict: PARTIAL

## Dispatch Source Mirror Manifest

| Manifest item | Evidence |
|---|---|
| Upstream repository | `https://github.com/opendatalab/MinerU.git` |
| Pinned commit | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` |
| Local mirror path | `.private_reference/source_mirrors/opendatalab__MinerU/` |
| Tracked file count | 425 |
| Manifest hash | `sha256:3a0ad960e1d8fc663c5f099c27f8416a0b2d8147718e9788ee298dd653da6a81` |
| Full file-level manifest | REQUIRED in planned worker return |

## Mandatory Blind-Spot Control Block

| Field | Disposition |
|---|---|
| fullMirrorEnumeration | REQUIRED: worker must enumerate all 425 tracked files and reconcile count/hash drift |
| highValueSampling | REQUIRED: README, pyproject, package metadata, CLI/API surfaces, docs, tests, and deployment files must be sampled before value conclusions |
| noSilentNoValue | REQUIRED: any `NO_PACKAGE_OR_RUNTIME_VALUE` row must name why it adds no CVF delta |
| noRuntimeShortcut | REQUIRED: runtime-looking value must be parked as candidate-only unless a later fresh work order authorizes execution |
| predecessorChallenge | REQUIRED: worker must compare current mirror facts against MSEA-T0/T1/T2/T3 and record confirmed, enriched, or rejected deltas |

## Source Mirror Migration Control

| Field | Disposition |
|---|---|
| Legacy source path | Legacy external repo clone and legacy adapter folder are not source authority for MSEA-R4; this dispatch uses the fresh source mirror instead. |
| Source mirror path | `.private_reference/source_mirrors/opendatalab__MinerU/` |
| Mirror index row | `.private_reference/source_mirrors/INDEX.md` row `opendatalab__MinerU` |
| Pinned upstream commit | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` |
| Migration disposition | MIGRATED_TO_SOURCE_MIRROR_AUTHORITY_FOR_THIS_TRANCHE |
| Legacy cleanup disposition | LEGACY_REFERENCE_ONLY_WITH_REASON: older local copies may be read only if needed for historical comparison and must not override current upstream facts |
| Claim boundary | source-mirror authority control only; no source import, package install, runtime execution, provider/live proof, public-sync, checker implementation, or production-readiness claim |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | external repo or copied folder -> pinned source mirror -> external absorption core -> full manifest and processing ledger -> value conversion matrix -> CVF owner-surface delta -> future package/runtime/checker work order only if separately authorized |
| Matching local-view guard | `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_source_mirror_migration.py` |
| Owner surface | `docs/baselines/CVF_GC018_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-07-02.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-07-02.md` |
| Disposition | DISPATCH upstream source-mirror absorption review |
| Claim boundary | dispatch only; no runtime, package activation, checker wiring, provider/live proof, public-sync, MCP server, API/router/Gradio, Docker, model download, OCR/VLM/hybrid execution, RAG write, benchmark, or production-readiness claim |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| Upstream source mirror control plane | Current MinerU source authority is pinned for future absorption. | DOCTRINE_ADAPTED | `.private_reference/source_mirrors/INDEX.md` | Use upstream mirror as source authority for MSEA-R4 facts. | No runtime or package behavior |
| README and pyproject document-conversion claims | MinerU describes multi-format document parsing into Markdown/JSON for downstream retrieval and extraction. | DOCTRINE_ADAPTED | planned MSEA-R4 owner-surface delta and existing MSEA-T2 advisory | Worker maps deltas to CVF extraction-foundation language. | Documentation/reference only |
| CLI/API/router/Gradio/Docker/server/model-download/VLM/OCR/hybrid surfaces | Upstream exposes executable surfaces, but CVF has not authorized execution. | RUNTIME_CANDIDATE | planned worker return and MSEA conditional reopen notes | Worker may classify value and reopen conditions only. | No install, execution, model download, API/router/Gradio, Docker, VLM/OCR/hybrid, or provider/live proof |
| MCP, RAG framework, SDK, and no-code integration claims | Upstream integration surfaces may become package or adapter candidates after separate authorization. | PACKAGE_CANDIDATE | planned worker return | Worker records candidate evidence only. | No package root, registry mutation, adapter, MCP/CLI integration, or activation |
| Claimed quality, OCR, parsing, table/formula, long-document, and concurrency behavior | Future guards may be valuable only if CVF identifies repeated real misses or authorized receipt gaps. | CHECKER_CANDIDATE | planned worker return and future reopen conditions | Worker may record candidate guard ideas with concrete triggers. | No checker implementation or hook wiring |
| Upstream source files, tests, workflows, and deployment recipes | Direct import remains unsafe and non-authoritative. | REJECT_DIRECT_IMPORT | CVF-native rewrite lanes only | Worker rejects direct copy/wiring and records reasons. | No direct source import |
| Duplicate, asset-only, marketing-only, or non-CVF-value files after full read | Some files may add no CVF-native doctrine/package/runtime/checker delta. | NO_PACKAGE_OR_RUNTIME_VALUE | worker ledger | Worker records explicit no-new-value reason. | No runtime or package behavior |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| Multi-format document extraction into Markdown/JSON | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | ENRICH_EXISTING | upstream mirror may refine receipt, output, and handoff language | worker enriches owner delta only |
| Runtime parser, OCR, VLM, hybrid, API, router, Docker, Gradio, model-download, remote-server surfaces | `docs/roadmaps/CVF_MSEA_T0_MINERU_STRUCTURED_EXTRACTION_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md`; `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | ENRICH_EXISTING | current upstream has more concrete runtime-candidate evidence than prior bounded closeout | worker parks with concrete reopen conditions |
| MCP/RAG/framework integration claims | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | ENRICH_EXISTING | integration claims may sharpen package/adapter candidate taxonomy | worker records candidate-only evidence |
| Direct upstream implementation source | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | REJECT_DIRECT_IMPORT | external source is not CVF authority or implementation | worker rejects direct import |
| Files that only restate already-owned MSEA doctrine | `docs/roadmaps/CVF_MSEA_T0_MINERU_STRUCTURED_EXTRACTION_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md`; `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md`; `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | NO_NEW_VALUE | no meaningful delta after worker comparison | worker closes row with reason |
| Any high-value source item without an existing CVF owner | OWNER_SURFACE_NOT_FOUND | OWNER_SURFACE_NOT_FOUND | worker must name source-backed gap rather than silently dropping value | worker records blocker or proposed future owner route |

## Required Proof Manifest Atomic Literal Discipline

| Field | Disposition |
|---|---|
| proofManifestMode | RECOMPUTE_REQUIRED |
| atomicLiteralRule | Worker must record source mirror commit, count, hash, gate commands, and git status as separate evidence rows without wrapping verdict tokens into prose-only claims. |
| claimBoundary | manifest literals prove review evidence shape only; they do not prove runtime parsing behavior or production readiness. |

## Provider Memory Authority Boundary

| Field | Disposition |
|---|---|
| providerMemoryUsedAsAuthority | NO |
| allowedUse | provider-local memory may guide the worker's operating context only after CVF-governed authority is read |
| requiredReverification | every source fact used in the worker return must cite the source mirror, CVF-governed reference, or work-order authority |
| forbiddenUse | provider memory must not be cited as Source Verification authority or closure proof |

## Work-Order Fulfillment Manifest

| Required output | Path or evidence | Owner | Required status |
|---|---|---|---|
| Worker return | `docs/reviews/CVF_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_WORKER_RETURN_2026-07-02.md` | worker | created, uncommitted, gate-checked |
| Owner-surface delta | `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md` | worker | created, uncommitted, source-backed |
| Source mirror manifest | worker return manifest section | worker | count/hash/commit recomputed |
| Processing ledger | worker return ledger section | worker | all 425 files reconciled or limitation/blocker classified |
| Value conversion matrix | worker return and owner delta | worker | conversion lanes populated with source-backed rows |
| Overlap classification | worker return and owner delta | worker | compared against MSEA-T0/T1/T2/T3 |
| No-commit evidence | worker return | worker | HEAD unchanged and no commit/stage/push |

## Worker Return Packet Shape Contract

| Field | Requirement |
|---|---|
| contractProfile | WORKER_RETURN_FULL_GATE_V1 |
| requiredGate | `python governance/compat/run_worker_return_fast_gate.py --base <executionBaseHead> --head HEAD --enforce` |
| individualCheckerSubstitution | FORBIDDEN |
| workerReturnSkeleton | CHECKER_SAFE_SKELETON_REQUIRED |
| requiredSections | Purpose; Scope / Methodology; Findings / Position; Risk / Corrective Action; Claim Boundary; Checker Source Read-Ahead Block; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; git status --short; Changed Files; Command Evidence; No-Commit Statement |
| conditionalSections | External Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance Learning Disposition; Epistemic Process Block; Machine Closure Package |
| sourceMirrorEvidence | remote URL, pinned commit, file count, manifest hash, and drift check |
| literalTrapAvoidance | do not cite never-created optional review paths as bare path evidence; use the planned worker return path and prose for optional reviewer-only artifacts |

contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py --base <executionBaseHead> --head HEAD --enforce`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
|---|---|
| Coverage index status | NOT_APPLICABLE_WITH_REASON |
| Canonical coverage index | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` |
| Reason | MSEA-R4 consumes a pinned upstream source mirror, not a legacy coverage-index closure wave |
| Controlling evidence | External Absorption Core, source mirror index, corpus completeness, and value conversion matrix in this work order |
| Required worker evidence | full upstream source-mirror manifest, processing ledger, value conversion matrix, overlap classification, and owner-surface delta |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation Storage Layout Block | N/A with reason: MSEA-R4 dispatch does not split, relocate, refactor, or redesign durable governance foundation files; it only dispatches source-mirror absorption artifacts |
| Protected storage paths | N/A with reason: no foundation storage topology path is changed |
| Follow-up condition | separate governed work order required before any storage-layout implementation |

## Verification Commands

Worker must run or return a classified blocker for:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_external_knowledge_intake_routing.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_external_absorption_core.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_external_absorption_value_conversion.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_external_absorption_overlap_discipline.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_corpus_completeness_report_integrity.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_source_mirror_migration.py --base <executionBaseHead> --head HEAD --enforce
```

Reviewer/closer must rerun appropriate review and pre-closure gates before any
material commit.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind source-intake --batch-id MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION --title "MSEA-R4 MinerU Upstream Source Mirror Absorption" --date 2026-07-02 --base 4d6cd237 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | packet-kind=source-intake; commit-mode=WORKER_MUST_NOT_COMMIT; worker-return skeleton requested |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced scaffold placeholders with MinerU source-mirror facts, MSEA predecessor surfaces, source verification, external absorption blocks, migration control, no-commit worker shape, and verification commands |
| checkerReadAheadConfirmation | read guard orientation, literal-format gotchas, work-order template, external absorption standards, scaffold provenance standard, worker-return quality standard, and applicable checker source paths before writing |
| docOnlyNewFields | planned worker return path; planned owner-surface delta path; MSEA-R4 manifest hash; source-mirror migration disposition; worker-return packet shape contract |
| claimBoundary | scaffold provenance supports dispatch authoring only; no worker completion, runtime/provider/live/public/package/Web/MCP/model-router/action-authority, checker, or production claim |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher |
| Provider or surface | local workspace |
| Session or invocation | MSEA-R4 dispatch authoring, 2026-07-02 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, git, apply_patch, governance checkers |
| Target paths | `docs/baselines/CVF_GC018_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-07-02.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-07-02.md` |
| Allowed scope source | operator request to create the MinerU work order after fresh source mirror clone |
| Before status evidence | clean worktree confirmed before dispatch authoring: `git status --short` was empty; planned MSEA-R4 paths returned `False` in negative search |
| After status evidence | dispatch baseline and work order created with source verification and pre-dispatch gates |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | dispatcher authoring only; worker execution remains no-commit |
| Claim boundary | no runtime/provider/public/source-import/Web/MCP/model-router/checker/package/action-authority claim |
| Agent type | dispatcher |
| Invocation ID | `msea-r4-mineru-upstream-source-mirror-dispatch-2026-07-02` |
| Expected manifest | baseline and work order paths named above |
| Actual changed set | baseline and work order paths named above |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in dispatch artifact creation |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | MSEA-R4 dispatch work order |
| claimDisposition | CLAIM_REJECTED: no Delta runtime execution-control claim is made |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed |
| invocationBoundary | local authoring, source-mirror enumeration, and governance checker invocation only |
| interceptionBoundary | no runtime interception, parser execution, provider invocation, or action-control behavior |
| claimLanguage | source-mirror dispatch and documentation/reference authorization only |
| forbiddenExpansion | no runtime/provider/live/public/package/Web/MCP/model-router/action-authority, automatic invocation, checker implementation, source import, or production-readiness claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: MSEA-R4 dispatch is private provenance source-mirror absorption work.
No public-sync artifact is created or authorized by this work order.

## Claim Boundary

MSEA-R4 authorizes a no-commit worker to read the pinned MinerU source mirror and
produce documentation/reference evidence only. It does not authorize or claim
MinerU runtime integration, parser execution, OCR execution, VLM/hybrid backend
routing, remote backend processing, model download, API/router/Gradio service,
Docker deployment, RAG indexing, document QA, document truth verification,
parser accuracy, table/formula correctness, public-sync export, checker
enforcement, package activation, certification, generated aggregate mutation,
production readiness, hosted readiness, model-router behavior, action authority,
or universal document intelligence.
