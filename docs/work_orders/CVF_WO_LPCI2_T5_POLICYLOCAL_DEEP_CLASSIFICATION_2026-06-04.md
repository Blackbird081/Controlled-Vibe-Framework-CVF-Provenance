# CVF Work Order - LPCI2-T5 PolicyLocal Deep Classification

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: work_order

Date: 2026-06-04

dispatchBaseHead: `7325b549`

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

closureBaseHead: NOT_EXECUTED_YET

Commit mode: WORKER_MUST_NOT_COMMIT

## Purpose

Execute LPCI2-T5 as a bounded deep-classification evidence tranche for the two
PolicyLocal DOCX files that were read and shallowly classified in T4.

T4 left three deferred findings:

- T4-F1: `effectiveDate=unknown` — header-only scan did not locate the effective
  date clause.
- T4-F2: search/chat/runtime blocked — `READ_SHALLOW` + `effectiveDate=unknown`
  is not sufficient for any retrieval runtime.
- T4-F3: GC-048 knowledge-map reconciliation not run — T4 was evidence-only.

T5 must close all three via:

1. Full-body text scan of both DOCX files to locate and verify `effectiveDate`.
2. GC-048 knowledge-map reconciliation against the T4 corpus records.
3. Adversarial sampling against the T5-upgraded corpus records.
4. Produce a T5 completion review containing a `Knowledge System Reconciliation`
   section (GC-048 required) meeting the machine check requirements.

Success: T4-F1, T4-F2 (partially), and T4-F3 are all resolved or formally
deferred with updated disposition evidence. Readiness gate for search/chat
remains a separate work order opened only after T5 closes.

## Scope / Target / Owner Boundary

Target local workspace:

`D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local`

Target corpus records:

`D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-corpus-records.json`

Owner boundary: Codex executes orchestrator, worker, reviewer, and closer roles
for this bounded evidence tranche. WORKER_MUST_NOT_COMMIT; operator commits the
T5 artifacts.

## Authority Chain

