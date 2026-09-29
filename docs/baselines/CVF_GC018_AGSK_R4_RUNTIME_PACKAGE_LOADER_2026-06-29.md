# CVF GC-018 Baseline: AGSK-R4 Runtime Package Loader

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-29

docType: baseline

Batch ID: AGSK-R4

dispatchBaseHead: 4003289a

## Decision / Baseline / Proposed Tranche

| Field | Disposition |
|---|---|
| Decision | implement a bounded internal runtime package loader for ASSF package metadata |
| Baseline | AGSK-R3 committed 24 PROPOSED package roots at `4003289a` |
| Proposed tranche | AGSK-R4 runtime package loader and focused tests |
| Execution route | Codex direct implementation with reviewer-owned commit |
| Closure posture | CLOSED_PASS_BOUNDED after focused tests and governance gates |

## Purpose

Create the first internal runtime package surface for CVF ASSF packages without
self-activating any package. The loader reads the generated ASSF index, applies
selector filters, reports runtime eligibility, and opens a package `SKILL.md`
body only when the caller explicitly requests instruction bodies and the
package passes the lifecycle gate.

This baseline does not certify the 24 AGSK-R3 packages, set `APPROVED` or
`ACTIVE`, implement external CLI/MCP adapter behavior, call providers, or grant
tool authority.

## Scope / Methodology

Allowed AGSK-R4 scope:

- add `governance/compat/run_assf_runtime_package_loader.py`;
- add focused tests in `governance/compat/test_run_assf_runtime_package_loader.py`;
- read the generated ASSF index and package-root topology;
- require `certificationState: CERTIFIED`, `uatState: PASSED`,
  `internalAgentDisposition: IMPLEMENTED`, and an in-scope package
  `canonicalRoot` ending in `SKILL.md` before opening an instruction body;
- keep default output metadata-only and no-body;
- return denial reasons for `PROPOSED` or otherwise ineligible packages;
- document completion in this baseline, paired work order, and completion
  review.

Forbidden AGSK-R4 scope:

- setting any registry entry to `APPROVED`, `ACTIVE`, `PASSED`, `CERTIFIED`, or
  `IMPLEMENTED`;
- mutating package roots, generated index sources, resolver behavior, hook
  catalogs, provider/live paths, Web runtime, public-sync, or session state;
- treating an opened `SKILL.md` body as authority to perform actions;
- implementing CLI/MCP adapter behavior or external-agent mutation.

## Findings / Position

AGSK-R3 made the 24 upstream skills package-shaped but still `PROPOSED`.
Current ASSF contracts support a bounded loader only if it preserves the
no-self-activation invariant. AGSK-R4 therefore implements runtime package
readout and gated body loading, while current AGSK-R3 packages remain
`NOT_RUNTIME_ELIGIBLE` until later UAT, certification, and implementation
evidence exists.

## Risk / Corrective Action

| Risk | Corrective action |
|---|---|
| Runtime helper could be mistaken for activation | Output claim boundary states it is not an activation receipt |
| `PROPOSED` packages could have `SKILL.md` opened by mistake | Body loading requires `CERTIFIED`, `PASSED`, and `IMPLEMENTED` |
| Out-of-scope canonical roots could be read | Loader accepts only repo-relative package roots under `docs/reference/agent_system_skills/packages/` ending in `SKILL.md` |
| External adapter support could be inferred | Claim boundary denies CLI/MCP behavior and mutation |
| Loader could expand authority | Packet states work-order scope and caller authority remain controlling |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add one new read-only governance helper
and one focused test under `governance/compat/` for ASSF runtime package
loading.

Protected paths:

- `governance/compat/run_assf_runtime_package_loader.py`
- `governance/compat/test_run_assf_runtime_package_loader.py`

Operator authorization: operator explicitly requested runtime packages for CVF
after AGSK-R3 package roots were created.

Rollback boundary: remove only the AGSK-R4 loader, test, paired governance
artifacts, and completion evidence. Do not revert AGSK-R3 package roots,
registry entries, generated index, or unrelated governance helpers.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`,
lifecyclePhase=`implementation`, surfaceSelector=`governance/compat`,
riskCeiling=`HIGH`, maxResults=`20`

Returned defects: NONE_RETURNED

Disclosure note: the read-only ADIF resolver returned no matching defects for
this implementation query.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| AGSK-R3 committed 24 package roots as PROPOSED, not runtime-active packages | `docs/reviews/CVF_AGSK_R3_RUNTIME_PACKAGE_ACTIVATION_WORKER_RETURN_2026-06-29.md` | Registry Source-State Update Evidence; Resolver Runtime Activation Boundary | `PROPOSED`; `NOT_APPLICABLE_WITH_REASON` | AGSK-R3 worker return | VALUE_SET | ACCEPT |
| ASSF package contract defines package lifecycle states | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Package lifecycle states | `CANDIDATE`; `PROPOSED`; `APPROVED`; `ACTIVE` | ASSF package contract | VALUE_SET | ACCEPT |
| ASSF composition contract forbids self-activation | `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md` | No-Self-Activation Invariant | `APPROVED`; `ACTIVE`; `UAT` | ASSF composition contract | LITERAL_INVARIANT | ACCEPT |
| Certification contract requires UAT before certification | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | Certification And UAT State Model | `certificationState`; `uatState` | ASSF certification lifecycle contract | LITERAL_INVARIANT | ACCEPT |
| Generated index is metadata-only and not activation evidence | `docs/reference/agent_system_skills/generated/skill-index.json` | `claimBoundary` | `claimBoundary` | ASSF generated index | LITERAL_INVARIANT | ACCEPT |
| Existing resolver is read-only and does not open SKILL.md | `governance/compat/run_assf_skill_resolver.py` | module docstring; `resolve_skill_packet` | `resolve_skill_packet` | ASSF metadata resolver | RUNTIME_BEHAVIOR | ACCEPT |
| External readout denies adapter implementation and instruction-body execution | `governance/compat/run_assf_external_agent_metadata_readout.py` | `CLAIM_BOUNDARY` | `CLAIM_BOUNDARY` | ASSF external metadata readout | LITERAL_INVARIANT | ACCEPT |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | `run_assf_skill_resolver.py`; `run_assf_external_agent_metadata_readout.py`; ASSF package/composition/certification contracts; generated skill index |
| Package roots before AGSK-R4 | AGSK-R3 package roots exist, but current 24 AGSK package entries remain `PROPOSED`, `NOT_STARTED`, and not implemented |
| Runtime behavior claimed | bounded internal package packet and lifecycle-gated instruction-body read only |
| Live/provider proof claimed | N/A_WITH_REASON: no provider/API/model behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |
| Freshness disposition | PASS - source supports a gated internal loader, not activation or adapter behavior |

## Evidence / Verification

| Evidence | Required or observed result |
|---|---|
| Focused unit tests | `python -m unittest governance.compat.test_run_assf_runtime_package_loader` PASS, 7 tests |
| ASSF drift check | `python governance/compat/check_assf_skill_index_drift.py` PASS |
| ASSF anatomy check | `python governance/compat/check_assf_package_candidate_anatomy.py --enforce` PASS |
| Real-index smoke | `cvf-engineering-code-review-quality` returns `NOT_RUNTIME_ELIGIBLE` when instruction bodies are requested |
| Reviewer-fast gate | pending rerun after literal-format repairs |

## Artifact Manifest

| Artifact | Status |
|---|---|
| `governance/compat/run_assf_runtime_package_loader.py` | IMPLEMENTED |
| `governance/compat/test_run_assf_runtime_package_loader.py` | IMPLEMENTED |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_R4_RUNTIME_PACKAGE_LOADER_2026-06-29.md` | CLOSED_PASS_BOUNDED |
| `docs/reviews/CVF_AGSK_R4_RUNTIME_PACKAGE_LOADER_COMPLETION_2026-06-29.md` | CLOSED_PASS_BOUNDED |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | `run_assf_runtime_package_loader.py` | internal agents may ask for a bounded package packet; package body read requires explicit request and lifecycle gates; no action authority is granted | focused tests and smoke output | no external adapter | `IMPLEMENTED_BOUNDED` |
| `EXTERNAL_AGENT_CLI_MCP` | future adapter only | external agents cannot use this helper to mutate, activate, execute, or publish packages | external readout boundary remains controlling | separate adapter work order required | `DEFERRED_WITH_REASON` |

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | Runtime loader returns bounded metadata package packets | focused unit tests PASS |
| AC2 | Instruction bodies are not opened by default | focused unit test patches `open` and PASS |
| AC3 | Instruction bodies open only after explicit request and lifecycle eligibility | synthetic eligible test PASS |
| AC4 | Real AGSK-R3 `PROPOSED` package is denied body loading | smoke command returns `NOT_RUNTIME_ELIGIBLE` |
| AC5 | No package lifecycle state, generated index, resolver, adapter, provider, public-sync, or session state was changed | `git diff --name-status` review and focused scope |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | AGSK-R3 package-root proposals -> AGSK-R4 bounded internal runtime package loader |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | AGSK-R4 baseline, work order, completion review, runtime loader helper, and focused tests |
| Disposition | IMPLEMENT bounded internal loader; defer activation, certification, external adapter, provider/live, and public-sync |
| Claim boundary | No external source or provider-local memory is promoted as CVF authority in AGSK-R4 |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_R4_RUNTIME_PACKAGE_LOADER_2026-06-29.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_AGSK_R4_RUNTIME_PACKAGE_LOADER_COMPLETION_2026-06-29.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | N/A with reason: AGSK-R4 is operator-directed follow-on runtime helper, not a roadmap status edit | N/A with reason | PASS |
| Registry JSON | N/A with reason: no registry JSON or generated index edit in AGSK-R4 | `check_assf_skill_index_drift.py` PASS | PASS |
| Registry Markdown | N/A with reason: no registry Markdown edit in AGSK-R4 | N/A with reason | PASS |
| External evidence digest | N/A with reason: no external evidence digest created; AGSK-R4 consumes existing governed AGSK-R3 package roots | N/A with reason | N/A with reason |
| System loop interlock | N/A with reason: no system-loop interlock roadmap or runtime loop change in AGSK-R4 | N/A with reason | PASS |
| Session continuity | N/A with reason: material baseline does not update session state; session-sync may follow after material commit | N/A with reason | PASS |
| Focused tests | `governance/compat/test_run_assf_runtime_package_loader.py` | 7 unittest cases PASS | PASS |
| Runtime smoke | `run_assf_runtime_package_loader.py` | `packageBodyDisposition=NOT_RUNTIME_ELIGIBLE` for current AGSK-R3 package | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Current AGSK-R3 package body loading | denied until UAT/certification/implementation evidence exists | `NOT_RUNTIME_ELIGIBLE` | PASS |
| Helper authority grant | no authority grant | claim boundary denies authority expansion | PASS |
| External adapter | not implemented | `EXTERNAL_AGENT_CLI_MCP` remains `DEFERRED_WITH_REASON` | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this baseline references private provenance package roots and private
governance helper surfaces. Public-safe export requires separate redaction and
public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | AGSK-R4 bounded internal runtime package loader |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - loader reads generated metadata and optionally opens eligible package bodies only after explicit request |
| receiptEvidence | CVF_RECEIPT_PRESENT - focused tests, smoke output, and completion review |
| actionEvidence | ACTION_EVIDENCE_PRESENT - helper, test, and source verification |
| invocationBoundary | governed local Python helper and tests only |
| interceptionBoundary | no IDE, shell hook, git, provider, CLI/MCP, Web, public-sync, or external runtime interception claim |
| claimLanguage | implements a bounded internal runtime package loader; does not activate packages |
| forbiddenExpansion | no package promotion, no certification, no generated index mutation, no resolver mutation, no external adapter, no provider/live proof, no public-sync, no production-readiness claim |

## Claim Boundary

AGSK-R4 implements a bounded internal runtime package loader only. It does not
promote, certify, activate, execute, publish, or externally expose any ASSF
package. Current AGSK-R3 package roots remain ineligible for instruction-body
loading until later governed UAT, certification, and implementation evidence
exists.
