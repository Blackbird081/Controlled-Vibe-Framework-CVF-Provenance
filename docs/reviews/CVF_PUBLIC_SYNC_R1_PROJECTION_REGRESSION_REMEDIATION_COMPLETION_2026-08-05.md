# CVF Public-Sync R1 Projection Regression Remediation Completion

Memory class: FULL_RECORD

docType: review

Status: REVIEW_ACCEPTED_PENDING_COMMIT

Date: 2026-08-05

dispatchBaseHead: `85ffba891`

executionBaseHead: `f645f19c8445dca4a4583712bb1f4d97451d89a6`

closureBaseHead: `f645f19c8445dca4a4583712bb1f4d97451d89a6`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Review route: `SINGLE_AGENT_MULTI_ROLE`

## Purpose

Record reviewer acceptance of the bounded provenance-side projection repair
without mutating or exporting to the public-sync clone.

## Scope / Methodology

The reviewer recomputed the worker evidence from disk with known provider-key
variables cleared, inspected the exact diff, verified the sibling public clone
remained clean, and compared the result to every work-order acceptance item.
Independent review is not claimed; the controlling single-agent route requires
role-separated recomputation and reviewer-owned commit decisions.

## Source Inventory

| Source | Use |
|---|---|
| `docs/baselines/CVF_GC018_PUBLIC_SYNC_R1_PROJECTION_REGRESSION_REMEDIATION_2026-08-05.md` | authority and bounded risk |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_PUBLIC_SYNC_R1_PROJECTION_REGRESSION_REMEDIATION_2026-08-05.md` | acceptance and changed-set contract |
| `docs/reviews/CVF_PUBLIC_SYNC_R1_PROJECTION_REGRESSION_REMEDIATION_WORKER_RETURN_2026-08-05.md` | no-commit worker evidence |
| `scripts/cvf-public-sync.ps1` | projection source of truth |
| `scripts/cvf_projection_policy.json` | machine-readable policy parity |
| `scripts/get_cvf_projection_map.ps1` | read-only mapper under test |
| `scripts/test_get_cvf_projection_map.ps1` | focused disposable-fixture proof |
| `EXTENSIONS/CVF_GUARD_CONTRACT/package.json` | package boundary source authority |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/package.boundary.test.ts` | focused package parity proof |

## Findings / Position

Disposition: `REVIEW_ACCEPTED_PENDING_COMMIT`.

- All five known private evidence paths classify as `SKIP_DENIED`.
- Script and JSON policy deny arrays match.
- The policy's pre-existing allowed-script drift was reconciled to the source
  script inside the already-authorized policy path.
- Guard Contract expected package exports/files now include the existing
  `mandatory-gateway` entries declared by `package.json`.
- Public-sync remained clean at
  `27137db4d9aa2aea931ddd2507185d5c24943080`.
- No provider, network, live governance, public mutation, or public push action
  was performed during implementation or reviewer recomputation.

## Risk / Corrective Action

| Risk | Corrective action | Result |
|---|---|---|
| Private evidence reintroduced by broad `docs/reference` projection | five exact anchored deny patterns in script and policy | PASS |
| Script/policy drift | retained real-group parity assertions; reconciled current allowed-script list | PASS |
| Package test stale against package manifest | expected exports and files updated from current `package.json` | PASS |
| Public clone accidental mutation | all tests use disposable fixtures; sibling status rechecked | PASS |
| Broad repair expansion | no cvf-web failure repair, runtime build, downstream edit, or public candidate | PASS |

## Roadmap-To-Work-Order Trace Matrix

| Authority item | Work-order requirement | Final artifact | Disposition |
|---|---|---|---|
| GC-018 exact five-file protection | exact deny rules in script and policy | script, policy, and five focused assertions | PASS |
| GC-018 policy parity | mapper parity remains MATCH | 52/52 focused suite | PASS |
| GC-018 stale package boundary | align test to existing manifest only | 2/2 focused Vitest plus typecheck | PASS |
| Public boundary | public clone stays read-only | empty public `git status --short` at unchanged SHA | PASS |
| No-commit handoff | worker returns evidence without commit | worker return at `COMPLETE_PENDING_REVIEW` | PASS |

N/A with reason: this remediation derives from its paired GC-018 rather than an
active roadmap tranche; the matrix maps the complete authority chain instead.

