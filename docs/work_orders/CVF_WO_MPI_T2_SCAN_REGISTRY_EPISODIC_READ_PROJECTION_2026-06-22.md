# CVF Agent Work Order - MPI-T2 Scan Registry Episodic Read Projection

Memory class: FULL_RECORD

Status: DISPATCHED_TO_WORKER

Date: 2026-06-22

docType: work_order

dispatchBaseHead: 867b4c05

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Worker. Reviewer/closer is a separate role after worker return.

Canonical packet:
`docs/work_orders/CVF_WO_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION_2026-06-22.md`

Current status: `DISPATCHED_TO_WORKER`. Dependencies released by MPI-T1 closure
artifact `docs/reviews/CVF_MPI_T1_MEMORY_PLANE_FRONT_DOOR_MAP_COMPLETION_2026-06-21.md`
at material commit `24f3b958` and INDEX-T1 closure artifact
`docs/reviews/CVF_INDEX_T1_FORWARD_ONLY_INDEX_CLASSIFICATION_CHECKER_COMPLETION_2026-06-21.md`
at material commit `993a8460`. This work order releases MPI-T2 only.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: worker must capture with `git rev-parse --short HEAD` at
worker start.

Current-time notes: MPI-T2 is a bounded read projection helper tranche. It
projects GC-051 scan-registry findings into Memory readout candidate-compatible
summary records. It does not change the existing Memory readout route.

Do-not-misread notes: do not edit the Memory readout route, Memory write route,
registry entries, generated registry aggregate, registry Markdown, registry
generator, durable store, session state, active handoff, public-sync, MCP
packages, dependency manifests, provider configuration, or `.github/**`. Do
not implement MPI-T3, MPI-T4, vector DB, graph persistence, external adapter
behavior, provider/live proof, public-sync, arbitrary command execution,
EDIT/COMMIT execution, queue, daemon, watcher, readiness, or universal
governed-coding-control claims.

Required first actions: read this work order, read the paired MPI-T2 GC-018
baseline, read the MPI roadmap, read `docs/reference/CVF_MEMORY_PLANE_MAP.md`,
read the GC-051 standard, read the Memory readout route, read
`memory-runtime-readout.ts` and current tests, capture `executionBaseHead`, and
inspect `git status --short`.

Return contract: return `COMPLETE_PENDING_REVIEW` with only allowed
uncommitted artifacts, actual `executionBaseHead`, actual `git status --short`,
focused Vitest/TypeScript/worker-return gate evidence, and no commit. If
blocked, return `BLOCKED_WITH_REASON` and name the exact dependency, source, or
gate.

The worker-return artifact must include either the structured
`WORKER_EXPERIENCE_RETRO` block or the exact asserting
`WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` line.

## Purpose

Implement a deterministic, read-only projection helper that turns GC-051
Corpus Scan Registry findings into summary-only Memory readout candidates.

MPI-T2 exists to make prior scan findings faster to retrieve without making the
scan registry a write authority and without changing the existing authenticated
Memory readout route.

## Agent Roles

