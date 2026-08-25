# CVF Agent Work Order - EAFR-R1B Baseline Variance Authority Adjudication

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: EAFR-R1B-BASELINE-VARIANCE-AUTHORITY-ADJUDICATION

Dispatch base head: 02cc34a4f

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated documentation reviewer

Reviewer/closer: independent orchestrator/reviewer/closer

Worker return path: `docs/reviews/CVF_EAFR_R1B_BASELINE_VARIANCE_AUTHORITY_ADJUDICATION_WORKER_RETURN_2026-08-25.md`

## Dispatch Prompt Envelope

Role: delegated no-commit documentation reviewer for EAFR-R1B.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_EAFR_R1B_BASELINE_VARIANCE_AUTHORITY_ADJUDICATION_2026-08-25.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: R1A is closed bounded at `ef142bfb2`; continuity is
committed at `02cc34a4f`.

Do-not-misread notes: this packet does not authorize tests, build, environment
or key access, live/provider/network actions, acceptance waiver, or source fix.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, this packet, paired baseline, cited R1/R1A artifacts, and applicable
checker sources before writing.

Return contract: create only the named worker return, leave it uncommitted and
return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Produce an independent, source-backed authority decision on the remaining R1
acceptance variance without silently lowering the parent contract.

## Authority Chain

Frozen doctrine and operating model route through `AGENTS.md`, the EAFR
roadmap, paired R1B baseline, this work order, committed R1/R1A evidence, and
applicable machine checkers. Worker opinion and historical precedent are not
variance authority.

## Agent Roles

- Operator: owns standing dependency-ordered EAFR authority.
- Worker: performs read-only source adjudication and writes one return.
- Reviewer/closer: independently accepts or rejects the decision and commits.

## Required First Reads

Read `CVF_SESSION_MEMORY.md`, bootstrap read model, active handoff, guard
orientation, literal gotchas, paired R1B baseline, this work order, cited
R1/R1A artifacts, and worker-return/trace/delta checker sources.

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| intake summary | committed R1 acceptance and execution-base variance evidence |
| scope classification | BOUNDED_DOCUMENTATION_AUTHORITY_ADJUDICATION |
| primary task class | review |
| risk sensitivity | ELEVATED because acceptance authority is at issue |
| selected role route | MULTI_AGENT_MULTI_ROLE |
| orchestration requirement | no-commit worker plus independent reviewer |
| role separation basis | worker cannot close or waive the contract it adjudicates |
| escalation condition | canonical source contradiction or forbidden action needed |

## Pre-Flight Checks

- Capture `git rev-parse HEAD`; require clean worktree and empty staging.
- Confirm named worker return does not exist.
- Confirm R1A completion exists at current HEAD ancestry.
- Stop on any source/hash/path contradiction.

## Write Ownership

Write exactly the named worker return. Every other path is read-only.

## Allowed Scope

Only writable path:

- `docs/reviews/CVF_EAFR_R1B_BASELINE_VARIANCE_AUTHORITY_ADJUDICATION_WORKER_RETURN_2026-08-25.md`

All repository sources are read-only. Do not run npm, Vitest, TypeScript,
build, environment, credential, network, provider, live, deploy, public-sync,
push, stage, commit, stash, reset, install or cleanup commands.

## Required Analysis

1. Quote no more than needed and map every R1 acceptance criterion to:
   `PASS`, `PRE_EXISTING_EXACT_MATCH`, `ENVIRONMENT_ONLY_CURRENT`,
   `REJECTED_AS_EVIDENCE`, or `UNSATISFIED`.
2. Search current CVF authority for an explicit rule permitting closure from
   execution-base exact variance. A historical precedent is not authority.
3. Treat the detached baseline build as rejected evidence unless a committed
   source proves otherwise; do not rerun it.
4. Select exactly one Decision Outcome from the paired baseline.
5. If keeping R1 blocked, name the smallest next repair/authority route without
   implementing it. R2 remains held.

## Execution Plan

1. Capture base and exact one-path boundary.
2. Read every cited authority/evidence surface.
3. Build the criterion and authority matrices before drafting a decision.
4. Select one exact outcome and state the smallest next route.
5. Scaffold the worker return, run its fast gate, and leave it uncommitted.

## Acceptance Criteria

