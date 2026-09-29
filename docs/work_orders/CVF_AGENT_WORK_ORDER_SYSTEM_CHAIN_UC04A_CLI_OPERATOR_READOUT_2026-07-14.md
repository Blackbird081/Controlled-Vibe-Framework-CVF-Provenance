# CVF Agent Work Order - System Chain UC-04A CLI Operator Readout

Memory class: FULL_RECORD

Status: CLOSED_BLOCKED_BOUNDED

docType: work_order

Work Order ID: SCLP-UC04A-T3

Date: 2026-07-14

dispatchBaseHead: `2970a6641`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: implementation/proof worker. Reviewer/closer is a separate role.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_SYSTEM_CHAIN_UC04A_CLI_OPERATOR_READOUT_2026-07-14.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

Base: capture `executionBaseHead` with `git rev-parse --short HEAD` at worker
start and require a clean worktree.

Current-time notes: selected owner is the existing autorun CLI. One proof
harness invocation may make exactly two local CLI sub-invocations: positive
`pre-dispatch` and expected-negative `pre-closure`. Zero retries and zero
provider calls.

Do-not-misread notes: do not edit the CLI, command catalog, checkers, tests,
hooks, roadmap, coverage, session, Web, provider, public, or runtime owners. Do
not treat aggregate counts as case identity. Do not commit or stage.

Required first actions: full-read this packet and paired baseline; source-
refresh the owner symbols; capture clean base; run pre-implementation; create
and pass focused mock-subprocess tests before the one real harness invocation.

Return contract: `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` with exact
changed paths, executionBaseHead, source refresh, test-before-run order, stable
case IDs, one harness/two CLI calls, receipts, diagnostic, zero provider calls,
and unchanged-HEAD evidence.

## Purpose

Implement and execute the smallest proof harness needed to decide whether the
current autorun CLI gives a local operator usable aggregate, per-check,
receipt, and meaningful failure readouts.

## Objective

Produce one current two-case receipt for the selected CLI owner without
changing that owner or implying Web, unified-checker, provider, or production
coverage.

Reviewer closure update: the one authorized harness invocation completed with
stable case identity. `negative_pre_closure` passed. `positive_pre_dispatch`
failed 73/75 because the dispatch manifest placed its focused test under the
protected `governance/compat` directory without a dispatch-time Core Guard
Self-Protection Authorization block. The CLI owner behaved correctly. This
attempt is closed blocked; no retry is authorized by this work order.

## Authority / Decision

Authority chain:

1. `docs/reference/system_chain/CVF_SYSTEM_CHAIN_LIVE_PROOF_AND_LEARNING_LOOP_STANDARD.md`
2. `docs/reference/system_chain/CVF_SYSTEM_CHAIN_LIVE_PROOF_COVERAGE.json`
3. `docs/roadmaps/CVF_SYSTEM_CHAIN_LIVE_PROOF_USE_CASE_ROADMAP_2026-07-14.md`
4. `docs/reviews/CVF_SYSTEM_CHAIN_UC03_CONTRACT_TO_RUNTIME_COMPLETION_2026-07-14.md`
5. paired UC-04A GC-018 baseline
6. this work order

UC-03 material commit `7a8f7268f` and session commit `2970a6641` release this
packet. Current CLI source controls every executable fact.

## Authority Chain

The order above is binding. Historical audits explain why CLI and Web are
separate; they do not replace current source.

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | dispatcher role | CLI-owner fidelity and dispatch gates |
| Worker | implementation/proof worker | exact manifest, focused tests, one harness invocation, two CLI calls, no commit |
| Reviewer/closer | reviewer/closer role | evidence review, closure, reverse projection, material commit |

## Required First Reads

| Source | Action |
|---|---|
| this work order and paired baseline | FULL_READ |
| live-proof standard, coverage ledger, and roadmap | FULL_READ |
| selected autorun CLI and focused tests | SOURCE_VERIFIED |
| accepted R90 Lane 5 audit | READ_FOR_BOUNDARY |
| ADIF-0032 | FULL_READ |
| retained live-run diagnostic standard | FULL_READ |

## Pre-Flight Checks

Dispatcher evidence is a clean worktree at `2970a6641`. Worker must capture a
clean `executionBaseHead`, recompute every Source Verification row, and run:

```text
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

Any contradiction stops before editing. Allowed-scope gate defects must be
repaired and rerun; scope expansion, retry, provider use, or owner mutation
returns to reviewer/orchestrator.

## Scope / Target / Owner Boundary

Worker may create only the four required paths in the Planned Worker
Fulfillment Manifest plus the conditional diagnostic. Existing CLI, command
catalog, checkers, tests, hooks, system-chain owners, roadmap, Catalog/GAP,
session, Web, provider, archive, and public paths are read-only.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| CLI prints one PASS or FAIL line per configured command | `governance/compat/run_agent_autorun_workflow_gate.py` | lines 72-76 | `_print_result` | autorun CLI | RUNTIME_BEHAVIOR | ACCEPT |
| CLI writes a structured PASS receipt only after all checks pass | `governance/compat/run_agent_autorun_workflow_gate.py` | lines 177-207 and 399-405 | `_write_receipt` | autorun receipt owner | RUNTIME_BEHAVIOR | ACCEPT |
| receipt retains phase context and one named result per configured check | `governance/compat/run_agent_autorun_workflow_gate.py` | lines 184-204 | `RECEIPT_SCHEMA` | autorun receipt schema | VALUE_SET | ACCEPT |
| pre-closure rejects an empty committed range | `governance/compat/run_agent_autorun_workflow_gate.py` | lines 334-341 | `_run_phase` | autorun CLI | RUNTIME_BEHAVIOR | ACCEPT |
| pre-closure reports dirty paths and blocks closure finality | `governance/compat/run_agent_autorun_workflow_gate.py` | lines 219-236 and 390-392 | `_closure_worktree_finality_failures` | autorun CLI | RUNTIME_BEHAVIOR | ACCEPT |
| CLI accepts phase, base, head, and receipt directory | `governance/compat/run_agent_autorun_workflow_gate.py` | lines 409-435 | `main` | autorun CLI argument parser | EXISTS | ACCEPT |
| focused owner tests cover the selected failure and result propagation | `governance/compat/test_run_agent_autorun_workflow_gate.py` | lines 166-207 and 267-295 | `test_closure_finality_blocks_dirty_stdout`; `test_pre_implementation_fails_when_aaf_helper_fails` | autorun focused test suite | EXISTS | ACCEPT |
| coverage requires current CLI proof before separate Web proof | `docs/reference/system_chain/CVF_SYSTEM_CHAIN_LIVE_PROOF_COVERAGE.json` | UC-04 and Evidence-to-Operator entries | `UC-04-EVIDENCE-TO-OPERATOR-SURFACE` | live-proof coverage ledger | VALUE_SET | ACCEPT |
| roadmap requires real CLI output, receipt path, usability, and one failure boundary | `docs/roadmaps/CVF_SYSTEM_CHAIN_LIVE_PROOF_USE_CASE_ROADMAP_2026-07-14.md` | tranche T3 / UC-04A | `T3 / UC-04A` | system-chain roadmap | VALUE_SET | ACCEPT |
| accepted audit proves current CLI output but separates Web coverage | `docs/audits/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_2026-07-10.md` | Lane 5, items (a)-(c) | `Evidence to operator surface` | accepted system-chain audit | VALUE_SET | ACCEPT |
| proof receipts must preserve distinct case identity | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0032.md` | remediation and prevention controls | `CVF_ADIF-0032` | ADIF registry | LITERAL_INVARIANT | ACCEPT |

## New Doc-Only Fields

| Field | Artifact | Purpose |
|---|---|---|
| `positive_pre_dispatch` | UC-04A proof receipt | stable positive case identity |
| `negative_pre_closure` | UC-04A proof receipt | stable negative case identity |
| `harnessInvocationCount` | UC-04A proof receipt | proves one harness call |
| `cliInvocationCount` | UC-04A proof receipt | proves exactly two CLI subprocess calls |
| `providerCallCount` | UC-04A proof receipt | records provider-free boundary |

These are proof-artifact fields only, not current runtime or canonical schema
fields.

## Current Runtime Freshness Verification

Fresh reads at dispatch base `2970a6641` verified every row above. Worker must
recompute source path, symbols, CLI argument choices, output markers, receipt
schema, focused tests, and roadmap boundary at execution base. Source drift
returns `BLOCKED_WITH_REASON` before editing or invoking.

## Execution Plan

1. Capture clean `executionBaseHead`; run pre-implementation.
2. Refresh every source row and preserve the CLI/Web split.
3. Create the Python proof runner and focused mock-subprocess tests.
4. Focused tests must validate command fidelity, stable case IDs, result
   parsing, receipt parsing, expected positive/negative exit codes, secret-safe
   diagnostics, exactly two subprocess calls, and rejection of missing or
   duplicate cases. No placeholder test body is permitted.
5. Run the focused test suite once. Stop on failure.
6. Invoke the proof runner exactly once. It must run the current CLI twice:
   - `positive_pre_dispatch`: `pre-dispatch`, explicit execution base/head,
     and a dedicated receipt directory under the declared evidence path;
   - `negative_pre_closure`: `pre-closure` with execution base as both range
     endpoints, while worker proof paths remain untracked.
7. Positive acceptance requires exit zero, named per-check PASS results,
   aggregate COMPLIANT, and a valid PASS receipt. Do not hard-code the current
   checker count; reconcile the printed and receipt denominators instead.
8. Negative acceptance requires nonzero exit and the exact non-empty committed
   range failure marker. Also record whether closure finality prints worker
   dirty paths; absence of dirty-path output is diagnostic, not a retry reason.
9. Write one two-case receipt and JSON `null` diagnostic on complete expected
   behavior; otherwise write one secret-safe diagnostic. Never retry.
10. Create the worker return from the required scaffold, run worker-return and
    reviewer-return gates, then stop with unchanged HEAD.

## Planned Worker Fulfillment Manifest

| Path | Ownership | Purpose |
|---|---|---|
| `scripts/run_cvf_system_chain_uc04a_cli_operator_readout_proof.py` | create | bounded two-call CLI proof runner and receipt validator |
| `governance/compat/test_run_cvf_system_chain_uc04a_cli_operator_readout_proof.py` | create | subprocess-free focused runner tests |
| `docs/reviews/evidence/system-chain-uc04a-cli-operator-readout-proof-2026-07-14.json` | create | two-case proof receipt with stable case IDs |
| `docs/reviews/CVF_SYSTEM_CHAIN_UC04A_CLI_OPERATOR_READOUT_WORKER_RETURN_2026-07-14.md` | create | no-commit worker return |

Conditional diagnostic path:
`docs/reviews/evidence/system-chain-uc04a-cli-operator-readout-proof-diagnostic-2026-07-14.json`.

Dedicated CLI PASS receipt directory:
`docs/reviews/evidence/system-chain-uc04a-cli-autorun-receipts-2026-07-14/`.
Its expected generated file is `pre-dispatch.json`; the directory and file are
part of allowed worker scope and must be listed in the return.

## Write Ownership

Worker owns only the exact manifest, conditional diagnostic, and dedicated
PASS receipt directory. Worker must not stage or commit. Reviewer owns paired
packet status, completion review, coverage, roadmap, Catalog/GAP disposition,
ADIF follow-up, material commit, and later session synchronization.

## Work-Order Fulfillment Manifest

