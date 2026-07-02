# CVF Agent Work Order - MSEA-R9 MinerU CVF Application Blueprint And Adapter Contract Readiness Selection

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work_order

Date: 2026-07-02

Batch ID: MSEA-R9

Dispatch base head: 89943d30

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: reviewer/closer role

Worker return path: `docs/reviews/CVF_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_SELECTION_WORKER_RETURN_2026-07-02.md`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA-R9.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_SELECTION_2026-07-02.md`

Paired GC-018 baseline: `docs/baselines/CVF_GC018_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_SELECTION_2026-07-02.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: worker must capture with `git rev-parse --short HEAD` before edits.

Current-time notes: artifact date is 2026-07-02; executionBaseHead must be
captured from the worker's actual starting HEAD, not copied from dispatch.

Do-not-misread notes: this work order is documentation/reference-only. It does
not authorize MinerU install, model download, parser/OCR/VLM/hybrid/API/router/
Gradio/Docker execution, provider/live calls, credential/S3 access, RAG writes,
source import, package activation, checker implementation, public-sync,
Web/MCP/model-router/action-authority, automatic invocation, benchmark,
document-truth, extraction-accuracy, or production-readiness claims.

Required first actions: read startup front doors, guard orientation, literal
gotchas, ADIF-0023, this work order, the paired GC-018 baseline, source files
named in Source Verification, and checker source for each output artifact
before writing any worker output. Create the worker-return skeleton first and
run the fast gate while the skeleton is still short.

Return contract: create the two planned output artifacts, run required gates,
leave changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`.

## Purpose

Create a CVF-owned MinerU application blueprint and adapter contract readiness
reference from accepted MSEA evidence. The worker must map practical CVF use
cases, receipt/quality/RAG prerequisites, adapter contract readiness levels,
and source-backed hold conditions, then select exactly one next route outcome
without opening any runtime, provider, package, public, checker, or adapter
implementation lane.

External knowledge intake routing: REQUIRED

External absorption core: REQUIRED

## Authority Chain

| Authority | Evidence | Disposition |
|---|---|---|
| Operator instruction | User approved creating this work order after MSEA-R8 and the worker-output checker-shape proposal | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` current mode and next allowed move | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V32_2026-07-02.md` records MSEA-R8 acceptance and no-runtime boundary | ACCEPT |
| GC-018 baseline | `docs/baselines/CVF_GC018_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_SELECTION_2026-07-02.md` | ACCEPT |
| Source mirror | `.private_reference/source_mirrors/INDEX.md` row `opendatalab__MinerU`; mirror HEAD `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`; 425 files | ACCEPT |
| Prior MSEA owner surfaces | MSEA-T2/R4/R5/R6/R7/R8 references and worker returns | ACCEPT |

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | dispatcher role | author source-verified dispatch packet and run pre-dispatch gates |
| Worker | delegated no-commit worker role | produce worker return and companion reference without committing |
| Reviewer/closer | reviewer/closer role | review returned artifacts, repair allowed-scope defects, and commit if accepted |
| Session-sync steward | session-sync steward role after material acceptance | update continuity after accepted material commit if next move changes |
| Operator checkpoint | operator | required for runtime, provider/live proof, credentials, S3, Docker, package activation, checker implementation, public-sync, or scope expansion |

## Scope

Allowed scope:

- Create the worker return at the planned worker return path.
- Create the companion reference at `docs/reference/CVF_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_2026-07-02.md`.
- Recompute MinerU source mirror commit and 425-file count before citing current source facts.
- Read accepted MSEA-T2/R4/R5/R6/R7/R8 artifacts and source mirror files only as evidence for blueprint/readiness synthesis.
- Map application blueprint layers, adapter contract prerequisites, route outcomes, and concrete hold/reopen conditions.
- Repair allowed-scope format/gate failures and rerun the failed gate.

Forbidden scope:

- Do not commit, stage for commit, push, or alter session-sync surfaces.
- Do not install or run MinerU, download models, start API/router/Gradio/Docker services, execute parser/OCR/VLM/hybrid backends, call providers, use credentials, connect to S3, or write a RAG index.
- Do not import upstream source into CVF runtime/source folders.
- Do not implement checker code, hook wiring, package activation, Web/UI/dashboard, MCP/CLI adapter, model-router, or action-authority work.
- Do not claim document truth, extraction accuracy, runtime readiness, hosted readiness, public readiness, adapter execution, or production readiness.

Risk ceiling: R0 documentation/reference synthesis only.

## Write Ownership

| Path | Worker permission | Boundary |
|---|---|---|
| `docs/reviews/CVF_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_SELECTION_WORKER_RETURN_2026-07-02.md` | create/modify pending worker return | must remain uncommitted by worker |
| `docs/reference/CVF_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_2026-07-02.md` | create/modify companion reference | must remain uncommitted by worker |
| any other path | FORBIDDEN | return to orchestrator unless a gate-safe same-scope repair is explicitly required by the planned artifacts |

## Worker Autonomy / No-Question Rule

The worker must proceed without asking the operator for routine allowed-scope
choices, including checker-shape remediation, grouping blueprint rows, and
rerunning failed gates. Operator escalation is reserved only for source
contradiction, scope expansion, live/provider proof, secrets/quota, runtime
execution, public-sync, destructive action, or a route decision that would
release a held implementation lane.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| MSEA-R8 accepted | `CVF_SESSION_MEMORY.md` and active handoff record material commit `42eeb411`; R8 reference records `CLEAR_WITH_DECLARED_BINARY_LIMITS` | A fresh documentation/reference follow-up may dispatch after operator selects concrete source-backed MinerU value | SATISFIED |
| Worker-output checker-shape learning recorded | ADIF-0023 and gotcha item 38 exist and are listed as first reads | R9 must convert the lesson into output-artifact read-ahead before writing | SATISFIED |
| Source mirror current authority | source mirror index row and local mirror HEAD match commit `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` with 425 files | Worker must stop if recomputation drifts | SATISFIED |

## Required First Reads

| Path | Why it matters |
|---|---|
| `CVF_SESSION_MEMORY.md` | startup front door and current mode |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | compact current state and next allowed move |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | canonical state registry |
| `AGENT_HANDOFF_V32_2026-07-02.md` | active handoff and MSEA boundaries |
| `docs/reference/guard_orientation/README.md` | role-specific guard orientation |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | literal-format traps, especially item 38 |
| `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0023.md` | worker-output artifact checker-shape learning |
| `docs/reference/work_order_authoring/CVF_WORKER_RETURN_FULL_GATE_CONTRACT_STANDARD.md` | compact worker-return contract |
| `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | receipt/quality/RAG owner surface |
| `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md` | CLI/API/Docker/runtime-candidate owner surface |
| `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` | deep document-layer candidates and reopen conditions |
| `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md` | prior route decision and held implementation lanes |
| `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` | receipt contract draft |
| `docs/reference/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md` | final residual absorption ledger |
| `.private_reference/source_mirrors/INDEX.md` | source mirror authority |

