# ACTIVE SESSION FRONT DOOR

Memory class: active-session-front-door
Status: ACTIVE
Last compacted: 2026-07-04

## Startup Order

Read these files before governed material work:

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
3. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
4. `AGENT_HANDOFF_V36_2026-07-04.md`
5. `docs/reference/guard_orientation/README.md`

For governed artifact authoring, also read:

`docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`

## Active Pointers

| Field | Path |
|---|---|
| Bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Canonical state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| Active handoff | `AGENT_HANDOFF_V36_2026-07-04.md` |
| Active review queue | `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` |
| Historical handoffs | `CVF_SESSION/handoffs/archive/` |
| Front-door archive snapshot | `CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-06-26.md` |
| Pain-point closure direction archive | `docs/reviews/archive/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md` |
| Freeze posture marker | `governance_kernel_freeze_recommended` |

## Startup Acknowledgment

Startup acknowledged: current mode=`msea_r28_t15_mineru_candidate_review_and_store_write_authority_decision_dispatched_pending_worker_return`; active handoff=AGENT_HANDOFF_V36_2026-07-04.md; next allowed move=no-commit T15 worker execution using the T15 work order and GC-018 baseline; parked checkpoint=actual memory/RAG write, MinerU runtime, private/generated content read, Candidate Group A import, checker/hook/source/test/session edits, provider/live proof, public-sync, standalone PDF app, legal/use-case deep-dive, worker commit/push, and production workflow lanes remain deferred unless a later accepted packet and gates explicitly release them; LHW24 remains the latest closed numbered LHW wave.

## Current Mode

Current mode marker: `msea_r28_t15_mineru_candidate_review_and_store_write_authority_decision_dispatched_pending_worker_return`

Current mode: `msea_r28_t15_mineru_candidate_review_and_store_write_authority_decision_dispatched_pending_worker_return`

`msea_r28_t15_mineru_candidate_review_and_store_write_authority_decision_dispatched_pending_worker_return`

Previous mode:

`msea_r28_t14_mineru_memory_record_candidate_builder_closed_pending_t15_candidate_review_and_store_write_authority_work_order_authoring`

## Current Work

| Work | Commit | Disposition |
|---|---|---|
| MSEA-R28-T15 MinerU Candidate Review And Store Write Authority Decision dispatch | `e3ef73e4` | DISPATCH_READY; created GC-018 baseline and source-verified no-commit docs-only decision work order; pre-dispatch autorun PASS 73/73, dispatch steward PASS, material pre-commit hook PASS 80/80; actual memory/RAG write remains unauthorized. |
| MSEA-R28-T14 MinerU Memory Record Candidate Builder | `1b367302` | CLOSED_PASS_BOUNDED; accepted deterministic metadata-only memory-record candidate builder, focused tests, and worker return; focused pytest PASS 48/48, worker-return fast gate PASS, pre-implementation autorun PASS 75/75, reviewer steward PASS, material pre-commit hook PASS 80/80; actual memory/RAG write remains unauthorized. |
| MSEA-R28-T13 MinerU Memory Write Authority Decision | `0002de2d` | CLOSED_PASS_BOUNDED; accepted docs-only authority decision matrix and worker return; selected `MEMORY_RECORD_CANDIDATE_BUILDER_READY`; T14 worker execution is now released by T14 dispatch; actual memory/RAG write remains unauthorized and T16 remains held. |

## Current Held Follow-Up Work

| Work | Commit | Disposition |
|---|---|---|
| Memory-route release | `e3ef73e4` | T15_DISPATCH_READY; memory/RAG write remains unauthorized; T16 actual write remains held pending accepted T15 source-backed decision. |
| Runtime/provider/public/checker/adapter/memory/RAG implementation lanes | `45bae1d4` | DEFERRED unless a fresh packet explicitly releases them. |
| Standalone PDF app and legal/use-case deep dive | `45bae1d4` | HELD; current MinerU work remains CVF foundation-plane work. |

## Current Closed Work

