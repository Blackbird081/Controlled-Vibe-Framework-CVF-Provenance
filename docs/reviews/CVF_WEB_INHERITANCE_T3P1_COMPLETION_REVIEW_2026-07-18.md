# CVF Web Inheritance T3P1 Completion Review

Memory class: FULL_RECORD

Status: REVIEWER_ACCEPTED_WITH_REPAIR

docType: completion_review

Review-Cost Telemetry: REQUIRED

Date: 2026-07-18

Review ID: CVF-WEB-INHERITANCE-T3P1-COMPLETION-REVIEW

## Purpose

Independently review and close the T3P1 read-only durable run-discovery
prerequisite before any evidence/liveness or Web implementation is released.

Responds to work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_WEB_INHERITANCE_T3P1_MAO_DURABLE_RUN_DISCOVERY_PREREQUISITE_2026-07-18.md`.

executionBaseHead: `233940c5b`

## Target / Source

The reviewed target is `MaoFileRunStore.listRunIds`, its typed package export,
focused real-filesystem tests, and the no-commit worker return.

## Scope / Methodology

The reviewer inspected candidate filtering, identity binding, reuse of full
replay validation, failure propagation, purity, package-root exports, and the
exact five-path worker boundary. Focused tests, the complete execution-plane
suite, TypeScript, governed gates, and file-size enforcement were recomputed.

## Findings / Position

The final method returns an empty list without creating a missing root,
considers only canonical regular snapshot entries, verifies filename-to-ID
hash binding, reuses `loadAndReplay` for full trust, returns no partial result
on failure, and sorts unique IDs deterministically. Discovery contains no
write path.

The result type is available through the local MAO barrel and package root.
T3P1 closes run discovery only; it does not supply durable evidence or
restart-safe heartbeat state and does not release T3B.

## Independent Evidence

| Evidence | Recomputed result | Verdict |
|---|---|---|
| Worker boundary | exact five allowed paths; nothing staged; HEAD `233940c5b` | PASS |
| Missing root | empty success and root remains absent | PASS |
| Candidate boundary | canonical regular files only; symlinks not followed | PASS_WITH_REPAIR |
| Validation | hash binding plus existing full replay owner | PASS |
| Failure contract | invalid canonical candidate fails whole call | PASS |
| Purity | repeated results, entry names, bytes, and mtime unchanged | PASS |
| Focused tests | 2 files, 32 tests passed | PASS |
| Full package tests | 70 files, 1790 tests passed | PASS |
| TypeScript | `npm run check` passed | PASS |
| Governed gates and file size | reviewer-fast and enforcement passed after repair | PASS |

## Risk / Corrective Action

The reviewer found one real path-boundary defect. The worker used `stat()` to
classify canonical-looking entries; `stat()` follows symbolic links, allowing
a canonical-named link to target a file outside the caller-supplied store
root. The reviewer changed enumeration to
`readdir(root, { withFileTypes: true })` and filters with
`Dirent.isFile()`, which classifies the entry without following links.

The ignored-entry regression now includes a canonical directory and a file
symlink where platform permissions allow creation. Focused tests, the full
suite, and TypeScript all pass after the repair. No API, failure enum, Web,
evidence, liveness, provider, or mutation scope expanded.

## Closure Diff Gate

| Requirement source | Required result | Final evidence | Verdict |
|---|---|---|---|
| Roadmap T3P1 | deterministic read-only discovery | final source and focused tests | PASS |
| Work order AC-01 | non-creating missing-root result | focused test | PASS |
| Work order AC-02 through AC-04 | ordering, trust, failures, hash binding | focused matrix | PASS |
| Work order AC-05 | repeated purity | entries, bytes, and mtime assertions | PASS |
| Work order AC-06 | package-root availability | root-export test and TypeScript | PASS |
| Work order AC-07 and AC-08 | all gates and exact no-commit boundary | command and git evidence | PASS |

## Disposition

`REVIEWER_ACCEPTED_WITH_REPAIR`.

CVF-WEB-INHERITANCE-T3P1 is closed. The next allowed material move is a
source-verified T3P2 decision packet for durable evidence and restart-safe
heartbeat availability. T3B and T4-T5 remain parked.

## Closure Checklist

- [x] execution HEAD and five-path worker boundary match dispatch.
- [x] missing-root, ordering, failure, validation, and purity contracts pass.
- [x] symlink-following risk is removed from candidate classification.
- [x] local and package-root exports compile.
- [x] focused tests, full tests, TypeScript, gates, and file-size pass.
- [x] worker no-commit boundary was honored.
- [x] no Web, evidence/liveness persistence, provider, or external mutation occurred.
- [x] protected continuity remains a separate sync batch.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | T3P1 baseline | `Status: CLOSED_PASS_WITH_REVIEWER_REPAIR` | PASS |
| Work order status | T3P1 work order | `Status: CLOSED_PASS_WITH_REVIEWER_REPAIR` | PASS |
| Completion or reviewer artifact | this file | `Status: REVIEWER_ACCEPTED_WITH_REPAIR` | PASS |
| Worker return | T3P1 worker return | `Status: ACCEPTED_BY_REVIEWER_WITH_REPAIRS` | PASS |
| Roadmap state | CVF Web inheritance roadmap | `Status: CVF_WEB_INHERITANCE_T3P1_PASS_T3P2_PACKET_AUTHORING_NEXT` | PASS |
| Registry JSON | corpus registry generated aggregate | existing execution-plane source/test scope coverage; drift check passed | PASS |
| Registry Markdown | corpus registry read model | existing execution-plane source/test scope coverage | PASS |
| External evidence digest | N/A with reason: repository-local source and tests | none | N/A with reason |
| System loop interlock | N/A with reason: no loop owner changed | none | N/A with reason |
| Session continuity | protected session surfaces | separate session-sync commit follows | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| Runtime receipt evidence | N/A with reason: read-only enumeration creates no receipt | N/A_WITH_REASON |
| Query acceptance evidence | focused real-filesystem discovery matrix 32/32 | PASS |
| Worker-return acceptance | exact five paths, unchanged HEAD, no staging, gates passed | PASS |
| Closure claim | read-only discovery accepted after symlink-boundary repair | PASS |

## Review Cost Telemetry And Stop Disposition

reviewRoundCount: 1

workerRepairTurnCount: 0

newRootCauseCountThisRound: 1

dependentFindingCountThisRound: 1

providerCallCount: 0

elapsedReviewMinutes: NOT_AVAILABLE_WITH_REASON: governed wall-clock telemetry is not exposed

tokenOrQuotaUsage: NOT_AVAILABLE_WITH_REASON: provider-neutral accounting is not exposed

valueDelta: Removed one root-boundary escape while retaining the narrow pure
discovery contract and complete test evidence.

stopDisposition: COMPLETE_REVIEW

## Epistemic Process Block

### Expected Result / Prediction

The worker implementation should provide deterministic discovery by reusing
the existing replay owner without adding a write path.

### Evidence Comparison

The prediction held for result and validation semantics, but direct source
review found `stat()` followed symbolic links and weakened root containment.

### Contradiction Or Gap Disposition

The entry-classification contradiction was repaired and regression-covered.
No remaining source or test contradiction blocks closure.

### Claim Update

T3P1 now proves read-only discovery of canonical regular snapshot entries. It
does not prove durable evidence, heartbeat reconstruction, or a Web caller.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Status; completion_review; Closure Diff Gate; Machine Closure Package; Acceptance Receipt Assertion Matrix; Agent Operation Trace Block; Public Export Disposition; Claim Boundary |
| gateRunPurpose | independent reviewer closure evidence |
| claimBoundary | checker conformance supplements source, test, and path-boundary review |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | CVF independent reviewer/closer |
| Provider or surface | local private provenance workspace |
| Session or invocation | CVF-WEB-INHERITANCE-T3P1 review closure, 2026-07-18 |
| Working directory | repository root and execution-plane package root |
| Command or tool surface | source review, diff inspection, focused/full tests, TypeScript, governance gates, commit stewardship |
| Target paths | four source/test paths; worker return; baseline; work order; roadmap; this review |
| Allowed scope source | T3P1 Reviewer Closure Conversion |
| Before status evidence | HEAD `233940c5b`; exact five-path worker return set |
| After status evidence | exact nine-path material closure set pending commit |
| Diff evidence | bounded source/test/docs diff and independent commands |
| Approval boundary | T3P1 closure and T3P2 packet authoring next |
| Claim boundary | no Web, evidence/liveness persistence, provider/live, public, push, or production mutation |
| Agent type | independent reviewer/closer |
| Invocation ID | `cvf-web-inheritance-t3p1-independent-review-closure-2026-07-18` |
| Expected manifest | four source/test paths; worker return; baseline; work order; roadmap; this review |
| Actual changed set | exact nine-path closure set before commit |
| Manifest delta | MATCH after verification |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance review closure; no public-sync authorization.

## Claim Boundary

This review accepts only T3P1 read-only discovery after one bounded repair.
It authorizes T3P2 packet authoring only, not T3P2 execution, T3B, Web changes,
evidence/heartbeat persistence, provider/live, public, push, release, or
production mutation.
