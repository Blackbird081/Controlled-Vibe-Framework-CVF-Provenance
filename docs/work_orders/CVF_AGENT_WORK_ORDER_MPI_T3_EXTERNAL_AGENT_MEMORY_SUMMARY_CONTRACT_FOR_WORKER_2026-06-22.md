# CVF Agent Work Order - MPI-T3 External Agent Memory Summary Contract

Memory class: FULL_RECORD

Status: DISPATCHED_TO_WORKER

Date: 2026-06-22

docType: work_order

dispatchBaseHead: a224da57

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Worker. Reviewer/closer is a separate role for the returned worker
packet.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_MPI_T3_EXTERNAL_AGENT_MEMORY_SUMMARY_CONTRACT_FOR_WORKER_2026-06-22.md`

Current status: `DISPATCHED_TO_WORKER`. Dependencies released by MPI-T2 closure
artifact `docs/reviews/CVF_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION_COMPLETION_2026-06-22.md`
at material commit `468ca3be` and MPI Phase 2 roadmap
`docs/roadmaps/CVF_MPI_PHASE2_EXTERNAL_MEMORY_READ_ROADMAP_2026-06-22.md` at
material commit `70963abc`. This work order releases MPI-T3 only.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: worker must capture with `git rev-parse --short HEAD` at
worker start.

Current-time notes: MPI-T3 is a bounded documentation-only contract tranche. It
defines the read-side external-agent memory summary contract that is the
counterpart of the LSC-T6 write-side signal contract. It does not change any
runtime route, helper, checker, or test.

Do-not-misread notes: do not edit the Memory readout route, Memory runtime
projection, scan-registry projection helper, any other runtime source or test,
registry entries, generated registry aggregate, registry Markdown, registry
generator, durable store, session state, active handoff, public-sync, MCP
packages, dependency manifests, provider configuration, `governance/compat/*.py`,
or `.github/**`. Do not implement MPI-T4, MPI-T5, a federated helper, a checker,
vector DB, graph persistence, external adapter behavior, provider/live proof,
public-sync, arbitrary command execution, EDIT/COMMIT execution, queue, daemon,
watcher, readiness, or universal governed-coding-control claims.

Required first actions: read this work order, read the paired MPI-T3 GC-018
baseline, read the MPI Phase 2 roadmap, read the MPI parent roadmap, read
`docs/reference/CVF_MEMORY_PLANE_MAP.md`, read the LSC-T6 write-side contract,
read the Memory readout route, read `memory-runtime-readout.ts`, read the RSE-T1
and RSE-T2 addenda, read the INDEX classification standard, capture
`executionBaseHead`, and inspect `git status --short`.

Return contract: return `COMPLETE_PENDING_REVIEW` with only allowed uncommitted
artifacts, actual `executionBaseHead`, actual `git status --short`, autorun and
worker-return gate evidence, and no commit. If blocked, return
`BLOCKED_WITH_REASON` and name the exact dependency, source, or gate.

The worker-return artifact must include either the structured
`WORKER_EXPERIENCE_RETRO` block or the exact asserting
`WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` line.

## Purpose

Author a deterministic, documentation-only External Agent Memory Summary
Contract that defines which caller may request a memory summary, which source
surfaces may be consulted, which request and response fields are allowed, and
how raw content, reinjection, route mutation, registry mutation, and adapter
execution stay blocked.

MPI-T3 exists to define the safe external read boundary before any later
federated helper, checker, or runtime decision packet in MPI Phase 2.

## Agent Roles

| Role | Owner | Commitment boundary |
|---|---|---|
| Roadmap author | Codex | authored the MPI Phase 2 roadmap; remains reviewer/closer |
| Dispatch author | assigned dispatch author | creates GC-018 baseline and this worker packet |
| Work-order reviewer | Codex | reviews this work order before worker execution |
| Worker | assigned worker | edits only Allowed scope and returns uncommitted |
| Reviewer/closer | Codex in reviewer-return phase | validates contract content, repairs allowed-scope packet defects, commits accepted material, and performs session sync if needed |
| Operator | human operator | checkpoint for scope expansion, route/schema/provider/live/public/adapter/generated/session/durable work, secrets, or destructive action |

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-22: author MPI-T3 work order from Phase 2 roadmap | ACCEPT |
| MPI-T3 GC-018 baseline | `docs/baselines/CVF_GC018_MPI_T3_EXTERNAL_AGENT_MEMORY_SUMMARY_CONTRACT_2026-06-22.md` | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V21_2026-06-22.md` | ACCEPT |
| MPI Phase 2 roadmap | `docs/roadmaps/CVF_MPI_PHASE2_EXTERNAL_MEMORY_READ_ROADMAP_2026-06-22.md` | ACCEPT |
| MPI parent roadmap | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | ACCEPT |
| Memory Plane map | `docs/reference/CVF_MEMORY_PLANE_MAP.md` | ACCEPT |
| LSC-T6 write-side signal contract | `docs/reference/learning_signal_chain/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT.md` | SOURCE_AUTHORITY_FOR_WRITE_SIDE_COUNTERPART |
| Memory readout route | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | SOURCE_AUTHORITY_FOR_EXISTING_ROUTE_SHAPE |
| Memory runtime readout projection | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` | SOURCE_AUTHORITY_FOR_SUMMARY_ONLY_SANITIZATION |
| MPI-T2 reference contract | `docs/reference/CVF_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION.md` | SOURCE_AUTHORITY_FOR_DERIVED_PROJECTION_BOUNDARY |
| RSE-T1 / RSE-T2 addenda | `docs/reference/role_switch_envelope/CVF_RSE_T1_OPERATOR_QUESTION_BOUNDARY_ADDENDUM.md`; `docs/reference/role_switch_envelope/CVF_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_ADDENDUM.md` | SOURCE_AUTHORITY_FOR_FINDING_ROUTING |
| INDEX classification standard | `docs/reference/CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21.md` | SOURCE_AUTHORITY_FOR_DOC_CLASSIFICATION |

## Dependency Release Gate

| Dependency | Release evidence | Current status |
|---|---|---|
| MPI-T2 closure | `docs/reviews/CVF_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION_COMPLETION_2026-06-22.md`; material commit `468ca3be` | RELEASED |
| MPI Phase 2 roadmap readiness | `docs/roadmaps/CVF_MPI_PHASE2_EXTERNAL_MEMORY_READ_ROADMAP_2026-06-22.md`; material commit `70963abc` | RELEASED |
| Operator selection | active next-move surfaces permit MPI-T3 work-order authoring; operator selected MPI-T3 on 2026-06-22 | RELEASED |
| Source verification refresh | this work order and paired GC-018 cite current route/projection/LSC-T6/RSE/INDEX source sections | RELEASED |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | roadmap author releases roadmap; dispatch author releases packet; work-order reviewer accepts packet; worker writes the contract/README/worker-return; reviewer/closer validates and commits if accepted |
| phase | DISPATCH_COMPLETE; EXECUTION; CLOSURE; SESSION_SYNC_IF_NEEDED |
| baseHeadFor(phase) | `dispatchBaseHead=a224da57`; `executionBaseHead` captured by worker at start; `closureBaseHead` set by reviewer before closure commit |
| changedSetScope(phase) | worker changes only Allowed scope; reviewer/closer owns status/closure/session-sync |
| traceScope(phase, actor) | worker-return trace covers MPI-T3 artifacts; reviewer trace covers review/closure |
| commitOwner(phase) | worker commits nothing; reviewer/closer owns accepted material/closure/session-sync commit |
| crossBatchIsolation | do not mix MPI-T3 with MPI-T4/T5/T6, route schema changes, helper implementation, registry writes, durable writes, provider/live, public-sync, adapter behavior, session-sync, or unrelated runtime work |
| Before status evidence | committed base `a224da57`; MPI Phase 2 roadmap continuity recorded the work-order-authoring next move |
| nextMoveSurfaces | reviewer updates only during MPI-T3 closure if current mode or next allowed move changes |
| Closer designation | reviewer/closer role is the designated closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_SUMMARY_CONTRACT_COMPLETION_2026-06-22.md` |
| reviewerOwnedClosurePaths | this work order; GC-018 baseline; MPI Phase 2 roadmap status row; worker-return artifact; reviewer-owned completion review; optional session-sync surfaces if accepted |
| workerReturnStatus | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| closer | reviewer/closer role |

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Selected route | `MULTI_AGENT_MULTI_ROLE` |
| Intake summary | operator selected MPI-T3 work-order authoring from MPI Phase 2 roadmap `docs/roadmaps/CVF_MPI_PHASE2_EXTERNAL_MEMORY_READ_ROADMAP_2026-06-22.md` at material commit `70963abc` |
| Scope assessment | bounded R1 documentation-only reference contract and README pointer |
| Risk sensitivity | documentation-only contract; no route edit, no helper, no registry write, no provider/live, no public-sync |
| Intake owner | dispatch author |
| Execution owner | worker |
| Review owner | reviewer/closer |
| Commit mode | `WORKER_MUST_NOT_COMMIT` |
| Escalation condition | `BLOCKED_WITH_REASON` if required action exceeds allowed scope or requires route/schema/helper/provider/live/public/generated/session/durable/adapter work |
| Rationale | release only the read-side contract before any federated helper, checker, or runtime decision packet |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | roadmap/operator selection to CVF-owned work order |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | MPI-T3 work order |
| Disposition | ADAPT as bounded CVF-owned documentation-only read contract packet |
| Claim boundary | no external input is source authority; LSC-T6, current runtime source, MPI-T2 reference, and Memory Plane map control |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: MPI-T3 does not rescan or absorb legacy source
families. MPI-T0/MPI-T1/MPI-T2 already handled INDEX, Memory Plane map, and the
scan-registry projection prerequisites. MPI-T3 consumes the LSC-T6 write-side
contract and current Memory readout source only.

## Required First Reads

| Source | Reason |
|---|---|
| `docs/reference/guard_orientation/README.md` | task-first guard map and worker-return packet requirements |
| `docs/baselines/CVF_GC018_MPI_T3_EXTERNAL_AGENT_MEMORY_SUMMARY_CONTRACT_2026-06-22.md` | GC-018 authorization and claim boundary |
| this work order | current worker packet and allowed scope |
| `docs/roadmaps/CVF_MPI_PHASE2_EXTERNAL_MEMORY_READ_ROADMAP_2026-06-22.md` | MPI-T3 required contract content |
| `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | MPI-T3 external read half background |
| `docs/reference/CVF_MEMORY_PLANE_MAP.md` | current Memory Plane map and parked MPI-T3 gap |
| `docs/reference/learning_signal_chain/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT.md` | write-side counterpart and adapterContractOnly pattern |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | existing auth and route response flags |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` | existing summary-only sanitization invariants |
| `docs/reference/CVF_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION.md` | derived projection boundary, not authority |
| `docs/reference/role_switch_envelope/CVF_RSE_T1_OPERATOR_QUESTION_BOUNDARY_ADDENDUM.md` | question classes for routing worker findings |
| `docs/reference/role_switch_envelope/CVF_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_ADDENDUM.md` | Worker Return Jurisdiction Block fields |
| `docs/reference/CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21.md` | GOVERNED_DOC vs INDEX_ARTIFACT classification |

## Allowed Scope

The worker may change only:

- `docs/reference/memory_plane/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_SUMMARY_CONTRACT.md`
- `docs/reference/memory_plane/README.md`
- `docs/reviews/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_SUMMARY_CONTRACT_WORKER_RETURN_2026-06-22.md`

## Write Ownership

| Path | Owner during worker execution | Disposition |
|---|---|---|
| `docs/reference/memory_plane/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_SUMMARY_CONTRACT.md` | worker | create |
| `docs/reference/memory_plane/README.md` | worker | create |
| `docs/reviews/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_SUMMARY_CONTRACT_WORKER_RETURN_2026-06-22.md` | worker | create |
| `docs/baselines/CVF_GC018_MPI_T3_EXTERNAL_AGENT_MEMORY_SUMMARY_CONTRACT_2026-06-22.md` | reviewer/closer | no worker edit |
| this work order | reviewer/closer | no worker edit |
| `docs/roadmaps/CVF_MPI_PHASE2_EXTERNAL_MEMORY_READ_ROADMAP_2026-06-22.md` | reviewer/closer | no worker edit |
| route files, runtime helpers/tests, registry aggregate/sources, durable store, generated state, active handoff, public-sync, MCP packages, dependency manifests, `governance/compat/*.py`, `.github/**` | out of worker scope | forbidden |

## Forbidden Scope

The worker must not:

- edit `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts`,
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts`,
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/scan-registry-memory-projection.ts`,
  or any other runtime source, helper, or test;
- edit Memory write route, durable store, scan registry source entries,
  generated registry aggregate, registry Markdown, registry generator, session
  state, active handoff, root startup routers, public-sync, MCP packages,
  dependency manifests, provider configuration, `governance/compat/*.py`,
  `.github/**`, or public repository files;
- implement a federated helper, checker, vector DB, embedding store, graph
  persistence, CLI/MCP adapter behavior, provider/live proof, wrapper/proxy
  enforcement, direct IDE/shell/git interception, arbitrary command execution,
  EDIT/COMMIT execution, queue, daemon, watcher, readiness, full-hook
  equivalence, cost optimization, or universal governed-coding control;
- mutate runtime Learning Plane state, create durable writes, write registry
  entries, run a registry generator, change route auth, change route schema, or
  claim production/public readiness.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| MPI-T3 is the External Agent Memory Summary Contract tranche and is contract-first | `docs/roadmaps/CVF_MPI_PHASE2_EXTERNAL_MEMORY_READ_ROADMAP_2026-06-22.md` | Proposed Tranche Sequence; MPI-T3 External Agent Memory Summary Contract | `MPI-T3`; `External Agent Memory Summary Contract` | MPI Phase 2 roadmap | VALUE_SET | ACCEPT |
| MPI-T3 required contract content lists adapterContractOnly and summary-only invariants | `docs/roadmaps/CVF_MPI_PHASE2_EXTERNAL_MEMORY_READ_ROADMAP_2026-06-22.md` | Required contract content | `adapterContractOnly`; `rawMemoryReleased`; `canReinject` | MPI Phase 2 roadmap | VALUE_SET | ACCEPT |
| LSC-T6 defines the write-side external-agent signal contract as adapter-contract-only | `docs/reference/learning_signal_chain/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT.md` | line 38 adapterContractOnly statement | `adapterContractOnly` | LSC-T6 external signal contract | LITERAL_INVARIANT | ACCEPT |
| Existing readout route authenticates by service token or session before readout | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | lines 3-4 imports; lines 148-156 auth branch | `verifyServiceTokenRequest`; `verifySessionCookie` | Memory readout route | EXISTS | ACCEPT |
| Existing readout route returns fixed false raw/reinject flags | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | lines 202-203 | `rawMemoryReleased`; `canReinject` | Memory readout route | LITERAL_INVARIANT | ACCEPT |
| Runtime readout projection omits raw candidate content and fixes false flags | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` | lines 9-23 content omission; lines 35-54 sanitizeWorkflowResult; line 57 buildMemoryRuntimeReadout | `sanitizeCandidates`; `sanitizeWorkflowResult`; `buildMemoryRuntimeReadout`; `content` | Memory runtime readout projection | LITERAL_INVARIANT | ACCEPT |
| Scan-registry projection helper is summary-only and not route-wired | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/scan-registry-memory-projection.ts` | line 119 projection function | `projectScanRegistryFindings` | scan registry memory projection helper | EXISTS | ACCEPT |
| MPI-T2 reference defines the projection as summary-only and not route-wired | `docs/reference/CVF_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION.md` | Readout Compatibility; Route Wiring Status | `summary-only`; `Route Wiring Status` | MPI-T2 reference contract | VALUE_SET | ACCEPT |
| RSE-T1 defines the four question classes used to route worker findings | `docs/reference/role_switch_envelope/CVF_RSE_T1_OPERATOR_QUESTION_BOUNDARY_ADDENDUM.md` | Question Classification table lines 55-57 | `ASK_OPERATOR`; `ASK_REVIEWER_OR_CLOSER`; `SELF_HANDLE_WITHIN_SCOPE` | RSE-T1 addendum | VALUE_SET | ACCEPT |
| RSE-T2 defines the Worker Return Jurisdiction Block and operatorActionRequired rule | `docs/reference/role_switch_envelope/CVF_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_ADDENDUM.md` | The Worker Return Jurisdiction Block; lines 66-67 | `Worker Return Jurisdiction Block`; `operatorActionRequired` | RSE-T2 addendum | VALUE_SET | ACCEPT |
| INDEX standard requires GOVERNED_DOC to never carry an INDEX type label | `docs/reference/CVF_INDEX_CLASSIFICATION_STANDARD_2026-06-21.md` | Core Distinction lines 54-55; line 60 | `GOVERNED_DOC`; `INDEX_ARTIFACT` | INDEX classification standard | VALUE_SET | ACCEPT |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED
recomputeReason: worker must re-read and source-verify current CVF-governed
sources before citing route, projection, LSC, RSE, INDEX, or roadmap facts in
the MPI-T3 contract.
freshRecomputeRequired: YES
unicodePathHandling: literal repo-relative paths and UTF-8-safe readers required
extractedTextAuthority: N/A with reason

| Evidence class | Reused source | Encoding / path handling | Disposition |
|---|---|---|---|
| Prior closure evidence | MPI-T2 completion review `docs/reviews/CVF_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION_COMPLETION_2026-06-22.md` at material commit `468ca3be` | ASCII path; cited as dependency-release evidence only | ACCEPT |
| Prior roadmap evidence | MPI Phase 2 roadmap `docs/roadmaps/CVF_MPI_PHASE2_EXTERNAL_MEMORY_READ_ROADMAP_2026-06-22.md` at material commit `70963abc` | ASCII path; cited as roadmap-to-work-order source | ACCEPT |
| Runtime source evidence | Memory readout route and projection source files under `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/` | ASCII repo-relative paths; line/section references must be source-verified by worker before citing in deliverables | ACCEPT |
| External input | operator-provided Memory Plane/INDEX/KGR critique already adapted into the roadmap | no external text becomes CVF authority; source facts must be re-verified against governed CVF surfaces | ACCEPT |
| Unicode or non-ASCII evidence | N/A | worker-authored artifacts must default to ASCII; quote non-ASCII only if unavoidable and record the exception | N/A_WITH_REASON |
| Extracted text / OCR / binary evidence | N/A | no extracted text, OCR evidence, screenshot text, or binary source bundle is reused | N/A_WITH_REASON |

This work order does not rely on provider-private memory, chat-only facts,
external source bundles, T11B evidence, OCR output, copied public docs, or
Unicode-path evidence as authority. If the worker learns a source fact from any
non-CVF or provider-specific surface, the worker must re-verify it against a
CVF-governed source before using it.

## New Doc-Only Terms

| Proposed term | Owner in MPI-T3 | Runtime status | Reason |
|---|---|---|---|
| `memorySummaryRequest` | MPI-T3 contract | DOC_ONLY_NEW until a separate tranche implements it | allowed request field set for an external memory summary read |
| `memorySummaryResponse` | MPI-T3 contract | DOC_ONLY_NEW until a separate tranche implements it | allowed response field set bounding summary-only output |
| `sourceScopeSelector` | MPI-T3 contract | DOC_ONLY_NEW | names which allowed source surfaces a request may consult |
| `forbiddenFieldFlags` | MPI-T3 contract | DOC_ONLY_NEW | records that raw content, reinjection, and durable writes stay blocked |

These terms are not existing route fields, registry fields, CLI/MCP fields, or
public API identifiers. They become real only if a future source-verified work
order implements them.

## Negative Search And Collision Discipline

Search roots: `docs/reference`; `docs/reviews`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src`.

Search command / query:
`rg -n "External Agent Memory Summary Contract|memorySummaryRequest|memorySummaryResponse|sourceScopeSelector|forbiddenFieldFlags" docs EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src`

Coverage: reference docs, reviews, work orders, baselines, and runtime source
under the searched roots.

| Check | Command or evidence | Result | Collision / disposition |
|---|---|---|---|
| target directory absent | `Test-Path docs/reference/memory_plane` | `False` | worker may create |
| contract file absent | `Test-Path docs/reference/memory_plane/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_SUMMARY_CONTRACT.md` | `False` | worker may create |
| MPI-T3 references exist in roadmap/map | `rg -n "MPI-T3|External Agent Memory"` | planning references only | no implementation collision |
| proposed doc-only terms not present in runtime source | `rg -n "memorySummaryRequest|memorySummaryResponse"` | absent in runtime source | no symbol collision |

## Current Runtime Freshness Verification

| Claim | Current evidence | Disposition |
|---|---|---|
| Existing readout route authenticates before readout | route auth lines 148-156 cited in Source Verification Block | ACCEPT |
| Existing readout route returns fixed false raw/reinject flags | route lines 202-203 cited in Source Verification Block | ACCEPT |
| Existing projection omits raw candidate content | `memory-runtime-readout.ts` lines 9-23, 35-54 cited in Source Verification Block | ACCEPT |
| Scan-registry projection is summary-only and not route-wired | projection helper line 119 and MPI-T2 reference cited in Source Verification Block | ACCEPT |
| MPI-T3 contract and target directory are not present before dispatch | `Test-Path` output `False` recorded by dispatcher | ACCEPT |
| Provider registry surface is not changed or claimed by MPI-T3 | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` exports `ProviderRegistry`; it is not claimed or modified by MPI-T3 | N/A_WITH_REASON |
| Provider/live proof is not authorized | Forbidden Scope and Claim Boundary in this work order | N/A_WITH_REASON |
| Public-sync is not authorized | Public Export Disposition in this work order | N/A_WITH_REASON |

## External Agent Memory Summary Contract Requirements

The worker must author a reference contract that:

1. Declares `adapterContractOnly=true` and states this defines IO shape and
   boundaries, mirroring the LSC-T6 write-side pattern.
2. Defines a `memorySummaryRequest` field set: task context, query topic,
   `sourceScopeSelector`, role identity, and max candidate count, marked as new
   doc-only fields.
3. Defines a `memorySummaryResponse` field set: bounded summaries, source
   attribution, confidence/disposition, freshness, and `forbiddenFieldFlags`,
   marked as new doc-only fields.
4. Explicitly inherits `rawMemoryReleased=false` and `canReinject=false` from
   the existing readout surface and cites the source lines.
5. Prohibits raw `content`, durable write, reinjection, route mutation, registry
   mutation, and external command execution.
6. Names the allowed source surfaces (Memory Plane map, MPI-T2 projection
   contract, LSC-T6 readout relationship, RSE references) as read-side scope
   without claiming runtime wiring.
7. Includes external knowledge intake routing for any external critique or
   returned output.
8. Includes RSE routing rules: routine reviewer/closer decisions route to
   reviewer/closer, operator-owned classes route to the operator, and in-scope
   findings are self-handled and captured.
9. Declares its own INDEX classification as `GOVERNED_DOC` (not an
   INDEX_ARTIFACT).

The contract must not implement or claim an MCP tool, CLI adapter, service
route, web route, authenticated runtime access, durable store, vector DB, graph
store, provider call, live proof, public-sync, worker apply mode, or commit
automation.

## README Pointer Requirements

The `docs/reference/memory_plane/README.md` front door must:

- name the new `memory_plane` reference directory and its purpose;
- point to the MPI-T3 contract as the active read-side contract;
- state the documentation-only, summary-only, adapter-contract-only boundary;
- declare its own INDEX classification as `GOVERNED_DOC`.

## Execution Plan

1. Capture `executionBaseHead`.
2. Capture `git status --short`.
3. Read all Required First Reads.
4. Create the `memory_plane` directory contract file.
5. Create the `memory_plane` README pointer.
6. Create the worker-return artifact.
7. Run required checks.
8. Return `COMPLETE_PENDING_REVIEW` uncommitted or `BLOCKED_WITH_REASON`.

## Pre-Flight Checks

Before dispatching this work order, dispatch author/reviewer must run:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/check_work_order_dispatch_quality.py --base a224da57 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base a224da57 --head HEAD
python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base a224da57 --head HEAD --enforce
```

Worker must also run the Required Checks section.

## Required Checks

The worker must run:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_automation_assist.py --base <executionBaseHead> --head HEAD --json --enforce
python governance/compat/run_worker_return_fast_gate.py
```

MPI-T3 is documentation-only, so no Vitest or TypeScript check is required. If a
required gate fails outside worker-owned scope, return `BLOCKED_WITH_REASON`
with exact command output and do not widen scope.

## Evidence Requirements

The worker-return packet must record:

- actual `executionBaseHead`;
- actual before/after `git status --short`;
- exact changed-file manifest;
- AAF helper `--json --enforce` output;
- worker-return fast gate output;
- explicit no-route-edit/no-helper/no-registry-write/no-generated/no-session/
  no-public/no-provider/no-MCP/no-durable-write boundary;
- exact Claim Boundary and Public Export Disposition.

## Worker Autonomy / No-Question Rule

The worker must repair allowed-scope contract, README, packet-shape,
source-fidelity, or gate failures and rerun relevant gates without asking the
operator. Required finding capture inside allowed scope is
`SELF_HANDLE_WITHIN_SCOPE`; the worker captures it in the worker-return and does
not ask.

The worker must stop and return `BLOCKED_WITH_REASON` only when the repair would
exceed Allowed scope, change the claim boundary, require route/schema/helper/
provider/live/public-sync/MCP/generated/session/handoff/durable edits, release a
new dependency, consume secrets or quota, alter parked-lane ordering, touch
forbidden paths, or perform a destructive or irreversible action. Out-of-scope
promotion candidates route to reviewer/closer via the Worker Return Jurisdiction
Block, not to the operator.

## Acceptance Criteria

| Criterion | Required evidence |
|---|---|
| Contract exists | `docs/reference/memory_plane/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_SUMMARY_CONTRACT.md` |
| README pointer exists | `docs/reference/memory_plane/README.md` |
| adapterContractOnly declared | contract states `adapterContractOnly=true` |
| Summary-only invariants inherited | contract cites `rawMemoryReleased=false`, `canReinject=false`, and content omission with source lines |
| No raw content / reinjection allowed | contract prohibits raw `content`, reinjection, durable write, route/registry mutation |
| Allowed request/response fields are doc-only | contract marks `memorySummaryRequest`/`memorySummaryResponse` fields as new doc-only |
| RSE routing present | contract includes RSE finding/promotion routing rules |
| INDEX classification | contract and README declare `GOVERNED_DOC` (not INDEX_ARTIFACT) |
| No route/helper edit | `git diff --name-status` contains no runtime route, helper, or test file |
| No registry write | `git diff --name-status` contains no registry aggregate/source/generator path |
| Required checks pass | worker-return evidence |

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only after the allowed artifacts exist, the
AAF helper passes with `defects=[]`, the worker-return fast gate passes or
records allowed `N/A with reason`, and all changes remain uncommitted.

Return `BLOCKED_WITH_REASON` when source verification fails, required source
cannot be read, a required gate fails outside worker-owned scope, or a necessary
action would exceed Allowed scope.

## Review Gate

Reviewer/closer must reject, repair inside reviewer-owned closure scope, or
return the worker output if:

- any path outside Allowed Scope is changed by the worker;
- the contract claims an MCP tool, CLI adapter, service route, web route,
  authenticated runtime access, durable store, vector DB, graph store, provider
  call, live proof, public-sync, worker apply mode, or commit automation;
- the contract flips or weakens `rawMemoryReleased=false` or `canReinject=false`;
- the contract permits raw `content`, reinjection, durable write, route
  mutation, or registry mutation;
- the contract omits RSE routing for worker findings and promotion candidates;
- the contract or README is mislabeled as an INDEX_ARTIFACT instead of
  GOVERNED_DOC;
- worker-return packet sections or gate evidence are missing;
- any route/schema/auth/provider/live/public/adapter claim appears.

## Operator Checkpoint

Human authorization is required before route edits, route schema changes, helper
or checker implementation, registry writes, durable writes, generated aggregate
edits, provider/live proof, public-sync, CLI/MCP adapter behavior, MPI-T4,
MPI-T5, MPI-T6, dependency changes, session/handoff edits by worker, risk-level
change, or universal-control claim.

No human authorization is needed for allowed-scope remediation during worker
execution.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order requirement | Disposition |
|---|---|---|
| MPI-T3 is contract-first | Allowed Scope includes reference/README/worker-return only | ACCEPT |
| Summary-only read boundary | Source Verification rows for `rawMemoryReleased`, `canReinject`, and omitted `content` | ACCEPT |
| Adapter-contract-only | contract states `adapterContractOnly=true`; Forbidden Scope rejects CLI/MCP adapter and route wiring | ACCEPT |
| Scan registry projection is derived and not authority | Source rows cite MPI-T2 and scan projection helper boundary | ACCEPT |
| INDEX applies to any new doc | contract and README declare GOVERNED_DOC | ACCEPT |
| RSE governs worker-return findings | Worker Return Jurisdiction Block required when findings/gate traps appear | ACCEPT |
| No runtime expansion | Claim Boundary and Delta Execution Claim Boundary Control Block list forbidden expansions | ACCEPT |

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| Foundation storage class | Memory Plane external-agent summary read contract |
| New durable storage | none |
| Generated aggregate impact | none |
| Source layout | N/A with reason: MPI-T3 is documentation-only; no source/test file is authorized |
| Index/front-door updates | `docs/reference/memory_plane/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_SUMMARY_CONTRACT.md`; `docs/reference/memory_plane/README.md` |
| Layout boundary | no route edit, no helper edit, no registry source/aggregate edit, no durable store, no generated state, no public-sync |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | MPI-T3 external memory summary contract work order only |
| claimDisposition | N/A with reason: no Delta execution-control behavior is implemented or claimed |
| receiptEvidence | N/A with reason: no Delta receipt is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed by dispatch |
| invocationBoundary | documentation-only reference contract and README pointer after worker execution |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | summary-only external memory read contract documentation only |
| forbiddenExpansion | route edit, helper implementation, checker, registry write, durable write, provider/live, public-sync, CLI/MCP adapter, vector DB, graph persistence, queue/daemon, watcher, readiness, full-hook equivalence, cost optimization, and universal control remain out of scope |

## Corpus Completeness And Report Integrity

- Corpus task class: NOT_APPLICABLE_WITH_REASON - MPI-T3 dispatch creates a
  documentation-only contract and does not open a new corpus scan.
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
- Reconciliation: manifest=inline Source Verification Block; ledger_terminal=READ for named source rows; exclusions=new corpus scan, helper implementation, checker implementation, route schema change, provider/live, public-sync, CLI/MCP adapter; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: new corpus scan, helper implementation, checker
  implementation, route schema change, provider/live proof, public-sync copy,
  and CLI/MCP adapter.
- Unreadable or unsupported files: 0.
- Aggregation check: NOT_APPLICABLE_WITH_REASON - no corpus aggregate is created
  or changed.
- Drift check: NOT_APPLICABLE_WITH_REASON - no corpus aggregate is changed.
- Output traceability: Allowed Scope and Source Verification Block define all
  worker output traceability.
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
| Worker Return Jurisdiction Block | present when the worker captures a finding, gate trap, or out-of-scope promotion candidate; otherwise the exact RSE N/A line |
| Claim Boundary | no route edit, helper edit, registry write, raw release, reinjection, public/provider/adapter scope |
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
- Contract declares `adapterContractOnly=true` and inherits summary-only
  invariants with source citation.
- Contract prohibits raw content, reinjection, durable write, route mutation,
  and registry mutation.
- Contract and README declare GOVERNED_DOC classification.
- Contract includes RSE finding/promotion routing.
- Worker-return packet includes required sections and worker-experience token.
- Worker Return Jurisdiction Block is present or the exact RSE N/A line is used.
- Reviewer-fast or stricter gate passes.
- Commit ownership remains reviewer/closer only.
- Session-sync is performed only if mode or next-move surfaces change.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | `Status: DISPATCHED_TO_WORKER` until reviewer closure | PASS |
| GC-018 status | `docs/baselines/CVF_GC018_MPI_T3_EXTERNAL_AGENT_MEMORY_SUMMARY_CONTRACT_2026-06-22.md` | `Status: DISPATCHED_TO_WORKER` until reviewer closure | PASS |
| Worker return | `docs/reviews/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_SUMMARY_CONTRACT_WORKER_RETURN_2026-06-22.md` | reviewer creates closure after accepting this worker-owned return | PASS |
| Completion or reviewer artifact | reviewer creates the completion review after accepting this return | reviewer-owned completion review | PASS |
| Roadmap state | `docs/roadmaps/CVF_MPI_PHASE2_EXTERNAL_MEMORY_READ_ROADMAP_2026-06-22.md` | MPI-T3 row updated at closure by reviewer | PASS |
| External evidence digest | N/A with reason: no external evidence digest created | N/A with reason |
| System loop interlock | N/A with reason: no system-loop behavior changed by dispatch | N/A with reason |
| Session continuity | active session front-door/state/handoff in reviewer-owned closure phase | PASS session-sync follows the accepted material closure commit if state changes | PASS |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| Runtime receipt evidence | N/A with reason: MPI-T3 creates no runtime receipt | N/A_WITH_REASON |
| `rawMemoryReleased` | `false` inherited and cited from the readout surface | PASS |
| `canReinject` | `false` inherited and cited from the readout surface | PASS |
| Raw content release | prohibited; contract forbids raw `content` and reinjection | PASS |
| Route behavior | unchanged; no Memory readout route file in changed set | PASS |
| Registry write | unchanged; no registry source, aggregate, Markdown, or generator path in changed set | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance MPI-T3 worker dispatch. No public-sync remote, public
commit, public artifact path, public README/catalog claim, or public repository
mutation is authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author |
| Provider or surface | local workspace |
| Session or invocation | MPI-T3 work order authoring, 2026-06-22 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | startup reads, source verification reads, file edits, dispatch gates |
| Target paths | `docs/baselines/CVF_GC018_MPI_T3_EXTERNAL_AGENT_MEMORY_SUMMARY_CONTRACT_2026-06-22.md`; this work order |
| Allowed scope source | operator instruction selecting MPI-T3 work-order authoring |
| Before status evidence | HEAD `a224da57`; clean worktree before dispatch authoring |
| After status evidence | MPI-T3 GC-018/work order authored for work-order review then worker dispatch; uncommitted until dispatcher commit |
| Diff evidence | pre-dispatch gates required before commit |
| Approval boundary | dispatch artifact only; worker implementation remains uncommitted |
| Claim boundary | dispatch packet only; no route edit, helper, registry write, durable write, provider/live, public-sync, or adapter behavior |
| Agent type | dispatcher |
| Invocation ID | `mpi-t3-external-agent-memory-summary-contract-work-order-2026-06-22` |
| Expected manifest | MPI-T3 GC-018 baseline; MPI-T3 work order |
| Actual changed set | checked by dispatch gates before commit |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in dispatch packet |

## Claim Boundary

This work order dispatches only MPI-T3's bounded documentation-only External
Agent Memory Summary Contract reference, a README pointer in the new
`memory_plane` directory, and worker-return evidence. It does not authorize
Memory readout route edits, route schema changes, helper or checker
implementation, registry source or aggregate edits, durable writes, registry
generator changes, provider/live proof, public-sync, actual CLI/MCP adapter
behavior, vector DB, graph persistence, direct interception, queue/daemon,
watcher, readiness, cost optimization, or universal governed-coding control.
