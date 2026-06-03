# CVF CI2 Dependency Release Work Order Guard Hardening

Memory class: FULL_RECORD

Status: AUTHORIZED

docType: review

Date: 2026-06-03

## Purpose

Authorize bounded guard/template hardening after the CI2-T4 to CI2-T5 release
showed that a downstream work order can be moved from `HOLD_*` to
`DISPATCH_READY` while still carrying stale prerequisite placeholders such as
`Disposition: REQUIRED` and `after closure`.

## Scope

Allowed changed paths:

- `governance/compat/check_work_order_dispatch_quality.py`
- `governance/compat/test_check_work_order_dispatch_quality.py`
- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
- `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md`
- `docs/reviews/CVF_CI2_DEPENDENCY_RELEASE_WORK_ORDER_GUARD_HARDENING_2026-06-03.md`

Forbidden scope: runtime code, provider/live proof, public-sync, LPCI product
implementation, unrelated checker changes, archive cleanup, and session-mode
changes.

## Target / Source

Target: work-order dispatch quality and commit choreography.

Source evidence:

- CI2-T4 closure commit `02a201bf`;
- CI2-T5 dispatch-sync commit `6a097dbd`;
- active T5 work order:
  `docs/work_orders/CVF_WO_CI2_T5_LPCI_PRODUCT_ROADMAP_PACKET_2026-06-02.md`;
- canonical work-order template:
  `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`;
- choreography standard:
  `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md`.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: update the dispatch-quality checker and
focused tests so READY/DISPATCH work orders fail if they still contain
unresolved prerequisite placeholders in machine-readable tables.

Protected paths:

- `governance/compat/check_work_order_dispatch_quality.py`
- `governance/compat/test_check_work_order_dispatch_quality.py`

Operator authorization: the operator asked to fix any finding caused by rules
or templates immediately, so future orchestrators/workers do not repeat the
same CI2-T5 dispatch friction.

Rollback boundary: revert this hardening commit to remove the new
dependency-release check and restore the prior template/choreography text.

## Evidence Trace Block

| Evidence | Value |
| --- | --- |
| Regression | CI2-T5 release required manual refresh from `HOLD_UNTIL_T4_PASS` to `DISPATCH_READY` |
| Guard behavior added | READY/DISPATCH work orders with `Disposition: REQUIRED` or stale `after closure` dependency prose fail dispatch quality |
| Template behavior added | work-order template now requires dependency-release refresh before READY/DISPATCH |
| Choreography behavior added | dedicated Step 2A records dependency-release refresh before session sync |
| Tests | `python -m unittest governance.compat.test_check_work_order_dispatch_quality` |

## Findings / Position

Position: APPROVE bounded guard/template hardening.

Findings:

- The root defect is not worker quality; it is a missing dispatch-time rule for
  dependency-gated work orders drafted before their prerequisite closed.
- A downstream worker should receive a refreshed artifact path, closure commit,
  and fresh base anchors instead of interpreting prose such as `after closure`.

## Risk / Corrective Action

Risk: low. The checker change is limited to READY/DISPATCH work orders and
does not reject closed historical packets unless they are reopened and edited
into a new dispatch range.

Corrective action: if an intentionally staged work order needs a future
dependency, keep it in `HOLD_*` status until evidence exists.

## Final Boundary

This authorization is final for dependency-release dispatch hardening only. It
does not authorize LPCI implementation, provider calls, public-sync, runtime
changes, legal advice claims, or broader guard refactors.

## Verification Boundary

Verification is local and structural: focused unit tests, dispatch-quality
gate, core guard self-protection gate, markdown structural gate, and autorun
gate. No live/provider proof is required or claimed.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next action |
| --- | --- | --- | --- | --- |
| CI2-T5 work order could be released from HOLD while dependency evidence still used placeholder prose | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | RULE_ADDED | Dispatch-quality checker now rejects unresolved READY/DISPATCH prerequisite placeholders |
| Orchestrator template did not spell out dependency-release refresh | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | TEMPLATE_UPDATED | Work-order template and choreography standard now require source-backed ACCEPT evidence and base refresh |
| Runtime/provider/cost terms appear only as forbidden-scope and boundary text | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | No runtime/provider/cost signal is evaluated in this guard-template batch |

## Claim Boundary

This packet authorizes and documents one bounded guard/template hardening. It
does not claim semantic correctness of future work orders or autonomous
dependency interpretation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance guard/template hardening; no public-facing product
artifact is exported.
