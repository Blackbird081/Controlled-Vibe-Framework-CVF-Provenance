# CVF GC-018 System Chain UC-02 Current Rerun

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: gc018_baseline

Date: 2026-07-14

Risk classification: R1

## Purpose

Authorize one fresh, bounded, provider-free rerun of the existing UC-02
registry-to-enforcement proof after the archive/live ownership repair closed
`CLOSED_PASS_BOUNDED`.

## Authorization / Decision

Repair completion commit `abb58be27` accepted the archive/live ownership and
bootstrap-order repair. Session commit `9c9245bd3` makes one source-verified
UC-02 rerun packet the next allowed move. This baseline authorizes the paired
no-commit worker to run the retained focused tests and invoke the existing
UC-02 proof runner exactly once.

## Decision

Authorize `SCLP-UC02-R2`. No retry is available inside the worker tranche. A
PASS requires 9/9 scenario events after one successful bootstrap. A failure
must stop with a secret-safe diagnostic and remains reviewer-owned.

## Scope / Target / Owner Boundary

The worker may create or regenerate only the paths in the paired work order's
Planned Worker Fulfillment Manifest. Existing runner, tests, registry,
checkers, coverage, roadmap, GAP, repair closure, retained blocked receipt,
session, archive, provider, and public surfaces are read-only.

## Design Control Gate

| Control | Decision |
|---|---|
| Runtime route | existing `run_cvf_system_chain_uc02_current_proof.py` only |
| Invocation ceiling | one proof-run invocation; zero worker retries |
| Denominator | one call-level result and exactly nine scenario events |
| Bootstrap outputs | 21 enumerated current live outputs; archive remains read-only |
| Provider boundary | zero provider/API/MCP calls; coverage owner declares `providerCallRequired=false` |
| Failure boundary | classify once, preserve receipt, stop |
| Closure owner | reviewer/closer only |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| retained UC-02 runner selects the canonical registry and nine target IDs | `scripts/run_cvf_system_chain_uc02_current_proof.py` | lines 20-25 | `SCENARIO_REGISTRY`; `TARGET_SCENARIO_IDS` | UC-02 proof runner | VALUE_SET | ACCEPT |
| runner bootstraps once and returns success only for 9/9 | `scripts/run_cvf_system_chain_uc02_current_proof.py` | `run_proof` and `main` | `run_proof`; `main` | UC-02 proof runner | RUNTIME_BEHAVIOR | ACCEPT |
| focused suite covers selection, command fidelity, bootstrap failure, 9/9, partial failure, and secret safety | `governance/compat/test_run_cvf_system_chain_uc02_current_proof.py` | test module | `test_*` | UC-02 focused test suite | EXISTS | ACCEPT |
| canonical IDs CF-076 through CF-084 exist exactly in the scenario registry | `docs/reference/CVF_CONFORMANCE_SCENARIOS.json` | lines 532-588 | `CF-076`; `CF-077`; `CF-078`; `CF-079`; `CF-080`; `CF-081`; `CF-082`; `CF-083`; `CF-084` | conformance scenario registry | VALUE_SET | ACCEPT |
| shared bootstrap runs the release gate then child packet runners | `scripts/run_cvf_packet_posture_state_bootstrap.py` | constants and `main` | `RELEASE_GATE`; `LOCAL_PACKET`; `SECONDARY_PACKETS`; `main` | packet-posture bootstrap | RUNTIME_BEHAVIOR | ACCEPT |
| release gate owns manifest generation and packet export | `scripts/run_cvf_runtime_evidence_release_gate.py` | constants and `main` | `MANIFEST_SCRIPT`; `PACKET_SCRIPT`; `main` | runtime evidence release gate | RUNTIME_BEHAVIOR | ACCEPT |
| UC-02 does not require a provider call and remains STALE before rerun | `docs/reference/system_chain/CVF_SYSTEM_CHAIN_LIVE_PROOF_COVERAGE.json` | UC-02 and `RUNTIME_TO_ENFORCEMENT` lane | `providerCallRequired`; `operationalProofStatus` | live-proof coverage ledger | VALUE_SET | ACCEPT |
| repair closure releases exactly one fresh rerun packet | `docs/reviews/CVF_SYSTEM_CHAIN_UC02_ARCHIVE_PATH_RECONCILIATION_COMPLETION_2026-07-14.md` | Next Move / completion decision | `CLOSED_PASS_BOUNDED` | SCLP-UC02-R1 completion review | VALUE_SET | ACCEPT |
| live-run failures require diagnosis before rerun | `docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md` | required diagnostic fields and retry discipline | `Live Run Diagnostic Record` | retained live-run diagnostic standard | LITERAL_INVARIANT | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Rerun control | Evidence requirement | Disposition |
|---|---|---|---|
| current UC-02 operational proof | invoke retained runner once | fresh receipt and diagnostic output | READY |
| 9/9 complete denominator | fail closed below nine PASS events | call-level and event-level fields | READY |
| diagnosis before retry | zero worker retries | failure diagnostic then stop | READY |
| reverse projection | reviewer-owned only after accepted proof | coverage/GAP diff in closure | PASS |
| later use cases remain parked | no UC-03/UC-04 work | exact changed-set review | READY |

## Cost And Retry Control

Proof-run invocation ceiling: one. Scenario-event denominator: nine. Provider
calls: zero. Retry count: zero. The worker must not repeat an unclear, partial,
failed, or timed-out run.

## Acceptance Criteria

- Focused suite passes before runtime invocation.
- Existing runner is invoked exactly once with the two new rerun output paths.
- Receipt records one successful bootstrap and 9/9 PASS events for acceptance.
- PASS diagnostic value is JSON `null`; failure diagnostic is secret-safe and
  complete enough for reviewer classification.
- All generated paths match the exact 24-path fulfillment manifest.
- Retained blocked evidence and archive owners remain unchanged.
- Worker returns with unchanged HEAD and no commit.

## Evidence / Verification

Dispatch evidence consists of current source verification, repair completion,
clean base `9c9245bd3`, and passing pre-dispatch gates. Worker evidence consists
of focused tests, one receipt, one diagnostic disposition, generated-output
inventory, worker return, diff/status evidence, and unchanged HEAD.

## Fail Conditions

Source drift, dirty unrelated paths, focused-test failure, more than one proof
invocation, any retry, bootstrap failure, any scenario failure, denominator
other than nine, secret leakage, unexpected output, retained evidence change,
archive write, provider call, or stronger claim stops the tranche.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| repair accepted | completion review at material commit `abb58be27` | SATISFIED |
| rerun packet is next allowed | session commit `9c9245bd3` | SATISFIED |
| dispatch base clean | `git status --short` at `9c9245bd3` | SATISFIED |
| provider call requirement | coverage ledger says `providerCallRequired=false` | SATISFIED |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`live-runtime-proof`, role=`dispatcher`, lifecyclePhase=`dispatch`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class live-runtime-proof --role dispatcher --lifecycle-phase dispatch --surface-selector system-chain --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Source Verification Block`; `Roadmap-To-Work-Order Trace Matrix`; `Dependency Release Evidence`; `ADIF Defect Registry Disclosure`; `Public Export Disposition` |
| gateRunPurpose | confirmation and evidence for one repaired UC-02 rerun; not first discovery |
| claimBoundary | authorization only; no UC-02 execution in dispatch tranche |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --help` |
| generatedProfile | GC-018 dispatch baseline |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | source-verified manual authoring from current governed pattern |
| checkerReadAheadConfirmation | checker sources and literal-format gotchas read before authoring |
| docOnlyNewFields | N/A with reason: no new runtime or schema fields |
| claimBoundary | dispatch authorization only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance runtime proof; no public-sync scope.

## Claim Boundary

This baseline authorizes one local provider-free UC-02 rerun. Even a 9/9 PASS
proves only the bounded registry-to-checker chain in the recorded environment
and evidence window. It does not prove provider governance, all CVF controls,
production, public readiness, scale, certification, or user value.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | this baseline | `Status: DISPATCH_READY` | PASS |
| Work order status | paired SCLP-UC02-R2 work order | `Status: DISPATCH_READY` | PASS |
| Completion or reviewer artifact | declared completion review | reviewer decision following worker return | BLOCKED |
| Roadmap state | system-chain live-proof roadmap | unchanged at dispatch | N/A with reason |
| Registry JSON | system-chain coverage/GAP owners | unchanged until accepted 9/9 proof | BLOCKED with reason |
| Registry Markdown | system-chain GAP README | unchanged until accepted 9/9 proof | BLOCKED with reason |
| External evidence digest | N/A with reason: no external evidence consumed | repository source only | N/A with reason |
| System loop interlock | fresh rerun receipt | not yet executed | BLOCKED |
| Session continuity | active session sources | separate synchronization following material completion | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Proof invocation | exactly one | NOT_RUN at dispatch | BLOCKED |
| Bootstrap | PASS exactly once | NOT_RUN at dispatch | BLOCKED |
| Scenario denominator | 9 | NOT_RUN at dispatch | BLOCKED |
| Scenario result | 9/9 PASS | NOT_RUN at dispatch | BLOCKED |
| Provider calls | 0 | 0 during packet authoring | PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher/reviewer role |
| Provider or surface | local private provenance repository |
| Session or invocation | SCLP-UC02-R2 dispatch authoring, 2026-07-14 |
| Working directory | repository root |
| Command or tool surface | governed reads, rg, git, apply_patch, ADIF resolver, dispatch gates |
| Target paths | this baseline and paired work order |
| Allowed scope source | active nextAllowedMove at session commit `9c9245bd3` |
| Before status evidence | clean worktree at HEAD `9c9245bd3` |
| After status evidence | source-verified two-file rerun dispatch packet |
| Diff evidence | two-file dispatch diff before commit |
| Approval boundary | packet authoring and one later no-commit worker only |
| Claim boundary | no proof execution, provider, public, coverage, GAP, or session edit |
| Agent type | dispatcher/reviewer |
| Invocation ID | system-chain-uc02-r2-baseline-2026-07-14 |
| Expected manifest | paired GC-018 baseline and work order |
| Actual changed set | paired GC-018 baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |
