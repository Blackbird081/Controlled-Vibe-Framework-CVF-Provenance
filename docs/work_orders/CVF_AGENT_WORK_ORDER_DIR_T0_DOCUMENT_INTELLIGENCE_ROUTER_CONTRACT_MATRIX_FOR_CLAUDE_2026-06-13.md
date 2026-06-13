# CVF Agent Work Order - DIR-T0 Document Intelligence Router Contract Matrix

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-13

Owner: Codex

Assigned worker: Claude

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `51cd1ded`

executionBaseHead: `51cd1ded`

closureBaseHead: `57799f67`

sourceAuthority:
`docs/baselines/CVF_GC018_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md`

rawMemoryReleased=false

completionReviewPath:
`docs/reviews/CVF_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_COMPLETION_2026-06-13.md`

reviewerOwnedClosurePaths:
`docs/reviews/CVF_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_COMPLETION_2026-06-13.md`;
`CVF_SESSION/ACTIVE_SESSION_STATE.json`;
`CVF_SESSION/state/**`;
`CVF_SESSION_MEMORY.md`;
`AGENT_HANDOFF_V18_2026-06-12.md`

GC-018:
`docs/baselines/CVF_GC018_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md`

Parent roadmap:
`docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md`

## Purpose

Implement the DIR-T0 documentation-only contract matrix for the Document
Intelligence Router foundation. Claude must reconcile current extraction owner
surfaces, define three doc-only contract tables, create an adapter eligibility
matrix, and specify machine-check candidates for a later implementation work
order.

The worker must not implement source code, inspect external use-case trees,
run OCR or providers, change retrieval behavior, edit public-sync, or update
session state.

## Authority Chain

| Authority | Path / evidence | Disposition |
| --- | --- | --- |
| Operator request | operator asked Codex to create the Claude work order after DIR final roadmap | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V18_2026-06-12.md` | ACCEPT |
| Parent roadmap | `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md` | ACCEPT |
| Claude rebuttal | `docs/reviews/CVF_DIR_FOUNDATION_ROADMAP_CLAUDE_REBUTTAL_2026-06-13.md`; commit `fc79fcdf` | ACCEPT |
| Codex finalization review | `docs/reviews/CVF_DIR_FOUNDATION_ROADMAP_CODEX_FINALIZATION_REVIEW_2026-06-13.md` | ACCEPT |
| GC-018 | `docs/baselines/CVF_GC018_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md` | ACCEPT |

## Agent Roles

| Role | Agent | Boundary |
| --- | --- | --- |
| Orchestrator | Codex | dispatches GC-018 and work order only |
| Worker | Claude | authors allowed-scope contract matrix and worker return |
| Reviewer / closer | Codex | reviews, fixes reviewer-owned issues, runs closure gates, commits |

## Intake Role Routing Decision

Intake summary: operator approved opening a work order for Claude after the DIR
foundation roadmap was finalized and the Claude rebuttal was incorporated.

Scope classification: bounded documentation contract and adapter matrix.

Risk sensitivity: medium governance risk because DIR will define the source
contract that later source code may follow. Risk remains bounded because no
runtime code, external tree operation, provider/API proof, OCR, retrieval, or
public-sync action is authorized.

Selected route mode: MULTI_AGENT_MULTI_ROLE.

Role separation basis: Claude acts as implementation worker under
`WORKER_MUST_NOT_COMMIT`; Codex remains reviewer, closer, and committer.

Escalation condition: return to Codex if implementation requires source code,
external workspace access, runtime wiring, generated JSON aggregate editing,
session state, public-sync, provider/API proof, OCR execution, operator sample
documents, or a wider claim boundary.

## Required First Reads

Claude must read:

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `AGENT_HANDOFF_V18_2026-06-12.md`
4. `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md`
5. `docs/reviews/CVF_DIR_FOUNDATION_ROADMAP_CLAUDE_REBUTTAL_2026-06-13.md`
6. `docs/reviews/CVF_DIR_FOUNDATION_ROADMAP_CODEX_FINALIZATION_REVIEW_2026-06-13.md`
7. `docs/baselines/CVF_GC018_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md`
8. `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py`
9. `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py`
10. `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py`
11. this work order

## Startup Acknowledgment Required

Claude must begin with:

`Startup acknowledged: current mode=dir_t0_document_intelligence_router_contract_matrix_dispatched; active handoff=AGENT_HANDOFF_V18_2026-06-12.md; work order=DIR-T0; next allowed move=Claude implements allowed-scope DIR-T0 contract matrix and worker return under WORKER_MUST_NOT_COMMIT and returns uncommitted; parked checkpoint=DIR-T1, DIR-T2, DT-CVF-T0, Policy_Local PL-S1, EC/retrieval, T12, OCR/provider/runtime/public-sync remain parked.`

## Commit Mode And Base-Anchor Lifecycle

| Anchor | Value | Owner | Disposition |
| --- | --- | --- | --- |
| dispatchBaseHead | `51cd1ded` | Codex | ACCEPT |
| executionBaseHead | `51cd1ded` | Claude | ACCEPT |
| closureBaseHead | `WORKER_MUST_NOT_SET` | Codex reviewer | ACCEPT |
| Commit mode | `WORKER_MUST_NOT_COMMIT` | Codex | ACCEPT |

Claude must not commit. Claude must record worker-return base/head and
`git status --short` output in the worker-return packet.

## Dependency Release Evidence

| Dependency | Required evidence | Disposition |
| --- | --- | --- |
| Claude rebuttal exists | `docs/reviews/CVF_DIR_FOUNDATION_ROADMAP_CLAUDE_REBUTTAL_2026-06-13.md`; commit `fc79fcdf`; status `REBUTTAL_FOR_CODEX_REVIEW` | ACCEPT |
| Codex finalization review accepted blockers | `docs/reviews/CVF_DIR_FOUNDATION_ROADMAP_CODEX_FINALIZATION_REVIEW_2026-06-13.md`; status `CLOSED_PASS_BOUNDED` | ACCEPT |
| Final roadmap released only DIR-T0 planning | `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md`; status before this dispatch `FINAL_ROADMAP_AWAITING_DIR_T0_AUTHORIZATION` | ACCEPT |
| Session state synchronized final roadmap | current HEAD before dispatch `51cd1ded` | ACCEPT |
| Fresh DIR-T0 baseline | `docs/baselines/CVF_GC018_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md` | ACCEPT |

## Current Runtime Freshness Verification

Claude must refresh these anchors before editing:

```powershell
rg -n "DIR-T0|DocumentProfile|DocumentStructureSignals|DocumentIntelligenceRouteDecision|DownstreamCapability|Router Composition Model|Required before opening DIR-T0|Public Export Disposition" docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md
rg -n "B1|B2|B3|B4|I1|I2|I3|I4|DownstreamCapability|DocumentIntelligenceRouteDecision" docs/reviews/CVF_DIR_FOUNDATION_ROADMAP_CLAUDE_REBUTTAL_2026-06-13.md docs/reviews/CVF_DIR_FOUNDATION_ROADMAP_CODEX_FINALIZATION_REVIEW_2026-06-13.md
rg -n "ScanRouteDisposition|SCAN_ROUTE_DECISION_VERSION|class DocumentScanSignals|class ScanRouteDecision|def decide_scan_route" EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py
rg -n "ExtractionStatus|class ExtractionQualityReport|class ExtractionStorageBoundary|def map_ocr_language_codes|def evaluate_extraction_quality" EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py
rg -n "class ScanOutcomeReport|def build_scan_outcome_report" EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py
```

## Pre-Flight Checks

Claude must run these before editing:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 51cd1ded --head HEAD
```

If the pre-implementation gate fails only on allowed-scope artifacts, Claude
must repair and rerun under the Worker Autonomy rule. If the failure is outside
allowed scope, Claude must return to Codex.

## Worker Autonomy / No-Question Rule

Claude must repair allowed-scope gate failures without asking the operator or
Codex for permission. This includes wording, status, source-verification,
dispatch-quality, closure-residue, artifact-quality, and proof-manifest defects
inside the two required DIR-T0 worker artifacts or this work order's
worker-return status evidence.

Claude must stop and return to Codex only when the required fix would exceed
Allowed Implementation Scope, change the claim boundary, require runtime code,
inspect an external tree, touch session state, touch public-sync, run
provider/live proof, consume secrets/quota, alter Policy_Local, release a
parked checkpoint, or perform a destructive/irreversible action.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS: scan route version | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | line 20 | `SCAN_ROUTE_DECISION_VERSION` | EXA-T2 scan route module | ACCEPT |
| EXISTS: scan route disposition owner | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | line 31 | `ScanRouteDisposition` | EXA-T2 scan route module | ACCEPT |
| EXISTS: scan signal contract | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | line 40 | `DocumentScanSignals` | EXA-T2 scan route module | ACCEPT |
| EXISTS: scan route decision contract | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | line 58 | `ScanRouteDecision` | EXA-T2 scan route module | ACCEPT |
| EXISTS: route decision function | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | line 71 | `decide_scan_route` | EXA-T2 scan route module | ACCEPT |
| EXISTS: extraction status owner | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 27 | `ExtractionStatus` | extraction pipeline | ACCEPT |
| EXISTS: extraction quality report | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 101 | `ExtractionQualityReport` | extraction pipeline | ACCEPT |
| EXISTS: storage boundary | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 152 | `ExtractionStorageBoundary` | extraction pipeline | ACCEPT |
| EXISTS: OCR language mapping owner | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 162 | `map_ocr_language_codes` | extraction pipeline | ACCEPT |
| EXISTS: extraction quality evaluator | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 235 | `evaluate_extraction_quality` | extraction pipeline | ACCEPT |
| EXISTS: scan outcome report | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | line 43 | `ScanOutcomeReport` | EX-T9 scan outcome report module | ACCEPT |
| EXISTS: scan outcome report builder | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | line 131 | `build_scan_outcome_report` | EX-T9 scan outcome report module | ACCEPT |
| DIR-T0 scope is doc-only contract and adapter matrix work | `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md` | lines 285-333 | `DIR-T0` | DIR roadmap | ACCEPT |
| DIR-T0 must not inspect external use-case source trees | `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md` | lines 318-323 | `Document_Translator`, `Policy_Local` | DIR roadmap | ACCEPT |
| DIR-T0 opening requires fresh GC-018 and source-verified work order | `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md` | lines 455-459 | `Required before opening DIR-T0` | DIR roadmap | ACCEPT |
| Claude rebuttal blockers were incorporated before dispatch | `docs/reviews/CVF_DIR_FOUNDATION_ROADMAP_CODEX_FINALIZATION_REVIEW_2026-06-13.md` | lines 68-97 | `B1`, `B2`, `B3`, `B4`, `I1`, `I2`, `I3`, `I4` | Codex finalization review | ACCEPT |

## New Doc-Only Fields Authorized

These names are new DIR-T0 documentation-contract fields. They are not claimed
as current runtime/source symbols.

| New doc-only field or symbol | Roadmap source | Target contract path | Boundary |
| --- | --- | --- | --- |
| `DocumentProfile` | roadmap lines 224 and 305 | `docs/reference/CVF_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md` | doc-only contract table, not runtime class |
| `requestedCapability` | roadmap lines 224 and 230-232 | same | document profile capability field, not use-case enum |
| `DocumentStructureSignals` | roadmap lines 225 and 305 | same | doc-only contract table, not runtime class |
| `DocumentIntelligenceRouteDecision` | roadmap lines 226 and 306 | same | doc-only contract table, not runtime class |
| `DownstreamCapability` | roadmap lines 230-232 and 308 | same | capability enum proposal, not app name enum |
| `authorization_gate` | roadmap lines 246-276 | same | router-owned authority axis, not scan disposition |
| `downstream_eligibility` | roadmap lines 246-276 | same | capability eligibility axis, not downstream app state |
| `scan_decision_digest` | roadmap lines 224-226 and 305-310 | same | reference digest only, no raw text/OCR/provider output |
| `ADAPTER_CONTRACT_NOT_YET_PUBLISHED` | roadmap lines 324-326 | same | adapter-matrix label for missing published contracts |

