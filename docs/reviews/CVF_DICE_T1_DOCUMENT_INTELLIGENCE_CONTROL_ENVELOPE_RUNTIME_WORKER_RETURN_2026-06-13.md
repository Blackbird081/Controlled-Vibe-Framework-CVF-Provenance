# CVF DICE-T1 Document Intelligence Control Envelope Runtime - Worker Return

Memory class: FULL_RECORD

Status: WORKER_RETURN_ACCEPTED_BY_CODEX

docType: worker_return

Date: 2026-06-13

Worker: Claude

Disposition: WORKER_RETURN_ACCEPTED_BY_CODEX

Worker base HEAD (executionBaseHead): `579962d7`

Worker return HEAD: `0fd52604` (no new commit; WORKER_MUST_NOT_COMMIT observed)

rawMemoryReleased=false

workOrder:
`docs/work_orders/CVF_AGENT_WORK_ORDER_DICE_T1_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_RUNTIME_FOR_CLAUDE_2026-06-13.md`

GC-018:
`docs/baselines/CVF_GC018_DICE_T1_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_RUNTIME_2026-06-13.md`

## Purpose

Record Claude's worker-return evidence for the DICE-T1 Document Intelligence
Control Envelope runtime tranche under `WORKER_MUST_NOT_COMMIT`. Codex owns
review, reviewer-owned closure conversion, session continuity, and commit.

## Scope / Target / Owner Boundary

Target: DICE-T1 local deterministic control envelope source, focused tests,
and worker-return evidence.

Owner boundary: Claude owns only the allowed-scope source, focused tests, and
this worker-return packet. Codex owns independent review, closure conversion,
roadmap/work-order finalization, session continuity, and commits.

## Scope / Methodology

Claude created a local deterministic envelope module that composes existing
DIR, EXA-T2 scan-route, and scan outcome owner surfaces; added focused tests
for DICE-MC-01 through DICE-MC-10; reran required proof commands; and reported
negative evidence for forbidden scope. The worker did not run OCR, call
providers, inspect external repositories, mutate session state, or commit.

## Target / Source

| Item | Path | Disposition |
| --- | --- | --- |
| DICE-T1 source | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_control_envelope.py` | CREATED |
| DICE-T1 focused tests | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_control_envelope.py` | CREATED |
| Worker-return packet | `docs/reviews/CVF_DICE_T1_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_RUNTIME_WORKER_RETURN_2026-06-13.md` | CREATED |
| DIR owner source | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | CONSUMED_ONLY |
| EXA-T2 scan-route owner source | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | CONSUMED_ONLY |
| Scan outcome report owner source | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | CONSUMED_ONLY |
| Extraction confidence owner source | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | CONSUMED_ONLY |

## WORKER_MUST_NOT_COMMIT Observed

Confirmed. No commit was created. All new artifacts are uncommitted in the working
tree. git status --short output:

```
?? EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_control_envelope.py
?? EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_control_envelope.py
```

The worker-return packet itself
`docs/reviews/CVF_DICE_T1_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_RUNTIME_WORKER_RETURN_2026-06-13.md`
is also uncommitted and appears as an additional `??` entry when created.

## Files Created Or Modified

| Path | Action |
| --- | --- |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_control_envelope.py` | CREATED |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_control_envelope.py` | CREATED |
| `docs/reviews/CVF_DICE_T1_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_RUNTIME_WORKER_RETURN_2026-06-13.md` | CREATED (this file) |

No existing file was modified. `src/__init__.py` was not modified (no export
change needed; tests use `sys.path.insert` matching the existing pattern).

## Proof Manifest Results

| Proof | Path | Required literal | Result |
| --- | --- | --- | --- |
| envelope source symbol | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_control_envelope.py` | `build_document_intelligence_control_envelope` | PASS - present at line 110 |
| envelope source result | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_control_envelope.py` | `DocumentIntelligenceControlEnvelopeResult` | PASS - present at line 95 |
| DICE-MC-08 regression | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_control_envelope.py` | `DICE-MC-08` | PASS - present in test names and docstrings |
| blocked handoff regression | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_control_envelope.py` | `DICE_MUST_NOT_FORWARD_BLOCKED_HANDOFF` | PASS - present at parametrized test assertion |
| worker return disposition | this file | `WORKER_RETURN_SUBMITTED_UNCOMMITTED` | PASS - present in Status and Disposition fields |

## Required Commands Results

### Command 1: DICE-T1 focused tests

```
python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_control_envelope.py -v
```

