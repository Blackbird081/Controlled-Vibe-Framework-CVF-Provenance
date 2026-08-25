# CVF EAFR-R1E Orchestrator Provider Execution Authority Completion Review

Memory class: FULL_RECORD

Status: REVIEWER_ACCEPTED_CLOSED_PASS_BOUNDED

Date: 2026-08-25

docType: review

rawMemoryReleased=false

## Target / Source

| Field | Value |
| --- | --- |
| Trigger | operator corrective order after the second accidental worker provider call |
| Authority | explicit operator authority for the current orchestrator to implement a lasting CVF foundation control |
| Predecessor | EAFR-R1D accepted bounded at material commit `87d3ddd40` |
| Reviewer | current orchestrator/reviewer/closer |

## Purpose

Prevent a worker or subagent from treating an API key, local environment, live
test selection, or provider-capable command as permission to call a provider.
Provider execution now defaults to forbidden and requires a bounded grant
issued by the orchestrator.

## Scope / Methodology

The review inspected the contract evaluator, provider fetch boundary, test
setup, environment loader, Vitest configuration, package script, integration
activation gate, canonical delegation texts and every new checker/catalog
change. It then ran focused negative/boundary tests, both TypeScript checks,
list-only discovery and governance checks. No provider-execution command was
authorized or run.

## Findings / Position

Position: `REVIEWER_ACCEPTED_CLOSED_PASS_BOUNDED`.

### R1E-RF1 - authority is explicit and fail closed

`DelegationContract` now requires `providerExecution`. Its default disposition
is `FORBIDDEN`; executable authority binds grant id, orchestrator issuer,
subject agent, delegation, provider allowlist, call budget and expiry. Missing,
malformed, mismatched, expired and exhausted grants deny.

### R1E-RF2 - selection no longer activates execution

`--mode live` controls collection only. `npm run test:live` is list-only, and
the provider integration cases cannot activate from a provider key alone.
Repository env files are forbidden from supplying grant identity or grant JSON.

### R1E-RF3 - CVF-owned provider traffic is denied before network I/O

The shared test setup installs a fetch guard. Recognized provider hosts reach
the underlying fetch only after the grant evaluator succeeds. Negative unit
tests prove zero underlying calls for absent or mismatched authority and prove
the global maximum-call budget.

### R1E-RF4 - the rule is promoted into an early machine gate

The new compatibility checker pins the runtime invariants and rejects changed
provider/live work orders that omit an exact authority disposition or an
executable bounded grant envelope. It is in autorun, reviewer-fast,
pre-commit and pre-push catalogs.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add and wire the fail-closed subagent
provider-execution authority checker.

Protected paths:

- `governance/compat/agent_autorun_command_catalog.py`
- add `governance/compat/check_subagent_provider_execution_authority.py`;
- `governance/compat/test_check_subagent_provider_execution_authority.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_pre_push.py`

Operator authorization: the operator explicitly ordered a lasting CVF
foundation control after the second accidental worker provider call.

Rollback boundary: revert only the R1E material commit; do not alter unrelated
guards, continuity history, provider credentials or incident evidence.

The authorization is limited to fail-closed worker/subagent provider execution
authority. It does not authorize weakening another checker or any provider
call.

## Verification Evidence

