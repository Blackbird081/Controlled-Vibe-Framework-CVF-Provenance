# CVF Work Order - LPCI2-T6 PolicyLocal Search/Chat Readiness Gate

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: work_order

Date: 2026-06-04

dispatchBaseHead: `802ec7f3`
closureBaseHead: `NOT_EXECUTED_YET`

Commit mode: WORKER_MUST_NOT_COMMIT

## Purpose

Execute LPCI2-T6 as a bounded readiness gate review. The goal is a machine-readable
verdict — READY, NOT_READY, or READY_WITH_CONDITIONS — on whether the current
PolicyLocal corpus evidence (T4 + T5) is sufficient to open any search or chat
layer. This work order does not authorize building search, chat, a vector store,
embeddings, or any runtime component. It produces a decision record only.

T5 deferred one explicit finding that must be resolved before search/chat can
open:

- **T5-F1 (implicit):** search/chat readiness gate not opened in T5 scope.
  T5 completion review and roadmap both state: *"Open bounded search/chat
  readiness gate as a separate work order. Do not start search, chat runtime,
  or product implementation until that readiness gate closes."*

T6 evaluates five gates against the T4+T5 evidence base:

1. Corpus completeness gate — are the source files fully enumerated, hashed,
   and provenance-stable?
2. Classification depth gate — does the current `READ_DEEP` + `DEEP_CLASSIFIED`
   state plus `answerClass=SUMMARY_WITH_SOURCE` meet the minimum bar for
   search/retrieval use?
3. Corpus Search And Filter Readiness gate — does the evidence satisfy the
   `CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md` required
   capability set?
4. Response boundary gate — are the `ESCALATE_OR_ABSTAIN` and
   `SUMMARY_WITH_SOURCE` boundaries machine-checkable and recorded so that a
   search layer cannot silently drop them?
5. Missing capability gap register — what concrete missing elements (faceted
   index schema, query receipt model, derived view trace, conflict/freshness
   model, negative search evidence) must be authored before any search layer
   opens?

Success: each gate is evaluated with a PASS, PARTIAL, or BLOCKED verdict, a
missing-capability gap register is produced, and the overall readiness verdict
is recorded. If verdict is READY_WITH_CONDITIONS, conditions must be discrete
and each assigned a remediation work order stub. If verdict is NOT_READY, the
blocking gaps must be recorded with disposition `MUST_CLOSE_BEFORE_SEARCH`.

## Scope / Target / Owner Boundary

