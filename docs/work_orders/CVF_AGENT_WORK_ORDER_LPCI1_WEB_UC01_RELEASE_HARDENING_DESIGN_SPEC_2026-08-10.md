# CVF Agent Work Order - LPCI1 Web UC-01 Release Hardening Design Spec

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Date: 2026-08-10

Batch ID: LPCI1-WEB-UC01-RELEASE-HARDENING-DESIGN-SPEC

Dispatch base head: `f391ec180`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated documentation-design worker

Reviewer/closer: primary agent

Worker return path: `docs/reviews/CVF_LPCI1_WEB_UC01_RELEASE_HARDENING_DESIGN_SPEC_WORKER_RETURN_2026-08-10.md`

## Dispatch Prompt Envelope

Role: delegated documentation-design worker.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI1_WEB_UC01_RELEASE_HARDENING_DESIGN_SPEC_2026-08-10.md`.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-08-10; current repository source wins over prior summaries.

Do-not-misread notes: authority is repository-local DESIGN/SPEC only; no BUILD, secret, live, deployment, public, or readiness authority.

Required first actions: read startup, guards, `DESIGN.md`, packet, accepted completion, current source, and applicable checkers; then run pre-implementation.

Return contract: create exactly three outputs, run the full gates, leave staging empty and HEAD unchanged, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` without reviewer acceptance.

## Purpose

Produce a source-verified release-hardening architecture DESIGN, a normative
SPEC, and a full worker return for UC-01. Define finite owners and acceptance
contracts for every readiness gap before any BUILD authority can be considered.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id LPCI1-WEB-UC01-RELEASE-HARDENING-DESIGN-SPEC --title "LPCI1 Web UC-01 Release Hardening Design Spec" --date 2026-08-10 --base f391ec180 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "UC-01 release-readiness discovery accepted at 944fdfc56" --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit Web documentation profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | completed dependencies, source verification, role routing, exact manifest, design/spec requirements, return contract, and boundaries |
| checkerReadAheadConfirmation | listed in Checker Source Read-Ahead Block |
| docOnlyNewFields | listed in New Doc-Only Fields |
| claimBoundary | packet authoring only |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| readiness discovery | accepted completion at `docs/reviews/CVF_LPCI1_WEB_UC01_RELEASE_READINESS_DISCOVERY_COMPLETION_2026-08-10.md`, material commit `944fdfc56` | must select DESIGN/SPEC-only continuation | SATISFIED |
| operator authority | original phrase and exact canonical token recorded in baseline and this order | explicit approval | SATISFIED |
| dispatch base | clean `f391ec180` | no unrelated changes | SATISFIED |

## Worker Autonomy / No-Question Rule

Repair allowed-scope documentation/checker failures directly. Return only for
a source contradiction, forbidden-scope need, failed mandatory gate outside the
three-path ownership, or missing authority that prevents completion.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`LPCI web UC-01 release hardening design spec`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver query executed: `python governance/compat/run_adif_defect_resolver.py --task-class "LPCI web UC-01 release hardening design spec" --role dispatcher --lifecycle-phase pre-dispatch --json`

Returned defect count: 0. Disclosed defectIds: none.

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | dispatch status, dependency rows, source-verification dispositions, worker trace, delta boundary, corpus/value wording, and public disposition |
| gateRunPurpose | confirmation after direct source and scaffold read-ahead |
| claimBoundary | dispatch quality only; no design acceptance or runtime proof |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| readiness matrix and next tranche | VALUE_SET | `docs/reviews/CVF_LPCI1_WEB_UC01_RELEASE_READINESS_DISCOVERY_COMPLETION_2026-08-10.md` | Findings / Position | `minimumSafeNextTranche` | reviewer completion | ACCEPT |
| route authorization | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | lines 115 onward | `authorizeRouteGovernanceProof` | `POST` | ACCEPT |
| authorization modes | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | `authorizeRouteGovernanceProof` | `authorizeRouteGovernanceProof` | route proof | ACCEPT |
| existing config binding | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/provider-binding.ts` | binding construction | `LPCI_LLM_API_KEY` | LPCI provider binding | ACCEPT |
| generic limiter | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | line 210 | `getRateLimiter` | limiter factory | ACCEPT |
| query route limiter binding | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | imports and POST | `getRateLimiter` | `POST` | REJECT |
| current audit receipt | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | response branches | `auditReceipt` | `POST` | ACCEPT |
| current provider timeout | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/provider-binding.ts` | provider execution | `AbortSignal` | binding | REJECT |

## New Doc-Only Fields

