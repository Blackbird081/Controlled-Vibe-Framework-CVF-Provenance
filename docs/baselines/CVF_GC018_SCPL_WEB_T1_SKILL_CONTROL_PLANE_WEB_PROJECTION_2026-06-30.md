# CVF GC-018 SCPL-WEB-T1 Skill Control Plane Web Projection

Memory class: gc-018-baseline

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

Batch ID: SCPL-WEB-T1

## Purpose

Authorize a bounded Web projection tranche so CVF Web and future dashboard
surfaces inherit package-skill runtime, domain, selection, activation, and
adapter state from the Skill Control Plane.

## Baseline Facts

| Fact | Evidence |
|---|---|
| Current ASSF package roots | Skill Control Plane inventory summary reports 24 |
| Current runtime-eligible packages | Skill Control Plane inventory summary reports 24 |
| Current Web front-door skills after generator run | `skills-index.json` meta reports 52 |
| Current ASSF Web projections after generator run | `skills-index.json` meta reports 25 |
| Current runtime package Web projections after generator run | `skills-index.json` meta reports 24 |
| Current Web projection drift | `check_cvf_web_skill_control_plane_projection.py --enforce` reports 0 violations |

## Scope / Target / Owner Boundary

Allowed target: Web projection generator, Web skill type/UI display, generated
Web data, Web projection drift checker, focused tests, and hook-catalog binding.

Forbidden expansion: no full dashboard build, public-sync, provider registry
mutation, package lifecycle promotion, package body rewrite, full MCP server,
Model Gateway/model router, automatic package invocation, or runtime action
authority from Web display state.

## Web Skill Control Plane Projection Control Block

- Standard source: `docs/reference/agent_system_skills/CVF_WEB_SKILL_CONTROL_PLANE_PROJECTION_STANDARD.md`
- Canonical source: `docs/reference/agent_system_skills/control_plane/generated/skill-inventory.json`
- Web read model: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/public/data/assf-skill-control-plane.json`
- Library projection: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/public/data/skills-index.json`
- Dashboard inheritance: future dashboards consume the Web read model instead of reconstructing ASSF state
- Claim boundary: read-only projection only

## Package Skill Productionization Control Block

- SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`
- Current phase: post-production Web projection inheritance for already ACTIVE package skills
- Target lifecycle state: no package lifecycle mutation in this tranche
- Prior phase evidence: ASCP-P4-P6 material commit `687d4423`; session sync `87823bd0`
- Next forbidden skip: Web projection must not replace UAT, certification, truth packet, generated index, adapter, dry-run, or live-proof gates for package productionization
- Runtime/provider proof: N/A with reason: this tranche claims read-only Web projection, not package runtime behavior
- Claim boundary: Web projection only; no package activation or runtime action authority

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`,
lifecyclePhase=`implementation`,
surfaceSelector=`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`,
riskCeiling=`HIGH`, maxResults=`20`

Returned defects: NONE_RETURNED

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Web build runs the skill index generator before dev and build | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | source | `predev`; `prebuild` | package scripts | RUNTIME_BEHAVIOR | ACCEPT |
| Web skills library reads the public skills index | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SkillLibrary.tsx` | source | `fetch('/data/skills-index.json'` | SkillLibrary component | RUNTIME_BEHAVIOR | ACCEPT |
| Web skill detail component displays ASSF projection fields | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SkillDetailView.tsx` | source | `runtimePackageProjection` | SkillDetailView component | RUNTIME_BEHAVIOR | ACCEPT |
| Skill Control Plane inventory is the generated package-skill source | `docs/reference/agent_system_skills/control_plane/generated/skill-inventory.json` | generated source | `summary.runtimeEligiblePackages` | Skill Control Plane inventory schema | VALUE_SET | ACCEPT |
| Web projection checker validates runtime package projection drift | `governance/compat/check_cvf_web_skill_control_plane_projection.py` | source | `check_projection` | Web projection checker | RUNTIME_BEHAVIOR | ACCEPT |

## Current Runtime Freshness Verification

| Claim | Verification | Disposition |
|---|---|---|
| This tranche does not implement package runtime behavior | `python governance/compat/check_cvf_web_skill_control_plane_projection.py --enforce` validates projection only | PASS |
| This tranche does not promote package lifecycle state | `python governance/compat/check_package_skill_productionization_pipeline.py --base 87823bd0 --head HEAD --enforce` passes with no lifecycle-source edits | PASS |
| This tranche does not implement provider or router behavior | no provider/runtime receipts are claimed; Web generated data is read-only projection | PASS |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add a Web projection drift checker and
bind it into governed hook catalogs for Skill Control Plane Web projection.

Protected paths:

| Path | Reason |
|---|---|
| `governance/compat/check_cvf_web_skill_control_plane_projection.py` | add Web projection drift guard |
| `governance/compat/test_cvf_web_skill_control_plane_projection.py` | add focused checker tests |
| `governance/compat/agent_autorun_command_catalog.py` | bind guard into autorun catalog |
| `governance/compat/local_governance_hook_catalog_pre_commit.py` | bind guard into pre-commit catalog |
| `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | bind guard into reviewer-fast catalog |
| `governance/compat/local_governance_hook_catalog_pre_push.py` | bind guard into pre-push catalog |

Operator authorization: operator approved creating the Web tranche and future
dashboard inheritance path.

Rollback boundary: revert only the SCPL-WEB-T1 checker, checker test, hook
catalog bindings, Web projection files, and paired SCPL-WEB-T1 artifacts.

## Evidence Requirements

| Evidence | Required result |
|---|---|
| Web generator | writes `assf-skill-control-plane.json` and refreshes `skills-index.json` |
| Web projection checker | 0 violations |
| Web type check | `npm run check` passes |
| Web component tests | `SkillLibrary` and `SkillDetailView` tests pass |
| Focused Python test | Web projection checker tests pass |
| Claim boundary | Web read model grants no runtime or activation authority |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this baseline changes private provenance Web projection and internal
governance guards. Public-safe export requires a separate public-sync tranche.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 baseline | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_SCPL_WEB_T1_SKILL_CONTROL_PLANE_WEB_PROJECTION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_SCPL_WEB_T1_SKILL_CONTROL_PLANE_WEB_PROJECTION_COMPLETION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | N/A with reason: operator-directed Web projection tranche, not a roadmap status edit | no roadmap path changed | PASS |
| Registry JSON | N/A with reason: this tranche does not edit ASSF registry entries | no registry JSON changed | PASS |
| Registry Markdown | N/A with reason: this tranche does not edit package front-door markdown | no registry markdown changed | PASS |
| Web data projection | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/public/data/assf-skill-control-plane.json` | 24 projected runtime packages | PASS |
| Web skill index | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/public/data/skills-index.json` | 52 front-door skills and 24 runtime package projections | PASS |
| Web projection guard | `governance/compat/check_cvf_web_skill_control_plane_projection.py` | 0 violations | PASS |
| External evidence digest | Web generated projection digest | `sha256:6e21f0b391e0a7628e2636c88248d82235b31836e7fe52d898f68d40e14113a1` | PASS |
| System loop interlock | no action authority from Web projection | read-only dashboard contract | PASS |
| Session continuity | N/A with reason: material commit first; session-sync handled separately if next move changes | active session gate after commit | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| SCPL-WEB-T1-B-Q1 | Web control-plane projection | `summary.projectedRuntimePackages` | `24` | `24` | PASS |
| SCPL-WEB-T1-B-Q2 | Web skills index | `meta.runtimePackageProjections` | `24` | `24` | PASS |
| SCPL-WEB-T1-B-Q3 | Web skills index | `meta.frontDoorSkills` | `52` | `52` | PASS |
| SCPL-WEB-T1-B-Q4 | Web projection checker | `violations` | `0` | `0` | PASS |

## Claim Boundary

SCPL-WEB-T1 authorizes Web projection and dashboard-read-model inheritance
only. It does not authorize dashboard product expansion, runtime activation,
provider routing, public export, or downstream action authority.