## New Files To Create

| Path | Required content |
| --- | --- |
| `docs/reference/CVF_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md` | DIR-T0 contract matrix with owner reconciliation, three contract tables, adapter eligibility matrix, and machine-check candidates |
| `docs/reviews/CVF_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_WORKER_RETURN_2026-06-13.md` | worker return packet with proof manifest and uncommitted artifact list |

## Allowed Implementation Scope

Claude may modify:

- `docs/reference/CVF_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md`
- `docs/reviews/CVF_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_WORKER_RETURN_2026-06-13.md`
- this work order only for worker-return status evidence if needed
- parent roadmap row only to mark worker-return status, not final closure

Claude must not modify:

- `EXTENSIONS/**`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/**`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V18_2026-06-12.md`
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Document_Translator`
- any external Policy_Local source tree
- retrieval, route/API, OCR, provider, corpus, or public-sync surfaces
- provider key files
- generated JSON aggregates

Claude must not read, list, hash, or modify the external Document Translator
or Policy_Local source trees for this work order.

## Write Ownership

| Artifact or surface | Owner | Write permission |
| --- | --- | --- |
| DIR contract matrix | Claude | create and edit |
| DIR-T0 worker-return packet | Claude | create and edit |
| this work order | Claude | edit only for worker-return status evidence if needed |
| parent roadmap row | Claude | edit only to mark worker-return status, not final closure |
| completion review | Codex | reviewer-owned |
| session state, front door, and active handoff | Codex | reviewer-owned session-sync only |
| runtime source, external repos, public-sync | no worker | forbidden in this tranche |

## Execution Plan

1. Read all Required First Reads and record the startup acknowledgment.
2. Refresh the source anchors listed in Current Runtime Freshness Verification.
3. Run Pre-Flight Checks from `dispatchBaseHead` `51cd1ded`.
4. Create the DIR contract matrix under `docs/reference/`.
5. Create the worker-return packet under `docs/reviews/`.
6. Run the Required Proof Manifest commands.
7. Return all changed artifacts uncommitted to Codex.

## Contract Matrix Requirements

The reference contract matrix must include:

- a Current Owner Reconciliation table for `DocumentScanSignals`,
  `ScanRouteDecision`, `decide_scan_route`, `ExtractionQualityReport`,
  `ExtractionStorageBoundary`, and `ScanOutcomeReport`;
- a Collision And Rejection table that rejects duplicate scan-route
  dispositions, raw document text, OCR output, provider response, downstream app
  state, and use-case-named foundation intent values;
- a `DocumentProfile` field table with each field labeled as existing,
  proposed doc-only, or rejected;
- a `DocumentStructureSignals` field table with each field labeled as existing,
  proposed doc-only, or rejected;
- a `DocumentIntelligenceRouteDecision` field table with each field labeled as
  existing, proposed doc-only, or rejected;
- a `DownstreamCapability` table using capability names only:
  `STRUCTURED_TEXT_HANDOFF`, `EVIDENCE_CITATION_HANDOFF`,
  `CORPUS_SCAN_HANDOFF`, `OPERATOR_REVIEW_ONLY`, and `ABSTAIN_OR_BLOCK`;
- an Adapter Eligibility Matrix that may name use-case lanes only as adapter
  rows, not as foundation enum values;
- missing published adapter contracts labeled
  `ADAPTER_CONTRACT_NOT_YET_PUBLISHED`;
- machine-check candidate specs for scan-disposition overlap, use-case name
  leakage, and raw-content/provider-output leakage;
- Claim Boundary and Public Export Disposition sections.

The contract matrix must not claim implementation, runtime behavior, external
repo inventory, OCR/provider proof, retrieval behavior, public readiness,
production readiness, cost improvement, or quality improvement.

## Evidence Requirements

Claude must provide evidence for:

- source anchor refresh from the three extraction foundation files;
- contract matrix coverage for all three proposed contract families;
- adapter matrix boundary discipline, including missing published adapter
  contracts labeled `ADAPTER_CONTRACT_NOT_YET_PUBLISHED`;
- machine-check candidate coverage for scan-disposition overlap, use-case name
  leakage, and raw-content/provider-output leakage;
- changed-file scope from `git diff --name-status`;
- no external Document Translator or Policy_Local tree read, list, hash,
  modification, or import.

## Acceptance Criteria

| Requirement | Acceptance condition |
| --- | --- |
| Source owner reconciliation | current EXA-T2 and EX-T9 owner surfaces are mapped without duplicate ownership |
| Contract tables | `DocumentProfile`, `DocumentStructureSignals`, and `DocumentIntelligenceRouteDecision` each have a field table |
| Capability boundary | `DownstreamCapability` contains capability names only |
| Adapter matrix | use-case names appear only as adapter rows |
| Missing adapter contracts | missing published contracts use `ADAPTER_CONTRACT_NOT_YET_PUBLISHED` |
| Runtime boundary | no `EXTENSIONS/**`, OCR/provider, retrieval, external repo, public-sync, or session-state file is changed |
| Worker return | worker-return packet states `WORKER_MUST_NOT_COMMIT observed` and `rawMemoryReleased=false` |

## Required Proof Manifest Atomic Literal Discipline

Each Required Proof Manifest row must contain one atomic command or one atomic
file path. Do not combine multiple commands in one row. Do not use compound
literal syntax in the command cells.

## Required Proof Manifest

Claude must include command output summaries in the worker-return packet.

| Proof item | Required literal | Expected result |
| --- | --- | --- |
| Base anchor | `git rev-parse --short HEAD` | records worker starting head |
| Worktree start | `git status --short` | records pre-edit worktree state |
| Pre-implementation gate | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 51cd1ded --head HEAD` | PASS or allowed-scope repair then PASS |
| Source anchor refresh | `rg -n "ScanRouteDisposition|SCAN_ROUTE_DECISION_VERSION|class DocumentScanSignals|class ScanRouteDecision|def decide_scan_route" EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | source anchors visible |
| Contract matrix content check | `rg -n "DocumentProfile|DocumentStructureSignals|DocumentIntelligenceRouteDecision|DownstreamCapability|ADAPTER_CONTRACT_NOT_YET_PUBLISHED|Public Export Disposition" docs/reference/CVF_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md` | required terms visible |
| Reviewer fast gate | `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` | PASS or allowed-scope repair then PASS |
| Pre-commit gate | `python governance/compat/run_local_governance_hook_chain.py --hook pre-commit` | PASS or allowed-scope repair then PASS |
| Changed file list | `git diff --name-status` | only allowed files changed |
| Worker return state | `git status --short` | uncommitted artifacts ready for Codex |

## Required Artifact Manifest

| Artifact | Required status in worker return |
| --- | --- |
| `docs/reference/CVF_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md` | created |
| `docs/reviews/CVF_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_WORKER_RETURN_2026-06-13.md` | created |
| this work order | unchanged unless worker-return evidence requires a status note |
| parent roadmap | unchanged unless worker-return evidence requires row-status note |

## Work-Order Fulfillment Manifest

The worker-return packet must include a Work-Order Fulfillment Manifest with
one row per requirement in this work order and dispositions of `PASS`,
`N/A_WITH_REASON`, or `BLOCKED`. Any `BLOCKED` row returns the packet to Codex.

## Closure Checklist

Claude must leave each checklist item checked, marked `N/A_WITH_REASON`, or
marked `BLOCKED` with a return-to-Codex action:

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

## Return-To-Orchestrator Conditions

Return to Codex immediately if:

- any required repair exceeds Allowed Implementation Scope;
- a gate failure requires source/runtime edits, external tree access, session
  state, generated JSON aggregate edits, public-sync, OCR/provider execution,
  secret use, retrieval changes, or operator sample documents;
- adapter matrix work requires inspecting the external Document Translator or
  Policy_Local source tree;
- a required artifact is `BLOCKED`;
- the worker cannot preserve `WORKER_MUST_NOT_COMMIT`.

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Roadmap source | Work-order instruction | Required evidence |
| --- | --- | --- | --- |
| Reuse EXA-T2 scan-route contracts | roadmap lines 42-49 and 165-171 | Source Verification Block and owner reconciliation table | source anchors plus contract matrix |
| Keep scan-layer and DIR authority separate | roadmap lines 246-276 | Contract Matrix Requirements and machine-check candidates | no duplicate scan disposition in DIR axis |
| Use capability names, not use-case names, in foundation enum | roadmap lines 230-242 and 280-282 | `DownstreamCapability` table and adapter matrix rule | use-case names only in adapter rows |
| Keep Document Translator and Policy_Local downstream | roadmap lines 50-57 and 318-326 | Allowed Implementation Scope forbids external tree operations | worker-return changed file list |
| Create three contract tables | roadmap lines 224-226 and 305-306 | Contract Matrix Requirements | matrix includes three tables |
| Add adapter eligibility matrix | roadmap lines 307-309 | Contract Matrix Requirements | adapter matrix labels missing contracts safely |
| Add machine-check candidate spec | roadmap lines 278-283 and 309-310 | Contract Matrix Requirements | machine-check candidate section |
| Keep DIR-T1 and DIR-T2 held | roadmap lines 289-363 | Claim Boundary and Required Artifact Manifest | no source/test/runtime files changed |

## Worker Return Packet Requirements

The worker-return packet must include:

- Startup acknowledgment;
- base/head and `git status --short`;
- list of changed files;
- Required Proof Manifest with command output summaries;
- Work-Order Fulfillment Manifest;
- Contract Matrix Coverage table;
- explicit `WORKER_MUST_NOT_COMMIT observed`;
- explicit `rawMemoryReleased=false`;
- Finding-To-Governance Learning Disposition with `N/A_WITH_REASON` if no
  finding is recorded;
- Claim Boundary;
- Public Export Disposition.

## Review Gate

Codex must not commit the worker return until:

- the changed file list stays inside Allowed Implementation Scope;
- reviewer-fast passes;
- pre-commit passes;
- the worker return states `WORKER_MUST_NOT_COMMIT observed`;
- no runtime, external repo, provider/OCR, retrieval, public-sync, session
  state, or generated aggregate file was changed by Claude.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_COMPLETION_2026-06-13.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md` | `Status: DIR_T0_CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | BLOCKED with reason | no GC-051 registry update authorized for DIR-T0 closure | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason | no GC-051 registry update authorized for DIR-T0 closure | BLOCKED with reason |
| External evidence digest | N/A with reason | no external corpus/provider evidence used | N/A with reason |
| System loop interlock | N/A with reason | no runtime loop mutation authorized | N/A with reason |
| Session continuity | active state/front door/handoff | separate session-sync commit follows material closure when required | N/A with reason |

## Reviewer Closure Conversion

Codex reviewer may later create a completion review and session-sync commit if
the worker return passes. Claude must not create the completion review unless
Codex issues a separate reviewer-owned instruction.

## Operator Checkpoint

No operator checkpoint is required for this dispatch. Operator input is
required only if the worker needs to exceed Allowed Implementation Scope or
asks to inspect external Document Translator or Policy_Local source trees.

## Export Surface Decision

Private provenance only. No public-sync path is authorized.

## Claim Boundary

This work order authorizes bounded DIR-T0 documentation-only contract matrix
work. It does not claim document intelligence behavior exists, router source
code is implemented, scan/extraction accuracy is improved, OCR/provider
behavior is available, retrieval behavior changed, Policy_Local is ready,
Document Translator is ready, public catalog export exists, release proof
exists, memory reinjection is authorized, high-risk promotion is authorized, or
autonomous mutation is authorized.

rawMemoryReleased=false

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

This is a private provenance dispatch work order. No public-sync artifact or
public catalog claim is authorized by this tranche.

## Dispatch Packet Authoring Learning Promotion

Learning lane: governance/control-plane learning.

Disposition: `N/A_WITH_REASON`.

Reason: this work order applies existing dispatch-quality, source-verification,
dependency-release, proof-manifest, and external-tree boundary rules. No new
repeated defect pattern is introduced by dispatch authoring.
