# CVF Agent Work Order - Public Projection Pre-Push T1 Profile Owner And Gate Amendment 2

Memory class: FULL_RECORD

Status: READY_FOR_DISPATCH

docType: work_order

Date: 2026-08-12

Batch ID: PUBLIC-PROJECTION-PREPUSH-T1-AMENDMENT-2

dispatchBaseHead: `225b6a01ab4400244a5cf56e47f58d16ecc0fba6`

executionBaseHead: a distinct, later value the orchestrator supplies after
committing the exact four-path Amendment 2 authority batch (this work
order, its paired GC-018 baseline, the source verification, and
`governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json`) to
Core.
`executionBaseHead` concerns that committed authority delta only; it does
not describe or require any state change to the five inherited
Amendment-1 working paths, which remain controlled by the Preimage
Authority Matrix in the paired baseline. No session-sync commit is
required before worker execution unless separately performed and
explicitly reported.

closureBaseHead: same as executionBaseHead because worker must not commit.

Commit mode: WORKER_MUST_NOT_COMMIT

## Dispatch Prompt Envelope

Task ID: PUBLIC-PROJECTION-PREPUSH-T1-AMENDMENT-2

Role: implementation worker

Objective: extract cohesive non-CLI implementation out of
`governance/compat/run_public_projection_pre_push_gate.py` into a new
library helper, `governance/compat/public_projection_pre_push_gate_lib.py`,
so both the CLI runner and the focused test file satisfy the closure-hook
governed Python automation size guard, while preserving every behavioral
invariant Amendment 1 already independently proved unchanged.

Allowed tools: local file reads, apply_patch, Git read-only inspection,
Python, pytest, PowerShell, local filesystem operations strictly bounded
to a disposable temporary sandbox directory and its dedicated support
directory (verification phase only), and governance gates.

Forbidden tools/actions: commit, push, deploy, browser/provider/store,
secrets, network install, `npm install`, public-clone mutation,
production, public `main`. Two distinct write boundaries apply and must
not be conflated: implementation-authoring writes are allowed only on the
exact seven Core owner paths (apply_patch/local editor only, no other Core
path); package-execution writes (everything a mutating test/type/lint/build
command produces during the worker's own required verification phase) are
allowed only inside the disposable sandbox and its temporary support
directory, never inside Core or the public clone. See the paired
baseline's Write Boundary section for the complete rule.

Expected outputs: the seven Amendment 2 owner paths, amended/created in
place.

Terminal status: `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Satisfy the closure-hook governed Python automation size guard
(`governance/compat/check_python_automation_size.py`) that currently
blocks commit/closure of the functionally-accepted Amendment 1 result, by
relocating cohesive non-CLI implementation into a new library helper, with
zero change to observable behavior, evidence, or fail-closed logic.

## Scope / Target / Owner Boundary

Worker owns exactly seven paths (five inherited from Amendment 1 plus one
new helper and the size-exception registry):

- `docs/reference/CVF_PUBLIC_PROJECTION_PRE_PUSH_PROFILE_STANDARD_2026-08-11.md`
- `governance/compat/CVF_PUBLIC_PROJECTION_PRE_PUSH_POLICY.json`
- `governance/compat/run_public_projection_pre_push_gate.py`
- `governance/compat/public_projection_pre_push_gate_lib.py` (new)
- `governance/compat/test_run_public_projection_pre_push_gate.py`
- `docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_WORKER_RETURN_2026-08-11.md`
- `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json`

Reviewer/closer owns acceptance and commits. Session-sync steward owns
later continuity changes. The real public clone remains read-only evidence
at all times; it is never a write target for this amendment.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator | dispatcher/Amendment-2-author authority-repair instruction naming `FUNCTIONALLY_ACCEPTED` / `CLOSURE_REJECTED_SIZE_GUARD`, the seven-path helper-extraction decision, and the official GC-018-seeded exception mechanism | ACCEPT |
| Amendment 1 worker return (functionally accepted) | `docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_WORKER_RETURN_2026-08-11.md` | ACCEPT |
| Amendment 2 source verification | `docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_AMENDMENT_2_SOURCE_VERIFICATION_2026-08-12.md` | ACCEPT |
| GC-018 Amendment 2 | `docs/baselines/CVF_GC018_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_AMENDMENT_2_2026-08-12.md` | ACCEPT |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| `run_public_projection_pre_push_gate.py` is 1380 physical lines, 580 lines over the `python_cli_orchestrator` hard limit of 800 | VALUE | `governance/compat/run_public_projection_pre_push_gate.py`; `governance/compat/check_python_automation_size.py` | full file; `DEFAULT_CLASS_THRESHOLDS`, line 39 | n/a; `DEFAULT_CLASS_THRESHOLDS["python_cli_orchestrator"]["hardThresholdLines"]` | governed size checker | ACCEPT |
| `test_run_public_projection_pre_push_gate.py` is 1279 physical lines, 79 lines over the `python_test` hard limit of 1200 | VALUE | `governance/compat/test_run_public_projection_pre_push_gate.py`; `governance/compat/check_python_automation_size.py` | full file; `DEFAULT_CLASS_THRESHOLDS`, line 37 | n/a; `DEFAULT_CLASS_THRESHOLDS["python_test"]["hardThresholdLines"]` | governed size checker | ACCEPT |
| A new `governance/compat/*.py` file that is neither `check_*.py`-named nor `run_*.py`-named nor test-named classifies as `python_library_helper` (soft 600 / hard 900) | BEHAVIOR | `governance/compat/check_python_automation_size.py` | `_classify_python`, lines 49-71 | `_classify_python` | classification function | ACCEPT |
| Amendment 1's real-candidate result is functionally accepted: 58/58 tests, exit 0, `compliant: true`, zero gate failures, exact evidence reconciliation on all `expectedEvidence`-bearing commands | EXECUTION_EVIDENCE | n/a (independent reviewer reproduction cited directly in this dispatch prompt, not a repository file) | n/a | n/a | independent reviewer evidence | ACCEPT |
| The profile's own `governed_python_automation_size` inherited-debt family checks an unrelated pinned file, not the CLI runner or test file - the closure-hook failure is a separate, general-purpose gate | VALUE | `governance/compat/CVF_PUBLIC_PROJECTION_PRE_PUSH_POLICY.json` | lines 65-71 | `inheritedDebtFamilies.governed_python_automation_size.subjectPath` | policy `inheritedDebtFamilies` block | ACCEPT |
| A new exception absent from the protected registry baseline is authorized when its `seedAuthorization` names an existing GC-018; later only a strict downward `approvedMaxLines` ratchet with every other field unchanged is authorized | BEHAVIOR | `governance/compat/check_python_automation_size.py`; `governance/compat/policy_baseline.py` | `_has_valid_seed_authorization`; `_is_authorized_ratchet_down`; `load_json_policy_baseline` | exception registry comparison | governed size checker / baseline loader | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_python_automation_size.py`; `governance/compat/policy_baseline.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_equivalence_claim_evidence.py` |
| literalTokensReviewed | seeded-exception authorization, `approvedMaxLines`-only downward ratchet, dispatch envelope, source verification columns, protected paths, operation trace, bounded claim fields, public disposition, `DEFAULT_CLASS_THRESHOLDS` category values |
| gateRunPurpose | confirm source-backed work-order shape before dispatch; not first discovery |
| claimBoundary | packet validation only; no implementation, sandbox execution, or push claim |

## Agent Roles

| Role | Owner | Boundary |
| --- | --- | --- |
| Dispatcher | orchestrator/Amendment-2 author | committed authority only |
| Worker | delegated implementation worker | exact seven-path no-commit structural refactor and registry ratchet |
| Reviewer/closer | independent reviewer | semantic review, real-candidate sandboxed re-run, material commit |
| Session-sync steward | orchestrator | separate continuity commit |

## Intake Role Routing Decision

route: MULTI_AGENT_MULTI_ROLE

selected role route: MULTI_AGENT_MULTI_ROLE

implementation owner: delegated worker

review/commit owner: independent reviewer/closer

intake summary: extract cohesive non-CLI logic into a new library helper
to satisfy the closure-hook size guard, inside the repaired seven-path
Amendment 2 owner scope.

risk sensitivity: MEDIUM because this is a structural-only refactor of
already-proven behavior, but an incomplete extraction or a broken import
could silently regress fail-closed evidence reconciliation without a
functional review catching it if the worker skips real-candidate
re-verification.

scope classification: BOUNDED_GOVERNANCE_CONTROL_MAINTAINABILITY.

escalation condition: public mutation, generic-gate weakening, secrets/network,
any command-category weakening or omission, any behavioral invariant
regression, circular import between the CLI runner and the helper, or any
path beyond the exact seven-path manifest.

## Worker Autonomy / No-Question Rule

Repair any failure inside the exact owned paths and rerun. Return only for
a scope conflict, missing authority, required public mutation,
secret/network need, a genuinely irreconcilable size-vs-behavior
requirement (in which case return `BLOCKED_WITH_REASON` again with fresh
evidence, not silently weakened output), or an irreparable gate failure
outside scope.

## Current Runtime Freshness Verification

At authority repair, Core `HEAD` is `225b6a01ab4400244a5cf56e47f58d16ecc0fba6`
(`dispatchBaseHead`) with the exact inherited five-path Amendment-1 dirty set present
(all five untracked, zero staged content) and no other dirty path - Core
is not, and is never claimed to be, clean. Public clone is clean on
`lpci1-ref-staging@021f8b852` with the correct `origin` remote. Re-verify
read-only at execution. The five existing Amendment-1 worker-owned paths
remain exactly as the accepted worker return left them; see the Preimage
Authority Matrix in the paired baseline for their pinned SHA-256 values.
`governance/compat/public_projection_pre_push_gate_lib.py` does not yet
exist.

## Required First Reads

Read startup surfaces, guard orientation, this work order, the paired
GC-018 Amendment 2 baseline (including its Preimage Authority Matrix,
Worker Preflight Requirements, Required Semantic Delta, Refactor Contract,
and Forbidden Scope sections), the Amendment 2 source verification, the
current worker return, the Amendment 1 baseline/work order/source
verification, and the applicable checker sources before editing.

## Pre-Flight Checks

Require Core `HEAD` equal to the `executionBaseHead` the orchestrator
supplies at dispatch (a value distinct from `dispatchBaseHead`; see
Authority Commit Choreography). Require the Core working-tree dirty set to
be exactly the five paths in the paired baseline's Preimage Authority
Matrix, each hashing to its pinned SHA-256, with zero staged content and
no additional dirty path; any mismatch is `BLOCKED_PREIMAGE_MISMATCH`.
Require `governance/compat/public_projection_pre_push_gate_lib.py` to not
yet exist. Require the committed registry to contain the two exactly seeded
entries at 1380 and 1279 with this baseline as `seedAuthorization`. Require
public clone clean at exact commit `021f8b852`, branch
`lpci1-ref-staging`, correct remote, and zero staging. Run the
pre-implementation autorun gate before material edits.

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
sandbox setup and teardown. The worker must additionally run its own
pre-implementation resolver query and record the result before editing.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: extend the same isolated
public-projection implementation surface under `governance/compat/` that
T1 and Amendment 1 already authorized, by relocating cohesive non-CLI
logic out of the existing runner into exactly one new, equally isolated
library helper file. Do not change generic checkers, hook catalogs, or
existing guard semantics. Do not introduce any protected path outside this
named set. The two registry exceptions exist only to admit the
already-proven untracked preimages into the governed commit flow; they
authorize no growth and no semantic weakening.

Protected paths:

- `governance/compat/run_public_projection_pre_push_gate.py`
- `governance/compat/public_projection_pre_push_gate_lib.py`
- `governance/compat/test_run_public_projection_pre_push_gate.py`
- `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json`

Operator authorization: dispatcher/Amendment-2-author role instruction and
disposition source for this batch.

Rollback boundary: revert exactly the seven Amendment 2 worker paths to
their pre-Amendment-2 (Amendment-1-accepted, five-path) state if rejected,
with the new helper removed and the two freshly seeded registry entries
removed as one authorized rollback; do not revert candidate commits
`492e11eab`, `021f8b852`, or any session-sync or prior Amendment authority
commit.

## Execution Instructions

Implement the structural extraction literally:

1. Do not modify the five existing implementation files' observable
   behavior in any way; only relocate cohesive non-CLI logic and adjust
   imports/call sites.
2. Create `governance/compat/public_projection_pre_push_gate_lib.py`
   containing, at minimum, the sandbox materialization and hash
   verification functions, the dependency physical-copy/isolation
   utilities (including the `next` full-copy exception and its
   `FULL_COPY_DEPENDENCY_ENTRIES` constant), the invariant capture/diff
   functions, the output-normalization and evidence-extraction functions
   (including `ANSI_ESCAPE_RE` and `_extract_observed_counts`), and the
   teardown support functions - disposition NOT_LITERAL_WITH_REASON: moved
   verbatim in logic (only module location and import statements change),
   not a byte-identical file move, since the extraction itself edits
   import lines and possibly a function's containing-module reference.
3. Update `governance/compat/run_public_projection_pre_push_gate.py` to
   import from the new helper and keep only: argument parsing, policy
   loading/top-level validation, orchestration (`run_gate` and its direct
   callees that are inherently CLI-orchestration, not reusable logic),
   report construction, human/JSON output, and exit-code mapping.
4. Preserve every public function/class name the test file currently
   imports from the runner module, either by keeping it in the runner or
   by re-exporting it from the runner if it moved to the helper, so
   `governance/compat/test_run_public_projection_pre_push_gate.py`
   requires no import-path changes beyond what a clean extraction
   naturally requires; if a test import path does need to change, update
   it precisely and re-verify every affected test still exercises the
   same behavior.
5. Both files individually must import cleanly with no circular
   dependency between the CLI runner and the helper.
6. Run every item in the paired baseline's Verification Contract before
   returning; do not claim `COMPLETE_PENDING_REVIEW` unless every item
   passes with fresh evidence from this exact refactor, including a
   real-candidate sandboxed run reproducing the exact same seven-command
   PASS set and exact same evidence counts Amendment 1 proved.
7. In `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json`,
   do not remove either exception and do not change `status`, `rationale`,
   `requiredFollowup`, `seedAuthorization`, `path`, or `fileClass`. After
   the structural refactor, ratchet only each `approvedMaxLines` downward
   to that file's exact final physical line count. Never raise either cap,
   and add no exception for the helper.

## Write Ownership

Two distinct write boundaries, carried forward from Amendment 1 and not
weakened: implementation-authoring writes (seven Core owner paths only,
apply_patch/local editor only); package-execution writes during the
worker's own required verification phase (disposable sandbox and its
temporary support directory only, never Core or the public clone). See
the paired baseline's Write Boundary section for the complete rule.

## Execution Plan

1. Pre-flight checks (Preimage Authority Matrix match; helper file
   absent; public clone clean).
2. ADIF resolver query.
3. Read the current runner and test file in full to identify cohesive
   non-CLI logic boundaries.
4. Create the new helper file with the relocated logic.
5. Update the runner to import from the helper and remove the relocated
   code.
6. Update the test file's imports only as strictly required by the
   extraction.
7. Ratchet only the two seeded registry `approvedMaxLines` values down to
   the runner's and test file's exact final physical line counts.
8. Run the full Verification Contract (eleven items, see the paired
   baseline).
9. Amend the existing worker return in place to record the Amendment 2
   continuation and its evidence.
10. Return exactly one terminal disposition.

## Work-Order Fulfillment Manifest

Seven paths: the five existing Amendment-1 owner paths (four amended, one
worker return amended), one new library helper file, and the size-exception
registry ratchet.

## Required Artifact Manifest

| Path | Action |
| --- | --- |
| `docs/reference/CVF_PUBLIC_PROJECTION_PRE_PUSH_PROFILE_STANDARD_2026-08-11.md` | amend only if the refactor changes any normatively-described behavior surface (expected: no change required) |
| `governance/compat/CVF_PUBLIC_PROJECTION_PRE_PUSH_POLICY.json` | amend only if the refactor changes any policy-facing field (expected: no change required) |
| `governance/compat/run_public_projection_pre_push_gate.py` | amend: reduce to <= 800 lines (target <= 780) |
| `governance/compat/public_projection_pre_push_gate_lib.py` | create: <= 900 lines (target <= 600) |
| `governance/compat/test_run_public_projection_pre_push_gate.py` | amend: reduce to <= 1200 lines (target <= 1150) if the extraction requires test-file changes; otherwise unchanged |
| `docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_WORKER_RETURN_2026-08-11.md` | amend in place: record Amendment 2 continuation and fresh verification evidence |
| `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json` | amend only `approvedMaxLines` on the two seeded entries, downward to exact final physical line counts; all other fields unchanged |

## Evidence Requirements

Fresh, this-refactor evidence for: line counts of both Python files after
extraction; 58+ passing focused tests; a no-circular-import proof; the
governed Python automation size gate result for both files; a real-candidate
sandboxed run reproducing the exact seven-command PASS set and exact
evidence counts; public clone before/after invariant match; sandbox/support
teardown proof; worker-return fast gate result; `git diff --check` result;
exact-seven manifest, exact registry-ratchet field diff, and staged-content-zero confirmation.

## Verification Commands

- `python -c "import governance.compat.run_public_projection_pre_push_gate"`
  and `python -c "import governance.compat.public_projection_pre_push_gate_lib"`
- `python -m pytest governance/compat/test_run_public_projection_pre_push_gate.py -q`
- `python governance/compat/check_python_automation_size.py` (or the
  applicable equivalent invocation covering both new/changed files)
- `git diff -- governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json`
- `python governance/compat/run_public_projection_pre_push_gate.py --public-root <public clone> --base 2103a38fda01ee827e9fc6c3be38a824fa5d54ad --head 021f8b852afc245a6383177dd69bf56caf488b02 --json`
- `python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_run_public_projection_pre_push_gate.py`
- `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast`
- `git diff --check`

## Acceptance Criteria

- `run_public_projection_pre_push_gate.py` <= 800 lines;
  `public_projection_pre_push_gate_lib.py` <= 900 lines;
  `test_run_public_projection_pre_push_gate.py` <= 1200 lines.
- Runner target <= 780; test target <= 1150; helper target <= 600 and
  hard maximum <= 900; no helper exception.
- Each seeded exception retains `status`, `rationale`, `requiredFollowup`,
  `seedAuthorization`, `path`, and `fileClass` unchanged, while only
  `approvedMaxLines` is ratcheted downward to the exact final physical
  line count.
- 58+ focused tests pass.
- No circular import.
- Real-candidate run: exit 0, `compliant: true`, zero gate failures, exact
  evidence reconciliation identical to Amendment 1's proof (Model Gateway
  30 files / 231 tests; cvf-web 15 files / 218 tests; Next build 121
  static pages).
- Public clone unchanged at `021f8b852afc245a6383177dd69bf56caf488b02`.
- No sandbox/support residue.
- Worker-return fast gate and reviewer-fast pass at the same rate
  Amendment 1 achieved (the pre-existing, disclosed `active session state
  compatibility` violation remains out of scope and does not block this
  amendment's own acceptance).
- `git diff --check` clean.
- Exact-seven manifest; staged content zero.

## Review Gate

Independent reviewer must inspect the extraction diff, confirm no
behavioral invariant regressed, rerun the focused tests and one
independent real-candidate sandboxed run, confirm the real public clone
showed zero deltas throughout, confirm the full proof envelope executed
unweakened with identical evidence counts to Amendment 1, and run
reviewer-fast plus committed-range pre-closure before acceptance.

## Closure Checklist

No open acceptance item; exact seven-path manifest; all tests/gates PASS; no
public mutation at any point; worker did not commit; reviewer owns
material commit; session sync is separate; push remains a later tranche.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for any required public edit, generic-gate
weakening, missing stable owner, secret/network need, a genuinely
irreconcilable size-vs-behavior requirement (with fresh evidence), a
circular import that cannot be resolved inside the seven-path scope, or
failure outside the exact owned scope.

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
| changedSetScope(phase) | exact seven worker-owned paths |
| traceScope(phase, actor) | local structural refactor and fresh proof only |
| commitOwner(phase) | reviewer/closer |
| crossBatchIsolation | public candidate and unrelated Core remain unchanged |
| nextMoveSurfaces | reviewer/session steward owned |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_AMENDMENT_2_COMPLETION_2026-08-12.md`

reviewerOwnedClosurePaths: exact seven worker paths, optional completion
review if needed, then separate session sync. The existing worker return
remains the single return artifact; no new worker-return file is
authorized by this amendment.

## Foundation Storage Layout Block

N/A with reason: this tranche relocates governance control-plane
implementation code within `governance/compat/`; it does not add
foundation runtime storage.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Public/simple CVF vocabulary |
| Chain map route | N/A with reason: no external knowledge intake |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | T1/Amendment-1/Amendment-2 standard, policy, runner, helper, tests, and worker return |
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
| INTERNAL_AGENT | local Python CLI, library helper, policy, and disposable sandbox | read-only public-root evaluation; sandbox-only mutation | JSON receipt and exit code | subprocess/Git/filesystem boundary bounded to sandbox | BUILD |
| EXTERNAL_AGENT_CLI_MCP | CLI may be invoked by an external worker only under the same explicit arguments | no MCP/provider authority | identical local receipt | CLI only; no MCP adapter | CONTRACT_ONLY |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher/Amendment-2 author |
| Provider or surface | private Core plus read-only public clone |
| Session or invocation | `public-projection-prepush-t1-amendment-2-dispatch-20260812` |
| Working directory | private Core root |
| Command or tool surface | local reads, Git inspection, apply_patch, governance gates |
| Target paths | exact four-path authority repair: paired Amendment 2 source verification, baseline, work order, and size-exception registry |
| Allowed scope source | dispatcher/Amendment-2-author role instruction and disposition source |
| Before status evidence | Core `HEAD` at `225b6a01ab4400244a5cf56e47f58d16ecc0fba6` with exact inherited five-path Amendment-1 dirty set present, zero staged, and the three Amendment 2 documents untracked; public clean at `021f8b852` |
| After status evidence | exact four-path authority repair pending orchestrator review; five Amendment-1 preimages and public clone untouched |
| Diff evidence | Core `git status --short` partitions into exactly three sets: (1) inherited five-path Amendment-1 implementation set, all untracked and unchanged; (2) exact four-path Amendment 2 authority repair (three untracked documents plus tracked registry); (3) unexpected paths: none |
| Approval boundary | local dispatch-authoring only |
| Claim boundary | no implementation, sandbox execution, push, deploy, provider/store, secret, or production action |
| Agent type | dispatcher/Amendment-2 author |
| Invocation ID | `public-projection-prepush-t1-amendment-2-dispatch-20260812` |
| Expected manifest | source verification, baseline, work order, size-exception registry |
| Actual changed set | source verification, baseline, work order, size-exception registry |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: three new authority files plus one tracked registry amendment; no deletion or rename |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: relocating cohesive non-CLI implementation
into a new library helper, with zero logic change, will bring both the
CLI runner and the test file under their applicable hard size thresholds
while reproducing an identical real-candidate proof envelope to Amendment
1's own independently reviewed result.

Evidence Comparison Requirement: compare the post-refactor real-candidate
run's evidence (exit code, `compliant`, gate failures, per-command
evidence counts) against the exact figures in this dispatch's Disposition
Source and against the current worker return's own recorded evidence.

Contradiction Handling Requirement: any before/after delta on the real
public clone, any evidence-count mismatch versus Amendment 1's proof, any
circular import, or any weakened command requires a Contradiction Or Gap
Disposition and a blocked return.

Claim Update Requirement: confirm, revise, narrow, or invalidate the
structural-extraction claim from fresh evidence.

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_CURRENT_SOURCE

priorVerificationArtifact: the current worker return's Amendment 1
evidence is predecessor authority, not substituted execution proof for
this refactor.

priorVerificationAnchor: public base `2103a38f` and candidate `021f8b852`.

freshRecomputeRequired: yes, all real-candidate proof envelope and
before/after invariant evidence, reproduced against the post-refactor
code.

unicodePathHandling: use resolved literal paths and UTF-8-safe readers.

extractedTextAuthority: repository bytes and command results only.

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | local structural-refactor implementation and read-only proof against the real public clone |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: worker has not executed yet |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source-backed dispatch packet |
| invocationBoundary | exact local owner paths; public clone read-only; sandbox strictly temporary and outside both repository roots |
| interceptionBoundary | no IDE, provider, browser, network, or remote mutation claim |
| claimLanguage | ready for no-commit implementation |
| forbiddenExpansion | generic gate weakening, public mutation, push, deploy, secrets, provider/store, production, command-category omission, registry mutation beyond the exact approvedMaxLines downward ratchet, threshold editing |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this work order authorizes local provenance gate maintainability
refactor only.

## No-Commit Statement

WORKER_MUST_NOT_COMMIT. The implementation worker leaves all seven owned
paths uncommitted and staged content at zero. Only the independent
reviewer/closer may create the later material commit. This dispatch author
also creates no commit; the exact four-path authority repair is returned
as `COMPLETE_PENDING_ORCHESTRATOR_REVIEW` for orchestrator review and
commit.

## Claim Boundary

This work order authorizes a maintainability-only structural refactor
(relocating cohesive non-CLI logic from the existing CLI runner into a new
library helper) to satisfy a source-verified closure-hook size guard. It
authorizes no semantic, functional, or evidentiary reopening of Amendment
1's independently proven result. It does not authorize commit, push,
deploy, Netlify or any provider/browser/store action, public clone
mutation, secret access, network installs, or any change to the generic
private pre-push catalog or size guard. Registry authority is limited to
the two freshly seeded entries and their later approvedMaxLines-only
downward ratchet.
