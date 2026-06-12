# CVF GC-018 Baseline: EXA-T2 Scan Signal And Route Decision Contracts

Memory class: FULL_RECORD

Status: DISPATCHED

docType: baseline

Date: 2026-06-12

Owner: Codex

baseHead: `8376a31a`

Parent roadmap:
`docs/roadmaps/CVF_EXTERNAL_EXTRACTION_PATTERN_ABSORPTION_ROADMAP_2026-06-12.md`

Parent closure:
`docs/reviews/CVF_EXA_T1_DICH_TAI_LIEU_SCAN_LAYER_PATTERN_ABSORPTION_COMPLETION_2026-06-12.md`

Work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_EXA_T2_SCAN_SIGNAL_ROUTE_DECISION_CONTRACTS_FOR_CLAUDE_2026-06-12.md`

## Purpose

Authorize a bounded EXA-T2 implementation tranche for deterministic CVF-owned
scan signal and route-decision contracts.

EXA-T2 converts the accepted EXA-T1 external-source learning into local CVF
foundation surfaces. It must not copy external code, install dependencies,
execute OCR, call providers, mutate Policy_Local, or claim readiness.

## Scope / Target / Owner Boundary

In scope:

- add deterministic `DocumentScanSignals` and `ScanRouteDecision` contracts in
  the CVF extraction foundation;
- reuse existing extraction quality, OCR language mapping, storage-boundary,
  and operator scan-report owner surfaces;
- add focused tests for route decisions and no-provider/no-OCR boundaries;
- update GC-051 source/test registry coverage if new source/test files are
  added;
- return uncommitted worker artifacts for Codex review.

Out of scope:

- code import from `nclamvn/dich-tai-lieu` or any external repository;
- dependency installation, OCR model download, OCR execution, or provider call;
- automatic retry, provider fallback, translation memory, glossary, UI, or
  publishing behavior;
- Policy_Local mutation, EC activation, retrieval behavior, corpus ingestion,
  or T12 unlock;
- public-sync, production readiness, public readiness, release readiness, or
  extraction accuracy claim.

## Authority Chain

| Authority | Path or source | Status |
| --- | --- | --- |
| Operator direction | 2026-06-12 next-road direction after EXA-T1 absorption | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | next move permits fresh EXA-T2 authorization |
| Active handoff | `AGENT_HANDOFF_V18_2026-06-12.md` | active handoff requires EXA-T2 fresh authorization |
| Parent roadmap | `docs/roadmaps/CVF_EXTERNAL_EXTRACTION_PATTERN_ABSORPTION_ROADMAP_2026-06-12.md` | EXA-T2 READY_FOR_FRESH_AUTHORIZATION |
| EXA-T1 completion | `docs/reviews/CVF_EXA_T1_DICH_TAI_LIEU_SCAN_LAYER_PATTERN_ABSORPTION_COMPLETION_2026-06-12.md` | CLOSED_PASS_BOUNDED |
| Reviewer-fast hardening | `docs/reviews/CVF_REVIEWER_FAST_RESCAN_GATE_PLACEMENT_HARDENING_COMPLETION_2026-06-12.md` | CLOSED_PASS_BOUNDED |

## Decision / Baseline

Decision: `DISPATCH_EXA_T2_WORKER_MUST_NOT_COMMIT`.

Claude may implement the deterministic EXA-T2 contracts and focused tests
inside the allowed CVF extraction-foundation scope. Codex remains reviewer and
committer.

## Design Control Gate

Design verdict: `PASS_BOUNDED`.

Selected design:

1. Place pre-extraction scan signals and route decisions in CVF-owned
   extraction foundation code.
2. Use deterministic local inputs and outputs only.
3. Reuse the current quality report, OCR language mapping, storage-boundary,
   and scan outcome report instead of creating parallel authorities.
4. Treat OCR/provider work as eligibility or escalation only, not execution.
5. Keep Policy_Local as downstream use-case work after EXA-T2 closure.

Rejected design:

- copying external code or adopting external class names as runtime authority;
- adding a broad extraction router framework;
- auto-running OCR or provider fallback;
- creating a second quality report or operator report stack;
- encoding legal-policy or Policy_Local assumptions into EXA-T2.

## Source / Predecessor Evidence

| Evidence item | Evidence artifact | Disposition |
| --- | --- | --- |
| EXA-T1 external source map | `docs/reference/CVF_EXA_T1_DICH_TAI_LIEU_SCAN_LAYER_PATTERN_SOURCE_MAP_2026-06-12.md` | ACCEPT_AS_PRIOR_VERIFICATION |
| EXA-T1 completion candidate table | `docs/reviews/CVF_EXA_T1_DICH_TAI_LIEU_SCAN_LAYER_PATTERN_ABSORPTION_COMPLETION_2026-06-12.md` | ACCEPT |
| Current extraction quality owner | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | ACCEPT |
| Current scan report owner | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | ACCEPT |

## Current Runtime Freshness Verification

| Runtime surface | Freshness check | Disposition |
| --- | --- | --- |
| Extraction quality owner | `rg -n "class ExtractionQualityReport|def evaluate_extraction_quality" EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` returned lines 101 and 235 | PASS |
| OCR language mapping owner | `rg -n "def map_ocr_language_codes" EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` returned line 162 | PASS |
| OCR adapter boundary | `rg -n "OcrDependencyUnavailableError|def extract_tier2_ocr" EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` returned lines 43 and 187 | PASS |
| Storage-boundary owner | `rg -n "class ExtractionStorageBoundary|def build_extraction_storage_boundary" EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` returned lines 152 and 424 | PASS |
| Scan outcome report owner | `rg -n "class ScanOutcomeReport|def build_scan_outcome_report" EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` returned lines 43 and 131 | PASS |
| Candidate runtime absence | `rg -n "DocumentScanSignals|ScanRouteDecision" EXTENSIONS/CVF_EXTRACTION_FOUNDATION governance --hidden --no-ignore` returned no matches | PASS |
| External app token absence in extraction foundation | `rg -n "ExtractionStrategy|EQSReport|provider fallback|auto.*retry|automatic.*retry" EXTENSIONS/CVF_EXTRACTION_FOUNDATION --hidden --no-ignore` returned no matches | PASS |

## Source Verification Table

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Fact class | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| `ExtractionQualityReport` exists | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 101 | `ExtractionQualityReport` | dataclass | EXISTS | ACCEPT |
| `evaluate_extraction_quality()` exists | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 235 | `evaluate_extraction_quality` | function | EXISTS | ACCEPT |
| `map_ocr_language_codes()` exists | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 162 | `map_ocr_language_codes` | function | EXISTS | ACCEPT |
| OCR execution requires caller adapter | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | lines 187-200 | `extract_tier2_ocr` | function | RUNTIME_BEHAVIOR | ACCEPT |
| `ExtractionStorageBoundary` exists | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 152 | `ExtractionStorageBoundary` | dataclass | EXISTS | ACCEPT |
| `build_extraction_storage_boundary()` exists | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 424 | `build_extraction_storage_boundary` | function | EXISTS | ACCEPT |
| `ScanOutcomeReport` exists | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | line 43 | `ScanOutcomeReport` | dataclass | EXISTS | ACCEPT |
| `build_scan_outcome_report()` exists | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | line 131 | `build_scan_outcome_report` | function | EXISTS | ACCEPT |
| EXA-T1 recommends EXA-T2 deterministic contracts | `docs/reviews/CVF_EXA_T1_DICH_TAI_LIEU_SCAN_LAYER_PATTERN_ABSORPTION_COMPLETION_2026-06-12.md` | lines 472-476 | `DocumentScanSignals`, `ScanRouteDecision` | completion review recommendation | DOC_ONLY_NEW | ACCEPT |

## New Doc-Only Fields

These names are authorized as EXA-T2 implementation candidates. They are not
current runtime facts until the worker creates and tests them.

| Proposed item | Proposed owner | Required worker disposition |
| --- | --- | --- |
| `DocumentScanSignals` | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` or another same-domain extraction-foundation source file | create deterministic local dataclass or equivalent typed contract |
| `ScanRouteDecision` | same owner as `DocumentScanSignals` unless worker records a better same-domain split | create deterministic local result contract |
| `LOCAL_TEXT_EXTRACTION_RECOMMENDED` | route-decision value | allowed when quality/profile signals support local extraction path |
| `OCR_ELIGIBLE_OPERATOR_REVIEW_REQUIRED` | route-decision value | allowed when OCR may be needed but must not execute automatically |
| `ESCALATE_OR_ABSTAIN` | route-decision value | allowed when supplied signals are insufficient, contradictory, or unsupported |
| `BLOCKED_UNSUPPORTED` | route-decision value | allowed when language, source type, or boundary condition is unsupported |

## Evidence Reuse And Encoding Plan

verificationMode: `REUSE_PRIOR_VERIFICATION`

priorVerificationArtifact:
`docs/reference/CVF_EXA_T1_DICH_TAI_LIEU_SCAN_LAYER_PATTERN_SOURCE_MAP_2026-06-12.md`

reuseReason: EXA-T1 already pinned and reconciled the external source snapshot
for pattern absorption. EXA-T2 implements CVF-owned deterministic contracts
from accepted candidate value and does not need to reread or rehash external
binary/source artifacts unless it cites new external facts.

freshRecomputeRequired: NO for external corpus inventory, external repository
hashes, README claims, performance claims, cost claims, OCR quality claims, or
provider behavior. Those claims remain outside EXA-T2.

freshRuntimeVerificationRequired: YES for current CVF source owners and any
new source/test paths the worker creates.

unicodePathHandling: use literal paths and UTF-8-safe readers when tests cover
non-ASCII caller-selected report paths. Do not rename or normalize files to
avoid Unicode handling.

## Negative Search And Collision Discipline

EXA-T2 must distinguish absent runtime ownership from documented candidate
names.

Required worker searches before return:

- search current CVF source/test roots for `DocumentScanSignals`;
- search current CVF source/test roots for `ScanRouteDecision`;
- search current extraction foundation for `ExtractionStrategy` and
  `EQSReport`;
- search changed files for external-provider fallback or automatic retry
  language.

If a token exists only in EXA-T1 docs or this dispatch packet, treat it as
candidate documentation, not runtime evidence.

## Acceptance Criteria

1. Deterministic scan-signal and route-decision contracts exist in CVF-owned
   extraction-foundation source.
2. Route decisions use supplied signals and existing extraction quality owner
   surfaces; they do not read external files, call OCR, call providers, or
   mutate Policy_Local.
3. Focused tests cover pass/local route, OCR-eligible escalation,
   unsupported-language or unsupported-source blocking, low/partial/empty
   extraction escalation, and no raw-content/provider/OCR execution boundary.
4. Existing extraction tests continue to pass.
5. New source/test files are registered in GC-051 if added.
6. Worker return includes actual changed files, gates run, claim boundary, and
   pending no-commit status.

## Evidence / Verification

Worker pending-return evidence must include:

- `executionBaseHead=<hash>` captured before edits;
- `git status --short` with actual pending file list;
- focused pytest command and result;
- extraction-foundation pytest command and result if feasible;
- `python -m py_compile` or equivalent compile check for changed Python files;
- GC-051 check result if registry paths change;
- reviewer-fast result, or explicit `PRE_CLOSURE_NOT_RUN_PENDING_COMMIT` with
  component gates passed and reason.

Codex reviewer closure must commit the approved range and run pre-closure with
a non-empty committed range before any closed-equivalent claim.

## Claim Boundary

EXA-T2 authorizes deterministic local scan-signal and route-decision contracts
only. It does not prove extraction accuracy, OCR quality, provider behavior,
Policy_Local readiness, EC activation, retrieval quality, current-law status,
production readiness, public readiness, release readiness, memory reinjection,
high-risk promotion, or autonomous mutation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private scan-layer foundation dispatch; no public-sync authorized.
