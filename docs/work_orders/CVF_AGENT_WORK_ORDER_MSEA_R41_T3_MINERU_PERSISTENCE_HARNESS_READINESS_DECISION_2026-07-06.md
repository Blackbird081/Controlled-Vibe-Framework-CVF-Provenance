# CVF Agent Work Order - MSEA R41 T3 MinerU Persistence Harness Readiness Decision

Memory class: governed-worker-dispatch

Status: CLOSED

Batch ID: MSEA_R41_T3_MINERU_PERSISTENCE_HARNESS_READINESS_DECISION

Dispatch base head: 6b03910e4

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: reviewer or delegated reviewer

Worker return path: `docs/reviews/CVF_MSEA_R41_T3_MINERU_PERSISTENCE_HARNESS_READINESS_DECISION_WORKER_RETURN_2026-07-06.md`

## Dispatch Prompt Envelope

Role: delegated docs-only readiness-decision worker for MSEA_R41_T3_MINERU_PERSISTENCE_HARNESS_READINESS_DECISION.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R41_T3_MINERU_PERSISTENCE_HARNESS_READINESS_DECISION_2026-07-06.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-06; current session state points from accepted R41-T2 completion review `docs/reviews/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_COMPLETION_2026-07-06.md` at material commit `4a08d3ef0` to operator-selected T3 lane handling.

Do-not-misread notes: This packet is not implementation authority, not a persistence harness execution packet, and not a production route release. Do not edit source/test files, run MinerU, read private/generated output, invoke file-backed persistence, invoke production durable-store behavior, release Memory/RAG, run provider/live proof, public-sync, commit, push, or make public claims.

Required first actions: read required startup files, guard orientation, literal gotchas, this packet, the paired GC-018 baseline, accepted R41-T1 and R41-T2 artifacts, source rows in the Source Verification Block, and all checker source listed in the Checker Source Read-Ahead Block before writing any artifact.

Return contract: create the decision matrix and worker return artifact, run required gates, leave changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Execute the R41-T3 docs-only readiness decision for a minimal production-adjacent MinerU persistence harness. The worker must decide whether a later narrow implementation packet may be authored, remains blocked by R41-T2 authority gaps, or should stop, while preserving all private-output, receipt, and Memory/RAG release boundaries.

rawMemoryReleased=false. This work order does not authorize raw memory release, retrieval, reinjection, private-output reading, memory write, file-backed persistence invocation, persistence-mode widening, or Memory/RAG route release.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA_R41_T3_MINERU_PERSISTENCE_HARNESS_READINESS_DECISION --title "MSEA R41 T3 MinerU Persistence Harness Readiness Decision" --date 2026-07-06 --base 6b03910e4 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced placeholders with R41-T3 readiness-decision scope, no-commit handoff controls, worker output manifest, dependency-release evidence, source verification, ADIF disclosure, and private-only boundaries. |
| checkerReadAheadConfirmation | Read `governance/compat/check_work_order_dispatch_quality.py`, `governance/compat/check_governed_artifact_checker_read_ahead.py`, `governance/compat/check_dispatch_prompt_envelope.py`, `governance/compat/check_dispatch_scaffold_provenance.py`, `governance/compat/check_adif_defect_registry_disclosure.py`, `governance/compat/check_agent_handoff_boundary.py`, and `governance/compat/check_public_export_disposition.py` before authoring. |
| docOnlyNewFields | `selectedR41T3Disposition`, `harnessReadinessBlocker`, `harnessReopenCondition` |
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
| Intake source | Operator request plus active session next allowed move from accepted R41-T2 closure at material commit `4a08d3ef0` |
| intake summary | Docs-only readiness decision for minimal production-adjacent persistence harness lane |
| scope classification | governed readiness-decision dispatch; no source/test edit, runtime, provider/live, public-sync, or persistence invocation |
| risk sensitivity | R2 governance/system-chain readiness decision with private-output and memory-release boundaries |
| Route | `SINGLE_AGENT_SINGLE_ROLE` |
| selected role route | `SINGLE_AGENT_SINGLE_ROLE` |
| dispatchRole | dispatcher has authored this packet and paired GC-018 baseline |
| workerRole | delegated worker performs docs-only readiness evidence synthesis |
| reviewerRole | reviewer/closer evaluates returned artifacts and owns closure conversion |
| rolePattern | dispatcher to no-commit docs-only worker to reviewer/closer |
| Commit mode | `WORKER_MUST_NOT_COMMIT` |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if worker needs scope expansion, source/test edit, live/provider proof, public-sync, persistence invocation, use-case/legal work, commit, push, or claim-boundary change |

## Authority Chain

| Authority | Evidence |
| --- | --- |
| Operator instruction | User selected the T3 lane after receiving the R41-T1 through R41-T4 roadmap proposal. |
| Active session front door | `CVF_SESSION_MEMORY.md` records R41-T2 closure and operator reopen-lane-or-stop decision posture. |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` points to active handoff `AGENT_HANDOFF_V37_2026-07-06.md`. |
| Active handoff | `AGENT_HANDOFF_V37_2026-07-06.md` records the R41-T2 closed mode and no-runtime boundary. |
| Accepted R41-T2 decision | `docs/reference/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_MATRIX_2026-07-06.md` selected held disposition pending authority gaps. |
| Accepted R41-T2 completion review | `docs/reviews/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_COMPLETION_2026-07-06.md` closed R41-T2 bounded and preserved the reopen condition. |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_MSEA_R41_T3_MINERU_PERSISTENCE_HARNESS_READINESS_DECISION_2026-07-06.md` |

## Dependency Release Evidence

| Dependency | Evidence artifact | Commit | Release disposition | T3 consequence |
| --- | --- | --- | --- | --- |
| R41-T1 file-backed persistence release authority decision | `docs/reviews/CVF_MSEA_R41_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_AUTHORITY_DECISION_COMPLETION_2026-07-06.md` | `51216fb9a` | Held pending authority gaps | T3 must not implement persistence until later authority exists |
| R41-T2 persistence-mode authorization decision | `docs/reviews/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_COMPLETION_2026-07-06.md` | `4a08d3ef0` | Held pending authority gaps | T3 readiness worker must treat harness implementation as blocked unless fresh accepted evidence satisfies R41-T2 reopen condition |
| Active session next move | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `6b03910e4` | Operator may select fresh source-verified packet, different held lane, or stop | Operator selected the T3 lane; dispatch remains docs-only and no-runtime |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap or source requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| Proposed R41-T3 minimal production-adjacent persistence harness should run only if T1/T2 release enough | Purpose; Mission; Dependency Release Evidence | `selectedR41T3Disposition` in decision matrix | Source verification rows for R41-T1 and R41-T2 held decisions | PASS |
| R41-T2 keeps persistence-mode authorization held pending authority gaps | Source Verification Block; Mission | `harnessReadinessBlocker` | Worker checks accepted R41-T2 matrix and completion review | PASS |
| Preserve no-runtime/no-private/no-release boundary | Forbidden Scope; Claim Boundary | Worker return claim boundary | Worker-return fast gate and reviewer closure | PASS |
| Avoid use-case/legal deep dive | Forbidden Scope; Acceptance Criteria | worker return boundary | Reviewer checks claim boundary | PASS |

## Mission

Create exactly two worker-owned artifacts:

- `docs/reference/CVF_MSEA_R41_T3_MINERU_PERSISTENCE_HARNESS_READINESS_DECISION_MATRIX_2026-07-06.md`
- `docs/reviews/CVF_MSEA_R41_T3_MINERU_PERSISTENCE_HARNESS_READINESS_DECISION_WORKER_RETURN_2026-07-06.md`

The decision matrix must select exactly one disposition:

- `R41_T3_MINIMAL_PERSISTENCE_HARNESS_BLOCKED_BY_R41_T2_AUTHORITY_GAPS`
- `R41_T3_MINIMAL_PERSISTENCE_HARNESS_READY_FOR_NARROW_IMPLEMENTATION_PACKET`
- `R41_T3_MINIMAL_PERSISTENCE_HARNESS_REJECTED_STOP`

The worker must select the blocked disposition unless it can cite accepted, source-verified evidence that satisfies the R41-T2 reopen condition. The worker must not treat the operator's desire to proceed to T3 as authority to run or implement a harness.

## Required Artifact Manifest

| Artifact | Required path | Owner | Closure disposition |
| --- | --- | --- | --- |
| Decision matrix | `docs/reference/CVF_MSEA_R41_T3_MINERU_PERSISTENCE_HARNESS_READINESS_DECISION_MATRIX_2026-07-06.md` | no-commit worker | accepted by reviewer completion |
| Worker return | `docs/reviews/CVF_MSEA_R41_T3_MINERU_PERSISTENCE_HARNESS_READINESS_DECISION_WORKER_RETURN_2026-07-06.md` | no-commit worker | accepted by reviewer completion |
| Completion review | `docs/reviews/CVF_MSEA_R41_T3_MINERU_PERSISTENCE_HARNESS_READINESS_DECISION_COMPLETION_2026-07-06.md` | reviewer/closer | `CLOSED_PASS_BOUNDED` |

## Allowed Scope

- Read only CVF-governed startup files, the paired GC-018 baseline, this work order, accepted R41-T1 and R41-T2 artifacts, and source files named in the Source Verification Block if fresh verification is necessary.
- Write only the two worker-owned artifacts named in the Mission.
- Use `rg`, `git status`, `git diff`, `git rev-parse`, source line reads, worker-return scaffold, worker-return fast gate, and pre-implementation autorun gates.
- Repair documentation-only gate failures inside the two worker-owned artifacts.
- Record provider-local or IDE stray files as removed or disclosed if they appear, without staging them.

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
- No use-case/legal workflow.
- No provider-local memory as source authority.
- No worker commit.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001 - Avoid exhaustive directory claims; worker must cite exact files and status evidence only.
- ADIF-0002 - Use only CVF-governed sources for cited evidence; provider-local notes stay out of evidence rows.
- ADIF-0014 - Completeness is bounded to this readiness decision and not a broad absorption claim.
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
| `docs/baselines/CVF_GC018_MSEA_R41_T3_MINERU_PERSISTENCE_HARNESS_READINESS_DECISION_2026-07-06.md` | Paired GC-018 dispatch baseline. |
| `docs/reference/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_MATRIX_2026-07-06.md` | Accepted R41-T2 decision matrix. |
| `docs/reviews/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_COMPLETION_2026-07-06.md` | Accepted R41-T2 completion review. |
| Source files named in Source Verification Block if worker recomputes source anchors | Required source facts for any readiness claim beyond accepted R41-T2 evidence. |

## Pre-Flight Checks

| Command | Required disposition |
| --- | --- |
| `git rev-parse --short HEAD` | Capture executionBaseHead before writing worker artifacts. |
| `git status --short --untracked-files=all` | Record pending and stray files before work. |
| `python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_MSEA_R41_T3_MINERU_PERSISTENCE_HARNESS_READINESS_DECISION_WORKER_RETURN_2026-07-06.md --title "MSEA R41 T3 MinerU Persistence Harness Readiness Decision Worker Return"` | Create checker-safe worker-return scaffold. |
| `python governance/compat/run_worker_return_fast_gate.py` | Run once on scaffold and once after final worker edit. |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD` | Required before worker handoff. |

## Write Ownership

| Path | Owner | Disposition |
| --- | --- | --- |
| `docs/reference/CVF_MSEA_R41_T3_MINERU_PERSISTENCE_HARNESS_READINESS_DECISION_MATRIX_2026-07-06.md` | worker | Allowed to create only. |
| `docs/reviews/CVF_MSEA_R41_T3_MINERU_PERSISTENCE_HARNESS_READINESS_DECISION_WORKER_RETURN_2026-07-06.md` | worker | Allowed to create only. |
| Source, tests, session state, handoff, public-sync, provider-local files | none for worker | Forbidden unless a future packet authorizes. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | `Dispatch Prompt Envelope`; `Role:`; `Canonical packet:`; `Commit mode:`; `executionBaseHead`; `Current-time notes:`; `Do-not-misread notes:`; `Required first actions:`; `Return contract:`; `Scaffold Provenance Block`; `ADIF Defect Registry Disclosure`; `Agent Handoff Contract Control Block`; `Reviewer Closure Conversion`; `Worker Return Packet Shape Contract`; `Work-Order Fulfillment Manifest`; `DEFERRED_PRIVATE_ONLY`; source-not-found disposition spelling |
| gateRunPurpose | Confirmation evidence for dispatch shape, not first discovery. |
| claimBoundary | Read-ahead confirms required literal surfaces for this work order and paired baseline only; it does not prove worker execution, closure, runtime behavior, or public export. |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R41-T2 selected persistence-mode authorization held pending authority gaps | VALUE_SET | `docs/reference/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_MATRIX_2026-07-06.md` | Selected Disposition section | `R41_T2_PERSISTENCE_MODE_AUTHORIZATION_HELD_PENDING_AUTHORITY_GAPS` | R41-T2 decision matrix | ACCEPT |
| R41-T2 closure accepted the held disposition | VALUE_SET | `docs/reviews/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_COMPLETION_2026-07-06.md` | Reviewer Decision section | `R41_T2_AUTHORITY_DECISION_COMPLETE_HELD_PENDING_AUTHORITY_GAPS` | R41-T2 completion review | ACCEPT |
| R41-T2 reopen condition requires explicit source-backed persistence authority actor or equivalent typed/runtime invariant | VALUE_SET | `docs/reference/CVF_MSEA_R41_T2_MINERU_PERSISTENCE_MODE_AUTHORIZATION_DECISION_MATRIX_2026-07-06.md` | Reopen Condition section | `R41-T2 reopen condition` | R41-T2 decision matrix | ACCEPT |
| R41-T1 file-backed persistence release remained held pending authority gaps | VALUE_SET | `docs/reference/CVF_MSEA_R41_T1_MINERU_FILE_BACKED_PERSISTENCE_RELEASE_AUTHORITY_DECISION_MATRIX_2026-07-06.md` | Selected Disposition section | `R41_T1_FILE_BACKED_PERSISTENCE_RELEASE_HELD_PENDING_AUTHORITY_GAPS` | R41-T1 decision matrix | ACCEPT |
| Active session next move allows operator to select a fresh source-verified packet, different held lane, or stop | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `nextAllowedMove` | `nextAllowedMove` | active session bootstrap read model | ACCEPT |
| Current T3 dispatch is operator-selected but remains docs-only and no-runtime | DOC_ONLY_NEW | `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R41_T3_MINERU_PERSISTENCE_HARNESS_READINESS_DECISION_2026-07-06.md` | Purpose and Mission sections | `selectedR41T3Disposition` | R41-T3 work order | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Path existence for R41-T3 baseline | `Test-Path docs/baselines/CVF_GC018_MSEA_R41_T3_MINERU_PERSISTENCE_HARNESS_READINESS_DECISION_2026-07-06.md` returned `False` before authoring. | ACCEPT_NO_COLLISION |
| Path existence for R41-T3 work order | `Test-Path docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R41_T3_MINERU_PERSISTENCE_HARNESS_READINESS_DECISION_2026-07-06.md` returned `False` before authoring. | ACCEPT_NO_COLLISION |
| Path existence for R41-T3 worker outputs | `Test-Path` for the planned matrix and worker-return paths returned `False` before authoring. | ACCEPT_NO_COLLISION |
| Token collision search | `rg -n "MSEA-R41-T3|MSEA_R41_T3|R41_T3|CVF_MSEA_R41_T3" docs/baselines docs/work_orders docs/reviews docs/reference CVF_SESSION` returned no matches before authoring. | ACCEPT_NO_COLLISION |
| Collision decision | R41-T3 artifact names are new in governed dispatch/review/reference/session surfaces. | ACCEPT |

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

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher authored packet; worker creates no-commit artifacts; reviewer/closer owns closure conversion |
| phase | dispatch and pending worker execution |
| baseHeadFor(phase) | dispatchBaseHead=6b03910e4; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | Worker owns only the matrix and worker return paths named in Mission. |
| traceScope(phase, actor) | Worker return must record repo-local Agent Operation Trace Block with commands, before/after status, diff evidence, and allowed-scope source. |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/committer owns any reviewed material commit. |
| crossBatchIsolation | Dispatch begins from clean worktree at 6b03910e4; worker must disclose any unrelated or provider-local stray files and leave them unstaged. |
| nextMoveSurfaces | Worker must not edit session state, front door, handoff, roadmap, public catalog, or next-move surfaces; reviewer/closer updates them if closure is accepted. |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R41_T3_MINERU_PERSISTENCE_HARNESS_READINESS_DECISION_COMPLETION_2026-07-06.md` |
| reviewerOwnedClosurePaths | `docs/reviews/CVF_MSEA_R41_T3_MINERU_PERSISTENCE_HARNESS_READINESS_DECISION_COMPLETION_2026-07-06.md`; this work order if status changes; active session surfaces only if reviewer accepts closure. |
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
| `docs/reference/CVF_MSEA_R41_T3_MINERU_PERSISTENCE_HARNESS_READINESS_DECISION_MATRIX_2026-07-06.md` | Create as source-verified readiness decision matrix with exactly one selected R41-T3 disposition token and explicit blocker or accepted-authority rationale. |
| `docs/reviews/CVF_MSEA_R41_T3_MINERU_PERSISTENCE_HARNESS_READINESS_DECISION_WORKER_RETURN_2026-07-06.md` | Create from worker-return scaffold, include required review headings and evidence, pass fast gate, and leave uncommitted. |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R41_T3_MINERU_PERSISTENCE_HARNESS_READINESS_DECISION_WORKER_RETURN_2026-07-06.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Shape-list rule: when listing required worker-output sections, write section names without the section-prefix marker. Reserve actual heading syntax for real sections so structural checkers do not treat this checklist as the artifact section body.

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
- Verification Evidence
- Claim Boundary

The worker return must also record `executionBaseHead`, `git status --short`,
and N/A with reason dispositions for conditional sections that do not apply.

## Verification Commands

Worker must run these commands from repo root and record results in the worker return:

```powershell
git rev-parse --short HEAD
python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_MSEA_R41_T3_MINERU_PERSISTENCE_HARNESS_READINESS_DECISION_WORKER_RETURN_2026-07-06.md --title "MSEA R41 T3 MinerU Persistence Harness Readiness Decision Worker Return"
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
| Session or invocation | MSEA_R41_T3_MINERU_PERSISTENCE_HARNESS_READINESS_DECISION dispatch authoring, 2026-07-06 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | `rg`; `Get-Content`; ADIF resolver; dispatch scaffold helper; `apply_patch`; planned dispatch gates |
| Target paths | Paired GC-018 baseline and this work order |
| Allowed scope source | Operator selected T3 lane plus R41-T2 accepted closure next allowed move |
| Before status evidence | `git status --short --untracked-files=all` clean worktree at dispatch base 6b03910e4 |
| After status evidence | Pending dispatch artifacts before commit; final evidence belongs to dispatcher commit and reviewer closure. |
| Diff evidence | `git diff --name-status` for dispatch range |
| Approval boundary | Docs-only dispatch packet authoring; no worker execution, runtime, public-sync, or source/test edit authorized. |
| Claim boundary | Repo-local trace only; no OS/user attribution, runtime behavior, or provider/live claim. |
| Agent type | dispatcher |
| Invocation ID | `msea-r41-t3-persistence-harness-readiness-decision-dispatch-2026-07-06` |
| Expected manifest | paired GC-018 baseline and this work order |
| Actual changed set | paired GC-018 baseline and this work order before commit |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename occurred |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | docs-only R41-T3 readiness dispatch for a minimal production-adjacent persistence harness decision |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, persistence invocation, or runtime harness behavior is claimed |
| receiptEvidence | N/A with reason: no runtime receipt or MinerU execution is authorized |
| actionEvidence | ACTION_EVIDENCE_PRESENT: dispatch artifacts and gate evidence only |
| invocationBoundary | Worker may write governed decision artifacts only; no runtime invocation |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized |
| claimLanguage | The packet asks for a source-verified readiness decision, not implementation or proof of production behavior |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router behavior without a fresh source-verified authorization |

## Execution Plan

| Step | Input | Output | Validation or stop condition |
| --- | --- | --- | --- |
| 1 | Required First Reads | Source inventory in worker return | Stop if a required source is missing or contradictory. |
| 2 | Accepted R41-T1 and R41-T2 artifacts | Decision matrix draft | Stop if no accepted authority evidence exists beyond R41-T2 hold. |
| 3 | Worker-return scaffold | Worker return draft | Run fast gate on scaffold before long prose. |
| 4 | Final matrix and worker return | Gate evidence | Run pre-implementation autorun and final fast gate. |
| 5 | Pending worker-owned artifacts | COMPLETE_PENDING_REVIEW handoff | Record actual `git status --short --untracked-files=all`; do not commit. |

## Evidence Requirements

| Evidence | Required form |
| --- | --- |
| Source verification | Table rows with source file, line/section, symbol-only cell, and disposition. |
| Decision | Exactly one R41-T3 disposition token in the matrix. |
| Worker gate evidence | Exact commands and PASS/BLOCKED/N/A with reason results in worker return. |
| Workspace hygiene | `git status --short --untracked-files=all` after final edit. |
| raw memory invariant | `rawMemoryReleased=false` in worker return and matrix claim boundary. |

## Acceptance Criteria

- Worker creates only the two owned artifacts named in the Mission.
- Decision matrix selects exactly one R41-T3 disposition token.
- If selecting ready-for-implementation-packet, matrix names accepted evidence that satisfies the R41-T2 reopen condition.
- If selecting blocked or stop, matrix names the unresolved authority gap and a concrete reopen or stop condition.
- Source Verification rows cite existing source files or accepted R41 artifacts and use symbol-only cells.
- Worker return records fresh gate commands, actual pending worktree status, and provider-local stray-file hygiene.
- No source/test edit, runtime execution, private-output read, persistence invocation, Memory/RAG release, live/provider proof, public-sync, commit, push, or public claim occurs.

## Fail Conditions

- Missing or multiple selected R41-T3 disposition tokens.
- Ready-for-implementation-packet is selected without source-backed evidence satisfying the R41-T2 reopen condition.
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

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Closure status | this work order | `Status: CLOSED` | PASS |
| Work order status | this work order | `Status: CLOSED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_MSEA_R41_T3_MINERU_PERSISTENCE_HARNESS_READINESS_DECISION_COMPLETION_2026-07-06.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | N/A | N/A with reason: R41-T3 is a standalone operator-selected readiness lane packet, not a roadmap-derived closure | N/A with reason |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | `python governance/compat/generate_corpus_scan_registry.py --check` PASS during worker-return fast gate | PASS |
| Registry Markdown | changed corpus registry coverage | reviewer-fast changed corpus registry coverage PASS | PASS |
| External evidence digest | N/A | N/A with reason: no external evidence artifact, public-web source, or local external file was absorbed | N/A with reason |
| System loop interlock | R41-T3 decision matrix and completion review | `R41_T3_MINIMAL_PERSISTENCE_HARNESS_BLOCKED_BY_R41_T2_AUTHORITY_GAPS`; no harness implementation or persistence-mode widening | PASS |
| Session continuity | session state, session memory, and active handoff | dedicated session-sync commit required after material commit | PASS |
| Worker return | `docs/reviews/CVF_MSEA_R41_T3_MINERU_PERSISTENCE_HARNESS_READINESS_DECISION_WORKER_RETURN_2026-07-06.md` | `Status: COMPLETE_PENDING_REVIEW`, accepted by completion review | PASS |
| Runtime boundary | R41-T3 completion review | no source/test/runtime/private/provider/public execution | PASS |
| Public disposition | this work order | `DEFERRED_PRIVATE_ONLY` | PASS |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
| --- | --- | --- |
| No runtime receipt is accepted by this closure | R41-T3 remains docs-only and accepts no MinerU runtime, harness execution, file-backed persistence, provider/live, memory-write, public-sync, or production route receipt | PASS |
| Worker return accepted only after reviewer closure | Completion review records `CLOSED_PASS_BOUNDED` | PASS |

## Claim Boundary

This work order authorizes only a docs-only R41-T3 readiness decision worker return. It does not authorize implementation, hook wiring, source/test edits, MinerU execution, private/generated output reads, file-backed persistence invocation, persistence-mode widening, production durable-store invocation, production Memory/RAG invocation or release, retrieval, vectorization, provider/live proof, public-sync, use-case/legal work, worker commit, push, or public claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: This is a private provenance work order. No public-sync artifact is changed or authorized by this packet.
