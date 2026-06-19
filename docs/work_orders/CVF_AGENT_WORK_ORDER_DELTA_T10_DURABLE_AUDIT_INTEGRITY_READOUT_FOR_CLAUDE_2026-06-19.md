# CVF Agent Work Order - Delta-T10 Durable Audit Integrity Readout

Memory class: FULL_RECORD
Status: CLOSED_PASS_BOUNDED
Date: 2026-06-19
docType: work_order
Batch ID: DELTA-T10
Owner: Claude worker, Codex reviewer
Commit mode: WORKER_MUST_NOT_COMMIT
dispatchBaseHead: `5f774742`
executionBaseHead: `b8545740`
closureBaseHead: `1a08cbd0`
rawMemoryReleased: false

## Dispatch Prompt Envelope

Role: Claude worker under Codex/orchestrator review.

Canonical packet: this work order and matching Delta-T10 GC-018.

Commit mode: `WORKER_MUST_NOT_COMMIT`. Do not commit, push, public-sync, or
edit active session continuity.

executionBaseHead: capture with `git rev-parse --short HEAD` before editing.
If Codex has added a dispatch handoff bridge, run the pre-implementation gate
from the current handoff bridge parent so reviewer-owned handoff sync stays
outside the worker changed range.

Current-time notes: current mode is
`delta_t9_durable_execution_audit_store_closed_next_foundation_ready`; Delta-T9
is closed at continuity commit `5f774742`.

Do-not-misread notes: implement a bounded deterministic integrity readout for
supplied Delta-T9 durable audit records only. Do not implement wrapper/proxy
enforcement, mandatory MCP invocation, direct IDE/shell/git/filesystem
interception, provider calls, external readiness, arbitrary commands, EDIT/
COMMIT execution, public-sync, or universal governed-coding control.

Required first actions: read `CVF_SESSION_MEMORY.md`, resolve
`CVF_SESSION/ACTIVE_SESSION_STATE.json`, read `AGENT_HANDOFF_V20_2026-06-19.md`,
read this work order and the matching GC-018, capture `executionBaseHead`, then
run pre-implementation gate before source edits.

Return contract: return uncommitted `COMPLETE_PENDING_REVIEW` artifacts for
Codex review, or return `BLOCKED` with evidence. Codex owns review, commit,
closure conversion, and session sync.

## Purpose

Implement the bounded Delta-T10 durable audit integrity readout for supplied
Delta-T9 durable execution audit records. The result should make already stored
or supplied records easier to review without claiming runtime enforcement or
external action observation.

## Required First Reads

| Artifact | Use |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | active mode and parked scope |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | machine-readable continuity |
| `AGENT_HANDOFF_V20_2026-06-19.md` | current handoff and no-commit boundary |
| `docs/baselines/CVF_GC018_DELTA_T10_DURABLE_AUDIT_INTEGRITY_READOUT_2026-06-19.md` | exact authorization |
| `docs/roadmaps/CVF_DELTA_EXECUTION_CONTROL_CAPABILITY_ROADMAP_2026-06-19.md` | parked execution-control boundary |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-store.ts` | existing durable record contract |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/receipt-to-execution-evidence-auditor.ts` | existing evidence/action verdict fields |

## Scope / Target / Owner Boundary

Allowed scope:

- create `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-readout.ts`;
- create `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-readout.test.ts`;
- create `docs/reviews/CVF_DELTA_T10_DURABLE_AUDIT_INTEGRITY_READOUT_COMPLETION_2026-06-19.md`;
- create `docs/reviews/evidence/delta-t10-durable-audit-integrity-readout-2026-06-19.json`;
- update this work order only for worker-return status/evidence if needed.
- Codex reviewer closure may update
  `docs/baselines/CVF_GC018_DELTA_T10_DURABLE_AUDIT_INTEGRITY_READOUT_2026-06-19.md`,
  this work order, the completion review, and the evidence JSON for closure
  conversion only.

Forbidden scope:

- no commits, staging for commit, push, or public-sync;
- no `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF*.md`, roadmap,
  baseline, active state, or generated aggregate edits;
- no `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts`, MCP tool registration,
  launcher/profile expansion, CLI binary registration, package lockfile, Model
  Gateway, CVF Web, provider/live, queue, daemon, or public repo changes;
- no arbitrary commands, EDIT/COMMIT execution, wrapper/proxy enforcement,
  direct interception, readiness, release, or universal-control claim.

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| intake summary | operator asked to proceed from closed Delta-T9 evidence at `docs/reviews/CVF_DELTA_T9_DURABLE_EXECUTION_AUDIT_CONTRACT_STORE_BOUNDARY_COMPLETION_2026-06-19.md` and continuity commit `5f774742` |
| scope classification | bounded local durable audit readout |
| risk sensitivity | R1; pure deterministic classification over supplied records |
| selected role route | `MULTI_AGENT_MULTI_ROLE` |
| role separation basis | Claude implements uncommitted; Codex reviews, commits, closes, and syncs |
| escalation condition | any runtime registration, provider/live, public-sync, direct interception, file-system observation, or claim expansion |

## Authority Chain

| Level | Artifact | Status |
| --- | --- | --- |
| Operator | current instruction, 2026-06-19 | ACCEPTED |
| Session | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | next high-value foundation selection |
| Roadmap | `docs/roadmaps/CVF_DELTA_EXECUTION_CONTROL_CAPABILITY_ROADMAP_2026-06-19.md` | durable audit continuation allowed only via fresh source-verified tranche |
| Delta-T9 closure | `docs/reviews/CVF_DELTA_T9_DURABLE_EXECUTION_AUDIT_CONTRACT_STORE_BOUNDARY_COMPLETION_2026-06-19.md` | CLOSED_PASS_BOUNDED |
| GC-018 | `docs/baselines/CVF_GC018_DELTA_T10_DURABLE_AUDIT_INTEGRITY_READOUT_2026-06-19.md` | CLOSED_PASS_BOUNDED |

## Agent Roles

| Role | Actor | Responsibility |
| --- | --- | --- |
| Dispatcher | Codex | source-verified packet and dispatch |
| Implementer | Claude | allowed source/test/worker-return/evidence files only |
| Reviewer/committer | Codex | inspect uncommitted return, run reviewer gates, commit or reject |
| Session-sync actor | Codex | update continuity only once Codex accepts the worker return |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: N/A with reason: Claude is not authorized to
edit protected governance guards, active state, active handoff, front door, or
session source. Codex may perform reviewer-owned continuity later in a separate
packet/commit if the worker return is accepted.

Protected paths:

- N/A with reason: no protected path is worker-owned.

Operator authorization: current operator instruction authorizes a Claude work
order only, not protected path mutation.

Rollback boundary: Codex may reject or revert only Delta-T10 worker-owned files
if returned work is unsafe. Do not revert prior Delta, GGL, MCP composition, or
public-sync history.

## Agent Handoff Contract Control Block

| Field | Disposition |
| --- | --- |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | worker-no-commit split: Claude worker returns uncommitted artifacts; Codex reviewer owns commit and closure |
| phase | DISPATCH_AUTHORING, WORKER_EXECUTION, REVIEWER_CLOSURE, SESSION_SYNC |
| baseHeadFor(phase) | dispatch=`5f774742`; execution=`b8545740`; closure=`1a08cbd0` |
| changedSetScope(phase) | dispatch packet; worker-owned source/test/worker-return/evidence; reviewer closure conversion; separate sync |
| traceScope(phase, actor) | exact manifests and commands per phase |
| commitOwner(phase) | Codex only |
| crossBatchIsolation | worker must start from clean worktree or record BLOCKED |
| nextMoveSurfaces | Claude must not edit; Codex handles during reviewer closure |
| closerOwner | Codex is designated closer |

## Reviewer Closure Conversion

| Field | Disposition |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_DELTA_T10_DURABLE_AUDIT_INTEGRITY_READOUT_COMPLETION_2026-06-19.md` |
| reviewerOwnedClosurePaths | matching GC-018, this work order, worker return/completion, evidence JSON, active session state/front door/handoff only if accepted |
| workerReturnStatus | worker no-commit return accepted by Codex at material commit `8f4abb28` |
| reviewerAction | Codex ran reviewer-fast, focused tests, full MCP tests/build, committed-range gates, and accepted bounded material |

## Durable Audit Integrity Readout Control Block

| Field | Disposition |
| --- | --- |
| input boundary | supplied `DurableExecutionAuditRecord[]` and/or supplied JSONL text only |
| identity | receiptId, requestId, consumptionId, profileId, bindingHash, and contractVersion preserved in findings when safe |
| parsing | fail-closed parse findings for malformed supplied JSONL lines |
| classification | invalid contract, malformed identity, invalid binding hash, invalid proof consistency, forbidden true claim fields, and secret-like values |
| determinism | stable sorted findings and stable summary counts |
| privacy boundary | no raw secrets, environment values, provider keys, or full command output in readout output |
| retention | readout reports existing retention/disposal fields; no deletion daemon |
| readout claim | deterministic local classification only |
| claim boundary | no mandatory invocation, no direct interception, no provider/live proof |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | durable audit integrity readout for supplied records only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | `CVF_RECEIPT_PRESENT` only when supplied records include valid receipt identity; `CLAIM_REJECTED_NO_RECEIPT` for missing or invalid receipt identity |
| actionEvidence | `ACTION_EVIDENCE_PRESENT` only as a supplied durable record field; `CLAIM_REJECTED_NO_ACTION` for invalid or missing action evidence |
| invocationBoundary | cooperating caller supplies records or JSONL text to the readout |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception |
| claimLanguage | deterministic integrity readout of supplied durable audit records |
| forbiddenExpansion | wrapper/proxy enforcement, direct interception, EDIT/COMMIT, provider/live, public-sync, queue/daemon, CVF Web action execution, and universal control parked |

## Delta Mutating Profile Boundary Control Block

| Field | Disposition |
| --- | --- |
| profileScope | N/A with reason: no mutating profile or target mutation is added |
| fixedTargetPolicy | N/A with reason: no target authority is added |
| approvalEvidenceSource | existing supplied durable record field only when present |
| callerPathInput | CALLER_PATH_INPUT_FORBIDDEN as target authority; readout consumes supplied record text/objects only |
| commandAuthority | no command authority, launcher profile, or target path authority added |
| receiptChain | existing receipt/consumption/execution/audit identity chain only |
| claimBoundary | readout does not add mutation or execution capability |
| forbiddenExpansion | arbitrary targets, EDIT/COMMIT, provider/live, public-sync, and interception remain parked |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | external runtime-control finding -> Delta roadmap -> source-verified durable audit tranche |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| Owner surface | Delta-T10 work order |
| Disposition | `DO_NOW` durable audit readout only |
| Claim boundary | no runtime/provider/public/interception/readiness/universal-control claim |

## Source Verification Block

| Claimed item | Verification type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Durable audit contract constant exists. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-store.ts` | line 11 | `DURABLE_EXECUTION_AUDIT_CONTRACT` | Delta-T9 durable store | ACCEPT |
| Binding hash validation pattern exists. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-store.ts` | line 14 | `BINDING_HASH_PATTERN` | Delta-T9 durable store | ACCEPT |
| Durable audit record interface exists. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-store.ts` | line 28 | `DurableExecutionAuditRecord` | Delta-T9 durable store | ACCEPT |
| Durable records set mandatory invocation proof false. | LITERAL_INVARIANT | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-store.ts` | lines 43, 109, and 138 | `mandatoryInvocationProved` | `DurableExecutionAuditRecord`; `buildDurableAuditRecord`; `validateDurableRecordBoundary` | ACCEPT |
| Durable records set direct interception proof false. | LITERAL_INVARIANT | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-store.ts` | lines 44, 110, and 141 | `directInterceptionProved` | `DurableExecutionAuditRecord`; `buildDurableAuditRecord`; `validateDurableRecordBoundary` | ACCEPT |
| Durable store validates records before append/read. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-store.ts` | lines 121, 156-157, and 181-182 | `validateDurableRecordBoundary`; `appendRecord`; `readRecords` | `JsonDurableExecutionAuditStore` | ACCEPT |
| Receipt-to-execution audit exposes evidence, action, and approval-backed mutation proof fields. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/receipt-to-execution-evidence-auditor.ts` | lines 64 and 67-69 | `ReceiptToExecutionEvidenceAudit`; `evidenceChainValid`; `actionExecutionProved`; `approvalBackedMutationProved` | Delta-T7 auditor | ACCEPT |
| Delta-T9 completion status is closed. | VALUE_SET | `docs/reviews/CVF_DELTA_T9_DURABLE_EXECUTION_AUDIT_CONTRACT_STORE_BOUNDARY_COMPLETION_2026-06-19.md` | line 5 | `Status` | Delta-T9 completion packet | ACCEPT |
| Delta-T9 completion records focused, full MCP, build, and worker-return gate evidence. | VALUE_SET | `docs/reviews/CVF_DELTA_T9_DURABLE_EXECUTION_AUDIT_CONTRACT_STORE_BOUNDARY_COMPLETION_2026-06-19.md` | line 121 | `AC6` | Delta-T9 completion packet | ACCEPT |
| Roadmap parks durable audit and all broader execution-control claims behind fresh source-verified work. | LITERAL_INVARIANT | `docs/roadmaps/CVF_DELTA_EXECUTION_CONTROL_CAPABILITY_ROADMAP_2026-06-19.md` | lines 149-151 and 158 | `Durable execution audit`; `Wrapper/proxy enforcement`; `Direct IDE/shell/git/filesystem interception`; `Next-Tranche Release Conditions` | Delta execution roadmap | ACCEPT |

## New Doc-Only Fields

| Item | Shape | Purpose |
| --- | --- | --- |
| `DURABLE_AUDIT_INTEGRITY_READOUT_CONTRACT` | literal string | stable readout contract identity |
| `DurableAuditIntegrityReadout` | typed summary | total/valid/invalid counts, finding counts, and bounded claim fields |
| `DurableAuditIntegrityFinding` | typed finding | deterministic code, severity, record identity, and secret-safe message |
| `buildDurableAuditIntegrityReadout` | pure function | classify supplied records |
| `parseDurableAuditJsonlLines` or equivalent | pure helper | classify supplied JSONL parse errors without file I/O |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: Claude must run source verification, tests, and gates against
current working tree before returning.

unicodePathHandling: literal paths and UTF-8-safe readers. New agent-authored
source and Markdown must default to ASCII.

## Foundation Storage Layout Block

| Field | Disposition |
| --- | --- |
| stable source | existing MCP `src/audit/` owner surface |
| durable store target | N/A with reason: T10 readout must not add a new store by default |
| dated execution artifacts | this GC-018, work order, worker return, evidence JSON |
| generated aggregate | N/A with reason: none added by Claude |
| index | N/A with reason: no MCP/server registration authorized |

## Current Runtime Freshness Verification

| Surface | Evidence |
| --- | --- |
| base | dispatch base `5f774742` |
| existing durable store | Delta-T9 module exists under `src/audit/` |
| existing auditor | Delta-T7 module exists under `src/audit/` |
| integrity readout | planned files absent at dispatch |
| live/provider | N/A with reason: forbidden and unnecessary |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order owner | Evidence |
| --- | --- | --- |
| durable execution audit requires fresh source-verified work | Codex dispatch | matching GC-018 and this source verification block |
| secret-safe retention/disposal readout | Claude worker | integrity readout fields, tests, worker return |
| local gate evidence | Claude worker | focused/full/build/worker-return fast gate results |
| no wrapper/proxy or direct interception | Claude worker and Codex reviewer | claim boundary fields and Delta checker compatibility |
| no universal control claim | Claude worker and Codex reviewer | readout-only contract and closure evidence |

## Work-Order Fulfillment Manifest

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
| --- | --- | --- |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-readout.ts` | Yes | durable audit integrity readout implementation |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-readout.test.ts` | Yes | focused regression and boundary tests |
| `docs/reviews/CVF_DELTA_T10_DURABLE_AUDIT_INTEGRITY_READOUT_COMPLETION_2026-06-19.md` | Yes | Claude no-commit return packet |
| `docs/reviews/evidence/delta-t10-durable-audit-integrity-readout-2026-06-19.json` | Yes | machine-readable worker evidence |

## Forbidden Path Manifest

| Path | Reason |
| --- | --- |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | no MCP registration authorized |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/**` | no launcher/profile expansion authorized |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/package.json` | no binary/script/dependency change authorized |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/**` | no CVF Web work authorized |
| `CVF_SESSION/**` | reviewer-owned continuity only |
| `CVF_SESSION_MEMORY.md` | reviewer-owned continuity only |
| `AGENT_HANDOFF*.md` | reviewer-owned continuity only |
| public-sync clone | no Claude public work authorized |

## Forbidden Filesystem State At Dispatch

| Forbidden path | Expected state | Actual state at dispatch | Action if PRESENT |
| --- | --- | --- | --- |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-readout.ts` | ABSENT | ABSENT | N/A |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-readout.test.ts` | ABSENT | ABSENT | N/A |
| `docs/reviews/CVF_DELTA_T10_DURABLE_AUDIT_INTEGRITY_READOUT_COMPLETION_2026-06-19.md` | ABSENT | ABSENT | N/A |
| `docs/reviews/evidence/delta-t10-durable-audit-integrity-readout-2026-06-19.json` | ABSENT | ABSENT | N/A |

## Required Proof Manifest

| Proof | Path | Required literal | Required at handoff |
| --- | --- | --- | --- |
| contract identity | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-readout.ts` | `DURABLE_AUDIT_INTEGRITY_READOUT_CONTRACT` | Yes |
| readout summary | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-readout.ts` | `DurableAuditIntegrityReadout` | Yes |
| bounded claim check | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-readout.ts` | `mandatoryInvocationProved` | Yes |
| bounded claim check | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-readout.ts` | `directInterceptionProved` | Yes |
| secret safety | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-readout.test.ts` | `secret-like values are classified without raw echo` | Yes |
| no-commit return | `docs/reviews/CVF_DELTA_T10_DURABLE_AUDIT_INTEGRITY_READOUT_COMPLETION_2026-06-19.md` | `COMPLETE_PENDING_REVIEW` | Yes |

## Allowed Changed Set

Claude may leave only the required artifact manifest paths plus this work order
if status/evidence rows need worker-return updates. Claude must not stage,
commit, push, public-sync, or edit session continuity.

## Acceptance Criteria

| ID | Criterion | Worker evidence |
| --- | --- | --- |
| AC1 | Valid Delta-T9 durable records produce a deterministic integrity readout with contract version, valid counts, and no findings. | focused test |
| AC2 | Malformed JSONL or structurally invalid records produce findings and cannot be summarized as all valid. | focused test |
| AC3 | `mandatoryInvocationProved=true` or `directInterceptionProved=true` is classified as a violation, and bounded false fields remain explicit in valid summaries. | focused test/source |
| AC4 | Secret-like values in supplied record fields are classified or rejected without being echoed raw in readout output. | focused test |
| AC5 | Finding order and finding counts are deterministic across repeated calls. | focused test |
| AC6 | Focused tests, MCP full test suite, build, and worker-return fast gate pass before handoff. | command evidence |

## Verification Commands

```powershell
cd EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER
npx vitest run src/audit/durable-execution-audit-readout.test.ts --reporter verbose
npm run test:run
npm run build
cd ..\..
python governance/compat/run_worker_return_fast_gate.py
git status --short
git diff --name-status
```

## Pre-Flight Checks

Before implementation, Claude must run:

```powershell
git rev-parse --short HEAD
$preImplementationBase = git rev-parse --short HEAD^
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base $preImplementationBase --head HEAD
```

Expected result: PASS. Codex verified this parent-bridge form before this
repair. Return `BLOCKED` if the repo is dirty or the gate failure is outside
this work order's allowed remediation scope.

## Write Ownership

Claude owns only:

- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-readout.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-readout.test.ts`
- `docs/reviews/CVF_DELTA_T10_DURABLE_AUDIT_INTEGRITY_READOUT_COMPLETION_2026-06-19.md`
- `docs/reviews/evidence/delta-t10-durable-audit-integrity-readout-2026-06-19.json`
- this work order, only for worker-return status/evidence updates

Write mode: create-only for new source/test/review/evidence files; limited
modify-listed for this work order.

## Execution Plan

1. Capture `executionBaseHead` and verify clean starting status.
2. Run pre-implementation autorun gate.
3. Implement durable audit integrity readout under `src/audit/` only.
4. Add focused tests for valid records, malformed JSONL, forged true claim
   fields, secret-like values, deterministic findings, and summary counts.
5. Run focused tests, full MCP tests, build, worker-return fast gate, status,
   and diff.
6. Create worker-return packet and evidence JSON.
7. Return uncommitted worker packet to Codex, or `BLOCKED`.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Claude worker |
| Provider or surface | Claude Code / local workspace |
| Session or invocation | Delta-T10 worker execution, 2026-06-19 |
| Working directory | repository root |
| Command or tool surface | startup reads, pre-implementation gate, Vitest, npm build/test, worker-return gate |
| Target paths | required artifact manifest only |
| Allowed scope source | this work order and matching Delta-T10 GC-018 |
| Before status evidence | clean worktree at dispatch base `5f774742`; worker must record `git status --short` and `git rev-parse --short HEAD` before edits |
| After status evidence | worker-return `git status --short` |
| Diff evidence | `git diff --name-status` |
| Approval boundary | worker may create allowed artifacts only; Codex commits/reviews |
| Claim boundary | durable audit readout only; no runtime interception or universal control |
| Agent type | worker-no-commit under `MULTI_AGENT_MULTI_ROLE` |
| Invocation ID | `delta-t10-durable-audit-integrity-readout-claude-2026-06-19` |
| Expected manifest | `docs/work_orders/CVF_AGENT_WORK_ORDER_DELTA_T10_DURABLE_AUDIT_INTEGRITY_READOUT_FOR_CLAUDE_2026-06-19.md` |
| Actual changed set | `docs/work_orders/CVF_AGENT_WORK_ORDER_DELTA_T10_DURABLE_AUDIT_INTEGRITY_READOUT_FOR_CLAUDE_2026-06-19.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: deletion/rename forbidden |

## Evidence Requirements

Required worker evidence:

- source verification notes for any final symbol names that differ from planned
  names;
- focused Vitest command/result;
- `npm run test:run` command/result;
- `npm run build` command/result;
- worker-return fast gate command/result;
- `git status --short`;
- `git diff --name-status`;
- worker-return packet;
- evidence JSON;
- explicit statement that no commit, push, public-sync, provider/live, session
  sync, MCP registration, launcher/profile expansion, wrapper/proxy
  enforcement, or direct interception occurred.

## Review Gate

Codex must reject the worker return if:

- any forbidden path changed;
- the readout implies it observed external action occurrence by itself;
- malformed or invalid records can be summarized as all valid;
- secret-like values are echoed raw in readout output;
- mandatory invocation, direct interception, provider/live, external readiness,
  deployment readiness, release readiness, or universal governed-coding control
  is claimed;
- worker committed, pushed, public-synced, or edited session continuity.

## Return-To-Orchestrator Conditions

Claude must return `BLOCKED` without continuing if:

- the pre-implementation gate fails outside allowed scope;
- source contracts are missing or materially changed from this packet;
- implementation requires editing forbidden paths;
- tests require provider/live keys, public-sync, or secrets;
- integrity readout cannot be made deterministic, secret-safe, and bounded.

## Closure Checklist

| Item | Worker disposition |
| --- | --- |
| acceptance criteria | worker records PASS, BLOCKED, or N/A with reason in completion packet |
| focused tests | required before worker no-commit return |
| full MCP tests | required before worker no-commit return |
| build | required before worker no-commit return |
| worker-return fast gate | required before worker no-commit return |
| commit mode | must remain `WORKER_MUST_NOT_COMMIT` |
| forbidden paths | must remain unchanged |
| public/provenance boundary | no worker export or sibling clone mutation |
| closure claim | Codex reviewer-owned only |

## Operator Checkpoint

No operator checkpoint applies inside the bounded worker scope. Operator
checkpoint is required for wrapper/proxy enforcement, direct interception,
EDIT/COMMIT execution, provider/live proof, public-sync, secrets/quota,
session continuity edits by Claude, or claim-boundary expansion.

## Worker Autonomy / No-Question Rule

Claude should proceed without operator questions for non-destructive work inside
Allowed scope. Allowed-scope test or lint failures must be repaired and rerun.
Escalate only for scope expansion, live/provider proof, public-sync, secrets,
forbidden paths, destructive actions, or claim-boundary changes.

## Closure Quality Gate

Worker handoff is not closure. Codex owns reviewer closure conversion,
committed-range pre-closure, final status, and session sync if the worker return
is accepted.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance Delta execution-control foundation tranche. Public
sync is not worker-authorized.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this work order | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_DELTA_T10_DURABLE_AUDIT_INTEGRITY_READOUT_COMPLETION_2026-06-19.md` | `Status: CLOSED_PASS_BOUNDED`; accepted material commit `8f4abb28` | PASS |
| Roadmap state | `docs/roadmaps/CVF_DELTA_EXECUTION_CONTROL_CAPABILITY_ROADMAP_2026-06-19.md` | roadmap remains `Status: CLOSED_PASS_BOUNDED`; Delta-T10 bounded continuation completed by this closure | PASS |
| Registry JSON | N/A with reason: not corpus intake | no registry mutation authorized | BLOCKED with reason: no registry mutation authorized for this tranche |
| Registry Markdown | N/A with reason: no registry edit authorized | no registry mutation authorized | BLOCKED with reason: no registry mutation authorized for this tranche |
| External evidence digest | N/A with reason: no external evidence | repo-local source/test evidence only | N/A with reason |
| System loop interlock | durable audit readout source/tests | focused 30/30, full MCP 688/688, build PASS, worker-return fast gate PASS | PASS |
| Session continuity | active state, memory, and handoff | material handoff bridge `1a08cbd0`; final closure sync remains separate reviewer-owned continuity | PASS |

## Acceptance Receipt Assertion Matrix

| Required value | Expected value | Status |
| --- | --- | --- |
| commit mode | `WORKER_MUST_NOT_COMMIT`; Codex committed accepted material | PASS |
| runtime scope | bounded new audit readout module only | PASS |
| provider/live scope | false | PASS |
| public-sync | false | PASS |
| direct interception claim | false | PASS |
| universal governed-coding claim | false | PASS |

## Claim Boundary

Delta-T10 may prove only a bounded deterministic integrity readout for supplied
Delta-T9 durable execution audit records. It does not prove that all actions
pass through CVF, that external actions are observed, that direct IDE/shell/git/
filesystem activity is intercepted, or that CVF has universal governed-coding
control.
