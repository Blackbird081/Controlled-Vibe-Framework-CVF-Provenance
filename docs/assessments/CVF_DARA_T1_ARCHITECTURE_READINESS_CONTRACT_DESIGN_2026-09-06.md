# CVF DARA-T1 Architecture Readiness Contract Design

Memory class: governed-assessment

Status: DARA_T1_DESIGN_ACCEPTED_BOUNDED

docType: assessment

Date: 2026-09-06

Batch ID: DARA-T1

providerExecutionAuthority: FORBIDDEN

## Purpose

Freeze the pre-invocation architecture-readiness contract that prevents an
external implementation worker from receiving an incomplete or self-selected
architecture. The contract extends the existing work-order quality owner,
preserves semantic reviewer authority, and supplies a digest-bound phase-return
identity that the existing MFRP route may consume later without a second
receipt, readout, collector, or review checkpoint.

## Target / Source

| Source | Design fact used | Disposition |
|---|---|---|
| `docs/roadmaps/CVF_DISPATCHER_ARCHITECTURE_READINESS_AND_QUOTA_ADMISSION_ROADMAP_2026-09-06.md` | T1 must freeze closed matrix fields, role/fault attribution, MFRP composition, and quota admission before invocation 1 | ACCEPT |
| `docs/reviews/CVF_DARA_T0_DISPATCHER_ARCHITECTURE_READINESS_EVIDENCE_REVIEW_2026-09-06.md` | T0 permits bounded T1 design and forbids T2 or finding repair before review | ACCEPT |
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | canonical work-order authority and dispatch contract owner | ACCEPT |
| `governance/compat/check_work_order_dispatch_quality.py` | canonical work-order quality gate entrypoint | ACCEPT |
| `governance/compat/check_work_order_dispatch_quality_range.py` | current dispatch-time work-order validation composition | ACCEPT |
| `governance/compat/check_work_order_dispatch_quality_source.py` | current exact path, symbol, line-anchor, and source-verification validation owner | ACCEPT |
| `governance/compat/build_dispatch_packet_scaffold.py` | current baseline/work-order scaffold owner | ACCEPT |
| `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md` | existing review admission, cumulative invocation ceiling, and non-recreation boundary | ACCEPT |
| `docs/roadmaps/CVF_GCLH_MACHINE_FIRST_REVIEW_PREFLIGHT_ROADMAP_2026-09-01.md` | MFRP owns deterministic evidence reuse and exception-focused reviewer readout | ACCEPT |
| `governance/compat/agent_autorun_machine_verification.py` | current receipt v3 explicitly does not check hard-obligation maps or complete phase-return envelopes | ACCEPT_LIMITATION |
| `governance/compat/agent_automation_machine_verification_readout.py` | current MFRP readout exposes limitations, unclassified items, exceptions, and deterministic results | ACCEPT_EXISTING_OWNER |

No pending `WP-ARCH-003` worker assertion is used as architecture authority.
Those two files remain parked incident evidence only.

## Source / Predecessor Evidence

DARA-T0 is accepted at the current continuity boundary, the roadmap explicitly
opens T1 design, and all eleven source rows above resolve locally. T2 remains
closed pending this design's sequential review and a fresh GC-018/work order.

## Scope / Methodology

This design resolves four bounded questions:

1. Which exact data must an orchestrator freeze before an external worker can
   implement HIGH or CRITICAL design-bearing work?
2. Which facts can machinery validate, and which decision remains semantic?
3. Which role owns a later defect and its quota cost?
4. How does the result enter MFRP later without creating a parallel control
   plane?

The design is documentation-only. It does not modify templates, scaffolds,
checkers, receipt schemas, runtime code, P4 eligibility, or worker findings.

## Applicability And Admission Declaration

Canonical declaration:

`Architecture-Readiness Admission: REQUIRED`

A work order must carry that declaration when all three conditions hold:

- `dispatchSurface: EXTERNAL_AGENT_CLI_MCP`;
- risk is HIGH or CRITICAL, or authority/scope expansion is admitted through
  the existing Review Cost trigger vocabulary; and
- the worker would create or materially change a behavior owner, producer,
  schema/context carrier, export, registration, composition root, runtime
  consumer, security decision, or migration route.

Documentation-only transcription of an already accepted exact architecture
uses `Architecture-Readiness Admission: NOT_APPLICABLE_ACCEPTED_DESIGN_ECHO`
and must cite the accepted matrix digest, review path, review commit, and
verdict. Internal-agent work remains governed by proportional routing and may
use `NOT_APPLICABLE_INTERNAL_AGENT_WITH_REASON`; this contract does not widen
the external invocation counter to provider-native helpers.

No agent may choose `NOT_APPLICABLE` merely because the work order already
contains filenames. Ambiguous applicability is
`BLOCKED_ARCHITECTURE_APPLICABILITY_UNCLASSIFIED`.

## Architecture Binding Matrix Contract

Schema identifier: `cvf.dara.architectureBindingMatrix.v1`.

One row represents one acceptance criterion whose behavior must reach a
production or explicitly contract-only consumer. All scalar cells are
required. `NONE_WITH_REASON:<reason>` is allowed only where stated below;
`TBD`, `TODO`, angle-bracket placeholders, unnamed adjacent files, path
classes, and worker-selection language are forbidden.

| Field | Required shape | Machine responsibility | Semantic owner |
|---|---|---|---|
| `criterionId` | unique stable ID | non-empty and unique | orchestrator defines; reviewer accepts coverage |
| `riskClass` | `LOW`, `MEDIUM`, `HIGH`, or `CRITICAL` | enum | orchestrator proposes; reviewer confirms |
| `behaviorIdentity` | unique stable behavior name | non-empty; duplicate name blocks | reviewer decides semantic uniqueness |
| `canonicalOwnerPath` | one exact repo-relative existing path | exists and is not archive/provider-private | reviewer accepts ownership |
| `canonicalOwnerLocator` | exact heading, type, function, schema, or field | locator resolves in owner path | reviewer judges meaning |
| `implementationDisposition` | `EXTEND_EXISTING` or `CREATE_NEW` | enum | reviewer accepts create/extend choice |
| `implementationPath` | exact repo-relative path | exists for extension; parent exists for creation | reviewer accepts placement |
| `implementationSymbol` | exact symbol or document section identity | existing symbol resolves; new symbol has no collision | reviewer accepts responsibility boundary |
| `producerPath` / `producerSymbol` | exact data or decision producer | path and existing symbol resolve | reviewer accepts trust source |
| `trustSource` | canonical authority path plus locator | authority path resolves and is not provider-private | reviewer accepts authority class |
| `contextCarrierPath` / `contextField` | exact transport type/schema and field | path and existing field resolve, or planned field has no collision | reviewer accepts transport semantics |
| `exportPath` / `exportSymbol` | exact public/package export | existing export resolves or planned export is collision-free | reviewer accepts exposure boundary |
| `registrationPath` / `registrationSymbol` | exact registry/factory binding, or `NONE_WITH_REASON:<reason>` | pair completeness and path/symbol resolution | reviewer accepts legitimate absence |
| `compositionRootPath` / `compositionRootSymbol` | exact production construction root | path and existing symbol resolve | reviewer accepts actual reachability |
| `runtimeConsumerPath` / `runtimeConsumerSymbol` | exact non-test consumer, or `NONE_WITH_REASON:CONTRACT_ONLY_<reason>` | pair completeness, non-test path, or explicit contract-only state | reviewer accepts claim boundary |
| `positiveTestPath` | exact test path | exists or parent exists for planned creation | reviewer accepts adequacy |
| `negativeTestPath` | exact rejection-path test | exists or parent exists for planned creation | reviewer accepts adequacy |
| `bypassTestPath` | exact fail-open/bypass test | exists or parent exists for planned creation | reviewer accepts adequacy |
| `compositionTestPath` | exact producer-to-consumer test | exists or explicit contract-only reason | reviewer accepts adequacy |
| `compatibilityDisposition` | exact migration/input/output posture | non-empty; controlled prefix | reviewer accepts compatibility |
| `rollbackPaths` | explicit semicolon-separated changed paths | each path is inside allowed scope | reviewer accepts reversibility |
| `evidenceOutputPath` | one literal dated repo-relative output path | exact path; no placeholder; unique across rows where required | reviewer accepts evidence sufficiency |
| `machineDisposition` | `PASS_IDENTITY_AND_COVERAGE`, `BLOCKED_*`, or `UNCLASSIFIED_*` | produced by gate, never worker-authored acceptance | reviewer consumes limitation-aware result |
| `semanticAcceptance` | `PENDING_REVIEW`, `ACCEPTED_BOUNDED`, or `REJECTED_WITH_REASON` | enum and commit/path binding only | reviewer is sole decision owner |
| `semanticReviewPath` / `semanticReviewCommit` | existing review path plus full commit SHA after acceptance | path exists at commit and contains criterion/verdict | reviewer-authored evidence |

Matrix-level scalars:

- `architectureMatrixSchema`;
- `architectureMatrixRowCount`;
- `architectureMatrixCanonicalDigest`;
- `architectureMatrixDigestRecipe`;
- `architectureMachineDisposition`;
- `architectureSemanticDisposition`;
- `architectureSemanticReviewPath`;
- `architectureSemanticReviewCommit`;
- `architectureSemanticReviewFileSha256`.

The digest recipe is UTF-8 without BOM, LF row serialization, forward-slash
repo-relative paths, ordinal/code-point row ordering by `criterionId`, and one
trailing LF. Its immutable authoring preimage includes fields from
`criterionId` through `evidenceOutputPath` only. It excludes derived
`machineDisposition`, `semanticAcceptance`, `semanticReviewPath`, and
`semanticReviewCommit` values, so the reviewer can bind the pre-review digest
without a circular self-reference. Machine output cannot set
`architectureSemanticDisposition: ACCEPTED_BOUNDED`.

## Closed-Chain Invariants

For every applicable row:

```text
canonical authority
  -> canonical owner
  -> implementation symbol
  -> producer and trust source
  -> context carrier
  -> export
  -> registration or accepted absence
  -> composition root
  -> non-test runtime consumer or explicit contract-only boundary
  -> positive + negative + bypass + composition verification
  -> literal evidence output
```

The machine blocks missing pairs, nonexistent existing identities, duplicate
behavior owners, path placeholders, archive/provider-private authority,
out-of-scope rollback paths, unbound semantic review evidence, and incomplete
chains. It reports `UNCLASSIFIED_*` when it cannot prove whether two symbols
are semantically equivalent or whether a runtime consumer is correct.

The reviewer decides ownership correctness, semantic equivalence, trust
fitness, architecture sufficiency, test adequacy, and whether an explicit
contract-only boundary is honest. Machine PASS is never architecture approval.

## Role And Fault Attribution Contract

Each dispatch and return carries non-negative counts and evidence IDs for:

| Fault class | Definition | Default accountable owner |
|---|---|---|
| `ORCHESTRATOR_ARCHITECTURE_DEFECT` | accepted work order omitted, contradicted, or delegated a required architecture binding | orchestrator/dispatcher |
| `WORKER_CONTRACT_EXECUTION_DEFECT` | worker violated a complete accepted contract without an upstream contradiction | implementation worker |
| `REVIEWER_LATE_DISCOVERY` | reviewer accepted a matrix despite evidence already showing the defect | reviewer |
| `REPAIR_INTRODUCED_DEFECT` | a repair created a new defect not present in the prior frozen result | actor performing repair |
| `MACHINE_COVERAGE_GAP` | deterministic gate admitted a machine-checkable malformed or missing field | checker owner; not automatically worker |
| `UNATTRIBUTED_PENDING_EVIDENCE` | causal evidence is insufficient | no blame until resolved |

Required scalars are `dispatcherDefectCount`, `workerExecutionDefectCount`,
`reviewerLateDiscoveryCount`, `repairIntroducedDefectCount`,
`machineCoverageGapCount`, `unattributedDefectCount`, and
`faultAttributionEvidenceIds`. Counts describe evidence, not severity.

A missing upstream binding cannot be reclassified as worker fault merely
because the worker selected an implementation. The correct state is
`ORCHESTRATOR_ARCHITECTURE_DEFECT`, followed by a return to design.

## Pre-Invocation Quota Admission State Machine

The existing Review Cost fields remain authoritative. DARA adds no invocation
counter and no second ceiling.

```text
DRAFT
  -> MATRIX_MACHINE_COMPLETE
  -> SEMANTIC_REVIEW_ACCEPTED
  -> EXISTING_USAGE_AND_CEILING_CHECK
  -> ADMITTED_WITHIN_CUMULATIVE_CEILING
  -> EXTERNAL_INVOCATION_1
```

Fail-closed terminal states before invocation are:

- `BLOCKED_ARCHITECTURE_MATRIX_INCOMPLETE`;
- `BLOCKED_ARCHITECTURE_UNCLASSIFIED`;
- `BLOCKED_SEMANTIC_REVIEW_MISSING_OR_STALE`;
- `BLOCKED_USAGE_UNKNOWN`;
- `BLOCKED_INVOCATION_CEILING_REACHED`;
- `BLOCKED_SOURCE_AUTHORITY_CONTRADICTION`.

Admission requires all of these simultaneously:

- `architectureMachineDisposition: PASS_IDENTITY_AND_COVERAGE`;
- `architectureSemanticDisposition: ACCEPTED_BOUNDED` bound to an immutable
  review path, commit, and file SHA-256;
- `preExecutionReviewAdmission: REQUIRED_TRIGGERED` with the applicable
  existing Review Cost trigger for the first design-bearing dispatch;
- `reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION`;
- known `cumulativeExternalInvocationCount` strictly below
  `externalInvocationCeiling`;
- `quotaAdmissionDisposition: ADMITTED_WITHIN_CUMULATIVE_CEILING`.

Once the design is accepted, authoring or transcribing a work order from that
same immutable matrix does not admit another pre-execution review. Any digest,
owner, path, symbol, scope, risk, authority, or external-effect change makes
the semantic acceptance stale and returns to the existing triggered review
boundary.

## MFRP Composition Contract

DARA-T2 must not modify `cvf.autorun.pass-receipt.v3`, P4-C1 eligibility,
`mfrp_shadow_canary_autocollect.py`, checkpoint counts, or safety markers.
The current receipt truthfully declares that hard-obligation maps and complete
phase-return envelopes are not checked; T2 must not erase that limitation.

Instead, the accepted matrix identity is carried in the existing work order
and echoed in the existing worker-return/phase-return surface using these
scalars:

- `architectureMatrixSchema`;
- `architectureMatrixCanonicalDigest`;
- `architectureSemanticReviewPath`;
- `architectureSemanticReviewCommit`;
- `architectureSemanticReviewFileSha256`;
- `architectureBindingEchoDisposition` set to `EXACT_MATCH` or
  `BLOCKED_IDENTITY_DRIFT`.

DARA-T2 validates the pre-invocation work order. DARA-T3 replays the historical
Initial/R1/R2 chain. Only DARA-T4 may propose feeding this already-bound echo
through the existing MFRP phase-return/readout seam, and only under MFRP's
existing admission and checkpoint rules. No DARA receipt, readout, reviewer
packet, evidence ledger, collector, or checkpoint may be created.

## DARA-T2 Exact Owner Change Map

Subject to fresh GC-018 and work-order authorization, T2 may change only these
existing owner surfaces plus its required baseline/work order/return/review:

| Path | Planned bounded change |
|---|---|
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | add the applicability declaration, matrix/scalars, fault attribution, echo contract, and fail-closed quota ordering |
| `governance/compat/build_dispatch_packet_scaffold.py` | emit checker-safe blocked defaults and matrix headings; never invent architecture rows |
| `governance/compat/test_build_dispatch_packet_scaffold.py` | prove applicable scaffold defaults are blocked and no second reviewer workflow appears |
| `governance/compat/build_worker_return_skeleton_scaffold.py` | emit the immutable architecture identity echo without copying or re-evaluating the matrix |
| `governance/compat/run_worker_return_scaffold.py` | keep the standalone worker-return generator aligned with the same echo contract |
| `governance/compat/test_run_worker_return_scaffold.py` | prove both worker-return generation routes remain aligned and blocked on identity drift |
| `governance/compat/check_work_order_dispatch_quality.py` | define shared marker/enums and preserve the existing gate entrypoint |
| `governance/compat/check_work_order_dispatch_quality_range.py` | invoke architecture validation only for applicable changed work orders |
| `governance/compat/check_work_order_dispatch_quality_source.py` | reuse exact path/symbol/line validation for matrix identities |
| `governance/compat/test_check_work_order_dispatch_quality.py` | add positive and hostile dispatch cases |

T2 must return to design before adding any other production/checker/helper
path. T2 does not touch MFRP receipt/readout/collector code.

## Hostile Test Contract

Minimum T2 test families:

1. applicable HIGH external dispatch with a complete accepted matrix passes;
2. missing declaration or row fails before invocation;
3. placeholder or path-class evidence output fails;
4. duplicate `behaviorIdentity`, or two owner assignments for the same
   behavior, fails; one owner path may legitimately own different behaviors;
5. nonexistent existing path, locator, or symbol fails;
6. producer without carrier/export/registration/composition/consumer fails;
7. planned component with no production composition test fails;
8. worker-selected owner or `PENDING_REVIEW` semantic state fails;
9. review path/commit/file-hash mismatch fails;
10. matrix digest drift fails;
11. unknown usage or reached ceiling fails;
12. architecture PASS with forbidden reviewer recreation language fails;
13. accepted-design documentation echo passes without a second review;
14. internal-agent non-applicability remains outside external quota counting;
15. current P4-C1 collector and receipt-v3 tests remain unchanged and pass;
16. the historical `WP-ARCH-003` Initial/R1/R2 fixture is not used until T3.

## Design Position

The safe composition exists. DARA can block architecture-incomplete external
dispatch inside the existing Work Order Template and dispatch-quality gate,
while Review Cost owns semantic admission/quota and MFRP retains reviewer
readout/evidence collection. No new control-plane owner is required.

Accepted T1 disposition: `DESIGN_ACCEPTED_BOUNDED` through the disclosed
sequential review recorded in
`docs/reviews/CVF_DARA_T1_ARCHITECTURE_READINESS_CONTRACT_DESIGN_REVIEW_2026-09-06.md`.

## Decision / Proposed Tranche

The frozen candidate at `86d5b7a69` was sequentially reviewed and repaired in
one consolidated reviewer-local set. Update the roadmap to
`DARA_T1_DESIGN_ACCEPTED_BOUNDED_T2_WORK_ORDER_ALLOWED`. That status permits
only T2 baseline/work-order authoring; it does not permit implementation or
external invocation.

## Risk / Corrective Action

The highest risk is false confidence from a syntactically complete matrix.
The design therefore makes machine output explicitly limited to identity and
coverage and requires immutable semantic review evidence. The second risk is
scope expansion into MFRP receipt internals; T2 is expressly forbidden from
changing them. Any need for a receipt/readout schema change returns to DARA-T4
and MFRP ownership after T3 replay.

## Acceptance Criteria

- Matrix fields are closed, exact, digest-bound, and separate machine from
  semantic authority.
- Full producer-to-consumer composition is represented or honestly bounded as
  contract-only.
- Fault attribution cannot default an upstream design omission to the worker.
- External invocation 1 is impossible before matrix, semantic, usage, and
  ceiling gates all pass.
- Accepted-design work-order transcription does not create duplicate review.
- T2 has an exact existing-owner path set and hostile-test contract.
- Receipt v3, MFRP P4-C1 collector, eligible count, and checkpoints remain
  unchanged.
- `WP-ARCH-003` findings remain parked until T2/T3 and a fresh accepted matrix.

## Evidence / Verification

Verification is provider-free: resolve every source path, run Markdown
structural and checker-read-ahead guards, verify the exact one-path diff, run
the pre-implementation bundle, commit the design alone, and review only from
that frozen commit. These checks prove document and identity consistency, not
semantic acceptance or implemented prevention.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Purpose, Target / Source, Scope / Methodology, Risk / Corrective Action, Acceptance Criteria, checker-read-ahead fields, operation-trace labels, public disposition and claim boundary |
| gateRunPurpose | confirm design-artifact shape after source/checker read-ahead; not infer semantic acceptance |
| claimBoundary | structural PASS cannot accept T1 design or authorize T2 |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex orchestrator/spec-author role |
| Provider or surface | local private CVF workspace |
| Session or invocation | DARA-T1 architecture-readiness contract design, 2026-09-06 |
| Working directory | repository root |
| Command or tool surface | current-authority reads, exact source/symbol searches, `apply_patch`, focused structural gates and git |
| Target paths | this design artifact only |
| Allowed scope source | DARA-T0 accepted T1 entry plus operator instruction to continue |
| Before status evidence | HEAD `c9200c395`; P4-C1 active at `b9bdba712`; universal binding active at `a7953e0f4`; two parked Phase-04 files untracked |
| After status evidence | one pending-review DARA-T1 design; no template/checker/runtime mutation |
| Diff evidence | exact one-path design diff; parked files excluded and hash-preserved during gates/commit |
| Approval boundary | T1 design only; reviewer phase begins from frozen commit |
| Claim boundary | no independent review, T2 implementation, external invocation, finding repair, runtime/provider/live/public action |
| Agent type | orchestrator/spec author |
| Invocation ID | `dara-t1-architecture-readiness-contract-design-2026-09-06` |
| Expected manifest | this design artifact only |
| Actual changed set | this design artifact only |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private foundation contract design pending sequential review.

## Claim Boundary

This artifact freezes a proposed DARA-T1 contract for review. It does not
claim independent review, implemented enforcement, architecture correctness
for `WP-ARCH-003`, external-agent authority, changed MFRP eligibility, runtime
or provider behavior, public export, deployment, release, or production
readiness.
