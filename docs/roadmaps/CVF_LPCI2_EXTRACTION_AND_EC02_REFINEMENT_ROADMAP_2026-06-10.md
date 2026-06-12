# CVF Corpus Extraction Foundation And Regulatory Date Model Roadmap

Memory class: FULL_RECORD

Status: ACTIVE_PARTIAL_EX_T8_CLOSED_EC_BLOCKED

docType: roadmap

Date: 2026-06-10

Author: Claude (operator-directed proposal for Codex review and explicit operator authorization)

---

## Authorization And Decision

Decision state: EX_T8_CLOSED_EC_BLOCKED.

Operator instruction on 2026-06-11 authorized Codex to author the next work
order under the hardened design-control foundation. EX-T1 is now completed as a
dependency/source audit child lane.

EX-T1 review accepted the recommendation `COMPOSED_STACK_PREFERRED` for the
EX-T2 Tier 1 digital-native extraction lane only. LiteParse remains
`LITEPARSE_ELIGIBLE_FOR_EX_T3_REEVALUATION` for a later OCR/spatial tradeoff
decision. EX-T2 is now closed pass bounded through fresh GC-018 authorization,
a source-verified work order, focused tests, and Codex completion review.

This records closure of the bounded EX-T2 Tier 1 digital-native extractor
implementation, EX-T3 through EX-T8 local extraction pipeline foundation,
EC-T1 regulatory date/status decision baseline, EC-T2 contract amendment plus
machine-readable EC-02 semantics JSON, EC-T3 TypeScript corpus schema fields,
EC-T4 parked evidence/backfill proposal, and EC-T5 bounded block decision.
It does not authorize repo dependency addition, OCR model download, corpus
ingestion, runtime retrieval behavior change, DSCP profile value update,
public-sync, or live/provider proof. Any later child lane must receive fresh
GC-018 authorization and a source-verified work order before execution release.

EC-T4 reviewer disposition on 2026-06-11: `RETURNED_BLOCKED_METADATA_GAPS`.
Two records are source-evidenced pending operator type/status confirmation;
four records require operator-confirmed signed dates/document numbers before
metadata backfill or EC-T5 can proceed.

EC-T5 reviewer disposition on 2026-06-11: `CLOSED_BLOCKED_BOUNDED`.
`QUERY_CLASS_GATED` was not applied to DSCP domain profiles because EC-T4
remains parked and the current CPF profile apply contract would treat the token
as a non-blocking custom gate before runtime/query-class routing is wired.

EX-T3 through EX-T8 reviewer disposition through 2026-06-12:
`CLOSED_PASS_BOUNDED`. CVF now has a local deterministic extraction pipeline
foundation for OCR adapter boundaries, OCR language-code mapping, confidence
capture, extraction quality reports, fixed-window and sentence-boundary chunks,
authority/rebuild metadata, storage-boundary records, DSCP descriptor input
handoff records, and GC-051 registry coverage. This closure does not install
OCR dependencies, download OCR models, ingest corpus files, call providers,
mutate external Policy_Local, or claim legal/current-status quality.

---

## Architecture Position

This roadmap delivers two CVF foundation capabilities. Neither is specific to
PolicyLocal or to any particular language.

**Extraction Pipeline (Part A)** is a CVF-layer capability: read any
`.docx` or `.pdf` file - regardless of domain, language, or purpose -
extract its text, chunk it, apply quality gates, and hand the result to
the DSCP pipeline. PolicyLocal is the first project that needs it, but
the pipeline belongs to CVF core, not to PolicyLocal.

**Regulatory Date Model / EC-02 Refinement (Part B)** is a CVF governance
rule that applies to any corpus domain where documents have a promulgation date
and a separate effective date. Not Vietnamese-law-specific. Applies equally
to EU directives, ISO standards, corporate policy releases, or any regulated
document type in any language.

**Core language principle - Language Transparency:**

CVF scan, extraction, memory, and retrieval layers are language-transparent.
They do not detect, normalize, translate, or make judgments about the natural
language of content. Language is an operator-declared attribute of a corpus
(`DscpDomainProfile.languageCodes`), not a property CVF infers from text.

```text
Input Vietnamese text   -> processed as-is   -> output Vietnamese text
Input English text      -> processed as-is   -> output English text
Input bilingual text    -> processed as-is   -> output bilingual text
```

CVF does not read language from content. It reads language from the domain
profile that the operator registered for that corpus. A corpus declared as
`["vi", "en"]` carries that declaration on every chunk - CVF does not
re-detect or validate it. The only place `languageCodes` drives behavior is
the OCR engine parameter selection in Tier 2 extraction, after a source-verified
mapping from DSCP language codes to extractor-specific OCR language codes.

**Agent communication standard (orthogonal rule, no conflict):**

CVF governance specs, work orders, contracts, and roadmaps are authored in
English. AI agents (Claude, Codex) parse and implement more accurately in
English - this is a known property of current LLM training data distribution,
not a preference. This rule applies to Tier 1 (agent instructions) and does
not touch Tier 2 (corpus content). A Vietnamese legal document corpus is
processed with full language transparency; the work order instructing an agent
to build that pipeline is written in English. The two rules coexist without
conflict because they operate on different objects.

