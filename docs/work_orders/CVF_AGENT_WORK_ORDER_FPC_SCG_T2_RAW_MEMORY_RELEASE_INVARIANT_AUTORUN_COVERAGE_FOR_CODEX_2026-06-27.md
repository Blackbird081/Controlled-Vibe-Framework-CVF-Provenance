# CVF Agent Work Order - FPC-SCG-T2 Raw Memory Release Invariant Autorun Coverage

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

dispatchBaseHead: be06a4cb

executionBaseHead: be06a4cb

closureBaseHead: be06a4cb

rawMemoryReleased: false

## Dispatch Prompt Envelope

Task: FPC-SCG-T2 Raw Memory Release Invariant Autorun Coverage.

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

Allowed scope: implement the FPC-T3-C06 raw-memory-release invariant checker,
focused tests, autorun/reviewer-fast catalog wiring, FPC guidance update,
GC-018 baseline, this work order, and completion review.

Forbidden scope: runtime memory behavior changes, provider/live proof,
MCP/CLI route work, durable store mutation, generated active-session mutation
in the material commit, public-sync, downstream adapter work, Policy_Local,
Document Translator, Model Gateway, Sandbox Runtime, MPI-T6 runtime, package
activation, certification decision, and public/production/readiness claims.

## Purpose

Provide the tactical execution packet for Codex to close FPC-T3-C06 with a
bounded read-only static checker and workflow wiring.

## 1. Mission

Implement a governance checker that scans changed governed Markdown and fails
memory-facing artifacts that discuss memory-write, raw-memory, reinjection,
retrieval-facing, or promotion surfaces without an explicit
`rawMemoryReleased=false` or `rawMemoryReleased: false` assertion.

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | source-verify scope and author GC-018/work order |
| Implementer | Codex | implement checker, tests, and command wiring |
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
| `docs/reference/CVF_MEMORY_PLANE_MAP.md` | READ |

## Pre-Flight Checks

| Check | Command |
|---|---|
| Current base | `git rev-parse --short HEAD` |
| FPC-T3-C06 source search | `rg -n "FPC-T3-C06|rawMemoryReleased|check_memory_access_claim" docs/reference governance/compat` |
| Existing runtime invariant search | `rg -n "rawMemoryReleased|canReinject" EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src` |
| Worktree | `git status --short` |

## 2. Authority Chain

- Operator instruction: 2026-06-27, continue according to next move.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V23_2026-06-26.md`.
- Routing guidance: `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md`.
- GC-018 baseline: `docs/baselines/CVF_GC018_FPC_SCG_T2_RAW_MEMORY_RELEASE_INVARIANT_AUTORUN_COVERAGE_2026-06-27.md`.

## Agent Handoff Contract Control Block

| Field | Value |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | Codex owns dispatch authoring, implementation, review, closure, and any later session-sync |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=be06a4cb`; `executionBaseHead=be06a4cb`; `closureBaseHead=be06a4cb` |
| changedSetScope(phase) | material phase changes only the checker, focused test, command catalogs, FPC guidance, GC-018 baseline, work order, and completion review; session-sync is a separate follow-up commit if required |
| traceScope(phase, actor) | Codex records AOT evidence in the work order and completion review |
| commitOwner(phase) | Codex owns the material commit and any separate session-sync commit |
| crossBatchIsolation | no public-sync, runtime, provider, generated-state, durable store, route, or downstream adapter batch may be merged into this material commit |
| nextMoveSurfaces | update only in a separate session-sync pass after material closure if gates pass |
| Before status evidence | `git rev-parse --short HEAD` = `be06a4cb`; worktree inspected before edit |
| Closer designation | Codex is the designated closer |

## Worker Autonomy / No-Question Rule

Codex must repair allowed-scope gate failures and rerun gates without asking the
operator. Codex must stop only if a required source artifact is missing, a gate
failure points outside authorized scope, or implementing C06 requires runtime or
provider behavior outside this work order.

## Write Ownership

Codex may create or edit only the allowed paths listed below. Runtime, route,
provider, generated-state, public-sync, adapter, and downstream use-case paths
are outside write ownership for this tranche.

## Core Guard Self-Protection Authorization

This work order intentionally creates and wires a governance checker.

Authorized guard-maintenance scope: add one read-only raw-memory-release
invariant checker, its focused tests, and the two command-catalog entries needed
for FPC-T3-C06 autorun/reviewer-fast coverage.

Protected paths:

