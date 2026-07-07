# CVF Agent Work Order - MSEA-R65D Provider Receipt-Link Integrity Checker Implementation

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: MSEA_R65D_PROVIDER_RECEIPT_LINK_INTEGRITY_CHECKER_IMPLEMENTATION

Dispatch base head: 961c56c5e

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: Codex reviewer/closer

Worker return path: `docs/reviews/CVF_MSEA_R65D_PROVIDER_RECEIPT_LINK_INTEGRITY_CHECKER_IMPLEMENTATION_WORKER_RETURN_2026-07-07.md`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA_R65D_PROVIDER_RECEIPT_LINK_INTEGRITY_CHECKER_IMPLEMENTATION.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R65D_PROVIDER_RECEIPT_LINK_INTEGRITY_CHECKER_IMPLEMENTATION_2026-07-07.md`

Paired baseline: `docs/baselines/CVF_GC018_MSEA_R65D_PROVIDER_RECEIPT_LINK_INTEGRITY_CHECKER_IMPLEMENTATION_2026-07-07.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START with `git rev-parse --short HEAD`.

Current-time notes: artifact date is 2026-07-07; provenance dispatch base is `961c56c5e`; public-sync is expected to be clean and `main...origin/main [ahead 2]` unless the operator has separately pushed or changed it.

Do-not-misread notes: this work order authorizes a bounded static checker in the sibling public-sync clone only. It does not authorize public-sync commit, public-sync push, provider status edits, provider/live proof, JSON receipt export, OpenAI certification uplift, or provenance runtime/source/test/checker edits.

Required first actions: read startup files, guard orientation, literal gotchas, this packet, the paired GC-018 baseline, R65C decision matrix and completion review, repository boundary, and every checker source listed in the Checker Source Read-Ahead Block.

Return contract: implement the bounded public-sync checker and static CI wiring, create the worker return artifact, run required gates, leave all changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Implement a static public-sync guard that prevents a provider readiness matrix
from publishing `CERTIFIED` provider rows whose `Latest Receipt` markdown link
does not resolve to a local public-sync file. The worker must wire the guard
into the existing public-sync static CI gate, prove it passes the current
Alibaba/DeepSeek certified rows, and preserve OpenAI as non-certified
`EXPERIMENTAL` without requiring an OpenAI receipt.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind public-sync --batch-id MSEA_R65D_PROVIDER_RECEIPT_LINK_INTEGRITY_CHECKER_IMPLEMENTATION --title "MSEA-R65D Provider Receipt-Link Integrity Checker Implementation" --date 2026-07-07 --base 961c56c5e --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | public-sync checker implementation plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Authored bounded R65D checker implementation dispatch from accepted R65C decision evidence and refreshed public-sync source verification. |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py` |
| docOnlyNewFields | R65D provider receipt-link integrity checker implementation route |
| claimBoundary | Dispatch authoring provenance only; no public push, provider/live proof, runtime implementation, or production behavior claim. |

## 1. Mission

Create `scripts/check_provider_receipt_link_integrity.py` in the sibling
public-sync clone. The checker must parse
`docs/reference/CVF_PROVIDER_LANE_READINESS_MATRIX.md`, require each
`CERTIFIED` provider row to contain a resolvable local markdown link in the
`Latest Receipt` cell, and return non-zero with clear diagnostics for missing,
external, escaping, or nonexistent receipt links. Then wire the checker into
`scripts/run_cvf_static_ci_gate.py` as one additional static CI check.

## 2. Authority Chain

| Authority | Path | Use |
| --- | --- | --- |
| Startup front door | `CVF_SESSION_MEMORY.md` | Current session mode and mandatory startup route |
| Bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | Compact next allowed move |
| Active state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Canonical state |
| Active handoff | `AGENT_HANDOFF_V38_2026-07-06.md` | Current R65D context |
| Guard orientation | `docs/reference/guard_orientation/README.md` | Worker guard map |
| Literal gotchas | `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | Literal-format traps |
| R65C decision matrix | `docs/reference/CVF_MSEA_R65C_PUBLIC_SYNC_PUBLISH_OR_HOLD_AND_PROVIDER_RECEIPT_LINK_INTEGRITY_DECISION_MATRIX_2026-07-07.md` | Accepted checker recommendation |
| R65C completion review | `docs/reviews/CVF_MSEA_R65C_PUBLIC_SYNC_PUBLISH_OR_HOLD_AND_PROVIDER_RECEIPT_LINK_INTEGRITY_CHECKER_DECISION_COMPLETION_REVIEW_2026-07-07.md` | Accepted next-move recommendation and public-sync hold |
| Repository boundary standard | `docs/reference/CVF_AGENTS_CRITICAL_REPOSITORY_BOUNDARY_2026-06-23.md` | Public/provenance separation and push boundary |

## 3. Agent Roles

| Role | Responsibility |
| --- | --- |
| Worker | Implement bounded public-sync checker and static CI wiring; create worker return; no commit. |
| Reviewer/closer | Review worker return and public-sync diff, run gates, decide closure and commit if accepted. |
| Operator | Owns any public push and any later publication action. |

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| Intake source | R65C accepted completion review and operator fresh R65D checker packet authorization |
| Scope classification | BOUNDED_PUBLIC_SYNC_CHECKER_IMPLEMENTATION: public-sync static checker plus provenance worker return |
| Risk sensitivity | public repository release posture; no provider/live proof or production readiness |
| Selected role route | MULTI_AGENT_SINGLE_ROLE via worker no-commit implementation and reviewer/closer acceptance |
| Route mode | MULTI_AGENT_SINGLE_ROLE |
| role route | MULTI_AGENT_SINGLE_ROLE |
| Intake role | dispatcher routes R65C accepted checker recommendation to worker implementation role |
| Worker role | no-commit public-sync checker implementation worker |
| Reviewer role | reviewer/closer validates diff, gates, and public/provenance boundary |
| Commit owner | reviewer/closer only; worker must not commit |
| Role separation basis | worker creates bounded diff and evidence; reviewer/closer owns acceptance and commit; operator owns public push |
| Escalation condition | stop and return `BLOCKED_WITH_REASON` if public-sync is dirty before work, remote is wrong, current matrix contradicts source verification, the checker requires provider status edits, or static CI cannot be wired without widening scope |
| Claim boundary | no provider/live proof, no public push, no provenance runtime/source/test/checker edit, no production claim |

## 4. Scope

Allowed public-sync write scope:

- `scripts/check_provider_receipt_link_integrity.py`
- `scripts/run_cvf_static_ci_gate.py`

Allowed provenance worker output:

- `docs/reviews/CVF_MSEA_R65D_PROVIDER_RECEIPT_LINK_INTEGRITY_CHECKER_IMPLEMENTATION_WORKER_RETURN_2026-07-07.md`

Forbidden scope:

- no public-sync commit or push;
- no provenance runtime/source/test/checker edits;
- no provider status row edits;
- no README, docs index, Known Limitations, provider routing, provider matrix claim, or receipt content edits;
- no provider/live proof;
- no JSON receipt export;
- no OpenAI certification uplift;
- no private/generated MinerU output read.

## Scope / Target / Owner Boundary

The worker owns only the bounded public-sync diff and the single provenance
worker return artifact. The reviewer/closer owns acceptance and any material
commit. The operator owns any public push.

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker, wiring, and worker-return formatting
failures directly by reading the failing source and matching the literal
required shape. Worker should return to orchestrator only for source
contradiction, public-sync drift, wrong remote, forbidden-scope need, missing
authority, or a current public-sync matrix that fails the intended checker.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | No ADIF defectId is required for this exact resolver query. |

## 5. Required First Reads

| File | Required action |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V38_2026-07-06.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |
| `docs/baselines/CVF_GC018_MSEA_R65D_PROVIDER_RECEIPT_LINK_INTEGRITY_CHECKER_IMPLEMENTATION_2026-07-07.md` | READ |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R65D_PROVIDER_RECEIPT_LINK_INTEGRITY_CHECKER_IMPLEMENTATION_2026-07-07.md` | READ |
| `docs/reference/CVF_MSEA_R65C_PUBLIC_SYNC_PUBLISH_OR_HOLD_AND_PROVIDER_RECEIPT_LINK_INTEGRITY_DECISION_MATRIX_2026-07-07.md` | READ |
| `docs/reviews/CVF_MSEA_R65C_PUBLIC_SYNC_PUBLISH_OR_HOLD_AND_PROVIDER_RECEIPT_LINK_INTEGRITY_CHECKER_DECISION_COMPLETION_REVIEW_2026-07-07.md` | READ |
| `docs/reference/CVF_AGENTS_CRITICAL_REPOSITORY_BOUNDARY_2026-06-23.md` | READ |

## 6. Pre-Flight Checks

1. Capture provenance `executionBaseHead` with `git rev-parse --short HEAD`.
2. Run provenance `git status --short --branch`.
3. Run public-sync `git remote -v`.
4. Run public-sync `git status --short --branch`.
5. Confirm public-sync is clean and `main...origin/main [ahead 2]`, unless a fresh operator action changed it.
6. Confirm public-sync latest local commits include `fbb782fee` and `756c465e1`.
7. Confirm no public-sync push is performed.

## 6A. Source-Fidelity Pass

### Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Public-facing changes must use sibling public-sync clone | REPOSITORY_BOUNDARY | `docs/reference/CVF_AGENTS_CRITICAL_REPOSITORY_BOUNDARY_2026-06-23.md` | `## Critical Repository Boundary - 2026-05-09` | public-sync clone | repository boundary standard | ACCEPT |
| R65C accepted checker packet recommendation | PROVENANCE_SOURCE | `docs/reviews/CVF_MSEA_R65C_PUBLIC_SYNC_PUBLISH_OR_HOLD_AND_PROVIDER_RECEIPT_LINK_INTEGRITY_CHECKER_DECISION_COMPLETION_REVIEW_2026-07-07.md` | `## Decision / Disposition` | R65C_PUBLIC_SYNC_PUSH_READY_PENDING_OPERATOR_CONFIRMATION_AND_CHECKER_PACKET_RECOMMENDED_ACCEPTED | R65C completion review | ACCEPT |
| R65C decision matrix selected checker packet recommendation | PROVENANCE_SOURCE | `docs/reference/CVF_MSEA_R65C_PUBLIC_SYNC_PUBLISH_OR_HOLD_AND_PROVIDER_RECEIPT_LINK_INTEGRITY_DECISION_MATRIX_2026-07-07.md` | `## Decision` | CHECKER_PACKET_RECOMMENDED | R65C decision matrix | ACCEPT |
| Existing public-sync workflow runs static CI gate | PUBLIC_SYNC_SOURCE | sibling public-sync `.github/workflows/cvf-static-ci.yml` | line 48 | scripts/run_cvf_static_ci_gate.py | GitHub workflow | ACCEPT |
| Existing public-sync static CI has a check list entrypoint | PUBLIC_SYNC_SOURCE | sibling public-sync `scripts/run_cvf_static_ci_gate.py` | line 124 | run_checks | static CI gate runner | ACCEPT |
| Existing public-sync static CI returns CheckResult values | PUBLIC_SYNC_SOURCE | sibling public-sync `scripts/run_cvf_static_ci_gate.py` | lines 21-23 | CheckResult | release gate bundle check result | ACCEPT |
| Existing public-sync matrix has provider readiness status vocabulary | PUBLIC_SYNC_SOURCE | sibling public-sync `docs/reference/CVF_PROVIDER_LANE_READINESS_MATRIX.md` | lines 17-19 | CERTIFIED; EXPERIMENTAL | provider lane readiness matrix | ACCEPT |
| Existing public-sync matrix has Latest Receipt column | PUBLIC_SYNC_SOURCE | sibling public-sync `docs/reference/CVF_PROVIDER_LANE_READINESS_MATRIX.md` | line 25 | Latest Receipt | provider lane readiness matrix | ACCEPT |
| Existing Alibaba certified row has receipt link | PUBLIC_SYNC_SOURCE | sibling public-sync `docs/reference/CVF_PROVIDER_LANE_READINESS_MATRIX.md` | line 27 | Alibaba receipt link | provider lane readiness matrix | ACCEPT |
| Existing DeepSeek certified row has receipt link | PUBLIC_SYNC_SOURCE | sibling public-sync `docs/reference/CVF_PROVIDER_LANE_READINESS_MATRIX.md` | line 28 | DeepSeek receipt link | provider lane readiness matrix | ACCEPT |
| Existing OpenAI row is experimental and not certified | PUBLIC_SYNC_SOURCE | sibling public-sync `docs/reference/CVF_PROVIDER_LANE_READINESS_MATRIX.md` | line 29 | OpenAI row | provider lane readiness matrix | ACCEPT |
| Alibaba exported receipt file exists in public-sync | PUBLIC_SYNC_EVIDENCE | sibling public-sync `docs/audits/alibaba-canary/CVF_RECEIPT_20260421-072551-422037.md` | file path exists | CVF_RECEIPT_20260421-072551-422037.md | public-sync audit receipt | ACCEPT |
| DeepSeek exported receipt file exists in public-sync | PUBLIC_SYNC_EVIDENCE | sibling public-sync `docs/audits/deepseek-canary/CVF_RECEIPT_20260421-114125-19515e.md` | file path exists | CVF_RECEIPT_20260421-114125-19515e.md | public-sync audit receipt | ACCEPT |

### Planned New Public-Sync Fields

| Planned item | Intended path or symbol | Source disposition | Boundary |
| --- | --- | --- | --- |
| provider receipt-link integrity checker script | `scripts/check_provider_receipt_link_integrity.py` | DOC_ONLY_NEW in this dispatch; worker creates it in public-sync if source verification remains valid | static checker only; no live provider call |
| static CI checker adapter | `check_provider_receipt_link_integrity` or equivalent local function in `scripts/run_cvf_static_ci_gate.py` | DOC_ONLY_NEW in this dispatch; worker may choose exact function name if it is local and clear | returns `CheckResult` and does not weaken existing checks |

### Current Public-Sync Evidence Snapshot

| Public-sync item | Read-only evidence | Required use |
| --- | --- | --- |
| branch state | `main...origin/main [ahead 2]` | confirm worker starts from expected public-sync state |
| remote | public `Controlled-Vibe-Framework-CVF.git` | confirm correct public-sync clone, but do not push |
| R65A local commit | `fbb782fee` changed public OpenAI claim files | preserve accepted Option B posture |
| R65B local commit | `756c465e1` added provider audit receipt/index markdown | preserve receipt evidence |
| static CI workflow | `.github/workflows/cvf-static-ci.yml` line 48 | existing CI calls `scripts/run_cvf_static_ci_gate.py --json` |
| static CI runner | `scripts/run_cvf_static_ci_gate.py` line 124 | existing `run_checks` list can receive one additional checker |
| OpenAI row | `EXPERIMENTAL` and not certified | checker must not require OpenAI receipt link |

## 6B. Evidence Reuse And Encoding Plan

verificationMode: REUSE_PRIOR_VERIFICATION_WITH_FRESH_PUBLIC_SYNC_RECHECK

priorVerificationArtifact: `docs/reviews/CVF_MSEA_R65C_PUBLIC_SYNC_PUBLISH_OR_HOLD_AND_PROVIDER_RECEIPT_LINK_INTEGRITY_CHECKER_DECISION_COMPLETION_REVIEW_2026-07-07.md`

priorVerificationAnchor: `R65C_PUBLIC_SYNC_PUSH_READY_PENDING_OPERATOR_CONFIRMATION_AND_CHECKER_PACKET_RECOMMENDED_ACCEPTED`

freshRecomputeRequired: yes - worker must rerun public-sync status, remote, matrix read, and receipt path checks before editing

unicodePathHandling: use literal paths and UTF-8-safe readers; do not normalize path text outside assigned files

extractedTextAuthority: current public-sync files and current provenance governed artifacts, not provider memory

## 6C. Roadmap-To-Work-Order Trace Matrix

| Source requirement | Worker instruction |
| --- | --- |
| R65C accepted checker recommendation | implement bounded static checker |
| Public/provenance boundary | edit only sibling public-sync allowed files and one provenance worker return; do not push |
| Existing static CI runner | wire checker into `run_checks` without weakening existing checks |
| Existing matrix status model | require receipt links for `CERTIFIED` rows only |
| OpenAI Option B | keep OpenAI `EXPERIMENTAL`; do not require receipt link or change status |

## Write Ownership

| Path | Worker action |
| --- | --- |
| `scripts/check_provider_receipt_link_integrity.py` | create in public-sync, uncommitted |
| `scripts/run_cvf_static_ci_gate.py` | edit in public-sync only to invoke the new checker, uncommitted |
| `docs/reviews/CVF_MSEA_R65D_PROVIDER_RECEIPT_LINK_INTEGRITY_CHECKER_IMPLEMENTATION_WORKER_RETURN_2026-07-07.md` | create provenance worker return, uncommitted |

## Execution Plan

| Step | Action | Evidence |
| --- | --- | --- |
| 1 | Capture provenance and public-sync status plus public-sync remote | status and remote output |
| 2 | Re-read public-sync matrix and static CI runner | line/source evidence |
| 3 | Create static checker script | public-sync diff |
| 4 | Wire checker into static CI runner | public-sync diff |
| 5 | Run focused checker | command output |
| 6 | Run static CI gate if feasible | command output or exact blocker |
| 7 | Create worker return | worker-return path exists |
| 8 | Run provenance gates | worker-return fast gate and pre-implementation autorun |

## Checker Implementation Requirements

| Requirement | Worker instruction |
| --- | --- |
| parser | parse the provider readiness markdown table by header names rather than hard-coding line numbers |
| target status | treat exactly `CERTIFIED` as requiring a receipt link |
| target column | use the `Latest Receipt` column |
| markdown link | require a local markdown link target for each certified row |
| path safety | reject absolute URLs, root-escaping relative paths, missing files, and non-file targets |
| non-certified rows | do not require a link for `EXPERIMENTAL`, `DEGRADED`, or other non-`CERTIFIED` values |
| diagnostics | include provider name, status, link target, and failure reason |
| exit code | return 0 only when all certified receipt links resolve |
| static CI integration | add one `CheckResult` entry while preserving all existing checks |
| current expected result | checker passes Alibaba and DeepSeek; OpenAI is skipped as non-certified |

## Evidence Requirements

- Show `executionBaseHead`.
- Show provenance and public-sync status before and after.
- Show public-sync remote.
- Show public-sync `git log --oneline -3`.
- Show line/source evidence for matrix, static CI runner, and workflow.
- Show `python scripts/check_provider_receipt_link_integrity.py`.
- Show `python scripts/run_cvf_static_ci_gate.py --json` if feasible.
- If broad static CI cannot run for an unrelated environment reason, record a diagnostic and still run the focused checker.
- Show `git diff --name-status` for public-sync and provenance.
- Show no public-sync commit or push was performed by worker.
- Show `python governance/compat/run_worker_return_fast_gate.py`.
- Show `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 961c56c5e --head HEAD`.

## Acceptance Criteria

1. Public-sync checker script exists and runs without provider/live calls.
2. Checker requires local resolvable receipt links for `CERTIFIED` rows only.
3. Checker passes current Alibaba and DeepSeek certified rows.
4. Checker does not require OpenAI receipt while OpenAI remains `EXPERIMENTAL`.
5. Static CI runner invokes the checker and preserves all existing checks.
6. Worker edits only the two allowed public-sync files and one allowed provenance worker-return path.
7. Public-sync remains uncommitted and unpushed.
8. Required gates pass or block reason is exact and source-backed.

## Review Gate

Reviewer must verify public-sync diff and rerun focused checker evidence before
acceptance. Reviewer must not push public-sync inside R65D closure unless the
operator separately authorizes a public push.

## Closure Checklist

- [x] Dispatch has source verification.
- [x] Dispatch has ADIF disclosure.
- [x] Dispatch has Agent Handoff Contract Control Block.
- [x] Dispatch has Reviewer Closure Conversion.
- [x] Dispatch has Worker Return Packet Shape Contract.
- [x] Dispatch has public/provenance boundary.
- [x] Dispatch has no public commit, public push, provider/live proof, or OpenAI certification uplift claim.

## Return Conditions

Return `COMPLETE_PENDING_REVIEW` if the worker creates the bounded public-sync
checker diff, creates the provenance worker return, records required evidence,
passes required focused checks, and leaves all changes uncommitted.

Return `BLOCKED_WITH_REASON` if public-sync status, remote, source shape,
current matrix contents, checker feasibility, static CI wiring, or scope
authority blocks implementation.

## Return-To-Orchestrator Conditions