Required artifacts are the four Planned Worker Fulfillment Manifest paths,
the conditional diagnostic, and the dedicated generated PASS receipt. All
other paths are forbidden. Required proof literals are
`positive_pre_dispatch`, `negative_pre_closure`, `harnessInvocationCount=1`,
`cliInvocationCount=2`, `retryCount=0`, and `providerCallCount=0`.

## Required Artifact Manifest

| Required artifact | Planned path | Final evidence | Status |
|---|---|---|---|
| proof runner | `scripts/run_cvf_system_chain_uc04a_cli_operator_readout_proof.py` | worker additive file | PASS |
| focused tests | `governance/compat/test_run_cvf_system_chain_uc04a_cli_operator_readout_proof.py` | 39/39 PASS | PASS |
| two-case receipt | `docs/reviews/evidence/system-chain-uc04a-cli-operator-readout-proof-2026-07-14.json` | positive FAIL; negative PASS | PASS |
| diagnostic | declared conditional diagnostic path | non-retryable packet gap | PASS |
| worker return | declared worker-return path | `BLOCKED_WITH_REASON` | PASS |
| generated positive PASS receipt | dedicated receipt directory | absent because positive aggregate failed | BLOCKED |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | local shell and current autorun CLI | exact proof manifest; no commit or owner mutation | focused tests, stdout summary, receipts, worker return | repository-local Python process only | IMPLEMENTED |
| `EXTERNAL_AGENT_CLI_MCP` | existing local CLI callable by a shell consumer | proof covers readout only; no remote access, authentication, mutation, MCP, or readiness claim | same bounded receipt and explicit claim boundary | no new adapter or MCP surface | DEFERRED_WITH_REASON |

## Evidence Requirements

Record execution base, refreshed source facts, focused test command/result,
proof command, stable case IDs, harness count one, CLI count two, retry count
zero, command fingerprints, exit codes, printed and receipt denominators,
aggregate markers, exact negative marker, dirty-finality observation, receipt
path/schema/status, provider count zero, diagnostic disposition, secret scan,
exact changed set, stage status, and unchanged HEAD. Do not retain raw
environment values or secrets.

## Acceptance Criteria

- AC-01: selected owner remains the current autorun CLI.
- AC-02: focused runner suite passes before the proof invocation and contains
  no placeholder body.
- AC-03: harness runs exactly once; CLI runs exactly twice; retry count is zero.
- AC-04: `positive_pre_dispatch` exits zero and retains named per-check PASS
  results plus aggregate COMPLIANT.
- AC-05: positive receipt exists at the dedicated path, uses the current
  receipt schema, reports PASS, and reconciles its check denominator.
- AC-06: `negative_pre_closure` exits nonzero and retains the non-empty
  committed-range failure marker; dirty-finality output is recorded.
- AC-07: both case IDs remain distinct in the final proof receipt.
- AC-08: provider/API/MCP call count is zero and UC-04B Web is untouched.
- AC-09: changed set is exact allowed scope with no existing owner mutation.
- AC-10: worker HEAD is unchanged, nothing is staged, and no commit exists.

## Fail Conditions

Source drift, unrelated dirty start, focused-test failure, placeholder test,
owner mutation, missing/duplicate case ID, second harness invocation, CLI call
count other than two, retry, unexpected positive failure, unexpected negative
success, missing PASS receipt, mismatched denominator, absent negative range
marker, provider use, Web work, secret leakage, unexpected path, or stronger
claim stops execution and returns evidence to reviewer.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only for the full expected two-case packet.
Return `BLOCKED_WITH_REASON` for every other result with one secret-safe
diagnostic and the smallest reviewer action. No worker retry is authorized.

## Operator Checkpoint

The selected local proof needs no additional operator checkpoint. Any retry,
new path, CLI owner edit, provider call, Web work, public action, or claim
expansion requires a fresh governed decision.

