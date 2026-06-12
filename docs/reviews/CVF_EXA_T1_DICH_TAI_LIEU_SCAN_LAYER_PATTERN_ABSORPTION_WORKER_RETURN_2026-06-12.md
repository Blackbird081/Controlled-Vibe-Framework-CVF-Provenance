# CVF EXA-T1: Dich Tai Lieu Scan Layer Pattern Absorption - Worker Return

Memory class: FULL_RECORD

Status: REVIEWED_READY_FOR_CLOSURE

docType: worker_return

Date: 2026-06-12

Worker: Claude

Reviewer: Codex

Commit mode: WORKER_MUST_NOT_COMMIT

Parent work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_EXA_T1_DICH_TAI_LIEU_EXTRACTION_PATTERN_ABSORPTION_FOR_CLAUDE_2026-06-12.md`

Source map:
`docs/reference/CVF_EXA_T1_DICH_TAI_LIEU_SCAN_LAYER_PATTERN_SOURCE_MAP_2026-06-12.md`

---

## Purpose

Return a bounded external-pattern absorption packet for Codex review before
any CVF scan-layer implementation or Policy_Local pilot work.

## Target And Source Under Review

- CVF work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_EXA_T1_DICH_TAI_LIEU_EXTRACTION_PATTERN_ABSORPTION_FOR_CLAUDE_2026-06-12.md`
- External repository: `https://github.com/nclamvn/dich-tai-lieu`
- External commit:
  `92c5aeb3b4886b6d5a14ea4682dc5e4e1bc1a336`

## Scope And Methodology

The worker inspected the bounded 15-file source set, classified the seven
required patterns, and performed exact-symbol negative searches. Codex then
independently recomputed the external inventory, source line counts, source
anchors, license evidence, and current CVF owner-surface overlap.

## External Commit Evidence

| Field | Value |
| --- | --- |
| Repository | `https://github.com/nclamvn/dich-tai-lieu` |
| Required commit | `92c5aeb3b4886b6d5a14ea4682dc5e4e1bc1a336` |
| Observed commit | `92c5aeb3b4886b6d5a14ea4682dc5e4e1bc1a336` |
| Drift | NONE |
| Clone method | `git clone` to `/tmp/dich-tai-lieu` then `git rev-parse HEAD` |

---

## Knowledge Absorption Blind-Spot Control Block

| Control gate | Worker action taken | Verdict |
| --- | --- | --- |
| Source depth | Read source files and unit tests directly, not README only; 15 files in bounded review set read | CLEAR |
| Corpus boundary | Every file read is enumerated in the source map processing ledger; bounded to work-order scope | CLEAR |
| Accept/defer/reject | Every required pattern in the work order classified below; 7/7 required patterns dispositioned | CLEAR |
| CVF owner routing | Every accepted pattern mapped to candidate CVF surface in the recommendation table below; all candidate names verified absent from CVF source via negative search | CLEAR |
| Adversarial review | Overclaim, dependency, provider, domain-bleed, and license risks reviewed in the Adversarial Verification section | CLEAR |
| Blind-spot delta | Uninspected files listed in source map with terminal-status totals; key deferred questions listed below | PARTIAL - 1125 tracked files intentionally excluded from semantic review |

**Overall verdict: PASS_BOUNDED**. The partial corpus is acceptable only
because EXA-T1 authorizes a bounded source set and makes no full-repository
completeness claim.

## Findings And Reviewer Position

| Finding | Severity | Reviewer position |
| --- | --- | --- |
| Worker reported 1138 files; independent enumeration found 1140 tracked files | MEDIUM | Corrected to 1140 with exact terminal-status reconciliation |
| Worker line-count notes understated several inspected files | MEDIUM | Replaced with exact physical line counts and section-level inspection wording |
| README verification rows contradicted the processing ledger | MEDIUM | Corrected to direct README lines 32 and 34-35 |
| Candidate table treated existing CVF capabilities as absent | HIGH | Reconciled against current extraction and DSCP owner surfaces; accepted value is now extension-oriented |
| Corpus verdict claimed completeness despite 1125 excluded files | HIGH | Downgraded to PARTIAL with bounded-closure rationale |
| Worker packet missed required review structure, ASCII discipline, and learning-disposition fields | MEDIUM | Repaired before closure; existing machine gates caught all three schema classes |
| Reviewer-fast omitted the applicable Rescan Intelligence checker | MEDIUM | Pre-commit caught the issue; promote checker placement before the next absorption return |

