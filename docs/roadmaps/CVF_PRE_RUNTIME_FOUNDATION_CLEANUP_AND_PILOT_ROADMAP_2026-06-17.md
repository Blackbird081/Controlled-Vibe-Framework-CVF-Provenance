# CVF Pre-Runtime Foundation Cleanup And Pilot Roadmap

Memory class: FULL_RECORD

Status: ROADMAP_READY_FOR_T1_GC018

docType: roadmap

Date: 2026-06-17

Owner: Codex

rawMemoryReleased: false

Roadmap class: governance-foundation-pre-runtime-cleanup

## Purpose

Prepare CVF for a later runtime pilot by cleaning the highest-value governance
foundation seams first. This roadmap covers the three operator-approved options:

1. reconcile the stale CCLV-T2 state/roadmap surfaces;
2. run a small CCLV-T3 Central Core + Local View pilot;
3. implement the PLCS companion-routing checker/interlock follow-up.

The intent is to reduce agent context-scanning ambiguity before runtime work
creates new queue records, state items, closure packets, or operator-facing
views.

## Scope / Target / Owner Boundary

Target: govern the next pre-runtime cleanup tranche sequence after AHB-Tn.8
through AHB-Tn.10 closed the workspace runtime-readiness foundation.

Owner boundary: this roadmap owns sequencing and acceptance criteria only.
Each tranche still requires fresh GC-018, source-verified work order, autorun
gates, and separate closure evidence before implementation.

## Authorization / Decision

Operator instruction on 2026-06-17: inspect whether a roadmap has higher value
than immediate runtime, then create a roadmap for options 1, 2, and 3.

Decision: prefer pre-runtime foundation cleanup over opening workspace runtime.
Runtime execution remains parked until these higher-value governance seams are
clean or explicitly deferred by the operator.

## Source Authority

- Active session front door:
  `CVF_SESSION_MEMORY.md`