## Intake Role Routing Decision

- Intake summary: operator requested continued MinerU absorption after MSEA-R8,
  with focus on a CVF application blueprint and adapter contract readiness.
- Scope classification: bounded external repository evidence synthesis into a
  documentation/reference blueprint.
- Risk sensitivity: no runtime, public-sync, provider/live run, secret,
  credential, package activation, checker implementation, production, adapter
  execution, document-truth, or extraction-accuracy claim.
- Selected role route: routeMode=SINGLE_AGENT_MULTI_ROLE.
- Role separation basis: dispatcher authors packet, worker produces
  uncommitted artifacts, reviewer/closer owns acceptance and commit.
- Escalation condition: stop if scope/risk changes or if runtime/provider/S3/
  RAG/Docker/checker/package/public action becomes needed.

## Single-Agent Multi-Role Control Block

- Role separation ledger: dispatcher, worker, reviewer/closer, and
  session-sync steward duties are recorded separately in this packet.
- Evidence basis: review must use git diff, source paths, worker return,
  companion reference, and gate output, not memory-only claims.
- Self-review boundary: this block does not claim independent review by a
  second human or provider.
- Escalation conditions: stop for operator checkpoint if the worker needs
  runtime execution, provider/live proof, secrets, credentials, public-sync,
  source import, Docker execution, checker implementation, or broader write
  scope.
- Gate sequence: worker runs pre-implementation and worker-return fast gates;
  reviewer/closer runs reviewer/steward and pre-closure gates on a real range.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | Worker-execution lesson ADIF-0023 is still mandatory read-ahead even though the dispatcher query returns no defects |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_epistemic_process_packet.py` |
| literalTokensReviewed | `## Dispatch Prompt Envelope`; `## Source Verification Block`; `## Current Runtime Freshness Verification`; `## Negative Search And Collision Discipline`; `## Agent Handoff Contract Control Block`; `## Reviewer Closure Conversion`; `## Work-Order Fulfillment Manifest`; `## Worker Return Packet Shape Contract`; `WORKER_RETURN_FULL_GATE_V1`; `requiredGate:`; `individualCheckerSubstitution: FORBIDDEN`; `workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED`; `## External Knowledge Intake Routing`; `## External Absorption Core`; `## Corpus Completeness And Report Integrity`; `## External Absorption Value Conversion Matrix`; `## Overlap And Novelty Classification`; `## Source Mirror Migration Control`; `## Target / Source`; `## Scope / Applies To`; rescan guard required section shape; `ledger_terminal=`; `CHECKER_CANDIDATE`; `REMOVED_OR_REJECTED`; `RESOLVED_BY_DESIGN`; `DEFERRED_PRIVATE_ONLY`; `CLAIM_REJECTED_NO_RECEIPT`; `CLAIM_REJECTED_NO_ACTION`; `PARTIAL` |
| gateRunPurpose | confirmation/evidence after checker-source read-ahead, not first discovery |
| claimBoundary | read-ahead for dispatch and worker-output shape only; no worker execution, runtime, provider/live, public-sync, package, checker, adapter, or production claim |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Current next allowed move requires fresh source-verified work order for concrete MinerU follow-up | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | field `nextAllowedMove` | `nextAllowedMove` | active session bootstrap | ACCEPT |
| Active handoff records MSEA-R8 acceptance and no-runtime boundary | EXISTS | `AGENT_HANDOFF_V32_2026-07-02.md` | `## Latest Changes`; `## Next Allowed Move` | `MSEA-R8` | active handoff | ACCEPT |
| Source mirror row exists and pins MinerU | VALUE_SET | `.private_reference/source_mirrors/INDEX.md` | row `opendatalab__MinerU` | `opendatalab__MinerU` | source mirror index | ACCEPT |
| Source mirror commit is current source anchor | VALUE_SET | `.private_reference/source_mirrors/INDEX.md` | row `opendatalab__MinerU` | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` | source mirror index | ACCEPT |
| R8 final absorption status is clear with declared binary limits | VALUE_SET | `docs/reference/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md` | blind-spot verdict | `CLEAR_WITH_DECLARED_BINARY_LIMITS` | MSEA-R8 residual ledger | ACCEPT |
| R6 selected a docs-only receipt schema route before R7 | VALUE_SET | `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md` | selected routing outcome | `OPEN_RECEIPT_SCHEMA_CONTRACT_DRAFT` | MSEA-R6 route decision matrix | ACCEPT |
| R7 names receipt artifact families relevant to application blueprinting | VALUE_SET | `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` | receipt artifact family table | `layout.pdf` | MSEA-R7 receipt contract draft | ACCEPT |
| R7 names structured output and backend boundaries | VALUE_SET | `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` | backend variant boundary | `content_list_v2.json` | MSEA-R7 receipt contract draft | ACCEPT |
| R5 identifies provider-call surface as demand-gated | EXISTS | `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` | conditional reopen candidates | `llm_aided.py` | MSEA-R5 owner-surface delta | ACCEPT |
| T2 owns receipt/RAG handoff advisory and future checker candidate | VALUE_SET | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | checker candidate ledger | `MSEA-CC-4` | MSEA-T2 advisory | ACCEPT |
| Worker-output shape lesson exists | EXISTS | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0023.md` | field block | `ADIF-0023` | ADIF entry | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Source treatment |
|---|---|---|
| applicationBlueprintLayer | Group practical CVF use cases and application surfaces | DOC_ONLY_NEW |
| adapterContractReadiness | Classify documentation/reference readiness for a future adapter contract | DOC_ONLY_NEW |
| routeDecisionOutcome | Select the next governed route token | DOC_ONLY_NEW |
| sourceBackedHoldCondition | Preserve concrete hold/reopen condition for deferred routes | DOC_ONLY_NEW |

## Current Runtime Freshness Verification

| Check | Command or evidence | Disposition |
|---|---|---|
| Runtime remains forbidden | Active bootstrap nextAllowedMove forbids install, runtime, model download, parser/OCR/VLM/hybrid execution, provider/live call, credentials/S3, RAG write, source import, package activation, checker implementation, public-sync, Web/MCP/model-router/action-authority, benchmark, document-truth, extraction-accuracy, and production claims | ACCEPT |
| Source mirror commit and count checked before dispatch | `git -C .private_reference/source_mirrors/opendatalab__MinerU rev-parse HEAD` returned `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`; `git -C .private_reference/source_mirrors/opendatalab__MinerU ls-files` returned 425 | ACCEPT |
| Planned R9 artifacts did not pre-exist | `Test-Path` returned `False` for planned baseline, work order, worker return, and reference output before authoring | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| R9 path and title collision | `rg -n "MSEA-R9|MinerU CVF Application Blueprint And Adapter Contract Readiness Selection|CVF_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT"` over governed docs/session surfaces returned no match before authoring | ACCEPT |
| Runtime work implied by title | Title says blueprint/readiness selection; forbidden scope blocks adapter implementation and runtime proof | ACCEPT |
| Optional decision packet absence | No optional decision packet is required; worker records route decision inside worker return and companion reference | ACCEPT |