## Existing CVF Owner-Surface Reconciliation

| External pattern | Current CVF owner evidence | Delta after reconciliation | Decision |
| --- | --- | --- | --- |
| Extraction quality score | `extraction_pipeline.py:101` `ExtractionQualityReport`; `extraction_pipeline.py:235` `evaluate_extraction_quality` | Multi-signal weighted profile may refine the existing gate; a second quality gate is not justified | ACCEPT_AS_EXTENSION_CANDIDATE |
| OCR language configuration | `extraction_pipeline.py:162` `map_ocr_language_codes`; DSCP profile `languageCodes` at `dscp.domain.profile.contract.ts:45` | Script detection and engine-scoped profile metadata remain possible extensions | ACCEPT_AS_EXTENSION_CANDIDATE |
| Feedback and escalation | `scan_outcome_report.py:43` `ScanOutcomeReport`; `scan_outcome_report.py:131` `build_scan_outcome_report` | Operator-visible actions exist; automatic retry orchestration remains a separate runtime decision | DEFER_REQUIRES_SEPARATE_ROADMAP |
| Strategy router | Current extraction tiers and quality statuses exist, but no source-backed pre-extraction page-signal decision contract was found | A deterministic decision contract remains useful without importing runtime dependencies | ACCEPT_AS_CVF_CONTRACT_CANDIDATE |
| Page/document analysis signals | Current quality evaluation occurs after extraction and uses a smaller signal set | A bounded pre-extraction signal schema remains useful | ACCEPT_AS_CVF_CONTRACT_CANDIDATE |

---

## Pattern Disposition Matrix

### Pattern 1: Strategy Router

**External source:** `core/smart_extraction/extraction_router.py`

**Evidence:**
- `SmartExtractionRouter.extract()` (line 99+) performs a 4-strategy dispatch:
  `FAST_TEXT` -> PyMuPDF, `HYBRID` -> PyMuPDF + selective Vision, `OCR` -> PaddleOCR,
  `FULL_VISION` -> Vision API
- Strategy selection is pre-computed by `DocumentAnalyzer.analyze()` then
  overridden if `force_strategy` or `use_vision=False` is set
- OCR bypass: if strategy is `FULL_VISION` AND `source_lang` is in
  `ocr_supported_langs` AND `analysis.scanned_pages > 0`, router downgrades to
  `OCR` without provider cost (lines 134-140)
- `ExtractionResult` dataclass captures: strategy used, time saved, cost saved,
  pages via text/vision/OCR, OCR confidence

**CVF value:** The dispatch-before-execute pattern is a CVF scan-layer primitive.
Current CVF extraction tiers do not expose a source-backed pre-extraction
page-signal decision contract. The pre-analysis -> override -> execute flow can
inform an adjacent deterministic decision contract without replacing existing
extraction tiers.

**Risk:**
- PyMuPDF (`fitz`) is a C-extension; CVF cannot adopt it without a dependency
  decision
- Vision API call paths reference provider-specific clients (`vision_reader`,
  `llm_client`) that are app-specific
- OCR path requires PaddleOCR (`paddle_client`) - app-specific runtime

**Disposition:** `ACCEPT_AS_CVF_CONTRACT_CANDIDATE`

**Proposed CVF candidate name:** `ScanRouteDecision` (deterministic contract
result only; no runtime code copied)

**Candidate owner surface:** `EXTENSIONS/CVF_EXTRACTION_FOUNDATION`, adjacent
to the existing extraction pipeline.

---

### Pattern 2: Page and Document Analysis Signals

**External source:** `core/smart_extraction/document_analyzer.py`

**Evidence:**
- `PageAnalysis` dataclass (line 33): `has_text`, `text_coverage`, `has_images`,
  `has_tables`, `has_formulas`, `is_scanned`, `needs_vision`, `text_blocks`,
  `image_count`, `char_count`, `sample_text`
