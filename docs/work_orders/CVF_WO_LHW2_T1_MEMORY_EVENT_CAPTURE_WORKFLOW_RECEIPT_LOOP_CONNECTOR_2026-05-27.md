# CVF Work Order — LHW2-T1 Memory Event Capture Workflow Receipt Loop Connector

Memory class: FULL_RECORD

Status: OPEN

docType: work_order

Date: 2026-05-27

---

## Purpose

Implement LHW2-T1: a connector spec binding W2 memory event hook classes →
VI3 agent memory capture record fields → GovernanceEvidenceReceipt fields into a
traceable loop. Closes the gap where W2, VI3, and M1 each exist as proven runtime
pieces but no connector standard ties them into a coherent handoff chain.

Documentation-only tranche. No source code, runtime module, route, or provider
behavior is changed.

## Authority Chain

- LHW2 roadmap: `docs/roadmaps/CVF_LHW2_WORKFLOW_CONNECTOR_COMPLETION_ROADMAP_2026-05-27.md`
- Fast Lane audit: `docs/reviews/CVF_LHW2_T1_FAST_LANE_AUDIT_2026-05-27.md` → FAST_LANE_READY
- LH1 ledger (`agentmemory` trigger): `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
- W2: `docs/reviews/CVF_W2_MEMORY_EVENT_HOOKS_CONTEXT_PACKAGER_COMPLETION_2026-05-24.md`
- VI3: `docs/reviews/CVF_VI3_AGENTMEMORY_CAPTURE_RECORD_READOUT_COMPLETION_2026-05-25.md`
- M1: `docs/reviews/CVF_M1_DURABLE_CROSS_SESSION_MEMORY_COMPLETION_2026-05-24.md`
- LHW1-T2 spec: `docs/reference/CVF_LHW1_WORKFLOW_CHAIN_STATE_CONNECTOR_SPEC_2026-05-27.md`

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `docs/reviews/CVF_W2_MEMORY_EVENT_HOOKS_CONTEXT_PACKAGER_COMPLETION_2026-05-24.md`
   — understand the 5 hook classes and `canReinject=false` / `rawMemoryReleased=false` bindings
4. `docs/reviews/CVF_VI3_AGENTMEMORY_CAPTURE_RECORD_READOUT_COMPLETION_2026-05-25.md`
   — understand `cvf.agentMemoryCaptureRecord.vi3.v1` fields and source-verified paths
5. `docs/reviews/CVF_LHW1_T2_WORKFLOW_CHAIN_STATE_CONNECTOR_COMPLETION_2026-05-27.md`
   — understand evidence receipt binding from S6 (GovernanceEvidenceReceipt field names)
6. `docs/reviews/CVF_M1_DURABLE_CROSS_SESSION_MEMORY_COMPLETION_2026-05-24.md`
   — understand durable memory read/write boundaries and what is visible in receipt
7. `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-event-hooks.ts`
   — read-only to confirm field names; do NOT modify

If any required file is missing, stop and report to Orchestrator.

## Scope

**Allowed:**

- `docs/reference/CVF_LHW2_MEMORY_EVENT_CAPTURE_WORKFLOW_RECEIPT_LOOP_CONNECTOR_SPEC_2026-05-27.md`
  (new — primary deliverable)
- this work order (status update only)
- session continuity files

**Forbidden:** `EXTENSIONS/` (any file), `governance/contracts/` (any file),
`memory-event-hooks.ts`, `audit-memory-receipt.ts`, any `.ts`/`.tsx`/`.js`/`.py`
file, receipt envelope schema, public-sync repo.

## Deliverable — Connector Spec

File: `docs/reference/CVF_LHW2_MEMORY_EVENT_CAPTURE_WORKFLOW_RECEIPT_LOOP_CONNECTOR_SPEC_2026-05-27.md`

Required sections:

### S1 — Purpose and claim boundary

- State what the connector is: a normative doc binding W2 event hook classes to
  VI3 capture record fields and GovernanceEvidenceReceipt fields.
- State what it is not: not a W2/VI3 runtime extension; not a new memory tier;
  not a reinjection path.
- Explicit statement: "`canReinject: false` and `rawMemoryReleased: false` are
  preserved from W2, VI3, M1, and M2 boundaries. This connector does not relax
  either constraint."

### S2 — Event hook class to capture record field mapping

Table columns: `W2 hook class` | `W2 decision` | `VI3 captureRecord field` |
`Propagation rule`

Minimum rows:

- `allow_capture` → `captureRecord.captureDecision` → include in receipt
- `allow_redacted_capture` → `captureRecord.privacyFilters` → redacted summary only
- `allow_context_read` → `captureRecord.memoryIds` → evidence ids in receipt
- `deny` → `captureRecord.captureDecision` → excluded; record denial reason
- `require_human_approval` → `captureRecord.policyContext` → hold; approval required

Use W2 and VI3 field names verbatim. If a field name is uncertain, write
"confirm field name against `memory-event-hooks.ts` or `audit-memory-receipt.ts`"
rather than inventing a name.

### S3 — Capture record to GovernanceEvidenceReceipt binding

Table columns: `VI3 captureRecord field` | `GovernanceEvidenceReceipt field` |
`Binding rule` | `Current status`

Minimum rows must cover: captureDecision, privacyFilters, memoryIds,
rawMemoryReleased, canReinject. Use existing `GovernanceEvidenceReceipt` field
names only. Do not define new receipt envelope fields.

`Current status` column must use one of: `RUNTIME_PROVEN` (if the field is
already wired in a closed PASS tranche) or `DOC_ONLY` (if the binding is
specified here but not yet wired in runtime).

### S4 — Loop completion standard

Prose description: when a memory event completes the full loop (hook → capture
→ receipt), what evidence trail is expected at each stage:

- At hook evaluation: W2 decision returned
- At capture record: VI3 fields populated
- At receipt: which GovernanceEvidenceReceipt fields carry the evidence
- Loop closed indicator: what confirms the loop is traceable end-to-end

State explicitly: "The loop is traceable when a receipt contains the memory ids
from `captureRecord.memoryIds` and `rawMemoryReleased=false` is confirmed."

### S5 — Runtime-enforcement boundary table

| Behavior | Current status | Future path |
| --- | --- | --- |
| W2 event hook classification | Runtime (LPF) | Stable |
| VI3 capture record readout | Runtime (cvf-web route) | Stable |
| M1 durable memory read/write | Runtime (LPF) | Stable |
| Hook-to-capture-record binding | Document-only | Future: LPF wire-up |
| Capture-to-receipt binding | Document-only | Future: receipt field extension tranche |
| Loop completion verification | Document-only | Future: loop-trace validator |

Do not label any row "Runtime" unless a closed PASS tranche implements it.

### S6 — Source Verification Table (mandatory)

Required columns: `Claimed field` | `Source file` | `Verified field path` |
`Owning interface/function` | `Disposition`

Cover every W2 and VI3 field name cited in S2 and S3. If any field cannot be
source-verified, mark Disposition as `UNVERIFIED — return to Orchestrator`.
No unverified field may remain in S2/S3.

## Pre-Flight

- [ ] Working tree clean
- [ ] All required first reads done
- [ ] W2 hook class names confirmed from `memory-event-hooks.ts`
- [ ] VI3 captureRecord field names confirmed from `audit-memory-receipt.ts`

## Agent Roles

Implementer writes spec (S1–S6); confirms field names from source files (read
only); updates session continuity. Reviewer checks field names verbatim, binding
rules honest, S5 boundary table correct, `canReinject=false` explicit, no `.ts`
file touched. Auditor confirms LH1 trigger documented, loop claim is doc-only,
no new runtime authority. No self-review.

## Write Ownership

Implementer owns all new files. No file outside the Allowed list may be modified.

## Execution Plan

1. Read all required first reads.
2. Confirm W2 hook class names and VI3 captureRecord field names from source.
3. Draft spec (S1–S6) with Source Verification Table.
4. Confirm no code file staged.
5. Reviewer perspective — record result.
6. Update session continuity (`lhw2_t1_complete`).
7. Commit: `docs(lhw2-t1): add memory event capture workflow receipt loop connector spec`.
8. Write completion review.

Spec size guard: < 250 lines. Split at 200 if needed (S1–S3 / S4–S6).

## Review Gate

Before committing: Reviewer perspective completed; `canReinject=false` and
`rawMemoryReleased=false` confirmed explicit; Source Verification Table complete
with no UNVERIFIED rows; no code file in diff.

## Acceptance Criteria

- [ ] Spec with all 6 sections created
- [ ] S2 field mapping table uses W2 and VI3 vocabulary verbatim
- [ ] S3 GovernanceEvidenceReceipt binding uses existing field names only
- [ ] S4 loop completion standard explicitly states traceability condition
- [ ] S5 boundary table honest (no doc-only row labeled Runtime)
- [ ] S6 Source Verification Table complete with no UNVERIFIED rows
- [ ] `canReinject: false` and `rawMemoryReleased: false` explicit in S1
- [ ] No code file in diff
- [ ] Session continuity updated

## T2 Gate Output (required in completion review)

Answer explicitly: "Was a concrete recovery packet gap identified during T1 work?"

- YES → describe gap in one sentence; T2 proceeds.
- NO → "No gap found. T2 gate question: does the T2 spec remain necessary per
  roadmap rationale?" (T2 proceeds regardless — this output is informational.)

## Evidence Requirements

- Spec at target path with all 6 sections present
- S2 field mapping uses W2 and VI3 vocabulary verbatim (no invented names)
- S3 GovernanceEvidenceReceipt binding uses existing field names only
- S4 loop completion states traceability condition explicitly
- S5 boundary table present; no doc-only row labeled Runtime
- S6 Source Verification Table complete; no UNVERIFIED rows
- `canReinject: false` and `rawMemoryReleased: false` explicit in S1
- No `.ts`/`.tsx`/`.js`/`.py` file in `git diff --name-only`
- Session continuity updated to `lhw2_t1_complete`
- Completion review file written with T2 gate answer

## Closure Checklist

- [ ] Spec created with all 6 sections
- [ ] S2 mapping table uses W2 + VI3 vocabulary verbatim
- [ ] S6 Source Verification Table complete; no UNVERIFIED rows
- [ ] `canReinject: false` and `rawMemoryReleased: false` explicit
- [ ] No code file in diff
- [ ] Session continuity updated
- [ ] Completion review with T2 gate answer written

## Return-To-Orchestrator Conditions

Stop and report to Orchestrator if:

- any required first read file is missing or unreadable;
- a W2 hook class name or VI3 captureRecord field name cannot be confirmed
  from source without modifying the source file;
- writing the connector requires adding a new GovernanceEvidenceReceipt field;
- spec exceeds 250 lines before S4 is complete.

## Operator Checkpoint

operator.checkpoint.waiver: Low-risk documentation-only tranche gated by
source-verified field names; no operator checkpoint required unless a conflict
with W2/VI3 TypeScript field names is discovered during implementation.

## Claim Boundary

LHW2-T1 produces a documentation artifact. It does not claim W2/VI3 runtime
extension, new memory tiers, memory reinjection, receipt envelope extension,
provider behavior, hosted readiness, production readiness, or public release
readiness.
