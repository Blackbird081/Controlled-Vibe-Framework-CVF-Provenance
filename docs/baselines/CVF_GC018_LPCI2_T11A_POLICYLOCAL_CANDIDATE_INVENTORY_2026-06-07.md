# CVF GC-018 LPCI2-T11A PolicyLocal Candidate Inventory

Memory class: FULL_RECORD

Status: ACTIVE

docType: gc018_baseline

Date: 2026-06-07

baseHead: `93bf9909`

## Purpose

Authorize the LPCI2-T11A Candidate Inventory work order after T10 foundation
readiness closed. T11A inventories newly added PolicyLocal candidate files
without extracting, ingesting, chunking, indexing, querying, or calling a
provider.

## Scope / Target / Owner Boundary

Target: the six newly added candidate files under
`D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\`.

Owner boundary: Claude may create inventory and manifest artifacts plus a
worker return packet. Codex or the operator remains reviewer/closer. T11A does
not authorize T11B source verification closure, T11C classification closure,
T11D readiness verdict, T12 ingestion, runtime changes, public-sync, or live
proof.

## Authorization / Decision

Operator stated on 2026-06-07 that the newly added files are not pure law but
are related and are real cases. Decision: T11A must treat them as mixed
PolicyLocal candidate material and preserve conservative classification until
later T11 tranches verify source access and classification.

## Source / Predecessor Evidence

| Evidence | Path / source | Disposition |
|---|---|---|
| T10 foundation readiness closure | `docs/reviews/CVF_LPCI2_T10_POLICYLOCAL_FOUNDATION_READINESS_COMPLETION_2026-06-07.md` | ACCEPT |
| T11 roadmap | `docs/roadmaps/CVF_LPCI2_T11_POLICYLOCAL_CORPUS_EXPANSION_READINESS_ROADMAP_2026-06-07.md` | ACCEPT |
| Existing candidate source directory | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\` | ACCEPT |
| T2 classification vocabulary | `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` | ACCEPT |
| Text encoding exception for existing Unicode filenames | `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md` | ACCEPT |

## Decision / Baseline / Proposed Tranche

Baseline decision: authorize only T11A candidate inventory.

Proposed tranche: `LPCI2-T11A PolicyLocal Candidate Inventory`.

Dispatch packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI2_T11A_POLICYLOCAL_CANDIDATE_INVENTORY_FOR_CLAUDE_2026-06-07.md`

Readiness dependency: T11B source verification must not begin until T11A
returns inventory and manifest evidence for reviewer acceptance.

## Candidate Boundary

Candidate files to inventory:

| Candidate ID | Source path | Initial candidate family |
|---|---|---|
| `T11A-CAND-001` | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\3094.pdf` | `applied_policy_record` |
| `T11A-CAND-002` | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\BC- Kết quả rà soát dự án chậm triển khai - Phú Xuyên 10.5.2026.pdf` | `project_case_record` |
| `T11A-CAND-003` | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\Kien nghi thành ủy hà nội (1).docx` | `applied_policy_record` |
| `T11A-CAND-004` | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\Phu luc danh sach du an.pdf` | `project_case_record` |
| `T11A-CAND-005` | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\QD chấm dứt.pdf` | `administrative_decision` |
| `T11A-CAND-006` | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\Thong bao thu hoi 24 du an.pdf` | `administrative_notice` |

Existing pilot source files remain excluded from T11A candidate expansion:

- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\116_2025_QH15_666020.docx`
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\148_2025_QH15_675262.docx`

## Work Plan

1. Enumerate the six candidate paths above and confirm filesystem presence.
2. Create a markdown inventory with one row per candidate.
3. Create a JSON candidate manifest with schema
   `policylocal.candidateManifest.t11.v1`.
4. Record pilot-source exclusions and the EC-02 boundary.
5. Return evidence to Codex without committing.

## Acceptance Criteria

- Inventory markdown exists and has exactly six candidate rows.
- Manifest JSON exists, parses, uses schema
  `policylocal.candidateManifest.t11.v1`, and has exactly six candidate
  records.
- Inventory and manifest candidate IDs reconcile exactly.
- Every candidate has a non-empty initial `currentStatus`, proposed
  `answerClass`, `candidateFamily`, `documentType`, and `readableAt`.
- Existing pilot law DOCX files are excluded from expansion candidates.
- No body extraction, corpus ingestion, chunking, indexing, runtime search,
  provider call, current-law claim, production claim, or public-sync occurs.

## Verification / Evidence

Required evidence:

- `git rev-parse --short HEAD`
- `git status --short`
- filesystem enumeration of the six candidate files
- JSON parse check for the manifest
- inventory/manifest candidate count reconciliation
- changed-file evidence
- pre-implementation or local component gate evidence if run by the worker

## Claim Boundary

This GC-018 authorizes T11A inventory only. It does not prove document
readability, text extraction, legal authority, source authenticity, current-law
status, legal advice quality, search behavior, provider behavior, hosted
readiness, production readiness, public readiness, or release readiness.

## Non-Goals

No extraction, OCR, PDF parsing, DOCX body parsing, ingestion, chunking,
runtime query execution, vector retrieval, provider call, public-sync, or
mutation of existing T9/T10 artifacts.

## Text Encoding And Symbol Boundary

Agent-authored prose defaults to ASCII. Existing source filenames include
Vietnamese Unicode characters and may be quoted exactly as source evidence
under the existing-filename exception in
`docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md`.
