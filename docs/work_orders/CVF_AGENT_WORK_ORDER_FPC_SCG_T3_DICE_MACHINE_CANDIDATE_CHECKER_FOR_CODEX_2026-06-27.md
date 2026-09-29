# CVF Agent Work Order - FPC-SCG-T3 DICE Machine-Candidate Checker

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

dispatchBaseHead: b64951d5

executionBaseHead: b64951d5

closureBaseHead: b64951d5

rawMemoryReleased: false

## Dispatch Prompt Envelope

Task: FPC-SCG-T3 DICE Machine-Candidate Checker.

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

Allowed scope: implement the FPC-T3-C02 DICE machine-candidate checker,
focused tests, autorun/reviewer-fast catalog wiring, FPC guidance update,
GC-018 baseline, this work order, and completion review.

Forbidden scope: DICE runtime expansion, DIR runtime mutation, OCR/provider/live
proof, downstream adapter work, external app tree access, route wiring, retrieval
behavior changes, generated active-session mutation in the material commit,
public-sync, Policy_Local, Document Translator, Model Gateway, Sandbox Runtime,
MPI-T6 runtime, package activation, certification decision, and
public/production/readiness claims.

## Purpose

Provide the tactical execution packet for Codex to close FPC-T3-C02 with a
bounded read-only checker that makes existing DICE-MC focused coverage visible
to local governance.

## 1. Mission

Implement a governance checker that scans changed paths and, when DICE/DIR
source, tests, or contract artifacts are touched, verifies DICE-MC-01 through
DICE-MC-10 marker coverage and runs the existing focused DICE test suite.

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
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_control_envelope.py` | READ |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_control_envelope.py` | READ |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | READ |

## Pre-Flight Checks

| Check | Command |
|---|---|
| Current base | `git rev-parse --short HEAD` |
| FPC-T3-C02 source search | `rg -n "FPC-T3-C02|check_dice_machine_candidates|DICE-MC" docs/reference EXTENSIONS/CVF_EXTRACTION_FOUNDATION` |
| DICE focused suite | `python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_control_envelope.py -q` |
| Worktree | `git status --short` |

## 2. Authority Chain

- Operator instruction: 2026-06-27, continue according to next move.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V23_2026-06-26.md`.
- Routing guidance: `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md`.
- GC-018 baseline: `docs/baselines/CVF_GC018_FPC_SCG_T3_DICE_MACHINE_CANDIDATE_CHECKER_2026-06-27.md`.

## Agent Handoff Contract Control Block

| Field | Value |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | Codex owns dispatch authoring, implementation, review, closure, and any later session-sync |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=b64951d5`; `executionBaseHead=b64951d5`; `closureBaseHead=b64951d5` |
| changedSetScope(phase) | material phase changes only the checker, focused test, command catalogs, FPC guidance, GC-018 baseline, work order, and completion review; session-sync is a separate follow-up commit if required |
| traceScope(phase, actor) | Codex records AOT evidence in the work order and completion review |
| commitOwner(phase) | Codex owns the material commit and any separate session-sync commit |
| crossBatchIsolation | no public-sync, runtime, provider, generated-state, route, downstream adapter, OCR, retrieval, or external app tree batch may be merged into this material commit |
| nextMoveSurfaces | update only in a separate session-sync pass after material closure if gates pass |
| Before status evidence | `git rev-parse --short HEAD` = `b64951d5`; worktree inspected before edit |
| Closer designation | Codex is the designated closer |

## Worker Autonomy / No-Question Rule

Codex must repair allowed-scope gate failures and rerun gates without asking the
operator. Codex must stop only if a required source artifact is missing, a gate
failure points outside authorized scope, or implementing C02 requires DICE
runtime expansion, provider behavior, OCR execution, or downstream adapter work
outside this work order.

## Write Ownership

Codex may create or edit only the allowed paths listed below. Runtime, route,
provider, generated-state, public-sync, adapter, external app tree, OCR, and
downstream use-case paths are outside write ownership for this tranche.

## Core Guard Self-Protection Authorization

This work order intentionally creates and wires a governance checker.

Authorized guard-maintenance scope: add one read-only DICE machine-candidate
checker, its focused tests, and the two command-catalog entries needed for
FPC-T3-C02 autorun/reviewer-fast coverage.

Protected paths:

- `governance/compat/check_dice_machine_candidates.py`
- `governance/compat/test_check_dice_machine_candidates.py`
- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`

Operator authorization: the operator approved continuing according to the next
move on 2026-06-27 after FPC-SCG-T2 closed and FPC-T3-C02 became the next P1
machine-check coverage gap.

Rollback boundary: if FPC-SCG-T3 is rejected, revert only the new checker,
focused test, command-catalog entries, FPC-SCG-T3 artifacts, and C02 guidance
update. Do not revert FPC-SCG-T2 material commit `62a76d05` or session-sync
commit `b64951d5`.

Authorization boundary: read-only static checker, focused tests, and command
catalog wiring only. No destructive command, runtime mutation, provider call,
external app tree access, OCR execution, downstream adapter work, or public-sync
is authorized.

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
| P1 machine-check coverage after C06 closure | Implement FPC-T3-C02 checker | focused tests and completion review |
| Preserve DICE/DIR ownership invariants | Require DICE-MC marker coverage and focused suite pass when DICE/DIR paths change | checker true-positive and true-negative tests |
| Avoid DICE runtime expansion | Checker invokes tests only and does not edit DICE source | closure diff gate |
| Preserve downstream restraint | No OCR/provider/adapter/retrieval/public/generated-state mutation | completion review |
| Keep P2 lanes parked | Forbidden scope and next-move update | completion review |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| FPC-T3-C02 is the recommended next P1 machine-check candidate | `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` | `Recommended next work order candidate` | `FPC-SCG-T3 DICE Machine-Candidate Checker` | foundation-plane guidance | ACCEPT |
| Original C02 checker was absent | `docs/reference/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md` | `Checker Inventory Snapshot` | `check_dice_machine_candidates.py` | FPC-T3 coverage plan | ACCEPT |
| C02 requires DICE-MC-01 through DICE-MC-10 ownership assertions | `docs/reference/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md` | `### FPC-T3-C02: check_dice_machine_candidates.py` | `DICE-MC-01` | FPC-T3 coverage plan | ACCEPT |
| DICE focused suite records DICE-MC-01 through DICE-MC-10 | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_control_envelope.py` | module header and `test_DICE_MC_*` functions | `DICE-MC-01` | DICE-T1 focused tests | ACCEPT |
| DICE envelope declares bounded claim boundary | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_control_envelope.py` | module constant | `CLAIM_BOUNDARY` | DICE-T1 envelope module | ACCEPT |
| DICE envelope builder is the owner function under test | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_control_envelope.py` | function definition | `build_document_intelligence_control_envelope` | DICE-T1 envelope module | ACCEPT |
| DIR owns authorization gates | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | literal type definition | `AuthorizationGate` | DIR-T1 router module | ACCEPT |
| DIR owns downstream capability literals | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | literal type definition | `DownstreamCapability` | DIR-T1 router module | ACCEPT |
| Autorun catalog supports range-aware static gates | `governance/compat/agent_autorun_command_catalog.py` | `_common_commands` | `_range_command` | autorun command catalog | ACCEPT |
| Reviewer-fast catalog supports range-aware static gates | `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | `REVIEWER_FAST_CHECKS` | `raw memory release invariant` | reviewer-fast hook catalog | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class work-order-authoring --role dispatcher --phase pre-dispatch --json`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0006, ADIF-0007

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_control_envelope.py`; `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_control_envelope.py`; `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py`; `governance/compat/check_dice_machine_candidates.py`; `governance/compat/test_check_dice_machine_candidates.py`; `governance/compat/agent_autorun_command_catalog.py`; `governance/compat/local_governance_hook_catalog_reviewer_fast.py` |
| Runtime behavior claimed | N/A_WITH_REASON: no product runtime, provider route, Web route, CLI/MCP adapter, OCR/provider call, retrieval behavior, or downstream adapter behavior is changed |
| Helper/checker implementation claimed | PASS: new read-only static checker and focused tests are the only implementation claim |
| Provider/live proof claimed | N/A_WITH_REASON |
| Provider registry surfaces | PASS: current provider registry surfaces `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and `PROVIDER_CAPABILITY_REGISTRY` are not changed; no provider-selection, provider-routing, provider-registry, or live-governance claim is made |
| Public-sync claimed | N/A_WITH_REASON |
| Freshness disposition | PASS - checker-only FPC-T3-C02 coverage |

## 3. Allowed Paths

- `governance/compat/check_dice_machine_candidates.py`
- `governance/compat/test_check_dice_machine_candidates.py`
- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
- `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md`
- `docs/baselines/CVF_GC018_FPC_SCG_T3_DICE_MACHINE_CANDIDATE_CHECKER_2026-06-27.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_SCG_T3_DICE_MACHINE_CANDIDATE_CHECKER_FOR_CODEX_2026-06-27.md`
- `docs/reviews/CVF_FPC_SCG_T3_DICE_MACHINE_CANDIDATE_CHECKER_COMPLETION_2026-06-27.md`

## Execution Plan

1. Implement the read-only checker with range-aware CLI behavior.
2. Add focused tests for non-applicable ranges, marker gaps, pytest failures,
   CLI enforce/json, and read-only implementation boundary.
3. Wire the checker into the agent autorun common command bundle and
   reviewer-fast local governance catalog.
4. Update FPC guidance to mark C02 closed bounded and route the next P1 move.
5. Run focused tests and governance gates before commit.

## 4. Required Implementation

1. Add `governance/compat/check_dice_machine_candidates.py`.
2. Add `governance/compat/test_check_dice_machine_candidates.py`.
3. Add `DICE machine-candidate coverage` command to `_common_commands`.
4. Add `DICE machine-candidate coverage` command to `REVIEWER_FAST_CHECKS`.
5. Update the FPC guidance P1 table so C02 no longer remains an open gap.

## 5. Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Focused tests for the new checker pass. |
| AC2 | Existing DICE focused suite still passes. |
| AC3 | The new checker passes on the changed material range. |
| AC4 | Autorun common catalog and reviewer-fast catalog include the new checker. |
| AC5 | Completion review records no DICE/DIR runtime source, OCR/provider/live, downstream adapter, public-sync, generated-state, or MPI-T6 runtime mutation in the material commit. |

## 6. Verification Commands

```powershell
python -m pytest governance/compat/test_check_dice_machine_candidates.py EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_control_envelope.py -q
python governance/compat/check_dice_machine_candidates.py --base b64951d5 --head HEAD --enforce
python governance/compat/check_work_order_dispatch_quality.py --base b64951d5 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base b64951d5 --head HEAD
git diff --check
git status --short
```

## Evidence Requirements

| Evidence | Required form |
|---|---|
| Focused tests | pytest output |
| Checker behavior | CLI output from `check_dice_machine_candidates.py` |
| Hook/autorun wiring | `rg` or source diff showing catalog entries |
| Changed set | `git diff --name-status` and `git status --short` |
| Boundary proof | completion review Closure Diff Gate |

## Review Gate

Codex must not commit until focused tests, DICE machine-candidate checker,
dispatch quality, markdown structural completeness, agent operation trace,
public export disposition, core guard self-protection, and pre-closure gates
pass or are explicitly blocked with a return-to-orchestrator reason.

## Return-To-Orchestrator Conditions

Return to orchestrator only if source verification shows FPC-T3-C02 cannot be
closed without DICE runtime expansion, provider behavior, OCR execution,
external app tree access, downstream adapter work, if a required source file is
missing, or if a required gate fails on a path outside the authorized scope.

## Operator Checkpoint

Operator checkpoint: none required before material closure. Post-closure next
move should remain in P1 and source-verify FPC-T3-C05 unless the operator
selects FPC-T3-C03 or another foundation-gap tranche.

## Closure Checklist

- [x] GC-018 baseline exists.
- [x] Work order exists.
- [x] Checker implementation exists.
- [x] Focused checker tests exist and pass.
- [x] DICE focused suite passes.
- [x] Autorun catalog wiring exists.
- [x] Reviewer-fast catalog wiring exists.
- [x] Guidance records C02 as closed bounded.
- [x] Completion review exists.
- [x] Runtime/provider/public/use-case/MPI-T6 lanes remain parked.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| GC-018 status | `docs/baselines/CVF_GC018_FPC_SCG_T3_DICE_MACHINE_CANDIDATE_CHECKER_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_FPC_SCG_T3_DICE_MACHINE_CANDIDATE_CHECKER_COMPLETION_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` | P1 guidance updated; no roadmap file changed | PASS |
| Checker source | `governance/compat/check_dice_machine_candidates.py` | focused tests pass | PASS |
| Focused checker tests | `governance/compat/test_check_dice_machine_candidates.py` | pytest pass | PASS |
| DICE focused suite | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_control_envelope.py` | pytest pass | PASS |
| Registry JSON | BLOCKED with reason: FPC-SCG-T3 is checker-only and does not edit GC-052 registry JSON | N/A | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown companion is edited in this tranche | N/A | BLOCKED with reason |
| System loop interlock | `governance/compat/check_system_loop_interlock.py` | registry checker remains pass with no registry edit | PASS |
| External evidence digest | N/A with reason: no external evidence or provider proof used | N/A | N/A with reason |
| Session continuity | reviewer-owned post-material sync | pending separate session-sync after material commit | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| DICE checker exists | `governance/compat/check_dice_machine_candidates.py` | new checker created | PASS |
| Focused checker tests exist | `governance/compat/test_check_dice_machine_candidates.py` | new focused tests created | PASS |
| DICE focused tests pass | `25 passed` | focused suite passes | PASS |
| Autorun command present | `DICE machine-candidate coverage` | added to `_common_commands` | PASS |
| Reviewer-fast command present | `DICE machine-candidate coverage` | added to `REVIEWER_FAST_CHECKS` | PASS |
| Runtime mutation | none | no DICE/DIR runtime source path changed | PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local repository tools |
| Session or invocation | 2026-06-27 FPC-SCG-T3 DICE machine-candidate checker |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, pytest, governance gates |
| Target paths | `governance/compat/check_dice_machine_candidates.py`; `governance/compat/test_check_dice_machine_candidates.py`; `governance/compat/agent_autorun_command_catalog.py`; `governance/compat/local_governance_hook_catalog_reviewer_fast.py`; `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md`; `docs/baselines/CVF_GC018_FPC_SCG_T3_DICE_MACHINE_CANDIDATE_CHECKER_2026-06-27.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_SCG_T3_DICE_MACHINE_CANDIDATE_CHECKER_FOR_CODEX_2026-06-27.md`; `docs/reviews/CVF_FPC_SCG_T3_DICE_MACHINE_CANDIDATE_CHECKER_COMPLETION_2026-06-27.md` |
| Allowed scope source | operator next-move instruction; active session state; FPC guidance; GC-018 baseline; this work order |
| Before status evidence | `git rev-parse --short HEAD` = `b64951d5` |
| After status evidence | focused tests and gates run before commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | bounded FPC-T3-C02 static checker implementation only |
| Claim boundary | static DICE/DIR governance visibility only; no runtime/provider/public/use-case/MPI-T6 readiness claim |
| Agent type | Codex single-agent dispatcher/implementer/reviewer |
| Invocation ID | `fpc-scg-t3-dice-machine-candidate-checker-2026-06-27` |
| Expected manifest | `governance/compat/check_dice_machine_candidates.py`; `governance/compat/test_check_dice_machine_candidates.py`; `governance/compat/agent_autorun_command_catalog.py`; `governance/compat/local_governance_hook_catalog_reviewer_fast.py`; `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md`; `docs/baselines/CVF_GC018_FPC_SCG_T3_DICE_MACHINE_CANDIDATE_CHECKER_2026-06-27.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_SCG_T3_DICE_MACHINE_CANDIDATE_CHECKER_FOR_CODEX_2026-06-27.md`; `docs/reviews/CVF_FPC_SCG_T3_DICE_MACHINE_CANDIDATE_CHECKER_COMPLETION_2026-06-27.md` |
| Actual changed set | `governance/compat/check_dice_machine_candidates.py`; `governance/compat/test_check_dice_machine_candidates.py`; `governance/compat/agent_autorun_command_catalog.py`; `governance/compat/local_governance_hook_catalog_reviewer_fast.py`; `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md`; `docs/baselines/CVF_GC018_FPC_SCG_T3_DICE_MACHINE_CANDIDATE_CHECKER_2026-06-27.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_SCG_T3_DICE_MACHINE_CANDIDATE_CHECKER_FOR_CODEX_2026-06-27.md`; `docs/reviews/CVF_FPC_SCG_T3_DICE_MACHINE_CANDIDATE_CHECKER_COMPLETION_2026-06-27.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance machine-check tranche. Public-sync is not authorized.

## Claim Boundary

This work order authorizes static DICE/DIR governance visibility only. It does
not modify or prove DICE runtime expansion, OCR/provider behavior, downstream
adapter behavior, route behavior, retrieval behavior, external app tree access,
public readiness, production readiness, or MPI-T6 runtime value.
