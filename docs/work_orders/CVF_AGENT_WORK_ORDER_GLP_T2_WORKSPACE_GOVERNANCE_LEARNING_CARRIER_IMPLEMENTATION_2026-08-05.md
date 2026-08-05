# CVF Agent Work Order - GLP T2 Workspace Governance Learning Carrier Implementation

Memory class: FULL_RECORD

Status: HOLD_OPERATOR_IMPLEMENTATION_AUTHORITY

docType: work_order

Date: 2026-08-05

Batch ID: GLP-T2

dispatchBaseHead: `2e540b429`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `NOT_EXECUTED_YET`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: bounded governance-template and hermetic-test implementation worker.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_GLP_T2_WORKSPACE_GOVERNANCE_LEARNING_CARRIER_IMPLEMENTATION_2026-08-05.md`

Paired baseline: `docs/baselines/CVF_GC018_GLP_T2_WORKSPACE_GOVERNANCE_LEARNING_CARRIER_IMPLEMENTATION_BASELINE_2026-08-05.md`

Current-time notes: authored from clean provenance HEAD `2e540b429` after
GLP-T1 acceptance at `87febcba9`.

Do-not-misread notes: status is held. This packet is not an implementation
dispatch until operator authority is recorded, dependency evidence is
refreshed, and the pre-dispatch gate passes.

Required first actions after release: complete startup acknowledgment; capture
HEAD and `git status --short`; read this packet, baseline, accepted T1 audit,
template, bootstrap CP1 source, golden harness, guard orientation, literal
gotchas, and named checker sources; then run pre-implementation from the
captured execution base before editing.

Return contract: modify exactly two implementation paths, create exactly one
worker return, run focused evidence and the worker-return fast gate, commit
nothing, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Implement the smallest public-safe governance-latency carrier accepted by
GLP-T1 and prove its existing project-consumer chain hermetically without
editing the bootstrap mechanism.

## Authority Chain

| Authority layer | Evidence | Disposition |
|---|---|---|
| operator roadmap authority | accepted GLP roadmap and current next-move surfaces | packet authoring only |
| design authority | GLP-T1 accepted at `87febcba9` | ACCEPT |
| implementation authority | explicit operator release | HOLD_OPERATOR_IMPLEMENTATION_AUTHORITY |
| review/commit authority | independent reviewer/closer after worker return | ACCEPT |

## Agent Roles

| Role | Ownership |
|---|---|
| dispatcher | authors, validates, and commits the held packet |
| worker | after release, edits exactly two implementation paths and creates one no-commit return |
| independent reviewer/closer | performs semantic review, bounded repairs, and material closure commit |
| session-sync steward | updates canonical continuity in a separate commit/range |

## Required First Reads

1. `CVF_SESSION_MEMORY.md`, active state registry, and active handoff.
2. `docs/reference/guard_orientation/README.md`.
3. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`.
4. Paired GC-018 baseline and this work order.
5. Accepted GLP-T1 audit and worker return.
6. `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md`.
7. `scripts/new-cvf-workspace.ps1` CP1 and
   `scripts/test_cvf_golden_downstream_bootstrap.ps1`.
8. Checker sources listed in the read-ahead block.

## Pre-Flight Checks

After authority release and before material edits:

```powershell
git rev-parse --short HEAD
git status --short --untracked-files=all
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <capturedExecutionBase> --head HEAD
```

Stop for non-clean worktree, source mismatch, missing path, or any gate failure
that cannot be repaired without leaving Allowed scope.

## Write Ownership

The worker owns only the two implementation paths and one worker-return path
listed under Scope / Allowed Paths. The dispatcher owns this packet; the
reviewer owns closure conversion and commits; the session-sync steward owns
continuity. `WORKER_MUST_NOT_COMMIT` is binding.

## Dependency Release Evidence

| Dependency | Artifact / evidence | Disposition |
|---|---|---|
| GLP-T1 acceptance | `docs/reviews/CVF_GLP_T1_WORKSPACE_GOVERNANCE_LEARNING_CARRIER_DESIGN_WORKER_RETURN_2026-08-05.md`; commit `87febcba9`; `CARRIER_DESIGN_ACCEPTED` | ACCEPT |
| exact carrier/test manifest | paired GC-018 Source Verification and Hermetic Proof Matrix | ACCEPT |
| clean dispatch anchor | HEAD `2e540b429`; `git status --short` empty before packet authoring | ACCEPT |
| operator implementation authority | not yet recorded | HOLD_OPERATOR_IMPLEMENTATION_AUTHORITY |

No worker may execute while the last row remains held.

## Scope / Allowed Paths

After release, the worker may modify or create only:

1. `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md`
2. `scripts/test_cvf_golden_downstream_bootstrap.ps1`
3. `docs/reviews/CVF_GLP_T2_WORKSPACE_GOVERNANCE_LEARNING_CARRIER_IMPLEMENTATION_WORKER_RETURN_2026-08-05.md`

No other path is allowed.

## Forbidden Scope

- Do not edit `scripts/new-cvf-workspace.ps1`, helper libraries, catalog,
  profile, manifest, policy, checker, hook, session, handoff, downstream
  project, public-sync clone, runtime, provider, credential, or deployment
  surfaces.
- Do not call providers or network services. The golden harness must use its
  existing hermetic local-clone mechanism.
- Do not copy ADIF evidence or private incident details into the template.
- Do not weaken an assertion to obtain PASS.
- If byte preservation, merge behavior, or delivery requires a forbidden path
  change, return `BLOCKED_WITH_REASON`; do not infer broader authority.
- Worker must not stage or commit.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id GLP-T2 --title "Workspace Governance Learning Carrier Implementation" --date 2026-08-05 --base 2e540b429 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | added authority hold, dependency evidence, exact implementation contract, source verification, public/private boundary, focused proof matrix, role routing, and no-commit return contract |
| checkerReadAheadConfirmation | dispatch-quality, ADIF disclosure, handoff-boundary, AOT, worker-return, public-export, file-size, and roadmap-freshness controls |
| docOnlyNewFields | carrierSection; carrierRuleIds; privateEvidenceSentinels; hermeticProofMatrix |
| claimBoundary | held implementation packet only; no behavior is implemented or released by this document |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| accepted T2 path and proof design | VALUE_SET | `docs/audits/CVF_GLP_T1_WORKSPACE_GOVERNANCE_LEARNING_CARRIER_DESIGN_2026-08-05.md` | R1-Corrected Design Schema | `T2AllowedPaths`; `positiveProof`; `negativeProof`; `rollback` | GLP-T1 design | ACCEPT |
| target insertion owner exists | EXISTS | `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md` | Risk Classification | `Risk Classification` | downstream AGENTS template | ACCEPT |
| bootstrap reads and projects template | RUNTIME_BEHAVIOR | `scripts/new-cvf-workspace.ps1` | CP1 lines 342-388 | `agentsTemplatePath`; `downstreamAgentsPath` | CP1 downstream AGENTS generation | ACCEPT |
| generated refresh branch exists | RUNTIME_BEHAVIOR | `scripts/new-cvf-workspace.ps1` | lines 362-369 | `isCvfGeneratedAgents` | CP1 refresh branch | ACCEPT |
| hand-edited merge branch exists | RUNTIME_BEHAVIOR | `scripts/new-cvf-workspace.ps1` | lines 372-383 | `CVF_MERGE_BLOCK_START` | CP1 merge branch | ACCEPT |
| hermetic local-core fixture exists | RUNTIME_BEHAVIOR | `scripts/test_cvf_golden_downstream_bootstrap.ps1` | setup lines 45-58 | `New-CvfHermeticCoreClone` | golden downstream bootstrap harness | ACCEPT |
| second-run idempotency fixture exists | RUNTIME_BEHAVIOR | `scripts/test_cvf_golden_downstream_bootstrap.ps1` | AC-06 lines 117-122 | `secondBootstrap` | golden downstream bootstrap harness | ACCEPT |
| legacy fixture owner exists | RUNTIME_BEHAVIOR | `scripts/test_cvf_golden_downstream_bootstrap.ps1` | BSL-R1 lines 292-318 | `sentinelProject` | golden downstream bootstrap harness | ACCEPT |
| canonical same-scope controls exist | VALUE_SET | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0026.md` | Same-scope authority continuity | `Same-scope authority continuity` | ADIF-0026 remediation | ACCEPT |
| template and harness are public projection inputs | VALUE_SET | `scripts/cvf-public-sync.ps1` | projection allowlist lines 90 and 134 | `test_cvf_golden_downstream_bootstrap.ps1`; `CVF_DOWNSTREAM_AGENTS_TEMPLATE.md` | public-sync projection allowlist | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Runtime status |
|---|---|---|
| carrierRuleIds | stable test-local identifiers for the five rule assertions if the worker needs them | DOC_ONLY_NEW; not an existing runtime field |
| privateEvidenceSentinels | exact forbidden strings used only by the hermetic test | DOC_ONLY_NEW; not a data schema |

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | NOT_APPLICABLE_WITH_REASON |
| reason | the work order concerns static template text and a hermetic local harness; it makes no provider, live, production, or runtime-enforcement claim |
| requiredFutureAction | any future live-governance or provider claim requires a separate GC-018 and real-provider proof |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`governance template implementation`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "governance template implementation" --role worker --lifecycle-phase pre-implementation --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | no additional ADIF-specific control beyond ADIF-0026 source semantics and standard worker/reviewer separation |

## Implementation Instructions

### Template carrier

Add one compact subsection immediately after the existing Risk Classification
section. Use provider-neutral operational language and cover exactly:

1. authority continuity for dependent same-scope repairs while objective,
   allowed path/artifact class, risk, external effect, and commit owner remain
   unchanged;
2. the exhaustive real-boundary escalation classes from the paired baseline;
3. one consolidated record/field/edge review before first repair;
4. `REVIEW_COST_ESCALATION_REQUIRED` at round three without an independent new
   root cause;
5. avoidable operator wait classification for repeated confirmation without a
   boundary change.

Do not include incident/tranche names, operator/session identity, historic
quota/token/time numbers, raw dissent, or private-only paths.

### Golden harness

Extend the existing harness rather than creating another test file:

- after first bootstrap, assert exactly one carrier subsection and all five
  semantics in generated `AGENTS.md`;
- after existing AC-06 second bootstrap, assert exactly one subsection, all
  five semantics, and no tracked drift;
- give the existing legacy/mixed fixture a hand-edited ASCII `AGENTS.md`, save
  its pre-bootstrap bytes, then assert exactly one merge block, carrier content
  inside that block, and byte-identical pre-existing content outside it;
- scan the template plus generated/refreshed/merge-path `AGENTS.md` files for
  exact private sentinels including `SOT3-T2`, `WS2-T1`, private provenance
  path fragments, raw dissent exemplars, operator/session identifiers, and
  incident-specific quota values;
- retain path-safe cleanup and zero-network behavior.

If the current merge implementation fails the byte-preservation assertion,
record the evidence and stop. Editing the bootstrap is not allowed.

## Execution Plan

1. Capture execution HEAD/status, complete required reads, and run the
   pre-implementation gate. Stop if authority is still held or state is dirty.
2. Add the compact carrier subsection to the template. Validate exact included
   semantics and excluded evidence before changing tests.
3. Extend the existing golden harness with fresh, refresh, merge, byte, and
   private-leakage assertions. Do not create another test file.
4. Run the focused harness once after the consolidated source/test edit. On a
   failure, classify it before any rerun; repair only within Allowed scope.
5. Create the worker return from the checker-safe scaffold, run all final
   commands once after the last edit, and leave every owned path uncommitted.

Each step consumes the prior step's files/evidence. A forbidden-path need,
private leakage, byte drift requiring bootstrap repair, or unclear failing test
is a stop condition.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| downstream AGENTS template | MODIFY with one compact public-safe carrier subsection |
| golden downstream bootstrap harness | MODIFY with fresh, refresh, merge, byte, and leakage assertions |
| worker return | CREATE with actual status, changed set, tests, boundary evidence, and no-commit declaration |

## Verification Commands

Run from repository root after the final worker edit:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/test_cvf_golden_downstream_bootstrap.ps1
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git diff --name-status
git status --short --untracked-files=all
```

The worker must record call-level test result, failed assertion name if any,
and temp-cleanup result. No provider/event denominator applies.

## Evidence Requirements

- exact diff of the carrier subsection and harness assertions;
- first-bootstrap generated-file assertion results;
- second-bootstrap uniqueness/idempotency results;
- hand-edited merge-block and outside-block byte comparison results;
- exact forbidden-sentinel scan results;
- harness cleanup evidence;
- final file-size, worker-return, diff, and Git-status evidence;
- actual `executionBaseHead`, reviewer-set `closureBaseHead`, and split
  material/session closure ranges.

Evidence Trace Block requirements for each decision-driving claim:

- Claim;
- Command;
- Result;
- Key path;
- Verdict.

## Acceptance Criteria

- [ ] exactly one public-safe carrier subsection is added adjacent to Risk Classification;
- [ ] all five accepted semantics are present and no excluded evidence is present;
- [ ] fresh generated project proof passes hermetically;
- [ ] generated-project second refresh is idempotent and retains one carrier;
- [ ] hand-edited project receives one merge block and retains outside-block bytes;
- [ ] only the two implementation paths and worker return are pending;
- [ ] golden harness, file-size guard, worker-return fast gate, and diff hygiene pass;
- [ ] worker records actual execution base/status and makes no commit.

Fail conditions:

- missing, duplicated, or semantically weakened carrier rule;
- private incident/evidence leakage;
- hand-edited content byte drift;
- need to modify bootstrap/helper/catalog/profile/checker/public/session path;
- network/provider call, public-sync, downstream mutation outside disposable
  temp fixtures, or any staged/committed worker change.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Closure evidence | Status |
|---|---|---|---|
| align provenance template surface | Template carrier | template diff | PENDING_IMPLEMENTATION_AUTHORITY |
| focused template tests | Golden harness | hermetic harness result | PENDING_IMPLEMENTATION_AUTHORITY |
| private leakage exclusion | Golden harness negatives | exact sentinel assertions | PENDING_IMPLEMENTATION_AUTHORITY |
| no bootstrap widening | Forbidden Scope and stop condition | changed-set evidence | PENDING_IMPLEMENTATION_AUTHORITY |
| independent review | no-commit route | reviewer disposition | PENDING_IMPLEMENTATION_AUTHORITY |

## Design Control Carry-Forward

| Design control | Roadmap source | Work-order handling | Verdict |
|---|---|---|---|
| smallest safe carrier | roadmap Design Control Gate; accepted T1 | one template owner only | PASS |
| public/private boundary | roadmap protected controls | exact included/excluded semantics and sentinel tests | PASS |
| project ownership | roadmap protected controls | generated project `AGENTS.md` remains the consumer | PASS |
| latency control | roadmap protected controls | five-rule carrier; no repeated worker checkpoints | PASS |
| no implicit implementation | T1 closure and current next move | held status pending operator authority | PASS |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | generated/refreshed downstream `AGENTS.md` | static guidance only; no mutation/commit authority beyond worker packet | CP1 source and golden harness | internal bootstrap projection only | `IMPLEMENTED` |
| `EXTERNAL_AGENT_CLI_MCP` | no external adapter in this tranche | no ingress, authentication, approval, receipt, raw-data, mutation, or runtime claim | forbidden scope | adapter work requires a separate packet | `DEFERRED_WITH_REASON` |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| existingFoundation | downstream AGENTS template and golden bootstrap harness remain their existing owners |
| newDurableFoundation | N/A with reason: no new durable foundation, folder, front door, or owner surface is created |
| storageClass | existing governed template and existing test harness paths |
| splitOrRelocation | N/A with reason: no split, move, relocation, or refactor is authorized |
| indexOrRegistryChange | N/A with reason: no index, catalog, profile, or registry change is authorized |
| datePolicy | N/A with reason: no new stable reference family is created |

## Agent Handoff Contract Control Block

Contract source: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher -> no-commit implementation worker -> independent reviewer/closer -> session-sync steward |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE, SESSION_SYNC |
| baseHeadFor(phase) | dispatchBaseHead=2e540b429; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | dispatch=paired packets; execution=two implementation paths plus worker return; closure=accepted worker paths and bounded reviewer repairs; session sync=canonical continuity only |
| traceScope(phase, actor) | each actor records phase-local trace and exact changed set |
| commitOwner(phase) | dispatcher commits packets; worker must not commit; reviewer commits accepted material; steward commits continuity |
| crossBatchIsolation | one GLP-T2 batch on a clean worktree; unrelated drift blocks execution |
| nextMoveSurfaces | reviewer/closer and steward update only after accepted or blocked T2 decision |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_GLP_T2_WORKSPACE_GOVERNANCE_LEARNING_CARRIER_IMPLEMENTATION_COMPLETION_2026-08-05.md` (optional; use only for unresolved disagreement) |
| reviewerOwnedClosurePaths | worker-owned implementation paths and worker return, plus optional completion review and bounded packet/roadmap lifecycle corrections |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_GLP_T2_WORKSPACE_GOVERNANCE_LEARNING_CARRIER_IMPLEMENTATION_WORKER_RETURN_2026-08-05.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

scopeClassification: SOURCE_TEST_AND_EVIDENCE_NO_COMMIT

publicSyncDisposition: FORBIDDEN

liveRuntimeDisposition: FORBIDDEN

checkerMutationDisposition: FORBIDDEN

workerSelfSelection: FORBIDDEN

Required review headings include Purpose, Target / Source, Scope /
Methodology, Findings / Position, Risk / Corrective Action, Decision /
Disposition, Checker Source Read-Ahead Block, Agent Operation Trace Block,
Delta Execution Claim Boundary Control Block, External Knowledge Intake
Routing, Epistemic Process Block, Public Export Disposition, Claim Boundary,
Changed Files, Command Evidence, Worker Experience Retrospective, and
No-Commit Statement. Conditional non-applicable sections must use explicit
`NOT_APPLICABLE_WITH_REASON` or `N/A_WITH_REASON` dispositions.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_roadmap_closure_freshness.py` |
| literalTokensReviewed | exact source dispositions and claim types; handoff route fields; worker-return contract terms; trace labels; public-export tokens; checklist residue; split material/session closure ranges |
| gateRunPurpose | confirmation evidence for held packet fidelity before authority release; not first discovery of worker requirements |
| claimBoundary | packet/readiness structure only; semantic implementation still requires worker evidence and independent review |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author |
| Provider or surface | local private provenance repository |
| Session or invocation | GLP-T2 packet authoring, 2026-08-05 |
| Working directory | repository root |
| Command or tool surface | startup reads, source verification, scaffold helper, ADIF resolver, apply_patch, dispatch gates |
| Target paths | paired GLP-T2 baseline and work order |
| Allowed scope source | accepted GLP roadmap; T1 material commit `87febcba9`; next-move surfaces at `2e540b429` |
| Before status evidence | HEAD `2e540b429`; clean worktree |
| After status evidence | held paired packet pending operator implementation authority |
| Diff evidence | `git diff --name-status` limited to paired packet paths |
| Approval boundary | packet authoring only |
| Claim boundary | no implementation, workspace/project mutation, public sync, provider/network use, push, or deployment |
| Agent type | dispatcher |
| Invocation ID | `glp-t2-work-order-authoring-2026-08-05` |
| Expected manifest | paired baseline and this work order |
| Actual changed set | paired baseline and this work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | future bounded template and hermetic-test implementation |
| claimDisposition | N/A with reason: held work order has not executed |
| receiptEvidence | N/A with reason: no runtime receipt is created |
| actionEvidence | N/A with reason: no implementation action has occurred |
| invocationBoundary | future local source/test edits and hermetic temp fixture only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, or agent-runtime interception claim |
| claimLanguage | deterministic template projection test, not runtime governance enforcement |
| forbiddenExpansion | no bootstrap/helper, provider/live, external CLI/MCP, public-sync, push, or deployment work |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: all three existing bootstrap branches carry one
public-safe subsection without private leakage or unrelated byte drift.

Evidence Comparison Requirement: worker return compares each named harness
assertion with this prediction and preserves any contradiction.

Contradiction Handling Requirement: missing delivery, duplication, leakage,
or byte drift blocks the tranche and does not authorize bootstrap edits.

Claim Update Requirement: report confirmed, narrowed, or blocked projection;
do not infer production adoption from a disposable harness.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next action |
|---|---|---|---|---|
| accepted latency control is absent from the mandatory project carrier | RULE_GAP | GOVERNANCE_CONTROL_PLANE | TEMPLATE_UPDATED | after authority release, add the compact rule and prove projection through the existing harness |

No new ADIF entry is required unless execution reveals a repeated or
non-obvious defect distinct from ADIF-0026.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: GLP-T2 implements an already-accepted provenance design and performs no absorption |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | downstream AGENTS template |
| Disposition | NOT_APPLICABLE_WITH_REASON: no new external source is absorbed in T2 |
| Claim boundary | no external input is promoted to CVF authority |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: the designed files are public projection inputs, but this provenance
work order does not authorize public-sync mutation or a public claim.

## Review Gate

Implementation may begin only when:

- operator implementation authority is recorded in the dependency table;
- status is changed from HOLD to a ready/dispatch-equivalent token;
- `dispatchBaseHead` is refreshed to that release commit;
- `executionBaseHead` remains worker-captured;
- pre-dispatch autorun passes on the released committed range.

Closure requires independent semantic review, reviewer-owned material commit,
material-only pre-closure evidence, separate session-sync commit/range, and a
clean worktree.

## Operator Checkpoint

One checkpoint is parked at implementation release. The operator must
explicitly authorize GLP-T2 implementation after reviewing this held packet.
After release, no repeated confirmation is required for same-scope repairs
that preserve objective, allowed paths, R2 ceiling, external-effect class, and
commit owner. A new checkpoint is required only for a real boundary change.

## Closure Checklist

- [ ] operator implementation authority recorded and dependency released;
- [ ] pre-dispatch gate passed on a non-empty committed release range;
- [ ] worker captured execution base and clean status;
- [ ] acceptance criteria resolved without forbidden-path widening;
- [ ] focused harness and all required guards passed or blocker preserved;
- [ ] independent reviewer disposition recorded;
- [ ] worker made no commit;
- [ ] material and session-sync closure ranges remain separate;
- [ ] public export remains deferred unless separately authorized.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for missing authority, source contradiction,
unexpected worktree state, private leakage, byte drift, forbidden-path need,
network/provider need, or any scope beyond the three worker-owned paths.

## Claim Boundary

This held work order precisely specifies GLP-T2. It does not dispatch a worker,
authorize implementation, mutate a workspace or project, prove real-world
adoption, publish, call a provider, use the network, push, or deploy.
