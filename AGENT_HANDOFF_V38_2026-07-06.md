# AGENT_HANDOFF_V38_2026-07-06

Memory class: active-agent-handoff
Status: ACTIVE
Purpose: compact current-session continuity for resumed agents after MSEA-R48 closure and V37 handoff rotation.
Scope/target/owner boundary: private provenance continuity only; Codex session-sync steward owns this handoff update; no runtime source, tests, public-sync, provider-local config, private/generated MinerU output, or use-case/legal workflow change is authorized here.
Supersedes: `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V37_2026-07-06.md`
Opened because: V37 reached 1158 lines and was rotated under governed file maintainability planning during R48 session-sync.

## Purpose

Keep resumed agents aligned on R48 closure, active handoff V38, and the next bounded R49 target-selection move.

## Scope

This handoff covers private provenance continuity after R48 only. It does not authorize runtime source, tests, public-sync, provider-local config, private/generated MinerU output, direct absorption, or use-case/legal workflow changes.

## Startup Acknowledgment

Startup acknowledged: current mode=`msea_r48_mineru_to_plane_absorb_transition_readiness_closed_pass_bounded_ready_for_r49_target_selection`; active handoff=AGENT_HANDOFF_V38_2026-07-06.md; next allowed move=author a fresh source-verified MSEA-R49 Plane Absorb Target Selection And Owner Surface Map packet, or stop/checkpoint; parked checkpoint=legal/use-case workflow remains parked unless explicitly selected; no external source absorption, source/test edit, runtime/provider/MCP proof, production Memory/RAG release, public-sync, private/generated MinerU output read, retrieval, vectorization, use-case/legal workflow, extraction accuracy claim, document truth claim, legal quality claim, current-law correctness claim, hosted release claim, standalone app work, provider-local config edit, push, or public claim is authorized.

## Mandatory Startup Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
3. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
4. `AGENT_HANDOFF_V38_2026-07-06.md`
5. `docs/reference/guard_orientation/README.md`
6. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
7. `DESIGN.md` only if touching Web/UI/dashboard work.

## Current Mode

`msea_r48_mineru_to_plane_absorb_transition_readiness_closed_pass_bounded_ready_for_r49_target_selection`

## Active Boundary

This handoff is active for startup routing. Historical continuity from V37 is archived at `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V37_2026-07-06.md`. R48 permits only a future target-selection and owner-surface mapping packet or a stop/checkpoint.

## Latest Material Closure

| Work | Commit | Disposition |
| --- | --- | --- |
| MSEA-R48 MinerU To Plane Absorb Transition Readiness Packet | `34151de7c` | CLOSED_PASS_BOUNDED; selected `R48_PLANE_ABSORB_TRANSITION_READY_FOR_TARGET_SELECTION_ONLY`; recommends fresh source-verified MSEA-R49 Plane Absorb Target Selection And Owner Surface Map packet. |
| MSEA-R47 MinerU System Chain Finalization And Plane Absorb Transition Readiness | `92f7b92ab` | CLOSED_PASS_BOUNDED; MinerU/scanlayer/memory chain complete as bounded internal foundation system chain, not production/public/use-case release. |
| Latest prior session-sync before R48 | `b6a69ed03` | Session state/handoff current for R47 before R48 material work. |

## Latest Work/Changes

R48 material closure added `docs/reviews/CVF_MSEA_R48_MINERU_TO_PLANE_ABSORB_TRANSITION_READINESS_PACKET_2026-07-06.md` at commit `34151de7c`. This session-sync updates active pointers, state source fragments, generated active state/bootstrap, front door, and handoff routing from V37 to V38.

## HEAD Freshness

Latest session-sync parent commit: `820b9fc3`.

## R48 Boundary

R48 is a docs-only source-verified transition-readiness decision. It allows only target selection and owner-surface mapping as a future packet. It does not authorize direct absorption, source/test edit, runtime/provider/MCP proof, production Memory/RAG release, public-sync, private/generated MinerU output read, retrieval, vectorization, use-case/legal workflow, hosted release, provider-local config edit, push, or public claim.

Latest closed numbered LHW wave: LHW24.

## Verification Snapshot

| Gate | Result |
| --- | --- |
| Rescan intelligence hardening on R48 | PASS |
| Markdown structural completeness on R48 | PASS |
| Pre-implementation autorun on `b6a69ed03..HEAD` | PASS 75/75 |
| Reviewer-return commit steward on `b6a69ed03..HEAD` | PASS |
| Material pre-commit hook | PASS 80/80 |

## Next Allowed Move

Author a fresh source-verified `MSEA-R49 Plane Absorb Target Selection And Owner Surface Map` packet, or stop/checkpoint. The R49 packet should select a target plane/source surface, map owner boundaries, and state what remains forbidden before any absorption or runtime proof. Do not jump into use-case/legal workflow.

## Agent Operation Trace

| Field | Value |
| --- | --- |
| Commit owner for R48 material | Codex reviewer/closer |
| Commit owner for this session-sync | Codex session-sync steward |
| Handoff rotation | V37 archived, V38 opened |
| Session source update requirement | Edit source fragments under `CVF_SESSION/state/`, run `governance/compat/generate_active_session_state.py` |
| Public-sync | Not authorized |
| Worker commit | Not applicable |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: session-sync only after MSEA-R48 material closure commit `34151de7c`, including active mode, next allowed move, generated active state, bootstrap read model, V37 archive rotation, V38 active handoff creation, and R48 closure state entry.

Operator authorization: implicit in the current operator request to continue the fresh source-verified plane/absorb transition readiness packet and complete the governed session-sync after material closure.

Protected paths: `AGENTS.md`, `AGENT_HANDOFF_V38_2026-07-06.md`, `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`, `CVF_SESSION/ACTIVE_SESSION_STATE.json`, `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V37_2026-07-06.md`, `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`, `CVF_SESSION/state/entries/mseaR48MineruToPlaneAbsorbTransitionReadinessPacket20260706.json`, `CVF_SESSION/state/entries/nextAllowedMove.json`, and `CVF_SESSION_MEMORY.md`. The purpose is solely to reflect R48 closure and handoff rotation. It may not change runtime source, tests, public-sync artifacts, provider-local config, private/generated MinerU output, or use-case/legal workflow material.

Rollback boundary: revert only this MSEA-R48 session-sync and handoff rotation if rejected; do not revert material closure commit `34151de7c` or older MSEA history.
