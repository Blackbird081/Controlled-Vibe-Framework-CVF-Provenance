# CVF GC-018 - EARC-T3A External Return Absorption Pilot

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-18

docType: baseline

## Purpose

Authorize a bounded pilot that uses the EARC-T3 absorption workflow on one real
external return source: the operator-copied workspace-layer production handoff
package.

## Scope

In scope:

- classify selected external package observations through
  `CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md`;
- produce a dated absorption review packet with the required absorption table;
- update the existing workspace-layer absorption map with the pilot result;
- update the EARC roadmap state and GC-051 registry coverage;
- record whether the EARC-T3 checker candidate is now ready for a future
  tranche.

Out of scope:

- public-sync or public repository edits;
- importing or modifying the raw external package;
- implementing MCP tools or workspace runtime behavior;
- provider or live API calls;
- runtime, public, production, release, MCP, provider, or external-facing
  readiness claims;
- adding the checker in this tranche.

## Source Verification

| Claimed item | Source file | Verified section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| EARC-T3 requires returned external output to be classified before CVF acts on it. | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md` | `## Classification Workflow`; `## Required Absorption Table` | required absorption table columns | external-agent finding absorption workflow | ACCEPT |
| The copied workspace package is external reference input and not CVF authority. | `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md` | `## Source Package Status`; `## Claim Boundary` | `NOT_CVF_SOURCE`; raw import rejected | workspace-layer absorption map | ACCEPT |
| The pilot will record external package claims as advisory evidence, not as CVF authority. | `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md` | `## Source Package Status`; `## Claim Boundary` | `NOT_CVF_SOURCE`; raw import rejected | workspace-layer absorption map | ACCEPT |
| The copied package root is available as frozen reference evidence for this pilot. | `governance/compat/CVF_ROOT_FOLDER_LIFECYCLE_REGISTRY.json` | root entry for `CVF_WORKSPACE_LAYER_PRODUCTION_HANDOFF_PACKAGE` | lifecycle/exposure classes | root folder lifecycle registry | ACCEPT |
| The package root is classified as frozen internal reference. | `governance/compat/CVF_ROOT_FOLDER_LIFECYCLE_REGISTRY.json` | root entry for `CVF_WORKSPACE_LAYER_PRODUCTION_HANDOFF_PACKAGE` | lifecycle/exposure classes | root folder lifecycle registry | ACCEPT |

## Decision

Proceed with a documentation/reference pilot. The pilot may consume external
package claims into a CVF-owned absorption review and update the existing
absorption map, but it may not import package code or claim runtime capability.

## Evidence / Verification

| Evidence | Expected result |
|---|---|
| `python governance/compat/generate_corpus_scan_registry.py --generate` | Registry aggregate updates from source entries |
| `python governance/compat/generate_corpus_scan_registry.py --check` | Registry aggregate matches sources |
| `git diff --check` | Diff hygiene passes |
| `python governance/compat/run_worker_return_fast_gate.py` | Reviewer-fast checks pass |
| `python governance/compat/run_agent_commit_steward_preflight.py --mode implementation --base 0f6d54e8 --head HEAD --enforce` | Material commit shape is bounded |
| Pre-commit hook | Required local governance checks pass |

## Claim Boundary

This GC-018 authorizes a reference absorption pilot only. It does not authorize
public-sync, MCP implementation, provider/live calls, workspace runtime
mutation, raw external package import, checker implementation, or readiness
claims.

## Work Order

The authorized work order is:

`docs/work_orders/CVF_AGENT_WORK_ORDER_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_FOR_CODEX_2026-06-18.md`
