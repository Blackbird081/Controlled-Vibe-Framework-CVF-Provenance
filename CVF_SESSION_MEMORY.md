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

Startup acknowledged: current mode=`cadp_ai_t2_dispatched_worker_must_not_commit`; active handoff=AGENT_HANDOFF_V59_2026-08-11.md; next allowed move=implementation worker executes the committed T2 exact-manifest packet and returns uncommitted evidence for independent review; parked checkpoint=F11 acceptance, T3+, runtime/provider/live, CLI/MCP, public sync, deploy and production.

## Current Mode

`cadp_ai_t2_dispatched_worker_must_not_commit`

Current mode marker: `cadp_ai_t2_dispatched_worker_must_not_commit`
Current mode: `cadp_ai_t2_dispatched_worker_must_not_commit`
Previous mode: `cadp_ai_t1_accepted_bounded_t2_packet_authoring_authorized`

## Next Allowed Move

Mode: `cadp_ai_t2_dispatched_worker_must_not_commit`

CADP-AI-T2 is dispatched at `9f08655f3d755873ad15854843dd015c56e8d95d`
under `WORKER_MUST_NOT_COMMIT`. The worker may execute only the exact 11-path
maximum manifest, must capture execution base, run hermetic proof, create the
required return and stop uncommitted for independent review. F11 remains open.
Latest closed numbered LHW wave: `LHW24`.

## Parked Checkpoints

F11 acceptance, T3+, runtime, provider/live, CLI/MCP, public sync, deployment,
production and cross-runtime determinism claims remain parked. Prior unrelated
checkpoints remain historical.

The `broad external knowledge absorption` lane remains outside the current
release. It is included in the `blocked work classes` unless the operator opens
a fresh, source-verified governed tranche.

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
