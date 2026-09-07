# CVF DARA-T2 R1 Root Contract And Manifest Amendment

Memory class: governed-design-record

Status: DESIGN_CANDIDATE_PENDING_REVIEW

docType: assessment

Date: 2026-09-07

Batch ID: DARA-T2-R1-DESIGN-AMENDMENT

providerExecutionAuthority: FORBIDDEN

## Purpose

Correct the DARA-T2 root contract before spending the final admitted external
worker invocation. This amendment converts reviewer findings R1-01 through
R1-05 into a feasible split-path manifest and explicit fail-closed machine
acceptance requirements; it does not implement them.

## Target / Source

| Source | Accepted fact | Disposition |
|---|---|---|
| `docs/reviews/CVF_DARA_T2_ARCHITECTURE_READINESS_ADMISSION_IMPLEMENTATION_COMPLETION_2026-09-06.md` | review commit `6746abf74e7ee691275a7979f78aa1b84b8b2c5a`; SHA-256 `57B8E57CF888F3228FFF7C322066373FB250BF71DE454E84DDB18722827E665F` | ACCEPT |
| `docs/assessments/CVF_DARA_T1_ARCHITECTURE_READINESS_CONTRACT_DESIGN_2026-09-06.md` | original schema, closed chain, digest, MFRP boundary, and return-to-design rule | ACCEPT_SUPERSEDED_IN_PART |
| `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json` | dispatch-quality monolith/test caps and split directions | ACCEPT |
| `governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json` | work-order template near-threshold rotation rule | ACCEPT |
| current uncommitted DARA-T2 worker delta | useful implementation candidate, not authority or accepted code | INPUT_PENDING_REWORK |

## Source / Predecessor Evidence

The R1 review is committed at `6746abf74e7ee691275a7979f78aa1b84b8b2c5a`
and records the five consolidated findings. T1 remains authoritative except for
the path manifest and validation details explicitly amended here. The worker
delta remains uncommitted and cannot serve as authority for this amendment.

## Scope / Methodology

The orchestrator used the committed R1 reviewer record and current size-policy
owners to replace the infeasible exact-eleven manifest. The amendment freezes
only the minimum new owner paths required to satisfy existing maintainability
rules and the five consolidated findings. Worker implementation choices inside
those boundaries remain autonomous.

## Root-Cause Reconciliation

| Finding | Root owner | Contract correction |
|---|---|---|
| R1-01 absent declaration bypass | implementation worker under complete T1 intent | require classification for every active external dispatch; absence blocks |
| R1-02 fabricated review commit accepted | implementation worker under complete T1 intent | validate full ancestor commit and committed review blob bytes |
| R1-03 incomplete chain validation | implementation worker under complete T1 intent | freeze path/locator, carrier, rollback, evidence-output, and authority-boundary checks |
| R1-04 failing commands called PASS/COMPLETE | worker evidence interpretation | require exit-state truthful labels and terminal reconciliation |
| R1-05 infeasible original manifest | orchestrator/dispatcher | authorize three exact split paths and final line-count outcomes |

## Amended Applicability Contract

Every active work order whose `dispatchSurface` is
`EXTERNAL_AGENT_CLI_MCP` must carry exactly one
`Architecture-Readiness Admission:` declaration. Missing or unknown declaration
is `BLOCKED_ARCHITECTURE_APPLICABILITY_UNCLASSIFIED`; it is never silently
non-applicable.

Allowed external declarations are:

- `REQUIRED`: HIGH/CRITICAL, authority-expanding, or otherwise design-bearing
  external dispatch; full matrix and admission checks apply;
- `NOT_APPLICABLE_ACCEPTED_DESIGN_ECHO`: a work order transcribed from a
  previously accepted immutable matrix; all six echo identities must match;
- `NOT_APPLICABLE_EXTERNAL_LOW_RISK_WITH_REASON:<reason>`: explicitly low-risk,
  non-design-bearing, non-authority-expanding work with a non-empty reason.

Internal dispatch may use `NOT_APPLICABLE_INTERNAL_AGENT_WITH_REASON:<reason>`.
The checker must determine external versus internal from the existing Review
Cost scalar, not from prose. Tests must prove that an active external packet
with no declaration blocks and that the existing R1 test accepting omission is
removed or inverted.

## Amended Immutable Semantic Review Binding

For `ACCEPTED_BOUNDED` and accepted-design echo:

1. `architectureSemanticReviewCommit` must be exactly 40 lowercase hexadecimal
   characters and resolve to a Git commit.
2. The commit must be an ancestor of current `HEAD`.
3. The normalized review path must exist in that commit.
4. Validation must read bytes from `<commit>:<review-path>`, not working-tree
   bytes.
5. `architectureSemanticReviewFileSha256` must equal SHA-256 of those committed
   bytes.
6. The committed review blob must contain every matrix `criterionId` and its
   accepted disposition.

Tests must reject nonexistent, non-ancestor, wrong-path, wrong-blob-hash, stale
working-tree, and missing-criterion cases. No fabricated commit may appear in a
positive test.

## Amended Closed-Chain Machine Contract

The row validator must add all missing T1 checks:

- parse `trustSource` as an exact normalized repo-relative authority path plus
  non-empty locator; both must resolve;
- reject archive paths, provider-specific/private memory carriers, traversal,
  absolute paths, and paths outside the repository for authority and owner
  identities;
- resolve the `contextCarrierPath` and `contextField` pair in the named source;
- require `evidenceOutputPath` to be a normalized repo-relative dated Markdown
  path under an authorized evidence/review directory with an existing parent;
- split semicolon-delimited `rollbackPaths`, normalize every entry, and require
  every path to be within the work order's writable artifact manifest;
- preserve registration and explicit contract-only exemptions without allowing
  those exemptions on unrelated fields; and
- emit specific blocked diagnostics for each missing or malformed link.

One negative test per bullet is mandatory. The previously demonstrated probe
with missing trust source, missing carrier, outside-root rollback, and undated
output must no longer return an empty issue list.

## Evidence Truth Contract

Command results with any failed test or non-zero exit are `FAIL`,
`KNOWN_FAILURE_WITH_REASON`, or `BLOCKED_WITH_REASON`; never PASS. A test family
is PASS only when every required case in that family passes. The worker may
prove a failure pre-existing by base replay, but that proof does not change the
command's exit status. `COMPLETE_PENDING_REVIEW` requires every mandatory gate
to pass; otherwise the return status is `BLOCKED_WITH_REASON`.

## Amended Maintainability And Owner Split Contract

Three new exact paths are authorized:

| New path | Owner purpose | Required outcome |
|---|---|---|
| `docs/reference/CVF_ARCHITECTURE_READINESS_ADMISSION_STANDARD_2026-09-07.md` | full DARA schema/applicability/binding/chain contract rotated from the near-threshold work-order template | template retains only a compact canonical pointer; same-directory active-Markdown rotation evidence exists |
| `governance/compat/build_dispatch_packet_architecture_readiness.py` | architecture block renderer/constants extracted from dispatch scaffold | main scaffold finishes at or below 874 physical lines and Python size gate passes |
| `governance/compat/test_check_work_order_dispatch_quality_architecture_readiness.py` | all DARA-specific positive/negative tests | frozen monolithic test file is byte-identical to base and absent from final diff |

No exception-registry bump is authorized. No compressed multi-statement lines
may be used to evade a threshold. New reference and Python files must satisfy
their own class limits and checker/source-read-ahead requirements.

## Revised Final Changed-Set Manifest

The final rework diff must contain exactly these thirteen worker-owned paths:

1. `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
2. `docs/reference/CVF_ARCHITECTURE_READINESS_ADMISSION_STANDARD_2026-09-07.md`
3. `governance/compat/build_dispatch_packet_scaffold.py`
4. `governance/compat/build_dispatch_packet_architecture_readiness.py`
5. `governance/compat/build_worker_return_skeleton_scaffold.py`
6. `governance/compat/check_work_order_dispatch_quality.py`
7. `governance/compat/check_work_order_dispatch_quality_range.py`
8. `governance/compat/check_work_order_dispatch_quality_source.py`
9. `governance/compat/run_worker_return_scaffold.py`
10. `governance/compat/test_build_dispatch_packet_scaffold.py`
11. `governance/compat/test_check_work_order_dispatch_quality_architecture_readiness.py`
12. `governance/compat/test_run_worker_return_scaffold.py`
13. `docs/reviews/CVF_DARA_T2_ARCHITECTURE_READINESS_ADMISSION_IMPLEMENTATION_WORKER_RETURN_2026-09-06.md`

Cleanup invariant: `governance/compat/test_check_work_order_dispatch_quality.py`
must be restored byte-for-byte to the execution-base blob and must not appear in
the final diff. It is an authorized cleanup target during rework but not a final
changed artifact.

## Regression And Acceptance Matrix

| ID | Required proof | Exit condition |
|---|---|---|
| AM-01 | external active packet without declaration | blocked as unclassified |
| AM-02 | accepted echo with genuine committed review identity | passes without second review |
| AM-03 | fake/non-ancestor/stale/mismatched review identity | all block |
| AM-04 | missing trust/carrier/rollback/output/authority-boundary link | each blocks independently |
| AM-05 | original sixteen hostile families | all cases exit zero, with corrected HT-02/HT-09 semantics |
| AM-06 | both return scaffold routes | exact echo parity and identity-drift block |
| AM-07 | Python and Markdown size guards | zero violations |
| AM-08 | pre-implementation and automation-assist gates | zero violations after exact isolation of unrelated parked files |
| AM-09 | return evidence truth | no PASS label attached to a non-zero command |
| AM-10 | final manifest | exact thirteen paths; cleanup target absent; no forbidden path |

## MFRP And Reviewer Boundary

MFRP P4-C1 remains the sole automatic reviewer-evidence collector. No receipt,
readout, collector, eligibility, checkpoint, or safety-marker change is allowed.
The final worker return may populate the existing optional P4 observation block
only from natural eligibility. Codex reviewer consumes returned evidence and
does not edit or recreate implementation.

## Decision / Proposed Tranche

This candidate permits only sequential review of this amendment. External
rework remains blocked until the amendment is committed, reviewed, and bound
into a REWORK packet with cumulative external invocation count 1 of ceiling 2.

## Risk / Corrective Action

The main residual risk is splitting logic while changing behavior. The rework
packet must require base-preserving extraction tests, exact old-test-file blob
restoration, and focused regression before repository gates. Any fourth new
path, exception bump, or MFRP change returns to design and does not consume the
remaining invocation automatically.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| infeasible destination manifest escaped dispatch review | `ORCHESTRATOR_PACKET_GAP` | `GOVERNANCE_CONTROL_PLANE` | `STANDARD_UPDATE_CANDIDATE` | future dispatchers must read size registries before freezing exact paths |
| hostile-test label allowed inverse behavior | `WORKER_EXECUTION_ERROR` | `GOVERNANCE_CONTROL_PLANE` | `MACHINE_CHECK_CANDIDATE` | require acceptance-text-to-test assertion reconciliation |
| current-tree hash substituted for committed review binding | `WORKER_EXECUTION_ERROR` | `GOVERNANCE_CONTROL_PLANE` | `MACHINE_CHECK_CANDIDATE` | use committed blob resolver pattern |

Runtime/provider/cost learning lane: N/A_WITH_REASON: this is a local design
amendment with no provider/live call or runtime behavior claim.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_python_automation_size.py` |
| literalTokensReviewed | assessment headings, defect classes, learning dispositions, trace labels, same-domain rotation, near-threshold shrink, exception touch rule, private export disposition |
| gateRunPurpose | confirm the design artifact after source and size-policy reconciliation |
| claimBoundary | structural conformance does not accept the design or implement rework |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex orchestrator after completing independent R1 review |
| Provider or surface | local private CVF workspace |
| Session or invocation | DARA-T2 R1 root-contract amendment, 2026-09-07 |
| Working directory | repository root |
| Command or tool surface | committed review reads, registry/checker reads, exact path design, apply_patch |
| Target paths | this design amendment only |
| Allowed scope source | operator authorized Codex to act as orchestrator and manage inter-agent exchange |
| Before status evidence | review committed at `6746abf74`; worker delta preserved outside worktree in named Git stash; unrelated WP files hash-preserved outside worktree |
| After status evidence | one design candidate; no implementation or external invocation |
| Diff evidence | exact one-path design candidate diff |
| Approval boundary | root-contract and manifest correction only |
| Claim boundary | no worker code change, accepted design, redispatch, commit of worker material, runtime/provider/live/public effect |
| Agent type | orchestrator |
| Invocation ID | `dara-t2-r1-root-contract-amendment-2026-09-07` |
| Expected manifest | this assessment only |
| Actual changed set | this assessment only |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private design amendment; no public-sync authority.

## Claim Boundary

This artifact proposes a corrected DARA-T2 rework contract only. It does not
accept itself, modify worker implementation, change MFRP, consume the remaining
external invocation, commit worker material, open DARA-T3, resume WP-ARCH-003,
publish, deploy, or claim runtime or production readiness.
