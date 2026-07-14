# CVF Agent Work Order - System Chain UC-04A-R1 Positive CLI Recovery

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: work_order

Work Order ID: SCLP-UC04A-R1

Date: 2026-07-14

dispatchBaseHead: `ed6561581`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: implementation/proof worker. Reviewer/closer is a separate role.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_SYSTEM_CHAIN_UC04A_R1_POSITIVE_CLI_RECOVERY_2026-07-14.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

Base: capture `executionBaseHead` at worker start and require a clean worktree.

Current-time notes: run the committed 39-test suite, then invoke the current
autorun CLI directly exactly once in `pre-dispatch` mode. Do not invoke the
retained proof runner because it performs two calls. Do not rerun the accepted
negative case. Zero retry and zero provider calls.

Do-not-misread notes: existing runner/test/CLI/checkers are read-only. This is
not permission to repair or tune a guard. Do not stage or commit.

Required first actions: full-read the paired packet and accepted blocked
closure; capture clean execution base; refresh the Source Verification Block;
run pre-implementation; then run the committed 39-test suite before the one
direct CLI call.

Return contract: `COMPLETE_PENDING_REVIEW` only when the positive call and
receipt pass; otherwise `BLOCKED_WITH_REASON`. Record exact paths, counts,
receipt, retained-negative citation, and unchanged HEAD.

## Purpose

Complete the missing positive half of UC-04A with one direct CLI call while
reusing the accepted negative evidence and committed test foundation.

## Objective

Produce one current `pre-dispatch` PASS receipt with usable aggregate and
per-check readout, without changing any owner or repeating negative/provider
work.

## Authority / Decision

Authority chain:

1. live-proof standard and coverage ledger;
2. system-chain live-proof roadmap;
3. accepted UC-04A blocked completion review;
4. `ADIF-0033`;
5. paired R1 GC-018 baseline;
6. this work order.

Material commit `da93a4b73` supplies accepted blocker closure and committed
runner/test evidence. Session commit `ed6561581` releases R1 packet authoring.

## Authority Chain

Current CLI source controls executable facts. The retained negative receipt is
accepted evidence and must not be regenerated.

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | dispatcher role | source fidelity, protected-path classification, dispatch gates |
| Worker | implementation/proof worker | tests, one direct CLI call, receipt, return, no commit |
| Reviewer/closer | reviewer/closer role | evidence decision, reverse projection, material commit |

## Required First Reads

| Source | Action |
|---|---|
| this work order and paired R1 baseline | FULL_READ |
| accepted UC-04A completion and retained receipt/diagnostic | FULL_READ |
| current autorun CLI | SOURCE_VERIFIED |
| committed runner and focused tests | SOURCE_VERIFIED |
| live-proof roadmap and coverage ledger | FULL_READ |
| `ADIF-0033` and live-run diagnostic standard | FULL_READ |

## Pre-Flight Checks

Capture a clean `executionBaseHead`. Run pre-implementation before any output
creation. Refresh every Source Verification row. Any contradiction stops
before the CLI call.

## Scope / Target / Owner Boundary

Worker may create only:

- `docs/reviews/evidence/system-chain-uc04a-r1-positive-cli-receipts-2026-07-14/pre-dispatch.json` through the CLI;
- `docs/reviews/CVF_SYSTEM_CHAIN_UC04A_R1_POSITIVE_CLI_RECOVERY_WORKER_RETURN_2026-07-14.md`;
- conditional `docs/reviews/evidence/system-chain-uc04a-r1-positive-cli-recovery-diagnostic-2026-07-14.json` only if blocked.

All existing files are read-only.

## Core Guard Self-Protection Authorization

Protected-path reuse inputs: the committed proof runner and focused test at
material commit `da93a4b73`. They may be read and tested but not changed.

Authorized protected-path mutations: NONE.

Operator authority: operator continuation plus active R1 next move.

Rollback boundary: reviewer may remove only new R1 receipt/return/diagnostic
artifacts. Retained closure evidence must remain unchanged.

Not authorized: no protected owner mutation or new protected path.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| CLI prints named per-check result lines | `governance/compat/run_agent_autorun_workflow_gate.py` | lines 72-76 | `_print_result` | autorun CLI | RUNTIME_BEHAVIOR | ACCEPT |
| CLI writes PASS receipt only on aggregate success | `governance/compat/run_agent_autorun_workflow_gate.py` | lines 177-207 and 399-405 | `_write_receipt` | autorun receipt owner | RUNTIME_BEHAVIOR | ACCEPT |
| receipt schema literal is current | `governance/compat/run_agent_autorun_workflow_gate.py` | line 30 | `RECEIPT_SCHEMA` | autorun receipt schema | VALUE_SET | ACCEPT |
| CLI supports explicit phase/base/head/receipt directory | `governance/compat/run_agent_autorun_workflow_gate.py` | lines 409-435 | `main` | autorun CLI parser | EXISTS | ACCEPT |
| committed runner would make both positive and negative calls and therefore must not be invoked here | `scripts/run_cvf_system_chain_uc04a_cli_operator_readout_proof.py` | lines 158-240 | `run_proof` | retained proof runner | RUNTIME_BEHAVIOR | ACCEPT |
| focused suite covers stable identity, counts, parsing, and secret safety | `governance/compat/test_run_cvf_system_chain_uc04a_cli_operator_readout_proof.py` | 39 test declarations | `TestCaseIdentity`; `TestInvocationCounts`; `TestReceiptParsing` | retained focused suite | EXISTS | ACCEPT |
| negative case is accepted and positive-only recovery is required | `docs/reviews/CVF_SYSTEM_CHAIN_UC04A_CLI_OPERATOR_READOUT_COMPLETION_2026-07-14.md` | Decision and Recommendation | `CLOSED_BLOCKED_BOUNDED` | accepted reviewer closure | VALUE_SET | ACCEPT |
| coverage remains recovery-required | `docs/reference/system_chain/CVF_SYSTEM_CHAIN_LIVE_PROOF_COVERAGE.json` | UC-04 entry | `BLOCKED_BOUNDED_RECOVERY_REQUIRED` | coverage ledger | VALUE_SET | ACCEPT |
| roadmap names UC-04A-R1 packet authoring next | `docs/roadmaps/CVF_SYSTEM_CHAIN_LIVE_PROOF_USE_CASE_ROADMAP_2026-07-14.md` | Current Next Action | `UC-04A-R1` | live-proof roadmap | VALUE_SET | ACCEPT |
| protected planned outputs require dispatch classification | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0033.md` | Remediation | `ADIF-0033` | ADIF registry | LITERAL_INVARIANT | ACCEPT |

## New Doc-Only Fields

| Field | Artifact | Purpose |
|---|---|---|
| `positive_pre_dispatch` | worker return evidence ledger | stable positive-case identity |
| `cliInvocationCount` | worker return evidence ledger | prove exactly one direct call |
| `retainedNegativeInvocationCount` | worker return evidence ledger | prove zero negative reruns |
| `retryCount` | worker return evidence ledger | prove zero retry |
| `providerCallCount` | worker return evidence ledger | prove provider-free boundary |

These are evidence fields only, not runtime schema additions.

## Current Runtime Freshness Verification

Dispatcher refreshed all source rows at `ed6561581`. Worker must recompute
them at execution base. Missing or changed source returns blocked before call.

## Execution Plan

1. Capture clean execution base and run pre-implementation.
2. Refresh sources and verify no protected-path mutation is planned.
3. Run the committed focused suite once; require 39/39 PASS.
4. Invoke `run_agent_autorun_workflow_gate.py` directly exactly once with
   phase `pre-dispatch`, base/head equal to execution base, and the dedicated
   R1 receipt directory.
5. Parse stdout and receipt. Require exit zero, aggregate COMPLIANT, named PASS
   results, current receipt schema/status, and matching nonzero denominators.
6. Cite the retained negative receipt and closure without invoking runner or
   negative CLI path.
7. Create worker return, run the required return gates, and stop. On any
   unexpected result, write one secret-safe diagnostic and do not retry.

## Planned Worker Fulfillment Manifest

| Path | Ownership | Purpose |
|---|---|---|
| `docs/reviews/evidence/system-chain-uc04a-r1-positive-cli-receipts-2026-07-14/pre-dispatch.json` | create through CLI | positive PASS receipt |
| `docs/reviews/CVF_SYSTEM_CHAIN_UC04A_R1_POSITIVE_CLI_RECOVERY_WORKER_RETURN_2026-07-14.md` | create | no-commit worker return |
| conditional R1 diagnostic path declared above | create only on block | secret-safe diagnosis |

## Write Ownership

Worker owns only the manifest. Reviewer owns packet status, completion review,
coverage, roadmap, Catalog/GAP/ADIF disposition, commit, and session sync.

## Work-Order Fulfillment Manifest

Required outputs are the positive receipt and worker return; diagnostic is
conditional. Required literals are `positive_pre_dispatch`,
`cliInvocationCount=1`, `retainedNegativeInvocationCount=0`, `retryCount=0`,
and `providerCallCount=0`.

## Required Artifact Manifest

| Required artifact | Planned path | Required evidence | Status |
|---|---|---|---|
| positive PASS receipt | declared R1 receipt path | current schema, PASS, nonzero denominator | REQUIRED |
| worker return | declared R1 worker-return path | pending-review disposition and full evidence | REQUIRED |
| diagnostic | declared conditional path | only on blocked outcome | N/A with reason: absent on expected PASS |
| retained negative | existing UC-04A proof receipt and completion | citation only; zero invocation | REUSED |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | local shell and autorun CLI | one direct positive call, no owner mutation | stdout, PASS receipt, return | repository-local process | IMPLEMENTED |
| `EXTERNAL_AGENT_CLI_MCP` | existing local CLI | no remote/MCP/readiness claim | same bounded receipt | no new adapter | DEFERRED_WITH_REASON |

## Evidence Requirements

Record execution base, source refresh, exact 39/39 test command, exact direct
CLI command, command fingerprint, one call, zero retry/negative/provider calls,
exit zero, named results, aggregate COMPLIANT, printed and receipt denominators,
receipt path/schema/status, retained negative citation, exact changed set,
secret scan, unchanged HEAD, no stage, and no commit.

## Acceptance Criteria

- AC-01: clean execution base and fresh source verification.
- AC-02: retained focused suite passes 39/39 before CLI invocation.
- AC-03: exactly one direct positive CLI call and no runner invocation.
- AC-04: positive call exits zero with named PASS lines and COMPLIANT.
- AC-05: PASS receipt is valid and denominator reconciles.
- AC-06: retained negative evidence is cited with zero rerun.
- AC-07: zero retry/provider calls and no Web/protected mutation.
- AC-08: exact manifest only; HEAD unchanged; nothing staged; no commit.

## Fail Conditions

Dirty start, source drift, focused-test failure, protected diff, runner or
negative invocation, CLI call count other than one, retry, nonzero exit,
missing COMPLIANT/readout/receipt, denominator mismatch, provider/Web work,
secret leakage, unexpected path, staging, commit, or stronger claim blocks.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only for full PASS evidence. Otherwise return
`BLOCKED_WITH_REASON` with one diagnostic and no retry.

## Operator Checkpoint

No additional checkpoint for the authorized local positive call. Retry,
protected mutation, provider/Web/public work, or claim expansion needs a fresh
decision.

## Closure Checklist

| Closure item | Worker disposition |
|---|---|
| source verification refreshed | required |
| retained suite 39/39 before call | required |
| one direct positive call | required |
| valid PASS receipt and reconciled denominator | required |
| retained negative cited, not invoked | required |
| zero retry/provider and no Web/protected changes | required |
| exact changed set, unchanged HEAD, no stage/commit | required |
| coverage/roadmap/Catalog-GAP/ADIF/session projection | reviewer-owned |

## Worker Autonomy / No-Question Rule

Proceed autonomously inside scope. Any unexpected result stops without retry.
Do not ask whether to modify a guard, rerun, or broaden scope.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order control | Output artifact or field | Verification | Status |
|---|---|---|---|---|
| positive CLI proof | one direct pre-dispatch call | PASS receipt | stdout/receipt parser | READY |
| retain negative | zero negative invocation | retained citation | invocation ledger | READY |
| cost control | one call, zero retry/provider | counters | worker return | READY |
| separate Web | Web forbidden | exact changed set | git status | READY |
| packet learning | protected inputs read-only | zero protected diff | git diff | READY |

## Cost And Retry Control

Focused test command: one. CLI calls: one. Negative calls: zero. Retries: zero.
Provider calls: zero.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | one no-commit proof worker, then reviewer/closer |
| phase | UC-04A-R1 positive-only CLI recovery |
| baseHeadFor(phase) | dispatchBaseHead=`ed6561581`; executionBaseHead=`WORKER_MUST_CAPTURE_AT_START`; closureBaseHead=`REVIEWER_TO_SET` |
| changedSetScope(phase) | exact R1 receipt, return, and conditional diagnostic |
| traceScope(phase, actor) | worker records sources, test, one call, receipt, retained negative, counts, diff, HEAD; reviewer closes |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer owns material commit |
| crossBatchIsolation | CLEAN_WORKTREE_CONFIRMED; all existing files read-only |
| nextMoveSurfaces | reviewer updates coverage, roadmap, Catalog/GAP/ADIF decision and session only after acceptance |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_SYSTEM_CHAIN_UC04A_R1_POSITIVE_CLI_RECOVERY_COMPLETION_2026-07-14.md` |
| reviewerOwnedClosurePaths | completion review; paired packet status; coverage; system-chain README; roadmap; Catalog/GAP/ADIF decision; session sources |
| closureOwner | reviewer/closer role |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_SYSTEM_CHAIN_UC04A_R1_POSITIVE_CLI_RECOVERY_WORKER_RETURN_2026-07-14.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake route | operator-directed system-chain recovery |
| canonical route mode | `SINGLE_AGENT_SINGLE_ROLE` |
| Selected role route | dispatcher -> no-commit worker -> reviewer/closer |
| scope classification | positive-only local CLI proof |
| risk sensitivity | R1 provider-free local subprocess |
| escalation condition | source drift, unexpected result, retry/protected/provider/Web need |
| Dispatcher role | dispatcher role |
| Worker route | `WORKER_MUST_NOT_COMMIT` |
| Reviewer/closer route | reviewer/closer after return |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | current local CLI proof and source verification |
| Matching local-view guard | `governance/compat/check_work_order_dispatch_quality.py` |
| Owner surface | autorun CLI and coverage ledger |
| Disposition | BLOCKED_UNTIL_CVF_PROOF at dispatch |
| Claim boundary | retained negative plus source existence do not prove the positive path |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: internal CLI recovery; no external or legacy corpus.

## Evidence Reuse And Encoding Plan

verificationMode: REUSE_PRIOR_VERIFICATION

priorVerificationArtifact: `docs/reviews/CVF_SYSTEM_CHAIN_UC04A_CLI_OPERATOR_READOUT_COMPLETION_2026-07-14.md`

priorVerificationAnchor: retained negative result and packet-gap diagnosis at material commit `da93a4b73`

freshRecomputeRequired: yes; current positive CLI behavior and receipt must be recomputed once

unicodePathHandling: literal repository paths and UTF-8-safe readers; new governed prose is ASCII

extractedTextAuthority: N/A with reason: no extraction or OCR input

## Provider Memory Authority Boundary

Provider memory and chat are not authority. Use current sources and governed
retained evidence only.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | one positive local autorun CLI readout |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT only if generated PASS receipt validates |
| actionEvidence | ACTION_EVIDENCE_PRESENT through exactly one direct CLI call |
| invocationBoundary | one positive call, zero negative/retry/provider calls |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, MCP, or Web interception claim |
| claimLanguage | selected local CLI exposed the recorded positive readout in one evidence window |
| forbiddenExpansion | no Web, unified inventory, external readiness, provider, public, production, scale, certification, or user-value claim |

## Verification Commands

```text
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python -m pytest governance/compat/test_run_cvf_system_chain_uc04a_cli_operator_readout_proof.py -q
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base <executionBaseHead> --head <executionBaseHead> --receipt-dir docs/reviews/evidence/system-chain-uc04a-r1-positive-cli-receipts-2026-07-14
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_run_cvf_system_chain_uc04a_cli_operator_readout_proof.py
python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return --base <executionBaseHead> --head HEAD --enforce
git diff --check
git status --short --untracked-files=all
```

The direct positive CLI command is execution proof, not the dispatcher's
packet-authoring pre-dispatch gate.

## Review Gate

Reviewer verifies source freshness, 39/39 tests before call, exactly one direct
positive call, valid receipt and denominator, retained negative citation, zero
negative/retry/provider calls, exact changed set, and unchanged HEAD.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`system-chain-live-proof`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class system-chain-live-proof --role dispatcher --lifecycle-phase pre-dispatch --surface-selector governance/compat --max-results 20 --json`

Returned defects: NONE_RETURNED

Mandatory predecessor learning applied: `ADIF-0033`.

## Commit Prompt Readiness

| Field | Value |
|---|---|
| workerCommitPrompt | FORBIDDEN |
| reviewerMaterialCommit | only after accepted review |
| sessionSyncCommit | separate after material completion |
| changedSetEvidence | exact manifest plus git diff/status |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --help` |
| generatedProfile | protected-path-aware work-order dispatch |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | narrowed from accepted original packet and blocked completion |
| checkerReadAheadConfirmation | guard orientation, checker sources, template, and literal gotchas read before writing |
| docOnlyNewFields | evidence-only counters listed above |
| claimBoundary | dispatch packet only; no execution during authoring |

## Foundation Storage Layout Block

The existing CLI remains executable owner. Existing runner/test are retained
read-only proof infrastructure. New dated evidence stays under reviews. No new
stable module, adapter, registry, provider, Web, MCP, or public surface.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_closure_packaging_preflight.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; `Core Guard Self-Protection Authorization`; `Source Verification Block`; `Work-Order Fulfillment Manifest`; `Roadmap-To-Work-Order Trace Matrix`; `Agent Handoff Contract Control Block`; `Reviewer Closure Conversion`; `Worker Return Packet Shape Contract`; `Evidence Reuse And Encoding Plan`; `Public Export Disposition` |
| gateRunPurpose | confirmation after full source/protected-path classification; not first discovery |
| claimBoundary | exact no-commit positive-only recovery |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance recovery; no public-sync authority.

## Claim Boundary

PASS can complete only bounded UC-04A CLI evidence when combined with retained
negative evidence. It cannot prove UC-04B Web, every checker surface, external
agent readiness, provider governance, production, public readiness, scale,
certification, or user value.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher/reviewer role |
| Provider or surface | local private provenance repository |
| Session or invocation | SCLP-UC04A-R1 work-order authoring, 2026-07-14 |
| Working directory | repository root |
| Command or tool surface | governed reads, source search, apply_patch, ADIF resolver, dispatch gates |
| Target paths | paired R1 baseline and this work order |
| Allowed scope source | active nextAllowedMove at session commit `ed6561581` |
| Before status evidence | clean worktree at HEAD `ed6561581` |
| After status evidence | source-verified positive-only recovery packet |
| Diff evidence | two-file packet diff before commit |
| Approval boundary | packet authoring and one later no-commit positive CLI call |
| Claim boundary | no execution, Web, provider, public, coverage, GAP, or session edit |
| Agent type | dispatcher/reviewer |
| Invocation ID | system-chain-uc04a-r1-work-order-2026-07-14 |
| Expected manifest | paired R1 baseline and work order |
| Actual changed set | paired R1 baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |
