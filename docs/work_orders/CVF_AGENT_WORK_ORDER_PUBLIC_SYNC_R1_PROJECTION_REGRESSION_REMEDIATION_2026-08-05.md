# CVF Agent Work Order - Public Sync R1 Projection Regression Remediation

Memory class: governed-worker-dispatch

Status: CLOSED_PASS_BOUNDED

Batch ID: PUBLIC-SYNC-R1

dispatchBaseHead: `85ffba891`

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: implementation worker

Reviewer/closer: reviewer/closer

Worker return path: `docs/reviews/CVF_PUBLIC_SYNC_R1_PROJECTION_REGRESSION_REMEDIATION_WORKER_RETURN_2026-08-05.md`

## Dispatch Prompt Envelope

Role: implementation worker for PUBLIC-SYNC-R1.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_PUBLIC_SYNC_R1_PROJECTION_REGRESSION_REMEDIATION_2026-08-05.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: worker captures current HEAD before edits.

Current-time notes: 2026-08-05 public-sync remediation only.

Do-not-misread notes: no public mutation, provider/live run, 19-failure cvf-web
repair, downstream edit, or governance-latency L0 work.

Required first actions: read startup files, guard orientation, literal gotchas,
paired baseline, this work order, and named source/checker files.

Return contract: leave the exact allowed changed set uncommitted and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Implement the three narrow consistency repairs authorized by the paired
GC-018 baseline and prove them without public mutation or provider use.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind public-sync --batch-id CVF-PUBLIC-SYNC-R1 --title "Public Sync Projection Regression Remediation" --date 2026-08-05 --base 85ffba891 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | public-sync plus no-commit worker |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced placeholders with verified authority, exact scope, offline verification, handoff controls, and stop conditions. |
| checkerReadAheadConfirmation | Dispatch-quality, handoff, ADIF, public-export, worker-return, trace, and structural checkers reviewed. |
| docOnlyNewFields | None. |
| claimBoundary | Dispatch authoring evidence only. |

## Authority Chain

| Authority | Evidence |
| --- | --- |
| Operator | `next` instruction after the 2026-08-05 blocked public-sync report |
| Baseline | `docs/baselines/CVF_GC018_PUBLIC_SYNC_R1_PROJECTION_REGRESSION_REMEDIATION_2026-08-05.md` |
| Repository boundary | `docs/reference/CVF_AGENTS_CRITICAL_REPOSITORY_BOUNDARY_2026-06-23.md` |
| Corrective precedent | public commit `27137db4d` and its provenance recovery review |

## Agent Roles

| Role | Ownership |
| --- | --- |
| Worker | Implements exact allowed paths and returns no-commit evidence. |
| Reviewer/closer | Recomputes evidence, accepts or rejects, and owns commits. |
| Operator | Owns any later public-push checkpoint. |

## Required First Reads

- `AGENTS.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V53_2026-07-26.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- paired baseline and this work order

## Pre-flight Checks

1. Confirm provenance HEAD `85ffba891` and a clean worktree except this dispatch packet.
2. Confirm public-sync HEAD `27137db4d`, exact public remote, and clean worktree.
3. Run pre-implementation autorun using the worker execution base.
4. Confirm provider keys are removed from every test process.

## Write Ownership

The worker owns only the five paths in Scope / Applies To and must not commit.
The reviewer owns material closure. The session-sync steward owns protected
continuity paths in a separate commit.

## Worker Autonomy / No-Question Rule

Repair allowed-scope checker failures directly. Return to the orchestrator
only for a source contradiction, additional path requirement, public mutation,
provider/live requirement, or inability to preserve the exact boundary.

## Scope / Applies To

Allowed changed paths:

- `scripts/cvf-public-sync.ps1`
- `scripts/cvf_projection_policy.json`
- `scripts/test_get_cvf_projection_map.ps1`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/package.boundary.test.ts`
- `docs/reviews/CVF_PUBLIC_SYNC_R1_PROJECTION_REGRESSION_REMEDIATION_WORKER_RETURN_2026-08-05.md`

Forbidden scope: every other path, public-sync mutation, public commit/push,
provider/network call, live test, runtime behavior change, and cvf-web repair.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Deny filtering owner | EXISTS | `scripts/cvf-public-sync.ps1` | denylist and `Test-Denied` | `DENY_PATTERNS` | public sync script | ACCEPT |
| Projection parity mirror | VALUE_SET | `scripts/cvf_projection_policy.json` | `sourceOfTruth` and `denyPatterns` | `denyPatterns` | projection policy | ACCEPT |
| Policy parity test seam | RUNTIME_BEHAVIOR | `scripts/test_get_cvf_projection_map.ps1` | real policy-parity assertions | `policyParity` | mapper test | ACCEPT |
| Five public deletions are accepted | VALUE_SET | `docs/reviews/CVF_PUBLIC_FIRST_GOLDEN_DOWNSTREAM_BOOTSTRAP_RECOVERY_2026-07-23.md` | public private-evidence removal row | `27137db4d` | corrective review | ACCEPT |
| Mandatory gateway is exported | VALUE_SET | `EXTENSIONS/CVF_GUARD_CONTRACT/package.json` | `exports` and `files` | `./runtime/mandatory-gateway` | package manifest | ACCEPT |
| Boundary assertions are stale | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_GUARD_CONTRACT/src/package.boundary.test.ts` | two exact collection assertions | `packageJson` | Vitest boundary test | ACCEPT |

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
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | dispatch lifecycle status, Source Verification Block, ADIF Defect Registry Disclosure, Agent Handoff Contract Control Block, Reviewer Closure Conversion, Public Export Disposition |
| gateRunPurpose | Confirm packet shape before worker implementation. |
| claimBoundary | Read-ahead evidence only; no repair or export claim. |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Work order path | `Test-Path` false before authoring | ACCEPT |
| Worker return path | `Test-Path` false before dispatch | ACCEPT |
| Batch token | repository search returned no prior matching packet | ACCEPT |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | worker returns no-commit evidence; reviewer/closer independently decides acceptance |
| phase | pre-implementation through reviewer closure |
| baseHeadFor(phase) | dispatchBaseHead=85ffba891; executionBaseHead=worker capture; closureBaseHead=reviewer capture |
| changedSetScope(phase) | exactly five allowed paths |
| traceScope(phase, actor) | worker return records commands, status, and exact diff |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer owns commit |
| crossBatchIsolation | clean worktree required; governance-latency L0, downstream work, broad cvf-web repair, and public export remain separate |
| nextMoveSurfaces | session-sync steward updates active continuity only after accepted material closure |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_PUBLIC_SYNC_R1_PROJECTION_REGRESSION_REMEDIATION_COMPLETION_2026-08-05.md` |
| reviewerOwnedClosurePaths | allowed source/test paths plus worker return; continuity paths only in a separate session-sync commit |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Intake Role Routing Decision

| Field | Decision |
| --- | --- |
| intake summary | First-party projection safety and stale-test consistency repair. |
| scope classification | Small bounded control-plane repair across five allowed paths. |
| risk sensitivity | Public-sync-sensitive, but provider/live, secrets, production, and readiness claims are forbidden. |
| selected role route | SINGLE_AGENT_MULTI_ROLE |
| role separation basis | No-commit worker evidence precedes reviewer/closer recomputation and commit ownership. |
| escalation condition | Stop and return to operator if public mutation, provider/live use, destructive action, claim expansion, or any extra path is required. |

## Single-Agent Multi-Role Control Block

| Control | Disposition |
| --- | --- |
| role separation ledger | Worker produces a no-commit return; reviewer/closer alone accepts, repairs, and commits. |
| evidence basis independent of memory | Source files, git diff, focused tests, and machine gates are recomputed from disk. |
| self-review boundary | Independent review is not claimed; the route is allowed only for this narrow non-public remediation. |
| escalation conditions | Stop for risk, scope, public-sync mutation, provider/live proof, secrets, destructive action, or claim-boundary change. |
| gate sequence | pre-dispatch, pre-implementation, worker-return fast gate, reviewer-fast, material pre-closure, commit steward, then separate session sync. |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `scripts/cvf-public-sync.ps1` | add exact deny rules for the five corrective-deletion paths |
| `scripts/cvf_projection_policy.json` | mirror the same deny rules exactly |
| `scripts/test_get_cvf_projection_map.ps1` | add focused proof that all five paths classify denied and parity remains MATCH |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/package.boundary.test.ts` | add mandatory gateway to both exact expected collections |
| worker return | record first failure, repairs, final offline commands, exact changed set, and no-commit evidence |

## Execution Plan

1. Capture `executionBaseHead`, status, and both remotes; stop if either worktree is dirty.
2. Add the five exact deny patterns to script and policy; update the focused mapper test.
3. Align only the stale package-boundary expectations.
4. Clear Alibaba and DashScope key variables in the test process; run mapper tests, package-boundary test, typecheck, JSON parse, and diff hygiene.
5. Create the worker return and run the worker-return fast gate.
6. Stop without commit, public mutation, or push.

## Verification Commands

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/test_get_cvf_projection_map.ps1
python -m json.tool scripts/cvf_projection_policy.json
node_modules/.bin/vitest.cmd run src/package.boundary.test.ts
node_modules/.bin/tsc.cmd --noEmit
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short --untracked-files=all
```

Provider key variables must be cleared in the Guard Contract test process.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_PUBLIC_SYNC_R1_PROJECTION_REGRESSION_REMEDIATION_WORKER_RETURN_2026-08-05.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The worker return must preserve the checker-recognized section labels for:

- Purpose
- Scope / Methodology
- Findings / Position
- Risk / Corrective Action
- Claim Boundary
- Agent Operation Trace Block
- Delta Execution Claim Boundary Control Block
- Public Export Disposition
- External Knowledge Intake Routing
- Rescan Intelligence Hardening
- Corpus Completeness And Report Integrity
- Finding-To-Governance Learning Disposition
- Epistemic Process Block
- Machine Closure Package

The worker return must also record `executionBaseHead` and command-backed
`git status --short` evidence. Every conditional section above must remain
present; when it does not apply, resolve it explicitly as `N/A with reason` or
`NOT_APPLICABLE_WITH_REASON` rather than omitting it.

## External Knowledge Intake Routing

| Field | Disposition |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: no external knowledge intake route is opened |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | the bounded public-sync projection remediation work order |
| Disposition | N/A with reason: no external-agent report, corpus, provider output, or new external knowledge source is consumed |
| Claim boundary | local source verification does not establish or absorb any external claim |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: exact deny rules prevent the known five-file
regression and the boundary-test delta is limited to manifest parity.

Evidence Comparison Requirement: compare focused results with this prediction.

Contradiction Handling Requirement: any additional required path or public
candidate mutation returns `BLOCKED_WITH_REASON`.

Claim Update Requirement: worker records confirmed, narrowed, or invalidated.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | local private provenance repository |
| Session or invocation | PUBLIC-SYNC-R1 dispatch, 2026-08-05 |
| Working directory | repository root |
| Command or tool surface | governed reads, read-only diagnostics, scaffold helper, ADIF resolver, and packet authoring |
| Target paths | paired baseline and work order |
| Allowed scope source | operator `next` instruction after blocked public-sync report |
| Before status evidence | HEAD `85ffba891`; clean worktree in provenance and public-sync before packet authoring |
| After status evidence | paired packet pending pre-dispatch gate |
| Diff evidence | `git diff --name-status` |
| Approval boundary | dispatch authoring only |
| Claim boundary | no implementation, public mutation, provider call, commit, or push |
| Agent type | dispatcher |
| Invocation ID | `public-sync-r1-dispatch-2026-08-05` |
| Expected manifest | paired baseline and work order |
| Actual changed set | paired baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | local projection policy and test consistency |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: no runtime receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT: local file diff and focused test results only |
| invocationBoundary | local governed commands inside provenance |
| interceptionBoundary | no IDE, shell, git, provider, or agent interception claim |
| claimLanguage | the repair may prove filtering and test parity only |
| forbiddenExpansion | no runtime/provider/live/public push, cvf-web repair, downstream edit, or governance-latency L0 work |

## Acceptance Criteria

- [x] All five paths classify as denied.
- [x] Script/policy parity is MATCH.
- [x] Mapper focused test passes.
- [x] Package-boundary focused test and typecheck pass offline.
- [x] Exact worker changed set contains only the five allowed paths.
- [x] Public-sync HEAD and worktree remain unchanged.

Fail conditions:

- [x] N/A with reason: no provider/live execution or public mutation occurred.
- [x] N/A with reason: none of the 19 cvf-web failures was repaired here.
- [x] N/A with reason: no extra implementation path was required; the
  pre-authorized completion review and work-order closure conversion are
  reviewer-owned artifacts.

## Evidence Requirements

- Exact before/after SHA and `git status --short --untracked-files=all`.
- Script/policy parity and five-path denial results.
- Focused package-boundary and typecheck results with keys cleared.
- Public-sync HEAD/status proving no mutation.
- Worker-return fast-gate result and exact changed-file manifest.

## Review Gate

Implementation requires this work order plus a passing pre-dispatch autorun
gate. Closure requires reviewer acceptance under the selected
`SINGLE_AGENT_MULTI_ROLE` route, a passing committed material-range
pre-closure gate, and a separate continuity sync. Independent review is not
claimed.

## Operator Checkpoint

Operator authority in `next` releases this remediation dispatch only. A public
commit or push remains blocked until a later reviewed public changed set has no
deferred/private artifact and its required tests pass.

## Closure Checklist

- [x] Worker return is complete and no-commit.
- [x] Every focused command passes after the last implementation edit.
- [x] Exact worker allowed changed set matches.
- [x] Reviewer recomputed evidence from disk; independence is not claimed.
- [x] Material pre-closure passed on committed range
  `f645f19c8..822b03ebc`; commit steward passed before commit.
- [x] N/A with reason: final closure continuity is owned by the required
  separate handoff-sync commit after this closure conversion.
- [x] Public-sync remains clean and unchanged at `27137db4d`.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_PUBLIC_SYNC_R1_PROJECTION_REGRESSION_REMEDIATION_COMPLETION_2026-08-05.md` | reviewer recomputation plus split material pre-closure 75/75 | PASS |
| Roadmap state | no active roadmap; standalone paired GC-018 remediation | no roadmap status changed | N/A with reason: standalone work order |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | aggregate drift check passed; no registry content change required | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | corpus registry gates passed; no registry content change required | PASS |
| External evidence digest | no external evidence absorbed | repository-local source and public-clone status only | N/A with reason: no external evidence digest |
| System loop interlock | no system-loop registry change | system loop interlock gate passed in material pre-closure | N/A with reason: no interlock mutation |
| Session continuity | active handoff | material sync commit `a4246f2f2`; closure sync follows separately | N/A with reason: final sync is separate |
| Implementation | four authorized source/test paths | material commit `822b03ebc` | PASS |
| Worker return | `docs/reviews/CVF_PUBLIC_SYNC_R1_PROJECTION_REGRESSION_REMEDIATION_WORKER_RETURN_2026-08-05.md` | `COMPLETE_PENDING_REVIEW`; worker fast gate PASS | PASS |
| Public export | sibling public-sync clone | clean unchanged SHA `27137db4d`; no public commit | N/A with reason: DEFERRED_PRIVATE_ONLY |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| five private paths classify `SKIP_DENIED` | five named assertions passed | PASS |
| all projection policy groups match source script | 52/52 focused mapper suite passed | PASS |
| public clone remains unchanged | empty status at `27137db4d` | PASS |
| live/provider receipt | no live/provider action authorized or performed | N/A with reason: local static remediation only |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | `scripts/cvf-public-sync.ps1`; `scripts/cvf_projection_policy.json`; `scripts/get_cvf_projection_map.ps1`; `EXTENSIONS/CVF_GUARD_CONTRACT/package.json` |
| Runtime behavior claimed | N/A_WITH_REASON: projection policy and focused local test consistency only |
| Helper/checker implementation claimed | BOUNDED: exact deny enforcement and regression assertions only |
| Provider/live proof claimed | N/A_WITH_REASON |
| Provider registry surfaces | N/A_WITH_REASON: no provider registry, provider selection, or live-governance claim |
| Public-sync claimed | N/A_WITH_REASON: public clone stayed unchanged |
| Freshness disposition | PASS - current source and package manifest were read directly; no absent, hardcoded, or unimplemented runtime claim is made |

## Return-To-Orchestrator Conditions

- Source contradiction or missing authority.
- Need for any path outside Allowed scope.
- Any provider/live test or public mutation requirement.
- Any proposal to repair the 19 cvf-web failures in this tranche.
- Any gate failure not repairable inside packet or allowed source/test scope.

## Claim Boundary

This work order authorizes only projection-denylist parity, its focused test,
and one stale package-boundary test repair. It does not authorize public export.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this no-commit remediation packet creates no public commit. A later
public-export decision must use a newly reviewed public-safe changed set.
