# CVF Agent Work Order - FPC-SCG-T4 Worker-Return Fast-Gate Epistemic Fixture

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

dispatchBaseHead: 30cedeff

executionBaseHead: 30cedeff

closureBaseHead: 30cedeff

rawMemoryReleased: false

## Dispatch Prompt Envelope

Task: FPC-SCG-T4 Worker-Return Fast-Gate Epistemic Fixture.

Agent: Codex.

Commit mode: WORKER_MAY_COMMIT.

Read first:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V23_2026-06-26.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- this work order

Allowed scope: wire the existing epistemic process packet checker into
`run_worker_return_fast_gate.py`, update focused tests, update FPC guidance,
author the GC-018 baseline, this work order, and completion review.

Forbidden scope: runtime/MCP/CLI/IDE bridge implementation, provider/live
proof, public-sync, registry mutation, DICE runtime expansion, generated
active-session mutation in the material commit, route wiring, downstream
adapter work, Policy_Local, Document Translator, Model Gateway, Sandbox
Runtime, MPI-T6 runtime, package activation, certification decision, and
public/production/readiness claims.

## Purpose

Provide the tactical execution packet for Codex to close FPC-T3-C05 with a
bounded fast-gate fixture that runs the existing epistemic process checker
before reviewer intake.

## 1. Mission

Add the `epistemic process packet` command to the worker-return fast gate before
the reviewer-fast command and add focused unit-test coverage proving the command
order and exact invocation.

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | source-verify scope and author GC-018/work order |
| Implementer | Codex | implement fast-gate wiring and focused test fixture |
| Reviewer / closer | Codex | run gates, write completion review, commit material closure |
| Operator | Human | intervene only if a required source artifact is missing or a forbidden lane is required |

## Required First Reads

| File | Action |
|---|---|
| `CVF_SESSION_MEMORY.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V23_2026-06-26.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |
| `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` | READ |
| `docs/reference/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md` | READ |
| `governance/compat/run_worker_return_fast_gate.py` | READ |
| `governance/compat/check_epistemic_process_packet.py` | READ |
| `governance/compat/test_run_worker_return_fast_gate.py` | READ |

## Pre-Flight Checks

| Check | Command |
|---|---|
| Current base | `git rev-parse --short HEAD` |
| FPC-T3-C05 source search | `rg -n "FPC-T3-C05|worker-return fast-gate|epistemic process packet|run_worker_return_fast_gate" docs/reference governance/compat` |
| Focused tests | `python -m pytest governance/compat/test_run_worker_return_fast_gate.py governance/compat/test_check_epistemic_process_packet.py -q` |
| Worktree | `git status --short` |

## 2. Authority Chain

- Operator instruction: 2026-06-27, continue according to next move.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V23_2026-06-26.md`.
- Routing guidance: `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md`.
- GC-018 baseline: `docs/baselines/CVF_GC018_FPC_SCG_T4_WORKER_RETURN_FAST_GATE_EPISTEMIC_FIXTURE_2026-06-27.md`.

## Agent Handoff Contract Control Block

| Field | Value |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | Codex owns dispatch authoring, implementation, review, closure, and any later session-sync |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=30cedeff`; `executionBaseHead=30cedeff`; `closureBaseHead=30cedeff` |
| changedSetScope(phase) | material phase changes only the fast-gate source, focused test, FPC guidance, GC-018 baseline, work order, and completion review; session-sync is a separate follow-up commit if required |
| traceScope(phase, actor) | Codex records AOT evidence in the work order, completion review, and changed guidance reference |
| commitOwner(phase) | Codex owns the material commit and any separate session-sync commit |
| crossBatchIsolation | no public-sync, runtime, provider, generated-state, route, downstream adapter, registry, or MPI-T6 batch may be merged into this material commit |
| nextMoveSurfaces | update only in a separate session-sync pass after material closure if gates pass |
| Before status evidence | `git rev-parse --short HEAD` = `30cedeff`; worktree inspected before edit |
| Closer designation | Codex is the designated closer |

## Worker Autonomy / No-Question Rule

Codex must repair allowed-scope gate failures and rerun gates without asking the
operator. Codex must stop only if a required source artifact is missing, a gate
failure points outside authorized scope, or implementing C05 requires runtime,
provider, registry, public-sync, generated-state, or downstream use-case work
outside this work order.

## Write Ownership

Codex may create or edit only the allowed paths listed below. Runtime, route,
provider, generated-state, public-sync, registry, adapter, external app tree,
and downstream use-case paths are outside write ownership for this tranche.

## Core Guard Self-Protection Authorization

This work order intentionally modifies governance guard surfaces.

Authorized guard-maintenance scope: add one explicit read-only epistemic packet
command to the worker-return fast gate and update the focused fast-gate test
fixture.

Protected paths:

- `governance/compat/run_worker_return_fast_gate.py`
- `governance/compat/test_run_worker_return_fast_gate.py`

Operator authorization: the operator approved continuing according to the next
move on 2026-06-27 after FPC-SCG-T3 closed and FPC-T3-C05 became the next P1
machine-check coverage gap.

Rollback boundary: if FPC-SCG-T4 is rejected, revert only the fast-gate command
addition, focused test update, FPC-SCG-T4 artifacts, and C05 guidance update.
Do not revert FPC-SCG-T3 material commit `2cff8570` or session-sync commit
`30cedeff`.

Authorization boundary: read-only fast-gate wiring and focused tests only. No
destructive command, runtime mutation, provider call, external app tree access,
registry edit, generated active-session mutation, downstream adapter work, or
public-sync is authorized.

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| Foundation files touched | existing `governance/compat/` fast-gate source and test; dated GC-018/work-order/review execution artifacts; current FPC guidance |
| Storage class | governance compatibility fast gate plus dated execution evidence |
| Index/front door | fast-gate command is discoverable through `run_worker_return_fast_gate.py`; no new reference folder is created |
| Date policy | execution artifacts carry tranche date; source edits remain undated code |
| Archive disposition | N/A with reason: no file is archived, split, relocated, or renamed in this tranche |
| Deferred layout work | N/A with reason: this tranche wires an existing checker into an existing fast gate |

## Roadmap-to-Work-Order Trace Matrix

| Routing requirement | Work-order instruction | Closure evidence |
|---|---|---|
| P1 machine-check coverage after C02 closure | Implement FPC-T3-C05 fast-gate fixture | focused tests and completion review |
| Preserve epistemic process enforcement | Invoke existing `check_epistemic_process_packet.py --enforce` directly in the worker-return fast gate | command sequence unit test |
| Fail before reviewer intake | Place the epistemic command before reviewer-fast | command order unit test |
| Avoid runtime/provider/registry expansion | Modify only fast-gate source, focused test, guidance, and execution artifacts | closure diff gate |
| Keep P2 lanes parked | Forbidden scope and next-move update | completion review |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| FPC-T3-C05 is the recommended next P1 machine-check candidate | `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` | `Recommended next work order candidate` | `FPC-SCG-T4 Worker-Return Fast-Gate Epistemic Fixture` | foundation-plane guidance | ACCEPT |
| C05 is worker-return fast-gate epistemic fixture | `docs/reference/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md` | `### FPC-T3-C05: Worker-Return Fast Gate Epistemic Fixture` | `FPC-T3-C05` | FPC-T3 coverage plan | ACCEPT |
| C05 value depends on existing C01 checker | `docs/reference/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md` | `### FPC-T3-C05: Worker-Return Fast Gate Epistemic Fixture` | `check_epistemic_process_packet.py` | FPC-T3 coverage plan | ACCEPT |
| Worker-return fast gate constructs command sequence | `governance/compat/run_worker_return_fast_gate.py` | function definition | `build_commands` | worker-return fast gate | ACCEPT |
| Epistemic checker has enforceable CLI | `governance/compat/check_epistemic_process_packet.py` | function definition | `main` | epistemic process packet checker | ACCEPT |
| Epistemic checker includes uncommitted changed-path detection | `governance/compat/check_epistemic_process_packet.py` | function definition | `get_changed_paths` | epistemic process packet checker | ACCEPT |
| Reviewer-fast already wires the epistemic checker | `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | `REVIEWER_FAST_CHECKS` | `epistemic process packet` | reviewer-fast hook catalog | ACCEPT |
| Focused fast-gate tests cover default command sequence | `governance/compat/test_run_worker_return_fast_gate.py` | test method | `test_default_commands_include_reviewer_fast_and_registry_drift` | worker-return fast-gate tests | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class work-order-authoring --role dispatcher --phase pre-dispatch --json`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0006, ADIF-0007

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | `governance/compat/run_worker_return_fast_gate.py`; `governance/compat/test_run_worker_return_fast_gate.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/local_governance_hook_catalog_reviewer_fast.py` |
| Runtime behavior claimed | N/A_WITH_REASON: no product runtime, provider route, Web route, CLI/MCP adapter, OCR/provider call, retrieval behavior, downstream adapter behavior, or registry behavior is changed |
| Helper/checker implementation claimed | PASS: existing fast gate now invokes the existing epistemic checker explicitly |
| Provider/live proof claimed | N/A_WITH_REASON |
| Provider registry surfaces | PASS: current provider registry surfaces `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and `PROVIDER_CAPABILITY_REGISTRY` are not changed; no provider-selection, provider-routing, provider-registry, or live-governance claim is made |
| Public-sync claimed | N/A_WITH_REASON |
| Freshness disposition | PASS - checker-only FPC-T3-C05 coverage |

## 3. Allowed Paths

- `governance/compat/run_worker_return_fast_gate.py`
- `governance/compat/test_run_worker_return_fast_gate.py`
- `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md`
- `docs/baselines/CVF_GC018_FPC_SCG_T4_WORKER_RETURN_FAST_GATE_EPISTEMIC_FIXTURE_2026-06-27.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_SCG_T4_WORKER_RETURN_FAST_GATE_EPISTEMIC_FIXTURE_FOR_CODEX_2026-06-27.md`
- `docs/reviews/CVF_FPC_SCG_T4_WORKER_RETURN_FAST_GATE_EPISTEMIC_FIXTURE_COMPLETION_2026-06-27.md`

## Execution Plan

1. Add the existing epistemic process checker command to `build_commands()`.
2. Place the command after corpus registry drift and before reviewer-fast.
3. Update focused tests for default command order and exact checker invocation.
4. Update FPC guidance to mark C05 closed bounded and route next P1 work to
   C03 expected-chain manifest source verification.
5. Run focused tests and governance gates before commit.

## 4. Required Implementation

1. Edit `governance/compat/run_worker_return_fast_gate.py`.
2. Edit `governance/compat/test_run_worker_return_fast_gate.py`.
3. Update `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md`.
4. Add the FPC-SCG-T4 GC-018 baseline.
5. Add this work order and the completion review.

## 5. Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Focused fast-gate and epistemic checker tests pass. |
| AC2 | `run_worker_return_fast_gate.py` includes an `epistemic process packet` command invoking `check_epistemic_process_packet.py --enforce`. |
| AC3 | The epistemic command runs before reviewer-fast. |
| AC4 | Worker-return fast gate runs the new step and reports it before reviewer-fast. |
| AC5 | Completion review records no runtime/provider/public/registry/generated-state/use-case/MPI-T6 mutation in the material commit. |

## 6. Verification Commands

```powershell
python -m pytest governance/compat/test_run_worker_return_fast_gate.py governance/compat/test_check_epistemic_process_packet.py -q
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_run_worker_return_fast_gate.py
python governance/compat/check_work_order_dispatch_quality.py --base 30cedeff --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 30cedeff --head HEAD
git diff --check
git status --short
```

## Evidence Requirements

| Evidence | Required form |
|---|---|
| Focused tests | pytest output |
| Fast-gate behavior | CLI output from `run_worker_return_fast_gate.py` |
| Command order | focused unit-test assertion |
| Changed set | `git diff --name-status` and `git status --short` |
| Boundary proof | completion review Closure Diff Gate |

## Review Gate

Codex must not commit until focused tests, worker-return fast gate, dispatch
quality, markdown structural completeness, agent operation trace, public export
disposition, core guard self-protection, and pre-closure gates pass or are
explicitly blocked with a return-to-orchestrator reason.

## Return-To-Orchestrator Conditions

Return to orchestrator only if source verification shows FPC-T3-C05 cannot be
closed without runtime expansion, provider behavior, registry mutation,
generated-state mutation, public-sync, if a required source file is missing, or
if a required gate fails on a path outside the authorized scope.

## Operator Checkpoint

Operator checkpoint: none required before material closure. Post-closure next
move should remain in P1 and source-verify FPC-T3-C03 expected-chain manifest
coverage unless the operator selects another foundation-gap tranche.

## Closure Checklist

- [x] GC-018 baseline exists.
- [x] Work order exists.
- [x] Fast-gate implementation exists.
- [x] Focused fast-gate tests exist and pass.
- [x] Worker-return fast gate runs the epistemic packet step.
- [x] Guidance records C05 as closed bounded.
- [x] Completion review exists.
- [x] Runtime/provider/public/registry/use-case/MPI-T6 lanes remain parked.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| GC-018 status | `docs/baselines/CVF_GC018_FPC_SCG_T4_WORKER_RETURN_FAST_GATE_EPISTEMIC_FIXTURE_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_FPC_SCG_T4_WORKER_RETURN_FAST_GATE_EPISTEMIC_FIXTURE_COMPLETION_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` | P1 guidance updated; no roadmap file changed | PASS |
| Fast gate source | `governance/compat/run_worker_return_fast_gate.py` | explicit epistemic process packet command added | PASS |
| Focused fast-gate tests | `governance/compat/test_run_worker_return_fast_gate.py` | pytest pass | PASS |
| Epistemic checker source | `governance/compat/check_epistemic_process_packet.py` | existing checker invoked by fast gate | PASS |
| Registry JSON | BLOCKED with reason: FPC-SCG-T4 is checker wiring only and does not edit GC-052 registry JSON | N/A | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown companion is edited in this tranche | N/A | BLOCKED with reason |
| System loop interlock | `governance/compat/check_system_loop_interlock.py` | registry checker remains pass with no registry edit | PASS |
| External evidence digest | N/A with reason: no external evidence or provider proof used | N/A | N/A with reason |
| Session continuity | reviewer-owned post-material sync | pending separate session-sync after material commit | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Fast gate command present | `epistemic process packet` | added to `build_commands` | PASS |
| Fast gate command invokes checker | `python governance/compat/check_epistemic_process_packet.py --enforce` | focused unit test asserts exact tuple | PASS |
| Command order | epistemic command before reviewer-fast | focused unit test asserts order | PASS |
| Focused tests pass | `18 passed` | `test_run_worker_return_fast_gate.py` and `test_check_epistemic_process_packet.py` pass | PASS |
| Runtime mutation | none | no runtime source path changed | PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local repository tools |
| Session or invocation | 2026-06-27 FPC-SCG-T4 worker-return fast-gate epistemic fixture |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, pytest, governance gates |
| Target paths | `governance/compat/run_worker_return_fast_gate.py`; `governance/compat/test_run_worker_return_fast_gate.py`; `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md`; `docs/baselines/CVF_GC018_FPC_SCG_T4_WORKER_RETURN_FAST_GATE_EPISTEMIC_FIXTURE_2026-06-27.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_SCG_T4_WORKER_RETURN_FAST_GATE_EPISTEMIC_FIXTURE_FOR_CODEX_2026-06-27.md`; `docs/reviews/CVF_FPC_SCG_T4_WORKER_RETURN_FAST_GATE_EPISTEMIC_FIXTURE_COMPLETION_2026-06-27.md` |
| Allowed scope source | operator next-move instruction; active session state; FPC guidance; GC-018 baseline; this work order |
| Before status evidence | `git rev-parse --short HEAD` = `30cedeff` |
| After status evidence | focused tests and gates run before commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | bounded FPC-T3-C05 fast-gate fixture implementation only |
| Claim boundary | static worker-return fast-gate visibility only; no runtime/provider/public/registry/use-case/MPI-T6 readiness claim |
| Agent type | Codex single-agent dispatcher/implementer/reviewer |
| Invocation ID | `fpc-scg-t4-worker-return-fast-gate-epistemic-fixture-2026-06-27` |
| Expected manifest | `governance/compat/run_worker_return_fast_gate.py`; `governance/compat/test_run_worker_return_fast_gate.py`; `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md`; `docs/baselines/CVF_GC018_FPC_SCG_T4_WORKER_RETURN_FAST_GATE_EPISTEMIC_FIXTURE_2026-06-27.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_SCG_T4_WORKER_RETURN_FAST_GATE_EPISTEMIC_FIXTURE_FOR_CODEX_2026-06-27.md`; `docs/reviews/CVF_FPC_SCG_T4_WORKER_RETURN_FAST_GATE_EPISTEMIC_FIXTURE_COMPLETION_2026-06-27.md` |
| Actual changed set | `governance/compat/run_worker_return_fast_gate.py`; `governance/compat/test_run_worker_return_fast_gate.py`; `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md`; `docs/baselines/CVF_GC018_FPC_SCG_T4_WORKER_RETURN_FAST_GATE_EPISTEMIC_FIXTURE_2026-06-27.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_SCG_T4_WORKER_RETURN_FAST_GATE_EPISTEMIC_FIXTURE_FOR_CODEX_2026-06-27.md`; `docs/reviews/CVF_FPC_SCG_T4_WORKER_RETURN_FAST_GATE_EPISTEMIC_FIXTURE_COMPLETION_2026-06-27.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance machine-check tranche. Public-sync is not authorized.

## Claim Boundary

This work order authorizes worker-return fast-gate visibility for an existing
epistemic checker only. It does not modify or prove runtime/provider behavior,
route behavior, retrieval behavior, registry behavior, public readiness,
production readiness, or MPI-T6 runtime value.
