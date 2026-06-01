# CVF Work Order - MKG6 Memory Runtime Readout Route

Memory class: FULL_RECORD

Status: DISPATCHED_TO_WORKER

docType: work_order

Date: 2026-06-01

## Purpose

Implement a bounded authenticated `POST /api/memory/readout` route for the
MKG5 Memory runtime workflow chain. Return a sanitized summary-only projection,
prove raw candidate content cannot leak into HTTP output, and leave the result
pending and uncommitted for orchestrator review.

## Authority Chain

| Authority | Path / basis | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-01 request to continue Memory system implementation through MKG6 | ACCEPT |
| MKG6 GC-018 | `docs/baselines/CVF_GC018_MKG6_MEMORY_RUNTIME_READOUT_ROUTE_2026-06-01.md` | ACCEPT |
| MKG6 roadmap | `docs/roadmaps/CVF_MKG6_MEMORY_RUNTIME_READOUT_ROUTE_ROADMAP_2026-06-01.md` | ACCEPT |
| MKG5 implementation review | `docs/reviews/CVF_MKG5_MEMORY_RUNTIME_WORKFLOW_CHAIN_IMPLEMENTATION_REVIEW_2026-06-01.md` | ACCEPT |
| Worker autonomy standard | `docs/reference/CVF_WORKER_AUTONOMY_DISPATCH_PROMPT_STANDARD_2026-06-01.md` | ACCEPT |

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | dispatch packet and review pending implementation | no silent boundary expansion |
| Worker | implement route/readout projection and tests | no commit, push, live proof, or prompt wiring |
| Reviewer | verify raw-content exclusion, auth, tests, and changed-file boundary | reject raw Memory leakage |

## Scope

Allowed scope:

- add `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime.ts`;
- modify `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/package.json` only to add a
  `./memory-runtime` subpath export;
- modify `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
  only through responsibility-preserving helper extraction;
- add one or more bounded helper modules under
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/`:
  `route-memory-context.ts`, `route-post-execution-readouts.ts`, or
  `route-final-response.ts`;
- add `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts`;
- add `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.test.ts`;
- add `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route-constants.ts`;
- add `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts`;
- add `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.test.ts`;
- create
  `docs/reviews/CVF_MKG6_MEMORY_RUNTIME_READOUT_ROUTE_COMPLETION_2026-06-01.md`;
- run listed focused tests, TypeScript checks, and governance gates;
- fix allowed-scope test, validation, projection, documentation-format, or
  gate defects and rerun.

Forbidden scope:

- further edits to `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/index.ts`;
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-response-readouts.ts`;
- provider calls or live proof;
- prompt injection or reinjection;
- raw candidate `content` release;
- persistence mutation;
- graph mutation;
- new memory tiers;
- `.private_reference/legacy/**` edits;
- public-sync, push, publish, or local commit by the worker;
- destructive action.

Risk ceiling: R2 bounded local route integration.

## Required First Reads

- `docs/baselines/CVF_GC018_MKG6_MEMORY_RUNTIME_READOUT_ROUTE_2026-06-01.md`
- `docs/roadmaps/CVF_MKG6_MEMORY_RUNTIME_READOUT_ROUTE_ROADMAP_2026-06-01.md`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/package.json`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/learning-plane/readout/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/learning-plane/readout/route.test.ts`
- `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md`

## Pre-Flight Checks

Capture `baseHead` before material implementation:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/check_work_order_dispatch_quality.py --base <baseHead> --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <baseHead> --head HEAD
```

The worktree already contains orchestrator-owned pending governance and MKG4/
MKG5 files. Do not edit, revert, stage, or claim ownership of pre-existing
changes. Record the actual `git status --short` output in the completion review.

## Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| MKG5 chain evaluator exists | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts` | line 95 | `runMemoryRuntimeWorkflowChain` | Memory runtime workflow chain | ACCEPT |
| MKG5 result exposes bounded invariant fields | LITERAL_INVARIANT | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts` | lines 60-61 | `rawMemoryReleased`, `canReinject` | `MemoryRuntimeWorkflowResult` | ACCEPT |
| Retrieval candidate may carry raw content | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | `MemoryRetrievalCandidate` | `content` | `MemoryRetrievalCandidate` | ACCEPT |
| Context packager returns summary-only text and false reinjection evidence | LITERAL_INVARIANT | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts` | `MemoryContextBlock`, `MemoryContextPackageEvidence` | `rawMemoryReleased`, `canReinject` | Memory context packager | ACCEPT |
| LPF currently exports only root entry | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/package.json` | `exports` | `exports` | package export map | ACCEPT |
| Existing authenticated readout route verifies service token or session cookie | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/learning-plane/readout/route.ts` | lines 80-101 | `verifyServiceTokenRequest`, `verifySessionCookie` | Learning Plane readout route | ACCEPT |
| LPF root index proactive split completed | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/index.ts` | physical line count command: `885` | `src/index.ts` | LPF root barrel | ACCEPT |
| Execute route is at hard-limit boundary | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | physical line count command: `999` | `POST` | execute route | ACCEPT |

## Near-Threshold Owner Maintainability Plan

Active owner entrypoint:

`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`

Current line count: `999`. Hard threshold: `1000`.

Action: extract stable orchestration from the execute route into one or more
bounded helpers under the same `src/app/api/execute/` owner domain before
adding the sibling Memory readout route. Preserve behavior and run existing
execute-route focused tests plus the execute-route step-sequence guard.

Minimum shrink target: 50 lines

Required result: `/api/execute/route.ts` must be at most `949` physical lines.
The active owner entrypoint is included in Allowed scope and Write Ownership.

## Planned New Source Surfaces

| New source surface | Purpose | Existing source authority reused | Boundary |
| --- | --- | --- | --- |
| `cvf-learning-plane-foundation/memory-runtime` | subpath barrel export | MKG5 chain | do not edit LPF root index |
| `buildMemoryRuntimeReadout` | sanitized HTTP projection | MKG5 result | no raw candidate `content` |
| `POST /api/memory/readout` | authenticated local HTTP readout | existing readout auth pattern | no provider or prompt execution |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| Add LPF Memory runtime subpath barrel | Scope / Execution Plan | `src/memory-runtime.ts`, package export | LPF `npm run check` | DISPATCHED |
| Split near-threshold execute-route owner | Near-Threshold Owner Maintainability Plan | `route.ts` <= 949 lines plus helper extraction | line-count command and focused route tests | DISPATCHED |
| Add sanitized projection | Risk Control / Execution Plan | `buildMemoryRuntimeReadout` | focused helper test | DISPATCHED |
| Add authenticated route | Execution Plan | `POST /api/memory/readout` | focused route test | DISPATCHED |
| Prove raw content does not leak | Acceptance Criteria | raw-content sentinel absent from serialized response | focused route test | DISPATCHED |
| Preserve file-size discipline | Near-Threshold Owner Maintainability Plan | LPF root remains reduced; execute route <= 949 lines | line-count command and file-size guard | DISPATCHED |
| Preserve no-live/no-prompt boundary | Scope / Claim Boundary | completion review | changed-file review | DISPATCHED |

## Worker Autonomy / No-Question Rule

The worker must not ask the operator before performing non-destructive actions
inside this work order's Allowed scope.

Proceed autonomously with reading named files, adding owned source and test
files, modifying the allowed package export map, running git status/diff/
rev-parse, running listed tests and gates, fixing allowed-scope implementation
or documentation defects, and rerunning failed checks.

Ask only if the next action would exceed Allowed scope, edit a forbidden path,
edit Legacy source, run live/provider proof, use secrets/quota, public-sync,
push/publish, commit, change claim boundary or risk, release a `HOLD_*`
prerequisite, or perform destructive/irreversible action.

If a machine gate or focused test fails inside Allowed scope, repair it and
rerun. Do not ask whether to fix routine failures.

## Pending Artifact Evidence Finality

The worker must not commit. Leave MKG6 source, tests, and completion review
pending for orchestrator review.

Do not claim `git status --short` is clean. Record the actual pending MKG6
status lines. Do not cite `HEAD~1..HEAD` as proof for pending implementation.

## Work-Order Fulfillment Manifest

This runtime/source work order is subject to machine-checked handoff
fulfillment. A worker handoff is incomplete if required artifacts or proof
literals are missing.

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
| --- | --- | --- |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime.ts` | Yes | narrow LPF Memory runtime subpath barrel |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-final-response.ts` | Yes | execute-route helper extraction |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` | Yes | sanitized summary-only projection helper |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.test.ts` | Yes | projection helper tests |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route-constants.ts` | Yes | readout route constants |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | Yes | authenticated Memory readout HTTP route |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.test.ts` | Yes | route tests and fail-closed proof |
| `docs/reviews/CVF_MKG6_MEMORY_RUNTIME_READOUT_ROUTE_COMPLETION_2026-06-01.md` | Yes | pending completion review |

## Forbidden Path Manifest

| Path | Reason |
| --- | --- |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/index.ts` | MKG6 must use a subpath barrel and must not expand or rework the LPF root index |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-response-readouts.ts` | explicitly forbidden by MKG6 boundary |
| `.private_reference/legacy/**` | Legacy source must not be edited |

## Pre-Existing Dirty Path Exemptions

| Path | Status at dispatch | Exemption boundary |
| --- | --- | --- |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/index.ts` | `M` from MKG5 pending barrel split | worker must not edit, stage, or claim this file for MKG6 |

## Required Proof Manifest

| Proof | Path | Required literal | Required at handoff |
| --- | --- | --- | --- |
| raw Memory leak sentinel test | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.test.ts` | `RAW_MEMORY_CONTENT_MUST_NOT_LEAK` | Yes |
| projection helper calls MKG5 chain | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` | `runMemoryRuntimeWorkflowChain` | Yes |
| boundary literal false returned | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.test.ts` | `rawMemoryReleased` | Yes |
| reinjection remains false | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.test.ts` | `canReinject` | Yes |

## Risk Control

Do not return the internal `MemoryRuntimeWorkflowResult` object verbatim.

`MemoryRetrievalCandidate` permits optional `content`, and the internal
retrieval result retains selected candidates. Add a projection helper that
returns only bounded status, reason, contract/version evidence, selected
memory IDs, exclusion reasons, summary-only context block/evidence, event or
gateway evidence needed for audit, `rawMemoryReleased=false`, and
`canReinject=false`.

The helper and route tests must construct a candidate whose `content` contains
the sentinel `RAW_MEMORY_CONTENT_MUST_NOT_LEAK` and assert that serialized
readout output does not contain that sentinel.

## Worker Dispatch Prompt

Send this exact prompt with the work order:

```text
You are assigned MKG6 Memory Runtime Readout Route.

Primary work order:
docs/work_orders/CVF_WO_MKG6_MEMORY_RUNTIME_READOUT_ROUTE_2026-06-01.md

Read the complete work order before editing. Implement only its Allowed scope.

Critical design rule:
- add POST /api/memory/readout as an authenticated summary-only readout route;
- add a sanitized projection helper;
- do not return the MKG5 internal result object verbatim;
- prove RAW_MEMORY_CONTENT_MUST_NOT_LEAK is absent from serialized HTTP output;
- do not expand LPF src/index.ts or edit route-response-readouts.ts;
- first extract stable helper logic from /api/execute/route.ts and shrink it
  from 999 to at most 949 lines without behavioral change;
- do not add prompt injection, reinjection, provider calls, or live proof.

Worker Autonomy Rule:
Do not ask the operator before performing non-destructive actions inside
Allowed scope. If a focused test or machine gate fails inside Allowed scope,
repair it and rerun. Do not ask whether to fix routine failures.

Pending Artifact Rule:
Do not commit. Leave source, tests, and the completion review pending for
orchestrator review. Record actual git status. Do not claim a clean worktree
and do not use HEAD~1..HEAD as proof for pending files.

Stop and ask only if the next action would exceed Allowed scope, touch a
forbidden path, edit Legacy source, run live/provider/API proof, use
secrets/quota, public-sync, push/publish, commit, change risk or claim boundary,
release a HOLD prerequisite, or perform destructive/irreversible action.
```

## Write Ownership

Owned files:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/package.json`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-memory-context.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-post-execution-readouts.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-final-response.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route-constants.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.test.ts`
- `docs/reviews/CVF_MKG6_MEMORY_RUNTIME_READOUT_ROUTE_COMPLETION_2026-06-01.md`

Write mode:

- add owned source/test/review files;
- create only the execute-route helper files actually needed;
- shrink `/api/execute/route.ts` by at least 50 physical lines;
- modify only the LPF package export map;
- leave all implementation pending and uncommitted.

## Execution Plan

1. Capture `baseHead` and actual dirty worktree status.
2. Extract stable orchestration from `/api/execute/route.ts` into one or more
   owned helper modules. Preserve behavior, shrink the route to at most `949`
   physical lines, and run existing route-focused checks.
3. Add `src/memory-runtime.ts` as a narrow LPF subpath barrel for the MKG5
   chain and add `./memory-runtime` to LPF package exports.
4. Add `buildMemoryRuntimeReadout()` under cvf-web `src/lib/`. It must call
   `runMemoryRuntimeWorkflowChain()` and return a sanitized projection.
5. Add projection tests including the raw-content sentinel exclusion.
6. Add `POST /api/memory/readout` using the existing service-token-or-session
   auth pattern, explicit JSON validation, and the projection helper.
7. Add route tests for allowed readout, unauthenticated request, invalid body,
   policy denial, false boundary literals, and raw-content sentinel exclusion.
8. Run focused tests, TypeScript checks, execute-route step-sequence guard,
   file-size guard, dispatch-quality
   guard, and pre-implementation autorun gate.
9. Create the pending completion review with actual changed files, command
   results, Public Export Disposition, Finding-To-Governance Learning
   Disposition, and Claim Boundary.
10. Leave all MKG6 implementation files pending and uncommitted.

## Evidence Requirements

- LPF focused MKG5 test result;
- LPF `npm run check` result;
- cvf-web focused projection and route test results;
- cvf-web `npm run check` result;
- `python governance/compat/check_governed_file_size.py --enforce`;
- `python governance/compat/check_execute_route_step_sequence.py --enforce`;
- `python governance/compat/check_work_order_dispatch_quality.py --base <baseHead> --head HEAD --enforce`;
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <baseHead> --head HEAD`;
- actual `git status --short`;
- `git diff --name-status`;
- explicit evidence that forbidden files were not edited;
- pending completion review.

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| Authenticated route | unauthenticated request returns `401`; session-authenticated request can evaluate readout |
| Explicit validation | invalid JSON and invalid/missing fields return `400` |
| Sanitized projection | serialized route response excludes raw candidate input and `retrievalResult.selected[].content` |
| Sentinel proof | response serialization does not contain `RAW_MEMORY_CONTENT_MUST_NOT_LEAK` |
| Boundary literals | response returns `rawMemoryReleased=false` and `canReinject=false` |
| Fail closed | denied policy returns bounded denial and no context block |
| File-size discipline | LPF root remains reduced; execute route shrinks from `999` to at most `949` physical lines |
| No prompt execution | no provider call, prompt assembly, or reinjection code added |

## Review Gate

Reject worker handoff if:

- raw candidate `content` appears in serialized HTTP output;
- internal MKG5 result is returned verbatim;
- `/api/execute/route.ts` remains above `949` lines, expands behavior, or lacks
  responsibility-preserving helper extraction;
- `route-response-readouts.ts` or LPF `src/index.ts` is edited;
- provider/live proof, prompt injection, reinjection, persistence mutation,
  graph mutation, or new memory tier appears;
- worker commits, pushes, publishes, or asks whether to fix an allowed-scope
  test/gate failure.

## Closure Checklist

- N/A with reason: worker must not close or commit MKG6. Worker returns pending
  implementation and completion review for orchestrator review.

## Return-To-Orchestrator Conditions

Return only if implementation requires a forbidden path, route/prompt behavior
outside the authorized readout boundary, live/provider proof, secrets/quota,
public-sync, destructive action, higher risk, or a claim-boundary change.

## Operator Checkpoint

Operator explicitly requested MKG6 work order dispatch so another agent can
implement the next Memory-system tranche and exercise the strengthened guards.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private dispatched route/readout work order only. No public-sync
remote, public repository commit, or public artifact path is included.

## Claim Boundary

MKG6 is dispatched as a bounded execute-route maintainability extraction plus
local authenticated Memory readout route. It does not authorize `/api/execute`
behavior expansion, provider behavior, live proof,
prompt injection, reinjection, raw Memory release, persistence mutation, graph
mutation, new memory tiers, hosted readiness, production readiness, public
readiness, public-sync, push, or autonomous mutation.
