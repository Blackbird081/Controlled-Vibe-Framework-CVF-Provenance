# AGENT HANDOFF V35 - 2026-07-03

Status: ACTIVE HANDOFF
Memory class: active-handoff
Supersedes: `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V34_2026-07-03.md`

## Purpose

Carry compact continuity after MSEA-R24-T1 dispatch and rotate the active
handoff because V34 exceeded the governed active-handoff file-size threshold.

## Scope / Target / Owner Boundary

Target: active CVF session continuity after dispatching MSEA-R24-T1 MinerU
model-source fallback decision.

Owner boundary: this handoff owns session-sync continuity, active pointer
updates, next-move routing, and claim boundaries only. It does not own MinerU
cache execution, alternate-source download execution, parser/OCR/VLM/hybrid/API/
router/Gradio/Docker/WSL execution, local service startup, source document
copy/import, document body read, extraction outputs, provider/live proof,
public-sync, schema/writer/checker/adapter implementation, package reinstall,
Web/MCP/model-router/action-authority work, benchmark, document-truth,
extraction-accuracy, legal advice quality, current-law correctness, runtime
smoke, workflow-chain completion, or production-readiness claims.

## Active Boundary

This is the active handoff named by `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
The prior V34 handoff is archived at
`CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V34_2026-07-03.md` and must not be
appended to. Future continuity updates must edit this V35 handoff or open a
later active successor if size pressure requires another rotation.

## Startup Acknowledgment

Startup acknowledged: current mode=`msea_r24_t1_mineru_model_source_fallback_decision_dispatched_pending_worker_return`; active handoff=AGENT_HANDOFF_V35_2026-07-03.md; next allowed move=execute MSEA-R24-T1 worker under WORKER_MUST_NOT_COMMIT, creating only the named worker return and companion decision matrix, and selecting exactly one route token; parked checkpoint=T2/T3/T4 remain dependent future tranches requiring fresh work orders and release evidence before any cache command, runtime smoke, workflow-chain receipt policy, or production claim.

## Current State

| Field | Value |
|---|---|
| Active front door | `CVF_SESSION_MEMORY.md` |
| Bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Canonical state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| Active review queue | `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` |
| Previous active handoff | `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V34_2026-07-03.md` |
| Remote tracking branch | `origin/codex/p1-p5-small-debt-remediation` |
| Latest material packet | `3e117e95` MSEA-R24-T1 model-source fallback decision dispatch |
| Latest session-sync target | session sync after MSEA-R24-T1 dispatch and handoff rotation |
| Latest closed numbered LHW wave | `LHW24` |

## Current Mode

`msea_r24_t1_mineru_model_source_fallback_decision_dispatched_pending_worker_return`

## Latest Changes

MSEA-R24-T1 MinerU model-source fallback decision dispatch was created at
material commit `3e117e95`.

Dispatch artifacts:

- `docs/baselines/CVF_GC018_MSEA_R24_T1_MINERU_MODEL_SOURCE_FALLBACK_DECISION_2026-07-03.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R24_T1_MINERU_MODEL_SOURCE_FALLBACK_DECISION_2026-07-03.md`

Material verification: pre-dispatch autorun PASS 72/72 and material pre-commit
hook PASS 79/79.

## Next Allowed Move

Next allowed move: execute the MSEA-R24-T1 work order under
WORKER_MUST_NOT_COMMIT.

The worker may create only:

- `docs/reviews/CVF_MSEA_R24_T1_MINERU_MODEL_SOURCE_FALLBACK_DECISION_WORKER_RETURN_2026-07-03.md`
- `docs/reference/CVF_MSEA_R24_T1_MINERU_MODEL_SOURCE_FALLBACK_DECISION_MATRIX_2026-07-03.md`

The worker may source-verify HuggingFace, ModelScope, auto, and local
model-source options and must select exactly one route token from the work
order's allowed list.

Forbidden until a later fresh work order releases it: cache commands,
alternate-source downloads, parser/OCR/VLM/hybrid/API/router/Gradio/Docker/WSL
execution, local service startup, source document copy/import, document body
read, extraction outputs, provider/live proof, public-sync, fuller sensitive
content, Candidate Group B, rejected derived outputs, RAG/S3/schema/writer/
adapter/checker implementation, package reinstall, Web/MCP/model-router/
action-authority work, benchmark, document-truth, extraction-accuracy, legal
advice quality, current-law correctness, runtime smoke, workflow-chain
completion, production readiness, stage, commit, push, or provider/live
governance proof.

T2/T3/T4 remain dependent future tranches requiring fresh work orders and
release evidence.

LHW24 remains the latest closed numbered LHW wave.

## Verification / Evidence

MSEA-R23-T1 material acceptance commit: `e9baa312`.

MSEA-R24 roadmap material commit: `aa2614f6`.

MSEA-R24-T1 material dispatch commit: `3e117e95`.

Previous active handoff V34 was 1118 lines after the prior sync and exceeded
the governed active-handoff hard threshold. This sync opens V35 and archives
V34 instead of appending more status to the oversized active handoff.

## Core Guard Self-Protection Authorization - MSEA-R24-T1 Dispatch Session Sync

Authorized guard-maintenance scope: session-sync and handoff rotation only
after MSEA-R24-T1 material dispatch commit `3e117e95`, including active
handoff rotation from V34 to V35, active mode, next allowed move, generated
active session state, bootstrap read model, front-door continuity, AGENTS
active-handoff pointer, and archived-handoff routing.

Protected paths:

- `AGENTS.md`
- `AGENT_HANDOFF_V35_2026-07-03.md`
- `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V34_2026-07-03.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/mseaR24T1MineruModelSourceFallbackDecisionDispatch20260703.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`

Operator authorization: operator approved handling the whole T1-T4 route, but
governance dependency rules keep T2/T3/T4 as future tranches until T1 selects a
route and a fresh work order releases the next step.

Rollback boundary: revert only this MSEA-R24-T1 dispatch session-sync and
handoff rotation if rejected; do not revert material dispatch commit
`3e117e95` or earlier accepted material/session-sync commits.

## GC-020 HEAD Marker - MSEA-R24-T1 Dispatch Session Sync

| Field | Value |
|---|---|
| lastSessionSyncMaterialHead | `3e117e95` |
| activeHandoff | `AGENT_HANDOFF_V35_2026-07-03.md` |
| archivedHandoff | `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V34_2026-07-03.md` |
| currentMode | `msea_r24_t1_mineru_model_source_fallback_decision_dispatched_pending_worker_return` |
| nextAllowedMove | execute MSEA-R24-T1 worker under WORKER_MUST_NOT_COMMIT |
| generator | `python governance/compat/generate_active_session_state.py --generate` |

## Agent Operation Trace Block - MSEA-R24-T1 Dispatch Session Sync

| Field | Value |
|---|---|
| Session or invocation | MSEA-R24-T1 dispatch session-sync, 2026-07-03 |
| Role | Session-sync steward |
| Operator instruction | Do all T1-T4, interpreted through dependency-gated tranche sequencing |
| Allowed scope source | bounded session-sync after MSEA-R24-T1 material dispatch commit |
| Before status evidence | material HEAD `3e117e95`; active state source already moved to R24-T1 pending worker, bootstrap/front door/handoff still needed sync |
| After status evidence | active session state, bootstrap, front door, AGENTS, and V35 route next move to MSEA-R24-T1 worker execution |
| Approval boundary | bounded session-sync and handoff rotation after MSEA-R24-T1 material dispatch commit |
| Protected path handling | edited only active session/front-door/handoff routing surfaces and generated state aggregate |
| Commit behavior | session-sync steward owns commit; worker execution remains no-commit until reviewer acceptance |
| T2/T3/T4 boundary | dependent future tranches only; no execution before fresh work orders and release evidence |
| Public/export behavior | no public-sync or public export |
| Actual changed set | `AGENTS.md`; `AGENT_HANDOFF_V35_2026-07-03.md`; `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V34_2026-07-03.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/mseaR24T1MineruModelSourceFallbackDecisionDispatch20260703.json`; `CVF_SESSION/state/entries/nextAllowedMove.json` |

