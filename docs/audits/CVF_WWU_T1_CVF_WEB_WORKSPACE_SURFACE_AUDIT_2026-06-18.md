# CVF WWU-T1 CVF Web Workspace Surface Audit

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-18

docType: audit

## Purpose

Map current `cvf-web` operator-facing and governance-facing surfaces before
building a CVF Web Workspace dashboard/read model.

## Scope / Target / Owner Boundary

Target: current `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web` pages,
components, route handlers, and existing Web governance inventory relevant to
the `CVF_WEB_WORKSPACE` layer.

Owner boundary: source-verification audit only. This audit does not implement
UI, mutate runtime state, implement MCP/CLI, run providers, public-sync, import
raw external package code, or claim production/public readiness.

## Source Authority

| Source | Role |
|---|---|
| `docs/reference/agent_workspace/CVF_WORKSPACE_TWO_LAYER_ARCHITECTURE_STANDARD.md` | Web/runtime boundary |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPERATOR_VIEW_PLAN.md` | operator read-model target |
| `docs/roadmaps/CVF_WEB_WORKSPACE_UPGRADE_ROADMAP_2026-06-18.md` | WWU sequencing |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/docs/reference/CVF_W112_WEB_GOVERNANCE_SURFACE_INVENTORY_2026-04-22.md` | existing Web governance inventory |
| Current `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/**` source | route/component/API surface evidence |

## Current Surface Map

| Surface | Source evidence | Current role | WWU-T2 disposition |
|---|---|---|---|
| Main Web entry | `src/app/page.tsx` returns landing page and redirects template/category to `/home` | product landing/home entry, not active CVF session workspace | do not make first WWU-T2 screen depend on root landing |
| Sidebar workspace/platform navigation | `src/components/Sidebar.tsx` lines 149-150, 209-210, 228-239 | existing nav groups include Workspace, Work Transfer, Runtime Monitor, Governance | reuse navigation placement, but add a distinct CVF Workspace route instead of overloading chat mode |
| Governance hub | `src/app/(dashboard)/governance/page.tsx` lines 27-30 and 134-152 | links System Health, Runtime Modules, Evidence State, Web Operations | reuse as related governance area; dashboard should summarize and deep-link |
| Evidence state | `src/app/(dashboard)/governance/evidence/page.tsx` lines 42-55, 126-166 | server-rendered evidence/gate state view | reuse as evidence panel source or linked detail view |
| System health | `src/app/(dashboard)/governance/system-health/page.tsx` lines 57-71, 126-136 | server-rendered local install/provider/release-proof readiness | reuse as guard/readiness panel source with no provider run |
| Web operations | `src/app/(dashboard)/governance/operations/page.tsx` lines 110-145 | client view that lists/submits allowlisted jobs through `/api/system/jobs` | keep out of first read-only dashboard except as a linked governed-action area |
| Approval inbox | `src/components/ApprovalInbox.tsx` lines 81-99 | lists approvals and patches approval decisions | later governed-action candidate; first dashboard may show counts/links only |
| Work transfer page | `src/app/(dashboard)/work-transfer/page.tsx` lines 13-14, 97-100 | manual work-transfer record generation | useful UX precedent, but not a CVF session-state source |
| Existing Web governance inventory | `cvf-web/docs/reference/CVF_W112_WEB_GOVERNANCE_SURFACE_INVENTORY_2026-04-22.md` `## Surface Inventory` | classifies governed execution, approval, evidence-read, and policy-mutation routes | carry forward as source verification input, not as workspace completeness proof |

## Current API / Data Surface Map

| API or server function | Source evidence | Current role | WWU-T2 disposition |
|---|---|---|---|
| `/api/system/jobs` | `src/app/api/system/jobs/route.ts` lines 29-60; `src/lib/server/web-governance-jobs.ts` lines 405-580 | list/submit allowlisted governance jobs with audit events and quota preflight | not first-dashboard mutation surface; may expose latest job audit summary read-only |
| `/api/system/health` | `src/app/api/system/health/route.ts` lines 6-7; `src/lib/server/system-health.ts` lines 118-290 | read local install/provider/release-proof readiness; explicit read-only boundary at lines 269-273 | reusable for health panel |
| `/api/governance/evidence` | `src/app/api/governance/evidence/route.ts` lines 6-7; `src/lib/server/governance-evidence.ts` lines 191-224 | read release gate, provider lane, evidence locations, policy snapshots; boundary says read-only | reusable for evidence panel |
| `/api/governance/ledger` | `src/app/api/governance/ledger/route.ts` lines 6-46 | paginated governance ledger read | possible linked evidence detail, not session continuity source |
| `/api/approvals` and `/api/approvals/[id]` | `src/app/api/approvals/route.ts` lines 24-171; `src/app/api/approvals/[id]/route.ts` lines 11-118 | approval create/list and review mutation | first WWU-T2 should avoid new approval mutation; later action-request tranche may use it |
| `/api/sessions` and `/api/sessions/[id]` | `src/app/api/sessions/route.ts` lines 4-40; `src/app/api/sessions/[id]/route.ts` lines 4-78 | chat/session storage | not CVF active session state |

## Gap Analysis Against Operator Read Model

| Required Web Workspace read-model item | Current `cvf-web` coverage | Gap |
|---|---|---|
| Current mode | No active CVF session-state endpoint found; `currentMode` in `src/components/AgentChatHeader.tsx` and `src/lib/hooks/useAgentChat.ts` is chat/spec mode | needs dedicated CVF session-state read model from `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| Next allowed move | No route found for `nextAllowedMove` or `CVF_SESSION_MEMORY.md` | needs read-only continuity projection |
| Active handoff | No route found for `activeHandoff` or active handoff summary | needs read-only active-handoff projection and link/source path |
| Parked checkpoints | Session front door has parked lanes, but Web has no projection | needs parsed bounded summary, not provider-memory text |
| Roadmap/work-order/work-return status | Web has docs/knowledge/governance pages, but no current CVF roadmap/work-order read model | needs a minimal governed-artifact summary |
| Evidence and receipts | Evidence page and `/api/governance/evidence` exist | can reuse/link, but must not imply fresh live proof |
| Guard status | System health and job audit surfaces exist | can reuse/link; first dashboard should read only |
| Operator decisions | Approval inbox exists for Web governance approvals | keep as link/count first; governed action requests require separate tranche |

## Findings

| Finding | Evidence | Disposition |
|---|---|---|
| WWU-T2 should not start by building Local Runtime/MCP. | Two-layer standard separates `CVF_WEB_WORKSPACE` and `CVF_LOCAL_WORKSPACE_RUNTIME`; current roadmap parks WWU-T3. | ACCEPT |
| Current Web already has governance/evidence/health/operations surfaces that can be linked or summarized. | Governance hub links four related views; evidence and health pages read server-side reports. | ACCEPT |
| Current Web does not expose CVF active session state, active handoff, next allowed move, or parked checkpoints as a first-class read model. | Route search found chat `/api/sessions` but no active-session/handoff/workspace route. | ACCEPT |
| Existing chat/spec `currentMode` is not CVF session mode. | `rg` shows `currentMode` in `AgentChatHeader` and `useAgentChat`, while no `ACTIVE_SESSION_STATE` use appears under `src`. | ACCEPT |
| Existing operations and approval controls are governed action surfaces, not the minimal first dashboard. | Operations page POSTs `/api/system/jobs`; ApprovalInbox PATCHes `/api/approvals/{id}`. | ACCEPT |

## Risk / Corrective Action

| Risk | Corrective action |
|---|---|
| A future UI tranche may confuse chat `currentMode` with CVF session mode. | WWU-T2 must name its read model `activeSessionMode` or equivalent, not reuse chat-mode state. |
| A future dashboard may treat Web operations as Local Runtime/MCP enforcement. | WWU-T2 must keep operation buttons out of the first read-only dashboard and deep-link existing governed operations only. |
| A future UI may claim fresh proof from stale evidence summaries. | WWU-T2 must label evidence as recorded/read-only unless a separate live proof is authorized and receipt-backed. |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next action | Handled or deferred |
|---|---|---|---|---|---|
| Current `cvf-web` lacks an active CVF session-state/handoff/workspace read model. | RULE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | WWU-T2 fresh GC-018 must source-verify a read-only continuity projection from CVF Core state. | deferred to WWU-T2 |
| Chat/spec `currentMode` collides with CVF session `currentMode` vocabulary. | OPERATOR_SCOPE_CLARITY_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | WWU-T2 work order must require explicit `activeSessionMode` naming or equivalent. | deferred to WWU-T2 |
| Existing operations/approval surfaces are action surfaces, not the first read-only workspace. | OPERATOR_SCOPE_CLARITY_GAP | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | Keep Workspace Two-Layer Control Block boundary; action requests require separate governed tranche. | handled by existing two-layer rule |
| Runtime/provider/cost learning from this audit. | RUNTIME_SIGNAL_GAP | DOCUMENTATION_ONLY_LEARNING | N/A_WITH_REASON | No runtime/provider/cost behavior was executed or diagnosed in WWU-T1. | handled in this audit |

Generalizable finding promotion: `DESIGN_REVIEW_REQUIRED` and existing
Workspace Two-Layer Control Block requirements route the reusable Web-read-model
gaps into WWU-T2 instead of provider memory or chat-only continuity.

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Runtime/provider receipt accepted in WWU-T1 | N/A with reason: audit-only tranche | No runtime/provider receipt is created or accepted | PASS |
| Evidence/receipt terms in audit packet | read-model target only | Existing evidence route is mapped as future dashboard input; no new proof claim is made | PASS |

## Minimal WWU-T2 Recommendation

WWU-T2 should be split as a read-only Web Workspace dashboard/read model:

1. Add a server-side read model that safely reads CVF Core continuity surfaces:
   `CVF_SESSION/ACTIVE_SESSION_STATE.json`, `CVF_SESSION_MEMORY.md`, active
   handoff named by the state registry, and selected roadmap/work-order/review
   artifacts.
2. Add a compact operator dashboard route, for example `/workspace`, with
   sections for Current Mode, Next Move, Active Handoff, Roadmap/Work Order
   Status, Evidence/Receipts, Guard Status, and Parked Checkpoints.
3. Deep-link existing Evidence, System Health, Governance Operations, Approval
   Inbox, and Work Transfer pages instead of duplicating their full behavior.
4. Keep all mutation controls out of the first tranche except links to existing
   governed surfaces. New action-request buttons require a later work order.
5. Read `DESIGN.md` before any frontend implementation.

## WWU-T2 Fresh GC-018 Requirements

The next implementation packet must include:

- fresh GC-018;
- source-verified work order;
- Agent Handoff Contract Control Block;
- Agent Workspace Design Control Block;
- Workspace Two-Layer Control Block with `targetLayer=CVF_WEB_WORKSPACE`;
- `DESIGN.md` first-read evidence;
- no Local Runtime/MCP mutation;
- focused type/UI tests.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Audit packet | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_WWU_T1_CVF_WEB_WORKSPACE_SURFACE_AUDIT_FOR_CODEX_2026-06-18.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_WWU_T1_CVF_WEB_WORKSPACE_SURFACE_AUDIT_COMPLETION_2026-06-18.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| GC-018 | `docs/baselines/CVF_GC018_WWU_T1_CVF_WEB_WORKSPACE_SURFACE_AUDIT_2026-06-18.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_WEB_WORKSPACE_UPGRADE_ROADMAP_2026-06-18.md` | `ROADMAP_T1_CLOSED_T2_READY_FOR_GC018_T3_PARKED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | generated from source entries | PASS |
| Registry Markdown | BLOCKED with reason: no separate markdown registry is required for this reference family | no path changed | BLOCKED with reason |
| External evidence digest | BLOCKED with reason: no new external package/source was consumed in WWU-T1 | no external evidence digest required | BLOCKED with reason |
| System loop interlock | BLOCKED with reason: no runtime interlock implementation changed | no path changed | BLOCKED with reason |
| Session continuity | separate session-sync follows material commit | active session surfaces update after material commit because next move changes | N/A with reason |
| Runtime proof | BLOCKED with reason: runtime/provider/MCP proof is out of scope | no runtime proof required | BLOCKED with reason |
| Public export disposition | `DEFERRED_PRIVATE_ONLY` | private provenance audit packet | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance source audit. Public-facing wording requires a
separate public-sync authorization.

## Claim Boundary

This audit maps current Web surfaces and recommends the smallest next tranche.
It does not implement UI, runtime/MCP, provider calls, public-sync, or
readiness.
