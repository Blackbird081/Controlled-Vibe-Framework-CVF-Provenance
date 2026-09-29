# CVF GC-018 System Chain UC-04A CLI Operator Readout

Memory class: FULL_RECORD

Status: CLOSED_BLOCKED_BOUNDED

docType: gc018_baseline

Date: 2026-07-14

Risk classification: R1

## Purpose

Authorize one bounded, provider-free proof that the current autorun CLI exposes
usable aggregate, per-check, receipt, and meaningful failure readouts to a
local operator.

## Authorization / Decision

The system-chain roadmap and accepted UC-03 closure make UC-04A packet
authoring the next allowed move. Fresh source verification selects
`governance/compat/run_agent_autorun_workflow_gate.py` because it is the
current CLI owner for per-check PASS/FAIL lines, aggregate disposition, local
PASS receipts, and closure-finality failure messages.

## Decision

Authorize `SCLP-UC04A-T3` for one no-commit worker. The worker may create a
proof runner, focused runner tests, one receipt, one diagnostic, and one worker
return. The proof runner may be invoked exactly once and may invoke the
selected CLI exactly twice: one successful `pre-dispatch` call and one expected
failing `pre-closure` call. No retry and no provider call are authorized.

Reviewer closure update: the attempt executed once and is closed
`CLOSED_BLOCKED_BOUNDED`. The negative readout passed, while the positive
readout was blocked because this packet authorized a new protected
`governance/compat` test path without carrying the required Core Guard
Self-Protection Authorization block. No retry occurred. A separate R1 packet
must reuse the retained negative evidence and authorize only one positive CLI
call after the protected proof test is committed through reviewer closure.

## Scope / Target / Owner Boundary

Target: the current local autorun CLI operator surface only. Existing CLI,
command catalog, checkers, tests, hooks, roadmap, system-chain references,
coverage ledger, Catalog/GAP, session, Web, provider, public, and runtime owners
are read-only during worker execution.

## Design Control Gate