Result: **25 passed in 0.18s**

All 25 tests PASS. No failures, no errors.

### Command 2: Combined suite (DIR + scan outcome + DICE-T1)

```
python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_router.py EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_scan_outcome_report.py EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_control_envelope.py -v
```

Result: **50 passed in 0.19s**

All 50 tests PASS. Prior DIR and scan outcome tests are unaffected.

### Command 3: Governance reviewer-fast hook chain

```
python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast
```

Result: **All reviewer-fast governance checks passed. 13/13 PASS.**

Note: Initial run found 1 violation (non-ASCII em-dash characters in string
literals in the test file). Repaired immediately by replacing em-dash `--` with
ASCII ` - ` in 3 assertion message strings. No forbidden scope was touched to
make the repair.

## DICE-MC Proof Table

| Candidate ID | Required proof | Test name(s) | Result |
| --- | --- | --- | --- |
| DICE-MC-01 | DICE does not define a new ScanRouteDisposition literal owner | `test_DICE_MC_01_envelope_module_does_not_define_scan_route_disposition` | PASS |
| DICE-MC-02 | DICE does not define a new AuthorizationGate literal owner | `test_DICE_MC_02_envelope_module_does_not_define_authorization_gate` | PASS |
| DICE-MC-03 | DICE does not define a new DownstreamCapability literal owner | `test_DICE_MC_03_envelope_module_does_not_define_downstream_capability` | PASS |
| DICE-MC-04 | blocked/provider/OCR gates do not produce unqualified downstream handoff | `test_DICE_MC_04_blocked_ocr_operator_gates_produce_blocked_handoff` (parametrized x3) + `test_DICE_MC_04_operator_review_required_blocks_handoff` | PASS |
| DICE-MC-05 | operator_review_required is surfaced in envelope result | `test_DICE_MC_05_operator_review_required_surfaced_when_true` + `test_DICE_MC_05_operator_review_required_false_on_clean_pass` | PASS |
| DICE-MC-06 | scan_decision_digest is preserved | `test_DICE_MC_06_scan_decision_digest_is_preserved_from_dir` | PASS |
| DICE-MC-07 | decision_version is preserved | `test_DICE_MC_07_decision_version_is_preserved_from_dir` | PASS |
| DICE-MC-08 | downstream eligibility not widened beyond DIR output; DIR passthrough preserved | `test_DICE_MC_08_downstream_eligibility_is_not_widened_beyond_dir_output` + `test_DICE_MC_08_dir_passthrough_preserved_for_local_deterministic_allowed` + `test_DICE_MC_08_blocked_route_yields_abstain_passthrough` + `test_DICE_MC_08_ocr_route_yields_operator_review_only_passthrough` | PASS |
| DICE-MC-09 | no new OCR confidence threshold is introduced | `test_DICE_MC_09_envelope_module_does_not_define_ocr_confidence_threshold` + `test_DICE_MC_09_envelope_does_not_evaluate_ocr_confidence_directly` | PASS |
| DICE-MC-10 | scan findings preserved without filtering or suppression | `test_DICE_MC_10_scan_findings_preserved_without_filtering` + `test_DICE_MC_10_additional_findings_preserved_without_suppression` + `test_DICE_MC_10_empty_findings_preserved` | PASS |

## Work-Order Fulfillment Manifest

### Required Artifact Manifest

| Path | Required at handoff | Status |
| --- | --- | --- |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_control_envelope.py` | Yes | CREATED |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_document_intelligence_control_envelope.py` | Yes | CREATED |
| `docs/reviews/CVF_DICE_T1_DOCUMENT_INTELLIGENCE_CONTROL_ENVELOPE_RUNTIME_WORKER_RETURN_2026-06-13.md` | Yes | CREATED |

### Forbidden Path Manifest

