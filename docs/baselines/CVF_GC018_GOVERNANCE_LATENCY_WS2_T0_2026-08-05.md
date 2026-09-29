# CVF GC-018 Baseline - Governance Latency WS2 T0 Capability Owner Decision

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: baseline

Date: 2026-08-05

Batch ID: CVF-GOVERNANCE-LATENCY-WS2-T0

dispatchBaseHead: `eb055983f75b0170fdaf057a75de9987044db9d4`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer owner: independent reviewer/closer

Worker target: documentation and source-verification worker

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-GOVERNANCE-LATENCY-WS2-T0 --title "Capability Enforcement Owner And Feasibility Decision" --date 2026-08-05 --base eb055983f --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced all placeholders with source-backed T0 scope, evidence, roles, and boundaries |
| checkerReadAheadConfirmation | dispatch-quality, handoff, ADIF, checker-read-ahead, and scaffold checkers read before final authoring |
| docOnlyNewFields | ownerCandidate, capabilityProfile, deniedCapability, allowedCapability, platformDisposition, proofCase, enforcementReceipt, T0Decision |
| claimBoundary | dispatch authoring provenance only; no runtime or enforcement claim |

## Purpose

Open only the source-native owner and feasibility decision required before any
WS2 capability-enforcement design or build. Determine whether an existing CVF
runtime surface can own a minimal zero-network profile and adversarial proof,
or whether the lane must remain parked.

## Current State

L0 closed bounded at material commit `daf7dba04`. Its independent disposition
was `ACCEPT_WITH_REVIEWER_CORRECTIONS`, and Gate A selected
`PROCEED_WS2_ONLY`. The operator's 2026-08-05 continuation instruction releases
this T0 packet preparation and documentation audit only.

Current source exposes a policy gate and injectable command-runtime executor.
The default executor is explicitly a deterministic stub. A `sandbox` decision
currently produces a delegated status, but no source-backed OS/network/process
isolation behavior has yet been established by this packet.

## Problem Statement

Prompt-only zero-network language failed in the downstream evidence, while the
rejected governed-plan runner showed that declarative policy plus arbitrary
argv/environment handling is not enforcement. Building a new wrapper or
control plane before locating the existing owner would repeat the same defect
and increase governance cost.

## Allowed Scope

- inspect provenance runtime, policy, tool, command, sandbox, environment,
  receipt, CLI/MCP, and test owners read-only;
- map Windows, Linux, and CI feasibility without executing external calls;
- identify the smallest viable existing owner and integration seam;
- distinguish current facts from proposed doc-only profile fields;
- define adversarial proof cases for `uv`, `pip`, `curl`, `wget`, remote Git,
  Python HTTP/socket, inherited credential/proxy environment, environment
  creation, and allowed tracked scripts;
- compare cheap alternatives and document program cost;
- return one decision: `OWNER_FOUND_DESIGN_READY`,
  `OWNER_FOUND_NEEDS_FOUNDATION`, `VALUE_PARKED_NO_VIABLE_OWNER`, or
  `BLOCKED_SOURCE_CONTRADICTION`.

## Forbidden Scope

- no runtime, test, checker, hook, package, profile, schema, CLI, MCP, Web, or
  workflow implementation;
- no provider/API/network call, package-manager execution, environment
  creation, dependency installation, remote Git operation, or live proof;
- no downstream or hidden distribution clone mutation;
- no governed-plan runner import, repair, copy, or promotion;
- no WS1, WS3+, broad latency program, learning-curve closure, public-sync,
  push, deployment, release, or production/readiness claim;
- no claim that the current `sandbox` label is technical isolation.

## Required Deliverables

1. Source-backed owner/feasibility audit.
2. Worker return for independent review.

The audit must include an owner candidate matrix, present-versus-missing
enforcement matrix, platform feasibility, bypass/threat matrix, cheapest viable
alternative, adversarial proof plan, receipt requirements, program-cost budget,
and exactly one T0 decision token.

## Decision / Proposed Tranche

Dispatch one documentation-only T0 source audit under
`WORKER_MUST_NOT_COMMIT`. The tranche decides ownership and feasibility; it
does not design or build enforcement.

## Evidence / Verification

Evidence consists of direct provenance source and test inspection, negative
searches, exact Git status/diff, the worker fast gate, and independent semantic
review. No runtime, provider, network, or bypass execution is valid evidence in
T0.

## Acceptance Criteria

- every current runtime fact cites a provenance source path and line/section or
  symbol;
- no downstream file is treated as authority;
- default stub execution is distinguished from real process/network control;
- `sandbox` status semantics are distinguished from isolation behavior;
- Windows, Linux, and CI receive separate feasibility dispositions;
- internal agent and external CLI/MCP consumers are accounted for separately;
- the audit tests extension of existing owners before proposing a new owner;
- negative controls cover the historical `uv` incident and all specified
  bypass families without running them;
- any proposed profile/receipt fields are labeled doc-only;
- build acceptance criteria are prepared only as a future candidate, not as
  authority;
- independent reviewer may accept, narrow, park, or block the decision;
- governance cost and a three-repair stop are explicit.

## Stop Conditions

Stop and return `BLOCKED_WITH_REASON` on source contradiction, need for a
forbidden execution, inability to distinguish current behavior from proposal,
third artifact-shape repair, unexpected worktree mutation, or any need to widen
into design implementation or build.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Gate A selected the bounded WS2 lane | VALUE_SET | `docs/reviews/CVF_GOVERNANCE_LATENCY_L0_COMPLETION_2026-08-05.md` | Gate A Recommendation, line 64 | `PROCEED_WS2_ONLY` | L0 independent completion review | ACCEPT |
| Current command runtime permits dependency injection of an executor | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/command.runtime.contract.ts` | lines 36-38 | `CommandRuntimeContractDependencies.executeTask` | `CommandRuntimeContractDependencies` | ACCEPT |
| Current default executor is a deterministic stub | LITERAL_INVARIANT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/command.runtime.contract.ts` | lines 43-67 | `defaultExecuteTask` | `CommandRuntimeContract` | ACCEPT |
| Allow and sandbox branches both invoke the injected executor | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/command.runtime.contract.ts` | lines 87-97 | `execute` | `CommandRuntimeContract` | ACCEPT |
| R3 maps to sandbox and R2 maps to review | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/policy.gate.contract.ts` | lines 39-49 | `deriveGateDecision` | `PolicyGateContract` | ACCEPT |

## Current Runtime Freshness Verification

| Runtime claim | Current source checked | Fresh result | Disposition |
|---|---|---|---|
| injectable executor exists | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/command.runtime.contract.ts` at HEAD `eb055983f` | `executeTask` dependency exists | ACCEPT |
| default executor behavior | same current source | deterministic stub only | ACCEPT |
| zero-network enforcement exists | current command/policy sources and bounded search | no such behavior is claimed by this baseline | REJECT_CURRENT_RUNTIME_CLAIM |
| sandbox is technical isolation | current command/policy sources | only decision/status/delegation semantics verified | REJECT_CURRENT_RUNTIME_CLAIM |

## New Doc-Only Fields

| Field | Purpose | Runtime claim |
|---|---|---|
| `ownerCandidate` | compare existing owner surfaces | NONE |
| `capabilityProfile` | name candidate machine profile | NONE |
| `deniedCapability` | describe a prohibited capability family | NONE |
| `allowedCapability` | describe a bounded allowed family | NONE |
| `platformDisposition` | record Windows/Linux/CI feasibility | NONE |
| `proofCase` | define an offline adversarial test case | NONE |
| `enforcementReceipt` | define future evidence needs | NONE |
| `T0Decision` | one bounded owner/feasibility token | NONE |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Baseline path | `Test-Path docs/baselines/CVF_GC018_GOVERNANCE_LATENCY_WS2_T0_2026-08-05.md` returned false before authoring | ACCEPT |
| Work-order path | `Test-Path docs/work_orders/CVF_AGENT_WORK_ORDER_GOVERNANCE_LATENCY_WS2_T0_2026-08-05.md` returned false before authoring | ACCEPT |
| Output paths | both planned audit and worker-return paths returned false before authoring | ACCEPT |
| Current owner search | direct source inspection found injectable execution and policy-gate owners but no proved zero-network isolation | ENRICH_EXISTING_FIRST |
| Collision decision | open T0 under existing Execution Plane and governance owner search; do not create a new runtime owner in this tranche | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "work-order authoring" --role dispatcher --lifecycle-phase pre-dispatch --risk-ceiling HIGH --max-results 20 --json` |
| Returned defect count | 0 |
| Disclosed defectIds | `NONE_RETURNED` |
| Dispatch impact | no registry-specific additions; canonical dispatch controls still apply |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | candidate existing Execution Plane policy/runtime seam | T0 may inspect and decide ownership only; no runtime mutation | source paths in verification block | internal-only source audit; no execution adapter | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no capability-enforcement adapter established | no CLI/MCP ingress, authentication, mutation, receipt, or enforcement behavior may be inferred | no accepted source fact proves an adapter | future adapter remains separately source-verified and separately authorized | `DEFERRED_WITH_REASON` |

## Governance Cost Budget

- one worker audit and one worker return;
- one independent reviewer pass;
- target one material closure commit plus continuity sync only if state changes;
- zero provider/network/package-manager calls;
- maximum two allowed-scope repair rounds; third repair stops the tranche;
- no second owner-search pass unless the first finds a named source
  contradiction.

## Reviewer Independence

The worker may not self-approve. A reviewer who did not author the owner
decision must verify source fidelity, current-versus-proposed separation,
platform feasibility, bypass coverage, cheap-alternative comparison, and the
single T0 decision before closure.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py` |
| literalTokensReviewed | Source Verification Block, New Doc-Only Fields, ADIF Defect Registry Disclosure, Dual Agent Surface Matrix, exact disposition tokens, Checker Source Read-Ahead Block |
| gateRunPurpose | confirm packet conformance after source-first authoring; gates are evidence, not first discovery |
| claimBoundary | baseline and dispatch readiness only; no design implementation, build, runtime, or provider proof |

## Epistemic Process Block

Expected Result / Prediction: an existing command-runtime seam is likely a
candidate owner, but its current sandbox semantics will not prove OS-level
zero-network enforcement.

Evidence Comparison Requirement: compare runtime source, tests, policy gate,
tool/command owners, CLI/MCP boundaries, and platform constraints without
averaging missing behavior into implemented behavior.

Contradiction Handling Requirement: if an existing technical isolation owner
is found, cite it directly and update the owner decision; if no viable owner is
found, park rather than invent a wrapper.

Claim Update Requirement: advance only to a future design packet when the
owner, interception boundary, platform feasibility, and proof seam are all
source-backed.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local private provenance repository |
| Session or invocation | WS2-T0 packet preparation, 2026-08-05 |
| Working directory | repository root |
| Command or tool surface | startup reads, local source inspection, ADIF resolver, apply-patch |
| Target paths | this baseline and paired work order |
| Allowed scope source | operator continuation after L0 Gate A `PROCEED_WS2_ONLY` |
| Before status evidence | HEAD `eb055983f`; clean worktree |
| After status evidence | paired documentation-only dispatch artifacts pending gates |
| Diff evidence | exact two-path packet changed set |
| Approval boundary | T0 source audit only |
| Claim boundary | no implementation, runtime proof, provider, downstream, public, or production claim |
| Agent type | dispatcher |
| Invocation ID | `governance-latency-ws2-t0-baseline-2026-08-05` |
| Expected manifest | this baseline and paired work order |
| Actual changed set | this baseline and paired work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: WS2-T0 is private provenance source analysis with no public-sync
authority.

## Claim Boundary

This baseline authorizes only a documentation and source-verification audit of
the minimal capability-enforcement owner and feasibility. It does not authorize
DESIGN implementation, SPEC implementation, BUILD, tests that execute denied
tools, provider/network use, downstream mutation, public export, push,
deployment, or a claim that zero-network enforcement exists.
