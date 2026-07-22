# ADIF-0044 - Parent Execution Ceiling Is Shorter Than Child Timeout

Memory class: POINTER_RECORD

Status: ACTIVE

```text
defectId: ADIF-0044
title: Parent execution ceiling is shorter than child timeout
defectCategory: GATE_TRIGGER_FRICTION
defectClass: RULE_GAP
defectRole: dispatcher
severity: HIGH
lifecycleState: ACTIVE
taskClasses: Work-order authoring / dispatch; Worker execution (`WORKER_MUST_NOT_COMMIT`); Reviewer-return review
roles: dispatcher; worker; reviewer
lifecyclePhases: pre-dispatch; pre-implementation; pre-closure
surfaceSelectors: work orders invoking a bounded local child process whose allowed timeout can exceed the worker tool harness single-command ceiling
detectionSignals: child timeout exceeds parent command ceiling; parent terminates first; stdout and stderr are empty; child diagnostic and exit status are unavailable
enforcementLevel: GUIDANCE_ONLY
checkerBindings: NOT_APPLICABLE_WITH_REASON: repository gates cannot observe every worker tool harness command ceiling
promotionState: MACHINE_CHECK_CANDIDATE
supersedes: NONE
lastVerifiedCommit: 7dbdf3488
roadmapSeedId: NONE
```

## Purpose

Prevent a source-valid long-running local command from being dispatched inside
a shorter opaque worker-tool command window that kills the parent before the
child can complete or emit its own bounded diagnostic.

## Scope / Applies To

Applies when a work order authorizes a local command timeout longer than the
delegated worker's maximum duration for one tool call, especially when the
operation has a no-retry ceiling.

## Bad Example

Authorize a child timeout of 3600 seconds, invoke it synchronously through a
worker tool that terminates commands at about 180 seconds, and depend on the
child's exit code or JSON diagnostic. The parent will terminate first and the
one allowed invocation can be consumed without usable output.

## Good Example

Before dispatch, reconcile the parent and child ceilings. If the parent cannot
wait long enough, start exactly one hidden local process, persist its PID and
output paths, and poll that same PID with short bounded checks. Keep the process
continuously supervised by the same worker, prohibit launching a second PID,
and terminate the exact process tree if supervision cannot continue.

## Canonical Sources

- `scripts/get_cvf_projection_drift_receipt.ps1`, ScanTimeoutSeconds parameter
  and timeout branch.
- `docs/work_orders/CVF_AGENT_WORK_ORDER_CONTINUOUS_PROJECTION_T4_BOUNDED_PILOT_AND_CLOSURE_2026-07-20.md`, Phase B.
- `docs/reviews/CVF_CONTINUOUS_PROJECTION_T4_WORKER_RETURN_2026-07-20.md`, R2 outer-harness interruption diagnosis.
- `docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`, bounded
  failure diagnosis and no-unclear-rerun discipline.

## Remediation

Record both ceilings before invoking the child. A no-retry long-running action
must use either a parent window that exceeds the child ceiling or a supervised
single-process launch-and-poll contract. The contract must persist one PID,
redirect stdout and stderr to disposable paths, use short polls, prevent a
second launch, and define exact-PID teardown if the worker cannot maintain
supervision.

## Epistemic Process Block

### Expected Result / Prediction

A source-valid stdout-only scan with a 3600-second internal timeout should
either produce a receipt or return the script's own structured diagnostic.

### Evidence Comparison

The T4 R2 worker harness terminated the invocation at about 180 seconds with
exit code 143, while the script's 3600-second ceiling had not fired. Redirected
stdout and stderr were both empty, no receipt existed, and no orphaned process
remained.

### Contradiction Or Gap Disposition

The child command contract was valid, but the dispatch did not reconcile it
with the shorter parent execution envelope. A script-level timeout cannot
protect an invocation when its parent always terminates first.

### Claim Update

A repaired dispatch may claim only that one exact local process is launched and
supervised across short polls. It may not claim the scan will complete, and it
must not treat relaunch as polling or recovery.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex reviewer and redispatch author |
| Provider or surface | local private provenance workspace |
| Session or invocation | Continuous Projection T4 R2 blocked-return review, 2026-07-21 |
| Working directory | repository root |
| Command or tool surface | local Git, direct artifact inspection, PowerShell/Python governance gates, apply_patch |
| Target paths | ADIF-0044 entry and entries README row |
| Allowed scope source | operator instruction to fix reviewer findings and record necessary learning; AGENTS.md mandatory ADIF disclosure |
| Before status evidence | R2 consumed one scan invocation when the worker harness terminated before the child timeout or output |
| After status evidence | ADIF-0044 is resolver-discoverable and the entries front door lists it |
| Diff evidence | new entry plus README row in the T4 R3 material redispatch batch |
| Approval boundary | governance learning and dispatch repair only; no scan, provider, CLI/MCP, browser, public-sync, or production action |
| Claim boundary | defect record and bounded prevention guidance only; no generic parent-child timeout checker exists |
| Agent type | reviewer and dispatcher |
| Invocation ID | `continuous-projection-t4-adif-0044-2026-07-21` |
| Expected manifest | ADIF-0044 entry and entries README row within the T4 R3 material redispatch batch |
| Actual changed set | ADIF-0044 entry and entries README row within the T4 R3 material redispatch batch |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance defect intelligence; no public-sync work is
authorized by this entry.

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | reusable parent-child timeout and supervised polling guidance only |
| claimDisposition | CLAIM_REJECTED: no runtime enforcement or universal harness-ceiling detection claim |
| receiptEvidence | `CLAIM_REJECTED_NO_RECEIPT`: R2 produced no child receipt or diagnostic before parent termination |
| actionEvidence | ACTION_EVIDENCE_PRESENT: R2 process, empty-output, and clean-root evidence support this defect record; the reviewer ran no real-root scan |
| invocationBoundary | local documentation, evidence inspection, and governance gates only |
| interceptionBoundary | no provider, CLI/MCP adapter, browser, public, runtime, or production interception |
| claimLanguage | a dispatcher must reconcile the parent command ceiling with the child timeout before releasing a no-retry invocation |
| forbiddenExpansion | no receipt-script edit, generic checker, provider/live call, public-sync, unattended loop, or production mutation |

## Claim Boundary

This entry records one reusable execution-envelope defect and its bounded
prevention rule. It does not alter the receipt script, authorize an agent CLI or
MCP call, authorize unattended execution, or prove a corrected scan will pass.
