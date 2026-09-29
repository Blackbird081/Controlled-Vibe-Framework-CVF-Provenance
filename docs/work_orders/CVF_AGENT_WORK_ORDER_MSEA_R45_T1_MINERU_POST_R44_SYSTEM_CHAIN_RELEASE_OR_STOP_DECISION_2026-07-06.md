# CVF Agent Work Order - MSEA R45 T1 MinerU Post R44 System Chain Release Or Stop Decision

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: MSEA_R45_T1_MINERU_POST_R44_SYSTEM_CHAIN_RELEASE_OR_STOP_DECISION

Dispatch base head: 2898812d8

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: Codex reviewer/closer

Worker return path: `docs/reviews/CVF_MSEA_R45_T1_MINERU_POST_R44_SYSTEM_CHAIN_RELEASE_OR_STOP_DECISION_WORKER_RETURN_2026-07-06.md`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA_R45_T1_MINERU_POST_R44_SYSTEM_CHAIN_RELEASE_OR_STOP_DECISION.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R45_T1_MINERU_POST_R44_SYSTEM_CHAIN_RELEASE_OR_STOP_DECISION_2026-07-06.md`

Paired GC-018 baseline: `docs/baselines/CVF_GC018_MSEA_R45_T1_MINERU_POST_R44_SYSTEM_CHAIN_RELEASE_OR_STOP_DECISION_2026-07-06.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-06; dispatch base head is `2898812d8`.

Do-not-misread notes: this packet authorizes a docs-only release-or-stop decision using accepted R44-T2 closure evidence. It does not authorize source/test edits, MinerU runtime execution, private/generated output reads, production durable-store invocation, production Memory/RAG route invocation or release, provider/live proof, public-sync, or legal/use-case workflow.

Required first actions: read required startup files, guard orientation, literal gotchas, this packet, the paired GC-018 baseline, R44-T2 closure evidence, current route source facts named in the Source Verification Block, and all checker source listed in the Checker Source Read-Ahead Block before writing any artifact.

Return contract: create only the companion decision matrix and worker return artifact, run required gates, leave changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Produce a docs-only, source-verified decision on the post-R44 MinerU/Memory/scanlayer system-chain state: stop as bounded internal candidate, open a later minimal private smoke packet, open a later operator-owned production release authority packet, or hold pending a named source gap. The worker must keep the lane focused on foundation-chain release/stop authority and must not drift into use-case/legal workflow.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA_R45_T1_MINERU_POST_R44_SYSTEM_CHAIN_RELEASE_OR_STOP_DECISION --title "MSEA R45 T1 MinerU Post R44 System Chain Release Or Stop Decision" --date 2026-07-06 --base 2898812d8 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Filled R45-T1 purpose, authority chain, source verification, ADIF disclosure, handoff control, allowed scope, output manifest, decision options, verification commands, and claim boundaries |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| docOnlyNewFields | `MSEA_R45_T1_MINERU_POST_R44_SYSTEM_CHAIN_RELEASE_OR_STOP_DECISION`; `R45_T1_POST_R44_STOP_BOUNDED_INTERNAL_CANDIDATE`; `R45_T1_POST_R44_READY_FOR_MINIMAL_PRIVATE_SYSTEM_CHAIN_SMOKE_PACKET`; `R45_T1_POST_R44_READY_FOR_OPERATOR_PRODUCTION_RELEASE_AUTHORITY_PACKET`; `R45_T1_POST_R44_HELD_PENDING_SOURCE_GAPS` |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Authority Chain

| Authority source | Role in this dispatch |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | Current front-door continuity and post-R44 next-move context |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | Compact current mode and next allowed move |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Canonical active mode, R44-T2 closure state, and active handoff routing |
| `AGENT_HANDOFF_V37_2026-07-06.md` | Active handoff named by the state registry |
| `docs/reference/guard_orientation/README.md` | Guard routing for dispatcher and worker execution |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | Literal-format guardrails |
| `docs/reviews/CVF_MSEA_R44_T2_MINERU_NARROW_FILE_BACKED_PERSISTENCE_INVOCATION_IMPLEMENTATION_WORKER_RETURN_2026-07-06.md` | Accepted R44-T2 worker-return and reviewer acceptance evidence |
| `CVF_SESSION/state/entries/mseaR44T2MineruNarrowFileBackedPersistenceInvocationImplementationClosure20260706.json` | Machine-readable R44-T2 closure entry and next recommendation |
| Current source files named in Source Verification Block | Runtime/source evidence for current route boundaries |