| Control | Decision |
|---|---|
| CLI owner | `run_agent_autorun_workflow_gate.py` |
| positive readout | `pre-dispatch` exits zero, prints per-check PASS lines and aggregate COMPLIANT, and writes a valid PASS receipt |
| meaningful failure readout | `pre-closure` uses the unchanged execution base as both range endpoints and exits nonzero with the non-empty committed-range reason; worker proof files also remain visible to closure finality |
| harness invocation ceiling | one |
| CLI sub-invocation ceiling | two; one positive and one negative |
| retry ceiling | zero |
| provider boundary | zero provider/API/MCP calls |
| Web boundary | UC-04B remains excluded |
| CLI mutation | forbidden |
| closure owner | reviewer/closer only |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| CLI prints one PASS or FAIL line per configured command | `governance/compat/run_agent_autorun_workflow_gate.py` | lines 72-76 | `_print_result` | autorun CLI | RUNTIME_BEHAVIOR | ACCEPT |
| CLI writes a structured PASS receipt only after all checks pass | `governance/compat/run_agent_autorun_workflow_gate.py` | lines 177-207 and 399-405 | `_write_receipt` | autorun receipt owner | RUNTIME_BEHAVIOR | ACCEPT |
| receipt contains schema, phase context, duration, and per-check results | `governance/compat/run_agent_autorun_workflow_gate.py` | lines 184-204 | `RECEIPT_SCHEMA` | autorun receipt schema | VALUE_SET | ACCEPT |
| pre-closure rejects an empty committed range | `governance/compat/run_agent_autorun_workflow_gate.py` | lines 334-341 | `_run_phase` | autorun CLI | RUNTIME_BEHAVIOR | ACCEPT |
| pre-closure reports dirty worktree paths and blocks closure | `governance/compat/run_agent_autorun_workflow_gate.py` | lines 219-236 and 390-392 | `_closure_worktree_finality_failures` | autorun CLI | RUNTIME_BEHAVIOR | ACCEPT |
| CLI supports explicit phase, base, head, and receipt directory arguments | `governance/compat/run_agent_autorun_workflow_gate.py` | lines 409-435 | `main` | autorun CLI argument parser | EXISTS | ACCEPT |
| focused owner tests cover dirty closure finality and PASS/failure propagation | `governance/compat/test_run_agent_autorun_workflow_gate.py` | lines 166-207 and 267-295 | `test_closure_finality_blocks_dirty_stdout`; `test_pre_implementation_fails_when_aaf_helper_fails` | autorun focused test suite | EXISTS | ACCEPT |
| coverage ledger requires CLI current-run readout before separate Web proof | `docs/reference/system_chain/CVF_SYSTEM_CHAIN_LIVE_PROOF_COVERAGE.json` | UC-04 and Evidence-to-Operator entries | `UC-04-EVIDENCE-TO-OPERATOR-SURFACE` | live-proof coverage ledger | VALUE_SET | ACCEPT |
| roadmap requires aggregate plus one meaningful failure/readout boundary | `docs/roadmaps/CVF_SYSTEM_CHAIN_LIVE_PROOF_USE_CASE_ROADMAP_2026-07-14.md` | tranche T3 / UC-04A | `T3 / UC-04A` | system-chain roadmap | VALUE_SET | ACCEPT |
| retained audit separates CLI output from the bounded Web subset | `docs/audits/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_2026-07-10.md` | Lane 5, items (a)-(c) | `Evidence to operator surface` | accepted system-chain audit | VALUE_SET | ACCEPT |
| distinct evidence-case identity is required for reusable aggregate proof | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0032.md` | remediation and prevention controls | `CVF_ADIF-0032` | ADIF registry | LITERAL_INVARIANT | ACCEPT |

## Current Runtime Freshness Verification

Fresh reads at dispatch base `2970a6641` verified the selected CLI owner,
argument parser, output markers, receipt schema, closure-finality behavior,
focused owner tests, and CLI/Web split. The worker must recompute these facts
at execution base. If the CLI no longer exposes the cited symbols or behavior,
the worker returns `BLOCKED_WITH_REASON` before creating proof artifacts.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Dispatch control | Evidence requirement | Disposition |
|---|---|---|---|
| real CLI output | invoke current autorun owner | retained stdout summary and command fingerprint | READY |
| receipt path | use an explicit evidence receipt directory | parsed structured PASS receipt | READY |
| usability evidence | retain per-check and aggregate markers | positive case evidence | READY |
| one meaningful failure/readout | expected empty-range and dirty-finality failure | negative case with exact reason markers | READY |
| stop after CLI boundary | two CLI calls only | invocation ledger and zero retries | READY |
| keep Web separate | UC-04B forbidden | exact changed-set review | READY |
| provider only when crossed | selected CLI claim is provider-free | provider call count zero | READY |
| reverse-project learning | reviewer-owned after acceptance | coverage, roadmap, Catalog/GAP, and ADIF decision | READY |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| UC-03 accepted | material commit `7a8f7268f` | SATISFIED |
| session routes UC-04A packet authoring | session commit `2970a6641` | SATISFIED |
| roadmap selects CLI before Web | current roadmap T3/T4 split | SATISFIED |
| CLI owner and failure behavior source-verified | Source Verification Block above | SATISFIED |
| dispatch worktree clean | empty `git status --short` at `2970a6641` | SATISFIED |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`system-chain-live-proof`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class system-chain-live-proof --role dispatcher --lifecycle-phase pre-dispatch --max-results 20 --json`

Returned defects: NONE_RETURNED

## Cost And Retry Control

One proof-harness invocation, two local CLI sub-invocations, zero retry, and
zero provider calls. Failure or unclear output stops worker execution.

## Acceptance Criteria

- Current source still proves the selected CLI owner and output behavior.
- Focused proof-runner tests pass before the single proof invocation.
- The positive case exits zero, retains individually named per-check results,
  prints aggregate COMPLIANT, and writes a valid PASS receipt.
- The negative case exits nonzero and retains the exact non-empty committed
  range failure; dirty worker evidence is visible to closure finality.
- Receipt cases use stable IDs `positive_pre_dispatch` and
  `negative_pre_closure`; aggregate counts cannot substitute for identity.
- Exactly one harness invocation, two CLI sub-invocations, zero retries, and
  zero provider calls are recorded.
- Worker changes only declared proof and return paths, leaves HEAD unchanged,
  stages nothing, and does not commit.

## Evidence / Verification

Worker evidence must include focused mock-subprocess tests, one real harness
invocation, the positive local PASS receipt, a two-case proof receipt, a
secret-safe diagnostic disposition, command hashes, case IDs, exit codes,
per-check denominator, exact failure markers, exact changed set, and unchanged
HEAD.

## Fail Conditions

