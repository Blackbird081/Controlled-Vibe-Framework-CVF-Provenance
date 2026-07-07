# CVF Agent Work Order - MSEA R43 T2 MinerU Actor Role Persistence Authority Wiring Implementation

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: MSEA_R43_T2_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_IMPLEMENTATION

Dispatch base head: 0d408e163

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: reviewer/closer role

Worker return path: `docs/reviews/CVF_MSEA_R43_T2_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_IMPLEMENTATION_WORKER_RETURN_2026-07-06.md`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA_R43_T2_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_IMPLEMENTATION.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R43_T2_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_IMPLEMENTATION_2026-07-06.md`

Paired baseline: `docs/baselines/CVF_GC018_MSEA_R43_T2_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_IMPLEMENTATION_2026-07-06.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-06; dispatch base head is `0d408e163`.

Do-not-misread notes: This packet does not authorize CVF to control or interfere with agents' internal operation. It authorizes only route-boundary authority checks, evidence, and traceability for `fileBackedPersistenceRequested`.

Required first actions: read required startup files, guard orientation, literal gotchas, this packet, the paired GC-018 baseline, R43-T1 worker return and matrix, source files named in the Source Verification Block, and checker source listed in the Checker Source Read-Ahead Block before writing any artifact.

Return contract: implement only the allowed source/test wiring, create the worker return artifact, run required focused tests and gates, leave changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Implement the accepted R43-T1 Option B design by adding a route-local actor-role authority gate for the MinerU system-chain file-backed persistence decision path. The approved allowlist is `OPERATOR`, `GOVERNOR`. The intended behavior is route-boundary control and traceable responsibility evidence only: an authorized actor role may pass the actor-role gate, unauthorized or missing actor roles must fail closed, and CVF must not claim it is controlling agent internals.

## Authority Chain

- Operator instruction: current session, 2026-07-06, approving the recommended `OPERATOR`, `GOVERNOR` allowlist and requiring clear traceability language.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- Active handoff: `AGENT_HANDOFF_V37_2026-07-06.md`
- Predecessor decision matrix: `docs/reference/CVF_MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN_MATRIX_2026-07-06.md`
- Predecessor worker return: `docs/reviews/CVF_MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN_WORKER_RETURN_2026-07-06.md`
- Paired GC-018 baseline: `docs/baselines/CVF_GC018_MSEA_R43_T2_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_IMPLEMENTATION_2026-07-06.md`

Authority boundary: this work order releases only the narrow source/test implementation scope below. If any cited source contradicts this packet, stop and return `BLOCKED_WITH_REASON`.

## Agent Roles

| Role | Owner | Responsibility |
| --- | --- | --- |
| Operator | Human operator | Approves allowlist and policy intent. |
| Dispatcher | dispatcher role | Authors GC-018 baseline and work order. |
| Worker | Delegated worker | Implements allowed source/test changes and returns without commit. |
| Reviewer/closer | reviewer/closer role | Reviews, may repair allowed-scope packet defects, commits if accepted. |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA_R43_T2_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_IMPLEMENTATION --title "MSEA R43 T2 MinerU Actor Role Persistence Authority Wiring Implementation" --date 2026-07-06 --base 0d408e163 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Filled mission, operator-approved allowlist, source verification, allowed paths, implementation plan, tests, and claim boundary. |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py` |
| docOnlyNewFields | `operatorApprovedFileBackedPersistenceActorRoles`; `agentOperationInterventionBoundary` |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly by reading the failing checker source and matching the literal required shape. Worker should return to orchestrator only for a source contradiction, forbidden-scope need, or missing authority that makes completion impossible.

## Mandatory Gate-Failure Remediation Protocol

- Allowed-scope failures are mandatory remediation. Complete the remediation and execute the failed gate again.
- Missing `N/A with reason`, stale closure residue, source-verification corrections, allowed continuity sync, and routine guard failures are not operator-preference questions.
- Escalation is reserved for remediation that would exceed Allowed scope, change the claim boundary, release a held prerequisite, change risk level, open public-sync, run live/provider proof, consume secrets/quota, touch forbidden paths, or perform destructive or irreversible actions.

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short --untracked-files=all
python governance/compat/check_work_order_dispatch_quality.py --base 0d408e163 --head HEAD --enforce
python governance/compat/check_adif_defect_registry_disclosure.py --base 0d408e163 --head HEAD --enforce
python governance/compat/check_agent_handoff_boundary.py --base 0d408e163 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 0d408e163 --head HEAD
```