## Pre-Flight Checks

| Command | Expected result |
|---|---|
| `git rev-parse --short HEAD` | worker captures real executionBaseHead |
| `git status --short` | worker records current pending changes accurately |
| `git -C .private_reference/source_mirrors/opendatalab__MinerU rev-parse HEAD` | commit matches `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` or worker blocks |
| `rg --files --hidden --no-ignore .private_reference/source_mirrors/opendatalab__MinerU -g '!**/.git/**'` | current source mirror enumeration is available for evidence |
| `python governance/compat/run_worker_return_fast_gate.py` | PASS after worker output artifacts are drafted and repaired |

## Blueprint Source Manifest

| Source group | Reviewable artifact or root | Dispatch disposition |
|---|---|---|
| MinerU source mirror authority | `.private_reference/source_mirrors/INDEX.md` and `.private_reference/source_mirrors/opendatalab__MinerU/` | source mirror commit/count must be recomputed by worker |
| MSEA receipt and RAG owner surface | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | read for doctrine and boundaries |
| MSEA runtime/package candidate deltas | `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md`; `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` | read for held runtime/package/provider/S3/RAG routes |
| MSEA route and receipt contract surfaces | `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md`; `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` | read for route outcomes and receipt prerequisites |
| MSEA residual closure ledger | `docs/reference/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md` | read for final corpus accounting boundary |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | dispatcher authored baseline/work order; delegated worker creates pending artifacts; reviewer/closer owns material commit; session-sync steward updates state only after accepted material commit |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=89943d30; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | worker may create only the planned worker return and planned reference output |
| traceScope(phase, actor) | worker records operation trace in worker return; reviewer validates and commits material artifacts if accepted |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT for worker; reviewer/closer owns material commit |
| crossBatchIsolation | no unrelated artifacts, session-sync, protected paths, runtime/source, checker, package, public-sync, or Web/MCP paths may be edited by worker |
| nextMoveSurfaces | worker must not edit next-move surfaces; reviewer/session-sync steward updates them after accepted material commit if needed |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | N/A_WITH_REASON: no separate `_COMPLETION_` reviewer artifact is planned; prefer repairing evidence in the worker return per literal-format gotcha 30 |
| reviewerOwnedClosurePaths | worker return and reference output after reviewer acceptance; session-sync surfaces only in a later dedicated commit |
| closureOwner | reviewer/closer role |
| workerCommitPermission | FORBIDDEN |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| `docs/reviews/CVF_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_SELECTION_WORKER_RETURN_2026-07-02.md` | create from worker-return scaffold, fill evidence, include route decision, run worker-return fast gate, leave uncommitted |
| `docs/reference/CVF_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_2026-07-02.md` | create CVF-owned blueprint/readiness reference with `## Scope / Applies To`, source-backed matrices, route decision outcome, and claim boundary |

## Worker Output Artifact Checker-Shape Plan

The worker must not treat this dispatch packet checklist as sufficient for the
files the worker creates. Before writing long prose, derive an output-artifact
shape checklist from checker source and record it in the worker return.

| Output artifact | Required pre-write action | Minimum literal requirements to confirm |
|---|---|---|
| worker return under reviews folder | run `python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_SELECTION_WORKER_RETURN_2026-07-02.md --title "CVF MSEA-R9 MinerU CVF Application Blueprint And Adapter Contract Readiness Selection Worker Return"`; run fast gate while skeleton is short | `## Target / Source`; `## Scope / Methodology`; `## Findings / Position`; `## Risk / Corrective Action`; `## External Knowledge Intake Routing`; rescan guard required section shape; `## Corpus Completeness And Report Integrity`; `## Finding-To-Governance Learning Disposition`; `## Epistemic Process Block`; `ledger_terminal=` if corpus claims are made; `CHECKER_CANDIDATE` if checker value is discussed; `REMOVED_OR_REJECTED` and `RESOLVED_BY_DESIGN` if a real rescan matrix is included |
| companion reference under reference folder | read structural and external-absorption checkers before writing | `## Scope / Applies To`; source mirror control; overlap classification; value conversion matrix; claim boundary; public export disposition; no runtime claim language |

If any of these requirements appears inapplicable, keep the heading and record
`N/A with reason` or the checker-accepted not-applicable token rather than
omitting the section.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_SELECTION_WORKER_RETURN_2026-07-02.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | external repo or copied folder -> pinned source mirror plus accepted MSEA owner surfaces -> CVF application blueprint -> adapter contract readiness route selection -> future work only by fresh authorization |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py`; `governance/compat/check_corpus_completeness_report_integrity.py` |
| Owner surface | this work order and paired MSEA-R9 GC-018 baseline |
| Disposition | DISPATCH documentation/reference blueprint and adapter-readiness selection from accepted MinerU evidence |
| Claim boundary | dispatch fulfillment only; no runtime, package activation, checker wiring, provider/live proof, public-sync, API/router/Gradio, Docker, model download, OCR/VLM/hybrid execution, S3, RAG write, benchmark, document-truth, extraction-accuracy, or production-readiness claim |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | `https://github.com/opendatalab/MinerU.git` at `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`; local mirror `.private_reference/source_mirrors/opendatalab__MinerU/`; accepted MSEA-T2/R4/R5/R6/R7/R8 evidence |
| Enumeration command | `rg --files --hidden --no-ignore .private_reference/source_mirrors/opendatalab__MinerU -g '!**/.git/**'`; plus `git -C .private_reference/source_mirrors/opendatalab__MinerU rev-parse HEAD` for commit evidence |
| Manifest artifact or inline manifest | inline table `## Blueprint Source Manifest` |
| Processing ledger artifact or inline ledger | planned `docs/reviews/CVF_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_SELECTION_WORKER_RETURN_2026-07-02.md` and `docs/reference/CVF_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_2026-07-02.md` |
| Ledger terminal statuses | READ, SOURCE_VERIFIED, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, SKIPPED_WITH_REASON, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | MSEA-T2/R4/R5/R6/R7/R8 owner surfaces and conditional reopen rows |
| Unresolved items | blueprint/readiness route selection pending worker execution |
| Completion claim boundary | documentation-only blueprint and readiness route selection; no runtime/provider/public/package/checker expansion |

## Corpus Completeness And Report Integrity

- Corpus task class: source-backed application blueprint dispatch from accepted MinerU absorption evidence.
- Corpus root: `.private_reference/source_mirrors/opendatalab__MinerU/` plus accepted MSEA governed artifacts.
- Snapshot time: 2026-07-02 local dispatch session.
- Enumeration command: `rg --files --hidden --no-ignore .private_reference/source_mirrors/opendatalab__MinerU -g '!**/.git/**'`; `git -C .private_reference/source_mirrors/opendatalab__MinerU ls-files` returned 425 files; source mirror index records 425 files.
- Manifest artifact or inline manifest: `.private_reference/source_mirrors/INDEX.md` plus accepted MSEA-R8 residual ledger.
- Manifest hash: source mirror commit `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`; worker must recompute commit and count before citing current source facts.
- Processing ledger artifact or inline ledger: planned worker return and reference output.
- Allowed terminal statuses: READ, SOURCE_VERIFIED, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, SKIPPED_WITH_REASON, BLOCKED_UNREADABLE, BLOCKED_WITH_REASON.
- Reconciliation: manifest=425 source-mirror files; ledger_terminal=0 at dispatch before worker execution; exclusions=0; unresolved=0.
- Unresolved files: 0 at dispatch because R8 already closed residual accounting; R9 is blueprint synthesis, not a new full-file corpus pass.
- Declared exclusions: none at dispatch.
- Unreadable or unsupported files: none known at dispatch.
- Aggregation check: R9 must cite accepted MSEA artifacts for prior file-depth claims and recompute source mirror commit/count before any new source assertion.
- Drift check: worker must stop if the mirror commit or 425-file count drifts.
- Output traceability: blueprint rows must cite accepted MSEA owner surfaces or source mirror paths.
- Adversarial verification: worker must distinguish blueprint/contract readiness from runtime readiness, production readiness, document truth, extraction accuracy, and adapter implementation.
- Corpus verdict: PARTIAL

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| Accepted MSEA-T2/R7 receipt doctrine | source-backed receipt artifact and field-family vocabulary | DOCTRINE_ADAPTED | planned MSEA-R9 blueprint reference | worker maps receipt contract prerequisites into application routes | no schema implementation or receipt writer |
| MSEA-R4/R5/R8 runtime and backend evidence | concrete CLI/API/backend/provider/S3/Docker surfaces remain demand-gated | RUNTIME_CANDIDATE | MSEA-R9 readiness matrix | preserve reopen conditions, do not execute | no install, model download, parser run, provider call, or source import |
| MSEA-R5 RagFlow and RAG-handoff evidence | shipped downstream integration evidence with CVF RAG boundary limits | DOCTRINE_ADAPTED | MSEA-R9 application use-case map | record RAG route prerequisites and hold conditions | no RAG index write or plugin wiring |
| MSEA-R4/R5 Docker and deployment recipes | deployment evidence may inform future package/deployment readiness | PACKAGE_CANDIDATE | MSEA-R9 readiness matrix | preserve package/deployment hold conditions only | no Docker build/run or package activation |
| MSEA-T3/R6 checker candidate evidence | possible future overclaim guards remain condition-gated | CHECKER_CANDIDATE | MSEA-R9 route decision matrix | select only a docs/checker-requirements route if conditions are met | no checker implementation or hook wiring |
| Direct MinerU upstream code | source remains external reference input only | REJECT_DIRECT_IMPORT | MSEA source mirror control | reject direct copy/import; adapt CVF-native doctrine only | no direct import |
| Repeated or already-owned evidence | prior MSEA artifacts may already own the value | NO_PACKAGE_OR_RUNTIME_VALUE | existing MSEA owner surfaces | close with explicit overlap disposition | no runtime or package behavior |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| Receipt artifact family and field vocabulary | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md`; `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` | ENRICH_EXISTING | R9 can connect receipt contract vocabulary to practical application routes | create blueprint map |
| Runtime/provider/S3/Docker/RAG surfaces | `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md`; `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md`; `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md`; `docs/reference/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md` | CONFIRMED_EXISTING | R9 should preserve hold conditions rather than reopen execution | classify readiness and hold |
| Adapter contract readiness | `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md`; `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` | NEW_FINDING | R9 may create a CVF-owned readiness selection surface that did not exist as a single artifact | create reference output |
| Checker candidate route | `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md`; `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md` | CONFIRMED_EXISTING | no current repeated-miss evidence is known at dispatch | keep parked unless worker finds source-backed condition met |
| Direct upstream implementation | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | REJECT_DIRECT_IMPORT | no direct import remains allowed | reject import and preserve source-mirror authority |

## Source Mirror Migration Control

| Field | Disposition |
|---|---|
| Legacy source path | Legacy MinerU adapter folder remains secondary historical material only. |
| Source mirror path | `.private_reference/source_mirrors/opendatalab__MinerU/` |
| Mirror index row | `.private_reference/source_mirrors/INDEX.md` row `opendatalab__MinerU` |
| Pinned upstream commit | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` |
| Migration disposition | MIGRATED_TO_SOURCE_MIRROR |
| Legacy cleanup disposition | LEGACY_REFERENCE_ONLY_WITH_REASON: historical comparison only; source facts must prefer the pinned mirror or governed MSEA artifacts |
| Claim boundary | source-mirror authority control only; no runtime, install, package activation, provider/live proof, public-sync, checker implementation, or production-readiness claim |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Storage action | N/A with reason: MSEA-R9 creates one worker return and one reference artifact in existing governed folders only. |
| Folder/index impact | No new folder, stable reference family, front door, storage layout, or dated duplicate standard is authorized. |
| Durable foundation impact | The blueprint/readiness reference is a tranche-specific reference artifact, not a central foundation standard. |
| Required boundary | Worker must not create or relocate foundation storage, index, template, standard, or front-door files. |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: MSEA-R9 routes the freshly cloned MinerU source
mirror under `.private_reference/source_mirrors/opendatalab__MinerU/`, not a
legacy absorption folder. The legacy coverage index is not the owner surface
for this tranche. The work order retains the legacy folder only as a
forbidden-scope boundary and historical-reference warning.

## Route Outcomes

The worker must select exactly one route outcome in the worker return and
companion reference.

| Outcome token | When allowed | Boundary |
|---|---|---|
| OPEN_ADAPTER_CONTRACT_DRAFT_ONLY | source-backed blueprint shows enough CVF-owned prerequisites to draft a non-runtime adapter contract in a later tranche | still docs/reference only; no runtime |
| OPEN_CHECKER_REQUIREMENTS_DRAFT_ONLY | source-backed evidence shows a concrete checker-requirements draft is higher value than adapter contract drafting | requirements only; no checker implementation |
| HOLD_BLUEPRINT_ONLY_NO_IMPLEMENTATION | blueprint is useful but no next route has source-backed value above hold | no implementation |
| REQUEST_RUNTIME_PROOF_GC018 | worker finds a source-backed operator use case that genuinely requires runtime proof | stop at request; no runtime proof |
| REQUEST_OPERATOR_REQUIREMENT_EVIDENCE | route cannot be chosen without a concrete operator product requirement | stop and record missing evidence |

## Rescan Intelligence Hardening

- Original source artifact: `https://github.com/opendatalab/MinerU.git` at `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`, mirrored at `.private_reference/source_mirrors/opendatalab__MinerU/`
- Predecessor intake artifact: `docs/reference/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md`
- Delta ledger status: COMPLETE (see Original-Intake Delta Ledger below)
- Routing matrix status: COMPLETE (see Follow-Up Routing Matrix below)
- Semantic sampling status: COMPLETE (see Semantic Sampling / Adversarial Review below)
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Prior intake claim | R9 dispatch treatment | Delta category | Evidence |
|---|---|---|---|
| MSEA-R8 closed residual repository accounting | reuse as source-backed predecessor evidence | UNCHANGED_FROM_INTAKE | MSEA-R8 reference and worker return |
| MSEA-R6/R7 established receipt-contract route and draft | convert into application blueprint/readiness task | CHANGED_DISPOSITION | this work order routes from receipt draft to blueprint synthesis |
| Adapter contract readiness is not yet a single owner artifact | create doc-only readiness reference | NEW_FINDING | source-backed synthesis task only |
| Runtime execution route from dispatch scope | keep excluded from this documentation/reference work order | REMOVED_OR_REJECTED | forbidden scope and route outcomes |

### Follow-Up Routing Matrix

| Route lane | R9 handling | Boundary |
|---|---|---|
| DO_NOW | create worker return and companion reference only | docs/reference work only |
| RESOLVED_BY_DESIGN | no direct runtime route is needed to complete R9 blueprint synthesis | handled by no-runtime scope design |
| SEPARATE_RUNTIME_TRANCHE | runtime/provider/RAG/package routes remain held | fresh GC-018 and live/provider proof if behavior is claimed |
| STRATEGIC_OPERATOR_DECISION | operator may later choose a concrete product/runtime route | worker records request token only |
| OUT_OF_SCOPE | install, execution, provider call, source import, public-sync, checker implementation | forbidden in this work order |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| R9-S1 | MSEA-R7 receipt artifact family | receipt artifacts can inform future CVF receipt schema | ENRICH_EXISTING | artifact existence is not accuracy proof | PASS |
| R9-S2 | MSEA-R6 deferred runtime routes | parser/RAG/provider/S3 routes require fresh authorization | CONFIRMED_EXISTING | route decision must not imply runtime readiness | PASS |
| R9-S3 | MSEA-R8 residual closure | corpus accounting is closed with declared limits | UNCHANGED_FROM_INTAKE | blueprint must not reopen full corpus scan silently | PASS |

## Execution Plan

| Step | Action | Evidence | Stop condition |
|---|---|---|---|
| 1 | Capture `executionBaseHead`, source mirror HEAD, file count, and current `git status --short` | command evidence in worker return | stop on mirror drift |
| 2 | Create worker-return skeleton and run worker-return fast gate while short | command evidence | stop if skeleton cannot satisfy gate inside scope |
| 3 | Read required MSEA owner surfaces and checker source by output artifact type | Source Inventory and Checker Source Read-Ahead Block | stop on missing required source |
| 4 | Create companion reference blueprint with source-backed matrices and route decision | reference output path | stop on forbidden runtime/source need |
| 5 | Fill worker return with findings, route outcome, command evidence, no-commit status, and pending changed files | worker return path | stop if required gate cannot pass inside scope |

## Verification Commands

```powershell
git rev-parse --short HEAD
git status --short
git -C .private_reference/source_mirrors/opendatalab__MinerU rev-parse HEAD
git -C .private_reference/source_mirrors/opendatalab__MinerU ls-files
python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_SELECTION_WORKER_RETURN_2026-07-02.md --title "CVF MSEA-R9 MinerU CVF Application Blueprint And Adapter Contract Readiness Selection Worker Return"
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_governed_artifact_checker_read_ahead.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_external_knowledge_intake_routing.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_external_absorption_core.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_external_absorption_value_conversion.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_external_absorption_overlap_discipline.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_source_mirror_migration.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_corpus_completeness_report_integrity.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
git diff --name-status
git status --short
```

The worker must also run any directly failing checker after repair, then rerun
the fast gate. Individual checker substitution for the final worker-return fast
gate is forbidden.

## Evidence Requirements

| Evidence | Required form |
|---|---|
| Base evidence | `executionBaseHead`, `git status --short`, source mirror commit, and mirror enumeration command |
| Source evidence | cited MSEA artifacts or source mirror paths for every blueprint/readiness row |
| Gate evidence | worker-return fast gate plus listed external absorption and corpus gates |
| Boundary evidence | no-commit statement, changed-file manifest, and explicit forbidden-scope claim boundary |

## Acceptance Criteria

| Criterion | Required evidence |
|---|---|
| Two output artifacts only | `git diff --name-status` and `git status --short` show only planned worker return and companion reference as pending worker changes |
| Source mirror reconfirmed | worker return records mirror commit and 425-file count or stops on drift |
| Blueprint is source-backed | companion reference maps each blueprint/readiness row to MSEA owner surfaces or source mirror paths |
| Route decision is single-token | worker return and reference select exactly one route outcome from this work order |
| Runtime boundary is preserved | no runtime/provider/live/public/package/checker/source-import/Web/MCP/model-router/action-authority/document-truth/extraction-accuracy/production claim is made |
| Worker output checker-shape plan executed | worker return records output-artifact checker read-ahead and fast-gate evidence |
| WORKER_MUST_NOT_COMMIT honored | worker return records HEAD unchanged and no commit/stage/push by worker |

