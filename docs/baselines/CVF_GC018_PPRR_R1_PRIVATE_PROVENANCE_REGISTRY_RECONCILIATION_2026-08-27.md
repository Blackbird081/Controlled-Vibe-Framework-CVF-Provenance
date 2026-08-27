# CVF GC-018 Baseline - PPRR-R1 Private Provenance Registry Reconciliation

Memory class: governed-baseline

Status: CLOSED_PASS_BOUNDED

Batch ID: PPRR-R1

Date: 2026-08-27

Decision owner: operator authority exercised by the orchestrator/reviewer under the standing full-authority instruction.

Active quality assessment: the private unchanged registry validator is red
because 335 generated user records no longer represent its 62 current source
skills, while the accepted public owner family is 62/62 and green.

Quality-first decision: REMEDIATE_FIRST

Remediation target: exact private provenance parity with the accepted public
generator and generated user-registry family.

Quality protection commitments: retain the unchanged validator and sources;
use exact hashes and manifest-limited deletion; forbid public or semantic scope.

## Purpose

Authorize one no-commit worker pass to reconcile the private generated
user-skill registry from the already reviewed public owner family.

## Decision / Baseline / Proposed Tranche

Decision: `CONTINUE_HIGH_VALUE`. Baseline: private HEAD
`91fff28bb72235489aafe95883385efe761962de` and read-only public HEAD
`af957e279a8118b152d957a29f5731c6304a86bf`. Proposed tranche: PPRR-R1
only, capped at one worker return and one atomic generated-owner family.

## Evidence / Verification

Private has 62 source skills, 335 generated records, generator digest
`fe831d48f1e1f44e45813e0fa898d6abe8558f51757bc475d0538d6ef9d043c8`,
no focused generator test and a failing validator. Public has the identical
source-name digest, 62 records, accepted generator digest
`0a4161cb94a068260d2eb0dfe590a8ebebb9ef7ddfd27e78b9a07e66cd2bae8a`,
a focused test and a passing unchanged validator.

## Large-Scope Authorization

The large path count is one deterministic generated owner family, not broad
corpus cleanup. Authorized private changes are the generator, focused test,
index, 62 desired records, deletion of manifest-stale `USR-*.gov.md` records,
and the named return. No other deletion or owner is authorized.

## Scope / Target / Owner Boundary

Writable private paths:

- `governance/skill-library/registry/generate_user_skills.py`
- `governance/skill-library/registry/test_generate_user_skills.py`
- `governance/skill-library/registry/user-skills/INDEX.md`
- `governance/skill-library/registry/user-skills/USR-*.gov.md`
- `docs/reviews/CVF_PPRR_R1_PRIVATE_PROVENANCE_REGISTRY_RECONCILIATION_WORKER_RETURN_2026-08-27.md`

The public repository, source skills, validator, agent records, workflows,
cleaner, products, dependencies and continuity surfaces are read-only for the
worker.

## Dependency Release Evidence

| Dependency | State | Evidence | Disposition |
| --- | --- | --- | --- |
| PSRR-R1 generated owner | accepted and exported | reviewer addendum and public commit `d27d3db2` | RELEASED_AS_EXACT_SOURCE |
| AGTR-R1 agent family | closed green | public commit `af957e27` and hosted proof | RELEASED |
| private source-name manifest | exact public match | digest `a08b90d...` in both repositories | RELEASED |
| public mutation or hosted rerun | unnecessary | target is private-only parity | PARKED |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| validator requires exact source-record parity, links and index | code contract | `governance/skill-library/registry/validate_registry.py` | user validation and main count checks | `validate_user_skill`; `validate_index`; `main` | registry validator | ACCEPT |
| PSRR owner safely reconciles the generated family | accepted review evidence | `docs/reviews/CVF_PSRR_R1_PUBLIC_SKILL_REGISTRY_ATOMIC_RECONCILIATION_WORKER_RETURN_2026-08-27.md` | Independent Reviewer Addendum | public commits `d35e84e2`, `01d27608`, `d27d3db2` | PSRR reviewer closure | ACCEPT |
| public agent family and full registry are green | accepted completion evidence | `docs/reviews/CVF_AGTR_R1_AGENT_SKILL_REGISTRY_STRUCTURAL_RECONCILIATION_COMPLETION_2026-08-27.md` | Material And Hosted Evidence | public commit `af957e27` | AGTR reviewer closure | ACCEPT |
| private and public source manifests are identical | repository evidence | `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/README.md` | current 62-file source tree under the named owner | `*.skill.md` source-name manifest | end-user skill library | ACCEPT |

## Negative Search And Collision Discipline

No PPRR authority or competing private generator owner exists. PSRR-R1 is the
accepted owner evidence; PPRR-R1 is a private provenance synchronization, not
a redesign or a second public registry roadmap.

## Scaffold Provenance Block

| Field | Evidence |
| --- | --- |
| scaffold source | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` and accepted PSRR/AGTR packet shapes |
| retained structure | GC-018 authority, source verification, exact ownership, no-commit return and reviewer closure |
| intentional delta | private-only accepted-byte import and atomic stale-record deletion boundary |
| validation | task routing, dispatch quality, worker-return and pre-commit gates |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | private generated registry | static read-model parity only | exact hashes and validator | N/A with reason: no runtime adapter | `IMPLEMENTED` |
| `EXTERNAL_AGENT_CLI_MCP` | unchanged public registry | no public behavior changes | public exact commit remains source comparison | no CLI/MCP change | `DEFERRED_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | public/simple cvf vocabulary |
| Chain map route | NOT_APPLICABLE_WITH_REASON: same-project public/private provenance reconciliation only |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; no external knowledge intake |
| Owner surface | generated user-skill registry |
| Disposition | LOCAL_ONLY_NO_EXTERNAL_INTAKE |
| Claim boundary | accepted public bytes are comparison evidence, not outside authority |

## Rescan Intelligence Hardening

- N/A with reason: fixed generated manifests are compared; no external corpus
  rescan, refresh or absorption occurs.
- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

## Package Skill Productionization Control Block

SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`

Current phase: N/A with reason: legacy generated registry parity only.

Target lifecycle state: unchanged.

Prior phase evidence: PSRR-R1 accepted owner.

Next forbidden skip: no promotion, activation, loading or eligibility.

Runtime/provider proof: N/A with reason: local deterministic files.

Claim boundary: generated registry parity only.

## Public/Provenance Boundary

Private provenance receives exact already accepted public owner bytes. The
public repository is read-only and must remain clean at the captured SHA.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this tranche corrects private provenance only. Public-sync already
contains the accepted owner family and no new public artifact is required.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defectIds: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044.

Applicable controls are exact source verification, manifest-bounded deletion,
clean-state evidence, no-commit mode, reviewer independence and no successor.

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_governed_artifact_authoring.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_task_governance_route.py` |
| literalTokensReviewed | quality-first fields, large-scope authorization, source columns, private-only disposition and claim boundary |
| gateRunPurpose | confirm with evidence that dispatch authority is complete before a large generated-family reconciliation; not first discovery |
| claimBoundary | authorization only; no imported or green private state is claimed |

## Claim Boundary

This baseline authorizes one private, Git-reversible generated-owner candidate.
It grants no public write, source-skill change, semantic rewrite, provider,
runtime, merge, deployment or successor authority.

## Closure Evidence

Independent reviewer accepted private material commit
`9cfdc6af838fcf3818c075f84df1be3faf5183e5`. The unchanged registry validator
passes at 62 user, 34 agent, and 62 source skills. Focused tests pass 10/10,
generator check is drift-free, and the public clone remains unchanged. The
private encoding exception is a bounded `ADAPTED_WITH_REASON` delta: normalized
generated data parity is 63/63, while generator and test retain explicit local
markers. All material pre-commit checks passed 87/87.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_PPRR_R1_PRIVATE_PROVENANCE_REGISTRY_RECONCILIATION_2026-08-27.md` | `CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_PPRR_R1_PRIVATE_PROVENANCE_REGISTRY_RECONCILIATION_WORKER_RETURN_2026-08-27.md` | accepted material `9cfdc6af838fcf3818c075f84df1be3faf5183e5` | PASS |
| Roadmap state | `docs/roadmaps/CVF_PRIVATE_PROVENANCE_REGISTRY_RECONCILIATION_ROADMAP_2026-08-27.md` | terminal one-tranche close | PASS |
| Registry JSON | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | closed PPRR-R1 evidence | PASS |
| Registry Markdown | `CVF_SESSION_MEMORY.md`; `AGENT_HANDOFF_V59_2026-08-11.md` | closed mode | PASS |
| External evidence digest | N/A with reason: private-only local reconciliation | public source SHA unchanged | N/A WITH REASON |
| System loop interlock | PPRR cap one | no automatic PPRR-R2 | PASS |
| Session continuity | bootstrap, state sources, aggregate, front door, handoff | `pprr_r1_closed_pass_bounded` | PASS |
