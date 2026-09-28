# CVF GC-018 Baseline - NCR Q001 HTML Ingress

Memory class: governed-dispatch-baseline

docType: baseline

Status: ACTIVE_BOUNDED

Batch ID: CVF-NCR-Q001-HTML-INGRESS

Dispatch base head: `97abcecc50b8f734376cec015b7e96b1126479d1`

Decision owner: operator for pilot data, effect, provider and cost; Local for bounded source repair and review.

## Purpose

The operator authorized the proposed Q001 HTML repair on 2026-09-28. Correct ingress validation, common-secret scanning, and receipt-state presentation on the existing export route. This is a source repair and synthetic verification tranche, not pilot admission.

## Scope

Allowed: the existing HTML export route, receipt helper, component and focused tests; one source/evidence review and Q001 roadmap status update. Inspect deployment configuration by secret-safe presence/shape only. Synthetic UI walkthrough may use a local browser without provider credentials.

Forbidden: P11, external runtime integration, raw secret or ledger reads, provider/live call, real content submission, deployment, public-sync, cost-bearing pilot, broad governance-engine changes.

## Source / Predecessor Evidence

Roadmap Q001/D015 and accepted NCR R0 W00/W01/W02 packets establish the selected HTML route, receipt-hop profile and downstream trace. The operator's 2026-09-28 instruction authorizes this local repair, while the active handoff keeps P11 parked.

## Baseline Invariants

1. A receipt anchor and successful HTML generation do not establish a governance decision or final acceptance.
2. Missing, malformed, or DENY receipt remains draft and unaccepted. ALLOW receipt is review evidence, not final artifact acceptance.
3. Reject invalid schema, type, size and common-secret patterns in every rendered input field before the receipt/evaluate hop.
4. Keep W00/W01/W02 accepted source findings; do not rerun their survey without a named contradiction.
5. Actual NEXTAUTH_URL destination, retention and cost remain UNKNOWN until a bounded operator profile is established.

## Verification / Evidence

Focused offline negative and positive tests; typecheck; synthetic UI walkthrough when local execution permits. These establish source behavior under fixtures only. Live governance proof, R0 exit and A04/A05/A08 acceptance remain open.

## Claim Boundary

This baseline authorizes a reversible local Q001 repair. It does not authorize live provider proof or certify the runtime chain.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_baseline_update_compat.py`; `governance/compat/check_gc018_stop_boundary_semantics.py` |
| literalTokensReviewed | `Status`, `Batch ID`, `Claim Boundary`, `Public Export Disposition`, `Source / Predecessor Evidence` |
| gateRunPurpose | Confirmation of the authored baseline and evidence, not first discovery of required shape. |
| claimBoundary | Read-ahead covers this bounded local baseline only; it does not establish live governance proof. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | bounded Q001 source repair; no P11, provider/live or public action |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
