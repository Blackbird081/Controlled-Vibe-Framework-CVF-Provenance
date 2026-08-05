# CVF Agent Work Order - GLP Public R1 Governance Latency Carrier Refresh

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: GLP-PUBLIC-R1

dispatchBaseHead: `744a02bdc`

executionBaseHead: `744a02bdc`

closureBaseHead: `744a02bdc`

Commit mode: WORKER_MAY_COMMIT

Worker: Codex public-sync executor

Reviewer/closer: Codex bounded evidence reviewer

## Dispatch Prompt Envelope

Role: public-sync executor and bounded closer for GLP-PUBLIC-R1.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_GLP_PUBLIC_R1_GOVERNANCE_LATENCY_CARRIER_REFRESH_2026-08-06.md`

Commit mode: WORKER_MAY_COMMIT in the sibling public-sync clone only.

executionBaseHead: `744a02bdc` provenance; public base `a307da84a`.

Current-time notes: operator selected the exact public GitHub repository on
2026-08-06.

Do-not-misread notes: do not export private GLP packets, change runtime, call a
provider, or broaden beyond the single carrier path.

Required first actions: verify both remotes, both worktrees, exact carrier diff,
repository boundary, paired baseline, and public startup files.

Return contract: create public commit and push evidence, then close the private
packet only if all acceptance criteria pass.

## Purpose

Copy the accepted five-semantic governance-latency block to the existing public
carrier owner, verify the bounded bootstrap behavior, commit, and push `main`.

## Agent Roles

| Role | Ownership |
| --- | --- |
| Operator | selected the exact public repository and owns any later scope expansion |
| Executor | edits and commits exactly one public carrier path |
| Reviewer/closer | recomputes the diff, test, leakage scan, remote push, and clean status |

## Required First Reads

- `AGENTS.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V55_2026-08-05.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- the paired baseline and repository-boundary reference
- public clone `AGENTS.md`, its current public continuation pointer,
  `docs/GET_STARTED.md`, and `docs/reference/CVF_WORKSPACE_RULES.md`

## Pre-flight Checks

1. Provenance HEAD is `744a02bdc` and began clean.
2. Public HEAD and `origin/main` are both `a307da84a` and began clean.
3. Public remote is the exact operator-selected repository and branch is `main`.
4. Direct no-index diff contains only the missing five-semantic block.

## Write Ownership

Codex owns the one public carrier edit and public commit. Private packet and
completion commits stay separate. No downstream or other public path is owned.

## Authority Chain

| Authority | Evidence |
| --- | --- |
| Operator | explicit push to `Blackbird081/Controlled-Vibe-Framework-CVF.git` |
| Baseline | `docs/baselines/CVF_GC018_GLP_PUBLIC_R1_GOVERNANCE_LATENCY_CARRIER_REFRESH_2026-08-06.md` |
| Private closure | GLP-T4 `CLOSED_PASS_BOUNDED_DEFERRED_PRIVATE_ONLY` |
| Boundary | public mutation only from sibling public-sync clone |

## Scope / Applies To

Allowed public changed path:

- `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md`

Reviewer-owned private closure path:

- `docs/reviews/CVF_GLP_PUBLIC_R1_GOVERNANCE_LATENCY_CARRIER_REFRESH_COMPLETION_2026-08-06.md`

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind public-sync --batch-id CVF-GLP-PUBLIC-R1 --title "Governance Latency Carrier Public Refresh" --date 2026-08-06 --base 744a02bdc --commit-mode WORKER_MAY_COMMIT --stdout` |
| generatedProfile | public-sync plus `WORKER_MAY_COMMIT` |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with one-path manifest, exact commands, boundaries, and closure ownership |
| checkerReadAheadConfirmation | dispatch-quality, public-export, closure-packaging, and trace checkers reviewed |
| docOnlyNewFields | None |
| claimBoundary | work-order authority only until public push receipt exists |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Public carrier path | EXISTS | `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md` | Governance Latency and Approval Continuity | `CVF_DOWNSTREAM_AGENTS_TEMPLATE.md` | downstream template | ACCEPT |
| Public allowlist owner | VALUE_SET | `scripts/cvf-public-sync.ps1` | `WORKSPACE_KIT_FILES` | `CVF_DOWNSTREAM_AGENTS_TEMPLATE.md` | public-sync script | ACCEPT |
| Golden test owner | EXISTS | `scripts/test_cvf_golden_downstream_bootstrap.ps1` | script entrypoint | `test_cvf_golden_downstream_bootstrap.ps1` | bootstrap test | ACCEPT |
| Authorized public remote | VALUE_SET | `docs/reference/CVF_AGENTS_CRITICAL_REPOSITORY_BOUNDARY_2026-06-23.md` | Critical Repository Boundary | `Controlled-Vibe-Framework-CVF.git` | Git remote | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045,
ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039,
ADIF-0043, ADIF-0049, ADIF-0006.

Disclosure count: 20

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_closure_packaging_preflight.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | dispatch status, Source Verification Block, exact manifest, Public Export Disposition, operation trace |
| gateRunPurpose | confirm work-order structure before public mutation |
| claimBoundary | structural confirmation only |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | one bounded executor/reviewer under explicit operator public authority |
| phase | public refresh through closure |
| baseHeadFor(phase) | provenance `744a02bdc`; public `a307da84a` |
| changedSetScope(phase) | one public carrier plus private packet/closure artifacts |
| traceScope(phase, actor) | exact Git diff, focused test, commit, push, and clean status |
| commitOwner(phase) | Codex owns public commit; provenance commits remain separate |
| crossBatchIsolation | clean worktree required; GLP private packets, WS2, GC010-AER, runtime, provider, and downstream repos excluded |
| Before status evidence | clean worktree in provenance and public-sync clones; public `HEAD=origin/main=a307da84a` |
| nextMoveSurfaces | session-sync follows a committed completion review |

## Worker Autonomy / No-Question Rule

Repair only formatting or test defects within the allowed carrier path. Stop
for any additional path, source contradiction, private leakage, remote mismatch,
or failed focused bootstrap behavior.

## Work-Order Fulfillment Manifest

| Artifact | Required action |
| --- | --- |
| public carrier | insert the exact accepted five-semantic block |
| focused proof | run golden downstream bootstrap test locally without provider use |
| Git evidence | commit one path, push `main`, and prove clean synchronized status |
| private completion | record public commit, remote, artifact path, test, and boundaries |

## Execution Plan

1. Commit this private dispatch packet after pre-dispatch gates pass.
2. Insert the exact carrier block in the sibling public-sync clone.
3. Confirm one-path diff and absence of private GLP artifact tokens.
4. Run `scripts/test_cvf_golden_downstream_bootstrap.ps1`.
5. Commit the one public path and run a range-aware public-safe pre-push check.
6. Push `main`, verify `HEAD=origin/main`, and close the private packet.

## Verification Commands

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/test_cvf_golden_downstream_bootstrap.ps1
git diff --check
git diff --name-status
git push origin main
git fetch origin
git status -sb
```

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex public-sync executor/closer |
| Provider or surface | local provenance and sibling public-sync Git worktrees |
| Session or invocation | GLP-PUBLIC-R1, 2026-08-06 |
| Working directory | both repository roots, each used only for its owned paths |
| Command or tool surface | local file edit, focused PowerShell test, Git commit/fetch/push/status |
| Target paths | exact fulfillment manifest |
| Allowed scope source | operator instruction and paired GC-018 |
| Before status evidence | clean worktree in provenance at `744a02bdc` and public-sync at `a307da84a` |
| After status evidence | pending execution |
| Diff evidence | exact Git name-status and content diff |
| Approval boundary | one public carrier refresh and push |
| Claim boundary | no private packet export, downstream adoption, runtime, provider, or production claim |
| Agent type | single-agent bounded executor/reviewer |
| Invocation ID | `glp-public-r1-2026-08-06` |
| Expected manifest | two private dispatch paths, one public carrier, one later private completion |
| Actual changed set | pending execution |
| Manifest delta | pending execution |

Before status evidence: both worktrees were clean; provenance HEAD
`744a02bdc`; public HEAD and `origin/main` `a307da84a`.

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | public documentation/template distribution only |
| claimDisposition | CLAIM_REJECTED: no execution-control or runtime-enforcement behavior is claimed |
| receiptEvidence | N/A with reason: this packet makes no Delta runtime receipt claim |
| actionEvidence | N/A with reason: public Git distribution is not Delta runtime action evidence |
| invocationBoundary | local Git and focused offline test |
| interceptionBoundary | no direct interception, wrapper, proxy, or runtime gate |
| claimLanguage | carrier content exported; adoption and effect remain unproven |
| forbiddenExpansion | runtime, provider/live, downstream mutation, deployment, or universal control |

## Acceptance Criteria

- [ ] Exact one-path public diff.
- [ ] Five-semantic carrier block matches provenance.
- [ ] Focused golden bootstrap test passes.
- [ ] Private leakage scan passes.
- [ ] Public commit is pushed to the authorized remote.
- [ ] Both worktrees are clean.

## Evidence Requirements

- Exact before/after public Git anchors and remote.
- One-path content and name-status diff.
- Focused golden bootstrap test output.
- Private-token leakage scan.
- Public push result and `HEAD=origin/main` proof.

## Review Gate

Reviewer recomputes every acceptance item from disk. Any second changed public
path or private leakage rejects the public commit before push.

## Closure Checklist

- [ ] Resolve every acceptance criterion with command-backed evidence.
- [ ] Record public commit, remote, branch, and artifact path.
- [ ] Mark the private baseline/work order closed without exporting them.
- [ ] Record `EXPORTED` only for the public carrier.
- [ ] Leave both worktrees clean.

## Return-To-Orchestrator Conditions

Return `CLOSED_PASS_BOUNDED_EXPORTED` only after the pushed commit is fetched
and equals public `origin/main`. Otherwise return `BLOCKED_WITH_REASON` without
claiming export.

## Operator Checkpoint

Satisfied: the operator explicitly selected the exact public GitHub repository
on 2026-08-06. No additional same-scope confirmation is required.

## Intake Role Routing Decision

| Field | Decision |
| --- | --- |
| intake summary | one-path public-safe carrier refresh |
| scope classification | bounded documentation/template distribution |
| risk sensitivity | public release, no secrets/provider/runtime |
| selected role route | SINGLE_AGENT_MULTI_ROLE |
| role separation basis | command-backed recomputation before push; no independent-review claim |
| escalation condition | any second path, leakage, remote mismatch, test failure, or claim expansion |

## Single-Agent Multi-Role Control Block

| Control | Disposition |
| --- | --- |
| role separation ledger | executor edit precedes a fresh reviewer diff/test/leakage recomputation |
| evidence basis independent of memory | current files, Git objects, test output, and remote refs |
| self-review boundary | no independent-review claim; operator explicitly owns the public release decision |
| escalation conditions | second path, private leakage, remote mismatch, failed test, or broadened claim |
| gate sequence | pre-dispatch, pre-implementation, focused test, public commit, pre-push, push, private closure |

## Foundation Storage Layout Block

N/A with reason: this work order edits an existing public carrier in place and
does not create, split, relocate, or refactor a governance foundation layout or
index.

## Stop Conditions

Stop on any second public path, private leakage, failed focused test, divergent
remote, rejected push, or required runtime/provider/downstream change.

## Claim Boundary

Authorize only the public-safe carrier refresh and its Git/test evidence. Do
not infer adoption, measured latency reduction, runtime enforcement, provider
behavior, production readiness, or universal control.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: the work order remains private. The public carrier becomes `EXPORTED`
only after remote commit evidence is recorded in the completion review.
