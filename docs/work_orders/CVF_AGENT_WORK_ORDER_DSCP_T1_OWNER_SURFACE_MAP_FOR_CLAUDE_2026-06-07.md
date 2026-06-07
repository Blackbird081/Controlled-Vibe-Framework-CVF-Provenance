# CVF Agent Work Order: DSCP-T1 Owner Surface Map and Schema Proposal

Memory class: POINTER_RECORD

Status: CLOSED_PASS_BOUNDED

Template: `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
(post-`fce62cd3` version with Worker Pending-Return Gate section 6D)

Commit mode: `WORKER_MUST_NOT_COMMIT`

completionReviewPath: `docs/reviews/CVF_DSCP_T1_OWNER_SURFACE_MAP_COMPLETION_2026-06-07.md`

dispatchBaseHead: `8e61f65d`
executionBaseHead: `8e61f65d`
closureBaseHead: `8e61f65d`

Status token rule:
- Worker must not change `Status` field.
- Reviewer/committer changed `Status` to `CLOSED_PASS_BOUNDED` after
  accepting the worker return for reviewer commit.

---

## Purpose

Map all existing scan, classification, context-pack, and retrieval receipt
surfaces currently in CVF. Identify which fields are domain-specific vs
domain-agnostic. Propose a domain-agnostic standard schema (doc-only
TypeScript interface definitions) for the governed scan -> classify ->
context pack -> retrieve pipeline, so future corpus expansion lanes can
reuse the pattern without reimplementing LPCI-specific schemas.

---

## 2. Authority Chain

- Operator instruction: 2026-06-07 - open DSCP roadmap; generalize
  PolicyLocal lessons into domain-agnostic standard; no T12; doc-only.
- LPCI2-T11D closure:
  `docs/reviews/CVF_LPCI2_T11_CORPUS_EXPANSION_READINESS_GATE_2026-06-07.md`
  (`readinessVerdict=READY_WITH_CONDITIONS`; next allowed move = choose new lane)
- Active handoff: `AGENT_HANDOFF_V16_2026-06-06.md` Next Allowed Move section
- GC-018:
  `docs/baselines/CVF_GC018_DSCP_T1_OWNER_SURFACE_MAP_AND_SCHEMA_PROPOSAL_2026-06-07.md`
- Roadmap:
  `docs/roadmaps/CVF_DSCP_DOMAIN_AGNOSTIC_SCAN_CONTEXT_PACK_READINESS_ROADMAP_2026-06-07.md`

---

## 3. Agent Roles

| Role | Agent | Responsibility |
|---|---|---|
| Worker | Claude | Read sources; produce owner surface map, schema proposal, worker return; return uncommitted |
| Reviewer / Committer | Codex | Review artifacts; run committed-range gates; commit; update session continuity |
| Orchestrator | Operator | Authorizes scope; reviews verdict; authorizes DSCP-T2 separately if desired |

---

## Scope / Target / Owner Boundary

### Write Ownership

Worker may create (uncommitted, staged):
- `docs/reference/CVF_DSCP_T1_OWNER_SURFACE_MAP_2026-06-07.md`
- `docs/reference/CVF_DSCP_T1_SCHEMA_PROPOSAL_2026-06-07.md`
- `docs/reviews/CVF_DSCP_T1_OWNER_SURFACE_MAP_WORKER_RETURN_2026-06-07.md`

Worker must not modify any existing file. No new `.ts` files.

### Allowed scope

- Reading all source files named in Section 5.
- Authoring the three output files listed above (doc-only, no `.ts`).
- Running pre-flight and component governance gate checks.
- Documentation format remediation inside Allowed scope.

### Forbidden scope

- Modifying any TypeScript source file in EXTENSIONS.
- Creating any new `.ts` implementation file.
- Modifying T11A/B/C/D artifacts or any existing governance artifact.
- Corpus ingestion, body extraction, OCR, or runtime query.
- Provider/API calls or live proof.
- Any claim of production, public, or hosted readiness.
- Any worker-side commit or push.

Risk ceiling: R1

---

## Roadmap-To-Work-Order Trace Matrix

| Roadmap / GC-018 requirement | Work-order instruction | Evidence target | Status |
|---|---|---|---|
| DSCP-T1: owner surface map (doc-only) | Section 6B step 3: write owner surface map | `docs/reference/CVF_DSCP_T1_OWNER_SURFACE_MAP_2026-06-07.md` | CLOSED_PASS_BOUNDED |
| DSCP-T1: schema proposal (doc-only) | Section 6B step 4: write schema proposal | `docs/reference/CVF_DSCP_T1_SCHEMA_PROPOSAL_2026-06-07.md` | CLOSED_PASS_BOUNDED |
| DSCP-T1: source verification required | Section 6A source verification table | all ACCEPT rows cite file + line range | CLOSED_PASS_BOUNDED |
| DSCP-T1: no `.ts` new files | Forbidden scope list | `git status --short` at return | CLOSED_PASS_BOUNDED |
| DSCP-T1: worker must not commit | `WORKER_MUST_NOT_COMMIT` commit mode | staged files; reviewer commits | CLOSED_PASS_BOUNDED |
| GC-018 boundary: no T12, no runtime | Forbidden scope list | worker return boundary statement | CLOSED_PASS_BOUNDED |

## Worker Autonomy / No-Question Rule

The worker proceeds without operator confirmation for all non-destructive
allowed-scope actions: reading source files, authoring doc-only output files,
running component gate checks, staging output files.

Repair doc-format and gate-compliance failures directly. Escalate only if:
a required source file is missing, a proposed interface requires body content
access, or a forbidden scope action would be required.

## Reviewer Closure Conversion Block

```text
completionReviewPath: `docs/reviews/CVF_DSCP_T1_OWNER_SURFACE_MAP_COMPLETION_2026-06-07.md`
reviewerOwnedClosurePaths:
- `docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T1_OWNER_SURFACE_MAP_FOR_CLAUDE_2026-06-07.md`
- `docs/reviews/CVF_DSCP_T1_OWNER_SURFACE_MAP_WORKER_RETURN_2026-06-07.md`
- `docs/reviews/CVF_DSCP_T1_OWNER_SURFACE_MAP_COMPLETION_2026-06-07.md`
- `docs/roadmaps/CVF_DSCP_DOMAIN_AGNOSTIC_SCAN_CONTEXT_PACK_READINESS_ROADMAP_2026-06-07.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V16_2026-06-06.md`
pendingStatusTokensAllowedBeforeReview: pending worker-return status only
forbiddenClosedEquivalentResidue: no pending worker-return or pending-finality token may remain as current final status
```

## Pre-Flight Checks

Capture `executionBaseHead` via `git rev-parse --short HEAD` before any edit.
Confirm working tree is clean except for DSCP artifacts authored in this
session. Verify that GC-018 and roadmap files are present at paths cited in
Section 2 before proceeding.

If any required source file in Section 5 is missing, stop and return
`BLOCKED_SOURCE_NOT_FOUND`.

## 5. Required First Reads

- `CVF_SESSION_MEMORY.md` - startup front door, current mode
- `AGENT_HANDOFF_V16_2026-06-06.md` - T11D closure and next allowed move
- `docs/roadmaps/CVF_DSCP_DOMAIN_AGNOSTIC_SCAN_CONTEXT_PACK_READINESS_ROADMAP_2026-06-07.md`
  - DSCP scope, tranche plan, acceptance criteria
- `docs/baselines/CVF_GC018_DSCP_T1_OWNER_SURFACE_MAP_AND_SCHEMA_PROPOSAL_2026-06-07.md`
  - authorization, boundaries, acceptance criteria
- Source surfaces (for mapping):
  - `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/context.packager.contract.ts`
    (lines 1-289: `ContextPackagerRequest`, `TypedContextPackage`,
    `TypedContextSegment`, `ExtendedSegmentType`, `ContextPackagerContract`)
  - `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/types.ts`
    (lines 1-53: `RAGDocument`, `RAGQuery`, `RAGResult`, `RetrievalTier`,
    `TierConfig`)
  - `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts`
    (lines 1-112: `MemoryContextPackageInput`, `MemoryContextBlock`,
    `MemoryContextPackageEvidence`, `packageMemoryContext`)
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts`
    (lines 1-133: `LpciIndexRecord`, `AnswerClass`, `RecordStatus`,
    `RetrievalReceipt`, `AuditReceipt`, `ManifestEntry`, `CorpusManifest`)
  - `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/rag.context.engine.convergence.contract.ts`
    (lines 1-77: surface map, `RagContextSurfaceEntry`,
    `DeterministicContextPackagingDeclaration`,
    `KnowledgeNativeRetrievalAuthorityDeclaration`)
  - `docs/reference/CVF_LPCI2_T11_CANDIDATE_INVENTORY_2026-06-07.md`
    (lines 37-44: T11A candidate inventory table header + rows)
  - `docs/reference/CVF_LPCI2_T11_CLASSIFICATION_PRE_CHECK_2026-06-07.md`
    (lines 50-58: classification table with `answerClass`, `ec02Gate`,
    `t12Eligible`, `currentStatus`, `jurisdiction`, `candidateFamily`)

---

## 6. Execution Plan

### 6A. Source Verification Table

Before writing output files, verify all source-fact claims against actual
source files. Every ACCEPT row must include exact file path and line range
or section name.

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| `ContextPackagerRequest` interface (EXISTS) | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/context.packager.contract.ts` | lines 29-38 | `ContextPackagerRequest` | `ContextPackagerContract.pack()` | ACCEPT |
| `TypedContextPackage` interface (EXISTS) | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/context.packager.contract.ts` | lines 49-59 | `TypedContextPackage` | `ContextPackagerContract.pack()` | ACCEPT |
| `ExtendedSegmentType` union (EXISTS) | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/context.packager.contract.ts` | lines 6-12 | `ExtendedSegmentType` | `TypedContextSegment` | ACCEPT |
| `RAGDocument` interface (EXISTS) | `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/types.ts` | lines 11-21 | `RAGDocument` | `RAGPipeline.query()` | ACCEPT |
| `RetrievalTier` union (EXISTS) | `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/types.ts` | line 1 | `RetrievalTier` | `RAGDocument.tier` | ACCEPT |
| `MemoryContextPackageInput` interface (EXISTS) | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts` | lines 17-25 | `MemoryContextPackageInput` | `packageMemoryContext()` | ACCEPT |
| `MemoryContextPackageEvidence` interface (EXISTS) | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts` | lines 37-48 | `MemoryContextPackageEvidence` | `MemoryContextBlock.evidence` | ACCEPT |
| `rawMemoryReleased: false` governance lock (EXISTS) | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts` | lines 34, 46, 106, 109 | `rawMemoryReleased` | `MemoryContextBlock`, `MemoryContextPackageEvidence` | ACCEPT |
| `LpciIndexRecord` interface (EXISTS) | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | lines 29-44 | `LpciIndexRecord` | LPCI retrieval pipeline | ACCEPT |
| `AnswerClass` union (EXISTS) | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | lines 3-7 | `AnswerClass` | `LpciIndexRecord.answerClass` | ACCEPT |
| `AuditReceipt` interface (EXISTS) | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | lines 88-103 | `AuditReceipt` | LPCI audit trail | ACCEPT |
| `RagContextSurfaceEntry` interface (EXISTS) | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/rag.context.engine.convergence.contract.ts` | lines 10-16 | `RagContextSurfaceEntry` | convergence contract surface map | ACCEPT |
| T11A candidate inventory table columns (EXISTS) | `docs/reference/CVF_LPCI2_T11_CANDIDATE_INVENTORY_2026-06-07.md` | line 37 | `candidateFamily`, `currentStatus`, `answerClass`, `ec02Applies`, `sourceRole` | T11A inventory schema | ACCEPT |
| T11C classification table columns (EXISTS) | `docs/reference/CVF_LPCI2_T11_CLASSIFICATION_PRE_CHECK_2026-06-07.md` | line 50 | `ec02Gate`, `t12Eligible`, `jurisdiction`, `domainCategory` | T11C classification schema | ACCEPT |
| DSCP roadmap (EXISTS) | `docs/roadmaps/CVF_DSCP_DOMAIN_AGNOSTIC_SCAN_CONTEXT_PACK_READINESS_ROADMAP_2026-06-07.md` | section Tranche Plan | DSCP-T1 through DSCP-T3 tranche plan | operator-authorized DSCP roadmap | ACCEPT |
| GC-018 authorization (EXISTS) | `docs/baselines/CVF_GC018_DSCP_T1_OWNER_SURFACE_MAP_AND_SCHEMA_PROPOSAL_2026-06-07.md` | section Decision | `Decision` | GC-018 baseline | ACCEPT |

### 6B. Execution Steps

1. Capture `executionBaseHead` via `git rev-parse --short HEAD` before any edit.
2. Confirm working tree is clean (no staged or unstaged changes other than
   DSCP artifacts authored in this session).
3. Write `docs/reference/CVF_DSCP_T1_OWNER_SURFACE_MAP_2026-06-07.md`:
   - Layer 1 - Scan / Artifact Descriptor surfaces
   - Layer 2 - Classification Envelope surfaces
   - Layer 3 - Context Pack surfaces
   - Layer 4 - Retrieval Receipt surfaces
   - Layer 5 - Gap Analysis per layer
4. Write `docs/reference/CVF_DSCP_T1_SCHEMA_PROPOSAL_2026-06-07.md`:
   - Proposed `GovernedArtifactDescriptor` + `GovernanceGateSet`
   - Proposed `GovernedContextPackRequest` + `GovernedContextPackage`
   - Proposed `GovernedRetrievalReceipt`
   - Standard context pack narrative
   - Migration path from LPCI-specific to domain-agnostic
5. Write `docs/reviews/CVF_DSCP_T1_OWNER_SURFACE_MAP_WORKER_RETURN_2026-06-07.md`
   with Worker Pending-Return Gate table.
6. Stage all three output files; do not commit.

### 6C. Pre-return Checks

| Check | Command | Expected result |
|---|---|---|
| Execution anchor | `git rev-parse --short HEAD` before edits | `executionBaseHead=<hash>` |
| Pending worktree | `git status --short` | new output files staged; no `.ts` new files |
| Markdown structural completeness | `python governance/compat/check_markdown_structural_completeness.py --base <executionBaseHead> --head HEAD --enforce` | `PASS` or pending-return exception with reason |
| Finding-To-Governance learning | `python governance/compat/check_finding_to_governance_learning.py --base <executionBaseHead> --head HEAD --enforce` | `PASS` or pending-return exception with reason |
| Machine Closure Package | `python governance/compat/check_machine_closure_package.py --base <executionBaseHead> --head HEAD --enforce` | `PASS`, `N/A with reason`, or pending-return exception |
| Dispatch quality | `python governance/compat/check_work_order_dispatch_quality.py --base <executionBaseHead> --head HEAD --enforce` | `PASS` or `BLOCKED` with return action |

### 6D. Worker Pending-Return Gate

| Component | Scope trigger | Verification command | Expected result |
|---|---|---|---|
| Execution anchor | every worker run | `git rev-parse --short HEAD` before edits | `executionBaseHead=<hash>` |
| Pending worktree | `WORKER_MUST_NOT_COMMIT` | `git status --short` | staged new files; no `.ts` new files |
| Markdown structural completeness | new governed markdown files | check_markdown_structural_completeness | `PASS` |
| Finding-To-Governance learning | output files may record domain-specificity findings | check_finding_to_governance_learning | `PASS` |
| Machine Closure Package | output files reference closure context | check_machine_closure_package | `PASS` or `N/A with reason` |
| Dispatch quality | this work order is a new dispatch packet | check_work_order_dispatch_quality | `PASS` |

If a component gate reports only expected pending-return residue from
uncommitted artifacts, record the pending-return exception and the exact
reason. Do not record that result as closure PASS.

The startup acknowledgment in the worker return must mirror the active
session state at execution time.

---

## 7. Expected Output Artifacts

| Artifact | Path | Status |
|---|---|---|
| Owner surface map | `docs/reference/CVF_DSCP_T1_OWNER_SURFACE_MAP_2026-06-07.md` | accepted for reviewer commit |
| Schema proposal | `docs/reference/CVF_DSCP_T1_SCHEMA_PROPOSAL_2026-06-07.md` | accepted for reviewer commit |
| Worker return packet | `docs/reviews/CVF_DSCP_T1_OWNER_SURFACE_MAP_WORKER_RETURN_2026-06-07.md` | accepted as RETURNED_PASS_BOUNDED |

---

## 8. Acceptance Criteria

| Criterion | Verification |
|---|---|
| All source paths cite existing file + line range | Section 6A source verification table |
| Domain-specific fields labelled per surface | Owner surface map, column `Domain-specific?` |
| Schema proposal defines all 5 proposed interfaces | Schema proposal Sections 2-4 |
| No new `.ts` implementation file created | `git status --short` shows no new `.ts` files |
| All component gates PASS | Worker Pending-Return Gate table in worker return |
| No runtime, ingestion, provider call, or worker commit | Forbidden scope log in worker return |

---

## Acceptance Receipt Assertion Matrix

DSCP-T1 is a doc-only surface mapping tranche. No runtime retrieval query,
provider receipt, or query acceptance was performed.

| Required value | Observed value | Status |
|---|---|---|
| No runtime query or provider receipt | Worker confirms: no provider call, no live retrieval, no query receipt generated in DSCP-T1 | N/A with reason: doc-only tranche; no runtime query executed |
| Worker Pending-Return Gate pre-return checks | All four component checks run and result recorded in worker return | N/A with reason: pending-return checks may show pending-return residue from uncommitted artifacts; committed-range checks pass only after reviewer commits |

## 9. Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED`; reviewer commit pending | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_DSCP_T1_OWNER_SURFACE_MAP_COMPLETION_2026-06-07.md` | reviewer completion review authored in the same closure batch | PASS |
| Roadmap state | `docs/roadmaps/CVF_DSCP_DOMAIN_AGNOSTIC_SCAN_CONTEXT_PACK_READINESS_ROADMAP_2026-06-07.md` | DSCP-T1 row updated to `CLOSED_PASS_BOUNDED`; T2 and T3 remain NOT_YET_AUTHORIZED | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | DSCP-T1 owner source surface entry added for three source paths | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | DSCP-T1 quick lookup and finding row added | PASS |
| External evidence digest | source surfaces confirmed by Section 6A verification table | no new external artifact hash generated in DSCP-T1 | N/A with reason: doc-only scan tranche; no external artifact produced |
| System loop interlock | no system-loop mutation authorized | DSCP-T1 is doc-only surface mapping; no runtime loop changed | N/A with reason: doc-only; no runtime mutation |
| Session continuity | `AGENT_HANDOFF_V16_2026-06-06.md` | updated in separate session-sync commit after material commit | N/A with reason |

---

## 10. Reviewer Checklist

Codex must verify before committing:

- Owner surface map contains all 4 surface layers with domain-specific field
  labels.
- Schema proposal defines `GovernedArtifactDescriptor`, `GovernanceGateSet`,
  `GovernedContextPackRequest`, `GovernedContextPackage`,
  `GovernedRetrievalReceipt`.
- No new `.ts` file was created or modified.
- All committed-range governance gates PASS after commit.
- DSCP roadmap T1 row updated to `CLOSED_PASS_BOUNDED`.
- Session continuity files updated.

## Evidence Requirements

The worker must record in the worker return:

- `executionBaseHead` captured before any edit.
- List of all files created (staged, not committed).
- For each output artifact: brief evidence that source citations were verified.
- Explicit statement of no-extraction, no-ingestion, no-provider-call,
  no-runtime-mutation, no-commit boundary.
- Component gate results for all four gates.

## Review Gate

Codex must review the DSCP-T1 worker return before deciding T1 closure.
After T1 closes, Codex may authorize DSCP-T2 (contract authoring) separately
if the schema proposal is accepted.

## Closure Checklist

- [x] Owner surface map created with all 4 layers and gap analysis.
- [x] Schema proposal created with all 5 proposed interfaces.
- [x] Worker return packet created with Worker Pending-Return Gate table.
- [x] No new `.ts` implementation file created.
- [x] All component gates PASS or pending-return exception recorded.
- [x] No forbidden scope action occurred.
- [x] Codex reviewed worker return.

## Return-To-Orchestrator Conditions

Return to Codex without marking PASS if:

- any required source file is not found at cited path;
- any proposed interface requires reading artifact body content;
- any forbidden scope action would be required;
- any component gate reports a non-pending-return violation.

## Operator Checkpoint

Operator input is not required for this doc-only surface mapping tranche.
Operator input is required before DSCP-T2 contract authoring, DSCP-T3
runtime pilot, any TypeScript implementation, corpus ingestion, provider
calls, or public-sync.

---

## Claim Boundary

This work order authorizes DSCP-T1 doc-only owner surface mapping and schema
proposal only. It does not authorize DSCP-T2 contract authoring, DSCP-T3
runtime pilot, LPCI2 T12, any TypeScript implementation, any runtime,
ingestion, provider call, public-sync, production readiness, or public
readiness activity.