Expected result: all pre-dispatch gates pass before the material dispatch commit.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001
- ADIF-0002
- ADIF-0014
- ADIF-0015
- ADIF-0020
- ADIF-0021
- ADIF-0007
- ADIF-0016
- ADIF-0017
- ADIF-0024
- ADIF-0006

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 20 --json` |
| Returned defect count | 11 |
| Returned defects | ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0024; ADIF-0006 |
| Disclosed defectIds | ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0024; ADIF-0006 |
| Dispatch impact | Packet uses source verification, checker read-ahead, exact commit mode, explicit worker scope, and no provider-local authority. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py` |
| literalTokensReviewed | ADIF disclosure query line; Source Verification Block table labels; Negative Search And Collision Discipline; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Worker Return Packet Shape Contract; WORKER_MUST_NOT_COMMIT; DISPATCH_READY |
| gateRunPurpose | Confirm dispatch packet shape and evidence after authoring; not first discovery. |
| claimBoundary | Read-ahead covers dispatch artifact shape only; it does not prove implementation behavior, runtime execution, live provider behavior, public-sync, or production readiness. |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| R43-T1 selected Option B for actor-role authority wiring design. | `docs/reference/CVF_MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN_MATRIX_2026-07-06.md` | Accepted design disposition section | `R43_T1_ACTOR_ROLE_WIRING_DESIGN_READY_FOR_IMPLEMENTATION_PACKET` | R43-T1 decision matrix | ACCEPT |
| Route authority currently has `fileBackedPersistenceRequested`. | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | line 40 | `fileBackedPersistenceRequested` | `MineruSystemChainRouteAuthority` | ACCEPT |
| Route builder currently rejects file-backed persistence requests. | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | lines 105-109 | `FAIL_CLOSED_FILE_BACKED_PERSISTENCE_REQUESTED` | `buildMineruSystemChainRouteCandidate` | ACCEPT |
| Runtime memory actor role vocabulary includes `OPERATOR` and `GOVERNOR`. | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts` | lines 12-22 | `RuntimeMemoryActorRole` | `RuntimeMemoryActorRole` | ACCEPT |
| Existing system-chain route candidate tests cover the current file-backed fail-closed path. | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-system-chain-route-candidate.test.ts` | lines 161-174 | `FAIL_CLOSED_FILE_BACKED_PERSISTENCE_REQUESTED` | `buildMineruSystemChainRouteCandidate` tests | ACCEPT |

## Operator Authority Recording

operatorApprovedFileBackedPersistenceActorRoles: `OPERATOR`, `GOVERNOR`

agentOperationInterventionBoundary: CVF does not intervene in or direct an agent's internal operation. CVF controls only the route boundary where file-backed persistence is requested, records actor-role authority evidence, and requires fail-closed behavior plus traceable proof so later review can attribute which actor role requested or authorized the route.

Authority note: the allowlist is operator-approved dispatch policy recorded by this packet, not a pre-existing runtime source fact.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Baseline path existence | `Test-Path docs/baselines/CVF_GC018_MSEA_R43_T2_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_IMPLEMENTATION_2026-07-06.md` returned `False` before authoring. | PASS |
| Work order path existence | `Test-Path docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R43_T2_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_IMPLEMENTATION_2026-07-06.md` returned `False` before authoring. | PASS |
| Token collision search | `rg -n "MSEA-R43-T2|MSEA_R43_T2|CVF_MSEA_R43_T2" docs/baselines docs/work_orders docs/reviews docs/reference CVF_SESSION CVF_SESSION_MEMORY.md AGENT_HANDOFF_V37_2026-07-06.md` returned only next-move/session references before authoring. | PASS |
| Collision decision | No existing R43-T2 baseline, work order, review, or reference artifact exists; current packet may claim the R43-T2 dispatch identifiers. | PASS |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | Dispatcher authors packet; worker implements and returns; reviewer/closer reviews and commits if accepted. |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=0d408e163; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | Worker may change only the two source/test paths and the worker return path named in this work order. |
| traceScope(phase, actor) | Worker return must record commands, cwd, changed files, test results, and pending worktree status. |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | Before status evidence must be clean or disclose only owned pending paths; unrelated provider-local or IDE files must be removed or disclosed as blockers. |
| nextMoveSurfaces | Worker must not edit session state, front door, or active handoff; reviewer/closer owns any next-move sync after acceptance. |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R43_T2_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_IMPLEMENTATION_COMPLETION_2026-07-06.md` (optional; prefer reviewer decision inside the worker return if evidence is complete) |
| reviewerOwnedClosurePaths | Worker return plus allowed source/test paths if accepted; optional completion review only if worker return cannot safely carry closure evidence. |
| closureOwner | reviewer/closer role |
| workerCommitPermission | FORBIDDEN |

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| routeMode | SINGLE_AGENT_SINGLE_ROLE |
| intakeSummary | User request records approval for the recommended R43-T2 allowlist and asks that the packet clearly state CVF controls evidence and traceability, not agent internal operation. |
| scopeClassification | Bounded allowed scope: two source/test paths plus the worker return path; blast radius is route-boundary actor-role authority for file-backed persistence requests. |
| riskSensitivity | Medium governance risk because the packet touches memory/persistence authority, but no public-sync, provider/live, secret, legal, production readiness, or private-output work is allowed. |
| selectedRoleRoute | routeMode SINGLE_AGENT_SINGLE_ROLE; worker executes and reviewer/closer commits only if accepted. |
| roleSeparationBasis | Worker must not commit; reviewer/closer owns closure decision and any later session-sync. |
| dispatcherRole | dispatcher role |
| workerRole | delegated worker |
| reviewerRole | reviewer/closer role |
| authorityCheckpoint | SATISFIED: `OPERATOR`, `GOVERNOR` allowlist was approved before dispatch. |
| escalationCondition | Stop and return BLOCKED if completion needs forbidden paths, role values beyond the allowlist, live/provider proof, private output, public-sync, production release, or agent-operation intervention. |
| claimBoundary | Role routing only; no provider-specific assignment, provider-local authority, live provider behavior, public-sync, or agent-operation intervention claim. |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: this is an internal dispatch packet responding to operator policy approval, not external knowledge absorption. |
| Matching local-view guard | N/A with reason: no external knowledge intake is consumed or absorbed. |
| Owner surface | This work order and paired GC-018 baseline. |
| Disposition | NOT_APPLICABLE_WITH_REASON: no external source is promoted to CVF authority by this packet. |
| Claim boundary | The section exists only because generic guards require a routing disposition when external-routing vocabulary appears; no external knowledge intake claim is made. |

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V37_2026-07-06.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- `docs/baselines/CVF_GC018_MSEA_R43_T2_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_IMPLEMENTATION_2026-07-06.md`
- `docs/reference/CVF_MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN_MATRIX_2026-07-06.md`
- `docs/reviews/CVF_MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN_WORKER_RETURN_2026-07-06.md`

## Allowed Scope

The worker may edit only:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-system-chain-route-candidate.test.ts`
- `docs/reviews/CVF_MSEA_R43_T2_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_IMPLEMENTATION_WORKER_RETURN_2026-07-06.md`

Implementation requirements:

- Import or reuse `RuntimeMemoryActorRole` only as a type for the new route authority field.
- Add optional `fileBackedPersistenceActorRole?: RuntimeMemoryActorRole` to `MineruSystemChainRouteAuthority`.
- Add a route-local allowlist constant whose values are exactly `OPERATOR`, `GOVERNOR`.
- Add a new fail-closed disposition token for missing or unauthorized file-backed persistence actor role.
- Check actor role before allowing a `fileBackedPersistenceRequested: true` request to pass the actor-role gate.
- Preserve fail-closed behavior for missing, malformed, or unauthorized actor role.
- Preserve current bounded candidate limits: productionRouteAuthorized remains false, held token remains the T25 candidate-only token, retrieval/vectorization/private-output reads remain blocked, and production release remains unclaimed.
- Update focused tests for authorized role, unauthorized role, and missing actor-role behavior.

## Forbidden Scope

- Do not run MinerU runtime, install models, download models, call OCR/VLM/parser/provider APIs, or read private/generated output content.
- Do not invoke file-backed persistence against real filesystem storage.
- Do not widen `MineruSystemChainPersistenceMode` beyond its current source-verified type unless a later packet authorizes that.
- Do not release production durable-store, production Memory/RAG, retrieval, vectorization, private-output reading, public-sync, provider/live proof, standalone app work, or use-case/legal workflow.
- Do not edit `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF*.md`, provider-local config, IDE config, public-sync clone, package root exports, interface/root-barrel wiring, or unrelated tests.
- Do not claim CVF controls agent internals. The claim is route-boundary authority checking and evidence only.
- Do not commit, stage for commit, push, or public-sync.

## Write Ownership

| Path | Worker permission | Reviewer permission |
| --- | --- | --- |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | EDIT_ALLOWED | REVIEW_AND_COMMIT_IF_ACCEPTED |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-system-chain-route-candidate.test.ts` | EDIT_ALLOWED | REVIEW_AND_COMMIT_IF_ACCEPTED |
| `docs/reviews/CVF_MSEA_R43_T2_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_IMPLEMENTATION_WORKER_RETURN_2026-07-06.md` | CREATE_ALLOWED | REVIEW_AND_COMMIT_IF_ACCEPTED |
| Any other path | FORBIDDEN | N/A with reason: outside R43-T2 allowed scope |

## Worker Output Checker Read-Ahead Mandate

Before writing the worker return, read checker source for the review path family and conditional content class. The worker return must include review-class sections for Target / Source, Scope / Methodology, Findings / Position, Risk / Corrective Action, Decision / Disposition, External Knowledge Intake Routing, Epistemic Process Block, Agent Operation Trace Block, Delta Execution Claim Boundary Control Block, Public Export Disposition, verification commands, changed files, and git status.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | Implement the actor-role field, allowlist, and fail-closed route-boundary check. |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-system-chain-route-candidate.test.ts` | Add or update focused tests for approved, missing, and unauthorized actor roles. |
| `docs/reviews/CVF_MSEA_R43_T2_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_IMPLEMENTATION_WORKER_RETURN_2026-07-06.md` | Record execution evidence, tests, gates, claim boundary, and pending worktree status. |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R43_T2_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_IMPLEMENTATION_WORKER_RETURN_2026-07-06.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Shape-list rule: when listing required worker-output sections, write section names without heading prefixes. Reserve actual heading syntax for real sections so structural checkers do not treat this checklist as the artifact section body.

## Verification Commands

```powershell
git rev-parse --short HEAD
git status --short --untracked-files=all
npx vitest run EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-system-chain-route-candidate.test.ts
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 0d408e163 --head HEAD
git diff --name-status
git status --short --untracked-files=all
```

If the package runner requires running from `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION`, record the exact command and working directory in the worker return. Do not substitute a broad test run for the focused route-candidate test unless the focused command is unavailable and the failure is documented.

## Evidence Requirements

Required worker evidence:

- `executionBaseHead`
- exact `git status --short --untracked-files=all` before and after edits
- exact focused test command and PASS/BLOCKED result
- exact worker-return fast gate result
- exact pre-implementation autorun result
- `git diff --name-status` showing only allowed paths
- claim-boundary statement confirming route-boundary authority only

## Execution Plan

1. Capture `executionBaseHead` and clean or pending worktree status.
2. Read required files and checker sources.
3. Edit only the allowed source/test files.
4. Create the worker return from the checker-safe scaffold.
5. Run the focused test and required worker-return/pre-implementation gates.
6. Record exact command results and pending changed files.
7. Return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` without committing.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher role |
| Provider or surface | local workspace |
| Session or invocation | MSEA_R43_T2_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_IMPLEMENTATION dispatch, 2026-07-06 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | `Get-Content`; `rg`; `Test-Path`; `python governance/compat/run_adif_defect_resolver.py`; `python governance/compat/build_dispatch_packet_scaffold.py`; `apply_patch`; governance gates |
| Target paths | This work order, paired GC-018 baseline, planned source/test path set, planned worker return path |
| Allowed scope source | Active session next allowed move plus operator-approved `OPERATOR`, `GOVERNOR` allowlist |
| Before status evidence | clean worktree: `git rev-parse --short HEAD` returned `0d408e163`; `git status --short --untracked-files=all` was empty before authoring. |
| After status evidence | Pending dispatch artifacts until material commit. |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | Operator approved the allowlist and asked to record clearly that CVF controls evidence/traceability, not agent internals. |
| Claim boundary | Dispatch packet only; no implementation behavior is proven until worker execution and reviewer acceptance. |
| Agent type | dispatcher |
| Invocation ID | `msea-r43-t2-mineru-actor-role-persistence-authority-wiring-implementation-dispatch-2026-07-06` |
| Expected manifest | `docs/baselines/CVF_GC018_MSEA_R43_T2_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_IMPLEMENTATION_2026-07-06.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R43_T2_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_IMPLEMENTATION_2026-07-06.md` |
| Actual changed set | `docs/baselines/CVF_GC018_MSEA_R43_T2_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_IMPLEMENTATION_2026-07-06.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R43_T2_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_IMPLEMENTATION_2026-07-06.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: dispatch authoring creates two new governed artifacts only. |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R43-T2 source/test implementation dispatch for route-boundary actor-role authority only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: dispatch authority and source facts are recorded; implementation behavior remains pending worker execution and reviewer acceptance. |
| receiptEvidence | N/A with reason: dispatch packet creates no runtime receipt. |
| actionEvidence | N/A with reason: no route or agent runtime action is executed by this dispatch. |
| invocationBoundary | Local governed file editing and deterministic focused test execution only after worker starts. |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, IDE control, shell control, provider control, or agent-internal control is claimed. |
| claimLanguage | CVF records route-boundary authority and traceability for file-backed persistence requests. |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router behavior, production release, or agent-operation intervention without fresh source-verified authorization. |

