# CVF Agent Work Order - AGSK-T7 Package Candidate Expansion From Source Pack

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-29

docType: work_order

Batch ID: AGSK-T7

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: e4526436

## Dispatch Prompt Envelope

Role: no-commit worker for AGSK-T7 metadata-only ASSF package-candidate
expansion; Codex remains reviewer/closer.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_T7_PACKAGE_CANDIDATE_EXPANSION_FROM_SOURCE_PACK_2026-06-29.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

Base: executionBaseHead must be captured with `git rev-parse --short HEAD`
before edits.

Current-time notes: current date is 2026-06-29. AGSK-T4 closed the
`riskTriggers` contract field at commit `2a84036a`; AGSK-T5 closed the first
AGSK-derived registry candidate at commit `a00f7cf5`. No runtime activation,
resolver mutation, package body, `SKILL.md`, checker wiring, provider call,
public-sync, session-sync, or lifecycle promotion is authorized.

Do-not-misread notes: execute AGSK-T7 only. This tranche converts concrete,
source-backed AGSK capability concepts into ASSF registry metadata candidates.
Do not claim that a candidate is active or usable as an executed skill. Do not
stop at a scan report; create the candidate entries unless source verification
blocks a specific candidate.

Required first actions: read this work order, AGSK reabsorption review, AGSK
package-candidate triage roadmap, AGSK-T4 and AGSK-T5 worker returns, ASSF
package contract, registry README, existing registry entries, generator, drift
checker, active session front door/state/handoff, guard orientation, and
literal-format gotchas; then capture `git status --short` and run
pre-implementation autorun.