- [ ] criterion-by-criterion matrix is complete;
- [ ] authority source has exact path and section or is source-not-found;
- [ ] decision token is exactly one allowed outcome;
- [ ] R1A remains closed and is not overclaimed as R1 closure;
- [ ] zero execution/external effect and exact one-path manifest;
- [ ] worker-return fast gate passes; staging empty; HEAD unchanged.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "EAFR-R1B",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "PURE_LOCAL_IMPLEMENTATION",
    "authorityImpact": "USES_EXISTING_OWNER",
    "externalEffect": "NONE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "NAMED_FILES",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "KNOWN_PATTERN"
  },
  "pathFamilies": [
    "docs/reviews/",
    "docs/baselines/CVF_GC018_EAFR_R1B_BASELINE_VARIANCE_AUTHORITY_ADJUDICATION_2026-08-25.md",
    "docs/work_orders/CVF_AGENT_WORK_ORDER_EAFR_R1B_BASELINE_VARIANCE_AUTHORITY_ADJUDICATION_2026-08-25.md",
    "docs/roadmaps/CVF_EAFR_REMEDIATION_ROADMAP_2026-08-25.md"
  ],
  "claims": ["source-backed R1 variance authority decision"],
  "requiredProof": ["acceptance matrix", "authority search", "exact decision token", "worker-return fast gate", "independent review"],
  "operatorCheckpoints": [],
  "forbiddenEffects": ["test or build execution", "environment or credential access", "provider/network/live call", "source mutation", "worker stage or commit", "public/deploy/push"],
  "sourceEvidence": {"selectedFilesFullyRead": true, "corpusReceiptRef": null, "completenessClaimChanged": false}
}
```

Expected route: `ROUTED_SHADOW`, profile `P3_ELEVATED`, selective execution
false, legacy disposition `RUN_FULL_LEGACY_BUNDLE`.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id EAFR-R1B-BASELINE-VARIANCE-AUTHORITY-ADJUDICATION --title "CVF EAFR-R1B Baseline Variance Authority Adjudication" --date 2026-08-25 --base 02cc34a4f --commit-mode WORKER_MUST_NOT_COMMIT --dependency "R1A closed bounded at ef142bfb2" --include-worker-return-skeleton --stdout` |
| generatedProfile | generic no-commit worker dispatch |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | bounded documentation-only decision, exact outcomes, forbidden execution and one-path return |
| checkerReadAheadConfirmation | dispatch, worker-return, trace and delta checkers read before authoring |
| docOnlyNewFields | `criterionStatus`; `varianceAuthorityDisposition` |
| claimBoundary | scaffold provenance only; no variance or closure claim |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| R1A repair | `docs/reviews/CVF_EAFR_R1A_NON_LIVE_TEST_RUNNER_EXTENSION_COVERAGE_COMPLETION_2026-08-25.md`; commit `ef142bfb2` | bounded R1A closure committed | RELEASED_FOR_R1B_ONLY |

## Worker Autonomy / No-Question Rule

Resolve routine documentation and checker-shape issues within the one writable
path. Return only for source contradiction, missing authority, or a required
forbidden action. Missing variance authority is a valid fail-closed decision,
not a reason to ask the operator.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`review`, role=`worker`, lifecyclePhase=`pre-execution`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class review --role worker --lifecycle-phase pre-execution --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | no additional ADIF constraint |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/run_worker_return_fast_gate.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; Source Verification columns; worker-return headings; trace and delta fields |
| gateRunPurpose | confirm final packet shape before dispatch |
| claimBoundary | shape compliance is not variance authority |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R1 literal acceptance remains non-green | REVIEW_SOURCE | `docs/reviews/CVF_EAFR_R1_AIF_REINJECTION_PROVENANCE_FAIL_CLOSED_COMPLETION_2026-08-25.md` | Acceptance Receipt Assertion Matrix | package-wide green | R1 reviewer decision | ACCEPT |
| R1A closes non-live selection only | REVIEW_SOURCE | `docs/reviews/CVF_EAFR_R1A_NON_LIVE_TEST_RUNNER_EXTENSION_COVERAGE_COMPLETION_2026-08-25.md` | Claim Boundary | R1A selection gap | R1A reviewer decision | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| R1 acceptance integrity | Required Analysis | acceptance matrix | source citations | READY |
| R1A bounded closure retained | Dependency Release Evidence | decision claim boundary | reviewer inspection | READY |
| R2 remains held | Decision Outcomes | exact token and next route | reviewer inspection | READY |

## External Knowledge Intake Routing

| Field | Disposition |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | external finding already converted to committed CVF evidence; R1B uses CVF-local authority only |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | EAFR roadmap and R1/R1A reviews |
| Disposition | N/A_WITH_REASON: no new external knowledge intake |
| Claim boundary | only committed CVF-governed sources may support the decision |

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
| --- | --- |
| Coverage index | NOT_APPLICABLE_WITH_REASON: named first-party authority review only; no legacy corpus, repository absorption, scan, or coverage-index claim |
| Claim boundary | no legacy completeness or absorption claim |

## Work-Order Fulfillment Manifest

## Required Artifact Manifest

| Path | Required at return | Purpose |
| --- | --- | --- |
| `docs/reviews/CVF_EAFR_R1B_BASELINE_VARIANCE_AUTHORITY_ADJUDICATION_WORKER_RETURN_2026-08-25.md` | Yes | source-backed decision and evidence |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | no-commit documentation worker plus independent reviewer |
| phase | adjudication pending worker return |
| baseHeadFor(phase) | dispatchBaseHead=02cc34a4f; executionBaseHead=worker captures; closureBaseHead=reviewer captures |
| changedSetScope(phase) | exact one-path worker return |
| traceScope(phase, actor) | read-only evidence and authority search |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | clean worktree required; R2-R6, RFR and all execution/external lanes parked |
| nextMoveSurfaces | worker return then independent reviewer decision |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | reviewer may convert the worker return or create a bounded completion if checker-required |
| reviewerOwnedClosurePaths | worker return, EAFR roadmap and continuity |
| closureOwner | independent orchestrator/reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_EAFR_R1B_BASELINE_VARIANCE_AUTHORITY_ADJUDICATION_WORKER_RETURN_2026-08-25.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | orchestrator/dispatcher |
| Provider or surface | private local repository |
| Session or invocation | EAFR-R1B dispatch, 2026-08-25 |
| Working directory | repository root |
| Command or tool surface | governed reads, scaffold, source verification and gates |
| Target paths | paired R1B baseline/work order and EAFR roadmap |
| Allowed scope source | standing operator dependency-ordered roadmap authority |
| Before status evidence | clean worktree at HEAD `02cc34a4f`; staging empty |
| After status evidence | two new dispatch docs plus roadmap conversion pending commit |
| Diff evidence | exact three-path dispatch-author manifest |
| Approval boundary | documentation-only adjudication dispatch |
| Claim boundary | no acceptance waiver, runtime, provider/live or public effect |
| Agent type | orchestrator/dispatcher |
| Invocation ID | `eafr-r1b-dispatch-2026-08-25` |
| Expected manifest | paired R1B baseline/work order and EAFR roadmap |
| Actual changed set | same three paths |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | documentation-only R1 variance authority adjudication |
| claimDisposition | CLAIM_REJECTED_NO_ACTION: decision remains worker-pending |
| receiptEvidence | N/A with reason: dispatch has no execution receipt |
| actionEvidence | CLAIM_REJECTED_NO_ACTION |
| invocationBoundary | local dispatch authoring only |
| interceptionBoundary | no runtime or agent interception claim |
| claimLanguage | packet ready; no variance authorized yet |
| forbiddenExpansion | tests, build, env, credentials, provider/network/live, source edits, public/deploy/push |

## Evidence Requirements

Return exact authority search, criterion matrix, one decision token, smallest
next route, zero-effect statement, actual one-path status and fast-gate result.

## Verification Commands

```powershell
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git diff --name-status
git status --short --untracked-files=all
git diff --cached --name-only
```

## Review Gate

Worker return is not closure. Reviewer must independently inspect authority and
evidence, preserve fail-closed handling, and own any roadmap/continuity commit.

## Closure Checklist

- [ ] exact one-path worker manifest and empty staging;
- [ ] complete criterion and authority matrices;
- [ ] one allowed decision token;
- [ ] zero forbidden execution or external effect;
- [ ] reviewer-return preflight passes.

## Operator Checkpoint

operator.checkpoint.waiver: standing operator authority covers this read-only
adjudication and independent review. It does not waive acceptance, execution,
external-effect, public, deploy, push, destructive, secret, or commit bounds.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` with the named artifact, or
`BLOCKED_WITH_REASON` for a canonical source contradiction or forbidden need.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance adjudication; no public-sync authority.

## Claim Boundary

This work order authorizes only read-only evidence adjudication and one worker
return. It grants no acceptance waiver, R1 closure, R2 release, execution, or
external effect.
