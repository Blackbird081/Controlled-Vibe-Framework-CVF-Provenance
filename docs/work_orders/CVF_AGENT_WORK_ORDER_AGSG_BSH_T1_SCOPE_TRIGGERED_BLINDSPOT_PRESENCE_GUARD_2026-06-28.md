# CVF Agent Work Order AGSG-BSH-T1 Scope-Triggered Blind-Spot Presence Guard

Memory class: FULL_RECORD

Status: HOLD_PENDING_EXECUTOR

Date: 2026-06-28

docType: work_order

Batch ID: AGSG-BSH-T1

## Dispatch Prompt Envelope

Implement a scope-triggered presence checker that closes ADIF-0014: when a
changed work order, GC-018 baseline, or completion review touches an
absorption source under `.private_reference/legacy/` or
`.private_reference/external_repos/`, the artifact must carry both
the Mandatory Blind-Spot Control Block heading and the Corpus Completeness And
Report Integrity section heading (or an allowed `NOT_APPLICABLE_WITH_REASON` /
`SKIPPED_WITH_REASON` disposition), independent of any completeness claim. You
are the executor, not the author. Do not commit; return for review.

## Authority Chain

This work order is authorized by
`docs/baselines/CVF_GC018_AGSG_BSH_T1_SCOPE_TRIGGERED_BLINDSPOT_PRESENCE_GUARD_2026-06-28.md`
and the Agent Error To Governance Learning Philosophy. It records
[ADIF-0014](../reference/agent_defect_intelligence/entries/CVF_ADIF-0014.md).

## Agent Roles

Route mode: `SINGLE_AGENT_SINGLE_ROLE`. The dispatch author (Claude) is not the
executor. The executor implements, self-checks, and returns under
WORKER_MUST_NOT_COMMIT.

Commit mode: WORKER_MUST_NOT_COMMIT

Base-anchor lifecycle markers: dispatchBaseHead=`a9c79eb8`;
executionBaseHead=`<executor resolves live at start>`;
closureBaseHead=`<closer resolves live at closure>`.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake classification | governance-hardening checker implementation, R1 offline guard |
| Scope classification | one new `governance/compat/` checker + test/fixture + one hook-chain wiring edit |
| Risk sensitivity | R1: offline guard, no runtime/provider/public/import surface |
| Escalation condition | escalate to orchestrator if scope-trigger cannot be bounded without false positives or an existing checker would need modification |
| Author role | dispatcher (Claude); authored this packet only |
| Executor role | worker (Codex); implements and self-checks under WORKER_MUST_NOT_COMMIT |
| Reviewer role | operator-assigned reviewer before commit |
| Role separation | dispatch authorship does not grant execution (B13/B23) |
| Route mode | `SINGLE_AGENT_SINGLE_ROLE` |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_SINGLE_ROLE` |
| rolePattern | one executor: Codex implements checker/tests/worker-return; operator-assigned reviewer reviews/closes |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE |
| baseHeadFor(phase) | `dispatchBaseHead=a9c79eb8`; `executionBaseHead` confirmed by Codex at start; `closureBaseHead` set by reviewer before closure |
| changedSetScope(phase) | worker creates only the checker, its test/fixture, and the hook-chain wiring edit; reviewer owns status/closure |
| traceScope(phase, actor) | one Codex worker-return trace covers the checker, test, and wiring; one reviewer trace covers review/closure if accepted |
| commitOwner(phase) | Codex commits nothing (`WORKER_MUST_NOT_COMMIT`); reviewer owns any material/closure commit |
| crossBatchIsolation | do not mix AGSG-BSH-T1 with skill-content import, runtime, public-sync, provider/live, or MCP work |
| Before status evidence | clean worktree at dispatch base `a9c79eb8` plus the staged AGSG-BSH-T1 dispatch artifacts |
| nextMoveSurfaces | reviewer updates next-move surfaces only after review if mode or next allowed move changes |
| Closer designation | operator-assigned reviewer is the designated reviewer and closer |

## Reviewer Closure Conversion

completionReviewPath:
`docs/reviews/CVF_AGSG_BSH_T1_SCOPE_TRIGGERED_BLINDSPOT_PRESENCE_GUARD_COMPLETION_2026-06-28.md`

reviewerOwnedClosurePaths:

- `docs/reviews/CVF_AGSG_BSH_T1_SCOPE_TRIGGERED_BLINDSPOT_PRESENCE_GUARD_COMPLETION_2026-06-28.md`
- session front-door/state/handoff paths only if the reviewer changes current
  mode or next allowed move after accepting the worker return.

Codex must not create the completion review and must not mark the work closed.

## Worker Return Packet Shape Contract

The worker return must include these sections so it passes the worker-return
fast gate without reviewer repair:

- Purpose
- Scope / Methodology
- Findings / Position
- Risk / Corrective Action
- Evidence / Verification (secret-safe checker and hook-chain output, plus
  `git status --short` and the resolved `executionBaseHead`)
- Source Verification Block (for any new named symbol)
- ADIF Defect Registry Disclosure (with the resolver query line)
- Agent Operation Trace Block
- Delta Execution Claim Boundary Control Block
- Public Export Disposition
- Claim Boundary

Conditional gate blocks (use `N/A with reason` / `NOT_APPLICABLE_WITH_REASON`
for any that do not apply to this offline checker work): the external-knowledge
intake-routing block, the re-scan intelligence hardening block, the
corpus-completeness report-integrity block, the finding-to-governance learning
disposition, the epistemic process block, and the machine closure package.

The worker return must not include a closure verdict or status change; those
are reviewer-owned.

## Worker Autonomy / No-Question Rule

The executor proceeds without questions for in-scope decisions (checker
structure, fixture content, wiring location). The executor returns to the
orchestrator only on the Return-To-Orchestrator Conditions below, not for
routine implementation choices.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: this work order implements an offline governance
checker and does not absorb or re-map legacy source content; the
legacy/external folders are named only as the scope-trigger path families the
checker must detect, not as a corpus to absorb.

## Required First Reads

- `docs/baselines/CVF_GC018_AGSG_BSH_T1_SCOPE_TRIGGERED_BLINDSPOT_PRESENCE_GUARD_2026-06-28.md`
- `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md`
- `governance/compat/check_corpus_completeness_report_integrity.py` (claim-trigger pattern to mirror)
- `governance/compat/check_adif_defect_registry_disclosure.py` (scope/phase wiring reference)
- `governance/compat/run_local_governance_hook_chain.py`

## Pre-Flight Checks

- Confirm the active handoff and current mode before starting.
- Confirm `governance/compat/check_absorption_blindspot_control_presence.py`
  does not already exist.
- Confirm the two existing claim-triggered checkers will not be modified.
- Resolve the live execution base head with `git rev-parse HEAD`.

## Write Ownership

The executor may create
`governance/compat/check_absorption_blindspot_control_presence.py`, create a
paired test/fixture file, and edit
`governance/compat/run_local_governance_hook_chain.py` to wire the checker. No
other file may be created or modified without returning for re-scoping.

## Purpose

Implement a scope-triggered presence checker that closes ADIF-0014: it requires
an absorption artifact touching a legacy or external source folder to carry the
Mandatory Blind-Spot Control Block heading and a Corpus Completeness And Report
Integrity block, independent of any completeness claim, so the control cannot be
evaded by staying silent about completeness.

## Scope / Target / Owner Boundary

In scope: create
`governance/compat/check_absorption_blindspot_control_presence.py`; add a paired
test/fixture file; wire the checker into the local governance hook chain at
pre-dispatch and pre-implementation. Owner boundary: offline governance guard
only. Do not modify the two existing claim-triggered checkers, import external
content, or touch runtime/provider/public surfaces.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Required Blind-Spot heading string to detect | `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md` | `## Mandatory Blind-Spot Control Block` | `Mandatory Blind-Spot Control Block` | blind-spot standard | ACCEPT |
| Required Corpus section heading string to detect | `governance/compat/check_corpus_completeness_report_integrity.py` | `REQUIRED_SECTION` | `REQUIRED_SECTION` constant value | corpus completeness checker | ACCEPT |
| Hook chain is the wiring target | `governance/compat/run_local_governance_hook_chain.py` | checker list section | hook chain checker list | local governance hook chain | ACCEPT |
| Scope-trigger source path families | `docs/baselines/CVF_GC018_AGSG_BSH_T1_SCOPE_TRIGGERED_BLINDSPOT_PRESENCE_GUARD_2026-06-28.md` | `Scope` | `.private_reference/legacy/`; `.private_reference/external_repos/` | AGSG-BSH-T1 baseline | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Worker execution (WORKER_MUST_NOT_COMMIT)`, role=`worker`, lifecyclePhase=`pre-implementation`.

Running `governance/compat/run_adif_defect_resolver.py` for worker execution at
pre-implementation returns: ADIF-0001 (exhaustive directory claim), ADIF-0002
(provider-local interaction accepted as authority), ADIF-0007 (gate marker in
boundary prose triggers wrong evidence class), ADIF-0008 (memory-only lesson),
and ADIF-0014 (scope-triggered absorption control evaded by completeness
silence). The executor honors each: enumerate the actual changed set
(ADIF-0001), cite governed sources not provider memory (ADIF-0002), keep gate
verdict tokens out of boundary prose (ADIF-0007), record evidence in the
governed artifact rather than session memory (ADIF-0008), and implement the
scope-triggered check that ADIF-0014 prescribes rather than restating it as
guidance.

## Execution Plan

1. Read the required first reads; mirror the section-detection style of
   `check_corpus_completeness_report_integrity.py`.
2. Implement `_changed_set_touches_absorption_source(paths)` resolving the two
   scope-trigger path families against the `--base`/`--head` changed range.
3. For each changed governed artifact in scope (work order, GC-018 baseline,
   completion review), require both headings, or an allowed disposition line;
   emit a violation otherwise.
4. Wire into the hook chain at pre-dispatch and pre-implementation.
5. Add a fixture pair: one in-scope artifact with both blocks (PASS) and one
   in-scope artifact missing them (FAIL).

## Acceptance Criteria

- Checker fails an in-scope artifact missing either required block.
- Checker passes an in-scope artifact carrying both blocks (or an allowed
  disposition).
- Checker is silent for artifacts whose changed set does not touch the two
  scope-trigger path families (no false positives on unrelated work).
- Checker is wired at pre-dispatch and pre-implementation in the hook chain.
- `python governance/compat/check_adif_entry_integrity.py --enforce` stays
  COMPLIANT; ADIF-0014 `enforcementLevel`/`checkerBindings` updated to
  MACHINE_CHECKED with the new path once it exists.

## Fail Conditions

- Editing the existing claim-triggered checkers.
- Importing upstream skill content or re-opening the AGSG absorption verdict.
- Committing before review (WORKER_MUST_NOT_COMMIT).
- A scope trigger that fires on every artifact (unbounded glob) instead of the
  two named source-path families.

## Verification / Evidence

Run the new checker over both fixtures and over the real changed range
(`--base <baseHead> --head HEAD`), and run the local governance hook chain.
Record command output (secret-safe) in the completion review.

## Evidence Requirements

- Command output (secret-safe) from running the new checker over both fixtures.
- Command output from running the new checker over the real changed range.
- Hook chain output showing the checker registered at pre-dispatch and
  pre-implementation.
- `check_adif_entry_integrity.py --enforce` COMPLIANT output after the
  ADIF-0014 enforcementLevel upgrade.

## Review Gate

Reviewer confirms: scope-trigger is bounded to the two named path families
(no unbounded glob), both fixtures behave as specified, existing checkers
untouched, and ADIF-0014 upgraded to MACHINE_CHECKED with the new checker path.

## Closure Checklist

- [ ] Checker created and passes both fixtures.
- [ ] Checker wired at pre-dispatch and pre-implementation.
- [ ] No false positive on out-of-scope artifacts.
- [ ] Existing claim-triggered checkers unchanged.
- [ ] ADIF-0014 enforcementLevel and checkerBindings upgraded.
- [ ] Completion review authored with secret-safe evidence.

## Return-To-Orchestrator Conditions

Return to the orchestrator if: the scope-trigger cannot be bounded to the two
named path families without false positives, an existing checker would need
modification, or any required block format conflicts with another gate.

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | governed work-order / source-verification / autorun lane |
| Matching local-view guard | `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_knowledge_absorption_priority_compat.py` |
| Owner surface | `governance/compat/check_absorption_blindspot_control_presence.py` (to be created) |
| Disposition | ADAPT as CVF-owned governance checker hardening |
| Claim boundary | existing CVF standards remain source authority; no third-party code or claim is absorbed |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | AGSG-BSH-T1 offline governance presence checker only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | cooperating local user or hook chain invokes the checker |
| interceptionBoundary | no direct IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | scope-triggered presence guard, not execution-control enforcement |
| forbiddenExpansion | wrapper/proxy enforcement, direct interception, arbitrary commands, EDIT/COMMIT execution, provider/live, public-sync, queue/daemon, readiness remain parked |

## Foundation Storage Layout Block

NOT_APPLICABLE_WITH_REASON: this work order creates one
`governance/compat/` checker plus a paired test/fixture and one hook-chain
wiring edit. It does not create, split, relocate, or refactor a durable
governance foundation file, front door, index, or session-state artifact, so no
foundation storage/index layout change applies.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude dispatch-author orchestrator |
| Provider or surface | local workspace |
| Session or invocation | AGSG-BSH-T1 dispatch authoring, 2026-06-28 |
| Working directory | repository root |
| Command or tool surface | governed source reads, grep over AGSG artifacts, file write tool |
| Target paths | this work order; paired baseline; ADIF-0014 entry; entries README |
| Allowed scope source | AGSG-BSH-T1 GC-018 baseline and operator instruction 2026-06-28 |
| Before status evidence | scope-triggered absorption presence check did not exist; AGSG-T1 carried neither control block |
| After status evidence | dispatch packet ready for executor; ADIF-0014 recorded |
| Diff evidence | new-file creation in the AGSG-BSH-T1 dispatch batch |
| Approval boundary | authorizes dispatch only; executor implements under WORKER_MUST_NOT_COMMIT |
| Claim boundary | dispatch packet only; no checker implemented in this artifact |
| Agent type | dispatcher |
| Invocation ID | `agsg-bsh-t1-dispatch-2026-06-28` |
| Expected manifest | work order, baseline, ADIF-0014, entries README |
| Actual changed set | work order, baseline, ADIF-0014, entries README |
| Manifest delta | MATCH |

## Operator Checkpoint

None parked. Operator selected dispatch-author = Claude, executor = Codex on
2026-06-28.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: internal governance work order. No public-sync claim.

## Claim Boundary

This work order delegates implementation of one offline scope-triggered
presence checker plus its hook wiring and fixtures. It makes no runtime,
provider, public, or skill-import claim.