## Acceptance Criteria

- Source adds `fileBackedPersistenceActorRole?: RuntimeMemoryActorRole` and a route-local allowlist containing exactly `OPERATOR`, `GOVERNOR`.
- Missing or unauthorized actor roles fail closed with the new actor-role disposition token before any route candidate writes through.
- Authorized `OPERATOR` and `GOVERNOR` actor roles may pass the actor-role gate while the broader bounded-candidate production release remains false.
- Focused route-candidate tests cover authorized, unauthorized, and missing actor-role cases.
- Worker return records exact commands, focused test results, worker-return fast gate result, pre-implementation gate result, changed files, and pending worktree status.
- No forbidden path, provider-local file, IDE config, private output, runtime execution, live/provider proof, public-sync, push, or commit is introduced.

## Fail Conditions

- Worker invents or changes the allowlist beyond `OPERATOR`, `GOVERNOR`.
- Worker claims CVF controls agent internals instead of route-boundary authority and traceability.
- Worker edits outside allowed paths.
- Worker widens persistence mode, invokes file-backed persistence, releases production Memory/RAG, reads private/generated output, or runs provider/live proof.
- Worker omits focused negative tests for missing or unauthorized actor role.
- Worker commits, stages for commit, pushes, or public-syncs.

## Review Gate

Reviewer acceptance requires:

- Worker return fast gate PASS.
- Focused route-candidate test PASS or BLOCKED with reason that does not hide source/test failures.
- Pre-implementation autorun gate PASS on the worker changed set.
- Reviewer confirms diff stays inside Allowed Scope.
- Reviewer confirms the claim boundary remains route-boundary control/evidence only, not agent-operation intervention.

## Operator Checkpoint

Status: SATISFIED

Checkpoint evidence: operator approved the recommended allowlist `OPERATOR`, `GOVERNOR` and directed the dispatch packet to record clearly that CVF does not interfere with agent operation, but requires controls, evidence, traceability, and responsibility review at each route-boundary step.

## Closure Checklist

- [ ] Worker return exists and records `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.
- [ ] Focused route-candidate tests passed or blocker is explicit.
- [ ] Worker-return fast gate passed.
- [ ] Pre-implementation autorun gate passed on worker changed set.
- [ ] Changed files are inside Write Ownership.
- [ ] No forbidden runtime, provider/live, private-output, public-sync, production-release, commit, or push action occurred.
- [ ] Reviewer decision recorded before any material commit.

## Claim Boundary

This work order authorizes only a narrow no-commit implementation tranche for route-boundary actor-role authority wiring and focused tests. It does not authorize MinerU runtime execution, private/generated output content read, real file-backed persistence invocation, persistence-mode widening, production durable-store invocation, production Memory/RAG route invocation or release, retrieval, vectorization, provider/live proof, Web/UI implementation, public-sync, standalone app work, legal/use-case deep dive, extraction accuracy, document truth, legal quality, current-law correctness, hosted release claim, production release claim, interface/root-barrel/runtime wiring, provider-local or IDE config edits, worker commit, push, or public claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch packet only; no public-sync scope is authorized.
