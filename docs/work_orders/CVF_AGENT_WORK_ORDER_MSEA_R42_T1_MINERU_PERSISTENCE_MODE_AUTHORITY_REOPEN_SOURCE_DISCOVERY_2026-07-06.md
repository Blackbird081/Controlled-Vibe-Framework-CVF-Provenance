# CVF Agent Work Order - MSEA R42 T1 MinerU Persistence Mode Authority Reopen Source Discovery

Memory class: governed-worker-dispatch

Status: CLOSED

Batch ID: MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY

Dispatch base head: 680d3492a

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: reviewer or delegated reviewer

Worker return path: `docs/reviews/CVF_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_WORKER_RETURN_2026-07-06.md`

## Dispatch Prompt Envelope

Role: delegated docs-only source-discovery worker for MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_2026-07-06.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-06; current session state points from accepted R41-T4 completion review `docs/reviews/CVF_MSEA_R41_T4_MINERU_FOUNDATION_CHAIN_STOP_RELEASE_DECISION_COMPLETION_2026-07-06.md` at material commit `41802d2ff` to operator-selected fresh R41-T2 reopen authority packet authoring.

Do-not-misread notes: This packet is not implementation authority, not a runtime harness packet, not a persistence release, not a production Memory/RAG release, and not a use-case/legal workflow packet. Do not edit source/test files, run MinerU, read private/generated output, invoke file-backed persistence, widen persistence mode, release Memory/RAG, run provider/live proof, public-sync, commit, push, or make public claims.

Required first actions: read required startup files, guard orientation, literal gotchas, this packet, the paired GC-018 baseline, accepted R41-T2 and R41-T4 artifacts, source rows in the Source Verification Block, and all checker source listed in the Checker Source Read-Ahead Block before writing any artifact.

Return contract: create the source-discovery decision matrix and worker return artifact, run required gates, leave changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Execute the R42-T1 docs-only source-discovery pass for the R41-T2 persistence
mode authority reopen condition. The worker must determine whether current
governed source already contains any actor/role, second persistence-mode
literal plus runtime check, receipt field, or invariant that can satisfy the
R41-T2 reopen condition, or whether the missing authority remains confirmed.

rawMemoryReleased=false. This work order does not authorize raw memory release,
retrieval, reinjection, private-output reading, memory write, file-backed
persistence invocation, persistence-mode widening, provider/live proof, or
Memory/RAG route release.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY --title "MSEA R42 T1 MinerU Persistence Mode Authority Reopen Source Discovery" --date 2026-07-06 --base 680d3492a --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced placeholders with R42-T1 source-discovery scope, no-commit handoff controls, worker output manifest, dependency-release evidence, source verification, ADIF disclosure, and private-only boundaries. |
| checkerReadAheadConfirmation | Read `governance/compat/check_work_order_dispatch_quality.py`, `governance/compat/check_governed_artifact_checker_read_ahead.py`, `governance/compat/check_dispatch_prompt_envelope.py`, `governance/compat/check_dispatch_scaffold_provenance.py`, `governance/compat/check_adif_defect_registry_disclosure.py`, `governance/compat/check_agent_handoff_boundary.py`, `governance/compat/check_public_export_disposition.py`, `governance/compat/check_delta_execution_claim_boundary.py`, `governance/compat/check_external_knowledge_intake_routing.py`, `governance/compat/check_worker_return_quality_gate.py`, and `governance/compat/check_foundation_storage_layout.py` before authoring. |
| docOnlyNewFields | `selectedR42T1Disposition`, `persistenceAuthoritySourceDiscoveryResult`, `reopenEvidenceClass` |
| claimBoundary | Dispatch authoring provenance only; no runtime, provider, live, public-sync, package, Web, MCP, model-router, MinerU execution, persistence invocation, or Memory/RAG release behavior claim. |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly by reading the
failing checker source and matching the required literal shape. Worker should
return to orchestrator only for a source contradiction, forbidden-scope need,
or missing authority that makes completion impossible.

