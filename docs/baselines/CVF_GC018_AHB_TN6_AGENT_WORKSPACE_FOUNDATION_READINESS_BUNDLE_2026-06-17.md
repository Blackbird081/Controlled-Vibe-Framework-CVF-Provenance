# CVF GC-018 - AHB-Tn.6 Agent Workspace Foundation Readiness Bundle

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: gc018

Date: 2026-06-17

Batch ID: AHB-Tn.6

Owner: Codex

executionBaseHead: `736fef37`

## Purpose

Authorize one combined pre-runtime workspace foundation bundle that absorbs the
useful AHB-Tn.5-B and AHB-Tn.5-C option work before any workspace runtime is
built.

## Scope / Target / Owner Boundary

Target: richer workspace state lanes, item template, generated-state checker
hardening, front-door/index updates, and active state item disposition.

Owner boundary: Codex owns dispatch, implementation, review, closure, material
commit, and later session-sync. This GC-018 does not authorize workspace UI,
runtime queues, product source mutation, provider/live proof, public-sync,
registry edit, production readiness, or public readiness.

## Authority Chain

| Level | Artifact | Status |
|---|---|---|
| Operator instruction | 2026-06-17 combine useful workspace foundation tranches before runtime | ACCEPTED |
| AHB-Tn.5 predecessor | `docs/reviews/CVF_AHB_TN5_AGENT_WORKSPACE_OPTION_READINESS_COMPLETION_2026-06-17.md` | PREDECESSOR_SATISFIED |
| Workspace front door | `docs/reference/agent_workspace/README.md` | ACTIVE_INDEX |
| Topology contract | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` | ACTIVE_CONTRACT |
| Generated workspace state | `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json` | ACTIVE_FOUNDATION |

## Source / Predecessor Evidence

| Source | Evidence | Disposition |
|---|---|---|
| AHB-Tn.5 completion | `docs/reviews/CVF_AHB_TN5_AGENT_WORKSPACE_OPTION_READINESS_COMPLETION_2026-06-17.md` | PREDECESSOR_SATISFIED |
| AHB-Tn.5 option matrix | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPTION_READINESS_MATRIX.md` | SOURCE_FOR_OPTIONS |
| Existing generator | `governance/compat/generate_agent_workspace_state.py` | SOURCE_FOR_SCHEMA |
| Existing checker | `governance/compat/check_agent_workspace_state.py` | SOURCE_FOR_MACHINE_GUARD |
| Existing state items | `CVF_SESSION/agent_workspace/state/items/` | SOURCE_FOR_ACTIVE_STATE |

## Decision / Baseline / Proposed Tranche

Decision: `APPROVE_COMBINED_AHB_TN6_FOUNDATION_READINESS_BUNDLE`.

Baseline: HEAD `736fef37` after AHB-Tn.5 material and session-sync closure.

Proposed tranche: absorb AHB-Tn.5-B richer state lanes and AHB-Tn.5-C
foundation hardening into one bounded foundation bundle. Keep AHB-Tn.5-A
workspace build parked.

## Authorized Changed Set

| Path | Disposition |
|---|---|
| `AGENTS.md` | mandatory pointer update |
| `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json` | regenerated aggregate |
| `CVF_SESSION/agent_workspace/state/items/ahb-tn4-workspace-state-foundation-parked.json` | add lane fields |
| `CVF_SESSION/agent_workspace/state/items/ahb-tn5-workspace-build-option-parked.json` | add lane fields; keep parked |
| `CVF_SESSION/agent_workspace/state/items/ahb-tn5-richer-state-lanes-option-parked.json` | close as absorbed by AHB-Tn.6 |
| `CVF_SESSION/agent_workspace/state/items/ahb-tn5-foundation-hardening-option-parked.json` | close as absorbed by AHB-Tn.6 |
| `CVF_SESSION/agent_workspace/state/items/ahb-tn6-workspace-foundation-readiness-bundle-closed.json` | accepted-material item |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_LANE_TAXONOMY.md` | stable taxonomy |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_ITEM_TEMPLATE.json` | stable item template |
| `docs/reference/agent_workspace/README.md` | front-door pointer |
| `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` | design standard pointer |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` | topology field update |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPTION_READINESS_MATRIX.md` | option disposition update |
| `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | operational index update |
| `governance/compat/generate_agent_workspace_state.py` | schema hardening |
| `governance/compat/check_agent_workspace_state.py` | marker and field guard hardening |
| `governance/compat/test_agent_workspace_state.py` | focused tests |
| `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` | roadmap closure update |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN6_AGENT_WORKSPACE_FOUNDATION_READINESS_BUNDLE_FOR_CODEX_2026-06-17.md` | work order |
| `docs/reviews/CVF_AHB_TN6_AGENT_WORKSPACE_FOUNDATION_READINESS_BUNDLE_COMPLETION_2026-06-17.md` | completion review |
| `docs/baselines/CVF_GC018_AHB_TN6_AGENT_WORKSPACE_FOUNDATION_READINESS_BUNDLE_2026-06-17.md` | this baseline |

## Acceptance Criteria

| Criterion | Required evidence |
|---|---|
| Lane taxonomy exists | stable taxonomy under `docs/reference/agent_workspace/` |
| Item template exists | stable JSON template under `docs/reference/agent_workspace/` |
| Checker enforces new fields | tests cover invalid lane and invalid supersedes |
| Active state is generated | `generate_agent_workspace_state.py --check` PASS |
| Tn.5-B/C are absorbed | active state records both as `CLOSED_PASS_BOUNDED` |
| Tn.5-A remains parked | active state keeps build option parked |
| No runtime/build scope | completion records no UI/runtime/provider/public/registry paths changed |

## Evidence / Verification

| Verification item | Required command or artifact | Disposition |
|---|---|---|
| Generated aggregate alignment | `python governance/compat/generate_agent_workspace_state.py --check` | REQUIRED |
| Workspace state guard | `python governance/compat/check_agent_workspace_state.py --base 736fef37 --head HEAD --enforce` | REQUIRED |
| Workspace design guard | `python governance/compat/check_agent_workspace_design.py --base 736fef37 --head HEAD --enforce` | REQUIRED |
| Handoff boundary guard | `python governance/compat/check_agent_handoff_boundary.py --base 736fef37 --head HEAD --enforce` | REQUIRED |
| Trace manifest guard | `python governance/compat/check_agent_operation_trace.py --base 736fef37 --head HEAD --enforce` | REQUIRED |
| Focused tests | `python -m pytest governance/compat/test_agent_workspace_state.py governance/compat/test_check_agent_workspace_design.py -q` | REQUIRED |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance foundation. No public-sync batch is
authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-17 AHB-Tn.6 agent workspace foundation readiness bundle |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, pytest |
| Target paths | `AGENTS.md`; `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn4-workspace-state-foundation-parked.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn5-foundation-hardening-option-parked.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn5-richer-state-lanes-option-parked.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn5-workspace-build-option-parked.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn6-workspace-foundation-readiness-bundle-closed.json`; `docs/baselines/CVF_GC018_AHB_TN6_AGENT_WORKSPACE_FOUNDATION_READINESS_BUNDLE_2026-06-17.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPTION_READINESS_MATRIX.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_ITEM_TEMPLATE.json`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_LANE_TAXONOMY.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`; `docs/reference/agent_workspace/README.md`; `docs/reviews/CVF_AHB_TN6_AGENT_WORKSPACE_FOUNDATION_READINESS_BUNDLE_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN6_AGENT_WORKSPACE_FOUNDATION_READINESS_BUNDLE_FOR_CODEX_2026-06-17.md`; `governance/compat/check_agent_workspace_state.py`; `governance/compat/generate_agent_workspace_state.py`; `governance/compat/test_agent_workspace_state.py` |
| Allowed scope source | operator authorization to combine useful workspace foundation tranches before runtime on 2026-06-17 |
| Before status evidence | HEAD `736fef37`; clean worktree |
| After status evidence | AHB-Tn.6 material closure pending commit |
| Diff evidence | `git diff --name-status 736fef37..HEAD` |
| Approval boundary | workspace foundation readiness only |
| Claim boundary | no workspace build, runtime/provider/live/public/registry implementation claim |
| Agent type | Codex implementer/closer |
| Invocation ID | `ahb-tn6-agent-workspace-foundation-readiness-bundle-2026-06-17` |
| Expected manifest | `AGENTS.md`; `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn4-workspace-state-foundation-parked.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn5-foundation-hardening-option-parked.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn5-richer-state-lanes-option-parked.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn5-workspace-build-option-parked.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn6-workspace-foundation-readiness-bundle-closed.json`; `docs/baselines/CVF_GC018_AHB_TN6_AGENT_WORKSPACE_FOUNDATION_READINESS_BUNDLE_2026-06-17.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPTION_READINESS_MATRIX.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_ITEM_TEMPLATE.json`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_LANE_TAXONOMY.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`; `docs/reference/agent_workspace/README.md`; `docs/reviews/CVF_AHB_TN6_AGENT_WORKSPACE_FOUNDATION_READINESS_BUNDLE_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN6_AGENT_WORKSPACE_FOUNDATION_READINESS_BUNDLE_FOR_CODEX_2026-06-17.md`; `governance/compat/check_agent_workspace_state.py`; `governance/compat/generate_agent_workspace_state.py`; `governance/compat/test_agent_workspace_state.py` |
| Actual changed set | `AGENTS.md`; `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn4-workspace-state-foundation-parked.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn5-foundation-hardening-option-parked.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn5-richer-state-lanes-option-parked.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn5-workspace-build-option-parked.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn6-workspace-foundation-readiness-bundle-closed.json`; `docs/baselines/CVF_GC018_AHB_TN6_AGENT_WORKSPACE_FOUNDATION_READINESS_BUNDLE_2026-06-17.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPTION_READINESS_MATRIX.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_ITEM_TEMPLATE.json`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_LANE_TAXONOMY.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`; `docs/reference/agent_workspace/README.md`; `docs/reviews/CVF_AHB_TN6_AGENT_WORKSPACE_FOUNDATION_READINESS_BUNDLE_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN6_AGENT_WORKSPACE_FOUNDATION_READINESS_BUNDLE_FOR_CODEX_2026-06-17.md`; `governance/compat/check_agent_workspace_state.py`; `governance/compat/generate_agent_workspace_state.py`; `governance/compat/test_agent_workspace_state.py` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This baseline authorizes pre-runtime workspace foundation readiness only. It
does not build a workspace, mutate runtime/product code, run provider proof,
public-sync, edit registries, or claim production/public readiness.
