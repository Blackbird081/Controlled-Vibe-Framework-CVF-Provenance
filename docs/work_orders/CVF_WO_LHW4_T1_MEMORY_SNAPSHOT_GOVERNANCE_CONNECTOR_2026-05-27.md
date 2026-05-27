# CVF Work Order — LHW4-T1 Memory Snapshot Governance Connector

Memory class: FULL_RECORD

Status: READY_FOR_DISPATCH

docType: work_order

Date: 2026-05-27

---

## Purpose

Implement LHW4-T1: a connector spec defining the governed memory snapshot
package standard — what surfaces contribute, which tiers are includable vs.
blocked, and what a snapshot receipt must contain to be auditable. Closes the
gap where AIF-B graph, AIF-C gateway, M1 durable memory, and VI3 capture record
all exist but no connector defines the snapshot governance package.

Documentation-only tranche. No source code, runtime module, route, or provider
behavior is changed. `canReinject=false` and `rawMemoryReleased=false` are
preserved throughout.

## Authority Chain

- LHW4 roadmap: `docs/roadmaps/CVF_LHW4_WORKFLOW_CONNECTOR_WAVE4_ROADMAP_2026-05-27.md`
- Fast Lane audit: `docs/reviews/CVF_LHW4_T1_FAST_LANE_AUDIT_2026-05-27.md` → FAST_LANE_READY
- LH1 ledger (`tolaria` trigger): `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
- AIF-B: `docs/reviews/CVF_AIF_B_GRAPH_KNOWLEDGE_PHASE1_COMPLETION_2026-05-24.md`
- AIF-C: `docs/reviews/CVF_AIF_C_MEMORY_GATEWAY_PHASE2_COMPLETION_2026-05-24.md`
- M1: `docs/reviews/CVF_M1_DURABLE_CROSS_SESSION_MEMORY_COMPLETION_2026-05-24.md`
- VI3: `docs/reviews/CVF_VI3_AGENTMEMORY_CAPTURE_RECORD_READOUT_COMPLETION_2026-05-25.md`
- H2: `docs/reviews/CVF_H2_RUNTIME_MEMORY_HIERARCHY_PHASE2_COMPLETION_2026-05-22.md`

## Agent Roles

Implementer writes spec (S1–S5) using AIF-B, AIF-C, M1, VI3, and H2 vocabulary
verbatim. Reviewer checks field names verbatim, `canReinject=false` explicit,
`rawMemoryReleased=false` explicit, boundary table honest, no runtime claim
added, no `.ts` file touched, S5 Source Verification complete. Auditor confirms
LH1 trigger documented, no live snapshot execution or reinjection claimed.
No self-review.

## Scope

**Allowed:**

- `docs/reference/CVF_LHW4_MEMORY_SNAPSHOT_GOVERNANCE_CONNECTOR_SPEC_2026-05-27.md`
  (new — primary deliverable)
- this work order (status update only)
- session continuity files

**Forbidden:** `EXTENSIONS/` (any file), `governance/contracts/` (any file),
any `.ts`/`.tsx`/`.js`/`.py` file, receipt envelope schema, public-sync repo.
Live snapshot execution, automated scheduling, and memory reinjection remain
blocked.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `docs/reviews/CVF_AIF_B_GRAPH_KNOWLEDGE_PHASE1_COMPLETION_2026-05-24.md`
   — confirm the AIF-B graph schema surface: `GraphKnowledgeService`,
   `SymbolIndex`, `ASTParser` — read-only; confirm what a graph index contains
4. `docs/reviews/CVF_AIF_C_MEMORY_GATEWAY_PHASE2_COMPLETION_2026-05-24.md`
   — confirm AIF-C memory gateway/lifecycle/retrieval module names;
   `canReinject=false` binding; `rawMemoryReleased=false`
5. `docs/reviews/CVF_M1_DURABLE_CROSS_SESSION_MEMORY_COMPLETION_2026-05-24.md`
   — confirm M1 durable tier names: `skill-tier`, `long-term-tier`; confirm
   that only summary-only access is allowed via AIF-C C2 gate
6. `docs/reviews/CVF_VI3_AGENTMEMORY_CAPTURE_RECORD_READOUT_COMPLETION_2026-05-25.md`
   — confirm VI3 `captureRecord` field names: `captureDecision`,
   `privacyFilters`, `memoryIds`, `rawMemoryReleased`, `canReinject`,
   `policyContext.actorRole`
7. `docs/reviews/CVF_H2_RUNTIME_MEMORY_HIERARCHY_PHASE2_COMPLETION_2026-05-22.md`
   — confirm H2 seven-tier vocabulary: `working`, `task`, `skill`,
   `organizational`, `long-term`, `audit`, `receipt`; which tiers are
   `canReinject=false` and `durablePersistenceAllowed=false`
8. `docs/reference/CVF_LHW4_WORKFLOW_CONNECTOR_WAVE4_ROADMAP_2026-05-27.md`
   — confirm T1 deliverable shape

If any required file is missing, stop and report to Orchestrator.

## Deliverable — Connector Spec

File: `docs/reference/CVF_LHW4_MEMORY_SNAPSHOT_GOVERNANCE_CONNECTOR_SPEC_2026-05-27.md`

Required sections:

### S1 — Purpose and claim boundary

- State what the connector is: a normative doc defining the governed memory
  snapshot package standard — which surfaces contribute, which tiers are
  includable vs. blocked, and what a snapshot receipt must contain.
- State what it is not: not an AIF-B/AIF-C/M1/VI3 runtime extension; not a
  live snapshot executor; not an automated snapshot scheduler.
- Explicit statement: "`canReinject=false` and `rawMemoryReleased=false` are
  preserved from W2, VI3, M1, and AIF-C boundaries. This connector does not
  relax either constraint. A snapshot is a read-only packaging record; it does
  not grant reinjection authority."

### S2 — Memory surface contribution table

Table columns: `Memory surface` | `AIF-B/AIF-C/M1/VI3/H2 owner` |
`Includable in snapshot?` | `Boundary rule` | `Current status`

Minimum rows:

- AIF-B graph index → `GraphKnowledgeService` → advisory-only (no scoring authority) → include as index reference only → DOC_ONLY binding
- AIF-C gateway retrieval result → `controlled-memory-gateway.ts` → summary-only → include summary; no raw item export → DOC_ONLY binding
- M1 `skill-tier` → durable store → includable → summary + evidence path only; no raw content → RUNTIME_PROVEN (M1 closed)
- M1 `long-term-tier` → durable store → includable → summary + evidence path only → RUNTIME_PROVEN (M1 closed)
- VI3 `captureRecord.memoryIds` → `audit-memory-receipt.ts` → includable → ids only; no raw memory content → RUNTIME_PROVEN (VI3 closed)
- H2 `working` / `task` tiers → in-process only → not includable → ephemeral; not persistent → DOC_ONLY boundary

Use field names verbatim from each completion review. If any field name cannot
be confirmed, mark `BLOCKED_SOURCE_NOT_FOUND`, stop, and return to Orchestrator.

### S3 — Snapshot receipt minimum field list

Prose + field list (max 10 lines):

Every governed memory snapshot receipt must contain:

- `snapshotId`: unique token
- `snapshotActor`: G1 actorId at time of snapshot
- `includedTiers`: list of H2 tier tokens included
- `captureDecision`: from VI3 `captureRecord.captureDecision`
- `evidencePaths`: list of M1 / AIF-B evidence file paths included
- `rawMemoryReleased`: always `false`
- `canReinject`: always `false`
- `snapshotBoundary`: one of `advisory_summary` | `evidence_path_only` | `index_reference_only`

State explicitly: "These fields are documentation-only minimum requirements.
They do not extend `GovernanceEvidenceReceipt` or any existing receipt
envelope type."

### S4 — Runtime-enforcement boundary table

| Behavior | Current status | Future path |
| --- | --- | --- |
| AIF-B graph index query | Runtime (AIF-B LPF) | Stable |
| AIF-C gateway retrieval | Runtime (AIF-C LPF) | Stable |
| M1 durable memory read | Runtime (M1 LPF) | Stable |
| VI3 capture record readout | Runtime (cvf-web route) | Stable |
| Snapshot package composition | Document-only | Future: snapshot assembler service |
| Snapshot receipt validation | Document-only | Future: receipt field validator |
| Automated snapshot scheduling | Document-only | Future: governance scheduling surface |

Do not label any row "Runtime" unless a closed PASS tranche implements it.

### S5 — Source Verification Table (mandatory)

Required columns: `Claimed item` | `Source file` | `Verified path or symbol` |
`Owning interface/function/schema` | `Disposition`

Cover every AIF-B, AIF-C, M1, VI3, and H2 field name cited in S2 and S3.
Valid dispositions are `ACCEPT`, `REJECT`, and `BLOCKED_SOURCE_NOT_FOUND`. If
any item cannot be source-verified, mark it `BLOCKED_SOURCE_NOT_FOUND`, stop,
and return to Orchestrator. No blocked, guessed, or confirm-later item may
remain in S2.

## Pre-Flight

- [ ] Working tree clean
- [ ] All required first reads done
- [ ] AIF-B/AIF-C module names confirmed from completion reviews
- [ ] M1 tier names confirmed from M1 completion review
- [ ] VI3 captureRecord field names confirmed from VI3 completion review
- [ ] H2 tier tokens confirmed from H2 completion review

## Write Ownership

Implementer owns all new files. No file outside the Allowed list may be
modified.

## Execution Plan

1. Read all required first reads.
2. Confirm all surface/field names from completion reviews.
3. Draft spec (S1–S5) with Source Verification Table.
4. Confirm no code file staged.
5. Reviewer perspective — record result.
6. Update session continuity (`lhw4_t1_complete`).
7. Commit: `docs(lhw4-t1): add memory snapshot governance connector spec`.
8. Write completion review; include T2 gate answer (see below).

Spec size guard: < 200 lines. Trim S3 prose if approaching 180 lines.

## Evidence Requirements

- Spec at target path with all 5 sections present
- S2 table uses AIF-B/AIF-C/M1/VI3/H2 vocabulary verbatim
- `canReinject=false` and `rawMemoryReleased=false` explicit in S1 and S3
- S4 boundary table present; no doc-only row labeled Runtime
- S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- No `.ts`/`.tsx`/`.js`/`.py` file in `git diff --name-only`
- Session continuity updated to `lhw4_t1_complete`
- Completion review written with T2 gate answer

## Acceptance Criteria

- [ ] Spec with all 5 sections created
- [ ] S2 covers all 6 memory surface rows
- [ ] `canReinject=false` and `rawMemoryReleased=false` explicit
- [ ] S3 snapshot receipt fields present and state doc-only boundary
- [ ] S4 boundary table honest (no doc-only row labeled Runtime)
- [ ] S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- [ ] No code file in diff
- [ ] Session continuity updated

## Review Gate

Before committing: Reviewer perspective completed; all AIF-B/AIF-C/M1/VI3/H2
field names verbatim; `canReinject=false` and `rawMemoryReleased=false` explicit;
S5 complete with no `BLOCKED_SOURCE_NOT_FOUND` rows; no code file in diff.

## Closure Checklist

- [ ] Spec created with all 5 sections
- [ ] S2 surface table uses existing vocabulary verbatim
- [ ] `canReinject=false` + `rawMemoryReleased=false` explicit
- [ ] S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- [ ] No code file in diff
- [ ] Session continuity updated
- [ ] Completion review with T2 gate answer written

## Return-To-Orchestrator Conditions

Stop and report to Orchestrator if:

- any required first read file is missing or unreadable;
- an AIF-B, AIF-C, M1, VI3, or H2 field name cannot be confirmed from
  completion reviews;
- writing the connector requires adding a new memory tier or relaxing
  `canReinject` or `rawMemoryReleased`;
- writing the connector requires modifying any `.ts` file;
- spec exceeds 200 lines before S4 is complete.

## T2 Gate Output (required in completion review)

Answer explicitly: "Was a concrete execution authority-chain gap identified
during T1 work?"

- YES → describe gap in one sentence; T2 proceeds.
- NO → "No gap found. T2 proceeds per roadmap rationale."
  (T2 proceeds regardless — this output is informational.)

## Operator Checkpoint

operator.checkpoint.waiver: Low-risk documentation-only tranche gated by
source-verified AIF-B/AIF-C/M1/VI3/H2 field names from existing completion
reviews; no operator checkpoint required unless a conflict with memory-tier
vocabulary or a `canReinject` relaxation is discovered during implementation.

## Claim Boundary

LHW4-T1 produces a documentation artifact. It does not claim AIF-B/AIF-C/M1/
VI3/H2 runtime extension, live snapshot execution, automated snapshot
scheduling, memory reinjection, receipt envelope extension, provider behavior,
hosted readiness, production readiness, or public release readiness.
