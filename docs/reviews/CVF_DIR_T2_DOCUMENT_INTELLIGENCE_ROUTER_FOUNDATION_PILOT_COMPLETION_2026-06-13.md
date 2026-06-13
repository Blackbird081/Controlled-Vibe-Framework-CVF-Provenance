# CVF DIR-T2 Document Intelligence Router Foundation Pilot - Completion Review

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: review

Date: 2026-06-13

Reviewer: Codex

Worker: Claude (under WORKER_MUST_NOT_COMMIT)

workOrder:
`docs/work_orders/CVF_AGENT_WORK_ORDER_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_FOR_CLAUDE_2026-06-13.md`

GC-018:
`docs/baselines/CVF_GC018_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_2026-06-13.md`

workerReturn:
`docs/reviews/CVF_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_WORKER_RETURN_2026-06-13.md`

closureBaseHead: `639405b1`

rawMemoryReleased=false

## Purpose

Record Codex's reviewer-owned acceptance and closure conversion of the DIR-T2
Document Intelligence Router foundation pilot delivered by Claude under
`WORKER_MUST_NOT_COMMIT`.

DIR-T2 is a CVF foundation pilot. It is not a Document Translator adaptation
tranche and does not authorize any external application repository work.

## Scope / Methodology

Codex reviewed the work order, GC-018 baseline, Claude worker return, and the
new focused pilot test file. Codex re-ran the required proof commands instead
of relying only on the worker-reported results, checked changed-file scope, and
treated the worker return as pending evidence until this review.

Out of scope: real document files, OCR/provider/API execution, retrieval
runtime, corpus ingestion, external Document Translator inspection or mutation,
Policy_Local mutation, public-sync, readiness/cost/quality claims, and
session-state mutation by the worker.

## Target / Source

| Item | Path | Disposition |
| --- | --- | --- |
| DIR-T2 pilot tests | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_router_foundation_pilot.py` | ACCEPT |
| Worker return | `docs/reviews/CVF_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_WORKER_RETURN_2026-06-13.md` | ACCEPT_WITH_NOTE |
| GC-018 baseline | `docs/baselines/CVF_GC018_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_2026-06-13.md` | ACCEPT |
| Work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_FOR_CLAUDE_2026-06-13.md` | ACCEPT |
| Parent roadmap | `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md` | ACCEPT |

## Review Verdict

Verdict: `CLOSED_PASS_BOUNDED`.

Claude's worker artifacts are accepted. The pilot harness uses synthetic
metadata-only fixtures, covers all four current EXA-T2 scan dispositions,
verifies DIR authorization gate derivation, preserves scan disposition
passthrough, checks operator action and downstream eligibility, and avoids raw
content and downstream use-case payloads.

`WORKER_MUST_NOT_COMMIT` was preserved: Claude did not commit. Codex owns this
review, closure conversion, session sync, and commit.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap / work-order requirement | Evidence reviewed | Closure disposition |
| --- | --- | --- |
| DIR-T2 is a bounded pilot | focused test file plus worker return | PASS |
| sample corpus is operator-approved and synthetic | four fixture IDs `DIR-T2-S1` through `DIR-T2-S4` | PASS |
| local deterministic runtime only | pytest proofs and no external service action | PASS |
| Document Translator remains downstream context only | no external tree access and no app path in changed files | PASS |
| no readiness/cost/quality claim | worker return and this claim boundary | PASS |

## Closure Diff Gate

| Work-order instruction | Final artifact evidence | Disposition |
| --- | --- | --- |
| Create focused DIR-T2 pilot test file | `test_document_intelligence_router_foundation_pilot.py` exists and passes | PASS |
| Create worker-return packet | worker return exists with proof summaries and negative evidence | PASS |
| Cover all scan dispositions | `test_pilot_corpus_covers_all_scan_dispositions` and parametrized samples | PASS |
| Assert gate/action/eligibility | focused tests assert all three dimensions | PASS |
| Keep DIR-T1 source unchanged unless blocked | no source modification in worker artifacts | PASS |
| Avoid forbidden paths and services | git status plus worker negative evidence; Codex did not observe forbidden path changes | PASS |

## Findings / Position

F-1: Pilot coverage is accepted. The focused harness reports 38 tests and
Codex re-ran them successfully. PASS.

F-2: DIR-T1 regression is preserved. Codex re-ran the existing DIR-T1 router
test suite and all 16 tests passed. PASS.