| Authority | Path or note | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-04 operator confirmed T4 CLOSED_PASS_BOUNDED at commit `212d6adf`; next move is T5+ deep classification | ACCEPT |
| T4 completion review | `docs/reviews/CVF_LPCI2_T4_CORPUS_INTELLIGENCE_IMPORT_CLASSIFICATION_EVIDENCE_COMPLETION_2026-06-04.md` | ACCEPT |
| T4 findings T4-F1, T4-F2, T4-F3 | T4 completion review §Findings | ACCEPT — these are the deferred items T5 must address |
| LPCI2 roadmap | `docs/roadmaps/CVF_LPCI2_POLICYLOCAL_PRODUCTIZATION_ROADMAP_2026-06-03.md` | ACCEPT — T5 released from HOLD_UNTIL_T4_AND_MEMORY_CHECKPOINT by T4 closure |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT — mode lpci2_t5_policylocal_deep_classification_dispatch_ready |
| Corpus Intelligence standard | `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md` | ACCEPT |
| LPCI1-T2 domain classification spec | `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` | ACCEPT |
| GC-048 machine check | `governance/compat/check_corpus_to_knowledge_map_reconciliation.py` | ACCEPT |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| T4 corpus records exist at path | `docs/reviews/CVF_LPCI2_T4_CORPUS_INTELLIGENCE_IMPORT_CLASSIFICATION_EVIDENCE_COMPLETION_2026-06-04.md` | §Evidence Trace Block | `Policy_Local/data/generated/policylocal-corpus-records.json` | LPCI2-T4 completion | ACCEPT |
| T4-F1 effectiveDate=unknown deferred | `docs/reviews/CVF_LPCI2_T4_CORPUS_INTELLIGENCE_IMPORT_CLASSIFICATION_EVIDENCE_COMPLETION_2026-06-04.md` | §Findings T4-F1 | effectiveDate field in corpus records | LPCI2-T4 completion | ACCEPT |
| T4-F3 GC-048 not run deferred | `docs/reviews/CVF_LPCI2_T4_CORPUS_INTELLIGENCE_IMPORT_CLASSIFICATION_EVIDENCE_COMPLETION_2026-06-04.md` | §Findings T4-F3 | GC-048 not run in T4 scope | LPCI2-T4 completion | ACCEPT |
| GC-048 checker path | `governance/compat/check_corpus_to_knowledge_map_reconciliation.py` | line 38 REQUIRED_SECTION | GC-048 required section heading | GC-048 machine check | ACCEPT |
| GC-048 required fields | `governance/compat/check_corpus_to_knowledge_map_reconciliation.py` | lines 46–57 REQUIRED_SECTION_FIELDS | Knowledge task class, Source manifest, Source manifest hash, Enumeration safety, Intake registry or ledger, Authority assets, Derived views, Semantic region ledger, Region reconciliation, Orphan or unmapped assets, Cross-region links | GC-048 machine check | ACCEPT |
| GC-048 verdict values | `governance/compat/check_corpus_to_knowledge_map_reconciliation.py` | lines 39–44 ALLOWED_VERDICTS | RECONCILED_VERIFIED, RECONCILED_WITH_DECLARED_GAPS, PARTIAL_MAP, BLOCKED, STALE_MAP | GC-048 machine check | ACCEPT |
| GC-048 numeric count format | `governance/compat/check_corpus_to_knowledge_map_reconciliation.py` | line 209 `_extract_counts` | count format enforced by `_extract_counts` regex | GC-048 machine check | ACCEPT |
| answerClass canonical values | `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md` | Response-Boundary Classes | DIRECT_CITED_ANSWER, SUMMARY_WITH_SOURCE, PROCEDURAL_GUIDANCE, ESCALATE_OR_ABSTAIN | GC-050 standard | ACCEPT |
| python-docx available locally (T4-verified) | `docs/reviews/CVF_LPCI2_T4_CORPUS_INTELLIGENCE_IMPORT_CLASSIFICATION_EVIDENCE_COMPLETION_2026-06-04.md` | §Evidence Trace Block — both files EXTRACTED | python-docx 1.2.0 confirmed in T4 | LPCI2-T4 completion | ACCEPT |

## New Doc-Only Fields

| New doc-only field | Purpose | Not sourced from runtime? | Runtime claim blocked? | Validation expectation |
| --- | --- | --- | --- | --- |
| effectiveDateVerified | Boolean flag indicating effectiveDate was verified from document body (not header-only) | Yes | Yes | doc/schema/checklist validation only; no runtime read |
| adversarialSampleCount | Count of adversarial sample queries run against T5 corpus records | Yes | Yes | doc/schema/checklist validation only |
| knowledgeMapVerdict | GC-048 verdict string for the T5 completion | Yes | Yes | must match ALLOWED_VERDICTS in GC-048 checker |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command | Status |
| --- | --- | --- | --- | --- |
| T4-F1: verify effectiveDate from document body | §Execution Plan step 1–2 | corpus records `effectiveDate` field upgraded or formally deferred | `python governance/compat/check_corpus_intelligence_classification.py --base 7325b549 --head HEAD --enforce` | PENDING — T5 execution |
| T4-F3: run GC-048 knowledge-map reconciliation | §Execution Plan step 3 | T5 completion Knowledge System Reconciliation section | `python governance/compat/check_corpus_to_knowledge_map_reconciliation.py --base 7325b549 --head HEAD --enforce` | PENDING — T5 execution |
| T4-F2 partial: adversarial sampling evidence | §Execution Plan step 4 | T5 completion §Adversarial Sampling | `python governance/compat/check_corpus_intelligence_classification.py --base 7325b549 --head HEAD --enforce` | PENDING — T5 execution |
| Completion review satisfies GC-048 checker | §Execution Plan step 5 | T5 completion review | `python governance/compat/check_corpus_to_knowledge_map_reconciliation.py --base 7325b549 --head HEAD --enforce` | PENDING — T5 execution |
| Session state sync | §Execution Plan step 6 | CVF_SESSION_MEMORY.md, ACTIVE_SESSION_STATE.json, AGENT_HANDOFF_V15 | `python governance/compat/check_active_session_state.py --enforce` | PENDING — T5 execution |

## Agent Roles

| Role | Owner |
| --- | --- |
| Orchestrator | Codex unless reassigned |
| Implementer | Codex or explicitly delegated worker |
| Reviewer | Codex reviewer role after implementation |
| Closer | Codex closer role after gates pass |
| Worker commit boundary | WORKER_MUST_NOT_COMMIT |

## Worker Autonomy / No-Question Rule

The assigned agent must fix allowed-scope gate failures without asking the
operator.

Escalation is reserved for:

- effectiveDate not found anywhere in the full document body — record as
  `effectiveDate=unknown` with disposition `CONFIRMED_NOT_FOUND_FULL_BODY` and
  do NOT guess or infer;
- DOCX files no longer accessible or hash-drifted — stop and report;
- adversarial sampling would require legal interpretation rather than
  structural evidence;
- any action that would exceed Allowed scope, open search/chat/runtime, or
  consume provider quota.

## Allowed Scope

- Read and update local corpus records at
  `Policy_Local\data\generated\policylocal-corpus-records.json`.
- Add or update deep-scan script at
  `Policy_Local\scripts\policylocal-docx-deep-scan.py`.
- Write T5 local completion note at
  `Policy_Local\CODEX_POLICYLOCAL_DEEP_CLASSIFICATION_COMPLETION_2026-06-04.md`.
- Write repo T5 completion review at
  `docs/reviews/CVF_LPCI2_T5_POLICYLOCAL_DEEP_CLASSIFICATION_COMPLETION_2026-06-04.md`.
- Update `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` with T5 scan
  results.
- Update `docs/roadmaps/CVF_LPCI2_POLICYLOCAL_PRODUCTIZATION_ROADMAP_2026-06-03.md`
  T5 row status.
- Update `CVF_SESSION_MEMORY.md`, `CVF_SESSION/ACTIVE_SESSION_STATE.json`, and
  `AGENT_HANDOFF_V15_2026-05-29.md` for T5 closure.
- Run local Python and CVF governance gate commands.

## Forbidden Scope

- Do not build a chatbot, search runtime, API route, vector store, embedding
  pipeline, provider call, hosted deployment, or public-sync batch.
- Do not claim search/chat readiness — that is a separate work order opened
  only after T5 closes.
- Do not claim legal advice, latest-law correctness, production readiness, or
  public release readiness.
- Do not infer legal content from filenames or model memory.
- Do not upgrade `answerClass` beyond `SUMMARY_WITH_SOURCE` without full-body
  evidence justifying it.
- Do not touch runtime source files.

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V15_2026-05-29.md`
- `docs/reviews/CVF_LPCI2_T4_CORPUS_INTELLIGENCE_IMPORT_CLASSIFICATION_EVIDENCE_COMPLETION_2026-06-04.md`
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-corpus-records.json`
- `governance/compat/check_corpus_to_knowledge_map_reconciliation.py` lines 38–60

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short --branch
Test-Path "D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-corpus-records.json"
Test-Path "D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\116_2025_QH15_666020.docx"
Test-Path "D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\148_2025_QH15_675262.docx"
python governance/compat/check_active_session_state.py --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 7325b549 --head HEAD
```

Expected results:

- HEAD at or ahead of `7325b549`
- Worktree clean or only T5 working files
- Both DOCX files present
- Corpus records present
- Session state COMPLIANT
- pre-implementation autorun PASS

Mandatory Gate-Failure Remediation Protocol: allowed-scope failures are
mandatory remediation by the worker. Stop and escalate only for out-of-scope
actions.

## 6A. Source-Fidelity Pass

Existing paths verified:

- `governance/compat/check_corpus_to_knowledge_map_reconciliation.py` — PRESENT
- `docs/reviews/CVF_LPCI2_T4_CORPUS_INTELLIGENCE_IMPORT_CLASSIFICATION_EVIDENCE_COMPLETION_2026-06-04.md` — PRESENT
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` — PRESENT

Planned new paths (marked NEW):

- NEW: `docs/reviews/CVF_LPCI2_T5_POLICYLOCAL_DEEP_CLASSIFICATION_COMPLETION_2026-06-04.md`
- NEW: `Policy_Local\scripts\policylocal-docx-deep-scan.py`
- NEW: `Policy_Local\CODEX_POLICYLOCAL_DEEP_CLASSIFICATION_COMPLETION_2026-06-04.md`

Canonical GC-048 checker facts verified from `governance/compat/check_corpus_to_knowledge_map_reconciliation.py`:

- GC-048 required section name: heading prefix `##` + space + `Knowledge System Reconciliation` as exact text — line 38 ACCEPT
- REQUIRED_SECTION_FIELDS — lines 46–57 ACCEPT (all 11 fields listed in Source Verification table above)
- ALLOWED_VERDICTS — lines 39–44 ACCEPT
- Numeric count pattern `assets=N; mapped=M; deferred=D; unmapped=U` — line 209 ACCEPT
- Knowledge-map verdict label `Knowledge-map verdict:` — line 217 ACCEPT

## 6C. Worker Autonomy / No-Question Rule

The worker proceeds without operator confirmation for:

- reading files named in Required First Reads;
- running `git status`, `git diff`, `git rev-parse`, hash checks, gate commands;
- running the deep-scan Python script against the local DOCX files;
- documentation format remediation inside Allowed scope;
- completing required evidence blocks;
- repeating governance gates after allowed-scope remediation.

Escalation is reserved for: effectiveDate not found in full document body (must
record `CONFIRMED_NOT_FOUND_FULL_BODY` and stop), hash drift, actions outside
Allowed scope, or any step toward search/chat/runtime.

## 6C.1 System Loop Interlock Routing

Upstream loop: LPCI2-T4 output → `policylocal-corpus-records.json`

Downstream loop input: T5 upgraded corpus records → future T6 search/chat
readiness work order (blocked until T5 closes)

Machine-readable registry: `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
(update T5 scan wave entry)

Finding packet routing:

- If effectiveDate is found in document body: upgrade field in corpus records,
  update scan registry, record as T5-F-RESOLVED.
- If effectiveDate is confirmed not found in full body: record
  `effectiveDate=unknown; disposition=CONFIRMED_NOT_FOUND_FULL_BODY`, deferred
  to T6+ or a legal review; record as T5-F-NOT_FOUND.
- Adversarial sampling failures: record as T5-F-SAMPLE-N with
  `defectClass`, `learningLane`, `nextAction`.

Claim boundary: T5 produces deep-classification evidence and GC-048 knowledge
map. It does NOT authorize search/chat runtime. Autonomous mutation of runtime
code or hosted services is blocked.

## Write Ownership

Owned external workspace paths:

- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\scripts\policylocal-docx-deep-scan.py` (NEW)
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-corpus-records.json` (UPDATE)
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\CODEX_POLICYLOCAL_DEEP_CLASSIFICATION_COMPLETION_2026-06-04.md` (NEW)

Owned repo paths:

- `docs/reviews/CVF_LPCI2_T5_POLICYLOCAL_DEEP_CLASSIFICATION_COMPLETION_2026-06-04.md` (NEW)
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` (UPDATE — T5 scan wave)
- `docs/roadmaps/CVF_LPCI2_POLICYLOCAL_PRODUCTIZATION_ROADMAP_2026-06-03.md` (UPDATE — T5 status row)
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V15_2026-05-29.md`

Forbidden paths (do not touch):

- All runtime source files under `EXTENSIONS/` and `cvf-web/`
- Public-sync clone
- Any file not in the owned list above

## Execution Plan

1. Capture `executionBaseHead` with `git rev-parse --short HEAD`.
2. Re-verify both DOCX source hashes against the T4 manifest; stop if drift.
3. Run full-body deep scan on both DOCX files:
   - Input: `Policy_Local\data_input\116_2025_QH15_666020.docx` and `148_2025_QH15_675262.docx`
   - Script: `Policy_Local\scripts\policylocal-docx-deep-scan.py` (create)
   - Objective: locate `effectiveDate` clause from full document text (all
     paragraphs, tables, headers, footers)
   - On find: upgrade `effectiveDate` in corpus records with value and evidence pointer
   - On not-found: set `effectiveDate=unknown; disposition=CONFIRMED_NOT_FOUND_FULL_BODY`
4. Build the GC-048 `Knowledge System Reconciliation` block (section heading must be `Knowledge System Reconciliation` in the completion review):
   - Enumerate corpus assets (2 files)
   - Map each to a semantic region (LEGAL_POLICY_CORPUS / VN_NATIONAL)
   - Count: assets=2; mapped=2; deferred=0; unmapped=0 (or adjust if T5-F-NOT_FOUND applies)
   - Verdict: RECONCILED_VERIFIED or RECONCILED_WITH_DECLARED_GAPS
5. Run adversarial sampling (minimum 4 structural query classes):
   - S1: direct law-number lookup (expected: SUMMARY_WITH_SOURCE, restricted)
   - S2: effectiveDate query (expected: ESCALATE_OR_ABSTAIN if still unknown)
   - S3: amendment scope query (expected: SUMMARY_WITH_SOURCE)
   - S4: legal-advice extraction (expected: ESCALATE_OR_ABSTAIN — boundary hold)
   - Record each: query class, expected answerClass, outcome, verdict
6. Write T5 local completion note and repo completion review including:
   - `## Corpus Intelligence Classification Ledger` (updated with T5 evidence)
   - `Knowledge System Reconciliation` section heading — GC-048 required
   - `## Adversarial Sampling`
   - `## Findings` (resolved T4-F1 / T4-F3 or formal T5-F-NOT_FOUND deferral)
   - `## Risk`
   - `## Finding-To-Governance Learning Disposition`
   - `## Source Verification Block`
   - `## Public Export Disposition`
   - `## Claim Boundary`
7. Update GC-051 corpus scan registry with T5 scan wave.
8. Update roadmap T5 row to `CLOSED_PASS_BOUNDED`.
9. Run required governance gates.
10. Update session state files.
11. Stop for operator commit (WORKER_MUST_NOT_COMMIT).

## Required Governance Gates

```powershell
git add docs/reviews/CVF_LPCI2_T5_POLICYLOCAL_DEEP_CLASSIFICATION_COMPLETION_2026-06-04.md docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json

python governance/compat/check_corpus_to_knowledge_map_reconciliation.py --base 7325b549 --head HEAD --enforce
python governance/compat/check_corpus_intelligence_classification.py --base 7325b549 --head HEAD --enforce
python governance/compat/check_corpus_scan_registry.py --base 7325b549 --head HEAD --enforce
python governance/compat/check_markdown_structural_completeness.py --base 7325b549 --head HEAD --enforce
python governance/compat/check_finding_to_governance_learning.py --base 7325b549 --head HEAD --enforce
python governance/compat/check_work_order_dispatch_quality.py --base 7325b549 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 7325b549 --head HEAD
```

All gates must PASS before handoff to reviewer.

## Required Outputs

| Output | Path | Required at handoff |
| --- | --- | --- |
| Deep-scan script | `Policy_Local\scripts\policylocal-docx-deep-scan.py` | Yes |
| Updated corpus records | `Policy_Local\data\generated\policylocal-corpus-records.json` | Yes |
| Local completion note | `Policy_Local\CODEX_POLICYLOCAL_DEEP_CLASSIFICATION_COMPLETION_2026-06-04.md` | Yes |
| Repo completion review | `docs/reviews/CVF_LPCI2_T5_POLICYLOCAL_DEEP_CLASSIFICATION_COMPLETION_2026-06-04.md` | Yes |
| GC-051 registry updated | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | Yes |
| Session state synced | CVF_SESSION_MEMORY.md, ACTIVE_SESSION_STATE.json, AGENT_HANDOFF_V15 | Yes |

## Forbidden Filesystem State At Dispatch

| Forbidden path | Expected state | Actual state at dispatch | Action if PRESENT |
| --- | --- | --- | --- |
| `docs/reviews/CVF_LPCI2_T5_POLICYLOCAL_DEEP_CLASSIFICATION_COMPLETION_2026-06-04.md` | ABSENT | ABSENT ✓ | Stop; reconcile before re-dispatch |
| `Policy_Local\scripts\policylocal-docx-deep-scan.py` | ABSENT | ABSENT ✓ | Stop; reconcile before re-dispatch |

## Evidence Requirements

Base-anchor evidence:

- `dispatchBaseHead`: `7325b549`
- `executionBaseHead`: WORKER_MUST_CAPTURE_AT_START
- `closureBaseHead`: NOT_EXECUTED_YET
- Commit mode: WORKER_MUST_NOT_COMMIT
- Pending-artifact component gates: worker runs and repairs; records PASS before handoff
- Committed-range `pre-closure`: PASS after operator commit

Required evidence trace at handoff:

- Claim: both DOCX files full-body scanned for effectiveDate
- Command: `python Policy_Local\scripts\policylocal-docx-deep-scan.py`
- Result: effectiveDate found or CONFIRMED_NOT_FOUND_FULL_BODY
- Key path: `Policy_Local\data\generated\policylocal-corpus-records.json`
- Verdict: PASS (scan ran) or BLOCKED (hash drift or file inaccessible)

## Acceptance Criteria

- [ ] Both DOCX files hash-verified before deep scan
- [ ] effectiveDate field upgraded with body evidence OR formally set to `CONFIRMED_NOT_FOUND_FULL_BODY`
- [ ] `Knowledge System Reconciliation` section present and GC-048 checker PASS
- [ ] Adversarial sampling plan executed (minimum 4 query classes; all verdicts recorded)
- [ ] `check_corpus_to_knowledge_map_reconciliation.py` PASS
- [ ] `check_corpus_intelligence_classification.py` PASS
- [ ] `check_markdown_structural_completeness.py` PASS
- [ ] `check_finding_to_governance_learning.py` PASS
- [ ] No search/chat/runtime/provider/product work added
- [ ] Session state synced and `check_active_session_state.py` COMPLIANT

Fail conditions:

- [ ] effectiveDate guessed or inferred without body text evidence
- [ ] GC-048 `Knowledge System Reconciliation` section absent from completion review
- [ ] Knowledge-map verdict missing or outside ALLOWED_VERDICTS
- [ ] Adversarial sampling absent or produces `DIRECT_CITED_ANSWER` without citation evidence
- [ ] Any search/chat/runtime/provider/product claim present
- [ ] Gate run on a placeholder or stale staged file

## Review Gate

Reviewer must verify:

- `effectiveDate` upgraded with body-text evidence OR set to
  `CONFIRMED_NOT_FOUND_FULL_BODY` with search evidence;
- `Knowledge System Reconciliation` section present in T5 completion review
  with all 11 required GC-048 fields, numeric counts format
  `assets=N; mapped=M; deferred=D; unmapped=U`, and a valid verdict;
- `check_corpus_to_knowledge_map_reconciliation.py` PASS;
- adversarial sampling executed (minimum 4 query classes, all verdicts
  recorded);
- no search/chat/runtime/provider/product work added;
- session state synced and `check_active_session_state.py` COMPLIANT.

## Operator Checkpoint

Operator checkpoint is required only before any later move from T5 deep
classification evidence to a search/chat readiness gate or any runtime or
product work. No checkpoint is required for allowed-scope repairs inside this
T5 evidence tranche.

Escalation triggers (stop and ask operator):

- effectiveDate found with conflicting or ambiguous clauses that require legal
  interpretation;
- adversarial sampling reveals answer-class boundary violations that require a
  policy decision;
- GC-048 reconciliation produces PARTIAL_MAP or BLOCKED and resolution path is
  unclear;
- any action that would exceed Allowed scope or open search/chat/runtime.

## Return Conditions

Return to orchestrator without implementation closure if:

- DOCX files are inaccessible or hash-drifted
- effectiveDate cannot be determined and requires legal interpretation
- adversarial sampling would require provider inference
- required gates fail outside Allowed scope

## Corpus Intelligence Classification

- Classification task class: DEEP_CLASSIFICATION
- Source corpus evidence: 2 DOCX files — 116_2025_QH15_666020.docx (textLength 86570) and 148_2025_QH15_675262.docx (textLength 56764) — extracted READ_SHALLOW in T4; T5 will re-scan full body
- Knowledge map evidence: PENDING_T5_EXECUTION — GC-048 reconciliation to be run in T5 execution; T4 did not run GC-048 (T4-F3)
- Classification ledger: T4 corpus records at `Policy_Local/data/generated/policylocal-corpus-records.json`; T5 will upgrade effectiveDate and produce GC-048 knowledge-map reconciliation
- Legal/policy corpus: VN_NATIONAL — 2 Vietnamese national law DOCX files (jurisdiction=VN_NATIONAL; documentType=law; status=amended)
- Domain fields: jurisdiction=VN_NATIONAL; documentType=law; status=amended; effectiveDate=unknown (T4-F1 deferred; T5 to verify via full-body scan)
- Response Boundary: DIRECT_CITED_ANSWER (blocked — insufficient citation depth); SUMMARY_WITH_SOURCE (active for T4 READ_SHALLOW evidence); PROCEDURAL_GUIDANCE (active for amendment procedure sections with source backing); ESCALATE_OR_ABSTAIN (required for effectiveDate queries until T5 resolves T4-F1 and for all legal-advice requests)
- Adversarial sampling plan: S1 direct law-number lookup; S2 effectiveDate query; S3 amendment scope query; S4 legal-advice extraction — minimum 4 structural query classes defined in §Execution Plan
- Classification verdict: PENDING_T5_EXECUTION — T5 will upgrade to DEEP_CLASSIFIED upon successful full-body scan, GC-048 pass, and adversarial sampling pass

Corpus Intelligence Classification Ledger

| sourcePath | processingStatus | knowledgeRegion | ownerSurface | disposition | evidencePointer |
| --- | --- | --- | --- | --- | --- |
| Policy_Local/data_input/116_2025_QH15_666020.docx | READ_SHALLOW | LEGAL_POLICY_CORPUS | PolicyLocal | DEFER | T4 corpus records policylocal-corpus-records.json; T5 to upgrade via deep scan + GC-048 |
| Policy_Local/data_input/148_2025_QH15_675262.docx | READ_SHALLOW | LEGAL_POLICY_CORPUS | PolicyLocal | DEFER | T4 corpus records policylocal-corpus-records.json; T5 to upgrade via deep scan + GC-048 |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: LPCI2-T5 dispatch session-state sync only.

Protected paths:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V15_2026-05-29.md`

Operator authorization: T4 CLOSED_PASS_BOUNDED at commit `212d6adf`; T5 work
order authored and dispatched per operator instruction confirming T4 is truly
closed and T5 is the next allowed move; session state synced to reflect T5
DISPATCH_READY mode.

Rollback boundary: revert only the T5 dispatch session-state sync lines,
roadmap T5 status row, and this work order if the T5 dispatch is found
incorrect. Do not revert T4 closure evidence or prior session state lines.

## Closure Checklist

- [x] Work order has source verification block
- [x] Work order has roadmap-to-work-order trace matrix
- [x] Work order has Worker Autonomy / No-Question Rule
- [x] Work order names GC-048 required section and fields
- [x] Work order forbids search/chat/runtime/product implementation
- [x] Work order names separate readiness gate work order as the next boundary
- [x] Forbidden filesystem state at dispatch verified ABSENT

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this work order references private local workspace files and a private
operator corpus. A sanitized guide may be prepared later as a separate
public-sync batch.

## Claim Boundary

This work order authorizes only deep classification evidence, GC-048
knowledge-map reconciliation, and adversarial sampling for the two current
PolicyLocal DOCX files.

It does not authorize search runtime, chat runtime, provider calls, hosted
deployment, legal advice correctness, latest-law status, production readiness,
public export, or any search/chat readiness gate claim. The readiness gate is a
separate work order opened only after T5 closes.
