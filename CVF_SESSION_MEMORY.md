# ACTIVE SESSION FRONT DOOR

Memory class: active-session-front-door
Status: ACTIVE
Last compacted: 2026-06-26

## Startup Order

Read these files before governed material work:

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
3. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
4. `AGENT_HANDOFF_V23_2026-06-26.md`
5. `docs/reference/guard_orientation/README.md`

For governed artifact authoring, also read:

`docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`

## Active Pointers

| Field | Path |
|---|---|
| Bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Canonical state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| Active handoff | `AGENT_HANDOFF_V23_2026-06-26.md` |
| Active review queue | `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` |
| Historical handoffs | `CVF_SESSION/handoffs/archive/` |
| Front-door archive snapshot | `CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-06-26.md` |

## Startup Acknowledgment

Startup acknowledged: current mode=`roadmap_status_reconciliation_sweep_closed_pass_bounded_pending_next_roadmap_selection`; active handoff=AGENT_HANDOFF_V23_2026-06-26.md; next allowed move=select the next high-value governed roadmap or open a fresh GC-018/source-verified work order before implementation; parked checkpoint=no validation semantics change, no runtime/provider/live proof, no public-sync, no generated aggregate mutation beyond session sync, no resolver mutation, no adapter mutation, and no push without separate authorization.

## Current Mode

Current mode marker: `roadmap_status_reconciliation_sweep_closed_pass_bounded_pending_next_roadmap_selection`

Current mode: `roadmap_status_reconciliation_sweep_closed_pass_bounded_pending_next_roadmap_selection`

`roadmap_status_reconciliation_sweep_closed_pass_bounded_pending_next_roadmap_selection`

Previous mode:

`rse_roadmap_status_reconciliation_closed_pass_bounded_pending_next_roadmap_selection`

## Latest Closed Work

| Work | Commit | Disposition |
|---|---|---|
| Orchestration command catalog refactor | `10dee6e9` | CLOSED_PASS_BOUNDED |
| Orchestration session sync | `f73546c5` | CLOSED_PASS |
| Guard binding catalog-aware checker hardening | `4927687c` | CLOSED_PASS_BOUNDED |
| ASSF Web projection schema/mapping dispatch | `b233ad46` | DISPATCH_READY |
| ASSF Web projection schema/mapping decision | `a408c13e` | CLOSED_PASS_BOUNDED |
| ASSF Web projection implementation dispatch | `0ba6eaee` | DISPATCH_READY |
| ASSF Web projection implementation | `0b57a4de` | CLOSED_PASS_BOUNDED |
| ASSF external-agent readout / CLI-MCP adapter boundary | `99fabd26` | CLOSED_PASS_BOUNDED |
| Governed artifact literal-format checklist learning | `13dcb7ad` | CLOSED_PASS_BOUNDED |
| ASSF external-agent metadata readout implementation dispatch | `ce102d77` | DISPATCH_READY |
| ASSF external-agent metadata readout implementation | `1f93ea33` | CLOSED_PASS_BOUNDED |
| ASSF metadata readout guard wiring dispatch | `810f3440` | DISPATCH_READY |
| ASSF metadata readout guard wiring | `e04ed428` | CLOSED_PASS_BOUNDED |
| AAF-T7A roadmap status reconciliation | `766f81e7` | CLOSED_PASS_BOUNDED |
| GFS-PY T2 lifecycle/status validator split | `3f7cb4e8` | CLOSED_PASS_BOUNDED |
| GFS-PY T3 source-verification/token-collision split | `f8f35e3e` | CLOSED_PASS_BOUNDED |
| GFS-PY T4 orchestrator-shell reduction / roadmap closure | `78798cd0` | CLOSED_PASS_BOUNDED |
| LSC roadmap status reconciliation | `46a1f17a` | CLOSED_PASS_BOUNDED |
| RSE roadmap status reconciliation | `23d99200` | CLOSED_PASS_BOUNDED |
| Roadmap status reconciliation sweep T0-T4 | `3ccf574c` | CLOSED_PASS_BOUNDED |

## Next Allowed Move

Mode: `roadmap_status_reconciliation_sweep_closed_pass_bounded_pending_next_roadmap_selection`

Next allowed move: select the next high-value governed roadmap or open a fresh GC-018/source-verified work order before implementation. LHW24 remains the latest closed numbered LHW wave.

No validation semantics change, no runtime/provider/live proof, no public-sync, no generated aggregate mutation beyond session sync, no resolver mutation, no adapter mutation, and no push without separate authorization.

## Parked Checkpoint

Roadmap status reconciliation sweep T0-T4 is closed bounded at material commit `3ccf574c`. P3, P4C, and DSCP-T11F stale status surfaces were reconciled; compound/held roadmaps remain deferred. Next roadmap selection remains pending user direction.

## Continuity Markers

| Field | Value |
|---|---|
| Freeze posture | `governance_kernel_freeze_recommended` |
| Pain-point closure direction | `docs/reviews/archive/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md` |
| Latest closed LHW wave | `LHW24` |

## Maintainability Note

This front door is intentionally compact. Long continuity history was archived to:

`CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-06-26.md`

Do not append long status history here. Update compact pointers, generated session state sources, and the active handoff instead.

## Claim Boundary

This file is a startup pointer surface only. Complete canonical state lives in `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