| Work | Commit | Disposition |
|---|---|---|
| MSEA-R28-T14 MinerU Memory Record Candidate Builder | `1b367302` | CLOSED_PASS_BOUNDED; selected `MEMORY_RECORD_CANDIDATE_READY_FOR_REVIEW`; memory/RAG write remains `MEMORY_WRITE_NOT_AUTHORIZED_BY_T14_CANDIDATE_ONLY`; future authority required is `FUTURE_MEMORY_STORE_WRITE_AUTHORITY_REQUIRED`; focused pytest PASS 48/48, worker-return fast gate PASS, pre-implementation autorun PASS 75/75, reviewer-return steward PASS, material pre-commit hook PASS 80/80. |
| MSEA-R28-T13 MinerU Memory Write Authority Decision | `0002de2d` | CLOSED_PASS_BOUNDED; selected `MEMORY_RECORD_CANDIDATE_BUILDER_READY`; memory/RAG write remains `MEMORY_WRITE_STILL_NOT_AUTHORIZED_BY_T13`; future authority required is `FUTURE_MEMORY_RECORD_CANDIDATE_WORK_ORDER_REQUIRED`; worker-return fast gate PASS, pre-implementation autorun PASS 75/75, reviewer-return steward PASS, material pre-commit hook PASS 80/80. |
| MSEA-R28-T12 MinerU Memory Owner Admission Readout Implementation | `91cc1422` | CLOSED_PASS_BOUNDED; accepted deterministic metadata-only memory-owner admission readout helper and focused tests; memory/RAG write remains `MEMORY_WRITE_NOT_AUTHORIZED_BY_T12_DISPATCH`; focused pytest PASS 41/41, worker-return fast gate PASS, pre-implementation autorun PASS 75/75, reviewer-return steward PASS, material pre-commit hook PASS 80/80. |
| Older MSEA-R28, R27, R26, KIOD, WOAS, FPC, MFE, and ASSF history | see state registry and governed artifacts | Summarized out of this front door after compaction; canonical detail remains in `CVF_SESSION/ACTIVE_SESSION_STATE.json`, source entries under `CVF_SESSION/state/entries/`, governed artifacts, and archived handoffs. |

## Latest Closed Work

Detailed historical closure rows are intentionally summarized out of this front
door to keep it below the governed file-size threshold. Use
`CVF_SESSION/ACTIVE_SESSION_STATE.json`, source entries under
`CVF_SESSION/state/entries/`, governed artifacts, and archived handoffs for
canonical older closure detail.

## Next Allowed Move

Mode: `msea_r28_t15_mineru_candidate_review_and_store_write_authority_decision_dispatched_pending_worker_return`

Next allowed move: no-commit T15 worker execution using the T15 work order and
GC-018 baseline.

LHW24 remains the latest closed numbered LHW wave.

Committed T15 dispatch artifacts:

- `docs/baselines/CVF_GC018_MSEA_R28_T15_MINERU_CANDIDATE_REVIEW_AND_STORE_WRITE_AUTHORITY_DECISION_2026-07-04.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T15_MINERU_CANDIDATE_REVIEW_AND_STORE_WRITE_AUTHORITY_DECISION_2026-07-04.md`

MSEA-R28-T15 is dispatched at material commit `e3ef73e4`. Worker may create
only the T15 decision matrix and T15 worker return, then return without staging,
committing, pushing, or session-sync. Actual memory/RAG write remains
unauthorized and T16 remains held pending accepted T15 source-backed decision.
Do not write memory/RAG, run MinerU, read private/generated content, import
Candidate Group A, edit checker/hook/session/source/test files, run
provider/live proof, public-sync, build standalone app surfaces, perform
legal/use-case deep dive, claim extraction accuracy, document truth, legal
quality, current-law correctness, workflow-chain production readiness, stage
worker changes, commit worker changes, or push unless a later accepted packet
explicitly releases that scope.

## Core Guard Self-Protection Authorization - MSEA-R28-T15 Dispatch Session Sync

Authorized guard-maintenance scope: session-sync only after MSEA-R28-T15
material dispatch commit `e3ef73e4`, including active mode, next allowed move,
generated active state, bootstrap read model, front-door continuity, active
handoff, and dispatch state entry.

Protected paths:

| Path | Purpose |
|---|---|
| `CVF_SESSION_MEMORY.md` | Update current mode, current dispatched work, startup acknowledgment, and next allowed move after T15 dispatch. |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | Regenerate compact startup facts after active state update. |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Regenerate aggregate from state sources after T15 dispatch session-sync. |
| `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json` | Update `currentMode` and `previousMode` for T15 dispatched pending worker return. |
| `CVF_SESSION/state/entries/mseaR28T15MineruCandidateReviewAndStoreWriteAuthorityDecisionDispatch20260704.json` | Record T15 dispatch evidence. |
| `CVF_SESSION/state/entries/nextAllowedMove.json` | Route next move to T15 no-commit worker execution. |
| `AGENT_HANDOFF_V36_2026-07-04.md` | Record T15 dispatch continuity and worker next move. |

Rollback boundary: revert only this MSEA-R28-T15 dispatch session-sync if
rejected; do not revert material dispatch commit `e3ef73e4` or older MSEA
history.

LHW24 remains the latest closed numbered LHW wave.

## Historical Detail Routing

This front door is intentionally compact. Historical continuity before the
latest R28 sequence is available through:

- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/entries/`
- `AGENT_HANDOFF_V36_2026-07-04.md`
- `CVF_SESSION/handoffs/archive/`
- governed baselines, work orders, reviews, matrices, and closure packets under
  `docs/`
