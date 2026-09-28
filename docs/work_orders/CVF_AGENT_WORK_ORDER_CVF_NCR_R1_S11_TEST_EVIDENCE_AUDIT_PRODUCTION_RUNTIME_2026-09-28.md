# CVF Agent Work Order - NCR-R1/S11 Test Evidence Audit Production Runtime

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Batch ID: CVF-NCR-R1-S11

Dispatch base head: `e5a97a6d2`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: one shared-workspace `INTERNAL_AGENT` worker.

Reviewer/closer: Local orchestrator/reviewer.

Worker return path: `docs/reviews/CVF_CVF_NCR_R1_S11_TEST_EVIDENCE_AUDIT_PRODUCTION_RUNTIME_WORKER_RETURN_2026-09-28.md`

## Dispatch Prompt Envelope

Role: INTERNAL_AGENT P10 production-runtime worker.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_R1_S11_TEST_EVIDENCE_AUDIT_PRODUCTION_RUNTIME_2026-09-28.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture the exact clean committed dispatch/continuity HEAD before edits.

Current-time notes: packet date is 2026-09-28; the one-call grant expires at 2026-09-29T23:59:59+07:00.

Do-not-misread notes: this packet enables exactly one package-specific external CLI/MCP production envelope and one provider call. It does not authorize a retry, audited-test execution, downstream mutation from the advisory output, executor/checker changes, another package, public sync, deployment, or platform-wide production readiness.

Required first actions: read startup and guard surfaces, paired baseline, this packet, P10 owners and every checker named below; capture clean HEAD/status; run the exact pre-implementation gate before package-body read or source mutation.

Return contract: leave exactly the twelve worker-owned paths uncommitted with empty staging; return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` to Local.

productionExecutionAuthority: ORCHESTRATOR_GRANT_REQUIRED
productionExecutionGrantOwner: LOCAL_ORCHESTRATOR
productionExecutionGrantSubject: CVF-NCR-R1-S11-P10-INTERNAL-WORKER
productionExecutionGrantDelegationId: CVF-NCR-R1-S11-P10-ONE-CALL-20260928
productionExecutionGrantMaxCalls: 1
productionExecutionGrantExpiresAt: 2026-09-29T23:59:59+07:00
productionExecutionGrantProviderAllowlist: alibaba-dashscope
productionExecutionGrantModelAllowlist: qwen3.7-flash-2026-07-15

providerExecutionAuthority: ORCHESTRATOR_GRANT_REQUIRED
providerExecutionGrantOwner: ORCHESTRATOR
providerExecutionGrantSubject: CVF-NCR-R1-S11-P10-INTERNAL-WORKER
providerExecutionGrantDelegationId: CVF-NCR-R1-S11-P10-ONE-CALL-20260928
providerExecutionGrantMaxCalls: 1
providerExecutionGrantExpiresAt: 2026-09-29T23:59:59+07:00
providerExecutionGrantProviderAllowlist: alibaba-dashscope
providerExecutionGrantModelAllowlist: qwen3.7-flash-2026-07-15

## Purpose

Complete P10 for `cvf-engineering-test-evidence-audit`: bind the existing
generic production executor and CLI/MCP envelope to this one ACTIVE package,
regenerate exact projections, prove provider-free dry admission, make at most
one live provider call, save the production receipt, and return for Local
review without committing.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind package-skill --batch-id CVF-NCR-R1-S11 --title "Test Evidence Audit P10 Production Runtime" --date 2026-09-28 --base e5a97a6d2 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | package-skill plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact P10 source/projection manifest, target-state contract, one-call grant, proof commands and closure ownership |
| checkerReadAheadConfirmation | dispatch, target-state, pipeline, closeability, handoff, trace and review-cost sources read before authoring |
| docOnlyNewFields | production grant fields in the dispatch envelope |
| claimBoundary | packet authority only; execution claims require returned receipt and Local acceptance |

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: CVF-NCR-R1-S11
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
preExecutionReviewAdmission: REQUIRED_TRIGGERED
preExecutionReviewTrigger: OPERATOR_EXPLICIT_REQUEST
nextRoutineReviewBoundary: PRE_EXECUTION_REVIEW
reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

## Semantic Convergence Outcome

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "CVF-NCR-TEST-EVIDENCE-AUDIT-P10",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {"prior": [], "resolved": [], "retained": [], "new": [], "reopened": [], "current": []},
  "resolutionEvidence": {},
  "counters": {"partialReadyClosures": 0, "reviewerScopeExpansions": 0, "sameClaimCorrections": 0, "nonDecreasingBlockerTransitions": 0},
  "claims": [{"claimId": "P10-PRODUCTION-RUNTIME", "claimClass": "OTHER", "proofClass": "NAMED_OBSERVABLE_PROOF", "evidenceRef": "docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_R1_S11_TEST_EVIDENCE_AUDIT_PRODUCTION_RUNTIME_2026-09-28.md"}],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| P9 closure | `docs/reviews/CVF_CVF_NCR_R1_S10_R1_OFFLINE_CLOSURE_PREREQUISITE_ROOT_REPAIR_COMPLETION_2026-09-28.md`; final correction `b2b08a607` | preserve accepted P9 receipt bytes and do not repeat P9 | ACCEPT |
| P10 runtime owners | production runtime standard, executor and CLI/MCP adapter listed in Source Verification | reuse existing generic code; no checker/executor edit | ACCEPT |
| exact live effect | operator delegation on 2026-09-28 | one allowed provider/model call, no retry | ACCEPT |

## Authority Chain

NCR roadmap P10 -> operator Local delegation -> paired GC-018 and this work
order -> one INTERNAL_AGENT worker -> Local independent review and commit.
Loading or executing the advisory package grants no downstream file, test, Git,
browser, public, deployment, or business-action authority.

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"CVF-NCR-R1-S11","requestedProfile":"P4_CRITICAL","classification":{"taskKind":"LIVE_PROOF","authorityImpact":"USES_EXISTING_OWNER","externalEffect":"NETWORK_WRITE","dataSensitivity":"CREDENTIAL_REFERENCE","reversibility":"PARTIALLY_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"KNOWN_PATTERN"},"pathFamilies":["docs/baselines/","docs/work_orders/","docs/reference/agent_system_skills/packages/cvf-engineering-test-evidence-audit/","docs/reference/agent_system_skills/registry/entries/","docs/reference/agent_system_skills/generated/","docs/reference/agent_system_skills/truth/","docs/reference/agent_system_skills/control_plane/generated/","EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/public/data/","docs/reviews/evidence/","docs/reviews/"],"claims":["one ACTIVE package may be admitted to the existing production executor and CLI/MCP envelope","one valid production receipt may support P10 Local review"],"requiredProof":["pre-implementation admission","source and projection agreement","external pre-mutation denial","dry production readiness","one live production envelope","receipt hash recomputation","exact twelve-path reconciliation"],"operatorCheckpoints":["one Alibaba/DashScope call using qwen3.7-flash-2026-07-15","no retry","no downstream action from advisory output"],"forbiddenEffects":["second provider call","audited-test execution","worker stage stash commit or push","executor checker generator mutation","other package mutation","public sync deployment or platform production claim"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"docs/reviews/CVF_CVF_NCR_R1_S10_R1_OFFLINE_CLOSURE_PREREQUISITE_ROOT_REPAIR_COMPLETION_2026-09-28.md","completenessClaimChanged":false}}
```

| Role | Phase | Decision owner | Boundary |
|---|---|---|---|
| Local dispatcher/reviewer | author, release, review and closure | LOCAL | technical disposition, provider grant and material commit |
| shared-workspace worker | exact implementation and proof | Local packet | twelve paths, one call, no commit |
| operator | program authority | OPERATOR | delegated Local handling and later receives outcome |
| external research agent | none | N/A | no external research lane |

## External/Local Coordination Binding

The relayed worker is `INTERNAL_AGENT` regardless of provider/model. Local owns
private-CVF verification and final technical disposition.

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | N/A with reason: external research ended before this internal dispatch |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | Local reviewer/closer and existing ASSF production runtime owners |
| Disposition | NOT_APPLICABLE_WITH_REASON: no external knowledge promotion |
| Claim boundary | provider output is runtime proof evidence, not CVF source authority |

## Scope And Maximum Worker Path Manifest

Maximum worker path count: 12.

1. `docs/reference/agent_system_skills/packages/cvf-engineering-test-evidence-audit/README.md`
2. `docs/reference/agent_system_skills/packages/cvf-engineering-test-evidence-audit/SKILL.md`
3. `docs/reference/agent_system_skills/packages/cvf-engineering-test-evidence-audit/skill.source.json`
4. `docs/reference/agent_system_skills/registry/entries/cvf-engineering-test-evidence-audit.json`
5. `docs/reference/agent_system_skills/generated/skill-index.json`
6. `docs/reference/agent_system_skills/truth/packets/cvf-engineering-test-evidence-audit.json`
7. `docs/reference/agent_system_skills/truth/generated/skill-truth-index.json`
8. `docs/reference/agent_system_skills/control_plane/generated/skill-inventory.json`
9. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/public/data/skills-index.json`
10. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/public/data/assf-skill-control-plane.json`
11. `docs/reviews/evidence/cvf-ncr-r1-s11-test-evidence-audit-production-runtime.json`
12. `docs/reviews/CVF_CVF_NCR_R1_S11_TEST_EVIDENCE_AUDIT_PRODUCTION_RUNTIME_WORKER_RETURN_2026-09-28.md`

Paths 5 and 7-10 are generator-owned projections and must never be hand-edited.
No baseline, work order, completion review, roadmap, continuity, handoff,
executor, checker, generator or test source is worker-owned.

## Work-Order Fulfillment Manifest

| Output | Required state at handoff |
|---|---|
| package trio and registry | ACTIVE/PASSED/CERTIFIED/internal IMPLEMENTED/external IMPLEMENTED; production adapter contract/evidence concrete |
| truth packet | approved STRICT truth with matching lifecycle snapshot and canonical recomputed receipt chain |
| five generated projections | regenerated and drift-free |
| production receipt | adapter-created P10 JSON from the one live attempt; never synthesized |
| worker return | checker-safe `COMPLETE_PENDING_REVIEW` or truthful `BLOCKED_WITH_REASON` |

## Required Artifact Manifest

| Path | Required at worker handoff | Rule |
|---|---|---|
| `docs/reference/agent_system_skills/packages/cvf-engineering-test-evidence-audit/README.md` | YES | production/external boundary synchronized |
| `docs/reference/agent_system_skills/packages/cvf-engineering-test-evidence-audit/SKILL.md` | YES | production/external boundary synchronized; advisory-only behavior preserved |
| `docs/reference/agent_system_skills/packages/cvf-engineering-test-evidence-audit/skill.source.json` | YES | external disposition and claim boundary synchronized |
| `docs/reference/agent_system_skills/registry/entries/cvf-engineering-test-evidence-audit.json` | YES | external IMPLEMENTED with concrete adapter contract/evidence |
| `docs/reference/agent_system_skills/generated/skill-index.json` | YES | generator-owned projection |
| `docs/reference/agent_system_skills/truth/packets/cvf-engineering-test-evidence-audit.json` | YES | approved STRICT truth updated and rehashed |
| `docs/reference/agent_system_skills/truth/generated/skill-truth-index.json` | YES | canonical truth projection |
| `docs/reference/agent_system_skills/control_plane/generated/skill-inventory.json` | YES | generator-owned inventory |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/public/data/skills-index.json` | YES | Web generator-owned projection |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/public/data/assf-skill-control-plane.json` | YES | Web generator-owned projection |
| `docs/reviews/evidence/cvf-ncr-r1-s11-test-evidence-audit-production-runtime.json` | YES after attempted live call | adapter-created receipt; never synthesize |
| `docs/reviews/CVF_CVF_NCR_R1_S11_TEST_EVIDENCE_AUDIT_PRODUCTION_RUNTIME_WORKER_RETURN_2026-09-28.md` | YES | terminal no-commit return |

## Required Root Contract

1. Verify this committed packet and continuity release, clean worktree, unexpired grant and exact model.
2. Run pre-implementation before any body read or mutation.
3. Prove current external CLI/MCP access is denied before mutation.
4. Change only the target package's external-adapter declarations and truthful P10 boundary prose. Preserve ACTIVE/PASSED/CERTIFIED/internal IMPLEMENTED and approved STRICT truth.
5. Set `externalCliMcpDisposition` to `IMPLEMENTED`; bind `adapterContract` to `docs/reference/agent_system_skills/CVF_ASSF_PRODUCTION_PACKAGE_RUNTIME_STANDARD.md`; bind `adapterEvidence` to the P10 completion path `docs/reviews/CVF_CVF_NCR_R1_S11_TEST_EVIDENCE_AUDIT_PRODUCTION_RUNTIME_COMPLETION_2026-09-28.md`, which Local owns and must create before acceptance.
6. Update the truth snapshot/evidence/obligations without weakening no-automatic-invocation or no-downstream-action boundaries; recompute its canonical hash chain.
7. Regenerate skill index, truth index, control-plane inventory and both Web read models in canonical order.
8. Run focused existing tests and all source/projection checks.
9. Run CLI/MCP dry proof once; require `DRY_RUN_PRODUCTION_PACKAGE_EXECUTION_READY` and zero provider calls.
10. Run the exact CLI/MCP live command once. Require HTTP 200, non-empty output, `PRODUCTION_PACKAGE_EXECUTION_PASS`, execution receipt and complete `sourceTruthTrace`.
11. Recompute the saved execution/use/output hashes offline. Do not invoke any adapter/provider a second time.
12. If the live attempt fails, is partial, times out, or is ambiguous, preserve secret-safe evidence, record `providerCallCount: 1`, and return `BLOCKED_WITH_REASON`; no retry.
13. Do not execute the audited test or treat the advisory output as action authority.
14. Return exactly twelve pending paths with empty staging; no stage, stash, commit, push, install or unrelated cleanup.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| P10 target is ACTIVE_PRODUCTION_RUNTIME | lifecycle | `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md` | End-To-End Phase Ladder P10 | `ACTIVE_PRODUCTION_RUNTIME` | productionization SOP | ACCEPT |
| Production executor requires ACTIVE source and emits execution receipt after live use proof | runtime | `governance/compat/run_assf_production_package_executor.py` | `_active_source_reasons`; `_execution_receipt`; `build_production_package_execution_packet` | `CVF_ASSF_PRODUCTION_PACKAGE_EXECUTION_RECEIPT` | production executor | ACCEPT |
| External wrapper delegates with consumer EXTERNAL_AGENT_CLI_MCP | runtime | `governance/compat/run_assf_production_cli_mcp_adapter.py` | `build_cli_mcp_execution_envelope` | `CONSUMER_EXTERNAL` | CLI/MCP adapter | ACCEPT |
| Target package is currently external-deferred and therefore denied | source state | `docs/reference/agent_system_skills/registry/entries/cvf-engineering-test-evidence-audit.json` | adapter fields | `externalCliMcpDisposition` | registry entry | ACCEPT |
| P10 feasibility requires ACTIVE source and full generated dependencies | admission | `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_TARGET_STATE_FEASIBILITY_STANDARD.md` | Phase And Decision Matrix; Dependency Inference | P10; mutation families | feasibility standard | ACCEPT |
| P9 proof is accepted and immutable | prerequisite | `docs/reviews/CVF_CVF_NCR_R1_S10_R1_OFFLINE_CLOSURE_PREREQUISITE_ROOT_REPAIR_COMPLETION_2026-09-28.md` | Decision; Evidence | receipt ID and file SHA-256 | Local completion review | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| planned four new artifact paths | all `Test-Path` results false before authoring | NO_COLLISION |
| exact token search | no prior S11/production-runtime packet found under `docs` or `CVF_SESSION` | NO_COLLISION |
| collision decision | fresh bounded P10 phase | CREATE_NEW |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | one-package P10 external CLI/MCP production runtime proof |
| scope classification | private source/projection mutation plus one bounded provider call |
| risk sensitivity | credential-referenced, quota-consuming, non-repeatable live effect |
| selected role route | one shared-workspace INTERNAL_AGENT, then Local independent review |
| escalation condition | preflight failure, source contradiction, receipt mismatch, second-call need or thirteenth path |
| canonical route mode | SINGLE_AGENT_SINGLE_ROLE |
| decision owner | Local |

## Required First Reads And Pre-Flight

Read `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`,
`CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF_V63_2026-09-18.md`, guard orientation,
literal gotchas, paired baseline, this work order, productionization SOP,
target-state feasibility standard, production runtime standard, current target
package/source/registry/truth surfaces, executor, CLI/MCP adapter and every
checker named below. Capture clean HEAD/status. Run pre-implementation before
body read or edits.

## Agent Roles

- Dispatcher: Local authors/releases the exact packet.
- Worker: executes exact twelve-path scope and returns without commit.
- Reviewer/closer: Local validates source, projections and receipts; may repair within the same exact dependency class; owns completion review and commit.
- Session-sync steward: Local updates continuity only after material disposition.

## Write Ownership

Write mode: modify-listed/create-listed only for the exact twelve paths.
Everything else is forbidden. `WORKER_MUST_NOT_COMMIT`; no stage, stash,
commit, push or public sync.

## Execution Plan

1. Confirm release, required reads, clean base and pre-implementation PASS.
2. Capture pre-mutation external denial and exact source snapshots.
3. Apply bounded package/registry/truth production-adapter declarations.
4. Run canonical generators and drift checks.
5. Run focused tests and dry production envelope.
6. Run the single live production envelope and save its JSON.
7. Validate hashes offline; scaffold and complete the worker return.
8. Run worker-return fast gate, exact-path/staging checks and return to Local.

## Evidence Requirements

- pre-mutation external denial;
- exact source field diff and truth receipt-chain recomputation;
- drift-free five projections;
- focused production executor and package-governance tests;
- dry disposition with zero provider calls;
- one live result with provider/model/HTTP status, receipt IDs and trace;
- offline receipt/hash recomputation without a second call;
- `providerCallCount: 1` after any attempted live call;
- exact twelve-path dirty set and empty cached diff.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_R1_S11_TEST_EVIDENCE_AUDIT_PRODUCTION_RUNTIME_2026-09-28.md
python governance/compat/run_assf_cli_mcp_adapter_projection.py --skill-id cvf-engineering-test-evidence-audit --json
python governance/compat/generate_assf_skill_index.py
python governance/compat/check_skill_truth_packets.py --enforce
python governance/compat/generate_skill_control_plane_inventory.py
Push-Location EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npm run build:skill-index
Pop-Location
python governance/compat/check_assf_package_candidate_anatomy.py --enforce
python governance/compat/check_assf_certified_metadata_admission.py --enforce
python governance/compat/check_package_skill_productionization_pipeline.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_skill_control_plane_inventory.py --enforce
python governance/compat/check_cvf_web_skill_control_plane_projection.py --enforce
python -m pytest governance/compat/test_run_assf_production_package_executor.py governance/compat/test_run_assf_package_use_proof_adapter.py -q
python governance/compat/run_assf_production_cli_mcp_adapter.py --skill-id cvf-engineering-test-evidence-audit --request-id cvf-ncr-r1-s11-p10-dry --provider alibaba-dashscope --model qwen3.7-flash-2026-07-15 --task-prompt "Given an asserted source-to-test coverage claim, return one advisory KEEP, REPAIR, CONSOLIDATE, ADD, or DEFER_WITH_REASON label with target, evidence, and reason; do not run or modify tests." --json
python governance/compat/run_assf_production_cli_mcp_adapter.py --skill-id cvf-engineering-test-evidence-audit --request-id cvf-ncr-r1-s11-p10-live --provider alibaba-dashscope --model qwen3.7-flash-2026-07-15 --live --task-prompt "Given an asserted source-to-test coverage claim, return one advisory KEEP, REPAIR, CONSOLIDATE, ADD, or DEFER_WITH_REASON label with target, evidence, and reason; do not run or modify tests." --json --receipt-out docs/reviews/evidence/cvf-ncr-r1-s11-test-evidence-audit-production-runtime.json
python governance/compat/check_cvf_skill_usage_receipt_trace.py --enforce
python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_CVF_NCR_R1_S11_TEST_EVIDENCE_AUDIT_PRODUCTION_RUNTIME_WORKER_RETURN_2026-09-28.md --title "CVF NCR R1 S11 Test Evidence Audit Production Runtime Worker Return"
python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_R1_S11_TEST_EVIDENCE_AUDIT_PRODUCTION_RUNTIME_2026-09-28.md --pytest-target governance/compat/test_run_assf_production_package_executor.py --pytest-target governance/compat/test_run_assf_package_use_proof_adapter.py
git diff --check
git diff --name-status
git diff --cached --name-status
git status --short --untracked-files=all
```

The worker may use one read-only one-shot local command to recompute JSON
receipt IDs and output hashes. It must record the exact command and must not
write another artifact.

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0

closeabilityDisposition: CLOSEABLE

implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT

foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET

returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired packet | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired packet | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V63_2026-09-18.md` material-SHA marker | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker return disclosure | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | exact twelve paths | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | existing tests and source/projection checks | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | worker return | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted twelve-path set | EXACT_PATHS | closer | MATERIAL_COMMIT | worker_return_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | completion review | EXACT_PATHS | closer | MATERIAL_COMMIT | reviewer_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material set | EXACT_PATHS | closer | MATERIAL_COMMIT | terminal_completion_review |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | active continuity | EXACT_PATHS | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | material and continuity ranges | EXACT_PATHS | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | INTERNAL_AGENT worker -> Local reviewer/closer |
| phase | P10_PRODUCTION_RUNTIME_EXECUTION |
| baseHeadFor(phase) | dispatchBaseHead=`e5a97a6d2`; executionBaseHead is worker capture; closureBaseHead is Local-set |
| changedSetScope(phase) | exact twelve-path worker manifest |
| traceScope(phase, actor) | source/projection diffs, dry/live receipt and Git scope evidence |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; Local owns commit |
| crossBatchIsolation | no unrelated dirty paths or other package changes |
| nextMoveSurfaces | worker return to Local only |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: one INTERNAL_AGENT worker after committed release and continuity

laneOwnedPaths: exactly the twelve worker paths listed above

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: terminal worker return, exact manifest reconciliation and empty staging

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`package_skill_productionization`, role=`dispatcher`, lifecyclePhase=`dispatch`.

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class package_skill_productionization --role dispatcher --lifecycle-phase dispatch --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | no registered defect changes this exact P10 boundary |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_release_readiness.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_package_skill_target_state_feasibility.py`; `governance/compat/check_package_skill_productionization_pipeline.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_skill_truth_packets.py`; `governance/compat/check_assf_certified_metadata_admission.py`; `governance/compat/check_skill_control_plane_inventory.py`; `governance/compat/check_cvf_web_skill_control_plane_projection.py` |
| literalTokensReviewed | dispatch prompt fields; P10 target matrix; external adapter contract/evidence; Local blocker route; inferred projection paths; closeability IDs; no-commit reviewer conversion; trace labels |
| gateRunPurpose | confirmation after source-first packet authoring |
| claimBoundary | structural and semantic admission only; not production proof |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_CVF_NCR_R1_S11_TEST_EVIDENCE_AUDIT_PRODUCTION_RUNTIME_WORKER_RETURN_2026-09-28.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_R1_S11_TEST_EVIDENCE_AUDIT_PRODUCTION_RUNTIME_2026-09-28.md --pytest-target governance/compat/test_run_assf_production_package_executor.py --pytest-target governance/compat/test_run_assf_package_use_proof_adapter.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Purpose; Scope / Methodology; Findings / Position; Risk /
Corrective Action; Decision; Claim Boundary; Agent Operation Trace Block;
Delta Execution Claim Boundary Control Block; CVF Skill Usage Receipt Trace;
Public Export Disposition; executionBaseHead; git status --short; External
Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus Completeness
And Report Integrity; Finding-To-Governance Learning Disposition; Epistemic
Process Block; Machine Closure Package. Use N/A with reason when applicable.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_CVF_NCR_R1_S11_TEST_EVIDENCE_AUDIT_PRODUCTION_RUNTIME_COMPLETION_2026-09-28.md` |
| reviewerOwnedClosurePaths | completion review, accepted worker set, roadmap/continuity only under separate Local closure authority |
| closureOwner | Local orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

## Worker Autonomy / No-Question Rule

Repair allowed-scope failures directly. A technical contradiction returns
`BLOCKED_WITH_REASON` to Local and never becomes an operator question. The live
call grant is already resolved; a need for another call is a blocker, not a
request to the operator.

## Package Skill Productionization Control Block

SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`

Current phase: P9 `USE_PROOF_PASSED`; source status `ACTIVE`; external adapter deferred.

Target lifecycle state: P10 `ACTIVE_PRODUCTION_RUNTIME` for this package only.

Prior phase evidence: accepted S10/S10-R1 P9 completion and immutable receipt.

Next forbidden skip: P11 scale-up or any other package activation by analogy.

Runtime/provider proof: one dry production envelope plus at most one live call.

Claim boundary: P10 receipt proves only this package and this governed invocation.

## Package Skill Target-State Feasibility Contract

```json
{
  "schemaVersion": "cvf.packageSkillTargetStateFeasibility.v1",
  "skillId": "cvf-engineering-test-evidence-audit",
  "sopPhase": "P10",
  "targetState": {
    "status": "ACTIVE",
    "candidateState": "ACTIVE",
    "uatState": "PASSED",
    "certificationState": "CERTIFIED",
    "internalAgentDisposition": "IMPLEMENTED",
    "externalCliMcpDisposition": "IMPLEMENTED",
    "truthApprovalStatus": "APPROVED",
    "truthAssuranceLevel": "STRICT",
    "adapterContract": "docs/reference/agent_system_skills/CVF_ASSF_PRODUCTION_PACKAGE_RUNTIME_STANDARD.md",
    "adapterEvidence": "docs/reviews/CVF_CVF_NCR_R1_S11_TEST_EVIDENCE_AUDIT_PRODUCTION_RUNTIME_COMPLETION_2026-09-28.md"
  },
  "externalUseClaimed": true,
  "expectedDecisions": {
    "internalActivation": "ACTIVATION_READY",
    "externalBodyRead": "DENIED_EXTERNAL_BODY_READ_NOT_IMPLEMENTED",
    "externalOutputUse": "DENIED_EXTERNAL_OUTPUT_USE_NOT_IMPLEMENTED"
  },
  "checkerSources": [
    "governance/compat/check_assf_certified_metadata_admission.py",
    "governance/compat/check_package_skill_productionization_pipeline.py",
    "governance/compat/generate_skill_control_plane_inventory.py",
    "governance/compat/run_assf_active_resolver.py",
    "governance/compat/run_assf_cli_mcp_adapter_projection.py"
  ],
  "mutations": ["REGISTRY_ENTRY", "PACKAGE_SOURCE", "TRUTH_PACKET", "USE_PROOF_RECEIPT"],
  "blockerRouting": {
    "technicalDecisionOwner": "LOCAL",
    "workerTerminalReturn": "BLOCKED_WITH_REASON",
    "operatorQuestionAllowed": false
  }
}
```

The feasibility contract intentionally records pre-mutation external denial.
The worker must prove post-mutation external production admission through the
actual CLI/MCP dry/live envelopes; the declaration itself is not that proof.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | production executor | may request receipt-backed package use only under this work order | P10 production receipt and sourceTruthTrace | no downstream action authority | IMPLEMENTED_PENDING_REVIEW |
| `EXTERNAL_AGENT_CLI_MCP` | bounded production CLI/MCP wrapper | one request envelope under exact provider grant | saved P10 envelope | no daemon/server/public API/provider router | IMPLEMENTED_PENDING_REVIEW |
| `EXTERNAL_AGENT_CLI_MCP` | other packages or future scale | no authority by analogy | fresh P0-P10 packet required | P11 remains closed | DEFERRED_WITH_REASON |

## Independent Review Probe Admission Contract

independentProbeRequired: YES

independentProbeRiskClass: P10_LIVE_PRODUCTION_ENVELOPE_AND_RECEIPT_INTEGRITY

independentProbeDispositionAtDispatch: PENDING_REVIEWER_EXECUTION

probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER

implementationOracleSeparation: worker makes the one call and creates the receipt; Local recomputes execution/use/output hashes and sourceTruthTrace offline without another call

positiveControl: external pre-mutation denial, post-mutation dry readiness, HTTP 200 live PASS, exact skill/provider/model and complete receipt chain

negativeMutationClasses: wrong package, stale truth, deferred external disposition, receipt tamper, output hash mismatch, lifecycle downgrade, second call, audited-test action or thirteenth path

expectedInformationGain: distinguish real package-specific production admission from P9 use proof or metadata-only activation readiness

rerunCostReason: one bounded live effect is required by P10; all independent review is provider-free

reviewerDecisionOwner: LOCAL

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | YES_PENDING_EXECUTION |
| runtimeMutationAuthorized | YES_EXACT_PACKAGE_METADATA_AND_PROJECTIONS |
| freshnessVerificationMode | FRESH_ONE_CALL_REQUIRED |
| reason | P9 receipt cannot be converted by the current executor into a P10 production execution receipt |
| requiredFutureAction | worker performs at most one exact call; Local reviews without rerun |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation surface | existing ASSF package/source/registry/truth roots and `docs/reviews/evidence/` |
| Storage decision | update existing sources and deterministic projections; create one receipt in the existing evidence family |
| Stable filename disposition | fixed S11 receipt and worker-return paths named in the manifest |
| Generated aggregate discipline | skill index, truth index, inventory and Web projections are generator-owned |
| Authority boundary | receipt is evidence; registry/truth/work order remain authority surfaces |
| Forbidden expansion | no new root, database, queue, watcher, daemon, executor or adapter implementation |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatch author |
| Provider or surface | private CVF workspace |
| Session or invocation | NCR-R1/S11 P10 packet authoring, 2026-09-28 |
| Working directory | repository root |
| Command or tool surface | governed reads, source probes, scaffold stdout, apply_patch and Git |
| Target paths | paired S11 baseline and work order |
| Allowed scope source | operator delegation on 2026-09-28 and canonical P10 frontier |
| Before status evidence | clean worktree at `e5a97a6d2` |
| After status evidence | paired dispatch packet pending validation/commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | packet authoring and exact one-call worker release only |
| Claim boundary | no package mutation or provider call during authoring |
| Agent type | INTERNAL_AGENT Local orchestrator/reviewer |
| Invocation ID | `cvf-ncr-r1-s11-p10-author-20260928` |
| Expected manifest | paired baseline and work order |
| Actual changed set | paired baseline and work order only at authoring |
| Manifest delta | MATCH |
| Deletion or rename disposition | none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | one package-specific P10 production executor/CLI-MCP envelope proof |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE_PENDING_WORKER_RETURN |
| receiptEvidence | CVF_RECEIPT_PRESENT_PENDING_WORKER: P9 is prerequisite only; P10 receipt must be freshly emitted by the production adapter |
| actionEvidence | ACTION_EVIDENCE_PRESENT_PENDING_WORKER: exactly one provider completion may occur; advisory output cannot trigger another action |
| invocationBoundary | existing CVF production executor and bounded CLI/MCP wrapper under this work order |
| interceptionBoundary | no daemon, server, IDE, shell, filesystem, Git or universal agent interception claim |
| claimLanguage | accepted P10 may prove one receipt-backed production envelope for this package only |
| forbiddenExpansion | no retry, audited-test execution, downstream mutation, other package, P11, public sync, deployment or platform production claim |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: current external request is denied before the
metadata change; after exact production binding, dry readiness and one live
receipt should pass without granting downstream action authority.

Evidence Comparison Requirement: worker return compares source/projection,
dry and live observations against this prediction.

Contradiction Handling Requirement: any contradiction or ambiguous live result
is preserved and returned `BLOCKED_WITH_REASON`; no retry or claim widening.

Claim Update Requirement: worker records confirmed, narrowed or invalidated
P10 claim; Local alone accepts and closes.

## Acceptance Criteria

- [ ] Exact twelve-path manifest only; staging empty and HEAD unchanged by worker.
- [ ] Package/source/registry/truth agree on ACTIVE, approved STRICT truth and external IMPLEMENTED production adapter posture.
- [ ] Five deterministic projections are regenerated and drift-free.
- [ ] Existing focused tests and package governance checks pass.
- [ ] Dry CLI/MCP envelope is ready with zero provider calls.
- [ ] At most one live call produces a valid production execution receipt and complete sourceTruthTrace, or the return is truthfully blocked with the grant consumed.
- [ ] No audited test or downstream mutation is executed from the advisory output.

Fail conditions: second call or retry; thirteenth path; source/truth mismatch;
hand-edited projection; missing receipt after claimed success; raw secret output;
worker commit/stage/stash; generic runtime code mutation; public/deploy claim.

## Review Gate

Implementation begins only after committed packet/continuity binding and exact
pre-implementation PASS. Closure requires Local receipt/hash verification,
worker-return fast PASS, reviewer-fast PASS, material pre-commit PASS and a
reviewer-owned completion artifact. Worker handoff is not closure.

## Closure Checklist

- [ ] Source, projections, receipt and changed set accepted by Local.
- [ ] No provider rerun during review.
- [ ] Completion review binds the adapterEvidence path.
- [ ] Material and continuity commits remain separate.
- [ ] P11 and broader production/public/deploy effects remain closed.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for any preflight failure, source contradiction,
needed checker/executor edit, missing completion-evidence route, provider
failure/timeout/ambiguity, second-call need, secret-risk evidence, thirteenth
path, or inability to keep staging empty. Do not ask the operator a technical
question and do not widen scope.

## Operator Checkpoint

SATISFIED_FOR_EXACT_ONE_CALL: operator delegated Local handling on 2026-09-28;
Local binds that authority to one Alibaba/DashScope call using
`qwen3.7-flash-2026-07-15`, expiring 2026-09-29T23:59:59+07:00. No retry,
provider/model substitution, additional expense, public effect or deployment
is authorized.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private runtime package and provider receipt evidence; no public sync.

## Claim Boundary

This work order authorizes exact P10 implementation/proof for one package and
one provider call. It does not authorize the worker to commit, retry, run the
audited test, act on the advisory label, change generic runtime code, touch a
thirteenth path, scale to another package, publish, deploy or claim CVF
production readiness.
