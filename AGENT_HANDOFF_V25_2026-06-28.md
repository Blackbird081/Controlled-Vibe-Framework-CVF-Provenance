# AGENT HANDOFF V25 - 2026-06-28

Status: ACTIVE HANDOFF
Memory class: active-handoff
Supersedes: `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V24_2026-06-27.md`

## Startup Acknowledgment

Startup acknowledged: current mode=`fpc_prg_t3_parked_reopen_gate_wiring_closed_pass_bounded_pending_prg_t4_fixture_coverage`; active handoff=AGENT_HANDOFF_V25_2026-06-28.md; next allowed move=FPC-PRG-T4 Fixture Coverage only; parked checkpoint=P0/P1 foundation chain, T7/T8 acceptance ledger, DSD-T0, UAP-T0/T1/T2, DSD-T1, PRG-T0, PRG-T1, PRG-T2, and PRG-T3 are closed bounded through material commit `f74f0b7a`; public repo remains current for UAP public comprehension at `04d88109317c780ceb2062a257c0e863e2379276`; runtime/provider-live lanes, adapter implementation, package activation, public-sync expansion, and MPI-T6 runtime remain parked unless a recorded reopen condition is verified through a fresh governed tranche.

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
| Latest material closure | `f74f0b7a` FPC-PRG-T3 parked reopen gate wiring |
| Latest session sync before V25 rotation | `743b24ad` |
| Public UAP comprehension export | `04d88109317c780ceb2062a257c0e863e2379276` |
| Latest closed numbered LHW wave | `LHW24` |

## Current Mode

`fpc_prg_t3_parked_reopen_gate_wiring_closed_pass_bounded_pending_prg_t4_fixture_coverage`

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

External agent memory files: non-canonical convenience only.

## Latest Work / Changes

Latest material closure: commit `f74f0b7a` closed FPC-PRG-T3 Parked Reopen
Gate Wiring as `CLOSED_PASS_BOUNDED`.

Prior material closure: commit `24726307` closed FPC-DSD-T1 Foundation
Downstream Post-Public-Export Lane Selection Decision as
`CLOSED_PASS_BOUNDED`.

Latest session sync before this rotation: commit `743b24ad` synced the session
after FPC-DSD-T1 closure and pushed it to the provenance branch.

Prerequisite maintenance commit: `f7f4294d` classified
`AGENT_HANDOFF_V25_2026-06-28.md` as `INTERNAL_ONLY` in the root exposure
registry so the new active handoff can exist as a root file without P3 drift.

Current session-sync change: refresh active startup/state pointers and this
handoff so next work routes to PRG-T4 fixture coverage before any downstream
runtime lane.

## Latest Closed Work

| Work | Commit | Disposition |
|---|---|---|
| FPC-SCG-T8 acceptance-ledger carrier reconciliation | `e278c039` | CLOSED_PASS_BOUNDED |
| FPC-DSD-T1 downstream post-public-export lane selection | `24726307` | CLOSED_PASS_BOUNDED; decision `HOLD_DOWNSTREAM_IMPLEMENTATION` |
| FPC-PRG-T0 parked reopen gate systemization | `8d4ed2f4` | CLOSED_PASS_BOUNDED; decision `SYSTEMIZE_PARKED_REOPEN_GATE_BEFORE_DOWNSTREAM_IMPLEMENTATION` |
| FPC-PRG-T1 parked reopen condition source inventory | `ca60e1fd` | CLOSED_PASS_BOUNDED; decision `INVENTORY_REOPEN_CONDITIONS_BEFORE_CHECKER_IMPLEMENTATION` |
| FPC-PRG-T2 parked reopen gate checker | `ec7e4057` | CLOSED_PASS_BOUNDED; decision `CHECKER_EXISTS_BEFORE_GATE_WIRING` |
| FPC-PRG-T3 parked reopen gate wiring | `f74f0b7a` | CLOSED_PASS_BOUNDED; decision `CHECKER_WIRED_INTO_LOCAL_GATES` |
| DSD-T1 session sync | `743b24ad` | CLOSED_PASS |
| V25 root exposure classification | `f7f4294d` | CLOSED_PASS_BOUNDED |

## Next Allowed Move

FPC-PRG-T4 Fixture Coverage only.

PRG-T4 may expand focused unit tests for
`governance/compat/check_fpc_parked_reopen_inventory.py` to cover wired-gate
drift cases such as wrong lane ID, missing evidence fields, boundary flag drift,
and forbidden-list drift. PRG-T4 must not add new gate wiring,
runtime/provider/live work, public-sync, adapter/package/certification,
downstream implementation, or MPI-T6 runtime. Final session/front-door sync is
deferred to PRG-T5 after T4 closes.

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
activation, certification decision, checker implementation, hook wiring,
generated workspace state mutation beyond active session sync, public-sync
expansion, private provenance evidence export, or push from the provenance
workspace is authorized by this handoff.

## Parked Checkpoint

FPC-SCG-T1 closed the P0 system-loop interlock registry visibility gap at
`75fcad20`. FPC-SCG-T2 through FPC-SCG-T7, FPC-DSD-T0, and FPC-UAP-T0 through
FPC-UAP-T2 are closed bounded at current provenance carrier `be253923`.
FPC-SCG-T8 closed the acceptance-ledger provenance carrier reconciliation at
`e278c039`. FPC-DSD-T1 closed the post-public-export downstream hold decision
at `24726307`. FPC-PRG-T0 closed parked reopen gate systemization at
`8d4ed2f4`. FPC-PRG-T1 closed parked reopen condition source inventory at
`ca60e1fd`. FPC-PRG-T2 closed parked reopen gate checker at `ec7e4057`.
FPC-PRG-T3 closed gate wiring at `f74f0b7a`. Runtime/provider-live lanes,
package activation, adapter implementation, public-sync expansion, and MPI-T6
runtime work remain parked unless a recorded reopen condition is verified
through a fresh governed tranche. LHW24 remains the latest closed numbered LHW
wave.

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
- `CVF_SESSION/state/entries/fpcPrgT0ParkedReopenGateSystemizationClosure20260628.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`

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

## Core Guard Self-Protection Authorization - PRG-T0 Session Sync

Authorized guard-maintenance scope: sync compact session front door, generated
active-session state, source state fragments, and active handoff after
FPC-PRG-T0 material closure at `8d4ed2f4`.

Protected paths:

- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/fpcPrgT0ParkedReopenGateSystemizationClosure20260628.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION_MEMORY.md`

Authorization basis: PRG-T0 changed the current mode, latest material closure,
and next allowed move. CVF session governance requires front door, generated
state, state sources, and active handoff to stay aligned after such a change.

Rollback boundary: if this session-sync is rejected, revert only the PRG-T0
session-sync edits listed above. Do not revert PRG-T0 material commit
`8d4ed2f4`, DSD-T1 material commit `24726307`, public-sync commit
`04d88109317c780ceb2062a257c0e863e2379276`, or earlier FPC-SCG/FPC-DSD/FPC-UAP
closures.

## Core Guard Self-Protection Authorization - PRG-T1 Session Sync

Authorized guard-maintenance scope: sync compact session front door, generated
active-session state, source state fragments, and active handoff after
FPC-PRG-T1 material closure at `ca60e1fd`.

Protected paths:

- `AGENT_HANDOFF_V25_2026-06-28.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/fpcPrgT1ParkedReopenConditionSourceInventoryClosure20260628.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION_MEMORY.md`

Operator authorization: approved T1-T5 continuation; PRG-T1 changed the
current mode, latest material closure, and next allowed move. CVF session
governance requires front door, generated state, state sources, and active
handoff to stay aligned after such a change.

Rollback boundary: if this session-sync is rejected, revert only the PRG-T1
session-sync edits listed above. Do not revert PRG-T1 material commit
`ca60e1fd`, PRG-T0 material commit `8d4ed2f4`, DSD-T1 material commit
`24726307`, public-sync commit `04d88109317c780ceb2062a257c0e863e2379276`, or
earlier FPC-SCG/FPC-DSD/FPC-UAP closures.

## Agent Operation Trace Block - PRG-T1 Session Sync

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local repository tools |
| Session or invocation | 2026-06-28 PRG-T1 session sync |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, apply_patch, active-session generator, governance gates |
| Target paths | `AGENT_HANDOFF_V25_2026-06-28.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/fpcPrgT1ParkedReopenConditionSourceInventoryClosure20260628.json`; `CVF_SESSION/state/entries/nextAllowedMove.json` |
| Allowed scope source | PRG-T1 material closure at `ca60e1fd` and session-governance next-move sync requirement |
| Before status evidence | HEAD `ca60e1fd`; PRG-T1 material closure committed separately |
| After status evidence | active-session generator run completed before governance gates |
| Diff evidence | `git diff --name-status ca60e1fd` |
| Approval boundary | PRG-T1 session-sync and pointer refresh only |
| Claim boundary | session-maintenance only; no downstream implementation, runtime/provider/live proof, public-sync mutation, generated workspace state mutation beyond active session, resolver, adapter, package activation, certification, DICE runtime expansion, Policy_Local, Document Translator, Model Gateway/Sandbox runtime expansion, or MPI-T6 runtime |
| Agent type | single-agent session-sync steward |
| Invocation ID | `fpc-prg-t1-session-sync-2026-06-28` |
| Expected manifest | `AGENT_HANDOFF_V25_2026-06-28.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/fpcPrgT1ParkedReopenConditionSourceInventoryClosure20260628.json`; `CVF_SESSION/state/entries/nextAllowedMove.json` |
| Actual changed set | `AGENT_HANDOFF_V25_2026-06-28.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/fpcPrgT1ParkedReopenConditionSourceInventoryClosure20260628.json`; `CVF_SESSION/state/entries/nextAllowedMove.json` |
| Manifest delta | MATCH |

## Core Guard Self-Protection Authorization - PRG-T2 Session Sync

Authorized guard-maintenance scope: sync compact session front door, generated
active-session state, source state fragments, and active handoff after
FPC-PRG-T2 material closure at `ec7e4057`.

Protected paths:

- `AGENT_HANDOFF_V25_2026-06-28.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/fpcPrgT2ParkedReopenGateCheckerClosure20260628.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION_MEMORY.md`

Operator authorization: approved T1-T5 continuation; PRG-T2 changed the
current mode, latest material closure, and next allowed move. CVF session
governance requires front door, generated state, state sources, and active
handoff to stay aligned after such a change.

Rollback boundary: if this session-sync is rejected, revert only the PRG-T2
session-sync edits listed above. Do not revert PRG-T2 material commit
`ec7e4057`, PRG-T1 material commit `ca60e1fd`, PRG-T1 session-sync commit
`5006698c`, PRG-T0 material commit `8d4ed2f4`, public-sync commit
`04d88109317c780ceb2062a257c0e863e2379276`, or earlier FPC closures.

## Agent Operation Trace Block - PRG-T2 Session Sync

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local repository tools |
| Session or invocation | 2026-06-28 PRG-T2 session sync |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, apply_patch, active-session generator, governance gates |
| Target paths | `AGENT_HANDOFF_V25_2026-06-28.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/fpcPrgT2ParkedReopenGateCheckerClosure20260628.json`; `CVF_SESSION/state/entries/nextAllowedMove.json` |
| Allowed scope source | PRG-T2 material closure at `ec7e4057` and session-governance next-move sync requirement |
| Before status evidence | HEAD `ec7e4057`; PRG-T2 material closure committed separately |
| After status evidence | active-session generator run completed before governance gates |
| Diff evidence | `git diff --name-status ec7e4057` |
| Approval boundary | PRG-T2 session-sync and pointer refresh only |
| Claim boundary | session-maintenance only; no downstream implementation, runtime/provider/live proof, public-sync mutation, generated workspace state mutation beyond active session, resolver, adapter, package activation, certification, DICE runtime expansion, Policy_Local, Document Translator, Model Gateway/Sandbox runtime expansion, or MPI-T6 runtime |
| Agent type | single-agent session-sync steward |
| Invocation ID | `fpc-prg-t2-session-sync-2026-06-28` |
| Expected manifest | `AGENT_HANDOFF_V25_2026-06-28.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/fpcPrgT2ParkedReopenGateCheckerClosure20260628.json`; `CVF_SESSION/state/entries/nextAllowedMove.json` |
| Actual changed set | `AGENT_HANDOFF_V25_2026-06-28.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/fpcPrgT2ParkedReopenGateCheckerClosure20260628.json`; `CVF_SESSION/state/entries/nextAllowedMove.json` |
| Manifest delta | MATCH |

## Core Guard Self-Protection Authorization - PRG-T3 Session Sync

Authorized guard-maintenance scope: sync compact session front door, generated
active-session state, source state fragments, and active handoff after
FPC-PRG-T3 material closure at `f74f0b7a`.

Protected paths:

- `AGENT_HANDOFF_V25_2026-06-28.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/fpcPrgT3ParkedReopenGateWiringClosure20260628.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION_MEMORY.md`

Operator authorization: approved T1-T5 continuation; PRG-T3 changed the
current mode, latest material closure, and next allowed move. CVF session
governance requires front door, generated state, state sources, and active
handoff to stay aligned after such a change.

Rollback boundary: if this session-sync is rejected, revert only the PRG-T3
session-sync edits listed above. Do not revert PRG-T3 material commit
`f74f0b7a`, PRG-T2 material commit `ec7e4057`, PRG-T2 session-sync commit
`c22ef0f0`, or earlier FPC closures.

## Agent Operation Trace Block - PRG-T3 Session Sync

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local repository tools |
| Session or invocation | 2026-06-28 PRG-T3 session sync |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, apply_patch, active-session generator, governance gates |
| Target paths | `AGENT_HANDOFF_V25_2026-06-28.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/fpcPrgT3ParkedReopenGateWiringClosure20260628.json`; `CVF_SESSION/state/entries/nextAllowedMove.json` |
| Allowed scope source | PRG-T3 material closure at `f74f0b7a` and session-governance next-move sync requirement |
| Before status evidence | HEAD `f74f0b7a`; PRG-T3 material closure committed separately |
| After status evidence | active-session generator run completed before governance gates |
| Diff evidence | `git diff --name-status f74f0b7a` |
| Approval boundary | PRG-T3 session-sync and pointer refresh only |
| Claim boundary | session-maintenance only; no downstream implementation, runtime/provider/live proof, public-sync mutation, generated workspace state mutation beyond active session, resolver, adapter, package activation, certification, DICE runtime expansion, Policy_Local, Document Translator, Model Gateway/Sandbox runtime expansion, or MPI-T6 runtime |
| Agent type | single-agent session-sync steward |
| Invocation ID | `fpc-prg-t3-session-sync-2026-06-28` |
| Expected manifest | `AGENT_HANDOFF_V25_2026-06-28.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/fpcPrgT3ParkedReopenGateWiringClosure20260628.json`; `CVF_SESSION/state/entries/nextAllowedMove.json` |
| Actual changed set | `AGENT_HANDOFF_V25_2026-06-28.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/fpcPrgT3ParkedReopenGateWiringClosure20260628.json`; `CVF_SESSION/state/entries/nextAllowedMove.json` |
| Manifest delta | MATCH |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local repository tools |
| Session or invocation | 2026-06-28 V25 active handoff rotation |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, apply_patch, active-session generator, governance gates |
| Target paths | `AGENT_HANDOFF_V25_2026-06-28.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/fpcPrgT0ParkedReopenGateSystemizationClosure20260628.json`; `CVF_SESSION/state/entries/nextAllowedMove.json` |
| Allowed scope source | PRG-T0 material closure at `8d4ed2f4` and session-governance next-move sync requirement |
| Before status evidence | HEAD `8d4ed2f4`; PRG-T0 material closure committed separately |
| After status evidence | active-session generator run completed before governance gates |
| Diff evidence | `git diff --name-status 8d4ed2f4` |
| Approval boundary | PRG-T0 session-sync and pointer refresh only |
| Claim boundary | session-maintenance only; no downstream implementation, runtime/provider/live proof, public-sync mutation, generated workspace state mutation beyond active session, resolver, adapter, package activation, certification, DICE runtime expansion, Policy_Local, Document Translator, Model Gateway/Sandbox runtime expansion, or MPI-T6 runtime |
| Agent type | session-sync steward |
| Invocation ID | `fpc-prg-t0-session-sync-2026-06-28` |
| Expected manifest | `AGENT_HANDOFF_V25_2026-06-28.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/fpcPrgT0ParkedReopenGateSystemizationClosure20260628.json`; `CVF_SESSION/state/entries/nextAllowedMove.json` |
| Actual changed set | `AGENT_HANDOFF_V25_2026-06-28.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/fpcPrgT0ParkedReopenGateSystemizationClosure20260628.json`; `CVF_SESSION/state/entries/nextAllowedMove.json` |
| Manifest delta | MATCH |
| Deletion or rename disposition | none |

## Claim Boundary

This handoff is a compact session-continuity and next-move routing surface
only. Complete canonical state lives in `CVF_SESSION/ACTIVE_SESSION_STATE.json`.

## GC-020 Marker - V25 Rotation Session Sync

Session-sync commit `2a04e28e` rotated the active handoff from V24 to V25,
archived V24, and updated front-door/state pointers after prerequisite root
exposure classification commit `f7f4294d`.

Handoff marker commit `8abba150` recorded `2a04e28e` in this active handoff so
the GC-020 in-place handoff HEAD rule can verify the V25 rotation chain.

This marker exists only to satisfy the GC-020 in-place handoff HEAD rule for
the committed V25 rotation. It does not reopen downstream implementation,
runtime/provider/live work, public-sync mutation, adapter implementation,
package activation, certification, Policy_Local, Document Translator,
Model Gateway/Sandbox runtime expansion, or MPI-T6 runtime.

Rollback boundary: if this marker is rejected, revert only this marker commit.
Do not revert V25 rotation commit `2a04e28e`, root exposure classification
commit `f7f4294d`, material commit `24726307`, or public-sync commit
`04d88109317c780ceb2062a257c0e863e2379276`.
