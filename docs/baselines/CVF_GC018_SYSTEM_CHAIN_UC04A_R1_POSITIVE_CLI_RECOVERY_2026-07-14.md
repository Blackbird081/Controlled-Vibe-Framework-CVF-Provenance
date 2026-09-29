# CVF GC-018 System Chain UC-04A-R1 Positive CLI Recovery

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: gc018_baseline

Date: 2026-07-14

Risk classification: R1

## Purpose

Authorize the smallest recovery needed to complete the missing positive half
of UC-04A operator-readout proof. The accepted negative case remains retained
and must not be rerun.

## Authorization / Decision

The blocked UC-04A closure at material commit `da93a4b73` proves that the CLI
failed closed because the original packet lacked dispatch-time protected-path
authorization. The proof runner and its 39-test suite are now committed. This
recovery creates no protected path and changes no protected owner.

Authorize one no-commit worker to run the existing autorun CLI directly once
with phase `pre-dispatch`, explicit base/head, and a dedicated receipt
directory. Zero retry, zero negative-case rerun, and zero provider calls are
authorized.

## Decision

Dispatch `SCLP-UC04A-R1` as a positive-only recovery. The worker may run the
committed focused suite and exactly one direct positive CLI invocation. The
retained negative case is evidence reuse, not executable scope.

## Scope / Target / Owner Boundary

Target: the existing local autorun CLI positive operator readout only. The CLI,
runner, focused tests, command catalog, checkers, hooks, system-chain owners,
roadmap, Catalog/GAP, session, Web, provider, public, and runtime sources are
read-only during worker execution.

## Core Guard Self-Protection Authorization

Protected-path classification: `scripts/run_cvf_system_chain_uc04a_cli_operator_readout_proof.py`
and `governance/compat/test_run_cvf_system_chain_uc04a_cli_operator_readout_proof.py`
are committed evidence at `da93a4b73` and are read-only reuse inputs.

Authorized protected-path mutations: NONE.

Operator authority: the operator instructed continuation after the bounded
blocked closure; the active next move narrows continuation to packet authoring
and one later positive-only recovery.

Rollback boundary: remove only the new R1 receipt and return artifacts if the
recovery is rejected. Do not revert or edit the retained runner, test, negative
receipt, diagnostic, or blocked closure.

Not authorized: no guard, checker, test, runner, hook, catalog, roadmap,
coverage, session, Web, provider, public, or runtime mutation.

## Design Control Gate

| Control | Decision |
|---|---|
| CLI owner | `governance/compat/run_agent_autorun_workflow_gate.py` |
| positive call | one direct `pre-dispatch` CLI invocation |
| retained negative | reuse accepted evidence; no invocation |
| retry ceiling | zero |
| provider boundary | zero provider/API/MCP calls |
| protected-path mutation | forbidden |
| worker commit | forbidden |
| closer | reviewer/closer only |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| CLI prints one result line per configured check | `governance/compat/run_agent_autorun_workflow_gate.py` | lines 72-76 | `_print_result` | autorun CLI | RUNTIME_BEHAVIOR | ACCEPT |
| CLI writes a PASS receipt only after all checks pass | `governance/compat/run_agent_autorun_workflow_gate.py` | lines 177-207 and 399-405 | `_write_receipt` | autorun receipt owner | RUNTIME_BEHAVIOR | ACCEPT |
| PASS receipt schema is `cvf.autorun.pass-receipt.v1` | `governance/compat/run_agent_autorun_workflow_gate.py` | line 30 and lines 184-204 | `RECEIPT_SCHEMA` | autorun receipt schema | VALUE_SET | ACCEPT |
| CLI accepts phase, base, head, and receipt-directory arguments | `governance/compat/run_agent_autorun_workflow_gate.py` | lines 409-435 | `main` | autorun CLI parser | EXISTS | ACCEPT |
| retained runner defines stable positive and negative case IDs | `scripts/run_cvf_system_chain_uc04a_cli_operator_readout_proof.py` | lines 25-26 | `POSITIVE_CASE_ID`; `NEGATIVE_CASE_ID` | retained proof runner | VALUE_SET | ACCEPT |
| retained focused suite contains 39 tests and protects command, receipt, identity, and call-count behavior | `governance/compat/test_run_cvf_system_chain_uc04a_cli_operator_readout_proof.py` | test declarations | `TestCaseIdentity`; `TestInvocationCounts`; `TestReceiptParsing` | retained focused suite | EXISTS | ACCEPT |
| accepted closure requires positive-only recovery and retains the negative result | `docs/reviews/CVF_SYSTEM_CHAIN_UC04A_CLI_OPERATOR_READOUT_COMPLETION_2026-07-14.md` | Decision and Recommendation | `CLOSED_BLOCKED_BOUNDED` | reviewer closure | VALUE_SET | ACCEPT |
| coverage keeps UC-04 blocked pending one positive-only recovery | `docs/reference/system_chain/CVF_SYSTEM_CHAIN_LIVE_PROOF_COVERAGE.json` | UC-04 entry | `BLOCKED_BOUNDED_RECOVERY_REQUIRED` | live-proof coverage ledger | VALUE_SET | ACCEPT |
| roadmap selects a fresh UC-04A-R1 packet as next | `docs/roadmaps/CVF_SYSTEM_CHAIN_LIVE_PROOF_USE_CASE_ROADMAP_2026-07-14.md` | Current Next Action | `UC-04A-R1` | system-chain roadmap | VALUE_SET | ACCEPT |
| protected manifest paths require dispatch-time classification | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0033.md` | Remediation | `ADIF-0033` | ADIF registry | LITERAL_INVARIANT | ACCEPT |

## Current Runtime Freshness Verification

Fresh reads at dispatch base `ed6561581` verified the CLI symbols, retained
runner/test identity, accepted blocked closure, coverage status, roadmap next
action, and ADIF-0033. The worker must refresh these facts before invocation.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Dispatch control | Evidence requirement | Disposition |
|---|---|---|---|
| complete missing positive readout | one direct current CLI call | stdout and PASS receipt | READY |
| retain prior negative evidence | forbid negative invocation | cited retained receipt and closure | READY |
| avoid repeated quota/time cost | zero retry and zero provider call | invocation ledger | READY |
| keep Web separate | Web paths forbidden | exact changed set | READY |
| close packet-authority learning | classify committed protected inputs as read-only | no protected diff | READY |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| original UC-04A attempt closed bounded | material commit `da93a4b73` | SATISFIED |
| protected runner/test committed | material commit `da93a4b73` | SATISFIED |
| session routes positive-only packet authoring | session commit `ed6561581` | SATISFIED |
| CLI and recovery boundary source-verified | Source Verification Block above | SATISFIED |
| dispatch worktree clean | empty `git status --short` at `ed6561581` | SATISFIED |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`system-chain-live-proof`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class system-chain-live-proof --role dispatcher --lifecycle-phase pre-dispatch --surface-selector governance/compat --max-results 20 --json`

Returned defects: NONE_RETURNED

Mandatory predecessor learning: `ADIF-0033` is applied because the accepted
UC-04A closure names it, even though the bounded resolver query returned no
items.

## Cost And Retry Control

One local CLI invocation, zero retries, zero negative calls, and zero provider
calls. Any unexpected result ends worker execution.

## Acceptance Criteria

- Focused retained suite passes 39/39 before the CLI call.
- Exactly one direct `pre-dispatch` CLI call exits zero.
- Output retains named per-check PASS lines and aggregate COMPLIANT.
- Generated receipt exists, has the current schema/status, and reconciles its
  check denominator with printed results.
- Retained negative evidence is cited without invocation.
- No protected source changes, retries, provider calls, Web work, staging, or
  worker commit occur.

## Evidence / Verification

Worker evidence must include clean execution base, source refresh, 39/39 test
result, exact CLI command fingerprint, one call count, exit code, aggregate and
per-check denominator, PASS receipt path/schema/status, retained negative
evidence citation, zero retry/provider counts, exact changed set, unchanged
HEAD, and secret-safe diagnostic only if blocked.

## Fail Conditions

