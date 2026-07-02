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

Startup acknowledged: current mode=`msea_r4_accepted_pending_msea_r5_deep_absorption_work_order_authoring`; active handoff=AGENT_HANDOFF_V32_2026-07-02.md; next allowed move=author a fresh MSEA-R5 GC-018/work order for deep MinerU layer-scan absorption over `docs/`, non-CLI `mineru/` internals, and Docker content verification; parked checkpoint=MSEA-R4 is accepted at material commit `a6ddd8ba` with `PARTIAL` blind-spot verdict and no runtime/package/checker/source-import/public/provider/live claim.

## Current State

| Field | Value |
|---|---|
| Active front door | `CVF_SESSION_MEMORY.md` |
| Bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Canonical state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| Active review queue | `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` |
| Previous active handoff | `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V31_2026-07-02.md` |
| Remote tracking branch | `origin/codex/p1-p5-small-debt-remediation` |
| Latest material packet | `a6ddd8ba` MSEA-R4 MinerU source mirror absorption acceptance |
| Latest session-sync target | session sync after MSEA-R4 closure and V32 handoff rotation |
| Latest closed numbered LHW wave | `LHW24` |

## Current Mode

`msea_r4_accepted_pending_msea_r5_deep_absorption_work_order_authoring`

## Latest Changes

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

Author a fresh source-verified MSEA-R5 GC-018 baseline and
`WORKER_MUST_NOT_COMMIT` work order for deep MinerU detailed document/layer
scan absorption. R5 should target the R4 declared depth gaps and high-value
application surfaces:

- per-file or file-row-compact ledger for `docs/` and non-CLI `mineru/`
  subfolders, including `backend`, `data`, `model`, `resources`, and `utils`;
- Docker content verification for `docker/global/Dockerfile`,
  `docker/compose.yaml`, `docker/china/Dockerfile`, and the 9 hardware-variant
  Dockerfiles;
- mapping to detailed document/layer scan use cases: layout, OCR, table,
  formula, reading order, Markdown/JSON output, RAG handoff, and receipt/quality
  claim boundaries;
- candidate-only classification for runtime/package/checker/MCP/API/RAG
  surfaces.

R5 must remain documentation/reference absorption unless a later fresh
authorization explicitly allows runtime. No install, model download,
execution, source import, package activation, checker implementation,
provider/live proof, public-sync, Web/MCP/model-router/action-authority,
automatic invocation, benchmark, or production claim is authorized now.

FPC-T4, FPC-DLR-T1, MFE-R1, literal trap learning, and KIOD runtime-candidate
parking remain as previously recorded. LHW24 remains the latest closed numbered
LHW wave.

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

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | MSEA-R4 closure session-sync and V32 handoff rotation, 2026-07-02 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, `git mv`, `apply_patch`, active-session generator, session-sync gates |
| Target paths | `AGENTS.md`; `AGENT_HANDOFF_V32_2026-07-02.md`; `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V31_2026-07-02.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION/state/entries/mseaR4MineruUpstreamSourceMirrorAbsorptionClosure20260702.json` |
| Allowed scope source | operator request to inspect MSEA-R4 completion and add follow-up requirements for high-value MinerU detailed document/layer scan absorption |
| Before status evidence | material HEAD `a6ddd8ba`; V31 active handoff near maintainability threshold at 975 lines; session-sync worktree started clean after material commit |
| After status evidence | V32 active handoff created; V31 moved to archive; active session state regenerated; session-sync pending commit |
| Diff evidence | `git diff --cached --name-status`; `git diff --name-status a6ddd8ba..HEAD` after commit |
| Approval boundary | bounded session-sync after accepted MSEA-R4 material closure |
| Claim boundary | session continuity, handoff rotation, next-move routing, and MSEA-R4 closure recording only |
| Agent type | Codex reviewer/session-sync steward |
| Invocation ID | `msea-r4-closure-session-sync-v32-2026-07-02` |
| Expected manifest | `AGENTS.md`; `AGENT_HANDOFF_V32_2026-07-02.md`; `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V31_2026-07-02.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION/state/entries/mseaR4MineruUpstreamSourceMirrorAbsorptionClosure20260702.json` |
| Actual changed set | `AGENTS.md`; `AGENT_HANDOFF_V32_2026-07-02.md`; `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V31_2026-07-02.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION/state/entries/mseaR4MineruUpstreamSourceMirrorAbsorptionClosure20260702.json` |
| Manifest delta | MATCH |
| Deletion or rename disposition | RENAME_ARCHIVE_WITH_REASON: `AGENT_HANDOFF_V31_2026-07-02.md` moved to `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V31_2026-07-02.md` because V31 reached 975 lines and V32 is now the active handoff; no continuity content was deleted. |

## Claim Boundary

V32 is a compact continuity handoff and session-sync carrier. It records
MSEA-R4 acceptance, V31 archive rotation, active session pointers, next allowed
move, and claim boundaries only. It does not create runtime/provider behavior,
external adapter behavior, package activation, checker wiring, live provider
proof, public export, merge authority, worker commit authority, action
authority, or broader production readiness.
