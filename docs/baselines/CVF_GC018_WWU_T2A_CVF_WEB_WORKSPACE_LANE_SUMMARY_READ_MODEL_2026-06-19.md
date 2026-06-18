# CVF GC-018 - WWU-T2A CVF Web Workspace Lane Summary Read Model

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-19

docType: baseline

Owner: Codex

rawMemoryReleased: false

GC-018 class: cvf-web-workspace-lane-summary-read-model

## Purpose

Authorize WWU-T2A dispatch for a bounded read-only enhancement to the CVF Web
Workspace dashboard: project the generated agent workspace state lane summary
into the existing `/workspace` read model.

## Authorization / Decision

Operator asked Codex to continue. WWU-T2 closure is source-backed at material
commit `b3593e1b` and session-sync commit `517ba80c`. The active session allows
only a later bounded Web Workspace follow-up with fresh GC-018 and a
source-verified work order; WWU-T3 Local Workspace Runtime/MCP remains parked.

Decision: AUTHORIZE WWU-T2A dispatch for read-only lane summary projection
from `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json`.

This baseline does not itself implement product UI. It creates execution
authority for:

`docs/work_orders/CVF_AGENT_WORK_ORDER_WWU_T2A_CVF_WEB_WORKSPACE_LANE_SUMMARY_READ_MODEL_FOR_CODEX_2026-06-19.md`

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
|---|---|
| Decision | AUTHORIZE |
| Baseline | `517ba80c` |
| Proposed tranche | WWU-T2A CVF Web Workspace Lane Summary Read Model |
| Worker | Codex |
| Commit mode | `WORKER_MAY_COMMIT` |
| Reviewer/closer | Codex single-agent multi-role with operator escalation |
| targetLayer | `CVF_WEB_WORKSPACE` |
| Runtime authorization | Read-only Web Workspace lane summary projection only |
| Live/provider authorization | Not authorized |

## Source Authority

| Source | Role |
|---|---|
| `CVF_SESSION_MEMORY.md` | current next allowed move and parked checkpoint source |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | machine-readable active session source |
| `AGENT_HANDOFF_V19_2026-06-15.md` | active handoff and handoff contract local view |
| `docs/roadmaps/CVF_WEB_WORKSPACE_UPGRADE_ROADMAP_2026-06-18.md` | WWU tranche authority |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPERATOR_VIEW_PLAN.md` | operator read-model target |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` | generated workspace state topology |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_LANE_TAXONOMY.md` | lane vocabulary |
| `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json` | generated active workspace state |
| `docs/reference/agent_workspace/CVF_WORKSPACE_TWO_LAYER_ARCHITECTURE_STANDARD.md` | Web/runtime layer split |
| `DESIGN.md` | canonical CVF visual system before frontend implementation |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/cvf-workspace-read-model.ts` | existing WWU-T2 server read model |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/workspace/page.tsx` | existing WWU-T2 dashboard route |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Active next move permits only a later bounded Web Workspace follow-up with fresh GC-018 and work order. | `CVF_SESSION_MEMORY.md` | `## Next Allowed Move` | `bounded Web Workspace follow-up` | active session front door | ACCEPT |
| Active handoff keeps WWU-T3 Local Runtime/MCP parked unless explicitly authorized. | `AGENT_HANDOFF_V19_2026-06-15.md` | `## Next Allowed Move` | `WWU-T3` | active handoff | ACCEPT |
| Operator view plan names Lane Summary as a read-model section. | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPERATOR_VIEW_PLAN.md` | `## Read Model Sections` | `Lane Summary` | operator view plan | ACCEPT |
| Workspace topology requires generated state records to include lane, itemKind, status, ownerRole, evidencePaths, claimBoundary, and nextMoveImpact. | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` | `## Required State Fields` | `Required State Fields` | state topology contract | ACCEPT |
| Lane taxonomy defines allowed lane values including accepted_material, parked, and session_sync. | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_LANE_TAXONOMY.md` | `## Central Core` | `Allowed lanes` | lane taxonomy | ACCEPT |
| Generated active workspace state exists as a read-only aggregate with `items`. | `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json` | top-level JSON | `items` | generated workspace state aggregate | ACCEPT |
| Two-layer standard separates CVF Web Workspace from Local Workspace Runtime. | `docs/reference/agent_workspace/CVF_WORKSPACE_TWO_LAYER_ARCHITECTURE_STANDARD.md` | `## Canonical Two-Layer Split` | `CVF_WEB_WORKSPACE` | workspace two-layer standard | ACCEPT |
| Existing read model exposes `CvfWorkspaceReadModel` and `getCvfWorkspaceReadModel`. | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/cvf-workspace-read-model.ts` | source symbols | `CvfWorkspaceReadModel`; `getCvfWorkspaceReadModel` | server read model | ACCEPT |
| DESIGN.md requires operational dashboards to prioritize state, evidence, hierarchy, and scanability. | canonical contract: DESIGN.md | `## 4. Layout & Navigation`; `## 12. Style Vocabulary` | `Enterprise Dashboard` | CVF design contract | ACCEPT |

## Authorized Changes

WWU-T2A execution may edit:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/cvf-workspace-read-model.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/cvf-workspace-read-model.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/workspace/state/route.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/workspace/page.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/workspace/page.test.tsx`
- `docs/reviews/CVF_WWU_T2A_CVF_WEB_WORKSPACE_LANE_SUMMARY_READ_MODEL_COMPLETION_2026-06-19.md`
- `docs/reviews/evidence/wwu-t2a-cvf-web-workspace-lane-summary-read-model-2026-06-19.json`
- `docs/roadmaps/CVF_WEB_WORKSPACE_UPGRADE_ROADMAP_2026-06-18.md`

Dispatch-only authoring may also edit:

- this GC-018 baseline;
- `docs/work_orders/CVF_AGENT_WORK_ORDER_WWU_T2A_CVF_WEB_WORKSPACE_LANE_SUMMARY_READ_MODEL_FOR_CODEX_2026-06-19.md`;
- `docs/corpus-intelligence/registry/entries/wwu-t2a-cvf-web-workspace-lane-summary-read-model.json`;
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`.

## Required Read-Only Product Boundary

The implementation must:

- read generated workspace state only from repo-local governed aggregate files;
- summarize lanes, counts, parked/accepted material, and evidence links without
  adding mutation controls;
- deep-link evidence paths as text/link surfaces only;
- preserve WWU-T2 continuity projection behavior;
- keep governed action requests for a later separate tranche.

## Forbidden Scope

WWU-T2A must not:

- implement or mutate Local Workspace Runtime;
- implement MCP, CLI wrappers, runtime queues, scheduler queues, worker daemons,
  or agent enforcement;
- mutate `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json` or its
  source fragments;
- run provider/live calls or consume secrets/quota;
- public-sync;
- import raw external workspace package code;
- edit active session state, session memory, or active handoff in the material
  implementation commit;
- claim runtime enforcement, production readiness, public readiness,
  release-facing readiness, or external-facing readiness.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Read model projects lane summaries from generated workspace state without mutating it. |
| AC2 | Lane summary includes counts and bounded recent items with evidence paths and claim boundaries. |
| AC3 | `/workspace` renders the lane summary in the existing dashboard shell with no mutation buttons. |
| AC4 | Existing continuity, source authority, related links, and parked checkpoint behavior remain intact. |
| AC5 | Focused tests cover generated-state parsing, API shape, and dashboard rendering. |
| AC6 | No Local Runtime/MCP/provider/live/public-sync/readiness claim appears in completion. |

## Evidence / Verification

Required before WWU-T2A closure:

- `git rev-parse --short HEAD`;
- `git status --short`;
- source-symbol re-verification using `rg -n`;
- `npm run check` from `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`;
- focused tests for the read-model/API/UI paths;
- `git diff --check`;
- `python governance/compat/run_worker_return_fast_gate.py`;
- committed-range `pre-closure` on the material range.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance Web Workspace dispatch. No public-sync batch is
authorized.

## Finding-To-Governance Learning Disposition

| Field | Disposition |
|---|---|
| Defect class | `OPERATOR_SCOPE_CLARITY_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Escalation state | `WORK_ORDER_ADDED` |
| Next control action | Implement a read-only lane summary before any governed action-request or Local Runtime/MCP tranche |
| Worker blame | `N/A_WITH_REASON`: this baseline releases a bounded read-model follow-up |

## Claim Boundary

This GC-018 authorizes only WWU-T2A dispatch for a read-only CVF Web Workspace
lane summary read model. It does not implement UI in this dispatch commit and
does not authorize Local Runtime/MCP, provider/live calls, public-sync, runtime
enforcement, governed action requests, or readiness claims.
