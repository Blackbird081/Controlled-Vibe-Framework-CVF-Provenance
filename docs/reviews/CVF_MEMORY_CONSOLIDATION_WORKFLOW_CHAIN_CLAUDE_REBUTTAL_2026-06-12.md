# CVF Memory Consolidation Workflow Chain - Claude Rebuttal

Memory class: FULL_RECORD

Status: CODEX_REVIEWED_ROADMAP_UPDATED

docType: rebuttal

Date: 2026-06-12

Worker: Claude

Reviewed roadmap:
`docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md`
(Status at review: `DRAFT_READY_FOR_CLAUDE_REBUTTAL`)

---

## Purpose

Rebut the proposed Memory Consolidation Workflow Chain roadmap before dispatch,
per the roadmap's `## Claude Rebuttal Questions` and `## Work Plan` step 1. This
is a read-only review. No build, schema authoring, provider call, Policy_Local
mutation, or memory mutation is performed or authorized.

## Scope / Methodology

Scope: review the draft roadmap only.

Method:

- read the roadmap in full;
- re-verify the roadmap's current-surface table against source-visible
  `EXTENSIONS/` files;
- identify roadmap overclaims, sequencing issues, and dispatch blockers;
- preserve `WORKER_MUST_NOT_COMMIT`;
- return findings to Codex for acceptance and incorporation.

Out of scope:

- implementation;
- schema authoring;
- runtime/source mutation;
- provider/API-key use;
- Policy_Local mutation;
- memory mutation;
- public-sync.

## Worker Mode

WORKER_MUST_NOT_COMMIT was preserved by the worker. Codex reviewed this
rebuttal, incorporated accepted corrections into the roadmap, and owns the
commit.

## Verification Boundary

This rebuttal proves only that the cited current CVF surfaces exist at the
reviewed worktree state and that the roadmap's Gap Statement contains the
overclaims named below. It does not prove runtime correctness of any surface,
does not measure coverage, and does not claim the proposed chain is complete or
safe to build. Findings are source-anchored to current `EXTENSIONS/` files.

---

## Overall Verdict

`ACCEPT_WITH_REQUIRED_CORRECTIONS`.

The roadmap is well-structured, correctly bounded, and its `## Current Surface
Verification` table is accurate: all 10 cited surfaces verify against current
source. The decision to keep memory foundation separate from Policy_Local, to
require fresh GC-018 per tranche, and to block raw-memory release and
hidden-memory authority are all correct and should be kept.

However, the `## Gap Statement` overclaims three "missing" items that already
have partial owner surfaces. Under the Public Catalog Update Rule failure mode
(claiming a capability does not exist when it does), these must be downgraded
from "missing" to "partial / needs-extension" before dispatch. Otherwise
MEMCON-T1 risks re-authoring contracts that already exist instead of extending
them.

---

## Source Verification Of Roadmap's Own Claims

Independently re-verified the roadmap `## Current Surface Verification` table.
All ACCEPT.

| Roadmap claim | Source file | Verified anchor | Status |
| --- | --- | --- | --- |
| Gateway denies global memory scope | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | `global_memory_scope_not_authorized` (memoryScope === "global" branch) | CONFIRMED |
| Gateway blocks unauthorized reinjection | same | `memory_reinjection_not_authorized` (reinject + canReinject !== true) | CONFIRMED |
| Gateway never releases raw memory | same | `rawMemoryReleased: false` in result shape and base decision | CONFIRMED |
| Retrieval lifecycle states exist | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | `lifecycleState: "working" \| "episodic" \| "semantic" \| "procedural" \| "expired" \| "disputed"` | CONFIRMED |
| Retrieval excludes expired and disputed | same | `BLOCKED_STATES = new Set(["expired", "disputed"])` | CONFIRMED |
| W7 carries contradiction flag | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/w7.memory.record.contract.ts` | `contradiction_flag?: boolean` on `W7MemoryRecord` | CONFIRMED |
| Knowledge maintenance signal types | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/knowledge.maintenance.contract.ts` | `KnowledgeMaintenanceSignalType = lint \| contradiction \| drift \| orphan \| staleness` | CONFIRMED |

The roadmap's planning-time surface map is honest. The defect is isolated to
the Gap Statement, addressed next.

---

## Findings / Position

Position: `ACCEPT_WITH_REQUIRED_CORRECTIONS`.

The roadmap should proceed only after correcting three overclaims:

- RF-1: learning-signal intake exists, so the gap is memory-specific
  consolidation intake, not total signal-intake absence;
- RF-2: lifecycle, tier, retrieval, and maintenance primitives exist, so the
  gap is a composing consolidation contract, not total consolidation absence;
- RF-3: a retrieval-time memory workflow chain exists, so MEMCON must be
  framed as pre-store consolidation feeding the existing post-store retrieval
  chain.

The non-blocking recommendations should refine tranche order and scope without
widening implementation authority.

---

## Rebuttal Findings

### RF-1 (CRITICAL) - Gap Statement overclaims "no signal intake lifecycle"

The roadmap `## Gap Statement` states there is "no canonical `MemorySignal` or
`MemoryCandidate` lifecycle for transcript and worker-return intake."

This overclaims. A signal-intake lifecycle already exists for the
learning/feedback lane:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts`
  defines `LearningSignalLane`, `LearningSignalDefectClass`,
  `LearningSignalSeverity`, `LearningSignalDisposition`,
  `LearningSignalIntakeInput`, and `LearningSignalIntakeRecord`
  (version `cvf.learningSignalIntakeBridge.2026-05-29.v1`).

The accurate gap is narrower: there is no *memory-candidate* intake lifecycle
specialized for transcript / worker-return / source-map signals with temporal
and consolidation fields. The new `MemorySignal` should be positioned as a
sibling-or-extension of the existing learning-signal intake, not as net-new
where nothing exists. Required correction: reword to "no memory-specific
candidate intake lifecycle; existing `learning-signal-intake-bridge.ts` covers
defect/feedback signals only and is not a consolidation intake."

### RF-2 (HIGH) - Gap Statement overclaims "no consolidation contract"

The roadmap states there is "no consolidation contract that merges duplicates,
resolves conflicts, and prunes low-value notes."

Partial owner surfaces already exist:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-lifecycle-policy.ts`
  defines `MemoryLifecycleState` and `evaluateLifecycleTransition`, including
  an `expired` transition (`unreinforced_memory_expired`) - this is the prune
  primitive.
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-tier-classifier.contract.ts`
  defines `MemoryTier` (working/task/skill/organizational/long-term/audit/receipt)
  with `persistenceClass` (ephemeral/bounded/durable/append_only) - this is the
  retention/promotion primitive.
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/knowledge.refactor.contract.ts`
  and `knowledge.maintenance.contract.ts` already carry contradiction/drift/
  staleness signal semantics the roadmap itself reuses in Stage 4.

The accurate gap is: no contract that *composes* these into a single
candidate-to-`ConsolidatedMemoryRecord` decision with merge/supersede/dedup
outputs. Required correction: reword "no consolidation contract" to "no
*composing* consolidation contract over existing lifecycle, tier, and
maintenance primitives." MEMCON-T1 must cite and build on
`memory-lifecycle-policy.ts` and `memory-tier-classifier.contract.ts` as inputs,
not re-invent lifecycle states.

### RF-3 (MEDIUM) - Existing runtime chain not mapped; naming collision risk

The roadmap proposes a "Memory Plane workflow chain" but does not map the
already-shipped runtime chain:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts`
  (version `cvf.memoryRuntimeWorkflowChain.mkg5.t1.v1`) already composes
  gateway + retrieval + context-packager + event-hooks into a
  `runMemoryRuntimeWorkflowChain` with `MemoryRuntimeWorkflowStatus`
  (`packaged | denied | deferred`) and `rawMemoryReleased: false`.

This is a *retrieval-time* chain (signals already in store -> packaged
context). The proposed roadmap is an *intake/consolidation-time* chain (raw
signals -> consolidated memory). They are complementary, but the roadmap must
say so explicitly to avoid two artifacts both calling themselves "the memory
workflow chain." Required correction: add a row to `## Current Surface
Verification` for `memory-runtime-workflow-chain.ts` and state that MEMCON
covers the *pre-store consolidation* half, feeding the existing *post-store
retrieval* chain at Stage 6. Also negative-search `MemorySignal`,
`MemoryCandidate`, `ConsolidatedMemoryRecord` against CVF source in MEMCON-T1
before fixing names (the `*WorkflowChain` token already collides conceptually).

### RF-4 (MEDIUM) - MEMCON-T1 is too broad; split standard from schema

Roadmap Rebuttal Question 4 asks this directly. Answer: yes, split.
`## MEMCON-T1 Detail` requires defining nine lifecycle/vocabulary surfaces
*and* a schema appendix in one tranche. Given RF-1/RF-2, T1 must also reconcile
against three existing contracts. That is too much for one closure with a clean
source-verification table. Recommendation: T1a = standard + vocabulary +
existing-owner reconciliation map; T1b = schema appendix + field tables. Keep
both doc-only, no GC-023 risk if split.

### RF-5 (MEDIUM) - Temporal normalization should precede consolidation

Roadmap Rebuttal Question 5. Answer: yes, as a gate, not a separate tranche.
`temporalNormalizationStatus = TIME_AMBIGUOUS_BLOCKED` already blocks
consolidation in Stage 3. That ordering is correct. But MEMCON-T2 (the temporal
checker) is sequenced *after* T1 and the consolidation vocabulary - meaning the
standard could ship consolidation decisions before the blocking checker exists.
Recommendation: keep T2's *rule* definition inside T1 (so consolidation never
ships without the temporal block defined), and keep only the *machine checker*
in T2. This matches the project's "rule first, machine check second" philosophy
in CLAUDE.md.

### RF-6 (LOW) - Operator packet Markdown-first is correct

Roadmap Rebuttal Question 6. Answer: yes, Markdown-only first (Stage 5 / T3).
The `## MEMCON-T3 Detail` already hedges JSON "if entries become large" and
defers to the JSON generated-aggregate discipline. No change needed; confirm
explicitly that the first T3 deliverable is Markdown and JSON is a follow-up
only when the ledger is append-heavy.

### RF-7 (LOW) - Cross-agent consistency belongs after retrieval-pack boundary

Roadmap Rebuttal Question 7. Answer: the current order (T4 cross-agent before
T5 retrieval) is defensible but inverts dependency. Retrieval-pack boundary
(T5) is the narrower, source-anchored contract that connects to the *existing*
`memory-retrieval-policy.ts` `BLOCKED_STATES`. Cross-agent consistency (T4) is a
new ledger with no existing owner and higher design risk. Recommendation: swap
to T4=retrieval-pack boundary (lower risk, extends existing surface),
T5=cross-agent consistency (higher risk, net-new). This de-risks the wave tail.

### RF-8 (PASS) - No tranche authorizes autonomous memory mutation

Roadmap Rebuttal Question 8. Answer: confirmed clean. `## Out of scope`,
`## Non-Goals`, every `MEMCON-Tn must not` block, and `## Claim Boundary` all
forbid autonomous memory mutation, durable truth-write without review, and
hidden-memory authority. The gateway's `rawMemoryReleased: false` and the
retrieval `BLOCKED_STATES` reinforce this at the contract level. No finding.

---

## Disposition Summary

| Finding | Severity | Disposition |
| --- | --- | --- |
| RF-1 signal-intake overclaim | CRITICAL | MUST FIX before dispatch - reword gap |
| RF-2 consolidation-contract overclaim | HIGH | MUST FIX - reword + cite existing primitives |
| RF-3 runtime-chain not mapped | MEDIUM | MUST FIX - add surface row + clarify pre/post-store split |
| RF-4 T1 too broad | MEDIUM | SHOULD FIX - split T1a/T1b |
| RF-5 temporal rule sequencing | MEDIUM | SHOULD FIX - rule in T1, checker in T2 |
| RF-6 operator packet Markdown-first | LOW | CONFIRM in text |
| RF-7 T4/T5 swap | LOW | RECOMMEND swap |
| RF-8 no autonomous mutation | PASS | No action |

## Required Corrections Before Dispatch (blocking)

1. RF-1: downgrade "no signal intake lifecycle" to "no memory-specific
   consolidation intake; learning-signal-intake-bridge covers feedback only."
2. RF-2: downgrade "no consolidation contract" to "no composing contract over
   existing lifecycle/tier/maintenance primitives," and cite
   `memory-lifecycle-policy.ts` + `memory-tier-classifier.contract.ts` as
   MEMCON-T1 inputs.
3. RF-3: add `memory-runtime-workflow-chain.ts` to the surface table; state
   MEMCON is the pre-store consolidation half feeding the existing post-store
   retrieval chain.

## Non-Blocking Recommendations

- RF-4 split MEMCON-T1 into T1a (standard) and T1b (schema).
- RF-5 keep temporal-block *rule* in T1, *checker* in T2.
- RF-7 swap T4 (retrieval-pack boundary) before T5 (cross-agent).

## Risk / Corrective Action

Primary risk: dispatching the roadmap without corrections would cause MEMCON-T1
to re-author or collide with existing CVF memory surfaces.

Corrective action:

- update the roadmap Gap Statement from absolute absence claims to
  partial-owner/needs-extension claims;
- add existing owner rows for learning-signal intake, memory lifecycle, tier
  classification, and memory runtime workflow chain;
- split standard/schema work into T1a and T1b;
- keep temporal rule definition in T1a and checker implementation in T2;
- keep Policy_Local and runtime memory mutation blocked.

## Finding-To-Governance Learning Disposition

The recurring pattern (RF-1/RF-2/RF-3) is: a roadmap Gap Statement asserting a
capability is "missing" without a negative-search against current
`EXTENSIONS/` owners. This is the same defect class the Public Catalog Update
Rule was written to prevent (the Review CVF.md three-factual-errors incident).
Promotion candidate: a roadmap-authoring checklist item requiring every
"missing" / "no X exists" Gap Statement line to carry a negative-search
command and result, mirroring the negative-search discipline already required
for new symbol names. `MACHINE_CHECK_CANDIDATE` only after the checklist text
exists.

| Finding | Defect class | Learning lane | Escalation state | Next control action | Result |
| --- | --- | --- | --- | --- | --- |
| Roadmap Gap Statement used absolute absence claims while partial owner surfaces existed | `ORCHESTRATOR_PACKET_GAP` | `GOVERNANCE_CONTROL_PLANE` | `MACHINE_CHECK_CANDIDATE` | Add roadmap-authoring checklist or future checker requiring negative-search or `PARTIAL_OWNER` evidence for "missing/no X exists" claims | RECORDED |
| Runtime/provider/cost findings | N/A | N/A | N/A_WITH_REASON | No runtime execution, provider call, cost, token, latency, or production behavior finding in this rebuttal | N/A |

## Acceptance Checklist

- [x] Roadmap read in full (557 lines)
- [x] All 10 surface-verification claims independently re-verified - CONFIRMED
- [x] Three overclaims source-anchored to existing files
- [x] All 8 Claude Rebuttal Questions answered
- [x] No build, schema authoring, provider call, or memory mutation performed
- [x] No Policy_Local mutation
- [x] WORKER_MUST_NOT_COMMIT preserved
- [x] Verdict + blocking corrections + learning disposition recorded

## Worker Return Signal

`WORKER_RETURN_READY`. Codex to review, incorporate accepted findings into the
roadmap without widening implementation authority, then decide
dispatch-vs-revise.
