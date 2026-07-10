# CVF Agent Work Order MSEA-R94-T0 Contract To Runtime 50 Row Inventory

Memory class: FULL_RECORD

Status: DISPATCH_READY

Batch ID: MSEA-R94-T0

Date: 2026-07-11

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `28d762c9c`

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

## Dispatch Prompt Envelope

Role route: `WORKER_MUST_NOT_COMMIT`

Role: delegated worker performing a read-only repository audit

Commit mode: `WORKER_MUST_NOT_COMMIT`

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R94_T0_CONTRACT_TO_RUNTIME_50_ROW_INVENTORY_2026-07-11.md`

Paired baseline: `docs/baselines/CVF_GC018_MSEA_R94_T0_CONTRACT_TO_RUNTIME_50_ROW_INVENTORY_2026-07-11.md`

Current-time notes: dispatch base `28d762c9c`; current matrix contains exactly
50 unique rows at lines 38-87; worker must capture the actual execution base.

Required first actions: read all Required First Reads, capture
executionBaseHead and status, confirm it equals the dispatched commit supplied
by the reviewer, count 50 unique matrix rows, then run pre-implementation.

Do-not-misread notes: this is a complete inventory, not an instruction to make
every row `PROVEN_CONNECTED`. Preserve honest partial, documentation-only,
unresolved-owner, and no-change outcomes. Capability is not execution; a test
file is not proof that it tests the cited implementation.

Return contract: create the audit Markdown, deterministic JSON evidence, and
worker return; run verification; leave every change uncommitted; return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R94-T0 --title "Contract To Runtime 50 Row Inventory" --date 2026-07-11 --base 28d762c9c --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic worker dispatch plus no-commit return profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Added exact 50-row schema, calibration rules, indirect-edge methods, output manifest, reviewer conversion, and roadmap trace; removed non-applicable live-run stubs. |
| checkerReadAheadConfirmation | Read all checker sources named in the Checker Source Read-Ahead Block. |
| docOnlyNewFields | rowId, matrixClaim, implementationStatus, invocationStatus, testPairingStatus, operatorEvidenceRouteStatus, finalDisposition, nextAction, confidence |
| claimBoundary | Dispatch packet only; no audit result or implementation claim. |

## Purpose

Produce a complete, source-backed contract-to-runtime inventory for all 50
Governance Control Matrix rows. The result must distinguish what is declared,
implemented, invoked, correctly tested, and routed to evidence/operator
surfaces, without mutating any inspected source.

## Authority Chain

| Authority | Evidence | Control |
|---|---|---|
| Operator | authorized continuation after R94 roadmap authoring | T0 only |
| Roadmap | `docs/roadmaps/CVF_MSEA_R94_SYSTEM_CHAIN_GAP_CLOSURE_ROADMAP_2026-07-11.md` | 50-row inventory before repair |
| Baseline | paired MSEA-R94-T0 GC-018 | allowed and forbidden scope |
| Matrix | `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` | row source and declared claims |
| Prior calibration | R90 Audit A Markdown and JSON | hypotheses to re-derive, not copy |
| Current source | runtime, checker, registry, workflow, hook, test, and evidence files | highest authority for execution facts |

## Agent Roles

The worker reads and writes only the three worker-owned outputs and must not
commit. The reviewer independently checks row reconciliation, challenges
overclaims and absence searches, performs allowed-scope repairs, creates the
completion review, commits material artifacts, and syncs session state later.

## Scope / Methodology

For each matrix row:

1. Copy the six matrix source fields without changing their meaning.
2. Resolve every cited primary-evidence path and owning symbol when applicable.
3. Trace implementation to real production use through direct callers,
   imports, registries, scenario records, parameterized commands, hook/autorun
   catalogs, workflows, lifecycle wrappers, or explicit documentation-only
   ownership.
4. Verify that cited tests exercise the cited implementation or record a
   pairing mismatch.
5. Trace the evidence/operator route only to the level actually proven.
6. Assign one terminal disposition with evidence, reason, confidence, and next
   action.

The audit may group shared invocation chains in reusable evidence records, but
each of the 50 rows must reference the exact record(s) that support its outcome.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| R90 Audit A accepted | `docs/reviews/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_COMPLETION_2026-07-10.md`; material `645df8b83` | SATISFIED |
| R91 freshness accepted | `docs/reviews/CVF_MSEA_R91_SYSTEM_CHAIN_MAP_AND_FRESHNESS_CONTROL_COMPLETION_2026-07-10.md`; material `017ae9718` | SATISFIED |
| R93 cleanup accepted | `docs/reviews/CVF_MSEA_R93_GOP_Y_CVF_STORAGE_CLEANUP_COMPLETION_2026-07-10.md`; material `0f05b7942` | SATISFIED |
| R94 roadmap exists | `docs/roadmaps/CVF_MSEA_R94_SYSTEM_CHAIN_GAP_CLOSURE_ROADMAP_2026-07-11.md`; material `383a273c8` | SATISFIED |

## Required First Reads

| Path | Read mode | Reason |
|---|---|---|
| `CVF_SESSION_MEMORY.md` | FULL_READ | front-door state |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | FULL_READ | canonical state |
| `AGENT_HANDOFF_V40_2026-07-10.md` | FULL_READ | active handoff |
| `docs/reference/guard_orientation/README.md` | FULL_READ | worker/reviewer guard routing |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | FULL_READ | literal-shape prevention |
| paired MSEA-R94-T0 baseline | FULL_READ | authority boundary |
| this work order | FULL_READ | execution contract |
| `docs/roadmaps/CVF_MSEA_R94_SYSTEM_CHAIN_GAP_CLOSURE_ROADMAP_2026-07-11.md` | FULL_READ | roadmap scope and dependencies |
| `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` | FULL_READ | 50-row source corpus |
| `docs/audits/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_2026-07-10.md` | FULL_READ | prior method and calibration |
| `docs/audits/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_EVIDENCE_2026-07-10.json` | FULL_READ | prior evidence schema and calibration |
| `docs/reference/system_chain/README.md` | FULL_READ | current five-lane owner |
| `docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json` | FULL_READ | current machine map and freshness inputs |

Advisory files under
`.private_reference/external_reviews/system_chain_gap_closure_2026-07-10/` may
be read for method/dissent context only. They are never Source Authority rows.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Matrix row columns | `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` | Control Matrix header, line 36 | `Control ID` | Governance Control Matrix | ACCEPT |
| Matrix row range and count | `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` | rows 38-87 | `GC-001` through `GC-050` | Governance Control Matrix | ACCEPT |
| Enforcement class semantics | `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` | Enforcement Classes, lines 24-32 | `RUNTIME_GUARD` | Governance Control Matrix | ACCEPT |
| T0 requires all-row classification | `docs/roadmaps/CVF_MSEA_R94_SYSTEM_CHAIN_GAP_CLOSURE_ROADMAP_2026-07-11.md` | R94-T0 section | `R94-T0` | MSEA-R94 roadmap | ACCEPT |
| Calibration record array | `docs/audits/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_EVIDENCE_2026-07-10.json` | CONTRACT_TO_RUNTIME object | `rowDispositions` | `cvf.msea_r90.audit_a.v1` | ACCEPT |
| Current map row contract | `docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json` | top-level chain records | `chainLinks` | system-chain map schema | ACCEPT |
| Worker-return enforcement marker | `governance/compat/check_worker_return_quality_gate.py` | module constants | `SELF_DECLARE_MARKER` | worker-return quality checker | ACCEPT |
| Dispatch source-verification enforcement | `governance/compat/check_work_order_dispatch_quality.py` | `main` and Source Verification validation | `main` | work-order dispatch checker | ACCEPT |

## New Doc-Only Fields

| Field | Required in Markdown | Required in JSON | Meaning |
|---|---|---|---|
| rowId | Yes | Yes | stable `GC-NNN` join key |
| matrixClaim | Yes | Yes | six source columns as a structured record |
| implementationStatus | Yes | Yes | existence and owning-symbol classification |
| invocationStatus | Yes | Yes | actual execution/use route classification |
| invocationMechanism | Yes | Yes | direct, registry, data-driven, hook, workflow, lifecycle, or documentation-only |
| testPairingStatus | Yes | Yes | cited-source/test relationship |
| operatorEvidenceRouteStatus | Yes | Yes | proven evidence and operator route |
| finalDisposition | Yes | Yes | terminal row outcome |
| nextAction | Yes | Yes | no-change, repair candidate, documentation correction, defer, or owner action |
| confidence | Yes | Yes | HIGH, MEDIUM, or LOW with reason |

## Current Runtime Freshness Verification

The worker must recompute every row from the captured executionBaseHead. R90
outcomes are calibration expectations only. Current source, generated command
data, registries, workflows, and hook catalogs outrank earlier reports.

## Negative Search And Collision Discipline

Every absence or non-invocation disposition must include:

- exact searched symbols and spelling variants;
- exact roots and file classes;
- commands or deterministic search method;
- treatment of tests, generated files, vendored files, archives, registries,
  scenario data, and parameterized commands;
- same-name collisions and why they are or are not authoritative;
- the strongest narrower claim supported by the search.

Do not convert a search miss into a universal absence claim.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`system chain contract runtime audit`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "system chain contract runtime audit" --role dispatcher --lifecycle-phase pre-dispatch --json`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Returned defect count | 0 |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | Explicit controls remain for generated edges, test-source pairing, collision handling, complete corpus accounting, and no-commit return. |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

route: MULTI_AGENT_MULTI_ROLE

rolePattern: MULTI_AGENT_MULTI_ROLE

phase: dispatch

baseHeadFor(phase): dispatchBaseHead=`28d762c9c`; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_MUST_CAPTURE_AT_CLOSURE

changedSetScope(phase): dispatch pair; then exactly the audit Markdown, audit
JSON, and worker return; reviewer-owned completion/closure paths later.

traceScope(phase, actor): dispatcher packet evidence; worker 50-row manifest,
searches, citations, reconciliation, tests, status; reviewer independent audit.

commitOwner(phase): worker must not commit; reviewer/closer owns material commit;
session-sync steward owns a later separate continuity commit.

crossBatchIsolation: Before status evidence: clean worktree at `28d762c9c`; no
T1-T4 implementation, matrix/source/checker/hook/Web, lifecycle, provider/live,
public, or session mutation by worker.

crossBatchIsolation: Before status evidence: clean worktree at `28d762c9c`; no unrelated product or governance work.

nextMoveSurfaces: reviewer updates only after accepted material commit.

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | MULTI_AGENT_MULTI_ROLE |
| phase | dispatch, worker execution, review/closure, session sync |
| baseHeadFor(phase) | dispatch `28d762c9c`; worker captures execution; reviewer captures closure |
| changedSetScope(phase) | exact phase-owned paths only |
| traceScope(phase, actor) | row ledger, source trace, commands, gates, diff/status |
| commitOwner(phase) | reviewer/closer, then session-sync steward |
| crossBatchIsolation | no unrelated material or session path in worker return |
| nextMoveSurfaces | reviewer-owned after material acceptance |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_MSEA_R94_T0_CONTRACT_TO_RUNTIME_50_ROW_INVENTORY_COMPLETION_2026-07-11.md`

reviewerOwnedClosurePaths: paired baseline; this work order; audit Markdown;
audit JSON; worker return; completion review.

reviewerAction: verify all 50 rows, challenge at least every non-invocation and
pairing-mismatch row, reconcile Markdown/JSON, repair only allowed-scope output
defects, convert statuses, commit material, run committed-range pre-closure,
then perform separate session sync.

pendingStatusTokensAllowedBeforeReview: COMPLETE_PENDING_REVIEW

## Intake Role Routing Decision

| Field | Value |
|---|---|
| Intake summary | current governed 50-row matrix plus repository execution evidence |
| Scope classification | bounded static repository audit |
| Risk sensitivity | overclaim, false absence, source/test mismatch, incomplete corpus |
| Selected role route | MULTI_AGENT_MULTI_ROLE |
| Escalation condition | unreadable source, non-unique IDs, unresolved row, scope mutation required |

## Worker Autonomy / No-Question Rule

Proceed without interruption for read-only exploration, helper creation within
owned outputs, evidence normalization, and allowed-scope repair. Stop only for
a fail condition or authority expansion.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order section | Worker evidence | Closure test | Status |
|---|---|---|---|---|
| classify all 50 rows | Scope and Execution Plan | 50-row Markdown/JSON ledger | exact 50/50 reconciliation | ACCEPT |
| distinguish implementation/invocation/test/evidence | New Doc-Only Fields and Evidence Requirements | per-row dimension records | required-field validator | ACCEPT |
| calibrate GC-001/009/011 | Execution Plan | fresh trace and delta from R90 | reviewer comparison | ACCEPT |
| no repair in T0 | Forbidden Scope | diff/status and claim boundary | changed-set audit | ACCEPT |
| select T1 candidates only from evidence | Acceptance Criteria | nextAction and risk ranking | reviewer decision | ACCEPT |

## Dual Agent Surface Matrix

| Agent surface | Role | Interface | Authority and risk boundary | Required evidence | Adapter boundary and disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | worker/reviewer | repository source and governed outputs | read-only worker, no commit | 50-row audit, JSON, worker return | repository-native; CONTRACT_ONLY |
| EXTERNAL_AGENT_CLI_MCP | N/A with reason: no adapter authorized | none | no ingress, execution, mutation, or authority | forbidden-scope confirmation | no adapter; N/A_WITH_REASON |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact: `docs/audits/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_EVIDENCE_2026-07-10.json`

priorVerificationAnchor: CONTRACT_TO_RUNTIME calibration records only

freshRecomputeRequired: all 50 rows from executionBaseHead

unicodePathHandling: use literal paths and UTF-8-safe readers; do not normalize unrelated filenames

extractedTextAuthority: current filesystem source is authoritative; extracted summaries are evidence aids only

R90 evidence may seed method and calibration comparisons but cannot supply a
current terminal outcome without fresh source confirmation.

## System Loop Interlock Routing

| Field | Value |
|---|---|
| Upstream output | 50-row audit Markdown and JSON |
| Interlock owner | R94 roadmap T0 -> T1 dependency |
| Trigger | reviewer accepts terminal row ledger |
| Downstream action | author separate repair packets for accepted candidates only |
| Forbidden shortcut | no direct mutation from worker findings |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| durableFoundationChange | new audit evidence only |
| ownerSurface | `docs/audits/` for audit pair; `docs/reviews/` for worker/reviewer packets |
| indexOrRegistryImpact | evaluate GC-051 corpus registry during review if checker requires it |
| duplicateSurfaceCheck | no new matrix, registry, or freshness owner |
| claimBoundary | storage placement does not establish semantic correctness |

## Corpus Completeness And Report Integrity

- Corpus task class: GOVERNANCE_CONTROL_MATRIX_50_ROW_AUDIT.
- Corpus root: the Control Matrix table plus per-row current source evidence.
- Snapshot time: worker execution start at captured executionBaseHead.
- Enumeration command: filesystem-backed direct file reads using a UTF-8-safe deterministic parser for the exact `GC-NNN` first-cell shape.
- Manifest artifact or inline manifest: audit JSON `sourceManifest` and `matrixRows`.
- Manifest hash: SHA-256 over normalized manifest records with algorithm recorded.
- Processing ledger artifact or inline ledger: audit JSON `rowRecords`.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=50 ledger_terminal=50 exclusions=0 unresolved=0.
- Unresolved files: 0 at completion.
- Declared exclusions: none at dispatch; any later exclusion must be explicit, counted, and reasoned.
- Unreadable or unsupported files: none at dispatch; any later unreadable item blocks complete status.
- Aggregation check: Markdown and JSON row IDs, dispositions, counts, and hash match.
- Drift check: record executionBaseHead and relevant source fingerprints.
- Output traceability: every row links to source evidence records.
- Adversarial verification: direct import, data-driven registry, generated command, same-name collision, and test-pairing cases checked.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Corpus scan or extraction intake |
| Chain map route | CVF source verification -> bounded audit -> reviewer decision |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | R94 audit pair and current matrix owners |
| Disposition | advisory files may inform dissent/method only |
| Claim boundary | no advisory file is canonical authority |

## Write Ownership

Worker-owned paths:

- `docs/audits/CVF_MSEA_R94_T0_CONTRACT_TO_RUNTIME_50_ROW_INVENTORY_2026-07-11.md`
- `docs/audits/CVF_MSEA_R94_T0_CONTRACT_TO_RUNTIME_50_ROW_INVENTORY_EVIDENCE_2026-07-11.json`
- `docs/reviews/CVF_MSEA_R94_T0_CONTRACT_TO_RUNTIME_50_ROW_INVENTORY_WORKER_RETURN_2026-07-11.md`

Every other path is read-only. The completion review, baseline, work order,
session state, and commits are reviewer-owned.

## Worker Output Checker Read-Ahead Mandate

Before writing outputs, read checker source as applied to each output path.
The audit Markdown must satisfy audit/review structural and finding-learning
requirements; JSON must be deterministic and reconciled; the worker return
must satisfy all current worker-return markers and headings. Do not copy a
heading checklist as fake output sections.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_finding_to_governance_learning.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Dispatch Prompt Envelope`; `Source Verification Block`; `Agent Handoff Contract Control Block`; `Reviewer Closure Conversion`; `Worker Return Packet Shape Contract`; `Public Export Disposition` |
| gateRunPurpose | confirmation and evidence after direct source verification; not first discovery |
| claimBoundary | dispatch and worker-output shape only; no row result predetermined |

## Planned Worker Fulfillment Manifest

| Path | Exists at dispatch | Worker action |
|---|---|---|
| audit Markdown path named in Write Ownership | No | create complete human ledger |
| audit JSON path named in Write Ownership | No | create deterministic evidence companion |
| worker return path named in Write Ownership | No | create no-commit return packet |
| paired baseline | Yes | read-only |
| this work order | Yes | read-only |
| Governance Control Matrix | Yes | read-only source corpus |

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The return must include the self-declaration marker and work-order response
marker required by the current checker, followed by real sections for Purpose,
Target / Source, Scope / Methodology, Findings / Position, Risk / Corrective
Action, Decision / Recommendation / Disposition, Checker Source Read-Ahead
Block, git status, Changed Files, No-Commit Statement, Corpus Completeness,
Epistemic Process, Finding-To-Governance Learning, Agent Operation Trace, Delta
Execution Claim Boundary, Public Export Disposition, and Claim Boundary.

All scaffold placeholders must be replaced with actual evidence. The return
must state `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` and must not claim
the working tree is clean while its three output files are uncommitted.

## Pre-Flight Checks

1. Capture `git rev-parse --short HEAD` as executionBaseHead.
2. Capture `git status --short --untracked-files=all`.
3. Confirm 50 unique matrix rows from `GC-001` through `GC-050`.
4. Confirm all three worker output paths are absent.
5. Read output-applicable checker sources.
6. Run pre-implementation with the real execution base.

## Evidence Requirements

For each row, record:

- all six matrix source fields;
- implementation status with file, symbol, and citation;
- invocation status and mechanism with real caller/registry/workflow evidence;
- test-pairing status with import or execution evidence;
- operator/evidence-route status without inference from route existence;
- collisions, exclusions, and negative-search method where applicable;
- final disposition, reason, next action, risk, and confidence;
- source fingerprint or aggregate evidence record reference.

Required final-disposition vocabulary:

- `PROVEN_CONNECTED`;
- `IMPLEMENTED_NOT_INVOCATION_PROVEN`;
- `INVOKED_TEST_PAIRING_MISMATCH`;
- `CONTRACT_ONLY_WITH_REASON`;
- `DOCUMENTATION_DRIFT`;
- `SOURCE_OWNER_UNRESOLVED_WITH_SEARCH_EVIDENCE`.

The worker may propose a narrower additional enum only if both artifacts define
it identically and explain why the existing vocabulary cannot represent the
evidence. The reviewer must approve any added enum.

## Execution Plan

| Step | Action | Required evidence |
|---|---|---|
| 1 | capture base/status and run pre-implementation | command output |
| 2 | parse and hash the 50-row matrix corpus | count, unique IDs, hash |
| 3 | re-derive GC-001, GC-009, GC-011 | fresh trace and R90 delta |
| 4 | trace GC-002 through GC-050 by enforcement class and owner family | per-row evidence plus reusable chain records |
| 5 | perform indirect-edge and collision searches | commands, scopes, exclusions, collision dispositions |
| 6 | verify cited test/source pairing | imports, test targets, or explicit absence |
| 7 | trace evidence/operator routes | bounded route evidence |
| 8 | write and reconcile Markdown/JSON | exact 50/50 match |
| 9 | complete worker return and gates | actual first/final results, diff/status |
| 10 | stop without commit | no-commit statement and final status |

## Acceptance Criteria

- [ ] Exactly 50 unique rows are present in both audit artifacts.
- [ ] Every row preserves the six matrix source fields.
- [ ] Every row has independent implementation, invocation, test-pairing, and
      operator/evidence-route evidence or a bounded reason.
- [ ] GC-001, GC-009, and GC-011 are freshly re-derived.
- [ ] All indirect execution mechanisms are considered before non-invocation.
- [ ] Every same-name collision is explicitly dispositioned.
- [ ] Every row has one terminal disposition and one next action.
- [ ] Markdown and JSON counts, row IDs, dispositions, and manifest hash agree.
- [ ] Repair candidates are risk-ranked; no implementation is performed.
- [ ] Worker return records actual uncommitted status and no commit.
- [ ] Required governance gates pass or the return is blocked honestly.

## Verification Commands

```powershell
$executionBaseHead = git rev-parse --short HEAD
git status --short --untracked-files=all
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base $executionBaseHead --head HEAD
python governance/compat/check_markdown_structural_completeness.py --base $executionBaseHead --head HEAD --enforce
python governance/compat/check_finding_to_governance_learning.py --base $executionBaseHead --head HEAD --enforce
python governance/compat/check_corpus_completeness_report_integrity.py --base $executionBaseHead --head HEAD --enforce
python governance/compat/check_agent_operation_trace.py --base $executionBaseHead --head HEAD --enforce
python governance/compat/check_delta_execution_claim_boundary.py --base $executionBaseHead --head HEAD --enforce
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/generate_corpus_scan_registry.py --check
git diff --check
git status --short --untracked-files=all
```

The worker must also run and record a deterministic reconciliation command that
loads the JSON and proves 50 unique IDs, exact Markdown/JSON disposition match,
zero unresolved rows, and matching manifest hash.

## Epistemic Process Block

### Expected Result / Prediction

The matrix likely contains a mixture of proven runtime guards, data-driven CI
gates, documentation-only contracts, citation drift, and some rows whose
invocation or test pairing is weaker than the matrix wording suggests.

### Evidence Comparison

R90 found one proven, one invocation-unproven, and one test-mismatched row in a
three-row sample. T0 tests whether that pattern generalizes without assuming it
does.

### Contradiction Or Gap Disposition

Current source wins over matrix prose and prior reports for execution facts.
The audit must narrow claims rather than force consensus when evidence differs.

### Claim Update

Only the reviewer-accepted 50-row ledger may select R94-T1 repair candidates.

## Finding-To-Governance Learning Disposition

If a repeated audit-method defect appears across rows, classify it with a real
defect class such as `METHOD_GAP`, `RULE_GAP`, or `MACHINE_GATE_GAP`, name the
learning lane, and propose a control action. Do not implement governance
hardening in T0. A one-row source defect is not automatically an ADIF entry.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | delegated worker role |
| Provider or surface | local private provenance repository |
| Session or invocation | MSEA-R94-T0 50-row audit |
| Working directory | repository root |
| Command or tool surface | read-only source reads, searches, parsing, worker-owned file writes, tests, governance gates |
| Target paths | three worker-owned output paths |
| Allowed scope source | paired GC-018 baseline and this work order |
| Before status evidence | clean worktree at `28d762c9c`; worker must recapture executionBaseHead and status at start |
| After status evidence | three uncommitted outputs and actual status |
| Diff evidence | `git diff --name-status`; `git status --short --untracked-files=all` |
| Approval boundary | static inventory only |
| Claim boundary | no source mutation, implementation, public, provider, lifecycle, or session claim |
| Agent type | worker |
| Invocation ID | worker records stable invocation identifier |
| Expected manifest | exact three worker-owned outputs |
| Actual changed set | worker records exact paths |
| Manifest delta | MATCH required for complete return |
| Deletion or rename disposition | N/A with reason: none authorized |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | static repository evidence for 50 matrix rows |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: no live/runtime receipt required for a static audit |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source reads, caller/registry/workflow searches, test pairing, reconciliation, and gates |
| invocationBoundary | evidence of existing repository invocation only; worker invokes no governed product action |
| interceptionBoundary | no provider, IDE, MCP, Web, adapter, or public interception claim |
| claimLanguage | per-row bounded dispositions at captured executionBaseHead |
| forbiddenExpansion | no matrix/runtime/test/checker/hook/workflow/Web/lifecycle/public/session mutation |

## Review Gate

Reviewer must inspect all rows marked non-invoked, mismatched, unresolved, or
repair-candidate; sample at least one real source citation for every other owner
family; rerun reconciliation and reviewer-fast gates; reject aggregate-only or
file-existence-only proof.

## Closure Checklist

- [ ] 50/50 row reconciliation accepted.
- [ ] Calibration rows independently confirmed or corrected.
- [ ] Negative searches and collisions reviewed.
- [ ] Markdown/JSON schema and hash match.
- [ ] Changed set contains only authorized outputs plus reviewer-owned closure.
- [ ] No implementation or source mutation occurred.
- [ ] Material and session commits remain separate.
- [ ] Roadmap T1 remains undispatched until reviewer acceptance.

## Return-To-Orchestrator Conditions

Return immediately if row count is not 50, control IDs collide, current source
cannot support a terminal row disposition, a required output needs a new owner
surface outside scope, or any repair/source mutation is required to complete
the inventory.

## Operator Checkpoint

No operator checkpoint is required during read-only T0 execution. After T0
reviewer acceptance, the operator/reviewer chooses whether and how to package
T1 repair candidates. T3 operator-surface implementation remains separately
value-gated.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance audit. No public artifact or public claim is
authorized.

## Claim Boundary

This work order authorizes a complete static inventory only. It does not
predetermine row outcomes, authorize repair, declare the system chain closed,
or change matrix, runtime, tests, governance, lifecycle, Web, provider, public,
or session state.
