# CVF Agent Work Order - GLP T2R1 CP1 Byte-Preserving Merge Repair

Memory class: FULL_RECORD

Status: REVIEWER_ACCEPTED_DISPATCH_READY

docType: work_order

Date: 2026-08-05

Batch ID: GLP-T2R1

dispatchBaseHead: `ff27d9904`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `NOT_EXECUTED_YET`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: bounded CP1 merge-repair implementation worker.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_GLP_T2R1_CP1_BYTE_PRESERVING_MERGE_REPAIR_2026-08-05.md`

Paired baseline: `docs/baselines/CVF_GC018_GLP_T2R1_CP1_BYTE_PRESERVING_MERGE_REPAIR_BASELINE_2026-08-05.md`

Current-time notes: authored from clean provenance HEAD `7cdc72393` after
GLP-T2 was independently blocked at material commit `071866e7b`.

Do-not-misread notes: this is one bounded implementation dispatch. It permits
only the exact CP1/template/harness
manifest; public sync, provider/network use, and worker commit remain forbidden.

Required first actions after release: complete startup acknowledgment; capture
HEAD and `git status --short`; read this packet, baseline, blocked T2 review,
template, bootstrap CP1 source, golden harness, guard orientation, literal
gotchas, and named checker sources; then run pre-implementation from the
captured execution base before editing.

Return contract: modify exactly three source/test paths, create exactly one
worker return, run focused evidence and the worker-return fast gate, commit
nothing, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Repair the source-proven CP1 whole-file rewrite so project-owned bytes outside
the CVF merge block remain identical, then implement the accepted public-safe
carrier and prove the full projection chain hermetically.

## Authority Chain

| Authority layer | Evidence | Disposition |
|---|---|---|
| operator roadmap authority | accepted GLP roadmap and explicit GLP-T2R1 release confirmation | bounded implementation dispatch |
| repair evidence | GLP-T2 blocked review at `071866e7b` | ACCEPT |
| implementation authority | operator confirmation on 2026-08-05 for the explicit GLP-T2R1 checkpoint | ACCEPT |
| review/commit authority | independent reviewer/closer after worker return | ACCEPT |

## Agent Roles

| Role | Ownership |
|---|---|
| dispatcher | authors, validates, releases, and commits the packet |
| worker | after release, edits exactly three source/test paths and creates one no-commit return |
| independent reviewer/closer | performs semantic review, bounded repairs, and material closure commit |
| session-sync steward | updates canonical continuity in a separate commit/range |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intakeRole | dispatcher |
| executionRole | bounded implementation worker |
| reviewRole | independent reviewer/closer |
| Route | `MULTI_AGENT_MULTI_ROLE` |
| canonical route mode | `MULTI_AGENT_MULTI_ROLE` |
| selected role route | dispatcher -> no-commit worker -> independent reviewer/closer -> session-sync steward |
| routingReason | source contradiction, owners, risk ceiling, and exact changed set are fixed by the blocked T2 review and current source |
| workerSelfSelection | FORBIDDEN |
| escalation condition | objective, allowed path/artifact class, R2 ceiling, external-effect class, secrets/quota, public/provider action, destructive action, or commit-owner change |
| claimBoundary | role routing only; no provider or model is selected |

## Worker Autonomy / No-Question Rule

Proceed without operator confirmation for every allowed-scope source/test edit,
assertion repair, diagnostic classification, worker-return repair, and required
gate rerun. Escalate only for a real change in objective, allowed path/artifact
class, R2 ceiling, external-effect class, secrets/quota, public/provider action,
or commit owner. Repairs inside the authorized CP1 path continue without
another question; any additional helper/path need is a blocked return.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`, active state registry, and active handoff.
2. `docs/reference/guard_orientation/README.md`.
3. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`.
4. Paired GC-018 baseline and this work order.
5. Blocked GLP-T2 completion review and worker return.
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

The worker owns only the three source/test paths and one worker-return path
listed under Scope / Allowed Paths. The dispatcher owns this packet; the
reviewer owns closure conversion and commits; the session-sync steward owns
continuity. `WORKER_MUST_NOT_COMMIT` is binding.

## Dependency Release Evidence

| Dependency | Artifact / evidence | Disposition |
|---|---|---|
| GLP-T2 blocked review | `docs/reviews/CVF_GLP_T2_WORKSPACE_GOVERNANCE_LEARNING_CARRIER_IMPLEMENTATION_COMPLETION_2026-08-05.md`; commit `071866e7b`; `BLOCKED_IMPLEMENTATION_EVIDENCE` | ACCEPT |
| exact repair/carrier/test manifest | paired GC-018 Source Verification and Hermetic Proof Matrix | ACCEPT |
| clean packet anchor | HEAD `7cdc72393`; `git status --short` empty | ACCEPT |
| operator implementation authority | operator confirmation on 2026-08-05 for expanded CP1 bootstrap scope | ACCEPT |

All dependency rows are source-backed and released for this bounded dispatch.

## Scope / Allowed Paths

After release, the worker may modify or create only:

1. `scripts/new-cvf-workspace.ps1`
2. `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md`
3. `scripts/test_cvf_golden_downstream_bootstrap.ps1`
4. `docs/reviews/CVF_GLP_T2R1_CP1_BYTE_PRESERVING_MERGE_REPAIR_WORKER_RETURN_2026-08-05.md`

No other path is allowed.

## Forbidden Scope

- Do not edit any other bootstrap/helper, catalog, profile, manifest, policy,
  checker, hook, session, handoff, downstream
  project, public-sync clone, runtime, provider, credential, or deployment
  surfaces.
- Do not call providers or network services. The golden harness must use its
  existing hermetic local-clone mechanism.
- Do not copy ADIF evidence or private incident details into the template.
- Do not weaken an assertion to obtain PASS.
- Do not normalize, decode/re-encode, or otherwise rewrite preserved
  project-owned bytes outside the CVF merge block.
- If the repair requires any additional path, return `BLOCKED_WITH_REASON`.
- Worker must not stage or commit.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id GLP-T2R1 --title "CP1 Byte-Preserving Merge Repair" --date 2026-08-05 --base 7cdc72393 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | adapted the accepted T2 packet to the CP1 contradiction, expanded exact manifest, byte-preservation contract, authority hold, and no-commit return contract |
| checkerReadAheadConfirmation | dispatch-quality, ADIF disclosure, handoff-boundary, AOT, worker-return, public-export, file-size, and roadmap-freshness controls |
| docOnlyNewFields | bytePreservingMergeContract; carrierSection; carrierRuleIds; privateEvidenceSentinels; hermeticProofMatrix |
| claimBoundary | bounded implementation dispatch packet; no behavior is implemented by this document |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T2 failed outside-block byte identity | VALUE_SET | `docs/reviews/CVF_GLP_T2_WORKSPACE_GOVERNANCE_LEARNING_CARRIER_IMPLEMENTATION_COMPLETION_2026-08-05.md` | Findings / Position | `BLOCKED_IMPLEMENTATION_EVIDENCE` | GLP-T2 completion review | ACCEPT |
| target insertion owner exists | EXISTS | `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md` | Risk Classification | `Risk Classification` | downstream AGENTS template | ACCEPT |
| bootstrap reads and projects template | RUNTIME_BEHAVIOR | `scripts/new-cvf-workspace.ps1` | CP1 lines 342-388 | `agentsTemplatePath`; `downstreamAgentsPath` | CP1 downstream AGENTS generation | ACCEPT |
| generated refresh branch exists | RUNTIME_BEHAVIOR | `scripts/new-cvf-workspace.ps1` | lines 362-369 | `isCvfGeneratedAgents` | CP1 refresh branch | ACCEPT |
| hand-edited merge branch exists | RUNTIME_BEHAVIOR | `scripts/new-cvf-workspace.ps1` | lines 372-383 | `CVF_MERGE_BLOCK_START` | CP1 merge branch | ACCEPT |
| merge branch currently decodes and rewrites complete file | RUNTIME_BEHAVIOR | `scripts/new-cvf-workspace.ps1` | lines 355-382 | `existingContent`; `Set-Content` | CP1 merge branch | ACCEPT |
| hermetic local-core fixture exists | RUNTIME_BEHAVIOR | `scripts/test_cvf_golden_downstream_bootstrap.ps1` | setup lines 45-58 | `New-CvfHermeticCoreClone` | golden downstream bootstrap harness | ACCEPT |
| second-run idempotency fixture exists | RUNTIME_BEHAVIOR | `scripts/test_cvf_golden_downstream_bootstrap.ps1` | AC-06 lines 117-122 | `secondBootstrap` | golden downstream bootstrap harness | ACCEPT |
| legacy fixture owner exists | RUNTIME_BEHAVIOR | `scripts/test_cvf_golden_downstream_bootstrap.ps1` | BSL-R1 lines 292-318 | `sentinelProject` | golden downstream bootstrap harness | ACCEPT |
| canonical same-scope controls exist | VALUE_SET | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0026.md` | Same-scope authority continuity | `Same-scope authority continuity` | ADIF-0026 remediation | ACCEPT |
| repair, template, and harness are public projection inputs | VALUE_SET | `scripts/cvf-public-sync.ps1` | projection allowlist | `new-cvf-workspace.ps1`; `test_cvf_golden_downstream_bootstrap.ps1`; `CVF_DOWNSTREAM_AGENTS_TEMPLATE.md` | public-sync projection allowlist | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Runtime status |
|---|---|---|
| carrierRuleIds | stable test-local identifiers for the five rule assertions if the worker needs them | DOC_ONLY_NEW; not an existing runtime field |
| privateEvidenceSentinels | exact forbidden strings used only by the hermetic test | DOC_ONLY_NEW; not a data schema |
| bytePreservingMergeContract | byte-oriented behavior required only by this repair packet | DOC_ONLY_NEW; not an existing runtime field |

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | NOT_APPLICABLE_WITH_REASON |
| reason | the work order concerns deterministic local bootstrap file transformation and a hermetic harness; it makes no provider, live, production, or runtime-enforcement claim |
| requiredFutureAction | any future live-governance or provider claim requires a separate GC-018 and real-provider proof |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --surface-selector scripts/new-cvf-workspace.ps1 --risk-ceiling MEDIUM --max-results 20 --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | no additional ADIF-specific control beyond ADIF-0026 source semantics and standard worker/reviewer separation |

## Implementation Instructions

### CP1 byte-preserving merge repair

Repair only the hand-edited `AGENTS.md` branch in
`scripts/new-cvf-workspace.ps1`:

- read and retain the original byte array before marker inspection;
- emit exactly one current CVF merge block at the top;
- preserve every byte outside a prior CVF merge block without decode/re-encode;
- on refresh, replace the prior block while preserving the project-owned
  prefix/suffix byte slices;
- reject duplicate, reversed, or unterminated markers without rewriting the
  file;
- keep the CVF-generated branch behavior unchanged.

Do not create a general-purpose encoding framework or another helper file.

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
   equivalence disposition: `MATCH` is required from direct byte comparison;
- scan the template plus generated/refreshed/merge-path `AGENTS.md` files for
  exact private sentinels including `SOT3-T2`, `WS2-T1`, private provenance
  path fragments, raw dissent exemplars, operator/session identifiers, and
  incident-specific quota values;
- retain path-safe cleanup and zero-network behavior.

The legacy fixture must run both first insertion and second refresh. Compare
the original project-owned bytes directly against the preserved outside-block
bytes after each run. Add malformed-marker cases proving fail-closed behavior
and zero mutation.

## Execution Plan

1. Capture execution HEAD/status, complete required reads, and run the
   pre-implementation gate. Stop if release evidence is missing or state is dirty.
2. Implement the bounded CP1 byte-preserving merge repair and validate marker
   failure behavior before changing the template.
3. Add the compact carrier subsection to the template. Validate exact included
   semantics and excluded evidence before changing tests.
4. Extend the existing golden harness with fresh, refresh, merge, byte,
   malformed-marker, and
   private-leakage assertions. Do not create another test file.
5. Run the focused harness once after the consolidated source/test edit. On a
   failure, classify it before any rerun; repair only within Allowed scope.
6. Create the worker return from the checker-safe scaffold, run all final
   commands once after the last edit, and leave every owned path uncommitted.

Each step consumes the prior step's files/evidence. A forbidden-path need,
private leakage, unresolved byte drift, or unclear failing test is a stop
condition.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| CP1 bootstrap | MODIFY only the hand-edited merge behavior for byte preservation and marker fail-closed handling |
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

- exact diff of the CP1 repair, carrier subsection, and harness assertions;
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

- [ ] CP1 preserves project-owned outside-block bytes on insertion and refresh;
- [ ] malformed marker structures fail closed without file mutation;
- [ ] CVF-generated refresh behavior remains unchanged;
- [ ] exactly one public-safe carrier subsection is added adjacent to Risk Classification;
- [ ] all five accepted semantics are present and no excluded evidence is present;
- [ ] fresh generated project proof passes hermetically;
- [ ] generated-project second refresh is idempotent and retains one carrier;
- [ ] hand-edited project receives one merge block and retains outside-block bytes;
- [ ] only the three source/test paths and worker return are pending;
- [ ] golden harness, file-size guard, worker-return fast gate, and diff hygiene pass;
- [ ] worker records actual execution base/status and makes no commit.

Fail conditions:

- missing, duplicated, or semantically weakened carrier rule;
- private incident/evidence leakage;
- hand-edited content byte drift or malformed-marker mutation;
- need to modify another bootstrap/helper/catalog/profile/checker/public/session path;
- network/provider call, public-sync, downstream mutation outside disposable
  temp fixtures, or any staged/committed worker change.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Closure evidence | Status |
|---|---|---|---|
| align provenance template surface | Template carrier | template diff | PENDING_IMPLEMENTATION_AUTHORITY |
| focused template tests | Golden harness | hermetic harness result | PENDING_IMPLEMENTATION_AUTHORITY |
| private leakage exclusion | Golden harness negatives | exact sentinel assertions | PENDING_IMPLEMENTATION_AUTHORITY |
| bounded CP1 repair | CP1 byte-preserving merge repair | source diff and byte/malformed-marker evidence | PENDING_IMPLEMENTATION_AUTHORITY |
| independent review | no-commit route | reviewer disposition | PENDING_IMPLEMENTATION_AUTHORITY |

## Design Control Carry-Forward

| Design control | Roadmap source | Work-order handling | Verdict |
|---|---|---|---|
| smallest safe carrier | roadmap Design Control Gate; accepted T1 | one template owner only | PASS |
| public/private boundary | roadmap protected controls | exact included/excluded semantics and sentinel tests | PASS |
| project ownership | roadmap protected controls | generated project `AGENTS.md` remains the consumer | PASS |
| latency control | roadmap protected controls | five-rule carrier; no repeated worker checkpoints | PASS |
| explicit implementation release | operator confirmation on 2026-08-05 | bounded worker dispatch only | PASS |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | generated/refreshed downstream `AGENTS.md` | static guidance only; no mutation/commit authority beyond worker packet | CP1 source and golden harness | internal bootstrap projection only | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no external adapter in this tranche | no ingress, authentication, approval, receipt, raw-data, mutation, or runtime claim | forbidden scope | adapter work requires a separate packet | `DEFERRED_WITH_REASON` |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| existingFoundation | CP1 bootstrap, downstream AGENTS template, and golden bootstrap harness remain their existing owners |
| newDurableFoundation | N/A with reason: no new durable foundation, folder, front door, or owner surface is created |
| storageClass | existing bootstrap source, governed template, and test harness paths |
| splitOrRelocation | N/A with reason: no split, move, relocation, or refactor is authorized |
| indexOrRegistryChange | N/A with reason: no index, catalog, profile, or registry change is authorized |
| datePolicy | N/A with reason: no new stable reference family is created |

## Legacy Absorption Coverage Index Disposition

| Field | Value |
|---|---|
| coverageIndex | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` |
| disposition | NOT_APPLICABLE_WITH_REASON |
| reason | GLP-T2R1 repairs existing bootstrap/template/test owners; it does not absorb, rescan, migrate, or reclassify a legacy source family |
| registryOrIndexMutation | N/A with reason: no legacy coverage or corpus registry change is authorized |
| claimBoundary | no legacy completeness or absorption claim |

## Agent Handoff Contract Control Block

Contract source: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher -> no-commit implementation worker -> independent reviewer/closer -> session-sync steward |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE, SESSION_SYNC |
| baseHeadFor(phase) | dispatchBaseHead=ff27d9904; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | dispatch=paired packets; execution=three source/test paths plus worker return; closure=accepted worker paths and bounded reviewer repairs; session sync=canonical continuity only |
| traceScope(phase, actor) | each actor records phase-local trace and exact changed set |
| commitOwner(phase) | dispatcher commits packets; worker must not commit; reviewer commits accepted material; steward commits continuity |
| crossBatchIsolation | one GLP-T2R1 batch on a clean worktree; unrelated drift blocks execution |
| nextMoveSurfaces | reviewer/closer and steward update only after accepted or blocked T2R1 decision |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_GLP_T2R1_CP1_BYTE_PRESERVING_MERGE_REPAIR_COMPLETION_2026-08-05.md` (optional; use only for unresolved disagreement) |
| reviewerOwnedClosurePaths | worker-owned implementation paths and worker return, plus optional completion review and bounded packet/roadmap lifecycle corrections |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_GLP_T2R1_CP1_BYTE_PRESERVING_MERGE_REPAIR_WORKER_RETURN_2026-08-05.md`

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
| gateRunPurpose | confirmation evidence for released packet fidelity before worker dispatch; not first discovery of worker requirements |
| claimBoundary | packet/readiness structure only; semantic implementation still requires worker evidence and independent review |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author |
| Provider or surface | local private provenance repository |
| Session or invocation | GLP-T2R1 repair packet authoring, 2026-08-05 |
| Working directory | repository root |
| Command or tool surface | startup reads, source verification, scaffold helper, ADIF resolver, apply_patch, dispatch gates |
| Target paths | paired GLP-T2R1 baseline and work order |
| Allowed scope source | GLP roadmap and blocked T2 review at `071866e7b`; continuity authorizes documentation-only repair packet authoring |
| Before status evidence | HEAD `7cdc72393`; clean worktree |
| After status evidence | paired packet ready for one bounded no-commit worker |
| Diff evidence | `git diff --name-status` limited to paired packet paths |
| Approval boundary | bounded GLP-T2R1 implementation dispatch only |
| Claim boundary | no implementation, workspace/project mutation, public sync, provider/network use, push, or deployment |
| Agent type | dispatcher |
| Invocation ID | `glp-t2r1-work-order-authoring-2026-08-05` |
| Expected manifest | paired baseline and this work order |
| Actual changed set | paired baseline and this work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | future bounded CP1 repair, carrier, and hermetic-test implementation |
| claimDisposition | N/A with reason: dispatch-ready work order has not executed |
| receiptEvidence | N/A with reason: no runtime receipt is created |
| actionEvidence | N/A with reason: no implementation action has occurred |
| invocationBoundary | future local source/test edits and hermetic temp fixture only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, or agent-runtime interception claim |
| claimLanguage | deterministic byte-preserving projection proof, not runtime governance enforcement |
| forbiddenExpansion | no other bootstrap/helper, provider/live, external CLI/MCP, public-sync, push, or deployment work |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: the repaired CP1 path carries one public-safe
subsection while preserving project-owned bytes and rejecting malformed markers.

Evidence Comparison Requirement: worker return compares each named harness
assertion with this prediction and preserves any contradiction.

Contradiction Handling Requirement: missing delivery, duplication, leakage,
byte drift, or malformed-marker mutation blocks the tranche and does not
authorize another path.

Claim Update Requirement: report confirmed, narrowed, or blocked projection;
do not infer production adoption from a disposable harness.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next action |
|---|---|---|---|---|
| accepted latency control is absent from the mandatory project carrier | RULE_GAP | GOVERNANCE_CONTROL_PLANE | IMPLEMENTATION_HELD | after authority release, add the compact rule and prove projection through the repaired CP1 path |
| CP1 whole-file rewrite violates byte-preservation contract | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | REPAIR_PACKET_HELD | after authority release, implement only the bounded CP1 byte repair |

No new ADIF entry is required unless execution reveals a repeated or
non-obvious defect distinct from ADIF-0026.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: GLP-T2R1 repairs a local source contradiction and performs no absorption |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | downstream AGENTS template |
| Disposition | NOT_APPLICABLE_WITH_REASON: no new external source is absorbed in T2R1 |
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

The operator explicitly authorized the expanded GLP-T2R1 CP1 scope on
2026-08-05. Dependent same-scope repairs require no repeated confirmation while
objective, paths, R2 ceiling, external-effect class, and commit owner remain
unchanged.

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
network/provider need, or any scope beyond the four worker-owned paths.

## Claim Boundary

This work order dispatches one bounded no-commit GLP-T2R1 worker. It does not
authorize broader
workspace/project mutation, prove real-world adoption, publish, call a
provider, use the network, push, or deploy.
