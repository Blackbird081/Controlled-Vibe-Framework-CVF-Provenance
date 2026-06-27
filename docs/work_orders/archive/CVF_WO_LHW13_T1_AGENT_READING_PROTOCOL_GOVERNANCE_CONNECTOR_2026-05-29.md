# CVF Work Order — LHW13-T1 Agent Reading Protocol Governance Connector

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-05-29

---

## Purpose

Implement LHW13-T1: a connector spec mapping connector-normalized CVF
claim-tier vocabulary
(`roadmap`/`schema_defined`/`active`/`proven`) × canonical-file-type
(`session_front_door`/`gc018_baseline`/`completion_review`/`runtime_source`) ×
startup acknowledgment status →
`agentReadingAdvisoryType` + `claimValidationAdvisory`.

Source: CVF 25.05 Gop_y.md Gap 1 — CLAUDE.md and AGENTS.md cover reading rules
piecemeal; no connector maps claim-tier × canonical-file-type → a named
advisory that Orchestrators can use to validate agent claims before acting.
An agent claiming "X is proven" should trigger a different reading advisory
than an agent claiming "X is roadmap."

This connector is advisory only. It does NOT enforce agent behavior at runtime.
`runtimeExecutionAuthorized=false` invariant.

## Authority Chain

- LHW13 roadmap: `docs/roadmaps/CVF_LHW13_WORKFLOW_CONNECTOR_WAVE13_ROADMAP_2026-05-29.md`
- LHW13 GC-018: `docs/baselines/CVF_GC018_LHW13_WORKFLOW_CONNECTOR_WAVE13_2026-05-29.md`
- CLAUDE.md: `CLAUDE.md` — Mandatory Startup Acknowledgment + Required First Reads
- Session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json` — `requiredFirstReads` at line 80
- CVF Release Readiness: `docs/reference/CVF_RELEASE_READINESS_STATUS_2026-03-20.md`
  — source status vocabulary to be normalized into doc-only claim tiers
- CVF 25.05 review: `.private_reference/legacy/CVF 25.05/CLAUDE_REVIEW_OF_GOP_Y_2026-05-25.md`
  — GAP 1 section

## Agent Roles

Implementer writes spec (S1–S5). Reviewer checks: all 4 connector-normalized
claim-tier values covered in S5; all 4 canonical-file-type values individually
row-verified; startup acknowledgment axis included;
`runtimeExecutionAuthorized=false` explicit; no runtime agent
enforcement claimed. Auditor confirms CVF 25.05 Gap 1 cited; advisory-only
posture preserved. No self-review.

## Scope

**Allowed:**

- `docs/reference/CVF_LHW13_T1_AGENT_READING_PROTOCOL_GOVERNANCE_CONNECTOR_SPEC_2026-05-29.md` (new)
- `docs/reviews/CVF_LHW13_T1_FAST_LANE_AUDIT_2026-05-29.md` (new)
- `docs/reviews/CVF_LHW13_T1_AGENT_READING_PROTOCOL_GOVERNANCE_CONNECTOR_COMPLETION_2026-05-29.md` (new)
- this work order (status update only)
- session continuity files

**Forbidden:** `EXTENSIONS/`, `governance/contracts/`, `CLAUDE.md` (read-only
reference), any `.ts`/`.tsx`/`.js`/`.py` file, receipt envelope schema,
public-sync repo.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json` — note `requiredFirstReads` field at line 80
3. `CLAUDE.md` — read Mandatory Startup Acknowledgment section; note canonical
   file priority: CVF_SESSION_MEMORY.md then ACTIVE_SESSION_STATE.json
4. `docs/reference/CVF_RELEASE_READINESS_STATUS_2026-03-20.md`
   — note source status vocabulary such as `ALIGNED`,
   `SUBSTANTIALLY ALIGNED`, and `ALIGNED WITH CAVEATS`; normalize into
   connector doc-only claim tiers only in the connector spec
5. `.private_reference/legacy/CVF 25.05/CLAUDE_REVIEW_OF_GOP_Y_2026-05-25.md`
   — confirm GAP 1 section: no single agent reading protocol doc exists yet
6. `docs/roadmaps/CVF_LHW13_WORKFLOW_CONNECTOR_WAVE13_ROADMAP_2026-05-29.md`
   — confirm T1 deliverable and claim-tier mapping design

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `requiredFirstReads` field | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | line 80 | `requiredFirstReads` | session state registry | ACCEPT |
| `startupAcknowledgmentRequired` field | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | line 107 | `startupAcknowledgmentRequired` | session state registry | ACCEPT |
| `activeSessionFrontDoor` field | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | line 3 | `activeSessionFrontDoor` | session state registry | ACCEPT |
| Source release status `ALIGNED` | `docs/reference/CVF_RELEASE_READINESS_STATUS_2026-03-20.md` | status rows | `ALIGNED` | CVF release readiness | ACCEPT |
| Source release status `SUBSTANTIALLY ALIGNED` | `docs/reference/CVF_RELEASE_READINESS_STATUS_2026-03-20.md` | status rows | `SUBSTANTIALLY ALIGNED` | CVF release readiness | ACCEPT |
| Source release status `ALIGNED WITH CAVEATS` | `docs/reference/CVF_RELEASE_READINESS_STATUS_2026-03-20.md` | status rows | `ALIGNED WITH CAVEATS` | CVF release readiness | ACCEPT |
| `session_front_door` canonical-file-type | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | `activeSessionFrontDoor` value | `CVF_SESSION_MEMORY.md` | session state registry | ACCEPT |
| `gc018_baseline` canonical-file-type | `docs/baselines/CVF_GC018_LHW13_WORKFLOW_CONNECTOR_WAVE13_2026-05-29.md` | docType field | `gc018_baseline` | GC-018 doc type | ACCEPT |
| `completion_review` canonical-file-type | `docs/reviews/CVF_LHW11_T1_SESSION_GOVERNANCE_POSTURE_AGGREGATOR_CONNECTOR_COMPLETION_2026-05-28.md` | docType field | `completion_review` | review doc type | ACCEPT |
| `runtime_source` canonical-file-type | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | file root | `workflow-resolver.ts` | runtime source class | ACCEPT |

New doc-only fields:

| New doc-only field | Purpose | Not sourced from runtime? | Runtime claim blocked? | Validation expectation |
| --- | --- | --- | --- | --- |
| `agentReadingAdvisoryType` | Names the agent-reading protocol planning advisory. | Yes | Yes | Defined only in the connector spec and verified by documentation review. |
| `claimValidationAdvisory` | Records claim-tier validation guidance without runtime enforcement. | Yes | Yes | Defined only in the connector spec and verified by documentation review. |
| `claimTier` values: `roadmap`, `schema_defined`, `active`, `proven` | Connector-normalized vocabulary derived from source statuses and CVF claim-boundary doctrine. | Yes | Yes | Spec must show source-to-normalized mapping; values are not claimed as runtime/source enum values. |
| `startupAcknowledgmentStatus` values: `acknowledged`, `missing` | Adds the required startup acknowledgment axis from session rules. | Yes | Yes | Spec S2/S3 must include this axis; no runtime enforcement claim. |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| T1 spec; connector-normalized claim-tier vocabulary with source-status mapping | S1-S5 | spec at target path | Reviewer confirms mapping is explicit | CLOSED |
| All 4 connector-normalized claim-tier values covered as doc-only | S2, New Doc-Only Fields | 4 values | No runtime/source enum claim | CLOSED |
| All 4 canonical-file-type values covered as doc-only | S2, New Doc-Only Fields | 4 values with source exemplars | No runtime/source enum claim | CLOSED |
| Startup acknowledgment status axis included | S2/S3 | `startupAcknowledgmentStatus` | Values covered in spec | CLOSED |
| `runtimeExecutionAuthorized=false` explicit | S1, S3 | invariant | grep check | CLOSED |
| CVF 25.05 Gap 1 cited | S1 | explicit in S1 Purpose | Auditor checks | CLOSED |

## Deliverable — Connector Spec

File: `docs/reference/CVF_LHW13_T1_AGENT_READING_PROTOCOL_GOVERNANCE_CONNECTOR_SPEC_2026-05-29.md`

S2 design: map claim-tier × canonical-file-type × startup acknowledgment
status → `agentReadingAdvisoryType`:

