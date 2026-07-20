# CVF Agent Work Order Continuous Projection T1 Read-Only Drift Receipt

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: CVF-CONTINUOUS-PROJECTION-T1

Dispatch base head: `c8f7bb9e7`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker return path: `docs/reviews/CVF_CONTINUOUS_PROJECTION_T1_WORKER_RETURN_2026-07-20.md`

## Dispatch Prompt Envelope

Role: delegated read-only implementation worker.

Canonical packet: this work order and its paired GC-018 baseline.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: capture the committed dispatch/session-sync HEAD and
require an initially clean worktree.

Current-time notes: T0 closed bounded at `d1cb8cba9` with a frozen 16-row
terminal contract; the accepted mapper already exists and must not be
rewritten or given an apply mode in T1.

Do-not-misread notes: read-only drift-receipt implementation only. Do not
edit the accepted mapper, the policy, the existing tests, cvf-web, either
repository root beyond the allowed new script paths, roadmap, registry, or
session. No apply, copy, real-root mutation, commit, push, or public action.

Required first actions: read startup front doors, guard orientation, literal
gotchas, the paired baseline, roadmap, T0 completion review, T0 ledger,
mapper, policy, both existing proof suites, and cited checkers. Run the
mandatory pre-implementation autorun gate before writing any of the three
worker outputs.

Return contract: leave the new read-only receipt script, its paired focused
proof suite, and the worker return uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-CONTINUOUS-PROJECTION-T1 --title "Continuous Projection Read-Only Drift Receipt" --date 2026-07-20 --base c8f7bb9e7 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | roles, verified sources, exact scope, roadmap trace, artifact/forbidden/proof manifests, reviewer closure conversion, and mutation boundary |
| checkerReadAheadConfirmation | dispatch-quality, handoff, worker-return, machine-closure, public-disposition, structural, and file-size checkers |
| docOnlyNewFields | `driftDisposition`, `semanticOwner`, `projectionTarget`, `evidenceClass`, `audience`, `reviewerNote`, and proposed codes `RECEIPT_TIMEOUT_INCONCLUSIVE`, `AUDIENCE_EVIDENCE_MISSING` |
| claimBoundary | dispatch authoring provenance only |

## Purpose

Implement a deterministic, read-only drift receipt that consumes the
T0-accepted 16-row three-root contract and the accepted mapper's read-only
observations, and emits a byte-stable JSON receipt classifying every mapped
surface by `driftDisposition` without any apply, copy, or auto-approve path.
Success means: a new read-only receipt script plus a focused proof suite
exist under `scripts/`, the receipt is deterministic across repeated runs,
the six target-only root files are classified `SOURCE_AUTHORITY_BLOCKED`,
tracked-versus-ignored public state is reported as distinct fields, the
recursive scan is time-bounded with explicit `RECEIPT_TIMEOUT_INCONCLUSIVE`
semantics, and no root is mutated. The worker commits nothing; the reviewer/closer reviews.

## 2. Authority Chain

- Operator instruction: 2026-07-20 instruction assigning independent packet review followed by designated worker execution
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- Decision pack / review authority: `docs/reviews/CVF_CONTINUOUS_PROJECTION_T0_COMPLETION_REVIEW_2026-07-20.md`
- Roadmap: `docs/roadmaps/CVF_CONTINUOUS_PROJECTION_DRIFT_DETECTION_AND_REVIEW_PACKET_AUTOMATION_ROADMAP_2026-07-19.md`
- Roadmap design-control gate: roadmap Design Control Gate and Audience Projection Contract sections
- Spec / contract / machine-readable semantics: `docs/reviews/CVF_CONTINUOUS_PROJECTION_T0_THREE_ROOT_DRIFT_CONTRACT_LEDGER_2026-07-20.md`
- GC-018 requirement: filed at `docs/baselines/CVF_GC018_CONTINUOUS_PROJECTION_T1_READ_ONLY_DRIFT_RECEIPT_2026-07-20.md`
- Active handoff: per `CVF_SESSION/ACTIVE_SESSION_STATE.json`

Authority boundary:

- This work order does not authorize work outside the cited authority chain.
- If any authority artifact conflicts with this work order, stop and
  reconcile before implementation.

## 3. Agent Roles

- Orchestrator / dispatcher: dispatcher role
- Implementer: designated worker after independent reviewer packet acceptance and session-sync dispatch
- Reviewer: independent reviewer/closer
- Operator approval recorded for: designated worker execution after independent reviewer packet acceptance, limited to the three Allowed paths
- Additional operator approval required for: any apply/copy mode, real-root or public-sync mutation, provider/live proof, or scope expansion

## Scope / Target / Owner Boundary

Target: one bounded read-only drift-receipt implementation assignment. Owner
boundary: the worker owns only the three Allowed output paths; the accepted
mapper, policy, existing tests, both repository roots beyond those paths,
roadmap, registries, and session files are read-only. the independent reviewer/closer owns closure conversion.

## 4. Scope

Allowed scope:

- create a new read-only drift-receipt script under `scripts/`
- create a paired focused deterministic proof suite under `scripts/`
- create the paired worker return under `docs/reviews/`
- read the accepted mapper, policy, existing tests, T0 ledger, and roots read-only

Forbidden scope:

- editing `scripts/get_cvf_projection_map.ps1`, `scripts/cvf_projection_policy.json`, `scripts/test_get_cvf_projection_map.ps1`, `scripts/test_cvf_projection_three_root_proof.ps1`, or `scripts/cvf-public-sync.ps1`
- adding any apply, copy, or auto-approve mode to any script
- mutating the sibling public-sync clone, cvf-web, either repository root beyond the allowed new paths, the roadmap, registries, or session files
- commit, push, deployment, public-sync mutation, provider/live calls, or production action

Risk ceiling:

- R1

## ADIF Defect Registry Disclosure

Before filing this work order, the read-only ADIF defect resolver was
queried for this dispatch's own task class, role, and lifecycle phase.

Resolver query: taskClass=`continuous projection T1 read-only drift receipt implementation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "continuous projection T1 read-only drift receipt implementation" --role dispatcher --lifecycle-phase pre-dispatch --json`

## 5. Required First Reads

Before filing GC-018 or editing files, read:

- `docs/baselines/CVF_GC018_CONTINUOUS_PROJECTION_T1_READ_ONLY_DRIFT_RECEIPT_2026-07-20.md` - the paired authorization and frozen source facts
- `docs/reviews/CVF_CONTINUOUS_PROJECTION_T0_COMPLETION_REVIEW_2026-07-20.md` - the three reviewer-set T1 conditions
- `docs/reviews/CVF_CONTINUOUS_PROJECTION_T0_THREE_ROOT_DRIFT_CONTRACT_LEDGER_2026-07-20.md` - the frozen 16-row terminal contract and proposed T1 schema
- `docs/roadmaps/CVF_CONTINUOUS_PROJECTION_DRIFT_DETECTION_AND_REVIEW_PACKET_AUTOMATION_ROADMAP_2026-07-19.md` - T1 tranche spec and forbidden-automation list
- `scripts/get_cvf_projection_map.ps1` - the accepted read-only mapper the receipt consumes and must not rewrite
- `scripts/cvf_projection_policy.json` - the policy whose `autoApproveForbidden` invariant must be preserved
- `scripts/test_get_cvf_projection_map.ps1` - the negative-case and determinism proof pattern to mirror
- `scripts/test_cvf_projection_three_root_proof.ps1` - the disposable-fixture discipline to mirror

## 6. Pre-Flight Checks