| Path | Status |
| --- | --- |
| `D:/UNG DUNG AI/TOOL AI 2026/CVF-Workspace/Document_Translator` | UNTOUCHED - not read, listed, hashed, imported, or modified |
| external Policy_Local tree | UNTOUCHED - not read, listed, hashed, imported, or modified |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | UNTOUCHED - consumed only via import; not modified |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | UNTOUCHED - consumed only via import; not modified |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | UNTOUCHED - consumed only via import; not modified |
| `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | UNTOUCHED - consumed only via import; not modified |
| `governance/compat/**` | UNTOUCHED - no checker created or modified |
| `CVF_SESSION/**` | UNTOUCHED - no session-state mutation by worker |
| `CVF_SESSION_MEMORY.md` | UNTOUCHED - no front-door mutation by worker |
| `AGENT_HANDOFF*.md` | UNTOUCHED - no handoff mutation by worker |
| public-sync repository | UNTOUCHED - not accessed |
| provider key files and environment files | UNTOUCHED - not accessed |

## Negative Scope Evidence

The following forbidden scope classes were NOT used in this DICE-T1 worker execution:

- External Document Translator source: NOT accessed. No read, list, hash, import,
  or modify of `D:/UNG DUNG AI/TOOL AI 2026/CVF-Workspace/Document_Translator`.
- External Policy_Local tree: NOT accessed.
- OCR/provider/API execution: NOT performed. No OCR library imported or called.
  No provider API key read or used. No HTTP/external call made.
- Retrieval runtime: NOT used. No retrieval index query performed.
- Corpus ingestion: NOT performed. No corpus record created or modified.
- Public-sync: NOT performed. No public-sync repository access.
- Generated aggregate edits: NONE. No generated aggregate file was modified.
- Governance checker edits: NONE. No checker under `governance/compat/` was
  created or modified.
- Session-state mutation: NONE. `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, and
  `AGENT_HANDOFF*.md` were not modified by Claude worker.
- Readiness claims: NONE. No readiness, production, cost, quality, hosted, or
  public claim is made in the source or tests.
- Memory reinjection: NONE. rawMemoryReleased=false.

## Findings / Position

F-1: Required DICE-T1 artifacts were created in allowed scope only. PASS.

F-2: DICE-MC-01 through DICE-MC-10 are covered by focused tests, including the
DICE-MC-08 DIR eligibility passthrough invariant. PASS.

F-3: DICE-T1 composes existing owner surfaces and does not redefine
`ScanRouteDisposition`, `AuthorizationGate`, `DownstreamCapability`, or OCR
confidence threshold ownership. PASS.

F-4: Worker-return evidence initially used one abbreviated pseudo-path for this
worker-return file and omitted structural review headings required by the
reviewer-fast gate. Codex reviewer repaired the packet before closure.
ACCEPT_WITH_REVIEWER_REPAIR.

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Worker-return packet structure could block reviewer-fast | Codex reviewer added the required structural sections before commit |
| Abbreviated pseudo-path could weaken authority traceability | Codex reviewer replaced it with the full literal worker-return path |
| DICE runtime evidence could be misread as downstream app readiness | Claim boundary states no Document Translator, Policy_Local, OCR/provider, retrieval, production, public, cost, quality, or readiness claim |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action | Result |
| --- | --- | --- | --- | --- | --- |
| DICE-MC-01/02/03 test strategy checks imported owner type identity rather than name absence, matching the constraint that DICE may import but must not redefine owner types | RULE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | Carry as a reusable helper candidate if future composition modules repeat the same owner-identity proof pattern | Accepted, no DICE-T1 blocker |
| Non-ASCII em-dash in assertion strings was caught by reviewer-fast and repaired by the worker before return | WORKER_EXECUTION_ERROR | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | No new rule; existing text encoding discipline standard and gate already caught the issue | Repaired |
| Runtime/provider/cost learning applicability | N/A_WITH_REASON | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | No runtime/provider/cost behavior changed; DICE-T1 is local deterministic source/tests only | No runtime/provider/cost control change |
| Worker-return structural and pseudo-path issues found by Codex reviewer | WORKER_EXECUTION_ERROR | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | Repair in packet and rely on reviewer-fast structural and authority gates | Repaired before commit |

Defect class: `RULE_GAP`, `WORKER_EXECUTION_ERROR`, and `N/A_WITH_REASON`.

Learning lane summary: `GOVERNANCE_CONTROL_PLANE` with
`RUNTIME_BEHAVIOR_LEARNING` marked `N/A_WITH_REASON` for unchanged
runtime/provider/cost behavior.

Next action: no new rule, template, or machine-check promotion is required for
DICE-T1 closure; existing reviewer-fast and text encoding gates caught the
reviewer-return defects.

## Claim Boundary

DICE-T1 is local deterministic CVF foundation source and tests only. It does not
authorize OCR/provider/API execution, external app tree access, retrieval behavior
changes, route/API wiring, corpus ingestion, public-sync, document correctness
claims, extraction accuracy claims, provider quality claims, readiness claims, cost
claims, memory reinjection, high-risk promotion, or autonomous mutation.

rawMemoryReleased=false
