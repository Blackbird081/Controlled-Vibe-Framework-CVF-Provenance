# CVF LPCI2 EC-T4 Operator-Date Evidence Backfill Completion Review

Memory class: FULL_RECORD

Status: PARKED_PENDING_OPERATOR_METADATA

docType: completion_review

Date: 2026-06-11

Reviewer: Codex

Worker: Claude

WorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI2_EC_T4_OPERATOR_DATE_EVIDENCE_BACKFILL_FOR_CLAUDE_2026-06-11.md`

WorkerReturn: `docs/reviews/CVF_LPCI2_EC_T4_OPERATOR_DATE_EVIDENCE_WORKER_RETURN_2026-06-11.md`

Baseline: `docs/baselines/CVF_GC018_LPCI2_EC_T4_OPERATOR_DATE_EVIDENCE_BACKFILL_2026-06-11.md`

---

## Target / Source

Target: EC-T4 operator-date evidence and proposed metadata backfill for six
T11 PolicyLocal candidate records.

Source authority:

- EC-T4 GC-018 baseline;
- EC-T4 work order;
- EC-T3 schema closure;
- EC-T2 machine-readable EC-02 semantics;
- T11B source verification result in the external operator workspace.

## Scope / Target / Owner Boundary

In scope:

- review the three worker-return artifacts;
- repair reviewer-detected JSON shape mismatch inside the proposed backfill
  artifact;
- recompute source path, SHA-256, and size evidence for the six T11B
  candidate paths;
- park EC-T4 if metadata gaps remain.

Out of scope:

- external Policy_Local mutation;
- EC-T5 `QUERY_CLASS_GATED` update;
- runtime retrieval/disclosure behavior;
- corpus ingestion;
- provider/API-key use;
- public-sync;
- current-law, legal-quality, production, public, or release-readiness claim.

## Purpose

Record Codex reviewer disposition for the EC-T4 worker return and preserve the
operator checkpoint that blocks EC-T5.

## Scope / Methodology

Codex reviewed the worker ledger, proposed JSON, and worker return; reran JSON
parse and reviewer-fast; compared the proposed JSON to work-order-required
shape; recomputed source file hashes and sizes from T11B absolute paths; and
updated session continuity so the next allowed move remains blocked on
operator metadata.

## Review Verdict

Verdict: `PARKED_PENDING_OPERATOR_METADATA`.

EC-T4 produced useful bounded evidence but cannot release EC-T5. Four of six
records lack source-backed final dates or signed document identifiers. The
packet is accepted as a parked evidence packet only.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order requirement | Reviewed artifact | Reviewer disposition |
| --- | --- | --- | --- |
| EC-T4 per-project metadata backfill | Produce evidence ledger plus proposed JSON | ledger + JSON present | ACCEPT_AS_PARKED |
| Operator dates required | Mark missing/ambiguous values instead of guessing | 4 records `UNKNOWN_OR_AMBIGUOUS` | ACCEPT_AS_BLOCKER |
| Preserve EC-02 hard boundary through EC-T4 | Keep `BLOCKED_UNTIL_2026-07-01` | 6/6 records retain gate | PASS |
| No `IN_FORCE` before 2026-07-01 | Reject `IN_FORCE` proposals | JSON forbidden-value check PASS | PASS |
| No external Policy_Local mutation | Worker must not edit external workspace | changed files limited to private docs | PASS |

## Findings / Position

F-1: Data gap, not worker failure. CAND-002, CAND-004, CAND-005, and CAND-006
have blank or ambiguous date/number fields. Operator confirmation is required
before any metadata backfill can be accepted for those records.

F-2: Worker JSON shape initially diverged from the work order. The work order
required `schemaVersion=lpci2.ecT4.proposedMetadataBackfill.v1`, `records[]`,
`sourcePath`, `hashMatch`, `sizeMatch`, and `t12StillBlocked`. Worker output
used `lpci2.ec_t4...`, `proposedRecords[]`, and omitted the listed fields.
Codex repaired the JSON before commit.

F-3: Worker hash recomputation stopped mid-execution. Codex reviewer
recomputed SHA-256 and size for all six T11B candidate paths on 2026-06-11.
All six paths existed, all hashes matched T11B `computedHashSha256`, and all
sizes matched T11B `observedSizeBytes`.

Position: accept EC-T4 as parked evidence only. Do not release EC-T5.

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Ambiguous dates could be mistaken for current-law status | Park EC-T4 and require operator-confirmed signed dates/document numbers |
| JSON output shape drift could break downstream tooling | Reviewer repaired JSON and recorded machine-check candidate |
| Worker hash recomputation stopped | Reviewer recomputed SHA-256 and size for all six source paths |
| EC-T5 could start too early | Session state, handoff, roadmap, baseline, and work order now keep EC-T5 blocked |

## Codex Reviewer Correction

Corrected artifact:

`docs/reference/CVF_LPCI2_EC_T4_PROPOSED_METADATA_BACKFILL_2026-06-11.json`

Correction summary:

- normalized schemaVersion to `lpci2.ecT4.proposedMetadataBackfill.v1`;
- renamed top-level `proposedRecords` to `records`;
- added `sourcePath`, `hashMatch`, `sizeMatch`, and `t12StillBlocked` for all
  six records;
- changed hash revalidation method to `CODEX_RECOMPUTED_SHA256`.

## Hash Revalidation Evidence

Command class: PowerShell `Test-Path`, `Get-FileHash -Algorithm SHA256`, and
`Get-Item` over T11B `absolutePath` values.

| candidateId | path exists | hashMatch | sizeMatch |
| --- | --- | --- | --- |
| T11A-CAND-001 | true | true | true |
| T11A-CAND-002 | true | true | true |
| T11A-CAND-003 | true | true | true |
| T11A-CAND-004 | true | true | true |
| T11A-CAND-005 | true | true | true |
| T11A-CAND-006 | true | true | true |

## Evidence Outcome

| Outcome | Count | Records |
| --- | --- | --- |
| `SOURCE_EVIDENCED` | 2 | T11A-CAND-001, T11A-CAND-003 |
| `UNKNOWN_OR_AMBIGUOUS` | 4 | T11A-CAND-002, T11A-CAND-004, T11A-CAND-005, T11A-CAND-006 |
| `BLOCKED_FOR_CONFLICT` | 0 | N/A |
| `BLOCKED_FOR_HASH_OR_PATH` | 0 | N/A |

## Operator Checkpoint

Operator must supply or confirm final signed metadata before EC-T5:

- CAND-002: final issue date/document status for the project review report;
- CAND-004: parent notice number/date for the annex;
- CAND-005: final signed decision number/date and effective date if
  applicable;
- CAND-006: final signed notice number/date and relationship to TB
  591/TB-UBND.

CAND-001 and CAND-003 have source-evidenced dates but still require operator
type/status confirmation before downstream corpus mutation.

## Finding-To-Governance Learning Disposition

Defect class: `MACHINE_GATE_GAP`

Learning lane: `GOVERNANCE_CONTROL_PLANE`

Escalation state: `MACHINE_CHECK_CANDIDATE`

Runtime/provider/cost lane: `N/A_WITH_REASON` - finding is about reviewer
validation of governed JSON shape, not runtime/provider/cost behavior.

Next control action: add a future checker or reviewer-fast extension that
validates machine-readable worker output against work-order-declared JSON
shape for governed data artifacts. This EC-T4 review caught the mismatch
manually; future orchestrators should not have to spot it by hand.

## Claim Boundary

This review accepts EC-T4 only as a parked evidence packet. It does not claim
current-law correctness, legal advice quality, source authenticity, corpus
ingestion, retrieval readiness, EC-T5 gate behavior, `QUERY_CLASS_GATED`
profile adoption, T12 readiness, production readiness, public readiness, or
release readiness.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance review packet; no public-sync authorized.
