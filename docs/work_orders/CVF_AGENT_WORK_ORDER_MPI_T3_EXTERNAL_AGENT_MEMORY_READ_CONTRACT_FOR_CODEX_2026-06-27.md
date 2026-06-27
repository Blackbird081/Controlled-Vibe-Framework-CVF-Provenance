# CVF Agent Work Order MPI-T3 External Agent Memory Read Contract For Codex

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

executionBaseHead: eeb0e532

## Purpose

This work order is the tactical execution packet for MPI-T3 contract-only
closure. It authorizes Codex to create the external-agent memory read reference
contract and update the parent Memory Plane navigation surfaces without
changing runtime behavior.

## Authority Chain

- Operator instruction: continue and proactively audit/do the next allowed CVF foundation move.
- Active session front door: `CVF_SESSION_MEMORY.md`.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V23_2026-06-26.md`.
- Parent roadmap: `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md`.
- GC-018 baseline: `docs/baselines/CVF_GC018_MPI_T3_EXTERNAL_AGENT_MEMORY_READ_CONTRACT_2026-06-27.md`.
- Agent handoff contract: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

## Agent Roles

Assigned agent: Codex

Role pattern: single-agent dispatcher/implementer/reviewer/closer.

Commit owner: Codex reviewer/closer after local gates pass.

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V23_2026-06-26.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md`
- `docs/reference/CVF_MEMORY_PLANE_MAP.md`
- `docs/reference/learning_signal_chain/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts`

## Pre-Flight Checks

- `git status --short`
- `git rev-parse --short HEAD`
- ADIF resolver query recorded in this work order.
- Source verification search/read for each runtime field, symbol, and contract token.

## Objective

Create and close the MPI-T3 external-agent memory read contract as a bounded
reference-only tranche. The output must let future external-agent adapter
authors know what memory read request/response shape they may map to, while
preserving the existing route, projection, raw-release, reinjection, registry,
durable-store, provider/live, and public boundaries.

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | Codex acts as dispatcher, implementer, reviewer/closer, then session-sync steward in separate commit |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=eeb0e532`; `executionBaseHead=eeb0e532`; `closureBaseHead=eeb0e532`; session-sync base is the material commit |
| changedSetScope(phase) | material phase is GC-018 baseline, work order, reference contract, completion review, Memory Plane map, and MPI roadmap only; session-sync phase is active front-door/state/handoff only |
| traceScope(phase, actor) | material trace covers MPI-T3 contract closure; session-sync trace covers continuity only |
| commitOwner(phase) | Codex owns material commit and separate session-sync commit |
| crossBatchIsolation | no public-sync, runtime, route, registry, generated-state, provider/live, adapter, package, resolver, DICE, or session-sync is mixed into the material commit |
| Before status evidence | `dispatchBaseHead=eeb0e532`; worktree clean before authoring |
| nextMoveSurfaces | update only after material commit because current mode and next allowed move change |
| Closer designation | Codex reviewer/closer |

## Allowed Scope

- `docs/baselines/CVF_GC018_MPI_T3_EXTERNAL_AGENT_MEMORY_READ_CONTRACT_2026-06-27.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_MPI_T3_EXTERNAL_AGENT_MEMORY_READ_CONTRACT_FOR_CODEX_2026-06-27.md`
- `docs/reference/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_READ_CONTRACT.md`
- `docs/reviews/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_READ_CONTRACT_COMPLETION_2026-06-27.md`
- `docs/reference/CVF_MEMORY_PLANE_MAP.md`
- `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md`
- active session sync surfaces after material closure only

## Forbidden Scope

- runtime implementation or tests;
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts`;
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts`;
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/scan-registry-memory-projection.ts`;
- corpus registry aggregate/source/generator mutation;
- service-token creation, transmission, or verification changes;
- CLI/MCP adapter, MCP tool, shell bridge, IDE bridge, queue, daemon, watcher, or helper implementation;
- provider/live proof, public-sync, package activation, resolver mutation, generated workspace state, DICE, or push.

## Write Ownership

Codex may edit only the allowed scope files in the material phase. Codex may
edit active session continuity surfaces only after the material commit and only
to record the closed MPI-T3 state and next allowed move.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| MPI roadmap names MPI-T3 as External Agent Memory Read Contract | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | Work Plan row `MPI-T3` | `MPI-T3` | MPI roadmap | ACCEPT |
| MPI roadmap says external read contract needs separate authorization | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | Acceptance Criteria row `External read contract` | `External read contract` | MPI roadmap | ACCEPT |
| Memory Plane map records Memory readout route as authenticated and summary-only | `docs/reference/CVF_MEMORY_PLANE_MAP.md` | LPF Memory Runtime Readout | `POST /api/memory/readout` | Memory Plane map | ACCEPT |
| Memory Plane map records MPI-T3 as parked before this work | `docs/reference/CVF_MEMORY_PLANE_MAP.md` | MPI Tranche Progression row `MPI-T3` | `MPI-T3` | Memory Plane map | ACCEPT |
| Runtime request body fields are source-owned by current route | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | interface declaration | `MemoryRuntimeReadoutBody` | Memory readout route | ACCEPT |
| Route validates `operationId`, `sessionId`, `projectId`, `actorId`, `actorRole`, `scope`, `riskLevel`, and `candidates` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | `validateBody` | `validateBody` | Memory readout route | ACCEPT |
| Route accepts service-token or session auth | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | `POST` auth branch | `verifyServiceTokenRequest`; `verifySessionCookie` | Memory readout route | ACCEPT |
| Route response fixes `rawMemoryReleased=false` and `canReinject=false` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | response object | `rawMemoryReleased`; `canReinject` | Memory readout route | ACCEPT |
| Projection omits candidate `content` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` | `sanitizeCandidates` | `content` | memory runtime readout projection | ACCEPT |
| Projection fixes `rawMemoryReleased=false` and `canReinject=false` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` | projection object | `rawMemoryReleased`; `canReinject` | memory runtime readout projection | ACCEPT |
| LSC-T6 defines contract-only external-agent CLI/MCP boundary | `docs/reference/learning_signal_chain/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT.md` | Scope and Claim Boundary | `adapterContractOnly` | LSC-T6 reference contract | ACCEPT |
| MPI-T2 closed without external-agent read behavior | `docs/reviews/CVF_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION_COMPLETION_2026-06-22.md` | Risk / Corrective Action row | `MPI-T3` | MPI-T2 completion review | ACCEPT |

## New Doc-Only Fields

| New doc-only field | Purpose | Runtime disposition |
|---|---|---|
| `externalAgentMemoryReadRequest` | portable documentation name for a future adapter's request mapping | DOC_ONLY_NEW |
| `externalAgentMemoryReadout` | portable documentation name for a future adapter's response mapping | DOC_ONLY_NEW |
| `externalAgentNoReadableMemoryAssertion` | portable documentation name for a no-readable-memory response | DOC_ONLY_NEW |
| `adapterContractOnly` | explicit documentation flag that this tranche creates no adapter behavior | DOC_ONLY_NEW |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`mpi_external_agent_memory_read_contract`, role=`dispatcher`, lifecyclePhase=`dispatch`

`python governance/compat/run_adif_defect_resolver.py --query "taskClass=mpi_external_agent_memory_read_contract role=dispatcher lifecyclePhase=dispatch"`

Returned defectIds:

- NONE_RETURNED

Returned defects: NONE_RETURNED

## Current Runtime Freshness Verification

| Surface | Verification | Disposition |
|---|---|---|
| Memory readout route | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` was read for current request/response fields | ACCEPT: cited as read-only source authority |
| Memory readout projection | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` was read for summary-only and false-flag invariants | ACCEPT: cited as read-only source authority |
| Provider registry surfaces | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` are accounted for because forbidden-scope prose names provider/live boundaries | PASS: this work order makes no provider registry absence, hardcoded-provider, provider-selection, provider-routing, or live-governance claim |
| Registry surfaces | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` and `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` exist and are out of material scope | PASS: no registry source, aggregate, Markdown, or generator mutation is authorized |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Storage purpose | add a compact governed reference contract and closure packet for MPI-T3 |
| Existing source layout reused | root governed docs layout: `docs/baselines/`, `docs/work_orders/`, `docs/reference/`, `docs/reviews/`, and `docs/roadmaps/` |
| New durable source layout | none |
| Generated aggregate impact | none |
| Registry impact | none; registry JSON and Markdown are unchanged |
| Split/rotation need | none; changed files remain within governed file-size limits |
| Runtime storage impact | none |

## Execution Plan

1. Create `docs/reference/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_READ_CONTRACT.md`.
2. Define request mapping only for source-verified existing route fields.
3. Define response mapping only for source-verified existing projection and route response fields.
4. Mark all external-agent shapes documentation-only and `adapterContractOnly=true`.
5. Update the Memory Plane map so MPI-T3 no longer appears undefined.
6. Update the MPI roadmap status and machine closure package to show MPI-T3 closed bounded.
7. Create the completion review and close this work order as `CLOSED_PASS_BOUNDED`.
8. Run local governance gates, repair in allowed scope, then commit material closure.
9. Perform session sync in a separate follow-up commit if material closure changes next-move surfaces.

## Evidence Requirements

- command-backed changed-file manifest;
- ADIF disclosure;
- source verification table with ACCEPT rows for all runtime fields and symbols;
- completed reference contract;
- parent roadmap and Memory Plane map state updates;
- governance gates and commit-steward output.

## Review Gate

Codex reviewer/closer must confirm that the reference contract is
documentation-only, that all fields map to existing source-verified route or
projection fields, and that no runtime/source/test/registry/generated-state
path is changed before committing.

## Return Conditions

Return to orchestrator or mark blocked if any source field cannot be verified,
if a gate requires runtime/source/test/registry work outside scope, if public
export is needed, or if the contract cannot stay adapter-only.

## Operator Checkpoint

No operator checkpoint remains for MPI-T3 contract-only closure. After material
closure, the next allowed move is to select another high-value foundation
roadmap, hold, or open a fresh governed tranche; MPI-T4 remains optional
parked.

## Acceptance Criteria

| Criterion | Evidence | Status |
|---|---|---|
| Contract defines request mapping to existing route fields only | Source Verification Block plus reference Request Mapping table | PASS |
| Contract defines response mapping to existing summary-only fields only | Source Verification Block plus reference Response Mapping table | PASS |
| No runtime path is changed | `git status --short` showed only the six allowed material paths | PASS |
| Parent roadmap and Memory Plane map reflect MPI-T3 closed bounded | changed roadmap/map diff | PASS |
| ADIF disclosure is present | ADIF section in this work order and baseline | PASS |
| Public Export Disposition is present | `DEFERRED_PRIVATE_ONLY` sections | PASS |
| Closure review records command-backed verification | completion review command table | PASS |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | operator continuation authorizes a CVF-owned contract-only read boundary; source facts remain verified against CVF-governed surfaces and runtime source |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | MPI-T3 work order |
| Disposition | ADAPT as bounded CVF-owned reference-contract implementation |
| Claim boundary | no external prompt is source proof; no runtime, adapter, provider/live, public, registry, route, or generated-state mutation is authorized |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order and reference contract. No public-sync
remote, public commit, public artifact path, or public claim is authorized.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | MPI-T3 external-agent memory read contract work order |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: source verification rows, ADIF query, reference artifact, completion review, and gates |
| actionEvidence | ACTION_EVIDENCE_PRESENT: governed markdown/reference edits only |
| invocationBoundary | local source reads, governed markdown edits, local governance gates |
| interceptionBoundary | no IDE/shell/git/filesystem/provider/CLI/MCP interception claim |
| claimLanguage | contract-only external-agent memory read boundary |
| forbiddenExpansion | no route edit, runtime schema change, service-token bridge, CLI/MCP adapter, helper implementation, registry write, durable write, provider/live proof, public-sync, generated-state mutation, queue/daemon, watcher, readiness, or universal control claim |

## Agent Operation Trace Block

| Field | Disposition |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | `mpi-t3-external-agent-memory-read-contract-2026-06-27` |
| Working directory | repository root |
| Command or tool surface | PowerShell, rg, git, apply_patch, python governance gates |
| Target paths | Allowed Scope |
| Allowed scope source | this work order and GC-018 baseline |
| Before status evidence | HEAD `eeb0e532`; clean worktree at startup |
| After status evidence | material closure verified by pre-dispatch/pre-implementation gates; post-commit pre-closure required for finality |
| Diff evidence | `git diff --name-status eeb0e532..HEAD` |
| Approval boundary | contract-only MPI-T3 execution |
| Claim boundary | no runtime, route, helper, adapter, provider/live, public-sync, registry, durable-write, package, resolver, DICE, or generated-state mutation |
| Agent type | Codex dispatcher/implementer/reviewer/closer |
| Invocation ID | `mpi-t3-external-agent-memory-read-contract-2026-06-27` |
| Expected manifest | GC-018 baseline; this work order; MPI-T3 reference; MPI-T3 completion review; Memory Plane map; MPI roadmap |
| Actual changed set | GC-018 baseline; work order; reference contract; completion review; Memory Plane map; MPI roadmap |
| Manifest delta | MATCH |

## Closure Checklist

- [x] Source Verification Block completed with ACCEPT rows only.
- [x] New doc-only fields separated from runtime/source facts.
- [x] ADIF disclosure included.
- [x] Agent Handoff Contract Control Block included.
- [x] Reference contract created.
- [x] Public Export Disposition included.
- [x] Runtime/source/test paths kept out of allowed implementation scope.
- [x] Closure review created.
- [x] Session sync required after material commit.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Baseline status | `docs/baselines/CVF_GC018_MPI_T3_EXTERNAL_AGENT_MEMORY_READ_CONTRACT_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Reference contract | `docs/reference/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_READ_CONTRACT.md` | `Status: ACTIVE_REFERENCE` | PASS |
| Completion review | `docs/reviews/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_READ_CONTRACT_COMPLETION_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_READ_CONTRACT_COMPLETION_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | `Status: MPI_T3_CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | file exists and is not mutated by MPI-T3 material scope | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | file exists and is not mutated by MPI-T3 material scope | PASS |
| External evidence digest | N/A | no external benchmark/provider/live digest created | N/A with reason |
| System loop interlock | N/A | no system-loop behavior changed | N/A with reason |
| Session continuity | active session front-door/state/handoff | session-sync follows material closure commit if gates pass | N/A with reason |
| Runtime scope | forbidden source paths | no runtime/source/test route path in intended changed set | PASS |
| Public export | Public Export Disposition | `DEFERRED_PRIVATE_ONLY` | PASS |

## Claim Boundary

This work order closes MPI-T3 as documentation/reference contract work only.
It does not authorize runtime implementation, source/test changes, route or
schema edits, service-token behavior, helper code, registry writes, durable
memory writes, CLI/MCP adapter behavior, provider/live calls, public-sync,
generated-state mutation, package activation, resolver mutation, DICE, push,
or release readiness.
