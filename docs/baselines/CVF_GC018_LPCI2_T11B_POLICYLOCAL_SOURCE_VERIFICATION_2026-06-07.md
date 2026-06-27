# CVF GC-018 LPCI2-T11B PolicyLocal Source Verification

Memory class: FULL_RECORD

Status: ACTIVE

docType: gc018_baseline

Date: 2026-06-07

baseHead: `486370fe`

## Purpose

Authorize the LPCI2-T11B Source Verification work order after T11A candidate
and bundle inventory closed. T11B verifies that every inventoried candidate
file resolves to a readable path and that SHA-256 hashes match the T11A
manifest values. It also validates that Unicode filename normalization does not
cause path resolution failures.

T11B implements a four-gate scan-layer standard:
path fidelity | hash match | size match | role/lineage reconciliation.

T11B does not extract document body content, ingest corpus records, run runtime
queries, call providers, or make current-law or production readiness claims.

## Scope / Target / Owner Boundary

Target files: the 7 distinct source-input or request files from T11A:

- 6 direct input candidates (`T11A-CAND-001` through `T11A-CAND-006`) under
  `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\`
- 1 `agent_request` file (`Request for agent.docx`) from the
  `Law use case_Codex` bundle

Note: the 6 direct input candidates are the same physical files as BNDL-001
through BNDL-007 (source_input role) in the bundle manifest, so path
verification covers both inventory views. The 7 `ungoverned_extracted_text`
files and 2 `rendered_output_variant` files are out of T11B scope (they are
not corpus ingestion candidates).

Owner boundary: Claude may produce a source verification report, a verification
result JSON, and a worker return packet. Codex or the operator remains
reviewer/closer. T11B does not authorize T11C classification pre-check, T11D
readiness verdict, T12 ingestion, runtime changes, public-sync, or live proof.

## Decision / Baseline / Proposed Tranche

T11A closed at `lpci2_t11a_candidate_and_bundle_inventory_closed_pass_bounded`.
`nextAllowedMove` in `CVF_SESSION/ACTIVE_SESSION_STATE.json` at baseHead
`486370fe` explicitly authorizes T11B source verification for the combined
direct candidate inventory and `Law use case_Codex` bundle evidence.

Operator road-map instruction 2026-06-07: T11B scope is access/path/hash
verification only. Unicode filename drift check is mandatory to avoid
re-introducing the path-normalization failure recorded in the T11A supplement
Codex review risk table.

## Source / Predecessor Evidence

| Evidence | Path / source | Disposition |
|---|---|---|
| T11A closure mode | `CVF_SESSION/ACTIVE_SESSION_STATE.json` `currentMode` | ACCEPT |
| T11A `nextAllowedMove` | `CVF_SESSION/ACTIVE_SESSION_STATE.json` `nextAllowedMove` | ACCEPT |
| T11A candidate inventory | `docs/reference/CVF_LPCI2_T11_CANDIDATE_INVENTORY_2026-06-07.md` | ACCEPT |
| T11A candidate manifest | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t11-candidate-manifest.json` | ACCEPT |
| T11A bundle inventory | `docs/reference/CVF_LPCI2_T11_REAL_USE_CASE_BUNDLE_INVENTORY_2026-06-07.md` | ACCEPT |
| T11A bundle manifest | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t11-real-use-case-bundle-manifest.json` | ACCEPT |
| T11A supplement Codex review (Unicode drift risk) | `docs/reviews/CVF_LPCI2_T11A_CANDIDATE_INVENTORY_CODEX_REVIEW_2026-06-07.md` | ACCEPT |
| T11 roadmap | `docs/roadmaps/CVF_LPCI2_T11_POLICYLOCAL_CORPUS_EXPANSION_READINESS_ROADMAP_2026-06-07.md` | ACCEPT |
| NR-04 source hash standard | `docs/reference/CVF_CORPUS_SOURCE_HASH_STANDARD_2026-06-02.md` | ACCEPT |
| Text encoding standard | `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md` | ACCEPT |

## Target File List

### Direct Input Candidates (also bundle source_input files)

| Candidate ID | Bundle ID | Exact filesystem path | T11A SHA-256 (first 16 chars) |
|---|---|---|---|
| `T11A-CAND-001` | `BNDL-001` | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\3094.pdf` | `61fafa4b69e9b042` |
| `T11A-CAND-002` | `BNDL-002` | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\BC- Kết quả rà soát dự án chậm triển khai - Phú Xuyên 10.5.2026.pdf` | `2e7ed68a7814ff04` |
| `T11A-CAND-003` | `BNDL-003` | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\Kien nghi thành ủy hà nội (1).docx` | `265047c2ca26b13f` |
| `T11A-CAND-004` | `BNDL-004` | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\Phu luc danh sach du an.pdf` | `cf4fa584fc62ea1e` |
| `T11A-CAND-005` | `BNDL-005` | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\QD chấm dứt.pdf` | `47460fdfbdde10d6` |
| `T11A-CAND-006` | `BNDL-007` | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\Thong bao thu hoi 24 du an.pdf` | `4522d37bf8da78fb` |

### Bundle-Only Files In Scope

| Bundle ID | Role | Exact filesystem path | T11A SHA-256 (first 16 chars) |
|---|---|---|---|
| `BNDL-006` | `agent_request` | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\Law use case_Codex\Request for agent.docx` | `29281becea319d59` |

### Out Of T11B Scope

