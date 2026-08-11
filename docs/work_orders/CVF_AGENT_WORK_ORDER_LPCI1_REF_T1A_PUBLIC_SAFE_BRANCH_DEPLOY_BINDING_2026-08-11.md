# CVF Agent Work Order - LPCI1-REF T1A Public-Safe Branch Deploy Binding

Memory class: governed-worker-dispatch

Status: APPROVED_FOR_EXECUTION

Batch ID: LPCI1-REF-T1A-PUBLIC-SAFE-BRANCH-DEPLOY-BINDING

Dispatch base head: `a2687471b8869dc6391273aa442b012fd287970b`

dispatchBaseHead: `a2687471b8869dc6391273aa442b012fd287970b`

executionBaseHead: captured after the dispatch authority commit.

closureBaseHead: same as executionBaseHead because the worker must not commit.

Commit mode: WORKER_MUST_NOT_COMMIT

Worker return path: `docs/reviews/CVF_LPCI1_REF_T1A_PUBLIC_SAFE_BRANCH_DEPLOY_BINDING_WORKER_RETURN_2026-08-11.md`

## Dispatch Prompt Envelope

Role: delegated implementation worker preparing a public-safe staging diff.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI1_REF_T1A_PUBLIC_SAFE_BRANCH_DEPLOY_BINDING_2026-08-11.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture clean Core dispatch HEAD and exact public target
base before any mutation.

Current-time notes: operator saved Netlify branch deploy context
`lpci1-ref-staging` on 2026-08-11.

Do-not-misread notes: this is local staging preparation only. It grants no
commit, push, deploy, browser, hosted smoke, provider, secret, or production
authority.

Required first actions: read startup front doors, active handoff, guard
orientation, literal gotchas, source verification, baseline, this packet,
repository boundary, `DESIGN.md`, and applicable checker sources; query ADIF;
verify both repositories and run the pre-implementation gate before editing.

