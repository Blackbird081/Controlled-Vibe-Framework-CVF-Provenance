# CVF Agent Work Order: SCPL-T1 Skill Control Plane Inventory

Memory class: governed-work-order

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

Batch ID: SCPL-T1

Commit mode: REVIEWER_MAY_COMMIT

dispatchBaseHead: c8ed6a9a

executionBaseHead: c8ed6a9a

closureBaseHead: c8ed6a9a

## Purpose

Implement a bounded Skill Control Plane inventory so agents can inspect skill
lifecycle position before scaling package skills.

## Authority Chain

| Authority | Path / Evidence |
|---|---|
| Operator request | current chat request for Skill Control Plane / Inventory Reconciliation |
| Active session | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| Package SOP | `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md` |
| Web projection boundary | `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` |
| New standard | `docs/reference/agent_system_skills/CVF_SKILL_CONTROL_PLANE_INVENTORY_STANDARD.md` |

## Agent Roles

| Role | Assignment |
|---|---|
| Dispatcher | Codex reviewer/closer |
| Worker | Codex reviewer/closer |
| Reviewer | Codex reviewer/closer |
| Session-sync steward | Codex reviewer/closer after material commit if needed |

## Scope / Target / Owner Boundary

Target paths:

- `docs/reference/agent_system_skills/CVF_SKILL_CONTROL_PLANE_INVENTORY_STANDARD.md`
- `docs/reference/agent_system_skills/control_plane/generated/skill-inventory.json`
- `governance/compat/generate_skill_control_plane_inventory.py`
- `governance/compat/run_skill_control_plane_inventory.py`
- `governance/compat/check_skill_control_plane_inventory.py`
- `governance/compat/test_skill_control_plane_inventory.py`
- governance hook and autorun catalogs

Owner boundary: reviewer/closer may implement and commit this bounded guard
tranche. No package lifecycle mutation, package body read, provider/live proof,
Web page, MCP server, public-sync, or production claim is authorized.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`guard`, role=`worker`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

## Package Skill Productionization Control Block

- SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`
- Current phase: control-plane inventory and drift guard
- Target lifecycle state: no package lifecycle mutation
- Prior phase evidence: PKGSOP-T2 guard closed at `eaadc5ed`
- Next forbidden skip: no package promotion, ACTIVE claim, runtime/provider proof, public/prod claim, or adapter claim may bypass the SOP
- Runtime/provider proof: N/A with reason: read-model and checker only; no runtime/provider governance behavior claimed
- Claim boundary: inventory and drift guard only

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASSF generated index source loader exists | `governance/compat/generate_assf_skill_index.py` | source | `load_source_entries` | ASSF skill index generator | EXISTS | ACCEPT |
| Runtime eligibility audit source exists | `governance/compat/run_assf_runtime_eligibility_audit.py` | source | `build_runtime_eligibility_audit` | ASSF runtime audit helper | EXISTS | ACCEPT |
| Active resolver source exists | `governance/compat/run_assf_active_resolver.py` | source | `build_active_resolver_packet` | ASSF active resolver helper | EXISTS | ACCEPT |
| Web projection contract separates display from authority | `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | Design Principles | `CVF Web Projects Packages` | ASSF Web projection contract | LITERAL_INVARIANT | ACCEPT |
| Skill Control Plane generator added | `governance/compat/generate_skill_control_plane_inventory.py` | source | `build_inventory` | Skill Control Plane generator | RUNTIME_BEHAVIOR | ACCEPT |
| Skill Control Plane checker added | `governance/compat/check_skill_control_plane_inventory.py` | source | `check` | Skill Control Plane checker | RUNTIME_BEHAVIOR | ACCEPT |
| Skill Control Plane CLI added | `governance/compat/run_skill_control_plane_inventory.py` | source | `main` | Skill Control Plane CLI | EXISTS | ACCEPT |

## Required First Reads

| Path | Action |
|---|---|
| `CVF_SESSION_MEMORY.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V28_2026-06-30.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |
| `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | READ |
| `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md` | READ |

## Roadmap-To-Work-Order Trace Matrix

| Operator need | Work order action | Evidence |
|---|---|---|
| Central Skill Inventory | generate `skill-inventory.json` from source surfaces | generator and generated aggregate |
| Skill Lifecycle Dashboard / CLI | add CLI readout | `run_skill_control_plane_inventory.py` |
| Cross-Surface Drift Guard | add checker and hook wiring | `check_skill_control_plane_inventory.py` and catalogs |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | single Codex reviewer/closer covering dispatch, implementation, review, and closure |
| baseHeadFor(phase) | `dispatchBaseHead=c8ed6a9a`; `executionBaseHead=c8ed6a9a`; `closureBaseHead=c8ed6a9a` |
| changedSetScope(phase) | material paths only; session-sync later if needed |
| traceScope(phase, actor) | work-order trace covers direct implementation; completion review trace covers reviewer closure |
| commitOwner(phase) | Codex reviewer/closer owns material commit; Codex owns any follow-up session-sync commit |
| crossBatchIsolation | no lifecycle mutation, package conversion, provider/live, Web page, MCP server, public-sync, or session-sync in material commit |
| nextMoveSurfaceHandling | update after material commit only if mode or next allowed move changes |
| nextMoveSurfaces | active session state, front door, and handoff |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Generated aggregate | `docs/reference/agent_system_skills/control_plane/generated/skill-inventory.json` |
| Source layout | current ASSF registry entries, package roots, truth index, Web projection JSON, and template map |
| Generator | `governance/compat/generate_skill_control_plane_inventory.py` |
| Drift checker | `governance/compat/check_skill_control_plane_inventory.py` |
| Runtime/provider boundary | no provider/live call and no package body read |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add Skill Control Plane inventory generator,
CLI readout, drift checker, focused tests, and governance catalog wiring.

Protected paths:

- `governance/compat/generate_skill_control_plane_inventory.py`
- `governance/compat/run_skill_control_plane_inventory.py`
- `governance/compat/check_skill_control_plane_inventory.py`
- `governance/compat/test_skill_control_plane_inventory.py`
- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_pre_push.py`

Operator authorization: operator requested a unified Skill Control Plane /
Inventory Reconciliation before scaling more package skills.

Rollback boundary: revert this SCPL-T1 material commit only; do not revert
PKGSOP-T2, PKGSOP-T1, ASCP-P1-P3, package roots, truth packets, or generated
ASSF skill index unless a separate reviewer reopens those closures.

## Execution Plan

| Step | Action | Evidence |
|---|---|---|
| 1 | Build generated inventory and CLI | generator/CLI files |
| 2 | Add drift checker and tests | checker/test files |
| 3 | Wire checker into gates | catalog diffs |
| 4 | Generate inventory | generated JSON |
| 5 | Run focused tests and governance gates | command evidence |

## Evidence Requirements

- generated inventory check must pass;
- CLI summary and one skill readout must pass;
- focused unit tests must pass;
- py_compile must pass;
- autorun pre-dispatch and pre-implementation must pass;
- commit steward must pass before commit.

## Pre-Flight Checks

| Check | Status |
|---|---|
| `git status --short` before implementation | PASS |
| ADIF disclosure query | PASS |
| Source facts verified against repo files | PASS |

## Write Ownership

Reviewer/closer owns all SCPL-T1 material files in this work order. No other
agent-owned changes are reverted or overwritten.

## Review Gate

Reviewer must confirm generated inventory drift is zero, focused tests pass,
and hook wiring includes the new checker before commit.

## Closure Checklist

| Item | Status |
|---|---|
| Generator added | PASS |
| CLI readout added | PASS |
| Checker added and wired | PASS |
| Generated aggregate created | PASS |
| Tests pass | PASS |
| No runtime/provider/Web/MCP/public expansion | PASS |

## Return-To-Orchestrator Conditions

Return to operator if implementation would require package lifecycle mutation,
provider/live proof, Web page build, MCP server runtime, public-sync, or
production action authority.

## Operator Checkpoint

Operator checkpoint is not required for SCPL-T1 because the operator requested
the control-plane inventory before package scale-up and this tranche stays
inside read-model/checker scope.

## Acceptance Criteria

| ID | Criterion | Status |
|---|---|---|
| AC1 | Inventory classifies ASSF registry, package root, runtime, resolver, CLI/MCP, Web, and provider-boundary surfaces | PASS |
| AC2 | CLI answers where a skill is in lifecycle | PASS |
| AC3 | Drift checker blocks generated drift and Web/registry certification mismatch | PASS |
| AC4 | Checker is wired into autorun and local hook catalogs | PASS |
| AC5 | No package lifecycle, provider/live, Web page, MCP server, public-sync, or production action authority added | PASS |

## Current Runtime Freshness Verification

| Runtime/source claim | Evidence | Disposition |
|---|---|---|
| No provider/live proof claimed | no live command run | PASS |
| No package body read claimed | generator reads metadata/projection JSON only | PASS |
| Existing Model Gateway provider surfaces | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and `PROVIDER_CAPABILITY_REGISTRY` are accounted-for, out-of-scope, and untouched | PASS |

## CVF Skill Usage Receipt Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| CVF skill id | N/A with reason: no CVF runtime package body was invoked |
| Package root | N/A with reason: inventory reads package metadata only |
| Invocation context | SCPL-T1 inventory and drift guard generation |
| Receipt evidence | N/A with reason: no package usage receipt required |
| Output consumed by CVF | N/A with reason: no CVF skill output consumed |
| Truth packet or source path | `docs/reference/agent_system_skills/control_plane/generated/skill-inventory.json` |
| Authority boundary | inventory read model does not activate, invoke, or promote any package skill |

## External Provider Skill Usage Trace

| Field | Value |
|---|---|
| Usage disposition | NOT_USED_WITH_REASON |
| Provider skill name | N/A with reason: no external/provider-owned skill output was consumed |
| Provider owner | N/A with reason: no provider-owned skill output consumed |
| Invocation context | SCPL-T1 taxonomy boundary and inventory read-model work |
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
| Claim boundary | operator taxonomy proposal converted into CVF-owned source-verified inventory/checker; external/provider skills remain non-CVF authority |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance control-plane read model. Public export requires
separate public-sync authorization and redaction decision.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Generated inventory | `docs/reference/agent_system_skills/control_plane/generated/skill-inventory.json` | `$.summary.assfRegistryEntries=32`; `$.summary.crossSurfaceDriftViolationCount=0` | PASS |
| Checker | `governance/compat/check_skill_control_plane_inventory.py` | command exits 0 with `Violations: 0` | PASS |
| CLI readout | `governance/compat/run_skill_control_plane_inventory.py` | summary and skill-id commands exit 0 | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_SCPL_T1_SKILL_CONTROL_PLANE_INVENTORY_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_SCPL_T1_SKILL_CONTROL_PLANE_INVENTORY_COMPLETION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | N/A with reason: operator requested direct bounded control-plane tranche, not a roadmap closeout | no roadmap status changed | PASS |
| Registry JSON | `docs/reference/agent_system_skills/control_plane/generated/skill-inventory.json` | generated aggregate exists and checker passes | PASS |
| Registry Markdown | `docs/reference/agent_system_skills/CVF_SKILL_CONTROL_PLANE_INVENTORY_STANDARD.md` | reference standard exists | PASS |
| External evidence digest | N/A with reason: no external/provider evidence consumed | no digest required | N/A with reason |
| System loop interlock | N/A with reason: no system-loop registry change | system-loop checker in autorun | PASS |
| Session continuity | N/A with reason: material commit first; session-sync handled separately if needed | active session gate after commit | PASS |
| Runtime/provider proof | N/A with reason: no runtime/provider governance behavior claimed | no live command run | PASS |
| Public export | N/A with reason: private provenance control-plane read model | `DEFERRED_PRIVATE_ONLY` | PASS |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| SCPL-T1-WO-01 | `docs/reference/agent_system_skills/control_plane/generated/skill-inventory.json` | `$.summary.assfRegistryEntries` | `32` | `32` | PASS |
| SCPL-T1-WO-02 | `docs/reference/agent_system_skills/control_plane/generated/skill-inventory.json` | `$.summary.runtimeEligiblePackages` | `6` | `6` | PASS |
| SCPL-T1-WO-03 | `docs/reference/agent_system_skills/control_plane/generated/skill-inventory.json` | `$.summary.crossSurfaceDriftViolationCount` | `0` | `0` | PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex reviewer/closer role |
| Provider or surface | local workspace |
| Session or invocation | SCPL-T1 skill control plane inventory, 2026-06-30 |
| Working directory | repository root |
| Command or tool surface | source reads, apply_patch, generator, checker, governance gates |
| Target paths | SCPL-T1 material paths |
| Allowed scope source | operator request for unified Skill Control Plane / Inventory Reconciliation before scaling more package skills |
| Before status evidence | PKGSOP-T2 closed at `eaadc5ed`; no unified inventory read model existed |
| After status evidence | material paths pending commit |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | generated read model and checker only |
| Claim boundary | no package promotion, runtime/provider call, Web page, MCP server, public-sync, or production action authority |
| Agent type | reviewer/closer |
| Invocation ID | `scpl-t1-skill-control-plane-inventory-2026-06-30` |
| Expected manifest | `docs/reference/agent_system_skills/CVF_SKILL_CONTROL_PLANE_INVENTORY_STANDARD.md`; `docs/reference/agent_system_skills/control_plane/generated/skill-inventory.json`; `governance/compat/generate_skill_control_plane_inventory.py`; `governance/compat/run_skill_control_plane_inventory.py`; `governance/compat/check_skill_control_plane_inventory.py`; `governance/compat/test_skill_control_plane_inventory.py`; `governance/compat/agent_autorun_command_catalog.py`; `governance/compat/local_governance_hook_catalog_reviewer_fast.py`; `governance/compat/local_governance_hook_catalog_pre_commit.py`; `governance/compat/local_governance_hook_catalog_pre_push.py` |
| Actual changed set | material commit steward will verify before commit |
| Manifest delta | MATCH_AFTER_COMMIT_REVIEW |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This work order authorizes SCPL-T1 read-model and checker work only. It does
not authorize package promotion, runtime/provider calls, Web page build, MCP
server, public-sync, or production action authority.