- BNDL-008 through BNDL-014: `ungoverned_extracted_text` — pre-CVF extraction
  artifacts; not corpus ingestion candidates; excluded from T11B verification.
- BNDL-015, BNDL-016: `rendered_output_variant` — pre-CVF generated outputs;
  not corpus ingestion candidates; excluded from T11B verification.

## Work Plan

1. Read required startup front doors and this GC-018.
2. Capture `git rev-parse --short HEAD` and `git status --short`.
3. For each of the 7 target files, run all four gates:
   a. **Gate 1 — Path fidelity:** `Test-Path -LiteralPath` — mandatory;
      use `-LiteralPath` on every Windows filesystem call to avoid glob
      expansion on Unicode characters. If False, attempt one fallback
      using exact path from manifest JSON `relativePath`; if still False
      record `PATH_NOT_FOUND` and skip gates 2–4 for that file.
   b. **Gate 2 — Hash match:** compute SHA-256 from binary stream
      (65536-byte chunks). Compare against T11A manifest
      `artifactHashSha256`. Record `HASH_MATCH` or `HASH_MISMATCH`.
   c. **Gate 3 — Size match:** read `(Get-Item -LiteralPath).Length`.
      Compare against T11A manifest `sizeBytes`. Record `sizeMatch` boolean.
   d. **Gate 4 — Role/lineage reconciliation:** read `bundleArtifactRole`
      and `lineageParentIds` from T11A bundle manifest for the matching
      artifact. Confirm values match the T11B reference table. Record
      `roleLineageMatch` boolean.
   e. Set `verificationResult` = `HASH_MATCH` only when all four gates pass;
      otherwise use the highest-severity failure token.
4. Produce verification report markdown with one row per file, all four gate
   columns.
5. Produce verification result JSON with schema
   `policylocal.sourceVerification.t11b.v1`.
6. Produce worker return packet with evidence, reconciliation, and claim
   boundary.
7. Return artifacts to Codex uncommitted.

## Unicode Filename Drift Guard

The T11A supplement Codex review recorded a Unicode path-normalization drift
risk. The mandatory guard for T11B:

- All filesystem calls must use `-LiteralPath` (PowerShell) or exact literal
  path strings; no glob patterns, no wildcard expansion.
- If a `Test-Path -LiteralPath` returns False for any file, the worker must
  attempt one fallback: retrieve exact filename from the bundle manifest JSON
  `relativePath` field and retest. If the second test also fails, record
  `PATH_NOT_FOUND` and do not continue to hash computation for that file.
- Hash mismatches must be recorded as `HASH_MISMATCH`; the worker must not
  silently treat a partial-read hash as a match.

## Acceptance Criteria

1. Verification report markdown exists and has one row per target file (7 rows)
   with columns for all four gates.
2. Verification result JSON exists, parses, uses schema
   `policylocal.sourceVerification.t11b.v1`, and has 7 file records.
3. Every file record has `candidateId` (or `bundleArtifactId` for bundle-only),
   `absolutePath`, `testPathResult`, `computedHashSha256`,
   `t11aManifestHashSha256`, `verificationResult`, `observedSizeBytes`,
   `t11aManifestSizeBytes`, `sizeMatch`, and `roleLineageMatch`.
4. All `testPathResult` values are `true` or `false`; `PASS` requires `true`.
5. All `verificationResult` values are one of: `HASH_MATCH`, `HASH_MISMATCH`,
   `SIZE_MISMATCH`, `ROLE_LINEAGE_MISMATCH`, `PATH_NOT_FOUND`, `READ_ERROR`.
6. `verificationSummary` field in JSON records: total files, HASH_MATCH count,
   per-gate failure lists (pathFailed, hashFailed, sizeFailed, roleFailed).
7. Gate 3 evidence: `observedSizeBytes` from `Get-Item -LiteralPath .Length`
   compared against `t11aManifestSizeBytes`; `sizeMatch` boolean present.
8. Gate 4 evidence: `bundleArtifactRole` and `lineageParentIds` read from T11A
   bundle manifest; `roleLineageMatch` boolean present; discrepancies listed.
9. Worker return records commands, counts, all four gate comparison tables,
   changed files, and claim boundary.
10. No forbidden scope action occurs.

## Verification / Evidence

Required evidence in worker return:

- `git rev-parse --short HEAD`
- `git status --short`
- `Test-Path -LiteralPath` output for each target file
- SHA-256 computation method (binary stream, 65536-byte chunks)
- hash comparison table (computed vs T11A manifest, first 16 chars minimum)
- verification result for each file
- `verificationSummary` from result JSON
- JSON parse check
- changed-file evidence
- explicit no-extraction/no-ingestion/no-provider/no-public-sync boundary

## Claim Boundary

This GC-018 authorizes T11B source verification only. It does not prove
document readability, text correctness, legal authority, source authenticity,
current-law status, legal advice quality, search behavior, provider behavior,
extraction quality, chunking readiness, hosted readiness, production readiness,
public readiness, or release readiness.

T11B `HASH_MATCH` result proves only that the file at the exact path has the
same binary content as when T11A hashes were computed. It does not prove legal
validity, effective date, current-in-force status, or retrieval quality.

EC-02 freshness review remains required on or after 2026-07-01 before any
current-law or production runtime claim for any PolicyLocal corpus material.

## Non-Goals

No extraction, OCR, PDF parsing, DOCX body parsing, ingestion, chunking,
runtime query execution, vector retrieval, provider call, public-sync, or
mutation of existing T9/T10/T11A artifacts.
