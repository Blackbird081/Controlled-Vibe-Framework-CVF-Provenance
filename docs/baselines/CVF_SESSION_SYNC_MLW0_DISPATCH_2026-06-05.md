# CVF Session Sync: MLW0 Dispatch

Memory class: POINTER_RECORD

Status: SESSION_SYNC_ONLY

docType: baseline

Date: 2026-06-05

## Purpose

Session state sync after MLW0 dispatch commit `b9c4a114`. Updates
`currentMode` and `nextAllowedMove` in active session state and front door.

## Scope / Target / Owner Boundary

Target: session state files `CVF_SESSION/ACTIVE_SESSION_STATE.json` and
`CVF_SESSION_MEMORY.md`. Owner: CVF session continuity surface.

Change scope: mode marker and `nextAllowedMove` field update only. No
governance policy, checker, guard contract, roadmap authority, or runtime
artifact is changed.

## Source / Predecessor Evidence

| Predecessor | Evidence | Dependency |
| --- | --- | --- |
| MLW0 dispatch commit | `b9c4a114` | dispatch baseline and work order committed |
| MLW0 GC-018 | `docs/baselines/CVF_GC018_MLW0_CURRENT_SOURCE_VERIFICATION_MAP_2026-06-05.md` | AUTHORIZED_DISPATCH_PACKET |
| MLW0 work order | `docs/work_orders/CVF_WO_MLW0_CURRENT_SOURCE_VERIFICATION_MAP_2026-06-05.md` | DISPATCH_READY |
| CI1-T11 roadmap | `docs/roadmaps/CVF_CI1_T11_MEMORY_LEARNING_ABSORPTION_CONSOLIDATED_ROADMAP_2026-06-05.md` | ROADMAP_READY — source of MLW0 tranche |

## Decision / Baseline / Proposed Tranche

Decision: SESSION_SYNC_ONLY — update mode and nextAllowedMove to reflect
MLW0 DISPATCH_READY. No tranche is opened by this baseline; MLW0 GC-018
is the authorizing baseline.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: session state mode and nextAllowedMove
field update only. No governance policy, no checker, no guard contract, no
roadmap authority changed.

Protected paths:

- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION_MEMORY.md`

Operator authorization: operator selected option A (open MLW0) on 2026-06-05;
session sync follows from dispatch commit `b9c4a114` as the mandatory
continuity step.

Rollback boundary: revert both files to HEAD at `b9c4a114` if the session sync
introduces a state incompatibility; no runtime artifacts are affected.

## Change Summary

- `currentMode`: `ci1_t11_memory_learning_related_scan_wave_roadmap_ready` →
  `mlw0_current_source_verification_map_dispatch_ready`
- `nextAllowedMove`: updated to point to MLW0 work order at `b9c4a114`
- `mlw0CurrentSourceVerificationMap`: new field recording DISPATCH_READY status
- `CVF_SESSION_MEMORY.md` continuity note and mode marker updated to match

## Evidence / Verification

Required verification for this session sync:

```powershell
python governance/compat/check_active_session_state.py --base b9c4a114 --head HEAD --enforce
```

Passes when HEAD SHA `b9c4a114` is present in active handoff and mode
field matches `mlw0_current_source_verification_map_dispatch_ready`.

## Claim Boundary

This baseline authorizes a session-state mode update only. It does not
authorize runtime implementation, route changes, schema changes, test
creation, live governance proof, public-sync, hosted readiness, production
readiness, public readiness, or autonomous mutation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: session state sync artifact; internal governance continuity record only.