| Proof | Result |
| --- | --- |
| control-plane delegation tests | 42/42 PASS |
| control-plane TypeScript | PASS, zero diagnostics |
| cvf-web focused tests | 12/12 PASS |
| cvf-web TypeScript | PASS, zero diagnostics |
| provider authority checker tests | 4/4 PASS |
| provider authority checker | COMPLIANT |
| live script | list-only, 35 paths, zero test execution |
| reviewer-fast governance | 66/66 PASS |
| pre-commit governance | 87/87 PASS |
| provider calls | zero |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_changed_corpus_registry_coverage.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_subagent_provider_execution_authority.py`; local hook and autorun catalogs |
| literalTokensReviewed | complete Core Guard Self-Protection Authorization fields; review scope/methodology; Machine Closure Package; Public Export Disposition |
| gateRunPurpose | confirm already-inspected source/test evidence and the governed closure shape without provider execution; not first discovery |
| claimBoundary | checker conformance does not replace runtime source or unit evidence |

## Risk / Corrective Action

This closes CVF-owned delegation, provider-adapter and test-runner paths. It is
not a universal firewall against an adversarial process given unrestricted
shell, credentials and network access. For such a process the orchestrator or
runtime host must additionally withhold keys and network capability. This
claim boundary is deliberate and prevents a false security claim.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| two workers independently treated execution-capable commands as usable despite no live authority | WORKER_EXECUTION_ERROR | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_ADDED | default-deny contract, bounded grant, pre-network guard and early checker; handled in this batch |
| prior live selection flag also activated provider cases | RULE_GAP | RUNTIME_BEHAVIOR_LEARNING | STANDARD_UPDATED | selection and execution authority separated; handled in this batch |

runtimeProviderCostLearningLane: SYSTEMIC_CONTROL_ADDED - zero R1E provider
calls; the six earlier incident calls remain excluded acceptance evidence.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | operator-authorized orchestrator/reviewer/closer |
| Provider or surface | private local repository; zero provider calls |
| Session or invocation | EAFR-R1E corrective foundation tranche, 2026-08-25 |
| Working directory | repository root, control-plane foundation and cvf-web |
| Command or tool surface | source edits, TypeScript, Vitest list/unit proof, pytest and compatibility checker |
| Target paths | control-plane delegation contract/test/barrel; cvf-web runner, guard, setup and tests; delegation standards; checker/test/catalogs; review and roadmap |
| Allowed scope source | operator's explicit lasting-control request after the second incident |
| Before status evidence | HEAD `d1b233e40`; staging empty; R1D closed and R6 next |
| After status evidence | R1E material set uncommitted; staging empty; zero provider calls |
| Diff evidence | direct source diff, focused negative tests, TypeScript, list-only output and governance receipts |
| Approval boundary | local CVF provider-execution authority control only |
| Claim boundary | no live provider, build, deployment, public sync or push |
| Agent type | orchestrator/reviewer/closer |
| Invocation ID | `eafr-r1e-provider-authority-2026-08-25` |
| Expected manifest | 21 R1E material paths before registry or continuity requirements |
| Actual changed set | MATCH at reviewer-fast attempt one |
| Manifest delta | NONE |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | CVF-owned worker/subagent provider execution boundary |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: unit/type/list/checker results above |
| actionEvidence | ACTION_EVIDENCE_PRESENT: contract, fetch guard, runner separation and catalog integration |
| invocationBoundary | local non-provider tests and list-only discovery |
| interceptionBoundary | CVF-owned fetch/test path; no universal shell or network interception claim |
| forbiddenExpansion | provider calls, deployment, public sync, push and R6 implementation |
| claimLanguage | bounded CVF-owned enforcement, not universal shell/network isolation |

## Epistemic Process Block

- Epistemic Process Applicability: HIGH_EVIDENCE_REVIEW
- Expected Result / Prediction: separating selection from execution and
  requiring a subject-bound grant would keep live discovery usable while an
  absent or mismatched grant caused zero underlying provider fetches.
- Evidence Comparison: list-only discovery found 35 live paths; focused live
  provider collection skipped all three cases without a grant; negative tests
  observed zero underlying calls; valid authority permitted only one call.
- Contradiction Or Gap Disposition: repository controls cannot universally
  isolate a process that the host gives unrestricted shell, credentials and
  network. The claim is bounded and host-level capability withholding remains
  required for that stronger threat model.
- Claim Update: R1E closes CVF-owned authority conflation and prevents the
  repeated accidental path; R6 remains next only after commit and continuity.

## Reviewer Decision

Accept EAFR-R1E as `CLOSED_PASS_BOUNDED` after final governance gates. R6 may
return to fresh source verification only after the material commit and separate
continuity sync.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance and runtime hardening; no public-sync
authority.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | direct operator corrective authority; no worker dispatch | operator request and trace | PASS |
| Completion or reviewer artifact | this review | `REVIEWER_ACCEPTED_CLOSED_PASS_BOUNDED` | PASS |
| runtime contract and guard | control-plane contract plus cvf-web fetch guard | focused tests and TypeScript | PASS |
| live runner boundary | package/config/provider test | list-only discovery and static guard | PASS |
| governance control | checker, test and hook catalogs | focused pytest and direct checker | PASS |
| canonical standard | delegation boundary standard and role/provider router | exact authority rules | PASS |
| roadmap state | EAFR roadmap | R1E accepted; R6 next after sync | PASS |
| Registry JSON | N/A with reason: no new governed source/test coverage entry required | changed corpus registry coverage checker | PASS |
| Registry Markdown | N/A with reason: no projection requested | no applicability | BLOCKED with reason: no registry projection mutation |
| External evidence digest | N/A with reason: no external evidence consumed | none | N/A with reason |
| System loop interlock | R1D incident -> R1E control -> R6 | roadmap and this review | PASS |
| Session continuity | separate post-material sync | material commit hash required first | BLOCKED with reason: material commit pending |

## Claim Boundary

R1E proves default-deny and bounded orchestrator-grant enforcement on the named
CVF-owned paths. It does not erase the prior incidents, grant a worker provider
authority, prove universal OS/network isolation, run a live test, resolve
BuildAuthority, implement R6, deploy, publish, push, or make a production claim.
