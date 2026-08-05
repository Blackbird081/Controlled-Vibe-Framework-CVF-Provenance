# ADIF-0026 - Sequential Reviewer Finding Cascade

Memory class: POINTER_RECORD

Status: ACTIVE

```text
defectId: ADIF-0026
title: Sequential reviewer finding cascade
defectCategory: GATE_TRIGGER_FRICTION
defectClass: RULE_GAP
defectRole: NOT_APPLICABLE_WITH_REASON: general reviewer method defect, not one worker finding row
severity: HIGH
lifecycleState: ACTIVE
taskClasses: Reviewer-return review; Closure
roles: dispatcher; reviewer; closer
lifecyclePhases: pre-implementation; pre-closure
surfaceSelectors: documentation contracts, schemas, authority chains, receipts, hash profiles, worker returns, completion reviews, operator-escalation routing
detectionSignals: predictable downstream findings are discovered one repair round at a time; repeated worker turns or repeated operator-confirmation requests consume quota and time without a new source event, independent root cause, changed objective, changed path class, or increased risk
enforcementLevel: PARTIAL_CHECK
checkerBindings: governance/compat/check_review_cost_control.py
promotionState: CHECKER_EXISTS
supersedes: NONE
lastVerifiedCommit: af1853cf4
roadmapSeedId: NONE
```

## Purpose

Prevent local, sequential review of one connected dependency graph. The defect
creates avoidable repair rounds, quota cost, latency, and operator overhead.
It also prevents an agent from converting one operator instruction to continue
or finish a bounded task into a self-invented one-repair-turn authorization.

## Scope / Applies To

Applies to contract, schema, receipt, hash, interface, and multi-record
authority-chain reviews. Implementation-only choices must be deferred with
reason rather than converted into later contract findings.

## Bad Example

> Vocabulary, state, receipt fields, authority links, and hash canonicalization
> are checked in separate rounds although all belong to the original graph.
> After each dependent finding in the same acceptance item, the agent asks the
> operator to authorize another correction even though objective, paths, risk,
> external effects, and commit ownership have not changed.

## Good Example

> Before the first repair, the reviewer builds one record/edge matrix covering
> ownership, state, identity, integrity, cross-record equality, missing/empty
> behavior, negative cases, and reproducibility; all blockers return together.
> When the operator says to continue or finish after an escalation, the agent
> retains that authority for dependent same-scope corrections until acceptance
> or a real authority boundary changes.

## Canonical Sources

- `docs/reference/guard_orientation/README.md` (reviewer-return guidance)
- `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` (learning closure rule)
- `docs/reference/CVF_VALUE_PARKED_LANE_REOPEN_DISCIPLINE_STANDARD_2026-06-25.md` (low-value parking)
- `docs/reviews/CVF_SOT3_T2_COMPLETION_REVIEW_2026-07-12.md` (sequential-review evidence)
- `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md` (same-scope authority continuity)
- `docs/reviews/CVF_GOVERNANCE_LATENCY_WS2_T1_COMPLETION_2026-08-05.md` (repeated micro-checkpoint evidence and final bounded closure)

## Remediation

Before the first repair return, trace every record, field, and edge and classify
issues as `CONTRACT_BLOCKING` or `DEFER_TO_IMPLEMENTATION_WITH_REASON`. If the
matrix is incomplete, use `BLOCKED_REVIEW_MATRIX_INCOMPLETE`.

After the first repair, record these provider-neutral signals:

| Signal | Meaning |
|---|---|
| `reviewRoundCount` | reviewer dispositions on the same tranche |
| `workerRepairTurnCount` | worker turns used only for repair |
| `newRootCauseCountThisRound` | independent new root causes |
| `dependentFindingCountThisRound` | findings derived from a known graph |
| `elapsedReviewMinutes` | wall time or `NOT_AVAILABLE_WITH_REASON` |
| `providerCallCount` | live/provider calls consumed |
| `tokenOrQuotaUsage` | exact usage when exposed, else `NOT_AVAILABLE_WITH_REASON` |
| `valueDelta` | newly closed authority, fail-open, value, or AC gap |

Mandatory stop control:

1. Before round two, complete root-cause consolidation and the full matrix.
2. At round three set `REVIEW_COST_ESCALATION_REQUIRED`; continue only for a
   newly evidenced critical authority/fail-open/integrity contradiction or an
   operator-authorized scope change.
3. Two rounds with no independent root cause and only dependent findings stop
   micro-repair; consolidate once or defer implementation detail.
4. A branch closing no authority boundary, fail-closed invariant, source-value
   conversion, or AC is `LOW_INCREMENTAL_VALUE` and is parked with a concrete
   reopen condition.
5. Stop control never waives a critical defect; it changes the route to one
   consolidated repair, blocked review, or operator checkpoint.

Single-pass latency control added after Continuous Projection T1:

1. Finish semantic inspection and the contract/schema/path/authority/test/
   range/commit-plan matrix before the first material commit.
2. For bounded local reviews with no long-running or external dependency, use
   10 elapsed minutes as the fast-path target and disclose any overrun.
3. Default to one material commit and at most one continuity commit.
4. Classify sequential finding, premature commit, range recomputation, gate
   discovery, and worktree churn as avoidable delay rather than normal review
   cost.
5. The checker enforces declaration shape and controlled vocabulary; semantic
   audit completeness and fast-path eligibility remain reviewer judgment.

Same-scope authority continuity added after Governance Latency WS2-T1:

1. Do not infer a one-repair-turn cap from an operator instruction such as
   continue, handle, or finish unless the operator or controlling packet states
   that cap explicitly.
2. Once the operator clears a round-three escalation, the authority remains
   valid for consolidated dependent repairs while objective, allowed path and
   artifact classes, risk ceiling, external-effect class, and commit owner stay
   unchanged.
3. A reviewer that narrows an already-open acceptance item to another
   source-backed sub-effect has not created a new task or scope by that fact
   alone. Repair it in the same bounded batch and re-review once.
4. Ask the operator again only for a real boundary change: new objective or
   artifact class, new protected or out-of-scope path, increased risk, live or
   provider use, destructive/public/external action, secrets/quota, changed
   commit authority, or an explicit operator-set budget that has been reached.
5. Repeated confirmation requests with none of those changes are
   `AVOIDABLE_OPERATOR_WAIT`, not governance safety.

## Epistemic Process Block

### Expected Result / Prediction

Sequential local review consumes more turns and finds predictable defects late.

### Evidence Comparison

SOT3-T2 accumulated related findings across repeated rounds from one authority
graph.

### Contradiction Or Gap Disposition

The findings were valid; late sequential discovery was the process defect.
Continuous Projection T1 added evidence that premature commits, range
recomputation, and worktree churn can compound the same latency pattern.

### Claim Update

First-return completeness, cost telemetry, single-pass audit evidence, commit
budget, latency disposition, round-three escalation, and same-scope authority
continuity are now shared reviewer obligations. The same-scope semantic remains
guidance and is not claimed as machine-enforced by the existing checker.

## Governance Latency WS2-T1 Learning Addendum - 2026-08-05

The WS2-T1 correction sequence repeatedly returned to the operator for another
confirmation while the objective, two worker-owned paths, documentation-only
risk ceiling, forbidden external effects, and reviewer commit ownership stayed
unchanged. The dependent findings were valid, but treating each as a new
authority event reproduced the governance latency being investigated.

The retained learning is provider-neutral: consolidate the dependency graph,
carry same-scope authority through dependent repairs, and escalate only a real
boundary change. This addendum does not weaken a stop rule or authorize scope
expansion; it prevents agents from inventing narrower authority than the
operator or controlling packet actually imposed.

rawMemoryReleased=false. This addendum records governed defect guidance only;
it releases no raw memory, provider-local memory, or reinjection payload.

### Learning Addendum Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher/reviewer/closer and governance maintainer |
| Provider or surface | local private provenance workspace |
| Session or invocation | governance-latency WS2-T1 learning promotion, 2026-08-05 |
| Working directory | repository root |
| Command or tool surface | governed reads, ADIF de-dup search, apply_patch, ADIF and review-cost checks |
| Target paths | this ADIF entry and review-cost standard |
| Allowed scope source | operator instruction to retain the observed latency finding as shared learning |
| Before status evidence | ADIF-0026 covered sequential findings but not repeated same-scope operator confirmation |
| After status evidence | ADIF-0026 and the review-cost standard define same-scope authority continuity and real escalation boundaries |
| Diff evidence | exact two-path material changed set before commit |
| Approval boundary | reviewer workflow guidance only; no runtime, checker, provider, public, or external action |
| Claim boundary | shared semantic learning; no automatic authority inference or machine-enforcement claim |
| Agent type | dispatcher/reviewer/closer and governance maintainer |
| Invocation ID | `governance-latency-ws2-t1-micro-checkpoint-learning-2026-08-05` |
| Expected manifest | ADIF-0026 and review-cost standard |
| Actual changed set | same two paths |
| Manifest delta | MATCH |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | reviewer/closer |
| Provider or surface | local private provenance workspace |
| Session or invocation | shared single-pass review latency SOP hardening, 2026-07-20 |
| Working directory | repository root |
| Command or tool surface | governed reads, rg, apply_patch, focused unit tests, review-cost and ADIF checks |
| Target paths | review-cost standard/checker/tests; this ADIF entry; guard orientation; commit steward standard; completion review |
| Allowed scope source | operator instruction to make the latency repair the common CVF SOP for all future agents |
| Before status evidence | cost telemetry existed, but pre-repair audit, latency target, avoidable-delay class, and commit budget were not required |
| After status evidence | ADIF-0026 and the review-cost checker require provider-neutral single-pass audit, latency, delay, and commit-plan evidence shapes |
| Diff evidence | exact seven-path `git diff --name-status` before material commit |
| Approval boundary | review workflow governance only; no Continuous Projection T2, runtime, public-sync, or provider/live authorization |
| Claim boundary | machine-checks evidence shape only; semantic audit completeness and fast-path eligibility remain reviewer judgment |
| Agent type | reviewer/closer |
| Invocation ID | `cvf-single-pass-review-latency-sop-2026-07-20` |
| Expected manifest | seven SOP owner, checker, test, orientation, ADIF, commit-steward, and completion-review paths |
| Actual changed set | same seven paths |
| Manifest delta | MATCH |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance reviewer-learning record.

## Claim Boundary

This entry defines shared reviewer guidance. It does not implement a semantic
checker, guarantee completeness, or accept SOT3-T2.
