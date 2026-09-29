# CVF Agent Work Order - FPC-SCG-T6 Interlock Expected-Chain Checker Extension

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

dispatchBaseHead: 372ba0e2

executionBaseHead: 372ba0e2

closureBaseHead: 372ba0e2

rawMemoryReleased: false

## Dispatch Prompt Envelope

Task: FPC-SCG-T6 Interlock Expected-Chain Checker Extension.

Agent: Codex.

Commit mode: WORKER_MAY_COMMIT.

Read first:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V23_2026-06-26.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md`
- this work order

Allowed scope: extend `governance/compat/check_system_loop_interlock.py` to
consume the T5 expected-chain manifest, add focused tests, update FPC guidance,
author the GC-018 baseline, this work order, and completion review.

Forbidden scope: registry mutation, manifest expansion, runtime/MCP/CLI/IDE
bridge implementation, provider/live proof, public-sync, downstream use-case
adapter work, DICE runtime expansion, generated active-session mutation in the
material commit, route wiring, Policy_Local, Document Translator, Model
Gateway, Sandbox Runtime, MPI-T6 runtime, package activation, certification
decision, and public/production/readiness claims.

## Purpose

Provide the tactical execution packet for Codex to close FPC-T3-C03 with a
bounded checker extension that consumes the T5 manifest.

## 1. Mission

Extend the existing system-loop interlock checker so every source-verified
eligible expected-chain row remains present in the registry with the expected
`status` and `automationLevel`.

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | source-verify scope and author GC-018/work order |
| Implementer | Codex | implement checker helper, focused tests, and guidance update |
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
| `docs/reference/CVF_FPC_T3_C03_INTERLOCK_EXPECTED_CHAIN_MANIFEST_2026-06-27.json` | READ |
| `docs/reference/CVF_FPC_T3_C03_INTERLOCK_EXPECTED_CHAIN_MANIFEST_2026-06-27.md` | READ |
| `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_STANDARD_2026-06-02.md` | READ |
| `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | READ |
| `governance/compat/check_system_loop_interlock.py` | READ |

## Pre-Flight Checks

| Check | Command |
|---|---|
| Current base | `git rev-parse --short HEAD` |
| FPC-T3-C03 source search | `rg -n "FPC-T3-C03|expected-chain|Interlock Registry Coverage" docs/reference docs/reviews docs/roadmaps governance/compat` |
| Registry validity | `python governance/compat/check_system_loop_interlock.py --enforce` |
| Worktree | `git status --short` |

## 2. Authority Chain

- Operator instruction: 2026-06-27, continue according to next move.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V23_2026-06-26.md`.
- Routing guidance: `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md`.
- GC-018 baseline: `docs/baselines/CVF_GC018_FPC_SCG_T6_INTERLOCK_EXPECTED_CHAIN_CHECKER_EXTENSION_2026-06-27.md`.

## Agent Handoff Contract Control Block

| Field | Value |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | Codex owns dispatch authoring, implementation, review, closure, and any later session-sync |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=372ba0e2`; `executionBaseHead=372ba0e2`; `closureBaseHead=372ba0e2` |
| changedSetScope(phase) | material phase changes only checker source, focused test, FPC guidance, GC-018 baseline, work order, and completion review; session-sync is a separate follow-up commit if required |
| traceScope(phase, actor) | Codex records AOT evidence in the work order, completion review, and changed guidance |
| commitOwner(phase) | Codex owns the material commit and any separate session-sync commit |
| crossBatchIsolation | no public-sync, runtime, provider, generated-state, route, downstream adapter, registry, manifest expansion, or MPI-T6 batch may be merged into this material commit |
| nextMoveSurfaces | update only in a separate session-sync pass after material closure if gates pass |
| Before status evidence | `git rev-parse --short HEAD` = `372ba0e2`; worktree inspected before edit |
| Closer designation | Codex is the designated closer |

## Worker Autonomy / No-Question Rule

Codex must repair allowed-scope gate failures and rerun gates without asking the
operator. Codex must stop only if a required source artifact is missing, a gate
failure points outside authorized scope, or completing T6 requires registry,
manifest, runtime, provider, public-sync, generated-state, downstream use-case,
or MPI-T6 work outside this work order.

## Write Ownership

Codex may create or edit only the allowed paths listed below.

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| Foundation files touched | existing GC-052 checker; focused Python test; current FPC guidance; dated execution artifacts |
| Storage class | foundation-plane checker extension and source-verified closure packet |
| Index/front door | checker remains the GC-052 machine guard; guidance records T6 closure and next decision |
| Date policy | execution artifacts carry tranche date |
| Archive disposition | N/A with reason: no file is archived, split, relocated, or renamed in this tranche |
| Deferred layout work | a later roadmap refresh may decide whether additional expected-chain manifests are needed |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: edit the existing GC-052 checker and add
one focused read-only test under `governance/compat/` for FPC-SCG-T6 only.

Protected paths:

- `governance/compat/check_system_loop_interlock.py`
- `governance/compat/test_check_system_loop_interlock.py`

Operator authorization: the operator instructed Codex to continue according to
the next move after FPC-SCG-T5, and active guidance selected FPC-SCG-T6 as the
next source-verified checker-extension tranche on 2026-06-27.

Rollback boundary: if FPC-SCG-T6 is rejected, remove only the T6 checker
extension, focused test, guidance update, and T6 execution artifacts. Do not
revert FPC-SCG-T5 material commit `fbd98f61` or session-sync commit `372ba0e2`.

Scope boundary: this authorization does not extend to registry mutation,
manifest expansion, runtime/product source, provider/live proof, public-sync,
generated active-session state, downstream adapter work, or MPI-T6 runtime.

## Roadmap-to-Work-Order Trace Matrix

| Routing requirement | Work-order instruction | Closure evidence |
|---|---|---|
| C03 must consume a stable expected-chain manifest | Add manifest comparison to existing checker | checker source and system-loop gate output |
| Avoid broad false-positive inference | Compare only eligible rows in the T5 manifest | helper implementation and focused tests |
| Keep registry mutation separate | Do not edit GC-052 registry JSON | closure diff gate |
| Keep manifest expansion separate | Do not edit T5 manifest JSON | closure diff gate |
| Keep P2 lanes parked | Forbidden scope and next-move update | completion review |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| FPC-T3-C03 extends the existing system-loop checker instead of creating a new checker | `docs/reference/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md` | `### FPC-T3-C03: Interlock Registry Coverage Checker Extension` | `check_system_loop_interlock.py` | FPC-T3 coverage plan | ACCEPT |
| Expected-chain manifest exists and names the future checker target | `docs/reference/CVF_FPC_T3_C03_INTERLOCK_EXPECTED_CHAIN_MANIFEST_2026-06-27.json` | `futureCheckerTarget` | `governance/compat/check_system_loop_interlock.py` | expected-chain manifest schema | ACCEPT |
| Future checker may compare expected ids against registry ids and matching status | `docs/reference/CVF_FPC_T3_C03_INTERLOCK_EXPECTED_CHAIN_MANIFEST_2026-06-27.json` | `futureCheckerMinimumRule` | `expectedChains[].expectedRegistryId` | expected-chain manifest schema | ACCEPT |
| Manifest rows declare expected automation level for the five eligible chains | `docs/reference/CVF_FPC_T3_C03_INTERLOCK_EXPECTED_CHAIN_MANIFEST_2026-06-27.json` | `expectedChains[]` | `expectedAutomationLevel` | expected-chain manifest schema | ACCEPT |
| System-loop registry contract uses stable connection ids, status, and automationLevel | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_STANDARD_2026-06-02.md` | `## Required Registry Fields` | `id`; `status`; `automationLevel` | system-loop interlock standard | ACCEPT |
| Current checker validates registry structure through `validate_registry` | `governance/compat/check_system_loop_interlock.py` | function definition | `validate_registry` | system-loop interlock checker | ACCEPT |
| Active guidance selects FPC-SCG-T6 as the next candidate | `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` | `Recommended next work order candidate` | `FPC-SCG-T6 Interlock Registry Expected-Chain Checker Extension` | foundation-plane gap priority guidance | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class work-order-authoring --role dispatcher --phase pre-dispatch --json`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0006, ADIF-0007

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | `governance/compat/check_system_loop_interlock.py`; `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`; `docs/reference/CVF_FPC_T3_C03_INTERLOCK_EXPECTED_CHAIN_MANIFEST_2026-06-27.json` |
| Runtime behavior claimed | N/A_WITH_REASON: no product runtime, provider route, Web route, CLI/MCP adapter, OCR/provider call, retrieval behavior, downstream adapter behavior, or registry behavior is changed |
| Helper/checker implementation claimed | PASS: existing checker now compares eligible expected-chain manifest rows against registry id/status/automationLevel |
| Provider/live proof claimed | N/A_WITH_REASON |
| Provider registry surfaces | PASS: `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and `PROVIDER_CAPABILITY_REGISTRY` are accounted-for, out-of-scope, and untouched; no provider-selection, provider-routing, provider-registry, or live-governance claim is made |
| Public-sync claimed | N/A_WITH_REASON |
| Freshness disposition | PASS - manifest-backed FPC-T3-C03 checker coverage |

## 3. Allowed Paths

- `governance/compat/check_system_loop_interlock.py`
- `governance/compat/test_check_system_loop_interlock.py`
- `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md`
- `docs/baselines/CVF_GC018_FPC_SCG_T6_INTERLOCK_EXPECTED_CHAIN_CHECKER_EXTENSION_2026-06-27.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_SCG_T6_INTERLOCK_EXPECTED_CHAIN_CHECKER_EXTENSION_FOR_CODEX_2026-06-27.md`
- `docs/reviews/CVF_FPC_SCG_T6_INTERLOCK_EXPECTED_CHAIN_CHECKER_EXTENSION_COMPLETION_2026-06-27.md`

## Execution Plan

1. Add manifest path and comparison helper to `check_system_loop_interlock.py`.
2. Call the comparison helper from `validate_registry`.
3. Add focused tests for matching, missing id, status mismatch, and automationLevel mismatch.
4. Update FPC guidance to mark T6 closed bounded and route next work to roadmap refresh/next tranche decision.
5. Add the FPC-SCG-T6 GC-018 baseline.
6. Add this work order and the completion review.
7. Run checker, focused pytest, and governance gates before commit.

## 4. Required Implementation

1. Extend the existing checker with a read-only manifest comparison.
2. Add focused unit tests.
3. Update FPC guidance.
4. Add the FPC-SCG-T6 GC-018 baseline.
5. Add this work order and the completion review.

## 5. Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Checker fails if an eligible expected-chain manifest row is missing from registry connections. |
| AC2 | Checker fails if an eligible expected-chain manifest row has mismatched expected status. |
| AC3 | Checker fails if an eligible expected-chain manifest row has mismatched expected automationLevel. |
| AC4 | Focused pytest for `test_check_system_loop_interlock.py` passes. |
| AC5 | Registry JSON and T5 manifest JSON remain unchanged. |
| AC6 | Guidance routes the next decision away from reopening C03 unless the manifest/checker regresses. |

## 6. Verification Commands

```powershell
python governance/compat/check_system_loop_interlock.py --enforce
python -m pytest governance/compat/test_check_system_loop_interlock.py -q
python governance/compat/check_work_order_dispatch_quality.py --base 372ba0e2 --head HEAD --enforce
python governance/compat/check_markdown_structural_completeness.py --base 372ba0e2 --head HEAD --enforce
python governance/compat/check_agent_operation_trace.py --base 372ba0e2 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 372ba0e2 --head HEAD --serial
git diff --check
git status --short
```

## Evidence Requirements

| Evidence | Required form |
|---|---|
| Checker validity | `check_system_loop_interlock.py --enforce` output |
| Focused tests | pytest output for `test_check_system_loop_interlock.py` |
| Changed set | `git diff --name-status` and `git status --short` |
| Boundary proof | completion review Closure Diff Gate |

## Review Gate

Codex must not commit until dispatch quality, markdown structural completeness,
agent operation trace, public export disposition, system-loop interlock,
focused pytest, and pre-closure gates pass or are explicitly blocked with a
return-to-orchestrator reason.

## Return-To-Orchestrator Conditions

Return to orchestrator only if source verification shows T6 cannot be closed
without registry mutation, manifest expansion, runtime expansion, provider
behavior, public-sync, generated-state mutation, downstream use-case work, a
required source file is missing, or a required gate fails on a path outside the
authorized scope.

## Operator Checkpoint

Operator checkpoint: none required before material closure. Post-closure next
move should remain foundation-gap oriented and use FPC-SCG-T0 roadmap refresh
or a fresh source-verified tranche decision before any P2 runtime/use-case lane.

## Closure Checklist

- [x] GC-018 baseline exists.
- [x] Work order exists.
- [x] Checker consumes expected-chain manifest.
- [x] Focused test exists.
- [x] Guidance records T6 as closed bounded and routes next decision.
- [x] Completion review exists.
- [x] Runtime/provider/public/registry/manifest/use-case/MPI-T6 lanes remain parked.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| GC-018 status | `docs/baselines/CVF_GC018_FPC_SCG_T6_INTERLOCK_EXPECTED_CHAIN_CHECKER_EXTENSION_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_FPC_SCG_T6_INTERLOCK_EXPECTED_CHAIN_CHECKER_EXTENSION_COMPLETION_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Checker source | `governance/compat/check_system_loop_interlock.py` | expected-chain manifest comparison added | PASS |
| Focused test | `governance/compat/test_check_system_loop_interlock.py` | pytest passes | PASS |
| FPC guidance | `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` | T6 disposition updated | PASS |
| Roadmap state | `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` | P1 guidance updated; no roadmap file changed | PASS |
| Registry JSON | BLOCKED with reason: T6 consumes but does not edit GC-052 registry JSON | N/A | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown companion is edited in this tranche | N/A | BLOCKED with reason |
| Manifest JSON | BLOCKED with reason: T6 consumes but does not edit the T5 expected-chain manifest | N/A | BLOCKED with reason |
| System loop interlock | `governance/compat/check_system_loop_interlock.py` | checker passes with manifest comparison enabled | PASS |
| External evidence digest | N/A with reason: no external evidence or provider proof used | N/A | N/A with reason |
| Session continuity | reviewer-owned post-material sync | pending separate session-sync after material commit | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Eligible manifest rows checked | all `ELIGIBLE_FOR_EXPECTED_CHAIN_CHECK` rows | helper iterates eligible rows | PASS |
| Registry id comparison | required | focused missing-id test passes | PASS |
| Status comparison | required | focused status mismatch test passes | PASS |
| automationLevel comparison | required | focused automationLevel mismatch test passes | PASS |
| Registry mutation | none | registry path unchanged | PASS |
| Manifest mutation | none | manifest path unchanged | PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local repository tools |
| Session or invocation | 2026-06-27 FPC-SCG-T6 interlock expected-chain checker extension |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, Python, pytest, governance gates |
| Target paths | `governance/compat/check_system_loop_interlock.py`; `governance/compat/test_check_system_loop_interlock.py`; `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md`; `docs/baselines/CVF_GC018_FPC_SCG_T6_INTERLOCK_EXPECTED_CHAIN_CHECKER_EXTENSION_2026-06-27.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_SCG_T6_INTERLOCK_EXPECTED_CHAIN_CHECKER_EXTENSION_FOR_CODEX_2026-06-27.md`; `docs/reviews/CVF_FPC_SCG_T6_INTERLOCK_EXPECTED_CHAIN_CHECKER_EXTENSION_COMPLETION_2026-06-27.md` |
| Allowed scope source | operator next-move instruction; active session state; FPC guidance; GC-018 baseline |
| Before status evidence | `git rev-parse --short HEAD` = `372ba0e2` |
| After status evidence | checker extension and focused tests authored; gates run before commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | bounded expected-chain checker extension only |
| Claim boundary | manifest-backed structural checker only; no registry mutation, manifest expansion, runtime/provider/public/use-case/MPI-T6 readiness claim |
| Agent type | Codex single-agent dispatcher/implementer/reviewer |
| Invocation ID | `fpc-scg-t6-interlock-expected-chain-checker-extension-2026-06-27` |
| Expected manifest | `governance/compat/check_system_loop_interlock.py`; `governance/compat/test_check_system_loop_interlock.py`; `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md`; `docs/baselines/CVF_GC018_FPC_SCG_T6_INTERLOCK_EXPECTED_CHAIN_CHECKER_EXTENSION_2026-06-27.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_SCG_T6_INTERLOCK_EXPECTED_CHAIN_CHECKER_EXTENSION_FOR_CODEX_2026-06-27.md`; `docs/reviews/CVF_FPC_SCG_T6_INTERLOCK_EXPECTED_CHAIN_CHECKER_EXTENSION_COMPLETION_2026-06-27.md` |
| Actual changed set | `governance/compat/check_system_loop_interlock.py`; `governance/compat/test_check_system_loop_interlock.py`; `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md`; `docs/baselines/CVF_GC018_FPC_SCG_T6_INTERLOCK_EXPECTED_CHAIN_CHECKER_EXTENSION_2026-06-27.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_SCG_T6_INTERLOCK_EXPECTED_CHAIN_CHECKER_EXTENSION_FOR_CODEX_2026-06-27.md`; `docs/reviews/CVF_FPC_SCG_T6_INTERLOCK_EXPECTED_CHAIN_CHECKER_EXTENSION_COMPLETION_2026-06-27.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance checker-extension tranche. Public-sync is not
authorized.

## Claim Boundary

This work order authorizes only manifest-backed expected-chain checking inside
the existing system-loop interlock checker. It does not modify or prove
registry behavior beyond structural validation, runtime/provider behavior, route
behavior, retrieval behavior, public readiness, production readiness, or MPI-T6
runtime value.