- `governance/compat/check_raw_memory_release_invariant.py`
- `governance/compat/test_check_raw_memory_release_invariant.py`
- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`

Operator authorization: the operator approved continuing according to the next
move on 2026-06-27 after FPC-SCG-T1 closed and P1 machine-check coverage became
the next foundation gap.

Rollback boundary: if FPC-SCG-T2 is rejected, revert only the new checker,
focused test, command-catalog entries, FPC-SCG-T2 artifacts, and C06 guidance
update. Do not revert FPC-SCG-T1 material commit `75fcad20` or session-sync
commit `be06a4cb`.

Authorization boundary: read-only static checker, focused tests, and command
catalog wiring only. No destructive command, runtime mutation, provider call,
or public-sync is authorized.

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| Foundation files touched | new `governance/compat/` checker and test; existing command catalogs; dated GC-018/work-order/review execution artifacts; current FPC guidance |
| Storage class | governance compatibility checker plus dated execution evidence |
| Index/front door | checker is discoverable through autorun/reviewer-fast command catalogs; no new reference folder is created |
| Date policy | execution artifacts carry tranche date; checker is undated code |
| Archive disposition | N/A with reason: no file is archived, split, relocated, or renamed in this tranche |
| Deferred layout work | N/A with reason: this tranche adds one narrow checker and does not create a new foundation file family |

## Roadmap-to-Work-Order Trace Matrix

| Routing requirement | Work-order instruction | Closure evidence |
|---|---|---|
| P1 machine-check coverage after P0 closure | Implement FPC-T3-C06 checker | focused tests and completion review |
| Preserve Memory / Knowledge raw-memory boundary | Require false assertion on memory-facing governed Markdown | checker true-positive and true-negative tests |
| Avoid duplicating MPI-T5 claim checker | Keep MPI-T5 overclaim checker intact and add separate C06 positive assertion guard | focused tests for both checkers |
| Preserve runtime restraint | No runtime/source route or durable store mutation | closure diff gate |
| Keep P2 lanes parked | Forbidden scope and next-move update | completion review |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| FPC-T3-C06 is a remaining P1 machine-check candidate | `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` | `P1 - Machine-Check Coverage Gap` | `FPC-T3-C06` | foundation-plane guidance | ACCEPT |
| C06 target is explicit `rawMemoryReleased=false` autorun check | `docs/reference/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md` | `### FPC-T3-C06: Memory rawMemoryReleased=false Autorun Check` | `rawMemoryReleased` | FPC-T3 coverage plan | ACCEPT |
| MPI-T5 memory access checker blocks explicit true overclaims | `governance/compat/check_memory_access_claim.py` | `CLAIM_RULES` | `raw_memory_or_reinjection_permitted` | memory access claim gate | ACCEPT |
| MPI-T5 focused test covers `rawMemoryReleased: true` | `governance/compat/test_check_memory_access_claim.py` | `test_raw_memory_release_detected` | `raw_memory_or_reinjection_permitted` | memory access claim focused tests | ACCEPT |
| Memory plane map records MPI-T5 checker as running static guard | `docs/reference/CVF_MEMORY_PLANE_MAP.md` | `### Memory Access Claim Checker` | `check_memory_access_claim.py` | Memory Plane map | ACCEPT |
| Runtime readout projection declares false invariant | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` | `buildMemoryRuntimeReadout` projection fields | `rawMemoryReleased` | memory runtime readout projection | ACCEPT |
| Memory readout route declares false response invariant | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | response body fields | `rawMemoryReleased` | memory readout route | ACCEPT |
| Durable memory store declares false receipt invariant | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | receipt fields | `rawMemoryReleased` | durable memory store | ACCEPT |
| Memory context packager declares false evidence invariant | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts` | package evidence fields | `rawMemoryReleased` | memory context packager | ACCEPT |
| Autorun catalog supports adding range-aware static gates | `governance/compat/agent_autorun_command_catalog.py` | `_common_commands` | `_range_command` | autorun command catalog | ACCEPT |
| Reviewer-fast catalog supports adding range-aware static gates | `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | `REVIEWER_FAST_CHECKS` | `memory access claim` | reviewer-fast hook catalog | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class work-order-authoring --role dispatcher --phase pre-dispatch --json`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0006, ADIF-0007

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | `governance/compat/check_raw_memory_release_invariant.py`; `governance/compat/test_check_raw_memory_release_invariant.py`; `governance/compat/agent_autorun_command_catalog.py`; `governance/compat/local_governance_hook_catalog_reviewer_fast.py` |
| Runtime behavior claimed | N/A_WITH_REASON: no product runtime, provider route, Web route, CLI/MCP adapter, durable store, or Learning Plane runtime behavior is changed |
| Helper/checker implementation claimed | PASS: new read-only static checker and focused tests are the only implementation claim |
| Provider/live proof claimed | N/A_WITH_REASON |
| Provider registry surfaces | N/A_WITH_REASON: no provider-selection, provider-routing, provider-registry, or live-governance claim is made |
| Public-sync claimed | N/A_WITH_REASON |
| Freshness disposition | PASS - checker-only FPC-T3-C06 coverage |

## 3. Allowed Paths

- `governance/compat/check_raw_memory_release_invariant.py`
- `governance/compat/test_check_raw_memory_release_invariant.py`
- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
- `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md`
- `docs/baselines/CVF_GC018_FPC_SCG_T2_RAW_MEMORY_RELEASE_INVARIANT_AUTORUN_COVERAGE_2026-06-27.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_SCG_T2_RAW_MEMORY_RELEASE_INVARIANT_AUTORUN_COVERAGE_FOR_CODEX_2026-06-27.md`
- `docs/reviews/CVF_FPC_SCG_T2_RAW_MEMORY_RELEASE_INVARIANT_AUTORUN_COVERAGE_COMPLETION_2026-06-27.md`

## Execution Plan

1. Implement the read-only checker with range-aware CLI behavior.
2. Add focused tests for true positives, true negatives, CLI enforce/json, and
   read-only implementation boundary.
3. Wire the checker into the agent autorun common command bundle and
   reviewer-fast local governance catalog.
4. Update FPC guidance to mark C06 closed bounded and route the next P1 move.
5. Run focused tests and governance gates before commit.

## 4. Required Implementation

1. Add `governance/compat/check_raw_memory_release_invariant.py`.
2. Add `governance/compat/test_check_raw_memory_release_invariant.py`.
3. Add `raw memory release invariant` command to `_common_commands`.
4. Add `raw memory release invariant` command to `REVIEWER_FAST_CHECKS`.
5. Update the FPC guidance P1 table so C06 no longer remains an open gap.

## 5. Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Focused tests for the new checker pass. |
| AC2 | Existing MPI-T5 memory access claim tests still pass. |
| AC3 | The new checker passes on the changed material range. |
| AC4 | Autorun common catalog and reviewer-fast catalog include the new checker. |
| AC5 | Completion review records no runtime/source route, durable store, provider/live, public-sync, generated-state, or MPI-T6 runtime mutation in the material commit. |

## 6. Verification Commands

```powershell
python -m pytest governance/compat/test_check_raw_memory_release_invariant.py governance/compat/test_check_memory_access_claim.py
python governance/compat/check_raw_memory_release_invariant.py --base be06a4cb --head HEAD --enforce
python governance/compat/check_work_order_dispatch_quality.py --base be06a4cb --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base be06a4cb --head HEAD
git diff --check
git status --short
```

## Evidence Requirements

| Evidence | Required form |
|---|---|
| Focused tests | pytest output |
| Checker behavior | CLI output from `check_raw_memory_release_invariant.py` |
| Hook/autorun wiring | `rg` or source diff showing catalog entries |
| Changed set | `git diff --name-status` and `git status --short` |
| Boundary proof | completion review Closure Diff Gate |

## Review Gate

Codex must not commit until focused tests, raw-memory invariant checker,
dispatch quality, markdown structural completeness, agent operation trace,
public export disposition, core guard self-protection, and pre-closure gates
pass or are explicitly blocked with a return-to-orchestrator reason.

## Return-To-Orchestrator Conditions

Return to orchestrator only if source verification shows FPC-T3-C06 cannot be
closed without runtime/provider behavior, if a required source file is missing,
or if a required gate fails on a path outside the authorized scope.

## Operator Checkpoint

Operator checkpoint: none required before material closure. Post-closure next
move should remain in P1 and source-verify FPC-T3-C02 unless the operator
selects FPC-T3-C05 or FPC-T3-C03.

## Closure Checklist

- [x] GC-018 baseline exists.
- [x] Work order exists.
- [x] Checker implementation exists.
- [x] Focused tests exist and pass.
- [x] Autorun catalog wiring exists.
- [x] Reviewer-fast catalog wiring exists.
- [x] Guidance records C06 as closed bounded.
- [x] Completion review exists.
- [x] Runtime/provider/public/use-case/MPI-T6 lanes remain parked.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| GC-018 status | `docs/baselines/CVF_GC018_FPC_SCG_T2_RAW_MEMORY_RELEASE_INVARIANT_AUTORUN_COVERAGE_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_FPC_SCG_T2_RAW_MEMORY_RELEASE_INVARIANT_AUTORUN_COVERAGE_COMPLETION_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` | P1 guidance updated; no roadmap file changed | PASS |
| Registry JSON | BLOCKED with reason: FPC-SCG-T2 is checker-only and does not edit GC-052 registry JSON | N/A | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown companion is edited in this tranche | N/A | BLOCKED with reason |
| External evidence digest | N/A with reason: no external evidence or provider proof used | N/A | N/A with reason |
| System loop interlock | `governance/compat/check_system_loop_interlock.py` | registry checker remains pass with no registry edit | PASS |
| Checker source | `governance/compat/check_raw_memory_release_invariant.py` | focused tests pass | PASS |
| Focused tests | `governance/compat/test_check_raw_memory_release_invariant.py` | pytest pass | PASS |
| Session continuity | reviewer-owned post-material sync | pending separate session-sync after material commit | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Raw-memory invariant checker exists | `governance/compat/check_raw_memory_release_invariant.py` | new checker created | PASS |
| Focused tests exist | `governance/compat/test_check_raw_memory_release_invariant.py` | new focused tests created | PASS |
| Autorun command present | `raw memory release invariant` | added to `_common_commands` | PASS |
| Reviewer-fast command present | `raw memory release invariant` | added to `REVIEWER_FAST_CHECKS` | PASS |
| Runtime mutation | none | no runtime/source route or durable store path in changed set | PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local repository tools |
| Session or invocation | 2026-06-27 FPC-SCG-T2 raw memory invariant coverage |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, pytest, governance gates |
| Target paths | `governance/compat/check_raw_memory_release_invariant.py`; `governance/compat/test_check_raw_memory_release_invariant.py`; `governance/compat/agent_autorun_command_catalog.py`; `governance/compat/local_governance_hook_catalog_reviewer_fast.py`; `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md`; `docs/baselines/CVF_GC018_FPC_SCG_T2_RAW_MEMORY_RELEASE_INVARIANT_AUTORUN_COVERAGE_2026-06-27.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_SCG_T2_RAW_MEMORY_RELEASE_INVARIANT_AUTORUN_COVERAGE_FOR_CODEX_2026-06-27.md`; `docs/reviews/CVF_FPC_SCG_T2_RAW_MEMORY_RELEASE_INVARIANT_AUTORUN_COVERAGE_COMPLETION_2026-06-27.md` |
| Allowed scope source | operator next-move instruction; active session state; FPC guidance; GC-018 baseline; this work order |
| Before status evidence | `git rev-parse --short HEAD` = `be06a4cb` |
| After status evidence | focused tests and gates run before commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | bounded FPC-T3-C06 static checker implementation only |
| Claim boundary | static governed Markdown check only; no runtime/provider/public/use-case/MPI-T6 readiness claim |
| Agent type | Codex single-agent dispatcher/implementer/reviewer |
| Invocation ID | `fpc-scg-t2-raw-memory-release-invariant-coverage-2026-06-27` |
| Expected manifest | `governance/compat/check_raw_memory_release_invariant.py`; `governance/compat/test_check_raw_memory_release_invariant.py`; `governance/compat/agent_autorun_command_catalog.py`; `governance/compat/local_governance_hook_catalog_reviewer_fast.py`; `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md`; `docs/baselines/CVF_GC018_FPC_SCG_T2_RAW_MEMORY_RELEASE_INVARIANT_AUTORUN_COVERAGE_2026-06-27.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_SCG_T2_RAW_MEMORY_RELEASE_INVARIANT_AUTORUN_COVERAGE_FOR_CODEX_2026-06-27.md`; `docs/reviews/CVF_FPC_SCG_T2_RAW_MEMORY_RELEASE_INVARIANT_AUTORUN_COVERAGE_COMPLETION_2026-06-27.md` |
| Actual changed set | `governance/compat/check_raw_memory_release_invariant.py`; `governance/compat/test_check_raw_memory_release_invariant.py`; `governance/compat/agent_autorun_command_catalog.py`; `governance/compat/local_governance_hook_catalog_reviewer_fast.py`; `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md`; `docs/baselines/CVF_GC018_FPC_SCG_T2_RAW_MEMORY_RELEASE_INVARIANT_AUTORUN_COVERAGE_2026-06-27.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_SCG_T2_RAW_MEMORY_RELEASE_INVARIANT_AUTORUN_COVERAGE_FOR_CODEX_2026-06-27.md`; `docs/reviews/CVF_FPC_SCG_T2_RAW_MEMORY_RELEASE_INVARIANT_AUTORUN_COVERAGE_COMPLETION_2026-06-27.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance machine-check tranche. Public-sync is not authorized.

## Claim Boundary

This work order authorizes static governed Markdown coverage only. It does not
modify or prove runtime memory behavior, provider behavior, MCP/CLI adapter
behavior, route behavior, durable store behavior, public readiness, production
readiness, or MPI-T6 runtime value.