- `DocumentAnalysis` dataclass (line 49): `text_coverage`, `native_text_pages`,
  `scanned_pages`, `complex_pages`, `has_tables`, `has_images`, `has_formulas`,
  `complex_page_numbers`, `strategy`, `strategy_reason`, `estimated_time_fast`,
  `estimated_time_vision`, `estimated_cost_vision`
- Strategy thresholds (lines 100-102):
  `TEXT_COVERAGE_THRESHOLD = 0.7`, `SCANNED_THRESHOLD = 0.1`,
  `COMPLEX_PAGE_THRESHOLD = 0.15`
- Academic paper detection (line ~170+): keyword list for English and Japanese;
  arXiv filename heuristic; formula-as-image detection bypass

**CVF value:** The `DocumentAnalysis` signal set can inform a reusable
pre-extraction analysis contract. The threshold trio is external calibration
evidence only; CVF may define configurable thresholds after local tests rather
than adopt the external values.

**Risk:**
- The `analyze()` implementation requires `fitz` (PyMuPDF) for page-level
  sampling - runtime dependency not available in CVF
- Academic paper keyword lists are language-specific heuristics that need domain
  review before any CVF adoption
- Strategy estimates (`estimated_time_vision`, `estimated_cost_vision`) embed
  provider cost assumptions (`$0.02/page`) that must not be adopted as CVF claims

**Disposition:** `ACCEPT_AS_CVF_CONTRACT_CANDIDATE`

**Proposed CVF candidate name:** `DocumentScanSignals` (schema/contract only;
thresholds as configurable constants)

**Candidate owner surface:** `EXTENSIONS/CVF_EXTRACTION_FOUNDATION`, as an
input schema for a future scan-route decision.

---

### Pattern 3: Extraction Quality Scoring (EQS)

**External source:** `api/services/eqs.py`

**Evidence:**
- `ExtractionQualityScorer.score()` computes a weighted composite from 6 signals
  (lines 109-135): `text_density`, `structure`, `encoding`, `language`,
  `completeness`, `format_integrity`
- `DEFAULT_WEIGHTS` (lines 74-80): weights sum to exactly 1.0; validated at
  construction time
- `EQSReport` (lines 32-54): exposes `overall_score`, `grade` (A/B/C/D/F),
  `passed` property (threshold 0.6), `signals`, `recommendation`, `to_dict()`
- Standalone module: no imports from `core/` or extraction modules; operates
  on plain text + metadata
- `tests/unit/test_eqs.py` covers constructor behavior, signal scorers, grading,
  and recommendation logic; no coverage percentage was independently measured

**CVF value:** CVF already has `ExtractionQualityReport` and
`evaluate_extraction_quality()`. The useful delta is a configurable,
multi-signal profile that may refine the existing gate after local calibration.
The external scorer must not become a parallel quality authority.

**Risk:**
- Weight values are calibrated for the external app's use case (PDF->translation);
  CVF may require different weight tuning for governance document ingestion
- The `passed` threshold (0.6) is hard-coded; CVF would need a configurable
  threshold per corpus type
- `format_integrity` signal detects LaTeX/Markdown markers; relevance for CVF
  governance documents (primarily Markdown) needs assessment
- No license issue with the *pattern* (not copying code); ideas are not
  copyrightable

**Disposition:** `ACCEPT_AS_CVF_CONTRACT_CANDIDATE`

**Proposed CVF candidate name:** `ExtractionQualitySignalProfile` (configuration
for the existing quality gate; weights and threshold locally calibrated)

**Candidate owner surface:** existing
`EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py`
`ExtractionQualityReport` / `evaluate_extraction_quality()`.

---

### Pattern 4: Feedback Loop and Escalation

**External source:** `api/services/extraction_feedback.py`

**Evidence:**
- `ExtractionFeedbackLoop` orchestrates quality-driven retry with configurable
  `min_score`, `max_retries`, and `fallback_chain`
- `DEFAULT_FALLBACK_CHAIN = [TEXT, OCR, VISION, MANUAL_REVIEW]` (lines 102-103)
- `evaluate()` method: if score < threshold -> `RETRY` to next strategy; if
  `max_retries` reached -> `ESCALATE`; if at `MANUAL_REVIEW` -> `ESCALATE`
- `run_loop()` async method: drives extraction fn across retries, records each
  iteration as `FeedbackResult`, returns `FeedbackLoopResult` with `best_result`
  property
- Standalone module: imports only `eqs.py` + stdlib

**CVF value:** CVF already emits operator-visible scan outcomes and actions.
The external pattern demonstrates a possible retry policy, but automatic retry
orchestration changes runtime behavior and is not required to close the current
operator-reporting gap.

**Risk:**
- The external `ExtractionStrategy` enum maps to specific runtime methods
  (TEXT, OCR, VISION) that are not CVF concepts; CVF would rename to corpus-
  ingestion terminology (e.g., `NATIVE_PARSE`, `STRUCTURED_PARSE`,
  `MANUAL_REVIEW`)
- `run_loop()` is async and calls an external `extract_fn` - CVF adoption
  would need adaptation to CVF's synchronous governance workflow

**Disposition:** `DEFER_REQUIRES_SEPARATE_ROADMAP`

**Reason for defer:** current `ScanOutcomeReport` already provides stable
operator actions. A retry policy requires a separate runtime design review,
quota/dependency boundaries, and failure diagnostics.

**Potential owner surface:** existing scan outcome reporting and extraction
pipeline, not a parallel feedback subsystem.

---

### Pattern 5: OCR Language and Script Routing

**External source:** `api/services/ocr_language_support.py`

**Evidence:**
- `OcrLanguageSupport.detect_script()`: Unicode range-based script detection
  (Latin, CJK, Hiragana, Katakana, Hangul, Arabic, Hebrew, Cyrillic, Devanagari,
  Thai); returns `ScriptInfo(script, language, confidence)`
- `LANGUAGE_CONFIGS` dict: 9 languages (en, vi, ja, zh, ko, ar, ru, hi, th),
  each with `OcrConfig(lang_code, script, engine, supports_vertical,
  requires_preprocessing, notes)`
- Vietnamese config: `lang_code="vie"`, `notes="Vietnamese diacritics require
  Unicode-aware OCR"` - directly relevant to Policy_Local (Vietnamese legal corpus)
- RTL/CJK/preprocessing flags: machine-readable per-language properties
- Standalone module: no runtime OCR imports; detection is pure Python stdlib

**CVF value:** CVF already carries DSCP profile language codes and maps
Vietnamese/English codes for governed OCR adapters. The useful delta is
optional script evidence and explicit engine-scoped OCR profile metadata,
without silently overriding caller-supplied language authority.

**Risk:**
- The `lang_code` values (`vie`, `jpn`, `chi_sim`) are PaddleOCR engine codes;
  CVF must not adopt these as generic language IDs without engine-routing context
- `supports_vertical` and `requires_preprocessing` flags are only relevant when
  an OCR runtime is wired in; CVF scan layer does not currently have an OCR
  runtime

**Disposition:** `ACCEPT_AS_CVF_CONTRACT_CANDIDATE`

**Proposed CVF candidate name:** `ExtractionScriptEvidence` (optional scan
evidence; engine-specific codes remain separate from authoritative DSCP
language codes)

**Candidate owner surface:** existing extraction pipeline language mapping plus
DSCP domain profile metadata.

---

### Pattern 6: Translation Memory and Glossary

**External source:** `api/services/translation_memory.py`,
`api/services/glossary_manager.py`

**Evidence:**
- `TranslationMemoryService`: fuzzy TM with `difflib.SequenceMatcher`; domain-
  aware (`medical`, `legal`, `general`); JSON persistence; no external deps
- `GlossaryManager`: CRUD glossary with JSON persistence; `get_term_dict()`
  returns `Dict[str, str]` for downstream consistency checking
- Both services are fully standalone (stdlib only)

**CVF value:** The domain-aware TM pattern (legal domain is a named first-class
value) is potentially useful for Policy_Local's legal terminology consistency.
However, Policy_Local's corpus is a read/query surface, not a translation
surface - the TM write path is out of scope for CVF's current use case.

**Disposition:** `DEFER_REQUIRES_SEPARATE_ROADMAP`

**Reason for defer:** CVF does not currently have a translation workflow.
Policy_Local serves Vietnamese legal Q&A, not document translation. The legal
domain label in the TM is a name match but not a functional match. A separate
roadmap is required to assess whether CVF needs a TM surface at all.

**Proposed future lane:** Legal terminology consistency checker for Policy_Local
corpus - requires operator decision before scoping.

---

### Pattern 7: Multi-Provider Fallback

**External source:** `api/services/provider_router.py`

**Evidence:**
- `COLD_START_DEFAULTS` dict: three providers (`openai`, `anthropic`, `deepseek`)
  with quality scores, cost per 1k tokens, latency, and language affinities
- `RoutingMode` enum: `BEST_QUALITY`, `CHEAPEST_GOOD_ENOUGH`, `BALANCED`
- Router selects provider based on historical performance stats, language pair
  affinity, and cost constraints
- Imports `ProviderStatsTracker` from `api/services/provider_stats.py`

**CVF value:** Pattern is interesting for multi-provider routing concepts.
However, CVF already has a governed multi-provider execution layer.
The cost/quality/latency trade-off pattern has limited incremental value over
existing CVF provider selection.

**Overclaim risk:**
- The `COLD_START_DEFAULTS` cost/quality numbers (`quality: 0.82`, `cost_per_1k:
  0.0125`) are the external app's estimates - must NOT be adopted as CVF claims
- Language affinity lists are the external app's opinion, not verified benchmarks

**Disposition:** `DEFER_REQUIRES_SEPARATE_ROADMAP`

**Reason for defer:** CVF execute layer already handles provider selection.
Incremental value requires a separate analysis of the execute layer's current
gaps. No adoption without a dedicated GC-018. Cost/quality numbers from the
external app must not be reused.

---

## CVF Candidate Recommendation Table

| Candidate name | Source pattern | CVF target surface | Adoption form | Priority |
| --- | --- | --- | --- | --- |
| `ScanRouteDecision` | Strategy router + OCR bypass | Existing extraction foundation | New deterministic decision result adjacent to existing tiers; no extractor dependency | HIGH - useful generic pre-extraction control |
| `DocumentScanSignals` | Page/document analysis signals | Existing extraction foundation | New bounded input schema; thresholds require local calibration | HIGH - required input for route decision |
| `ExtractionQualitySignalProfile` | EQS 6-signal scorer | Existing `ExtractionQualityReport` and `evaluate_extraction_quality()` | Optional configuration/refinement, not a parallel quality gate | MEDIUM - useful only after regression comparison |
| `ExtractionScriptEvidence` | OCR language/script registry | Existing OCR mapping plus DSCP language metadata | Optional evidence that cannot override authoritative profile language | MEDIUM - generic multilingual extension |
| Retry orchestration | Feedback loop + escalation | Existing scan outcome reporting and extraction pipeline | Deferred runtime policy; requires separate design and diagnostics | DEFERRED |
| TM / Glossary | Translation memory + glossary | No current CVF owner selected | Deferred; requires separate operator decision | LOW - translation workflow mismatch |
| Multi-provider fallback | Provider router + cold-start defaults | Existing CVF execute layer | Deferred; external constants and routing policy are non-authoritative | LOW - overlaps existing provider layer |

---

## No-Code-Import Proof

No source code from `nclamvn/dich-tai-lieu` has been copied into any CVF file.
All patterns are described as design abstractions, interface shapes, and
candidate names. No `import` statement, no function body, no class definition
from the external repo appears in any CVF artifact.

**Verification:** `git status --short` in CVF repo before and after worker
execution shows only two new untracked files:

```
?? docs/reference/CVF_EXA_T1_DICH_TAI_LIEU_SCAN_LAYER_PATTERN_SOURCE_MAP_2026-06-12.md
?? docs/reviews/CVF_EXA_T1_DICH_TAI_LIEU_SCAN_LAYER_PATTERN_ABSORPTION_WORKER_RETURN_2026-06-12.md
```

No modifications to existing CVF files. No new dependencies. No new imports.

---

## No-Provider / No-API-Key Proof

