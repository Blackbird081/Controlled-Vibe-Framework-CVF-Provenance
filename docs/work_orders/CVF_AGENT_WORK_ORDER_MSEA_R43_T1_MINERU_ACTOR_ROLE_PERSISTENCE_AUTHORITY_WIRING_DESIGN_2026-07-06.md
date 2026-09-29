# CVF Agent Work Order - MSEA R43 T1 MinerU Actor Role Persistence Authority Wiring Design

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN

Dispatch base head: 6a36aaa2e

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: reviewer or delegated reviewer

Worker return path: `docs/reviews/CVF_MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN_WORKER_RETURN_2026-07-06.md`

## Dispatch Prompt Envelope

Role: delegated docs-only design worker for MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN_2026-07-06.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-06; current session state points from accepted R42-T1 completion review `docs/reviews/CVF_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_COMPLETION_2026-07-06.md` at material commit `f88ecfaca` to operator-selected fresh actor-role wiring design packet authoring.

Do-not-misread notes: This packet is not implementation authority, not a runtime harness packet, not a persistence release, not a production Memory/RAG release, and not a use-case/legal workflow packet. Do not edit source/test files, run MinerU, read private/generated output, invoke file-backed persistence, widen persistence mode, release Memory/RAG, run provider/live proof, public-sync, commit, push, edit provider-local or IDE config, or make public claims.

Required first actions: read required startup files, guard orientation, literal gotchas, this packet, the paired GC-018 baseline, accepted R41-T2 and R42-T1 artifacts, source rows in the Source Verification Block, and all checker source listed in the Checker Source Read-Ahead Block before writing any artifact.

Return contract: create the actor-role wiring design matrix and worker return artifact, run required gates, leave changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Execute the R43-T1 docs-only design pass for wiring actor-role authority into
the MinerU `fileBackedPersistenceRequested` decision path. The worker must
propose and source-verify a narrow design that can satisfy the R41-T2 reopen
condition without claiming implementation, runtime behavior, or production
release.

rawMemoryReleased=false. This work order does not authorize raw memory release,
retrieval, reinjection, private-output reading, memory write, file-backed
persistence invocation, persistence-mode widening, provider/live proof, source
or test edits, or Memory/RAG route release.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN --title "MSEA R43 T1 MinerU Actor Role Persistence Authority Wiring Design" --date 2026-07-06 --base 6a36aaa2e --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced placeholders with R43-T1 actor-role wiring design scope, no-commit handoff controls, worker output manifest, dependency-release evidence, source verification, ADIF disclosure, and private-only boundaries. |
| checkerReadAheadConfirmation | Read `governance/compat/check_work_order_dispatch_quality.py`, `governance/compat/check_governed_artifact_checker_read_ahead.py`, `governance/compat/check_dispatch_prompt_envelope.py`, `governance/compat/check_dispatch_scaffold_provenance.py`, `governance/compat/check_adif_defect_registry_disclosure.py`, `governance/compat/check_agent_handoff_boundary.py`, `governance/compat/check_public_export_disposition.py`, `governance/compat/check_delta_execution_claim_boundary.py`, `governance/compat/check_external_knowledge_intake_routing.py`, `governance/compat/check_worker_return_quality_gate.py`, and `governance/compat/check_foundation_storage_layout.py` before authoring. |
| docOnlyNewFields | `selectedR43T1Disposition`, `actorRoleWiringDesignDisposition`, `implementationPacketReadiness` |
| claimBoundary | Dispatch authoring provenance only; no runtime, provider, live, public-sync, package, Web, MCP, model-router, MinerU execution, persistence invocation, source/test edit, or Memory/RAG release behavior claim. |

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
invocation, provider-local or IDE config edits, or commit.

## Agent Roles

| Role | Owner |
| --- | --- |
| Orchestrator / dispatcher | dispatcher |
| Implementer | delegated no-commit docs-only design worker |
| Reviewer | reviewer or delegated reviewer |
| Closer | reviewer/closer after returned artifacts are accepted |
| Operator approval required for | scope expansion, source/test edit, runtime execution, provider/live proof, public-sync, persistence invocation, use-case/legal work, commit, push, or claim-boundary change |

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| Intake source | Operator selected a fresh design packet after R42-T1 confirmed missing source authority. |
| intake summary | Docs-only actor-role authority wiring design for `fileBackedPersistenceRequested`. |
| scope classification | governed design dispatch; no source/test edit, runtime, provider/live, public-sync, production release, or persistence invocation |
| risk sensitivity | R2 governance/system-chain release-boundary decision with private-output and memory-release boundaries |
| Route | `SINGLE_AGENT_SINGLE_ROLE` |
| selected role route | `SINGLE_AGENT_SINGLE_ROLE` |
| dispatchRole | dispatcher has authored this packet and paired GC-018 baseline |
| workerRole | delegated worker performs docs-only design analysis and evidence synthesis |
| reviewerRole | reviewer/closer evaluates returned artifacts and owns closure conversion |
| rolePattern | dispatcher to no-commit docs-only worker to reviewer/closer |
| Commit mode | `WORKER_MUST_NOT_COMMIT` |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if worker needs scope expansion, source/test edit, live/provider proof, public-sync, persistence invocation, production release, use-case/legal work, commit, push, or claim-boundary change |

## Authority Chain

| Authority | Evidence |
| --- | --- |
| Operator instruction | User asked for a fresh design packet to wire actor-role authority into `fileBackedPersistenceRequested` and requested work-order authoring. |
| Active session front door | `CVF_SESSION_MEMORY.md` records the R42-T1 missing-authority closure and fresh design-packet next move. |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` points to active handoff `AGENT_HANDOFF_V37_2026-07-06.md`. |
| Active handoff | `AGENT_HANDOFF_V37_2026-07-06.md` records the R42-T1 closed mode and no-runtime boundary. |
| Accepted R41-T2 decision | `docs/reference/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_MATRIX_2026-07-06.md` selected held disposition pending authority gaps and named the reopen condition. |
| Accepted R42-T1 source discovery | `docs/reviews/CVF_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_COMPLETION_2026-07-06.md` confirmed missing source authority and pointed to a design packet as next allowed move. |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN_2026-07-06.md` |

## Dependency Release Evidence

| Dependency | Evidence artifact | Commit | Release disposition | T1 consequence |
| --- | --- | --- | --- | --- |
| R41-T2 persistence-mode authorization decision | `docs/reference/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_MATRIX_2026-07-06.md` | `4a08d3ef0` | Held pending authority gaps with a specific reopen condition | Worker must design how actor-role authority would satisfy the missing path, not claim existing release. |
| R42-T1 source discovery | `docs/reviews/CVF_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_COMPLETION_2026-07-06.md` | `f88ecfaca` | Missing source authority confirmed | Worker must treat the lane as design-only and avoid implementation. |
| Active session next move | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `6a36aaa2e` | Operator may author a fresh actor-role wiring design packet | Operator selected this dispatch; work remains docs-only and no-runtime. |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap or source requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| R41-T2 reopen requires actor/role, second persistence-mode literal/runtime check, or new invariant field | Purpose; Mission; Source Verification Block | `selectedR43T1Disposition` in design matrix | Worker checks cited source rows and accepted R41/R42 artifacts | PASS |
| R42-T1 confirmed nearest actor-role controls are not wired into `fileBackedPersistenceRequested` | Dependency Release Evidence; Authority Chain | `actorRoleWiringDesignDisposition` | Worker checks R42-T1 matrix and completion review | PASS |
| Preserve no-runtime/no-private/no-release boundary | Forbidden Scope; Claim Boundary | Worker return claim boundary | Worker-return fast gate and reviewer closure | PASS |
| Avoid use-case/legal deep dive | Forbidden Scope; Acceptance Criteria | worker return boundary | Reviewer checks claim boundary | PASS |

## Mission

Create exactly two worker-owned artifacts:

- `docs/reference/CVF_MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN_MATRIX_2026-07-06.md`
- `docs/reviews/CVF_MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN_WORKER_RETURN_2026-07-06.md`

The design matrix must select exactly one disposition:

- `R43_T1_ACTOR_ROLE_WIRING_DESIGN_READY_FOR_IMPLEMENTATION_PACKET`
- `R43_T1_ACTOR_ROLE_WIRING_DESIGN_HELD_PENDING_MISSING_AUTHORITY`
- `R43_T1_ACTOR_ROLE_WIRING_DESIGN_CONTRADICTION_BLOCKED`

The worker must select `R43_T1_ACTOR_ROLE_WIRING_DESIGN_READY_FOR_IMPLEMENTATION_PACKET`
only if it can describe a narrow, source-verified design that can be
implemented later without changing this packet's forbidden scope. The worker
must not treat the existing `RuntimeMemoryActorRole` type cast in the durable
store invocation helper as route-decision authority unless the design explicitly
adds a future implementation step to connect actor-role authority to
`fileBackedPersistenceRequested`.

## Required Artifact Manifest

| Artifact | Required path | Owner | Closure disposition |
| --- | --- | --- | --- |
| Actor-role wiring design matrix | `docs/reference/CVF_MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN_MATRIX_2026-07-06.md` | no-commit worker | reviewer-owned acceptance or rejection |
| Worker return | `docs/reviews/CVF_MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN_WORKER_RETURN_2026-07-06.md` | no-commit worker | reviewer-owned acceptance or rejection |
| Completion review | `docs/reviews/CVF_MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN_COMPLETION_2026-07-06.md` | reviewer/closer | reviewer-created only if closure proceeds and worker return cannot carry acceptance safely |

## Allowed Scope

- Read only CVF-governed startup files, the paired GC-018 baseline, this work order, accepted R41/R42 artifacts, and the source files named in the Source Verification Block.
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
- No provider-local or IDE config edits.
- No worker commit.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001 - Avoid exhaustive directory claims; worker must cite exact files and status evidence only.
- ADIF-0002 - Use only CVF-governed sources for cited evidence; provider-local notes stay out of evidence rows.
- ADIF-0014 - Completeness is bounded to this design decision and not a broad absorption claim.
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
| Dispatch impact | Worker must perform source verification, no-commit return, fresh gate evidence, static-analysis diagnostic handling, and workspace hygiene before handoff. |

## Required First Reads

| Path | Reason |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | Active front door and next allowed move. |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | Compact startup state. |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Canonical active handoff and current mode. |
| `AGENT_HANDOFF_V37_2026-07-06.md` | Active handoff continuity. |
| `docs/reference/guard_orientation/README.md` | Guard orientation for governed work. |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | Literal-format traps. |
| `docs/baselines/CVF_GC018_MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN_2026-07-06.md` | Paired GC-018 dispatch baseline. |
| `docs/reference/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_MATRIX_2026-07-06.md` | Accepted R41-T2 reopen condition. |
| `docs/reference/CVF_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_MATRIX_2026-07-06.md` | Accepted R42-T1 missing-authority evidence. |
| `docs/reviews/CVF_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_COMPLETION_2026-07-06.md` | Accepted R42-T1 closure and next-move boundary. |
| Source files named in Source Verification Block | Required source facts for any design-ready or held claim. |

## Pre-Flight Checks

