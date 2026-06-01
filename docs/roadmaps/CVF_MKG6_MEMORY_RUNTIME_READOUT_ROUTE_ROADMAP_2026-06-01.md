# CVF MKG6 Memory Runtime Readout Route Roadmap

Memory class: FULL_RECORD

Status: IMPLEMENTATION_REVIEW_READY

docType: roadmap

Date: 2026-06-01

## Purpose

Expose the MKG5 Memory runtime workflow chain through one authenticated,
summary-only HTTP readout route without mixing Memory retrieval evidence into
provider prompt execution.

## Authorization / Decision

Authority:

- `docs/baselines/CVF_GC018_MKG6_MEMORY_RUNTIME_READOUT_ROUTE_2026-06-01.md`
- `docs/reviews/CVF_MKG5_MEMORY_RUNTIME_WORKFLOW_CHAIN_IMPLEMENTATION_REVIEW_2026-06-01.md`
- operator request on 2026-06-01 to continue making Memory a real system.

## Scope

In scope:

- add a small LPF package subpath export for the MKG5 chain;
- extract stable `/api/execute` orchestration into one or more bounded helper
  modules and reduce `route.ts` from `999` to at most `949` physical lines;
- add a cvf-web Memory readout projection helper;
- add authenticated `POST /api/memory/readout`;
- validate route input;
- return only sanitized summary-only evidence;
- add focused helper and route tests;
- file a pending uncommitted completion review.

Out of scope:

- further LPF `src/index.ts` expansion;
- route-response readout assembly;
- provider calls or live proof;
- prompt injection or reinjection;
- raw candidate content release;
- persistence mutation;
- graph mutation;
- new memory tiers;
- Legacy edits;
- public-sync, commit, push, or publish.

## Non-Goals

- no `/api/execute` behavioral change beyond responsibility-preserving helper
  extraction;
- no provider or hosted behavior claim;
- no live governance proof in this tranche;
- no prompt injection or reinjection;
- no persistence or graph mutation;
- no public readiness claim;
- no full Memory-system completion claim beyond local authenticated readout.

## Risk Control

The MKG5 internal result is not an HTTP response schema. Its retrieval result
may retain selected candidates with optional raw `content`. MKG6 must add a
projection layer and prove that a raw-content sentinel does not appear in the
serialized route response.

## Work Plan

| Step | Requirement | Output | Status |
| --- | --- | --- | --- |
| M6.0 | Split near-threshold execute-route owner before adjacent API growth | `route.ts` <= 949 lines plus helper extraction | REVIEW_READY |
| M6.1 | Add LPF Memory runtime subpath barrel export | `src/memory-runtime.ts`, `package.json` | REVIEW_READY |
| M6.2 | Add sanitized web readout projection | `src/lib/memory-runtime-readout.ts` | REVIEW_READY |
| M6.3 | Add authenticated route and explicit validation | `src/app/api/memory/readout/*` | REVIEW_READY |
| M6.4 | Add focused projection and route tests | focused test files | REVIEW_READY |
| M6.5 | Run TypeScript and governance gates | evidence block | REVIEW_READY |
| M6.6 | File pending completion review | completion review packet | REVIEW_READY |

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| HTTP route | authenticated `POST /api/memory/readout` exists |
| Safe projection | response does not expose `retrievalResult.selected[].content` or raw candidate input |
| Boundary literals | returned readout includes `rawMemoryReleased=false` and `canReinject=false` |
| Fail closed | invalid input, unauthenticated request, and denied policy do not return Memory context |
| File-size discipline | LPF root remains reduced; `/api/execute/route.ts` shrinks from `999` to at most `949` physical lines |
| Local verification | focused tests and both TypeScript checks pass |

## Verification / Evidence

Required before worker handoff:

```powershell
npm test -- tests/memory-runtime-workflow-chain.test.ts
npm run check
npx vitest run src/lib/memory-runtime-readout.test.ts src/app/api/memory/readout/route.test.ts
npm run check
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/check_work_order_dispatch_quality.py --base <baseHead> --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <baseHead> --head HEAD
```

Run the first two commands from
`EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION`. Run the next two from
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`.

## Roadmap-To-Work-Order Trace

Work order:

`docs/work_orders/CVF_WO_MKG6_MEMORY_RUNTIME_READOUT_ROUTE_2026-06-01.md`

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private route/readout roadmap only. No public-sync remote, public
repository commit, or public artifact path is included.

## Claim Boundary

MKG6 delivers a local authenticated readout route only. It does not authorize
provider behavior, live proof, prompt injection, reinjection, raw Memory
release, persistence mutation, graph mutation, hosted readiness, production
readiness, public readiness, public-sync, push, or autonomous mutation.
