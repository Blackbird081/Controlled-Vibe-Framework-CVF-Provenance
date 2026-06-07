# CVF Agent Work Order: DSCP-T2 Standard Contract Authoring

Memory class: POINTER_RECORD

Status: CLOSED_PASS_BOUNDED

Template: `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
(post-`fce62cd3` version with Worker Pending-Return Gate section 6D)

Commit mode: `WORKER_MUST_NOT_COMMIT`

completionReviewPath: `docs/reviews/CVF_DSCP_T2_STANDARD_CONTRACT_AUTHORING_COMPLETION_2026-06-07.md`

dispatchBaseHead: `6535568d`
executionBaseHead: `6535568d`
closureBaseHead: `6535568d`

Status token rule:
- Worker must not change `Status` field.
- Reviewer/committer changes `Status` to `CLOSED_PASS_BOUNDED` after
  committed-range gates pass.

---

## Purpose

Author TypeScript contract interfaces and unit tests for the domain-agnostic
governance scan -> classify -> pack -> retrieve standard schema accepted in
DSCP-T1. Convert the 8 doc-only interface proposals from the DSCP-T1 schema
proposal into compilable TypeScript type contracts with shape validation
test coverage in `CVF_CONTROL_PLANE_FOUNDATION`.

## Scope / Target / Owner Boundary

Target: two new files in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/`.

- `src/dscp.governed.context.contract.ts` - 8 exported types
- `tests/dscp.governed.context.contract.test.ts` - shape validation tests

Owner boundary: worker owns authoring the two new files and the worker
return packet. Reviewer/committer (Codex) owns review, commit, and
session continuity update. No existing file is in scope for modification.

## 1. Authority Chain

- Operator authorized DSCP-T2 on 2026-06-07.
- GC-018: `docs/baselines/CVF_GC018_DSCP_T2_STANDARD_CONTRACT_AUTHORING_2026-06-07.md`
- Predecessor: DSCP-T1 `CLOSED_PASS_BOUNDED` at `62fa6943`
- Active handoff: `AGENT_HANDOFF_V17_2026-06-07.md`
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`

---

## 2. Transfer Objective

Author the TypeScript contract interfaces and unit tests for the
domain-agnostic scan -> classify -> pack -> retrieve standard schema
accepted in DSCP-T1.

Deliverables:
1. `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts`
   - 8 exported types compiled from the DSCP-T1 schema proposal
2. `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.governed.context.contract.test.ts`
   - shape validation and boundary tests; all vitest PASS

---

## 3. Source Packet

Prerequisites verified:
- DSCP-T1 schema proposal: `docs/reference/CVF_DSCP_T1_SCHEMA_PROPOSAL_2026-06-07.md`
  `Status: CLOSED_PASS_BOUNDED`
- GC-018 (T2): `docs/baselines/CVF_GC018_DSCP_T2_STANDARD_CONTRACT_AUTHORING_2026-06-07.md`
  `Status: ACTIVE_BASELINE`
- CPF module: `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/` (existing)

---

## 4. Agent Roles

Worker: Claude (implementation agent)
Reviewer/committer: Codex

---

## 5. Execution Plan

### Commit Mode And Base-Anchor Lifecycle

1. Capture `executionBaseHead` via `git rev-parse --short HEAD` before
   any edit. Record in worker return.
2. Confirm working tree is clean except for DSCP-T2 artifacts authored in
   this session.
3. Verify GC-018, schema proposal, and roadmap are present at paths in
   Section 3 before proceeding.
4. If any required source file is missing, stop and return
   `BLOCKED_SOURCE_NOT_FOUND`.

### Work Plan

5. Author `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts`
   containing all 8 exports from the schema proposal exactly as proposed
   in `docs/reference/CVF_DSCP_T1_SCHEMA_PROPOSAL_2026-06-07.md`.
6. Author `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.governed.context.contract.test.ts`
   with shape validation and boundary tests covering all 8 types.
7. Run `tsc --noEmit` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/`.
   All TypeScript errors must be resolved before returning.
8. Run vitest focused on the new test file:
   `npx vitest run tests/dscp.governed.context.contract.test.ts`
   All tests must PASS before returning.
9. Stage both new files: `git add` them (do not commit).
10. Run Worker Pending-Return Gate checks (Section 6D).
11. Write worker return packet.
12. Stage worker return packet.

---

## 6A. Source Verification Table

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| `ContextPackagerRequest` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/context.packager.contract.ts` | lines 29-38 | `ContextPackagerRequest` | `context.packager.contract.ts` | ACCEPT |
| `TypedContextPackage` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/context.packager.contract.ts` | lines 49-59 | `TypedContextPackage` | `context.packager.contract.ts` | ACCEPT |
| `GovernanceGateSet` proposal | `docs/reference/CVF_DSCP_T1_SCHEMA_PROPOSAL_2026-06-07.md` | lines 72-86 | `GovernanceGateSet` | schema proposal Section 2.1 | ACCEPT |
| `GovernedArtifactDescriptor` proposal | `docs/reference/CVF_DSCP_T1_SCHEMA_PROPOSAL_2026-06-07.md` | lines 100-125 | `GovernedArtifactDescriptor` | schema proposal Section 2.2 | ACCEPT |
| `GovernanceContextEnvelope` proposal | `docs/reference/CVF_DSCP_T1_SCHEMA_PROPOSAL_2026-06-07.md` | lines 144-160 | `GovernanceContextEnvelope` | schema proposal Section 3.1 | ACCEPT |
| `GovernedContextPackRequest` proposal | `docs/reference/CVF_DSCP_T1_SCHEMA_PROPOSAL_2026-06-07.md` | lines 170-176 | `GovernedContextPackRequest` | schema proposal Section 3.2 | ACCEPT |
| `GovernedContextPackageEvidence` proposal | `docs/reference/CVF_DSCP_T1_SCHEMA_PROPOSAL_2026-06-07.md` | lines 193-210 | `GovernedContextPackageEvidence` | schema proposal Section 3.3 | ACCEPT |
| `GovernedContextPackage` proposal | `docs/reference/CVF_DSCP_T1_SCHEMA_PROPOSAL_2026-06-07.md` | lines 212-218 | `GovernedContextPackage` | schema proposal Section 3.3 | ACCEPT |
| `ContentDeliveryClass` proposal | `docs/reference/CVF_DSCP_T1_SCHEMA_PROPOSAL_2026-06-07.md` | lines 230-234 | `ContentDeliveryClass` | schema proposal Section 4.1 | ACCEPT |
| `GovernedRetrievalReceipt` proposal | `docs/reference/CVF_DSCP_T1_SCHEMA_PROPOSAL_2026-06-07.md` | lines 244-276 | `GovernedRetrievalReceipt` | schema proposal Section 4.2 | ACCEPT |
| CPF src/ target directory | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/context.packager.contract.ts` | line 1 | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/` | CPF module | ACCEPT |
| CPF tests/ target directory | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/context.packager.test.ts` | line 1 | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/` | CPF module | ACCEPT |
| DSCP roadmap T2 scope | `docs/roadmaps/CVF_DSCP_DOMAIN_AGNOSTIC_SCAN_CONTEXT_PACK_READINESS_ROADMAP_2026-06-07.md` | lines 102-114 | `DSCP-T2 Standard Contract Authoring` | roadmap tranche plan | ACCEPT |
| GC-018 (T2) | `docs/baselines/CVF_GC018_DSCP_T2_STANDARD_CONTRACT_AUTHORING_2026-06-07.md` | lines 1-12 | `ACTIVE_BASELINE` | GC-018 baseline | ACCEPT |

---

## 6B. Task Execution

### New Files

| File | Action | Path |
|---|---|---|
| TypeScript contract | CREATE | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` |
| TypeScript test | CREATE | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.governed.context.contract.test.ts` |

### Forbidden Scope

- Modifying any existing `.ts` file (CPF src or tests, or any other module)
- Adding any export to `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/index.ts`
  (barrel export is a separate authorized action)
- Runtime logic, class bodies, service implementations
- Corpus ingestion, OCR, body extraction
- Provider/API calls or live proof
- Public-sync or push to public repo
- LPCI2 T12 promotion or eligibility mutation
- Worker-side commit or push

Risk ceiling: R2 (new TypeScript files; no runtime, no existing mutation)

---

## Roadmap-To-Work-Order Trace Matrix

| Roadmap / GC-018 requirement | Work-order instruction | Evidence target | Status |
|---|---|---|---|
| DSCP-T2: author TypeScript contracts | Section 5 step 5: create contract file | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | READY |
| DSCP-T2: author tests | Section 5 step 6: create test file | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.governed.context.contract.test.ts` | READY |
| DSCP-T2: TypeScript compilation pass | Section 5 step 7: `tsc --noEmit` PASS | `tsc --noEmit` zero errors recorded in worker return | READY |
| DSCP-T2: all tests PASS | Section 5 step 8: vitest PASS | vitest result recorded in worker return | READY |
| DSCP-T2: no existing file modified | Forbidden scope list | `git status --short` at return | READY |
| DSCP-T2: worker must not commit | `WORKER_MUST_NOT_COMMIT` commit mode | staged files; reviewer commits | READY |
| GC-018 boundary: no runtime, no T3 | Forbidden scope list | worker return boundary statement | READY |

## Worker Autonomy / No-Question Rule

The worker proceeds without operator confirmation for all non-destructive
allowed-scope actions: reading source files, authoring the two new TypeScript
files, running `tsc --noEmit`, running vitest, running component gate checks,
staging output files.

Repair TypeScript type errors and test failures directly. Escalate only if:
a source-verified interface requires a runtime import that does not exist,
or a forbidden-scope action would be required to fix a type error.

## Reviewer Closure Conversion Block

```text
completionReviewPath: `docs/reviews/CVF_DSCP_T2_STANDARD_CONTRACT_AUTHORING_COMPLETION_2026-06-07.md`
reviewerOwnedClosurePaths:
- `docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T2_STANDARD_CONTRACT_AUTHORING_FOR_CLAUDE_2026-06-07.md`
- `docs/reviews/CVF_DSCP_T2_STANDARD_CONTRACT_AUTHORING_WORKER_RETURN_2026-06-07.md`
- `docs/reviews/CVF_DSCP_T2_STANDARD_CONTRACT_AUTHORING_COMPLETION_2026-06-07.md`
- `docs/roadmaps/CVF_DSCP_DOMAIN_AGNOSTIC_SCAN_CONTEXT_PACK_READINESS_ROADMAP_2026-06-07.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V17_2026-06-07.md`
closureResidueCheck: PASS
reviewerConversionStatus: worker pending tokens resolved in closure batch
```

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `AGENT_HANDOFF_V17_2026-06-07.md`
4. `docs/baselines/CVF_GC018_DSCP_T2_STANDARD_CONTRACT_AUTHORING_2026-06-07.md`
5. `docs/reference/CVF_DSCP_T1_SCHEMA_PROPOSAL_2026-06-07.md`
6. `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/context.packager.contract.ts`

## Write Ownership

Owned paths (new files only; no existing file modified):

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts`
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.governed.context.contract.test.ts`
- `docs/reviews/CVF_DSCP_T2_STANDARD_CONTRACT_AUTHORING_WORKER_RETURN_2026-06-07.md`

All session continuity and registry files are reviewer-owned.

## Pre-Flight Checks

Capture `executionBaseHead` via `git rev-parse --short HEAD` before any edit.
Confirm working tree is clean except for DSCP-T2 artifacts authored in this
session. Verify that GC-018, schema proposal, and roadmap files are present
at paths cited in Section 3 before proceeding.

If any required source file in Section 6A is missing, stop and return
`BLOCKED_SOURCE_NOT_FOUND`.

---

## 6C. Work-Order Fulfillment Manifest

## Required Artifact Manifest

| Path | Output stage | Purpose |
|---|---|---|
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | worker return | 8 exported domain-agnostic governance interfaces |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.governed.context.contract.test.ts` | worker return | shape validation and governance lock tests |
| `docs/reviews/CVF_DSCP_T2_STANDARD_CONTRACT_AUTHORING_WORKER_RETURN_2026-06-07.md` | worker return | worker evidence packet for Codex review |

---

## 6D. Worker Pending-Return Gate

| Component | Scope trigger | Verification command | Expected result |
|---|---|---|---|
| Execution anchor | every worker run | `git rev-parse --short HEAD` | HEAD at dispatch or later; record in worker return |
| Pending worktree | `WORKER_MUST_NOT_COMMIT` | `git status --short` | new files staged; no `.ts` existing file modified |
| TypeScript compilation | new `.ts` file authored | `npx tsc --noEmit` in CPF directory | zero type errors |
| Vitest | new test file authored | `npx vitest run tests/dscp.governed.context.contract.test.ts` in CPF directory | all tests PASS |
| Markdown structural completeness | new governed markdown files | `python governance/compat/check_markdown_structural_completeness.py --base <dispatchBaseHead> --head HEAD --enforce` | COMPLIANT |
| Finding-To-Governance learning | output files may record findings | `python governance/compat/check_finding_to_governance_learning.py --base <dispatchBaseHead> --head HEAD --enforce` | COMPLIANT |
| Machine Closure Package | output files reference closure context | `python governance/compat/check_machine_closure_package.py --base <dispatchBaseHead> --head HEAD --enforce` | COMPLIANT |
| Dispatch quality | this work order is a dispatch packet | `python governance/compat/check_work_order_dispatch_quality.py --base <dispatchBaseHead> --head HEAD --enforce` | COMPLIANT |

---

## 7. Dissent And Review Ledger

No dissent recorded at dispatch.

---

## 8. Integration Decision

Integration decision: APPROVED. DSCP-T1 schema proposal is
`CLOSED_PASS_BOUNDED`; all 8 interface proposals are source-verified.
TypeScript contract authoring is bounded to the exact interface shapes
in the schema proposal with no added logic.

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

1. `dscp.governed.context.contract.ts` created with all 8 exports matching
   schema proposal shapes exactly.
2. `rawContentReleased: false`, `canBypassGovernance: false`,
   `rawSourceReleased: false` typed as literal `false`, not `boolean`.
3. `tsc --noEmit` completes with zero errors.
4. All vitest tests PASS (30 or more tests).
5. No existing `.ts` file modified.
6. All four governance component gates PASS on committed range.
7. Worker return packet present with all required evidence.

## Review Gate

Codex must review the DSCP-T2 worker return before deciding T2 closure.
After T2 closes, Codex may open the DSCP-T3 Runtime Pilot work order only
with a fresh operator-authorized scope expansion.

## Operator Checkpoint

operator.checkpoint.waiver: DSCP-T2 contract authoring is bounded to two
new type-only files in CPF. Operator input is not required for execution.
Operator input IS required before DSCP-T3 runtime pilot, corpus ingestion,
any provider call, or any public-sync.

## 9. Completion Evidence

| Evidence item | Path | Status |
|---|---|---|
| TypeScript contract (staged) | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | PASS |
| TypeScript test (staged) | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.governed.context.contract.test.ts` | PASS |
| Worker return packet | `docs/reviews/CVF_DSCP_T2_STANDARD_CONTRACT_AUTHORING_WORKER_RETURN_2026-06-07.md` | PASS |
| TypeScript compilation | `tsc --noEmit` result | PASS |
| Vitest result | vitest run result | PASS |
| Committed-range gate results | reviewer-owned closure gates | PASS |

---

## Claim Boundary

This work order claims: dispatch authorization for DSCP-T2 TypeScript
contract authoring and test coverage, bounded to two new files in
`EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/`. It does not claim: runtime
pipeline implementation, corpus ingestion, provider calls, DSCP-T3 pilot,
LPCI2 T12 promotion, public-sync, production readiness, or public readiness.

---

## Acceptance Receipt Assertion Matrix

DSCP-T2 authors `GovernedRetrievalReceipt` as a TypeScript interface definition.
No runtime retrieval query or provider call is made in this tranche.

| Required value | Observed value | Status |
|---|---|---|
| No runtime query performed | Worker confirms: no provider call, no live retrieval, no LLM query in DSCP-T2 | N/A with reason: contract authoring only; no runtime query executed |
| No query receipt generated | `GovernedRetrievalReceipt` is authored as an interface type only; no instance created at runtime | N/A with reason: type contract only |

---

## 9. Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED`; reviewer-owned closure conversion complete | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_DSCP_T2_STANDARD_CONTRACT_AUTHORING_COMPLETION_2026-06-07.md` | reviewer completion artifact added in closure batch | PASS |
| Roadmap state | `docs/roadmaps/CVF_DSCP_DOMAIN_AGNOSTIC_SCAN_CONTEXT_PACK_READINESS_ROADMAP_2026-06-07.md` | DSCP-T2 row updated to `CLOSED_PASS_BOUNDED` by reviewer | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | DSCP-T2 contract/test scope registered in GC-051 by reviewer | PASS |
| Registry Markdown | `CVF_SESSION_MEMORY.md` and `AGENT_HANDOFF_V17_2026-06-07.md` | session markdown sync in reviewer closure sequence | PASS |
| External evidence digest | external artifact path | no external artifact produced | N/A with reason: all evidence is in-repo source, tests, and governance docs |
| System loop interlock | no system-loop mutation authorized | DSCP-T2 is contracts + tests only; no runtime loop changed | N/A with reason: contracts + tests only |
| Session continuity | `CVF_SESSION_MEMORY.md` and `AGENT_HANDOFF_V17_2026-06-07.md` | session sync in reviewer closure sequence | PASS |

---

## 10. Reviewer Checklist

Codex must verify before committing:

- Contract file exports exactly 8 types matching schema proposal shapes.
- `rawContentReleased: false`, `canBypassGovernance: false`,
  `rawSourceReleased: false` are typed as literal `false`, not `boolean`.
- Test file imports from `../src/dscp.governed.context.contract`.
- `tsc --noEmit` PASS recorded in worker return.
- Vitest all PASS recorded in worker return.
- No existing file modified (`git diff --name-only HEAD~1..HEAD` clean
  except for new files + governance docs).
- All four governance component gates PASS on committed range.

## Closure Checklist

- [x] TypeScript contract file created at specified path.
- [x] TypeScript test file created at specified path.
- [x] TypeScript compilation PASS recorded.
- [x] All vitest tests PASS recorded.
- [x] No existing `.ts` file modified.
- [x] All component governance gates PASS or pending-return exception recorded.
- [x] No forbidden scope action occurred.
- [x] Codex reviewed worker return.

## Return-To-Orchestrator Conditions

Worker returns to orchestrator when:
- Both new files staged and all Pending-Return Gate checks recorded; OR
- A `BLOCKED_SOURCE_NOT_FOUND` or `BLOCKED_FORBIDDEN_SCOPE` condition is hit.
