# CVF PolicyLocal Successor Pilot Roadmap

Memory class: FULL_RECORD

Status: PROPOSED_READY_FOR_FRESH_AUTHORIZATION

docType: roadmap

Date: 2026-06-12

Owner: Codex

## Authorization / Decision

Decision: `POLICYLOCAL_SUCCESSOR_PILOT_AFTER_RDA_FOUNDATION`.

RDA-T4 releases this roadmap as a proposed next use-case lane only. No
Policy_Local implementation, corpus mutation, retrieval, OCR, EC activation,
provider/API-key use, public-sync, production readiness, or public readiness
is authorized by this roadmap alone.

## Purpose

Use Policy_Local as the first real use-case pilot for the CVF scan layer,
metadata evidence layer, and regulated-domain adapter foundation.

The first pilot should prove that CVF can turn imperfect input files into a
clean operator-visible evidence and correction workflow before deeper domain
retrieval or current-law reasoning is attempted.

## Scope / Target / Owner Boundary

In scope for a future authorized pilot:

- consume existing governed EX, MEOR, RDA, and EC-T4 evidence;
- produce operator-visible metadata gap and resolution workflow artifacts;
- preserve source-embedded versus operator-supplied evidence labels;
- keep unresolved records blocked;
- define the next allowed real Policy_Local integration step.

Out of scope until separately authorized:

- external Policy_Local workspace writes;
- candidate metadata mutation;
- EC-T5/EC-T6 activation or `QUERY_CLASS_GATED` write;
- retrieval behavior, OCR installation, corpus ingestion;
- provider/API-key use;
- T12 authoring or eligibility claim;
- public-sync, production readiness, public readiness.

## Non-Goals

This roadmap does not:

- prove legal or current-law correctness;
- repair the current Policy_Local input corpus;
- activate EC gate values or retrieval;
- install OCR or ingest documents;
- call providers or use API keys;
- export public-facing claims.

## Authority Chain

| Authority | Path | Disposition |
| --- | --- | --- |
| RDA-T4 closure | `docs/reviews/CVF_MEOR_RDA_T4_FOUNDATION_CLOSURE_AND_POLICYLOCAL_SUCCESSOR_COMPLETION_2026-06-12.md` | RELEASES_PROPOSED_ROADMAP |
| EX-T9 completion | `docs/reviews/CVF_LPCI2_EX_T9_OPERATOR_VISIBLE_SCAN_OUTCOME_REPORT_COMPLETION_2026-06-12.md` | ACCEPT_AS_SCAN_REPORT_FOUNDATION |
| MEOR-T5 closure | `docs/reviews/CVF_MEOR_T5_FOUNDATION_CLOSURE_AND_DOWNSTREAM_READINESS_COMPLETION_2026-06-12.md` | ACCEPT_AS_METADATA_FOUNDATION |
| RDA-T3 completion | `docs/reviews/CVF_MEOR_RDA_T3_CROSS_DOMAIN_CONFORMANCE_COMPLETION_2026-06-12.md` | ACCEPT_AS_REGULATED_ADAPTER_FOUNDATION |
| EC-T4 completion | `docs/reviews/CVF_LPCI2_EC_T4_OPERATOR_DATE_EVIDENCE_BACKFILL_COMPLETION_2026-06-11.md` | ACCEPT_AS_BLOCKER_INPUT |

## Design Control Gate

Design verdict: `PASS_BOUNDED_PROPOSED`.

Selected design:

1. Start with an evidence-resolution pilot, not retrieval/chat.
2. Treat EC-T4 gaps as useful scan-layer output.
3. Preserve generic CVF foundation surfaces and keep Policy_Local as a use
   case, not a global schema default.
4. Require fresh GC-018 and source-verified work order before any build.

Rejected design:

- jump directly into legal QA or current-law answer generation;
- ingest or mutate corpus records before operator evidence is accepted;
- activate EC-T5/EC-T6 before blocked metadata is resolved;
- install OCR or run provider calls in the first successor tranche.

## Proposed Tranche Plan

| Tranche | Deliverable | Dependency | Status |
| --- | --- | --- | --- |
| PL-S1 | Policy_Local evidence-resolution pilot authorization and source map | RDA-T4 closure | READY_FOR_FRESH_AUTHORIZATION |
| PL-S2 | Operator-supplied metadata resolution packet | PL-S1 plus operator evidence | HOLD_PENDING_OPERATOR_EVIDENCE |
| PL-S3 | Corpus mutation or integration dry-run decision | PL-S2 closure | HOLD_PENDING_PL_S2 |
| PL-S4 | Retrieval/chat readiness assessment | PL-S3 closure plus EC gate decision | HOLD_PENDING_EC |

## Work Plan

1. Open PL-S1 only through fresh GC-018 and a source-verified work order.
2. Source-map existing governed EX, MEOR, RDA, and EC-T4 evidence.
3. Produce an operator-readable evidence-resolution plan.
4. Keep unresolved candidates blocked until operator evidence is accepted.
5. Decide whether a later PL-S2 operator packet is safe to open.

## Dispatch Boundary

The next authorized work order may only open PL-S1.

PL-S1 may:

- read governed private provenance artifacts;
- source-map current Policy_Local evidence artifacts;
- produce a bounded operator evidence-resolution plan.

PL-S1 must not:

- edit external Policy_Local workspace files;
- write corpus records;
- activate EC-T5/EC-T6;
- install OCR or ingest corpus;
- call providers or use API keys;
- claim retrieval, T12, production, or public readiness.

## Acceptance Criteria

1. PL-S1 remains source-map and evidence-resolution only.
2. Policy_Local external files remain untouched until a later explicit
   integration tranche.
3. EC-T4 blocked metadata records remain blocked until operator evidence is
   supplied and accepted.
4. Any later corpus mutation or retrieval work receives a separate roadmap,
   GC-018 baseline, and work order.
5. All outputs keep CVF foundation claims separate from Policy_Local use-case
   claims.

## Verification / Evidence

Evidence for this roadmap is limited to governed provenance artifacts:

- RDA-T4 closure package;
- EX-T9 scan outcome reporting closure;
- MEOR-T5 foundation closure;
- RDA-T3 conformance closure;
- EC-T4 blocked metadata report and completion.

Future PL-S1 must record changed-path proof showing no external Policy_Local
mutation unless a later operator-authorized integration tranche explicitly
allows it.

## Governed Work Lifecycle

`INTAKE -> DESIGN -> SPEC -> WORK ORDER -> BUILD -> REVIEW -> FREEZE`

- INTAKE: RDA-T4 releases Policy_Local only as a proposed use-case lane.
- DESIGN: this roadmap starts with evidence resolution before integration.
- SPEC: PL-S1 must define the source map and acceptance rules.
- WORK ORDER: PL-S1 requires fresh GC-018 and source verification.
- BUILD: no build occurs until PL-S1 is authorized.
- REVIEW: blocked metadata remains visible to the operator.
- FREEZE: only after evidence is resolved may deeper integration be proposed.

## Claim Boundary

This roadmap proposes a Policy_Local successor pilot only. It does not prove
metadata truth, legal/current status, source authenticity, OCR quality,
retrieval quality, Policy_Local readiness, EC activation, T12 readiness,
provider behavior, production readiness, public readiness, or autonomous
correction.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private use-case pilot planning; no public-sync authorized.
