# CVF Session Memory Front Door

Memory class: POINTER_RECORD

Status: ACTIVE SESSION FRONT DOOR

Last updated: 2026-06-08

Current mode marker: `dscp_t7_closed_pass_bounded`
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

Current mode: `dscp_t7_closed_pass_bounded`.

Active handoff:

`AGENT_HANDOFF_V17_2026-06-07.md`

Active state registry:

`CVF_SESSION/ACTIVE_SESSION_STATE.json`

Active review queue:

`CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`

Pain-point closure direction:

`docs/reviews/archive/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md`

## Latest Continuity Note

DSCP-T7 ECO Multi-Domain Pilot is `CLOSED_PASS_BOUNDED` in the current closure
batch.

Delivered scope:

- DSCP-T6 deterministic `buildGovernedArtifactDescriptor()` helper and focused
  tests from worker return;
- GC-051 registry coverage for the new T6 source/test paths;
- dispatch-quality checker hardening for pending predecessor release language,
  noncanonical Source Verification dispositions, and deferred worker/future
  source verification;
- T6 completion review:
  `docs/reviews/CVF_DSCP_T6_SCAN_DESCRIPTOR_RUNTIME_COMPLETION_2026-06-08.md`;
- T7 deterministic `buildECOGovernedPackRequest()` adapter and focused tests;
- T7 completion review:
  `docs/reviews/CVF_DSCP_T7_ECO_MULTI_DOMAIN_PILOT_COMPLETION_2026-06-08.md`;
- T7 `KnowledgeItem` mapping corrected to current source fields;
- T8 remains dependency-controlled until refreshed T7 release evidence is
  applied.

Boundary: T6 deterministic local helper plus governance checker/docs cleanup
only; no provider call, corpus ingestion, T7/T8 execution, T12 authorization,
public-sync, production readiness, public readiness, or live governance proof.

## Next Allowed Move

Next allowed move: refresh DSCP-T7 dependency-release evidence and execute
DSCP-T8 MKE1 Cross-Lane Wire-In.

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
