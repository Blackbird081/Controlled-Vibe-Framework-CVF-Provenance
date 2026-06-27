# CVF Agent Work Order - WWU-T2 CVF Web Workspace Operator Dashboard Read Model For Codex

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-18

docType: work_order

Batch ID: WWU-T2

Owner: Codex worker; Codex reviewer/closer

Commit mode: WORKER_MAY_COMMIT

dispatchBaseHead: `93540bbf`

executionBaseHead: `93540bbf`

closureBaseHead: `c31e0069`

rawMemoryReleased: false

## Dispatch Prompt Envelope

Role: Codex implementer/reviewer/closer under single-agent multi-role control,
with the operator as escalation point.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_WWU_T2_CVF_WEB_WORKSPACE_OPERATOR_DASHBOARD_READ_MODEL_FOR_CODEX_2026-06-18.md`

Commit mode: `WORKER_MAY_COMMIT`

Base: executionBaseHead `93540bbf` captured after WWU-T1 session-sync.
Re-confirm with `git rev-parse --short HEAD` before implementation.

Current-time notes: WWU-T1 closed at material commit `3db83d3b` and
session-sync commit `93540bbf`. WWU-T2 is authorized only as the first
read-only CVF Web Workspace operator dashboard/read-model implementation.

Do-not-misread notes: this is not Local Workspace Runtime, not MCP/CLI
ingress, not provider/live proof, not a public-sync batch, not a readiness
claim, and not a governed action-request tranche. The Web dashboard may read
and display CVF-governed continuity, evidence, and status; it must not mutate
active session state, handoff files, runtime queues, provider state, or closure
artifacts.

Required first actions: read the CVF startup front door, active session state,
active handoff, this work order, WWU-T2 GC-018, WWU roadmap, WWU-T1 audit, the
workspace front door, the two-layer standard, the operator view plan, the
workspace design standard, the handoff boundary standard, and `DESIGN.md`.

Return contract: close `CLOSED_PASS_BOUNDED` only after a read-only Web
Workspace route/API/read-model implementation, focused tests, Web checks,
worker-return fast gate, committed-range pre-closure gate, and explicit
no-Local-Runtime/no-MCP/no-provider/no-public-sync/no-readiness boundary.

## Purpose

Implement the smallest read-only CVF Web Workspace operator dashboard/read
model so non-coder operators can inspect current mode, next allowed move,
active handoff, roadmap/work-order status, evidence/guard links, and parked
checkpoints without reading raw session files.

## Scope / Target / Owner Boundary

Target: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`.

Owner boundary: Codex may implement only the read-only Web Workspace projection
and dashboard paths named in Write Ownership. Session/front-door files may be
read as source data during runtime, but must not be edited in the material
implementation commit. Session-sync is a separate commit following the accepted
material commit only if
next move changes.

Risk ceiling: R2, because this is product UI/source work that reads governed
continuity artifacts, but it is read-only and no-provider/no-runtime.

## Intake Role Routing Decision

intake summary: active session next allowed move authorized WWU-T2 fresh
GC-018/work-order authoring after WWU-T1 source audit.

scope class: read-only CVF Web Workspace dashboard/read model.

risk sensitivity: R2; frontend and API source work inside existing `cvf-web`
only.

selected role route: `SINGLE_AGENT_MULTI_ROLE`

role separation basis: one Codex session may implement, self-review, commit,
and session-sync, but material implementation and session-sync ranges must stay
separate.

escalation condition: stop for operator decision if implementation requires
Local Runtime/MCP, provider/live proof, secrets/quota, public-sync, runtime
queues, active session mutation, handoff mutation in material range, readiness
claims, destructive actions, or paths outside Write Ownership.

## Agent Roles

| Role | Actor | Responsibility |
|---|---|---|
| Dispatcher | Codex | Author WWU-T2 GC-018 and this work order |
| Worker | Codex | Implement read-only Web Workspace projection and dashboard |
| Reviewer / closer | Codex | Review actual diff, run gates, commit material |
| Session-sync actor | Codex | Update continuity in a separate range only following accepted material commit |
| Operator | Human | Decide any scope expansion, runtime/MCP, public-sync, provider/live, or readiness claim |

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| Applicability | applies because selected route is `SINGLE_AGENT_MULTI_ROLE` |
| actor | Codex |
| role set | dispatcher, worker, reviewer, closer, session-sync actor if needed |
| Role separation ledger | dispatch commit, material execution commit, and session-sync commit must remain separate |
| Evidence basis independent of memory | source files, command outputs, tests, and governed completion packet |
| Gate sequence | pre-dispatch before dispatch commit; pre-implementation before product edits; focused tests/checks during execution; pre-closure before material commit; session-sync steward before session-sync commit |
| Self-review boundary | Codex may close only with command-backed evidence and exact changed-set trace |
| escalation condition | operator decision required for Local Runtime/MCP, provider/live, public-sync, active session mutation in material range, readiness claim, or forbidden path expansion |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | Codex worker; Codex reviewer/closer; Codex session-sync actor if needed; operator escalation |
| phase | DISPATCH_AUTHORING now; EXECUTION by Codex; CLOSURE by Codex; SESSION_SYNC by Codex in a separate range if next move changes |
| baseHeadFor(phase) | `dispatchBaseHead=93540bbf`; `executionBaseHead=93540bbf`; `closureBaseHead=c31e0069` |
| changedSetScope(phase) | dispatch scope is WWU-T2 GC-018, work order, roadmap, and registry; execution scope is named `cvf-web` read-model/API/UI/test paths plus completion/evidence; session-sync range is protected continuity files only |
| traceScope(phase, actor) | dispatch trace covers dispatch files only; execution trace covers product and completion files; session-sync trace covers session/front-door files only |
| commitOwner(phase) | Codex for dispatch, material execution, closure, and session-sync |
| crossBatchIsolation | clean worktree confirmed before dispatch authoring; worker must reconfirm before implementation and stop on unrelated dirty files |
| nextMoveSurfaces | update `CVF_SESSION/ACTIVE_SESSION_STATE.json`, `CVF_SESSION_MEMORY.md`, and active handoff only in a separate session-sync range following accepted material commit |
| Closer designation | Codex |

## Workspace Two-Layer Control Block

| Field | Disposition |
|---|---|
| targetLayer | `CVF_WEB_WORKSPACE` |
| operatorSurface | read-only dashboard and read-only API projection |
| agentExecutionSurface | N/A with reason: Local Workspace Runtime, MCP, CLI, queues, and agent enforcement are out of scope |
| sourceOfTruth | `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION_MEMORY.md`; active handoff named by state registry; WWU roadmap; governed reviews/evidence routes |
| mutationBoundary | no mutation except normal Web source implementation inside Write Ownership; no governed state/runtime/provider mutation |
| receiptBoundary | completion review and optional local evidence JSON only; no provider/live receipt |
| forbiddenConflationCheck | Web dashboard/read model is not Local Workspace Runtime enforcement and must not be claimed as such |

## Agent Workspace Design Control Block

| Field | Disposition |
|---|---|
| Workspace purpose | One bounded operator dashboard showing current CVF work state and links to existing governed evidence surfaces |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`; `docs/reference/agent_workspace/CVF_WORKSPACE_TWO_LAYER_ARCHITECTURE_STANDARD.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPERATOR_VIEW_PLAN.md` |
| Front door | `docs/reference/agent_workspace/README.md` |
| Design standard | `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `DESIGN.md` |
| Storage class | product source and tests under `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`; dated completion/evidence under `docs/reviews/` |
| Handoff fields | AHB block above owns route/base/commit semantics; dashboard may display active handoff path read-only |
| State ownership | no new generated workspace state; read-only projection from existing active session state and governed docs |
| Guard owner | existing handoff-boundary, workspace-design, runtime-boundary, AOT, dispatch-quality, and Web test/check gates |
| Build boundary | runtime source: no; Web source: yes, bounded; provider proof: no; public-sync: no; registry edits: only GC-051 source entry if required; runtime/MCP: no |

## Runtime Expansion Control Block

| Field | Disposition |
|---|---|
| runtimeExpansionMode | `READ_MODEL_ONLY` |
| queueScope | N/A with reason: no runtime queue, scheduler queue, or worker daemon is authorized |
| runtimeSourceScope | N/A with reason: Local Workspace Runtime is parked under WWU-T3 |
| operatorViewScope | read-only CVF Web Workspace dashboard |
| providerLiveScope | N/A with reason: no provider/live proof or secrets/quota use authorized |
| publicSyncScope | N/A with reason: no public-sync authorized |
| registryScope | GC-051 source registry only if changed artifacts require coverage |
| guardBoundary | existing CVF guards and focused Web tests; no new runtime guard implementation |

## Worker Autonomy / No-Question Rule

Codex should repair allowed-scope gate failures and rerun the failing gate.
Ask the operator only if the repair would require forbidden paths, Local
Runtime/MCP, provider/live proof, secrets/quota, public-sync, active session
mutation in material range, readiness claims, destructive actions, or higher
risk.

## Foundation Storage Layout Block

This task uses existing indexed execution and product folders:

- GC-018 under `docs/baselines/`;
- work order under `docs/work_orders/`;
- completion and optional evidence under `docs/reviews/`;
- product implementation under existing `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/`.

No new stable foundation file or new workspace root is authorized. If a
reusable design or governance lesson appears, record it in the completion
Finding-To-Governance Learning Disposition and route it to the appropriate
governed surface instead of provider-local memory.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: none in the material implementation range.

