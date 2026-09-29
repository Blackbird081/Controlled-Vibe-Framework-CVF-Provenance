# CVF Agent Work Order - KIOD-R11 Runtime Candidate Reopen Inventory Guard

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: KIOD-R11

Dispatch base head: `9c7aa4d5`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated worker role

Reviewer/closer: reviewer/closer role

Worker return path: `docs/reviews/CVF_KIOD_R11_RUNTIME_CANDIDATE_REOPEN_INVENTORY_GUARD_WORKER_RETURN_2026-07-02.md`

## Dispatch Prompt Envelope

Role: delegated worker for KIOD-R11.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_KIOD_R11_RUNTIME_CANDIDATE_REOPEN_INVENTORY_GUARD_2026-07-02.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: capture with `git rev-parse --short HEAD` at worker start.

Current-time notes: artifact date is 2026-07-02; dispatch base head is
`9c7aa4d5`. KIOD-R10 is closed at material commit `e89e3dd4` and recorded
D-file06 plus I-file19 as parked runtime candidates with concrete reopen
conditions.

Do-not-misread notes: this packet authorizes only KIOD-specific local
governance inventory/checker/test/catalog work. It does not authorize vector
retrieval, LanceDB, embeddings, Learning Plane runtime integration,
provider/live proof, source import, public-sync, Web/UI/dashboard work,
MCP/CLI adapter behavior, package lifecycle mutation, model-router work,
action authority, automatic invocation, or production-readiness claims.

Required first actions: read required startup files, guard orientation,
literal-format gotchas, this work order, the paired GC-018 baseline, KIOD-R10
decision artifacts, value-parked standard, FPC parked-reopen inventory/checker
pattern, hook/autorun catalogs, and all checker source listed in the Checker
Source Read-Ahead Block before writing any artifact.

Return contract: create the inventory/checker/tests/wiring and worker return,
run required gates, leave changes uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Implement a KIOD-specific runtime-candidate reopen inventory guard so future
agents cannot casually re-propose D-file06 or I-file19 runtime work without
source-backed evidence that the KIOD-R10 recorded reopen condition has been
met. Success means the inventory, checker, tests, and gate wiring are present,
focused, and bounded to KIOD runtime candidates.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id KIOD-R11 --title "Runtime Candidate Reopen Inventory Guard" --date 2026-07-02 --base 9c7aa4d5 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "KIOD-R10 closed at e89e3dd4 and recorded D-file06 plus I-file19 runtime candidates with concrete reopen conditions" --stdout --include-worker-return-skeleton` |
| generatedProfile | protected-governance-path plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Filled mission, dependency release, source verification, protected-path authorization, fulfillment manifest, dual-agent matrix, acceptance criteria, verification commands, and claim boundaries; removed unresolved scaffold markers from dispatch-ready fields. |
| checkerReadAheadConfirmation | `governance/compat/check_fpc_parked_reopen_inventory.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_worker_return_quality_gate.py` |
| docOnlyNewFields | `runtimeCandidateId`; `reopenConditionText`; `requiredReopenEvidence`; `forbiddenUntilReopenGatePasses`; `reproposalRule`; `kiodRuntimeCandidateReopenInventory` |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Authority Chain

| Authority | Evidence |
| --- | --- |
| Operator instruction | Operator accepted moving to the next tranche and instructed `ok. write work order`. |
| Active session front door | `CVF_SESSION_MEMORY.md` at HEAD `9c7aa4d5` records KIOD-R10 closed and operator next-lane selection. |
| Active handoff | `AGENT_HANDOFF_V31_2026-07-02.md` records KIOD-R10 closure and D-file06/I-file19 reopen conditions. |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_KIOD_R11_RUNTIME_CANDIDATE_REOPEN_INVENTORY_GUARD_2026-07-02.md` |
| KIOD-R10 decision packet | `docs/reviews/CVF_KIOD_R10_RUNTIME_DEFERRED_CANDIDATE_DECISION_2026-07-01.md` |
| KIOD-R10 worker return | `docs/reviews/CVF_KIOD_R10_RUNTIME_DEFERRED_CANDIDATE_DECISION_WORKER_RETURN_2026-07-01.md` |
| Value-parked standard | `docs/reference/CVF_VALUE_PARKED_LANE_REOPEN_DISCIPLINE_STANDARD_2026-06-25.md` |
| FPC parked-reopen precedent | `docs/reference/CVF_FPC_PRG_T1_PARKED_REOPEN_CONDITION_SOURCE_INVENTORY_2026-06-28.json`; `governance/compat/check_fpc_parked_reopen_inventory.py` |

## Agent Roles

| Role | Responsibility |
| --- | --- |
| dispatcher | Author this GC-018/work-order pair and run pre-dispatch gates. |
| worker | Execute only the allowed inventory/checker/test/wiring scope and create the worker return without committing. |
| reviewer/closer | Review worker return, repair only allowed-scope closure defects if needed, and own material commit if accepted. |
| session-sync steward | Update active state and handoff only if reviewer/closer creates an accepted material commit. |

## Required First Reads

| Path | Required action |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V31_2026-07-02.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |
| `docs/baselines/CVF_GC018_KIOD_R11_RUNTIME_CANDIDATE_REOPEN_INVENTORY_GUARD_2026-07-02.md` | READ |
| this work order | READ |
| `docs/reviews/CVF_KIOD_R10_RUNTIME_DEFERRED_CANDIDATE_DECISION_2026-07-01.md` | SOURCE_VERIFIED |
| `docs/reviews/CVF_KIOD_R10_RUNTIME_DEFERRED_CANDIDATE_DECISION_WORKER_RETURN_2026-07-01.md` | SOURCE_VERIFIED |
| `docs/reference/CVF_VALUE_PARKED_LANE_REOPEN_DISCIPLINE_STANDARD_2026-06-25.md` | SOURCE_VERIFIED |
| `docs/reference/CVF_FPC_PRG_T1_PARKED_REOPEN_CONDITION_SOURCE_INVENTORY_2026-06-28.json` | SOURCE_VERIFIED |
| `governance/compat/check_fpc_parked_reopen_inventory.py` | SOURCE_VERIFIED |
| `governance/compat/test_check_fpc_parked_reopen_inventory.py` | SOURCE_VERIFIED |
| `governance/compat/agent_autorun_command_catalog.py` | SOURCE_VERIFIED |
| `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | SOURCE_VERIFIED |
| `governance/compat/local_governance_hook_catalog_pre_commit.py` | SOURCE_VERIFIED |
| `governance/compat/local_governance_hook_catalog_pre_push.py` | SOURCE_VERIFIED |
| Applicable checker files listed in this packet's Checker Source Read-Ahead Block | READ |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly by reading the
failing checker source and matching the literal required shape. Worker should
return to orchestrator only for a source contradiction, forbidden-scope need,
or missing authority that makes completion impossible.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class dispatch --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | No resolver entries were returned for this exact query. Worker must still record any new repeated non-obvious defect pattern in ADIF before closure if one is found. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_fpc_parked_reopen_inventory.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_forbidden_filesystem_state.py` |
| literalTokensReviewed | `## Dispatch Prompt Envelope`; `Role:`; `Canonical packet:`; `Commit mode:`; `executionBaseHead`; `Return contract:`; `## Checker Source Read-Ahead Block`; `applicableCheckersRead`; `literalTokensReviewed`; `gateRunPurpose`; `claimBoundary`; `Source Verification Block`; `Claimed item`; `Source file`; `Verified line/section`; `Verified path or symbol`; `Owning interface/function/schema`; `Disposition`; `Agent Handoff Contract Control Block`; `Reviewer Closure Conversion`; `Core Guard Self-Protection Authorization`; `WORKER_MUST_NOT_COMMIT`; `Self-declared worker-return artifact: yes`; `WORKER_MUST_NOT_COMMIT honored`; `requiredLaneIds`; `laneInventories`; `conditionText`; `requiredConditions`; `forbiddenUntilGatePasses`; `reproposalRule`; `## Delta Execution Claim Boundary Control Block`; `CLAIM_REJECTED`; `CLAIM_REJECTED_NO_RECEIPT`; `CLAIM_REJECTED_NO_ACTION`; `## Public Export Disposition`; `DEFERRED_PRIVATE_ONLY`; `Agent Operation Trace Block` |
| gateRunPurpose | Confirmation evidence, not first discovery; checker source and literal tokens were read before this work order was authored. |
| claimBoundary | Read-ahead evidence for this dispatch packet only; worker must repeat read-ahead for its own changed artifacts before implementation. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Active session permits operator selection of a next governed lane after KIOD-R10 closure. | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | line 5 | `nextAllowedMove` | active session bootstrap read model | VALUE_SET | ACCEPT |
| Active handoff records KIOD-R10 closed and D-file06/I-file19 parked with concrete reopen conditions. | VALUE_SET | `AGENT_HANDOFF_V31_2026-07-02.md` | `Next Allowed Move`; lines 93-117 | `D-file06`; `I-file19`; `reopen` | active handoff | VALUE_SET | ACCEPT |
| KIOD-R10 decision packet records per-candidate reopen conditions for D-file06 and I-file19. | VALUE_SET | `docs/reviews/CVF_KIOD_R10_RUNTIME_DEFERRED_CANDIDATE_DECISION_2026-07-01.md` | lines 136-137 | `D-file06`; `I-file19` | KIOD-R10 decision packet | VALUE_SET | ACCEPT |
| KIOD-R10 worker return says future agents should not re-propose D-file06/I-file19 without first checking the recorded conditions. | VALUE_SET | `docs/reviews/CVF_KIOD_R10_RUNTIME_DEFERRED_CANDIDATE_DECISION_WORKER_RETURN_2026-07-01.md` | lines 358-361 | `reopen conditions`; `D-file06/I-file19` | KIOD-R10 worker return | VALUE_SET | ACCEPT |
| Value-parked standard requires concrete checkable reopen conditions and blocks re-proposal before checking them. | LITERAL_INVARIANT | `docs/reference/CVF_VALUE_PARKED_LANE_REOPEN_DISCIPLINE_STANDARD_2026-06-25.md` | `Required Action When Declining For Low Value`; `Required Action Before Re-Proposing` | `nextAllowedMove`; `reopen condition` | value-parked lane reopen discipline standard | VALUE_SET | ACCEPT |
| Existing FPC parked-reopen inventory checker defines the source-backed inventory pattern and required lane fields. | EXISTS | `governance/compat/check_fpc_parked_reopen_inventory.py` | lines 15-63 and 180-253 | `INVENTORY_PATH`; `REQUIRED_TOP_FIELDS`; `REQUIRED_LANE_FIELDS`; `REQUIRED_LANE_IDS`; `validate_inventory` | FPC parked-reopen inventory checker | EXISTS | ACCEPT |
| Existing FPC parked-reopen checker has focused tests for valid fixture, missing lane, condition drift, required-condition drift, wrong lane id, empty evidence fields, boundary flag drift, and forbidden-list drift. | EXISTS | `governance/compat/test_check_fpc_parked_reopen_inventory.py` | test methods | `TestFpcParkedReopenInventory` | FPC parked-reopen checker tests | EXISTS | ACCEPT |
| Existing gate catalogs already wire the FPC parked-reopen checker and provide the wiring pattern for KIOD-R11. | EXISTS | `governance/compat/agent_autorun_command_catalog.py`; `governance/compat/local_governance_hook_catalog_reviewer_fast.py`; `governance/compat/local_governance_hook_catalog_pre_commit.py`; `governance/compat/local_governance_hook_catalog_pre_push.py` | `FPC parked reopen inventory` entries | `FPC parked reopen inventory` | autorun and local hook catalogs | EXISTS | ACCEPT |
| Core guard marks `governance/compat/*.py` as protected and requires an authorization carrier. | LITERAL_INVARIANT | `governance/compat/check_core_guard_self_protection.py`; `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md` | protected path logic and Protected-Path Authorization Carrier | `Core Guard Self-Protection Authorization`; `Protected paths` | core guard self-protection checker and closure-quality standard | VALUE_SET | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Planned baseline path existence | `Test-Path docs/baselines/CVF_GC018_KIOD_R11_RUNTIME_CANDIDATE_REOPEN_INVENTORY_GUARD_2026-07-02.md` returned `False` before authoring. | PASS |
| Planned work-order path existence | `Test-Path docs/work_orders/CVF_AGENT_WORK_ORDER_KIOD_R11_RUNTIME_CANDIDATE_REOPEN_INVENTORY_GUARD_2026-07-02.md` returned `False` before authoring. | PASS |
| Planned worker-return path existence | `Test-Path docs/reviews/CVF_KIOD_R11_RUNTIME_CANDIDATE_REOPEN_INVENTORY_GUARD_WORKER_RETURN_2026-07-02.md` returned `False` before authoring. | PASS |
| Token collision search | `rg -n "KIOD-R11|Runtime Candidate Reopen Inventory Guard|kiod_runtime_candidate_reopen" docs governance CVF_SESSION AGENT_HANDOFF_V31_2026-07-02.md` found no prior KIOD-R11 artifact before authoring. | PASS |
| Collision decision | Existing FPC-PRG parked-reopen inventory/checker is precedent, not a KIOD owner surface. KIOD-R11 must create a KIOD-specific inventory/checker rather than broadening FPC lanes. | PASS |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| KIOD-R10 material closure | KIOD-R10 decision packet accepted at material commit `e89e3dd4`; session-sync completed at `6f42f4cc`; handoff marker sync completed at `9c7aa4d5`. | KIOD-R11 may systemize the recorded reopen conditions but must not change the KIOD-R10 decision itself. | SATISFIED |
| KIOD-R10 D-file06/I-file19 reopen conditions | `CVF_SESSION_MEMORY.md`, active handoff V31, and KIOD-R10 decision packet record concrete D-file06/I-file19 reopen conditions. | Worker must preserve the same semantic conditions in inventory/checker form. | SATISFIED |
| FPC-PRG precedent | FPC-PRG-T1 through T4 already established an inventory/checker/test/wiring pattern for parked reopen gates. | Worker may adapt the pattern for KIOD runtime candidates only; no FPC behavior change is authorized. | SATISFIED |

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| Intake summary | Operator selected the next governed lane after KIOD-R10 and accepted the proposed KIOD-R11 parked-runtime-candidate inventory guard. |
| Scope classification | Bounded governance-control implementation: KIOD-specific inventory, local checker, focused tests, hook/autorun catalog wiring, and worker return. |
| Risk sensitivity | Medium governance risk because protected `governance/compat/` paths and hook catalogs are authorized; runtime risk remains low because runtime work is forbidden. |
| Selected role route | routeMode=`SINGLE_AGENT_SINGLE_ROLE`; one worker executes, then reviewer/closer converts if accepted. |
| Role separation basis | Worker must not commit; reviewer/closer owns review, material commit, and any session-sync. |
| Escalation condition | Escalate with `BLOCKED_WITH_REASON` for forbidden scope, source contradiction, missing authority, or gate failure outside allowed-scope repair. |

## Commit Mode And Base-Anchor Lifecycle

| Field | Value |
| --- | --- |
| dispatchBaseHead | `9c7aa4d5` |
| executionBaseHead | Worker must capture with `git rev-parse --short HEAD` before edits. |
| closureBaseHead | Reviewer/closer sets this when reviewing the uncommitted worker return. |
| commitMode | WORKER_MUST_NOT_COMMIT |
| workerCommitPermission | FORBIDDEN |
| reviewerCommitOwner | reviewer/closer role only if the worker return is accepted |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher-authored packet to one worker role, then reviewer/closer conversion |
| phase | dispatch-to-worker |
| baseHeadFor(phase) | dispatchBaseHead=`9c7aa4d5`; executionBaseHead=worker captures at start; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | Worker may change only the Allowed scope paths listed in this work order. |
| traceScope(phase, actor) | Worker return must include Agent Operation Trace Block with expected manifest, actual changed set, and manifest delta. |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer owns any material commit if the worker return is accepted. |
| crossBatchIsolation | KIOD-R11 only; no runtime implementation, source import, Web, package, public-sync, MCP/CLI, provider/live, model-router, or session-sync work. |
| nextMoveSurfaces | Worker must not update next-move surfaces; reviewer/closer owns session-sync if closure is accepted. |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_KIOD_R11_RUNTIME_CANDIDATE_REOPEN_INVENTORY_GUARD_COMPLETION_2026-07-02.md` optional; prefer repairing evidence in the worker return unless a separate completion review is needed for checker shape. |
| reviewerOwnedClosurePaths | `docs/reference/CVF_KIOD_RUNTIME_CANDIDATE_REOPEN_CONDITION_INVENTORY_2026-07-02.json`; `governance/compat/check_kiod_runtime_candidate_reopen_inventory.py`; `governance/compat/test_check_kiod_runtime_candidate_reopen_inventory.py`; `governance/compat/agent_autorun_command_catalog.py`; `governance/compat/local_governance_hook_catalog_reviewer_fast.py`; `governance/compat/local_governance_hook_catalog_pre_commit.py`; `governance/compat/local_governance_hook_catalog_pre_push.py`; worker return path above; optional completion review path above |
| closureOwner | reviewer/closer role |
| workerCommitPermission | FORBIDDEN |

## Pre-Flight Checks

Worker must capture `executionBaseHead` with `git rev-parse --short HEAD`
before edits, run `git status --short`, and read the checker sources named in
this packet before writing the first changed artifact.

## Write Ownership

Worker owns only the allowed paths listed below and must leave all changes
uncommitted. Reviewer/closer owns acceptance, material commit, and any
session-sync.

## Allowed Scope

Allowed scope:

- `docs/reference/CVF_KIOD_RUNTIME_CANDIDATE_REOPEN_CONDITION_INVENTORY_2026-07-02.json`
- `governance/compat/check_kiod_runtime_candidate_reopen_inventory.py`
- `governance/compat/test_check_kiod_runtime_candidate_reopen_inventory.py`
- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_pre_push.py`
- `docs/reviews/CVF_KIOD_R11_RUNTIME_CANDIDATE_REOPEN_INVENTORY_GUARD_WORKER_RETURN_2026-07-02.md`

Reviewer-owned closure paths:

- `docs/baselines/CVF_GC018_KIOD_R11_RUNTIME_CANDIDATE_REOPEN_INVENTORY_GUARD_2026-07-02.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_KIOD_R11_RUNTIME_CANDIDATE_REOPEN_INVENTORY_GUARD_2026-07-02.md`
- `docs/reviews/CVF_KIOD_R11_RUNTIME_CANDIDATE_REOPEN_INVENTORY_GUARD_COMPLETION_2026-07-02.md` if needed

## Forbidden Scope

Forbidden scope:

- Do not change KIOD-R10 decision semantics or soften D-file06/I-file19 reopen conditions.
- Do not implement LanceDB, vector retrieval, embeddings, rerank, memory-index read, Learning Plane runtime integration, automatic promotion, provider/live proof, or service calls.
- Do not edit external source files, source mirrors, package lifecycle records, Web/UI/dashboard, MCP/CLI adapter, model-router, public-sync clone, generated session state, active handoff, or front door.
- Do not make runtime/provider/live, action-authority, automatic-invocation, public-readiness, or production-readiness claims.
- Do not broaden the FPC parked-reopen checker or change FPC inventory semantics.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: KIOD-R11 may create a KIOD runtime-candidate
reopen inventory checker, focused tests, and hook/autorun catalog wiring that
blocks or warns on unsupported D-file06/I-file19 re-proposal attempts.

Protected paths:

- `governance/compat/check_kiod_runtime_candidate_reopen_inventory.py`
- `governance/compat/test_check_kiod_runtime_candidate_reopen_inventory.py`
- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_pre_push.py`

Operator authorization: operator approved moving to the next tranche after
KIOD-R10 and requested a work order for the proposed KIOD-R11 checker-backed
runtime-candidate reopen inventory guard.

Rollback boundary: reviewer/closer may reject the uncommitted worker return;
no protected-path change is committed unless reviewer accepts the KIOD-R11
material batch. Do not revert KIOD-R10 material or session-sync commits.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | Repo-local governance checker and hook/autorun catalogs under `governance/compat/` | Internal agents receive machine feedback when governed docs attempt to re-propose D-file06/I-file19 without evidence. No runtime or action authority is granted. | This work order; paired GC-018; planned checker/test evidence. | N/A with reason: internal local governance gate only. | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | No CLI/MCP or external-agent adapter owner is authorized. | External agents may read the governed work order and receive local hook failures only when operating in this repo. No MCP/CLI tool, adapter, public surface, or external invocation contract is created. | Dual-agent accounting standard requires explicit disposition. | N/A_WITH_REASON: adapter work is forbidden by this dispatch and requires a fresh source-verified work order. | N/A_WITH_REASON |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | NOT_APPLICABLE_WITH_REASON: KIOD-R11 does not ingest new outside-source material; it systemizes KIOD-R10 internal decision evidence. |
| Matching local-view guard | N/A with reason: no new outside-source local-view guard is needed for KIOD-R11. |
| Owner surface | `docs/reviews/CVF_KIOD_R10_RUNTIME_DEFERRED_CANDIDATE_DECISION_2026-07-01.md`; `docs/reference/CVF_VALUE_PARKED_LANE_REOPEN_DISCIPLINE_STANDARD_2026-06-25.md`; `governance/compat/` |
| Disposition | NOT_APPLICABLE_WITH_REASON: local governance-control dispatch over already-closed KIOD decisions. |
| Claim boundary | No new outside-source intake, absorption, source import, source-mirror mutation, or external-agent output conversion is authorized. |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/reference/CVF_KIOD_RUNTIME_CANDIDATE_REOPEN_CONDITION_INVENTORY_2026-07-02.json` | CREATE source-backed inventory with exactly D-file06 and I-file19 lane records, source authority, required evidence fields, forbidden-until-gate-passes, and claim boundary. |
| `governance/compat/check_kiod_runtime_candidate_reopen_inventory.py` | CREATE checker using the FPC checker pattern, adapted to KIOD runtime candidates and changed-range governed-doc scan behavior. |
| `governance/compat/test_check_kiod_runtime_candidate_reopen_inventory.py` | CREATE focused tests for valid inventory, missing lane, condition drift, empty evidence fields, missing owner artifact, unsupported re-proposal in changed docs, and valid source-backed re-proposal evidence. |
| `governance/compat/agent_autorun_command_catalog.py` | MODIFY to include the KIOD checker in common autorun commands. |
| `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | MODIFY to include the KIOD checker in reviewer-fast. |
| `governance/compat/local_governance_hook_catalog_pre_commit.py` | MODIFY to include the KIOD checker in pre-commit. |
| `governance/compat/local_governance_hook_catalog_pre_push.py` | MODIFY to include the KIOD checker in pre-push. |
| `docs/reviews/CVF_KIOD_R11_RUNTIME_CANDIDATE_REOPEN_INVENTORY_GUARD_WORKER_RETURN_2026-07-02.md` | CREATE worker return with command evidence, no-commit evidence, and any self-repaired defects. |

## Worker Return Packet Shape Contract

Worker return must be created at
`docs/reviews/CVF_KIOD_R11_RUNTIME_CANDIDATE_REOPEN_INVENTORY_GUARD_WORKER_RETURN_2026-07-02.md`
and include:

- `Self-declared worker-return artifact: yes`
- `Responds to work order:`
- `dispatchWorkOrder:`
- `executionBaseHead:`
- `## Purpose`
- `## Scope / Methodology`
- `## Findings / Position`
- `## Risk / Corrective Action`
- `## Checker Source Read-Ahead Block`
- Agent Operation Trace Block heading
- `## Delta Execution Claim Boundary Control Block`
- `## Public Export Disposition`
- External Knowledge Intake Routing heading
- Rescan Intelligence Hardening heading
- Corpus Completeness And Report Integrity heading
- Finding-To-Governance Learning Disposition heading
- Epistemic Process Block heading
- Machine Closure Package heading
- `## Claim Boundary`
- `## git status --short`
- `## Changed Files`
- `## Command Evidence`
- `## No-Commit Statement`

The no-commit statement must include `WORKER_MUST_NOT_COMMIT honored`. For
non-applicable conditional blocks, use `N/A with reason` or
`NOT_APPLICABLE_WITH_REASON`.

## Inventory And Checker Required Shape

Inventory required fields:

- top-level `schemaVersion`, `inventoryId`, `status`, `date`, `docType`,
  `sourceAuthority`, `inventoryBoundary`, `requiredCandidateIds`,
  `candidateInventories`, `checkerCandidate`, `publicExportDisposition`, and
  `claimBoundary`;
- `requiredCandidateIds` exactly `D-file06` and `I-file19`;
- each candidate record includes `candidateId`, `gateStatus`, `conditionText`,
  `owningArtifacts`, `evidenceFields`, `requiredConditions`,
  `forbiddenUntilGatePasses`, and `reproposalRule`;
- every owning artifact path exists;
- boundary flags for runtime/provider/live/public/package/Web/MCP/action
  behavior are false.

Checker required behavior:

- inventory validation must fail missing candidate, duplicate candidate,
  condition drift from KIOD-R10, empty evidence fields, missing owning artifact,
  invalid boundary flags, and missing claim boundary;
- changed governed docs must fail when they propose D-file06/I-file19 runtime
  implementation without evidence tokens such as fresh operator decision,
  fresh GC-018, source verification, and proof plan;
- changed governed docs must pass when they only cite KIOD-R10 closure, list the
  candidates as parked/forbidden, or record no-current-implementation boundary.

## Current Runtime Freshness Verification

| Field | Value |
| --- | --- |
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | NO |
| providerLiveProofAuthorized | NO |
| freshnessVerificationMode | NOT_APPLICABLE_WITH_REASON |
| reason | KIOD-R11 authorizes only local governance inventory/checker/test/wiring work. It does not claim D-file06 or I-file19 runtime behavior exists. |
| requiredFutureAction | Any vector retrieval, memory-index read, Learning Plane runtime, provider/live proof, or external adapter lane requires fresh operator decision, fresh GC-018, source verification, and proof planning. |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| Storage layout action | CREATE_SINGLE_REFERENCE_FILE_WITH_REASON |
| Target path | `docs/reference/CVF_KIOD_RUNTIME_CANDIDATE_REOPEN_CONDITION_INVENTORY_2026-07-02.json` |
| Folder front door | N/A with reason: this work order creates one dated top-level reference JSON, not a new reference family folder. |
| Durable governance boundary | The inventory is a private provenance reference input for a local checker. It is not runtime storage, corpus storage, source mirror storage, public storage, or generated session state. |
| Index update requirement | N/A with reason: no stable reference-family folder or generated aggregate index is created by this work order. |
| Claim boundary | Foundation storage block covers planned reference-file placement only; no runtime storage or public storage claim. |

## Rescan Intelligence Hardening

- Original source artifact: `docs/reviews/CVF_KIOD_R10_RUNTIME_DEFERRED_CANDIDATE_DECISION_2026-07-01.md`; `docs/reviews/CVF_KIOD_R10_RUNTIME_DEFERRED_CANDIDATE_DECISION_WORKER_RETURN_2026-07-01.md`
- Predecessor intake artifact: `docs/reviews/CVF_KIOD_R10_RUNTIME_DEFERRED_CANDIDATE_DECISION_2026-07-01.md`
- Delta ledger status: COMPLETE_WITH_DELTA_ROUTING_SAMPLE
- Routing matrix status: COMPLETE_WITH_DELTA_ROUTING_SAMPLE
- Semantic sampling status: COMPLETE_WITH_DELTA_ROUTING_SAMPLE
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Count | Notes |
| --- | --- | --- |
| UNCHANGED_FROM_INTAKE | 2 | D-file06 and I-file19 remain parked runtime candidates; KIOD-R11 must not change KIOD-R10 reopen-condition semantics. |
| CHANGED_DISPOSITION | 1 | KIOD-R11 changes only the control-plane representation: prose reopen conditions become inventory/checker inputs. |
| NEW_FINDING | 1 | KIOD-R10 worker return identified that future agents should not re-propose D-file06/I-file19 without first checking recorded conditions; KIOD-R11 systemizes that gap. |
| REMOVED_OR_REJECTED | 1 | Runtime implementation, source import, provider/live proof, Web, package, MCP/CLI, and public-sync remain rejected for this tranche. |

### Follow-Up Routing Matrix

| Routing lane | Assigned items | Notes |
| --- | --- | --- |
| DO_NOW | KIOD-specific inventory/checker/test/wiring | execute in KIOD-R11 as local governance-control work |
| SEPARATE_RUNTIME_TRANCHE | D-file06 vector retrieval and I-file19 Learning Plane memory-index read | still parked; reopen only if KIOD-R10 conditions are source-backed in a fresh packet |
| STRATEGIC_OPERATOR_DECISION | whether runtime retrieval or Learning Plane memory-index read is worth future product work | operator decision required; not decided by KIOD-R11 |
| OUT_OF_SCOPE | source import, runtime code, provider/live proof, public-sync, Web, package, MCP/CLI adapter | forbidden by this work order |
| RESOLVED_BY_DESIGN | prose-only reopen conditions exist in KIOD-R10 and session state | KIOD-R11 adds machine-checkable inventory/guard coverage, not new semantics |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| KIOD-R11-S1 | KIOD-R10 reopen table | D-file06 may reopen only after explicit product/integration need and runtime proof plan | inventory candidate row | could inventory wording make vector retrieval look authorized now? | PASS - inventory must set runtime/provider/live/public/package flags false and preserve forbidden-until evidence |
| KIOD-R11-S2 | KIOD-R10 reopen table | I-file19 may reopen only after Learning Plane need, source verification, and non-auto-promotion design | inventory candidate row | could checker wording imply automatic promotion or memory-index read exists? | PASS - checker must block runtime proposal without evidence and must not create runtime behavior |
| KIOD-R11-S3 | KIOD-R10 worker return | future agents should not re-propose candidates without checking conditions | changed-doc detection | could ordinary closure references false-positive as re-proposal? | PASS - focused tests must allow parked/forbidden/closure-only references |
| KIOD-R11-S4 | FPC parked-reopen checker precedent | inventory/checker pattern exists for parked lanes | KIOD adaptation | could worker broaden FPC semantics or global parked lanes? | PASS - Allowed Scope forbids FPC semantic changes and requires a KIOD-specific checker |

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - KIOD-R11 is not a bounded-corpus
  scan; it creates a two-candidate governance inventory from KIOD-R10 closure
  evidence and does not enumerate or process a new source corpus.

## Execution Plan

| Step | Action | Evidence |
| --- | --- | --- |
| 1 | Capture executionBaseHead and worktree status before edits. | `git rev-parse --short HEAD`; `git status --short` |
| 2 | Read required sources and checker source before writing. | Source Inventory and Checker Source Read-Ahead Block in worker return |
| 3 | Create the KIOD runtime-candidate reopen inventory JSON. | Inventory file plus checker validation |
| 4 | Implement checker by adapting FPC checker pattern without altering FPC semantics. | New checker file and focused tests |
| 5 | Add focused tests covering valid inventory, drift, missing records, and changed-doc re-proposal evidence. | unittest output |
| 6 | Wire checker into autorun, reviewer-fast, pre-commit, and pre-push catalogs. | Catalog diff and gate output |
| 7 | Run required focused tests and gates. | Command Evidence |
| 8 | Create worker return and leave all changes uncommitted. | `git status --short`; no-commit statement |

## Evidence Requirements

Worker return must include:

- exact executionBaseHead and initial `git status --short`;
- source reads for KIOD-R10 decision packet, KIOD-R10 worker return,
  value-parked standard, FPC inventory/checker/tests, and catalog wiring;
- inventory validation evidence;
- focused unittest evidence;
- direct checker evidence;
- worker-return fast gate evidence;
- pre-implementation autorun evidence;
- git diff name-status showing only allowed-scope files;
- explicit confirmation that no runtime, provider/live proof, source import,
  public-sync, session-state, handoff, package, Web, MCP/CLI, model-router,
  action-authority, automatic-invocation, or production path was touched.

## Acceptance Criteria

| ID | Criterion | Required evidence |
| --- | --- | --- |
| AC1 | Inventory contains exactly `D-file06` and `I-file19` records and preserves KIOD-R10 reopen-condition semantics. | Inventory file plus checker/test evidence |
| AC2 | Checker validates inventory shape, owning artifacts, required evidence fields, forbidden-until-gate lists, and claim boundary. | Focused tests and direct checker PASS |
| AC3 | Checker detects changed governed docs that re-propose D-file06/I-file19 runtime work without source-backed reopen evidence. | Focused tests |
| AC4 | Checker allows closure-only or parked-boundary references. | Focused tests |
| AC5 | Checker is wired into autorun, reviewer-fast, pre-commit, and pre-push catalogs. | Catalog diff and gate evidence |
| AC6 | Worker return itself passes worker-return quality gate shape and records no-commit evidence. | Worker-return fast gate and no-commit statement |

## Fail Conditions

| Condition | Required response |
| --- | --- |
| Worker needs to change KIOD-R10 decision semantics or loosen reopen conditions. | Return `BLOCKED_WITH_REASON`. |
| Worker needs runtime implementation, provider/live proof, public-sync, Web/UI/dashboard, MCP/CLI adapter behavior, package lifecycle mutation, model-router work, action authority, automatic invocation, or production-readiness work. | Return `BLOCKED_WITH_REASON`. |
| Worker cannot implement changed-doc detection without broad false positives against ordinary closure references. | Narrow the checker inside allowed scope and prove with focused tests, or return `BLOCKED_WITH_REASON`. |
| Worker needs to edit `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF*.md`, external source files, or public-sync clone. | Return `BLOCKED_WITH_REASON`. |

## Review Gate

Reviewer/closer must reject or return the worker output if any of these are
true:

- worker changed files outside Allowed Scope without source-backed reason;
- worker implemented runtime, provider/live, package, Web, public-sync, MCP/CLI,
  model-router, generated aggregate, or session-sync behavior;
- checker changes FPC semantics or KIOD-R10 decision semantics;
- worker return contains unresolved worker-return quality gate violations;
- tests do not cover both false-positive and true-positive changed-doc cases;
- command evidence omits no-commit evidence.

## Closure Checklist

- [x] Dispatch packet includes source verification and dependency-release evidence.
- [x] Dispatch packet includes protected-path authorization.
- [x] Dispatch packet includes Worker Return Packet Shape Contract and reviewer conversion.
- [x] Dispatch packet forbids worker commit and session-sync mutation.
- [ ] Reviewer/closer reviews worker return.
- [ ] Reviewer/closer runs closure gates on the accepted changed set.
- [ ] Reviewer/closer commits material batch if accepted.
- [ ] Reviewer/closer performs session-sync after accepted material commit.

## Operator Checkpoint

Operator checkpoint: worker may proceed under `WORKER_MUST_NOT_COMMIT` using
this dispatch packet. Operator intervention is required only if worker needs to
change KIOD-R10 reopen conditions, exceed Allowed Scope, edit forbidden paths,
run live/provider proof, consume secrets/quota, open public-sync, implement
runtime behavior, implement external adapters, or change risk/claim boundary.

## Verification Commands

Worker must run at minimum:

```powershell
git rev-parse --short HEAD
git status --short
python -m unittest governance.compat.test_check_kiod_runtime_candidate_reopen_inventory -v
python governance/compat/check_kiod_runtime_candidate_reopen_inventory.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_kiod_runtime_candidate_reopen_inventory.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <executionBaseHead> --head HEAD
```

If a listed command is unavailable because the worker has not yet created the
checker, create the checker inside Allowed scope and rerun. If a command fails
inside Allowed scope, repair and rerun; do not ask the operator whether to fix
owned machine-shape failures.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex dispatcher |
| Provider or surface | local workspace |
| Session or invocation | KIOD-R11 runtime-candidate reopen inventory guard dispatch, 2026-07-02 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, Get-Content, scaffold helper stdout, apply_patch, pre-dispatch gates |
| Target paths | this work order; paired KIOD-R11 baseline |
| Allowed scope source | operator said `ok. write work order` after accepting the proposed KIOD-R11 parked-runtime-candidate inventory guard |
| Before status evidence | HEAD `9c7aa4d5`; worktree clean before dispatch authoring |
| After status evidence | pending pre-dispatch verification before material dispatch commit |
| Diff evidence | `git diff --name-status` before dispatch commit |
| Approval boundary | dispatch packet authoring only |
| Claim boundary | no runtime/provider/public/source-import/Web/MCP/model-router/action-authority claim |
| Agent type | dispatcher |
| Invocation ID | `kiod-r11-dispatch-2026-07-02` |
| Expected manifest | paired KIOD-R11 baseline and this work order |
| Actual changed set | to be verified before dispatch commit |
| Manifest delta | TO_VERIFY_BEFORE_COMMIT |
| Deletion or rename disposition | N/A with reason: no deletion or rename in dispatch authoring |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | KIOD-R11 runtime-candidate reopen inventory guard work order |
| claimDisposition | CLAIM_REJECTED: this packet makes no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, or universal governed-coding-control claim. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed by this dispatch. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed by this dispatch. |
| invocationBoundary | Manual local checker/test/hook invocation only after worker implementation. |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized. |
| claimLanguage | Work order for KIOD inventory, local checker/test coverage, and hook/autorun catalog wiring only. |
| forbiddenExpansion | Runtime/provider/live/public/package/Web/MCP/model-router behavior requires fresh source-verified authorization. |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: KIOD-R11 is private provenance governance-control work over internal
KIOD decisions and copied external-source candidate lineage. No public-sync
export is authorized by this work order.

## Claim Boundary

This work order authorizes only KIOD-specific inventory/checker/test/wiring and
one no-commit worker return. It does not reopen D-file06 or I-file19 runtime
implementation, prove provider behavior, export public artifacts, mutate
package lifecycle, create an external adapter, or change session state.
