# CVF Session Memory Front Door Root Handoff Archive Baseline

Memory class: SUMMARY_RECORD

Status: BASELINE UPDATE RECORD — accepted for 2026-05-17 session-memory cleanup.

## Purpose

Record the governed baseline update for moving historical root handoffs out of
the repository root and routing active session startup through one front door.

## Scope

In scope:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/handoffs/archive/`
- active handoff pointer `AGENT_HANDOFF_V8_2026-05-17.md`
- guard compatibility updates that previously hard-coded `AGENT_HANDOFF.md`

Out of scope:

- deleting historical handoffs
- rewriting archived handoff contents
- implementing `cvf-cli`
- implementing `cvf-mcp-server`

## Reviewed Change

Root handoff clutter was reduced by keeping only the active handoff in root:

- `AGENT_HANDOFF_V8_2026-05-17.md`

Historical and side-channel handoffs were moved to:

- `CVF_SESSION/handoffs/archive/`

The active state registry now owns the current handoff pointer and archive
pointer:

- `CVF_SESSION/ACTIVE_SESSION_STATE.json`

## Active Boundary

The active session handoff remains:

- `AGENT_HANDOFF_V8_2026-05-17.md`

Archived handoffs under `CVF_SESSION/handoffs/archive/` are provenance-only and
must not be loaded as current session truth unless an audit explicitly requires
historical comparison.

## Latest Work Changes

- Created the session-memory front door.
- Added the machine-readable active state registry.
- Moved historical handoffs out of root into the archive folder.
- Updated affected compatibility checkers away from root `AGENT_HANDOFF.md`.
- Added ADR and knowledge-base entries for the new startup entrypoint.

## Next Action Approval Gate

Next allowed cleanup: classify and quarantine misleading 17.05 review-folder
packets behind a read-first registry.

Approval boundary: do not delete review or handoff provenance without a separate
operator decision and registry update.

## Rationale

The old root layout made session startup ambiguous. Agents could load
`AGENT_HANDOFF.md`, V2-V8, side-channel handoffs, or memory docs and accidentally
inherit stale state. The new layout preserves provenance while removing stale
handoffs from the default visual path.

## Verification

Executed checks:

- `python governance/compat/check_active_session_state.py --enforce`
- `python governance/compat/check_agent_handoff_guard_compat.py --base HEAD --head HEAD --enforce`
- `python governance/compat/check_surface_scan_registry.py --enforce`
- `python governance/compat/check_markdown_structural_completeness.py --base HEAD --head HEAD --enforce`
- `python -m unittest governance.compat.test_check_active_session_state governance.compat.test_check_agent_handoff_guard_compat governance.compat.test_check_surface_scan_registry`

Observed result: all listed targeted checks passed after the archive routing
updates.

## Boundaries And Non-Goals

- This review does not claim CVF has completed Governance Kernel Freeze.
- This review does not claim the review-folder cleanup is complete.
- Archived handoffs remain historical evidence and must not be treated as active
  startup truth.

## Related Artifacts

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/READ_FIRST.md`
- `CVF_SESSION/REQUIRED_STARTUP_GUARDS.md`
- `governance/compat/check_active_session_state.py`
- `governance/compat/check_surface_scan_registry.py`
- `docs/CVF_ARCHITECTURE_DECISIONS.md`
- `docs/CVF_CORE_KNOWLEDGE_BASE.md`

## Claim Boundary

This packet records the root handoff archive cleanup and session-memory
front-door routing baseline. It does not authorize new absorption, new runtime
semantics, or public claims of a unified governed capability runtime.
