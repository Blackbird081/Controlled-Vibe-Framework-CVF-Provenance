# CVF Agent Work Order - MSEA-R11-T1 MinerU Productization Readiness Route Selection

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work_order

Date: 2026-07-03

Batch ID: MSEA-R11-T1

Dispatch base head: `8f73e469`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated worker role

Reviewer/closer: reviewer/closer role

Worker return path: `docs/reviews/CVF_MSEA_R11_T1_MINERU_PRODUCTIZATION_READINESS_ROUTE_SELECTION_WORKER_RETURN_2026-07-03.md`

Companion reference path: `docs/reference/CVF_MSEA_R11_T1_MINERU_PRODUCTIZATION_READINESS_ROUTE_SELECTION_DECISION_MATRIX_2026-07-03.md`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA-R11-T1 route selection.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R11_T1_MINERU_PRODUCTIZATION_READINESS_ROUTE_SELECTION_2026-07-03.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: worker must capture with `git rev-parse --short HEAD` before edits.

Current-time notes: artifact date is 2026-07-03.

Do-not-misread notes: this packet does not authorize MinerU install, parser execution, model download, schema implementation, receipt-writer code, adapter implementation, provider/live proof, source import, public-sync, package activation, checker implementation, RAG write, Docker build/run, production readiness, or document-truth/extraction-accuracy claims.

Required first actions: read startup files, guard orientation, literal gotchas, this work order, paired GC-018 baseline, R11 roadmap, R10/R9/R8/R7 owner surfaces, source mirror index, and all checker source listed in the Checker Source Read-Ahead Block before writing any artifact.

Return contract: create only the worker return and companion decision matrix, run required gates, leave changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Dispatch a bounded no-commit worker to select the next MinerU productization
route from accepted MSEA owner surfaces. This work order does not authorize
implementation, runtime proof, source import, or production-readiness claims.

## 1. Mission

Select the next MinerU productization route from accepted MSEA owner surfaces.
The worker must produce a source-backed decision matrix that recommends exactly
one next roadmap/work-order direction, or holds all productization lanes with
concrete reopen conditions. The worker must not implement the selected route.

## 2. Authority Chain

- Operator instruction: operator asked the agent to proceed and propose the next roadmap.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V33_2026-07-03.md`.
- Roadmap: `docs/roadmaps/CVF_MSEA_R11_MINERU_DOCUMENT_EXTRACTION_PRODUCTIZATION_READINESS_ROADMAP_2026-07-03.md`.
- GC-018 baseline: `docs/baselines/CVF_GC018_MSEA_R11_T1_MINERU_PRODUCTIZATION_READINESS_ROUTE_SELECTION_2026-07-03.md`.
- Source mirror index: `.private_reference/source_mirrors/INDEX.md`.
- Predecessor owner surfaces: R10 adapter contract draft, R9 application blueprint readiness, R8 residual ledger, R7 receipt schema contract draft.

Authority boundary: if any source contradicts this packet, stop and return
`BLOCKED_WITH_REASON`. Do not infer implementation authority from product value.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R11-T1 --title "MinerU Productization Readiness Route Selection" --date 2026-07-03 --base 8f73e469 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced placeholders with MSEA-R11-specific route-selection scope, source verification, worker-return outputs, and no-runtime boundary. |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py` |
| docOnlyNewFields | selectedRouteCandidate; routeSelectionVerdict; selectedNextRoadmapRecommendation |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | `## Checker Source Read-Ahead Block`; `applicableCheckersRead`; `literalTokensReviewed`; `gateRunPurpose`; `claimBoundary`; `## ADIF Defect Registry Disclosure`; `Resolver query:`; `Returned defects: NONE_RETURNED`; `WORKER_MUST_NOT_COMMIT`; `Agent Handoff Contract Control Block`; `Reviewer Closure Conversion`; `completionReviewPath`; `reviewerOwnedClosurePaths`; `## Intake Role Routing Decision`; `## Legacy Absorption Coverage Index Disposition`; `## Verification Commands`; `External Knowledge Intake Routing`; `External Absorption Core`; `External Absorption Value Conversion Matrix`; `Overlap And Novelty Classification`; `Source Mirror Migration Control`; `Delta Execution Claim Boundary Control Block`; `DEFERRED_PRIVATE_ONLY` |
| gateRunPurpose | Confirmation evidence after reading checker source ahead of work-order writing; not first discovery. |
| claimBoundary | Read-ahead covers dispatch packet shape and worker output shape requirements; worker must still read checker source before writing output artifacts. |

