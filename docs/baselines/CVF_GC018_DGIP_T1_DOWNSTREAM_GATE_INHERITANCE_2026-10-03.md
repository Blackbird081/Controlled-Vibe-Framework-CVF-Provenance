# GC-018 - Portable Downstream Gate Inheritance

Memory class: POINTER_RECORD
docType: baseline
Status: ACCEPTED_BASELINE
Date: 2026-10-03
Batch ID: CVF-DGIP-T1
providerExecutionAuthority: FORBIDDEN

## Purpose

Implement a versioned portable downstream control-plane gate profile and its bootstrap/invocation/claim chain. Extend existing Golden Bootstrap and GLP learning with the CCMAI use case; do not reopen their closures. Cover continuity, fail-closed packet applicability, conditional reviewer-local repair routing and project-to-parent finding intake in one integrated root contract.

## Authority Chain

| Authority | Evidence | Disposition |
|---|---|---|
| Operator current request | `docs/reviews/evidence/cvf-dgip-t1-dispatch-inputs-2026-10-03.json` | ACCEPT parent work-order implementation and manual relay after PASS |
| Existing learning | Golden Bootstrap intake and GLP roadmap | ACCEPT dedup/owner mapping; no reopened closure |
| Parent repair routing | `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md` | ACCEPT conditional routing |
| CCMAI intake | `docs/reviews/evidence/ccmai-to-cvf-downstream-gate-learning-intake-2026-10-01.txt` | INPUT_ONLY, no downstream/project mutation authority |
| GC-018 | `docs/baselines/CVF_GC018_DGIP_T1_DOWNSTREAM_GATE_INHERITANCE_2026-10-03.md` | ACCEPT exact scope after bound release |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Doctor continuity presence/parse gap | CURRENT_LOCAL_SOURCE | `scripts/check_cvf_workspace_agent_enforcement.ps1` | Check 19/20/22 | stateFields; rehydrationTokens | downstream doctor | ACCEPT |
| Core schema differs from project | CURRENT_LOCAL_SOURCE | `scripts/lib/downstream_catalog/CvfDownstreamBootstrapContent.ps1` | Get-CvfActiveStateObject / Get-CvfImplementationStatusObject | activePhase/currentPhase | generated project 1.0 | ACCEPT |
| Active status can skip contract | CURRENT_LOCAL_SOURCE | `governance/compat/check_gate_to_role_closeability.py` | check_work_order | anchored status and early return | Core closeability | ACCEPT |
| Parent conditional repair route | GOVERNED_STANDARD | `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md` | Reviewer-Local Repair Versus Worker Return Routing | reviewerLocalRepairBoundary/Basis | review-cost owner | ACCEPT |
| Downstream template projection gap | CURRENT_LOCAL_SOURCE | `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md` | Provider-Neutral Role Contract | reviewer independence/repair roles | downstream instructions | ACCEPT |
| Golden learning reuse | GOVERNED_RETAINED_INTAKE | `docs/reference/CVF_GOLDEN_DOWNSTREAM_BOOTSTRAP_LEARNING_INTAKE_2026-07-23.md` | Observed learning / Success boundary | executable drift/golden proof | BSL learning | ACCEPT |
| Historical CCMAI commits/PR runs | ADVISORY_UNVERIFIED | `docs/reviews/evidence/ccmai-to-cvf-downstream-gate-learning-intake-2026-10-01.txt` | Observed use case | R019/R020/PR1 | external intake, not Core proof | REJECT |

## Scope / Target / Owner Boundary

Worker changes only the existing exact paths and two new bounded families listed below, plus exact test/return paths. Private provenance implementation and hermetic disposable tests only. No real downstream project, public clone, workspace-root inventory/promotion, customer data, secrets/provider memory, provider/live call, network/fetch/install, host security/control mutation, public sync/push/deploy or worker commit. S05 roots/packets/C1 STOP remain frozen and unrelated. No subagents.

## Implementation Contract

