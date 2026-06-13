# CVF DIR-T1 Document Intelligence Router Source And Tests - Completion Review

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: review

Date: 2026-06-13

Reviewer: Claude (orchestrator/reviewer/closer)

Worker: Codex (under WORKER_MUST_NOT_COMMIT)

workOrder:
`docs/work_orders/CVF_AGENT_WORK_ORDER_DIR_T1_DOCUMENT_INTELLIGENCE_ROUTER_SOURCE_AND_TESTS_FOR_CODEX_2026-06-13.md`

GC-018:
`docs/baselines/CVF_GC018_DIR_T1_DOCUMENT_INTELLIGENCE_ROUTER_SOURCE_AND_TESTS_2026-06-13.md`

workerReturn:
`docs/reviews/CVF_DIR_T1_DOCUMENT_INTELLIGENCE_ROUTER_SOURCE_AND_TESTS_WORKER_RETURN_2026-06-13.md`

closureBaseHead: `e426d983`

rawMemoryReleased=false

## Purpose

Record Claude's reviewer-owned acceptance and closure conversion of the DIR-T1
Document Intelligence Router source and tests delivered by Codex under
`WORKER_MUST_NOT_COMMIT`. Codex did not commit; Claude reviews, closes, and
commits.

## Scope / Methodology

Claude independently read the four worker artifacts (router source, focused
tests, overlap checker, worker return) plus the two dispatch artifacts (GC-018,
work order). Claude re-ran the focused tests and the overlap checker rather than
relying only on Codex's reported results, and verified changed-file scope.

Out of scope: OCR/provider execution, retrieval/corpus mutation, external
Document Translator or Policy_Local tree operations, public-sync, and any
session-state change other than reviewer-owned closure/session-sync.

## Target / Source

| Item | Path | Disposition |
| --- | --- | --- |
| Router source | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | ACCEPT |
| Focused tests | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_router.py` | ACCEPT |
| Overlap checker | `governance/compat/check_dir_disposition_no_scan_overlap.py` | ACCEPT |
| Worker return | `docs/reviews/CVF_DIR_T1_DOCUMENT_INTELLIGENCE_ROUTER_SOURCE_AND_TESTS_WORKER_RETURN_2026-06-13.md` | ACCEPT |
| GC-018 baseline | `docs/baselines/CVF_GC018_DIR_T1_DOCUMENT_INTELLIGENCE_ROUTER_SOURCE_AND_TESTS_2026-06-13.md` | ACCEPT |
| Work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_DIR_T1_DOCUMENT_INTELLIGENCE_ROUTER_SOURCE_AND_TESTS_FOR_CODEX_2026-06-13.md` | ACCEPT |

## Review Verdict

Verdict: `CLOSED_PASS_BOUNDED`.

The worker implementation is accepted. The router composes EXA-T2 scan-route
contracts by import, keeps `AuthorizationGate` disjoint from
`ScanRouteDisposition`, implements the DIR-T0 derivation map as a total
function, stores no raw content, preserves operator-review and blocked-source
semantics, and passes all focused tests and the overlap gate. `WORKER_MUST_NOT_COMMIT`
was preserved: Codex did not commit.

## Findings / Position

F-1: Composition not duplication. The router imports `DocumentScanSignals`,
`ScanRouteDecision`, `ScanRouteDisposition`, and `decide_scan_route` from the
scan-route module (`document_intelligence_router.py:17-22`) and never retypes
scan disposition values. PASS.

F-2: Gate disjointness. `AuthorizationGate`
(`document_intelligence_router.py:35-41`) shares no value with
`ScanRouteDisposition`. Independently re-verified by running
`check_dir_disposition_no_scan_overlap.py`: overlap count 0, COMPLIANT. PASS.

F-3: Derivation correctness and totality. `SCAN_ROUTE_TO_AUTHORIZATION_GATE`
(`document_intelligence_router.py:51-56`) maps all four scan dispositions to
exactly the gates specified in the DIR-T0 contract matrix derivation table.
The test `test_derivation_map_is_total_for_current_scan_route_dispositions`
asserts the map domain equals the full `ScanRouteDisposition` set. PASS.

F-4: No raw content. None of the three dataclasses expose a raw-text, OCR,
provider-response, or extracted-text field; the test
`test_dir_dataclasses_do_not_expose_raw_content_fields` enforces this. PASS.

F-5: Operator-review and blocked-source semantics preserved. `ESCALATE_OR_ABSTAIN`
yields `OPERATOR_REVIEW_REQUIRED`; `BLOCKED_UNSUPPORTED` yields `BLOCKED`. PASS.

F-6 (non-blocking observation): `_derive_downstream_eligibility`
(`document_intelligence_router.py:126-129`) contains a redundant branch -- the
`if profile.requested_capability in {...}` arm and the fall-through both return
`(profile.requested_capability,)`. This is dead logic, not a correctness defect;
behavior is correct and test-covered. Disposition: ACCEPT_WITH_NOTE. Recommended
cleanup in a later DIR tranche or a fast-lane tidy; not a closure blocker.

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| DIR-T1 is deterministic-only and unvalidated against real documents | DIR-T2 pilot remains held behind fresh authorization and operator sample corpus |
| Redundant branch (F-6) could mask future intent if edited carelessly | Note recorded; optional cleanup in a later tranche; behavior is currently correct and tested |
| New checker not yet wired into the hook chain | DIR-T1 authorized creation only; hook-chain wiring is a separate governed decision (the overlap checker is runnable standalone and was run for this closure) |

## Independent Verification

| Check | Command | Result |
| --- | --- | --- |
| Focused tests | `python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_router.py -q` | 16 passed |
| Overlap checker | `python governance/compat/check_dir_disposition_no_scan_overlap.py` | COMPLIANT, overlap count 0 |
| Changed-file scope | `git status --short` | only 4 worker artifacts + 2 dispatch artifacts; no session/front-door/handoff/external file; `Thong_tin.md` excluded from commit |
| Pre-commit chain | `python governance/compat/run_local_governance_hook_chain.py --hook pre-commit` | recorded at closure commit |

## Rebuttal Incorporation Trace

DIR-T1 implements exactly the contracts that incorporated the Claude rebuttal
B1-B4 at DIR-T0:

| Rebuttal item | DIR-T1 implementation evidence |
| --- | --- |
| B1 (no flat enum re-encoding scan route) | `AuthorizationGate` disjoint; scan route passthrough field; overlap checker COMPLIANT |
| B2 (capability names, not use-case names) | `DownstreamCapability` carries capability shapes; `test_downstream_capabilities_do_not_contain_use_case_names` enforces it |
| B3 (collapse speculation; structure separate-but-collapsible) | `DocumentStructureSignals` kept separate with `KEEP_SEPARATE_BUT_COLLAPSIBLE_AT_T1` docstring |
| B4 (no external-tree read) | worker-return External Tree Boundary section; no external path in changed files |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| DIR-T1 work order authorized a new `governance/compat/*.py` checker but did not instruct the worker-return packet to carry a `Core Guard Self-Protection Authorization` block; reviewer-fast/core-guard required it; Codex repaired in-scope | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | TEMPLATE_UPDATED | Open a small governed batch after DIR-T1 closure to update the work-order template/addendum and dispatch-quality checker so any work order authorizing protected paths (`governance/compat/*.py`, `CVF_SESSION/**`, `AGENT_HANDOFF*.md`) must specify the required authorization carrier: `Core Guard Self-Protection Authorization`, exact `Protected paths`, `Authorized guard-maintenance scope`, `Operator authorization`, and `Rollback boundary` |
| Redundant branch in `_derive_downstream_eligibility` (F-6) | RULE_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | Behavior correct and test-covered; optional cleanup in a later tranche; no governance rule needed |

Runtime/provider/cost lane: `N/A_WITH_REASON` - no provider, OCR service,
retrieval runtime, or cost-bearing service was used.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | DIR-T1 work order | `Status: CLOSED_PASS_BOUNDED` after closure | PASS |
| Completion or reviewer artifact | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md` | DIR-T1 row updated to `CLOSED_PASS_BOUNDED` | PASS |
| GC-018 baseline state | DIR-T1 GC-018 | `Status: CLOSED_PASS_BOUNDED` after closure | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | GC-051 checker remains PASS; no new corpus source surface created | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | no new quick-lookup row required | PASS |
| External evidence digest | N/A | no external source tree was read | N/A with reason |
| System loop interlock | N/A | no runtime loop, route, retrieval, or interlock mutation | N/A with reason |
| Worker return artifact | DIR-T1 worker return | `Status: WORKER_RETURN_SUBMITTED_UNCOMMITTED` then accepted | PASS |
| Session continuity | active state/front door/handoff | pending dedicated session-sync commit | N/A with reason |

## Verification / Evidence

Required verification for this closure:

- focused tests re-run by reviewer: 16 passed;
- overlap checker re-run by reviewer: COMPLIANT;
- full pre-commit governance hook chain before commit;
- changed-file scope excludes `Thong_tin.md` and all session/front-door/handoff
  files;
- `WORKER_MUST_NOT_COMMIT` preserved: Codex did not commit.

## Claim Boundary

This review closes DIR-T1 deterministic local source and test work only. It
does not claim document intelligence behavior is validated against real
documents, scan/extraction accuracy is improved, OCR/provider behavior is
available, retrieval behavior changed, Policy_Local is ready, Document
Translator is ready, public catalog export exists, release proof exists, memory
reinjection is authorized, high-risk promotion is authorized, or autonomous
mutation is authorized.

rawMemoryReleased=false

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance completion review; no public-sync batch is
authorized.