Commands to run before implementation:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base c8f7bb9e7 --head HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base c8f7bb9e7 --head HEAD --enforce
python governance/compat/check_adif_defect_registry_disclosure.py --base c8f7bb9e7 --head HEAD --enforce
```

Expected results:

- dispatch packet review begins at HEAD `c8f7bb9e7`; the worker captures the
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
| mapper accepts three roots plus optional receipt path | EXISTS | `scripts/get_cvf_projection_map.ps1` | parameter block, lines 65-80 | `ReceiptOutputPath` | mapper parameter contract | ACCEPT |
| candidate actions are classification labels only | LITERAL_INVARIANT | `scripts/get_cvf_projection_map.ps1` | description, lines 21-28 | `FLAG_SEMANTIC_REVIEW_CHANGED` | mapper action vocabulary | ACCEPT |
| policy parity read model exists | EXISTS | `scripts/get_cvf_projection_map.ps1` | function, lines 249-328 | `Get-PolicyParityReport` | mapper policy parity read model | ACCEPT |
| cvf-web observation read model exists | EXISTS | `scripts/get_cvf_projection_map.ps1` | function, lines 330-376 | `Get-CvfWebObservation` | mapper Web observation read model | ACCEPT |
| deterministic receipt id and reconciliation exist | EXISTS | `scripts/get_cvf_projection_map.ps1` | receipt assembly, lines 558-576 | `reconciliationMatch` | mapper receipt schema | ACCEPT |
| no-target-write confirmation string exists | LITERAL_INVARIANT | `scripts/get_cvf_projection_map.ps1` | receipt assembly, line 571 | `noTargetWriteConfirmation` | mapper receipt schema | ACCEPT |
| automatic semantic approval is forbidden | VALUE_SET | `scripts/cvf_projection_policy.json` | semanticReviewBoundary, lines 138-141 | `autoApproveForbidden` | projection policy schema | ACCEPT |
| deterministic and negative proof seams exist | EXISTS | `scripts/test_get_cvf_projection_map.ps1` | assertions, lines 292, 309, 318, 441 | `provenance_remote_substring_spoof_rejected` | focused mapper proof suite | ACCEPT |
| frozen T0 terminal contract exists | EXISTS | `docs/reviews/CVF_CONTINUOUS_PROJECTION_T0_THREE_ROOT_DRIFT_CONTRACT_LEDGER_2026-07-20.md` | Findings / Position terminal rows | Terminal Contract Rows | T0 accepted drift contract | ACCEPT |

## Current Runtime Freshness Verification

The claim that no read-only drift-receipt script yet exists was checked:
`scripts/get_cvf_projection_map.ps1` is the only projection mapper and emits
a projection-map receipt, not a drift receipt over the T0 contract; no
drift-receipt script exists under `scripts/`. Command:
`rg -n --files scripts | rg -i "drift.*receipt"` returned no match. The
worker must create a new file rather than editing the accepted mapper.

## T1 Receipt Contract And Input Seam

The worker must not parse the governed Markdown ledger at runtime. The new
script must define a source-local, immutable `Get-FrozenT0ContractRows` array
that transcribes the accepted 16 terminal surfaces and their five contract
dimensions. The proof suite must assert exactly these ordinally sorted surface
ids so a missing, duplicated, or invented row fails:

1. `mapped:AGENTS.md`
2. `mapped:public-core-continuation`
3. `mapped:scripts/install_cvf_workspace_root_wrappers.ps1`
4. `allowedRootFiles:byte-identical-eight`
5. `allowedRootFiles:target-only-six`
6. `denied:docs/baselines`
7. `denied:docs/reviews`
8. `denied:docs/roadmaps`
9. `denied:root-agent-handoffs`
10. `allowedTrees`
11. `allowedDocsPaths`
12. `denyPatterns`
13. `cvfWeb:sot3-parity`
14. `policy:sync-parity`
15. `manual:technical-product-catalog`
16. `presentation:README`

The script invokes the accepted mapper read-only as a child process using the
same explicit provenance, public-sync, cvf-web, and policy inputs. It consumes
the mapper JSON output; it must not duplicate or weaken mapper root validation,
remote validation, dirty-root refusal, allow/deny classification, hash
comparison, or policy-parity behavior. A nonzero mapper exit is propagated as
a nonzero T1 result with its structured error code preserved.

Successful receipt JSON must implement the T0 Proposed T1 Read-Only Receipt
Schema exactly and add this T1 object:

```text
driftReceipt.publicTargetState.trackedDeniedPaths[]  : sorted relative paths
driftReceipt.publicTargetState.trackedDeniedCount    : integer
driftReceipt.publicTargetState.ignoredResiduePaths[] : sorted relative paths
driftReceipt.publicTargetState.ignoredResidueCount   : integer
```

Paths are repository-relative and secret-free; absolute workstation paths are
forbidden. Arrays use ordinal sorting. `generatedAtLogical` is the stable
contract revision `T0-2026-07-20`, not wall-clock time. `receiptId` is SHA-256
over compressed canonical JSON excluding `receiptId`, as in the accepted
mapper. The six target-only files remain one frozen
`allowedRootFiles:target-only-six` row with `SOURCE_AUTHORITY_BLOCKED`; target
presence or target hashing must never upgrade that row to `CURRENT`.

Timeout semantics are fail-closed: `ScanTimeoutSeconds` is an integer
parameter with default `60` and accepted range `1..3600`. If the mapper child
does not complete within the bound, terminate only that child process, emit a
structured stdout error whose first code is
`RECEIPT_TIMEOUT_INCONCLUSIVE`, exit nonzero, emit no success receipt rows,
and write no receipt file. A timeout is never a partial success and never
defaults any row to `CURRENT`. The focused suite must exercise this path
deterministically without scanning either real repository root.

## Negative Search And Collision Discipline

Every named source symbol and path in this work order was found and cited in
the Source Verification Block above; no unresolved source is claimed. The
worker's own build reuses the T0 ledger's already-verified six target-only
file finding for the `SOURCE_AUTHORITY_BLOCKED` classification rather than
re-deriving it. Search roots: `scripts/`, `docs/reviews/`. Command:
`rg -n "SOURCE_AUTHORITY_BLOCKED" docs/reviews/CVF_CONTINUOUS_PROJECTION_T0_THREE_ROOT_DRIFT_CONTRACT_LEDGER_2026-07-20.md`
confirms the six-file finding. No similarly named path was promoted without
source-owner confirmation.

## 6B. Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| extend the accepted mapper with deterministic receipts | T1 Receipt Contract And Input Seam; Section 8 Execution Plan | child-process consumption of accepted mapper JSON plus new read-only receipt script | worker byte-identical repeated-run proof | PASS |
| classify changed owner, missing target, stale target, audience-presentation risk | Section 4 Scope; Section 8 | receipt `driftDisposition` per row | focused proof suite assertions | PASS |
| provide manual, CI, and scheduled invocation seams | Section 8 | receipt script invocation documentation | worker return seam description plus fixture proof | PASS |
| no apply mode is allowed | Section 4 Forbidden scope | receipt script emits classification only | reviewer diff scan for any copy/apply call | PASS |
| separate tracked public drift from ignored residue | Reviewer-Set T1 Conditions | distinct tracked/ignored receipt fields | reviewer `git ls-files`/`git check-ignore` recomputation | PASS |
| classify the six target-only root files | Reviewer-Set T1 Conditions | `SOURCE_AUTHORITY_BLOCKED` rows | reviewer row audit against T0 ledger | PASS |
| resolve bounded timeout semantics | Reviewer-Set T1 Conditions | `RECEIPT_TIMEOUT_INCONCLUSIVE` behavior | focused proof suite timeout case | PASS |

## 6C. Worker Autonomy / No-Question Rule

The worker proceeds without operator confirmation for non-destructive actions
inside this work order's Allowed scope: reading named files, running
`git status`/`git diff`/`git rev-parse`/hash checks and listed gates,
documentation format remediation, evidence-block completion, and repeated
guard execution after allowed-scope remediation.

Escalation is reserved for actions that would exceed Allowed scope, edit the
accepted mapper/policy/existing tests, add an apply/copy mode, run
live/provider proof, use secrets/quota, public-sync, push/publish, change
risk or claim boundary, touch forbidden paths, or perform destructive action.

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
python governance/compat/check_machine_closure_package.py --base c8f7bb9e7 --head HEAD --enforce
```

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_CONTINUOUS_PROJECTION_T1_READ_ONLY_DRIFT_RECEIPT_2026-07-20.md` | closed-equivalent status set by the reviewer/closer; no stale residue | N/A with reason: reviewer/closer owns closure conversion |
| Completion or reviewer artifact | `docs/reviews/CVF_CONTINUOUS_PROJECTION_T1_COMPLETION_REVIEW_2026-07-20.md` | reviewer decision, changed-file evidence, claim boundary, gate evidence | N/A with reason: authored by independent reviewer/closer at closure |
| Roadmap state | `docs/roadmaps/CVF_CONTINUOUS_PROJECTION_DRIFT_DETECTION_AND_REVIEW_PACKET_AUTOMATION_ROADMAP_2026-07-19.md` | T1 tranche final status set by the reviewer/closer | N/A with reason: reviewer-owned closure edit |
| Registry JSON | N/A with reason: no corpus registry state changes | no registry mutation | N/A with reason |
| Registry Markdown | N/A with reason: no corpus registry state changes | no registry mutation | N/A with reason |
| External evidence digest | N/A with reason: repository-local roots only | no imported evidence bundle | N/A with reason |
| System loop interlock | N/A with reason: no interlock owner changed | no interlock mutation | N/A with reason |
| Session continuity | protected continuity surfaces | separate post-material session sync | N/A with reason: reviewer/closer owns session sync |

## 6G. Work-Order Fulfillment Manifest

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
|---|---|---|
| `scripts/get_cvf_projection_drift_receipt.ps1` | Yes | the new read-only drift-receipt script consuming the accepted mapper observations |
| `scripts/test_cvf_projection_drift_receipt.ps1` | Yes | the paired focused deterministic proof suite using disposable fixtures |
| `docs/reviews/CVF_CONTINUOUS_PROJECTION_T1_WORKER_RETURN_2026-07-20.md` | Yes | the no-commit worker return with evidence |

## Forbidden Path Manifest

| Path | Reason |
|---|---|
| `scripts/get_cvf_projection_map.ps1` | accepted mapper; read-only, must not be rewritten or given an apply mode |
| `scripts/cvf_projection_policy.json` | accepted policy; `autoApproveForbidden` invariant must be preserved |
| `scripts/test_get_cvf_projection_map.ps1` | accepted focused proof; read-only reference |
| `scripts/test_cvf_projection_three_root_proof.ps1` | accepted three-root proof; read-only reference |
| `scripts/cvf-public-sync.ps1` | projection source-of-truth script; deny-patterned, read-only |

## Forbidden Filesystem State At Dispatch

| Forbidden path | Expected state | Actual state at dispatch | Action if PRESENT |
|---|---|---|---|
| `scripts/get_cvf_projection_drift_receipt.ps1` | ABSENT | ABSENT | N/A |
| `scripts/test_cvf_projection_drift_receipt.ps1` | ABSENT | ABSENT | N/A |
| `docs/reviews/CVF_CONTINUOUS_PROJECTION_T1_WORKER_RETURN_2026-07-20.md` | ABSENT | ABSENT | N/A |

Rules:

- `ABSENT` - path does not exist on disk. Dispatch is safe.
- `PRESENT` - path already exists. Dispatch is blocked until the orchestrator
  removes the files, opens a governance packet for them, or records an
  explicit operator exemption with reason.

## Required Proof Manifest

| Proof | Path | Required literal | Required at handoff |
|---|---|---|---|
| deterministic receipt id across repeated runs | `scripts/test_cvf_projection_drift_receipt.ps1` | `deterministic_repeated_run_receipt_id` | Yes |
| dirty-root fail-closed inheritance | `scripts/test_cvf_projection_drift_receipt.ps1` | `DIRTY_PROVENANCE_ROOT` | Yes |
| no-target-write confirmation | `scripts/get_cvf_projection_drift_receipt.ps1` | `noTargetWriteConfirmation` | Yes |
| six target-only files blocked | `scripts/test_cvf_projection_drift_receipt.ps1` | `SOURCE_AUTHORITY_BLOCKED` | Yes |

## 7. Write Ownership

Owned files or modules:

- `scripts/get_cvf_projection_drift_receipt.ps1`
- `scripts/test_cvf_projection_drift_receipt.ps1`
- `docs/reviews/CVF_CONTINUOUS_PROJECTION_T1_WORKER_RETURN_2026-07-20.md`

Forbidden paths:

- `scripts/get_cvf_projection_map.ps1`
- `scripts/cvf_projection_policy.json`
- `scripts/test_get_cvf_projection_map.ps1`
- `scripts/test_cvf_projection_three_root_proof.ps1`
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
2. Author `scripts/get_cvf_projection_drift_receipt.ps1` as a read-only wrapper
   that invokes the accepted mapper child process, preserves its
   `MISSING_*`/`WRONG_*_REMOTE`/`DIRTY_*_ROOT` failures verbatim, bounds the
   child process with the exact fail-closed timeout contract above,
   classifies each surface by `driftDisposition`, classifies the six
   target-only root files `SOURCE_AUTHORITY_BLOCKED`, reports tracked-versus-
   ignored public counts as distinct fields, and emits a deterministic JSON
   receipt with a `noTargetWriteConfirmation` string; stop condition: any need
   to add an apply/copy mode returns `BLOCKED_WITH_REASON`.
3. Author `scripts/test_cvf_projection_drift_receipt.ps1` using disposable
   temp fixtures only (never the real public-sync remote), asserting
   determinism, dirty-root refusal, the six-file block, tracked/ignored
   separation, and timeout semantics; stop condition: any assertion that would
   require touching a real root returns `BLOCKED_WITH_REASON`.
4. Run the focused proof suite and record pass counts; stop condition: a
   non-deterministic receipt returns `BLOCKED_WITH_REASON`.
5. Author the worker return, record exact diff, empty staged set, and
   unchanged HEAD, run the worker-return fast gate and file-size gate; stop
   condition: any forbidden-path change returns `BLOCKED_WITH_REASON`.
6. Return `COMPLETE_PENDING_REVIEW` without commit.

## 8A. Design Control Carry-Forward

| Design control | Roadmap source | Work-order handling | Verdict |
|---|---|---|---|
| Scope boundary | roadmap Scope section | read-only receipt only; no apply mode | PASS |
| Non-goals | roadmap Non-Goals section | no auto content rewrite, no real-root apply | PASS |
| Lane split | roadmap Work Plan T1 | this work order executes T1 only; T2-T4 parked | PASS |
| Dependency/source-verification plan | Section 6A | all source facts verified before dispatch | PASS |
| Claim boundary | roadmap Claim Boundary | read-only; no implementation-authorizing claim | PASS |
| Acceptance criteria | Section 10 | observable receipt and proof rows below | PASS |
| Verification/evidence | Section 9 | commands and focused tests required | PASS |
| Dispatch-readiness decision | T0 completion review Next Allowed Move | T1 packet authoring released; implementation parked | PASS |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | private provenance workspace |
| Session or invocation | CVF-CONTINUOUS-PROJECTION-T1 dispatch, 2026-07-20 |
| Working directory | repository root |
| Command or tool surface | source reads, ADIF resolver, autorun gates, apply_patch |
| Target paths | paired baseline; this work order |
| Allowed scope source | operator continuation instruction and T0 completion review Next Allowed Move |
| Before status evidence | clean worktree at HEAD `c8f7bb9e7` |
| After status evidence | two untracked dispatch artifacts pending commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | T1 packet authoring only; implementation parked |
| Claim boundary | repo-local trace only; no implementation, root mutation, public action, or provider call |
| Agent type | dispatcher |
| Invocation ID | `continuous-projection-t1-dispatch-2026-07-20` |
| Expected manifest | paired baseline; this work order |
| Actual changed set | paired baseline; this work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## 8C. Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: a read-only drift receipt can be built on the
accepted mapper's observations and the frozen T0 contract without any apply
mode, and it can classify the six target-only files and separate tracked from
ignored public state deterministically.

Evidence Comparison Requirement: the worker return compares the actual
receipt output and proof counts against this prediction.

Contradiction Handling Requirement: if a deterministic read-only receipt
cannot be built within the bounded time budget, the worker records a
Contradiction Or Gap Disposition and returns `BLOCKED_WITH_REASON` rather than
weakening the fail-closed boundary.

Claim Update Requirement: the worker return records whether the read-only
receipt claim was confirmed, revised, narrowed, or invalidated.

## Evidence Requirements

Required evidence:

- `git rev-parse --short HEAD` before edits
- both autorun phase gate results
- focused proof suite pass counts with byte-identical repeated-run proof
- tracked-versus-ignored counts and six-file `SOURCE_AUTHORITY_BLOCKED` classification
- exact `git diff --name-status`, empty staged set, unchanged HEAD
- complete Agent Operation Trace Block in the worker return

Base-anchor evidence:

- `dispatchBaseHead`: `c8f7bb9e7`
- `executionBaseHead`: worker captures final dispatch/session-sync HEAD
- `closureBaseHead`: `N/A - pending review`
- Commit mode: `WORKER_MUST_NOT_COMMIT`
- Worker-return fast gate: `python governance/compat/run_worker_return_fast_gate.py`
- Committed-range `pre-closure`: `N/A - pending review`

## 10. Acceptance Criteria

- [ ] A new read-only drift-receipt script exists under `scripts/` and adds no apply/copy mode.
- [ ] A paired focused proof suite exists and passes deterministically on disposable fixtures.
- [ ] The receipt classifies the six target-only root files `SOURCE_AUTHORITY_BLOCKED`.
- [ ] The receipt reports tracked and ignored public counts as distinct fields.
- [ ] The recursive scan is time-bounded with explicit `RECEIPT_TIMEOUT_INCONCLUSIVE` semantics.
- [ ] The receipt is byte-identical across repeated runs with a stable receipt id.
- [ ] No forbidden path changed; nothing staged or committed by the worker.

Fail conditions:

- [ ] Any apply, copy, or auto-approve mode is added to any script.
- [ ] Any forbidden path is modified, or any real root is mutated.
- [ ] The receipt defaults the six target-only files to `CURRENT` or conflates tracked with ignored state.
- [ ] Any commit, push, public-sync, provider/live, or production claim appears.

Closure is blocked if any fail condition is present.

## 11. Review Gate

Implementation may proceed only after:

- this GC-018 is accepted by the independent reviewer and the operator's
  2026-07-20 designated-worker authorization is recorded in the paired baseline
- `pre-dispatch` autorun gate passed before dispatch
- `pre-implementation` autorun gate passed before material edits

Closure may proceed only after:

- independent reviewer/closer no-blocking objection or operator waiver
- `pre-closure` autorun gate passed and result recorded

For `WORKER_MUST_NOT_COMMIT` mode, worker handoff is not closure. the independent reviewer or the
committer must approve disposition, commit the reviewed owned diff, and run
the committed-range `pre-closure` gate before changing status to a
closed-equivalent value.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | repository-local read-only drift-receipt implementation over the frozen T0 contract |
| scope classification | read-only script and focused-proof implementation; no apply mode |
| risk sensitivity | R1; new read-only script plus disposable-fixture proof |
| escalation condition | source contradiction, missing authority, need for an apply/copy mode, unsafe dirty root, or forbidden mutation need |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | no-commit implementation worker -> independent reviewer/closer |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher -> no-commit implementation worker -> independent reviewer/closer |
| phase | EXECUTION |
| baseHeadFor(phase) | dispatchBaseHead=`c8f7bb9e7`; executionBaseHead=worker captures final dispatch/session-sync HEAD; closureBaseHead=reviewer sets |
| changedSetScope(phase) | exactly three worker outputs: new receipt script, new proof suite, worker return |
| traceScope(phase, actor) | base, source reads, root observations, receipt determinism, tracked/ignored counts, six-file classification, timeout semantics, commands, diff, staged state, and no-commit evidence |
| commitOwner(phase) | independent reviewer/closer; worker forbidden |
| crossBatchIsolation | initially clean provenance worktree required; foreign changes block execution |
| nextMoveSurfaces | reviewer/session-sync steward only |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_CONTINUOUS_PROJECTION_T1_COMPLETION_REVIEW_2026-07-20.md` |
| reviewerOwnedClosurePaths | paired baseline, this work order, roadmap, completion review, and session sync |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_CONTINUOUS_PROJECTION_T1_WORKER_RETURN_2026-07-20.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/test_cvf_projection_drift_receipt.ps1
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
- the receipt cannot be built read-only within the bounded time budget;
- an apply/copy mode would be required;
- scope conflict is discovered;
- public/provenance boundary is unclear.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | Status; Dispatch Prompt Envelope; Purpose; Scope / Target / Owner Boundary; Source Verification Block; Intake Role Routing Decision; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Worker Return Packet Shape Contract; Evidence Requirements; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirm this work order's dispatch shape, required sections, and source citations before dispatch |
| claimBoundary | checker compliance confirms packet structure only; worker execution begins only after independent reviewer commit and session-sync dispatch |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | read-only drift-receipt implementation over the frozen T0 contract |
| claimDisposition | N/A with reason: no execution-control implementation is claimed by this dispatch |
| receiptEvidence | N/A with reason: the worker produces a read-only drift receipt, not a runtime governance receipt |
| actionEvidence | N/A with reason: source and targets remain read-only |
| invocationBoundary | governed local document/code editing under WORKER_MUST_NOT_COMMIT, no broader claim |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | implement, classify, and prove read-only receipt behavior only |
| forbiddenExpansion | no apply/copy mode, real-root mutation, commit, push, deploy, public-sync mutation, provider/live, or production |

## Operator Checkpoint

SATISFIED_FOR_BOUNDED_WORKER_AFTER_REVIEW: the operator's 2026-07-20
instruction assigns the designated worker step after independent review. T1
implementation remains parked until the reviewer commits this packet and the
session sync records the final `executionBaseHead`. All mutation and expansion
lanes remain parked.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T1 is a private provenance read-only implementation tranche and
creates no public-safe export; the sibling public-sync clone is not mutated.

## Claim Boundary

This work order authorizes a bounded read-only drift-receipt implementation
under `WORKER_MUST_NOT_COMMIT`, to be reviewed by the independent reviewer. It does not authorize
apply/copy modes, real-root mutation, semantic decisions, commit, push,
deployment, public-sync mutation, provider/live calls, production action, or
unattended mutation. Implementation begins only after the independent reviewer
commits this packet and session continuity records the worker dispatch.

## Reviewer Dispatch Disposition

`REVIEWER_ACCEPTED_DISPATCH_READY_WITH_REPAIRS`: the reviewer corrected the
lifecycle anchor, recorded the operator's designated-worker authorization, fixed
role wording, bound the 16-row input seam, defined tracked-versus-ignored
receipt fields, and resolved timeout behavior as a nonzero fail-closed result
with no partial or file receipt. Reviewer acceptance authorizes only the three
Allowed worker outputs under `WORKER_MUST_NOT_COMMIT`.
