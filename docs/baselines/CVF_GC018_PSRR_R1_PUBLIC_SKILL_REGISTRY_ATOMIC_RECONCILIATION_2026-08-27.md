# CVF GC-018 Baseline - PSRR-R1 Public Skill Registry Atomic Reconciliation

Memory class: governed-dispatch-baseline

Status: APPROVED_FOR_EXECUTION

Batch ID: PSRR-R1

Dispatch base head: `35be0dbe5`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: independent orchestrator/reviewer

Worker target: one no-commit public generated-registry reconciliation worker

## Purpose

Authorize one bounded implementation that upgrades the existing user-registry
generator into the exact lifecycle owner for its generated outputs, proves
safe reconciliation in isolation, and emits the 62-record public registry
without weakening validation.

## Decision / Baseline

The operator selected the next roadmap after PCIT-R1-BD1 bounded closure.
Private dispatch base is `35be0dbe5`; public execution base is
`86b1e728d8363e66c700ffdde9c2f6c02c93ed1e`. PR `#4` remains unmerged.
One worker return is authorized; no PSRR-R2 exists.

## Evidence / Verification

The exact hosted public candidate is green except registry validation and its
dependent fail-closed status job. The existing generator discovers the 62
source files and writes desired records but does not remove stale outputs. The
existing cleaner deletes all 335 records plus the index. Read-only manifest
comparison finds six retained names, 329 stale names and 56 new names.

## Large-Scope Authorization

Scope and target: one generated owner family under the public user-skills
registry, plus generator and focused tests. The large changed count is required
because 329 stale generated filenames remain from an older 335-record source
set. Protected governance/session paths are not implementation targets.

Allowed deletion: only stale `USR-*.gov.md` outputs absent from the computed
desired manifest. `INDEX.md` may be deterministically replaced. No arbitrary
file or other registry family may be deleted. All writes remain Git-reversible,
uncommitted and independently reviewable.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind public-sync --batch-id PSRR-R1 --title "Public Skill Registry Atomic Reconciliation" --date 2026-08-27 --base 35be0dbe5 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | public-sync, package-skill trigger and no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with exact generator ownership, generated-family deletion boundary and one-tranche proof contract |
| checkerReadAheadConfirmation | work-order quality, governed authoring, route, export, scaffold and package-skill pipeline checkers |
| docOnlyNewFields | atomic reconciliation contract; large generated-family authorization |
| claimBoundary | dispatch provenance only; no implementation or hosted-green claim |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| PCIT-R1-BD1 | closure commit `8480ed51f`; continuity `35be0dbe5` | one separately selected registry roadmap | RELEASED_BY_OPERATOR |
| public candidate | exact SHA `86b1e728`; PR `#4` open | worker leaves public writes uncommitted | RELEASED_READ_ONLY_BASE |
| canonical generator | existing generator reads 62 source files and writes user records/index | implement exact safe reconciliation before applying | RELEASED_BOUNDED |
| hosted execution | all non-registry required families green | reviewer only after local acceptance | HELD_FOR_REVIEWER |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| generator is the current record/index owner | source owner | `governance/skill-library/registry/generate_user_skills.py` | lines 12-14, 79-199 | `SKILL_LIBRARY_PATH`; `OUTPUT_PATH`; `generate_gov_file`; `main` | user registry generator | ACCEPT |
| generator leaves stale outputs | lifecycle gap | `governance/skill-library/registry/generate_user_skills.py` | lines 147-199 | write desired files and index without stale deletion | user registry generator | ACCEPT |
| cleaner deletes every user record | destructive gap | `governance/skill-library/registry/clean_user_registry.py` | lines 17-41 | cleanup loop | legacy cleaner | ACCEPT |
| validator requires exact source parity and valid links/index | acceptance contract | `governance/skill-library/registry/validate_registry.py` | lines 132-176 | `main`; `validate_index`; source-link checks | registry validator | ACCEPT |
| registry is required hosted status | release boundary | `.github/workflows/documentation-testing.yml` | registry-validate and status-check jobs | `Governance Registry Validation`; `needs` | public CI | ACCEPT |

## Negative Search And Collision Discipline

Exact PSRR artifact paths and token were absent before authoring. Existing
PCIT artifacts remain predecessor evidence, not competing PSRR authority. The
new roadmap owns one successor identifier and no R2.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`public-sync`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_authoring.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_package_skill_productionization_pipeline.py` |
| literalTokensReviewed | approved status, source columns, large-scope boundary, package control and public disposition |
| gateRunPurpose | confirm dispatch shape after full source review |
| claimBoundary | structural pass does not prove implementation safety |

## Package Skill Productionization Control Block

SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`

Current phase: N/A with reason: legacy user governance projections are not
ASSF package lifecycle entries.

Target lifecycle state: unchanged.

Prior phase evidence: existing source library and generated projections.

Next forbidden skip: no promotion, activation, loading or runtime eligibility.

Runtime/provider proof: N/A with reason: local deterministic generation only.

Claim boundary: registry parity only.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | generator and generated user records | local Git-reversible generated outputs | tests and validator | N/A with reason: no agent adapter | `IMPLEMENTED` |
| `EXTERNAL_AGENT_CLI_MCP` | public Markdown records | read-only public artifact consumption only | public paths after reviewer export | no CLI/MCP adapter in scope | `DEFERRED_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | NOT_TRIGGERED with reason: no outside input or external repository is used |
| Matching local-view guard | `governance/compat/check_public_export_disposition.py` |
| Owner surface | public user-registry generator and generated records |
| Disposition | RECONCILED_DESIGN_INPUT_ONLY |
| Claim boundary | existing CVF source and hosted receipts only; no external knowledge promotion |

## Public/Provenance Boundary

Private provenance owns authority and the worker return. The sibling public
clone owns generator, focused tests and generated outputs. Worker may not
commit, push, merge, deploy, trigger hosted runs or access secrets.

## Public Export Disposition

BLOCKED_MISSING_PUBLIC_ARTIFACTS

Reason: no accepted PSRR public commit or exact-SHA hosted proof exists yet.

## Claim Boundary

This baseline authorizes one no-commit atomic reconciliation candidate. It
does not authorize source-skill or validator mutation, arbitrary deletion,
package activation, external-agent runtime, merge, deploy, secrets, providers
or a successor tranche.
