# CVF GC-018 MPI-T3 External Agent Memory Read Contract

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: baseline

executionBaseHead: eeb0e532

## Purpose

Authorize a bounded MPI-T3 documentation/reference tranche to define the
summary-only read-direction contract for external agents that need memory
readout guidance. This tranche may create a reference contract and update
existing MPI navigation surfaces. It must not implement a CLI/MCP adapter,
route change, schema validator, service-token bridge, runtime helper, durable
write, registry write, provider/live proof, public-sync batch, or generated
state mutation.

## Scope

Allowed scope:

- `docs/reference/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_READ_CONTRACT.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_MPI_T3_EXTERNAL_AGENT_MEMORY_READ_CONTRACT_FOR_CODEX_2026-06-27.md`
- `docs/reviews/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_READ_CONTRACT_COMPLETION_2026-06-27.md`
- `docs/baselines/CVF_GC018_MPI_T3_EXTERNAL_AGENT_MEMORY_READ_CONTRACT_2026-06-27.md`
- `docs/reference/CVF_MEMORY_PLANE_MAP.md`
- `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md`

Forbidden scope:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/scan-registry-memory-projection.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/*.test.ts`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
- `docs/corpus-intelligence/registry/`
- `CVF_SESSION/agent_workspace/`
- any CLI/MCP adapter, provider/live, public-sync, package, resolver, or generated-state path

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| MPI roadmap lists MPI-T3 as External Agent Memory Read Contract | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | Work Plan row `MPI-T3` | `MPI-T3` | MPI roadmap | ACCEPT |
| MPI roadmap requires separate authorization for external-agent read contract | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | Acceptance Criteria row `External read contract` | `External read contract` | MPI roadmap | ACCEPT |
| Memory Plane map records external read contract as parked pending MPI-T3 | `docs/reference/CVF_MEMORY_PLANE_MAP.md` | Running vs Contract-Only vs Parked row `External read contract` | `External read contract` | Memory Plane map | ACCEPT |
| Memory readout route request body has required runtime fields | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | interface declaration | `MemoryRuntimeReadoutBody` | Memory readout route | ACCEPT |
| Memory readout route accepts service-token or session auth | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | `POST` auth branch | `verifyServiceTokenRequest`; `verifySessionCookie` | Memory readout route | ACCEPT |
| Memory readout route response fixes raw release and reinjection flags false | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | response object | `rawMemoryReleased`; `canReinject` | Memory readout route | ACCEPT |
| Memory readout projection strips candidate content | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` | `sanitizeCandidates` | `content` | memory runtime readout projection | ACCEPT |
| Memory readout projection fixes raw release and reinjection flags false | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` | `buildMemoryRuntimeReadout` projection object | `rawMemoryReleased`; `canReinject` | memory runtime readout projection | ACCEPT |
| LSC-T6 defines external-agent CLI/MCP contract-only boundary | `docs/reference/learning_signal_chain/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT.md` | Scope and Claim Boundary | `adapterContractOnly` | LSC-T6 reference contract | ACCEPT |
| MPI-T2 closed a read-only projection and left external-agent read behavior parked | `docs/reviews/CVF_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION_COMPLETION_2026-06-22.md` | Risk / Corrective Action row | `MPI-T3` | MPI-T2 completion review | ACCEPT |

## Evidence / Verification

Evidence required for closure:

- source verification rows above;
- ADIF disclosure below;
- created MPI-T3 reference contract;
- updated Memory Plane map and MPI roadmap state;
- command-backed changed-file manifest;
- pre-dispatch, pre-closure, closure-quality, file-size, and commit-steward gate output.

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
| Provider registry surfaces | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` are accounted for because forbidden-scope prose names provider/live boundaries | PASS: this baseline makes no provider registry absence, hardcoded-provider, provider-selection, provider-routing, or live-governance claim |
| Registry surfaces | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` and `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` exist and are out of material scope | PASS: no registry source, aggregate, Markdown, or generator mutation is authorized |

## Decision

MPI-T3 is authorized as a contract-only tranche.

The contract may define:

- external-agent read request vocabulary mapped to the existing memory readout route body;
- external-agent read response vocabulary mapped to the existing summary-only projection;
- fixed invariants `rawMemoryReleased=false`, `canReinject=false`, and no raw candidate `content`;
- no-signal / no-readable-memory assertion vocabulary;
- safe external-agent consumption boundary.

The contract may not define:

- a new runtime endpoint;
- a new body field not mapped to an existing source-verified field;
- service-token generation or distribution;
- a CLI/MCP tool, adapter, shell bridge, queue, daemon, watcher, or IDE bridge;
- automatic scan-registry route wiring;
- durable memory write behavior;
- public export or release-readiness behavior.

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | operator continuation authorizes a CVF-owned contract-only read boundary; source facts remain verified against CVF-governed surfaces and runtime source |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | MPI-T3 GC-018 baseline |
| Disposition | ADAPT as bounded CVF-owned reference-contract authorization |
| Claim boundary | no external prompt is source proof; no runtime, adapter, provider/live, public, registry, route, or generated-state mutation is authorized |

## Acceptance Criteria

| Criterion | Required evidence | Status |
|---|---|---|
| Source verification covers every runtime field and contract token | Source Verification Block in this baseline and work order | PASS |
| Reference contract exists and states summary-only read invariants | `docs/reference/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_READ_CONTRACT.md` | PASS |
| Existing MPI navigation surfaces no longer say MPI-T3 is undefined | changed `docs/reference/CVF_MEMORY_PLANE_MAP.md`; changed `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | PASS |
| No runtime/source/test/registry/generated-state implementation path changed | `git status --short` showed only the six allowed material paths | PASS |
| Governance gates pass or any failure is recorded with blocker disposition | pre-dispatch PASS; dispatch-quality PASS; pre-implementation PASS; file-size PASS; implementation steward PASS; post-commit pre-closure required for finality | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance contract baseline. No public-sync remote, public
commit, public artifact path, or public claim is authorized.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | MPI-T3 external-agent memory read contract authorization |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: source verification rows, ADIF query, contract artifact, completion review, and gate output |
| actionEvidence | ACTION_EVIDENCE_PRESENT: bounded governed markdown/reference edits only |
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
| Target paths | allowed scope in this baseline |
| Allowed scope source | active session next allowed move plus MPI roadmap next action |
| Before status evidence | HEAD `eeb0e532`; clean worktree at startup |
| After status evidence | material closure verified by pre-dispatch/pre-implementation gates; post-commit pre-closure required for finality |
| Diff evidence | `git diff --name-status eeb0e532..HEAD` |
| Approval boundary | contract-only MPI-T3 execution |
| Claim boundary | no runtime, route, helper, adapter, provider/live, public-sync, registry, durable-write, package, resolver, DICE, or generated-state mutation |
| Agent type | Codex dispatcher/implementer/reviewer/closer |
| Invocation ID | `mpi-t3-external-agent-memory-read-contract-2026-06-27` |
| Expected manifest | this baseline; MPI-T3 work order; MPI-T3 reference; MPI-T3 completion review; Memory Plane map; MPI roadmap |
| Actual changed set | GC-018 baseline; work order; reference contract; completion review; Memory Plane map; MPI roadmap |
| Manifest delta | MATCH |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_MPI_T3_EXTERNAL_AGENT_MEMORY_READ_CONTRACT_FOR_CODEX_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
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

This baseline authorizes MPI-T3 contract-only documentation. It does not
authorize runtime implementation, source/test changes, route or schema edits,
service-token behavior, helper code, registry writes, durable memory writes,
CLI/MCP adapter behavior, provider/live calls, public-sync, generated-state
mutation, package activation, resolver mutation, DICE, push, or release
readiness.
