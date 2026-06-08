# CVF Session Memory Front Door

Memory class: POINTER_RECORD

Status: ACTIVE SESSION FRONT DOOR

Last updated: 2026-06-08

Current mode marker: `dscp_t5_parent_roadmap_source_freshness_consolidation_dispatched`
Enforcement posture: `agent_autorun_workflow_control_enforced`
Freeze posture marker: `governance_kernel_freeze_recommended`

---

## Purpose

This file is the compact startup front door for new or resumed CVF agents.
It points to canonical state instead of carrying long history.

Previous long front-door snapshot:

`CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_PRE_ROTATION_ARCHIVE_2026-05-28.md`

Active handoff predecessor archived in this batch:

`CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V16_2026-06-06.md`

## Startup Order

1. Read this file.
2. Resolve machine-readable state:
   `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. Resolve review queue:
   `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
4. Resolve active handoff from the state registry:
   `AGENT_HANDOFF_V17_2026-06-07.md`
5. Read mandatory startup guards listed in the state registry.

## Current State

Current mode: `dscp_t5_parent_roadmap_source_freshness_consolidation_dispatched`.

Active handoff:

`AGENT_HANDOFF_V17_2026-06-07.md`

Active state registry:

`CVF_SESSION/ACTIVE_SESSION_STATE.json`

Active review queue:

`CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`

Pain-point closure direction:

`docs/reviews/archive/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md`

## Latest Continuity Note

DSCP-T5 Parent Roadmap Source-Freshness Consolidation is `DISPATCHED` at commit
`ca3f5f9c`.

Delivered scope:

- added post-T4 audit
  `docs/audits/CVF_DSCP_POST_T4_NEXT_ROADMAP_AUDIT_2026-06-08.md`;
- added GC-018 baseline
  `docs/baselines/CVF_GC018_DSCP_T5_PARENT_ROADMAP_SOURCE_FRESHNESS_CONSOLIDATION_2026-06-08.md`;
- added T5 roadmap
  `docs/roadmaps/CVF_DSCP_T5_PARENT_ROADMAP_SOURCE_FRESHNESS_CONSOLIDATION_ROADMAP_2026-06-08.md`;
- added Claude work order
  `docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T5_PARENT_ROADMAP_SOURCE_FRESHNESS_CONSOLIDATION_FOR_CLAUDE_2026-06-08.md`;
- updated parent DSCP roadmap with T5 `DISPATCHED` row.

Previous product/control-plane note:

DSCP-T1 Owner Surface Map is `CLOSED_PASS_BOUNDED` at material commit
`62fa6943`, with session sync at `82b53975`.

Roadmap:
`docs/roadmaps/CVF_DSCP_DOMAIN_AGNOSTIC_SCAN_CONTEXT_PACK_READINESS_ROADMAP_2026-06-07.md`.

Completion:
`docs/reviews/CVF_DSCP_T1_OWNER_SURFACE_MAP_COMPLETION_2026-06-07.md`.

Boundary: DSCP-T5 is documentation/source-freshness dispatch only. It does not
claim TypeScript modification, runtime behavior, provider call, live retrieval
query, response hash computation, corpus ingestion, T12 authorization,
public-sync, production readiness, public readiness,
provider-quality/cost/performance claim, memory reinjection, high-risk
promotion, Learning Orchestrator runtime behavior, or autonomous mutation.

## Next Allowed Move

Next allowed move: Claude executes T5 work order
`docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T5_PARENT_ROADMAP_SOURCE_FRESHNESS_CONSOLIDATION_FOR_CLAUDE_2026-06-08.md`
under `WORKER_MUST_NOT_COMMIT` and returns staged/uncommitted artifacts.

LHW24 remains the latest closed numbered LHW wave in the state registry.

LPCI2-T12 remains forbidden until a separate operator-authorized evidence path
resolves EC-02 review on or after 2026-07-01, known `currentStatus`, known
`jurisdiction`, and a later eligibility re-evaluation produces at least one
`t12Eligible=YES` candidate.

The prior product lanes remain parked:

- DEP2 next-auth stable migration: `HARD_BLOCKED`;
- external receipt-anchor provider/service selection:
  `PARKED_PENDING_OPERATOR_DECISION`;
- live Redis service proof: `PARKED_PENDING_CREDENTIALS`.

LHW24 remains the latest closed numbered LHW wave in the state registry.

## Active Rule Additions

Agents must use the active standards named in `AGENTS.md` and the machine
guards named in `CVF_SESSION/ACTIVE_SESSION_STATE.json`. This pointer record
does not duplicate those long rules.

## Enforcement

Startup acknowledgment, active-session state compatibility, autorun workflow
gates, and governed file-size checks enforce this front-door contract.

## Related Artifacts

- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
- `AGENT_HANDOFF_V17_2026-06-07.md`
- `governance/compat/check_active_session_state.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_local_governance_hook_chain.py`

## Claim Boundary

This front door is a pointer record only. It does not prove runtime behavior,
provider behavior, hosted freshness, public readiness, production readiness, or
automatic loading by external agents.
