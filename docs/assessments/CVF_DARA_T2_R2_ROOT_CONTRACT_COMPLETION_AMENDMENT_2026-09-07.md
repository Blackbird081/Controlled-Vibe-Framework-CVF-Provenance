# CVF DARA-T2 R2 Root Contract Completion Amendment

Memory class: governed-design-record

Status: DESIGN_CANDIDATE_PENDING_REVIEW

docType: assessment

Date: 2026-09-07

Batch ID: DARA-T2-R2-ROOT-CONTRACT-COMPLETION-AMENDMENT

providerExecutionAuthority: FORBIDDEN

## Purpose

Repair the two orchestrator-contract defects proven by the final admitted
external-worker return and its independent R2 review. This amendment makes the
existing implementation candidate reviewable without another external context
reload; it does not change implementation or pre-accept it.

## Target / Source

| Source | Frozen identity | Accepted fact | Disposition |
|---|---|---|---|
| `docs/reviews/CVF_DARA_T2_R1_CONSOLIDATED_REWORK_REVIEW_2026-09-07.md` | commit `eee0b0e57025538d411d78b6eaae6c34c810904f`; Git blob `6c7f72466831bedc0dd64275a0085019d149a4d6`; SHA-256 `6CB1F04AD9FE2E3964247EB644401A584C95C54A525294964228BD83D4609A86` | one required schema owner was omitted; exact base debt was not represented; lower return blocks are stale | ACCEPT |
| `docs/assessments/CVF_DARA_T2_R1_ROOT_CONTRACT_AND_MANIFEST_AMENDMENT_2026-09-07.md` | commit `203e9e6f7bc63873da008284688f7b533f65fbf9` | R1-01 through R1-05 behavior contract remains authoritative except where amended here | ACCEPT_SUPERSEDED_IN_PART |
| `docs/reviews/CVF_DARA_T2_R1_ROOT_CONTRACT_AND_MANIFEST_AMENDMENT_REVIEW_2026-09-07.md` | commit `1316ea7340541ab8e675c5b1965f5a1ff3ef52d0` | accepted R1 architecture identity remains the implementation behavior identity | ACCEPT_SUPERSEDED_IN_PART |
| `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json` | current size-policy owner | no exception bump; split owner is the compliant remedy | ACCEPT |
| current uncommitted DARA-T2 candidate | worker return SHA-256 `A536C8295565F0ED41EAC1DA76DEE84F869D8A0C938EF620109A4DB04BB8938D` | implementation evidence input only; not authority | INPUT_PENDING_REVIEW |

## Source / Predecessor Evidence

The worker consumed external invocation two of ceiling two and stopped
truthfully when the manifest required a fourth new path. The independent review
at `eee0b0e57025538d411d78b6eaae6c34c810904f` verified the additional path,
the exact base-existing golden-fixture failure, cleanup equality, parked-file
hashes, empty staging and unchanged worker HEAD. This amendment is based on
that committed review, not on memory-only worker conclusions.

## Scope / Methodology

The orchestrator changes only authority and evidence interpretation needed to
make the already-returned candidate decidable. It adds one exact file owner,
defines a strict differential rule for one named pre-existing test debt, and
permits one evidence-only reviewer reconciliation of the existing return. It
does not authorize implementation edits, a fixture repair, an exception bump,
another worker, another reviewer workflow, or any MFRP surface.

## Root-Cause Reconciliation

| Finding | Root owner | Contract correction |
|---|---|---|
| DARA-T2-R2-01 schema owner absent from manifest | orchestrator/dispatcher | add the exact schema-helper path as final path 14 |
| DARA-T2-R2-02 all-pass contract ignored exact base debt | orchestrator/dispatcher | accept only the named unchanged base failure while requiring zero DARA regressions |
| DARA-T2-R2-03 stale lower return blocks | worker evidence reconciliation | allow one reviewer-local documentation-only correction after amendment acceptance |

## Amended Maintainability Owner Contract

The following exact path is added as the fourth authorized new owner:

`governance/compat/check_work_order_dispatch_quality_architecture_schema.py`

Its sole role is DARA schema constants and schema-level parsing helpers used by
`check_work_order_dispatch_quality_source.py`. It must remain within the active
Python helper limit. The source owner must remain outside its near-hard band.
No exception-registry edit, compressed multi-statement workaround, unrelated
logic, or fifth new path is authorized.

## Revised Final Changed-Set Manifest

The final DARA-T2 material set contains exactly these fourteen paths:

1. `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
2. `docs/reference/CVF_ARCHITECTURE_READINESS_ADMISSION_STANDARD_2026-09-07.md`
3. `governance/compat/build_dispatch_packet_scaffold.py`
4. `governance/compat/build_dispatch_packet_architecture_readiness.py`
5. `governance/compat/build_worker_return_skeleton_scaffold.py`
6. `governance/compat/check_work_order_dispatch_quality.py`
7. `governance/compat/check_work_order_dispatch_quality_range.py`
8. `governance/compat/check_work_order_dispatch_quality_source.py`
9. `governance/compat/check_work_order_dispatch_quality_architecture_schema.py`
10. `governance/compat/run_worker_return_scaffold.py`
11. `governance/compat/test_build_dispatch_packet_scaffold.py`
12. `governance/compat/test_check_work_order_dispatch_quality_architecture_readiness.py`
13. `governance/compat/test_run_worker_return_scaffold.py`
14. `docs/reviews/CVF_DARA_T2_ARCHITECTURE_READINESS_ADMISSION_IMPLEMENTATION_WORKER_RETURN_2026-09-06.md`

Cleanup invariant: `governance/compat/test_check_work_order_dispatch_quality.py`
must remain byte-equal to its execution-base blob and absent from the final
material diff.

The two WP-ARCH-003 files are preserved incident evidence outside this
fourteen-path set. This amendment grants no authority to edit, stage, commit,
replace, archive or reject them.

## Differential Base-Debt Acceptance Contract

The command
`python -m unittest test_build_dispatch_packet_scaffold` remains a mandatory
truthful run. Its terminal result may be
`KNOWN_FAILURE_WITH_REASON_BASE_EQUIVALENT` only when all conditions below are
met:

1. the only failure is
   `TestWorkerReturnSkeleton.test_skeleton_matches_golden_fixture_exactly`;
2. the same test fails against the execution-base behavior for the same P4
   observation-block versus checked-in fixture drift;
3. DARA explicitly disables its architecture echo in that legacy golden
   fixture test, so DARA introduces no output delta in the tested fixture;
4. every other test in the module passes and the final count is exactly 79/80;
5. all DARA-specific tests, both return-scaffold tests, both size guards,
   pre-implementation, automation-assist, worker-return fast gate and later
   reviewer/commit gates pass; and
6. no PASS label is attached to this nonzero command.

Any different failure, additional failure, changed count, DARA-caused fixture
delta, or missing base-equivalence evidence blocks closure. This is a bounded
debt disposition, not a fixture acceptance, waiver, exception-registry change,
or authorization to call a failing command PASS.

## Reviewer-Local Evidence Reconciliation Authorization

After this amendment is committed and reviewed, the reviewer may edit only the
existing DARA worker-return document to reconcile its stale lower sections with
the already truthful top-level stop and this accepted authority. The allowed
corrections are:

- change the return to `COMPLETE_PENDING_REVIEW` only after all amended
  acceptance conditions are verified;
- replace eleven/thirteen-path stale claims with the exact fourteen-path set;
- bind every work-order field to the R1 consolidated rework work order and this
  accepted amendment/review;
- reconcile Machine Closure Package, jurisdiction, delta-claim, command,
  counter and claim-boundary text; and
- disclose the reviewer-local evidence repair and zero third invocation.

No Python, test, template, standard, fixture, MFRP, session, roadmap, ADIF or
WP-ARCH-003 edit is authorized by this reconciliation. If implementation
must change, closure stops and returns to design; it does not open invocation
three automatically.

## Amended Acceptance Matrix

| ID | Required proof | Exit condition |
|---|---|---|
| AM-01 through AM-05 | unchanged R1 behavior and hostile-family contract | exact focused evidence passes |
| AM-06 | both return routes echo six identities; scaffold module has no DARA regression | return-route tests pass; scaffold result is 80/80 or exact 79/80 bounded base debt above |
| AM-07 | Python and Markdown size guards | zero violations; no exception bump |
| AM-08 | pre-implementation and automation-assist | zero violations after exact unrelated-file isolation |
| AM-09 | terminal evidence reconciliation | no false PASS; all lower blocks match top status and amended authority |
| AM-10 | final manifest and cleanup | exact fourteen; cleanup target absent; no forbidden path |
| AM-11 | quota and role boundary | external invocation remains two; reviewer edits evidence only; provider calls zero |

## MFRP And Reviewer Boundary

MFRP P4-C1 remains the sole automatic reviewer-evidence collector. No receipt,
readout, collector, eligibility, checkpoint, or safety-marker change is
authorized. Reviewer work remains
`EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION`. One returned-evidence
reconciliation is allowed because it is fully determined, local, and cheaper
than a third external context reload.

## Evidence / Verification

The design-review boundary must verify the committed R2 review identity, the
fourteen-path arithmetic, the schema-helper import from the source owner, the
888-line final source-owner size, cleanup-path base equality, both parked-file
SHA-256 values, and the exact named golden-fixture failure. It must also run
reviewer-fast on this amendment. These checks establish amendment consistency
only; implementation acceptance remains a later reviewer decision.

## Decision / Proposed Tranche

This candidate permits only sequential review of this immutable amendment.
If accepted, the reviewer may perform the bounded return reconciliation and
evaluate the existing fourteen-path candidate. No external redispatch packet
is created.

## Risk / Corrective Action

The primary risk is converting a precise base-debt exception into a general
waiver. The six conjunctive conditions above therefore fail closed, keep the
nonzero command labeled as known failure, and preserve the separate fixture
debt. The second risk is role blending; the reviewer-local authorization is
restricted to one documentation artifact and forbids implementation edits.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| exact manifest froze direct owners but missed a transitive near-threshold split | `ORCHESTRATOR_PACKET_GAP` | `GOVERNANCE_CONTROL_PLANE` | `STANDARD_UPDATE_CANDIDATE` | require transitive touched-owner size projection before external dispatch |
| all-pass language had no exact differential-debt branch | `ORCHESTRATOR_PACKET_GAP` | `GOVERNANCE_CONTROL_PLANE` | `DESIGN_REVIEW_REQUIRED` | add bounded base-equivalence vocabulary without permitting false PASS |
| recalling the worker would spend invocation three only to rewrite evidence | `REVIEW_COST_OVERHEAD` | `REVIEW_COST_CONTROL` | `OWNER_SURFACE_UPDATE_CANDIDATE` | prefer disclosed reviewer-local evidence repair when implementation is unchanged |

No new ADIF entry is opened by this amendment. Final closure must decide
whether the transitive size-projection and return-consistency observations meet
the recurrence threshold for existing-owner promotion.

Runtime/provider/cost learning lane: N/A_WITH_REASON: this is local authority
repair with no provider/live execution. Exact token usage is unavailable; only
the avoided invocation count is asserted.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_python_automation_size.py` |
| literalTokensReviewed | assessment headings, defect classes, learning dispositions, trace labels, protected-path authorization and private export disposition |
| gateRunPurpose | confirm the completed amendment after source, size, manifest and review-cost reconciliation |
| claimBoundary | checker conformance does not accept this design or the implementation candidate |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: after this amendment receives an immutable
review, retain and review the returned DARA implementation on the eleven
protected paths below. The authorization adds the schema helper but changes no
implementation semantics by itself.

Protected paths:

- `governance/compat/build_dispatch_packet_architecture_readiness.py`
- `governance/compat/build_dispatch_packet_scaffold.py`
- `governance/compat/build_worker_return_skeleton_scaffold.py`
- `governance/compat/check_work_order_dispatch_quality.py`
- `governance/compat/check_work_order_dispatch_quality_architecture_schema.py`
- `governance/compat/check_work_order_dispatch_quality_range.py`
- `governance/compat/check_work_order_dispatch_quality_source.py`
- `governance/compat/run_worker_return_scaffold.py`
- `governance/compat/test_build_dispatch_packet_scaffold.py`
- `governance/compat/test_check_work_order_dispatch_quality_architecture_readiness.py`
- `governance/compat/test_run_worker_return_scaffold.py`

Operator authorization: the operator authorized Codex as orchestrator and
reviewer, delegated inter-agent exchange, and required evidence-driven CVF
foundation improvement before resuming WP-ARCH-003.

Rollback boundary: revert only the eventual DARA-T2 material commit and its
completion evidence if rejected. Preserve T1, both R1/R2 reviews, MFRP P4-C1,
the two parked WP-ARCH-003 files, and unrelated worktree state.

Not authorized: no worker commit, external invocation three, exception bump,
MFRP change, runtime/provider/live/public action, DARA-T3, or WP-ARCH-003 repair.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex orchestrator after independent R2 review |
| Provider or surface | local private CVF workspace |
| Session or invocation | DARA-T2 R2 root-contract completion amendment, 2026-09-07 |
| Working directory | repository root |
| Command or tool surface | committed review reads, size-policy and source-import reads, exact manifest reconciliation, apply_patch |
| Target paths | this amendment only |
| Allowed scope source | operator authorized Codex as orchestrator/reviewer and delegated inter-agent exchange; committed R2 review requires root-contract repair without redispatch |
| Before status evidence | R2 rejection review committed at `eee0b0e57025538d411d78b6eaae6c34c810904f`; fourteen-path worker candidate preserved uncommitted; two WP files hash-preserved |
| After status evidence | one design candidate; implementation untouched; external invocation count remains two |
| Diff evidence | exact one-path orchestrator amendment diff |
| Approval boundary | root-contract, manifest, differential-debt and evidence-reconciliation authority only |
| Claim boundary | no implementation repair, design acceptance, worker redispatch, material closure, runtime/provider/live/public effect |
| Agent type | orchestrator |
| Invocation ID | `dara-t2-r2-root-contract-completion-amendment-2026-09-07` |
| Expected manifest | this assessment only |
| Actual changed set | this assessment plus preserved worker and parked pre-existing worktree changes |
| Manifest delta | MATCH for orchestrator-owned output |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private design amendment; no public-sync authority.

## Claim Boundary

This artifact proposes a bounded authority correction only. It does not accept
itself or DARA-T2, edit worker implementation, consume an external invocation,
open DARA-T3, resume WP-ARCH-003, change MFRP, publish, deploy, or claim runtime
or production readiness.
