# CVF Metadata Evidence And Operator Resolution Foundation Roadmap

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-06-12

Owner: Codex

---

## Authorization / Decision

Decision: `FOUNDATION_FIRST_POLICYLOCAL_DOWNSTREAM`.

The operator authorized a roadmap that prioritizes reusable CVF foundation
work. Policy_Local remains the first real evidence corpus, but its six EC-T4
candidate records must not define the generic contract and must not be mutated
by this foundation roadmap.

EX-T1 through EX-T9 are closed bounded. This roadmap does not reopen EX. It
starts at the next reusable gap exposed by EC-T4: CVF can report a generic
finding, but it does not yet own a canonical, domain-agnostic contract for
metadata uncertainty, evidence basis, operator action, and downstream release.

## Purpose

Create a reusable CVF layer that can:

1. declare metadata requirements without hard-coding a domain;
2. classify missing, ambiguous, conflicting, or unsupported metadata;
3. record whether evidence came from source content, an operator, a derived
   hint, or no acceptable source;
4. produce deterministic machine-readable and operator-readable resolution
   packets;
5. retain downstream blocks until an explicit evidence-backed resolution is
   accepted;
6. prove that legal-policy and non-legal domains do not inherit each other's
   metadata fields or gate semantics.

Policy_Local will later consume this foundation as a real use case. It is not
the owner of the foundation contract.

## Architecture Position

The layer sits between extraction outcome reporting and domain/runtime
activation:

```text
SOURCE FILE
  -> EXTRACTION FOUNDATION
  -> SCAN OUTCOME REPORT
  -> METADATA EVIDENCE AND RESOLUTION CONTRACT
  -> OPERATOR CHECKPOINT WHEN REQUIRED
  -> DOMAIN PROFILE / GATE RE-EVALUATION
  -> RETRIEVAL OR OTHER DOWNSTREAM USE
```

The layer is governance infrastructure. It does not determine legal status,
technical correctness, document authenticity, or semantic truth. It records
what is known, why it is known, what remains unresolved, and whether downstream
work may proceed.

## Scope / Target / Owner Boundary

Target owners:

- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION` for scan-layer finding normalization
  and deterministic operator report integration;
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION` for profile-declared metadata
  requirements and downstream block/re-evaluation signals;
- `docs/reference` for the canonical contract and machine-readable semantics.

In scope:

- generic metadata requirement and finding vocabulary;
- evidence-basis and resolution-state semantics;
- deterministic JSON/Markdown operator packets;
- explicit downstream retain-block or re-evaluate signals;
- profile-driven requirements with no global domain defaults;
- legal-policy and technical-project conformance fixtures;
- focused tests, registry coverage, completion evidence, and continuity.

Out of scope:

- changing any file in the external Policy_Local workspace;
- correcting CAND-001 through CAND-006;
- installing OCR dependencies or models;
- ingesting a real corpus;
- deciding legal/current status;
- activating EC-T5, EC-T6, T12, or retrieval;
- provider/API-key use, public-sync, production, or public readiness.

## Non-Goals

This roadmap does not:

- infer required metadata from document text;
- treat filename values as verified evidence;
- make operator input equivalent to source-embedded evidence;
- promote unresolved records automatically;
- create a universal metadata schema for all domains;
- require regulatory dates for non-regulatory domains;
- claim that a report proves source authenticity or output quality;
- authorize autonomous correction or mutation.

## Authority Chain

| Authority | Path or decision | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-12 foundation-first roadmap; Policy_Local remains downstream use case | ACCEPT |
| EX-T9 completion | `docs/reviews/CVF_LPCI2_EX_T9_OPERATOR_VISIBLE_SCAN_OUTCOME_REPORT_COMPLETION_2026-06-12.md` | ACCEPT |
| EC-T4 gap report | `docs/reference/CVF_LPCI2_EC_T4_OPERATOR_METADATA_GAP_REPORT_2026-06-12.md` | ACCEPT_AS_USE_CASE_EVIDENCE |
| Existing EX report source | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | ACCEPT |
| DSCP profile contract | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | ACCEPT |
| EC-02 semantics | `docs/reference/CVF_EC02_GATE_SEMANTICS_2026-06-11.json` | ACCEPT_AS_REGULATED_DOMAIN_EXTENSION |
| Governed lifecycle standard | `docs/reference/CVF_GOVERNED_WORK_LIFECYCLE_AND_DESIGN_CONTROL_STANDARD_2026-06-11.md` | ACCEPT |

