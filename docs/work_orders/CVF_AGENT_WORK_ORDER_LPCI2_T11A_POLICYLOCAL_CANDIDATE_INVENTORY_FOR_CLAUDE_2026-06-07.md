# CVF Agent Work Order - LPCI2-T11A PolicyLocal Candidate Inventory For Claude

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-07

dispatchBaseHead: `93bf9909`

executionBaseHead: `93bf9909`

closureBaseHead: `34f1c4ec`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Risk class: R1_LOCAL_INVENTORY_AND_EVIDENCE_ONLY

Worker: Claude

Reviewer / closer: Codex or operator-designated reviewer

## Purpose

Create a bounded T11A candidate inventory for the six newly added PolicyLocal
input files. The files are mixed real-case policy/legal material, not pure law
only. T11A records candidate metadata and a machine-readable manifest, but does
not extract document body text or ingest anything into the corpus.

## Scope / Target / Owner Boundary

Target: six candidate files under
`D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\`.

Owner boundary: Claude owns the T11A inventory, manifest, and worker return
packet only. Codex owns closure review, commits, session sync, and any later
T11B/T11C/T11D work orders.

## Authorization / Decision

Operator stated on 2026-06-07 that newly added files are not pure law but are
related and are real cases. This work order therefore authorizes mixed
candidate inventory only, with conservative classification and no runtime or
legal-readiness claim.

## Authority Chain

| Authority item | Path / evidence |
|---|---|
| Active session front door | `CVF_SESSION_MEMORY.md` |
| Machine state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| Active handoff | `AGENT_HANDOFF_V16_2026-06-06.md` |
| T11 roadmap | `docs/roadmaps/CVF_LPCI2_T11_POLICYLOCAL_CORPUS_EXPANSION_READINESS_ROADMAP_2026-06-07.md` |
| T11A GC-018 | `docs/baselines/CVF_GC018_LPCI2_T11A_POLICYLOCAL_CANDIDATE_INVENTORY_2026-06-07.md` |
| T10 completion | `docs/reviews/CVF_LPCI2_T10_POLICYLOCAL_FOUNDATION_READINESS_COMPLETION_2026-06-07.md` |
| T2 domain classification spec | `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` |
| Text encoding standard | `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md` |

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Orchestrator / dispatcher | Codex | Repair roadmap, file GC-018, source-verify and dispatch T11A |
| Worker / implementer | Claude | Create inventory, manifest, and worker return packet; do not commit |
| Reviewer / closer | Codex or operator-designated reviewer | Review worker return, run closure gates, commit if accepted |
| Operator checkpoint | Operator | Required only for scope expansion, missing candidate sources, extraction, ingestion, live/provider proof, public-sync, or claim-boundary change |

## Startup Acknowledgment Required

Before implementation, Claude must read the active startup front doors and
acknowledge:

`Startup acknowledged: current mode=<mode>; active handoff=<handoff>; next allowed move=<summary>; parked checkpoint=<none|summary>.`

## Worker Autonomy / No-Question Rule

Claude must proceed autonomously inside Allowed scope. In-scope formatting,
schema, count, path, manifest, JSON parse, and gate failures must be repaired
and rerun before return.

Claude must stop only if the repair would exceed Allowed scope, require document
body extraction, consume live/provider quota, touch forbidden paths, change the
claim boundary, or require operator facts not available from the candidate file
names and filesystem metadata.

## Source Verification Block

### Source Verification Table

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| T11 roadmap exists and authorizes candidate inventory before T12 | `docs/roadmaps/CVF_LPCI2_T11_POLICYLOCAL_CORPUS_EXPANSION_READINESS_ROADMAP_2026-06-07.md` | `## Tranche Plan`; `### T11-A: Candidate Inventory`; `## Next Allowed Move After This Roadmap Is Committed` | `T11-A` | LPCI2-T11 roadmap | ACCEPT |
| T11A GC-018 exists | `docs/baselines/CVF_GC018_LPCI2_T11A_POLICYLOCAL_CANDIDATE_INVENTORY_2026-06-07.md` | `## Purpose`; `## Candidate Boundary` | `T11A-CAND-*` | GC-018 baseline | ACCEPT |
| T10 foundation readiness is closed and T11 planning is allowed | `docs/reviews/CVF_LPCI2_T10_POLICYLOCAL_FOUNDATION_READINESS_COMPLETION_2026-06-07.md` | `## Final Disposition`; `## Claim Boundary`; `## Next Roadmap Recommendation` | `CLOSED_PASS_BOUNDED` | T10 completion review | ACCEPT |
| T2 answerClass vocabulary | `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` | `## answerClass Classification Criteria` | `DIRECT_CITED_ANSWER`, `SUMMARY_WITH_SOURCE`, `PROCEDURAL_GUIDANCE`, `ESCALATE_OR_ABSTAIN` | T2 domain classification spec | ACCEPT |
| Text encoding exception for existing Unicode filenames | `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md` | canonical standard | existing Unicode filenames | Text encoding standard | ACCEPT |
| Candidate source file exists | canonical-contract: filesystem-verified external candidate path | filesystem enumeration 2026-06-07 | `T11A-CAND-001` | PolicyLocal candidate source | ACCEPT |
| Candidate source file exists | canonical-contract: filesystem-verified external candidate path | filesystem enumeration 2026-06-07 | `T11A-CAND-002` | PolicyLocal candidate source | ACCEPT |
| Candidate source file exists | canonical-contract: filesystem-verified external candidate path | filesystem enumeration 2026-06-07 | `T11A-CAND-003` | PolicyLocal candidate source | ACCEPT |
| Candidate source file exists | canonical-contract: filesystem-verified external candidate path | filesystem enumeration 2026-06-07 | `T11A-CAND-004` | PolicyLocal candidate source | ACCEPT |
| Candidate source file exists | canonical-contract: filesystem-verified external candidate path | filesystem enumeration 2026-06-07 | `T11A-CAND-005` | PolicyLocal candidate source | ACCEPT |
| Candidate source file exists | canonical-contract: filesystem-verified external candidate path | filesystem enumeration 2026-06-07 | `T11A-CAND-006` | PolicyLocal candidate source | ACCEPT |
| Existing pilot law source excluded from T11A candidate expansion | canonical-contract: filesystem-verified external pilot path | filesystem enumeration 2026-06-07 | `pilot-exclusion-116_2025_QH15_666020` | T9/T10 pilot corpus source | ACCEPT |
| Existing pilot law source excluded from T11A candidate expansion | canonical-contract: filesystem-verified external pilot path | filesystem enumeration 2026-06-07 | `pilot-exclusion-148_2025_QH15_675262` | T9/T10 pilot corpus source | ACCEPT |

