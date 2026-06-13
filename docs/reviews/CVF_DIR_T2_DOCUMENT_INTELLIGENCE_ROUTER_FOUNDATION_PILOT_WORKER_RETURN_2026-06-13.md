# CVF DIR-T2 Document Intelligence Router Foundation Pilot - Worker Return

Memory class: FULL_RECORD

Status: WORKER_RETURN_SUBMITTED_UNCOMMITTED

docType: review

Date: 2026-06-13

Worker: Claude

Commit mode: WORKER_MUST_NOT_COMMIT

executionBaseHead: `30e6d174`

workerReturnBaseHead: `30e6d174`

rawMemoryReleased=false

workOrder:
`docs/work_orders/CVF_AGENT_WORK_ORDER_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_FOR_CLAUDE_2026-06-13.md`

GC-018:
`docs/baselines/CVF_GC018_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_2026-06-13.md`

## Purpose

Record Claude's worker-return evidence for the DIR-T2 foundation pilot harness
under `WORKER_MUST_NOT_COMMIT`. Codex owns review, reviewer-owned closure
conversion, and commit.

## Scope / Target / Owner Boundary

Target: DIR-T2 local deterministic foundation pilot evidence for the existing
Document Intelligence Router.

Owner boundary: Claude owns only the worker test harness and this worker-return
packet. Codex owns independent review, closure conversion, session continuity,
and commits.

## Scope / Methodology

Claude created a synthetic metadata-only fixture corpus, exercised the existing
DIR-T1 router through local Python tests, ran the required proof commands, and
reported negative evidence for forbidden scope. The worker did not run OCR,
call providers, inspect external repositories, mutate session state, or commit.

## Target / Source

