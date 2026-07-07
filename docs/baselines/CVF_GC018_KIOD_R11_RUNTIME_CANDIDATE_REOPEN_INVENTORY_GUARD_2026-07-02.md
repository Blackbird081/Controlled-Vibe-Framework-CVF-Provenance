# CVF GC-018 Baseline - KIOD-R11 Runtime Candidate Reopen Inventory Guard

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: KIOD-R11

Dispatch base head: `9c7aa4d5`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Operator

Reviewer owner: reviewer/closer role

Worker target: delegated worker role, not a provider-specific role

## Purpose

Authorize one bounded governance-control tranche that turns the KIOD-R10
D-file06 and I-file19 runtime-candidate reopen conditions into a source-backed
inventory plus checker coverage. The worker must create a KIOD-specific reopen
inventory, implement a local checker with focused tests, and wire the checker
into existing governance gate catalogs using the existing FPC parked-reopen
checker pattern as precedent.

This baseline does not authorize vector retrieval, LanceDB, embeddings,
Learning Plane runtime integration, provider/live proof, source import,
public-sync, Web/UI/dashboard work, MCP/CLI adapter behavior, package lifecycle
mutation, model-router work, action authority, automatic invocation, or any
production-readiness claim.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id KIOD-R11 --title "Runtime Candidate Reopen Inventory Guard" --date 2026-07-02 --base 9c7aa4d5 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "KIOD-R10 closed at e89e3dd4 and recorded D-file06 plus I-file19 runtime candidates with concrete reopen conditions" --stdout --include-worker-return-skeleton` |
| generatedProfile | protected-governance-path plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Filled mission, dependency release, source verification, protected-path authorization, fulfillment manifest, dual-agent matrix, acceptance criteria, verification commands, and claim boundaries; removed unresolved scaffold markers from dispatch-ready fields. |
| checkerReadAheadConfirmation | `governance/compat/check_fpc_parked_reopen_inventory.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_agent_operation_trace.py` |
| docOnlyNewFields | `runtimeCandidateId`; `reopenConditionText`; `requiredReopenEvidence`; `forbiddenUntilReopenGatePasses`; `reproposalRule`; `kiodRuntimeCandidateReopenInventory` |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class dispatch --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | No resolver entries were returned for this exact query. Worker must still read the relevant checker source before editing and add ADIF only if a new repeated non-obvious defect pattern is found. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_fpc_parked_reopen_inventory.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `## Scaffold Provenance Block`; `manualEditsAfterScaffold`; `checkerReadAheadConfirmation`; `## Checker Source Read-Ahead Block`; `applicableCheckersRead`; `literalTokensReviewed`; `gateRunPurpose`; `claimBoundary`; `## Source Verification Block`; `Claimed item`; `Source file`; `Verified line/section`; `Verified path or symbol`; `Owning interface/function/schema`; `Disposition`; `Core Guard Self-Protection Authorization`; `Agent Handoff Contract Control Block`; `Reviewer Closure Conversion`; `WORKER_MUST_NOT_COMMIT`; `WORKER_MUST_NOT_COMMIT honored`; `## Delta Execution Claim Boundary Control Block`; `CLAIM_REJECTED`; `CLAIM_REJECTED_NO_RECEIPT`; `CLAIM_REJECTED_NO_ACTION`; `## Public Export Disposition`; `DEFERRED_PRIVATE_ONLY`; `requiredLaneIds`; `laneInventories`; `conditionText`; `requiredConditions`; `forbiddenUntilGatePasses`; `reproposalRule` |
| gateRunPurpose | Confirmation evidence, not first discovery; checker source and literal tokens were read before this baseline was authored. |
| claimBoundary | Read-ahead evidence for this dispatch baseline only; worker must repeat read-ahead for its own changed artifacts before implementation. |

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
| Token collision search | `rg -n "KIOD-R11|Runtime Candidate Reopen Inventory Guard|kiod_runtime_candidate_reopen" docs governance CVF_SESSION AGENT_HANDOFF_V31_2026-07-02.md` found no prior KIOD-R11 artifact before authoring. | PASS |
| Pattern collision decision | Existing FPC-PRG parked-reopen inventory/checker is precedent, not a KIOD owner surface. KIOD-R11 must create a KIOD-specific inventory/checker rather than broadening FPC lanes. | PASS |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| KIOD-R10 material closure | KIOD-R10 decision packet accepted at material commit `e89e3dd4`; session-sync completed at `6f42f4cc`; handoff marker sync completed at `9c7aa4d5`. | KIOD-R11 may systemize the recorded reopen conditions but must not change the KIOD-R10 decision itself. | SATISFIED |
| KIOD-R10 D-file06/I-file19 reopen conditions | `CVF_SESSION_MEMORY.md`, active handoff V31, and KIOD-R10 decision packet record concrete D-file06/I-file19 reopen conditions. | Worker must preserve the same semantic conditions in inventory/checker form. | SATISFIED |
| FPC-PRG precedent | FPC-PRG-T1 through T4 already established an inventory/checker/test/wiring pattern for parked reopen gates. | Worker may adapt the pattern for KIOD runtime candidates only; no FPC behavior change is authorized. | SATISFIED |

## Baseline Decision

Decision: DISPATCH_READY

Proposed tranche: KIOD-R11 Runtime Candidate Reopen Inventory Guard.

Baseline boundary: KIOD-specific inventory/checker/test/wiring only, with
`WORKER_MUST_NOT_COMMIT` and reviewer-owned closure.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | Repo-local governance checker and hook/autorun catalogs under `governance/compat/` | Internal agents receive machine feedback when governed docs attempt to re-propose D-file06/I-file19 without evidence. No runtime or action authority is granted. | This GC-018; paired work order; planned checker/test evidence. | N/A with reason: internal local governance gate only. | CONTRACT_ONLY |
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

## Current Runtime Freshness Verification

| Field | Value |
| --- | --- |
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | NO |
| providerLiveProofAuthorized | NO |
| freshnessVerificationMode | NOT_APPLICABLE_WITH_REASON |
| reason | KIOD-R11 authorizes only local governance inventory/checker/test/wiring work. It does not claim D-file06 or I-file19 runtime behavior exists. |
| requiredFutureAction | Any vector retrieval, memory-index read, Learning Plane runtime, provider/live proof, or external adapter lane requires fresh operator decision, fresh GC-018, source verification, and proof planning. |

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

## Planned Worker Fulfillment Manifest

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

## Acceptance Criteria

| ID | Criterion |
| --- | --- |
| AC1 | Inventory contains exactly `D-file06` and `I-file19` records and preserves the KIOD-R10 reopen-condition semantics. |
| AC2 | Checker validates inventory shape, owning artifacts, required evidence fields, forbidden-until-gate lists, and claim boundary. |
| AC3 | Checker detects changed governed docs that re-propose D-file06/I-file19 runtime work without source-backed reopen evidence. |
| AC4 | Checker allows docs that merely cite KIOD-R10 closure or list the parked candidates as forbidden/parked without proposing implementation. |
| AC5 | Focused tests cover valid and violating cases, including condition drift and missing evidence. |
| AC6 | Checker is wired into autorun, reviewer-fast, pre-commit, and pre-push catalogs using the existing FPC wiring pattern. |
| AC7 | Worker return passes worker-return fast gate and records no-commit evidence. |

## Fail Conditions

| Condition | Required response |
| --- | --- |
| Worker needs to change KIOD-R10 decision semantics or loosen reopen conditions. | Return `BLOCKED_WITH_REASON`; KIOD-R11 may systemize but not revise KIOD-R10. |
| Worker needs runtime implementation, provider/live proof, public-sync, Web/UI/dashboard, MCP/CLI adapter behavior, package lifecycle mutation, model-router work, action authority, automatic invocation, or production-readiness work. | Return `BLOCKED_WITH_REASON`; fresh source-verified authorization is required. |
| Worker cannot implement a checker without broad false positives against ordinary KIOD-R10 closure references. | Return `BLOCKED_WITH_REASON` or narrow the checker inside allowed scope and prove with focused tests. |
| Worker needs to edit `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF*.md`, external source files, or public-sync clone. | Return `BLOCKED_WITH_REASON`; those paths are reviewer/session-sync or separate-lane surfaces. |

## Verification Commands

Worker must run at minimum:

```text
git rev-parse --short HEAD
git status --short
python -m unittest governance.compat.test_check_kiod_runtime_candidate_reopen_inventory -v
python governance/compat/check_kiod_runtime_candidate_reopen_inventory.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_kiod_runtime_candidate_reopen_inventory.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <executionBaseHead> --head HEAD
```

Gate runs are confirmation evidence after checker read-ahead, not first
discovery.

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | KIOD-R11 runtime-candidate reopen inventory guard baseline |
| claimDisposition | CLAIM_REJECTED: this packet makes no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, or universal governed-coding-control claim. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed by this dispatch. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed by this dispatch. |
| invocationBoundary | Manual local checker/test/hook invocation only after worker implementation. |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized. |
| claimLanguage | Dispatch artifact shape, KIOD inventory, local checker/test coverage, and hook/autorun catalog wiring only. |
| forbiddenExpansion | Runtime/provider/live/public/package/Web/MCP/model-router behavior requires fresh source-verified authorization. |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex dispatcher |
| Provider or surface | local workspace |
| Session or invocation | KIOD-R11 runtime-candidate reopen inventory guard dispatch, 2026-07-02 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, Get-Content, scaffold helper stdout, apply_patch, pre-dispatch gates |
| Target paths | this baseline; paired KIOD-R11 work order |
| Allowed scope source | operator said `ok. write work order` after accepting the proposed KIOD-R11 parked-runtime-candidate inventory guard |
| Before status evidence | HEAD `9c7aa4d5`; worktree clean before dispatch authoring |
| After status evidence | pending pre-dispatch verification before material dispatch commit |
| Diff evidence | `git diff --name-status` before dispatch commit |
| Approval boundary | dispatch packet authoring only |
| Claim boundary | no runtime/provider/public/source-import/Web/MCP/model-router/action-authority claim |
| Agent type | dispatcher |
| Invocation ID | `kiod-r11-dispatch-2026-07-02` |
| Expected manifest | this baseline; paired KIOD-R11 work order |
| Actual changed set | to be verified before dispatch commit |
| Manifest delta | TO_VERIFY_BEFORE_COMMIT |
| Deletion or rename disposition | N/A with reason: no deletion or rename in dispatch authoring |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: KIOD-R11 is private provenance governance-control work over internal
KIOD decisions and copied external-source candidate lineage. No public-sync
export is authorized by this dispatch.

## Claim Boundary

This baseline dispatches a bounded KIOD-specific inventory/checker/test/wiring
tranche. It does not reopen D-file06 or I-file19 runtime implementation, prove
provider behavior, export public artifacts, mutate package lifecycle, create an
external adapter, or change session state. Reviewer/closer owns acceptance,
material commit, and session-sync if the worker return is accepted.
