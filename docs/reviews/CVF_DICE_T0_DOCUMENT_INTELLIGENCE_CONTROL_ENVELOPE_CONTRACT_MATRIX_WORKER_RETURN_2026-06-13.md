# CVF DICE-T0 Document Intelligence Control Envelope Contract Matrix - Worker Return

Memory class: FULL_RECORD

Status: WORKER_RETURN_ACCEPTED_BY_CODEX

docType: review

Date: 2026-06-13

Owner: Claude (worker return); Codex (reviewer/closer)

workOrder:
`docs/work_orders/CVF_AGENT_WORK_ORDER_DICE_T0_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_FOR_CLAUDE_2026-06-13.md`

GC-018:
`docs/baselines/CVF_GC018_DICE_T0_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_2026-06-13.md`

executionBaseHead: `9fe5fc89`

rawMemoryReleased=false

## Purpose

Record Claude's DICE-T0 worker return for Codex review. This packet proves the
allowed doc-only artifacts were created, records worker-side proof results,
flags findings for reviewer disposition, and confirms `WORKER_MUST_NOT_COMMIT`
was observed.

## Target

Worker return packet for DICE-T0 Document Intelligence Control Envelope contract
matrix. Produced under `WORKER_MUST_NOT_COMMIT`. Codex reviewer owns closure,
session sync, and commit.

## Scope

Scope: Claude worker execution of DICE-T0 allowed artifacts only. Worker scope
was doc-only contract matrix and worker return. No runtime source, tests,
checkers, session state, external tree access, OCR/provider, retrieval, corpus
ingestion, or public-sync was authorized or performed.

## Files Created

| Artifact | Path | Status |
| --- | --- | --- |
| DICE-T0 contract matrix | `docs/reference/CVF_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_2026-06-13.md` | CREATED |
| This worker return | `docs/reviews/CVF_DICE_T0_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_WORKER_RETURN_2026-06-13.md` | CREATED |
| Work order (dispatch quality repair only) | `docs/work_orders/CVF_AGENT_WORK_ORDER_DICE_T0_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_FOR_CLAUDE_2026-06-13.md` | MODIFIED (added `## Forbidden Filesystem State At Dispatch` block only; see Finding-To-Governance section) |

## Git Status --short

```
 M docs/work_orders/CVF_AGENT_WORK_ORDER_DICE_T0_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_FOR_CLAUDE_2026-06-13.md
?? docs/reference/CVF_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_2026-06-13.md
?? docs/reviews/CVF_DICE_T0_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_WORKER_RETURN_2026-06-13.md
```

Only allowed artifacts are present. No forbidden paths are modified.

## Proof Manifest Results

| Command | Result | Notes |
| --- | --- | --- |
| `git rev-parse --short HEAD` | `9fe5fc89` | execution base confirmed |
| `git status --short` | see above | only allowed artifacts present |
| `python governance/compat/check_work_order_dispatch_quality.py --base bea8e1f1 --head HEAD --enforce` | PASS (0 violations) | pre-existing violation `missing Forbidden Filesystem State At Dispatch block` was repaired by worker under autonomy rule; re-run confirmed PASS |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base bea8e1f1 --head HEAD` | PASS (COMPLIANT) | all sub-gates pass after structural repair |
| Markdown structural completeness | PASS (0 violations, 4 files checked) | `## Scope` section added to contract matrix to satisfy GC-045 reference type requirement |

## Source Verification Summary

All source facts in the contract matrix were verified against current source
files at execution base `9fe5fc89`. No memory summaries or chat-only references
were used for runtime field citations.

| Source module | Source path | Verified symbols | Outcome |
| --- | --- | --- | --- |
| DIR-T1 router | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | `DOCUMENT_INTELLIGENCE_ROUTE_VERSION` (25), `CLAIM_BOUNDARY` (27), `AuthorizationGate` (35), `DownstreamCapability` (43), `SCAN_ROUTE_TO_AUTHORIZATION_GATE` (51), `OPERATOR_ACTION_BY_GATE` (58), `DocumentProfile` (68), `DocumentStructureSignals` (86), `DocumentIntelligenceRouteDecision` (105/108-114), `decide_document_intelligence_route` (139) | ALL_VERIFIED |
| EXA-T2 scan route | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | `SCAN_ROUTE_DECISION_VERSION` (20), `ScanRouteDisposition` (31), `DocumentScanSignals` (40), `ScanRouteDecision` (58), `decide_scan_route` (71) | ALL_VERIFIED |
| Extraction pipeline | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | `ExtractionQualityReport` (101), `mean_ocr_confidence` (111), `raw_ocr_retained` (113), `ExtractionStorageBoundary` (152), `map_ocr_language_codes` (162), `evaluate_extraction_quality` (235) | ALL_VERIFIED |
| EX-T9 scan outcome report | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | `ScanOutcomeReport` (43), `ScanOutcomeReport.operator_review_required` (51), `ScanOutcomeReport.disposition` (50), `ScanOutcomeReport.findings` (54), `build_scan_outcome_report` (131), `render_scan_outcome_report_markdown` (217) | ALL_VERIFIED |

