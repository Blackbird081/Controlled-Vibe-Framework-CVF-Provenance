# CVF Active Continuity Read-Budget Head-Anchor Companion Fix

Memory class: FULL_RECORD

Status: ACCEPTED_BOUNDED_FOR_FINAL_ANCHOR

Date: 2026-08-11

docType: review

## Purpose

Close the final GC-020 integration gap created when the active handoff is
exact-hash pinned by the active-continuity migration registry.

## Target / Source

Target: the active-session session-sync path classifier and its focused proof.

Source: GC-020 parent-SHA acceptance in
`governance/compat/check_active_session_state.py`, the active-continuity
migration registry, and the accepted T1 closure-sync commit `83a80c318`.

## Scope / Methodology

Classify only the canonical migration registry as a session-sync companion.
Add one focused assertion, synchronize the handoff to the current closure HEAD,
and refresh its exact no-growth pin. No prefix or generic registry exception is
introduced.

## Findings / Position

The parent-SHA rule already accepts a dedicated session-sync commit, but its
path classifier omitted the registry that must change whenever the pinned
handoff bytes change. That omission made the final anchor impossible without a
transient invalid pin.

## Risk / Corrective Action

Risk is bounded to one exact path. A final follow-up commit may change only the
handoff and registry, allowing the handoff to cite this repair's parent SHA.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_active_session_state.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_finding_to_governance_learning.py` |
| literalTokensReviewed | `_is_session_sync_path`; `handoffSyncCommitOnly`; `Expected manifest`; `Actual changed set`; `Manifest delta` |
| gateRunPurpose | confirm the source-reviewed exact registry companion classification and record closure evidence for GC-020 parent-SHA enforcement |
| claimBoundary | one canonical migration registry only; no generic session-path expansion |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add the canonical read-budget migration
registry to the existing active-session sync-path classifier and focused proof.

Protected paths:

- `governance/compat/check_active_session_state.py`
- `governance/compat/test_check_active_session_state.py`

Operator authorization: accepted T1 closure authority and the operator's
direction to complete bounded reviewer repairs directly.

Rollback boundary: revert this exact five-path repair together. Do not alter
other session-path classification, migration semantics, or GC-020 enforcement.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| Exact handoff pin omitted from session-sync path ownership | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_ADDED | Accept only the canonical registry companion and retain focused proof |
| Runtime/provider terms appear only in the forbidden boundary | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | No runtime or provider behavior changed; retain zero-call boundary |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex reviewer/closer |
| Provider or surface | local CVF provenance workspace |
| Session or invocation | T1 final head-anchor companion repair, 2026-08-11 |
| Working directory | repository root |
| Command or tool surface | governed reads, `apply_patch`, focused pytest, local gates, Git |
| Target paths | exact five-path repair manifest below |
| Allowed scope source | accepted T1 closure and operator direct-repair instruction |
| Before status evidence | closure-sync HEAD `83a80c318`; staged zero; parked mode active |
| After status evidence | exact companion classifier plus synchronized no-growth handoff pin |
| Diff evidence | exact name-status, focused tests, active-session report, local gates |
| Approval boundary | final T1 closure anchoring only |
| Claim boundary | no T2/T3, provider/live, downstream, public-sync, push, deploy, or production action |
| Agent type | reviewer/closer |
| Invocation ID | `active-continuity-head-anchor-companion-fix-20260811` |
| Expected manifest | `AGENT_HANDOFF_V57_2026-08-10.md`; `docs/reviews/CVF_ACTIVE_CONTINUITY_READ_BUDGET_HEAD_ANCHOR_COMPANION_FIX_2026-08-11.md`; `governance/compat/CVF_ACTIVE_CONTINUITY_READ_BUDGET_MIGRATION.json`; `governance/compat/check_active_session_state.py`; `governance/compat/test_check_active_session_state.py` |
| Actual changed set | `AGENT_HANDOFF_V57_2026-08-10.md`; `docs/reviews/CVF_ACTIVE_CONTINUITY_READ_BUDGET_HEAD_ANCHOR_COMPANION_FIX_2026-08-11.md`; `governance/compat/CVF_ACTIVE_CONTINUITY_READ_BUDGET_MIGRATION.json`; `governance/compat/check_active_session_state.py`; `governance/compat/test_check_active_session_state.py` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no path deleted or renamed |

## Mixed Protected-Path Atomicity Authorization

Disposition: AUTHORIZED_EXACT_MANIFEST

Atomicity reason: the handoff, exact pin, classifier, proof, and authorization
must land together so the current active-session gate remains valid.

Rollback boundary: revert all five paths together; no partial rollback is
valid because it separates the handoff bytes from their exact pin or gate.

Exact changed manifest:

- `AGENT_HANDOFF_V57_2026-08-10.md`
- `docs/reviews/CVF_ACTIVE_CONTINUITY_READ_BUDGET_HEAD_ANCHOR_COMPANION_FIX_2026-08-11.md`
- `governance/compat/CVF_ACTIVE_CONTINUITY_READ_BUDGET_MIGRATION.json`
- `governance/compat/check_active_session_state.py`
- `governance/compat/test_check_active_session_state.py`

## Epistemic Process Block

EPISTEMIC_PROCESS_NA_WITH_REASON: deterministic path classification, exact-byte
pin validation, and focused regression tests were sufficient; no external
factual synthesis or competing hypothesis was required.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | local session-sync path classification for one canonical registry |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: no runtime receipt is created |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source diff, exact pin, and focused test |
| invocationBoundary | local governance compatibility only |
| interceptionBoundary | no provider, network, product runtime, CLI/MCP, or external interception claim |
| claimLanguage | canonical migration registry may accompany its pinned handoff in session-sync |
| forbiddenExpansion | no generic exception, T2/T3, runtime, downstream, public-sync, push, deploy, or production action |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance repair only; no public-sync action is
authorized.

## Claim Boundary

This review authorizes only the exact five-path repair above and the subsequent
two-path final anchor. It does not release T2/T3 or authorize provider/live,
downstream, public-sync, push, deployment, or production work.
