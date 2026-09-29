# CVF Agent Work Order - Public Projection Pre-Push T1 Profile Owner And Gate Amendment 1

Memory class: FULL_RECORD

Status: READY_FOR_DISPATCH

docType: work_order

Date: 2026-08-12

Batch ID: PUBLIC-PROJECTION-PREPUSH-T1-AMENDMENT-1

dispatchBaseHead: `bbcb21acd753ec5c4f5a5c234da585e09febc562`

executionBaseHead: a distinct, later value the orchestrator supplies after
committing exactly the three Amendment 1 authority artifacts (this work
order, its paired baseline, and the source verification) to Core.
`executionBaseHead` concerns that committed authority delta only; it does
not describe or require any state change to the five inherited T1 working
paths, which remain controlled by the Preimage Authority Matrix in the
paired baseline. No session-sync commit is required before worker
execution unless separately performed and explicitly reported.

closureBaseHead: same as executionBaseHead because worker must not commit.

Commit mode: WORKER_MUST_NOT_COMMIT

## Dispatch Prompt Envelope

Task ID: PUBLIC-PROJECTION-PREPUSH-T1-AMENDMENT-1

Role: implementation worker

Objective: amend the provenance-owned public-projection pre-push profile so
that mutating package commands (test/type/lint/build) execute only inside a
disposable, hash-verified candidate sandbox materialized outside both
repository roots, while the real public clone remains strictly read-only
evidence for every existing Git-level validation, resolving the
`BLOCKED_CONTRACT_CONTRADICTION` recorded against T1 without weakening any
required command.

Allowed tools: local file reads, apply_patch, Git read-only inspection,
Python, pytest, PowerShell, local filesystem operations strictly bounded to
a disposable temporary sandbox directory and its dedicated support
directory, and governance gates.

Forbidden tools/actions: commit, push, deploy, browser/provider/store,
secrets, network install, `npm install`, public-clone mutation, production,
public `main`. Two distinct write boundaries apply and must not be
conflated: implementation-authoring writes are allowed only on the exact
five Core owner paths (apply_patch/local editor only, no other Core path);
package-execution writes (everything a mutating test/type/lint/build
command produces) are allowed only inside the disposable sandbox and its
temporary support directory, never inside Core or the public clone. See the
paired baseline's Write Boundary section for the complete rule.

Expected outputs: the same five T1 owner paths, amended in place.

Terminal status: `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Resolve T1's `BLOCKED_CONTRACT_CONTRADICTION` by relocating mutating package
execution to a disposable candidate sandbox, per the accepted Amendment 1
source verification, while preserving every existing fail-closed Git-level
validation against the real public clone unchanged.

## Scope / Target / Owner Boundary

Worker owns exactly the same five paths T1 already owns; no new path:

- `docs/reference/CVF_PUBLIC_PROJECTION_PRE_PUSH_PROFILE_STANDARD_2026-08-11.md`
- `governance/compat/CVF_PUBLIC_PROJECTION_PRE_PUSH_POLICY.json`
- `governance/compat/run_public_projection_pre_push_gate.py`
- `governance/compat/test_run_public_projection_pre_push_gate.py`
- `docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_WORKER_RETURN_2026-08-11.md`

Reviewer/closer owns acceptance and commits. Session-sync steward owns later
continuity changes. The real public clone remains read-only evidence at all
times; it is never a write target for this amendment.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator | dispatcher/amendment-author role instruction naming `REVIEWER_CONFIRMED_BLOCKED_UNDER_CURRENT_CONTRACT` and the disposable-sandbox amendment decision | ACCEPT |
| T1 blocked disposition | `docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_WORKER_RETURN_2026-08-11.md` | ACCEPT |
| Amendment 1 source verification | `docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_AMENDMENT_1_SOURCE_VERIFICATION_2026-08-12.md` | ACCEPT |
| GC-018 Amendment 1 | `docs/baselines/CVF_GC018_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_AMENDMENT_1_2026-08-12.md` | ACCEPT |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T1's build blocker is real against the real public clone | BEHAVIOR | `docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_WORKER_RETURN_2026-08-11.md` | Findings / Position | `prebuild` `fs.rmSync`/`fs.writeFileSync` evidence | T1 blocked worker return | ACCEPT |
| The eight-package dependency topology for the identical public candidate is viable and produces a successful build (121 static pages) when fully materialized; this proves topology and outcome only, not disposable-sandbox isolation - Amendment 2 materialized its junctions directly inside the real public clone's worktree and restored them afterward, which is not the pattern this amendment authorizes | EXECUTION_EVIDENCE | `docs/reviews/CVF_LPCI1_REF_T1A_PUBLIC_SAFE_BRANCH_DEPLOY_BINDING_AMENDMENT_2_COMPLETION_2026-08-11.md` | Findings / Position; Verification table | Production build PASS row | Amendment 2 accepted completion | ACCEPT |
| `cvf-web` declares exactly eight `file:` sibling dependencies, each needed for offline dependency isolation | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` (public candidate) | `dependencies` block | `cvf-control-plane-foundation`, `cvf-execution-plane-foundation`, `cvf-guard-contract`, `cvf-learning-plane-foundation`, `cvf-model-gateway`, `cvf-refinery`, `cvf-truth-flow`, `cvf-truth-kernel` | public candidate package manifest | ACCEPT |
| `cvf-model-gateway`'s own relative imports require it to sit at its real sibling position (not a flattened `node_modules` copy) for TypeScript resolution to succeed | BEHAVIOR | `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` (public candidate) | import statements | `../../CVF_v1.7.3_RUNTIME_ADAPTER_HUB/...`, `../../CVF_v1.2.1_EXTERNAL_INTEGRATION/...` | Model Gateway package source | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | dispatch envelope, source verification columns, protected paths, operation trace, bounded claim fields, public disposition |
| gateRunPurpose | confirm source-backed work-order shape before dispatch; not first discovery |
| claimBoundary | packet validation only; no implementation, sandbox execution, or push claim |

## Agent Roles

| Role | Owner | Boundary |
| --- | --- | --- |
| Dispatcher | orchestrator/amendment author | committed authority only |
| Worker | delegated implementation worker | exact five-path no-commit sandbox-strategy implementation |
| Reviewer/closer | independent reviewer | semantic review, real-candidate sandboxed re-run, material commit |
| Session-sync steward | orchestrator | separate continuity commit |

## Intake Role Routing Decision

route: MULTI_AGENT_MULTI_ROLE

selected role route: MULTI_AGENT_MULTI_ROLE

implementation owner: delegated worker

review/commit owner: independent reviewer/closer

intake summary: implement the operator-authorized disposable-sandbox amendment inside the existing five T1 owner paths.

risk sensitivity: HIGH because a false pass could authorize public push, and an isolation defect could mutate the real public clone.

scope classification: BOUNDED_GOVERNANCE_CONTROL_IMPLEMENTATION.

escalation condition: public mutation, generic-gate weakening, secrets/network, any command-category weakening or omission, dependency-isolation defect, or any path beyond the exact five-path manifest.

## Worker Autonomy / No-Question Rule

Repair any failure inside the exact owned paths and rerun. Return only for a
scope conflict, missing authority, required public mutation, secret/network
need, a genuinely irreconcilable command requirement (in which case return
`BLOCKED_CONTRACT_CONTRADICTION` again with fresh evidence, not silently
weakened output), or an irreparable gate failure outside scope.

## Current Runtime Freshness Verification

At dispatch, Core `HEAD` is `bbcb21acd753ec5c4f5a5c234da585e09febc562`
(`dispatchBaseHead`) with the exact inherited five-path T1 dirty set
present (four intent-to-added with zero staged content, one untracked) and
no other dirty path - Core is not, and is never claimed to be, clean.
Public clone is clean on `lpci1-ref-staging@021f8b852` with the correct
`origin` remote. Re-verify read-only at execution. The five existing T1
worker-owned paths remain exactly as the blocked worker return left them;
see the Preimage Authority Matrix in the paired baseline for their pinned
SHA-256 values.

## Required First Reads

Read startup surfaces, guard orientation, this work order, the paired
GC-018 Amendment 1 baseline (including its Preimage Authority Matrix,
Worker Preflight Requirements, Authority Commit Choreography, and Pinned
Command Manifest sections), the Amendment 1 source verification, the T1
blocked worker return, the T1 baseline/work order, the LPCI1-REF-T1A
Amendment 2 completion and worker return, and the applicable checker
sources before editing.

## Pre-Flight Checks

Require Core `HEAD` equal to the `executionBaseHead` the orchestrator
supplies at dispatch (a value distinct from `dispatchBaseHead`; see
Authority Commit Choreography). Require the Core working-tree dirty set to
be exactly the five paths in the paired baseline's Preimage Authority
Matrix, each hashing to its pinned SHA-256, with zero staged content and no
additional dirty path; any mismatch is `BLOCKED_PREIMAGE_MISMATCH`. Require
public clone clean at exact commit `021f8b852`, branch `lpci1-ref-staging`,
correct remote, and zero staging. Run the pre-implementation autorun gate
before material edits.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`PUBLIC-PROJECTION-PREPUSH-T1 Amendment 1 sandbox verification dispatch`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED

Worker must rerun the exact resolver query at execution time and record the
result again; a `NONE_RETURNED` result at dispatch-authoring time is not a
substitute for the worker's own pre-implementation run.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: amend in place the same one isolated
public-projection runner, its policy registry, focused tests, and the
companion standard that T1 already authorized. Do not change generic
checkers, hook catalogs, or existing guard semantics. Do not introduce any
new protected path.

Protected paths:

- `governance/compat/CVF_PUBLIC_PROJECTION_PRE_PUSH_POLICY.json`
- `governance/compat/run_public_projection_pre_push_gate.py`
- `governance/compat/test_run_public_projection_pre_push_gate.py`

Operator authorization: dispatcher/amendment-author role instruction and
disposition source for this batch.

Rollback boundary: revert exactly the five existing T1 paths to their
blocked-worker-return state if rejected; do not revert candidate commits
`492e11eab`, `021f8b852`, or any session-sync commit.

## Large-Scope Change Authorization

AUTHORIZED_EXACT_INHERITED_PUBLIC_RANGE for read-only evaluation of the
exact 41-path range
`2103a38fda01ee827e9fc6c3be38a824fa5d54ad..021f8b852afc245a6383177dd69bf56caf488b02`,
identical to T1. No public clone mutation is authorized. Additionally
authorizes materializing a disposable, hash-verified read-only extraction
of the exact candidate commit `021f8b852afc245a6383177dd69bf56caf488b02`
into a temporary sandbox directory outside both repository roots, strictly
to run mutating package commands; the sandbox is never a governed authority
surface.

## Execution Instructions

Implement the disposable-sandbox strategy literally against the real public
clone at `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync`:

1. Keep every existing Git-level validation against the real public clone
   unchanged: root containment, remote, branch, clean state, HEAD match,
   non-empty range, exact 41-path manifest.
2. Before any package command, materialize a sandbox in a fresh temporary
   directory (e.g. under the OS temp root, never inside either repository
   root) using `git archive <authorizedCandidateHead> | tar -x` (or an
   equivalently hash-verifiable extraction) run against the real public
   clone's Git object store read-only - never by copying the public clone's
   working-tree files directly, and never by copying anything from an
   uncommitted Core worktree.
3. Prove the sandbox's materialized content matches the pinned head: compare
   the archived path set and per-path content hash against
   `git ls-tree -r <authorizedCandidateHead>` / `git show
   <authorizedCandidateHead>:<path>` read against the real clone. Fail
   closed on any missing, extra, or mismatched path.
4. Materialize dependency isolation for the sandbox's eight `cvf-web`
   sibling `file:` packages (and Model Gateway's own transitive sibling
   references) using junctions/symlinks/copies sourced only from existing
   local dependency stores already present on this machine (for example the
   real public clone's or Core's already-installed `node_modules`, used as
   a read-only copy source, never as a live link target). No `npm install`;
   no network access. Every created junction/symlink/copy target must
   resolve to a path inside the sandbox directory or its dedicated
   temporary support directory; verify this explicitly and fail closed if
   any target would resolve inside either real repository root.
5. Run the exact Pinned Command Manifest from the paired baseline inside
   the sandbox only, using the exact argv listed there (Model Gateway
   full `vitest run` and `tsc --noEmit`; the exact 15-file cvf-web
   `vitest run` invocation listing every path explicitly, never a glob or
   directory; cvf-web `tsc --noEmit -p tsconfig.json` under the complete
   eight-package offline dependency topology; ESLint scoped to exactly
   `src/app/api/lpci/query/route.governance.test.ts`, the
   predecessor-accepted scope, not a broader `src` lint; then the
   three-step build sequence `node scripts/build-risk-models.js`, `node
   scripts/build-skill-index.js`, `node
   node_modules/next/dist/bin/next build --webpack`) - all inside the
   sandbox, never against the real public clone. Compare actual counts
   against the manifest's recorded expectations (231 tests, 218 tests, 121
   static pages) as evidence, but treat any nonzero exit, missing
   executable, or timeout as `GATE` regardless of count.
6. Capture the real public clone's HEAD, branch, and full `git status
   --short` (including untracked files) plus staged and unstaged diff
   immediately before sandbox materialization begins and immediately after
   the complete sandboxed run and its cleanup finish. Any difference is a
   `GATE`. Never have the runner clean, restore, or repair the public
   clone; only report the discrepancy and fail.
7. Tear down the sandbox and its temporary support directory completely
   after the run (success or failure). Fail closed if cleanup itself fails
   or leaves temporary governed state behind.
8. Add positive and fail-closed tests using temporary local fixtures for
   the sandbox lifecycle (materialization, hash verification, dependency
   isolation, escape attempts, cleanup failure) plus real subprocess
   execution for nonzero-exit and timeout cases, exactly as D-02 of the
   prior T1 repair required for the non-sandbox commands; never substitute
   a Git-subprocess failure for a package-command failure or timeout.
9. Run focused tests, help, syntax/type checks, one real-candidate run that
   actually materializes a sandbox from the real public clone, the
   worker-return fast gate, and final status evidence.
10. Return without commit.

## Write Ownership

Implementation-authoring writes: exactly the five paths in Scope, and no
other Core path. No deletion or rename. No generated aggregate, session,
public clone, hook catalog, or existing checker edits.

Package-execution writes (produced by running test/type/lint/build
commands): allowed only inside the disposable sandbox and its temporary
support directory; never inside Core and never inside the public clone.
The sandbox itself is never committed, staged, or left behind after the
run - it is torn down completely regardless of run outcome.

## Execution Plan

1. Reconfirm source, path state, bases, remotes, and ADIF.
2. Amend the standard: add the sandbox-materialization, hash-verification,
   dependency-isolation, and before/after invariant-capture requirements to
   Fail-Closed Validation Requirements; keep everything else T1 already
   requires.
3. Amend the policy JSON: add sandbox configuration (source extraction
   method, dependency-link plan, full command set restored to the
   previously accepted envelope) and remove the prior `excludedCommands`
   entries whose exclusion reason no longer applies once execution is
   sandboxed.
4. Amend the runner: add sandbox materialization/verification/isolation/
   teardown logic; route every mutating package command through the
   sandbox; add before/after real-public-clone invariant capture around the
   full run; keep the existing Git-level validation layer unchanged.
5. Extend the focused tests with the new sandbox-specific fail-closed cases
   and the full-envelope real-candidate proof.
6. Run focused tests, help, real-candidate sandboxed run, worker-return fast
   gate, and final status evidence.
7. Amend the T1 worker return in place to record this amendment's repaired
   evidence and updated terminal disposition.
8. Return without commit.

## Work-Order Fulfillment Manifest

Expected changed set is exactly the five existing T1 paths, amended in
place. Manifest delta must be `MATCH`.

## Required Artifact Manifest

| Path | Required at handoff |
| --- | --- |
| `docs/reference/CVF_PUBLIC_PROJECTION_PRE_PUSH_PROFILE_STANDARD_2026-08-11.md` | yes |
| `governance/compat/CVF_PUBLIC_PROJECTION_PRE_PUSH_POLICY.json` | yes |
| `governance/compat/run_public_projection_pre_push_gate.py` | yes |
| `governance/compat/test_run_public_projection_pre_push_gate.py` | yes |
| `docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_WORKER_RETURN_2026-08-11.md` | yes |

All five paths already exist from T1; this amendment requires each to still
exist, amended in place, at worker handoff. No new path is required.

## Evidence Requirements

Record command, working directory, result, exit code, relevant safe output,
exact manifest, policy hash, current Core/public Git state (before and
after the full run), sandbox path (temporary, never a governed path), and
negative tests. Do not record credentials, headers, tokens, cookies, or
Netlify configuration values.

## Verification Commands

- `python -m pytest governance/compat/test_run_public_projection_pre_push_gate.py -q`
- `python governance/compat/run_public_projection_pre_push_gate.py --help`
- exact runner invocation against the real, read-only public candidate,
  materializing an actual disposable sandbox, using the committed policy,
  base, and head required by the baseline
- `python governance/compat/run_worker_return_fast_gate.py`
- `git diff --check`

## Acceptance Criteria

- AC-01: Git-level validation against the real public clone is unchanged
  and still read-only.
- AC-02: package commands execute only inside a disposable, hash-verified
  sandbox extracted from `authorizedCandidateHead`.
- AC-03: dependency isolation uses only existing local stores; no install;
  no network; no link target resolves inside either real repository root.
- AC-04: the exact Pinned Command Manifest from the paired baseline
  executes unweakened, with results compared against its recorded
  expected counts.
- AC-05: fail-closed coverage exists for sandbox creation failure,
  dependency isolation failure, source/manifest mismatch, missing
  executable, timeout, nonzero exit, cleanup failure, and any real-clone
  before/after delta.
- AC-06: worker changes remain exactly the five existing T1 paths.
- AC-07: all required gates pass; no public, remote, provider, or
  deployment effect occurs.
- AC-08: the amended worker return records the prior rejection, the
  amendment, and a truthful updated terminal disposition -
  `COMPLETE_PENDING_REVIEW` only if the full envelope genuinely passes
  inside the sandbox with zero real-clone deltas, otherwise
  `BLOCKED_WITH_REASON` with fresh evidence.

## Review Gate

Independent reviewer must inspect all code and policy changes, rerun
negative tests and one independent real-candidate sandboxed run, confirm
the real public clone showed zero deltas throughout, confirm the full
proof envelope executed unweakened, and run reviewer-fast plus
committed-range pre-closure before acceptance.

## Closure Checklist

No open acceptance item; exact five-path manifest; all tests/gates PASS; no
public mutation at any point; worker did not commit; reviewer owns material
commit; session sync is separate; push remains a later tranche.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for any required public edit, generic-gate
weakening, missing stable owner, secret/network need, an irreconcilable
command requirement even after sandboxing (with fresh evidence), or failure
outside the exact owned scope.

## Operator Checkpoint

No checkpoint inside owned local implementation. Push and Netlify
deployment remain separate external-action checkpoints after accepted
closure.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | worker-no-commit split |
| phase | EXECUTION |
| baseHeadFor(phase) | exact committed executionBaseHead |
| changedSetScope(phase) | exact five worker-owned paths |
| traceScope(phase, actor) | local sandboxed gate implementation and proof only |
| commitOwner(phase) | reviewer/closer |
| crossBatchIsolation | public candidate and unrelated Core remain unchanged |
| nextMoveSurfaces | reviewer/session steward owned |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_AMENDMENT_1_COMPLETION_2026-08-12.md`

reviewerOwnedClosurePaths: exact five worker paths, optional completion
review if needed, then separate session sync. A separate amendment-return
artifact (distinct from the existing T1 worker return) is authorized only
if a named checker proves updating the existing worker return in place
cannot satisfy its structural requirements; that determination and its
citation must be recorded by the worker before creating any such file.

## Foundation Storage Layout Block

N/A with reason: this tranche amends governance control-plane files and
adds disposable, non-tracked temporary sandbox logic; it does not add
foundation runtime storage.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Public/simple CVF vocabulary |
| Chain map route | N/A with reason: no external knowledge intake |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | T1 standard, policy, runner, tests, and worker return (Amendment 1) |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | no external authority admitted |

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required section names include Purpose, Target / Source, Scope /
Methodology, Findings / Position, Risk / Corrective Action, Checker Source
Read-Ahead Block, Agent Operation Trace Block, Delta Execution Claim
Boundary Control Block, External Knowledge Intake Routing, Rescan
Intelligence Hardening, Corpus Completeness And Report Integrity, Epistemic
Process Block, Machine Closure Package, Public Export Disposition, Claim
Boundary, git status --short, Changed Files, Worker Experience
Retrospective, Command Evidence, No-Commit Statement, and Terminal
Disposition.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| INTERNAL_AGENT | local Python CLI, policy, and disposable sandbox | read-only public-root evaluation; sandbox-only mutation | JSON receipt and exit code | subprocess/Git/filesystem boundary bounded to sandbox | BUILD |
| EXTERNAL_AGENT_CLI_MCP | CLI may be invoked by an external worker only under the same explicit arguments | no MCP/provider authority | identical local receipt | CLI only; no MCP adapter | CONTRACT_ONLY |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher/amendment author |
| Provider or surface | private Core plus read-only public clone |
| Session or invocation | `public-projection-prepush-t1-amendment-1-dispatch-20260812` |
| Working directory | private Core root |
| Command or tool surface | local reads, Git inspection, ADIF resolver, apply_patch, governance gates |
| Target paths | paired Amendment 1 source verification, baseline, and work order |
| Allowed scope source | dispatcher/amendment-author role instruction and disposition source |
| Before status evidence | Core `HEAD` at `bbcb21acd753ec5c4f5a5c234da585e09febc562` with exact inherited five-path T1 dirty set present, zero staged, no other dirty path; public clean at `021f8b852` |
| After status evidence | authority pending commit; five T1 paths and public clone untouched |
| Diff evidence | Core `git status --short` partitions into exactly three sets: (1) inherited five-path T1 implementation set (four intent-to-added, one untracked, unchanged from before this dispatch) - see Preimage Authority Matrix in the paired baseline; (2) new three-path Amendment 1 authority-authoring set (this work order, the paired baseline, the source verification), all untracked pending commit; (3) unexpected paths: none |
| Approval boundary | local dispatch-authoring only |
| Claim boundary | no implementation, sandbox execution, push, deploy, provider/store, secret, or production action |
| Agent type | dispatcher/amendment author |
| Invocation ID | `public-projection-prepush-t1-amendment-1-dispatch-20260812` |
| Expected manifest | source verification, baseline, work order |
| Actual changed set | source verification, baseline, work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: three new authority files only |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: relocating mutating package execution to a
disposable, hash-verified sandbox that mirrors the already-proven Amendment
2 offline-junction topology will let the full previously accepted proof
envelope pass without ever writing to the real public clone.

Evidence Comparison Requirement: compare the sandboxed run's evidence
against the Amendment 2 completion's accepted proof rows and against the
before/after real-clone invariant capture.

Contradiction Handling Requirement: any before/after delta on the real
public clone, any unresolved dependency-isolation escape, or any weakened
command requires a Contradiction Or Gap Disposition and a blocked return.

Claim Update Requirement: confirm, revise, narrow, or invalidate the
sandbox-amendment claim from evidence.

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_CURRENT_SOURCE

priorVerificationArtifact: the T1 blocked worker return and the LPCI1-REF-T1A
Amendment 2 completion/worker return are predecessor authority, not
substituted execution proof.

priorVerificationAnchor: public base `2103a38f` and candidate `021f8b852`.

freshRecomputeRequired: yes, all sandbox materialization, isolation, proof
envelope, and before/after invariant evidence.

unicodePathHandling: use resolved literal paths and UTF-8-safe readers.

extractedTextAuthority: repository bytes and command results only.

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | local disposable-sandbox amendment implementation and read-only proof against the real public clone |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: worker has not executed yet |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source-backed dispatch packet |
| invocationBoundary | exact local owner paths; public clone read-only; sandbox strictly temporary and outside both repository roots |
| interceptionBoundary | no IDE, provider, browser, network, or remote mutation claim |
| claimLanguage | ready for no-commit implementation |
| forbiddenExpansion | generic gate weakening, public mutation, push, deploy, secrets, provider/store, production, command-category omission |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this work order authorizes local provenance gate amendment only.

## Claim Boundary

This work order does not authorize push or Netlify deployment. Successful
worker return still requires independent review, material commit, and a
later explicit external-action tranche.
