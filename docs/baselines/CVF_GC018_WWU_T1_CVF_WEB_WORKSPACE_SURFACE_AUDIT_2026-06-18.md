# CVF GC-018 - WWU-T1 CVF Web Workspace Surface Audit

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-18

docType: baseline

## Purpose

Authorize a bounded source-verification audit of current `cvf-web` surfaces
before any CVF Web Workspace UI implementation.

## Decision / Baseline / Proposed Tranche

Decision: approve WWU-T1 as an audit-only tranche.

Baseline: WWU-T0 established the two-layer workspace split and made WWU-T1 the
required next move before UI implementation.

Proposed tranche: map current `cvf-web` pages, routes, and read surfaces against
the CVF Web Workspace read-model requirements; identify the smallest WWU-T2
operator dashboard/read-model scope; keep Local Workspace Runtime/MCP parked.

## Scope / Target / Owner Boundary

Target: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web` route/component/API
surface inventory as it relates to `CVF_WEB_WORKSPACE`.

Owner boundary: source-verification audit only. No `cvf-web` source edit, UI
implementation, MCP implementation, Local Workspace Runtime mutation,
provider/live proof, public-sync, raw external package import, or readiness
claim is authorized.

## Source Authority

| Source | Role |
|---|---|
| `docs/reference/agent_workspace/CVF_WORKSPACE_TWO_LAYER_ARCHITECTURE_STANDARD.md` | Central two-layer workspace architecture |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPERATOR_VIEW_PLAN.md` | CVF Web Workspace read-model requirements |
| `docs/roadmaps/CVF_WEB_WORKSPACE_UPGRADE_ROADMAP_2026-06-18.md` | WWU tranche sequence |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/docs/reference/CVF_W112_WEB_GOVERNANCE_SURFACE_INVENTORY_2026-04-22.md` | existing Web governance-surface inventory |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/governance/page.tsx` | current governance hub |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/governance/operations/page.tsx` | current governed operations view |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/governance/evidence/page.tsx` | current evidence view |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/governance/system-health/page.tsx` | current health/readiness view |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ApprovalInbox.tsx` | current approval inbox |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/Sidebar.tsx` | current navigation grouping |

## Authorized Changes

| Path | Change |
|---|---|
| `docs/baselines/CVF_GC018_WWU_T1_CVF_WEB_WORKSPACE_SURFACE_AUDIT_2026-06-18.md` | create and close GC-018 |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_WWU_T1_CVF_WEB_WORKSPACE_SURFACE_AUDIT_FOR_CODEX_2026-06-18.md` | create and close source-verified work order |
| `docs/audits/CVF_WWU_T1_CVF_WEB_WORKSPACE_SURFACE_AUDIT_2026-06-18.md` | create source-backed audit packet |
| `docs/reviews/CVF_WWU_T1_CVF_WEB_WORKSPACE_SURFACE_AUDIT_COMPLETION_2026-06-18.md` | create completion review |
| `docs/roadmaps/CVF_WEB_WORKSPACE_UPGRADE_ROADMAP_2026-06-18.md` | mark WWU-T1 closed and WWU-T2 ready for fresh GC-018 |
| `docs/corpus-intelligence/registry/entries/wwu-t1-cvf-web-workspace-surface-audit.json` | add GC-051 source entry |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | regenerate aggregate |

## Evidence / Verification

| Evidence | Required result |
|---|---|
| `git diff --check` | PASS |
| `python governance/compat/generate_corpus_scan_registry.py --check` | PASS |
| `python governance/compat/check_work_order_dispatch_quality.py --base 6628ae40 --head HEAD --enforce` | PASS |
| `python governance/compat/check_machine_closure_package.py --base 6628ae40 --head HEAD --enforce` | PASS |
| `python governance/compat/run_worker_return_fast_gate.py` | PASS before material commit |

## Stop Boundaries

- Do not edit `cvf-web` product source in WWU-T1.
- Do not implement the CVF Web Workspace UI.
- Do not implement MCP, CLI wrappers, runtime queues, or Local Workspace
  Runtime.
- Do not run provider/live calls.
- Do not public-sync.
- Do not import raw external package code.
- Do not claim production/public/readiness behavior.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance audit and roadmap sequencing only.

## Claim Boundary

This GC-018 authorizes and closes a source-verification audit only.
