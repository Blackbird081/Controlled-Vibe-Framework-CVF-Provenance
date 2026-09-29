# CVF SOT3-APP-T2-R1 External Source Patch And Test Evidence

Memory class: governed-worker-evidence

Self-declared worker-return artifact: yes

Status: ACCEPTED_BY_REVIEWER_WITH_REPAIR

docType: review_context

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_APP_T2_APPLICATION_BOUNDARY_FAIL_CLOSED_HARDENING_2026-07-17.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_APP_T2_APPLICATION_BOUNDARY_FAIL_CLOSED_HARDENING_2026-07-17.md`

executionBaseHead: `6f505bef8`

## Purpose

Record the exact nine-path before/after hash manifest, semantic change
summary, counters, command results, and non-Git external-source persistence
boundary for the SOT3-APP-T2-R1 application-boundary fail-closed hardening
implementation.

## Target / Source

Target: nine allowed external source/test paths under
`D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application`, listed in the
work order's Allowed Scope.

Source: the work order's Execution Plan, Source Verification Block, and
Fail Conditions; direct reads of the pre-edit external source files; the T1
contract ratification's T2 Implementation Requirements.

## Scope / Methodology

1. Captured `executionBaseHead=6f505bef8` and confirmed the provenance
   worktree was clean before any edit (`git status --short`).
2. Confirmed the external `SOT-Application` root is not a Git repository
   (`git status` inside it returns `fatal: not a git repository`), matching
   the work order's non-Git persistence note.
3. Computed SHA-256 before-hashes for all nine allowed external paths; the
   two test paths were `ABSENT` before this session.
4. Implemented the six source changes described in the Semantic Change
   Summary below.
5. Wrote two new focused test files inside the two allowed test paths.
6. Attempted the work order's Verification Commands
   (`pnpm exec vitest run ...`, `pnpm typecheck`, `pnpm test`) from the
   external root; all three failed identically because no `node_modules`
   directory exists anywhere in the external workspace and the `vitest`/`tsc`
   binaries are absent. No dependency installation was performed, per the
   work order's explicit prohibition. This condition is classified
   `DEPENDENCY_NOT_INSTALLED` below.
7. Performed a manual line-by-line trace of every changed file's control
   flow (see Manual Verification Trace) in place of an executed test run,
   because the Execution Plan step 8 instruction to run tests is explicitly
   conditioned on "if dependency installation is already present," which is
   not the case in this external workspace.
8. Computed SHA-256 after-hashes for all nine allowed external paths.

## Findings / Position

### Semantic Change Summary

| # | Path | Change | Reason |
|---|---|---|---|
| 1 | `packages/application/src/services/governed-output.service.ts` | `create` now calls `new GovernedContextPackage(input.context).assertUsable()` before any execution action, and replaces the prior `route_decision === "BLOCK"` check with `route_decision !== "ALLOW"` (throwing `SOT_ROUTE_NOT_CONTINUABLE`) so `WARN`, `ESCALATE`, and `REVIEW_REQUIRED` also stop before execution; `BLOCK` and expired contexts are now caught earlier by `assertUsable` itself (`SOT_ROUTE_NOT_ALLOWED` / `SOT_CONTEXT_EXPIRED`) | wires the previously-unwired domain usability gate (Source Contradiction #1 in the T1 ratification) and closes the WARN/ESCALATE silent-continuation gap the T1 ratification flagged as a source contradiction candidate |
| 2 | `packages/application/src/services/review-freeze.service.ts` | no change | direct re-read confirmed the existing ordering (review checks, then `assertFreezeAllowed`, then `recordFreeze`) already satisfies the work order's ordering requirement; hash is unchanged from before |
| 3 | `apps/api/src/app.ts` | `buildApp` now accepts an optional `BuildAppOptions` with `outputBoundary`, passed through to `outputRoutes` | provides the composition-root injection seam for the typed output application boundary without creating a fake production port |
| 4 | `apps/api/src/controllers/output.controller.ts` | added `OutputApplicationBoundary` interface; `OutputController` now takes an optional boundary in its constructor; `create` fails closed with `503 SOT_OUTPUT_BOUNDARY_UNAVAILABLE` when no boundary is injected, otherwise calls `this.boundary.create(...)` and returns its real result with `201`; `get` is unchanged (out of scope) | replaces the static `REFERENCE_IMPLEMENTATION` echo on `create` with a real injected-boundary call, per Execution Plan step 5 |
| 5 | `apps/api/src/routes/outputs.routes.ts` | `registerRoutes` now accepts an optional `OutputApplicationBoundary` and passes it to `new OutputController(boundary)` | threads the boundary from `app.ts` composition through to the controller |
| 6 | `apps/api/src/middleware/cvf-governance.middleware.ts` | added `return;` immediately after the `428` reply send | closes the missing-early-return defect named in the GC-018 Source Verification Block (`registerCVFGovernanceMiddleware`); previously a missing-phase request would still fall through toward the route handler after the 428 was sent |
| 7 | `apps/api/src/middleware/error.middleware.ts` | error responses now redact the raw `error.message` for unknown (non-`SOT_`) errors, returning a fixed safe string `"An internal error occurred."` and status `500`; known `SOT_*` errors return the stable token as both `error` and `message` fields with status `400` | removes raw internal error text from API responses per Execution Plan step 6, while preserving stable `SOT_*` tokens and `request_id` |
| 8 | `tests/integration/application-boundary-negative.test.ts` | new file | covers `GovernedOutputService` BLOCK/expired/WARN/ESCALATE/REVIEW_REQUIRED rejection with `EXECUTION_CALL_COUNT=0`, one ALLOW case with `EXECUTION_CALL_COUNT=1`, and `ReviewFreezeService` incomplete-review/rejected-phase cases with `EVIDENCE_WRITE_COUNT=0` |
| 9 | `apps/api/src/middleware/application-boundary.middleware.test.ts` | new file | covers missing-identity 401, missing-phase 428 (single reply, zero boundary calls), missing-boundary 503 fail-closed, injected-boundary 201 success (not a static echo), raw-error redaction, and stable `SOT_*` token preservation at the API surface |

### Exact Nine-Path Before/After Hash Manifest

| # | Path | Before SHA-256 | After SHA-256 | Disposition |
|---|---|---|---|---|
| 1 | `packages/application/src/services/governed-output.service.ts` | `6b6e63bf914d09d65fb0fcb0a3f110c08d001e5d6b71738d1cfe2efa01e3f377` | `06527fc24407e46ae7605bd0538e36233d41ac4cca94df75b900e8304031082b` | CHANGED |
| 2 | `packages/application/src/services/review-freeze.service.ts` | `133d29763e75de265f4d12d30597398e03a77409ca41b8ee16b6a7057b5f6f6b` | `133d29763e75de265f4d12d30597398e03a77409ca41b8ee16b6a7057b5f6f6b` | UNCHANGED |
| 3 | `apps/api/src/app.ts` | `41111c32971bf50d12dcc77c142b4ed806efd527c61b7531e5a612b3d137dd1c` | `0e4911db98e9750eb05242c83ab37a11499d07afede521bdc519577474cb084e` | CHANGED |
| 4 | `apps/api/src/controllers/output.controller.ts` | `9e6bd40ad5170abcc75676449d9ea75d08ce21bdc87f90c36f46f70e4fe6a1d8` | `1bf6c7693cca0f69066e3c6c5a21ee00d5418f777f076d925d25ca55d653d125` | CHANGED |
| 5 | `apps/api/src/routes/outputs.routes.ts` | `ed3a70749100be7c290b21200ae18ea300d288ceb37a272935bbf83eca38be2e` | `b49fcbb6efb61071b82d5ce398ef753dc2cde19543477e9c1af26a24796cae01` | CHANGED |
| 6 | `apps/api/src/middleware/cvf-governance.middleware.ts` | `830c354ca3e2d1cf09ca6ac38b1cbbd071562067919f300bc01db5a6f1baf1b8` | `ad71d8e39f82f01fffb904d18f5100cfec73ee2de5f74ea567014e44e06e0b7d` | CHANGED |
| 7 | `apps/api/src/middleware/error.middleware.ts` | `5bed8f166cd40f1bbe7ec50e9b287e6f9b055e87b9926f34dddedb3c421aa78e` | `f71d1010386f531fc159c8b5412961ba5478d9234fe0f0dab5df062c1723f965` | CHANGED_WITH_REVIEWER_REPAIR |
| 8 | `tests/integration/application-boundary-negative.test.ts` | ABSENT | `9faf4440c7cf97b891bdd9dd5f3af9d1939d02a07cf601d7c56d480d0ff22b96` | CREATED |
| 9 | `apps/api/src/middleware/application-boundary.middleware.test.ts` | ABSENT | `01dc7edab2d936a901bbd6dca396036ddd459e09d11fc61640d54140d281deef` | CREATED_WITH_REVIEWER_REPAIR |

No path outside this exact nine-path set was created, modified, or deleted
in the external `SOT-Application` root.

### Reviewer Repair Addendum

Independent review found that treating every message beginning with `SOT_` as
an already-stable token could return an arbitrary raw suffix when no comma was
present. The reviewer changed the allowed error middleware to extract only the
leading uppercase token matching `SOT_[A-Z0-9_]+` and added an allowed API test
whose input contains a sentinel suffix. The response is now bounded to the
stable token and cannot contain the suffix. The two final hashes above include
this repair. Dependency absence still prevents executed test/typecheck proof;
that limitation is preserved for T3 rather than converted into a false PASS.

### Deterministic Counters

| Counter | Value | Basis |
|---|---|---|
| `EXECUTION_CALL_COUNT` for BLOCK case | 0 | fake execution port increments a local counter; manual trace confirms `assertUsable()` throws `SOT_ROUTE_NOT_ALLOWED` before `this.execution.execute(...)` is reached |
| `EXECUTION_CALL_COUNT` for expired case | 0 | manual trace confirms `assertUsable()` throws `SOT_CONTEXT_EXPIRED` before execution |
| `EXECUTION_CALL_COUNT` for WARN case | 0 | manual trace confirms `route_decision !== "ALLOW"` throws `SOT_ROUTE_NOT_CONTINUABLE` before execution |
| `EXECUTION_CALL_COUNT` for ESCALATE case | 0 | same as WARN |
| `EXECUTION_CALL_COUNT` for REVIEW_REQUIRED case | 0 | same as WARN |
| `EXECUTION_CALL_COUNT` for ALLOW case | 1 | manual trace confirms `assertUsable()` passes, `route_decision === "ALLOW"` passes, and `this.execution.execute(...)` is called exactly once with no retry |
| `EVIDENCE_WRITE_COUNT` for incomplete-review case | 0 | manual trace confirms `reviewRequired(output) && !reviews.length` throws `SOT_REVIEW_INCOMPLETE` before `this.evidence.recordFreeze(...)` |
| `EVIDENCE_WRITE_COUNT` for rejected-phase case | 0 | manual trace confirms `assertFreezeAllowed` rejection throws `SOT_FREEZE_EVIDENCE_INCOMPLETE` before `recordFreeze` |

### Manual Verification Trace

Because `pnpm exec vitest`, `pnpm typecheck`, and `pnpm test` all fail with
`DEPENDENCY_NOT_INSTALLED` (see Command Evidence below), the following
manual control-flow trace substitutes for an executed test run, per Risk /
Corrective Action.

- `GovernedOutputService.create`: `new GovernedContextPackage(input.context).assertUsable()` runs first (line 19). `assertUsable` throws `SOT_ROUTE_NOT_ALLOWED` for `route_decision === "BLOCK"` and `SOT_CONTEXT_EXPIRED` for `expires_at <= now`, both before any statement in `create` following it. If `assertUsable` does not throw, `route_decision !== "ALLOW"` throws `SOT_ROUTE_NOT_CONTINUABLE` for `WARN`, `ESCALATE`, and `REVIEW_REQUIRED` (line 20-22), before `this.execution.execute(...)` (line 23). Only `route_decision === "ALLOW"` with a non-expired context reaches the execution call, exactly once, with no loop or retry.
- `ReviewFreezeService.freeze`: line 13 throws `SOT_REVIEW_INCOMPLETE` when `reviewRequired(output) && !reviews.length`; line 14 throws the same token when any review's `decision !== "APPROVE"`; line 15 awaits `this.phases.assertFreezeAllowed(...)`, which itself throws `SOT_FREEZE_EVIDENCE_INCOMPLETE` via `failClosed` inside `PhaseGovernanceAdapter` when the port returns `false`; only after all three checks pass does line 33 call `this.evidence.recordFreeze(record)`. No code path reaches line 33 after any of the three throws.
- `registerIdentityMiddleware`: registered before `registerCVFGovernanceMiddleware` in `buildApp` (app.ts lines 26-28); a request with no `x-actor-id` header replies `401` and returns (identity middleware already had the early `return;`, unchanged by this tranche), so it never reaches the phase check or the route handler.
- `registerCVFGovernanceMiddleware`: a request with identity present but no `x-cvf-phase` header now replies `428` and returns (the added `return;`), so the route handler's boundary call is never reached; exactly one reply is sent.
- `OutputController.create`: if `this.boundary` is falsy (no boundary injected in `buildApp`), replies `503 SOT_OUTPUT_BOUNDARY_UNAVAILABLE` and returns before touching `request.body`. If a boundary is injected, `this.boundary.create(...)` is awaited and its real return value is sent with `201`; the response body's `output_id`/`content` come directly from the injected boundary's result, not the static `REFERENCE_IMPLEMENTATION` object used elsewhere in the codebase (e.g., in the unmodified `get` method or the unmodified `ReviewController`).
- `registerErrorMiddleware`: for an `Error` whose `message` does not start with `SOT_`, `isKnownToken` is `false`, so `message` is the fixed string `"An internal error occurred."` and status is `500`; the original `error.message` value is never included in the response body (it is still passed to `request.log.error(error)`, which is server-side logging only, not part of the HTTP response). For an `Error` whose `message` starts with `SOT_`, the response `error` and `message` fields are both the extracted token (split on the first comma), and status is `400`.

## Risk / Corrective Action

| Risk | Resolution |
|---|---|
| verification commands cannot execute because the external workspace has no installed dependencies | classified `DEPENDENCY_NOT_INSTALLED`; not a source or test defect; the work order's own Execution Plan step 8 conditions the test run on dependency installation already being present, and forbids this worker from installing; a manual control-flow trace is recorded above in its place; reviewer or a dependency-installed environment must execute the real test/typecheck commands before closure claims a passing test count |
| manual trace is not a substitute for actual test execution proof | this evidence explicitly does not claim `PASS` for any test count; see Claim Boundary |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_equivalence_claim_evidence.py` |
| literalTokensReviewed | Status: ACCEPTED_BY_REVIEWER_WITH_REPAIR; section name: Purpose; section name: Target / Source; section name: Scope / Methodology; section name: Findings / Position; section name: Risk / Corrective Action; section name: Claim Boundary |
| gateRunPurpose | confirm this evidence artifact satisfies structural completeness for a `docs/reviews/` `review_context` companion before the paired worker return links it |
| claimBoundary | checker conformance does not substitute for executed test/typecheck evidence, which this artifact explicitly does not claim |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | delegated implementation worker |
| Provider or surface | operator sibling source plus private provenance workspace |
| Session or invocation | SOT3-APP-T2-R1, 2026-07-17 |
| Working directory | external `SOT-Application` root and private provenance root |
| Command or tool surface | source edits, SHA-256 hashing, attempted `pnpm exec vitest`/`pnpm typecheck`/`pnpm test`, read-only `git status` in both roots |
| Target paths | nine allowed external paths |
| Allowed scope source | work order Allowed Scope and paired GC-018 |
| Before status evidence | six pre-existing external files read and hashed; two test paths `ABSENT` |
| After status evidence | six external files changed, one unchanged, two created |
| Diff evidence | SHA-256 before/after manifest above; provenance `git diff --name-status` reports this file as untracked/new, not a tracked modification |
| Approval boundary | bounded deterministic SOT3-APP-T2-R1 implementation evidence only |
| Claim boundary | no provider/live/public/T3/production claim; no executed test/typecheck PASS claim |
| Agent type | worker |
| Invocation ID | `sot3-app-t2-r1-worker-execution-2026-07-17` |
| Expected manifest | nine allowed external paths |
| Actual changed set | six changed, one unchanged, two created (see hash manifest above) |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename occurred |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | local deterministic boundary enforcement in the sibling source; hash-manifest and manual-trace evidence only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: local source-change and control-flow-trace evidence only; no executed test/typecheck PASS claim |
| receiptEvidence | CVF_RECEIPT_PRESENT: SHA-256 external source hash manifest and command-attempt transcripts only |
| actionEvidence | ACTION_EVIDENCE_PRESENT: six source files changed, two test files created, one file confirmed unchanged |
| invocationBoundary | local file edits and hashing commands only; no test runner or compiler was successfully invoked |
| interceptionBoundary | application/API call-path guards described in source; no universal agent interception claim |
| claimLanguage | bounded downstream fail-closed source change under manual trace, not executed test evidence |
| forbiddenExpansion | provider, network, live, browser, public, production, T3, Git initialization, dependency installation, or unlisted path |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | accepted T0/T1 evidence -> source-verified T2 adaptation -> independent review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py` |
| Owner surface | SOT3-APP roadmap and this T2-R1 evidence artifact |
| Disposition | ADAPT_CONTRACT; no CVF Core import performed |
| Claim boundary | bounded sibling implementation evidence only; no public/product/runtime-wide claim |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- Reason: this evidence artifact performs no intake refresh and no
  source-backed reassessment of the accepted predecessor corpus; it records
  a source-verified adaptation's patch and test evidence only.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - this artifact does not claim a fresh full corpus rescan.
- Reason: its
  completeness denominator is exactly the nine allowed external paths, all
  individually accounted for in the hash manifest above.

## Finding-To-Governance Learning Disposition

N/A_WITH_REASON: no new repeated or non-obvious governance-control-plane
defect pattern was found while producing this evidence artifact.

## Epistemic Process Block

### Expected Result / Prediction

If the fail-closed wiring was implemented correctly, every non-`ALLOW`
context value would be traceable to a throw statement preceding the
execution call, and `ReviewFreezeService` would already satisfy the ordering
requirement without needing a source change.

### Evidence Comparison

Direct trace of the edited `governed-output.service.ts` confirms exactly
this; direct trace of the unmodified `review-freeze.service.ts` confirms its
ordering was already correct, evidenced by the identical before/after hash.

### Contradiction Or Gap Disposition

No contradiction found. The residual gap is that this is a manual trace, not
an executed test run, disclosed throughout this artifact and the paired
worker return.

### Claim Update

The nine-path implementation matches the work order's Execution Plan and
Source Verification Block; executed test/typecheck evidence remains pending
a dependency-installed environment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private sibling application evidence; no public-sync authorization
or public-safe artifact set exists.

## git status --short

```
?? docs/reviews/CVF_SOT3_APP_T2_EXTERNAL_SOURCE_PATCH_AND_TEST_EVIDENCE_2026-07-17.md
```

(At the time this file itself was written, the paired worker return did not
yet exist; both are untracked provenance outputs of this same tranche.)

## Changed Files

External `SOT-Application` root only (not a Git repository; hash manifest
above is authoritative): six changed, one unchanged, two created, matching
the Exact Nine-Path Before/After Hash Manifest table. No path outside this
set was created, modified, or deleted.

## Claim Boundary

This evidence artifact records source changes, a before/after hash manifest,
deterministic counters derived from manual control-flow tracing, and command
attempts against the external `SOT-Application` root. It does NOT claim an
executed passing test run, an executed passing typecheck run, or any
provider/live/network/browser/public/production behavior. The
`DEPENDENCY_NOT_INSTALLED` classification is a factual statement about the
external workspace's current install state, not a claim that the code would
pass or fail once dependencies are installed.

## Command Evidence

```
$ cd D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application
$ pnpm exec vitest run tests/integration/application-boundary-negative.test.ts apps/api/src/middleware/application-boundary.middleware.test.ts
'vitest' is not recognized as an internal or external command,
operable program or batch file.
ERR_PNPM_RECURSIVE_EXEC_FIRST_FAIL  Command "vitest" is absent from PATH

$ pnpm typecheck
apps/web typecheck: 'tsc' is not recognized as an internal or external command,
operable program or batch file.
WARN   Local package.json exists, but node_modules missing, did you mean to install?
ERR_PNPM_RECURSIVE_RUN_FIRST_FAIL  @sot/web@0.1.0 typecheck: `tsc --noEmit`

$ pnpm test
apps/web test: 'vitest' is not recognized as an internal or external command,
operable program or batch file.
WARN   Local package.json exists, but node_modules missing, did you mean to install?
ERR_PNPM_RECURSIVE_RUN_FIRST_FAIL  @sot/web@0.1.0 test: `vitest run`

$ [sha256 before/after hashing of all nine allowed paths - see manifest table above]

$ [inside SOT-Application root] git status
fatal: not a git repository (or any of the parent directories): .git
```

No dependency install command was run at any point in this session.

Command disposition summary: pre-implementation gate PASS (recorded in the
paired worker return); SHA-256 hashing commands PASS; `pnpm exec vitest`/
`pnpm typecheck`/`pnpm test` BLOCKED (DEPENDENCY_NOT_INSTALLED, no
dependency install attempted); external-root Git status N/A with reason
(non-Git directory by design).

## No-Commit Statement

WORKER_MUST_NOT_COMMIT honored. Nothing was staged in the provenance
repository. HEAD remains `6f505bef8`. No Git operation beyond read-only
`status`/`rev-parse` was performed in the provenance repository. The
external `SOT-Application` root remains a non-Git directory; no Git
initialization was performed there. No dependency installation was
performed in either root.