## Agent Roles

| Role | Responsibility | Commit authority |
| --- | --- | --- |
| Dispatcher | Author GC-018 baseline and work order | May commit dispatch artifacts if gates pass |
| Worker | Create decision matrix and worker return only | WORKER_MUST_NOT_COMMIT |
| Reviewer/closer | Review worker return, run closure gates, decide acceptance, and own material/session-sync commits | Reviewer-owned |
| Operator | Owns any future production, provider/live, public, or use-case checkpoint | N/A |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly by reading the failing checker source and matching the literal required shape. Worker should return to orchestrator only for a source contradiction, forbidden-scope need, or missing authority that makes completion impossible.

## Pre-Flight Checks

| Check | Required worker evidence |
| --- | --- |
| Execution base | Record `git rev-parse --short HEAD` before writing |
| Clean worktree | Record `git status --short --untracked-files=all` before writing |
| Required reads | List startup, guard, dispatch, predecessor, source, and checker files actually read |
| Scope confirmation | Confirm only the companion matrix and worker return paths are changed |
| Provider-local hygiene | Confirm no provider-local or IDE config file was created |

## Mandatory Gate-Failure Remediation Protocol

- Allowed-scope failures are mandatory remediation. Complete the remediation and execute the failed gate again.
- Missing `N/A with reason`, stale closure residue, source-verification corrections, allowed worker-return repair, and routine guard failures are not operator-preference questions.
- Escalation is reserved for remediation that would exceed Allowed Scope, release production behavior, consume secrets or live quota, touch forbidden paths, change risk posture, public-sync, run MinerU runtime, read private/generated output content, or perform destructive filesystem actions.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0024; ADIF-0006

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 20 --json` |
| Returned defect count | 11 |
| Returned defects | ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0024; ADIF-0006 |
| Disclosed defectIds | ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0024; ADIF-0006 |
| Dispatch impact | Packet uses source verification, checker read-ahead, exact commit mode, explicit worker scope, provider-local hygiene, no public/export overclaim, and no implementation-before-authority wording |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| literalTokensReviewed | Dispatch Prompt Envelope; Source Verification Block; ADIF Defect Registry Disclosure; Checker Source Read-Ahead Block; Negative Search And Collision Discipline; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Worker Output Checker Read-Ahead Mandate; Work-Order Fulfillment Manifest; Worker Return Packet Shape Contract; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; DISPATCH_READY; WORKER_MUST_NOT_COMMIT; ACCEPT; VALUE_SET; EXISTS; RUNTIME_BEHAVIOR; DOC_ONLY_NEW; N/A with reason; DEFERRED_PRIVATE_ONLY |
| gateRunPurpose | Confirmation after source-read authoring; gate runs are evidence and not first discovery for packet shape |
| claimBoundary | Read-ahead covers dispatch artifact shape only; it does not prove implementation behavior, runtime execution, live provider behavior, public-sync, or production readiness |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Active session next move authorizes a fresh post-R44 release-or-stop decision packet | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `nextAllowedMove` field | `nextAllowedMove` | active session bootstrap read model | ACCEPT |
| R44-T2 closure accepted bounded source/test implementation | VALUE_SET | `CVF_SESSION/state/entries/mseaR44T2MineruNarrowFileBackedPersistenceInvocationImplementationClosure20260706.json` | lines 5, 18, and 21-28 | `R44_T2_NARROW_FILE_BACKED_PERSISTENCE_INVOCATION_IMPLEMENTATION_ACCEPTED_BOUNDED` | R44-T2 closure state entry | ACCEPT |
| Route candidate supports file-backed persistence mode only as a route mode value | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | line 46 | `MineruSystemChainPersistenceMode` | MinerU system-chain route candidate | ACCEPT |
| Route authority carries explicit file-backed request and actor-role fields | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | lines 52-60 | `MineruSystemChainRouteAuthority` | MinerU system-chain route candidate | ACCEPT |
| File-backed route acceptance still requires explicit request and actor-role allowlist | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | lines 129-146 | `fileBackedPersistenceRequested` | `buildMineruSystemChainRouteCandidate` | ACCEPT |
| Route result remains production-route unauthorized | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | lines 74, 89, 200, and 212 | `productionRouteAuthorized` | MinerU system-chain route candidate result | ACCEPT |
| Route result preserves the T25 held token | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | lines 29-30, 79, 94, 205, and 217 | `PRODUCTION_MEMORY_RAG_ROUTE_NOT_RELEASED_BY_T25_CANDIDATE_ONLY` | MinerU system-chain route candidate result | ACCEPT |
| R44-T1 predecessor selected readiness for the narrow invocation implementation packet | VALUE_SET | `docs/reference/CVF_MSEA_R44_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_RECHECK_OR_STOP_DECISION_MATRIX_2026-07-06.md` | lines 45, 53, and 58 | `R44_T1_FILE_BACKED_PERSISTENCE_RELEASE_READY_FOR_NARROW_INVOCATION_PACKET` | R44-T1 decision matrix | ACCEPT |
| Provider/live proof remained bounded private provenance evidence, not production readiness | VALUE_SET | `docs/reference/CVF_MSEA_R44_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_RECHECK_OR_STOP_DECISION_MATRIX_2026-07-06.md` | line 71 | `R40_T1_PROVIDER_LIVE_PROOF_COMPLETE_BOUNDED_PRIVATE` | R44-T1 decision matrix dependency table | ACCEPT |
| Earlier foundation-chain stop state existed before R44 reopening work | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | `mseaR41T4MineruFoundationChainStopReleaseDecisionClosure20260706` entry | `R41_T4_FOUNDATION_CHAIN_STOP_BOUNDED_CANDIDATE` | active session state registry | ACCEPT |

## New Doc-Only Fields

| Field | Owner artifact | Purpose | Runtime/source status |
| --- | --- | --- | --- |
| `MSEA_R45_T1_MINERU_POST_R44_SYSTEM_CHAIN_RELEASE_OR_STOP_DECISION` | This work order and paired baseline | Batch identifier for the docs-only decision dispatch | DOC_ONLY_NEW |
| `R45_T1_POST_R44_STOP_BOUNDED_INTERNAL_CANDIDATE` | Worker decision matrix | Allowed decision token for stopping as bounded internal candidate | DOC_ONLY_NEW |
| `R45_T1_POST_R44_READY_FOR_MINIMAL_PRIVATE_SYSTEM_CHAIN_SMOKE_PACKET` | Worker decision matrix | Allowed decision token for later private smoke packet authoring | DOC_ONLY_NEW |
| `R45_T1_POST_R44_READY_FOR_OPERATOR_PRODUCTION_RELEASE_AUTHORITY_PACKET` | Worker decision matrix | Allowed decision token for later operator-owned production authority packet authoring | DOC_ONLY_NEW |
| `R45_T1_POST_R44_HELD_PENDING_SOURCE_GAPS` | Worker decision matrix | Allowed decision token for holding on named source gaps | DOC_ONLY_NEW |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Path existence for R45-T1 baseline before authoring | `Test-Path docs/baselines/CVF_GC018_MSEA_R45_T1_MINERU_POST_R44_SYSTEM_CHAIN_RELEASE_OR_STOP_DECISION_2026-07-06.md` returned `False` before authoring | ACCEPT |
| Path existence for R45-T1 work order before authoring | `Test-Path docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R45_T1_MINERU_POST_R44_SYSTEM_CHAIN_RELEASE_OR_STOP_DECISION_2026-07-06.md` returned `False` before authoring | ACCEPT |
| Path existence for planned R45-T1 worker outputs before authoring | Planned matrix and worker return paths both returned `False` before authoring | ACCEPT |
| Token search before authoring | `rg -n "MSEA-R45-T1|MSEA_R45_T1|CVF_MSEA_R45_T1" docs CVF_SESSION CVF_SESSION_MEMORY.md AGENT_HANDOFF_V37_2026-07-06.md EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests` returned no matches before authoring | ACCEPT |
| Collision decision | No existing R45-T1 packet or worker-output path was present | ACCEPT |

## Dependency Release Evidence

| Dependency | Required evidence | Refreshed evidence | Disposition |
| --- | --- | --- | --- |
| R44-T2 closure | Accepted bounded implementation and session-sync current state | Material commit `8004f30c6`; session-sync commit `2898812d8`; closure state entry records focused Vitest PASS 1 file / 21 tests and next move to post-R44 release-or-stop packet | SATISFIED |
| Production route boundary | Packet must not release production Memory/RAG or production durable-store behavior | Route source keeps `productionRouteAuthorized` false and T25 held token; active state next move forbids production invocation/release without a fresh accepted packet | SATISFIED |
| Use-case boundary | Operator warned not to drift into use-case/legal workflow | This packet is docs-only system-chain decision; legal/use-case workflow remains forbidden | SATISFIED |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | Dispatcher authors packet; worker creates docs-only decision matrix and worker return; reviewer/closer reviews and commits if accepted |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=2898812d8; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | Worker may create only the companion decision matrix and worker return listed in Work-Order Fulfillment Manifest |
| traceScope(phase, actor) | Worker return must record commands, cwd, changed files, decision token, gate results, pending status, manifest match, and no-commit evidence |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | Before status evidence must be clean or disclose only owned pending paths; unrelated provider-local or IDE files must be removed or disclosed as blockers |
| nextMoveSurfaces | Worker must not edit session state, front door, or active handoff; reviewer/closer owns any next-move sync after acceptance |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R45_T1_MINERU_POST_R44_SYSTEM_CHAIN_RELEASE_OR_STOP_DECISION_COMPLETION_2026-07-06.md` (optional; prefer reviewer decision inside the worker return if evidence is complete) |
| reviewerOwnedClosurePaths | Worker return plus companion decision matrix if accepted; optional completion review only if worker return cannot safely carry closure evidence; active session state source fragments; generated active session state; active handoff; session memory front door |
| closureOwner | Codex reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| routeMode | SINGLE_AGENT_SINGLE_ROLE |
| intakeSummary | Operator requested a fresh post-R44 release-or-stop decision packet using accepted R44-T2 closure evidence |
| scopeClassification | Docs-only source-verified release-or-stop decision for MinerU/Memory/scanlayer system-chain foundation state |
| riskSensitivity | Medium governance risk because the packet decides whether a later runtime, provider/live, production authority, or stop lane should be opened |
| selectedRoleRoute | routeMode SINGLE_AGENT_SINGLE_ROLE; delegated worker creates decision artifacts and reviewer/closer owns acceptance and commits |
| roleSeparationBasis | Worker must not commit; reviewer/closer owns closure decision and any session-sync |
| dispatcherRole | dispatcher role |
| workerRole | delegated worker |
| reviewerRole | reviewer/closer role |
| authorityCheckpoint | SATISFIED: R44-T2 closed and active next move authorizes only fresh post-R44 decision packet authoring |
| escalationCondition | Stop and return BLOCKED if completion needs source/test edits, runtime execution, private-output read, provider/live proof, production release, public-sync, use-case/legal workflow, or agent-operation intervention |
| claimBoundary | Role routing only; no provider-specific assignment, provider-local authority, live provider behavior, public-sync, or agent-operation intervention claim |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: R45-T1 uses only CVF-governed source files and accepted CVF review artifacts |
| Matching local-view guard | N/A with reason: no external intake event occurred |
| Owner surface | This work order and paired GC-018 baseline |
| Disposition | NOT_APPLICABLE_WITH_REASON: no external source is promoted to CVF authority |
| Claim boundary | This section is routing evidence only and does not authorize outside-source absorption |

