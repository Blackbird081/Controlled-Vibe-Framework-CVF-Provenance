# CVF GC-018 - MPI-T4 Federated Memory Read Helper

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-22

docType: gc018_baseline

dispatchBaseHead: 355d4774

Batch ID: MPI-T4

## Purpose

Authorize one bounded implementation tranche for a deterministic, read-only
federated Memory Plane helper. The helper combines caller-supplied Learning
Plane Foundation memory candidates with caller-supplied parsed scan-registry
entries, projects registry findings through the existing MPI-T2 helper, and
passes the combined candidates through the existing summary-only Memory
runtime readout projection.

This baseline does not authorize route wiring, automatic file loading, registry
or durable writes, CLI/MCP adapter behavior, provider/live proof, or public
sync. The helper is advisory and must never block closure.

## Decision / Baseline / Proposed Tranche

Decision: dispatch MPI-T4 after MPI-T3 closure.

Baseline: current source-verified Memory Plane readout/projection helpers plus
the MPI-T3 summary-only external-agent memory contract.

Proposed tranche: create one local deterministic federated read helper, one
focused test file, and one worker-return packet. The worker must not commit.

## Operator Authorization

The operator explicitly selected MPI-T4 on 2026-06-22 after MPI-T3 closed.
The selected route is `WORKER_MUST_NOT_COMMIT`; reviewer/closer retains commit
and closure ownership.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-22: continue with MPI-T4 | ACCEPT |
| Active state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V22_2026-06-22.md` | ACCEPT |
| Phase 2 roadmap | `docs/roadmaps/CVF_MPI_PHASE2_EXTERNAL_MEMORY_READ_ROADMAP_2026-06-22.md` | ACCEPT |
| Parent MPI roadmap | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | ACCEPT |
| MPI-T3 contract | `docs/reference/memory_plane/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_SUMMARY_CONTRACT.md` | SOURCE_AUTHORITY_FOR_EXTERNAL_READ_BOUNDARY |
| MPI-T2 projection | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/scan-registry-memory-projection.ts` | SOURCE_AUTHORITY_FOR_REGISTRY_DERIVED_VIEW |
| Memory readout | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` | SOURCE_AUTHORITY_FOR_SANITIZED_READOUT |

Provider-specific memory is not CVF authority. Runtime claims in this packet
were refreshed against current source.

## Dependency Release Evidence

| Dependency | Evidence | Status |
|---|---|---|
| MPI-T3 closure | `docs/reviews/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_SUMMARY_CONTRACT_COMPLETION_2026-06-22.md`; material commit `c4c53588`; disposition `CLOSED_PASS_BOUNDED` | RELEASED |
| Operator decision | explicit MPI-T4 selection on 2026-06-22 | RELEASED |
| Source refresh | Source Verification Block below cites current runtime files and symbols | RELEASED |
| Dispatch base | clean committed HEAD `355d4774` before authoring | RELEASED |

## Scope And Owner Boundary

Allowed worker scope:

- create `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/federated-memory-read.ts`;
- create `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/federated-memory-read.test.ts`;
- create `docs/reviews/CVF_MPI_T4_FEDERATED_MEMORY_READ_HELPER_WORKER_RETURN_2026-06-22.md`.

Forbidden worker scope includes all route files, existing helpers, foundation
packages, registry sources/aggregates/generator, durable stores, session and
handoff files, public-sync, provider configuration, dependency manifests,
`.github/**`, and `governance/compat/*.py`.

Risk ceiling: R2 bounded local helper and focused unit tests; no route or
external execution behavior.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| MPI-T4 is an optional deterministic read-only federated helper | `docs/roadmaps/CVF_MPI_PHASE2_EXTERNAL_MEMORY_READ_ROADMAP_2026-06-22.md` | MPI-T4 Federated Memory Read Helper | `MPI-T4` | MPI Phase 2 roadmap | VALUE_SET | ACCEPT |
| Parent roadmap defines LPF readout plus scan-registry summary in one advisory output | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | MPI-T4 Federated Read Helper Fast-Path | `MPI-T4` | parent MPI roadmap | VALUE_SET | ACCEPT |
| MPI-T3 permits a future helper only inside its summary-only contract | `docs/reference/memory_plane/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_SUMMARY_CONTRACT.md` | Purpose; Forbidden Operations; Allowed Source Surfaces | `MPI-T4` | MPI-T3 external read contract | VALUE_SET | ACCEPT |
| Existing readout projection removes candidate content | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` | lines 9-23 and 35-57 | `buildMemoryRuntimeReadout` | Memory runtime readout projection | RUNTIME_BEHAVIOR | ACCEPT |
| Existing readout projection fixes raw-memory and reinjection flags false | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` | lines 35-54 | `rawMemoryReleased`; `canReinject` | MemoryRuntimeProjection | LITERAL_INVARIANT | ACCEPT |
| MPI-T2 helper accepts parsed registry entries and emits bounded summary candidates | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/scan-registry-memory-projection.ts` | lines 20-61 and 93-152 | `projectScanRegistryFindings` | scan registry memory projection | RUNTIME_BEHAVIOR | ACCEPT |
| Runtime workflow input accepts caller-supplied candidates and query | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts` | lines 31-47 | `MemoryRuntimeWorkflowInput` | MemoryRuntimeWorkflowInput | EXISTS | ACCEPT |
| Retrieval candidate permits content but readout sanitizer must remove it | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | lines 17-26 | `MemoryRetrievalCandidate` | MemoryRetrievalCandidate | EXISTS | ACCEPT |
| Existing focused tests exercise MPI-T2 projection through readout sanitization | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/scan-registry-memory-projection.test.ts` | projection through buildMemoryRuntimeReadout | `projectScanRegistryFindings`; `buildMemoryRuntimeReadout` | Vitest test surface | EXISTS | ACCEPT |
| MPI-T3 closure released MPI-T4 operator selection | `docs/reviews/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_SUMMARY_CONTRACT_COMPLETION_2026-06-22.md` | Final Disposition; Next Allowed Move | `CLOSED_PASS_BOUNDED` | MPI-T3 completion review | VALUE_SET | ACCEPT |

## New Implementation Symbols

| Proposed symbol | Target file | Status before worker execution | Boundary |
|---|---|---|---|
| `buildFederatedMemoryRead` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/federated-memory-read.ts` | NEW_SOURCE_SYMBOL | deterministic orchestration over existing projection/readout helpers |
| `FederatedMemoryReadInput` | same target | NEW_SOURCE_SYMBOL | caller-supplied runtime input plus parsed registry entries |
| `FederatedMemoryReadResult` | same target | NEW_SOURCE_SYMBOL | advisory readout plus source-count metadata and fixed false flags |

These symbols are proposals, not pre-existing source facts. The worker may use
clearer names only if the worker-return records the exact replacement and tests
prove the same boundary.

## Implementation Requirements

The helper must:

1. accept a `MemoryRuntimeWorkflowInput`, parsed `ScanRegistryEntry[]`, and
   optional deterministic projection options;
2. call `projectScanRegistryFindings` with the input query;
3. combine original candidates and projected candidates without mutating either
   input collection;
4. call `buildMemoryRuntimeReadout` with the combined candidates;
5. return a deterministic advisory result containing the sanitized readout,
   counts/attribution metadata, `rawMemoryReleased=false`, and
   `canReinject=false`;
6. return advisory/degraded output for absent or malformed registry input and
   never throw solely because the registry source is absent;
7. contain no filesystem, network, provider, route, registry-write, durable
   store, command-execution, or adapter behavior.

Focused tests must prove determinism, no input mutation, allowed source
selection, summary-only output, forbidden-field absence, fixed false flags,
and advisory degradation.

## Negative Search And Collision Discipline

Search roots: `docs`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src`.

Search command:
`rg -n -i "federated memory|federated.*read|buildFederatedMemoryRead" docs EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src`

Before dispatch, both target source/test files returned `False` from
`Test-Path`; existing matches were roadmap references only. There is no source
symbol collision.

## Current Runtime Freshness Verification

| Claim | Current evidence | Disposition |
|---|---|---|
| Readout sanitizer remains callable and summary-only | current `memory-runtime-readout.ts` Source Verification rows | ACCEPT |
| Registry projection remains caller-supplied and read-only | current `scan-registry-memory-projection.ts` Source Verification row | ACCEPT |
| New target files do not exist at dispatch | `Test-Path` returned `False` for both targets | ACCEPT |
| Route wiring | N/A with reason: forbidden by this baseline | N/A_WITH_REASON |
| Provider/live proof | N/A with reason: no provider behavior is changed or claimed | N/A_WITH_REASON |
| Public sync | N/A with reason: private provenance dispatch only | N/A_WITH_REASON |

## Evidence / Verification

Dispatch verification uses current source reads, Source Verification rows,
target-file absence checks, negative collision search, roadmap freshness, work
order dispatch quality, pre-dispatch autorun gate, commit steward dispatch
preflight, local hook chain, and git diff/status evidence.

## Acceptance And Fail Conditions

Accept only when all three allowed artifacts exist, focused Vitest and
TypeScript checks pass, inputs are not mutated, raw `content` is absent from
the returned readout, both safety flags remain false, no forbidden path is
changed, and the worker returns uncommitted `COMPLETE_PENDING_REVIEW`.

Fail or return `BLOCKED_WITH_REASON` for stale source symbols, ambiguous helper
output, route wiring, filesystem loading, source mutation, registry/durable
write, raw-content leakage, reinjection, provider/live/public/adapter claims,
or any required change outside Allowed scope.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance helper dispatch; no public artifact or public claim
is authorized.

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator selection to CVF-owned GC-018 baseline and work order |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this MPI-T4 GC-018 baseline |
| Disposition | ADAPT as bounded local helper implementation |
| Claim boundary | external/provider memory is not authority; current CVF source controls |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | MPI-T4 local read-only helper dispatch |
| claimDisposition | N/A with reason: no Delta execution-control behavior is implemented or claimed |
| receiptEvidence | N/A with reason: no Delta receipt |
| actionEvidence | N/A with reason: dispatch creates no runtime action evidence; worker will provide focused test evidence |
| claimLanguage | MPI-T4 local read-only helper dispatch only |
| forbiddenExpansion | route/schema/auth changes, automatic source loading, registry/durable writes, CLI/MCP adapter, provider/live, public-sync, wrapper/proxy enforcement, direct interception, arbitrary commands, EDIT/COMMIT execution, queue/daemon, watcher, readiness, full-hook equivalence, and universal control remain out of scope |
| invocationBoundary | direct library call by tests or a future separately authorized caller |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, or route interception |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author |
| Provider or surface | local workspace |
| Session or invocation | MPI-T4 packet authoring, 2026-06-22 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Target paths | this GC-018 baseline and paired work order |
| Allowed scope source | operator instruction selecting MPI-T4 |
| Before status evidence | clean HEAD `355d4774` |
| Approval boundary | dispatch only; worker returns uncommitted |
| Claim boundary | no route, write, adapter, provider/live, public-sync, or session behavior |

## Claim Boundary

This baseline authorizes only a local, deterministic, read-only helper, focused
tests, and a worker-return packet. It does not authorize route/schema/auth
changes, automatic source loading, registry or durable writes, existing helper
edits, CLI/MCP adapters, external commands, vector/graph storage, provider/live
proof, public sync, readiness, or universal control claims.
