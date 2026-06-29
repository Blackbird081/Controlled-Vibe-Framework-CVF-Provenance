# CVF ASSF Package: Governance Skill Discovery And Invocation

Memory class: FULL_RECORD

Status: PROPOSED

docType: assf_package

Batch ID: AGSK-R3

skillId: cvf-governance-skill-discovery-invocation

## Purpose

Guide metadata-first skill discovery discipline: identify the development phase, match it to the right ASSF skill, read the skill metadata before invoking instructions, and route to CVF governance surfaces when CVF authority controls apply. This is the meta-skill governing how all other ASSF skills are discovered and invoked within CVF governance boundaries. Use when a governed CVF task needs to determine which skill applies to the current situation. Do not use when: runtime activation, automated skill injection, provider/live proof, or authority beyond the active governed work order is required.

## Scope / Applies-To

| Field | Value |
|---|---|
| Package root | `docs/reference/agent_system_skills/packages/cvf-governance-skill-discovery-invocation/` |
| Owner surface | ASSF package proposal evidence under AGSK-R3 |
| Applies to | Metadata-only advisory package review, not runtime execution |
| Does not apply to | `APPROVED`, `ACTIVE`, resolver/runtime mutation, CLI/MCP adapter, provider/live proof, public-sync, or production readiness |

## Invocation Boundary

| Field | Value |
|---|---|
| Allowed task classes | skill-discovery, skill-routing, phase-identification, invocation-guidance |
| Allowed roles | dispatcher, worker, reviewer |
| Allowed phases | INTAKE, DISPATCH_AUTHORING, WORKER_EXECUTION, REVIEWER_CLOSURE |
| Allowed surfaces | docs/reference/agent_system_skills/packages/cvf-governance-skill-discovery-invocation/, registry entries, review artifacts |
| Risk ceiling | R1 |
| Authority ceiling | metadata-only advisory; loading never authorizes automatic skill injection, resolver activation, or external actions |

## Inputs And Outputs

| Field | Value |
|---|---|
| Inputs | operator request or governed task context; source mirror file `.private_reference/source_mirrors/addyosmani__agent-skills/skills/using-agent-skills/SKILL.md`; active CVF authority and allowed-scope boundaries |
| Outputs | proposed package-body guidance (awaiting reviewer acceptance); skill discovery routing map notes; recommended CVF owner-surface routing |
| Acceptance evidence | AGSK-R3 worker return with package-root proposal evidence; reviewer-fast gate PASS; anatomy checker PASS |

## Risk And Authority

| Field | Value |
|---|---|
| Risk class | R1 |
| Authority ceiling | metadata-only advisory selection; this meta-skill does not grant authority to invoke any other skill beyond metadata reading |
| Side effects | none from metadata reading; skill resolver activation, automatic skill injection, or authority escalation requires separate authorization |
| Rollback | delete this package root and revert registry entry to CANDIDATE; regenerate generated index |
| Safe stop | stop and open a fresh ASSF runtime tranche if automatic skill routing, resolver activation, or authority above the active work order is needed |
| Policy bindings | none until APPROVED or ACTIVE lifecycle state with separate reviewer authorization; this meta-skill does not bootstrap authority for other skills |

## Progressive Disclosure

| Stage | Accessible fields |
|---|---|
| Metadata-only (CANDIDATE/PROPOSED) | skillId, name, status, purpose, triggerPatterns, riskCeiling, sourceArtifacts; meta-skill routing map accessible as guidance only |
| Post-reviewer-acceptance (APPROVED) | full skill discovery and routing protocol; requires reviewer decision gate |
| Runtime (ACTIVE) | full instructions with active resolver; requires UAT evidence and separate ACTIVE tranche; activation of this meta-skill does not activate other skills |

## Evidence And UAT

| Field | Value |
|---|---|
| Required evidence | AGSK-R3 worker return with source reads and 24-candidate coverage table; anatomy checker PASS |
| UAT binding | NOT_STARTED; APPROVED tranche requires UAT evidence and reviewer acceptance |
| Validation hooks | ASSF anatomy checker; generated-index drift checker; reviewer-fast gate |
| Review evidence | docs/reviews/CVF_AGSK_R3_RUNTIME_PACKAGE_ACTIVATION_WORKER_RETURN_2026-06-29.md |

## External Disposition

| Field | Value |
|---|---|
| External CLI/MCP disposition | DEFERRED_WITH_REASON: no external adapter authorized in AGSK-R3 |
| Adapter contract | N/A with reason: external adapter not authored in AGSK-R3 |
| Adapter evidence | N/A with reason: no adapter implemented |
| External mutation boundary | no external mutation, CLI/MCP export, provider call, public-sync, or package activation until separate ASSF adapter or runtime work order accepted |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | AGSK-R3 worker with reviewer packet-shape repair |
| Provider or surface | Local workspace |
| Session or invocation | AGSK-R3 package proposal execution, 2026-06-29 |
| Working directory | Repository root |
| Command or tool surface | PowerShell, repo-local Python governance checkers, apply_patch |
| Target paths | `docs/reference/agent_system_skills/packages/cvf-governance-skill-discovery-invocation/` |
| Allowed scope source | `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_R3_RUNTIME_PACKAGE_ACTIVATION_FOR_WORKER_2026-06-29.md` |
| Before status evidence | package root did not exist before AGSK-R3 worker execution |
| After status evidence | package root exists in PROPOSED state pending reviewer acceptance |
| Diff evidence | `git diff --name-status` over AGSK-R3 range |
| Approval boundary | WORKER_MUST_NOT_COMMIT; reviewer/closer owns acceptance and commit |
| Claim boundary | PROPOSED package-root evidence only; no runtime activation claim |
| Agent type | worker plus reviewer packet-shape repair |
| Invocation ID | `agsk-r3-package-cvf-governance-skill-discovery-invocation-2026-06-29` |
| Expected manifest | `SKILL.md`; `skill.source.json`; `README.md` |
| Actual changed set | `SKILL.md`; `skill.source.json`; `README.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Epistemic Process Block

### Expected Result / Prediction

A PROPOSED ASSF package root should preserve the upstream skill's useful workflow discipline while keeping CVF authority, lifecycle, and runtime boundaries explicit.

### Evidence Comparison

The package cites the pinned upstream source mirror, the AGSK-R2 source-mirror backfill review, the AGSK-R3 baseline, and the AGSK-R3 worker return. The package remains PROPOSED and does not claim APPROVED, ACTIVE, UAT, certification, runtime execution, provider behavior, or external adapter support.

### Contradiction Or Gap Disposition

No contradiction is resolved inside the package root. Any missing reviewer acceptance, UAT, certification, runtime loader, CLI/MCP adapter, provider proof, public export, or production-readiness evidence remains a blocker for later promotion.

### Claim Update

The package claim is narrowed to CVF-owned PROPOSED package-root evidence only. It is not activation evidence.
## Claim Boundary

This package root is a PROPOSED CVF adaptation sourced from the upstream `using-agent-skills` skill at pinned commit `aba7c4e9695c363e65cb59effe926c7f1d1abe3d`. It does not inject skills automatically, activate the resolver, bootstrap authority for other ASSF skills, implement a CLI/MCP adapter, or claim automatic invocation. Loading this meta-skill package never grants authority to any other skill package.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this package root cites private source mirror and private provenance registry surfaces.


