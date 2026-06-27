# CVF Agent Work Order: DSCP-T9 Local Pipeline Harness

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-08

Worker: Claude

Reviewer: Codex

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `f331c10d`

executionBaseHead: `f331c10d`

closureBaseHead: `5c90506a`

---

## Purpose

Implement a focused local deterministic harness proving the closed DSCP-T6,
DSCP-T7, DSCP-T8, DSCP-T3, and DSCP-T4 surfaces compose without raw content
release, raw source release, or governance bypass.

## Authority Chain

Operator instruction 2026-06-08 -> audit:
`docs/audits/CVF_POST_DSCP_T8_NEXT_ROADMAP_AUDIT_2026-06-08.md` -> GC-018:
`docs/baselines/CVF_GC018_DSCP_T9_LOCAL_PIPELINE_HARNESS_2026-06-08.md` ->
roadmap:
`docs/roadmaps/CVF_DSCP_T9_LOCAL_PIPELINE_HARNESS_ROADMAP_2026-06-08.md` ->
this work order.

Prerequisite release evidence:

| Prerequisite | Artifact | Commit | Disposition |
|---|---|---|---|
| DSCP-T6 scan descriptor runtime | `docs/reviews/CVF_DSCP_T6_SCAN_DESCRIPTOR_RUNTIME_COMPLETION_2026-06-08.md` | `13cc1505` | ACCEPT |
| DSCP-T7 ECO multi-domain pilot | `docs/reviews/CVF_DSCP_T7_ECO_MULTI_DOMAIN_PILOT_COMPLETION_2026-06-08.md` | `958f8d2b` | ACCEPT |
| DSCP-T8 MKE1 cross-lane wire-in | `docs/reviews/CVF_DSCP_T8_MKE1_CROSS_LANE_WIREIN_COMPLETION_2026-06-08.md` | `e96aacaf` | ACCEPT |
| Parent DSCP T1-T8 roadmap closure | `docs/roadmaps/CVF_DSCP_DOMAIN_AGNOSTIC_SCAN_CONTEXT_PACK_READINESS_ROADMAP_2026-06-07.md` | `e96aacaf` | ACCEPT |

## Agent Roles

| Role | Agent | Responsibility |
|---|---|---|
| Worker | Claude | Add focused test harness, GC-051 entry, worker return; do not commit |
| Reviewer | Codex | Review, run gates, close and commit if PASS |
| Operator | Human | Authorized roadmap selection and Claude dispatch |

## Scope / Target / Owner Boundary

Allowed scope:

- Create `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.local.pipeline.harness.test.ts`.
- Update `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` only for
  the new harness test path.
- Create
  `docs/reviews/CVF_DSCP_T9_LOCAL_PIPELINE_HARNESS_WORKER_RETURN_2026-06-08.md`.

Reviewer-owned closure scope:

- `docs/reviews/CVF_DSCP_T9_LOCAL_PIPELINE_HARNESS_COMPLETION_2026-06-08.md`
- `docs/roadmaps/CVF_DSCP_T9_LOCAL_PIPELINE_HARNESS_ROADMAP_2026-06-08.md`
- this work order status conversion;
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V17_2026-06-07.md`

Forbidden scope:

- Do not modify runtime source files in CPF, ECO, LPF, or cvf-web.
- Do not run provider calls, load API keys, ingest corpus files, perform OCR,
  create vector retrieval, author PolicyLocal T12, public-sync, push, or
  claim hosted/production/public readiness.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap section | Work order section | Status |
|---|---|---|
| Purpose: local deterministic cross-surface harness | Purpose | TRACED |
| Scope: test file plus GC-051 entry | Scope / Target / Owner Boundary | TRACED |
| Acceptance: ECO path, blocked path, LPF path | Implementation Contract and Acceptance Criteria | TRACED |
| Verification commands | Evidence Requirements | TRACED |
| T12 invariant | Forbidden Scope and Claim Boundary | TRACED |

## Worker Autonomy / No-Question Rule

Worker-Autonomy / No-Question Rule: any governance gate failure within allowed
scope must be repaired and rerun by the worker without escalating to the
operator. If repair requires runtime source modification, provider/key use,
corpus ingestion, T12 authoring, public-sync, or any forbidden path, stop and
return `BLOCKED_SOURCE_NOT_FOUND` with exact evidence.

## Required Artifact Manifest

| Artifact | Type | Required path | Proof literal |
|---|---|---|---|
| Harness test | new TypeScript test | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.local.pipeline.harness.test.ts` | focused vitest PASS |
| GC-051 update | JSON registry update | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | new test path covered |
| Worker return | new Markdown review | `docs/reviews/CVF_DSCP_T9_LOCAL_PIPELINE_HARNESS_WORKER_RETURN_2026-06-08.md` | all evidence fields populated |

## Work-Order Fulfillment Manifest

See `## Required Artifact Manifest` above.

## Required First Reads

| File | Purpose |
|---|---|
| `docs/audits/CVF_POST_DSCP_T8_NEXT_ROADMAP_AUDIT_2026-06-08.md` | Confirm why T9 was selected |
| `docs/baselines/CVF_GC018_DSCP_T9_LOCAL_PIPELINE_HARNESS_2026-06-08.md` | Confirm authorized scope |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.artifact.descriptor.ts` | Verify descriptor helper |
| `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/dscp.eco.adapter.ts` | Verify ECO adapter |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.packer.ts` | Verify governed packer behavior |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.retrieval.receipt.ts` | Verify receipt helper |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.lpf.adapter.ts` | Verify LPF adapter |
| `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/types.ts` | Verify `RAGResult` and `RAGDocument` |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts` | Verify `packageMemoryContext` and raw-memory locks |

## Pre-Flight Checks

| Check | Command | Required result |
|---|---|---|
| Clean working tree | `git status --short` | no unexpected modified files |
| Base HEAD captured | `git rev-parse --short HEAD` | record as `executionBaseHead` |
| T6/T7/T8 release evidence present | inspect prerequisite completion packets | PASS |
| Harness test absent before implementation | `Test-Path -LiteralPath EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.local.pipeline.harness.test.ts` | False |

## Source Verification

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| EXISTS: `buildGovernedArtifactDescriptor` helper | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.artifact.descriptor.ts` | lines 31-60 | `buildGovernedArtifactDescriptor` | `GovernedArtifactDescriptorInput` | ACCEPT |
| EXISTS: `GovernedArtifactDescriptorInput.governanceGates` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.artifact.descriptor.ts` | lines 11-19 | `governanceGates` | `GovernedArtifactDescriptorInput` | ACCEPT |
| EXISTS: `GovernedContextPackerContract.pack` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.packer.ts` | lines 52-99 | `GovernedContextPackerContract` | `GovernedContextPackerContract.pack` | ACCEPT |
| LITERAL_INVARIANT: governed packer emits raw content lock | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.packer.ts` | lines 84-94 | `rawContentReleased` | `GovernedContextPackageEvidence` | ACCEPT |
| LITERAL_INVARIANT: governed packer emits bypass lock | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.packer.ts` | lines 84-94 | `canBypassGovernance` | `GovernedContextPackageEvidence` | ACCEPT |
| EXISTS: governed packer blocked package helper | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.packer.ts` | lines 18-45 | `makeBlockedPackage` | `GovernedContextPackage` | ACCEPT |
| EXISTS: `buildGovernedRetrievalReceipt` helper | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.retrieval.receipt.ts` | lines 30-56 | `buildGovernedRetrievalReceipt` | `GovernedRetrievalReceiptInput` | ACCEPT |
| LITERAL_INVARIANT: retrieval receipt emits raw source lock | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.retrieval.receipt.ts` | lines 52-55 | `rawSourceReleased` | `GovernedRetrievalReceipt` | ACCEPT |
| RUNTIME_BEHAVIOR: receipt gate values come from package evidence | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.retrieval.receipt.ts` | lines 43-51 | `governanceGateResults` | `buildGovernedRetrievalReceipt` | ACCEPT |
| EXISTS: ECO request adapter | `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/dscp.eco.adapter.ts` | lines 19-34 | `buildECOGovernedPackRequest` | `GovernedContextPackRequest` | ACCEPT |
| EXISTS: ECO `RAGResult` shape | `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/src/types.ts` | lines 23-29 | `RAGResult` | ECO RAG types | ACCEPT |
| EXISTS: LPF package adapter | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.lpf.adapter.ts` | lines 42-62 | `buildLPFGovernedPackage` | `GovernedContextPackage` | ACCEPT |
| EXISTS: `MemoryContextBlock` shape | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts` | lines 27-35 | `MemoryContextBlock` | `packageMemoryContext` | ACCEPT |
| LITERAL_INVARIANT: LPF memory packer emits raw memory lock | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts` | lines 100-109 | `rawMemoryReleased` | `packageMemoryContext` | ACCEPT |

## New Doc-Only Fields

None.

## Write Ownership

| Path | Ownership |
|---|---|
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.local.pipeline.harness.test.ts` | Worker-created |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | Worker-updated only for new harness test path |
| `docs/reviews/CVF_DSCP_T9_LOCAL_PIPELINE_HARNESS_WORKER_RETURN_2026-06-08.md` | Worker-created |
| `docs/reviews/CVF_DSCP_T9_LOCAL_PIPELINE_HARNESS_COMPLETION_2026-06-08.md` | Reviewer-created |
| `docs/roadmaps/CVF_DSCP_T9_LOCAL_PIPELINE_HARNESS_ROADMAP_2026-06-08.md` | Reviewer-updated at closure |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T9_LOCAL_PIPELINE_HARNESS_FOR_CLAUDE_2026-06-08.md` | Reviewer-updated at closure |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Reviewer-updated at closure |
| `CVF_SESSION_MEMORY.md` | Reviewer-updated at closure |
| `AGENT_HANDOFF_V17_2026-06-07.md` | Reviewer-updated at closure |
| Runtime source files | FORBIDDEN |

## Execution Plan

1. Capture `executionBaseHead` with `git rev-parse --short HEAD`.
2. Confirm the working tree contains only expected dispatch files before
   implementation.
3. Read all Required First Reads.
4. Create the focused harness test.
5. Add one GC-051 registry entry for the new harness test path.
6. Run CPF `npm run check`.
7. Run focused harness vitest.
8. Run reviewer-fast gate.
9. Author the worker return packet.
10. Stage allowed worker artifacts and return without committing.

## Implementation Contract

Create one focused test file:

`EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.local.pipeline.harness.test.ts`

Required test cases:

1. ECO PASS path:
   - create two `RAGDocument` records from two domains;
   - build two descriptors with `buildGovernedArtifactDescriptor()`;
   - build one PASS `GovernanceContextEnvelope`;
   - build a `GovernedContextPackRequest` with
     `buildECOGovernedPackRequest()`;
   - pack with `createGovernedContextPackerContract()` using deterministic
     `now` and `estimateTokens` dependencies;
   - build a receipt with `buildGovernedRetrievalReceipt()`;
   - assert source artifact IDs, context package ID, `rawContentReleased`,
     `canBypassGovernance`, and `rawSourceReleased`.

2. ECO blocked gate path:
   - build a request whose envelope has `classificationGate: "BLOCKED"`;
   - assert the governed packer returns `innerPackage.packageId === "BLOCKED"`;
   - assert no source artifact IDs are exposed in the blocked package;
   - assert raw locks remain false.

3. LPF path:
   - create a `MemoryContextBlock` using `packageMemoryContext()`;
   - build a governed package with `buildLPFGovernedPackage()`;
   - build a receipt with `buildGovernedRetrievalReceipt()`;
   - assert `rawMemoryReleased`, `rawContentReleased`, and `rawSourceReleased`
     are all false;
   - assert the receipt source artifact IDs match the package evidence.

Do not create runtime helper source unless a reviewer separately authorizes a
new GC-018. This tranche is test-harness-only.

## Evidence Requirements

| Evidence | Required result |
|---|---|
| `npm run check` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION` | PASS |
| `npm run test -- tests/dscp.local.pipeline.harness.test.ts` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION` | PASS |
| `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` | PASS |
| `git diff --name-status` | only allowed worker paths |
| Worker return packet | includes command output summaries and changed-file list |

## Acceptance Criteria

| Criterion | Required result |
|---|---|
| ECO PASS path composes descriptor, adapter, packer, and receipt | PASS |
| ECO blocked path cannot leak source artifact IDs from blocked package | PASS |
| LPF path preserves memory lock into DSCP package and receipt | PASS |
| Receipt gate results derive from package evidence | PASS |
| GC-051 covers new harness test path | PASS |
| No runtime source files modified | PASS |

## Fail Conditions

| Condition | Action |
|---|---|
| Any runtime source file needs modification | STOP and return `BLOCKED_SOURCE_NOT_FOUND` |
| Any provider call or API key use appears necessary | STOP and return to reviewer |
| Any T12, current-law, legal-quality, public-readiness, or production-readiness claim is introduced | STOP and remove claim |
| GC-051 cannot cover the new harness path cleanly | STOP and return exact registry error |
| Test cannot compile due existing cross-package config issue | Return blocked diagnostic; do not patch runtime source |

## Return Packet Requirements

Claude must return uncommitted artifacts with:

- `executionBaseHead`;
- `git status --short`;
- `git diff --name-status`;
- focused check command and result;
- focused test command and result;
- reviewer-fast result;
- GC-051 registry entry identifier;
- exact claim boundary.

## Acceptance Receipt Assertion Matrix

| Required value | Required assertion | Status |
|---|---|---|
| `rawContentReleased` remains false on governed package evidence | focused test | PASS — vitest 3/3 PASS at `5c90506a` |
| `canBypassGovernance` remains false on governed package evidence | focused test | PASS — vitest 3/3 PASS at `5c90506a` |
| `rawSourceReleased` remains false on receipt | focused test | PASS — vitest 3/3 PASS at `5c90506a` |
| `contextPackageId` equals package ID used by receipt | focused test | PASS — vitest 3/3 PASS at `5c90506a` |
| blocked gate returns `BLOCKED` package ID | focused test | PASS — vitest 3/3 PASS at `5c90506a` |
| blocked package does not expose source artifact IDs | focused test | PASS — vitest 3/3 PASS at `5c90506a` |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_DSCP_T9_LOCAL_PIPELINE_HARNESS_COMPLETION_2026-06-08.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_DSCP_T9_LOCAL_PIPELINE_HARNESS_ROADMAP_2026-06-08.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | entry `dscp-t9-local-pipeline-harness` SCANNED at `5c90506a` | PASS |
| Registry Markdown | `CVF_SESSION_MEMORY.md` and `AGENT_HANDOFF_V17_2026-06-07.md` | mode marker `dscp_t9_closed_pass_bounded` updated in closure batch | PASS |
| External evidence digest | no external artifact authorized | N/A | N/A with reason: local deterministic only |
| System loop interlock | no system-loop mutation | test harness only | N/A with reason: no runtime connection |
| Session continuity | `CVF_SESSION/ACTIVE_SESSION_STATE.json`, `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF_V17_2026-06-07.md` | mode `dscp_t9_closed_pass_bounded` in all three | PASS |

## Review Gate

Reviewer must confirm:

1. `git diff --name-status` contains only allowed worker paths.
2. CPF `npm run check` PASS.
3. Focused harness vitest PASS.
4. Reviewer-fast PASS.
5. GC-051 registry covers the new harness test path.
6. Worker return contains all required evidence.

## Closure Checklist

- [x] Worker return reviewed and accepted
- [x] CPF `npm run check` PASS confirmed
- [x] Focused harness vitest PASS confirmed
- [x] GC-051 registry PASS confirmed
- [x] Governance gates PASS confirmed
- [x] Reviewer commits material artifacts
- [x] Completion review authored by reviewer
- [x] Session continuity synced by reviewer

## Return-To-Orchestrator Conditions

Worker returns when:

- all allowed worker artifacts are staged and uncommitted;
- required commands have PASS evidence or a bounded blocker diagnostic;
- no forbidden path is modified;
- worker return packet is complete.

## Operator Checkpoint

operator.checkpoint.waiver: operator authorized Codex to close T6/T7/T8 and
select the next roadmap for Claude execution on 2026-06-08. No additional
operator decision is required for this test-only DSCP-T9 dispatch.

## Reviewer Closure Conversion

```yaml
completionReviewPath: docs/reviews/CVF_DSCP_T9_LOCAL_PIPELINE_HARNESS_COMPLETION_2026-06-08.md
reviewerOwnedClosurePaths:
  - CVF_SESSION/ACTIVE_SESSION_STATE.json
  - CVF_SESSION_MEMORY.md
  - AGENT_HANDOFF_V17_2026-06-07.md
  - docs/roadmaps/CVF_DSCP_T9_LOCAL_PIPELINE_HARNESS_ROADMAP_2026-06-08.md
  - docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T9_LOCAL_PIPELINE_HARNESS_FOR_CLAUDE_2026-06-08.md
closedStatusTokens:
  - CLOSED_PASS_BOUNDED
reviewerClosureCompleted: false
forbiddenClosedEquivalentResidue: []
```

## Claim Boundary

This work order claims a test-only local deterministic integration harness. It
does not claim provider behavior, live governance proof, retrieval quality,
corpus ingestion, OCR, vector search, PolicyLocal T12 readiness, legal advice
quality, current-law status, public readiness, hosted readiness, production
readiness, public-sync, memory reinjection, high-risk promotion, or autonomous
mutation.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order; not public-synced.