Source drift, CLI-owner mutation, focused-test failure, missing case identity,
missing receipt, second harness invocation, more or fewer than two CLI calls,
retry, unexpected positive failure, unexpected negative success, absent
failure reason, provider use, Web work, secret leakage, unexpected path, or
stronger claim stops the tranche.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | local repository shell and selected autorun CLI | read-only CLI proof; no commit or owner mutation | focused tests, CLI output, receipts, worker return | package-local Python process only | IMPLEMENTED |
| `EXTERNAL_AGENT_CLI_MCP` | existing CLI can be invoked from a local external shell | this tranche proves operator readout only, not remote access, auth, mutation, or MCP | same bounded CLI receipt; no external-agent readiness claim | no new adapter or MCP surface | DEFERRED_WITH_REASON |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | current local CLI proof and source verification |
| Matching local-view guard | `governance/compat/check_work_order_dispatch_quality.py` |
| Owner surface | current autorun CLI and system-chain coverage ledger |
| Disposition | BLOCKED_UNTIL_CVF_PROOF at dispatch; reviewer accepts only fresh two-case receipt |
| Claim boundary | historical audit and source existence are not current UC-04A operational proof |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Source Verification Block`; `Roadmap-To-Work-Order Trace Matrix`; `Dependency Release Evidence`; `ADIF Defect Registry Disclosure`; `Dual Agent Surface Matrix`; `Public Export Disposition` |
| gateRunPurpose | confirmation after full CLI-owner and output-contract source verification; not first discovery |
| claimBoundary | dispatch authorization only; no UC-04A proof execution in this batch |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --help` |
| generatedProfile | GC-018 dispatch baseline |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | source-verified authoring from the accepted system-chain dispatch pattern |
| checkerReadAheadConfirmation | applicable checker sources and literal-format gotchas read before authoring |
| docOnlyNewFields | N/A with reason: baseline introduces no runtime or canonical schema field |
| claimBoundary | packet authorization only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance proof packet; no public-sync scope.

## Claim Boundary

This baseline authorizes one local proof of the selected autorun CLI readout.
A PASS may prove only that the CLI exposed the retained aggregate, per-check,
receipt, and selected failure information in one local environment and evidence
window. It does not prove UC-04B Web, every checker surface, external-agent
readiness, provider governance, production, public readiness, scale,
certification, or user value.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | this baseline | `CLOSED_BLOCKED_BOUNDED` | PASS |
| Work order status | paired SCLP-UC04A-T3 work order | `CLOSED_BLOCKED_BOUNDED` | PASS |
| Completion or reviewer artifact | UC-04A completion review | reviewer blocker disposition | PASS |
| Worker return | declared worker-return path | `BLOCKED_WITH_REASON` | PASS |
| Runtime receipt | UC-04A two-case JSON | positive FAIL 73/75; negative PASS | PASS |
| Diagnostic | UC-04A diagnostic JSON | non-retryable packet gap | PASS |
| Roadmap state | system-chain roadmap | recovery packet next | PASS |
| Registry JSON | live-proof coverage ledger | UC-04A partial blocked | PASS |
| Registry Markdown | system-chain README and Catalog/GAP decision | blocker and no architecture gap recorded | PASS |
| Learning | ADIF-0033 | resolver-discoverable packet rule | PASS |
| External evidence digest | N/A with reason: no external evidence consumed | local repository evidence only | N/A with reason |
| System loop interlock | retained UC-04A receipt and diagnostic | one bounded attempt, zero retry, partial result preserved | PASS |
| Session continuity | active session sources | separate post-material synchronization | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| harness invocation | 1 | 1 | PASS |
| CLI invocation count | 2 | 2 | PASS |
| positive aggregate | PASS | FAIL 73/75 | BLOCKED |
| positive PASS receipt | present | absent because aggregate failed | BLOCKED |
| negative readout | PASS | PASS | PASS |
| stable case IDs | 2 distinct | 2 distinct | PASS |
| retry count | 0 | 0 | PASS |
| provider calls | 0 | 0 | PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher/reviewer role |
| Provider or surface | local private provenance repository |
| Session or invocation | SCLP-UC04A-T3 baseline authoring, 2026-07-14 |
| Working directory | repository root |
| Command or tool surface | governed reads, source search, apply_patch, ADIF resolver, dispatch gates |
| Target paths | this baseline and paired work order |
| Allowed scope source | active nextAllowedMove at session commit `2970a6641` |
| Before status evidence | clean worktree at HEAD `2970a6641` |
| After status evidence | source-verified two-file UC-04A dispatch packet |
| Diff evidence | two-file dispatch diff before commit |
| Approval boundary | packet authoring and one later no-commit worker only |
| Claim boundary | no proof execution, Web, provider, public, coverage, GAP, or session edit |
| Agent type | dispatcher/reviewer |
| Invocation ID | system-chain-uc04a-t3-baseline-2026-07-14 |
| Expected manifest | paired GC-018 baseline and work order |
| Actual changed set | paired GC-018 baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |
