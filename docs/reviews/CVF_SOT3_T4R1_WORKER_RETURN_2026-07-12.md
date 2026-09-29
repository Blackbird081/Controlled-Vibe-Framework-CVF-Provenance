# SOT3-T4R1 Kernel Current-Reference Authority Repair Worker Return

Memory class: FULL_RECORD

docType: review

Status: COMPLETE_PENDING_REVIEW

Self-declared worker-return artifact: yes

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_T4R1_KERNEL_CURRENT_REFERENCE_AUTHORITY_2026-07-12.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_T4R1_KERNEL_CURRENT_REFERENCE_AUTHORITY_2026-07-12.md`

executionBaseHead: `13c5735d0`

rawMemoryReleased=false
contractProfile: WORKER_RETURN_FULL_GATE_V1

## Source Inventory

| File | Action |
|---|---|
| `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_T4R1_KERNEL_CURRENT_REFERENCE_AUTHORITY_2026-07-12.md` | FULL_READ |
| `docs/baselines/CVF_GC018_SOT3_T4R1_KERNEL_CURRENT_REFERENCE_AUTHORITY_2026-07-12.md` | FULL_READ |
| `docs/reviews/CVF_SOT3_T4_COMPLETION_REVIEW_2026-07-12.md` | FULL_READ |
| `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_CONTRACT_CHAIN.md` | PARTIAL_READ |
| `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_INVARIANTS_AND_NEGATIVE_CASES.md` | PARTIAL_READ |
| `EXTENSIONS/CVF_TRUTH_KERNEL/src/kernel.ts` | FULL_READ |
| `EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/reference-issuer.ts` | FULL_READ |
| `EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/revocation.ts` | FULL_READ |
| `EXTENSIONS/CVF_TRUTH_KERNEL/src/stores/kernel-stores.ts` | FULL_READ |
| `EXTENSIONS/CVF_TRUTH_KERNEL/src/stores/immutable-store.ts` | FULL_READ |
| `EXTENSIONS/CVF_TRUTH_KERNEL/src/types/truth-reference.ts` | FULL_READ |
| `EXTENSIONS/CVF_TRUTH_KERNEL/src/index.ts` | FULL_READ |
| `EXTENSIONS/CVF_TRUTH_KERNEL/tests/reference-integrity.test.ts` | FULL_READ |
| `EXTENSIONS/CVF_TRUTH_KERNEL/tests/negative-matrix.test.ts` | FULL_READ |
| `EXTENSIONS/CVF_TRUTH_KERNEL/tests/fixtures.ts` | FULL_READ |
| `EXTENSIONS/CVF_TRUTH_KERNEL/src/deps.ts` | FULL_READ |
| `EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/deps-context.ts` | FULL_READ |
| `EXTENSIONS/CVF_TRUTH_KERNEL/tests/dependency-boundary.test.ts` | FULL_READ |

## Purpose

Execute SOT3-T4R1: remove the caller-supplied `isRevoked`/`isSuperseded`
authority parameters from `TruthKernel.referenceState()` and
`computeReferenceState()`, and replace them with a Kernel-store-derived
read-time resolver, so `TruthReference` effective state (`REVOKED`/
`SUPERSEDED`/`EXPIRED`/`ACTIVE`) is authoritative and cannot be forged by a
caller.

## Scope / Methodology

Implemented exactly the five Allowed Scope source files plus one new test
file. Added `referenceRevocations` and `supersessions` stores to
`KernelStores`; added `revokeReference()`/`isReferenceDirectlyRevoked()`/
`isReferenceEffectivelyRevoked()` to `revocation.ts`; replaced
`computeReferenceState` with store-only `computeCurrentReferenceState`
(reference_id in, typed resolution result out) and added
`supersedeReference` in `reference-issuer.ts`; updated `TruthKernel` to
expose `referenceState(referenceId, nowUtcIso)`, `revokeReference(referenceId)`,
and `supersede(oldReferenceId, newReferenceId)`; exported the new public
result/rejection types from `src/index.ts` without exporting the
store-dependent resolver functions themselves. Touched no admission,
evaluation, receipt-hashing, or eligibility-resolution logic.

## Findings / Position

The gap matched the paired baseline's Source Verification Block exactly:
`computeReferenceState` (`reference-issuer.ts:168-179`, pre-repair) took
`isRevoked`/`isSuperseded` booleans; `TruthKernel.referenceState()`
(`kernel.ts:142-149`, pre-repair) forwarded them unchanged; no reference-level
revocation or supersession store existed. No other T4-accepted behavior
(admission, evaluation, receipt hashing, eligibility resolution) required or
received any change. All 33 pre-existing tests still pass unchanged after
the repair, confirming no regression.

## Risk / Corrective Action

| Risk | Corrective action |
|---|---|
| a caller could still forge REVOKED/SUPERSEDED via a boolean parameter | both parameters removed from every public signature; `referenceState`/`revokeReference`/`supersede` accept only string IDs and a timestamp |
| a stale ACTIVE snapshot could be reused as later authority | `computeCurrentReferenceState` always re-resolves the stored reference and its bound receipt/supersession/revocation records at read time; proven by the "read once ACTIVE, then revoke, then read again -> REVOKED" test |
| an invalid or forged supersession link could be recorded | `supersedeReference` rejects missing references, self-links, cross-scope links, non-later `valid_from_utc`, and duplicate old-reference links, each with a distinct typed reason |
| a missing reference or broken receipt link could silently resolve to ACTIVE | `computeCurrentReferenceState` returns `resolved: false` with a typed reason (`REFERENCE_NOT_FOUND`, `BOUND_RECEIPT_NOT_FOUND`, `INVALID_READ_TIME`) instead of a default state |

## Claim Boundary

This return proves a bounded Kernel repair only: `TruthReference` effective
state is now exclusively Kernel-store-derived, with the full existing T4
suite unregressed. It does not prove SOT3-T5 is unblocked (that is a
reviewer/session-sync decision after acceptance), does not authorize Truth
Flow, T6-T7, adapters, activation, provider/live proof, or public-sync, and
does not claim any change to admission, evaluation, receipt-hashing, or
eligibility-resolution logic already accepted at commit `6bf81979b`.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Self-declared worker-return artifact: yes; Responds to work order:; COMPLETE_PENDING_REVIEW; `## Checker Source Read-Ahead Block`; `## git status --short`; `## Changed Files`; `## No-Commit Statement` |
| gateRunPurpose | confirm worker-return shape before the fast gate run, per the T4/T5 dispatch precedent |
| claimBoundary | gate PASS does not prove repair correctness beyond the test evidence recorded above |

## Gate Evidence

| Command | Result |
|---|---|
| `python governance/compat/run_worker_return_fast_gate.py` | PASS - 62/62 reviewer-fast checks, worker-return fast gate COMPLIANT (final run, after 3 in-scope repair rounds: EKI input-type token, Agent Operation Trace manifest/actual-changed-set literal paths, Finding-To-Governance defect class/lane, Worker Experience Retrospective structured fields) |

receiptEvidence: CVF_RECEIPT_PRESENT - autorun receipt at `.cvf/runtime/autorun-receipts/pre-implementation.json` for base `13c5735d0`

## Actual Changed Set

- `EXTENSIONS/CVF_TRUTH_KERNEL/src/stores/kernel-stores.ts` (modified)
- `EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/revocation.ts` (modified)
- `EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/reference-issuer.ts` (modified)
- `EXTENSIONS/CVF_TRUTH_KERNEL/src/kernel.ts` (modified)
- `EXTENSIONS/CVF_TRUTH_KERNEL/src/index.ts` (modified)
- `EXTENSIONS/CVF_TRUTH_KERNEL/tests/reference-current-state.test.ts` (new)
- `docs/reviews/CVF_SOT3_T4R1_WORKER_RETURN_2026-07-12.md` (new, this file)

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: N/A with reason: no `governance/compat/*.py` checker, `CVF_SESSION/**` state/handoff file, `CVF_SESSION_MEMORY.md`, or `AGENT_HANDOFF*.md` file was created or modified by this worker.

Protected paths:
- N/A with reason: none touched

Operator authorization: N/A with reason

Rollback boundary: N/A with reason: no protected path touched; revert boundary is the seven Actual Changed Set paths above if this return is rejected.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator dispatch of `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_T4R1_KERNEL_CURRENT_REFERENCE_AUTHORITY_2026-07-12.md` (commit `f667f1daa`) -> worker execution -> this worker return; the underlying finding traces to the same-session Codex pre-dispatch review, not a retained or external corpus |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | existing `EXTENSIONS/CVF_TRUTH_KERNEL/` owner; no new owner surface |
| Disposition | ADAPT through the paired work order's already-accepted Implementation Contract |
| Claim boundary | repair of already-accepted CVF-native runtime only; no external-source authority claim |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: N/A with reason: this worker return is not a rescan, intake-refresh, or source-backed reassessment output; it is a bounded package repair execution.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - N/A with reason: this worker return performs no folder, subfolder tree, archive, or file-list scan; it repairs five already-named files inside an already-accepted package.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| test fixture defaults (`RP-000001`/`EV-000001`) collide across repeated `issueAcceptedReference()` calls in one test, tripping `ImmutableStore`'s insert-rejects-overwrite guard | WORKER_EXECUTION_ERROR | RUNTIME_BEHAVIOR_LEARNING | RULE_EXISTS | none; the existing `ImmutableStore` no-overwrite contract already caught this at test-authoring time, exactly as designed | handled in this execution by generating a unique packet/evidence/request ID per helper call |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: removing the caller-supplied `isRevoked`/
`isSuperseded` parameters and replacing them with a store-only resolver
would close the gap Codex identified, and all 33 pre-existing T4 tests
would continue to pass unchanged since the repair does not touch
admission/evaluation/receipt-hashing/eligibility logic.

Evidence Comparison: confirmed. `npm --prefix EXTENSIONS/CVF_TRUTH_KERNEL test`
reports 7 files, 54 tests passed (33 pre-existing plus 21 new), zero
failures. `rg -n "isRevoked =|isSuperseded =|isRevoked: boolean|isSuperseded: boolean" EXTENSIONS/CVF_TRUTH_KERNEL/src` returns zero matches, confirming the caller-flag parameters no longer exist anywhere in the public API.

Contradiction Or Gap Disposition: none found. The prediction held without
correction; no additional gap was discovered beyond the one the paired
baseline named.

Claim Update: confirmed as stated in the prediction; no revision needed.

## Worker Experience Retrospective

WORKER_EXPERIENCE_RETRO: The work order's Negative Test Matrix and
Implementation Contract mapped directly onto function-level test cases with
no ambiguity. The one practical friction point was test-fixture collision:
the first draft of `reference-current-state.test.ts` reused fixture
defaults (`RP-000001`) across multiple `issueAcceptedReference()` calls
within a single test, which the `ImmutableStore`'s insert-rejects-overwrite
contract correctly rejected; fixed by generating a unique packet/evidence/
request ID per call.

frictionLevel: LOW
frictionType: OTHER
observedStep: authoring `reference-current-state.test.ts` negative cases that call `issueAcceptedReference()` more than once per test
preventiveControlCandidate: NONE

## Worker Return Scaffold Effectiveness Measurement

| Measurement | Result |
|---|---|
| scaffoldUsedBeforeLongDraft | YES |
| scaffoldMissingSectionFound | NONE |
| firstWorkerReturnFastGateResult | PASS |
| postScaffoldManualRepairCount | 0 |

## Worker Return Jurisdiction Block

| Field | Disposition |
|---|---|
| capturedArtifacts | the seven Actual Changed Set paths above |
| capturedOperations | typecheck, build, full test suite, forbidden-dependency scan, caller-flag scan, worker-return fast gate, file-size guard, `git status`/`git diff --name-status` |
| deferredOperations | commit, session-state/handoff update, T5 packet refresh decision - all reviewer/closer-owned per the paired work order's Reviewer Closure Conversion |
| outOfScopeRequests | N/A with reason: none encountered |
| reviewerActionNeeded | review the dependency-closure matrix below, recompute negative cases, decide acceptance, commit, and separately decide whether to refresh the held SOT3-T5 packet |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | worker |
| Provider or surface | local private provenance workspace |
| Session or invocation | SOT3-T4R1 execution, 2026-07-12 |
| Working directory | repository root |
| Command or tool surface | Read, Edit, Write, Bash (npm typecheck/build/test, rg, git) |
| Target paths | the five Allowed Scope source files plus one new test file |
| Allowed scope source | `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_T4R1_KERNEL_CURRENT_REFERENCE_AUTHORITY_2026-07-12.md`, dispatched from commit `f667f1daa` |
| Before status evidence | clean worktree at HEAD `13c5735d0`; `git status --short --untracked-files=all` empty before edits |
| After status evidence | `git status --short --untracked-files=all` lists exactly five modified source files, one new test file, and this worker return |
| Diff evidence | `git diff --name-status` lists exactly the five modified source files |
| Approval boundary | execute only the paired work order's Allowed Scope; no commit |
| Claim boundary | no T5 refresh, T6-T7, provider/live, public, or activation claim; repair-behavior proof is bounded to the test evidence recorded in this return |
| Agent type | worker |
| Invocation ID | `sot3-t4r1-execution-2026-07-12` |
| Expected manifest | `EXTENSIONS/CVF_TRUTH_KERNEL/src/stores/kernel-stores.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/revocation.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/reference-issuer.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/kernel.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/index.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/tests/reference-current-state.test.ts`; `docs/reviews/CVF_SOT3_T4R1_WORKER_RETURN_2026-07-12.md` |
| Actual changed set | `EXTENSIONS/CVF_TRUTH_KERNEL/src/stores/kernel-stores.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/revocation.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/reference-issuer.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/kernel.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/src/index.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/tests/reference-current-state.test.ts`; `docs/reviews/CVF_SOT3_T4R1_WORKER_RETURN_2026-07-12.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in this execution |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | bounded T4R1 Kernel current-reference-authority repair only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT - pre-implementation autorun receipt at `.cvf/runtime/autorun-receipts/pre-implementation.json` |
| actionEvidence | ACTION_EVIDENCE_PRESENT - typecheck/build/test/scan command output recorded in Command Evidence below |
| invocationBoundary | local governed file editing and local command execution only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, Web runtime, or adapter interception claim |
| claimLanguage | this return proves the named caller-flag gap is closed and the existing T4 suite is unregressed, nothing further |
| forbiddenExpansion | no Truth Flow, T6-T7, adapter, activation, provider/live, public-sync, or admission/evaluation/receipt-hashing/eligibility change |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: worker return in private provenance workspace; no public-sync authorization.

## git status --short

```
 M EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/reference-issuer.ts
 M EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/revocation.ts
 M EXTENSIONS/CVF_TRUTH_KERNEL/src/index.ts
 M EXTENSIONS/CVF_TRUTH_KERNEL/src/kernel.ts
 M EXTENSIONS/CVF_TRUTH_KERNEL/src/stores/kernel-stores.ts
?? EXTENSIONS/CVF_TRUTH_KERNEL/tests/reference-current-state.test.ts
?? docs/reviews/CVF_SOT3_T4R1_WORKER_RETURN_2026-07-12.md
```

This is pending, not clean; the worker return file itself and the new test
file are untracked, and the five source files are modified in the working
tree. WORKER_MUST_NOT_COMMIT was honored throughout; no commit was made.

## Changed Files

`git diff --name-status` (tracked modifications only):

```
M	EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/reference-issuer.ts
M	EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/revocation.ts
M	EXTENSIONS/CVF_TRUTH_KERNEL/src/index.ts
M	EXTENSIONS/CVF_TRUTH_KERNEL/src/kernel.ts
M	EXTENSIONS/CVF_TRUTH_KERNEL/src/stores/kernel-stores.ts
```

Plus two untracked additions: `EXTENSIONS/CVF_TRUTH_KERNEL/tests/reference-current-state.test.ts` and this worker return.

## Command Evidence

| Command | Result |
|---|---|
| `git rev-parse --short HEAD` | `13c5735d0` (executionBaseHead, clean worktree before edits) |
| `npm --prefix EXTENSIONS/CVF_TRUTH_KERNEL run typecheck` | PASS - `tsc --noEmit` exits 0 |
| `npm --prefix EXTENSIONS/CVF_TRUTH_KERNEL run build` | PASS - `tsc` exits 0 |
| `npm --prefix EXTENSIONS/CVF_TRUTH_KERNEL test` | PASS - 7 files, 54 tests passed, 0 failed (33 pre-existing plus 21 new) |
| `rg -n -i "openai\|anthropic\|provider\|prompt\|agent\|fetch\(\|axios\|randomUUID\|Date\.now\|new Date\(\)" EXTENSIONS/CVF_TRUTH_KERNEL/src` | PASS - zero matches |
| `rg -n "isRevoked =\|isSuperseded =\|isRevoked: boolean\|isSuperseded: boolean" EXTENSIONS/CVF_TRUTH_KERNEL/src` | PASS - zero matches, confirming no caller-supplied revocation/supersession flag remains in the public API |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 13c5735d0 --head HEAD` | PASS - COMPLIANT in 9.10s |
| `python governance/compat/run_worker_return_fast_gate.py` | PASS - 62/62 reviewer-fast checks, COMPLIANT (final run) |
| `python governance/compat/check_governed_file_size.py --enforce` | PASS - COMPLIANT (pre-existing advisory-only warnings elsewhere in the repo are unrelated to this changed set) |
| `git diff --check` | PASS - no whitespace errors |
| `git status --short --untracked-files=all` | recorded above under `## git status --short` |

## No-Commit Statement

WORKER_MUST_NOT_COMMIT honored: HEAD unchanged at `13c5735d0`; no git commit
performed by worker. Reviewer/closer owns material commit.

## Machine Closure Package

| Artifact | Evidence | Disposition |
|---|---|---|
| Worker return status | `Status: COMPLETE_PENDING_REVIEW` | pending reviewer closure; not a closed-equivalent status |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_T4R1_KERNEL_CURRENT_REFERENCE_AUTHORITY_2026-07-12.md` remains `DISPATCH_READY` | N/A with reason: reviewer/closer owns closure conversion |
| Changed set | `## Actual Changed Set` | lists real paths as required |
| Gate evidence | `## Command Evidence` | records pass/fail for every required command |

## Dependency-Closure Matrix

| Dependency or invariant | Evidence | Disposition |
|---|---|---|
| Required Invariant 1 (no caller reference object/flags; resolver takes reference_id) | `referenceState(referenceId, nowUtcIso)` in `kernel.ts`; zero `isRevoked`/`isSuperseded` matches in `src` | PASS |
| Required Invariant 2 (revocation resolvable via receipt_id link or direct reference revocation) | `isReferenceEffectivelyRevoked` in `revocation.ts`; tests "receipt is revoked" and "reference itself is revoked" | PASS |
| Required Invariant 3 (supersession validation: distinct, same scope, strictly later, no duplicates) | `supersedeReference` in `reference-issuer.ts`; five dedicated negative tests | PASS |
| Required Invariant 4 (precedence REVOKED > SUPERSEDED > EXPIRED > ACTIVE) | `computeCurrentReferenceState` step order; "both revoked and expired" and "both superseded and expired" tests | PASS |
| Required Invariant 5 (expiry derived from valid_until_utc only) | `computeCurrentReferenceState` step 4; "EXPIRED" test | PASS |
| Required Invariant 6 (no stale ACTIVE snapshot reused as later authority) | "read once ACTIVE, then revoke, then read again -> REVOKED" test | PASS |
| Required Invariant 7 (missing reference/receipt/invalid timestamp fails closed with typed reason) | `REFERENCE_NOT_FOUND`, `BOUND_RECEIPT_NOT_FOUND`, `INVALID_READ_TIME` tests | PASS |
| Required Invariant 8 (TruthReference field set/vocabulary unchanged) | `src/types/truth-reference.ts` untouched (not in Allowed Scope, not modified) | PASS |
| Required Invariant 9 (no AI/agent/prompt/provider/network/monitor/adapter dependency) | dependency scan zero matches; `dependency-boundary.test.ts` still passes | PASS |
| No regression in already-accepted T4 behavior | full 33 pre-existing tests still pass unchanged | PASS |
| T5 and all later tranches held | no `EXTENSIONS/CVF_TRUTH_FLOW/**` path created; no session/roadmap/handoff touched | PASS |
