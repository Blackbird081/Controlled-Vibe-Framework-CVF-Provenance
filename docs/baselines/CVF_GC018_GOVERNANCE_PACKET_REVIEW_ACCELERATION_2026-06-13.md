# CVF GC-018 - Governance Packet Review Acceleration

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-13

Owner: Codex

## Purpose

Authorize a bounded CVF control-plane hardening batch before MEMCON-T1b.

The operator asked whether CVF can stay strict while reviewing faster. This
batch promotes a repeated review-latency pattern into a pre-dispatch machine
check: Required Proof Manifest literals must be atomic instead of compound
cells that force reviewers or workers to debug malformed proof requirements
late in the hook chain.

## Authority Chain

Operator direction: "Nang cap di, truoc khi qua MEMCON-T1b".

Governance standards:

- `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md`
- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
- `docs/reference/CVF_WORK_ORDER_AUTHORING_HARDENING_ADDENDUM_2026-06-11.md`
- `governance/compat/check_work_order_dispatch_quality.py`

## Objective

Reduce reviewer and worker latency without weakening governance by moving a
packet-authoring defect from late review into the earliest applicable
dispatch-quality gate.

## Decision / Baseline / Proposed Tranche

Decision: close this as one small control-plane hardening tranche.

Baseline: before this batch, a Required Proof Manifest cell could contain more
than one required literal, and the checker would treat the compound text as one
literal.

Proposed tranche:

- add an atomic-literal rule to the authoring hardening addendum;
- harden `check_work_order_dispatch_quality.py`;
- add focused unit tests;
- close with bounded private-provenance evidence.

## Bounded Scope

Allowed:

- `docs/reference/CVF_WORK_ORDER_AUTHORING_HARDENING_ADDENDUM_2026-06-11.md`
- `governance/compat/check_work_order_dispatch_quality.py`
- `governance/compat/test_check_work_order_dispatch_quality.py`
- this GC-018 baseline, matching work order, and completion review

Forbidden:

- MEMCON-T1b implementation or dispatch;
- Policy_Local mutation;
- EC activation, retrieval, OCR/provider/API, corpus ingestion, public-sync,
  public readiness, production readiness, memory reinjection, or autonomous
  mutation claims;
- broad template refactor or session-front-door rotation.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| Work-order template defines Required Proof Manifest | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | Required Proof Manifest | `Required literal` | work-order template | ACCEPT |
| Dispatch checker validates Required Proof Manifest proof files and literals | `governance/compat/check_work_order_dispatch_quality.py` | `_validate_work_order_fulfillment_manifests` | `Required Proof Manifest` | dispatch-quality checker | ACCEPT |
| Authoring addendum is the current owner surface for packet-hardening rules | `docs/reference/CVF_WORK_ORDER_AUTHORING_HARDENING_ADDENDUM_2026-06-11.md` | existing packet-hardening sections | `Near-Threshold Template Owner Discipline` | work-order authoring hardening addendum | ACCEPT |

## Closure Summary

This GC-018 closes in the same batch because the operator authorized Codex to
self-execute this small control-plane hardening before MEMCON-T1b.

Completion evidence is recorded in:

`docs/reviews/CVF_GOVERNANCE_PACKET_REVIEW_ACCELERATION_COMPLETION_2026-06-13.md`

## Evidence / Verification

Required closure evidence:

- focused dispatch-quality unittest PASS;
- dispatch-quality gate PASS;
- reviewer-fast PASS before material closure;
- no public-sync, provider/API, Policy_Local, or MEMCON-T1b implementation
  claims.

## Claim Boundary

This baseline authorizes only governance packet authoring acceleration for
Required Proof Manifest atomic literal discipline. It does not prove faster
global pre-commit runtime, MEMCON-T1b readiness, Policy_Local readiness, public
readiness, production readiness, OCR/provider behavior, or autonomous mutation.