Minor discrepancy noted: GC-018 and work order source verification block cite
`build_scan_outcome_report` at line 137. Direct source inspection shows the
function symbol (`def build_scan_outcome_report(`) is at line 131; line 137 is
the last parameter line of the function signature. The contract matrix uses the
correct verified line 131. This discrepancy is recorded in the Finding-To-
Governance section and flagged for Codex reviewer.

## Negative Evidence

| Forbidden scope | Status |
| --- | --- |
| External Document Translator tree (`D:/UNG DUNG AI/TOOL AI 2026/CVF-Workspace/Document_Translator`) | NOT_ACCESSED: no file listing, hash, import, or content citation from this tree |
| External Policy_Local tree | NOT_ACCESSED: no file listing, hash, import, or content citation |
| EXTENSIONS runtime source or tests | NOT_CREATED_OR_MODIFIED: no EXTENSIONS file was created or modified |
| governance compatibility checkers | NOT_CREATED_OR_MODIFIED: no checker was created or modified |
| CVF_SESSION session state | NOT_MUTATED: session state files not touched by worker |
| `CVF_SESSION_MEMORY.md` front door | NOT_MUTATED: front door not touched by worker |
| AGENT_HANDOFF handoffs | NOT_MUTATED: handoff files not touched by worker |
| Public-sync repository | NOT_ACCESSED: no public-sync action |
| Provider key files and environment files | NOT_ACCESSED: no key or env file read |
| OCR execution | NOT_PERFORMED: no OCR call or model invocation |
| Provider/API call | NOT_PERFORMED: no provider or API call |
| Retrieval runtime | NOT_CHANGED: no retrieval behavior alteration |
| Corpus ingestion | NOT_PERFORMED: no corpus record added or modified |
| Readiness, cost, or quality claims | NOT_MADE: no readiness, cost, or quality claim |
| Worker commit | NOT_MADE: `WORKER_MUST_NOT_COMMIT` observed; no commit was performed |

rawMemoryReleased=false

## Work-Order Fulfillment Manifest

### Required Artifact Manifest

| Artifact | Required content | Status |
| --- | --- | --- |
| `docs/reference/CVF_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_2026-06-13.md` | DICE-T0 source-owned control-envelope matrix | CREATED |
| `docs/reviews/CVF_DICE_T0_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_WORKER_RETURN_2026-06-13.md` | worker return, evidence, findings, and claim boundary | CREATED (this document) |

### Forbidden Path Manifest

| Path or surface | Status |
| --- | --- |
| `D:/UNG DUNG AI/TOOL AI 2026/CVF-Workspace/Document_Translator` | UNTOUCHED |
| External Policy_Local tree | UNTOUCHED |
| EXTENSIONS runtime source or tests | UNTOUCHED |
| governance compatibility checkers | UNTOUCHED |
| CVF_SESSION session state | UNTOUCHED |
| `CVF_SESSION_MEMORY.md` | UNTOUCHED |
| AGENT_HANDOFF handoffs | UNTOUCHED |
| Public-sync repository | UNTOUCHED |
| Provider key files and environment files | UNTOUCHED |

## Contract Matrix Section Completion

| Required section | Status |
| --- | --- |
| Purpose | PRESENT |
| Scope | PRESENT |
| Source Authority And Owner Map | PRESENT |
| Existing Source-Owned Controls | PRESENT (four role subsections: EnvelopeInputAuthority, EnvelopeReviewSignal, EnvelopeProviderCostBoundary, EnvelopeAdapterHandoff) |
| Proposed DICE Doc-Only Envelope Labels | PRESENT |
| Rejected Duplication Table | PRESENT |
| Provider/OCR/Cost Authorization Boundary | PRESENT |
| Operator-Visible Review Packet Boundary | PRESENT |
| Downstream Adapter Consumption Boundary | PRESENT |
| Machine-Check Candidates For DICE-T1 | PRESENT (10 candidates: DICE-MC-01 through DICE-MC-10) |
| Finding-To-Governance Learning Disposition | PRESENT |
| Claim Boundary | PRESENT |
| Public Export Disposition | PRESENT |

## Findings

Claude reports four findings for Codex reviewer disposition: DICE-T0-F1 through
DICE-T0-F4 in the Finding-To-Governance Learning Disposition table below.

## Risk And Corrective Action

Risk is bounded to dispatch/contract quality. No runtime, external source tree,
provider/OCR, retrieval, corpus-ingestion, public-sync, or readiness surface was
touched. Corrective action is Codex review of the worker repair, acceptance or
adjustment of the line-anchor correction, and carry-forward of DICE-MC-08 into
DICE-T1 if a later source tranche is authorized.

## Finding-To-Governance Learning Disposition

| ID | Finding | Governance learning | Action |
| --- | --- | --- | --- |
| DICE-T0-F1 | Dispatch work order was missing the required `## Forbidden Filesystem State At Dispatch` block, causing dispatch-quality gate to fail. Worker repaired the block under the autonomy rule (allowed-scope gate repair). | Future Codex dispatch work orders that include a `## Forbidden Path Manifest` must also include a `## Forbidden Filesystem State At Dispatch` block. The dispatch quality checker enforces this pairing. Consider adding the block as a template requirement at dispatch time. | MINOR_FINDING_FOR_REVIEWER: Codex should verify the repair was correct; consider adding the block to the DICE-T0 work order template for future lanes. |
| DICE-T0-F2 | GC-018 and work order source verification block cite `build_scan_outcome_report` at line 137; direct source inspection shows the function symbol starts at line 131. Line 137 is the last parameter of the function signature, not the function symbol line. | Work order and GC-018 source line anchors should cite the function definition line (`def ...`), not an intermediate parameter line. Dispatch authors should verify line anchors by searching for `def <function_name>` in source. | ADVISORY_FOR_REVIEWER: contract matrix uses correct verified line 131; GC-018 and work order line 137 reference is technically the function signature endpoint. No material impact on contract correctness. |
| DICE-T0-F3 | Reference document type (path under `docs/reference/`) requires a `## Scope` section per GC-045 structural completeness checker (`scope/applies-to` group). Contract matrix initially lacked this section. Worker added it as an allowed-scope gate repair. | Future reference documents under `docs/reference/` must include a `## Scope` or `## Applies To` or equivalent section. This is already enforced by the GC-045 structural checker; worker should add it proactively. | NOTED_REPAIRED: section added; gate passes. |
| DICE-T0-F4 | DIR `_derive_downstream_eligibility` returns the requested capability for `LOCAL_DETERMINISTIC_ALLOWED` even when the capability is `OPERATOR_REVIEW_ONLY` or `ABSTAIN_OR_BLOCK` (lines 127-129 of `document_intelligence_router.py`). This means `downstream_eligibility` can carry these values even under the permissive gate. Machine-check candidate DICE-MC-08 must account for this invariant to avoid a false-positive widen detection. | DICE-T1 machine-check implementation must be scoped to detect injections of new capability values, not flag the existing DIR passthrough behavior. | ADVISORY_FOR_DICE_T1_REVIEWER: DICE-MC-08 wording in the contract matrix explicitly uses "must not widen" to preserve this invariant. Reviewer should validate the DICE-T1 checker test fixtures cover this edge case. |

### Machine-Readable Learning Disposition

| ID | Defect class | Learning lane | Learning disposition | Next action |
| --- | --- | --- | --- | --- |
| DICE-T0-F1 | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | TEMPLATE_UPDATED | Codex accepts the worker-added dispatch filesystem block in this work order and carries the pattern forward when authoring similar work orders. |
| DICE-T0-F2 | ORCHESTRATOR_PACKET_GAP | DOCUMENTATION_ONLY_LEARNING | N/A_WITH_REASON | Contract matrix uses corrected line 131; no machine-check change because current source verification table still cites an existing signature line. |
| DICE-T0-F3 | WORKER_EXECUTION_ERROR | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | GC-045 already enforces reference `## Scope`; worker repaired the artifact before return. |
| DICE-T0-F4 | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | Preserve DICE-MC-08 for DICE-T1 so future checker tests detect capability widening without rejecting existing DIR passthrough behavior. |
| Runtime/provider/cost lane | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | No runtime, provider, OCR, cost-bearing service, live proof, retrieval runtime, or external service was used or claimed. |

## Acceptance Criteria Self-Check

| Criterion | Status |
| --- | --- |
| Both allowed artifacts exist | PASS |
| Every runtime/source fact cites current source or canonical governed docs | PASS |
| New DICE labels are explicitly doc-only | PASS |
| Matrix rejects confidence, scan route, authorization gate, provider/OCR, and downstream use-case duplication | PASS (see Rejected Duplication Table) |
| Worker-return packet records proof results and negative evidence | PASS |
| No forbidden path or runtime surface was touched | PASS |
| Claude did not commit | PASS - WORKER_MUST_NOT_COMMIT observed |

## Claim Boundary

This worker return records Claude's execution of DICE-T0 allowed artifacts only.
It does not constitute closure, review, or acceptance. Codex reviewer owns the
completion review, any session-state sync, final governance gates, and commit.

DICE-T0 is a doc-only tranche. No runtime implementation, OCR/provider/API
calls, external repo access, retrieval behavior changes, corpus ingestion,
public-sync, Document Translator readiness, Policy_Local readiness, document
correctness, extraction accuracy, provider quality, production readiness, public
readiness, release readiness, cost claims, memory reinjection, high-risk
promotion, or autonomous mutation is authorized or claimed.

rawMemoryReleased=false

WORKER_MUST_NOT_COMMIT observed.

Worker disposition: `WORKER_RETURN_SUBMITTED_UNCOMMITTED`

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

This worker return is a private provenance artifact. No public-sync batch or
public catalog claim is authorized.
