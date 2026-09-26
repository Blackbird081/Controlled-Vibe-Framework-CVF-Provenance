# CVF GC-018 Baseline - NCR-R1/S01 Skill Lifecycle Body Reconciliation

Memory class: governed-dispatch-baseline

docType: baseline

Status: DISPATCH_READY

Batch ID: CVF-NCR-R1-S01

Dispatch base head: `2de2a9eea48ee560dc7ae70fe63f0828208c445d`

providerExecutionAuthority: FORBIDDEN

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Local technical disposition; operator retains effect, data and expense decisions

Reviewer owner: Local orchestrator/reviewer

Worker target: one shared-workspace INTERNAL_AGENT

## Purpose

Correct the active lifecycle prose in the two existing CVF engineering package bodies identified by NCR-R0/S01. Keep their substantive TDD and code-review instructions, upstream attribution, machine metadata and host boundaries intact.

## Authorization / Decision

The operator authorized Local to progress tranche by tranche and stop at the finished work order for relay to Claude. NCR roadmap D013 and closed S01 completion `09b62aa3b57fd8dfda93140f30a845b7177be24c` authorize this exact package-content repair. They do not authorize a candidate audit skill, discovery enrichment, host exposure or lifecycle promotion.

## Scope

Worker may edit only the two named `SKILL.md` bodies and create one pending worker return under the paired work order. Read the exact existing source JSON, registry, truth, promotion reviews and package productionization owner before editing. Reconcile all present-tense lifecycle and policy-binding claims in each body against existing ACTIVE evidence. Preserve historical APPROVED promotion statements by explicitly dating or qualifying them where needed.

## Baseline Invariants

- ACTIVE status is already recorded in both package source, registry and truth surfaces; this task repairs contradictory human-readable bodies and does not promote a lifecycle state.
- A package body does not grant task authority, provider access, test execution, commit, public export, host auto-selection or production readiness.
- All substantive TDD/code-review procedures, source attribution and license notices remain intact.
- Worker leaves edits uncommitted and unstaged for distinct Local review.
- If current source contradicts the S01 trace, stop and return the exact conflict; do not widen the manifest.

## Verification / Evidence

Record before/after raw SHA-256 for both bodies, a line-level lifecycle-claim inventory, exact diff, current metadata alignment, package-specific validation and full worker-return gate. Check `git diff --check` and exact three-path status. A package-specific gate passing verifies its configured checks only; it does not prove actual provider/host behavior.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind package-skill --batch-id CVF-NCR-R1-S01 --title "Core Skill Lifecycle Body Reconciliation" --date 2026-09-27 --base 2de2a9eea --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --no-evidence-readiness-applicable --stdout` |
| generatedProfile | package-skill and no-commit internal worker |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | exact three-path write manifest and S01 source-backed lifecycle acceptance |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_package_skill_productionization_pipeline.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| docOnlyNewFields | none |
| claimBoundary | dispatch authority only; no package execution proof |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| D013 scope | governed roadmap | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | D013 | R1 content and S01 prerequisite | Local roadmap | ACCEPT |
| S01 disposition | completion evidence | `docs/reviews/CVF_CVF_NCR_R0_S01_CORE_SKILLS_RECONCILIATION_COMPLETION_2026-09-27.md` | Findings / Position | two body prose mismatches | Local review | ACCEPT |
| TDD body | current source | `docs/reference/agent_system_skills/packages/cvf-engineering-test-driven-development/SKILL.md` | Status, Scope, Claim Boundary | APPROVED wording | ASSF package | ACCEPT |
| code-review body | current source | `docs/reference/agent_system_skills/packages/cvf-engineering-code-review-quality/SKILL.md` | Status, Scope, Claim Boundary | APPROVED wording | ASSF package | ACCEPT |
| TDD source | current source | `docs/reference/agent_system_skills/packages/cvf-engineering-test-driven-development/skill.source.json` | lifecycleState | ACTIVE | ASSF source | ACCEPT |
| review source | current source | `docs/reference/agent_system_skills/packages/cvf-engineering-code-review-quality/skill.source.json` | lifecycleState | ACTIVE | ASSF source | ACCEPT |
| package sequence | canonical owner | `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md` | End-To-End Phase Ladder | existing ACTIVE versus body correction | ASSF SOP | ACCEPT |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| S01 Local closure | `09b62aa3b57fd8dfda93140f30a845b7177be24c` | bounded source trace accepted | ACCEPT |
| ACTIVE sibling metadata | two source JSON files, registry entries and truth packets | recheck before body edit | ACCEPT |
| host/runtime behavior | not requested | separate work order and authority | DEFER |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | bounded existing-package body repair only |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_package_skill_productionization_pipeline.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | dispatch status, Source Verification columns, package phase block, private export reason |
| gateRunPurpose | confirmation of source-backed dispatch shape, not first discovery |
| claimBoundary | document admission only, not package behavior proof |

## Package Skill Productionization Control Block

- SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`
- Current phase: existing ACTIVE package body maintenance after prior promotion.
- Target lifecycle state: ACTIVE unchanged.
- Prior phase evidence: S01 reconciliation and cited ASCP/AGSK promotion records in both source JSON files.
- Next forbidden skip: no candidate creation, new activation, host projection or use proof.
- Runtime/provider proof: NOT_RUN; no invocation authorized.
- Claim boundary: human-readable body reconciliation only.

## Claim Boundary

This baseline authorizes only the exact existing-package body prose repair and one pending return. It makes no new selection, execution, host, provider, live, public, deployment or production claim.

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | NOT_APPLICABLE_WITH_REASON |
| reason | current task edits package prose; no runtime path is executed or asserted |
| requiredFutureAction | independently authorize and verify any host or runtime claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch and package-content maintenance only.
