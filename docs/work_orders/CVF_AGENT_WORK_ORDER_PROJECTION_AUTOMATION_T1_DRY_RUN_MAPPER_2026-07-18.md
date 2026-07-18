# CVF Agent Work Order Projection Automation T1 Dry-Run Mapper

Memory class: governed-worker-dispatch

Status: CLOSED_PASS_BOUNDED

Batch ID: CVF-PROJECTION-AUTO-T1

Dispatch base head: `20ba27996`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker return path: `docs/reviews/CVF_PROJECTION_AUTOMATION_T1_WORKER_RETURN_2026-07-18.md`

## Dispatch Prompt Envelope

Role: delegated implementation worker.

Canonical packet: this work order.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: must equal the committed T1 dispatch/session-sync HEAD named
by the dispatcher prompt.

Current-time notes: T0 closed at `38ec816f9`; registry-evidence erratum committed
at `20ba27996`; T2 is held.

Do-not-misread notes: dry-run mapper only. Receipt output is the sole permitted
mapper write. No apply, copy, target mutation, stage, commit, push, provider, or
cvf-web repair.

Required first actions: read startup front doors, guard orientation, literal
gotchas, paired baseline, this work order, T0 closure/erratum, and cited sources.

Return contract: leave all six outputs uncommitted and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Operator Checkpoint

N/A with reason: standing authorization covers this local dry-run tranche; T2
and every external or public action remain held.

## Purpose

Implement and prove a portable, deterministic, fail-closed projection mapper
that reports how private provenance would map to public-sync and how cvf-web
registry/dependency seams compare, without changing any target surface.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-PROJECTION-AUTO-T1 --title "Projection Automation Dry-Run Mapper" --date 2026-07-18 --base 20ba27996 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | populated exact source contract, six-path scope, tests, receipts, and fail conditions |
| checkerReadAheadConfirmation | dispatch-quality, handoff, worker-return, structural, receipt, and public-disposition checkers |
| docOnlyNewFields | mapper/receipt fields are declared in the paired baseline and implemented only in this tranche |
| claimBoundary | dispatch authoring provenance only |

## Authority Chain

Operator standing continuation -> automation roadmap -> accepted T0 closure and
erratum -> paired T1 baseline -> this packet -> no-commit worker -> independent
reviewer/closer.

## Agent Roles

Dispatcher owns the packet. Worker owns exactly six outputs. Independent
reviewer/closer owns acceptance, material commit, T2 release, and session sync.

## Required First Reads

Read the paired baseline, accepted T0 ledger/review, `scripts/cvf-public-sync.ps1`,
`scripts/update_cvf_workspace_public_core.ps1`, cvf-web runtime registry and
package manifest, applicable checker sources, and PowerShell AST documentation
available locally through the installed runtime. Do not use external material
as source authority.

## Pre-Flight Checks

Confirm exact executionBaseHead, clean worktree, both git roots and their distinct
origins, all cited source paths, six-path ownership, and pre-implementation
autorun PASS before editing. A foreign dirty worktree blocks execution.

## Write Ownership

Worker may create or modify exactly these six paths:

1. `scripts/cvf_projection_policy.json`
2. `scripts/get_cvf_projection_map.ps1`
3. `scripts/test_get_cvf_projection_map.ps1`
4. `docs/reference/CVF_PROJECTION_MAPPING_RECEIPT_SCHEMA_2026-07-18.md`
5. `docs/reviews/CVF_PROJECTION_AUTOMATION_T1_DRY_RUN_RECEIPT_2026-07-18.json`
6. `docs/reviews/CVF_PROJECTION_AUTOMATION_T1_WORKER_RETURN_2026-07-18.md`

Every other path is read-only.

## Forbidden Scope

Forbidden: editing or invoking `scripts/cvf-public-sync.ps1`; dot-sourcing it;
editing workspace updater, cvf-web, registries, generated aggregates, session
surfaces, hooks/checkers, dependency manifests, public-sync clone files, or any
other path; adding apply/copy switches; staging, committing, pushing, provider
calls, network calls, deployment, production action, or secrets in output.

## Dependency Release Evidence

| Dependency | Artifact | Commit | Final disposition |
|---|---|---|---|
| T0 closure | `docs/reviews/CVF_PROJECTION_AUTOMATION_T0_COMPLETION_REVIEW_2026-07-18.md` | `38ec816f9` | REVIEWER_ACCEPTED_BOUNDED |
| T0 erratum | corrected T0 ledger and completion review | `20ba27996` | PASS |

## Source Verification Block

Use and directly reconfirm every ACCEPT row in the paired T1 baseline. If a
named current symbol/path is absent or contradictory, stop with
`BLOCKED_WITH_REASON`; do not invent a replacement contract. New T1 fields are
owned by the paired baseline's New Doc-Only Fields section and are not existing
runtime claims.

## Required Implementation

### Policy manifest

Create stable JSON containing schema version, expected provenance/public remotes,
allowlist trees/root files/script files/workspace templates/docs paths, mapped
exports, deny patterns, action enums, and semantic-review boundary. Values must
match current `cvf-public-sync.ps1` exactly where that script owns them.

### Dry-run mapper

Create an advanced PowerShell script with help and parameters for
`ProvenanceRoot`, `PublicSyncRoot`, `CvfWebRoot`, `PolicyPath`, and optional
`ReceiptOutputPath`. It must canonicalize and validate roots, verify distinct
origin remotes, reject dirty provenance/public-sync roots, and run path-
containment checks for every candidate destination and receipt output.

It must inspect only. Candidate actions are:

- `COPY_CANDIDATE_ABSENT_TARGET` for allowlisted source files absent at target;
- `FLAG_SEMANTIC_REVIEW_CHANGED` for allowlisted files with byte differences;
- `SKIP_UNCHANGED` for byte-identical mappings;
- `SKIP_DENIED` for deny matches;
- `SKIP_NOT_ALLOWLISTED` for other source files.

Mapped exports must use their declared destination. Output ordering must be
ordinal and stable. `receiptId` must be derived from canonical semantic content,
not timestamp, random value, machine path, or volatile HEAD. No timestamp may
participate in deterministic equality.

The cvf-web observation must compare package dependencies and registry entries,
report the three current SOT3 entries as present, and flag inconsistencies for
semantic review only. It must never edit registry source.

If `ReceiptOutputPath` is omitted, write JSON to stdout only. If present, it is
the one allowed script write after containment validation; create no other file.

### Focused tests

Create one self-contained PowerShell test runner using temporary disposable git
repositories/fixtures. It must not touch the real public-sync clone. Cover at
least:

1. help/parameter contract;
2. policy parity by parsing current sync-script assignments without executing or
   dot-sourcing that script;
3. missing provenance root;
4. missing public root;
5. wrong provenance remote;
6. wrong public remote;
7. dirty provenance root;
8. dirty public root;
9. candidate destination path escape;
10. receipt output path escape;
11. absent-target candidate;
12. changed-content semantic-review flag;
13. unchanged skip;
14. mapped export destination;
15. deny and not-allowlisted dispositions;
16. all three current SOT3 registry entries observed;
17. two identical runs produce byte-identical JSON and receipt ID;
18. no target filesystem or git-status change before/after successful mapping;
19. secret-like fixture value is not emitted.

The test runner must clean its own temp area in `finally` and return nonzero on
any failed assertion.

### Receipt schema and evidence

Document field types, enums, canonical ordering, hashing input, count
reconciliation, failure envelope, secret boundary, and no-target-write claim.
Generate the governed T1 JSON receipt from a deterministic disposable fixture,
not from a dirty real worktree. The receipt must state fixture roots without
operator-specific absolute paths.

## Acceptance Criteria

- All paired baseline AC-01 through AC-07 pass.
- Focused test matrix has at least 19 named passing cases and zero failure.
- Policy parity covers every source-owned group and mapped field.
- Test receipt validates against documented schema and count reconciliation.
- `git diff --name-status` plus status show exactly six allowed paths, nothing
  staged, and unchanged HEAD.
- No target/public-sync/cvf-web mutation, provider call, commit, or push occurs.

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Work-order implementation | Evidence |
|---|---|---|
| mapper and manifest/schema | policy JSON, mapper, receipt schema | exact paths 1, 2, 4 |
| focused tests and CLI help | PowerShell test matrix and comment-based help | exact path 3 |
| deterministic dry-run | canonical ordering/hash and repeated-run test | test receipt and worker return |
| fail-closed negatives | missing/wrong/dirty/escape cases | named tests 3-10 |
| no semantic auto-approval | changed files and Web gaps flag review | action enum assertions |
| no mutation/commit/push | read-only implementation and before/after evidence | test 18 and git evidence |

## Work-Order Fulfillment Manifest

| Required artifact | Required proof literal |
|---|---|
| `scripts/cvf_projection_policy.json` | `schemaVersion` and all policy groups |
| `scripts/get_cvf_projection_map.ps1` | `COPY_CANDIDATE_ABSENT_TARGET` and `FLAG_SEMANTIC_REVIEW_CHANGED` |
| `scripts/test_get_cvf_projection_map.ps1` | at least 19 named cases and final PASS count |
| receipt schema reference | deterministic hashing and no-target-write boundary |
| governed JSON receipt | reconciled counts and stable receipt ID |
| worker return | `COMPLETE_PENDING_REVIEW`, commands, exact changed set, no-commit statement |

Forbidden paths: every path outside the six-path Write Ownership list.

## Required Artifact Manifest

| Artifact | Required disposition | Final evidence |
|---|---|---|
| policy JSON | present and source-parity checked | PASS |
| mapper script | present, dry-run-only, fail closed | PASS |
| focused test script | present with reviewer-expanded matrix | PASS_48_OF_48 |
| receipt schema | present and aligned to accepted output | PASS |
| governed receipt | schema 1.0.0, all parity MATCH, zero errors | PASS |
| worker return | accepted with reviewer repair addendum | PASS |

## Evidence Requirements

Record test names/counts, parity results, before/after fixture hashes/status,
receipt reconciliation, script help, exact changed set, staged state, unchanged
HEAD, and all governed gates. Do not print environment values or secrets.

## Execution Plan

1. Reconfirm source and clean-base conditions.
2. Implement policy manifest and read-only mapper.
3. Implement disposable-fixture test matrix and receipt schema.
4. Run the full focused suite twice for deterministic evidence.
5. Generate the governed fixture receipt, reconcile the six-path diff, run all
   required gates, and author the worker return.

## Review Gate

Independent reviewer recomputes policy parity, reruns all 19 or more focused
cases, validates receipt canonicalization/counts, compares target status before
and after, inspects the exact six-path set, and runs reviewer-fast before any
acceptance or material commit.

## Closure Checklist

- [x] T0 closure and erratum commits are source-backed.
- [x] T1 scope is exactly six paths.
- [x] T1 has no apply, copy, commit, push, provider, or Web repair authority.
- [x] T2 remains dependency-held.

## Return-To-Orchestrator Conditions

Return only after all allowed-scope defects are repaired and required gates
pass, or with one source-backed Stop Condition that cannot be resolved inside
the six owned paths without violating Forbidden Scope.

## Stop Conditions

Return `BLOCKED_WITH_REASON` before out-of-scope mutation if current source
contradicts an ACCEPT row, policy parity cannot be obtained without executing
the mutating sync flow, root/remote safety cannot fail closed, deterministic
receipt requires volatile data, or completion would require a forbidden path.

## Worker Autonomy / No-Question Rule

Independently remediate implementation, test, format, and gate defects within
the six allowed paths. Stop only on a listed genuine blocker.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | operator-authorized implementation of the accepted T0 mapper contract |
| scope classification | repository-local source/tool implementation with disposable fixtures |
| risk sensitivity | R2; local read-only tool with explicit receipt output only |
| escalation condition | current-source contradiction or forbidden-path requirement |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | no-commit implementation worker to independent reviewer/closer |

## Dual Agent Surface Matrix

| Surface | Interface | Authority/risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | local PowerShell CLI | local read-only mapping and explicit receipt output | focused tests and receipt | filesystem/git command adapter | ACCEPT |
| EXTERNAL_AGENT_CLI_MCP | documented local CLI invocation | no MCP/provider/remote authority | help text and schema | same CLI; no external adapter | DEFER_WITH_REASON |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher -> no-commit implementation worker -> independent reviewer/closer |
| phase | EXECUTION |
| baseHeadFor(phase) | dispatchBaseHead=`20ba27996`; executionBaseHead=committed dispatch/session-sync HEAD from prompt; closureBaseHead=reviewer sets |
| changedSetScope(phase) | exactly six Write Ownership paths |
| traceScope(phase, actor) | base, source reconfirmation, tests, receipt, commands, diff, no-commit evidence |
| commitOwner(phase) | reviewer/closer; worker forbidden |
| crossBatchIsolation | clean worktree required; foreign changes block execution |
| nextMoveSurfaces | reviewer/session-sync steward only |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_PROJECTION_AUTOMATION_T1_COMPLETION_REVIEW_2026-07-18.md` |
| reviewerOwnedClosurePaths | six worker outputs, baseline, work order, roadmap, completion review, later session sync |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_PROJECTION_AUTOMATION_T1_WORKER_RETURN_2026-07-18.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`projection automation implementation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "projection automation implementation" --role dispatcher --lifecycle-phase pre-dispatch --json`

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Public/simple CVF vocabulary |
| Chain map route | source-verify local vocabulary -> mapper/test evidence -> independent review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired T1 baseline and this work order |
| Disposition | QUESTION_OR_HYPOTHESIS until source-verified; T1 uses only verified local source |
| Claim boundary | local source and disposable fixtures only |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | one flat `scripts/` policy JSON, mapper, and focused test plus one governed reference schema |
| Storage decision | keep the local operator tool beside existing public-sync/workspace scripts; no new package or runtime service |
| Existing aggregate impact | none |
| Generated state impact | none during T1 |
| Durable governance boundary | read-only local CLI and schema; no runtime memory, MCP, provider, Web, or public target authority |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Dispatch Prompt Envelope; Source Verification Block; Required Implementation; Roadmap-to-Work-Order Trace Matrix; Work-Order Fulfillment Manifest; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Worker Return Packet Shape Contract; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirmation and evidence for T1 dispatch quality, not first discovery |
| claimBoundary | dry-run-only mapper implementation dispatch |

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/test_cvf_projection_map.ps1
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_governed_file_size.py --enforce
git diff --name-status
git diff --cached --name-status
git status --short
```

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | private provenance workspace |
| Session or invocation | projection automation T1 dispatch, 2026-07-18 |
| Working directory | repository root |
| Command or tool surface | source reads, apply_patch, ADIF resolver, governed gates |
| Target paths | roadmap, paired T1 baseline, this work order |
| Allowed scope source | operator standing continuation and accepted T0 completion review |
| Before status evidence | clean worktree at HEAD `20ba27996` |
| After status evidence | three-path dispatch packet pending material commit |
| Diff evidence | git diff/status and eventual committed diff |
| Approval boundary | T1 dry-run mapper dispatch only |
| Claim boundary | no implementation, target mutation, provider, public push, or production action by dispatcher |
| Agent type | dispatcher |
| Invocation ID | `projection-automation-t1-dispatch-2026-07-18` |
| Expected manifest | roadmap, T1 baseline, T1 work order |
| Actual changed set | same three paths |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | deterministic dry-run projection mapping |
| claimDisposition | CLAIM_REJECTED_PENDING_EVIDENCE until worker tests and independent review |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT until the governed fixture receipt exists |
| actionEvidence | CLAIM_REJECTED_NO_ACTION because T1 permits classification only |
| invocationBoundary | local PowerShell process and disposable fixtures |
| interceptionBoundary | no IDE, provider, wrapper, MCP, or runtime interception |
| claimLanguage | inspect, validate, classify, and emit receipt |
| forbiddenExpansion | apply, copy, target mutation, registry repair, commit, push, provider/live, production |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | paired T1 GC-018 | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | this work order | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | T1 completion review | `Status: REVIEWER_ACCEPTED_BOUNDED` | PASS |
| Worker return | T1 worker return | `Status: ACCEPTED_BY_REVIEWER` | PASS |
| Roadmap state | automation roadmap | `Status: T1_PASS_BOUNDED_T2_PACKET_AUTHORING_NEXT` | PASS |
| Registry JSON | existing GC-051 coverage | aggregate drift checked | PASS |
| Registry Markdown | existing registry front door | no new family required | PASS |
| External evidence digest | repository-local evidence only | none | N/A with reason |
| System loop interlock | no loop owner changed | none | N/A with reason |
| Session continuity | protected session surfaces | separate sync | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| deterministic equality | two identical fixture runs byte-identical | reviewer rerun PASS | PASS |
| target mutation | zero before/after delta | focused status/filesystem tests PASS | PASS |
| negative cases | missing, wrong remote, dirty, escape, and parity fail closed | reviewer-expanded suite PASS | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this packet authorizes private local tooling only, with no public-sync
mutation or GitHub push.

## Commit Prompt Readiness

Worker must not stage or commit. Reviewer/closer may commit only after exact
scope reconciliation, focused tests, worker-fast/reviewer-fast, receipt review,
file-size compliance, and closure diff PASS.

## Claim Boundary

This work order authorizes exactly six T1 outputs and a dry-run-only mapper. It
does not authorize target writes beyond the explicit receipt, apply/copy,
cvf-web repair, public-sync mutation, commit, push, provider/live calls, network
access, deployment, production use, or public availability claims.
