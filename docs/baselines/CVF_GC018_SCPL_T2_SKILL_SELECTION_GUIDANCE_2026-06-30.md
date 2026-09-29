# CVF GC-018 SCPL-T2 Skill Selection Guidance Baseline

Memory class: governed-baseline

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

Batch ID: SCPL-T2

## Purpose

Authorize a bounded Skill Control Plane enhancement that adds package-skill
domain classification and spec-to-skill selection guidance.

## Scope / Methodology

Allowed scope:

- add canonical selection profile source for the 24 package roots;
- project selection guidance into the generated Skill Control Plane inventory;
- add deterministic CLI ranking from spec text or spec file;
- extend focused tests and rerun the existing Skill Control Plane checker.

Forbidden scope:

- no package lifecycle mutation;
- no package body invocation;
- no provider/live proof;
- no Web dashboard or console UI;
- no MCP server;
- no public-sync;
- no production action authority.

## Evidence / Verification

| Evidence | Expected result |
|---|---|
| generated inventory | includes 24 selection-profiled packages |
| focused unittest | selection profile coverage and spec recommendation tests pass |
| inventory checker | no generated drift and no selection-profile drift |
| CLI spec smoke | security spec recommends `cvf-engineering-security-hardening` |

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

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Skill Control Plane inventory generator exists | `governance/compat/generate_skill_control_plane_inventory.py` | source | `build_inventory` | Skill Control Plane generator | EXISTS | ACCEPT |
| Selection profile source constant exists | `governance/compat/generate_skill_control_plane_inventory.py` | source | `SELECTION_PROFILES_PATH` | Skill Control Plane generator | EXISTS | ACCEPT |
| Selection scorer exists | `governance/compat/generate_skill_control_plane_inventory.py` | source | `recommend_skills_for_spec` | Skill Control Plane generator | RUNTIME_BEHAVIOR | ACCEPT |
| CLI spec text flag exists | `governance/compat/run_skill_control_plane_inventory.py` | source | `--spec-text` | Skill Control Plane CLI | EXISTS | ACCEPT |
| Existing checker validates generated inventory | `governance/compat/check_skill_control_plane_inventory.py` | source | `check` | Skill Control Plane checker | RUNTIME_BEHAVIOR | ACCEPT |

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | all 24 package roots have a selection profile | CLI summary reports 24 selection-profiled packages |
| AC2 | inventory projects selection profiles | generated inventory includes `selection` fields |
| AC3 | checker fails on missing package selection profile | focused unittest |
| AC4 | CLI recommends skills from spec text | CLI smoke with security spec |
| AC5 | generated inventory has no drift | `check_skill_control_plane_inventory.py --enforce` PASS |

## Decision / Baseline

SCPL-T2 is accepted as a bounded control-plane enhancement. It improves skill
selection quality but does not authorize runtime package invocation.

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

## Claim Boundary

SCPL-T2 is selection guidance only. It does not create package lifecycle
authority, runtime invocation authority, provider behavior, Web UI, MCP server,
public-sync, or production readiness.
