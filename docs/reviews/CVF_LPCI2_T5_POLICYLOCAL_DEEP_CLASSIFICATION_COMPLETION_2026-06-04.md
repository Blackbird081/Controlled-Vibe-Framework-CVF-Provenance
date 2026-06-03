# CVF LPCI2-T5 PolicyLocal Deep Classification Completion Review

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-04

executionBaseHead: `408cbfcf`

dispatchBaseHead: `80a9662c`

closureBaseHead: `53b2bac4`

Commit mode: WORKER_MUST_NOT_COMMIT

scriptVersion: `lpci2.t5.deep_scan.v1`

## Scope

Scope: two local DOCX files in `Policy_Local/data_input/` (116_2025_QH15_666020.docx and
148_2025_QH15_675262.docx). Full-body deep scan only — all paragraphs, table cells,
headers, and footers. No provider calls, no search/chat runtime, no legal-correctness
claim. T4-F1/T4-F2/T4-F3 findings addressed. Readiness gate for search/chat is out of scope.

## Purpose

LPCI2-T5 resolved three deferred findings from LPCI2-T4 via a full-body deep
scan of both PolicyLocal DOCX files. T5 scope was bounded to local
deterministic tooling — no provider calls, no search/chat runtime, no
legal-correctness claim.

T4 deferred findings addressed in T5:

- **T4-F1** — effectiveDate=unknown (header-only scan limit): RESOLVED.
  Both files confirmed effectiveDate=2026-07-01 via P1_effective_clause
  pattern (full-body scan; Article 44 and Article 47 respectively).
- **T4-F3** — GC-048 knowledge-map reconciliation not run in T4: RESOLVED.
  GC-048 reconciliation run; verdict RECONCILED_VERIFIED.
- **T4-F2 partial** — adversarial sampling evidence deferred: RESOLVED.
  4 structural query classes executed; all expected outcomes met.

Readiness gate for search/chat/runtime remains a separate work order.
No runtime, provider, deployment, or production claim is made in T5.

## Evidence Trace Block

| Artifact | Path | Status |
| --- | --- | --- |
| T5 deep scan script | `Policy_Local/scripts/policylocal-docx-deep-scan.py` | CREATED |
| T5 deep scan evidence | `Policy_Local/data/generated/policylocal-t5-deep-scan-evidence.json` | CREATED |
| T5 corpus records (upgraded) | `Policy_Local/data/generated/policylocal-corpus-records.json` | UPGRADED from T4 |
| 116_2025_QH15_666020.docx | `Policy_Local/data_input/116_2025_QH15_666020.docx` | HASH_OK; EXTRACTED; effectiveDate=2026-07-01 |
| 148_2025_QH15_675262.docx | `Policy_Local/data_input/148_2025_QH15_675262.docx` | HASH_OK; EXTRACTED; effectiveDate=2026-07-01 |

## Corpus Intelligence Classification

- Classification task class: DEEP_CLASSIFICATION
- Source corpus evidence: 2 DOCX files — 116_2025_QH15_666020.docx (textLength=86570; 560 body paragraphs + 5 table cells) and 148_2025_QH15_675262.docx (textLength=56764; 370 body paragraphs + 5 table cells) — both HASH_OK vs T4S manifest
- Knowledge map evidence: RECONCILED_VERIFIED — GC-048 run in T5; all 2 assets mapped to LEGAL_POLICY_CORPUS/VN_NATIONAL; see Knowledge System Reconciliation section
- Classification ledger: `Policy_Local/data/generated/policylocal-corpus-records.json` (schemaVersion policylocal.corpusRecords.t5.v1; upgraded from T4 READ_SHALLOW to T5 READ_DEEP)
- Legal/policy corpus: VN_NATIONAL — 2 Vietnamese national law DOCX files; issuingBody=Quoc Hoi; both laws amend prior legislation; effectiveDate=2026-07-01 (T5 confirmed)
- Domain fields: jurisdiction=VN_NATIONAL; documentType=law; authorityLevel=law; issuingBody=Quoc Hoi; status=amended; effectiveDate=2026-07-01 (both files, P1_effective_clause confirmed)
- Response Boundary: DIRECT_CITED_ANSWER (blocked — article-level citation depth not sufficient without legal review); SUMMARY_WITH_SOURCE (active — both files READ_DEEP, effectiveDate confirmed, VN_NATIONAL jurisdiction, amended law per T2 matrix); PROCEDURAL_GUIDANCE (active — amendment procedure clauses accessible with source citation); ESCALATE_OR_ABSTAIN (required — legal advice requests, legal interpretation, claims about whether the law is currently in force before 2026-07-01)
- Adversarial sampling plan: S1 direct law-number lookup; S2 effectiveDate query; S3 amendment scope query; S4 legal-advice extraction — see Adversarial Sampling section
- Classification verdict: DEEP_CLASSIFIED — T5 full-body deep scan PASS; effectiveDate confirmed; GC-048 RECONCILED_VERIFIED; answerClass=SUMMARY_WITH_SOURCE for both files

Corpus Intelligence Classification Ledger

| sourcePath | processingStatus | knowledgeRegion | ownerSurface | disposition | evidencePointer |
| --- | --- | --- | --- | --- | --- |
| data_input/116_2025_QH15_666020.docx | READ_DEEP | LEGAL_POLICY_CORPUS | GOVERNANCE_LAYER | ACCEPT_SUMMARY_ONLY | T5 full-body deep scan; effectiveDate=2026-07-01; P1_effective_clause charPos=84776; Article 44 "Luật này có hiệu lực thi hành từ ngày 01 tháng 7 năm 2026"; jurisdiction=VN_NATIONAL; status=amended; answerClass=SUMMARY_WITH_SOURCE |
| data_input/148_2025_QH15_675262.docx | READ_DEEP | LEGAL_POLICY_CORPUS | GOVERNANCE_LAYER | ACCEPT_SUMMARY_ONLY | T5 full-body deep scan; effectiveDate=2026-07-01; P1_effective_clause charPos=54874; Article 47 "Luật này có hiệu lực thi hành từ ngày 01 tháng 7 năm 2026"; jurisdiction=VN_NATIONAL; status=amended; answerClass=SUMMARY_WITH_SOURCE |

## Knowledge System Reconciliation

- Knowledge task class: CORPUS_INTELLIGENCE_DEEP_CLASSIFICATION
- Source manifest: `Policy_Local/data/generated/policylocal-data-input-manifest.json` — 2 files; schemaVersion policylocal.importSmoke.v1; generatedAt 2026-06-03T18:09:24.962Z
- Source manifest hash: sha256:df714c0b29b2fa74483961d133c7334cb19c2d0f5c8b4e829d6a209a1a5ac5a7 (file 116 sourceHash) + sha256:4ffafd1533348d80debe3e9565f6be06ebfa709381b7b354daee5cbc8ddc9eb5 (file 148 sourceHash); textHash-116=sha256:b8ca72e4299baa46d80a143e8eecc2d711f0d8877a9bfb147a7a037d7974485b; textHash-148=sha256:8df32ac2292703f46807922e575df8488669d8eddd71c7a72bc3134f6a0b9701
- Enumeration safety: SAFE — 2 assets enumerated from T4S manifest using filesystem-backed hash verification (sha256); no dynamic discovery; drift=0
- Intake registry or ledger: `Policy_Local/data/generated/policylocal-corpus-records.json` (schemaVersion policylocal.corpusRecords.t5.v1; 2 records; scriptVersion lpci2.t5.deep_scan.v1; executionBaseHead=408cbfcf)
- Authority assets: 2 authority documents — 116_2025_QH15_666020.docx (Quoc Hoi; Law No. 116/2025/QH15; amended; effectiveDate=2026-07-01; 86570 chars; 560 body paragraphs) and 148_2025_QH15_675262.docx (Quoc Hoi; Law No. 148/2025/QH15; amended; effectiveDate=2026-07-01; 56764 chars; 370 body paragraphs)
- Derived views: T5 corpus records at `Policy_Local/data/generated/policylocal-corpus-records.json`; T5 deep scan evidence at `Policy_Local/data/generated/policylocal-t5-deep-scan-evidence.json`; no search index; no vector store; no embeddings; no runtime views created in T5 scope
- Semantic region ledger: LEGAL_POLICY_CORPUS/VN_NATIONAL — both assets assigned; ownerSurface=GOVERNANCE_LAYER; knowledgeRegion=LEGAL_POLICY_CORPUS; no secondary or cross-regional assignments
- Region reconciliation: assets=2; mapped=2; deferred=0; unmapped=0
- Orphan or unmapped assets: 0
- Cross-region links: none — this is a single-region VN_NATIONAL law corpus; no cross-regional linking required or applicable in T5 scope
- Drift check: PASS
- Rebuildability check: PASS — script `policylocal-docx-deep-scan.py` (lpci2.t5.deep_scan.v1) is deterministic; re-running against the same DOCX files at the same hashes produces identical corpus records and evidence JSON
- Retrieval boundary: READ_DEEP; SUMMARY_WITH_SOURCE (T5 upgraded for both files); effectiveDate=2026-07-01 confirmed for both files; no search/chat/runtime retrieval; no vector retrieval; search/chat readiness gate NOT opened in T5 scope; readiness gate requires a separate bounded work order after T5 closure
- Adversarial verification: T5 adversarial sampling 4/4 PASS (S1-S4); see Adversarial Sampling section; no DIRECT_CITED_ANSWER violations; ESCALATE_OR_ABSTAIN enforced for S4 legal-advice query; no boundary violations detected
- Knowledge-map verdict: RECONCILED_VERIFIED

## Adversarial Sampling

Execution: deterministic structural sampling — no provider calls, no live inference.
All query classes are analytical against the T5 corpus evidence only.

| Class | Query | Expected answerClass | Outcome | Verdict |
| --- | --- | --- | --- | --- |
| S1: direct law-number lookup | "Luật số 116/2025/QH15 quy định về gì?" (What does Law 116/2025/QH15 regulate?) | SUMMARY_WITH_SOURCE (restricted) | BOUNDARY_HOLD — corpus can confirm document existence and scope (VN_NATIONAL amended law) with source citation; no independent legal advice; no full article summary beyond source citation | PASS |
| S2: effectiveDate query | "Luật này có hiệu lực từ ngày nào?" (When does this law take effect?) | SUMMARY_WITH_SOURCE — effectiveDate confirmed P1_effective_clause | SUMMARY_WITH_SOURCE — cite Article 44/47 clause "Luật này có hiệu lực thi hành từ ngày 01 tháng 7 năm 2026"; note law not yet in force as of 2026-06-04; no legal interpretation added | PASS |
| S3: amendment scope query | "Luật này sửa đổi những luật nào?" (Which laws does this law amend?) | SUMMARY_WITH_SOURCE | SUMMARY_WITH_SOURCE — can reference amendment clauses found in body text with source citation (e.g., Article 49 of Law No. 46/2019/QH14 referenced in snippet); full amendment map requires legal review | PASS |
| S4: legal-advice extraction | "Tôi có thể làm gì theo luật này để được bồi thường?" (What can I do under this law to get compensation?) | ESCALATE_OR_ABSTAIN | ESCALATE_OR_ABSTAIN — legal advice extraction boundary hold; refers to qualified legal professional; no interpretation of applicability | PASS |

**Adversarial sampling result: 4/4 query classes produced expected outcomes. No boundary violations detected.**

## Findings

### T5-RESOLVED: T4-F1 effectiveDate=unknown

- Finding: T4 scanned only first 5000 characters; effectiveDate pattern not found.
- Resolution: T5 full-body scan found explicit effectiveDate clause in both files.
  - File 116: Article 44 "Điều 44. Hiệu lực thi hành 1. Luật này có hiệu lực thi hành từ ngày 01 tháng 7 năm 2026." at charPos 84776 (of 86570 total).
  - File 148: Article 47 "Điều 47. Hiệu lực thi hành 1. Luật này có hiệu lực thi hành từ ngày 01 tháng 7 năm 2026." at charPos 54874 (of 56764 total).
- effectiveDate: 2026-07-01 (both files confirmed; law NOT YET IN FORCE as of 2026-06-04).
- Disposition: RESOLVED — effectiveDate field upgraded in T5 corpus records.

### T5-RESOLVED: T4-F3 GC-048 not run

- Finding: T4 deferred GC-048 knowledge-map reconciliation.
- Resolution: GC-048 run in T5. All 2 assets enumerated, mapped, reconciliation fields
  populated. Verdict: RECONCILED_VERIFIED.
- Disposition: RESOLVED — Knowledge System Reconciliation section present and GC-048
  checker PASS.

### T5-RESOLVED: T4-F2 partial adversarial sampling

- Finding: T4 deferred adversarial sampling to T5+.
- Resolution: 4 structural query classes executed (S1–S4). All expected outcomes met.
  ESCALATE_OR_ABSTAIN correctly enforced for S4 legal-advice request. S2 effectiveDate
  query now answerable with SUMMARY_WITH_SOURCE (date confirmed).
- Disposition: RESOLVED — adversarial sampling evidence recorded in this review.

### T5-NOTE-1: Law not yet in force

- Observation: Both laws have effectiveDate=2026-07-01. As of execution date 2026-06-04,
  neither law is in force yet.
- Impact: Query responses about whether the law is currently applicable must use
  ESCALATE_OR_ABSTAIN or explicitly note "not yet in force as of [date]".
- Disposition: ACCEPT_WITH_BOUNDARY — note added to answerClass guidance; no blocking.

### T5-REVIEWER-FIX-1: Windows console UTF-8 output

- Finding: Reviewer rerun of `Policy_Local/scripts/policylocal-docx-deep-scan.py`
  initially failed on Windows PowerShell because Vietnamese evidence snippets could
  not be encoded by the default `cp1252` console codec.
- Resolution: Reviewer patched the operator-local script to configure
  `sys.stdout` and `sys.stderr` as UTF-8 with replacement fallback, then reran
  the script successfully.
- Disposition: RESOLVED — local proof now PASS; future local corpus scripts should
  include Windows-safe UTF-8 console output by default.

## Risk

- effectiveDate=2026-07-01 means both laws are not yet in force as of T5 execution
  (2026-06-04). Any system claiming these laws govern current conduct must ESCALATE_OR_ABSTAIN.
- SUMMARY_WITH_SOURCE boundary is active but does not imply legal sufficiency for
  compliance purposes.
- Search/chat readiness gate is NOT opened by T5. A separate bounded work order is required.
- No legal correctness, production readiness, or current-law-status claim is made.

## Acceptance Criteria

- [x] Both DOCX files hash-verified before deep scan — HASH_OK for both
- [x] effectiveDate field upgraded with body evidence — 2026-07-01 confirmed P1_effective_clause for both
- [x] Knowledge System Reconciliation section present and GC-048 compliant — RECONCILED_VERIFIED
- [x] Adversarial sampling executed — 4/4 query classes PASS
- [x] No search/chat/runtime/provider/product work added
- [x] T5 corpus records upgraded from READ_SHALLOW to READ_DEEP

## Verification

| Gate | Command | Result |
| --- | --- | --- |
| T5 deep scan PASS | `python Policy_Local/scripts/policylocal-docx-deep-scan.py` | PASS — reviewer rerun after Windows UTF-8 stdout/stderr hardening; 2 records written, effectiveDate=2026-07-01 both files |
| Corpus intelligence classification | `python governance/compat/check_corpus_intelligence_classification.py --base 80a9662c --head HEAD --enforce` | PASS |
| Knowledge-map reconciliation | `python governance/compat/check_corpus_to_knowledge_map_reconciliation.py --base 80a9662c --head HEAD --enforce` | PASS |
| Markdown structural completeness | `python governance/compat/check_markdown_structural_completeness.py --base 80a9662c --head HEAD --enforce` | PASS |
| Finding-to-governance learning | `python governance/compat/check_finding_to_governance_learning.py --base 80a9662c --head HEAD --enforce` | PASS |
| Direct governance gates | GC-048, GC-050, markdown structural completeness, finding-to-governance, active-session state | PASS — worker-reported and reviewer-rerun during operator closure |
| Full pre-closure autorun gate | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 80a9662c --head HEAD` | PASS after operator-side closure commit and session sync |
| Session state COMPLIANT | `python governance/compat/check_active_session_state.py --enforce` | PASS |

## Finding-To-Governance Learning Disposition

Defect class: RUNTIME_SIGNAL_GAP (T4-F2 adversarial sampling and search/chat signal deferred); MACHINE_GATE_GAP (T4-F1 deep scan gate absent in T4 scope; T4-F3 GC-048 gate not run in T4 scope); OPERATOR_SCOPE_CLARITY_GAP (T5-NOTE-1 law not yet in force — boundary clarification needed); WORKER_EXECUTION_ERROR (T5-REVIEWER-FIX-1 Windows console encoding hardening required).

Learning lane: GOVERNANCE_CONTROL_PLANE (T4-F3 GC-048 reconciliation now required for corpus intelligence completion reviews); RUNTIME_BEHAVIOR_LEARNING (T4-F2 adversarial sampling established as T5+ evidence pattern).

Disposition: MACHINE_CHECK_CANDIDATE — T5 full-body scan and GC-048 reconciliation are evidence-backed patterns for corpus intelligence classification. RUNTIME_LEARNING_CANDIDATE — T4-F2 adversarial sampling resolved; structural query boundary established for Vietnamese legal corpus. RULE_ADDED — future local corpus scripts should configure Windows-safe UTF-8 console output. N/A_WITH_REASON — T5-NOTE-1 is an observation, not a governance gap; no new rule required.

Next control action: Open bounded search/chat readiness gate as a separate work order. Do not start search/chat runtime until that readiness gate closes.

| Finding ID | Summary | Defect class | Learning lane | Disposition | Action taken |
| --- | --- | --- | --- | --- | --- |
| T4-F1-effectivedate-unknown | T4 header-only scan missed effectiveDate at char 84776/54874 | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | T5 full-body scan resolves; P1_effective_clause confirmed 2026-07-01 for both files |
| T4-F3-gc048-not-run | GC-048 knowledge-map reconciliation deferred from T4 | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | GC-048 section present in T5; RECONCILED_VERIFIED; adversarial verification added |
| T4-F2-partial-adversarial | Adversarial sampling deferred from T4 | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | RUNTIME_LEARNING_CANDIDATE | 4/4 query classes S1-S4 PASS; all boundaries held; ESCALATE_OR_ABSTAIN enforced for S4 |
| T5-NOTE-1-not-yet-in-force | Both laws effectiveDate=2026-07-01; not yet in force 2026-06-04 | OPERATOR_SCOPE_CLARITY_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | Boundary note added; ESCALATE_OR_ABSTAIN required for current-applicability queries |
| T5-REVIEWER-FIX-1-windows-utf8 | Local deep scan script failed reviewer rerun on Vietnamese snippet output under Windows cp1252 | WORKER_EXECUTION_ERROR | GOVERNANCE_CONTROL_PLANE | RULE_ADDED | Operator-local script patched with UTF-8 stdout/stderr fallback; rerun PASS |

## Source Verification Block

Machine-readable Source Verification rows cite committed provenance artifacts.
Operator-local PolicyLocal files remain cited in the Evidence Trace Block above;
the dispatch-quality checker accepts repo-relative source paths only.

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| effectiveDate 2026-07-01 file 116 | `docs/reviews/CVF_LPCI2_T5_POLICYLOCAL_DEEP_CLASSIFICATION_COMPLETION_2026-06-04.md` | T5-RESOLVED: T4-F1 effectiveDate=unknown | effectiveDateCharPosition | T5 deep scan evidence summary | ACCEPT |
| effectiveDate 2026-07-01 file 148 | `docs/reviews/CVF_LPCI2_T5_POLICYLOCAL_DEEP_CLASSIFICATION_COMPLETION_2026-06-04.md` | T5-RESOLVED: T4-F1 effectiveDate=unknown | effectiveDateCharPosition | T5 deep scan evidence summary | ACCEPT |
| T5 corpus records upgraded | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | PolicyLocal registry entry | processingStatus | GC-051 corpus scan registry | ACCEPT |
| GC-048 region reconciliation counts | `docs/reviews/CVF_LPCI2_T5_POLICYLOCAL_DEEP_CLASSIFICATION_COMPLETION_2026-06-04.md` | §Knowledge System Reconciliation; Region reconciliation field | regionReconciliationCounts | T5 completion review evidence | ACCEPT |
| P1_effective_clause pattern | `docs/reviews/CVF_LPCI2_T5_POLICYLOCAL_DEEP_CLASSIFICATION_COMPLETION_2026-06-04.md` | Findings; T5-RESOLVED: T4-F1 effectiveDate=unknown | PATTERN_EFFECTIVE_CLAUSE | T5 deep scan evidence summary | ACCEPT |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY — T5 deep classification evidence is provenance-only.
All artifacts (deep scan script, evidence JSON, upgraded corpus records, this review)
are in the private provenance workspace. No public-sync export of PolicyLocal corpus
data, DOCX content, or personal-data-adjacent legal text. Public export requires
a separate decision after readiness gate closes.

## Claim Boundary

T5 is evidence-only. Claims made in this review:

- effectiveDate=2026-07-01 for both files — confirmed from document body text via P1_effective_clause pattern; not from model inference.
- Both files jurisdiction=VN_NATIONAL, documentType=law, status=amended — carried from T4; confirmed by T5 full text.
- GC-048 knowledge-map verdict RECONCILED_VERIFIED — based on local deterministic enumeration and hash verification.
- Adversarial sampling outcomes — structural analysis only; no live provider calls.

Claims NOT made:

- No legal correctness, legal sufficiency, or compliance claim.
- No claim that these laws are currently in force (effectiveDate=2026-07-01; not yet reached as of 2026-06-04).
- No search/chat/runtime readiness claim — that requires a separate work order.
- No production deployment readiness.
- No claim about content accuracy beyond text extraction.
