# CVF Agent Work Order - SOT3-T4R1 Kernel Current-Reference Authority Repair

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-07-12

Work Order ID: SOT3-T4R1

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `a99a4a035`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `REVIEWER_MUST_CAPTURE_AT_CLOSURE`

## Dispatch Prompt Envelope

Role: no-commit deterministic TypeScript Kernel repair worker.

Canonical packet: this work order and paired T4R1 GC-018.

Commit mode: WORKER_MUST_NOT_COMMIT

Base: capture HEAD and full status before edits.

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

Current-time notes: T0-T4 are accepted; T5 is HOLD_UNTIL_T4_CURRENT_REFERENCE_AUTHORITY
per Codex pre-dispatch review; only this T4R1 repair is released.

Do-not-misread notes: this is a repair of the already-accepted T4 package, not
a new tranche or a reopening of any other T4 finding (R1-R12 remain accepted
as closed). The only in-scope defect is the caller-supplied
`isRevoked`/`isSuperseded` parameters on `computeReferenceState`/
`TruthKernel.referenceState()`. Do not touch admission, evaluation, receipt
hashing, or eligibility-resolution logic already accepted at commit
`6bf81979b`.

Required first actions: startup reads, paired baseline, T4 completion review,
T2 contracts/negative cases (section 6, Invariant 6, NC-09, NC-10), and the
exact current source of `kernel.ts`, `reference-issuer.ts`, `revocation.ts`,
`kernel-stores.ts`, `immutable-store.ts`, `truth-reference.ts`, and
`reference-integrity.test.ts`.

Return contract: repair implementation and `COMPLETE_PENDING_REVIEW`, no commit.

## Purpose

Close the source-verified gap blocking SOT3-T5: make `TruthReference`
effective-state derivation (`REVOKED`/`SUPERSEDED`/`EXPIRED`/`ACTIVE`)
exclusively Kernel-store-derived at read time, removing the caller-supplied
`isRevoked`/`isSuperseded` boolean parameters.

## Target / Source

Target root is `EXTENSIONS/CVF_TRUTH_KERNEL/`; source precedence is the
paired baseline Source Verification Block.

## Scope / Methodology

Add direct-reference revocation and supersession stores to `KernelStores`.
Replace the caller-object/flag resolver with a store-only
`computeCurrentReferenceState(referenceId, stores, nowUtcIso)` that resolves
the immutable stored reference first. Update
`TruthKernel.referenceState(referenceId, nowUtcIso)`, add
`TruthKernel.revokeReference(referenceId)`, and add validated
`TruthKernel.supersede(oldReferenceId, newReferenceId)`. Keep the internal
store-dependent resolver out of the package root exports.

## Authority Chain

Operator continuation -> Codex pre-dispatch review of SOT3-T5 (blocking
finding) -> T2 contracts (section 6, Invariant 6, NC-09, NC-10) -> accepted
T4 material commit `6bf81979b` -> paired GC-018 -> this work order.

## Agent Roles

Dispatcher owns source fidelity; worker implements without commit;
reviewer/closer audits all contract dependencies in one first-pass matrix,
then decides whether SOT3-T5 may be refreshed and redispatched.

## Worker Autonomy / No-Question Rule

Repair in-scope package/test defects. Stop for a T2 contradiction, a change
that would alter any other already-accepted T4 behavior (admission,
evaluation, receipt hashing, eligibility resolution), external dependency,
forbidden path, or scope expansion.

## Required First Reads

Startup front doors; guard orientation; literal gotchas; paired baseline; T4
completion review; T2 contracts/negative cases (section 6, Invariant 6,
NC-09, NC-10); current `EXTENSIONS/CVF_TRUTH_KERNEL/src/kernel.ts`,
`src/engine/reference-issuer.ts`, `src/engine/revocation.ts`,
`src/stores/kernel-stores.ts`, `src/stores/immutable-store.ts`,
`src/types/truth-reference.ts`, `src/index.ts`,
`tests/reference-integrity.test.ts`.

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short --untracked-files=all
python governance/compat/generate_active_session_state.py --check
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | accepted T4 Kernel package under repair; no new external corpus |
| Scope classification | ACCEPTED_PACKAGE_BOUNDED_REPAIR |
| Intake role | no-commit package repair worker |
| Risk sensitivity | HIGH: reference authority is the exact gate T5 distribution depends on |
| Provider surface | local deterministic tools only |
| Reviewer role | contract, store-derivation, precedence, and regression audit |
| Routing decision | WORKER_MUST_NOT_COMMIT |
| Escalation condition | T2 contradiction, regression in already-accepted T4 behavior, new dependency, or forbidden path |
| Public route | DEFERRED_PRIVATE_ONLY |
| canonical route mode | MULTI_AGENT_MULTI_ROLE |
| selected role route | dispatcher -> package repair worker -> reviewer/closer |

## Allowed Scope

Only `EXTENSIONS/CVF_TRUTH_KERNEL/src/stores/kernel-stores.ts`,
`EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/revocation.ts`,
`EXTENSIONS/CVF_TRUTH_KERNEL/src/engine/reference-issuer.ts`,
`EXTENSIONS/CVF_TRUTH_KERNEL/src/kernel.ts`,
`EXTENSIONS/CVF_TRUTH_KERNEL/src/index.ts`,
`EXTENSIONS/CVF_TRUTH_KERNEL/tests/**` (additions only), and
`docs/reviews/CVF_SOT3_T4R1_WORKER_RETURN_2026-07-12.md`.

## Forbidden Scope

`EXTENSIONS/CVF_TRUTH_FLOW/**` (does not exist; must not be created),
`EXTENSIONS/CVF_REFINERY/**`, any `EXTENSIONS/CVF_TRUTH_KERNEL/src/types/**`
or `schemas/**` field change, admission/evaluation/receipt-hashing logic in
`src/engine/admission.ts`/`src/engine/evaluator.ts`/`src/engine/receipt-issuer.ts`,
other extensions, governance checkers/hooks, session files, Web/UI,
provider/live, public-sync, package activation, database/SOT-index service,
monitors, adapters.

## Source Verification Block

Use and reopen every row in the paired baseline. T2 is canonical; the
already-accepted T4 package is the sole runtime authority for what changed
versus what remains fixed.

## Negative Search And Collision Discipline

| Search | Command | Result | Dispatch consequence |
|---|---|---|---|
| direct-reference revocation or supersession-link store | `rg -n "referenceRevocation\|supersession\|supersede" EXTENSIONS/CVF_TRUTH_KERNEL/src` | zero matches in `EXTENSIONS/CVF_TRUTH_KERNEL/src`; no current store, field, or function name resolves these concepts | worker adds both stores inside the existing `KernelStores` owner, not a new package |
| standalone `computeReferenceState` export outside `reference-issuer.ts` | `rg -n "computeReferenceState" EXTENSIONS/CVF_TRUTH_KERNEL/src` | found only in `src/engine/reference-issuer.ts` (definition) and `src/kernel.ts` (import/call site); no other collision | confirms the single function to replace with `computeCurrentReferenceState`; no rename collision elsewhere |
| caller-supplied `isRevoked`/`isSuperseded` parameters elsewhere in the package | `rg -n "isRevoked\|isSuperseded" EXTENSIONS/CVF_TRUTH_KERNEL/src` | found only in `src/engine/reference-issuer.ts:172-176` and `src/kernel.ts:145-148` | both call sites are in Allowed Scope; no forbidden-path collision |

## Implementation Contract

- `KernelStores` gains `referenceRevocations`, keyed by `reference_id`, and a
  `supersessions` store: `ImmutableStore<{
  superseded_reference_id: string; superseding_reference_id: string }>`,
  keyed by `superseded_reference_id`.
- `revocation.ts` gains direct-reference revocation plus a resolver that
  treats either a direct reference revocation or a revoked bound receipt as
  authoritative `REVOKED` evidence.
- `reference-issuer.ts`'s `computeReferenceState` is replaced by
  `computeCurrentReferenceState(referenceId: string, stores: KernelStores,
  nowUtcIso: string): ReferenceStateResolutionResult` that:
  1. resolves the immutable reference from `stores.references` and its bound
     receipt; missing records or invalid timestamps return typed rejection;
  2. returns `REVOKED` if the reference or its receipt is revoked;
  3. else returns `SUPERSEDED` if `stores.supersessions.has(reference.reference_id)`;
  4. else returns `EXPIRED` if `Date.parse(nowUtcIso) >=
     Date.parse(reference.valid_until_utc)`;
  5. else returns `ACTIVE`.
- `TruthKernel.referenceState(referenceId, nowUtcIso)` calls the new resolver
  with exactly these two arguments; the `isRevoked`/`isSuperseded`
  parameters and caller-supplied reference object are removed entirely.
- `TruthKernel.revokeReference(referenceId)` records a direct reference
  revocation and fails typed when the reference is absent or already revoked.
- `TruthKernel.supersede(oldReferenceId: string, newReferenceId: string)` is
  added only for distinct existing references with identical `scope` and a
  strictly later `newReference.valid_from_utc`; missing, self, cross-scope,
  older/equal, invalid-time, or duplicate links fail typed without insertion.
- A read on a `reference_id` absent from `stores.references` fails closed
  with a typed rejection, not a default `ACTIVE`.
- `src/index.ts` exports public result/rejection types as needed, but does not
  export the store-dependent `computeCurrentReferenceState` implementation;
  there was no prior root `computeReferenceState` export to replace.
- No global clock/random source is read; `nowUtcIso` remains an injected
  read-time argument, unchanged from the existing pattern.

## New Doc-Only Fields

| Proposed item | Intended implementation owner | Source-status boundary |
|---|---|---|
| `ReferenceStateResolutionResult`; `ReferenceStateResolutionReason` | `reference-issuer.ts` plus public type export | new in T4R1; not an existing source fact |
| `ReferenceRevocationRecord`; `ReferenceSupersessionRecord` | `KernelStores` | new in T4R1; not an existing source fact |
| typed reference revocation/supersession rejection tokens | revocation/reference engines plus public type export | new in T4R1; not an existing source fact |

## Negative Test Matrix

| Case | Required result |
|---|---|
| reference's receipt is revoked, then state is read | `REVOKED`, no caller flag involved |
| reference itself is revoked, while receipt remains issued | `REVOKED`, no caller flag involved |
| reference is superseded via `supersede()`, then state is read | `SUPERSEDED`, no caller flag involved |
| reference's `valid_until_utc` has passed, no revocation or supersession recorded | `EXPIRED` |
| reference is both revoked and expired | `REVOKED` (precedence: `REVOKED > SUPERSEDED > EXPIRED > ACTIVE`) |
| reference is both superseded and expired, not revoked | `SUPERSEDED` (precedence) |
| reference is none of revoked/superseded/expired | `ACTIVE` |
| a reference is read once (`ACTIVE`), then its receipt is revoked, then read again | second read reports `REVOKED`; the first `ACTIVE` snapshot is never reused as later authority |
| `referenceState()`/`computeCurrentReferenceState` is called with an unresolvable `reference_id` or a reference whose receipt cannot be resolved | typed rejection, never a default `ACTIVE` |
| `supersede()` called with a nonexistent old or new reference id | typed rejection; no supersession recorded |
| `supersede()` called with self-link, cross-scope pair, older/equal `valid_from_utc`, invalid timestamp, or duplicate old-reference link | typed rejection; no supersession recorded |
| caller supplies a forged `TruthReference` object with a real receipt id | impossible at the public state-read boundary; API accepts stored `reference_id` only |
| full existing T4 suite (positive path, negative matrix, receipt-hash vector, schema surfaces, dependency boundary, reference integrity) | still 100% passing, confirming no regression in already-accepted behavior |

## Dual Agent Surface Matrix

| Surface | Role | Interface | Authority/risk boundary | Evidence | Adapter boundary |
|---|---|---|---|---|---|
| INTERNAL_AGENT | worker/reviewer | local files and commands | worker cannot commit; Kernel package repair only | tests and return | local process |
| EXTERNAL_AGENT_CLI_MCP | future worker | same packet | no provider authority or MCP support | locally revalidated return | NOT_IMPLEMENTED_WITH_REASON: separate adapter authorization required |

## ADIF Defect Registry Disclosure

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 20 --json`

Returned defectIds: ADIF-0001, ADIF-0002, ADIF-0006, ADIF-0007,
ADIF-0014, ADIF-0015, ADIF-0016, ADIF-0017, ADIF-0020, ADIF-0021, ADIF-0024.

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

## Agent Handoff Contract Control Block

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher -> no-commit package repair worker -> reviewer/closer |
| phase | SOT3-T4R1 Kernel current-reference authority repair |
| contractSource | canonical contract citation immediately above |
| baseHeadFor(phase) | dispatch=`a99a4a035`; execution=worker-captured HEAD; closure=reviewer-captured base |
| changedSetScope(phase) | five named Kernel files, test additions, one worker return |
| traceScope(phase, actor) | reads, manifest, code, tests, scans, gates, no-commit evidence |
| commitOwner(phase) | worker=WORKER_MUST_NOT_COMMIT; reviewer owns accepted commit |
| crossBatchIsolation | T5 (held), T6-T7, other extensions, session, provider, public paths excluded |
| nextMoveSurfaces | reviewer/session-sync steward only after acceptance; T5 packet refresh is a separate later action |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_SOT3_T4R1_COMPLETION_REVIEW_2026-07-12.md`

reviewerOwnedClosurePaths: completion review and accepted repair material;
session continuity in a separate commit. After acceptance, the reviewer
separately decides whether to refresh the held SOT3-T5 packet against the
new material commit; that refresh and any redispatch is not authorized by
this work order.

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| TruthReference precedence and state model must be Kernel-derived | Implementation Contract | `computeCurrentReferenceState` | negative test matrix (precedence rows) | PASS |
| distribution requires a valid, non-expired, non-revoked reference (Invariant 8 dependency) | Implementation Contract | store-derived `REVOKED`/`SUPERSEDED`/`EXPIRED` | negative tests | PASS |
| no caller-supplied approval/authority flag may substitute for Kernel evaluation (Invariant 7/10 dependency for future Flow work) | Implementation Contract | removal of `isRevoked`/`isSuperseded` parameters | source diff; negative tests | PASS |
| no regression in already-accepted T4 behavior | Negative Test Matrix, final row | full existing suite re-run | `npm test` | PASS |
| T5 and all later tranches held | Forbidden Scope | no Flow paths created | exact status/diff | PASS |

## Execution Plan

1. Capture `executionBaseHead` and `git status --short --untracked-files=all`.
   Input: clean worktree. Output: recorded base. Validation: command output.
   Stop condition: worktree not clean at start.
2. Reopen T2 contract chain section 6, Invariant 6, NC-09, NC-10, and the
   five cited current Kernel source files plus the existing reference-
   integrity test. Input: cited sources. Output: confirmed gap and unchanged
   surrounding contract. Validation: source re-read. Stop condition: contract
   mismatch found, or gap does not match the baseline's claim.
3. Add `referenceRevocations` and `supersessions` stores to `KernelStores`. Input: `ImmutableStore`
   pattern. Output: updated `src/stores/kernel-stores.ts`. Validation:
   `tsc --noEmit`. Stop condition: store shape diverges from
   `ImmutableStore<T>`'s existing insert/get/has contract.
4. Add direct-reference revocation and receipt-resolution-by-reference helpers
   to `revocation.ts`. Input: existing receipt revocation plus new
   `referenceRevocations` store. Output: updated `src/engine/revocation.ts`.
   Validation: both revocation paths independently tested. Stop condition:
   existing receipt revocation is re-keyed or weakened.
5. Replace `computeReferenceState` with `computeCurrentReferenceState` in
   `reference-issuer.ts`, implementing the four-step precedence resolution
   exactly as specified in Implementation Contract. Input: steps 3-4 output.
   Output: updated `src/engine/reference-issuer.ts`. Validation: precedence
   negative tests. Stop condition: any caller-supplied boolean remains in the
   function signature.
6. Update `TruthKernel.referenceState()` to the reference-ID two-argument form
   and add `TruthKernel.revokeReference()` plus validated
   `TruthKernel.supersede()`. Input: step 5 output. Output: updated
   `src/kernel.ts`. Validation: `tsc --noEmit`; unit test. Stop condition:
   any forwarded caller flag remains.
7. Update `src/index.ts` public type exports without exposing the internal
   store-dependent resolver. Validation: `tsc --noEmit`, `npm run build`.
8. Author the full negative test matrix plus re-run the entire existing T4
   suite. Validation: `npm test`. Stop condition: any negative case fails to
   fail closed, or any previously-passing test now fails (regression).
9. Run forbidden-dependency scan, worker-return fast gate, file-size guard,
   and record exact manifest/status/diff. Return `COMPLETE_PENDING_REVIEW`
   without commit. Stop condition: any command fails without an in-scope
   repair.

## Write Ownership

Worker owns the five named Kernel files, test additions, and worker return
only. Reviewer owns closure/commit and any later T5 packet refresh decision.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Verification Commands

```powershell
npm --prefix EXTENSIONS/CVF_TRUTH_KERNEL run typecheck
npm --prefix EXTENSIONS/CVF_TRUTH_KERNEL run build
npm --prefix EXTENSIONS/CVF_TRUTH_KERNEL test
rg -n -i "openai|anthropic|provider|prompt|agent|fetch\(|axios|randomUUID|Date\.now|new Date\(\)" EXTENSIONS/CVF_TRUTH_KERNEL/src
rg -n "isRevoked =|isSuperseded =|isRevoked: boolean|isSuperseded: boolean" EXTENSIONS/CVF_TRUTH_KERNEL/src
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_governed_file_size.py --enforce
git diff --check
git status --short --untracked-files=all
git rev-parse --short HEAD
```

The second `rg` command must return zero matches; any match indicates a
caller-supplied revocation/supersession flag remains in the public API and
blocks closure.

## Review Gate

Reviewer builds one dependency-closure matrix before repair and recomputes
all negative cases, precedence ordering, regression status of the full
existing suite, dependency scan, exact exports, status/diff, and committed
pre-closure range. Reviewer separately determines whether this closes the
condition needed to refresh and redispatch SOT3-T5.

## Evidence Requirements

Exact manifest, test counts (new plus existing, with explicit before/after
comparison proving no regression), typecheck/build output, precedence-table
proof, dependency scan, no-copy disposition, status/diff and unchanged HEAD.

## Acceptance Criteria

All baseline invariants and negative cases pass; the full pre-existing T4
suite still passes unchanged; no caller-supplied revocation/supersession
flag remains in any public method signature; no forbidden dependency or
out-of-scope path exists; worker did not commit.

## Operator Checkpoint

No checkpoint for in-scope repair. Stop for any change to already-accepted
T4 behavior outside the named gap, a T2 contradiction, dependency,
adapter/database/monitor/Flow integration, activation, or provider/live
proof.

## Closure Checklist

- [ ] `supersessions` store added; revocation resolvable via `receipt_id` link;
- [ ] `computeCurrentReferenceState` derives all three dynamic states from
  stores only, with no caller-supplied boolean parameter;
- [ ] precedence `REVOKED > SUPERSEDED > EXPIRED > ACTIVE` proven by test;
- [ ] a state re-read after revocation/supersession reflects the update, not
  a stale issuance-time snapshot;
- [ ] missing-reference and missing-receipt-link reads fail closed;
- [ ] full pre-existing T4 suite still passes (no regression);
- [ ] determinism and no-AI/no-provider proof pass;
- [ ] exact manifest and no-commit evidence returned.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW`, `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`,
or `BLOCKED_WITH_REASON`; never a closed-equivalent worker status.

## Worker Return Conditions

Return after all commands pass or one source-backed blocker. Do not commit.

## Return / Escalation Conditions

Escalate only contract contradiction, regression risk to already-accepted
behavior, dependency, forbidden path, or expansion.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| durable family | `EXTENSIONS/CVF_TRUTH_KERNEL/` (existing owner; repair only) |
| stable front door | package README (update if the public `referenceState()` signature changes require a doc note) |
| canonical owner | existing T4 runtime owner; truth-foundation remains doctrine owner |
| generated aggregate | NOT_APPLICABLE_WITH_REASON: direct package source authority |
| index/update route | package exports and later accepted Catalog projection |
| claim boundary | repair of a private package candidate until reviewer acceptance |

## Repair Scope Control Block

This work order repairs an already-accepted CVF-native package in place. It
is not a retained-corpus enumeration, external-repository intake, or
knowledge absorption action, so the coverage-index and external-intake
routing control families do not apply to this artifact class. The
triggering evidence is a same-session Codex pre-dispatch finding against
already-accepted CVF source, not an external or retained corpus.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id SOT3-T4R1 --title "Kernel Current-Reference Authority Repair" --date 2026-07-12 --base 1bf21dcee --commit-mode WORKER_MUST_NOT_COMMIT --stdout --include-worker-return-skeleton` |
| generatedProfile | no-commit TypeScript package repair worker |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Hand-authored from the work-order template directly, following the T4/T5 work orders' proven section shape. Added the caller-flag repair scope, store-derivation implementation contract, and regression-focused negative test matrix. |
| checkerReadAheadConfirmation | dispatch, structural, handoff, worker-return, file-size checkers |
| docOnlyNewFields | proposed `ReferenceStateResolutionResult`, `ReferenceStateResolutionReason`, `ReferenceRevocationRecord`, `ReferenceSupersessionRecord`, and typed revocation/supersession rejection tokens; worker must use these as new T4R1 surfaces, not claim they pre-exist |
| claimBoundary | dispatch only; no implementation proof |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Reviewer Closure Conversion; Roadmap-to-Work-Order Trace Matrix; Public Export Disposition |
| gateRunPurpose | confirm source-derived dispatch before implementation |
| claimBoundary | gates do not prove repair semantics |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local private provenance workspace |
| Session or invocation | SOT3-T4R1 repair packet authoring, 2026-07-12 |
| Working directory | repository root |
| Command or tool surface | governed reads, rg, source verification, file writes, dispatch gates |
| Target paths | paired T4R1 baseline and this work order |
| Allowed scope source | Codex pre-dispatch review blocking SOT3-T5 and directing a fresh bounded T4 repair packet |
| Before status evidence | clean worktree after held SOT3-T5 packet and handoff anchor at HEAD `a99a4a035`; caller-object/flag gap confirmed present at `kernel.ts:142-149` and `reference-issuer.ts:168-179` |
| After status evidence | T4R1 packet authored; implementation awaits pre-dispatch |
| Diff evidence | exact two-path packet diff before commit |
| Approval boundary | T4R1 packet authoring and bounded no-commit dispatch |
| Claim boundary | no repair behavior proof, T5 refresh, T6-T7, provider/live or public claim |
| Agent type | dispatcher |
| Invocation ID | `sot3-t4r1-dispatch-authoring-2026-07-12` |
| Expected manifest | paired baseline and work order |
| Actual changed set | paired baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance repair packet; no public-sync authorization.

## Claim Boundary

This work order authorizes one bounded no-commit T4R1 repair worker after
pre-dispatch. It does not authorize T5 implementation or redispatch, T6-T7,
provider/live, public, activation, or any change to already-accepted T4
behavior outside the named caller-flag gap.