### New Doc-Only Fields

| Field | Owner artifact | Purpose | Runtime status |
|---|---|---|---|
| `candidateFamily` | T11A inventory and manifest | Planning metadata for mixed candidate material | DOC_ONLY_NEW |
| `readableAt` | T11A manifest | Source path or URL for later T11B access verification | DOC_ONLY_NEW |
| `sourceRole` | T11A inventory and manifest | Distinguish expansion candidate from existing pilot exclusion | DOC_ONLY_NEW |
| `ec02Applies` | T11A inventory and manifest | Preserve freshness boundary before 2026-07-01 | DOC_ONLY_NEW |

## Allowed Scope

Claude may:

- create `docs/reference/CVF_LPCI2_T11_CANDIDATE_INVENTORY_2026-06-07.md`;
- create
  `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t11-candidate-manifest.json`;
- create
  `docs/reviews/CVF_LPCI2_T11A_CANDIDATE_INVENTORY_WORKER_RETURN_2026-06-07.md`;
- enumerate filesystem metadata for the six candidate files and the two pilot
  exclusion files;
- record file names, extensions, sizes, last-write timestamps, candidate IDs,
  conservative initial `documentType`, `candidateFamily`, `currentStatus`,
  `answerClass`, `ec02Applies`, and `readableAt`;
- run local JSON parse/count reconciliation and markdown/gate checks.

## Forbidden Scope

Claude must not:

- extract PDF/DOCX body text, run OCR, parse document clauses, or summarize
  contents;
- ingest new documents into `policylocal-corpus-records.json`;
- modify T9/T10 artifacts, chunks, receipts, search runtime, or existing pilot
  corpus records;
- run provider calls, LLM/chat runtime, browser proof, live proof, vector or
  embedding retrieval;
- claim legal advice quality, source authenticity, current-law status,
  production readiness, hosted readiness, public readiness, or release
  readiness;
- update public-sync or expose private file paths publicly;
- commit changes.

## Candidate Inputs

| Candidate ID | Source path | Initial candidateFamily | Initial documentType | Initial answerClass |
|---|---|---|---|---|
| `T11A-CAND-001` | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\3094.pdf` | `applied_policy_record` | `other` | `ESCALATE_OR_ABSTAIN` |
| `T11A-CAND-002` | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\BC- Kết quả rà soát dự án chậm triển khai - Phú Xuyên 10.5.2026.pdf` | `project_case_record` | `other` | `ESCALATE_OR_ABSTAIN` |
| `T11A-CAND-003` | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\Kien nghi thành ủy hà nội (1).docx` | `applied_policy_record` | `other` | `ESCALATE_OR_ABSTAIN` |
| `T11A-CAND-004` | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\Phu luc danh sach du an.pdf` | `project_case_record` | `other` | `ESCALATE_OR_ABSTAIN` |
| `T11A-CAND-005` | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\QD chấm dứt.pdf` | `administrative_decision` | `decision` | `ESCALATE_OR_ABSTAIN` |
| `T11A-CAND-006` | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\Thong bao thu hoi 24 du an.pdf` | `administrative_notice` | `notice` | `ESCALATE_OR_ABSTAIN` |

Initial `ESCALATE_OR_ABSTAIN` is conservative. T11C may revise only after
source verification and classification pre-check.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Evidence target | Status |
|---|---|---|---|
| T11-A Candidate Inventory | Create inventory markdown and manifest JSON | Required Artifact Manifest | READY |
| Mixed case files must stay candidate-only | Initial conservative metadata and claim boundary | Candidate Inputs and Claim Boundary | READY |
| EC-02 boundary applies | Preserve `ec02Applies` and no current-law claim | Required Proof Manifest | READY |
| No ingestion/runtime/provider work | Forbidden Scope and Fail Conditions | Worker return packet | READY |
| T12 gated behind later T11-D verdict | T11A return only; no readiness verdict | Claim Boundary | READY |

## Required First Reads

Claude must read:

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `AGENT_HANDOFF_V16_2026-06-06.md`
4. `docs/roadmaps/CVF_LPCI2_T11_POLICYLOCAL_CORPUS_EXPANSION_READINESS_ROADMAP_2026-06-07.md`
5. `docs/baselines/CVF_GC018_LPCI2_T11A_POLICYLOCAL_CANDIDATE_INVENTORY_2026-06-07.md`
6. `docs/reviews/CVF_LPCI2_T10_POLICYLOCAL_FOUNDATION_READINESS_COMPLETION_2026-06-07.md`
7. `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md`
8. `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md`

## Pre-Flight Checks

Before edits, Claude must capture:

```powershell
git rev-parse --short HEAD
git status --short
Get-ChildItem -LiteralPath 'D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input' -File
```

Expected base head is `93bf9909` or a later Codex dispatch commit that contains
this work order unchanged. If the six candidate files are missing, stop and
return `BLOCKED_SOURCE_NOT_FOUND`.

## Write Ownership

Owned paths:

- `docs/reference/CVF_LPCI2_T11_CANDIDATE_INVENTORY_2026-06-07.md`
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t11-candidate-manifest.json`
- `docs/reviews/CVF_LPCI2_T11A_CANDIDATE_INVENTORY_WORKER_RETURN_2026-06-07.md`

Forbidden paths:

- `EXTENSIONS/*`
- `.github/*`
- `governance/compat/*`
- package manifests and lockfiles
- public-sync clone
- T9/T10 generated corpus, chunks, receipts, scripts, and readiness report
- active session files, except reviewer-owned session sync after acceptance

## Work-Order Fulfillment Manifest

## Required Artifact Manifest

| Path | Output stage | Purpose |
|---|---|---|
| `docs/reference/CVF_LPCI2_T11_CANDIDATE_INVENTORY_2026-06-07.md` | worker return | markdown candidate inventory |
| `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t11-candidate-manifest.json` | worker return | machine-readable candidate manifest |
| `docs/reviews/CVF_LPCI2_T11A_CANDIDATE_INVENTORY_WORKER_RETURN_2026-06-07.md` | worker return | worker evidence packet for Codex review |

## Required Proof Manifest

| Proof | Required evidence |
|---|---|
| Candidate count | exactly six candidate rows in inventory and manifest |
| Schema | manifest `schemaVersion=policylocal.candidateManifest.t11.v1` |
| Reconciliation | candidate IDs match between inventory and manifest |
| Pilot exclusion | two existing law DOCX files listed as excluded baseline sources |
| EC-02 boundary | all unknown/not-yet-current candidates keep `ec02Applies=true` or `currentStatus=unknown` with no current-law claim |
| No extraction | worker return states no body extraction/OCR/ingestion/chunking/runtime query |

## Execution Plan

1. Read this work order, T11 roadmap, T11A GC-018, T10 completion, T2 spec, and
   text encoding standard.
2. Capture `git rev-parse --short HEAD` and `git status --short`.
3. Enumerate the six candidate paths and two pilot exclusion paths.
4. Create the markdown inventory with conservative planning metadata.
5. Create the JSON manifest and parse it with Python or Node.
6. Reconcile candidate IDs and counts between inventory and manifest.
7. Create the worker return packet with evidence and claim boundary.
8. Run allowed local gates and repair any allowed-scope failures before return.

## Evidence Requirements

Claude must record:

- startup acknowledgment;
- pre-flight commands and results;
- filesystem enumeration evidence for six candidates and two pilot exclusions;
- inventory path and row count;
- manifest path, schemaVersion, and record count;
- inventory/manifest candidate ID reconciliation result;
- changed files from `git status --short`;
- explicit no-extraction/no-ingestion/no-provider/no-runtime/no-public-sync
  boundary statement.

## Review Gate

Codex reviewer may accept T11A only if all acceptance criteria pass, the worker
return packet is bounded, changed files stay inside Write Ownership, and no
forbidden runtime/legal/public claim is made.

## Closure Checklist

- [x] Inventory markdown created.
- [x] Manifest JSON created and parse-checked.
- [x] Six candidate rows reconciled.
- [x] Two pilot law DOCX files recorded as exclusions.
- [x] EC-02 boundary recorded.
- [x] Worker return packet created.
- [x] No forbidden scope action occurred.

## Return-To-Orchestrator Conditions

Return `RETURNED_PASS_BOUNDED` if all acceptance criteria pass. Return
`BLOCKED_SOURCE_NOT_FOUND` if any named candidate path is missing. Return
`BLOCKED_SCOPE_EXCEEDED` if completing the work would require extraction,
ingestion, runtime changes, provider calls, public-sync, or operator facts not
available from source filenames and filesystem metadata.

## Operator Checkpoint

Operator checkpoint is required only for adding/removing candidate files,
authorizing extraction/OCR/body parsing, changing answerClass beyond the
conservative initial value, opening T11B/T11C/T11D, or authorizing any public,
runtime, provider, or current-law claim.

## Acceptance Criteria

1. Inventory markdown exists and has exactly six candidate rows.
2. Manifest JSON exists, parses, has schema
   `policylocal.candidateManifest.t11.v1`, and has exactly six candidate
   records.
3. Every candidate has non-empty `candidateId`, `readableAt`, `sourceRole`,
   `candidateFamily`, `documentType`, `currentStatus`, `answerClass`, and
   `ec02Applies`.
4. Candidate IDs reconcile exactly between inventory and manifest.
5. Pilot law DOCX files are excluded from candidate expansion.
6. Worker return packet records changed files, commands, and boundaries.
7. No forbidden scope action occurs.

## Fail Conditions

- Any candidate file named in this work order is missing.
- Manifest count and inventory count differ.
- Any candidate has empty required metadata.
- Any candidate is promoted beyond `ESCALATE_OR_ABSTAIN` without T11C
  classification evidence.
- Any body extraction, OCR, ingestion, chunking, runtime query, provider call,
  public-sync, current-law claim, or production/public readiness claim occurs.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED`; `Commit mode: WORKER_MUST_NOT_COMMIT` preserved for worker execution | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_LPCI2_T11A_CANDIDATE_AND_BUNDLE_INVENTORY_COMPLETION_2026-06-07.md` | Codex closure review after original and supplement returns | PASS |
| GC-018 baseline | `docs/baselines/CVF_GC018_LPCI2_T11A_POLICYLOCAL_CANDIDATE_INVENTORY_2026-06-07.md` | active authorization for T11A | PASS |
| Roadmap state | `docs/roadmaps/CVF_LPCI2_T11_POLICYLOCAL_CORPUS_EXPANSION_READINESS_ROADMAP_2026-06-07.md` | T11 roadmap remains `PROPOSED`; T11A sub-tranche closed only | PASS |
| Worker return packet | `docs/reviews/CVF_LPCI2_T11A_CANDIDATE_INVENTORY_WORKER_RETURN_2026-06-07.md` | `RETURNED_PASS_BOUNDED` for original direct scope | PASS |
| Inventory markdown | `docs/reference/CVF_LPCI2_T11_CANDIDATE_INVENTORY_2026-06-07.md` | six candidate rows and pilot exclusions | PASS |
| Manifest JSON | `CVF-Workspace/Policy_Local/data/generated/policylocal-t11-candidate-manifest.json` | sha256:e06dc12c54c3a3ecab7d468c8de996feae9f1f79b9cce568642932e2ea0cf43e | PASS |
| Registry JSON | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | T11A closed and T11B routed; GC-051 corpus registry not updated until T11D/T12 readiness | PASS |
| Registry Markdown | `CVF_SESSION_MEMORY.md`; `AGENT_HANDOFF_V16_2026-06-06.md` | T11A closure and next allowed move recorded | PASS |
| External evidence digest | candidate manifest | sha256:e06dc12c54c3a3ecab7d468c8de996feae9f1f79b9cce568642932e2ea0cf43e | PASS |
| System loop interlock | N/A with reason | inventory-only work; no runtime/system loop mutation authorized | N/A with reason |
| Session continuity | reviewer-owned session sync | mode/next move/handoff updated for T11A closure | PASS |

## Public Export Disposition

`DEFERRED_PRIVATE_ONLY`

Reason: this work order references private PolicyLocal local paths and
candidate source filenames. No public-facing artifact, public-sync, public
push, or public readiness claim is authorized.

## Text Encoding And Symbol Boundary

Agent-authored prose must default to ASCII. Exact source filenames may contain
Vietnamese Unicode characters; quoting those existing filenames is allowed only
as source evidence under the existing-filename exception in the text encoding
standard.

## Claim Boundary

This work order may claim only that Claude produced a T11A candidate inventory
and manifest for named private candidate files.

It does not claim document readability, source authenticity, extraction
correctness, corpus ingestion, current-law status, legal answer quality, search
runtime behavior, provider behavior, hosted readiness, production readiness,
public readiness, release readiness, memory reinjection, high-risk promotion,
or autonomous mutation.
