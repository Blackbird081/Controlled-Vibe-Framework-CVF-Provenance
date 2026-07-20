# CVF Agent Work Order Continuous Projection T2 Governed Review-Packet Drafting

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: CVF-CONTINUOUS-PROJECTION-T2

Dispatch base head: `0ea461553`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker return path: `docs/reviews/CVF_CONTINUOUS_PROJECTION_T2_WORKER_RETURN_2026-07-20.md`

## Dispatch Prompt Envelope

Role: delegated read-only implementation worker.

Canonical packet: this work order and its paired GC-018 baseline.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: capture the committed dispatch/session-sync HEAD and
require an initially clean worktree.

Current-time notes: T1 closed with reviewer repairs at implementation commit
`a394d635c`; the accepted drift receipt and the accepted mapper it wraps
already exist and must not be rewritten or given an apply mode in T2.

Reviewer finding notes: the original T2 packet falsely paired a dispatch-ready
status with still-parked implementation authority, disagreed on the route token,
and left draft persistence/schema/action mapping ambiguous. The reviewer
repaired all three. Read the paired baseline's Reviewer Finding Carry-Forward
and Frozen T2 Draft Output Contract before editing; do not reintroduce those
defects.

Do-not-misread notes: read-only review-packet drafting implementation only.
Do not edit the accepted drift receipt, the accepted mapper, the policy, the
existing tests, cvf-web, either repository root beyond the allowed new script
paths, roadmap, registry, or session. No apply, copy, real-root scan, commit,
push, or public action, and the generated draft packet must itself remain a
review-required, uncommitted draft.

Required first actions: read startup front doors, guard orientation, literal
gotchas, the paired baseline, roadmap, T1 completion review, T1 worker
return, the accepted drift receipt and its proof suite, and cited checkers.
Run the mandatory pre-implementation autorun gate before writing any of the
three worker outputs.

Return contract: leave the new read-only drafter script, its paired focused
proof suite, and the worker return uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-CONTINUOUS-PROJECTION-T2 --title "Continuous Projection Governed Review-Packet Drafting" --date 2026-07-20 --base 0ea461553 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | roles, verified sources, exact scope, roadmap trace, artifact/forbidden/proof manifests, reviewer closure conversion, and mutation boundary |
| checkerReadAheadConfirmation | dispatch-quality, handoff, worker-return, machine-closure, public-disposition, structural, and file-size checkers |
| docOnlyNewFields | `sourceFacts`, `affectedProjections`, `recommendedReviewerActions`, `publicProvenanceBoundary`, `evidence`, `draftStatus` |
| claimBoundary | dispatch authoring provenance only |

## Purpose

Implement a deterministic, read-only review-packet drafter that consumes an
accepted drift receipt (reused or fixture, never a fresh real-root scan) and
emits a governed stdout-only JSON draft review packet listing source facts, affected
projections, recommended reviewer actions, the public/provenance boundary,
and evidence. Success means: a new read-only drafter script plus a focused
proof suite exist under `scripts/`, the draft is deterministic across
repeated runs over the same receipt, the draft carries an explicit
review-required `draftStatus` and authorizes no decision, the drafter adds
no apply/copy mode and never commits or writes into any real root, and the
proof suite exercises the drafter against disposable fixtures and reused
accepted receipts only. The worker commits nothing; the reviewer/closer
  reviews. The operator's post-review instruction authorizes transfer of this
  repaired packet to that worker after dispatch/session-sync commit.

## 2. Authority Chain

- Operator instruction: 2026-07-20 instruction authorizing only T2 GC-018 and work-order authoring, with T2 implementation and all mutation/public/live lanes parked
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- Decision pack / review authority: `docs/reviews/CVF_CONTINUOUS_PROJECTION_T1_COMPLETION_REVIEW_2026-07-20.md`
- Roadmap: `docs/roadmaps/CVF_CONTINUOUS_PROJECTION_DRIFT_DETECTION_AND_REVIEW_PACKET_AUTOMATION_ROADMAP_2026-07-19.md`
- Roadmap design-control gate: roadmap Design Control Gate and Audience Projection Contract sections
- Spec / contract / machine-readable semantics: `scripts/get_cvf_projection_drift_receipt.ps1` receipt output schema
- GC-018 requirement: filed at `docs/baselines/CVF_GC018_CONTINUOUS_PROJECTION_T2_GOVERNED_REVIEW_PACKET_DRAFTING_2026-07-20.md`
- Active handoff: per `CVF_SESSION/ACTIVE_SESSION_STATE.json`

Authority boundary:

- This work order does not authorize work outside the cited authority chain.
- If any authority artifact conflicts with this work order, stop and
  reconcile before implementation.

## 3. Agent Roles

- Orchestrator / dispatcher: dispatcher role
- Implementer: designated worker after independent reviewer packet acceptance and session-sync dispatch
- Reviewer: independent reviewer/closer
- Operator approval recorded for: T2 packet authoring plus the reviewer-repaired exact three-output no-commit implementation transfer to Claude
- Additional operator approval required for: any apply/copy mode, real-root or public-sync mutation, provider/live proof, T3-T4, or scope expansion

## Scope / Target / Owner Boundary

Target: one bounded read-only review-packet drafting implementation
assignment. Owner boundary: the worker owns only the three Allowed output
paths; the accepted drift receipt, accepted mapper, policy, existing tests,
both repository roots beyond those paths, roadmap, registries, and session
files are read-only. The independent reviewer/closer owns closure conversion.

## 4. Scope

Allowed scope:

- create a new read-only review-packet drafter script under `scripts/`
- create a paired focused deterministic proof suite under `scripts/`
- create the paired worker return under `docs/reviews/`
- read the accepted drift receipt, accepted mapper, policy, existing tests, and roots read-only

Forbidden scope:

- editing `scripts/get_cvf_projection_drift_receipt.ps1`, `scripts/test_cvf_projection_drift_receipt.ps1`, `scripts/get_cvf_projection_map.ps1`, `scripts/cvf_projection_policy.json`, `scripts/test_get_cvf_projection_map.ps1`, `scripts/test_cvf_projection_three_root_proof.ps1`, or `scripts/cvf-public-sync.ps1`
- adding any apply, copy, or auto-approve mode to any script
- running the real-root three-root scan (that is T4-owned) or committing any drafted packet
- mutating the sibling public-sync clone, cvf-web, either repository root beyond the allowed new paths, the roadmap, registries, or session files
- commit, push, deployment, public-sync mutation, provider/live calls, or production action

Risk ceiling:

- R1

## ADIF Defect Registry Disclosure

Before filing this work order, the read-only ADIF defect resolver was
queried for this dispatch's own task class, role, and lifecycle phase.

Resolver query: taskClass=`continuous projection T2 governed review-packet drafting`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "continuous projection T2 governed review-packet drafting" --role dispatcher --lifecycle-phase pre-dispatch --json`

## 5. Required First Reads

Before filing GC-018 or editing files, read:

- `docs/baselines/CVF_GC018_CONTINUOUS_PROJECTION_T2_GOVERNED_REVIEW_PACKET_DRAFTING_2026-07-20.md` - the paired authorization and frozen source facts
- `docs/reviews/CVF_CONTINUOUS_PROJECTION_T1_COMPLETION_REVIEW_2026-07-20.md` - the T2 content requirements and parked boundaries
- `docs/roadmaps/CVF_CONTINUOUS_PROJECTION_DRIFT_DETECTION_AND_REVIEW_PACKET_AUTOMATION_ROADMAP_2026-07-19.md` - the T2 tranche spec and forbidden-automation list
- `scripts/get_cvf_projection_drift_receipt.ps1` - the accepted receipt whose output schema the drafter consumes and must not rewrite
- `scripts/test_cvf_projection_drift_receipt.ps1` - the disposable-fixture and reused-receipt discipline to mirror
- `scripts/get_cvf_projection_map.ps1` - the accepted mapper wrapped by the receipt; read-only reference for the source/target boundary
- `scripts/cvf_projection_policy.json` - the policy whose `autoApproveForbidden` invariant must be preserved

## 6. Pre-Flight Checks

Commands to run before implementation:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 0ea461553 --head HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base 0ea461553 --head HEAD --enforce
python governance/compat/check_adif_defect_registry_disclosure.py --base 0ea461553 --head HEAD --enforce
```

Expected results:

- dispatch packet review begins at HEAD `0ea461553`; the worker captures the
  final committed dispatch/session-sync HEAD as `executionBaseHead`, and the
  worktree is clean before worker edits
- both applicable autorun phase gates report COMPLIANT using their correct
  lifecycle anchors
- dispatch-quality and ADIF disclosure checks report zero violations

If a pre-flight check fails, stop and record the failed command and result.
The worker must not continue past a failed autorun phase gate.

Mandatory Gate-Failure Remediation Protocol:

- Allowed-scope failures are mandatory remediation. Complete the remediation
  and execute the failed gate again.
- Escalation is reserved for remediation that would exceed Allowed scope,
  change the claim boundary, release a `HOLD_*` prerequisite, change risk
  level, open public-sync, run live/provider proof, consume secrets/quota,
  touch forbidden paths, or perform destructive/irreversible actions.

Staging and checker-source rule:

- Before running `run_local_governance_hook_chain.py` or simulating
  pre-commit, stage the intended new file set with `git add <paths>` so
  staged-index checkers read the current artifact.
- If a checker appears to reject a file that is correct on disk, first verify
  whether the corrected file was staged.

## 6A. Source-Fidelity Pass

Before marking this work order ready for execution, the source facts it
depends on were verified.

Full rules are in:
`docs/reference/work_order_template/CVF_WORK_ORDER_SOURCE_VERIFICATION_ADDENDUM.md`

### Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| drift receipt emits a 16-surface rows array | EXISTS | `scripts/get_cvf_projection_drift_receipt.ps1` | receipt assembly, lines 663-680 | `rows` | drift receipt output schema | ACCEPT |
| drift receipt emits a tracked/ignored public split | EXISTS | `scripts/get_cvf_projection_drift_receipt.ps1` | receipt assembly, line 671 | `publicTargetState` | drift receipt output schema | ACCEPT |
| drift receipt emits a reconciled disposition summary | EXISTS | `scripts/get_cvf_projection_drift_receipt.ps1` | receipt assembly, lines 672-676 | `reconciliationMatch` | drift receipt output schema | ACCEPT |
| receipt schema version exists | VALUE_SET | `scripts/get_cvf_projection_drift_receipt.ps1` | receipt assembly, line 664 | `schemaVersion` | drift receipt output schema | ACCEPT |
| observed roots exist | EXISTS | `scripts/get_cvf_projection_drift_receipt.ps1` | receipt assembly, line 669 | `rootsObserved` | drift receipt output schema | ACCEPT |
| mapper receipt identity exists | EXISTS | `scripts/get_cvf_projection_drift_receipt.ps1` | receipt assembly, line 677 | `mapperReceiptId` | drift receipt output schema | ACCEPT |
| successful receipt has an errors array | EXISTS | `scripts/get_cvf_projection_drift_receipt.ps1` | receipt assembly, line 679 | `errors` | drift receipt output schema | ACCEPT |
| top-level receipt identity exists | EXISTS | `scripts/get_cvf_projection_drift_receipt.ps1` | final receipt assembly, lines 683-688 | `receiptId` | drift receipt output schema | ACCEPT |
| each row carries a reviewer note field | EXISTS | `scripts/get_cvf_projection_drift_receipt.ps1` | frozen contract rows, line 119 | `reviewerNote` | drift receipt row schema | ACCEPT |
| frozen contract owner exists | EXISTS | `scripts/get_cvf_projection_drift_receipt.ps1` | function, line 108 | `Get-FrozenT0ContractRows` | drift receipt frozen contract | ACCEPT |
| no-target-write confirmation string exists | LITERAL_INVARIANT | `scripts/get_cvf_projection_drift_receipt.ps1` | receipt assembly, line 678 | `noTargetWriteConfirmation` | drift receipt output schema | ACCEPT |
| automatic semantic approval is forbidden | VALUE_SET | `scripts/cvf_projection_policy.json` | semanticReviewBoundary, lines 138-141 | `autoApproveForbidden` | projection policy schema | ACCEPT |
| T1 receipt is deterministic and fail-closed | RUNTIME_BEHAVIOR | `docs/reviews/CVF_CONTINUOUS_PROJECTION_T1_COMPLETION_REVIEW_2026-07-20.md` | Independent Recomputed Evidence table | 53/53 fixture proof | T1 accepted implementation | ACCEPT |

## New Doc-Only Fields

| Proposed item | Kind | Existing runtime status | T2 disposition |
|---|---|---|---|
| top-level draft fields and five content groups in paired baseline | ordered JSON schema | does not exist before T2 | worker implements exactly as new T2 output |
| `recommendedAction` and `decisionAuthority` | action-row fields | does not exist before T2 | worker implements only the frozen mapping |
| `UNSUPPORTED_OR_INVALID_DRIFT_RECEIPT` | diagnostic code | does not exist before T2 | worker implements fail-closed validation code |
| `draftId` hash profile | deterministic output identity | does not exist before T2 | worker implements uppercase SHA-256 over fields 1-9 |

## Current Runtime Freshness Verification

The claim that no review-packet drafter script yet exists was checked:
`scripts/get_cvf_projection_drift_receipt.ps1` emits a drift receipt but does
not draft a governed review packet, and no packet-drafter script exists under
`scripts/`. Command: `rg -n --files scripts | rg -i "review.*packet|packet.*draft"`
returned no match. The worker must create a new file rather than editing the
accepted receipt.

## Evidence Reuse And Encoding Plan

verificationMode: REUSE_PRIOR_VERIFICATION

priorVerificationArtifact: `docs/reviews/CVF_CONTINUOUS_PROJECTION_T1_COMPLETION_REVIEW_2026-07-20.md`

priorVerificationAnchor: `a394d635c`

freshRecomputeRequired: NO

Reason: the T2 drafter consumes the accepted T1 drift receipt schema, whose
determinism, fail-closed behavior, and 16-surface fidelity were independently
recomputed and accepted in the T1 completion review at implementation commit
`a394d635c` (53/53 fixture proof). T2 reuses that accepted verification rather
than re-running the T1 receipt over the real-root state, which is T4-owned.
The T2 proof suite still independently exercises the new drafter against
disposable fixtures and reused fixture receipts.

## Negative Search And Collision Discipline

Every named source symbol and path in this work order was found and cited in
the Source Verification Block above; no unresolved source is claimed. The
worker consumes the accepted receipt's output schema fields (`rows`,
`publicTargetState`, `summary`, `reviewerNote`) rather than re-deriving them.
Search roots: `scripts/`, `docs/reviews/`. Command:
`rg -n "publicTargetState" scripts/get_cvf_projection_drift_receipt.ps1`
confirms the receipt field. No similarly named path was promoted without
source-owner confirmation.

## 6B. Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| list source facts | Roadmap-Set T2 Constraints; Section 8 | draft `sourceFacts` group | focused proof suite assertion | PASS |
| list affected projections | Section 8 | draft `affectedProjections` group | focused proof suite assertion | PASS |
| list recommended reviewer actions | Section 8 | draft `recommendedReviewerActions` group | focused proof suite assertion | PASS |
| state public/provenance boundary | Section 8 | draft `publicProvenanceBoundary` group | focused proof suite assertion | PASS |
| list evidence | Section 8 | draft `evidence` group | focused proof suite assertion | PASS |
| keep output a review-required uncommitted draft | Roadmap-Set T2 Constraints | draft `draftStatus` plus no-commit boundary | reviewer diff scan and draft-status assertion | PASS |
| no apply mode, no real-root run | Section 4 Forbidden scope | drafter emits a draft only | reviewer diff scan for apply/copy or real-root call | PASS |

## 6B.1 Frozen Drafter Interface And Output Schema

The paired baseline's Frozen T2 Draft Output Contract is binding. The worker
implements only this interface:

```text
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/get_cvf_projection_review_packet.ps1 -ReceiptPath <existing-fixture-or-reused-receipt.json>
```

Input is one existing UTF-8 JSON receipt file. Output is one ordered JSON object
on stdout only. The script must not expose `OutputPath`, apply, copy, commit,
public-sync, root-write, or auto-approve parameters. The only durable worker
outputs remain the three paths in the Required Artifact Manifest.

The top-level field order, constants, five content groups, affected-row filter,
five-token action mapping, fail-closed code, and `draftId` hash profile are
copied exactly from the paired baseline. The worker must test every supported
disposition, both excluded dispositions, and at least these negative cases:

- missing required top-level receipt field;
- missing required row field;
- row count other than 16 or nonempty receipt `errors`;
- `summary.reconciliationMatch` is not true;
- unknown `driftDisposition`;
- affected-projection/action cardinality mismatch;
- attempted output-path/apply/copy parameter;
- repeated identical input produces different bytes or `draftId`.

## 6C. Worker Autonomy / No-Question Rule

The worker proceeds without operator confirmation for non-destructive actions
inside this work order's Allowed scope: reading named files, running
`git status`/`git diff`/`git rev-parse`/hash checks and listed gates,
documentation format remediation, evidence-block completion, and repeated
guard execution after allowed-scope remediation.

Escalation is reserved for actions that would exceed Allowed scope, edit the
accepted receipt/mapper/policy/existing tests, add an apply/copy mode, run
the real-root scan, commit a draft, run live/provider proof, use
secrets/quota, public-sync, push/publish, change risk or claim boundary,
touch forbidden paths, or perform destructive action.

If a machine gate fails inside Allowed scope, complete the remediation and
execute the gate again. Routine gate remediation is not an operator-preference
checkpoint.

## 6D. Pending Artifact Evidence Finality

The worker leaves changed, staged, or untracked governed artifacts for
review; those artifacts must not claim `git status --short` is clean. They
must record the actual pending status. Pending artifacts must not cite
`--base HEAD~1 --head HEAD` or another committed-only range as proof for the
pending artifact itself.

## 6E. Self-Reported Gate Evidence Consistency

If the worker records governance gate results, those results must match the
current handoff state. If a required gate fails inside Allowed scope, repair
and rerun before handoff; if it cannot be repaired inside Allowed scope, set
status to `BLOCKED_WITH_REASON` and name the return action. Do not leave a
non-blocked artifact saying a required gate failed while asking the reviewer
to rerun or decide.

## 6E.1 Machine Closure Package

Machine check:

```powershell
python governance/compat/check_machine_closure_package.py --base 0ea461553 --head HEAD --enforce
```

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_CONTINUOUS_PROJECTION_T2_GOVERNED_REVIEW_PACKET_DRAFTING_2026-07-20.md` | closed-equivalent status set by the reviewer/closer; no stale residue | N/A with reason: reviewer/closer owns closure conversion |
| Completion or reviewer artifact | `docs/reviews/CVF_CONTINUOUS_PROJECTION_T2_COMPLETION_REVIEW_2026-07-20.md` | reviewer decision, changed-file evidence, claim boundary, gate evidence | N/A with reason: authored by independent reviewer/closer at closure |
| Roadmap state | `docs/roadmaps/CVF_CONTINUOUS_PROJECTION_DRIFT_DETECTION_AND_REVIEW_PACKET_AUTOMATION_ROADMAP_2026-07-19.md` | T2 tranche final status set by the reviewer/closer | N/A with reason: reviewer-owned closure edit |
| Registry JSON | N/A with reason: no corpus registry state changes | no registry mutation | N/A with reason |
| Registry Markdown | N/A with reason: no corpus registry state changes | no registry mutation | N/A with reason |
| External evidence digest | N/A with reason: repository-local roots and reused receipts only | no imported evidence bundle | N/A with reason |
| System loop interlock | N/A with reason: no interlock owner changed | no interlock mutation | N/A with reason |
| Session continuity | protected continuity surfaces | separate post-material session sync | N/A with reason: reviewer/closer owns session sync |

## 6G. Work-Order Fulfillment Manifest

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
|---|---|---|
| `scripts/get_cvf_projection_review_packet.ps1` | Yes | the new read-only review-packet drafter consuming an accepted drift receipt |
| `scripts/test_cvf_projection_review_packet.ps1` | Yes | the paired focused deterministic proof suite using disposable fixtures and reused receipts |
| `docs/reviews/CVF_CONTINUOUS_PROJECTION_T2_WORKER_RETURN_2026-07-20.md` | Yes | the no-commit worker return with evidence |

## Forbidden Path Manifest

| Path | Reason |
|---|---|
| `scripts/get_cvf_projection_drift_receipt.ps1` | accepted T1 receipt; read-only, must not be rewritten or given an apply mode |
| `scripts/get_cvf_projection_map.ps1` | accepted mapper; read-only reference |
| `scripts/cvf_projection_policy.json` | accepted policy; `autoApproveForbidden` invariant must be preserved |
| `scripts/test_cvf_projection_drift_receipt.ps1` | accepted T1 proof; read-only reference |
| `scripts/cvf-public-sync.ps1` | projection source-of-truth script; deny-patterned, read-only |

## Forbidden Filesystem State At Dispatch

| Forbidden path | Expected state | Actual state at dispatch | Action if PRESENT |
|---|---|---|---|
| `scripts/get_cvf_projection_review_packet.ps1` | ABSENT | ABSENT | N/A |
| `scripts/test_cvf_projection_review_packet.ps1` | ABSENT | ABSENT | N/A |
| `docs/reviews/CVF_CONTINUOUS_PROJECTION_T2_WORKER_RETURN_2026-07-20.md` | ABSENT | ABSENT | N/A |

Rules:

- `ABSENT` - path does not exist on disk. Dispatch is safe.
- `PRESENT` - path already exists. Dispatch is blocked until the orchestrator
  removes the files, opens a governance packet for them, or records an
  explicit operator exemption with reason.

## Required Proof Manifest

| Proof | Path | Required literal | Required at handoff |
|---|---|---|---|
| deterministic draft across repeated runs | `scripts/test_cvf_projection_review_packet.ps1` | `deterministic_repeated_run_draft` | Yes |
| draft is review-required and authorizes no decision | `scripts/test_cvf_projection_review_packet.ps1` | `draftStatus` | Yes |
| five content groups present | `scripts/test_cvf_projection_review_packet.ps1` | `recommendedReviewerActions` | Yes |
| no apply/copy mode in drafter source | `scripts/test_cvf_projection_review_packet.ps1` | `no_apply_copy_mode_in_source` | Yes |

## 7. Write Ownership

Owned files or modules:

- `scripts/get_cvf_projection_review_packet.ps1`
- `scripts/test_cvf_projection_review_packet.ps1`
- `docs/reviews/CVF_CONTINUOUS_PROJECTION_T2_WORKER_RETURN_2026-07-20.md`

Forbidden paths:

- `scripts/get_cvf_projection_drift_receipt.ps1`
- `scripts/get_cvf_projection_map.ps1`
- `scripts/cvf_projection_policy.json`
- `scripts/test_cvf_projection_drift_receipt.ps1`
- `scripts/cvf-public-sync.ps1`

Write mode:

- create-only

Any file outside ownership requires an updated work order or operator
approval. If the closure diff shows files outside Allowed scope or ownership,
the worker must stop, split the cleanup into a separate governed batch, or
return to the Orchestrator.

## 8. Execution Plan

1. Capture preflight evidence (HEAD, clean worktree, both autorun gates) as
   the first step; stop condition: any preflight failure returns
   `BLOCKED_WITH_REASON`.
2. Author `scripts/get_cvf_projection_review_packet.ps1` as a read-only
   drafter that accepts an already-produced drift receipt from required
   `-ReceiptPath` and emits one stdout-only ordered JSON draft with exactly five content groups
   (`sourceFacts`, `affectedProjections`, `recommendedReviewerActions`,
   `publicProvenanceBoundary`, `evidence`), plus an explicit review-required
   `draftStatus` and a claim that the draft authorizes no reviewer decision;
   it must implement the paired baseline's exact disposition-to-action mapping,
   must not re-run the real-root scan, must not add an output/apply/copy mode,
   and must perform no filesystem write; stop condition: any need to add an
   apply/copy mode or run the real-root scan returns `BLOCKED_WITH_REASON`.
3. Author `scripts/test_cvf_projection_review_packet.ps1` using disposable
   temp fixtures and reused accepted receipts only, asserting determinism,
   the review-required draft status, the five content groups, and the
   supported/excluded/unknown dispositions, invalid receipt shapes, and the
   absence of any output-path/apply/copy parameter in the drafter; stop condition:
   any assertion that would require the real-root scan returns
   `BLOCKED_WITH_REASON`.
4. Run the focused proof suite and record pass counts; stop condition: a
   non-deterministic draft returns `BLOCKED_WITH_REASON`.
5. Author the worker return, record exact diff, empty staged set, and
   unchanged HEAD, run the worker-return fast gate and file-size gate; stop
   condition: any forbidden-path change returns `BLOCKED_WITH_REASON`.
6. Return `COMPLETE_PENDING_REVIEW` without commit.

## 8A. Design Control Carry-Forward

| Design control | Roadmap source | Work-order handling | Verdict |
|---|---|---|---|
| Scope boundary | roadmap Scope section | read-only drafter only; no apply mode | PASS |
| Non-goals | roadmap Non-Goals section | no auto content rewrite, no real-root scan, no committed draft | PASS |
| Lane split | roadmap Work Plan T2 | this work order executes T2 only; T3-T4 parked | PASS |
| Dependency/source-verification plan | Section 6A | all source facts verified before dispatch | PASS |
| Claim boundary | roadmap Claim Boundary | read-only; draft authorizes no decision | PASS |
| Acceptance criteria | Section 10 | observable draft and proof rows below | PASS |
| Verification/evidence | Evidence Requirements section | commands and focused tests required | PASS |
| Dispatch-readiness decision | T1 completion review Next Allowed Move | T2 packet authoring released; implementation parked | PASS |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | private provenance workspace |
| Session or invocation | CVF-CONTINUOUS-PROJECTION-T2 dispatch, 2026-07-20 |
| Working directory | repository root |
| Command or tool surface | source reads, ADIF resolver, autorun gates, apply_patch |
| Target paths | paired baseline; this work order |
| Allowed scope source | operator continuation instruction and T1 completion review Next Allowed Move |
| Before status evidence | clean worktree at HEAD `0ea461553` |
| After status evidence | reviewer-repaired two-artifact packet accepted for exact no-commit implementation transfer after dispatch/session-sync commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | T2 packet authoring only; implementation parked |
| Claim boundary | repo-local trace only; no implementation, root mutation, public action, or provider call |
| Agent type | dispatcher |
| Invocation ID | `continuous-projection-t2-dispatch-2026-07-20` |
| Expected manifest | paired baseline; this work order |
| Actual changed set | paired baseline; this work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## 8C. Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: a read-only drafter can consume the accepted
drift receipt's output schema and emit a deterministic, review-required draft
packet with the five roadmap-required content groups, without any apply mode
and without re-running the real-root scan.

Evidence Comparison Requirement: the worker return compares the actual draft
output and proof counts against this prediction.

Contradiction Handling Requirement: if a deterministic review-required draft
cannot be built read-only from an accepted receipt, the worker records a
Contradiction Or Gap Disposition and returns `BLOCKED_WITH_REASON` rather
than weakening the review-required or read-only boundary.

Claim Update Requirement: the worker return records whether the read-only
draft claim was confirmed, revised, narrowed, or invalidated.

## Evidence Requirements

Required evidence:

- `git rev-parse --short HEAD` before edits
- both autorun phase gate results
- focused proof suite pass counts with deterministic repeated-run proof
- the five content groups and the review-required `draftStatus` in the draft output
- exact `git diff --name-status`, empty staged set, unchanged HEAD
- complete Agent Operation Trace Block in the worker return

Base-anchor evidence:

- `dispatchBaseHead`: `0ea461553`
- `executionBaseHead`: worker captures final dispatch/session-sync HEAD
- `closureBaseHead`: `N/A - pending review`
- Commit mode: `WORKER_MUST_NOT_COMMIT`
- Worker-return fast gate: `python governance/compat/run_worker_return_fast_gate.py`
- Committed-range `pre-closure`: `N/A - pending review`

## 10. Acceptance Criteria

- [ ] A new read-only review-packet drafter script exists under `scripts/` and adds no apply/copy mode.
- [ ] A paired focused proof suite exists and passes deterministically on disposable fixtures and reused receipts.
- [ ] The draft lists source facts, affected projections, recommended reviewer actions, public/provenance boundary, and evidence.
- [ ] The draft carries an explicit review-required `draftStatus` and states it authorizes no reviewer decision.
- [ ] The drafter never re-runs the real-root scan and never writes into any real root.
- [ ] The draft is deterministic across repeated runs over the same receipt.
- [ ] No forbidden path changed; nothing staged or committed by the worker.

Fail conditions:

- [ ] Any apply, copy, or auto-approve mode is added to any script.
- [ ] Any forbidden path is modified, the real-root scan is run, or any draft is committed.
- [ ] The draft omits any of the five required content groups or the review-required status.
- [ ] Any commit, push, public-sync, provider/live, or production claim appears.

Closure is blocked if any fail condition is present.

## 11. Review Gate

Implementation may proceed only after:

- this GC-018 is accepted by the independent reviewer, the fresh operator implementation authorization is recorded in the paired baseline, and the reviewer dispatch/session-sync commits land
- `pre-dispatch` autorun gate passed before dispatch
- `pre-implementation` autorun gate passed before material edits

Closure may proceed only after:

- independent reviewer/closer no-blocking objection or operator waiver
- `pre-closure` autorun gate passed and result recorded

For `WORKER_MUST_NOT_COMMIT` mode, worker handoff is not closure. The
independent reviewer or the committer must approve disposition, commit the
reviewed owned diff, and run the committed-range `pre-closure` gate before
changing status to a closed-equivalent value.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | repository-local read-only review-packet drafting over an accepted drift receipt |
| scope classification | read-only script and focused-proof implementation; no apply mode, no real-root scan |
| risk sensitivity | R1; new read-only script plus disposable-fixture proof |
| escalation condition | source contradiction, missing authority, need for an apply/copy mode or real-root scan, or forbidden mutation need |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | no-commit implementation worker -> independent reviewer/closer |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher -> no-commit implementation worker -> independent reviewer/closer |
| phase | EXECUTION |
| baseHeadFor(phase) | dispatchBaseHead=`0ea461553`; executionBaseHead=worker captures final dispatch/session-sync HEAD; closureBaseHead=reviewer sets |
| changedSetScope(phase) | exactly three worker outputs: new drafter script, new proof suite, worker return |
| traceScope(phase, actor) | base, source reads, receipt consumption, draft content groups, draft status, determinism, commands, diff, staged state, and no-commit evidence |
| commitOwner(phase) | independent reviewer/closer; worker forbidden |
| crossBatchIsolation | initially clean provenance worktree required; foreign changes block execution |
| nextMoveSurfaces | reviewer/session-sync steward only |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_CONTINUOUS_PROJECTION_T2_COMPLETION_REVIEW_2026-07-20.md` |
| reviewerOwnedClosurePaths | paired baseline, this work order, roadmap, completion review, and session sync |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_CONTINUOUS_PROJECTION_T2_WORKER_RETURN_2026-07-20.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/test_cvf_projection_review_packet.ps1
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_governed_file_size.py --enforce
git diff --name-status
git diff --cached --name-status
git status --short
```

## 12. Closure Checklist

- [ ] All acceptance criteria satisfied or explicitly marked N/A with reason
- [ ] Required focused tests run with pass counts recorded
- [ ] Autorun `pre-closure` gate passed once the reviewer commit lands
- [ ] Commit mode recorded as `WORKER_MUST_NOT_COMMIT`
- [ ] `dispatchBaseHead` and `executionBaseHead` recorded without treating a stale anchor as current worker proof
- [ ] For `WORKER_MUST_NOT_COMMIT`, pending handoff used a non-closed status and recorded actual `git status --short`
- [ ] Worker-return fast gate result recorded with focused pytest/proof targets
- [ ] Agent Operation Trace Block present and complete
- [ ] Closure gate used a non-empty committed diff range, not a single-commit self-range
- [ ] Changed-file set is inside Allowed scope
- [ ] Roadmap-to-work-order trace matrix final statuses are PASS or N/A with reason
- [ ] No open checkbox residue remains after closure
- [ ] Public catalog updated or explicitly N/A with reason
- [ ] GC-020 handoff updated with current HEAD after commit
- [ ] Active session front door and state registry updated if state changed

## 13. Return-To-Orchestrator Conditions

Return to orchestrator without continuing if:

- pre-flight fails;
- any autorun phase gate fails outside Allowed scope;
- source-fidelity pass finds a missing path, invented symbol, or unverified mapping;
- a deterministic review-required draft cannot be built read-only from an accepted receipt;
- an apply/copy mode or the real-root scan would be required;
- scope conflict is discovered;
- public/provenance boundary is unclear.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | Status; Dispatch Prompt Envelope; Purpose; Scope / Target / Owner Boundary; Source Verification Block; Intake Role Routing Decision; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Worker Return Packet Shape Contract; Evidence Requirements; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirm this work order's dispatch shape, required sections, and source citations before dispatch |
| claimBoundary | checker compliance confirms packet structure only; the T2 tranche remains parked pending independent review and fresh operator implementation authorization |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | read-only review-packet drafting over an accepted drift receipt |
| claimDisposition | N/A with reason: no execution-control implementation is claimed by this dispatch |
| receiptEvidence | N/A with reason: the worker produces a read-only draft packet, not a runtime governance receipt |
| actionEvidence | N/A with reason: source and targets remain read-only |
| invocationBoundary | governed local document/code editing under WORKER_MUST_NOT_COMMIT, no broader claim |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | implement, draft, and prove read-only review-packet behavior only |
| forbiddenExpansion | no apply/copy mode, real-root scan, committed draft, real-root mutation, commit, push, deploy, public-sync mutation, provider/live, or production |

## Operator Checkpoint

Released after reviewer dispatch/session-sync commit: exactly the three-output
T2 no-commit implementation assignment to Claude. Parked: T3-T4, the real-root
receipt run, and all mutation/public/provider/live/push/deployment/production
lanes. Any deviation from the paired baseline's frozen stdout-only schema or
write boundary returns to the reviewer.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T2 is a private provenance read-only implementation tranche and
creates no public-safe export; the drafted review packet itself is a
private, review-required draft, and the sibling public-sync clone is not
mutated.

## Claim Boundary

This reviewer-repaired work order authorizes a bounded read-only review-packet
drafting implementation under `WORKER_MUST_NOT_COMMIT`, to be executed by
Claude after dispatch/session-sync commit and reviewed by the
independent reviewer. It does not authorize apply/copy modes, the real-root
scan, a committed draft, real-root mutation, semantic decisions, commit,
push, deployment, public-sync mutation, provider/live calls, production
action, or unattended mutation. Implementation itself remains parked until
the independent reviewer accepts this packet and the operator records a fresh
implementation authorization.
