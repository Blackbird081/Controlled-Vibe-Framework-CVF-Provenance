# CVF GC-018 Public Projection Pre-Push T1 Profile Owner And Gate Amendment 2

Memory class: FULL_RECORD

Status: BASELINE_ACCEPTED

docType: baseline

Batch ID: PUBLIC-PROJECTION-PREPUSH-T1-AMENDMENT-2

## Purpose

Authorize a maintainability-only structural refactor of the
PUBLIC-PROJECTION-PREPUSH-T1-AMENDMENT-1 implementation to satisfy the
closure-hook governed Python automation size guard, without reopening any
functional, semantic, or evidentiary question Amendment 1 already closed
and independently proved. Amendment 1's own result is
`FUNCTIONALLY_ACCEPTED`; only its closure is `CLOSURE_REJECTED_SIZE_GUARD`.

## Scope / Target / Owner Boundary

Amendment 2 worker ownership becomes exactly seven paths:

1. `docs/reference/CVF_PUBLIC_PROJECTION_PRE_PUSH_PROFILE_STANDARD_2026-08-11.md`
2. `governance/compat/CVF_PUBLIC_PROJECTION_PRE_PUSH_POLICY.json`
3. `governance/compat/run_public_projection_pre_push_gate.py`
4. `governance/compat/public_projection_pre_push_gate_lib.py` (new;
   authorized by this baseline)
5. `governance/compat/test_run_public_projection_pre_push_gate.py`
6. `docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_WORKER_RETURN_2026-08-11.md`
7. `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json`

The existing worker return remains the only return path; no new
worker-return artifact is authorized. No other path, including any
`governance/compat/*.py` file not named above, is in scope.

## Source / Predecessor Evidence

- Amendment 1 work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_AMENDMENT_1_2026-08-12.md`
  (SHA-256 `674d3cbb28b827f463d20ee8fb7aabcb7b69cb3821774bc4a207590946e925da`).
- Amendment 1 GC-018 baseline:
  `docs/baselines/CVF_GC018_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_AMENDMENT_1_2026-08-12.md`
  (SHA-256 `df3a61f19228e0beb3a3baf6840050ba01ab25aef2910c4ed53c264967f12144`).
- Amendment 1 source verification:
  `docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_AMENDMENT_1_SOURCE_VERIFICATION_2026-08-12.md`
  (SHA-256 `1cd6bb1fb30923e83e3a065575b627d386c5255e9ef6fc35bc6b51a051cee66f`).
- Amendment 2 source verification (sibling of this baseline):
  `docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_AMENDMENT_2_SOURCE_VERIFICATION_2026-08-12.md`.
- Current worker return (unchanged, carried forward):
  `docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_WORKER_RETURN_2026-08-11.md`
  (SHA-256 `2aa8da4d4d9682a02d0e5cfdcba6ced995f7101f6e8ec6857049dbb530232499`).

## Predecessor Evidence Scope

Independent reviewer reproduction, accepted as-is and not reopened by this
amendment:

- 58/58 focused tests PASS.
- Real-candidate sandboxed run completed in 639.9 seconds, exit 0,
  `compliant: true`, `gateFailureCount: 0`.
- All seven external command categories PASS.
- Exact evidence reconciliation: Model Gateway 30 files / 231 tests;
  cvf-web 15 files / 218 tests; Next production build 121 static pages.
- Four inherited-debt rows reported correctly.
- Public clone remained clean at `021f8b852afc245a6383177dd69bf56caf488b02`.
- No sandbox/support residue.

## Preimage Authority Matrix

| Path | SHA-256 (dispatchBaseHead `225b6a01ab4400244a5cf56e47f58d16ecc0fba6`) |
| --- | --- |
| `docs/reference/CVF_PUBLIC_PROJECTION_PRE_PUSH_PROFILE_STANDARD_2026-08-11.md` | `99795c7a8a0a107582ac7a235f5e308dbae5b38b334946fa4e6df82a3cd07850` |
| `governance/compat/CVF_PUBLIC_PROJECTION_PRE_PUSH_POLICY.json` | `cbe70fbb9ff9a8a98935968d4beed12bb04e5df992ce72e58f493f50cd4b8784` |
| `governance/compat/run_public_projection_pre_push_gate.py` | `91591e24d94b32ede775b60cbc535338f4ebb20241d068edaaebc02849964e5b` |
| `governance/compat/test_run_public_projection_pre_push_gate.py` | `c85f0c41db4c83661b57083d0edb5359eb4a67857271de3cc8a4e450227e35cb` |
| `docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_WORKER_RETURN_2026-08-11.md` | `2aa8da4d4d9682a02d0e5cfdcba6ced995f7101f6e8ec6857049dbb530232499` |

`governance/compat/public_projection_pre_push_gate_lib.py` has no preimage:
it does not yet exist and is created fresh by the Amendment 2 worker.

## Worker Preflight Requirements

Before any edit, the Amendment 2 implementation worker must verify, in
full, and fail closed as `BLOCKED_PREIMAGE_MISMATCH` on any mismatch:

1. Core `HEAD` is exactly the `executionBaseHead` supplied by the
   orchestrator after the exact four-path Amendment 2 authority batch is
   committed; it must be distinct from `dispatchBaseHead`
   `225b6a01ab4400244a5cf56e47f58d16ecc0fba6`.
2. The five existing implementation paths are untracked, exactly as listed
   in the Preimage Authority Matrix, with no sixth or additional dirty
   path in Core.
3. Each of the five existing paths' SHA-256 matches the Preimage Authority
   Matrix exactly.
4. `governance/compat/public_projection_pre_push_gate_lib.py` does not yet
   exist.
5. The committed exception registry contains both freshly seeded entries
   exactly as authorized below, at caps 1380 and 1279.
6. Staged content is zero (`git diff --cached --stat` empty).
7. The public-sync clone is clean at
   `021f8b852afc245a6383177dd69bf56caf488b02` on `lpci1-ref-staging`.

## Authority Commit Choreography

`dispatchBaseHead` (`225b6a01ab4400244a5cf56e47f58d16ecc0fba6`) is the base
this baseline, its paired work order, the source verification, and the
size-exception registry repair were authored against; it does not change
as a result of authoring these four paths.

`executionBaseHead` is a distinct, later value: it will be supplied by the
orchestrator after committing the exact four-path Amendment 2 authority
batch (this baseline, the paired work
order, the source verification, and the registry) to Core.
`executionBaseHead` concerns that committed
authority delta only - it says nothing about the five inherited
Amendment-1 working paths, which are controlled separately by the
Preimage Authority Matrix and are not expected to be part of any commit
that produces `executionBaseHead`.

No claim in this baseline, the paired work order, or the source
verification asserts that Core is clean, and none may. The correct
Core-state claim is always: Core `HEAD` is the stated base value; the
exact inherited five-path Amendment-1 dirty set is present with zero
staged content; the three new Amendment 2 authority documents plus the
tracked registry repair are a separate exact four-path delta; no other
Core path is dirty.

No session-sync commit is required before worker execution unless one is
separately performed and explicitly reported by the orchestrator as part
of supplying `executionBaseHead`.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_python_automation_size.py`; `governance/compat/policy_baseline.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_packet_authority_and_encoding.py` |
| literalTokensReviewed | seeded new-exception authorization through an existing GC-018; strict `approvedMaxLines`-only downward ratchet; `DEFAULT_CLASS_THRESHOLDS` category hard/soft values; `python_cli_orchestrator`/`python_library_helper`/`python_test` classification rules in `_classify_python`; `Core Guard Self-Protection Authorization` required tokens (`Authorized guard-maintenance scope`, `Protected paths`, `Operator authorization`, `Rollback boundary`); `Large-Scope Change Authorization` 40-file default limit (not triggered) |
| gateRunPurpose | confirm the exact size targets, classification outcome for the new helper file, and self-protection token requirements before authorizing the refactor |
| claimBoundary | baseline-authoring only; no implementation, no gate execution |

## Dependency Release Evidence

Not applicable. This amendment introduces no new third-party or sibling
package dependency; it relocates existing first-party code within
`governance/compat/`.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch`

Returned defects (bounded result of 10; resolver reported `Truncated: True`):
`ADIF-0001`, `ADIF-0002`, `ADIF-0014`, `ADIF-0015`, `ADIF-0020`,
`ADIF-0021`, `ADIF-0028`, `ADIF-0029`, `ADIF-0033`, `ADIF-0044`.

Disposition: applied to this dispatch through exact manifest and source
verification, CVF-governed authority only, absorption N/A boundaries,
role-consistent dispatcher activity, checker read-ahead, literal-marker
discipline, bounded evidence claims, protected-path authorization, and a
parent execution ceiling that must exceed the longest child command plus
sandbox setup and teardown.

## Write Boundary (Two Explicit Boundaries)

- **Authority-authoring writes** (this dispatch only): exactly the three
  Amendment 2 authority artifacts plus
  `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json`.
  No implementation preimage is touched during authority authoring.
- **Implementation writes** (subsequent, separate worker dispatch only):
  exactly the seven paths named in Scope / Target / Owner Boundary above.
  The worker must not run package commands, materialize a sandbox, or
  execute the real-candidate proof envelope until after this baseline and
  its sibling work order are committed and the worker's own pre-flight
  checks pass. Package-execution writes, when the worker does reach
  verification, remain confined to a disposable sandbox outside both
  repository roots, exactly as Amendment 1 established - this baseline
  changes nothing about that boundary, only about where the orchestration
  and helper code that drives it physically live.

## Required Semantic Delta

None. This is the baseline's central constraint: Amendment 2 authorizes a
structural (file-location) delta only. Every behavioral invariant proven
under Amendment 1 must be preserved exactly:

- Exact policy pins (`pinnedBaseHead`, `authorizedCandidateHead`,
  `expectedRemoteUrl`, `expectedBranch`).
- Exact 41-path candidate manifest.
- Check-registry reconciliation (every declared policy check id actually
  executed; every executed check id declared).
- Copy-isolated dependency topology: every third-party `node_modules`
  entry copied into the disposable support store first, then linked only
  from that copy - never a live link/hard link into Core or the public-sync
  clone directly.
- The physical, junction-free, full copy of `next` directly into the
  sandbox's own `node_modules` (and its independent peer copy in the
  support store).
- Exact test/type/lint/build argv for every configured external command.
- Exact evidence counts (`expectedEvidence` values unchanged: Model Gateway
  30 files / 231 tests; cvf-web 15 files / 218 tests; Next build 121
  static pages).
- Public-root before/after invariant capture and comparison.
- Sandbox and support-directory cleanup on both success and failure.
- Deterministic JSON and human-readable output shape.
- Current CLI arguments (`--public-root`, `--base`, `--head`, `--policy`,
  `--timeout`, `--json`) and exit-code semantics (`0` only when
  `compliant: true`).

## Refactor Contract

Required size targets:

- CLI runner (`run_public_projection_pre_push_gate.py`): <= 800 physical
  lines (hard, `python_cli_orchestrator`); target <= 780.
- New library helper (`public_projection_pre_push_gate_lib.py`): <= 600
  physical lines preferred (`python_library_helper` soft threshold); must
  remain below 900 physical lines (hard threshold) in all cases.
- Focused test file (`test_run_public_projection_pre_push_gate.py`): <=
  1200 physical lines (hard, `python_test`); target <= 1150.

Move cohesive non-CLI implementation into the helper, preferably:

- Sandbox materialization and hash verification.
- Dependency physical-copy/isolation utilities.
- Invariant capture/diff.
- Output normalization and evidence extraction.
- Teardown support.

Keep in the CLI runner:

- Argument parsing.
- Policy loading/top-level validation.
- Orchestration.
- Report construction.
- Human/JSON output.
- Exit-code mapping.

## Forbidden Scope

Do not satisfy the size guard by:

- Deleting required validation.
- Weakening fail-closed behavior.
- Removing evidence reconciliation.
- Compressing code into unreadable semicolon-heavy lines.
- Hiding executable Python in JSON/Markdown.
- Raising thresholds.
- Editing the size guard
  (`governance/compat/check_python_automation_size.py`).
- Removing either newly seeded exception, or changing its `status`,
  `rationale`, `requiredFollowup`, `seedAuthorization`, `path`, or
  `fileClass`.
- Raising either exception's `approvedMaxLines`, leaving it above the
  exact final physical line count, or adding any helper exception.

The helper must not become another oversized monolith: it must remain
below its own applicable hard threshold (900 lines for
`python_library_helper`) after the extraction, not merely move the
violation from one file to another.

Also forbidden, carried forward from Amendment 1 and unaffected by this
amendment: committing; pushing; deploying; Netlify or any provider/browser/
store action; secrets access; network installs; public-clone mutation;
session-sync; any public-main or production action; running package
commands or sandbox execution during authority authoring specifically (the
implementation worker may run them only during its own later verification
phase, inside the disposable sandbox, exactly as Amendment 1 authorized).

## Pinned Command Manifest

Unchanged from Amendment 1. Not reproduced verbatim here (not a paraphrase
substitute; the authoritative pin remains the current
`governance/compat/CVF_PUBLIC_PROJECTION_PRE_PUSH_POLICY.json`
`externalCommands.commands` array, which this amendment does not
authorize modifying in argv, working directory, timeout, or
`expectedEvidence` content). The implementation worker's Required
Verification After Authority Commit step 5 (real-candidate sandbox run)
must reproduce the exact same seven-command PASS set with the exact same
evidence counts as the predecessor's proof.

## Verification Contract

The implementation worker must run, after authority commit and before
returning:

1. Python syntax/import checks for the CLI runner and the new helper.
2. 58+ focused tests (the existing 58 plus any new tests the refactor
   itself requires, for example a no-circular-import test).
3. An explicit test proving the CLI runner imports the helper without a
   circular dependency.
4. The governed Python automation size gate
   (`governance/compat/check_python_automation_size.py`) against both the
   CLI runner and the new helper, confirming both are below their
   applicable hard thresholds.
5. A real-candidate sandbox run reproducing all current exact evidence
   (58/58 tests unaffected by the refactor is necessary but not
   sufficient; the real external-command proof envelope must also be
   reproduced).
6. The worker-return fast gate.
7. The reviewer-fast governance gate.
8. `git diff --check`.
9. Exact-seven manifest confirmation, including verification that only
   each seeded entry's `approvedMaxLines` changed and was ratcheted down
   to the exact final physical line count; staged-content-zero confirmation.
10. Confirmation the runner is <= 800 (target <= 780), test is <= 1200
    (target <= 1150), helper is <= 900 (target <= 600), and the helper has
    no exception.
11. Confirmation the public clone remains unchanged at
    `021f8b852afc245a6383177dd69bf56caf488b02`.

## Acceptance Criteria

- Both `run_public_projection_pre_push_gate.py` and
  `public_projection_pre_push_gate_lib.py` are below their applicable hard
  thresholds (800 and 900 lines respectively); `test_run_public_projection_pre_push_gate.py`
  remains below 1200 lines.
- Both freshly seeded exceptions admitted only the already-proven
  untracked preimages into the governed commit flow, authorized no growth
  or semantic weakening, and have only `approvedMaxLines` ratcheted down
  to the exact final physical line counts. The helper has no exception.
- All ten Verification Contract items pass.
- No behavioral invariant in Required Semantic Delta regresses.
- No Forbidden Scope item is exercised.
- The worker return remains the single, same artifact
  (`docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_WORKER_RETURN_2026-08-11.md`),
  amended in place to record the Amendment 2 continuation, not replaced or
  duplicated.

## Decision / Baseline / Proposed Tranche

BASELINE_ACCEPTED. This document, together with its sibling source
verification and work order, authorizes a subsequent, separate
implementation-worker dispatch to perform the seven-path refactor described
above across the exact seven-path worker manifest. No implementation
occurs under this baseline itself.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: extend the same isolated
public-projection implementation surface under `governance/compat/` that
T1 and Amendment 1 already authorized, by relocating cohesive non-CLI
logic out of the existing runner into exactly one new, equally isolated
library helper file, while using the GC-018-seeded registry mechanism only
to admit the already-proven runner and test preimages into governed commit
flow; no growth or semantic weakening is authorized.

Protected paths:

- `governance/compat/run_public_projection_pre_push_gate.py`
- `governance/compat/public_projection_pre_push_gate_lib.py`
- `governance/compat/test_run_public_projection_pre_push_gate.py`
- `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json`

Operator authorization: this dispatch's `ROLE: dispatcher / Amendment 2
authority author` instruction, carried forward from the committed
Amendment 2 authority-repair instruction at Core base
`225b6a01ab4400244a5cf56e47f58d16ecc0fba6`.

Rollback boundary: revert exactly the seven Amendment 2 worker paths to
their pre-Amendment-2 state (the five-path Amendment 1 state, the new
helper removed, and the two freshly seeded registry entries removed as
one authorized rollback) if rejected; do not revert candidate commits
`492e11eab`, `021f8b852`, or any session-sync or prior Amendment authority
commit.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this baseline and its sibling authority artifacts are private
provenance governance-control-plane work. No public artifact is created.

## Claim Boundary

This baseline authorizes a maintainability-only structural refactor
(file-location relocation of already-proven logic into a new library
helper) to satisfy a source-verified closure-hook size-guard failure. It
authorizes no semantic, functional, or evidentiary reopening of Amendment
1's independently proven result; no commit; no package command execution
or sandbox materialization during authority authoring; no push, deploy,
provider/store, secret, network install, or public-clone mutation. The
subsequent implementation worker's own verification, not this baseline,
is what will actually prove the refactored code preserves every
behavioral invariant listed above.
