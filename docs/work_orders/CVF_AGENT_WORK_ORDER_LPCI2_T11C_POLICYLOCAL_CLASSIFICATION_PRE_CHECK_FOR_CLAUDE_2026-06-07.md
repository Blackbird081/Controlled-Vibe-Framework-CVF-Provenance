# CVF Agent Work Order - LPCI2-T11C PolicyLocal Classification Pre-Check For Claude

Memory class: FULL_RECORD

Status: DISPATCHED_TO_WORKER

docType: work_order

Date: 2026-06-07

dispatchBaseHead: `e18ec2f1`

executionBaseHead: `PENDING`

closureBaseHead: `PENDING`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Risk class: R1_LOCAL_CLASSIFICATION_ONLY

Worker: Claude, or Codex under explicit operator-authorized multi-role override

Reviewer / closer: Codex or operator-designated reviewer

completionReview: `docs/reviews/CVF_LPCI2_T11C_CLASSIFICATION_PRE_CHECK_COMPLETION_2026-06-07.md`

## Purpose

Classify the T11B-verified candidate records against the T2 domain
classification matrix, the EC-02 freshness gate, and a T12-eligibility verdict,
before T12 corpus ingestion is authorized. Consume the T11B resolved-path
evidence and carry the Unicode path-fidelity finding forward. Return an
uncommitted evidence packet to Codex.

This is classification pre-check only: metadata classification bound to
verified paths. No body extraction, no ingestion, no runtime query, no provider
call.

## Scope / Target / Owner Boundary

Target records: 7 T11B-verified records.

- 6 corpus candidates (`T11A-CAND-001` through `T11A-CAND-006`) classified
  against the T2 matrix, EC-02 gate, and t12-eligibility.
- 1 non-corpus request artifact (`BNDL-006`, `agent_request`) classified only
  as a request artifact with `t12Eligible=NO` and no corpus answerClass.

Owner boundary: Claude owns the classification pre-check report, the additive
manifest update, and the worker return packet when this packet is delegated to
Claude. For an operator-authorized Codex multi-role override, Codex owns worker
execution, review, commits, session sync, and later T11D work order.

## Authorization / Decision

GC-018: `docs/baselines/CVF_GC018_LPCI2_T11C_POLICYLOCAL_CLASSIFICATION_PRE_CHECK_2026-06-07.md`

T11B closed at `lpci2_t11b_source_verification_closed_pass_bounded`.
`nextAllowedMove` in `CVF_SESSION/ACTIVE_SESSION_STATE.json` authorizes
authoring a source-verified T11C Classification Pre-Check work order.

Operator instruction 2026-06-07: next road is T11C Classification Pre-Check;
classify the 7 file-records per role/lineage/source authority before any
ingestion/chunking/query runtime is allowed in.

## Authority Chain

| Authority item | Path / evidence |
|---|---|
| GC-018 | `docs/baselines/CVF_GC018_LPCI2_T11C_POLICYLOCAL_CLASSIFICATION_PRE_CHECK_2026-06-07.md` |
| Active session front door | `CVF_SESSION_MEMORY.md` |
| Machine state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| Active handoff | `AGENT_HANDOFF_V16_2026-06-06.md` |
| T11 roadmap | `docs/roadmaps/CVF_LPCI2_T11_POLICYLOCAL_CORPUS_EXPANSION_READINESS_ROADMAP_2026-06-07.md` |
| T11B completion | `docs/reviews/CVF_LPCI2_T11B_SOURCE_VERIFICATION_COMPLETION_2026-06-07.md` |
| T11B result JSON | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t11b-source-verification-result.json` |
| T11A candidate manifest | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t11-candidate-manifest.json` |
| T11A bundle manifest | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t11-real-use-case-bundle-manifest.json` |
| T2 domain classification spec | `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` |
| Text encoding standard | `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md` |

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Orchestrator / dispatcher | Codex | Review T11B and dispatch T11C |
| Worker / implementer | Claude, or Codex under explicit operator override | Classification, manifest update, return packet |
| Reviewer / closer | Codex or operator-designated reviewer | Review return and decide T11C closure |
| Operator checkpoint | Operator | Required only for scope expansion beyond classification pre-check |

## Startup Acknowledgment Required

Before implementation, the worker must read the active startup front doors and
record:

`Startup acknowledged: current mode=<mode>; active handoff=<handoff>; next allowed move=<summary>; parked checkpoint=<none|summary>.`

## Worker Autonomy / No-Question Rule

The worker must proceed autonomously inside Allowed scope. In-scope formatting,
schema, count, vocabulary, and gate-accounting failures must be repaired and
rerun before return.

The worker must stop only if the repair would exceed Allowed scope, require body
extraction, consume live/provider quota, touch forbidden paths, change the
claim boundary, introduce a new answerClass value, or require operator facts not
available from existing metadata and T11B evidence.

Specific stop condition: if classifying a record would require reading document
body text to resolve `documentType`, `currentStatus`, or `jurisdiction`, leave
the record at its T11A metadata-derived classification and record a
`REQUIRES_BODY_REVIEW` note rather than performing extraction.

## Source Verification Block

### Source Verification Table

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| T11B closed PASS_BOUNDED | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | `currentMode` | `currentMode` | Session state registry | ACCEPT |
| T11C authorized as next allowed move | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | `nextAllowedMove` | `nextAllowedMove` | Session state registry | ACCEPT |
| T11C sub-tranche contract | `docs/roadmaps/CVF_LPCI2_T11_POLICYLOCAL_CORPUS_EXPANSION_READINESS_ROADMAP_2026-06-07.md` | T11-C section | `t12Eligible` | T11 roadmap | ACCEPT |
| T11B resolved paths | `docs/reviews/CVF_LPCI2_T11B_SOURCE_VERIFICATION_COMPLETION_2026-06-07.md` | External Artifact Hash Manifest | `resolvedPath` | T11B completion (external result JSON digest) | ACCEPT |
| Candidate classification metadata | `docs/reference/CVF_LPCI2_T11_CANDIDATE_INVENTORY_2026-06-07.md` | candidate rows | `candidateFamily` | T11A candidate inventory | ACCEPT |
| answerClass vocabulary | `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` | answerClass section | `answerClass` | T2 domain spec | ACCEPT |
| documentType enum | `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` | documentType enum | `documentType` | T2 domain spec | ACCEPT |
| Unicode filename exception | `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md` | canonical standard | existing-filename exception | Text encoding standard | ACCEPT |

### New Doc-Only Fields

| Field | Owner artifact | Purpose | Runtime status |
|---|---|---|---|
| `domainCategory` | T11C report and manifest update | T2 domain category per candidate | DOC_ONLY_NEW |
| `ec02Gate` | T11C report and manifest update | `BLOCKED_UNTIL_2026-07-01` / `PASSES_EC02` / `REQUIRES_REVIEW` | DOC_ONLY_NEW |
| `t12Eligible` | T11C report and manifest update | `YES` / `NO` / `CONDITIONAL` | DOC_ONLY_NEW |
| `classificationPreCheck` | T11A candidate manifest update | Additive object holding domainCategory, answerClass, ec02Gate, t12Eligible, rationale | DOC_ONLY_NEW |

## Target Record List

### Corpus candidates (6, classified against T2 matrix)

| ID | candidateFamily | documentType | currentStatus | ec02Applies | T11A answerClass |
|---|---|---|---|---|---|
| `T11A-CAND-001` | `applied_policy_record` | `other` | `unknown` | true | `ESCALATE_OR_ABSTAIN` |
| `T11A-CAND-002` | `project_case_record` | `other` | `unknown` | true | `ESCALATE_OR_ABSTAIN` |
| `T11A-CAND-003` | `applied_policy_record` | `other` | `unknown` | true | `ESCALATE_OR_ABSTAIN` |
| `T11A-CAND-004` | `project_case_record` | `other` | `unknown` | true | `ESCALATE_OR_ABSTAIN` |
| `T11A-CAND-005` | `administrative_decision` | `decision` | `unknown` | true | `ESCALATE_OR_ABSTAIN` |
| `T11A-CAND-006` | `administrative_notice` | `notice` | `unknown` | true | `ESCALATE_OR_ABSTAIN` |

### Non-corpus record (1)

| ID | Role | Disposition |
|---|---|---|
| `BNDL-006` | `agent_request` | Non-corpus request artifact; `t12Eligible=NO`; no corpus answerClass |

T11B-resolved paths (consume these; do not re-derive from T11A `readableAt`):

- `T11A-CAND-001`: `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\3094.pdf`
- `T11A-CAND-002`: `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\Law use case_Codex\BC- Kết quả rà soát dự án chậm triển khai - Phú Xuyên 10.5.2026.pdf`
- `T11A-CAND-003`: `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\Law use case_Codex\Kien nghi thành ủy hà nội (1).docx`
- `T11A-CAND-004`: `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\Phu luc danh sach du an.pdf`
- `T11A-CAND-005`: `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\Law use case_Codex\QD chấm dứt.pdf`
- `T11A-CAND-006`: `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\Thong bao thu hoi 24 du an.pdf`
- `BNDL-006`: `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data_input\Law use case_Codex\Request for agent.docx`

## Allowed Scope

The worker may:

- read T11A candidate manifest, T11A bundle manifest, T11B result JSON, and the
  T2 domain spec for classification metadata and vocabulary;
- assign `domainCategory` and `answerClass` from the T2 matrix using
  `documentType`, `currentStatus`, and `jurisdiction` rules only;
- assign `ec02Gate` and `t12Eligible` per the GC-018 work plan;
- create `docs/reference/CVF_LPCI2_T11_CLASSIFICATION_PRE_CHECK_2026-06-07.md`;
- update
  `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t11-candidate-manifest.json`
  with additive `classificationPreCheck` fields only (no removal of prior
  T11A fields);
- create `docs/reviews/CVF_LPCI2_T11C_CLASSIFICATION_PRE_CHECK_WORKER_RETURN_2026-06-07.md`;
- run local JSON parse and field-presence checks.

## Forbidden Scope

The worker must not:

- parse, extract, summarize, OCR, or read body content of any target file;
- modify any target source file;
- ingest candidates into `policylocal-corpus-records.json`;
- modify T9/T10/T11A/T11B generated chunks, receipts, scripts, readiness
  reports, the T11B result JSON, or the bundle manifest;
- introduce a new answerClass value beyond the four T2 matrix values;
- run provider calls, LLM/chat runtime, browser proof, live proof, vector or
  embedding retrieval;
- mark any `ec02Gate=BLOCKED_UNTIL_2026-07-01` record as `t12Eligible=YES`;
- claim legal advice quality, source authenticity, current-law status,
  production readiness, hosted readiness, public readiness, or release
  readiness;
- update public-sync or expose private file paths publicly;
- commit changes.

## Unicode Path Fidelity Carry-Forward (MANDATORY)

The T11B completion recorded that `T11A-CAND-002`, `T11A-CAND-003`, and
`T11A-CAND-005` required Unicode fallback through the bundle manifest before
resolving (their resolved paths are under `Law use case_Codex\`).

1. Consume the T11B result JSON resolved paths for all records. Do not
   re-derive paths from T11A candidate `readableAt` literals alone.
2. If any filesystem call is made, use `-LiteralPath` on every call.
3. Use Python `sys.stdout.reconfigure(encoding='utf-8')` if a Python script
   prints Vietnamese filenames, to prevent Windows cp1252 errors.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap / GC-018 requirement | Work-order instruction | Evidence target | Status |
|---|---|---|---|
| T11-C domain category from T2 spec | classify each candidate via T2 matrix | `domainCategory` per candidate | READY |
| T11-C expected answerClass | assign from T2 matrix; unknown status/jurisdiction -> ESCALATE_OR_ABSTAIN | `answerClass` per candidate | READY |
| T11-C EC-02 gate | assign `ec02Gate` per record | `ec02Gate` per candidate | READY |
| T11-C t12 eligibility | assign `t12Eligible` per record | `t12Eligible` per candidate | READY |
| Zero BLOCKED records marked t12Eligible=YES | enforce in classification | EC-02 gate accounting | READY |
| answerClass vocabulary integrity | four T2 values only | classification report | READY |
| Manifest additive update only | add `classificationPreCheck`, retain prior fields | manifest diff | READY |
| Consume T11B resolved paths | use T11B result JSON paths | Unicode carry-forward section | READY |
| T11C cannot close until Codex reviews | return uncommitted packet | worker return packet | READY |

## Required First Reads

The worker must read:

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `AGENT_HANDOFF_V16_2026-06-06.md`
4. `docs/baselines/CVF_GC018_LPCI2_T11C_POLICYLOCAL_CLASSIFICATION_PRE_CHECK_2026-06-07.md`
5. `docs/roadmaps/CVF_LPCI2_T11_POLICYLOCAL_CORPUS_EXPANSION_READINESS_ROADMAP_2026-06-07.md`
6. `docs/reviews/CVF_LPCI2_T11B_SOURCE_VERIFICATION_COMPLETION_2026-06-07.md`
7. `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md`
8. `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t11b-source-verification-result.json`
9. `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t11-candidate-manifest.json`

## Pre-Flight Checks

Before implementation, capture:

```powershell
git rev-parse --short HEAD
git status --short
Test-Path -LiteralPath 'D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t11-candidate-manifest.json'
Test-Path -LiteralPath 'D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t11b-source-verification-result.json'
```

Expected base head is `e18ec2f1` or a later Codex dispatch commit that
contains this work order unchanged.

If the T11A candidate manifest or T11B result JSON is missing, stop and return
`BLOCKED_SOURCE_NOT_FOUND`.

## Write Ownership

Owned paths:

- `docs/reference/CVF_LPCI2_T11_CLASSIFICATION_PRE_CHECK_2026-06-07.md`
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t11-candidate-manifest.json` (additive `classificationPreCheck` fields only)
- `docs/reviews/CVF_LPCI2_T11C_CLASSIFICATION_PRE_CHECK_WORKER_RETURN_2026-06-07.md`

Forbidden paths:

- `EXTENSIONS/*`
- `.github/*`
- `governance/compat/*`
- package manifests and lockfiles
- public-sync clone
- T9/T10/T11A/T11B generated corpus, chunks, receipts, scripts, readiness
  reports, the T11B result JSON, and the bundle manifest
- external bundle source files under `Law use case_Codex`
- `policylocal-corpus-records.json`
- active session files (session sync is reviewer-owned, after acceptance only)

## Work-Order Fulfillment Manifest

## Required Artifact Manifest

| Path | Output stage | Purpose |
|---|---|---|
| `docs/reference/CVF_LPCI2_T11_CLASSIFICATION_PRE_CHECK_2026-06-07.md` | worker return | classification pre-check report, 7 rows |
| `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t11-candidate-manifest.json` | worker return | manifest with additive `classificationPreCheck` fields |
| `docs/reviews/CVF_LPCI2_T11C_CLASSIFICATION_PRE_CHECK_WORKER_RETURN_2026-06-07.md` | worker return | worker evidence packet for Codex review |

## Required Proof Manifest

| Proof | Required evidence |
|---|---|
| Domain classification | `domainCategory` + `answerClass` per candidate with T2-matrix rationale |
| EC-02 gate | `ec02Gate` per candidate; count of `BLOCKED_UNTIL_2026-07-01` |
| t12 eligibility | `t12Eligible` per record; count by `YES` / `NO` / `CONDITIONAL` |
| answerClass integrity | all values within the four T2 matrix values |
| EC-02 safety invariant | zero `BLOCKED_UNTIL_2026-07-01` records with `t12Eligible=YES` |
| Manifest additive | updated manifest parses; prior T11A fields retained |
| No extraction | worker return states no body parsing, OCR, ingestion, runtime, provider action |

## Execution Plan

1. Read required startup, roadmap T11-C section, T11B completion/result JSON,
   T11A candidate manifest, and T2 domain spec.
2. Capture `git rev-parse --short HEAD` and `git status --short`.
3. For each of the 6 corpus candidates:
   a. Resolve `documentType`, `currentStatus`, and `jurisdiction` from T11A
      manifest metadata only (no body read).
   b. Apply the T2 decision matrix to assign `domainCategory` and `answerClass`.
      Records with `currentStatus=unknown` or `jurisdiction=unknown` resolve to
      `ESCALATE_OR_ABSTAIN`.
   c. Assign `ec02Gate`. Records with `ec02Applies=true` and any current-law
      implication use `BLOCKED_UNTIL_2026-07-01`.
   d. Assign `t12Eligible`. Any record with
      `ec02Gate=BLOCKED_UNTIL_2026-07-01` must be `NO` or `CONDITIONAL`, never
      `YES`.
4. Classify `BNDL-006` as a non-corpus request artifact: `t12Eligible=NO`, no
   corpus answerClass.
5. Produce classification pre-check report (one row per record; 7 rows total).
6. Update the T11A candidate manifest with additive `classificationPreCheck`
   per candidate; do not remove any prior field.
7. Reconcile: 6 corpus candidate rows + 1 non-corpus row = 7; EC-02 count;
   t12-eligibility counts.
8. Produce worker return packet with all evidence.
9. Run local JSON parse and field-presence checks.

## Evidence Requirements

The worker must record:

- startup acknowledgment;
- pre-flight commands and results;
- per-record classification table with domainCategory, answerClass, ec02Gate,
  t12Eligible, and T2-matrix rationale;
- EC-02 gate accounting (count of `BLOCKED_UNTIL_2026-07-01`);
- t12-eligibility summary (count by `YES` / `NO` / `CONDITIONAL`);
- manifest additive-update evidence (fields added; prior fields retained);
- JSON parse result on updated manifest;
- changed files;
- explicit no-extraction/no-ingestion/no-provider/no-public-sync boundary.

## Review Gate

Codex must review the T11C worker return before deciding T11C closure. After
T11C closes, Codex may open the T11D Readiness Gate work order.

## Closure Checklist

- [ ] Classification pre-check report created (7 rows).
- [ ] Manifest updated with additive `classificationPreCheck` fields; prior
      fields retained.
- [ ] Every corpus candidate has non-empty `domainCategory`, `answerClass`,
      `ec02Gate`, and `t12Eligible`.
- [ ] `BNDL-006` row marks it a non-corpus request artifact with
      `t12Eligible=NO`.
- [ ] Zero `BLOCKED_UNTIL_2026-07-01` records marked `t12Eligible=YES`.
- [ ] All answerClass values within the four T2 matrix values.
- [ ] No forbidden scope action occurred.
- [ ] Codex reviewed worker return.

## Return-To-Orchestrator Conditions

Return to Codex without marking PASS if:

- the T11A candidate manifest or T11B result JSON is missing;
- classifying a record would require reading document body text;
- a record cannot be assigned an answerClass within the four T2 matrix values
  without a new vocabulary value;
- any forbidden path would need modification;
- the EC-02 safety invariant cannot be satisfied.

## Operator Checkpoint

Operator input is not required for classification pre-check execution. Operator
input is required before any later extraction, ingestion, runtime query,
provider call, public-sync, current-law claim, or legal advice quality claim.

## Acceptance Criteria

1. Classification pre-check report markdown exists, has exactly 7 rows
   (6 corpus candidates + `BNDL-006`), and passes markdown structural check.
2. Every corpus candidate has non-empty `domainCategory`, `answerClass`,
   `ec02Gate`, and `t12Eligible`.
3. `BNDL-006` has a row marking it a non-corpus request artifact with
   `t12Eligible=NO` and no corpus answerClass.
4. Zero candidates with `ec02Gate=BLOCKED_UNTIL_2026-07-01` carry
   `t12Eligible=YES`.
5. All `answerClass` values are one of: `DIRECT_CITED_ANSWER`,
   `SUMMARY_WITH_SOURCE`, `PROCEDURAL_GUIDANCE`, `ESCALATE_OR_ABSTAIN`.
   Records with `currentStatus=unknown` or `jurisdiction=unknown` are
   `ESCALATE_OR_ABSTAIN`.
6. The T11A candidate manifest is updated with additive `classificationPreCheck`
   fields and retains all prior T11A fields; the updated manifest parses.
7. Worker return records pre-flight output, the classification table, EC-02
   accounting, t12-eligibility summary, changed files, and claim boundary.
8. No forbidden scope action occurs.

## Fail Conditions

- missing T11A candidate manifest or T11B result JSON;
- a `BLOCKED_UNTIL_2026-07-01` record marked `t12Eligible=YES`;
- an answerClass value outside the four T2 matrix values;
- body extraction or legal-content evaluation;
- removal of any prior T11A manifest field;
- runtime/provider/public-sync claim;
- worker commit.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: DISPATCHED_TO_WORKER`; `Commit mode: WORKER_MUST_NOT_COMMIT` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_LPCI2_T11C_CLASSIFICATION_PRE_CHECK_COMPLETION_2026-06-07.md` | N/A with reason: completion authored by reviewer at closure, not at dispatch | N/A with reason |
| GC-018 baseline | `docs/baselines/CVF_GC018_LPCI2_T11C_POLICYLOCAL_CLASSIFICATION_PRE_CHECK_2026-06-07.md` | `Status: ACTIVE`; `baseHead: e18ec2f1` | PASS |
| Roadmap state | `docs/roadmaps/CVF_LPCI2_T11_POLICYLOCAL_CORPUS_EXPANSION_READINESS_ROADMAP_2026-06-07.md` | T11A/T11B closed; T11C dispatched; T11D open | PASS |
| Registry JSON | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | session sync recorded in the dispatch session-sync commit | PASS |
| Registry Markdown | `CVF_SESSION_MEMORY.md`; `AGENT_HANDOFF_V16_2026-06-06.md` | session sync recorded in the dispatch session-sync commit | PASS |
| External evidence digest | updated `policylocal-t11-candidate-manifest.json` | N/A with reason: manifest SHA-256 is recorded in the completion at closure, not at dispatch | N/A with reason |
| System loop interlock | this file | classification pre-check only; no runtime/system loop mutation authorized | PASS |
| Session continuity | `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `AGENT_HANDOFF_V16_2026-06-06.md` | session sync recorded in the dispatch session-sync commit | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private PolicyLocal candidate metadata and workspace paths are in scope.
No public-sync, public remote push, public catalog update, or public artifact
export is authorized.

## Text Encoding And Symbol Boundary

Agent-authored prose defaults to ASCII. Exact existing filenames and filesystem
paths may include Vietnamese Unicode characters and may be quoted only as source
evidence under the existing-filename exception in
`docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md`.

When printing file paths to console (Python), use
`sys.stdout.reconfigure(encoding='utf-8')` to prevent Windows cp1252 errors.

## Claim Boundary

This work order authorizes local classification pre-check only: T2-matrix
classification, EC-02 gate assignment, and t12-eligibility verdict bound to
T11B-verified records. It does not authorize document body parsing, OCR,
summarization, legal-content evaluation, corpus ingestion, chunking, search
runtime, memory reinjection, provider calls, public-sync, source authenticity
claims, current-law claims, legal advice quality claims, hosted readiness,
production readiness, public readiness, or release readiness.
