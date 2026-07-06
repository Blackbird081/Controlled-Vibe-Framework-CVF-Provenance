# CVF Agent Work Order - MSEA R41 T2 MinerU Persistence Mode Authorization Decision

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION

Dispatch base head: b5c200480

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: reviewer or delegated reviewer

Worker return path: `docs/reviews/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_WORKER_RETURN_2026-07-06.md`

## Dispatch Prompt Envelope

Role: delegated docs-only authority-decision worker for MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_2026-07-06.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-06; current session state points from accepted R41-T1 completion review `docs/reviews/CVF_MSEA_R41_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_AUTHORITY_DECISION_COMPLETION_2026-07-06.md` at material commit `51216fb9a` to this persistence-mode authorization packet.

Do-not-misread notes: This packet is not implementation authority and not a production route release. Do not edit source/test files, run MinerU, read private/generated output, invoke file-backed persistence, invoke production durable-store behavior, release Memory/RAG, run provider/live proof, public-sync, commit, push, or make public claims.

Required first actions: read required startup files, guard orientation, literal gotchas, this packet, the paired GC-018 baseline, R41-T1 accepted artifacts, runtime source rows in the Source Verification Block, and all checker source listed in the Checker Source Read-Ahead Block before writing any artifact.

Return contract: create the decision matrix and worker return artifact, run required gates, leave changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Execute the R41-T2 docs-only authority decision for MinerU persistence mode. The worker must decide whether a later narrow implementation packet may be authored to allow `fileBackedPersistenceRequested` true, must remain held pending authority gaps, or should stop, while preserving all private-output, receipt, and Memory/RAG release boundaries.

rawMemoryReleased=false. This work order does not authorize raw memory release, retrieval, reinjection, private-output reading, memory write, or Memory/RAG route release.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION --title "MSEA R41 T2 MinerU Persistence Mode Authorization Decision" --date 2026-07-06 --base b5c200480 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced placeholders with R41-T2 source-verified mission, no-commit handoff controls, worker output manifest, source verification, ADIF disclosure, and private-only boundaries. |
| checkerReadAheadConfirmation | Read `governance/compat/check_work_order_dispatch_quality.py`, `governance/compat/check_governed_artifact_checker_read_ahead.py`, `governance/compat/check_dispatch_prompt_envelope.py`, `governance/compat/check_dispatch_scaffold_provenance.py`, `governance/compat/check_adif_defect_registry_disclosure.py`, `governance/compat/check_agent_handoff_boundary.py`, and `governance/compat/check_public_export_disposition.py` before authoring. |
| docOnlyNewFields | `persistenceAuthorityActor`, `persistenceAuthorizationConditions`, `persistenceInvariantConditions`, `selectedR41T2Disposition` |
| claimBoundary | Dispatch authoring provenance only; no runtime, provider, live, public-sync, package, Web, MCP, model-router, MinerU execution, persistence invocation, or Memory/RAG release behavior claim. |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly by reading the failing checker source and matching the required literal shape. Worker should return to orchestrator only for a source contradiction, forbidden-scope need, or missing authority that makes completion impossible.

Allowed-scope remediation includes documentation formatting, missing required review headings, source verification table correction, worker-return scaffold repair, gate reruns, and provider-local stray-file removal or disclosure. It does not include source/test edits, runtime execution, provider/live proof, public-sync, secret use, or commit.

## Agent Roles

| Role | Owner |
| --- | --- |
| Orchestrator / dispatcher | dispatcher |
| Implementer | delegated no-commit worker |
| Reviewer | reviewer or delegated reviewer |
| Closer | reviewer/closer after returned artifacts are accepted |
| Operator approval required for | scope expansion, source/test edit, runtime execution, provider/live proof, public-sync, persistence invocation, use-case/legal work, commit, push, or claim-boundary change |

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| Intake source | Operator request plus active session next allowed move from accepted R41-T1 completion review at material commit `51216fb9a` |
| intake summary | Docs-only MinerU persistence-mode authorization decision for `fileBackedPersistenceRequested` authority |
| scope classification | governed authority-decision dispatch; no source/test edit, runtime, provider/live, public-sync, or persistence invocation |
| risk sensitivity | R2 governance/system-chain release authority decision with private-output and memory-release boundaries |
| Route | `SINGLE_AGENT_SINGLE_ROLE` |
| selected role route | `SINGLE_AGENT_SINGLE_ROLE` |
| dispatchRole | dispatcher has authored this packet and paired GC-018 baseline |
| workerRole | delegated worker performs docs-only authority-decision evidence synthesis |
| reviewerRole | reviewer/closer evaluates returned artifacts and owns closure conversion |
| rolePattern | dispatcher to no-commit docs-only worker to reviewer/closer |
| Commit mode | `WORKER_MUST_NOT_COMMIT` |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if worker needs scope expansion, source/test edit, live/provider proof, public-sync, persistence invocation, use-case/legal work, commit, push, or claim-boundary change |

## Authority Chain

| Authority | Evidence |
| --- | --- |
| Operator instruction | User requested creation of the next work order; dependency release is R41-T1 completion review at material commit `51216fb9a`. |
| Active session front door | `CVF_SESSION_MEMORY.md` line 144 names the persistence-mode authorization packet as next allowed move. |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` points to active handoff `AGENT_HANDOFF_V37_2026-07-06.md`. |
| Active handoff | `AGENT_HANDOFF_V37_2026-07-06.md` records the R41-T1 closed mode and the same next move. |
| Accepted prior decision | `docs/reference/CVF_MSEA_R41_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_AUTHORITY_DECISION_MATRIX_2026-07-06.md` selected held disposition pending authority gaps. |
| Accepted completion review | `docs/reviews/CVF_MSEA_R41_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_AUTHORITY_DECISION_COMPLETION_2026-07-06.md` closed R41-T1 bounded and routed to this packet. |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_2026-07-06.md` |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap or source requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| R41-T1 held file-backed persistence release pending explicit authority gaps | Purpose; Mission; Source Verification Block | `selectedR41T2Disposition` in decision matrix | Source verification rows for R41-T1 matrix and route candidate | PASS |
| Name who may set `fileBackedPersistenceRequested` true | Mission; Worker Output Requirements | `persistenceAuthorityActor` | Reviewer checks matrix field and source-backed rationale | PASS |
| Name receipt and invariant conditions for any future true setting | Mission; Acceptance Criteria | `persistenceAuthorizationConditions`; `persistenceInvariantConditions` | Reviewer checks conditions against durable receipt fields and route invariants | PASS |
| Preserve no-runtime/no-private/no-release boundary | Forbidden Scope; Claim Boundary | Worker return claim boundary | Worker-return fast gate and reviewer closure | PASS |

## Mission

Create exactly two worker-owned artifacts:

- `docs/reference/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_MATRIX_2026-07-06.md`
- `docs/reviews/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_WORKER_RETURN_2026-07-06.md`

The decision matrix must select exactly one disposition:

- `R41_T2_PERSISTENCE_MODE_AUTHORIZATION_READY_FOR_NARROW_IMPLEMENTATION_PACKET`
- `R41_T2_PERSISTENCE_MODE_AUTHORIZATION_HELD_PENDING_AUTHORITY_GAPS`
- `R41_T2_PERSISTENCE_MODE_AUTHORIZATION_REJECTED_STOP`

If the selected disposition is ready-for-implementation-packet, the matrix must name the authority actor, the source-backed invariant conditions, and the required future implementation packet boundaries. If the selected disposition is held or stop, the matrix must name the unresolved authority gap and the exact condition that would reopen the lane.

## Allowed Scope

- Read only CVF-governed startup files, the paired GC-018 baseline, this work order, accepted R41-T1 artifacts, and source files named in the Source Verification Block.
- Write only the two worker-owned artifacts named in the Mission.
- Use `rg`, `git status`, `git diff`, `git rev-parse`, source line reads, worker-return scaffold, worker-return fast gate, and pre-implementation autorun gates.
- Repair documentation-only gate failures inside the two worker-owned artifacts.
- Record provider-local or IDE stray files as removed or disclosed if they appear, without staging them.

## Forbidden Scope

- No source/test edit.
- No MinerU runtime execution.
- No private/generated output read.
- No file-backed persistence invocation.
- No production durable-store invocation.
- No production Memory/RAG invocation or release.
- No retrieval, vectorization, RAG indexing, memory write, or reinjection.
- No provider/live proof, API-key use, or quota consumption.
- No public-sync, public catalog update, push, or public claim.
- No use-case/legal workflow.
- No provider-local memory as source authority.
- No worker commit.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001 - Avoid exhaustive directory claims; worker must cite exact files and status evidence only.
- ADIF-0002 - Use only CVF-governed sources for cited evidence; provider-local notes stay out of evidence rows.
- ADIF-0014 - Completeness is bounded to this authority decision and not a broad absorption claim.
- ADIF-0015 - Route mode is no-commit worker dispatch and closure conversion is reviewer-owned.
- ADIF-0020 - Checker read-ahead is mandatory before worker writes outputs.
- ADIF-0021 - Applicability markers are scoped; no external intake or public-sync scope is created.
- ADIF-0007 - Gate-sensitive markers are placed only in control/evidence blocks.
- ADIF-0016 - New reusable defect patterns must be promoted to ADIF before closure.
- ADIF-0017 - Commit steward and split ownership are required before any reviewer commit.
- ADIF-0024 - Worker must provide fresh gates, workspace hygiene, and stray provider-local file disclosure.
- ADIF-0006 - Source Verification symbol cells must contain only symbols.

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 20 --json` |
| Returned defect count | 11 |
| Returned defects | ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0006 |
| Disclosed defectIds | ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0006 |
| Dispatch impact | Worker must perform source verification, no-commit return, fresh gate evidence, and workspace hygiene before handoff. |

## Required First Reads

| Path | Reason |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | Active front door and next allowed move. |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | Compact startup state. |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Canonical active handoff and current mode. |
| `AGENT_HANDOFF_V37_2026-07-06.md` | Active handoff continuity. |
| `docs/reference/guard_orientation/README.md` | Guard orientation for governed work. |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | Literal-format traps. |
| `docs/baselines/CVF_GC018_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_2026-07-06.md` | Paired GC-018 dispatch baseline. |
| `docs/reference/CVF_MSEA_R41_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_AUTHORITY_DECISION_MATRIX_2026-07-06.md` | Accepted prior decision matrix. |
| `docs/reviews/CVF_MSEA_R41_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_AUTHORITY_DECISION_COMPLETION_2026-07-06.md` | Accepted R41-T1 completion review. |
| Runtime source files named in Source Verification Block | Required source facts for this authority decision. |

## Pre-Flight Checks

| Command | Required disposition |
| --- | --- |
| `git rev-parse --short HEAD` | Capture executionBaseHead before writing worker artifacts. |
| `git status --short --untracked-files=all` | Record pending and stray files before work. |
| `python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_WORKER_RETURN_2026-07-06.md --title "MSEA R41 T2 MinerU Persistence Mode Authorization Decision Worker Return"` | Create checker-safe worker-return scaffold. |
| `python governance/compat/run_worker_return_fast_gate.py` | Run once on scaffold and once after final worker edit. |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD` | Required before worker handoff. |

## Write Ownership

| Path | Owner | Disposition |
| --- | --- | --- |
| `docs/reference/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_MATRIX_2026-07-06.md` | worker | Allowed to create only. |
| `docs/reviews/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_WORKER_RETURN_2026-07-06.md` | worker | Allowed to create only. |
| Source, tests, session state, handoff, public-sync, provider-local files | none for worker | Forbidden unless a future packet authorizes. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | `Dispatch Prompt Envelope`; `Role:`; `Canonical packet:`; `Commit mode:`; `executionBaseHead`; `Current-time notes:`; `Do-not-misread notes:`; `Required first actions:`; `Return contract:`; `Scaffold Provenance Block`; `ADIF Defect Registry Disclosure`; `Agent Handoff Contract Control Block`; `Reviewer Closure Conversion`; `Worker Return Packet Shape Contract`; `Work-Order Fulfillment Manifest`; `DEFERRED_PRIVATE_ONLY`; source-not-found disposition spelling |
| gateRunPurpose | Confirmation evidence for dispatch shape, not first discovery. |
| claimBoundary | Read-ahead confirms required literal surfaces for this work order and paired baseline only; it does not prove worker execution, closure, runtime behavior, or public export. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R41-T1 selected disposition held file-backed persistence release pending authority gaps | VALUE_SET | `docs/reference/CVF_MSEA_R41_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_AUTHORITY_DECISION_MATRIX_2026-07-06.md` | line 118 | `R41_T1_FILE_BACKED_PERSISTENCE_RELEASE_HELD_PENDING_AUTHORITY_GAPS` | R41-T1 decision matrix | ACCEPT |
| R41-T1 explicitly routes next move to persistence-mode authorization | VALUE_SET | `docs/reference/CVF_MSEA_R41_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_AUTHORITY_DECISION_MATRIX_2026-07-06.md` | lines 153-154 | `persistence-mode authorization` | R41-T1 decision matrix | ACCEPT |
| Active front door names this packet's central field and next move | VALUE_SET | `CVF_SESSION_MEMORY.md` | line 144 | `fileBackedPersistenceRequested` | active session front door | ACCEPT |
| Route authority contains `fileBackedPersistenceRequested` | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | line 40 | `fileBackedPersistenceRequested` | `MineruSystemChainRouteAuthority` | ACCEPT |
| Persistence mode type is currently restricted to in-process mode | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | line 33 | `MineruSystemChainPersistenceMode` | `MineruSystemChainPersistenceMode` | ACCEPT |
| Route candidate fail-closes file-backed persistence request | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | lines 105-107 | `FAIL_CLOSED_FILE_BACKED_PERSISTENCE_REQUESTED` | `evaluateMineruSystemChainRouteCandidate` | ACCEPT |
| Accepted route result reports in-process persistence mode | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | line 158 | `persistenceMode` | `evaluateMineruSystemChainRouteCandidate` | ACCEPT |
| Internal harness records file-backed persistence not used | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-internal-system-chain-harness.ts` | lines 49, 147 | `fileBackedPersistenceUsed` | MinerU internal system-chain harness result | ACCEPT |
| Internal harness default input keeps file-backed persistence unrequested | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-internal-system-chain-harness.ts` | line 111 | `fileBackedPersistenceRequested` | MinerU internal system-chain harness input | ACCEPT |
| File-backed durable-memory store factory exists | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | line 105 | `createFileBackedDurableMemoryStore` | durable memory store factory | ACCEPT |
| Durable memory receipt preserves summary-only and non-reinjection private-output invariants | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 46-48 | `summaryOnly`; `canReinject`; `rawMemoryReleased` | `DurableMemoryReceipt` | ACCEPT |
| Production Memory/RAG route remains not authorized | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-memory-rag-route-release.ts` | lines 33-34, 64, 231 | `productionRouteAuthorized` | MinerU Memory/RAG route release | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Path existence for R41-T2 baseline | `Test-Path docs/baselines/CVF_GC018_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_2026-07-06.md` returned `False` before authoring. | ACCEPT_NO_COLLISION |
| Path existence for R41-T2 work order | `Test-Path docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_2026-07-06.md` returned `False` before authoring. | ACCEPT_NO_COLLISION |
| Token collision search | `rg -n "MSEA-R41-T2|CVF_MSEA_R41_T2|R41_T2" docs/baselines docs/work_orders docs/reviews docs/reference CVF_SESSION` returned no matches before authoring. | ACCEPT_NO_COLLISION |
| Collision decision | R41-T2 artifact names are new in governed dispatch/review/reference/session surfaces. | ACCEPT |

## External Knowledge Intake Routing

| Field | Disposition |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | no external intake route selected; internal governed source-verification dispatch only |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | dispatcher work order and worker return |
| Disposition | NOT_APPLICABLE_WITH_REASON: this work order uses only CVF-governed repository sources and accepted R41-T1 artifacts. |
| Claim boundary | If worker discovers external knowledge is needed, return `BLOCKED_WITH_REASON`; do not absorb it under this packet. |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher authored packet; worker creates no-commit artifacts; reviewer/closer owns closure conversion |
| phase | dispatch and pending worker execution |
| baseHeadFor(phase) | dispatchBaseHead=b5c200480; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | Worker owns only the matrix and worker return paths named in Mission. |
| traceScope(phase, actor) | Worker return must record repo-local Agent Operation Trace Block with commands, before/after status, diff evidence, and allowed-scope source. |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/committer owns any reviewed material commit. |
| crossBatchIsolation | Dispatch begins from clean worktree at b5c200480; worker must disclose any unrelated or provider-local stray files and leave them unstaged. |
| nextMoveSurfaces | Worker must not edit session state, front door, handoff, roadmap, public catalog, or next-move surfaces; reviewer/closer updates them if closure is accepted. |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_COMPLETION_2026-07-06.md` |
| reviewerOwnedClosurePaths | `docs/reviews/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_COMPLETION_2026-07-06.md`; this work order if status changes; active session surfaces only if reviewer accepts closure. |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Output Checker Read-Ahead Mandate

Before writing each worker-owned output artifact, read checker source for that file's docType, path family, and conditional content class.

| Output artifact | Required read-ahead result |
| --- | --- |
| worker return under `docs/reviews/` | Derive exact review headings, worker-return quality terms, trace labels, delta boundary labels, source inventory action tokens, and no-commit evidence shape before writing. |
| companion reference under `docs/reference/` | Derive exact reference headings such as Scope / Applies To, Target / Source, source verification, trace, and claim-boundary labels before writing. |

Literal-shape reminders: do not list required headings as backticked section strings before the real section; write source-not-found disposition spelling instead of the exact blocked enum in literalTokensReviewed; avoid dependency-release wording unless a dependency-release row cites the accepted artifact path and commit.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/reference/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_MATRIX_2026-07-06.md` | Create as source-verified decision matrix with exactly one selected R41-T2 disposition token and explicit authority actor/conditions or gap rationale. |
| `docs/reviews/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_WORKER_RETURN_2026-07-06.md` | Create from worker-return scaffold, include required review headings and evidence, pass fast gate, and leave uncommitted. |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_WORKER_RETURN_2026-07-06.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Shape-list rule: when listing required worker-output sections, write section names without the section-prefix marker. Reserve actual heading syntax for real sections so structural checkers do not treat this checklist as the artifact section body.

The worker return must include at least these real sections:

- Target
- Scope
- Methodology
- Findings
- Risk / Corrective Action
- External Knowledge Intake Routing
- Epistemic Process Block
- Decision
- Source Inventory
- Agent Operation Trace Block
- Delta Execution Claim Boundary Control Block
- Verification Evidence
- Claim Boundary

## Verification Commands

Worker must run these commands from repo root and record results in the worker return:

```powershell
git rev-parse --short HEAD
python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_WORKER_RETURN_2026-07-06.md --title "MSEA R41 T2 MinerU Persistence Mode Authorization Decision Worker Return"
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git status --short --untracked-files=all
```

The first fast gate should run while the worker return is still a short scaffold. The second fast gate and pre-implementation autorun must run after the last material edit.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | local CLI / PowerShell |
| Session or invocation | MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION dispatch authoring, 2026-07-06 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | `rg`; `Get-Content`; ADIF resolver; dispatch scaffold helper; `apply_patch`; planned dispatch gates |
| Target paths | Paired GC-018 baseline and this work order |
| Allowed scope source | Operator request plus R41-T1 accepted closure next allowed move |
| Before status evidence | `git status --short --untracked-files=all` clean worktree at dispatch base b5c200480 |
| After status evidence | Pending dispatch artifacts before commit; final evidence belongs to dispatcher commit and reviewer closure. |
| Diff evidence | `git diff --name-status` for dispatch range |
| Approval boundary | Docs-only dispatch packet authoring; no worker execution, runtime, public-sync, or source/test edit authorized. |
| Claim boundary | Repo-local trace only; no OS/user attribution, runtime behavior, or provider/live claim. |
| Agent type | dispatcher |
| Invocation ID | `msea_r41_t2_mineru_persistence_mode_authorization_decision-2026-07-06` |
| Expected manifest | Baseline and work order only for dispatch; worker later owns matrix and worker return only. |
| Actual changed set | To be confirmed by dispatcher commit evidence. |
| Manifest delta | To be confirmed by dispatcher commit evidence. |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | Docs-only dispatch for an authority-decision worker packet. |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, or mandatory-wrapper behavior is claimed. |
| receiptEvidence | N/A with reason: no runtime receipt or MinerU execution is authorized. |
| actionEvidence | ACTION_EVIDENCE_PRESENT: dispatch artifacts and gate evidence only. |
| invocationBoundary | Worker may write governed decision artifacts only; no runtime invocation. |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized. |
| claimLanguage | The packet asks for a source-verified decision, not implementation or proof of production behavior. |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router behavior without a fresh source-verified authorization. |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: Current evidence likely supports a held disposition unless the worker can identify a source-backed authority actor and invariant set that safely permits a later narrow implementation packet.

Evidence Comparison Requirement: Worker return must compare actual source evidence against the prediction.

Contradiction Handling Requirement: Contradictory evidence requires a Contradiction Or Gap Disposition and claim-boundary update.

Claim Update Requirement: Worker return records whether the claim was confirmed, revised, narrowed, or invalidated.

## Execution Plan

| Step | Input | Output | Validation or stop condition |
| --- | --- | --- | --- |
| 1 | Required First Reads | Source inventory in worker return | Stop if a required source is missing or contradictory. |
| 2 | Source Verification Block and R41-T1 artifacts | Decision matrix draft | Stop if no source-backed authority or gap rationale can be stated. |
| 3 | Worker-return scaffold | Worker return draft | Run fast gate on scaffold before long prose. |
| 4 | Final matrix and worker return | Gate evidence | Run pre-implementation autorun and final fast gate. |
| 5 | Pending worker-owned artifacts | COMPLETE_PENDING_REVIEW handoff | Record actual `git status --short --untracked-files=all`; do not commit. |

## Evidence Requirements

| Evidence | Required form |
| --- | --- |
| Source verification | Table rows with source file, line/section, symbol-only cell, and disposition. |
| Decision | Exactly one R41-T2 disposition token in the matrix. |
| Worker gate evidence | Exact commands and PASS/BLOCKED/N/A with reason results in worker return. |
| Workspace hygiene | `git status --short --untracked-files=all` after final edit. |
| raw memory invariant | `rawMemoryReleased=false` in worker return and matrix claim boundary. |

## Acceptance Criteria

- Worker creates only the two owned artifacts named in the Mission.
- Decision matrix selects exactly one R41-T2 disposition token.
- If selecting ready-for-implementation-packet, matrix names `persistenceAuthorityActor`, `persistenceAuthorizationConditions`, and `persistenceInvariantConditions`.
- If selecting held or stop, matrix names the unresolved authority gap and a concrete reopen or stop condition.
- Source Verification rows cite existing source files or accepted R41-T1 artifacts and use symbol-only cells.
- Worker return records fresh gate commands, actual pending worktree status, and provider-local stray-file hygiene.
- No source/test edit, runtime execution, private-output read, persistence invocation, Memory/RAG release, live/provider proof, public-sync, commit, push, or public claim occurs.

## Fail Conditions

- Missing or multiple selected R41-T2 disposition tokens.
- Authority actor or invariant conditions are asserted without source-backed evidence.
- A ready-for-implementation-packet disposition attempts to authorize implementation directly.
- Any worker-owned artifact cites provider-local memory as CVF authority.
- Any forbidden scope item is performed or claimed.
- Worker leaves `.qwen/`, IDE, provider-local, or other stray files undisclosed or staged without authorization.
- Required gates are skipped, stale, or recorded before final material edit.

## Review Gate

Worker handoff is not closure. Reviewer/closer must inspect the matrix and worker return, run reviewer-return steward and applicable closure gates, decide whether to accept, repair, or reject, and only then commit reviewed artifacts and update session continuity if accepted.

## Closure Checklist

| Item | Closure disposition |
| --- | --- |
| Worker artifacts reviewed | Reviewer-owned; must be PASS, BLOCKED, or rejected with reason. |
| Reviewer-return steward | Reviewer-owned before material commit. |
| Pre-closure autorun | Reviewer-owned after material commit range is available. |
| Session continuity | Reviewer/closer-owned only if accepted closure changes current mode or next move. |
| Public export | Private-only unless a future public-sync packet authorizes export. |

## Operator Checkpoint

No operator checkpoint is required for worker execution inside Allowed Scope. Operator approval is required before source/test edits, runtime execution, private/generated output reads, persistence invocation, Memory/RAG release, provider/live proof, public-sync, use-case/legal work, worker commit, push, or claim-boundary expansion.

## Claim Boundary

This work order authorizes only a docs-only R41-T2 authority decision worker return. It does not authorize implementation, hook wiring, source/test edits, MinerU execution, private/generated output reads, file-backed persistence invocation, production durable-store invocation, production Memory/RAG invocation or release, retrieval, vectorization, provider/live proof, public-sync, use-case/legal work, worker commit, push, or public claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: This is a private provenance work order. No public-sync artifact is changed or authorized by this packet.
