# CVF Agent Work Order - MPI-T4 Federated Memory Read Helper

Memory class: FULL_RECORD

Status: DISPATCHED_TO_WORKER

Date: 2026-06-22

docType: work_order

dispatchBaseHead: 355d4774

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Worker. Reviewer/closer is a separate role.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_MPI_T4_FEDERATED_MEMORY_READ_HELPER_FOR_WORKER_2026-06-22.md`

Current status: `DISPATCHED_TO_WORKER`. MPI-T3 dependency is released by
`docs/reviews/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_SUMMARY_CONTRACT_COMPLETION_2026-06-22.md`
at material commit `c4c53588`, final disposition `CLOSED_PASS_BOUNDED`.
Operator selected MPI-T4 on 2026-06-22. This packet releases MPI-T4 only.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture with `git rev-parse --short HEAD` at worker start.

Current-time notes: MPI-T4 is a bounded helper/test tranche dispatched on
2026-06-22 with MPI-T3 release evidenced by material commit `c4c53588`.

Do-not-misread notes: Do not edit routes, schemas, auth, existing helpers,
foundation files, registry sources or aggregates, durable stores, generated
state, session/handoff files, provider configuration, public-sync, adapters,
or governance checkers.

Required first actions: read this work order, paired GC-018, Required First
Reads, and current source symbols before editing; capture `executionBaseHead`
and initial `git status --short`.

Return contract: return `COMPLETE_PENDING_REVIEW` with only allowed
uncommitted artifacts and exact gate evidence, or `BLOCKED_WITH_REASON` when
the required action exceeds Allowed Scope.

Build one local deterministic helper that federates caller-supplied LPF memory
candidates and caller-supplied parsed scan-registry entries through existing
projection/readout helpers. Do not build or edit a route, load files, write any
source surface, or implement adapter/provider behavior.

Return `COMPLETE_PENDING_REVIEW` with only allowed uncommitted artifacts,
actual `executionBaseHead`, actual `git status --short`, focused test/typecheck
and worker-return gate evidence. If blocked, return `BLOCKED_WITH_REASON`.

The worker return must include `WORKER_EXPERIENCE_RETRO` or the exact
`WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` assertion.

## Purpose

Implement the MPI-T4 federated advisory read fast-path without widening the
Memory Plane runtime boundary. The helper composes existing source-verified
functions; it does not become a source of truth or a public/runtime adapter.

## Agent Roles

| Role | Owner | Boundary |
|---|---|---|
| Dispatch author | Codex | authors and gates GC-018/work order |
| Worker | assigned worker | edits only Allowed Scope and returns uncommitted |
| Reviewer/closer | Codex | validates, repairs reviewer-owned closure artifacts, commits accepted work |
| Operator | human operator | authorizes scope, risk, live/provider/public/adapter/generated expansion |

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-22: continue with MPI-T4 | ACCEPT |
| MPI-T4 GC-018 | `docs/baselines/CVF_GC018_MPI_T4_FEDERATED_MEMORY_READ_HELPER_2026-06-22.md` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V22_2026-06-22.md` | ACCEPT |
| Phase 2 roadmap | `docs/roadmaps/CVF_MPI_PHASE2_EXTERNAL_MEMORY_READ_ROADMAP_2026-06-22.md` | ACCEPT |
| Parent MPI roadmap | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | ACCEPT |
| MPI-T3 contract | `docs/reference/memory_plane/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_SUMMARY_CONTRACT.md` | SUMMARY_ONLY_CONTRACT_AUTHORITY |
| MPI-T2 helper | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/scan-registry-memory-projection.ts` | REGISTRY_PROJECTION_AUTHORITY |
| Memory readout helper | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` | SANITIZATION_AUTHORITY |

## Dependency Release Gate

| Dependency | Release evidence | Current status |
|---|---|---|
| MPI-T3 closure | completion review above; commit `c4c53588`; `CLOSED_PASS_BOUNDED` | RELEASED |
| Operator selection | explicit selection on 2026-06-22 | RELEASED |
| Fresh GC-018 | paired baseline in Authority Chain | RELEASED |
| Source refresh | current source rows below; targets confirmed absent | RELEASED |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher releases packet; worker creates helper/test/worker-return; reviewer/closer validates and commits |
| phase | DISPATCH_COMPLETE; EXECUTION; CLOSURE; SESSION_SYNC_IF_NEEDED |
| baseHeadFor(phase) | `dispatchBaseHead=355d4774`; worker captures `executionBaseHead`; reviewer records `closureBaseHead` |
| changedSetScope(phase) | worker changes only Allowed Scope; reviewer owns closure and continuity surfaces |
| traceScope(phase, actor) | worker trace covers three worker-owned artifacts; reviewer trace covers closure |
| commitOwner(phase) | worker commits nothing; reviewer/closer owns accepted material and later session-sync commits |
| crossBatchIsolation | do not mix MPI-T5/T6, route/schema, existing helper, registry/durable write, provider/live, public-sync, or session work |
| Before status evidence | clean worktree at dispatch start; `git status --short` empty; committed base `355d4774`; MPI-T3 closure at `c4c53588` |
| nextMoveSurfaces | reviewer updates when the MPI-T4 material completion review records an accepted closure commit |
| Closer designation | reviewer/closer is designated closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_MPI_T4_FEDERATED_MEMORY_READ_HELPER_COMPLETION_2026-06-22.md` |
| reviewerOwnedClosurePaths | this work order; paired GC-018; Phase 2 roadmap; worker return; completion review; continuity surfaces only if state changes |
| workerReturnStatus | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| closer | reviewer/closer |

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Selected route | `MULTI_AGENT_MULTI_ROLE` |
| Intake summary | operator selected MPI-T4; MPI-T3 release evidence is completion commit `c4c53588` |
| Scope assessment | R2 bounded local helper plus focused tests |
| Risk sensitivity | no route, filesystem, registry write, durable write, provider/live, or public behavior |
| Intake owner | dispatch author |
| Execution owner | worker |
| Review owner | reviewer/closer |
| Commit mode | `WORKER_MUST_NOT_COMMIT` |
| Escalation condition | `BLOCKED_WITH_REASON` for any necessary action outside Allowed Scope |
| Rationale | compose existing safe projections without opening runtime access |

## Single-Agent Multi-Role Control Block

N/A with reason: this packet selects `MULTI_AGENT_MULTI_ROLE`; worker and
reviewer/closer are separate roles and commit ownership is explicit.

- Role separation ledger: dispatcher authors; worker implements and returns
  uncommitted; reviewer/closer independently owns acceptance and commit.
- Evidence basis: source reads, git diff, focused tests, and machine gates;
  provider memory or chat memory is not evidence.
- Self-review boundary: worker checks are not claimed as independent review.
- Escalation conditions: stop and route to reviewer/closer or operator under the
  Worker Autonomy rule when the required action exceeds Allowed Scope.
- Gate sequence: pre-dispatch; worker pre-implementation/assist and fast return;
  reviewer-fast; pre-closure; pre-push only if separately authorized.

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator selection to CVF-owned work order |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this MPI-T4 work order |
| Disposition | ADAPT as bounded local helper implementation |
| Claim boundary | external/provider memory is not authority; current CVF source controls |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: MPI-T4 composes current Memory Plane helpers and
does not rescan or absorb a legacy source family. MPI-T0/T1/T2 predecessor
coverage remains unchanged.

## Required First Reads

| Required source | Reason |
|---|---|
| this work order and paired GC-018 | exact scope and source facts |
| `docs/roadmaps/CVF_MPI_PHASE2_EXTERNAL_MEMORY_READ_ROADMAP_2026-06-22.md` | MPI-T4 requirements |
| `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | federated fast-path boundary |
| `docs/reference/memory_plane/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_SUMMARY_CONTRACT.md` | summary-only external read boundary |
| `docs/reference/CVF_MPI_T2_SCAN_REGISTRY_EPISODIC_READ_PROJECTION.md` | derived-view boundary |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/scan-registry-memory-projection.ts` | existing registry projection API |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` | existing sanitizer API |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts` | runtime input/result types |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | candidate type |
| RSE-T1 and RSE-T2 addenda | finding and worker-return routing |

## Allowed Scope

The worker may create only:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/federated-memory-read.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/federated-memory-read.test.ts`
- `docs/reviews/CVF_MPI_T4_FEDERATED_MEMORY_READ_HELPER_WORKER_RETURN_2026-06-22.md`

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| new helper and focused test above | worker | create |
| worker-return path above | worker | create |
| GC-018, this work order, roadmap, completion review, continuity files | reviewer/closer | no worker edit |
| every other path | out of worker scope | forbidden |

## Forbidden Scope

The worker must not edit existing route/helper/foundation source, registry
source or aggregate, generator, durable store, session state, active handoff,
root routers, public-sync, provider configuration, dependencies, `.github/**`,
or `governance/compat/*.py`.

The worker must not add automatic file loading, registry/durable writes,
route/schema/auth behavior, CLI/MCP adapters, provider/network calls, external
commands, vector/graph storage, queue/daemon/watcher, direct IDE/shell/git
interception, EDIT/COMMIT automation, readiness, or universal control claims.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| MPI-T4 helper is deterministic, read-only, advisory, and optional | `docs/roadmaps/CVF_MPI_PHASE2_EXTERNAL_MEMORY_READ_ROADMAP_2026-06-22.md` | MPI-T4 Federated Memory Read Helper | `MPI-T4` | MPI Phase 2 roadmap | VALUE_SET | ACCEPT |
| Federated output combines LPF readout summary and registry finding summary | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | MPI-T4 Federated Read Helper Fast-Path | `MPI-T4` | parent MPI roadmap | VALUE_SET | ACCEPT |
| MPI-T3 contract requires summary-only, false safety flags, and no route/write/adapter execution | `docs/reference/memory_plane/CVF_MPI_T3_EXTERNAL_AGENT_MEMORY_SUMMARY_CONTRACT.md` | Inherited Invariants; Forbidden Operations | `rawMemoryReleased`; `canReinject` | MPI-T3 contract | LITERAL_INVARIANT | ACCEPT |
| Readout builder sanitizes selected candidates and fixes false flags | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` | lines 9-23 and 35-62 | `buildMemoryRuntimeReadout` | Memory runtime readout projection | RUNTIME_BEHAVIOR | ACCEPT |
| Scan projection accepts parsed entries/query and returns bounded summary candidates | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/scan-registry-memory-projection.ts` | lines 20-61 and 93-152 | `projectScanRegistryFindings` | scan registry memory projection | RUNTIME_BEHAVIOR | ACCEPT |
| Scan projection option values include deterministic createdAt, auditTrust, and maxResults | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/scan-registry-memory-projection.ts` | lines 54-69 | `ScanRegistryProjectionOptions` | ScanRegistryProjectionOptions | EXISTS | ACCEPT |
| Workflow input contains query and caller-supplied candidates | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts` | lines 31-47 | `MemoryRuntimeWorkflowInput` | MemoryRuntimeWorkflowInput | EXISTS | ACCEPT |
| Candidate fields include summary and optional content | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | lines 17-26 | `MemoryRetrievalCandidate` | MemoryRetrievalCandidate | EXISTS | ACCEPT |
| Existing projection test proves integration through sanitized readout | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/scan-registry-memory-projection.test.ts` | projection through buildMemoryRuntimeReadout | `buildMemoryRuntimeReadout` | Vitest test surface | EXISTS | ACCEPT |
| RSE-T1 routes routine findings without operator interruption | `docs/reference/role_switch_envelope/CVF_RSE_T1_OPERATOR_QUESTION_BOUNDARY_ADDENDUM.md` | Question Classification | `SELF_HANDLE_WITHIN_SCOPE` | RSE-T1 addendum | VALUE_SET | ACCEPT |
| RSE-T2 defines worker-return jurisdiction fields | `docs/reference/role_switch_envelope/CVF_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_ADDENDUM.md` | Worker Return Jurisdiction Block | `operatorActionRequired` | RSE-T2 addendum | VALUE_SET | ACCEPT |

## New Implementation Symbols

| Proposed symbol | Target | Status | Required semantic |
|---|---|---|---|
| `buildFederatedMemoryRead` | new helper | NEW_SOURCE_SYMBOL | compose projection and readout deterministically |
| `FederatedMemoryReadInput` | new helper | NEW_SOURCE_SYMBOL | workflow input, parsed registry entries, projection options |
| `FederatedMemoryReadResult` | new helper | NEW_SOURCE_SYMBOL | advisory readout, source counts, fixed false flags |

Do not place these rows in Source Verification as existing facts. Renaming is
allowed only when exact replacements are recorded in worker-return evidence.

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: runtime symbols and line anchors must be refreshed by worker.

freshRecomputeRequired: YES

unicodePathHandling: literal repo-relative paths with UTF-8-safe readers

extractedTextAuthority: N/A with reason: source is read directly

Prior MPI-T3 closure evidence is reused only for dependency release. Runtime
behavior must be recomputed against current source and focused tests.

## Negative Search And Collision Discipline

Search roots: `docs`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src`.

Search command:
`rg -n -i "federated memory|federated.*read|buildFederatedMemoryRead" docs EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src`

At dispatch, target helper/test paths do not exist and no source symbol named
`buildFederatedMemoryRead` exists. Roadmap references are planning authority,
not implementation collisions.

## Current Runtime Freshness Verification

| Claim | Evidence | Disposition |
|---|---|---|
| Existing readout function and fixed flags remain current | Source Verification rows for `buildMemoryRuntimeReadout` | ACCEPT |
| Existing registry projection remains current | Source Verification row for `projectScanRegistryFindings` | ACCEPT |
| Runtime input/candidate shapes remain current | source rows for `MemoryRuntimeWorkflowInput` and `MemoryRetrievalCandidate` | ACCEPT |
| Target files absent | dispatcher `Test-Path` results are `False` | ACCEPT |
| Route/provider/public behavior | N/A with reason: forbidden and not claimed | N/A_WITH_REASON |

## Helper Contract

The worker must implement a pure orchestration helper that:

1. accepts `MemoryRuntimeWorkflowInput`, optional parsed
   `ScanRegistryEntry[]`, and optional `ScanRegistryProjectionOptions`;
2. projects registry findings with `projectScanRegistryFindings(entries,
   input.query, options)`;
3. combines input candidates plus projected candidates without mutating input;
4. calls `buildMemoryRuntimeReadout` with a copied workflow input and combined
   candidates;
5. returns the sanitized readout plus stable metadata identifying original and
   projected candidate counts and an advisory/degraded disposition;
6. returns `rawMemoryReleased=false` and `canReinject=false` only by preserving
   existing readout invariants;
7. degrades safely when registry entries are absent/malformed and never blocks
   closure merely because registry projection has no usable result;
8. performs no I/O and imports no filesystem, network, route, provider, durable
   store, registry writer, or command-execution module.

## Focused Test Requirements

Tests must prove:

- deterministic output for identical inputs/options;
- input arrays and nested records are not mutated;
- original and matching registry candidates can be selected through readout;
- no returned selected candidate has a `content` field or RAW sentinel;
- `rawMemoryReleased` and `canReinject` remain false;
- empty, missing, and malformed registry input produces advisory/degraded output
  without throwing;
- result counts/attribution match actual candidate composition;
- no file, registry, durable store, route, network, or provider behavior exists.

## Execution Plan

1. Capture `executionBaseHead` and `git status --short`.
2. Read all Required First Reads and refresh named symbols.
3. Create helper and focused test only.
4. Run focused Vitest, TypeScript check, automation assist, and worker-return
   fast gate.
5. Create the worker-return packet with exact evidence.
6. Return `COMPLETE_PENDING_REVIEW` uncommitted or `BLOCKED_WITH_REASON`.

## Pre-Flight Checks

Dispatcher/reviewer runs:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/check_work_order_dispatch_quality.py --base 355d4774 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 355d4774 --head HEAD
python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base 355d4774 --head HEAD --enforce
```

## Required Checks

Worker runs from repository root:

```powershell
git rev-parse --short HEAD
git status --short
npm --prefix EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web exec vitest run src/lib/federated-memory-read.test.ts
npm --prefix EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web run check
python governance/compat/run_agent_automation_assist.py --base <executionBaseHead> --head HEAD --json --enforce
python governance/compat/run_worker_return_fast_gate.py --pytest-target EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/federated-memory-read.test.ts
```

If the fast gate does not accept a Vitest target, run it without
`--pytest-target` and record focused Vitest separately. Do not convert that
tooling mismatch into scope expansion.

## Evidence Requirements

Worker-return evidence must include actual base/status, exact changed manifest,
focused Vitest and TypeScript outputs, automation-assist JSON result,
worker-return fast-gate result, no-input-mutation proof, safety-flag and
forbidden-content assertions, and explicit no-route/no-I/O/no-write/no-provider/
no-public/no-adapter boundaries.

## Worker Autonomy / No-Question Rule

Repair allowed-scope helper, test, packet-shape, source-fidelity, and gate
failures and rerun gates without asking the operator. Classify these as
`SELF_HANDLE_WITHIN_SCOPE`.

Stop with `BLOCKED_WITH_REASON` only if repair requires a forbidden path,
claim/risk expansion, dependency release, route/schema/auth change, existing
helper/foundation edit, generated/session/handoff/public/provider/live/adapter/
durable work, secrets/quota, or destructive action. Route ordinary promotion
candidates to reviewer/closer through the Worker Return Jurisdiction Block.

## Mandatory Gate-Failure Remediation Protocol

Any failed gate caused by an Allowed Scope artifact is mandatory worker
remediation. A failing gate outside Allowed Scope is recorded verbatim and
returned as `BLOCKED_WITH_REASON`; it is not bypassed or hand-labeled PASS.

## Acceptance Criteria

| Criterion | Required evidence |
|---|---|
| Exact allowed artifacts | `git diff --name-status` contains only three worker-owned paths |
| Deterministic federation | focused equality test on repeated calls |
| No mutation | frozen/deep-copy input assertions |
| Summary-only | selected candidates contain no `content` and no RAW sentinel |
| Safety flags | `rawMemoryReleased=false`; `canReinject=false` |
| Advisory degradation | absent/malformed registry input does not throw or block |
| Existing owners reused | helper calls both source-verified functions |
| No I/O or wiring | import/diff inspection and forbidden-path absence |
| Checks pass | focused Vitest, TypeScript, assist, worker-return gates |
| Commit boundary | worker changes remain uncommitted |

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when all criteria pass. Return
`BLOCKED_WITH_REASON` for missing/stale source, ambiguous safety semantics,
out-of-scope gate remediation, or any necessary forbidden action.

## Operator Checkpoint

Human authorization is required before any route/schema/auth change, existing
helper or foundation edit, registry/durable write, generated/session/handoff
edit by worker, provider/live proof, public-sync, adapter behavior, MPI-T5/T6
work, risk/claim expansion, secrets/quota use, or destructive action.

No human authorization is required for allowed-scope helper/test/worker-return
remediation or gate reruns.

## Review Gate

Reviewer rejects or repairs within reviewer-owned closure scope if changed
paths exceed Allowed Scope; source names drift; output can expose `content`;
either safety flag can become true; input is mutated; helper performs I/O,
route wiring, writes, adapter/provider behavior; advisory degradation throws or
blocks; tests/typecheck/gates fail; or worker-return evidence is incomplete.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order control | Disposition |
|---|---|---|
| One federated advisory read | Helper Contract composes LPF and MPI-T2 candidates | ACCEPT |
| Deterministic and read-only | pure orchestration plus determinism/no-mutation tests | ACCEPT |
| No raw content/reinjection | existing sanitizer plus forbidden-field/false-flag tests | ACCEPT |
| Registry remains derived | caller supplies parsed entries; helper performs no registry I/O | ACCEPT |
| Advisory degradation | no-entry/malformed-entry tests and non-blocking result | ACCEPT |
| No route/adapter/provider/live/public expansion | Forbidden Scope and Claim Boundary | ACCEPT |
| Focused tests | Focused Test Requirements and Required Checks | ACCEPT |
| RSE finding routing | Worker Return Jurisdiction Block requirement | ACCEPT |

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| Foundation storage class | no storage; derived local advisory helper |
| New durable storage | none |
| Generated aggregate impact | none |
| Source layout | one new helper beside existing readout/projection helpers; one colocated test |
| Index/front-door updates | none during worker execution |
| Layout boundary | no existing source edit, route edit, store, registry source, or generator |

## Governed File Maintainability Plan

The two target files are new and must remain focused modules. Existing owner
files are not near-threshold targets for this tranche and are not edited. If a
target would approach a governed hard threshold, return `BLOCKED_WITH_REASON`
instead of growing or splitting outside Allowed Scope.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | MPI-T4 local helper execution in focused tests |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: local helper behavior must be proven by focused tests only |
| receiptEvidence | N/A with reason: no Delta receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT in worker focused tests; dispatch has N/A with reason while worker return is absent |
| claimLanguage | MPI-T4 local read-only helper dispatch only |
| forbiddenExpansion | route/schema/auth changes, automatic source loading, registry/durable writes, CLI/MCP adapter, provider/live, public-sync, wrapper/proxy enforcement, direct interception, arbitrary commands, EDIT/COMMIT execution, queue/daemon, watcher, readiness, full-hook equivalence, and universal control remain out of scope |
| invocationBoundary | direct library invocation only |
| interceptionBoundary | no IDE/shell/git/filesystem/provider/route interception |

## Corpus Completeness And Report Integrity

- Corpus task class: bounded source implementation.
- Corpus root: Required First Reads plus two new source/test targets.
- Snapshot time: 2026-06-22T00:00:00+07:00
- Enumeration command: `rg --files --hidden --no-ignore docs EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src`
- Manifest artifact or inline manifest: inline Source Verification Block above
  plus exact worker changed manifest.
- Manifest hash: NOT_APPLICABLE_WITH_REASON - no corpus manifest hash is
  created.
- Processing ledger artifact or inline ledger: inline Source Verification Block.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED,
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=inline Source Verification Block; ledger_terminal=READ for named source rows; exclusions=declared below; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: broad corpus scan, registry source/aggregate, route,
  durable store, provider/live, public-sync, adapter, MPI-T5/T6.
- Unreadable or unsupported files: 0.
- Aggregation check: NOT_APPLICABLE_WITH_REASON - no aggregate changed.
- Drift check: NOT_APPLICABLE_WITH_REASON - no generated aggregate changed.
- Output traceability: Allowed Scope, Source Verification Block, and focused
  tests.
- Adversarial verification: reviewer/closer must run reviewer-fast or stricter
  gate before acceptance.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Worker Return Packet Shape Contract

The worker-return must contain:

| Required item | Required value |
|---|---|
| Status | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| executionBaseHead | actual start HEAD |
| git status --short | actual post-edit output |
| Purpose | purpose section |
| Scope / Methodology | exact execution method |
| Findings / Position | result and disposition |
| Risk / Corrective Action | residual risk and remediation |
| Changed Files | exact manifest |
| Gate Evidence | exact required check results |
| Worker Return Jurisdiction Block | present for findings, or exact RSE N/A line |
| Claim Boundary | no forbidden expansion |
| Agent Operation Trace Block | worker trace |
| Delta Execution Claim Boundary Control Block | local helper-only boundaries |
| Public Export Disposition | `DEFERRED_PRIVATE_ONLY` |
| WORKER_EXPERIENCE_RETRO | structured block or exact N/A assertion |

| Conditional gate term | Required disposition |
|---|---|
| External Knowledge Intake Routing | section or `N/A with reason` |
| Rescan Intelligence Hardening | section or `N/A with reason` |
| Corpus Completeness And Report Integrity | section or `N/A with reason` |
| Finding-To-Governance Learning Disposition | section or `N/A with reason` |
| Epistemic Process Block | section or `N/A with reason` |
| Machine Closure Package | section or `N/A with reason` |

## Open Artifact Evidence Finality

Worker evidence remains open while the uncommitted return is unreviewed. The
worker must not describe absent completion review, closure commit, or session
sync as complete. Reviewer/closer supplies committed closure evidence.

## Work-Order Fulfillment Manifest

The worker fulfills the proof manifest only with the exact three Allowed Scope
paths, actual command outputs, and actual git evidence. No inferred or
chat-memory evidence substitutes for a source file or command result.

## Self-Reported Gate Evidence Consistency

Any claimed PASS must match the recorded command exit/result. A skipped or
unavailable check is `N/A with reason` only when this packet allows it;
otherwise return `BLOCKED_WITH_REASON`.

## Dispatch Packet Learning Disposition

The prior reviewer finding that evidence packets can pass syntax while lacking
source fidelity is absorbed here: all existing source facts cite current files
and bare symbols; proposed helper symbols are separated from Source
Verification. Repeated drift must be routed as a governance-learning finding.

## ACCEPT_AS_OWNER_MAP coverage

N/A with reason: this is not a corpus owner-map or connector-spec intake. The
Authority Chain explicitly names every current owner surface consumed.

## Closure Checklist

Reviewer/closer must resolve: exact deliverables; exact scope diff; focused
tests/typecheck/gates; deterministic/no-mutation proof; summary-only and false
flags; advisory degradation; no I/O/write/route/adapter/provider/public scope;
worker-return shape; commit ownership; closure diff gate; and continuity sync
if current mode changes. Each item must be PASS, `N/A with reason`, or BLOCKED.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | target closure status `CLOSED_PASS_BOUNDED` in reviewer-owned completion review path `docs/reviews/CVF_MPI_T4_FEDERATED_MEMORY_READ_HELPER_COMPLETION_2026-06-22.md` | N/A with reason: dispatch packet awaits worker return |
| Completion or reviewer artifact | `docs/reviews/CVF_MPI_T4_FEDERATED_MEMORY_READ_HELPER_COMPLETION_2026-06-22.md` | completion review status and closure commit recorded by reviewer/closer | N/A with reason: reviewer artifact is created during reviewer-owned closure |
| Roadmap state | `docs/roadmaps/CVF_MPI_PHASE2_EXTERNAL_MEMORY_READ_ROADMAP_2026-06-22.md` | current top status and Machine Closure Package row match | PASS |
| Registry JSON | N/A | no registry JSON changes authorized; verify unchanged with `git diff --name-status` before closure | PASS |
| Registry Markdown | N/A | no registry Markdown changes authorized; verify unchanged with `git diff --name-status` before closure | PASS |
| External evidence digest | this work order and paired GC-018 | External Knowledge Intake Routing present; chain map sha256=09CD47C35F9A271748B8D51CC4C682426C74E9E2D4C2B211C5C189A7E66F98D7 | PASS |
| System loop interlock | this work order | no system loop, wrapper, proxy, queue, daemon, watcher, or universal-control expansion | PASS |
| GC-018 | paired baseline | target closure status `CLOSED_PASS_BOUNDED` in reviewer-owned completion review | N/A with reason: awaits worker return |
| Worker return | `docs/reviews/CVF_MPI_T4_FEDERATED_MEMORY_READ_HELPER_WORKER_RETURN_2026-06-22.md` | `Status: ACCEPTED_BY_REVIEWER` | N/A with reason: awaits worker return |
| Runtime helper/tests | two worker source paths | committed diff plus focused checks | N/A with reason: awaits worker return |
| Session continuity | reviewer-owned later phase | current mode/next move aligned | N/A with reason: session update occurs during material closure |

## Acceptance Receipt Assertion Matrix

| Receipt/query item | Required value | Observed value | Status |
|---|---|---|---|
| Receipt behavior | no receipt/query acceptance behavior in MPI-T4 dispatch | no receipt/query behavior is authorized or claimed | N/A with reason: helper dispatch has no receipt/query surface |
| Query handling | caller-supplied `input.query` only | helper contract routes query only to existing registry projection/readout helpers | PASS |
| Closure acceptance | reviewer-owned worker-return acceptance | worker must return `COMPLETE_PENDING_REVIEW`; reviewer supplies completion review | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance MPI-T4 dispatch; no public repository artifact or
claim is authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author |
| Provider or surface | local workspace |
| Session or invocation | MPI-T4 work-order authoring, 2026-06-22 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | startup/source reads, patching, dispatch gates |
| Target paths | paired GC-018, this work order, Phase 2 roadmap status |
| Allowed scope source | operator instruction selecting MPI-T4 |
| Before status evidence | clean worktree at dispatch start; `git status --short` empty; HEAD `355d4774` |
| After status evidence | dispatch artifacts only; worker implementation absent |
| Diff evidence | pre-dispatch and steward gates before commit |
| Approval boundary | dispatch only; no worker commit |
| Claim boundary | local helper packet only |
| Agent type | dispatcher |
| Invocation ID | `mpi-t4-federated-memory-read-helper-dispatch-2026-06-22` |
| Expected manifest | GC-018, work order, Phase 2 roadmap |
| Actual changed set | verified before dispatch commit |
| Manifest delta | MATCH required |
| Deletion or rename disposition | N/A with reason: none planned |

## Claim Boundary

This work order authorizes only one new local read-only helper, one focused test
file, and one uncommitted worker return. It does not authorize any route,
schema, auth, existing helper/foundation edit, automatic source loading,
registry/durable write, generator, CLI/MCP adapter, external command,
vector/graph store, provider/live proof, public sync, session edit by worker,
readiness, or universal governance-control claim.
