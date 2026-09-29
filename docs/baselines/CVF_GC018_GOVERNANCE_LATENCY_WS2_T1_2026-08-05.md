# CVF GC-018 Baseline - Governance Latency WS2 T1 Command And Proof Boundary Decision

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: baseline

Date: 2026-08-05

Batch ID: CVF-GOVERNANCE-LATENCY-WS2-T1

dispatchBaseHead: `b047748c527e3321ca8724e235115729f77c5447`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer owner: independent reviewer/closer

Worker target: documentation and source-verification worker

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-GOVERNANCE-LATENCY-WS2-T1 --title "Command Contract And Enforcement Proof Boundary Decision" --date 2026-08-05 --base b047748c5 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with a bounded command-demand and enforcement-boundary source audit |
| checkerReadAheadConfirmation | dispatch-quality, handoff, ADIF, checker-read-ahead, scaffold, external-intake, and foundation-layout checkers read before final authoring |
| docOnlyNewFields | commandDemand, effectClass, environmentContract, transitiveChildBoundary, enforcementBoundary, proofBoundary, T1Decision |
| claimBoundary | dispatch authoring provenance only; no design implementation, runtime, provider, live, public, Web, CLI, or MCP behavior claim |

## Purpose

Resolve the bounded prerequisite left by WS2-T0: identify the exact commands
actually demanded by the candidate WS2 role and determine whether a cheap,
source-backed environment, effect, network, and transitive-child enforcement
boundary exists. This is a documentation decision before design, not design or
build authority.

## Current State

L0 closed at `daf7dba04` with Gate A `PROCEED_WS2_ONLY`. WS2-T0 closed at
`0f2fc9c9d`, with the final continuity anchor at `b047748c5`, and accepted the
current governed launcher only for fixed-profile command admission. Technical
zero-network isolation remains unproven and parked.

## Problem Statement

An allowlist can prevent unknown profile selection, but an allowed executable
or tracked script may still inherit credentials or proxies, create child
processes, mutate files, or open sockets. A credible WS2 design cannot begin
until command demand and the enforcement/proof boundary are source-backed, or
the zero-network lane is explicitly parked as too costly.

## Allowed Scope

- inspect current provenance source, tests, scripts, hooks, and governed command
  callers read-only;
- inventory exact command demand for the smallest useful local role;
- classify executable, argv, cwd, environment, filesystem effect, child
  process, network, and receipt requirements;
- assess existing OS/runtime enforcement seams for Windows, Linux, and CI using
  current local sources only;
- compare fixed-profile admission, reduced-environment execution, OS-native
  isolation, and parking;
- return one bounded T1 decision token.

## Forbidden Scope

- no DESIGN implementation, SPEC implementation, BUILD, runtime or test-source
  change;
- no execution of adversarial commands, package manager, remote Git, socket,
  provider/API, credential, or live-proof path;
- no environment creation, dependency installation, downstream/public mutation,
  push, deployment, or public export;
- no import, copy, repair, or promotion of the downstream governed-plan runner;
- no claim that allowlisting, `shell: false`, sandbox labels, or redaction prove
  technical zero-network isolation.

## Required Deliverables

1. A source-backed command-demand and enforcement-proof-boundary audit.
2. A no-commit worker return for independent review.

## Decision / Proposed Tranche

Dispatch one documentation-only T1 source audit under
`WORKER_MUST_NOT_COMMIT`. It may recommend a later bounded DESIGN packet, retain
fixed-profile admission only, park zero-network for lack of source-backed demand,
or block on a source contradiction. It cannot implement its recommendation.

## Evidence / Verification

Evidence is limited to direct current-source inspection, exact bounded searches,
Git status/diff, machine gates, and independent semantic review. No process,
network, provider, or bypass execution is valid evidence in T1.

## Acceptance Criteria

- exact current profiles and current callers are inventoried without treating
  repository-wide developer commands as agent-role demand;
- each proposed allowed command has a source-backed consumer and value case;
- executable, immutable argv, cwd, environment, filesystem effects, child
  processes, network, and receipt fields are separated;
- inherited credential/proxy and transitive-child risks are explicit;
- Windows, Linux, and CI are assessed independently without portability claims
  unsupported by source;
- the cheapest option satisfying the same claim is preferred;
- inability to prove technical isolation parks or narrows the claim;
- one T1 decision is returned and independently reviewed;
- governance cost and a third-repair stop are explicit.

## Stop Conditions

Stop on third repair, source contradiction, absent command-demand evidence,
need for a forbidden execution, unexpected mutation, or need to widen into
design implementation or build. Missing technical isolation is a valid parked
result, not permission to invent a control plane.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Gate A allows only a future separately authorized WS2 packet | VALUE_SET | `docs/reviews/CVF_GOVERNANCE_LATENCY_L0_COMPLETION_2026-08-05.md` | Gate A Recommendation, lines 64-71 | `PROCEED_WS2_ONLY` | L0 independent completion review | ACCEPT |
| WS2-T0 found fixed-profile admission but not technical isolation | VALUE_SET | `docs/reviews/CVF_GOVERNANCE_LATENCY_WS2_T0_COMPLETION_2026-08-05.md` | Decision Review, lines 77-84 | `OWNER_FOUND_NEEDS_FOUNDATION` | WS2-T0 independent completion review | ACCEPT |
| Current launcher exposes exactly three frozen profiles | VALUE_SET | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | lines 33-72 | `GOVERNED_COMMAND_PROFILE_IDS` | `getGovernedCommandProfile` | ACCEPT |
| Direct runner spawns without a shell but supplies no explicit child environment | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | lines 104-120 | `DirectGovernedCommandRunner.run` | `GovernedCommandRunner` | ACCEPT |
| Current response explicitly rejects external interception proof | LITERAL_INVARIANT | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | lines 186-202 and 493-509 | `externalInterceptionProved` | `GovernedCommandLauncherResponse` | ACCEPT |
| CLI accepts profile, workspace, cwd, and json options only | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-exec.ts` | lines 19-53 | `parseGovernedExecArgs` | `GovernedExecCliArgs` | ACCEPT |
| CLI wires the direct runner into the launcher | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-exec.ts` | lines 61-87 | `runGovernedExecCli` | `DirectGovernedCommandRunner` | ACCEPT |
| Tests reject arbitrary executable and argument surfaces | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.test.ts` | lines 369-391 | `cvf-governed-exec parser` | `parseGovernedExecArgs` tests | ACCEPT |

## Current Runtime Freshness Verification

| Runtime claim | Current source checked | Fresh result | Disposition |
|---|---|---|---|
| fixed-profile command admission exists | governed launcher and CLI at HEAD `b047748c5` | three fixed profiles plus profile-only CLI | ACCEPT |
| child environment is minimized | governed launcher spawn options | no explicit `env` option | REJECT_CURRENT_RUNTIME_CLAIM |
| network and transitive children are technically intercepted | launcher response and bounded source search | `externalInterceptionProved` remains false | REJECT_CURRENT_RUNTIME_CLAIM |
| exact future WS2 role demand is already defined | current profile registry and caller search | not established by this baseline | REJECT_CURRENT_RUNTIME_CLAIM |

## New Doc-Only Fields

| Field | Purpose | Runtime claim |
|---|---|---|
| `commandDemand` | source-backed need for one exact command | NONE |
| `effectClass` | declared filesystem/process/network effect family | NONE |
| `environmentContract` | proposed inherited/allowed environment boundary | NONE |
| `transitiveChildBoundary` | proposed child-process containment boundary | NONE |
| `enforcementBoundary` | candidate technical owner and mechanism | NONE |
| `proofBoundary` | future adversarial evidence limit | NONE |
| `T1Decision` | one bounded decision token | NONE |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Four planned artifact paths | `Test-Path` returned false for baseline, work order, audit, and worker return before authoring | ACCEPT |
| Current caller search | `rg` found production use through `governed-exec.ts` and evidence-auditor type imports; launcher invocation otherwise appears in focused tests | SOURCE_AUDIT_REQUIRED |
| Current profile search | launcher source defines `git-status`, `git-diff-check`, and `approval-marker-write` only | ACCEPT |
| Collision decision | continue the existing governed launcher owner; create no new runtime owner in T1 | ENRICH_EXISTING_FIRST |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "work-order authoring" --role dispatcher --lifecycle-phase pre-dispatch --risk-ceiling HIGH --max-results 20 --json` |
| Returned defect count | 0 |
| Disclosed defectIds | `NONE_RETURNED` |
| Dispatch impact | canonical source-verification and handoff controls remain binding |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | candidate governed launcher route | documentation audit only; no command execution or profile mutation | verified launcher and CLI source | existing fixed-profile admission only | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | `cvf-governed-exec` CLI only; MCP enforcement not established | no authentication, network-isolation, or generalized external-agent claim | CLI package and source | later source-verified adapter packet required | `DEFERRED_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | accepted L0 evidence -> WS2-T0 provenance owner audit -> WS2-T1 provenance boundary audit -> independent review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | WS2-T1 audit and independent review |
| Disposition | adapt the accepted learning into a provenance-native source decision; do not import the downstream runner |
| Claim boundary | routing evidence only; downstream remains read-only and non-authoritative |

## Governance Cost Budget

- one audit, one worker return, and one independent review;
- target one material closure commit plus continuity sync only if state changes;
- zero provider, network, package-manager, or bypass calls;
- maximum two allowed-scope repair rounds; third repair stops;
- if exact role demand is not source-identifiable in one bounded pass, park it.

## Reviewer Independence

The worker may not self-approve. The reviewer must not have authored the T1
decision and must verify demand evidence, claim narrowing, enforcement gaps,
platform limits, cheap alternatives, and the single decision token.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_foundation_storage_layout.py` |
| literalTokensReviewed | Source Verification Block, New Doc-Only Fields, ADIF Defect Registry Disclosure, Dual Agent Surface Matrix, Checker Source Read-Ahead Block, exact decision tokens |
| gateRunPurpose | confirm packet conformance after source-first authoring; gates are evidence, not first discovery |
| claimBoundary | baseline and dispatch readiness only; no design implementation, build, runtime, or provider proof |

## Epistemic Process Block

Expected Result / Prediction: the three frozen profiles will support only a
narrow local command-demand case, while technical zero-network isolation will
remain unsupported unless a separate current source owner is found.

Evidence Comparison Requirement: compare actual callers and role value against
launcher, environment, process, network, platform, and receipt sources. Do not
convert repository-wide developer commands into role demand.

Contradiction Handling Requirement: retain missing demand or enforcement as a
parked result; use the blocked decision only for conflicting current sources.

Claim Update Requirement: recommend later design only when both exact command
demand and a source-backed enforcement/proof boundary are present.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local private provenance repository |
| Session or invocation | WS2-T1 packet preparation, 2026-08-05 |
| Working directory | repository root |
| Command or tool surface | startup reads, local source inspection, ADIF resolver, scaffold helper, apply-patch |
| Target paths | this baseline and paired work order |
| Allowed scope source | operator continuation after WS2-T0 closure |
| Before status evidence | HEAD `b047748c5`; clean worktree |
| After status evidence | paired documentation-only dispatch artifacts pending gates |
| Diff evidence | exact two-path packet changed set |
| Approval boundary | T1 documentation audit only |
| Claim boundary | no design implementation, build, execution, provider, downstream, public, or production claim |
| Agent type | dispatcher |
| Invocation ID | `governance-latency-ws2-t1-baseline-2026-08-05` |
| Expected manifest | this baseline and paired work order |
| Actual changed set | this baseline and paired work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | documentation-only command-demand and enforcement-boundary analysis |
| claimDisposition | CLAIM_REJECTED: no execution-control or runtime-enforcement behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt exists or is required for T1 |
| actionEvidence | ACTION_EVIDENCE_PRESENT: local source and Git evidence only |
| invocationBoundary | read-only provenance inspection plus a paired dispatch packet |
| interceptionBoundary | no direct process, network, filesystem, environment, shell, IDE, CLI, MCP, or provider interception |
| claimLanguage | exact demand and future enforcement/proof boundary only |
| forbiddenExpansion | runtime, bypass execution, provider/live, downstream, public, deployment, readiness, and universal enforcement |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: WS2-T1 is private provenance source analysis with no public-sync
authority.

## Claim Boundary

This baseline authorizes only a documentation and source-verification audit of
the exact WS2 command demand and technical enforcement/proof boundary. It does
not authorize DESIGN implementation, SPEC implementation, BUILD, denied-tool
execution, provider/network use, downstream mutation, public export, push, or
deployment.
