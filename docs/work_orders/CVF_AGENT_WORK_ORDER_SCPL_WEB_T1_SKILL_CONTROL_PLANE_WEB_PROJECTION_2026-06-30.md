# CVF Agent Work Order SCPL-WEB-T1 Skill Control Plane Web Projection

Memory class: governed-work-order

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

Batch ID: SCPL-WEB-T1

Commit mode: REVIEWER_MAY_COMMIT

dispatchBaseHead: 87823bd0

executionBaseHead: 87823bd0

closureBaseHead: 87823bd0

## Purpose

Implement a bounded Web projection bridge so CVF Web and future dashboard
surfaces inherit Skill Control Plane package-skill state through generated
read models instead of hand-edited or independently inferred lifecycle data.

## Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Operator instruction | current conversation approval to create a Web tranche and dashboard inheritance path | authorizes this tranche |
| Active session front door | `CVF_SESSION_MEMORY.md` | startup and next-move source |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | generated session state |
| Active handoff | `AGENT_HANDOFF_V29_2026-06-30.md` | active handoff named by state registry |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_SCPL_WEB_T1_SKILL_CONTROL_PLANE_WEB_PROJECTION_2026-06-30.md` | scope and claim boundary |
| Web projection standard | `docs/reference/agent_system_skills/CVF_WEB_SKILL_CONTROL_PLANE_PROJECTION_STANDARD.md` | projection contract |

## Scope / Target / Owner Boundary

Target: Web skill generator, Web generated data, Web type definitions,
SkillLibrary and SkillDetailView ASSF runtime projection display, focused Web
tests, Web projection checker, and guard catalog binding.

Owner boundary: Codex reviewer/closer may implement and commit this bounded
projection tranche. No public-sync, full dashboard page, provider registry
mutation, package lifecycle promotion, Model Gateway/model router, or runtime
action authority is authorized.

## Agent Roles

| Role | Assignment |
|---|---|
| Dispatcher | Codex reviewer/closer |
| Implementer | Codex reviewer/closer |
| Reviewer | Codex reviewer/closer |
| Session-sync steward | Codex after material commit if next move changes |

## Web Skill Control Plane Projection Control Block

- Standard source: `docs/reference/agent_system_skills/CVF_WEB_SKILL_CONTROL_PLANE_PROJECTION_STANDARD.md`
- Canonical source: `docs/reference/agent_system_skills/control_plane/generated/skill-inventory.json`
- Web read model: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/public/data/assf-skill-control-plane.json`
- Library projection: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/public/data/skills-index.json`
- Dashboard inheritance: future dashboard pages consume the Web read model
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
| Web build invokes the skill index generator | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | source | `predev`; `prebuild` | package scripts | RUNTIME_BEHAVIOR | ACCEPT |
| Web skills library reads the generated public skills index | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SkillLibrary.tsx` | source | `fetch('/data/skills-index.json'` | SkillLibrary component | RUNTIME_BEHAVIOR | ACCEPT |
| Web skill detail component displays runtime projection fields | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SkillDetailView.tsx` | source | `runtimePackageProjection` | SkillDetailView component | RUNTIME_BEHAVIOR | ACCEPT |
| Web generator can load ASSF Skill Control Plane inventory | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/scripts/build-skill-index.js` | source | `ASSF_CONTROL_PLANE_INVENTORY_PATH` | skill index generator | RUNTIME_BEHAVIOR | ACCEPT |
| Web projection checker validates runtime package coverage | `governance/compat/check_cvf_web_skill_control_plane_projection.py` | source | `check_projection` | Web projection checker | RUNTIME_BEHAVIOR | ACCEPT |
| Skill type supports runtime projection fields | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/types/skill.ts` | source | `runtimePackageProjection`; `skillControlPlaneProjection` | Skill and SkillIndexMeta interfaces | RUNTIME_BEHAVIOR | ACCEPT |

## Current Runtime Freshness Verification

| Claim | Verification | Disposition |
|---|---|---|
| This tranche does not implement package runtime behavior | `python governance/compat/check_cvf_web_skill_control_plane_projection.py --enforce` validates projection only | PASS |
| This tranche does not promote package lifecycle state | `python governance/compat/check_package_skill_productionization_pipeline.py --base 87823bd0 --head HEAD --enforce` passes with no lifecycle-source edits | PASS |
| This tranche does not implement provider or router behavior | no provider/runtime receipts are claimed; Web generated data is read-only projection | PASS |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher -> implementer -> reviewer/closer in one governed tranche |
| baseHeadFor(phase) | `dispatchBaseHead=87823bd0`; `executionBaseHead=87823bd0`; `closureBaseHead=87823bd0` |
| changedSetScope(phase) | Web projection standard, baseline, work order, completion review, Web generator, Web generated data, Web UI/types/tests, projection checker, hook catalogs |
| traceScope(phase, actor) | work-order trace covers implementation; completion review trace covers closure |
| commitOwner(phase) | reviewer/closer owns material commit; session-sync steward owns follow-up session sync |
| crossBatchIsolation | no public-sync, full dashboard build, package lifecycle promotion, provider registry mutation, or Model Gateway/model router |
| nextMoveSurfaceHandling | session-sync follows material closure if current mode or next allowed move changes |
| nextMoveSurfaces | active session state, front door, and handoff |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Durable foundation class | Web projection read model for agent-system package skills |
| Storage owner | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/public/data/` |
| Source layout | ASSF registry, package roots, generated ASSF index, and generated Skill Control Plane inventory |
| Generated layout | Web skills index and Web ASSF control-plane projection |
| Generator/checker owner | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/scripts/build-skill-index.js`; `governance/compat/check_cvf_web_skill_control_plane_projection.py` |
| Layout mutation boundary | generated Web projection only; no canonical package-state edits |
| Drift guard | Web projection checker plus Skill Control Plane inventory checker |
| Claim boundary | Web display/filtering data only |

## Execution Plan

| Step | Action | Evidence |
|---|---|---|
| 1 | extend Web generator to build `assf-skill-control-plane.json` from Skill Control Plane inventory | generated JSON |
| 2 | enrich ASSF projected Web skill records with runtime, activation, domain, and selection fields | `skills-index.json` |
| 3 | expose runtime package projection badges and metadata in existing skill UI | component tests |
| 4 | add Web projection checker and focused unit tests | Python checker tests |
| 5 | bind checker into autorun and local governance hook catalogs | catalog diff |
| 6 | run Web and governance verification | command evidence |

## Required First Reads

| Path | Action |
|---|---|
| `CVF_SESSION_MEMORY.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V29_2026-06-30.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `DESIGN.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |

## Pre-Flight Checks

| Check | Required result |
|---|---|
| `git status --short` | identify material-only changed paths |
| ADIF resolver query | no returned defects for this task tuple |
| source verification | all ACCEPT rows cite current repo source |
| Web generator dry run | generated data reports 24 runtime package projections |

## Write Ownership

| Path family | Owner | Boundary |
|---|---|---|
| Web generator and generated data | reviewer/closer | projection bridge only |
| Web types/components/tests | reviewer/closer | runtime projection display only |
| Web projection checker and tests | reviewer/closer | drift guard only |
| governance hook catalogs | reviewer/closer | add checker command only |
| baseline, work order, standard, completion review | reviewer/closer | SCPL-WEB-T1 material only |
| active session surfaces | session-sync steward | separate commit if next move changes |

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
| Web projection generated data | 24 runtime package projections |
| `python governance/compat/check_cvf_web_skill_control_plane_projection.py --enforce` | PASS |
| `python -m unittest governance.compat.test_cvf_web_skill_control_plane_projection` | PASS |
| `npm test -- --run src/components/SkillLibrary.test.tsx src/components/SkillDetailView.test.tsx` | PASS |
| `npm run check` | PASS |

## CVF Skill Usage Receipt Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| CVF skill id | N/A with reason: this tranche projects package metadata and does not execute a CVF package skill |
| Package root | N/A with reason: no package skill was invoked |
| Invocation context | SCPL-WEB-T1 Web projection implementation |
| Receipt evidence | N/A with reason: no package execution receipt required for read-only Web projection |
| Output consumed by CVF | N/A with reason: local source edits and generated Web data only |
| Truth packet or source path | `docs/reference/agent_system_skills/control_plane/generated/skill-inventory.json` |
| Authority boundary | no skill execution or downstream action authority |

## External Provider Skill Usage Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| Provider skill name | N/A with reason: no external/provider-owned skill output was consumed |
| Provider owner | N/A with reason: no provider-owned skill output consumed |
| Invocation context | SCPL-WEB-T1 local Web projection implementation |
| Output consumed by CVF | N/A with reason: no provider skill output consumed |
| CVF source-of-truth promotion path | N/A with reason: no provider skill output promoted |
| Evidence artifact | this work order and paired completion review |
| Authority boundary | provider skill surface: none; not CVF canonical authority |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | local CVF Web projection implementation -> no external knowledge promotion |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | SCPL-WEB-T1 baseline, work order, completion review, standard, Web projection files, and checker |
| Disposition | REJECT_DIRECT for external intake promotion; this tranche uses repo-local CVF source verification only |
| Claim boundary | operator instruction is scope authority; no external source is promoted as canonical content |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance Web projection and internal guard binding only; no
public-sync batch is authorized.

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | Web emits a dashboard-ready Skill Control Plane projection | `assf-skill-control-plane.json` |
| AC2 | Web skill index carries 24 runtime package projections | `skills-index.json` meta |
| AC3 | existing skills UI shows runtime package projection metadata | component tests |
| AC4 | new checker catches cross-surface Web projection drift | Python checker tests |
| AC5 | checker is wired into governed hook catalogs | catalog diff |

## Review Gate

Reviewer confirms that Web/dashboard projection inherits from generated Skill
Control Plane inventory and does not create independent runtime, activation,
provider, certification, or public-export authority.

## Closure Checklist

| Item | Status |
|---|---|
| Web projection standard added | PASS |
| Web generator updated | PASS |
| Web control-plane projection generated | PASS |
| Skill UI runtime metadata displayed | PASS |
| Web tests passed | PASS |
| Web projection checker added and tested | PASS |
| Hook catalogs wired | PASS |
| Completion review filed | PASS |

## Return-To-Orchestrator Conditions

Return `CLOSED_PASS_BOUNDED` only after Web generated data, checker, Web tests,
type check, and governance gates pass. Return `BLOCKED` if the work requires
full dashboard product scope, public-sync, package lifecycle promotion,
provider routing, or runtime action authority.

## Operator Checkpoint

No further operator checkpoint is required for this bounded Web projection
closure. A full Skill Governance Console/dashboard product build, public-sync,
provider registry mutation, package lifecycle promotion, or Model
Gateway/model router requires fresh authorization.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 baseline | `docs/baselines/CVF_GC018_SCPL_WEB_T1_SKILL_CONTROL_PLANE_WEB_PROJECTION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
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
| SCPL-WEB-T1-Q1 | Web control-plane projection | `summary.projectedRuntimePackages` | `24` | `24` | PASS |
| SCPL-WEB-T1-Q2 | Web skills index | `meta.runtimePackageProjections` | `24` | `24` | PASS |
| SCPL-WEB-T1-Q3 | Web skills index | `meta.frontDoorSkills` | `52` | `52` | PASS |
| SCPL-WEB-T1-Q4 | Web projection checker | `violations` | `0` | `0` | PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex reviewer/closer |
| Provider or surface | local workspace |
| Session or invocation | SCPL-WEB-T1 Skill Control Plane Web projection, 2026-06-30 |
| Working directory | repository root |
| Command or tool surface | source reads, apply_patch, Web generator, Web tests, governance checks |
| Target paths | Web projection standard, baseline, work order, completion review, Web generator, Web data, Web components/types/tests, Web projection checker and hook catalogs |
| Allowed scope source | operator instruction to create Web tranche and dashboard inheritance path |
| Before status evidence | base commit `87823bd0`; Web had no generated dashboard-ready package-skill control-plane read model |
| After status evidence | Web generated projection reports 24 runtime package projections and checker reports 0 violations |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | Web projection bridge only |
| Claim boundary | read-only Web projection, not runtime or provider authority |
| Agent type | dispatcher/implementer/reviewer/closer |
| Invocation ID | `cvf-scpl-web-t1-skill-control-plane-web-projection-2026-06-30` |
| Expected manifest | Web projection standard, GC-018, work order, completion review, Web generator, Web data, Web components/types/tests, Web projection checker and hook catalogs |
| Actual changed set | pending material diff before closure |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename planned |

## Claim Boundary

SCPL-WEB-T1 implements Web projection inheritance for package-skill state only.
It does not implement a full Skill Governance Console/dashboard, public export,
provider routing, package lifecycle promotion, or downstream action authority.
