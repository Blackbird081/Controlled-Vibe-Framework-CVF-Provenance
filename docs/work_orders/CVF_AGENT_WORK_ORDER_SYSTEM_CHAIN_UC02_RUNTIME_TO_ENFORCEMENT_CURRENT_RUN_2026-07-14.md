# CVF Agent Work Order - System Chain UC-02 Runtime-To-Enforcement Current Run

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: work_order

Work Order ID: SCLP-UC02

Date: 2026-07-14

dispatchBaseHead: `a9507c1b0`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: implementation/proof worker. The reviewer/closer is a separate role.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_SYSTEM_CHAIN_UC02_RUNTIME_TO_ENFORCEMENT_CURRENT_RUN_2026-07-14.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

Base: executionBaseHead captured with `git rev-parse --short HEAD` at worker start.

Current-time notes: local provider-free chain; no API key or external service required.

Do-not-misread notes: run the dedicated proof runner once; do not run the full CF-001 through CF-084 aggregate and do not invoke checkers directly.

Required first actions: read this work order, paired GC-018, standard, ledger, registry, and both runner sources; then capture clean executionBaseHead and run pre-implementation.

Return contract: `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` with exact changed paths, executionBaseHead, tests/gates, receipt/diagnostic, denominator, and HEAD-unchanged evidence.

## Purpose

Convert the UC-02 operational evidence gap into one reproducible, bounded,
current-run worker task without changing existing enforcement semantics.

## Objective

Produce one current, bounded, provider-free execution receipt proving that the
canonical registry routes CF-076 through CF-084 through the real
packet-posture runner to their nine named governance checkers.

## Authority / Decision

Authority chain:

1. `docs/reference/system_chain/CVF_SYSTEM_CHAIN_LIVE_PROOF_AND_LEARNING_LOOP_STANDARD.md`
2. `docs/reference/system_chain/CVF_SYSTEM_CHAIN_LIVE_PROOF_COVERAGE.json`
3. `docs/roadmaps/CVF_SYSTEM_CHAIN_LIVE_PROOF_USE_CASE_ROADMAP_2026-07-14.md`
4. paired GC-018 baseline
5. this work order

T0 material commit `e4a585b8c` and session commit `a9507c1b0` release UC-02
packet authoring. This dispatch authorizes exactly one no-commit worker after
pre-dispatch passes.

## Authority Chain

The authority order is canonical live-proof standard, machine coverage ledger,
active roadmap, paired GC-018, then this work order. Current source overrides
historical review prose for executable symbols and commands.

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | dispatcher role | source verification and packet quality |
| Worker | delegated implementation/proof agent | exact manifest, one bounded run, no commit |
| Reviewer/closer | reviewer/closer role | independent evidence review, repair decision, commit, reverse projection |

## Required First Reads

| Source | Action |
|---|---|
| this work order | FULL_READ |
| paired GC-018 baseline | FULL_READ |
| live-proof standard | FULL_READ |
| live-proof coverage ledger | FULL_READ |
| canonical scenario registry | SOURCE_VERIFIED |
| aggregate and packet-posture runners | SOURCE_VERIFIED |

## Pre-Flight Checks

Before status evidence: clean worktree confirmed at dispatcher base
`a9507c1b0`; only this paired dispatch packet is introduced by the dispatcher.

Worker must capture `executionBaseHead`, run `git status --short`, rerun source
search, execute pre-implementation autorun, and stop if the worktree contains
unrelated changes.

## Scope / Target / Owner Boundary

Allowed worker outputs:

- `scripts/run_cvf_system_chain_uc02_current_proof.py`
- `governance/compat/test_run_cvf_system_chain_uc02_current_proof.py`
- `docs/reviews/evidence/system-chain-uc02-current-run-2026-07-14.json`
- `docs/reviews/evidence/system-chain-uc02-diagnostic-2026-07-14.json`
- `docs/reviews/CVF_SYSTEM_CHAIN_UC02_RUNTIME_TO_ENFORCEMENT_CURRENT_RUN_WORKER_RETURN_2026-07-14.md`
- one GC-051 source entry for the new governed test and regenerated corpus
  aggregate if the registry checker requires it.

All existing scenario, runner, packet, checker, CI, semantic-map, Catalog/GAP,
session, and public paths are read-only.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| canonical scenario registry path | `scripts/run_cvf_cross_extension_conformance.py` | line 20 | `SCENARIO_REGISTRY` | aggregate conformance runner | ACCEPT |
| registry loader consumes command arrays | `scripts/run_cvf_cross_extension_conformance.py` | lines 203-217 | `_load_scenarios` | aggregate conformance runner | ACCEPT |
| subprocess execution preserves UTF-8 output | `scripts/run_cvf_cross_extension_conformance.py` | lines 235-251 | `_run` | aggregate conformance runner | ACCEPT |
| CF-076 through CF-084 share packet state bootstrap | `scripts/run_cvf_cross_extension_conformance.py` | lines 103-148 | `SCENARIO_DEPENDENCY_GROUPS` | dependency-group mapping | ACCEPT |
| target scenario command arrays | `docs/reference/CVF_CONFORMANCE_SCENARIOS.json` | lines 532-592 | `CF-076`; `CF-077`; `CF-078`; `CF-079`; `CF-080`; `CF-081`; `CF-082`; `CF-083`; `CF-084` | scenario registry `scenarios` array | ACCEPT |
| real packet set contains four canonical packets | `scripts/run_cvf_packet_posture_gate_conformance.py` | lines 17-22 | `PACKETS` | packet-posture gate runner | ACCEPT |
| gate CLI resolves and invokes named checker | `scripts/run_cvf_packet_posture_gate_conformance.py` | lines 42-56 | `main` | packet-posture gate runner | ACCEPT |
| UC-02 required proof and scope | `docs/reference/system_chain/CVF_SYSTEM_CHAIN_LIVE_PROOF_COVERAGE.json` | use case UC-02 and lane `RUNTIME_TO_ENFORCEMENT` | `UC-02-RUNTIME-TO-ENFORCEMENT-CURRENT-RUN` | live-proof coverage schema | ACCEPT |
| UC-02 is the first planned runtime use case | `docs/roadmaps/CVF_SYSTEM_CHAIN_LIVE_PROOF_USE_CASE_ROADMAP_2026-07-14.md` | Tranche Plan | `T1 / UC-02` | system-chain live-proof roadmap | ACCEPT |

## New Doc-Only Fields

| Field | Owner | Purpose |
|---|---|---|
| `proofClass` | UC-02 JSON receipt | records `CURRENT_RUNTIME_INVOCATION` |
| `scenarioDenominator` | UC-02 JSON receipt | distinguishes 9 scenario results from one proof-run invocation |
| `bootstrapResult` | UC-02 JSON receipt | records the single shared bootstrap outcome |
| `commandSha256` | UC-02 JSON receipt | proves each executed command matches the registry array without duplicating long command text |
| `diagnostic` | UC-02 diagnostic JSON | secret-safe failure classification before retry |

These are new receipt-only fields. They are not represented as existing runtime
or registry fields.

## Current Runtime Freshness Verification

Fresh source search at `dispatchBaseHead a9507c1b0` confirmed all Source
Verification rows and found no bounded scenario-selection CLI on the aggregate
runner. The worker must recompute line/symbol presence at `executionBaseHead`.
If any symbol, registry command, or exact nine-ID set differs, stop and return
`BLOCKED_WITH_REASON` rather than adapting from memory.

## Execution Plan

1. Capture clean `executionBaseHead`; confirm it equals or descends only from
   the dispatch commit and run pre-implementation.
2. Recompute all Source Verification facts and exact target IDs.
3. Implement a dedicated proof runner that:
   - reads the canonical registry with UTF-8;
   - requires exactly the nine target IDs once each;
   - validates every target command begins with the existing packet-posture
     runner and a named `governance/compat/check_*.py` gate;
   - invokes the existing packet bootstrap exactly once;
   - sets `CVF_SKIP_PACKET_POSTURE_STATE_BOOTSTRAP=1` only for the nine
     scenario commands to prevent repeated bootstrap;
   - executes registry command arrays unchanged with UTF-8 replacement-safe
     capture;
   - fails closed and writes one atomic secret-safe JSON receipt.
4. Add focused tests using temporary registries and fake subprocess results;
   do not invoke the nine real checkers from unit tests.
5. Run focused tests, JSON/schema assertions, and secret scan.
6. Invoke the proof runner once against the real registry.
7. If it fails, write the diagnostic and stop. One retry is permitted only
   after a concrete repair changes the expected result.
8. Write the checker-safe worker return and leave HEAD unchanged.

## Planned Worker Fulfillment Manifest

| Artifact | Required action |
|---|---|
| `scripts/run_cvf_system_chain_uc02_current_proof.py` | create bounded registry-driven proof runner |
| `governance/compat/test_run_cvf_system_chain_uc02_current_proof.py` | create focused positive and negative tests |
| `docs/reviews/evidence/system-chain-uc02-current-run-2026-07-14.json` | current real-run receipt with 9-scenario denominator |
| `docs/reviews/evidence/system-chain-uc02-diagnostic-2026-07-14.json` | write `null` on first-run PASS or secret-safe diagnostic on failure |
| worker return path | create full-gate no-commit return |
| GC-051 source entry and aggregate | add/regenerate only when required by the registry checker |

## Write Ownership

Worker owns only the Planned Worker Fulfillment Manifest and must not commit.
Reviewer owns completion review, dispatch status conversion, coverage-ledger
update, roadmap state, material commit, and later session synchronization.

## Evidence Requirements

Record execution base, registry hash, selected IDs, command digests,
bootstrap result, each scenario result and duration, aggregate status,
`scenarioDenominator=9`, proof-run invocation count, retry count, diagnostic
disposition, focused test results, secret scan, exact changed set, and unchanged
HEAD. Do not persist raw secrets, environment values, or unbounded subprocess
output.

## Acceptance Criteria

- AC-01: target IDs equal CF-076 through CF-084, unique and complete.
- AC-02: executed commands are byte-equivalent JSON arrays from the registry.
- AC-03: bootstrap succeeds exactly once.
- AC-04: all nine scenarios execute through the existing packet runner.
- AC-05: each selected checker is therefore invoked against four canonical
  packets by the existing runner.
- AC-06: receipt reports one proof-run call and nine scenario events without
  denominator ambiguity.
- AC-07: all nine scenarios pass for acceptance; any failure remains honest.
- AC-08: negative tests cover missing, duplicate, invalid command, bootstrap
  failure, scenario failure, and partial denominator.
- AC-09: no provider/API call, direct checker shortcut, existing-source
  mutation, or semantic verdict change.
- AC-10: worker return passes the full gate and HEAD remains unchanged.

## Fail Conditions

Missing source, stale command, ID drift, bootstrap failure, any scenario
failure, denominator other than nine, raw secret/output leakage, existing
source mutation, direct checker invocation, second retry requirement, or a
claim stronger than current bounded execution returns the packet for review.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only with all planned artifacts, exact command
evidence, complete denominator, diagnostic disposition, gate results, clean
secret scan, changed-set evidence, and unchanged HEAD. Return
`BLOCKED_WITH_REASON` for any fail condition, naming the stopping evidence and
the smallest reviewer action needed.

## Operator Checkpoint

No operator checkpoint is required for one planned local invocation or one
diagnosed result-changing retry. A second retry, scope expansion, provider use,
existing checker/registry mutation, or claim expansion returns to the operator.

## Closure Checklist

| Closure item | Worker disposition |
|---|---|
| source verification refreshed | required in return |
| exact manifest respected | required in return |
| focused tests and real proof run recorded | required in return |
| denominator and diagnostic reconciled | required in return |
| HEAD unchanged and no commit | required in return |
| reviewer reverse projection | reviewer-owned, not worker closure |

