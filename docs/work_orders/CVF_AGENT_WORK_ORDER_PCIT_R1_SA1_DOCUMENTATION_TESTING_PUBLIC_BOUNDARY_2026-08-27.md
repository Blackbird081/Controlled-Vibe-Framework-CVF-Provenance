# CVF Agent Work Order - PCIT-R1-SA1 Documentation Testing Public Boundary

Memory class: governed-worker-dispatch

Status: APPROVED_FOR_EXECUTION

Batch ID: PCIT-R1-SA1

Dispatch base head: `2c9f7d3b2`

Commit mode: WORKER_MUST_NOT_COMMIT

providerExecutionAuthority: FORBIDDEN

Worker return path: `docs/reviews/CVF_PCIT_R1_SA1_DOCUMENTATION_TESTING_PUBLIC_BOUNDARY_WORKER_RETURN_2026-08-27.md`

## Dispatch Prompt Envelope

Role: one no-commit public workflow reconciliation worker.

Canonical packet: parent PCIT-R1 roadmap/baseline/work order, reviewer blocker
`92ae3460a`, paired PCIT-R1-SA1 baseline and this work order.

executionBaseHead: capture private and public exact HEADs before edits.

Do-not-misread: same-roadmap scope amendment, not R2, dependency repair,
product work, public commit, push, merge, deploy or hosted rerun authority.

Required first actions: read startup front doors, guard orientation, literal
gotchas, canonical packet, PR run `33036642522`, this workflow and active
public owner workflows; prove both staging areas empty.

Return contract: author only the named return plus the one public workflow
candidate and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Produce one truthful automatic public workflow by reconciling the bounded job
inventory in `documentation-testing.yml`, preserving useful public coverage and
removing false-green orchestration.

## Authority Chain

- Operator scope-amendment approval, 2026-08-27.
- Parent PCIT-R1 roadmap, baseline and work order.
- Reviewer blocker commit `92ae3460a` and continuity checkpoint `2c9f7d3b2`.
- Paired PCIT-R1-SA1 GC-018 baseline and this work order.

## Agent Roles

- Dispatcher: orchestrator/reviewer; amendment authority only.
- Worker: one no-commit workflow worker.
- Reviewer/closer: independent acceptance, PR update and hosted evaluation.
- Operator: any second owner, product/dependency change or successor.

## Required First Reads

Read the startup bootstrap/front door/handoff, guard orientation, literal
gotchas, parent and amendment authority, reviewer evidence, the changed
workflow, active public workflows, run `33036642522`, and checker sources named
below.

## Pre-Flight Checks

Require private HEAD descended from the committed amendment authority, public
branch `pcit-r1-public-ci-truthfulness` at `910665e62`, expected public remote,
clean private/public worktrees and empty staging areas before edits.

## Scope / Target / Owner Boundary

Allowed public-sync write: `.github/workflows/documentation-testing.yml`.

Allowed private write: the named PCIT-R1-SA1 worker return only.

The five files in public commit `910665e62` are read-only. No other file may
change, including generated output.

## Write Ownership

Write exactly the one public workflow and one named private return. Read-only
inspection does not expand ownership.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| PCIT-R1 review blocker | `docs/reviews/CVF_PCIT_R1_PUBLIC_CI_TRUTHFULNESS_AND_CORPUS_BOUNDARY_RECONCILIATION_WORKER_RETURN_2026-08-27.md`; commit `92ae3460a` | operator approves exact owner amendment | RELEASED_BY_OPERATOR |
| current public candidate | branch `pcit-r1-public-ci-truthfulness`; commit `910665e62`; PR `#4` | remain read-only | RELEASED_READ_ONLY |

## Work Plan

1. Capture dual-repository HEAD, branch, status, staging and remotes.
2. Build a bounded job/coverage matrix for `documentation-testing.yml` using
   hosted logs and current public corpus.
3. Keep automatic jobs only when their inputs exist publicly and their result
   has unique or named public-safe value.
4. Retire private-only or stale jobs only after mapping useful coverage to an
   active public owner.
5. Make the summary fail closed over retained dependencies or remove it; an
   echo-only success over failures is forbidden.
6. Validate YAML, triggers, dependencies, retained local commands and public
   preflight, then return without commit or external write.

## Execution Plan

Execute the Work Plan once as one consolidated owner repair. Do not split job
families into child tranches or change prior candidate paths.

## Evidence Requirements

Record exact dual HEAD/status/staging/remotes, hosted run/job IDs, bounded job
classifications, coverage owners, workflow before/after topology, YAML result,
retained-command results, public preflight, changed manifest and zero external
effect statement.

## Failure Classification Contract

Use exactly one of `PUBLIC_PRIVATE_CORPUS_MISMATCH`,
`WORKFLOW_BOOTSTRAP_DRIFT`, `DUPLICATE_OR_STALE_WORKFLOW`,
`GENUINE_PRODUCT_DEFECT`, or `NOT_REPRODUCED_WITH_EVIDENCE` per bounded job or
job family. A genuine product defect remains blocking and unchanged.

## Required Artifact Manifest

| Path | Required state |
| --- | --- |
| public `.github/workflows/documentation-testing.yml` | minimal truthful topology with no private-corpus job and no false-green summary |
| private named worker return | classifications, coverage owners, diff and proof |

No additional artifact is authorized.

## Acceptance Criteria

- Automatic jobs reference public-present inputs only.
- Unique useful public checks remain blocking under a named active owner.
- Duplicated/private-only checks are retired with coverage evidence.
- No summary can succeed merely by printing failed dependency results.
- No `continue-on-error`, manual-only conversion or threshold weakening is
  introduced to hide a failure.
- Exact two-path worker manifest, unchanged HEADs and empty staging areas.

## Verification Commands

```powershell
git status --short
git -C "D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync" status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 2c9f7d3b2 --head HEAD
python scripts/check_cvf_public_sync_candidate.py --public-root "D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync" --authorized-paths-json <exact-authorized-path-file> --expected-remote https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git --baseline-ref origin/main --json
python governance/compat/run_worker_return_fast_gate.py
```

Parse the changed workflow as YAML. Execute locally only the retained commands
whose inputs exist publicly. Do not trigger hosted reruns or pushes.

## Stop Conditions

Return blocked on a second public owner need, product source, package/lockfile,
dependency, secret/provider, Netlify, branch-policy, commit/push/merge/deploy,
private export, genuine product repair or successor need.

## Review Gate

Reviewer rechecks job classifications, coverage ownership, YAML, fail-closed
summary semantics, exact manifest and local gates before any branch commit.
After push, merge remains blocked until relevant exact-SHA public workflows are
green and no new owner gap appears.

## Closure Checklist

One workflow; one return; public inputs only; coverage retained; no false-green
summary; no suppression; no forbidden surface; staging empty; independent
review and exact-SHA hosted proof.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when the checklist passes locally.
Otherwise return `BLOCKED_WITH_REASON` at the first named stop condition.

## Operator Checkpoint

No checkpoint inside exact ownership. Stop for a second owner, product or
dependency mutation, secret/provider need, branch-policy change or successor.

## Worker Autonomy / No-Question Rule

Proceed without questions inside exact ownership. Address packet-format failures
by reading checker source. Stop only on a named stop condition.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| private-corpus guards fail publicly | boundary mismatch | `.github/workflows/documentation-testing.yml` | failed job logs from run `33036642522` | jobs | GitHub Actions | ACCEPT |
| Python install target lacks package metadata | bootstrap drift | `.github/workflows/documentation-testing.yml` | `test` install step | test | GitHub Actions | ACCEPT |
| status summary is false-green | orchestration defect | `.github/workflows/documentation-testing.yml` | `status-check` | status-check | GitHub Actions | ACCEPT |

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "PCIT-R1-SA1",
  "requestedProfile": "P4_CRITICAL",
  "classification": {
    "taskKind": "PUBLIC_RELEASE",
    "authorityImpact": "USES_EXISTING_OWNER",
    "externalEffect": "LOCAL_REVERSIBLE",
    "dataSensitivity": "PUBLIC",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "NAMED_FILES",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "OWNER_COMPOSITION"
  },
  "pathFamilies": [".github/workflows/documentation-testing.yml", "docs/baselines", "docs/work_orders", "docs/reviews"],
  "claims": ["one public workflow candidate removes private-corpus execution and false-green summary behavior"],
  "requiredProof": ["bounded job matrix", "coverage-owner mapping", "YAML validation", "public-sync preflight", "independent review"],
  "operatorCheckpoints": ["second owner", "genuine product defect", "public write"],
  "forbiddenEffects": ["worker commit", "worker push", "merge", "deploy", "secret read", "provider call", "product or dependency edit"],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": null,
    "completenessClaimChanged": false
  }
}
```

## Coverage Matrix Requirement

For the bounded workflow job list, record classification, public input
availability, unique value, retained owner, disposition and proof. Group jobs
only when they share the same command, missing corpus class and owner.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | one no-commit worker, then independent reviewer/closer |
| phase | implementation |
| baseHeadFor(phase) | dispatchBaseHead=`2c9f7d3b2`; executionBaseHead=worker capture; closureBaseHead=reviewer capture |
| changedSetScope(phase) | one public workflow plus one private return |
| traceScope(phase, actor) | dual-repo state, job matrix, workflow diff and local gates |
| commitOwner(phase) | reviewer only |
| crossBatchIsolation | clean worktree before edits; no R2, product, dependency or other owner |
| Before status evidence | private and public worktrees clean; both staging areas empty before worker edits |
| nextMoveSurfaces | named return then independent review of PR update |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | optional; prefer reviewer addendum in amendment worker return |
| reviewerOwnedClosurePaths | amendment return; existing PR branch; roadmap/continuity only after acceptance |
| closureOwner | independent orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_PCIT_R1_SA1_DOCUMENTATION_TESTING_PUBLIC_BOUNDARY_WORKER_RETURN_2026-08-27.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

executionBaseHead: worker must record both repositories at start.

requiredTerms: Purpose | Scope / Methodology | Findings / Position | Risk / Corrective Action | Checker Source Read-Ahead Block | Agent Operation Trace Block | Delta Execution Claim Boundary Control Block | Public Export Disposition | Claim Boundary | executionBaseHead | git status --short

conditionalTerms: External Knowledge Intake Routing | Rescan Intelligence
Hardening | Corpus Completeness And Report Integrity | Finding-To-Governance
Learning Disposition | Epistemic Process Block | Machine Closure Package | N/A
with reason

Required sections: Purpose; Scope / Methodology; Findings / Position; Risk /
Corrective Action; Checker Source Read-Ahead Block; Agent Operation Trace
Block; Delta Execution Claim Boundary Control Block; Public Export
Disposition; Claim Boundary; git status --short; Changed Files; Command
Evidence; No-Commit Statement.

Conditional sections must contain evidence or `N/A with reason`: External
Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus Completeness
And Report Integrity; Finding-To-Governance Learning Disposition; Epistemic
Process Block; Machine Closure Package.

## Foundation Storage Layout Block

N/A with reason: this amendment creates no durable foundation, index, locator,
registry or generated aggregate; it changes one existing public workflow.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | NOT_TRIGGERED with reason: receipts are current execution evidence, not an external corpus |
| Matching local-view guard | `governance/compat/check_public_export_disposition.py` |
| Owner surface | `.github/workflows/documentation-testing.yml` |
| Disposition | RECONCILED_DESIGN_INPUT_ONLY |
| Claim boundary | no outside repository, recommendation or knowledge package is promoted into CVF authority |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| amended workflow | create the one-file local candidate |
| named amendment return | create full-gate evidence packet |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Public sync`, role=`dispatcher`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_authoring.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_dispatch_scaffold_provenance.py` |
| literalTokensReviewed | dispatch envelope, required manifest, handoff fields, return shape and public disposition |
| gateRunPurpose | confirm amendment authority before worker execution |
| claimBoundary | conformance does not prove workflow or hosted success |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind public-sync --batch-id PCIT-R1-SA1 --title "Documentation Testing Public Boundary Scope Amendment" --date 2026-08-27 --base 2c9f7d3b2 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | public-sync plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with exact parent evidence, ownership, work plan and proof |
| checkerReadAheadConfirmation | sources listed in Checker Source Read-Ahead Block |
| docOnlyNewFields | bounded job/coverage matrix requirement |
| claimBoundary | dispatch authoring only |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher/reviewer |
| Provider or surface | private provenance plus public-sync/GitHub read evidence |
| Session or invocation | PCIT-R1-SA1 dispatch, 2026-08-27 |
| Working directory | private root; public sibling read-only |
| Command or tool surface | Git reads, workflow/log reads, patches and gates |
| Target paths | paired amendment baseline/work order |
| Allowed scope source | user authorization after reviewer blocker |
| Before status evidence | clean worktree in both repositories at private HEAD `2c9f7d3b2` and public candidate `910665e62`; both staging areas empty |
| After status evidence | paired authority pending dispatch commit only |
| Diff evidence | `git diff --name-status` |
| Approval boundary | dispatch only; no public implementation write |
| Claim boundary | one-owner amendment authority only |
| Agent type | dispatcher |
| Invocation ID | `pcit-r1-sa1-dispatch-2026-08-27` |
| Expected manifest | paired baseline and work order |
| Actual changed set | must match expected manifest before commit |
| Manifest delta | must be NONE |
| Deletion or rename disposition | N/A with reason: authority artifacts only |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | no-commit one-workflow public candidate |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: run `33036642522` and local Git evidence |
| actionEvidence | ACTION_EVIDENCE_PRESENT: later local workflow diff only |
| invocationBoundary | hosted read plus local reversible worker edit |
| interceptionBoundary | no runtime/provider/secret interception |
| claimLanguage | candidate pending independent review |
| forbiddenExpansion | other owners, product, dependency, secret, provider, deploy, R2 |

## Public/Provenance Boundary

Worker operates on the sibling public-sync clone locally. Reviewer alone may
commit/push the branch and evaluate a new exact SHA. Public `main` and branch
protection must not be bypassed.

## Public Export Disposition

BLOCKED_MISSING_PUBLIC_ARTIFACTS

Reason: amendment candidate and accepted hosted result do not yet exist; PR
`#4` remains unmerged.

## Claim Boundary

This work order authorizes one no-commit worker to modify one public workflow
and create one private return. It grants no other repository or external
effect and does not claim public CI is green.
