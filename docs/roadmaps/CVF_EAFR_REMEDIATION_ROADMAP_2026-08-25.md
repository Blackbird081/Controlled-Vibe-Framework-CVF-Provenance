# CVF EAFR Remediation Roadmap

Memory class: SUMMARY_RECORD

Status: ACTIVE_R5_REVIEWER_ACCEPTED_CLOSED_PASS_BOUNDED_R1C_READY_FOR_DISPATCH_AUTHORING

Date: 2026-08-25

Roadmap ID: EAFR

Decision owner: operator through explicit 2026-08-25 orchestrator authority

Reviewer/closer: current independent orchestrator/reviewer

## Authorization Decision

The operator explicitly authorized the current orchestrator on 2026-08-25 to
prioritize and govern this sequence before returning to the parked checkpoint.

## Purpose

Close the source-verified safety and truthfulness gaps accepted into EAFR while
the earlier RFR final-reconciliation checkpoint remains parked. Execute small,
dependency-ordered tranches and require independent review before each closure.

## Source Evidence

| Source | Current verified fact | Disposition |
| --- | --- | --- |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/aif-memory-reinjection.ts` | omitted item provenance currently defaults to `1` before eligibility | ACCEPT |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/aif-memory-reinjection.test.ts` | existing adversarial coverage omits missing and non-finite provenance cases | ACCEPT |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | the decision prompt block is composed into the execute system prompt | ACCEPT |
| archive-hygiene commit `0fcc1dc20` | advisory inputs preserved as history without authority status | ACCEPT_AS_LINEAGE_ONLY |

## Scope

In scope: AIF reinjection provenance admission, durable-memory write authority
and omission behavior, as-built memory map reconciliation, provider-current
claim inventory, retrieval evidence semantics, and final EAFR reconciliation.

Out of scope: public sync, push, deployment, unrelated product work, automatic
use of credentials, and resuming the parked RFR checkpoint before EAFR closes.

## Non-Goals

This roadmap does not combine tranches, pre-approve live calls, treat advisory
history as authority, or permit a worker to review, close, commit, or publish
its own work.

## Proposed Tranches

| Tranche | Objective | Dependency | Status |
| --- | --- | --- | --- |
| EAFR-R1 | reject missing or non-finite AIF item provenance before prompt composition | archive hygiene `0fcc1dc20` | REVIEWER_ACCEPTED_CLOSED_PASS_BOUNDED_BY_EXPLICIT_OPERATOR_WAIVER: focused implementation accepted; three non-green package criteria preserved as R1C debt |
| EAFR-R1A | make the package non-live test runner exclude both `.live.test.ts` and `.live.test.tsx`, then reconcile the R1 incident | R1 implementation accepted | REVIEWER_ACCEPTED_COMPLETE_BOUNDED at `ef142bfb2` |
| EAFR-R1B | adjudicate exact execution-base variance against the parent R1 acceptance authority | R1A accepted and prior A/B evidence committed | REVIEWER_ACCEPTED_FAIL_CLOSED_ADJUDICATION at `fc10c8e65`; subsequent explicit operator waiver closes R1 without changing R1B's evidence finding |
| EAFR-R2 | make durable-memory HTTP writes and authority inputs fail closed | R1 bounded waiver closure, R1A accepted, and R1B adjudication accepted | REVIEWER_ACCEPTED_CLOSED_PASS_BOUNDED; 26/26 focused; package/typecheck debt remains R1C-owned |
| EAFR-R3 | reconcile the memory-plane map to accepted as-built behavior | R2 accepted | REVIEWER_ACCEPTED_CLOSED_PASS_BOUNDED; 46/46 focused; worker-return fast and reviewer-fast 65/65 PASS |
| EAFR-R4 | replace partial provider-current claims with a complete private manifest | R3 accepted | REVIEWER_ACCEPTED_CLOSED_PASS_BOUNDED; 29 classified active entries, zero unmapped; focused 17/17 and reviewer-fast 65/65 PASS; broad debt remains R1C-owned |
| EAFR-R5 | decide and prove retrieval evidence semantics without weakening admission | R4 accepted | REVIEWER_ACCEPTED_CLOSED_PASS_BOUNDED; focused LPF 66/66 and Web 20/20; safe LPF package 1943/1943; six unintended provider calls disclosed and excluded from acceptance |
| EAFR-R1C | repair or freshly adjudicate the waived typecheck, full non-live-suite, and build debt | explicit R1 waiver and R5 accepted | READY_FOR_FRESH_DISPATCH_AUTHORING; mandatory before R6 |
| EAFR-R6 | independently reconcile closures and decide whether parked RFR may resume | R1/R1A/R1B, R2-R5 accepted, and R1C debt resolved or freshly adjudicated | HOLD_DEPENDENCY |

## Design Controls

- Each implementation tranche owns the smallest source/test surface that can
  prove its invariant.
- Missing evidence at a safety boundary fails closed.
- A worker never closes its own tranche and never commits in this roadmap.
- Provider/live proof is used only when a later work order explicitly requires
  it and carries diagnostic, secret, quota, and external-effect controls.
- Documentation is updated only after corresponding runtime behavior is
  accepted; documentation never substitutes for runtime proof.

## Design Control Gate

Each tranche must have a source-verified GC-018 baseline, committed no-commit
work order, exact ownership manifest, negative proof, and independent closure.

## Work Plan

Execute the Proposed Tranches table strictly in dependency order. Only the
current `DISPATCH_READY` row may enter worker execution.

## Acceptance Criteria

- R1 proves omitted, explicit-undefined, and non-finite provenance cannot enter
  selected memory or the generated system prompt.
- R2 proves unauthorized or incomplete durable writes are rejected with no
  storage mutation.
- R3 maps only accepted as-built components and clearly marks absent behavior.
- R4 has a complete, source-backed private provider manifest without a public
  export claim.
- R5 records a bounded design verdict plus executable proof for any admitted
  retrieval evidence.
- R6 contains no unresolved P0/P1 row before the parked roadmap can resume.

## Risk / Corrective Action

Primary risk is a compatibility repair that silently weakens admission. Every
runtime tranche therefore requires negative tests, unchanged-path hashes, a
no-commit worker return, and independent reviewer closure. Any need to change
the claim boundary, use live credentials, or touch a forbidden path returns
`BLOCKED_WITH_REASON`.

## Verification Evidence

Roadmap verification consists of tranche-specific focused/full tests,
governance phase gates, exact manifests, reviewer decisions, committed hashes,
and a final reconciliation before the parked checkpoint is reconsidered.

## Current Runtime Freshness Verification

Current source was independently reviewed on 2026-08-25 after R5 worker return
and bounded reviewer repair. Retrieval evidence now requires finite trust in
the closed interval `[0,1]` before selection on ordinary, KGR and injected graph
paths, and the authenticated readout route rejects malformed trust before
workflow construction. Lexical relevance remains subordinate to actor, scope,
privacy, lifecycle and trust admission. Six unintended provider calls caused by
a contradictory broad command are disclosed and excluded from acceptance; they
grant no repeat-live authority. This is bounded local source/test acceptance,
not provider, deployment, exposure or production proof.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_core_guard_self_protection.py` |
| literalTokensReviewed | roadmap status; dependency rows; public export disposition; checker read-ahead confirmation language |
| gateRunPurpose | confirm and record evidence for the already source-verified roadmap shape; not first discovery |
| claimBoundary | checker conformance does not prove runtime remediation or release readiness |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private provenance remediation sequence; public sync is not
authorized.

## Claim Boundary

This roadmap authorizes bounded dispatch authoring and dependency sequencing.
It does not itself implement, test, live-prove, deploy, publish, push, or close
any runtime behavior.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | EAFR tranche packets | R1-R5 committed dispatch authority | PASS |
| Completion or reviewer artifact | R5 completion review | reviewer-accepted bounded closure and incident recorded | PASS |
| Roadmap state | this file | R5 accepted bounded; R1C ready only for fresh dispatch authoring | PASS |
| Registry JSON | system-chain map | `ARCHITECTURE.md` fingerprint refreshed; freshness CURRENT | PASS |
| Registry Markdown | N/A with reason: no registry projection | no applicability | BLOCKED |
| External evidence digest | archived corrected external report | input only, not authority | N/A with reason |
| System loop interlock | R5 -> R1C -> R6 | fail-closed dependencies explicit | PASS |
| Session continuity | separate post-material sync | required after material commit | PASS |
