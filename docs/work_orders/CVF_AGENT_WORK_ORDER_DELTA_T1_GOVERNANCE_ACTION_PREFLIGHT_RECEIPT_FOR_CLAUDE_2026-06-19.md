# CVF Agent Work Order - Delta-T1 Governance Action Preflight Receipt For Claude

Memory class: FULL_RECORD

Status: DISPATCH_READY_FOR_CLAUDE

Date: 2026-06-19

docType: work_order

Batch ID: DELTA-T1

Owner: Codex dispatcher; Claude worker; Codex reviewer/closer

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `087f7678`

executionBaseHead: `087f7678`

closureBaseHead: `087f7678`

rawMemoryReleased: false

## Dispatch Prompt Envelope

Role: Claude worker/implementer. Codex is dispatcher, reviewer, closer, and
commit owner.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_DELTA_T1_GOVERNANCE_ACTION_PREFLIGHT_RECEIPT_FOR_CLAUDE_2026-06-19.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

Base: executionBaseHead `087f7678`; at worker start, record the actual current
HEAD in the worker-return packet and keep HEAD unchanged.

Current-time notes: MCP to Model Gateway Composition Proof is closed bounded at
material commit `befad4a9`. Delta-T1 is authorized only
for a deterministic MCP governance-action preflight receipt and durable local
audit. No live key or provider call is authorized.

Do-not-misread notes: `cvf_check_governance_action` already exists as a Gamma
advisory classifier and must remain compatible. Add the distinct Delta tool
`cvf_preflight_governance_action`. Prompt-level mandatory language is not proof
of IDE, shell, git, filesystem, Claude, or Codex interception.

Required first actions: read `CVF_SESSION_MEMORY.md`, resolve
`CVF_SESSION/ACTIVE_SESSION_STATE.json`, read the active handoff, this work
order, matching GC-018, `MCP-GW-001`, the external knowledge absorption chain
map, and the source files in the Source Verification Block; then run the
pre-implementation autorun gate before source edits.

Return contract: return `COMPLETE_PENDING_REVIEW` with changed paths, actual
worker-start HEAD, focused/full test and build results, durable-audit readback,
guard results, `git diff --check`, `git status --short`, `git diff --name-status`,
and confirmation that HEAD is unchanged; otherwise return `BLOCKED_WITH_REASON`.

## Purpose

Implement Delta-T1 as one modular MCP preflight tool that evaluates planned
`EDIT`, `RUN`, and `COMMIT` actions through the existing guard engine, persists
a secret-safe audit entry, and returns a correlated receipt only after durable
persistence succeeds.

## Scope / Target / Owner Boundary

Target: MCP package source, focused tests, prompt guidance, and one worker-return
packet.

Owner boundary: the existing Gamma classifier, Model Gateway, CVF Web,
workspace state, provider runtime, and public-sync remain outside worker write
ownership.

Risk ceiling: R2 local deterministic implementation. No network, credentials,
quota, public action, destructive action, or irreversible action.

## Intake Role Routing Decision

intake summary: operator requested a work order so Claude can implement the next
authorized Delta Execution Control step.

scope classification: bounded MCP Local Workspace Runtime component.

risk sensitivity: R2 because the tranche adds durable local audit writes; live,
secret, public, and broad interception paths are forbidden.

selected role route: `MULTI_AGENT_MULTI_ROLE`

role separation basis: Codex authors and commits dispatch; Claude implements
without commit; Codex reviews, closes, commits accepted material, and syncs
session continuity separately.

escalation condition: any need for wrapper/proxy, shell/IDE/git/filesystem
interception, provider/live proof, secret/quota use, public-sync, workspace
state mutation, or broader enforcement claim.

## Agent Roles

| Role | Actor | Responsibility |
| --- | --- | --- |
| Dispatcher | Codex | Author, source-verify, gate, and commit dispatch packet |
| Worker | Claude | Implement allowed source/tests and return uncommitted evidence |
| Reviewer / closer | Codex | Inspect worker diff, repair only allowed-scope defects, run closure gates, commit accepted material |
| Session-sync actor | Codex | Update protected continuity in a separate commit following the accepted material commit |
| Operator | Human | Authorize any forbidden scope expansion |

## Authority Chain

