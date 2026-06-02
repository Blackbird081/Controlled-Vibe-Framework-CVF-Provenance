# CVF Work Order - MKG7-T1 Memory Plane Operational Contract

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-01

## Purpose

Produce a documentation-only Memory Plane Operational Contract that formalizes,
from current source, the bounded runtime contract the Memory plane already
implements. The contract names inputs, authorization signals, route surfaces,
the returned readout shape, forbidden fields, lifecycle states, the
advisory-only execution boundary, and the surface scope of the
`canReinject=false` invariant, each backed by a source-verified citation. Every
later MKG7 tranche (T2-T7) must cite this contract.

Success means: one reference document exists with a Source Verification table
whose `ACCEPT` rows cite real source files and line/symbol evidence; the
`canReinject=false` claim is scoped to the readout/advisory surface; the durable
write is described as present and fail-closed; markdown-structural and
public-export gates pass; both the contract and a completion review are left
pending and uncommitted.

## Authority Chain

| Authority | Path / basis | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-01 request to create work orders so another agent executes MKG7 | ACCEPT |
| MKG7-T1 GC-018 | `docs/baselines/CVF_GC018_MKG7_T1_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md` | ACCEPT |
| MKG7 roadmap | `docs/roadmaps/CVF_MKG7_MEMORY_PLANE_OPERATIONALIZATION_ROADMAP_2026-06-01.md` | ACCEPT |
| MKG tranche completion review | `docs/reviews/CVF_MKG_MEMORY_SYSTEM_TRANCHE_COMPLETION_2026-06-01.md` | ACCEPT_AS_POINTER |
| Worker autonomy standard | `docs/reference/CVF_WORKER_AUTONOMY_DISPATCH_PROMPT_STANDARD_2026-06-01.md` | ACCEPT |

Authority boundary:

- This work order does not authorize work outside the cited authority chain.
- If any authority artifact conflicts with this work order, stop and reconcile
  before implementation.

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | dispatch packet and review pending contract | no silent boundary expansion |
| Worker | write the source-verified contract document and pending completion review | no runtime/source edits, no commit, no live proof |
| Reviewer | verify every contract claim is source-backed and that boundary wording is accurate | reject memory-only or mis-stated invariant claims |

Operator approval required for: scope expansion, runtime/source edits, live
proof, public-sync, push, or claim-boundary change.

## Scope

Allowed scope:

- create `docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md`;
- create `docs/reviews/CVF_MKG7_T1_MEMORY_PLANE_OPERATIONAL_CONTRACT_COMPLETION_2026-06-01.md`;
- read the source files named in Required First Reads;
- run listed governance gates;
- fix allowed-scope documentation-format or gate defects and rerun.

Forbidden scope:

- any edit to runtime/source `.ts` files (the contract is documentation-only);
- adding new runtime fields, types, routes, or enums;
- provider calls or live proof;
- prompt injection or reinjection;
- raw candidate `content` reproduction in the document;
- persistence mutation or graph mutation;
- `.private_reference/legacy/**` edits;
- public-sync, push, publish, or local commit by the worker;
- destructive action.

Risk ceiling: R1 documentation-only.

## Required First Reads

- `docs/baselines/CVF_GC018_MKG7_T1_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md` - authorization and boundary
- `docs/roadmaps/CVF_MKG7_MEMORY_PLANE_OPERATIONALIZATION_ROADMAP_2026-06-01.md` - T1 workstream detail and roadmap-level Source Verification Block
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` - request body, auth signals, returned shape, sentinel guard
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route-constants.ts` - route version literal
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` - projection helper
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts` - chain result invariants
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-lifecycle-policy.ts` - tier-state machine and tier-scoped canReinject
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` - retrieval result fields
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` - fail-closed write branches and receipt invariants
- `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md` - closure-quality expectations

## Pre-Flight Checks

Capture `baseHead` before material implementation:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/check_work_order_dispatch_quality.py --base <baseHead> --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <baseHead> --head HEAD
```

`baseHead` at dispatch is `ad9c2b75` (the committed MKG7 roadmap). Expected
results: dispatch-quality and pre-implementation autorun gates PASS.

If a pre-flight check fails inside Allowed scope, repair and rerun. The worker
must not continue past a failed autorun phase gate.

## 6A. Source-Fidelity Pass