## Closure Diff Gate

| Requirement | Work-order instruction | Final evidence | Disposition |
|---|---|---|---|
| Five paths denied | add exact deny rules and fixtures | five named `private_evidence_deny_*` assertions pass | PASS |
| Script/policy parity | mirror exact rules | every real policy group reports PASS | PASS |
| Mapper regression | run focused matrix | 52/52 PASS | PASS |
| Package boundary | align expected collections | 2/2 PASS | PASS |
| Static typing | run `tsc --noEmit` | PASS | PASS |
| Worker manifest | exactly four source/test paths plus worker return | MATCH before completion packet | PASS |
| Public isolation | no mutation | public status empty; SHA unchanged | PASS |
| Provider/live prohibition | clear keys; do not call provider | no provider/network/live command in trace | PASS |

## Acceptance Criteria

- [x] All five paths classify as denied.
- [x] Script/policy parity is MATCH.
- [x] Mapper focused test passes.
- [x] Package-boundary focused test and typecheck pass offline.
- [x] Worker changed set contains only the five allowed paths.
- [x] Public-sync HEAD and worktree remain unchanged.
- [x] Worker return is complete and no-commit.
- [x] Reviewer recomputed evidence from disk.
- [x] Public export remains deferred to a separate reviewed tranche.

Fail-condition resolution:

- [x] N/A with reason: no provider/live execution or public mutation occurred.
- [x] N/A with reason: none of the 19 cvf-web failures was repaired here.
- [x] N/A with reason: no implementation path outside worker scope was needed;
  this completion packet is the pre-authorized reviewer-owned closure artifact.

## Verification / Evidence

All focused commands ran with `DASHSCOPE_API_KEY`, `ALIBABA_API_KEY`,
`CVF_ALIBABA_API_KEY`, `CVF_BENCHMARK_ALIBABA_KEY`, and `DEEPSEEK_API_KEY`
cleared in the command process.

| Command | Reviewer result |
|---|---|
| `python -m json.tool scripts/cvf_projection_policy.json` | PASS |
| `powershell -NoProfile -ExecutionPolicy Bypass -File scripts/test_get_cvf_projection_map.ps1` | PASS, 52/52 |
| `vitest.cmd run src/package.boundary.test.ts` | PASS, 1 file and 2/2 tests |
| `tsc.cmd --noEmit` | PASS |
| `python governance/compat/run_worker_return_fast_gate.py` | PASS; reviewer-fast 62/62 |
| `git diff --check` | PASS |
| public-sync `git status --short` | PASS, empty |
| public-sync `git rev-parse HEAD` | `27137db4d9aa2aea931ddd2507185d5c24943080` |

## Reviewer Independence And Claim Control

Reviewer independence: NOT_CLAIMED.

Reason: the committed work order selected `SINGLE_AGENT_MULTI_ROLE`. The worker
stopped without commit, and the reviewer recomputed commands and diffs from
disk before deciding acceptance. A different-agent or external independent
review was not required for this narrow private remediation and is not implied.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | `REVIEW_ACCEPTED_PENDING_COMMIT`; `CLOSED_PASS_BOUNDED`; `Closure item`; `Required artifact/path`; `Machine-readable evidence`; `Final status`; `DEFERRED_PRIVATE_ONLY` |
| gateRunPurpose | confirmation/evidence after checker read-ahead: keep the review packet non-closed until a non-empty committed range exists, then support closure conversion |
| claimBoundary | checker read-ahead validates artifact shape only and does not replace focused functional evidence |

## Governance Cost

The remediation required a paired dispatch packet, two governance commits,
four focused implementation edits, one worker return, and this completion
packet. Two worker-return fast-gate iterations exposed three literal/enum
repairs before final PASS. This cost is retained as evidence for future helper
hardening but does not authorize expanding this tranche.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | State |
|---|---|---|---|---|---|
| Projection policy can drift from its source script | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | retain and run focused real-group parity assertions | handled |
| Worker-return scaffold emitted a non-asserting retrospective marker | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | consider separate helper hardening only if reprioritized | deferred |

Runtime/provider/cost learning lane disposition: `N/A_WITH_REASON` because this
closure makes no runtime, provider-output, quota, token, or cost finding.

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator continuation -> paired GC-018/work order -> local source verification -> no-commit return -> reviewer closure |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this completion review |
| Disposition | ADAPT as bounded CVF-owned projection safety repair |
| Claim boundary | downstream/public observations remain evidence only; repo-governed CVF source remains authority |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: N/A with reason: no rescan, source-mirror refresh, or corpus
reassessment occurred.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - N/A with reason: no corpus
completeness or exhaustive-source claim is made.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: exact denies would block the five known private
paths and the package test would pass after manifest parity repair.

Evidence Comparison: confirmed for 5/5 deny classifications, 52/52 mapper
assertions, 2/2 package assertions, and TypeScript. One adjacent policy drift
was found and resolved within the authorized policy file.

Contradiction Handling: no evidence justified broad directory denial, cvf-web
repair, public candidate generation, or any provider/live action.

Claim Update: provenance-side remediation is closed; public export remains a
separate decision with separate evidence.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex reviewer/closer |
| Provider or surface | local private provenance repository |
| Session or invocation | PUBLIC-SYNC-R1 reviewer recomputation, 2026-08-05 |
| Working directory | repository root and Guard Contract package directory |
| Command or tool surface | local source inspection, focused PowerShell tests, JSON parse, Vitest, TypeScript, worker-return fast gate, git diff/status |
| Target paths | four implementation paths, worker return, and this completion review |
| Allowed scope source | committed GC-018/work order and reviewer closure conversion block |
| Before status evidence | HEAD `f645f19c8`; five-path worker return changed set; public clean at `27137db4d` |
| After status evidence | six-path material closure candidate; public remains clean at `27137db4d` |
| Diff evidence | `git diff --name-status`; `git status --short --untracked-files=all`; focused command outputs |
| Approval boundary | reviewer acceptance and provenance material commit only |
| Claim boundary | no independent-review, public export, provider/live, runtime, downstream, deployment, or production claim |
| Agent type | reviewer/closer |
| Invocation ID | `public-sync-r1-reviewer-2026-08-05` |
| Expected manifest | four implementation paths, worker return, and completion review |
| Actual changed set | four implementation paths, worker return, and completion review |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | provenance projection enforcement and focused test consistency only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT - deterministic local command evidence above |
| actionEvidence | ACTION_EVIDENCE_PRESENT - exact diff, test counts, and public status recomputed |
| invocationBoundary | repository-local execution with provider keys cleared |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, Web runtime, or adapter interception claim |
| claimLanguage | remediation passed focused local acceptance and may be committed to provenance |
| forbiddenExpansion | public candidate/push, broad cvf-web repair, provider/live proof, downstream edit, L0 work, runtime build, or deployment |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this closure repairs private provenance projection controls only. It
does not produce a reviewed public candidate, public commit, or public push.

Next action: commit and push the accepted provenance closure, then open a
separate public-export tranche only if its candidate and required tests pass.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 authority | `docs/baselines/CVF_GC018_PUBLIC_SYNC_R1_PROJECTION_REGRESSION_REMEDIATION_2026-08-05.md` | committed dispatch packet `3324361ef` | SATISFIED |
| Work-order authority | `docs/work_orders/CVF_AGENT_WORK_ORDER_PUBLIC_SYNC_R1_PROJECTION_REGRESSION_REMEDIATION_2026-08-05.md` | committed dispatch packet `3324361ef` | SATISFIED |
| Worker return | `docs/reviews/CVF_PUBLIC_SYNC_R1_PROJECTION_REGRESSION_REMEDIATION_WORKER_RETURN_2026-08-05.md` | status `COMPLETE_PENDING_REVIEW`; fast gate PASS | ACCEPTED |
| Completion review | this file | status `REVIEW_ACCEPTED_PENDING_COMMIT` | PENDING_COMMITTED_RANGE |
| Material changed set | four source/test paths plus worker return and completion review | `git diff --name-status`; Agent Operation Trace manifest | MATCH |
| Public export | sibling public-sync clone | clean SHA `27137db4d`; no public candidate/commit/push | DEFERRED_PRIVATE_ONLY |

## Claim Boundary

This completion closes only the private provenance projection-regression
remediation. It does not close the broader public-sync backlog, repair the 19
cvf-web failures, authorize public export, or reopen governance-latency L0.
