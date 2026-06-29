# CVF Agent Work Order - AGSK-T5 First External Absorption Package Candidate

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-29

docType: work_order

Batch ID: AGSK-T5

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: 3ce884c9

## Dispatch Prompt Envelope

Role: no-commit worker for AGSK-T5 documentation-only ASSF registry candidate creation; Codex remains reviewer/closer.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_T5_FIRST_EXTERNAL_ABSORPTION_PACKAGE_CANDIDATE_2026-06-29.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

Base: executionBaseHead must be captured with `git rev-parse --short HEAD` before edits.

Current-time notes: current date is 2026-06-29. AGSK-T4 is closed at material commit `2a84036a`; `riskTriggers` is now present in the ASSF package contract. No live key, provider call, runtime run, public-sync, resolver mutation, checker wiring, package root, or package activation is authorized.

Do-not-misread notes: execute AGSK-T5 only. Create the first AGSK-derived registry candidate and regenerate the ASSF skill index. Do not create `packages/<skill-id>/SKILL.md`, do not promote the candidate above `CANDIDATE`, do not wire a resolver or checker, and do not edit session state.

Required first actions: read this work order, the triage roadmap, the ASSF package contract, registry README, existing registry entries, generator, drift checker, active session front door/state/handoff, guard orientation, and gotchas; then capture `git status --short` and run pre-implementation autorun.

Return contract: return `COMPLETE_PENDING_REVIEW`, `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, or `BLOCKED_WITH_REASON` with changed paths, executionBaseHead, gate results, source-verification evidence, generated-index drift proof, and HEAD unchanged.

## Purpose

Convert the AGSK-T5 roadmap decision into a bounded no-commit worker packet.
The worker creates one ASSF registry source entry for
`cvf-governance-external-absorption` at `CANDIDATE` state, regenerates the
metadata-only skill index from registry sources, and returns evidence for
reviewer acceptance.

## 1. Mission

Author the first AGSK-derived external-absorption skill candidate in the
existing ASSF registry source layout. Success means one new registry source
JSON exists, `docs/reference/agent_system_skills/generated/skill-index.json`
is regenerated from source, the drift checker passes, and all claims remain
metadata-only and documentation-only.

## 2. Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Operator instruction | chat request on 2026-06-29: "next tranche" and "viet work order cho next tranche" | authorizes work-order authoring for AGSK-T5 |
| Active session front door | `CVF_SESSION_MEMORY.md` | names AGSK-T5 as next allowed move; prerequisite AGSK-T4 is closed at material commit `2a84036a` |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | generated state registry with AGSK-T5 next allowed move |
| Active handoff | `AGENT_HANDOFF_V26_2026-06-28.md` | active handoff named by state registry |
| Triage roadmap | `docs/roadmaps/CVF_AGSK_PACKAGE_CANDIDATE_TRIAGE_ROADMAP_2026-06-29.md` | opens AGSK-T5 and defines minimum outputs, status ceiling, non-goals, and acceptance criteria |
| T4 closure authority | `docs/reviews/CVF_AGSK_T4_ASSF_RISK_TRIGGERS_FIELD_PATCH_WORKER_RETURN_2026-06-29.md`; material commit `2a84036a` | confirms `riskTriggers` contract field is available before T5 |
| Contract owner surface | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | canonical package contract, including `riskTriggers` |
| Registry owner surface | `docs/reference/agent_system_skills/registry/README.md` | authoritative registry source layout and generator flow |
| External absorption owner surfaces | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md`; `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | source-backed capability content for the candidate |
| Source review | `docs/reviews/CVF_AGSK_ABSORPTION_PACK_REABSORPTION_REVIEW_2026-06-29.md` | source review and value-conversion matrix proving package-candidate opportunity |

Authority boundary:

- If this work order conflicts with the triage roadmap, ASSF package contract,
  or registry README, stop and return `BLOCKED_WITH_REASON`.
- External AGSK material is evidence input only. The worker must create a
  CVF-owned registry entry and must not copy pack-local runtime, persona,
  slash-command, hook, or checker vocabulary as CVF authority.

## 3. Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | authored this source-verified work order |
| Worker | assigned no-commit worker agent | creates the registry candidate, regenerates the index, and returns evidence |
| Reviewer/closer | Codex | validates returned diff, gates, source fidelity, claim boundary, and commits if accepted |
| Operator approval required | operator | any expansion into runtime, resolver, checker wiring, public-sync, provider/live proof, session-sync ownership, package root creation, approval/promotion, or package activation |

## 4. Scope

Allowed scope:

- create `docs/reference/agent_system_skills/registry/entries/cvf-governance-external-absorption.json`;
- regenerate `docs/reference/agent_system_skills/generated/skill-index.json` using the existing ASSF generator command listed in this work order's evidence requirements;
- create `docs/reviews/CVF_AGSK_T5_FIRST_EXTERNAL_ABSORPTION_PACKAGE_CANDIDATE_WORKER_RETURN_2026-06-29.md`;
- run read-only source searches, JSON validation, drift check, and governance gates;
- repair documentation formatting or evidence blocks inside the owned files.

Forbidden scope:

- creating `docs/reference/agent_system_skills/packages/` or any `SKILL.md`;
- changing existing registry source entries except if a generator or drift check proves a mechanical formatting correction is mandatory and the worker records the reason;
- editing `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`;
- editing any `governance/compat/*.py` checker, hook, autorun script, generator, or test;
- editing `.private_reference/legacy/` or external repo/folder contents;
- editing `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, or `AGENT_HANDOFF*.md`;
- claiming runtime behavior, resolver selection, provider/live proof, package activation, production readiness, public readiness, or public-sync.

Risk ceiling: R0 documentation and metadata-only registry candidate.

## Scope / Target / Owner Boundary

Target: one new ASSF registry source entry, one regenerated metadata index, and
one worker-return artifact.

Owner boundary:

- worker owns only the paths listed in Write Ownership;
- Codex reviewer/closer owns material commit, completion review only if needed,
  and later session-sync if next move changes;
- operator approval is required for any expansion beyond AGSK-T5.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch-authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, surfaceSelector=`docs/work_orders`, riskCeiling=`HIGH`, maxResults=`20`

Returned defects: NONE_RETURNED

Disclosure note: resolver was invoked through `resolve_defect_packet(...)` from
`governance/compat/run_adif_defect_resolver.py`; it returned `totalCandidates=0`.

## 5. Required First Reads

Before editing files, read:

- `CVF_SESSION_MEMORY.md` - active front door and next-move context.
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` - generated state registry.
- `AGENT_HANDOFF_V26_2026-06-28.md` - active handoff.
- `docs/reference/guard_orientation/README.md` - applicable guard surfaces.
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` - literal-format pitfalls.
- this work order - execution authority.
- `docs/roadmaps/CVF_AGSK_PACKAGE_CANDIDATE_TRIAGE_ROADMAP_2026-06-29.md` - roadmap source and T5 acceptance.
- `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` - package contract and required field families.
- `docs/reference/agent_system_skills/registry/README.md` - registry source layout and generator flow.
- `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` - existing CANDIDATE entry shape and `registryOrder=1`.
- `docs/reference/agent_system_skills/registry/entries/cvf-worker-return-author.json` - existing CANDIDATE entry shape and `registryOrder=2`.
- `governance/compat/generate_assf_skill_index.py` - source-to-index generator.
- `governance/compat/check_assf_skill_index_drift.py` - generated-index drift checker.
- `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` - external absorption capability owner surface.
- `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` - external absorption routing owner surface.
- `docs/reviews/CVF_AGSK_ABSORPTION_PACK_REABSORPTION_REVIEW_2026-06-29.md` - source review and value-conversion matrix.

## 6. Pre-Flight Checks

Commands to run before implementation:

```powershell
git rev-parse --short HEAD
git status --short
Test-Path docs/reference/agent_system_skills/registry/entries/cvf-governance-external-absorption.json
Test-Path docs/reference/agent_system_skills/packages
rg -n "riskTriggers|Required field families|externalCliMcpDisposition|candidateState" docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md
rg -n "Adding A New Entry|registryOrder|CANDIDATE|generate_assf_skill_index.py|check_assf_skill_index_drift.py" docs/reference/agent_system_skills/registry/README.md
python governance/compat/check_assf_skill_index_drift.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

Expected results:

- worktree state is recorded before edits;
- candidate entry path is absent before worker implementation;
- package root is absent and must remain absent;
- ASSF contract search shows `riskTriggers` and required field families;
- registry README search shows add-entry flow and generator/drift commands;
- current generated index is in sync before the worker edits sources;
- pre-implementation gate passes or any allowed-scope failure is repaired and rerun.

Allowed-scope gate failures must be repaired and rerun. Escalate only if repair
would exceed Allowed scope, change the claim boundary, require live/provider
proof, touch forbidden paths, or alter commit mode.

## 6A. Source-Fidelity Pass

### Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| EXISTS: active session authorizes AGSK-T5 dispatch with AGSK-T4 prerequisite satisfied at `2a84036a` | `CVF_SESSION_MEMORY.md` | Next Allowed Move | AGSK-T5 first package-candidate registry instance | active session front door | VALUE_SET | ACCEPT |
| EXISTS: T5 roadmap opens `cvf-governance-external-absorption` candidate | `docs/roadmaps/CVF_AGSK_PACKAGE_CANDIDATE_TRIAGE_ROADMAP_2026-06-29.md` | Tranche AGSK-T5 | cvf-governance-external-absorption | AGSK package-candidate triage roadmap | EXISTS | ACCEPT |
| VALUE_SET: T5 status ceiling is `CANDIDATE` | `docs/roadmaps/CVF_AGSK_PACKAGE_CANDIDATE_TRIAGE_ROADMAP_2026-06-29.md` | Tranche AGSK-T5 acceptance criteria | CANDIDATE | AGSK-T5 roadmap tranche | VALUE_SET | ACCEPT |
| EXISTS: package contract required field families include Identity, Provenance, Purpose and trigger, Selectors, Capability, Risk and authority, Lifecycle, Composition, Internal disposition, External disposition, Platform | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema | Required field families | ASSF package contract | VALUE_SET | ACCEPT |
| EXISTS: contract includes `riskTriggers` in Purpose and trigger fields | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema and Risk And Lifecycle Fields | riskTriggers | ASSF package contract | EXISTS | ACCEPT |
| VALUE_SET: `riskTriggers` cannot raise authority beyond `authorityCeiling` or bypass `riskCeiling` | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Risk And Lifecycle Fields | riskTriggers | ASSF package contract | LITERAL_INVARIANT | ACCEPT |
| VALUE_SET: `externalCliMcpDisposition` allowed values include `DEFERRED_WITH_REASON` | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Internal-Agent And External-Agent CLI/MCP Disposition Fields | externalCliMcpDisposition | ASSF package contract | VALUE_SET | ACCEPT |
| EXISTS: registry README says entries are authoritative source files and generated index must not be hand-edited | `docs/reference/agent_system_skills/registry/README.md` | Purpose | entries; generated/skill-index.json | ASSF registry source family | LITERAL_INVARIANT | ACCEPT |
| VALUE_SET: adding an entry requires next `registryOrder`, status `CANDIDATE` or `PROPOSED`, generator run, and drift check | `docs/reference/agent_system_skills/registry/README.md` | Adding A New Entry | registryOrder; status; generate_assf_skill_index.py; check_assf_skill_index_drift.py | ASSF registry source family | VALUE_SET | ACCEPT |
| EXISTS: existing first registry entry uses `registryOrder=1` and `status=CANDIDATE` | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | top-level JSON fields | registryOrder; status | ASSF registry source entry | VALUE_SET | ACCEPT |
| EXISTS: existing second registry entry uses `registryOrder=2` and `status=CANDIDATE` | `docs/reference/agent_system_skills/registry/entries/cvf-worker-return-author.json` | top-level JSON fields | registryOrder; status | ASSF registry source entry | VALUE_SET | ACCEPT |
| VALUE_SET: generator strips `registryOrder`, sorts by `registryOrder` then `skillId`, and writes generated index | `governance/compat/generate_assf_skill_index.py` | module docstring and `build_index` | SOURCE_ONLY_FIELDS; build_index; generate_index | ASSF skill index generator | VALUE_SET | ACCEPT |
| EXISTS: drift checker validates generated index against current per-entry registry sources | `governance/compat/check_assf_skill_index_drift.py` | module docstring and `check` | check | ASSF skill index drift checker | EXISTS | ACCEPT |
| DOC_ONLY_NEW: new candidate source entry path | `docs/roadmaps/CVF_AGSK_PACKAGE_CANDIDATE_TRIAGE_ROADMAP_2026-06-29.md` | Tranche AGSK-T5 minimum outputs | docs/reference/agent_system_skills/registry/entries/cvf-governance-external-absorption.json | AGSK-T5 worker output | DOC_ONLY_NEW | ACCEPT |
| DOC_ONLY_NEW: worker return path | `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_T5_FIRST_EXTERNAL_ABSORPTION_PACKAGE_CANDIDATE_2026-06-29.md` | Allowed scope and Worker Return Packet Shape Contract | docs/reviews/CVF_AGSK_T5_FIRST_EXTERNAL_ABSORPTION_PACKAGE_CANDIDATE_WORKER_RETURN_2026-06-29.md | AGSK-T5 worker return | DOC_ONLY_NEW | ACCEPT |

### New Doc-Only Fields Table

| New doc-only field or file | Purpose | Not sourced from runtime? | Runtime claim blocked? | Validation expectation |
|---|---|---|---|---|
| `docs/reference/agent_system_skills/registry/entries/cvf-governance-external-absorption.json` | first AGSK-derived external-absorption registry candidate | Yes | Yes | JSON source validates by generator and drift checker; status remains `CANDIDATE` |
| generated index entry for `cvf-governance-external-absorption` | metadata-only aggregate projection from registry source | Yes | Yes | regenerated only by `generate_assf_skill_index.py --generate` |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`; `docs/reference/agent_system_skills/registry/README.md`; `docs/reference/agent_system_skills/registry/entries/`; `docs/reference/agent_system_skills/generated/skill-index.json`; `governance/compat/generate_assf_skill_index.py`; `governance/compat/check_assf_skill_index_drift.py` |
| Existing candidate entry check | `Test-Path docs/reference/agent_system_skills/registry/entries/cvf-governance-external-absorption.json` returned `False` at dispatch authoring |
| Existing package root check | `Test-Path docs/reference/agent_system_skills/packages` returned `False` at dispatch authoring |
| Existing registry order | current entries use `registryOrder` 1 and 2, so T5 must use 3 unless the worker finds a new pre-existing entry before edits |
| Generated index freshness | `python governance/compat/check_assf_skill_index_drift.py` returned PASS before dispatch authoring |
| Runtime behavior claimed | N/A_WITH_REASON: this work order creates metadata source and generated index only |
| Live/provider proof claimed | N/A_WITH_REASON: no live governance behavior, provider call, model/API behavior, or benchmark is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |
| Freshness disposition | PASS - current source supports a bounded registry-candidate tranche only |

### Negative Search And Collision Discipline

| Search target | Command or source | Result | Disposition |
|---|---|---|---|
| candidate source entry path | `Test-Path docs/reference/agent_system_skills/registry/entries/cvf-governance-external-absorption.json` | `False` before dispatch authoring | create as AGSK-T5 DOC_ONLY_NEW artifact |
| package root | `Test-Path docs/reference/agent_system_skills/packages` | `False` before dispatch authoring | remain absent; do not create package body |
| generated index drift | `python governance/compat/check_assf_skill_index_drift.py` | PASS before dispatch authoring | worker must keep PASS after generator run |

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
|---|---|
| Coverage index status | NOT_APPLICABLE_WITH_REASON |
| Canonical coverage index | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` |
| Reason | AGSK-T5 does not run a new legacy corpus scan or claim coverage-index closure; it consumes the already closed AGSK reabsorption review, EAVC value-conversion guard, and AGSK triage roadmap |
| Required worker evidence | cite the inherited AGSK reabsorption review manifest/ledger, this work order's source verification, and the generated ASSF registry/index proof |
| Future guard candidate | N/A with reason: AGSK-T6 checker candidate remains parked until AGSK-T5 closes and a concrete repeated defect or high-risk gap exists |

## 6B. Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| Author `cvf-governance-external-absorption` registry entry | Mission; Allowed scope; Execution Plan | `docs/reference/agent_system_skills/registry/entries/cvf-governance-external-absorption.json` | `Test-Path`; JSON parse; reviewer diff | PASS |
| Include all compact machine source schema field families | Source-Fidelity Pass; Acceptance Criteria | new registry JSON fields | contract cross-check and worker return field-family table | PASS |
| Include `riskTriggers` from post-T4 contract | Source-Fidelity Pass; Evidence Requirements | `riskTriggers` field in new JSON | `rg -n "riskTriggers" <new entry>` | PASS |
| Keep status ceiling `CANDIDATE` | Scope; Acceptance Criteria | `status` and `candidateState` values | JSON parse and reviewer check | PASS |
| Set external disposition to `DEFERRED_WITH_REASON` | Scope; Acceptance Criteria | `externalCliMcpDisposition` value | JSON parse and reviewer check | PASS |
| Use next registry order after existing entries | Source-Fidelity Pass | `registryOrder=3` unless collision found | source entry comparison | PASS |
| Regenerate generated skill index | Execution Plan | `docs/reference/agent_system_skills/generated/skill-index.json` | `python governance/compat/generate_assf_skill_index.py --generate` | PASS |
| Prove drift check passes | Evidence Requirements | drift checker output | `python governance/compat/check_assf_skill_index_drift.py` | PASS |
| Do not create package body, resolver, checker, runtime, provider/live, or public-sync claim | Forbidden scope; Claim Boundary | no forbidden paths changed | `git diff --name-status` and claim scan | PASS |

## 6C. Worker Autonomy / No-Question Rule

The worker proceeds without operator confirmation for allowed-scope reads,
registry JSON authoring, generator run, worker-return authoring, evidence-block
repairs, and gate reruns. The worker must repair allowed-scope gate failures
and rerun the failed gate before handoff.

Stop and return `BLOCKED_WITH_REASON` if remediation would touch forbidden
paths, create a package body, wire a checker, run live/provider proof,
public-sync, use secrets/quota, edit session state, promote lifecycle status,
or change the claim boundary.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake summary | AGSK triage opened T5 to create the first AGSK-derived external-absorption registry candidate |
| Scope classification | bounded documentation and metadata-only registry candidate |
| Risk sensitivity | low runtime risk, high governance precision value; no public, live, provider, secrets, or runtime behavior |
| Selected role route | `MULTI_AGENT_SINGLE_ROLE` |
| Role separation basis | no-commit worker authors bounded registry candidate and return; Codex reviewer/closer validates and commits if accepted |
| Escalation condition | any scope expansion into package body, runtime, resolver, checker, public-sync, session state, promotion, or provider/live proof |
| Dispatch status | ACCEPT |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | Codex dispatcher creates work order; worker performs no-commit registry candidate creation; Codex reviewer/closer decides acceptance and commit |
| phase | DISPATCH_AUTHORING -> EXECUTION -> CLOSURE -> SESSION_SYNC if next move changes |
| baseHeadFor(phase) | dispatchBaseHead=`3ce884c9`; executionBaseHead=worker captures with `git rev-parse --short HEAD`; closureBaseHead=reviewer captures from worker return |
| changedSetScope(phase) | worker may change only the registry candidate, generated index, and worker-return paths listed in Allowed scope |
| traceScope(phase, actor) | worker return must record commands, changed paths, generator result, drift check, gate results, source evidence, and claim boundary |
| commitOwner(phase) | `WORKER_MUST_NOT_COMMIT`; Codex reviewer/closer owns material commit if accepted |
| crossBatchIsolation | no AGSK-T6, runtime, checker, session-sync, CodeGraph, or unrelated batch work while this worker return is pending |
| nextMoveSurfaces | worker must not edit next-move surfaces |
| closer designation | Codex reviewer/closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_AGSK_T5_FIRST_EXTERNAL_ABSORPTION_PACKAGE_CANDIDATE_COMPLETION_2026-06-29.md` optional; create only if worker return cannot safely carry reviewer decision |
| workerReturnPath | `docs/reviews/CVF_AGSK_T5_FIRST_EXTERNAL_ABSORPTION_PACKAGE_CANDIDATE_WORKER_RETURN_2026-06-29.md` |
| reviewerOwnedClosurePaths | accepted registry entry, generated index, worker return reviewer decision, optional completion review only if needed, material commit, and later session-sync if next move changes |
| workerReturnDisposition | `COMPLETE_PENDING_REVIEW`, `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, or `BLOCKED_WITH_REASON` |
| reviewerCommitRule | reviewer may commit only after source-fidelity, claim boundary, changed-set scope, generator/drift proof, and gates pass |

## Forbidden Filesystem State Precheck

| Forbidden path | Expected state | Actual state at dispatch | Action if PRESENT |
|---|---|---|---|
| `docs/reference/agent_system_skills/packages/` | ABSENT | ABSENT | block T5 dispatch and ask for scope reconciliation |
| `docs/reference/agent_system_skills/registry/entries/cvf-governance-external-absorption.json` | ABSENT | ABSENT | block if pre-existing unowned artifact appears |
| `docs/reviews/CVF_AGSK_T5_FIRST_EXTERNAL_ABSORPTION_PACKAGE_CANDIDATE_WORKER_RETURN_2026-06-29.md` | ABSENT | ABSENT | block if pre-existing unowned artifact appears |

## Pre-Existing Dirty Path Exemptions

| Path | Status at dispatch | Exemption boundary |
|---|---|---|
| N/A with reason | clean worktree at dispatch authoring start | no dirty-path exemption |

## 7. Write Ownership

Owned files:

- `docs/reference/agent_system_skills/registry/entries/cvf-governance-external-absorption.json`
- `docs/reference/agent_system_skills/generated/skill-index.json`
- `docs/reviews/CVF_AGSK_T5_FIRST_EXTERNAL_ABSORPTION_PACKAGE_CANDIDATE_WORKER_RETURN_2026-06-29.md`

Forbidden paths:

- `docs/reference/agent_system_skills/packages/`
- `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`
- existing files under `docs/reference/agent_system_skills/registry/entries/` except mechanical generator-related correction if justified in worker return
- `governance/compat/`
- `.private_reference/`
- `CVF_SESSION/`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF*.md`

Write mode: create one new registry entry, regenerate the generated index, create one worker return. Do not commit.

## 8. Execution Plan

1. Capture `executionBaseHead`, `git status --short`, and pre-flight checks.
2. Read the required first-read files and source-verify the field families,
   registry add flow, generator behavior, and drift checker behavior.
3. Create `docs/reference/agent_system_skills/registry/entries/cvf-governance-external-absorption.json` with `registryOrder=3`, `status=CANDIDATE`, `candidateState=CANDIDATE`, `riskTriggers`, and `externalCliMcpDisposition=DEFERRED_WITH_REASON`.
4. Use source-backed external absorption references for `sourceArtifacts`,
   `reviewArtifacts`, `purpose`, `triggerPatterns`, `inputs`, `outputs`,
   `executionConstraints`, `acceptanceEvidence`, `riskProfile`,
   `authorityCeiling`, `safeStop`, and `capabilityBoundary`.
5. Run `python governance/compat/generate_assf_skill_index.py --generate`.
6. Run `python governance/compat/check_assf_skill_index_drift.py`.
7. Create the worker return at the owned path and include required evidence,
   source verification, field-family coverage, generator/drift proof, and
   claim boundary.
8. Run `python governance/compat/run_worker_return_fast_gate.py`.
9. Run `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast --parallel --max-workers 6` or record an allowed-scope blocker and direct repaired rerun.
10. Return without committing.

Stop condition for every step: if evidence contradicts the planned candidate,
or required remediation exceeds Allowed scope, return `BLOCKED_WITH_REASON`.

## 8A. Design Control Carry-Forward

| Design control | Roadmap source | Work-order handling | Verdict |
|---|---|---|---|
| Scope boundary | triage roadmap Non-Goals and T5 tranche | only one registry source entry, generated index, and worker return allowed | PASS |
| Non-goals | triage roadmap Non-Goals | package body, runtime, resolver, checker, public, provider, session-sync, and promotion all forbidden | PASS |
| Lane split | triage roadmap Work Plan | executes AGSK-T5 only; AGSK-T6 remains parked | PASS |
| Dependency/source-verification plan | triage roadmap Source Evidence | T4 closed; source checks required before build | PASS |
| Claim boundary | triage roadmap Claim Boundary | metadata-only candidate; no runtime/package activation | PASS |
| Acceptance criteria | triage roadmap AGSK-T5 criteria | mapped in trace matrix and evidence requirements | PASS |
| Verification/evidence | triage roadmap Verification | generator, drift checker, gates, and searches listed | PASS |
| Dispatch-readiness decision | triage roadmap Authorization Boundary plus active session next move | T5 is authorized because T4 is closed at material commit `2a84036a` | PASS |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | ASSF registry metadata entry and generated skill index | CANDIDATE metadata only; no resolver activation, no package body, no commit authority | ASSF contract, registry README, generator, drift checker, T5 worker output | internal metadata-only surface; no loader behavior changed | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future CLI/MCP adapter projection, not implemented in T5 | no external ingress, authentication, mutation, receipt, or public boundary is implemented | ASSF external disposition fields and dual-agent standard | adapter deferred to separate source-verified work order | `DEFERRED_WITH_REASON` |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher |
| Provider or surface | Codex local workspace |
| Session or invocation | AGSK-T5 work order authoring, 2026-06-29 |
| Working directory | repository root |
| Command or tool surface | source reads, ADIF resolver import, rg searches, apply_patch |
| Target paths | this work order |
| Allowed scope source | operator requested next tranche work order; active session records AGSK-T4 closed at `2a84036a` and AGSK-T5 as next allowed move |
| Before status evidence | clean worktree at HEAD `3ce884c9` |
| After status evidence | dispatch-ready work order pending gate/commit |
| Diff evidence | `git diff --name-status`; `git status --short` before commit |
| Approval boundary | dispatch authoring only; no AGSK-T5 execution by dispatcher |
| Claim boundary | repo-local trace only; no runtime/provider/public claim |
| Agent type | dispatcher |
| Invocation ID | `agsk-t5-first-external-absorption-package-candidate-work-order-2026-06-29` |
| Expected manifest | N/A with reason: dispatch work order defines future worker/reviewer scope; exact implementation manifest is required in the worker return and reviewer closure |
| Actual changed set | N/A with reason: dispatch authoring changes only this work-order artifact before execution starts |
| Manifest delta | N/A with reason: no implementation manifest is being closed by this dispatch artifact |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Durable files changed by worker | one new ASSF registry entry, one regenerated index, and one worker-return review artifact |
| Canonical package root | N/A with reason: AGSK-T5 must not create a package root or `SKILL.md` |
| Generated index or aggregate | `docs/reference/agent_system_skills/generated/skill-index.json` must be generated by `generate_assf_skill_index.py --generate` |
| Storage migration | N/A with reason: no file relocation or storage migration is authorized |
| New reference-family folders | N/A with reason: no new folder is authorized |
| Layout risk | bounded registry-candidate metadata only; T6 checker and runtime lanes remain separate governed work |

## 8C. Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: After AGSK-T4, the ASSF contract can support one
external-absorption registry candidate that consumes `riskTriggers`, remains
`CANDIDATE`, and keeps external CLI/MCP disposition deferred.

Evidence Comparison Requirement: worker return must compare actual registry
JSON, generated index, and drift checker result against the prediction.

Contradiction Handling Requirement: if the contract, registry README, generator,
or existing entries contradict the planned shape, worker must stop or narrow the
candidate rather than inventing fields.

Claim Update Requirement: worker return records whether the claim was confirmed,
revised, narrowed, or invalidated.

## Evidence Requirements

Required evidence:

- `executionBaseHead` and `git status --short` before edits.
- `git diff --name-status` showing only owned paths.
- JSON parse or equivalent validation of the new registry entry.
- `rg -n "riskTriggers|CANDIDATE|DEFERRED_WITH_REASON" docs/reference/agent_system_skills/registry/entries/cvf-governance-external-absorption.json`.
- `python governance/compat/generate_assf_skill_index.py --generate` result.
- `python governance/compat/check_assf_skill_index_drift.py` result.
- `rg -n "cvf-governance-external-absorption" docs/reference/agent_system_skills/generated/skill-index.json`.
- worker return fast gate result.
- reviewer-fast hook result or classified failure.
- clear statement that HEAD is unchanged by worker.

Base-anchor evidence:

| Field | Required value |
|---|---|
| dispatchBaseHead | `3ce884c9` |
| executionBaseHead | worker captures before edits |
| closureBaseHead | reviewer captures from worker return |
| Commit mode | `WORKER_MUST_NOT_COMMIT` |

## 10. Acceptance Criteria

| Criterion | Evidence |
|---|---|
| new registry source entry exists at the planned path | `Test-Path`; diff |
| `skillId` equals `cvf-governance-external-absorption` | JSON parse or `rg` |
| `registryOrder` equals 3 unless a pre-existing collision is discovered and documented | source entry comparison |
| `status` and `candidateState` equal `CANDIDATE` | JSON parse or `rg` |
| new entry includes all required ASSF compact machine source field families | worker return field-family coverage table |
| new entry includes `riskTriggers` and does not use it to raise authority beyond `authorityCeiling` or bypass `riskCeiling` | JSON parse and worker return |
| `externalCliMcpDisposition` equals `DEFERRED_WITH_REASON` | JSON parse or `rg` |
| generated skill index includes the new skill and excludes source-only `registryOrder` from aggregate skill objects | generated index review |
| drift checker passes after generation | drift checker command |
| no package root, checker, runtime, resolver, session, legacy, provider, live, or public-sync paths changed | `git diff --name-status` |
| worker makes no commit | `git status --short` and HEAD unchanged |

Fail conditions:

| Fail condition | Required action |
|---|---|
| worker creates package root, `SKILL.md`, resolver, checker, session edit, or public-sync artifact | return `BLOCKED_WITH_REASON`; reviewer rejects scope |
| worker sets lifecycle above `CANDIDATE` or claims package activation | return `BLOCKED_WITH_REASON` |
| generated index is hand-edited without generator run | return `BLOCKED_WITH_REASON` |
| source verification cannot trace required field families to ASSF contract | return `BLOCKED_WITH_REASON` |
| drift checker fails and cannot be repaired inside Allowed scope | return `BLOCKED_WITH_REASON` |
| any runtime/provider/live/public claim is introduced | return `BLOCKED_WITH_REASON` |

## 11. Review Gate

Implementation may proceed only after:

- this dispatch work order exists and passes pre-dispatch/dispatch-quality gates;
- worker captures `executionBaseHead`;
- worker runs pre-implementation autorun on a real base.

Closure may proceed only after:

- reviewer verifies changed-set scope;
- reviewer verifies source-fidelity, JSON shape, generator use, drift proof, and claim-boundary evidence;
- relevant gates pass on the accepted range;
- reviewer commits accepted material if disposition is pass.

No-commit worker return should run:

```powershell
python governance/compat/run_worker_return_fast_gate.py
```

Reviewer validation should use:

```powershell
python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return --base <closureBaseHead> --head HEAD --enforce
```

## 12. Worker Return Packet Shape Contract

Path:

`docs/reviews/CVF_AGSK_T5_FIRST_EXTERNAL_ABSORPTION_PACKAGE_CANDIDATE_WORKER_RETURN_2026-06-29.md`

Required sections:

- Purpose
- Target
- Scope / Methodology
- Findings / Position
- Risk / Corrective Action
- Worker Status
- Source Inventory
- Source Verification Block
- Roadmap-To-Work-Order Trace Matrix
- Current Runtime Freshness Verification
- Registry Field-Family Coverage
- Generated Index Drift Proof
- Corpus Completeness And Report Integrity
- External Knowledge Intake Routing
- Rescan Intelligence Hardening
- Finding-To-Governance Learning Disposition
- Epistemic Process Block
- Delta Execution Claim Boundary Control Block
- Agent Operation Trace Block
- Machine Closure Package
- Public Export Disposition
- Claim Boundary

Required status token: `COMPLETE_PENDING_REVIEW`,
`COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, or `BLOCKED_WITH_REASON`.

The worker return must record `executionBaseHead`, `git status --short`, actual
changed paths, generator and drift-check commands/results, gate commands/results,
and a `dispatchWorkOrder:` line citing this work order. Conditional sections
that do not apply must remain present with `N/A with reason` or
`NOT_APPLICABLE_WITH_REASON`; do not omit them.

## Work-Order Fulfillment Manifest

| Required output | Path or evidence | Owner | Status |
|---|---|---|---|
| Registry candidate | `docs/reference/agent_system_skills/registry/entries/cvf-governance-external-absorption.json` | worker | REQUIRED |
| Generated index | `docs/reference/agent_system_skills/generated/skill-index.json` | worker via generator | REQUIRED |
| Worker return | `docs/reviews/CVF_AGSK_T5_FIRST_EXTERNAL_ABSORPTION_PACKAGE_CANDIDATE_WORKER_RETURN_2026-06-29.md` | worker | REQUIRED |
| Material commit | accepted registry candidate, generated index, and worker return committed by reviewer only | reviewer | PENDING_REVIEW |
| Session sync | only after material acceptance if next move changes | reviewer | PENDING_REVIEW |

## Required Proof Manifest

| Proof | Path | Required literal | Required at handoff |
|---|---|---|---|
| Dispatch status | `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_T5_FIRST_EXTERNAL_ABSORPTION_PACKAGE_CANDIDATE_2026-06-29.md` | `DISPATCH_READY` | Yes |
| Commit mode | `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_T5_FIRST_EXTERNAL_ABSORPTION_PACKAGE_CANDIDATE_2026-06-29.md` | `WORKER_MUST_NOT_COMMIT` | Yes |
| Candidate ID | `docs/reference/agent_system_skills/registry/entries/cvf-governance-external-absorption.json` | `cvf-governance-external-absorption` | Yes |
| Status ceiling | `docs/reference/agent_system_skills/registry/entries/cvf-governance-external-absorption.json` | `CANDIDATE` | Yes |
| External boundary | `docs/reference/agent_system_skills/registry/entries/cvf-governance-external-absorption.json` | `DEFERRED_WITH_REASON` | Yes |
| Drift proof | `governance/compat/check_assf_skill_index_drift.py` | `PASS - skill index is in sync with registry entry sources.` | Yes |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | `.private_reference/legacy/CVF 28.06/CVF_Agent_Skills_Governance_Absorption_Pack`; inherited source review: `docs/reviews/CVF_AGSK_ABSORPTION_PACK_REABSORPTION_REVIEW_2026-06-29.md` |
| Enumeration command | inherited from source review: `Get-ChildItem -Recurse -File ".private_reference\legacy\CVF 28.06\CVF_Agent_Skills_Governance_Absorption_Pack"` |
| Manifest artifact or inline manifest | `docs/reviews/CVF_AGSK_ABSORPTION_PACK_REABSORPTION_REVIEW_2026-06-29.md` section `## Corpus Manifest` |
| Processing ledger artifact or inline ledger | `docs/reviews/CVF_AGSK_ABSORPTION_PACK_REABSORPTION_REVIEW_2026-06-29.md` section `## Processing Ledger` |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | `docs/reviews/CVF_AGSK_ABSORPTION_PACK_REABSORPTION_REVIEW_2026-06-29.md` section `## Owner-Surface Map`; T5 target owner surfaces are `docs/reference/agent_system_skills/registry/entries/` and `docs/reference/agent_system_skills/generated/skill-index.json` |
| Unresolved items | 0 unresolved in inherited review; T5 resolves one package-candidate opportunity |
| Completion claim boundary | work-order dispatch only; no new corpus sweep, runtime, provider, package activation, public-sync, or production claim |

## Mandatory Blind-Spot Control Block

| Gate | Evidence |
|---|---|
| Gate 1: absorption source enumerated | inherited from `docs/reviews/CVF_AGSK_ABSORPTION_PACK_REABSORPTION_REVIEW_2026-06-29.md` |
| Gate 2: all files listed | inherited source review lists 29 files |
| Gate 3: each file has terminal status | inherited source review processing ledger has terminal rows |
| Gate 4: reconciliation passes | inherited source review reports manifest=29, ledger_terminal=29, unresolved=0 |
| Gate 5: adapted/deferred items traced | T5 traces one package-candidate opportunity to ASSF registry source layout |
| Blind-spot verdict | CLEAR_FOR_T5_DISPATCH_WITH_INHERITED_CORPUS_REVIEW |

## Corpus Completeness And Report Integrity

- Corpus task class: WORK_ORDER_FOR_PRIOR_COMPLETE_ABSORPTION_TRIAGE
- Corpus root: `.private_reference/legacy/CVF 28.06/CVF_Agent_Skills_Governance_Absorption_Pack`
- Snapshot time: inherited from AGSK reabsorption review
- Enumeration command: inherited filesystem-backed `Get-ChildItem -Recurse -File ".private_reference\legacy\CVF 28.06\CVF_Agent_Skills_Governance_Absorption_Pack"`
- Manifest artifact or inline manifest: `docs/reviews/CVF_AGSK_ABSORPTION_PACK_REABSORPTION_REVIEW_2026-06-29.md` section `## Corpus Manifest`
- Manifest hash: inherited hash prefix `249dc5bf1200dbdc`
- Processing ledger artifact or inline ledger: `docs/reviews/CVF_AGSK_ABSORPTION_PACK_REABSORPTION_REVIEW_2026-06-29.md` section `## Processing Ledger`
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE
- Reconciliation: manifest=29; ledger_terminal=29; exclusions=0; unresolved=0
- Unresolved files: 0
- Declared exclusions: none
- Unreadable or unsupported files: none
- Aggregation check: source review reports 8 ADAPTED + 16 NO_NEW_VALUE + 2 DEFERRED + 3 REJECTED = 29
- Drift check: this work order does not re-enumerate the corpus; it consumes the closed review and roadmap triage
- Output traceability: T5 maps one package-candidate opportunity to the ASSF registry source layout and generated index
- Adversarial verification: T5 must create metadata-only candidate entry and must not claim runtime activation, package body, resolver behavior, or external adapter support
- Corpus verdict: PARTIAL - work-order dispatch based on prior COMPLETE_VERIFIED review; no new corpus completeness claim is made here

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | legacy source family |
| Chain map route | legacy source family -> AGSK reabsorption review -> AGSK package-candidate triage -> ASSF registry candidate -> reviewer closure |
| Matching local-view guard | `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py` |
| Owner surface | `docs/reference/agent_system_skills/registry/entries/cvf-governance-external-absorption.json`; `docs/reference/agent_system_skills/generated/skill-index.json` |
| Disposition | ADAPT one external-absorption package-candidate concept into CVF ASSF registry metadata |
| Claim boundary | documentation and metadata-only work order; no runtime, provider, package activation, checker, public-sync, or production claim |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| AGSK advisory doctrine already absorbed | skill anatomy, anti-rationalization, progressive-disclosure, persona-boundary, and evidence-receipt patterns | DOCTRINE_ADAPTED | `docs/reference/agent_system_skills/CVF_AGSG_AGENT_SKILLS_ASSF_CAPABILITY_ANATOMY_AND_RATIONALIZATION_ADVISORY.md` | none in T5 | documentation-only doctrine; no runtime or package activation |
| `cvf-governance-external-absorption` candidate concept | external absorption governance capability as a CVF-owned skill candidate | PACKAGE_CANDIDATE | `docs/reference/agent_system_skills/registry/entries/cvf-governance-external-absorption.json`; `docs/reference/agent_system_skills/generated/skill-index.json` | Execute AGSK-T5 registry candidate creation | CANDIDATE metadata only; no resolver activation, provider call, CLI/MCP adapter, or runtime behavior |
| AGSK-T4 `riskTriggers` contract field | pattern-level risk escalation metadata | PACKAGE_CANDIDATE | new registry entry field | consume in candidate metadata | no enforcement until separate checker or resolver tranche |
| Future package anatomy checker | possible package field-shape checker | CHECKER_CANDIDATE | future `governance/compat` work order | parked until T5 closes and concrete defect exists | no checker wiring in T5 |
| Activation resolver states | possible runtime selection behavior | RUNTIME_CANDIDATE | future runtime/resolver work order | parked | no runtime in T5 |
| Pack-internal Python checkers | direct import rejected | REJECT_DIRECT_IMPORT | AGSK reabsorption review rejected ledger | none | no direct import |
| README and tree inventory value | no package/runtime/checker delta for T5 | NO_PACKAGE_OR_RUNTIME_VALUE | source review provenance | none | no runtime/package/checker action |

## Finding-To-Governance Learning Disposition

| Field | Required worker value |
|---|---|
| Defect class | `VALUE_CONVERSION_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Disposition | `PACKAGE_CANDIDATE_CREATED_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| Runtime/provider/cost lane | `N/A_WITH_REASON` |
| Next control action | state that AGSK-T6 checker remains parked unless T5 demonstrates a concrete repeated defect or high-risk gap |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | AGSK-T5 documentation and metadata-only ASSF registry candidate creation |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT - worker must provide source searches, generator result, drift check, gate results, and changed-set evidence |
| actionEvidence | ACTION_EVIDENCE_PRESENT - worker must provide registry JSON, generated index, and source-verification evidence |
| invocationBoundary | governed local documentation and metadata editing only |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | create one `CANDIDATE` registry source entry and regenerate metadata-only index |
| forbiddenExpansion | no package body, `SKILL.md`, resolver, checker, runtime, provider/live proof, public-sync, session sync, package activation, lifecycle promotion, or production claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this work order cites private provenance paths under
`.private_reference/legacy/`. Public-safe publication requires separate
redaction and public-sync authorization.

## Closure Checklist

| Checklist item | Required disposition |
|---|---|
| Acceptance criteria satisfied | reviewer verifies after worker return |
| Required evidence commands run | worker records command/result/path evidence |
| Commit mode recorded | `WORKER_MUST_NOT_COMMIT` |
| Changed files inside Allowed scope | reviewer verifies with `git diff --name-status` |
| Generator used | worker records command/result evidence |
| Drift checker passes | worker records PASS or blocker |
| Worker return fast gate | worker runs or records blocker |
| Reviewer-fast gate | worker runs or records blocker; reviewer reruns before commit |
| Public export disposition | `DEFERRED_PRIVATE_ONLY` |
| Session continuity | reviewer-owned after material commit if next move changes |

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` without continuing if:

- pre-implementation autorun fails outside Allowed scope;
- the ASSF contract, registry README, generator, drift checker, or AGSK source evidence cannot be read;
- source verification contradicts the planned registry-candidate shape;
- the patch would require package root, checker, resolver, runtime, provider/live, public-sync, session-state, or existing contract changes;
- any required gate cannot be repaired inside Allowed scope.

## Operator Checkpoint

N/A with reason: operator already approved moving from AGSK-T4 closure into the
next work order. No extra checkpoint is required for the bounded T5
documentation and metadata-only registry candidate. Operator approval is
required only for scope expansion listed in Return-To-Orchestrator Conditions.

## Claim Boundary

This work order authorizes only a no-commit worker-return lane for one
metadata-only ASSF registry candidate and regenerated skill index. It does not
authorize AGSK-T6 checker work, package body creation, resolver mutation,
runtime activation, automatic skill invocation, CLI/MCP adapter implementation,
provider/live proof, public-sync, session-sync, lifecycle promotion, production
readiness, or worker commit.
