# CVF Agent Work Order - Qwen Turbo Deprecation Migration

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work-order

Date: 2026-08-15

Batch ID: QTDM-01

## Dispatch Prompt Envelope

Role: migration worker. Independent reviewer/closer is later.
Canonical packet: docs/work_orders/CVF_AGENT_WORK_ORDER_QWEN_TURBO_DEPRECATION_MIGRATION_2026-08-15.md
Commit mode: WORKER_MUST_NOT_COMMIT
executionBaseHead: WORKER_MUST_CAPTURE_AT_START
Current-time notes: operator directed Qwen-Turbo removal after blocked T6 and environment repair; canonical replacement is the qwen-flash alias with snapshot qwen-flash-2025-07-28.
Do-not-misread notes: this packet does not authorize a live provider call, T6 retry, npm/npx repair, blind replacement, session-state or handoff mutation, or any production/public/deployment action.
Required first actions: capture HEAD and status; read startup surfaces, guard orientation, literal gotchas, the paired baseline, this packet, and every checker source in the Checker Source Read-Ahead Block; enumerate the exact active files with git grep before editing any file.
Return contract: edit only the Active-Surface Migration Manifest, preserve every Historical-Evidence Exclusion Manifest path, leave staging empty and HEAD unchanged, and return COMPLETE_PENDING_INDEPENDENT_REVIEW or BLOCKED_WITH_REASON.

dispatchBaseHead: `fc11bf46c2a46b09bfc1affefce0960bbbcbde72`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `NOT_EXECUTED_YET`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Execute the identifier-level Qwen-Turbo deprecation migration: remove
`qwen-turbo` from every active surface and replace it with `qwen-flash`,
record `qwen-flash-2025-07-28` as the official replacement snapshot, and
leave every historical receipt, archive, evidence JSON, handoff, and prior
session-state entry unchanged. No live provider call occurs.

completionReviewPath: `docs/reviews/CVF_QWEN_TURBO_DEPRECATION_MIGRATION_COMPLETION_2026-08-15.md`
reviewerOwnedClosurePaths: optional completion review; proposed machine guard
checker promotion; GC-051 registry source entry and aggregate; session
continuity separately. The worker owns none of these.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id QTDM-01 --title "Qwen Turbo Deprecation Migration" --date 2026-08-15 --base fc11bf46c2a46b09bfc1affefce0960bbbcbde72 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| scaffoldedSections | dispatch, source verification, agent handoff contract, reviewer closure conversion, worker return shape, trace, delta block, public disposition, claim boundary |
| manualEditsAfterScaffold | bound migration semantics, replacement contract, active/historical manifests, machine guard proposal, GC-051 obligations |
| checkerReadAheadConfirmation | checker sources listed in the paired baseline read-ahead block were read before authoring |
| docOnlyNewFields | `Replacement Contract`; `Active-Surface Migration Manifest`; `Historical-Evidence Exclusion Manifest`; no runtime schema field introduced |
| claimBoundary | dispatch provenance only; no live, runtime, provider, public-sync, or production behavior is implemented |

## Roadmap-To-Work-Order Trace Matrix

| Requirement | Work order section | Output artifact or field | Verification | State |
|---|---|---|---|---|
| remove qwen-turbo from active surfaces | Active-Surface Migration Manifest; Acceptance Criteria | edited active files | git grep absence | MAPPED |
| preserve historical evidence | Historical-Evidence Exclusion Manifest | unchanged historical files | git diff limited to active manifest | MAPPED |
| qwen-flash replacement | Replacement Contract | qwen-flash identifier | grep for qwen-flash presence | MAPPED |
| no live call | Diagnostic And Retry Protocol; Operator Checkpoint | zero provider calls | no provider command | MAPPED |
| machine guard | Machine Guard Proposal | proposed checker | reviewer-owned | MAPPED |

## Required First Reads

1. `AGENTS.md`
2. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
3. `docs/reference/guard_orientation/README.md`
4. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
5. `AGENT_HANDOFF_V59_2026-08-11.md`
6. `scripts/evaluate_cvf_provider_lane_certification.py`
7. `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`
8. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai-providers.ts`
9. `docs/baselines/CVF_GC018_QWEN_TURBO_DEPRECATION_MIGRATION_2026-08-15.md`

## Pre-Flight Checks

- confirm HEAD contains the independently accepted QTDM-01 dispatch packet,
  capture that exact HEAD as `executionBaseHead`, and confirm staging is empty;
- confirm both output paths are absent;
- enumerate the exact active files with `git grep -l -i qwen-turbo` and record the list before editing;
- classify every enumerated file as active or historical and record the classification;
- do not start if any unrelated dirty path exists;
- record exact commands and results in the worker return.

## Authority Chain

| Authority item | Evidence | Disposition |
|---|---|---|
| operator instruction | operator deprecation directive 2026-08-15 | ACCEPT |
| active session state | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | ACCEPT |
| active handoff | `AGENT_HANDOFF_V59_2026-08-11.md` | ACCEPT |
| GC-018 requirement | paired QTDM-01 baseline | ACCEPT |

Authority boundary: this work order authorizes only the identifier migration
above. It does not authorize live calls, T6 retry, environment repair, session
mutation, public sync, or production action.

## Agent Roles

| Role | Responsibility |
|---|---|
| Operator | directs the deprecation migration |
| Dispatcher | authors baseline and work order; runs pre-dispatch gate; commits nothing in this turn |
| Worker | edits only the Active-Surface Migration Manifest without commit |
| Reviewer/closer | verifies manifest exactness and historical preservation, projects guard/registry, commits material then session sync |
| External reviewer | N/A with reason: no external reviewer input is used |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | migrate deprecated qwen-turbo to qwen-flash across active surfaces |
| scope classification | SOURCE_MIGRATION_NO_COMMIT |
| primary task class | identifier-level deprecation migration |
| risk sensitivity | high: blind replacement or historical mutation would corrupt evidence |
| selected role route | SINGLE_AGENT_SINGLE_ROLE |
| orchestration requirement | no-commit worker followed by independent reviewer/closer |
| role separation basis | worker migration cannot close its own tranche |
| escalation condition | ambiguity in active-vs-historical classification, or a live-call demand |

## Worker Autonomy / No-Question Rule

The worker proceeds without operator confirmation for non-destructive
identifier substitution inside the Active-Surface Migration Manifest. A file
whose active-vs-historical classification is ambiguous must be classified
historical (preserve) and listed in the worker return, not edited. Escalation
is reserved for a forbidden-scope need, a live-call demand, or an ambiguity
that cannot be resolved by preserving the file.

## Allowed Scope

Worker may edit exactly the files named in the Active-Surface Migration
Manifest (Classes A through E), and create exactly:

1. `docs/reviews/CVF_QWEN_TURBO_DEPRECATION_MIGRATION_WORKER_RETURN_2026-08-15.md`

Forbidden: every other path; any Historical-Evidence Exclusion Manifest path;
session state, active handoff, front door, `.env.local`, generated aggregates;
staging or commit; live provider call; T6 retry; npm/npx repair; deployment;
public sync; production action.

For Class B, family globs are summaries and do not grant wildcard write scope.
The worker must capture exactly 72 dispatch-base Qwen-Turbo test/support hits
using the baseline command, add only the named provisional SOT3 test, and treat
that resulting 73-path list as the Class B write manifest. A mismatch blocks.

## Write Ownership

Worker owns only the manifest edits plus the single worker return. Reviewer
owns the optional completion review, material commit, and separate
session/handoff sync. Guard implementation and GC-051 projection require a
later separately governed checker tranche.

## Replacement Contract

- Canonical runtime alias: `qwen-flash`.
- Official replacement snapshot: `qwen-flash-2025-07-28`.
- `qwen3.6-flash` must not be introduced as canonical authority; where it is a
  factual versioned snapshot in an existing ledger it may remain as a snapshot.
- Provider lane is retained; DeepSeek and OpenAI lanes are untouched.
- Never edit a historical receipt, archive, evidence JSON, handoff archive, or
  prior session-state entry.

## Diagnostic And Retry Protocol

- No live provider call is permitted in this tranche.
- On any ambiguity in classification, classify the file historical and record
  it in the worker return instead of editing.
- No blind replacement. The worker edits only after the exact active-file
  enumeration is recorded.

## Acceptance Commands

After migration, the worker must run and record:

```powershell
git grep -n -i "qwen-turbo" -- "EXTENSIONS" "scripts" "governance/compat" "README.md" "ARCHITECTURE.md" "docs/CVF_CORE_KNOWLEDGE_BASE.md" "docs/CVF_INCREMENTAL_TEST_LOG.md" "docs/reference" "docs/guides/CVF_DEMO_SCRIPT_2026-04-21.md" ':!*archive*' ':!*evidence*' ':!*.jsonl'
```

Expected: zero matches in active surfaces.

```powershell
git grep -n -i "qwen3\.6-flash" -- "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.sot3-activation.alibaba.live.test.ts"
```

Expected: zero matches; this provisional blocked-attempt choice must become
the canonical `qwen-flash` alias before any T6 retry.

```powershell
git grep -l -i "qwen-turbo" -- "docs/evidence" "docs/audits/alibaba-canary" "docs/reviews/evidence" "CVF_SESSION/handoffs/archive" "docs/*/archive" | find /c /v ""
```

Expected: unchanged historical count (greater than zero; preserved as facts).

## Machine Guard Proposal

The worker records a proposal for
`governance/compat/check_qwen_turbo_active_reference.py` plus its test that
fails pre-implementation when `qwen-turbo` appears in an active surface and
ignores archive, evidence, receipt, and prior-session-state paths. The worker
does not implement the checker; QTDM-01 reviewer/closer also must not promote
it. Promotion requires a later separately governed checker tranche.

## GC-051 Registry Obligations

The migration itself adds no corpus source path. If the reviewer promotes the
proposed machine guard and its test, those must be registered in the corpus
scan registry with a source entry and regenerated aggregate in the same
material batch per GC-051.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| provider cert evaluator pins alibaba to qwen-turbo | VALUE_SET | `scripts/evaluate_cvf_provider_lane_certification.py` | `PROVIDERS` | `qwen-turbo` | provider certification evaluator | ACCEPT |
| capability registry lists qwen-turbo | VALUE_SET | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | `PROVIDER_CAPABILITY_REGISTRY` | `PROVIDER_CAPABILITY_REGISTRY` | model gateway capability registry | ACCEPT |
| provider registry enforces routable admission | LITERAL_INVARIANT | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | `ProviderRegistry` class | `assertAllowed`; `listRoutable` | model gateway provider registry | ACCEPT |
| web provider defaults to qwen-turbo | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai-providers.ts` | `AlibabaDashScopeWebProvider` constructor | `config.model || 'qwen-turbo'` | web AI provider adapter | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | `Source Verification Block`; `Checker Source Read-Ahead Block`; `Agent Handoff Contract Control Block`; `Dual Agent Surface Matrix`; `Delta Execution Claim Boundary Control Block`; `Public Export Disposition`; `Reviewer Closure Conversion`; `Worker Autonomy / No-Question Rule`; `WORKER_MUST_NOT_COMMIT`; `Replacement Contract` |
| gateRunPurpose | confirmation and evidence after reading checker source ahead of writing |
| claimBoundary | structural read-ahead does not prove migration correctness |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, surfaceSelector=`qwen`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class dispatch --role dispatcher --lifecycle-phase pre-dispatch --surface-selector qwen --risk-ceiling HIGH --max-results 20 --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | no added ADIF constraint; no-live-call and preserve-historical boundaries remain mandatory |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Path existence for the two QTDM-01 dispatch artifact paths | both proposed baseline and work order paths were absent before authoring | ABSENT_BEFORE_AUTHORING |
| Bounded collision search | `git grep -l qwen-turbo` enumerated 427 files and `git grep -l qwen-flash` 6 files; no existing QTDM-01 packet | EXISTING_OWNER_SURFACES_REUSED |
| Collision decision | existing provider/registry/session surfaces remain their owners; this packet adds baseline and work order only | REUSE_AS_SOURCE_NOT_DUPLICATE_OWNER |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | active runtime/test/script/reference surfaces | identifier migration only; no semantic/runtime change, no live call, no session mutation | source-verified manifests and future worker return | none introduced | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no external CLI/MCP surface | no invocation, launch, credential, mutation, or public authority | T5 decision remains deferred | future fresh packet required | `DEFERRED_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: no external artifact or recommendation is ingested |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired QTDM-01 baseline and this work order |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | only CVF-governed repository sources plus cited official lifecycle pages support this dispatch |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Requirement |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | one no-commit migration worker, then independent reviewer/closer |
| phase | worker execution pending |
| baseHeadFor(phase) | dispatchBaseHead=`fc11bf46c2a46b09bfc1affefce0960bbbcbde72`; executionBaseHead=`WORKER_MUST_CAPTURE_AT_START`; closureBaseHead=`REVIEWER_TO_SET` |
| executionBaseHead | worker records exact current HEAD before edits |
| dirtyPathPolicy | zero unrelated dirty paths |
| changedSetScope(phase) | manifest edits plus one worker return; no historical or session path |
| traceScope(phase, actor) | worker records enumeration, edits, acceptance commands, diff, status, and gates |
| operationReceiptWriteOrder | worker writes return last after edits stabilize |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; independent reviewer owns commits |
| crossBatchIsolation | no unrelated changed path may be touched or absorbed |
| nextMoveSurfaces | reviewer-owned guard/registry projection and material commit, then separate session sync |
| commitBoundary | worker MUST NOT stage or commit |

## Reviewer Closure Conversion

| Field | Requirement |
|---|---|
| completionReviewPath | `docs/reviews/CVF_QWEN_TURBO_DEPRECATION_MIGRATION_COMPLETION_2026-08-15.md` (optional; prefer repairing evidence in the worker return) |
| reviewerOwnedClosurePaths | optional completion review; material commit; session continuity separately; no guard/checker or GC-051 registry mutation |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |
| publicRule | no EXPORTED disposition without public-sync remote, commit, and artifact path evidence |

## Worker Output Checker Read-Ahead Mandate

Before writing the worker return, read checker source for the `docs/reviews`
docType, path family, and conditional content class, deriving the review
headings, worker-return quality terms, trace labels, delta boundary labels,
corpus/value/rescan tokens, and no-commit evidence shape.

## Work-Order Fulfillment Manifest

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
|---|---|---|
| Every exact active path authorized by Classes A-E in the paired baseline | Yes | replace deprecated active model authority only |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.sot3-activation.alibaba.live.test.ts` | Yes | replace provisional blocked-attempt `qwen3.6-flash` with canonical `qwen-flash` |
| `docs/reviews/CVF_QWEN_TURBO_DEPRECATION_MIGRATION_WORKER_RETURN_2026-08-15.md` | Yes | exact enumeration, preservation, validation, and no-commit evidence |

