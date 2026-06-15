# CVF GC-018 Session Continuity Rotation Guard Hardening - 2026-06-15

Memory class: GC018_BASELINE_PACKET

Status: AUTHORIZED

## Purpose

Authorize a bounded session-continuity machine guard hardening tranche.

## Objective

Authorize a focused machine-guard hardening pass for session handoff rotation:
any root `AGENT_HANDOFF*.md` other than the active handoff named by
`CVF_SESSION/ACTIVE_SESSION_STATE.json` must fail the active-session guard.

## Decision / Baseline / Proposed Tranche

Decision: authorize one focused guard-hardening tranche.

Baseline: current guard detects duplicate ACTIVE root handoffs and root
ARCHIVED handoffs.

Proposed tranche: generalize stale root handoff detection so any non-active
root `AGENT_HANDOFF*.md` fails, including SUPERSEDED or unexpected statuses.

## Authorization Basis

Operator request: audit the completed IS-1 through IS-10 worker return, then
write the next roadmap and Claude work order.

Reviewer finding: the compaction worker correctly archived V18 and opened V19,
but root V18 required reviewer deletion. The existing guard catches duplicate
ACTIVE root handoffs and ARCHIVED root handoffs, but does not catch a root
handoff marked SUPERSEDED.

## Allowed Scope

- `governance/compat/check_active_session_state.py`
- `governance/compat/test_check_active_session_state.py`
- Worker return review for this hardening pass under `docs/reviews/`

## Forbidden Scope

- Runtime source outside the two governance compat files above.
- Provider/API/live proof.
- Model Gateway behavior.
- Public-sync.
- Legacy absorption or `.private_reference/legacy/` reads.
- Handoff/state mutation, unless a test fixture requires temporary files inside
  a temporary repository.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Root handoff discovery | `governance/compat/check_active_session_state.py` | lines 272-273 | `_root_handoff_paths` | Active session state guard | ACCEPT |
| Handoff status parser | `governance/compat/check_active_session_state.py` | lines 290-296 | `_handoff_status` | Active session state guard | ACCEPT |
| Active root handoff detector | `governance/compat/check_active_session_state.py` | lines 299-305 | `_active_handoffs` | Active session state guard | ACCEPT |
| Exact-one-ACTIVE enforcement | `governance/compat/check_active_session_state.py` | lines 507-512 | `active_handoffs` | `_classify` | ACCEPT |
| Registry mismatch enforcement | `governance/compat/check_active_session_state.py` | lines 513-516 | `active_handoff` | `_classify` | ACCEPT |
| Archived-root stale handoff enforcement | `governance/compat/check_active_session_state.py` | lines 517-526 | `handoff_violations` | `_classify` | ACCEPT |
| Existing archived-root unit coverage | `governance/compat/test_check_active_session_state.py` | lines 238-250 | `test_unregistered_archived_root_handoff_fails` | Active session state tests | ACCEPT |

## Evidence / Verification

Required verification:

- `python -m pytest governance/compat/test_check_active_session_state.py`
- `python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_active_session_state.py`
- `git diff --name-status`
- worker return with Agent Operation Trace Block

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: this GC-018 authorizes machine guard hardening for
current session-continuity files only. It does not scope or absorb legacy
knowledge.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: internal provenance governance guard work only.

## Completion Boundary

Completion requires focused tests, reviewer-fast or worker-return fast gate,
worker return evidence, and Codex review before commit. Claude must not commit.

## Claim Boundary

This GC-018 authorizes only stale root handoff machine-check hardening. It does
not authorize session state mutation, live proof, Model Gateway work, provider
changes, public-sync, or legacy absorption.

## Verification Boundary

Verification is limited to focused active-session guard tests, fast governance
gates, changed-path evidence, and independent Codex review.
