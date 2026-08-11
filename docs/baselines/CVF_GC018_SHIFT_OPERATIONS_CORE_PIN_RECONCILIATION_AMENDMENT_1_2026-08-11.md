# GC-018 Baseline - Shift Operations Core Pin Reconciliation Amendment 1

Status: PROPOSED

Memory class: governed-baseline

Date: 2026-08-11

Batch ID: SOPR-CP1-A1

Risk: R2

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: `0b835be3ff1ac1fbd1c95e365471887202d718b5`

## Purpose

Authorize the smallest test-only repair required to make SOPR-CP1 AC-07
deterministic after independent review reproduced the disclosed intermittent
failure outside the original exact-10 boundary.

## Scope / Methodology

Retain the original exact-10 pending diff unchanged except for evidence text in
the worker return. Add exactly one test path, replace the ambiguous final-JWT-
character mutation with a real decoded-signature-byte flip, rerun the isolated
stress and full CVF suite, and return again without staging or committing.

## Findings / Position

The defect is in the negative-signature fixture. It is not evidence that the
runtime accepts a changed signature: the failing token's textual suffix was
different but its decoded signature bytes were identical.

## Risk / Corrective Action

Test-only corrective action. Any production/runtime edit, alternative waiver,
or additional target path is a stop condition.

## Source / Predecessor Evidence

- Parent baseline: `docs/baselines/CVF_GC018_SHIFT_OPERATIONS_CORE_PIN_RECONCILIATION_2026-08-11.md`.
- Parent Work Order: `docs/work_orders/CVF_AGENT_WORK_ORDER_SHIFT_OPERATIONS_CORE_PIN_RECONCILIATION_2026-08-11.md`.
- Reviewer source verification: `docs/reviews/CVF_SHIFT_OPERATIONS_CORE_PIN_RECONCILIATION_AMENDMENT_1_SOURCE_VERIFICATION_2026-08-11.md`.

## Decision / Baseline / Proposed Tranche

Decision: propose exactly one test path plus correction of the existing worker
return; retain all other pending bytes and forbid runtime/product expansion.

## Acceptance Criteria

- AC-A1-01: target HEAD remains exact and original pending exact-10 preimages
  match the Amendment 1 Work Order.
- AC-A1-02: only the test file and existing worker return are written by the
  repair worker; final pending manifest is exact-11.
- AC-A1-03: the fixture flips at least one decoded signature byte and the
  re-encoded token differs from the original.
- AC-A1-04: the isolated authorization file passes ten consecutive fresh
  pytest invocations.
- AC-A1-05: the full `tests/cvf` suite passes twice consecutively.
- AC-A1-06: every original SOPR-CP1 required check still passes; doctor retains
  only the bounded legacy-catalog warning.
- AC-A1-07: worker return removes the false 65-character claim and replaces
  the cross-test/clock hypothesis with the verified base64url fixture cause.
- AC-A1-08: staged zero, worker commit zero, provider/network/live calls zero.

## Stop Conditions

Stop for any preimage/base/status mismatch, a twelfth target path, production
or runtime change, provider/network/live need, hidden-Core mutation, new doctor
warning, or any failure remaining after the exact test/evidence repair.

## Verification Evidence

The paired source-verification review supplies the reproduced failure and
root-cause diagnostic. The repair worker supplies exact diffs, hashes, two full
suite passes, ten isolated passes, original gates, staged-zero and no-commit
evidence. Independent reviewer recomputes all evidence.

## External Knowledge Intake Routing

Canonical chain map:
`docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`.

| Field | Value |
|---|---|
| Chain map | canonical chain map above |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | `BLOCKED_UNTIL_CVF_PROOF`; no runtime claim admitted |
| Matching local-view guard | `governance/compat/check_delta_execution_claim_boundary.py` |
| Owner surface | Amendment 1 baseline |
| Disposition | `NOT_APPLICABLE_WITH_REASON` |
| Claim boundary | no external input admitted as CVF authority |

## Corpus Completeness And Report Integrity

Corpus task class: N/A with reason - not a corpus task.
Corpus root: N/A with reason - none.
Snapshot time: 2026-08-11 dispatch.
Enumeration command: named-file reads only.
Manifest artifact or inline manifest: Amendment exact target manifest.
Manifest hash: N/A with reason - no corpus manifest.
Processing ledger artifact or inline ledger: paired source verification.
Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
Reconciliation: N/A with reason - no corpus totals.
Unresolved files: none.
Declared exclusions: all unnamed paths.
Unreadable or unsupported files: none.
Aggregation check: N/A with reason - no aggregation.
Drift check: exact hashes required.
Output traceability: baseline to Work Order amendment.
Adversarial verification: decoded-byte diagnostic.
- Corpus verdict: NOT_APPLICABLE_WITH_REASON - this baseline is not a corpus report.

## Finding-To-Governance Learning Disposition

| Field | Value |
|---|---|
| defectClass | `WORKER_EXECUTION_ERROR` |
| lane | `GOVERNANCE_CONTROL_PLANE` |
| disposition | `RULE_EXISTS` |
| owner | repair worker and independent reviewer |

## Epistemic Process Block

The accepted claim is limited to the deterministic base64url diagnostic and
test-fixture repair. Runtime security remains governed by existing tests and
source; this baseline adds no production claim.

## Machine Closure Package

NOT_APPLICABLE_WITH_REASON: this is a repair baseline pending worker and
independent reviewer evidence.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | baseline structure; ADIF; corpus; external routing; Delta tokens |
| gateRunPurpose | confirmation of proposed repair baseline |
| claimBoundary | test/evidence repair baseline only |

## ADIF Defect Registry Disclosure

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch`.

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Returned defectIds: `ADIF-0001`, `ADIF-0002`, `ADIF-0014`, `ADIF-0015`,
`ADIF-0020`, `ADIF-0021`, `ADIF-0028`, `ADIF-0029`, `ADIF-0033`, `ADIF-0044`.

Dispatch impact: exact manifest/hash verification, provider-memory exclusion,
checker read-ahead, protected-path avoidance, and bounded command timeouts.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | orchestrator/reviewer |
| Provider or surface | private Core authority authoring |
| Session or invocation | `sopr-cp1-a1-baseline-20260811` |
| Working directory | private Core root |
| Command or tool surface | local files, Git, checkers |
| Target paths | paired Amendment 1 authority packet |
| Allowed scope source | operator delegated decision authority |
| Before status evidence | SOPR-CP1 review blocked on AC-07 |
| After status evidence | test-only repair baseline proposed |
| Diff evidence | Core pre-dispatch gate |
| Approval boundary | exact test/evidence repair only |
| Claim boundary | no runtime/product expansion |
| Agent type | orchestrator/reviewer |
| Invocation ID | `sopr-cp1-a1-baseline-20260811` |
| Expected manifest | source review, baseline, Work Order amendment |
| Actual changed set | resolved by pre-dispatch gate |
| Manifest delta | MATCH required |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | deterministic test fixture repair |
| claimDisposition | CLAIM_REJECTED: no runtime-control claim |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT; local tests only |
| actionEvidence | CLAIM_REJECTED_NO_ACTION; no external action |
| invocationBoundary | local pytest/checker commands |
| interceptionBoundary | no interception or proxy claim |
| claimLanguage | test reliability only |
| forbiddenExpansion | production/runtime/provider/live/public/deploy/push |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private repair authority only.

## Claim Boundary

This baseline does not accept SOPR-CP1, waive AC-07, or authorize any product,
runtime, provider, public-sync, push, deployment or production change.
