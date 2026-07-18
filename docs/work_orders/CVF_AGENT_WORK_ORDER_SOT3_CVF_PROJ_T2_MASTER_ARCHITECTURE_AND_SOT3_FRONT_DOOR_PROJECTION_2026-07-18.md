# CVF Agent Work Order - SOT3 CVF Master Architecture And Front Door Projection

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-07-18

Batch ID: SOT3-CVF-PROJ-T2

Dispatch base head: `1820bdff9`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated Claude worker

Reviewer/closer: independent reviewer/closer

Worker return path: `docs/reviews/CVF_SOT3_CVF_PROJ_T2_WORKER_RETURN_2026-07-18.md`

## Dispatch Prompt Envelope

Role: delegated documentation/architecture worker for `SOT3-CVF-PROJ-T2`.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_CVF_PROJ_T2_MASTER_ARCHITECTURE_AND_SOT3_FRONT_DOOR_PROJECTION_2026-07-18.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture committed dispatch/session-sync HEAD at start.

Current-time notes: T1 is accepted at material commit `11bfd46a0`; T2 is the
only released implementation tranche.

Do-not-misread notes: do not edit the frozen whitepaper or version-bounded
diagram set, runtime, tests, provider registry, catalog, GAP, Web, session,
public-sync, Git state, or production surfaces.

Required first actions: perform mandatory startup acknowledgment; read guard
orientation, literal gotchas, this packet, paired baseline, T0 ledger, T1
completion, every source below, and applicable checkers before writing.

Return contract: leave all changes unstaged and uncommitted with unchanged
HEAD; return exactly `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Create a coherent CVF architecture projection of the accepted SOT3 lifecycle
and proof ladder across current architecture front doors while preserving
historical snapshot boundaries and bounded claims.

## Authority Chain

`AGENTS.md` and active session state; paired GC-018; SOT3-CVF roadmap; accepted
T0 ledger and T1 completion; current source and accepted SOT3 reviews; this
work order for exact worker scope.

## Agent Roles

Dispatcher commits packet; worker edits without commit; independent
reviewer/closer recomputes and owns material closure; session-sync steward
updates protected continuity separately.

## Scope / Target / Owner Boundary

### Allowed worker paths

1. `ARCHITECTURE.md`
2. `CVF_ECOSYSTEM_ARCHITECTURE.md`
3. `docs/CVF_ARCHITECTURE_DECISIONS.md`
4. `docs/reference/CVF_ARCHITECTURE_MAP.md`
5. `docs/reference/sot_three_layer/README.md`
6. `docs/reviews/CVF_SOT3_CVF_PROJ_T2_WORKER_RETURN_2026-07-18.md`

The SOT3 README is conditional: use `NO_CHANGE_WITH_REASON` in the worker
return if T1 content already aligns; do not edit it merely to consume scope.

### Mandatory read-only/defer paths

- `docs/reference/CVF_MASTER_ARCHITECTURE_WHITEPAPER.md`
- `docs/reference/CVF_ARCHITECTURE_DIAGRAMS.md`

### Forbidden scope

All other paths, including runtime/tests, catalog/GAP/schema/checkers, provider
registry, Web/UI, roadmap/baseline/work order, completion review, registry,
session/handoff/state, public-sync, commit/tag/push/PR, provider/live, and
production action.

## Write Ownership

| Surface | Worker | Reviewer |
|---|---|---|
| five conditional architecture/reference targets | update only when required; uncommitted | independently verify and repair inside scope |
| worker return | create uncommitted | accept/repair evidence |
| two defer files | read only | verify unchanged |
| closure/session surfaces | forbidden | reviewer/session steward only |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| T0 exact routing | accepted T0 ledger rows 2-7 | ACCEPT |
| T1 closure | `docs/reviews/CVF_SOT3_CVF_PROJ_T1_COMPLETION_REVIEW_2026-07-18.md`; material commit `11bfd46a0` | ACCEPT |
| current dispatch base | clean session-sync commit `1820bdff9` | ACCEPT |
| operator continuation | standing sequential roadmap instruction | ACCEPT |

## Required First Reads

Read startup front doors, active handoff, guard orientation, literal gotchas,
paired baseline/work order, T0 ledger, T1 completion, all target/defer files,
SOT3 contract/activation/application evidence, runtime owners, provider
registry acknowledgment, and checker sources listed below.

## Pre-Flight Checks

Confirm clean worktree, capture HEAD, match dispatcher-supplied execution base,
run pre-implementation autorun on the dispatch range, hash the two read-only
defer files, and stop on foreign changes or source contradiction.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| root architecture missing SOT3 | LITERAL_INVARIANT | canonical-contract marker: `ARCHITECTURE.md` | sections 1-8 | `ARCHITECTURE.md` | architecture front door | ACCEPT |
| ecosystem tree missing packages | LITERAL_INVARIANT | canonical-contract marker: `CVF_ECOSYSTEM_ARCHITECTURE.md` | Section 2 | `MASTER TREEVIEW` | ecosystem blueprint | ACCEPT |
| ADR log missing SOT3 decision | LITERAL_INVARIANT | `docs/CVF_ARCHITECTURE_DECISIONS.md` | current ADR sequence | `ADR-011` through `ADR-052` | ADR log | ACCEPT |
| map missing SOT3 | LITERAL_INVARIANT | `docs/reference/CVF_ARCHITECTURE_MAP.md` | Layer Architecture | `Layer Architecture` | architecture map | ACCEPT |
| whitepaper frozen | VALUE_SET | `docs/reference/CVF_MASTER_ARCHITECTURE_WHITEPAPER.md` | top matter declares Version `3.7-W46T1` and active tranche `NONE` | `Version` | master whitepaper | ACCEPT |
| diagrams version-bounded | VALUE_SET | `docs/reference/CVF_ARCHITECTURE_DIAGRAMS.md` | scope line declares v1.0 through v1.7.2 | `document scope line` | diagram set | ACCEPT |
| composition owner | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_SOT_THREE_LAYER_SLICE/src/orchestrator.ts` | imports and line 52 | `runThreeLayerScenario` | vertical slice | ACCEPT |
| activation closure | VALUE_SET | `docs/roadmaps/CVF_SOT3_ACTIVATION_AND_OPERATIONAL_PROOF_ROADMAP_2026-07-13.md` | top status | `LIVE_GOVERNANCE_PROVEN_BOUNDED` | activation roadmap | ACCEPT |
| downstream proof | VALUE_SET | `docs/reviews/CVF_SOT3_APP_T5_COMPLETION_REVIEW_2026-07-18.md` | evidence row | `SOT3_APP_T5_LIVE_PROOF_PASS` | application review | ACCEPT |
| provider registry exists | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | line 30 class declaration | `ProviderRegistry` | Model Gateway | ACCEPT |

## New Doc-Only Fields

New ADR identifier/title and diagram labels are doc-only. They must not be
represented as pre-existing runtime symbols.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap/T0 requirement | Output | Verification | Status |
|---|---|---|---|
| root architecture pointer | `ARCHITECTURE.md` | lifecycle/proof-ladder review | PASS |
| master tree placement | ecosystem architecture | exact four-package tree entries | PASS |
| architecture decision | ADR log | decision/boundary/related-file review | PASS |
| canonical map | architecture map | layers and arrows agree | PASS |
| SOT3 front door alignment | SOT3 README or no-change reason | cross-surface comparison | PASS |
| frozen/version-bound defer | two read-only files | hashes and no diff | PASS |
| no scope expansion | worker return | Git status/diff | PASS |

## Required Implementation

1. Add a compact SOT3 architecture path to `ARCHITECTURE.md`, showing source
   intake -> Refinery -> Truth Kernel -> Truth Flow -> governed context ->
   governed execution -> review/freeze -> impact/recall. Distinguish knowledge
   authority from provider output and downstream content.
2. Add the four actual package roots to the ecosystem Section 2 treeview with
   concise roles and no invented paths.
3. Add one next available ADR after the current sequence. Record contract,
   owner, activation, application, bounded proof, and rejected overclaims;
   cite canonical paths.
4. Add the SOT3 family to the architecture map using existing layer vocabulary
   or an explicitly bounded cross-plane overlay. Do not silently redefine the
   frozen L0-L6 doctrine.
5. Compare the T1 SOT3 README with all four updates. Edit only to repair a real
   mismatch; otherwise document `NO_CHANGE_WITH_REASON` in the worker return.
6. Preserve the whitepaper and diagram set byte-for-byte and record their
   defer reasons from the T0 ledger.

## Architecture Claim Contract

- Refinery prepares deterministic source-bound material; no truth authority.
- Truth Kernel alone owns decision, receipt, and truth reference.
- Truth Flow manages post-Kernel distribution/lifecycle without recreating
  upstream authority.
- Provider output is downstream content, not truth authority.
- Activation and application proofs are bounded, not universal or production.
- The separate Model Gateway provider registry exists and is unchanged.

## Execution Plan

Capture base/hashes; reread sources; edit four required surfaces; conditionally
reconcile SOT3 README; verify diagrams/text/links and frozen hashes; create
checker-safe return; run gates; leave unstaged with unchanged HEAD.

## Evidence Requirements

Worker return must include startup/base evidence, exact changed set, each
source confirmation, cross-surface role/proof matrix, defer-file before/after
hash equality, link/path checks, Mermaid structural evidence where edited,
worker-fast and file-size results, unstaged/cached/status diffs, final HEAD,
no-commit statement, and terminal token.

## Planned Worker Fulfillment Manifest

| Artifact | Action |
|---|---|
| four architecture surfaces | bounded updates |
| SOT3 README | conditional update or terminal no-change reason |
| T2 worker return | create full evidence packet |

## Acceptance Criteria

Exact allowed-path set; four required architecture updates; conditional SOT3
front-door decision; two defer files unchanged; consistent roles, arrows, and
proof ladder; no universal/provider/public/production overclaim; all gates
PASS; nothing staged/committed; HEAD unchanged.

## Review Gate

Reviewer independently rereads sources, compares all architecture projections,
checks ADR numbering and layer/doctrine boundaries, validates defer hashes,
reruns gates, and owns closure/material commit.

## Closure Checklist

- [x] T1 closure commit explicitly releases T2.
- [x] Six ledger rows are mapped, including two read-only defers.
- [x] Exact allowed and forbidden scope is stated.
- [x] Source facts and provider-registry existence are verified.
- [x] Worker no-commit and reviewer ownership are explicit.
- [x] T3-T4 and public-sync remain parked.

## Stop Conditions

Stop for dirty/foreign worktree, base mismatch, source contradiction, ADR
collision, needed forbidden path, frozen-file mutation, unresolved checker
failure outside scope, or need for provider/live/public/production action.

## Return-To-Orchestrator Conditions

Return blocker, source/command, observed state, affected criterion, and narrow
next action. Do not guess paths, fields, or architecture ownership.

## Worker Autonomy / No-Question Rule

Repair in-scope defects directly. Ask no preference questions. Escalate only
for a stop condition or required scope expansion.

## Operator Checkpoint

None during T2 execution. Independent reviewer acceptance is required before
T3 packet authoring. Public-sync remains parked.

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| intake summary | project accepted SOT3 architecture and proof boundaries into current CVF master architecture surfaces |
| scope | private documentation/architecture projection |
| route | `MULTI_AGENT_MULTI_ROLE` |
| selected role route | dispatcher, no-commit worker, independent reviewer/closer, separate session-sync steward |
| worker | exact allowed paths, no commit |
| reviewer | independent closure owner |
| risk sensitivity | documentation-only; runtime, provider/live, public, production, and push are prohibited |
| public route | `DEFERRED_PRIVATE_ONLY` |
| escalation | source contradiction, foreign change, or scope expansion |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`architecture-design`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class architecture-design --role worker --lifecycle-phase pre-implementation --surface-selector architecture --risk-ceiling HIGH --max-results 20 --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | standing guards remain binding |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher commits packet; worker edits without commit; reviewer/closer commits acceptance; session steward syncs continuity |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE, SESSION_SYNC |
| baseHeadFor(phase) | dispatchBaseHead=`1820bdff9`; executionBaseHead=worker captures committed dispatch HEAD; closureBaseHead=reviewer sets |
| changedSetScope(phase) | dispatch roadmap/baseline/work order; execution six allowed paths; closure reviewer packet and accepted outputs; session protected paths only |
| traceScope(phase, actor) | each actor records commands, paths, diff, base, and boundary evidence |
| commitOwner(phase) | dispatcher, then reviewer/closer, then session steward; worker forbidden |
| crossBatchIsolation | Before status evidence: clean worktree at dispatch HEAD `1820bdff9`; worker must also start clean and foreign change blocks execution |
| nextMoveSurfaces | worker forbidden; reviewer/session steward update only with accepted material evidence |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_SOT3_CVF_PROJ_T2_COMPLETION_REVIEW_2026-07-18.md` |
| reviewerOwnedClosurePaths | completion review, roadmap, paired baseline/work order, accepted return, separate session sync |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_SOT3_CVF_PROJ_T2_WORKER_RETURN_2026-07-18.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 1820bdff9 --head HEAD
rg -n "CVF_REFINERY|CVF_TRUTH_KERNEL|CVF_TRUTH_FLOW|CVF_SOT_THREE_LAYER_SLICE" CVF_ECOSYSTEM_ARCHITECTURE.md
rg -n "Refinery|Truth Kernel|Truth Flow|SOT3" ARCHITECTURE.md docs/CVF_ARCHITECTURE_DECISIONS.md docs/reference/CVF_ARCHITECTURE_MAP.md docs/reference/sot_three_layer/README.md
git diff --exit-code -- docs/reference/CVF_MASTER_ARCHITECTURE_WHITEPAPER.md docs/reference/CVF_ARCHITECTURE_DIAGRAMS.md
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_governed_file_size.py --enforce
git diff --name-status
git diff --cached --name-status
git status --short
git rev-parse --short HEAD
```

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Status; Dispatch Prompt Envelope; Scope / Target / Owner Boundary; Dependency Release Evidence; Source Verification Block; New Doc-Only Fields; Roadmap-To-Work-Order Trace Matrix; Required Implementation; Evidence Requirements; Acceptance Criteria; Review Gate; Closure Checklist; Stop Conditions; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Worker Return Packet Shape Contract; Public Export Disposition; Claim Boundary |
| gateRunPurpose | dispatch confirmation after checker/source read-ahead |
| claimBoundary | structural packet evidence only; semantic acceptance remains reviewer-owned |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id SOT3-CVF-PROJ-T2 --title "SOT3 CVF Master Architecture And Front Door Projection" --date 2026-07-18 --base 1820bdff9 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact source, scope, defer, evidence, handoff, and return contracts added |
| checkerReadAheadConfirmation | checker paths listed above |
| docOnlyNewFields | ADR identifier and architecture labels only |
| claimBoundary | dispatch-authoring provenance only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | private provenance workspace |
| Session or invocation | SOT3-CVF-PROJ-T2 dispatch, 2026-07-18 |
| Working directory | repository root |
| Command or tool surface | source reads, `rg`, patch, governance gates |
| Target paths | roadmap, paired T2 baseline and work order |
| Allowed scope source | roadmap sequence plus operator standing instruction |
| Before status evidence | clean worktree at HEAD `1820bdff9`; T1 closed at `11bfd46a0` |
| After status evidence | exact three-path dispatch pending commit |
| Diff evidence | Git diff before commit |
| Approval boundary | T2 documentation dispatch only |
| Claim boundary | no runtime, provider/live, public, production, push, or session mutation |
| Agent type | dispatcher |
| Invocation ID | `sot3-cvf-proj-t2-dispatch-2026-07-18` |
| Expected manifest | roadmap, T2 baseline, T2 work order |
| Actual changed set | exact three paths before commit |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | architecture documentation and navigation projection |
| claimDisposition | N/A with reason: no execution-control or runtime-enforcement implementation |
| receiptEvidence | N/A with reason: accepted receipts are cited, not recreated |
| actionEvidence | N/A with reason: documentation edits are not runtime actions |
| invocationBoundary | exact T2 packet and six worker paths |
| interceptionBoundary | no wrapper, provider, IDE, shell, or agent-action interception claim |
| claimLanguage | document, map, cite, align, and defer only |
| forbiddenExpansion | runtime/test/catalog/GAP/provider/live/Web/public/push/production/session changes and universal SOT3 claims |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | paired T2 baseline | `Status: DISPATCH_READY` | PASS |
| Work order status | this work order | `Status: DISPATCH_READY` | PASS |
| Completion or reviewer artifact | T2 completion review | reviewer-owned | N/A with reason |
| Worker return | T2 worker return | worker-owned uncommitted | N/A with reason |
| Roadmap state | SOT3-CVF projection roadmap | `Status: SOT3_CVF_PROJ_T2_DISPATCH_READY` | PASS |
| Registry JSON | existing GC-051 coverage | reviewer verifies coverage | N/A with reason |
| Registry Markdown | existing registry front door | no mutation authorized | N/A with reason |
| External evidence digest | repository-local evidence only | none | N/A with reason |
| System loop interlock | no loop owner changed | none | N/A with reason |
| Session continuity | protected surfaces | separate sync | N/A with reason |

## Current Runtime Freshness Verification

The current SOT3 source owners and bounded proofs were directly verified. The
existing `PROVIDER_CAPABILITY_REGISTRY` in Model Gateway is acknowledged and
unchanged; no provider absence or hardcoding claim is made.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private-provenance architecture projection; GitHub publication is a
later separately authorized public-sync batch.

## Claim Boundary

Exactly six conditional worker paths, documentation only. No runtime, test,
provider/live, Web, catalog/GAP, public, production, session, commit, or push
authority. Completion remains pending independent review.
