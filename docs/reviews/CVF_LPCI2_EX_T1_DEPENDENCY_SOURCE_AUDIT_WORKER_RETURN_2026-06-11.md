# CVF LPCI2 EX-T1 Dependency Source Audit - Worker Return

Memory class: FULL_RECORD

Status: WORKER_RETURN_PENDING_REVIEW

docType: worker_return

Date: 2026-06-11

Worker: Claude

Reviewer: Codex

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `8b6bd04d`

executionBaseHead: `798eb17b`

Note: HEAD at worker execution start = `798eb17b`; HEAD at worker completion
= `76cdf464` (Codex committed public README workflow-map sync during worker
session).

---

## Purpose

Return Claude's EX-T1 dependency source audit packet: source-backed dependency
evidence, local feasibility probes, OCR language-code mapping, decision gate
answers, and recommendation for EX-T2 path selection.

---

## Scope / Target / Owner Boundary

Target:

- human-readable dependency audit report (docs/reference/);
- machine-readable JSON summary (docs/reference/);
- worker evidence packet (docs/reviews/).

Owner boundary:

- Worker owns only the three audit artifacts listed above.
- Codex owns handoff sync, active session state update, work order status
  conversion, reviewer-fast gate rerun after handoff sync, completion review,
  commit, and session continuity.
- No extractor implementation, repo dependency addition, OCR model download,
  corpus ingestion, EC-02 semantic change, public-sync, hosted/production
  readiness, or legal-quality claim is authorized or delivered.

---

## Pre-Flight Evidence

| Check | Command | Result |
| --- | --- | --- |
| executionBaseHead | `git rev-parse --short HEAD` (before edits) | `798eb17b` |
| Audit report absent | `Test-Path -LiteralPath docs/reference/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_REPORT_2026-06-11.md` | False (before worker edits) |
| JSON summary absent | `Test-Path -LiteralPath docs/reference/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_SUMMARY_2026-06-11.json` | False (before worker edits) |
| Worker return absent | `Test-Path -LiteralPath docs/reviews/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_WORKER_RETURN_2026-06-11.md` | False (before worker edits) |
| Pre-implementation gate | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 8b6bd04d --head HEAD` | COMPLIANT: pre-implementation autorun gate passed |

---

## Changed File List

`git status --short` result at worker completion (before worker return file created):

| Status | Path |
| --- | --- |
| ?? (new, untracked) | `docs/reference/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_REPORT_2026-06-11.md` |
| ?? (new, untracked) | `docs/reference/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_SUMMARY_2026-06-11.json` |
| ?? (new, untracked) | `docs/reviews/CVF_LPCI2_EX_T1_DEPENDENCY_SOURCE_AUDIT_WORKER_RETURN_2026-06-11.md` |

No forbidden paths modified. Confirmed: no runtime source tree, package
manifest, lockfile, corpus-intelligence, Policy_Local, or public-sync files
changed.

---

## Reviewer-Fast Gate

Command: `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast --serial`

**First run:** FAILED -- active session state check: handoff HEAD mismatch.
Active handoff `AGENT_HANDOFF_V17_2026-06-07.md` contains HEAD `37665acc`;
current HEAD = `76cdf464` (Codex committed public README workflow-map sync;
handoff was not updated between that commit and this worker execution).

**Repair attempted:** Non-ASCII violations (em-dashes) in audit report -- REPAIRED
(all em-dashes replaced with ASCII ` -- `; encoding gate now passes).

**Reviewer-fast blocker (active-session-state check):** The handoff HEAD sync
is Codex-owned. Worker cannot update `AGENT_HANDOFF_V17_2026-06-07.md` or
`CVF_SESSION/ACTIVE_SESSION_STATE.json` without exceeding WORKER_MUST_NOT_COMMIT
scope and forbidden-scope boundary. Per work order fail conditions: repair
requiring forbidden paths = return blocked diagnostic.

**Status:** BOUNDED_BLOCKER -- reviewer-fast requires Codex to sync handoff
HEAD to `76cdf464` before rerunning and confirming PASS.

**Repairs within allowed scope completed:**
- Non-ASCII encoding violations (em-dashes): ALL REPAIRED. Zero non-ASCII
  characters remain in any worker artifact.

---

## Local Probe Ledger

All probes run in-process or via pip --dry-run. No repo manifests modified.

| Probe | Command | Result |
| --- | --- | --- |
| pdfplumber installed version | `pip show pdfplumber` | 0.11.7; latest: 0.11.9 |
| pdfplumber import | `python -c "import pdfplumber; print(pdfplumber.__version__)"` | 0.11.7 PASS |
| python-docx installed version | `pip show python-docx` | 1.2.0 (latest) |
| python-docx import | `python -c "import docx; print('python-docx import OK')"` | PASS |
| pdf2image available | `pip index versions pdf2image` | 1.17.0 latest |
| pdf2image dry-run | `pip install pdf2image --dry-run` | Would install 1.17.0; Pillow already satisfied |
| easyocr available | `pip index versions easyocr` | 1.7.2 latest |
| easyocr dry-run | `pip install easyocr --dry-run` | Would install easyocr-1.7.2 + torch-2.12.0 + ~14 deps |
| poppler in PATH | `where.exe pdftoppm`, `where.exe pdfinfo` | NOT FOUND -- poppler absent from PATH |
| liteparse available | `pip index versions liteparse` | 2.0.7 latest; 12 versions on PyPI |
| liteparse dry-run | `pip install liteparse --dry-run` | Would install liteparse-2.0.7 only; 7.7MB single package |
| liteparse wheel download | `pip download liteparse --no-deps -d TEMP` | liteparse-2.0.7-cp311-cp311-win_amd64.whl 7.7MB; downloaded |
| liteparse wheel contents | zipfile inspection | pdfium.dll bundled; _liteparse.cp311-win_amd64.pyd; no Rust tool needed |
| liteparse license | wheel METADATA | MIT (Python wrapper); Apache-2.0 (Rust core, SBOM) |
| liteparse SBOM | wheel CycloneDX JSON | Apache-2.0 for liteparse, liteparse-pdfium, liteparse-pdfium-sys |
| liteparse .docx support | wheel METADATA README | requires LibreOffice |
| liteparse ocr_language format | wheel METADATA README | Tesseract code (3-letter ISO 639-2/T); `ocr_language="eng"` example |
| Rust toolchain | `rustc --version`, `cargo --version` | NOT FOUND -- Rust not installed on this machine |
| Pre-implementation gate | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 8b6bd04d --head HEAD` | COMPLIANT PASS |

