# CVF MFRP-P4 Sample-Gated P5 Reopen Amendment

Memory class: BOUNDED_AUTHORITY

Status: ACTIVE_AMENDMENT

docType: baseline

Date: 2026-09-02

## Purpose

Remove calendar-wait ambiguity from the accepted P4 canary without changing
its sample target, trusted route, review cadence, or P5 authority boundary.

## Source / Predecessor Evidence

The accepted P4 design closes observation at the earlier of 20 eligible
natural returns or 30 calendar days. The operator clarified that this window
rule must not be read as a mandatory 30-day wait before P5 reconsideration.

## Authorization / Scope

P5 reconsideration is sample-gated. Fewer than 20 eligible natural returns
keeps P5 closed. At 20, a separate P5 decision may proceed immediately without
waiting for day 30. Day 30 alone never satisfies the sample gate; if the count
is below 20 then, the disposition is `INSUFFICIENT_EVIDENCE` and P5 stays
closed.

## Decision / Baseline

The 20-return threshold is necessary, not sufficient. Reaching it does not
open P5 and does not bypass safety, audit, recall, evidence-quality, or
separate-decision requirements. No review is added per return.

## Evidence / Verification

The P4 evidence emits a deterministic `p5ReopenSampleGate` object. Focused
tests cover counts 19 and 20, no calendar wait after count 20, day-30
non-authorization, and fail-closed negative input.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add the sample-gate evidence/readout and
focused regressions only.

Protected paths:

- `governance/compat/mfrp_shadow_canary.py`
- `governance/compat/test_mfrp_shadow_canary_core.py`

Operator authorization: the operator explicitly required P5 reopening to be
conditioned on enough samples rather than a mandatory 30-day wait.

Rollback boundary: revert only this amendment, the sample-gate helper,
evidence/readout field, focused tests and fixture projection. Preserve the
accepted P4 implementation, ledger and trusted-route authority.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | `Core Guard Self-Protection Authorization`; `Authorized guard-maintenance scope`; `Protected paths`; `Operator authorization`; `Rollback boundary`; `Purpose`; `Source`; `Decision`; `Evidence`; `Claim Boundary` |
| gateRunPurpose | Confirmation evidence after authoring, not first discovery of required shape. |
| claimBoundary | Checker PASS confirms artifact shape and authorized changed paths only. |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is private Core canary authority and makes no public-release claim.

## Claim Boundary

This amendment neither opens P5 nor proves recall preservation, cost saving,
correctness, route replacement, provider/live behavior, or production safety.
