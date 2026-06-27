# CVF GC-018 Baseline: MEOR-RDA-T4 Foundation Closure And PolicyLocal Successor

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: baseline

Date: 2026-06-12

Owner: Codex

baseHead: `2fd34992`

## Purpose

Authorize and close the final regulated-domain adapter foundation tranche.

RDA-T4 freezes the MEOR regulated-domain adapter foundation and releases only
a proposed Policy_Local successor pilot roadmap. It does not authorize
Policy_Local corpus mutation, EC activation, retrieval, OCR, provider/API-key
use, public-sync, production readiness, or public readiness.

## Scope / Target / Owner Boundary

In scope:

- close the RDA roadmap as a bounded foundation;
- record RDA-T1 through RDA-T3 evidence chain;
- decide whether a Policy_Local successor pilot may be proposed;
- author a proposed Policy_Local successor pilot roadmap;
- update RDA roadmap status and closure evidence.

Out of scope:

- external Policy_Local workspace edits;
- candidate metadata correction;
- EC-T5/EC-T6 activation or `QUERY_CLASS_GATED` write;
- retrieval behavior, OCR, corpus ingestion, provider/API-key use;
- T12 authoring or eligibility claim;
- public-sync, production readiness, public readiness;
- memory reinjection, high-risk promotion, autonomous mutation.

## Authority Chain

| Authority | Path | Status |
| --- | --- | --- |
| Operator direction | 2026-06-12 agreement to proceed after RDA-T3 | ACCEPT |
| RDA roadmap | `docs/roadmaps/CVF_MEOR_REGULATED_DOMAIN_ADAPTER_ROADMAP_2026-06-12.md` | ACTIVE_RDA_T3_CLOSED_RDA_T4_AUTHORIZATION_READY |
| RDA-T1 completion | `docs/reviews/CVF_MEOR_RDA_T1_REGULATED_DATE_ADAPTER_CONTRACT_COMPLETION_2026-06-12.md` | CLOSED_PASS_BOUNDED |
| RDA-T2 completion | `docs/reviews/CVF_MEOR_RDA_T2_DETERMINISTIC_ADAPTER_IMPLEMENTATION_COMPLETION_2026-06-12.md` | CLOSED_PASS_BOUNDED |
| RDA-T3 completion | `docs/reviews/CVF_MEOR_RDA_T3_CROSS_DOMAIN_CONFORMANCE_COMPLETION_2026-06-12.md` | CLOSED_PASS_BOUNDED |
| EX-T9 completion | `docs/reviews/CVF_LPCI2_EX_T9_OPERATOR_VISIBLE_SCAN_OUTCOME_REPORT_COMPLETION_2026-06-12.md` | CLOSED_PASS_BOUNDED |
| EC-T4 completion | `docs/reviews/CVF_LPCI2_EC_T4_OPERATOR_DATE_EVIDENCE_BACKFILL_COMPLETION_2026-06-11.md` | CLOSED_BLOCKED_BOUNDED |

## Source / Predecessor Evidence

| Predecessor | Evidence artifact | Disposition |
| --- | --- | --- |
| RDA-T1 | `docs/reviews/CVF_MEOR_RDA_T1_REGULATED_DATE_ADAPTER_CONTRACT_COMPLETION_2026-06-12.md` | ACCEPT |
| RDA-T2 | `docs/reviews/CVF_MEOR_RDA_T2_DETERMINISTIC_ADAPTER_IMPLEMENTATION_COMPLETION_2026-06-12.md` | ACCEPT |
| RDA-T3 | `docs/reviews/CVF_MEOR_RDA_T3_CROSS_DOMAIN_CONFORMANCE_COMPLETION_2026-06-12.md` | ACCEPT |
| EX scan report foundation | `docs/reviews/CVF_LPCI2_EX_T9_OPERATOR_VISIBLE_SCAN_OUTCOME_REPORT_COMPLETION_2026-06-12.md` | ACCEPT |
| EC metadata blocker | `docs/reviews/CVF_LPCI2_EC_T4_OPERATOR_DATE_EVIDENCE_BACKFILL_COMPLETION_2026-06-11.md` | ACCEPT_AS_BLOCKER |

## Decision / Baseline

Decision: `RDA_FOUNDATION_CLOSED_POLICYLOCAL_SUCCESSOR_PROPOSED`.

RDA-T4 may close the regulated-domain adapter foundation and propose the next
Policy_Local use-case lane. The successor lane must begin with fresh
authorization before any build or external workspace action.

## Design Control Gate

Design verdict: `PASS_BOUNDED`.

Selected design:

1. Close RDA as a foundation layer, not as a Policy_Local readiness claim.
2. Release a proposed Policy_Local pilot roadmap that starts with evidence
   resolution and operator-visible reporting.
3. Preserve EC-T4 blocked metadata as a useful input-quality result.
4. Keep EC-T5/EC-T6, retrieval, OCR, and T12 behind separate authorization.

Rejected design:

- mutate Policy_Local immediately after RDA-T3;
- treat RDA closure as legal/current-status proof;
- treat scan-layer success as retrieval or T12 readiness;
- use provider/API keys or live proof for this local documentation decision.

## Acceptance Criteria

1. RDA-T1 through RDA-T3 are source-backed and closed bounded.
2. RDA roadmap is closed bounded through T4.
3. Policy_Local successor is only proposed and remains unopened.
4. EC-T4 metadata gaps remain explicit blockers.
5. No external Policy_Local path is touched.
6. No runtime/source behavior changes.
7. Reviewer-fast and pre-closure gates pass.

## Evidence / Verification

| Evidence requirement | Verification path | Result |
| --- | --- | --- |
| RDA predecessor chain | Authority Chain and Source / Predecessor Evidence | PASS |
| Closed roadmap status | `docs/roadmaps/CVF_MEOR_REGULATED_DOMAIN_ADAPTER_ROADMAP_2026-06-12.md` | PASS |
| Proposed successor only | `docs/roadmaps/CVF_POLICYLOCAL_SUCCESSOR_PILOT_ROADMAP_2026-06-12.md` | PASS |
| EC blocker retained | EC-T4 completion reference | PASS |
| External Policy_Local untouched | changed-path review | PASS |

## Claim Boundary

RDA-T4 proves only that the regulated-domain adapter foundation is ready to
support a later Policy_Local successor pilot. It does not prove metadata truth,
legal/current status, source authenticity, retrieval quality, OCR quality,
Policy_Local readiness, EC activation, T12 readiness, provider behavior,
production readiness, public readiness, or autonomous correction.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private RDA foundation closure and proposed Policy_Local successor
planning; no public-sync authorized.
