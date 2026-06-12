# CVF EXA-T2 Scan Signal And Route Decision Contracts - Worker Return

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: review

Date: 2026-06-12

Worker: Claude

Reviewer: Codex

Commit mode: WORKER_MUST_NOT_COMMIT

Work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_EXA_T2_SCAN_SIGNAL_ROUTE_DECISION_CONTRACTS_FOR_CLAUDE_2026-06-12.md`

## Purpose

Return uncommitted EXA-T2 source, test, and registry artifacts implementing
deterministic CVF-owned scan-signal and route-decision contracts for the
extraction foundation, for Codex reviewer inspection and commit.

## Target / Source

Target:

- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` (new)
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_scan_route_decision.py` (new)
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` (modified)
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` (modified)

Source authority:

- Work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_EXA_T2_SCAN_SIGNAL_ROUTE_DECISION_CONTRACTS_FOR_CLAUDE_2026-06-12.md`
- GC-018 baseline:
  `docs/baselines/CVF_GC018_EXA_T2_SCAN_SIGNAL_ROUTE_DECISION_CONTRACTS_2026-06-12.md`
- Existing owner surfaces:
  `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` and
  `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py`

## Scope / Methodology

Worker read the work order, GC-018 baseline, and existing owner surfaces
(`ExtractionStatus`, `ExtractionQualityReport`, `map_ocr_language_codes`,
`UnsupportedOcrLanguageError`, `ScanOutcomeReport`, `_QUALITY_FINDINGS`) before
implementation. Pre-flight negative search confirmed no prior owner for
`DocumentScanSignals` or `ScanRouteDecision`. Implementation created one new source
module and one test file, then updated the GC-051 registry. Three iterations of
reviewer-fast were required to resolve non-ASCII encoding violations in registry
updates before PASS.

## Findings / Position

Position: implementation complete and accepted after Codex reviewer inspection.

- All five `ExtractionStatus` values map to stable route dispositions.
- Unsupported source type and unsupported language code both gate to
  `BLOCKED_UNSUPPORTED` without executing OCR.
- `map_ocr_language_codes()` is reused as the language-support gate (dictionary
  lookup only; no OCR engine, no model, no network call).
- No raw extracted text field appears in `DocumentScanSignals` or `ScanRouteDecision`.
- Focused pytest 23/23 PASS after Codex reviewer repair; full
  extraction-foundation pytest 105/105 PASS; reviewer-fast 12/12 PASS.
- GC-051 registry coverage added for both new files.
- No Policy_Local path, EC activation, retrieval, provider, or public-sync
  change is present in the worktree.

## Codex Reviewer Addendum

Codex accepted the packet after two allowed-scope reviewer repairs:

- narrowed the GC-051 JSON/Markdown diff so EXA-T2 did not normalize unrelated
  historical registry punctuation outside the tranche scope;
- added deterministic fail-closed handling for invalid or contradictory scan
  signals, plus two focused tests.

The reviewer repair remains inside EXA-T2 scope. It does not add dependencies,
execute OCR, call providers, mutate Policy_Local, activate EC, change
retrieval, ingest corpus records, or claim readiness.

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| OCR accidentally invoked via language check | `map_ocr_language_codes` performs a dict lookup only; no OCR adapter is passed or called in this module |
| Parallel quality stack created | No new quality report or operator report introduced; `ExtractionStatus` and `UnsupportedOcrLanguageError` are imported from the existing owner |
| Raw content released through decision fields | `ScanRouteDecision` has no text, raw_text, extracted_text, or ocr_output field; covered by focused test |
| Non-determinism | `decide_scan_route` is a pure function with no mutable global state; covered by repeatability test |
| Non-ASCII in registry updates | Fixed before PASS: em-dashes and right-arrow replaced with ASCII equivalents within allowed worker repair scope |

## Pre-Flight Evidence

| Check | Result |
| --- | --- |
| executionBaseHead | `5a3d1262` |
| Dispatch ancestry | HEAD `5a3d1262` descends from dispatch base `8376a31a` via `5ad40259` - PASS |
| Worktree state before edits | clean (no pending changes) |
| Commit mode | WORKER_MUST_NOT_COMMIT acknowledged |

## Negative Search And Collision Discipline

Pre-flight negative searches performed before any edits using grep_search scoped to
`EXTENSIONS/CVF_EXTRACTION_FOUNDATION` and `governance` paths:

| Token searched | Scope | Result | Collision risk |
| --- | --- | --- | --- |
| `DocumentScanSignals` | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION` | absent | None - new symbol created by this worker |
| `ScanRouteDecision` | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION` | absent | None - new symbol created by this worker |
| `ExtractionStrategy` | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION` | absent | No prior extraction strategy owner |
| `EQSReport` | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION` | absent | No prior EQS report owner |
| `provider fallback` | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION` | absent | No provider fallback text in module |

All absent results are for new symbols created by this worker. No collision with
existing non-authoritative occurrences was found.

## Source Verification

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `ExtractionStatus` imported | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 27 | `ExtractionStatus` | extraction_pipeline module | ACCEPT |
| `UnsupportedOcrLanguageError` imported | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 39 | `UnsupportedOcrLanguageError` | extraction_pipeline module | ACCEPT |
| `map_ocr_language_codes` imported | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 162 | `map_ocr_language_codes` | extraction_pipeline module | ACCEPT |

New symbols created by this worker (not prior-source facts):

| New symbol | Created in | Description |
| --- | --- | --- |
| `DocumentScanSignals` | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | New frozen dataclass for normalized scan signals |
| `ScanRouteDecision` | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | New frozen dataclass for deterministic route recommendation |
| `ScanRouteDisposition` | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | New Literal type for four stable route values |
| `decide_scan_route` | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | New deterministic route function |
| `SUPPORTED_SOURCE_TYPES` | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | New frozenset constant for supported source types |

## Changed Files

git status output after edits:

```
 M docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json
 M docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md
?? EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py
?? EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_scan_route_decision.py
?? docs/reviews/CVF_EXA_T2_SCAN_SIGNAL_ROUTE_DECISION_CONTRACTS_WORKER_RETURN_2026-06-12.md
```

All files are uncommitted as required by WORKER_MUST_NOT_COMMIT.

## Implementation Summary

### scan_route_decision.py

Surfaces added in
`EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py`:

- `SUPPORTED_SOURCE_TYPES: frozenset[str]` = {"pdf", "docx"}
- `ScanRouteDisposition`: four stable Literal values
- `DocumentScanSignals`: frozen dataclass with no raw text field
- `ScanRouteDecision`: frozen dataclass with no raw text field
- `decide_scan_route(signals)`: deterministic pure function

### test_scan_route_decision.py

21 focused pytest assertions in
`EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_scan_route_decision.py`.

## Gates Run

| Gate | Command | Result |
| --- | --- | --- |
| Compile changed source | python -m py_compile .../scan_route_decision.py | PASS |
| Focused tests | python -m pytest .../test_scan_route_decision.py -q | PASS 23/23 after Codex reviewer repair |
| Extraction foundation tests | python -m pytest .../tests/ -q | PASS 105/105 after Codex reviewer repair |
| Reviewer-fast | run_local_governance_hook_chain.py --hook reviewer-fast | PASS 12/12 |

## GC-051 Coverage

Two new entries added to `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
and two new rows to `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md`:

- `exa-t2-scan-route-decision-source` covering
  `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py`
- `exa-t2-scan-route-decision-tests` covering
  `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_scan_route_decision.py`

GC-051 corpus scan registry gate: PASS (included in reviewer-fast 12/12).

## Finding-To-Governance Learning Disposition

defectClass: `WORKER_EXECUTION_ERROR`

learningLane: `GOVERNANCE_CONTROL_PLANE`

escalationState: `RULE_EXISTS`

Runtime/provider/cost lane: `N/A_WITH_REASON` - no provider call, no OCR execution,
and no cost-bearing runtime was used in this implementation.

Finding EXA-T2-F1: worker-generated registry rows contained em-dash (U+2014) and
right-arrow (U+2192); caught by the agent packet authority and encoding gate; repaired
within allowed worker repair scope before PASS.

The machine check that caught this finding already exists. No new rule or guard is
required.

Next control action: retain the existing agent packet authority and encoding gate.
Workers writing registry files must use only ASCII characters. Em-dashes as `-`,
arrows as `->` or descriptive prose.

## Claim Boundary

This worker return authorizes deterministic local scan-signal and route-decision
implementation only. It does not prove extraction accuracy, OCR quality, provider
behavior, Policy_Local readiness, EC activation, retrieval quality, current-law
status, production readiness, public readiness, release readiness, memory
reinjection, high-risk promotion, or autonomous mutation.

No OCR, provider, API-key, Policy_Local, EC, retrieval, corpus ingestion,
public-sync, T12, or readiness claim is introduced by this worker return.

## No-Commit Status

WORKER_MUST_NOT_COMMIT boundary observed. All artifacts are uncommitted.
Codex must review, approve, and commit the batch.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_EXA_T2_SCAN_SIGNAL_ROUTE_DECISION_CONTRACTS_FOR_CLAUDE_2026-06-12.md` | Codex-owned closure artifact | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_EXA_T2_SCAN_SIGNAL_ROUTE_DECISION_CONTRACTS_COMPLETION_2026-06-12.md` | reviewer-owned completion artifact | PASS |
| Roadmap state | `docs/roadmaps/CVF_EXTERNAL_EXTRACTION_PATTERN_ABSORPTION_ROADMAP_2026-06-12.md` | Codex-owned roadmap closure state | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | EXA-T2 source/test rows | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | EXA-T2 source/test rows | PASS |
| External evidence digest | EXA-T1 source map | prior verification reused; `sha256:e1bdc496a12c5d313098e7ee45166f0706a84162065bf71c24ca25b9decec603` | PASS |
| System loop interlock | N/A with reason: no loop mutation authorized | no interlock update required | N/A with reason |
| Session continuity | active session files | Codex-owned follow-up sync after material closure commit | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private foundation implementation; public-sync is not authorized by EXA-T2.