No provider API was called during this worker execution. No API key, bearer
token, or provider credential was used or referenced. The external repository
was accessed via public `git clone` only. EQS and feedback loop patterns were
read from source text, not executed.

---

## Adversarial Verification

### Overclaim Risk Review

| Risk | Assessment |
| --- | --- |
| Performance claims (`95% faster`, `97% cheaper`) | NOT adopted. These are README marketing claims about a specific app setup. CVF claim boundary excludes performance, cost, and accuracy claims from external sources. |
| Provider cost numbers (`$0.02/page`, cold-start defaults) | NOT adopted. These are the app's estimates for its own provider contracts. CVF must not surface these as authoritative. |
| OCR accuracy (`85-95% for clean scanned documents`) | NOT adopted. This is a third-party claim about PaddleOCR performance. Not verifiable from source reading. |
| EQS threshold (0.6 pass/fail) | Noted as the app's calibration, NOT adopted as CVF's threshold. CVF must configure its own threshold per corpus type. |
| `ExtractionStrategy` enum values as CVF vocabulary | NOT adopted verbatim. Worker proposes CVF-native renames (e.g., `CorpusIngestionFeedbackGate` with corpus-ingestion strategy vocabulary). |

### Dependency Risk Review

| Risk | Assessment |
| --- | --- |
| PyMuPDF (`fitz`) | Major C-extension dependency. CVF scan layer patterns derived from the router and analyzer are described as interface contracts only. No fitz dependency introduced. |
| PaddleOCR | Runtime OCR engine. Not imported. The `OcrConfig` pattern is abstracted as a language-profile schema only. |
| External provider clients (Vision, OpenAI, Anthropic via external app) | Not imported. Provider integration patterns are deferred to a separate roadmap. |
| `difflib.SequenceMatcher` (TM) | Python stdlib. Not introduced into CVF - TM pattern is deferred. |

### Domain Bleed Risk Review

| Risk | Assessment |
| --- | --- |
| Policy_Local legal corpus mutation | NOT triggered. EXA-T1 is pattern absorption only. No Policy_Local file modified. EC-02 boundary intact. |
| Legal accuracy claims from external app | NOT present. External app is a translation tool, not a legal authority. No legal content claims absorbed. |
| Vietnamese legal terminology normalization | The OCR language config confirms `vie` + diacritics handling is a real concern for Policy_Local. This is a design input, not a legal claim. |

### License Risk Review

| Risk | Assessment |
| --- | --- |
| Code copying | NONE - no code copied (verified by no-code-import proof above). |
| Pattern-level learning | Bounded descriptions and independent CVF owner mapping only; no legal conclusion about abstract idea ownership is required for this closure. |
| Repository license | MIT license verified from external `LICENSE`; future code reuse would still require attribution/license handling and explicit authorization. |

---

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| Worker corpus count, line-count notes, and README verification were inaccurate | WORKER_EXECUTION_ERROR | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | Require exact command-backed counts and reviewer recomputation before closure |
| Exact-symbol negative search did not detect overlap with existing CVF capabilities | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | Future absorption work orders must require current owner-surface reconciliation, not token absence alone |
| Worker packet omitted structural, ASCII, and learning-disposition requirements | WORKER_EXECUTION_ERROR | DOCUMENTATION_ONLY_LEARNING | RULE_EXISTS | Reviewer-fast remains mandatory before semantic acceptance |
| Rescan Intelligence failed only at pre-commit because reviewer-fast did not run that checker | PHASE_GATE_PLACEMENT_GAP | GOVERNANCE_CONTROL_PLANE | PHASE_GATE_PLACEMENT_GAP | Add the rescan checker to reviewer-fast in a separate control-plane hardening batch |
| External provider cost/quality constants are not CVF evidence | RUNTIME_SIGNAL_GAP | COST_ECONOMICS_LEARNING | N/A_WITH_REASON | No runtime/provider/cost claim is adopted; any future claim requires separately authorized evidence |
| External retry loop would change runtime behavior | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | RUNTIME_LEARNING_CANDIDATE | Keep deferred unless a separate roadmap defines diagnostics, limits, and human escalation |
| External provider selection does not prove provider output quality | RUNTIME_SIGNAL_GAP | PROVIDER_OUTPUT_LEARNING | N/A_WITH_REASON | Provider routing remains outside EXA-T1 and no provider-quality conclusion is made |

---

## Blind-Spot Delta (Uninspected Files and Deferred Questions)

**Uninspected files (out-of-scope for EXA-T1):**

- `core/ocr/paddle_client.py` - OCR engine interface; needed if CVF ever considers
  native OCR runtime adoption (requires separate GC-018)
- `ai_providers/` (8 files) - multi-provider runtime; needed for EXA-T2 if
  provider fallback is scoped
- `core/tm/` (7 files) - TM runtime; needed if TM adoption is scoped
- `core/batch/` and related - batch processing patterns; potentially interesting
  for CVF corpus batch ingestion but outside EXA-T1 scope
- `core/layout_preserve/` - layout-preserving translation pipeline; potentially
  relevant for formatted document ingestion but outside EXA-T1 scope

**Deferred questions for Codex / operator:**

1. **EXA-T2 scope recommendation:** Limit EXA-T2 to deterministic
   `DocumentScanSignals` and `ScanRouteDecision` contracts plus focused tests.
   Do not open OCR engines, provider runtime, or dependency installation.
2. **Dependency decision:** Keep PyMuPDF and other extractor dependencies
   delegated to caller adapters. EXA-T2 should accept normalized signals rather
   than parse documents itself.
3. **Policy_Local corpus language:** Is the Policy_Local corpus
   Vietnamese-only, or does it require multi-script support? This determines
   whether `CorpusScriptProfile` is HIGH or LOW priority.
4. **Quality profile decision:** Compare any multi-signal refinement against
   current `evaluate_extraction_quality()` behavior in a later tranche; do not
   assume external EQS weights improve CVF.

## Risks And Corrective Actions

| Risk | Corrective action |
| --- | --- |
| Duplicate scan-layer authorities | Extend current extraction owner surfaces instead of creating parallel gates |
| External thresholds treated as calibrated CVF values | Keep values as source observations until local regression evidence exists |
| Language detection overrides governed profile metadata | Treat script detection as optional evidence only |
| Runtime/provider scope creep | Keep OCR engines, automatic retries, and provider fallback outside EXA-T2 |
| Bounded review mistaken for full absorption | Preserve corpus verdict PARTIAL and explicit exclusions |

## Rescan Intelligence Hardening

- Original source artifact: `https://github.com/nclamvn/dich-tai-lieu` at `92c5aeb3b4886b6d5a14ea4682dc5e4e1bc1a336`.
- Predecessor intake artifact: operator request dated 2026-06-12 and EXA-T1 dispatch packet.
- Delta ledger status: COMPLETE_FOR_BOUNDED_REVIEW
- Routing matrix status: COMPLETE_FOR_BOUNDED_REVIEW
- Semantic sampling status: COMPLETE_FOR_BOUNDED_REVIEW
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Category | Delta | Disposition |
| --- | --- | --- |
| UNCHANGED_FROM_INTAKE | External extraction source contains reusable scan-layer patterns | Retain bounded absorption |
| CHANGED_DISPOSITION | Quality, language, and feedback patterns overlap current CVF owner surfaces | Convert new-system proposals into owner-surface extensions or deferrals |
| NEW_FINDING | Worker corpus counts and completeness claim were inaccurate | Correct evidence and retain PARTIAL corpus verdict |
| REMOVED_OR_REJECTED | Parallel quality gate, provider fallback, runtime retry, and direct dependency adoption | Reject from EXA-T1/EXA-T2 scope |

### Follow-Up Routing Matrix

| Routing lane | Item | Decision |
| --- | --- | --- |
| DO_NOW | Close corrected EXA-T1 evidence packet | Reviewer closure |
| SEPARATE_RUNTIME_TRANCHE | Automatic retries, OCR engines, provider fallback | Keep parked |
| STRATEGIC_OPERATOR_DECISION | Policy_Local pilot after foundation refinement | Keep downstream |
| OUT_OF_SCOPE | Translation product, UI, publishing, and external runtime import | Reject |
| RESOLVED_BY_DESIGN | Extend existing CVF extraction owners rather than create parallel authorities | Apply to EXA-T2 |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| EXA-R1 | external extraction router | pre-analysis routing is reusable | ACCEPT_AS_CVF_CONTRACT_CANDIDATE | Current CVF already has extraction tiers | ACCEPT_ONLY_AS_ADJACENT_DECISION_CONTRACT |
| EXA-R2 | external EQS service | weighted quality scoring improves CVF | ACCEPT_AS_EXTENSION_CANDIDATE | Current CVF already has a quality report and gate | DEFER_PROFILE_REFINEMENT_PENDING_LOCAL_TESTS |
| EXA-R3 | external OCR language support | script routing is reusable | ACCEPT_AS_EXTENSION_CANDIDATE | DSCP language metadata must remain authoritative | ACCEPT_ONLY_AS_OPTIONAL_EVIDENCE |

## Decision And Disposition

Reviewer decision: `ACCEPT_WITH_CORRECTIONS`.

EXA-T1 demonstrates bounded reusable value. The next justified foundation
tranche is EXA-T2 for deterministic pre-extraction signal and route-decision
contracts only. Quality-profile refinement, automatic retry, OCR runtime,
provider fallback, translation memory, and Policy_Local integration remain
separate decisions.

---

## Claim Boundary

This worker return authorizes only external pattern absorption. It does not
authorize:

- Code import from `nclamvn/dich-tai-lieu`
- Dependency installation (PyMuPDF, PaddleOCR, or any external library)
- OCR runtime execution
- Provider API calls
- Policy_Local corpus mutation
- EC activation or retrieval claims
- T12 eligibility for any Policy_Local record
- Public-sync of any EXA-T1 artifact
- Production readiness or performance claims

All accepted patterns are proposed as CVF-native contract candidates only.
Implementation requires separate GC-018 per candidate.

---

## Acceptance Checklist (Worker Self-Assessment)

| Item | Status |
| --- | --- |
| Source map authored | DONE - `docs/reference/CVF_EXA_T1_DICH_TAI_LIEU_SCAN_LAYER_PATTERN_SOURCE_MAP_2026-06-12.md` |
| Worker return authored | DONE - this file |
| External commit evidence recorded | DONE - `92c5aeb3b4886b6d5a14ea4682dc5e4e1bc1a336` verified |
| Pattern matrix complete | DONE - 7/7 required patterns classified |
| Forbidden actions avoided | DONE - no commit, no code copy, no dependency install, no provider call, no Policy_Local mutation, no public-sync |
| Negative searches executed | DONE - 7 tokens searched in CVF, 0 collisions found |
| No-code-import proof | DONE - `git status --short` confirms only 2 new untracked files |
| Source verification table | DONE - 12/12 claims from work order verified |
| Blind-spot control block | DONE - 6/6 gates executed, overall CLEAR |
| Corpus completeness block | CORRECTED BY REVIEWER - 15 READ, 1091 SKIPPED_WITH_REASON, 34 BLOCKED_UNREADABLE, verdict PARTIAL |

## Reviewer Verification

Codex independently verified:

- CVF execution HEAD `e010c9d2`;
- external remote and commit anchor;
- 1140 tracked external files;
- exact reconciliation `15 + 1091 + 34 = 1140`;
- physical line counts for all 15 reviewed files;
- all 12 work-order source claims;
- absence of exact external symbols in scoped CVF source;
- presence of overlapping current CVF extraction/DSCP owner surfaces;
- external MIT license text;
- only the two worker-owned files were created before reviewer closure edits.

---

## Return-To-Orchestrator Signal

**REVIEWED_READY_FOR_BOUNDED_CLOSURE**

Worker evidence required corrections, but no remaining blocking condition
requires operator input or scope expansion.

Conditions that would have blocked (none triggered):
- External commit drift: NOT triggered (`92c5aeb...` confirmed)
- Files unreadable: NOT triggered (all 15 bounded-set files read successfully)
- Source evidence contradicts work order: NOT triggered (12/12 claims verified)
- Useful absorption requires code import or provider calls: NOT triggered;
  accepted value is limited to deterministic contracts or existing-owner
  refinements