## Current Runtime Freshness Verification

Verified at base `618cee29`:

```text
EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py
EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts
docs/reference/CVF_EC02_GATE_SEMANTICS_2026-06-11.json
```

Observed:

- EX-T9 exposes `ScanOutcomeFinding`, but `code`, `required_action`, and
  `evidence` are caller-supplied strings without a metadata-resolution schema.
- EX-T9 can append generic findings and render deterministic JSON/Markdown.
- DSCP profiles carry generic metadata maps, gate keys, boundary rules, and the
  optional regulated-domain flag `supportsDocumentStatus`.
- EC-T3 added PolicyLocal-specific `DocumentStatus`, `promulgationDate`, and
  `effectiveDate` fields to LPCI record types.
- No source-verified generic metadata evidence contract, operator resolution
  record, or cross-domain metadata requirement declaration exists.

## Gap Statement

The current system has two valid but disconnected surfaces:

1. EX-T9 can display a finding supplied by a caller.
2. EC-T4 can document Policy_Local metadata gaps manually.

The reusable missing layer is a governed contract connecting those surfaces.
Without it, each domain can invent finding codes, evidence labels, operator
actions, and release semantics. That creates inconsistent reports and makes it
too easy for a domain-specific assumption to bleed into CVF foundation.

## Design Control Gate

Design verdict: `PASS_BOUNDED`.

Selected design:

1. Define the contract and machine semantics before runtime implementation.
2. Keep requirement declarations profile-scoped rather than global.
3. Separate observed metadata state from evidence basis.
4. Separate resolution state from downstream release state.
5. Reuse EX-T9 report rendering instead of building a parallel reporter.
6. Require cross-domain conformance before foundation closure.
7. Keep Policy_Local correction and activation in a later use-case roadmap.

Rejected design:

- adding Policy_Local candidate IDs or Vietnamese legal fields to foundation;
- treating `documentStatus` as a global CVF metadata requirement;
- automatically accepting operator values without provenance;
- letting report generation directly mutate descriptors or domain profiles;
- activating `QUERY_CLASS_GATED` as part of metadata reporting;
- reopening EX for OCR installation or corpus ingestion.

## Required Contract Semantics

T1 must lock exact names and machine values before implementation. At minimum,
the contract must distinguish:

- metadata requirement identity and owning domain profile;
- observed state: present, missing, ambiguous, conflicting, unsupported, or
  not applicable;
- evidence basis: source-embedded, operator-supplied, derived hint, or none;
- resolution state: resolved, operator action required, or blocked;
- required operator action and acceptable evidence classes;
- downstream disposition: retain block or eligible for re-evaluation;
- evidence pointer and provenance without raw source-content release;
- explicit claim boundary and autonomous-mutation prohibition.

These are design requirements, not approved field or enum names. T1 must
source-verify existing symbols and declare all new values as new contract
surface before a worker may implement them.

## Lane Split

### Lane F - CVF Foundation

Lane F owns the reusable contract, implementation, integration, and
cross-domain proof. It is the only active lane in this roadmap.

### Lane R - Regulated-Domain Adapter

Lane R maps regulated-date concepts such as `documentStatus`,
`promulgationDate`, and `effectiveDate` into the generic foundation contract.
It remains held until Lane F closes.

### Lane P - Policy_Local Real Use Case

Lane P resolves the six Policy_Local candidate records, performs real OCR or
ingestion when separately authorized, and tests EC/retrieval quality. It
requires a separate roadmap and remains held until Lane F closes and operator
evidence exists.

## Tranche Plan

| Tranche | Deliverable | Dependency | Status |
| --- | --- | --- | --- |
| MEOR-T1 | Canonical contract plus machine-readable semantics for metadata evidence, operator resolution, and downstream disposition | this roadmap | CLOSED_PASS_BOUNDED at `f3c7ff11` |
| MEOR-T2 | Extraction-foundation implementation that normalizes metadata findings and feeds the existing EX-T9 report surface | MEOR-T1 completion at `22818605` plus sync `662e3c76` | CLOSED_PASS_BOUNDED at `d18a3e47` |
| MEOR-T3 | DSCP profile requirement bridge with profile-scoped declarations and no cross-domain default injection | MEOR-T2 completion `69ec7574` and sync `472c474d` | CLOSED_PASS_BOUNDED at `0c4997a5` |
| MEOR-T4 | Cross-domain conformance suite using legal-policy and technical-project synthetic fixtures | MEOR-T3 material `0c4997a5`, closure `5f328d11`, and sync `7b2204dc` | CLOSED_PASS_BOUNDED at `bfd38775` |
| MEOR-T5 | Foundation closure, registry/continuity sync, and downstream readiness decision | MEOR-T4 material `bfd38775`, closure `0098de68`, and sync `390f5426` | CLOSED_PASS_BOUNDED |
| EC-ADAPTER successor | Map regulated-date metadata into the generic contract | MEOR-T5 closed plus fresh authorization | READY_FOR_FRESH_AUTHORIZATION |
| Policy_Local validation successor | Resolve real candidate evidence and test integration | MEOR-T5 closed plus operator evidence and separate roadmap | NOT_OPEN |

## Work Plan

1. Author MEOR-T1 as a specification-only GC-018 and source-verified work
   order.
2. Lock machine semantics, invalid combinations, fail tokens, and examples.
3. Review and close T1 before authoring any implementation work order.
4. Implement scan-layer normalization and EX-T9 report integration in T2.
5. Add profile-scoped requirement declarations in T3 without global defaults.
6. Prove cross-domain isolation and deterministic outcomes in T4.
7. Close the foundation and issue a bounded downstream readiness decision in
   T5.
8. Open regulated-domain or Policy_Local successors only through fresh
   operator authorization, GC-018, source verification, and work orders.

Dependency release rule: each held tranche must cite the predecessor completion
artifact and closure commit, refresh its dispatch base, and pass pre-dispatch
autorun. Chat history or this roadmap table alone is not release evidence.

## MEOR-T1 First Dispatch Target

The first child packet is specification-only.

Required outputs:

- fresh GC-018 baseline;
- source-verified work order;
- canonical Markdown contract;
- machine-readable JSON semantics;
- conformance examples for one regulated and one non-regulated profile;
- explicit new-field table;
- no runtime/source implementation.

T1 must not ask a worker to invent fields while coding. Exact values, invalid
combinations, fail tokens, and release rules must be locked in the spec first.

## Dispatch Boundary

MEOR-T1 may authorize only:

- contract and machine-semantics authoring;
- source verification of EX-T9, DSCP profile, and existing EC/LPCI fields;
- synthetic examples;
- governance tests or checkers needed to validate the contract artifacts;
- completion review and continuity updates.

MEOR-T1 must not authorize:

- Python or TypeScript runtime implementation;
- external Policy_Local changes;
- candidate metadata correction;
- OCR execution or dependency installation;
- corpus ingestion;
- EC-T5/EC-T6/T12 release;
- retrieval behavior;
- provider/API-key use;
- public-sync or readiness claims.

## Acceptance Criteria

Foundation acceptance requires all of the following:

1. A canonical machine-readable contract exists before implementation.
2. Requirement ownership is profile-scoped, not globally inferred.
3. Evidence basis distinguishes source, operator, hint, and absent evidence.
4. Missing, ambiguous, and conflicting states remain blocked.
5. Operator-supplied resolution retains provenance and does not masquerade as
   source-embedded evidence.
6. Downstream release is explicit and never implied by report generation.
7. EX-T9 remains the report renderer; no duplicate reporting pipeline appears.
8. No raw OCR text, chunk text, or sensitive source content is emitted.
9. Legal-policy requirements do not appear in technical-project output.
10. Technical-project requirements do not appear in legal-policy output.
11. Synthetic conformance tests cover resolved, unresolved, conflict, and
    not-applicable paths.
12. Policy_Local files and candidate records remain unchanged.
13. Focused tests, registry checks, reviewer-fast, and closure gates pass.

## Verification And Evidence Plan

- JSON parse and schema/value conformance for T1 semantics;
- source-verification table for every existing symbol;
- focused Python tests for finding normalization and report integration;
- focused TypeScript tests for profile-scoped requirements;
- cross-domain synthetic fixtures and negative bleed assertions;
- deterministic report equality checks;
- raw-content non-release assertions;
- changed-path proof excluding external Policy_Local;
- GC-051 registry coverage for new source and test corpora;
- reviewer-fast, pre-implementation, pre-closure, and pre-push gates as
  applicable.

No live provider proof is required because this roadmap authorizes local,
deterministic control-plane behavior only. Any later claim about governed AI
behavior or Policy_Local answer quality requires the applicable live proof.

## Stop Conditions

Stop and return to orchestrator if:

- T1 cannot define a domain-agnostic contract without legal-specific fields;
- implementation requires changing Policy_Local or ingesting its corpus;
- a proposed requirement becomes a global default across unrelated profiles;
- operator evidence would be silently promoted to source evidence;
- report generation would mutate a profile, descriptor, corpus, or retrieval
  index;
- EC activation, query routing, or current-status claims become necessary;
- a new dependency, provider call, secret, or external service is required;
- source verification finds that an assumed owner surface does not exist.

## Governed Work Lifecycle

`INTAKE -> DESIGN -> SPEC -> WORK ORDER -> BUILD -> REVIEW -> FREEZE`

- INTAKE: EC-T4 exposes a reusable control gap through Policy_Local evidence.
- DESIGN: this roadmap separates foundation, regulated adapter, and use case.
- SPEC: MEOR-T1 locks contract semantics and invalid combinations.
- WORK ORDER: each tranche receives fresh GC-018 and source verification.
- BUILD: implementation starts only at MEOR-T2.
- REVIEW: focused and cross-domain tests prove bounded behavior.
- FREEZE: MEOR-T5 records closure and releases only the next authorized lane.

## Claim Boundary

This roadmap proves only a design direction for metadata evidence and operator
resolution governance. It does not prove metadata correctness, source
authenticity, semantic understanding, legal/current status, OCR quality,
retrieval quality, Policy_Local readiness, production readiness, public
readiness, or autonomous correction.

## Closure Decision

MEOR foundation is closed bounded at T5. The released next move is a fresh
regulated-domain adapter roadmap, GC-018 baseline, and source-verified work
order. Policy_Local remains downstream and must not be updated until the
adapter and operator/source metadata evidence path are separately authorized.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Roadmap state | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_MEOR_T5_FOUNDATION_CLOSURE_AND_DOWNSTREAM_READINESS_COMPLETION_2026-06-12.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_MEOR_T5_FOUNDATION_CLOSURE_FOR_CODEX_2026-06-12.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Baseline status | `docs/baselines/CVF_GC018_MEOR_T5_FOUNDATION_CLOSURE_AND_DOWNSTREAM_READINESS_2026-06-12.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | N/A with reason: no new runtime/source corpus | no registry change because T5 creates no corpus/search/classification source | BLOCKED with reason |
| Registry Markdown | N/A with reason: no new runtime/source corpus | no registry change because T5 creates no corpus/search/classification source | BLOCKED with reason |
| External evidence digest | N/A with reason: private repo-local foundation closure | no external evidence | N/A with reason |
| System loop interlock | N/A with reason: no loop mutation | docs-only closure | N/A with reason |
| Session continuity | active state, memory, and handoff | adapter roadmap next | PASS |

## Foundation / Use-Case Boundary

CVF foundation owns:

- contract vocabulary;
- evidence provenance;
- resolution and downstream disposition;
- profile-scoped requirements;
- deterministic operator packets;
- cross-domain non-bleed tests.

Policy_Local owns:

- the six real candidate files and their corrections;
- operator-confirmed legal metadata;
- OCR and corpus ingestion for that application;
- EC activation and retrieval-quality validation;
- user-interface integration and domain-specific wording.

A Policy_Local finding may motivate a reusable CVF control, but the control
must close with domain-agnostic semantics and cross-domain evidence.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private foundation roadmap and pre-spec design record; no public-sync
artifact or public claim is authorized.
