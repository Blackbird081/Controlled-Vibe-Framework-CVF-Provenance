# CVF Agent Work Order - NCR Next-Move Alignment
Memory class: governed-worker-dispatch
docType: work_order
Status: DISPATCH_READY
Date: 2026-10-07
Batch ID: CVF-NCR-NEXT-MOVE-ALIGNMENT-EXECUTION-20261007
Dispatch base head: `e1a39623d2da54c0a5523bbec0d3574ff8d06b1e`
Commit mode: `WORKER_MUST_NOT_COMMIT`
providerExecutionAuthority: FORBIDDEN
rawMemoryReleased=false

## Dispatch Prompt Envelope

Role: INTERNAL_AGENT implementation worker LOCAL_CODEX_ROOT.
Canonical packet: this work order and its named baseline, committed and pinned.
Commit mode: WORKER_MUST_NOT_COMMIT.
executionBaseHead: capture actual clean released HEAD before source writes.
Current-time notes: bounded implementation admitted; separate Local reviewer is operator-relayed.
Do-not-misread notes: earlier DRAFT preparation PASS was not release or implementation proof.
Required first actions: startup, packet pins, clean worktree, release gate and unchanged source pins.
Return contract: exact six-path return with consolidated evidence and COMPLETE_PENDING_REVIEW.

Exact workspace: private CVF repository root. Read this order and baseline
`docs/baselines/CVF_GC018_NCR_NEXT_MOVE_ALIGNMENT_2026-10-07.md`. Return at `docs/reviews/CVF_NCR_NEXT_MOVE_ALIGNMENT_WORKER_RETURN_2026-10-07.md` with COMPLETE_PENDING_REVIEW or one consolidated
BLOCKED_WITH_REASON after authorized execution. Execute only after the committed packet and continuity pass the release gate.
Operator continuation admits this scope; independent review is relayed by the
operator to a separate Local actor after worker return. No subagent,
provider, public/deploy or live data use. No parallel provider-named relay.

## Purpose

Repair NCR next-move consistency in the existing checker, preserve legacy
behavior and create headroom in the two near-hard owners as one admitted outcome.

## Scope / Target / Owner Boundary

Proposed worker is INTERNAL_AGENT implementation worker; Local reviewer/closer
owns semantic acceptance and commits. Only the following six paths may change
after admission; worker does not edit baseline/order/continuity or commit.

## Allowed Paths

- `governance/compat/check_active_session_state.py`
- `governance/compat/test_check_active_session_state.py`
- `governance/compat/active_session_next_move_alignment.py`
- `governance/compat/test_active_session_next_move_alignment.py`
- `docs/reviews/evidence/cvf-ncr-next-move-alignment-worker-2026-10-07.json`
- `docs/reviews/CVF_NCR_NEXT_MOVE_ALIGNMENT_WORKER_RETURN_2026-10-07.md`

## Forbidden Paths

All other paths, including AGENTS.md, hook catalogs, schema/generator/migration
registry, current state/front door/handoff, product code, dependencies and env.
No source removals or renamed paths. Proposed extraction retains the current
CLI/import entrypoint. Unrelated dirty files require Local reconciliation first.

## Implementation Contract

The current-format branch applies only when the primary state declaration is
PROGRAM_ID=CVF-NCR, with optional Next allowed move: prefix. Recognize it before
searching incidental legacy-family tokens in its narrative. Require exactly one
nonempty PROGRAM_ID, NEXT_ACTION_CLASS and BATCH_ID in that order, separated
by semicolons and followed by the header-ending period. Values use uppercase
letters,digits,underscore or hyphen and start with a letter. Extra/duplicate
header assignments and missing/malformed required assignments fail closed in
this NCR branch. Spaces around assignments/delimiters are formatting only.

Compare the full NCR declaration, including guidance after the header, across
state, the front door Next Allowed Move section and the active handoff section.
Use the single physical declaration line, with optional matching outer Markdown
backticks/prefix and surrounding whitespace removed; collapse internal whitespace
runs in guidance for comparison; compare canonical header values independently
of spacing around assignments/delimiters. Preserve case and punctuation in
values/guidance. State NCR declaration must also be a single physical line. Same IDs
with changed authority/stop guidance must reject. Missing, duplicate, malformed,
wrong-program or different declaration on either Markdown surface must reject.
Do not consume adjacent historical prose/Mode lines or scan the whole document
for an incidental PROGRAM_ID. Multiple declaration lines fail even if identical.
Multiline state strings and incomplete physical-line headers must reject.
Unmarked prose on subsequent Markdown lines is outside the declaration: do not
claim to detect arbitrary prose wrapping while also ignoring historical prose. Existing generated declarations are one
physical line. This is textual consistency, not semantic authority validation.

State declarations outside this NCR format retain legacy token behavior and the
existing unknown-family disposition. Existing _next_allowed_move_signature and
_check_next_allowed_move_alignment entrypoints remain callable; current callers,
classify/report/CLI behavior, budget and authority checks remain unchanged.
No generalized new grammar, generator/state-schema change or case-insensitive
full prose matching. Changes cannot enable work or equate aligned text with an
agent understanding it.

Move the bounded next-move comparison responsibility to the new named helper
through the current entrypoint. Move the related test group to its named test
owner without dropping legacy full-classifier drift coverage. Choose ordinary
implementation details within these contracts; no duplication of a whole test
fixture class, inherited duplicate test suite or broad helper extraction.

## Required Proof Cases

NCR-01: current synchronized single-line declarations pass, also with harmless
spacing/prefix/outer-backtick differences. NCR-02: front-door-only and
handoff-only guidance drift fail, even with identical header IDs. NCR-03: missing,
duplicate, empty or wrong-program declarations fail; malformed state NCR header
fails rather than skipping. NCR-04: incidental legacy tokens and historical
prose cannot mask the primary NCR comparison. NCR-05: existing DIR-T cases and
other legacy families retain their prior primary-token behavior; old unknown
non-NCR families keep prior disposition. NCR-06: current classifier reaches the
new comparison through its real entrypoint with disposable fixtures; whole
authority/budget regression suite passes. NCR-07: file budgets and direct CLI
imports pass after extraction; no release/provider behavior is asserted.

Capture discriminating pre-repair negatives against unchanged checker code
before product edits, then green controls and named regression results. Store
commands/exits, failing assertions, old/final source hashes and exact changed
paths in the evidence JSON. Separate fixture/helper observations from the
full-classifier cases. Do not call real providers or read/modify a live ledger.

## Near-Threshold Owner Maintainability Plan

| Owner | Current count | Hard threshold | Extraction/split target | New helper path | Minimum shrink target | Post-change limit |
|---|---|---|---|---|---|---|
| governance/compat/check_active_session_state.py | 951 | 1000 | next-move comparison responsibility | governance/compat/active_session_next_move_alignment.py | 50 lines | <=901 |
| governance/compat/test_check_active_session_state.py | 1172 | 1200 | related alignment tests, preserving full-classifier oracles | governance/compat/test_active_session_next_move_alignment.py | 50 lines | <=1122 |

Minimum shrink target: 50 lines per existing owner; measured from committed
source pins, not achieved by deleting oracles or bulk whitespace compaction.
New files remain below their applicable GC-023 hard limits. Entrypoints are
writable, not forbidden. Count command: Python len(Path(path).read_text().splitlines())
for the four named code/test paths. All extraction writes are worker-owned.
## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| NCR declaration has no recognized legacy signature; helper returns no violation | governance/compat/check_active_session_state.py | next-move helpers | _check_next_allowed_move_alignment | active continuity | ACCEPT |
| Existing full-classifier fixtures cover legacy front-door/handoff drift | governance/compat/test_check_active_session_state.py | primary-token cases | ActiveSessionStateTests | checker regression | ACCEPT |
| Dispatcher/Git/proof joins already owned | docs/reference/work_order_template/CVF_WORK_ORDER_ACCEPTANCE_LEDGER_ADDENDUM.md | Oracle And Reducer Rules | N/A | return admission | ACCEPT |
| Outcome design selects reuse; parser candidate remains unimplemented | docs/reviews/learnings/CVF_OUTCOME_BOUND_CONTINUATION_LEARNING_2026-10-07.md | Existing-Owner Design Disposition | N/A | Local design | ACCEPT |

Exact source Git-byte pins at 35c7f8f1cf054f6d23f0cffd22c9a2103fe0cd1e:
- `governance/compat/check_active_session_state.py` SHA256 `5b8a085f847622d6d772e66be74e31bed4472e3d42d9f2d815c24d65e7c1eca5`.
- `governance/compat/test_check_active_session_state.py` SHA256 `cb6d2ee61a57a71b7561620be0f0f1d84d21593ff8c01648a626837c18955b6f`.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`
Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045, ADIF-0051, ADIF-0052, ADIF-0056, ADIF-0057, ADIF-0058, ADIF-0061, ADIF-0062, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006
Full query used --max-results 100: totalCandidates=27;truncated=false. All returned
IDs disclosed; no claim that this proves understanding. Applicable precautions:
source/authority fidelity, read-ahead, protected-scope admission, transitive
continuity pins, execution-base freshness, closeability, authoring-vs-release,
acceptance join, output-root anchoring and valid command signatures. No corpus
claim, provider memory authority, detached launch or live/runtime execution.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | governance/compat/check_active_session_state.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_dispatch_release_readiness.py; governance/compat/check_adif_defect_registry_disclosure.py; governance/compat/check_core_guard_self_protection.py; governance/compat/check_markdown_structural_completeness.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_agent_handoff_boundary.py; governance/compat/check_delta_execution_claim_boundary.py; governance/compat/check_foundation_storage_layout.py; governance/compat/check_independent_review_probe_admission.py |
| literalTokensReviewed | DRAFT; WORKER_MUST_NOT_COMMIT; acceptance-ledger-json; requirementId; requiredProofIds; exact graph fields; Source Verification; trace labels |
| gateRunPurpose | confirm admitted packet before committed release |
| claimBoundary | admitted packet structure only; corrected behavior and independent proof not yet supplied |

## Negative Search And Collision Discipline

`rg -n 'CVF-NCR-NEXT-MOVE-ALIGNMENT|NCR_NEXT_MOVE_ALIGNMENT' docs CVF_SESSION`
returned no governed matches before authoring. Exact baseline/order/new helper,
new test and proof output paths did not exist; checker/test owners exist.
Collision decision: reuse the existing owners, two budget-driven helper paths;
no second checker, schema or registry. Scope is named paths, not a corpus inventory.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id CVF-NCR-NEXT-MOVE-ALIGNMENT --title "NCR Next-Move Alignment" --date 2026-10-07 --base 35c7f8f1cf054f6d23f0cffd22c9a2103fe0cd1e --commit-mode WORKER_MUST_NOT_COMMIT --no-evidence-readiness-applicable --stdout |
| generatedProfile | protected-governance-path plus WORKER_MUST_NOT_COMMIT |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | resolve scope/spec/source/ADIF; keep DRAFT; add exact ledger and closeability graph; retain generated convergence block |
| checkerReadAheadConfirmation | governance/compat/check_active_session_state.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_dispatch_release_readiness.py; governance/compat/check_adif_defect_registry_disclosure.py; governance/compat/check_core_guard_self_protection.py; governance/compat/check_markdown_structural_completeness.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_agent_handoff_boundary.py; governance/compat/check_delta_execution_claim_boundary.py; governance/compat/check_foundation_storage_layout.py; governance/compat/check_independent_review_probe_admission.py |
| docOnlyNewFields | NONE; existing contract fields reused |
| claimBoundary | packet preparation only |
## Review Dispatch Convergence And Invocation Budget Control
Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: CVF-NCR-NEXT-MOVE-ALIGNMENT
reviewRoundCount: 0
priorFindingSetDigest: NOT_APPLICABLE_INITIAL_DISPATCH
dependencyAuditDisposition: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
reworkFindingDisposition: NOT_APPLICABLE_INITIAL_DISPATCH
newIndependentCriticalEvidence: NONE
regressionGuardDisposition: BASELINE_NEGATIVE_TESTS_PLANNED
cumulativeExternalInvocationCount: 0
externalInvocationCeiling: 0
usageAvailability: NOT_APPLICABLE_INTERNAL_AGENT
quotaAdmissionDisposition: NOT_APPLICABLE_INTERNAL_AGENT
nextDispatchDisposition: INITIAL_DISPATCH
rootCauseClusterId: NOT_APPLICABLE_INITIAL_DISPATCH
reworkGeneration: 0
consolidatedDefectClassSweep: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
successorTrancheOpened: NO
implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY
preExecutionReviewAdmission: NOT_REQUIRED_BEFORE_EXECUTION
preExecutionReviewTrigger: NONE
nextRoutineReviewBoundary: WORKER_RETURN
reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION
## Semantic Convergence Outcome
Standard: `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "cvf-ncr-next-move-alignment-problem",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {
    "prior": [],
    "resolved": [],
    "retained": [],
    "new": [],
    "reopened": [],
    "current": []
  },
  "resolutionEvidence": {},
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0,
    "nonDecreasingBlockerTransitions": 0
  },
  "claims": [],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

Author reminder: fill `blockerDelta`, `counters`, and `claims` with real evidence before dispatch. Replace any unresolved `SCEC_PREDECESSOR_HASH_UNRESOLVED` with a real predecessor path/hash; the checker fails closed on the sentinel.

## Worker Autonomy / No-Question Rule

After lawful release, resolve normal implementation choices and compatible
repairs within this outcome. Report one consolidated blocker only for authority,
scope or capability contradiction; do not ask per test or patch. Committed release must precede implementation worker execution.

## Work-Order Fulfillment Manifest

```acceptance-ledger-json
{
  "schemaVersion": "cvf.workOrderAcceptanceLedger@1.0.0",
  "requirements": [
    {
      "requirementId": "NCR-ALIGNMENT",
      "mandatory": true,
      "expectedArtifacts": [
        "governance/compat/check_active_session_state.py",
        "governance/compat/test_check_active_session_state.py",
        "governance/compat/active_session_next_move_alignment.py",
        "governance/compat/test_active_session_next_move_alignment.py"
      ],
      "requiredProofIds": [
        "NCR-RED-GREEN",
        "LEGACY-CLASSIFIER",
        "OWNER-BUDGET"
      ]
    },
    {
      "requirementId": "NCR-RETURN",
      "mandatory": true,
      "expectedArtifacts": [
        "docs/reviews/evidence/cvf-ncr-next-move-alignment-worker-2026-10-07.json",
        "docs/reviews/CVF_NCR_NEXT_MOVE_ALIGNMENT_WORKER_RETURN_2026-10-07.md"
      ],
      "requiredProofIds": [
        "SEALED-EVIDENCE",
        "RETURN-GATE"
      ]
    }
  ],
  "proofCatalog": [
    {
      "proofId": "NCR-RED-GREEN",
      "kind": "COMMAND",
      "locator": "python -m pytest governance/compat/test_active_session_next_move_alignment.py -q"
    },
    {
      "proofId": "LEGACY-CLASSIFIER",
      "kind": "COMMAND",
      "locator": "python -m pytest governance/compat/test_check_active_session_state.py governance/compat/test_active_session_next_move_alignment.py -q"
    },
    {
      "proofId": "OWNER-BUDGET",
      "kind": "COMMAND",
      "locator": "Python line counts and git diff --check"
    },
    {
      "proofId": "SEALED-EVIDENCE",
      "kind": "ARTIFACT",
      "locator": "docs/reviews/evidence/cvf-ncr-next-move-alignment-worker-2026-10-07.json"
    },
    {
      "proofId": "RETURN-GATE",
      "kind": "COMMAND",
      "locator": "python governance/compat/run_worker_return_fast_gate.py"
    }
  ]
}
```

Worker evidence uses the existing acceptance-evidence-json schema and exactly
one result per requirement. Dispatcher-owned expected set cannot be redefined by
worker prose. The actual union comes from Git at fresh executionBaseHead.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED
workerReturnPath: `docs/reviews/CVF_NCR_NEXT_MOVE_ALIGNMENT_WORKER_RETURN_2026-10-07.md`

Worker returns Purpose, Scope / Methodology, Findings / Position,
Risk / Corrective Action, Claim Boundary, Checker Source Read-Ahead Block,
Agent Operation Trace Block, Delta Execution Claim Boundary Control Block,
Public Export Disposition, executionBaseHead and `git status --short`.
Conditional blocks: External Knowledge Intake Routing;
Rescan Intelligence Hardening; Corpus Completeness And Report Integrity;
Finding-To-Governance Learning Disposition; Epistemic Process Block;
Machine Closure Package. Include applicable evidence or `N/A with reason`.
Return is pending review, not closure. Use current scaffold/fast gate owners.

## Commit Mode And Base-Anchor Lifecycle

WORKER_MUST_NOT_COMMIT. Dispatch base is planning provenance, not executionBaseHead.
Capture actual clean HEAD immediately before implementation and preserve source
pins. Reviewer captures closureBaseHead at review; Local alone commits material,
then session-sync steward records the real SHA and generates continuity. Run
committed-range closure only after continuity. No prediction of commit hashes.

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0
closeabilityDisposition: CLOSEABLE
returnTimeRecheck: REQUIRED_BEFORE_REPAIR
implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT
foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | packet baseline/order | EXACT_PATHS | Local-closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | packet baseline/order | EXACT_PATHS | Local-closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | AGENT_HANDOFF_V63_2026-09-18.md material-SHA marker and source continuity | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| pre_implementation_autorun | IMPLEMENTATION | worker | IMPLEMENTATION | six allowed paths | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | dispatch_continuity |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | six allowed paths | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | dispatch_continuity,pre_implementation_autorun |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker proof/return | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | focused_checker_tests |
| worker_return_fast | WORKER_RETURN | worker | WORKER_RETURN | worker proof/return | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | adif_integrity |
| reviewer_fast | REVIEW | reviewer | REVIEW | six allowed paths and Local completion | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | PRE_MATERIAL_COMMIT | reviewed six paths and Local completion | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | POST_MATERIAL | reviewer | REVIEW | Local completion review | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | source continuity and generated views | EXACT_PATHS | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL_CLOSURE | reviewed material/continuity ranges | EXACT_PATHS | Local-closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

Graph is a design-time topology, not passed execution gates. The graph must pass for the admitted dispatch state. Explicit candidate-only validation may substitute
DISPATCH_READY in memory to inspect the graph without changing repository status.

## Verification Commands

After lawful release: focused pytest targets named by proof catalog; direct
`python governance/compat/check_active_session_state.py`; Python source line counts;
`git diff --check`; `python governance/compat/run_worker_return_fast_gate.py`.
No subprocess provider call or live Governance Engine is needed for these
textual consistency fixtures. Real governance behavior is not claimed.

## Reviewer Closure Conversion

Local reviews exact source delta, discriminating negatives, current/legacy
controls, file counts and proof contents. Consume valid worker evidence; no broad
duplicate rerun. Acceptance ledger reduction authorizes only pending review.
Local completion and continuity remain separate from worker output paths.
completionReviewPath: docs/reviews/CVF_NCR_NEXT_MOVE_ALIGNMENT_COMPLETION_2026-10-07.md
reviewerOwnedClosurePaths: Local completion and separately authorized source/generated continuity only.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: bounded NCR comparison and related owner extraction.
Protected paths: `governance/compat/check_active_session_state.py`; `governance/compat/test_check_active_session_state.py`; `governance/compat/active_session_next_move_alignment.py`; `governance/compat/test_active_session_next_move_alignment.py`.
Operator authorization: continuation on 2026-10-07 under the prepared scope;
operator explicitly selected a separate Claude Local reviewer via manual relay.
Rollback boundary: named implementation paths only; preserve legacy behavior,
NIS closure, immutable archive, current unrelated rules and parked lanes.

## Claim Boundary

Prepared spec/scope/proof design, not executable authority or release readiness.
No corrected checker, worker transfer, agent comprehension or runtime proof.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md |
| Input type | internal governed input (no external intake) |
| Internal source | docs/reviews/learnings/CVF_OUTCOME_BOUND_CONTINUATION_LEARNING_2026-10-07.md |
| Chain map route | Local existing-owner control repair planning |
| Matching local-view guard | N/A with reason: internal sources only |
| Owner surface | governance/compat/check_active_session_state.py |
| Disposition | Local scope admitted; committed release gate required |
| Claim boundary | no external repository absorption or public absence claim |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## External Repository Absorption Entry Control

NOT_APPLICABLE_WITH_REASON - internal packet preparation only.

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON - no absorption corpus processed.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - named checker/test and proof packet only.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY - private maintenance packet.
## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatcher/reviewer |
| Provider or surface | private repository tools, no delegation/provider call |
| Session or invocation | ncr-next-move-alignment-packet-20261007 |
| Working directory | repository root |
| Command or tool surface | source/pin review, admitted contract revision, exact-path staging and commit helper |
| Target paths | `docs/baselines/CVF_GC018_NCR_NEXT_MOVE_ALIGNMENT_2026-10-07.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_NEXT_MOVE_ALIGNMENT_2026-10-07.md` |
| Allowed scope source | operator continuation and explicit Local reviewer relay selection on 2026-10-07 |
| Before status evidence | clean worktree at e1a39623d2da54c0a5523bbec0d3574ff8d06b1e before Local disposition |
| After status evidence | exact two admitted packet paths; implementation not started |
| Diff evidence | Git diff of the two packet artifacts; unchanged source pins; active-state validators |
| Approval boundary | admitted six-path implementation; committed release required before execution; final independent review pending |
| Claim boundary | no implementation/dispatch/provider or runtime control proof |
| Agent type | INTERNAL_AGENT |
| Invocation ID | ncr-next-move-alignment-packet-20261007 |
| Expected manifest | `docs/baselines/CVF_GC018_NCR_NEXT_MOVE_ALIGNMENT_2026-10-07.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_NEXT_MOVE_ALIGNMENT_2026-10-07.md` |
| Actual changed set | `docs/baselines/CVF_GC018_NCR_NEXT_MOVE_ALIGNMENT_2026-10-07.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_NEXT_MOVE_ALIGNMENT_2026-10-07.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Authority Chain

Root AGENTS.md and canonical lifecycle/acceptance-ledger owners govern. Active
Operator continuation admits the named GC-018 maintenance scope; committed
packet pins and release continuity bind current execution authority. Historical
NIS-T1J closure remains separate and gains no successor work.

## Agent Roles

Dispatcher prepares packet; implementation worker may execute only after lawful
release; Local reviewer accepts evidence; Local closer commits; session-sync
steward updates current continuity. No provider-specific worker requirement.

## Required First Reads

Startup bootstrap/front door/active handoff; root routing and guard orientation;
this order and named baseline; acceptance-ledger addendum; source pins/checkers
listed in read-ahead; governed file-size guard and handoff contract below.

## Pre-Flight Checks

Before execution: committed baseline/order pins, bound release gate, no source
drift, clean execution
worktree, outputs absent, pre-dispatch and bound release gates, source continuity.
Fresh executionBaseHead is captured only after these requirements are satisfied.

## Write Ownership

Worker owns proposed six-path implementation manifest; dispatcher alone owns
packet. Reviewer owns completion; session-sync steward owns protected continuity.
Execution writes require the committed release gate; reviewer writes require lane handoff.

## Execution Plan

After lawful admission: capture source/evidence plan and discriminating negatives;
perform bounded comparison/test extraction and NCR correction together; verify
legacy/current/classifier and budget requirements; return once through the bound
full gate. Local reviews proof content and closes only after accepted fulfillment.

## Evidence Requirements

Actual commands/exits/assertions and old/final hashes for the required NCR cases,
legacy/classifier regression, owner budgets and return gate. JSON records exact
six paths. Evidence ID presence alone is not semantic acceptance.

## Acceptance Criteria

All required cases NCR-01 through NCR-07 satisfied at final source revision;
existing owners shrink at least50 lines each without dropped tests; current CLI
and legacy behavior preserved; ledger output union and proof IDs agree with Git.
Pending worker return is not final closure or proof of continuous agent behavior.

## Review Gate

Local checks exact scope and evidence under EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION.
Consume valid proof; rerun only a named contradiction with information gain/cost.
No dispatch or release readiness follows from DRAFT authoring PASS.

## Closure Checklist

Applicable ledger/return and review gates; no forbidden changes; all admitted
requirements accepted; material commit then real-SHA continuity and committed
closure. Preserve public/private and parked lanes; current closed NIS authority
remains until a lawful packet admission explicitly binds its successor.

## Return-To-Orchestrator Conditions

After execution admission, one consolidated BLOCKED_WITH_REASON for scope,
authority, source drift, impossible dependency or unresolved required proof.
No commit, per-case operator question or self-expanded scope.

## Operator Checkpoint

Operator continuation admits the bounded implementation and selected a separate
Local reviewer via manual relay. Final closure requires that actual review. Provider/live/effect/public/deploy remain excluded.

## Independent Review Probe Admission Contract

independentProbeRequired: YES
independentProbeRiskClass: PROTECTED_CORE_GUARD_TEXT_ALIGNMENT
independentProbeDispositionAtDispatch: PENDING_REVIEWER_EXECUTION
probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER
implementationOracleSeparation: reviewer derives expectations from this committed contract and disposable source fixtures, without importing worker test expectations; actual actor separation must be bound at release and recorded at closure, not inferred from role labels
positiveControl: synchronized NCR declaration with legacy tokens only in narrative must pass full classifier
negativeMutationClasses: reviewer changes guidance only, duplicates the primary declaration and removes one required header assignment; each must fail the relevant continuity comparison
expectedInformationGain: distinguish real current-format drift rejection from a passing token-only or malformed-header bypass
rerunCostReason: bounded disposable lexical fixtures only; no full-suite duplication, provider calls or runtime enforcement claim
reviewerDecisionOwner: LOCAL

## Foundation Storage Layout Block

Existing governance/compat entrypoint retained; stable undated comparison and
adjacent test helper paths in that same folder. No new folder/reference taxonomy,
registry or runtime checker. Durable plan/evidence artifacts use existing
baselines/work_orders/reviews roots. File-size shrink is in the same worker scope.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md.

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | implementation worker then Local review/commit |
| phase | admitted dispatch; bound release before implementation |
| baseHeadFor(phase) | dispatchBaseHead=e1a39623d2da54c0a5523bbec0d3574ff8d06b1e;executionBaseHead=fresh clean released HEAD;closureBaseHead=Local review head |
| changedSetScope(phase) | exact six-path worker ledger;packet dispatcher-owned |
| traceScope(phase, actor) | source pins,actual assertions/exit and exact Git diff |
| commitOwner(phase) | Local closer,worker forbidden |
| crossBatchIsolation | closed NIS and parked effects/public/deploy retained |
| nextMoveSurfaces | committed packet,source continuity and bound release |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF
activeLaneOwner: LOCAL_CODEX_ROOT implementation worker after committed release; LOCAL_CLAUDE_OPERATOR_RELAY reviewer only after worker lane release
laneOwnedPaths: exact six-path acceptance ledger
dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE
laneReleaseEvidence: returned exact diff/evidence and full return gate before Local review

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | draft NCR textual consistency repair preparation |
| claimDisposition | CLAIM_REJECTED: no implementation or universal enforcement claim |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: worker proof not executed |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: checker unchanged |
| invocationBoundary | source/packet reads and structural validators |
| interceptionBoundary | cooperative repository path only,no arbitrary client interception |
| claimLanguage | prepared contract,not released or corrected |
| forbiddenExpansion | no runtime authority,provider/pilot,actual-data/public/deploy effect |

## Local Technical Disposition

ACCEPT_SCOPE_FOR_BOUNDED_IMPLEMENTATION. Operator continuation on 2026-10-07
admits the named repair; operator selected Claude running Local as independent
reviewer and will relay the task. No automatic Claude invocation or subagent.
Implementation actor: LOCAL_CODEX_ROOT; probe actor: LOCAL_CLAUDE_OPERATOR_RELAY.
Actual invocation IDs, distinct oracle/evidence bytes and probe result must
be recorded at review; assignment is not executed independent proof.
Source Git-byte hashes and 951/1172 line counts reverified at e1a39623d2da54c0a5523bbec0d3574ff8d06b1e;
no source diff. Existing source handles legacy primary tokens and skips NCR;
three legacy full-classifier fixtures establish the preserved oracle group.
Ledger validation COMPLIANT. Full comparison remains textual consistency.
Prose-wrap claim narrowed to observable single-line boundaries; no arbitrary
history/prose discrimination or general semantic authorization is promised.
Packet commit plus current-authority pins, EXECUTE continuity and release gate
must precede worker edits. Worker returns once; independent proof and final
closure remain pending the operator-relayed Local reviewer.

## Required Artifact Manifest

| Path | Required at handoff |
|---|---|
| governance/compat/check_active_session_state.py | YES |
| governance/compat/test_check_active_session_state.py | YES |
| governance/compat/active_session_next_move_alignment.py | YES |
| governance/compat/test_active_session_next_move_alignment.py | YES |
| docs/reviews/evidence/cvf-ncr-next-move-alignment-worker-2026-10-07.json | YES |
| docs/reviews/CVF_NCR_NEXT_MOVE_ALIGNMENT_WORKER_RETURN_2026-10-07.md | YES |

Worker return path: docs/reviews/CVF_NCR_NEXT_MOVE_ALIGNMENT_WORKER_RETURN_2026-10-07.md

## Intake Role Routing Decision

Operator request: continue the bounded NCR repair and relay review to Claude Local.
Selected role route: MULTI_AGENT_MULTI_ROLE. Protected scope is four code/test
paths and two worker evidence paths. Provider/live risk is excluded. Worker
LOCAL_CODEX_ROOT and reviewer LOCAL_CLAUDE_OPERATOR_RELAY are separate actors.
Escalation: consolidate scope/source drift findings; stop closure if actual
independent reviewer evidence is absent or shares the worker oracle.

## Single-Agent Multi-Role Control Block

Local root role separation ledger: dispatcher releases; worker implements;
steward prepares evidence and continuity. Evidence basis is source, Git diff and
actual gate/test results. Root self-review is not independent. Gate sequence:
pre-dispatch, committed release, pre-implementation, worker-return, independent
reviewer probe and Local closure. Operator relays the separate reviewer task.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: bounded existing continuity parser maintenance;
no new repository absorption, coverage-index capability or legacy corpus claim.

Execution batch separates the newly admitted implementation from the earlier
planning/disposition batch; scope and source pins remain those reviewed above.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "CVF-NCR-NEXT-MOVE-ALIGNMENT-EXECUTION-20261007",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "STATEFUL_LOCAL_IMPLEMENTATION",
    "authorityImpact": "USES_EXISTING_OWNER",
    "externalEffect": "LOCAL_REVERSIBLE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "NAMED_FILES",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "KNOWN_PATTERN"
  },
  "pathFamilies": [
    "docs/baselines/CVF_GC018_NCR_NEXT_MOVE_ALIGNMENT_2026-10-07.md",
    "docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_NEXT_MOVE_ALIGNMENT_2026-10-07.md",
    "governance/compat/check_active_session_state.py",
    "governance/compat/test_check_active_session_state.py",
    "governance/compat/active_session_next_move_alignment.py",
    "governance/compat/test_active_session_next_move_alignment.py",
    "docs/reviews/evidence/cvf-ncr-next-move-alignment-worker-2026-10-07.json",
    "docs/reviews/CVF_NCR_NEXT_MOVE_ALIGNMENT_WORKER_RETURN_2026-10-07.md",
    "AGENT_HANDOFF_V63_2026-09-18.md",
    "CVF_SESSION_MEMORY.md",
    "CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json",
    "CVF_SESSION/state/entries/nextAllowedMove.json",
    "CVF_SESSION/ACTIVE_SESSION_STATE.json",
    "CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json"
  ],
  "claims": [
    "BOUNDED_TEXT_ALIGNMENT_NOT_RUNTIME_GOVERNANCE",
    "INDEPENDENT_PROBE_PENDING_REVIEWER_EXECUTION"
  ],
  "requiredProof": [
    "NCR_RED_GREEN",
    "LEGACY_CLASSIFIER",
    "OWNER_BUDGET",
    "FULL_LEGACY_GATES",
    "INDEPENDENT_REVIEWER_PROBE"
  ],
  "operatorCheckpoints": [
    "OPERATOR_RELAY_LOCAL_REVIEWER_BEFORE_CLOSURE"
  ],
  "forbiddenEffects": [
    "PROVIDER_CALL",
    "NETWORK_ACCESS",
    "INSTALL",
    "PUBLIC_WRITE",
    "DEPLOYMENT",
    "REAL_DATA_MUTATION"
  ],
  "sourceEvidence": {
    "selectedFilesFullyRead": false,
    "corpusReceiptRef": null,
    "completenessClaimChanged": false
  }
}
```

SHADOW_FULL_GATE_FALLBACK; full legacy bundles remain mandatory.