- Active state registry:
  `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- Active handoff:
  `AGENT_HANDOFF_V19_2026-06-15.md`
- CCLV roadmap:
  `docs/roadmaps/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_ROADMAP_2026-06-16.md`
- CCLV-T2 completion and audit:
  `docs/reviews/CVF_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_COMPLETION_2026-06-16.md`
  and
  `docs/reviews/CVF_CCLV_T2_CLAUDE_ACTUAL_WORK_AUDIT_AND_RSF_T3_SELECTION_2026-06-16.md`
- CCLV checker:
  `governance/compat/check_central_facts_reference.py`
- PLCS roadmap:
  `docs/roadmaps/CVF_PLANE_LAYER_WORKFLOW_CHAIN_SYSTEMIZATION_ROADMAP_2026-06-16.md`
- PLCS-T3 decision:
  `docs/reference/CVF_PLCS_T3_COMPANION_ROUTING_CHECKER_TEMPLATE_DECISION_2026-06-16.md`
- Active workspace runtime-readiness foundation:
  `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md`

## Scope

In scope:

- update or dispatch a bounded state/roadmap reconciliation packet for CCLV-T2;
- pilot Central Core + Local View on one small closure workflow after the CCLV
  state surfaces are clean;
- implement a narrow PLCS companion-routing checker or interlock pre-dispatch
  gate for future FPC-T2 C01-C04 registry-edit work orders;
- preserve stable foundation storage/index rules and machine-readable state;
- update active session surfaces only when a tranche changes next allowed move.

Out of scope:

- executable workspace runtime queue;
- scheduler, worker daemon, UI implementation, provider/live proof, or
  public-sync;
- registry edits for FPC-T2 C01-C04 themselves;
- Model Gateway redispatch, Model Gateway P3, new provider behavior, or
  product-runtime mutation;
- historical rewrite of closed artifacts beyond the minimum current-state
  reconciliation authorized by a fresh work order.

## Non-Goals

- Do not treat this roadmap as authorization to run workspace runtime.
- Do not implement PRFC-T1, PRFC-T2, or PRFC-T3 in the roadmap authoring batch.
- Do not use provider-local memory, chat history, or an unindexed folder as
  source authority.
- Do not rewrite closed historical artifacts unless a fresh PRFC-T1 work order
  proves that a current-state surface needs bounded reconciliation.
- Do not use PLCS checker work as a back door to edit FPC registry entries.
- Do not weaken local closure evidence merely because a central facts packet
  exists.

## Design Rule

Do not open runtime while the control plane still has avoidable context-scan
ambiguity. A future runtime tranche should consume clean current-state surfaces,
not ask agents to infer which roadmap, completion packet, or machine-readable
entry is fresher.

## Design Control Gate

| Control | Decision |
|---|---|
| Foundation value | High: lowers context-scan ambiguity before runtime generates more state |
| Scope size | Small to medium; each option stays its own tranche |
| Runtime risk | None authorized |
| Central Core + Local View posture | Mandatory by default for all three tranches |
| Foundation storage posture | Stable indexed paths required for any new foundation artifact |
| Claim boundary | Governance cleanup and pilot planning only |

## Tranche Plan

| Tranche | Status | Purpose | Owner |
|---|---|---|---|
| PRFC-T1 | CLOSED_PASS_BOUNDED | CCLV-T2 current-state reconciliation: align active state, CCLV roadmap, completion/audit pointers, and next-move language so no current surface implies CCLV-T2 is still paused after its accepted implementation | Codex |
| PRFC-T2 | READY_FOR_GC018 | CCLV-T3 pilot: use one small governance closure workflow to prove Central Core + Local View reduces duplicate shared facts without removing local judgment | Codex |
| PRFC-T3 | HOLD_UNTIL_T2_PASS_OR_OPERATOR_RELEASE | PLCS companion-routing checker/interlock: implement the PLCS-T3 approved companion block check for future FPC-T2 C01-C04 registry-edit work orders | Codex |

## Work Plan

1. PRFC-T1 authors fresh GC-018 and a source-verified work order for the CCLV-T2
   reconciliation. It should inspect actual commits, files, state entries, and
   active surfaces before any edit.
2. PRFC-T1 closes only after machine-readable state and local roadmap prose no
   longer disagree about whether CCLV-T2 is paused or closed.
3. PRFC-T2 selects a small closure workflow with repeated shared facts, creates
   one central facts packet, and keeps local artifacts as local views.
4. PRFC-T2 records operator readability and reviewer latency evidence. If the
   pilot creates more friction than it removes, CCLV-T4 must decide whether to
   limit the pattern.
5. PRFC-T3 adds the narrow PLCS checker/interlock placement only for changed
   future FPC-T2 C01-C04 registry-edit work orders. It must not edit the
   registry entries themselves.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | The roadmap records all three operator-approved options as bounded tranches. |
| AC2 | PRFC-T1 is sequenced before PRFC-T2 and PRFC-T3 because current-state ambiguity should be removed before pilots or new checks. |
| AC3 | Runtime execution remains parked and requires a separate fresh GC-018 plus source-verified work order. |
| AC4 | Each tranche preserves Central Core + Local View and foundation storage/index discipline. |
| AC5 | The roadmap authoring batch creates no work order, checker implementation, registry edit, provider/live proof, public-sync, production readiness, or public readiness claim. |

## PRFC-T1 Acceptance Criteria

| ID | Criterion |
|---|---|
| T1-AC1 | Source verification compares current `ACTIVE_SESSION_STATE.json`, CCLV roadmap, CCLV-T2 completion, CCLV-T2 audit, and checker/test files. |
| T1-AC2 | No current machine-readable state entry says CCLV-T2 is paused when accepted closure evidence exists, unless the packet records a precise bounded reason. |
| T1-AC3 | The CCLV roadmap status and tranche row are consistent with the accepted material/completion evidence. |
| T1-AC4 | Next-move surfaces do not dispatch stale CCLV-T2 work or stale Model Gateway work. |
| T1-AC5 | No runtime, provider/live, public-sync, or registry edit is introduced. |

## PRFC-T2 Acceptance Criteria

| ID | Criterion |
|---|---|
| T2-AC1 | The pilot has one central facts packet and at least two local views that reference it. |
| T2-AC2 | Local views retain role-specific judgment, dissent, evidence limits, and claim boundary. |
| T2-AC3 | The central facts packet is checked by the CCLV-T2 advisory checker. |
| T2-AC4 | Completion evidence states whether the pilot reduced duplicate fact edits. |
| T2-AC5 | No historical artifact is rewritten solely to demonstrate the pilot. |

## PRFC-T3 Acceptance Criteria

| ID | Criterion |
|---|---|
| T3-AC1 | The checker enforces the seven-field PLCS companion block only where PLCS-T3 made it mandatory: future FPC-T2 C01-C04 registry-edit work orders. |
| T3-AC2 | The checker does not require companion routing for unrelated work orders. |
| T3-AC3 | Focused tests cover missing block, incomplete field set, wrong candidate scope, and unrelated work-order exemption. |
| T3-AC4 | Hook/autorun placement matches the PLCS-T3 recommendation or records a bounded alternative with reason. |
| T3-AC5 | No FPC registry entry, runtime source, provider/live proof, public-sync, production readiness, or public readiness is claimed. |

## Verification / Evidence

Future tranches must provide:

- fresh GC-018 and source-verified work order;
- Roadmap-to-Work-Order Trace Matrix;
- Agent Handoff Contract Control Block if handoff semantics appear;
- Central Core + Local View disposition;
- Finding-To-Governance Learning disposition;
- machine gate output for the changed range;
- `git diff --check`;
- session-sync evidence if next allowed move or current mode changes.

## Finding-To-Governance Learning Disposition

| Field | Disposition |
|---|---|
| Defect class | `CURRENT_STATE_SURFACE_DRIFT` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Escalation state | `ROADMAP_ADDED` |
| Next control action | PRFC-T1 CCLV-T2 current-state reconciliation |
| Worker blame | `N/A_WITH_REASON`: the risk comes from multiple current-state surfaces aging differently after later closures |

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance governance roadmap. No public-sync batch is
authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex orchestrator |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-17 pre-runtime foundation cleanup roadmap authoring |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch |
| Target paths | `docs/roadmaps/CVF_PRE_RUNTIME_FOUNDATION_CLEANUP_AND_PILOT_ROADMAP_2026-06-17.md` |
| Allowed scope source | operator asked Codex to roadmap options 1, 2, and 3 after comparing higher-value CVF roadmaps |
| Before status evidence | clean worktree at HEAD before roadmap authoring |
| After status evidence | roadmap authored; pending material commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | roadmap only; no GC-018, work order, checker implementation, runtime, registry edit, provider/live proof, or public-sync |
| Claim boundary | planning and sequencing only |
| Expected manifest | `docs/roadmaps/CVF_PRE_RUNTIME_FOUNDATION_CLEANUP_AND_PILOT_ROADMAP_2026-06-17.md` |
| Actual changed set | `docs/roadmaps/CVF_PRE_RUNTIME_FOUNDATION_CLEANUP_AND_PILOT_ROADMAP_2026-06-17.md` |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This roadmap does not implement PRFC-T1, PRFC-T2, or PRFC-T3. It does not open
workspace runtime execution, provider/live proof, registry edits, public-sync,
Model Gateway work, production readiness, or public readiness. Each tranche
requires fresh GC-018 and a source-verified work order before implementation.
