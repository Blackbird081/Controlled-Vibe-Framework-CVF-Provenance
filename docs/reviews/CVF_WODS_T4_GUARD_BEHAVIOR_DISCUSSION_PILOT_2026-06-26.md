# CVF WODS-T4 Guard Behavior Discussion Pilot

Memory class: FULL_RECORD

Status: COMPLETE_PENDING_REVIEW

docType: review

## Purpose

Pilot a narrow shared discussion-section parser for the two guards with
confirmed marker-prose self-trigger evidence.

## Target / Source

Target guards: `governance/compat/check_delta_execution_claim_boundary.py`
and `governance/compat/check_rescan_intelligence_hardening.py`.

## Scope / Methodology

The pilot adds one shared parser and applies it only to Delta execution-claim
and intake-analysis applicability scans. Focused tests verify marked discussion prose is
ignored for applicability while unmarked prose remains checked.

## Findings / Position

The shared `## Guard Behavior Discussion` section requires the exact
`Discussion-only disposition: META_DISCUSSION_ONLY` marker. Only this marked
section is removed before applicability detection; field validation still runs
when a real guard section or path marker applies.

## Risk / Corrective Action

Risk: a broad exclusion could hide a true claim. Corrective action: this pilot
is limited to two proven guards and retains their path markers, explicit
required markers, and all post-applicability validation. Wider adoption needs
separate evidence.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: implement and test a bounded common
discussion-section parser for the intake-analysis and Delta applicability scans only.

Protected paths:

- `governance/compat/check_delta_execution_claim_boundary.py`
- `governance/compat/check_rescan_intelligence_hardening.py`
- `governance/compat/guard_behavior_discussion.py`
- `governance/compat/test_check_delta_execution_claim_boundary.py`
- `governance/compat/test_check_rescan_intelligence_hardening.py`

Operator authorization: the operator selected WODS-T4 after WODS-T3 documented
the fourth recurring marker-prose authoring cycle.

Rollback boundary: revert only this pilot and its matching session sync; do
not revert WODS-T1 through WODS-T3.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| Marker prose can self-trigger multiple full-text guards | PHASE_GATE_PLACEMENT_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | pilot only two confirmed guards |

Runtime/provider/cost learning lane: N/A_WITH_REASON - local guard parsing only.

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: this pilot changes guard applicability parsing; it does not rescan or
refresh an intake source.

## Epistemic Process Block

Expected Result: marked discussion prose no longer creates applicability false positives.

Evidence Comparison: focused tests cover marked and unmarked prose cases.

Contradiction Or Gap Disposition: no global adoption claim is made.

Claim Update: pilot remains bounded to two guards.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | WODS-T4 local guard parsing pilot |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT - focused test results |
| actionEvidence | ACTION_EVIDENCE_PRESENT - guarded source and test diff |
| invocationBoundary | local repository checker code only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, Web runtime, or adapter interception claim |
| claimLanguage | two-guard applicability pilot only |
| forbiddenExpansion | package, runtime, provider/live, public-sync, push, session-sync, and ASSF-PIC-T4 remain out of scope |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private governance guard pilot.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex multi-role implementation/review |
| Provider or surface | local workspace |
| Session or invocation | WODS-T4 pilot, 2026-06-26 |
| Working directory | repository root |
| Command or tool surface | apply_patch, pytest, direct guards |
| Target paths | five protected pilot paths and this review |
| Allowed scope source | operator WODS-T4 authorization |
| Before status evidence | WODS-T3 `IMPROVED_WITH_NEW_FINDING` |
| After status evidence | focused tests pass before closure |
| Diff evidence | `git diff --name-status` |
| Approval boundary | two guard pilot only |
| Claim boundary | no global exclusion or runtime claim |
| Agent type | implementer/reviewer |
| Invocation ID | `wods-t4-guard-discussion-pilot-2026-06-26` |
| Expected manifest | five protected pilot paths; this review |
| Actual changed set | five protected pilot paths; this review |
| Manifest delta | MATCH |

## Claim Boundary

This record authorizes only a two-guard authoring-friction pilot. It does not
authorize ASSF-PIC-T4, package work, runtime behavior, provider/live proof,
public-sync, or push.
