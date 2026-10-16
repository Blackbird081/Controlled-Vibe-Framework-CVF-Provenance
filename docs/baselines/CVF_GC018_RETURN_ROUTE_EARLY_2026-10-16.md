# CVF GC-018 Baseline - Return Route Early Dispatch Validation

Memory class: governed-baseline
docType: baseline
Status: REVIEWER_ACCEPTED_BOUNDED_PROCEDURE_PARTIAL
Date: 2026-10-16
Batch ID: CVF-RETURN-ROUTE-EARLY-20261016
Commit mode: WORKER_MUST_NOT_COMMIT
providerExecutionAuthority: FORBIDDEN
Inspection base: a6057f3eff1d0e983fdd8b7c8a9dd8da69b3bbe2

## Purpose

Operator authorizes implementing the repeated-defect checker correction with low incremental latency. Reuse the existing dispatch-quality gate and production return parser. This baseline is the bounded SPEC; docs/work_orders/CVF_AGENT_WORK_ORDER_RETURN_ROUTE_EARLY_2026-10-16.md is the worker packet. No new general checker, runtime or broad verification campaign.

## Scope / Target / Owner Boundary

Explicit current operator instruction2026-10-16 and standing Local orchestrator/reviewer authority. Existing learning docs/reviews/learnings/CVF_ORCHESTRATOR_PREAPPROVAL_FEASIBILITY_LEARNING_2026-10-08.md O10-O14 is already committed58d19d787/a6057f3ef. Scope is exact3 current compatibility source/test paths plus full worker return/evidence2. Local owns review, commits, status metadata and exact6 continuity. All prior B-E grants stay retired. Source/authority differences discovered outside this scope return once to Local.

## Locked Action Contract

earlyRouteSpecVersion: RETURN_ROUTE_EARLY_V1

1. Extend the existing work-order dispatch-quality gate, no new checker/catalog/hook. For changed READY/DISPATCHED work orders with a real requiredGate scalar declaring governance/compat/run_worker_return_fast_gate.py in Worker Return Packet Shape Contract, validate mandatory return-command construction before dispatch even without preapproval opt-in. Arbitrary prose/examples and unmarked legacy orders do not activate this check.
2. Reuse the production build_commands and _worker_return_path parser with exact snapshotted text, repository root and work-order path. Reject missing, bare and duplicate workerReturnPath via one actionable issue. Do not implement a parallel permissive parser. Do not require future return output to exist. Preserve current production path semantics; return-path safety expansion is outside this patch.
3. Keep draft/HOLD/closed historical packets and non-fast-gate work orders outside this new check. Preserve changed-file and inherited-violation semantics by adding a helper in the small main module and one call in the existing dispatching branch in range module. READY mutations that newly violate the route must fail. Existing opt-in preapproval semantics remain unchanged.
4. No subprocess, downstream gate/test run, whole-repository scan or new service in this validation. Build commands with empty test targets; lazy imports or an existing shared import are ordinary detail. Main<=400lines, range<=985lines, existing test<=300lines. No split/size exception.
5. Regression tests exercise production dispatch validator/caller, exact bare/missing/duplicate/valid variants, no opt-in marker, DRAFT/HOLD/closed/non-fast/prose immunity and the real frozen October16 order preimage from immutable Git revision 27dff0217. Keep historical source bytes read-only; fixture copies only. Stub subprocess execution to fail if invoked by new validation.
6. Measure incremental validation cost separately from full hook startup: finite warm valid/invalid fixtures, report count/elapsed/per-call and actual new subprocess count0. Avoid brittle wall-clock pass thresholds. One worker focused subset plus one distinct Local oracle; no repeated full suites or provider/runtime probe.
7. Existing scripts/cvf_commit_tranche.py already stops failed preparation commands. Reuse it for task commits, inspect its existing failure test rather than create another runner. Explicitly preserve the fact that a post-commit release rejection cannot undo the already-made continuity commit. No automated guard can attest arbitrary future shell command handling.
8. Return all8 requirement/proof joins, actual source pins/tests/costs/failures and pending independent Local probe. Learning O10/O11/O13/O14 applied to this guard task; Windows preload/junction functional fix/proof remains the separate source-correction plan, not silently claimed by this guard patch.

## Write Ownership

- `governance/compat/check_work_order_dispatch_quality.py`
- `governance/compat/check_work_order_dispatch_quality_range.py`
- `governance/compat/test_check_work_order_dispatch_quality_worker_return_contract.py`
- `docs/reviews/CVF_RETURN_ROUTE_EARLY_WORKER_RETURN_2026-10-16.md`
- `docs/reviews/evidence/return-route-early-worker-20261016.json`

Only these five paths are worker writable. Main<=400lines; range<=985lines (current971); existing test<=300lines (current112). No source split or exception. Fixtures live under worker-owned temporary/ignored custody; installed local tools only. Root task-source edits include baseline/order/status/completion/evidence, related existing shared learning/discovery/parent raw source pins and exact6 continuity. Local documentary closure topology only; worker exact5/effect/source3 scope unchanged.

## Source / Predecessor Evidence

```json
[
  {
    "path": "governance/compat/check_work_order_dispatch_quality.py",
    "sha256": "a2356b1d86c32ddd3773eb908e13d0ef698d4cbc58500da2bb983a718caa8988"
  },
  {
    "path": "governance/compat/check_work_order_dispatch_quality_range.py",
    "sha256": "980e52435ea3e02dd0a1065c4f2c95d7fe6c0d1896ee83a34123b3bea4763c7f"
  },
  {
    "path": "governance/compat/test_check_work_order_dispatch_quality_worker_return_contract.py",
    "sha256": "54a91271d2bd6badff47a40c6666d121ab689936df2758785c4ae71880a18d09"
  },
  {
    "path": "governance/compat/run_worker_return_fast_gate.py",
    "sha256": "8132cd26c46bb9a2c26e2dd86a13a45b07cdbbe822f62011adee1af6b801e8ee"
  },
  {
    "path": "scripts/cvf_commit_tranche.py",
    "sha256": "1a296b55e9590d80f83f3a57f9f88f0ddc3d8071c7ca909682a817ac38284754"
  },
  {
    "path": "scripts/test_cvf_commit_tranche.py",
    "sha256": "d9cc5479e57286a9f96f090f45def137a6193b0bcde59f3d7054f3fef016169e"
  },
  {
    "path": "docs/reviews/learnings/CVF_ORCHESTRATOR_PREAPPROVAL_FEASIBILITY_LEARNING_2026-10-08.md",
    "sha256": "2e27b93ec2ddf2197ed7320357647c3f84ba36b154ebd310b1935970ccf34c40"
  }
]
```

Current raw pin identity is checked before worker edits; historical pins remain dispatch facts after implementation, not final-source hashes. Original pair is retained in ignored custody before any closure status transition.

## Evidence / Verification

REQ-01 trigger/current dispatch coverage; REQ-02 exact production parser negatives; REQ-03 command binding/static buildability; REQ-04 compatibility; REQ-05 frozen real-packet regression; REQ-06 cost/no-subprocess evidence; REQ-07 fail-fast reuse/outcome boundary; REQ-08 full return/source/learning/manifest/gate evidence. All mandatory. Distinct Local probe remains pending until actually executed; worker tests are consumed once. Normal required full gates remain; extra repeated suites or runtime calls are not authorized by this SPEC.

## Core Guard Self-Protection Authorization

Additional Local final topology protected path: `governance/compat/check_work_order_dispatch_quality_artifacts.py`. Explicit operator-authorized guard correction; exact body relocation only.

Authorized guard-maintenance scope: extend existing dispatch-quality return-route construction and focused regression only.
Protected paths:
- `governance/compat/check_work_order_dispatch_quality.py`
- `governance/compat/check_work_order_dispatch_quality_range.py`
- `governance/compat/test_check_work_order_dispatch_quality_worker_return_contract.py`
Operator authorization: operator explicitly said to implement the preceding checker proposal and avoid disproportionate latency on2026-10-16; standing Local orchestration/maintenance/commit authority applies.
Rollback boundary: these three source/test paths and exact new task artifacts only; preserve October16 negative runtime originals, retired grants, source13/adjunct5, gen9/SCEC2/counters2,0,2,0/blockers2/freeze/prior7 exclusions and parked lanes. No runtime/provider/public/deploy or other guard semantics.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_work_order_dispatch_quality_range.py; governance/compat/run_worker_return_fast_gate.py; governance/compat/check_core_guard_self_protection.py; governance/compat/check_work_order_acceptance_ledger.py |
| literalTokensReviewed | exact workerReturnPath; requiredGate; no opt-in assumption; full-return and source pins |
| gateRunPurpose | bounded packet confirmation after source/design review |
| claimBoundary | declared-state command construction only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Private maintenance only; no public catalog/export claim.

## Claim Boundary

No B-E replay or product source amendment. Windows integration repair remains separate PLAN. All historical first negative bytes, stage/custody, retired pair and source13/adjunct5/gen9/SCEC2/counters2,0,2,0/blockers2/freeze/prior7 exclusions/parked effects remain. No AI behavior, runtime readiness or universal agent compliance proof.

## Decision / Baseline

Proceed with the exact3 guard/test amendment after committed packet/continuity and actual gates; no runtime grant.

## ADIF Defect Registry Disclosure


Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, maxResults=`40`
Resolver command: `python -B governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 40 --json`
Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045, ADIF-0051, ADIF-0052, ADIF-0056, ADIF-0057, ADIF-0058, ADIF-0061, ADIF-0062, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006
Actual query exit0 retained in task custody; relevant source/ownership/closeability and failure route applied. Worker resolves its own role/phase before edits; no claim all entry bodies were reread.


## Scaffold Provenance Block


| Field | Value |
|---|---|
| scaffoldHelperCommand | `python -B governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id CVF-RETURN-ROUTE-EARLY-20261016 --title Return Route Early Dispatch Validation --date 2026-10-16 --base a6057f3eff1d0e983fdd8b7c8a9dd8da69b3bbe2 --commit-mode WORKER_MUST_NOT_COMMIT --scec-problem-key return-route-early-dispatch-coverage --no-evidence-readiness-applicable --stdout` |
| generatedProfile | protected-governance-path; INTERNAL_AGENT INITIAL; WORKER_MUST_NOT_COMMIT |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | ADAPTED_WITH_REASON: existing accepted control shape adapted to exact3 code/test, locked SPEC and8 joins |
| checkerReadAheadConfirmation | operative source/predicate and exact literals read |
| docOnlyNewFields | earlyRouteSpecVersion |
| claimBoundary | actual helper exit0/hash in ignored preparation; no semantic approval |


## Pre-Implementation Ledger Correction

The required test file is included in REQ-01..07 expectedArtifacts so the union of eight requirements covers every exact5 worker deliverable. Worker caught this Local packet omission during read-ahead before any gate/edit/test. This corrects ledger coverage only; source/effect/role/budget scope unchanged. Original release preimages retained in ignored custody.

## Local Closure Disposition

ACCEPTED_TECHNICAL_BOUNDED_PROCEDURE_PARTIAL: Local accepted the static early return-route repair after consumed worker evidence and distinct seven-case production-validator oracle. REQ01..07 technical requirements accepted; REQ08 historical mandatory read order remains BLOCKED. Full work-order fulfillment is not asserted and cannot be repaired retroactively. No B-E functionality, Windows source repair or universal learning effectiveness claim. Original dispatch pair/worker bytes retained in Local custody; no successor grant.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | docs/work_orders/CVF_AGENT_WORK_ORDER_RETURN_ROUTE_EARLY_2026-10-16.md; docs/baselines/CVF_GC018_RETURN_ROUTE_EARLY_2026-10-16.md | eight result rows and Local proof; REQ08 procedure limit retained | PASS - bounded technical disposition only |
| Completion or reviewer artifact | docs/reviews/CVF_RETURN_ROUTE_EARLY_COMPLETION_2026-10-16.md; docs/reviews/evidence/return-route-early-local-20261016.json | distinct Local7/7 and frozen source/worker hashes | PASS - accepted static scope |
| Roadmap state | existing NCR Windows source-correction PLAN | source13/adjunct5/gen9/SCEC2 remain | PASS - no product stage advanced |
| Registry JSON | docs/reference/downstream_gate_profile/downstream_finding_intake_registry.json | two learning raw source pins refreshed; typed lifecycle decisions/receipts unchanged | PASS - source pins only |
| Registry Markdown | docs/reviews/learnings/README.md | existing learning discovery updated | PASS - no new guard family |
| External evidence digest | docs/reviews/evidence/return-route-early-local-20261016.json | internal worker/source and Local proof only | N/A with reason - no external intake |
| System loop interlock | existing parent NCR state | no parent runtime/counter transition | N/A with reason - no loop change |
| Session continuity | active handoff/front/core/entry and generated source6 | paired raw hashes atomic; actual material SHA in following exact6 | PASS - source-owned continuity; clean split closure follows |

## Local Final Topology Correction

Local final approved-size gate found the dispatcher budget was wrong: main was frozen at approved313, not the packet400. Original worker return/source/proof bytes remain unchanged in custody; this is a Local preparation defect. Local relocated the exact two helper bodies and runner import into the existing exec-loaded artifacts module, restoring the main file byte-identical to the release HEAD304. Final source3 is artifacts757/range972/test274; no new module, registry exception, checker or hook. Existing class hard1000 remains; artifacts757 is a soft advisory under existing policy. This bounded topology amendment authorizes only governance/compat/check_work_order_dispatch_quality_artifacts.py in addition to the original historical worker scope; final material replaces the unchanged main with artifacts and remains exact18. No redispatch, business effect or runtime grant. Named information gain for focused rerun: approved-size contradiction and import/exec placement changed; contract module7PASS0.68s and Local seven-case production oracle passed after relocation. Worker full gate applies to frozen returned layout; final Local gates bind final layout. Historical REQ08 remains BLOCKED.

Final governing size budgets: main<=313 and net delta0; existing artifacts<=800 task budget within hard1000; range<=985; test<=300. Earlier main<=400 and no foreseeable relocation estimates are superseded at this Local final boundary. Original ledger/proof remains the worker historical contract, not a rewritten claim of original preparation.
