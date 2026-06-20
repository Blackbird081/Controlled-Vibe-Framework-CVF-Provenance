# CVF Agent Work Order - AAF-T5 Worker Experience Retrospective Capture Foundation

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-20

docType: work_order

dispatchBaseHead: 8f8bc2d5

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Worker. Reviewer/closer is a separate role after worker return.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_AAF_T5_WORKER_EXPERIENCE_RETROSPECTIVE_CAPTURE_FOUNDATION_FOR_WORKER_2026-06-20.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: confirm with `git rev-parse --short HEAD` at worker start.

Current-time notes: AAF-T4 is closed at material commit `518d4131` and session
sync commit `8f8bc2d5`. The operator and advisory chain have reclassified the
next step: AAF-T5 is not the Guard Orientation Read-Receipt Gate. AAF-T5 is the
Worker Experience Retrospective Capture Foundation. AAF-T6 may later implement
the read-receipt gate. AAF-T7 may later harden helper/index friction.

Do-not-misread notes: do not open AAF-T6, AAF-T7, automated provider selection,
runtime provider routing, provider/API calls, live proof, secrets/quota use,
public-sync, runtime product behavior, MCP execution, wrapper/proxy
enforcement, direct IDE/shell/git/filesystem interception, arbitrary command
execution, EDIT/COMMIT execution, queue/daemon, watcher, readiness,
full-hook equivalence, cost optimization, speed claim, or universal
governed-coding-control claims.

Role-neutrality note: normative instructions must name roles and artifact
classes, not a specific agent/provider/model as the required worker.

Required first actions: read this work order, read the AAF-T5 GC-018 baseline,
read the Codex classification, read the three advisory packets, read the source
files named in the Source Verification Block, confirm actual
`executionBaseHead`, and inspect current `git status --short` before editing.

Return contract: return `COMPLETE_PENDING_REVIEW` with the uncommitted artifacts
named in Required Deliverables, actual `executionBaseHead`, actual
`git status --short`, focused test and gate evidence, and no commit. If blocked,
return `BLOCKED_WITH_REASON` and name the exact source or gate that blocked the
work.

This AAF-T5 worker return must self-host the new convention by including either
the structured `WORKER_EXPERIENCE_RETRO` block or the exact asserting
`WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` line defined below.

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | two roles across phases: dispatch author creates packet; worker creates standard/checker/helper/test artifacts; reviewer/closer reviews and commits if accepted |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=8f8bc2d5`; `executionBaseHead` confirmed by worker; `closureBaseHead` set by reviewer before closure commit |
| changedSetScope(phase) | worker changes only Required Deliverables; reviewer/closer owns status/closure/session-sync if accepted |
| traceScope(phase, actor) | one worker-return trace covers pending AAF-T5 artifacts; one reviewer trace covers review/closure if accepted |
| commitOwner(phase) | worker commits nothing (`WORKER_MUST_NOT_COMMIT`); reviewer/closer owns any material/closure/session-sync commit |
| crossBatchIsolation | do not mix AAF-T5 with AAF-T6, AAF-T7, CGE-T3, ACE-R1, runtime/provider/live, MCP, public-sync, automated provider selection, or direct-interception work |
| Before status evidence | clean worktree at dispatch base `8f8bc2d5` before the advisory packets and AAF-T5 dispatch artifacts were added; current dispatch batch intentionally includes those files, plus recurring Windows global git-ignore permission warning |
| nextMoveSurfaces | reviewer/closer updates next-move surfaces only after review if mode or next allowed move changes |
| Closer designation | reviewer/closer role is the designated closer |

## Reviewer Closure Conversion

completionReviewPath:
`docs/reviews/CVF_AAF_T5_WORKER_EXPERIENCE_RETROSPECTIVE_CAPTURE_FOUNDATION_COMPLETION_2026-06-20.md`

reviewerOwnedClosurePaths:

- `docs/reviews/CVF_AAF_T5_WORKER_EXPERIENCE_RETROSPECTIVE_CAPTURE_FOUNDATION_COMPLETION_2026-06-20.md`
- this work order status/checklist/closure package if accepted;
- session front-door/state/handoff paths only if reviewer/closer changes
  current mode or next allowed move after accepting the worker return.

The closure packet is reviewer-owned. The execution role must not mark the work
closed.

## Purpose

Implement the AAF-T5 worker-experience retrospective capture foundation so CVF
can learn from worker friction even when a worker passes all gates.

The implementation should add a small, deterministic token requirement for
self-declared worker-return artifacts, plus helper diagnostics and hook-chain
enforcement. The goal is to move useful friction signals from chat-only
operator/reviewer questioning into the governed return packet itself.

## Agent Roles

| Role | Owner |
|---|---|
| Operator | project authority and scope approval |
| Dispatcher | dispatch author role |
| Worker | implementation role for AAF-T5 artifacts |
| Reviewer | review role after worker return |
| Closer | closer role after acceptance |
| Session-sync steward | session-sync steward role when session-sync is required |

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-20 authorization to proceed after advisory response | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | ACCEPT |
| AAF-T5 GC-018 | `docs/baselines/CVF_GC018_AAF_T5_WORKER_EXPERIENCE_RETROSPECTIVE_CAPTURE_FOUNDATION_2026-06-20.md` | ACCEPT |
| Codex classification | `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_T5_T6_T7_CODEX_CLASSIFICATION_2026-06-20.md` | ACCEPT |
| Original worker-experience proposal | `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_AND_T5_PROPOSAL_FOR_CODEX_2026-06-20.md` | ADVISORY_INPUT_ACCEPTED |
| Codex rebuttal | `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_AND_T5_PROPOSAL_CODEX_REBUTTAL_2026-06-20.md` | CLASSIFICATION_INPUT |
| Returned advisory response | `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_AND_T5_PROPOSAL_CLAUDE_REBUTTAL_RESPONSE_2026-06-20.md` | ADVISORY_INPUT_ACCEPTED |
| AAF-T4 completion | `docs/reviews/CVF_AAF_T4_PROJECT_ROLE_PROVIDER_DELEGATION_ENVELOPE_COMPLETION_2026-06-20.md` | ACCEPT |
| AAF helper source | `governance/compat/run_agent_automation_assist.py` | ACCEPT |
| Commit steward source | `governance/compat/run_agent_commit_steward_preflight.py` | ACCEPT |
| Worker-return fast gate | `governance/compat/run_worker_return_fast_gate.py` | ACCEPT |
| Local hook chain | `governance/compat/run_local_governance_hook_chain.py` | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- create `docs/reference/worker_experience_retrospective/README.md`;
- create `governance/compat/check_worker_experience_retrospective.py`;
- create `governance/compat/test_check_worker_experience_retrospective.py`;
- update `governance/compat/run_agent_automation_assist.py` only to report
  missing or malformed worker-experience retrospective tokens earlier;
- update `governance/compat/test_run_agent_automation_assist.py` only for the
  helper changes;
- update `governance/compat/run_local_governance_hook_chain.py` only to wire
  the checker into reviewer-fast, pre-commit, and pre-push;
- update `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` only
  to route worker-experience retrospective lookup;
- create `docs/reviews/CVF_AAF_T5_WORKER_EXPERIENCE_RETROSPECTIVE_CAPTURE_FOUNDATION_WORKER_RETURN_2026-06-20.md`.

Forbidden scope:

- no edits to closed AAF-T1/T2/T3/T4 artifacts;
- no edits to `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`,
  `AGENT_HANDOFF_V20_2026-06-19.md`, `AGENTS.md`, generated session state, root
  startup routers, public-sync, `.github/**`, dependency manifests,
  `EXTENSIONS/**`, product runtime, web UI, MCP packages, or unrelated tests;
- no implementation of AAF-T6 Guard Orientation Read-Receipt Gate;
- no implementation of AAF-T7 helper/index friction hardening, except that
  AAF-T5 may record the `KEYWORD_TRAP` and `ENUM_OR_TOKEN_MISMATCH` enum values
  and must preserve current `push` behavior;
- no provider/model addition, concrete provider binding, automated provider
  selection, runtime provider routing, provider/API call, live proof,
  secrets/quota use, dependency setup, CodeGraph setup/init, watcher/daemon,
  queue, background service, or CVF Web action execution;
- no direct IDE/shell/git/filesystem interception claim;
- no readiness, production, public release, universal speed, cost optimization,
  full-hook equivalence, or universal governed-coding-control claim.

Risk ceiling: R2 governance helper/checker implementation.

## Required First Reads

The worker must read these before editing:

- `docs/baselines/CVF_GC018_AAF_T5_WORKER_EXPERIENCE_RETROSPECTIVE_CAPTURE_FOUNDATION_2026-06-20.md`
- `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_T5_T6_T7_CODEX_CLASSIFICATION_2026-06-20.md`
- `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_AND_T5_PROPOSAL_FOR_CODEX_2026-06-20.md`
- `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_AND_T5_PROPOSAL_CODEX_REBUTTAL_2026-06-20.md`
- `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_AND_T5_PROPOSAL_CLAUDE_REBUTTAL_RESPONSE_2026-06-20.md`
- `docs/reviews/CVF_AAF_T4_PROJECT_ROLE_PROVIDER_DELEGATION_ENVELOPE_COMPLETION_2026-06-20.md`
- `governance/compat/run_agent_automation_assist.py`
- `governance/compat/test_run_agent_automation_assist.py`
- `governance/compat/run_agent_commit_steward_preflight.py`
- `governance/compat/run_worker_return_fast_gate.py`
- `governance/compat/run_local_governance_hook_chain.py`
- `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`

## Pre-Flight Checks

Before implementation, the worker must run or record:

```powershell
git rev-parse --short HEAD
git status --short
```

If the worktree contains unrelated dirty paths, the worker must preserve them
and avoid editing outside the Required Deliverables.

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| `docs/reference/worker_experience_retrospective/README.md` | worker | create within AAF-T5 scope |
| `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | worker | modify only to route worker-experience retrospective lookup |
| `governance/compat/check_worker_experience_retrospective.py` | worker | create |
| `governance/compat/test_check_worker_experience_retrospective.py` | worker | create |
| `governance/compat/run_agent_automation_assist.py` | worker | modify only for worker-experience diagnostics |
| `governance/compat/test_run_agent_automation_assist.py` | worker | modify only for worker-experience diagnostics |
| `governance/compat/run_local_governance_hook_chain.py` | worker | modify only to wire the checker |
| `docs/reviews/CVF_AAF_T5_WORKER_EXPERIENCE_RETROSPECTIVE_CAPTURE_FOUNDATION_WORKER_RETURN_2026-06-20.md` | worker | create only |
| Any other path | Not worker-owned | forbidden unless a revised work order authorizes it |

## Core Guard Self-Protection Authorization

AAF-T5 authorizes a new governance checker and local hook-chain wiring, bounded
to worker-experience retrospective capture. It does not authorize edits to root
startup routers, session state, active handoff, public-sync, product runtime, or
provider/live paths.

| Field | Disposition |
|---|---|
| Authorized guard-maintenance scope | create `check_worker_experience_retrospective.py`, focused tests, AAF helper diagnostics, and local hook-chain wiring only |
| Protected paths | authorized protected paths: `governance/compat/check_worker_experience_retrospective.py`, `governance/compat/test_check_worker_experience_retrospective.py`, `governance/compat/run_agent_automation_assist.py`, `governance/compat/test_run_agent_automation_assist.py`, `governance/compat/run_local_governance_hook_chain.py`; forbidden protected paths: `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF_V20_2026-06-19.md`, `AGENTS.md`, public-sync, product runtime, provider/live paths, and closed AAF-T1/T2/T3/T4 artifacts |
| Operator authorization | 2026-06-20 operator approved turning the worker-experience finding into AAF-T5 automation/helper foundation work |
| Rollback boundary | revert AAF-T5 checker/helper/hook/test/reference changes only; do not modify closed predecessor artifacts or session state during worker execution |

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | operator-originated AAF worker-experience blind-spot finding plus returned advisory response |
| Route | `MULTI_AGENT_SINGLE_ROLE` |
| risk sensitivity | R2; governance helper/checker implementation |
| selected role route | `MULTI_AGENT_SINGLE_ROLE` |
| Worker role | worker creates standard, checker, helper diagnostics, hook wiring, tests, and worker return |
| Reviewer role | reviewer/closer reviews, commits, closes, and session-syncs if accepted |
| Commit mode | `WORKER_MUST_NOT_COMMIT` |
| Checkpoint disposition | satisfied for dispatch; fresh checkpoint required for T6, T7, runtime, provider/live, public-sync, or claim-boundary expansion |
| escalation condition | scope expansion, forbidden paths, provider/live, public-sync, secrets/quota, dependency setup, destructive actions, runtime implementation, AAF-T6/T7 implementation, or claim-boundary change |

## Worker Autonomy / No-Question Rule

The worker must repair and rerun gate failures inside Allowed scope. The worker
must stop and return `BLOCKED_WITH_REASON` only for scope expansion, forbidden
paths, live/provider proof, public-sync, secret/quota consumption, dependency
install, destructive actions, runtime implementation, AAF-T6/T7 scope, or
claim-boundary changes.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | stable reference folder plus governance compat checker/test/helper wiring |
| Storage decision | create `README.md` as stable reference front door; checker remains deterministic source |
| Existing aggregate impact | none |
| Generated state impact | none during worker execution |
| Durable governance boundary | retrospective token is artifact-level evidence, not hidden state store |

## Required Deliverables

The worker must leave exactly these uncommitted artifact changes unless a gate
requires an in-scope focused test adjustment:

- `docs/reference/worker_experience_retrospective/README.md`
- `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`
- `governance/compat/check_worker_experience_retrospective.py`
- `governance/compat/test_check_worker_experience_retrospective.py`
- `governance/compat/run_agent_automation_assist.py`
- `governance/compat/test_run_agent_automation_assist.py`
- `governance/compat/run_local_governance_hook_chain.py`
- `docs/reviews/CVF_AAF_T5_WORKER_EXPERIENCE_RETROSPECTIVE_CAPTURE_FOUNDATION_WORKER_RETURN_2026-06-20.md`

## Required Worker Experience Token Contract

Eligible worker-return artifacts must include exactly one of the following.

Structured retrospective form:

```text
WORKER_EXPERIENCE_RETRO:
frictionLevel: NONE|LOW|MEDIUM|HIGH|BLOCKING
frictionType: NONE|GATE_SURPRISE|SCOPE_AMBIGUITY|SOURCE_DISCOVERY|WORKTREE_CONTAMINATION|HELPER_GAP|LATENCY|KEYWORD_TRAP|ENUM_OR_TOKEN_MISMATCH|OTHER
observedStep: short text
preventiveControlCandidate: NONE|INDEX_UPDATE|HELPER_DIAGNOSTIC|CHECKER|WORK_ORDER_TEMPLATE|STANDARD_UPDATE|DEFER
```

No-friction escape hatch:

```text
WORKER_EXPERIENCE_RETRO_NA_WITH_REASON: no friction beyond normal gates; no gate surprise, no helper gap, no worktree contamination this return
```

The AAF-T5 worker-return artifact itself must include one of these forms.

## Checker Requirements

The new checker must:

- inspect changed Markdown files in governed worker-return locations;
- apply only to self-declared worker-return artifacts;
- accept `Self-declared worker-return artifact: yes` as the explicit marker;
- otherwise require both `Status: COMPLETE_PENDING_REVIEW` or
  `Status: BLOCKED_WITH_REASON` and a `Responds to work order:` line;
- exclude `docType: review_context`, completion reviews, reference standards,
  baselines, work orders, session-sync files, and advisory classification
  packets;
- require exactly one accepted token form;
- validate all enum values exactly;
- reject empty `observedStep` in structured retrospective form;
- reject bare `WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` without the exact
  asserting reason;
- provide path-specific diagnostics;
- support `--base`, `--head`, and `--enforce`.

## Helper Requirements

The AAF helper must:

- remain read-only;
- report missing or malformed worker-experience retrospective tokens for
  eligible worker-return artifacts before reviewer-fast when possible;
- include a concise next-action recommendation;
- avoid false positives on advisory/classification packets that merely discuss
  worker returns.

Do not add `push` to helper modes in AAF-T5. The current `push` omission is
deferred to AAF-T7 for an intentional drift test or comment.

## Test And Gate Requirements

The worker must run or record:

```powershell
python -m unittest governance.compat.test_check_worker_experience_retrospective governance.compat.test_run_agent_automation_assist
python governance/compat/run_agent_automation_assist.py --base 8f8bc2d5 --head HEAD --json --enforce
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_worker_experience_retrospective.py --pytest-target governance/compat/test_run_agent_automation_assist.py
```

If a focused test target name differs after implementation, use the matching
repo-local unittest/pytest invocation and record the exact command.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| AAF-T4 read receipt is voluntary and only a future gate candidate | `docs/reviews/CVF_AAF_T4_PROJECT_ROLE_PROVIDER_DELEGATION_ENVELOPE_COMPLETION_2026-06-20.md` | lines 69-72, 102-103, 118, 150 | read-receipt candidate | AAF-T4 completion | ACCEPT |
| Original proposal identifies helper/steward `push` mismatch | `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_AND_T5_PROPOSAL_FOR_CODEX_2026-06-20.md` | lines 83-88 | `push` | advisory proposal | ACCEPT |
| Original proposal requests helper early failure before reviewer-fast | `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_AND_T5_PROPOSAL_FOR_CODEX_2026-06-20.md` | lines 145-150 | helper early failure | advisory proposal | ACCEPT |
| Codex rebuttal proposes `WORKER_EXPERIENCE_RETRO` | `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_AND_T5_PROPOSAL_CODEX_REBUTTAL_2026-06-20.md` | line 84 | `WORKER_EXPERIENCE_RETRO` | Codex rebuttal | ACCEPT |
| Codex rebuttal proposes `WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` | `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_AND_T5_PROPOSAL_CODEX_REBUTTAL_2026-06-20.md` | lines 94, 164-165 | `WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` | Codex rebuttal | ACCEPT |
| Codex rebuttal classifies helper/steward mode drift as AAF-T7 | `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_AND_T5_PROPOSAL_CODEX_REBUTTAL_2026-06-20.md` | lines 145, 220 | `push` | Codex rebuttal | ACCEPT |
| Returned response accepts T5/T6/T7 split | `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_AND_T5_PROPOSAL_CLAUDE_REBUTTAL_RESPONSE_2026-06-20.md` | lines 28-34, 162 | tranche split | advisory response | ACCEPT |
| Returned response recommends enum additions | `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_AND_T5_PROPOSAL_CLAUDE_REBUTTAL_RESPONSE_2026-06-20.md` | lines 69, 74, 165 | `KEYWORD_TRAP`; `ENUM_OR_TOKEN_MISMATCH` | advisory response | ACCEPT |
| Returned response proposes exact asserting NA token | `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_AND_T5_PROPOSAL_CLAUDE_REBUTTAL_RESPONSE_2026-06-20.md` | line 91 | `WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` | advisory response | ACCEPT |
| Returned response proposes worker-return marker | `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_AND_T5_PROPOSAL_CLAUDE_REBUTTAL_RESPONSE_2026-06-20.md` | lines 125-144 | self-declared worker-return artifact | advisory response | ACCEPT |
| Returned response describes this packet class as a worked example of the T5 channel | `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_AND_T5_PROPOSAL_CLAUDE_REBUTTAL_RESPONSE_2026-06-20.md` | lines 152-153 | worker experience signal | advisory response | ACCEPT |
| AAF helper is read-only and never pushes or mutates state | `governance/compat/run_agent_automation_assist.py` | line 11 | read-only helper boundary | AAF helper | ACCEPT |
| AAF helper has mode vocabulary and worker-return pattern | `governance/compat/run_agent_automation_assist.py` | lines 142, 161, 419, 670 | `ALLOWED_MODES`; `_WORKER_RETURN_RE` | AAF helper | ACCEPT |
| Commit steward supports `push`, which is not AAF-T5 helper scope | `governance/compat/run_agent_commit_steward_preflight.py` | lines 200, 273, 317 | `push` | commit steward | ACCEPT |
| Worker-return fast gate runs reviewer-fast and supports repeated focused targets | `governance/compat/run_worker_return_fast_gate.py` | lines 46-47, 84 | `--pytest-target` | worker-return fast gate | ACCEPT |
| Local hook chain has reviewer-fast, pre-commit, and pre-push lanes | `governance/compat/run_local_governance_hook_chain.py` | lines 24, 151, 155, 159, 384 | hook lanes | local governance hook chain | ACCEPT |

## New Doc-Only Fields

| Proposed item | Disposition |
|---|---|
| `WORKER_EXPERIENCE_RETRO` | new artifact-level worker-return token |
| `WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` | new artifact-level no-friction token |
| `frictionLevel` | new token field |
| `frictionType` | new token field |
| `observedStep` | new token field |
| `preventiveControlCandidate` | new token field |
| `Self-declared worker-return artifact: yes` | new explicit worker-return marker |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | returned output to finding classification to governed work order |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py` |
| Owner surface | worker-experience retrospective standard and checker |
| Disposition | ADAPT as CVF-owned governance helper foundation |
| Claim boundary | advisory inputs are not canonical authority until absorbed by Codex classification and this work order |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | AAF-T5 worker-experience retrospective capture implementation only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | deterministic local checker/helper/hook text inspection only |
| interceptionBoundary | no direct IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | retrospective capture standard, checker, helper diagnostic, tests, hook wiring |
| forbiddenExpansion | read-receipt gate, automated provider selection, runtime routing, provider/live proof, wrapper/proxy enforcement, direct interception, arbitrary commands, EDIT/COMMIT execution, public-sync, queue/daemon, watcher, readiness, full-hook equivalence, and universal control remain parked |

## Rescan Intelligence Hardening

- Original source artifact: operator worker-experience blind-spot finding and
  advisory response packets.
- Predecessor intake artifact:
  `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_AND_T5_PROPOSAL_CLAUDE_REBUTTAL_RESPONSE_2026-06-20.md`.
- Delta ledger status: `CHANGED_DISPOSITION` because AAF-T5 is worker-experience
  capture first; AAF-T6 and AAF-T7 are separate.
- Routing matrix status:
  - `DO_NOW`: implement AAF-T5 worker-experience capture foundation.
  - `RESOLVED_BY_DESIGN`: keep T5 as capture sensor while T6/T7 remain separate.
  - `DEFER`: AAF-T6 read-receipt gate.
  - `DEFER`: AAF-T7 helper/index hardening.
  - `SEPARATE_RUNTIME_TRANCHE`: runtime/provider/live/MCP/direct-interception scope.
  - `STRATEGIC_OPERATOR_DECISION`: CGE-T3 and ACE-R1 remain parked.
  - `OUT_OF_SCOPE`: runtime/provider/live/public-sync/direct interception.
- Semantic sampling status: `PARTIAL_TARGETED` to the advisory packets and
  source surfaces named above.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Disposition |
|---|---|
| UNCHANGED_FROM_INTAKE | Worker-experience friction remains governance-control-plane evidence. |
| CHANGED_DISPOSITION | AAF-T5 dispatch is worker-experience capture first, not read-receipt first. |
| NEW_FINDING | Worker-return packets need explicit experience token or exact no-friction assertion. |
| REMOVED_OR_REJECTED | Runtime/provider/live/public-sync/direct-interception scope remains rejected. |

### Follow-Up Routing Matrix

| Lane | Disposition |
|---|---|
| DO_NOW | Implement AAF-T5 standard, checker, helper diagnostics, tests, and hook wiring. |
| RESOLVED_BY_DESIGN | Keep T5 as a capture sensor and defer read receipt/helper drift. |
| DEFER | AAF-T6 Guard Orientation Read-Receipt Gate. |
| DEFER | AAF-T7 helper/index friction hardening. |
| SEPARATE_RUNTIME_TRANCHE | Runtime/provider/live/MCP/direct-interception work requires separate authorization. |
| STRATEGIC_OPERATOR_DECISION | CGE-T3 and ACE-R1 remain parked. |
| OUT_OF_SCOPE | Public readiness, production readiness, universal governed-coding control. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| AAF-T5-WO-RS1 | Operator finding | worker pass can hide friction | DO_NOW checker | Could this remain reviewer-only? | PASS_MACHINE_CHANNEL_REQUIRED |
| AAF-T5-WO-RS2 | Returned advisory Q2 | KEYWORD_TRAP and ENUM_OR_TOKEN_MISMATCH recur | DO_NOW enum | Could enum growth be deferred? | PASS_BOUND_ENUM_INCLUDED |
| AAF-T5-WO-RS3 | Returned advisory Q4 | `push` drift exists | DEFER AAF-T7 | Could worker fix helper modes now? | PASS_SCOPE_DEFERRED |

## Corpus Completeness And Report Integrity

Corpus task class: PARTIAL_TARGETED

Corpus root: `docs/reviews`, `docs/baselines`, `docs/work_orders`,
`governance/compat`, and `docs/reference` files named by Required First Reads.

Snapshot time: 2026-06-20 dispatch authoring.

- Corpus task class: PARTIAL_TARGETED

- Corpus root: `docs/reviews`, `docs/baselines`, `docs/work_orders`,
  `governance/compat`, and `docs/reference` files named by Required First Reads.

- Snapshot time: 2026-06-20 dispatch authoring.

- Enumeration command: `rg --files --hidden --no-ignore docs/reviews docs/baselines docs/work_orders governance/compat docs/reference`

- Manifest artifact or inline manifest: inline Source Verification Block above.

- Manifest hash: N/A with reason: targeted dispatch packet, not a generated
  corpus manifest.

- Processing ledger artifact or inline ledger: inline Source Verification Block
  and Required First Reads.

- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.

- Reconciliation: manifest=inline Source Verification Block; ledger_terminal=READ for named source rows; exclusions=closed predecessor artifacts except cited AAF-T4 completion and forbidden runtime/provider/live/public-sync surfaces; unresolved=0.

- Unresolved files: 0.

- Declared exclusions: closed AAF-T1/T2/T3/T4 artifacts except cited AAF-T4
  completion; runtime/provider/live/public-sync surfaces.

- Unreadable or unsupported files: none observed.

- Aggregation check: bounded to AAF-T5 dispatch inputs.

- Drift check: worker must rerun gates after implementation.

- Output traceability: worker return must cite commands and actual
  `executionBaseHead`.

- Adversarial verification: avoid false positives on advisory packets that
  merely discuss worker-return vocabulary.

- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Finding-To-Governance Learning Disposition

Learning lane: `GOVERNANCE_CONTROL_PLANE`

Runtime/provider/cost learning lane: `N/A_WITH_REASON` - AAF-T5 changes
governance helper/checker scope only and does not change runtime, provider,
live, cost, token-budget, or public-sync behavior.

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Passing worker returns can hide useful friction | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | Implement AAF-T5 checker and helper diagnostic | handled by worker |
| Missing no-friction assertion can hide default-pasted NA | RULE_GAP | GOVERNANCE_CONTROL_PLANE | STANDARD_ADDED | Define exact asserting NA token in standard | handled by worker |
| Worker-return vocabulary in advisory packets can false-fire | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | Require self-declared worker-return boundary | handled by worker |
| Helper should reduce latency before reviewer-fast where possible | PHASE_GATE_PLACEMENT_GAP | GOVERNANCE_CONTROL_PLANE | PHASE_GATE_PLACEMENT_GAP | Add helper early diagnostic | handled by worker |
| Runtime/provider/cost applicability | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime/provider/cost behavior changed or claimed | handled |

## Epistemic Process Block

| Field | Disposition |
|---|---|
| Source class | operator finding plus source-checked advisory packets |
| Confidence | HIGH for existence of blind spot; MEDIUM for final enum coverage |
| Verification method | direct source reads, `rg -n` anchors, bounded source verification table |
| Known uncertainty | exact checker implementation details belong to worker within Allowed scope |
| Dissent handling | advisory response accepted T5/T6/T7 split and enum additions; `push` drift deferred to AAF-T7 |

## Worker Return Packet Shape Contract

The worker-return artifact must include:

- `Purpose`;
- `Scope / Methodology`;
- `Findings / Position`;
- `Risk / Corrective Action`;
- `Agent Operation Trace Block`;
- `Delta Execution Claim Boundary Control Block`;
- `External Knowledge Intake Routing`;
- `Rescan Intelligence Hardening`;
- `Corpus Completeness And Report Integrity`;
- `Finding-To-Governance Learning Disposition`;
- `Epistemic Process Block`;
- `Machine Closure Package`;
- `Status: COMPLETE_PENDING_REVIEW` or `Status: BLOCKED_WITH_REASON`;
- `Self-declared worker-return artifact: yes`;
- `Responds to work order:` with this work order path;
- `executionBaseHead`;
- `git status --short`;
- changed files;
- focused test and gate commands with PASS/BLOCKED evidence;
- Source Verification Block delta notes if implementation discovers source
  mismatch;
- `WORKER_EXPERIENCE_RETRO` structured form or exact
  `WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` asserting form;
- Public Export Disposition;
- Claim Boundary;
- no commit.

For any conditional block that does not apply, the worker must write
`N/A with reason` or `NOT_APPLICABLE_WITH_REASON` inside that block and state
why it does not apply.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | A stable worker-experience retrospective standard exists and routes eligible worker-return artifacts. |
| AC2 | A deterministic checker enforces the token on eligible worker-return artifacts and ignores advisory/classification packets. |
| AC3 | Focused checker tests cover pass, missing token, malformed enum, bare NA rejection, exact NA acceptance, explicit self-declaration, and advisory-packet exclusion. |
| AC4 | AAF helper reports missing or malformed worker-experience tokens early while remaining read-only. |
| AC5 | Local hook chain wires the checker into reviewer-fast, pre-commit, and pre-push. |
| AC6 | AAF-T5 worker return self-hosts the new token contract. |
| AC7 | No AAF-T6, AAF-T7, runtime/provider/live/public-sync/direct-interception scope is opened. |

## Execution Plan

1. Read required sources and record actual `executionBaseHead`.
2. Create the worker-experience reference standard.
3. Implement the checker and focused checker tests.
4. Add read-only AAF helper diagnostics.
5. Wire the checker into reviewer-fast, pre-commit, and pre-push.
6. Update operational reference routing.
7. Create the AAF-T5 worker return and self-host the new token.
8. Run required focused tests and worker-return fast gate.

## Evidence Requirements

Evidence must include actual `git status --short`, actual `executionBaseHead`,
changed file list, focused test commands, AAF helper result, worker-return fast
gate result, and the worker-experience token used in the worker return.

## Review Gate

Reviewer/closer must run reviewer-fast and focused tests before accepting the
worker return. Reviewer/closer must reject claims that open AAF-T6, AAF-T7,
runtime/provider/live/public-sync/direct-interception, readiness, or universal
control scope.

## Closure Checklist

| Item | Required disposition |
|---|---|
| Required deliverables present | PASS before closure |
| Worker return includes required token | PASS before closure |
| Focused tests pass | PASS before closure |
| Reviewer-fast passes | PASS before closure |
| Forbidden scope untouched | PASS before closure |
| Session-sync need assessed by reviewer | PASS or N/A with reason |

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when required deliverables are left
uncommitted with passing focused evidence. Return `BLOCKED_WITH_REASON` when an
in-scope remediation cannot clear a machine check or scope expansion would be
required.

## Operator Checkpoint

No further checkpoint is required for this AAF-T5 tranche. Fresh authorization
is required before any forbidden scope expansion listed in the Forbidden scope
section.

## Agent Operation Trace Block

| Field | Value |
|---|---|
| Actor | dispatch author role |
| Provider or surface | local workspace |
| Session or invocation | current Codex session |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | local file reads, `rg`, governance gates, `apply_patch` |
| Target paths | this work order |
| Allowed scope source | operator instruction and AAF-T5 GC-018 baseline |
| Before status evidence | clean worktree at dispatch base `8f8bc2d5` before advisory/dispatch additions |
| After status evidence | AAF-T5 dispatch packet created for worker |
| Diff evidence | `git diff --check` required before commit |
| Approval boundary | dispatch only; worker must not commit |
| Claim boundary | no runtime/provider/live/public-sync/direct-interception claim |
| Agent type | dispatch author |
| Invocation ID | local-session-2026-06-20-aaf-t5-dispatch |
| Expected manifest | AAF-T5 baseline; AAF-T5 work order; Codex classification; three advisory input files |
| Actual changed set | checked by git status and autorun gates before commit |
| Manifest delta | none expected beyond AAF-T5 dispatch/advisory packet normalization |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: AAF-T5 is private provenance governance-helper foundation work. Public
export requires separate public-sync authorization and remote verification.

## Claim Boundary

This work order authorizes only AAF-T5 worker-experience retrospective capture
standard, checker, helper diagnostic, focused tests, hook wiring, operational
index routing, and worker return. It does not authorize or claim guard
orientation read-receipt enforcement, automated provider selection, runtime
provider routing, provider/live behavior, public readiness, production
readiness, release readiness, direct interception, wrapper/proxy enforcement,
queue/daemon execution, cost optimization, full-hook equivalence, or universal
governed-coding control.
