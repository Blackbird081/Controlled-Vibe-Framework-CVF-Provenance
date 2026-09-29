# CVF Agent Work Order - WOAS-R5 Scaffold-First Dispatch Quality Gate

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: WOAS-R5

Dispatch base head: `048816a0`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated worker role

Reviewer/closer: reviewer/closer role

Worker return path: `docs/reviews/CVF_WOAS_R5_SCAFFOLD_FIRST_DISPATCH_QUALITY_GATE_WORKER_RETURN_2026-07-01.md`

## Dispatch Prompt Envelope

Role: delegated worker for WOAS-R5.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_WOAS_R5_SCAFFOLD_FIRST_DISPATCH_QUALITY_GATE_2026-07-01.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-01; dispatch base head is `048816a0`.

Do-not-misread notes: this packet authorizes only scaffold provenance standard/helper/checker/test/catalog wiring for dispatch artifact quality. It does not authorize runtime/provider/live proof, real outside-source intake, public-sync, Web/UI/dashboard, MCP/CLI adapter behavior, package lifecycle mutation, model-router work, action authority, automatic invocation, or production-readiness claims.

Required first actions: read required startup files, guard orientation, literal-format gotchas, this packet, the paired GC-018 baseline, the WOAS-R4 worker-return quality gate standard, the scaffold helper source, and every checker source listed in the Checker Source Read-Ahead Block before writing any artifact.

Return contract: create the worker return artifact at `docs/reviews/CVF_WOAS_R5_SCAFFOLD_FIRST_DISPATCH_QUALITY_GATE_WORKER_RETURN_2026-07-01.md`, run required gates, leave changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Implement a scaffold-first dispatch quality control so future GC-018 baselines
and work orders carry explicit scaffold provenance before they are sent to a
worker. The output should reduce work-order authoring latency and improve
worker output quality by making generated scaffold origin, manual edits,
checker read-ahead, and doc-only field declarations visible to both worker and
reviewer before implementation begins.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id WOAS-R5 --title "Scaffold-First Dispatch Quality Gate" --date 2026-07-01 --base 048816a0 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | protected-governance-path plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Filled authority chain, allowed scope, source verification, Core Guard authorization, acceptance criteria, fail conditions, verification commands, worker-return path, and claim boundaries; removed all unresolved placeholder fields. |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| docOnlyNewFields | `Scaffold Provenance Block`; `scaffoldHelperCommand`; `generatedProfile`; `generatedSkeletonStatus`; `manualEditsAfterScaffold`; `checkerReadAheadConfirmation`; `docOnlyNewFields` |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Authority Chain

| Authority | Evidence |
| --- | --- |
| Operator instruction | Operator approved R5 after WOAS-R4 and asked to test whether Claude executes better with stronger work-order scaffolding. |
| Active session front door | `CVF_SESSION_MEMORY.md` current mode allows selection of the next governed lane after material commit `e6a56718`. |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_WOAS_R5_SCAFFOLD_FIRST_DISPATCH_QUALITY_GATE_2026-07-01.md` |
| Work-order template | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` |
| WOAS-R4 quality gate standard | `docs/reference/work_order_authoring/CVF_WORKER_RETURN_QUALITY_GATE_STANDARD.md` |
| Active handoff | `AGENT_HANDOFF_V30_2026-07-01.md` |

## Agent Roles

| Role | Responsibility |
| --- | --- |
| dispatcher | Author this GC-018/work-order pair and run pre-dispatch gates. |
| worker | Execute only the allowed scaffold/checker/test/catalog scope and create the worker return without committing. |
| reviewer/closer | Review worker return, repair only allowed-scope closure defects if needed, and own material commit if accepted. |
| session-sync steward | Update active state and handoff only if reviewer/closer creates an accepted material commit. |

## Required First Reads

| Path | Required action |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V30_2026-07-01.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |
| `docs/reference/work_order_authoring/CVF_WORKER_RETURN_QUALITY_GATE_STANDARD.md` | READ |
| `governance/compat/build_dispatch_packet_scaffold.py` | SOURCE_VERIFIED |
| `governance/compat/check_work_order_dispatch_quality.py` | SOURCE_VERIFIED |
| `governance/compat/check_worker_return_quality_gate.py` | SOURCE_VERIFIED |
| Applicable checker files listed in this packet's Checker Source Read-Ahead Block | READ |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly by reading the
failing checker source and matching the literal required shape. Worker should
return to orchestrator only for a source contradiction, forbidden-scope need,
or missing authority that makes completion impossible.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order-authoring-scaffold`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "work-order-authoring-scaffold" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | No ADIF entries were returned for this exact query; worker must still record any new repeated non-obvious defect pattern in ADIF before closure if one is found. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | `## Dispatch Prompt Envelope`; `Role:`; `Canonical packet:`; `Commit mode:`; `executionBaseHead`; `Return contract:`; `## Checker Source Read-Ahead Block`; `applicableCheckersRead`; `literalTokensReviewed`; `gateRunPurpose`; `claimBoundary`; `Source Verification Block`; `Claimed item`; `Source file`; `Verified line/section`; `Verified path or symbol`; `Owning interface/function/schema`; `Disposition`; `Agent Handoff Contract Control Block`; `Reviewer Closure Conversion`; `Core Guard Self-Protection Authorization`; `WORKER_MUST_NOT_COMMIT`; `## Delta Execution Claim Boundary Control Block`; `CLAIM_REJECTED`; `CLAIM_REJECTED_NO_RECEIPT`; `CLAIM_REJECTED_NO_ACTION`; `## Public Export Disposition`; `DEFERRED_PRIVATE_ONLY`; `Agent Operation Trace Block`; `Scaffold Provenance Block`; `scaffoldHelperCommand`; `manualEditsAfterScaffold`; `WORKER_MUST_NOT_COMMIT honored` |
| gateRunPurpose | Confirmation evidence, not first discovery; checker source and literal tokens were read before this work order was authored. |
| claimBoundary | Read-ahead evidence for this dispatch packet only; worker must repeat read-ahead for its own changed artifacts before implementation. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Active session permits another bounded work-order-authoring scaffold hardening tranche following WOAS-R4 material commit `e6a56718`. | EXISTS | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `nextAllowedMove` | `nextAllowedMove` | active session bootstrap read model | ACCEPT |
| Dispatch scaffold helper owns trigger-family and scaffold argument generation. | EXISTS | `governance/compat/build_dispatch_packet_scaffold.py` | line 49 and line 134 | `TRIGGER_FAMILIES`; `ScaffoldArgs` | dispatch scaffold helper | ACCEPT |
| Dispatch scaffold helper owns baseline and work-order text generation. | EXISTS | `governance/compat/build_dispatch_packet_scaffold.py` | line 519 and line 591 | `build_gc018_baseline`; `build_work_order` | dispatch scaffold helper | ACCEPT |
| Worker-return skeleton helper emits self-declaration and work-order response markers. | EXISTS | `governance/compat/build_worker_return_skeleton_scaffold.py` | line 9 and lines 21-22 | `build_worker_return_skeleton`; `work_order_path` | worker-return skeleton helper | ACCEPT |
| Worker-return fast gate command list includes the worker-return quality gate before reviewer-fast. | EXISTS | `governance/compat/run_worker_return_fast_gate.py` | line 30 and lines 50-51 | `build_commands`; `worker-return quality gate` | worker-return fast gate | ACCEPT |
| Dispatch prompt envelope checker requires exact envelope fields near the top of dispatch-ready work orders. | EXISTS | `governance/compat/check_dispatch_prompt_envelope.py` | lines 38 and 59 | `ENVELOPE_SECTION_MARKER`; `REQUIRED_FIELDS` | dispatch prompt envelope checker | ACCEPT |
| Checker read-ahead guard requires machine-shaped checker source read-ahead fields. | EXISTS | `governance/compat/check_governed_artifact_checker_read_ahead.py` | lines 22-23 | `REQUIRED_HEADING`; `REQUIRED_FIELDS` | checker read-ahead guard | ACCEPT |
| Core guard treats `governance/compat/*.py` as protected. | EXISTS | `governance/compat/check_core_guard_self_protection.py` | `_is_protected` | `governance/compat/` | core guard self-protection checker | ACCEPT |
| Current repo has no scaffold provenance checker or standard before WOAS-R5. | LITERAL_INVARIANT | `governance/compat/`; `docs/reference/work_order_authoring/`; `docs/baselines/`; `docs/work_orders/`; `docs/reviews/` | negative search before authoring returned no matches | `Scaffold Provenance Block`; `scaffold provenance`; `SCAFFOLD_PROVENANCE` | pre-dispatch negative search | ACCEPT |

## New Doc-Only Fields

| Field | Intended owner | Dispatch disposition |
| --- | --- | --- |
| `Scaffold Provenance Block` | new standard and checker to be created by worker | DOC_ONLY_NEW until worker implementation creates source and tests |
| `scaffoldHelperCommand` | generated dispatch provenance block | DOC_ONLY_NEW until worker implementation creates source and tests |
| `generatedProfile` | generated dispatch provenance block | DOC_ONLY_NEW until worker implementation creates source and tests |
| `generatedSkeletonStatus` | generated dispatch provenance block | DOC_ONLY_NEW until worker implementation creates source and tests |
| `manualEditsAfterScaffold` | generated dispatch provenance block | DOC_ONLY_NEW until worker implementation creates source and tests |
| `checkerReadAheadConfirmation` | generated dispatch provenance block | DOC_ONLY_NEW until worker implementation creates source and tests |
| `docOnlyNewFields` | generated dispatch provenance block | DOC_ONLY_NEW until worker implementation creates source and tests |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Path existence for baseline | `Test-Path docs/baselines/CVF_GC018_WOAS_R5_SCAFFOLD_FIRST_DISPATCH_QUALITY_GATE_2026-07-01.md` returned `False` before authoring | PASS |
| Path existence for work order | `Test-Path docs/work_orders/CVF_AGENT_WORK_ORDER_WOAS_R5_SCAFFOLD_FIRST_DISPATCH_QUALITY_GATE_2026-07-01.md` returned `False` before authoring | PASS |
| Path existence for planned worker return | `Test-Path docs/reviews/CVF_WOAS_R5_SCAFFOLD_FIRST_DISPATCH_QUALITY_GATE_WORKER_RETURN_2026-07-01.md` returned `False` before authoring | PASS |
| Token collision search | `rg -n "WOAS_R5_SCAFFOLD_FIRST|WOAS-R5 Scaffold-First|woas_r5_scaffold_first|CVF_WOAS_R5" docs/baselines docs/work_orders docs/reviews docs/reference/work_order_authoring governance/compat CVF_SESSION_MEMORY.md AGENT_HANDOFF_V30_2026-07-01.md` returned no matches before authoring | PASS |
| Scaffold provenance negative search | `rg -n "Scaffold Provenance Block|scaffold provenance|SCAFFOLD_PROVENANCE" governance/compat docs/reference/work_order_authoring docs/baselines docs/work_orders docs/reviews` returned no matches before authoring | PASS |
| Collision decision | No existing WOAS-R5 packet, worker return, scaffold provenance standard, or scaffold provenance checker was found. | PASS |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| WOAS-R1 dispatch scaffold foundation | Material commit `fb6a0ae9`; helper and standard exist. | R5 may extend scaffold authoring because the helper foundation is closed and current. | SATISFIED |
| WOAS-R3 worker-return skeleton scaffold | Material commit `38765baf`; generated worker-return skeleton exists. | R5 may rely on worker-return skeleton fields and must preserve them. | SATISFIED |
| WOAS-R4 worker-return quality gate | Material commit `e6a56718`; worker-return quality gate is wired into worker-return fast gate and local hooks. | R5 may add the analogous dispatch-input quality gate following material commit `e6a56718`. | SATISFIED |
| Current active mode | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` records lane selection after material commit `e6a56718`. | Dispatch may proceed only as bounded scaffold/checker hardening with no runtime/provider/public expansion. | SATISFIED |

## Commit Mode And Base-Anchor Lifecycle

| Field | Value |
| --- | --- |
| dispatchBaseHead | `048816a0` |
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
| baseHeadFor(phase) | dispatchBaseHead=`048816a0`; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | Worker may change only the Allowed scope paths listed in this work order. |
| traceScope(phase, actor) | Worker return must include Agent Operation Trace Block with expected manifest, actual changed set, and manifest delta. |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer owns any material commit if the worker return is accepted. |
| crossBatchIsolation | WOAS-R5 only; no KIOD, Web, package, public-sync, MCP/CLI, runtime/provider, model-router, or session-sync work. |
| nextMoveSurfaces | Worker must not update next-move surfaces; reviewer/closer owns session-sync if closure is accepted. |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_WOAS_R5_SCAFFOLD_FIRST_DISPATCH_QUALITY_GATE_COMPLETION_2026-07-01.md` optional; prefer repairing evidence in the worker return unless a separate completion review is needed for checker shape. |
| reviewerOwnedClosurePaths | `docs/baselines/CVF_GC018_WOAS_R5_SCAFFOLD_FIRST_DISPATCH_QUALITY_GATE_2026-07-01.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_WOAS_R5_SCAFFOLD_FIRST_DISPATCH_QUALITY_GATE_2026-07-01.md`; optional completion review path above |
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

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| Intake summary | Operator request: continue from WOAS-R4 into a tranche that tests whether stronger dispatch scaffolding improves delegated worker quality. |
| Scope classification | Bounded allowed scope: one new standard, helper output update, one new checker, focused tests, local hook/catalog wiring, and one worker return. |
| Risk sensitivity | Medium governance-shape risk because protected `governance/compat/` paths and blocking gate wiring are authorized; public-sync, provider, live, secret, production, and readiness claims are forbidden. |
| Selected role route | routeMode=`SINGLE_AGENT_SINGLE_ROLE`; one worker executes, then reviewer/closer converts if accepted. |
| Role separation basis | Worker must not commit; reviewer/closer owns review, material commit, and any session-sync. |
| Escalation condition | Escalate with `BLOCKED_WITH_REASON` for forbidden scope, missing authority, source contradiction, or gate failure outside allowed-scope repair. |

## Allowed Scope

Allowed scope:

- `docs/reference/work_order_authoring/CVF_DISPATCH_SCAFFOLD_PROVENANCE_STANDARD.md`
- `governance/compat/build_dispatch_packet_scaffold.py`
- `governance/compat/test_build_dispatch_packet_scaffold.py`
- `governance/compat/check_dispatch_scaffold_provenance.py`
- `governance/compat/test_check_dispatch_scaffold_provenance.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_pre_push.py`
- `governance/compat/agent_autorun_command_catalog.py`
- `docs/reviews/CVF_WOAS_R5_SCAFFOLD_FIRST_DISPATCH_QUALITY_GATE_WORKER_RETURN_2026-07-01.md`

Reviewer-owned closure paths:

- `docs/baselines/CVF_GC018_WOAS_R5_SCAFFOLD_FIRST_DISPATCH_QUALITY_GATE_2026-07-01.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_WOAS_R5_SCAFFOLD_FIRST_DISPATCH_QUALITY_GATE_2026-07-01.md`
- `docs/reviews/CVF_WOAS_R5_SCAFFOLD_FIRST_DISPATCH_QUALITY_GATE_COMPLETION_2026-07-01.md`

## Forbidden Scope

Forbidden scope:

- Do not edit `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF_V30_2026-07-01.md`, or archived handoffs.
- Do not perform real outside-source intake, source import, source-mirror mutation, source absorption, or package candidate admission.
- Do not edit Web/UI/dashboard code, MCP/CLI adapter code, package lifecycle state, provider registry, model-router code, or public-sync clone.
- Do not make runtime/provider/live-proof, action-authority, automatic-invocation, public-readiness, or production-readiness claims.
- Do not broaden the checker to old archived docs, completion reviews, or unchanged historical dispatch artifacts.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add a scaffold provenance checker, helper
output support, focused tests, and local gate wiring for dispatch artifact
quality only.

Protected paths:

- `governance/compat/build_dispatch_packet_scaffold.py`
- `governance/compat/test_build_dispatch_packet_scaffold.py`
- `governance/compat/check_dispatch_scaffold_provenance.py`
- `governance/compat/test_check_dispatch_scaffold_provenance.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_pre_push.py`
- `governance/compat/agent_autorun_command_catalog.py`

Operator authorization: current operator instruction selected R5 following
material commit `e6a56718` to reduce work-order latency and improve worker
output quality.

Rollback boundary: reviewer/closer may reject the uncommitted worker return; no
protected-path change is committed unless reviewer accepts the WOAS-R5 material
batch.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/reference/work_order_authoring/CVF_DISPATCH_SCAFFOLD_PROVENANCE_STANDARD.md` | Add new standard defining required fields, eligibility, claim boundary, and false-positive exclusions. |
| `governance/compat/build_dispatch_packet_scaffold.py` | Add generated `Scaffold Provenance Block` to GC-018 and work-order output; preserve existing trigger behavior and worker-return skeleton output. |
| `governance/compat/test_build_dispatch_packet_scaffold.py` | Add focused tests proving helper output includes the block and has no unresolved placeholder values for known fields. |
| `governance/compat/check_dispatch_scaffold_provenance.py` | Add range-aware checker for changed dispatch-ready baselines/work orders. |
| `governance/compat/test_check_dispatch_scaffold_provenance.py` | Add focused checker tests for pass/fail/false-positive cases. |
| `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | Wire checker into reviewer-fast. |
| `governance/compat/local_governance_hook_catalog_pre_commit.py` | Wire checker into pre-commit. |
| `governance/compat/local_governance_hook_catalog_pre_push.py` | Wire checker into pre-push. |
| `governance/compat/agent_autorun_command_catalog.py` | Wire checker into autorun common commands, including pre-dispatch coverage. |
| `docs/reviews/CVF_WOAS_R5_SCAFFOLD_FIRST_DISPATCH_QUALITY_GATE_WORKER_RETURN_2026-07-01.md` | Create worker return with required WOAS-R4 quality-gate sections and command evidence; leave uncommitted. |

## Execution Plan

1. Capture `executionBaseHead` and current worktree status.
2. Read required first-read files and checker source before writing.
3. Add the scaffold provenance standard.
4. Extend scaffold helper output for GC-018 and work-order generation.
5. Add the dedicated range-aware scaffold provenance checker.
6. Add focused helper/checker/catalog tests.
7. Wire checker into reviewer-fast, pre-commit, pre-push, and autorun common commands.
8. Run verification commands and create the no-commit worker return.

## Worker Return Packet Shape Contract

Worker return must be created at
`docs/reviews/CVF_WOAS_R5_SCAFFOLD_FIRST_DISPATCH_QUALITY_GATE_WORKER_RETURN_2026-07-01.md`
and include:

- `Self-declared worker-return artifact: yes`
- `Responds to work order:`
- `dispatchWorkOrder:`
- `executionBaseHead:`
- `Purpose`
- `Scope / Methodology`
- `Findings / Position`
- `Risk / Corrective Action`
- `Checker Source Read-Ahead Block`
- `Agent Operation Trace Block`
- `Delta Execution Claim Boundary Control Block`
- `Public Export Disposition`
- `External Knowledge Intake Routing`
- `Rescan Intelligence Hardening`
- `Corpus Completeness And Report Integrity`
- `Finding-To-Governance Learning Disposition`
- `Epistemic Process Block`
- `Machine Closure Package`
- `git status --short`
- changed files
- command evidence
- no-commit statement

Worker return must not retain `FILL_ME` or
`WORKER_MUST_CAPTURE_AT_START` at `COMPLETE_PENDING_REVIEW`.
Worker return must fill non-applicable conditional sections with
`N/A with reason` or `NOT_APPLICABLE_WITH_REASON`.

## Acceptance Criteria

| ID | Criterion |
| --- | --- |
| AC1 | Standard exists and defines the scaffold provenance fields, eligibility, exclusions, and claim boundary. |
| AC2 | Generated GC-018 and work-order scaffold output includes `Scaffold Provenance Block` with concrete command/profile/status/manual-edit/checker-read-ahead/doc-only-field placeholders and no unresolved values for known fields. |
| AC3 | Checker fails changed dispatch-ready baselines/work orders missing the block, missing required fields, retaining placeholder values, or claiming scaffold provenance without helper command evidence. |
| AC4 | Checker excludes archived docs, completion reviews, worker returns, and quoted/non-dispatch examples. |
| AC5 | Checker is wired into reviewer-fast, pre-commit, pre-push, and autorun common commands. |
| AC6 | Focused tests cover checker pass/fail behavior, helper output inclusion, and catalog wiring. |
| AC7 | Worker return passes WOAS-R4 worker-return quality gate and remains uncommitted. |

## Fail Conditions

| Condition | Required response |
| --- | --- |
| Runtime/provider/live/public/Web/MCP/model-router/package lifecycle work appears necessary. | Return `BLOCKED_WITH_REASON`; new authorization is required. |
| The checker needs to scan or rewrite old archived docs to pass. | Repair eligibility; do not broaden scope. |
| The helper introduces unresolved scaffold placeholders into DISPATCH_READY output. | Repair helper output or return `BLOCKED_WITH_REASON` if impossible in scope. |
| Catalog wiring causes reviewer-fast or pre-commit to fail unrelated historical artifacts. | Narrow checker eligibility and add regression tests. |
| The worker cannot produce a worker return that passes WOAS-R4 quality gate. | Return `BLOCKED_WITH_REASON` with exact checker evidence. |

## Verification Commands

Worker must run at minimum:

```text
python -m unittest governance.compat.test_check_dispatch_scaffold_provenance governance.compat.test_build_dispatch_packet_scaffold governance.compat.test_run_local_governance_hook_chain -v
python governance/compat/check_dispatch_scaffold_provenance.py --base 048816a0 --head HEAD --enforce
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_dispatch_scaffold_provenance.py --pytest-target governance/compat/test_build_dispatch_packet_scaffold.py --pytest-target governance/compat/test_run_local_governance_hook_chain.py
python governance/compat/run_agent_automation_assist.py --base 048816a0 --head HEAD --json --enforce
```

Worker may add direct checker commands when a failure names a more specific
guard. Gate runs are confirmation evidence, not first discovery.

## Evidence Requirements

| Evidence item | Required form |
| --- | --- |
| Execution base | `git rev-parse --short HEAD` recorded in worker return as `executionBaseHead` |
| Changed set | `git status --short` plus `git diff --name-status` in worker return |
| Checker source read-ahead | Worker-return `Checker Source Read-Ahead Block` listing every relevant `governance/compat/check_*.py` file read before implementation |
| Focused tests | command/result rows for helper, checker, and catalog tests |
| Gate proof | worker-return fast gate output with PASS or explicit `BLOCKED_WITH_REASON` |
| No-commit proof | `WORKER_MUST_NOT_COMMIT honored` statement and unchanged HEAD evidence |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| Foundation subject | Dispatch scaffold provenance standard and checker |
| Stable folder | `docs/reference/work_order_authoring/` |
| New reference path | `docs/reference/work_order_authoring/CVF_DISPATCH_SCAFFOLD_PROVENANCE_STANDARD.md` |
| Date policy | Stable reference filename without date suffix; use git history and completion evidence for versioning |
| Folder front door | Existing `docs/reference/work_order_authoring/README.md` remains the family front door |
| Generated aggregate impact | N/A with reason: no generated JSON aggregate is created or edited by this worker tranche |
| Claim boundary | Foundation storage layout only; no runtime/provider/public/Web/MCP/model-router claim |

## Review Gate

Reviewer/closer must verify the worker return against this work order, the
paired GC-018 baseline, and the WOAS-R4 worker-return quality gate before any
material commit. Reviewer may repair only allowed-scope closure defects; scope
expansion returns the packet as `BLOCKED_WITH_REASON`.

## Closure Checklist

| Item | Required closure disposition |
| --- | --- |
| Worker return | `COMPLETE_PENDING_REVIEW` accepted or `BLOCKED_WITH_REASON` retained |
| Commit mode | Worker made no commit; reviewer/closer owns material commit |
| Changed set | Material paths stay inside Allowed Scope or are explicitly rejected |
| Gates | Focused tests, worker-return fast gate, pre-implementation/pre-closure gates pass on real ranges before closure claim |
| Session sync | If accepted, active state/front door/handoff updated in a separate session-sync commit |
| Public export | Remains `DEFERRED_PRIVATE_ONLY` unless a separate public-sync work order exists |

## Operator Checkpoint

No additional checkpoint is needed for allowed-scope implementation or
allowed-scope gate remediation. Return to the operator only for a source
contradiction, forbidden-scope need, credential/live-provider need, public-sync
request, or unresolved `BLOCKED_WITH_REASON`.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` instead of continuing if the worker needs any
forbidden path, cannot source-verify a required current symbol, cannot keep the
checker range-aware, or cannot produce a worker return that passes the WOAS-R4
quality gate.

## Current Runtime Freshness Verification

| Field | Value |
| --- | --- |
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | NOT_APPLICABLE_WITH_REASON |
| reason | WOAS-R5 authorizes dispatch scaffold/checker/test/catalog wiring only. |
| requiredFutureAction | If a later packet adds runtime or provider behavior, create a fresh source-verified work order and live-proof plan. |
| providerRegistryBoundary | N/A with reason: no provider registry mutation or provider routing claim. |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | NOT_APPLICABLE_WITH_REASON: WOAS-R5 does not ingest or classify outside source material. |
| Matching local-view guard | N/A with reason: no outside-source local-view guard is needed for scaffold/checker work. |
| Owner surface | `docs/reference/work_order_authoring/`; `governance/compat/` |
| Disposition | NOT_APPLICABLE_WITH_REASON: local scaffold provenance and checker-hardening tranche only. |
| Claim boundary | No outside-source intake, absorption, source import, source-mirror mutation, or external-agent output conversion is authorized. |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | WOAS-R5 scaffold-first dispatch quality gate work order |
| claimDisposition | CLAIM_REJECTED: this work order makes no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, or universal governed-coding-control claim. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed by this dispatch. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed by this dispatch. |
| invocationBoundary | Manual local helper/checker/test invocation only after worker implementation. |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized. |
| claimLanguage | Dispatch artifact shape, helper scaffolding, and local checker coverage only. |
| forbiddenExpansion | Runtime/provider/live/public/package/Web/MCP/model-router behavior requires fresh source-verified authorization. |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex dispatcher |
| Provider or surface | local workspace |
| Session or invocation | WOAS-R5 scaffold-first dispatch quality gate, 2026-07-01 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | shell, scaffold helper stdout, apply_patch, pre-dispatch gates |
| Target paths | paired GC-018 baseline; this work order |
| Allowed scope source | current operator instruction to create R5 work order after material commit `e6a56718` |
| Before status evidence | HEAD `048816a0`; worktree clean before dispatch authoring |
| After status evidence | pending pre-dispatch verification before material dispatch commit |
| Diff evidence | `git diff --name-status` before dispatch commit |
| Approval boundary | dispatch packet authoring only |
| Claim boundary | no runtime/provider/public/source-import/Web/MCP/model-router claim |
| Agent type | dispatcher |
| Invocation ID | `woas-r5-dispatch-2026-07-01` |
| Expected manifest | paired GC-018 baseline; this work order |
| Actual changed set | to be verified before dispatch commit |
| Manifest delta | TO_VERIFY_BEFORE_COMMIT |
| Deletion or rename disposition | N/A with reason: no deletion or rename planned |

## Claim Boundary

This work order authorizes local scaffold provenance standard/helper/checker/test
and gate-catalog wiring only. It does not authorize real outside-source intake,
source import, source-mirror mutation, runtime/provider/live proof,
public-sync, Web/UI/dashboard, MCP/CLI adapter behavior, package lifecycle
mutation, model-router work, action authority, automatic invocation, or
production-readiness claims.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: WOAS-R5 is private provenance governance-helper work. No public-sync
export is authorized by this work order.
