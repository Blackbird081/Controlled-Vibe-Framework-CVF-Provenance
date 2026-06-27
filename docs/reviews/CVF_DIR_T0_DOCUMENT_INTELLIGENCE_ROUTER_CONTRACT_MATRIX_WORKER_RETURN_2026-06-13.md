# CVF DIR-T0 Document Intelligence Router Contract Matrix - Worker Return

Memory class: FULL_RECORD

Status: WORKER_RETURN_ACCEPTED_BY_CODEX

docType: review

Date: 2026-06-13

Worker: Claude

workOrder:
`docs/work_orders/CVF_AGENT_WORK_ORDER_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_FOR_CLAUDE_2026-06-13.md`

GC-018:
`docs/baselines/CVF_GC018_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md`

dispatchBaseHead: `51cd1ded`

executionBaseHead: `51cd1ded`

workerStartHead: `57799f67`

rawMemoryReleased=false

WORKER_MUST_NOT_COMMIT observed.

## Purpose

Worker return packet for DIR-T0 contract matrix work. Documents startup
acknowledgment, proof manifest results, fulfillment manifest, contract matrix
coverage, and boundary compliance for Codex review before commit.

## Scope / Methodology

Worker implemented the two authorized artifacts under the allowed scope:
`docs/reference/CVF_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md`
and this worker return. Worker did not modify EXTENSIONS, session state,
external repos, retrieval, or public-sync surfaces.

Methodology: read all required first reads; ran pre-flight checks; authored
contract matrix following work order requirements; repaired one allowed-scope
gate failure (non-ASCII em-dash characters); re-ran reviewer-fast and
pre-commit until 38/38 PASS; recorded proof manifest.

## Target / Source

| Item | Path | Disposition |
| --- | --- | --- |
| Contract matrix artifact | `docs/reference/CVF_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md` | CREATED |
| This worker return | `docs/reviews/CVF_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_WORKER_RETURN_2026-06-13.md` | CREATED |
| EXTENSIONS source (read-only) | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/` | READ_ONLY_VERIFIED |
| External Document Translator tree | `D:\...\CVF-Workspace\Document_Translator` | NOT_READ_NOT_MODIFIED |
| External Policy_Local tree | external Policy_Local source | NOT_READ_NOT_MODIFIED |

## Startup Acknowledgment

`Startup acknowledged: current mode=dir_t0_document_intelligence_router_contract_matrix_dispatched; active handoff=AGENT_HANDOFF_V18_2026-06-12.md; work order=DIR-T0; next allowed move=Claude implements allowed-scope DIR-T0 contract matrix and worker return under WORKER_MUST_NOT_COMMIT and returns uncommitted; parked checkpoint=DIR-T1, DIR-T2, DT-CVF-T0, Policy_Local PL-S1, EC/retrieval, T12, OCR/provider/runtime/public-sync remain parked.`

## Required Proof Manifest

| Proof item | Command | Result |
| --- | --- | --- |
| Base anchor | `git rev-parse --short HEAD` | `57799f67` (worker starting head; dispatch base `51cd1ded`) |
| Worktree start | `git status --short` | `?? Thong_tin.md` (pre-existing untracked only; no tracked changes) |
| Pre-implementation gate | `run_agent_autorun_workflow_gate.py --phase pre-implementation --base 51cd1ded --head HEAD` | COMPLIANT |
| Source anchor refresh (scan_route) | `rg -n "ScanRouteDisposition|..." scan_route_decision.py` | all 5 anchors visible at cited lines |
| Contract matrix content check | `rg -n "DocumentProfile|DocumentStructureSignals|..."` | all required terms visible; confirmed present |
| Reviewer-fast gate | `run_local_governance_hook_chain.py --hook reviewer-fast` | 13/13 PASS (after non-ASCII repair; see repair note below) |
| Pre-commit gate | `run_local_governance_hook_chain.py --hook pre-commit` | 38/38 PASS |
| Changed file list | `git diff --name-status` | no tracked diff because worker artifacts are untracked until Codex review |
| Worker return state | `git status --short` | two untracked worker artifacts plus pre-existing `?? Thong_tin.md` |

### Allowed-scope repair note

Reviewer-fast [5/13] agent packet authority and encoding initially FAIL:
13 lines contained em-dash (`--`) characters (non-ASCII) without a Text
Encoding Exception. These were introduced by the initial write of the contract
matrix. Repaired by replacing all em-dash instances with ASCII `--` (replace_all
edit). Reran reviewer-fast: 13/13 PASS. Reran pre-commit: 38/38 PASS. This
repair was within allowed scope (contract matrix artifact only).

## Contract Matrix Coverage

| Required contract or section | Present in matrix | Status |
| --- | --- | --- |
| Owner Reconciliation table (12 symbols) | yes -- all 12 source-verified owner surfaces mapped | PASS |
| Collision And Rejection table | yes -- 13 rejected items with owner citations | PASS |
| `DocumentProfile` field table | yes -- 8 fields, all labeled PROPOSED_DOC_ONLY | PASS |
| `DocumentStructureSignals` field table | yes -- 7 fields, all labeled PROPOSED_DOC_ONLY; 2 rejected fields named | PASS |
| `DocumentIntelligenceRouteDecision` field table | yes -- 7 fields, all labeled PROPOSED_DOC_ONLY | PASS |
| `AuthorizationGate` Literal table | yes -- 5 values, all PROPOSED_DOC_ONLY, fully disjoint from `ScanRouteDisposition` | PASS |
| `AuthorizationGate` derivation table | yes -- total map from 4 `ScanRouteDisposition` values | PASS |
| `DownstreamCapability` table | yes -- 5 capability-shaped values, 2 rejected use-case-named values | PASS |
| Adapter Eligibility Matrix | yes -- 5 rows; 4 lanes labeled `ADAPTER_CONTRACT_NOT_YET_PUBLISHED` | PASS |
| Machine-check candidates | yes -- MC-1 (scan overlap), MC-2 (use-case leakage), MC-3 (raw content) | PASS |
| Claim Boundary section | yes | PASS |
| Public Export Disposition | yes -- `DEFERRED_PRIVATE_ONLY` | PASS |

## Work-Order Fulfillment Manifest

| Requirement | Work order section | Disposition | Notes |
| --- | --- | --- | --- |
| Startup acknowledgment recorded | Startup Acknowledgment Required | PASS | recorded above |
| Required First Reads completed | Required First Reads (11 items) | PASS | all 11 read before execution |
| Runtime Freshness Verification commands summarized | Current Runtime Freshness Verification | PASS | all 5 rg commands run; anchors confirmed |
| Pre-Flight Checks run | Pre-Flight Checks | PASS | base anchor, worktree state, pre-implementation gate |
| Contract matrix artifact created | New Files To Create | PASS | `docs/reference/CVF_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md` |
| Worker-return packet created | New Files To Create | PASS | this artifact |
| Required Proof Manifest completed | Required Proof Manifest | PASS | all 9 rows satisfied |
| Changed files inside Allowed Implementation Scope | Allowed Implementation Scope | PASS | only contract matrix and worker return created; no EXTENSIONS or session-state file touched |
| Claim Boundary and Public Export Disposition included | Contract Matrix Requirements | PASS | both present in contract matrix |
| `WORKER_MUST_NOT_COMMIT observed` | Commit Mode | PASS | recorded in header and this section |
| Source owner reconciliation | Contract Matrix Requirements | PASS | 12 symbols mapped without duplicate ownership |
| Contract tables (3 contracts) | Contract Matrix Requirements | PASS | `DocumentProfile`, `DocumentStructureSignals`, `DocumentIntelligenceRouteDecision` |
| Capability boundary (`DownstreamCapability` capability names only) | Contract Matrix Requirements | PASS | 5 capability-shaped values; 2 use-case names explicitly rejected |
| Adapter matrix (use-case names in adapter rows only) | Contract Matrix Requirements | PASS | use-case lanes appear only as row labels in the matrix |
| Missing adapter contracts labeled `ADAPTER_CONTRACT_NOT_YET_PUBLISHED` | Contract Matrix Requirements | PASS | 4 of 5 lanes fully labeled |
| Runtime boundary (no EXTENSIONS, OCR, external repo, public-sync, session-state change) | Allowed Implementation Scope | PASS | `git diff --name-status` shows only allowed files |
| Worker return states `WORKER_MUST_NOT_COMMIT observed` and `rawMemoryReleased=false` | Worker Return Packet Requirements | PASS | both present |
| Finding-To-Governance Learning Disposition with N/A_WITH_REASON if no finding | Worker Return Packet Requirements | PASS | present in this packet and in the contract matrix |

## Findings / Position

One allowed-scope defect was encountered and repaired during execution:

- Non-ASCII em-dash characters in the initial contract matrix write caused
  agent packet authority and encoding gate failure. Repaired by ASCII
  substitution (replace_all). No governance rule gap identified; the
  CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD already covers this.

No other defects encountered. All acceptance criteria from the work order are
satisfied as recorded in the fulfillment manifest above.

## Required Corrective

None. The one in-scope defect (non-ASCII) was repaired before this return.
All gates PASS.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| Non-ASCII em-dash in initial contract matrix write | WORKER_EXECUTION_ERROR | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | CVF text encoding standard already forbids non-ASCII without exception; if this recurs across multiple workers, add a Write-time pre-check reminder to the work order template |

Runtime/provider/cost lane: `N/A_WITH_REASON` -- no provider, OCR service,
retrieval runtime, or cost-bearing service was used.

## Uncommitted Artifact List

| Artifact | Status |
| --- | --- |
| `docs/reference/CVF_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md` | untracked, ready for Codex review and commit |
| `docs/reviews/CVF_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_WORKER_RETURN_2026-06-13.md` | untracked, ready for Codex review and commit |

Pre-existing untracked (not part of this work order): `Thong_tin.md`

## Closure Checklist

- [x] Startup acknowledgment recorded.
- [x] Required First Reads completed.
- [x] Current Runtime Freshness Verification commands summarized.
- [x] Pre-Flight Checks run.
- [x] Contract matrix artifact created.
- [x] Worker-return packet created.
- [x] Required Proof Manifest completed.
- [x] Changed files remain inside Allowed Implementation Scope.
- [x] Claim Boundary and Public Export Disposition included.
- [x] `WORKER_MUST_NOT_COMMIT observed` recorded.

## Claim Boundary

This worker return reports DIR-T0 documentation contract matrix work. It does
not prove document intelligence behavior, implement router source code, improve
extraction accuracy, execute or authorize OCR, call or authorize providers,
change retrieval behavior, prove Policy_Local readiness, prove Document
Translator readiness, authorize public-sync, claim production or release
readiness, authorize memory reinjection, authorize high-risk promotion, or
authorize autonomous mutation.

rawMemoryReleased=false

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance worker return for Codex review; no public-sync
batch is authorized by this tranche.
