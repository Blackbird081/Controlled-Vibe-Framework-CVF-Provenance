# ADIF-0058 - Authoring Pass Mistaken For Worker-Release Readiness

Memory class: POINTER_RECORD

Status: ACTIVE

```text
defectId: ADIF-0058
title: Authoring pass mistaken for worker-release readiness
defectCategory: PROCESS_AND_GATE_ORDER
defectClass: PHASE_GATE_PLACEMENT_GAP
defectRole: ROOT_CAUSE
severity: HIGH
lifecycleState: ACTIVE
taskClasses: Work-order authoring / dispatch
roles: dispatcher; session-sync steward
lifecyclePhases: pre-dispatch; pre-implementation
surfaceSelectors: docs/baselines/*.md; docs/work_orders/*.md; active handoff and session continuity surfaces
detectionSignals: worker is invoked while packet is untracked or dirty; currentAuthority selects a predecessor packet; active handoff lacks the packet material-SHA marker; nextAllowedMove still authorizes authoring rather than execution
enforcementLevel: MACHINE_CHECKED
checkerBindings: governance/compat/check_dispatch_release_readiness.py; governance/compat/run_agent_autorun_workflow_gate.py
promotionState: MACHINE_CHECK_ADDED
supersedes: NONE
lastVerifiedCommit: 40d430f63
roadmapSeedId: NONE
```

## Purpose

Make premature work-order release discoverable before a worker, CLI, or MCP
invocation becomes the first actor to stop on missing dispatch continuity.

## Scope / Applies To

Applies when a dispatcher authors a baseline/work-order packet and a later
session-sync steward must project the packet's material commit into the active
handoff, bootstrap, state aggregate, front door, and next move. It does not
authorize implementation, provider calls, commits outside the dispatch chain,
public sync, deployment, or production action.

## Bad Example

The packet passes author-fast and a broad pre-dispatch content bundle while its
files are still untracked. The orchestrator sends the work order immediately.
The unattended worker stops because no material commit exists, the handoff has
no material-SHA marker, and `currentAuthority` still names an older packet.

## Good Example

The dispatcher completes packet authoring checks, commits the baseline and
work order together, performs and commits the continuity sync, then runs final
`pre-dispatch` with the exact `--active-work-order`. Only that release receipt
permits worker invocation. The worker revalidates the same binding at
`pre-implementation` before editing.

## Canonical Sources

- `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md`
- `docs/reference/CVF_DISPATCH_RELEASE_READINESS_MACHINE_STANDARD_2026-09-25.md`
- `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md`
- `docs/reference/guard_orientation/README.md`

## Remediation

1. Treat author-fast/pre-commit PASS as packet-content evidence only.
2. Commit the paired baseline/work order as the material dispatch commit.
3. Commit a later continuity projection containing the batch/material marker,
   exact current authority and execution next move.
4. Require the exact work-order binding at final `pre-dispatch`; fail before
   receipt reuse or worker invocation when it is absent.
5. Re-run release readiness at bound `pre-implementation` so continuity drift
   cannot be hidden from the worker entry gate.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Orchestrator released AKOE-P1 after authoring checks but before material and continuity commits | `PHASE_GATE_PLACEMENT_GAP` | `GOVERNANCE_CONTROL_PLANE` | `MACHINE_CHECK_ADDED` | bind final dispatch release to explicit packet, material SHA, continuity commit, current authority and execution next move | Handled by dispatch-release checker and autorun wiring |

Runtime/provider/cost learning lane: `N/A_WITH_REASON` - no provider execution,
live call, credential, quota, or cost behavior was required to reproduce or
guard this local orchestration defect.

## Machine Enforcement

`governance/compat/check_dispatch_release_readiness.py` checks the explicit
work-order binding and the two-commit dispatch chain. The autorun wrapper
requires that binding at `pre-dispatch` when bootstrap says the next move is
work-order based, and reuses the checker at bound `pre-implementation`.
Regression cases cover the three observed failures and a fully committed
positive control.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer and governance guard maintainer |
| Provider or surface | private CVF workspace |
| Session or invocation | AKOE-P1 premature-dispatch correction, 2026-09-25 |
| Working directory | repository root |
| Command or tool surface | governed source reads, `apply_patch`, pytest, autorun and Git |
| Target paths | this entry; dispatch-release standard/checker/tests; autorun runner/catalog/tests; guard routing prose |
| Allowed scope source | operator instruction to tighten the machine gate after the orchestrator failed to finish dispatch before worker handoff |
| Before status evidence | AKOE-P1 worker returned `BLOCKED_WITH_REASON` on untracked packet, absent material marker and stale current authority |
| After status evidence | final bound pre-dispatch fails until packet and continuity are committed and aligned |
| Diff evidence | focused regression suite plus full autorun/pre-commit evidence before commit |
| Approval boundary | governance control-plane correction only |
| Claim boundary | local configured gate behavior; no universal interception of arbitrary messages or external tools |
| Agent type | orchestrator/reviewer |
| Invocation ID | `adif-0058-akoe-p1-dispatch-release-20260925` |
| Expected manifest | this entry plus the dispatch-release hardening manifest |
| Actual changed set | verified before commit |
| Manifest delta | pending final verification |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance defect learning. No public-sync action or public
catalog claim is authorized.

## Epistemic Process Block

### Expected Result / Prediction

A phase-specific, explicitly bound release checker will fail before worker
invocation for the exact incomplete states seen in AKOE-P1.

### Evidence Comparison

Negative fixtures isolate dirty/untracked packet state, a new material commit
without continuity, a missing marker, and stale current authority. The
positive fixture supplies both commits and aligned session state.

### Contradiction Or Gap Disposition

The earlier bundle was not false about packet content; it was insufficient as
release evidence. The correction separates authoring validation from final
worker-release admission.

### Claim Update

The defect is `MACHINE_CHECKED` for configured local autorun entry points, not
for arbitrary out-of-band human messages.

## Claim Boundary

This entry records one orchestration control defect and its bounded machine
guard. It does not assess worker capability, authorize implementation or scope
expansion, or claim provider/live/public/deployment/production readiness.