Target corpus: two DOCX files at
`D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\`

Target evidence base:
- `Policy_Local/data/generated/policylocal-corpus-records.json`
  (schemaVersion `policylocal.corpusRecords.t5.v1`)
- `Policy_Local/data/generated/policylocal-t5-deep-scan-evidence.json`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
  (entry `policylocal-production-corpus-dropzone`)
- T4 completion review:
  `docs/reviews/CVF_LPCI2_T4_CORPUS_INTELLIGENCE_IMPORT_CLASSIFICATION_EVIDENCE_COMPLETION_2026-06-04.md`
- T5 completion review:
  `docs/reviews/CVF_LPCI2_T5_POLICYLOCAL_DEEP_CLASSIFICATION_COMPLETION_2026-06-04.md`

Owner boundary: Codex executes orchestrator, reviewer, and closer roles.
This is a review/decision tranche only — no runtime implementation.
WORKER_MUST_NOT_COMMIT.

## Authority Chain

| Authority | Path or note | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-04 session — T5 closed; next move is search/chat readiness gate work order | ACCEPT |
| T5 completion review finding-to-governance disposition | `docs/reviews/CVF_LPCI2_T5_POLICYLOCAL_DEEP_CLASSIFICATION_COMPLETION_2026-06-04.md` §Finding-To-Governance Learning Disposition | ACCEPT — "Open bounded search/chat readiness gate as a separate work order" |
| LPCI2 roadmap | `docs/roadmaps/CVF_LPCI2_POLICYLOCAL_PRODUCTIZATION_ROADMAP_2026-06-03.md` | ACCEPT — T5 CLOSED_PASS_BOUNDED; T6 readiness gate is next |
| Corpus Search And Filter Readiness Standard | `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md` | ACCEPT — canonical readiness standard for this gate |
| GC-047 Corpus Completeness standard | `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md` | ACCEPT |
| GC-048 Knowledge Map Reconciliation standard | `docs/reference/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_STANDARD_2026-06-01.md` | ACCEPT — T5 produced RECONCILED_VERIFIED; T6 inherits |
| GC-050 Classification standard | `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md` | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT — mode `lpci2_t5_policylocal_deep_classification_closed_pass_bounded` |
| LPCI1-T2 domain classification spec | `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` | ACCEPT — response-boundary matrix carries forward |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| T5 corpus records path and schemaVersion | `docs/reviews/CVF_LPCI2_T5_POLICYLOCAL_DEEP_CLASSIFICATION_COMPLETION_2026-06-04.md` | §Evidence Trace Block | `Policy_Local/data/generated/policylocal-corpus-records.json` schemaVersion `policylocal.corpusRecords.t5.v1` | LPCI2-T5 completion | ACCEPT |
| T5 deep scan evidence path | `docs/reviews/CVF_LPCI2_T5_POLICYLOCAL_DEEP_CLASSIFICATION_COMPLETION_2026-06-04.md` | §Evidence Trace Block | `Policy_Local/data/generated/policylocal-t5-deep-scan-evidence.json` | LPCI2-T5 completion | ACCEPT |
| effectiveDate=2026-07-01 both files | `docs/reviews/CVF_LPCI2_T5_POLICYLOCAL_DEEP_CLASSIFICATION_COMPLETION_2026-06-04.md` | §Findings T5-RESOLVED: T4-F1 | effectiveDateCharPosition; P1_effective_clause | T5 deep scan evidence | ACCEPT |
| GC-048 verdict RECONCILED_VERIFIED | `docs/reviews/CVF_LPCI2_T5_POLICYLOCAL_DEEP_CLASSIFICATION_COMPLETION_2026-06-04.md` | §Knowledge System Reconciliation; Knowledge-map verdict field | `RECONCILED_VERIFIED` | GC-048 checker | ACCEPT |
| answerClass=SUMMARY_WITH_SOURCE active | `docs/reviews/CVF_LPCI2_T5_POLICYLOCAL_DEEP_CLASSIFICATION_COMPLETION_2026-06-04.md` | §Corpus Intelligence Classification | Response Boundary field | GC-050 standard | ACCEPT |
| ESCALATE_OR_ABSTAIN enforced for legal-advice | `docs/reviews/CVF_LPCI2_T5_POLICYLOCAL_DEEP_CLASSIFICATION_COMPLETION_2026-06-04.md` | §Adversarial Sampling S4 row | ESCALATE_OR_ABSTAIN | T5 adversarial sampling | ACCEPT |
| Corpus Search And Filter Readiness Standard required capabilities | `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md` | §Required Capabilities table | nine capability rows | CVF Search/Filter Readiness Standard | ACCEPT |
| GC-051 registry entry policylocal-production-corpus-dropzone | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | entry key `policylocal-production-corpus-dropzone` | GC-051 registry entry | Corpus Scan Registry | ACCEPT |

## New Doc-Only Fields

| New doc-only field | Purpose | Not sourced from runtime? | Runtime claim blocked? | Validation expectation |
| --- | --- | --- | --- | --- |
| `readinessVerdict` | Overall search/chat readiness verdict for T6 completion | Yes | Yes | must be READY, NOT_READY, or READY_WITH_CONDITIONS |
| `gateVerdict` | Per-gate verdict (PASS, PARTIAL, BLOCKED) in the five-gate evaluation | Yes | Yes | doc/schema/checklist validation only |
| `missingCapabilityGap` | Enumerated missing capabilities blocking or conditioning readiness | Yes | Yes | doc/schema/checklist validation only |
| `remediationStub` | Named follow-on work order stub for each READY_WITH_CONDITIONS gap | Yes | Yes | name-only; no content or runtime claim |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command | Status |
| --- | --- | --- | --- | --- |
| Open bounded search/chat readiness gate after T5 closes | §Purpose; §Five-Gate Evaluation | T6 completion review `readinessVerdict` field | `python governance/compat/check_markdown_structural_completeness.py --base 802ec7f3 --head HEAD --enforce` | DISPATCH_READY |
| Corpus completeness gate | §Five-Gate Evaluation Gate 1 | Gate 1 verdict + evidence citations | `python governance/compat/check_corpus_completeness_report_integrity.py --base 802ec7f3 --head HEAD --enforce` | DISPATCH_READY |
| Classification depth gate | §Five-Gate Evaluation Gate 2 | Gate 2 verdict + READ_DEEP/DEEP_CLASSIFIED confirmation | `python governance/compat/check_corpus_intelligence_classification.py --base 802ec7f3 --head HEAD --enforce` | DISPATCH_READY |
| Corpus Search And Filter Readiness gate | §Five-Gate Evaluation Gate 3 | Gate 3 verdict + `## Corpus Search And Filter Readiness` block | `python governance/compat/check_corpus_completeness_report_integrity.py --base 802ec7f3 --head HEAD --enforce` | DISPATCH_READY |
| Response boundary gate | §Five-Gate Evaluation Gate 4 | Gate 4 verdict + boundary enforcement evidence | `python governance/compat/check_corpus_intelligence_classification.py --base 802ec7f3 --head HEAD --enforce` | DISPATCH_READY |
| Missing capability gap register | §Five-Gate Evaluation Gate 5; §Gap Register | gap table with MUST_CLOSE_BEFORE_SEARCH or remediation stub | `python governance/compat/check_markdown_structural_completeness.py --base 802ec7f3 --head HEAD --enforce` | DISPATCH_READY |
| Session state sync | §Execution Plan step 8 | CVF_SESSION_MEMORY.md, ACTIVE_SESSION_STATE.json, AGENT_HANDOFF_V15 | `python governance/compat/check_active_session_state.py --enforce` | DISPATCH_READY |

## Agent Roles

| Role | Owner |
| --- | --- |
| Orchestrator | Codex unless reassigned |
| Implementer / Reviewer | Codex (review/decision tranche — same agent may hold both) |
| Closer | Codex closer role after gates pass |
| Worker commit boundary | WORKER_MUST_NOT_COMMIT |

## Worker Autonomy / No-Question Rule

The assigned agent must evaluate all five gates and produce the gap register
without asking the operator, as long as work stays within Allowed scope.

Escalation is reserved for:

- a gate evaluation would require live legal review or provider inference;
- corpus files are inaccessible or hash-drifted from T5 values;
- readiness verdict is NOT_READY and the operator must decide whether to proceed
  to a larger remediation roadmap or pause the LPCI2 lane;
- any action that would exceed Allowed scope, open search/chat/runtime, or
  consume provider quota.

## Allowed Scope

- Read T4 and T5 corpus records, evidence JSON, and completion reviews.
- Read the Corpus Search And Filter Readiness Standard and related GC-047/
  GC-048/GC-050 standards.
- Write T6 completion review at
  `docs/reviews/CVF_LPCI2_T6_SEARCH_CHAT_READINESS_GATE_COMPLETION_2026-06-04.md`.
- Update `docs/roadmaps/CVF_LPCI2_POLICYLOCAL_PRODUCTIZATION_ROADMAP_2026-06-03.md`
  T6 row status.
- Update `CVF_SESSION_MEMORY.md`, `CVF_SESSION/ACTIVE_SESSION_STATE.json`, and
  `AGENT_HANDOFF_V15_2026-05-29.md` for T6 closure.
- Run local CVF governance gate commands.

## Forbidden Scope

- Do not build a chatbot, search index, search API route, vector store,
  embedding pipeline, provider call, hosted deployment, or public-sync batch.
- Do not author any runtime source file under `EXTENSIONS/` or `cvf-web/`.
- Do not claim search/chat readiness without completing the five-gate evaluation.
- Do not claim legal advice, latest-law correctness, production readiness, or
  public release readiness.
- Do not open a follow-on search/chat implementation work order in this same
  tranche — remediation stubs are name-only placeholders; a new operator
  instruction is required to open and dispatch them.

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V15_2026-05-29.md`
- `docs/reviews/CVF_LPCI2_T5_POLICYLOCAL_DEEP_CLASSIFICATION_COMPLETION_2026-06-04.md`
- `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md`
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-corpus-records.json`

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short --branch
Test-Path "D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-corpus-records.json"
Test-Path "D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t5-deep-scan-evidence.json"
Test-Path "D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\116_2025_QH15_666020.docx"
Test-Path "D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\148_2025_QH15_675262.docx"
python governance/compat/check_active_session_state.py --enforce
```

Expected results:

- HEAD at or ahead of `802ec7f3`
- Worktree clean or only T6 working files
- Both DOCX files present
- T5 corpus records and deep scan evidence present
- Session state COMPLIANT

## 6A. Source-Fidelity Pass

Existing paths verified before dispatch:

- `docs/reviews/CVF_LPCI2_T5_POLICYLOCAL_DEEP_CLASSIFICATION_COMPLETION_2026-06-04.md` — PRESENT
- `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md` — PRESENT
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` — PRESENT
- `docs/roadmaps/CVF_LPCI2_POLICYLOCAL_PRODUCTIZATION_ROADMAP_2026-06-03.md` — PRESENT

Planned new paths (marked NEW):

- NEW: `docs/reviews/CVF_LPCI2_T6_SEARCH_CHAT_READINESS_GATE_COMPLETION_2026-06-04.md`

## 6C. System Loop Interlock Routing

Upstream loop: T5 output (`policylocal-corpus-records.json` schemaVersion t5.v1;
GC-048 RECONCILED_VERIFIED; adversarial sampling 4/4 PASS) → T6 five-gate
evaluation.

Downstream loop input: T6 `readinessVerdict` and gap register → operator
decision on whether to open a search/chat implementation work order.

Machine-readable registry: `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
— no update required in T6 (no new scan wave; T6 is a review/decision tranche).

Finding packet routing:

- Gate verdict PASS → carry forward as satisfied prerequisite to any future
  search/chat work order.
- Gate verdict PARTIAL → record in gap register with `READY_WITH_CONDITIONS`
  condition stub; operator must authorize remediation before search opens.
- Gate verdict BLOCKED → record as `MUST_CLOSE_BEFORE_SEARCH`; overall verdict
  must be NOT_READY for that gate; operator decides remediation path.

Claim boundary: T6 produces a readiness verdict and gap register. It does NOT
authorize search/chat runtime. A separate implementation work order — requiring
a fresh operator instruction — is needed to open any search or chat layer.

## Execution Plan

1. Capture `executionBaseHead` with `git rev-parse --short HEAD`.
2. Run pre-flight checks; stop and report if any DOCX file or T5 evidence file
   is missing or hash-drifted.
3. Evaluate Gate 1 — Corpus Completeness:
   - Confirm 2 assets enumerated, hashed (sha256), and provenance-stable from
     T4S manifest through T5 corpus records.
   - Confirm `processingStatus=READ_DEEP` for both files.
   - Confirm GC-051 registry entry `policylocal-production-corpus-dropzone`
     is present and reflects T5 scan state.
   - Verdict: PASS / PARTIAL / BLOCKED with evidence citations.
4. Evaluate Gate 2 — Classification Depth:
   - Confirm both files are `DEEP_CLASSIFIED` with `answerClass=SUMMARY_WITH_SOURCE`.
   - Confirm `effectiveDate=2026-07-01` confirmed via P1_effective_clause for both.
   - Confirm `jurisdiction=VN_NATIONAL; documentType=law; status=amended` for both.
   - Confirm adversarial sampling 4/4 PASS carried from T5.
   - Verdict: PASS / PARTIAL / BLOCKED with evidence citations.
5. Evaluate Gate 3 — Corpus Search And Filter Readiness Standard:
   - Map each of the nine required capabilities in the standard against current T4/T5
     evidence; record PRESENT, PARTIAL, or ABSENT for each.
   - PRESENT = evidence exists in T4/T5 artifacts; PARTIAL = evidence exists but
     gaps noted; ABSENT = no evidence, creates a gap register entry.
   - Produce a `## Corpus Search And Filter Readiness` block in the completion
     review meeting the standard's block format.
   - Verdict: PASS (all PRESENT) / PARTIAL (≥1 PARTIAL, no ABSENT) /
     BLOCKED (≥1 ABSENT that is required before search).
6. Evaluate Gate 4 — Response Boundary:
   - Confirm `ESCALATE_OR_ABSTAIN` is documented and enforced for: legal-advice
     queries, current-applicability queries (law not yet in force as of 2026-06-04),
     and queries requiring legal interpretation.
   - Confirm `SUMMARY_WITH_SOURCE` is the active ceiling for search answers.
   - Confirm `DIRECT_CITED_ANSWER` remains blocked (insufficient citation depth).
   - Verdict: PASS / PARTIAL / BLOCKED.
7. Evaluate Gate 5 — Missing Capability Gap Register:
   - Enumerate all PARTIAL or ABSENT items from Gates 1–4.
   - For each: assign `gapId`, `description`, `blockingClass`
     (`MUST_CLOSE_BEFORE_SEARCH` or `REMEDIATION_RECOMMENDED`), and
     `remediationStub` (name-only work order placeholder, no content).
   - Produce `## Gap Register` table in the completion review.
8. Record overall `readinessVerdict`:
   - READY: all five gates PASS, gap register empty.
   - READY_WITH_CONDITIONS: all gates PASS or PARTIAL, gap register has only
     `REMEDIATION_RECOMMENDED` entries; each condition has a remediation stub.
   - NOT_READY: any gate BLOCKED or any gap register entry has
     `MUST_CLOSE_BEFORE_SEARCH`.
9. Write T6 completion review
   `docs/reviews/CVF_LPCI2_T6_SEARCH_CHAT_READINESS_GATE_COMPLETION_2026-06-04.md`
   including all required sections (see §Required Outputs).
10. Update roadmap T6 row to `CLOSED_PASS_BOUNDED`.
11. Run required governance gates.
12. Update session state files.
13. Stop for operator commit (WORKER_MUST_NOT_COMMIT).

## Five-Gate Evaluation Summary (dispatch-time expectation)

This table records the expected gate evaluation direction at dispatch, based on
T4+T5 evidence. Worker must verify each against actual artifacts, not this table.

| Gate | Name | T4+T5 evidence available | Expected gap area |
| --- | --- | --- | --- |
| Gate 1 | Corpus Completeness | 2 files; sha256 hashed; GC-051 registered; READ_DEEP both | None anticipated; verify registry is current |
| Gate 2 | Classification Depth | DEEP_CLASSIFIED; answerClass=SUMMARY_WITH_SOURCE; effectiveDate confirmed; adversarial 4/4 PASS | None anticipated |
| Gate 3 | Search/Filter Readiness Standard | Corpus discovery index: partial (manifest has hash+path but no topicTags/sensitivity/freshnessStatus); query receipt model: absent; derived view trace: partial (no retrieval layer yet); negative search evidence: absent | Multiple PARTIAL/ABSENT expected |
| Gate 4 | Response Boundary | ESCALATE_OR_ABSTAIN documented; SUMMARY_WITH_SOURCE ceiling active; T5-NOTE-1 not-in-force boundary recorded | None anticipated; confirm machine-checkable |
| Gate 5 | Gap Register | Derived from Gates 1–4 | At minimum: query receipt model, faceted index schema, negative search evidence, derived view trace to retrieval layer |

At dispatch, overall readiness verdict is expected to be NOT_READY or
READY_WITH_CONDITIONS given the search/filter standard gaps above.
Worker must record the actual verdict from evidence, not from this expectation.

## Required Governance Gates

```powershell
git add docs/reviews/CVF_LPCI2_T6_SEARCH_CHAT_READINESS_GATE_COMPLETION_2026-06-04.md

python governance/compat/check_corpus_completeness_report_integrity.py --base 802ec7f3 --head HEAD --enforce
python governance/compat/check_corpus_to_knowledge_map_reconciliation.py --base 802ec7f3 --head HEAD --enforce
python governance/compat/check_corpus_intelligence_classification.py --base 802ec7f3 --head HEAD --enforce
python governance/compat/check_markdown_structural_completeness.py --base 802ec7f3 --head HEAD --enforce
python governance/compat/check_finding_to_governance_learning.py --base 802ec7f3 --head HEAD --enforce
python governance/compat/check_work_order_dispatch_quality.py --base 802ec7f3 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 802ec7f3 --head HEAD
```

All gates must PASS before handoff to closer.

## Required Outputs

| Output | Path | Required at handoff |
| --- | --- | --- |
| T6 completion review | `docs/reviews/CVF_LPCI2_T6_SEARCH_CHAT_READINESS_GATE_COMPLETION_2026-06-04.md` | Yes |
| Roadmap T6 row updated | `docs/roadmaps/CVF_LPCI2_POLICYLOCAL_PRODUCTIZATION_ROADMAP_2026-06-03.md` | Yes |
| Session state synced | CVF_SESSION_MEMORY.md, ACTIVE_SESSION_STATE.json, AGENT_HANDOFF_V15 | Yes |

## Required Completion Review Sections

The T6 completion review must contain all of the following sections:

- `## Scope`
- `## Purpose`
- `## Five-Gate Evaluation` (with sub-sections Gate 1–5, each with verdict)
- `## Corpus Search And Filter Readiness` (block format per standard)
- `## Gap Register` (table: gapId, description, blockingClass, remediationStub)
- `## Readiness Verdict` (READY / NOT_READY / READY_WITH_CONDITIONS + rationale)
- `## Findings`
- `## Risk`
- `## Acceptance Criteria` (checklist)
- `## Verification` (gate commands + results)
- `## Finding-To-Governance Learning Disposition`
- `## Source Verification Block`
- `## Public Export Disposition`
- `## Claim Boundary`

## Acceptance Criteria

- [ ] Pre-flight checks PASS (both DOCX files and T5 evidence files present)
- [ ] Gate 1 Corpus Completeness evaluated with PASS/PARTIAL/BLOCKED verdict
- [ ] Gate 2 Classification Depth evaluated with PASS/PARTIAL/BLOCKED verdict
- [ ] Gate 3 Search/Filter Readiness Standard evaluated; all nine capabilities
      mapped; `## Corpus Search And Filter Readiness` block present
- [ ] Gate 4 Response Boundary evaluated with PASS/PARTIAL/BLOCKED verdict
- [ ] Gate 5 Gap Register produced; all PARTIAL/ABSENT items enumerated
- [ ] Overall `readinessVerdict` recorded (READY / NOT_READY /
      READY_WITH_CONDITIONS)
- [ ] `check_corpus_completeness_report_integrity.py` PASS
- [ ] `check_corpus_to_knowledge_map_reconciliation.py` PASS
- [ ] `check_corpus_intelligence_classification.py` PASS
- [ ] `check_markdown_structural_completeness.py` PASS
- [ ] `check_finding_to_governance_learning.py` PASS
- [ ] No search/chat/runtime/provider/product work added
- [ ] Session state synced and `check_active_session_state.py` COMPLIANT

## Review Gate

Reviewer must verify:

- All five gates are evaluated with explicit verdicts (PASS/PARTIAL/BLOCKED);
- Gap register contains all items with `blockingClass` and `remediationStub`;
- `readinessVerdict` is consistent with gate verdicts (NOT_READY if any gate
  BLOCKED; READY_WITH_CONDITIONS if any gate PARTIAL with no BLOCKED);
- `## Corpus Search And Filter Readiness` block is present and follows the
  standard format;
- no search/chat/runtime/provider/product work is present;
- session state synced and `check_active_session_state.py` COMPLIANT.

## Operator Checkpoint

Operator checkpoint is required before any move from T6 verdict to a
search/chat implementation work order or any runtime or product work.

If verdict is NOT_READY: operator must review the gap register and decide
whether to authorize a remediation roadmap or pause the LPCI2 lane.

If verdict is READY_WITH_CONDITIONS: operator must review each condition's
remediation stub and decide which to authorize first.

If verdict is READY: operator must explicitly authorize opening a search/chat
implementation work order before any implementation begins.

## Return Conditions

Return to orchestrator without implementation closure if:

- T5 evidence files are inaccessible or DOCX files have hash-drifted
- Any gate evaluation would require live legal review or provider inference
- Gate verdicts cannot be determined from T4/T5 evidence alone
- Any action within Allowed scope would inadvertently open search/chat runtime

## Corpus Intelligence Classification

- Classification task class: READINESS_GATE_REVIEW (review/decision tranche;
  no new corpus scan)
- Source corpus evidence: inherited from T5 — 2 DOCX files READ_DEEP;
  GC-048 RECONCILED_VERIFIED; adversarial sampling 4/4 PASS
- Knowledge map evidence: RECONCILED_VERIFIED (inherited from T5; no new
  reconciliation needed unless drift detected)
- Classification ledger: T5 corpus records at
  `Policy_Local/data/generated/policylocal-corpus-records.json`
  (schemaVersion policylocal.corpusRecords.t5.v1)
- Legal/policy corpus: VN_NATIONAL — 2 Vietnamese national law DOCX files;
  effectiveDate=2026-07-01 (both; not yet in force as of 2026-06-04)
- Response Boundary: DIRECT_CITED_ANSWER blocked pending runtime citation receipts; SUMMARY_WITH_SOURCE current ceiling; PROCEDURAL_GUIDANCE blocked pending procedural receipts; ESCALATE_OR_ABSTAIN required for legal-advice and current-applicability queries
- Classification verdict: READINESS_GATE — T6 does not change corpus records;
  classification evidence is inherited from T5

Domain fields: jurisdiction=VN_NATIONAL; authorityLevel=LAW; documentType=law;
effectiveDate=2026-07-01; sourceAuthority=local operator corpus evidence;
answerBoundary=SUMMARY_WITH_SOURCE ceiling plus ESCALATE_OR_ABSTAIN for legal
advice and current-applicability queries.

Response boundary classes:

- DIRECT_CITED_ANSWER: BLOCKED in T6; current corpus evidence is not yet a
  search/chat runtime with citation-selection receipts.
- SUMMARY_WITH_SOURCE: ALLOWED as the current ceiling inherited from T5.
- PROCEDURAL_GUIDANCE: BLOCKED in T6 unless later work adds procedural guidance
  receipts and operator approval.
- ESCALATE_OR_ABSTAIN: REQUIRED for legal-advice, applicability, conflict, or
  freshness-sensitive queries.

Classification ledger:

| sourcePath | processingStatus | knowledgeRegion | ownerSurface | disposition | evidencePointer |
| --- | --- | --- | --- | --- | --- |
| `Policy_Local/data/generated/policylocal-corpus-records.json` | READ_DEEP | legal_policy_corpus | corpus_intelligence | ACCEPT_SUMMARY_ONLY | `docs/reviews/CVF_LPCI2_T5_POLICYLOCAL_DEEP_CLASSIFICATION_COMPLETION_2026-06-04.md` |
| `Policy_Local/data/generated/policylocal-t5-deep-scan-evidence.json` | READ_DEEP | legal_policy_corpus | corpus_intelligence | ACCEPT_SUMMARY_ONLY | `docs/reviews/CVF_LPCI2_T5_POLICYLOCAL_DEEP_CLASSIFICATION_COMPLETION_2026-06-04.md` |

