# CVF GC-018 - WWU-T0 Workspace Two-Layer Foundation

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-18

docType: baseline

## Purpose

Authorize the bounded foundation batch that makes the CVF Web Workspace and CVF
Local Workspace Runtime split explicit before any CVF Web upgrade work begins.

## Decision / Baseline / Proposed Tranche

Decision: approve WWU-T0 as a documentation/reference foundation tranche.

Baseline: EARC-T3A absorbed the useful workspace-package split, but the split
was not yet expressed as a named CVF-native Central Core standard.

Proposed tranche: add the stable two-layer architecture standard, wire it into
workspace local views, create the CVF Web Workspace upgrade roadmap, and record
registry/completion evidence.

## Scope / Target / Owner Boundary

Target: stable workspace reference docs, WWU roadmap, dated work order,
completion review, and corpus registry coverage.

Owner boundary: documentation/reference foundation only. No product UI,
runtime/MCP implementation, provider/live proof, public-sync, raw external
package import, or production/public readiness claim is authorized.

## Source Authority

| Source | Role |
|---|---|
| Operator instruction 2026-06-18 | Clarify the two workspace layers and prepare CVF Web upgrade |
| `docs/reference/agent_workspace/README.md` | stable workspace front door |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPERATOR_VIEW_PLAN.md` | operator-facing read model |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` | runtime/MCP boundary |
| `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md` | external package absorption map |
| `docs/reviews/CVF_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_WORKSPACE_LAYER_2026-06-18.md` | absorption decisions and rejected external assumptions |

## Authorized Changes

| Path | Change |
|---|---|
| `docs/reference/agent_workspace/CVF_WORKSPACE_TWO_LAYER_ARCHITECTURE_STANDARD.md` | add stable Central Core standard |
| `docs/reference/agent_workspace/README.md` | index the new standard and read triggers |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPERATOR_VIEW_PLAN.md` | bind operator view to CVF Web Workspace |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` | bind runtime contract to Local Workspace Runtime |
| `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md` | map external package Web/runtime areas into CVF layers |
| `docs/roadmaps/CVF_WEB_WORKSPACE_UPGRADE_ROADMAP_2026-06-18.md` | create Web Workspace upgrade roadmap |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_WWU_T0_WORKSPACE_TWO_LAYER_FOUNDATION_FOR_CODEX_2026-06-18.md` | create and close this work order |
| `docs/reviews/CVF_WWU_T0_WORKSPACE_TWO_LAYER_FOUNDATION_COMPLETION_2026-06-18.md` | create completion review |
| `docs/corpus-intelligence/registry/entries/wwu-t0-workspace-two-layer-foundation.json` | add GC-051 source entry |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | regenerate aggregate |

## Evidence / Verification

| Evidence | Required result |
|---|---|
| `git diff --check` | PASS |
| `python governance/compat/generate_corpus_scan_registry.py --check` | PASS |
| `python governance/compat/check_foundation_storage_layout.py --base f688fa9e --head HEAD --enforce` | PASS |
| `python governance/compat/check_work_order_dispatch_quality.py --base f688fa9e --head HEAD --enforce` | PASS |
| `python governance/compat/check_machine_closure_package.py --base f688fa9e --head HEAD --enforce` | PASS |
| `python governance/compat/run_worker_return_fast_gate.py` | PASS before commit |

## Stop Boundaries

- Do not edit `cvf-web` product source in WWU-T0.
- Do not implement MCP or Local Workspace Runtime.
- Do not run provider/live calls.
- Do not public-sync.
- Do not import raw external package code.
- Do not claim production/public readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance foundation clarification only.

## Claim Boundary

This GC-018 authorizes architecture clarification and roadmap creation only.