Stop and return rather than guessing if public-sync is dirty before work,
remote is not the public CVF repository, the current matrix lacks parseable
provider/status/latest-receipt columns, certified rows currently fail the
intended checker, or a needed action would require provider status edits,
public push, provider/live proof, JSON receipt export, or provenance
runtime/source/test/checker edits.

## Operator Checkpoint

Public push remains operator-owned and separately authorized. R65D authorizes
only checker implementation and evidence return. It does not release the
existing public-sync ahead-two commits or any new checker diff for push.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher creates packet; worker executes no-commit public-sync checker implementation; reviewer/closer owns acceptance and commits |
| phase | pre-dispatch |
| baseHeadFor(phase) | dispatchBaseHead=961c56c5e; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | R65D baseline, R65D work order, two public-sync checker files, and R65D worker return only |
| traceScope(phase, actor) | worker records provenance and public-sync status, command evidence, checker output, static CI output or blocker, no-public-push proof, and claim boundary |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | Do not modify R65A/R65B/R65C artifacts, provider status claim files, receipt content, provenance runtime/source/tests/checkers, or unrelated tranches. |
| nextMoveSurfaces | Worker does not update session/front-door/handoff surfaces; reviewer/closer handles closure routing. |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R65D_PROVIDER_RECEIPT_LINK_INTEGRITY_CHECKER_IMPLEMENTATION_COMPLETION_REVIEW_2026-07-07.md` |
| reviewerOwnedClosurePaths | R65D worker return; public-sync checker diff; optional completion review only if needed; material provenance commit if accepted; session-sync later only if next move changes |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Output Checker Read-Ahead Mandate

Before writing the worker return, read checker source for that file's docType,
path family, and conditional content class.

| Output artifact | Required read-ahead result |
| --- | --- |
| worker return under reviews directory | derive exact review headings, worker-return quality terms, trace labels, Delta block labels, corpus/value/rescan tokens, and no-commit evidence shape before writing |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R65D_PROVIDER_RECEIPT_LINK_INTEGRITY_CHECKER_IMPLEMENTATION_WORKER_RETURN_2026-07-07.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Shape-list rule: when listing required worker-output sections, write section
names without the heading prefix. Reserve actual heading syntax for real
sections so structural checkers do not treat this checklist as the artifact
section body.

Required worker-return terms:
- Purpose
- Scope / Methodology
- Findings / Position
- Risk / Corrective Action
- Claim Boundary
- Agent Operation Trace Block
- Delta Execution Claim Boundary Control Block
- Public Export Disposition
- executionBaseHead
- git status --short

Conditional worker-return terms:
- External Knowledge Intake Routing
- Rescan Intelligence Hardening
- Corpus Completeness And Report Integrity
- Finding-To-Governance Learning Disposition
- Epistemic Process Block
- Machine Closure Package

N/A with reason instruction: every conditional term that does not apply to the
future worker return must appear with an explicit N/A with reason or
NOT_APPLICABLE_WITH_REASON disposition in the worker return.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | section name: ADIF Defect Registry Disclosure; section name: Source Verification Block; section name: Worker Return Packet Shape Contract; section name: Agent Handoff Contract Control Block; section name: Reviewer Closure Conversion; section name: Public Export Disposition; enum: DISPATCH_READY; enum: WORKER_MUST_NOT_COMMIT; required worker-return terms listed one per physical line |
| gateRunPurpose | Confirmation/evidence after checker source and gotcha checklist read-ahead, not first discovery. |
| claimBoundary | Read-ahead covers dispatch artifact shape and worker-return shape contract only. |

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 961c56c5e --head HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 961c56c5e --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git status --short
```

## Public/Provenance Boundary

| Field | Value |
| --- | --- |
| Provenance repo | this workspace is the private provenance repository |
| Public-sync boundary | Worker may edit only the two allowed files in `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync`; worker must confirm `git remote -v`; worker must not commit or push |
| Export disposition | see `## Public Export Disposition` |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | R65C accepted checker recommendation -> R65D bounded checker implementation work order |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py` |
| Owner surface | this work order and paired baseline |
| Disposition | ADAPT as source-verified checker-implementation dispatch |
| Claim boundary | no direct external import; no public push or provider/live proof |

## External Absorption Core

| Field | Value |
| --- | --- |
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | accepted R65C provenance artifacts plus sibling public-sync static CI and matrix source |
| Enumeration command | `rg --files --hidden --no-ignore` for R65C provenance artifacts plus targeted public-sync `git status`, `git remote -v`, static CI source read, matrix line read, and receipt path checks |
| Manifest artifact or inline manifest | inline Source Verification Block and Checker Implementation Requirements |
| Processing ledger artifact or inline ledger | inline Source Verification Block |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | public-sync static CI gate; public-sync provider readiness matrix; R65C decision artifacts |
| Unresolved items | 0 for dispatch; worker blocks if refreshed public-sync evidence contradicts the expected state |
| Completion claim boundary | dispatch work order only; no public-sync commit, public push, live proof, runtime/source/test edit in provenance, or certification uplift |

## Corpus Completeness And Report Integrity

- Corpus task class: COMPARISON
- Corpus root: R65C accepted artifacts plus public-sync static CI/matrix/audit evidence.
- Snapshot time: 2026-07-07 packet authoring.
- Enumeration command: `rg --files --hidden --no-ignore` for provenance artifacts plus targeted public-sync `git status`, `git remote -v`, static CI source read, matrix line read, and receipt path checks.
- Manifest artifact or inline manifest: inline Source Verification Block and Checker Implementation Requirements.
- Manifest hash: N/A with reason: no external corpus import.
- Processing ledger artifact or inline ledger: Source Verification Block.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=R65D_checker_dispatch_scope ledger_terminal=PARTIAL exclusions=public_push_and_provider_live_proof unresolved=0.
- Unresolved files: 0.
- Declared exclusions: public push, public-sync commit, live proof, JSON receipt export, provider status changes, provenance runtime/source/test/checker edits.
- Unreadable or unsupported files: none.
- Aggregation check: R65C decision artifacts and current public-sync static CI/matrix sources are represented.
- Drift check: worker must refresh public-sync status and matrix source before editing.
- Output traceability: worker return must map each implementation change and gate result to command/source evidence.
- Adversarial verification: checker must prove it passes current Alibaba/DeepSeek certified receipt links and does not require OpenAI while `EXPERIMENTAL`.
- Corpus verdict: PARTIAL

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
| --- | --- | --- | --- | --- | --- |
| R65C checker recommendation | recurrent public receipt-link defect class deserves a static guard | CHECKER_CANDIDATE | public-sync static CI gate | implement bounded checker in R65D | no provider/live proof |
| Existing public-sync matrix | certified provider rows carry receipt links | DOCTRINE_ADAPTED | checker behavior contract | require resolvable links only for `CERTIFIED` rows | no provider status change |
| OpenAI experimental row | non-certified rows must not require receipt links | DOCTRINE_ADAPTED | checker behavior contract | preserve experimental/non-certified posture | no certification uplift |
| Public push action | operator-owned release action | NO_PACKAGE_OR_RUNTIME_VALUE | authorization hold | no push in R65D | no push authority |
| Future live re-certification | not required for static link integrity | RUNTIME_CANDIDATE | future live-proof tranche only | no action in R65D | live proof forbidden |
| Direct external pack files | none consumed | REJECT_DIRECT_IMPORT | N/A with reason: no external file import | no action | no package/runtime value |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| R65C checker recommendation | `docs/reviews/CVF_MSEA_R65C_PUBLIC_SYNC_PUBLISH_OR_HOLD_AND_PROVIDER_RECEIPT_LINK_INTEGRITY_CHECKER_DECISION_COMPLETION_REVIEW_2026-07-07.md` | ENRICH_EXISTING | converts recommendation into an authorized implementation packet | dispatch R65D worker |
| Public-sync static CI runner | sibling public-sync `scripts/run_cvf_static_ci_gate.py` | ENRICH_EXISTING | add one link-integrity check to existing static gate | worker implementation only |
| Provider readiness matrix | sibling public-sync `docs/reference/CVF_PROVIDER_LANE_READINESS_MATRIX.md` | CONFIRMED_EXISTING | target document already has certified rows and receipt links | checker reads current shape |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| Foundation Storage Layout Block | N/A with reason: this work order adds a bounded public-sync checker and worker return only; it does not create, split, relocate, refactor, rename, or redesign durable governance foundation files |
| Folder/index impact | none in provenance beyond the allowed worker return |
| Claim boundary | guard-compatibility block only; no foundation storage layout mutation is authorized |

## Work-Order Fulfillment Manifest

The required artifact manifest below binds the worker-owned public-sync diff
and provenance worker return to the R65D work-order scope.

## Required Artifact Manifest

| Artifact | Required worker action |
| --- | --- |
| `scripts/check_provider_receipt_link_integrity.py` | create public-sync static checker, uncommitted |
| `scripts/run_cvf_static_ci_gate.py` | wire checker into public-sync static CI, uncommitted |
| `docs/reviews/CVF_MSEA_R65D_PROVIDER_RECEIPT_LINK_INTEGRITY_CHECKER_IMPLEMENTATION_WORKER_RETURN_2026-07-07.md` | create worker return with gate and diff evidence, uncommitted |

## Planned Artifact Manifest

| Artifact | Required status | Owner |
| --- | --- | --- |
| `scripts/check_provider_receipt_link_integrity.py` | created by worker in public-sync, uncommitted, pending reviewer acceptance | worker |
| `scripts/run_cvf_static_ci_gate.py` | edited by worker in public-sync, uncommitted, pending reviewer acceptance | worker |
| `docs/reviews/CVF_MSEA_R65D_PROVIDER_RECEIPT_LINK_INTEGRITY_CHECKER_IMPLEMENTATION_WORKER_RETURN_2026-07-07.md` | created by worker in provenance, uncommitted, pending reviewer acceptance | worker |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex dispatcher/reviewer |
| Provider or surface | local provenance workspace |
| Session or invocation | MSEA_R65D_PROVIDER_RECEIPT_LINK_INTEGRITY_CHECKER_IMPLEMENTATION dispatch, 2026-07-07 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, governance gates |
| Target paths | `docs/baselines/CVF_GC018_MSEA_R65D_PROVIDER_RECEIPT_LINK_INTEGRITY_CHECKER_IMPLEMENTATION_2026-07-07.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R65D_PROVIDER_RECEIPT_LINK_INTEGRITY_CHECKER_IMPLEMENTATION_2026-07-07.md` |
| Allowed scope source | operator authorized fresh R65D checker packet after accepted R65C checker recommendation |
| Before status evidence | provenance `git status --short --branch` showed clean worktree at `961c56c5e`; public-sync `git status --short --branch` showed clean worktree and `main...origin/main [ahead 2]` |
| After status evidence | R65D dispatch packet and work order authored for no-commit worker execution |
| Diff evidence | `git diff --name-status` |
| Approval boundary | worker may edit two public-sync files and create one provenance worker return only; no push |
| Claim boundary | dispatch only; no public-sync commit/push, provider/live proof, provenance runtime/source/test/checker edit, production claim, or certification uplift |
| Agent type | dispatcher/reviewer |
| Invocation ID | `msea-r65d-provider-receipt-link-integrity-checker-implementation-2026-07-07` |
| Expected manifest | R65D baseline; R65D work order |
| Actual changed set | R65D baseline; R65D work order |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R65D provider receipt-link integrity checker implementation worker dispatch |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, or mandatory-wrapper behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no live runtime receipt is created or consumed |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: dispatch artifact authoring only; worker execution is future bounded static checker work |
| invocationBoundary | Manual local read, dispatch authoring, and governance-gate invocation |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, public remote action, or agent coding control is authorized |
| claimLanguage | Dispatch-ready docs-only checker worker instructions |
| forbiddenExpansion | Do not expand into public push, provider/live proof, runtime/package/Web/MCP/model-router behavior, JSON receipt export, provider status changes, OpenAI certification uplift, or production claims |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: This provenance work order authorizes a no-commit public-sync checker
implementation worker pass but does not itself export, commit, or push public
artifacts.

## Claim Boundary

This work order authorizes only a bounded public-sync static checker
implementation and one provenance worker return. It does not authorize
public-sync commit, public push, provenance runtime/source/test/checker edits,
provider/live proof, JSON receipt export, provider status changes, OpenAI
certification uplift, production readiness, or private provenance publication.