Existing paths verified: all Required First Reads exist (verified by
orchestrator 2026-06-01). Planned new paths marked NEW: the contract document
and the completion review. No new runtime symbols are introduced.

### Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Readout request body fields | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | lines 9-32 | `MemoryRuntimeReadoutBody` | readout route | ACCEPT |
| Service-token + session auth signals | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | lines 147-163 | `verifyServiceTokenRequest`, `verifySessionCookie` | readout route | ACCEPT |
| Returned readout response shape | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | lines 198-204 | `memoryRuntimeReadout` | readout route response | ACCEPT |
| Readout surface returns false invariants | LITERAL_INVARIANT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | lines 202-203 | `rawMemoryReleased`, `canReinject` | readout route response | ACCEPT |
| Raw-content sentinel guard | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | lines 7, 194-196 | `RAW_SENTINEL` | readout route | ACCEPT |
| Route version literal | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route-constants.ts` | line 2 | `MEMORY_RUNTIME_READOUT_ROUTE_VERSION` | route constants | ACCEPT |
| Chain result invariants false | LITERAL_INVARIANT | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts` | lines 60-61 | `rawMemoryReleased`, `canReinject` | `MemoryRuntimeWorkflowResult` | ACCEPT |
| Chain status set | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts` | line 29 | `MemoryRuntimeWorkflowStatus` | workflow chain | ACCEPT |
| Tier-state machine states | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-lifecycle-policy.ts` | lines 4-11 | `MemoryLifecycleState` | tier lifecycle policy | ACCEPT |
| Tier canReinject true for semantic/procedural | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-lifecycle-policy.ts` | line 44 | `canReinject` | `transition` | ACCEPT |
| Retrieval result fields | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | lines 40, 88 | `MemoryRetrievalResult`, `evaluateRetrievalRequest` | retrieval policy | ACCEPT |
| Durable write fails closed | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 195, 201 | `write` | `InProcessDurableMemoryStore` | ACCEPT |
| Durable provenance floor | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | line 98 | `MIN_PROVENANCE_SCORE` | durable store | ACCEPT |

Source priority: current runtime/source file first. The MKG tranche completion
review is a pointer only, not source authority for any field.

Forbidden closeout vocabulary (`UNVERIFIED`, `TBD`, `TODO`, `confirm later`,
`verify during implementation`) must not appear as an allowed disposition,
acceptance criterion, or closure item.

## 6B. Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| Name Memory plane inputs | Execution Plan step 2 | contract Inputs section citing `MemoryRuntimeReadoutBody` | reviewer source check | DISPATCHED |
| Name authorization signals | Execution Plan step 2 | contract Auth section citing route auth | reviewer source check | DISPATCHED |
| Name allowed route surfaces | Execution Plan step 2 | contract Surfaces section (`/api/memory/readout`, proposed `/api/execute` advisory point) | reviewer source check | DISPATCHED |
| Name returned readout shape and forbidden fields | Execution Plan step 3 | contract Response + Forbidden Fields sections | reviewer source check | DISPATCHED |
| Name lifecycle states | Execution Plan step 3 | contract Lifecycle section distinguishing tier states from T2 readout-eligibility states | reviewer source check | DISPATCHED |
| Scope canReinject=false to readout/advisory surface | Execution Plan step 4 | contract Invariant Scope section | reviewer source check | DISPATCHED |
| Describe durable write as present + fail-closed | Execution Plan step 4 | contract Durable Boundary section | reviewer source check | DISPATCHED |
| Cite source not memory summaries | Source Verification Block | contract Source Verification table | dispatch-quality + reviewer | DISPATCHED |

## 6C. Worker Autonomy / No-Question Rule

The worker must not ask the operator before performing non-destructive actions
inside Allowed scope: reading named files, writing the contract and completion
review, running `git status`/`diff`/`rev-parse`, running listed gates, fixing
documentation-format defects, and rerunning failed gates after allowed-scope
remediation.

Ask the operator only if the next action would exceed Allowed scope, edit any
runtime/source `.ts` file, edit legacy source, run live/provider proof, use
secrets/quota, public-sync, push/publish, commit, change risk or claim
boundary, release a `HOLD_*` prerequisite, touch forbidden paths, or perform
destructive/irreversible action.

If a machine gate fails inside Allowed scope, repair it and rerun. Do not ask
whether to fix routine gate failures.

## 6D. Pending Artifact Evidence Finality

The worker must not commit. Leave the contract and completion review pending for
orchestrator review. Do not claim `git status --short` is clean; record the
actual pending status lines. Do not cite a committed-only or empty range (such
as `HEAD~1..HEAD`, or a base equal to head) as proof for the pending documents;
use working-tree-aware validation, or note that clean-status evidence is
post-commit and command-backed.

## 6E. Self-Reported Gate Evidence Consistency

If the completion review records gate results, those results must match the
current state. A finding-bearing review must include
`## Finding-To-Governance Learning Disposition`. Do not record autorun `PASS`
while a required section is missing. Update recorded gate results after any
rerun.

## 6G. Work-Order Fulfillment Manifest

### Required Artifact Manifest

| Path | Required at handoff | Purpose |
| --- | --- | --- |
| `docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md` | Yes | source-verified Memory plane operational contract |
| `docs/reviews/CVF_MKG7_T1_MEMORY_PLANE_OPERATIONAL_CONTRACT_COMPLETION_2026-06-01.md` | Yes | pending completion review |

### Forbidden Path Manifest

| Path | Reason |
| --- | --- |
| `EXTENSIONS/**/*.ts` | T1 is documentation-only; no runtime/source edits |
| `.private_reference/legacy/**` | legacy source must not be edited |
| `docs/roadmaps/CVF_MKG7_MEMORY_PLANE_OPERATIONALIZATION_ROADMAP_2026-06-01.md` | already committed; T1 does not re-edit the roadmap |

### Required Proof Manifest

| Proof | Path | Required literal | Required at handoff |
| --- | --- | --- | --- |
| Contract scopes the reinjection invariant | `docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md` | `canReinject` | Yes |
| Contract names the raw-leak sentinel | `docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md` | `RAW_MEMORY_CONTENT_MUST_NOT_LEAK` | Yes |
| Contract describes durable fail-closed branch | `docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md` | `actorAuthorized` | Yes |

## 7. Write Ownership

Owned files:

- `docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md`
- `docs/reviews/CVF_MKG7_T1_MEMORY_PLANE_OPERATIONAL_CONTRACT_COMPLETION_2026-06-01.md`

Forbidden paths: all `EXTENSIONS/**/*.ts`, the committed roadmap, legacy source.

Write mode: create-only. Leave both files pending and uncommitted.

## 8. Execution Plan

1. Capture `baseHead` and actual dirty worktree status; run pre-flight gates.
2. Read all Required First Reads. Confirm each Source Verification Block row
   against the cited file and line.
3. Write the contract document with these sections, each citing source:
   Purpose; Inputs; Authorization Signals; Allowed Route Surfaces; Returned
   Readout Shape; Forbidden Fields; Lifecycle States (tier-state machine vs the
   T2 readout-eligibility states to be added later); Advisory-Only Execution
   Boundary; Durable Write Boundary (present + fail-closed); Source Verification
   table; Claim Boundary.
4. In the Invariant Scope subsection, state that `canReinject=false` applies to
   the readout/advisory surface (`route.ts:203`, chain result lines 60-61) and
   that the tier policy's `canReinject:true` for semantic/procedural
   (`memory-lifecycle-policy.ts:44`) is a separate, non-prompt-assembly signal.
   State that the durable write is present and fails closed
   (`durable-memory-store.ts:201`), not disabled and not an open exposure.
5. Run markdown structural completeness and public-export gates.
6. Write the pending completion review with actual changed files, command
   results, Public Export Disposition, Finding-To-Governance Learning
   Disposition, and Claim Boundary.
7. Leave both documents pending and uncommitted.

Each step input is the prior artifact/source; output is the named document;
validation is the reviewer source check plus the listed gates; stop condition
is any forbidden-path or runtime-edit requirement.

## 9. Evidence Requirements

- `python governance/compat/check_markdown_structural_completeness.py --base <baseHead> --head HEAD --enforce`
- `python governance/compat/check_public_export_disposition.py --base <baseHead> --head HEAD --enforce`
- `python governance/compat/check_work_order_dispatch_quality.py --base <baseHead> --head HEAD --enforce`
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <baseHead> --head HEAD`
- actual `git status --short`
- `git diff --name-status`
- pending completion review

Evidence Trace Block:

- Claim: contract formalizes existing Memory plane source without new fields
- Command: reviewer source check against Source Verification Block + gates above
- Result: to be recorded by worker
- Key path: `docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md`
- Verdict: to be recorded by worker

## 10. Acceptance Criteria

- [x] Contract document exists with all sections in Execution Plan step 3
- [x] Every contract claim cites a source file with line/symbol evidence
- [x] `canReinject=false` is explicitly scoped to the readout/advisory surface
- [x] Tier policy `canReinject:true` for semantic/procedural is acknowledged as a separate signal
- [x] Durable write described as present and fail-closed, not disabled or exposed
- [x] Source Verification table present with no `UNVERIFIED`/`TBD`/`TODO` dispositions
- [x] Markdown-structural and public-export gates PASS
- [x] Both documents left pending and uncommitted with actual git status recorded

Fail conditions:

- [x] Any runtime/source `.ts` file edited
- [x] Any contract claim sourced only from memory/roadmap prose where runtime source exists
- [x] Blanket `canReinject=false` claim that contradicts the tier policy
- [x] Durable write described as disabled or as an ungoverned exposure
- [x] Worker commits, pushes, or asks whether to fix an allowed-scope gate failure

Closure is blocked if any fail condition is present.

## 11. Review Gate

Implementation may proceed after the MKG7-T1 GC-018 is filed (it is) and the
`pre-implementation` autorun gate passes. Closure (by orchestrator, not worker)
may proceed after reviewer no-blocking objection and a recorded `pre-closure`
gate.

A gate failure inside Allowed scope is authorization to repair and rerun, not a
reason to ask the operator. Reviewer silence is not approval unless the operator
records a waiver.

## 12. Closure Checklist

- N/A with reason: the worker must not close or commit MKG7-T1. The worker
  returns the pending contract and completion review for orchestrator review.
  Orchestrator performs the committed-range closure checklist.

## 13. Return-To-Orchestrator Conditions

Return without continuing if: pre-flight fails outside Allowed scope; a Source
Verification row cannot be confirmed against its cited file
(`BLOCKED_SOURCE_NOT_FOUND`); the contract would require a runtime/source edit;
scope conflict is found; or public/provenance boundary is unclear.

## Worker Dispatch Prompt

Send this exact prompt with the work order:

```text
You are assigned MKG7-T1 Memory Plane Operational Contract.

Primary work order:
docs/work_orders/CVF_WO_MKG7_T1_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md

Read the complete work order before writing. Implement only its Allowed scope.

Critical rules:
- documentation-only: do NOT edit any .ts file;
- create one contract document under docs/reference/ plus a pending completion
  review under docs/reviews/;
- every claim must cite a source file with line/symbol evidence; the MKG
  completion review is a pointer, not source authority;
- scope canReinject=false to the readout/advisory surface (route.ts:203, chain
  result lines 60-61); acknowledge memory-lifecycle-policy.ts:44 returns
  canReinject:true for semantic/procedural as a separate, non-prompt signal;
- describe the durable write (durable-memory-store.ts:201) as present and
  fail-closed, NOT disabled and NOT an open exposure;
- run markdown-structural and public-export gates.

Worker Autonomy Rule:
Do not ask the operator before non-destructive actions inside Allowed scope. If
a gate fails inside Allowed scope, repair it and rerun. Do not ask whether to
fix routine failures.

Pending Artifact Rule:
Do not commit. Leave both documents pending for orchestrator review. Record
actual git status. Do not claim a clean worktree and do not use HEAD~1..HEAD as
proof for pending files.

Stop and ask only if the next action would exceed Allowed scope, edit a .ts or
forbidden path, edit legacy source, run live/provider proof, use secrets/quota,
public-sync, push/publish, commit, change risk or claim boundary, release a HOLD
prerequisite, or perform a destructive/irreversible action.
```

## Operator Checkpoint

Operator requested MKG7 work orders so another agent can execute the final
Memory-plane closing roadmap. T1 is dispatched first because it is
documentation-only and every later MKG7 tranche cites its contract.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private documentation-only contract work order. No public-sync remote,
public repository commit, or public artifact path is included.

## Claim Boundary

MKG7-T1 is dispatched as a documentation-only Memory Plane Operational Contract
that formalizes existing source behavior. It does not authorize runtime/source
changes, new fields, provider execution, live proof, prompt injection,
reinjection, raw Memory release, persistence mutation, graph mutation, new
memory tiers, hosted readiness, production readiness, public readiness,
public-sync, push, or autonomous mutation.
