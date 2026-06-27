# CVF DIR-T1 Document Intelligence Router Source And Tests Worker Return

Memory class: FULL_RECORD

Status: WORKER_RETURN_ACCEPTED_BY_CLAUDE

docType: worker_return

Date: 2026-06-13

Owner: Codex (worker)

Orchestrator / reviewer: Claude

Commit mode: WORKER_MUST_NOT_COMMIT

workOrder:
`docs/work_orders/CVF_AGENT_WORK_ORDER_DIR_T1_DOCUMENT_INTELLIGENCE_ROUTER_SOURCE_AND_TESTS_FOR_CODEX_2026-06-13.md`

GC-018:
`docs/baselines/CVF_GC018_DIR_T1_DOCUMENT_INTELLIGENCE_ROUTER_SOURCE_AND_TESTS_2026-06-13.md`

executionBaseHead: `e426d983`

workerHeadAtReturn: `e426d983`

rawMemoryReleased=false

## Purpose

Return the bounded DIR-T1 worker implementation artifacts to Claude for
review, closure conversion, and commit. This packet records the worker's
evidence while preserving `WORKER_MUST_NOT_COMMIT`.

## Scope / Methodology

Codex read the required front-door/session files, DIR roadmap, DIR-T0 contract
matrix, DIR-T1 GC-018 baseline, work order, scan-route source,
extraction-pipeline source, and existing scan-route tests. Codex then
implemented only the allowed local deterministic source module, focused test
file, overlap checker, and this worker-return packet.

No OCR/provider execution, retrieval mutation, external tree inspection,
public-sync, session-state edit, generated JSON edit, or commit was performed.

## Startup Acknowledgment

Startup acknowledged: current mode=dir_t1_document_intelligence_router_source_and_tests_dispatched; active handoff=AGENT_HANDOFF_V18_2026-06-12.md; work order=DIR-T1; next allowed move=Codex implements allowed-scope DIR-T1 router source, focused tests, and overlap checker under WORKER_MUST_NOT_COMMIT and returns uncommitted; parked checkpoint=DIR-T2, DT-CVF-T0, Policy_Local PL-S1, EC/retrieval, T12, OCR/provider/runtime/public-sync remain parked.

## Worker Return Summary

WORKER_MUST_NOT_COMMIT observed.

Codex created the allowed-scope DIR-T1 deterministic source module, focused
tests, overlap checker, and this worker-return packet. All artifacts remain
uncommitted for Claude review and commit.

## Artifact Manifest

| Artifact | Status | Evidence |
| --- | --- | --- |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | CREATED | deterministic DIR router module |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_router.py` | CREATED | focused pytest coverage |
| `governance/compat/check_dir_disposition_no_scan_overlap.py` | CREATED | overlap checker |
| `docs/reviews/CVF_DIR_T1_DOCUMENT_INTELLIGENCE_ROUTER_SOURCE_AND_TESTS_WORKER_RETURN_2026-06-13.md` | CREATED | this packet |
| work order | UNCHANGED_BY_CODEX | no worker-return status edit required |
| parent roadmap | UNCHANGED_BY_CODEX | Claude reviewer owns closure/status conversion |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: create the DIR-T1 overlap checker required
by the source-verified work order, without changing existing guard semantics or
hook-chain placement.

Protected paths:

- `governance/compat/check_dir_disposition_no_scan_overlap.py`

Operator authorization: the DIR-T1 GC-018 baseline and work
order explicitly authorize this checker as the MC-1 scan-disposition overlap
check. Codex is the worker and must return the checker uncommitted for Claude
review.

Rollback boundary: Claude reviewer may drop or revise only the DIR-T1 checker
and related worker artifacts if the implementation is rejected. Do not revert
DIR-T0 closure commit `082b02ff` or session-sync commit `e426d983`.

## Source Anchor Refresh

| Command | Result summary |
| --- | --- |
| `rg -n "ScanRouteDisposition|SCAN_ROUTE_DECISION_VERSION|class DocumentScanSignals|class ScanRouteDecision|def decide_scan_route" EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | refreshed scan route anchors at lines 20, 31, 40, 58, and 71 |
| `rg -n "ExtractionStatus|class ExtractionQualityReport" EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | refreshed extraction anchors at lines 27 and 101 |
| `rg -n "AuthorizationGate|DownstreamCapability|DocumentProfile|DocumentStructureSignals|DocumentIntelligenceRouteDecision|Derivation Table" docs/reference/CVF_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md` | refreshed DIR-T0 contract anchors including Contract 1, Contract 2, Contract 3, AuthorizationGate, derivation table, and Contract 4 |
| `rg -n "sys.path.insert|from scan_route_decision import" EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_scan_route_decision.py` | refreshed test import convention at lines 10 and 12 |

## Required Proof Manifest

| Proof item | Required literal | Result summary |
| --- | --- | --- |
| Base anchor | `git rev-parse --short HEAD` | `e426d983` |
| Worktree start | `git status --short` | pre-edit state contained untracked `Thong_tin.md` plus untracked DIR-T1 GC-018/work-order dispatch artifacts |
| Pre-implementation gate | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base e426d983 --head HEAD` | PASS |
| Router test run | `python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_router.py -q` | PASS 16/16 |
| Overlap checker run | `python governance/compat/check_dir_disposition_no_scan_overlap.py` | COMPLIANT; AuthorizationGate values 5, ScanRouteDisposition values 4, overlap count 0 |
| Reviewer fast gate | `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` | PASS 13/13 after worker-return Core Guard authorization block was added |
| Pre-commit gate | `python governance/compat/run_local_governance_hook_chain.py --hook pre-commit` | PASS 38/38 |
| Changed file list | `git diff --name-status` | no tracked diff because all worker artifacts are untracked under WORKER_MUST_NOT_COMMIT |
| Worker return state | `git status --short` | untracked allowed DIR-T1 source, test, checker, worker-return, GC-018, and work-order artifacts; pre-existing untracked `Thong_tin.md` remains untouched |

