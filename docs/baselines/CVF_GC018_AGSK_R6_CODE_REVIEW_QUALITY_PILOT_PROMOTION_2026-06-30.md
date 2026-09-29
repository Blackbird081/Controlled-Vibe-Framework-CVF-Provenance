# CVF GC-018 Baseline: AGSK-R6 Code Review Quality Pilot Promotion

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

docType: baseline

Batch ID: AGSK-R6

dispatchBaseHead: 932001da

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
|---|---|
| Decision | promote one AGSK-R3 package root to bounded runtime-loader eligibility |
| Baseline | AGSK-R5 closed with 24 package roots, zero runtime eligible, and lifecycle blockers identified |
| Proposed tranche | pilot `cvf-engineering-code-review-quality` with UAT, certification, and internal-agent disposition evidence |
| Execution route | Codex direct implementation with reviewer-owned commit |
| Closure posture | CLOSED_PASS_BOUNDED after source-state update, generated-index regeneration, body-read smoke, focused tests, and governance gates |

## Purpose

AGSK-R6 creates the first runtime-eligible CVF ASSF package root from the 24
AGSK-R3 upstream package adaptations. The pilot package is
`cvf-engineering-code-review-quality` because it is useful for governed review
work and already has a package root, local loader coverage, and no provider or
external adapter dependency.

This baseline permits explicit internal package-loader body reads only. It does
not make the package ACTIVE, mutate automatic resolver behavior, expose a
CLI/MCP adapter, call providers, merge code, commit without the normal reviewer
flow, public-sync, or claim production readiness.

## Scope / Methodology

Allowed AGSK-R6 scope:

- update the pilot package registry entry lifecycle fields to `APPROVED`,
  `PASSED`, `CERTIFIED`, and `IMPLEMENTED`;
- update the pilot package root front door, body, and source metadata to match
  that bounded lifecycle state;
- regenerate the ASSF generated skill index from registry sources;
- run certified metadata admission, anatomy, drift, loader, audit, and focused
  regression checks;
- record closure evidence for one package root only.

Forbidden AGSK-R6 scope:

- setting package status to `ACTIVE`;
- changing automatic resolver invocation behavior;
- promoting any other package root;
- implementing external CLI/MCP adapters;
- calling providers or claiming live governance behavior;
- public-sync or production-readiness claims.

## Findings / Position

AGSK-R5 showed all 24 package roots blocked by `certificationState`,
`uatState`, and `internalAgentDisposition`. The pilot package has enough local
evidence for a bounded internal loader-read promotion: upstream source mirror,
AGSK-R3 package-root evidence, anatomy checks, generated-index drift checks,
AGSK-R5 eligibility audit, and AGSK-R6 loader body-read smoke.

The package body and registry both classify the pilot as `R1`. This corrects
the prior mismatch where the package body declared `R1` but the registry entry
declared `R0`.

## Risk / Corrective Action

| Risk | Corrective action |
|---|---|
| Certification could be mistaken for ACTIVE resolver behavior | Status remains `APPROVED`; claim boundary denies automatic invocation |
| Runtime eligibility could be mistaken for merge or commit authority | Authority ceiling and loader boundary deny merge, commit, provider, public, and production authority |
| Generated index could drift from source registry | Regenerate with `generate_assf_skill_index.py --generate` and verify drift |
| Other package roots could be accidentally promoted | Scope and audit evidence require exactly one runtime-eligible package root after this tranche |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`,
lifecyclePhase=`implementation`, surfaceSelector=`docs/reference/agent_system_skills`,
riskCeiling=`HIGH`, maxResults=`20`

Returned defects: NONE_RETURNED

Disclosure note: the read-only ADIF resolver returned no matching defects for
this implementation query.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Runtime loader requires certified, UAT-passed, implemented internal disposition before body reads | `governance/compat/run_assf_runtime_package_loader.py` | `_runtime_ineligibility_reasons` | `certificationState`; `uatState`; `internalAgentDisposition` | AGSK-R4 runtime package loader | RUNTIME_BEHAVIOR | ACCEPT |
| Runtime loader opens instruction bodies only when explicitly requested and eligible | `governance/compat/run_assf_runtime_package_loader.py` | `build_runtime_package_packet` | `include_instruction_bodies` | AGSK-R4 runtime package loader | RUNTIME_BEHAVIOR | ACCEPT |
| Certification lifecycle contract defines `CERTIFIED` and requires `uatState: PASSED` | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | Certification And UAT State Model | `CERTIFIED`; `PASSED` | ASSF certification lifecycle contract | LITERAL_INVARIANT | ACCEPT |
| Certified metadata checker rejects ACTIVE status for certified metadata | `governance/compat/check_assf_certified_metadata_admission.py` | `_check_certified_entry` | `ACTIVE` | ASSF certified metadata admission checker | RUNTIME_BEHAVIOR | ACCEPT |
| Pilot package root exists as a SKILL.md package body | `docs/reference/agent_system_skills/packages/cvf-engineering-code-review-quality/SKILL.md` | top-level metadata and package body | `skillId` | ASSF package root | EXISTS | ACCEPT |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | AGSK-R4 loader, AGSK-R5 audit helper, certification lifecycle contract, certified admission checker, pilot package root, pilot registry entry |
| Runtime behavior claimed | explicit internal package-loader body read for one package root |
| Live/provider proof claimed | N/A_WITH_REASON: no provider/API/model behavior or live governance behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |
| Freshness disposition | PASS - source supports bounded body-read promotion, not ACTIVE activation |

## Evidence / Verification

| Evidence | Required or observed result |
|---|---|
| Source-state update | pilot registry records `APPROVED`, `PASSED`, `CERTIFIED`, and `IMPLEMENTED` |
| Generated index drift | regenerated index matches registry sources |
| Runtime loader smoke | pilot package is runtime eligible and body is loaded only with explicit body request |
| Runtime eligibility audit | 24 package roots, 1 runtime eligible, 23 runtime ineligible |
| Provider/live proof | NOT_RUN_WITH_REASON: no live provider behavior is claimed |

## Artifact Manifest

| Artifact | Status |
|---|---|
| `docs/reference/agent_system_skills/registry/entries/cvf-engineering-code-review-quality.json` | UPDATED |
| `docs/reference/agent_system_skills/packages/cvf-engineering-code-review-quality/SKILL.md` | UPDATED |
| `docs/reference/agent_system_skills/packages/cvf-engineering-code-review-quality/README.md` | UPDATED |
| `docs/reference/agent_system_skills/packages/cvf-engineering-code-review-quality/skill.source.json` | UPDATED |
| `docs/reference/agent_system_skills/generated/skill-index.json` | REGENERATED |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_R6_CODE_REVIEW_QUALITY_PILOT_PROMOTION_2026-06-30.md` | CLOSED_PASS_BOUNDED |
| `docs/reviews/CVF_AGSK_R6_CODE_REVIEW_QUALITY_PILOT_PROMOTION_COMPLETION_2026-06-30.md` | CLOSED_PASS_BOUNDED |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | AGSK-R4 runtime package loader and ASSF generated index | explicit body-read guidance for one package only; no action authority | loader smoke and audit evidence | no external adapter | `IMPLEMENTED_BOUNDED` |
| `EXTERNAL_AGENT_CLI_MCP` | future adapter only | no external mutation, activation, provider call, public-sync, commit, or push | claim boundary | separate adapter contract required | `DEFERRED_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | AGSK-R3 package root -> AGSK-R4 loader -> AGSK-R5 audit -> AGSK-R6 one-package lifecycle promotion |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | AGSK-R6 baseline, work order, completion review, package root, registry entry, and generated index |
| Disposition | IMPLEMENT bounded internal package-loader body read; defer ACTIVE resolver, external adapter, provider/live, public-sync, and production claims |
| Claim boundary | No external source or provider-local memory is promoted as CVF authority in AGSK-R6 |

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | Exactly one pilot package root is promoted to runtime-loader eligibility | audit smoke PASS |
| AC2 | Pilot package body loads only through explicit body request | loader smoke PASS |
| AC3 | Generated index is regenerated from registry source | drift checker PASS |
| AC4 | Certified metadata admission passes | certified metadata checker PASS |
| AC5 | No ACTIVE, provider, external adapter, public-sync, merge, or commit authority is claimed | claim boundary PASS |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_R6_CODE_REVIEW_QUALITY_PILOT_PROMOTION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_AGSK_R6_CODE_REVIEW_QUALITY_PILOT_PROMOTION_COMPLETION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | N/A with reason: AGSK-R6 is operator-directed follow-on promotion, not a roadmap status edit | N/A with reason | PASS |
| Registry JSON | pilot registry entry | lifecycle fields updated | PASS |
| Registry Markdown | pilot package `SKILL.md` and `README.md` | lifecycle boundary updated | PASS |
| External evidence digest | N/A with reason: no external evidence digest created; AGSK-R6 consumes governed ASSF sources | N/A with reason | N/A with reason |
| System loop interlock | N/A with reason: no system-loop runtime loop change in AGSK-R6 | N/A with reason | PASS |
| Session continuity | N/A with reason: material baseline does not update session state; session-sync may follow after material commit | N/A with reason | PASS |
| Focused tests | ASSF loader and audit tests | PASS after execution | PASS |
| Runtime smoke | AGSK-R4 loader and AGSK-R5 audit | one eligible package root | PASS |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Live proof | this file | N/A with reason: no live governance behavior claim | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this baseline references private provenance package roots and internal
governed ASSF metadata. Public-safe export requires separate redaction and
public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | AGSK-R6 bounded one-package runtime-loader eligibility |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - one package may be opened by the internal loader after lifecycle gates pass |
| receiptEvidence | CVF_RECEIPT_PRESENT - loader smoke, audit smoke, drift, anatomy, and admission checks |
| actionEvidence | ACTION_EVIDENCE_PRESENT - registry, package root, source metadata, and generated index updated |
| invocationBoundary | governed local Python helper and generated ASSF metadata only |
| interceptionBoundary | no IDE, shell hook, git hook, provider, CLI/MCP, Web, public-sync, or external runtime interception claim |
| claimLanguage | promotes one package root to explicit internal loader body-read eligibility |
| forbiddenExpansion | no ACTIVE resolver, automatic invocation, external adapter, provider/live proof, public-sync, merge, commit, or production-readiness claim |

## Claim Boundary

AGSK-R6 implements a bounded internal lifecycle promotion for one ASSF package
root only. It does not activate automatic resolver behavior, execute reviews
autonomously, grant merge or commit authority, expose CLI/MCP adapters, call
providers, public-sync, or claim production readiness.