Adversarial sampling plan: T6 must evaluate whether the T5 4/4 adversarial
sampling evidence is sufficient for search/chat readiness. It must not claim
new semantic correctness unless it adds a separate sample table with source
citations, verdicts, and claim boundaries in the T6 completion artifact.

## Write Ownership

Owned repo paths:

- `docs/reviews/CVF_LPCI2_T6_SEARCH_CHAT_READINESS_GATE_COMPLETION_2026-06-04.md` (NEW)
- `docs/roadmaps/CVF_LPCI2_POLICYLOCAL_PRODUCTIZATION_ROADMAP_2026-06-03.md` (UPDATE — T6 row)
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V15_2026-05-29.md`

Forbidden paths (do not touch):

- All runtime source files under `EXTENSIONS/` and `cvf-web/`
- `Policy_Local/data/generated/policylocal-corpus-records.json`
  (T5 records are read-only in T6 scope; no mutation)
- Public-sync clone
- Any file not in the owned list above

## Forbidden Filesystem State At Dispatch

| Forbidden path | Expected state | Actual state at dispatch | Action if PRESENT |
| --- | --- | --- | --- |
| `docs/reviews/CVF_LPCI2_T6_SEARCH_CHAT_READINESS_GATE_COMPLETION_2026-06-04.md` | ABSENT | ABSENT ✓ | Stop; reconcile before re-dispatch |

## Evidence Requirements

Base-anchor evidence:

- `dispatchBaseHead`: `802ec7f3`
- `closureBaseHead`: `NOT_EXECUTED_YET`
- Commit mode: WORKER_MUST_NOT_COMMIT
- Pending-artifact component gates: worker runs and repairs; records PASS before handoff
- Committed-range `pre-closure`: PASS after operator commit

Required evidence trace at handoff:

- Claim: five-gate evaluation completed against T4+T5 evidence
- Key path: `docs/reviews/CVF_LPCI2_T6_SEARCH_CHAT_READINESS_GATE_COMPLETION_2026-06-04.md`
- Verdict: READY / NOT_READY / READY_WITH_CONDITIONS with gate-by-gate support
- Gate commands: all PASS before handoff

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: LPCI2-T6 dispatch session-state sync only.

Protected paths:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V15_2026-05-29.md`

Operator authorization: T5 CLOSED_PASS_BOUNDED at commit `53b2bac4`;
T6 work order authored per operator instruction confirming T5 is closed and
T6 readiness gate is the next allowed move; session state synced to
`lpci2_t6_search_chat_readiness_gate_dispatch_ready`.

Rollback boundary: revert only the T6 dispatch session-state sync lines,
roadmap T6 status row, and this work order if the T6 dispatch is found
incorrect. Do not revert T5 closure evidence or prior session state lines.

## Closure Checklist

- [x] Work order has source verification block
- [x] Work order has roadmap-to-work-order trace matrix
- [x] Work order has Worker Autonomy / No-Question Rule
- [x] Work order names five-gate evaluation with per-gate criteria
- [x] Work order names Corpus Search And Filter Readiness Standard as authority
- [x] Work order forbids search/chat/runtime/product implementation
- [x] Work order names operator checkpoint before search/chat implementation
- [x] Forbidden filesystem state at dispatch verified ABSENT

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this work order references private local workspace files and a private
operator corpus. A sanitized guide may be prepared later as a separate
public-sync batch.

## Claim Boundary

This work order authorizes only a readiness gate review — evaluating five gates
against T4+T5 corpus evidence and producing a verdict plus gap register.

It does not authorize search runtime, chat runtime, provider calls, vector store
creation, embedding pipeline, hosted deployment, legal advice correctness,
latest-law status, production readiness, public export, or any search/chat
implementation work. A separate operator instruction and work order are required
before any of those activities begin.