Allowed-scope remediation includes documentation formatting, missing required
review headings, source verification table correction, worker-return scaffold
repair, gate reruns, static-analysis diagnostic disclosure, and provider-local
or IDE stray-file removal or disclosure. It does not include source/test edits,
runtime execution, provider/live proof, public-sync, secret use, persistence
invocation, or commit.

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
| Intake source | Operator accepted the R42-T1 recommendation after R41-T4 bounded stop closure |
| intake summary | Docs-only source discovery for R41-T2 persistence-mode authority reopen condition |
| scope classification | governed source-discovery dispatch; no source/test edit, runtime, provider/live, public-sync, production release, or persistence invocation |
| risk sensitivity | R2 governance/system-chain release-boundary decision with private-output and memory-release boundaries |
| Route | `SINGLE_AGENT_SINGLE_ROLE` |
| selected role route | `SINGLE_AGENT_SINGLE_ROLE` |
| dispatchRole | dispatcher has authored this packet and paired GC-018 baseline |
| workerRole | delegated worker performs docs-only source discovery and evidence synthesis |
| reviewerRole | reviewer/closer evaluates returned artifacts and owns closure conversion |
| rolePattern | dispatcher to no-commit docs-only worker to reviewer/closer |
| Commit mode | `WORKER_MUST_NOT_COMMIT` |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if worker needs scope expansion, source/test edit, live/provider proof, public-sync, persistence invocation, production release, use-case/legal work, commit, push, or claim-boundary change |

## Authority Chain

| Authority | Evidence |
| --- | --- |
| Operator instruction | User agreed to create work order for the recommended R41-T2 reopen authority source-discovery lane. |
| Active session front door | `CVF_SESSION_MEMORY.md` records R41-T4 closure and operator next-move options. |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` points to active handoff `AGENT_HANDOFF_V37_2026-07-06.md`. |
| Active handoff | `AGENT_HANDOFF_V37_2026-07-06.md` records the R41-T4 closed mode and no-runtime boundary. |
| Accepted R41-T2 decision | `docs/reference/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_MATRIX_2026-07-06.md` selected held disposition pending authority gaps and named the reopen condition. |
| Accepted R41-T4 stop decision | `docs/reviews/CVF_MSEA_R41_T4_MINERU_FOUNDATION_CHAIN_STOP_RELEASE_DECISION_COMPLETION_2026-07-06.md` closed the foundation chain as bounded candidate stop-state. |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_2026-07-06.md` |

## Dependency Release Evidence

| Dependency | Evidence artifact | Commit | Release disposition | T1 consequence |
| --- | --- | --- | --- | --- |
| R41-T2 persistence-mode authorization decision | `docs/reference/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_MATRIX_2026-07-06.md` | `4a08d3ef0` | Held pending authority gaps with a specific reopen condition | Worker must test only whether current source already satisfies one of the three named reopen paths. |
| R41-T4 foundation-chain stop/release decision | `docs/reviews/CVF_MSEA_R41_T4_MINERU_FOUNDATION_CHAIN_STOP_RELEASE_DECISION_COMPLETION_2026-07-06.md` | `41802d2ff` | Foundation chain stopped as bounded candidate | Worker must not treat this source-discovery packet as production release or implementation authority. |
| Active session next move | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `680d3492a` | Operator may author a fresh source-verified R41-T2 reopen authority packet | Operator selected this dispatch; work remains docs-only and no-runtime. |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap or source requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| R41-T2 reopen requires actor/role, second persistence-mode literal/runtime check, or new invariant field | Purpose; Mission; Source Verification Block | `selectedR42T1Disposition` in decision matrix | Worker checks cited source rows and accepted R41-T2 matrix | PASS |
| R41-T4 stopped chain as bounded candidate unless a fresh packet is selected | Dependency Release Evidence; Authority Chain | `persistenceAuthoritySourceDiscoveryResult` | Worker checks R41-T4 completion and matrix | PASS |
| Preserve no-runtime/no-private/no-release boundary | Forbidden Scope; Claim Boundary | Worker return claim boundary | Worker-return fast gate and reviewer closure | PASS |
| Avoid use-case/legal deep dive | Forbidden Scope; Acceptance Criteria | worker return boundary | Reviewer checks claim boundary | PASS |

## Mission

Create exactly two worker-owned artifacts:

- `docs/reference/CVF_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_MATRIX_2026-07-06.md`
- `docs/reviews/CVF_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_WORKER_RETURN_2026-07-06.md`

The decision matrix must select exactly one disposition:

- `R42_T1_PERSISTENCE_AUTHORITY_SOURCE_FOUND_FOR_REOPEN_DESIGN`
- `R42_T1_PERSISTENCE_AUTHORITY_SOURCE_MISSING_CONFIRMED`
- `R42_T1_PERSISTENCE_AUTHORITY_SOURCE_CONTRADICTION_BLOCKED`

The worker must select `R42_T1_PERSISTENCE_AUTHORITY_SOURCE_FOUND_FOR_REOPEN_DESIGN`
only if it can cite accepted, source-verified evidence satisfying at least one
R41-T2 reopen path. The worker must not treat adjacent source existence as
authority unless the source directly binds actor/role, persistence-mode literal,
runtime check, receipt field, or invariant to `fileBackedPersistenceRequested`
or equivalent persistence-mode acceptance.

## Required Artifact Manifest

| Artifact | Required path | Owner | Closure disposition |
| --- | --- | --- | --- |
| Source-discovery decision matrix | `docs/reference/CVF_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_MATRIX_2026-07-06.md` | no-commit worker | reviewer-owned acceptance or rejection |
| Worker return | `docs/reviews/CVF_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_WORKER_RETURN_2026-07-06.md` | no-commit worker | reviewer-owned acceptance or rejection |
| Completion review | `docs/reviews/CVF_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_COMPLETION_2026-07-06.md` | reviewer/closer | reviewer-created only if closure proceeds |

## Allowed Scope

- Read only CVF-governed startup files, the paired GC-018 baseline, this work order, accepted R41 artifacts, and the source files named in the Source Verification Block.
- Write only the two worker-owned artifacts named in the Mission.
- Use `rg`, `git status`, `git diff`, `git rev-parse`, source line reads, worker-return scaffold, worker-return fast gate, and pre-implementation autorun gates.
- Repair documentation-only gate failures inside the two worker-owned artifacts.
- Record static-analysis warnings as fixed inside Allowed Scope or out-of-scope without editing source/test code.
- Remove or disclose `.qwen/`, IDE, provider-local, or other stray files if they appear, without staging them.

## Forbidden Scope

- No source/test edit.
- No MinerU runtime execution.
- No private/generated output read.
- No file-backed persistence invocation.
- No persistence-mode widening.
- No production durable-store invocation.
- No production Memory/RAG invocation or release.
- No retrieval, vectorization, RAG indexing, memory write, or reinjection.
- No provider/live proof, API-key use, or quota consumption.
- No public-sync, public catalog update, push, or public claim.
- No Web/UI/dashboard work.
- No standalone PDF app or hosted release work.
- No use-case/legal workflow.
- No extraction accuracy, document truth, legal quality, or current-law correctness claim.
- No provider-local memory as source authority.
- No worker commit.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001 - Avoid exhaustive directory claims; worker must cite exact files and status evidence only.
- ADIF-0002 - Use only CVF-governed sources for cited evidence; provider-local notes stay out of evidence rows.
- ADIF-0014 - Completeness is bounded to this source-discovery decision and not a broad absorption claim.
- ADIF-0015 - Route mode is no-commit worker dispatch and closure conversion is reviewer-owned.
- ADIF-0020 - Checker read-ahead is mandatory before worker writes outputs.
- ADIF-0021 - Applicability markers are scoped; no external intake or public-sync scope is created.
- ADIF-0007 - Gate-sensitive markers are placed only in control/evidence blocks.
- ADIF-0016 - New reusable defect patterns must be promoted to ADIF before closure.
- ADIF-0017 - Commit steward and split ownership are required before any reviewer commit.
- ADIF-0024 - Worker must provide fresh gates, workspace hygiene, static-analysis diagnostic handling, and provider-local stray-file disclosure.
- ADIF-0006 - Source Verification symbol cells must contain symbols only.

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
| `docs/baselines/CVF_GC018_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_2026-07-06.md` | Paired GC-018 dispatch baseline. |
| `docs/reference/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_MATRIX_2026-07-06.md` | Accepted R41-T2 reopen condition. |
| `docs/reviews/CVF_MSEA_R41_T4_MINERU_FOUNDATION_CHAIN_STOP_RELEASE_DECISION_COMPLETION_2026-07-06.md` | Accepted R41-T4 bounded stop closure. |
| Source files named in Source Verification Block | Required source facts for any source-found or source-missing claim. |

## Pre-Flight Checks

| Command | Required disposition |
| --- | --- |
| `git rev-parse --short HEAD` | Capture executionBaseHead before writing worker artifacts. |
| `git status --short --untracked-files=all` | Record pending and stray files before work. |
| `python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_WORKER_RETURN_2026-07-06.md --title "MSEA R42 T1 MinerU Persistence Mode Authority Reopen Source Discovery Worker Return"` | Create checker-safe worker-return scaffold. |
| `python governance/compat/run_worker_return_fast_gate.py` | Run once on scaffold and once after final worker edit. |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD` | Required before worker handoff. |

## Write Ownership

| Path | Owner | Disposition |
| --- | --- | --- |
| `docs/reference/CVF_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_MATRIX_2026-07-06.md` | worker | Allowed to create only. |
| `docs/reviews/CVF_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_WORKER_RETURN_2026-07-06.md` | worker | Allowed to create only. |
| Source, tests, session state, handoff, public-sync, provider-local files | none for worker | Forbidden unless a future packet authorizes. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_foundation_storage_layout.py` |
| literalTokensReviewed | `Dispatch Prompt Envelope`; `Role:`; `Canonical packet:`; `Commit mode:`; `executionBaseHead`; `Current-time notes:`; `Do-not-misread notes:`; `Required first actions:`; `Return contract:`; `Scaffold Provenance Block`; `ADIF Defect Registry Disclosure`; `Source Verification Block`; `Negative Search And Collision Discipline`; `Required Artifact Manifest`; `Agent Handoff Contract Control Block`; `Reviewer Closure Conversion`; `Worker Return Packet Shape Contract`; `DEFERRED_PRIVATE_ONLY`; source-not-found disposition spelling |
| gateRunPurpose | Confirmation evidence for dispatch shape, not first discovery. |
| claimBoundary | Read-ahead confirms required literal surfaces for this work order and paired baseline only; it does not prove worker execution, closure, runtime behavior, or public export. |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R41-T2 selected persistence-mode authorization held pending authority gaps | VALUE_SET | `docs/reference/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_MATRIX_2026-07-06.md` | line 131 | `R41_T2_PERSISTENCE_MODE_AUTHORIZATION_HELD_PENDING_AUTHORITY_GAPS` | R41-T2 decision matrix | ACCEPT |
| R41-T2 reopen condition names actor/role, second persistence-mode literal/runtime check, or new invariant field as reopen paths | VALUE_SET | `docs/reference/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_MATRIX_2026-07-06.md` | Reopen Condition section | `Reopen Condition` | R41-T2 decision matrix | ACCEPT |
| R41-T4 selected bounded-candidate stop and preserved R41-T2 reopen condition as future option | VALUE_SET | `docs/reference/CVF_MSEA_R41_T4_MINERU_FOUNDATION_CHAIN_STOP_RELEASE_DECISION_MATRIX_2026-07-06.md` | lines 106 and 122-126 | `R41_T4_FOUNDATION_CHAIN_STOP_BOUNDED_CANDIDATE` | R41-T4 decision matrix | ACCEPT |
| R41-T4 completion review accepted the bounded-candidate stop without authorizing implementation | VALUE_SET | `docs/reviews/CVF_MSEA_R41_T4_MINERU_FOUNDATION_CHAIN_STOP_RELEASE_DECISION_COMPLETION_2026-07-06.md` | Reviewer Decision section | `R41_T4_STOP_RELEASE_DECISION_COMPLETE_BOUNDED_CANDIDATE` | R41-T4 completion review | ACCEPT |
| Persistence-mode type is currently a single literal | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | line 33 | `MineruSystemChainPersistenceMode` | MinerU system-chain route candidate | ACCEPT |
| Route authority includes `fileBackedPersistenceRequested` as the field named by R41-T2 | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | line 40 | `fileBackedPersistenceRequested` | MinerU system-chain route candidate | ACCEPT |
| Route candidate fail-closes when file-backed persistence is requested | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | lines 105-107 | `FAIL_CLOSED_FILE_BACKED_PERSISTENCE_REQUESTED` | MinerU system-chain route candidate | ACCEPT |
| Memory-owner authorization has actor role fields in the adjacent route-release helper | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-memory-rag-route-release.ts` | lines 40-45 | `MineruMemoryOwnerAuthorization` | MinerU Memory/RAG route release candidate | ACCEPT |
| Durable-memory receipt already carries private-output invariants | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 35 and 46-48 | `DurableMemoryReceipt` | durable memory store | ACCEPT |
| Active session next move permits a fresh source-verified R41-T2 reopen authority packet | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `nextAllowedMove` | `nextAllowedMove` | active session bootstrap read model | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Path existence for R42-T1 baseline | `Test-Path docs/baselines/CVF_GC018_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_2026-07-06.md` returned `False` before authoring. | ACCEPT_NO_COLLISION |
| Path existence for R42-T1 work order | `Test-Path docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_2026-07-06.md` returned `False` before authoring. | ACCEPT_NO_COLLISION |
| Path existence for R42-T1 worker outputs | `Test-Path` for the planned matrix, worker return, and completion-review paths returned `False` before authoring. | ACCEPT_NO_COLLISION |
| Token collision search | `rg -n "MSEA-R42-T1|MSEA_R42_T1|R42_T1|CVF_MSEA_R42_T1" docs/baselines docs/work_orders docs/reviews docs/reference CVF_SESSION AGENT_HANDOFF_V37_2026-07-06.md CVF_SESSION_MEMORY.md` returned no matches before authoring. | ACCEPT_NO_ARTIFACT_COLLISION |
| Collision decision | R42-T1 artifact names are new in governed dispatch/review/reference artifact surfaces. | ACCEPT |

## External Knowledge Intake Routing

| Field | Disposition |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | no external intake route selected; internal governed source-verification dispatch only |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | dispatcher work order and worker return |
| Disposition | NOT_APPLICABLE_WITH_REASON: this work order uses only CVF-governed repository sources and accepted R41 artifacts. |
| Claim boundary | If worker discovers external knowledge is needed, return `BLOCKED_WITH_REASON`; do not absorb it under this packet. |

## Foundation Storage Layout Block

| Field | Disposition |
| --- | --- |
| Standard | `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` |
| Applicability | N/A with reason: this work order does not create, split, relocate, refactor, or index durable governance foundation files. |
| Reference-family folder effect | N/A with reason: the worker may create one dated companion reference artifact under the existing reference root only; no stable reference family folder or README front door is created. |
| Storage layout action | N/A with reason: no folder movement, stable-path policy change, date-policy change, index update, or storage layout decision is authorized. |
| Claim boundary | This block prevents source-discovery work from being misread as durable governance storage-layout mutation. |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher authored packet; worker creates no-commit artifacts; reviewer/closer owns closure conversion |
| phase | dispatch and pending worker execution |
| baseHeadFor(phase) | dispatchBaseHead=680d3492a; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | Worker owns only the matrix and worker return paths named in Mission. |
| traceScope(phase, actor) | Worker return must record repo-local Agent Operation Trace Block with commands, before/after status, diff evidence, and allowed-scope source. |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/committer owns any reviewed material commit. |
| crossBatchIsolation | Dispatch begins from clean worktree at 680d3492a; worker must disclose any unrelated or provider-local stray files and leave them unstaged. |
| nextMoveSurfaces | Worker must not edit session state, front door, handoff, roadmap, public catalog, or next-move surfaces; reviewer/closer updates them if closure is accepted. |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_COMPLETION_2026-07-06.md` |
| reviewerOwnedClosurePaths | `docs/reviews/CVF_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_COMPLETION_2026-07-06.md`; this work order if status changes; active session surfaces only if reviewer accepts closure. |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Output Checker Read-Ahead Mandate

Before writing each worker-owned output artifact, read checker source for that
file's docType, path family, and conditional content class.

| Output artifact | Required read-ahead result |
| --- | --- |
| worker return under `docs/reviews/` | Derive exact review headings, worker-return quality terms, trace labels, delta boundary labels, source inventory action tokens, and no-commit evidence shape before writing. |
| companion reference under `docs/reference/` | Derive exact reference headings such as Scope / Applies To, Target / Source, source verification, trace, and claim-boundary labels before writing. |

Literal-shape reminders: do not list required headings as backticked section
strings before the real section; write source-not-found disposition spelling
instead of the exact blocked enum in literalTokensReviewed; avoid
dependency-release wording unless a dependency-release row cites the accepted
artifact path and commit.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/reference/CVF_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_MATRIX_2026-07-06.md` | Create as source-verified source-discovery decision matrix with exactly one selected R42-T1 disposition token and explicit source-found, source-missing, or contradiction-blocked rationale. |
| `docs/reviews/CVF_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_WORKER_RETURN_2026-07-06.md` | Create from worker-return scaffold, include required review headings and evidence, pass fast gate, and leave uncommitted. |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_WORKER_RETURN_2026-07-06.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Shape-list rule: when listing required worker-output sections, write section
names without the section-prefix marker. Reserve actual heading syntax for real
sections so structural checkers do not treat this checklist as the artifact
section body.

The worker return must include at least these real sections:

- Purpose
- Target
- Target / Source
- Scope
- Scope / Methodology
- Methodology
- Findings
- Findings / Position
- Risk / Corrective Action
- External Knowledge Intake Routing
- Epistemic Process Block
- Decision
- Source Inventory
- Public Export Disposition
- Rescan Intelligence Hardening
- Corpus Completeness And Report Integrity
- Finding-To-Governance Learning Disposition
- Agent Operation Trace Block
- Delta Execution Claim Boundary Control Block
- Machine Closure Package
- Command Evidence
- Claim Boundary

The worker return must also record `executionBaseHead`, `git status --short`,
and N/A with reason dispositions for conditional sections that do not apply.

## Verification Commands

Worker must run these commands from repo root and record results in the worker return:

```powershell
git rev-parse --short HEAD
python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_WORKER_RETURN_2026-07-06.md --title "MSEA R42 T1 MinerU Persistence Mode Authority Reopen Source Discovery Worker Return"
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git status --short --untracked-files=all
```

The first fast gate should run while the worker return is still a short
scaffold. The second fast gate and pre-implementation autorun must run after
the last material edit.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | local CLI / PowerShell |
| Session or invocation | MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY dispatch authoring, 2026-07-06 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | `rg`; `Get-Content`; ADIF resolver; dispatch scaffold helper; `apply_patch`; planned dispatch gates |
| Target paths | Paired GC-018 baseline and this work order |
| Allowed scope source | Operator continuation request plus R41-T4 accepted closure next allowed move |
| Before status evidence | clean worktree at dispatch base 680d3492a; `git status --short --untracked-files=all` showed no changed paths |
| After status evidence | Pending dispatch artifacts before commit; final evidence belongs to dispatcher commit and reviewer closure. |
| Diff evidence | `git diff --name-status` for dispatch range |
| Approval boundary | Docs-only dispatch packet authoring; no worker execution, runtime, public-sync, or source/test edit authorized. |
| Claim boundary | Repo-local trace only; no OS/user attribution, runtime behavior, or provider/live claim. |
| Agent type | dispatcher |
| Invocation ID | `msea-r42-t1-persistence-mode-authority-reopen-source-discovery-dispatch-2026-07-06` |
| Expected manifest | paired GC-018 baseline and this work order |
| Actual changed set | paired GC-018 baseline and this work order before commit |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename occurred |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | docs-only R42-T1 persistence-mode authority reopen source-discovery dispatch |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, persistence invocation, production release, or runtime harness behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt or MinerU execution is authorized |
| actionEvidence | ACTION_EVIDENCE_PRESENT: dispatch artifacts and gate evidence only |
| invocationBoundary | Worker may write governed decision artifacts only; no runtime invocation |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized |
| claimLanguage | The packet asks for source discovery, not implementation or proof of production behavior |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router behavior without a fresh source-verified authorization |

## Execution Plan

| Step | Input | Output | Validation or stop condition |
| --- | --- | --- | --- |
| 1 | Required First Reads | Source inventory in worker return | Stop if a required source is missing or contradictory. |
| 2 | Accepted R41-T2 and R41-T4 artifacts plus source files | Decision matrix draft | Stop if evidence cannot support exactly one R42-T1 disposition. |
| 3 | Worker-return scaffold | Worker return draft | Run fast gate on scaffold before long prose. |
| 4 | Final matrix and worker return | Gate evidence | Run pre-implementation autorun and final fast gate. |
| 5 | Pending worker-owned artifacts | COMPLETE_PENDING_REVIEW handoff | Record actual `git status --short --untracked-files=all`; do not commit. |

## Evidence Requirements

| Evidence | Required form |
| --- | --- |
| Source verification | Table rows with source file, line/section, symbol-only cell, and disposition. |
| Decision | Exactly one R42-T1 disposition token in the matrix. |
| Source-found evidence | Exact source path, line/section, symbol, and explanation of how it satisfies a named R41-T2 reopen path. |
| Source-missing evidence | Exact searched source surfaces and a concrete remaining missing element. |
| Worker gate evidence | Exact commands and PASS/BLOCKED/N/A with reason results in worker return. |
| Workspace hygiene | `git status --short --untracked-files=all` after final edit. |
| Static-analysis hygiene | Any IDE/Pylance or equivalent diagnostic affecting worker-owned files is fixed if inside Allowed Scope or recorded as out-of-scope without source/test edit. |
| Provider-local hygiene | `.qwen/`, IDE, provider-local, or other stray files are removed, disclosed, or left unstaged with reason; worker must not create or leave provider-local files casually. |
| raw memory invariant | `rawMemoryReleased=false` in worker return and matrix claim boundary. |

## Acceptance Criteria

- Worker creates only the two owned artifacts named in the Mission.
- Decision matrix selects exactly one R42-T1 disposition token.
- If selecting source-found, matrix names the exact R41-T2 reopen path satisfied and cites direct source evidence.
- If selecting source-missing, matrix names each unresolved missing element and explains why no implementation packet is released.
- If selecting contradiction-blocked, matrix names the contradictory source rows and return-to-orchestrator action.
- Source Verification rows cite existing source files or accepted R41 artifacts and use symbol-only cells.
- Worker return records fresh gate commands, actual pending worktree status, static-analysis diagnostic handling, and provider-local stray-file hygiene.
- No source/test edit, runtime execution, private-output read, persistence invocation, Memory/RAG release, live/provider proof, public-sync, commit, push, or public claim occurs.

## Fail Conditions

- Missing or multiple selected R42-T1 disposition tokens.
- Source-found is selected without direct source-backed evidence satisfying a named R41-T2 reopen path.
- Any disposition attempts to authorize implementation directly.
- Any worker-owned artifact cites provider-local memory as CVF authority.
- Any forbidden scope item is performed or claimed.
- Worker leaves `.qwen/`, IDE, provider-local, or other stray files undisclosed or staged without authorization.
- Required gates are skipped, stale, or recorded before final material edit.

## Review Gate

Worker handoff is not closure. Reviewer/closer must inspect the matrix and
worker return, run reviewer-return steward and applicable closure gates, decide
whether to accept, repair, or reject, and only then commit reviewed artifacts
and update session continuity if accepted.

## Closure Checklist

| Item | Closure disposition |
| --- | --- |
| Worker artifacts reviewed | Reviewer-owned; must be PASS, BLOCKED, or rejected with reason. |
| Reviewer-return steward | Reviewer-owned before material commit. |
| Pre-closure autorun | Reviewer-owned after material commit range is available. |
| Session continuity | Reviewer/closer-owned only if accepted closure changes current mode or next move. |
| Public export | Private-only unless a future public-sync packet authorizes export. |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this work order | `Status: CLOSED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_COMPLETION_2026-07-06.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker return | `docs/reviews/CVF_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_WORKER_RETURN_2026-07-06.md` | `Status: COMPLETE_PENDING_REVIEW`; accepted by completion review | PASS |
| Companion decision matrix | `docs/reference/CVF_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_MATRIX_2026-07-06.md` | selected `R42_T1_PERSISTENCE_AUTHORITY_SOURCE_MISSING_CONFIRMED` | PASS |
| Roadmap state | N/A | N/A with reason: R42-T1 is a standalone operator-selected source-discovery packet, not a roadmap-derived closure | N/A with reason |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | `python governance/compat/generate_corpus_scan_registry.py --check` PASS during worker-return fast gate | PASS |
| Registry Markdown | changed corpus registry coverage | reviewer-fast changed corpus registry coverage PASS | PASS |
| External evidence digest | N/A | N/A with reason: no external evidence artifact, public-web source, or local external file was absorbed | N/A with reason |
| System loop interlock | R42-T1 decision matrix and completion review | source-missing confirmed; no implementation or production release | PASS |
| Session continuity | session state, session memory, and active handoff | dedicated session-sync commit required after material commit | PASS |
| Runtime boundary | completion review and worker return | no source/test/runtime/private/provider/public execution | PASS |
| Public disposition | this work order and completion review | `DEFERRED_PRIVATE_ONLY` | PASS |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
| --- | --- | --- |
| No runtime receipt is accepted by this closure | R42-T1 remains docs-only and accepts no MinerU runtime, harness execution, file-backed persistence, provider/live, memory-write, public-sync, or production route receipt | PASS |
| Worker return accepted only after reviewer closure | R42-T1 completion review records `CLOSED_PASS_BOUNDED` | PASS |
| Gate evidence is closure evidence only | Worker-return fast gate, pre-implementation autorun, and corpus scan registry checks are recorded as governance evidence, not runtime release evidence | PASS |

## Operator Checkpoint

No operator checkpoint is required for worker execution inside Allowed Scope.
Operator approval is required before source/test edits, runtime execution,
private/generated output reads, persistence invocation, Memory/RAG release,
provider/live proof, public-sync, use-case/legal work, worker commit, push, or
claim-boundary expansion.

## Claim Boundary

This work order authorizes only a docs-only R42-T1 source-discovery worker
return. It does not authorize implementation, hook wiring, source/test edits,
MinerU execution, private/generated output reads, file-backed persistence
invocation, persistence-mode widening, production durable-store invocation,
production Memory/RAG invocation or release, retrieval, vectorization,
provider/live proof, public-sync, Web/UI/dashboard work, standalone app work,
use-case/legal work, worker commit, push, or public claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: This is a private provenance work order. No public-sync artifact is
changed or authorized by this packet.
