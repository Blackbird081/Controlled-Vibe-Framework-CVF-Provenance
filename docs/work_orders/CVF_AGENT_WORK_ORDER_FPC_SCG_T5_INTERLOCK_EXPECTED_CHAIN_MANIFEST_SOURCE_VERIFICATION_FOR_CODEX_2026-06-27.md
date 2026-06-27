# CVF Agent Work Order - FPC-SCG-T5 Interlock Expected-Chain Manifest Source Verification

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

dispatchBaseHead: 49fa5a69

executionBaseHead: 49fa5a69

closureBaseHead: 49fa5a69

rawMemoryReleased: false

## Dispatch Prompt Envelope

Task: FPC-SCG-T5 Interlock Expected-Chain Manifest Source Verification.

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

Allowed scope: create the FPC-T3-C03 expected-chain manifest JSON and Markdown
companion, update FPC guidance, author the GC-018 baseline, this work order,
and completion review.

Forbidden scope: checker implementation, registry mutation, runtime/MCP/CLI/IDE
bridge implementation, provider/live proof, public-sync, downstream use-case
adapter work, DICE runtime expansion, generated active-session mutation in the
material commit, route wiring, Policy_Local, Document Translator, Model
Gateway, Sandbox Runtime, MPI-T6 runtime, package activation, certification
decision, and public/production/readiness claims.

## Purpose

Provide the tactical execution packet for Codex to close the FPC-T3-C03
manifest prerequisite with a bounded source-verification artifact.

## 1. Mission

Create a stable expected-chain manifest that a later FPC-T3-C03 checker
extension can compare against the system-loop interlock registry.

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | source-verify scope and author GC-018/work order |
| Implementer | Codex | author manifest JSON, Markdown companion, and guidance update |
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
| `docs/reference/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_MATRIX_2026-06-13.md` | READ |
| `docs/reviews/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_COMPLETION_2026-06-13.md` | READ |
| `docs/reviews/CVF_FPC_T3_C04_C01_EPISTEMIC_WORK_ORDER_AND_PROCESS_PACKET_GUARD_COMPLETION_2026-06-13.md` | READ |
| `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_STANDARD_2026-06-02.md` | READ |
| `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | READ |
| `governance/compat/check_system_loop_interlock.py` | READ |

## Pre-Flight Checks

| Check | Command |
|---|---|
| Current base | `git rev-parse --short HEAD` |
| FPC-T3-C03 source search | `rg -n "FPC-T3-C03|expected-chain|Interlock Registry Coverage" docs/reference docs/reviews docs/roadmaps governance/compat` |
| Registry validity | `python governance/compat/check_system_loop_interlock.py --enforce` |
| Expected id readout | PowerShell here-string Python registry readout for five expected ids |
| Worktree | `git status --short` |

## 2. Authority Chain

- Operator instruction: 2026-06-27, continue according to next move.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V23_2026-06-26.md`.
- Routing guidance: `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md`.
- GC-018 baseline: `docs/baselines/CVF_GC018_FPC_SCG_T5_INTERLOCK_EXPECTED_CHAIN_MANIFEST_SOURCE_VERIFICATION_2026-06-27.md`.

## Agent Handoff Contract Control Block

| Field | Value |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | Codex owns dispatch authoring, implementation, review, closure, and any later session-sync |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=49fa5a69`; `executionBaseHead=49fa5a69`; `closureBaseHead=49fa5a69` |
| changedSetScope(phase) | material phase changes only manifest JSON, manifest Markdown, FPC guidance, GC-018 baseline, work order, and completion review; session-sync is a separate follow-up commit if required |
| traceScope(phase, actor) | Codex records AOT evidence in the work order, completion review, and changed manifest reference |
| commitOwner(phase) | Codex owns the material commit and any separate session-sync commit |
| crossBatchIsolation | no public-sync, runtime, provider, generated-state, route, downstream adapter, registry, checker implementation, or MPI-T6 batch may be merged into this material commit |
| nextMoveSurfaces | update only in a separate session-sync pass after material closure if gates pass |
| Before status evidence | `git rev-parse --short HEAD` = `49fa5a69`; worktree inspected before edit |
| Closer designation | Codex is the designated closer |

## Worker Autonomy / No-Question Rule

Codex must repair allowed-scope gate failures and rerun gates without asking the
operator. Codex must stop only if a required source artifact is missing, a gate
failure points outside authorized scope, or completing T5 requires checker,
registry, runtime, provider, public-sync, generated-state, downstream use-case,
or MPI-T6 work outside this work order.

## Write Ownership

Codex may create or edit only the allowed paths listed below.

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| Foundation files touched | dated expected-chain manifest JSON and Markdown companion; dated execution artifacts; current FPC guidance |
| Storage class | source-verified foundation-plane reference manifest |
| Index/front door | manifest is referenced from FPC guidance and can be consumed by a later C03 checker work order |
| Date policy | manifest and execution artifacts carry tranche date |
| Archive disposition | N/A with reason: no file is archived, split, relocated, or renamed in this tranche |
| Deferred layout work | a later checker-extension tranche may decide whether to add a generated source layout if the manifest expands materially |

## Roadmap-to-Work-Order Trace Matrix

| Routing requirement | Work-order instruction | Closure evidence |
|---|---|---|
| C03 needs a stable expected-chain manifest | Author JSON manifest and Markdown companion | completion review and manifest files |
| Avoid false-positive checker inference | Limit expected chains to five source-verified FPC candidates | manifest source verification table |
| Keep checker implementation separate | Do not edit `check_system_loop_interlock.py` | closure diff gate |
| Keep registry mutation separate | Do not edit GC-052 registry JSON | closure diff gate |
| Keep P2 lanes parked | Forbidden scope and next-move update | completion review |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| FPC-T3-C03 requires a stable expected-chain manifest before checker extension | `docs/reference/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md` | `### FPC-T3-C03: Interlock Registry Coverage Checker Extension` | `FPC-T3-C03` | FPC-T3 coverage plan | ACCEPT |
| Active guidance selects FPC-SCG-T5 as the next work order candidate | `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` | `Recommended next work order candidate` | `FPC-SCG-T5 Interlock Registry Expected-Chain Manifest Source Verification` | foundation-plane gap priority guidance | ACCEPT |
| C01 through C04 were accepted as proposal-only interlock entries | `docs/reviews/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_COMPLETION_2026-06-13.md` | `## Decision Result` | `ADD_INTERLOCK_ENTRY` | FPC-T2 completion review | ACCEPT |
| C05 was machine-check-first until FPC-T3-C01 existed | `docs/reviews/CVF_FPC_T2_SYSTEM_LOOP_INTERLOCK_EXPANSION_DECISION_COMPLETION_2026-06-13.md` | `## Decision Result` | `MACHINE_CHECK_FIRST` | FPC-T2 completion review | ACCEPT |
| FPC-T3-C04+C01 closed the epistemic checker prerequisite | `docs/reviews/CVF_FPC_T3_C04_C01_EPISTEMIC_WORK_ORDER_AND_PROCESS_PACKET_GUARD_COMPLETION_2026-06-13.md` | `## Claim Update` | `check_epistemic_process_packet.py` | FPC-T3-C04+C01 completion review | ACCEPT |
| Current checker validates registry structure through `validate_registry` | `governance/compat/check_system_loop_interlock.py` | function definition | `validate_registry` | system-loop interlock checker | ACCEPT |
| Current registry contains all five expected ids | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | `connections[]` | `connections` | system-loop interlock registry schema | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class work-order-authoring --role dispatcher --phase pre-dispatch --json`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0006, ADIF-0007

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | `governance/compat/check_system_loop_interlock.py`; `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` |
| Runtime behavior claimed | N/A_WITH_REASON: no product runtime, provider route, Web route, CLI/MCP adapter, OCR/provider call, retrieval behavior, downstream adapter behavior, or registry behavior is changed |
| Helper/checker implementation claimed | N/A_WITH_REASON: T5 creates a manifest only and does not edit checker source |
| Provider/live proof claimed | N/A_WITH_REASON |
| Provider registry surfaces | PASS: no provider-selection, provider-routing, provider-registry, or live-governance claim is made |
| Public-sync claimed | N/A_WITH_REASON |
| Freshness disposition | PASS - manifest-only FPC-T3-C03 prerequisite coverage |

## 3. Allowed Paths

- `docs/reference/CVF_FPC_T3_C03_INTERLOCK_EXPECTED_CHAIN_MANIFEST_2026-06-27.json`
- `docs/reference/CVF_FPC_T3_C03_INTERLOCK_EXPECTED_CHAIN_MANIFEST_2026-06-27.md`
- `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md`
- `docs/baselines/CVF_GC018_FPC_SCG_T5_INTERLOCK_EXPECTED_CHAIN_MANIFEST_SOURCE_VERIFICATION_2026-06-27.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_SCG_T5_INTERLOCK_EXPECTED_CHAIN_MANIFEST_SOURCE_VERIFICATION_FOR_CODEX_2026-06-27.md`
- `docs/reviews/CVF_FPC_SCG_T5_INTERLOCK_EXPECTED_CHAIN_MANIFEST_SOURCE_VERIFICATION_COMPLETION_2026-06-27.md`

## Execution Plan

1. Author the expected-chain manifest JSON with five source-verified entries.
2. Author the Markdown companion with source verification and future checker boundary.
3. Update FPC guidance to mark T5 closed bounded and route next work to T6 checker extension.
4. Add the FPC-SCG-T5 GC-018 baseline.
5. Add this work order and the completion review.
6. Run manifest, registry, and governance gates before commit.

## 4. Required Implementation

1. Add the manifest JSON.
2. Add the manifest Markdown companion.
3. Update FPC guidance.
4. Add the FPC-SCG-T5 GC-018 baseline.
5. Add this work order and the completion review.

## 5. Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Manifest JSON lists exactly five expected chains for FPC-T2-C01 through C05. |
| AC2 | Manifest Markdown source-verifies the expected-chain basis from FPC and current registry sources. |
| AC3 | Current registry checker remains passing. |
| AC4 | No checker source or registry JSON is changed. |
| AC5 | Guidance routes the next P1 candidate to FPC-SCG-T6 checker extension using the manifest. |

## 6. Verification Commands

```powershell
python governance/compat/check_system_loop_interlock.py --enforce
python governance/compat/check_work_order_dispatch_quality.py --base 49fa5a69 --head HEAD --enforce
python governance/compat/check_markdown_structural_completeness.py --base 49fa5a69 --head HEAD --enforce
python governance/compat/check_agent_operation_trace.py --base 49fa5a69 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 49fa5a69 --head HEAD --serial
git diff --check
git status --short
```

## Evidence Requirements

| Evidence | Required form |
|---|---|
| Manifest validity | JSON parse and expected-chain count |
| Registry validity | `check_system_loop_interlock.py --enforce` output |
| Changed set | `git diff --name-status` and `git status --short` |
| Boundary proof | completion review Closure Diff Gate |

## Review Gate

Codex must not commit until dispatch quality, markdown structural completeness,
agent operation trace, public export disposition, system-loop interlock,
manifest parse, and pre-closure gates pass or are explicitly blocked with a
return-to-orchestrator reason.

## Return-To-Orchestrator Conditions

Return to orchestrator only if source verification shows the manifest cannot be
closed without checker implementation, registry mutation, runtime expansion,
provider behavior, public-sync, generated-state mutation, downstream use-case
work, a required source file is missing, or a required gate fails on a path
outside the authorized scope.

## Operator Checkpoint

Operator checkpoint: none required before material closure. Post-closure next
move should remain in P1 and may open FPC-SCG-T6 checker extension against this
manifest unless the operator selects another foundation-gap tranche.

## Closure Checklist

- [x] GC-018 baseline exists.
- [x] Work order exists.
- [x] Manifest JSON exists.
- [x] Manifest Markdown companion exists.
- [x] Guidance records T5 as closed bounded and routes T6 next.
- [x] Completion review exists.
- [x] Runtime/provider/public/registry/checker/use-case/MPI-T6 lanes remain parked.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| GC-018 status | `docs/baselines/CVF_GC018_FPC_SCG_T5_INTERLOCK_EXPECTED_CHAIN_MANIFEST_SOURCE_VERIFICATION_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_FPC_SCG_T5_INTERLOCK_EXPECTED_CHAIN_MANIFEST_SOURCE_VERIFICATION_COMPLETION_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Manifest JSON | `docs/reference/CVF_FPC_T3_C03_INTERLOCK_EXPECTED_CHAIN_MANIFEST_2026-06-27.json` | five expected chains | PASS |
| Manifest Markdown | `docs/reference/CVF_FPC_T3_C03_INTERLOCK_EXPECTED_CHAIN_MANIFEST_2026-06-27.md` | source verification block | PASS |
| FPC guidance | `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` | T5 disposition updated | PASS |
| Roadmap state | `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` | P1 guidance updated; no roadmap file changed | PASS |
| Registry JSON | BLOCKED with reason: T5 consumes but does not edit GC-052 registry JSON | N/A | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown companion is edited in this tranche | N/A | BLOCKED with reason |
| Checker source | BLOCKED with reason: T5 does not implement C03 checker extension | N/A | BLOCKED with reason |
| System loop interlock | `governance/compat/check_system_loop_interlock.py` | registry checker remains pass | PASS |
| External evidence digest | N/A with reason: no external evidence or provider proof used | N/A | N/A with reason |
| Session continuity | reviewer-owned post-material sync | pending separate session-sync after material commit | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Expected-chain count | 5 | five FPC-T2 C01 through C05 expected chains | PASS |
| Registry comparison target | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | recorded in manifest JSON | PASS |
| Future checker target | `governance/compat/check_system_loop_interlock.py` | recorded in manifest JSON | PASS |
| Checker implementation | none | no checker path changed | PASS |
| Registry mutation | none | registry path unchanged | PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local repository tools |
| Session or invocation | 2026-06-27 FPC-SCG-T5 interlock expected-chain manifest source verification |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, Python, governance gates |
| Target paths | `docs/reference/CVF_FPC_T3_C03_INTERLOCK_EXPECTED_CHAIN_MANIFEST_2026-06-27.json`; `docs/reference/CVF_FPC_T3_C03_INTERLOCK_EXPECTED_CHAIN_MANIFEST_2026-06-27.md`; `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md`; `docs/baselines/CVF_GC018_FPC_SCG_T5_INTERLOCK_EXPECTED_CHAIN_MANIFEST_SOURCE_VERIFICATION_2026-06-27.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_SCG_T5_INTERLOCK_EXPECTED_CHAIN_MANIFEST_SOURCE_VERIFICATION_FOR_CODEX_2026-06-27.md`; `docs/reviews/CVF_FPC_SCG_T5_INTERLOCK_EXPECTED_CHAIN_MANIFEST_SOURCE_VERIFICATION_COMPLETION_2026-06-27.md` |
| Allowed scope source | operator next-move instruction; active session state; FPC guidance; GC-018 baseline |
| Before status evidence | `git rev-parse --short HEAD` = `49fa5a69` |
| After status evidence | manifest and source-verification artifacts authored; gates run before commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | bounded expected-chain manifest source verification only |
| Claim boundary | manifest/reference only; no checker implementation, registry mutation, runtime/provider/public/use-case/MPI-T6 readiness claim |
| Agent type | Codex single-agent dispatcher/implementer/reviewer |
| Invocation ID | `fpc-scg-t5-interlock-expected-chain-manifest-source-verification-2026-06-27` |
| Expected manifest | `docs/reference/CVF_FPC_T3_C03_INTERLOCK_EXPECTED_CHAIN_MANIFEST_2026-06-27.json`; `docs/reference/CVF_FPC_T3_C03_INTERLOCK_EXPECTED_CHAIN_MANIFEST_2026-06-27.md`; `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md`; `docs/baselines/CVF_GC018_FPC_SCG_T5_INTERLOCK_EXPECTED_CHAIN_MANIFEST_SOURCE_VERIFICATION_2026-06-27.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_SCG_T5_INTERLOCK_EXPECTED_CHAIN_MANIFEST_SOURCE_VERIFICATION_FOR_CODEX_2026-06-27.md`; `docs/reviews/CVF_FPC_SCG_T5_INTERLOCK_EXPECTED_CHAIN_MANIFEST_SOURCE_VERIFICATION_COMPLETION_2026-06-27.md` |
| Actual changed set | `docs/reference/CVF_FPC_T3_C03_INTERLOCK_EXPECTED_CHAIN_MANIFEST_2026-06-27.json`; `docs/reference/CVF_FPC_T3_C03_INTERLOCK_EXPECTED_CHAIN_MANIFEST_2026-06-27.md`; `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md`; `docs/baselines/CVF_GC018_FPC_SCG_T5_INTERLOCK_EXPECTED_CHAIN_MANIFEST_SOURCE_VERIFICATION_2026-06-27.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_SCG_T5_INTERLOCK_EXPECTED_CHAIN_MANIFEST_SOURCE_VERIFICATION_FOR_CODEX_2026-06-27.md`; `docs/reviews/CVF_FPC_SCG_T5_INTERLOCK_EXPECTED_CHAIN_MANIFEST_SOURCE_VERIFICATION_COMPLETION_2026-06-27.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance manifest source-verification tranche. Public-sync is
not authorized.

## Claim Boundary

This work order authorizes only expected-chain manifest source verification. It
does not modify or prove checker behavior, registry behavior, runtime/provider
behavior, route behavior, retrieval behavior, public readiness, production
readiness, or MPI-T6 runtime value.
