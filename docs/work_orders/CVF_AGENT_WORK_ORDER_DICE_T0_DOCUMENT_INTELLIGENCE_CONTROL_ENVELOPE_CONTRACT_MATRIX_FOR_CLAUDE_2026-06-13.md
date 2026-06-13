# CVF Agent Work Order - DICE-T0 Document Intelligence Control Envelope Contract Matrix

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: work_order

Date: 2026-06-13

Owner: Codex (orchestrator)

Assigned worker: Claude

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `bea8e1f1`

executionBaseHead: `bea8e1f1`

closureBaseHead: `WORKER_MUST_NOT_SET`

sourceAuthority:
`docs/baselines/CVF_GC018_DICE_T0_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_2026-06-13.md`

rawMemoryReleased=false

completionReviewPath:
`docs/reviews/CVF_DICE_T0_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_COMPLETION_2026-06-13.md`

reviewerOwnedClosurePaths:
`docs/reviews/CVF_DICE_T0_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_COMPLETION_2026-06-13.md`;
`CVF_SESSION/ACTIVE_SESSION_STATE.json`;
`CVF_SESSION/state/**`;
`CVF_SESSION_MEMORY.md`;
`AGENT_HANDOFF_V18_2026-06-12.md`

GC-018:
`docs/baselines/CVF_GC018_DICE_T0_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_2026-06-13.md`

Parent roadmap:
`docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_ROADMAP_2026-06-13.md`

Predecessor tranche:
`docs/reviews/CVF_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_COMPLETION_2026-06-13.md`

## Purpose

Create a doc-only DICE-T0 contract matrix for the Document Intelligence Control
Envelope. Claude must map current extraction foundation and DIR owner surfaces
into a reusable control envelope that downstream document workflows can consume
without redefining scan route, authorization gate, confidence/review, provider
OCR, or cost boundaries.

This work order is foundation hardening. It is not Document Translator
implementation work.

## Authority Chain

| Authority | Path / evidence | Disposition |
| --- | --- | --- |
| Operator request | operator asked Codex to continue opening a CVF foundation roadmap and create a Claude work order | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V18_2026-06-12.md` | ACCEPT |
| Parent roadmap | `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_ROADMAP_2026-06-13.md` | ACCEPT |
| DIR-T2 completion | `docs/reviews/CVF_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_COMPLETION_2026-06-13.md` | ACCEPT |
| GC-018 | `docs/baselines/CVF_GC018_DICE_T0_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_2026-06-13.md` | ACCEPT |

## Agent Roles

| Role | Agent | Boundary |
| --- | --- | --- |
| Orchestrator | Codex | dispatches roadmap, GC-018, and work order |
| Worker | Claude | authors allowed-scope DICE-T0 matrix and worker return |
| Reviewer / closer | Codex | reviews, fixes reviewer-owned issues, runs closure gates, commits |

## Intake Role Routing Decision

Intake summary: operator selected another CVF foundation lane after DIR-T2
closure. The selected lane is DICE-T0, a reusable document-control envelope
contract matrix.

Scope classification: doc-only contract matrix and source map.

Risk sensitivity: medium governance risk because DICE defines boundaries that
later use-case and runtime lanes may consume. Risk remains bounded because the
worker may not implement runtime source, execute OCR/providers, read external
use-case trees, or make readiness/cost/quality claims.

Selected route mode: MULTI_AGENT_MULTI_ROLE.

Role separation basis: Claude acts as worker under `WORKER_MUST_NOT_COMMIT`;
Codex remains reviewer, closer, and committer.

Escalation condition: return `BLOCKED_SCOPE_EXPANSION` if Claude needs
external Document Translator files, Policy_Local files, OCR/provider/API
execution, retrieval runtime, corpus ingestion, public-sync, session-state
mutation, or a claim outside the doc-only foundation boundary.

## Required First Reads

Claude must read:

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `AGENT_HANDOFF_V18_2026-06-12.md`
4. `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_ROADMAP_2026-06-13.md`
5. `docs/baselines/CVF_GC018_DICE_T0_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_2026-06-13.md`
6. `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md`
7. `docs/reference/CVF_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md`
8. `docs/roadmaps/CVF_DOCUMENT_TRANSLATOR_CONTROL_ADAPTATION_ROADMAP_2026-06-13.md`
9. `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py`
10. `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py`
11. `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py`
12. `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py`
13. this work order

## Startup Acknowledgment Required

Claude must begin with:

`Startup acknowledged: current mode=dice_t0_document_intelligence_control_envelope_contract_matrix_dispatched; active handoff=AGENT_HANDOFF_V18_2026-06-12.md; work order=DICE-T0; next allowed move=Claude creates the doc-only DICE-T0 contract matrix and worker-return packet under WORKER_MUST_NOT_COMMIT; parked checkpoint=DT-CVF-T0, Policy_Local PL-S1, external Document Translator repo, OCR/provider/retrieval/runtime, corpus ingestion, public-sync, T12, readiness/cost/quality claims remain parked.`

## Commit Mode And Base-Anchor Lifecycle

| Anchor | Value | Owner | Disposition |
| --- | --- | --- | --- |
| dispatchBaseHead | `bea8e1f1` | Codex | ACCEPT |
| executionBaseHead | `bea8e1f1` | Claude | ACCEPT |
| closureBaseHead | `WORKER_MUST_NOT_SET` | Codex reviewer | ACCEPT |
| Commit mode | `WORKER_MUST_NOT_COMMIT` | Codex | ACCEPT |

Claude must not commit. Claude must record worker-return base/head and
`git status --short` output in the worker-return packet.

## Dependency Release Evidence

| Dependency | Required evidence | Disposition |
| --- | --- | --- |
| DIR-T2 foundation pilot closed | `docs/reviews/CVF_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_COMPLETION_2026-06-13.md` at material closure commit `e3395acc` | ACCEPT |
| DIR-T2 session state synchronized | current dispatch base `bea8e1f1` | ACCEPT |
| Operator selected new CVF foundation lane | 2026-06-13 operator instruction in chat | ACCEPT |
| Fresh DICE roadmap | `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_ROADMAP_2026-06-13.md` | ACCEPT |
| Fresh DICE-T0 baseline | `docs/baselines/CVF_GC018_DICE_T0_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_2026-06-13.md` | ACCEPT |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS: DIR route version | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 25 | `DOCUMENT_INTELLIGENCE_ROUTE_VERSION` | DIR-T1 router module | ACCEPT |
| EXISTS: DIR claim boundary | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 27 | `CLAIM_BOUNDARY` | DIR-T1 router module | ACCEPT |
| EXISTS: DIR authorization gate | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 35 | `AuthorizationGate` | DIR-T1 router module | ACCEPT |
| EXISTS: DIR downstream capability | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 43 | `DownstreamCapability` | DIR-T1 router module | ACCEPT |
| EXISTS: scan-to-gate map | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 51 | `SCAN_ROUTE_TO_AUTHORIZATION_GATE` | DIR-T1 router module | ACCEPT |
| EXISTS: document profile | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 68 | `DocumentProfile` | DIR-T1 router module | ACCEPT |
| EXISTS: structure signals | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 86 | `DocumentStructureSignals` | DIR-T1 router module | ACCEPT |
| EXISTS: route decision | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 105 | `DocumentIntelligenceRouteDecision` | DIR-T1 router module | ACCEPT |
| EXISTS: route function | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | line 139 | `decide_document_intelligence_route` | DIR-T1 router module | ACCEPT |
| EXISTS: scan route version | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | line 20 | `SCAN_ROUTE_DECISION_VERSION` | EXA-T2 scan-route module | ACCEPT |
| EXISTS: scan disposition | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | line 31 | `ScanRouteDisposition` | EXA-T2 scan-route module | ACCEPT |
| EXISTS: scan signals | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | line 40 | `DocumentScanSignals` | EXA-T2 scan-route module | ACCEPT |
| EXISTS: scan route function | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | line 71 | `decide_scan_route` | EXA-T2 scan-route module | ACCEPT |
| EXISTS: extraction quality report | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 101 | `ExtractionQualityReport` | extraction pipeline | ACCEPT |
| EXISTS: OCR confidence owner field | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 111 | `mean_ocr_confidence` | extraction quality report | ACCEPT |
| EXISTS: raw OCR retention owner field | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 113 | `raw_ocr_retained` | extraction quality report | ACCEPT |
| EXISTS: extraction quality evaluator | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | line 235 | `evaluate_extraction_quality` | extraction pipeline | ACCEPT |
| EXISTS: operator scan outcome report | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | line 43 | `ScanOutcomeReport` | scan outcome report module | ACCEPT |
| EXISTS: scan outcome report builder | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | line 137 | `build_scan_outcome_report` | scan outcome report module | ACCEPT |
| EXISTS: scan report markdown renderer | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | line 217 | `render_scan_outcome_report_markdown` | scan outcome report module | ACCEPT |
| EXISTS: DIR-T2 closed | `docs/reviews/CVF_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_COMPLETION_2026-06-13.md` | Status line | `CLOSED_PASS_BOUNDED` | DIR-T2 completion review | ACCEPT |
| EXISTS: DT-CVF remains separate use-case lane | `docs/roadmaps/CVF_DOCUMENT_TRANSLATOR_CONTROL_ADAPTATION_ROADMAP_2026-06-13.md` | lines 267-290 | downstream-use-case boundary | DT-CVF roadmap | ACCEPT |

## New Doc-Only Fields

The following labels may be introduced in the DICE-T0 matrix as doc-only
contract labels. They must not be presented as existing runtime symbols:

| New doc-only label | Purpose | Boundary |
| --- | --- | --- |
| `DocumentIntelligenceControlEnvelope` | names the future reusable envelope | doc-only at DICE-T0 |
| `EnvelopeInputAuthority` | classifies source-owned inputs | doc-only at DICE-T0 |
| `EnvelopeReviewSignal` | classifies operator-visible review signals | doc-only at DICE-T0 |
| `EnvelopeProviderCostBoundary` | classifies provider/OCR/cost authorization state | doc-only at DICE-T0 |
| `EnvelopeAdapterHandoff` | classifies downstream adapter consumption | doc-only at DICE-T0 |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Roadmap evidence | Work-order section | Verification |
| --- | --- | --- | --- |
| DICE-T0 is doc-only | roadmap DICE-T0 Detail | Purpose; Runtime Authorization | worker return negative evidence |
| source-map existing owner surfaces | roadmap Scope and Relationship To DIR | Source Verification Block; Deliverables | contract matrix owner map |
| keep provider/OCR/cost blocked | roadmap Design Control Gate | Deliverables; Forbidden Path Manifest | boundary table |
| keep Document Translator downstream | roadmap Scope and Claim Boundary | Required First Reads; Forbidden Path Manifest | no external tree access evidence |
| define machine-check candidates | roadmap DICE-T0 Detail | Deliverables | candidate table in matrix |

## Worker Autonomy / No-Question Rule

Claude must repair allowed-scope gate failures without asking the operator.
Claude must return `BLOCKED_SCOPE_EXPANSION` only if the repair would touch
forbidden paths, alter the claim boundary, require external repo access, run
OCR/provider/API, mutate retrieval/corpus/session state, use public-sync, or
make readiness/cost/quality claims.

## Pre-Flight Checks

Before implementation, Claude must:

1. Read every Required First Reads path.
2. Confirm `git rev-parse --short HEAD`.
3. Confirm `git status --short`.
4. Confirm the external Document Translator and Policy_Local trees are not
   read, listed, hashed, modified, or imported.
5. Use current source files over memory or prior summaries for every source
   fact.

## Single-Agent Multi-Role Control Block

| Control item | Requirement | Disposition |
| --- | --- | --- |
| Role separation ledger | Codex=orchestrator/reviewer/closer; Claude=worker only | ACCEPT |
| Evidence basis independent of memory | closure must rely on git diff, source files, worker return, reviewer-fast, pre-closure, and pre-push evidence | ACCEPT |
| Self-review boundary | Claude worker return is not independent review; Codex review is required | ACCEPT |
| Escalation conditions | any need for external files, OCR/provider/API, retrieval, session mutation, public-sync, or widened claim returns blocked | ACCEPT |
| Gate sequence | Codex dispatch uses pre-dispatch; Claude worker uses required proofs; Codex review uses reviewer-fast and closure gates | ACCEPT |
| Raw memory boundary | rawMemoryReleased=false | ACCEPT |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact:
`docs/reviews/CVF_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_COMPLETION_2026-06-13.md`

recomputeReason: DICE-T0 is a new envelope contract and must source-map current
owner surfaces directly.

unicodePathHandling: literal UTF-8-safe repository paths only.

extractedTextAuthority: N/A with reason - no sample document text or OCR output
is authorized.

Evidence reuse is limited to source-verified contracts and current runtime
source. Memory summaries and chat reports are not source authority for runtime
fields.

## Allowed Implementation Scope

Claude may create:

- `docs/reference/CVF_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_2026-06-13.md`;
- `docs/reviews/CVF_DICE_T0_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_WORKER_RETURN_2026-06-13.md`.

Claude may update this work order only to add worker-return evidence if needed.

## Allowed / Forbidden Scope

Allowed scope:

- create the DICE-T0 reference contract matrix;
- create the DICE-T0 worker-return packet;
- run local documentation/governance checkers listed in the Required Proof
  Manifest;
- cite current in-repo source files and current governed docs.

Forbidden scope:

- external Document Translator source access;
- Policy_Local source access or mutation;
- OCR/provider/API/service execution;
- retrieval runtime or corpus ingestion;
- runtime source implementation;
- tests, checkers, or generated aggregate edits;
- session-state, handoff, or front-door mutation by Claude;
- public-sync;
- readiness, cost, quality, hosted, production, or public claims.

## Forbidden Path Manifest

| Path or surface | Boundary |
| --- | --- |
| `D:/UNG DUNG AI/TOOL AI 2026/CVF-Workspace/Document_Translator` | do not read, list, hash, import, or modify |
| external Policy_Local tree | do not read, list, hash, import, or modify |
| `EXTENSIONS/**` | do not create or modify runtime source/tests |
| `governance/compat/**` | do not create or modify checkers |
| `CVF_SESSION/**` | worker session-state mutation not authorized |
| `CVF_SESSION_MEMORY.md` | worker front-door mutation not authorized |
| `AGENT_HANDOFF*.md` | worker handoff mutation not authorized |
| public-sync repository | not authorized |
| provider key files and environment files | not authorized |

## Deliverables

Claude must create:

1. `docs/reference/CVF_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_2026-06-13.md`
2. `docs/reviews/CVF_DICE_T0_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_WORKER_RETURN_2026-06-13.md`

The contract matrix must include these sections:

- Purpose
- Source Authority And Owner Map
- Existing Source-Owned Controls
- Proposed DICE Doc-Only Envelope Labels
- Rejected Duplication Table
- Provider/OCR/Cost Authorization Boundary
- Operator-Visible Review Packet Boundary
- Downstream Adapter Consumption Boundary
- Machine-Check Candidates For DICE-T1
- Finding-To-Governance Learning Disposition
- Claim Boundary
- Public Export Disposition

The worker-return packet must include:

- files created;
- `git status --short`;
- proof manifest results;
- negative evidence for external tree access, runtime implementation,
  OCR/provider/API, retrieval, corpus ingestion, public-sync, readiness, cost,
  and quality claims;
- worker disposition `WORKER_RETURN_SUBMITTED_UNCOMMITTED`.

## Required Artifact Manifest

| Artifact | Required content | Owner |
| --- | --- | --- |
| `docs/reference/CVF_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_2026-06-13.md` | DICE-T0 source-owned control-envelope matrix | Claude |
| `docs/reviews/CVF_DICE_T0_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_WORKER_RETURN_2026-06-13.md` | worker return, evidence, findings, and claim boundary | Claude |

## Work-Order Fulfillment Manifest

Claude must report each Required Artifact Manifest row as created, updated, or
blocked. Claude must also report each Forbidden Path Manifest row as untouched
or blocked.

## Write Ownership

| Path | Owner | Boundary |
| --- | --- | --- |
| `docs/reference/CVF_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_2026-06-13.md` | Claude | create/update allowed |
| `docs/reviews/CVF_DICE_T0_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_CONTRACT_MATRIX_WORKER_RETURN_2026-06-13.md` | Claude | create/update allowed |
| completion review artifact | Codex | reviewer-owned closure only |
| session front door and active state | Codex | reviewer-owned session sync only |
| active handoff | Codex | reviewer-owned session sync only |

## Required Proof Manifest

| Command or evidence | Required result | Worker-owned |
| --- | --- | --- |
| `git rev-parse --short HEAD` | records execution base | yes |
| `git status --short` | shows only allowed DICE-T0 worker artifacts and any pre-existing operator-owned dirt | yes |
| `python governance/compat/check_work_order_dispatch_quality.py --base bea8e1f1 --head HEAD --enforce` | PASS or N/A with reason if worker did not alter dispatch packet | yes |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base bea8e1f1 --head HEAD` | PASS or N/A with reason if worker did not alter dispatch packet | yes |

No runtime test, OCR proof, provider proof, live proof, external repo scan, or
public-sync proof is required or allowed for the worker.

## Execution Plan

1. Read the Required First Reads.
2. Re-run source searches for every field or symbol cited in the matrix.
3. Create the DICE-T0 matrix with owner, boundary, adapter, and machine-check
   candidate tables.
4. Create the worker-return packet with proof results and negative evidence.
5. Confirm only allowed artifacts are changed.
6. Return uncommitted artifacts to Codex.

## Evidence Requirements

Claude's worker-return packet must include:

- `WORKER_MUST_NOT_COMMIT observed`;
- `rawMemoryReleased=false`;
- changed-file list from `git status --short`;
- source-verification summary;
- proof command summaries;
- explicit statement that no external Document Translator tree, Policy_Local
  tree, public-sync, OCR/provider/API, retrieval runtime, corpus ingestion, or
  session-state mutation was used;
- Finding-To-Governance Learning Disposition, using `N/A_WITH_REASON` only if
  no reusable finding appears.

## Acceptance Criteria

Codex may accept the worker return only if:

- both allowed artifacts exist;
- every runtime/source fact in the matrix cites current source or canonical
  governed docs;
- new DICE labels are explicitly doc-only;
- the matrix rejects confidence, scan route, authorization gate, provider/OCR,
  and downstream use-case duplication;
- the worker-return packet records proof results and negative evidence;
- no forbidden path or runtime surface was touched;
- Claude did not commit.

## Reviewer Closure Conversion

Codex must treat Claude's worker return as pending evidence, not closure.
Codex owns the completion review, any session-state sync, final gates, and
commit.

## Review Gate

Codex reviewer must verify:

- Claude honored `WORKER_MUST_NOT_COMMIT`;
- all Required Artifact Manifest rows are present or explicitly blocked;
- Required Proof Manifest commands pass or have safe diagnostics;
- no forbidden path or external runtime was used;
- claim boundary remains foundation-only.

## Closure Checklist

| Item | Required closure disposition |
| --- | --- |
| Worker return reviewed | PASS, BLOCKED, or N/A with reason |
| Required proofs reviewed | PASS, BLOCKED, or N/A with reason |
| Source verification reviewed | PASS, BLOCKED, or N/A with reason |
| Forbidden scope checked | PASS, BLOCKED, or N/A with reason |
| Finding-To-Governance disposition reviewed | PASS, BLOCKED, or N/A with reason |
| Session continuity updated by reviewer | PASS, BLOCKED, or N/A with reason |

## Return-To-Orchestrator Conditions

Return `BLOCKED_SCOPE_EXPANSION` if any required result needs:

- external Document Translator source access;
- Policy_Local source access;
- OCR/provider/API execution;
- retrieval runtime or corpus ingestion;
- runtime source, tests, checkers, or generated aggregate edits;
- session-state or handoff mutation by Claude;
- public-sync;
- readiness, quality, cost, hosted, production, or public claim.

## Operator Checkpoint

No operator checkpoint is required for DICE-T0 doc-only matrix work. Operator
checkpoint is required if Claude or Codex needs external Document Translator
access, Policy_Local access, OCR/provider/API execution, retrieval runtime,
corpus ingestion, public-sync, or readiness/cost/quality claims.

## Claim Boundary

DICE-T0 is a doc-only control-envelope contract tranche. It does not authorize
runtime implementation, OCR/provider/API calls, external repo access, retrieval
behavior changes, corpus ingestion, public-sync, Document Translator readiness,
Policy_Local readiness, document correctness, extraction accuracy, provider
quality, production readiness, public readiness, release readiness, cost
claims, memory reinjection, high-risk promotion, or autonomous mutation.

rawMemoryReleased=false

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

This work order is private provenance dispatch authority only. No public-sync
artifact or public catalog claim is authorized.
