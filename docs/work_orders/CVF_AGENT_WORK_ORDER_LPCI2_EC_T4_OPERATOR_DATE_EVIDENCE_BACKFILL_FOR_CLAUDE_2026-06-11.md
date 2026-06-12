# CVF Agent Work Order: LPCI2 EC-T4 Operator-Date Evidence Backfill

Memory class: FULL_RECORD

Status: CLOSED_BLOCKED_BOUNDED

docType: work_order

Date: 2026-06-11

Worker: Claude

Reviewer: Codex

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `5296825c`

executionBaseHead: worker must capture before edits

closureBaseHead: `265c64dd`

completionReviewPath:

`docs/reviews/CVF_LPCI2_EC_T4_OPERATOR_DATE_EVIDENCE_BACKFILL_COMPLETION_2026-06-11.md`

---

## Purpose

Execute EC-T4 as a bounded operator-date evidence and proposed metadata
backfill tranche. The worker must revalidate the six T11 candidate files,
collect source-backed date/status/jurisdiction evidence, and produce reviewable
proposed metadata artifacts. The worker must not edit external Policy_Local
data, runtime source, DSCP profiles, or session files.

EC-T4 is not EC-T5. `ec02Gate` stays `BLOCKED_UNTIL_2026-07-01` through this
tranche.

Reviewer disposition on 2026-06-12: EC-T4 returned
`RETURNED_BLOCKED_METADATA_GAPS` and is complete as a bounded input-quality
assessment. Missing signed dates/document numbers for CAND-002, CAND-004,
CAND-005, and CAND-006 remain an operator evidence dependency. EC-T5 remains
unauthorized.

## Authority Chain

- Operator instruction: 2026-06-11, prepare EC-T4 path using EC-T3 completion
  evidence at `docs/reviews/CVF_LPCI2_EC_T3_CORPUS_RECORD_SCHEMA_UPDATE_COMPLETION_2026-06-11.md`
  and closure commit `54bfff3f`.
- Operator instruction: 2026-06-12, stop EX foundation expansion and complete
  EC-T4 as a bounded quality-test result before deeper Policy_Local work.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- Active handoff: `AGENT_HANDOFF_V17_2026-06-07.md`
- Roadmap:
  `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md`
- GC-018:
  `docs/baselines/CVF_GC018_LPCI2_EC_T4_OPERATOR_DATE_EVIDENCE_BACKFILL_2026-06-11.md`
- EC-T1 decision baseline:
  `docs/baselines/CVF_GC018_LPCI2_EC_T1_REGULATORY_DATE_MODEL_GOVERNANCE_DECISION_2026-06-11.md`
- EC-T2 machine semantics:
  `docs/reference/CVF_EC02_GATE_SEMANTICS_2026-06-11.json`
- EC-T3 closure:
  `docs/reviews/CVF_LPCI2_EC_T3_CORPUS_RECORD_SCHEMA_UPDATE_COMPLETION_2026-06-11.md`

Authority boundary:

- If this work order conflicts with any cited authority artifact, stop and
  return the conflict to Codex.

## Agent Roles

| Role | Agent | Responsibility |
| --- | --- | --- |
| Orchestrator / dispatcher | Codex | Author dispatch packet and review return |
| Worker | Claude | Execute EC-T4 evidence/backfill proposal only; do not commit |
| Reviewer | Codex | Review artifacts, run gates, commit if bounded PASS |
| Operator | Human | Required before EC-T5, public-sync, provider/key use, current-law claim, or accepting ambiguous date evidence |

## Intake Role Routing Decision

| Field | Decision |
| --- | --- |
| Intake summary | Operator asked Codex to switch roles and prepare the EC-T4 path for Claude using EC-T3 completion evidence at closure commit `54bfff3f`. |
| Scope classification | Bounded documentation/data-evidence tranche; no runtime behavior change. |
| Risk sensitivity | R2 because metadata can be misread as legal/current status if overclaimed. |
| Selected canonical route mode | MULTI_AGENT_MULTI_ROLE: Codex dispatches/reviews; Claude executes worker-return only. |
| Role separation basis | Worker gathers evidence and proposed backfill; reviewer validates claim boundary and gates before any commit. |
| Escalation condition | Any missing, ambiguous, conflicting, or unsupported date/status/jurisdiction evidence returns `UNKNOWN_OR_AMBIGUOUS`; no guessing. |

## Role Separation Control Note

N/A with reason: implementation and review roles are assigned to separate
agents. Claude is worker only; Codex owns review, closure, commit, and
session continuity.

## Scope / Target / Owner Boundary

Allowed worker scope:

- Create
  `docs/reference/CVF_LPCI2_EC_T4_OPERATOR_DATE_EVIDENCE_LEDGER_2026-06-11.md`.
- Create
  `docs/reference/CVF_LPCI2_EC_T4_PROPOSED_METADATA_BACKFILL_2026-06-11.json`.
- Create
  `docs/reviews/CVF_LPCI2_EC_T4_OPERATOR_DATE_EVIDENCE_WORKER_RETURN_2026-06-11.md`.
- Read external operator workspace files only for evidence:
  `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t11-candidate-manifest.json`,
  `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t11b-source-verification-result.json`,
  and the six hash-verified candidate source files named there.
- Read existing extracted text in the external `Law use case_Codex\_extracted_text`
  folder as auxiliary evidence only when the source hash is already verified
  and the ledger identifies the extracted text provenance boundary.

Forbidden worker scope:

- Do not edit anything under
  `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\**`.
- Do not edit `EXTENSIONS/**`, `docs/reference/CVF_EC02_GATE_SEMANTICS_2026-06-11.json`,
  `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-11.md`,
  T11 manifests, DSCP profiles, package manifests, lockfiles, public-sync,
  session files, handoffs, or active state.
- Do not change `ec02Gate` to `QUERY_CLASS_GATED`; EC-T5 owns that.
- Do not run provider/API-key calls, OCR model downloads, corpus ingestion,
  vector indexing, runtime retrieval, public-sync, or live governance proof.
- Do not claim legal advice quality, current-law status, source authenticity,
  hosted readiness, production readiness, public readiness, or release
  readiness.

Risk ceiling:

R2 evidence handling. Escalate if any evidence would require a legal/current
status judgment rather than metadata transcription.

## Reviewer Closure Conversion Block

Reviewer-owned closure paths:

- `docs/reviews/CVF_LPCI2_EC_T4_OPERATOR_DATE_EVIDENCE_BACKFILL_COMPLETION_2026-06-11.md`
- `docs/reference/CVF_LPCI2_EC_T4_OPERATOR_METADATA_GAP_REPORT_2026-06-12.md`
- `docs/reference/CVF_LPCI2_EC_T4_OPERATOR_METADATA_GAP_REPORT_2026-06-12.json`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI2_EC_T4_OPERATOR_DATE_EVIDENCE_BACKFILL_FOR_CLAUDE_2026-06-11.md`
- `docs/baselines/CVF_GC018_LPCI2_EC_T4_OPERATOR_DATE_EVIDENCE_BACKFILL_2026-06-11.md`
- `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V17_2026-06-07.md`

completionReviewPath: `docs/reviews/CVF_LPCI2_EC_T4_OPERATOR_DATE_EVIDENCE_BACKFILL_COMPLETION_2026-06-11.md`

reviewerOwnedClosurePaths:

- `docs/reviews/CVF_LPCI2_EC_T4_OPERATOR_DATE_EVIDENCE_BACKFILL_COMPLETION_2026-06-11.md`
- `docs/reference/CVF_LPCI2_EC_T4_OPERATOR_METADATA_GAP_REPORT_2026-06-12.md`
- `docs/reference/CVF_LPCI2_EC_T4_OPERATOR_METADATA_GAP_REPORT_2026-06-12.json`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI2_EC_T4_OPERATOR_DATE_EVIDENCE_BACKFILL_FOR_CLAUDE_2026-06-11.md`
- `docs/reviews/CVF_LPCI2_EC_T4_OPERATOR_DATE_EVIDENCE_WORKER_RETURN_2026-06-11.md`
- `docs/baselines/CVF_GC018_LPCI2_EC_T4_OPERATOR_DATE_EVIDENCE_BACKFILL_2026-06-11.md`
- `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V17_2026-06-07.md`

pendingStatusTokensAllowedBeforeReview: `COMPLETE_PENDING_REVIEW`,
`RETURNED_PASS_BOUNDED`, `RETURNED_BLOCKED_METADATA_GAPS`,
`RETURNED_BLOCKED_GUARD_FAILURE`

forbiddenClosedEquivalentResidue: resolved; no pending execution,
worker-return, or pre-closure markers remain as current state.

predecessorClosureFactSource: EC-T3 completion
`docs/reviews/CVF_LPCI2_EC_T3_CORPUS_RECORD_SCHEMA_UPDATE_COMPLETION_2026-06-11.md`

Claude must not create or edit the completion review unless later explicitly
authorized. Codex owns closure conversion, final gate reruns, commit, and
continuity sync.

## Required First Reads

| File | Purpose |
| --- | --- |
| `docs/baselines/CVF_GC018_LPCI2_EC_T4_OPERATOR_DATE_EVIDENCE_BACKFILL_2026-06-11.md` | Confirm EC-T4 authorization and boundary |
| `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | Confirm EC-T4 row and EC-T5 dependency |
| `docs/reference/CVF_EC02_GATE_SEMANTICS_2026-06-11.json` | Confirm boundary and `documentStatus` enum |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | Confirm EC-T3 schema fields |
| External T11 candidate manifest | Confirm six candidate records and current unknown status |
| External T11B source verification result | Confirm file path/hash/size evidence before reading candidate source files |

## Pre-Flight Checks

| Check | Command | Required result |
| --- | --- | --- |
| Base HEAD captured | `git rev-parse --short HEAD` | record as `executionBaseHead` |
| Work order status | inspect this file | `Status: DISPATCHED` |
| Candidate manifest exists | `Test-Path -LiteralPath <candidate manifest path>` | True |
| T11B verification result exists | `Test-Path -LiteralPath <t11b result path>` | True |
| EC-T4 evidence ledger absent | `Test-Path -LiteralPath docs/reference/CVF_LPCI2_EC_T4_OPERATOR_DATE_EVIDENCE_LEDGER_2026-06-11.md` | False |
| EC-T4 proposed JSON absent | `Test-Path -LiteralPath docs/reference/CVF_LPCI2_EC_T4_PROPOSED_METADATA_BACKFILL_2026-06-11.json` | False |
| EC-T4 worker return absent | `Test-Path -LiteralPath docs/reviews/CVF_LPCI2_EC_T4_OPERATOR_DATE_EVIDENCE_WORKER_RETURN_2026-06-11.md` | False |
| Pre-implementation gate | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 5296825c --head HEAD` | PASS before worker edits |

If a pre-flight check fails inside allowed scope, repair and rerun it. If
repair requires forbidden scope, stop and return a blocked diagnostic.

## Source Verification

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS: EC-T4 tranche | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | line 623 | `EC-T4` | parent roadmap work plan | ACCEPT |
| VALUE_SET: operator dates required | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | lines 623 and 700 | `promulgationDate`; `effectiveDate` | parent roadmap | ACCEPT |
| LITERAL_INVARIANT: EC-02 boundary active through EC-T4 | `docs/reference/CVF_EC02_GATE_SEMANTICS_2026-06-11.json` | lines 53-56 | `boundaryActiveThrough` | EC-T2 machine semantics | ACCEPT |
| LITERAL_INVARIANT: no `IN_FORCE` before 2026-07-01 | `docs/reference/CVF_EC02_GATE_SEMANTICS_2026-06-11.json` | line 55 | `noRecordMayReceive` | EC-T2 machine semantics | ACCEPT |
| LITERAL_INVARIANT: EC-T1 D-04 no exception | `docs/baselines/CVF_GC018_LPCI2_EC_T1_REGULATORY_DATE_MODEL_GOVERNANCE_DECISION_2026-06-11.md` | lines 230-250 | `D-04` | EC-T1 decision baseline | ACCEPT |
| EXISTS: EC-T3 `DocumentStatus` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | line 20 | `DocumentStatus` | LPCI TypeScript schema | ACCEPT |
| EXISTS: `LpciIndexRecord` lifecycle fields | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | lines 33 and 41-42 | `documentStatus`; `promulgationDate` | `LpciIndexRecord` | ACCEPT |
| EXISTS: `ManifestEntry` lifecycle fields | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | lines 112 and 120-121 | `documentStatus`; `promulgationDate` | `ManifestEntry` | ACCEPT |
| EXISTS: `supportsDocumentStatus` flag | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 53 | `supportsDocumentStatus` | `DscpDomainProfile` | ACCEPT |
| VALUE_SET: six T11 candidates | N/A with reason - external operator workspace artifact verified by `Test-Path` and SHA-256 in dispatch evidence | line 6 | `candidateCount` | `policylocal.candidateManifest.t11.v1` | ACCEPT |
| VALUE_SET: six candidates have unknown status and blocked EC-02 | N/A with reason - external operator workspace artifact verified by `Test-Path` and SHA-256 in dispatch evidence | lines 20, 30, 47, 57, 75, 85, 103, 113, 130, 140, 158, 168 | `currentStatus`; `ec02Gate` | T11 candidate manifest | ACCEPT |
| VALUE_SET: T11B has HASH_MATCH for six candidate files | N/A with reason - external operator workspace artifact verified by `Test-Path`; T11B hashes are revalidated by worker | lines 17, 51, 77, 103, 129, 155, 181 | `verificationResult` | T11B verification result | ACCEPT |
| EXISTS: EC-T4 next allowed move | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | line 213 | `nextAllowedMove` | active session registry | ACCEPT |

## Negative Search And Collision Discipline

EC-T4 must not introduce new runtime symbols. The proposed JSON fields are
doc-only evidence fields owned by this work order and must not be listed as
existing runtime fields.

| Token | Dispatch disposition |
| --- | --- |
| `QUERY_CLASS_GATED` | Existing EC-T2 semantics token only; forbidden in DSCP profile values during EC-T4 |

## Current Runtime Freshness Verification

Verified at reviewer closure base `265c64dd`.

Commands:

```powershell
rg -n "export type DocumentStatus|documentStatus\?|promulgationDate\?|effectiveDate\?" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts
rg -n --fixed-strings "QUERY_CLASS_GATED" EXTENSIONS
```

Observed result:

- EC-T3 lifecycle fields remain present in the current TypeScript owner.
- `QUERY_CLASS_GATED` remains absent from `EXTENSIONS/**`.
- EC-T4 remains documentation/data-evidence work only; no runtime
  implementation or hardcoded runtime behavior is claimed.
| `documentStatus=IN_FORCE` | Forbidden before 2026-07-01; worker must return blocked if detected as a proposed value |
| External extracted text | Auxiliary evidence only; not source authenticity proof |

## New Doc-Only Fields

The following fields are new documentation/evidence fields for the EC-T4
ledger and JSON only. They are not runtime schema claims.

| Field | Artifact | Meaning |
| --- | --- | --- |
| `operatorDateEvidenceState` | ledger + JSON | `SOURCE_EVIDENCED`, `UNKNOWN_OR_AMBIGUOUS`, or `BLOCKED_FOR_CONFLICT` |
| `evidencePointer` | ledger + JSON | Page, paragraph, line, heading, filename, or extracted-text line pointer |
| `evidenceSourceType` | ledger + JSON | `SOURCE_FILE`, `EXTRACTED_TEXT_AUXILIARY`, `FILENAME_ONLY`, or `NONE` |
| `operatorConfirmationRequired` | ledger + JSON | Always true unless Codex/operator later accepts the value |
| `proposedDocumentStatus` | JSON | `PROMULGATED` or `STATUS_UNKNOWN`; `IN_FORCE` forbidden in this tranche |
| `ec02GateRetained` | JSON | Must remain `BLOCKED_UNTIL_2026-07-01` |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| EC-T4 per-project metadata backfill | Execution Plan steps 1-5 | proposed backfill JSON with six records | JSON parse + record count = 6 | ASSIGNED |
| Operator dates required | Evidence Rules | ledger fields for date evidence and confirmation | no accepted date without evidence pointer | ASSIGNED |
| Preserve EC-02 hard boundary through EC-T4 | Forbidden scope and Acceptance Criteria | `ec02GateRetained` per record | grep JSON for `QUERY_CLASS_GATED` must find none | ASSIGNED |
| No `IN_FORCE` before 2026-07-01 | Acceptance Criteria | `proposedDocumentStatus` values | grep JSON for `IN_FORCE` must find none | ASSIGNED |
| Missing status/jurisdiction blocks T12 | Evidence Rules | `currentStatusCandidate`; `jurisdictionCandidate` | unknown values remain explicit blockers | ASSIGNED |

## Design Control Carry-Forward

| Design-control element | EC-T4 carry-forward |
| --- | --- |
| INTAKE | Operator requested next EC-T4 path using EC-T3 completion evidence at closure commit `54bfff3f`. |
| DESIGN | Preserve EC-02 boundary through EC-T4; collect evidence before EC-T5. |
| SPEC | Output ledger + proposed JSON schema defined in this work order. |
| WORK ORDER | Claude worker-return only; Codex reviews/closes. |
| BUILD | Create evidence artifacts only; no runtime or external workspace edits. |
| REVIEW | Codex validates hashes, evidence pointers, gate tokens, and boundary claims. |
| FREEZE | EC-T4 can close only with bounded metadata evidence; EC-T5 remains separate. |

## Execution Plan

### Step 1: Capture base and revalidate inputs

Record `executionBaseHead`. Load the candidate manifest and T11B verification
result. For each of the six candidate records:

- run `Test-Path -LiteralPath` on the T11B `absolutePath`;
- compute SHA-256 for the source file;
- compare to T11B `computedHashSha256`;
- stop that record with `BLOCKED_FOR_HASH_OR_PATH` if path or hash fails.

### Step 2: Inspect evidence sources

For each hash-verified candidate, inspect the source file and any matching
extracted-text auxiliary file. Record which evidence source was used.

Do not treat filename dates as sufficient for final date backfill. Filename
dates may be recorded as `FILENAME_ONLY` evidence and must keep
`operatorConfirmationRequired=true`.

### Step 3: Populate ledger

Create `docs/reference/CVF_LPCI2_EC_T4_OPERATOR_DATE_EVIDENCE_LEDGER_2026-06-11.md`
with one row per candidate and columns:

- `candidateId`
- `sourceHashSha256`
- `pathVerification`
- `promulgationDateCandidate`
- `effectiveDateCandidate`
- `jurisdictionCandidate`
- `currentStatusCandidate`
- `proposedDocumentStatus`
- `operatorDateEvidenceState`
- `evidenceSourceType`
- `evidencePointer`
- `operatorConfirmationRequired`
- `ec02GateRetained`
- `disposition`

### Step 4: Populate proposed JSON

Create `docs/reference/CVF_LPCI2_EC_T4_PROPOSED_METADATA_BACKFILL_2026-06-11.json`
with:

```json
{
  "schemaVersion": "lpci2.ecT4.proposedMetadataBackfill.v1",
  "generatedAt": "2026-06-11",
  "executionBaseHead": "<captured>",
  "sourceManifestSha256": "023F1276092756232949662E9BE6E635D545AB22B2BD19284F11F82789C7FD1A",
  "ec02GateRetained": "BLOCKED_UNTIL_2026-07-01",
  "records": []
}
```

Each `records[]` entry must include all ledger fields plus:

- `candidateFamily`
- `documentType`
- `sourcePath`
- `hashMatch`
- `sizeMatch` if available from T11B
- `t12StillBlocked`

### Step 5: Enforce status rules

Allowed `proposedDocumentStatus` values in EC-T4:

- `PROMULGATED`
- `STATUS_UNKNOWN`

Forbidden in EC-T4:

- `IN_FORCE`

If a document appears already effective, record the evidence in
`currentStatusCandidate`, keep `proposedDocumentStatus` as `PROMULGATED` or
`STATUS_UNKNOWN`, and mark `operatorConfirmationRequired=true`. EC-T5 or a
later operator-authorized tranche owns any transition to `IN_FORCE`.

### Step 6: Create worker return

Create `docs/reviews/CVF_LPCI2_EC_T4_OPERATOR_DATE_EVIDENCE_WORKER_RETURN_2026-06-11.md`
with:

- executionBaseHead;
- changed files;
- per-record summary;
- JSON parse result;
- hash revalidation summary;
- forbidden path scan;
- claim boundary;
- findings and learning disposition if any defects were found.

### Step 7: Stage but do not commit

Stage only the three worker-owned output files. Do not commit.

## Write Ownership

Claude owns writes only to:

- `docs/reference/CVF_LPCI2_EC_T4_OPERATOR_DATE_EVIDENCE_LEDGER_2026-06-11.md`
- `docs/reference/CVF_LPCI2_EC_T4_PROPOSED_METADATA_BACKFILL_2026-06-11.json`
- `docs/reviews/CVF_LPCI2_EC_T4_OPERATOR_DATE_EVIDENCE_WORKER_RETURN_2026-06-11.md`

Everything else is read-only unless Codex later assigns a separate repair
order.

## Worker Autonomy / No-Question Rule

The worker proceeds without operator confirmation for non-destructive actions
inside this work order's Allowed scope.

Proceed autonomously with:

- reading the files named by this work order;
- running `git status`, `git diff`, `git rev-parse`, JSON parse checks,
  `Test-Path`, SHA-256 hashing, and listed governance gates;
- completing evidence tables and formatting remediation inside Allowed scope;
- rerunning failed gates after allowed-scope remediation.

Escalate only when the repair would exceed Allowed scope, edit forbidden
paths, run live/provider proof, use secrets/quota, public-sync, push/publish,
change risk or claim boundary, release EC-T5, or perform destructive action.

If a machine gate fails inside Allowed scope, repair and rerun it before
returning the packet.

## Evidence Requirements

The worker return must include:

1. `executionBaseHead`.
2. `git status --short` after staging.
3. `git diff --name-status --cached`.
4. JSON parse proof for the proposed backfill file.
5. Per-candidate hash revalidation summary.
6. Count of `SOURCE_EVIDENCED`, `UNKNOWN_OR_AMBIGUOUS`, and
   `BLOCKED_FOR_CONFLICT` records.
7. Forbidden path scan confirming no external workspace, runtime source,
   session, or public-sync edits.
8. Claim boundary and finding-to-governance learning disposition for any
   defect.

## Review Gate

Before return, run:

```bash
python -m json.tool docs/reference/CVF_LPCI2_EC_T4_PROPOSED_METADATA_BACKFILL_2026-06-11.json
python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast
```

If reviewer-fast fails on artifacts inside worker ownership, repair and rerun.
If it fails because Codex-owned session/closure files are not yet updated,
record the failure as reviewer-owned finality and return the packet.

## Closure Checklist

- [x] Three worker-owned files were created and reviewed.
- [x] Proposed metadata and operator-gap JSON artifacts parse successfully.
- [x] Exactly six candidate records are present.
- [x] All six records retain `BLOCKED_UNTIL_2026-07-01`.
- [x] No record proposes `IN_FORCE`.
- [x] Hash/path revalidation is recorded for each candidate.
- [x] Missing or ambiguous evidence is explicitly marked.
- [x] No forbidden paths were modified.
- [x] Worker return includes claim boundary and learning disposition.

## Return-To-Orchestrator Conditions

Return `RETURNED_PASS_BOUNDED` only if all acceptance criteria pass.

Return `RETURNED_BLOCKED_METADATA_GAPS` if any candidate lacks enough evidence
for a proposed date/status/jurisdiction value. This is an acceptable EC-T4
outcome; do not invent values to avoid a blocked return.

Return `RETURNED_BLOCKED_GUARD_FAILURE` if an allowed-scope guard failure
cannot be repaired.

## Operator Checkpoint

Operator confirmation remains required before:

- accepting any ambiguous or filename-only date evidence as final;
- moving any record to `documentStatus=IN_FORCE`;
- opening EC-T5;
- modifying external Policy_Local data;
- making current-law, legal-quality, production, public, or release claims.

## Work-Order Fulfillment Manifest

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
| --- | --- | --- |
| `docs/reference/CVF_LPCI2_EC_T4_OPERATOR_DATE_EVIDENCE_LEDGER_2026-06-11.md` | No (worker creates) | Human-readable date/status/jurisdiction evidence ledger |
| `docs/reference/CVF_LPCI2_EC_T4_PROPOSED_METADATA_BACKFILL_2026-06-11.json` | No (worker creates) | Machine-readable proposed backfill artifact |
| `docs/reviews/CVF_LPCI2_EC_T4_OPERATOR_DATE_EVIDENCE_WORKER_RETURN_2026-06-11.md` | No (worker creates) | Worker return packet |
| `docs/reference/CVF_LPCI2_EC_T4_OPERATOR_METADATA_GAP_REPORT_2026-06-12.md` | Reviewer creates at closure | Operator-readable correction checklist |
| `docs/reference/CVF_LPCI2_EC_T4_OPERATOR_METADATA_GAP_REPORT_2026-06-12.json` | Reviewer creates at closure | Machine-readable operator checkpoint |

## Forbidden Path Manifest

| Path | Reason |
| --- | --- |
| `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\**` | External workspace is read-only in this tranche |
| `EXTENSIONS/**` | No runtime/source/schema change in EC-T4 |
| `docs/reference/CVF_EC02_GATE_SEMANTICS_2026-06-11.json` | EC-T2 semantics are not edited by EC-T4 |
| `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-11.md` | Contract already closed at EC-T2 |
| `docs/corpus-intelligence/**` | No corpus registry change in EC-T4 |
| `CVF_SESSION/**` | Reviewer-owned session continuity only |
| `AGENT_HANDOFF_V17_2026-06-07.md` | Reviewer-owned handoff only |
| `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync\**` | No public-sync authorized |

## Forbidden Filesystem State At Dispatch

This is the preserved dispatch boundary. Existing owner surfaces were present
and exempted as read-only; worker-created outputs were absent at dispatch.

| Forbidden path | Expected state | Actual state at dispatch | Action if PRESENT |
| --- | --- | --- | --- |
| `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\**` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Read evidence only; do not edit, stage, or claim |
| `EXTENSIONS/**` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Do not edit runtime/source |
| `docs/reference/CVF_EC02_GATE_SEMANTICS_2026-06-11.json` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Read-only EC-T2 authority |
| `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-11.md` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Read-only contract |
| `docs/corpus-intelligence/**` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | No registry mutation |
| `CVF_SESSION/**` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Reviewer-owned only |
| `AGENT_HANDOFF_V17_2026-06-07.md` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | Reviewer-owned only |
| `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync\**` | PRESENT_EXEMPTED | PRESENT_EXEMPTED | No public-sync |

## Acceptance Criteria

1. Exactly three worker-owned files are created and staged.
2. Proposed JSON parses successfully.
3. Proposed JSON contains exactly six records matching `T11A-CAND-001`
   through `T11A-CAND-006`.
4. Each record includes path/hash verification fields and `hashMatch=true`.
5. Each proposed date/status/jurisdiction value has an evidence pointer or is
   explicitly `unknown` / `UNKNOWN_OR_AMBIGUOUS`.
6. No record proposes `documentStatus=IN_FORCE`.
7. Every record retains `ec02GateRetained: "BLOCKED_UNTIL_2026-07-01"`.
8. `QUERY_CLASS_GATED` appears only as a forbidden/not-yet-active token if
   mentioned at all.
9. No external Policy_Local files are modified.
10. No runtime/source/session/public-sync files are modified.
11. Worker return includes claim boundary and finding-to-governance learning
    disposition for any defect.

## Worker Return Summary Required

At return, say:

`EC-T4 Worker Return -- <RETURNED_PASS_BOUNDED|RETURNED_BLOCKED_METADATA_GAPS|RETURNED_BLOCKED_GUARD_FAILURE>`

Then include:

- executionBaseHead;
- three staged files;
- JSON parse status;
- candidate count;
- count of `SOURCE_EVIDENCED`, `UNKNOWN_OR_AMBIGUOUS`, and
  `BLOCKED_FOR_CONFLICT`;
- forbidden path scan result;
- explicit next required Codex action.

## Claim Boundary

EC-T4 may claim only that evidence was collected and proposed metadata was
prepared for Codex/operator review. It must not claim current-law correctness,
legal advice quality, source authenticity, retrieval readiness, T12 readiness,
EC-T5 gate behavior, public readiness, production readiness, or release
readiness.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | `Status: CLOSED_BLOCKED_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_LPCI2_EC_T4_OPERATOR_DATE_EVIDENCE_BACKFILL_COMPLETION_2026-06-11.md` | matching closed-bounded status | PASS |
| Roadmap state | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | EC-T4 row closed blocked bounded | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | no corpus registry mutation authorized for metadata reporting | BLOCKED with reason: no corpus/source registration changed |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | no corpus registry mutation authorized for metadata reporting | BLOCKED with reason: no corpus/source registration changed |
| Proposed metadata JSON | `docs/reference/CVF_LPCI2_EC_T4_PROPOSED_METADATA_BACKFILL_2026-06-11.json` | six records; retained EC-02 gate | PASS |
| Operator gap JSON | `docs/reference/CVF_LPCI2_EC_T4_OPERATOR_METADATA_GAP_REPORT_2026-06-12.json` | parseable six-record checkpoint | PASS |
| External evidence digest | proposed metadata JSON and operator gap JSON | sha256:cd4fd3d2896fee19bd46ef9da5147a05f806f7fc4e29965554371c6fd4da903b; sha256:e9615e977ad77428de4a8006223746c7a1ba425491736b7e0e8a9f7e68839e04 | PASS |
| System loop interlock | no system-loop mutation | N/A with reason: evidence/report closure only | PASS |
| Runtime/source registry | runtime source tree | N/A with reason: EC-T4 does not change runtime/source | PASS |
| External Policy_Local | external operator workspace | N/A with reason: read-only evidence source; no mutation authorized | PASS |
| Public-sync | public-sync clone | N/A with reason: no public export authorized | PASS |
| Session continuity | state, memory, and active handoff | reviewer-owned final sync | PASS |

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order; no public-sync authorized.