Source drift, dirty start, retained-test failure, protected mutation, more or
fewer than one CLI call, retry, negative invocation, nonzero positive exit,
missing or invalid receipt, denominator mismatch, provider use, Web work,
secret leakage, unexpected path, staging, commit, or stronger claim stops the
recovery.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | local shell and autorun CLI | one positive read-only proof; no owner mutation | stdout, receipt, worker return | repository-local process only | IMPLEMENTED |
| `EXTERNAL_AGENT_CLI_MCP` | existing local CLI | no remote access, auth, mutation, MCP, or readiness claim | same bounded receipt | no new adapter | DEFERRED_WITH_REASON |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | current local CLI proof and source verification |
| Matching local-view guard | `governance/compat/check_work_order_dispatch_quality.py` |
| Owner surface | current autorun CLI and system-chain coverage ledger |
| Disposition | BLOCKED_UNTIL_CVF_PROOF at dispatch |
| Claim boundary | retained evidence plus source existence do not substitute for the one positive call |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_closure_packaging_preflight.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Core Guard Self-Protection Authorization`; `Source Verification Block`; `Roadmap-To-Work-Order Trace Matrix`; `Dependency Release Evidence`; `ADIF Defect Registry Disclosure`; `Public Export Disposition` |
| gateRunPurpose | confirmation after source and protected-path classification; not first discovery |
| claimBoundary | packet authorization only; no recovery execution in this batch |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --help` |
| generatedProfile | protected-path-aware GC-018 dispatch baseline |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | narrowed from the accepted original packet and blocked closure |
| checkerReadAheadConfirmation | guard orientation, checker sources, template, and literal-format gotchas read before authoring |
| docOnlyNewFields | N/A with reason: baseline introduces no runtime or canonical schema field |
| claimBoundary | packet authorization only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance recovery packet; no public-sync scope.

## Claim Boundary

This baseline authorizes one positive local CLI readout. A PASS may complete
only the bounded UC-04A CLI evidence when combined with the retained negative
case. It does not prove UC-04B Web, every checker surface, external-agent
readiness, provider governance, production, public readiness, scale,
certification, or user value.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | this baseline | `CLOSED_PASS_BOUNDED` | PASS |
| Work order status | paired R1 work order | `CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | R1 completion review | reviewer disposition | PASS |
| Worker return | R1 worker return | `COMPLETE_PENDING_REVIEW` converted by reviewer | PASS |
| Positive receipt | dedicated R1 receipt | schema/status and 75 named PASS rows | PASS |
| Retained negative | original UC-04A receipt | range/finality PASS without rerun | PASS |
| Roadmap state | system-chain roadmap | UC-04A bounded; UC-04B next | PASS |
| Registry JSON | live-proof coverage ledger | CLI bounded, Web unproven | PASS |
| Registry Markdown | system-chain README | combined positive/negative CLI evidence | PASS |
| Catalog/GAP | completion decision | no architecture owner or edge changed | N/A with reason |
| External evidence digest | N/A with reason: no external evidence consumed | local repository evidence only | N/A with reason |
| System loop interlock | one positive plus retained negative | no retry or negative rerun | PASS |
| Session continuity | active session sources | separate post-material synchronization | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Required | Observed | Status |
|---|---|---|---|
| focused tests | 39/39 before call | 39/39 | PASS |
| positive CLI calls | exactly one | 1 | PASS |
| positive aggregate | COMPLIANT | COMPLIANT 75/75 | PASS |
| positive receipt | current schema and PASS | present, 75 named PASS rows | PASS |
| negative rerun | zero | 0 | PASS |
| retries | zero | 0 | PASS |
| provider calls | zero | 0 | PASS |
| protected mutation | none | none | PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher/reviewer role |
| Provider or surface | local private provenance repository |
| Session or invocation | SCLP-UC04A-R1 packet authoring, 2026-07-14 |
| Working directory | repository root |
| Command or tool surface | governed reads, source search, apply_patch, ADIF resolver, dispatch gates |
| Target paths | this baseline and paired work order |
| Allowed scope source | active nextAllowedMove at session commit `ed6561581` |
| Before status evidence | clean worktree at HEAD `ed6561581` |
| After status evidence | source-verified positive-only recovery packet |
| Diff evidence | paired packet diff before commit |
| Approval boundary | packet authoring and one later no-commit positive CLI recovery |
| Claim boundary | no recovery invocation, Web, provider, public, coverage, GAP, or session edit |
| Agent type | dispatcher/reviewer |
| Invocation ID | system-chain-uc04a-r1-baseline-2026-07-14 |
| Expected manifest | paired GC-018 baseline and work order |
| Actual changed set | paired GC-018 baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |
