# CVF Agent Work Order - MSEA-R65B Provider Canary Receipt Evidence Index Integrity

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: MSEA_R65B_PROVIDER_CANARY_RECEIPT_EVIDENCE_INDEX_INTEGRITY

Dispatch base head: ab7248a03

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: Codex reviewer/closer

Worker return path: `docs/reviews/CVF_MSEA_R65B_PROVIDER_CANARY_RECEIPT_EVIDENCE_INDEX_INTEGRITY_WORKER_RETURN_2026-07-07.md`

## Dispatch Prompt Envelope

Role: delegated worker for MSEA_R65B_PROVIDER_CANARY_RECEIPT_EVIDENCE_INDEX_INTEGRITY.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R65B_PROVIDER_CANARY_RECEIPT_EVIDENCE_INDEX_INTEGRITY_2026-07-07.md`

Paired baseline: `docs/baselines/CVF_GC018_MSEA_R65B_PROVIDER_CANARY_RECEIPT_EVIDENCE_INDEX_INTEGRITY_2026-07-07.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START with `git rev-parse --short HEAD`.

Current-time notes: artifact date is 2026-07-07; public-sync local base is R65A commit `fbb782fee4509af99a02c8632ddf8bde3aa449e6`, ahead origin by 1 unless the operator has pushed it separately.

Do-not-misread notes: this work order does not authorize OpenAI certification uplift, live proof, JSON receipt export, public commit, or public push.

Required first actions: read startup files, guard orientation, literal gotchas, this packet, the paired GC-018 baseline, R65A worker return, repository boundary, and every checker source listed in the Checker Source Read-Ahead Block.

Return contract: create the worker return artifact, run required gates, leave changes uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Execute a no-commit public-sync docs-only repair for provider canary receipt
evidence-index integrity. Alibaba and DeepSeek remain `CERTIFIED`, but the
public provider readiness matrix links their rows to public-sync receipt paths
that are absent. The worker must source-verify provenance markdown receipts
and indexes, export only public-safe markdown artifacts if valid, and preserve
OpenAI as `EXPERIMENTAL`.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind public-sync --batch-id MSEA_R65B_PROVIDER_CANARY_RECEIPT_EVIDENCE_INDEX_INTEGRITY --title "MSEA-R65B Provider Canary Receipt Evidence Index Integrity" --date 2026-07-07 --base ab7248a03 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | public-sync plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Replaced R65A OpenAI consistency scope with R65B provider canary receipt evidence-index integrity scope. |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py` |
| docOnlyNewFields | R65B provider canary receipt evidence-index integrity route |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public-push behavior claim. |

## 1. Mission

Restore or repair public evidence link integrity for Alibaba and DeepSeek
certified provider rows. If the cited provenance markdown receipts or indexes
are not public-safe, return `BLOCKED_WITH_REASON` rather than inventing or
rewriting certification evidence.

## 2. Authority Chain

| Authority | Path | Use |
| --- | --- | --- |
| Startup front door | `CVF_SESSION_MEMORY.md` | Current session mode and mandatory startup route |
| Bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | Compact next allowed move |
| Active state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Canonical state |
| Active handoff | `AGENT_HANDOFF_V38_2026-07-06.md` | Current R65/R65B context |
| Guard orientation | `docs/reference/guard_orientation/README.md` | Worker guard map |
| Literal gotchas | `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | Literal-format traps |
| R65A worker return | `docs/reviews/CVF_MSEA_R65A_PUBLIC_OPENAI_CERTIFICATION_CLAIM_CONSISTENCY_OPTION_B_WORKER_RETURN_2026-07-07.md` | Discovered receipt evidence-index gap |
| Repository boundary standard | `docs/reference/CVF_AGENTS_CRITICAL_REPOSITORY_BOUNDARY_2026-06-23.md` | Public/provenance separation |
| Alibaba provenance source | `docs/audits/alibaba-canary/INDEX.md`; `docs/audits/alibaba-canary/CVF_RECEIPT_20260421-072551-422037.md` | Candidate public-safe export source |
| DeepSeek provenance source | `docs/audits/deepseek-canary/INDEX.md`; `docs/audits/deepseek-canary/CVF_RECEIPT_20260421-114125-19515e.md` | Candidate public-safe export source |

## 3. Agent Roles

| Role | Responsibility |
| --- | --- |
| Worker | Source-verify receipt/index artifacts, edit public-sync working tree, create worker return, no commit. |
| Reviewer/closer | Review worker return and public-sync diff, decide commit. |
| Operator | Owns public push and any future live/provider proof authorization. |

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| Intake source | R65A worker-return out-of-scope receipt/evidence-index finding |
| Scope classification | BOUNDED_PUBLIC_SYNC_DOCS_ONLY: allowed scope is certified Alibaba/DeepSeek receipt/index markdown and readiness matrix only |
| Risk sensitivity | public-sync certification evidence integrity; no live/provider proof, secrets, legal workflow, or production readiness |
| Selected role route | MULTI_AGENT_SINGLE_ROLE via worker no-commit execution and reviewer/closer acceptance |
| Route mode | MULTI_AGENT_SINGLE_ROLE |
| role route | MULTI_AGENT_SINGLE_ROLE |
| Intake role | dispatcher routes source-verified public evidence integrity issue to worker role |
| Worker role | no-commit public-sync documentation worker |
| Reviewer role | reviewer/closer validates worker return and public-sync diff |
| Commit owner | reviewer/closer only; worker must not commit |
| Role separation basis | worker performs no-commit edit; reviewer/closer owns material commit and any later public-sync decision |
| Escalation condition | stop and return `BLOCKED_WITH_REASON` if receipt content is not public-safe, source evidence is missing, or OpenAI certification uplift would be required |
| Claim boundary | no direct external import, runtime/source/test/checker edit, provider/live proof, public push, or production claim |

## 4. Scope

Allowed public-sync edit/add paths:

- `docs/reference/CVF_PROVIDER_LANE_READINESS_MATRIX.md`
- `docs/audits/alibaba-canary/INDEX.md`
- `docs/audits/alibaba-canary/CVF_RECEIPT_20260421-072551-422037.md`
- `docs/audits/deepseek-canary/INDEX.md`
- `docs/audits/deepseek-canary/CVF_RECEIPT_20260421-114125-19515e.md`

Allowed provenance worker output:

- `docs/reviews/CVF_MSEA_R65B_PROVIDER_CANARY_RECEIPT_EVIDENCE_INDEX_INTEGRITY_WORKER_RETURN_2026-07-07.md`

Forbidden scope:

- no OpenAI certification uplift;
- no live/provider proof;
- no JSON receipt export;
- no runtime/source/test/checker edit;
- no public-sync commit or push;
- no edits outside the paths above;
- no private/generated MinerU output read.

## Scope / Target / Owner Boundary

The worker owns the no-commit working-tree edit and worker return only. The
reviewer/closer owns acceptance and any material commit. The operator owns any
future public push or live proof authorization.

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly by reading the
failing checker source and matching the literal required shape. Worker should
return to orchestrator only for source contradiction, non-public-safe receipt
content, forbidden-scope need, or missing authority.

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
| `docs/baselines/CVF_GC018_MSEA_R65B_PROVIDER_CANARY_RECEIPT_EVIDENCE_INDEX_INTEGRITY_2026-07-07.md` | READ |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R65B_PROVIDER_CANARY_RECEIPT_EVIDENCE_INDEX_INTEGRITY_2026-07-07.md` | READ |
| `docs/reviews/CVF_MSEA_R65A_PUBLIC_OPENAI_CERTIFICATION_CLAIM_CONSISTENCY_OPTION_B_WORKER_RETURN_2026-07-07.md` | READ |
| `docs/reference/CVF_AGENTS_CRITICAL_REPOSITORY_BOUNDARY_2026-06-23.md` | READ |
| `docs/audits/alibaba-canary/INDEX.md` | SOURCE_VERIFIED |
| `docs/audits/alibaba-canary/CVF_RECEIPT_20260421-072551-422037.md` | SOURCE_VERIFIED |
| `docs/audits/deepseek-canary/INDEX.md` | SOURCE_VERIFIED |
| `docs/audits/deepseek-canary/CVF_RECEIPT_20260421-114125-19515e.md` | SOURCE_VERIFIED |

## 6. Pre-Flight Checks

1. Capture provenance `executionBaseHead` with `git rev-parse --short HEAD`.
2. Run provenance `git status --short --branch`.
3. Run public-sync `git remote -v`.
4. Run public-sync `git status --short --branch`.
5. Confirm public-sync is at or after local R65A commit `fbb782fee4509af99a02c8632ddf8bde3aa449e6`.
6. Verify public-sync `docs/audits` lacks the canary folders before repair.
7. Verify provenance candidate receipt/index markdown content is public-safe before copying.

## 6A. Source-Fidelity Pass

### Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Public-sync Alibaba receipt link is missing target | PUBLIC_SYNC_EVIDENCE | sibling public-sync `docs/reference/CVF_PROVIDER_LANE_READINESS_MATRIX.md` | line 27 | Alibaba receipt link | provider lane readiness matrix | ACCEPT |
| Public-sync DeepSeek receipt link is missing target | PUBLIC_SYNC_EVIDENCE | sibling public-sync `docs/reference/CVF_PROVIDER_LANE_READINESS_MATRIX.md` | line 28 | DeepSeek receipt link | provider lane readiness matrix | ACCEPT |
| Alibaba source receipt exists in provenance | PROVENANCE_SOURCE | `docs/audits/alibaba-canary/CVF_RECEIPT_20260421-072551-422037.md` | file path exists | CVF_RECEIPT_20260421-072551-422037.md | provenance audit receipt | ACCEPT |
| DeepSeek source receipt exists in provenance | PROVENANCE_SOURCE | `docs/audits/deepseek-canary/CVF_RECEIPT_20260421-114125-19515e.md` | file path exists | CVF_RECEIPT_20260421-114125-19515e.md | provenance audit receipt | ACCEPT |
| Public-facing edits must go through sibling public-sync clone | REPOSITORY_BOUNDARY | `docs/reference/CVF_AGENTS_CRITICAL_REPOSITORY_BOUNDARY_2026-06-23.md` | `## Critical Repository Boundary - 2026-05-09` | public-sync clone | repository boundary standard | ACCEPT |

### Current Public-Sync Evidence Snapshot

| Public-sync item | Read-only evidence | Required action |
| --- | --- | --- |
| `docs/reference/CVF_PROVIDER_LANE_READINESS_MATRIX.md:27` | Alibaba row links missing public-sync receipt path | Export public-safe receipt/index or block. |
| `docs/reference/CVF_PROVIDER_LANE_READINESS_MATRIX.md:28` | DeepSeek row links missing public-sync receipt path | Export public-safe receipt/index or block. |
| `docs/reference/CVF_PROVIDER_LANE_READINESS_MATRIX.md:29` | OpenAI row remains `EXPERIMENTAL` and says receipt not present | Preserve; no certification uplift. |
| public-sync `docs/audits` | no canary provider directories | Add only allowed markdown receipt/index artifacts if public-safe. |

## 6B. Roadmap-To-Work-Order Trace Matrix

| Source requirement | Worker instruction |
| --- | --- |
| R65A follow-up finding | Repair certified provider receipt/index link integrity. |
| Public/provenance boundary | Mutate sibling public-sync working tree only; do not commit or push. |
| OpenAI Option B | Preserve OpenAI experimental/non-certified posture. |

## Write Ownership

| Path | Worker action |
| --- | --- |
| `docs/reviews/CVF_MSEA_R65B_PROVIDER_CANARY_RECEIPT_EVIDENCE_INDEX_INTEGRITY_WORKER_RETURN_2026-07-07.md` | create provenance worker return, uncommitted |
| allowed sibling public-sync files | add/edit only if public-safe and needed, uncommitted |

## Execution Plan

| Step | Action | Evidence |
| --- | --- | --- |
| 1 | Capture provenance and public-sync status | status and remote output |
| 2 | Source-verify provenance markdown receipts/indexes | file reads and content safety notes |
| 3 | Export public-safe markdown artifacts or block | public-sync diff |
| 4 | Verify public-sync links resolve | `Test-Path` for linked paths |
| 5 | Create worker return | worker-return path exists |
| 6 | Run gates | worker-return fast gate and pre-implementation autorun |

## Evidence Requirements

- Show `executionBaseHead`.
- Show provenance and public-sync status before/after.
- Show public-sync remote.
- Show source verification for each exported markdown file.
- Show public-sync `git diff --name-status`.
- Show `Test-Path` evidence that matrix links resolve after edits.
- Show `python governance/compat/run_worker_return_fast_gate.py`.
- Show `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base ab7248a03 --head HEAD`.
- Show no public-sync commit or push was performed by worker.

## Acceptance Criteria

1. Alibaba and DeepSeek readiness matrix evidence links resolve in public-sync, or worker returns blocked with exact source-backed reason.
2. Exported receipt/index artifacts are markdown only and public-safe.
3. OpenAI remains `EXPERIMENTAL`; no OpenAI certification claim is added.
4. No JSON receipts are exported.
5. Worker edits only allowed paths and creates only the worker-return output in provenance.
6. Required gates pass or block reason is exact and source-backed.
7. Worker performs no commit and no push.

## Review Gate

Reviewer must verify public-sync link resolution and public-safe markdown
content before acceptance. Reviewer must not accept an OpenAI certification
uplift under this tranche.

## Closure Checklist

- [x] Dispatch has source verification.
- [x] Dispatch has ADIF disclosure.
- [x] Dispatch has Agent Handoff Contract Control Block.
- [x] Dispatch has Reviewer Closure Conversion.
- [x] Dispatch has Worker Return Packet Shape Contract.
- [x] Dispatch has public/provenance boundary.
- [x] Dispatch has no public commit or push claim.

## Return Conditions

Return `COMPLETE_PENDING_REVIEW` if the worker exports or repairs only allowed
paths, records required evidence, passes required gates, and leaves changes
uncommitted.

Return `BLOCKED_WITH_REASON` if receipt/index content is not public-safe,
source evidence is missing, OpenAI certification uplift is required, or any
necessary path lies outside allowed scope.

## Return-To-Orchestrator Conditions

Stop and return rather than guessing if any candidate receipt includes private
secrets, non-public provider tokens, private generated output, or other
material not suitable for public-sync.

## Operator Checkpoint

No live proof or public push is authorized. Operator checkpoint is needed only
if the worker determines certified status cannot be supported without live
provider rerun or broader receipt export.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher creates packet; worker executes no-commit public-sync edit; reviewer/closer owns acceptance and commits |
| phase | pre-dispatch |
| baseHeadFor(phase) | dispatchBaseHead=ab7248a03; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | R65B baseline, R65B work order, worker return, and allowed sibling public-sync files only |
| traceScope(phase, actor) | worker records provenance and public-sync status, command evidence, public-sync diff, no-commit proof, and claim boundary |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | Do not modify R65A artifacts or unrelated tranches; public-sync starts from local R65A commit. |
| nextMoveSurfaces | Worker does not update session/front-door/handoff surfaces; reviewer/closer handles closure routing. |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R65B_PROVIDER_CANARY_RECEIPT_EVIDENCE_INDEX_INTEGRITY_COMPLETION_REVIEW_2026-07-07.md` |
| reviewerOwnedClosurePaths | R65B worker return; R65B completion review; public-sync diff review; material provenance commit if accepted; session-sync later only if next move changes |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Output Checker Read-Ahead Mandate

Before writing the worker return, read checker source for that file's docType,
path family, and conditional content class.

| Output artifact | Required read-ahead result |
| --- | --- |
| worker return under reviews directory | derive exact review headings, worker-return quality terms, trace labels, Delta block labels, corpus/value/rescan tokens, and no-commit evidence shape before writing |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | R65A worker-return finding -> R65B public-sync receipt evidence-index integrity work order |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py` |
| Owner surface | this work order and paired baseline |
| Disposition | ADAPT as source-verified public-sync follow-up work order |
| Claim boundary | no direct external source import; provenance receipt artifacts are CVF-owned source evidence |

## External Absorption Core

| Field | Value |
| --- | --- |
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | R65A worker-return finding plus CVF provenance receipt artifacts |
| Enumeration command | targeted `rg --files --hidden --no-ignore` for cited receipt/index paths and public-sync audit folder listing |
| Manifest artifact or inline manifest | inline Current Public-Sync Evidence Snapshot table |
| Processing ledger artifact or inline ledger | inline Source Verification Block |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | `docs/audits/alibaba-canary/INDEX.md`; `docs/audits/deepseek-canary/INDEX.md`; public-sync provider readiness matrix |
| Unresolved items | 0 for dispatch; worker blocks if receipt content is not public-safe |
| Completion claim boundary | dispatch work order only; no public-sync commit/push, live proof, or certification change |

## Corpus Completeness And Report Integrity

- Corpus task class: COMPARISON
- Corpus root: provider readiness matrix plus cited Alibaba and DeepSeek provenance receipt/index markdown files.
- Snapshot time: 2026-07-07 packet authoring.
- Enumeration command: targeted `rg --files --hidden --no-ignore` and public-sync `docs/audits` listing.
- Manifest artifact or inline manifest: inline Current Public-Sync Evidence Snapshot table.
- Manifest hash: N/A with reason: no external corpus import.
- Processing ledger artifact or inline ledger: Source Verification Block.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=provider_receipt_integrity_scope ledger_terminal=PARTIAL exclusions=JSON_receipts_and_OpenAI_certification unresolved=0.
- Unresolved files: 0.
- Declared exclusions: JSON receipts, OpenAI certification uplift, live proof, runtime/source/test/checker files.
- Unreadable or unsupported files: none.
- Aggregation check: Alibaba and DeepSeek linked receipt targets are represented.
- Drift check: worker must refresh public-sync status before editing.
- Output traceability: receipt links map to exact provenance receipt files.
- Adversarial verification: worker must verify exported public links resolve after edits.
- Corpus verdict: PARTIAL

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
| --- | --- | --- | --- | --- | --- |
| Alibaba cited canary receipt | public matrix link target absent in public-sync but present in provenance | DOCTRINE_ADAPTED | public-sync audit receipt/index markdown | worker exports public-safe markdown or blocks | no runtime/live proof |
| DeepSeek cited canary receipt | public matrix link target absent in public-sync but present in provenance | DOCTRINE_ADAPTED | public-sync audit receipt/index markdown | worker exports public-safe markdown or blocks | no runtime/live proof |
| OpenAI canary evidence | OpenAI remains experimental after R65A | NO_PACKAGE_OR_RUNTIME_VALUE | provider readiness matrix | preserve experimental/no certification | no provider certification uplift |
| Future receipt-link checker | possible automation candidate | CHECKER_CANDIDATE | future checker tranche only | no action in R65B | checker implementation forbidden |
| Future public evidence package | possible reusable public-evidence package candidate | PACKAGE_CANDIDATE | future package tranche only | no action in R65B | no package authority |
| Future live re-certification | possible runtime/provider candidate | RUNTIME_CANDIDATE | future live-proof tranche only | no action in R65B | live proof forbidden |
| Direct external pack files | none consumed | REJECT_DIRECT_IMPORT | N/A with reason: no external file import | no action | no package/runtime value |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| Alibaba receipt/index | `docs/audits/alibaba-canary/INDEX.md`; `docs/audits/alibaba-canary/CVF_RECEIPT_20260421-072551-422037.md` | ENRICH_EXISTING | public-sync missing linked public evidence | export if public-safe |
| DeepSeek receipt/index | `docs/audits/deepseek-canary/INDEX.md`; `docs/audits/deepseek-canary/CVF_RECEIPT_20260421-114125-19515e.md` | ENRICH_EXISTING | public-sync missing linked public evidence | export if public-safe |
| OpenAI receipt/index | R65A worker return and public-sync matrix | CONFIRMED_EXISTING | intentionally experimental and not certified | no certification export |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| Foundation Storage Layout Block | N/A with reason: this work order adds public-sync audit evidence files only; it does not create, split, relocate, refactor, rename, or redesign durable governance foundation files |
| Folder/index impact | public-sync audit folders may be added under allowed scope; no provenance foundation storage layout change |
| Claim boundary | guard-compatibility block only; no foundation storage layout mutation is authorized |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/reviews/CVF_MSEA_R65B_PROVIDER_CANARY_RECEIPT_EVIDENCE_INDEX_INTEGRITY_WORKER_RETURN_2026-07-07.md` | create uncommitted worker return with gate and diff evidence |
| sibling public-sync allowed files | add/edit only within allowed path list and leave uncommitted |

## Required Artifact Manifest

| Artifact | Required status | Owner |
| --- | --- | --- |
| `docs/reviews/CVF_MSEA_R65B_PROVIDER_CANARY_RECEIPT_EVIDENCE_INDEX_INTEGRITY_WORKER_RETURN_2026-07-07.md` | created by worker, uncommitted, pending reviewer acceptance | worker |
| sibling public-sync audit markdown/index files | added only if public-safe, uncommitted | worker |
| sibling public-sync provider readiness matrix | edited only if needed for link integrity, uncommitted | worker |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R65B_PROVIDER_CANARY_RECEIPT_EVIDENCE_INDEX_INTEGRITY_WORKER_RETURN_2026-07-07.md`
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
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base ab7248a03 --head HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base ab7248a03 --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git status --short
```

## Public/Provenance Boundary

| Field | Value |
| --- | --- |
| Provenance repo | this workspace is the private provenance repository |
| Public-sync boundary | Worker must mutate only `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync`; worker must confirm `git remote -v`; worker must not push |
| Export disposition | see `## Public Export Disposition` |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex dispatcher/reviewer |
| Provider or surface | local provenance workspace |
| Session or invocation | MSEA_R65B_PROVIDER_CANARY_RECEIPT_EVIDENCE_INDEX_INTEGRITY dispatch, 2026-07-07 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, governance gates |
| Target paths | `docs/baselines/CVF_GC018_MSEA_R65B_PROVIDER_CANARY_RECEIPT_EVIDENCE_INDEX_INTEGRITY_2026-07-07.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R65B_PROVIDER_CANARY_RECEIPT_EVIDENCE_INDEX_INTEGRITY_2026-07-07.md` |
| Allowed scope source | operator asked to handle R65A and move to the next tranche |
| Before status evidence | R65A material commit `6ff1a7287`; provenance worktree clean before R65B dispatch files were authored; public-sync local commit `fbb782fee4509af99a02c8632ddf8bde3aa449e6`; public-sync worktree clean with main ahead origin by 1 |
| After status evidence | R65B dispatch packet and work order authored for no-commit worker execution |
| Diff evidence | `git diff --name-status` |
| Approval boundary | worker may edit allowed public-sync files only and must not commit or push |
| Claim boundary | dispatch only; no public-sync execution, runtime/provider/live proof, source/test/checker edit, production claim, or push |
| Agent type | dispatcher/reviewer |
| Invocation ID | `msea_r65b_provider_canary_receipt_evidence_index_integrity-2026-07-07` |
| Expected manifest | R65B baseline; R65B work order |
| Actual changed set | R65B baseline; R65B work order |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R65B provider canary receipt evidence-index integrity worker dispatch |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, or mandatory-wrapper behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no live runtime receipt is created or consumed |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: dispatch artifact authoring only; worker execution is future no-commit public-sync work |
| invocationBoundary | Manual local read, dispatch authoring, and governance-gate invocation |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized |
| claimLanguage | Dispatch-ready docs-only public-sync worker instructions |
| forbiddenExpansion | Do not expand into runtime/provider/live/public-push/package/Web/MCP/model-router behavior, JSON receipt export, OpenAI certification uplift, or production claims |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: This provenance work order authorizes a no-commit public-sync worker
pass but does not itself export, commit, or push public artifacts.

## Claim Boundary

This work order authorizes only a no-commit public-sync documentation/evidence
repair in the sibling public-sync clone and a provenance worker return. It
does not authorize public commit, public push, runtime behavior, provider/live
proof, source/test/checker edits, JSON receipt export, OpenAI certification
uplift, production readiness, or private provenance publication.
