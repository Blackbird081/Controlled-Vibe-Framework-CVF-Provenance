# CVF Agent Work Order - PCIT-R1 Public CI Truthfulness And Corpus Boundary Reconciliation

Memory class: governed-worker-dispatch

Status: APPROVED_FOR_EXECUTION

providerExecutionAuthority: FORBIDDEN

Batch ID: PCIT-R1

Dispatch base head: `eb60e89d3e53c8ae11bab36d1767ff43ff81430d`

Commit mode: WORKER_MUST_NOT_COMMIT

Worker return path: `docs/reviews/CVF_PCIT_R1_PUBLIC_CI_TRUTHFULNESS_AND_CORPUS_BOUNDARY_RECONCILIATION_WORKER_RETURN_2026-08-27.md`

## Dispatch Prompt Envelope

Role: no-commit public CI reconciliation worker.

Canonical packet: this work order plus the paired PCIT-R1 GC-018 baseline.

executionBaseHead: capture private and public exact HEADs before edits.

Do-not-misread: this is not dependency modernization, product repair, private
corpus export, CI weakening, commit, push, deploy or provider/live authority.

Required first actions: read startup front doors, guard orientation, literal
gotchas, roadmap, baseline, this work order, the six public files in scope and
checker sources named below; then verify both repositories are clean.

Return contract: one worker return with `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`; both HEADs unchanged and both staging areas empty.

## Purpose

Classify every current red always-on public CI job, repair only public/private
corpus mismatch or workflow/runner bootstrap drift inside the exact allowlist,
and produce an independently reviewable public candidate.

## Authority Chain

- Operator instruction: select and proceed to the next high-value roadmap,
  2026-08-27.
- Active bootstrap: `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`.
- Roadmap: `docs/roadmaps/CVF_PUBLIC_CI_TRUTHFULNESS_AND_CORPUS_BOUNDARY_RECONCILIATION_ROADMAP_2026-08-27.md`.
- GC-018: `docs/baselines/CVF_GC018_PCIT_R1_PUBLIC_CI_TRUTHFULNESS_AND_CORPUS_BOUNDARY_RECONCILIATION_2026-08-27.md`.
- Active handoff: `AGENT_HANDOFF_V59_2026-08-11.md`.

## Agent Roles

- Dispatcher: orchestrator acting under the operator instruction.
- Worker: one no-commit implementation role.
- Reviewer/closer: independent orchestrator/reviewer after return.
- Operator checkpoint: any scope expansion, public write, secret/provider need,
  genuine product defect repair or successor.

## Required First Reads

- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V59_2026-08-11.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- the roadmap, baseline and this work order
- every allowed public workflow/runner path that exists
- checker sources named in the read-ahead block

## Pre-Flight Checks

Before editing, prove both worktrees clean, both staging areas empty, exact
HEADs captured, and public `origin` equals the expected repository. Run the
pre-implementation autorun gate from the private root. Stop on any mismatch.

## Scope / Target / Owner Boundary

Allowed public-sync writes:

- `.github/workflows/ci.yml`
- `.github/workflows/cvf-ci.yml`
- `.github/workflows/cvf-static-ci.yml`
- `.github/workflows/cvf-web-ci.yml`
- `scripts/run_cvf_static_ci_gate.py`
- `scripts/test_run_cvf_static_ci_gate.py` only if the runner changes

Allowed private write:

- the named worker return only

Read-only access is allowed for GitHub Actions metadata/logs, package manifests,
workflow files and source needed to classify failures. Network write is
forbidden.

## Write Ownership

Write ownership is exactly the six public-sync paths and one private worker
return listed in Scope. All other paths are forbidden even if a test or gate
names them.

## Work Plan

1. Capture private/public HEAD, branch, status, staging and remotes.
2. Inventory always-on public workflows and exact-SHA runs.
3. Reproduce or inspect every red job and assign one roadmap classification.
4. Create a coverage matrix proving every removed/retired automatic check has
   an active public-safe owner, or keep it active.
5. Apply the smallest allowlisted workflow/runner correction.
6. Run focused runner tests, YAML/workflow checks, applicable package commands
   and public-sync preflight.
7. Return exact evidence without commit, push or deploy.

## Execution Plan

Execute the Work Plan once, in order. Consolidate all workflow/runner repairs
sharing the verified root cause into this return. Do not split them into child
tranches.

## Failure Classification Contract

Use exactly one of `PUBLIC_PRIVATE_CORPUS_MISMATCH`,
`WORKFLOW_BOOTSTRAP_DRIFT`, `DUPLICATE_OR_STALE_WORKFLOW`,
`GENUINE_PRODUCT_DEFECT`, or `NOT_REPRODUCED_WITH_EVIDENCE` for each red job.
Never convert `GENUINE_PRODUCT_DEFECT` into skip, manual-only or
continue-on-error status.

## Acceptance Criteria

- private-only governance is absent from always-on public execution;
- useful CI coverage is retained under a named active owner;
- workflow bootstrap aligns with package dependencies without package edits;
- local focused proof and public-sync preflight pass;
- any genuine product defect is returned blocking and unchanged;
- exact changed set remains inside ownership;
- no secrets, provider calls or public writes occur.

## Evidence Requirements

Record command, exit/result, working directory, exact SHA, job/run ID where
applicable, classification, coverage owner, changed path and boundary. Do not
record secret values or unredacted credentials.

## Worker Autonomy / No-Question Rule

Proceed without questions for read-only diagnosis, allowlisted edits, local
tests and allowed-scope gate remediation. Stop only when a named stop condition
requires scope expansion or external effect.

## Stop Conditions

Return `BLOCKED_WITH_REASON` on dirty initial state, remote mismatch, product or
runtime source need, package/lockfile/dependency change, threshold weakening,
genuine failure suppression, private artifact export, secret need,
provider/live call, commit/push/deploy need, or out-of-scope path.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| private hook is wired into public generic CI | workflow behavior | `.github/workflows/ci.yml` | Web UI Tests | `Governance Hook Chain` | GitHub Actions | ACCEPT |
| public preflight is an independent green owner | workflow behavior | `.github/workflows/public-sync-preflight.yml` | public-sync-preflight | `check_cvf_public_sync_candidate.py` | GitHub Actions | ACCEPT |
| static runner includes private continuity gate | source behavior | `scripts/run_cvf_static_ci_gate.py` | `run_checks` | `check_continuation_chain` | Python runner | ACCEPT |
| exact published SHA is recorded by terminal closure | governed receipt | `docs/reviews/CVF_LPCI1_WEB_R3_FINAL_AUTH_BUILD_PUBLIC_RELEASE_COMPLETION_2026-08-27.md` | Verification And Evidence | `a0ef5923d100b02c43294815ac9d01d8db20e8b8` | terminal LPCI1 Web R3 review | ACCEPT |

## Current Runtime Freshness Verification

Fresh GitHub metadata was read on 2026-08-27 for exact public SHA
`a0ef5923d100b02c43294815ac9d01d8db20e8b8`. The worker must refresh the run
inventory at execution start and record any newer exact evidence. No claim is
made that all red jobs share one cause.

## Negative Search And Collision Discipline

Artifact path and token searches found no prior PCIT-R1 authority. WSR1 is not
the owner because it governs workspace-kit publication rather than current
always-on GitHub Actions truthfulness.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output evidence | Verification | Status |
| --- | --- | --- | --- | --- |
| classify each red job | Failure Classification Contract | worker classification matrix | exact run/job evidence | READY |
| retain public-safe coverage | Work Plan | coverage owner matrix | workflow diff review | READY |
| workflow/runner-only repair | Scope | exact changed manifest | `git diff --name-status` | READY |
| no hidden product defect | Stop Conditions | blocking finding if observed | reviewer semantic audit | READY |
| no public worker effects | Public boundary | dual-repo HEAD/status | Git reads | READY |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| named private worker return | create with full-gate packet shape and exact evidence |
| allowed public workflow/runner files | edit only those necessary; list unchanged allowed paths as not touched |

## Required Proof Manifest Atomic Literal Discipline

Required proof is one atomic set: refreshed run inventory, job classification,
coverage matrix, exact diff, focused tests, workflow/YAML validation,
public-sync preflight, dual-repository status/staging, and zero external-effect
statement. Partial proof is not completion.

## Verification Commands

```powershell
git status --short
git -C "D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync" status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base a6cc271895cfc015c049e3d0731fff7e99b894e9 --head HEAD
python scripts/check_cvf_public_sync_candidate.py --public-root "D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync" --expected-remote https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git --baseline-ref origin/main --json
python governance/compat/run_worker_return_fast_gate.py
```

If the runner changes, add its focused test command. Validate every changed
workflow as YAML and inspect the resulting triggers/jobs. Do not use GitHub
reruns or pushes from the worker lane.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | one no-commit worker, then independent reviewer/closer |
| phase | implementation |
| baseHeadFor(phase) | dispatchBaseHead=`eb60e89d3e53c8ae11bab36d1767ff43ff81430d`; executionBaseHead=worker capture; closureBaseHead=reviewer capture |
| changedSetScope(phase) | exact public allowlist plus one private return |
| traceScope(phase, actor) | dual-repo state, run/job evidence, classifications, diffs and gates |
| commitOwner(phase) | reviewer only |
| crossBatchIsolation | no LPCI1 R4, dependency roadmap, product repair or other parked lane |
| Before status evidence | private and public worktrees clean; both staging areas empty; exact HEADs and remotes captured before worker edits |
| nextMoveSurfaces | named worker return, then independent review |

## Dual Agent Surface Matrix

| Surface | Role | Interface | Authority / risk boundary | Evidence | Adapter boundary |
| --- | --- | --- | --- | --- | --- |
| INTERNAL_AGENT | worker | local filesystem, Git and GitHub read-only CLI | allowlisted local candidate only | worker return | no runtime agent adapter |
| EXTERNAL_AGENT_CLI_MCP | deferred | none | no external-agent invocation or write | NOT_APPLICABLE_WITH_REASON | separate authorization required |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_PCIT_R1_PUBLIC_CI_TRUTHFULNESS_AND_CORPUS_BOUNDARY_RECONCILIATION_WORKER_RETURN_2026-08-27.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required worker-return sections: Purpose; Scope / Methodology; Findings /
Position; Risk / Corrective Action; Checker Source Read-Ahead Block; Agent
Operation Trace Block; Delta Execution Claim Boundary Control Block; Public
Export Disposition; Claim Boundary; git status --short; Changed Files; Command
Evidence; No-Commit Statement. Record `executionBaseHead` at start.

Conditional sections must be present with evidence or `N/A with reason`:
External Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus
Completeness And Report Integrity; Finding-To-Governance Learning Disposition;
Epistemic Process Block; Machine Closure Package.

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | optional; prefer an Independent Reviewer Addendum in the worker return if sufficient |
| reviewerOwnedClosurePaths | worker return, roadmap terminal status and continuity; public candidate paths only after acceptance |
| closureOwner | independent orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

## Review Gate

Independent review must reclassify every red job, verify the coverage matrix,
rerun focused/local gates, inspect both diffs, and reject any hidden genuine
failure or out-of-scope change before considering a commit.

## Closure Checklist

Exact allowlist; clean starts; classifications complete; coverage preserved;
focused proof; public-sync preflight; zero product/dependency/secret/provider
change; worker HEADs unchanged; staging empty; independent review complete.

## Return-To-Orchestrator Conditions

Return only `COMPLETE_PENDING_REVIEW` when every criterion passes, otherwise
`BLOCKED_WITH_REASON` at the first named stop condition. Do not propose R2 in
the worker return.

## Operator Checkpoint

No checkpoint is required for allowlisted local reversible work. Stop for a
genuine product defect requiring repair, any public write, dependency change,
secret/provider need, destructive action or successor proposal.

## Public/Provenance Boundary

| Field | Value |
| --- | --- |
| private root | current provenance workspace |
| public root | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync` |
| expected public remote | `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git` |
| worker public effects | forbidden; local reversible edits only |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Public sync`, role=`dispatcher`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Public sync" --role dispatcher --lifecycle-phase pre-implementation` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | none |
| Dispatch impact | exact repository and no-commit controls remain mandatory |

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "PCIT-R1",
  "requestedProfile": "P4_CRITICAL",
  "classification": {
    "taskKind": "PUBLIC_RELEASE",
    "authorityImpact": "USES_EXISTING_OWNER",
    "externalEffect": "LOCAL_REVERSIBLE",
    "dataSensitivity": "PUBLIC",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "BOUNDED_CLUSTER",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "OWNER_COMPOSITION"
  },
  "pathFamilies": ["AGENT_HANDOFF_V59_2026-08-11.md", "CVF_SESSION", "CVF_SESSION_MEMORY.md", ".github/workflows", "scripts", "docs/baselines", "docs/roadmaps", "docs/reviews"],
  "claims": ["public CI candidate separates public-safe checks from private-only governance"],
  "requiredProof": ["exact run inventory", "failure classification", "coverage matrix", "focused tests", "public-sync preflight", "independent review"],
  "operatorCheckpoints": ["genuine product defect", "scope expansion", "public write"],
  "forbiddenEffects": ["worker commit", "worker push", "worker deploy", "secret read", "provider call", "product source edit", "dependency upgrade"],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": null,
    "completenessClaimChanged": false
  }
}
```

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_authoring.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_dispatch_scaffold_provenance.py` |
| literalTokensReviewed | dispatch envelope placement, source columns, fulfillment manifest, proof atomicity, handoff fields, dual surface rows, public disposition and task JSON |
| gateRunPurpose | confirm final dispatch packet after source-first authoring |
| claimBoundary | machine conformance does not prove candidate or server success |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | private provenance and public-sync read-only evidence |
| Session or invocation | PCIT-R1 dispatch, 2026-08-27 |
| Working directory | private root; public sibling read-only |
| Command or tool surface | Git reads, file reads, GitHub Actions metadata/log reads, scaffold helper, apply patch and governance gates |
| Target paths | roadmap, baseline and this work order |
| Allowed scope source | operator next-roadmap instruction |
| Before status evidence | clean worktree in private at `eb60e89d3e53c8ae11bab36d1767ff43ff81430d`; clean worktree in public at `a0ef5923d100b02c43294815ac9d01d8db20e8b8`; both staging areas empty |
| After status evidence | three private dispatch artifacts pending gate/commit |
| Diff evidence | `git diff --name-status` plus untracked manifest |
| Approval boundary | dispatch only; no implementation or public write |
| Claim boundary | source-verified CI finding and bounded worker authority only |
| Agent type | dispatcher |
| Invocation ID | `pcit-r1-dispatch-2026-08-27` |
| Expected manifest | roadmap, baseline, work order |
| Actual changed set | must match expected manifest before dispatch commit |
| Manifest delta | must be NONE |
| Deletion or rename disposition | N/A with reason: none authorized |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | no-commit public CI candidate preparation |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: exact GitHub run metadata and local command output only |
| actionEvidence | ACTION_EVIDENCE_PRESENT: local allowlisted diff only |
| invocationBoundary | read-only hosted metadata plus local reversible edits |
| interceptionBoundary | no runtime/provider/secret/public-write interception |
| claimLanguage | candidate and classification evidence, never green/production claim before exact-SHA proof |
| forbiddenExpansion | product source, dependencies, secrets, provider/live, push, deploy, successor |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | NOT_TRIGGERED: receipts are evidence, not absorbed external authority |
| Matching local-view guard | `governance/compat/check_public_export_disposition.py` plus public-sync preflight |
| Owner surface | public GitHub Actions workflows |
| Disposition | RECONCILED_DESIGN_INPUT_ONLY |
| Claim boundary | no external document or repository corpus is absorbed |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: exact workflow/job diagnosis, not a corpus rescan.

## Foundation Storage Layout Block

N/A with reason: PCIT-R1 creates no durable governance foundation, storage
layout, index, locator or generated aggregate; it only reconciles existing
public workflows and their static runner.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - bounded named workflow/source cluster.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| public CI inherited private-provenance checks and masks product feedback | REPOSITORY_BOUNDARY_MISMATCH | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | apply existing public/provenance boundary to CI topology; add no new standard unless recurrence remains after repair |

## Public Export Disposition

BLOCKED_MISSING_PUBLIC_ARTIFACTS

Reason: worker has not produced an accepted public candidate; commit and push
belong to the independent reviewer after review.

## Claim Boundary

This work order authorizes one no-commit, workflow/runner-only candidate. It
does not authorize product repair, dependency mutation, CI suppression,
private corpus export, secrets, provider/live use, commit, push, deploy,
production readiness or a second tranche.
