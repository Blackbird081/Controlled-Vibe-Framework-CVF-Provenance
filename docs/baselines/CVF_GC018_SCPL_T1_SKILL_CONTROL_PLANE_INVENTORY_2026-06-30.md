# CVF GC-018: SCPL-T1 Skill Control Plane Inventory

Memory class: governed-baseline

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

Batch ID: SCPL-T1

dispatchBaseHead: c8ed6a9a

## Purpose

Add the first Skill Control Plane / Inventory Reconciliation layer so CVF can
scale skills without losing track of which surface is canonical metadata,
package body candidate, runtime eligible, activation-ready, adapter-ready, Web
projection, or external-provider-only.

## Decision / Baseline

Decision: implement SCPL-T1 as a bounded generated inventory, CLI readout, and
drift checker before any further package-skill scale-up.

## Scope

IN SCOPE:

- generated Skill Control Plane inventory aggregate;
- CLI readout for quick skill lifecycle status;
- cross-surface drift checker;
- focused tests;
- autorun, reviewer-fast, pre-commit, and pre-push wiring;
- reference standard for taxonomy and claim boundary.

OUT OF SCOPE:

- remaining package promotion;
- lifecycle source mutation;
- package body loading;
- provider/live proof;
- Web page implementation;
- MCP server implementation;
- public-sync or public/prod claim.

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
| ASSF source entries are generated into skill index | `governance/compat/generate_assf_skill_index.py` | source | `load_source_entries` | ASSF skill index generator | RUNTIME_BEHAVIOR | ACCEPT |
| Runtime eligibility is no-body metadata audit | `governance/compat/run_assf_runtime_eligibility_audit.py` | source | `build_runtime_eligibility_audit` | ASSF runtime audit helper | RUNTIME_BEHAVIOR | ACCEPT |
| Active resolver emits readiness decision only | `governance/compat/run_assf_active_resolver.py` | source | `build_active_resolver_packet` | ASSF active resolver helper | RUNTIME_BEHAVIOR | ACCEPT |
| Web projection is display authority only | `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | Design Principles | `CERTIFIED_PACKAGE_PROJECTION` | ASSF Web projection contract | LITERAL_INVARIANT | ACCEPT |
| New inventory generator exists | `governance/compat/generate_skill_control_plane_inventory.py` | source | `build_inventory` | Skill Control Plane generator | RUNTIME_BEHAVIOR | ACCEPT |
| New inventory checker exists | `governance/compat/check_skill_control_plane_inventory.py` | source | `check` | Skill Control Plane checker | RUNTIME_BEHAVIOR | ACCEPT |
| New CLI readout exists | `governance/compat/run_skill_control_plane_inventory.py` | source | `main` | Skill Control Plane CLI | EXISTS | ACCEPT |

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

## Evidence

| Check | Result |
|---|---|
| `python governance/compat/generate_skill_control_plane_inventory.py --generate` | PASS |
| `python governance/compat/check_skill_control_plane_inventory.py --enforce` | PASS |
| `python governance/compat/run_skill_control_plane_inventory.py --summary-only` | PASS |
| `python governance/compat/run_skill_control_plane_inventory.py --skill-id cvf-engineering-code-review-quality` | PASS |
| `python -m unittest governance.compat.test_skill_control_plane_inventory` | PASS |
| `python -m py_compile governance/compat/generate_skill_control_plane_inventory.py governance/compat/run_skill_control_plane_inventory.py governance/compat/check_skill_control_plane_inventory.py governance/compat/test_skill_control_plane_inventory.py` | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance control-plane read model. Public export requires a
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
| SCPL-T1-INV-01 | `docs/reference/agent_system_skills/control_plane/generated/skill-inventory.json` | `$.summary.assfRegistryEntries` | `32` | `32` | PASS |
| SCPL-T1-INV-02 | `docs/reference/agent_system_skills/control_plane/generated/skill-inventory.json` | `$.summary.runtimeEligiblePackages` | `6` | `6` | PASS |
| SCPL-T1-INV-03 | `docs/reference/agent_system_skills/control_plane/generated/skill-inventory.json` | `$.summary.crossSurfaceDriftViolationCount` | `0` | `0` | PASS |

## Claim Boundary

SCPL-T1 adds a generated read model and drift guard only. It does not promote
packages, load package bodies, call providers, implement a Web page or MCP
server, public-sync, or grant production action authority.
