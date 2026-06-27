# CVF Agent Work Order - LPCI2-T11B PolicyLocal Source Verification For Claude

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-07

dispatchBaseHead: `486370fe`

executionBaseHead: `08293726`

closureBaseHead: `08293726`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Codex execution override: `OPERATOR_AUTHORIZED_CODEX_WORKER_REVIEWER_CLOSURE`

Risk class: R1_LOCAL_VERIFICATION_ONLY

Worker: Claude, or Codex under explicit operator-authorized multi-role override

Reviewer / closer: Codex or operator-designated reviewer

completionReview: `docs/reviews/CVF_LPCI2_T11B_SOURCE_VERIFICATION_COMPLETION_2026-06-07.md`

## Purpose

Verify that every inventoried T11B target file resolves to a readable path,
that computed SHA-256 hashes match T11A manifest values, that observed file
sizes match T11A manifest sizes, that bundle artifact roles and lineage edges
reconcile with T11A manifest records, and that Unicode filename normalization
does not cause path resolution failures. Return uncommitted evidence packet to
Codex.

This implements the full four-gate scan-layer standard:
path fidelity | hash match | size match | role/lineage reconciliation.

## Scope / Target / Owner Boundary

Target files: 7 (6 direct input candidates + 1 bundle agent_request file).

Owner boundary: Claude owns the verification report, result JSON, and worker
return packet when this packet is delegated to Claude. For the 2026-06-07
operator-authorized Codex multi-role override, Codex owns worker execution,
review, commits, session sync, and later T11C/T11D work orders.

## Authorization / Decision

GC-018: `docs/baselines/CVF_GC018_LPCI2_T11B_POLICYLOCAL_SOURCE_VERIFICATION_2026-06-07.md`

T11A closed at `lpci2_t11a_candidate_and_bundle_inventory_closed_pass_bounded`.
`nextAllowedMove` in `CVF_SESSION/ACTIVE_SESSION_STATE.json` explicitly
authorizes T11B source verification.

Operator instruction 2026-06-07 (amended): T11B scope = four-gate scan-layer
verification: path fidelity, hash match, size match, role/lineage reconciliation.
Unicode drift check mandatory (`-LiteralPath` on all filesystem calls).
No body extraction, no ingestion.

## Authority Chain

| Authority item | Path / evidence |
|---|---|
| GC-018 | `docs/baselines/CVF_GC018_LPCI2_T11B_POLICYLOCAL_SOURCE_VERIFICATION_2026-06-07.md` |
| Active session front door | `CVF_SESSION_MEMORY.md` |
| Machine state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| Active handoff | `AGENT_HANDOFF_V16_2026-06-06.md` |
| T11 roadmap | `docs/roadmaps/CVF_LPCI2_T11_POLICYLOCAL_CORPUS_EXPANSION_READINESS_ROADMAP_2026-06-07.md` |
| T11A candidate inventory | `docs/reference/CVF_LPCI2_T11_CANDIDATE_INVENTORY_2026-06-07.md` |
| T11A candidate manifest | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t11-candidate-manifest.json` |
| T11A bundle inventory | `docs/reference/CVF_LPCI2_T11_REAL_USE_CASE_BUNDLE_INVENTORY_2026-06-07.md` |
| T11A bundle manifest | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t11-real-use-case-bundle-manifest.json` |
| NR-04 source hash standard | `docs/reference/CVF_CORPUS_SOURCE_HASH_STANDARD_2026-06-02.md` |
| Text encoding standard | `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md` |

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Orchestrator / dispatcher | Codex | Review T11A and dispatch T11B |
| Worker / implementer | Claude, or Codex under explicit operator override | Path verification, hash computation, artifacts, return packet |
| Reviewer / closer | Codex or operator-designated reviewer | Review return and decide T11B closure |
| Operator checkpoint | Operator | Required only for scope expansion beyond path/hash verification |

## Startup Acknowledgment Required

Before implementation, Claude must read the active startup front doors and
record:

`Startup acknowledged: current mode=<mode>; active handoff=<handoff>; next allowed move=<summary>; parked checkpoint=<none|summary>.`

## Worker Autonomy / No-Question Rule

Claude must proceed autonomously inside Allowed scope. In-scope formatting,
schema, count, path, hash, and gate failures must be repaired and rerun before
return.

Claude must stop only if the repair would exceed Allowed scope, require body
extraction, consume live/provider quota, touch forbidden paths, change the
claim boundary, or require operator facts not available from filesystem
metadata.

Specific stop condition: if 3 or more of the 7 target files return
`PATH_NOT_FOUND` after the mandatory fallback attempt (see Unicode Drift Guard
below), return `BLOCKED_MASS_PATH_FAILURE` rather than continuing.

## Source Verification Block

### Source Verification Table

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| T11A closed PASS_BOUNDED | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | `currentMode` | `currentMode` | Session state registry | ACCEPT |
| T11B authorized as next allowed move | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | `nextAllowedMove` | `nextAllowedMove` | Session state registry | ACCEPT |
| T11A-CAND-001 path | `docs/reference/CVF_LPCI2_T11_CANDIDATE_INVENTORY_2026-06-07.md` | Candidate row 1 | `readableAt` | T11A candidate inventory | ACCEPT |
| T11A-CAND-002 path | `docs/reference/CVF_LPCI2_T11_CANDIDATE_INVENTORY_2026-06-07.md` | Candidate row 2 | `readableAt` | T11A candidate inventory | ACCEPT |
| T11A-CAND-003 path | `docs/reference/CVF_LPCI2_T11_CANDIDATE_INVENTORY_2026-06-07.md` | Candidate row 3 | `readableAt` | T11A candidate inventory | ACCEPT |
| T11A-CAND-004 path | `docs/reference/CVF_LPCI2_T11_CANDIDATE_INVENTORY_2026-06-07.md` | Candidate row 4 | `readableAt` | T11A candidate inventory | ACCEPT |
| T11A-CAND-005 path | `docs/reference/CVF_LPCI2_T11_CANDIDATE_INVENTORY_2026-06-07.md` | Candidate row 5 | `readableAt` | T11A candidate inventory | ACCEPT |
| T11A-CAND-006 path | `docs/reference/CVF_LPCI2_T11_CANDIDATE_INVENTORY_2026-06-07.md` | Candidate row 6 | `readableAt` | T11A candidate inventory | ACCEPT |
| BNDL-006 path | `docs/reference/CVF_LPCI2_T11_REAL_USE_CASE_BUNDLE_INVENTORY_2026-06-07.md` | Bundle row BNDL-006 | `relativePath` | T11A bundle inventory | ACCEPT |
| SHA-256 hash standard (NR-04) | `docs/reference/CVF_CORPUS_SOURCE_HASH_STANDARD_2026-06-02.md` | canonical standard | `artifactHashSha256` | NR-04 hash standard | ACCEPT |
| Unicode filename exception | `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md` | canonical standard | existing-filename exception | Text encoding standard | ACCEPT |

### New Doc-Only Fields

| Field | Owner artifact | Purpose | Runtime status |
|---|---|---|---|
| `verificationResult` | T11B report and JSON | Per-file outcome: HASH_MATCH / HASH_MISMATCH / SIZE_MISMATCH / ROLE_LINEAGE_MISMATCH / PATH_NOT_FOUND / READ_ERROR | DOC_ONLY_NEW |
| `testPathResult` | T11B JSON | Boolean result of `Test-Path -LiteralPath` | DOC_ONLY_NEW |
| `computedHashSha256` | T11B JSON | SHA-256 hex computed at T11B execution time | DOC_ONLY_NEW |
| `t11aManifestHashSha256` | T11B JSON | SHA-256 hex from T11A manifest (reference value) | DOC_ONLY_NEW |
| `observedSizeBytes` | T11B JSON | File size observed via `Get-Item -LiteralPath | .Length` | DOC_ONLY_NEW |
| `t11aManifestSizeBytes` | T11B JSON | File size from T11A manifest `sizeBytes` field (reference value) | DOC_ONLY_NEW |
| `sizeMatch` | T11B JSON | Boolean: observed == manifest size | DOC_ONLY_NEW |
| `roleLineageMatch` | T11B JSON | Boolean: bundle role and lineage parent IDs match T11A bundle manifest row | DOC_ONLY_NEW |
| `verificationSummary` | T11B JSON | Total files, all-gates-PASS count, per-gate failure lists | DOC_ONLY_NEW |

## Target File List

### In-scope files (7 total: 6 direct candidates + 1 bundle agent_request)

Reference values sourced from T11A manifests. Worker must verify all four gates per row.

| ID | Candidate/Bundle ID | Role | T11A size (bytes) | T11A SHA-256 (full 64-char) |
|---|---|---|---|---|
| 1 | `T11A-CAND-001` / `BNDL-001` | `source_input` | 842159 | `61fafa4b69e9b0423c9bd3533ba6b5be531b9b73c26c6cfb62933008bfecc4d5` |
| 2 | `T11A-CAND-002` / `BNDL-002` | `source_input` | 933326 | `2e7ed68a7814ff04e8246dbfb179f928d4d952b30169685f73115f2702459adc` |
| 3 | `T11A-CAND-003` / `BNDL-003` | `source_input` | 45314 | `265047c2ca26b13f2c6212313f550f3ce0f66f85bd7470ec9c3618d4c54cb4f6` |
| 4 | `T11A-CAND-004` / `BNDL-004` | `source_input` | 537770 | `cf4fa584fc62ea1edc9c9d27e7396040c7036b2f313c8f5586df04d5529ee46e` |
| 5 | `T11A-CAND-005` / `BNDL-005` | `source_input` | 1292455 | `47460fdfbdde10d69ae4838b711e086f4037cfd2609d6a4263caefbb1e9fabe7` |
| 6 | `T11A-CAND-006` / `BNDL-007` | `source_input` | 1076338 | `4522d37bf8da78fb41d01d97cdb2bff3f7133af2b02e146f3537132ce603bee6` |
| 7 | `BNDL-006` | `agent_request` | 15248 | `29281becea319d5985298cd34a6a66a6b1e2a051a4f157a254d18aebfa734806` |

Absolute paths (exact, for `-LiteralPath` use):

- ID 1: `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\3094.pdf`
- ID 2: `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\BC- Kết quả rà soát dự án chậm triển khai - Phú Xuyên 10.5.2026.pdf`
- ID 3: `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\Kien nghi thành ủy hà nội (1).docx`
- ID 4: `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\Phu luc danh sach du an.pdf`
- ID 5: `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\QD chấm dứt.pdf`
- ID 6: `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\Thong bao thu hoi 24 du an.pdf`
- ID 7: `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\Law use case_Codex\Request for agent.docx`

Role/lineage reference (from T11A bundle manifest for IDs 1–7):

- IDs 1–6 (`source_input`): `lineageParentIds=[]`; cross-referenced by `t11aCandidateRef` in bundle manifest.
- ID 7 (`agent_request`): `lineageParentIds=[]`; references BNDL-001..005 + BNDL-007 semantically per bundle inventory lineage map.

## Allowed Scope

Claude may:

- call `Test-Path -LiteralPath` for each target file path;
- read file size via `(Get-Item -LiteralPath <path>).Length` after path resolves;
- compute SHA-256 hashes from raw binary file reads (65536-byte chunks), same
  method as T11A supplement;
- compare computed hashes against T11A manifest `artifactHashSha256` values;
- compare observed sizes against T11A manifest `sizeBytes` values;
- read `bundleArtifactRole` and `lineageParentIds` from the T11A bundle manifest
  JSON and compare against T11A bundle inventory rows for bundle-scope files
  (BNDL-001..007); for direct-input candidates, confirm matching `bundleArtifactId`
  cross-reference via `t11aCandidateRef` field;
- create `docs/reference/CVF_LPCI2_T11B_SOURCE_VERIFICATION_REPORT_2026-06-07.md`;
- create
  `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t11b-source-verification-result.json`;
- create
  `docs/reviews/CVF_LPCI2_T11B_SOURCE_VERIFICATION_WORKER_RETURN_2026-06-07.md`;
- record Unicode drift fallback attempts if any initial `Test-Path` fails;
- run local JSON parse/count/gate checks.

## Forbidden Scope

Claude must not:

- parse, extract, summarize, OCR, or read body content of any target file;
- modify any target file;
- ingest candidates into `policylocal-corpus-records.json`;
- modify T9/T10/T11A artifacts, chunks, receipts, scripts, readiness reports;
- run provider calls, LLM/chat runtime, browser proof, live proof, vector or
  embedding retrieval;
- claim legal advice quality, extraction quality, source authenticity,
  current-law status, production readiness, hosted readiness, public readiness,
  or release readiness;
- update public-sync or expose private file paths publicly;
- commit changes.

## Unicode Filename Drift Guard (MANDATORY)

The T11A supplement review recorded Unicode path-normalization drift as a risk.
All filesystem operations in T11B must follow this guard:

1. Use `-LiteralPath` on every `Test-Path`, `Get-Item`, or equivalent call.
   Never use positional path argument without `-LiteralPath`.
2. Load exact paths from the T11A bundle manifest JSON `relativePath` field
   for bundle files and from the T11A candidate inventory `Readable At` column
   for direct-input candidates.
3. If `Test-Path -LiteralPath` returns False for a file:
   a. Attempt fallback: re-read exact path from the bundle manifest JSON
      `relativePath` field and retest with `-LiteralPath`.
   b. If fallback also fails, record `PATH_NOT_FOUND` and `testPathResult=false`.
   c. Do not attempt hash computation for `PATH_NOT_FOUND` files.
4. Compute SHA-256 hash only after `Test-Path` returns True.
5. Use Python `sys.stdout.reconfigure(encoding='utf-8')` if using a Python
   script for hash computation, to prevent Windows cp1252 UnicodeEncodeError
   on Vietnamese filenames in console output.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap / GC-018 requirement | Work-order instruction | Evidence target | Status |
|---|---|---|---|
| T11-B Source Verification — path fidelity | `Test-Path -LiteralPath` per file; fallback on failure | `testPathResult` per file | READY |
| T11-B Source Verification — hash match | SHA-256 binary stream vs T11A manifest | `computedHashSha256` vs `t11aManifestHashSha256` | READY |
| T11-B Source Verification — size match | `Get-Item -LiteralPath .Length` vs T11A manifest | `observedSizeBytes` vs `t11aManifestSizeBytes` | READY |
| T11-B Source Verification — role/lineage reconciliation | compare `bundleArtifactRole` + `lineageParentIds` vs T11A bundle manifest | `roleLineageMatch` per file | READY |
| Unicode drift check mandatory | `-LiteralPath` on all filesystem calls | Unicode Drift Guard section | READY |
| No body extraction | Forbidden Scope | worker return packet | READY |
| T11B cannot close until Codex reviews | return uncommitted packet | worker return packet | READY |

## Required First Reads

Claude must read:

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `AGENT_HANDOFF_V16_2026-06-06.md`
4. `docs/baselines/CVF_GC018_LPCI2_T11B_POLICYLOCAL_SOURCE_VERIFICATION_2026-06-07.md`
5. `docs/reference/CVF_LPCI2_T11_CANDIDATE_INVENTORY_2026-06-07.md`
6. `docs/reference/CVF_LPCI2_T11_REAL_USE_CASE_BUNDLE_INVENTORY_2026-06-07.md`
7. `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t11-candidate-manifest.json`
8. `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t11-real-use-case-bundle-manifest.json`

## Pre-Flight Checks

Before implementation, capture:

```powershell
git rev-parse --short HEAD
git status --short
Test-Path -LiteralPath 'D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\3094.pdf'
Test-Path -LiteralPath 'D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\Law use case_Codex\Request for agent.docx'
```

Expected base head is `486370fe` or a later Codex dispatch commit that
contains this work order unchanged.

If the target directory `Policy_Local\data_input` is missing entirely, stop
and return `BLOCKED_SOURCE_NOT_FOUND`.

## Write Ownership

Owned paths:

- `docs/reference/CVF_LPCI2_T11B_SOURCE_VERIFICATION_REPORT_2026-06-07.md`
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t11b-source-verification-result.json`
- `docs/reviews/CVF_LPCI2_T11B_SOURCE_VERIFICATION_WORKER_RETURN_2026-06-07.md`

Forbidden paths:

- `EXTENSIONS/*`
- `.github/*`
- `governance/compat/*`
- package manifests and lockfiles
- public-sync clone
- T9/T10/T11A generated corpus, chunks, receipts, scripts, readiness reports
- external bundle source files under `Law use case_Codex`
- `policylocal-corpus-records.json`
- `policylocal-t11-candidate-manifest.json`
- `policylocal-t11-real-use-case-bundle-manifest.json`
- active session files (session sync is reviewer-owned, after acceptance only)

## Work-Order Fulfillment Manifest

## Required Artifact Manifest

| Path | Output stage | Purpose |
|---|---|---|
| `docs/reference/CVF_LPCI2_T11B_SOURCE_VERIFICATION_REPORT_2026-06-07.md` | worker return | markdown verification report, 7 rows |
| `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t11b-source-verification-result.json` | worker return | machine-readable verification result |
| `docs/reviews/CVF_LPCI2_T11B_SOURCE_VERIFICATION_WORKER_RETURN_2026-06-07.md` | worker return | worker evidence packet for Codex review |

## Required Proof Manifest

| Proof | Required evidence |
|---|---|
| Gate 1 — Path fidelity | `testPathResult` boolean for each of the 7 target files |
| Gate 2 — Hash match | `computedHashSha256` vs `t11aManifestHashSha256` comparison table for all 7 files |
| Gate 3 — Size match | `observedSizeBytes` vs `t11aManifestSizeBytes` comparison table for all 7 files |
| Gate 4 — Role/lineage reconciliation | `roleLineageMatch` boolean per file; role and lineageParentIds compared against T11A bundle manifest |
| Unicode drift check | evidence that `-LiteralPath` was used; any drift fallback cases recorded |
| Schema | `policylocal.sourceVerification.t11b.v1` parses and validates |
| No extraction | worker return states no body parsing, OCR, ingestion, runtime, provider action |

## Execution Plan

1. Read required startup and inventory artifacts (including both T11A manifests).
2. Capture `git rev-parse --short HEAD` and `git status --short`.
3. For each of the 7 target files, run all four gates:
   a. **Gate 1 — Path fidelity:** `Test-Path -LiteralPath <path>` — record boolean.
      If False: attempt fallback using exact `relativePath` from bundle manifest JSON.
      Re-test with `-LiteralPath`. If still False, record `PATH_NOT_FOUND`; skip
      Gates 2–4 for that file.
   b. **Gate 2 — Hash match:** compute SHA-256 from binary stream (65536-byte chunks).
      Compare against `t11aManifestHashSha256`. Record `HASH_MATCH` or `HASH_MISMATCH`.
   c. **Gate 3 — Size match:** read `(Get-Item -LiteralPath <path>).Length`.
      Compare against `t11aManifestSizeBytes`. Record `sizeMatch=true/false`.
      If false, flag `SIZE_MISMATCH` in `verificationResult`.
   d. **Gate 4 — Role/lineage reconciliation:** read `bundleArtifactRole` and
      `lineageParentIds` from T11A bundle manifest for the matching `bundleArtifactId`.
      Confirm role matches the T11B target list reference value. Confirm
      `lineageParentIds` matches manifest record. Record `roleLineageMatch=true/false`.
      If false, flag `ROLE_LINEAGE_MISMATCH` in `verificationResult`.
   e. Set `verificationResult` = `HASH_MATCH` only when all four gates pass.
      If any gate fails, use the most severe failure token:
      `PATH_NOT_FOUND` > `READ_ERROR` > `HASH_MISMATCH` > `SIZE_MISMATCH` > `ROLE_LINEAGE_MISMATCH`.
4. Produce markdown verification report (one row per file, all four gate columns).
5. Produce JSON verification result (schema `policylocal.sourceVerification.t11b.v1`).
6. Reconcile: total=7; verify `verificationSummary` all-gates-pass count and
   per-gate failure lists.
7. Produce worker return packet with all evidence.
8. Run local JSON parse check and gate checks.

## Evidence Requirements

Claude must record:

- startup acknowledgment;
- pre-flight commands and results;
- Gate 1: `Test-Path -LiteralPath` output and any fallback attempts for all 7 files;
- Gate 2: SHA-256 computation method + hash comparison table (computed vs manifest) for all 7 files;
- Gate 3: `observedSizeBytes` vs `t11aManifestSizeBytes` comparison table for all 7 files;
- Gate 4: `bundleArtifactRole` and `lineageParentIds` comparison vs manifest for all 7 files;
- `verificationSummary` from JSON (all-gates-pass count + per-gate failure lists);
- JSON parse result;
- changed files;
- explicit no-extraction/no-ingestion/no-provider/no-public-sync boundary.

## Review Gate

Codex must review the T11B worker return before deciding T11B closure. After
T11B closes, Codex may open the T11C Classification Pre-Check work order.

## Closure Checklist

- [x] Verification report created (7 rows, all four gate columns present).
- [x] Result JSON parses and reconciles.
- [x] All 7 files have `testPathResult`, `computedHashSha256`, `t11aManifestHashSha256`,
      `observedSizeBytes`, `t11aManifestSizeBytes`, `sizeMatch`, `roleLineageMatch`,
      and `verificationResult`.
- [x] Unicode drift guard applied (`-LiteralPath` used on every filesystem call).
- [x] `verificationSummary` includes all-gates-pass count and per-gate failure lists.
- [x] No forbidden scope action occurred.
- [x] Codex reviewed worker return.

## Return-To-Orchestrator Conditions

Return to Codex without marking PASS if:

- the target data_input directory is missing entirely;
- 3 or more of the 7 target files return `PATH_NOT_FOUND`
  (`BLOCKED_MASS_PATH_FAILURE`);
- hash computation fails for a file for a reason other than file not found;
- body extraction, OCR, summarization, or semantic evaluation becomes necessary;
- any forbidden path would need modification.

## Operator Checkpoint

Operator input is not required for path/hash verification execution. Operator
input is required before any later governed rerun, legal-content evaluation,
corpus classification change, public-sync, provider call, or production claim.

## Acceptance Criteria

1. Verification report markdown exists, has exactly 7 rows, and includes columns
   for all four gates (path, hash, size, role/lineage).
2. Result JSON exists, parses, uses schema `policylocal.sourceVerification.t11b.v1`,
   and has exactly 7 file records.
3. Every file record has: `candidateId` (or `bundleArtifactId`), `absolutePath`,
   `testPathResult`, `computedHashSha256`, `t11aManifestHashSha256`,
   `observedSizeBytes`, `t11aManifestSizeBytes`, `sizeMatch`,
   `roleLineageMatch`, and `verificationResult`.
4. All `testPathResult` values are boolean; `PASS` requires `true` for all 7.
5. All `verificationResult` values are one of: `HASH_MATCH`, `HASH_MISMATCH`,
   `SIZE_MISMATCH`, `ROLE_LINEAGE_MISMATCH`, `PATH_NOT_FOUND`, `READ_ERROR`.
6. `verificationSummary` field present in JSON with: `totalFiles`, `allGatesPass`
   count, `gate1PathFailures`, `gate2HashFailures`, `gate3SizeFailures`,
   `gate4RoleLineageFailures` lists.
7. Worker return records pre-flight output, all four gate comparison tables,
   `verificationSummary`, changed files, and claim boundary.
8. No forbidden scope action occurs.

## Fail Conditions

- missing `data_input` directory;
- 3 or more `PATH_NOT_FOUND` after drift fallback (`BLOCKED_MASS_PATH_FAILURE`);
- missing hash, size, or role/lineage fields for any resolved file;
- semantic/body extraction or legal-content evaluation;
- runtime/provider/public-sync claim;
- worker commit.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED`; `Commit mode: WORKER_MUST_NOT_COMMIT`; Codex override recorded | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_LPCI2_T11B_SOURCE_VERIFICATION_COMPLETION_2026-06-07.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| GC-018 baseline | `docs/baselines/CVF_GC018_LPCI2_T11B_POLICYLOCAL_SOURCE_VERIFICATION_2026-06-07.md` | `Status: ACTIVE`; `baseHead: 486370fe` | PASS |
| Roadmap state | `docs/roadmaps/CVF_LPCI2_T11_POLICYLOCAL_CORPUS_EXPANSION_READINESS_ROADMAP_2026-06-07.md` | T11A/T11B closed; T11C/T11D remain open | PASS |
| Registry JSON | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | session sync required after closure commit | PASS |
| Registry Markdown | `CVF_SESSION_MEMORY.md`; `AGENT_HANDOFF_V16_2026-06-06.md` | session sync required after closure commit | PASS |
| External evidence digest | `policylocal-t11b-source-verification-result.json` | `sha256:0d24870a43b0e33eecddae438d669983be508eff9ed4ca4e112ffb48870fd79d` | PASS |
| System loop interlock | this file | path/hash verification only; no runtime/system loop mutation authorized | PASS |
| Session continuity | `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `AGENT_HANDOFF_V16_2026-06-06.md` | session sync required after closure commit | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private PolicyLocal real use-case source files and workspace paths are
in scope. No public-sync, public remote push, public catalog update, or public
artifact export is authorized.

## Text Encoding And Symbol Boundary

Agent-authored prose defaults to ASCII. Exact existing filenames and filesystem
paths may include Vietnamese Unicode characters and may be quoted only as source
evidence under the existing-filename exception in
`docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md`.

When printing file paths to console (Python), use
`sys.stdout.reconfigure(encoding='utf-8')` to prevent Windows cp1252 errors.

## Claim Boundary

This work order authorizes local path verification and SHA-256 hash matching
only. It does not authorize document body parsing, OCR, summarization,
legal-content evaluation, corpus ingestion, chunking, search runtime, memory
reinjection, provider calls, public-sync, source authenticity claims,
current-law claims, legal advice quality claims, hosted readiness, production
readiness, public readiness, or release readiness.