| Item | Path | Disposition |
| --- | --- | --- |
| Pilot test harness | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_router_foundation_pilot.py` | CREATED |
| Worker-return packet | this file | CREATED |
| DIR-T1 router source | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | READ/EXERCISED |
| EXA-T2 scan-route source | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | READ/EXERCISED |
| External Document Translator tree | forbidden external path | NOT_ACCESSED |

## WORKER_MUST_NOT_COMMIT Observed

`WORKER_MUST_NOT_COMMIT observed` -- Claude did not commit. Both new files are
untracked. Codex reviews and commits.

## Changed-File List

`git status --short` at worker return:

```
?? EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_router_foundation_pilot.py
?? Thong_tin.md
```

`Thong_tin.md` is the pre-existing operator-owned untracked file. It was not
modified by Claude and is outside this work order.

## Worktree Pre-Flight Confirmation

- Pre-existing dirty paths at dispatch: `?? Thong_tin.md` only.
- External Document Translator tree: NOT read, NOT listed, NOT hashed, NOT
  imported.
- External Document Translator tree (`D:/UNG DUNG AI/TOOL AI 2026/CVF-Workspace/Document_Translator/**`): untouched.
- Session-state files (`CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF*.md`): NOT mutated by Claude.
- Public-sync (`Controlled-Vibe-Framework-CVF-public-sync/**`): NOT used.
- `Policy_Local/**`: NOT mutated.
- `.env*`: NOT read.

## Artifacts Created

| Artifact | Path | Status |
| --- | --- | --- |
| DIR-T2 pilot test harness | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_router_foundation_pilot.py` | CREATED (uncommitted) |
| This worker-return packet | `docs/reviews/CVF_DIR_T2_DOCUMENT_INTELLIGENCE_ROUTER_FOUNDATION_PILOT_WORKER_RETURN_2026-06-13.md` | CREATED (uncommitted) |

## Forbidden Path Manifest Verification

| Path / Pattern | Worker action | Status |
| --- | --- | --- |
| `D:/UNG DUNG AI/TOOL AI 2026/CVF-Workspace/Document_Translator/**` | not read, listed, hashed, modified, or imported | UNTOUCHED |
| `D:/UNG DUNG AI/TOOL AI 2026/Controlled-Vibe-Framework-CVF-public-sync/**` | not accessed | UNTOUCHED |
| `Policy_Local/**` | not mutated | UNTOUCHED |
| `CVF_SESSION/**` | not mutated | UNTOUCHED |
| `CVF_SESSION_MEMORY.md` | not mutated | UNTOUCHED |
| `AGENT_HANDOFF*.md` | not mutated | UNTOUCHED |
| `.env*` | not read | UNTOUCHED |

## Proof Command Summaries

| Proof item | Command | Result |
| --- | --- | --- |
| DIR-T2 focused pilot tests | `python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_router_foundation_pilot.py -q` | 38 passed |
| DIR-T1 router tests (regression) | `python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_router.py -q` | 16 passed |
| DIR overlap checker | `python governance/compat/check_dir_disposition_no_scan_overlap.py` | COMPLIANT -- overlap count 0 |
| Worker worktree state | `git status --short` | `?? EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_router_foundation_pilot.py` + `?? Thong_tin.md` only |

## Sample Corpus Ledger

| sampleId | Intent | Scan disposition supplied | Expected gate | Test result |
| --- | --- | --- | --- | --- |
| DIR-T2-S1 | digital-native structured text handoff | `LOCAL_TEXT_EXTRACTION_RECOMMENDED` | `LOCAL_DETERMINISTIC_ALLOWED` | PASS |
| DIR-T2-S2 | scanned/image-heavy requiring OCR auth | `OCR_ELIGIBLE_OPERATOR_REVIEW_REQUIRED` | `OCR_REQUIRES_SEPARATE_AUTH` | PASS |
| DIR-T2-S3 | ambiguous/low-confidence requiring operator review | `ESCALATE_OR_ABSTAIN` | `OPERATOR_REVIEW_REQUIRED` | PASS |
| DIR-T2-S4 | unsupported source blocked by scan layer | `BLOCKED_UNSUPPORTED` | `BLOCKED` | PASS |

All four GC-018 required sample IDs are present. All four EXA-T2
`ScanRouteDisposition` values are covered (verified by
`test_pilot_corpus_covers_all_scan_dispositions`).

## Test Coverage Summary

The pilot harness contains 38 tests (parametrized expansions included) across
12 named test functions:

1. `test_pilot_corpus_covers_all_scan_dispositions` -- all 4 EXA-T2 dispositions covered.
2. `test_authorization_gate_per_sample` (x4) -- gate correct per sample.
3. `test_operator_action_per_sample` (x4) -- operator action correct per sample.
4. `test_s1_local_deterministic_preserves_requested_capability` -- S1 eligibility = requested capability.
5. `test_s2_ocr_yields_operator_review_only` -- S2 eligibility = OPERATOR_REVIEW_ONLY.
6. `test_s3_escalate_yields_operator_review_only` -- S3 eligibility = OPERATOR_REVIEW_ONLY.
7. `test_s4_blocked_yields_abstain_or_block` -- S4 eligibility = ABSTAIN_OR_BLOCK.
8. `test_scan_route_passthrough_per_sample` (x4) -- DIR does not alter scan disposition.
9. `test_no_raw_content_tokens_in_decision_fields` (x4) -- no raw-content tokens in decision fields.
10. `test_no_external_usecase_tokens_in_decision_fields` (x4) -- no use-case tokens in non-boundary fields.
11. `test_version_and_claim_boundary_per_sample` (x4) -- version and boundary invariants.
12. `test_scan_decision_digest_present_per_sample` (x4) -- digest present and not verbatim route.
13. `test_scan_route_to_authorization_gate_total_for_pilot_corpus` -- derivation map covers all corpus samples.
14. `test_downstream_capabilities_remain_foundation_level` -- capability names contain no use-case tokens.
15. `test_pilot_corpus_fixtures_are_metadata_only` -- no raw/use-case tokens in intent strings.
16. `test_all_pilot_samples_use_supplied_scan_decision_path` (x4) -- supplied scan-decision path routes correctly.
17. `test_s1_via_scan_signals_composition_path` -- scan_signals composition path also routes correctly for S1.

All 38 tests pass. DIR-T1 regression suite (16 tests) also passes. DIR-T1
source was not modified.

## Negative Evidence -- Forbidden Scope

- No real document files were used. All fixtures are synthetic metadata-only.
- No external Document Translator source files were read, listed, hashed, modified, or imported.
- No public-sync action was performed.
- No OCR/provider/API execution occurred.
- No retrieval runtime or corpus ingestion was triggered.
- No session-state or handoff mutation was performed by Claude.
- No readiness, cost, quality, hosted, production, or public claim is made.

## Findings / Position

F-1: Synthetic fixture corpus covers all four current EXA-T2 scan dispositions.
PASS.

F-2: DIR-T2 proof remains local deterministic and test-only. PASS.

F-3: Worker-return `git status --short` was captured before or without listing
this worker-return packet itself. Codex must correct final changed-file
evidence during reviewer-owned closure. ACCEPT_WITH_NOTE.

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Worker-return status snippet may understate changed files | Codex reviewer must use live `git status --short` before commit |
| Pilot evidence could be misread as downstream app readiness | Claim boundary states no Document Translator, Policy_Local, OCR/provider, retrieval, production, or public readiness claim |

## DIR-T1 Source Change

DIR-T1 source `document_intelligence_router.py` was NOT modified. The pilot
tests are test-only and exercise the existing source through the authorized
test interfaces.

Note carried from DIR-T1 completion (F-6): the redundant branch in
`_derive_downstream_eligibility` (lines 126-129) remains non-blocking. The
pilot tests exercise that code path and confirm behavior is correct; no
cleanup was required for the pilot.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| Pilot harness has 38 tests vs DIR-T1's 16 -- the parametrized sample-corpus pattern expands coverage without proportional file-line growth | RULE_GAP | DOCUMENTATION_ONLY_LEARNING | N/A_WITH_REASON | Parametrized sample-corpus pattern is functioning as intended; no governance gap identified |
| `test_no_external_usecase_tokens_in_decision_fields` excludes `claim_boundary` from token check (claim boundary prose is allowed to carry the negative evidence tokens by design) | RULE_GAP | DOCUMENTATION_ONLY_LEARNING | N/A_WITH_REASON | The exclusion is documented inline and is consistent with claim-boundary purpose; no new rule needed |

No new governance rule, machine check, or template update is required from this
pilot execution.

## Acceptance Criteria Check (self-reported, for Codex review)

| Criterion | Self-assessed evidence | Status |
| --- | --- | --- |
| Four synthetic samples cover all scan dispositions | `test_pilot_corpus_covers_all_scan_dispositions` passes | PASS |
| DIR gates remain disjoint from scan dispositions | overlap checker COMPLIANT, overlap count 0 | PASS |
| Document Translator remains downstream context only | no DT file access; no DT path in changed files | PASS |
| No external files or services are used | negative evidence section above | PASS |
| Worker does not commit | `git status --short` shows new files as untracked | PASS |

Note: self-assessment is not independent review. Codex reviewer must re-verify.

## Claim Boundary

This worker return provides local deterministic foundation pilot evidence only.
It does not claim document intelligence behavior validated against real documents,
extraction accuracy, OCR quality, provider behavior, retrieval quality, Document
Translator readiness, Policy_Local readiness, public readiness, production
readiness, hosted readiness, memory reinjection, high-risk promotion, or
autonomous mutation.

rawMemoryReleased=false
