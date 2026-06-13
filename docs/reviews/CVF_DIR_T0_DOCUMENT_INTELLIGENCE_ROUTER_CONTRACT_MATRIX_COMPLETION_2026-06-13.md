# CVF DIR-T0 Document Intelligence Router Contract Matrix Completion

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: completion_review

Date: 2026-06-13

Owner: Codex

Worker: Claude

Execution base head: `57799f67`

Closure base head: `57799f67`

sourceAuthority:
`docs/work_orders/CVF_AGENT_WORK_ORDER_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_FOR_CLAUDE_2026-06-13.md`

rawMemoryReleased=false

GC-018:
`docs/baselines/CVF_GC018_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md`

Work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_FOR_CLAUDE_2026-06-13.md`

Worker return:
`docs/reviews/CVF_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_WORKER_RETURN_2026-06-13.md`

Contract matrix:
`docs/reference/CVF_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md`

Parent roadmap:
`docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md`

## Executive Result

DIR-T0 is closed bounded.

Result:

- accepted the Claude worker return under `WORKER_MUST_NOT_COMMIT`;
- added the Document Intelligence Router contract matrix;
- preserved EXA-T2 scan-route ownership and EX-T9 scan outcome ownership;
- defined doc-only tables for `DocumentProfile`,
  `DocumentStructureSignals`, `DocumentIntelligenceRouteDecision`,
  `AuthorizationGate`, and `DownstreamCapability`;
- added adapter eligibility rows while keeping use-case names out of
  foundation capability values;
- carried forward machine-check candidates for DIR-T1;
- kept extension source files, tests, OCR/provider, retrieval, corpus, external
  Document Translator, external Policy_Local, public-sync, session-state, and
  generated aggregate surfaces untouched in the material closure batch.

## Purpose

This review closes DIR-T0 and records whether the returned documentation
artifacts satisfy the source-verified work order without claiming a runtime
Document Intelligence Router exists.

## Scope / Target / Owner Boundary

Target: bounded DIR contract matrix and worker-return packet.

Owner boundary: Claude authored the worker artifacts without committing. Codex
reviewed the files, corrected a worker-return proof wording defect within
allowed documentation scope, authored this completion review, converted the
work order, GC-018, roadmap, contract matrix, and worker return to bounded
closure, and owns the final material commit plus session sync.

## Target / Source

Target artifacts:

- `docs/reference/CVF_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md`;
- `docs/reviews/CVF_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_WORKER_RETURN_2026-06-13.md`;
- `docs/work_orders/CVF_AGENT_WORK_ORDER_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_FOR_CLAUDE_2026-06-13.md`;
- `docs/baselines/CVF_GC018_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md`;
- `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md`;
- this completion review.

Source artifacts:

- DIR final roadmap;
- DIR Claude rebuttal;
- DIR Codex finalization review;
- DIR-T0 GC-018;
- DIR-T0 work order;
- current extraction foundation source anchors named in the work order;
- worker return packet.

## Scope / Methodology

Method:

- read active session front door, active state, active handoff, GC-018, and
  work order;
- inspected the worker files and allowed path set;
- confirmed the worker did not commit;
- ran reviewer-fast on the uncommitted worker artifacts;
- corrected worker-return proof wording so `git diff --name-status` is not
  misrepresented as listing untracked files;
- converted the work order, GC-018, roadmap, contract matrix, worker return,
  and completion packet to bounded closure.

## Findings / Position

Position: PASS bounded.

Findings:

- The worker did not commit and left two required artifacts uncommitted for
  Codex.
- The changed worker files stayed within allowed implementation scope.
- The contract matrix maps the current owner surfaces for
  `DocumentScanSignals`, `ScanRouteDecision`, `decide_scan_route`,
  `ExtractionQualityReport`, `ExtractionStorageBoundary`,
  `ScanOutcomeReport`, and related source anchors.
- The matrix rejects duplicate scan-route dispositions, raw document text,
  OCR output, provider response, downstream app state, and use-case-named
  foundation capability values.
- `DownstreamCapability` values remain capability-shaped; use-case names appear
  only in adapter matrix rows.
- Missing downstream adapter contracts are labeled
  `ADAPTER_CONTRACT_NOT_YET_PUBLISHED`.
- No runtime, route/API, OCR/provider, retrieval, corpus, external workspace,
  public-sync, generated aggregate, or session-state surface was modified in
  the material closure batch.

## Risk / Corrective Action

| Risk | Disposition | Corrective action |
| --- | --- | --- |
| DIR contract could be mistaken for runtime implementation | Blocked | Completion and matrix repeat doc-only boundary |
| Router authority axis could duplicate scan disposition values | Reduced | Contract matrix records MC-1 candidate for DIR-T1 |
| Use-case names could leak into foundation capability enum | Blocked | Matrix keeps use-case names in adapter rows and records MC-2 candidate |
| Worker proof wording overstated `git diff --name-status` output for untracked files | Corrected | Codex changed the row to state that untracked artifacts are shown by `git status --short`, not tracked diff |
| Runtime/provider/cost claim overreach | Blocked | No provider/API, live proof, route, storage, token, latency, or cost claim is made |

## Evidence Trace Block

| Evidence item | Path / command | Result |
| --- | --- | --- |
| Worker return | `docs/reviews/CVF_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_WORKER_RETURN_2026-06-13.md` | `WORKER_MUST_NOT_COMMIT` observed |
| Worker artifact state | `git status --short` before closure conversion | two untracked DIR-T0 worker artifacts plus pre-existing `Thong_tin.md` |
| Reviewer-fast | `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` | PASS, 13/13 before closure conversion |
| Contract matrix terms | `docs/reference/CVF_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md` | required contract tables, adapter matrix, and claim boundary present |
| Changed file scope | `git status --short` | no runtime/source/session/public-sync files touched by worker |
| Closure conversion | this file plus status updates | Codex-owned reviewer closure only |

## Closure Diff Gate

| Requirement | Final artifact | Disposition |
| --- | --- | --- |
| Contract matrix created | `docs/reference/CVF_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md` | PASS |
| Worker return created | `docs/reviews/CVF_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_WORKER_RETURN_2026-06-13.md` | PASS |
| Three contract tables covered | contract matrix sections for `DocumentProfile`, `DocumentStructureSignals`, and `DocumentIntelligenceRouteDecision` | PASS |
| Owner reconciliation covered | contract matrix Owner Reconciliation table | PASS |
| Collision and rejection covered | contract matrix Collision And Rejection table | PASS |
| Adapter matrix covered | contract matrix Adapter Eligibility Matrix | PASS |
| Machine-check candidates carried forward | MC-1, MC-2, MC-3 sections | PASS |
| External-tree boundary preserved | worker return and matrix state no Document Translator or Policy_Local tree operation | PASS |
| Raw release boundary | all artifacts carry `rawMemoryReleased=false` | PASS |
| Worker did not commit | worker return and pre-review status | PASS |

## Runtime And Workspace Boundary Evidence

Changed files reviewed before Codex closure were limited to the two new worker
documentation artifacts plus pre-existing untracked `Thong_tin.md`, which was
not part of DIR-T0 and is not included in this closure. Codex closure
conversion additionally touched only the DIR-T0 work order, GC-018 baseline,
parent roadmap, contract matrix status, worker-return proof wording/status, and
this completion review. No extension source files, route/API, OCR/provider, retrieval,
corpus registry, external Document Translator, external Policy_Local,
public-sync, generated aggregate, or session-state file is part of this
material closure.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_FOR_CLAUDE_2026-06-13.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| GC-018 | `docs/baselines/CVF_GC018_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker return | `docs/reviews/CVF_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_WORKER_RETURN_2026-06-13.md` | `WORKER_MUST_NOT_COMMIT` observed | PASS |
| Roadmap state | `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md` | `Status: DIR_T0_CLOSED_PASS_BOUNDED` | PASS |
| Contract artifact | `docs/reference/CVF_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md` | file exists and `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | BLOCKED with reason | no GC-051 registry update authorized for DIR-T0 closure | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason | no GC-051 registry update authorized for DIR-T0 closure | BLOCKED with reason |
| External evidence digest | N/A with reason | no external corpus/provider evidence used | N/A with reason |
| System loop interlock | N/A with reason | no runtime loop mutation authorized | N/A with reason |
| Runtime evidence | N/A with reason | contract is doc-only and no runtime behavior changed | N/A with reason |
| Live proof | N/A with reason | no provider/API call authorized or needed | N/A with reason |
| Public-sync | N/A with reason | private provenance work; public-sync not authorized | N/A with reason |
| Session continuity | active state/front door/handoff | separate session-sync commit follows material closure when required | N/A with reason |

## Finding-To-Governance Learning Disposition

| Finding / risk | Defect class | Learning lane | Escalation state | Disposition | Next control action |
| --- | --- | --- | --- | --- | --- |
| Worker proof wording overstated `git diff --name-status` output for untracked files | EVIDENCE_WORDING_GAP | GOVERNANCE_CONTROL_PLANE | REVIEWER_CORRECTED | N/A_WITH_REASON | Existing reviewer-fast plus Codex review caught and corrected before commit; no new machine check needed |
| Non-ASCII em dash repaired by worker before return | WORKER_EXECUTION_ERROR | GOVERNANCE_CONTROL_PLANE | WORKER_CORRECTED | RULE_EXISTS | Existing text encoding standard and gate already caught the defect |
| Runtime/provider/cost lane | RUNTIME_SIGNAL_GAP | DOCUMENTATION_ONLY_LEARNING | N/A_WITH_REASON | N/A_WITH_REASON | No runtime, provider, cost, token, latency, live proof, or route-behavior claim is made |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private Document Intelligence Router foundation contract matrix
closure; public-sync is not authorized.

## Claim Boundary

DIR-T0 proves only that CVF has a doc-only Document Intelligence Router
contract matrix with owner reconciliation, proposed contract tables, adapter
eligibility rows, and machine-check candidates for a later source tranche. It
does not claim document intelligence behavior exists, router source code is
implemented, scan/extraction accuracy is improved, OCR/provider behavior is
available, retrieval behavior changed, Policy_Local is ready, Document
Translator is ready, public catalog export exists, release proof exists, memory
reinjection is authorized, high-risk promotion is authorized, or autonomous
mutation is authorized.

## Next Allowed Move

DIR-T1 may be opened only through fresh GC-018 and a source-verified work order
for deterministic local source implementation and focused tests. DIR-T2,
DT-CVF-T0, Policy_Local PL-S1, EC/retrieval, T12, OCR/provider/runtime,
public-sync, readiness, cost, and quality claims remain held until later
explicit authorization.
