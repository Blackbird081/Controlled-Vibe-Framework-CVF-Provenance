# CVF Agent Work Order - MEMCON-T4 Retrieval-Pack Boundary Conformance

Memory class: FULL_RECORD

Status: DISPATCHED

docType: work_order

Date: 2026-06-13

Owner: Codex

Assigned worker: Claude

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `a6902ef2`

executionBaseHead: `a6902ef2`

closureBaseHead: `WORKER_MUST_NOT_SET`

sourceAuthority:
`docs/baselines/CVF_GC018_MEMCON_T4_RETRIEVAL_PACK_BOUNDARY_CONFORMANCE_2026-06-13.md`

rawMemoryReleased=false

completionReviewPath:
`docs/reviews/CVF_MEMCON_T4_RETRIEVAL_PACK_BOUNDARY_CONFORMANCE_COMPLETION_2026-06-13.md`

reviewerOwnedClosurePaths:
`docs/reviews/CVF_MEMCON_T4_RETRIEVAL_PACK_BOUNDARY_CONFORMANCE_COMPLETION_2026-06-13.md`;
`CVF_SESSION/ACTIVE_SESSION_STATE.json`;
`CVF_SESSION/state/**`;
`CVF_SESSION_MEMORY.md`;
`AGENT_HANDOFF_V18_2026-06-12.md`

GC-018:
`docs/baselines/CVF_GC018_MEMCON_T4_RETRIEVAL_PACK_BOUNDARY_CONFORMANCE_2026-06-13.md`

Parent roadmap:
`docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md`

## Purpose

Implement a bounded MEMCON-T4 retrieval-pack boundary helper and focused
conformance tests. The helper must prepare summary-only retrieval-pack input
from consolidated-memory summaries and prove that disallowed memory categories
are excluded before they can be handed toward the existing retrieval policy or
runtime workflow surfaces.

The worker must not wire the helper into a live route, durable store, provider
call, Policy_Local flow, public-sync artifact, generated JSON aggregate, or
autonomous memory loop.

## Authority Chain

| Authority | Path / evidence | Disposition |
| --- | --- | --- |
| Operator request | operator asked Codex to continue by creating a Claude work order for implementation | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V18_2026-06-12.md` | ACCEPT |
| Parent roadmap | `docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md` | ACCEPT |
| T1b schema appendix | `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md` | ACCEPT |
| T3 operator packet contract | `docs/reference/CVF_MEMORY_CONSOLIDATION_LEDGER_OPERATOR_PACKET_CONTRACT_2026-06-13.md` | ACCEPT |
| Existing retrieval policy | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | ACCEPT |
| Existing runtime workflow chain | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts` | ACCEPT |
| GC-018 | `docs/baselines/CVF_GC018_MEMCON_T4_RETRIEVAL_PACK_BOUNDARY_CONFORMANCE_2026-06-13.md` | ACCEPT |

## Agent Roles

| Role | Agent | Boundary |
| --- | --- | --- |
| Orchestrator | Codex | dispatches work order and baseline only |
| Worker | Claude | implements allowed-scope artifacts and returns uncommitted |
| Reviewer / closer | Codex | reviews, fixes only reviewer-owned issues, runs closure gates, commits |

## Intake Role Routing Decision

Intake summary: operator asked Codex to continue by creating the next Claude
work order after MEMCON-T3 closure.

Scope classification: bounded Learning Plane helper plus conformance tests for
retrieval-pack boundary discipline.

Risk sensitivity: medium governance/runtime-adjacent risk because the helper
touches Learning Plane source and names retrieval owner surfaces. Risk remains
bounded because no route wiring, durable storage, provider/API proof,
Policy_Local mutation, public-sync, or live retrieval behavior change is
authorized.

Selected route mode: MULTI_AGENT_MULTI_ROLE.

Role separation basis: Claude acts as implementation worker under
`WORKER_MUST_NOT_COMMIT`; Codex remains reviewer, closer, and committer.

Escalation condition: return to Codex if implementation requires forbidden
paths, existing route wiring, durable store mutation, provider/API proof,
public-sync, generated JSON aggregate architecture, external workspace
mutation, Policy_Local mutation, operator evidence, or a wider claim boundary.

Reason: T4 crosses from MEMCON docs into a small source helper. Multi-agent
separation keeps implementation separate from reviewer closure and session
state authority.

## Required First Reads

Claude must read:

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `AGENT_HANDOFF_V18_2026-06-12.md`
4. `docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md`
5. `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md`
6. `docs/reference/CVF_MEMORY_CONSOLIDATION_LEDGER_OPERATOR_PACKET_CONTRACT_2026-06-13.md`
7. `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts`
8. `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts`
9. `governance/compat/check_memory_consolidation_artifact_quality.py`
10. this work order

## Startup Acknowledgment Required

Claude must begin with:

`Startup acknowledged: current mode=memcon_t4_retrieval_pack_boundary_conformance_dispatched; active handoff=AGENT_HANDOFF_V18_2026-06-12.md; work order=MEMCON-T4; next allowed move=Claude implements allowed-scope MEMCON-T4 helper and tests under WORKER_MUST_NOT_COMMIT and returns uncommitted; parked checkpoint=Policy_Local PL-S1, EC/T12, DEP2/Redis/receipt-anchor remain parked.`

## Commit Mode And Base-Anchor Lifecycle

| Anchor | Value | Owner | Disposition |
| --- | --- | --- | --- |
| dispatchBaseHead | `a6902ef2` | Codex | ACCEPT |
| executionBaseHead | `a6902ef2` | Claude | ACCEPT |
| closureBaseHead | `WORKER_MUST_NOT_SET` | Codex reviewer | ACCEPT |
| Commit mode | `WORKER_MUST_NOT_COMMIT` | Codex | ACCEPT |

Claude must not commit. Claude must record the worker-return base/head and
`git status --short` output in the worker-return packet.

## Dependency Release Evidence

| Dependency | Required evidence | Disposition |
| --- | --- | --- |
| MEMCON-T1a standard closure | material commit `84a46b62`; standard path `docs/reference/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_STANDARD_2026-06-12.md` | ACCEPT |
| MEMCON-T1b schema closure | material commit `f94d2fbd`; schema path `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md` | ACCEPT |
| MEMCON-T2 checker closure | material commit `f83aa7d8`; checker path `governance/compat/check_memory_consolidation_artifact_quality.py` | ACCEPT |
| MEMCON-T3 operator packet closure | material commit `2800e83c`; session sync `a6902ef2`; contract path `docs/reference/CVF_MEMORY_CONSOLIDATION_LEDGER_OPERATOR_PACKET_CONTRACT_2026-06-13.md` | ACCEPT |
| Fresh MEMCON-T4 baseline | `docs/baselines/CVF_GC018_MEMCON_T4_RETRIEVAL_PACK_BOUNDARY_CONFORMANCE_2026-06-13.md` | ACCEPT |

## Current Runtime Freshness Verification

Claude must refresh these anchors before editing:

```powershell
rg -n "MEMCON-T4 Detail|Required conformance|Policy_Local Relationship" docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md
rg -n "MemoryRetrievalPackInput|selectedRecordIds|summaryOnly|rawMemoryReleased|retrievalConsumer|retrievalBoundary|retrievalEligibility|Promotion And Blocking Rules" docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md
rg -n "MEMORY_RETRIEVAL_POLICY_VERSION|MemoryRetrievalCandidate|lifecycleState|BLOCKED_STATES|rawMemoryReleased|evaluateRetrievalRequest" EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts
rg -n "MEMORY_RUNTIME_WORKFLOW_CHAIN_VERSION|MemoryRuntimeWorkflowStatus|runMemoryRuntimeWorkflowChain|rawMemoryReleased" EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts
```

## Pre-Flight Checks

Claude must run these before editing:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base a6902ef2 --head HEAD
```

If the pre-implementation gate fails only on allowed-scope artifacts, Claude
must repair and rerun under the Worker Autonomy rule. If the failure is outside
allowed scope, Claude must return to Codex.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| T4 goal is retrieval-pack boundary | `docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md` | lines 544-560 | `MEMCON-T4` | MEMCON roadmap | ACCEPT |
| T4 connects consolidated memory to existing retrieval policy and runtime workflow surfaces without claiming raw memory release | `docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md` | lines 548-550 | `memory-retrieval-policy.ts`, `memory-runtime-workflow-chain.ts` | MEMCON roadmap | ACCEPT |
| T4 conformance excludes expired, disputed, sensitive, time-ambiguous, stale-blocked memory and includes source path plus confidence in selected context | `docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md` | lines 552-560 | `Required conformance` | MEMCON roadmap | ACCEPT |
| Policy_Local remains downstream and still requires fresh PL-S1 authorization | `docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md` | lines 578-591 | `Policy_Local Relationship` | MEMCON roadmap | ACCEPT |
| Retrieval policy exposes candidate lifecycle state and raw release invariant | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | lines 17-49 | `MemoryRetrievalCandidate`, `rawMemoryReleased` | memory retrieval policy | ACCEPT |
| Retrieval policy blocks expired and disputed lifecycle states | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | lines 52, 147-148, 232-233 | `BLOCKED_STATES` | memory retrieval policy | ACCEPT |
| Existing retrieval policy evaluator exists | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | lines 106-258 | `evaluateRetrievalRequest` | memory retrieval policy | ACCEPT |
| Runtime workflow chain exposes packaged, denied, and deferred statuses while preserving raw release false | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts` | lines 26-60, 95-215 | `runMemoryRuntimeWorkflowChain`, `rawMemoryReleased` | memory runtime workflow chain | ACCEPT |
| Controlled memory gateway preserves raw release false and blocks unauthorized reinjection | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | lines 35-50, 76-88, 120-121 | `rawMemoryReleased`, `memory_reinjection_not_authorized` | controlled memory gateway | ACCEPT |
| MemoryRetrievalPackInput fields include selected/excluded record IDs, summary-only, raw release false, and retrieval consumer | `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md` | lines 149-166 | `MemoryRetrievalPackInput` | MEMCON T1b schema appendix | ACCEPT |
| ConsolidatedMemoryRecord retrieval fields include retrievalBoundary, retrievalEligibility, and raw release false | `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md` | lines 121-147 | `ConsolidatedMemoryRecord` | MEMCON T1b schema appendix | ACCEPT |
| Source authority and relative-date blocking rules apply to retrieval-facing shapes | `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md` | lines 188-198 | `Promotion And Blocking Rules` | MEMCON T1b schema appendix | ACCEPT |
| T3 retrieval preview section requires rawMemoryReleased=false and no raw memory release implication | `docs/reference/CVF_MEMORY_CONSOLIDATION_LEDGER_OPERATOR_PACKET_CONTRACT_2026-06-13.md` | lines 166-181 | `rawMemoryReleased` | MEMCON-T3 operator packet contract | ACCEPT |
| MEMCON checker enforces retrieval-facing raw release boundary on changed MEMCON artifacts | `governance/compat/check_memory_consolidation_artifact_quality.py` | lines 102-108, 355-368 | `RETRIEVAL_BOUNDARY_MARKER`, `_check_retrieval_boundary` | MEMCON artifact quality checker | ACCEPT |

## New Implementation Symbols Authorized

These symbols are new T4 implementation targets, not pre-existing source
claims:

| New symbol | Target file | Purpose | Boundary |
| --- | --- | --- | --- |
| `MEMCON_RETRIEVAL_PACK_BOUNDARY_VERSION` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-consolidation-retrieval-pack-boundary.ts` | version constant for the T4 helper | new T4 source |
| `MemconConsolidatedMemoryRecordInput` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-consolidation-retrieval-pack-boundary.ts` | narrow input shape for consolidated-memory summaries | does not replace doc-only schema appendix |
| `MemconRetrievalPackBoundaryResult` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-consolidation-retrieval-pack-boundary.ts` | result shape with selected/excluded IDs and raw release boundary | no durable storage |
| `buildMemconRetrievalPackBoundary` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-consolidation-retrieval-pack-boundary.ts` | deterministic pack-selection helper | no route wiring or provider call |

## New Files To Create

| Path | Required content |
| --- | --- |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-consolidation-retrieval-pack-boundary.ts` | deterministic MEMCON retrieval-pack boundary helper |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/memory-consolidation-retrieval-pack-boundary.test.ts` | focused conformance tests |
| `docs/reviews/CVF_MEMCON_T4_RETRIEVAL_PACK_BOUNDARY_CONFORMANCE_WORKER_RETURN_2026-06-13.md` | worker return packet with proof manifest |

## Allowed Implementation Scope

Claude may modify:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-consolidation-retrieval-pack-boundary.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/memory-consolidation-retrieval-pack-boundary.test.ts`
- `docs/reviews/CVF_MEMCON_T4_RETRIEVAL_PACK_BOUNDARY_CONFORMANCE_WORKER_RETURN_2026-06-13.md`
- this work order only for worker-return status evidence if needed
- parent roadmap row only to mark worker-return status, not final closure

Claude must not modify:

- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/**`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V18_2026-06-12.md`
- existing retrieval policy or runtime workflow files unless Codex issues a new work order
- route/API files
- durable memory store files
- package export surfaces
- Policy_Local or any external workspace
- public-sync
- provider key files
- generated JSON aggregates

## Allowed / Forbidden Scope

Allowed scope is exactly the paths listed in `Allowed Implementation Scope`.
Forbidden scope is exactly the paths and behaviors listed under `Claude must
not modify` plus the non-goals in the claim boundary.

## Write Ownership

Claude owns worker implementation changes only until return:

- new T4 helper source;
- focused T4 tests;
- worker-return packet;
- optional status evidence inside this work order or parent roadmap row.

Codex owns closure conversion:

- completion review path;
- session state, handoff, and front-door sync;
- final roadmap closure status;
- commits.

## Execution Plan

1. Read the required first-read files and record the startup acknowledgment.
2. Run the pre-flight commands from this work order.
3. Implement the helper with pure deterministic filtering and summary-only
   output.
4. Add focused tests for required conformance and raw release invariant.
5. Run the Required Proof Manifest commands.
6. Draft the worker-return packet with changed-file evidence, proof results,
   fulfillment manifest, unresolved issues, and no-commit statement.
7. Leave artifacts uncommitted and return to Codex.

## Helper Requirements

The helper must:

- accept bounded consolidated-memory summary inputs, not raw transcript dumps;
- select only records with `retrievalEligibility=ELIGIBLE`;
- exclude expired and disputed lifecycle states;
- exclude sensitive records unless the output is summary-only and no raw content
  is emitted;
- exclude `TIME_AMBIGUOUS_BLOCKED`;
- exclude stale-blocked records;
- exclude records with unresolved conflicts;
- exclude records without source authority;
- exclude records without confidence;
- include source path or source authority and confidence in selected summaries;
- emit `summaryOnly=true`;
- emit `rawMemoryReleased=false`;
- expose excluded record IDs with reasons;
- avoid calling providers, storage, external services, routes, or public-sync.

The helper may import existing types or constants from current Learning Plane
source when helpful. It must not modify existing retrieval policy or runtime
workflow files.

## Test Requirements

Focused tests must prove:

- an eligible consolidated record enters the selected pack and carries source
  authority plus confidence;
- expired and disputed records are excluded;
- sensitive records do not release raw content;
- time-ambiguous, stale-blocked, conflicted, source-missing, and
  confidence-missing records are excluded;
- output keeps `summaryOnly=true` and `rawMemoryReleased=false`;
- raw record content is not copied into the retrieval-facing output;
- the helper can produce an input shape compatible with existing retrieval
  owner surfaces without changing those owner surfaces.

## Evidence Requirements

Claude must provide:

- changed-file evidence from `git status --short`;
- command evidence for focused tests, Learning Plane type check, MEMCON checker,
  reviewer-fast, and pre-commit;
- file evidence for helper, tests, and worker return;
- explicit `N/A with reason` for live proof, public-sync, provider/API, OCR,
  Policy_Local, durable storage, route wiring, generated JSON aggregate, and
  session state evidence;
- statement that no commit was created by Claude.

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| Helper source | Created at the required Learning Plane path |
| Focused tests | Created at the required tests path |
| Worker-return artifact | Created at the required review path |
| Expired/disputed exclusion | Tests prove both cannot enter selected pack |
| Sensitive boundary | Tests prove raw sensitive content is not released |
| Time/stale/conflict/source/confidence blocking | Tests prove blocked records are excluded |
| Selected context evidence | Tests prove selected summaries include source authority/path and confidence |
| Raw release boundary | Helper and tests preserve `rawMemoryReleased=false` |
| No route wiring | Existing route/API files remain unchanged |
| Worker commit boundary | Claude returns uncommitted artifacts |

## Worker Autonomy / No-Question Rule

Worker-Autonomy / No-Question Rule: any governance gate failure within allowed
scope must be repaired and rerun by Claude without asking the operator. Claude
must return to Codex only when repair would exceed allowed scope, touch
forbidden paths, alter the claim boundary, consume provider/API quota, mutate
external workspaces, or require operator evidence.

## Required Proof Manifest Atomic Literal Discipline

Each Required Proof Manifest row below contains one command literal only.
Claude must keep new proof rows atomic.

## Required Proof Manifest

| Proof item | Command literal | Required result |
| --- | --- | --- |
| Worktree start state | `git status --short` | records actual worker start state |
| Pre-implementation gate | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base a6902ef2 --head HEAD` | PASS or source-scoped return |
| Focused T4 test | `npm --prefix EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION run test -- --run tests/memory-consolidation-retrieval-pack-boundary.test.ts` | PASS |
| Learning Plane type check | `npm --prefix EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION run check` | PASS |
| MEMCON checker | `python governance/compat/check_memory_consolidation_artifact_quality.py --base a6902ef2 --head HEAD --enforce` | PASS |
| Reviewer-fast early filter | `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` | PASS |
| Pre-commit hook chain | `python governance/compat/run_local_governance_hook_chain.py --hook pre-commit` | PASS |
| Worker return state | `git status --short` | lists uncommitted worker artifacts |

## Required Artifact Manifest

| Artifact | Owner | Required state at worker return |
| --- | --- | --- |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-consolidation-retrieval-pack-boundary.ts` | Claude | created |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/memory-consolidation-retrieval-pack-boundary.test.ts` | Claude | created |
| `docs/reviews/CVF_MEMCON_T4_RETRIEVAL_PACK_BOUNDARY_CONFORMANCE_WORKER_RETURN_2026-06-13.md` | Claude | created |
| `docs/reviews/CVF_MEMCON_T4_RETRIEVAL_PACK_BOUNDARY_CONFORMANCE_COMPLETION_2026-06-13.md` | Codex | reviewer-owned closure artifact |

## Work-Order Fulfillment Manifest

Claude must include this table in the worker-return packet:

| Requirement | Evidence path or command | Worker disposition |
| --- | --- | --- |
| Helper created | path and summary | PASS or BLOCKED |
| Focused tests created | path and summary | PASS or BLOCKED |
| Required conformance covered | path and test list | PASS or BLOCKED |
| rawMemoryReleased boundary present | command or file evidence | PASS or BLOCKED |
| Focused test run | command result | PASS or BLOCKED |
| type check run | command result | PASS or BLOCKED |
| MEMCON checker run | command result | PASS or BLOCKED |
| reviewer-fast run | command result | PASS or BLOCKED |
| pre-commit run | command result | PASS or BLOCKED |

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Evidence expected |
| --- | --- | --- |
| Retrieval-pack boundary | create T4 helper | helper source path |
| Connect to existing retrieval policy and runtime workflow surfaces | produce compatible summary-only pack boundary without modifying owner files | helper tests and no route/runtime-owner diff |
| Expired memory excluded | focused test requirement | focused test output |
| Disputed memory excluded | focused test requirement | focused test output |
| Sensitive memory redacted or summary-only | helper and test requirements | helper source and tests |
| Time-ambiguous memory excluded | helper and test requirements | helper source and tests |
| Stale-blocked memory excluded | helper and test requirements | helper source and tests |
| Source path and confidence included in selected context | helper and test requirements | focused test output |
| Policy_Local remains downstream | forbidden scope and claim boundary | worker-return packet |