The following are proposed contract names, not current source facts:
`releaseRolePolicy`, `hostedConfigLifecycle`, `queryQuotaPolicy`,
`durableAuditProjection`, `providerAttemptTimeout`, `releaseHealthContract`,
and `promotionRollbackContract`. Each must remain labeled `DOC_ONLY_NEW` in the
worker outputs until a separately authorized BUILD implements it.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| output paths | all three returned False before dispatch authoring | PASS |
| duplicate owner | existing auth, binding, limiter, health, and gateway owners must be composed, not replaced | PASS |
| proposed names | all new contract names are labeled `DOC_ONLY_NEW` | PASS |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| Intake source | operator approval of the immediately preceding exact DESIGN/SPEC-only proposal |
| scope classification | bounded repository-local documentation design/spec |
| risk sensitivity | medium; release controls touch auth, credentials, quota, audit, and recovery contracts but no execution is authorized |
| Route | `MULTI_AGENT_MULTI_ROLE` |
| selected role route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | primary dispatcher/reviewer/closer/steward plus one no-commit worker |
| escalation condition | source contradiction, forbidden scope, or unrepairable mandatory gate |

## Evidence Reuse And Encoding Plan

| Field | Value |
|---|---|
| prior evidence reused | accepted readiness completion at material commit `944fdfc56` |
| refresh rule | worker re-reads current runtime and records drift before design decisions |
| verificationMode | direct current-source refresh plus range-aware governance gates |
| external evidence | N/A with reason: repository-local sources only |
| encoding | ASCII by default; source paths and protocol literals preserved exactly |
| unicodePathHandling | no Unicode path is consumed; do not normalize or rename existing paths |
| Unicode exception | N/A with reason: operator wording is paraphrased in ASCII and canonical token is authoritative for packet routing |

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: current runtime source must be refreshed at the worker execution base because design contracts cannot rely only on the prior discovery snapshot.

unicodePathHandling: use literal paths and UTF-8-safe readers for governed artifact reads.

## Authority Chain

Operator approval -> primary dispatcher packet -> delegated no-commit worker ->
independent primary reviewer/closer -> reviewer-owned material commit -> separate
session-sync commit. No downstream authority is inherited.

## Agent Roles

The worker owns only the three fulfillment outputs. The primary agent owns
dispatch, independent review, repair direction, closure decision, commits, and
session continuity. The operator owns any later BUILD, live, deploy, or public
checkpoint.

## Required First Reads

Read `CVF_SESSION_MEMORY.md`, bootstrap/state, active handoff, guard orientation,
literal gotchas, `DESIGN.md`, paired packet, readiness completion, cited source,
and applicable checker source before writing.

## Pre-Flight Checks

Confirm clean execution HEAD, empty staging, absent output collisions, correct
active handoff, no unrelated changes, ADIF worker query, and mandatory
pre-implementation PASS before authoring.

## Write Ownership

Worker may create only the three fulfillment-manifest paths. It must not edit
the packet, roadmap, runtime, tests, configuration, UI, session state, or any
other file.

## Agent Handoff Contract Control Block

Contract source; archive classification N/A:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | primary dispatcher/reviewer/closer/commit/session steward plus one no-commit documentation worker |
| phase | DESIGN/SPEC worker execution, then independent reviewer closure conversion |
| baseHeadFor(phase) | dispatchBaseHead=`f391ec180`; executionBaseHead=worker capture after dispatch/session commits; closureBaseHead=reviewer capture |
| changedSetScope(phase) | worker exactly three fulfillment paths; reviewer owns packet, roadmap, completion, commit, and continuity paths |
| traceScope(phase, actor) | worker trace covers its reads, three outputs, and gates; reviewer trace separately covers review, repair, closure, commits, and sync |
| commitOwner(phase) | primary reviewer/closer; worker commit forbidden |
| crossBatchIsolation | worker starts from clean synchronized HEAD and must not absorb unrelated changes |
| nextMoveSurfaces | reviewer alone updates roadmap and protected continuity after accepted material commit |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_LPCI1_WEB_UC01_RELEASE_HARDENING_DESIGN_SPEC_COMPLETION_2026-08-10.md` |
| reviewerOwnedClosurePaths | paired packet, LPCI roadmap, completion review, then separate session-sync surfaces |
| closureOwner | primary reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Roadmap-to-Work-Order Trace Matrix

| Readiness requirement | Work-order instruction | Required evidence |
|---|---|---|
| preserve route authorization | define UC-01 role policy around existing proof | actor/role/service identity decision and fail-close cases |
| complete hosted config lifecycle | specify atomic three-variable ownership and promotion | owner, environment, rotation, startup, and recovery contracts |
| bind rate limits and quotas | specify query and provider-attempt controls | identity keys, thresholds/config ownership, fail-close and receipt projection |
| durable audit/observability | specify minimized sink and server telemetry | exact allowed fields, retention/access owner, correlations, prohibited content |
| timeout and health | specify bounded provider timeout and side-effect-free health | deadlines, diagnostic mapping, dependency states, no implicit retry |
| deploy/rollback | specify promotion, smoke, rollback and recovery | offline smoke, separately authorized hosted proof, rollback trigger and owner |
| public boundary | keep private-only | explicit deferred disposition and fresh public packet requirement |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| `docs/audits/CVF_LPCI1_WEB_UC01_RELEASE_HARDENING_DESIGN_2026-08-10.md` | create source-backed architecture decision and option comparison |
| `docs/reference/CVF_LPCI1_WEB_UC01_RELEASE_HARDENING_SPEC_2026-08-10.md` | create normative finite acceptance specification |
| `docs/reviews/CVF_LPCI1_WEB_UC01_RELEASE_HARDENING_DESIGN_SPEC_WORKER_RETURN_2026-08-10.md` | create full checker-safe execution return |

All other paths are forbidden to the worker.

## Required DESIGN Decisions

1. Preserve the existing fail-closed route proof and define an explicit UC-01
   session-role allowlist plus service-identity policy owner.
2. Reuse the existing LPCI provider binding, Model Gateway, limiter, health,
   and monitoring owners; reject a parallel generic owner.
3. Define the atomic `LPCI_LLM_API_KEY` / `LPCI_LLM_MODEL` /
   `LPCI_LLM_ENDPOINT` hosted lifecycle without reading secret values.
4. Define distributed query and provider-attempt quota semantics keyed by
   authenticated actor or service identity, with fail-closed configuration.
5. Define a durable minimized audit sink and server telemetry. Raw prompt,
   answer, provider body, headers, tokens, and secrets are prohibited.
6. Define one bounded provider-attempt timeout, safe error mapping, and zero
   automatic retry in this design.
7. Define side-effect-free readiness/health states for auth, config, limiter,
   audit sink, route composition, and provider lane without making a live call.
8. Define environment promotion, deterministic smoke, separately authorized
   hosted/live smoke, rollback trigger, recovery owner, and migration stance.
9. Bound UI implications to information and error states under `DESIGN.md`.
10. Provide a future BUILD manifest and deterministic test matrix without
    editing or executing runtime/tests.

## Required SPEC Shape

The normative specification must use MUST/MUST NOT/SHOULD language and include:

- named current owners and `DOC_ONLY_NEW` future interfaces;
- role and service-identity admission matrix;
- three-key atomic configuration states;
- rate/quota identity and decision matrix;
- minimized durable audit schema and prohibited fields;
- timeout, retry, safe diagnostic, and health state tables;
- promotion, smoke, rollback, recovery, and migration rules;
- deterministic acceptance cases with observable results;
- lifecycle interlock:
  DESIGN/SPEC accepted -> fresh BUILD authority -> deterministic tests -> fresh
  hosted/live/deploy authority;
- explicit statement that authority never inherits across those arrows.

## Execution Plan

1. Capture execution base and run mandatory pre-implementation.
2. Refresh every cited current-source fact without secrets or execution.
3. Author design options, select composition, and define ownership.
4. Author normative matrices and deterministic future acceptance cases.
5. Author the full return, run all gates, and leave staging empty.

## Evidence Requirements

Record source citations, current-versus-document-only separation, option
comparison, selected owners, eight-dimension contract matrix, deterministic
case matrix, exact manifest, command outcomes, HEAD/staging evidence, and zero
forbidden-action counts.

## Acceptance Criteria

| ID | Criterion | Fail condition |
|---|---|---|
| AC-01 | exact three-path worker manifest | any other path changes |
| AC-02 | all eight readiness dimensions resolved into owners/contracts | gap restated without a decision |
| AC-03 | current symbols and future names separated | document-only interface claimed implemented |
| AC-04 | no parallel generic auth/provider/limiter/audit/health owner | duplicate owner remains selectable |
| AC-05 | finite fail-closed matrices and minimized observability | raw sensitive payload persistence allowed |
| AC-06 | one timeout and zero automatic retry | retry or live execution implied |
| AC-07 | release chain has fresh authority at each transition | BUILD/deploy inherited from this packet |
| AC-08 | full worker-return fast gate passes | checker substitution or incomplete return |
| AC-09 | staging empty and HEAD unchanged | worker stages or commits |

## Worker Output Checker Read-Ahead Mandate

Before writing each output, read the checker sources applicable to audit,
reference, and worker-return paths. Write real headings before mentioning them
in prose. Include applicable source verification, external-input disposition,
corpus/value, AOT, Delta, public disposition, and claim-boundary shapes.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_LPCI1_WEB_UC01_RELEASE_HARDENING_DESIGN_SPEC_WORKER_RETURN_2026-08-10.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The return must record execution base, current source refresh, exact manifest,
command results, epistemic comparison, finding-to-governance disposition,
external-input status, corpus/value N/A reasons, staging, unchanged HEAD,
zero forbidden actions, and `COMPLETE_PENDING_REVIEW`.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD --serial
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/check_corpus_scan_registry.py
git diff --check
git diff --name-status
git diff --cached --name-only
git status --short
git rev-parse --short HEAD
```

No runtime test, secret read, provider/network call, browser/server action, or
hosted/deploy command is required or allowed.

## Web/UI Claim Boundary

| Field | Value |
|---|---|
| DESIGN.md read | dispatcher confirmed; worker must confirm independently |
| UI claim boundary | response/error/health information contracts only; no UI implementation or production claim |

## Review Gate

Worker output remains pending until the primary reviewer independently checks
source fidelity, option selection, all matrices, manifest, and gates. Reviewer
may request bounded repairs only within the three worker paths.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` when all criteria and gates pass. Return
`BLOCKED_WITH_REASON` only for contradictory current source, mandatory
forbidden-path expansion, missing authority, or a repeated gate blocker that
cannot be repaired inside the exact three-path scope.

## Operator Checkpoint

This DESIGN/SPEC checkpoint is released. BUILD, runtime/test/config/UI change,
secret/private access, provider/network/live, hosted deployment/rollback,
public-sync, push, production, and readiness remain parked behind fresh exact
operator authority.

## Closure Checklist

- [ ] exact three worker outputs returned
- [ ] current and future contract names separated
- [ ] all eight dimensions have owners and observable acceptance
- [ ] zero runtime/secret/live/deploy/public action
- [ ] worker staging empty and HEAD unchanged
- [ ] full fast gate passes
- [ ] independent reviewer verdict recorded

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Current status |
|---|---|---|---|
| Work order | this file | `Status: DISPATCH_READY` | PASS |
| Completion review | `docs/reviews/CVF_LPCI1_WEB_UC01_RELEASE_HARDENING_DESIGN_SPEC_COMPLETION_2026-08-10.md` | reviewer-owned future artifact | N/A with reason: not yet reviewed |
| Roadmap state | `docs/roadmaps/CVF_LPCI1_WEB_CONTEXT_TO_LLM_USE_CASE_ROADMAP_2026-08-09.md` | reviewer-owned future closure update | N/A with reason: not yet reviewed |
| Registry JSON | N/A with reason: no corpus registry mutation | no change | N/A with reason |
| Registry Markdown | N/A with reason: no corpus registry mutation | no change | N/A with reason |
| External evidence digest | N/A with reason: repository-local sources only | no intake | N/A with reason |
| Session continuity | protected session surfaces | separate reviewer sync | N/A with reason: after material commit |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | primary dispatcher |
| Provider or surface | private provenance repository |
| Session or invocation | `lpci1-web-uc01-release-hardening-design-spec-dispatch-2026-08-10` |
| Working directory | repository root |
| Command or tool surface | startup/guard/source reads, scaffold, ADIF, patch authoring, governance gates, Git |
| Target paths | paired baseline and this work order |
| Allowed scope source | original approval phrase plus canonical DESIGN/SPEC-only token |
| Before status evidence | clean worktree at `f391ec180` |
| After status evidence | exact paired dispatch packet before commit |
| Diff evidence | `git diff --name-status`; `git status --short` |
| Approval boundary | repository-local UC-01 release-hardening DESIGN/SPEC dispatch only |
| Claim boundary | no acceptance, BUILD, runtime, live, deployment, or public action |
| Agent type | dispatcher/reviewer role, not worker |
| Invocation ID | `lpci1-web-uc01-release-hardening-design-spec-dispatch-2026-08-10` |
| Expected manifest | paired dispatch paths |
| Actual changed set | paired dispatch paths before commit |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | repository-local design/spec documentation |
| claimDisposition | CLAIM_REJECTED: no runtime enforcement or readiness is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no provider/runtime receipt is created |
| actionEvidence | ACTION_EVIDENCE_PRESENT only for repository reads, documentation, gates, and governed Git operations |
| invocationBoundary | local repository tooling only |
| interceptionBoundary | no runtime interception, wrapper, route, provider, browser, server, or hosted execution |
| claimLanguage | source-backed architecture proposal pending independent review |
| forbiddenExpansion | runtime/test/config/UI, secret/private, provider/network/live, deploy/rollback execution, public-sync, push, production |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private source-specific design/spec packet; no public export authority.

## Claim Boundary

This work order authorizes exactly three uncommitted documentation outputs. It
does not accept them or authorize BUILD, source/test/config/UI mutation,
secret/private access, browser/server/provider/network/live/cloud action,
deployment, rollback execution, public-sync, push, production, or readiness.
