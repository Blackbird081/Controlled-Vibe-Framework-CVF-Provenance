# ADIF-0045 - Detached Launch With Spaced Path Lacks Preflight Proof

Memory class: POINTER_RECORD

Status: ACTIVE

```text
defectId: ADIF-0045
title: Detached launch with spaced path lacks preflight proof
defectCategory: GATE_TRIGGER_FRICTION
defectClass: RULE_GAP
defectRole: dispatcher
severity: HIGH
lifecycleState: ACTIVE
taskClasses: Work-order authoring / dispatch; Worker execution (`WORKER_MUST_NOT_COMMIT`); Reviewer-return review
roles: dispatcher; worker; reviewer
lifecyclePhases: pre-dispatch; pre-implementation; pre-closure
surfaceSelectors: no-retry detached process launch using Start-Process ArgumentList with absolute script or input paths containing spaces
detectionSignals: child stderr reports truncated File argument; target script never executes; launched PID exits before first poll; no launch-mechanics smoke proof preceded the one-shot action
enforcementLevel: GUIDANCE_ONLY
checkerBindings: NOT_APPLICABLE_WITH_REASON: generic repository gates cannot prove provider-specific or shell-version-specific command-line marshaling
promotionState: MACHINE_CHECK_CANDIDATE
supersedes: NONE
lastVerifiedCommit: 8824cb8c7
roadmapSeedId: NONE
```

## Purpose

Prevent a one-shot detached local process from consuming its only authorized
invocation because a path containing spaces is split before the target script
starts.

## Scope / Applies To

Applies to no-retry or quota-bounded process launches that rely on
`Start-Process -ArgumentList`, especially when `-File` or another path-bearing
argument is absolute and contains spaces.

## Bad Example

Pass an unquoted absolute script path as one array element to `-ArgumentList`
and spend the real one-shot invocation without first proving the final child
command line against a harmless disposable script or echo target.

## Good Example

Before releasing the real invocation, prove the exact launch mechanism with a
disposable local smoke target whose path also contains spaces. Require the
child to echo every received argument, exit cleanly, and leave a durable
stdout/stderr result. Only then substitute the real target paths without
changing quoting, working directory, executable, or argument construction.

## Canonical Sources

- `docs/work_orders/CVF_AGENT_WORK_ORDER_CONTINUOUS_PROJECTION_T4_BOUNDED_PILOT_AND_CLOSURE_2026-07-20.md`, R3 Phase B.
- `docs/reviews/CVF_CONTINUOUS_PROJECTION_T4_WORKER_RETURN_2026-07-20.md`, R3 launch failure.
- `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0044.md`, parent-child timeout reconciliation.
- `docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`, diagnose-before-rerun discipline.

## Remediation

A no-retry detached launch must receive a disposable preflight that exercises
the same executable, working directory, launch API, quoting strategy, and
space-bearing argument shape without touching the real target. If the preflight
cannot prove argument fidelity, the real invocation remains blocked. Do not use
the real action itself as the quoting experiment.

## Epistemic Process Block

### Expected Result / Prediction

The single R3 process should start the target receipt script and remain
observable through short PID polls.

### Evidence Comparison

The process returned PID 22624 but exited before the first poll. Stderr showed
that `-File` received only `D:\UNG`; the target script never executed.

### Contradiction Or Gap Disposition

The supervision design solved the R2 parent-timeout problem, but its launch
mechanics were not preflighted against the workspace's space-bearing path. The
real no-retry PID became the quoting test.

### Claim Update

R3 proves only a clean fail-closed launch failure. It does not test the receipt
script or real-root mapper behavior.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex reviewer/closer |
| Provider or surface | local private provenance workspace |
| Session or invocation | Continuous Projection T4 R3 final blocked-return closure, 2026-07-21 |
| Working directory | repository root |
| Command or tool surface | local evidence reads, Git, PowerShell process inspection, apply_patch, Python governance gates |
| Target paths | ADIF-0045 entry and entries README row |
| Allowed scope source | reviewer closure conversion and operator instruction to record reusable findings |
| Before status evidence | R3 worker returned two unstaged review paths at clean executionBaseHead `8824cb8c7` |
| After status evidence | defect is resolver-discoverable and T4 is closed blocked bounded without R4 |
| Diff evidence | reviewer material closure changed set |
| Approval boundary | learning and bounded closure only; no scan, provider, CLI/MCP, public, or production action |
| Claim boundary | guidance only; no generic quoting checker or helper is implemented |
| Agent type | reviewer/closer |
| Invocation ID | `continuous-projection-t4-adif-0045-2026-07-21` |
| Expected manifest | ADIF-0045 and README row inside the T4 blocked closure batch |
| Actual changed set | ADIF-0045 and README row inside the T4 blocked closure batch |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private governance learning; public-sync is outside this closure.

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | detached-launch argument-fidelity guidance only |
| claimDisposition | CLAIM_REJECTED: no automatic quoting enforcement or cross-shell guarantee |
| receiptEvidence | `CLAIM_REJECTED_NO_RECEIPT`: the target script never executed |
| actionEvidence | ACTION_EVIDENCE_PRESENT: PID, stderr, clean-root, and no-orphan evidence support the defect |
| invocationBoundary | local reviewer inspection and documentation only |
| interceptionBoundary | no provider, CLI/MCP adapter, browser, public, runtime, or production interception |
| claimLanguage | preflight the exact space-bearing launch shape before spending a no-retry invocation |
| forbiddenExpansion | no R4, real scan, helper implementation, provider/live call, public-sync, or production mutation |

## Claim Boundary

This entry records a reusable launch-preflight defect. It does not authorize a
new T4 attempt or claim that one quoting strategy is portable across shells.