1. Define profile `cvf.downstreamGateProfile@1.0.0` in `docs/reference/downstream_gate_profile/` with a canonical standard, README front door, schema/phase applicability map, fail-closed outcomes and upgrade/migration contract. Reconcile BSL/GLP and existing ADIF-0026/0050/0052/0058; record EXTENDS_EXISTING or independent reason before proposing any new defect ID. Do not create a duplicate automatic-learning framework or assign an ID without the existing registry route.
2. Implement portable stdlib Python control modules/runner and PowerShell integration in `scripts/lib/downstream_governance/`. Generated project schema differs from core: do not hardcode Core state paths/marker grammar. Version/pin the downstream state/handoff/memory/implementation contract; compare phase/mode and active handoff/tranche relations, define REVIEW_PENDING mapping explicitly, reject missing/duplicate/conflicting/unknown fields. Emit field-specific mismatch locators, not generic doctor PASS. Initial bootstrapped memory must contain machine-comparable truth; migration of existing surfaces is explicit, no silent overwrite or heuristic alignment.
3. Strictly parse applicability in closeability: active inline status cannot silently skip; accept only explicitly specified prospective grammar, reject malformed/unknown/contradictory status on a candidate work order. Explicit HOLD/DRAFT/non-applicable returns reason plus checked control IDs, never PASS for an unchecked contract. Preserve historical unchanged artifacts and Core active-packet semantics; tests for blank, duplicate, inline/issue suffix, unknown and historical/non-work-order inputs.
4. Install the pinned runner/profile/CI invocation template via bootstrap. Bind mandatory controls to doctor/new-project enforcement, pre-dispatch, worker-return/reviewer-fast, pre-commit preflight and generated PR CI. Keep a single framework-owned control source; inherited copies require version/content identity and invocation receipts. Test that the trusted doctor/runner rejects a missing/empty/tampered mandatory runner/profile and no-op local override. File existence or a YAML token is not executed CI evidence. State the trust boundary: fully replacing the trusted gate or invoking out of band is not intercepted.
5. Project reviewer-local repair assessment into the downstream AGENTS/reviewer packet. Before REWORK require conditional assessment of unchanged objective/design/paths/authority/effects/commit owner, determined evidence and focused verification. Validate allowed reviewerLocalRepairBoundary/reviewerLocalRepairBasis reason tokens from the parent standard. A tiny closed-evidence workflow repair considers reviewer-local first; boundary change justifies worker route. Preserve independent reviewer owner responsibility; machine checks validate the decision envelope, not semantic smallness. Do not force a specific provider or commit role from an intake anecdote.
6. Add a bounded downstream finding intake schema/template and dedup/back-link contract under the existing F2G owner responsibility. Version/source SHA/observed-expected/negative evidence/chain joins/defect lane/disposition/parent owner/claim limit are mandatory. Create intake deterministically from an explicit finding input at the review boundary; no daemon, scanner, remote submission or silent knowledge ingestion. Parent dedup/admission/accept-decline links are explicit; generation is not automatic semantic acceptance. Source project claims from the snapshot remain unverified until actual project evidence is separately admitted.
7. Truthful coverage output distinguishes INSTALLED, INVOKED, PROVEN_HERMETIC and NOT_APPLICABLE_WITH_REASON/BLOCKED per phase/control with exit/result/evidence identity. Remove broad agent-enforcement-ready inference from shallow doctor/bridge status. Real CCMAI adoption/hosted PR verification and public rollout stay DEFERRED_PRIVATE_ONLY with owner/checkpoint, never a T1 proven claim. Fresh projects receive the profile; pre-existing projects get explicit migration/coverage gaps without rewriting history or project-owned content.
8. Prove the full chain in an offline disposable golden project created from a local fresh clone and staged candidate overlay (worker cannot commit). Overlay only the declared changed files; record staged/worktree raw identity so a HEAD-only clone cannot falsely test old code. Disable bytecode/cache pollution. Run bootstrap twice; preserve existing project-owned content byte-for-byte; deliberate continuity drifts on each truth surface, malformed status, reviewer self-review/unsupported claim, unjustified REWORK and override/no-op gate must fail. Mandatory gate failure propagates through doctor/workspace aggregate/PR command runner. Include source-derived positive and negative controls, LF/CRLF checkout transformations, Windows actual run and platform-neutral Python tests. If actual Linux execution is unavailable, record NOT_EXECUTED_PLATFORM_UNAVAILABLE and keep cross-OS/hosted rollout unproven; no WSL install or remote CI trigger. Do not fabricate CCMAI PR results.
9. Evidence includes exact changed set/hashes/profile pins, phase-control applicability/coverage, test commands/results, pre-fix repro for each locally verified class, preservation/idempotency, negative mutations, dedup disposition and explicit deferred real-adoption/public evidence. Full worker return and acceptance ledger join all requirements; separate reviewer probe pending. One cooperative240-minute turn; <=600 physical lines per new file, existing tracked size debt must not grow. New family split <=16 files per family; no general refactor. Stop for a missing required mutation surface rather than silently expanding.


## Independent Review Probe Admission Contract

independentProbeRequired: YES
independentProbeRiskClass: HIGH
independentProbeDispositionAtDispatch: PLAN_ADMITTED_PENDING_REVIEWER_EXECUTION
probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER
implementationOracleSeparation: REQUIRED_DIFFERENT_FIXTURE_AND_ASSERTION_PATH
positiveControl: reviewer-owned fresh project truth fixture matches trusted pinned profile and actual invocation receipt.
negativeMutationClasses: stale phase/memory/handoff; inline/unknown status skip; missing mandatory control/no-op override; unjustified REWORK; stale pin/unsupported claim; self-review; false CI execution.
expectedInformationGain: actual inherited gate invocation and refusal chain, not AI/provider behavior.
rerunCostReason: one narrow independent oracle after return; consume valid worker evidence, no broad duplicate suite.
reviewerDecisionOwner: LOCAL

Worker records PENDING_REVIEWER_EXECUTION.

## Semantic Convergence Outcome

Standard: `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "downstream-gate-inheritance",
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

## Prospective File-Size Admission

New family files <=600 lines each, <=16 per family; existing tracked file-size debt must not grow. Allowed split within new families only. `docs/reviews/CVF_DGIP_T1_DOWNSTREAM_GATE_INHERITANCE_WORKER_RETURN_2026-10-03.md` <=620 lines; `docs/reviews/evidence/cvf-dgip-t1-worker-2026-10-03.json` <=950 lines; combined <=512KiB. One cooperative240-minute turn, costs UNKNOWN; no OS resource-enforcement claim.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: operator-requested parent machine-control implementation after bound release; Local commits packet then continuity; worker changes admitted checker/template/runner/test owners only.

Protected paths: `scripts/new-cvf-workspace.ps1`; `scripts/check_cvf_workspace_agent_enforcement.ps1`; `scripts/check_cvf_workspace_new_project_enforcement.ps1`; `scripts/write_cvf_workspace_web_evidence_bridge.ps1`; `scripts/sync_cvf_workspace_rule_pack.ps1`; `scripts/lib/downstream_catalog/CvfDownstreamBootstrapContent.ps1`; `scripts/lib/downstream_catalog/CvfGoldenHarnessSupport.ps1`; `scripts/test_cvf_golden_downstream_bootstrap.ps1`; `governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/test_check_gate_to_role_closeability.py`; `governance/compat/test_downstream_gate_profile.py`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `scripts/lib/downstream_governance/`; `docs/reference/downstream_gate_profile/`; `AGENT_HANDOFF_V63_2026-09-18.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`.

Operator authorization: current instruction to orchestrator/reviewer to implement work order for manual worker relay.
Rollback boundary: revert only this new private implementation/continuity, preserve S05 STOP/frozen evidence and all existing project-owned content; no historical rewriting/public/security effects.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatcher/reviewer |
| Provider or surface | private shared CVF workspace |
| Session or invocation | CVF-DGIP-T1 |
| Working directory | repository root |
| Command or tool surface | local governed reads, scaffold, packet authoring and structural gates |
| Target paths | `docs/baselines/CVF_GC018_DGIP_T1_DOWNSTREAM_GATE_INHERITANCE_2026-10-03.md`; `docs/reviews/evidence/ccmai-to-cvf-downstream-gate-learning-intake-2026-10-01.txt`; `docs/reviews/evidence/cvf-dgip-t1-dispatch-inputs-2026-10-03.json`; `docs/work_orders/CVF_AGENT_WORK_ORDER_DGIP_T1_DOWNSTREAM_GATE_INHERITANCE_2026-10-03.md` |
| Allowed scope source | operator explicitly instructed orchestrator/reviewer to create work order |
| Before status evidence | clean worktree at HEAD 6c3e5ac7f39ba1406e09c99a4d1f9a1fb00b923c; four exact dispatcher paths absent |
| After status evidence | four dispatcher artifacts only, no implementation/project effect |
| Diff evidence | git diff --check; git status --short --untracked-files=all |
| Approval boundary | manual worker relay after actual bound gate; no dispatcher worker/provider invocation |
| Claim boundary | portable downstream gate implementation, no native proof |
| Agent type | INTERNAL_AGENT dispatcher |
| Invocation ID | dgip-t1-dispatch-20261003 |
| Expected manifest | `docs/baselines/CVF_GC018_DGIP_T1_DOWNSTREAM_GATE_INHERITANCE_2026-10-03.md`; `docs/reviews/evidence/ccmai-to-cvf-downstream-gate-learning-intake-2026-10-01.txt`; `docs/reviews/evidence/cvf-dgip-t1-dispatch-inputs-2026-10-03.json`; `docs/work_orders/CVF_AGENT_WORK_ORDER_DGIP_T1_DOWNSTREAM_GATE_INHERITANCE_2026-10-03.md` |
| Actual changed set | `docs/baselines/CVF_GC018_DGIP_T1_DOWNSTREAM_GATE_INHERITANCE_2026-10-03.md`; `docs/reviews/evidence/ccmai-to-cvf-downstream-gate-learning-intake-2026-10-01.txt`; `docs/reviews/evidence/cvf-dgip-t1-dispatch-inputs-2026-10-03.json`; `docs/work_orders/CVF_AGENT_WORK_ORDER_DGIP_T1_DOWNSTREAM_GATE_INHERITANCE_2026-10-03.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_dispatch_release_readiness.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_independent_review_probe_admission.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | first-section envelope; acceptance ledger; gate-role graph; SCEC predecessor/retained counters/escalation; trace/delta fields; standalone independent-probe declaration |
| gateRunPurpose | Confirm bounded paired design dispatch before release, not first discovery |
| claimBoundary | Declaration/static evidence only; not runtime enforcement |

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - named owner/source learning implementation, no full corpus or all-files-read claim.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Input source | `docs/reviews/evidence/ccmai-to-cvf-downstream-gate-learning-intake-2026-10-01.txt` / `docs/reviews/evidence/cvf-dgip-t1-dispatch-inputs-2026-10-03.json` |
| Chain map route | CCMAI advisory learning -> private source verification/dedup -> integrated parent implementation -> Local proof |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | Golden Bootstrap/GLP/review-cost/F2G + portable downstream profile |
| Disposition | SOURCE_COMPARISON_RUNTIME_PENDING |
| Claim boundary | current Core verified gaps; historical project facts unverified; no real downstream/public effects |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Claim Boundary