Fail conditions:

| Condition | Required response |
|---|---|
| Mirror commit or count drifts from source mirror index | `BLOCKED_WITH_REASON` and no blueprint conclusion from stale source facts |
| Worker needs runtime execution, live/provider proof, credentials, source import, checker implementation, or public-sync to decide | `BLOCKED_WITH_REASON` or route request token only; do not execute |
| Any output artifact lacks checker-required headings/tokens | repair inside allowed scope and rerun gate |
| Route decision uses an invented outcome token | repair to one allowed token or block |
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
artifact is missing, a route decision requires forbidden runtime/provider/
public/package/checker work, a gate cannot be repaired inside allowed scope, or
the worker needs to create paths outside Write Ownership.

## Operator Checkpoint

Operator approval is required before any runtime/provider/live proof,
credential/S3 use, MinerU install/model download/execution, source import,
public-sync, package activation, checker implementation, Web/MCP/model-router
work, action-authority work, benchmark, document-truth claim, extraction-
accuracy claim, or production-readiness claim.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher role |
| Provider or surface | local workspace |
| Session or invocation | MSEA-R9 dispatch authoring, 2026-07-02 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell; `rg`; source reads; scaffold helper; `apply_patch`; governance gates |
| Target paths | this work order; paired GC-018 baseline |
| Allowed scope source | operator instruction to create work order after MSEA-R8 and worker-output checker-shape learning |
| Before status evidence | clean worktree at HEAD `89943d30` before authoring |
| After status evidence | dispatch artifacts pending pre-dispatch gates and material commit |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | documentation/reference-only MSEA-R9 dispatch |
| Claim boundary | dispatch authoring only; no worker execution or runtime/provider/public/package/checker/source-import claim |
| Agent type | dispatcher |
| Invocation ID | `msea-r9-dispatch-authoring-2026-07-02` |
| Expected manifest | paired GC-018 baseline and this work order |
| Actual changed set | paired GC-018 baseline and this work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in this dispatch batch |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | MSEA-R9 work order for documentation/reference MinerU CVF application blueprint and adapter contract readiness selection |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, provider, parser, adapter, or production behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed |
| invocationBoundary | local governed document authoring and future worker document synthesis only |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | work order authorizes pending worker documentation/reference artifacts only |
| forbiddenExpansion | no MinerU runtime, install, model download, parser/OCR/VLM/hybrid/API/router/Gradio/Docker execution, provider/live call, credentials/S3, RAG write, source import, package activation, checker implementation, public-sync, Web/MCP/model-router/action-authority, automatic invocation, benchmark, document-truth, extraction-accuracy, or production-readiness claim |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R9 --title "MinerU CVF Application Blueprint And Adapter Contract Readiness Selection" --date 2026-07-02 --base 89943d30 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "MSEA-R8 accepted at material commit 42eeb411; operator selected continued MinerU absorption for CVF application blueprint and adapter readiness" --include-worker-return-skeleton --stdout` |
| generatedProfile | packet-kind=generic-worker-dispatch; commit-mode=WORKER_MUST_NOT_COMMIT; worker-return skeleton requested |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced scaffold placeholders with MSEA-R9 blueprint/readiness scope, source verification, external absorption blocks, worker-output checker-shape plan, route outcomes, and no-runtime claim boundary |
| checkerReadAheadConfirmation | read guard orientation, literal-format gotchas, worker-return full-gate standard, work-order template, R8 dispatch pattern, MSEA owner surfaces, source mirror anchors, and applicable checker source paths before writing |
| docOnlyNewFields | applicationBlueprintLayer; adapterContractReadiness; routeDecisionOutcome; sourceBackedHoldCondition |
| claimBoundary | scaffold provenance supports dispatch authoring only; no worker completion, runtime/provider/live/public/package/Web/MCP/model-router/action-authority, checker, or production claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order. No public-sync artifact is created or
modified by this tranche.

## Claim Boundary

This work order authorizes only MSEA-R9 worker execution under
WORKER_MUST_NOT_COMMIT to create one worker return and one companion reference.
It does not authorize worker commits, source import, runtime execution,
provider/live proof, credential use, public-sync, package activation, checker
implementation, Web/MCP/model-router work, action authority, automatic
invocation, benchmark, document-truth, extraction-accuracy, or
production-readiness claims.