## Required First Reads

| Required read | Purpose |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | Session front door |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | Compact state read |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Canonical current mode and handoff routing |
| `AGENT_HANDOFF_V37_2026-07-06.md` | Current governed continuity |
| `docs/reference/guard_orientation/README.md` | Guard orientation |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | Literal-format failure prevention |
| this work order and paired GC-018 baseline | Dispatch authority |
| `docs/reviews/CVF_MSEA_R44_T2_MINERU_NARROW_FILE_BACKED_PERSISTENCE_INVOCATION_IMPLEMENTATION_WORKER_RETURN_2026-07-06.md` | Accepted predecessor worker return |
| `CVF_SESSION/state/entries/mseaR44T2MineruNarrowFileBackedPersistenceInvocationImplementationClosure20260706.json` | Machine-readable closure evidence |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | Current route candidate source facts |
| checker files listed in Checker Source Read-Ahead Block | Output-shape authority |

## Allowed Scope

The worker may create only:

- `docs/reference/CVF_MSEA_R45_T1_MINERU_POST_R44_SYSTEM_CHAIN_RELEASE_OR_STOP_DECISION_MATRIX_2026-07-06.md`
- `docs/reviews/CVF_MSEA_R45_T1_MINERU_POST_R44_SYSTEM_CHAIN_RELEASE_OR_STOP_DECISION_WORKER_RETURN_2026-07-06.md`

The decision matrix must:

- compare R41-T4 stop state, R40-T1 bounded live proof, R44-T1 narrow invocation readiness, and R44-T2 bounded source/test implementation;
- select exactly one allowed disposition token from Decision Options;
- identify any blocker or next packet as source-verified and bounded;
- preserve the statement that CVF controls route-boundary authority, evidence, traceability, and responsibility review, not agent internal operation;
- explicitly keep legal/use-case workflow parked.

## Forbidden Scope

- Do not edit runtime source, tests, durable store implementation, route harnesses, package exports, session state, handoffs, front door, provider-local files, IDE config, public-sync clone, hook catalogs, or unrelated docs.
- Do not run MinerU runtime, install models, download models, call OCR/VLM/parser/provider APIs, read private/generated output content, run provider/live proof, or consume secrets/quota.
- Do not invoke production file-backed persistence, production durable-store behavior, production Memory/RAG route, retrieval, vectorization, public-sync, standalone app work, Web/UI implementation, or use-case/legal workflow.
- Do not claim extraction accuracy, document truth, legal quality, current-law correctness, hosted release, production release, public readiness, or workflow-chain production readiness.
- Do not claim CVF controls agent internals. The claim is route-boundary authority checking, evidence, and traceability only.
- Do not commit, stage for commit, push, public-sync, or leave stray provider-local files such as `.qwen/settings.json`.

## Decision Options

| Allowed disposition token | Required evidence logic |
| --- | --- |
| `R45_T1_POST_R44_STOP_BOUNDED_INTERNAL_CANDIDATE` | Select when the foundation chain is valuable but further work has diminishing value without an operator production/live/use-case checkpoint |
| `R45_T1_POST_R44_READY_FOR_MINIMAL_PRIVATE_SYSTEM_CHAIN_SMOKE_PACKET` | Select only if source evidence supports a later narrow private smoke packet without private-output reads, production release, provider/live proof, public-sync, or use-case claims |
| `R45_T1_POST_R44_READY_FOR_OPERATOR_PRODUCTION_RELEASE_AUTHORITY_PACKET` | Select only if the correct next move is an operator-owned production authority decision, not implementation or runtime execution |
| `R45_T1_POST_R44_HELD_PENDING_SOURCE_GAPS` | Select when source evidence still leaves a named authority, traceability, receipt, or quality gap that blocks release-or-stop decision |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/reference/CVF_MSEA_R45_T1_MINERU_POST_R44_SYSTEM_CHAIN_RELEASE_OR_STOP_DECISION_MATRIX_2026-07-06.md` | Create source-verified decision matrix selecting exactly one allowed disposition token |
| `docs/reviews/CVF_MSEA_R45_T1_MINERU_POST_R44_SYSTEM_CHAIN_RELEASE_OR_STOP_DECISION_WORKER_RETURN_2026-07-06.md` | Record execution evidence, gates, claim boundary, hygiene checks, and pending worktree status |

## Write Ownership

| Path | Worker permission | Reviewer permission |
| --- | --- | --- |
| `docs/reference/CVF_MSEA_R45_T1_MINERU_POST_R44_SYSTEM_CHAIN_RELEASE_OR_STOP_DECISION_MATRIX_2026-07-06.md` | CREATE_ALLOWED | REVIEW_AND_COMMIT_IF_ACCEPTED |
| `docs/reviews/CVF_MSEA_R45_T1_MINERU_POST_R44_SYSTEM_CHAIN_RELEASE_OR_STOP_DECISION_WORKER_RETURN_2026-07-06.md` | CREATE_ALLOWED | REVIEW_AND_COMMIT_IF_ACCEPTED |
| Any other path | FORBIDDEN | N/A with reason: outside R45-T1 allowed scope |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| foundationStorageChange | N/A with reason: R45-T1 does not create durable governance foundation storage or change storage layout |
| durableStoreRuntimeChange | N/A with reason: no runtime durable-store invocation is authorized |
| indexOrCatalogChange | N/A with reason: no index, catalog, public-sync, or storage-layout update is authorized |
| claimBoundary | The packet authorizes docs-only decision artifacts only; it does not change production storage layout or public catalog state |

## Worker Output Checker Read-Ahead Mandate

Before writing each worker-owned output artifact, read checker source for that file's docType, path family, and conditional content class.

| Output artifact | Required read-ahead result |
| --- | --- |
| Worker return under the reviews folder | Derive exact review headings, worker-return quality terms, trace labels, Delta block labels, corpus/value/rescan tokens, and no-commit evidence shape before writing |
| Companion reference under the reference folder | Derive exact reference headings, target/source evidence, source verification, trace, and claim-boundary labels before writing |

Literal-shape reminders: do not list required worker-output sections with heading prefixes before the real section; write source-not-found disposition spelling in literal-token lists; avoid unnecessary literal extension source paths in review prose when the companion matrix Source Verification Block can carry the exact source evidence.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R45_T1_MINERU_POST_R44_SYSTEM_CHAIN_RELEASE_OR_STOP_DECISION_WORKER_RETURN_2026-07-06.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Shape-list rule: when listing required worker-output sections, write section names without the `##` prefix. Reserve actual heading syntax for real sections so structural checkers do not treat this checklist as the artifact section body.

## Verification Commands

```powershell
git rev-parse --short HEAD
git status --short --untracked-files=all
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
git diff --name-status
git status --short --untracked-files=all
```

## Evidence Requirements

| Evidence | Required form |
| --- | --- |
| executionBaseHead | `git rev-parse --short HEAD` captured before edits |
| Worktree before/after | Exact `git status --short --untracked-files=all` output before and after edits |
| Decision matrix | Path plus selected disposition token |
| Worker-return gate | Exact `python governance/compat/run_worker_return_fast_gate.py` result |
| Pre-implementation gate | Exact command with execution base and PASS/BLOCKED result |
| Changed set | `git diff --name-status` plus pending status showing only allowed paths |
| Provider-local hygiene | Evidence that no provider-local or IDE config file was created |
| Claim boundary | Explicit no runtime, no private output, no production Memory/RAG, no provider/live, no public-sync, no use-case/legal claim |

## Execution Plan

1. Capture `executionBaseHead` and clean or disclosed worktree status.
2. Read mandatory startup, guard, dispatch, predecessor, source, and checker files.
3. Create only the companion decision matrix and worker return.
4. Compare the post-R44 evidence chain against each allowed disposition token.
5. Select exactly one disposition token and state next action or stop condition.
6. Run worker-return fast gate and pre-implementation autorun gate.
7. Record exact command results, changed files, provider-local hygiene, and no-commit statement.
8. Return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` without committing.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher role |
| Provider or surface | local workspace |
| Session or invocation | MSEA_R45_T1_MINERU_POST_R44_SYSTEM_CHAIN_RELEASE_OR_STOP_DECISION dispatch, 2026-07-06 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | `Get-Content`; `rg`; `Test-Path`; `python governance/compat/run_adif_defect_resolver.py`; `python governance/compat/build_dispatch_packet_scaffold.py`; `apply_patch`; governance gates |
| Target paths | This work order, paired GC-018 baseline, planned decision matrix path, and planned worker return path |
| Allowed scope source | Active session next allowed move plus R44-T2 accepted closure state |
| Before status evidence | clean worktree: `git rev-parse --short HEAD` returned `2898812d8`; `git status --short --untracked-files=all` was empty before authoring |
| After status evidence | Pending dispatch artifacts until material commit |
| Diff evidence | `git diff --name-status` before material commit |
| Deletion or rename disposition | N/A with reason: dispatch authoring creates two new governed artifacts only |
| Approval boundary | Operator requested fresh GC-018/source-verified post-R44 release-or-stop decision packet; no worker execution yet |
| Claim boundary | Dispatch packet only; no decision result is accepted until worker execution and reviewer acceptance |
| Agent type | dispatcher |
| Invocation ID | `msea-r45-t1-mineru-post-r44-system-chain-release-or-stop-decision-dispatch-2026-07-06` |
| Expected manifest | `docs/baselines/CVF_GC018_MSEA_R45_T1_MINERU_POST_R44_SYSTEM_CHAIN_RELEASE_OR_STOP_DECISION_2026-07-06.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R45_T1_MINERU_POST_R44_SYSTEM_CHAIN_RELEASE_OR_STOP_DECISION_2026-07-06.md` |
| Actual changed set | `docs/baselines/CVF_GC018_MSEA_R45_T1_MINERU_POST_R44_SYSTEM_CHAIN_RELEASE_OR_STOP_DECISION_2026-07-06.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R45_T1_MINERU_POST_R44_SYSTEM_CHAIN_RELEASE_OR_STOP_DECISION_2026-07-06.md` |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R45-T1 docs-only post-R44 release-or-stop decision dispatch |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: dispatch authority and source facts are recorded; decision result remains pending worker execution and reviewer acceptance |
| receiptEvidence | N/A with reason: dispatch packet creates no runtime receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT: governed dispatch artifacts only |
| invocationBoundary | Local governed file editing and deterministic governance gates only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, IDE control, shell control, provider control, or agent-internal control is claimed |
| claimLanguage | CVF records route-boundary authority and traceability for post-R44 release-or-stop decisions |
| forbiddenExpansion | Do not expand into MinerU runtime, provider/live, public, package, Web/MCP/model-router behavior, production release, or agent-operation intervention without fresh source-verified authorization |

## Acceptance Criteria

- Decision matrix exists and selects exactly one allowed disposition token.
- Worker return records exact commands, worker-return fast gate result, pre-implementation gate result, changed files, provider-local hygiene, and pending worktree status.
- Decision keeps production Memory/RAG, production durable-store invocation, provider/live proof, public-sync, and use-case/legal workflow out of scope unless it selects a future authority packet only.
- No source/test, runtime, session state, handoff, provider-local, IDE config, or public-sync path is edited by the worker.

## Fail Conditions

- Worker creates any file outside Work-Order Fulfillment Manifest.
- Worker edits runtime source, tests, session state, active handoff, front door, provider-local files, IDE config, public-sync clone, or hook catalogs.
- Worker runs MinerU runtime, reads private/generated output, runs provider/live proof, invokes production durable-store behavior, releases production Memory/RAG, public-syncs, or enters use-case/legal workflow.
- Worker claims extraction accuracy, document truth, legal quality, current-law correctness, hosted release, production release, public readiness, or workflow-chain production readiness.
- Worker omits a selected disposition token or selects a token outside Decision Options.
- Worker commits, stages for commit, pushes, or leaves stray provider-local files.

## Review Gate

Reviewer acceptance requires:

- Worker return fast gate PASS.
- Pre-implementation autorun gate PASS on the worker changed set.
- Reviewer confirms diff stays inside Work-Order Fulfillment Manifest.
- Reviewer confirms the claim boundary remains docs-only release-or-stop decision, not production release, runtime proof, public-sync, or agent-operation intervention.

## Closure Checklist

| Item | Required closure handling |
| --- | --- |
| Worker changed-set manifest | Must match Work-Order Fulfillment Manifest or return blocked |
| Decision token | Must be exactly one allowed token |
| Worker return fast gate | Must pass or cite reviewer-owned repair |
| Autorun gate | Must run on proper execution range and be dispositioned |
| Commit ownership | Worker must not commit; reviewer/closer owns accepted material commit |
| Session sync | Reviewer/closer updates next-move surfaces only after acceptance |
| Public export | Must remain private-only unless a future public-sync packet authorizes export |

## Operator Checkpoint

| Field | Value |
| --- | --- |
| Current checkpoint | Operator requested a fresh GC-018/source-verified post-R44 release-or-stop decision packet |
| Worker checkpoint need | N/A with reason: worker can complete the docs-only decision within the authorized scope |
| Future checkpoint | Required before MinerU runtime, private-output read, provider/live proof, production Memory/RAG release, production durable-store invocation, public-sync, push, or use-case/legal workflow |

## Claim Boundary

This work order authorizes only a no-commit docs-only decision tranche for post-R44 MinerU/Memory/scanlayer release-or-stop authority. It does not authorize source/test edits, MinerU runtime execution, private/generated output content read, production file-backed persistence invocation, production durable-store invocation, production Memory/RAG route invocation or release, retrieval, vectorization, provider/live proof, Web/UI implementation, public-sync, standalone app work, legal/use-case deep dive, extraction accuracy, document truth, legal quality, current-law correctness, hosted release claim, production release claim, provider-local or IDE config edits, worker commit, push, or public claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: This is a private provenance dispatch packet only; no public-sync scope is authorized.
