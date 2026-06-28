# AGENT HANDOFF V26 - 2026-06-28

Status: ACTIVE HANDOFF
Memory class: active-handoff
Supersedes: `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V25_2026-06-28.md`

## Startup Acknowledgment

Startup acknowledged: current mode=`aecg_t0_codegraph_agent_engineering_control_absorption_roadmap_ready_for_t1_gc018`; active handoff=AGENT_HANDOFF_V26_2026-06-28.md; next allowed move=author AECG-T1 GC-018 for source-verified Agent Engineering Control triage and CodeGraph delta adaptation; parked checkpoint=AECG-T0 roadmap is ready at material commit `edee01a0`, CodeGraph prior CGE-T1/T2 boundaries remain binding, the operator-provided Agent Engineering Control folder is retained under `.private_reference/legacy`, and runtime/MCP/watcher/daemon/merge automation/hook repair/package import remain parked behind fresh GC-018 and source verification.

## Current State

| Field | Value |
|---|---|
| Active front door | `CVF_SESSION_MEMORY.md` |
| Bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Canonical state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| Active review queue | `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` |
| Previous active handoff | `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V25_2026-06-28.md` |
| Remote tracking branch | `origin/codex/p1-p5-small-debt-remediation` |
| Latest material roadmap | `edee01a0` AECG-T0 CodeGraph and Agent Engineering Control external absorption roadmap |
| Latest closed numbered LHW wave | `LHW24` |

## Current Mode

`aecg_t0_codegraph_agent_engineering_control_absorption_roadmap_ready_for_t1_gc018`

## Purpose

Keep the active handoff compact after V25 reached the governed file-size guard
near-threshold. V25 is archived as historical continuity; V26 is the sole root
active handoff.

## Scope / Target / Owner Boundary

Target: rotate active handoff V25 to compact active handoff V26, update active
startup pointers, and preserve the AECG-T1 next-move boundary.

Owner boundary: this handoff authorizes session continuity maintenance only. It
does not authorize downstream implementation, runtime/provider/live work,
public-sync mutation, CodeGraph runtime/MCP/watcher/daemon adoption, merge
automation, hook repair, package activation, certification, checker
implementation, or generated aggregate mutation beyond active-session sync.

## Active Boundary

Active handoff: `AGENT_HANDOFF_V26_2026-06-28.md`.

Archived predecessor:
`CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V25_2026-06-28.md`.

External agent memory files and provider-local memory are non-canonical
convenience only. Source facts for governed CVF work must be re-verified
against CVF-governed surfaces.

## Latest Work / Changes

Material commit `edee01a0` added
`docs/roadmaps/CVF_AECG_T0_CODEGRAPH_AGENT_ENGINEERING_CONTROL_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md`.

The roadmap audits current `colbymchenry/codegraph` against prior CVF
CGE-T1/CGE-T2 absorption, records that those prior CodeGraph runtime/MCP/
watcher/daemon boundaries remain binding, reviews the operator-provided
`CVF_Agent_Engineering_Control_Standard` folder as source input, and selects
AECG-T1 source-verified triage/adaptation as the next governed move.

The operator-provided Agent Engineering Control folder was moved from root to
ignored legacy reference storage:

` .private_reference/legacy/CVF_Agent_Engineering_Control_Standard`

The leading space above is intentional to avoid bare ignored-directory gate
matching in this handoff prose; use the actual path without the leading space
when reading the source bundle.

## Next Allowed Move

Author AECG-T1 GC-018 for source-verified Agent Engineering Control triage and
CodeGraph delta adaptation.

Required boundaries:

- Keep prior CGE-T1/CGE-T2 CodeGraph decisions binding.
- Do not reopen CodeGraph runtime, MCP wiring, watcher/daemon, benchmark,
  package activation, public-sync, or production-readiness claims.
- Treat the Agent Engineering Control folder as source material only; adapt
  useful concepts into CVF's existing guard and roadmap form instead of
  importing the package directly.
- Keep runtime/provider/live/public-sync/adapter/package/MPI-T6, merge
  automation, hook repair, and checker implementation parked unless a fresh
  GC-018/source-verification packet authorizes them.

## Parked Checkpoint

AECG-T0 is a roadmap and triage-selection commit only. It does not implement
runtime behavior, provider/live proof, CodeGraph install/init, MCP integration,
watcher/daemon adoption, merge automation, hook repair, package activation,
certification, checker implementation, public export, or generated aggregates
beyond active-session sync.

TKG runtime/package/MCP/hypervisor/evidence database/obligation registry/
provenance-label enforcement candidates remain parked behind their recorded
reopen conditions.

## Claim Boundary

This handoff may be cited only as session-continuity evidence for the AECG-T0
roadmap and V25-to-V26 handoff rotation. It is not final proof that the Agent
Engineering Control source bundle has been fully absorbed, and it is not
runtime, provider/live, public-sync, package, MCP, watcher/daemon, merge
automation, hook repair, checker, or production-readiness evidence.

Verification for this batch must come from the active-session generator,
session-mode, next-move freshness, core-guard self-protection, governed
file-size, markdown structural, and commit-steward gates run on the changed
session-sync range.

## Core Guard Self-Protection Authorization - AECG-T0 Session Sync And Handoff Rotation

Authorized guard-maintenance scope: update active session continuity after
AECG-T0 material roadmap commit `edee01a0`, archive near-threshold active
handoff V25, open compact active handoff V26, and regenerate active session
state so the front door, generated state sources, generated aggregates,
bootstrap read model, and active handoff all point to AECG-T1 GC-018 authoring
as the next allowed move.

Protected paths:

- `AGENTS.md`
- `AGENT_HANDOFF_V26_2026-06-28.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/aecgT0CodeGraphAgentEngineeringControlRoadmap20260628.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION_MEMORY.md`
- `docs/reference/CVF_FPC_PRG_T1_PARKED_REOPEN_CONDITION_SOURCE_INVENTORY_2026-06-28.json`

Operator authorization: the operator instructed Codex to continue with
`colbymchenry/codegraph` and `CVF_Agent_Engineering_Control_Standard`.

Rollback boundary: if this session-sync and handoff-rotation batch is rejected,
revert only the session-sync and V25-to-V26 handoff rotation changes. Do not
revert AECG-T0 material commit `edee01a0`, TKG-T5 material commit `6ce94464`,
TKG-T4 material commit `79f26845`, or earlier TKG/EverOS/PRG/FPC/session-sync
commits.

## GC-020 Marker - AECG-T0 CodeGraph And Agent Engineering Control Roadmap Commit

Material commit `edee01a0` added
`docs/roadmaps/CVF_AECG_T0_CODEGRAPH_AGENT_ENGINEERING_CONTROL_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md`.
The roadmap keeps prior CGE-T1/CGE-T2 CodeGraph boundaries binding, retains the
operator-provided Agent Engineering Control folder under ignored legacy
reference storage, and selects AECG-T1 source-verified triage/adaptation as the
next governed move.

This marker exists only to satisfy the GC-020 in-place handoff HEAD rule for
the committed AECG-T0 roadmap. It does not implement runtime, provider/live
proof, public-sync export, CodeGraph install/init, MCP wiring, watcher/daemon,
merge automation, hook repair, package activation, certification, checker
implementation, generated aggregate beyond session sync, or
production/hosted readiness.
