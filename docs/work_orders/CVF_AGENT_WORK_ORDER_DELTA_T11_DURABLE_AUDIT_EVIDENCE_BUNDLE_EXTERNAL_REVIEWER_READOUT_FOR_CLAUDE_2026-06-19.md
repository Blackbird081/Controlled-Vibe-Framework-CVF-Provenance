# CVF Agent Work Order - Delta-T11 Durable Audit Evidence Bundle External Reviewer Readout

Memory class: FULL_RECORD
Status: DISPATCHED
Date: 2026-06-19
docType: work_order
Batch ID: DELTA-T11
Owner: Claude worker, Codex reviewer
Commit mode: WORKER_MUST_NOT_COMMIT
dispatchBaseHead: `66cb8494`
executionBaseHead: `PENDING_CLAUDE_CAPTURE`
closureBaseHead: `N/A_REVIEWER_OWNED`
rawMemoryReleased: false

## Dispatch Prompt Envelope

Role: Claude worker under Codex/orchestrator review.

Canonical packet: this work order and matching Delta-T11 GC-018.

Commit mode: `WORKER_MUST_NOT_COMMIT`. Do not commit, push, public-sync, or
edit active session continuity.

executionBaseHead: capture with `git rev-parse --short HEAD` before editing.
If Codex has added a dispatch handoff bridge, run the pre-implementation gate
from the current handoff bridge parent so reviewer-owned handoff sync stays
outside the worker changed range.

Current-time notes: current mode is
`delta_t10_durable_audit_integrity_readout_closed_next_foundation_ready`;
Delta-T10 is closed at continuity commit `66cb8494`.

Do-not-misread notes: implement a bounded deterministic evidence bundle for
supplied Delta-T9 durable audit records and supplied Delta-T10 integrity
readouts only. Do not implement wrapper/proxy enforcement, mandatory MCP
invocation, direct IDE/shell/git/filesystem interception, provider calls,
external readiness, arbitrary commands, EDIT/COMMIT execution, public-sync, or
universal governed-coding control.

Required first actions: read `CVF_SESSION_MEMORY.md`, resolve
`CVF_SESSION/ACTIVE_SESSION_STATE.json`, read `AGENT_HANDOFF_V20_2026-06-19.md`,
read this work order and the matching GC-018, capture `executionBaseHead`, then
run pre-implementation gate before source edits.

Return contract: return uncommitted `COMPLETE_PENDING_REVIEW` artifacts for
Codex review, or return `BLOCKED` with evidence. Codex owns review, commit,
closure conversion, and session sync.

## Purpose

Implement the bounded Delta-T11 durable audit evidence bundle and external
reviewer readout for supplied Delta-T9/T10 durable audit artifacts. The result
should make already stored and already classified evidence easier for an
external reviewer to inspect without claiming runtime enforcement or external
action observation.

## Required First Reads

| Artifact | Use |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | active mode and parked scope |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | machine-readable continuity |
| `AGENT_HANDOFF_V20_2026-06-19.md` | current handoff and no-commit boundary |
| `docs/baselines/CVF_GC018_DELTA_T11_DURABLE_AUDIT_EVIDENCE_BUNDLE_EXTERNAL_REVIEWER_READOUT_2026-06-19.md` | exact authorization |
| `docs/reference/external_agent_review/README.md` | external review context front door |
| `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_REVIEW_CONTEXT_STANDARD.md` | external review context boundary |
| `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | external knowledge intake routing |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-store.ts` | existing durable record contract |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-readout.ts` | existing integrity readout contract |

## Scope / Target / Owner Boundary

Allowed scope:

- create `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-audit-evidence-bundle.ts`;
- create `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-audit-evidence-bundle.test.ts`;
- create `docs/reviews/CVF_DELTA_T11_DURABLE_AUDIT_EVIDENCE_BUNDLE_EXTERNAL_REVIEWER_READOUT_COMPLETION_2026-06-19.md`;
- create `docs/reviews/evidence/delta-t11-durable-audit-evidence-bundle-external-reviewer-readout-2026-06-19.json`;
- update this work order only for worker-return status/evidence if needed.
- Codex reviewer closure may update the matching GC-018, this work order, the
  completion review, and the evidence JSON for closure conversion only.

Forbidden scope:

- no commits, staging for commit, push, or public-sync;
- no `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF*.md`, roadmap,
  baseline, active state, or generated aggregate edits by Claude;
- no `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts`, MCP tool registration,
  launcher/profile expansion, CLI binary registration, package lockfile, Model
  Gateway, CVF Web, provider/live, queue, daemon, or public repo changes;
- no arbitrary commands, EDIT/COMMIT execution, wrapper/proxy enforcement,
  direct interception, readiness, release, production, or universal-control
  claim.

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| intake summary | current instruction accepted Delta-T11 from closed Delta-T10 continuity commit `66cb8494` |
| scope classification | bounded local durable audit evidence bundle and reviewer readout |
| risk sensitivity | R1; pure deterministic summarization over supplied artifacts |
| selected role route | `MULTI_AGENT_MULTI_ROLE` |
| role separation basis | Claude implements uncommitted; Codex reviews, commits, closes, and syncs |
| escalation condition | any runtime registration, provider/live, public-sync, direct interception, file-system observation, or claim expansion |

## Authority Chain

| Level | Artifact | Status |
| --- | --- | --- |
| Operator | current instruction, 2026-06-19 | ACCEPTED |
| Session | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | next high-value foundation selection |
| External review reference | `docs/reference/external_agent_review/README.md` | ACTIVE_INDEX |
| Delta-T10 closure | `docs/reviews/CVF_DELTA_T10_DURABLE_AUDIT_INTEGRITY_READOUT_COMPLETION_2026-06-19.md` | CLOSED_PASS_BOUNDED |
| GC-018 | `docs/baselines/CVF_GC018_DELTA_T11_DURABLE_AUDIT_EVIDENCE_BUNDLE_EXTERNAL_REVIEWER_READOUT_2026-06-19.md` | DISPATCHED |

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

Human authorization: current instruction authorizes a Claude work order only,
not protected path mutation.

Rollback boundary: Codex may reject or revert only Delta-T11 worker-owned files
if returned work is unsafe. Do not revert prior Delta, GGL, MCP composition, or
public-sync history.

## Agent Handoff Contract Control Block

| Field | Disposition |
| --- | --- |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | worker-no-commit split: Claude worker returns uncommitted artifacts; Codex reviewer owns commit and closure |
| phase | DISPATCH_AUTHORING, WORKER_EXECUTION, REVIEWER_CLOSURE, SESSION_SYNC |
| baseHeadFor(phase) | dispatch=`66cb8494`; execution=`PENDING_CLAUDE_CAPTURE`; closure=`N/A_REVIEWER_OWNED` |
| changedSetScope(phase) | dispatch packet; worker-owned source/test/worker-return/evidence; reviewer closure conversion; separate sync |
| traceScope(phase, actor) | exact manifests and commands per phase |
| commitOwner(phase) | Codex only |
| crossBatchIsolation | worker must start from clean worktree or record BLOCKED |
| nextMoveSurfaces | Claude must not edit; Codex handles during reviewer closure |
| closerOwner | Codex is designated closer |

## Reviewer Closure Conversion

| Field | Disposition |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_DELTA_T11_DURABLE_AUDIT_EVIDENCE_BUNDLE_EXTERNAL_REVIEWER_READOUT_COMPLETION_2026-06-19.md` |
| reviewerOwnedClosurePaths | matching GC-018, this work order, worker return/completion, evidence JSON, active session state/front door/handoff only if accepted |
| workerReturnStatus | PENDING |
| reviewerAction | PENDING |

## Durable Audit Evidence Bundle Control Block

| Field | Disposition |
| --- | --- |
| input boundary | supplied `DurableExecutionAuditRecord[]` and supplied `DurableAuditIntegrityReadout` only |
| source refs | optional caller-supplied artifact paths and commit refs as labels only |
| claim matrix | receipt evidence, action evidence, durable storage, integrity readout, mandatory invocation, direct interception, provider/live, public-sync, readiness, universal control |
| disposition values | `PROVED`, `BOUNDED`, `REJECTED`, `NOT_CLAIMED` |
| determinism | stable sorted claims, counts, and markdown output |
| privacy boundary | no raw secrets, environment values, provider keys, or full command output |
| readout claim | deterministic local evidence summary only |
| claim boundary | no mandatory invocation, no direct interception, no provider/live proof |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | durable audit evidence bundle and external reviewer readout for supplied records/readouts only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | `CVF_RECEIPT_PRESENT` only when supplied valid durable records include receipt identity; `CLAIM_REJECTED_NO_RECEIPT` otherwise |
| actionEvidence | `ACTION_EVIDENCE_PRESENT` only as supplied durable record/readout evidence; `CLAIM_REJECTED_NO_ACTION` otherwise |
| invocationBoundary | cooperating caller supplies records and readout |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception |
| claimLanguage | deterministic evidence bundle for reviewer readout |
| forbiddenExpansion | wrapper/proxy enforcement, direct interception, EDIT/COMMIT, provider/live, public-sync, queue/daemon, CVF Web action execution, and universal control parked |

## Delta Mutating Profile Boundary Control Block

| Field | Disposition |
| --- | --- |
| profileScope | N/A with reason: no mutating profile or target mutation is added |
| fixedTargetPolicy | N/A with reason: no target authority is added |
| approvalEvidenceSource | existing supplied durable record/readout field only when present |
| callerPathInput | CALLER_PATH_INPUT_FORBIDDEN as target authority; bundle consumes supplied objects/labels only |
| commandAuthority | no command authority, launcher profile, or target path authority added |
| receiptChain | existing receipt/consumption/execution/audit identity chain only |
| claimBoundary | bundle does not add mutation or execution capability |
| forbiddenExpansion | arbitrary targets, EDIT/COMMIT, provider/live, public-sync, and interception remain parked |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent packet request |
| Chain map route | source-verified durable audit evidence -> bounded reviewer readout |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| Owner surface | Delta-T11 work order |
| Disposition | `DO_NOW` evidence-bundle readout only |
| Claim boundary | no runtime/provider/public/interception/readiness/universal-control claim |

## Rescan Intelligence Hardening

Original source artifact: `docs/reference/external_agent_review/README.md` and
`docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_REVIEW_CONTEXT_STANDARD.md`.

Predecessor intake artifact:
`docs/reviews/CVF_DELTA_T10_DURABLE_AUDIT_INTEGRITY_READOUT_COMPLETION_2026-06-19.md`
at continuity commit `66cb8494`.

Delta ledger status: COMPLETE_WITH_DECLARED_LIMITS - this dispatch routes a
bounded follow-up from closed Delta-T10 evidence into a new source-verified
implementation packet.

Routing matrix status: COMPLETE_WITH_DECLARED_LIMITS - all routing lanes are
classified below for this dispatch.

Semantic sampling status: COMPLETE_WITH_DECLARED_LIMITS - representative claims
are adversarially checked below.

- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Category | Delta-T11 disposition |
| --- | --- |
| UNCHANGED_FROM_INTAKE | T9/T10 durable audit contracts remain the source authority. |
| CHANGED_DISPOSITION | External-review context moves from reference guidance to a bounded evidence-bundle implementation packet. |
| NEW_FINDING | External reviewer readout needs explicit `NOT_CLAIMED` rows for forbidden expansion claims. |
| REMOVED_OR_REJECTED | Public-sync, provider/live, readiness, direct interception, and universal-control claims remain rejected. |

### Follow-Up Routing Matrix

| Routing lane | Delta-T11 route |
| --- | --- |
| DO_NOW | Build local deterministic evidence-bundle helpers and tests only. |
| SEPARATE_RUNTIME_TRANCHE | Wrapper/proxy enforcement, direct interception, MCP registration, queues, daemons, and provider/live proof. |
| STRATEGIC_OPERATOR_DECISION | Public publication strategy and external evaluator package scope. |
| OUT_OF_SCOPE | Public-sync, production readiness, arbitrary commands, EDIT/COMMIT execution, and CVF Web actions. |
| RESOLVED_BY_DESIGN | Source verification and claim-boundary blocks prevent bounded evidence from becoming universal-control proof. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| T11-RIH-001 | External review context | context packets do not authorize public-sync/readiness | OUT_OF_SCOPE | Could the bundle be read as public readiness? | PASS - forbidden scope and claim matrix require `NOT_CLAIMED`. |
| T11-RIH-002 | T10 integrity readout | all-valid applies only to supplied records/readout | DO_NOW | Could all-valid imply universal action interception? | PASS - T11 requires separate not-claimed interception rows. |
| T11-RIH-003 | Delta claim boundary | provider/live and public-sync remain parked | SEPARATE_RUNTIME_TRANCHE | Could reviewer markdown imply live proof? | PASS - AC3/AC4 forbid it. |

## Legacy Absorption Coverage Index Disposition

Disposition: NOT_APPLICABLE_WITH_REASON.

Reason: Delta-T11 uses current governed T9/T10 source files and the governed
external-agent review reference folder. It does not reopen `.private_reference/legacy/`,
does not claim legacy absorption coverage, and does not require a legacy
coverage-index row for this bounded evidence-bundle dispatch.

## Source Verification Block

| Claimed item | Verification type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Durable audit contract constant exists. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-store.ts` | line 11 | `DURABLE_EXECUTION_AUDIT_CONTRACT` | Delta-T9 durable store | ACCEPT |
| Durable audit record interface exists. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-store.ts` | line 28 | `DurableExecutionAuditRecord` | Delta-T9 durable store | ACCEPT |
| Durable records set mandatory invocation proof false. | LITERAL_INVARIANT | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-store.ts` | lines 43, 109, and 138 | `mandatoryInvocationProved` | `DurableExecutionAuditRecord`; `buildDurableAuditRecord`; `validateDurableRecordBoundary` | ACCEPT |
| Durable records set direct interception proof false. | LITERAL_INVARIANT | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-store.ts` | lines 44, 110, and 141 | `directInterceptionProved` | `DurableExecutionAuditRecord`; `buildDurableAuditRecord`; `validateDurableRecordBoundary` | ACCEPT |
| Durable store exposes read records behavior. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-store.ts` | lines 151 and 162 | `JsonDurableExecutionAuditStore`; `readRecords` | Delta-T9 durable store | ACCEPT |
| Durable audit integrity readout contract exists. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-readout.ts` | line 10 | `DURABLE_AUDIT_INTEGRITY_READOUT_CONTRACT` | Delta-T10 integrity readout | ACCEPT |
| Durable audit integrity readout interface exists. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-readout.ts` | line 36 | `DurableAuditIntegrityReadout` | Delta-T10 integrity readout | ACCEPT |
| Durable audit integrity readout records findings and all-valid verdict. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-readout.ts` | lines 43 and 46 | `findings`; `allValid` | `DurableAuditIntegrityReadout` | ACCEPT |
| Durable audit integrity readout keeps mandatory invocation and direct interception false. | LITERAL_INVARIANT | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-readout.ts` | lines 44, 45, 207, and 208 | `mandatoryInvocationProved`; `directInterceptionProved` | `DurableAuditIntegrityReadout`; `buildDurableAuditIntegrityReadout` | ACCEPT |
| Durable audit integrity readout can be built from supplied records. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-readout.ts` | line 181 | `buildDurableAuditIntegrityReadout` | Delta-T10 integrity readout | ACCEPT |
| Durable audit integrity readout can be built from supplied JSONL text. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-execution-audit-readout.ts` | lines 214 and 238 | `parseDurableAuditJsonlLines`; `buildDurableAuditIntegrityReadoutFromJsonl` | Delta-T10 integrity readout | ACCEPT |
| External review context preparation does not authorize public-sync or readiness claims. | LITERAL_INVARIANT | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_REVIEW_CONTEXT_STANDARD.md` | `## Scope / Target / Owner Boundary`; `## Claim Boundary` | external review context boundary | external agent review context standard | ACCEPT |
| External knowledge intake chain requires fresh GC-018 and work order before implementation. | LITERAL_INVARIANT | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | `## Mandatory Chain` | external knowledge intake chain | external knowledge absorption chain map | ACCEPT |
| Delta-T10 completion is closed and records focused/full/build gate evidence. | VALUE_SET | `docs/reviews/CVF_DELTA_T10_DURABLE_AUDIT_INTEGRITY_READOUT_COMPLETION_2026-06-19.md` | `Status: CLOSED_PASS_BOUNDED`; test evidence sections | Delta-T10 completion | Delta-T10 completion packet | ACCEPT |

## New Doc-Only Fields

| Item | Shape | Purpose |
| --- | --- | --- |
| `DURABLE_AUDIT_EVIDENCE_BUNDLE_CONTRACT` | literal string | stable evidence bundle contract identity |
| `DurableAuditEvidenceBundle` | typed summary | source refs, counts, claim matrix, and boundary notes |
| `DurableAuditEvidenceBundleClaim` | typed claim row | disposition, evidence basis, and reviewer-facing explanation |
| `DurableAuditEvidenceBundleClaimDisposition` | string union | `PROVED`, `BOUNDED`, `REJECTED`, `NOT_CLAIMED` |
| `buildDurableAuditEvidenceBundle` | pure function | summarize supplied records and readout |
| `renderDurableAuditEvidenceBundleMarkdown` | pure helper, if implemented | deterministic secret-safe markdown readout |

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
| durable store target | N/A with reason: T11 bundle must not add a new store by default |
| dated execution artifacts | this GC-018, work order, worker return, evidence JSON |
| generated aggregate | N/A with reason: none added by Claude |
| index | N/A with reason: no MCP/server registration authorized |

## Current Runtime Freshness Verification

| Surface | Evidence |
| --- | --- |
| base | dispatch base `66cb8494` |
| existing durable store | Delta-T9 module exists under `src/audit/` |
| existing integrity readout | Delta-T10 module exists under `src/audit/` |
| evidence bundle | planned files absent at dispatch |
| live/provider | N/A with reason: forbidden and unnecessary |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order owner | Evidence |
| --- | --- | --- |
| durable execution audit continuation requires fresh source-verified work | Codex dispatch | matching GC-018 and this source verification block |
| reviewer-facing bounded readout | Claude worker | evidence bundle fields, tests, worker return |
| local gate evidence | Claude worker | focused/full/build/worker-return fast gate results |
| no wrapper/proxy or direct interception | Claude worker and Codex reviewer | claim boundary fields and Delta checker compatibility |
| no public/readiness/universal-control claim | Claude worker and Codex reviewer | bundle-only contract and closure evidence |

## Work-Order Fulfillment Manifest

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
| --- | --- | --- |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-audit-evidence-bundle.ts` | Yes | durable audit evidence bundle implementation |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-audit-evidence-bundle.test.ts` | Yes | focused regression and boundary tests |
| `docs/reviews/CVF_DELTA_T11_DURABLE_AUDIT_EVIDENCE_BUNDLE_EXTERNAL_REVIEWER_READOUT_COMPLETION_2026-06-19.md` | Yes | Claude no-commit return packet |
| `docs/reviews/evidence/delta-t11-durable-audit-evidence-bundle-external-reviewer-readout-2026-06-19.json` | Yes | machine-readable worker evidence |

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
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-audit-evidence-bundle.ts` | ABSENT | ABSENT | N/A |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-audit-evidence-bundle.test.ts` | ABSENT | ABSENT | N/A |
| `docs/reviews/CVF_DELTA_T11_DURABLE_AUDIT_EVIDENCE_BUNDLE_EXTERNAL_REVIEWER_READOUT_COMPLETION_2026-06-19.md` | ABSENT | ABSENT | N/A |
| `docs/reviews/evidence/delta-t11-durable-audit-evidence-bundle-external-reviewer-readout-2026-06-19.json` | ABSENT | ABSENT | N/A |

## Required Proof Manifest

| Proof | Path | Required literal | Required at handoff |
| --- | --- | --- | --- |
| contract identity | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-audit-evidence-bundle.ts` | `DURABLE_AUDIT_EVIDENCE_BUNDLE_CONTRACT` | Yes |
| bundle summary | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-audit-evidence-bundle.ts` | `DurableAuditEvidenceBundle` | Yes |
| claim matrix | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-audit-evidence-bundle.ts` | `DurableAuditEvidenceBundleClaim` | Yes |
| bounded claim check | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-audit-evidence-bundle.ts` | `NOT_CLAIMED` | Yes |
| secret safety | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-audit-evidence-bundle.test.ts` | `secret-safe reviewer readout` | Yes |
| no-commit return | `docs/reviews/CVF_DELTA_T11_DURABLE_AUDIT_EVIDENCE_BUNDLE_EXTERNAL_REVIEWER_READOUT_COMPLETION_2026-06-19.md` | `COMPLETE_PENDING_REVIEW` | Yes |

## Allowed Changed Set

Claude may leave only the required artifact manifest paths plus this work order
if status/evidence rows need worker-return updates. Claude must not stage,
commit, push, public-sync, or edit session continuity.

## Acceptance Criteria

| ID | Criterion | Worker evidence |
| --- | --- | --- |
| AC1 | Valid supplied Delta-T9 records plus a valid supplied Delta-T10 readout produce a deterministic bundle with contract version, counts, source refs, and claim matrix. | focused test |
| AC2 | Empty input, invalid readout, or findings cannot be summarized as proof; affected claim rows are `REJECTED` or `NOT_CLAIMED`. | focused test |
| AC3 | Mandatory invocation, direct interception, provider/live, public-sync, readiness, and universal-control rows remain `NOT_CLAIMED`. | focused test/source |
| AC4 | The markdown readout, if implemented, is deterministic, reviewer-readable, and secret-safe. | focused test |
| AC5 | Bundle output distinguishes `PROVED`, `BOUNDED`, `REJECTED`, and `NOT_CLAIMED` without collapsing bounded local evidence into universal control. | focused test |
| AC6 | Focused tests, MCP full test suite, build, and worker-return fast gate pass before handoff. | command evidence |

## Verification Commands

```powershell
cd EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER
npx vitest run src/audit/durable-audit-evidence-bundle.test.ts --reporter verbose
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

Expected result: PASS. Return `BLOCKED` if the repo is dirty or the gate failure
is outside this work order's allowed remediation scope.

## Write Ownership

Claude owns only:

- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-audit-evidence-bundle.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/durable-audit-evidence-bundle.test.ts`
- `docs/reviews/CVF_DELTA_T11_DURABLE_AUDIT_EVIDENCE_BUNDLE_EXTERNAL_REVIEWER_READOUT_COMPLETION_2026-06-19.md`
- `docs/reviews/evidence/delta-t11-durable-audit-evidence-bundle-external-reviewer-readout-2026-06-19.json`
- this work order, only for worker-return status/evidence updates

Write mode: create-only for new source/test/review/evidence files; limited
modify-listed for this work order.

## Execution Plan

1. Capture `executionBaseHead` and verify clean starting status.
2. Run pre-implementation autorun gate.
3. Implement durable audit evidence bundle under `src/audit/` only.
4. Add focused tests for valid evidence, empty input, invalid readout/finding
   rows, `NOT_CLAIMED` forbidden-expansion rows, secret-safe markdown, and
   deterministic ordering.
5. Run focused tests, full MCP tests, build, worker-return fast gate, status,
   and diff.
6. Create worker-return packet and evidence JSON.
7. Return uncommitted worker packet to Codex, or `BLOCKED`.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex dispatcher |
| Provider or surface | Codex / local workspace |
| Session or invocation | Delta-T11 dispatch, 2026-06-19 |
| Working directory | repository root |
| Command or tool surface | startup reads, source verification, apply_patch, pre-dispatch gates |
| Target paths | this work order and matching Delta-T11 GC-018 |
| Allowed scope source | current instruction, this work order, matching Delta-T11 GC-018 |
| Before status evidence | clean worktree at dispatch base `66cb8494` |
| After status evidence | dispatch `git status --short` |
| Diff evidence | dispatch `git diff --name-status` |
| Approval boundary | Codex may create dispatch artifacts only; Claude implements no-commit |
| Claim boundary | evidence bundle only; no runtime interception or universal control |
| Agent type | dispatcher under `MULTI_AGENT_MULTI_ROLE` |
| Invocation ID | `delta-t11-durable-audit-evidence-bundle-external-reviewer-readout-dispatch-2026-06-19` |
| Expected manifest | `docs/baselines/CVF_GC018_DELTA_T11_DURABLE_AUDIT_EVIDENCE_BUNDLE_EXTERNAL_REVIEWER_READOUT_2026-06-19.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_DELTA_T11_DURABLE_AUDIT_EVIDENCE_BUNDLE_EXTERNAL_REVIEWER_READOUT_FOR_CLAUDE_2026-06-19.md` |
| Actual changed set | `docs/baselines/CVF_GC018_DELTA_T11_DURABLE_AUDIT_EVIDENCE_BUNDLE_EXTERNAL_REVIEWER_READOUT_2026-06-19.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_DELTA_T11_DURABLE_AUDIT_EVIDENCE_BUNDLE_EXTERNAL_REVIEWER_READOUT_FOR_CLAUDE_2026-06-19.md` |
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
- the bundle implies it observed external action occurrence by itself;
- empty input, invalid readout, or readout findings can be summarized as proof;
- secret-like values are echoed raw in readout output;
- mandatory invocation, direct interception, provider/live, external readiness,
  deployment readiness, release readiness, production readiness, or universal
  governed-coding control is claimed;
- worker committed, pushed, public-synced, or edited session continuity.

## Return-To-Orchestrator Conditions

Claude must return `BLOCKED` without continuing if:

- the pre-implementation gate fails outside allowed scope;
- source contracts are missing or materially changed from this packet;
- implementation requires editing forbidden paths;
- tests require provider/live keys, public-sync, or secrets;
- evidence bundle cannot be made deterministic, secret-safe, and bounded.

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

## Scope Expansion Checkpoint

No human checkpoint applies inside the bounded worker scope. Escalation is
required for wrapper/proxy enforcement, direct interception, EDIT/COMMIT
execution, provider/live proof, public-sync, secrets/quota, session continuity
edits by Claude, or claim-boundary expansion.

## Worker Autonomy / No-Question Rule

Claude should proceed with non-destructive work inside Allowed scope.
Allowed-scope test or lint failures are mandatory remediation and must be
rerun. Escalate only for scope expansion, live/provider proof, public-sync,
secrets, forbidden paths, destructive actions, or claim-boundary changes.

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
| Work order status | this work order | `Status: DISPATCHED` | PENDING |
| Completion or reviewer artifact | `docs/reviews/CVF_DELTA_T11_DURABLE_AUDIT_EVIDENCE_BUNDLE_EXTERNAL_REVIEWER_READOUT_COMPLETION_2026-06-19.md` | pending worker return | PENDING |
| Roadmap state | N/A with reason: no roadmap status edit authorized at dispatch | no roadmap mutation authorized | N/A with reason |
| Registry JSON | N/A with reason: not corpus intake | no registry mutation authorized | N/A with reason |
| Registry Markdown | N/A with reason: no registry edit authorized | no registry mutation authorized | N/A with reason |
| External evidence digest | N/A with reason: no external evidence | repo-local source/test evidence only | N/A with reason |
| System loop interlock | durable audit evidence bundle source/tests | pending worker return | PENDING |
| Session continuity | active state, memory, and handoff | reviewer-owned during accepted worker-return closure conversion | PENDING |

## Acceptance Receipt Assertion Matrix

| Required value | Expected value | Status |
| --- | --- | --- |
| commit mode | `WORKER_MUST_NOT_COMMIT`; Codex commits only after review | PENDING |
| runtime scope | bounded new audit evidence-bundle module only | PENDING |
| provider/live scope | false | PENDING |
| public-sync | false | PENDING |
| direct interception claim | false | PENDING |
| universal governed-coding claim | false | PENDING |

## Claim Boundary

Delta-T11 may prove only a bounded deterministic evidence bundle and external
reviewer readout for supplied Delta-T9/T10 durable audit artifacts. It does not
prove that all actions pass through CVF, that external actions are observed,
that direct IDE/shell/git/filesystem activity is intercepted, that public
artifacts were updated, or that CVF has universal governed-coding control.

## Operator Checkpoint

No checkpoint applies inside the bounded worker scope. A checkpoint is required
only for forbidden scope expansion listed above.