| Role | Owner | Commitment boundary |
|---|---|---|
| Dispatcher | Codex/orchestrator | creates GC-018 baseline and this worker packet |
| Worker | assigned worker | edits only Allowed scope and returns uncommitted |
| Reviewer/closer | Codex/orchestrator after worker return | validates source/test behavior, repairs allowed-scope packet defects, commits accepted material, and performs session sync if needed |
| Operator | human operator | checkpoint for scope expansion, route/schema/provider/live/public/adapter/generated/session/durable work, secrets, or destructive action |

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-22: write work order for MPI-T2 | ACCEPT |
| MPI-T2 GC-018 baseline | `docs/baselines/CVF_GC018_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION_2026-06-22.md` | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | ACCEPT |
| MPI roadmap | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | ACCEPT |
| MPI-T1 Memory Plane map | `docs/reference/CVF_MEMORY_PLANE_MAP.md` | ACCEPT |
| GC-051 standard | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` | SOURCE_AUTHORITY_FOR_REGISTRY_FINDINGS |
| Memory readout route | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | SOURCE_AUTHORITY_FOR_EXISTING_ROUTE_SHAPE |
| Memory runtime readout projection | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` | SOURCE_AUTHORITY_FOR_SUMMARY_ONLY_SANITIZATION |
| Current readout tests | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.test.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.test.ts` | ACCEPT |

## Dependency Release Gate

| Dependency | Release evidence | Current status |
|---|---|---|
| MPI-T1 Memory Plane map | `docs/reviews/CVF_MPI_T1_MEMORY_PLANE_FRONT_DOOR_MAP_COMPLETION_2026-06-21.md`; `docs/reference/CVF_MEMORY_PLANE_MAP.md` | RELEASED |
| INDEX-T1 checker closure | `docs/reviews/CVF_INDEX_T1_FORWARD_ONLY_INDEX_CLASSIFICATION_CHECKER_COMPLETION_2026-06-21.md`; material commit `993a8460` | RELEASED |
| Operator selection | active next-move surfaces permit MPI-T2 selection; operator requested MPI-T2 work order on 2026-06-22 | RELEASED |
| Source verification refresh | this work order and paired GC-018 cite current route/projection/GC-051 source sections | RELEASED |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | dispatcher releases packet; worker implements helper/tests/reference; reviewer/closer validates and commits if accepted |
| phase | DISPATCH_COMPLETE; EXECUTION; CLOSURE; SESSION_SYNC_IF_NEEDED |
| baseHeadFor(phase) | `dispatchBaseHead=867b4c05`; `executionBaseHead` captured by worker at start; `closureBaseHead` set by reviewer before closure commit |
| changedSetScope(phase) | worker changes only Allowed scope; reviewer/closer owns status/closure/session-sync |
| traceScope(phase, actor) | worker-return trace covers MPI-T2 artifacts; reviewer trace covers review/closure |
| commitOwner(phase) | worker commits nothing; reviewer/closer owns accepted material/closure/session-sync commit |
| crossBatchIsolation | do not mix MPI-T2 with MPI-T3/T4, route schema changes, registry writes, durable writes, provider/live, public-sync, adapter behavior, session-sync, or unrelated runtime work |
| Before status evidence | committed base `867b4c05`; INDEX-T1 closure continuity recorded operator checkpoint |
| nextMoveSurfaces | reviewer updates only during MPI-T2 closure if current mode or next allowed move changes |
| Closer designation | reviewer/closer role is the designated closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION_COMPLETION_2026-06-22.md` |
| reviewerOwnedClosurePaths | this work order; GC-018 baseline; MPI roadmap status row; worker-return artifact; reviewer-owned completion review; optional session-sync surfaces if accepted |
| workerReturnStatus | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| closer | reviewer/closer role |

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Selected route | `MULTI_AGENT_SINGLE_ROLE` |
| Intake summary | operator selected MPI-T2 from INDEX-T1 closed checkpoint artifact `docs/reviews/CVF_INDEX_T1_FORWARD_ONLY_INDEX_CLASSIFICATION_CHECKER_COMPLETION_2026-06-21.md` at material commit `993a8460` |
| Scope classification | bounded R1/R2 runtime-adjacent helper/test/reference tranche |
| Risk sensitivity | summary-only projection helper; no route edit, no registry write, no provider/live, no public-sync |
| Intake owner | dispatcher |
| Execution owner | worker |
| Review owner | reviewer/closer |
| Commit mode | `WORKER_MUST_NOT_COMMIT` |
| Escalation condition | `BLOCKED_WITH_REASON` if required action exceeds allowed scope or requires route/schema/provider/live/public/generated/session/durable/adapter work |
| Rationale | release only the smallest projection step before MPI-T3 external read contract or MPI-T4 helper |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | roadmap/operator selection to CVF-owned work order |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | MPI-T2 work order |
| Disposition | ADAPT as bounded CVF-owned read projection helper packet |
| Claim boundary | no external input is source authority; GC-051 and current runtime source control |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: MPI-T2 does not rescan or absorb legacy source
families. MPI-T0/MPI-T1 already handled INDEX and Memory Plane map prerequisites.
MPI-T2 consumes GC-051 governed registry data and current Memory readout source
only.

## Required First Reads

| Source | Reason |
|---|---|
| `docs/reference/guard_orientation/README.md` | task-first guard map and worker-return packet requirements |
| `docs/baselines/CVF_GC018_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION_2026-06-22.md` | GC-018 authorization and claim boundary |
| this work order | current worker packet and allowed scope |
| `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | MPI-T2 roadmap requirements |
| `docs/reference/CVF_MEMORY_PLANE_MAP.md` | current Memory Plane map and parked MPI-T2 gap |
| `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` | GC-051 registry/finding fields and Finding Discovery Rule |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | generated registry aggregate shape and sample entries |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | existing auth, candidate schema, route response flags |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` | existing summary-only sanitization |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.test.ts` | existing projection test pattern |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.test.ts` | existing route test pattern |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | exact focused test and TypeScript commands |

## Allowed Scope

The worker may change only:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/scan-registry-memory-projection.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/scan-registry-memory-projection.test.ts`
- `docs/reference/CVF_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION.md`
- `docs/reference/CVF_MEMORY_PLANE_MAP.md`
- `docs/reviews/CVF_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION_WORKER_RETURN_2026-06-22.md`

## Write Ownership

| Path | Owner during worker execution | Disposition |
|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/scan-registry-memory-projection.ts` | worker | create |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/scan-registry-memory-projection.test.ts` | worker | create |
| `docs/reference/CVF_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION.md` | worker | create |
| `docs/reference/CVF_MEMORY_PLANE_MAP.md` | worker | update narrowly |
| `docs/reviews/CVF_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION_WORKER_RETURN_2026-06-22.md` | worker | create |
| `docs/baselines/CVF_GC018_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION_2026-06-22.md` | reviewer/closer | no worker edit |
| this work order | reviewer/closer | no worker edit |
| `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | reviewer/closer | no worker edit |
| route files, registry aggregate/sources, durable store, generated state, active handoff, public-sync, MCP packages, dependency manifests, `.github/**` | out of worker scope | forbidden |

## Forbidden Scope

The worker must not:

- edit `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts`;
- edit Memory write route, durable store, scan registry source entries,
  generated registry aggregate, registry Markdown, registry generator, session
  state, active handoff, root startup routers, public-sync, MCP packages,
  dependency manifests, provider configuration, `.github/**`, or public
  repository files;
- implement vector DB, embedding store, graph persistence, CLI/MCP adapter
  behavior, provider/live proof, wrapper/proxy enforcement, direct IDE/shell/git
  interception, arbitrary command execution, EDIT/COMMIT execution, queue,
  daemon, watcher, readiness, full-hook equivalence, cost optimization, or
  universal governed-coding control;
- mutate runtime Learning Plane state, create durable writes, write registry
  entries, run registry generator as part of implementation, change route auth,
  change route schema, or claim production/public readiness.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| MPI-T2 is planned as Scan Registry Episodic Read Projection | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | lines 273, 360-377 | `MPI-T2` | MPI roadmap | VALUE_SET | ACCEPT |
| MPI-T2 must preserve summary-only readout invariants | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | lines 369-370, 422 | `rawMemoryReleased`; `canReinject` | MPI roadmap | VALUE_SET | ACCEPT |
| Memory Plane map identifies scan-registry projection as parked MPI-T2 gap | `docs/reference/CVF_MEMORY_PLANE_MAP.md` | lines 70, 108, 149, 159 | `Scan-registry read projection`; `MPI-T2` | Memory Plane map | VALUE_SET | ACCEPT |
| Existing readout route authenticates service token or session | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | lines 135-163 | `verifyServiceTokenRequest`; `verifySessionCookie`; unauthorized branch | Memory readout route | EXISTS | ACCEPT |
| Existing route candidate schema has summary-compatible fields | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | lines 19-28, 82-103 | `MemoryRuntimeReadoutBody.candidates` | Memory readout route body | EXISTS | ACCEPT |
| Existing route passes candidates to readout projection and returns fixed false flags | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | lines 177-204 | `buildMemoryRuntimeReadout`; `rawMemoryReleased`; `canReinject` | Memory readout route | EXISTS | ACCEPT |
| Existing projection strips candidate content and fixes false flags | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` | lines 15-22, 35-54 | `sanitizeCandidates`; `sanitizeWorkflowResult` | Memory runtime readout projection | LITERAL_INVARIANT | ACCEPT |
| Existing tests prove content stripping and false flags | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.test.ts` | lines 29-60 | `buildMemoryRuntimeReadout` tests | Vitest test surface | EXISTS | ACCEPT |
| Existing route tests prove auth failure, invalid fields, sanitized projection, and false flags | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.test.ts` | lines 52-101 | `/api/memory/readout` tests | Vitest route test surface | EXISTS | ACCEPT |
| Registry aggregate is generated from per-entry sources and must not be hand-edited | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` | lines 51-75 | registry location; generator command; drift checker | GC-051 standard | VALUE_SET | ACCEPT |
| Registry entries expose semanticRegions and findings | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` | lines 79-105 | `semanticRegions`; `findings` | GC-051 standard | VALUE_SET | ACCEPT |
| Finding records expose id, summary, disposition, nextAction, defectClass, learningLane | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` | lines 107-122 | `findings[]` fields | GC-051 standard | VALUE_SET | ACCEPT |
| Finding Discovery Rule defines keyword matching against semanticRegions or findings summaries | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` | lines 304-315 | Finding Discovery Rule | GC-051 standard | VALUE_SET | ACCEPT |
| cvf-web package has focused test and TypeScript commands | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | scripts section | `test run script`; `check script` | cvf-web package scripts | EXISTS | ACCEPT |

## Negative Search And Collision Discipline

Search roots: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src`; `docs`.

Search command / query:
`rg -n "scan-registry-memory-projection|Scan Registry Episodic Read Projection|registryProjectionSource|scanRegistryMemoryCandidate" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src docs`

Coverage: runtime source, tests, reference docs, reviews, work orders, and
baselines under the searched roots.

| Check | Command or evidence | Result | Collision / disposition |
|---|---|---|---|
| helper file absent | `Test-Path EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/scan-registry-memory-projection.ts` | `False` | worker may create |
| test file absent | `Test-Path EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/scan-registry-memory-projection.test.ts` | `False` | worker may create |
| MPI-T2 references exist in roadmap/map | `rg -n "MPI-T2|Scan Registry Episodic"` | planning references only | no implementation collision |
| route already has candidate schema | Source Verification Block route rows | compatible surface | no route edit needed |

## Current Runtime Freshness Verification

| Claim | Current evidence | Disposition |
|---|---|---|
| Existing readout route can consume candidates if supplied by caller | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` candidate schema and tests cited in Source Verification Block | ACCEPT |
| Existing route auth remains unchanged | route auth lines cited in Source Verification Block | ACCEPT |
| Existing projection strips raw candidate content | `memory-runtime-readout.ts` and focused tests cited in Source Verification Block | ACCEPT |
| GC-051 aggregate is generated and should not be hand-edited | GC-051 standard lines 51-75 cited in Source Verification Block | ACCEPT |
| MPI-T2 projection helper is not present before dispatch | `Test-Path` output `False` recorded by dispatcher | ACCEPT |
| Provider registry surface is not changed or claimed by MPI-T2 | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` exports `ProviderRegistry`; `PROVIDER_CAPABILITY_REGISTRY` is not claimed or modified by MPI-T2 | N/A_WITH_REASON |
| Provider/live proof is not authorized | Forbidden Scope and Claim Boundary in this work order | N/A_WITH_REASON |
| Public-sync is not authorized | Public Export Disposition in this work order | N/A_WITH_REASON |

## Projection Helper Contract

The helper must:

1. Define narrow TypeScript types for the subset of GC-051 registry data it
   consumes.
2. Accept parsed registry data or registry entries as function input.
3. Extract deterministic domain keywords from a query.
4. Match keywords against `semanticRegions` and `findings[].summary`.
5. Return Memory retrieval candidate-compatible summaries that can be passed as
   `candidates` to `buildMemoryRuntimeReadout` or the existing route body.
6. Include source attribution using registry entry id and finding id.
7. Avoid raw packet content and avoid copying long findings beyond concise
   summaries.
8. Preserve input immutability.
9. Return an empty list for no matches.
10. Avoid filesystem writes, registry writes, route auth changes, and route
    schema changes.

The helper may include constant lifecycle/audit-trust defaults only if tests
prove deterministic values and the reference contract records that they are
projection metadata, not source authority.

## Required Tests

Focused tests must cover:

- keyword match against `semanticRegions`;
- keyword match against `findings[].summary`;
- no-match returns empty list;
- projected candidate contains source attribution to entry id and finding id;
- projected candidate has no raw `content`;
- input registry object is not mutated;
- duplicate or repeated matching does not create unstable duplicate candidates;
- `buildMemoryRuntimeReadout` consumes projected candidates while preserving
  `rawMemoryReleased=false`, `canReinject=false`, and no RAW sentinel leakage;
- invalid or incomplete registry entries degrade safely without throwing an
  unhandled exception.

## Execution Plan

1. Capture `executionBaseHead`.
2. Capture `git status --short`.
3. Read all Required First Reads.
4. Create the projection helper.
5. Create focused tests.
6. Create the MPI-T2 reference contract.
7. Update the Memory Plane map narrowly from parked gap to dispatched/active
   helper status if implementation passes.
8. Run required checks.
9. Create worker-return artifact.
10. Return `COMPLETE_PENDING_REVIEW` uncommitted or `BLOCKED_WITH_REASON`.

## Pre-Flight Checks

Before dispatching this work order, dispatcher/reviewer must run:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/check_work_order_dispatch_quality.py --base 867b4c05 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 867b4c05 --head HEAD
python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base 867b4c05 --head HEAD --enforce
```

Worker must also run the Required Checks section.

## Required Checks

The worker must run:

```powershell
git rev-parse --short HEAD
git status --short
Push-Location EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npm run test:run -- src/lib/scan-registry-memory-projection.test.ts src/lib/memory-runtime-readout.test.ts src/app/api/memory/readout/route.test.ts
npm run check
Pop-Location
python governance/compat/run_worker_return_fast_gate.py
```

If `npm run check` fails due an unrelated pre-existing error, return
`BLOCKED_WITH_REASON` with exact command output and do not widen scope.

## Evidence Requirements

The worker-return packet must record:

- actual `executionBaseHead`;
- actual before/after `git status --short`;
- exact changed-file manifest;
- focused Vitest command output;
- TypeScript check output;
- worker-return fast gate output;
- explicit no-route-edit/no-registry-write/no-generated/no-session/no-public/
  no-provider/no-MCP/no-durable-write boundary;
- exact Claim Boundary and Public Export Disposition.

## Worker Autonomy / No-Question Rule

The worker must repair allowed-scope helper, test, reference, map, packet-shape,
source-fidelity, or gate failures and rerun relevant gates without asking the
operator.

The worker must stop and return `BLOCKED_WITH_REASON` only when the repair
would exceed Allowed scope, change the claim boundary, require route/schema/
provider/live/public-sync/MCP/generated/session/handoff/durable edits, release a
new dependency, consume secrets or quota, alter parked-lane ordering, touch
forbidden paths, or perform destructive or irreversible actions.

## Acceptance Criteria

| Criterion | Required evidence |
|---|---|
| Helper exists | `scan-registry-memory-projection.ts` |
| Focused tests exist | `scan-registry-memory-projection.test.ts` |
| GC-051 matching reused | tests and source use `semanticRegions` and `findings[].summary` |
| Candidate shape compatible with Memory readout | tests pass through `buildMemoryRuntimeReadout` |
| Raw content absent | tests prove no `content` and no RAW sentinel in serialized readout |
| No mutation | tests prove input object remains unchanged |
| No route edit | `git diff --name-status` contains no readout route file |
| No registry write | `git diff --name-status` contains no registry aggregate/source/generator path |
| Reference contract exists | `docs/reference/CVF_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION.md` |
| Memory Plane map updated narrowly | map records MPI-T2 projection helper status and boundary |
| Required checks pass | worker-return evidence |

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only after allowed artifacts exist, focused
tests pass, TypeScript check passes, worker-return fast gate passes or records
allowed `N/A with reason`, and all changes remain uncommitted.

Return `BLOCKED_WITH_REASON` when source verification fails, required source
cannot be read, a required gate fails outside worker-owned scope, or a necessary
action would exceed Allowed scope.

## Review Gate

Reviewer/closer must reject, repair inside reviewer-owned closure scope, or
return the worker output if:

- any path outside Allowed Scope is changed by the worker;
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

## Operator Checkpoint

Human authorization is required before route edits, route schema changes,
registry writes, durable writes, generated aggregate edits, provider/live proof,
public-sync, CLI/MCP adapter behavior, MPI-T3, MPI-T4, dependency changes,
session/handoff edits by worker, risk-level change, or universal-control claim.

No human authorization is needed for allowed-scope remediation during worker
execution.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order requirement | Disposition |
|---|---|---|
| MPI-T2 exposes GC-051 findings as read-only summary-only projection | Projection Helper Contract and Required Tests | ACCEPT |
| Reuse existing summary-only invariants | Source Verification Block and tests through `buildMemoryRuntimeReadout` | ACCEPT |
| Derived view only, not registry write path | Forbidden Scope and Acceptance Criteria | ACCEPT |
| Reuse Finding Discovery Rule | helper must match semanticRegions and findings summaries | ACCEPT |
| No provider call; deterministic and testable | Required Checks and Forbidden Scope | ACCEPT |
| Runtime route tests required for MPI-T2/T3 if later authorized | focused route/readout tests included without route edit | ACCEPT |

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| Foundation storage class | Memory Plane projection helper and reference contract |
| New durable storage | none |
| Generated aggregate impact | none |
| Source layout | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/scan-registry-memory-projection.ts`; focused test beside it |
| Index/front-door updates | `docs/reference/CVF_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION.md`; `docs/reference/CVF_MEMORY_PLANE_MAP.md` |
| Layout boundary | no route edit, no registry source/aggregate edit, no durable store, no generated state, no public-sync |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | MPI-T2 projection helper work order only |
| claimDisposition | N/A with reason: no Delta execution-control behavior is implemented or claimed |
| receiptEvidence | N/A with reason: no Delta receipt is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed by dispatch |
| invocationBoundary | deterministic local helper/test after worker execution |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | summary-only read projection helper and reference contract |
| forbiddenExpansion | route edit, registry write, durable write, provider/live, public-sync, CLI/MCP adapter, queue/daemon, watcher, readiness, full-hook equivalence, cost optimization, and universal control remain out of scope |

## Corpus Completeness And Report Integrity

- Corpus task class: NOT_APPLICABLE_WITH_REASON - MPI-T2 dispatch creates a
  projection helper and does not open a new corpus scan.
- Corpus root: NOT_APPLICABLE_WITH_REASON - no corpus root is assigned.
- Snapshot time: NOT_APPLICABLE_WITH_REASON - no corpus snapshot is taken.
- Enumeration command: filesystem-backed direct file reads listed in Source
  Verification Block; no corpus enumeration command is authorized.
- Manifest artifact or inline manifest: inline Source Verification Block above.
- Manifest hash: NOT_APPLICABLE_WITH_REASON - no corpus manifest hash is created.
- Processing ledger artifact or inline ledger: inline Source Verification Block
  and semantic sampling in paired GC-018 baseline.
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

## Worker Return Packet Shape Contract

The worker-return artifact must include these required terms and sections:

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
| Claim Boundary | no route edit, registry write, raw release, reinjection, public/provider/adapter scope |
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

## Closure Checklist

Reviewer/closer closure evidence must resolve these items:

- Required deliverables exist.
- No forbidden paths changed.
- Projection helper is deterministic and read-only.
- Focused tests cover matching, no-match, no mutation, duplicate/source
  attribution, sentinel stripping, and fixed false flags.
- `npm run check` passes or blocker is returned without scope expansion.
- Memory Plane map update is narrow and does not overclaim route wiring.
- Reference contract states route, registry, durable-store, provider/live,
  public-sync, and adapter boundaries.
- Worker-return packet includes required sections and worker-experience token.
- Reviewer-fast or stricter gate passes.
- Commit ownership remains reviewer/closer only.
- Session-sync is performed only if mode or next-move surfaces change.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | `Status: DISPATCHED_TO_WORKER` | PASS_FOR_DISPATCH |
| GC-018 status | `docs/baselines/CVF_GC018_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION_2026-06-22.md` | `Status: DISPATCHED_TO_WORKER` | PASS_FOR_DISPATCH |
| Worker return | `docs/reviews/CVF_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION_WORKER_RETURN_2026-06-22.md` | worker-owned return after execution | PENDING_WORKER |
| Completion or reviewer artifact | `docs/reviews/CVF_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION_COMPLETION_2026-06-22.md` | reviewer-owned after worker return | PENDING_REVIEWER |
| Roadmap state | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | MPI-T2 row updated to dispatch | PASS_FOR_DISPATCH |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | no registry JSON mutation authorized | N/A with reason |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | no registry Markdown mutation authorized | N/A with reason |
| External evidence digest | N/A | no external evidence digest created | N/A with reason |
| System loop interlock | N/A | no system-loop behavior changed by dispatch | N/A with reason |
| Session continuity | active session front-door/state/handoff after material dispatch | session-sync follows material dispatch if accepted | PENDING_SESSION_SYNC |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance MPI-T2 worker dispatch. No public-sync remote, public
commit, public artifact path, public README/catalog claim, or public repository
mutation is authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author |
| Provider or surface | local workspace |
| Session or invocation | MPI-T2 work order authoring, 2026-06-22 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | startup reads, source verification reads, apply_patch edits, dispatch gates |
| Target paths | `docs/baselines/CVF_GC018_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION_2026-06-22.md`; this work order; MPI roadmap |
| Allowed scope source | operator instruction selecting MPI-T2 |
| Before status evidence | HEAD `867b4c05`; clean worktree before dispatch authoring |
| After status evidence | MPI-T2 GC-018/work order released for worker dispatch; uncommitted until dispatcher commit |
| Diff evidence | pre-dispatch gates required before commit |
| Approval boundary | dispatch artifact only; worker implementation remains uncommitted |
| Claim boundary | dispatch packet only; no route edit, registry write, durable write, provider/live, public-sync, or adapter behavior |
| Agent type | dispatcher |
| Invocation ID | `mpi-t2-scan-registry-episodic-read-projection-work-order-2026-06-22` |
| Expected manifest | MPI-T2 GC-018 baseline; MPI-T2 work order; MPI roadmap status update |
| Actual changed set | checked by dispatch gates before commit |
| Manifest delta | MATCH |

## Claim Boundary

This work order dispatches only MPI-T2's bounded scan-registry episodic read
projection helper, focused tests, reference contract, Memory Plane map update,
and worker-return evidence. It does not authorize Memory readout route edits,
route schema changes, registry source or aggregate edits, durable writes,
registry generator changes, provider/live proof, public-sync, actual CLI/MCP
adapter behavior, vector DB, graph persistence, direct interception,
queue/daemon, watcher, readiness, cost optimization, or universal
governed-coding control.
