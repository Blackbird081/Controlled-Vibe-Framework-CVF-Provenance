# CVF Work Order - MKG2 Deferred Runtime Candidate Triage

Memory class: FULL_RECORD

Status: PLANNING_OPEN_NOT_DISPATCHED

docType: work_order

Date: 2026-06-01

## Purpose

Prepare the next agent to triage the `21` MKG1 deferred assets only after the
operator starts MKG2. This work order is intentionally held; it is not a
dispatch signal.

## Authority Chain

| Authority | Path / basis | Disposition |
| --- | --- | --- |
| MKG2 GC-018 | `docs/baselines/CVF_GC018_MKG2_DEFERRED_RUNTIME_CANDIDATE_TRIAGE_2026-06-01.md` | ACCEPT |
| MKG2 roadmap | `docs/roadmaps/CVF_MKG2_DEFERRED_RUNTIME_CANDIDATE_TRIAGE_ROADMAP_2026-06-01.md` | ACCEPT |
| MKG1 completion | `docs/reviews/CVF_MKG1_MEMORY_KNOWLEDGE_GRAPH_OWNER_SURFACE_REVIEW_COMPLETION_2026-06-01.md` | ACCEPT |
| RESCAN-C manifest | `docs/audits/CVF_LHW_RESCAN_C_LEGACY_PARTIAL_ROOTS_CORPUS_MANIFEST_2026-06-01.json` | ACCEPT |

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | release HOLD only when MKG2 is intentionally dispatched | no silent implementation |
| Worker | enumerate and classify deferred assets | no runtime edits |
| Reviewer | challenge source-owner claims | block guessed owners |

## Scope

Allowed scope after dispatch:

- read MKG1 completion and RESCAN-C manifest;
- enumerate the `21` deferred assets;
- source-verify current owner candidates;
- draft future tranche routing.

Forbidden scope:

- `.private_reference/legacy/**` edits;
- runtime source edits;
- live/provider proof;
- graph retrieval execution;
- Memory reinjection;
- skill mutation;
- public-sync or push;
- destructive action.

Risk ceiling: R1 planning and documentation.

## Required First Reads

- `docs/reviews/CVF_MKG1_MEMORY_KNOWLEDGE_GRAPH_OWNER_SURFACE_REVIEW_COMPLETION_2026-06-01.md`
- `docs/audits/CVF_LHW_RESCAN_C_LEGACY_PARTIAL_ROOTS_CORPUS_MANIFEST_2026-06-01.json`
- `docs/reference/CVF_WORKER_AUTONOMY_DISPATCH_PROMPT_STANDARD_2026-06-01.md`
- `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md`

## Pre-Flight Checks

Do not run as implementation until the operator explicitly starts MKG2.

Required after dispatch:

```powershell
git rev-parse --short HEAD
git status --short
python scripts/build_legacy_rescan_c_manifest.py --check-only --expected-manifest-hash ae7fe05e016b7079a81002de60de1e1209112de59c8bee793e15e11557cae0ff
python governance/compat/check_work_order_dispatch_quality.py --base <baseHead> --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base <baseHead> --head HEAD
```

## Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| MKG1 has 21 deferred candidates | VALUE_SET | `docs/reviews/CVF_MKG1_MEMORY_KNOWLEDGE_GRAPH_OWNER_SURFACE_REVIEW_COMPLETION_2026-06-01.md` | Owner-Surface Mapping | `deferred` | MKG1 completion | ACCEPT |
| RESCAN-C manifest hash backs candidate enumeration | VALUE_SET | `docs/audits/CVF_LHW_RESCAN_C_LEGACY_PARTIAL_ROOTS_CORPUS_MANIFEST_2026-06-01.json` | `manifestHash` | `ae7fe05e016b7079a81002de60de1e1209112de59c8bee793e15e11557cae0ff` | RESCAN-C manifest | ACCEPT |
| Worker autonomy standard exists | EXISTS | `docs/reference/CVF_WORKER_AUTONOMY_DISPATCH_PROMPT_STANDARD_2026-06-01.md` | Worker Autonomy Prompt | `Worker Autonomy / No-Question Rule` | worker autonomy standard | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| Re-enumerate deferred rows | Scope / Required First Reads | deferred-candidate ledger | manifest hash check | HOLD |
| Source-verify owner candidates | Source Verification Block | owner map | dispatch-quality gate | HOLD |
| Split future roadmaps | Execution Plan | candidate routing matrix | reviewer challenge | HOLD |
| Apply worker autonomy | Worker Autonomy / No-Question Rule | prompt block | dispatch-quality gate | HOLD |

## Worker Autonomy / No-Question Rule

Once MKG2 is explicitly dispatched, the worker must not ask the operator before
performing non-destructive actions inside Allowed scope.

Proceed autonomously with reading named files, running manifest/hash checks,
running governance gates, fixing documentation format defects inside Allowed
scope, adding missing required evidence blocks, and rerunning failed guards
after allowed-scope remediation.

Ask only if the next action would exceed Allowed scope, edit Legacy source,
edit runtime/source code, run live/provider proof, use secrets/quota,
public-sync, push/publish, change claim boundary or risk, release a `HOLD_*`
prerequisite, touch forbidden paths, or perform destructive/irreversible
action.

## Write Ownership

Owned future paths after dispatch:

- a future MKG2 completion or candidate-routing review;
- this MKG2 work order;
- MKG2 roadmap and continuity records if status changes.

Forbidden paths are listed in Scope.

## Execution Plan

1. Recompute the `21` deferred rows from MKG1.
2. Classify candidates into Cortex bridge/runtime, skill-governance, and graph
   implementation planning.
3. Verify current owner surfaces before naming any future implementation path.
4. Draft future roadmaps or return blocked items to the orchestrator.
5. Run dispatch and closure gates before any ready/closed claim.

## Evidence Requirements

- manifest JSON and hash citation;
- `21/21` deferred candidate ledger;
- source verification for every runtime/source owner claim;
- explicit no-runtime/no-live/no-public boundary.

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| Deferred count | `21/21` accounted for |
| Source verification | no guessed runtime/source owner |
| Autonomy standard | worker prompt rule present |
| Runtime boundary | no implementation or live proof |

## Review Gate

Reviewer must reject any MKG2 packet that treats Legacy `cortex-hub`,
`Memento-Skills`, or `code-review-graph` as current CVF owners without current
source verification.

## Closure Checklist

- N/A with reason: this work order is held, not executed.

## Return-To-Orchestrator Conditions

Return if implementation becomes necessary, a current source owner cannot be
verified, live proof is required, or the worker needs to exceed Allowed scope.

## Operator Checkpoint

This work order remains not dispatched until the operator explicitly starts
MKG2.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private held work order only. No public-sync remote, public repository
commit, or public artifact path is included.

## Claim Boundary

MKG2 is not dispatched by this file. It is a held work order for future planning
only and does not authorize implementation, live proof, runtime behavior,
public-sync, graph retrieval, Memory reinjection, skill mutation, hosted
readiness, production readiness, or public readiness.