F-3: DIR authority gates remain disjoint from scan dispositions. Codex re-ran
`check_dir_disposition_no_scan_overlap.py`; overlap count remained 0 and the
checker returned COMPLIANT. PASS.

F-4: Worker-return `git status --short` snippet omits the worker-return packet
itself, even though the packet exists as an untracked artifact in the actual
reviewer worktree. This is a packet-evidence precision defect, not a scope
defect. Codex corrected the evidence in this completion review and final git
status. Disposition: ACCEPT_WITH_NOTE.

F-5: The test helper inserts the local source directory into `sys.path`, which
matches the existing focused test style in this extension and does not import
external repositories. PASS.

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Worker-return status snippet omitted the worker-return file itself | Recorded as F-4; Codex closure review corrects the changed-file evidence |
| Foundation pilot could be over-read as Document Translator readiness | Claim boundary and negative evidence explicitly reject readiness, quality, provider, OCR, and app-adaptation claims |
| Synthetic fixtures do not validate real document extraction quality | Keep any real-document, OCR, provider, or use-case validation behind a later fresh GC-018 and operator authorization |

## Independent Verification

| Check | Command | Result |
| --- | --- | --- |
| Focused DIR-T2 pilot tests | `python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_router_foundation_pilot.py -q` | 38 passed |
| Existing DIR-T1 router tests | `python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_router.py -q` | 16 passed |
| DIR overlap checker | `python governance/compat/check_dir_disposition_no_scan_overlap.py` | COMPLIANT, overlap count 0 |
| Changed-file scope | `git status --short` | only DIR-T2 closure artifacts plus pre-existing `Thong_tin.md` before reviewer-owned closure edits |

Pytest emitted the existing `pytest_asyncio` deprecation warning about
`asyncio_default_fixture_loop_scope`; this warning is unrelated to DIR-T2 and
did not fail the tests.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| Worker return omitted its own untracked packet from the reported `git status --short` snippet | OPERATOR_SCOPE_CLARITY_GAP | GOVERNANCE_CONTROL_PLANE | N/A_WITH_REASON | Reviewer caught and corrected the evidence; existing reviewer-owned closure conversion is sufficient for this one-off packet issue |
| Parametrized synthetic sample-corpus harness expanded coverage without adding runtime/source complexity | RULE_GAP | DOCUMENTATION_ONLY_LEARNING | N/A_WITH_REASON | Positive design validation only; no governance rule or machine check needed |

Runtime/provider/cost lane: `N/A_WITH_REASON` - no provider, OCR service,
retrieval runtime, or cost-bearing service was used.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | DIR-T2 work order | `Status: CLOSED_PASS_BOUNDED` after closure | PASS |
| Completion or reviewer artifact | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_ROADMAP_2026-06-13.md` | `Status: DIR_T2_CLOSED_PASS_BOUNDED` | PASS |
| GC-018 baseline state | DIR-T2 GC-018 | `Status: CLOSED_PASS_BOUNDED` after closure | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | GC-051 entry added for the DIR-T2 pilot test harness; checker PASS | PASS |
| Registry Markdown | BLOCKED with reason | no Markdown quick-lookup row is required for this generated registry-source update | BLOCKED with reason |
| External evidence digest | N/A with reason | no external source tree was read or hashed | N/A with reason |
| System loop interlock | N/A with reason | no runtime loop, route, retrieval, or interlock mutation | N/A with reason |
| Worker return artifact | DIR-T2 worker return | `Status: WORKER_RETURN_SUBMITTED_UNCOMMITTED` then accepted | PASS |
| Session continuity | active state/front door/handoff | pending dedicated session-sync commit | N/A with reason |

## Verification / Evidence

Required verification for this closure:

- focused DIR-T2 tests re-run by reviewer: 38 passed;
- existing DIR-T1 router tests re-run by reviewer: 16 passed;
- overlap checker re-run by reviewer: COMPLIANT with overlap count 0;
- pre-closure and pre-commit governance gates before closure commit;
- changed-file scope excludes `Thong_tin.md` from the commit;
- `WORKER_MUST_NOT_COMMIT` preserved: Claude did not commit.

## Claim Boundary

This review closes DIR-T2 local deterministic foundation pilot work only. It
does not claim document intelligence behavior validated against real
documents, extraction accuracy, OCR quality, provider behavior, retrieval
quality, Document Translator readiness, Policy_Local readiness, public
readiness, production readiness, hosted readiness, cost reduction, memory
reinjection, high-risk promotion, or autonomous mutation.

rawMemoryReleased=false

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance completion review; no public-sync batch is
authorized.
