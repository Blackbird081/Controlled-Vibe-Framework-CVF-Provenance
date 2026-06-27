# CVF Agent Work Order: DSCP-T3 Runtime Pilot (CPF Internal)

Memory class: POINTER_RECORD

Status: CLOSED_PASS_BOUNDED

Template: `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
(post-`fce62cd3` version with Worker Pending-Return Gate section 6D)

completionReviewPath: `docs/reviews/CVF_DSCP_T3_RUNTIME_PILOT_CPF_INTERNAL_COMPLETION_2026-06-07.md`

dispatchBaseHead: `fda6eff4`
executionBaseHead: `fda6eff4`
closureBaseHead: `fda6eff4`

Status token rule:
- Worker must not change `Status` field.
- Reviewer/committer changes `Status` to `CLOSED_PASS_BOUNDED` after
  committed-range gates pass.

Commit mode: `WORKER_MUST_NOT_COMMIT`

---

## Purpose

Implement `GovernedContextPackerContract` in `CVF_CONTROL_PLANE_FOUNDATION`
as a deterministic governed wrapper around the existing
`ContextPackagerContract.pack()`. This is the DSCP-T3 CPF internal runtime
pilot: wire T2 type contracts into a real, compilable, testable runtime
function and prove it deterministically.

## Scope / Target / Owner Boundary

Target: two new files in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/`.

- `src/dscp.governed.context.packer.ts` - GovernedContextPackerContract class
- `tests/dscp.governed.context.packer.test.ts` - deterministic vitest

Owner boundary: worker owns authoring the two new files and the worker
return packet. Reviewer/committer (Codex) owns review, commit, and
session continuity update. No existing file is in scope for modification.

## 1. Authority Chain

- Operator authorized DSCP-T3 CPF Internal on 2026-06-07.
- GC-018: `docs/baselines/CVF_GC018_DSCP_T3_RUNTIME_PILOT_CPF_INTERNAL_2026-06-07.md`
- Predecessor: DSCP-T2 `CLOSED_PASS_BOUNDED` at `932a40aa`
- Active handoff: `AGENT_HANDOFF_V17_2026-06-07.md`
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`

---

## 2. Transfer Objective

Author a `GovernedContextPackerContract` class that:
1. Validates `governanceEnvelope.classificationGate === "PASS"` AND
   `governanceEnvelope.freshnessGate === "PASS"` before proceeding.
2. On gate failure: returns a blocked `GovernedContextPackage` with
   `governanceEvidence.classificationGate` or `freshnessGate` reflecting
   the actual gate result; does NOT call `ContextPackagerContract.pack()`.
3. On gates PASS: calls `ContextPackagerContract.pack(packRequest)` and
   returns a `GovernedContextPackage` wrapping the result.
4. Always sets `rawContentReleased: false` and `canBypassGovernance: false`
   on `GovernedContextPackageEvidence`.

Deliverables:
1. `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.packer.ts`
   - GovernedContextPackerContract with gate enforcement + inner pack call
2. `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.governed.context.packer.test.ts`
   - deterministic vitest: PASS path + BLOCKED path + governance lock assertions

---

## 3. Source Packet

DSCP-T2 contracts (source for T3 types):
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts`
  (`CLOSED_PASS_BOUNDED` at `932a40aa`)

CPF inner engine (source for T3 implementation):
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/context.packager.contract.ts`
  (`ContextPackagerContract.pack()` at lines 104-280)
  (`createContextPackagerContract()` factory at lines 284-287)

Prerequisites verified:
- DSCP-T2 contract file: present at dispatch HEAD
- CPF `ContextPackagerContract`: present at dispatch HEAD
- GC-018 (T3): `docs/baselines/CVF_GC018_DSCP_T3_RUNTIME_PILOT_CPF_INTERNAL_2026-06-07.md`
  `Status: ACTIVE_BASELINE`

---

## 4. Agent Roles

Worker: Claude (implementation agent)
Reviewer/committer: Codex

---

## 5. Execution Plan

### Commit Mode And Base-Anchor Lifecycle

1. Capture `executionBaseHead` via `git rev-parse --short HEAD` before
   any edit. Record in worker return.
2. Confirm working tree is clean.
3. Verify all required source files listed in Section 6A are present.
4. If any required source file is missing, stop and return
   `BLOCKED_SOURCE_NOT_FOUND`.

### Work Plan

1. Read `CVF_SESSION_MEMORY.md`, `CVF_SESSION/ACTIVE_SESSION_STATE.json`,
   `AGENT_HANDOFF_V17_2026-06-07.md`.
2. Read GC-018 (T3).
3. Read `dscp.governed.context.contract.ts` (T2 types).
4. Read `context.packager.contract.ts` (CPF inner engine).
5. Read an existing CPF contract test for style reference.
6. Author `dscp.governed.context.packer.ts`.
7. Author `dscp.governed.context.packer.test.ts`.
8. Run `npx tsc --noEmit` in CPF directory. Fix any errors.
9. Run `npx vitest run tests/dscp.governed.context.packer.test.ts`. Fix
   any failures.
10. Run Worker Pending-Return Gate checks (Section 6D).
11. Write worker return packet.
12. Stage all new files.

---

## 6A. Source Verification Table

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| `GovernedContextPackRequest` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | lines 78-84 | `GovernedContextPackRequest` | `dscp.governed.context.contract.ts` | ACCEPT |
| `GovernedContextPackage` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | lines 111-117 | `GovernedContextPackage` | `dscp.governed.context.contract.ts` | ACCEPT |
| `GovernedContextPackageEvidence` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | lines 90-107 | `GovernedContextPackageEvidence` | `dscp.governed.context.contract.ts` | ACCEPT |
| `GovernanceContextEnvelope` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | lines 58-73 | `GovernanceContextEnvelope` | `dscp.governed.context.contract.ts` | ACCEPT |
| `ContextPackagerContract.pack()` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/context.packager.contract.ts` | lines 104-280 | `ContextPackagerContract` | `context.packager.contract.ts` | ACCEPT |
| `createContextPackagerContract` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/context.packager.contract.ts` | lines 284-287 | `createContextPackagerContract` | `context.packager.contract.ts` | ACCEPT |
| `TypedContextPackage` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/context.packager.contract.ts` | lines 49-59 | `TypedContextPackage` | `context.packager.contract.ts` | ACCEPT |
| CPF src/ target directory | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/context.packager.contract.ts` | line 1 | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/` | CPF module | ACCEPT |
| GC-018 (T3) | `docs/baselines/CVF_GC018_DSCP_T3_RUNTIME_PILOT_CPF_INTERNAL_2026-06-07.md` | lines 1-12 | `ACTIVE_BASELINE` | GC-018 baseline | ACCEPT |

---

## 6B. Task Execution

### New Files

| File | Action | Path |
|---|---|---|
| GovernedContextPackerContract | CREATE | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.packer.ts` |
| Deterministic test | CREATE | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.governed.context.packer.test.ts` |

### Implementation Contract

`GovernedContextPackerContract.pack(request: GovernedContextPackRequest)`:

```
PRECONDITION CHECK:
  envelope = request.governanceEnvelope
  if envelope.classificationGate !== "PASS" OR envelope.freshnessGate !== "PASS":
    return GovernedContextPackage {
      innerPackage: <blocked placeholder with packageId="BLOCKED", zero segments>
      governanceEvidence: {
        classificationGate: envelope.classificationGate,
        freshnessGate: envelope.freshnessGate,
        policyDecision: "BLOCKED: governance gate not PASS",
        sourceArtifactIds: [],
        rawContentReleased: false,
        canBypassGovernance: false,
      }
    }

PACK:
  innerPackage = this.packager.pack(request.packRequest)
  return GovernedContextPackage {
    innerPackage,
    governanceEvidence: {
      classificationGate: envelope.classificationGate,
      freshnessGate: envelope.freshnessGate,
      policyDecision: envelope.policyDecision,
      sourceArtifactIds: envelope.artifactDescriptors.map(a => a.artifactId),
      rawContentReleased: false,
      canBypassGovernance: false,
      authorizationRef: envelope.authorizationRef,
    }
  }
```

### Governance Lock Invariant

`rawContentReleased` and `canBypassGovernance` MUST be typed as literal
`false` in `GovernedContextPackageEvidence` (from T2 contracts) and the
implementation MUST assign the literal value `false` - never a variable
or computed boolean.

### Forbidden Scope

The worker must not:
- modify any existing `.ts` file;
- export new symbols from any existing `index.ts`;
- add provider/live API calls;
- call `ContextPackagerContract.pack()` when governance gates are not PASS;
- add runtime logic beyond gate check + inner pack call;
- add non-deterministic behavior to the test (no `Date.now()` without
  injected mock);
- commit or push.

---

## Roadmap-To-Work-Order Trace Matrix

| Roadmap / GC-018 requirement | Work-order instruction | Evidence target | Status |
|---|---|---|---|
| GovernedContextPackerContract class | Section 6B implementation contract | packer source file | READY |
| Gate enforcement before inner pack | Section 6B PRECONDITION CHECK | blocked-path test | READY |
| Governance locks on evidence block | Section 6B Governance Lock Invariant | governance lock test assertions | READY |
| Deterministic vitest | Section 6B test file | vitest PASS count in worker return | READY |
| tsc PASS | Section 6D gate row | tsc result in worker return | READY |
| No existing file modified | Forbidden Scope section | git status in worker return | READY |

---

## Worker Autonomy / No-Question Rule

Worker must proceed autonomously inside Allowed scope. In-scope TypeScript
compilation errors, test failures, and gate violations must be repaired by
the worker before returning. Worker must stop and return
`BLOCKED_SOURCE_NOT_FOUND` only if a required source file is missing.

---

## Reviewer Closure Conversion Block

```
completionReviewPath: docs/reviews/CVF_DSCP_T3_RUNTIME_PILOT_CPF_INTERNAL_COMPLETION_2026-06-07.md
reviewerOwnedClosurePaths:
- docs/reviews/CVF_DSCP_T3_RUNTIME_PILOT_CPF_INTERNAL_WORKER_RETURN_2026-06-07.md
- docs/reviews/CVF_DSCP_T3_RUNTIME_PILOT_CPF_INTERNAL_COMPLETION_2026-06-07.md
- docs/roadmaps/CVF_DSCP_DOMAIN_AGNOSTIC_SCAN_CONTEXT_PACK_READINESS_ROADMAP_2026-06-07.md
- CVF_SESSION/ACTIVE_SESSION_STATE.json
- CVF_SESSION_MEMORY.md
- AGENT_HANDOFF_V17_2026-06-07.md
closureResidueCheck: PASS
reviewerConversionStatus: worker pending tokens resolved in closure batch
```

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `AGENT_HANDOFF_V17_2026-06-07.md`
4. `docs/baselines/CVF_GC018_DSCP_T3_RUNTIME_PILOT_CPF_INTERNAL_2026-06-07.md`
5. `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts`
6. `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/context.packager.contract.ts`
7. `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/context.packager.test.ts` (style reference)

## Write Ownership

Owned paths (new files only; no existing file modified):

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.packer.ts`
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.governed.context.packer.test.ts`
- `docs/reviews/CVF_DSCP_T3_RUNTIME_PILOT_CPF_INTERNAL_WORKER_RETURN_2026-06-07.md`

All session continuity and registry files are reviewer-owned.

## Pre-Flight Checks

Capture `executionBaseHead` via `git rev-parse --short HEAD` before any edit.
Confirm working tree is clean. Verify that GC-018 and all source files in
Section 6A are present before proceeding.

If any required source file in Section 6A is missing, stop and return
`BLOCKED_SOURCE_NOT_FOUND`.

---

## 6C. Work-Order Fulfillment Manifest

## Required Artifact Manifest

| Path | Output stage | Purpose |
|---|---|---|
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.packer.ts` | worker return | GovernedContextPackerContract with gate enforcement |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.governed.context.packer.test.ts` | worker return | deterministic vitest: PASS path + BLOCKED path + governance locks |
| `docs/reviews/CVF_DSCP_T3_RUNTIME_PILOT_CPF_INTERNAL_WORKER_RETURN_2026-06-07.md` | worker return | worker evidence packet for Codex review |

---

## 6D. Worker Pending-Return Gate

| Component | Scope trigger | Verification command | Expected result |
|---|---|---|---|
| Execution anchor | every worker run | `git rev-parse --short HEAD` | HEAD at dispatch or later; record in worker return |
| Pending worktree | `WORKER_MUST_NOT_COMMIT` | `git status --short` | new files staged; no `.ts` existing file modified |
| TypeScript compilation | new `.ts` file authored | `npx tsc --noEmit` in CPF directory | zero type errors |
| Focused vitest | new `.test.ts` file authored | `npx vitest run tests/dscp.governed.context.packer.test.ts` | all tests PASS |
| Markdown structural | new `.md` file in tracked path | `check_markdown_structural_completeness.py --base fda6eff4 --head HEAD --enforce` | COMPLIANT |
| Finding-to-governance | new `.md` file in tracked path | `check_finding_to_governance_learning.py --base fda6eff4 --head HEAD --enforce` | COMPLIANT |
| Machine Closure Package | new `.md` file in tracked path | `check_machine_closure_package.py --base fda6eff4 --head HEAD --enforce` | COMPLIANT |
| Dispatch quality | new work order in tracked path | `check_work_order_dispatch_quality.py --base fda6eff4 --head HEAD --enforce` | COMPLIANT |

---

## 7. Dissent And Review Ledger

No dissent recorded at dispatch.

---

## 8. Integration Decision

Integration decision: APPROVED. DSCP-T2 contracts `CLOSED_PASS_BOUNDED`;
`ContextPackagerContract.pack()` is the existing canonical CPF packaging
API (declared canonical by W9-T1). DSCP-T3 adds a thin governed wrapper
with no new dependency and no existing file mutation.

---

## Evidence Requirements

The worker must record in the worker return packet:

- `executionBaseHead` captured via `git rev-parse --short HEAD`
- TypeScript compilation result (`tsc --noEmit` pass/fail + error count)
- Vitest result (pass count / total count)
- All four component governance gate results
- `git status --short` output confirming no existing file modified
- Explicit forbidden scope boundary statement

## Acceptance Criteria

1. `dscp.governed.context.packer.ts` created: `GovernedContextPackerContract.pack()` compiles.
2. PASS path test: fixed `GovernedContextPackRequest` with all gates PASS produces `GovernedContextPackage` with correct `innerPackage`.
3. BLOCKED path test: `classificationGate !== "PASS"` input does NOT call inner packager; returns blocked evidence.
4. Governance locks: `rawContentReleased === false` and `canBypassGovernance === false` on all evidence blocks.
5. `tsc --noEmit` PASS, zero errors.
6. All vitest tests PASS (target 10+).
7. No existing `.ts` file modified.
8. All four governance component gates PASS on committed range.
9. Worker return packet present with all required evidence.

## Review Gate

Codex must review the DSCP-T3 worker return before deciding T3 closure.
After T3 closes, any DSCP-T4 or DSCP extension (retrieval receipt runtime,
multi-domain pilot) requires a fresh operator-authorized scope expansion.

## Operator Checkpoint

operator.checkpoint.waiver: DSCP-T3 is a governed runtime wrapper adding
two new files to CPF with no existing mutation. Operator input is not
required for execution. Operator input IS required before any live provider
call, corpus ingestion, retrieval receipt runtime, public-sync, production
readiness, or public readiness claim.

## 9. Completion Evidence

| Evidence item | Path | Status |
|---|---|---|
| GovernedContextPackerContract (staged) | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.packer.ts` | PASS |
| Deterministic test (staged) | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.governed.context.packer.test.ts` | PASS |
| Worker return packet | `docs/reviews/CVF_DSCP_T3_RUNTIME_PILOT_CPF_INTERNAL_WORKER_RETURN_2026-06-07.md` | PASS |
| TypeScript compilation | `tsc --noEmit` result | PASS |
| Vitest result | vitest run result | PASS |
| Committed-range gate results | reviewer-owned closure gates | PASS |

---

## Claim Boundary

This work order claims: dispatch authorization for DSCP-T3 governed runtime
wrapper authoring and deterministic test coverage, bounded to two new files
in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/`. It does not claim: provider
API quality, corpus ingestion, retrieval receipt runtime, public-sync,
production readiness, or public readiness.

---

## Acceptance Receipt Assertion Matrix

`GovernedRetrievalReceipt` is NOT instantiated at runtime in DSCP-T3.
Receipt runtime is explicitly out of scope for this tranche.

| Required value | Observed value | Status |
|---|---|---|
| No runtime retrieval query | No provider call, no LLM query, no GovernedRetrievalReceipt instance created | N/A with reason: DSCP-T3 is governance wrapper + pack only; receipt runtime is out of scope |

---

## 9. Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED`; reviewer-owned closure conversion complete | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_DSCP_T3_RUNTIME_PILOT_CPF_INTERNAL_COMPLETION_2026-06-07.md` | reviewer completion artifact added in closure batch | PASS |
| Roadmap state | `docs/roadmaps/CVF_DSCP_DOMAIN_AGNOSTIC_SCAN_CONTEXT_PACK_READINESS_ROADMAP_2026-06-07.md` | DSCP-T3 row updated to `CLOSED_PASS_BOUNDED` by reviewer | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | DSCP-T3 packer/test scope registered in GC-051 by reviewer | PASS |
| Registry Markdown | `CVF_SESSION_MEMORY.md` and `AGENT_HANDOFF_V17_2026-06-07.md` | session markdown sync in reviewer closure sequence | PASS |
| External evidence digest | external artifact path | no external artifact produced | N/A with reason: all evidence is in-repo source, tests, and governance docs |
| System loop interlock | no system-loop mutation authorized | DSCP-T3 is governed wrapper only; no system loop changed | N/A with reason: governed wrapper only |
| Session continuity | `CVF_SESSION_MEMORY.md` and `AGENT_HANDOFF_V17_2026-06-07.md` | session sync in reviewer closure sequence | PASS |

---

## 10. Reviewer Checklist

- [x] Worker return reviewed.
- [x] `dscp.governed.context.packer.ts` spot-checked: gate enforcement correct.
- [x] `rawContentReleased === false` confirmed in implementation.
- [x] `canBypassGovernance === false` confirmed in implementation.
- [x] Blocked path: inner packager NOT called on gate failure confirmed.
- [x] tsc PASS confirmed.
- [x] vitest PASS confirmed.
- [x] No existing file modified confirmed.
- [x] All four governance gates PASS confirmed.
- [x] Session sync scoped to reviewer closure sequence.

## Closure Checklist

- [x] GovernedContextPackerContract file created at specified path.
- [x] Deterministic test file created at specified path.
- [x] TypeScript compilation PASS recorded.
- [x] All vitest tests PASS recorded.
- [x] No existing `.ts` file modified.
- [x] All component governance gates PASS or pending-return exception recorded.
- [x] No forbidden scope action occurred.
- [x] Codex reviewed worker return.

## Return-To-Orchestrator Conditions

Return to Codex without marking PASS if:
- any required source file in Section 6A is missing;
- `tsc --noEmit` cannot be made to pass;
- the blocked-gate path cannot be implemented without modifying an existing file;
- any forbidden scope action would be required.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order; not public-synced and no
public-facing artifact or public catalog claim is made in this batch.