## Work-Order Fulfillment Manifest

| Requirement | Disposition | Evidence |
| --- | --- | --- |
| Startup acknowledgment recorded | PASS | Startup Acknowledgment section |
| Required First Reads completed | PASS | front door, active state, handoff, roadmap, DIR-T0 matrix, GC-018, scan route source, extraction pipeline, scan route test, and work order read |
| Current Runtime Freshness Verification commands summarized | PASS | Source Anchor Refresh section |
| Pre-Flight Checks run | PASS | Required Proof Manifest |
| Router module created | PASS | `document_intelligence_router.py` |
| Focused test file created and passing | PASS | pytest PASS 16/16 |
| Overlap checker created and COMPLIANT | PASS | checker COMPLIANT |
| Worker-return packet created | PASS | this artifact |
| Required Proof Manifest completed | PASS | Required Proof Manifest |
| Changed files remain inside Allowed Implementation Scope | PASS | changed worker artifacts are allowed; `Thong_tin.md` is pre-existing operator untracked file and untouched |
| Claim Boundary and Public Export Disposition included | PASS | sections below |
| `WORKER_MUST_NOT_COMMIT observed` recorded | PASS | Worker Return Summary |

## Findings / Position

Position: worker implementation is ready for Claude review.

No implementation blocker remains in the allowed scope. The router composes
EXA-T2 scan-route symbols by import, keeps `AuthorizationGate` disjoint from
`ScanRouteDisposition`, preserves operator-review and blocked-source
semantics, and stores no raw text, OCR output, provider response, or downstream
application state.

## Risk / Corrective Action

Residual risk: DIR-T1 is a deterministic local contract implementation only.
It has not been validated against operator-approved sample documents and does
not prove OCR/provider/retrieval behavior or downstream use-case readiness.

Corrective action: Claude reviewer should run closure gates, review source and
test semantics, and perform any reviewer-owned completion/session-sync work
before committing. DIR-T2 remains held behind fresh authorization.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| Initial reviewer-fast run before worker-return creation lacked a Core Guard authorization carrier for the new checker | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | N/A_WITH_REASON | Existing core-guard rule worked as intended; worker-return packet now carries the required authorization block |

Runtime/provider/cost lane: `N/A_WITH_REASON` - no provider, OCR, retrieval
runtime, service token, or cost-bearing action was used.

## External Tree Boundary

Codex did not read, list, hash, or modify
`D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Document_Translator`.

Codex did not read, list, hash, or modify any external Policy_Local source
tree.

## Claim Boundary

This worker return covers bounded DIR-T1 deterministic local source and test
work only. It does not prove document intelligence behavior against real
documents, improve extraction accuracy, execute or authorize OCR, call or
authorize providers, change retrieval behavior, prove Policy_Local readiness,
prove Document Translator readiness, authorize public-sync, claim production
or release readiness, authorize memory reinjection, authorize high-risk
promotion, or authorize autonomous mutation.

rawMemoryReleased=false

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance worker-return packet. No public-sync artifact or
public catalog claim is authorized by DIR-T1.