| Level | Artifact | Status |
| --- | --- | --- |
| Operator authorization | current request on 2026-06-19 | ACCEPTED for work-order creation and Claude dispatch |
| Active session | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Composition Proof closed; Delta requires fresh GC-018 and source-verified work order |
| Active handoff | `AGENT_HANDOFF_V19_2026-06-15.md` | Delta is next allowed candidate |
| Legacy absorption | `MCP-GW-001` in `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` | source-backed Delta controls |
| Chain authority | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | runtime/MCP work routes through fresh GC-018/work order/source verification |
| Composition prerequisite | `docs/reviews/CVF_MCP_MODEL_GATEWAY_COMPOSITION_PROOF_COMPLETION_2026-06-19.md` | `CLOSED_PASS_BOUNDED` |
| GC-018 | `docs/baselines/CVF_GC018_DELTA_T1_GOVERNANCE_ACTION_PREFLIGHT_RECEIPT_2026-06-19.md` | DISPATCH_READY |
| Roadmap | N/A with reason: Delta-T1 is released by active-session next-move authority and `MCP-GW-001`, not a numbered roadmap tranche | N/A with reason |

## Agent Handoff Contract Control Block

| Field | Disposition |
| --- | --- |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | Codex dispatcher; Claude worker; Codex reviewer/closer and session-sync actor |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE, SESSION_SYNC |
| baseHeadFor(phase) | dispatch=`087f7678`; worker records actual execution HEAD at start; Codex records closure base after accepting return |
| changedSetScope(phase) | dispatch baseline/work order; worker named MCP source/tests/return packet; reviewer completion/evidence; protected continuity only in session-sync |
| traceScope(phase, actor) | each actor records its own phase-local command and changed-set evidence |
| commitOwner(phase) | Codex for dispatch, accepted material closure, and session-sync; Claude must not commit |
| crossBatchIsolation | one Delta-T1 batch in a clean worktree; no concurrent batch mixing |
| nextMoveSurfaces | Codex updates session state/front door/active handoff following an accepted material commit or blocked disposition |
| closerDesignation | Codex is the designated closer |

## Reviewer Closure Conversion

completionReviewPath:
`docs/reviews/CVF_DELTA_T1_GOVERNANCE_ACTION_PREFLIGHT_RECEIPT_COMPLETION_2026-06-19.md`

reviewerOwnedClosurePaths:

- `docs/reviews/CVF_DELTA_T1_GOVERNANCE_ACTION_PREFLIGHT_RECEIPT_COMPLETION_2026-06-19.md`
- `docs/reviews/evidence/delta-t1-governance-action-preflight-receipt-2026-06-19.json`
- this work order and matching GC-018 for final status/evidence conversion;
- protected session continuity files only in a separate session-sync commit.

Claude creates only the worker-return packet named in Write Ownership.
Reviewer-owned closure artifacts, protected continuity, and commits remain
outside Claude's write set.

## Single-Agent Multi-Role Control Block

| Field | Disposition |
| --- | --- |
| Applicability | N/A with reason: dispatch uses multiple agents |
| Role separation ledger | Codex dispatch -> Claude implementation -> Codex independent review/closure -> Codex session-sync |
| Evidence basis independent of memory | repo-visible source, diff, test, build, and gate evidence |
| Self-review boundary | no self-review route is used; Codex independently reviews Claude's uncommitted return |
| Gate sequence | pre-dispatch -> pre-implementation -> worker-return fast gate -> pre-closure -> pre-push |
| Escalation conditions | operator checkpoint required for any forbidden scope or claim expansion |

## Workspace Two-Layer Control Block

| Field | Disposition |
| --- | --- |
| targetLayer | `CVF_LOCAL_WORKSPACE_RUNTIME` |
| operatorSurface | N/A with reason: no CVF Web UI or operator dashboard change |
| agentExecutionSurface | MCP governance-action preflight call path only |
| sourceOfTruth | CVF guard types/engine, persistence port, GC-018, and this work order |
| mutationBoundary | MCP source/test plus user-local audit file at runtime |
| receiptBoundary | receipt correlates to durable guard audit `requestId` |
| forbiddenConflationCheck | preflight invocation does not prove external action interception or execution |

## Agent Workspace Design Control Block

