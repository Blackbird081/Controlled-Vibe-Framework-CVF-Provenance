# CVF GC-018 Baseline - Public Projection Pre-Push T1 Profile Owner And Gate Amendment 1

Memory class: FULL_RECORD

Status: READY_FOR_DISPATCH

docType: baseline

Date: 2026-08-12

Batch ID: PUBLIC-PROJECTION-PREPUSH-T1-AMENDMENT-1

dispatchBaseHead: `bbcb21acd753ec5c4f5a5c234da585e09febc562`

Commit mode: WORKER_MUST_NOT_COMMIT

## Purpose

Amend the `REVIEWER_CONFIRMED_BLOCKED_UNDER_CURRENT_CONTRACT` disposition of
PUBLIC-PROJECTION-PREPUSH-T1 by authorizing a disposable, hash-verified
candidate sandbox in which mutating package commands (test/type/lint/build)
may run, while the real public-sync clone remains strictly read-only
evidence for every Git-level validation (remote, branch, clean state, HEAD,
pinned range, exact 41-path manifest). No requirement is waived: the full
previously accepted candidate proof envelope must still execute, and no
command may mutate the real public clone.

## Scope / Target / Owner Boundary

Stable owner role: Public Projection Release Steward (unchanged from T1),
fulfilled by the reviewer/closer lane.

Amendment worker owns exactly the same five paths T1 already owns; no new
owner path is introduced:

- `docs/reference/CVF_PUBLIC_PROJECTION_PRE_PUSH_PROFILE_STANDARD_2026-08-11.md`
- `governance/compat/CVF_PUBLIC_PROJECTION_PRE_PUSH_POLICY.json`
- `governance/compat/run_public_projection_pre_push_gate.py`
- `governance/compat/test_run_public_projection_pre_push_gate.py`
- `docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_WORKER_RETURN_2026-08-11.md`

If, and only if, a named checker requires a separate amendment-return
artifact instead of updating the existing worker return in place, the
paired work order's Reviewer Closure Conversion records that narrow
exception; it does not create a general license to add paths.

## Source / Predecessor Evidence

- `docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_AMENDMENT_1_SOURCE_VERIFICATION_2026-08-12.md` records the accepted amendment decision and its full source basis.
- `docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_WORKER_RETURN_2026-08-11.md` records the current `BLOCKED_WITH_REASON` / `BLOCKED_CONTRACT_CONTRADICTION` disposition and its exact command/package evidence for why `cvf-web` `build` cannot run against the real public clone.
- `docs/reviews/CVF_LPCI1_REF_T1A_PUBLIC_SAFE_BRANCH_DEPLOY_BINDING_AMENDMENT_2_COMPLETION_2026-08-11.md` and its paired worker return record that the identical public candidate package graph was already proven buildable (121 static pages) by temporarily materializing all eight sibling `file:` dependencies as offline junctions **inside the real public clone's own worktree**, with no tracked-source delta and no network access. This is dependency-topology and expected-outcome evidence only; see Predecessor Evidence Scope below for what it does not prove.
- `docs/baselines/CVF_GC018_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_2026-08-11.md` and `docs/work_orders/CVF_AGENT_WORK_ORDER_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_2026-08-11.md` remain the governing T1 authority for everything this amendment does not change.
- Public clone remote is `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`; clean branch `lpci1-ref-staging` is at candidate `021f8b852` as of dispatch evidence.

## Predecessor Evidence Scope

The LPCI1-REF-T1A Amendment 2 completion and worker return prove three
things and no more: (1) the eight-package `file:` dependency topology for
this exact `cvf-web`/`CVF_MODEL_GATEWAY` package graph is viable when fully
materialized; (2) TypeScript and the focused test suites pass under that
topology; (3) `next build --webpack` compiles successfully and emits 121
static pages under that topology. That review materialized its eight
temporary junctions **directly inside the real public-sync clone's
worktree** and restored the original state afterward; it did not create,
verify, or tear down a disposable sandbox located outside the public clone,
and it recorded no before/after invariant capture of the kind this
amendment requires. It is not evidence that disposable-sandbox isolation
outside the public clone works, nor that zero transient public-clone
mutation is achievable - Amendment 2's own methodology was a temporary
in-place mutation with restoration, which is precisely the pattern this
amendment must avoid. Only the dependency-topology composition and the
expected test/build outcomes (file counts, test counts, static-page count)
are reusable predecessor evidence; sandbox isolation itself must be freshly
proven by the amendment worker against a real, disposable, out-of-repository
sandbox.

## Preimage Authority Matrix

The five paths below are the exact T1 worker-owned artifacts this amendment
worker inherits, unmodified, at dispatch. Each row pins the exact SHA-256 of
that path's current bytes at `dispatchBaseHead`. This matrix is the sole
authority for "unchanged since T1" claims; no worker-return prose statement
substitutes for a preimage hash match.

| Path | Pinned SHA-256 |
| --- | --- |
| `docs/reference/CVF_PUBLIC_PROJECTION_PRE_PUSH_PROFILE_STANDARD_2026-08-11.md` | `f2ea0f2c4247aa7f4eff59a32c0c0b0a0a62c2f7e68bb39dca4dde964eaad2b8` |
| `governance/compat/CVF_PUBLIC_PROJECTION_PRE_PUSH_POLICY.json` | `dcf1d0473792bf6931184a7e23f0c8fcd56b8f8cec1415442fe803af8062a086` |
| `governance/compat/run_public_projection_pre_push_gate.py` | `8283d58e542ef22d4c4154c1d0b22541109fd670b4e0ae1fa1d37fdea9772eb1` |
| `governance/compat/test_run_public_projection_pre_push_gate.py` | `1b07917cbb1fab65d9ebbf60b357345974780207a840b55bb1133a8d024ae139` |
| `docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_WORKER_RETURN_2026-08-11.md` | `e457e0776844c1a6ba72b3ef75aed134962c4ac279c256681b7c5c5552c0e3c4` |

These five paths are currently working-tree dirty in Core relative to
`dispatchBaseHead` (four intent-to-added with zero staged content, one
untracked) - that is expected, inherited, authorized T1 state, not an
anomaly. Core's tracked `HEAD` remains `dispatchBaseHead` throughout
dispatch-authoring; only the five preimage paths above and, once committed,
the three new Amendment 1 authority paths differ from a clean checkout of
that `HEAD`.

## Worker Preflight Requirements

Before any implementation-authoring edit, the amendment worker must verify,
and fail closed as `BLOCKED_PREIMAGE_MISMATCH` on any failure:

1. Core `HEAD` equals the later `executionBaseHead` the orchestrator
   supplies at worker dispatch (captured after the three Amendment 1
   authority files are committed) - not `dispatchBaseHead`, which only
   governs this baseline's own authoring.
2. The Core working-tree dirty set is exactly the five paths in the
   Preimage Authority Matrix; no additional dirty path exists.
3. Each of the five paths' current bytes hash to exactly its pinned
   SHA-256 in the Preimage Authority Matrix.
4. Staged content is zero (`git diff --cached --name-only` empty).

The worker must not choose between competing byte versions of a preimage
path and must not regenerate or re-derive a preimage from any other source
if a hash mismatch is found; a mismatch is a hard stop requiring an
orchestrator decision, not a worker judgment call.

## Authority Commit Choreography

`dispatchBaseHead` (`bbcb21acd753ec5c4f5a5c234da585e09febc562`) is the base
this baseline, its paired work order, and the source verification were
authored against; it does not change as a result of authoring these three
files.

`executionBaseHead` is a distinct, later value: it will be supplied by the
orchestrator after committing exactly the three Amendment 1 authority
artifacts (this baseline, the paired work order, and the source
verification) to Core. `executionBaseHead` concerns that committed
authority delta only - it says nothing about the five inherited T1 working
paths, which are controlled separately by the Preimage Authority Matrix and
are not expected to be part of any commit that produces
`executionBaseHead`.

No claim in this baseline, the paired work order, or the source
verification asserts that Core is clean, and none may. The correct
Core-state claim is always: Core `HEAD` is the stated base value; the exact
inherited five-path T1 dirty set is present with zero staged content; the
three new Amendment 1 authority paths are a separate delta; no other Core
path is dirty.

No session-sync commit is required before worker execution unless one is
separately performed and explicitly reported by the orchestrator as part of
supplying `executionBaseHead`.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | source verification columns, protected-path authorization, operation trace fields, bounded claim vocabulary, public disposition enum |
| gateRunPurpose | confirm source-backed amendment dispatch shape after the sandbox decision was selected; not first discovery |
| claimBoundary | dispatch authority only; no sandbox execution or push/deploy claim |

## Dependency Release Evidence

The dispatcher/amendment-author role instruction supplies the disposition
source (`REVIEWER_CONFIRMED_BLOCKED_UNDER_CURRENT_CONTRACT`) and the exact
amendment decision (disposable candidate-sandbox execution; no waived
test/type/lint/build; no mutation of the real public clone). That
instruction is this amendment's dependency release.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`PUBLIC-PROJECTION-PREPUSH-T1 Amendment 1 sandbox verification dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Dispatch impact: source-backed sandbox design, exact fail-closed conditions,
no command weakening, no real-clone mutation path.

## Large-Scope Change Authorization

AUTHORIZED_EXACT_INHERITED_PUBLIC_RANGE: the amended profile may evaluate
the already-committed exact 41-path public range
`2103a38fda01ee827e9fc6c3be38a824fa5d54ad..021f8b852afc245a6383177dd69bf56caf488b02`,
identically to T1. This authorization does not permit the amendment worker
to edit the public clone and does not waive manifest, leakage, build, or
regression checks. It additionally authorizes materializing a disposable,
read-only-extracted copy of that exact candidate commit outside both
repository roots, strictly for running mutating package commands; that
sandbox copy is never itself an authority surface and carries no governed
path ownership.

## Write Boundary (Two Explicit Boundaries)

This amendment has exactly two distinct write boundaries; they must never be
conflated:

**Implementation-authoring writes** (the worker editing the standard,
policy, runner, tests, and worker return): allowed only on the exact five
Core owner paths named in Scope / Target / Owner Boundary, using
apply_patch or an equivalent local editor only. No other Core path may be
written. This is ordinary Core file editing, not sandbox activity, and it
happens before any package command runs.

**Package-execution writes** (everything a mutating test/type/lint/build
command produces - generated `.cvf`, `.next`, generated `src` files,
caches, reports, test artifacts): allowed only inside the disposable
sandbox directory and its dedicated temporary support directory, created
fresh under the OS temp root, never inside Core and never inside the
public-sync clone.

**Public clone**: read-only for the complete worker turn, from before the
first Git-level check through after sandbox teardown. The runner must never
clean, restore, delete, or repair it under any circumstance, including to
correct a mutation the runner itself detects.

## Required Semantic Delta

The amended profile must, in addition to everything T1 already required:

1. keep every existing Git-level validation (root containment, remote,
   branch, clean state, HEAD match, non-empty range, exact 41-path
   manifest) running against the real public clone, read-only, exactly as
   T1 already implements it - this amendment does not touch that layer;
2. before any package command executes, materialize a disposable sandbox
   outside both the private Core and the public-sync roots, using a
   hash-verifiable read-only extraction (`git archive` from the real public
   clone at `authorizedCandidateHead`, or an equivalently verifiable
   method) rather than copying an uncommitted Core worktree as substitute
   evidence;
3. before package execution, prove the sandbox's materialized manifest and
   content correspond exactly to `authorizedCandidateHead` (deterministic
   materialization evidence: per-path hash or tree-object comparison), and
   fail closed on any missing, extra, or mismatched governed path;
4. achieve dependency isolation for the sandbox using only existing local
   dependency stores (junction/copy/link), never `npm install` and never
   network access; every junction/symlink/copy target must resolve inside
   the disposable sandbox or its dedicated temporary support directory,
   never inside the real public clone or the real Core;
5. permit mutation only inside the disposable sandbox (generated `.cvf`,
   `.next`, generated `src` files, caches, reports, and test artifacts are
   all acceptable there because the whole sandbox is disposable) and prove
   dependency isolation cannot allow entries in the real public clone to be
   replaced or mutated - fail closed if that proof cannot be constructed;
6. execute the full previously accepted candidate proof envelope inside the
   sandbox without substitution or narrowing, using the exact command
   manifest in Pinned Command Manifest below (not a paraphrase of it);
7. capture the real public clone's HEAD, branch, and full status (including
   untracked files, staged diff, and unstaged diff) both immediately before
   sandbox materialization begins and immediately after the complete
   sandboxed run (including any cleanup) finishes; any difference between
   the two captures is a `GATE`, even if the runner could technically
   repair it - the runner must never clean or repair the public clone
   itself, only report the discrepancy and fail;
8. fail closed on: sandbox creation/materialization failure; dependency
   isolation failure or unprovable isolation; source/manifest mismatch
   against the pinned head; missing executable inside the sandbox; command
   timeout or nonzero exit; cleanup failure that leaves temporary governed
   state behind; and any observed before/after change to the real public
   clone;
9. emit deterministic JSON plus human-readable summary and nonzero exit on
   any gate failure, exactly as T1 already requires, extended with the
   sandbox materialization, isolation, and invariant-capture evidence.

## Pinned Command Manifest

This is the exact, non-substitutable command manifest for the proof
envelope required by Required Semantic Delta item 6 and Acceptance
Criteria AC-04. All commands run inside the disposable sandbox only.

**Model Gateway** (sandbox path `EXTENSIONS/CVF_MODEL_GATEWAY`):

- full suite: `node_modules/.bin/vitest.cmd run --config vitest.config.ts` - expected 30 files / 231 tests passed.
- TypeScript: `node_modules/.bin/tsc.cmd -p tsconfig.json --noEmit` - expected zero errors.

**cvf-web** (sandbox path `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`):

- focused union-41 suite, exact 15 files, single `vitest run` invocation
  listing every path explicitly (no glob, no directory argument):
  `node_modules/.bin/vitest.cmd run` followed by exactly these 15 paths:

  1. `src/app/(dashboard)/lpci/page.test.tsx`
  2. `src/app/api/lpci/query/route.governance.test.ts`
  3. `src/app/api/lpci/query/route.test.ts`
  4. `src/lib/control-plane-events.test.ts`
  5. `src/lib/lpci/audit-receipt.test.ts`
  6. `src/lib/lpci/filter-pipeline.test.ts`
  7. `src/lib/lpci/provider-binding.test.ts`
  8. `src/lib/lpci/query-conformance.test.ts`
  9. `src/lib/lpci/release-audit.test.ts`
  10. `src/lib/lpci/release-health.test.ts`
  11. `src/lib/lpci/release-policy.test.ts`
  12. `src/lib/lpci/retrieval.test.ts`
  13. `src/lib/rate-limit.test.ts`
  14. `src/lib/server/system-health.test.ts`
  15. `src/lib/storage-adapter.test.ts`

  - expected 15 files / 218 tests passed.
- TypeScript: `node_modules/.bin/tsc.cmd --noEmit -p tsconfig.json` under
  the complete eight-package offline dependency topology - expected zero
  errors.
- scoped ESLint: `node_modules/.bin/eslint.cmd
  src/app/api/lpci/query/route.governance.test.ts` - this is the exact
  predecessor-accepted scope (Amendment 2's "Scoped ESLint" row); a
  broader candidate-owned lint set (for example the full `src` tree used
  in the rejected T1 attempt) is not authorized by this baseline and must
  not be substituted unless separately source-verified in a future
  amendment.

**Production build** (sandbox path
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`), exact sequence, all three
commands required in order:

1. `node scripts/build-risk-models.js`
2. `node scripts/build-skill-index.js`
3. `node node_modules/next/dist/bin/next build --webpack` - expected
   successful compilation and 121 static pages.

All expected counts (231 tests, 218 tests, 121 static pages, zero
TypeScript errors, zero ESLint problems in scope) are evidence
expectations recorded for comparison, not permission to treat a nonzero
exit code, a missing executable, or a timeout as anything other than a
`GATE` failure. A run that produces different counts than expected is
itself a fail-closed condition requiring investigation, not a value to
silently accept because "the command ran."

## Forbidden Scope

No edit to generic pre-push catalogs or weakening of private gates (carried
forward from T1). No public clone edit, commit, push, deploy, Netlify
action, secret read, network install, `npm install`, public `main`,
production promotion, or unrelated source change. No substitution of any
required test/type/lint/build command category with a narrower or
unrelated one; no dropping of a category to resolve the read-only-vs-build
conflict - the conflict is resolved by sandbox location, not by requirement
weakening. No junction, symlink, or copy target may resolve inside either
real repository root.

## Verification Contract

- focused pytest for the amended runner, including new sandbox-specific
  fail-closed cases;
- runner `--help` and policy schema validation (unchanged surface, plus any
  new sandbox-related flags/policy fields);
- negative tests proving: mutating commands write only inside the sandbox;
  the real public root remains unchanged after a full run; sandbox source
  content matches the pinned head; sandbox/path escape fails closed;
  dependency-link target escape fails closed; cleanup failure fails closed;
  real test/type/lint/build nonzero-exit and timeout conditions gate
  (not merely resolution-layer or Git-subprocess substitutes); the policy
  check registry reconciles exactly against what actually executed;
- one real-candidate run that materializes an actual disposable sandbox
  from the real public clone at the pinned head, runs the full proof
  envelope inside it, tears it down, and proves the real public clone was
  unchanged throughout;
- existing Core reviewer-fast and pre-closure gates.

## Acceptance Criteria

- AC-01: the real public clone is validated read-only for every Git-level
  check, exactly as T1 already does; no new write path to it is
  introduced.
- AC-02: package commands execute only inside a disposable sandbox
  materialized from a hash-verified extraction of `authorizedCandidateHead`.
- AC-03: dependency isolation uses only existing local stores; no install;
  no network; every link target is proven to resolve only inside the
  sandbox or its temporary support directory.
- AC-04: the exact Pinned Command Manifest executes unweakened inside the
  sandbox, with actual results compared against its recorded expected
  counts (Model Gateway 30/231 + TypeScript; cvf-web union-41 exact-15
  files/218 tests; cvf-web TypeScript under the complete eight-package
  topology; scoped ESLint limited to
  `src/app/api/lpci/query/route.governance.test.ts`; production build with
  121 static pages) - any nonzero exit, missing executable, or timeout
  gates regardless of count expectations.
- AC-05: the profile fails closed for every negative case listed in the
  Verification Contract, with tests that could not pass via a Git-layer or
  resolution-layer substitute.
- AC-06: before/after invariant capture of the real public clone (HEAD,
  branch, full status) surrounds the complete sandboxed run; any delta is a
  `GATE`; the runner never repairs or cleans the public clone.
- AC-07: worker changes remain inside the existing five T1 owner paths
  unless a named checker proves a separate path is required.
- AC-08: no public, remote, provider, secret, or deployment effect occurs
  at any point, including during sandbox teardown.

## Decision / Baseline / Proposed Tranche

Decision: PROCEED_DISPOSABLE_SANDBOX_AMENDMENT.

This is the amendment-authoring tranche only. It authorizes drafting the
paired work order and, upon separate no-commit worker dispatch,
implementing the disposable-sandbox strategy inside the existing five T1
paths. It does not itself implement, execute, commit, push, or deploy
anything.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: provenance-owned amendment authority only.

## Claim Boundary

This baseline authorizes a local, provenance-owned amendment to the T1
public-projection pre-push profile: disposable-sandbox execution of
mutating package commands, with the real public clone remaining strictly
read-only evidence throughout. It makes no claim of push, deploy, hosted
behavior, production readiness, or public export, and it does not itself
implement or execute anything.
