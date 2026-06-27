# CVF GC-018 - WWU-T2 CVF Web Workspace Operator Dashboard Read Model

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-18

docType: baseline

Owner: Codex

rawMemoryReleased: false

GC-018 class: cvf-web-workspace-operator-dashboard-read-model

## Purpose

Authorize WWU-T2 dispatch for the first bounded CVF Web Workspace operator
dashboard/read model. The tranche may implement a read-only Web route and
read-only server/API projection from CVF-governed continuity artifacts, but it
must not implement Local Workspace Runtime, MCP tooling, provider/live proof,
public-sync, or governed action mutation.

## Authorization / Decision

Operator authorized the next WWU step with "next" after WWU-T1 closed. The
active session front door and handoff name WWU-T2 fresh GC-018/work-order
authoring as the next allowed move.

Decision: AUTHORIZE WWU-T2 dispatch for a read-only CVF Web Workspace operator
dashboard/read model.

This baseline does not itself implement product UI. It creates execution
authority for the following work order:

`docs/work_orders/CVF_AGENT_WORK_ORDER_WWU_T2_CVF_WEB_WORKSPACE_OPERATOR_DASHBOARD_READ_MODEL_FOR_CODEX_2026-06-18.md`

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
|---|---|
| Decision | AUTHORIZE |
| Baseline | `93540bbf` |
| Proposed tranche | WWU-T2 CVF Web Workspace Operator Dashboard Read Model |
| Worker | Codex |
| Commit mode | `WORKER_MAY_COMMIT` |
| Reviewer/closer | Codex single-agent multi-role with operator escalation |
| targetLayer | `CVF_WEB_WORKSPACE` |
| Runtime authorization | Read-only Web Workspace projection only |
| Live/provider authorization | Not authorized |

## Source Authority

| Source | Role |
|---|---|
| `CVF_SESSION_MEMORY.md` | current next allowed move and parked checkpoint source |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | machine-readable active session source |
| `AGENT_HANDOFF_V19_2026-06-15.md` | active handoff and handoff contract local view |
| `docs/roadmaps/CVF_WEB_WORKSPACE_UPGRADE_ROADMAP_2026-06-18.md` | WWU tranche authority |
| `docs/audits/CVF_WWU_T1_CVF_WEB_WORKSPACE_SURFACE_AUDIT_2026-06-18.md` | source-backed WWU-T1 surface audit |
| `docs/reference/agent_workspace/CVF_WORKSPACE_TWO_LAYER_ARCHITECTURE_STANDARD.md` | Web/runtime layer split |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPERATOR_VIEW_PLAN.md` | operator read-model target |
| `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` | workspace design control block source |
| `DESIGN.md` | canonical CVF visual system before frontend implementation |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/Sidebar.tsx` | current Web navigation placement |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/governance/evidence/route.ts` | existing read-only evidence API precedent |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/system/health/route.ts` | existing read-only health API precedent |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| WWU-T2 is ready only for fresh GC-018 authoring after WWU-T1. | `CVF_SESSION_MEMORY.md` | `## Next Allowed Move` | `WWU-T2` | active session front door | ACCEPT |
| Active handoff routes next allowed move to WWU-T2 fresh GC-018/work order. | `AGENT_HANDOFF_V19_2026-06-15.md` | `## Startup Acknowledgment`; `## Next Allowed Move` | `WWU-T2` | active handoff | ACCEPT |
| WWU roadmap makes WWU-T2 the next tranche after T1 and keeps T3 parked. | `docs/roadmaps/CVF_WEB_WORKSPACE_UPGRADE_ROADMAP_2026-06-18.md` | `## Tranche Plan`; `## WWU-T1 Closure Note` | `WWU-T2` | CVF Web Workspace upgrade roadmap | ACCEPT |
| WWU-T1 found no active CVF session-state/handoff/workspace read-model endpoint in current Web. | `docs/audits/CVF_WWU_T1_CVF_WEB_WORKSPACE_SURFACE_AUDIT_2026-06-18.md` | `## Gap Analysis Against Operator Read Model`; `## Minimal WWU-T2 Recommendation` | `active CVF session-state/handoff/workspace read model` | WWU-T1 audit | ACCEPT |
| CVF Web Workspace may show current mode, next allowed move, active handoff, parked checkpoints, evidence, receipts, guard status, and closure boundaries. | `docs/reference/agent_workspace/CVF_WORKSPACE_TWO_LAYER_ARCHITECTURE_STANDARD.md` | `## CVF Web Workspace` | `CVF_WEB_WORKSPACE` | workspace two-layer standard | ACCEPT |
| Operator view plan defines Current Mode, Active Handoff, Guard Status, and Next Move as read-model sections. | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPERATOR_VIEW_PLAN.md` | `## Read Model Sections` | `Read Model Sections` | operator view plan | ACCEPT |
| DESIGN.md is the canonical visual contract before Web implementation. | canonical contract: DESIGN.md | `## 9. Agent Prompt Guide`; `## 12. Style Vocabulary` | `DESIGN.md` | CVF design contract | ACCEPT |
| Current sidebar already has a Workspace nav group and Governance/Runtime/Work Transfer links. | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/Sidebar.tsx` | lines 149, 208, 228, 238 | `SidebarNavGroup` | Sidebar | ACCEPT |
| Existing governance evidence route returns a server-side read-only evidence report. | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/governance/evidence/route.ts` | lines 6-7 | `getGovernanceEvidenceReport` | governance evidence route | ACCEPT |
| Existing system health route returns a server-side read-only system health report. | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/system/health/route.ts` | lines 6-7 | `getSystemHealth` | system health route | ACCEPT |

## Authorized Changes

WWU-T2 execution may create or edit only these product/source paths:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/cvf-workspace-read-model.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/cvf-workspace-read-model.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/workspace/state/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/workspace/state/route.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/workspace/page.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/workspace/page.test.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/Sidebar.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/i18n.ts`