| Field | Disposition |
| --- | --- |
| Workspace purpose | Add a bounded agent-facing pre-action governance receipt to Local Workspace Runtime |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` |
| Front door | `docs/reference/agent_workspace/README.md` |
| Storage class | MCP runtime source/test; user-local audit JSON outside repo; dated execution reviews |
| Handoff fields | Agent Handoff Contract Control Block above |
| State ownership | no generated workspace state, lane item, queue, inbox, or dashboard mutation |
| Guard owner | existing guard engine plus handoff/workspace/AOT/autorun machine checks |
| Build boundary | preflight component only; no Web UI, queue, provider proof, public-sync, registry edits, or broad wrapper/proxy build |

## Runtime Expansion Control Block

| Field | Disposition |
| --- | --- |
| runtimeMode | `RUNTIME_IMPLEMENTATION_REQUESTED` |
| contractSource | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` |
| frontDoor | `docs/reference/agent_workspace/README.md` |
| stateSourceOfTruth | existing MCP guard runtime; no workspace state mutation |
| queueBoundary | N/A with reason: no queue, scheduler, worker, or daemon |
| operatorViewBoundary | N/A with reason: no Web UI |
| providerBoundary | no provider or Model Gateway call |
| publicBoundary | private provenance only; no public-sync |
| guardOwner | existing `GuardRuntimeEngine`, persistence boundary, focused package tests, and governance gates |

## Delta-T1 Execution Control Block

| Field | Disposition |
| --- | --- |
| Existing Gamma tool | preserve `cvf_check_governance_action` and its source-compatible output |
| New tool | `cvf_preflight_governance_action` |
| Contract version | `cvf.delta.governanceActionPreflight.v1` |
| Action classes | `EDIT`, `RUN`, `COMMIT` |
| Guard input | source-defined `GuardRequestContext` fields; tool schema uses strict enums/types |
| Guard execution | existing `GuardRuntimeEngine.evaluate` injected into pure handler |
| Persistence | existing `PersistenceAdapter.saveAuditEntry`; server uses `JsonFileAdapter` |
| Audit location | `CVF_MCP_DELTA_AUDIT_DIR`; otherwise user-local default outside repository |
| Receipt issuance | after durable save resolves successfully |
| Receipt identity | `receiptId` equals persisted `requestId` |
| Proceed claim | `governedActionClaimAllowed=true` only for `ALLOW` plus `auditPersisted=true` |
| Block/escalate | persisted receipt may be returned, but proceed claim remains false |
| Persistence failure | fail closed with `auditPersisted=false` and no valid receipt claim |
| Secret safety | redact or reject credential-bearing action text before evaluation, response, and persistence; raw value must be absent |
| Workflow guidance | system prompt requires new preflight before edit/run/commit when MCP tool is available |
| Enforcement limit | no external interception, receipt consumption, or universal governed-coding claim |

## Foundation Storage Layout Block

| Field | Disposition |
| --- | --- |
| Stable source owner | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/` |
| Stable runtime owner | existing MCP `guards/` and `persistence/` modules |
| Stable reference | existing agent workspace and MCP boundary front doors reused |
| Dated execution artifacts | GC-018, work order, worker return, completion, evidence JSON |
| Archive policy | no archive movement |
| Generated aggregate | N/A with reason: no large JSON aggregate is added or edited |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: read-only startup resolution for Claude and
reviewer-owned continuity sync in a separate post-closure batch. Delta-T1 does
not authorize Claude to edit protected continuity.

Protected paths:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V19_2026-06-15.md`

Operator authorization: the current request authorizes work-order creation and
Claude implementation only. Codex retains protected-path ownership for a
separate session-sync following the accepted material commit.

Rollback boundary: revert only the phase-local dispatch, accepted material, or
session-sync commit that introduced the rejected change. Do not rewrite
unrelated continuity or historical handoffs.

## Worker Autonomy / No-Question Rule

Claude must repair allowed-scope source, test, formatting, type, and gate
failures and rerun the failed checks. Do not ask the operator whether to fix an
allowed-scope failure.

Return `BLOCKED_WITH_REASON` only if remediation requires forbidden paths,
claim expansion, a live/provider call, secrets/quota, public-sync, destructive
action, workspace state mutation, wrapper/proxy interception, or a change to
the existing Gamma contract.

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact:
`docs/reviews/CVF_MCP_MODEL_GATEWAY_COMPOSITION_PROOF_COMPLETION_2026-06-19.md`

freshRecomputeRequired: YES

recomputeReason: Delta-T1 adds a new runtime tool, durable local write path, and
prompt guidance not covered by Composition Proof.

unicodePathHandling: repo-relative paths and ASCII-authored content. Existing
Unicode comments outside changed lines need no broad normalization.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. active handoff named by the state registry
4. `docs/baselines/CVF_GC018_DELTA_T1_GOVERNANCE_ACTION_PREFLIGHT_RECEIPT_2026-06-19.md`
5. this work order
6. `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` row `MCP-GW-001`
7. `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`
8. `docs/reviews/CVF_MCP_MODEL_GATEWAY_COMPOSITION_PROOF_COMPLETION_2026-06-19.md`
9. source files named in the Source Verification Block

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| Gamma advisory classifier is already registered. | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | lines 512-526 | `cvf_check_governance_action` | MCP server registration | ACCEPT |
| Gamma classifier returns `ALLOW_WITH_GUARDS`, `CLARIFY`, or `BLOCK` from action text. | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/startup/startup-state.ts` | lines 39-46, 193-243 | `GovernanceCheckReadout`; `checkGovernanceAction` | startup-state Gamma helper | ACCEPT |
| Full guard pipeline evaluation exists. | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/guards/engine.ts` | lines 55-113 | `evaluate` | `GuardRuntimeEngine` | ACCEPT |
| Guard request and result fields are source-defined. | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/guards/types.ts` | lines 27-67 | `GuardRequestContext`; `GuardPipelineResult`; `GuardAuditEntry` | guard types | ACCEPT |
| Default guard engine has audit enabled and strict mode. | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/guards/types.ts` | lines 86-91 | `DEFAULT_GUARD_RUNTIME_CONFIG` | guard runtime config | ACCEPT |
| Guard factory registers six guards. | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/guards/index.ts` | lines 24-38 | `createGuardEngine` | guard factory | ACCEPT |
| Persistence port saves and retrieves guard audit entries. | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/persistence.interface.ts` | lines 17-29 | `saveAuditEntry`; `getAuditEntries` | `PersistenceAdapter` | ACCEPT |
| JSON adapter persists audit entries to local JSON. | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-file.adapter.ts` | lines 31-67 | `JsonFileAdapter`; `saveAuditEntry` | JSON persistence adapter | ACCEPT |
| Existing tool-call audit is process-local. | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/mcp-tool-audit.ts` | lines 4-6, 26-49 | `auditEntries` | Gamma MCP tool audit | ACCEPT |
| Prompt tool list and mandatory edit guidance have a source owner. | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/prompt/system-prompt.ts` | lines 52-60, 263-281 | `MCP_TOOL_DESCRIPTIONS`; `buildMcpToolsSection` | MCP system prompt | ACCEPT |
| `MCP-GW-001` requires preflight, durable audit/receipt, and bounded claim language. | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` | row `MCP-GW-001` | `MCP-GW-001` | legacy absorption coverage index | ACCEPT |
| Composition prerequisite is closed. | `docs/reviews/CVF_MCP_MODEL_GATEWAY_COMPOSITION_PROOF_COMPLETION_2026-06-19.md` | `Status`; `## Claim Boundary` | `CLOSED_PASS_BOUNDED` | Composition Proof completion | ACCEPT |

## New Doc-Only Fields

| Proposed field or symbol | Disposition |
| --- | --- |
| `cvf_preflight_governance_action` | new Delta-T1 MCP tool id authorized by GC-018 |
| `cvf.delta.governanceActionPreflight.v1` | new receipt contract version |
| `EDIT`, `RUN`, `COMMIT` | new strict action-class values for this tool |
| `CVF_MCP_DELTA_AUDIT_DIR` | new optional local runtime configuration key |
| `receiptId`, `auditPersisted`, `governedActionClaimAllowed` | new Delta-T1 receipt fields |

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
| --- | --- |
| Coverage index | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` |
| Stable row | `MCP-GW-001` |
| Parent gateway row | `MGW-001`; named here to satisfy the current stable-row checker vocabulary while `MCP-GW-001` remains the direct Delta authority |
| Coverage status | `COVERED_SOURCE_BACKED` |
| Delta-T1 use | pre-action governance, no direct bypass claim, durable audit/receipt, and no governed-coding claim without receipt |
| Deferred legacy value | wrapper/CLI/proxy receipt enforcement remains a separate runtime tranche |

## Roadmap-To-Work-Order Trace Matrix

Applicability: N/A with reason: no roadmap tranche owns Delta-T1. The trace
chain is active session next move -> `MCP-GW-001` -> Composition Proof closure
-> fresh GC-018 -> this work order.

| Upstream requirement | Work order section | Worker deliverable | Verification | Dispatch state |
| --- | --- | --- | --- | --- |
| pre-action governance | Delta-T1 Control Block | new modular MCP tool | focused tests | READY |
| durable audit/receipt | Delta-T1 Control Block | persistence-backed receipt | temp-directory readback | READY |
| no direct bypass claim | Claim Boundary | bounded response and worker return | reviewer text/diff check | READY |
| no governed claim without receipt | acceptance AC3-AC5 | fail-closed persistence behavior | focused tests | READY |
| source verification and autorun | source/pre-flight blocks | command evidence | governance gates | READY |

## Write Ownership

Claude may create or modify only:

- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/governance-action-preflight.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/governance-action-preflight.test.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/prompt/system-prompt.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/prompt/system-prompt.test.ts`
- `docs/reviews/CVF_DELTA_T1_GOVERNANCE_ACTION_PREFLIGHT_RECEIPT_WORKER_RETURN_2026-06-19.md`

Claude must not modify:

- this work order or matching GC-018;
- `CVF_SESSION_MEMORY.md`, `CVF_SESSION/`, or the active handoff;
- Model Gateway, CVF Web, generated workspace state, governance checkers, git
  hooks, public-sync clone, provider registry, credential files, or unrelated
  source/tests;
- completion review or closure evidence JSON;
- dependencies or lockfiles.

## Work-Order Fulfillment Manifest

Required worker artifacts:

| Artifact | Required result |
| --- | --- |
| `src/tools/governance-action-preflight.ts` | pure handler plus MCP registration function using injected guard engine and persistence port |
| `src/tools/governance-action-preflight.test.ts` | deterministic allow/block/escalate/persistence-failure/secret-safety coverage |
| `src/index.ts` | bounded registration and user-local JSON adapter configuration; no inline feature implementation |
| `src/prompt/system-prompt.ts` | new tool description and edit/run/commit receipt guidance |
| `src/prompt/system-prompt.test.ts` | exact guidance regression assertions |
| worker-return packet | changed set, tests, gate evidence, claim boundary, HEAD unchanged |

Forbidden worker artifacts: commits, completion review, closure JSON, session
sync, live receipts, provider logs, raw secrets, public artifacts, queues,
wrappers, proxies, git hooks, or new dependencies.

## Pre-Flight Checks

Run from repository root before source edits:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 087f7678 --head HEAD
python governance/compat/run_agent_commit_steward_preflight.py --mode implementation --base 087f7678 --head HEAD --enforce
```

Expected: current dispatch/session commits are visible, worktree is clean, and
both implementation gates pass. If the actual worker-start HEAD differs from
the metadata value, record it in the worker-return packet; do not edit this
work order.

## Execution Instructions

1. Re-read each source symbol in the Source Verification Block.
2. Add a separate `governance-action-preflight.ts` module. Keep feature logic
   out of the 881-line `index.ts` entrypoint.
3. Define a strict input contract for `EDIT`, `RUN`, and `COMMIT`, using existing
   CVF phase/risk/role types and optional source-defined context fields.
4. Inject `GuardRuntimeEngine` and a minimal persistence port into the pure
   handler. Do not instantiate providers or import Model Gateway.
5. Generate a request id, evaluate the guard pipeline, construct a
   `GuardAuditEntry`, and await `saveAuditEntry` before returning a valid
   receipt.
6. Return `governedActionClaimAllowed=true` only when the guard decision is
   `ALLOW` and audit persistence succeeded. `BLOCK`, `ESCALATE`, invalid input,
   secret-bearing input, and persistence error must not produce a proceed claim.
7. Ensure raw credential material is absent from the response, in-memory guard
   context used for persistence, and written audit JSON.
8. Register the tool in `index.ts` with `JsonFileAdapter`, using
   `CVF_MCP_DELTA_AUDIT_DIR` when set and otherwise a user-local directory
   outside the repository. Do not write runtime audit data during module import.
9. Update system-prompt tool guidance to require this tool before edit, run, or
   commit and retain the receipt. State in the prompt that a receipt proves only
   preflight evaluation, not action execution or external interception.
10. Add deterministic focused tests. Use temporary directories and clean them
    after each test. Do not write audit fixtures into the repository.
11. Run all required verification, create the worker-return packet, and leave
    HEAD unchanged.

## Execution Plan

1. Source re-verification and pre-implementation gates.
2. Modular preflight handler and registration implementation.
3. Secret-safe durable audit and receipt behavior.
4. Prompt workflow guidance and regression test.
5. Focused/full package verification.
6. Worker-return packet with exact changed-set evidence.

## Acceptance Criteria

| ID | Criterion |
| --- | --- |
| AC1 | `cvf_preflight_governance_action` is registered; Gamma `cvf_check_governance_action` remains compatible. |
| AC2 | `EDIT`, `RUN`, and `COMMIT` are evaluated through injected `GuardRuntimeEngine`. |
| AC3 | An allowed action returns `receiptId=requestId`, `auditPersisted=true`, and `governedActionClaimAllowed=true` only after durable save succeeds. |
| AC4 | Blocked and escalated actions are persisted, return their actual decision, and keep `governedActionClaimAllowed=false`. |
| AC5 | Persistence failure fails closed with no valid governed-action receipt claim. |
| AC6 | Credential-bearing input is rejected or redacted before output and persistence; raw value is absent from JSON readback. |
| AC7 | Prompt guidance requires Delta preflight before edit/run/commit and says the receipt does not prove execution/interception. |
| AC8 | No provider/live call, secret/quota use, public-sync, queue, wrapper/proxy, workspace state mutation, or readiness claim occurs. |
| AC9 | Focused tests, full MCP test suite, MCP build, worker-return fast gate, and diff checks pass. |
| AC10 | Claude returns uncommitted changes with HEAD unchanged and a complete worker-return packet. |

## Evidence Requirements

Run from `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER`:

```powershell
npx vitest run src/tools/governance-action-preflight.test.ts src/prompt/system-prompt.test.ts --reporter verbose
npm run test:run
npm run build
```

Then run from repository root:

```powershell
git diff --check
python governance/compat/run_worker_return_fast_gate.py
git diff --name-status 087f7678
git status --short
git rev-parse --short HEAD
```

The worker-return packet must report command, result, changed paths, actual
worker-start HEAD, final HEAD, and a secret-safe description of persisted JSON
readback. Do not include raw credential samples in the packet.

## Review Gate

Codex must reject or repair before closure if any of these occurs:

- existing Gamma tool behavior is replaced or renamed;
- a valid receipt is returned before persistence completes;
- persistence failure returns a proceed claim;
- blocked or escalated decisions permit a governed-action claim;
- raw credential material appears in response, memory context, test output, or
  persisted JSON;
- runtime data is written into the repository;
- `index.ts` receives feature logic instead of thin registration;
- wrapper/proxy, shell/IDE/git/filesystem interception, provider, public,
  workspace state, or unrelated files are touched;
- tests/build/gates fail;
- worker commits;
- completion text claims universal governed coding or readiness.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` if the source contracts cannot support durable
receipt correlation without modifying forbidden paths, or if correct behavior
requires external interception, new dependencies, provider/live execution,
secret/quota use, public-sync, workspace state mutation, or claim expansion.

## Operator Checkpoint

No additional operator checkpoint is required for the allowed Delta-T1 worker
scope. Any wrapper/CLI/proxy enforcement, receipt consumption by an execution
launcher, git/IDE/filesystem interception, provider/live proof, secret/quota
use, public-sync, or broader readiness/enforcement claim requires a new
operator checkpoint and fresh governed tranche.

## Closure Checklist

| Item | Dispatch state |
| --- | --- |
| Dispatch Prompt Envelope first | PASS |
| Fresh GC-018 | PASS |
| Source Verification Block | PASS |
| Agent Handoff Contract Control Block | PASS |
| Reviewer Closure Conversion | PASS |
| Work-Order Fulfillment Manifest | PASS |
| Runtime implementation | REQUIRED |
| Focused/full verification | REQUIRED |
| Worker return with unchanged HEAD | REQUIRED |
| Codex completion/evidence/closure gates | REQUIRED |

## Finding-To-Governance Learning Disposition

| Field | Disposition |
| --- | --- |
| Finding | Gamma action classification and in-process audit do not establish durable preflight receipt control |
| Defect class | `RUNTIME_SIGNAL_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Escalation state | `DISPATCHED_BOUNDED_DELTA_T1` |
| Current control action | add durable preflight receipt using existing guard/persistence owners |
| Machine-check action | deferred to a later tranche: receipt consumption/interception is not authorized here |
| Worker blame | N/A with reason: this is a planned architecture progression, not a worker failure |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance Delta runtime implementation. No public-sync is
authorized.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex dispatcher; Claude worker; Codex reviewer/closer |
| Provider or surface | local provenance workspace |
| Session or invocation | `delta-t1-governance-action-preflight-receipt-2026-06-19` |
| Working directory | repository root |
| Command or tool surface | PowerShell, rg, apply_patch, Vitest, TypeScript, Python governance gates |
| Target paths | exact Write Ownership and reviewer closure paths in this work order |
| Allowed scope source | operator request, fresh GC-018, `MCP-GW-001`, Composition Proof closure |
| Before status evidence | clean worktree at `087f7678` before dispatch authoring |
| After status evidence | dispatch gate output for baseline and work order; worker evidence pending execution |
| Diff evidence | dispatch range diff; worker `git diff --name-status`; reviewer closure diff |
| Approval boundary | bounded Delta-T1 local deterministic preflight receipt only |
| Claim boundary | no external interception, provider/live, public-sync, wrapper/proxy, or universal governed-coding claim |
| Agent type | multi-agent dispatch: Codex -> Claude -> Codex |
| Invocation ID | `delta-t1-preflight-receipt-dispatch-codex-2026-06-19` |
| Expected manifest | dispatch: matching GC-018 and this work order; worker: six Write Ownership paths; reviewer: completion/evidence and status conversion |
| Actual changed set | dispatch: matching GC-018 and this work order |
| Manifest delta | MATCH for dispatch phase |
| Deletion or rename disposition | N/A with reason: no deletion or rename authorized |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order | this file | `Status: DISPATCH_READY_FOR_CLAUDE` | PASS |
| GC-018 | matching baseline | `Status: DISPATCH_READY` | PASS |
| Worker return | `docs/reviews/CVF_DELTA_T1_GOVERNANCE_ACTION_PREFLIGHT_RECEIPT_WORKER_RETURN_2026-06-19.md` | `COMPLETE_PENDING_REVIEW` or blocked disposition | REQUIRED |
| Completion review | reviewer-owned path | final bounded disposition | REQUIRED |
| Evidence JSON | reviewer-owned path | acceptance assertion results | REQUIRED |
| Runtime source/tests | Work-Order Fulfillment Manifest | exact changed-set evidence | REQUIRED |
| Provider/live proof | N/A with reason: component-only claim and live execution forbidden | no live command | N/A with reason |
| Public-sync | N/A with reason: not authorized | `DEFERRED_PRIVATE_ONLY` | N/A with reason |
| Session continuity | reviewer-owned separate sync | post-closure or blocked state | REQUIRED |

## Acceptance Receipt Assertion Matrix

| Assertion | Required observation | Dispatch state |
| --- | --- | --- |
| allowed preflight is durable | JSON readback contains matching `requestId` before valid receipt return | REQUIRED |
| blocked/escalated cannot proceed | persisted decision plus `governedActionClaimAllowed=false` | REQUIRED |
| persistence failure fails closed | no valid receipt claim and `auditPersisted=false` | REQUIRED |
| raw credential is absent | secret-safe response and JSON readback | REQUIRED |
| claim stays bounded | prompt, worker return, and completion reject external interception claim | REQUIRED |

## Claim Boundary

Delta-T1 may prove only that an invoked MCP preflight evaluates a planned
action through the existing guard engine, durably records a secret-safe audit
entry, and returns a correlated receipt with a bounded proceed claim. It does
not prove that Claude, Codex, an IDE, shell, git, or filesystem was forced to
invoke the tool; that any action was executed; that a wrapper consumed the
receipt; or that all coding actions are governed.