Return contract: exact 23 public files plus one private return, empty staging,
unchanged HEADs, and `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Create a local public-sync branch from the pinned public base, project exactly
the accepted public-safe LPCI1 implementation bytes, and prove the resulting
tree with deterministic tests and build without external effects.

## Scope / Target / Owner Boundary

The target is one local branch in the public-sync clone and the exact 23 public
paths named by the baseline. The worker owns preparation only; the reviewer
owns acceptance and commit. Every external action and production surface is
outside this work order.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator | `ok, tien hanh di` after staging-only proposal | ACCEPT |
| Source verification | `docs/reviews/CVF_LPCI1_REF_T1A_PUBLIC_SAFE_BRANCH_DEPLOY_BINDING_SOURCE_VERIFICATION_2026-08-11.md` | ACCEPT |
| GC-018 baseline | `docs/baselines/CVF_GC018_LPCI1_REF_T1A_PUBLIC_SAFE_BRANCH_DEPLOY_BINDING_2026-08-11.md` | ACCEPT |
| Accepted material | private Core commit `e82ab11dc` | ACCEPT |
| Public target | public-sync `main@2103a38fda01ee827e9fc6c3be38a824fa5d54ad` | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | envelope placement, source verification, no-commit lifecycle, return sections, trace fields, public disposition |
| gateRunPurpose | confirm work-order compliance after authoring |
| claimBoundary | machine shape does not prove worker execution or hosted behavior |

## Agent Roles

| Role | Owner | Boundary |
| --- | --- | --- |
| Dispatcher | primary orchestrator | source verification, baseline, committed packet |
| Worker | delegated implementation role | exact public projection and private return; no commit |
| Reviewer/closer | primary independent reviewer | semantic/diff/test review, commit and optional branch push only after acceptance |
| Session-sync steward | primary orchestrator | separate continuity update after closure |

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| Intake summary | operator authorized the proposed staging-only next tranche after Netlify branch context was saved |
| risk sensitivity | public repository mutation with external deployment deliberately deferred |
| scope classification | exact-manifest public-safe byte projection and deterministic validation |
| selected role route | MULTI_AGENT_MULTI_ROLE |
| route | MULTI_AGENT_MULTI_ROLE |
| implementation owner | delegated worker |
| review/commit owner | independent reviewer/closer |
| escalation condition | base/hash contradiction, secret exposure, extra required path, external action, or repeated governed blocker |

## Worker Autonomy / No-Question Rule

Proceed autonomously inside the exact scope. Repair only failures that require
changes within the exact 23 public paths or the private return. Stop for any
extra path, dependency mutation, secret-bearing input, branch/base conflict,
external request, or change to the claim boundary.

## Required First Reads

- `CVF_SESSION_MEMORY.md`, bootstrap read model, and active handoff.
- `docs/reference/guard_orientation/README.md` and literal gotchas.
- `docs/reference/CVF_AGENTS_CRITICAL_REPOSITORY_BOUNDARY_2026-06-23.md`.
- Source verification, GC-018 baseline, and this work order.
- `DESIGN.md` for Web/UI claim discipline.
- Accepted completion and exact source files named by the baseline.

## Pre-Flight Checks

In private Core, capture HEAD/status, query ADIF, and run:

```powershell
python governance/compat/run_adif_defect_resolver.py --task-class "LPCI1-REF public-safe branch deploy binding" --role worker --lifecycle-phase pre-implementation --json
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base a2687471b8869dc6391273aa442b012fd287970b --head HEAD
```

In public-sync, require clean `main`, exact HEAD
`2103a38fda01ee827e9fc6c3be38a824fa5d54ad`, and exact public remote. If local
branch `lpci1-ref-staging` exists, require it to point exactly at the target
base and have a clean tree; otherwise create it from that base. Do not fetch.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`LPCI1-REF public-safe branch deploy binding`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

The worker must record its own resolver output rather than inheriting this
dispatcher result.

## Execution Instructions

1. Use private Core commit `e82ab11dc` as the only content source.
2. Project exactly the 23 paths listed in the baseline into the public-sync
   branch. Preserve exact bytes; do not redesign or manually normalize them.
3. Do not project the private operations runbook or any private governance
   artifact.
4. Verify SHA-256 equality for every source/target pair.
5. Run the focused Model Gateway suite and TypeScript check.
6. Run exact cvf-web LPCI1/release suites, TypeScript, scoped local ESLint, and
   production build using installed dependencies only. Do not invoke a shim
   that downloads tooling.
7. Run `git diff --check`, reconcile the exact public manifest, and keep the
   public staging index empty.
8. Create only the private Core worker return. Run worker-return fast gate.

## Write Ownership

- Worker-owned public paths: exact 23-path baseline manifest.
- Worker-owned private path: exact worker return.
- Reviewer-owned paths: completion review and accepted closure repairs only.
- No other path has write ownership in this tranche.

## Execution Plan

1. Verify both bases and gates.
2. Create or select the exact clean local staging branch.
3. Project exact accepted bytes.
4. Run hash, test, type, lint, build, and negative-scope checks.
5. Produce the no-commit return and stop for independent review.

## Work-Order Fulfillment Manifest

Required public outputs: exactly the 23 paths under `## Exact Public-Safe
Projection Manifest` in the GC-018 baseline.

Required private output: exactly the worker return path named above.

Forbidden paths: every other public-sync path; all Core paths except the
worker return; all secrets/private environment files; all session surfaces;
all package manifests and lockfiles.

Required proof literals: `executionBaseHead`, `publicTargetBaseHead`,
`sourceMaterialCommit`, `COMPLETE_PENDING_REVIEW`, `WORKER_MUST_NOT_COMMIT`,
exact manifest reconciliation, zero commit, zero push, zero deploy, zero
provider request, zero hosted-store request, and actual Git status.

## Evidence Requirements

Record command, result, repository, path/range, and zero-count evidence for
every required verification and forbidden external action.

## Acceptance Criteria

| Requirement | Evidence | Failure condition |
| --- | --- | --- |
| Source fidelity | 23 SHA-256 source/target equality rows | any mismatch |
| Public boundary | exact name-status set | extra or missing public path |
| Deterministic runtime | focused suites and typechecks | any failure |
| Build integrity | scoped lint and production build | any failure or tool download |
| No external effect | operation trace and Git/command evidence | commit, push, deploy, provider/store request |
| Return integrity | worker-return fast gate | gate failure or false clean claim |

## Review Gate

Independent reviewer acceptance is mandatory. The reviewer checks byte
fidelity, public safety, exact manifests, actual statuses, and proportionate
test/build reruns before committing anything.

## Closure Checklist

- [ ] Exact 23 public paths and one private return.
- [ ] Both staging indexes empty and both HEADs unchanged by worker.
- [ ] All required deterministic verification passes.
- [ ] No secret read or external action.
- [ ] Independent reviewer disposition recorded.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when every checklist item owned by the
worker passes. Otherwise return `BLOCKED_WITH_REASON` with the exact first
blocking contradiction or forbidden-scope requirement.

## Operator Checkpoint

No operator checkpoint is required for allowed local remediation. A new
operator decision is required only to widen paths, use secrets, push, deploy,
run hosted/provider proof, or change production.

## Agent Handoff Contract Control Block

Canonical source: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | worker-no-commit split |
| phase | EXECUTION |
| baseHeadFor(phase) | executionBaseHead equals the clean committed dispatch HEAD; public target base remains `2103a38fda01ee827e9fc6c3be38a824fa5d54ad` |
| changedSetScope(phase) | exact 23 public paths plus one private worker return |
| traceScope(phase, actor) | worker execution trace covers only the exact pending worker set |
| commitOwner(phase) | nobody during EXECUTION; independent reviewer/closer during CLOSURE |
| crossBatchIsolation | both repositories must start clean; no inherited or unrelated change is allowed |
| nextMoveSurfaces | session front door, bootstrap, active state, and active handoff remain reviewer/session-steward owned |
| Worker terminal status | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_LPCI1_REF_T1A_PUBLIC_SAFE_BRANCH_DEPLOY_BINDING_COMPLETION_2026-08-11.md`

reviewerOwnedClosurePaths: completion review, accepted public exact-23 material,
and allowed-scope repair only; session-sync remains separate.

The reviewer may accept only after fresh semantic inspection and rerunning
proportionate deterministic evidence. On acceptance, the reviewer may commit
the public staging branch and then run the public-sync pre-push gates. Push is
a reviewer-owned later action; Netlify branch deployment and hosted smoke must
be evidenced separately. Production `main` remains forbidden.

## External Knowledge Intake Routing

Chain map: `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`.

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | NOT_APPLICABLE_WITH_REASON |
| Matching local-view guard | N/A with reason: operator-owned deployment configuration fact; no external epistemic packet is admitted |
| Owner surface | local governed source verification plus operator-owned external configuration state |
| Disposition | N/A with reason: the screenshot is operational context, not external epistemic authority or corpus input |
| Claim boundary | accepts only the named branch-context fact; no deploy success or hosted behavior inference |

## Worker Return Packet Shape Contract

The return must include: Summary; Purpose; Target / Source; Scope /
Methodology; Authority And Base; Source Verification Refresh; Exact Changed
Manifest; Byte Equality Ledger; Tests And Build Evidence; Negative Scope
Proof; Findings / Position; Risk / Corrective Action; Checker Source Read-Ahead
Block; Agent Operation Trace Block; Delta Execution Claim Boundary Control
Block; External Knowledge Intake Routing; Corpus Completeness And Report
Integrity; Finding-To-Governance Learning Disposition; Epistemic Process Block;
Machine Closure Package; Public Export Disposition; Claim Boundary; Terminal
Disposition.

## Dual Agent Surface Matrix

| Surface | Disposition | Evidence boundary |
| --- | --- | --- |
| INTERNAL_AGENT | AUTHORIZED | exact local filesystem/Git projection and deterministic commands |
| EXTERNAL_AGENT_CLI_MCP | NOT_AUTHORIZED | no CLI/MCP adapter or external execution path is needed |
| Adapter boundary | NONE | file projection only; no agent-runtime adapter claim |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | orchestrator/work-order author |
| Provider or surface | private Core and read-only public-sync inspection |
| Session or invocation | `lpci1-ref-t1a-public-safe-branch-deploy-binding-dispatch-20260811` |
| Working directory | private Core root plus read-only public-sync clone |
| Command or tool surface | local reads, hashes, Git inspection, governed packet authoring, gates |
| Target paths | exact three private dispatch artifacts |
| Allowed scope source | operator staging-only continuation authority |
| Before status evidence | clean worktree in Core at `a2687471b`; clean worktree in public-sync at `main@2103a38f` |
| After status evidence | dispatch packet pending commit; no public mutation or external action |
| Diff evidence | exact private three-path status and pre-dispatch range |
| Approval boundary | dispatch authority only |
| Claim boundary | no worker execution, public commit/push, deploy, provider, hosted smoke, or production action |
| Agent type | orchestrator/dispatcher |
| Invocation ID | `lpci1-ref-t1a-public-safe-branch-deploy-binding-dispatch-20260811` |
| Expected manifest | source verification, baseline, work order |
| Actual changed set | reviewer verifies before dispatch commit |
| Manifest delta | must be zero before dispatch commit |
| Deletion or rename disposition | N/A with reason: three new files only |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | local dispatch authority and future deterministic staging preparation |
| claimDisposition | CLAIM_REJECTED: no hosted, deployment, provider, or production behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no hosted receipt exists in this tranche |
| actionEvidence | ACTION_EVIDENCE_PRESENT: local source/hash/Git inspection and authored packet |
| invocationBoundary | zero public mutation, commit, push, deploy, provider, store, browser, or production invocation |
| interceptionBoundary | repository-local file and deterministic command boundary only |
| claimLanguage | approved for no-commit local staging preparation |
| forbiddenExpansion | public push, Netlify deploy, live proof, secrets, provider/store, production, and `main` |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this packet authorizes local public-safe preparation only. Export is
deferred until independent review, reviewer-owned commit, pre-push gates, and
an explicit push action.

## Claim Boundary

The work order can establish a locally tested public-sync candidate. It cannot
establish hosted availability, provider/store liveness, credential validity,
Netlify success, public release readiness, or production readiness.