WWU-T2 execution may also create completion evidence under:

- `docs/reviews/CVF_WWU_T2_CVF_WEB_WORKSPACE_OPERATOR_DASHBOARD_READ_MODEL_COMPLETION_2026-06-18.md`
- `docs/reviews/evidence/wwu-t2-cvf-web-workspace-operator-dashboard-read-model-2026-06-18.json`

Roadmap and corpus registry updates are allowed only if needed for closure:

- `docs/roadmaps/CVF_WEB_WORKSPACE_UPGRADE_ROADMAP_2026-06-18.md`
- `docs/corpus-intelligence/registry/entries/wwu-t2-cvf-web-workspace-operator-dashboard-read-model.json`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`

## Required Read-Only Product Boundary

The implementation work order must preserve these rules:

- read CVF state from governed repo artifacts only;
- expose a read-only operator projection;
- name the CVF session mode field `activeSessionMode` or another explicit
  non-chat name;
- deep-link existing Evidence, System Health, Governance Operations, Approval
  Inbox, Work Transfer, and Runtime Monitor surfaces instead of duplicating
  their mutations;
- avoid new action buttons beyond read-only links unless a later governed
  action-request tranche authorizes them.

## Forbidden Scope

WWU-T2 must not:

- implement or mutate Local Workspace Runtime;
- implement MCP, CLI wrappers, runtime queues, scheduler queues, worker daemons,
  or agent enforcement;
- run provider/live calls or consume secrets/quota;
- public-sync;
- import raw external workspace package code;
- edit provider registries, active session state, or active handoff in the
  material implementation commit;
- claim runtime enforcement, production readiness, public readiness,
  release-facing readiness, or external-facing readiness.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | A read-only server read model projects current mode, next allowed move, active handoff, roadmap/work-order status, evidence/guard links, and parked checkpoints from CVF-governed sources. |
| AC2 | The Web API route returns the read model without mutating files, queues, provider state, active session state, or handoff files. |
| AC3 | The `/workspace` dashboard route renders the operator read model using DESIGN.md-compatible operational dashboard layout and existing project conventions. |
| AC4 | Navigation exposes the new workspace route without breaking existing Workspace, Work Transfer, Runtime Monitor, or Governance links. |
| AC5 | Focused tests cover read-model parsing, route response, and dashboard rendering or an explicit source-backed blocker is recorded. |
| AC6 | No Local Runtime/MCP/provider/live/public-sync/readiness claim appears in completion. |
| AC7 | Any reusable finding is recorded in a governed artifact disposition, not provider-local memory only. |

## Evidence / Verification

Required before WWU-T2 closure:

- `git rev-parse --short HEAD`;
- `git status --short`;
- source-symbol re-verification using `rg -n`;
- `npm run check` from `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`;
- focused tests for the new read-model/API/UI paths;
- `git diff --check`;
- `python governance/compat/run_worker_return_fast_gate.py`;
- committed-range `pre-closure` on the material range;
- session-sync steward only following the accepted material commit if next move changes.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance Web Workspace dispatch. No public-sync batch is
authorized.

## Finding-To-Governance Learning Disposition

| Field | Disposition |
|---|---|
| Defect class | `ORCHESTRATOR_PACKET_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Escalation state | `WORK_ORDER_ADDED` |
| Next control action | WWU-T2 implements a read-only CVF Web Workspace projection before any governed action-request or Local Runtime/MCP tranche |
| Worker blame | `N/A_WITH_REASON`: this baseline releases a previously identified WWU-T1 read-model gap |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-18 WWU-T2 GC-018 authoring |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, governance gates |
| Target paths | WWU roadmap; WWU-T2 GC-018; WWU-T2 work order; GC-051 registry source entry |
| Allowed scope source | active session next allowed move after WWU-T1 closure |
| Before status evidence | base `93540bbf`; clean worktree |
| After status evidence | pending WWU-T2 dispatch commit |
| Diff evidence | `git diff --name-status 93540bbf..HEAD` |
| Approval boundary | GC-018 and work-order dispatch only |
| Claim boundary | no product source implementation in this dispatch batch; no runtime/provider/live/public-sync/readiness claim |
| Agent type | Codex dispatcher |
| Invocation ID | `wwu-t2-cvf-web-workspace-operator-dashboard-read-model-gc018-2026-06-18` |
| Expected manifest | `docs/baselines/CVF_GC018_WWU_T2_CVF_WEB_WORKSPACE_OPERATOR_DASHBOARD_READ_MODEL_2026-06-18.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_WWU_T2_CVF_WEB_WORKSPACE_OPERATOR_DASHBOARD_READ_MODEL_FOR_CODEX_2026-06-18.md`; `docs/roadmaps/CVF_WEB_WORKSPACE_UPGRADE_ROADMAP_2026-06-18.md`; `docs/corpus-intelligence/registry/entries/wwu-t2-cvf-web-workspace-operator-dashboard-read-model.json`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` |
| Actual changed set | pending dispatch material range |
| Manifest delta | pending until commit |
| Deletion or rename disposition | N/A with reason: no deletion or rename authorized |

## Claim Boundary

This GC-018 authorizes only WWU-T2 dispatch for a read-only CVF Web Workspace
operator dashboard/read model. It does not implement UI in this dispatch
commit and does not authorize Local Runtime/MCP, provider/live calls,
public-sync, runtime enforcement, or readiness claims.
