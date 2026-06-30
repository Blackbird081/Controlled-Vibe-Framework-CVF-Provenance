# CVF Agent Work Order SCPL-T2 Skill Selection Guidance

Memory class: governed-work-order

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

Batch ID: SCPL-T2

## Purpose

Add package-skill domain classification and spec-to-skill selection guidance so
users and agents can choose relevant package skills from a received spec before
runtime package use.

## Authority Chain

| Authority | Path |
|---|---|
| Operator request | current conversation request to add domain and spec-selection guidance for package skills |
| Active session | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| Active handoff | `AGENT_HANDOFF_V29_2026-06-30.md` |
| Prior control plane | `docs/reference/agent_system_skills/CVF_SKILL_CONTROL_PLANE_INVENTORY_STANDARD.md` |
| New selection standard | `docs/reference/agent_system_skills/CVF_SKILL_SELECTION_GUIDANCE_STANDARD.md` |

## Agent Roles

| Role | Assignment |
|---|---|
| Dispatcher | reviewer/closer |
| Worker | reviewer/closer |
| Reviewer | reviewer/closer |
| Session-sync steward | reviewer/closer after material commit if needed |

## Scope / Target / Owner Boundary

Target paths:

- `docs/reference/agent_system_skills/CVF_SKILL_SELECTION_GUIDANCE_STANDARD.md`
- `docs/reference/agent_system_skills/control_plane/source/skill-selection-profiles.json`
- `docs/reference/agent_system_skills/control_plane/generated/skill-inventory.json`
- `governance/compat/generate_skill_control_plane_inventory.py`
- `governance/compat/run_skill_control_plane_inventory.py`
- `governance/compat/test_skill_control_plane_inventory.py`

Owner boundary: reviewer/closer may implement and commit this bounded
control-plane tranche. No package lifecycle mutation, package body read,
provider/live proof, Web page, MCP server, public-sync, or production claim is
authorized.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`guard`, role=`worker`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

## Package Skill Productionization Control Block

- SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`
- Current phase: selection guidance and discovery readiness
- Target lifecycle state: no package lifecycle mutation
- Prior phase evidence: SCPL-T1 closed at `c5670974`
- Next forbidden skip: no package promotion, ACTIVE claim, runtime/provider proof, public/prod claim, or adapter claim may bypass the SOP
- Runtime/provider proof: N/A with reason: selection guidance and checker only; no runtime/provider governance behavior claimed
- Claim boundary: package-skill selection guidance only

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Durable foundation class | agent-system-skills control-plane source and reference standard |
| Storage owner | `docs/reference/agent_system_skills/` |
| Source layout | `docs/reference/agent_system_skills/control_plane/source/skill-selection-profiles.json` |
| Generated layout | `docs/reference/agent_system_skills/control_plane/generated/skill-inventory.json` |
| Generator/checker owner | `governance/compat/generate_skill_control_plane_inventory.py`; `governance/compat/check_skill_control_plane_inventory.py` |
| Index or front door update | `docs/reference/agent_system_skills/CVF_SKILL_SELECTION_GUIDANCE_STANDARD.md` defines the selection profile contract |
| Layout mutation boundary | add selection-profile source and generated projection only; no package root relocation, registry entry relocation, Web projection relocation, runtime package promotion, MCP server, public-sync, or provider runtime change |
| Drift guard | `python governance/compat/check_skill_control_plane_inventory.py --enforce` |
| Claim boundary | durable selection metadata and CLI recommendation read model only |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Skill Control Plane inventory generator exists | `governance/compat/generate_skill_control_plane_inventory.py` | source | `build_inventory` | Skill Control Plane generator | EXISTS | ACCEPT |
| Selection profile source constant exists | `governance/compat/generate_skill_control_plane_inventory.py` | source | `SELECTION_PROFILES_PATH` | Skill Control Plane generator | EXISTS | ACCEPT |
| Selection scorer exists | `governance/compat/generate_skill_control_plane_inventory.py` | source | `recommend_skills_for_spec` | Skill Control Plane generator | RUNTIME_BEHAVIOR | ACCEPT |
| CLI spec text flag exists | `governance/compat/run_skill_control_plane_inventory.py` | source | `--spec-text` | Skill Control Plane CLI | EXISTS | ACCEPT |
| Existing checker validates generated inventory | `governance/compat/check_skill_control_plane_inventory.py` | source | `check` | Skill Control Plane checker | RUNTIME_BEHAVIOR | ACCEPT |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | single reviewer/closer covering dispatch, implementation, review, and closure |
| baseHeadFor(phase) | `dispatchBaseHead=0ddf5bdf`; `executionBaseHead=0ddf5bdf`; `closureBaseHead=0ddf5bdf` |
| changedSetScope(phase) | selection standard, source profiles, generated inventory, generator, CLI, tests, baseline, work order, and completion review |
| traceScope(phase, actor) | work-order trace covers direct implementation; completion review trace covers reviewer closure |
| commitOwner(phase) | reviewer/closer owns material commit; reviewer/closer owns any follow-up session-sync commit |
| crossBatchIsolation | no package lifecycle mutation, package conversion, provider/live proof, Web page, MCP server, public-sync, or session-sync in material commit |
| nextMoveSurfaceHandling | update after material commit only if mode or next allowed move changes |
| nextMoveSurfaces | active session state, front door, and handoff |

## Execution Plan

| Step | Action | Evidence |
|---|---|---|
| 1 | add selection profile source for all package roots | JSON source file |
| 2 | merge selection profiles into generated inventory | generator and generated inventory |
| 3 | expose deterministic spec recommendation through CLI | `--spec-text` smoke |
| 4 | add focused test coverage | unittest |
| 5 | run governance gates | checker and autorun |

## Required First Reads

| Path | Action |
|---|---|
| `CVF_SESSION_MEMORY.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V29_2026-06-30.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |
| `docs/reference/agent_system_skills/CVF_SKILL_CONTROL_PLANE_INVENTORY_STANDARD.md` | READ |

## Pre-Flight Checks

| Check | Required result |
|---|---|
| `git status --short` | identify material-only changed paths |
| ADIF resolver query | no returned defects for this task tuple |
| source verification | all ACCEPT rows cite current repo source |
| generated inventory | regenerated after source profile edits |

## Write Ownership

| Path family | Owner | Boundary |
|---|---|---|
| selection standard and profiles | reviewer/closer | material only |
| generator, CLI, tests | reviewer/closer | material only |
| generated inventory | reviewer/closer | regenerated from source |
| active session surfaces | session-sync steward | separate commit if needed |

## Evidence Requirements

| Requirement | Evidence |
|---|---|
| profile coverage | 24 selection-profiled packages in summary |
| missing-profile guard | focused unittest |
| spec recommendation | CLI smoke output |
| generated drift guard | `check_skill_control_plane_inventory.py --enforce` |
| claim boundary | trace tables and completion review |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex reviewer/closer role |
| Provider or surface | local workspace |
| Session or invocation | SCPL-T2 skill selection guidance, 2026-06-30 |
| Working directory | repository root |
| Command or tool surface | source reads, apply_patch, generator, checker, CLI smoke, governance gates |
| Target paths | `docs/reference/agent_system_skills/CVF_SKILL_SELECTION_GUIDANCE_STANDARD.md`; `docs/reference/agent_system_skills/control_plane/source/skill-selection-profiles.json`; `docs/reference/agent_system_skills/control_plane/generated/skill-inventory.json`; `governance/compat/generate_skill_control_plane_inventory.py`; `governance/compat/run_skill_control_plane_inventory.py`; `governance/compat/test_skill_control_plane_inventory.py`; `docs/baselines/CVF_GC018_SCPL_T2_SKILL_SELECTION_GUIDANCE_2026-06-30.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_SCPL_T2_SKILL_SELECTION_GUIDANCE_2026-06-30.md`; `docs/reviews/CVF_SCPL_T2_SKILL_SELECTION_GUIDANCE_COMPLETION_2026-06-30.md` |
| Allowed scope source | operator request to classify package skills by domain and spec-selection guidance so users and agents choose correct skills |
| Before status evidence | SCPL-T1 inventory classified lifecycle/runtime surfaces but did not include domain and spec-selection guidance |
| After status evidence | selection profile source, inventory projection, CLI spec recommendation, and tests added |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | package-skill selection guidance only |
| Claim boundary | no package promotion, runtime/provider call, Web page, MCP server, public-sync, or production action authority |
| Agent type | reviewer/closer |
| Invocation ID | `scpl-t2-skill-selection-guidance-2026-06-30` |
| Expected manifest | `docs/reference/agent_system_skills/CVF_SKILL_SELECTION_GUIDANCE_STANDARD.md`; `docs/reference/agent_system_skills/control_plane/source/skill-selection-profiles.json`; `docs/reference/agent_system_skills/control_plane/generated/skill-inventory.json`; `governance/compat/generate_skill_control_plane_inventory.py`; `governance/compat/run_skill_control_plane_inventory.py`; `governance/compat/test_skill_control_plane_inventory.py`; `docs/baselines/CVF_GC018_SCPL_T2_SKILL_SELECTION_GUIDANCE_2026-06-30.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_SCPL_T2_SKILL_SELECTION_GUIDANCE_2026-06-30.md`; `docs/reviews/CVF_SCPL_T2_SKILL_SELECTION_GUIDANCE_COMPLETION_2026-06-30.md` |
| Actual changed set | `docs/reference/agent_system_skills/CVF_SKILL_SELECTION_GUIDANCE_STANDARD.md`; `docs/reference/agent_system_skills/control_plane/source/skill-selection-profiles.json`; `docs/reference/agent_system_skills/control_plane/generated/skill-inventory.json`; `governance/compat/generate_skill_control_plane_inventory.py`; `governance/compat/run_skill_control_plane_inventory.py`; `governance/compat/test_skill_control_plane_inventory.py`; `docs/baselines/CVF_GC018_SCPL_T2_SKILL_SELECTION_GUIDANCE_2026-06-30.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_SCPL_T2_SKILL_SELECTION_GUIDANCE_2026-06-30.md`; `docs/reviews/CVF_SCPL_T2_SKILL_SELECTION_GUIDANCE_COMPLETION_2026-06-30.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## CVF Skill Usage Receipt Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| CVF skill id | N/A with reason: no CVF runtime package body was invoked |
| Package root | N/A with reason: inventory reads package metadata only |
| Invocation context | SCPL-T2 selection guidance generation and CLI recommendation smoke |
| Receipt evidence | N/A with reason: no package usage receipt required |
| Output consumed by CVF | N/A with reason: no CVF skill output consumed |
| Truth packet or source path | `docs/reference/agent_system_skills/control_plane/source/skill-selection-profiles.json` |
| Authority boundary | selection guidance does not activate, invoke, or promote any package skill |

## External Provider Skill Usage Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| Provider skill name | N/A with reason: no external/provider-owned skill output was consumed |
| Provider owner | N/A with reason: no provider-owned skill output consumed |
| Invocation context | SCPL-T2 selection guidance and deterministic CLI smoke |
| Output consumed by CVF | N/A with reason: no provider skill output consumed |
| CVF source-of-truth promotion path | N/A with reason: no provider skill output promoted |
| Evidence artifact | this work order and paired completion review |
| Authority boundary | provider skills remain external/provider runtime skills, non-CVF authority |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | source-verify and convert into CVF-owned guard/read-model work |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `docs/reference/agent_system_skills/` and `governance/compat/` |
| Disposition | ADAPTED_WITH_CVF_AUTHORITY |
| Claim boundary | operator selection-guidance requirement converted into CVF-owned profile source, generated inventory, CLI, and tests |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance control-plane work only; no public-sync batch is
authorized.

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | all 24 package roots have a selection profile | CLI summary reports 24 selection-profiled packages |
| AC2 | inventory projects selection profiles | generated inventory includes `selection` fields |
| AC3 | checker fails on missing package selection profile | focused unittest |
| AC4 | CLI recommends skills from spec text | CLI smoke with security spec |
| AC5 | generated inventory has no drift | `check_skill_control_plane_inventory.py --enforce` PASS |

## Review Gate

Reviewer/closer must run focused tests, generator, inventory checker, and
relevant governance gates before committing material paths.

## Closure Checklist

- [x] selection profile source added
- [x] inventory regenerated
- [x] CLI recommendation smoke passed
- [x] focused tests passed
- [x] checker passed
- [x] no runtime/provider/live claim made

## Return-To-Orchestrator Conditions

Return if checker drift cannot be resolved, if a package profile requires a
domain not covered by the standard, or if runtime/provider behavior becomes
necessary.

## Operator Checkpoint

N/A with reason: operator authorized proceeding directly.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_SCPL_T2_SKILL_SELECTION_GUIDANCE_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_SCPL_T2_SKILL_SELECTION_GUIDANCE_COMPLETION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | N/A with reason: operator-directed follow-on to SCPL-T1, not a roadmap status edit | no roadmap path changed | N/A with reason |
| Registry JSON | `docs/reference/agent_system_skills/control_plane/source/skill-selection-profiles.json` | 24 profiles | PASS |
| Registry Markdown | `docs/reference/agent_system_skills/CVF_SKILL_SELECTION_GUIDANCE_STANDARD.md` | active reference standard | PASS |
| External evidence digest | N/A with reason: no external/provider evidence consumed | no digest required | N/A with reason |
| System loop interlock | N/A with reason: no system-loop runtime loop change | N/A with reason | PASS |
| Session continuity | N/A with reason: material commit first; session-sync handled separately if needed | active session gate after commit | PASS |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| SCPL-T2-Q1 | `docs/reference/agent_system_skills/control_plane/generated/skill-inventory.json` | `summary.selectionProfiledPackages` | `24` | `24` | PASS |
| SCPL-T2-Q2 | `docs/reference/agent_system_skills/control_plane/generated/skill-inventory.json` | `summary.crossSurfaceDriftViolationCount` | `0` | `0` | PASS |
| SCPL-T2-Q3 | CLI smoke output | top recommendation | `cvf-engineering-security-hardening` | `cvf-engineering-security-hardening` | PASS |

## Claim Boundary

This work order closes selection guidance only. It does not authorize package
promotion, package body invocation, provider/live calls, Web UI, MCP server,
public-sync, or production readiness.
