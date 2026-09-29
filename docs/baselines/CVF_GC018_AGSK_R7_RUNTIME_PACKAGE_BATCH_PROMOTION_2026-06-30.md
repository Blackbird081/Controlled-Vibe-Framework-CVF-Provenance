# CVF GC-018 Baseline: AGSK-R7 Runtime Package Batch Promotion

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-30

docType: baseline

Batch ID: AGSK-R7

dispatchBaseHead: 0ce9838c

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
|---|---|
| Decision | promote five additional AGSK-R3 package roots to bounded runtime-loader eligibility |
| Baseline | AGSK-R6 closed with 24 package roots, 1 runtime eligible, and 23 still blocked by lifecycle gates |
| Proposed tranche | batch promotion for planning, spec, test, debugging, and security packages |
| Execution route | Codex direct implementation with reviewer-owned commit |
| Closure posture | CLOSED_PASS_BOUNDED after source-state update, generated-index regeneration, body-read smoke, focused tests, and governance gates |

## Purpose

AGSK-R7 expands the bounded internal runtime-package set after the AGSK-R6
pilot proved the lifecycle path. The promoted package roots are:

- `cvf-engineering-planning-task-breakdown`
- `cvf-engineering-spec-driven-development`
- `cvf-engineering-test-driven-development`
- `cvf-engineering-debugging-error-recovery`
- `cvf-engineering-security-hardening`

This baseline permits explicit internal package-loader body reads only. It does
not make any package ACTIVE, mutate automatic resolver behavior, expose a
CLI/MCP adapter, call providers, merge code, public-sync, or claim production
readiness.

## Scope / Methodology

Allowed AGSK-R7 scope:

- update the five target package registry entries to `APPROVED`, `PASSED`,
  `CERTIFIED`, and `IMPLEMENTED`;
- update target package front doors, bodies, and source metadata to match the
  bounded lifecycle state;
- align risk metadata where registry and package body disagreed;
- regenerate the ASSF generated skill index from registry sources;
- run certified metadata admission, anatomy, drift, loader, audit, and focused
  regression checks;
- record closure evidence for these five package roots only.

Forbidden AGSK-R7 scope:

- setting package status to `ACTIVE`;
- changing automatic resolver invocation behavior;
- promoting package roots outside the five target packages;
- implementing external CLI/MCP adapters;
- calling providers or claiming live governance behavior;
- public-sync or production-readiness claims.

## Findings / Position

AGSK-R6 established one package-root promotion pattern. The five AGSK-R7
packages have enough governed local evidence for bounded internal body-read
promotion: upstream source mirror, AGSK-R3 package-root evidence, package
anatomy checks, generated-index drift checks, certified metadata admission, and
AGSK-R4/AGSK-R5 loader and audit paths.

Risk metadata is corrected conservatively. Planning and spec package registry
entries are raised from `R0` to `R1` to match their package bodies. Security is
kept conservative at `R2` by raising the package body to match the registry.
Test and debugging remain `R1`.

## Risk / Corrective Action

| Risk | Corrective action |
|---|---|
| Certified packages could be mistaken for ACTIVE resolver behavior | Status remains `APPROVED`; claim boundary denies automatic invocation |
| Runtime eligibility could be mistaken for action authority | Loader boundary denies edit, merge, commit, provider, public, and production authority |
| Generated index could drift from source registry | Regenerate with `generate_assf_skill_index.py --generate` and verify drift |
| Batch scope could accidentally promote unrelated packages | Audit evidence requires exactly six runtime-eligible package roots after AGSK-R7 |

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
| Generated skill index is regenerated from registry entries | `docs/reference/agent_system_skills/generated/README.md` | regeneration instructions | `generate_assf_skill_index.py --generate` | ASSF generated index source layout | LITERAL_INVARIANT | ACCEPT |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | AGSK-R4 loader, AGSK-R5 audit helper, certification lifecycle contract, certified admission checker, target package roots, target registry entries |
| Runtime behavior claimed | explicit internal package-loader body read for five additional package roots |
| Live/provider proof claimed | N/A_WITH_REASON: no provider/API/model behavior or live governance behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |
| Freshness disposition | PASS - source supports bounded body-read promotion, not ACTIVE activation |

## Evidence / Verification

| Evidence | Required or observed result |
|---|---|
| Source-state update | five target registries record `APPROVED`, `PASSED`, `CERTIFIED`, and `IMPLEMENTED` |
| Generated index drift | regenerated index matches registry sources |
| Runtime loader smoke | target packages are runtime eligible and bodies load only with explicit body request |
| Runtime eligibility audit | 24 package roots, 6 runtime eligible, 18 runtime ineligible |
| Provider/live proof | NOT_RUN_WITH_REASON: no live provider behavior is claimed |

## Artifact Manifest

| Artifact | Status |
|---|---|
| five target registry entries | UPDATED |
| five target package `SKILL.md` files | UPDATED |
| five target package `README.md` files | UPDATED |
| five target package `skill.source.json` files | UPDATED |
| `docs/reference/agent_system_skills/generated/skill-index.json` | REGENERATED |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_R7_RUNTIME_PACKAGE_BATCH_PROMOTION_2026-06-30.md` | CLOSED_PASS_BOUNDED |
| `docs/reviews/CVF_AGSK_R7_RUNTIME_PACKAGE_BATCH_PROMOTION_COMPLETION_2026-06-30.md` | CLOSED_PASS_BOUNDED |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | AGSK-R4 runtime package loader and ASSF generated index | explicit body-read guidance for six packages total; no action authority | loader smoke and audit evidence | no external adapter | `IMPLEMENTED_BOUNDED` |
| `EXTERNAL_AGENT_CLI_MCP` | future adapter only | no external mutation, activation, provider call, public-sync, commit, or push | claim boundary | separate adapter contract required | `DEFERRED_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | AGSK-R3 package roots -> AGSK-R4 loader -> AGSK-R5 audit -> AGSK-R6 pilot -> AGSK-R7 batch promotion |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | AGSK-R7 baseline, work order, completion review, package roots, registry entries, and generated index |
| Disposition | IMPLEMENT bounded internal package-loader body reads; defer ACTIVE resolver, external adapter, provider/live, public-sync, and production claims |
| Claim boundary | No external source or provider-local memory is promoted as CVF authority in AGSK-R7 |

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | Exactly five additional package roots are promoted to runtime-loader eligibility | audit smoke PASS |
| AC2 | Target package bodies load only through explicit body request | loader smoke PASS |
| AC3 | Generated index is regenerated from registry source | drift checker PASS |
| AC4 | Certified metadata admission passes | certified metadata checker PASS |
| AC5 | No ACTIVE, provider, external adapter, public-sync, merge, or commit authority is claimed | claim boundary PASS |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_R7_RUNTIME_PACKAGE_BATCH_PROMOTION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_AGSK_R7_RUNTIME_PACKAGE_BATCH_PROMOTION_COMPLETION_2026-06-30.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | N/A with reason: AGSK-R7 is operator-directed follow-on promotion, not a roadmap status edit | N/A with reason | PASS |
| Registry JSON | five target registry entries | lifecycle fields updated | PASS |
| Registry Markdown | five target package `SKILL.md` and `README.md` files | lifecycle boundary updated | PASS |
| External evidence digest | N/A with reason: no external evidence digest created; AGSK-R7 consumes governed ASSF sources | N/A with reason | N/A with reason |
| System loop interlock | N/A with reason: no system-loop runtime loop change in AGSK-R7 | N/A with reason | PASS |
| Session continuity | N/A with reason: material baseline does not update session state; session-sync may follow after material commit | N/A with reason | PASS |
| Focused tests | ASSF loader and audit tests | PASS after execution | PASS |
| Runtime smoke | AGSK-R4 loader and AGSK-R5 audit | six eligible package roots | PASS |
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
| claimScope | AGSK-R7 bounded five-package runtime-loader eligibility |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - five additional packages may be opened by the internal loader after lifecycle gates pass |
| receiptEvidence | CVF_RECEIPT_PRESENT - loader smoke, audit smoke, drift, anatomy, and admission checks |
| actionEvidence | ACTION_EVIDENCE_PRESENT - registry, package root, source metadata, and generated index updated |
| invocationBoundary | governed local Python helper and generated ASSF metadata only |
| interceptionBoundary | no IDE, shell hook, git hook, provider, CLI/MCP, Web, public-sync, or external runtime interception claim |
| claimLanguage | promotes five package roots to explicit internal loader body-read eligibility |
| forbiddenExpansion | no ACTIVE resolver, automatic invocation, external adapter, provider/live proof, public-sync, merge, commit, or production-readiness claim |

## Claim Boundary

AGSK-R7 implements a bounded internal lifecycle promotion for five ASSF package
roots only. It does not activate automatic resolver behavior, execute package
guidance autonomously, grant merge or commit authority, expose CLI/MCP
adapters, call providers, public-sync, or claim production readiness.
