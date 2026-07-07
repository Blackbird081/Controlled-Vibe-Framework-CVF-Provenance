# CVF Agent Work Order - AGSK-T4 ASSF Risk Triggers Field Patch

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-29

docType: work_order

Batch ID: AGSK-T4

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: d8b14a2e

## Dispatch Prompt Envelope

Role: no-commit worker for AGSK-T4 documentation-only ASSF contract patch; Codex remains reviewer/closer.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_T4_ASSF_RISK_TRIGGERS_FIELD_PATCH_2026-06-29.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

Base: executionBaseHead must be captured with `git rev-parse --short HEAD` before edits.

Current-time notes: current date is 2026-06-29. This work order starts after triage roadmap commit `d8b14a2e`. No live key, provider call, runtime run, public-sync, or package activation is authorized.

Do-not-misread notes: execute AGSK-T4 only. Do not create the AGSK-T5 registry entry, do not create `packages/<skill-id>/SKILL.md`, do not regenerate the skill index, do not wire a checker, and do not edit session state.

Required first actions: read this work order, the triage roadmap, the ASSF package contract, the AGSK reabsorption review, the active session front door/state/handoff, and guard orientation; then capture `git status --short` and run pre-implementation autorun.

Return contract: return `COMPLETE_PENDING_REVIEW`, `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, or `BLOCKED_WITH_REASON` with changed paths, executionBaseHead, gate results, source-verification evidence, and HEAD unchanged.

## Purpose

Convert the AGSK-T4 roadmap decision into a bounded no-commit worker packet.
The worker updates only the ASSF package contract with a CVF-owned
`riskTriggers` field and returns evidence for reviewer acceptance.

## 1. Mission

Patch `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` so the
ASSF package contract has a CVF-owned `riskTriggers` field for pattern-level
risk escalation guidance. The patch is documentation-only. It must reconcile
external AGSK evidence into CVF contract language without creating runtime
behavior, a package instance, a resolver, a checker, generated registry output,
or any provider/live/public claim.

## 2. Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Operator instruction | chat request on 2026-06-29: "ban viet work order" after AGSK triage roadmap | authorizes work-order authoring for the next AGSK tranche |
| Active session front door | `CVF_SESSION_MEMORY.md` | startup front door and active session pointers |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | current generated state; pending next-move sync after AGSK triage |
| Active handoff | `AGENT_HANDOFF_V26_2026-06-28.md` | active handoff named by state registry |
| Triage roadmap | `docs/roadmaps/CVF_AGSK_PACKAGE_CANDIDATE_TRIAGE_ROADMAP_2026-06-29.md` | opens AGSK-T4 and defines minimum outputs, status ceiling, non-goals, and T5 dependency |
| Source review | `docs/reviews/CVF_AGSK_ABSORPTION_PACK_REABSORPTION_REVIEW_2026-06-29.md` | file-level AGSK pack review and value-conversion matrix |
| Contract owner surface | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | sole authorized target for the T4 contract field patch |
| External source evidence | `.private_reference/legacy/CVF 28.06/CVF_Agent_Skills_Governance_Absorption_Pack/.cvfgenerated/examples/agent-skills-governance/sample_capability_manifest.json` | evidence input only; not canonical CVF authority |
| GC-018 candidate | triage roadmap section `Tranche AGSK-T4` | bounded continuation candidate for documentation-only contract patch |

Authority boundary:

- If this work order conflicts with the triage roadmap or ASSF contract owner
  surface, stop and return `BLOCKED_WITH_REASON`.
- External AGSK files are evidence inputs only. The worker must rewrite into
  CVF terms and must not copy or promote pack-local status vocabulary as CVF
  authority.

## 3. Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | authored this source-verified work order |
| Worker | assigned no-commit worker agent | performs the bounded contract patch and worker return |
| Reviewer/closer | Codex | validates returned diff, gates, source fidelity, claim boundary, and commits if accepted |
| Operator approval required | operator | any expansion into T5, runtime, checker wiring, public-sync, provider/live proof, session-sync ownership, or package activation |

## 4. Scope

Allowed scope:

- edit `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`;
- create `docs/reviews/CVF_AGSK_T4_ASSF_RISK_TRIGGERS_FIELD_PATCH_WORKER_RETURN_2026-06-29.md`;
- run read-only source searches and governance gates;
- repair documentation formatting or evidence blocks inside the two allowed paths.

Forbidden scope:

- creating or editing `docs/reference/agent_system_skills/registry/entries/`;
- editing `docs/reference/agent_system_skills/generated/skill-index.json`;
- running `governance/compat/generate_assf_skill_index.py --generate`;
- creating `docs/reference/agent_system_skills/packages/` or any `SKILL.md`;
- editing any `governance/compat/*.py` checker, hook, autorun script, or test;
- editing `.private_reference/legacy/` or external repo/folder contents;
- editing `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, or `AGENT_HANDOFF*.md`;
- claiming runtime behavior, provider/live proof, package activation,
  production readiness, public readiness, or public-sync.

Risk ceiling: R0 documentation-only governance contract patch.

## Scope / Target / Owner Boundary

Target: one documentation-only ASSF contract field patch and one worker-return
artifact.

Owner boundary:

- worker owns only the two paths listed in Write Ownership;
- Codex reviewer/closer owns material commit, completion review if needed, and
  later session-sync;
- operator approval is required for any expansion beyond T4.

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
- `docs/roadmaps/CVF_AGSK_PACKAGE_CANDIDATE_TRIAGE_ROADMAP_2026-06-29.md` - roadmap source and T4 acceptance.
- `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` - contract owner surface to patch.
- `docs/reviews/CVF_AGSK_ABSORPTION_PACK_REABSORPTION_REVIEW_2026-06-29.md` - source review and deferred field evidence.
- `.private_reference/legacy/CVF 28.06/CVF_Agent_Skills_Governance_Absorption_Pack/.cvfgenerated/examples/agent-skills-governance/sample_capability_manifest.json` - external evidence input.

## 6. Pre-Flight Checks

Commands to run before implementation:

```powershell
git rev-parse --short HEAD
git status --short
rg -n "riskTriggers|useWhen|doNotUseWhen|riskCeiling|authorityCeiling" docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md
rg -n "risk_triggers|use_when|do_not_use_when|requires_approval" ".private_reference/legacy/CVF 28.06/CVF_Agent_Skills_Governance_Absorption_Pack/.cvfgenerated/examples/agent-skills-governance/sample_capability_manifest.json"
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

Expected results:

- worktree state is recorded before edits;
- current ASSF contract search shows `useWhen`, `doNotUseWhen`, `riskCeiling`,
  and `authorityCeiling`;
- `riskTriggers` is absent from the current ASSF contract before this patch;
- external evidence search shows `risk_triggers` in the AGSK sample manifest;
- pre-implementation gate passes or any allowed-scope failure is repaired and rerun.

Allowed-scope gate failures must be repaired and rerun. Escalate only if repair
would exceed Allowed scope, change the claim boundary, require live/provider
proof, touch forbidden paths, or alter commit mode.

## 6A. Source-Fidelity Pass

### Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| EXISTS: T4 roadmap opens ASSF contract `riskTriggers` field patch | `docs/roadmaps/CVF_AGSK_PACKAGE_CANDIDATE_TRIAGE_ROADMAP_2026-06-29.md` | Tranche AGSK-T4 | AGSK-T4 | AGSK package-candidate triage roadmap | EXISTS | ACCEPT |
| VALUE_SET: T4 output is documentation-only with status ceiling `ADVISORY_READY` | `docs/roadmaps/CVF_AGSK_PACKAGE_CANDIDATE_TRIAGE_ROADMAP_2026-06-29.md` | Tranche AGSK-T4 minimum outputs | ADVISORY_READY | AGSK-T4 roadmap tranche | VALUE_SET | ACCEPT |
| EXISTS: current ASSF compact schema has `useWhen` and `doNotUseWhen` | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema, Purpose and trigger row | useWhen; doNotUseWhen | ASSF package contract | EXISTS | ACCEPT |
| EXISTS: current ASSF compact schema has `riskCeiling` | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema, Selectors row | riskCeiling | ASSF package contract | EXISTS | ACCEPT |
| EXISTS: current ASSF risk fields include `authorityCeiling` | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Risk And Lifecycle Fields | authorityCeiling | ASSF package contract | EXISTS | ACCEPT |
| DOC_ONLY_NEW: `riskTriggers` is the new CVF contract field to add | `docs/roadmaps/CVF_AGSK_PACKAGE_CANDIDATE_TRIAGE_ROADMAP_2026-06-29.md` | External Absorption Value Conversion Matrix and Tranche AGSK-T4 | riskTriggers | ASSF package contract patch | DOC_ONLY_NEW | ACCEPT |
| EXISTS: external AGSK sample manifest contains `activation.risk_triggers` | `.private_reference/legacy/CVF 28.06/CVF_Agent_Skills_Governance_Absorption_Pack/.cvfgenerated/examples/agent-skills-governance/sample_capability_manifest.json` | activation object | risk_triggers | AGSK external evidence input | EXISTS | ACCEPT |
| EXISTS: external AGSK package standard lists `risk_triggers` under activation | `.private_reference/legacy/CVF 28.06/CVF_Agent_Skills_Governance_Absorption_Pack/docs/absorptions/agent-skills-governance/04_CVF_CAPABILITY_PACKAGE_STANDARD.md` | Required manifest fields | risk_triggers | AGSK external evidence input | EXISTS | ACCEPT |
| EXISTS: worker return path is planned new review artifact | `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_T4_ASSF_RISK_TRIGGERS_FIELD_PATCH_2026-06-29.md` | Allowed scope and Worker Return Packet Shape | `docs/reviews/CVF_AGSK_T4_ASSF_RISK_TRIGGERS_FIELD_PATCH_WORKER_RETURN_2026-06-29.md` | AGSK-T4 worker return | DOC_ONLY_NEW | ACCEPT |

### New Doc-Only Fields Table

| New doc-only field | Purpose | Not sourced from runtime? | Runtime claim blocked? | Validation expectation |
|---|---|---|---|---|
| `riskTriggers` | list of pattern-level risk escalation triggers for ASSF package metadata | Yes | Yes | contract/documentation validation now; future checker only if AGSK-T6 is separately opened |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`; `docs/reference/agent_system_skills/registry/entries/`; `docs/reference/agent_system_skills/generated/skill-index.json` |
| Search for existing field | `rg -n "riskTriggers" docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` returned no current contract field before dispatch |
| Existing adjacent fields | `useWhen`, `doNotUseWhen`, `riskCeiling`, and `authorityCeiling` exist in the contract |
| Provider registry surfaces checked | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and `PROVIDER_CAPABILITY_REGISTRY` are N/A with reason: this work order makes no provider-registry absence or hardcoded-runtime claim; provider terms are forbidden-scope boundaries only |
| Runtime behavior claimed | N/A_WITH_REASON: this work order patches documentation contract only |
| Live/provider proof claimed | N/A_WITH_REASON: no live governance behavior, provider call, model/API behavior, or benchmark is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |
| Freshness disposition | PASS - current source supports a bounded contract-field patch only |

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
|---|---|
| Coverage index status | NOT_APPLICABLE_WITH_REASON |
| Canonical coverage index | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` |
| Reason | AGSK-T4 does not run a new legacy corpus scan or claim coverage-index closure; it consumes the already closed AGSK reabsorption review and the triage roadmap |
| Required worker evidence | cite the inherited AGSK reabsorption review manifest/ledger and this work order's source verification |
| Future guard candidate | N/A with reason: AGSK-T6 checker candidate remains parked until T4 and T5 close |

### Negative Search And Collision Discipline

| Search target | Command or source | Result | Disposition |
|---|---|---|---|
| `riskTriggers` in current ASSF contract | `rg -n "riskTriggers" docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | no match before dispatch | field absent from contract; add as DOC_ONLY_NEW |
| `risk_triggers` in external AGSK source | `rg -n "risk_triggers" ".private_reference/legacy/CVF 28.06/CVF_Agent_Skills_Governance_Absorption_Pack"` | matches sample manifest and external package standard | evidence input only; normalize to CVF camelCase `riskTriggers` |
| `packages/<skill-id>/SKILL.md` owner surface | `Test-Path docs/reference/agent_system_skills/packages` | not present before dispatch | out of scope for T4; do not create |

## 6B. Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| Add `riskTriggers` to ASSF package contract | Mission; Allowed scope; Execution Plan | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | `rg -n "riskTriggers" docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | PASS |
| Source-verify field against AGSK manifest evidence | Source-Fidelity Pass | Source Verification Block and worker return | `rg -n "risk_triggers" <external sample manifest>` | PASS |
| Keep status ceiling advisory and documentation-only | Scope; Claim Boundary | no runtime/source code paths touched | `git diff --name-status` | PASS |
| Do not create package instance or generated index | Forbidden scope | no registry/generated/package paths changed | `git diff --name-status` | PASS |
| Record finding-to-governance learning | Evidence Requirements | worker return and contract learning note if applicable | reviewer checks worker return | PASS |
| Run governance gates on real changed range | Review Gate | gate receipts in worker return | listed commands | PASS |

## 6C. Worker Autonomy / No-Question Rule

The worker proceeds without operator confirmation for allowed-scope reads,
documentation edits, evidence-block repairs, and gate reruns. The worker must
repair allowed-scope gate failures and rerun the failed gate before handoff.

Stop and return `BLOCKED_WITH_REASON` if remediation would touch forbidden
paths, create a package candidate, wire a checker, run live/provider proof,
public-sync, use secrets/quota, alter commit mode, edit session state, or change
the claim boundary.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake summary | AGSK triage opened T4 to patch `riskTriggers` into ASSF package contract |
| Scope classification | bounded documentation-only governance contract patch |
| Risk sensitivity | low runtime risk, high governance precision value; no public, live, provider, secrets, or runtime behavior |
| Selected role route | `MULTI_AGENT_SINGLE_ROLE` |
| Role separation basis | no-commit worker authors bounded patch and return; Codex reviewer/closer validates and commits if accepted |
| Escalation condition | any scope expansion into T5 registry, runtime, checker, public-sync, session state, or provider/live proof |
| Dispatch status | ACCEPT |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | Codex dispatcher creates work order; worker performs no-commit contract patch; Codex reviewer/closer decides acceptance and commit |
| phase | DISPATCH_AUTHORING -> EXECUTION -> CLOSURE -> SESSION_SYNC if next move changes |
| baseHeadFor(phase) | dispatchBaseHead=`d8b14a2e`; executionBaseHead=worker captures with `git rev-parse --short HEAD`; closureBaseHead=reviewer captures from worker return |
| changedSetScope(phase) | worker may change only the contract and worker-return paths listed in Allowed scope |
| traceScope(phase, actor) | worker return must record commands, changed paths, gate results, source evidence, and claim boundary |
| commitOwner(phase) | `WORKER_MUST_NOT_COMMIT`; Codex reviewer/closer owns material commit if accepted |
| crossBatchIsolation | no AGSK-T5, AGSK-T6, session-sync, or unrelated batch work while this worker return is pending |
| nextMoveSurfaces | worker must not edit next-move surfaces |
| closer designation | Codex reviewer/closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_AGSK_T4_ASSF_RISK_TRIGGERS_FIELD_PATCH_COMPLETION_2026-06-29.md` |
| workerReturnPath | `docs/reviews/CVF_AGSK_T4_ASSF_RISK_TRIGGERS_FIELD_PATCH_WORKER_RETURN_2026-06-29.md` |
| reviewerOwnedClosurePaths | accepted contract patch, optional completion review, material commit, and later session-sync if next move changes |
| workerReturnDisposition | `COMPLETE_PENDING_REVIEW`, `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, or `BLOCKED_WITH_REASON` |
| reviewerCommitRule | reviewer may commit only after source-fidelity, claim boundary, changed-set scope, and gates pass |

## Forbidden Filesystem State Precheck

| Forbidden path | Expected state | Actual state at dispatch | Action if PRESENT |
|---|---|---|---|
| `docs/reference/agent_system_skills/packages/` | ABSENT | ABSENT | block T4 dispatch and ask for scope reconciliation |
| `docs/reviews/CVF_AGSK_T4_ASSF_RISK_TRIGGERS_FIELD_PATCH_WORKER_RETURN_2026-06-29.md` | ABSENT | ABSENT | block if pre-existing unowned artifact appears |

## Pre-Existing Dirty Path Exemptions

| Path | Status at dispatch | Exemption boundary |
|---|---|---|
| N/A with reason | clean worktree at dispatch authoring start | no dirty-path exemption |

## 7. Write Ownership

Owned files:

- `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`
- `docs/reviews/CVF_AGSK_T4_ASSF_RISK_TRIGGERS_FIELD_PATCH_WORKER_RETURN_2026-06-29.md`

Forbidden paths:

- `docs/reference/agent_system_skills/registry/entries/`
- `docs/reference/agent_system_skills/generated/skill-index.json`
- `docs/reference/agent_system_skills/packages/`
- `governance/compat/`
- `CVF_SESSION/`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF*.md`
- `.private_reference/legacy/`

Write mode: modify-listed for the contract; create-only for the worker return.

## Worker Avoidance Checklist

Use this checklist before editing and again before return:

| Finding to avoid | Required worker behavior |
|---|---|
| Do not repeat the false zero-candidate claim | Treat existing ASSF registry entries as real CANDIDATE metadata; T4 does not create or evaluate new entries |
| Do not overfit external `risk_triggers` shape | The external sample uses a list; normalize into CVF `riskTriggers` language rather than requiring an unverified object schema |
| Do not start AGSK-T5 early | Do not create `cvf-governance-external-absorption.json`, regenerate `skill-index.json`, or create package folders |
| Do not treat external pack files as canonical CVF authority | Use them only as evidence inputs already routed through the AGSK review and triage roadmap |
| Do not omit inherited external-absorption controls | Keep Blind-Spot, EAC, corpus, routing, and value-conversion evidence present in the return, using inherited-review wording where no new scan occurs |
| Do not claim runtime absence loosely | Use `Current Runtime Freshness Verification` and state runtime/provider/public claims are N/A with reason |
| Do not list future worker outputs as existing required artifacts | Planned worker-return/completion paths belong in fulfillment or return-contract sections, not as existing proof files |
| Do not mix dispatch trace with session-sync trace | The worker return traces only worker-owned paths; reviewer/session-sync traces belong to reviewer-owned artifacts |
| Do not leave gate failures for the operator | Repair allowed-scope formatting/evidence failures and rerun the failed gate before returning |
| Do not commit | Return with HEAD unchanged; reviewer/closer owns material commit and any session sync |

## 8. Execution Plan

1. Capture `executionBaseHead` and worktree status.
2. Complete Required First Reads.
3. Run pre-implementation autorun with the captured execution base.
4. Patch `CVF_ASSF_PACKAGE_CONTRACT.md`:
   - add `riskTriggers` to the compact machine source schema table;
   - add a rule to the risk/authority field reference or equivalent owner table;
   - specify zero-or-more cardinality;
   - specify entry content as CVF-normalized trigger patterns with optional escalation metadata;
   - state that `riskTriggers` cannot raise authority beyond `authorityCeiling`.
5. Add a concise source-verification or evidence note in the contract if the
   current contract style supports it; otherwise record full source verification
   in the worker return.
6. Author the worker return with source inventory, changed paths, gate results,
   claim boundary, and no-commit status.
7. Run focused verification:
   - `rg -n "riskTriggers|authorityCeiling|riskCeiling" docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`
   - `python governance/compat/check_markdown_structural_completeness.py --base <executionBaseHead> --head HEAD --enforce`
   - `python governance/compat/run_worker_return_fast_gate.py`
   - `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast --parallel --max-workers 6`
8. Return without committing.

## 8A. Design Control Carry-Forward

| Design control | Roadmap source | Work-order handling | Verdict |
|---|---|---|---|
| Scope boundary | triage roadmap Non-Goals and T4 tranche | only contract patch and worker return allowed | PASS |
| Non-goals | triage roadmap Non-Goals | registry, package, checker, runtime, public, provider, session-sync all forbidden | PASS |
| Lane split | triage roadmap Work Plan | executes AGSK-T4 only; T5 starts after T4 closes | PASS |
| Dependency/source-verification plan | triage roadmap Source Evidence | source rows and searches required before implementation | PASS |
| Claim boundary | triage roadmap Claim Boundary | documentation-only contract field; no runtime/package activation | PASS |
| Acceptance criteria | triage roadmap AGSK-T4 criteria | mapped in trace matrix and evidence requirements | PASS |
| Verification/evidence | triage roadmap Verification | gates and focused searches listed | PASS |
| Dispatch-readiness decision | triage roadmap Authorization Boundary | T4 authorized now | PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher |
| Provider or surface | Codex local workspace |
| Session or invocation | AGSK-T4 work order authoring, 2026-06-29 |
| Working directory | repository root |
| Command or tool surface | source reads, ADIF resolver import, rg searches, apply_patch |
| Target paths | this work order |
| Allowed scope source | operator requested work order after AGSK package-candidate triage roadmap commit |
| Before status evidence | clean worktree at HEAD `d8b14a2e` |
| After status evidence | dispatch-ready work order pending gate/commit |
| Diff evidence | `git diff --name-status`; `git status --short` before commit |
| Approval boundary | dispatch authoring only; session-sync is reviewer-owned follow-up; no contract patch execution by dispatcher |
| Claim boundary | repo-local trace only; no runtime/provider/public claim |
| Agent type | dispatcher |
| Invocation ID | `agsk-t4-risk-triggers-work-order-2026-06-29` |
| Expected manifest | N/A with reason: dispatch work order defines future worker/reviewer scope; exact implementation manifest is required in the worker return and reviewer closure |
| Actual changed set | N/A with reason: dispatch authoring changes only this work-order artifact before execution starts |
| Manifest delta | N/A with reason: no implementation manifest is being closed by this dispatch artifact |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Durable files changed by worker | one existing ASSF contract file and one worker-return review artifact |
| Canonical package root | N/A with reason: AGSK-T4 must not create a package root or `SKILL.md` |
| Generated index or aggregate | N/A with reason: AGSK-T4 must not regenerate or edit `docs/reference/agent_system_skills/generated/skill-index.json` |
| Storage migration | N/A with reason: no file relocation or storage migration is authorized |
| New reference-family folders | N/A with reason: no new folder is authorized |
| Layout risk | bounded contract-field addition only; T5 registry entry and T6 checker remain separate governed work |

## 8C. Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: The ASSF contract lacks `riskTriggers`; external
AGSK evidence contains `risk_triggers`; a bounded documentation-only patch can
add CVF-normalized `riskTriggers` without authorizing runtime behavior.

Evidence Comparison Requirement: worker return must compare actual contract
diff and source searches against the prediction.

Contradiction Handling Requirement: if the contract already contains equivalent
coverage under another field, worker must stop or narrow the patch rather than
duplicating schema.

Claim Update Requirement: worker return records whether the claim was confirmed,
revised, narrowed, or invalidated.

## Evidence Requirements

Required evidence:

- `executionBaseHead` and `git status --short` before edits.
- `git diff --name-status` showing only owned paths.
- `rg -n "riskTriggers|authorityCeiling|riskCeiling" docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`.
- `rg -n "risk_triggers" ".private_reference/legacy/CVF 28.06/CVF_Agent_Skills_Governance_Absorption_Pack/.cvfgenerated/examples/agent-skills-governance/sample_capability_manifest.json"`.
- worker return fast gate result.
- reviewer-fast hook result or classified failure.
- clear statement that HEAD is unchanged by worker.

Base-anchor evidence:

| Field | Required value |
|---|---|
| dispatchBaseHead | `d8b14a2e` |
| executionBaseHead | worker captures before edits |
| closureBaseHead | reviewer captures from worker return |
| Commit mode | `WORKER_MUST_NOT_COMMIT` |

## 10. Acceptance Criteria

| Criterion | Evidence |
|---|---|
| `riskTriggers` appears in ASSF contract compact schema or equivalent field table | contract diff and `rg` output |
| rule defines zero-or-more cardinality | contract diff |
| rule defines trigger pattern plus optional escalation metadata or approval/safe-stop note | contract diff |
| rule states `riskTriggers` cannot raise authority beyond `authorityCeiling` | contract diff |
| worker return includes source verification and evidence comparison | worker return |
| no registry/generated/package/checker/session/legacy paths changed | `git diff --name-status` |
| no runtime/provider/live/public/package activation claim | worker return Claim Boundary |
| worker makes no commit | `git status --short` and HEAD unchanged |

Fail conditions:

| Fail condition | Required action |
|---|---|
| worker creates registry entry, package path, checker, generated index, or session edit | return `BLOCKED_WITH_REASON`; reviewer rejects scope |
| worker copies external pack vocabulary as canonical CVF status without normalization | return `BLOCKED_WITH_REASON` or reviewer repair |
| source verification cannot trace the field to roadmap and external evidence | return `BLOCKED_WITH_REASON` |
| gate failure cannot be repaired inside Allowed scope | return `BLOCKED_WITH_REASON` |
| any runtime/provider/live/public claim is introduced | return `BLOCKED_WITH_REASON` |

## 11. Review Gate

Implementation may proceed only after:

- this dispatch work order exists and passes pre-dispatch/dispatch-quality gates;
- worker captures `executionBaseHead`;
- worker runs pre-implementation autorun on a real base.

Closure may proceed only after:

- reviewer verifies changed-set scope;
- reviewer verifies source-fidelity and claim-boundary evidence;
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

`docs/reviews/CVF_AGSK_T4_ASSF_RISK_TRIGGERS_FIELD_PATCH_WORKER_RETURN_2026-06-29.md`

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
changed paths, gate commands/results, and a `dispatchWorkOrder:` line citing
this work order. Conditional sections that do not apply must remain present with
`N/A with reason` or `NOT_APPLICABLE_WITH_REASON`; do not omit them.

## Work-Order Fulfillment Manifest

| Required output | Path or evidence | Owner | Status |
|---|---|---|---|
| Contract patch | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | worker | REQUIRED |
| Worker return | `docs/reviews/CVF_AGSK_T4_ASSF_RISK_TRIGGERS_FIELD_PATCH_WORKER_RETURN_2026-06-29.md` | worker | REQUIRED |
| Material commit | accepted patch committed by reviewer only | reviewer | PENDING_REVIEW |
| Session sync | only after material acceptance if next move changes | reviewer | PENDING_REVIEW |

## Required Artifact Manifest

| Required output | Path | Required at handoff | Exists |
|---|---|---|---|
| Dispatch work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_T4_ASSF_RISK_TRIGGERS_FIELD_PATCH_2026-06-29.md` | yes | yes |
| Contract patch | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | yes | yes |

## Required Proof Manifest

| Proof | Path | Required literal | Required at handoff |
|---|---|---|---|
| Dispatch status | `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_T4_ASSF_RISK_TRIGGERS_FIELD_PATCH_2026-06-29.md` | `DISPATCH_READY` | Yes |
| Commit mode | `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_T4_ASSF_RISK_TRIGGERS_FIELD_PATCH_2026-06-29.md` | `WORKER_MUST_NOT_COMMIT` | Yes |
| T4 field instruction | `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_T4_ASSF_RISK_TRIGGERS_FIELD_PATCH_2026-06-29.md` | `riskTriggers` | Yes |
| T5 boundary | `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_T4_ASSF_RISK_TRIGGERS_FIELD_PATCH_2026-06-29.md` | `AGSK-T5 registry candidate work remains blocked until AGSK-T4 closes` | Yes |

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
| Owner-surface map | source review section `## Owner-Surface Map`; T4 target owner is `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` |
| Unresolved items | 0 unresolved in inherited review; T4 resolves one deferred contract-field gap |
| Completion claim boundary | work-order dispatch only; no new corpus sweep, runtime, provider, package activation, public-sync, or production claim |

## Mandatory Blind-Spot Control Block

| Gate | Evidence |
|---|---|
| Gate 1: absorption source enumerated | inherited from `docs/reviews/CVF_AGSK_ABSORPTION_PACK_REABSORPTION_REVIEW_2026-06-29.md` |
| Gate 2: all files listed | inherited source review lists 29 files |
| Gate 3: each file has terminal status | inherited source review processing ledger has terminal rows |
| Gate 4: reconciliation passes | inherited source review reports manifest=29, ledger_terminal=29, unresolved=0 |
| Gate 5: adapted/deferred items traced | T4 traces one deferred package-candidate field to `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` |
| Blind-spot verdict | CLEAR_FOR_T4_DISPATCH_WITH_INHERITED_CORPUS_REVIEW |

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
- Output traceability: T4 maps one deferred package-candidate field to the ASSF package contract owner surface
- Adversarial verification: external sample shape is list-based, so worker must normalize into CVF `riskTriggers` and must not require unverified object schema
- Corpus verdict: PARTIAL - work-order dispatch based on prior COMPLETE_VERIFIED review; no new corpus completeness claim is made here

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | legacy source family |
| Chain map route | legacy source family -> AGSK reabsorption review -> AGSK package-candidate triage -> ASSF contract field patch -> reviewer closure |
| Matching local-view guard | `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py` |
| Owner surface | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` |
| Disposition | ADAPT one external activation risk-trigger concept into CVF ASSF contract language |
| Claim boundary | documentation-only work order; no runtime, provider, package activation, checker, public-sync, or production claim |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| `sample_capability_manifest.json` and external package standard | activation `risk_triggers` field concept | PACKAGE_CANDIDATE | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Execute AGSK-T4 contract field patch | Contract field only; no package activation |
| AGSK advisory doctrine already absorbed | skill anatomy and anti-rationalization patterns | DOCTRINE_ADAPTED | ASSF advisory reference | none in T4 | documentation-only |
| Future external-absorption skill candidate | package candidate consuming `riskTriggers` | PACKAGE_CANDIDATE | registry entry planned for AGSK-T5 | wait until T4 closes | no registry mutation in T4 |
| Activation resolver states | possible future resolver behavior | RUNTIME_CANDIDATE | future runtime/resolver work order | parked | no runtime in T4 |
| Package anatomy checker | future checker candidate | CHECKER_CANDIDATE | future `governance/compat` work order | parked until T4/T5 close | no checker wiring in T4 |
| Pack-internal Python checkers | direct import rejected | REJECT_DIRECT_IMPORT | AGSK reabsorption review rejected ledger | none | no direct import |
| README and tree inventory value | no package/runtime/checker delta for T4 | NO_PACKAGE_OR_RUNTIME_VALUE | source review provenance | none | no runtime/package/checker action |

## Finding-To-Governance Learning Disposition

| Field | Required worker value |
|---|---|
| Defect class | `RULE_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Disposition | `DESIGN_REVIEW_REQUIRED` or `REFERENCE_ONLY` unless worker finds a concrete checker-worthy repeat defect |
| Runtime/provider/cost lane | `N/A_WITH_REASON` |
| Next control action | state that AGSK-T5 may consume the field only after reviewer acceptance; AGSK-T6 checker remains parked |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | AGSK-T4 documentation-only ASSF package contract field patch |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT - worker must provide searches, gate results, and changed-set evidence |
| actionEvidence | ACTION_EVIDENCE_PRESENT - worker must provide contract diff and source-verification evidence |
| invocationBoundary | governed local documentation editing only |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | add `riskTriggers` contract metadata field |
| forbiddenExpansion | no registry entry, generated index, package body, checker, runtime, provider/live proof, public-sync, session sync, or production claim |

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
| Worker return fast gate | worker runs or records blocker |
| Reviewer-fast gate | worker runs or records blocker; reviewer reruns before commit |
| Public export disposition | `DEFERRED_PRIVATE_ONLY` |
| Session continuity | reviewer-owned after material commit if next move changes |

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` without continuing if:

- pre-implementation autorun fails outside Allowed scope;
- the ASSF contract or AGSK source evidence cannot be read;
- source verification contradicts the planned field patch;
- the patch would require registry, generated index, package body, checker,
  runtime, provider/live, public-sync, or session-state changes;
- any required gate cannot be repaired inside Allowed scope.

## Operator Checkpoint

N/A with reason: operator already approved moving from AGSK triage into the next
work order. No extra checkpoint is required for the bounded T4 documentation-only
patch. Operator approval is required only for scope expansion listed in
Return-To-Orchestrator Conditions.

## Claim Boundary

This work order authorizes only a no-commit worker-return lane for a
documentation-only `riskTriggers` field patch in the ASSF package contract. It
does not authorize AGSK-T5 package candidate creation, AGSK-T6 checker work,
registry/generated index mutation, runtime activation, automatic skill
invocation, CLI/MCP adapter implementation, provider/live proof, public-sync,
session-sync, production readiness, or worker commit.
