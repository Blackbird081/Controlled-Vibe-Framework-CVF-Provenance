# CVF Agent Interaction Workspace Design Standard

Memory class: FULL_RECORD

Status: ACTIVE_STANDARD

docType: reference

## Purpose

Define the bounded design requirements for the future CVF agent-interaction
workspace so future agents can prepare that workspace without weakening the
ratified Agent Handoff Contract, foundation storage discipline, or provider
memory boundary.

## Scope / Target / Owner Boundary

Target: design governance for a future dedicated workspace where multiple CVF
actors can exchange work, evidence, objections, review state, and next-move
signals.

Owner boundary: this standard authorizes analysis and design only. It does not
build the workspace, create runtime queues, edit product code, change provider
behavior, public-sync, or claim production readiness.

## Source Authority

| Source | Path | Role |
|---|---|---|
| AHB-T2 ratified contract | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | Central Core for role, phase, base-head, trace, commit, and next-move fields |
| AHB-T3 checker | `governance/compat/check_agent_handoff_boundary.py` | Machine-enforced work-order local view |
| AHB roadmap | `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` | Workspace candidate route after AHB-T3 |
| Foundation storage standard | `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` | Stable folder/index rule |
| Provider memory boundary | `AGENTS.md` | Provider-local memory is not CVF source of truth |

## Design Decision

The agent-interaction workspace must be designed as a governed coordination
surface, not as an informal chat archive or provider-local memory substitute.

The workspace design must preserve:

- Agent Handoff Contract fields as the Central Core;
- per-batch work orders, trace blocks, reviews, and session-sync records as
  Local Views;
- stable indexed foundation paths for durable workspace rules;
- dated execution/evidence paths for batch-specific receipts and reviews;
- explicit separation between design artifacts and any later runtime/product
  implementation.

## Required Workspace Design Model

Any future build work order for the agent-interaction workspace must define
these design surfaces before implementation:

| Surface | Required decision before build |
|---|---|
| Front door | Stable `docs/reference/agent_workspace/README.md` remains the first read |
| Actor lanes | Which actors may author, execute, review, close, and session-sync |
| Handoff contract fields | How `route`, `rolePattern`, `phase`, base heads, changed-set scope, trace scope, commit owner, cross-batch isolation, and next-move surfaces are represented |
| Evidence storage | Which artifacts are stable foundation records and which are dated execution evidence |
| Workspace state | Whether state is markdown-only, generated JSON, runtime-backed, or deferred |
| Guard placement | Which existing or future machine checks enforce the design before dispatch, implementation, closure, and session sync |
| Archive policy | How stale workspace records leave the active front door |
| Public boundary | Whether any workspace output may ever enter public-sync, and under which separate authorization |

## Minimum Pre-Build Control Block

A future workspace build work order must include an `Agent Workspace Design
Control Block` with:

| Field | Required content |
|---|---|
| Workspace purpose | One bounded use case, not broad collaboration infrastructure |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| Front door | `docs/reference/agent_workspace/README.md` |
| Storage class | stable foundation file, dated execution evidence, generated state, runtime source, or public-sync artifact |
| Handoff fields | concrete mapping for CF-01 through CF-09 |
| State ownership | owner for each proposed workspace state file or runtime table |
| Guard owner | existing checker or proposed machine-check candidate |
| Build boundary | explicit yes/no for runtime source, provider proof, public-sync, and registry edits |

## Folder And File Policy

Stable workspace foundation rules live under:

`docs/reference/agent_workspace/`

Dated GC-018, work orders, completion reviews, and evidence stay in their
existing execution folders:

- `docs/baselines/`
- `docs/work_orders/`
- `docs/reviews/`
- `docs/reviews/evidence/`

Do not create a workspace root, runtime queue, generated JSON aggregate, UI,
provider integration, or public-facing copy from this standard alone.

## Relationship To Existing Guards

| Guard | Relationship |
|---|---|
| `governance/compat/check_agent_handoff_boundary.py` | Enforces handoff contract evidence in changed work orders |
| `governance/compat/check_foundation_storage_layout.py` | Enforces stable folder/index discipline for durable workspace rules |
| `governance/compat/check_agent_operation_trace.py` | Enforces per-phase changed-set and trace manifest evidence |
| `governance/compat/check_finding_to_governance_learning.py` | Prevents workspace findings from staying only in provider memory |
| `governance/compat/check_next_move_freshness.py` | Prevents stale next-move surfaces after workspace-related closures |

## Machine Enforcement

Current enforcement is by existing guards only:

```powershell
python governance/compat/check_agent_handoff_boundary.py --base <baseHead> --head HEAD --enforce
python governance/compat/check_foundation_storage_layout.py --base <baseHead> --head HEAD --enforce
python governance/compat/check_agent_operation_trace.py --base <baseHead> --head HEAD --enforce
```

No dedicated `check_agent_workspace_design.py` exists yet. A future build or
implementation tranche must decide whether the `Agent Workspace Design Control
Block` needs a dedicated checker before runtime or product work begins.

## Work Order Requirement

Any future work order that proposes or builds an agent-interaction workspace
must:

- cite this standard and the agent workspace front door;
- include the Agent Handoff Contract Control Block required by AHB-T3;
- include a Foundation Storage Layout Block if it creates durable workspace
  foundation files;
- include the Agent Workspace Design Control Block above before implementation;
- state whether it is analysis-only, design-only, machine-check, runtime build,
  provider-proof, public-sync, or archive-cleanup scope.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance design. No public-sync batch is
authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-17 AHB-Tn.1 agent-interaction workspace analysis/design |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch |
| Target paths | `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` |
| Allowed scope source | operator authorization for AHB-Tn analysis/design on 2026-06-17 |
| Before status evidence | HEAD `05f3f795`; clean worktree |
| After status evidence | AHB-Tn.1 material closure pending commit |
| Diff evidence | `git diff --name-status 05f3f795..HEAD` |
| Approval boundary | bounded workspace analysis/design foundation only |
| Claim boundary | no workspace build, runtime/provider/live/public/registry implementation claim |
| Agent type | Codex implementer/closer |
| Invocation ID | `ahb-tn1-agent-interaction-workspace-analysis-design-2026-06-17` |
| Expected manifest | `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` |
| Actual changed set | `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This standard defines workspace design controls only. It does not authorize a
workspace build, runtime behavior, provider calls, public-sync, autonomous
mutation, or production/public readiness claims.
