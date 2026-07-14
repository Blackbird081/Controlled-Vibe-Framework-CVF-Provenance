# CVF GC-018 System Chain UC-03 Contract-To-Runtime Representative Path

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: gc018_baseline

Date: 2026-07-14

Risk classification: R1

## Purpose

Authorize one bounded, provider-free proof of a representative active
caller-backed Contract-to-Runtime route for system-chain use case UC-03.

## Authorization / Decision

The system-chain roadmap at material commit `ed4052a27` makes UC-03 packet
authoring the next move after UC-02 and its renderer repair closed. Fresh source
verification selects GC-011 because `CvfSdk` constructs and calls
`PipelineOrchestrator` through an existing exported SDK route. GC-009 and
GC-010 remain excluded because no non-test production caller or active package
export is proven.

## Decision

Authorize `SCLP-UC03-T2` for one no-commit worker. The worker may create a
bounded proof harness and invoke it once after focused tests pass. Acceptance
requires one positive SDK route and one fail-closed negative route, a complete
receipt, zero provider calls, and no runtime-owner mutation.

## Scope / Target / Owner Boundary

Target: the current GC-011 route from the exported `CvfSdk` owner into
`PipelineOrchestrator`. The worker may create only the proof runner, focused
test, one receipt, one diagnostic, and one worker return named by the paired
work order. Existing SDK, orchestrator, package, tests, system-chain map,
coverage ledger, roadmap, Catalog/GAP, session, provider, and public surfaces
are read-only.

## Design Control Gate

| Control | Decision |
|---|---|
| Representative row | GC-011 only |
| Active caller | `CvfSdk` constructs and invokes `PipelineOrchestrator` |
| Positive case | public `runReferenceGovernedLoop` reaches governed terminal success |
| Negative case | governed SDK-created pipeline is blocked from BUILD without PLAN evidence |
| Invocation ceiling | one proof-run invocation; zero worker retries |
| Provider boundary | zero provider/API/MCP calls |
| Runtime mutation | forbidden; proof harness only |
| Excluded rows | GC-009 and GC-010 remain invocation-unproven |
| Closure owner | reviewer/closer only |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| GC-011 has a current non-test caller in the SDK | `EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/governance/guard_runtime/sdk/cvf.sdk.ts` | line 132 | `PipelineOrchestrator` | `CvfSdk` constructor | RUNTIME_BEHAVIOR | ACCEPT |
| SDK exposes a public full governed-loop method | `EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/governance/guard_runtime/sdk/cvf.sdk.ts` | lines 189-229 | `runReferenceGovernedLoop` | `CvfSdk` | EXISTS | ACCEPT |
| SDK action handlers invoke pipeline create, artifact, advance, and complete operations | `EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/governance/guard_runtime/sdk/cvf.sdk.ts` | lines 317, 364, 449, 503 | `bootstrapExtensionBridge` | `CvfSdk` | RUNTIME_BEHAVIOR | ACCEPT |
| orchestrator owns pipeline creation and phase advancement | `EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/governance/guard_runtime/pipeline.orchestrator.ts` | lines 147 and 191 | `createPipeline`; `advancePhase` | `PipelineOrchestrator` | EXISTS | ACCEPT |
| governed BUILD transition validates required evidence before advancing | `EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/governance/guard_runtime/pipeline.orchestrator.ts` | lines 646-665 | `validateControlBoundary` | `PipelineOrchestrator` | RUNTIME_BEHAVIOR | ACCEPT |
| existing SDK test exercises the public governed loop end to end | `EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/tests/sdk.test.ts` | lines 366-390 | `runReferenceGovernedLoop` | SDK test suite | EXISTS | ACCEPT |
| package test command uses Vitest | `EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/package.json` | scripts section, line 8 | `test` | npm package scripts | VALUE_SET | ACCEPT |
| canonical map names GC-011 as invoked through the SDK caller | `docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json` | `CONTRACT_TO_RUNTIME` lane | `invokedBy` | system-chain map | VALUE_SET | ACCEPT |
| UC-03 requires one active caller-backed representative path | `docs/reference/system_chain/CVF_SYSTEM_CHAIN_LIVE_PROOF_COVERAGE.json` | UC-03 and `CONTRACT_TO_RUNTIME` entries | `UC-03-CONTRACT-TO-RUNTIME-REPRESENTATIVE-PATH` | live-proof coverage ledger | VALUE_SET | ACCEPT |
| GC-009 and GC-010 have no proven production caller | `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` | GC-009 and GC-010 rows | `GC-009`; `GC-010` | governance control matrix | LITERAL_INVARIANT | ACCEPT |
| failed live runs require diagnosis before rerun | `docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md` | diagnostic fields and retry discipline | `Live Run Diagnostic Record` | retained diagnostic standard | LITERAL_INVARIANT | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Dispatch control | Evidence requirement | Disposition |
|---|---|---|---|
| one representative active caller path | select GC-011 SDK route | source chain plus current receipt | READY |
| focused negative | missing-PLAN BUILD rejection | negative case in receipt | READY |
| current invocation | one proof runner call | invocation count and timestamp | READY |
| no unsupported caller claim | exclude GC-009 and GC-010 | exact claim boundary | READY |
| learning reverse projection | reviewer-owned after acceptance | coverage, roadmap, Catalog/GAP review | READY |
| UC-04 remains held | no operator-surface work | exact changed-set review | READY |

## Cost And Retry Control

Proof-run invocation ceiling: one. Evidence-case denominator: two. Provider
calls: zero. Worker retries: zero. A failed or unclear invocation stops with a
secret-safe diagnostic for reviewer disposition.

## Acceptance Criteria

- Fresh source verification still proves the GC-011 SDK caller chain.
- Focused proof-runner tests pass before the proof invocation.
- The proof runner is invoked exactly once.
- Positive case enters through `CvfSdk.runReferenceGovernedLoop` and records
  terminal workflow and pipeline success.
- Negative case uses an SDK-created governed pipeline and proves BUILD is not
  entered without PLAN evidence.
- Receipt reports two of two cases passing, one call, zero retries, and zero
  provider calls.
- Existing runtime, test, package, map, coverage, roadmap, Catalog/GAP,
  session, provider, and public owners remain unchanged.
- Worker returns with unchanged HEAD, nothing staged, and no commit.

## Evidence / Verification

Dispatch evidence is the current source chain, the existing E2E test, clean
base `6886a825c`, and passing pre-dispatch gates. Worker evidence is focused
tests, one proof receipt, diagnostic disposition, exact changed-set evidence,
secret-safe output, and unchanged HEAD.

## Fail Conditions

Missing or changed caller, direct orchestrator-only positive proof, runtime
owner mutation, focused-test failure, more than one proof invocation, any
retry, incomplete two-case denominator, provider call, secret leakage,
unexpected path, GC-009/GC-010 promotion, UC-04 work, or expanded claim stops
the tranche.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| UC-02 and renderer repair accepted | material commits `9173af70b` and `36aefceab` | SATISFIED |
| roadmap reconciled to UC-03 packet next | material commit `ed4052a27` | SATISFIED |
| session authorizes packet authoring | session commit `6886a825c` | SATISFIED |
| GC-011 caller source-proven | SDK and orchestrator source rows above | SATISFIED |
| dispatch base clean | empty `git status --short` at `6886a825c` | SATISFIED |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`live-runtime-proof`, role=`dispatcher`, lifecyclePhase=`dispatch`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class live-runtime-proof --role dispatcher --lifecycle-phase dispatch --surface-selector system-chain --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Source Verification Block`; `Roadmap-To-Work-Order Trace Matrix`; `Dependency Release Evidence`; `ADIF Defect Registry Disclosure`; `Public Export Disposition` |
| gateRunPurpose | confirmation after caller-chain source verification; not first discovery |
| claimBoundary | dispatch authorization only; no UC-03 proof execution in this batch |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --help` |
| generatedProfile | GC-018 dispatch baseline |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | source-verified manual authoring from the current system-chain dispatch pattern |
| checkerReadAheadConfirmation | checker sources and literal-format gotchas read before authoring |
| docOnlyNewFields | N/A with reason: baseline introduces no runtime or schema field |
| claimBoundary | packet authorization only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance proof packet; no public-sync scope.

## Claim Boundary

This baseline authorizes one local provider-free proof of the GC-011 SDK route.
Even a PASS proves only that the selected contract-to-runtime path behaved as
recorded in one local environment and evidence window. It does not prove every
Governance Control Matrix row, GC-009, GC-010, all CVF controls, production,
public readiness, scale, certification, or user value.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | this baseline | `Status: DISPATCH_READY` | PASS |
| Work order status | paired SCLP-UC03-T2 work order | `Status: DISPATCH_READY` | PASS |
| Completion or reviewer artifact | declared completion review | reviewer decision after worker return | BLOCKED |
| Roadmap state | system-chain live-proof roadmap | UC-03 packet next | PASS |
| Registry JSON | coverage and Catalog/GAP owners | unchanged until accepted proof | BLOCKED with reason |
| Registry Markdown | system-chain GAP README | unchanged until accepted proof | BLOCKED with reason |
| External evidence digest | N/A with reason: no external evidence consumed | repository source only | N/A with reason |
| System loop interlock | fresh UC-03 receipt | not yet executed | BLOCKED |
| Session continuity | active session sources | separate synchronization after material completion | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Proof invocation | exactly one | NOT_RUN at dispatch | BLOCKED |
| Positive path | PASS | NOT_RUN at dispatch | BLOCKED |
| Negative path | PASS | NOT_RUN at dispatch | BLOCKED |
| Evidence denominator | 2 | NOT_RUN at dispatch | BLOCKED |
| Provider calls | 0 | 0 during packet authoring | PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher/reviewer role |
| Provider or surface | local private provenance repository |
| Session or invocation | SCLP-UC03-T2 baseline authoring, 2026-07-14 |
| Working directory | repository root |
| Command or tool surface | governed reads, source search, apply_patch, ADIF resolver, dispatch gates |
| Target paths | this baseline and paired work order |
| Allowed scope source | active nextAllowedMove at session commit `6886a825c` |
| Before status evidence | clean worktree at HEAD `6886a825c` |
| After status evidence | source-verified two-file UC-03 dispatch packet |
| Diff evidence | two-file dispatch diff before commit |
| Approval boundary | packet authoring and one later no-commit worker only |
| Claim boundary | no proof execution, provider, public, coverage, GAP, or session edit |
| Agent type | dispatcher/reviewer |
| Invocation ID | system-chain-uc03-t2-baseline-2026-07-14 |
| Expected manifest | paired GC-018 baseline and work order |
| Actual changed set | paired GC-018 baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |
