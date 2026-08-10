# CVF Active Continuity Read-Cost T1 Work Order

Memory class: ACTIVE_WORK_ORDER

Status: DISPATCH_READY

Date: 2026-08-10

Risk ceiling: R2

Commit mode: WORKER_MUST_NOT_COMMIT

Execution base HEAD: `64afcf84739de5b85ec05e2816bedcda30b7a972`

## Dispatch Prompt Envelope

```text
Role: worker/implementer; an independent reviewer/closer owns acceptance.
Canonical packet: docs/work_orders/CVF_ACTIVE_CONTINUITY_READ_COST_T1_WORK_ORDER_2026-08-10.md.
Commit mode: WORKER_MUST_NOT_COMMIT.
executionBaseHead: capture current git rev-parse HEAD before the first edit.
Current-time notes: no live key, provider, network, downstream, deployment,
  public-sync, push, or Core compaction is authorized.
Do-not-misread notes: T1 creates rules and enforcement only; T2 compacts Core
  and T3 migrates the downstream workspace.
Required first actions: read the bootstrap, this Work Order, its authorization
  review, the seven source paths, and checker sources; then verify hashes,
  HEAD, staged zero, and migration debt facts.
Return contract: COMPLETE_PENDING_INDEPENDENT_REVIEW or BLOCKED with
  executionBaseHead, exact changed paths, tests/gates, file facts,
  HEAD/staged state, no-commit, and zero-call evidence.
```

Roadmap:
`docs/roadmaps/CVF_ACTIVE_CONTINUITY_READ_COST_REDUCTION_ROADMAP_2026-08-10.md`

## Purpose

Implement T1 of the active continuity read-cost roadmap: establish a compact
startup standard, enforce bounded active surfaces with exact migration debt,
and distribute progressive-read instructions to Core and future downstream
workspaces.

T1 does not compact current Core continuity files and does not touch any
downstream repository. T2 owns Core compaction. T3 owns the downstream
application after its active worker/reviewer checkpoint stops.

## Authority Chain

1. The operator instruction dated 2026-08-10 authorizes the continuity
   read-cost roadmap and bounded T1 preparation.
2. The roadmap defines tranche boundaries and leaves T2/T3 parked.
3. This Work Order is implementation authority after independent review PASS.
4. The worker returns uncommitted evidence to an independent reviewer/closer.

## Agent Roles

- Dispatcher authors and repairs the dispatch packet.
- Independent reviewer authorizes implementation.
- Separate worker implements without committing.
- Independent reviewer/closer accepts or returns changes.

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| Intake source | operator report that long active continuity history delays worker startup |
| Route | `MULTI_AGENT_MULTI_ROLE` |
| canonical route mode | `MULTI_AGENT_MULTI_ROLE` |
| scope classification | R2 protected governance-maintenance implementation |
| selected role route | dispatcher authors; independent reviewer authorizes; separate worker implements; independent reviewer/closer accepts |
| Runtime/source modification | only the exact seven governance paths |
| External evidence intake | not authorized |
| Disposition | no-commit T1 implementation after independent authorization PASS |
| escalation condition | exact-seven expansion, continuity compaction, downstream mutation, secret/provider/network/public/deploy effect, destructive action, or claim-boundary change |

## Scope

Allowed scope is exactly the seven paths in `## 4. Exact Changed Set`.
Forbidden scope is every other path and every external effect named in the
claim boundary.

## Required First Reads

1. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
2. this Work Order
3. `docs/reviews/CVF_ACTIVE_CONTINUITY_READ_COST_T1_WORK_ORDER_AUTHORIZATION_REVIEW_2026-08-10.md`
4. the seven authorized source/output paths
5. the checker sources in `## Checker Source Read-Ahead Block`

Full active-state/history reads are not required unless a current fact is
missing or contradictory.

## Preflight Checks

Before editing, verify current HEAD, staged-zero state, authority hashes,
exact-seven containment, and both migration-debt source hashes/line/byte
counts. A mismatch returns `BLOCKED`.

## Write Ownership

The worker owns edits only to the exact seven paths and must not commit. The
independent reviewer/closer owns semantic acceptance, completion review, and
any later commit or session-sync action.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order coverage | Evidence | Status |
|---|---|---|---|
| T1 canonical standard | sections 3 and 5.1 | new reference file plus source review | MAPPED |
| T1 machine enforcement | sections 5.4 and 5.5 | checker diff and adversarial tests | MAPPED |
| Core progressive startup | section 5.2 | `AGENTS.md` diff | MAPPED |
| future downstream progressive startup | section 5.3 | downstream template diff with non-blocking bootstrap fallback | MAPPED |
| current debt cannot grow | section 5.4 exact registry contract | current-byte recomputation and negative tests | MAPPED |
| no T2/T3 execution | sections 1, 4, 9 and 15 | exact-seven diff and claim boundary | MAPPED |
| no history deletion | sections 5.1 and 6 | source diff and reviewer inspection | MAPPED |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact: the roadmap measurements are planning evidence only.

priorVerificationAnchor: `64afcf84739de5b85ec05e2816bedcda30b7a972`.

freshRecomputeRequired: true

unicodePathHandling: use literal paths and UTF-8-safe readers; authored files
remain ASCII unless an existing protocol literal requires otherwise.

extractedTextAuthority: repository bytes and checker output only.

## Worker Autonomy / No-Question Rule

Inside exact-seven scope, repair source, test, packet-shape, file-size,
encoding and local-gate failures and rerun the relevant checks without asking
the operator. Ask only when the required change exceeds exact-seven, changes
risk/external effect/commit ownership, consumes secrets or quota, deletes
history, compacts current continuity, mutates downstream, or contradicts this
Work Order.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The worker return must contain Status, Purpose, Scope / Methodology, Findings /
Position, Risk / Corrective Action, Claim Boundary, Checker Source Read-Ahead
Block, Agent Operation Trace Block, Delta Execution Claim Boundary Control
Block, Public Export Disposition, executionBaseHead, git status, exact changed
files, tests, gates, migration facts, file sizes, no-commit and zero-call
accounting. Conditional gate sections must be present with `N/A with reason`
when they do not apply.

## 2. Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Verification class | Disposition |
|---|---|---|---|---|---|---|
| Core already exposes a compact bootstrap read model | `AGENTS.md` | lines 3-16 | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | Core agent startup router | EXISTS | ACCEPT |
| Core startup still requires session memory and full state resolution | `AGENTS.md` | lines 34-38 | `Mandatory Startup Acknowledgment` | Core agent startup router | RUNTIME_BEHAVIOR | ACCEPT |
| Downstream startup requires every manifest document and full continuity sequence | `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md` | lines 20-54 | `First-Request Protocol` | generated downstream agent instructions | RUNTIME_BEHAVIOR | ACCEPT |
| Downstream rehydration requires rereading the whole sequence | `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md` | lines 72-92 | `Mandatory Continuity Rehydration` | generated downstream agent instructions | RUNTIME_BEHAVIOR | ACCEPT |
| Bootstrap byte ceiling already exists at 4096 bytes | `governance/compat/generate_active_session_state.py` | lines 23-37 | `CVF_ACTIVE_SESSION_BOOTSTRAP_READ_MODEL_MAX_BYTES` | bootstrap generator contract | LITERAL_INVARIANT | ACCEPT |
| Active session checker already validates bootstrap, state, handoff and required reads | `governance/compat/check_active_session_state.py` | lines 354-450 | `_classify` | active session compatibility gate | RUNTIME_BEHAVIOR | ACCEPT |
| Required-first-read count has no ceiling | `governance/compat/check_active_session_state.py` | lines 415-420 | `required_first_reads` | active session compatibility gate | RUNTIME_BEHAVIOR | ACCEPT |
| Existing active front door and handoff size policy is generic only | `governance/compat/check_governed_file_size.py` | lines 169-210 | `_classify` | governed file-size gate | RUNTIME_BEHAVIOR | ACCEPT |
| Existing session bootstrap guard owns startup continuity behavior | `governance/toolkit/05_OPERATION/CVF_SESSION_GOVERNANCE_BOOTSTRAP_GUARD.md` | complete guard | `CVF Session Governance Bootstrap Guard` | operational guard owner | EXISTS | ACCEPT |
| Active session checker tests use isolated repository fixtures | `governance/compat/test_check_active_session_state.py` | `class ActiveSessionStateTests` definition | `ActiveSessionStateTests` | checker proof owner | RUNTIME_BEHAVIOR | ACCEPT |

No source item is blocked. The new standard and migration registry are listed
as new outputs, not claimed as existing source.

## 3. New Output Fields And Files

| New item | Owner | Purpose |
|---|---|---|
| `docs/reference/CVF_ACTIVE_CONTINUITY_READ_BUDGET_STANDARD_2026-08-10.md` | canonical reference | define progressive disclosure, budgets, rotation, migration and downstream safety |
| `governance/compat/CVF_ACTIVE_CONTINUITY_READ_BUDGET_MIGRATION.json` | active session checker | exact-hash temporary debt for current Core front door and handoff only |

No new runtime provider field, API, route, state schema, handoff schema, or
external interface is introduced.

## 4. Exact Changed Set

The worker may edit exactly these seven paths:

1. `AGENTS.md`
2. `docs/reference/CVF_ACTIVE_CONTINUITY_READ_BUDGET_STANDARD_2026-08-10.md`
3. `governance/toolkit/05_OPERATION/CVF_SESSION_GOVERNANCE_BOOTSTRAP_GUARD.md`
4. `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md`
5. `governance/compat/CVF_ACTIVE_CONTINUITY_READ_BUDGET_MIGRATION.json`
6. `governance/compat/check_active_session_state.py`
7. `governance/compat/test_check_active_session_state.py`

The list contains seven paths. No eighth path is authorized.

The roadmap is dispatcher-owned and must remain byte-identical during worker
execution. Current session memory, bootstrap, state sources/aggregate, active
handoff, review queue, README, knowledge base, hooks, command catalogs, public
sync, downstream projects, and every other path remain read-only.

## 5. Required Behavior

### 5.1 Canonical standard

The new standard must bind:

- bootstrap-first startup;
- progressive reads rather than full historical reads;
- current-only front doors and handoffs;
- archive pointers instead of copied closed history;
- authority refresh on accepted Work Order amendments;
- exact line and byte budgets;
- exact-hash migration debt with no growth;
- downstream no-compaction-while-worker-active safety; and
- T2/T3 migration responsibilities.

Use these limits:

| Surface | Maximum lines | Maximum bytes |
|---|---:|---:|
| bootstrap read model | 60 | 4,096 |
| active front door | 120 | 20,480 |
| active handoff | 220 | 32,768 |
| default required-first-read list | 12 paths | N/A |

The full active-state aggregate is not a default startup read. T1 warns when
it exceeds 131,072 bytes but does not fail on that aggregate size because T2
owns the schema/content migration.

### 5.2 Core startup rule

Update `AGENTS.md` so a new/resumed agent:

1. reads the bootstrap first;
2. reads the compact front door and active handoff;
3. reads only the current authority paths selected by those surfaces; and
4. performs targeted state/history lookup only when a current fact is missing,
   contradictory, or explicitly required.

Do not require a full read of the aggregate or historical handoffs by default.
Keep the existing startup acknowledgment fields and provider-memory boundary.

### 5.3 Downstream startup rule

Update the downstream template with the same progressive sequence. When a
bootstrap exists, read it first. When a current generated project does not yet
have a bootstrap, extract only the current mode, active handoff, next allowed
move, parked checkpoint and current-authority fields from the state file. Mark
`BOOTSTRAP_MIGRATION_PENDING` as a non-blocking migration note; do not read the
whole state/history and do not make the generated workspace unusable.

Manifest `requiredDocs` and state history become targeted authority inputs,
not unconditional full reads. Current task authority remains mandatory.
Provisioning a downstream bootstrap is deferred to T3 or a separately
authorized generator tranche.

This template edit changes future/generated instructions only. Do not mutate
an existing downstream project in T1.

### 5.4 Checker enforcement

Enhance the existing active-session checker; do not create a parallel checker.

It must:

- enforce bootstrap line and byte budgets;
- enforce front-door and active-handoff line/byte budgets;
- reject more than 12 `requiredFirstReads` entries;
- reject router text that makes the full state aggregate or historical
  handoffs an unconditional default read;
- verify the standard and migration registry exist;
- accept an oversize front door or handoff only when an enabled migration row
  matches path, SHA-256, line count, byte count, approved maxima and mandatory
  T2 removal action exactly;
- reject migration-row drift, growth, missing fields, duplicate paths, unknown
  paths, expired rows, or a row for a currently compliant surface;
- emit an advisory for the full state aggregate above 131,072 bytes; and
- retain every existing session, generated-state, handoff, queue and freshness
  check.

The current migration registry may contain exactly two debt rows:

- `CVF_SESSION_MEMORY.md`;
- `AGENT_HANDOFF_V57_2026-08-10.md`.

The registry contract is exact and closed:

```json
{
  "schemaVersion": "1.0",
  "status": "ACTIVE_MIGRATION_DEBT",
  "expiresOn": "2026-08-17",
  "removalAction": "REMOVE_ROW_IN_T2_AFTER_SURFACE_COMPACTION",
  "entries": [
    {
      "path": "CVF_SESSION_MEMORY.md",
      "sha256": "55ce8aece6f3aa2c017a7316e589fac4ec4b6fc6870441d809413a51f06d62c1",
      "lineCount": 522,
      "byteCount": 97464,
      "approvedMaxLines": 522,
      "approvedMaxBytes": 97464,
      "targetMaxLines": 120,
      "targetMaxBytes": 20480,
      "enabled": true
    },
    {
      "path": "AGENT_HANDOFF_V57_2026-08-10.md",
      "sha256": "9e7ca04d323cb731a9609f0d78f511efbfb5d43d0919bbee53868102d267faad",
      "lineCount": 922,
      "byteCount": 47102,
      "approvedMaxLines": 922,
      "approvedMaxBytes": 47102,
      "targetMaxLines": 220,
      "targetMaxBytes": 32768,
      "enabled": true
    }
  ]
}
```

Top-level fields and entry fields must match the example exactly. Types are
strict JSON types. `expiresOn` is an ISO `YYYY-MM-DD` UTC date and must not be
earlier than the current UTC date. The status and removal-action literals are
exact. Unknown or missing fields, duplicate paths, disabled rows, other paths,
hash/line/byte drift, approved maxima below current facts, target maxima that
do not equal the canonical budgets, expired rows, or rows for compliant files
fail closed.

The worker must independently recompute both source hashes, lines and bytes
before editing. Any mismatch with the pinned facts is `BLOCKED` rather than an
authority to refresh debt.

### 5.5 Adversarial proof

Extend the existing test module with isolated fixtures proving:

1. all compliant budgets pass;
2. each line budget fails at N+1;
3. each byte budget fails at N+1 even when line count passes;
4. 13 required reads fail and 12 pass;
5. exact migration debt passes;
6. hash, line, byte, max, expiry, path and duplicate-row drift each fail;
7. a compliant surface cannot retain a migration waiver;
8. full-state oversize is advisory, not T1 enforcement failure;
9. unconditional full-state/history startup wording fails; and
10. progressive targeted-lookup wording passes.

No test may edit the real repository continuity files.

## Execution Plan

1. Verify HEAD, clean staging, roadmap/Work Order hashes and the two exact debt
   source facts.
2. Author the standard and exact migration registry.
3. Update the operational guard, Core router and downstream template.
4. Extend the existing checker without creating a parallel hook or checker.
5. Add isolated adversarial tests and run focused checks.
6. Run the remaining local verification and return an uncommitted exact-seven
   packet.

## Evidence Requirements

Return command-backed evidence for executionBaseHead, exact changed set,
focused/full tests, every required gate, debt facts, file sizes, `git diff
--check`, staged zero, no commit, and zero external calls.

## 6. Core Guard Self-Protection Authorization

Protected paths:

- `AGENTS.md`
- `governance/toolkit/05_OPERATION/CVF_SESSION_GOVERNANCE_BOOTSTRAP_GUARD.md`
- `governance/compat/check_active_session_state.py`
- `governance/compat/test_check_active_session_state.py`

Operator authorization: on 2026-08-10 the operator reported that agents lose
time reading long session/state/handoff history and requested refactoring plus
new rules that keep irrelevant history out of latest active surfaces.

Authorized guard-maintenance scope: only progressive startup routing and active-continuity
read-budget enforcement described by this Work Order.

Rollback boundary: revert only the exact seven T1 paths if rejected. Do not
rewrite or delete historical evidence, state sources, archived handoffs,
provider rules, runtime code, public history, or downstream project state.

## Verification Commands

Run:

1. focused active-session checker tests;
2. the active-session checker in enforce mode;
3. governed file-size and text-encoding checks;
4. guard self-protection and dispatch-scope checks;
5. `python governance/compat/run_worker_return_fast_gate.py` against the
   checker test target and returned packet;
6. full sanitized non-live Python suite if the focused and local gates pass;
7. git diff check, exact-seven changed-set, secret scan and staged-zero audit.

No doctor, provider, network, live, browser, Docker, PostgreSQL, deployment,
public-sync, push, or downstream mutation is authorized.

## Acceptance Criteria

- AC-01: bootstrap-first progressive startup is canonical in Core and the
  downstream template.
- AC-02: full state/history is no longer an unconditional default agent read.
- AC-03: all four read budgets are machine-enforced.
- AC-04: existing oversized Core surfaces are exact-hash migration debt and
  cannot grow or drift.
- AC-05: current aggregate oversize is visible but does not block T1.
- AC-06: all adversarial fixtures pass without touching real continuity files.
- AC-07: every pre-existing active-session invariant remains enforced.
- AC-08: exactly seven paths change; no session/downstream/runtime path changes.
- AC-09: all external-effect counts remain zero.

## Review Gate

An independent reviewer must inspect semantics and adversarial coverage, rerun
the bounded gates, verify exact-seven/no-eighth containment, and issue PASS or
CHANGES_REQUIRED. Green tests alone are not acceptance.

## Closure Checklist

- [x] Roadmap requirement trace is present.
- [x] Source Verification Block is complete.
- [x] Exact changed set and forbidden scope are explicit.
- [x] Worker return shape and no-commit rule are explicit.
- [x] Reviewer/closer conversion is explicit.
- [x] External-effect and claim boundaries are explicit.

Worker implementation evidence remains unresolved until reviewer acceptance;
this checklist covers dispatch completeness only.

## 9. Worker Return

Return exactly `COMPLETE_PENDING_INDEPENDENT_REVIEW` or `BLOCKED`.

Include execution HEAD, exact-seven name-status and hashes, AC-01 through AC-09
matrix, first-fail/final test evidence, migration rows, file sizes, staged-zero,
no-commit, zero-call accounting and claim boundary.

Stop after return. The worker must not stage, commit, push, compact Core, edit
downstream, or begin T2/T3.

## Return-To-Orchestrator Conditions

Return `BLOCKED` for authority/hash drift, exact-seven insufficiency, required
scope expansion, an in-scope gate failure that remains unresolved, secret/quota need,
destructive action, or conflict with the no-external-effect boundary.

## Execution Authority Waiver

operator.checkpoint.waiver: exact-seven execution is already authorized.
Fresh operator authority is mandatory for scope expansion, T2/T3 entry,
provider or live work, deployment, public sync, push, deletion, or commit-mode
change.

## 10. Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Binding |
|---|---|
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher, independent work-order reviewer, separate no-commit worker, independent build reviewer/closer |
| phase | `T1_WORK_ORDER`, `T1_BUILD`, `T1_REVIEW`, `T1_CLOSURE_OR_BLOCK` |
| baseHeadFor(phase) | `dispatchBaseHead=64afcf84739de5b85ec05e2816bedcda30b7a972`; worker records `executionBaseHead`; reviewer records `closureBaseHead` before closure |
| changedSetScope(phase) | exact seven T1 paths only |
| traceScope(phase, actor) | dispatcher trace covers roadmap and Work Order; worker trace covers exact-seven implementation; reviewer trace covers review/closure only |
| commitOwner(phase) | reviewer/closer after semantic acceptance |
| crossBatchIsolation | Core compaction T2 and downstream migration T3 remain separate |
| nextMoveSurfaces | unchanged during worker execution |

Designated closer: `INDEPENDENT_BUILD_REVIEWER_CLOSER`.

## 11. Reviewer Closure Conversion

- completionReviewPath:
  `docs/reviews/CVF_ACTIVE_CONTINUITY_READ_COST_T1_COMPLETION_REVIEW_2026-08-10.md`
- reviewerOwnedClosurePaths: completion review and later commit only after PASS
- worker commit disposition: `WORKER_MUST_NOT_COMMIT`
- session-sync disposition: not part of T1 worker scope

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_active_session_state.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_foundation_storage_layout.py`; `governance/compat/check_dispatch_scaffold_provenance.py` |
| literalTokensReviewed | `## Dispatch Prompt Envelope`, `## Source Verification Block`, `## Core Guard Self-Protection Authorization`, `## Agent Handoff Contract Control Block`, `## Reviewer Closure Conversion`, `## Checker Source Read-Ahead Block`, `## Delta Execution Claim Boundary Control Block`, `## Foundation Storage Layout Block`, `## Scaffold Provenance Block` |
| gateRunPurpose | confirmation and evidence after source-verified authoring, not first discovery of required artifact shape |
| claimBoundary | read-ahead evidence covers this T1 dispatch packet and its exact-seven implementation contract only |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --help` |
| generatedProfile | `WORK_ORDER` |
| generatedSkeletonStatus | `NOT_USED_WITH_REASON` |
| manualEditsAfterScaffold | packet predated this recheck; dispatcher repaired the required carrier blocks directly |
| checkerReadAheadConfirmation | checker constants were read before repair and gates are confirmation evidence |
| docOnlyNewFields | none; this block records dispatch provenance only |
| claimBoundary | no claim that the helper generated this Work Order |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | one canonical reference at the established `docs/reference/` root plus existing guard/checker/template paths |
| Storage decision | reuse established roots; no new family directory, duplicate standard, or parallel checker |
| Existing aggregate impact | none |
| Generated state impact | none during T1 worker execution |
| Durable governance boundary | T1 defines read-budget rules and enforcement only; T2/T3 own continuity migration |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | repository-local startup instructions and compatibility checking |
| claimDisposition | N/A with reason: no universal execution-control claim is made |
| receiptEvidence | N/A with reason: T1 creates no runtime receipt |
| actionEvidence | N/A with reason: T1 evidence is local source, test, and gate output |
| invocationBoundary | local worker shell and Python test/checker invocation |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, or network interception claim |
| claimLanguage | bounded progressive-read routing and repository-local fail-closed checks |
| forbiddenExpansion | runtime/provider control, universal agent control, deployment, public sync, push, or production-readiness claim |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defectIds:

- `ADIF-0001`
- `ADIF-0002`
- `ADIF-0014`
- `ADIF-0015`
- `ADIF-0020`
- `ADIF-0021`
- `ADIF-0028`
- `ADIF-0029`
- `ADIF-0033`
- `ADIF-0044`

## 14. Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | Core/downstream startup instruction and local checker | repository-local R2 governance-maintenance only | roadmap, source verification, focused and local gates | filesystem continuity reads only | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | generated downstream AGENTS instructions | no CLI/MCP runtime or external invocation added | template text and checker evidence only | no runtime adapter | `N/A_WITH_REASON` |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher / work-order author role |
| Provider or surface | local CVF Core workspace |
| Session or invocation | active-continuity read-cost T1 dispatch authoring, 2026-08-10 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | repository reads, source search, hash/size probes, patch authoring, independent review |
| Target paths | roadmap and this Work Order only |
| Allowed scope source | operator instruction on 2026-08-10 to refactor long active continuity reads and keep irrelevant history out of latest surfaces |
| Before status evidence | clean worktree at base HEAD `64afcf84739de5b85ec05e2816bedcda30b7a972` before dispatch authoring |
| After status evidence | exactly the untracked roadmap and Work Order; staged paths zero |
| Diff evidence | `git status --short` and per-file SHA-256 before independent authorization |
| Approval boundary | dispatch artifacts only; exact-seven implementation follows only after review PASS |
| Claim boundary | no T1 implementation, continuity compaction, downstream mutation, provider/network/live/public/deploy action, commit or push |
| Agent type | dispatcher |
| Invocation ID | `active-continuity-read-cost-t1-dispatch-2026-08-10` |
| Expected manifest | roadmap plus this Work Order |
| Actual changed set | roadmap plus this Work Order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: dispatch authoring deletes or renames nothing |

## 15. Claim Boundary

T1 reduces continuity startup read cost and establishes enforceable migration
rules. It does not itself compact current Core/downstream state, change runtime
governance, call a provider, deploy, publish, complete LPCI1 Web, or develop the
shift-operations project.