Worker changes only the existing exact paths and two new bounded families listed below, plus exact test/return paths. Private provenance implementation and hermetic disposable tests only. No real downstream project, public clone, workspace-root inventory/promotion, customer data, secrets/provider memory, provider/live call, network/fetch/install, host security/control mutation, public sync/push/deploy or worker commit. S05 roots/packets/C1 STOP remain frozen and unrelated. No subagents.

Pure file-based control-plane/hermetic checks, not live AI governance or production enforcement. Real CCMAI rollout/hosted CI and actual Linux evidence are not implied. DEFERRED_PRIVATE_ONLY.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Command: `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json`; 0 items, truncated=false.

Returned defects: NONE_RETURNED

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id CVF-DGIP-T1 --title "Portable Downstream Gate Inheritance" --date 2026-10-03 --base 6c3e5ac7f39ba1406e09c99a4d1f9a1fb00b923c --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | protected-governance-path plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | integrated parent implementation contract, bounded scope, golden proof and external-intake boundary |
| checkerReadAheadConfirmation | listed current-session source/literal reads before packet authoring; prior full mechanical checker reads reused |
| docOnlyNewFields | prospective profileId/control coverage/intake linkage; worker implements exact versioned schema |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Decision / Baseline / Proposed Tranche

Integrated private parent implementation admitted only after material/continuity and actual bound gate PASS. No automatic worker/provider call or external rollout.

## Evidence Requirements

Full source/proof/hash/coverage/negative-test receipts per work order; no historical CCMAI facts accepted as private proof.

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | portable downstream gate inheritance |
| claimDisposition | CLAIM_REJECTED: no runtime behavior proven |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: implementation will occur only under bound release; no OS action or source execution |
| invocationBoundary | private control-plane implementation/hermetic tests only |
| interceptionBoundary | no implemented enforcement |
| claimLanguage | proposals, UNKNOWN or NO_GO, cases planned |
| forbiddenExpansion | payload/install/build/upstream import/control mutation/voice/render/provider/public/deploy |

