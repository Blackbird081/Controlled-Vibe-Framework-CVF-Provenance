# CVF Agent Work Order MSEA R90 System Chain Audit A Completion

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work-order

Date: 2026-07-10

Batch ID: MSEA-R90

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker role

Reviewer/closer: reviewer/closer role

## Dispatch Prompt Envelope

Role: delegated worker for MSEA-R90. A separate reviewer/closer owns closure.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_COMPLETION_2026-07-10.md`

Commit mode: WORKER_MUST_NOT_COMMIT

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

Current-time notes: Audit A correction is accepted only as advisory input;
all accepted facts must be recomputed from current CVF-owned sources.

Do-not-misread notes: do not build Deliverable B, implement freshness controls,
move the advisory directory, modify source/checkers/session state, or commit.

Required first actions: read startup front doors, guard orientation, literal
gotchas, the paired GC-018 baseline, this packet, all Required First Reads, and
the checker sources in the read-ahead block; then capture executionBaseHead and
run pre-implementation.

Return contract: create the two Audit A artifacts and worker return, run the
required component gates, leave all changes uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` with exact changed paths,
commands, results, and unchanged HEAD.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R90 --title "System Chain Audit A Completion" --date 2026-07-10 --base 3bdb6640a --commit-mode WORKER_MUST_NOT_COMMIT --dependency "SATISFIED: operator authorized correction repair and a fresh bounded Audit A completion packet on 2026-07-10." --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker return |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced placeholders with source-backed Audit A instructions, output schema, evidence rules, and reviewer boundary. |
| checkerReadAheadConfirmation | Read all checker sources named in the Checker Source Read-Ahead Block. |
| docOnlyNewFields | chainLink, claimedBy, implementedBy, invokedBy, testedBy, evidenceOwner, operatorSurface, evidenceClass, freshnessDisposition |
| claimBoundary | Docs/evidence-only Audit A worker dispatch. |

## Purpose

Complete a truthful, source-backed Audit A that traces CVF from doctrine to
contract, contract to runtime, enforcement to evidence, and evidence to
operator-visible surfaces. Reverify the runtime-to-enforcement row and return
one human audit plus one deterministic machine-evidence companion.

## Authority Chain

- Operator instruction on 2026-07-10: repair the correction evidence and
  author a governed worker order.
- Active state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V40_2026-07-10.md`.
- Baseline: `docs/baselines/CVF_GC018_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_COMPLETION_2026-07-10.md`.
- Existing system-audit input: `docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md`.
- Current lifecycle decision: `docs/reference/CVF_MSEA_R72F_FIRST_RETIREMENT_OR_CONSOLIDATION_PILOT_DECISION_MATRIX_2026-07-08.md`.

Authority precedence: current source and canonical contracts outrank prior
reviews, historical traces, temporary reports, and provider-specific guidance.
The existing FPC-T1 matrix is an input to reconcile, not authority to copy.

## Agent Roles

- Dispatcher: dispatcher role.
- Worker: delegated worker role; the operator assigns the execution surface
  separately from this role-based contract.
- Reviewer/closer: reviewer/closer role.
- Session-sync steward: reviewer/closer only if accepted closure changes mode
  or next move.

## Scope / Methodology

Use filesystem-backed direct reads, JSON parsing, Python AST where relevant,
exact `rg` searches, and current Git metadata. Build a declared audit manifest;
trace each edge through source, invocation, test/evidence, and operator output;
record contradictions; and keep structural, manual, historical, machine-checked,
and unresolved evidence classes separate.

Audit lanes:

1. Doctrine to contract.
2. Contract to runtime.
3. Runtime to enforcement revalidation.
4. Enforcement to evidence completion, including all twelve prior path
   candidates.
5. Evidence to operator surface.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| Fresh operator authorization | Operator instruction exists in this session. | Paired GC-018 and work order remain bounded and source-verified. | PASS |
| Corrected invocation interpretation | Workflow, runner, registry, posture runner, and R72F sources are current and directly readable. | Worker recomputes the full edge from source. | PASS |
| Output placement | Audit and evidence artifacts have no existing path collision. | Worker creates only planned paths. | PASS |

## Required First Reads

| Source | Action | Why |
|---|---|---|
| `CVF_SESSION_MEMORY.md` | FULL_READ | Current mode and next move. |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | FULL_READ | Canonical state. |
| `AGENT_HANDOFF_V40_2026-07-10.md` | FULL_READ | Active continuity and parked checkpoint. |
| `docs/reference/guard_orientation/README.md` | FULL_READ | Task and role guard routing. |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | FULL_READ | Pre-write shape traps. |
| Paired MSEA-R90 GC-018 baseline | FULL_READ | Allowed and forbidden scope. |
| `ECOSYSTEM/doctrine/CVF_LAYER_MODEL.md` | FULL_READ | Official L0-L6 doctrine. |
| `ARCHITECTURE.md` | FULL_READ | Current architecture and evidence posture claims. |
| `docs/reference/CVF_ARCHITECTURE_DIAGRAMS.md` | FULL_READ | Diagram claims requiring current reconciliation. |
| `docs/reference/CVF_MODULE_INVENTORY.md` | FULL_READ | Module and evidence-owner claims. |
| `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` | FULL_READ | Guard-to-owner and stale-path claims. |
| `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | FULL_READ | Operator lookup paths and boundaries. |
| `docs/CVF_CORE_KNOWLEDGE_BASE.md` | FULL_READ | Core placement and link claims. |
| `docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md` | FULL_READ | Prior audit input and unresolved/stale assertions. |
| `docs/reference/CVF_MSEA_R72F_FIRST_RETIREMENT_OR_CONSOLIDATION_PILOT_DECISION_MATRIX_2026-07-08.md` | FULL_READ | Later lifecycle authority. |
| `docs/reference/CVF_CONFORMANCE_SCENARIOS.json` | FULL_READ | Data-driven conformance commands. |
| `scripts/run_cvf_cross_extension_conformance.py` | FULL_READ | Registry loader and scenario execution. |
| `scripts/run_cvf_packet_posture_gate_conformance.py` | FULL_READ | Parameterized checker execution. |
| Temporary correction artifacts under the operator advisory directory | READ | Advisory context only; never cite as CVF authority. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Official layer vocabulary is L0 through L6. | VALUE_SET | canonical contract - ECOSYSTEM/doctrine/CVF_LAYER_MODEL.md | Layer Overview, lines 18-32 | `Layer Overview` | doctrine layer model | ACCEPT |
| Workflow currently invokes the cross-extension conformance runner. | RUNTIME_BEHAVIOR | `.github/workflows/documentation-testing.yml` | lines 734-789 | `conformance-artifact-consistency` | documentation testing workflow | ACCEPT |
| Runner declares, loads, and executes the canonical scenario registry. | RUNTIME_BEHAVIOR | `scripts/run_cvf_cross_extension_conformance.py` | lines 20, 204, 393 | `SCENARIO_REGISTRY` | conformance runner | ACCEPT |
| Registry owns CF-076 through CF-084 commands. | VALUE_SET | `docs/reference/CVF_CONFORMANCE_SCENARIOS.json` | CF-076 through CF-084 | `scenarios` | scenario registry | ACCEPT |
| Posture runner resolves and executes a selected gate. | RUNTIME_BEHAVIOR | `scripts/run_cvf_packet_posture_gate_conformance.py` | lines 42-55 | `main` | packet posture runner | ACCEPT |
| R72F later decision is retirement hold, not retirement authorization. | LITERAL_INVARIANT | `docs/reference/CVF_MSEA_R72F_FIRST_RETIREMENT_OR_CONSOLIDATION_PILOT_DECISION_MATRIX_2026-07-08.md` | Decision Matrix and Claim Update | `RETIREMENT_HOLD_SOURCE_GAP` | R72F decision matrix | ACCEPT |
| Existing FPC-T1 audit explicitly denies a complete-plane claim. | LITERAL_INVARIANT | `docs/reference/CVF_FPC_T1_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_AUDIT_MATRIX_2026-06-13.md` | Claim Boundary | `Claim Boundary` | FPC-T1 audit matrix | ACCEPT |
| Work-order source verification requires exact current source or canonical contract. | LITERAL_INVARIANT | `docs/reference/work_order_template/CVF_WORK_ORDER_SOURCE_VERIFICATION_ADDENDUM.md` | Source Priority | `Source Priority` | source-verification addendum | ACCEPT |

Existing paths verified: all Required First Reads except the explicitly temporary
advisory set were verified before dispatch.

Planned new paths clearly marked as NEW: Audit A Markdown, Audit A JSON evidence,
worker return, and reviewer completion paths named below.

Canonical role/type values verified from: handoff boundary checker route tokens
and work-order template role vocabulary.

Canonical template or pack IDs verified from: worker-return full-gate standard.

Runtime/source facts verified from current source or canonical contract: CI and
conformance chain facts in the Source Verification Block.

Completion review facts used only when no runtime/source contract exists:
R72F lifecycle decision and FPC-T1 bounded prior audit posture.

Draft-only tokens that appear nowhere else in repo: MSEA-R90 artifact IDs and
the new Audit A JSON schema fields listed below.

Same-token collisions with different meaning: none found for the new MSEA-R90
artifact IDs.

Any missing or ambiguous source fact: none at dispatch; unresolved Audit A
edges are the worker's evidence-classification target, not assumed facts.

## New Doc-Only Fields

| New doc-only field | Purpose | Not sourced from runtime? | Runtime claim blocked? | Validation expectation |
|---|---|---|---|---|
| chainLink | Stable edge ID shared by Markdown and JSON. | Yes | Yes | Exact cross-artifact match. |
| claimedBy | Canonical claim source. | Yes | Yes | Path plus line, section, or symbol. |
| implementedBy | Contract/source owner. | Yes | Yes | Existing path or explicit bounded disposition. |
| invokedBy | Automatic, indirect, wrapper, or manual invocation owner. | Yes | Yes | Exact caller chain. |
| testedBy | Test, scenario, command, or historical evidence. | Yes | Yes | Current or historical class stated. |
| evidenceOwner | Current evidence artifact owner. | Yes | Yes | Freshness checked. |
| operatorSurface | Operator-visible destination. | Yes | Yes | Existing route/readout or explicit absence. |
| evidenceClass | Evidence strength classification. | Yes | Yes | Allowed enum in audit. |
| freshnessDisposition | Current/stale/superseded/missing/historical state. | Yes | Yes | Current HEAD recomputation. |

## Current Runtime Freshness Verification

Worker must recompute current workflow, runner, registry, import, test, evidence,
and operator-surface edges. Prior report counts and statuses are predictions,
not reusable proof. Record current HEAD, script/config hashes where used, and
all source lines in the JSON companion.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Artifact path collision | Pre-dispatch command `rg --files --hidden --no-ignore docs CVF_SESSION | rg 'MSEA[_-]R90|SYSTEM_CHAIN_AUDIT_A_COMPLETION'` returned none. | PASS |
| Missing-path candidate | Re-run `Test-Path` and `rg --files --hidden --no-ignore` for the H2 completion candidate, then search archive and supersession surfaces. | RECOMPUTE_REQUIRED |
| Stale-path candidates | For every candidate, search exact basename in active and archive roots before disposition. | RECOMPUTE_REQUIRED |
| Temporary-input collision | Provider-named temporary reports may describe the same edge but are advisory only. | PASS; CVF source wins. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`system-chain audit`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "system-chain audit" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | N/A with reason: exact query returned no entries. |
| Dispatch impact | Indirect registry edges, authority precedence, and freshness recomputation are explicit controls despite no ADIF match. |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

route: MULTI_AGENT_MULTI_ROLE

rolePattern: MULTI_AGENT_MULTI_ROLE

phase: dispatch, worker execution, reviewer closure, optional session sync

baseHeadFor(phase): dispatchBaseHead=`3bdb6640a`; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_MUST_CAPTURE_AT_CLOSURE

changedSetScope(phase): dispatch pair; worker Audit A pair plus worker return;
reviewer-owned closure paths only

traceScope(phase, actor): exact reads, commands, paths, line evidence, diffs,
and per-role base anchors

commitOwner(phase): worker commit forbidden; reviewer/closer owns any accepted
material commit

crossBatchIsolation: no B, freshness implementation, cleanup, session, public,
runtime, or R72F lifecycle mutation in the worker batch

nextMoveSurfaces: reviewer updates continuity only if accepted closure changes
current mode or next allowed move

dispatchBaseHead: `3bdb6640a`

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

closureBaseHead: REVIEWER_MUST_CAPTURE_AT_CLOSURE

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_COMPLETION_2026-07-10.md`

reviewerOwnedClosurePaths:

- `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_COMPLETION_2026-07-10.md`
- `docs/reviews/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_COMPLETION_WORKER_RETURN_2026-07-10.md`
- `docs/reviews/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_COMPLETION_2026-07-10.md`
- `docs/audits/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_2026-07-10.md`
- `docs/audits/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_EVIDENCE_2026-07-10.json`

pendingStatusTokensAllowedBeforeReview: COMPLETE_PENDING_REVIEW,
IMPLEMENTATION_COMPLETE_PENDING_REVIEW, DRAFT, HOLD_*

forbiddenClosedEquivalentResidue: COMPLETE_PENDING_REVIEW, NOT_EXECUTED_YET,
WORKER_RETURNS_PENDING, PRE_CLOSURE_NOT_RUN, FAIL_EXPECTED_PENDING_FINALITY,
DISPATCHED as current status

predecessorClosureFactSource: stable completion/review artifact, not mutable
active session current mode

## Intake Role Routing Decision

| Field | Value |
|---|---|
| Intake summary | Operator-provided adversarial scout and correction context requiring CVF-native source revalidation. |
| Scope classification | Documentation and machine-readable evidence audit only. |
| Risk sensitivity | Stale authority, indirect invocation, false broken-chain claims, and public overclaim risk. |
| Selected role route | MULTI_AGENT_MULTI_ROLE |
| Escalation condition | Required CVF authority missing, contradictory current sources, or need for forbidden mutation. |

## Worker Autonomy / No-Question Rule

Proceed without operator confirmation for direct reads, searches, JSON parsing,
AST inspection, evidence-table repair, deterministic formatting, and required
gate reruns inside Write Ownership. Return only for a source contradiction,
forbidden-scope requirement, claim-boundary expansion, destructive action,
public action, provider/live need, or missing authority that prevents a bounded
verdict.

## Roadmap-To-Work-Order Trace Matrix

N/A with reason: MSEA-R90 is authorized directly by operator instruction and
the paired GC-018 baseline, not by a new roadmap. The baseline requirements are
mapped below for closure-diff purposes.

| Baseline requirement | Work-order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| Doctrine to contract | Execution Plan | Audit A edge rows and JSON records | source-line reconciliation | ACCEPT |
| Contract to runtime | Execution Plan | Audit A edge rows and JSON records | symbol/caller reconciliation | ACCEPT |
| Runtime to enforcement revalidation | Source Verification and Execution Plan | indirect and manual invocation records | workflow/registry/AST evidence | ACCEPT |
| Enforcement to evidence | Execution Plan | twelve candidate dispositions | active/archive basename search | ACCEPT |
| Evidence to operator surface | Execution Plan | operatorSurface records | route/readout existence checks | ACCEPT |
| No B or maintenance implementation | Forbidden Scope | claim boundary | changed-set review | ACCEPT |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | Audit A Markdown and JSON evidence | Read-only analysis; worker cannot commit or mutate control surfaces. | Worker return and reviewer completion. | Repository artifacts only. | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | N/A with reason: no adapter is authorized. | No ingress, auth, approval, receipt, raw-data, mutation, or public claim. | Forbidden Scope. | External adapter remains outside MSEA-R90. | N/A_WITH_REASON |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact: temporary scout/correction reports and the FPC-T1
audit are advisory inputs only.

priorVerificationAnchor: current dispatch HEAD `3bdb6640a`; prior evidence
anchors must be recorded individually when historical proof is used.

freshRecomputeRequired: YES

unicodePathHandling: use literal repo-relative paths and UTF-8-safe readers
with replacement for decoding errors; authored governed artifacts remain ASCII.

extractedTextAuthority: SOURCE_AUTHORITY

## System Loop Interlock Routing

| Field | Value |
|---|---|
| Upstream loop | Current CVF doctrine, contract, runtime, enforcement, evidence, and operator surfaces. |
| Upstream output | MSEA-R90 Audit A Markdown and JSON evidence. |
| Downstream loop | Deliverable B design, then maintenance/freshness planning. |
| Downstream input | Reviewer-accepted Audit A only. |
| Finding route | New reusable defects go through Finding-To-Governance disposition; stale links receive owner and next action. |
| Mutation boundary | No downstream work starts automatically and no control surface is mutated in this tranche. |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | Dated audit and review evidence in existing governed path families; no new stable reference foundation. |
| Storage decision | Human Audit A and machine JSON companion stay together under the existing audits owner; worker return stays under the existing reviews owner. |
| Existing aggregate impact | None; this tranche does not create or edit a generated aggregate. |
| Generated state impact | None; no session or workspace state change. |
| Durable governance boundary | A later maintenance packet may create a stable front door, generator, and freshness checker only with fresh authorization. |

## Corpus Completeness And Report Integrity

- Corpus task class: BOUNDED_REPOSITORY_SYSTEM_CHAIN_AUDIT.
- Corpus root: declared manifest of CVF-governed source surfaces; not the whole repository.
- Snapshot time: worker records UTC and current HEAD at execution start.
- Enumeration command: explicit manifest paths plus `rg --files --hidden --no-ignore` within each declared source root.
- Manifest artifact or inline manifest: Audit A JSON `sourceManifest`.
- Manifest hash: worker computes SHA-256 over normalized manifest records.
- Processing ledger artifact or inline ledger: Audit A JSON `chainEdges` and `pathDispositions`.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=0 ledger_terminal=0 exclusions=0 unresolved=0 at dispatch; worker replaces these dispatch-zero values with current execution counts.
- Unresolved files: 0 at dispatch because corpus processing has not started; worker records the actual numeric count and blocks complete-A when nonzero.
- Declared exclusions: archives are searched for stale targets but are not treated as current authority.
- Unreadable or unsupported files: count and list explicitly.
- Aggregation check: Markdown and JSON edge IDs and dispositions match.
- Drift check: current HEAD, source lines, and hashes recorded.
- Output traceability: every audit claim maps to a source manifest record.
- Adversarial verification: authority precedence, indirect registry commands, manual controls, stale links, and absent operator surfaces sampled.
- Corpus verdict: PARTIAL

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | advisory scout -> CVF-owned source verification -> Audit A |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | MSEA-R90 Audit A artifacts |
| Disposition | ADAPT method lessons only; reject temporary reports as authority. |
| Claim boundary | All accepted facts come from CVF-governed sources. |

## Write Ownership

Worker-owned paths:

- `docs/audits/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_2026-07-10.md`
- `docs/audits/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_EVIDENCE_2026-07-10.json`
- `docs/reviews/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_COMPLETION_WORKER_RETURN_2026-07-10.md`

Write mode: create-only for planned outputs; modify-created-file for
allowed-scope remediation before handoff.

Forbidden paths: every other repository path, including the paired dispatch
artifacts, current source, workflows, checkers, session state, active handoff,
public-sync, and the operator advisory directory.

## Worker Output Checker Read-Ahead Mandate

Before authoring the audit, JSON, or worker return, read checker source for the
output path family and content triggers. For the review artifact, derive the
review heading groups, trace fields, Delta block, public disposition,
epistemic fields, corpus fields, finding disposition, and no-commit evidence
shape before writing. Do not use the dispatch checklist as a substitute.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Dispatch Prompt Envelope`; `Source Verification Block`; `ADIF Defect Registry Disclosure`; `Agent Handoff Contract Control Block`; `Reviewer Closure Conversion`; `Worker Return Packet Shape Contract`; `Agent Operation Trace Block`; `Delta Execution Claim Boundary Control Block`; `Public Export Disposition` |
| gateRunPurpose | Confirmation and evidence following direct checker-source review, not first discovery. |
| claimBoundary | Dispatch and planned worker-output shape only; semantic Audit A truth remains worker and reviewer responsibility. |

## Planned Worker Fulfillment Manifest

| Artifact | Required worker action | Required at handoff |
|---|---|---|
| `docs/audits/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_2026-07-10.md` | Create human Audit A with complete edge matrix, source manifest, findings, risks, disposition, and claim boundary. | Yes |
| `docs/audits/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_EVIDENCE_2026-07-10.json` | Create deterministic machine companion with schema version, HEAD, hashes, source lines, edges, path dispositions, and reconciliation counts. | Yes |
| `docs/reviews/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_COMPLETION_WORKER_RETURN_2026-07-10.md` | Create no-commit return with commands, changed set, gates, contradiction handling, and exact pending status. | Yes |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_COMPLETION_WORKER_RETURN_2026-07-10.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required worker-return section names include Purpose, Target / Source, Scope /
Methodology, Findings / Position, Risk / Corrective Action, Decision /
Disposition, Checker Source Read-Ahead Block, External Knowledge Intake
Routing, Epistemic Process Block, Agent Operation Trace Block, Delta Execution
Claim Boundary Control Block, Public Export Disposition, Corpus Completeness
And Report Integrity, Finding-To-Governance Learning Disposition, Claim
Boundary, Changed Files, Command Evidence, and No-Commit Statement.

## Pre-Flight Checks

Worker captures a fresh execution anchor before edits and runs:

```powershell
git rev-parse --short HEAD
git status --short --untracked-files=all
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 3bdb6640a --head HEAD
python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_COMPLETION_WORKER_RETURN_2026-07-10.md --title "MSEA R90 System Chain Audit A Completion Worker Return"
```

The scaffold command runs before long-form worker-return drafting. A failed
pre-implementation gate blocks edits unless the failure is an allowed-scope
packet-shape defect the worker can repair without editing dispatcher-owned
paths; otherwise return `BLOCKED_WITH_REASON`.

## Evidence Requirements

For every chain edge, record:

- Claim.
- Command or direct read.
- Result.
- Key path plus line, section, or symbol.
- Evidence class.
- Freshness disposition.
- Verdict.

The audit must distinguish current execution from historical PASS evidence,
manual controls from automatic triggers, file existence from invocation,
documentation claims from runtime symbols, and operator visibility from raw
backend output.

## Execution Plan

1. Capture executionBaseHead, current status, manifest roots, and relevant
   source hashes. Stop on unexpected tracked changes or missing dispatch
   authority.
2. Reverify the complete runtime-to-enforcement path, including all indirect
   registry hops, exact source lines, historical evidence, and manual gates.
3. Trace doctrine L0-L6 claims to current contract owners. Mark missing or
   illustrative mappings honestly; do not force one-to-one folder mappings.
4. Trace selected canonical contracts to runtime symbols, callers, and tests.
   Separate contract-only, implemented, invoked, and tested states.
5. Recompute the one missing and eleven stale-path candidates. Search active,
   archive, successor, and supersession surfaces before final disposition.
6. Trace evidence owners to real operator-visible readouts, docs, CLI, Web, or
   explicit absent surfaces. Do not infer visibility from backend existence.
7. Reconcile all rows into the Markdown and deterministic JSON companion;
   compare edge IDs, statuses, counts, and claim boundaries.
8. Complete the worker return, run all verification commands following the
   last edit, record actual pending paths, and hand off without commit.

## Acceptance Criteria

- [ ] All five chain lanes have terminal, source-backed rows.
- [ ] Runtime-to-enforcement correction includes exact workflow, registry,
      runner, checker, and per-checker historical evidence lines.
- [ ] Doctrine-to-contract rows use L0-L6 authority and do not reuse provider
      guidance.
- [ ] Contract-to-runtime rows cite current symbols/callers/tests or use a
      bounded non-implementation disposition.
- [ ] All twelve evidence-path candidates have current dispositions and owner
      actions; Markdown and JSON agree.
- [ ] Evidence-to-operator rows prove a real surface or explicitly record its
      absence.
- [ ] JSON is deterministic, schema-versioned, secret-free, and contains
      source manifest/hash/reconciliation data.
- [ ] No final complete-A claim remains if any required edge is unresolved.
- [ ] Worker return passes its full fast gate and records actual pending paths.
- [ ] Worker performs no commit and HEAD remains unchanged.

Fail conditions:

- [ ] Any accepted row cites temporary/provider-specific material as CVF
      authority.
- [ ] Any indirect invocation skips a registry/runner hop or lacks source-line
      evidence.
- [ ] Any stale path is called missing without archive/successor search.
- [ ] Any operator-surface claim lacks a real route, readout, command, or doc.
- [ ] Any runtime, provider/live, public, B, maintenance implementation,
      cleanup, retirement, or session mutation appears in the changed set.

Closure is blocked if any fail condition is present.

## Verification Commands

Run following the last material edit:

```powershell
python -m json.tool docs/audits/CVF_MSEA_R90_SYSTEM_CHAIN_AUDIT_A_EVIDENCE_2026-07-10.json
python governance/compat/check_markdown_structural_completeness.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_finding_to_governance_learning.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_corpus_completeness_report_integrity.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_agent_operation_trace.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_delta_execution_claim_boundary.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git diff --name-status
git status --short --untracked-files=all
```

The worker must also run a deterministic Markdown/JSON reconciliation command
and record the exact command and result in the worker return.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: at least some current CVF chain edges will be
structural, manual, historical, stale, or absent rather than uniformly
machine-connected; prior scout counts may change under correct authority and
data-driven invocation resolution.

Evidence Comparison Requirement: compare every final lane result with this
prediction and with prior FPC-T1/scout claims.

Contradiction Handling Requirement: contradictory evidence requires a
Contradiction Or Gap Disposition, authority-precedence note, and narrowed claim.

Claim Update Requirement: record whether each prior claim is confirmed,
revised, narrowed, superseded, or rejected.

## Finding-To-Governance Learning Disposition

If execution exposes a reusable control defect, use a checker-accepted defect
class and learning lane in the worker return. Data-driven registry omission is
currently treated as an audit-method lesson; do not add or modify an ADIF entry
in worker scope. If no new reusable finding exists, use `N/A_WITH_REASON` only
as the disposition and provide an accepted defect-class reason or omit a new
finding row.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher role |
| Provider or surface | Codex local workspace |
| Session or invocation | MSEA-R90 work-order dispatch, 2026-07-10 |
| Working directory | repository root |
| Command or tool surface | source reads, rg, JSON inspection, apply_patch, governance gates |
| Target paths | MSEA-R90 baseline and work order |
| Allowed scope source | operator instruction and paired GC-018 baseline |
| Before status evidence | HEAD `3bdb6640a`; tracked worktree clean |
| After status evidence | dispatch pair pending validation |
| Diff evidence | `git diff --name-status` |
| Approval boundary | dispatch authoring only; worker outputs remain future artifacts |
| Claim boundary | repo-local trace; no implementation result or external attribution claim |
| Agent type | Codex |
| Invocation ID | `msea-r90-work-order-dispatch-2026-07-10` |
| Expected manifest | MSEA-R90 baseline and work order |
| Actual changed set | MSEA-R90 baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename. |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | bounded static system-chain audit and machine evidence |
| claimDisposition | CLAIM_REJECTED: no runtime enforcement or execution-control behavior is implemented. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed. |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source reads, parsing, searches, diffs, and gates are required as audit evidence. |
| invocationBoundary | manually invoked local read-only analysis and creation of three governed artifacts |
| interceptionBoundary | no IDE, shell, filesystem, provider, runtime, or agent interception claim |
| claimLanguage | source-backed chain classification, not behavior modification |
| forbiddenExpansion | no B, freshness implementation, cleanup, retirement, source/checker/runtime/session/public mutation, or commit |

## Review Gate

Worker handoff is not closure. Reviewer must inspect every claimed edge,
recompute representative indirect/manual/stale/operator-surface samples,
compare Markdown and JSON, repair only allowed-scope defects, and run reviewer
preflight before any material commit. Closed-equivalent status requires a
non-empty committed range and reviewer-owned completion artifact.

## Closure Checklist

- [ ] Worker artifacts match the planned manifest.
- [ ] All acceptance criteria resolved PASS or explicit blocking disposition.
- [ ] No fail condition remains.
- [ ] Reviewer recomputed representative source edges and path dispositions.
- [ ] Markdown and JSON reconciliation passes.
- [ ] Worker-return fast gate passes.
- [ ] Commit mode remains WORKER_MUST_NOT_COMMIT for worker handoff.
- [ ] Reviewer captures closureBaseHead and owns any accepted commit.
- [ ] Deliverable B remains unauthorized until Audit A reviewer acceptance.
- [ ] Maintenance/freshness implementation remains a later fresh packet.
- [ ] Advisory-directory relocation remains a later governed cleanup batch.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` when current sources conflict without a valid
authority precedence rule; an expected source is unreadable; a required edge
cannot receive a bounded disposition; Markdown/JSON reconciliation cannot be
repaired inside owned paths; or completion would require forbidden scope.

## Operator Checkpoint

The operator authorized this bounded worker dispatch. No intermediate operator
checkpoint is required for allowed-scope read-only analysis or output-shape
repair. Fresh operator approval is required for Deliverable B, maintenance or
freshness implementation, advisory-directory relocation, lifecycle mutation,
public-sync, provider/live proof, destructive work, or any scope expansion.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: MSEA-R90 is a private provenance audit; public-sync and public claims
are forbidden.

## Claim Boundary

This work order authorizes source-backed Audit A documentation and evidence
only. It does not prove all CVF planes complete, change any behavior, authorize
Deliverable B, implement freshness controls, clean the repository root, retire
checkers, or claim provider, public, production, or universal agent governance.
