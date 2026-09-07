# CVF Agent Work Order - DARA T2B Operator-Authorized Internal Recovery

Memory class: governed-worker-dispatch

docType: work_order

Status: CLOSED_PASS_BOUNDED

Batch ID: DARA-T2B-OPERATOR-AUTHORIZED-INTERNAL-RECOVERY

Dispatch base head: 0ba931bb1073afef3b4e5c376fc9161548c759b0

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: internal implementation worker

Reviewer/closer: reviewer/closer role

Worker return path: `docs/reviews/CVF_DARA_T2_ARCHITECTURE_READINESS_ADMISSION_IMPLEMENTATION_WORKER_RETURN_2026-09-06.md`

providerExecutionAuthority: FORBIDDEN

## Dispatch Prompt Envelope

Role: internal implementation worker for DARA-T2B.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_DARA_T2B_OPERATOR_AUTHORIZED_INTERNAL_RECOVERY_2026-09-07.md`.

Recovery route: `OPERATOR_AUTHORIZED_INTERNAL_RECOVERY`.

Transport: operator manual copy/paste only. The orchestrator must not invoke
an external worker through CLI or another direct provider-control surface.

Consumer boundary: before editing, confirm that this execution qualifies as
`INTERNAL_AGENT` under the Dual Agent Surface Accounting Standard. If it
crosses an independent provider, account, credential, process, durable-action,
or external authority boundary, stop and return `BLOCKED_SURFACE_MISMATCH`.
Manual copy/paste does not make an external model internal.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: predecessor review round is 3; external invocation count
and ceiling remain 2/2; operator-reported elapsed time is 200 minutes; exact
quota usage is unavailable. The DARA candidate is uncommitted and the two
WP-ARCH-003 files are parked.

Do-not-misread notes: repair only the exact 14-path candidate. Do not edit this
work order, its baseline, the roadmap, committed reviews, MFRP, ADIF, session
state, active handoff, WP-ARCH-003, runtime/provider/public surfaces, or create
a new output file. Do not commit.

Return contract: update the existing worker return in place, preserve truthful
predecessor telemetry, run the exact focused proof after the last material
edit, and return `COMPLETE_PENDING_REVIEW`, `BLOCKED_WITH_REASON`, or
`BLOCKED_SURFACE_MISMATCH`. The reviewer evaluates the evidence and does not
recreate the repair.

Required first actions: read the startup front door, active bootstrap and
handoff, this work order, paired baseline, committed R3 review, accepted R1/R2
amendments, guard orientation, literal gotchas, and named checker sources;
capture HEAD/full status/staging; verify internal surface and exact manifests;
run pre-implementation before editing.

## Purpose

Repair the complete committed DARA-T2 R3 finding set as one internal,
no-commit recovery assignment. Close the accepted-echo identity bypass, the
three closed-chain omissions, and the dependent test-evidence overstatement
without consuming a third external invocation or expanding the 14-path worker
manifest.

## Authority Chain

1. `ECOSYSTEM/doctrine/` and `ECOSYSTEM/operating-model/`.
2. `AGENTS.md` and current work-order, review-cost, dual-agent, and commit
   choreography standards.
3. `docs/roadmaps/CVF_DISPATCHER_ARCHITECTURE_READINESS_AND_QUOTA_ADMISSION_ROADMAP_2026-09-06.md`.
4. `docs/reviews/CVF_DARA_T2_R2_FINAL_IMPLEMENTATION_COMPLETION_REVIEW_2026-09-07.md`
   at commit `ceadf2c3ff8d5e42d37d974a5ba8c1413b617ccb`.
5. `docs/baselines/CVF_GC018_DARA_T2B_OPERATOR_AUTHORIZED_INTERNAL_RECOVERY_2026-09-07.md`.
6. Operator instruction dated 2026-09-07 opening
   `OPERATOR_AUTHORIZED_INTERNAL_RECOVERY`, retaining the current agent as
   orchestrator/reviewer, prohibiting external-worker CLI use by the orchestrator, and
   reserving worker-packet relay to the operator.

Authority boundary: this packet is internal-only, exact-manifest, no-commit,
and provider-free. Any surface mismatch or required path outside the manifest
stops execution.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL

dispatchSurface: INTERNAL_AGENT

parentAssignmentId: DARA-T2B-OPERATOR-AUTHORIZED-INTERNAL-RECOVERY

reviewRoundCount: 0

priorFindingSetDigest: NOT_APPLICABLE_INITIAL_DISPATCH

dependencyAuditDisposition: COMPLETE_INITIAL_ACCEPTANCE_MATRIX

reworkFindingDisposition: NOT_APPLICABLE_INITIAL_DISPATCH

newIndependentCriticalEvidence: NONE

regressionGuardDisposition: BASELINE_NEGATIVE_TESTS_PLANNED

cumulativeExternalInvocationCount: 2

externalInvocationCeiling: 2

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

Predecessor history is not reset: DARA-T2 reached review round 3, used two
external invocations, and was rejected on two new critical root causes plus
three dependent findings. This new parent assignment exists only because the
committed review changed the critical authority boundary and the operator
explicitly authorized an internal recovery route.

## Accepted Architecture Identity Echo

Architecture-Readiness Admission: NOT_APPLICABLE_ACCEPTED_DESIGN_ECHO

architectureMatrixSchema: cvf.dara.architectureBindingMatrix.v1

architectureMatrixCanonicalDigest: 8d82ed44b5f5e66576639e54e610f4bd659210561fe6a2b6ac1a4b8b15b221b2

architectureSemanticReviewPath: docs/reviews/CVF_DARA_T2_R1_ROOT_CONTRACT_AND_MANIFEST_AMENDMENT_REVIEW_2026-09-07.md

architectureSemanticReviewCommit: 1316ea7340541ab8e675c5b1965f5a1ff3ef52d0

architectureSemanticReviewFileSha256: 677a7647a810fd78340b217c319dfbb7201da7ee5d3426889c503435b1008984

architectureBindingEchoDisposition: EXACT_MATCH

These values are genuine committed identity evidence. The worker must make the
validator verify them through the same immutable path as a required matrix; it
must not special-case this packet to obtain a pass.

## Semantic Convergence Outcome

Standard: `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "DARA-T2B-INTERNAL-RECOVERY",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {
    "prior": ["fabricated_accepted_echo", "unresolved_trust_locator", "rollback_outside_writable_manifest", "private_legacy_owner", "unbound_test_identity"],
    "resolved": [],
    "retained": ["fabricated_accepted_echo", "unresolved_trust_locator", "rollback_outside_writable_manifest", "private_legacy_owner", "unbound_test_identity"],
    "new": [],
    "reopened": [],
    "current": ["fabricated_accepted_echo", "unresolved_trust_locator", "rollback_outside_writable_manifest", "private_legacy_owner", "unbound_test_identity"]
  },
  "resolutionEvidence": {},
  "counters": {"partialReadyClosures": 0, "reviewerScopeExpansions": 0, "sameClaimCorrections": 0, "nonDecreasingBlockerTransitions": 0},
  "claims": [{"claimId": "DARA-T2B-DISPATCH", "claimClass": "DOCUMENTATION_ONLY", "proofClass": "PROPOSAL_ONLY_NO_RUNTIME_READINESS", "evidenceRef": "docs/reviews/CVF_DARA_T2_R2_FINAL_IMPLEMENTATION_COMPLETION_REVIEW_2026-09-07.md"}],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"DARA-T2B-OPERATOR-AUTHORIZED-INTERNAL-RECOVERY","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"PURE_LOCAL_IMPLEMENTATION","authorityImpact":"ENRICHES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"KNOWN_PATTERN"},"pathFamilies":["docs/assessments/","docs/baselines/","docs/reference/","docs/reviews/","docs/roadmaps/","docs/work_orders/","governance/compat/"],"claims":["one internal recovery can repair the complete committed R3 finding set"],"requiredProof":["immutable echo negative tests","closed-chain containment tests","real test identity map","exact 14-path manifest","zero external calls","no-commit return"],"operatorCheckpoints":["surface mismatch","reviewer terminal disposition","provider/live","public sync"],"forbiddenEffects":["external invocation 3","worker commit","new implementation path","MFRP change","WP-ARCH-003 change","runtime provider call","session mutation","public sync","automatic successor"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"N/A with reason: bounded named files","completenessClaimChanged":false}}
```

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| exact architecture bindings remain controlling | Accepted Architecture Identity Echo; Source Verification Block | genuine committed echo identity | immutable echo hostile tests | PASS |
| block fabricated echo and incomplete closed chain | Architecture Readiness Repair Contract | shared identity validator, locator resolution, rollback containment, authority rejection | HT-IR-02 through HT-IR-13 | PASS |
| preserve worker fault attribution and cost history | Fault Attribution And Foundation Learning Contract | predecessor round 3, count 2/2, elapsed 200, quota unavailable | return evidence comparison | PASS |
| no duplicate reviewer work | Reviewer Non-Duplication Contract | reviewerWorkBoundary | reviewer-return evidence ledger | PASS |
| no external invocation 3 | Review Dispatch Convergence And Invocation Budget Control | INTERNAL_AGENT; cumulative count 2; ceiling 2 | surface declaration plus zero-call evidence | PASS |
| no WP-ARCH-003 repair before DARA closure | Forbidden Path Manifest | two parked hash-bound paths | before/after SHA-256 | PASS |
| no automatic DARA-T3 opening | Claim Boundary | successorTrancheOpened remains NO | final return and reviewer disposition | PASS |

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | committed DARA R3 review and existing uncommitted 14-path candidate |
| Route | `MULTI_AGENT_MULTI_ROLE` |
| canonical route mode | `MULTI_AGENT_MULTI_ROLE` |
| scope classification | bounded local governance recovery under a new parent assignment |
| risk sensitivity | HIGH because pre-dispatch authority and containment checks are repaired |
| selected role route | operator relays packet; internal worker edits without commit; reviewer evaluates returned evidence and owns disposition |
| External agent disposition | blocked at predecessor ceiling 2/2; no external worker is admitted |
| escalation condition | recipient is external, required path is outside exact 14, current authority contradicts the packet, or a provider/live/public effect is required |

## Agent Roles

- Operator: owns manual prompt relay and any future external/quota expansion.
- Orchestrator: authors and commits the dispatch packet, preserves scope,
  and does not implement the worker repair.
- Worker: one qualifying internal agent executes only this packet and does not
  commit.
- Reviewer/closer: consumes returned evidence, performs only admitted
  focused checks, and decides acceptance or block.

## Worker Autonomy / No-Question Rule

Within the exact worker manifest, repair implementation and tests, reconcile
the existing return, and rerun failed focused gates without asking for routine
operator preferences. Stop only for surface mismatch, source contradiction,
out-of-manifest repair, higher risk, provider/live/public action, secret use,
or destructive/irreversible action.

## Required First Reads

| Path | Action | Reason |
|---|---|---|
| `CVF_SESSION_MEMORY.md` | FULL_READ | session front door and current boundary |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | FULL_READ | current mode and next move |
| `AGENT_HANDOFF_V59_2026-08-11.md` | FULL_READ | active handoff only |
| `docs/reference/guard_orientation/README.md` | FULL_READ | worker and protected-path guards |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | FULL_READ | literal and gate traps |
| `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md` | FULL_READ | recovery history and reviewer boundary |
| `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | FULL_READ | internal/external classification |
| `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md` | FULL_READ | no-commit and closure ownership |
| `docs/reviews/CVF_DARA_T2_R2_FINAL_IMPLEMENTATION_COMPLETION_REVIEW_2026-09-07.md` | FULL_READ | complete finding set |
| `docs/assessments/CVF_DARA_T2_R1_ROOT_CONTRACT_AND_MANIFEST_AMENDMENT_2026-09-07.md` | FULL_READ | controlling R1-02/R1-03 semantics |
| `docs/assessments/CVF_DARA_T2_R2_ROOT_CONTRACT_COMPLETION_AMENDMENT_2026-09-07.md` | FULL_READ | exact 14-path and base-debt authority |
| `docs/baselines/CVF_GC018_DARA_T2B_OPERATOR_AUTHORIZED_INTERNAL_RECOVERY_2026-09-07.md` | FULL_READ | recovery authorization |

Also read every implementation/test file in the exact worker manifest before
the first edit. Provider-specific memory or IDE summaries are not authority.

## Pre-Flight Checks

Run before editing:

```powershell
git rev-parse HEAD
git status --short --untracked-files=all
git diff --cached --name-only
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 0ba931bb1073afef3b4e5c376fc9161548c759b0 --head HEAD
```

Expected: current HEAD equals the committed dispatch HEAD supplied by the
operator; staging is empty; the exact 14 DARA candidate paths and two parked WP
paths are visible; no other unexpected path exists. If the packet itself is
not committed, the recipient is external, staging is nonempty, or the candidate
manifest differs, stop before editing.

## Scope / Target / Owner Boundary

Allowed scope: modify only the exact 14 worker paths below to satisfy IR-01
through IR-10. The worker may inspect committed authority and run local tests.

Forbidden scope: all other paths and all external effects. Risk ceiling: R2
local reversible guard/test repair. No live proof is required or authorized.

## Planned Worker Fulfillment Manifest

| Path | Required at handoff | Purpose |
|---|---|---|
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | Yes | current pending DARA template integration remains in exact candidate |
| `docs/reference/CVF_ARCHITECTURE_READINESS_ADMISSION_STANDARD_2026-09-07.md` | Yes | current pending DARA standard remains in exact candidate |
| `governance/compat/build_dispatch_packet_scaffold.py` | Yes | current pending DARA scaffold integration |
| `governance/compat/build_dispatch_packet_architecture_readiness.py` | Yes | current pending architecture rendering helper |
| `governance/compat/build_worker_return_skeleton_scaffold.py` | Yes | accepted-echo parity |
| `governance/compat/check_work_order_dispatch_quality.py` | Yes | validator composition and writable-manifest data flow |
| `governance/compat/check_work_order_dispatch_quality_range.py` | Yes | shared immutable identity validation and owner boundary |
| `governance/compat/check_work_order_dispatch_quality_source.py` | Yes | locator resolution, rollback containment, authority rejection |
| `governance/compat/run_worker_return_scaffold.py` | Yes | accepted-echo parity |
| `governance/compat/test_build_dispatch_packet_scaffold.py` | Yes | scaffold regression |
| `governance/compat/test_check_work_order_dispatch_quality_architecture_readiness.py` | Yes | all IR hostile cases and real test identities |
| `governance/compat/test_run_worker_return_scaffold.py` | Yes | return scaffold regression |
| `governance/compat/check_work_order_dispatch_quality_architecture_schema.py` | Yes | schema owner retained in final candidate |
| `docs/reviews/CVF_DARA_T2_ARCHITECTURE_READINESS_ADMISSION_IMPLEMENTATION_WORKER_RETURN_2026-09-06.md` | Yes | truthful in-place recovery return |

Cleanup invariant: `governance/compat/test_check_work_order_dispatch_quality.py`
must be byte-identical to execution base and absent from final diff.

## Forbidden Path Manifest

| Path | Reason |
|---|---|
| `docs/roadmaps/**` | orchestrator-owned authority, not worker scope |
| `docs/baselines/**` | dispatch authority, not worker scope |
| `docs/work_orders/**` | dispatch authority, not worker scope |
| `docs/reference/agent_defect_intelligence/**` | no ADIF expansion in recovery |
| `CVF_SESSION/**` | session-sync is reviewer/closer owned |
| `CVF_SESSION_MEMORY.md` | session front door is protected |
| `AGENT_HANDOFF_V59_2026-08-11.md` | active handoff is protected |
| `docs/assessments/CVF_PHASE04_WAVE0_WP_ARCH_003_OWNER_GAP_AUDIT_2026-09-06.md` | parked incident evidence; preserve SHA-256 `91b2a5c07fcf341c94f3adbcaab040ec7e343a4a7faf523becabad17ec321f27` |
| `docs/reviews/CVF_PHASE04_WAVE0_WP_ARCH_003_OWNER_GAP_AUDIT_WORKER_RETURN_2026-09-06.md` | parked incident evidence; preserve SHA-256 `ce137665a13a852c05ed0b03aca60c58c6feb7829ff4fe3e7335f4c3209ba8ac` |

## Architecture Readiness Repair Contract

### R3-01 Shared immutable identity path

The accepted-design echo branch must call the same immutable semantic-review
identity validation used by the required/accepted-bounded route. It must verify
40-lowercase-hex commit shape, repository resolution, ancestry from current
HEAD, path presence in the committed tree, committed bytes, exact SHA-256,
canonical digest relationship, required criterion identity, and exact echo
disposition. Do not duplicate a weaker echo-only validator.

### R3-02 Closed-chain completion

- Normalize and resolve each `trustSource.locator` against the cited authority
  file bytes; nonempty text is insufficient.
- Pass the exact writable manifest into row validation and require every
  normalized rollback path to be a member of it.
- Apply one normalized private/archive/legacy-private rejection helper to
  trust-source paths, canonical-owner paths, and canonical-authority paths.
- Preserve fail-closed behavior for malformed or missing fields.

### R3-03 Evidence truth

Add tests with discoverable stable names for each repaired negative case.
Before updating the return, prove every cited test symbol exists using an exact
repository search or test collection. Remove nonexistent `test_ht*` names and
do not convert a passing count into proof of an untested predicate.

## Hostile Test And Acceptance Matrix

| ID | Required negative or positive case | Expected result |
|---|---|---|
| HT-IR-01 | genuine accepted echo identity | PASS |
| HT-IR-02 | fabricated commit | blocking identity issue |
| HT-IR-03 | non-ancestor commit | blocking identity issue |
| HT-IR-04 | review path missing from commit | blocking identity issue |
| HT-IR-05 | wrong committed-byte SHA | blocking identity issue |
| HT-IR-06 | arbitrary canonical digest | blocking identity issue |
| HT-IR-07 | required criterion absent from committed review | blocking identity issue |
| HT-IR-08 | trust locator absent from cited bytes | blocking locator issue |
| HT-IR-09 | rollback path `AGENTS.md` outside writable manifest | blocking containment issue |
| HT-IR-10 | private legacy trust source | blocking authority issue |
| HT-IR-11 | private legacy canonical owner | blocking authority issue |
| HT-IR-12 | private legacy canonical authority | blocking authority issue |
| HT-IR-13 | valid public canonical owner/authority and valid locator | PASS |
| HT-IR-14 | both worker-return scaffold routes | exact identity-echo parity |

## Execution Plan

1. Capture execution HEAD, full status, staging, exact candidate manifest,
   cleanup equality, and parked-file hashes. Stop on mismatch.
2. Read the complete finding set and trace data flow across range, source,
   schema, top-level checker, scaffold, and return paths before editing.
3. Implement the shared immutable validator and closed-chain predicates without
   new files or exception changes.
4. Add all HT-IR tests and verify their identities are discoverable.
5. Run focused tests after the last code edit, then update the existing worker
   return with actual commands/results and predecessor cost history.
6. Run final focused tests, size gates, worker-return fast gate, automation
   assist, and pre-implementation; repair allowed-scope failures and rerun.
7. Record final status/diff/hash evidence, leave staging empty, do not commit,
   and return for one terminal reviewer decision.

## Evidence Requirements

- exact execution base HEAD and final HEAD;
- exact final 14-path `git diff --name-only` reconciliation;
- cleanup-only base equality;
- both parked WP hashes before and after;
- test collection or exact searches proving every cited test identity exists;
- focused test commands and counts after the last material edit;
- first and final gate results without relabeling a nonzero exit as PASS;
- zero internal helper/provider/external invocation counts stated separately;
- predecessor external count 2/2 preserved;
- worker elapsed time when measured and quota usage or exact unavailable reason;
- no-commit and empty-staging evidence.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id DARA-T2B-OPERATOR-AUTHORIZED-INTERNAL-RECOVERY --title "DARA T2B Operator-Authorized Internal Recovery" --date 2026-09-07 --base 0ba931bb1073afef3b4e5c376fc9161548c759b0 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --review-round-count 0 --cumulative-external-invocation-count 2 --external-invocation-ceiling 2 --stdout` |
| generatedProfile | protected-governance-path plus no-commit internal-worker profile |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | authored from committed template and accepted DARA precedent because the helper working tree is part of the rejected candidate under recovery |
| checkerReadAheadConfirmation | dispatch, convergence, source, protected-path, handoff, worker-return, trace, size, and public guards |
| docOnlyNewFields | recovery route, manual transport, predecessor telemetry, and surface mismatch stop |
| claimBoundary | provenance only; no implementation or internal-surface proof |

## Fault Attribution And Foundation Learning Contract

Record `dispatcherDefectCount`, `workerExecutionDefectCount`,
`reviewerLateDiscoveryCount`, `repairIntroducedDefectCount`,
`avoidableExternalInvocationCount`, and `tokenOrQuotaUsage`. Preserve the
committed attribution that R3-01/R3-02 are worker contract-execution defects
against explicit R1 requirements and R3-03 is dependent evidence
interpretation. Do not generalize this into worker unreliability or erase the
earlier orchestrator defects.

Operator-supplied cost baseline: 200 elapsed minutes for the observed run;
exact quota not measured. New measurements must state source and boundary.

## Reviewer Non-Duplication Contract

The reviewer will consume valid returned evidence. No per-row review, broad
suite replay, or implementation recreation is admitted. A focused rerun needs
a named contradiction or insufficiency, bounded claim, expected information
gain, and cost reason. One terminal review will decide acceptance or block.

## Verification Commands

Run the narrowest applicable forms supported by current `--help`; do not invent
flags. At minimum:

```powershell
python -m pytest governance/compat/test_check_work_order_dispatch_quality_architecture_readiness.py -q
python -m pytest governance/compat/test_build_dispatch_packet_scaffold.py governance/compat/test_run_worker_return_scaffold.py -q
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/check_python_automation_size.py --enforce
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_work_order_dispatch_quality_architecture_readiness.py --pytest-target governance/compat/test_build_dispatch_packet_scaffold.py --pytest-target governance/compat/test_run_worker_return_scaffold.py
python governance/compat/run_agent_automation_assist.py --base <executionBaseHead> --head HEAD --json --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
git diff --check
git status --short --untracked-files=all
git diff --cached --name-only
```

No release-quality live gate is applicable because this tranche makes no CVF
governance-behavior release claim and forbids provider/live execution.

## Acceptance Criteria

- [x] IR-01 through IR-10 pass with command-backed evidence.
- [x] HT-IR-01 through HT-IR-14 exist and pass with the expected outcomes.
- [x] Final worker diff was exactly 14 paths and no new implementation file existed.
- [x] Cleanup-only path was base-equal and absent from final diff.
- [x] Both parked WP hashes matched at worker return; the later operator-authorized evidence normalization is preserved separately at `c2a1f7c7c`.
- [x] Worker return cites only real tests and truthful final commands.
- [x] External count remains 2/2; this recovery used zero external/provider calls.
- [x] Staging was empty and the worker made no commit.

Fail conditions: surface mismatch; missing or fabricated evidence; any fail-open
hostile case; any extra path; exception increase; parked hash drift; external,
provider, live, public, credential, destructive, commit, or push action.

## Return-To-Orchestrator Conditions

Return immediately with a reason if the recipient is not internal, authority
conflicts, a required repair needs a fifteenth path, a protected path is not
listed, final evidence remains nonzero, an external effect is needed, or the
exact candidate/parked-file state differs from dispatch evidence.

## Operator Checkpoint

No operator checkpoint is required for routine allowed-scope repair. Operator
authority is required for any external recipient or call, external ceiling
increase, new path, risk/claim expansion, provider/live/public action,
credential use, destructive action, commit, or push.

## Evidence Reuse And Encoding Plan

verificationMode: REUSE_PRIOR_VERIFICATION

priorVerificationArtifact: docs/reviews/CVF_DARA_T2_R2_FINAL_IMPLEMENTATION_COMPLETION_REVIEW_2026-09-07.md

priorVerificationAnchor: ceadf2c3ff8d5e42d37d974a5ba8c1413b617ccb

freshRecomputeRequired: targeted repaired predicates, exact final manifest, cleanup equality, parked hashes, test identities, and final focused gates only

unicodePathHandling: use literal Windows-safe paths and UTF-8 readers with replacement for subprocess output

extractedTextAuthority: committed CVF source bytes only; provider-local memory and conversation summaries are not authority

## Negative Search And Collision Discipline

| Check | Evidence requirement | Disposition |
|---|---|---|
| new implementation path | final untracked/diff inventory contains no path beyond exact 14 | MUST_PASS |
| test identity | exact symbol search or test collection resolves every cited test | MUST_PASS |
| private authority | hostile trust/owner/authority cases are rejected | MUST_PASS |
| extra review or return | worker updates only the existing return | MUST_PASS |
| parallel MFRP surface | no collector/readout/receipt path changes | MUST_PASS |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| accepted echo bypass | committed reviewer evidence | `docs/reviews/CVF_DARA_T2_R2_FINAL_IMPLEMENTATION_COMPLETION_REVIEW_2026-09-07.md` | DARA-T2-R3-01 | NOT_APPLICABLE_ACCEPTED_DESIGN_ECHO | DARA range validator | ACCEPT |
| locator, rollback, and authority gaps | committed reviewer evidence | `docs/reviews/CVF_DARA_T2_R2_FINAL_IMPLEMENTATION_COMPLETION_REVIEW_2026-09-07.md` | DARA-T2-R3-02 | trustSource | DARA source validator | ACCEPT |
| test evidence overstatement | committed reviewer evidence | `docs/reviews/CVF_DARA_T2_R2_FINAL_IMPLEMENTATION_COMPLETION_REVIEW_2026-09-07.md` | DARA-T2-R3-03 | test_ht13_accepted_design_echo_passes | worker-return evidence contract | ACCEPT |
| exact 14-path authority | accepted amendment | `docs/assessments/CVF_DARA_T2_R2_ROOT_CONTRACT_COMPLETION_AMENDMENT_2026-09-07.md` | Exact Manifest Reconciliation | check_work_order_dispatch_quality_architecture_schema.py | DARA R2 amendment | ACCEPT |
| immutable binding semantics | accepted root contract | `docs/assessments/CVF_DARA_T2_R1_ROOT_CONTRACT_AND_MANIFEST_AMENDMENT_2026-09-07.md` | R1-02 and R1-03 | architectureSemanticReviewCommit | DARA R1 amendment | ACCEPT |
| internal consumer boundary | active standard | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | Core Rule | INTERNAL_AGENT | dual-agent accounting | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045,
ADIF-0051, ADIF-0052, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024,
ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006.

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 50 --json` |
| Returned defect count | 22 |
| Disclosed defectIds | all IDs listed above |
| Dispatch impact | route truth, source fidelity, exact paths, protected authorization, real test identity, pending-return freshness, and commit separation |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_range.py`; `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_python_automation_size.py` |
| literalTokensReviewed | CLOSED_PASS_BOUNDED, INITIAL internal convergence values, accepted design echo, source table columns, protected authorization, no-commit return, trace labels, private export disposition |
| gateRunPurpose | confirm this complete internal-only recovery packet after source and checker read-ahead; not first discovery |
| claimBoundary | gate conformance cannot accept implementation or reclassify an external worker as internal |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| existing owner surfaces | retain the current DARA standard, range/source/top-level validators, schema helper, scaffold routes, and tests |
| new owner surface | none |
| overlap rule | share identity and authority helpers; do not create a second recovery framework, receipt, readout, or collector |
| output storage | update the existing DARA worker return in place |
| maintainability | no exception-registry increase; size guards must pass |

## Write Ownership

Write mode: modify-listed only. Owned paths are exactly the 14 rows in Planned
Worker Fulfillment Manifest. Every other path is forbidden.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | operator -> orchestrator/dispatcher -> no-commit internal implementation worker -> reviewer/closer |
| phase | DARA-T2B operator-authorized internal recovery |
| baseHeadFor(phase) | dispatchBaseHead=0ba931bb1073afef3b4e5c376fc9161548c759b0; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exact 14 worker paths; cleanup-only path absent final diff; two parked WP paths excluded |
| traceScope(phase, actor) | worker records surface, diff, hashes, tests, gates, cost, failures and no-commit; reviewer consumes returned evidence |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer only after acceptance |
| crossBatchIsolation | cross-batch worktree clean: no unrelated tracked edits; only the exact held DARA candidate and two hash-bound parked exemptions may be present |
| nextMoveSurfaces | existing worker return, then one terminal reviewer decision; no external invocation 3, DARA-T3, or WP repair |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | exact 14-path DARA candidate | local reversible edit, no commit, no external effect | this packet, committed R3 review, focused tests, existing return | internal workspace only; operator may relay text without widening scope | IMPLEMENTED |
| `EXTERNAL_AGENT_CLI_MCP` | execution excluded from DARA-T2B | predecessor count and ceiling 2/2; no third external invocation | committed final review plus explicit surface check | no CLI/MCP/provider adapter; external recipient must stop | N/A_WITH_REASON |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | predecessor returned evidence -> committed local review -> bounded internal recovery |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | DARA roadmap, accepted amendments, committed final review, this work order |
| Disposition | consume committed review evidence; no new external intake or invocation |
| Claim boundary | predecessor external return is evidence input only; this packet grants no external authority |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: this is a bounded repair of named local files and
makes no corpus, copied-folder, or external-repository absorption claim.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | reviewer may create one conventional completion review only if needed; worker ownership is forbidden |
| reviewerOwnedClosurePaths | accepted 14-path material, existing worker return, optional reviewer completion artifact, and separate continuity update |
| closureOwner | reviewer/closer role |
| workerCommitPermission | FORBIDDEN |

The reviewer captures a fresh closure base, commits only accepted owned
material, runs the committed-range closure gate, then performs continuity sync
separately when the next allowed move changes.

## Worker Output Checker Read-Ahead Mandate

Before editing the existing return, read the constants and applicability rules
for worker-return quality, structural completeness, finding learning, trace,
external intake, epistemic process, delta boundary, public disposition, and
file size. Required section names include Target / Source, Scope / Methodology,
Findings / Position, Risk / Corrective Action, Decision / Disposition, Checker
Source Read-Ahead Block, Agent Operation Trace Block, External Knowledge Intake
Routing, Epistemic Process Block, Changed Files, git status, and No-Commit
Statement. Use N/A with a reason only where the governing checker permits it.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

workerReturnPath: `docs/reviews/CVF_DARA_T2_ARCHITECTURE_READINESS_ADMISSION_IMPLEMENTATION_WORKER_RETURN_2026-09-06.md`

Existing-file rule: do not generate another skeleton or return; update the
existing checker-safe return in place.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: repair only the DARA candidate on the
protected implementation and test paths in the exact 14-path manifest.

Protected paths:

- `governance/compat/build_dispatch_packet_scaffold.py`
- `governance/compat/build_dispatch_packet_architecture_readiness.py`
- `governance/compat/build_worker_return_skeleton_scaffold.py`
- `governance/compat/check_work_order_dispatch_quality.py`
- `governance/compat/check_work_order_dispatch_quality_range.py`
- `governance/compat/check_work_order_dispatch_quality_source.py`
- `governance/compat/run_worker_return_scaffold.py`
- `governance/compat/test_build_dispatch_packet_scaffold.py`
- `governance/compat/test_check_work_order_dispatch_quality_architecture_readiness.py`
- `governance/compat/test_run_worker_return_scaffold.py`
- `governance/compat/check_work_order_dispatch_quality_architecture_schema.py`

Operator authorization: operator instruction dated 2026-09-07 explicitly
opened `OPERATOR_AUTHORIZED_INTERNAL_RECOVERY`, retained the current agent as
orchestrator/reviewer, prohibited orchestrator use of an external-worker CLI, and reserved
manual worker-packet relay to the operator.

Rollback boundary: revert only the DARA-T2B worker edits if rejected. Preserve
committed DARA authorities/reviews, P4-C1, continuity, and parked WP evidence.

Not authorized: external invocation 3, new path, exception increase, MFRP or
session mutation, provider/live/public action, worker commit, or push.

## Commit Mode And Base-Anchor Lifecycle

- `dispatchBaseHead`: `0ba931bb1073afef3b4e5c376fc9161548c759b0` for authoring provenance.
- `executionBaseHead`: worker captures current committed dispatch HEAD before
  editing and records it in the return.
- `closureBaseHead`: reviewer captures only after accepting the pending return.
- Worker must leave staging empty and make no commit.
- Reviewer owns any material commit and later continuity/handoff sync.

## Review Gate

Worker handoff is admitted only when the exact return is current and all
required final focused commands are zero-exit. Reviewer applies
`EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION` and performs one
terminal review. Closure requires an accepted exact manifest, no critical
finding, a reviewer-owned commit, and committed-range pre-closure evidence.

## Closure Checklist

- [x] Surface classification is `INTERNAL_AGENT` and zero external/provider calls occurred.
- [x] Exact 14-path manifest and cleanup equality pass.
- [x] IR-01 through IR-10 and HT-IR-01 through HT-IR-14 pass.
- [x] Existing return contains real test identities and current final evidence.
- [x] Parked WP evidence is preserved through the authorized transition at `c2a1f7c7c`.
- [x] Worker made no commit and staging was empty.
- [x] Reviewer disposition and material commit `483176267` are complete.
- [x] DARA-T3 and WP-ARCH-003 remain parked unless separately released.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | orchestrator/reviewer role; future internal worker is separately identified in return |
| Provider or surface | local private CVF workspace; operator manual relay |
| Session or invocation | DARA-T2B recovery dispatch authoring, 2026-09-07 |
| Working directory | repository root |
| Command or tool surface | governed reads, ADIF resolver, `rg`, `apply_patch`, local gates, git; no external-worker CLI |
| Target paths | DARA roadmap, paired baseline, this work order; worker later owns exact 14 candidate paths |
| Allowed scope source | operator instruction dated 2026-09-07 and committed R3 review |
| Before status evidence | cross-batch worktree clean of unrelated tracked edits at HEAD `0ba931bb1073afef3b4e5c376fc9161548c759b0`; exact held 14-path DARA candidate plus two explicit hash-bound parked exemptions; staging empty |
| After status evidence | orchestrator authored dispatch artifacts only and did not edit worker candidate |
| Diff evidence | `git diff --name-status`; `git status --short --untracked-files=all` |
| Approval boundary | internal recovery dispatch authoring and later reviewer disposition |
| Claim boundary | no worker implementation, external/provider call, ceiling increase, acceptance, runtime, or production claim |
| Agent type | orchestrator/reviewer |
| Invocation ID | `dara-t2b-operator-authorized-internal-recovery-dispatch-2026-09-07` |
| Expected manifest | DARA roadmap, paired baseline, this work order |
| Actual changed set | same three orchestrator-owned paths; existing worker/WP paths remain unstaged |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | one internal no-commit repair of the exact 14-path DARA candidate |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: local pending worker return, no runtime receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT through exact diff, tests, gates, and return |
| invocationBoundary | operator-mediated text relay and local repository edits only; no direct orchestrator provider invocation |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, account, or out-of-band action interception claim |
| claimLanguage | packet authorizes bounded internal editing and evidence return only |
| forbiddenExpansion | no external reclassification, provider/live action, runtime release, public sync, commit, push, DARA-T3, or WP repair |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private internal-recovery dispatch; no public-sync authority.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | terminal `CLOSED_PASS_BOUNDED`; acceptance and closure checklists complete | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_DARA_T2B_INTERNAL_RECOVERY_COMPLETION_REVIEW_2026-09-07.md` | exact 15-path material commit `483176267`; bounded terminal decision | PASS |
| Roadmap state | `docs/roadmaps/CVF_DISPATCHER_ARCHITECTURE_READINESS_AND_QUOTA_ADMISSION_ROADMAP_2026-09-06.md` | DARA-T2B accepted bounded; DARA-T3 parked | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`; `docs/corpus-intelligence/registry/entries/phase04-wave0-wp-arch-003-bounded-owner-gap-source-audit.json` | GC-051 source/aggregate match committed at `c2a1f7c7c` | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | existing operator lookup remains valid; no Markdown registry mutation required | PASS |
| External evidence digest | N/A with reason: no external path or external artifact was accepted | repo-local committed evidence and zero provider/live calls | N/A with reason: no external evidence digest |
| System loop interlock | N/A with reason: no downstream tranche opens | DARA-T3 and WP-ARCH-003 remain parked | N/A with reason: no loop transition |
| Session continuity | `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `AGENT_HANDOFF_V59_2026-08-11.md` | handoff recognizes material HEAD `483176267`; dedicated final sync follows closeout | PASS |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| accepted-design echo identity fails closed on missing or altered digest | valid echo yields zero issues; missing SHA, arbitrary digest and missing disposition each block | PASS |
| exact worker manifest and no-commit boundary | fourteen worker-owned paths; cleanup-only path absent; worker staging empty | PASS |
| external/provider quota boundary | cumulative external count remains 2/2; provider call count 0 | PASS |
| reviewer terminal evidence | completion review and exact 15-path material commit `483176267` | PASS |

## Claim Boundary

This work order governed one completed internal recovery assignment based on committed new
critical evidence and explicit operator authority. It does not classify manual
contact with an external model as internal, raise the 2/2 external ceiling,
repair or accept DARA-T2 by itself, authorize a worker commit, resume
WP-ARCH-003, open DARA-T3, change MFRP, invoke a provider, publish, deploy, or
claim runtime/production readiness.
