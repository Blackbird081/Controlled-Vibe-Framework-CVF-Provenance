# CVF Agent Work Order - DIR-T1 Document Intelligence Router Source And Tests

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-13

Owner: Claude (orchestrator)

Assigned worker: Codex

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `e426d983`

executionBaseHead: `e426d983`

closureBaseHead: `WORKER_MUST_NOT_SET`

sourceAuthority:
`docs/baselines/CVF_GC018_DIR_T1_DOCUMENT_INTELLIGENCE_ROUTER_SOURCE_AND_TESTS_2026-06-13.md`

rawMemoryReleased=false

completionReviewPath:
`docs/reviews/CVF_DIR_T1_DOCUMENT_INTELLIGENCE_ROUTER_SOURCE_AND_TESTS_COMPLETION_2026-06-13.md`

reviewerOwnedClosurePaths:
`docs/reviews/CVF_DIR_T1_DOCUMENT_INTELLIGENCE_ROUTER_SOURCE_AND_TESTS_COMPLETION_2026-06-13.md`;
`CVF_SESSION/ACTIVE_SESSION_STATE.json`;
`CVF_SESSION/state/**`;
`CVF_SESSION_MEMORY.md`;
`AGENT_HANDOFF_V18_2026-06-12.md`

GC-018:
`docs/baselines/CVF_GC018_DIR_T1_DOCUMENT_INTELLIGENCE_ROUTER_SOURCE_AND_TESTS_2026-06-13.md`

Parent roadmap:
`docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md`

Predecessor tranche:
`docs/reference/CVF_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md`

## Purpose

Implement the DIR-T1 deterministic local Document Intelligence Router source
module plus focused tests and one governance overlap checker. Codex must
implement exactly the contracts the closed DIR-T0 contract matrix defined,
compose the existing EXA-T2 scan-route contracts rather than retype them, and
prove the router authorization gate is disjoint from scan dispositions.

The worker must not execute OCR or providers, change retrieval behavior, ingest
corpus, inspect external use-case trees, edit public-sync, or update session
state.

## Authority Chain

| Authority | Path / evidence | Disposition |
| --- | --- | --- |
| Operator request | operator asked Claude to invert roles and create the Codex DIR-T1 work order | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V18_2026-06-12.md` | ACCEPT |
| Parent roadmap | `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md` | ACCEPT |
| DIR-T0 contract matrix | `docs/reference/CVF_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md`; predecessor tranche closed (see Dependency Release Evidence) | ACCEPT |
| DIR-T0 worker return | `docs/reviews/CVF_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_WORKER_RETURN_2026-06-13.md`; status `WORKER_RETURN_ACCEPTED_BY_CODEX` | ACCEPT |
| GC-018 | `docs/baselines/CVF_GC018_DIR_T1_DOCUMENT_INTELLIGENCE_ROUTER_SOURCE_AND_TESTS_2026-06-13.md` | ACCEPT |

## Agent Roles

| Role | Agent | Boundary |
| --- | --- | --- |
| Orchestrator | Claude | dispatches GC-018 and work order only |
| Worker | Codex | authors allowed-scope source, tests, checker, and worker return |
| Reviewer / closer | Claude | reviews, fixes reviewer-owned issues, runs closure gates, commits |

Role inversion note: DIR-T0 had Codex orchestrating and Claude as worker. For
DIR-T1 the roles invert by operator instruction: Claude orchestrates and Codex
implements. This is intentional and authorized.

## Intake Role Routing Decision

Intake summary: operator approved opening DIR-T1 for Codex after DIR-T0 closed
`CLOSED_PASS_BOUNDED`.

Scope classification: bounded deterministic source plus focused tests plus one
governance overlap checker.

Risk sensitivity: medium governance risk because DIR-T1 produces the first
runtime DIR source. Risk remains bounded because no OCR, provider/API proof,
retrieval, external tree operation, public-sync, or session-state action is
authorized, and the router is deterministic and offline.

Selected route mode: MULTI_AGENT_MULTI_ROLE.

Role separation basis: Codex acts as implementation worker under
`WORKER_MUST_NOT_COMMIT`; Claude remains reviewer, closer, and committer.

Escalation condition: return to Claude if implementation requires OCR, provider
calls, retrieval changes, external workspace access, session state, public-sync,
generated JSON aggregate editing, operator sample documents, or a wider claim
boundary.

## Required First Reads

Codex must read:

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `AGENT_HANDOFF_V18_2026-06-12.md`
4. `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md`
5. `docs/reference/CVF_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md`
6. `docs/baselines/CVF_GC018_DIR_T1_DOCUMENT_INTELLIGENCE_ROUTER_SOURCE_AND_TESTS_2026-06-13.md`
7. `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py`
8. `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py`
9. `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_scan_route_decision.py`
10. this work order

## Startup Acknowledgment Required

Codex must begin with:

`Startup acknowledged: current mode=dir_t1_document_intelligence_router_source_and_tests_dispatched; active handoff=AGENT_HANDOFF_V18_2026-06-12.md; work order=DIR-T1; next allowed move=Codex implements allowed-scope DIR-T1 router source, focused tests, and overlap checker under WORKER_MUST_NOT_COMMIT and returns uncommitted; parked checkpoint=DIR-T2, DT-CVF-T0, Policy_Local PL-S1, EC/retrieval, T12, OCR/provider/runtime/public-sync remain parked.`

## Commit Mode And Base-Anchor Lifecycle

| Anchor | Value | Owner | Disposition |
| --- | --- | --- | --- |
| dispatchBaseHead | `e426d983` | Claude | ACCEPT |
| executionBaseHead | `e426d983` | Codex | ACCEPT |
| closureBaseHead | `WORKER_MUST_NOT_SET` | Claude reviewer | ACCEPT |
| Commit mode | `WORKER_MUST_NOT_COMMIT` | Claude | ACCEPT |

Codex must not commit. Codex must record worker-return base/head and
`git status --short` output in the worker-return packet.

## Dependency Release Evidence

| Dependency | Required evidence | Disposition |
| --- | --- | --- |
| DIR-T0 contract matrix closed | `docs/reference/CVF_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md`; status `CLOSED_PASS_BOUNDED` | ACCEPT |
| DIR-T0 worker return accepted | `docs/reviews/CVF_DIR_T0_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_WORKER_RETURN_2026-06-13.md`; status `WORKER_RETURN_ACCEPTED_BY_CODEX` | ACCEPT |
| Final roadmap holds DIR-T1 behind fresh GC-018 | roadmap DIR-T1 status `AWAITING_FRESH_AUTHORIZATION` | ACCEPT |
| Session state synchronized DIR-T0 closure | current HEAD before dispatch `e426d983` | ACCEPT |
| Fresh DIR-T1 baseline | `docs/baselines/CVF_GC018_DIR_T1_DOCUMENT_INTELLIGENCE_ROUTER_SOURCE_AND_TESTS_2026-06-13.md` | ACCEPT |

## Current Runtime Freshness Verification

Codex must refresh these anchors before editing:

```powershell
rg -n "ScanRouteDisposition|SCAN_ROUTE_DECISION_VERSION|class DocumentScanSignals|class ScanRouteDecision|def decide_scan_route" EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py
rg -n "ExtractionStatus|class ExtractionQualityReport" EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py
rg -n "AuthorizationGate|DownstreamCapability|DocumentProfile|DocumentStructureSignals|DocumentIntelligenceRouteDecision|Derivation Table" docs/reference/CVF_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md
rg -n "sys.path.insert|from scan_route_decision import" EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_scan_route_decision.py
```

## Pre-Flight Checks

Codex must run these before editing:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base e426d983 --head HEAD
```

If the pre-implementation gate fails only on allowed-scope artifacts, Codex
must repair and rerun under the Worker Autonomy rule. If the failure is outside
allowed scope, Codex must return to Claude.

## Worker Autonomy / No-Question Rule

Codex must repair allowed-scope gate failures without asking the operator or
Claude for permission. This includes lint, type, test, wording, status,
source-verification, dispatch-quality, closure-residue, artifact-quality,
encoding, and proof-manifest defects inside the four allowed DIR-T1 artifacts
or this work order's worker-return status evidence.

Codex must stop and return to Claude only when the required fix would exceed
Allowed Implementation Scope, change the claim boundary, require OCR/provider
execution, inspect an external tree, touch session state, touch public-sync,
consume secrets/quota, alter Policy_Local, release a parked checkpoint, or
perform a destructive/irreversible action.

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
| EXISTS: test import pattern | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_scan_route_decision.py` | lines 5-18 | `sys.path.insert` plus bare module import | EXA-T2 test convention | ACCEPT |
| EXISTS: DIR-T0 AuthorizationGate spec | `docs/reference/CVF_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md` | AuthorizationGate table and Derivation Table | `AuthorizationGate` | DIR-T0 contract matrix Contract 3 | ACCEPT |
| EXISTS: DIR-T0 DownstreamCapability spec | `docs/reference/CVF_DOCUMENT_INTELLIGENCE_ROUTER_CONTRACT_MATRIX_2026-06-13.md` | Contract 4 | `DownstreamCapability` | DIR-T0 contract matrix Contract 4 | ACCEPT |

## New Source And Test Symbols Authorized

These names are authorized as new DIR-T1 runtime symbols, sourced from the
closed DIR-T0 contract matrix.

| New symbol | DIR-T0 contract source | Target file | Boundary |
| --- | --- | --- | --- |
| `DOCUMENT_INTELLIGENCE_ROUTE_VERSION` | matrix Contract 3 | `document_intelligence_router.py` | version constant distinct from scan route version |
| `AuthorizationGate` | matrix Contract 3 | `document_intelligence_router.py` | router Literal disjoint from `ScanRouteDisposition` |
| `DownstreamCapability` | matrix Contract 4 | `document_intelligence_router.py` | capability Literal; no use-case names |
| `DocumentProfile` | matrix Contract 1 | `document_intelligence_router.py` | frozen dataclass; no raw text |
| `DocumentStructureSignals` | matrix Contract 2 | `document_intelligence_router.py` | frozen dataclass kept separate at T1 |
| `DocumentIntelligenceRouteDecision` | matrix Contract 3 | `document_intelligence_router.py` | frozen dataclass; scan passthrough plus gate |
| `decide_document_intelligence_route` | matrix Contract 3 derivation | `document_intelligence_router.py` | deterministic function |

## New Files To Create

| Path | Required content |
| --- | --- |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | deterministic router module per DIR-T0 contracts |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_router.py` | focused tests per Test Requirements |
| `governance/compat/check_dir_disposition_no_scan_overlap.py` | MC-1 overlap checker per DIR-T0 machine-check candidate |
| `docs/reviews/CVF_DIR_T1_DOCUMENT_INTELLIGENCE_ROUTER_SOURCE_AND_TESTS_WORKER_RETURN_2026-06-13.md` | worker return packet with proof manifest |

## Allowed Implementation Scope

Codex may modify:

- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py`
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_router.py`
- `governance/compat/check_dir_disposition_no_scan_overlap.py`
- `docs/reviews/CVF_DIR_T1_DOCUMENT_INTELLIGENCE_ROUTER_SOURCE_AND_TESTS_WORKER_RETURN_2026-06-13.md`
- this work order only for worker-return status evidence if needed
- parent roadmap DIR-T1 row only to mark worker-return status, not final closure

Codex must not modify:

- any existing `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/` file other than the
  new router module
- any existing test file other than the new router test
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/**`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V18_2026-06-12.md`
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Document_Translator`
- any external Policy_Local source tree
- retrieval, route/API, OCR, provider, corpus, or public-sync surfaces
- provider key files
- generated JSON aggregates

Codex must not read, list, hash, or modify the external Document Translator or
Policy_Local source trees for this work order.

## Write Ownership

| Artifact or surface | Owner | Write permission |
| --- | --- | --- |
| DIR router source module | Codex | create and edit |
| DIR router focused tests | Codex | create and edit |
| DIR overlap checker | Codex | create and edit |
| DIR-T1 worker-return packet | Codex | create and edit |
| this work order | Codex | edit only for worker-return status evidence if needed |
| parent roadmap DIR-T1 row | Codex | edit only to mark worker-return status, not final closure |
| completion review | Claude | reviewer-owned |
| session state, front door, and active handoff | Claude | reviewer-owned session-sync only |
| existing EXTENSIONS source/tests, external repos, public-sync | no worker | forbidden in this tranche |

## Execution Plan

1. Read all Required First Reads and record the startup acknowledgment.
2. Refresh the source anchors listed in Current Runtime Freshness Verification.
3. Run Pre-Flight Checks from `dispatchBaseHead` `e426d983`.
4. Create the router module under `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/`.
5. Create the focused test file under
   `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/`.
6. Create the overlap checker under `governance/compat/`.
7. Run the Required Proof Manifest commands.
8. Create the worker-return packet under `docs/reviews/`.
9. Return all changed artifacts uncommitted to Claude.

## Implementation Requirements

The router module must:

1. import EXA-T2 scan route values rather than retype them, using the same
   `sys.path` or package convention the existing tests use, so that
   `ScanRouteDisposition` is composed, never copied;
2. define `AuthorizationGate` as a Literal whose values are fully disjoint from
   `ScanRouteDisposition` values;
3. define `DocumentProfile`, `DocumentStructureSignals`, and
   `DocumentIntelligenceRouteDecision` as frozen dataclasses with no raw text,
   OCR output, or provider response fields;
4. implement `decide_document_intelligence_route` as a deterministic function
   that consumes a `ScanRouteDecision` (or calls `decide_scan_route` on supplied
   signals), sets `scan_route` as passthrough, and derives `authorization_gate`
   via the DIR-T0 total derivation map;
5. preserve `BLOCKED_UNSUPPORTED` and `ESCALATE_OR_ABSTAIN` semantics and never
   downgrade an operator-review requirement;
6. keep all provider/OCR routes as `*_REQUIRES_SEPARATE_AUTH` gate values, never
   as executed actions;
7. include a module-level claim boundary docstring like the EXA-T2 modules;
8. keep `DocumentStructureSignals` as a separate dataclass and record the
   `KEEP_SEPARATE_BUT_COLLAPSIBLE_AT_T1` decision in a comment or docstring.

## Test Requirements

The focused test file must cover at least:

- gate disjointness: no `AuthorizationGate` value equals any
  `ScanRouteDisposition` value;
- derivation correctness: each of the 4 scan dispositions maps to its specified
  gate;
- passthrough: `scan_route` in the decision equals the source scan route;
- no-raw-content: dataclass fields contain no raw text or OCR/provider output;
- operator-review preservation: an `ESCALATE_OR_ABSTAIN` scan route yields
  `OPERATOR_REVIEW_REQUIRED`;
- blocked source: a `BLOCKED_UNSUPPORTED` scan route yields `BLOCKED`;
- digest presence: `scan_decision_digest` is populated and is not raw content.

## Checker Requirements

`check_dir_disposition_no_scan_overlap.py` must:

- import `ScanRouteDisposition` from the scan route module and `AuthorizationGate`
  from the new router module using the repo's existing checker import
  conventions;
- compute the set intersection of their Literal values;
- exit non-zero with a clear message if the intersection is non-empty;
- exit zero with a COMPLIANT message if the sets are disjoint;
- follow the output style of existing `governance/compat/check_*.py` files.

## Evidence Requirements

Codex must provide evidence for:

- source anchor refresh from the scan route, extraction pipeline, and DIR-T0
  contract matrix;
- router module composition (import, not retype) of EXA-T2 values;
- full focused test pass output;
- overlap checker COMPLIANT output;
- changed-file scope from `git diff --name-status` and `git status --short`;
- no external Document Translator or Policy_Local tree read, list, hash,
  modification, or import.

## Acceptance Criteria

| Requirement | Acceptance condition |
| --- | --- |
| Composition not duplication | router imports `ScanRouteDisposition`, does not retype its values |
| Gate disjointness | overlap checker COMPLIANT; disjointness test passes |
| Derivation correctness | all 4 scan dispositions map to the DIR-T0-specified gates |
| No raw content | no dataclass field stores raw text, OCR output, or provider response |
| Operator-review preserved | review/abstain semantics are not downgraded |
| Tests pass | focused test file passes fully |
| Runtime boundary | no OCR/provider execution, retrieval change, external repo, public-sync, or session-state file changed |
| Worker return | worker-return packet states `WORKER_MUST_NOT_COMMIT observed` and `rawMemoryReleased=false` |

## Required Proof Manifest Atomic Literal Discipline

Each Required Proof Manifest row must contain one atomic command or one atomic
file path. Do not combine multiple commands in one row. Do not use compound
literal syntax in the command cells.

## Required Proof Manifest

Codex must include command output summaries in the worker-return packet.

| Proof item | Required literal | Expected result |
| --- | --- | --- |
| Base anchor | `git rev-parse --short HEAD` | records worker starting head |
| Worktree start | `git status --short` | records pre-edit worktree state |
| Pre-implementation gate | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base e426d983 --head HEAD` | PASS or allowed-scope repair then PASS |
| Router test run | `python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_router.py -q` | all tests pass |
| Overlap checker run | `python governance/compat/check_dir_disposition_no_scan_overlap.py` | COMPLIANT exit zero |
| Reviewer fast gate | `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` | PASS or allowed-scope repair then PASS |
| Pre-commit gate | `python governance/compat/run_local_governance_hook_chain.py --hook pre-commit` | PASS or allowed-scope repair then PASS |
| Changed file list | `git diff --name-status` | only allowed files changed |
| Worker return state | `git status --short` | uncommitted artifacts ready for Claude |

## Required Artifact Manifest

| Artifact | Required status in worker return |
| --- | --- |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | created |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_router.py` | created |
| `governance/compat/check_dir_disposition_no_scan_overlap.py` | created |
| `docs/reviews/CVF_DIR_T1_DOCUMENT_INTELLIGENCE_ROUTER_SOURCE_AND_TESTS_WORKER_RETURN_2026-06-13.md` | created |
| this work order | unchanged unless worker-return evidence requires a status note |
| parent roadmap | unchanged unless worker-return evidence requires row-status note |

## Work-Order Fulfillment Manifest

The worker-return packet must include a Work-Order Fulfillment Manifest with
one row per requirement in this work order and dispositions of `PASS`,
`N/A_WITH_REASON`, or `BLOCKED`. Any `BLOCKED` row returns the packet to Claude.

## Closure Checklist

All checklist items resolved by the worker return and reviewer acceptance
(see DIR-T1 worker return and completion review):

- [x] Startup acknowledgment recorded.
- [x] Required First Reads completed.
- [x] Current Runtime Freshness Verification commands summarized.
- [x] Pre-Flight Checks run.
- [x] Router module created.
- [x] Focused test file created and passing.
- [x] Overlap checker created and COMPLIANT.
- [x] Worker-return packet created.
- [x] Required Proof Manifest completed.
- [x] Changed files remain inside Allowed Implementation Scope.
- [x] Claim Boundary and Public Export Disposition included.
- [x] `WORKER_MUST_NOT_COMMIT observed` recorded.

## Return-To-Orchestrator Conditions

Return to Claude immediately if:

- any required repair exceeds Allowed Implementation Scope;
- a gate failure requires OCR/provider execution, retrieval change, external
  tree access, session state, generated JSON aggregate edits, public-sync,
  secret use, or operator sample documents;
- the router cannot compose EXA-T2 values without retyping them;
- a required artifact is `BLOCKED`;
- the worker cannot preserve `WORKER_MUST_NOT_COMMIT`.

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Roadmap source | Work-order instruction | Required evidence |
| --- | --- | --- | --- |
| Implement deterministic local router after DIR-T0 closes | roadmap lines 334-336 | Implementation Requirements | router module created |
| Import/source-verify EXA-T2 values instead of retyping | roadmap lines 348-349 | Implementation Requirement 1 | import evidence in worker return |
| Preserve BLOCKED_UNSUPPORTED and ESCALATE_OR_ABSTAIN | roadmap line 350 | Implementation Requirement 5 | semantics tests pass |
| Never downgrade operator review | roadmap line 351 | Implementation Requirement 5 | operator-review test passes |
| Keep provider/OCR blocked | roadmap lines 352-353 | Implementation Requirement 6 | gate values remain `*_REQUIRES_SEPARATE_AUTH` |
| Keep DocumentStructureSignals separate, collapsible at T1 | roadmap lines 354-356 | Implementation Requirement 8 | separate dataclass plus decision comment |
| Governance checker or test proving gate/scan disjointness | roadmap lines 343-344 | Checker Requirements plus Test Requirements | overlap checker COMPLIANT plus disjointness test |
| No raw text, OCR, provider, readiness claim | roadmap lines 358-363 | Acceptance Criteria and Claim Boundary | no-raw-content test plus claim boundary |

## Worker Return Packet Requirements

The worker-return packet must include:

- Startup acknowledgment;
- base/head and `git status --short`;
- list of changed files;
- Required Proof Manifest with command output summaries;
- Work-Order Fulfillment Manifest;
- test result summary;
- overlap checker result summary;
- explicit `WORKER_MUST_NOT_COMMIT observed`;
- explicit `rawMemoryReleased=false`;
- Finding-To-Governance Learning Disposition with `N/A_WITH_REASON` if no
  finding is recorded;
- Claim Boundary;
- Public Export Disposition.

## Review Gate

Claude must not commit the worker return until:

- the changed file list stays inside Allowed Implementation Scope;
- the focused tests pass;
- the overlap checker is COMPLIANT;
- reviewer-fast passes;
- pre-commit passes;
- the worker return states `WORKER_MUST_NOT_COMMIT observed`;
- no OCR/provider execution, retrieval change, external repo, public-sync,
  session state, or generated aggregate file was changed by Codex.

## Reviewer Closure Conversion

Claude reviewer may later create a completion review and session-sync commit if
the worker return passes. Codex must not create the completion review unless
Claude issues a separate reviewer-owned instruction.

## Operator Checkpoint

No operator checkpoint is required for this dispatch. Operator input is
required only if the worker needs to exceed Allowed Implementation Scope or
asks to execute OCR/providers or inspect external use-case source trees.

## Export Surface Decision

Private provenance only. No public-sync path is authorized.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this work order | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_DIR_T1_DOCUMENT_INTELLIGENCE_ROUTER_SOURCE_AND_TESTS_COMPLETION_2026-06-13.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker return artifact | `docs/reviews/CVF_DIR_T1_DOCUMENT_INTELLIGENCE_ROUTER_SOURCE_AND_TESTS_WORKER_RETURN_2026-06-13.md` | `Status: WORKER_RETURN_ACCEPTED_BY_CLAUDE` | PASS |
| GC-018 baseline state | DIR-T1 GC-018 | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md` | DIR-T1 row `CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | two DIR-T1 entries added and aggregate regenerated; GC-051 checker COMPLIANT | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | no new quick-lookup row required for DIR-T1 source/test entries | PASS |
| External evidence digest | N/A | no external source tree was read | N/A with reason |
| System loop interlock | N/A | no runtime loop, route, retrieval, or interlock mutation | N/A with reason |
| Session continuity | active state/front door/handoff | pending dedicated session-sync commit | N/A with reason |

## Claim Boundary

This work order authorizes bounded DIR-T1 deterministic source and test work.
It does not claim document intelligence behavior is validated against real
documents, scan/extraction accuracy is improved, OCR/provider behavior is
available, retrieval behavior changed, Policy_Local is ready, Document
Translator is ready, public catalog export exists, release proof exists, memory
reinjection is authorized, high-risk promotion is authorized, or autonomous
mutation is authorized.

rawMemoryReleased=false

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

This is a private provenance dispatch work order. No public-sync artifact or
public catalog claim is authorized by this tranche.

## Dispatch Packet Authoring Learning Promotion

Learning lane: governance/control-plane learning.

Disposition: `N/A_WITH_REASON`.

Reason: this work order applies existing dispatch-quality, source-verification,
dependency-release, proof-manifest, and external-tree boundary rules. The role
inversion is operator-authorized and recorded; no new repeated defect pattern
is introduced by dispatch authoring.