## Closure Checklist

| Closure item | Worker disposition |
|---|---|
| source verification refreshed | required in return |
| focused suite precedes proof | required in return |
| distinct case IDs retained | required in return |
| one harness, two CLI calls, zero retries | required in return |
| positive receipt and denominator reconciled | required in return |
| meaningful negative reason retained | required in return |
| exact allowed changed set | required in return |
| zero provider calls and no Web changes | required in return |
| HEAD unchanged, nothing staged, no commit | required in return |
| coverage, roadmap, Catalog/GAP, and ADIF reverse projection | reviewer-owned |

## Worker Autonomy / No-Question Rule

Worker proceeds autonomously for non-destructive work inside declared scope.
Allowed-scope machine-gate defects must be repaired and rerun. Worker stops for
source contradiction, unexpected CLI result, secret risk, retry need, owner
mutation, Web/provider work, or claim expansion and must not ask whether to
retry.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order control | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| real CLI output | current autorun owner only | two-case proof receipt | command fingerprint and captured markers | READY |
| receipt path | dedicated receipt directory | generated `pre-dispatch.json` | schema/status/denominator parser | READY |
| usability | per-check plus aggregate evidence | `positive_pre_dispatch` | named-result reconciliation | READY |
| one meaningful failure/readout | empty committed-range closure call | `negative_pre_closure` | nonzero exit and exact marker | READY |
| bounded aggregate and failure | one harness, two calls, zero retry | invocation ledger | exact counters | READY |
| separate Web | all Web paths forbidden | exact changed-set evidence | `git status --short` | READY |
| provider boundary | zero provider use | `providerCallCount` | receipt assertion | READY |
| reverse projection | reviewer owns closure updates | coverage/roadmap/Catalog-GAP/ADIF decision | reviewer closure diff | READY |

## Cost And Retry Control

Planned harness calls: one. Planned CLI calls: two. Evidence cases: two.
Worker retries: zero. Provider calls: zero. Any unexpected result ends worker
execution.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | one no-commit implementation/proof worker, then reviewer/closer |
| phase | UC-04A CLI proof harness, two CLI calls, and worker return |
| baseHeadFor(phase) | dispatchBaseHead=`2970a6641`; executionBaseHead=`WORKER_MUST_CAPTURE_AT_START`; closureBaseHead=`REVIEWER_TO_SET` |
| changedSetScope(phase) | exact Planned Worker Fulfillment Manifest, conditional diagnostic, and dedicated PASS receipt only |
| traceScope(phase, actor) | worker records source refresh, tests, case IDs, one harness, two CLI calls, receipts, diagnostic, provider count, diff, and HEAD; reviewer owns closure |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer owns material commit |
| crossBatchIsolation | CLEAN_WORKTREE_CONFIRMED at dispatch; all non-manifest surfaces read-only |
| nextMoveSurfaces | reviewer updates coverage, roadmap, Catalog/GAP, ADIF decision, session state, handoff, and memory only after accepted completion |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_SYSTEM_CHAIN_UC04A_CLI_OPERATOR_READOUT_COMPLETION_2026-07-14.md` |
| reviewerOwnedClosurePaths | completion review; paired baseline/work-order status; coverage ledger; system-chain README; roadmap; Catalog/GAP decision; ADIF decision; active session sources |
| closureOwner | reviewer/closer role |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_SYSTEM_CHAIN_UC04A_CLI_OPERATOR_READOUT_WORKER_RETURN_2026-07-14.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Skeleton command: `python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_SYSTEM_CHAIN_UC04A_CLI_OPERATOR_READOUT_WORKER_RETURN_2026-07-14.md --title "CVF System Chain UC-04A CLI Operator Readout Worker Return" --profile WORKER_RETURN_FULL_GATE_V1`

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake route | operator-directed system-chain proof continuation |
| canonical route mode | `SINGLE_AGENT_SINGLE_ROLE` |
| Selected role route | dispatcher -> no-commit worker -> reviewer/closer |
| scope classification | bounded local CLI operator-readout proof |
| risk sensitivity | R1 provider-free local subprocess execution |
| escalation condition | source drift, unexpected result, secret risk, retry need, owner mutation, provider/Web work, or claim expansion |
| Dispatcher role | dispatcher role |
| Worker route | `WORKER_MUST_NOT_COMMIT` |
| Reviewer/closer route | reviewer/closer role after return |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | current local CLI proof and source verification |
| Matching local-view guard | `governance/compat/check_work_order_dispatch_quality.py` |
| Owner surface | current autorun CLI and system-chain coverage ledger |
| Disposition | BLOCKED_UNTIL_CVF_PROOF at dispatch; reviewer accepts only fresh two-case receipt |
| Claim boundary | chat, historical source audit, and source existence are not current UC-04A operational proof |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: this is an internal CLI proof and does not scan or
absorb an external or legacy corpus.

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: current operator-surface proof must re-read and invoke the
active CLI because the retained R90 source audit is not a current invocation

priorVerificationArtifact: `docs/audits/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_2026-07-10.md`

priorVerificationAnchor: accepted Lane 5 CLI/Web distinction; current CLI
source and behavior must still be recomputed

freshRecomputeRequired: yes; source existence does not prove current CLI output

unicodePathHandling: literal repository paths and explicit UTF-8 readers; new
governed prose remains ASCII

extractedTextAuthority: N/A with reason: no extraction or OCR input

## Provider Memory Authority Boundary

Provider-specific memory and IDE summaries are execution aids only. They are
not source authority. Every executable claim comes from the Source
Verification Block and fresh worker recomputation.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | one local autorun CLI operator-readout proof |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT through the generated CLI PASS receipt and UC-04A two-case receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT through one harness invocation and two CLI calls |
| invocationBoundary | one harness, two CLI calls, two stable case IDs, zero retry, zero provider calls |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, external CLI, MCP, or Web interception claim |
| claimLanguage | selected local CLI exposed or failed to expose the recorded readouts in the evidence window |
| forbiddenExpansion | no UC-04B Web, unified checker inventory, external-agent readiness, provider, public, production, scale, certification, or user-value claim |

## Verification Commands

```text
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python -m pytest governance/compat/test_run_cvf_system_chain_uc04a_cli_operator_readout_proof.py -q
python scripts/run_cvf_system_chain_uc04a_cli_operator_readout_proof.py --execution-base <executionBaseHead> --json-output docs/reviews/evidence/system-chain-uc04a-cli-operator-readout-proof-2026-07-14.json --diagnostic-output docs/reviews/evidence/system-chain-uc04a-cli-operator-readout-proof-diagnostic-2026-07-14.json --receipt-dir docs/reviews/evidence/system-chain-uc04a-cli-autorun-receipts-2026-07-14
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return --base <executionBaseHead> --head HEAD --enforce
git diff --check
git status --short
```

## Review Gate

Reviewer independently verifies source freshness, test quality including no
placeholder bodies, stable case identity, exact command fidelity, one harness
and two CLI calls, positive receipt integrity, negative reason, denominator
reconciliation, zero provider calls, exact changed set, and unchanged worker
HEAD. Only reviewer may update system-chain owners.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`system-chain-live-proof`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class system-chain-live-proof --role dispatcher --lifecycle-phase pre-dispatch --max-results 20 --json`

Returned defects: NONE_RETURNED

## Commit Prompt Readiness

