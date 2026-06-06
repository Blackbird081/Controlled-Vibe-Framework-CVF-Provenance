# CVF GC-018 LPCI1-T1 Supplement Baseline

Memory class: FULL_RECORD

Status: ACTIVE

docType: baseline

Date: 2026-06-03

executionBaseHead: `a155f505`

## Purpose

Satisfy the GC-018 baseline obligation for LPCI1-T1 Product Intake and
Architecture. This supplement extends the LPCI1 GC-018 parent baseline
(`docs/baselines/CVF_GC018_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_2026-06-02.md`)
with T1-specific gap acknowledgments (NR-04, NR-05, NR-11) and the T1
implementation boundary.

Per CI1-T7 intake bridge (lines 165-167), LPCI-T1 must explicitly acknowledge
the three inherited gaps and their post-CI2 dispositions before any
implementation begins.

---

## Source

| Predecessor | Path | Status |
| --- | --- | --- |
| LPCI1 GC-018 (parent) | `docs/baselines/CVF_GC018_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_2026-06-02.md` | ACTIVE |
| CI1-T7 LPCI intake bridge | `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` | ACTIVE |
| CI2-T4 pilot pack | `docs/corpus-intelligence/CVF_CI2_T4_PRODUCT_READINESS_PILOT_CORPUS_PACK.json` | CLOSED_PASS_BOUNDED |
| LPCI1-T1 work order | `docs/work_orders/CVF_WO_LPCI1_T1_PRODUCT_INTAKE_AND_ARCHITECTURE_2026-06-02.md` | DISPATCH_READY |
| NR-04 standard | `docs/reference/CVF_CORPUS_SOURCE_HASH_STANDARD_2026-06-02.md` | ACTIVE |
| NR-05 standard | `docs/reference/CVF_CORPUS_PATH_NORMALIZATION_ALGORITHM_STANDARD_2026-06-02.md` | ACTIVE |
| NR-11 standard | `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md` | ACTIVE |

---

## Decision

LPCI1-T1 is authorized as an architecture-only tranche with the following
binding decisions:

1. **NR-04 sourceHash adopted**: LPCI1 corpus intake adopts the CVF Corpus
   Source Hash Standard. Per-file SHA-256 is the preferred hash policy.
   Operator-documented manifest proxy is accepted per the conditions stated
   in `docs/reference/CVF_LPCI1_T1_CORPUS_INTAKE_SPEC_2026-06-02.md`.

2. **NR-05 normalizedPath adopted**: LPCI1 corpus intake adopts the CVF
   Corpus Path Normalization Algorithm Standard without modification.

3. **NR-11 dispositionAlias adopted**: LPCI1 classification pipeline must
   preserve `rawDisposition` and add `dispositionAlias: ACCEPT_DEFERRED`
   for all DEFER and ACCEPT_SUMMARY_ONLY rows.

4. **No runtime implementation in T1**: this tranche creates planning and
   architecture artifacts only. Zero UI, API, vector DB, embedding pipeline,
   or provider call files may be created.

5. **Architecture review required before T2 dispatch**: LPCI1-T2 may not be
   dispatched until this supplement, the architecture document, and the corpus
   intake spec are reviewed and the T1 completion review is closed.

---

## Gap Acknowledgment (NR-04, NR-05, NR-11)

Per `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` lines 169-173:

| gapId | T6/CI2 resolution | Post-CI2 status | LPCI1-T1 acknowledgment |
| --- | --- | --- | --- |
| NR-04 | STRUCTURAL_CHECK_REQUIRED — satisfied by CI2-T1/T2; standard: `CVF_CORPUS_SOURCE_HASH_STANDARD_2026-06-02.md`; checker: `check_corpus_packet_source_hash.py` | SATISFIED_BY_CI2_T1_T2 | ADOPTED — LPCI1 intake requires per-file SHA-256 or documented manifest proxy; policy declared in corpus intake spec; checker enforces at intake commit |
| NR-05 | STANDARD_REQUIRED_FIRST — satisfied by CSA1/CI2-T2; standard: `CVF_CORPUS_PATH_NORMALIZATION_ALGORITHM_STANDARD_2026-06-02.md`; checker: `check_corpus_packet_normalized_path.py` | SATISFIED_BY_CSA1_CI2_T2 | ADOPTED — LPCI1 intake uses same normalizedPath algorithm; no modification; checker enforces at intake commit |
| NR-11 | STANDARD_REQUIRED_FIRST — satisfied by CSA1/CI2-T2; standard: `CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md`; checker: `check_corpus_packet_disposition_canonical.py` | SATISFIED_BY_CSA1_CI2_T2 | ADOPTED — LPCI1 classification preserves `rawDisposition` and adds `dispositionAlias`; ACCEPT_DEFERRED for DEFER/ACCEPT_SUMMARY_ONLY rows; checker enforces at classification commit |

Non-blocking gaps (adopted or guidance-only):

| gapId | T6 decision | LPCI1-T1 stance |
| --- | --- | --- |
| NR-03-vocab | VOCABULARY_EXTENSION_REQUIRED — extension applied | CONTROL_PLANE_ADAPTERS in T4 vocabulary; LPCI may use it; no new extension needed for T1 |
| NR-06 | DOCUMENTATION_ONLY | per-row sensitivity declared in corpus intake spec; enforced from T2 |
| NR-07 | DOCUMENTATION_ONLY | optional `primaryLanguage`/`secondaryLanguages` fields may be used in T2 classification; no obligation in T1 |

---

## Evidence

Evidence confirming NR-04/NR-05/NR-11 gap closure before T1 implementation:

| Evidence type | Artifact | Verified state |
| --- | --- | --- |
| NR-04 standard | `docs/reference/CVF_CORPUS_SOURCE_HASH_STANDARD_2026-06-02.md` | ACTIVE |
| NR-04 checker | `governance/compat/check_corpus_packet_source_hash.py` | active autorun |
| NR-04 CI2-T4 proof | `docs/corpus-intelligence/CVF_CI2_T4_PRODUCT_READINESS_PILOT_CORPUS_PACK.json` | CLOSED_PASS_BOUNDED with `manifestHashProxy: true` |
| NR-05 standard | `docs/reference/CVF_CORPUS_PATH_NORMALIZATION_ALGORITHM_STANDARD_2026-06-02.md` | ACTIVE |
| NR-05 checker | `governance/compat/check_corpus_packet_normalized_path.py` | active autorun |
| NR-11 standard | `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md` | ACTIVE |
| NR-11 checker | `governance/compat/check_corpus_packet_disposition_canonical.py` | active autorun |
| T1 hash policy | `docs/reference/CVF_LPCI1_T1_CORPUS_INTAKE_SPEC_2026-06-02.md` | ACTIVE — NR-04 adoption declared |
| T1 architecture | `docs/reference/CVF_LPCI1_T1_ARCHITECTURE_2026-06-02.md` | ACTIVE |

---

## Scope / Applies To

Applies to: LPCI1-T1 architecture tranche and all subsequent LPCI tranches
until superseded by a later GC-018 supplement.

Owner surface: CVF governance layer; LPCI1-T1 worker and reviewer.

Out of scope: T2–T7 runtime implementation (each tranche opens its own work
order with a GC-018 supplement if required).

---

## Claim Boundary

This supplement claims:

- NR-04, NR-05, NR-11 gap acknowledgment and adoption for LPCI1-T1;
- T1 architecture-only implementation boundary;
- hash policy declaration for LPCI1 corpus intake.

This supplement does NOT claim:

- runtime implementation correctness;
- legal answer accuracy or production readiness;
- corpus completeness or currentness;
- embedding quality or vector index correctness.

---

## Finding-To-Governance Learning Disposition

Defect class: `RULE_GAP` — no T1-level GC-018 supplement existed prior to
this tranche

Learning lane: `GOVERNANCE_CONTROL_PLANE`

Disposition: `RULE_ADDED` — LPCI1-T1 GC-018 supplement satisfies CI1-T7
gap acknowledgment obligation (NR-04/NR-05/NR-11) and declares hash policy

Next control action: `OPEN` — T2 classification enforces these standards
at runtime

Runtime/provider/cost learning: `N/A_WITH_REASON`

Reason: planning baseline only; no provider calls, runtime changes, or cost.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: supplement references private internal governance chain and CI2
evidence; not suitable for public CVF repository at this stage.

Public-sync boundary: no artifacts from this batch are queued for public-sync.