---

## Purpose

Two gaps exist at the CVF foundation layer that block any real-document corpus
project from reaching retrieval:

1. **Extraction gap** - CVF has no mechanism to convert `.docx` and `.pdf`
   files (including scanned-image PDFs) into governed plain-text chunks. Without
   extraction, corpus records are hash-only. Hash-only records cannot be searched,
   retrieved, or answered against. This blocks all corpus projects, not only
   PolicyLocal.

2. **Regulatory date model gap** - The current EC-02 gate is a binary date
   block. This is incorrect for any document system where signing/publication
   date and operative/effective date are independent events. The pattern appears
   in every regulated domain: law, standards, policy, compliance frameworks.
   EC-02 as currently written blocks content reading when it should only block
   applicability claims.

This roadmap proposes a phased solution. It is a PROPOSAL for Codex rebuttal
and explicit operator authorization before execution release.

---

## Scope

In scope for this parent roadmap:

- define why CVF needs a reusable document extraction foundation for scan-layer
  corpus work;
- define the first evidence gates for dependency selection and local extraction
  feasibility;
- define why EC-02 needs a regulatory date model before T12-style current-law
  readiness can be revisited;
- define the required split between extraction implementation and EC-02
  retrieval-governance semantics.

Out of scope for this parent roadmap:

- releasing a worker packet;
- selecting a final OCR/parser dependency;
- changing runtime retrieval behavior;
- changing public-facing docs or public-sync;
- claiming PolicyLocal legal quality, current-law status, hosted readiness, or
  production readiness.

---

## Non-Goals

This roadmap does NOT claim:

- production deployment or public readiness for any project;
- legal advice quality or current-law status;
- provider calls, API keys, or LLM inference during extraction;
- OCR output as authoritative text for any regulated purpose;
- any corpus expansion before operator re-authorization per project;
- weakening EC-01 (legal advice), EC-03 (interpretation), EC-04 (compliance).

All extraction output must flow through the DSCP pipeline
(domain profile, descriptor, gate, receipt) before any retrieval use.

---

## Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Operator instruction | 2026-06-10 - two foundation gaps identified; roadmap as CVF-layer capability | SUPERSEDED_BY_CHILD_CLOSURES |
| LPCI2 productization roadmap | `docs/roadmaps/CVF_LPCI2_POLICYLOCAL_PRODUCTIZATION_ROADMAP_2026-06-03.md` | DOWNSTREAM_CONSUMER |
| T11 corpus expansion readiness | `docs/roadmaps/CVF_LPCI2_T11_POLICYLOCAL_CORPUS_EXPANSION_READINESS_ROADMAP_2026-06-07.md` | DOWNSTREAM_CONSUMER |
| LPCI response boundary contract | `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-04.md` | TARGET_OF_EC02_CHANGE |
| DSCP domain profile contract | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | INTEGRATION_POINT |
| DSCP profile selection adapter | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.profile.selection.adapter.ts` | INTEGRATION_POINT |

---

## Claim Boundary

This roadmap is a planning artifact only. It records a CVF foundation direction
and release prerequisites. It does not prove an extraction runtime, dependency
fitness, OCR quality, legal status accuracy, retrieval quality, EC-02 runtime
behavior, T12 eligibility, public readiness, production readiness, or release
readiness.

---

## Historical Release Boundary

This parent roadmap is a planning and closure coordination record, not a
standalone worker implementation order. It split into two separately governed
child lanes before worker execution:

- EX lane: CVF scan/extraction foundation for document-to-chunk processing.
- EC lane: EC-02 regulatory date model and retrieval-gate semantics.

The EX lane improves the CVF scan layer by turning file-level corpus assets
into governed text chunks with extraction provenance, quality flags, and DSCP
receipts. The EC lane improves response eligibility and disclosure semantics
after chunks exist. The two lanes may be planned together, but implementation
and closure evidence must stay separately attributable unless a later explicit
integration tranche joins them.

---

## Work Plan

The work plan is intentionally split into two lanes:

- EX lane first release target: EX-T1 dependency and source audit only.
- EC lane first release target: EC-T1 governance decision record only.

No implementation tranche may start until its preceding audit/decision tranche
is closed and a fresh work order cites the closure evidence. EX and EC closure
evidence must remain separate until an explicit integration tranche joins them.

---

## Acceptance Criteria

Historical release criteria for child-lane execution:

- EX-T1 work order includes source verification for dependency install,
  supported input formats, OCR language-code mapping, local and CI feasibility,
  and no runtime extraction claim beyond audit.
- EC-T1 work order includes source verification for EC-01/EC-02/EC-03/EC-04,
  answer-class vocabulary, corpus schema owner, response-boundary owner, and
  DSCP `boundaryRules` / `ec02Gate` ownership.
- No implementation tranche combines EX and EC scopes in one work order before
  an explicitly authorized integration tranche.
- Any machine-gate failure inside the assigned work order's allowed scope is
  repaired and rerun by the assigned agent before return.
- Any dependency, OCR model, parser, runtime field, or schema key named in a
  child work order is source-verified before execution release.
- Public Export Disposition remains `DEFERRED_PRIVATE_ONLY` unless public-sync
  remote, commit, and artifact-path evidence exists.

---

## Verification And Evidence

Before any child work order execution release, the orchestrator must capture a real
`baseHead` and run:

```bash
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base <baseHead> --head HEAD
python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast
```

Minimum EX-T1 evidence:

- official dependency source links or local package metadata for each candidate;
- local install/import probe results for the target environment;
- OCR language-code mapping evidence for DSCP `languageCodes`;
- explicit no-secret/no-provider-proof boundary.

Minimum EC-T1 evidence:

- grep-backed source map for current EC vocabulary, response-boundary contract,
  corpus schema owner, and DSCP profile fields;
- decision record for whether `QUERY_CLASS_GATED` is accepted, renamed, or
  rejected before runtime use;
- machine-readable gate-semantics artifact plan before any EC-T5 runtime wire-in.

---

## Source Verification And Dependency Evidence Needed

This proposal references dependency tools and new runtime fields. Before any
work order is released for execution, the child work order must include a source
verification table with current evidence for every tool, package, runtime
field, and schema key it uses.

Dependency claims in this roadmap are governed by the repo-local EX-T1 audit
artifacts and their External Evidence Digest. LiteParse remains a deferred
candidate recorded in the EX-T1 audit, not an accepted dependency for this
EX-T3 through EX-T6 closure.

Minimum EX-T1 source checks:

- `liteparse` Python installation path and whether prebuilt wheels exist for
  the target OS/Python versions;
- LiteParse input-format support for `.pdf`, `.docx`, images, and whether
  `.docx` requires LibreOffice conversion;
- LiteParse OCR language parameter format and Tesseract traineddata
  requirements;
- EasyOCR language-code format and model download behavior;
- `pdfplumber`, `python-docx`, `pdf2image`, poppler, and EasyOCR installation
  constraints in local Windows and CI environments.

Minimum EC-T1 source checks:

- current corpus record schema owner;
- current response boundary contract owner;
- existing EC-01/EC-02/EC-03/EC-04 vocabulary and answer-class vocabulary;
- current DSCP `boundaryRules` type and accepted `ec02Gate` values.

---

## Part A - CVF Corpus Extraction Foundation

### Problem Statement

Any corpus project that ingests `.docx` or `.pdf` files hits the same wall:
CVF has no extraction layer. Files are hashed at intake and marked
`DEFERRED_*_TEXT_EXTRACTION`. Text extraction is a prerequisite for every
downstream capability: chunking, search indexing, retrieval, answer generation.

Two structural file classes exist, and they are language-independent:

```
Class 1: Digital-native (text layer present)
  .docx  -> python-docx extracts document text directly
  .pdf   -> pdfplumber extracts the PDF text layer directly
  Result: no OCR loss, but still subject to layout/order quality gates

Class 2: Scanned image (no text layer)
  .pdf where pages are rasterized photographs of paper
  -> pdfplumber returns empty string or garbage characters
  -> must render pages as images, then OCR
  Result: text quality depends on scan resolution and OCR model
```

Detection of Class 2 is automatic: if Tier 1 extraction returns fewer than
`MIN_CHARS` per page on average, the pipeline escalates to Tier 2 without
operator intervention.

### Implementation Options (pending EX-T1 evaluation)

Two candidate implementation stacks exist. EX-T1 (dependency audit) must
evaluate both before the operator selects one. Neither is committed yet.

#### Option 1 - Composed stack (python-docx + pdfplumber + EasyOCR)

Build the 3-tier pipeline from individual, well-understood Python libraries:

```text
Tier 1 (digital-native): python-docx (.docx) + pdfplumber (.pdf text layer)
Tier 2 (scanned OCR):    pdf2image (render pages) + EasyOCR (OCR, 90+ langs)
Tier 3 (quality gate):   custom quality_gate.py
```

| Dimension | Assessment |
| --- | --- |
| Language support | EasyOCR: 90+ languages, ISO 639-1 codes, runtime param |
| Setup | Multiple pip installs + system deps (poppler for pdf2image) |
| CI compatibility | No Rust compilation; Python-only; standard CI |
| Output | Plain text per page; no spatial metadata |
| Vendor lock | Low - each lib replaceable independently |
| Maturity | Each lib is widely used and well-documented |
| Risk | More moving parts; manual Tier 1 to Tier 2 escalation logic needed |

#### Option 2 - LiteParse (run-llama/liteparse)

Single unified library: Rust core, Python bindings, Apache 2.0 license.
Source: EX-T1 dependency/source audit External Evidence Digest.

```text
Tier 1+2 (unified): LiteParse
  - PDFium C library: native PDF text extraction
  - Tesseract: built-in OCR path, with OCR language parameter
  - EasyOCR / PaddleOCR via HTTP API: optional OCR server path
Tier 3 (quality gate): custom quality_gate.py (same as Option 1)
```

| Dimension | Assessment |
| --- | --- |
| Language support | Tesseract: 100+ languages; EasyOCR/PaddleOCR via HTTP: 90+ |
| Setup | Single `pip install liteparse`; Rust binary bundled |
| CI compatibility | Provisional: EX-T1 must verify whether target installs use prebuilt wheels or require Rust build tooling |
| Output | JSON: text + bounding boxes + font metrics + OCR confidence per item |
| Vendor lock | Moderate - unified lib; but pluggable OCR via HTTP API |
| Maturity | Newer library (run-llama ecosystem); less battle-tested than pdfplumber |
| Risk | Rust compilation complexity; LibreOffice optional dep (~300MB) |
| Advantage | Spatial layout (bounding boxes) enables future chunk-by-section splitting |

**Comparison matrix:**

| Criterion | Option 1 (Composed) | Option 2 (LiteParse) | Weight |
| --- | --- | --- | --- |
| CI/CD compatibility | High (pure Python) | Unknown (Rust build) | HIGH |
| Setup simplicity | Medium (multiple libs) | High (single install) | MEDIUM |
| OCR quality | Good (EasyOCR) | Good (Tesseract bundled) | MEDIUM |
| Output richness | Basic (text only) | Rich (spatial + confidence) | LOW now, HIGH future |
| Language transparency | Full | Full | REQUIRED (both pass) |
| Offline deployment | Needs poppler install | Needs Rust + traineddata | MEDIUM |
| Library maturity | High | Lower (newer) | MEDIUM |
| Future upgrade path | Manual lib swap | HTTP OCR swap with adapter validation | MEDIUM |

**Decision gate:** EX-T1 must answer before option is chosen:

1. Can the CI environment compile Rust at build time? (blocks Option 2 if NO)
2. Is LibreOffice available or installable? (Option 2 only)
3. Is poppler installable for pdf2image? (Option 1 only)
4. What is the offline/air-gapped deployment constraint, if any?
5. Is spatial output (bounding boxes) a near-term requirement, or deferred?

If CI cannot support Rust: **Option 1 is default**.
If CI supports Rust and spatial output is valued: **Option 2 is preferred**.
The dependency choice is made only after EX-T1 evidence and explicit governance
authorization.

### Architecture: 3-Tier Extraction Pipeline

```
INPUT: file path  +  DscpDomainProfile
                     (provides languageCodes, domainFamily, schema owner)
    |
    +--[.docx]--------> Tier 1: python-docx
    |
    +--[.pdf]---------> Tier 1: pdfplumber
                             |
                    char_count/page >= MIN_CHARS?
                             |
              YES -----------+--------------- NO (scan detected)
               |                               |
               |                         Tier 2: pdf2image
               |                         + OCR engine using mapped OCR language codes
               |                         confidence_score per page recorded
               |                               |
               +-------------------------------+
                                   |
                            Tier 3: Quality Gate
                        char_count/page >= MIN_CHARS?    -> else PARTIAL_EXTRACTION flag
                        OCR confidence >= 0.75?          -> else OCR_LOW_CONFIDENCE flag
                        page_coverage >= 80%?            -> else PARTIAL_EXTRACTION flag
                                   |
                      Governed chunk records (JSON)
              chunkId | sourceHash | text | tier | confidence
              extractionMethod | pageRange | languageCodes | flags[]
              ocrLanguageCodes | languageCodes copied from domain profile
                                   |
                         DSCP pipeline entry point
              domain profile -> descriptor -> gate -> receipt
```

### Key Design Decisions

**OCR language is a runtime parameter after deterministic mapping.**
`DscpDomainProfile.languageCodes` are CVF profile values, not necessarily
extractor-native OCR values. EX-T1 must source-verify and implement a mapping
table before any OCR execution release. Example shape:

| CVF profile code | EasyOCR candidate | Tesseract/LiteParse candidate | Status |
|---|---|---|---|
| `en` | `en` | `eng` | EX-T1_VERIFY |
| `vi` | `vi` | `vie` | EX-T1_VERIFY |

The extraction pipeline must not infer language from content. It must copy
profile `languageCodes` into chunk metadata and separately record the mapped
`ocrLanguageCodes` actually passed to the selected OCR engine.

**Language is carried from the domain profile, never inferred from content.**
The chunk record carries `languageCodes` copied directly from the domain
profile. CVF does not run language detection on extracted text. If the
operator registers a corpus with `["vi", "en"]`, every chunk from that
corpus carries `["vi", "en"]` - regardless of what language any individual
chunk happens to contain. CVF does not re-detect, validate, or second-guess
the operator-declared language.

**Bilingual content needs no special handling.**
A document with mixed Vietnamese and English text is extracted, chunked,
and stored exactly like any other document. The `languageCodes` field on
each chunk reflects the profile declaration. Retrieval returns whatever
text was extracted - in whatever language it is - without transformation.

**Flags are non-blocking metadata.**
`OCR_LOW_CONFIDENCE`, `PARTIAL_EXTRACTION` - carried in the chunk record
and surfaced in retrieval receipts. The retrieval layer must disclose flags.
It must not silently suppress or promote flagged chunks.

### Quality Gates

| Gate | Threshold | Rationale | Fail action |
| --- | --- | --- | --- |
| `MIN_CHARS` | 100 chars/page average | Readable content signal - language-independent | Auto-escalate to Tier 2 OCR |
| `OCR_CONFIDENCE` | >= 0.75 mean score | OCR output quality - language-independent | Flag `OCR_LOW_CONFIDENCE` |
| `PAGE_COVERAGE` | >= 80% pages with output | Completeness signal - language-independent | Flag `PARTIAL_EXTRACTION` |

CVF does not inspect or judge the natural language of extracted text.
No language-content gate exists. Language is declared by the operator
via the domain profile, not inferred from text.

### Proposed Tranches

| Tranche | Goal | Key output | Depends on |
|---|---|---|---|
| EX-T1 | Dependency and source audit | Option evidence, local install probes, CI feasibility note, OCR language-code mapping table | PASS_BOUNDED |
| EX-T2 | Tier 1 digital-native extractor | extractor owner module for `.docx` and PDF text-layer path | CLOSED_PASS_BOUNDED |
| EX-T3 | Tier 2 OCR fallback boundary | Local OCR adapter boundary, language-code mapping, and confidence capture | CLOSED_PASS_BOUNDED |
| EX-T4 | Tier 3 quality gate and chunk schema | Deterministic extraction quality report and fixed-window chunk schema | CLOSED_PASS_BOUNDED |
| EX-T5 | DSCP descriptor input handoff | Chunks become descriptor-shaped inputs with `rawContentReleased=false`; no profile apply/runtime receipt claim | CLOSED_PASS_BOUNDED |
| EX-T6 | GC-051 coverage | Extraction pipeline source/test corpus records added to GC-051 registry | CLOSED_PASS_BOUNDED |
| EX-T7 | Sentence-boundary chunking upgrade | Optional `sentence-boundary-chars` strategy with fixed-window fallback and offset trace metadata; fixed-window default preserved | CLOSED_PASS_BOUNDED |
| EX-T8 | Extraction authority and storage boundary | `ExtractionAuthorityLevel`, `RebuildClass`, `raw_ocr_retained`, `ExtractionStorageBoundary`, boundary hash, and descriptor metadata propagation; operator correction report remains successor EX scope | CLOSED_PASS_BOUNDED |

### Open Questions for Codex Rebuttal

1. **EasyOCR vs Tesseract**: EasyOCR supports many languages with a single
   pip install; Tesseract requires per-language `traineddata` files downloaded
   separately. EasyOCR is preferred for a language-agnostic pipeline. Codex
   should confirm model download size is acceptable in
   the CI and offline deployment environments.

2. **Chunking strategy**: Fixed-size windows (512 chars) vs sentence-boundary
   chunking. EX-T4 closed with fixed-window chunks. EX-T7 closed a bounded
   deterministic sentence-boundary upgrade that uses punctuation/newline
   boundaries with fixed-window fallback for long spans. Multilingual ML
   sentence splitting remains out of scope unless separately authorized.

3. **Raw OCR storage**: EX-T8 resolved this as bounded pipeline behavior. The
   pipeline does not persist raw OCR intermediates. Callers may capture
   `Tier2OcrPageResult` outside the pipeline and record that fact through
   `raw_ocr_retained`.

4. **Mixed-language chunk handling**: When a single PDF page contains multiple
   languages, should the pipeline simply carry profile-declared `languageCodes`
   or should it add an operator-declared `mixedContentExpected` flag?
   Recommendation: carry profile-declared `languageCodes` only for EX-T4;
   content-level language labeling is out of scope unless separately approved.

---

## Part B - Regulatory Date Model (EC-02 Refinement)

### Problem Statement

The current EC-02 gate treats document access as binary: blocked until
`effectiveDate`, unrestricted after. This is wrong for any domain where
documents have two independent dates:

```
promulgationDate  - document is signed, published, and publicly accessible
                    Content can be read, cited, summarized from this date.
                    "Article 5 of Law X states Y" is valid.

effectiveDate     - document becomes operative / legally binding
                    "Is this currently enforceable?" requires this date.
                    Gap from promulgation: hours to 18 months.
```

This two-date structure is not specific to Vietnamese law. It appears in:
EU directives (publication in Official Journal vs transposition deadline),
ISO standards (publication vs mandatory adoption date), US federal rules
(Federal Register date vs compliance date), corporate policies (approval date
vs rollout date), and Vietnamese legislation (ban hanh vs co hieu luc).

EC-02's current overcorrection blocks `SUMMARY_WITH_SOURCE` answers about
document content - when only applicability answers need gating.

### Proposed Model: `documentStatus` Three-State Enum

Replace the binary `BLOCKED_UNTIL_*` gate with a `documentStatus` field
on every corpus record:

| `documentStatus` | Condition | Content query | Applicability query |
|---|---|---|---|
| `PROMULGATED` | promulgationDate reached, effectiveDate not yet | `SUMMARY_WITH_SOURCE` + disclosure note | `ESCALATE_OR_ABSTAIN` (EC-02 fires) |
| `IN_FORCE` | effectiveDate reached | `SUMMARY_WITH_SOURCE`, `DIRECT_CITED_ANSWER` | `DIRECT_CITED_ANSWER` if record is current |
| `STATUS_UNKNOWN` | Either date absent or unverifiable | `ESCALATE_OR_ABSTAIN` (all query types) | `ESCALATE_OR_ABSTAIN` |

**EC-02 trigger matrix (query-class aware):**

```
documentStatus=PROMULGATED:
  content query    -> SUMMARY_WITH_SOURCE  (allowed, + mandatory disclosure)
  applicability    -> ESCALATE_OR_ABSTAIN  (EC-02 fires)
  legal advice     -> ESCALATE_OR_ABSTAIN  (EC-01 fires, independent)

documentStatus=IN_FORCE:
  content query    -> SUMMARY_WITH_SOURCE or DIRECT_CITED_ANSWER
  applicability    -> DIRECT_CITED_ANSWER  (EC-02 no longer fires)
  legal advice     -> ESCALATE_OR_ABSTAIN  (EC-01 still fires)

documentStatus=STATUS_UNKNOWN:
  all query types  -> ESCALATE_OR_ABSTAIN
```

EC-01 (legal advice), EC-03 (interpretation), EC-04 (compliance) remain
active regardless of `documentStatus`. This refinement affects only EC-02.

### Mandatory Disclosure (PROMULGATED state)

When `documentStatus=PROMULGATED`, every response must append a disclosure.
The disclosure is template-driven. The template is stored in the domain
profile or a project-level i18n config - never hardcoded in pipeline code.

```text
Template fields: {promulgationDate}, {effectiveDate}, {freshnessCheckedAt}

locale=en (default):
  "Note: This document was promulgated on {promulgationDate} and is not yet
  in force as of {freshnessCheckedAt}. Effective date: {effectiveDate}.
  Verify current status before relying on this information."

locale=vi (PolicyLocal i18n config):
  "Luu y: Van ban nay da ban hanh ngay {promulgationDate}, chua co hieu luc
  tinh den {freshnessCheckedAt}. Ngay co hieu luc: {effectiveDate}.
  Vui long kiem tra trang thai phap ly truoc khi ap dung."
```

The pipeline renders whichever locale the domain profile declares. A profile
without a locale declaration defaults to `en`. Adding a new locale requires
only adding a template entry - no pipeline code change.

### Schema Changes Required

**Corpus record fields (applies to all domains, not only PolicyLocal):**

- Add `promulgationDate: string | null` - ISO 8601 date or null if unknown
- Add `effectiveDate: string | null` - ISO 8601 date or null if unknown
- Add `documentStatus: "PROMULGATED" | "IN_FORCE" | "STATUS_UNKNOWN"` - computed
- Remove or alias `BLOCKED_UNTIL_*` strings to `documentStatus=PROMULGATED`

**EC-02 contract update (`CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT`):**

- Refine trigger from date-only to `query_class + documentStatus` matrix
- Add `documentStatus` as a required corpus record field checked at retrieval
- Add `notYetInForceDisclosure` template mechanism

**DSCP domain profile `boundaryRules` (`ec02Gate`):**

Current: `ec02Gate: "BLOCKED_UNTIL_2026-07-01"` - flat string
Proposed candidate: `ec02Gate: "QUERY_CLASS_GATED"` - signals the retrieval layer
to apply the `query_class + documentStatus` matrix rather than a date check.

This token must not be introduced by prose alone. Before any runtime or
retrieval code consumes `QUERY_CLASS_GATED`, EC-T2 must add a machine-readable
gate semantics artifact, for example
`docs/reference/CVF_EC02_GATE_SEMANTICS_*.json`, and the checker must verify
that the runtime token, contract table, and machine semantics agree.

### Proposed Tranches

| Tranche | Goal | Key output | Depends on |
|---|---|---|---|
| EC-T1 | Governance decision record | `CVF_GC018_REGULATORY_DATE_MODEL_*.md` - explicitly authorized scope; establishes `documentStatus` as CVF-layer concept | Explicit authorization |
| EC-T2 | Contract and machine semantics | COMPLETE_BOUNDED: response boundary contract update plus machine-readable EC-02 gate semantics JSON | EC-T1 |
| EC-T3 | Corpus record schema update | CLOSED_PASS_BOUNDED at `a895dc03`: `documentStatus`, `promulgationDate`, and `effectiveDate` schema support in TypeScript; no corpus JSON migration | EC-T2 |
| EC-T4 | Per-project metadata backfill | PARKED_PENDING_OPERATOR_METADATA: evidence ledger and proposed JSON exist; CAND-002, CAND-004, CAND-005, and CAND-006 require operator-confirmed signed dates/document numbers; no external workspace edit, no `IN_FORCE`, no `ec02Gate` change | EC-T3, operator dates |
| EC-T5 | DSCP gate value update | CLOSED_BLOCKED_BOUNDED: `QUERY_CLASS_GATED` not applied; EC-T4 remains metadata-gapped and current CPF apply logic blocks only `BLOCKED*`/`PROHIBITED`, so token activation is deferred to a successor with operator metadata and runtime/query routing scope | EC-T4 |
| EC-T6 | Retrieval disclosure wire-in | BLOCKED_BY_EC_T5: retrieval disclosure wire-in remains unauthorized until a successor gate-value activation tranche closes with source-verified runtime/query routing behavior | EC-T5 successor |

### Open Questions for Codex Rebuttal

1. **`documentStatus` vs `legalStatus` naming**: `documentStatus` is more
   general (applies to any regulated document, not only laws). `legalStatus`
   was the prior name. Codex should confirm preferred naming before EC-T1
   schema commit - name change is breaking once downstream records are written.

2. **Migration guard**: All 6 current T11 records carry `BLOCKED_UNTIL_2026-07-01`.
   EC-T3 closed as schema-only; EC-T4 must migrate or backfill these records to
   `documentStatus=PROMULGATED` without silently dropping the applicability
   block. Codex should propose a checker assertion that zero records transition
   from `BLOCKED_*` to `IN_FORCE` without an operator-supplied `effectiveDate`
   that has actually passed.

3. **`ec02Gate: "QUERY_CLASS_GATED"` semantics**: The retrieval layer must know
   what `"QUERY_CLASS_GATED"` means. Codex position: machine-readable
   gate-semantics JSON is required before EC-T5. Contract prose alone is not
   release-ready evidence for runtime behavior.

4. **Non-regulatory domains**: Technical project docs and company docs do not
   typically have `promulgationDate`/`effectiveDate`. Should `documentStatus`
   default to `IN_FORCE` for non-regulatory domain families, or should those
   records simply omit the field and have no EC-02 check at all?

---

## Sequencing Recommendation

```
Phase 1 (parallel - no cross-dependency):
  EX-T1  dependency audit
  EC-T1  governance decision + explicit authorization

Phase 2 (after Phase 1):
  EX-T2  Tier 1 extractor (digital-native) CLOSED_PASS_BOUNDED
  EX-T3  Tier 2 OCR fallback
  EC-T2  contract amendment COMPLETE_BOUNDED

Phase 3 (after Phase 2):
  EX-T4  quality gate + chunk schema CLOSED_PASS_BOUNDED
  EC-T3  corpus record schema update
  EC-T4  per-project metadata backfill (needs operator-supplied dates)

Phase 4 (after Phase 3, parallel):
  EX-T5  DSCP descriptor handoff CLOSED_PASS_BOUNDED
  EX-T6  GC-051 coverage CLOSED_PASS_BOUNDED
  EX-T7  sentence-boundary chunking upgrade CLOSED_PASS_BOUNDED
  EX-T8  extraction authority/storage boundary CLOSED_PASS_BOUNDED
  EC-T5  DSCP gate value update CLOSED_BLOCKED_BOUNDED
  EC-T6  retrieval disclosure wire-in BLOCKED_BY_EC_T4_METADATA_AND_EC_T5

Phase 5 (integration convergence):
  EX-T5 + EC-T6 -> any project's corpus expansion readiness gate (LPCI2-T12 first)
  NOT_OPEN until EC-T4 metadata and EC-T5 runtime/query-class gate value are
  resolved through a fresh evidence path.
```

EC-T1 explicit authorization is the critical gate. EX tranches are independent
of EC approval and can begin at Phase 1 in parallel.

---

## Risk Register

| Risk | Severity | Mitigation |
|---|---|---|
| OCR low confidence on poor-quality scans | HIGH | Quality flags in chunk; retrieval discloses; human review mandatory before any regulated use |
| EC-02 content unlock too broad | HIGH | Query-class gate enforced at retrieval layer AND at corpus record level; dual enforcement; EC-01/03/04 unchanged |
| Operator-supplied dates absent or incorrect | MEDIUM | No auto-inference of regulated dates; operator must supply; EC-T4 blocked until supplied |
| EasyOCR model size breaks CI environment | MEDIUM | EX-T1 audits CI constraints; OCR tier may be offline-only tool if CI cannot support |
| Non-ASCII filenames cause extraction path errors | LOW | T11B Unicode fallback pattern already exists; apply same fix to extraction pipeline intake |
| `documentStatus` name conflicts with existing schema fields | LOW | EC-T1 must grep all corpus JSON schemas before committing field name |

---

## What This Roadmap Does NOT Decide

- Canonical OCR library (EasyOCR vs Tesseract) - deferred to EX-T1 audit
- ML/multilingual sentence splitter selection - EX-T7 closed deterministic punctuation/newline chunking only
- Operator-visible scan outcome report generation - EX-T8 records this as
  successor EX scope; not implemented in EX-T8
- Actual `promulgationDate`/`effectiveDate` values for specific records - operator input required at EC-T4
- Whether `documentStatus` is `IN_FORCE` by default for non-regulatory domains - deferred to EC-T1
- GC-018 authorization for each individual tranche - required before execution release

---

## Status

EX_T8_CLOSED_PASS_BOUNDED_EC_BLOCKED.

EX-T1 is closed as a dependency/source audit and local feasibility probe under:

- `docs/baselines/CVF_GC018_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_2026-06-11.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_FOR_CLAUDE_2026-06-11.md`

EX-T2 is closed pass bounded only under:

- `docs/baselines/CVF_GC018_LPCI2_EX_T2_TIER1_DIGITAL_NATIVE_EXTRACTOR_2026-06-11.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI2_EX_T2_TIER1_DIGITAL_NATIVE_EXTRACTOR_FOR_CLAUDE_2026-06-11.md`
- `docs/reviews/CVF_LPCI2_EX_T2_TIER1_EXTRACTOR_WORKER_RETURN_2026-06-11.md`
- `docs/reviews/CVF_LPCI2_EX_T2_TIER1_EXTRACTOR_COMPLETION_2026-06-11.md`

EX-T3 through EX-T6 are closed pass bounded only under:

- `docs/baselines/CVF_GC018_LPCI2_EX_T3_T6_EXTRACTION_PIPELINE_COMPLETION_2026-06-11.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI2_EX_T3_T6_EXTRACTION_PIPELINE_FOR_CODEX_2026-06-11.md`
- `docs/reviews/CVF_LPCI2_EX_T3_T6_EXTRACTION_PIPELINE_COMPLETION_2026-06-11.md`

EX-T7 is closed pass bounded only under:

- `docs/baselines/CVF_GC018_LPCI2_EX_T7_SENTENCE_BOUNDARY_CHUNKING_2026-06-12.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI2_EX_T7_SENTENCE_BOUNDARY_CHUNKING_FOR_CODEX_2026-06-12.md`
- `docs/reviews/CVF_LPCI2_EX_T7_SENTENCE_BOUNDARY_CHUNKING_COMPLETION_2026-06-12.md`

EX-T8 is closed pass bounded only under:

- `docs/baselines/CVF_GC018_LPCI2_EX_T8_EXTRACTION_AUTHORITY_AND_STORAGE_BOUNDARY_2026-06-12.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI2_EX_T8_EXTRACTION_AUTHORITY_AND_STORAGE_BOUNDARY_FOR_CLAUDE_2026-06-12.md`
- `docs/reviews/CVF_LPCI2_EX_T8_EXTRACTION_AUTHORITY_AND_STORAGE_BOUNDARY_COMPLETION_2026-06-12.md`

No dependency addition to repo manifests, OCR model download, corpus
ingestion, EC-T5 DSCP profile value update, EC-T6 retrieval disclosure
wire-in, T12 authoring, external Policy_Local mutation, public-sync, or
live/provider proof is authorized by this status change.

## Current Runtime Freshness Verification

Runtime freshness command:

`rg -n "ExtractionAuthorityLevel|RebuildClass|ExtractionStorageBoundary|build_extraction_storage_boundary|authorityLevel|rebuildClass|raw_ocr_retained" EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_extraction_pipeline.py`

Observed result: current runtime source and focused tests contain the EX-T8
authority metadata, rebuild metadata, raw OCR retention flag, storage-boundary
builder, and descriptor metadata propagation.

Freshness disposition: SOURCE_VERIFIED_LOCAL_DETERMINISTIC. The roadmap's
negative claims remain bounded to no dependency addition, no OCR model
download, no provider call, no external Policy_Local mutation, no public-sync,
and no EC retrieval/query activation in this EX-T8 closure.

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
| --- | --- | --- |
| Retrieval receipt acceptance claim | N/A with reason: roadmap records EX descriptor handoff only; retrieval receipt remains EC-T6/successor scope | PASS |
| Query acceptance claim | N/A with reason: EC query-class routing remains blocked | PASS |
| Public/export receipt claim | N/A with reason: `DEFERRED_PRIVATE_ONLY` | PASS |

---

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI2_EX_T3_T6_EXTRACTION_PIPELINE_FOR_CODEX_2026-06-11.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_LPCI2_EX_T3_T6_EXTRACTION_PIPELINE_COMPLETION_2026-06-11.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | this file | `Status: ACTIVE_PARTIAL_EX_T8_CLOSED_EC_BLOCKED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | entries through `ex-t8-extraction-authority-storage-boundary-source` and `ex-t8-extraction-authority-storage-boundary-tests` | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | quick lookup rows for EX-T3-EX-T8 source/tests | PASS |
| External evidence digest | EX-T1 audit and EX-T2 completion repo-local artifacts | sha256:46caff533ab8e4d8bc0cfa68070abdf69b7eb205e420c66d9b5db2729109492c; sha256:6e6ee6e640275a85541bcd32a4f9290585fb6d30debc5780df10ef2ea6491e9d; sha256:5e118d33e888176d0f7dc9657602ec041197a46699767d3aa11fe0a48b01a2c9 | PASS |
| System loop interlock | no system-loop mutation | local extraction foundation only | N/A with reason: no runtime loop changed |
| Session continuity | `CVF_SESSION_MEMORY.md`, `CVF_SESSION/ACTIVE_SESSION_STATE.json`, `AGENT_HANDOFF_V17_2026-06-07.md` | reviewer-owned final sync | PASS |

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: internal governance roadmap and closure record; not public-synced.
The EX foundation is private provenance evidence, while EC runtime/query-class
activation remains blocked by EC-T4 metadata gaps and the EC-T5 gate boundary.
