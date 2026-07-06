# AGENT_HANDOFF_V38_2026-07-06

Memory class: active-agent-handoff
Status: ACTIVE
Purpose: compact current-session continuity for resumed agents after MSEA-R49 closure and R50 seal routing.
Scope/target/owner boundary: private provenance continuity only; Codex session-sync steward owns this handoff update; no runtime source, tests, public-sync, provider-local config, private/generated MinerU output, or use-case/legal workflow change is authorized here.
Supersedes: `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V37_2026-07-06.md`
Opened because: V37 reached 1158 lines and was rotated under governed file maintainability planning during R48 session-sync.

## Purpose

Keep resumed agents aligned on R49 closure, active handoff V38, and the next bounded R50 seal/recheck move.

## Scope

This handoff covers private provenance continuity after R49 only. It does not authorize runtime source, tests, public-sync, provider-local config, private/generated MinerU output, direct absorption, or use-case/legal workflow changes.

## Startup Acknowledgment

Startup acknowledged: current mode=`msea_r49_plane_absorb_target_selection_closed_pass_bounded_ready_for_r50_system_chain_seal`; active handoff=AGENT_HANDOFF_V38_2026-07-06.md; next allowed move=author a fresh source-verified MSEA-R50 MinerU Adapter Contract Owner Surface System Chain Seal packet, or stop/checkpoint; parked checkpoint=legal/use-case workflow remains parked unless explicitly selected; no external source absorption, source/test edit, runtime/provider/MCP proof, production Memory/RAG release, public-sync, private/generated MinerU output read, retrieval, vectorization, use-case/legal workflow, extraction accuracy claim, document truth claim, legal quality claim, current-law correctness claim, hosted release claim, standalone app work, provider-local config edit, push, or public claim is authorized.

## Mandatory Startup Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
3. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
4. `AGENT_HANDOFF_V38_2026-07-06.md`
5. `docs/reference/guard_orientation/README.md`
6. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
7. `DESIGN.md` only if touching Web/UI/dashboard work.

## Current Mode

`msea_r49_plane_absorb_target_selection_closed_pass_bounded_ready_for_r50_system_chain_seal`

## Active Boundary

This handoff is active for startup routing. Historical continuity from V37 is archived at `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V37_2026-07-06.md`. R49 permits only a future R50 source-verified seal/recheck packet or a stop/checkpoint.

## Latest Material Closure

| Work | Commit | Disposition |
| --- | --- | --- |
| MSEA-R49 Plane Absorb Target Selection And Owner Surface Map | `85bd012a3` | CLOSED_PASS_BOUNDED; selected `R49_SELECT_EXISTING_R10_ADAPTER_CONTRACT_OWNER_SURFACE_FOR_SYSTEM_CHAIN_SEAL`; owner surface is `docs/reference/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md`; recommends fresh source-verified MSEA-R50 MinerU Adapter Contract Owner Surface System Chain Seal packet. |
| MSEA-R48 MinerU To Plane Absorb Transition Readiness Packet | `34151de7c` | CLOSED_PASS_BOUNDED; selected `R48_PLANE_ABSORB_TRANSITION_READY_FOR_TARGET_SELECTION_ONLY`; recommends fresh source-verified MSEA-R49 Plane Absorb Target Selection And Owner Surface Map packet. |
| MSEA-R47 MinerU System Chain Finalization And Plane Absorb Transition Readiness | `92f7b92ab` | CLOSED_PASS_BOUNDED; MinerU/scanlayer/memory chain complete as bounded internal foundation system chain, not production/public/use-case release. |
| Latest prior session-sync before R48 | `b6a69ed03` | Session state/handoff current for R47 before R48 material work. |

## Latest Work/Changes

R49 material closure added `docs/reviews/CVF_MSEA_R49_PLANE_ABSORB_TARGET_SELECTION_AND_OWNER_SURFACE_MAP_2026-07-06.md` at commit `85bd012a3`. This session-sync updates active pointers, state source fragments, generated active state/bootstrap, front door, and handoff routing for the R50 seal/recheck next move.

## HEAD Freshness

Latest session-sync parent commit: pending after R49 session-sync.

## R49 Boundary

R49 is a docs-only source-verified target-selection and owner-surface mapping decision. It selects the existing R10 adapter-contract reference as the owner surface for system-chain seal and allows only a future R50 seal/recheck packet. It does not authorize direct absorption, source/test edit, runtime/provider/MCP proof, production Memory/RAG release, public-sync, private/generated MinerU output read, retrieval, vectorization, use-case/legal workflow, hosted release, provider-local config edit, push, or public claim.

Latest closed numbered LHW wave: LHW24.

## Verification Snapshot

| Gate | Result |
| --- | --- |
| Focused structural/external/corpus/rescan/delta/AOT gates on R49 | PASS |
| Pre-implementation autorun on `dce655773..HEAD` | PASS 75/75 |
| Reviewer-return commit steward on `dce655773..HEAD` | PASS |
| Material pre-commit hook | PASS 80/80 |

## Next Allowed Move

Author a fresh source-verified `MSEA-R50 MinerU Adapter Contract Owner Surface System Chain Seal` packet, or stop/checkpoint. The R50 packet should verify the join from the selected R10 owner surface through the completed MinerU/scanlayer/memory chain and decide whether to stop the MinerU foundation lane as complete. Do not jump into use-case/legal workflow.

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

Authorized guard-maintenance scope: session-sync only after MSEA-R49 material closure commit `85bd012a3`, including active mode, next allowed move, generated active state, bootstrap read model, active handoff, and R49 closure state entry.

Operator authorization: implicit in the current operator request to continue until the system chain is complete and complete the governed session-sync after material closure.

Protected paths: `AGENT_HANDOFF_V38_2026-07-06.md`, `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`, `CVF_SESSION/ACTIVE_SESSION_STATE.json`, `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`, `CVF_SESSION/state/entries/mseaR49PlaneAbsorbTargetSelectionOwnerSurfaceMap20260706.json`, `CVF_SESSION/state/entries/nextAllowedMove.json`, and `CVF_SESSION_MEMORY.md`. The purpose is solely to reflect R49 closure and R50 seal routing. It may not change runtime source, tests, public-sync artifacts, provider-local config, private/generated MinerU output, or use-case/legal workflow material.

Rollback boundary: revert only this MSEA-R49 session-sync if rejected; do not revert material closure commit `85bd012a3` or older MSEA history.