Protected paths mentioned in this work order are read-only source surfaces
during implementation unless a later dedicated session-sync range is opened:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/**`
- `AGENT_HANDOFF_V19_2026-06-15.md`

The worker must not edit protected session/handoff paths in the material
implementation commit. If next allowed move changes following accepted material
commit, open a separate session-sync range with protected-path authorization.

Operator authorization: active session next allowed move authorizes WWU-T2
dispatch only; protected session/handoff edits require a later dedicated
session-sync range.

Rollback boundary: revert only the WWU-T2 dispatch/material implementation if
rejected; do not revert WWU-T1 material commit `3db83d3b`, WWU-T1 session-sync
commit `93540bbf`, or earlier WWU/EARC/RTAD/AHB closures.

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact: `docs/audits/CVF_WWU_T1_CVF_WEB_WORKSPACE_SURFACE_AUDIT_2026-06-18.md`

priorVerificationAnchor: WWU-T1 material commit `3db83d3b` and session-sync
commit `93540bbf`.

freshRecomputeRequired: YES

recomputeReason: WWU-T2 touches current cvf-web source; recompute source searches, route existence checks, npm run check, and focused tests from the current worktree.

unicodePathHandling: use repo-relative paths and UTF-8-safe command output.
Agent-authored markdown and source comments should remain ASCII unless an
existing file convention requires otherwise.

## Current Runtime Freshness Verification

Dispatch-time checks found these planned paths absent:

| Planned path | Dispatch-time state |
|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/cvf-workspace-read-model.ts` | ABSENT |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/workspace/state/route.ts` | ABSENT |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/workspace/page.tsx` | ABSENT |

Dispatch-time search found no active CVF session-state/handoff/workspace read
model under `cvf-web/src`:

```powershell
rg -n "getWorkspace|workspace/state|ACTIVE_SESSION_STATE|CVF_SESSION_MEMORY|activeHandoff|nextAllowedMove|activeSessionMode" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src
```

The worker must recompute this search before implementation. If equivalent
files already exist at execution time, reuse or extend them instead of
duplicating routes.

## Negative Search And Collision Discipline

| Search / collision | Dispatch-time result | Required worker action |
|---|---|---|
| `currentMode` under `cvf-web/src` | present only as chat/spec mode in `AgentChatHeader.tsx` and `useAgentChat.ts` | do not reuse as CVF session mode; use `activeSessionMode` or equivalent |
| `api/sessions` route | present as chat session list/load/create/update/delete | do not treat as `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| `workspace/state` route | absent from searched `cvf-web/src` root at dispatch; tokens may appear in this work order after authoring | create only if still absent at execution |
| `cvf-workspace-read-model` helper | absent from searched `cvf-web/src` root at dispatch; tokens may appear in this work order after authoring | create only if still absent at execution |

## 1. Mission

Implement WWU-T2 as a read-only CVF Web Workspace operator dashboard/read
model. Success means the Web app exposes a compact operator view of current CVF
continuity and evidence without mutating governed state or implying Local
Runtime/MCP enforcement.

## 2. Authority Chain

| Level | Artifact | Status |
|---|---|---|
| Operator instruction | 2026-06-18 `next` following WWU-T1 material commit `3db83d3b` and session-sync commit `93540bbf` | ACCEPTED |
| Active session | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | WWU-T2 fresh GC-018 ready |
| Active handoff | `AGENT_HANDOFF_V19_2026-06-15.md` | next allowed move is WWU-T2 |
| WWU roadmap | `docs/roadmaps/CVF_WEB_WORKSPACE_UPGRADE_ROADMAP_2026-06-18.md` | WWU-T2 closed by completion review |
| WWU-T1 audit | `docs/audits/CVF_WWU_T1_CVF_WEB_WORKSPACE_SURFACE_AUDIT_2026-06-18.md` | closed source audit |
| WWU-T2 GC-018 | `docs/baselines/CVF_GC018_WWU_T2_CVF_WEB_WORKSPACE_OPERATOR_DASHBOARD_READ_MODEL_2026-06-18.md` | dispatch baseline packet |
| Design contract | `DESIGN.md` | read before frontend implementation |

## 3. Required First Reads

Codex must read:

- `CVF_SESSION_MEMORY.md`;
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`;
- `AGENT_HANDOFF_V19_2026-06-15.md`;
- this work order;
- `docs/baselines/CVF_GC018_WWU_T2_CVF_WEB_WORKSPACE_OPERATOR_DASHBOARD_READ_MODEL_2026-06-18.md`;
- `docs/roadmaps/CVF_WEB_WORKSPACE_UPGRADE_ROADMAP_2026-06-18.md`;
- `docs/audits/CVF_WWU_T1_CVF_WEB_WORKSPACE_SURFACE_AUDIT_2026-06-18.md`;
- `docs/reference/agent_workspace/README.md`;
- `docs/reference/agent_workspace/CVF_WORKSPACE_TWO_LAYER_ARCHITECTURE_STANDARD.md`;
- `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPERATOR_VIEW_PLAN.md`;
- `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`;
- `docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md`;
- `DESIGN.md`;
- current source files named in the Source Verification Block.

## 4. Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Active next move authorizes WWU-T2 GC-018/work-order authoring. | `CVF_SESSION_MEMORY.md` | `## Next Allowed Move` | `WWU-T2` | active session front door | ACCEPT |
| Active handoff routes WWU-T2 to a read-only operator dashboard/read model. | `AGENT_HANDOFF_V19_2026-06-15.md` | `## Startup Acknowledgment`; `## Next Allowed Move` | `WWU-T2` | active handoff | ACCEPT |
| WWU roadmap requires DESIGN.md, fresh GC-018, UI tests, and no Local Runtime mutation for WWU-T2. | `docs/roadmaps/CVF_WEB_WORKSPACE_UPGRADE_ROADMAP_2026-06-18.md` | `## Design Control Gate`; `## Tranche Plan` | `WWU-T2` | WWU roadmap | ACCEPT |
| WWU-T1 identified the missing active CVF session-state/handoff/workspace read model. | `docs/audits/CVF_WWU_T1_CVF_WEB_WORKSPACE_SURFACE_AUDIT_2026-06-18.md` | `## Gap Analysis Against Operator Read Model` | `active CVF session-state/handoff/workspace read model` | WWU-T1 audit | ACCEPT |
| Two-layer standard separates Web Workspace from Local Workspace Runtime. | `docs/reference/agent_workspace/CVF_WORKSPACE_TWO_LAYER_ARCHITECTURE_STANDARD.md` | `## Canonical Two-Layer Split`; `## Forbidden Conflations` | `CVF_WEB_WORKSPACE` | workspace two-layer standard | ACCEPT |
| Operator view plan defines required read-model sections. | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPERATOR_VIEW_PLAN.md` | `## Read Model Sections` | `Current Mode`; `Active Handoff`; `Guard Status`; `Next Move` | operator view plan | ACCEPT |
| DESIGN.md defines operational dashboard visual rules and pre-delivery UI obligations. | canonical contract: DESIGN.md | `## 4. Layout & Navigation`; `## 9. Agent Prompt Guide`; `## 14.6 Pre-ship verification` | `DESIGN.md` | CVF design contract | ACCEPT |
| Sidebar has a Workspace group and related Work Transfer, Runtime Monitor, and Governance links. | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/Sidebar.tsx` | lines 149, 208, 228, 238 | `SidebarNavGroup` | Sidebar | ACCEPT |
| Governance evidence API is read-only and returns a governance evidence report. | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/governance/evidence/route.ts` | lines 6-7 | `getGovernanceEvidenceReport` | governance evidence route | ACCEPT |
| System health API is read-only and returns system health. | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/system/health/route.ts` | lines 6-7 | `getSystemHealth` | system health route | ACCEPT |
| Approval inbox is an action surface, not a first-dashboard mutation target. | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ApprovalInbox.tsx` | lines 81, 98 | `/api/approvals` | approval inbox | ACCEPT |
| System jobs route can list and submit governance jobs, so WWU-T2 should deep-link it rather than duplicate mutation controls. | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/system/jobs/route.ts` | lines 29, 60 | `/api/system/jobs` | system jobs route | ACCEPT |

If any source symbol above is missing or materially different at execution
time, update the work order through a governed correction or return
`BLOCKED_WITH_REASON`; do not invent substitute fields.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Worker deliverable | Verification command or check | Status |
|---|---|---|---|---|
| WWU-T2 must implement first bounded Web Workspace operator dashboard/read model. | Mission; Write Ownership | `/workspace` page and read-only API/read-model helper | focused tests plus `npm run check` | READY |
| Must read `DESIGN.md` before frontend implementation. | Required First Reads; Source Verification Block | completion records DESIGN.md read and UI conformance | completion evidence plus UI tests | READY |
| Must include Agent Handoff Contract Control Block. | Agent Handoff Contract Control Block | this work order and completion preserve AHB fields | `check_agent_handoff_boundary.py` | READY |
| Must include Agent Workspace Design Control Block. | Agent Workspace Design Control Block | this work order and completion preserve workspace design fields | `check_agent_workspace_design.py` | READY |
| Must include Workspace Two-Layer Control Block. | Workspace Two-Layer Control Block | target layer locked to `CVF_WEB_WORKSPACE` | dispatch-quality gate | READY |
| Must avoid Local Runtime/MCP mutation. | Forbidden Scope; Runtime Expansion Control Block | no runtime/MCP paths touched | git diff/name-status review | READY |
| Must include focused UI/type/test evidence. | Evidence Requirements; Acceptance Criteria | focused tests and Web check | `npm run check`; focused tests | READY |

## 5. Write Ownership

Codex may create or edit:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/cvf-workspace-read-model.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/cvf-workspace-read-model.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/workspace/state/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/workspace/state/route.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/workspace/page.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/workspace/page.test.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/Sidebar.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/i18n.ts`
- `docs/reviews/CVF_WWU_T2_CVF_WEB_WORKSPACE_OPERATOR_DASHBOARD_READ_MODEL_COMPLETION_2026-06-18.md`
- `docs/reviews/evidence/wwu-t2-cvf-web-workspace-operator-dashboard-read-model-2026-06-18.json`
- `docs/roadmaps/CVF_WEB_WORKSPACE_UPGRADE_ROADMAP_2026-06-18.md`
- `docs/corpus-intelligence/registry/entries/wwu-t2-cvf-web-workspace-operator-dashboard-read-model.json`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`

Codex must not edit:

- `CVF_SESSION_MEMORY.md`, `CVF_SESSION/**`, or `AGENT_HANDOFF_V19_2026-06-15.md` in the material implementation range;
- Local Workspace Runtime, MCP, CLI, runtime queue, scheduler, or worker daemon files;
- provider credentials, `.env` files, provider registries, or live-proof harnesses;
- public-sync clone or public-facing repository files;
- raw external package files;
- unrelated `cvf-web` product files outside the owned paths.

## 6. Pre-Flight Checks

Run before implementation:

```powershell
git rev-parse --short HEAD
git status --short
rg -n "getWorkspace|workspace/state|ACTIVE_SESSION_STATE|CVF_SESSION_MEMORY|activeHandoff|nextAllowedMove|activeSessionMode" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src
Test-Path "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/workspace/page.tsx"
Test-Path "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/workspace/state/route.ts"
Test-Path "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/cvf-workspace-read-model.ts"
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 93540bbf --head HEAD
```

Expected result:

- execution base is `93540bbf` unless a newer explicit dispatch/session-sync
  base is recorded;
- worktree is clean before implementation;
- no existing equivalent read-model files are present, or the worker records
  and reuses them if they appeared after dispatch.

## 7. Execution Instructions

1. Re-confirm execution base and worktree isolation.
2. Complete all Required First Reads, including `DESIGN.md`.
3. Re-run the Source Verification Block against current files.
4. Create a read-only server helper that parses `CVF_SESSION/ACTIVE_SESSION_STATE.json`, resolves `activeHandoff`, extracts a bounded next-move/current-mode/parked-checkpoint summary, and exposes stable links to existing evidence/health/operations/work-transfer surfaces.
5. Create `GET /api/workspace/state` as a read-only route returning the helper output with no-store headers.
6. Create `/workspace` dashboard under the existing dashboard shell, following DESIGN.md Enterprise Dashboard/Ops-style operational density.
7. Add or update Sidebar/i18n entries only as needed to make `/workspace` reachable.
8. Add focused tests for helper parsing, API route response, and dashboard rendering.
9. Run Web checks/tests and governance gates.
10. Create completion review and optional local evidence JSON.
11. Commit material after gates pass.
12. Open a separate session-sync range only following accepted material commit if next move changes.

## Execution Plan

1. Confirm base/head and clean worktree.
2. Read authority, design, and source files.
3. Recompute negative search and source verification.
4. Implement read-only helper/API/page/nav.
5. Add focused tests.
6. Run `npm run check` and focused tests from `cvf-web`.
7. Run worker-return fast gate and pre-closure autorun on the material range.
8. Commit material.
9. Session-sync separately if required.

## Work-Order Fulfillment Manifest

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/cvf-workspace-read-model.ts` | No - execution deliverable | Read-only CVF continuity projection |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/workspace/state/route.ts` | No - execution deliverable | Read-only Web API endpoint |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/workspace/page.tsx` | No - execution deliverable | Operator dashboard route |
| focused tests for helper/API/page | No - execution deliverable | Guard parsing and UI regressions |
| `docs/reviews/CVF_WWU_T2_CVF_WEB_WORKSPACE_OPERATOR_DASHBOARD_READ_MODEL_COMPLETION_2026-06-18.md` | No - execution deliverable | Closure evidence |

## Forbidden Path Manifest

| Path | Reason |
|---|---|
| `CVF_SESSION_MEMORY.md` | protected continuity; material range must read only |
| `CVF_SESSION/**` | protected generated/session state; material range must read only |
| `AGENT_HANDOFF_V19_2026-06-15.md` | protected active handoff; material range must read only |
| `CVF_SESSION/agent_workspace/runtime_queue/**` | Local Runtime/queue scope parked under WWU-T3 |
| `docs/reference/mcp_gateway/**` | MCP scope parked |
| `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync` | public-sync not authorized |

## Forbidden Filesystem State At Dispatch

| Forbidden path | Expected state | Actual state at dispatch | Action if PRESENT |
|---|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/workspace/page.tsx` | ABSENT | ABSENT | N/A |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/workspace/state/route.ts` | ABSENT | ABSENT | N/A |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/cvf-workspace-read-model.ts` | ABSENT | ABSENT | N/A |

## Required Proof Manifest

| Proof | Path | Required literal | Required at handoff |
|---|---|---|---|
| Active CVF mode is not chat mode | read-model helper/test | `activeSessionMode` | No - execution deliverable |
| Read-only route | API route/test | `GET` | No - execution deliverable |
| Web/runtime split | completion review | `CVF_WEB_WORKSPACE` | No - execution deliverable |
| No Local Runtime/MCP claim | completion review | `no Local Runtime/MCP` | No - execution deliverable |

## Evidence Requirements

Completion must include:

- execution base and material changed-path list;
- updated Source Verification Block with current line/source evidence;
- negative search results after implementation;
- `npm run check` result from `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`;
- focused tests for helper/API/page, or a source-backed blocker;
- `git diff --check`;
- `python governance/compat/run_worker_return_fast_gate.py`;
- pre-closure autorun result on the material range;
- Public Export Disposition;
- Finding-To-Governance Learning Disposition for every reusable finding;
- explicit claim boundary excluding Local Runtime/MCP, provider/live,
  public-sync, readiness, and runtime enforcement.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Read-only helper projects active session mode, next allowed move, active handoff, roadmap/work-order state, evidence/guard links, and parked checkpoints from CVF-governed sources. |
| AC2 | `GET /api/workspace/state` returns the projection and performs no mutation. |
| AC3 | `/workspace` renders an operator dashboard in the existing dashboard shell and follows DESIGN.md operational dashboard rules. |
| AC4 | New route is reachable through existing navigation without removing Work Transfer, Runtime Monitor, Governance, or other existing links. |
| AC5 | Tests cover helper parsing, API route, and dashboard rendering. |
| AC6 | Material changed set stays inside Write Ownership. |
| AC7 | Completion records no Local Runtime/MCP/provider/live/public-sync/readiness claim. |

## Review Gate

Before accepting the material range, Codex must confirm:

- changed paths stay inside Write Ownership;
- no protected session/handoff paths appear in the material range;
- no Local Runtime/MCP/provider/live/public-sync/raw external package files
  appear in the material range;
- no UI action mutates governed state;
- tests/check evidence is current;
- findings have governed disposition;
- pre-closure autorun gate and commit steward preflight pass on a real range.

## Closure Checklist

| Item | Required disposition at closure |
|---|---|
| Required first reads completed | PASS or BLOCKED with reason |
| Source Verification Block recomputed | PASS or BLOCKED with reason |
| Read-only helper/API/page implemented | PASS or BLOCKED with reason |
| Focused tests/checks run | PASS or BLOCKED with reason |
| Material changed paths inside ownership | PASS or BLOCKED with reason |
| No protected session/handoff material mutation | PASS |
| No Local Runtime/MCP/provider/live/public-sync/readiness claim | PASS |
| Completion review filed | PASS |
| Session-sync split if next move changes | PASS or N/A with reason |

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` if:

- required source facts are missing;
- current `cvf-web` structure conflicts with the planned route/helper and the
  fix would exceed Write Ownership;
- focused tests or `npm run check` fail outside allowed scope;
- implementation requires Local Runtime/MCP, provider/live proof, credentials,
  public-sync, active session mutation in material range, or readiness claims.

## Verification To Run Before Closure

```powershell
Push-Location EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npm run check
<focused test command for helper/API/page>
Pop-Location
git diff --check
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <materialBaseHead> --head HEAD
python governance/compat/run_agent_commit_steward_preflight.py --mode closure --base <materialBaseHead> --head HEAD --enforce
```

Use the actual material base/head range. An empty self-range is not closure
evidence.

## Operator Checkpoint

No operator checkpoint is needed for allowed read-only Web Workspace
implementation and tests. Operator decision is required before Local
Runtime/MCP, provider/live proof, secrets/quota, public-sync, active session
mutation in material range, readiness claims, destructive actions, or scope
expansion.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| GC-018 baseline | `docs/baselines/CVF_GC018_WWU_T2_CVF_WEB_WORKSPACE_OPERATOR_DASHBOARD_READ_MODEL_2026-06-18.md` | dispatch baseline packet retained as source authority | PASS |
| Roadmap state | `docs/roadmaps/CVF_WEB_WORKSPACE_UPGRADE_ROADMAP_2026-06-18.md` | WWU-T2 row `CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_WWU_T2_CVF_WEB_WORKSPACE_OPERATOR_DASHBOARD_READ_MODEL_COMPLETION_2026-06-18.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | generated from source entries if registry changed | PASS after generation |
| Registry Markdown | BLOCKED with reason: no separate markdown registry exists for this reference family | no path changed | BLOCKED with reason |
| External evidence digest | N/A with reason: no external evidence consumed in dispatch | repo-local governed artifacts only | N/A with reason |
| System loop interlock | N/A with reason: no runtime interlock mutation authorized | no interlock path changed | N/A with reason |
| Session continuity | separate session-sync follows material commit | active session surfaces update only following accepted material commit if next move changes | N/A with reason |
| Runtime/provider proof | BLOCKED with reason: runtime/provider proof is forbidden in WWU-T2 | no provider/live receipt accepted | BLOCKED with reason |

## Acceptance Receipt Assertion Matrix

| Criterion | Required value | Observed value | Status |
|---|---|---|---|
| Work order closure state | `CLOSED_PASS_BOUNDED` | this packet is closed by completion review | PASS |
| Runtime proof boundary | no provider/network proof | no provider command authorized | PASS |
| Receipt boundary | local completion/evidence only | no live receipt produced in dispatch | PASS |
| Local Runtime/MCP boundary | forbidden | WWU-T3 remains parked | PASS |
| Public boundary | private only | no public-sync authorized | PASS |

## Finding-To-Governance Learning Disposition

| Field | Disposition |
|---|---|
| Defect class | `ORCHESTRATOR_PACKET_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Escalation state | `WORK_ORDER_ADDED` |
| Next control action | Implement the WWU-T2 read-only Web Workspace dashboard before any governed action-request or Local Runtime/MCP work |
| Worker blame | `N/A_WITH_REASON`: this work order releases a WWU-T1 identified read-model gap |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance Web Workspace work order. No public-sync batch is
authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-18 WWU-T2 work order dispatch |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, governance gates |
| Target paths | WWU roadmap; WWU-T2 GC-018; this work order; GC-051 registry source entry |
| Allowed scope source | active session next allowed move following WWU-T1 material commit `3db83d3b` and session-sync commit `93540bbf` |
| Before status evidence | base `93540bbf`; clean worktree before dispatch authoring |
| After status evidence | WWU-T2 dispatch material diff ready for commit |
| Diff evidence | `git diff --name-status 93540bbf..HEAD` |
| Approval boundary | work-order dispatch only |
| Claim boundary | no product source implementation in dispatch batch; no runtime/provider/live/public-sync/readiness claim |
| Agent type | Codex |
| Invocation ID | `wwu-t2-cvf-web-workspace-operator-dashboard-read-model-codex-2026-06-18` |
| Expected manifest | N/A with reason: dispatch-ready work order names future execution paths in Write Ownership, so AOT exact-manifest comparison is deferred to material implementation |
| Actual changed set | N/A with reason: dispatch-ready work order names future execution paths in Write Ownership, so AOT exact-manifest comparison is deferred to material implementation |
| Manifest delta | N/A with reason: dispatch-ready work order names future execution paths in Write Ownership, so AOT exact-manifest comparison is deferred to material implementation |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This work order authorizes only a read-only CVF Web Workspace operator
dashboard/read model. It does not authorize Local Runtime/MCP, provider/live
proof, credential use, public-sync, runtime enforcement, production readiness,
public readiness, release-facing readiness, or external-facing readiness.
