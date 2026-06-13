# CVF Agent Work Order - Model Gateway Legacy Absorption Coverage Index For Claude - 2026-06-13

Memory class: FULL_RECORD

Status: DISPATCH_READY

Owner: Codex Orchestrator

Worker target: Claude

Commit mode: WORKER_MUST_NOT_COMMIT

rawMemoryReleased=false

Base head: 86d9e46d

dispatchBaseHead: `86d9e46d`

executionBaseHead: `86d9e46d`

closureBaseHead: `86d9e46d`

completionReviewPath:
`docs/reviews/CVF_MODEL_GATEWAY_LEGACY_ABSORPTION_COVERAGE_INDEX_COMPLETION_2026-06-13.md`

reviewerOwnedClosurePaths:

- `docs/reviews/CVF_MODEL_GATEWAY_LEGACY_ABSORPTION_COVERAGE_INDEX_COMPLETION_2026-06-13.md`

## Purpose

Claude is assigned a bounded legacy absorption recheck for Model Gateway and a
coverage-index update pass.

Primary deliverables:

1. Update:
   `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md`
2. Create:
   `docs/reference/CVF_MODEL_GATEWAY_LEGACY_ABSORPTION_RECHECK_PLAN_2026-06-13.md`
3. Create worker return:
   `docs/reviews/CVF_MODEL_GATEWAY_LEGACY_ABSORPTION_COVERAGE_INDEX_WORKER_RETURN_2026-06-13.md`

Claude must not commit.

## Scope / Target / Owner Boundary

Target: `MGW-001` in the legacy absorption coverage index, plus evidence-only
reconciliation rows for `MEM-001`, `SCAN-001`, `FPC-001`, `AOT-001`, and
`SLI-001` when source evidence supports updates.

Owner: Codex owns dispatch, review, final commit, completion review, and
session sync. Claude owns the uncommitted worker deliverables only.

Boundary: documentation and index update only; no runtime/source/test mutation,
provider/API call, public-sync, production readiness, public readiness, cost
claim, quality claim, or broad legacy absorption outside the named scope.

## Agent Roles

| Role | Agent | Responsibility |
| --- | --- | --- |
| Orchestrator | Codex | Dispatch, scope control, reviewer-owned closure |
| Worker | Claude | Bounded legacy recheck and uncommitted deliverables |
| Reviewer | Codex | Review, allowed repair, commit, completion review, session sync |
| Operator | Human | Strategic authorization and any scope expansion decision |

## Intake Role Routing Decision

Intake summary: operator identified a likely legacy-coverage blind spot in
Model Gateway planning and requested a durable index so future plane/workflow
upgrades can prove legacy coverage before proceeding.

Scope classification: documentation-only legacy absorption recheck and
coverage-index update; no runtime/source/test/provider/public mutation.

Risk sensitivity: medium governance risk because the worker may read bounded
legacy architecture content and may influence whether C-02 planning resumes;
runtime and provider risk remains forbidden.

Selected role route: Claude worker produces uncommitted artifacts; Codex
reviewer owns closure conversion, final commit, and session sync.

Canonical route mode: `MULTI_AGENT_MULTI_ROLE`.

Escalation condition: return to orchestrator if the needed evidence requires
legacy families outside the allowed gateway scope, runtime/provider/live work,
protected session-state mutation, public-sync, destructive actions, or operator
scope expansion.

## Required First Reads

1. `docs/baselines/CVF_GC018_MODEL_GATEWAY_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md`
2. `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md`
3. `docs/reviews/CVF_MODEL_GATEWAY_LEGACY_ABSORPTION_GAP_DISPATCH_CORRECTION_2026-06-13.md`
4. `docs/reference/archive/CVF_LHW17_T2_MODEL_GATEWAY_UNIFICATION_ADVISORY_CONNECTOR_SPEC_2026-05-30.md`
5. `docs/baselines/archive/CVF_GC018_LHW17_CVF_IMPORTANT_ABSORPTION_WAVE_2026-05-30.md`
6. `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md`
7. `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md`
8. `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md`
9. `docs/audits/CVF_MEMORY_METHOD_LEGACY_RESCAN_AUDIT_2026-06-01.md`

## Pre-Flight Checks

Claude must record:

```text
git status --short
git rev-parse --short HEAD
rg --files --hidden --no-ignore ".private_reference/legacy/CVF_Important/ADDING_MODEL GATEWAY"
rg --files --hidden --no-ignore ".private_reference/legacy/CVF_Important/ADDING_MODEL_ROUTER"
rg --files --hidden --no-ignore ".private_reference/legacy/CVF_Important/ADDING_MINI_MODEL GATEWAY"
rg --files --hidden --no-ignore ".private_reference/legacy/CVF_Important/ADDING_AI GATEWAY"
```

If `rg` is unavailable, use an ignore-proof filesystem enumeration and record
the replacement command.

## Write Ownership

Claude may write only:

- `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md`
- `docs/reference/CVF_MODEL_GATEWAY_LEGACY_ABSORPTION_RECHECK_PLAN_2026-06-13.md`
- `docs/reviews/CVF_MODEL_GATEWAY_LEGACY_ABSORPTION_COVERAGE_INDEX_WORKER_RETURN_2026-06-13.md`

Codex owns:

- `docs/reviews/CVF_MODEL_GATEWAY_LEGACY_ABSORPTION_COVERAGE_INDEX_COMPLETION_2026-06-13.md`
- any session-state or handoff sync;
- final commit.

## Worker Autonomy / No-Question Rule

Claude must repair allowed-scope gate failures and missing required sections
without asking the operator. Claude must stop and return
`BLOCKED_RETURN_TO_ORCHESTRATOR` only if the needed repair would exceed allowed
scope, authorize runtime/provider/public work, mutate protected session state,
or require a new legacy family outside this work order.

## Reviewer Closure Conversion Block

Because this is `WORKER_MUST_NOT_COMMIT`, Claude must return uncommitted
deliverables. Codex will review the worker return, perform allowed repairs if
needed, create the completion review at `completionReviewPath`, run closure
gates on the committed range, commit, and sync session state.

## 1. Authority Chain

| Authority | Path | Role |
| --- | --- | --- |
| GC-018 baseline | `docs/baselines/CVF_GC018_MODEL_GATEWAY_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` | dispatch authority |
| Active hold correction | `docs/reviews/CVF_MODEL_GATEWAY_LEGACY_ABSORPTION_GAP_DISPATCH_CORRECTION_2026-06-13.md` | reason C-02 is held |
| Coverage index | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` | index to update |
| Prior Model Gateway advisory | `docs/reference/archive/CVF_LHW17_T2_MODEL_GATEWAY_UNIFICATION_ADVISORY_CONNECTOR_SPEC_2026-05-30.md` | prior absorption evidence |
| Legacy blind-spot standard | `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md` | mandatory absorption control |
| Corpus registry standard | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` | duplicate-prevention registry rules |

## 2. Objective

Resolve whether C-02 Model Gateway EPF provider-routing boundary planning can
resume after legacy absorption recheck.

Claude must answer:

1. Which gateway-related legacy files were already absorbed by LHW17 T2?
2. Which gateway-related legacy files exist now but were not covered by LHW17
   T2?
3. Which accepted values map to current Model Gateway / EPF owner surfaces?
4. Which values must be deferred, rejected, or sent to a later implementation
   tranche?
5. What update is required to `MGW-001` in the coverage index?
6. Do `MEM-001` and `SCAN-001` need only evidence reconciliation, or is a
   later separate GC-018 needed?

## 3. Allowed Scope

Allowed legacy content reading:

- `.private_reference/legacy/CVF_Important/ADDING_MODEL GATEWAY/`
- `.private_reference/legacy/CVF_Important/ADDING_MODEL_ROUTER/`
- `.private_reference/legacy/CVF_Important/ADDING_MINI_MODEL GATEWAY/`
- `.private_reference/legacy/CVF_Important/ADDING_AI GATEWAY/`
- gateway-related files in `.private_reference/legacy/CVF_Important/REVIEW FOLDER/`
  only when cited by LHW17 T2, the C-02 correction, or a gateway-family file.

Allowed governed-source reading:

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/`
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/`
- FPC-T1 through FPC-T4 packets;
- AOT-T1/T2 packets only for index coverage status;
- MEMCON, MLW0, CI1-T11, and corpus registry entries only for index evidence
  reconciliation.

Allowed writes:

- `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md`
- `docs/reference/CVF_MODEL_GATEWAY_LEGACY_ABSORPTION_RECHECK_PLAN_2026-06-13.md`
- `docs/reviews/CVF_MODEL_GATEWAY_LEGACY_ABSORPTION_COVERAGE_INDEX_WORKER_RETURN_2026-06-13.md`

## 4. Forbidden Scope

Do not:

- commit;
- mutate runtime/source/test files;
- call providers or run live proof;
- add providers, models, package dependencies, routes, registries, or public
  surfaces;
- inspect secrets or print secret values;
- use public-sync;
- inspect or mutate external Document Translator, Policy_Local, EC, OCR,
  retrieval, Redis, DEP2, or T12 surfaces;
- broaden memory/scan legacy reading beyond governed evidence reconciliation;
- claim production readiness, public readiness, cost improvement, quality
  improvement, or provider behavior.

## 5. Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS: dispatch baseline is ready | `docs/baselines/CVF_GC018_MODEL_GATEWAY_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` | header | `Status` | GC-018 baseline | ACCEPT |
| EXISTS: coverage index row `MGW-001` is active blocking row | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` | `## Initial Coverage Ledger` | `MGW-001` | coverage index | ACCEPT |
| EXISTS: C-02 is held pending legacy absorption | `docs/reviews/CVF_MODEL_GATEWAY_LEGACY_ABSORPTION_GAP_DISPATCH_CORRECTION_2026-06-13.md` | `## Corrective Decision` | `Corrective Decision status` | correction review | ACCEPT |
| EXISTS: LHW17 T2 prior advisory exists | `docs/reference/archive/CVF_LHW17_T2_MODEL_GATEWAY_UNIFICATION_ADVISORY_CONNECTOR_SPEC_2026-05-30.md` | header | `cvf.modelGatewayUnificationAdvisory.lhw17.t2.v1` | LHW17 T2 connector spec | ACCEPT |
| EXISTS: LHW17 T2 cites Model Gateway legacy source files | `docs/reference/archive/CVF_LHW17_T2_MODEL_GATEWAY_UNIFICATION_ADVISORY_CONNECTOR_SPEC_2026-05-30.md` | `## Source` | `ADDING_MODEL GATEWAY`; `ADDING_MODEL_ROUTER`; `ADDING_MINI_MODEL GATEWAY` | LHW17 T2 connector spec | ACCEPT |
| EXISTS: corpus registry field `priorAbsorption` is canonical | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` | `## Required Registry Entry Fields` | `priorAbsorption` | corpus scan registry standard | ACCEPT |
| EXISTS: memory method audit is partial | `docs/audits/CVF_MEMORY_METHOD_LEGACY_RESCAN_AUDIT_2026-06-01.md` | header | `Status` | memory method audit | ACCEPT |
| EXISTS_PATH_ONLY: active operator-opened file is in allowed gateway scope | `.private_reference/legacy/CVF_Important/ADDING_MODEL GATEWAY/CVF_ARCHITECTURE.md` | path inventory | `CVF_ARCHITECTURE.md` | legacy path inventory | ACCEPT |

## 6. Execution Instructions

1. Read all authority-chain files.
2. Inventory gateway-family files with ignore-proof enumeration.
3. Compare inventory against LHW17 T2 source list and C-02 correction source
   inventory.
4. Read gateway-family legacy content only within the allowed scope.
5. Produce an accept/defer/reject matrix:
   - accepted legacy value;
   - source file;
   - current owner surface;
   - duplicate prevention key;
   - disposition;
   - reason.
6. Update `MGW-001` in the coverage index.
7. Reconcile `MEM-001` and `SCAN-001` from registry/audit evidence only.
8. Produce the Model Gateway recheck plan.
9. Produce worker return with gates and exact uncommitted artifact list.

## Execution Plan

| Step | Action | Output |
| --- | --- | --- |
| 1 | Read required first reads | Source authority understood |
| 2 | Inventory allowed gateway legacy families | Gateway legacy inventory table |
| 3 | Reconcile LHW17 T2 source list against current inventory | Prior absorption reconciliation |
| 4 | Read allowed gateway legacy files | Accept/defer/reject matrix |
| 5 | Map accepted or deferred values to owner surfaces | Current owner surface map |
| 6 | Update coverage index | Updated `MGW-001`; evidence-only updates where justified |
| 7 | Produce recheck plan and worker return | Two new uncommitted artifacts |
| 8 | Run worker gates | Gate evidence in worker return |

## 7. Required Sections In Worker Deliverables

The recheck plan must include:

- `## Purpose`
- `## Source Authority Table`
- `## Gateway Legacy Inventory`
- `## Prior Absorption Reconciliation`
- `## Current Owner Surface Map`
- `## Accept / Defer / Reject Matrix`
- `## Duplicate Prevention Ledger`
- `## C-02 Resume Decision`
- `## Knowledge Absorption Blind-Spot Control Block`
- `## Claim Boundary`

The worker return must include:

- `## Summary`
- `Agent Operation Trace Block`
- `## Source Verification Block`
- `## Negative Search And Collision Discipline`
- `## Finding-To-Governance Learning Disposition`
- `## Worker Pending-Return Gate`
- `## Public Export Disposition`
- `## Claim Boundary`

## 8. Required Worker Gates

Run before return:

```text
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short
```

If focused tests are not applicable, record `N/A with reason: documentation
and index update only; no runtime/source/test files changed`.

## Evidence Requirements

Worker evidence must include:

- exact gateway legacy inventory command and result summary;
- prior LHW17 T2 reconciliation table;
- current owner-surface search commands;
- index row changes;
- no-runtime/no-provider/no-public claim boundary;
- `git diff --name-status`;
- `git status --short`;
- worker gate outputs.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Claude worker |
| Provider or surface | Claude cowork |
| Session or invocation | `model_gateway_legacy_absorption_coverage_index_2026-06-13` |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | Worker must record exact commands used |
| Target paths | index, recheck plan, worker return |
| Allowed scope source | this work order and GC-018 baseline |
| Before status evidence | worker must record `git status --short` before edits |
| After status evidence | worker must record `git status --short` after edits |
| Diff evidence | worker must record `git diff --name-status` |
| Approval boundary | documentation and index update only |
| Claim boundary | bounded legacy absorption recheck; no runtime/provider/public claims |
| Agent type | Claude |
| Invocation ID | `model_gateway_legacy_absorption_coverage_index_2026-06-13` |
| Expected manifest | N/A with reason: this trace block covers dispatch packet authoring; worker deliverable manifest is specified in `## 0. Dispatch Summary` and must be repeated in the worker return |
| Actual changed set | N/A with reason: dispatch changed-set evidence is captured by Codex gates before commit; worker must record actual changed set in the worker return |
| Manifest delta | N/A with reason: worker manifest delta is not available until Claude returns uncommitted deliverables |
| Deletion or rename disposition | N/A with reason: no delete or rename authorized |

## 10. Completion Criteria

The worker return is acceptable only if:

- `MGW-001` is updated with source-backed legacy coverage status;
- the recheck plan says whether C-02 can resume, must be rewritten, or remains
  held;
- prior LHW17 T2 evidence is reconciled instead of repeated blindly;
- any new gateway legacy value is mapped to owner surface or deferred/rejected;
- `MEM-001` and `SCAN-001` remain evidence-only unless a separate future
  GC-018 is required;
- no runtime/source/test/provider/public mutation occurs;
- worker gates pass.

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| `MGW-001` coverage status updated | Source-backed status and next action |
| C-02 decision | `RESUME_WITH_REWRITE`, `RESUME_WITH_BOUNDARY_PATCH`, or `REMAIN_HELD` |
| Duplicate prevention | LHW17 T2 evidence reconciled before new value is accepted |
| Memory/scan layer | Evidence-only reconciliation or explicit later GC-018 recommendation |
| Runtime/provider/public boundary | No mutation or readiness claim |
| Worker gates | PASS or blocked return with evidence |

## Review Gate

Codex must run reviewer-fast before accepting the return:

```text
python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast
```

Codex may repair allowed-scope documentation or index defects. Codex must not
convert worker findings into runtime/source/test changes in this closure.

## Closure Checklist

Closure requires:

- Worker return received with exact artifact list.
- Reviewer-fast passes.
- Completion review created at `completionReviewPath`.
- Pre-closure autorun gate passes on the committed range.
- Session state is synced if next allowed move changes.
- Worktree is clean after commit.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when all allowed deliverables are present
and worker gates pass.

Return `BLOCKED_RETURN_TO_ORCHESTRATOR` if a needed action exceeds allowed
scope, requires a new legacy family, requires provider/live/runtime work, or
requires operator authorization.

## Operator Checkpoint

No operator checkpoint is required for allowed-scope recheck and index update.
Operator checkpoint is required before:

- resuming C-02 as implementation;
- opening broad memory/scan legacy content reread;
- adding runtime/provider/live-proof work;
- using public-sync;
- changing agent computer-control or OS audit behavior.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order. Public-sync is not authorized.

## Claim Boundary

This work order authorizes bounded Model Gateway legacy absorption recheck and
coverage-index update only. It does not authorize implementation, provider
calls, live proof, public-sync, production readiness, public readiness, cost or
quality claims, or broad legacy absorption outside the named scope.
