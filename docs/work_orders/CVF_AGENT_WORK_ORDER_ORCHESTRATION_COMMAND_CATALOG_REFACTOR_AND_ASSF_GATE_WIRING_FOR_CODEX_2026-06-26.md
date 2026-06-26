# CVF Agent Work Order: Orchestration Command Catalog Refactor And ASSF Gate Wiring

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-26

docType: work_order

Batch ID: ORCHESTRATION-CATALOG-ASSF-WIRING

dispatchBaseHead: 3384a941

executionBaseHead: 3384a941

closureBaseHead: 3384a941

Commit mode: `WORKER_MAY_COMMIT`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_ORCHESTRATION_COMMAND_CATALOG_REFACTOR_AND_ASSF_GATE_WIRING_FOR_CODEX_2026-06-26.md`

## Dispatch Prompt Envelope

Role: Codex single-agent multi-role executor. This packet authorizes bounded
orchestration command catalog refactor and ASSF gate wiring only.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_ORCHESTRATION_COMMAND_CATALOG_REFACTOR_AND_ASSF_GATE_WIRING_FOR_CODEX_2026-06-26.md`

Paired GC-018 baseline:
`docs/baselines/CVF_GC018_ORCHESTRATION_COMMAND_CATALOG_REFACTOR_AND_ASSF_GATE_WIRING_2026-06-26.md`

## Purpose

Refactor the two near-limit orchestration runner files into smaller runners
plus command catalog helpers, then wire the ASSF certified metadata admission
checker into the standard gate catalogs.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | proactively refactor the two near-limit orchestration files | ACCEPT |
| Active session front door | `CVF_SESSION_MEMORY.md` | ACCEPT |
| Active state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V22_2026-06-22.md` | ACCEPT |
| Paired roadmap | `docs/roadmaps/CVF_ORCHESTRATION_COMMAND_CATALOG_REFACTOR_AND_ASSF_GATE_WIRING_ROADMAP_2026-06-26.md` | ACCEPT |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_ORCHESTRATION_COMMAND_CATALOG_REFACTOR_AND_ASSF_GATE_WIRING_2026-06-26.md` | ACCEPT |

## Agent Roles

| Role | Owner |
|---|---|
| Operator | scope authorization |
| Dispatcher | Codex |
| Worker | Codex single-agent multi-role |
| Reviewer | Codex |
| Closer | Codex |
| Session-sync steward | Codex in a separate commit if session state changes |

## Scope / Methodology

Extract command catalog definitions from the local hook-chain runner and the
agent autorun workflow runner, keep imports compatible for direct script and
package contexts, add the ASSF admission checker to the catalogs, and verify
with compile, size, direct gate, local hook, autorun, and steward gates.

## Findings / Position

The prior bounded decision to leave ASSF admission as a direct material gate
was not enough because the standard orchestration bundles should carry it. This
work order repairs the file-size bottleneck first and then wires the gate.

## Execution Plan

| Step | Action | Evidence |
|---|---|---|
| T0 | verify base and line-count pressure | line count command |
| T1 | extract local hook command catalog | new catalog and py_compile |
| T2 | extract autorun command catalog | new catalog and py_compile |
| T3 | add ASSF admission gate to catalogs | source verification rows |
| T4 | run focused and bundled gates | completion review evidence |

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/check_python_automation_size.py --enforce
python governance/compat/check_assf_certified_metadata_admission.py --require-certified
```

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| contractSource | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | Codex acts as dispatcher, worker, reviewer, and closer for this local material tranche |
| phase | dispatch, execution, closure |
| baseHeadFor(phase) | dispatchBaseHead=`3384a941`; executionBaseHead=`3384a941`; closureBaseHead=`3384a941` |
| changedSetScope(phase) | material scope only: two runners, five catalog helper modules, roadmap, GC-018, work order, completion review |
| traceScope(phase, actor) | Agent Operation Trace Blocks in this work order and completion review |
| commitOwner(phase) | Codex owns material commit; Codex session-sync steward owns separate sync commit if needed |
| crossBatchIsolation | do not mix with session-sync, Web implementation, resolver source mutation, CLI/MCP adapter, provider/live, public-sync, or package instance work |
| nextMoveSurfaces | update only after material commit in separate session-sync if needed |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ORCHESTRATION_COMMAND_CATALOG_REFACTOR_AND_ASSF_GATE_WIRING_COMPLETION_2026-06-26.md` |
| reviewerOwnedClosurePaths | roadmap, baseline, work order, two runners, five catalog helper modules, completion review |

## Required First Reads

| Source | Action | Reason |
|---|---|---|
| `CVF_SESSION_MEMORY.md` | READ | active front door |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ | compact startup facts |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ | full state registry |
| `AGENT_HANDOFF_V22_2026-06-22.md` | READ | active handoff |
| `docs/reference/guard_orientation/README.md` | READ | guard orientation |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ | literal-format checklist |
| `governance/compat/run_local_governance_hook_chain.py` | SOURCE_VERIFIED | local hook runner |
| `governance/compat/run_agent_autorun_workflow_gate.py` | SOURCE_VERIFIED | autorun runner |
| `governance/compat/check_assf_certified_metadata_admission.py` | SOURCE_VERIFIED | gate to wire |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`governance-orchestration-refactor`, role=`codex-multi-role`, lifecyclePhase=`material-implementation`

Returned defects: NONE_RETURNED

- none

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| local runner imports extracted catalog | `governance/compat/run_local_governance_hook_chain.py` | lines 125-131 | `HOOK_CHAINS` | local hook runner | EXISTS | ACCEPT |
| local catalog aggregator defines hook chains | `governance/compat/local_governance_hook_catalog.py` | lines 19-23 | `HOOK_CHAINS` | local hook catalog aggregator | EXISTS | ACCEPT |
| reviewer-fast local chain includes ASSF gate | `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | line 120 | `ASSF certified metadata admission` | reviewer-fast hook catalog | EXISTS | ACCEPT |
| pre-commit local chain includes ASSF gate | `governance/compat/local_governance_hook_catalog_pre_commit.py` | line 175 | `ASSF certified metadata admission` | pre-commit hook catalog | EXISTS | ACCEPT |
| pre-push local chain includes ASSF gate | `governance/compat/local_governance_hook_catalog_pre_push.py` | line 136 | `ASSF certified metadata admission` | pre-push hook catalog | EXISTS | ACCEPT |
| autorun runner imports extracted catalog | `governance/compat/run_agent_autorun_workflow_gate.py` | lines 36-54 | `_common_commands` | autorun workflow runner | EXISTS | ACCEPT |
| autorun catalog owns common command builder | `governance/compat/agent_autorun_command_catalog.py` | line 51 | `_common_commands` | autorun command catalog | EXISTS | ACCEPT |
| autorun catalog includes ASSF gate | `governance/compat/agent_autorun_command_catalog.py` | lines 255-257 | `ASSF certified metadata admission` | autorun command catalog | EXISTS | ACCEPT |
| ASSF admission checker entry point exists | `governance/compat/check_assf_certified_metadata_admission.py` | line 168 | `check` | ASSF admission checker | EXISTS | ACCEPT |

## Write Ownership

| Path | Action |
|---|---|
| `governance/compat/run_local_governance_hook_chain.py` | refactor to import catalog |
| `governance/compat/local_governance_hook_catalog.py` | create local hook catalog aggregator |
| `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | create reviewer-fast catalog and add ASSF gate |
| `governance/compat/local_governance_hook_catalog_pre_commit.py` | create pre-commit catalog and add ASSF gate |
| `governance/compat/local_governance_hook_catalog_pre_push.py` | create pre-push catalog and add ASSF gate |
| `governance/compat/run_agent_autorun_workflow_gate.py` | refactor to import catalog |
| `governance/compat/agent_autorun_command_catalog.py` | create catalog and add ASSF gate |
| `docs/roadmaps/CVF_ORCHESTRATION_COMMAND_CATALOG_REFACTOR_AND_ASSF_GATE_WIRING_ROADMAP_2026-06-26.md` | create and close |
| `docs/baselines/CVF_GC018_ORCHESTRATION_COMMAND_CATALOG_REFACTOR_AND_ASSF_GATE_WIRING_2026-06-26.md` | create and close |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ORCHESTRATION_COMMAND_CATALOG_REFACTOR_AND_ASSF_GATE_WIRING_FOR_CODEX_2026-06-26.md` | create and close |
| `docs/reviews/CVF_ORCHESTRATION_COMMAND_CATALOG_REFACTOR_AND_ASSF_GATE_WIRING_COMPLETION_2026-06-26.md` | create completion review |

## Forbidden Scope

No package instance creation, certification decision, generated-index mutation,
resolver source mutation, Web runtime change, CLI/MCP adapter, provider/live
proof, public-sync, push, or session-sync is authorized in the material commit.

## Evidence Requirements

| Evidence | Required result |
|---|---|
| `python -m py_compile governance/compat/run_local_governance_hook_chain.py governance/compat/local_governance_hook_catalog.py governance/compat/local_governance_hook_catalog_reviewer_fast.py governance/compat/local_governance_hook_catalog_pre_commit.py governance/compat/local_governance_hook_catalog_pre_push.py governance/compat/run_agent_autorun_workflow_gate.py governance/compat/agent_autorun_command_catalog.py` | PASS |
| `python governance/compat/check_python_automation_size.py --enforce` | PASS |
| `python governance/compat/check_assf_certified_metadata_admission.py --require-certified` | PASS |
| `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast --serial` | PASS |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 3384a941 --head HEAD --serial` | PASS |
| `python governance/compat/run_agent_commit_steward_preflight.py --mode implementation --base 3384a941 --head HEAD --enforce` | PASS |

## Current Runtime Freshness Verification

| Surface | Command | Result |
|---|---|---|
| provider registry boundary | `git diff --name-only 3384a941..HEAD -- EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | PASS - no provider registry file in material diff |
| provider capability registry boundary | `git diff --name-only 3384a941..HEAD -- EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | PASS - no PROVIDER_CAPABILITY_REGISTRY mutation in material diff |
| runtime source boundary | `git diff --name-only 3384a941..HEAD -- EXTENSIONS/CVF_v1.6_AGENT_PLATFORM` | PASS - no runtime source path owned |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| storageClass | same-domain governance compatibility helper modules |
| affectedFoundationSurface | `governance/compat` orchestration gate runner helpers |
| layoutDecision | split command catalog data into focused helper modules beside the runners |
| frontDoorImpact | no new docs/reference family folder or README front door is created |
| generatedAggregateImpact | no generated aggregate or index mutation |
| archiveOrRelocationImpact | no archive movement, relocation, or delete |
| maintainabilityOutcome | runner files gain headroom and helper modules stay below python automation hard limits |

## Acceptance Criteria

| ID | Criterion | Status |
|---|---|---|
| AC1 | orchestration runners have material line-count headroom after extraction | PASS |
| AC2 | local hook catalog carries ASSF admission gate | PASS |
| AC3 | autorun common command catalog carries ASSF admission gate | PASS |
| AC4 | focused and bundled governance gates pass | PASS |
| AC5 | material commit excludes session-sync and unrelated ASSF/Web/package work | PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local shell and file-edit tools |
| Session or invocation | 2026-06-26 ORCHESTRATION-CATALOG-ASSF-WIRING material tranche |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, Python governance commands, apply_patch |
| Target paths | two orchestration runners, five catalog helper modules, roadmap, GC-018, work order, completion review |
| Allowed scope source | operator instruction to proactively refactor near-limit orchestration files |
| Before status evidence | `git status --short` empty at base `3384a941` |
| After status evidence | material changed set listed in Actual changed set |
| Diff evidence | `git diff --name-status` over material worktree |
| Approval boundary | operator authorized this maintenance tranche only |
| Claim boundary | command catalog extraction and ASSF gate wiring only; no runtime, package instance, Web implementation, adapter, provider/live, public-sync, push, resolver or registry mutation, or session-sync |
| Agent type | SINGLE_AGENT_MULTI_ROLE |
| Invocation ID | ORCHESTRATION-CATALOG-ASSF-WIRING-CODEX-2026-06-26 |
| Expected manifest | `governance/compat/run_local_governance_hook_chain.py`; `governance/compat/local_governance_hook_catalog.py`; `governance/compat/local_governance_hook_catalog_reviewer_fast.py`; `governance/compat/local_governance_hook_catalog_pre_commit.py`; `governance/compat/local_governance_hook_catalog_pre_push.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/agent_autorun_command_catalog.py`; `docs/roadmaps/CVF_ORCHESTRATION_COMMAND_CATALOG_REFACTOR_AND_ASSF_GATE_WIRING_ROADMAP_2026-06-26.md`; `docs/baselines/CVF_GC018_ORCHESTRATION_COMMAND_CATALOG_REFACTOR_AND_ASSF_GATE_WIRING_2026-06-26.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ORCHESTRATION_COMMAND_CATALOG_REFACTOR_AND_ASSF_GATE_WIRING_FOR_CODEX_2026-06-26.md`; `docs/reviews/CVF_ORCHESTRATION_COMMAND_CATALOG_REFACTOR_AND_ASSF_GATE_WIRING_COMPLETION_2026-06-26.md` |
| Actual changed set | `governance/compat/run_local_governance_hook_chain.py`; `governance/compat/local_governance_hook_catalog.py`; `governance/compat/local_governance_hook_catalog_reviewer_fast.py`; `governance/compat/local_governance_hook_catalog_pre_commit.py`; `governance/compat/local_governance_hook_catalog_pre_push.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/agent_autorun_command_catalog.py`; `docs/roadmaps/CVF_ORCHESTRATION_COMMAND_CATALOG_REFACTOR_AND_ASSF_GATE_WIRING_ROADMAP_2026-06-26.md`; `docs/baselines/CVF_GC018_ORCHESTRATION_COMMAND_CATALOG_REFACTOR_AND_ASSF_GATE_WIRING_2026-06-26.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ORCHESTRATION_COMMAND_CATALOG_REFACTOR_AND_ASSF_GATE_WIRING_FOR_CODEX_2026-06-26.md`; `docs/reviews/CVF_ORCHESTRATION_COMMAND_CATALOG_REFACTOR_AND_ASSF_GATE_WIRING_COMPLETION_2026-06-26.md` |
| Manifest delta | MATCH |

## Review Gate

| Gate | Command | Required result |
|---|---|---|
| Compile | `python -m py_compile governance/compat/run_local_governance_hook_chain.py governance/compat/local_governance_hook_catalog.py governance/compat/local_governance_hook_catalog_reviewer_fast.py governance/compat/local_governance_hook_catalog_pre_commit.py governance/compat/local_governance_hook_catalog_pre_push.py governance/compat/run_agent_autorun_workflow_gate.py governance/compat/agent_autorun_command_catalog.py` | PASS |
| Size | `python governance/compat/check_python_automation_size.py --enforce` | PASS |
| ASSF gate | `python governance/compat/check_assf_certified_metadata_admission.py --require-certified` | PASS |
| Bundled local hook | `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast --serial` | PASS |
| Autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 3384a941 --head HEAD --serial` | PASS |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | direct operator authorization |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this work order |
| Disposition | no external material absorbed |
| Claim boundary | repository-local source and command evidence only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance maintenance; no public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | orchestration command catalog work order |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- command catalog extraction and gate wiring only |
| receiptEvidence | CVF_RECEIPT_PRESENT - compile, size, ASSF gate, local hook, autorun, steward evidence |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- runner extraction, new catalog helper modules, governed artifacts |
| invocationBoundary | local governed source and markdown edits |
| interceptionBoundary | no provider, Web, adapter, resolver, registry, package instance, public-sync, push, or session-sync claim |
| claimLanguage | work order closed bounded |
| forbiddenExpansion | no package instance, activation, runtime behavior, resolver source mutation, Web projection implementation, CLI/MCP adapter, provider/live proof, public-sync, push, package execution, or session-sync |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ORCHESTRATION_COMMAND_CATALOG_REFACTOR_AND_ASSF_GATE_WIRING_COMPLETION_2026-06-26.md` | completion review exists | PASS |
| Roadmap state | `docs/roadmaps/CVF_ORCHESTRATION_COMMAND_CATALOG_REFACTOR_AND_ASSF_GATE_WIRING_ROADMAP_2026-06-26.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | N/A with reason: no registry JSON mutation applies | no registry path owned | N/A with reason |
| Registry Markdown | N/A with reason: no registry markdown mutation applies | no registry path owned | N/A with reason |
| External evidence digest | N/A with reason: no external artifact applies | repository-local evidence only | N/A with reason |
| System loop interlock | N/A with reason: no system loop surface changed | gate remains in bundle | N/A with reason |
| Session continuity | N/A with reason: material commit excludes session-sync | session-sync follows separately if needed | N/A with reason |

## Closure Checklist

| Item | Status |
|---|---|
| Source inventory completed | PASS |
| Catalog extraction completed | PASS |
| ASSF gate wired into standard catalogs | PASS |
| Size guard no longer blocks this wiring | PASS |
| Session-sync excluded from material commit | PASS |

## Return-To-Orchestrator Conditions

Return `CLOSED_PASS_BOUNDED` if the catalog extraction, ASSF gate wiring, size
guard, focused checks, bundled gates, and steward preflight pass. Return
`BLOCKED_WITH_REASON` if the maintenance requires Web, runtime, package,
resolver, registry, provider/live, public-sync, push, or session-sync work.

## Operator Checkpoint

No new operator checkpoint is required for this bounded maintenance closure.
A future checkpoint is required before Web projection implementation, package
instance creation, provider/live proof, public-sync, push, or session-sync
beyond closure continuity.

## Claim Boundary

This work order closes command catalog maintenance only.