## Worker Return Packet Requirements

Claude must return uncommitted artifacts and include:

- startup acknowledgment;
- base/head anchors;
- changed file list;
- Required Proof Manifest results;
- Work-Order Fulfillment Manifest;
- unresolved issues, if any;
- explicit statement that Claude did not commit;
- claim boundary;
- Public Export Disposition.

## Review Gate

Codex must not close this work order until reviewer gates pass on the actual
worker-return range and the worker-return packet records the uncommitted
artifact state.

## Reviewer Closure Conversion

Codex owns reviewer closure. Codex may add the completion review path, update
session state/front door/handoff, update final roadmap closure status, and
commit only after closure gates pass.

## Machine Closure Package

Worker-return evidence must be machine-checkable:

- `git diff --name-status` or equivalent changed-file evidence;
- `git status --short` showing worker-return state;
- focused test output;
- type-check output;
- MEMCON checker output;
- reviewer-fast output;
- pre-commit output;
- explicit `N/A with reason` for live proof, public-sync, provider/API, OCR,
  Policy_Local, durable storage, route wiring, generated JSON aggregate, and
  session continuity evidence.

## Closure Checklist

| Closure item | Owner | Required disposition |
| --- | --- | --- |
| Worker-return packet complete | Claude | PASS |
| Focused tests evidence present | Claude/Codex | PASS |
| Type-check evidence present | Claude/Codex | PASS |
| MEMCON checker evidence present | Claude/Codex | PASS |
| Reviewer-fast evidence present | Claude/Codex | PASS |
| Pre-commit evidence present | Claude/Codex | PASS |
| Completion review authored | Codex | PASS |
| Session state/front door/handoff synced | Codex | N/A with reason - separate session-sync commit follows material closure |
| Final commit created | Codex | N/A with reason - material closure commit follows reviewer conversion |

## Return-To-Orchestrator Conditions

Claude must return to Codex rather than widening scope if any condition appears:

- existing retrieval policy or runtime workflow file needs modification;
- route/API wiring is needed;
- durable memory storage is needed;
- generated JSON aggregate becomes necessary;
- Policy_Local or external workspace changes are needed;
- provider/API proof or secrets are needed;
- public-sync is needed;
- session state or active handoff changes are needed;
- operator evidence is needed;
- a governance gate fails outside allowed scope.

## Operator Checkpoint

No operator checkpoint is required for Claude to execute the allowed-scope T4
helper and conformance-test work. Operator checkpoint is required before
Policy_Local PL-S1, EC activation, route wiring, durable storage, public-sync,
provider/API proof, T12 unlock, high-risk promotion, memory reinjection, or
autonomous mutation.

## Export Surface Decision

This is private provenance work. Do not copy artifacts to public-sync and do
not make a public catalog claim from T4.

## Claim Boundary

This work order authorizes a bounded helper and conformance tests for
MEMCON-T4 only. It does not claim runtime retrieval behavior is changed,
semantic memory correctness is proven, durable memory storage exists, vector
retrieval exists, operator UI exists, Policy_Local is ready, public catalog
export exists, provider/API proof exists, OCR is available, memory reinjection
is authorized, high-risk promotion is authorized, or autonomous mutation is
authorized.

rawMemoryReleased=false

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

No public-sync artifact exists for this private dispatch. Public export is a
separate authorization path.

## Dispatch Packet Authoring Learning Promotion

This work order carries forward the current CVF dispatch controls: source
verification before worker execution, dependency release evidence, worker
autonomy for allowed-scope gate failures, atomic proof rows, reviewer-owned
closure for `WORKER_MUST_NOT_COMMIT`, and explicit route/storage/provider
boundary handling.
