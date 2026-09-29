# CVF Agent Work Order - LPCI1-REF T1A Public-Safe Branch Deploy Binding Amendment 1

Memory class: governed-worker-dispatch

Status: APPROVED_FOR_EXECUTION

Batch ID: LPCI1-REF-T1A-PUBLIC-SAFE-BRANCH-DEPLOY-BINDING-AMENDMENT-1

Dispatch base head: `5d9a718032ed1ca3bfcae8f0287f549209157cf5`

dispatchBaseHead: `5d9a718032ed1ca3bfcae8f0287f549209157cf5`

executionBaseHead: captured after the Amendment 1 dispatch authority commit.

closureBaseHead: same as executionBaseHead because the worker must not commit.

Commit mode: WORKER_MUST_NOT_COMMIT

Worker return path: `docs/reviews/CVF_LPCI1_REF_T1A_PUBLIC_SAFE_BRANCH_DEPLOY_BINDING_AMENDMENT_1_WORKER_RETURN_2026-08-11.md`

## Dispatch Prompt Envelope

Role: delegated implementation worker repairing the blocked local candidate.

Canonical packet: this Amendment 1 work order, paired source verification and
GC-018 Amendment 1 baseline.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: require the exact clean Core dispatch HEAD supplied by the
orchestrator and public branch HEAD `2103a38f...` before mutation.

Current-time notes: the public branch already contains the exact inherited 23
uncommitted paths; this is authorized predecessor state, not contamination.

Do-not-misread notes: add exactly 18 paths to produce union 41. No commit,
push, deploy, network install, secret, provider/store, browser, or production
authority is granted.

Required first actions: read startup and governed packet surfaces, query ADIF,
verify both bases, refresh exact-23 byte equality, and pass pre-implementation
gate before projecting the amendment.

Return contract: exact 41-path public worktree, Amendment 1 private return,
both staging indexes empty, both HEADs unchanged, and
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Repair the accepted public candidate by adding its exact transitive prerequisite
lineage and rerun all mandatory deterministic evidence.

## Scope / Target / Owner Boundary

The target is the existing local public-sync `lpci1-ref-staging` branch. Worker
owns exact byte projection and verification only. Reviewer owns acceptance and
any commit. External and production state is excluded.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator | delegated orchestrator/reviewer authority and `next` | ACCEPT |
| Amendment source verification | `docs/reviews/CVF_LPCI1_REF_T1A_PUBLIC_SAFE_BRANCH_DEPLOY_BINDING_AMENDMENT_1_SOURCE_VERIFICATION_2026-08-11.md` | ACCEPT |
| Amendment baseline | `docs/baselines/CVF_GC018_LPCI1_REF_T1A_PUBLIC_SAFE_BRANCH_DEPLOY_BINDING_AMENDMENT_1_2026-08-11.md` | ACCEPT |
| Blocker evidence | committed original worker return | ACCEPT |
| Final source bytes | private Core `e82ab11dc0c3b7af46b330c6eedf10049231d7de` | ACCEPT |
| Public target | local `lpci1-ref-staging@2103a38fda01ee827e9fc6c3be38a824fa5d54ad` | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | envelope placement, exact union, inherited state exception, no-commit lifecycle, return sections, trace, public disposition |
| gateRunPurpose | confirm Amendment 1 work-order compliance |
| claimBoundary | machine shape does not prove execution, build, hosted behavior, or export |

## Agent Roles

| Role | Owner | Boundary |
| --- | --- | --- |
| Dispatcher | primary orchestrator | amendment authority |
| Worker | delegated implementation role | exact union-41 preparation and return; no commit |
| Reviewer/closer | primary independent reviewer | semantic/diff/test review and any accepted closure commit |
| Session-sync steward | primary orchestrator | continuity update separate from authority and closure |

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| Intake summary | deterministic review exposed omitted accepted prerequisite lineage |
| risk sensitivity | public candidate mutation with external actions deferred |
| scope classification | exact transitive-lineage byte repair |
| selected role route | MULTI_AGENT_MULTI_ROLE |
| route | MULTI_AGENT_MULTI_ROLE |
| implementation owner | delegated worker |
| review/commit owner | independent reviewer/closer |
| escalation condition | base/hash contradiction, extra required path, network-only dependency, secret, or external action |

## Worker Autonomy / No-Question Rule

Proceed autonomously inside exact scope. Do not repair repository files beyond
the union 41. A local ignored/offline dependency link may be used solely to run
tests, but no registry fetch or repository-path mutation is authorized.

## Required First Reads

- Session front doors and active handoff.
- Guard orientation, literal gotchas, repository boundary, and `DESIGN.md`.
- Original blocked return and all three Amendment 1 authority files.
- Applicable checker sources and accepted source tree.

## Pre-Flight Checks

In Core, require clean exact `executionBaseHead` and run:

```powershell
python governance/compat/run_adif_defect_resolver.py --task-class "LPCI1-REF public-safe prerequisite lineage amendment" --role worker --lifecycle-phase pre-implementation --json
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 5d9a718032ed1ca3bfcae8f0287f549209157cf5 --head HEAD
```

In public-sync, require branch `lpci1-ref-staging`, HEAD `2103a38f...`, exact
23 inherited pending paths, empty staging, and 23/23 equality to `e82ab11dc`.
Do not clean, reset, fetch, or recreate the authorized inherited worktree.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`LPCI1-REF public-safe prerequisite lineage amendment`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Worker must record its own resolver result.

## Execution Instructions

1. Preserve and freshly verify the inherited exact 23 paths.
2. Project exactly the Amendment baseline's 18 paths from `e82ab11dc` while
   preserving bytes, yielding exact union 41.
3. Do not manually edit projected files. The two package files are authorized
   only as exact accepted byte projections.
4. Prove SHA-256 equality for all 41 source/target pairs, exact changed-set
   reconciliation, no secret/private artifact, and empty staging.
5. Run Model Gateway tests and TypeScript; run cvf-web grounding, provider,
   release and route/page suites, TypeScript, scoped ESLint, and production
   build with already-installed offline tooling.
6. Do not fetch dependencies or invoke a download shim. If an ignored local
link is needed and can be created entirely from installed repository-local
content, use it only for verification and record it. Otherwise return a
precise blocker.

## Current Runtime Freshness Verification

Fresh reviewer evidence at Core `4cb250a96` and public target `2103a38f...`
shows Model Gateway TypeScript passes, while cvf-web has two unresolved-import
test suites and seven TypeScript errors caused by the omitted accepted
prerequisite lineage. This current failure evidence is the trigger for the
exact 18-path amendment; no hosted or provider freshness claim is made.
7. Run `git diff --check`, author only the Amendment 1 private return, and run
   worker-return fast gate.

## Write Ownership

- Public: exact 18 amendment paths; inherited 23 may only be preserved and
  verified, not changed to different source bytes.
- Private: exact Amendment 1 worker return path.
- Reviewer: completion review and accepted closure repairs.
- No other path is worker-owned.

## Execution Plan

1. Validate governed inherited state.
2. Add exact prerequisite delta.
3. Verify union hashes, tests, types, lint, build, and negative scope.
4. Return no-commit evidence for independent review.

## Work-Order Fulfillment Manifest

Required public output: exact union of the original baseline's 23 paths and
Amendment 1 baseline's 18 paths, total 41.

Required private output: exact Amendment 1 worker return.

Forbidden paths: every other path. Required proof literals:
`executionBaseHead`, `publicTargetBaseHead`, `sourceMaterialCommit`,
`WORKER_MUST_NOT_COMMIT`, exact 41 reconciliation, zero commit, zero push,
zero deploy, zero provider/store request, and actual Git status.

## Evidence Requirements

Record command, repository, result, exact counts, path/hash ledger, local-only
dependency preparation, and zero-count external-action evidence. Never claim a
deferred mandatory check as passing.

## Acceptance Criteria

| Requirement | Evidence | Failure condition |
| --- | --- | --- |
| Source fidelity | 41 SHA-256 equality rows | mismatch or missing path |
| Public boundary | exact union-41 name-status set; staged zero | extra/missing/staged path |
| Deterministic runtime | Model Gateway and cvf-web lineage/release tests and typechecks | any failure |
| Build integrity | scoped lint and production build | failure, deferral, or network fetch |
| No external effect | operation trace and Git evidence | commit, push, deploy, provider/store request |
| Return integrity | worker-return fast gate | gate failure or false claim |

## Review Gate

Independent reviewer must inspect semantics, 41 hashes, exact manifests,
statuses, tests, lint, build, and local dependency handling before acceptance.

## Closure Checklist

- [ ] Exact 41 public paths and one private Amendment return.
- [ ] Both staging indexes empty; both HEADs unchanged by worker.
- [ ] All mandatory deterministic checks pass without network.
- [ ] No secrets or external action.
- [ ] Independent reviewer disposition remains pending.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only if every worker-owned criterion passes.
Otherwise return `BLOCKED_WITH_REASON` naming the first exact contradiction.

## Operator Checkpoint

No checkpoint for exact local repair. New authority is required for any wider
path, network dependency action, secret, push, deploy, provider/store, or
production operation.

## Agent Handoff Contract Control Block

Canonical source: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | worker-no-commit split |
| phase | EXECUTION |
| baseHeadFor(phase) | executionBaseHead is clean committed Amendment dispatch HEAD; public branch HEAD remains `2103a38f...` with authorized inherited worktree |
| changedSetScope(phase) | exact union 41 public paths plus one Amendment worker return |
| traceScope(phase, actor) | worker trace covers inherited verification, 18-path projection, deterministic checks, and return only |
| commitOwner(phase) | nobody during EXECUTION; reviewer/closer during CLOSURE |
| crossBatchIsolation | inherited exact-23 state is the sole allowed predecessor change; every unrelated change blocks |
| nextMoveSurfaces | session front door, bootstrap, active state, and handoff remain reviewer/session-steward owned |
| Worker terminal status | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_LPCI1_REF_T1A_PUBLIC_SAFE_BRANCH_DEPLOY_BINDING_AMENDMENT_1_COMPLETION_2026-08-11.md`

reviewerOwnedClosurePaths: completion review, accepted exact union-41 public
material, and allowed-scope repair only; session-sync is separate.

Acceptance does not itself authorize push or deployment. Production `main`
remains forbidden.

## External Knowledge Intake Routing

Chain map: `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`.

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: no external epistemic input is admitted |
| Matching local-view guard | N/A with reason: exact local Git and deterministic evidence control |
| Owner surface | Amendment authority and accepted material tree |
| Disposition | N/A with reason: Netlify configuration is not needed for this local repair |
| Claim boundary | no external runtime or deployment inference |

## Worker Return Packet Shape Contract

The return must include: Summary; Purpose; Target / Source; Scope /
Methodology; Authority And Base; Source Verification Refresh; Exact Changed
Manifest; Byte Equality Ledger; Tests And Build Evidence; Negative Scope
Proof; Findings / Position; Risk / Corrective Action; Checker Source Read-Ahead
Block; Agent Operation Trace Block; Delta Execution Claim Boundary Control
Block; External Knowledge Intake Routing; Corpus Completeness And Report
Integrity; Finding-To-Governance Learning Disposition; Epistemic Process Block;
Machine Closure Package; Public Export Disposition; Claim Boundary; Terminal
Disposition; git status --short; Changed Files; Command Evidence; No-Commit
Statement; Worker Experience Retrospective.

## Dual Agent Surface Matrix

| Surface | Disposition | Evidence boundary |
| --- | --- | --- |
| INTERNAL_AGENT | AUTHORIZED | exact local filesystem/Git and deterministic tooling |
| EXTERNAL_AGENT_CLI_MCP | NOT_AUTHORIZED | no external adapter is required |
| Adapter boundary | NONE | local candidate preparation only |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | orchestrator/work-order author |
| Provider or surface | private Core and read-only public-sync inspection |
| Session or invocation | `lpci1-ref-t1a-amendment-1-dispatch-20260811` |
| Working directory | private Core plus public-sync clone |
| Command or tool surface | local reads, Git/hash/import/test evidence, authority authoring, gates |
| Target paths | exact three Amendment authority paths |
| Allowed scope source | delegated operator authority and committed blocker evidence |
| Before status evidence | Core clean worktree at `5d9a71803`; public exact inherited 23-path authorized worktree with staging empty |
| After status evidence | Amendment packet pending commit; public candidate untouched |
| Diff evidence | exact private three-path authority set |
| Approval boundary | dispatch authority only |
| Claim boundary | no worker execution, public commit/push, deploy, provider, hosted smoke, or production action |
| Agent type | orchestrator/dispatcher |
| Invocation ID | `lpci1-ref-t1a-amendment-1-dispatch-20260811` |
| Expected manifest | source verification, baseline, work order |
| Actual changed set | reviewer verifies before dispatch commit |
| Manifest delta | must be zero |
| Deletion or rename disposition | N/A with reason: three new files only |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | local amendment authority and deterministic candidate repair |
| claimDisposition | CLAIM_REJECTED: no hosted, deploy, provider, store, or production behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no hosted receipt exists |
| actionEvidence | ACTION_EVIDENCE_PRESENT: local source/Git/test evidence and authority authoring |
| invocationBoundary | zero public mutation, commit, push, deploy, provider/store, browser, or production invocation |
| interceptionBoundary | local repositories only |
| claimLanguage | approved for exact no-commit union-41 repair |
| forbiddenExpansion | network fetch, public push, Netlify action, secrets, provider/store, production, and `main` |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: local repair and independent review must complete before any export.

## Claim Boundary

This work order can establish a locally verified exact 41-path candidate. It
cannot establish or authorize public export, Netlify deployment, hosted
availability, provider/store behavior, credentials, or production readiness.