## 3. Agent Roles

| Role | Assignment | Boundary |
|---|---|---|
| Dispatcher | dispatcher role | authors and commits dispatch packet only |
| Worker | delegated worker role | creates pending worker return and companion reference only |
| Reviewer/closer | reviewer/closer role | reviews, repairs allowed-scope defects, commits material if accepted |
| Operator | operator | required only for scope expansion, live/provider proof, implementation, public-sync, or destructive action |

## 4. Scope

Allowed scope:

- Read the required MSEA owner surfaces and source mirror index.
- Recompute MinerU source mirror HEAD and file count only.
- Create the worker return named above.
- Create the companion decision matrix named above.
- Compare candidate next routes and select one recommendation or hold all.
- Run worker-return fast gate and listed component checks.

Explicitly not required:

- A full per-file ledger of the 425-file mirror.
- Reabsorbing the repository.
- Reading every MinerU source file again.

Forbidden scope:

- MinerU install, parser execution, OCR/VLM/hybrid execution, remote backend processing, model download, API/router/Gradio startup, Docker build/run, provider/live proof, S3 connection, credential handling, RAG index write, source import, package activation, checker implementation, schema implementation, receipt-writer code, adapter implementation, public-sync, Web/MCP/model-router/action-authority, automatic invocation, benchmark, document-truth, extraction-accuracy, certification, production-readiness claim, commit, stage, push, or session-sync edit.

Risk ceiling: R1 documentation/reference decision only.

## Worker Autonomy / No-Question Rule

Worker must proceed without operator confirmation for non-destructive reads,
route matrix drafting, required evidence-block completion, and allowed-scope
gate remediation. Routine checker-shape fixes are mandatory remediation, not
operator-preference questions.

Escalate only for source contradiction, missing authority, implementation need,
live/provider proof, secrets/quota, public-sync, forbidden paths, destructive
action, or a change to the claim boundary.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | No ADIF-specific remediation is required for this query. |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| Intake summary | Operator asked dispatch author to proceed with MSEA-R11-T1 and propose the next roadmap direction. |
| Scope classification | documentation/reference route-selection worker dispatch |
| Risk sensitivity | R1 documentation decision; no runtime/provider/live/source import or implementation |
| Selected route mode | MULTI_AGENT_MULTI_ROLE |
| Role separation basis | dispatcher authors packet; delegated worker creates pending artifacts; reviewer/closer converts and commits if accepted |
| Escalation condition | Worker must return `BLOCKED_WITH_REASON` for source contradiction, forbidden-scope requirement, missing authority, live/provider need, or implementation demand. |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: MSEA-R11-T1 uses accepted MSEA owner surfaces and
the pinned source mirror index only; it does not reopen legacy absorption
coverage or claim foundation/workflow-chain coverage.

## Foundation Storage Layout Block

NOT_APPLICABLE_WITH_REASON: this work order creates only two dispatch artifacts
and assigns two pending worker output artifacts; it does not create, split,
relocate, or refactor durable governance foundation storage.

## 5. Required First Reads

| Path | Why it matters |
|---|---|
| `CVF_SESSION_MEMORY.md` | active startup front door |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | compact current mode and next move |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | canonical state registry |
| `AGENT_HANDOFF_V33_2026-07-03.md` | active handoff and parked boundary |
| `docs/reference/guard_orientation/README.md` | task-class guard map |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | literal-format traps |
| `docs/baselines/CVF_GC018_MSEA_R11_T1_MINERU_PRODUCTIZATION_READINESS_ROUTE_SELECTION_2026-07-03.md` | paired dispatch authority |
| `docs/roadmaps/CVF_MSEA_R11_MINERU_DOCUMENT_EXTRACTION_PRODUCTIZATION_READINESS_ROADMAP_2026-07-03.md` | route-selection roadmap |
| `docs/reference/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md` | adapter contract obligations and held lanes |
| `docs/reference/CVF_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_2026-07-02.md` | application blueprint and readiness |
| `docs/reference/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md` | residual mirror closure and candidates |
| `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` | receipt families and field vocabulary |
| `.private_reference/source_mirrors/INDEX.md` | pinned MinerU source mirror metadata |

## 6. Pre-Flight Checks

Commands before worker edits:

```powershell
git rev-parse --short HEAD
git status --short
git -C .private_reference/source_mirrors/opendatalab__MinerU rev-parse HEAD
(rg --files --hidden --no-ignore .private_reference/source_mirrors/opendatalab__MinerU -g '!**/.git/**' | Measure-Object -Line).Lines
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 8f73e469 --head HEAD
```

Expected results:

- Worktree status may show only worker-owned pending artifacts after edits.
- Source mirror HEAD should be `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` unless worker records drift and returns `BLOCKED_WITH_REASON`.
- Source mirror file count should be `425` unless worker records drift and returns `BLOCKED_WITH_REASON`.
- Pre-implementation gate must pass or be repaired inside allowed scope before worker output is returned.

## 6A. Source-Fidelity Pass

### Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| R11-T1 route selection is the next authorized move | `docs/roadmaps/CVF_MSEA_R11_MINERU_DOCUMENT_EXTRACTION_PRODUCTIZATION_READINESS_ROADMAP_2026-07-03.md` | `## Authorization / Decision`; `## Work Plan` | `AUTHOR_MSEA_R11_T1_GC018_AND_WORK_ORDER_FOR_SOURCE_VERIFIED_PRODUCTIZATION_ROUTE_SELECTION` | MSEA-R11 roadmap | ACCEPT |
| Productization candidate lanes are route-selection inputs, not implementation authorization | `docs/roadmaps/CVF_MSEA_R11_MINERU_DOCUMENT_EXTRACTION_PRODUCTIZATION_READINESS_ROADMAP_2026-07-03.md` | `## Findings / Position`; `## Non-Goals` | `ROUTE_SELECTION_CANDIDATE`; `HELD_RUNTIME_CANDIDATE` | MSEA-R11 roadmap | ACCEPT |
| R10 is documentation/reference-only adapter contract vocabulary | `docs/reference/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md` | `## Contract Class`; `## Explicit Non-Claims` | `runtimeExecutionAuthorized`; `adapterImplementationAuthorized` | MSEA-R10 reference | ACCEPT |
| R7 owns receipt artifact and field families for schema/writer evaluation | `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` | `## Receipt Artifact Family Map`; `## Field Family Map` | `Receipt Artifact Family Map`; `Field Family Map` | MSEA-R7 reference | ACCEPT |
| R9 owns application blueprint readiness and held runtime/provider/RAG/S3/checker conditions | `docs/reference/CVF_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_2026-07-02.md` | `## Adapter Contract Readiness Matrix`; `## Source-Backed Hold Conditions` | `OPEN_ADAPTER_CONTRACT_DRAFT_ONLY` | MSEA-R9 reference | ACCEPT |
| R8 residual ledger confirms 425-file source mirror accounting and parked runtime/package evidence | `docs/reference/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md` | `## Prior Coverage Reconciliation`; `## Candidate And No-Value Ledger` | `425`; `RUNTIME_CANDIDATE`; `PACKAGE_CANDIDATE` | MSEA-R8 reference | ACCEPT |
| Source mirror is pinned at the MinerU upstream commit used by predecessor evidence | `.private_reference/source_mirrors/INDEX.md` | row `opendatalab__MinerU` | `.private_reference/source_mirrors/opendatalab__MinerU/` | source mirror index | ACCEPT |

### Current Runtime Freshness Verification

| Claim | Command | Result | Disposition |
|---|---|---|---|
| This work order does not authorize runtime implementation | review of Allowed and Forbidden scope | implementation paths excluded | PASS |
| Source mirror commit can be checked without running MinerU | `git -C .private_reference/source_mirrors/opendatalab__MinerU rev-parse HEAD` | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` during dispatch authoring | PASS |
| Source mirror count can be checked without full per-file ledger | `rg --files --hidden --no-ignore .private_reference/source_mirrors/opendatalab__MinerU -g '!**/.git/**'` piped to line count | `425` during dispatch authoring | PASS |

### Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Planned worker-return path did not exist before dispatch | `Test-Path docs/reviews/CVF_MSEA_R11_T1_MINERU_PRODUCTIZATION_READINESS_ROUTE_SELECTION_WORKER_RETURN_2026-07-03.md` returned `False` | PASS |
| Planned companion reference path did not exist before dispatch | `Test-Path docs/reference/CVF_MSEA_R11_T1_MINERU_PRODUCTIZATION_READINESS_ROUTE_SELECTION_DECISION_MATRIX_2026-07-03.md` returned `False` | PASS |
| Route token collision | `rg -n "OPEN_MSEA_R11_T1_PRODUCTIZATION_READINESS_SELECTION" docs CVF_SESSION AGENT_HANDOFF_V33_2026-07-03.md .private_reference/source_mirrors/INDEX.md` returned R11 roadmap/session evidence only | PASS |

## 6B. Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| Author source-verified R11-T1 route-selection work order | sections 1-6 | this work order and paired baseline | pre-dispatch autorun | PASS |
| Select first implementation-facing lane or hold all | sections 8 and 9 | decision matrix `selectedRouteCandidate` and worker-return `routeSelectionVerdict` | worker-return fast gate plus reviewer read | PASS |
| Compare sample corpus, schema, receipt writer, runtime, RAG, provider/S3, Docker/package, checker | section 8 | Candidate Route Matrix | worker output must contain every candidate row | PASS |
| Preserve all implementation holds until future GC-018 | sections 4, 8, Claim Boundary | explicit forbidden scope and candidate dispositions | dispatch-quality and Delta block checks | PASS |
| Recompute source mirror commit/count | sections 6 and 9 | command evidence in worker return | reviewer checks command output | PASS |
| Avoid full repository reabsorption | section 4 | no full per-file ledger requirement | reviewer checks output scope | PASS |

## 6C. Worker Autonomy / No-Question Rule

Proceed autonomously with required reads, safe source mirror commit/count
checks, route matrix writing, worker-return scaffold generation, and allowed
format/gate remediation. Do not ask the operator to choose between full ledger
and sampling; this packet already selects route-selection evidence from owner
surfaces and count/commit drift checks only.

## 6D. Pending Artifact Evidence Finality

The worker return must record actual `git status --short` output with the two
pending artifacts. The worker must not claim clean status while those artifacts
are untracked or modified.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher -> delegated worker -> reviewer/closer -> session-sync steward |
| phase | dispatch and worker pending-return |
| baseHeadFor(phase) | dispatchBaseHead=8f73e469; executionBaseHead=worker captured before edits; closureBaseHead=reviewer set after acceptance |
| changedSetScope(phase) | worker may create only the named worker return and companion decision matrix |
| traceScope(phase, actor) | worker records Agent Operation Trace Block for both output artifacts; reviewer records closure evidence if accepted |
| commitOwner(phase) | worker commit forbidden; reviewer/closer owns material commit; session-sync steward owns continuity commit |
| crossBatchIsolation | dispatch worktree was clean before authoring; worker must not touch unrelated paths |
| nextMoveSurfaces | unchanged by worker; reviewer/closer updates session state only after accepted material commit |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_MSEA_R11_T1_MINERU_PRODUCTIZATION_READINESS_ROUTE_SELECTION_COMPLETION_2026-07-03.md` |
| reviewerOwnedClosurePaths | `docs/reviews/CVF_MSEA_R11_T1_MINERU_PRODUCTIZATION_READINESS_ROUTE_SELECTION_WORKER_RETURN_2026-07-03.md`; `docs/reference/CVF_MSEA_R11_T1_MINERU_PRODUCTIZATION_READINESS_ROUTE_SELECTION_DECISION_MATRIX_2026-07-03.md` |
| closureOwner | reviewer/closer role |
| workerCommitPermission | FORBIDDEN |
| allowedPendingWorkerStatus | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| forbiddenFinalResidue | worker output must not claim `CLOSED_PASS_BOUNDED`, commit ownership, public export, runtime proof, production readiness, or clean worktree when artifacts are pending |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| `docs/reviews/CVF_MSEA_R11_T1_MINERU_PRODUCTIZATION_READINESS_ROUTE_SELECTION_WORKER_RETURN_2026-07-03.md` | create from worker-return scaffold, fill required review headings and evidence, run worker-return fast gate |
| `docs/reference/CVF_MSEA_R11_T1_MINERU_PRODUCTIZATION_READINESS_ROUTE_SELECTION_DECISION_MATRIX_2026-07-03.md` | create companion reference containing route-selection matrix and source-backed recommendation |

Forbidden filesystem state:

| Path or class | Required dispatch status | Worker action if present |
|---|---|---|
| any MinerU runtime/source file outside output artifacts | ABSENT_OR_UNCHANGED | return `BLOCKED_WITH_REASON` before editing |
| `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF*.md`, `AGENTS.md` | ABSENT_OR_UNCHANGED | worker must not edit |
| source mirror files | READ_ONLY | worker may read and count only |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R11_T1_MINERU_PRODUCTIZATION_READINESS_ROUTE_SELECTION_WORKER_RETURN_2026-07-03.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Worker must create the return from scaffold before long prose:

```powershell
python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_MSEA_R11_T1_MINERU_PRODUCTIZATION_READINESS_ROUTE_SELECTION_WORKER_RETURN_2026-07-03.md --title "CVF MSEA-R11-T1 MinerU Productization Readiness Route Selection Worker Return"
python governance/compat/run_worker_return_fast_gate.py
```

Worker output must include these review-shape headings: `## Target / Source`,
`## Scope / Methodology`, `## Findings / Position`, `## Risk / Corrective Action`,
`## Decision / Recommendation`, `## External Knowledge Intake Routing`,
`## Epistemic Process Block`, and `## Claim Boundary`.

## 7. Write Ownership

Owned files:

- `docs/reviews/CVF_MSEA_R11_T1_MINERU_PRODUCTIZATION_READINESS_ROUTE_SELECTION_WORKER_RETURN_2026-07-03.md`
- `docs/reference/CVF_MSEA_R11_T1_MINERU_PRODUCTIZATION_READINESS_ROUTE_SELECTION_DECISION_MATRIX_2026-07-03.md`

Write mode: create-only for worker.

Forbidden paths: every path outside the two owned files, including source
mirror files and session/handoff/front-door files.

## 8. Execution Plan

| Step | Input | Output | Validation | Stop condition |
|---|---|---|---|---|
| 1 | startup files and this packet | captured executionBaseHead and actual `git status --short` | command evidence | dirty unrelated worktree |
| 2 | source mirror index and mirror root | recomputed commit/count evidence | command evidence | drift from expected commit or count |
| 3 | R11/R10/R9/R8/R7 owner surfaces | candidate route matrix | every candidate row present | missing owner surface |
| 4 | candidate matrix | selected route or hold-all recommendation | source-backed rationale | route would require forbidden implementation |
| 5 | worker-return scaffold | completed worker return and companion reference | worker-return fast gate | unrepaired allowed-scope gate failure |

Candidate Route Matrix rows required in the companion reference:

| Candidate route | Required worker disposition |
|---|---|
| Sample corpus and expected receipt policy | select, defer, or reject with source-backed rationale |
| Receipt schema implementation | select, defer, or reject with source-backed rationale |
| Receipt-writer code | select, defer, or reject with source-backed rationale |
| Local parser runtime pilot | hold unless runtime proof prerequisites are source-backed |
| RAG handoff adapter | hold unless receipt and quality/downstream-use prerequisites are source-backed |
| Provider-assisted correction | hold unless operator use case and secret-safe live-proof boundary exist |
| S3 storage boundary | hold unless operator use case and credential plan exist |
| Docker/package lane | hold unless deployment target and hardware profile exist |
| Overclaim checker | hold unless repeated misses or authorized ingestion tranche exists |
| Hold all productization lanes | select only if no route has source-backed value/risk advantage |

Recommended route bias for worker evaluation: prefer `Sample corpus and expected
receipt policy` if evidence shows implementation cannot be safely scoped without
a concrete input corpus and expected receipt contract. This is a recommendation
bias, not a mandatory outcome.

## 8A. Design Control Carry-Forward

| Design control | Roadmap source | Work-order handling | Verdict |
|---|---|---|---|
| Scope boundary | R11 `## Scope` | route selection only | PASS |
| Non-goals | R11 `## Non-Goals` | repeated in forbidden scope | PASS |
| Lane split | R11 candidate table | route matrix required | PASS |
| Dependency/source-verification plan | R11 Source Verification Block | source verification table above | PASS |
| Claim boundary | R11 Claim Boundary | no implementation/public/runtime claims | PASS |
| Acceptance criteria | R11 Acceptance Criteria | acceptance criteria and gates below | PASS |
| Verification/evidence | R11 Verification / Evidence | pre-dispatch and worker gates required | PASS |
| Dispatch-readiness decision | R11 status line | this work order dispatches T1 only | PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | Codex local workspace |
| Session or invocation | MSEA-R11-T1 dispatch authoring, 2026-07-03 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, `rg`, scaffold helper, source reads, `apply_patch`, governance gates |
| Target paths | this work order; paired GC-018 baseline |
| Allowed scope source | operator instruction plus MSEA-R11 roadmap material commit `30a15322` |
| Before status evidence | clean worktree; `git status --short` was empty before dispatch authoring |
| After status evidence | two new dispatch artifacts pending pre-dispatch gates |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | dispatch authoring for no-commit route-selection worker only |
| Claim boundary | no runtime/provider/live/public/package/checker/source-import/schema/receipt-writer/adapter/Web/MCP/model-router/action-authority claim |
| Agent type | dispatcher |
| Invocation ID | `msea-r11-t1-dispatch-2026-07-03` |
| Expected manifest | this work order; `docs/baselines/CVF_GC018_MSEA_R11_T1_MINERU_PRODUCTIZATION_READINESS_ROUTE_SELECTION_2026-07-03.md` |
| Actual changed set | `docs/baselines/CVF_GC018_MSEA_R11_T1_MINERU_PRODUCTIZATION_READINESS_ROUTE_SELECTION_2026-07-03.md` |
| Manifest delta | MATCH_FOR_NON_TRACE_PAIRED_ARTIFACT |
| Deletion or rename disposition | N/A with reason: no deletion or rename; two new dispatch artifacts |

## 8C. Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: sample corpus and expected receipt policy is
likely the safest next roadmap because schema, writer, runtime, and RAG routes
need concrete input/expected-output boundaries first.

Evidence Comparison Requirement: worker return must compare actual owner-surface
evidence against this prediction.

Contradiction Handling Requirement: contradictory evidence requires a
Contradiction Or Gap Disposition and route recommendation update.

Claim Update Requirement: worker return records whether the route prediction is
confirmed, revised, narrowed, or invalidated.

## Evidence Requirements

Required worker evidence:

- `executionBaseHead` from `git rev-parse --short HEAD`.
- Actual `git status --short`.
- Source mirror HEAD and count command outputs.
- Source Inventory table with bare action tokens only.
- Candidate route matrix with every required candidate row.
- Selected route token or hold-all token.
- `python governance/compat/run_worker_return_fast_gate.py` result.
- `git diff --name-status` showing only owned files.

Allowed selected route tokens:

- `OPEN_SAMPLE_CORPUS_AND_EXPECTED_RECEIPT_POLICY_ROADMAP`
- `OPEN_RECEIPT_SCHEMA_IMPLEMENTATION_ROADMAP`
- `OPEN_RECEIPT_WRITER_CODE_ROADMAP`
- `OPEN_LOCAL_PARSER_RUNTIME_PILOT_ROADMAP`
- `OPEN_RAG_HANDOFF_ADAPTER_ROADMAP`
- `OPEN_PROVIDER_OR_S3_BOUNDARY_ROADMAP`
- `OPEN_DOCKER_PACKAGE_LANE_ROADMAP`
- `OPEN_OVERCLAIM_CHECKER_ROADMAP`
- `HOLD_ALL_PRODUCTIZATION_LANES`

## 10. Acceptance Criteria

| Criterion | Required evidence |
|---|---|
| Worker return exists at the named path | file exists and status is `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| Companion reference exists at the named path | file exists with `## Scope / Applies To`, route matrix, and claim boundary |
| All candidate route rows are evaluated | candidate route matrix contains all required rows |
| Recommendation is source-backed | selected route cites R11/R10/R9/R8/R7 owner surfaces |
| No implementation was performed | `git diff --name-status` contains only owned docs paths |
| Worker did not commit | HEAD unchanged from executionBaseHead in worker return |
| Worker-return fast gate passes or blocker is explicit | command evidence recorded |

## Closure Checklist

| Item | Disposition |
|---|---|
| Worker return created at named path | reviewer verifies before closure |
| Companion reference created at named path | reviewer verifies before closure |
| Worker did not commit, stage, push, or edit forbidden paths | reviewer verifies with `git status --short` and diff evidence |
| Selected route or hold-all token is source-backed | reviewer verifies against R11/R10/R9/R8/R7 owner surfaces |
| Runtime/provider/live/public/package/source-import/schema/writer/adapter claims are absent | reviewer verifies claim boundary |

## Operator Checkpoint

No operator checkpoint is required for worker route-selection execution. Operator
approval is required only for scope expansion, implementation, live/provider
proof, secret use, public-sync, package activation, or destructive action.

Fail conditions:

| Condition | Blocking action |
|---|---|
| Worker runs MinerU, installs packages, downloads models, calls providers, uses credentials, writes RAG, builds Docker, edits source mirror, implements schema/writer/adapter/checker, commits, stages, pushes, or edits session state | reviewer must reject and return to orchestrator |
| Source mirror commit/count drift without explicit blocked disposition | worker must return `BLOCKED_WITH_REASON` |
| Candidate matrix omits a required row | worker must repair before handoff |
| Output claims document truth, extraction accuracy, live proof, production readiness, or public readiness | worker must remove claim or return blocked |

## 11. Review Gate

Dispatch may proceed only after:

- paired GC-018 baseline exists;
- pre-dispatch autorun gate passes;
- commit steward preflight passes;
- material pre-commit hook passes.

Worker handoff is not closure. Reviewer/closer must run reviewer-return checks
and commit accepted material separately.

## Verification Commands

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base 8f73e469 --head HEAD --enforce
python governance/compat/check_adif_defect_registry_disclosure.py --base 8f73e469 --head HEAD --enforce
python governance/compat/check_governed_artifact_checker_read_ahead.py --base 8f73e469 --head HEAD --enforce
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 8f73e469 --head HEAD
python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base 8f73e469 --head HEAD --enforce
```

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | accepted MSEA owner surfaces plus pinned MinerU source mirror -> MSEA-R11-T1 route-selection worker return and companion decision matrix |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py` |
| Owner surface | this work order |
| Disposition | ADAPT: route accepted MinerU absorption and contract vocabulary into a productization decision |
| Claim boundary | dispatch-only; no runtime/provider/live/S3/RAG/Docker/package/checker/source-import/schema/receipt-writer/adapter implementation/public-sync/production claim |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| R11 roadmap | productization route candidates | DOCTRINE_ADAPTED | worker return and decision matrix | select next roadmap or hold all | no implementation |
| R10 adapter contract draft | held-lane prerequisites | DOCTRINE_ADAPTED | decision matrix | compare route readiness | no adapter implementation |
| R7 receipt vocabulary | receipt families and fields | DOCTRINE_ADAPTED | decision matrix | compare schema/writer/sample-corpus routes | no schema/writer implementation |
| R8 runtime/package evidence | held runtime/package candidates | RUNTIME_CANDIDATE | decision matrix held rows | keep demand-gated unless future roadmap selected | no runtime/package action |
| Checker notes | overclaim checker possibility | CHECKER_CANDIDATE | decision matrix held row | keep condition-gated | no checker implementation |
| Direct upstream implementation | advisory source only | REJECT_DIRECT_IMPORT | source mirror control | reject direct import | no source import |
| Prior absorption facts | already-owned evidence | NO_PACKAGE_OR_RUNTIME_VALUE | predecessor owner surfaces | cite only | no runtime/package behavior |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| R11-T1 route-selection lane | `docs/roadmaps/CVF_MSEA_R11_MINERU_DOCUMENT_EXTRACTION_PRODUCTIZATION_READINESS_ROADMAP_2026-07-03.md` | ENRICH_EXISTING | converts roadmap seed into worker dispatch | dispatch |
| Adapter contract vocabulary | `docs/reference/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md` | CONFIRMED_EXISTING | used as source input | cite |
| Receipt vocabulary | `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` | CONFIRMED_EXISTING | used as source input | cite |
| Runtime/provider/S3/Docker/RAG/package/checker holds | `docs/reference/CVF_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_2026-07-02.md`; `docs/reference/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md` | CONFIRMED_EXISTING | preserved as held lanes | defer |
| Direct upstream implementation | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md`; `.private_reference/source_mirrors/INDEX.md` | REJECT_DIRECT_IMPORT | direct import remains forbidden | reject |

## Source Mirror Migration Control

| Field | Disposition |
|---|---|
| Legacy source path | Legacy MinerU adapter folder remains secondary historical material only |
| Source mirror path | `.private_reference/source_mirrors/opendatalab__MinerU/` |
| Mirror index row | `.private_reference/source_mirrors/INDEX.md` row `opendatalab__MinerU` |
| Pinned upstream commit | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` |
| Migration disposition | MIGRATED_TO_SOURCE_MIRROR |
| Legacy cleanup disposition | LEGACY_REFERENCE_ONLY_WITH_REASON: historical comparison only; source facts prefer pinned mirror or governed MSEA artifacts |
| Claim boundary | source-mirror authority control only; no runtime, install, package activation, provider/live proof, public-sync, checker implementation, source import, schema implementation, receipt-writer code, adapter implementation, or production-readiness claim |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | MSEA-R11-T1 work order for MinerU productization readiness route selection |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, provider, parser, adapter, schema, receipt-writer, or production behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed |
| invocationBoundary | local governed worker-return authoring only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, Web runtime, adapter, package, watcher, daemon, parser, RAG index, or production route interception claim |
| claimLanguage | no-commit route-selection worker dispatch and future reviewer evidence only |
| forbiddenExpansion | no MinerU runtime, install, model download, parser/OCR/VLM/hybrid/API/router/Gradio/Docker execution, provider/live call, credentials/S3, RAG write, source import, package activation, checker implementation, public-sync, Web/MCP/model-router/action-authority, automatic invocation, benchmark, document-truth, extraction-accuracy, schema implementation, receipt-writer code, adapter implementation, or production-readiness claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order. No public-sync export is authorized.

## Claim Boundary

This work order authorizes only no-commit route-selection evidence. It does not
authorize or claim MinerU installation, parser execution, OCR/VLM/hybrid
routing, remote backend processing, model download, API/router/Gradio service,
Docker deployment, provider/live proof, S3 access, credential handling, RAG
indexing, source import, checker enforcement, package activation, schema
implementation, receipt-writer code, adapter implementation, public-sync
export, document truth, extraction accuracy, benchmark, certification,
generated aggregate mutation, production readiness, model-router behavior,
action authority, automatic invocation, or universal document intelligence.
