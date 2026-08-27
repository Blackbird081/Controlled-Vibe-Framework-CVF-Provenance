# CVF GC-018 Baseline - AGTR-R1 Agent Skill Registry Structural Reconciliation

Memory class: governed-baseline

Status: APPROVED_FOR_EXECUTION

Batch ID: AGTR-R1

Date: 2026-08-27

Decision owner: operator authority exercised by the orchestrator/reviewer under the standing full-authority instruction.

## Purpose

Authorize one no-commit worker pass to repair the canonical structure of
`AGT-021` through `AGT-034` in private provenance and public-sync without
changing validator policy or the records' substantive authority.

## Decision / Baseline / Proposed Tranche

Decision: `CONTINUE_HIGH_VALUE`. Baseline: private HEAD `22c28f04b` and public
HEAD `d27d3db261404e8f594f130702ca7ef2c86a0ee7`. Proposed tranche: AGTR-R1
only, capped at one worker return and fourteen mirrored record pairs.

## Evidence / Verification

Hosted Documentation & Testing run `33053902261` fails only Governance Registry
Validation and dependent Status Check. Local unchanged validation reproduces
89 error lines against the fourteen named records. Hash comparison proves all
fourteen private/public pairs are byte-identical before execution.

## Large-Scope Authorization

The numerical scope is authorized because fourteen files are one homogeneous
registry-owner family with the same validator contract and mirrored boundary.
This does not authorize broad corpus cleanup. Exactly `AGT-021` through
`AGT-034` may change in each repository; all other paths are forbidden except
the named private worker return.

## Scope / Target / Owner Boundary

Authorized private and public targets are the existing files whose basenames
begin `AGT-021_` through `AGT-034_` under
`governance/skill-library/registry/agent-skills/`.

The worker must preserve the pre-edit record's ID, title, source/provenance,
capability meaning, constraints, risk, autonomy, dependencies, licensing and
UAT references. Removal is limited to duplicated or format-corrupted copies of
content retained in a readable canonical location.

## Scaffold Provenance Block

| Field | Evidence |
| --- | --- |
| scaffold source | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` and the accepted PSRR single-tranche packet family |
| retained structure | GC-018 authority, source verification, scope cap, dual-agent boundary, public disposition, no-commit return |
| intentional delta | AGT semantic-preservation ledger and mirrored fourteen-file owner family |
| validation | governed authoring, dispatch quality, reviewer-fast and pre-commit gates |

## Dependency Release Evidence

| Dependency | State | Evidence | Disposition |
| --- | --- | --- | --- |
| PSRR-R1 user registry | closed bounded | public SHA `d27d3db2`; USR validator errors zero | RELEASED |
| GC-019/public surface repair | closed bounded | Public Surface `33053902181`; Static CI `33053902347` | RELEASED |
| AGT semantic fidelity | unresolved by design | fourteen malformed source records | OWNED_BY_AGTR_R1 |
| PR merge/deploy | not authorized | operator boundary | PARKED |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| agent records require five sections plus risk/autonomy rows | code contract | `governance/skill-library/registry/validate_registry.py` | `validate_agent_skill`; agent validation loop | `validate_agent_skill` | registry validator | ACCEPT |
| AGT-001 through AGT-020 provide valid local structure | repository evidence | `governance/skill-library/registry/agent-skills/AGT-020_ANALYTICS_DASHBOARD_GENERATOR.gov.md` | complete record | `AGT-020` | agent registry | ACCEPT |
| AGT-021 is flattened and duplicated | repository evidence | `governance/skill-library/registry/agent-skills/AGT-021_CONTEXT_ENGINEERING_OPTIMIZER.gov.md` | leading content and later readable sections | `AGT-021` | agent registry | ACCEPT |
| AGT-034 retains readable semantics but lacks canonical validator sections | repository evidence | `governance/skill-library/registry/agent-skills/AGT-034_OPERATOR_WORKFLOW_ORCHESTRATOR.gov.md` | headings and metadata | `AGT-034` | agent registry | ACCEPT |

## Negative Search And Collision Discipline

Search found no AGT generator or alternate canonical owner. Historical commits
are evidence inputs, not automatic authority. The valid `AGT-001..020` files
are structural exemplars only and must not be copied mechanically where doing
so would alter the later records' semantics.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 30 --json`

Returned defectIds: ADIF-0001, ADIF-0002, ADIF-0006, ADIF-0007, ADIF-0014,
ADIF-0015, ADIF-0016, ADIF-0017, ADIF-0020, ADIF-0021, ADIF-0024,
ADIF-0028, ADIF-0029, ADIF-0031, ADIF-0033, ADIF-0039, ADIF-0043,
ADIF-0044, ADIF-0045, ADIF-0049, ADIF-0051, ADIF-0052.

Applicable controls are source verification, exact ownership, checker
read-ahead, clean-worktree evidence, no-commit mode, per-record semantic review
and reviewer-owned closure. This static registry lane creates no executable
defect classification or runtime path.

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_governed_artifact_authoring.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_package_skill_productionization_pipeline.py` |
| literalTokensReviewed | `Decision / Baseline / Proposed Tranche`; `Large-Scope Authorization`; `Source Verification Block`; `Public Export Disposition`; `Claim Boundary` |
| gateRunPurpose | confirm with evidence one bounded mirrored structural repair |
| claimBoundary | authorization only; no repaired or green claim |

## Package Skill Productionization Control Block

SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`

Current phase: N/A with reason: static legacy AGT records are not ASSF package candidates.

Target lifecycle state: unchanged.

Prior phase evidence: existing registry records only.

Next forbidden skip: no activation, promotion, loading or runtime eligibility claim.

Runtime/provider proof: N/A with reason: static local documentation repair.

Claim boundary: structural registry compliance only.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | private/public AGT records | preserve existing documented authority | semantic ledger and validator | N/A with reason: no runtime adapter change | `IMPLEMENTED` |
| `EXTERNAL_AGENT_CLI_MCP` | public Markdown registry | read-only documentation consumption | mirrored public records | no CLI/MCP activation claim | `DEFERRED_WITH_REASON` |

## External Knowledge Intake Routing

Chain map source: `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | public/simple cvf vocabulary |
| Chain map route | NOT_APPLICABLE_WITH_REASON: no new external intake |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; N/A with reason: no external intake beyond current records and local git history |
| Owner surface | agent-skills registry |
| Disposition | LOCAL_ONLY_NO_EXTERNAL_INTAKE |
| Claim boundary | preserve existing provenance only; no upstream equivalence claim |

## Rescan Intelligence Hardening

- N/A with reason: AGTR-R1 repairs a fixed fourteen-record owner family and
  does not re-scan or refresh an external intake corpus.
- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

## Public/Provenance Boundary

Private is the provenance source of truth. Public receives byte-identical
copies of only the fourteen accepted records. The worker may not commit or
push either repository; reviewer owns materialization and hosted proof.

## Public Export Disposition

BLOCKED_MISSING_PUBLIC_ARTIFACTS

Reason: no accepted AGTR public commit or exact-SHA hosted proof exists.

## Claim Boundary

This baseline authorizes only one no-commit candidate across the fourteen
mirrored records and named private return. It authorizes no guessed semantics,
validator/workflow/index changes, source absorption, provider use, secrets,
merge, deploy, AGTR-R2, or unrelated repair.
