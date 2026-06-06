# CVF GC-018 - MKG6 Memory Runtime Readout Route

Memory class: FULL_RECORD

Status: AUTHORIZED_FOR_IMPLEMENTATION

docType: baseline

Date: 2026-06-01

## Purpose

Authorize the first safe HTTP readout route for the MKG5 Memory runtime
workflow chain.

MKG6 exposes a bounded `POST /api/memory/readout` surface that evaluates the
MKG5 chain and returns a sanitized summary-only readout. It must not wire
Memory into provider prompts, edit `/api/execute`, release raw candidate
content, or authorize reinjection.

## Scope / Target / Owner Boundary

Target owner surfaces:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/package.json`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- one or more bounded execute-route extraction helpers under
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route-constants.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.test.ts`

Boundary:

- authenticated readout route only;
- summary-only HTTP projection;
- `/api/execute/route.ts` must shrink by at least 50 lines through helper
  extraction before the new readout route is added;
- no prompt injection or reinjection;
- no raw candidate `content` in HTTP output;
- no provider/live proof;
- no persistence mutation or new memory tier.

## Decision

Decision: authorize MKG6 route/readout implementation as the next bounded
Memory-system tranche after MKG5 runtime-chain foundation.

The worker may add a package subpath export, a web projection helper, one
authenticated route, focused tests, and the completion review. The worker must
leave implementation pending and uncommitted for orchestrator review.

## Runtime Owner Surface

| Owner surface | Source path | Disposition |
| --- | --- | --- |
| MKG5 Memory runtime workflow chain | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts` | ACCEPT |
| LPF package export map | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/package.json` | ACCEPT |
| Existing authenticated readout route pattern | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/learning-plane/readout/route.ts` | ACCEPT_AS_PATTERN |
| Existing execute route | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | ACCEPT_FOR_MANDATORY_SPLIT |

## Source / Predecessor Evidence

Predecessors:

- MKG1 reconciled the Memory/Knowledge/Graph owner surfaces.
- MKG2 triaged deferred runtime candidates.
- MKG3 checked negative owner evidence for deferred groups.
- MKG4 tested pending-artifact gate-evidence consistency.
- MKG5 added the deterministic LPF Memory runtime workflow chain and focused
  tests.

Current source evidence:

- MKG5 chain source exists under LPF and exposes the workflow evaluator.
- LPF package metadata currently exposes only the root package entry.
- The existing Learning Plane readout route proves the current cvf-web
  service-token-or-session authentication pattern.
- LPF root `src/index.ts` was proactively split from `975` to `885` lines.
- `/api/execute/route.ts` remains at `999` lines, so MKG6 must reduce that
  active owner entrypoint before adding a sibling API route.

## Knowledge Absorption Blind-Spot Control Block

### Gate 1 - Source Inventory

This tranche does not absorb a new Legacy folder or external corpus.

Reviewed current source owner files:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/package.json`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/learning-plane/readout/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`

Filesystem corpus listing is `N/A with reason`: MKG6 consumes the bounded MKG5
runtime owner set and does not claim corpus completeness or new absorption.

### Gate 2 - Prior Absorption Resolution

Resolved predecessors:

- MKG1 owner-surface reconciliation;
- MKG2 deferred runtime triage;
- MKG3 current-owner negative evidence;
- MKG4 gate-evidence consistency probe;
- MKG5 Memory runtime workflow chain.

### Gate 3 - File-Level Value Extraction

Accepted runtime value:

- MKG5 already composes retrieval event, controlled gateway, retrieval policy,
  summary-only context packager, and context event.
- `MemoryRetrievalCandidate` may contain optional raw `content`.
- The HTTP route therefore needs a sanitized projection instead of returning
  the internal MKG5 result object verbatim.

### Gate 4 - Owner-Surface Normalization

Normalize the new route into existing owner surfaces:

- LPF owns the Memory workflow-chain contract;
- cvf-web owns authentication, HTTP validation, and HTTP projection;
- `/api/execute` remains unchanged.

### Gate 5 - Accept / Defer / Reject Disposition

| Candidate | Disposition | Reason |
| --- | --- | --- |
| Authenticated Memory readout route | ACCEPT_NOW | safe bounded route integration |
| Summary-only HTTP projection | ACCEPT_NOW | prevents raw candidate content leakage |
| `/api/execute` Memory prompt wiring | DEFER_DEMAND_GATED | requires a separate route/prompt-risk tranche |
| Provider/live proof | DEFER_DEMAND_GATED | route must exist and pass local review first |
| Prompt reinjection | REJECT_DIRECT | forbidden by current MKG5/MKG6 boundary |

### Gate 6 - Adversarial Role Review

Reviewer challenge:

- returning the MKG5 internal result verbatim can expose
  `retrievalResult.selected[].content`;
- adding exports through LPF `src/index.ts` would touch a near-threshold file;
- leaving `/api/execute/route.ts` untouched while adding a sibling API route
  would bypass active owner-surface maintainability debt.

Required response:

- add a dedicated projection helper;
- add a package subpath export;
- keep the LPF root index reduced through its new barrel split;
- extract stable execute-route orchestration into helper modules and shrink
  `/api/execute/route.ts` by at least 50 lines before adding the sibling route.

### Gate 7 - Thin Proof And Closure Delta

Required closure delta:

- route auth tests;
- execute-route helper extraction with `/api/execute/route.ts` reduced from
  `999` to at most `949` physical lines;
- valid readout test;
- denied/fail-closed test;
- JSON serialization test proving a raw sentinel in candidate `content` is
  absent from the HTTP response;
- TypeScript checks for LPF and cvf-web;
- governed file-size guard.

Gate 7 completeness cross-check is `N/A with reason`: no folder absorption or
subfolder completeness claim is made.

Blind-spot verdict: CLEAR_FOR_BOUNDED_IMPLEMENTATION.

## Required Evidence

- package subpath export without editing LPF `src/index.ts`;
- authenticated `POST /api/memory/readout`;
- explicit request validation;
- sanitized HTTP projection;
- focused unit/route tests;
- LPF and cvf-web TypeScript checks;
- governance guards;
- pending uncommitted completion review.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private route/readout implementation packet only. No public-sync
remote, public repository commit, or public artifact path is included.

## Claim Boundary

MKG6 authorizes a bounded execute-route maintainability extraction followed by
a local authenticated Memory runtime readout route with summary-only HTTP
evidence. It does not authorize provider execution, live proof, prompt
injection, reinjection, raw Memory
release, persistence mutation, graph mutation, new memory tiers, hosted
readiness, production readiness, public readiness, public-sync, push, or
autonomous mutation.
