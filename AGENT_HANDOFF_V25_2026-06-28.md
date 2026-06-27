# AGENT HANDOFF V25 - 2026-06-28

Status: ACTIVE HANDOFF
Memory class: active-handoff
Supersedes: `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V24_2026-06-27.md`

## Startup Acknowledgment

Startup acknowledged: current mode=`fpc_dsd_t1_downstream_hold_closed_pass_bounded_pending_hold_or_fresh_reopen_condition`; active handoff=AGENT_HANDOFF_V25_2026-06-28.md; next allowed move=hold downstream implementation by default, or open a fresh GC-018/source-verified downstream or foundation-maintenance tranche only if a concrete recorded reopen condition is satisfied by current source evidence; parked checkpoint=P0/P1 foundation chain, T7/T8 acceptance ledger, DSD-T0, UAP-T0/T1/T2, and DSD-T1 are closed bounded through material commit `24726307`; public repo remains current for UAP public comprehension at `04d88109317c780ceb2062a257c0e863e2379276`; runtime/provider-live lanes, adapter implementation, package activation, public-sync expansion, and MPI-T6 runtime remain parked unless a recorded reopen condition is verified through a fresh governed tranche.

## Current State

| Field | Value |
|---|---|
| Active front door | `CVF_SESSION_MEMORY.md` |
| Bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Canonical state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| Active review queue | `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` |
| Previous active handoff | `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V24_2026-06-27.md` |
| Remote tracking branch | `origin/codex/p1-p5-small-debt-remediation` |
| Current local/remote base before V25 rotation | `743b24ad` |
| V25 root exposure classification | `f7f4294d` |
| Latest material closure | `24726307` FPC-DSD-T1 downstream hold decision |
| Latest session sync before V25 rotation | `743b24ad` |
| Public UAP comprehension export | `04d88109317c780ceb2062a257c0e863e2379276` |
| Latest closed numbered LHW wave | `LHW24` |

## Current Mode

`fpc_dsd_t1_downstream_hold_closed_pass_bounded_pending_hold_or_fresh_reopen_condition`

## Purpose

Keep the active handoff compact after V24 exceeded the active-markdown soft
threshold and accumulated prior route markers. V24 is archived as historical
continuity; V25 is the sole root active handoff.

## Scope / Target / Owner Boundary

Target: rotate active handoff V24 to compact active handoff V25, update active
startup pointers, and preserve the DSD-T1 downstream-hold boundary.

Owner boundary: this handoff authorizes session continuity maintenance only. It
does not authorize downstream implementation, runtime/provider/live work,
public-sync mutation, MPI-T6 runtime reopening, adapter implementation, package
activation, certification, resolver mutation, or generated workspace state
mutation beyond active-session sync.

## Active Boundary

Active handoff: `AGENT_HANDOFF_V25_2026-06-28.md`.

Archived predecessor:
`CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V24_2026-06-27.md`.

Remote tracking branch: `origin/codex/p1-p5-small-debt-remediation`.

Exact remote SHA must be derived live from git when needed; do not hand-maintain
remote SHA in handoff.

## Latest Work / Changes

Latest material closure: commit `24726307` closed FPC-DSD-T1 Foundation
Downstream Post-Public-Export Lane Selection Decision as
`CLOSED_PASS_BOUNDED`.

Latest session sync before this rotation: commit `743b24ad` synced the session
after FPC-DSD-T1 closure and pushed it to the provenance branch.

Prerequisite maintenance commit: `f7f4294d` classified
`AGENT_HANDOFF_V25_2026-06-28.md` as `INTERNAL_ONLY` in the root exposure
registry so the new active handoff can exist as a root file without P3 drift.

Current change: archive V24, open compact V25, refresh active startup/state
pointers.

## Latest Closed Work

| Work | Commit | Disposition |
|---|---|---|
| FPC-SCG-T8 acceptance-ledger carrier reconciliation | `e278c039` | CLOSED_PASS_BOUNDED |
| FPC-DSD-T1 downstream post-public-export lane selection | `24726307` | CLOSED_PASS_BOUNDED; decision `HOLD_DOWNSTREAM_IMPLEMENTATION` |
| DSD-T1 session sync | `743b24ad` | CLOSED_PASS |
| V25 root exposure classification | `f7f4294d` | CLOSED_PASS_BOUNDED |

## Next Allowed Move

Hold downstream implementation by default. A fresh GC-018/source-verified
downstream or foundation-maintenance tranche may open only if current source
evidence satisfies one recorded reopen condition.

Recorded reopen conditions:

- `use-case-adapter-public`: a fresh GC-018 proves a concrete adapter behavior
  or public-surface gap remains after UAP-T2, cites owner source files, and
  includes public/provenance boundary evidence.
- `runtime-provider-live`: a fresh GC-018 proves a concrete runtime governance
  behavior claim needs live proof, with secret-safe diagnostics and
  quota/provider failure classification.
- `MPI-T6-runtime`: a fresh GC-018 proves an operator-stated product
  requirement explicitly needs the MPI lane itself and current MPI
  contract/helper/durable surfaces are insufficient.

No runtime/MCP/CLI/IDE bridge implementation, provider/live proof,
Policy_Local, Document Translator, Model Gateway/Sandbox runtime expansion,
MPI-T6 runtime work, resolver mutation, adapter implementation, package
activation, certification decision, generated workspace state mutation beyond
active session sync, public-sync expansion, private provenance evidence export,
or push from the provenance workspace is authorized by this handoff.

## Parked Checkpoint

FPC-SCG-T1 closed the P0 system-loop interlock registry visibility gap at
`75fcad20`. FPC-SCG-T2 through FPC-SCG-T7, FPC-DSD-T0, and FPC-UAP-T0 through
FPC-UAP-T2 are closed bounded at current provenance carrier `be253923`.
FPC-SCG-T8 closed the acceptance-ledger provenance carrier reconciliation at
`e278c039`. FPC-DSD-T1 closed the post-public-export downstream hold decision
at `24726307`. Runtime/provider-live lanes, package activation, adapter
implementation, public-sync expansion, and MPI-T6 runtime work remain parked
unless a recorded reopen condition is verified through a fresh governed
tranche. LHW24 remains the latest closed numbered LHW wave.

## Core Guard Self-Protection Authorization - V25 Handoff Rotation

Authorized guard-maintenance scope: rotate the active handoff after V24 crossed
the active-markdown soft threshold, update front-door/state pointers, and keep
downstream implementation parked. Root exposure classification for V25 was
completed separately at `f7f4294d`.

Protected paths:

- `AGENTS.md`
- `AGENT_HANDOFF_V25_2026-06-28.md`
- `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V24_2026-06-27.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`

Operator authorization: the operator asked to continue through the next move;
the current next move permits foundation maintenance only when source evidence
supports it, and the source evidence is V24 line count plus governed file-size
policy requiring active handoff rotation near threshold.

Rollback boundary: if this rotation is rejected, revert only the V25 handoff
rotation, V24 archival move, pointer updates, and generated active-session
aggregate/read model. Do not revert root exposure classification commit
`f7f4294d`, material commit `24726307`, session-sync commit `743b24ad`,
public-sync commit `04d88109317c780ceb2062a257c0e863e2379276`, or earlier
FPC-SCG/FPC-DSD/FPC-UAP closures.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local repository tools |
| Session or invocation | 2026-06-28 V25 active handoff rotation |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, git mv, apply_patch, active-session generator, governance gates |
| Target paths | `AGENTS.md`; `AGENT_HANDOFF_V25_2026-06-28.md`; `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V24_2026-06-27.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json` |
| Allowed scope source | governed file-size advisory for active handoff V24 and AGENTS.md handoff-rotation rule |
| Before status evidence | HEAD `f7f4294d`; V24 line count 1040; V25 root exposure classification already committed |
| After status evidence | active-session generator run completed before governance gates |
| Diff evidence | `git diff --name-status f7f4294d..HEAD` |
| Approval boundary | active handoff rotation and pointer sync only |
| Claim boundary | session-maintenance only; no downstream implementation, runtime/provider/live proof, public-sync mutation, generated workspace state mutation beyond active session, resolver, adapter, package activation, certification, DICE runtime expansion, Policy_Local, Document Translator, Model Gateway/Sandbox runtime expansion, or MPI-T6 runtime |
| Agent type | session-sync steward |
| Invocation ID | `v25-active-handoff-rotation-2026-06-28` |
| Expected manifest | `AGENTS.md`; `AGENT_HANDOFF_V25_2026-06-28.md`; `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V24_2026-06-27.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json` |
| Actual changed set | `AGENTS.md`; `AGENT_HANDOFF_V25_2026-06-28.md`; `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V24_2026-06-27.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json` |
| Manifest delta | MATCH |
| Deletion or rename disposition | V24 is archived to `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V24_2026-06-27.md`; V25 is the active root handoff |

## Claim Boundary

This handoff is a compact session-continuity and next-move routing surface
only. Complete canonical state lives in `CVF_SESSION/ACTIVE_SESSION_STATE.json`.

## GC-020 Marker - V25 Rotation Session Sync

Session-sync commit `2a04e28e` rotated the active handoff from V24 to V25,
archived V24, and updated front-door/state pointers after prerequisite root
exposure classification commit `f7f4294d`.

This marker exists only to satisfy the GC-020 in-place handoff HEAD rule for
the committed V25 rotation. It does not reopen downstream implementation,
runtime/provider/live work, public-sync mutation, adapter implementation,
package activation, certification, Policy_Local, Document Translator,
Model Gateway/Sandbox runtime expansion, or MPI-T6 runtime.

Rollback boundary: if this marker is rejected, revert only this marker commit.
Do not revert V25 rotation commit `2a04e28e`, root exposure classification
commit `f7f4294d`, material commit `24726307`, or public-sync commit
`04d88109317c780ceb2062a257c0e863e2379276`.
