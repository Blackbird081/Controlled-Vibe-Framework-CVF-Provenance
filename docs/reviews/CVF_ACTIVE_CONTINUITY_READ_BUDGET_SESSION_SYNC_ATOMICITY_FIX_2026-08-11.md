# CVF Active Continuity Read-Budget Session-Sync Atomicity Fix

Memory class: FULL_RECORD

Status: ACCEPTED_BOUNDED_FOR_T1_SESSION_SYNC

Date: 2026-08-11

docType: review

## Purpose

Record the bounded commit-steward correction required after T1 introduced an
exact-hash migration registry for oversized active continuity surfaces.

## Target / Source

Target: the commit-steward path classifier and the final T1 continuity sync.

Source authority: the existing mixed-manifest exception in
`docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md`, the
accepted T1 completion review, and the current active-session checker contract.

## Scope / Methodology

The active-session checker requires each migration row to match the current
front-door or handoff bytes exactly. A session change and its pin refresh
therefore cannot be split into separate valid commits. The commit steward now
classifies only the canonical T1 migration registry as an atomic session-sync
companion. Focused tests prove the positive classification and preserve the
material classification of unrelated governance paths.

## Findings / Position

The prior steward classification conflicted with the accepted read-budget
contract: either split order created a transient invalid repository state and
failed the active-session gate. The narrow companion-path classification closes
that integration gap without weakening material/session separation generally.

## Risk / Corrective Action

Risk is bounded by one exact path. No prefix or generic registry exception is
added. Session-sync still requires the active-session checker, generated-state
check, exact manifest evidence, and no-growth migration facts.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/run_agent_commit_steward_preflight.py`; `governance/compat/check_active_session_state.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_finding_to_governance_learning.py` |
| literalTokensReviewed | `ATOMIC_SESSION_COMPANION_PATHS`; `_is_protected_session_path`; `session-sync`; `Expected manifest`; `Actual changed set`; `Manifest delta` |
| gateRunPurpose | confirm the exact-path atomicity exception and protected-checker authorization |
| claimBoundary | one canonical migration registry only; no generic material/session mixing |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add one exact active-continuity migration
registry to commit-steward session-sync classification and focused tests.

Protected paths:

- `governance/compat/run_agent_commit_steward_preflight.py`
- `governance/compat/test_run_agent_commit_steward_preflight.py`

Operator authorization: the accepted T1 exact-eight authority plus the
operator direction to complete bounded trivial reviewer repairs directly. This
fix is required to close T1 without bypassing an enforced commit gate.

Rollback boundary: revert this review, steward correction, focused tests, and
the exact synchronized continuity manifest together. Do not alter the migration
schema, other registry classification, or commit-mode enforcement.

## Verification Plan

- focused commit-steward tests;
- reviewer-fast governance gate;
- Python and governed file-size gates;
- `git diff --check`;
- exact mixed-manifest session-sync plan and closure gates.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| Exact-hash continuity pins made the normal material/session split impossible | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_ADDED | Honor the standard's existing explicit exact-manifest exception and retain focused regression proof |
| Runtime, provider, and cost language appears only in the forbidden boundary | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | No runtime/provider/cost behavior changed; retain zero-call and parked-lane boundary |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex reviewer/closer |
| Provider or surface | local CVF provenance workspace |
| Session or invocation | T1 session-sync atomicity repair, 2026-08-11 |
| Working directory | repository root |
| Command or tool surface | governed reads, `apply_patch`, focused pytest, reviewer-fast gates, Git |
| Target paths | this review, steward source/tests, and the exact eight-path T1 continuity manifest |
| Allowed scope source | accepted T1 closure and operator direct-repair instruction |
| Before status evidence | clean material HEAD `f5c2aabf1`; session sync isolated in a recoverable local stash |
| After status evidence | exact eleven-path atomic closure manifest ready for commit |
| Diff evidence | `git diff --name-status`, focused tests, and steward path-plan output |
| Approval boundary | exact migration-registry atomicity classification only |
| Claim boundary | no session mutation, T2/T3, provider/live, downstream, public, deploy, push, or production action |
| Agent type | reviewer/closer |
| Invocation ID | `active-continuity-session-sync-atomicity-fix-20260811` |
| Expected manifest | `AGENT_HANDOFF_V57_2026-08-10.md`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/activeContinuityReadCostT1Closure20260811.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION_MEMORY.md`; `docs/reviews/CVF_ACTIVE_CONTINUITY_READ_BUDGET_SESSION_SYNC_ATOMICITY_FIX_2026-08-11.md`; `governance/compat/CVF_ACTIVE_CONTINUITY_READ_BUDGET_MIGRATION.json`; `governance/compat/run_agent_commit_steward_preflight.py`; `governance/compat/test_run_agent_commit_steward_preflight.py` |
| Actual changed set | `AGENT_HANDOFF_V57_2026-08-10.md`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/activeContinuityReadCostT1Closure20260811.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION_MEMORY.md`; `docs/reviews/CVF_ACTIVE_CONTINUITY_READ_BUDGET_SESSION_SYNC_ATOMICITY_FIX_2026-08-11.md`; `governance/compat/CVF_ACTIVE_CONTINUITY_READ_BUDGET_MIGRATION.json`; `governance/compat/run_agent_commit_steward_preflight.py`; `governance/compat/test_run_agent_commit_steward_preflight.py` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no path deleted or renamed |

## Mixed Protected-Path Atomicity Authorization

Disposition: AUTHORIZED_EXACT_MANIFEST

Atomicity reason: the active continuity surfaces and their exact hash/line/byte
pins cannot be valid in either split order. The same atomic commit also adds the
machine acceptance path required by the existing steward standard.

Rollback boundary: revert all eleven paths as one unit; no partial rollback is
valid because it would separate continuity bytes from their migration pins.

Exact changed manifest:

- `AGENT_HANDOFF_V57_2026-08-10.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/activeContinuityReadCostT1Closure20260811.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION_MEMORY.md`
- `docs/reviews/CVF_ACTIVE_CONTINUITY_READ_BUDGET_SESSION_SYNC_ATOMICITY_FIX_2026-08-11.md`
- `governance/compat/CVF_ACTIVE_CONTINUITY_READ_BUDGET_MIGRATION.json`
- `governance/compat/run_agent_commit_steward_preflight.py`
- `governance/compat/test_run_agent_commit_steward_preflight.py`

## Epistemic Process Block

EPISTEMIC_PROCESS_NA_WITH_REASON: deterministic local path classification,
exact-byte pin validation, and focused regression tests were sufficient; no
external factual synthesis or competing hypothesis was required.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | local commit-shape classification for one canonical registry |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: no runtime receipt is created |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source diff, standard text, and focused tests |
| invocationBoundary | local governance preflight only |
| interceptionBoundary | no provider, network, product runtime, CLI/MCP, or external interception claim |
| claimLanguage | canonical exact-hash registry may commit atomically with its session surfaces |
| forbiddenExpansion | no generic registry exception, runtime mutation, public-sync, push, deploy, or production claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance repair only; no public-sync action is
authorized.

## Claim Boundary

This review authorizes only the exact eleven-path atomic T1 closure manifest
above. It does not change migration semantics, permit debt growth, release
T2/T3, mutate downstream projects, call providers, deploy, public-sync, or push.
