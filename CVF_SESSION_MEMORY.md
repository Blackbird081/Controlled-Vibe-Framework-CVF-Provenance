# ACTIVE SESSION FRONT DOOR

Memory class: active-session-front-door

Status: ACTIVE

Last compacted: 2026-08-11

## Startup Order

Read progressively, stopping once current facts are resolved; the full
history/state aggregate is a targeted lookup, not a default startup step:

1. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` (compact current
   facts: current mode, active handoff, next allowed move)
2. this front door
3. `AGENT_HANDOFF_V59_2026-08-11.md`
4. only the current-authority paths those two surfaces name for the task
5. `CVF_SESSION/ACTIVE_SESSION_STATE.json` only as a targeted lookup, when a
   current fact above is missing, contradictory, or the task explicitly
   requires historical evidence

Canonical read-budget standard:
`docs/reference/CVF_ACTIVE_CONTINUITY_READ_BUDGET_STANDARD_2026-08-10.md`.
Machine guard: `governance/compat/check_active_session_state.py`.

Read `DESIGN.md` only when touching Web, UI, or dashboard work. Read
`docs/reference/guard_orientation/README.md` before authoring a governed
artifact.

## Active Pointers

| Field | Path |
|---|---|
| Bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Canonical state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| Active handoff | `AGENT_HANDOFF_V59_2026-08-11.md` |
| Active review queue | `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` |
| Pain-point closure direction | `docs/reviews/archive/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md` |
| Historical handoffs | `CVF_SESSION/handoffs/archive/` |
| Prior handoff (archive-qualified) | `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V58_2026-08-11.md` |
| Latest front-door archive | `CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-08-11.md` |
| Current authority (baseline/work order + hashes) | `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json` `currentAuthority` |
| Freeze posture | `governance_kernel_freeze_recommended` |

## Startup Acknowledgment

Startup acknowledged: current mode=`local_retention_artifact_roadmap_closed_next_operator_selection`; active handoff=AGENT_HANDOFF_V59_2026-08-11.md; next allowed move=operator selects a different roadmap; parked checkpoint=MAO T1, ZIP deletion, archive import, DESIGN, BUILD, runtime, provider/live, public `main` merge, deploy, hosted smoke, secrets, store, and production.

## Current Mode

`local_retention_artifact_roadmap_closed_next_operator_selection`

Current mode marker: `local_retention_artifact_roadmap_closed_next_operator_selection`
Current mode: `local_retention_artifact_roadmap_closed_next_operator_selection`
Previous mode: `local_retention_artifact_t2_terminal_disposition_dispatched`

## Next Allowed Move

Mode: `local_retention_artifact_roadmap_closed_next_operator_selection`

LRA-T2 is accepted and T4 closes the roadmap with
`RETAIN_SINGLE_PINNED_ARCHIVE`. No further LRA tranche is authorized. The
operator may select a different roadmap; MAO T1 and archive deletion remain
parked. No source/runtime/provider/public
scope is open.
Latest closed numbered LHW wave: `LHW24`.

## Parked Checkpoints

Public staging push is complete at `origin/lpci1-ref-staging@021f8b852`.
MAO T1, DESIGN, BUILD, Netlify deployment, hosted/provider/store, secrets,
production, and public `main` merge remain parked.

## Targeted Lookup Rules

- For complete canonical state, read `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- For prior T2A closure narrative, read
  `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V58_2026-08-11.md`; do not
  restate it here.
- For pre-2026-08-11 front-door history, read the front-door archive above.
- For guard/task orientation, read
  `docs/reference/guard_orientation/README.md`.

## Claim Boundary

This is a compact current-only pointer record. It carries no closed-tranche
narrative; historical evidence lives in the dated archives listed above.