| `claimTier` | `canonicalFileType` | `startupAcknowledgmentStatus` | `agentReadingAdvisoryType` | `claimValidationAdvisory` |
| --- | --- | --- | --- | --- |
| `proven` | `runtime_source` | `acknowledged` | `reading_claim_verified` | Claim backed by runtime source; advisory-clear |
| `proven` | `completion_review` | `acknowledged` | `reading_claim_evidence_backed` | Claim backed by completion evidence; advisory-clear |
| `active` | `gc018_baseline` | `acknowledged` | `reading_claim_authorized` | Claim authorized by GC-018; no live proof required |
| `active` | `session_front_door` | `acknowledged` | `reading_claim_session_bounded` | Claim valid within this session scope |
| `schema_defined` | any | `acknowledged` | `reading_claim_schema_only` | Claim is schema/contract only; no live execution proven |
| `roadmap` | any | `acknowledged` | `reading_claim_future_only` | Claim is roadmap only; block if agent implies current capability |
| any | any | `missing` | `reading_claim_startup_incomplete` | Agent must resolve startup front door before material work |

Key invariant: "This connector does not enforce agent behavior at runtime. The
reading advisory is a governance planning record for Orchestrators.
`runtimeExecutionAuthorized=false`."

## Pre-Flight

- [x] Working tree clean at LHW13-T1 closure capture
- [x] All required first reads done
- [x] Source status vocabulary confirmed from CVF Release Readiness doc
- [x] Canonical-file-type classes documented as connector-normalized classes with source exemplars

## Write Ownership

Implementer owns all new files. No file outside Allowed list may be modified.

## Execution Plan

1. Read all required first reads.
2. Confirm claim-tier vocabulary and canonical-file-type values.
3. Draft spec (S1–S5); verify < 250 lines.
4. Run Fast Lane audit.
5. Run governance gates with `--base 7de75901`.
6. Reviewer perspective.
7. Update session continuity.
8. Commit.
9. Write completion review with T2 gate answer.

## Evidence Requirements

- Spec < 250 lines
- All 4 connector-normalized claim-tier values covered in S5 with source-status mapping
- All 4 canonical-file-type values individually row-verified
- Startup acknowledgment status axis included
- `runtimeExecutionAuthorized=false` explicit
- CVF 25.05 Gap 1 cited in S1
- No code file in diff

## Acceptance Criteria

- [x] Spec with all 5 sections; < 250 lines
- [x] All 4 connector-normalized claim-tier values covered as doc-only
- [x] All 4 canonical-file-type values covered as doc-only with source exemplars
- [x] Startup acknowledgment status axis covered
- [x] `runtimeExecutionAuthorized=false` explicit; no runtime enforcement claimed
- [x] CVF 25.05 Gap 1 cited in S1
- [x] No code file in diff
- [x] Session continuity updated

Fail conditions:
- Runtime agent enforcement claimed
- Connector-normalized claim-tier values aggregated in S5
- Missing LHW13 GC-018

## Review Gate

All 4 connector-normalized claim-tier values + 4 canonical-file-type values
covered; startup acknowledgment axis included; `runtimeExecutionAuthorized=false`; no enforcement; spec < 250 lines; no code file.

## Closure Checklist

- [x] Spec with all 5 sections
- [x] S2 mapping includes claim-tier, canonical-file-type, and startup acknowledgment status
- [x] `runtimeExecutionAuthorized=false` explicit
- [x] S5 complete; source facts separated from New Doc-Only Fields
- [x] No code file in diff
- [x] Fast Lane audit created
- [x] Session continuity updated
- [x] Completion review with T2 gate answer written

## Return-To-Orchestrator Conditions

Stop if: claim-tier vocabulary cannot be confirmed; connector requires runtime
enforcement; spec > 250 lines before S4.

## T2 Gate Output

Was a concrete memory continuity level advisory gap identified during T1?

**Expected YES:** T1 reading protocol reveals that when an agent claims memory
continuity, no connector maps `memorySnapshotAdvisoryType` × `canReinject` ×
`memoryContextSeedDecayAdvisoryType` → a named `memoryContinuityLevelAdvisoryType`
(L0/L1/L2/L3). T2 closes that gap.

## Operator Checkpoint

operator.checkpoint.waiver: Low-risk documentation-only tranche.

## Claim Boundary

LHW13-T1 produces a documentation artifact. It does not claim runtime agent
enforcement, receipt envelope extension, memory reinjection, hosted readiness,
production readiness, or public release readiness.