| Command | Required disposition |
| --- | --- |
| `git rev-parse --short HEAD` | Capture executionBaseHead before writing worker artifacts. |
| `git status --short --untracked-files=all` | Record pending and stray files before work. |
| `python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN_WORKER_RETURN_2026-07-06.md --title "MSEA R43 T1 MinerU Actor Role Persistence Authority Wiring Design Worker Return"` | Create checker-safe worker-return scaffold. |
| `python governance/compat/run_worker_return_fast_gate.py` | Run once on scaffold and once after final worker edit. |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD` | Required before worker handoff. |

## Write Ownership

| Path | Owner | Disposition |
| --- | --- | --- |
| `docs/reference/CVF_MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN_MATRIX_2026-07-06.md` | worker | Allowed to create only. |
| `docs/reviews/CVF_MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN_WORKER_RETURN_2026-07-06.md` | worker | Allowed to create only. |
| Source, tests, session state, handoff, public-sync, provider-local files | none for worker | Forbidden unless a future packet authorizes. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_foundation_storage_layout.py` |
| literalTokensReviewed | `Dispatch Prompt Envelope`; `Role:`; `Canonical packet:`; `Commit mode:`; `executionBaseHead`; `Current-time notes:`; `Do-not-misread notes:`; `Required first actions:`; `Return contract:`; `Scaffold Provenance Block`; `ADIF Defect Registry Disclosure`; `Source Verification Block`; `Negative Search And Collision Discipline`; `Required Artifact Manifest`; `Agent Handoff Contract Control Block`; `Reviewer Closure Conversion`; `Worker Return Packet Shape Contract`; `DEFERRED_PRIVATE_ONLY`; source-not-found disposition spelling |
| gateRunPurpose | Confirmation evidence for dispatch shape, not first discovery. |
| claimBoundary | Read-ahead confirms required literal surfaces for this work order and paired baseline only; it does not prove worker execution, closure, runtime behavior, implementation readiness, or public export. |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R42-T1 accepted missing source authority for the R41-T2 reopen condition | VALUE_SET | `docs/reviews/CVF_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_COMPLETION_2026-07-06.md` | lines 64-82 | `R42_T1_PERSISTENCE_AUTHORITY_SOURCE_MISSING_CONFIRMED` | R42-T1 completion review | ACCEPT |
| R42-T1 matrix says the nearest actor-role controls are real but not connected to `fileBackedPersistenceRequested` | VALUE_SET | `docs/reference/CVF_MSEA_R42_T1_MINERU_PERSISTENCE_MODE_AUTHORITY_REOPEN_SOURCE_DISCOVERY_MATRIX_2026-07-06.md` | lines 141-152 | `R42_T1_PERSISTENCE_AUTHORITY_SOURCE_MISSING_CONFIRMED` | R42-T1 decision matrix | ACCEPT |
| R41-T2 reopen condition requires actor/role, second persistence-mode literal/runtime check, or a new invariant field before accepting file-backed persistence | VALUE_SET | `docs/reference/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_MATRIX_2026-07-06.md` | lines 137-156 | `Reopen Condition` | R41-T2 decision matrix | ACCEPT |
| Route authority currently carries `fileBackedPersistenceRequested` as a plain boolean field | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | lines 36-44 | `MineruSystemChainRouteAuthority` | MinerU system-chain route candidate | ACCEPT |
| Route candidate currently fail-closes any true file-backed persistence request | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | lines 105-107 | `FAIL_CLOSED_FILE_BACKED_PERSISTENCE_REQUESTED` | MinerU system-chain route candidate | ACCEPT |
| Runtime memory hierarchy defines actor roles and an actor-role decision function | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts` | lines 12 and 245 | `RuntimeMemoryActorRole`; `evaluateRuntimeMemoryAction` | runtime memory hierarchy | ACCEPT |
| Runtime memory action denies durable persistence when the tier does not authorize it and denies actors outside the allowlist | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts` | lines 253-255 and 273-275 | `evaluateRuntimeMemoryAction` | runtime memory hierarchy | ACCEPT |
| Durable-store invocation helper imports `RuntimeMemoryActorRole`, casts `actorRole`, and calls the supplied store, but does not decide the system-chain file-backed request | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-durable-store-invocation.ts` | lines 18 and 371-383 | `invokeMineruDurableStoreWrite` | MinerU durable-store invocation helper | ACCEPT |
| Durable memory store exposes a file-backed store factory that is not selected by the system-chain route candidate | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | line 105 | `createFileBackedDurableMemoryStore` | durable memory store | ACCEPT |
| Active session next move permits this fresh actor-role wiring design packet | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `nextAllowedMove` | `nextAllowedMove` | active session bootstrap read model | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Path existence for R43-T1 baseline | `Test-Path docs/baselines/CVF_GC018_MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN_2026-07-06.md` returned `False` before authoring. | ACCEPT_NO_COLLISION |
| Path existence for R43-T1 work order | `Test-Path docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN_2026-07-06.md` returned `False` before authoring. | ACCEPT_NO_COLLISION |
| Token collision search | `rg -n "MSEA-R43-T1|MSEA_R43_T1|R43_T1|CVF_MSEA_R43_T1" docs/baselines docs/work_orders docs/reviews docs/reference CVF_SESSION AGENT_HANDOFF_V37_2026-07-06.md CVF_SESSION_MEMORY.md` returned no matches before authoring. | ACCEPT_NO_ARTIFACT_COLLISION |
| Collision decision | R43-T1 artifact names are new in governed dispatch, review, and reference artifact surfaces. | ACCEPT |

## External Knowledge Intake Routing

| Field | Disposition |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | no external intake route selected; internal governed source-verification dispatch only |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | dispatcher baseline and paired work order |
| Disposition | NOT_APPLICABLE_WITH_REASON: this work order uses only CVF-governed repository sources and accepted R41/R42 artifacts. |
| Claim boundary | If worker discovers external knowledge is needed, return `BLOCKED_WITH_REASON`; do not absorb it under this packet. |

## Foundation Storage Layout Block

| Field | Disposition |
| --- | --- |
| Standard | `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` |
| Applicability | N/A with reason: this work does not create, split, relocate, refactor, or index durable governance foundation files. |
| Reference-family folder effect | N/A with reason: the worker may create one dated companion reference artifact under the existing reference root only; no stable reference family folder or README front door is created. |
| Storage layout action | N/A with reason: no folder movement, stable-path policy change, date-policy change, index update, or storage layout decision is authorized. |
| Claim boundary | This block prevents design-packet work from being misread as durable governance storage-layout mutation. |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher to no-commit docs-only worker to reviewer/closer |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=6a36aaa2e; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | worker may create only the design matrix and worker return named in the Mission; reviewer owns closure conversion |
| traceScope(phase, actor) | worker trace must cover required reads, source verification, gate commands, git status, expected manifest, actual changed set, and provider-local stray-file disposition |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | no source/test, runtime, session-sync, public-sync, provider-local, IDE config, or unrelated governed artifact edits are authorized for worker |
| nextMoveSurfaces | reviewer/closer updates next-move surfaces only once reviewer acceptance is recorded and in a separate session-sync commit |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN_COMPLETION_2026-07-06.md` (optional; prefer repairing evidence in the worker return per gotcha 30) |
| reviewerOwnedClosurePaths | worker return reviewer decision; optional completion review only if required; paired work order status conversion if closure proceeds |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Output Checker Read-Ahead Mandate

Before writing each worker-owned output artifact, read checker source for that
file's docType, path family, and conditional content class.

| Output artifact | Required read-ahead result |
| --- | --- |
| worker return under `docs/reviews` | derive exact review headings, worker-return quality terms, trace labels, delta boundary labels, corpus/value/rescan tokens, no-commit evidence shape, static-analysis diagnostic handling, and workspace hygiene evidence before writing |
| companion reference under `docs/reference` | derive exact reference headings such as Scope / Applies To, Target / Source, source verification, design disposition, trace, and claim-boundary labels before writing |

Literal-shape reminders: do not list required headings as backticked heading
strings before the real section; write source-not-found disposition spelling
instead of the exact blocked enum in literalTokensReviewed; avoid stale
dependency wording unless a dependency-release row cites the accepted artifact
path and commit.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/reference/CVF_MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN_MATRIX_2026-07-06.md` | Create design matrix; select exactly one R43-T1 disposition; source-verify proposed implementation surfaces and invariants; record no-runtime boundary. |
| `docs/reviews/CVF_MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN_WORKER_RETURN_2026-07-06.md` | Create worker return; include required trace, gates, git status, worker-output quality controls, static-analysis disposition, provider-local stray-file disposition, and final `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`. |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN_WORKER_RETURN_2026-07-06.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Shape-list rule: when listing required worker-output sections, write section
names without the heading prefix. Reserve actual heading syntax for real
sections so structural checkers do not treat this checklist as the artifact
section body.

## Execution Plan

| Step | Action | Evidence |
| --- | --- | --- |
| 1 | Capture `executionBaseHead` and `git status --short --untracked-files=all`. | Worker return Agent Operation Trace Block. |
| 2 | Read required startup, R41/R42, source, and checker files. | Worker return source inventory and checker read-ahead. |
| 3 | Compare at least three design options: reuse `evaluateRuntimeMemoryAction`, introduce a narrow route-authority actor-role field, or keep held pending missing authority. | Design matrix option table. |
| 4 | Select exactly one R43-T1 disposition and define the next allowed move. | Design matrix Selected Disposition section. |
| 5 | Run worker-return fast gate and pre-implementation autorun on the worker changed set. | Worker return verification table. |
| 6 | Leave worker artifacts uncommitted for reviewer closure conversion. | `git status --short --untracked-files=all` evidence. |

## Verification Commands

```powershell
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
git status --short --untracked-files=all
```

## Evidence Requirements

| Evidence item | Required evidence |
| --- | --- |
| Source verification | Every design option and selected disposition must cite CVF-governed source, accepted R41/R42 artifact evidence, or current runtime source lines. |
| No-runtime boundary | Worker return must state that no MinerU runtime, persistence invocation, provider/live proof, private-output read, Memory/RAG release, public-sync, source/test edit, commit, push, or public claim occurred. |
| Design readiness | If `R43_T1_ACTOR_ROLE_WIRING_DESIGN_READY_FOR_IMPLEMENTATION_PACKET` is selected, the matrix must name the later implementation surfaces and invariants without editing them. |
| Workspace hygiene | Worker return must include fresh `git status --short --untracked-files=all` output and disclose or remove provider-local and IDE side-channel files without staging them. |
| Gate evidence | Worker return must record `run_worker_return_fast_gate.py` and pre-implementation autorun results run after final edits. |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | local workspace |
| Session or invocation | MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN dispatch authoring, 2026-07-06 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, scaffold helper, ADIF resolver, apply_patch, governance gates |
| Target paths | `docs/baselines/CVF_GC018_MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN_2026-07-06.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN_2026-07-06.md` |
| Allowed scope source | operator requested a fresh design packet to wire actor-role authority into `fileBackedPersistenceRequested` |
| Before status evidence | clean worktree confirmed at HEAD `6a36aaa2e`; R42-T1 closed missing-confirmed and authorized only fresh design packet authoring |
| After status evidence | paired R43-T1 GC-018 baseline and work order created as DISPATCH_READY after gates pass |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | dispatch artifact authoring only |
| Claim boundary | docs-only design dispatch; no source/test edit, runtime, provider/live proof, persistence invocation, Memory/RAG release, public-sync, worker commit, push, or public claim |
| Agent type | dispatcher |
| Invocation ID | `msea-r43-t1-actor-role-persistence-authority-wiring-design-dispatch-2026-07-06` |
| Expected manifest | `docs/baselines/CVF_GC018_MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN_2026-07-06.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN_2026-07-06.md` |
| Actual changed set | `docs/baselines/CVF_GC018_MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN_2026-07-06.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN_2026-07-06.md` |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R43-T1 dispatch authoring for docs-only actor-role persistence authority wiring design |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, or mandatory-wrapper behavior is claimed. |
| receiptEvidence | N/A with reason: no runtime receipt is created or consumed by this dispatch packet. |
| actionEvidence | N/A with reason: no runtime action is executed or observed. |
| invocationBoundary | worker may read source and write only the two planned docs artifacts. |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized. |
| claimLanguage | dispatch-readiness and design-only authority only |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router behavior without a fresh source-verified authorization. |

## Acceptance Criteria

- Worker creates only the two artifacts named in the Mission.
- Worker selects exactly one R43-T1 disposition token.
- Worker distinguishes existing actor-role type usage from `fileBackedPersistenceRequested` decision-path authority.
- Worker names the minimal later implementation surfaces if the selected design is ready for an implementation packet.
- Worker does not edit source/test files or invoke any runtime or persistence path.
- Worker records fresh gate evidence, current git status, static-analysis diagnostic handling, and provider-local stray-file disposition.
- Worker returns uncommitted `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Review Gate

Reviewer must reject or repair within allowed scope if the worker output
overclaims implementation, treats adjacent actor-role type usage as route
decision authority, omits fresh gate evidence, leaves undisclosed stray
provider-local or IDE files, edits source/test files, or expands into runtime,
private-output, persistence invocation, provider/live proof, Memory/RAG release,
public-sync, push, or public claim.

Required reviewer commands before closure conversion:

```powershell
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return --base <closureBaseHead> --head HEAD --enforce
```

## Closure Checklist

- [ ] Worker return is `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`, not a worker-made closure.
- [ ] Design matrix selects exactly one R43-T1 disposition token.
- [ ] Source Verification rows are current and cite accepted source files or sections.
- [ ] No source/test/runtime/private-output/provider-live/public-sync/provider-local or IDE config edit occurred.
- [ ] Fresh worker-return gate and pre-implementation autorun evidence is recorded.
- [ ] Reviewer/closer owns any material closure commit.
- [ ] Session-sync surfaces are updated separately only if closure changes current mode or next allowed move.

## Operator Checkpoint

No operator checkpoint is required for the worker to complete the docs-only
design analysis. Fresh operator authorization is required before any later
implementation packet, source/test edit, runtime execution, persistence
invocation, provider/live proof, public-sync, push, public claim, or use-case
legal workflow expansion.

## Fail Conditions

- Any source/test edit.
- Any MinerU runtime execution, private/generated output content read, file-backed persistence invocation, provider/live proof, public-sync, worker commit, push, or public claim.
- Any design-ready claim that treats the existing `RuntimeMemoryActorRole` type cast alone as route-decision authority.
- Missing Source Verification Block, ADIF disclosure, checker read-ahead, worker output manifest, or no-commit handoff controls.
- Missing or stale gate evidence.
- Provider-local or IDE config file left undisclosed or staged.

## Claim Boundary

This work order authorizes only R43-T1 docs-only actor-role persistence
authority wiring design. It does not authorize implementation, hook wiring,
source/test edits, file-backed persistence invocation, production durable-store
invocation, Memory/RAG production route release, retrieval, vectorization,
live/provider proof, public-sync, use-case/legal work, worker commit, push, or
public claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: This is a private provenance dispatch work order. No public-sync
artifact is changed or authorized by this packet.
