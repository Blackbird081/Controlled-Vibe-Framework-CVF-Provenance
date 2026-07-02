# AGENT HANDOFF V32 - 2026-07-02

Status: ACTIVE HANDOFF
Memory class: active-handoff
Supersedes: `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V31_2026-07-02.md`

## Purpose

Carry compact continuity after MSEA-R4 closure and V31 handoff rotation.

## Scope / Target / Owner Boundary

Target: active CVF session continuity after MSEA-R4 reviewer closure and
handoff rotation from V31 to V32.

Owner boundary: this handoff owns session-sync continuity, active pointer
updates, next-move routing, and claim boundaries only. It does not own MinerU
runtime work, source import, public-sync, checker implementation, package
activation, provider/live proof, Web/UI work, MCP/CLI adapter work,
model-router work, action authority, automatic invocation, benchmarks, or
production-readiness claims.

## Active Boundary

This is the active handoff named by `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
The prior V31 handoff is archived at
`CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V31_2026-07-02.md` and must not be
appended to. Future continuity updates must edit this V32 handoff or open a
later active successor if size pressure requires another rotation.

## Startup Acknowledgment

Startup acknowledged: current mode=`msea_r6_mineru_application_route_decision_dispatched_pending_worker_return`; active handoff=AGENT_HANDOFF_V32_2026-07-02.md; next allowed move=execute MSEA-R6 no-commit worker route-decision work order; parked checkpoint=MSEA-R6 worker must return exactly one route decision or blocker and must not commit; no runtime/package/checker/source-import/public/provider/live claim is authorized.

## Current State

| Field | Value |
|---|---|
| Active front door | `CVF_SESSION_MEMORY.md` |
| Bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Canonical state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| Active review queue | `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` |
| Previous active handoff | `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V31_2026-07-02.md` |
| Remote tracking branch | `origin/codex/p1-p5-small-debt-remediation` |
| Latest material packet | `6ab29617` MSEA-R6 MinerU application route decision dispatch |
| Latest session-sync target | session sync after MSEA-R6 dispatch |
| Latest closed numbered LHW wave | `LHW24` |

## Current Mode

`msea_r6_mineru_application_route_decision_dispatched_pending_worker_return`

## Latest Changes

MSEA-R6 MinerU application route decision and adapter-readiness selection is
dispatched at material commit `6ab29617`. The dispatch artifacts are
`docs/baselines/CVF_GC018_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_AND_ADAPTER_READINESS_SELECTION_2026-07-02.md`
and
`docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_AND_ADAPTER_READINESS_SELECTION_2026-07-02.md`.
The worker must run as `WORKER_MUST_NOT_COMMIT` and produce
`docs/reviews/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_AND_ADAPTER_READINESS_SELECTION_WORKER_RETURN_2026-07-02.md`
plus
`docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md`.
The route decision must select exactly one allowed outcome or return a
source-backed blocker. The dispatch pre-dispatch autorun passed 72/72 and
material pre-commit hook passed 79/79. This dispatch does not authorize MinerU
runtime execution, source import, provider/live proof, credentials, S3/RAG use,
package activation, checker implementation, public-sync, Web/MCP/model-router/
action-authority, automatic invocation, benchmark, or production-readiness
claim.

MSEA-R5 MinerU deep document layer scan absorption is accepted at material
commit `1bac8163`. The accepted worker return and owner-surface delta are
`docs/reviews/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_WORKER_RETURN_2026-07-02.md`
and
`docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md`.
The source mirror reconciled 425/425 and the R5 target subset reconciled
373/373. New deferred candidate evidence records `mineru/utils/llm_aided.py`,
`mineru/data/io/s3.py`, RagFlow built-in parser integration evidence, and
output receipt schema evidence. The blind-spot verdict remains `PARTIAL`.

The MSEA-R5 dispatch artifacts remain
`docs/baselines/CVF_GC018_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_2026-07-02.md`
and
`docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_2026-07-02.md`.

MSEA-R4 MinerU upstream source mirror absorption is accepted at material commit
`a6ddd8ba`. The accepted worker return is
`docs/reviews/CVF_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_WORKER_RETURN_2026-07-02.md`
and the owner-surface delta is
`docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md`.
Reviewer repaired the worker-return evidence by recomputing the source-mirror
manifest hash and correcting the Docker file-count wording. Gates passed after
repair, and the material pre-commit hook passed 79/79.

MSEA-R4 remains bounded: full source-mirror count/hash manifest reconciled
425/425, high-value CLI and Docker candidate files are recorded, no prior
MSEA-T0/T1/T2/T3 conclusion is contradicted or reopened, and the blind-spot
verdict remains `PARTIAL` because `docs/` and non-CLI `mineru/` internals were
read only at structural/group depth. No MinerU runtime, install, model
download, OCR/VLM/hybrid/parser/API/router/Gradio/Docker/RAG execution,
provider/live proof, package activation, checker implementation, source
import, public-sync, Web/MCP/model-router/action-authority, automatic
invocation, benchmark, or production-readiness claim is made.

## Next Allowed Move

Execute the MSEA-R6 no-commit worker route-decision work order. Worker must
produce the MSEA-R6 worker return and route decision matrix, evaluate every
allowed route candidate, select exactly one allowed routing outcome or return
`BLOCKED_WITH_REASON`, run required gates or classify blockers, and leave
changes uncommitted. No install, model download, execution, source import,
credential/S3 use, RAG write, package activation, checker implementation,
provider/live proof, public-sync, Web/MCP/model-router/action-authority,
automatic invocation, benchmark, or production claim is authorized now.

FPC-T4, FPC-DLR-T1, MFE-R1, literal trap learning, and KIOD runtime-candidate
parking remain as previously recorded. LHW24 remains the latest closed numbered
LHW wave.

## Core Guard Self-Protection Authorization - MSEA-R6 Dispatch Session Sync

Authorized guard-maintenance scope: session-sync only after material commit
`6ab29617`, including active mode, next allowed move, generated active session
state, front-door continuity, and this active handoff marker.

Protected paths:
- `AGENT_HANDOFF_V32_2026-07-02.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/state/entries/mseaR6MineruApplicationRouteDecisionDispatch20260702.json`

Operator authorization: user requested issuance of the next MinerU work order
after MSEA-R5 completion and detailed document/layer scan value confirmation.

Rollback boundary: revert only this session-sync batch if rejected; do not
alter material commit `6ab29617` or prior accepted material commits.

Not authorized: runtime/provider/live proof, MinerU install, source import,
package activation, model download, OCR/VLM/hybrid/parser/API/router/Gradio/
Docker/RAG execution, checker implementation, public-sync, Web/UI dashboard
work, MCP/CLI adapter implementation, model-router work, action authority,
automatic invocation, benchmark, or production claims.

## Core Guard Self-Protection Authorization - MSEA-R5 Dispatch Session Sync

Authorized guard-maintenance scope: session-sync only after material commit
`7bb7b509`, including active mode, next allowed move, generated active session
state, front-door continuity, and this active handoff marker.

Protected paths:
- `AGENT_HANDOFF_V32_2026-07-02.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/state/entries/mseaR5MineruDeepDocumentLayerScanAbsorptionDispatch20260702.json`

Operator authorization: user requested creation of the deeper MinerU absorption
work order after MSEA-R4, and material commit `7bb7b509` dispatched that
`WORKER_MUST_NOT_COMMIT` lane.

Rollback boundary: revert only this session-sync batch if rejected; do not
alter material commit `7bb7b509` or prior accepted material commits.

Not authorized: runtime/provider/live proof, MinerU install, source import,
package activation, model download, OCR/VLM/hybrid/parser/API/router/Gradio/
Docker/RAG execution, checker implementation, public-sync, Web/UI dashboard
work, MCP/CLI adapter implementation, model-router work, action authority,
automatic invocation, benchmark, or production claims.

## Core Guard Self-Protection Authorization - MSEA-R5 Closure Session Sync

Authorized guard-maintenance scope: session-sync only after material commit
`1bac8163`, including active mode, next allowed move, generated active session
state, front-door continuity, and this active handoff marker.

Protected paths:
- `AGENT_HANDOFF_V32_2026-07-02.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/state/entries/mseaR5MineruDeepDocumentLayerScanAbsorptionClosure20260702.json`

Operator authorization: user asked reviewer to check the MSEA-R5 worker return
and continue after the worker completed the deeper MinerU absorption lane.

Rollback boundary: revert only this session-sync batch if rejected; do not
alter material commit `1bac8163` or prior accepted material commits.

Not authorized: runtime/provider/live proof, MinerU install, source import,
package activation, model download, OCR/VLM/hybrid/parser/API/router/Gradio/
Docker/RAG execution, checker implementation, public-sync, Web/UI dashboard
work, MCP/CLI adapter implementation, model-router work, action authority,
automatic invocation, benchmark, or production claims.

## Core Guard Self-Protection Authorization - MSEA-R4 Closure Session Sync And V32 Rotation

Authorized guard-maintenance scope: session-sync only after material commit
`a6ddd8ba`, including active handoff rotation from V31 to V32.

Protected paths:
- `AGENTS.md`
- `AGENT_HANDOFF_V32_2026-07-02.md`
- `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V31_2026-07-02.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/state/entries/mseaR4MineruUpstreamSourceMirrorAbsorptionClosure20260702.json`

Operator authorization: user asked the reviewer to inspect MSEA-R4 completion
and add follow-up requirements because MinerU has high value for detailed
document/layer scan use cases.

Rollback boundary: revert only this session-sync batch if rejected; do not
alter material commit `a6ddd8ba` or prior accepted material commits.

Not authorized: runtime/provider/live proof, MinerU install, source import,
package activation, model download, OCR/VLM/hybrid/parser/API/router/Gradio/
Docker/RAG execution, checker implementation, public-sync, Web/UI dashboard
work, MCP/CLI adapter implementation, model-router work, action authority,
automatic invocation, benchmark, or production claims.

## GC-020 HEAD Marker - MSEA-R4 Closure

Latest material commit requiring in-place handoff trace:

`a6ddd8ba`

Full SHA:

`a6ddd8baf364c4e5703d5448b02871f62d32c83e`

This marker satisfies the GC-020 in-place handoff HEAD rule for material commit
`a6ddd8ba`. It records accepted MSEA-R4 documentation/reference absorption
only and routes deeper source absorption to MSEA-R5 work-order authoring.

## GC-020 HEAD Marker - MSEA-R4 Session Sync

Latest dedicated session-sync parent commit requiring in-place handoff trace:

`e69eef9e`

Full SHA:

`e69eef9e116644038a3cbfa880449a630be411f5`

This marker records the session-sync commit that opened active V32, archived
V31, updated active session state, and routed the next allowed move to MSEA-R5
work-order authoring. A follow-up handoff-only sync commit may cite this parent
SHA because the content-addressed SHA of that follow-up commit is not knowable
before the handoff edit exists.

## GC-020 HEAD Marker - MSEA-R5 Dispatch Prereq Session Wording Repair

Latest dedicated session-sync parent commit requiring in-place handoff trace:

`6f7103f3`

Full SHA:

`6f7103f3dc8c3b139e5bedaa3dec74985ae4a18f`

This marker records the session-sync commit that repaired active continuity
wording before MSEA-R5 dispatch authoring, avoiding false closed-lane lifecycle
classification while preserving the accepted MSEA-R4 material boundary. A
follow-up handoff-only sync commit may cite this parent SHA because the
content-addressed SHA of that follow-up commit is not knowable before the
handoff edit exists.

## GC-020 HEAD Marker - MSEA-R5 Dispatch

Latest material commit requiring in-place handoff trace:

`7bb7b509`

Full SHA:

`7bb7b5096ceec662c2796e3b13db365a5a88bcc1`

This marker satisfies the GC-020 in-place handoff HEAD rule for material commit
`7bb7b509`. It records MSEA-R5 dispatch only and does not claim worker
execution, source import, runtime/provider/live proof, public-sync, package
activation, checker implementation, MCP/CLI adapter behavior, model-router
work, action authority, automatic invocation, benchmark, or production
readiness.

## GC-020 HEAD Marker - MSEA-R5 Closure

Latest material commit requiring in-place handoff trace:

`1bac8163`

Full SHA:

`1bac8163e657c31a36b7011849b5c2a9277c4c3b`

This marker satisfies the GC-020 in-place handoff HEAD rule for material commit
`1bac8163`. It records accepted MSEA-R5 documentation/reference absorption
only and routes any MinerU follow-up through fresh GC-018/source-verified work
order selection.

## GC-020 HEAD Marker - MSEA-R6 Dispatch

Latest material commit requiring in-place handoff trace:

`6ab29617`

Full SHA:

`6ab296176ae7fdaf4291f01a01306ff12726d26d`

This marker satisfies the GC-020 in-place handoff HEAD rule for material commit
`6ab29617`. It records MSEA-R6 dispatch only and does not claim worker
execution, MinerU runtime behavior, source import, provider/live proof,
credential/S3/RAG use, public-sync, package activation, checker implementation,
MCP/CLI adapter behavior, model-router work, action authority, automatic
invocation, benchmark, or production readiness.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | MSEA-R6 dispatch session-sync, 2026-07-02 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, `apply_patch`, active-session generator, session-sync gates |
| Target paths | `AGENT_HANDOFF_V32_2026-07-02.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION/state/entries/mseaR6MineruApplicationRouteDecisionDispatch20260702.json` |
| Allowed scope source | operator request to issue the next MinerU work order after MSEA-R5 and material commit `6ab29617` dispatching MSEA-R6 |
| Before status evidence | material HEAD `6ab29617`; session-sync worktree started clean after material commit |
| After status evidence | active session state regenerated; front door and active handoff route next move to MSEA-R6 worker execution; session-sync pending commit |
| Diff evidence | `git diff --name-status`; `git diff --cached --name-status` before session-sync commit |
| Approval boundary | bounded session-sync after MSEA-R6 dispatch material commit |
| Claim boundary | session continuity, next-move routing, and MSEA-R6 dispatch recording only |
| Agent type | Codex reviewer/session-sync steward |
| Invocation ID | `msea-r6-dispatch-session-sync-2026-07-02` |
| Expected manifest | `AGENT_HANDOFF_V32_2026-07-02.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION/state/entries/mseaR6MineruApplicationRouteDecisionDispatch20260702.json` |
| Actual changed set | `AGENT_HANDOFF_V32_2026-07-02.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION/state/entries/mseaR6MineruApplicationRouteDecisionDispatch20260702.json` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in this session-sync batch. |

## Claim Boundary

V32 is a compact continuity handoff and session-sync carrier. It records
MSEA-R4 acceptance, V31 archive rotation, active session pointers, next allowed
move, and claim boundaries only. It does not create runtime/provider behavior,
external adapter behavior, package activation, checker wiring, live provider
proof, public export, merge authority, worker commit authority, action
authority, or broader production readiness.
