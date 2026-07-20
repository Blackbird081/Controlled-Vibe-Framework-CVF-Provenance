# ADIF-0043 - Output Path Contract Ignores Process Working Directory

Memory class: POINTER_RECORD

Status: ACTIVE

```text
defectId: ADIF-0043
title: Output path contract ignores process working directory
defectCategory: SOURCE_FIDELITY
defectClass: RULE_GAP
defectRole: dispatcher
severity: MEDIUM
lifecycleState: ACTIVE
taskClasses: Work-order authoring / dispatch; Worker execution (`WORKER_MUST_NOT_COMMIT`); Reviewer-return review
roles: dispatcher; worker; reviewer
lifecyclePhases: pre-dispatch; pre-implementation; pre-closure
surfaceSelectors: work orders invoking local scripts whose output path must be contained by process current working directory while excluded from read-only target roots
detectionSignals: prescribed output path is outside process current working directory; command changes no working directory; script rejects with PATH_ESCAPE before its intended read-only operation
enforcementLevel: GUIDANCE_ONLY
checkerBindings: NOT_APPLICABLE_WITH_REASON: current source-verification gates confirm parameter existence but do not reconcile process CWD, output containment, and excluded-root constraints
promotionState: MACHINE_CHECK_CANDIDATE
supersedes: NONE
lastVerifiedCommit: 5b929dad9
roadmapSeedId: NONE
```

## Purpose

Prevent a source-verified work order from prescribing an invocation that is
syntactically valid but impossible under the called script's current-working-
directory and excluded-root constraints.

## Scope / Applies To

Applies when a work order supplies an output path to a local script or CLI and
the implementation checks containment relative to process CWD in addition to
checking that the output remains outside one or more protected roots.

## Bad Example

Run from a protected repository root, require output outside that root, and
also call a script that requires the output to be contained under process CWD.
Merely verifying that the output parameter exists misses the contradiction.

## Good Example

Source-verify every path predicate. Prefer the script's documented stdout-only
mode when a persistent script-owned output is unnecessary. Otherwise choose a
common parent working directory that contains both protected roots and a
disposable sibling output directory, resolve every input to an absolute path,
and record the working directory explicitly in the dispatched command.

## Canonical Sources

- `scripts/get_cvf_projection_drift_receipt.ps1`, ReceiptOutputPath parameter
  documentation and lines 612-619 containment branch.
- `docs/work_orders/CVF_AGENT_WORK_ORDER_CONTINUOUS_PROJECTION_T4_BOUNDED_PILOT_AND_CLOSURE_2026-07-20.md`, Phase B.
- `docs/reviews/CVF_CONTINUOUS_PROJECTION_T4_WORKER_RETURN_2026-07-20.md`, R1 PATH_ESCAPE diagnosis.
- `docs/reference/guard_orientation/README.md`, Work-order authoring / dispatch.

## Remediation

Before dispatch, model the conjunction of process CWD containment and every
excluded-root predicate. Omit the optional output path and capture stdout when
the source contract supports that safer route. If a file path is required,
the command must name its working directory and use absolute input paths. A
no-retry operation must receive a preflight path proof before its one allowed
invocation is released.

## Epistemic Process Block

### Expected Result / Prediction

A source-verified real-root receipt command with an outside-root temporary
path should reach the read-only scan.

### Evidence Comparison

The T4 R1 command ran from the provenance root and supplied a `%TEMP%` receipt
path. The accepted script rejected that path in 0.35 seconds because it was
not contained by process CWD; no receipt or scan result was produced.

### Contradiction Or Gap Disposition

Parameter existence is insufficient source verification for a path-bearing
invocation. All path predicates and process-location assumptions must be
reconciled before dispatch.

### Claim Update

The repaired command may claim only that its chosen working directory and
receipt path satisfy the directly inspected containment predicates. It does
not claim that the later scan will succeed.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex reviewer and redispatch author |
| Provider or surface | local private provenance workspace |
| Session or invocation | Continuous Projection T4 R1 blocked-return review, 2026-07-21 |
| Working directory | repository root |
| Command or tool surface | local Git, PowerShell/Python gates, direct source inspection, apply_patch |
| Target paths | ADIF-0043 entry and entries README row |
| Allowed scope source | operator instruction to fix reviewer findings and record necessary learning; AGENTS.md mandatory ADIF disclosure |
| Before status evidence | R1 consumed its one invocation on PATH_ESCAPE before the read-only scan because dispatch omitted the script's CWD predicate |
| After status evidence | ADIF-0043 is resolver-discoverable and the entries front door lists it |
| Diff evidence | new entry plus README row in the T4 R2 material redispatch batch |
| Approval boundary | governance learning and dispatch repair only; no script/runtime, provider, CLI/MCP, browser, public-sync, or production change |
| Claim boundary | defect record and bounded prevention guidance only; no generic path-contract checker exists |
| Agent type | reviewer and dispatcher |
| Invocation ID | `continuous-projection-t4-adif-0043-2026-07-21` |
| Expected manifest | ADIF-0043 entry and entries README row within the T4 R2 material redispatch batch |
| Actual changed set | ADIF-0043 entry and entries README row within the T4 R2 material redispatch batch |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance defect intelligence; no public-sync work is
authorized by this entry.

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | reusable path-contract and dispatch guidance only |
| claimDisposition | CLAIM_REJECTED: no runtime enforcement or automatic path-proof claim |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: R1 blocked worker return records PATH_ESCAPE and zero receipt output |
| actionEvidence | ACTION_EVIDENCE_PRESENT: direct source inspection supports the defect record; no real-root scan was run by the reviewer |
| invocationBoundary | local documentation, source inspection, and governance gates only |
| interceptionBoundary | no provider, CLI/MCP adapter, browser, public, runtime, or production interception |
| claimLanguage | dispatch must reconcile process CWD containment with every excluded-root predicate before a no-retry invocation |
| forbiddenExpansion | no script edit, generic checker, provider/live call, public-sync, or production mutation |

## Claim Boundary

This entry records one non-obvious, reusable dispatch defect and its bounded
prevention rule. It does not implement a checker, alter the receipt script,
authorize retry, or prove that a corrected real-root scan will succeed.
