# CVF MAO-T7 Evidence, Observability, And Operator Readout Completion Review

Memory class: FULL_RECORD

docType: review

Status: REVIEWER_ACCEPTED_BOUNDED

Date: 2026-07-11

Responds to work order: `CVF_AGENT_WORK_ORDER_MAO_T7_EVIDENCE_OBSERVABILITY_AND_OPERATOR_READOUT_2026-07-11.md`

## Purpose

Record independent review and bounded acceptance of MAO-T7.

## Target / Source

T7 baseline/work order, worker outputs, current MAO receipt contracts, workspace
projection authority, and focused tests.

## Scope / Methodology

Reviewer read source/tests, independently ran Vitest/typecheck, checked the
single-graph ledger invariant, repaired cross-graph admission, added GC-051
coverage, and ran reviewer gates.

## Findings / Position

ACCEPT_BOUNDED. The worker implementation passed its focused suite, but the
ledger accepted evidence whose `taskGraphId` differed from the graph bound in
its constructor. Reviewer added fail-closed `TASK_GRAPH_ID_MISMATCH` handling
and a negative test. Final focused suite passes 35/35.

## Risk / Corrective Action

Redaction is a denylisted-field-name boundary, not a content DLP scanner.
Callers must not place unknown secret values under benign field names. This
tranche proves deterministic local in-memory mechanics only; it does not prove
durable storage, real providers, production observability, or a workspace UI.

## Verification

- focused Vitest: 35/35 PASS;
- TypeScript typecheck: PASS;
- cross-graph admission negative: PASS;
- GC-051 aggregate: regenerated and aligned.

## Epistemic Process Block

### Expected Result / Prediction

The graph-bound ledger rejects evidence from any other task graph.

### Evidence Comparison

Initial source contradicted that invariant even though 34/34 worker tests passed.

### Contradiction Or Gap Disposition

Repair cross-graph admission and add a negative test.

### Claim Update

Bounded deterministic local evidence/readout mechanics accepted; secret-safety
claim is calibrated to explicit denylisted-field redaction.

## Closure Diff Gate

| Requirement | Result |
|---|---|
| deterministic ledger/readout | PASS |
| graph-bound admission | PASS after reviewer repair |
| retention/freshness classification | PASS |
| milestone-only workspace projection | PASS |
| five worker outputs/no worker commit | PASS |
| durable/provider/UI claim | N/A with reason: outside T7 boundary |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_machine_closure_package.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_corpus_scan_registry.py` |
| literalTokensReviewed | closure rows, trace labels, public disposition, registry entry |
| gateRunPurpose | closure confirmation |
| claimBoundary | local T7 only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | reviewer/closer |
| Provider or surface | private workspace |
| Session or invocation | MAO-T7 closure 2026-07-11 |
| Working directory | repository root/package |
| Command or tool surface | review, patch, Vitest, tsc, generators, gates |
| Target paths | T7 material and reviewer closure paths |
| Allowed scope source | Reviewer Closure Conversion |
| Before status evidence | five uncommitted worker outputs |
| After status evidence | accepted repaired material |
| Diff evidence | `git diff --name-status` |
| Approval boundary | T7 only |
| Claim boundary | no durable runtime/provider/UI claim |
| Agent type | reviewer/closer |
| Invocation ID | `mao-t7-closure-2026-07-11` |
| Expected manifest | worker five plus baseline/work order/review/registry source/aggregate |
| Actual changed set | same |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

Deterministic local evidence, operator readout, retention/freshness, and
milestone projection mechanics only.
