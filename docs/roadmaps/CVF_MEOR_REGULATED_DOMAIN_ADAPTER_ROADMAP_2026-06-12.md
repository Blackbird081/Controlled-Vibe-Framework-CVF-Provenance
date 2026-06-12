# CVF MEOR Regulated-Domain Adapter Roadmap

Memory class: FULL_RECORD

Status: ACTIVE_RDA_T2_DISPATCHED

docType: roadmap

Date: 2026-06-12

Owner: Codex

## Authorization / Decision

Decision: `REGULATED_DOMAIN_ADAPTER_AFTER_MEOR_FOUNDATION`.

MEOR foundation closed bounded at `6c2ad2b3`. The released next lane is a
fresh regulated-domain adapter roadmap, GC-018 baseline, and source-verified
work order. This roadmap maps regulated-date concepts into the generic MEOR
contract without making Policy_Local or legal-policy fields global CVF
defaults.

## Purpose

Create a reusable regulated-domain adapter layer that can:

1. map profile-scoped regulated concepts into MEOR metadata requirements;
2. preserve the distinction between source-embedded, operator-supplied,
   derived-hint, and absent evidence;
3. keep unresolved regulated records blocked until evidence is accepted;
4. prevent `documentStatus`, `promulgationDate`, and `effectiveDate` from
   appearing in non-regulatory profiles by default;
5. prepare a later Policy_Local use-case roadmap without mutating its corpus.

## Scope / Target / Owner Boundary

Target owners:

- MEOR contract and semantics documents for adapter-level mapping;
- Control Plane Foundation profile requirement declarations in a later
  implementation tranche;
- focused synthetic conformance tests for legal-policy versus non-regulatory
  domains.

In scope:

- adapter contract and machine-readable semantics;
- source-verified mapping from regulated-date fields to generic MEOR
  requirement records;
- profile-scoped requirements for regulated domains only;
- query-class-gated readiness as a downstream disposition candidate, not a
  runtime gate activation in T1;
- synthetic conformance planning.

Out of scope:

- external Policy_Local workspace edits;
- candidate metadata correction;
- EC-T5/EC-T6 activation;
- retrieval, OCR installation, corpus ingestion, provider/API-key use;
- public-sync, production readiness, or public readiness.

## Non-Goals

This roadmap does not:

- decide legal or current-law status;
- infer effective dates from filenames, OCR text, or derived hints;
- make operator-supplied evidence equivalent to source-embedded evidence;
- default non-regulatory records to regulated lifecycle fields;
- activate `QUERY_CLASS_GATED` at runtime;
- release Policy_Local, EC retrieval, or T12 work.

## Authority Chain

| Authority | Path or decision | Disposition |
| --- | --- | --- |
| Operator direction | 2026-06-12 continue after MEOR foundation closure | ACCEPT |
| MEOR-T5 closure | `docs/reviews/CVF_MEOR_T5_FOUNDATION_CLOSURE_AND_DOWNSTREAM_READINESS_COMPLETION_2026-06-12.md` | ACCEPT |
| MEOR foundation roadmap | `docs/roadmaps/CVF_METADATA_EVIDENCE_AND_OPERATOR_RESOLUTION_FOUNDATION_ROADMAP_2026-06-12.md` | ACCEPT |
| MEOR contract | `docs/reference/CVF_METADATA_EVIDENCE_AND_OPERATOR_RESOLUTION_CONTRACT_2026-06-12.md` | ACCEPT |
| MEOR semantics | `docs/reference/CVF_METADATA_EVIDENCE_AND_OPERATOR_RESOLUTION_SEMANTICS_2026-06-12.json` | ACCEPT |
| EC-T1 regulated-date decision | `docs/baselines/CVF_GC018_LPCI2_EC_T1_REGULATORY_DATE_MODEL_GOVERNANCE_DECISION_2026-06-11.md` | ACCEPT_AS_REGULATED_DOMAIN_INPUT |
| EC-02 semantics | `docs/reference/CVF_EC02_GATE_SEMANTICS_2026-06-11.json` | ACCEPT_AS_REGULATED_DOMAIN_INPUT |

## Current Runtime Freshness Verification

Verified at base `d1140459`:

```text
docs/reference/CVF_METADATA_EVIDENCE_AND_OPERATOR_RESOLUTION_CONTRACT_2026-06-12.md
docs/reference/CVF_METADATA_EVIDENCE_AND_OPERATOR_RESOLUTION_SEMANTICS_2026-06-12.json
EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/metadata_evidence.py
EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.metadata.requirement.bridge.ts
EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts
docs/reference/CVF_EC02_GATE_SEMANTICS_2026-06-11.json
```

Observed:

- MEOR has generic metadata evidence fields and fail-closed semantics.
- Extraction foundation can evaluate metadata evidence records.
- DSCP profiles can declare profile-scoped `metadataRequirements`.
- LPCI types now expose `DocumentStatus`, `documentStatus`,
  `promulgationDate`, `effectiveDate`, and `jurisdiction`.
- EC-02 semantics define `QUERY_CLASS_GATED` and keep
  `BLOCKED_UNTIL_2026-07-01` active until the evidence path is resolved.

## Gap Statement

MEOR can represent generic metadata evidence, and LPCI has regulated-date
fields. The missing layer is the adapter contract that says exactly how
regulated-date concepts become MEOR requirements and when their resolution may
release a downstream re-evaluation. Without this adapter, Policy_Local can
tempt the system into hard-coding legal-policy fields into CVF foundation.

## Design Control Gate

Design verdict: `PASS_BOUNDED`.

Selected design:

1. T1 locks the adapter contract and JSON semantics before implementation.
2. Regulated fields are profile-scoped, not global defaults.
3. `documentStatus` is treated as a regulated lifecycle field, distinct from
   `domainFacetFields.documentStatus` fixtures.
4. `QUERY_CLASS_GATED` remains a documented downstream target until a runtime
   gate tranche is separately authorized.
5. Operator-supplied metadata remains provenance-labeled and does not
   masquerade as source-embedded evidence.

Rejected design:

- mutate Policy_Local records before the adapter exists;
- infer current legal status from filenames or OCR text;
- default non-regulatory domains to `documentStatus=IN_FORCE`;
- activate EC-T5/EC-T6 inside this roadmap;
- treat adapter closure as retrieval or T12 readiness.

## Tranche Plan

| Tranche | Deliverable | Dependency | Status |
| --- | --- | --- | --- |
| RDA-T1 | Regulated-date adapter contract and machine semantics | MEOR-T5 closure `6c2ad2b3` | CLOSED_PASS_BOUNDED |
| RDA-T2 | Local deterministic adapter implementation for regulated profile requirement generation | RDA-T1 closure `6a6b343f` and sync `6a9a5703` | DISPATCHED |
| RDA-T3 | Cross-domain conformance proving non-regulatory profiles do not inherit regulated fields | RDA-T2 closure | HOLD_UNTIL_T2_PASS |
| RDA-T4 | Foundation closure and Policy_Local successor readiness decision | RDA-T3 closure | HOLD_UNTIL_T3_PASS |
| Policy_Local successor | Real candidate metadata resolution and integration | RDA-T4 closure plus operator/source evidence | NOT_OPEN |

## RDA-T1 Dispatch Target

RDA-T1 is specification-only.

Required outputs:

- fresh GC-018 baseline;
- source-verified work order;
- canonical adapter Markdown contract;
- machine-readable JSON semantics;
- examples for one legal-policy profile and one non-regulatory profile;
- explicit forbidden global-default rules;
- no runtime/source implementation.

## Work Plan

1. Dispatch RDA-T1 as specification-only.
2. Lock the adapter contract and JSON semantics.
3. Validate JSON parse and examples.
4. Close RDA-T1 before any runtime implementation.
5. Dispatch RDA-T2 only after T1 closure and dependency-release evidence.
6. Prove cross-domain non-bleed in RDA-T3.
7. Close the adapter in RDA-T4 and decide whether a Policy_Local successor can
   be opened.

## Dispatch Boundary

RDA-T1 may authorize only:

- contract and semantics authoring;
- source verification of existing MEOR, DSCP, LPCI, and EC-02 surfaces;
- synthetic examples;
- completion review and continuity updates.

RDA-T1 must not authorize:

- TypeScript or Python runtime implementation;
- external Policy_Local changes;
- candidate metadata correction;
- EC-T5/EC-T6 activation;
- OCR execution or dependency installation;
- corpus ingestion;
- retrieval behavior;
- provider/API-key use;
- public-sync or readiness claims.

## Acceptance Criteria

1. Adapter semantics are locked before implementation.
2. Regulated fields are profile-scoped and not globally injected.
3. `documentStatus`, `promulgationDate`, and `effectiveDate` map to MEOR
   requirement IDs only for regulated profiles.
4. Operator-supplied evidence retains its evidence basis.
5. Missing, ambiguous, or conflicting regulated evidence retains downstream
   block.
6. Non-regulatory domains can explicitly produce `NOT_APPLICABLE` without
   receiving lifecycle fields.
7. No Policy_Local external path is touched.
8. No runtime source is changed in T1.
9. Reviewer-fast, pre-dispatch, and closure gates pass.

## Verification And Evidence Plan

- JSON parse and value conformance for RDA-T1 semantics;
- source-verification table for every existing source fact;
- negative collision note for `domainFacetFields.documentStatus`;
- synthetic legal-policy and technical-project examples;
- changed-path proof excluding runtime source and external Policy_Local;
- reviewer-fast, pre-dispatch, pre-implementation, and pre-closure gates as
  applicable.

No live provider proof is required because this roadmap authorizes local,
deterministic control-plane contract work only.

## Governed Work Lifecycle

`INTAKE -> DESIGN -> SPEC -> WORK ORDER -> BUILD -> REVIEW -> FREEZE`

- INTAKE: MEOR-T5 released a regulated-domain adapter lane.
- DESIGN: this roadmap keeps adapter, Policy_Local, and EC activation separate.
- SPEC: RDA-T1 locks adapter semantics before build.
- WORK ORDER: each tranche receives fresh GC-018 and source verification.
- BUILD: runtime/source work may begin only at RDA-T2.
- REVIEW: cross-domain conformance proves non-bleed.
- FREEZE: RDA-T4 releases only the next bounded use-case lane.

## Claim Boundary

This roadmap proves only a design direction and dispatch plan for a
regulated-domain adapter. It does not prove legal/current status, metadata
truth, source authenticity, OCR quality, retrieval quality, Policy_Local
readiness, EC activation, T12 readiness, provider behavior, production
readiness, public readiness, or autonomous correction.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private adapter roadmap and dispatch plan; no public-sync authorized.
