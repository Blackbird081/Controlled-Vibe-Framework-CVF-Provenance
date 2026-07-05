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

Startup acknowledged: current mode=`msea_r28_t19_mineru_durable_store_invocation_release_decision_dispatched_pending_worker_return`; active handoff=AGENT_HANDOFF_V36_2026-07-04.md; next allowed move=execute MSEA-R28-T19 WORKER_MUST_NOT_COMMIT docs-only durable-store invocation release-decision worker packet; parked checkpoint=actual memory/RAG write, durable-store invocation, Learning Plane source edits, checker/hook/session/handoff edits by worker, MinerU runtime, private/generated content read, Candidate Group A import, provider/live proof, public-sync, standalone PDF app, legal/use-case deep-dive, worker commit/push, and production workflow lanes remain deferred; LHW24 remains the latest closed numbered LHW wave.

## Current Mode

Current mode marker: `msea_r28_t19_mineru_durable_store_invocation_release_decision_dispatched_pending_worker_return`

Current mode: `msea_r28_t19_mineru_durable_store_invocation_release_decision_dispatched_pending_worker_return`

`msea_r28_t19_mineru_durable_store_invocation_release_decision_dispatched_pending_worker_return`

Previous mode:

`msea_r28_t18_mineru_actual_durable_memory_write_adapter_implementation_closed_pending_t19_durable_store_invocation_release_decision_work_order_authoring`

## Current Work

| Work | Commit | Disposition |
|---|---|---|
| MSEA-R28-T19 MinerU Durable Store Invocation Release Decision dispatch | `8db612b0` | DISPATCH_READY; authored fresh GC-018 baseline and source-verified WORKER_MUST_NOT_COMMIT docs-only release-decision work order; pre-dispatch autorun PASS 73/73, dispatch steward PASS, material pre-commit hook PASS 80/80; actual memory/RAG write and durable-store invocation remain unauthorized. |
| MSEA-R28-T18 MinerU Actual Durable Memory Write Adapter Implementation | `51966467` | CLOSED_PASS_BOUNDED; accepted deterministic metadata-only durable-memory write adapter candidate implementation, focused tests, and worker return; focused pytest PASS 71/71, worker-return fast gate PASS, pre-implementation autorun PASS 75/75, reviewer steward PASS, material pre-commit hook PASS 80/80; actual memory/RAG write and durable-store invocation remain unauthorized pending fresh T19 release-decision authoring. |
| MSEA-R28-T17 MinerU Durable Memory Write Authority Decision | `5166a624` | CLOSED_PASS_BOUNDED; accepted docs-only decision matrix and worker return; selected `T18_ACTUAL_DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_CANDIDATE`; worker-return fast gate PASS, pre-implementation autorun PASS 75/75, reviewer steward PASS, material pre-commit hook PASS 80/80; actual memory/RAG write and durable-store invocation remain unauthorized pending T18 authoring and acceptance. |
| MSEA-R28-T17 MinerU Durable Memory Write Authority Decision dispatch | `b62e1be3` | DISPATCH_READY; created GC-018 baseline and source-verified no-commit docs-only authority decision work order; pre-dispatch autorun PASS 73/73, dispatch steward PASS, material pre-commit hook PASS 80/80; actual memory/RAG write and durable-store invocation remain unauthorized. |
| MSEA-R28-T16 MinerU Memory Store Adapter Mapping Implementation | `0bf81a68` | CLOSED_PASS_BOUNDED; accepted deterministic summary-only durable-memory write-input candidate mapping helper, focused tests, and worker return; focused pytest PASS 55/55, worker-return fast gate PASS, pre-implementation autorun PASS 75/75, reviewer steward PASS, material pre-commit hook PASS 80/80; actual memory/RAG write and durable-store invocation remain unauthorized pending T17 authority decision. |
| MSEA-R28-T15 MinerU Candidate Review And Store Write Authority Decision | `50afaa0f` | CLOSED_PASS_BOUNDED; accepted docs-only decision matrix and worker return; selected `MEMORY_STORE_WRITE_WORK_ORDER_AUTHORING_READY`; worker-return fast gate PASS, pre-implementation autorun PASS 75/75, reviewer steward PASS, material pre-commit hook PASS 80/80; actual memory/RAG write remains unauthorized until a later accepted T16 packet and closure. |
| MSEA-R28-T15 MinerU Candidate Review And Store Write Authority Decision dispatch | `e3ef73e4` | DISPATCH_READY; created GC-018 baseline and source-verified no-commit docs-only decision work order; pre-dispatch autorun PASS 73/73, dispatch steward PASS, material pre-commit hook PASS 80/80; actual memory/RAG write remains unauthorized. |
| MSEA-R28-T14 MinerU Memory Record Candidate Builder | `1b367302` | CLOSED_PASS_BOUNDED; accepted deterministic metadata-only memory-record candidate builder, focused tests, and worker return; focused pytest PASS 48/48, worker-return fast gate PASS, pre-implementation autorun PASS 75/75, reviewer steward PASS, material pre-commit hook PASS 80/80; actual memory/RAG write remains unauthorized. |
| MSEA-R28-T13 MinerU Memory Write Authority Decision | `0002de2d` | CLOSED_PASS_BOUNDED; accepted docs-only authority decision matrix and worker return; selected `MEMORY_RECORD_CANDIDATE_BUILDER_READY`; T14 worker execution is now released by T14 dispatch; actual memory/RAG write remains unauthorized and T16 remains held. |

## Current Held Follow-Up Work

| Work | Commit | Disposition |
|---|---|---|
| Memory-route release | `8db612b0` | T19_DISPATCH_DECISION_ONLY; actual memory/RAG write and durable-store invocation remain unauthorized pending T19 no-commit worker execution, review, and acceptance. |
| Runtime/provider/public/checker/adapter/memory/RAG implementation lanes | `45bae1d4` | DEFERRED unless a fresh packet explicitly releases them. |
| Standalone PDF app and legal/use-case deep dive | `45bae1d4` | HELD; current MinerU work remains CVF foundation-plane work. |

## Current Closed Work

| Work | Commit | Disposition |
|---|---|---|
| MSEA-R28-T18 MinerU Actual Durable Memory Write Adapter Implementation | `51966467` | CLOSED_PASS_BOUNDED; selected `DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_CANDIDATE_READY`; memory/RAG write remains `MEMORY_WRITE_NOT_AUTHORIZED_BY_T18_ADAPTER_ONLY`; durable-store invocation remains `DURABLE_STORE_INVOCATION_NOT_AUTHORIZED_BY_T18`; private/generated output remains `PRIVATE_OUTPUT_NOT_READ_OR_RELEASED`; focused pytest PASS 71/71, worker-return fast gate PASS, pre-implementation autorun PASS 75/75, reviewer-return steward PASS, material pre-commit hook PASS 80/80. |
| MSEA-R28-T17 MinerU Durable Memory Write Authority Decision | `5166a624` | CLOSED_PASS_BOUNDED; selected `T18_ACTUAL_DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_CANDIDATE`; memory/RAG write remains `MEMORY_WRITE_NOT_AUTHORIZED_BY_T17_DECISION_ONLY`; private/generated output remains `PRIVATE_OUTPUT_NOT_READ_OR_RELEASED`; worker-return fast gate PASS after reviewer path normalization, pre-implementation autorun PASS 75/75, reviewer-return steward PASS, material pre-commit hook PASS 80/80. |
| MSEA-R28-T16 MinerU Memory Store Adapter Mapping Implementation | `0bf81a68` | CLOSED_PASS_BOUNDED; selected `MEMORY_STORE_ADAPTER_MAPPING_IMPLEMENTED`; memory/RAG write remains `MEMORY_WRITE_NOT_AUTHORIZED_BY_T16_MAPPING_ONLY`; durable-store invocation remains held pending T17 authority decision; focused pytest PASS 55/55, worker-return fast gate PASS, pre-implementation autorun PASS 75/75, reviewer-return steward PASS, material pre-commit hook PASS 80/80. |
| MSEA-R28-T15 MinerU Candidate Review And Store Write Authority Decision | `50afaa0f` | CLOSED_PASS_BOUNDED; selected `MEMORY_STORE_WRITE_WORK_ORDER_AUTHORING_READY`; memory/RAG write remains `MEMORY_WRITE_NOT_AUTHORIZED_BY_T15_DECISION_ONLY`; adapter mapping required before any write; worker-return fast gate PASS, pre-implementation autorun PASS 75/75, reviewer-return steward PASS, material pre-commit hook PASS 80/80. |
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

Mode: `msea_r28_t19_mineru_durable_store_invocation_release_decision_dispatched_pending_worker_return`

Next allowed move: execute the MSEA-R28-T19 WORKER_MUST_NOT_COMMIT docs-only
durable-store invocation release-decision worker packet.

LHW24 remains the latest closed numbered LHW wave.

Accepted T19 dispatch artifacts:

- `docs/baselines/CVF_GC018_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_2026-07-05.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_2026-07-05.md`

Required T19 worker output artifacts:

- `docs/reference/CVF_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_MATRIX_2026-07-05.md`
- `docs/reviews/CVF_MSEA_R28_T19_MINERU_DURABLE_STORE_INVOCATION_RELEASE_DECISION_WORKER_RETURN_2026-07-05.md`

Accepted T18 closure artifacts:

- `docs/baselines/CVF_GC018_MSEA_R28_T18_MINERU_ACTUAL_DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_2026-07-04.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R28_T18_MINERU_ACTUAL_DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_2026-07-04.md`
- `docs/reviews/CVF_MSEA_R28_T18_MINERU_ACTUAL_DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md`
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py`
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py`

MSEA-R28-T19 dispatch is at material commit `8db612b0`. It authorizes only a
no-commit docs-only worker decision matrix and worker return. The worker must
use accepted T18 source/test evidence, the T17 authority decision matrix, the
T16 write-input candidate mapping, R27 route matrix, R24-T4 private-output
policy, and durable-memory-store/runtime-hierarchy source evidence. Actual
memory/RAG write, durable-store invocation, vectorization, retrieval, MinerU
runtime, private/generated content read, Candidate Group A import,
provider/live proof, public-sync, standalone app surfaces, legal/use-case deep
dive, extraction accuracy, document truth, legal quality, current-law
correctness, workflow-chain production readiness, Learning Plane source edits,
checker/hook/session/handoff edits by worker, worker commit, and push remain
held until T19 is executed, reviewed, and accepted.

## Core Guard Self-Protection Authorization - MSEA-R28-T19 Dispatch Session Sync

Authorized guard-maintenance scope: session-sync only after MSEA-R28-T19
material dispatch commit `8db612b0`, including active mode, next allowed move,
generated active state, bootstrap read model, front-door continuity, active
handoff, and dispatch state entry.

Protected paths:

| Path | Purpose |
|---|---|
| `CVF_SESSION_MEMORY.md` | Update current mode, current dispatched work, startup acknowledgment, and next allowed move after T19 dispatch. |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | Regenerate compact startup facts after active state update. |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Regenerate aggregate from state sources after T19 dispatch session-sync. |
| `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json` | Update `currentMode` and `previousMode` for T19 dispatched pending worker return. |
| `CVF_SESSION/state/entries/mseaR28T19MineruDurableStoreInvocationReleaseDecisionDispatch20260705.json` | Record T19 dispatch evidence. |
| `CVF_SESSION/state/entries/nextAllowedMove.json` | Route next move to T19 no-commit docs-only worker execution. |
| `AGENT_HANDOFF_V36_2026-07-04.md` | Record T19 dispatch continuity and next move. |

Rollback boundary: revert only this MSEA-R28-T19 dispatch session-sync if
rejected; do not revert material dispatch commit `8db612b0`, T18 material
closure commit `51966467`, or older MSEA history.

## Core Guard Self-Protection Authorization - MSEA-R28-T18 Closure Session Sync

Authorized guard-maintenance scope: session-sync only after MSEA-R28-T18
material closure commit `51966467`, including active mode, next allowed move,
generated active state, bootstrap read model, front-door continuity, active
handoff, and closure state entry.

Protected paths:

| Path | Purpose |
|---|---|
| `CVF_SESSION_MEMORY.md` | Update current mode, current/closed work, startup acknowledgment, and next allowed move after T18 closure. |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | Regenerate compact startup facts after active state update. |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Regenerate aggregate from state sources after T18 closure session-sync. |
| `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json` | Update `currentMode` and `previousMode` for T18 closed pending T19 work-order authoring. |
| `CVF_SESSION/state/entries/mseaR28T18MineruActualDurableMemoryWriteAdapterImplementationClosure20260704.json` | Record accepted T18 closure evidence. |
| `CVF_SESSION/state/entries/nextAllowedMove.json` | Route next move to T19 GC-018/source-verified durable-store invocation release-decision work-order authoring only. |
| `AGENT_HANDOFF_V36_2026-07-04.md` | Record T18 closure continuity and T19 next move. |

Rollback boundary: revert only this MSEA-R28-T18 closure session-sync if
rejected; do not revert material closure commit `51966467` or older MSEA
history.

## Core Guard Self-Protection Authorization - MSEA-R28-T18 Dispatch Session Sync

Authorized guard-maintenance scope: session-sync only after MSEA-R28-T18
material dispatch commit `02d174be`, including active mode, next allowed move,
generated active state, bootstrap read model, front-door continuity, active
handoff, and dispatch state entry.

Protected paths:

| Path | Purpose |
|---|---|
| `CVF_SESSION_MEMORY.md` | Update current mode, current dispatched work, startup acknowledgment, and next allowed move after T18 dispatch. |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | Regenerate compact startup facts after active state update. |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Regenerate aggregate from state sources after T18 dispatch session-sync. |
| `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json` | Update `currentMode` and `previousMode` for T18 dispatched pending worker return. |
| `CVF_SESSION/state/entries/mseaR28T18MineruActualDurableMemoryWriteAdapterImplementationDispatch20260704.json` | Record T18 dispatch evidence. |
| `CVF_SESSION/state/entries/nextAllowedMove.json` | Route next move to T18 no-commit source/test worker execution. |
| `AGENT_HANDOFF_V36_2026-07-04.md` | Record T18 dispatch continuity and worker next move. |

Rollback boundary: revert only this MSEA-R28-T18 dispatch session-sync if
rejected; do not revert material dispatch commit `02d174be` or older MSEA
history.

## Core Guard Self-Protection Authorization - MSEA-R28-T17 Closure Session Sync

Authorized guard-maintenance scope: session-sync only after MSEA-R28-T17
material closure commit `5166a624`, including active mode, next allowed move,
generated active state, bootstrap read model, front-door continuity, active
handoff, and closure state entry.

Protected paths:

| Path | Purpose |
|---|---|
| `CVF_SESSION_MEMORY.md` | Update current mode, current/closed work, startup acknowledgment, and next allowed move after T17 closure. |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | Regenerate compact startup facts after active state update. |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Regenerate aggregate from state sources after T17 closure session-sync. |
| `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json` | Update `currentMode` and `previousMode` for T17 closed pending T18 work-order authoring. |
| `CVF_SESSION/state/entries/mseaR28T17MineruDurableMemoryWriteAuthorityDecisionClosure20260704.json` | Record accepted T17 closure evidence. |
| `CVF_SESSION/state/entries/nextAllowedMove.json` | Route next move to T18 GC-018/source-verified work-order authoring only. |
| `AGENT_HANDOFF_V36_2026-07-04.md` | Record T17 closure continuity and T18 next move. |

Rollback boundary: revert only this MSEA-R28-T17 closure session-sync if
rejected; do not revert material closure commit `5166a624` or older MSEA
history.

## Core Guard Self-Protection Authorization - MSEA-R28-T17 Dispatch Session Sync

Authorized guard-maintenance scope: session-sync only after MSEA-R28-T17
material dispatch commit `b62e1be3`, including active mode, next allowed move,
generated active state, bootstrap read model, front-door continuity, active
handoff, and dispatch state entry.

Protected paths:

| Path | Purpose |
|---|---|
| `CVF_SESSION_MEMORY.md` | Update current mode, current dispatched work, startup acknowledgment, and next allowed move after T17 dispatch. |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | Regenerate compact startup facts after active state update. |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Regenerate aggregate from state sources after T17 dispatch session-sync. |
| `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json` | Update `currentMode` and `previousMode` for T17 dispatched pending worker return. |
| `CVF_SESSION/state/entries/mseaR28T17MineruDurableMemoryWriteAuthorityDecisionDispatch20260704.json` | Record T17 dispatch evidence. |
| `CVF_SESSION/state/entries/nextAllowedMove.json` | Route next move to T17 no-commit docs-only worker execution. |
| `AGENT_HANDOFF_V36_2026-07-04.md` | Record T17 dispatch continuity and worker next move. |

Rollback boundary: revert only this MSEA-R28-T17 dispatch session-sync if
rejected; do not revert material dispatch commit `b62e1be3` or older MSEA
history.

## Core Guard Self-Protection Authorization - MSEA-R28-T16 Closure Session Sync

Authorized guard-maintenance scope: session-sync only after MSEA-R28-T16
material closure commit `0bf81a68`, including active mode, next allowed move,
generated active state, bootstrap read model, front-door continuity, active
handoff, and closure state entry.

Protected paths:

| Path | Purpose |
|---|---|
| `CVF_SESSION_MEMORY.md` | Update current mode, current/closed work, startup acknowledgment, and next allowed move after T16 closure. |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | Regenerate compact startup facts after active state update. |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Regenerate aggregate from state sources after T16 closure session-sync. |
| `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json` | Update `currentMode` and `previousMode` for T16 closed pending T17 work-order authoring. |
| `CVF_SESSION/state/entries/mseaR28T16MineruMemoryStoreAdapterMappingImplementationClosure20260704.json` | Record accepted T16 closure evidence. |
| `CVF_SESSION/state/entries/nextAllowedMove.json` | Route next move to T17 GC-018/source-verified work-order authoring only. |
| `AGENT_HANDOFF_V36_2026-07-04.md` | Record T16 closure continuity and T17 next move. |

Rollback boundary: revert only this MSEA-R28-T16 closure session-sync if
rejected; do not revert material closure commit `0bf81a68` or older MSEA
history.

## Core Guard Self-Protection Authorization - MSEA-R28-T16 Dispatch Session Sync

Authorized guard-maintenance scope: session-sync only after MSEA-R28-T16
material dispatch commit `93d94b0d`, including active mode, next allowed move,
generated active state, bootstrap read model, front-door continuity, active
handoff, and dispatch state entry.

Protected paths:

| Path | Purpose |
|---|---|
| `CVF_SESSION_MEMORY.md` | Update current mode, current dispatched work, startup acknowledgment, and next allowed move after T16 dispatch. |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | Regenerate compact startup facts after active state update. |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Regenerate aggregate from state sources after T16 dispatch session-sync. |
| `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json` | Update `currentMode` and `previousMode` for T16 dispatched pending worker return. |
| `CVF_SESSION/state/entries/mseaR28T16MineruMemoryStoreAdapterMappingImplementationDispatch20260704.json` | Record T16 dispatch evidence. |
| `CVF_SESSION/state/entries/nextAllowedMove.json` | Route next move to T16 no-commit worker execution. |
| `AGENT_HANDOFF_V36_2026-07-04.md` | Record T16 dispatch continuity and worker next move. |

Rollback boundary: revert only this MSEA-R28-T16 dispatch session-sync if
rejected; do not revert material dispatch commit `93d94b0d` or older MSEA
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
