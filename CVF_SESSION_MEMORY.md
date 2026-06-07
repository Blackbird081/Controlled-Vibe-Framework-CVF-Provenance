# CVF Session Memory Front Door

Memory class: POINTER_RECORD

Status: ACTIVE SESSION FRONT DOOR

Last updated: 2026-06-07

Current mode marker: `governance_fast_reviewer_gate_and_front_door_rotation`
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

Current mode: `governance_fast_reviewer_gate_and_front_door_rotation`.

Active handoff:

`AGENT_HANDOFF_V17_2026-06-07.md`

Active state registry:

`CVF_SESSION/ACTIVE_SESSION_STATE.json`

Active review queue:

`CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`

Pain-point closure direction:

`docs/reviews/archive/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md`

## Latest Continuity Note

Governance Fast Reviewer Gate and front-door rotation are in progress from
base `82b53975`.

Planned scope:

- add a `reviewer-fast` local governance hook mode for reviewer-return
  preflight before full commit;
- run latency-sensitive local hook modes in parallel by default, with
  `--serial` available for debugging;
- archive predecessor handoff
  `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V16_2026-06-06.md` and keep
  active V17 compact;
- keep this front door compact.

Latest closed product/control-plane note:

DSCP-T1 Owner Surface Map is `CLOSED_PASS_BOUNDED` at material commit
`62fa6943`, with session sync at `82b53975`.

Roadmap:
`docs/roadmaps/CVF_DSCP_DOMAIN_AGNOSTIC_SCAN_CONTEXT_PACK_READINESS_ROADMAP_2026-06-07.md`.

Completion:
`docs/reviews/CVF_DSCP_T1_OWNER_SURFACE_MAP_COMPLETION_2026-06-07.md`.

Boundary: DSCP-T1 is doc-only. No DSCP-T2 implementation, runtime pilot,
corpus ingestion, provider call, public-sync, production readiness, or public
readiness is authorized by this note.

## Next Allowed Move

Close the Governance Fast Reviewer Gate and front-door rotation batch.

After closure, recommended next roadmap is DSCP-T2 Standard Contract Authoring
from the accepted DSCP-T1 schema proposal, bounded to TypeScript contracts and
tests only. DSCP-T2 must not claim runtime pilot, corpus ingestion, provider
calls, public-sync, production readiness, or public readiness without a fresh
operator-authorized work order.

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
