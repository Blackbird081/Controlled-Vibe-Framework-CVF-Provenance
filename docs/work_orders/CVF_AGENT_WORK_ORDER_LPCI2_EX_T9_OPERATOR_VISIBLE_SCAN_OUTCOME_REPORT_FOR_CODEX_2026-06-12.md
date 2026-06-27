# CVF Agent Work Order: LPCI2 EX-T9 Operator-Visible Scan Outcome Report

docType: work_order

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

dispatchBaseHead: `6b8e75a9`

executionBaseHead: `a672f416`

closureBaseHead: `a672f416`

Commit mode: `WORKER_MAY_COMMIT`

completionReviewPath:
`docs/reviews/CVF_LPCI2_EX_T9_OPERATOR_VISIBLE_SCAN_OUTCOME_REPORT_COMPLETION_2026-06-12.md`

Date: 2026-06-12

Assigned to: Codex

---

## Purpose

Implement the domain-agnostic EX-T9 scan outcome report contract selected by
the EX-T9 roadmap. The report must make scan failures visible to a non-coder
operator without coupling EX to Policy_Local or EC.

## Authority Chain

- Operator instruction: finish all EX work before returning to EC.
- Roadmap:
  `docs/roadmaps/CVF_LPCI2_EX_T9_OPERATOR_VISIBLE_SCAN_OUTCOME_REPORT_ROADMAP_2026-06-12.md`.
- GC-018:
  `docs/baselines/CVF_GC018_LPCI2_EX_T9_OPERATOR_VISIBLE_SCAN_OUTCOME_REPORT_2026-06-12.md`.
- EX-T8 material closure: `43eb9624`.
- Design-control standard:
  `docs/reference/CVF_GOVERNED_WORK_LIFECYCLE_AND_DESIGN_CONTROL_STANDARD_2026-06-11.md`.

## Agent Roles

| Role | Agent | Constraint |
| --- | --- | --- |
| Worker | Codex | Implement only EX-T9 source/tests |
| Reviewer | Codex | Review diff, run tests and gates |
| Closer | Codex | Close governance artifacts and session continuity |

## Required First Reads

1. `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py`
2. `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_extraction_pipeline.py`
3. `docs/reviews/CVF_LPCI2_EX_T8_EXTRACTION_AUTHORITY_AND_STORAGE_BOUNDARY_COMPLETION_2026-06-12.md`
4. `docs/roadmaps/CVF_LPCI2_EX_T9_OPERATOR_VISIBLE_SCAN_OUTCOME_REPORT_ROADMAP_2026-06-12.md`
5. `governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md`

## Pre-Flight Checks

1. Confirm `6b8e75a9` is an ancestor of current HEAD.
2. Confirm EX-T8 material commit `43eb9624` exists.
3. Confirm the three proposed EX-T9 runtime symbols remain absent.
4. Run pre-dispatch and pre-implementation autorun gates.
5. Stop if any EC or external Policy_Local write is required.

## Scope

Allowed:

- create `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py`;
- create `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_scan_outcome_report.py`;
- create deterministic JSON/Markdown serializers and UTF-8 file writer;
- update `docs/baselines/CVF_GC018_LPCI2_EX_T9_OPERATOR_VISIBLE_SCAN_OUTCOME_REPORT_2026-06-12.md`;
- update `docs/roadmaps/CVF_LPCI2_EX_T9_OPERATOR_VISIBLE_SCAN_OUTCOME_REPORT_ROADMAP_2026-06-12.md`;
- update `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md`;
- update `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI2_EX_T9_OPERATOR_VISIBLE_SCAN_OUTCOME_REPORT_FOR_CODEX_2026-06-12.md`;
- create `docs/reviews/CVF_LPCI2_EX_T9_OPERATOR_VISIBLE_SCAN_OUTCOME_REPORT_COMPLETION_2026-06-12.md`;
- update `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`;
- update `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md`;
- update `CVF_SESSION_MEMORY.md`;
- update `CVF_SESSION/ACTIVE_SESSION_STATE.json`;
- update `AGENT_HANDOFF_V17_2026-06-07.md`.

Forbidden:

- modify EC runtime/data or the parked EC report;
- modify external Policy_Local;
- ingest corpus files or execute OCR;
- release raw chunks or raw OCR text;
- call providers or use API keys;
- modify retrieval behavior or public-sync.

## Write Ownership

Codex owns:

- the new EX-T9 source and test modules;
- EX-T9 roadmap, GC-018, work order, completion review;
- additive GC-051 registry entries;
- bounded EX-T9 continuity sync.

The parked EC metadata-gap report is read-only and outside this batch.

## Source Verification Table

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| Extraction quality report exists | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 101 | `ExtractionQualityReport` | extraction pipeline dataclass | ACCEPT |
| Quality flags exist | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 105 | `quality_flags` | `ExtractionQualityReport` | ACCEPT |
| Storage boundary exists | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 152 | `ExtractionStorageBoundary` | extraction pipeline dataclass | ACCEPT |
| Boundary hash exists | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 159 | `boundary_sha256` | `ExtractionStorageBoundary` | ACCEPT |
| Storage boundary builder exists | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 424 | `build_extraction_storage_boundary` | extraction pipeline function | ACCEPT |

## New Doc-Only Fields

| Field | Purpose |
| --- | --- |
| `reportVersion` | serialized report version |
| `operatorReviewRequired` | explicit operator checkpoint signal |
| `claimBoundary` | bounded interpretation of report output |

## Current Runtime Freshness Verification

Verified at `6b8e75a9`:

`rg -n "class ExtractionQualityReport|class ExtractionStorageBoundary|quality_flags:|boundary_sha256:|def build_extraction_storage_boundary" EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py`

Negative search:

`rg -n --fixed-strings "ScanOutcomeReport|build_scan_outcome_report|write_scan_outcome_report_files" EXTENSIONS docs governance`

Result: existing EX-T8 source owners are present; EX-T9 symbols are absent.
No provider/API-key path is used by the extraction foundation.

## Negative Search And Collision Discipline

| Token | Result | Disposition |
| --- | --- | --- |
| `ScanOutcomeReport` | absent from source at base | new EX type |
| `build_scan_outcome_report` | absent from source at base | new EX function |
| `write_scan_outcome_report_files` | absent from source at base | new EX function |
| operator metadata gap report | domain-specific document exists | non-collision; not consumed or modified |

## Execution Plan

1. Create immutable `ScanOutcomeFinding` and `ScanOutcomeReport` dataclasses.
2. Map quality flags to stable codes, severity, summary, and required action.
3. Set disposition to `READY_FOR_DOWNSTREAM` only when no finding requires review.
4. Accept optional additional generic findings without domain-specific schema.
5. Render deterministic JSON with sorted keys and a trailing newline.
6. Render Markdown with source evidence, metrics, findings, and claim boundary.
7. Write caller-selected JSON/Markdown paths as UTF-8.
8. Do not serialize descriptor lists, chunk text, or OCR text.
9. Add focused tests, including Unicode filename output.

## Evidence Requirements

- source/test diff;
- py_compile PASS;
- focused EX-T9 pytest PASS;
- full extraction-foundation pytest PASS;
- deterministic JSON parse evidence;
- Unicode path write/read evidence;
- changed-path evidence proving no EC or external workspace mutation;
- reviewer-fast and full pre-commit PASS.

## Acceptance Criteria

- [x] PASS quality produces no operator checkpoint.
- [x] Every current extraction quality flag maps to a stable operator action.
- [x] Additional generic findings force operator review when severity is blocking.
- [x] JSON is deterministic and parses.
- [x] Markdown is readable and bounded.
- [x] Unicode path output passes.
- [x] No raw content is serialized.
- [x] Focused and full extraction tests pass.
- [x] Reviewer-fast and pre-commit gates pass.

## Verification And Evidence

Commands:

- `python -m py_compile EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py`
- `python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_scan_outcome_report.py -q`
- `python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests -q`
- `python governance/compat/check_corpus_scan_registry.py --enforce`
- `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast`

## Fail Conditions

Return blocked if:

- a source owner differs from the Source Verification Table;
- a quality flag lacks a stable action mapping;
- serializers expose descriptor lists or raw text;
- implementation requires EC, Policy_Local, OCR execution, provider, retrieval,
  public-sync, secrets, or destructive action;
- any required focused test or governance gate fails outside repairable scope.

## Review Gate

Reviewer must confirm acceptance criteria, inspect serialized fixtures, run
focused/full tests, run reviewer-fast, run pre-closure on a real committed
range, and verify the changed path list before closure.

## Closure Checklist

- [x] Source verification remains current.
- [x] New source/test modules are within size limits.
- [x] PASS and all four quality-flag mappings are tested.
- [x] Additional generic findings are tested.
- [x] JSON determinism and parse are tested.
- [x] Markdown content is tested.
- [x] Unicode path output is tested.
- [x] Raw content non-release is tested.
- [x] GC-051 registry is updated.
- [x] Completion review and session continuity are finalized.

## Return-To-Orchestrator Conditions

Return only when the implementation is complete and evidence is available, or
when a fail condition exceeds allowed scope. Do not return partial code.

## Operator Checkpoint

operator.checkpoint.waiver: Operator explicitly authorized Codex to finish all
bounded EX foundation work before EC; no provider, secret, public-sync,
destructive action, or domain decision is involved.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order handling |
| --- | --- |
| operator-visible generic report | dataclasses plus Markdown renderer |
| machine-readable report | deterministic JSON renderer |
| non-coder correction path | stable finding summaries and required actions |
| Unicode-safe evidence handling | UTF-8 `pathlib.Path` writer test |
| no domain coupling | no EC or Policy_Local fields |
| no raw content release | serializers omit descriptors and text |

## Intake Role Routing Decision

| Field | Decision |
| --- | --- |
| Intake summary | Operator instructed Codex to finish all EX foundation work before EC. |
| Scope classification | Bounded local Python source/test and governance closure. |
| Risk sensitivity | R2 because operator reports can be misread as semantic validation. |
| Selected canonical route mode | SINGLE_AGENT_MULTI_ROLE |
| Role separation basis | Source verification, separate roadmap/spec/order, focused tests, reviewer-fast, pre-commit, and completion review. |
| Escalation condition | Stop if implementation needs EC decisions, external Policy_Local writes, provider/API keys, OCR execution, retrieval, or public-sync. |

## Single-Agent Multi-Role Control Block

roleMode: `SINGLE_AGENT_MULTI_ROLE`

allowedBecause: operator explicitly authorized Codex to finish the bounded EX
foundation before EC.

roleSeparationMechanism:

- roadmap, GC-018, and work order are separate artifacts;
- source verification and negative search precede implementation;
- focused tests precede reviewer-fast and full pre-commit;
- completion review records findings and claim boundary.

Role separation ledger:

| Role | Evidence surface |
| --- | --- |
| Orchestrator | roadmap, GC-018, source verification, dispatch gate |
| Worker | source/test diff and focused commands |
| Reviewer | test evidence, reviewer-fast, closure diff |
| Closer | committed range, completion packet, continuity sync |

Evidence basis: current source, git diff, focused tests, JSON parsing, Unicode
path test, reviewer-fast, pre-closure, and pre-commit gates. Memory-only claims
are not accepted.

Self-review boundary: independent review is not claimed. Single-agent review is
bounded to the explicit source/test contract and machine gates.

Escalation conditions: stop and return to the operator if scope, risk,
public-sync, provider/live proof, secrets, destructive action, or claim boundary
changes.

Gate sequence: pre-dispatch -> pre-implementation -> focused tests ->
reviewer-fast -> commit/pre-commit -> pre-closure on a real range -> continuity
sync.

forbiddenSelfApprovalClaims:

- extraction or OCR accuracy;
- metadata correctness;
- domain eligibility;
- legal/current status;
- retrieval, production, public, or release readiness.

## Evidence Reuse And Encoding Plan

verificationMode: `REUSE_PRIOR_VERIFICATION`

priorVerificationArtifact:
`docs/reviews/CVF_LPCI2_EX_T8_EXTRACTION_AUTHORITY_AND_STORAGE_BOUNDARY_COMPLETION_2026-06-12.md`

priorVerificationAnchor: `43eb9624`

freshRecomputeRequired: `NO`

recomputeReason: `N/A with reason - EX-T9 consumes repo-local dataclasses and
synthetic tests, not external binary corpus evidence.`

unicodePathHandling: `REQUIRED - write/read UTF-8 report files through
pathlib.Path using a Unicode test filename.`

extractedTextAuthority: `SOURCE_AUTHORITY`

## Worker Autonomy / No-Question Rule

Worker-Autonomy / No-Question Rule: repair any gate failure inside allowed
scope and rerun the gate without asking the operator. Ask only when remediation
would cross forbidden scope, change risk or claim boundary, require
provider/secrets, public-sync, destructive action, or an EC/domain decision.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | completionReviewPath | file and `CLOSED_PASS_BOUNDED` verdict | PASS |
| Roadmap state | EX-T9 roadmap | closed row/status | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | EX-T9 source/test entries | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | EX-T9 quick lookup rows | PASS |
| External evidence digest | N/A with reason: no external artifact | repo-local synthetic evidence | N/A with reason |
| System loop interlock | no system-loop mutation | local report generator only | N/A with reason |
| Session continuity | active memory/state/handoff | EX-T9 closure and next move | PASS |

## Reviewer Closure Conversion Block

Reviewer replaced all provisional rows, resolved every acceptance checkbox,
captured the implementation base, and prepared continuity for the material
closure commit.

## Claim Boundary

EX-T9 authorizes deterministic report generation only. It does not authorize
semantic correction, domain activation, retrieval, provider use, or readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance EX foundation work; no public-sync authorized.