## Forbidden Path Manifest

| Path | Reason |
|---|---|
| Historical-Evidence Exclusion Manifest paths in the paired baseline | immutable historical facts |
| `governance/compat/check_qwen_turbo_active_reference.py` and its test | later checker tranche only |
| session/front-door/handoff/generated-state paths | session-sync steward only after material acceptance |

| Artifact | Required worker action |
|---|---|
| active-surface edits | substitute `qwen-turbo` with `qwen-flash` in Classes A-E; record `qwen-flash-2025-07-28` snapshot |
| worker return | record enumeration, edits, acceptance command results, preserved files, gate outcomes, no-commit confirmation |
| proposed machine guard | record the proposal text only; do not implement |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_QWEN_TURBO_DEPRECATION_MIGRATION_WORKER_RETURN_2026-08-15.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Acceptance Criteria

- `qwen-turbo` is absent from every Active-Surface Migration Manifest path;
- the provisional SOT3 route test contains no `qwen3.6-flash` occurrence;
- every Historical-Evidence Exclusion Manifest path is byte-for-byte unchanged;
- `qwen-flash` is present as the replacement and `qwen-flash-2025-07-28` is
  recorded as the official snapshot;
- no `qwen3.6-flash` canonical authority was introduced;
- no live provider call, no T6 retry, no npm/npx repair occurred;
- the worker return passes the fast gate;
- staging empty; HEAD unchanged; worker did not commit.

## Verification Commands

```powershell
git rev-parse HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base fc11bf46c2a46b09bfc1affefce0960bbbcbde72 --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git diff --name-only
git diff --cached --name-only
git rev-parse HEAD
```

No live provider, credential, public-sync, deployment, or production command is
permitted.

## Execution Plan

1. capture execution base and clean state;
2. enumerate the exact active files with `git grep -l -i qwen-turbo`;
3. classify each active file against the manifest and preserve historical files;
4. substitute `qwen-turbo` with `qwen-flash` in active files only;
5. run the acceptance commands and record results;
6. write the worker return;
7. run fast gates and repair only the owned paths;
8. confirm staging empty and HEAD unchanged.

## Evidence Requirements

- exact active-file enumeration before edits;
- per-file classification (active-edited vs historical-preserved);
- acceptance command output;
- actual git status, changed set, staging state, and HEAD;
- no self-reported clean claim that omits the untracked worker return and edits.

## Review Gate

The independent reviewer must challenge manifest exactness, historical
preservation, replacement-contract compliance, absence of live calls, and the
exact changed set. Gate success alone is not semantic acceptance.

## Independent Review Conversion

| Review item | Finding and repair | Disposition |
|---|---|---|
| Official replacement authority | original packet inferred replacement from catalog absence/operator direction; repaired to cite Alibaba lifecycle and Qwen-Flash pages directly | ACCEPTED_AFTER_REPAIR |
| Class B manifest exactness | original family globs were broader than write authority; repaired with a dispatch-base enumeration command, exact count 72, and mismatch-block rule | ACCEPTED_AFTER_REPAIR |
| Blocked T6 provisional model | original Qwen-Turbo-only search missed the SOT3 test already changed to `qwen3.6-flash`; added it as the sole 73rd Class B path and required migration to `qwen-flash` | ACCEPTED_AFTER_REPAIR |
| Guard ownership | original packet contradicted separate-tranche staging by assigning guard promotion to the migration reviewer; repaired to forbid guard/GC-051 mutation in QTDM-01 | ACCEPTED_AFTER_REPAIR |
| Required artifact manifest | original work order omitted the checker-required exact heading/table | ACCEPTED_AFTER_REPAIR |
| Independent gates | pre-dispatch 76/76 PASS; reviewer-fast 63/63 PASS; Class B dispatch-base count 72 | PASS |

Independent review disposition: `DISPATCH_READY_AFTER_INDEPENDENT_REPAIR`.

## Closure Checklist

- [ ] active manifest files only were edited
- [ ] historical evidence paths unchanged
- [ ] qwen-flash replacement and snapshot recorded
- [ ] no qwen3.6-flash canonical authority introduced
- [ ] acceptance commands return zero active qwen-turbo
- [ ] worker-return fast gate passes
- [ ] staging empty and HEAD unchanged
- [ ] worker did not commit

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_INDEPENDENT_REVIEW` only after the edits and required
gates pass. Return `BLOCKED_WITH_REASON` when a classification contradiction
or a forbidden-scope need prevents completion.

## Operator Checkpoint

No live provider call, T6 retry, npm/npx repair, session/handoff mutation,
public sync, deployment, or production action opens from this packet. Any later
action requires the independent reviewer conversion and a fresh governed
packet where applicable.

## Worker Return Required Evidence

The worker return must state executionBaseHead, final HEAD, exact changed-set
status, staging state, per-class edit counts, preserved-file count, acceptance
command results, gate outcomes, and no-commit confirmation.

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| Storage standard | `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` |
| Planned durable reference folder | N/A with reason: no durable governance foundation reference folder is created, split, relocated, or refactored by this tranche |
| Planned front door/index | N/A with reason: no foundation front door or index is created or changed |
| Date policy | N/A with reason: no dated foundation file is introduced |
| Owner surface | existing runtime/test/script/reference surfaces and the worker return |
| Claim boundary | identifier migration only; no foundation storage or index mutation |

## MCP/CLI Adapter Boundary

| Field | Binding |
|---|---|
| Adapter scope | none; T5 implementation remains deferred |
| External-agent surface | no CLI/MCP invocation or launch |
| Public surface | no public artifact, remote, commit, push, or deploy |
| No-runtime-overclaim | no runtime, provider, credential, mutation, interception, or live claim |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher; independent reviewer/closer repair and acceptance |
| Provider or surface | local repository tools |
| Session or invocation | QTDM-01 dispatch authoring and independent review, 2026-08-15 |
| Working directory | repository root |
| Command or tool surface | PowerShell, `git grep`, repository Python guards, and apply-patch editing |
| Target paths | paired QTDM-01 baseline and paired QTDM-01 work order |
| Allowed scope source | operator deprecation directive and active handoff next-move |
| Before status evidence | clean worktree at HEAD `fc11bf46c2a46b09bfc1affefce0960bbbcbde72` |
| After status evidence | exact two-path unstaged dispatch authoring set before validation |
| Diff evidence | `git diff --name-status` |
| Approval boundary | migration dispatch only; no live call, source mutation, or production action |
| Claim boundary | packet authoring and dispatch gates only |
| Agent type | dispatcher author followed by independent reviewer/closer |
| Invocation ID | `qtdm-01-dispatch-2026-08-15` |
| Expected manifest | QTDM-01 baseline; QTDM-01 work order |
| Actual changed set | QTDM-01 baseline; QTDM-01 work order |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | repo-local Qwen-Turbo deprecation migration dispatch |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, interception, or migration completion is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created by this dispatch |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime, provider, or live action occurs during dispatch authoring |
| invocationBoundary | local read-only source verification and governed document authoring only |
| interceptionBoundary | no direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized |
| claimLanguage | migration authorization only, pending independent review |
| forbiddenExpansion | no live provider call, no T6 retry, no npm/npx repair, no blind replacement, no session mutation, no public export, no production |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance migration dispatch with no public-sync authorization.

## Claim Boundary

This work order authorizes exactly one identifier-level Qwen-Turbo deprecation
migration with its worker return. It does not implement or prove the
migration, does not perform any live provider call, does not authorize T6
retry or environment repair, and does not claim provider compatibility,
production readiness, or cross-runtime determinism. Historical receipts,
archives, evidence JSON, handoffs, and prior session-state entries remain
immutable. The worker commits nothing.