## Worker Autonomy / No-Question Rule

Repair allowed-scope implementation/test/receipt defects directly. Stop only
for a Source Verification contradiction, forbidden-path need, unclear live
failure without safe diagnosis, secret risk, or second-retry need. Do not ask
the operator whether to repair an allowed-scope defect.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order control | Evidence |
|---|---|---|
| current real registry invocation | dedicated proof runner reads canonical registry | receipt registry hash and selected IDs |
| aggregate plus nine per-scenario results | receipt schema and AC-06 | one call-level status plus denominator 9 |
| diagnostic before retry | execution steps 6-7 | diagnostic JSON and retry count |
| no provider call | scope and AC-09 | source/diff review and process environment boundary |
| reverse projection | reviewer-owned closure conversion | coverage ledger update only following accepted evidence |
| stop after one complete invocation | one planned call; one diagnosed retry ceiling | invocation and retry counts |

## Cost And Retry Control

Planned current-run invocation count: one. This invokes nine scenario commands,
each applying one checker to four canonical packets. The receipt must report
both one proof-run call and nine scenario events; it must not present 9/9 as
nine independent proof-run calls. One diagnosed, result-changing retry is the
hard ceiling. No provider quota is used.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | one no-commit implementation/proof worker, then reviewer/closer |
| phase | UC-02 implementation, current run, and worker return |
| baseHeadFor(phase) | dispatchBaseHead=`a9507c1b0`; executionBaseHead=`WORKER_MUST_CAPTURE_AT_START`; closureBaseHead=`REVIEWER_TO_SET` |
| changedSetScope(phase) | exact Planned Worker Fulfillment Manifest only |
| traceScope(phase, actor) | worker records source refresh, tests, invocation, denominator, diagnostic, receipt, diff, and HEAD; reviewer owns closure |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer owns material commit |
| crossBatchIsolation | CLEAN_WORKTREE_CONFIRMED at dispatch; all existing source, registry, checker, packet, CI, semantic map, session, and public paths are read-only |
| nextMoveSurfaces | reviewer updates coverage ledger, roadmap, session state, handoff, and memory only following accepted material closure |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_SYSTEM_CHAIN_UC02_RUNTIME_TO_ENFORCEMENT_CURRENT_RUN_COMPLETION_2026-07-14.md` |
| reviewerOwnedClosurePaths | completion review; paired baseline/work-order status; coverage ledger; roadmap; active session sources |
| closureOwner | reviewer/closer role |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_SYSTEM_CHAIN_UC02_RUNTIME_TO_ENFORCEMENT_CURRENT_RUN_WORKER_RETURN_2026-07-14.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Skeleton command:
`python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_SYSTEM_CHAIN_UC02_RUNTIME_TO_ENFORCEMENT_CURRENT_RUN_WORKER_RETURN_2026-07-14.md --title "CVF System Chain UC-02 Runtime-To-Enforcement Current Run Worker Return" --profile WORKER_RETURN_FULL_GATE_V1`

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake route | operator-directed system-chain live-proof continuation |
| canonical route mode | `SINGLE_AGENT_SINGLE_ROLE` |
| selected role route | dispatcher -> no-commit worker -> reviewer/closer |
| scope classification | bounded local runtime-chain proof |
| risk sensitivity | R1 provider-free subprocess execution |
| escalation condition | source drift, forbidden path, secret risk, unclear failure, second retry, or claim expansion |
| Dispatcher role | dispatcher role |
| Worker route | `WORKER_MUST_NOT_COMMIT` |
| Reviewer/closer route | reviewer/closer role after worker return |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | current runtime proof and source verification |
| Matching local-view guard | `governance/compat/check_work_order_dispatch_quality.py` |
| Owner surface | canonical CVF scenario registry and runners |
| Disposition | BLOCKED_UNTIL_CVF_PROOF at dispatch; reviewer accepts only fresh UC-02 receipt |
| Claim boundary | chat, provider-local memory, and historical PASS prose are not current-run authority |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: this tranche executes an already-mapped internal
system chain and does not scan or absorb an external/legacy corpus.

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact: `docs/audits/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_2026-07-10.md`

priorVerificationAnchor: material commit `645df8b83`

freshRecomputeRequired: yes; historical PASS rows select the use case but do
not close the current-run claim

unicodePathHandling: use literal repository paths and explicit UTF-8 readers;
new source, JSON keys, and governed prose remain ASCII

extractedTextAuthority: N/A with reason: no external extraction or OCR input

## Verification Commands

```text
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python -m pytest governance/compat/test_run_cvf_system_chain_uc02_current_proof.py -q
python scripts/run_cvf_system_chain_uc02_current_proof.py --json-output docs/reviews/evidence/system-chain-uc02-current-run-2026-07-14.json --diagnostic-output docs/reviews/evidence/system-chain-uc02-diagnostic-2026-07-14.json
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return --base <executionBaseHead> --head HEAD --enforce
git diff --check
git status --short
```

## Review Gate

Reviewer must independently verify registry hash, exact nine IDs, command
digests, bootstrap-once evidence, 9/9 results, denominator, secret safety,
changed set, and unchanged worker HEAD. Only the reviewer may update the
coverage ledger from `STALE` to `PROVEN` and close UC-02.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`live-proof`, role=`dispatcher`, lifecyclePhase=`dispatch`

Query:
`python governance/compat/run_adif_defect_resolver.py --task-class live-proof --role dispatcher --lifecycle-phase dispatch --surface-selector system-chain --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --help` |
| generatedProfile | work-order full dispatch |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | all sections manually source-verified and reconciled |
| checkerReadAheadConfirmation | applicable checker sources read before first bundled gate |
| docOnlyNewFields | receipt-only fields listed in New Doc-Only Fields |
| claimBoundary | dispatch packet only; no UC-02 execution during authoring |

## Foundation Storage Layout Block

The new proof runner belongs under `scripts/` as an executable operational
surface. Its focused test belongs under `governance/compat/` for governed test
coverage. Evidence remains dated under the reviews evidence area. No stable
reference-family owner or new index folder is created; the existing
system-chain README and coverage ledger remain the durable front doors.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Source Verification Block`; `Current Runtime Freshness Verification`; `Roadmap-To-Work-Order Trace Matrix`; `Agent Handoff Contract Control Block`; `Reviewer Closure Conversion`; `Evidence Reuse And Encoding Plan`; `Public Export Disposition` |
| gateRunPurpose | confirmation and dispatch evidence after reading checker source; not first discovery |
| claimBoundary | exact no-commit UC-02 worker route and provider-free bounded proof |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance execution evidence; no public-sync authority.

## Claim Boundary

Passing UC-02 may prove only that the canonical registry-driven CF-076 through
CF-084 chain executed successfully in the recorded local environment and
evidence window. It does not prove provider governance, all CVF controls,
production, public readiness, scale, certification, or user value.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher/reviewer role |
| Provider or surface | local private provenance repository |
| Session or invocation | UC-02 work-order authoring, 2026-07-14 |
| Working directory | repository root |
| Command or tool surface | governed reads, rg, apply_patch, dispatch gates |
| Target paths | paired GC-018 baseline and this work order |
| Allowed scope source | operator continuation under UC-02 nextAllowedMove |
| Before status evidence | HEAD `a9507c1b0`; worktree clean before this two-file dispatch batch; UC-02 planned but undispatched |
| After status evidence | source-verified UC-02 dispatch packet |
| Diff evidence | dispatch changed set captured before commit |
| Approval boundary | packet authoring and bounded no-commit worker route |
| Claim boundary | no UC-02 execution during packet authoring |
| Agent type | dispatcher/reviewer |
| Invocation ID | system-chain-uc02-work-order-2026-07-14 |
| Expected manifest | paired GC-018 baseline and this work order |
| Actual changed set | paired GC-018 baseline and this work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |
