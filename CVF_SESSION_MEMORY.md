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

Startup acknowledged: current mode=`assf_external_agent_readout_adapter_boundary_closed_pass_bounded_pending_readout_implementation_gc018`; active handoff=AGENT_HANDOFF_V23_2026-06-26.md; next allowed move=open a fresh GC-018/source-verified work order for read-only external-agent metadata readout implementation; parked checkpoint=no adapter behavior implementation, package instance, certification decision, lifecycle mutation, ASSF registry/generated-index source mutation, resolver mutation, provider/live proof, public-sync, push, activation, package execution, or package integration without future accepted work order authorization.

## Current Mode

Current mode marker: `assf_external_agent_readout_adapter_boundary_closed_pass_bounded_pending_readout_implementation_gc018`

Current mode: `assf_external_agent_readout_adapter_boundary_closed_pass_bounded_pending_readout_implementation_gc018`

`assf_external_agent_readout_adapter_boundary_closed_pass_bounded_pending_readout_implementation_gc018`

Previous mode:

`assf_web_projection_implementation_closed_pass_bounded_pending_external_agent_readout_adapter_roadmap`

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

## Next Allowed Move

Mode: `assf_external_agent_readout_adapter_boundary_closed_pass_bounded_pending_readout_implementation_gc018`

Next allowed move: open a fresh GC-018/source-verified work order for read-only external-agent metadata readout implementation, using `docs/reference/agent_system_skills/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_CONTRACT.md` as the boundary source. LHW24 remains the latest closed numbered LHW wave.

No adapter behavior implementation, package instance creation, certification decision, lifecycle mutation, ASSF registry-source mutation, ASSF generated-index source mutation, resolver mutation, provider/live proof, public-sync, push, activation, package instruction execution, or package integration is authorized until that future work order is accepted and closed.

## Parked Checkpoint

ASSF external-agent readout / CLI-MCP adapter boundary is closed bounded. Adapter behavior, provider/live proof, package execution, public-sync, and push remain parked until separately authorized.

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
