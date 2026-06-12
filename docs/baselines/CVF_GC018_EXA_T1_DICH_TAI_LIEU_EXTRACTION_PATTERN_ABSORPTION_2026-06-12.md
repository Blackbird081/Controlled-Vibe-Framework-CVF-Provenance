# CVF GC-018 Baseline: EXA-T1 Dich Tai Lieu Extraction Pattern Absorption

Memory class: FULL_RECORD

Status: DISPATCHED

docType: baseline

Date: 2026-06-12

Owner: Codex

baseHead: `d1167f69`

externalRepo: `https://github.com/nclamvn/dich-tai-lieu`

externalCommit: `92c5aeb3b4886b6d5a14ea4682dc5e4e1bc1a336`

## Purpose

Authorize Claude to inspect a pinned external repository for reusable
scan-layer patterns and return bounded absorption evidence for Codex review.

## Scope / Target / Owner Boundary

In scope:

- bounded source map for relevant extraction files;
- pattern disposition matrix;
- CVF scan-layer candidate recommendations;
- worker return packet.

Out of scope:

- code import;
- dependency installation;
- OCR execution;
- provider/API-key use;
- Policy_Local mutation;
- EC activation, retrieval, corpus ingestion, or T12 unlock;
- public-sync or readiness claims.

## Source / Predecessor Evidence

| Predecessor | Evidence artifact | Disposition |
| --- | --- | --- |
| RDA-T4 closure | `docs/reviews/CVF_MEOR_RDA_T4_FOUNDATION_CLOSURE_AND_POLICYLOCAL_SUCCESSOR_COMPLETION_2026-06-12.md` | ACCEPT |
| Policy_Local successor roadmap | `docs/roadmaps/CVF_POLICYLOCAL_SUCCESSOR_PILOT_ROADMAP_2026-06-12.md` | ACCEPT_AS_DOWNSTREAM |
| External repo clone | `https://github.com/nclamvn/dich-tai-lieu` at `92c5aeb3b4886b6d5a14ea4682dc5e4e1bc1a336` | ACCEPT_AS_SOURCE |

## Authority Chain

| Authority | Path or source | Status |
| --- | --- | --- |
| Operator direction | 2026-06-12 external-source absorption request | ACCEPT |
| Parent roadmap | `docs/roadmaps/CVF_EXTERNAL_EXTRACTION_PATTERN_ABSORPTION_ROADMAP_2026-06-12.md` | EXA_T1_DISPATCHED |
| Work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_EXA_T1_DICH_TAI_LIEU_EXTRACTION_PATTERN_ABSORPTION_FOR_CLAUDE_2026-06-12.md` | DISPATCHED |

## Knowledge Absorption Blind-Spot Control Block

| Control | Requirement | Disposition |
| --- | --- | --- |
| Source depth | inspect source files, not README only | REQUIRED |
| Corpus boundary | enumerate bounded external files read | REQUIRED |
| Accepted value routing | map accepted value into CVF-owned scan-layer candidates | REQUIRED |
| Rejection clarity | separate rejected app-specific value from rejected source | REQUIRED |
| Adversarial review | identify overclaim, dependency, provider, and domain bleed risks | REQUIRED |
| Blind-spot delta | list what remains uninspected or deferred | REQUIRED |

## Rescan Intelligence Hardening

- Original source artifact:
  `https://github.com/nclamvn/dich-tai-lieu` at
  `92c5aeb3b4886b6d5a14ea4682dc5e4e1bc1a336`
- Predecessor intake artifact: operator request in active session on
  2026-06-12 naming `nclamvn/dich-tai-lieu` as a scan-layer learning source
- Delta ledger status: REQUIRED_IN_EXA_T1_WORKER_RETURN
- Routing matrix status: REQUIRED_IN_EXA_T1_WORKER_RETURN
- Semantic sampling status: REQUIRED_IN_EXA_T1_WORKER_RETURN
- Rescan intelligence verdict: PARTIAL

### Original-Intake Delta Ledger

| Delta category | Current finding | Predecessor finding | Disposition | Reason |
| --- | --- | --- | --- | --- |
| UNCHANGED_FROM_INTAKE | External repo may contain reusable scan-layer extraction patterns | Operator intake identified repo as learning source | DO_NOW | Must be source-verified before Policy_Local use-case work resumes. |
| CHANGED_DISPOSITION | README-level feature signals are not sufficient evidence | Initial chat named repo generally | SOURCE_VERIFICATION_REQUIRED | Worker must verify source files and tests, not absorb README claims alone. |
| NEW_FINDING | External code may mix document extraction, translation memory, OCR, and provider behavior | None | ROUTE_BY_PATTERN | CVF must separate scan-layer value from app-specific provider/runtime choices. |
| REMOVED_OR_REJECTED | No external code import or dependency adoption is authorized | None | REJECTED_FROM_EXA_T1 | This tranche is knowledge absorption only. |

### Follow-Up Routing Matrix

| Routing lane | Item | Disposition | Next action |
| --- | --- | --- | --- |
| DO_NOW | Source-map external extraction, quality, fallback, OCR-language, and memory/glossary patterns | EXA_T1_WORKER_SCOPE | Produce source map and worker return only. |
| SEPARATE_RUNTIME_TRANCHE | Any OCR/provider execution, dependency install, performance benchmark, or live extraction proof | OUT_OF_EXA_T1 | Requires later explicit operator authorization. |
| STRATEGIC_OPERATOR_DECISION | Whether accepted patterns should become Policy_Local pilot requirements | PARKED_FOR_POST_EXA_T1 | Codex/operator decide after source map review. |
| OUT_OF_SCOPE | Copying external code, licenses, UI, deployment, or translation product behavior | REJECTED_FROM_EXA_T1 | Do not implement or claim. |
| RESOLVED_BY_DESIGN | CVF-native ownership boundary for absorbed ideas | DESIGN_BOUNDARY_SET | Accepted value must become CVF-owned scan-layer candidate contracts. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| EXA-S1 | README smart extraction feature rows | Smart extraction can inform CVF scan-layer routing | ACCEPT_IF_SOURCE_BACKED | README alone may overclaim runtime behavior | SAMPLE_REQUIRED_IN_WORKER_RETURN |
| EXA-S2 | `core/smart_extraction` router/analyzer files | Route/page metrics and strategy decisions may inform scan diagnostics | ACCEPT_IF_SOURCE_BACKED | External app assumptions may not match CVF governance semantics | SAMPLE_REQUIRED_IN_WORKER_RETURN |
| EXA-S3 | EQS and feedback service files | Quality scoring and fallback loops may inform operator-visible scan outcomes | DEFER_OR_ACCEPT_BY_BOUNDARY | Provider fallback, translation quality, and performance claims may bleed into CVF claims | SAMPLE_REQUIRED_IN_WORKER_RETURN |

Rebuildability: worker must record the external remote, commit, enumeration
command, and file-level ledger so Codex can re-run the bounded source review.
Scope guard: accepted value may become only CVF-native scan-layer candidate
contracts. External code, dependency choices, provider fallback behavior, and
README performance claims remain non-authoritative.
Blind-spot guard: worker must report excluded files, unreadable files, and
deferred patterns instead of claiming full-repo absorption.

## Source Verification Table

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Fact class | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| External README names Smart Extraction | canonical external source snapshot | external root readme lines 31-32 | `Smart Extraction` | README feature table | VALUE_SET | ACCEPT |
| External README names translation memory and glossary | canonical external source snapshot | external root readme lines 34-35 | `Translation Memory`, `Glossary Management` | README feature table | VALUE_SET | ACCEPT |
| Router records extraction page-route metrics | canonical external source snapshot | external `core/smart_extraction/extraction_router.py` lines 38-52 | `ExtractionResult` | dataclass | EXISTS | ACCEPT |
| Router analyzes before strategy selection | canonical external source snapshot | external `core/smart_extraction/extraction_router.py` line 118 | `self.analyzer.analyze` | `SmartExtractionRouter.extract` | RUNTIME_BEHAVIOR | ACCEPT |
| Router has OCR language route list | canonical external source snapshot | external `core/smart_extraction/extraction_router.py` lines 134-137 | `ocr_supported_langs` | `SmartExtractionRouter.extract` | VALUE_SET | ACCEPT |
| Document analysis exposes page and document signals | canonical external source snapshot | external `core/smart_extraction/document_analyzer.py` lines 33-80 | `PageAnalysis`, `DocumentAnalysis` | dataclasses | EXISTS | ACCEPT |
| Document analysis thresholds exist | canonical external source snapshot | external `core/smart_extraction/document_analyzer.py` lines 100-102 | `TEXT_COVERAGE_THRESHOLD`, `SCANNED_THRESHOLD`, `COMPLEX_PAGE_THRESHOLD` | `DocumentAnalyzer` | VALUE_SET | ACCEPT |
| EQS defines six quality signals | canonical external source snapshot | external `api/services/eqs.py` lines 5-10 | `text_density`, `structure`, `encoding`, `language`, `completeness`, `format_integrity` | module docstring | VALUE_SET | ACCEPT |
| EQS has weighted signal map | canonical external source snapshot | external `api/services/eqs.py` lines 74-80 | `DEFAULT_WEIGHTS` | module constant | VALUE_SET | ACCEPT |
| Feedback loop defines fallback chain | canonical external source snapshot | external `api/services/extraction_feedback.py` lines 32-37 and 102-103 | `ExtractionStrategy`, `DEFAULT_FALLBACK_CHAIN` | enum and constant | EXISTS | ACCEPT |
| OCR language support contains Vietnamese OCR config | canonical external source snapshot | external `api/services/ocr_language_support.py` lines 122-130 | `LANGUAGE_CONFIGS.vi` | module constant | VALUE_SET | ACCEPT |

## Decision / Baseline

Decision: `DISPATCH_EXA_T1_WORKER_MUST_NOT_COMMIT`.

Claude may inspect the external repository at the pinned commit and produce
analysis artifacts only. Codex remains reviewer and committer.

## Design Control Gate

Design verdict: `PASS_BOUNDED`.

Selected design:

1. Treat external code as learning source, not dependency source.
2. Require source-file evidence for every accepted pattern.
3. Convert accepted ideas into CVF-native candidate contracts.
4. Preserve provider and OCR execution behind later authorization.

Rejected design:

- code import;
- dependency installation;
- provider fallback;
- production/performance claim adoption;
- Policy_Local execution.

## Acceptance Criteria

1. Worker packet includes external remote and commit evidence.
2. Worker packet includes bounded source inventory.
3. Worker packet includes pattern disposition matrix.
4. Worker packet includes CVF-owned candidate recommendations.
5. Worker packet records explicit claim boundary and learning disposition.

## Evidence / Verification

Codex pre-dispatch must pass before this packet is given to Claude.

Worker return must include:

- source map;
- pattern absorption report;
- `git status --short` from CVF workspace after worker artifacts;
- no-commit confirmation.

## Claim Boundary

EXA-T1 authorizes external pattern absorption only. It does not authorize code
import, dependency installation, OCR runtime, provider calls, Policy_Local
mutation, EC activation, retrieval, corpus ingestion, T12, public-sync,
production readiness, public readiness, or third-party performance claims.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private external-source absorption dispatch; no public-sync authorized.