Return contract: return `COMPLETE_PENDING_REVIEW`,
`COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, or `BLOCKED_WITH_REASON` with
changed paths, executionBaseHead, gate results, source-verification evidence,
candidate coverage, generated-index drift proof, and HEAD unchanged.

## Purpose

Close the second-pass AGSK blind-spot risk: prior AGSK work absorbed doctrine
and one external-absorption candidate, but did not convert the source pack's
concrete capability inventory into CVF-owned ASSF registry candidates.

AGSK-T7 creates a bounded set of additional `CANDIDATE` registry entries so CVF
gains practical skill/capability inventory while preserving the metadata-only
ASSF boundary.

## 1. Mission

Create source-backed ASSF registry entries for the following AGSK-derived
capability candidates:

| Candidate ID | Source-backed value |
|---|---|
| `cvf-engineering-spec-driven-development` | spec-to-work-order and procedure discipline around engineering tasks |
| `cvf-engineering-planning-task-breakdown` | activation resolver example and task decomposition candidate |
| `cvf-governance-anti-rationalization-guard` | stop/escalation signals against shortcut claims |
| `cvf-governance-context-packet-builder` | scoped context packet construction and contamination control |
| `cvf-governance-evidence-receipt-review-freeze` | skill receipt, review gate receipt, and freeze condition discipline |
| `cvf-governance-persona-skill-boundary-review` | persona/command/skill boundary review for multi-agent scope control |

Each candidate must stay at `status = CANDIDATE` and
`candidateState = CANDIDATE`. The worker may narrow or omit a candidate only
when source verification proves the value is insufficient; any omission must be
recorded in the worker return with source-backed reason.

## 2. Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Operator instruction | chat request on 2026-06-29 to return to `CVF_Agent_Skills_Governance_Absorption_Pack` because blind spots may remain | authorizes AGSK second-pass package-candidate expansion |
| Active session front door | `CVF_SESSION_MEMORY.md` | session startup and governed-work routing source |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | active generated session state |
| Active handoff | `AGENT_HANDOFF_V27_2026-06-29.md` | active handoff named by state registry |
| AGSK source review | `docs/reviews/CVF_AGSK_ABSORPTION_PACK_REABSORPTION_REVIEW_2026-06-29.md` | 29-file corpus review and value-conversion source |
| AGSK triage roadmap | `docs/roadmaps/CVF_AGSK_PACKAGE_CANDIDATE_TRIAGE_ROADMAP_2026-06-29.md` | permits additional AGSK/external-absorption skill candidates after T5 closes |
| AGSK-T4 closure | `docs/reviews/CVF_AGSK_T4_ASSF_RISK_TRIGGERS_FIELD_PATCH_WORKER_RETURN_2026-06-29.md`; commit `2a84036a` | `riskTriggers` field is available |
| AGSK-T5 closure | `docs/reviews/CVF_AGSK_T5_FIRST_EXTERNAL_ABSORPTION_PACKAGE_CANDIDATE_WORKER_RETURN_2026-06-29.md`; commit `a00f7cf5` | first candidate proved registry/index path |
| ASSF package contract | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | required field families and lifecycle ceiling |
| ASSF registry source layout | `docs/reference/agent_system_skills/registry/README.md` | adding entries, generator, drift check |
| Existing registry entries | `docs/reference/agent_system_skills/registry/entries/` | current entry shape and next `registryOrder` |

Authority boundary:

- External AGSK files are evidence input only. The worker must rewrite value
  into CVF-owned ASSF metadata.
- The registry source family is metadata-only and not a package root.
- Any runtime, resolver, checker, provider, public, session-sync, or package
  activation step requires a separate governed work order.

## 3. Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | authors this source-verified work order |
| Worker | assigned no-commit worker agent | creates candidate entries, regenerates index, returns evidence |
| Reviewer/closer | Codex | validates source fidelity, generated index, gates, and commits if accepted |
| Operator approval required | operator | any expansion beyond metadata-only candidate entries |

## 4. Scope

Allowed scope:

- create candidate JSON files under
  `docs/reference/agent_system_skills/registry/entries/`;
- regenerate `docs/reference/agent_system_skills/generated/skill-index.json`
  using `python governance/compat/generate_assf_skill_index.py --generate`;
- create
  `docs/reviews/CVF_AGSK_T7_PACKAGE_CANDIDATE_EXPANSION_FROM_SOURCE_PACK_WORKER_RETURN_2026-06-29.md`;
- run read-only source searches, JSON validation, drift checks, resolver smoke
  checks, worker-return fast gate, and reviewer-fast gate;
- repair allowed-scope documentation or JSON formatting defects.

Forbidden scope:

- creating `docs/reference/agent_system_skills/packages/` or any `SKILL.md`;
- promoting any entry above `CANDIDATE` or setting `certificationState` above
  `NOT_STARTED`;
- editing existing candidate entries except to repair a generator-detected
  mechanical collision with explicit worker-return evidence;
- editing `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`;
- editing `governance/compat/*.py`, hooks, tests, generators, or checkers;
- editing `.private_reference/legacy/` or external source contents;
- editing `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, or handoff files;
- claiming runtime behavior, resolver activation, package execution,
  provider/live proof, production readiness, public readiness, or public-sync.

Risk ceiling: R0 documentation and metadata-only registry candidate expansion.

## Scope / Target / Owner Boundary

Target: additional ASSF registry source entries, regenerated metadata-only skill
index, and one worker-return artifact.

Owner boundary:

- worker owns only allowed-scope files;
- Codex owns reviewer closure and commits after acceptance;
- session-sync is reviewer-owned only after material closure, if next move
  changes;
- operator approval is required for any expansion beyond AGSK-T7.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch-authoring`, role=`dispatcher`,
lifecyclePhase=`pre-dispatch`, surfaceSelector=`docs/work_orders`,
riskCeiling=`HIGH`, maxResults=`20`

Returned defects: NONE_RETURNED

Disclosure note: resolver was invoked through `resolve_defect_packet(...)` from
`governance/compat/run_adif_defect_resolver.py`; it returned
`totalCandidates=0`.

## 5. Required First Reads

Before editing, read:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V27_2026-06-29.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- this work order
- `docs/reviews/CVF_AGSK_ABSORPTION_PACK_REABSORPTION_REVIEW_2026-06-29.md`
- `docs/roadmaps/CVF_AGSK_PACKAGE_CANDIDATE_TRIAGE_ROADMAP_2026-06-29.md`
- `docs/reviews/CVF_AGSK_T4_ASSF_RISK_TRIGGERS_FIELD_PATCH_WORKER_RETURN_2026-06-29.md`
- `docs/reviews/CVF_AGSK_T5_FIRST_EXTERNAL_ABSORPTION_PACKAGE_CANDIDATE_WORKER_RETURN_2026-06-29.md`
- `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`
- `docs/reference/agent_system_skills/registry/README.md`
- every existing JSON file under
  `docs/reference/agent_system_skills/registry/entries/`
- `governance/compat/generate_assf_skill_index.py`
- `governance/compat/check_assf_skill_index_drift.py`
- the source AGSK files cited in this work order's Source Verification Block.

## 6. Pre-Flight Checks

Run before implementation:

```powershell
git rev-parse --short HEAD
git status --short
Get-ChildItem docs/reference/agent_system_skills/registry/entries -File | Select-Object -ExpandProperty Name
python governance/compat/check_assf_skill_index_drift.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
rg -n "cvf\\.engineering|cvf\\.governance|cvf\\.review|spec_driven|planning_task|anti_rationalization|context_packet|receipt|persona" ".private_reference/legacy/CVF 28.06/CVF_Agent_Skills_Governance_Absorption_Pack"
```

Expected results:

- worktree state is recorded before edits;
- existing registry entries are visible and determine the next registry order;
- generated index is in sync before edits;
- pre-implementation autorun passes or allowed-scope failures are repaired;
- source search shows the candidate concepts listed in this work order.

## 6A. Source-Fidelity Pass

### Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| EXISTS: AGSK source review recorded `sample_capability_manifest.json` as a package-candidate gap | `docs/reviews/CVF_AGSK_ABSORPTION_PACK_REABSORPTION_REVIEW_2026-06-29.md` | Processing Ledger and Value Conversion Matrix | sample_capability_manifest.json | AGSK reabsorption review | EXISTS | ACCEPT |
| EXISTS: AGSK triage roadmap permits additional AGSK/external-absorption candidates after T5 | `docs/roadmaps/CVF_AGSK_PACKAGE_CANDIDATE_TRIAGE_ROADMAP_2026-06-29.md` | Open / Parked Follow-Ups | Additional AGSK/external-absorption skill candidates | AGSK triage roadmap | EXISTS | ACCEPT |
| VALUE_SET: status ceiling is metadata-only `CANDIDATE` | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Package lifecycle states | CANDIDATE | ASSF package contract | VALUE_SET | ACCEPT |
| EXISTS: registry source files are authoritative and generated index must not be hand-edited | `docs/reference/agent_system_skills/registry/README.md` | Purpose; Adding A New Entry | entries; generated skill index | ASSF registry source family | LITERAL_INVARIANT | ACCEPT |
| VALUE_SET: new entries must use next `registryOrder`, `CANDIDATE` or `PROPOSED`, generator, and drift check | `docs/reference/agent_system_skills/registry/README.md` | Adding A New Entry | registryOrder; status; generator; drift checker | ASSF registry source family | VALUE_SET | ACCEPT |
| EXISTS: existing AGSK candidate used `registryOrder=3` and status `CANDIDATE` | `docs/reference/agent_system_skills/registry/entries/cvf-governance-external-absorption.json` | top-level JSON fields | registryOrder; status | ASSF registry source entry | VALUE_SET | ACCEPT |
| EXISTS: source pack names `cvf.engineering.spec_driven_development` | `.private_reference/legacy/CVF 28.06/CVF_Agent_Skills_Governance_Absorption_Pack/docs/reference/CVF_AGENT_SKILL_CAPABILITY_STANDARD_2026-06-28.md` | example identifiers | cvf.engineering.spec_driven_development | AGSK evidence input | EXISTS | ACCEPT |
| EXISTS: source pack names `cvf.engineering.planning_task_breakdown` and activation resolver example | `.private_reference/legacy/CVF 28.06/CVF_Agent_Skills_Governance_Absorption_Pack/docs/reference/CVF_AGENT_SKILL_CAPABILITY_STANDARD_2026-06-28.md`; `.private_reference/legacy/CVF 28.06/CVF_Agent_Skills_Governance_Absorption_Pack/docs/absorptions/agent-skills-governance/05_SKILL_ACTIVATION_RESOLVER.md` | example identifiers; activation decision sample | cvf.engineering.planning_task_breakdown | AGSK evidence input | EXISTS | ACCEPT |
| EXISTS: anti-rationalization guard source defines signal and required disposition concepts | `.private_reference/legacy/CVF 28.06/CVF_Agent_Skills_Governance_Absorption_Pack/docs/absorptions/agent-skills-governance/06_ANTI_RATIONALIZATION_GUARD.md`; `.private_reference/legacy/CVF 28.06/CVF_Agent_Skills_Governance_Absorption_Pack/docs/reference/CVF_ANTI_RATIONALIZATION_GUARD_2026-06-28.md` | Guard logic; common signals | anti_rationalization_guard | AGSK evidence input | EXISTS | ACCEPT |
| EXISTS: context packet source defines structure and required receipt link | `.private_reference/legacy/CVF 28.06/CVF_Agent_Skills_Governance_Absorption_Pack/docs/absorptions/agent-skills-governance/08_CONTEXT_PACKET_STANDARD.md` | Context packet structure; Required receipt link | context_packet | AGSK evidence input | EXISTS | ACCEPT |
| EXISTS: evidence receipt source defines skill receipt and review gate receipt fields | `.private_reference/legacy/CVF 28.06/CVF_Agent_Skills_Governance_Absorption_Pack/docs/absorptions/agent-skills-governance/10_VERIFICATION_AND_EVIDENCE_RECEIPT.md` | Required receipt fields; Review gate receipt | skill receipt; review gate receipt | AGSK evidence input | EXISTS | ACCEPT |
| EXISTS: persona boundary source forbids persona spawning and preserves CVF-owned orchestration | `.private_reference/legacy/CVF 28.06/CVF_Agent_Skills_Governance_Absorption_Pack/docs/absorptions/agent-skills-governance/07_PERSONA_ORCHESTRATION_BOUNDARY.md` | Allowed; Forbidden; Merge rule | persona boundary | AGSK evidence input | EXISTS | ACCEPT |
| DOC_ONLY_NEW: AGSK-T7 candidate registry entries | `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_T7_PACKAGE_CANDIDATE_EXPANSION_FROM_SOURCE_PACK_2026-06-29.md` | Mission | candidate JSON entry paths | AGSK-T7 worker output | DOC_ONLY_NEW | ACCEPT |
| DOC_ONLY_NEW: AGSK-T7 worker return path | `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_T7_PACKAGE_CANDIDATE_EXPANSION_FROM_SOURCE_PACK_2026-06-29.md` | Worker Return Packet Shape Contract | docs/reviews/CVF_AGSK_T7_PACKAGE_CANDIDATE_EXPANSION_FROM_SOURCE_PACK_WORKER_RETURN_2026-06-29.md | AGSK-T7 worker return | DOC_ONLY_NEW | ACCEPT |

### New Doc-Only Fields Table

| New doc-only field or file | Purpose | Not sourced from runtime? | Runtime claim blocked? | Validation expectation |
|---|---|---|---|---|
| additional registry entry JSON files | metadata-only candidate inventory from source-backed AGSK capability concepts | Yes | Yes | JSON parse, generator run, drift checker PASS |
| generated index rows for new entries | aggregate projection from registry sources | Yes | Yes | produced only by `generate_assf_skill_index.py --generate` |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`; `docs/reference/agent_system_skills/registry/README.md`; `docs/reference/agent_system_skills/registry/entries/`; `docs/reference/agent_system_skills/generated/skill-index.json`; `governance/compat/generate_assf_skill_index.py`; `governance/compat/check_assf_skill_index_drift.py`; `governance/compat/run_assf_skill_resolver.py` |
| Existing registry entries at dispatch | `cvf-dispatch-quality-reviewer.json`; `cvf-worker-return-author.json`; `cvf-governance-external-absorption.json` |
| Existing AGSK-derived entries at dispatch | one: `cvf-governance-external-absorption` |
| Resolver smoke result at dispatch | task-class `external-absorption` returns one AGSK-derived candidate only |
| Runtime behavior claimed | N/A_WITH_REASON: AGSK-T7 creates registry metadata only |
| Live/provider proof claimed | N/A_WITH_REASON: no provider/API/model behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |
| Freshness disposition | PASS - current source supports metadata-only candidate expansion and does not support runtime activation |

### Negative Search And Collision Discipline

| Search target | Command or source | Required result | Action if collision appears |
|---|---|---|---|
| candidate source filenames | `Test-Path docs/reference/agent_system_skills/registry/entries/<candidate>.json` | absent before creating | if present, read and either update only if owned by AGSK-T7 or return blocked |
| package root | `Test-Path docs/reference/agent_system_skills/packages` | absent or unchanged | do not create or edit |
| lifecycle promotion tokens | JSON parse of new entries | `status=CANDIDATE`; `candidateState=CANDIDATE`; `certificationState=NOT_STARTED` | repair before return |
| generated index drift | `python governance/compat/check_assf_skill_index_drift.py` | PASS after generator run | repair within scope or block |

## Core Guard Self-Protection Authorization

AGSK-T7 authorizes read/run use of existing ASSF registry generator and checker
scripts only. It does not authorize editing any protected governance helper,
hook, checker, generator, test, session state, handoff, public-sync, product
runtime, provider/live path, or closed predecessor artifact.

| Field | Disposition |
|---|---|
| Authorized guard-maintenance scope | no guard-maintenance edits; read/run existing `generate_assf_skill_index.py`, `check_assf_skill_index_drift.py`, and `run_assf_skill_resolver.py` only |
| Protected paths | authorized protected paths for read/run only: `governance/compat/generate_assf_skill_index.py`, `governance/compat/check_assf_skill_index_drift.py`, `governance/compat/run_assf_skill_resolver.py`; forbidden protected paths: all `governance/compat/*.py` edits, `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, handoff files, public-sync, product runtime, provider/live paths |
| Operator authorization | 2026-06-29 operator asked to reopen AGSK because blind spots may remain |
| Rollback boundary | delete AGSK-T7-created registry entries and worker return, rerun generator to restore index; do not modify protected scripts |

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
|---|---|
| Coverage index status | NOT_APPLICABLE_WITH_REASON |
| Canonical coverage index | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` |
| Reason | AGSK-T7 does not run a new legacy corpus scan or claim coverage-index closure; it consumes the already closed AGSK reabsorption review, the AGSK triage roadmap, and the T4/T5 closures |
| Required worker evidence | cite inherited AGSK reabsorption review manifest/ledger, this work order's source verification, generated ASSF registry/index proof, and candidate coverage table |
| Future guard candidate | AGSK-T6 checker candidate remains conditionally parked until AGSK-T7 provides multiple candidate fixtures and reviewer decides whether checker value is concrete |

## 6B. Roadmap-To-Work-Order Trace Matrix

| Roadmap or review requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| Additional AGSK/external-absorption candidates are allowed after T5 | Authority Chain; Mission | new registry entries | diff and JSON parse | PASS |
| Do not stop at pattern-only absorption | Purpose; External Absorption Value Conversion Matrix | concrete candidate inventory | resolver smoke check | PASS |
| Keep package boundary metadata-only | Scope; Claim Boundary | status and lifecycle fields | JSON parse | PASS |
| Use registry source layout and generator | Scope; Evidence Requirements | generated skill index | generator and drift checker | PASS |
| Preserve runtime/checker conditions | Conditional Reopen Index Handling | no runtime/checker paths changed | `git diff --name-status` | PASS |

## 6C. Worker Autonomy / No-Question Rule

The worker proceeds without operator confirmation for allowed-scope reads,
candidate JSON authoring, generated-index regeneration, evidence-block repairs,
and gate reruns.

Stop and return `BLOCKED_WITH_REASON` if remediation would touch forbidden
paths, create package bodies, wire runtime/checkers, run providers, public-sync,
edit session state, change commit mode, or promote lifecycle state above
`CANDIDATE`.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake summary | second-pass AGSK review found under-converted package-candidate inventory |
| Scope classification | bounded metadata-only registry candidate expansion |
| Risk sensitivity | low runtime risk, high governance value; private external source evidence remains non-authoritative |
| Selected role route | `MULTI_AGENT_SINGLE_ROLE` |
| Role separation basis | no-commit worker authors entries and return; Codex reviewer/closer validates and commits |
| Escalation condition | any runtime, checker, public, provider, package root, or lifecycle promotion |
| Dispatch status | ACCEPT |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | Codex dispatcher creates work order; worker performs no-commit metadata candidate expansion; Codex reviewer/closer decides acceptance and commit |
| phase | DISPATCH_AUTHORING -> EXECUTION -> CLOSURE -> SESSION_SYNC if next move changes |
| baseHeadFor(phase) | dispatchBaseHead=`e4526436`; executionBaseHead=worker captures with `git rev-parse --short HEAD`; closureBaseHead=reviewer captures from worker return |
| changedSetScope(phase) | worker may change only registry entries, generated index, and worker-return path listed in Allowed scope |
| traceScope(phase, actor) | worker return must record commands, changed paths, gate results, source evidence, and claim boundary |
| commitOwner(phase) | `WORKER_MUST_NOT_COMMIT`; Codex reviewer/closer owns material commit if accepted |
| crossBatchIsolation | no AGSK-T6 checker, runtime, session-sync, or unrelated batch work while worker return is pending |
| nextMoveSurfaces | worker must not edit next-move surfaces |
| closer designation | Codex reviewer/closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_AGSK_T7_PACKAGE_CANDIDATE_EXPANSION_FROM_SOURCE_PACK_COMPLETION_2026-06-29.md` |
| workerReturnPath | `docs/reviews/CVF_AGSK_T7_PACKAGE_CANDIDATE_EXPANSION_FROM_SOURCE_PACK_WORKER_RETURN_2026-06-29.md` |
| reviewerOwnedClosurePaths | accepted registry entries, generated index, worker return, material commit, and later session-sync if next move changes |
| workerReturnDisposition | `COMPLETE_PENDING_REVIEW`, `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, or `BLOCKED_WITH_REASON` |
| reviewerCommitRule | reviewer may commit only after source-fidelity, claim boundary, changed-set scope, generator, drift check, and gates pass |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | ASSF registry source family plus generated metadata index |
| Storage decision | add compact per-candidate JSON sources under existing registry entries; regenerate the existing skill index aggregate through the existing generator |
| Existing aggregate impact | `docs/reference/agent_system_skills/generated/skill-index.json` changes only through generator output |
| Generated state impact | none; no `CVF_SESSION/**` generated aggregate changes are authorized |
| Durable governance boundary | metadata-only candidate inventory; no package root, `SKILL.md`, runtime loader, checker, provider, public-sync, or session state |

## 7. Write Ownership

Owned file patterns:

- `docs/reference/agent_system_skills/registry/entries/cvf-engineering-spec-driven-development.json`
- `docs/reference/agent_system_skills/registry/entries/cvf-engineering-planning-task-breakdown.json`
- `docs/reference/agent_system_skills/registry/entries/cvf-governance-anti-rationalization-guard.json`
- `docs/reference/agent_system_skills/registry/entries/cvf-governance-context-packet-builder.json`
- `docs/reference/agent_system_skills/registry/entries/cvf-governance-evidence-receipt-review-freeze.json`
- `docs/reference/agent_system_skills/registry/entries/cvf-governance-persona-skill-boundary-review.json`
- `docs/reference/agent_system_skills/generated/skill-index.json`
- `docs/reviews/CVF_AGSK_T7_PACKAGE_CANDIDATE_EXPANSION_FROM_SOURCE_PACK_WORKER_RETURN_2026-06-29.md`

Forbidden paths:

- `docs/reference/agent_system_skills/packages/`
- `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`
- `governance/compat/`
- `.private_reference/legacy/`
- `CVF_SESSION/`
- `CVF_SESSION_MEMORY.md`
- handoff files

## 8. Execution Plan

1. Capture `executionBaseHead` and pre-edit `git status --short`.
2. Run pre-flight checks and pre-implementation autorun.
3. Read and compare existing registry entries to determine next
   `registryOrder` values. Expected next values are 4 through 9 unless the
   worker finds new entries already present.
4. Create the candidate JSON files listed in Write Ownership. Each entry must:
   - conform to ASSF compact machine source field families;
   - use `status = CANDIDATE`;
   - use `candidateState = CANDIDATE`;
   - use `approvalState = AWAITING_REVIEW`;
   - use `uatState = NOT_STARTED`;
   - use `certificationState = NOT_STARTED`;
   - include `riskTriggers`;
   - keep `externalCliMcpDisposition = DEFERRED_WITH_REASON`;
   - state that metadata loading never grants authority or runtime activation.
5. Run:

```powershell
python governance/compat/generate_assf_skill_index.py --generate
python governance/compat/check_assf_skill_index_drift.py
```

6. Run resolver smoke checks for representative task classes:

```powershell
python governance/compat/run_assf_skill_resolver.py --task-class source-review --max-results 20
python governance/compat/run_assf_skill_resolver.py --task-class worker-execution --max-results 20
python governance/compat/run_assf_skill_resolver.py --task-class package-candidate-triage --max-results 20
```

7. Create the worker-return artifact with required sections and evidence.
8. Run `python governance/compat/run_worker_return_fast_gate.py`.
9. Run reviewer-fast hook or record an allowed-scope blocker.
10. Return without committing.

## Evidence Requirements

Required evidence:

- `executionBaseHead` and `git status --short` before edits.
- `git diff --name-status` showing only owned paths.
- JSON parse or equivalent validation of every new entry.
- source search evidence for each candidate concept.
- generator command/result.
- `python governance/compat/check_assf_skill_index_drift.py` PASS.
- `rg -n` evidence that generated index contains all new skill IDs.
- resolver smoke-check output after generation.
- worker-return fast gate result.
- reviewer-fast gate result or classified failure.
- statement that HEAD is unchanged by worker.

Base-anchor evidence:

| Field | Required value |
|---|---|
| dispatchBaseHead | `e4526436` |
| executionBaseHead | worker captures before edits |
| closureBaseHead | reviewer captures from worker return |
| Commit mode | `WORKER_MUST_NOT_COMMIT` |

## 10. Acceptance Criteria

| Criterion | Evidence |
|---|---|
| At least five of six planned candidates are created, or every omitted candidate has a source-backed blocker | candidate coverage table in worker return |
| Every created entry has unique `skillId` and `registryOrder` | JSON parse and generated index review |
| Every created entry remains `CANDIDATE` with no lifecycle promotion | JSON parse |
| Every created entry includes `riskTriggers` and metadata-only claim boundary | JSON parse |
| Generated index includes created entries and omits `registryOrder` from generated skill objects | generated index review |
| Drift checker passes after generation | drift checker command |
| No package root, checker, runtime, resolver mutation, session edit, provider, public-sync, or legacy mutation occurs | `git diff --name-status` |
| Worker makes no commit | HEAD unchanged and `git status --short` |

Fail conditions:

| Fail condition | Required action |
|---|---|
| worker creates package root, `SKILL.md`, resolver, checker, session edit, or public-sync artifact | return `BLOCKED_WITH_REASON`; reviewer rejects scope |
| worker promotes lifecycle above `CANDIDATE` or claims package activation | return `BLOCKED_WITH_REASON` |
| generated index is hand-edited without generator run | return `BLOCKED_WITH_REASON` |
| source verification cannot trace a candidate to AGSK source evidence | omit that candidate with explicit blocker or return `BLOCKED_WITH_REASON` |
| drift checker fails and cannot be repaired inside Allowed scope | return `BLOCKED_WITH_REASON` |
| any runtime/provider/live/public claim is introduced | return `BLOCKED_WITH_REASON` |

## 11. Review Gate

Implementation may proceed only after:

- this work order exists and passes pre-dispatch/dispatch-quality gates;
- worker captures `executionBaseHead`;
- worker runs pre-implementation autorun on a real base.

Closure may proceed only after:

- reviewer verifies changed-set scope;
- reviewer verifies source-fidelity, candidate coverage, generated-index
  provenance, drift proof, resolver smoke checks, and claim boundary;
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

`docs/reviews/CVF_AGSK_T7_PACKAGE_CANDIDATE_EXPANSION_FROM_SOURCE_PACK_WORKER_RETURN_2026-06-29.md`

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
- Registry Candidate Coverage Table
- Registry Field-Family Coverage
- Generated Index Drift Proof
- Resolver Smoke Check
- Corpus Completeness And Report Integrity
- External Knowledge Intake Routing
- External Absorption Value Conversion Matrix
- Conditional Reopen Index Handling
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
candidate coverage, and a `dispatchWorkOrder:` line citing this work order.
Conditional sections that do not apply must remain present with
`N/A with reason` or `NOT_APPLICABLE_WITH_REASON`; do not omit them.

## Work-Order Fulfillment Manifest

| Required output | Path or evidence | Owner | Status |
|---|---|---|---|
| Candidate entries | planned files under `docs/reference/agent_system_skills/registry/entries/` | worker | REQUIRED |
| Generated index | `docs/reference/agent_system_skills/generated/skill-index.json` | worker via generator | REQUIRED |
| Worker return | `docs/reviews/CVF_AGSK_T7_PACKAGE_CANDIDATE_EXPANSION_FROM_SOURCE_PACK_WORKER_RETURN_2026-06-29.md` | worker | REQUIRED |
| Material commit | accepted outputs committed by reviewer only | reviewer | PENDING_REVIEW |
| Session sync | only after material acceptance if next move changes | reviewer | PENDING_REVIEW |

## Required Proof Manifest

| Proof | Path | Required literal | Required at handoff |
|---|---|---|---|
| Dispatch status | this work order | `DISPATCH_READY` | Yes |
| Commit mode | this work order | `WORKER_MUST_NOT_COMMIT` | Yes |
| Candidate lifecycle | new registry entries | `CANDIDATE` | Yes |
| External boundary | new registry entries | `DEFERRED_WITH_REASON` | Yes |
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
| Owner-surface map | inherited review owner-surface map plus AGSK-T7 target `docs/reference/agent_system_skills/registry/entries/` and generated index |
| Unresolved items | T7 resolves the package-candidate inventory gap; any omitted candidate must be listed in worker return |
| Completion claim boundary | work-order dispatch only; no new corpus sweep, runtime, provider, package activation, checker, public-sync, or production claim |

## Mandatory Blind-Spot Control Block

| Gate | Evidence |
|---|---|
| Gate 1: absorption source enumerated | inherited from `docs/reviews/CVF_AGSK_ABSORPTION_PACK_REABSORPTION_REVIEW_2026-06-29.md` |
| Gate 2: all files listed | inherited source review lists 29 files |
| Gate 3: each file has terminal status | inherited source review processing ledger has terminal rows |
| Gate 4: reconciliation passes | inherited source review reports manifest=29, ledger_terminal=29, unresolved=0 |
| Gate 5: adapted/deferred items traced | T7 traces concrete capability concepts into ASSF registry candidates |
| Blind-spot verdict | REOPENED_FOR_PACKAGE_CANDIDATE_EXPANSION |

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
- Drift check: this work order reuses the closed corpus review and performs targeted source verification for candidate expansion
- Output traceability: each created candidate must cite source artifacts and review artifacts
- Adversarial verification: worker must not treat metadata candidate creation as runtime activation
- Corpus verdict: PARTIAL - work-order dispatch based on prior COMPLETE_VERIFIED review plus second-pass package-candidate audit

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | legacy source family |
| Chain map route | legacy source family -> AGSK reabsorption review -> AGSK package-candidate triage -> AGSK-T7 ASSF registry candidate expansion -> reviewer closure |
| Matching local-view guard | `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py` |
| Owner surface | `docs/reference/agent_system_skills/registry/entries/`; `docs/reference/agent_system_skills/generated/skill-index.json` |
| Disposition | ADAPT concrete AGSK capability concepts into CVF ASSF registry candidates |
| Claim boundary | documentation and metadata-only work order; no runtime, provider, package activation, checker, public-sync, or production claim |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| AGSK advisory doctrine already absorbed | skill anatomy, anti-rationalization, progressive disclosure, persona boundary, and evidence-receipt doctrine | DOCTRINE_ADAPTED | `docs/reference/agent_system_skills/CVF_AGSG_AGENT_SKILLS_ASSF_CAPABILITY_ANATOMY_AND_RATIONALIZATION_ADVISORY.md` | none in AGSK-T7 | documentation-only doctrine; no runtime or package activation |
| `sample_capability_manifest.json`; `04_CVF_CAPABILITY_PACKAGE_STANDARD.md` | `cvf.engineering.spec_driven_development` capability pattern | PACKAGE_CANDIDATE | `cvf-engineering-spec-driven-development.json` | create metadata candidate | CANDIDATE only; no package body or runtime activation |
| `05_SKILL_ACTIVATION_RESOLVER.md`; capability ID examples | planning/task-breakdown resolver candidate | PACKAGE_CANDIDATE | `cvf-engineering-planning-task-breakdown.json` | create metadata candidate | CANDIDATE only |
| `06_ANTI_RATIONALIZATION_GUARD.md`; anti-rationalization reference | shortcut-signal escalation guard | PACKAGE_CANDIDATE | `cvf-governance-anti-rationalization-guard.json` | create metadata candidate | CANDIDATE only |
| `08_CONTEXT_PACKET_STANDARD.md` | scoped context-packet construction | PACKAGE_CANDIDATE | `cvf-governance-context-packet-builder.json` | create metadata candidate | CANDIDATE only |
| `10_VERIFICATION_AND_EVIDENCE_RECEIPT.md` | skill receipt, review gate receipt, freeze condition | PACKAGE_CANDIDATE | `cvf-governance-evidence-receipt-review-freeze.json` | create metadata candidate | CANDIDATE only |
| `07_PERSONA_ORCHESTRATION_BOUNDARY.md` | persona may not orchestrate persona; fan-out and merge controls | PACKAGE_CANDIDATE | `cvf-governance-persona-skill-boundary-review.json` | create metadata candidate | CANDIDATE only |
| AGSK activation resolver runtime states | possible executable selection behavior | RUNTIME_CANDIDATE | conditional reopen index | keep parked until package promotion review approves at least one package | no runtime in T7 |
| AGSK package anatomy checker requirements | possible ASSF candidate anatomy checker | CHECKER_CANDIDATE | conditional reopen index | after T7, reviewer may decide whether multiple candidate fixtures justify AGSK-T6 checker | no checker wiring in T7 |
| Pack-internal Python checkers | direct import rejected | REJECT_DIRECT_IMPORT | existing AGSK review rejected ledger | none | no direct checker import |
| README and TREEVIEW | inventory/provenance only | NO_PACKAGE_OR_RUNTIME_VALUE | inherited review | none | no runtime/package/checker action |

## Conditional Reopen Index Handling

| Candidate lane | Current handling | AGSK-T7 effect |
|---|---|---|
| Activation resolver runtime | cited existing row `AGSK-activation-resolver-runtime` | remains parked until a later package promotion review approves at least one package |
| Package anatomy checker | cited existing row `AGSK-package-anatomy-checker` | T7 may create enough candidate fixtures for a future value probe, but no checker implementation is authorized here |
| Additional package candidates | this work order | resolves the immediate inventory gap by creating metadata candidates |

## Finding-To-Governance Learning Disposition

| Field | Required worker value |
|---|---|
| Defect class | `VALUE_CONVERSION_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Disposition | `PACKAGE_CANDIDATES_CREATED_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| Runtime/provider/cost lane | `N/A_WITH_REASON` |
| Next control action | state whether AGSK-T6 checker value should be reopened after multiple candidate fixtures exist |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | AGSK-T7 metadata-only ASSF registry candidate expansion |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT - worker must provide source searches, generator result, drift check, resolver smoke checks, gate results, and changed-set evidence |
| actionEvidence | ACTION_EVIDENCE_PRESENT - worker must provide registry JSON entries, generated index, and source-verification evidence |
| invocationBoundary | governed local documentation and metadata editing only |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | create additional `CANDIDATE` registry source entries and regenerate metadata-only index |
| forbiddenExpansion | no package body, `SKILL.md`, resolver mutation, checker wiring, runtime, provider/live proof, public-sync, session sync, package activation, lifecycle promotion, or production claim |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher |
| Provider or surface | local workspace |
| Session or invocation | AGSK-T7 work order authoring, 2026-06-29 |
| Working directory | repository root |
| Command or tool surface | source reads, rg searches, ADIF resolver import, apply_patch |
| Target paths | this work order |
| Allowed scope source | operator requested second-pass AGSK review because blind spots may remain |
| Before status evidence | clean worktree at HEAD `e4526436` |
| After status evidence | dispatch-ready work order pending gate/commit |
| Diff evidence | `git diff --name-status`; `git status --short` before commit |
| Approval boundary | dispatch authoring only; no AGSK-T7 execution by dispatcher |
| Claim boundary | repo-local trace only; no runtime/provider/public claim |
| Agent type | dispatcher |
| Invocation ID | `agsk-t7-package-candidate-expansion-work-order-2026-06-29` |
| Expected manifest | N/A with reason: dispatch work order defines future worker/reviewer scope; exact implementation manifest is required in worker return |
| Actual changed set | N/A with reason: dispatch authoring changes only this work-order artifact before execution starts |
| Manifest delta | N/A with reason: no implementation manifest is being closed by this dispatch artifact |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Rescan Intelligence Hardening

- Original source artifact:
  `.private_reference/legacy/CVF 28.06/CVF_Agent_Skills_Governance_Absorption_Pack`.
- Predecessor intake artifact:
  `docs/reviews/CVF_AGSK_ABSORPTION_PACK_REABSORPTION_REVIEW_2026-06-29.md`.
- Delta ledger status: `CHANGED_DISPOSITION` because prior AGSK closeout
  accepted doctrine and one candidate, while AGSK-T7 now treats the concrete
  capability inventory as package-candidate value to convert.
- Routing matrix status:
  - `DO_NOW`: create metadata-only ASSF registry candidates for source-backed
    AGSK capability concepts.
  - `RESOLVED_BY_DESIGN`: keep already-adapted doctrine in the AGSG advisory.
  - `SEPARATE_RUNTIME_TRANCHE`: activation resolver runtime remains parked.
  - `STRATEGIC_OPERATOR_DECISION`: checker value after multiple candidate
    fixtures requires reviewer/operator decision.
  - `OUT_OF_SCOPE`: provider/live, public-sync, package activation, runtime,
    checker wiring, and direct pack checker import.
- Semantic sampling status: `PARTIAL_TARGETED` to candidate-bearing AGSK source
  files and existing ASSF registry surfaces.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Disposition |
|---|---|
| UNCHANGED_FROM_INTAKE | Direct import, runtime activation, provider/live proof, and pack-local checker wiring remain rejected or parked. |
| CHANGED_DISPOSITION | Concrete AGSK capability examples move from pattern-only/doctrine context into metadata package-candidate expansion. |
| NEW_FINDING | Existing ASSF registry has only one AGSK-derived candidate, so source pack value is under-converted as practical inventory. |
| REMOVED_OR_REJECTED | `ABSORPTION_SPEC_ONLY` pack-local status and direct checker code remain rejected as CVF authority. |

### Follow-Up Routing Matrix

| Lane | Disposition |
|---|---|
| DO_NOW | Execute AGSK-T7 metadata-only candidate expansion. |
| RESOLVED_BY_DESIGN | Existing AGSG advisory remains the owner for doctrine-level anatomy and rationalization guidance. |
| DEFER | Package anatomy checker value probe until AGSK-T7 creates multiple candidate fixtures and reviewer accepts concrete value. |
| SEPARATE_RUNTIME_TRANCHE | Activation resolver runtime requires future package promotion and fresh work order. |
| STRATEGIC_OPERATOR_DECISION | Whether AGSK-T6 checker should reopen after T7 is a reviewer/operator decision. |
| OUT_OF_SCOPE | Runtime, provider/live proof, public-sync, package body, `SKILL.md`, direct checker import, and lifecycle promotion. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| AGSK-T7-RS1 | `04_CVF_CAPABILITY_PACKAGE_STANDARD.md` | `cvf.engineering.spec_driven_development` is a concrete capability example | DO_NOW candidate | Could doctrine-only absorption be enough? | FAIL_DOCTRINE_ONLY_UNDER_CONVERTS_PACKAGE_VALUE |
| AGSK-T7-RS2 | `08_CONTEXT_PACKET_STANDARD.md` | context packet has structure and receipt link | DO_NOW candidate | Could this wait for runtime resolver? | PASS_METADATA_CANDIDATE_FIRST |
| AGSK-T7-RS3 | pack-internal checkers | direct checker import exists | OUT_OF_SCOPE direct import | Could direct wiring close blind spot faster? | PASS_REJECT_DIRECT_IMPORT_CVF_NATIVE_ONLY |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: The AGSK source pack contains several concrete
capability concepts that can become metadata-only ASSF registry candidates
without runtime activation.

Evidence Comparison Requirement: worker return must compare actual created
candidate entries and resolver smoke output against the planned candidate list.

Contradiction Handling Requirement: if a candidate lacks enough source support,
omit that candidate with a source-backed blocker rather than inventing content.

Claim Update Requirement: worker return records whether the package-candidate
inventory gap was confirmed, narrowed, or invalidated.

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
| Resolver smoke checks run | worker records outputs |
| Worker return fast gate | worker runs or records blocker |
| Reviewer-fast gate | worker runs or records blocker; reviewer reruns before commit |
| Public export disposition | `DEFERRED_PRIVATE_ONLY` |
| Session continuity | reviewer-owned after material commit if next move changes |

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` without continuing if:

- pre-implementation autorun fails outside Allowed scope;
- the ASSF contract, registry README, generator, drift checker, existing
  entries, or AGSK source evidence cannot be read;
- source verification contradicts the planned candidate shape;
- a required candidate needs package root, checker, resolver, runtime,
  provider/live, public-sync, session-state, or existing contract changes;
- any required gate cannot be repaired inside Allowed scope.

## Operator Checkpoint

N/A with reason: operator requested this second-pass AGSK return because blind
spots may remain. No extra checkpoint is required for bounded metadata-only
candidate expansion. Operator approval is required only for scope expansion
listed in Return-To-Orchestrator Conditions.

## Claim Boundary

This work order authorizes only a no-commit worker-return lane for
metadata-only ASSF registry candidate expansion and regenerated skill index. It
does not authorize package body creation, `SKILL.md`, checker implementation,
resolver mutation, runtime activation, automatic skill invocation, CLI/MCP
adapter implementation, provider/live proof, public-sync, session-sync,
lifecycle promotion, production readiness, or worker commit.
