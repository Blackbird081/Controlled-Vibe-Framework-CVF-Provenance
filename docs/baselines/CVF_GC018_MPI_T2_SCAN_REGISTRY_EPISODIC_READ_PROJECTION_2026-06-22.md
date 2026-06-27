# CVF GC-018 - MPI-T2 Scan Registry Episodic Read Projection

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-22

docType: gc018_baseline

dispatchBaseHead: 867b4c05

Batch ID: MPI-T2

## Purpose

Authorize a bounded MPI-T2 worker tranche that projects GC-051 Corpus Scan
Registry findings into summary-only Memory readout candidate shape.

The tranche is runtime-adjacent but intentionally narrow. It creates a pure,
deterministic projection helper and focused tests, updates the Memory Plane map
with the projection contract, and returns uncommitted worker evidence. It does
not edit the Memory readout route, does not write the scan registry, does not
run a registry generator, does not add a durable store, and does not implement
an external CLI/MCP adapter.

## Operator Authorization

The operator selected MPI-T2 from the INDEX-T1 closed checkpoint. Current
session continuity records the allowed next move as selecting MPI-T2 Scan
Registry Episodic Read Projection, MPI-T3 External Agent Memory Read Contract,
or hold.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-22: write work order for MPI-T2 | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` current mode `index_t1_forward_only_index_checker_closed_operator_checkpoint` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` next allowed move permits MPI-T2 selection | ACCEPT |
| MPI roadmap | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` row `MPI-T2` | ACCEPT |
| Memory Plane map | `docs/reference/CVF_MEMORY_PLANE_MAP.md` marks scan-registry read projection as parked MPI-T2 and records readout invariants | ACCEPT |
| GC-051 standard | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` | SOURCE_AUTHORITY_FOR_REGISTRY_FINDINGS |
| Memory readout route | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | SOURCE_AUTHORITY_FOR_EXISTING_ROUTE_SHAPE |
| Memory runtime projection | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` | SOURCE_AUTHORITY_FOR_SUMMARY_ONLY_PROJECTION |

Provider-specific memory, chat memory, and private agent-local files are not CVF
source authority. Runtime claims must cite current source.

## Decision / Baseline / Proposed Tranche

Baseline decision: MPI-T2 is released for worker execution after MPI-T1
Memory Plane Front-Door Map closure and INDEX-T1 checker closure.

Proposed tranche: `MPI-T2 Scan Registry Episodic Read Projection`.

Dependency release evidence:

- MPI-T1 closure: `docs/reviews/CVF_MPI_T1_MEMORY_PLANE_FRONT_DOOR_MAP_COMPLETION_2026-06-21.md`, material commit `24f3b958`.
- INDEX-T1 closure: `docs/reviews/CVF_INDEX_T1_FORWARD_ONLY_INDEX_CLASSIFICATION_CHECKER_COMPLETION_2026-06-21.md`, material commit `993a8460`.
- Session continuity: active next-move surfaces permit MPI-T2 selection after session-sync commit `867b4c05`.

## Scope / Owner Boundary

Allowed worker scope:

- create `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/scan-registry-memory-projection.ts`;
- create `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/scan-registry-memory-projection.test.ts`;
- create `docs/reference/CVF_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION.md`;
- update `docs/reference/CVF_MEMORY_PLANE_MAP.md` narrowly to record MPI-T2
  projection status and boundary;
- create `docs/reviews/CVF_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION_WORKER_RETURN_2026-06-22.md`.

Forbidden worker scope:

- no edits to `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts`;
- no edits to Memory write route, durable store, registry source entries,
  generated registry aggregate, registry Markdown, registry generator, active
  session state, active handoff, root startup routers, public-sync,
  `.github/**`, dependency manifests, MCP packages, or provider configuration;
- no registry write, durable write, generator run as an implementation step,
  route schema change, service-token change, adapter behavior, CLI/MCP tool,
  vector DB, embedding store, graph persistence, queue, daemon, watcher,
  wrapper/proxy enforcement, direct IDE/shell/git/filesystem interception,
  arbitrary command execution, EDIT/COMMIT execution, provider/live proof,
  public-sync, readiness claim, or universal governed-coding-control claim.

Risk ceiling: R1/R2 bounded read projection helper plus focused tests.

## Required Deliverables

The worker must return uncommitted `COMPLETE_PENDING_REVIEW` with only these
worker-owned artifacts changed:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/scan-registry-memory-projection.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/scan-registry-memory-projection.test.ts`
- `docs/reference/CVF_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION.md`
- `docs/reference/CVF_MEMORY_PLANE_MAP.md`
- `docs/reviews/CVF_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION_WORKER_RETURN_2026-06-22.md`

No commit is permitted by the worker.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| MPI-T2 is the scan-registry episodic read projection tranche | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | lines 273, 360-377 | `MPI-T2`; `Scan Registry Episodic Read Projection` | MPI roadmap | VALUE_SET | ACCEPT |
| MPI-T2 must preserve summary-only invariants | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | lines 369-370, 422 | `rawMemoryReleased`; `canReinject` | MPI roadmap | VALUE_SET | ACCEPT |
| Memory Plane map marks scan-registry read projection as parked before this tranche | `docs/reference/CVF_MEMORY_PLANE_MAP.md` | lines 70, 108, 149, 159 | `Scan-registry read projection`; `MPI-T2` | Memory Plane map | VALUE_SET | ACCEPT |
| Existing readout route authenticates before readout | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | lines 135-163 | `verifyServiceTokenRequest`; `verifySessionCookie`; 401 branch | Memory readout route | EXISTS | ACCEPT |
| Existing readout route accepts candidates with id, scope, summary, createdAt, auditTrust, lifecycleState, and optional content | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | lines 19-28, 82-103 | `MemoryRuntimeReadoutBody.candidates` | Memory readout route body | EXISTS | ACCEPT |
| Existing readout route calls buildMemoryRuntimeReadout with candidates and returns fixed false flags | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | lines 177-204 | `buildMemoryRuntimeReadout`; `rawMemoryReleased`; `canReinject` | Memory readout route | EXISTS | ACCEPT |
| Runtime readout projection strips candidate content | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` | lines 15-22, 35-54 | `sanitizeCandidates`; `sanitizeWorkflowResult` | Memory runtime readout projection | LITERAL_INVARIANT | ACCEPT |
| Runtime readout tests assert sentinel removal and fixed false flags | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.test.ts` | lines 29-46, 48-60 | `buildMemoryRuntimeReadout` tests | Vitest test surface | EXISTS | ACCEPT |
| Route tests assert 401, invalid fields, sanitized projection, and fixed false flags | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.test.ts` | lines 52-84, 86-101 | `/api/memory/readout` tests | Vitest route test surface | EXISTS | ACCEPT |
| Registry aggregate is generated from per-entry sources and is not hand-edited | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` | lines 51-75 | Registry Location; generator command; drift checker | GC-051 standard | VALUE_SET | ACCEPT |
| Registry entries define semanticRegions and findings[] | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` | lines 79-105 | `semanticRegions`; `findings`; `negativeSearchTerms` | GC-051 standard | VALUE_SET | ACCEPT |
| Finding records require id, summary, disposition, nextAction, defectClass, learningLane | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` | lines 107-122 | `findings[]` fields | GC-051 standard | VALUE_SET | ACCEPT |
| Finding Discovery Rule requires domain keyword matching against semanticRegions or findings summaries | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` | lines 304-315 | Finding Discovery Rule | GC-051 standard | VALUE_SET | ACCEPT |
| cvf-web focused tests are run through Vitest | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | scripts section | `test run script`; `check script` | cvf-web package scripts | EXISTS | ACCEPT |

## New Doc-Only Terms

| Proposed term | Owner in MPI-T2 | Runtime status | Reason |
|---|---|---|---|
| `scanRegistryMemoryCandidate` | MPI-T2 helper/reference | DOC_ONLY_NEW until implemented by worker | candidate shape derived from GC-051 findings for Memory readout consumption |
| `registryProjectionSource` | MPI-T2 helper/reference | DOC_ONLY_NEW until implemented by worker | records the source entry and finding ids behind a projected summary |
| `projectionBoundary` | MPI-T2 helper/reference | DOC_ONLY_NEW | records summary-only, no-write, no-reinjection boundary |

These terms are not existing route fields, registry fields, CLI/MCP fields, or
public API identifiers unless the worker creates them inside the allowed helper
or reference contract.

## Projection Contract

The worker must implement a pure helper that:

- accepts parsed GC-051 registry data or registry entry objects as input;
- extracts domain keywords from a query using deterministic local string
  matching;
- matches query keywords against `semanticRegions` and `findings[].summary`
  using the GC-051 Finding Discovery Rule;
- maps matched findings to Memory retrieval candidate-compatible records with
  `id`, `scope`, `summary`, `createdAt`, `auditTrust`, `lifecycleState`, and no
  raw registry packet content;
- sets lifecycle state to an episodic/semantic value justified by tests;
- includes enough attribution in the summary or metadata for a reviewer to find
  the source registry entry and finding id;
- never mutates registry input;
- never writes to `docs/corpus-intelligence/**`;
- never flips `rawMemoryReleased` or `canReinject`;
- never bypasses `buildMemoryRuntimeReadout` sanitization.

The helper should not import the generated registry aggregate directly unless
the worker can prove the import is server-safe and TypeScript-safe. A pure
function over parsed data is preferred.

## Current Runtime Freshness Verification

| Claim | Freshness evidence | Disposition |
|---|---|---|
| Existing readout route can consume candidates if supplied by caller | route body candidate schema and tests in Source Verification Block | ACCEPT |
| Existing route auth remains unchanged | route auth lines in Source Verification Block | ACCEPT |
| Existing projection strips raw candidate content | readout projection and tests in Source Verification Block | ACCEPT |
| GC-051 aggregate is generated and should not be hand-edited | GC-051 standard lines 51-75 | ACCEPT |
| MPI-T2 projection helper is not present before dispatch | `Test-Path` output `False` | ACCEPT |
| Provider registry surface is not changed or claimed by MPI-T2 | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` exports `ProviderRegistry`; `PROVIDER_CAPABILITY_REGISTRY` is not claimed or modified by MPI-T2 | N/A_WITH_REASON |
| Provider/live proof is not authorized | this baseline Forbidden worker scope | N/A_WITH_REASON |
| Public-sync is not authorized | Public Export Disposition below | N/A_WITH_REASON |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | roadmap/operator selection to CVF-owned dispatch packet |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | MPI-T2 GC-018 baseline |
| Disposition | ADAPT as bounded CVF-owned read projection helper work |
| Claim boundary | no external input is promoted as source authority; GC-051, current route source, and Memory Plane map control |

## Rescan Intelligence Hardening

- Original source artifact: `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md`.
- Predecessor intake artifact: `docs/reference/CVF_MEMORY_PLANE_MAP.md`.
- Delta ledger status: `CHANGED_DISPOSITION` because MPI-T2 moves from parked
  roadmap item to dispatched worker packet.
- Routing matrix status: `DO_NOW` for helper/test/reference only;
  `SEPARATE_RUNTIME_TRANCHE` for route schema changes, external read contract,
  federated helper, registry write, durable write, provider/live, and public
  sync.
- Semantic sampling status: sampled readout route auth/candidate shape,
  runtime projection sanitization, GC-051 registry/finding rules, route tests,
  and Memory Plane map parked status.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Evidence |
|---|---|
| UNCHANGED_FROM_INTAKE | `rawMemoryReleased=false`, `canReinject=false`, and RAW sentinel remain inherited from existing readout surface. |
| CHANGED_DISPOSITION | MPI-T2 projection moved from PARKED to CLOSED_PASS_BOUNDED helper/reference closure. |
| NEW_FINDING | The existing route already accepts sanitized candidate inputs, so a pure helper can project registry findings without route schema edits. |
| REMOVED_OR_REJECTED | Direct route edit, registry write, generator mutation, provider/live proof, public-sync, and adapter behavior remain rejected. |

### Follow-Up Routing Matrix

| Routing lane | Disposition |
|---|---|
| DO_NOW | projection helper, focused tests, MPI-T2 reference contract, Memory Plane map status update, worker return |
| SEPARATE_RUNTIME_TRANCHE | route schema change, actual external-agent read contract, federated helper, durable write, registry mutation |
| STRATEGIC_OPERATOR_DECISION | MPI-T3 or hold once MPI-T2 worker return is reviewed and closed |
| OUT_OF_SCOPE | provider/live, public-sync, vector DB, graph persistence, CLI/MCP adapter behavior, universal-control claims |
| RESOLVED_BY_DESIGN | use existing candidate shape and existing readout sanitization instead of adding a parallel readout route |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| MPI-T2-S1 | readout route auth | route requires session or service token | keep route unchanged | prevents unauthenticated projection path | PASS |
| MPI-T2-S2 | candidate schema | route accepts candidate summaries and optional content | helper emits compatible summaries | prevents parallel schema drift | PASS |
| MPI-T2-S3 | readout projection | content is stripped and false flags are fixed | focused tests must prove sentinel removal | prevents raw leakage |
| MPI-T2-S4 | GC-051 standard | findings and semanticRegions are canonical matching inputs | helper uses those fields | prevents parallel finding model |
| MPI-T2-S5 | Memory Plane map | MPI-T2 was parked until separate GC-018 | this baseline releases only helper/test/reference | prevents silent broad runtime expansion |

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| Foundation area | Memory Plane scan-registry episodic read projection |
| New source file | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/scan-registry-memory-projection.ts` |
| New test file | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/scan-registry-memory-projection.test.ts` |
| Reference output | `docs/reference/CVF_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION.md` |
| Map update | `docs/reference/CVF_MEMORY_PLANE_MAP.md` |
| Generated aggregate impact | N/A with reason: no generated registry aggregate edit is authorized |
| Registry source impact | N/A with reason: no registry entry edit is authorized |
| Route impact | N/A with reason: existing readout route remains unchanged in MPI-T2 |

## Worker Return Packet Shape Contract

The worker-return artifact must include:

| Required item | Required value |
|---|---|
| Status | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| executionBaseHead | actual `git rev-parse --short HEAD` captured at worker start |
| git status | actual `git status --short` after worker edits |
| Source Inventory | all files read and created |
| Scan Depth Ledger | source-read depth and any unreadable/deferred files |
| Gate Evidence | required command results |
| Changed Files | exact pending changed paths |
| Purpose | worker-return purpose section |
| Scope / Methodology | worker-return scope and methodology section |
| Findings / Position | worker-return findings and final position section |
| Risk / Corrective Action | worker-return risk and corrective action section |
| Claim Boundary | no route edit, no registry write, no raw release, no reinjection, no public/provider/adapter scope |
| Agent Operation Trace Block | worker role trace |
| Delta Execution Claim Boundary Control Block | N/A rows for execution-control claims |
| Public Export Disposition | `DEFERRED_PRIVATE_ONLY` |
| WORKER_EXPERIENCE_RETRO | structured block or exact N/A token |

Conditional sections must be present or marked `N/A with reason`:

- External Knowledge Intake Routing
- Rescan Intelligence Hardening
- Corpus Completeness And Report Integrity
- Finding-To-Governance Learning Disposition
- Epistemic Process Block
- Machine Closure Package

## Evidence / Verification

Dispatch author verification before this packet:

- `git rev-parse --short HEAD` returned `867b4c05`.
- `git status --short` was clean before dispatch authoring.
- Source verification used direct file reads against current repository files.

Required pre-dispatch verification before dispatch commit:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 867b4c05 --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base 867b4c05 --head HEAD --enforce
python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base 867b4c05 --head HEAD --enforce
```

Required worker checks:

```powershell
git rev-parse --short HEAD
git status --short
Push-Location EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npm run test:run -- src/lib/scan-registry-memory-projection.test.ts src/lib/memory-runtime-readout.test.ts src/app/api/memory/readout/route.test.ts
npm run check
Pop-Location
python governance/compat/run_worker_return_fast_gate.py
```

## Review Gate

Reviewer/closer must reject, repair inside reviewer-owned closure scope, or
return the worker output if:

- any path outside the Required Deliverables is changed by the worker;
- the helper reads or writes filesystem paths directly without a documented
  server-safe reason;
- the helper mutates registry input or writes generated registry artifacts;
- the helper emits raw packet content instead of bounded summaries and
  attribution;
- tests do not cover keyword matching, no-match behavior, no mutation,
  duplicate/source attribution, sentinel/raw-content stripping through
  `buildMemoryRuntimeReadout`, and fixed false flags;
- TypeScript check fails;
- worker-return packet sections or gate evidence are missing;
- any route/schema/auth/provider/live/public/adapter claim appears.

## Corpus Completeness And Report Integrity

- Corpus task class: NOT_APPLICABLE_WITH_REASON - MPI-T2 dispatch is a bounded
  projection-helper work order, not a new corpus enumeration or scan.
- Corpus root: NOT_APPLICABLE_WITH_REASON - no corpus root is assigned.
- Snapshot time: NOT_APPLICABLE_WITH_REASON - no corpus snapshot is taken.
- Enumeration command: filesystem-backed direct file reads listed in Source
  Verification Block; no corpus enumeration command is authorized.
- Manifest artifact or inline manifest: inline Source Verification Block above.
- Manifest hash: NOT_APPLICABLE_WITH_REASON - no corpus manifest hash is created.
- Processing ledger artifact or inline ledger: inline Source Verification Block
  and semantic sampling tables above.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED,
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=inline Source Verification Block; ledger_terminal=READ for named source rows; exclusions=new corpus scan, registry mutation, route schema change, provider/live, public-sync, CLI/MCP adapter; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: new corpus scan, registry mutation, generated aggregate
  edit, route schema change, provider/live proof, public-sync copy, and CLI/MCP
  adapter.
- Unreadable or unsupported files: 0.
- Aggregation check: NOT_APPLICABLE_WITH_REASON - no corpus aggregate is created
  or changed.
- Drift check: NOT_APPLICABLE_WITH_REASON - no corpus aggregate is changed.
- Output traceability: Required Deliverables and Source Verification Block define
  all worker output traceability.
- Adversarial verification: reviewer/closer must run reviewer-fast or stricter
  applicable gate before acceptance.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch for a bounded Memory Plane projection
helper. No public-sync remote, public commit, public artifact path, public
README/catalog claim, or public repository mutation is authorized.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | MPI-T2 projection helper dispatch only |
| claimDisposition | N/A with reason: no Delta execution-control behavior is implemented or claimed |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed by this dispatch |
| invocationBoundary | worker implements deterministic local helper/test only after dispatch |
| interceptionBoundary | no direct IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | bounded read projection helper, tests, and reference contract only |
| forbiddenExpansion | route edit, registry write, durable write, provider/live, public-sync, CLI/MCP adapter behavior, queue/daemon, watcher, readiness, full-hook equivalence, cost optimization, and universal control remain out of scope |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author |
| Provider or surface | local workspace |
| Session or invocation | MPI-T2 dispatch authoring, 2026-06-22 |
| Working directory | repository root |
| Command or tool surface | startup reads, source verification reads, apply_patch edits, dispatch gates |
| Target paths | this GC-018 baseline; `docs/work_orders/CVF_WO_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION_2026-06-22.md`; roadmap/session sync surfaces after dispatch |
| Allowed scope source | operator selection of MPI-T2 from INDEX-T1 closed checkpoint |
| Before status evidence | HEAD `867b4c05`; worktree clean before dispatcher edits |
| After status evidence | dispatch packet created for worker |
| Diff evidence | pre-dispatch gates required before commit |
| Approval boundary | dispatch only; no worker execution, provider/live, public-sync, route edit, registry write, or adapter behavior |
| Claim boundary | worker dispatch packet only |
| Agent type | dispatcher |
| Invocation ID | `mpi-t2-scan-registry-episodic-read-projection-dispatch-2026-06-22` |
| Expected manifest | this GC-018 baseline; paired MPI-T2 work order; roadmap dispatch row |
| Actual changed set | checked by dispatch gates before commit |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in dispatch packet |

## Claim Boundary

This baseline authorizes only a bounded scan-registry episodic read projection
helper, focused tests, and reference/map updates. It does not authorize Memory
route edits, registry source or aggregate edits, durable writes, registry
generator changes, provider/live proof, public-sync, actual CLI/MCP adapter
behavior, vector DB, embedding index, graph persistence, direct interception,
queue, daemon, watcher, readiness, cost optimization, or universal
governed-coding control.
