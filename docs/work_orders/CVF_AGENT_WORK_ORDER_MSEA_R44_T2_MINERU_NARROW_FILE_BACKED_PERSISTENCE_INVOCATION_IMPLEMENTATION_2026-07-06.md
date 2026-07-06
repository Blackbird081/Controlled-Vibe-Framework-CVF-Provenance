# CVF Agent Work Order - MSEA R44 T2 MinerU Narrow File Backed Persistence Invocation Implementation

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

rawMemoryReleased=false

Batch ID: MSEA_R44_T2_MINERU_NARROW_FILE_BACKED_PERSISTENCE_INVOCATION_IMPLEMENTATION

Dispatch base head: 31472cfcc

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: Codex reviewer/closer

Worker return path: `docs/reviews/CVF_MSEA_R44_T2_MINERU_NARROW_FILE_BACKED_PERSISTENCE_INVOCATION_IMPLEMENTATION_WORKER_RETURN_2026-07-06.md`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA_R44_T2_MINERU_NARROW_FILE_BACKED_PERSISTENCE_INVOCATION_IMPLEMENTATION.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R44_T2_MINERU_NARROW_FILE_BACKED_PERSISTENCE_INVOCATION_IMPLEMENTATION_2026-07-06.md`

Paired GC-018 baseline: `docs/baselines/CVF_GC018_MSEA_R44_T2_MINERU_NARROW_FILE_BACKED_PERSISTENCE_INVOCATION_IMPLEMENTATION_2026-07-06.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-06; dispatch base head is `31472cfcc`.

Do-not-misread notes: this packet authorizes a narrow source/test implementation and focused deterministic tests only. It does not authorize MinerU runtime execution, private/generated output content reads, provider/live proof, production Memory/RAG release, retrieval, vectorization, public-sync, worker commit, push, or use-case/legal workflow.

Required first actions: read required startup files, guard orientation, literal gotchas, this packet, the paired GC-018 baseline, R44-T1 decision matrix and worker return, the current source/test files named in the Source Verification Block, and all checker source listed in the Checker Source Read-Ahead Block before writing any artifact.

Return contract: implement only the allowed source/test change, create the worker return artifact, run focused tests and required gates, leave changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Implement the accepted R44-T1 next move by widening the MinerU system-chain route candidate just enough to accept file-backed persistence when an OPERATOR or GOVERNOR actor role passes the existing route-local actor gate. The implementation must keep production Memory/RAG release false, preserve no-private-output and no-provider boundaries, and prove behavior only with focused deterministic tests.

## Authority Chain

| Authority source | Role in this dispatch |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | Current front-door continuity and R44-T2 next-move context |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Canonical active mode, active handoff, and session state |
| `AGENT_HANDOFF_V37_2026-07-06.md` | Active handoff named by the state registry |
| `docs/reference/guard_orientation/README.md` | Guard routing for dispatch and worker execution |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | Literal-format guardrails |
| `docs/reference/CVF_MSEA_R44_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_RECHECK_OR_STOP_DECISION_MATRIX_2026-07-06.md` | Accepted decision selecting narrow invocation packet readiness |
| `docs/reviews/CVF_MSEA_R44_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_RECHECK_OR_STOP_WORKER_RETURN_2026-07-06.md` | Accepted worker-return evidence and reviewer acceptance |
| Current source files named in Source Verification Block | Runtime/source evidence for allowed implementation surface |

## Agent Roles

| Role | Responsibility | Commit authority |
| --- | --- | --- |
| Dispatcher | Author GC-018 baseline and work order | May commit dispatch artifacts if gates pass |
| Worker | Edit only allowed source/test paths and create worker return | WORKER_MUST_NOT_COMMIT |
| Reviewer/closer | Review worker return, run closure gates, decide acceptance, and own material/session-sync commits | Reviewer-owned |
| Operator | Owns any future production, provider/live, public, or use-case checkpoint | N/A |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA_R44_T2_MINERU_NARROW_FILE_BACKED_PERSISTENCE_INVOCATION_IMPLEMENTATION --title "MSEA R44 T2 MinerU Narrow File Backed Persistence Invocation Implementation" --date 2026-07-06 --base 31472cfcc --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Filled R44-T2 purpose, dependency evidence, source verification, ADIF disclosure, handoff control, allowed scope, verification commands, and claim boundaries |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| docOnlyNewFields | R44_T2_NARROW_FILE_BACKED_PERSISTENCE_INVOCATION_IMPLEMENTATION |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly by reading the failing checker source and matching the literal required shape. Worker should return to orchestrator only for a source contradiction, forbidden-scope need, or missing authority that makes completion impossible.

## Pre-Flight Checks

| Check | Required worker evidence |
| --- | --- |
| Execution base | Record `git rev-parse --short HEAD` before writing |
| Clean worktree | Record `git status --short --untracked-files=all` before writing |
| Required reads | List startup, guard, dispatch, predecessor, source, test, and checker files actually read |
| Scope confirmation | Confirm only the two allowed source/test paths and one worker return path are changed |
| Provider-local hygiene | Confirm no provider-local stray files or IDE config changes were created |

## Mandatory Gate-Failure Remediation Protocol

- Allowed-scope failures are mandatory remediation. Complete the remediation and execute the failed gate again.
- Missing `N/A with reason`, stale closure residue, source-verification corrections, allowed worker-return repair, and routine guard failures are not operator-preference questions.
- Escalation is reserved for remediation that would exceed Allowed Scope, release production behavior, consume secrets or live quota, touch forbidden paths, change risk posture, public-sync, run MinerU runtime, read private/generated output content, or perform destructive filesystem actions.

## Dependency Release Evidence

| Dependency | Required evidence | Refreshed evidence | Disposition |
| --- | --- | --- | --- |
| R44-T1 release readiness | Accepted decision selecting a future narrow invocation packet | R44-T1 decision matrix selects `R44_T1_FILE_BACKED_PERSISTENCE_RELEASE_READY_FOR_NARROW_INVOCATION_PACKET`; worker return records reviewer decision `ACCEPTED_FOR_MATERIAL_COMMIT`; material commit `c892ba922`; session-sync commit `31472cfcc` | SATISFIED |
| R43-T2 actor-role route gate | Accepted implementation of OPERATOR/GOVERNOR route-local authority | Route source currently includes `fileBackedPersistenceActorRole` and `FILE_BACKED_PERSISTENCE_ACTOR_ROLE_ALLOWLIST`; focused tests prove authorized and unauthorized behavior | SATISFIED |
| Production boundary | The packet must keep production release and public claims closed | Source result type has `productionRouteAuthorized: false`; R44-T1 claim boundary forbids production Memory/RAG release and public claim | SATISFIED |

## Roadmap-to-Work-Order Trace Matrix

| Predecessor decision | Required next action | R44-T2 handling |
| --- | --- | --- |
| R41-T1 and R41-T2 held file-backed persistence pending authority gaps | Do not invoke until authority gap is source-resolved | R43-T2 resolved route-local actor role authority; R44-T1 selected narrow invocation packet readiness |
| R44-T1 selected readiness for a narrow invocation packet | Author a source-verified implementation work order before any source/test edit | This work order releases only the narrow source/test implementation path |
| Operator warning to avoid use-case drift | Keep system-chain foundation work bounded | R44-T2 forbids legal/use-case workflow, public claim, extraction accuracy, document truth, and current-law correctness claims |

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
| literalTokensReviewed | Source Verification Block; ADIF Defect Registry Disclosure; Checker Source Read-Ahead Block; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Work-Order Fulfillment Manifest; Worker Return Packet Shape Contract; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; WORKER_MUST_NOT_COMMIT; DISPATCH_READY; ACCEPT; VALUE_SET; EXISTS; RUNTIME_BEHAVIOR; DOC_ONLY_NEW; N/A with reason |
| gateRunPurpose | Confirmation after source-read authoring; gate runs are evidence and not first discovery for packet shape |
| claimBoundary | Read-ahead covers dispatch artifact shape only; it does not prove implementation behavior, runtime execution, live provider behavior, public-sync, or production readiness |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R44-T1 selected readiness for a future narrow invocation implementation packet | VALUE_SET | `docs/reference/CVF_MSEA_R44_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_RECHECK_OR_STOP_DECISION_MATRIX_2026-07-06.md` | lines 56-58 and 77-79 | `R44_T1_FILE_BACKED_PERSISTENCE_RELEASE_READY_FOR_NARROW_INVOCATION_PACKET` | R44-T1 decision matrix | ACCEPT |
| Route candidate currently imports the runtime actor-role type | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | line 15 | `RuntimeMemoryActorRole` | MinerU system-chain route candidate | ACCEPT |
| Route authority contains explicit file-backed request and actor-role fields | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | lines 49-60 | `MineruSystemChainRouteAuthority` | MinerU system-chain route candidate | ACCEPT |
| Current persistence mode type remains restricted to in-process-only and must be widened by this implementation | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | line 46 | `MineruSystemChainPersistenceMode` | MinerU system-chain route candidate | ACCEPT |
| Current route still blocks authorized file-backed requests with the bounded cap token | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | lines 125-144 | `FAIL_CLOSED_FILE_BACKED_PERSISTENCE_REQUESTED` | `buildMineruSystemChainRouteCandidate` | ACCEPT |
| Current result shape keeps production route unauthorized while carrying a persistence mode value | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | lines 71-79 and 188-197 | `MineruSystemChainRouteCandidateResult` | MinerU system-chain route candidate result | ACCEPT |
| Focused tests already prove authorized OPERATOR and GOVERNOR pass the actor gate but still hit the bounded cap | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-system-chain-route-candidate.test.ts` | lines 249-290 | `FAIL_CLOSED_FILE_BACKED_PERSISTENCE_REQUESTED` | MinerU system-chain route candidate tests | ACCEPT |
| Focused tests already prove missing and unauthorized actor roles fail closed | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-system-chain-route-candidate.test.ts` | lines 292-361 | `FAIL_CLOSED_FILE_BACKED_PERSISTENCE_ACTOR_ROLE_NOT_AUTHORIZED` | MinerU system-chain route candidate tests | ACCEPT |
| Durable memory store exposes a file-backed constructor and keeps raw-memory receipt invariants false | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 35-49 and 106-110 | `createFileBackedDurableMemoryStore` | Durable memory store | ACCEPT |
| Durable memory store writes summary-only records through policy-gated write behavior | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 195-305 | `write` | `DurableMemoryStore` | ACCEPT |
| Runtime actor role vocabulary includes OPERATOR and GOVERNOR | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts` | lines 12-14 | `RuntimeMemoryActorRole` | Runtime memory hierarchy | ACCEPT |
| Internal harness currently defaults file-backed persistence off and must remain untouched by this packet | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-internal-system-chain-harness.ts` | lines 107-115 and 139-155 | `fileBackedPersistenceUsed` | MinerU internal system-chain harness | ACCEPT |

## New Doc-Only Fields

| Field | Owner artifact | Purpose | Runtime/source status |
| --- | --- | --- | --- |
| `R44_T2_NARROW_FILE_BACKED_PERSISTENCE_INVOCATION_IMPLEMENTATION` | This work order and paired baseline | Batch identifier for the narrow implementation dispatch | DOC_ONLY_NEW |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Path existence for R44-T2 baseline before authoring | `Test-Path docs/baselines/CVF_GC018_MSEA_R44_T2_MINERU_NARROW_FILE_BACKED_PERSISTENCE_INVOCATION_IMPLEMENTATION_2026-07-06.md` returned `False` before authoring | ACCEPT |
| Path existence for R44-T2 work order before authoring | `Test-Path docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R44_T2_MINERU_NARROW_FILE_BACKED_PERSISTENCE_INVOCATION_IMPLEMENTATION_2026-07-06.md` returned `False` before authoring | ACCEPT |
| Path existence for R44-T2 worker return before authoring | `Test-Path docs/reviews/CVF_MSEA_R44_T2_MINERU_NARROW_FILE_BACKED_PERSISTENCE_INVOCATION_IMPLEMENTATION_WORKER_RETURN_2026-07-06.md` returned `False` before authoring | ACCEPT |
| Token search before authoring | `rg -n "MSEA-R44-T2|MSEA_R44_T2|CVF_MSEA_R44_T2" docs CVF_SESSION CVF_SESSION_MEMORY.md AGENT_HANDOFF_V37_2026-07-06.md EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests` returned no matches before authoring | ACCEPT |
| Collision decision | No existing R44-T2 packet or worker-output path was present | ACCEPT |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | Dispatcher authors packet; worker implements and returns; reviewer/closer reviews and commits if accepted |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=31472cfcc; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | Worker may edit only the two allowed source/test files and create the worker return listed in Work-Order Fulfillment Manifest |
| traceScope(phase, actor) | Worker return must record commands, cwd, changed files, focused test results, pre-implementation gate result, pending status, manifest match, and no-commit evidence |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | Before status evidence must be clean or disclose only owned pending paths; unrelated provider-local or IDE files must be removed or disclosed as blockers |
| nextMoveSurfaces | Worker must not edit session state, front door, or active handoff; reviewer/closer owns any next-move sync after acceptance |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R44_T2_MINERU_NARROW_FILE_BACKED_PERSISTENCE_INVOCATION_IMPLEMENTATION_COMPLETION_2026-07-06.md` (optional; prefer reviewer decision inside the worker return if evidence is complete) |
| reviewerOwnedClosurePaths | Worker return plus allowed source/test paths if accepted; optional completion review only if worker return cannot safely carry closure evidence; active session state source fragments; generated active session state; active handoff; session memory front door |
| closureOwner | Codex reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| routeMode | SINGLE_AGENT_SINGLE_ROLE |
| intakeSummary | User requested continuation work order using accepted R44-T1 closure evidence; R44-T1 authorized a future narrow invocation implementation packet only |
| scopeClassification | Bounded source/test implementation for route-candidate file-backed persistence behavior under the existing actor-role gate |
| riskSensitivity | Medium governance risk because the packet touches persistence authority; no provider/live, private-output, public-sync, production release, or use-case/legal work is allowed |
| selectedRoleRoute | routeMode SINGLE_AGENT_SINGLE_ROLE; delegated worker implements and reviewer/closer owns acceptance and commits |
| roleSeparationBasis | Worker must not commit; reviewer/closer owns closure decision and any session-sync |
| dispatcherRole | dispatcher role |
| workerRole | delegated worker |
| reviewerRole | reviewer/closer role |
| authorityCheckpoint | SATISFIED: R44-T1 accepted source-verified readiness for a narrow invocation packet |
| escalationCondition | Stop and return BLOCKED if completion needs forbidden paths, role values beyond OPERATOR/GOVERNOR, MinerU runtime, private output, provider/live proof, production release, public-sync, use-case/legal workflow, or agent-operation intervention |
| claimBoundary | Role routing only; no provider-specific assignment, provider-local authority, live provider behavior, public-sync, or agent-operation intervention claim |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: R44-T2 uses only CVF-governed source files and accepted CVF review artifacts |
| Matching local-view guard | N/A with reason: no external knowledge intake event occurred |
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
| `docs/reference/CVF_MSEA_R44_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_RECHECK_OR_STOP_DECISION_MATRIX_2026-07-06.md` | Accepted predecessor decision |
| `docs/reviews/CVF_MSEA_R44_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_RECHECK_OR_STOP_WORKER_RETURN_2026-07-06.md` | Accepted predecessor worker return |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | Current route candidate source |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-system-chain-route-candidate.test.ts` | Current route candidate tests |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | Durable store and receipt evidence |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts` | Actor role source vocabulary |
| checker files listed in Checker Source Read-Ahead Block | Output-shape authority |

## Allowed Scope

The worker may edit only:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-system-chain-route-candidate.test.ts`
- `docs/reviews/CVF_MSEA_R44_T2_MINERU_NARROW_FILE_BACKED_PERSISTENCE_INVOCATION_IMPLEMENTATION_WORKER_RETURN_2026-07-06.md`

Implementation requirements:

- Widen `MineruSystemChainPersistenceMode` only enough to represent the file-backed route mode while preserving existing in-process behavior.
- Preserve the existing `fileBackedPersistenceActorRole` field and OPERATOR/GOVERNOR allowlist check.
- Missing, null, malformed, or unauthorized file-backed actor roles must still fail closed before route candidate acceptance.
- Authorized OPERATOR and GOVERNOR requests may pass the actor gate and use file-backed mode only when the route authority explicitly requests file-backed persistence and the production persistence mode is the widened file-backed value.
- Preserve `productionRouteAuthorized: false` and `PRODUCTION_MEMORY_RAG_ROUTE_NOT_RELEASED_BY_T25_CANDIDATE_ONLY`.
- Preserve retrieval, vectorization, private/generated output content read, provider/live, and public-sync fail-closed boundaries.
- Focused tests must prove in-process behavior still passes, missing/unauthorized roles still fail, authorized file-backed route behavior passes using a deterministic temporary file-backed durable store, and receipt invariants remain summary-only with `canReinject` false and `rawMemoryReleased` false.

## Forbidden Scope

- Do not run MinerU runtime, install models, download models, call OCR/VLM/parser/provider APIs, or read private/generated output content.
- Do not perform production file-backed persistence, production durable-store invocation, production Memory/RAG release, retrieval, vectorization, public-sync, provider/live proof, standalone app work, Web/UI implementation, or use-case/legal workflow.
- Do not edit durable memory store implementation, runtime memory hierarchy, internal harness, package root exports, interface/root-barrel wiring, session state, handoffs, front door, provider-local files, IDE config, public-sync clone, hook catalogs, or unrelated tests.
- Do not expand the actor allowlist beyond OPERATOR and GOVERNOR.
- Do not claim CVF controls agent internals. The claim is route-boundary authority checking, evidence, and traceability only.
- Do not commit, stage for commit, push, public-sync, or leave stray provider-local files such as `.qwen/settings.json`.

## Write Ownership

| Path | Worker permission | Reviewer permission |
| --- | --- | --- |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | EDIT_ALLOWED | REVIEW_AND_COMMIT_IF_ACCEPTED |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-system-chain-route-candidate.test.ts` | EDIT_ALLOWED | REVIEW_AND_COMMIT_IF_ACCEPTED |
| `docs/reviews/CVF_MSEA_R44_T2_MINERU_NARROW_FILE_BACKED_PERSISTENCE_INVOCATION_IMPLEMENTATION_WORKER_RETURN_2026-07-06.md` | CREATE_ALLOWED | REVIEW_AND_COMMIT_IF_ACCEPTED |
| Any other path | FORBIDDEN | N/A with reason: outside R44-T2 allowed scope |

## Worker Output Checker Read-Ahead Mandate

Before writing the worker return, read checker source for the review path family and conditional content class. The worker return must include review-class sections for Purpose, Target / Source, Scope / Methodology, Findings / Position, Risk / Corrective Action, Decision / Disposition, External Knowledge Intake Routing, Epistemic Process Block, Agent Operation Trace Block, Delta Execution Claim Boundary Control Block, Public Export Disposition, verification commands, changed files, no-commit statement, and git status.

Shape-list rule: when listing required worker-output sections, write section names without heading prefixes. Reserve actual heading syntax for real sections so structural checkers do not treat this checklist as the artifact section body.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | Implement narrow file-backed route acceptance under existing actor-role gate while keeping production route authorization false |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-system-chain-route-candidate.test.ts` | Add or update focused deterministic tests for authorized file-backed mode, unauthorized roles, missing roles, and in-process regression behavior |
| `docs/reviews/CVF_MSEA_R44_T2_MINERU_NARROW_FILE_BACKED_PERSISTENCE_INVOCATION_IMPLEMENTATION_WORKER_RETURN_2026-07-06.md` | Record execution evidence, tests, gates, claim boundary, hygiene checks, and pending worktree status |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| foundationStorageChange | N/A with reason: R44-T2 does not change governed foundation storage layout or create durable governance storage files |
| durableStoreRuntimeChange | BOUNDED_TEST_ONLY: deterministic focused tests may use a temporary file-backed durable store fixture; production durable-store invocation remains forbidden |
| indexOrCatalogChange | N/A with reason: no index, catalog, public-sync, or storage-layout update is authorized |
| claimBoundary | The packet authorizes route source/test behavior only; it does not change production storage layout or public catalog state |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R44_T2_MINERU_NARROW_FILE_BACKED_PERSISTENCE_INVOCATION_IMPLEMENTATION_WORKER_RETURN_2026-07-06.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Shape-list rule: when listing required worker-output sections, write section names without the `##` prefix. Reserve actual heading syntax for real sections so structural checkers do not treat this checklist as the artifact section body.

## Verification Commands

```powershell
git rev-parse --short HEAD
git status --short --untracked-files=all
npx vitest run EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-system-chain-route-candidate.test.ts
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
git diff --name-status
git status --short --untracked-files=all
```

If the package runner requires running from `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION`, record the exact command and working directory in the worker return. Do not substitute a broad test run for the focused route-candidate test unless the focused command is unavailable and the failure is documented.

## Evidence Requirements

| Evidence | Required form |
| --- | --- |
| executionBaseHead | `git rev-parse --short HEAD` captured before edits |
| Worktree before/after | Exact `git status --short --untracked-files=all` output before and after edits |
| Focused test | Exact command and PASS/BLOCKED result for route-candidate test |
| Worker-return gate | Exact `python governance/compat/run_worker_return_fast_gate.py` result |
| Pre-implementation gate | Exact command with execution base and PASS/BLOCKED result |
| Changed set | `git diff --name-status` plus pending status showing only allowed paths |
| Provider-local hygiene | Evidence that no provider-local or IDE config file was created |
| Claim boundary | Explicit no MinerU runtime, no private output, no provider/live, no production Memory/RAG, no public-sync, no use-case/legal claim |

## Execution Plan

1. Capture `executionBaseHead` and clean or disclosed worktree status.
2. Read mandatory startup, guard, dispatch, predecessor, source, test, and checker files.
3. Edit only the allowed route source and focused route test.
4. Preserve the existing OPERATOR/GOVERNOR actor-role gate and forbidden-scope boundaries.
5. Add or update focused deterministic tests, including test-only temporary file-backed durable store behavior.
6. Create the worker return from checker-safe shape.
7. Run focused test and required worker-return/pre-implementation gates.
8. Record exact command results, changed files, provider-local hygiene, and no-commit statement.
9. Return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` without committing.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher role |
| Provider or surface | local workspace |
| Session or invocation | MSEA_R44_T2_MINERU_NARROW_FILE_BACKED_PERSISTENCE_INVOCATION_IMPLEMENTATION dispatch, 2026-07-06 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | `Get-Content`; `rg`; `Test-Path`; `python governance/compat/run_adif_defect_resolver.py`; `python governance/compat/build_dispatch_packet_scaffold.py`; `apply_patch`; governance gates |
| Target paths | This work order, paired GC-018 baseline, planned source/test path set, planned worker return path |
| Allowed scope source | Active session next allowed move plus R44-T1 accepted decision matrix and worker return |
| Before status evidence | clean worktree: `git rev-parse --short HEAD` returned `31472cfcc`; `git status --short --untracked-files=all` was empty before authoring. |
| After status evidence | Pending dispatch artifacts until material commit. |
| Diff evidence | `git diff --name-status` before material commit |
| Deletion or rename disposition | N/A with reason: dispatch authoring creates two new governed artifacts only. |
| Approval boundary | Operator requested continuation work order; R44-T1 authorizes only a future narrow invocation implementation packet |
| Claim boundary | Dispatch packet only; no implementation behavior is proven until worker execution and reviewer acceptance |
| Agent type | dispatcher |
| Invocation ID | `msea-r44-t2-mineru-narrow-file-backed-persistence-invocation-implementation-dispatch-2026-07-06` |
| Expected manifest | `docs/baselines/CVF_GC018_MSEA_R44_T2_MINERU_NARROW_FILE_BACKED_PERSISTENCE_INVOCATION_IMPLEMENTATION_2026-07-06.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R44_T2_MINERU_NARROW_FILE_BACKED_PERSISTENCE_INVOCATION_IMPLEMENTATION_2026-07-06.md` |
| Actual changed set | `docs/baselines/CVF_GC018_MSEA_R44_T2_MINERU_NARROW_FILE_BACKED_PERSISTENCE_INVOCATION_IMPLEMENTATION_2026-07-06.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R44_T2_MINERU_NARROW_FILE_BACKED_PERSISTENCE_INVOCATION_IMPLEMENTATION_2026-07-06.md` |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R44-T2 narrow file-backed persistence route source/test implementation dispatch |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: dispatch authority and source facts are recorded; implementation behavior remains pending worker execution and reviewer acceptance |
| receiptEvidence | N/A with reason: dispatch packet creates no runtime receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT: governed dispatch artifacts only |
| invocationBoundary | Local governed file editing and deterministic focused test execution only after worker starts |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, IDE control, shell control, provider control, or agent-internal control is claimed |
| claimLanguage | CVF records route-boundary authority and traceability for file-backed persistence requests |
| forbiddenExpansion | Do not expand into MinerU runtime, provider/live, public, package, Web/MCP/model-router behavior, production release, or agent-operation intervention without fresh source-verified authorization |

## Acceptance Criteria

- `MineruSystemChainPersistenceMode` is widened only for the narrow file-backed route mode required by this packet.
- Authorized OPERATOR and GOVERNOR file-backed requests pass the actor-role gate and can produce an accepted bounded route candidate with `productionRouteAuthorized` false.
- Missing, null, malformed, or unauthorized actor roles still fail closed with `FAIL_CLOSED_FILE_BACKED_PERSISTENCE_ACTOR_ROLE_NOT_AUTHORIZED`.
- In-process default behavior remains accepted and backward compatible.
- Focused deterministic tests cover authorized file-backed mode, unauthorized/missing actor roles, and in-process regression.
- Worker return records exact commands, focused test result, worker-return fast gate result, pre-implementation gate result, changed files, provider-local hygiene, and pending worktree status.
- No forbidden path, provider-local file, IDE config, private output, MinerU runtime, live/provider proof, public-sync, push, or commit is introduced.

## Fail Conditions

- Worker expands the allowlist beyond OPERATOR and GOVERNOR.
- Worker claims CVF controls agent internals instead of route-boundary authority and traceability.
- Worker edits outside Write Ownership.
- Worker runs MinerU runtime, reads private/generated output, runs provider/live proof, public-syncs, or enters use-case/legal workflow.
- Worker releases production Memory/RAG, retrieval, vectorization, production durable-store behavior, or public claim.
- Worker omits focused negative tests for missing or unauthorized actor role.
- Worker commits, stages for commit, pushes, or leaves stray provider-local files.

## Review Gate

Reviewer acceptance requires:

- Worker return fast gate PASS.
- Focused route-candidate test PASS or BLOCKED with reason that does not hide source/test failures.
- Pre-implementation autorun gate PASS on the worker changed set.
- Reviewer confirms diff stays inside Write Ownership.
- Reviewer confirms the claim boundary remains bounded route source/test behavior only, not production release or agent-operation intervention.

## Closure Checklist

| Item | Required closure handling |
| --- | --- |
| Worker changed-set manifest | Must match Work-Order Fulfillment Manifest or return blocked |
| Focused test evidence | Must pass or cite an explicit blocker |
| Worker return fast gate | Must pass or cite reviewer-owned repair |
| Autorun gate | Must run on proper execution range and be dispositioned |
| Commit ownership | Worker must not commit; reviewer/closer owns accepted material commit |
| Session sync | Reviewer/closer updates next-move surfaces only after acceptance |
| Public export | Must remain private-only unless a future public-sync packet authorizes export |

## Operator Checkpoint

| Field | Value |
| --- | --- |
| Current checkpoint | Operator asked to continue work-order creation using accepted R44-T1 closure evidence |
| Worker checkpoint need | N/A with reason: worker can complete the source/test implementation within the authorized scope |
| Future checkpoint | Required before MinerU runtime, private-output read, provider/live proof, production Memory/RAG release, public-sync, push, or use-case/legal workflow |

## Claim Boundary

This work order authorizes only a narrow no-commit source/test implementation tranche for route-candidate file-backed persistence behavior under the existing actor-role gate. It does not authorize MinerU runtime execution, private/generated output content read, production durable-store invocation, production Memory/RAG route invocation or release, retrieval, vectorization, provider/live proof, Web/UI implementation, public-sync, standalone app work, legal/use-case deep dive, extraction accuracy, document truth, legal quality, current-law correctness, hosted release claim, production release claim, interface/root-barrel/runtime wiring, provider-local or IDE config edits, worker commit, push, or public claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: This is a private provenance dispatch packet only; no public-sync scope is authorized.
