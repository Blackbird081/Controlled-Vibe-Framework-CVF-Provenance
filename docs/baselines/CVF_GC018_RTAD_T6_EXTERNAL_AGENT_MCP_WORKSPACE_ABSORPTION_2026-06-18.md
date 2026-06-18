# CVF GC-018 - RTAD-T6 External Agent MCP Workspace Absorption

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-18

docType: baseline

## Purpose

Authorize a bounded documentation/reference tranche that corrects the external
agent review-context gap and absorbs useful MCP/workspace patterns from:

- Foundry repository audit;
- local `CVF_WORKSPACE_LAYER_PRODUCTION_HANDOFF_PACKAGE/` external-agent
  package.

## Scope

In scope:

- create stable external-agent review context front door;
- clarify public/simple workflow vocabulary versus internal governed
  workflow-chain authority;
- create CVF-owned absorption map for the copied workspace package;
- update MCP and agent workspace reference front doors;
- keep raw external package out of commits.

Out of scope:

- public-sync;
- importing the raw package;
- implementing MCP tools;
- workspace runtime execution;
- provider calls or live proof;
- product UI, production readiness, public readiness, or release claims.

## Source Verification

| Claimed item | Source file | Verified section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Active next move permits choosing a fresh governed runtime tranche. | `CVF_SESSION/state/entries/nextAllowedMove.json` | `value` | `nextAllowedMove` | active session state | ACCEPT |
| RTAD-T5 boundary keeps MCP implementation parked. | `docs/reference/mcp_gateway/CVF_MODEL_GATEWAY_MCP_RUNTIME_BRIDGE_BOUNDARY.md` | `Forbidden Without Separate Authorization` | MCP implementation boundary | MCP Gateway reference | ACCEPT |
| Agent workspace runtime remains foundation-only. | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` | `Runtime Expansion Boundary` | `QUEUE_SKELETON_ONLY` | agent workspace runtime contract | ACCEPT |

## External Reference Input Table

These sources are useful review inputs but are not CVF source authority.

| Input | Observed pattern | CVF disposition |
|---|---|---|
| `CVF_WORKSPACE_LAYER_PRODUCTION_HANDOFF_PACKAGE/EXTENSIONS/CVF_WORKSPACE_LAYER/README.md` | CVF Core remains authority and workspace state is projection. | `NOT_CVF_SOURCE`; absorb through `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md`. |
| `CVF_WORKSPACE_LAYER_PRODUCTION_HANDOFF_PACKAGE/EXTENSIONS/CVF_WORKSPACE_LAYER/contracts/WORKSPACE_MCP_CONTRACT.md` | Proposal-before-execution and dangerous-action blocking. | `NOT_CVF_SOURCE`; adapt through CVF MCP/workspace contracts. |
| `CVF_WORKSPACE_LAYER_PRODUCTION_HANDOFF_PACKAGE/EXTENSIONS/CVF_WORKSPACE_LAYER/schemas/workflow_state.schema.json` | Hard-coded public/simple workflow enum. | `NOT_CVF_SOURCE`; reject as internal authority. |
| `https://github.com/sonht113/Foundry` | MCP as first-class agent ingress over local state. | `EXTERNAL_REFERENCE`; adapt through CVF MCP Gateway boundary. |

## Decision

Proceed with documentation/reference absorption only. CVF-owned artifacts must
absorb patterns through stable indexed paths and keep CVF as the source of
truth.

## Evidence / Verification

| Evidence | Result |
|---|---|
| Foundry audit | README and MCP server source inspected on 2026-06-18. |
| Local package smoke test | PASS in temp directory: safe proposal approved, `shell_exec` blocked, evidence accepted. |
| Raw package boundary | raw copied package is ignored and not part of governed material. |
| Registry discipline | GC-051 source entries added and aggregate regenerated. |

## Claim Boundary

This GC-018 closes a bounded foundation/reference tranche. It does not
authorize runtime implementation, MCP tool creation, public-sync, live proof,
provider routing mutation, or external-facing readiness.
