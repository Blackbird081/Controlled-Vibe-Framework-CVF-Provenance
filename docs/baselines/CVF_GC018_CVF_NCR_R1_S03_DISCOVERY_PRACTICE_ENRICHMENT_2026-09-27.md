# CVF GC-018 Baseline - NCR-R1/S03 Discovery Practice Enrichment

Memory class: governed-dispatch-baseline

docType: baseline

Status: DISPATCH_READY

Batch ID: CVF-NCR-R1-S03

Dispatch base head: `3557276d97e9becd0c3d094c753e54a511016b16`

providerExecutionAuthority: FORBIDDEN

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Local technical disposition; operator retains effect, data and expense decisions

Reviewer owner: Local orchestrator/reviewer

Worker target: one shared-workspace INTERNAL_AGENT

## Purpose

Enrich the existing ACTIVE `cvf-governance-skill-discovery-invocation` package body with three role-specific worked examples for dispatcher selection, worker context routing, and reviewer governance orientation. Keep the change documentation-only and preserve all existing lifecycle, receipt, authority, attribution, and host boundaries.

## Authorization / Decision

The operator authorized the Local orchestrator/reviewer to create the next roadmap work order after R1/S02. NCR roadmap D013, accepted R0/S01 source reconciliation, R1/S01 package-body repair, and R1/S02 content closure at material commit `555999a83` permit source verification and a separate bounded discovery-content packet. They do not authorize package metadata mutation, skill execution, evaluation, host exposure, provider/live work, public sync, or production effect.

## Scope

Worker may modify only the existing discovery package `SKILL.md` and create the paired pending worker return. The body enrichment must add one worked example for each existing task class and role mapping: dispatcher/`skill-selection`, worker/`context-routing`, reviewer/`governance-orientation`. Each example states input task context, metadata or boundary evidence used, selection or no-match/rejection result, and the resulting Allowed Reads/Allowed Writes boundary.

No new task class, trigger pattern, registry field, workflow skill, resolver behavior, automatic invocation claim, or runtime receipt is introduced.

## Baseline Invariants

- The package remains ACTIVE; lifecycle, certification, UAT, adapter, registry, source, truth packet, and generated indexes are unchanged.
- Package guidance cannot grant task authority or expand an active work order.
- Metadata selection is advisory; selection is not invocation, body delivery, or permission to act.
- A no-match result is valid and must not force a best-effort skill selection.
- Read authority is not execution authority. Only commands expressly listed in the paired work order may run.
- Worker leaves both owned paths unstaged and uncommitted for distinct Local review.
- Any needed edit outside the two-path worker manifest returns as a blocker.

## Verification / Evidence

Record the discovery body pre/post raw SHA-256, exact diff, a role-to-example matrix, confirmation that machine-readable sibling paths are byte-unchanged, the exact two-path status, and all allowed validation results. Static gates prove document shape only; they do not prove runtime selection, invocation, host discovery, provider behavior, or skill effectiveness.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind package-skill --batch-id CVF-NCR-R1-S03 --title "Discovery Practice Enrichment" --date 2026-09-27 --base 3557276d97e9becd0c3d094c753e54a511016b16 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --no-evidence-readiness-applicable --stdout` |
| generatedProfile | package-skill and no-commit internal worker |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | exact two-path write manifest, D013 source bindings, read-versus-execute boundary, worked-example acceptance |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_package_skill_productionization_pipeline.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| docOnlyNewFields | none |
| claimBoundary | dispatch authority only; no package execution proof |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| next D013 slice | governed direction | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | D013 | discovery enrichment remains separately scoped | NCR roadmap | ACCEPT |
| predecessor closure | completion evidence | `docs/reviews/CVF_CVF_NCR_R1_S02_TEST_EVIDENCE_AUDIT_CONTENT_COMPLETION_2026-09-27.md` | Decision / Recommendation / Disposition | next discovery/content or SOP phase needs separate authority | Local reviewer | ACCEPT |
| existing coverage | source/design evidence | `docs/reviews/CVF_CVF_NCR_R0_S01_CORE_SKILLS_RECONCILIATION_WORKER_RETURN_2026-09-27.md` | Discovery Practice Coverage | three consumers already map to three task classes | accepted S01 evidence | ACCEPT |
| target body | current source | `docs/reference/agent_system_skills/packages/cvf-governance-skill-discovery-invocation/SKILL.md` | Purpose; Invocation Boundary; Inputs And Outputs | abstract selection/routing/orientation guidance | ASSF package | ACCEPT |
| ACTIVE state | current source | `docs/reference/agent_system_skills/packages/cvf-governance-skill-discovery-invocation/skill.source.json` | lifecycleState | ACTIVE | ASSF source | ACCEPT |
| task classes | current source | `docs/reference/agent_system_skills/registry/entries/cvf-governance-skill-discovery-invocation.json` | taskClasses, roles, phases, triggerPatterns | existing three-role coverage | ASSF registry | ACCEPT |
| truth boundary | current source | `docs/reference/agent_system_skills/truth/packets/cvf-governance-skill-discovery-invocation.json` | authorityBoundary, lifecycleSnapshot | receipt-backed explicit execution only | ASSF truth | ACCEPT |
| phase discipline | canonical owner | `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md` | phase ladder and claim boundaries | content edit cannot self-promote | ASSF SOP | ACCEPT |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| R1/S02 closure | material commit `555999a83` and named completion | separate bounded next packet allowed | ACCEPT |
| discovery package ACTIVE state | package/source/registry/truth agree | preserve state; no machine-readable mutation | ACCEPT |
| new workflow skill | no distinct consumer/input/output/trigger gap found | requires separate positive evidence | DEFER |
| SOP/package productionization | candidate content and operator choice required | no phase skip from this order | DEFER |
| host/runtime/evaluation | separate authority and proof | no effect under this order | DEFER |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | one existing package-body enrichment and one return; no execution authority |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_package_skill_productionization_pipeline.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | dispatch status, Source Verification columns, package phase block, no-commit boundary, private export reason |
| gateRunPurpose | confirmation of source-backed dispatch shape, not first discovery |
| claimBoundary | document admission only, not package behavior proof |

## Package Skill Productionization Control Block

- SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`
- Current phase: existing ACTIVE package-body content maintenance.
- Target lifecycle state: ACTIVE unchanged.
- Prior phase evidence: R0/S01 coverage map, R1/S01 body closure, R1/S02 content closure, and current package/source/registry/truth.
- Next forbidden skip: no metadata/source/truth/index mutation, new package, evaluation, host exposure, invocation, use proof, or production claim.
- Runtime/provider proof: NOT_RUN; expressly forbidden.
- Claim boundary: role-specific human-readable examples only.

## Claim Boundary

This baseline authorizes one existing package-body prose enrichment and one pending return. It makes no new resolver, automatic-selection, invocation, host, provider, live, public, deployment, effectiveness, or production claim.

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | NOT_APPLICABLE_WITH_REASON |
| reason | package prose is edited without executing or observing a runtime path |
| requiredFutureAction | separately authorize and freshly verify any runtime or host claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch and package-content maintenance only.
