# CVF GC-018 LPCI2 EC-T4 Operator-Date Evidence Backfill Baseline

Memory class: FULL_RECORD

Status: DISPATCHED

docType: baseline

Date: 2026-06-11

dispatchBaseHead: `5296825c`

---

## Purpose

Authorize LPCI2 EC-T4 as a bounded operator-date evidence and proposed
metadata-backfill tranche. EC-T4 may inspect the six PolicyLocal T11 candidate
records, revalidate their T11B file hashes, and produce a date/status evidence
ledger plus a proposed metadata backfill JSON for Codex review.

This tranche does not change runtime behavior, DSCP profile gate values,
external Policy_Local data, corpus ingestion state, retrieval behavior, or
public-facing documentation.

## Authorization

Operator instruction on 2026-06-11 authorized Codex to prepare the next
allowed EC-T4 path for Claude after EC-T3 closure.

Active state:

`CVF_SESSION/ACTIVE_SESSION_STATE.json`

Active handoff:

`AGENT_HANDOFF_V17_2026-06-07.md`

## Decision

Open EC-T4 as a worker-return tranche for source-backed date evidence and
proposed metadata backfill only. Claude must run in `WORKER_MUST_NOT_COMMIT`
mode and return staged/uncommitted artifacts for Codex review.

EC-T4 is allowed to propose `promulgationDate`, `effectiveDate`,
`documentStatus`, `jurisdiction`, and `currentStatus` values only when every
value is tied to a file-hash-verified source and a specific evidence pointer.
When evidence is missing or ambiguous, the worker must output an explicit
`UNKNOWN_OR_AMBIGUOUS` disposition rather than guessing.

## Predecessor Evidence

| Predecessor | Closure evidence | Disposition |
| --- | --- | --- |
| EC-T1 decision baseline | `docs/baselines/CVF_GC018_LPCI2_EC_T1_REGULATORY_DATE_MODEL_GOVERNANCE_DECISION_2026-06-11.md`; D-04 confirms `BLOCKED_UNTIL_2026-07-01` remains active through EC-T4 | ACCEPT |
| EC-T2 machine semantics | `docs/reference/CVF_EC02_GATE_SEMANTICS_2026-06-11.json`; boundary active through EC-T4 inclusive | ACCEPT |
| EC-T3 schema support | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts`; material commit `a895dc03`; closure commit `54bfff3f` | ACCEPT |
| T11D readiness gate | `CVF_SESSION/ACTIVE_SESSION_STATE.json`; six candidates remained conditional because `currentStatus` and `jurisdiction` were unknown | ACCEPT |
| T11B source verification | External operator workspace result `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-t11b-source-verification-result.json`; 7/7 `HASH_MATCH` | ACCEPT |
| Parent roadmap | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md`; EC-T4 row requires operator dates | ACCEPT |

## Scope / Target / Owner Boundary

In scope:

- Revalidate the six T11 candidate source files against T11B hash evidence.
- Read the six source files and available operator-supplied/previously generated
  text evidence only to locate date/status/jurisdiction evidence.
- Create a Markdown evidence ledger for each candidate.
- Create a proposed metadata backfill JSON for each candidate.
- Create a worker return packet.

Out of scope:

- No edits to `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\**`.
- No edits to runtime source, DSCP profiles, corpus generated data, retrieval
  logic, EC-T2 semantics JSON, EC-T3 schema files, package manifests, lockfiles,
  public-sync, or session continuity files.
- No `ec02Gate` value change to `QUERY_CLASS_GATED`; that remains EC-T5.
- No corpus ingestion, OCR model download, vector index, provider/API-key use,
  live proof, legal advice, current-law claim, production readiness, public
  readiness, memory reinjection, high-risk promotion, or autonomous mutation.

## Source Verification Summary

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS: EC-T4 tranche | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | line 623 | `EC-T4` | parent roadmap work plan | ACCEPT |
| VALUE_SET: EC-T4 depends on operator dates | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | lines 623 and 700 | `operator dates`; `promulgationDate`; `effectiveDate` | parent roadmap | ACCEPT |
| LITERAL_INVARIANT: EC-02 boundary active through EC-T4 inclusive | `docs/reference/CVF_EC02_GATE_SEMANTICS_2026-06-11.json` | lines 53-56 | `boundaryActiveThrough` | EC-T2 machine semantics | ACCEPT |
| LITERAL_INVARIANT: no `documentStatus=IN_FORCE` before 2026-07-01 | `docs/reference/CVF_EC02_GATE_SEMANTICS_2026-06-11.json` | line 55 | `noRecordMayReceive` | EC-T2 machine semantics | ACCEPT |
| LITERAL_INVARIANT: EC-T1 D-04 keeps hard boundary through EC-T4 | `docs/baselines/CVF_GC018_LPCI2_EC_T1_REGULATORY_DATE_MODEL_GOVERNANCE_DECISION_2026-06-11.md` | lines 230-250 | `D-04` | EC-T1 decision baseline | ACCEPT |
| EXISTS: EC-T3 `DocumentStatus` type | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | line 20 | `DocumentStatus` | LPCI TypeScript schema | ACCEPT |
| EXISTS: EC-T3 `LpciIndexRecord` lifecycle fields | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | lines 33 and 41-42 | `LpciIndexRecord.documentStatus`; `promulgationDate` | LPCI TypeScript schema | ACCEPT |
| EXISTS: EC-T3 `ManifestEntry` lifecycle fields | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | lines 112 and 120-121 | `ManifestEntry.documentStatus`; `promulgationDate` | LPCI TypeScript schema | ACCEPT |
| EXISTS: profile support flag | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 53 | `supportsDocumentStatus` | `DscpDomainProfile` | ACCEPT |
| VALUE_SET: T11 candidate count is 6 | N/A with reason - external operator workspace artifact verified by `Test-Path` and SHA-256 in dispatch evidence | line 6 | `candidateCount` | `policylocal.candidateManifest.t11.v1` | ACCEPT |
| VALUE_SET: all six candidates have `currentStatus=unknown` and blocked EC-02 gate | N/A with reason - external operator workspace artifact verified by `Test-Path` and SHA-256 in dispatch evidence | lines 20, 30, 47, 57, 75, 85, 103, 113, 130, 140, 158, 168 | `currentStatus`; `ec02Gate` | T11 candidate manifest | ACCEPT |
| VALUE_SET: T11B source verification has HASH_MATCH for candidate files | N/A with reason - external operator workspace artifact verified by `Test-Path`; T11B hashes are revalidated by worker | lines 17, 51, 77, 103, 129, 155, 181 | `verificationSummary`; `verificationResult` | T11B source verification result | ACCEPT |
| EXISTS: active state names EC-T4 as next allowed move | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | line 213 | `nextAllowedMove` | active session registry | ACCEPT |

## Evidence / Verification

| Evidence | Required result |
| --- | --- |
| Work order status | `DISPATCHED` before Claude execution |
| Worker return mode | `WORKER_MUST_NOT_COMMIT` |
| Hash revalidation | six candidate files revalidated against T11B SHA-256 before any date evidence is accepted |
| Date evidence ledger | Markdown table with one row per candidate and evidence pointer per proposed value |
| Proposed backfill JSON | JSON parse PASS and exactly six records |
| Boundary scan | no `documentStatus=IN_FORCE` value before 2026-07-01 unless explicitly marked `FORBIDDEN_VALUE_DETECTED` and returned blocked |
| Forbidden path scan | no external Policy_Local edit, runtime source edit, public-sync edit, or DSCP gate value update |

## Claim Boundary

This baseline authorizes only source-backed evidence collection and proposed
metadata backfill for EC-T4. It does not prove current-law status, legal advice
quality, retrieval correctness, EC-T5 gate behavior, corpus ingestion,
provider behavior, hosted readiness, production readiness, public readiness,
public-sync, memory reinjection, high-risk promotion, Learning Orchestrator
runtime behavior, or autonomous mutation.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch baseline; no public-sync authorized.
