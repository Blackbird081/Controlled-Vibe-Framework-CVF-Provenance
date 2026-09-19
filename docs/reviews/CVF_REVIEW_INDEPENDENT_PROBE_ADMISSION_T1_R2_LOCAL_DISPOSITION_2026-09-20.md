# CVF Review - Independent Probe Admission T1 R2 Local Disposition

Memory class: FULL_RECORD

docType: review

Status: BLOCKED_WITH_REASON

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_REVIEW_INDEPENDENT_PROBE_ADMISSION_T1_2026-09-19.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_REVIEW_INDEPENDENT_PROBE_ADMISSION_T1_2026-09-19.md`

independentProbeDisposition: FAIL_INDEPENDENT_PROBE

Date: 2026-09-20

## Purpose

Decide whether the R2 worker return closes the independent-probe admission
claim and select the governed successor when it does not.

## Source / Target

Local reviewed the no-commit R2 worker return and its seven-path implementation
at execution base `672e41cda`. The review evaluates returned evidence and adds
independently authored hostile inputs; it does not recreate the worker suite.

## Scope / Methodology

Local confirmed the return shape, ran the focused 68-test suite, invoked the
new checker directly, inspected the parser and linkage code, and exercised
unseen variants through direct `diagnose_closure` calls and temporary-repository
fixtures. No provider, Party A, live source, public-sync or runtime action ran.

## Findings / Position

The R2 return is `REWORK_REQUIRED_ROOT_CONTRACT`; it is not accepted.

| ID | Independent hostile input | Observed result | Required result |
| --- | --- | --- | --- |
| RIPA-ROOT-01 | terminal `Status:` exists only inside a tilde fence | `clean=True` | reject; fenced examples never count |
| RIPA-ROOT-02 | `probeEvidenceRef` is `https://example.invalid/probe.json` | `clean=True` | reject; evidence refs are canonical repo-relative paths |
| RIPA-ROOT-03 | two identical `Responds to work order` declarations | `clean=True` | reject duplicate cardinality before value comparison |
| RIPA-ROOT-04 | referenced work order contains `independentProbeRequired: YES` plus an empty duplicate | `clean=True` | fail closed on duplicate/empty declaration |
| RIPA-ROOT-05 | PASS actor is `Claude implementation worker` | `clean=True` | reject an explicitly worker-owned probe actor |

The worker's focused suite passed 68/68, and its own pending return diagnoses
cleanly. Those facts are useful corroboration but do not overcome the five
independent counterexamples. The direct gate also reports three pre-existing
parked artifacts whose referenced work orders predate the new required field;
that integration consequence remains parked and must be addressed explicitly
by the integrated successor rather than silently excluded.

## Risk / Corrective Action

The recurring cause is duplicated ad hoc Markdown parsing and local validation:
fence masking, declaration cardinality, link resolution, actor identity and
path canonicalization do not share one typed contract. A third narrow regex
repair is prohibited. The successor must implement one reusable declaration
scanner and typed validators, migrate the admission checker to them, bind
evidence digests to existing referenced bytes, and encode the full equivalence
classes as parameterized hostile tests.

## Decision / Disposition

`REJECT_R2_AND_OPEN_INTEGRATED_ROOT_CONTRACT`.

The R2 implementation stays uncommitted for successor repair. This is a new
integrated-root-contract batch, not automatic R3 redispatch. Local remains the
reviewer, probe executor, disposition owner and committer.

## Return-Time Closeability Recheck

| Surface | Result |
| --- | --- |
| worker return shape | PASS |
| focused worker tests | PASS 68/68 |
| independent hostile probe | FAIL, five counterexamples |
| worker-return fast gate | BLOCKED by three disclosed parked-artifact findings |
| closure | BLOCKED_ROOT_CONTRACT_REQUIRED |

## Finding-To-Governance Learning Disposition

| Field | Value |
| --- | --- |
| Defect class | MACHINE_GATE_GAP |
| Learning lane | PROMOTE_TO_INTEGRATED_ROOT_CONTRACT |
| Finding | repeated parser and evidence-binding bypasses survived two bounded correction rounds |
| Disposition | ROOT_CONTRACT_REQUIRED |
| Runtime/provider/cost lane | N/A with reason: repository governance parser only |
| Next control action | dispatch the integrated parser/binding contract successor |

## Epistemic Process Block

- Epistemic Process Applicability: HIGH_EVIDENCE
- Expected result / prediction: R2 should reject all declared fence, cardinality, actor and path variants.
- Evidence Comparison: five unseen variants were accepted unexpectedly.
- Contradiction or gap disposition: invalidate the R2 closure claim and escalate the same problem chain.
- Claim update: focused regression success is narrowed to the encoded fixtures only.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Local orchestrator/reviewer |
| Provider or surface | private CVF workspace |
| Session or invocation | RIPA-T1-R2 independent Local review, 2026-09-20 |
| Working directory | repository root |
| Command or tool surface | git status, unittest, checker CLI, source inspection, direct Python hostile probes |
| Target paths | returned seven-path implementation and this disposition |
| Allowed scope source | active handoff and RIPA-T1 R2 work order |
| Before status evidence | HEAD `672e41cda`; worker changes uncommitted |
| After status evidence | worker changes remain uncommitted; no parked path edited |
| Diff evidence | `git status --short`; direct probe outputs recorded above |
| Approval boundary | Local semantic review and integrated-root selection only |
| Claim boundary | no implementation acceptance or runtime/live/public claim |
| Agent type | reviewer/closer |
| Invocation ID | `ripa-t1-r2-local-probe-20260920` |
| Expected manifest | this Local disposition only |
| Actual changed set | this Local disposition only |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | independent review and architecture escalation |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT: five direct hostile-probe observations |
| invocationBoundary | local read-only review commands and this review artifact |
| interceptionBoundary | no universal agent/tool interception claim |
| claimLanguage | R2 rejected; integrated root contract required |
| forbiddenExpansion | Party A, source creation, provider/live/public/runtime actions |

## External Knowledge Intake Routing

NOT_APPLICABLE_WITH_REASON: internal Local review of private repository work.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private governance review evidence.

## Claim Boundary

This disposition proves five concrete counterexamples against the returned
checker. It does not claim the selected successor is implemented or accepted.
