# CVF EXA-T2 Scan Signal And Route Decision Contracts Completion Review

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: completion_review

Date: 2026-06-12

Reviewer: Codex

Worker: Claude, with Codex allowed-scope reviewer repair

Work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_EXA_T2_SCAN_SIGNAL_ROUTE_DECISION_CONTRACTS_FOR_CLAUDE_2026-06-12.md`

Baseline:
`docs/baselines/CVF_GC018_EXA_T2_SCAN_SIGNAL_ROUTE_DECISION_CONTRACTS_2026-06-12.md`

Parent roadmap:
`docs/roadmaps/CVF_EXTERNAL_EXTRACTION_PATTERN_ABSORPTION_ROADMAP_2026-06-12.md`

## Purpose

Close EXA-T2 with deterministic CVF-owned scan-signal and route-decision
contracts inside the extraction foundation.

## Scope / Methodology

Codex reviewed the Claude no-commit packet against the EXA-T2 work order,
source-read the new module and tests, narrowed unrelated registry churn, added
fail-closed validation for invalid or contradictory scan signals, reran focused
and full extraction-foundation tests, and reran reviewer-fast.

Scope remained limited to EXA-T2 source/test/registry/review/roadmap closure
artifacts. No external source was reread or rehashed because EXA-T2 reuses the
EXA-T1 prior verification artifact and implements only repo-local contracts.

## Review Verdict

Verdict: `CLOSED_PASS_BOUNDED`.

EXA-T2 converts the EXA-T1 accepted external-pattern learning into local CVF
contracts without copying external code, installing dependencies, executing
OCR, calling providers, mutating Policy_Local, activating EC, changing
retrieval, ingesting corpus records, or claiming readiness.

## What Changed

- Added `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py`.
- Added `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_scan_route_decision.py`.
- Added EXA-T2 source/test rows to the GC-051 JSON and Markdown registries.
- Closed the EXA-T2 work order, worker return, and parent roadmap row.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order handling | Final artifact | Disposition |
| --- | --- | --- | --- |
| Implement deterministic scan strategy contract | `DocumentScanSignals`, `ScanRouteDecision`, and `decide_scan_route()` | source/tests | PASS |
| Reuse current extraction quality owner | imports `ExtractionStatus` from `extraction_pipeline.py` | source/tests | PASS |
| Reuse OCR language mapping owner | unsupported language uses `map_ocr_language_codes()` only | source/tests | PASS |
| Avoid parallel quality/reporting stack | no new quality report or operator report class | source diff | PASS |
| Preserve OCR/provider boundary | route recommends OCR eligibility only; no OCR/provider call path | source/tests | PASS |
| Keep Policy_Local downstream | no external Policy_Local file changed | git status/diff | PASS |
| Register new source/test files | GC-051 JSON/Markdown entries added | registry diff | PASS |

## Closure Diff Gate

| Requirement | Evidence | Result |
| --- | --- | --- |
| Source implementation | `scan_route_decision.py` created | PASS |
| Focused tests | `test_scan_route_decision.py` created | PASS |
| Registry coverage | EXA-T2 source/test rows added | PASS |
| No external code import | changed source imports only local extraction owner and stdlib | PASS |
| No dependency install | no manifest path changed | PASS |
| No OCR/provider execution | no adapter, model, network, or key path invoked | PASS |
| No Policy_Local/EC/retrieval mutation | no external Policy_Local, EC activation, or retrieval path changed | PASS |
| Registry diff bounded | unrelated historical punctuation normalization removed by Codex | PASS |
| Fail-closed contradictory signals | invalid and contradictory scan signal tests added | PASS |

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Worker repair broadens registry churn outside tranche scope | Codex restored unrelated historical registry text and retained only EXA-T2 rows/header |
| Scan route treats contradictory signals as pass | Codex added invalid/contradictory signal guards and focused tests |
| OCR language mapping is mistaken for OCR execution | Completion records that `map_ocr_language_codes()` is a local mapping check only |
| Contract is mistaken for Policy_Local readiness | Claim boundary and roadmap state keep Policy_Local behind PL-S1 authorization |
| Route decision becomes a parallel quality/report system | Source only consumes current `ExtractionStatus` and adds no report class |

## Source Verification

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS: extraction status owner | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | type alias | `ExtractionStatus` | extraction pipeline | ACCEPT |
| EXISTS: OCR language mapping owner | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | function | `map_ocr_language_codes` | extraction pipeline | ACCEPT |
| EXISTS: unsupported language error | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | class | `UnsupportedOcrLanguageError` | extraction pipeline | ACCEPT |
| EXISTS: scan signal contract | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | dataclass | `DocumentScanSignals` | EXA-T2 module | ACCEPT |
| EXISTS: scan route contract | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | dataclass | `ScanRouteDecision` | EXA-T2 module | ACCEPT |
| EXISTS: route decision function | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | function | `decide_scan_route` | EXA-T2 module | ACCEPT |

## Verification Evidence

| Command | Result |
| --- | --- |
| `python -m py_compile EXTENSIONS\CVF_EXTRACTION_FOUNDATION\src\scan_route_decision.py` | PASS |
| `python -m pytest EXTENSIONS\CVF_EXTRACTION_FOUNDATION\tests\test_scan_route_decision.py -q` | PASS: 23/23 |
| `python -m pytest EXTENSIONS\CVF_EXTRACTION_FOUNDATION\tests -q` | PASS: 105/105 |
| `python governance\compat\run_local_governance_hook_chain.py --hook reviewer-fast` | PASS: 12/12 |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
| --- | --- | --- |
| PASS quality route | `LOCAL_TEXT_EXTRACTION_RECOMMENDED` | PASS |
| OCR-needed route | `OCR_ELIGIBLE_OPERATOR_REVIEW_REQUIRED` | PASS |
| Low-confidence/partial/empty route | `ESCALATE_OR_ABSTAIN` | PASS |
| Unsupported source/language route | `BLOCKED_UNSUPPORTED` | PASS |
| Invalid or contradictory signal route | `ESCALATE_OR_ABSTAIN` | PASS |
| Raw content release | no text/raw_text/extracted_text/ocr_output fields | PASS |
| OCR/provider execution | no execution path | PASS |
| Policy_Local integration | N/A with reason: downstream PL-S lane only | PASS |

## Findings / Position

F-1: Worker initially normalized unrelated historical punctuation in the GC-051
registry while repairing ASCII findings. Codex narrowed the registry diff to
EXA-T2-owned changes before closure.

F-2: Worker implementation mapped the status values correctly but did not
fail-close invalid or contradictory scan signals. Codex added deterministic
validation and two focused tests.

Position: accept EXA-T2 after reviewer repair. Both findings were inside
allowed scope and did not require operator escalation.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| F-1 broad unrelated registry normalization | WORKER_EXECUTION_ERROR | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | Retain existing text encoding and governed file-scope rules; if this recurs, promote focused diff-scope machine check for unrelated historical registry/reference churn |
| F-2 missing contradictory-signal validation | WORKER_EXECUTION_ERROR | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | Closed by EXA-T2 source/tests; no reusable governance rule needed because behavior is contract-specific |

Runtime/provider/cost lane: `N/A_WITH_REASON` - no provider, OCR service,
retrieval runtime, or cost-bearing service was used.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | EXA-T2 work order | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | parent roadmap | `Status: EXA_T2_CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | EXA-T2 source/test entries | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | EXA-T2 quick lookup rows | PASS |
| External evidence digest | EXA-T1 source map | prior verification reused; `sha256:e1bdc496a12c5d313098e7ee45166f0706a84162065bf71c24ca25b9decec603` | PASS |
| System loop interlock | no loop mutation | no interlock update required | N/A with reason |
| Session continuity | active memory/state/handoff | reviewer-owned sync after material closure commit | N/A with reason |

## Claim Boundary

This review proves deterministic local scan-signal and route-decision contract
behavior from supplied signals only. It does not prove extraction accuracy,
OCR quality, provider behavior, Policy_Local readiness, EC activation,
retrieval quality, current-law status, production readiness, public readiness,
release readiness, memory reinjection, high-risk promotion, or autonomous
mutation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance scan-layer foundation closure; public-sync is not
authorized by EXA-T2.
