# CVF Agent Work Order - LPCI2-T11A Supplement Real Use-Case Bundle Inventory For Claude

Memory class: FULL_RECORD

Status: DISPATCHED_TO_WORKER

docType: work_order

Date: 2026-06-07

dispatchBaseHead: `db43e449`

executionBaseHead: `db43e449`

closureBaseHead: `N/A - worker must return uncommitted supplement packet for Codex review`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Risk class: R1_LOCAL_INVENTORY_AND_EVIDENCE_ONLY

Worker: Claude

Reviewer / closer: Codex or operator-designated reviewer

## Purpose

Supplement T11A by inventorying the full real use-case bundle that contains
the six PolicyLocal source files plus the unguided Codex request, extracted
text, and rendered output artifacts.

This supplement exists because PolicyLocal is a pilot for a domain-agnostic CVF
scan/memory/context layer. The real use-case bundle is evidence of prior
ungoverned Codex behavior before CVF applies scan-layer and memory-context
governance.

## Scope / Target / Owner Boundary

Target directory:

`D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\Law use case_Codex`

Owner boundary: Claude owns the supplement inventory, manifest, and worker
return packet only. Codex owns review, commits, session sync, and later
T11B/T11C/T11D work orders.

## Authorization / Decision

Operator clarified on 2026-06-07 that the six files are part of a real Codex
use case, including:

- 6 source input files;
- `Request for agent.docx`;
- `_extracted_text/`;
- `_rendered_don_kien_nghi/` with two rendered output versions.

This supplement authorizes inventory and lineage mapping only.

## Authority Chain

| Authority item | Path / evidence |
|---|---|
| Active session front door | `CVF_SESSION_MEMORY.md` |
| Machine state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| Active handoff | `AGENT_HANDOFF_V16_2026-06-06.md` |
| T11 roadmap | `docs/roadmaps/CVF_LPCI2_T11_POLICYLOCAL_CORPUS_EXPANSION_READINESS_ROADMAP_2026-06-07.md` |
| T11A original work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI2_T11A_POLICYLOCAL_CANDIDATE_INVENTORY_FOR_CLAUDE_2026-06-07.md` |
| T11A Codex review | `docs/reviews/CVF_LPCI2_T11A_CANDIDATE_INVENTORY_CODEX_REVIEW_2026-06-07.md` |
| Text encoding standard | `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md` |

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Orchestrator / dispatcher | Codex | Review original T11A return and dispatch supplement |
| Worker / implementer | Claude | Create real use-case bundle inventory, manifest, and worker return; do not commit |
| Reviewer / closer | Codex or operator-designated reviewer | Review supplement return and decide combined T11A closure |
| Operator checkpoint | Operator | Required only for scope expansion beyond inventory/lineage, body extraction, ingestion, live/provider proof, public-sync, or claim-boundary change |

## Startup Acknowledgment Required

Before implementation, Claude must read the active startup front doors and
acknowledge:

`Startup acknowledged: current mode=<mode>; active handoff=<handoff>; next allowed move=<summary>; parked checkpoint=<none|summary>.`

## Worker Autonomy / No-Question Rule

Claude must proceed autonomously inside Allowed scope. In-scope formatting,
schema, count, path, manifest, JSON parse, hash, and gate failures must be
repaired and rerun before return.

Claude must stop only if the repair would exceed Allowed scope, require
document body extraction, consume live/provider quota, touch forbidden paths,
change the claim boundary, or require operator facts not available from
filesystem metadata and folder structure.

## Source Verification Block

### Source Verification Table

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Original T11A direct input inventory returned | `docs/reviews/CVF_LPCI2_T11A_CANDIDATE_INVENTORY_WORKER_RETURN_2026-06-07.md` | `## Return Disposition` | `RETURNED_PASS_BOUNDED` | T11A worker return | ACCEPT |
| Codex review requires supplement for real use-case bundle | `docs/reviews/CVF_LPCI2_T11A_CANDIDATE_INVENTORY_CODEX_REVIEW_2026-06-07.md` | `## Review Verdict`; `## Required Remediation` | `PASS_FOR_ORIGINAL_SCOPE__SUPPLEMENT_REQUIRED` | T11A Codex review | ACCEPT |
| Target real use-case bundle directory exists | canonical-contract: filesystem-verified external bundle path | filesystem enumeration 2026-06-07 | `Law use case_Codex` | PolicyLocal external use-case bundle | ACCEPT |
| Bundle includes request artifact | canonical-contract: filesystem-verified external bundle path | filesystem enumeration 2026-06-07 | `Request for agent.docx` | PolicyLocal external use-case bundle | ACCEPT |
| Bundle includes extracted-text artifact folder | canonical-contract: filesystem-verified external bundle path | filesystem enumeration 2026-06-07 | `_extracted_text` | PolicyLocal external use-case bundle | ACCEPT |
| Bundle includes rendered-output artifact folder | canonical-contract: filesystem-verified external bundle path | filesystem enumeration 2026-06-07 | `_rendered_don_kien_nghi` | PolicyLocal external use-case bundle | ACCEPT |
| Text encoding exception allows exact existing Unicode filenames when needed | `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md` | canonical standard | existing Unicode filenames | Text encoding standard | ACCEPT |

### New Doc-Only Fields

| Field | Owner artifact | Purpose | Runtime status |
|---|---|---|---|
| `bundleArtifactId` | supplement inventory and manifest | Stable ID for every artifact in the real use-case bundle | DOC_ONLY_NEW |
| `bundleArtifactRole` | supplement inventory and manifest | Role classification for source/request/extracted/rendered artifacts | DOC_ONLY_NEW |
| `lineageParentIds` | supplement manifest | Rebuildable relationship from request to source inputs to extracted text to outputs | DOC_ONLY_NEW |
| `ungovernedCodexBaseline` | supplement manifest | Flag artifacts produced before CVF governance intervention | DOC_ONLY_NEW |
| `artifactHashSha256` | supplement manifest | Secret-safe file identity for later provenance comparison | DOC_ONLY_NEW |

## Allowed Scope

Claude may:

- enumerate all files and immediate folders under the target bundle directory;
- compute SHA256 hashes for files without summarizing or extracting semantic
  content;
- create `docs/reference/CVF_LPCI2_T11_REAL_USE_CASE_BUNDLE_INVENTORY_2026-06-07.md`;
- create
  `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t11-real-use-case-bundle-manifest.json`;
- create
  `docs/reviews/CVF_LPCI2_T11A_SUPPLEMENT_REAL_USE_CASE_BUNDLE_WORKER_RETURN_2026-06-07.md`;
- classify artifacts only by filename, extension, folder, and provenance role:
  `source_input`, `agent_request`, `ungoverned_extracted_text`,
  `ungoverned_generated_output`, `rendered_output_variant`;
- record lineage edges at folder/file level;
- run local JSON parse/count/hash reconciliation and markdown/gate checks.

## Forbidden Scope

Claude must not:

- parse, summarize, evaluate, improve, rewrite, or rerun the document body
  content;
- OCR PDFs or parse DOCX body content;
- modify any external bundle files;
- ingest bundle artifacts into `policylocal-corpus-records.json`;
- modify T9/T10 artifacts, chunks, receipts, scripts, readiness reports, or the
  original T11A manifest;
- run provider calls, LLM/chat runtime, browser proof, live proof, vector or
  embedding retrieval;
- claim legal advice quality, extraction quality, source authenticity,
  current-law status, production readiness, hosted readiness, public readiness,
  or release readiness;
- update public-sync or expose private file paths publicly;
- commit changes.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap / review requirement | Work-order instruction | Evidence target | Status |
|---|---|---|---|
| T11-A Candidate Inventory | Supplement direct input inventory with real use-case bundle inventory | Required Artifact Manifest | READY |
| Mixed case files must stay candidate-only | Role classify source/request/extracted/rendered artifacts without body parsing | Bundle inventory and manifest | READY |
| Domain-general scan/memory value must be preserved | Mark unguided Codex baseline and lineage for later CVF context comparison | `ungovernedCodexBaseline`; `lineageParentIds` | READY |
| No ingestion/runtime/provider work | Forbidden Scope and Fail Conditions | Worker return packet | READY |
| T11A cannot close until supplement reviewed | Return uncommitted supplement packet to Codex | Worker return packet | READY |

## Required First Reads

Claude must read:

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `AGENT_HANDOFF_V16_2026-06-06.md`
4. `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI2_T11A_POLICYLOCAL_CANDIDATE_INVENTORY_FOR_CLAUDE_2026-06-07.md`
5. `docs/reviews/CVF_LPCI2_T11A_CANDIDATE_INVENTORY_WORKER_RETURN_2026-06-07.md`
6. `docs/reviews/CVF_LPCI2_T11A_CANDIDATE_INVENTORY_CODEX_REVIEW_2026-06-07.md`
7. `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md`

## Pre-Flight Checks

Before edits, Claude must capture:

```powershell
git rev-parse --short HEAD
git status --short
Get-ChildItem -LiteralPath 'D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\Law use case_Codex' -Force
Get-ChildItem -LiteralPath 'D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\Law use case_Codex' -Force -Recurse
```

Expected base head is `db43e449` or a later Codex dispatch commit that
contains this supplement work order unchanged. If the target bundle directory
is missing, stop and return `BLOCKED_SOURCE_NOT_FOUND`.

## Write Ownership

Owned paths:

- `docs/reference/CVF_LPCI2_T11_REAL_USE_CASE_BUNDLE_INVENTORY_2026-06-07.md`
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t11-real-use-case-bundle-manifest.json`
- `docs/reviews/CVF_LPCI2_T11A_SUPPLEMENT_REAL_USE_CASE_BUNDLE_WORKER_RETURN_2026-06-07.md`

Forbidden paths:

- `EXTENSIONS/*`
- `.github/*`
- `governance/compat/*`
- package manifests and lockfiles
- public-sync clone
- T9/T10 generated corpus, chunks, receipts, scripts, and readiness report
- original external bundle files under `Law use case_Codex`
- active session files, except reviewer-owned session sync after acceptance

## Work-Order Fulfillment Manifest

## Required Artifact Manifest

| Path | Output stage | Purpose |
|---|---|---|
| `docs/reference/CVF_LPCI2_T11_REAL_USE_CASE_BUNDLE_INVENTORY_2026-06-07.md` | worker return | markdown real use-case bundle inventory |
| `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t11-real-use-case-bundle-manifest.json` | worker return | machine-readable bundle manifest |
| `docs/reviews/CVF_LPCI2_T11A_SUPPLEMENT_REAL_USE_CASE_BUNDLE_WORKER_RETURN_2026-06-07.md` | worker return | worker evidence packet for Codex review |

## Required Proof Manifest

| Proof | Required evidence |
|---|---|
| Bundle existence | target directory exists and is enumerated |
| Artifact roles | every file has one allowed `bundleArtifactRole` |
| Lineage | manifest records request -> source inputs -> extracted text -> rendered outputs at folder/file level |
| Hash identity | every file row has `artifactHashSha256` |
| Ungoverned baseline | extracted text and rendered output artifacts are marked `ungovernedCodexBaseline=true` |
| No extraction | worker return states no body parsing/OCR/summarization/rerun/ingestion/runtime/provider action |

## Execution Plan

1. Read required startup and review artifacts.
2. Capture `git rev-parse --short HEAD` and `git status --short`.
3. Enumerate the real use-case bundle recursively.
4. Classify each file by role from folder/name/extension only.
5. Compute SHA256 file hashes.
6. Create markdown inventory and JSON manifest.
7. Reconcile file counts, role counts, hashes, and lineage edges.
8. Create worker return packet with evidence and claim boundary.
9. Run allowed local gates and repair any allowed-scope failures before return.

## Evidence Requirements

Claude must record:

- startup acknowledgment;
- pre-flight commands and results;
- filesystem enumeration evidence;
- inventory path and row count;
- manifest path, schemaVersion, role counts, and file count;
- SHA256 hash coverage for all file rows;
- lineage summary;
- JSON parse result;
- changed files;
- explicit no-extraction/no-ingestion/no-provider/no-public-sync boundary.

## Review Gate

Codex must review the supplement together with the original T11A return before
deciding T11A closure.

## Closure Checklist

- [ ] Bundle inventory created.
- [ ] Manifest parses and reconciles.
- [ ] All file rows have artifact roles and SHA256 hashes.
- [ ] Lineage edges are present.
- [ ] Ungoverned Codex baseline artifacts are marked.
- [ ] No forbidden scope action occurred.
- [ ] Codex reviewed original T11A return plus supplement together.

## Return-To-Orchestrator Conditions

Return to Codex without marking PASS if:

- the target bundle directory is missing;
- file enumeration cannot be completed;
- hash computation fails for one or more files;
- role classification cannot stay filename/folder-based;
- body extraction, OCR, summarization, or semantic evaluation becomes necessary;
- any forbidden path would need modification.

## Operator Checkpoint

Operator input is not required for inventory-only supplement execution. Operator
input is required before any later governed rerun, legal-content evaluation,
domain-general runtime abstraction, public-sync, provider call, or production
claim.

## Acceptance Criteria

1. supplement inventory markdown exists and includes every file in the bundle;
2. manifest parses as JSON and includes every file in the bundle;
3. every file has `bundleArtifactId`, `bundleArtifactRole`,
   `artifactHashSha256`, and `ungovernedCodexBaseline`;
4. role counts reconcile with inventory rows;
5. lineage edges distinguish source inputs, request, extracted text, and
   rendered outputs;
6. worker return records commands, counts, hash coverage, changed files, and
   claim boundary;
7. no forbidden scope action occurs.

## Fail Conditions

- missing target bundle directory;
- missing `Request for agent.docx`;
- missing `_extracted_text`;
- missing `_rendered_don_kien_nghi`;
- manifest count mismatch;
- missing hashes;
- semantic/body extraction or legal-content evaluation;
- runtime/provider/public-sync claim;
- worker commit.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: DISPATCHED_TO_WORKER`; `Commit mode: WORKER_MUST_NOT_COMMIT` | PASS |
| Completion or reviewer artifact | N/A with reason | Worker has not returned supplement yet | N/A with reason |
| Roadmap state | `docs/roadmaps/CVF_LPCI2_T11_POLICYLOCAL_CORPUS_EXPANSION_READINESS_ROADMAP_2026-06-07.md` | T11 remains in progress; T11A requires supplement before closure | PASS |
| Registry JSON | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Next allowed move routes T11A supplement execution | PASS |
| Registry Markdown | `CVF_SESSION_MEMORY.md`; `AGENT_HANDOFF_V16_2026-06-06.md` | Active front doors route T11A supplement execution | PASS |
| External evidence digest | N/A with reason | Supplement manifest/hash evidence is required before reviewer closure | N/A with reason |
| System loop interlock | this file | Inventory-only supplement; no runtime/system loop mutation authorized | PASS |
| Session continuity | `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `AGENT_HANDOFF_V16_2026-06-06.md` | Session sync required after dispatch commit | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private PolicyLocal real use-case source files, extracted text, rendered
outputs, and workspace paths are in scope.

No public-sync repository change, public remote push, public catalog update,
public readiness claim, or public artifact export is authorized.

Next public action: N/A with reason. Public export can be considered only after
a later public-safe summary strips private paths, hashes, and non-public source
material.

## Text Encoding And Symbol Boundary

Agent-authored prose defaults to ASCII. Exact existing filenames and filesystem
paths may include Vietnamese Unicode characters and may be quoted only as source
evidence under the existing-filename exception in
`docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md`.

## Claim Boundary

This work order authorizes local inventory and lineage mapping only. It does
not authorize document body parsing, OCR, summarization, legal-content
evaluation, corpus ingestion, chunking, search runtime, memory reinjection,
provider calls, public-sync, source authenticity claims, current-law claims,
legal advice quality claims, hosted readiness, production readiness, public
readiness, or release readiness.