| Field | Value |
|---|---|
| workerCommitPrompt | FORBIDDEN |
| reviewerMaterialCommit | required only after accepted review |
| sessionSyncCommit | separate following material completion |
| changedSetEvidence | exact manifest plus `git diff --name-status` and `git status --short` |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --help` |
| generatedProfile | work-order full dispatch |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | manually source-verified against current autorun CLI and accepted SCLP pattern |
| checkerReadAheadConfirmation | applicable checker sources and literal-format gotchas read before authoring |
| docOnlyNewFields | stable case and invocation-counter fields listed above |
| claimBoundary | dispatch packet only; no UC-04A execution during authoring |

## Foundation Storage Layout Block

The existing autorun CLI remains the executable owner. The new runner is
proof-only orchestration, its focused test is compatibility-owned, and dated
evidence remains under reviews. No new stable runtime module, CLI contract,
registry, provider, Web, MCP, or public surface is created.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; `Source Verification Block`; `Current Runtime Freshness Verification`; `Work-Order Fulfillment Manifest`; `Roadmap-To-Work-Order Trace Matrix`; `Agent Handoff Contract Control Block`; `Reviewer Closure Conversion`; `Worker Return Packet Shape Contract`; `Evidence Reuse And Encoding Plan`; `Public Export Disposition` |
| gateRunPurpose | confirmation after complete CLI-owner and output inventory; not first discovery |
| claimBoundary | exact no-commit UC-04A provider-free local CLI proof |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance execution evidence; no public-sync authority.

## Claim Boundary

A two-case PASS may prove only that the selected autorun CLI exposed its
retained aggregate, per-check, PASS-receipt, and selected closure-failure
readouts in one local environment and evidence window. It does not prove
UC-04B Web, a unified all-checker operator inventory beyond the invoked phase,
external-agent readiness, provider governance, production, public readiness,
scale, certification, or user value.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | paired UC-04A GC-018 | `CLOSED_BLOCKED_BOUNDED` | PASS |
| Work order status | this work order | `CLOSED_BLOCKED_BOUNDED` | PASS |
| Completion or reviewer artifact | declared completion review | reviewer accepted deterministic packet blocker | PASS |
| Roadmap state | system-chain live-proof roadmap | UC-04A recovery packet next | PASS |
| Registry JSON | live-proof coverage ledger | CLI proof partial blocked | PASS |
| Registry Markdown | system-chain README and Catalog/GAP decision | packet blocker recorded; no architecture gap | PASS |
| External evidence digest | N/A with reason: no external evidence consumed | repository/runtime evidence only | N/A with reason |
| System loop interlock | fresh UC-04A receipt | positive FAIL 73/75; negative PASS; stable case IDs | PASS |
| Session continuity | active session state | separate post-material synchronization | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| harness invocation | exactly one | 1 | PASS |
| CLI calls | exactly two | 2 | PASS |
| positive aggregate | PASS | FAIL 73/75 | BLOCKED |
| positive receipt | present | absent by fail-closed receipt behavior | BLOCKED |
| negative range/finality | PASS | PASS | PASS |
| stable case IDs | two distinct | two distinct | PASS |
| retry count | 0 | 0 | PASS |
| provider calls | 0 | 0 | PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher/reviewer role |
| Provider or surface | local private provenance repository |
| Session or invocation | SCLP-UC04A-T3 work-order authoring, 2026-07-14 |
| Working directory | repository root |
| Command or tool surface | governed reads, source search, apply_patch, ADIF resolver, dispatch gates |
| Target paths | paired GC-018 baseline and this work order |
| Allowed scope source | active nextAllowedMove at session commit `2970a6641` |
| Before status evidence | clean worktree at HEAD `2970a6641` |
| After status evidence | source-verified UC-04A dispatch packet |
| Diff evidence | two-file dispatch diff before commit |
| Approval boundary | packet authoring and one later no-commit worker |
| Claim boundary | no UC-04A execution, Web, provider, public, coverage, GAP, or session edit |
| Agent type | dispatcher/reviewer |
| Invocation ID | system-chain-uc04a-t3-work-order-2026-07-14 |
| Expected manifest | paired GC-018 baseline and work order |
| Actual changed set | paired GC-018 baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |
