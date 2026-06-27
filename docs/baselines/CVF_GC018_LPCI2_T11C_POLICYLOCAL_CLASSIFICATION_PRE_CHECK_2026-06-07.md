# CVF GC-018 LPCI2-T11C PolicyLocal Classification Pre-Check

Memory class: FULL_RECORD

Status: ACTIVE

docType: gc018_baseline

Date: 2026-06-07

baseHead: `e18ec2f1`

## Purpose

Authorize the LPCI2-T11C Classification Pre-Check work order after T11B
four-gate source verification closed `CLOSED_PASS_BOUNDED` at material commit
`acdbcd8b` with 7/7 `verificationResult=HASH_MATCH`.

T11C classifies only the T11B-verified candidate records against the T2 domain
classification matrix, the EC-02 freshness gate, and a T12-eligibility verdict.
It consumes the T11B resolved-path evidence and carries the Unicode
path-fidelity finding forward so classification metadata is bound to verified
paths, not to T11A candidate `readableAt` literals alone.

T11C does not extract document body content, ingest corpus records, run runtime
queries, call providers, or make current-law or production readiness claims.

## Scope / Target / Owner Boundary

Target records: the 6 T11B-verified direct candidate records
(`T11A-CAND-001` through `T11A-CAND-006`). The seventh T11B-verified record,
`BNDL-006` (`agent_request`, `Request for agent.docx`), is classified only as
a non-corpus request artifact with `t12Eligible=NO` and is not assigned a
corpus answerClass.

Owner boundary: the worker may produce a classification pre-check report and a
manifest update with `classificationPreCheck` fields. Codex or the operator
remains reviewer/closer. T11C does not authorize T11D readiness verdict, T12
ingestion, runtime changes, public-sync, or live proof.

## Decision / Baseline / Proposed Tranche

T11B closed at `lpci2_t11b_source_verification_closed_pass_bounded`.
`nextAllowedMove` in `CVF_SESSION/ACTIVE_SESSION_STATE.json` at baseHead
`e18ec2f1` authorizes authoring a source-verified T11C Classification
Pre-Check work order.

The T11 roadmap sub-tranche T11-C (lines 212-250 of
`docs/roadmaps/CVF_LPCI2_T11_POLICYLOCAL_CORPUS_EXPANSION_READINESS_ROADMAP_2026-06-07.md`)
defines the T11C deliverables, scope boundary, and acceptance criteria. This
GC-018 inherits that contract.

Operator instruction 2026-06-07: next road is T11C Classification Pre-Check;
classify the 7 file-records per role/lineage/source authority before any
ingestion/chunking/query runtime is allowed in.

## Source / Predecessor Evidence

| Evidence | Path / source | Disposition |
|---|---|---|
| T11B closure mode | `CVF_SESSION/ACTIVE_SESSION_STATE.json` `currentMode` | ACCEPT |
| T11B `nextAllowedMove` | `CVF_SESSION/ACTIVE_SESSION_STATE.json` `nextAllowedMove` | ACCEPT |
| T11B completion | `docs/reviews/CVF_LPCI2_T11B_SOURCE_VERIFICATION_COMPLETION_2026-06-07.md` | ACCEPT |
| T11B source verification report | `docs/reference/CVF_LPCI2_T11B_SOURCE_VERIFICATION_REPORT_2026-06-07.md` | ACCEPT |
| T11B result JSON (resolved paths) | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t11b-source-verification-result.json` | ACCEPT |
| T11A candidate manifest | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t11-candidate-manifest.json` | ACCEPT |
| T11A bundle manifest | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t11-real-use-case-bundle-manifest.json` | ACCEPT |
| T2 domain classification spec | `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` | ACCEPT |
| T11 roadmap | `docs/roadmaps/CVF_LPCI2_T11_POLICYLOCAL_CORPUS_EXPANSION_READINESS_ROADMAP_2026-06-07.md` | ACCEPT |
| Text encoding standard | `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md` | ACCEPT |

## Target Record List

### Corpus candidates (classified against T2 matrix)

| Candidate ID | candidateFamily | documentType | currentStatus | ec02Applies |
|---|---|---|---|---|
| `T11A-CAND-001` | `applied_policy_record` | `other` | `unknown` | true |
| `T11A-CAND-002` | `project_case_record` | `other` | `unknown` | true |
| `T11A-CAND-003` | `applied_policy_record` | `other` | `unknown` | true |
| `T11A-CAND-004` | `project_case_record` | `other` | `unknown` | true |
| `T11A-CAND-005` | `administrative_decision` | `decision` | `unknown` | true |
| `T11A-CAND-006` | `administrative_notice` | `notice` | `unknown` | true |

### Non-corpus record (request artifact)

| Bundle ID | Role | Disposition |
|---|---|---|
| `BNDL-006` | `agent_request` | Non-corpus request artifact; `t12Eligible=NO`; no corpus answerClass assigned |

## Work Plan

1. Read required startup front doors, this GC-018, the T11 roadmap T11-C
   section, the T11B completion/report/result JSON, and the T2 domain spec.
2. Capture `git rev-parse --short HEAD` and `git status --short`.
3. For each of the 6 corpus candidates, consume the T11B-resolved path and
   classify (no body read; metadata-only):
   a. Domain category and expected `answerClass` from the T2 matrix, using
      `documentType`, `currentStatus`, and `jurisdiction` rules. Records with
      `currentStatus=unknown` or `jurisdiction=unknown` must resolve to
      `ESCALATE_OR_ABSTAIN` per T2 spec.
   b. `ec02Gate`: one of `BLOCKED_UNTIL_2026-07-01` / `PASSES_EC02` /
      `REQUIRES_REVIEW`. Records with `ec02Applies=true` and any current-law
      implication must use `BLOCKED_UNTIL_2026-07-01`.
   c. `t12Eligible`: one of `YES` / `NO` / `CONDITIONAL`. Any record with
      `ec02Gate=BLOCKED_UNTIL_2026-07-01` must not be `t12Eligible=YES`.
4. Classify `BNDL-006` as a non-corpus request artifact with `t12Eligible=NO`.
5. Produce the classification pre-check report markdown (one row per record).
6. Update the T11A candidate manifest with additive `classificationPreCheck`
   fields per candidate, without removing any prior T11A field.
7. Produce a worker return packet with evidence, reconciliation, and claim
   boundary.
8. Return artifacts to Codex uncommitted.

## Unicode Path Fidelity Carry-Forward

The T11B completion recorded that three T11A candidate manifest paths
(`T11A-CAND-002`, `T11A-CAND-003`, `T11A-CAND-005`) required Unicode fallback
through the T11A bundle manifest before resolving. T11C must consume the
T11B result JSON resolved paths for those records and must not re-derive paths
from T11A candidate `readableAt` literals alone. All filesystem calls, if any,
must use `-LiteralPath`.

## Acceptance Criteria

1. Classification pre-check report markdown exists and passes the markdown
   structural check.
2. Every corpus candidate (6) has a row with non-empty domain category,
   `answerClass`, `ec02Gate`, and `t12Eligible`.
3. `BNDL-006` has a row marking it a non-corpus request artifact with
   `t12Eligible=NO` and no corpus answerClass.
4. Zero candidates with `ec02Gate=BLOCKED_UNTIL_2026-07-01` carry
   `t12Eligible=YES`.
5. All `answerClass` values match the T2 matrix vocabulary only:
   `DIRECT_CITED_ANSWER`, `SUMMARY_WITH_SOURCE`, `PROCEDURAL_GUIDANCE`,
   `ESCALATE_OR_ABSTAIN`. Records with `currentStatus=unknown` or
   `jurisdiction=unknown` are `ESCALATE_OR_ABSTAIN`.
6. The T11A candidate manifest is updated with additive `classificationPreCheck`
   fields and retains all prior T11A fields.
7. Worker return records commands, counts, classification rationale per record,
   changed files, and claim boundary.
8. No forbidden scope action occurs.

## Verification / Evidence

Required evidence in worker return:

- `git rev-parse --short HEAD`
- `git status --short`
- per-record classification table (domain category, answerClass, ec02Gate,
  t12Eligible) with T2-matrix rationale
- EC-02 gate accounting (count of `BLOCKED_UNTIL_2026-07-01`)
- t12-eligibility summary (count by `YES` / `NO` / `CONDITIONAL`)
- manifest update evidence (additive fields only; prior fields retained)
- JSON parse check on the updated manifest
- changed-file evidence
- explicit no-extraction/no-ingestion/no-provider/no-public-sync boundary

## Claim Boundary

This GC-018 authorizes T11C classification pre-check only. T11C classifies
candidate records against the T2 matrix and EC-02 gate using metadata and
T11B-verified path evidence. It does not prove document body readability, text
correctness, legal authority, source authenticity, current-law status, legal
advice quality, extraction quality, chunking readiness, search behavior,
provider behavior, hosted readiness, production readiness, public readiness, or
release readiness.

EC-02 freshness review remains required on or after 2026-07-01 before any
current-law or production runtime claim for any PolicyLocal corpus material.
Until then, no candidate may be promoted to `t12Eligible=YES` on the basis of a
current-law reading.

## Non-Goals

No extraction, OCR, PDF parsing, DOCX body parsing, ingestion, chunking,
runtime query execution, vector retrieval, provider call, public-sync, T11D
readiness verdict, T12 ingestion, or mutation of existing T9/T10/T11A/T11B
generated corpus, chunks, receipts, scripts, or readiness reports beyond the
single additive manifest update authorized above.
