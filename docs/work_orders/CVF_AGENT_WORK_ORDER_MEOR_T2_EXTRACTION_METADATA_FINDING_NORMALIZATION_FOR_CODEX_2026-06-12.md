# CVF Agent Work Order: MEOR-T2 Extraction Metadata Finding Normalization

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-12

Worker: Codex

Reviewer: Codex in separated reviewer pass

Commit mode: WORKER_MAY_COMMIT

dispatchBaseHead: `662e3c76`

executionBaseHead: `427532c8`

closureBaseHead: `d18a3e47`

GC-018:
`docs/baselines/CVF_GC018_MEOR_T2_EXTRACTION_METADATA_FINDING_NORMALIZATION_2026-06-12.md`

## Purpose

Implement the T1 machine semantics in the extraction foundation and expose
normalized operator findings through the existing EX-T9 report surface.

## Authority Chain

| Authority | Path | Status |
| --- | --- | --- |
| Operator direction | 2026-06-12 execute foundation roadmap | ACCEPT |
| Roadmap | `docs/roadmaps/CVF_METADATA_EVIDENCE_AND_OPERATOR_RESOLUTION_FOUNDATION_ROADMAP_2026-06-12.md` | MEOR-T2 `SPEC_PENDING` |
| T1 completion | `docs/reviews/CVF_MEOR_T1_METADATA_EVIDENCE_RESOLUTION_CONTRACT_COMPLETION_2026-06-12.md` | PASS at `22818605` |
| GC-018 | T2 baseline | PASS |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order requirement | Output | Verification |
| --- | --- | --- | --- |
| Normalize metadata findings | deterministic evaluator | new Python module | focused tests |
| Reuse EX-T9 reporting | adapter returns `ScanOutcomeFinding` | new Python module | integration test |
| Retain downstream blocks | exact T1 matrix | evaluator result | 21-pair test |
| No raw content | pointer-only input/output | source and tests | negative assertion |
| No domain defaults | generic identifiers only | source and tests | token inspection |

## Intake Role Routing Decision

- Intake summary: implement bounded deterministic Python behavior from the
  closed MEOR-T1 contract.
- Risk sensitivity: low-risk local control-plane code; no provider, secret,
  external workspace, legal decision, or public claim.
- routeMode: `SINGLE_AGENT_MULTI_ROLE`;
- reason: narrow module/test tranche with deterministic expected outcomes;
- independence control: implementation, test recomputation, and closure review
  occur as separate passes.
- Escalation condition: stop if implementation requires DSCP changes,
  Policy_Local mutation, external content, new dependency, provider use,
  retrieval, gate activation, or a wider claim.

## Agent Roles

| Role | Actor | Responsibility |
| --- | --- | --- |
| Implementer | Codex build pass | module and focused tests |
| Adversarial reviewer | Codex reviewer pass | recompute matrix and inspect boundaries |
| Closer | Codex closure pass | full tests, registries, gates, continuity |

## Single-Agent Multi-Role Control Block

- Role separation ledger: implementer, test reviewer, closer, and committer are
  recorded as separate passes.
- Evidence basis: source inspection, exhaustive matrix tests, full extraction
  tests, git diff, and machine gates.
- Self-review boundary: no independent external review is claimed.
- Escalation conditions: scope expansion, provider/live use, external changes,
  secrets, destructive action, public-sync, or claim-boundary change.
- Gate sequence: pre-dispatch, pre-implementation, reviewer-fast, committed
  material evidence, pre-closure, and continuity sync.

## Worker Autonomy / No-Question Rule

Repair allowed-scope implementation, tests, typing, formatting, and gate
failures without asking the operator. Escalate only for a listed
Return-To-Orchestrator condition.

## Required First Reads

1. T1 contract and semantics references.
2. T1 completion review.
3. `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py`.
4. `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_scan_outcome_report.py`.

## Source Verification Table

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Fact class | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Existing finding type | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | line 32 | `ScanOutcomeFinding` | dataclass | EXISTS | ACCEPT |
| Existing finding injection | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | lines 131-144 | `additional_findings` | `build_scan_outcome_report` | RUNTIME_BEHAVIOR | ACCEPT |
| Existing JSON renderer | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | line 202 | `render_scan_outcome_report_json` | function | EXISTS | ACCEPT |
| Existing Markdown renderer | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | line 217 | `render_scan_outcome_report_markdown` | function | EXISTS | ACCEPT |
| T1 rule matrix | `docs/reference/CVF_METADATA_EVIDENCE_AND_OPERATOR_RESOLUTION_SEMANTICS_2026-06-12.json` | `rules` | `rules` | machine semantics | VALUE_SET | ACCEPT |

## New Runtime Fields And Symbols

| New item | Intended owner | Disposition |
| --- | --- | --- |
| `MetadataEvidenceRecord` | extraction metadata module | DOC_ONLY_NEW |
| `MetadataEvidenceEvaluation` | extraction metadata module | DOC_ONLY_NEW |
| `MetadataEvidenceValidationError` | extraction metadata module | DOC_ONLY_NEW |
| `evaluate_metadata_evidence` | extraction metadata module | DOC_ONLY_NEW |
| `to_scan_outcome_finding` | extraction metadata module | DOC_ONLY_NEW |

## Allowed Scope

- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/metadata_evidence.py`;
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_metadata_evidence.py`;
- T2 baseline, work order, completion, parent roadmap, GC-051, and continuity.

## Forbidden Scope

- editing `scan_outcome_report.py` unless a source-verified incompatibility
  blocks the adapter;
- all DSCP, LPCI, EC, and external Policy_Local source;
- dependencies, OCR, corpus ingestion, retrieval, provider/API-key use;
- public-sync and readiness claims.

## Write Ownership

| Path | Action |
| --- | --- |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/metadata_evidence.py` | CREATE |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_metadata_evidence.py` | CREATE |
| T2 governance and GC-051 surfaces | CREATE/UPDATE |
| other runtime paths | FORBIDDEN |

## Forbidden Filesystem State At Dispatch

- both target Python paths are absent;
- no external Policy_Local path is modified;
- worktree contains only this dispatch packet and roadmap status.

## Pre-Flight Checks

1. Confirm HEAD descends from `22818605` and includes sync `662e3c76`.
2. Confirm T1 completion and both T1 references exist.
3. Confirm target Python paths are absent.
4. Run pre-dispatch autorun on the dispatch range.
5. Commit dispatch and capture execution base.

## Execution Plan

1. Implement immutable input/evaluation records and exact literal values.
2. Evaluate the T1 rule matrix without reading files or source text.
3. Validate identifiers, pointers, action policy, and state combinations.
4. Convert valid evaluations into existing `ScanOutcomeFinding` records.
5. Include only bounded string evidence; release no raw content.
6. Test all allowed pairs and representative invalid records.
7. Inject the finding into an EX-T9 report in a focused integration test.
8. Run focused and full extraction tests.

## Evidence Requirements

- exhaustive rule-pair coverage;
- deterministic equality;
- exact failure tokens;
- source/operator distinction;
- no hint release;
- no mutation or raw-content field;
- focused and full pytest PASS;
- Python compile PASS;
- changed-path and registry evidence.

## Acceptance Criteria

1. All T1 canonical values are represented exactly.
2. All 21 allowed state/basis pairs evaluate deterministically.
3. Invalid combinations fail closed with T1 failure tokens.
4. `DERIVED_HINT` never becomes eligible for re-evaluation.
5. Source and operator evidence remain distinct in report evidence.
6. The adapter uses existing `ScanOutcomeFinding`.
7. EX-T9 renderer source remains unchanged.
8. No domain-specific requirement is hard-coded.
9. No raw content or autonomous mutation appears.
10. Focused and full extraction tests pass.

## Review Gate

The reviewer must independently enumerate the T1 rule matrix, verify all
expected outcomes, inspect failure precedence, and reject any implicit
activation, raw-content field, or domain-specific default.

## Closure Checklist

- [x] Source and tests exist.
- [x] Exact rule matrix and failure tokens pass.
- [x] EX-T9 integration passes without renderer changes.
- [x] Focused and full tests pass.
- [x] GC-051 JSON and Markdown are updated.
- [x] Reviewer-fast and pre-closure pass.
- [x] Roadmap and continuity release only MEOR-T3 specification.

## Return-To-Orchestrator Conditions

Return if T1 cannot be implemented without changing its semantics, editing
DSCP or Policy_Local, adding a dependency, reading raw source content, invoking
a provider/service, or widening the claim.

## Operator Checkpoint

operator.checkpoint.waiver: operator explicitly authorized execution of the
full foundation roadmap. No additional checkpoint is required inside scope.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | T2 completion review | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | foundation roadmap | T2 closed; T3 spec pending | PASS |
| Registry JSON | GC-051 JSON | T2 source/test entries | PASS |
| Registry Markdown | GC-051 Markdown | T2 quick lookup rows | PASS |
| External evidence digest | N/A with reason: repo-local implementation only | no external evidence | N/A with reason |
| System loop interlock | N/A with reason: no loop mutation planned | local adapter only | N/A with reason |
| Session continuity | active state/memory/handoff | T3 spec-only next move | PASS |

## Claim Boundary

This work order authorizes local deterministic normalization only. It does not
authorize domain decisions, metadata correction, gate activation, retrieval,
provider use, external integration, or readiness claims.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private foundation implementation; no public-sync authorized.