---

## Source Citation List

| Source | URL or path | What it supports |
| --- | --- | --- |
| pdfplumber GitHub | https://github.com/jsvine/pdfplumber | License, format support, dependencies |
| python-docx GitHub | https://github.com/python-openxml/python-docx | License, .docx format only |
| pdf2image GitHub | https://github.com/Belval/pdf2image | poppler system dependency requirement |
| EasyOCR GitHub | https://github.com/JaidedAI/EasyOCR | vi and en language code confirmation; model download behavior |
| liteparse GitHub | https://github.com/run-llama/liteparse | Official source; format support; OCR language format |
| liteparse PyPI | https://pypi.org/project/liteparse/ | Version availability; Python requirement >= 3.10 |
| liteparse wheel METADATA | local: liteparse-2.0.7-cp311-cp311-win_amd64.whl | License classifiers; README; format support table; ocr_language example |
| liteparse wheel SBOM | local: liteparse-2.0.7.dist-info/sboms/liteparse-python.cyclonedx.json | Apache-2.0 for Rust core; PDFium wrapper; cargo-cyclonedx provenance |
| poppler freedesktop | https://poppler.freedesktop.org/ | Official poppler source |
| poppler-windows | https://github.com/oschwartz10612/poppler-windows | Windows binary distribution |
| Tesseract tessdata | Tesseract naming convention (eng/vie) | ISO 639-2/T code mapping for LiteParse |
| EasyOCR language list | EasyOCR README language table | vi->vi; en->en ISO 639-1 mapping |

---

## Candidate Recommendation

**Recommendation: COMPOSED_STACK_PREFERRED with LITEPARSE_ELIGIBLE_FOR_EX_T3_REEVALUATION**

**For EX-T2 (Tier 1 digital-native only):**

COMPOSED_STACK_PREFERRED.

- pdfplumber (0.11.7 installed; 0.11.9 latest): PASS -- import verified locally.
- python-docx (1.2.0 installed, latest): PASS -- import verified locally.
- No system dependencies for Tier 1. No OCR model download. No Rust toolchain.
- EX-T2 implements only digital-native extraction. EasyOCR and pdf2image
  (Tier 2) are scoped to EX-T3 and require a separate operator decision.

**For EX-T3 (Tier 2 OCR): operator decision required.**

Both options remain eligible:

- Option 1 EasyOCR: requires poppler + EasyOCR model download (~430MB). ISO 639-1
  codes (vi, en) match DSCP codes directly.
- Option 2 LiteParse Tesseract: prebuilt wheel (no Rust), but Tesseract must be
  installed system-wide + tessdata files downloaded per language. Requires a
  code-level OCR language mapping (vi -> vie, en -> eng).

EasyOCR model download size is the primary risk for CI and offline deployments.
LiteParse offers lighter per-language data files but adds Tesseract system dependency.

**Decision gate summary:**

| Gate | Answer |
| --- | --- |
| DG-1: CI Rust compilation required? | NO -- prebuilt wheels for liteparse 2.0.7 |
| DG-2: LibreOffice available? | NO on this machine; needed only for LiteParse .docx path |
| DG-3: poppler available? | NO in PATH on this machine; installable via apt-get (Linux) or manual (Windows) |
| DG-4: Offline/air-gap constraint? | High for EasyOCR; lower for LiteParse/Tesseract (pre-stageable tessdata) |
| DG-5: Spatial output near-term? | Operator decision required |

---

## Acceptance Criteria Coverage

| Criterion | Status |
| --- | --- |
| Report exists and covers all candidate dependencies named in the roadmap | PASS |
| JSON summary exists and mirrors the report verdicts | PASS |
| Every dependency claim is backed by primary-source or command evidence | PASS |
| Local install/import probes are recorded | PASS (pdfplumber + python-docx: import PASS; others: dry-run PASS or NOT_INSTALLED recorded) |
| OCR language-code mapping for `en` and `vi` is source-backed | PASS (EasyOCR: en->en, vi->vi; Tesseract: en->eng, vi->vie) |
| CI and Windows feasibility risks are explicit | PASS (poppler, EasyOCR size, Tesseract all flagged) |
| Recommendation is bounded to EX-T2 planning and does not claim runtime proof | PASS |
| No forbidden path is modified | PASS |

---

## Bounded Blocker

**Blocker class:** ACTIVE_SESSION_STATE_HANDOFF_HEAD_STALE

**Description:** reviewer-fast check `active session state compatibility` fails
because `AGENT_HANDOFF_V17_2026-06-07.md` contains HEAD `37665acc` but current
HEAD = `76cdf464`. Codex committed DSCP-T11F artifacts between the time the
HEAD = `76cdf464`. Codex committed public README workflow-map sync between the
time the handoff was last updated and this worker execution. The active handoff
and session state HEAD sync is Codex-owned (not in worker allowed scope).

**Action required by Codex:**
1. Update `AGENT_HANDOFF_V17_2026-06-07.md` HEAD block to `76cdf464` (or the
   commit SHA after Codex commits the worker artifacts).
2. Update `CVF_SESSION/ACTIVE_SESSION_STATE.json` accordingly.
3. Rerun reviewer-fast to confirm PASS before closure.

**Worker artifacts are clean:** All three owned artifact files pass encoding
gate (zero non-ASCII characters). No forbidden paths touched.

---

## Findings / Position

Position: `RETURNED_PASS_BOUNDED_WITH_REVIEWER_REMEDIATION`.

The worker artifacts are inside allowed scope and provide a bounded
dependency/source audit with a recommendation limited to EX-T2 Tier 1
digital-native extraction. Codex reviewer found two closure-readiness defects:
missing structural review headings in this worker return and stale active
handoff HEAD after an intervening public README workflow-map sync. Both are
reviewer-owned remediation items and do not change the dependency audit result.

---

## Risk / Corrective Action

| Risk | Disposition | Corrective action |
| --- | --- | --- |
| Worker return could be misread as final closure because reviewer-fast had a stale handoff blocker | MITIGATED_BY_REVIEWER | Codex must sync active handoff/session state before closure. |
| Missing structural headings block reviewer-fast | MITIGATED_BY_REVIEWER | Codex added required sections before commit. |
| EX-T1 recommendation could be mistaken for extractor runtime readiness | MITIGATED | Claim boundary limits recommendation to EX-T2 planning only. |

---

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| Reviewer-fast handoff HEAD mismatch occurred outside worker scope | ORCHESTRATOR_CONTINUITY_GAP | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS_MACHINE_CHECK_EXISTS | Existing active session compatibility gate caught it; Codex syncs continuity in closure. |
| Worker return initially missed structural headings | WORKER_EXECUTION_ERROR | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS_MACHINE_CHECK_EXISTS | Existing reviewer-fast structural checker caught it; Codex added required headings before commit. |
| Runtime/provider/cost words appear only inside claim-boundary exclusions | N/A_WITH_REASON | RUNTIME_BEHAVIOR_LEARNING; PROVIDER_OUTPUT_LEARNING; COST_ECONOMICS_LEARNING | NOT_A_FINDING | No runtime/provider/cost behavior was tested or claimed; no runtime/provider/cost control action applies. |

---

## New Doc-Only Fields (Confirmed Non-Runtime)

| Field | Artifact | Runtime claim? |
| --- | --- | --- |
| `dependencyCandidateId` | audit report + JSON | None |
| `primarySourceUrl` | audit report + JSON | None |
| `installProbeResult` | audit report + JSON | None |
| `importProbeResult` | audit report + JSON | None |
| `inputFormatFinding` | audit report + JSON | None |
| `ocrLanguageMappingFinding` | audit report + JSON | None |
| `ciFeasibilityVerdict` | audit report + JSON | None |

---

## Claim Boundary

This worker return covers dependency/source audit, temporary local feasibility
probes, OCR language-code mapping evidence, and a recommendation bounded to
EX-T2 planning only. It does not prove extraction runtime fitness, dependency
fitness for production, OCR quality, parser correctness, retrieval quality,
corpus ingestion, EC-02 runtime behavior, T12 eligibility, legal advice quality,
current-law status, provider behavior, hosted readiness, production readiness,
public readiness, public-sync, memory reinjection, high-risk promotion,
Learning Orchestrator runtime behavior, or autonomous mutation.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance worker return; not public-synced.
