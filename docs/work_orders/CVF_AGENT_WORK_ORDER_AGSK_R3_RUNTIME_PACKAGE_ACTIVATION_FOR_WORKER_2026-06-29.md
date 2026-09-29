# CVF Agent Work Order - AGSK-R3 Runtime And Package Activation For Worker

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-29

docType: work_order

Batch ID: AGSK-R3

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: 3e53eba5

## Dispatch Prompt Envelope

Role: no-commit worker for AGSK-R3 runtime/package activation opening. Codex
remains reviewer/closer.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_R3_RUNTIME_PACKAGE_ACTIVATION_FOR_WORKER_2026-06-29.md`.

Paired GC-018 baseline:
`docs/baselines/CVF_GC018_AGSK_R3_RUNTIME_PACKAGE_ACTIVATION_2026-06-29.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

Base: capture `executionBaseHead` with `git rev-parse --short HEAD` before
edits.

Current-time notes: current date is 2026-06-29. AGSK-R2 closed at material
commit `50689173` with 24 upstream `skills/*/SKILL.md` packages represented as
metadata-only `CANDIDATE` registry entries and the generated ASSF skill index
regenerated. This dispatch opens package activation enablement only.

Mission summary: use AGSK-R2's 24 upstream `skills/*/SKILL.md` metadata-only
`CANDIDATE` entries and regenerated generated index as the input set. Create a
source-verified package activation readiness packet, package-root proposals,
optional `PROPOSED` registry source updates, regenerated generated index, and a
worker return. Do not set any package to `APPROVED` or `ACTIVE`.

Do-not-misread notes: this work order opens package activation enablement, not
runtime execution. Runtime resolver activation, automatic skill invocation,
CLI/MCP adapter behavior, provider/live proof, public-sync, and production
readiness remain forbidden.

Required first actions: read this work order, paired GC-018 baseline, AGSK-R2
review, ASSF package contract, ASSF composition contract, registry README,
active session front door/state/handoff, guard orientation, and literal-format
gotchas; capture `executionBaseHead`; record `git status --short`; run the
pre-flight checks before edits.

Return contract: return `COMPLETE_PENDING_REVIEW`,
`COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, or `BLOCKED_WITH_REASON` with
actual changed paths, executionBaseHead, source verification, 24-candidate
coverage, generated-index drift proof, and no worker commit.

## Purpose

Execute the first governed AGSK package-activation enablement tranche after
AGSK-R2. The worker turns metadata-only candidates into CVF-owned package-root
proposals and bounded lifecycle source-state evidence, while keeping runtime
activation behind later reviewer/UAT authorization.

## 1. Mission

For the 24 AGSK-R2 upstream skill candidates, create source-verified activation
readiness evidence and package-root proposals. If a candidate has enough source
evidence and a CVF adaptation can be written safely, create:

- `docs/reference/agent_system_skills/packages/<skill-id>/SKILL.md`;
- `docs/reference/agent_system_skills/packages/<skill-id>/skill.source.json`;
- a matching registry source update from `CANDIDATE` to `PROPOSED`;
- a regenerated generated ASSF skill index.

If a candidate is not ready, leave its registry entry at `CANDIDATE` and record
the source-backed blocker in the worker return.

## 2. Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Operator instruction | chat request on 2026-06-29 to open runtime/package activation for the 24 upstream skills converted in AGSK-R2 | authorizes AGSK-R3 opening |
| Active session front door | `CVF_SESSION_MEMORY.md` | startup and next-move source |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | current generated session state |
| Active handoff | `AGENT_HANDOFF_V27_2026-06-29.md` | current handoff named by state registry |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_AGSK_R3_RUNTIME_PACKAGE_ACTIVATION_2026-06-29.md` | dispatch baseline |
| AGSK-R2 review | `docs/reviews/CVF_AGSK_R2_AGENT_SKILLS_SOURCE_MIRROR_FULL_PACKAGE_BACKFILL_2026-06-29.md` | 24 upstream package candidate inventory |
| Source mirror index | `.private_reference/source_mirrors/INDEX.md` | pinned upstream source authority |
| ASSF package contract | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | package topology, schema, lifecycle vocabulary |
| ASSF composition contract | `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md` | no-self-activation invariant |
| ASSF registry README | `docs/reference/agent_system_skills/registry/README.md` | source entries and generated index flow |
| ASSF generator | `governance/compat/generate_assf_skill_index.py` | generated index regeneration |
| ASSF resolver | `governance/compat/run_assf_skill_resolver.py` | read-only metadata resolver boundary |

Authority boundary:

- AGSK-R2 metadata candidate entries are the starting set, not activation proof.
- Upstream `SKILL.md` files are source evidence; CVF package roots must be
  adapted and bounded by CVF authority.
- This work order does not authorize `APPROVED`, `ACTIVE`, runtime resolver
  mutation, or execution.

## 3. Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | authors AGSK-R3 baseline and work order |
| Worker | assigned no-commit worker agent | creates package-root proposals, bounded registry updates, generated index, and worker return |
| Reviewer/closer | Codex | validates worker return, repairs allowed-scope defects, and commits only if accepted |
| Operator approval required | operator | any lifecycle state above `PROPOSED`, runtime resolver mutation, CLI/MCP adapter, provider/live proof, public-sync, or production claim |

## 4. Scope

Allowed scope:

- read all first-read files and the 24 upstream `SKILL.md` files under
  `.private_reference/source_mirrors/addyosmani__agent-skills/skills/`;
- create package-root proposal folders under
  `docs/reference/agent_system_skills/packages/<skill-id>/` for AGSK-R2
  candidates only;
- write CVF-adapted `SKILL.md` and `skill.source.json` files for those package
  roots;
- update only the 24 AGSK-R2 registry entries from `CANDIDATE` to `PROPOSED`
  when the matching package root exists and is source-verified;
- append worker-return evidence to
  `docs/reviews/CVF_AGSK_R3_RUNTIME_PACKAGE_ACTIVATION_WORKER_RETURN_2026-06-29.md`;
- regenerate `docs/reference/agent_system_skills/generated/skill-index.json`
  with the existing generator;
- run source-verification searches, JSON parsing, generated-index drift checks,
  resolver smoke checks, worker-return fast gate, and reviewer-fast gate.

Forbidden scope:

- setting any package or registry field to `APPROVED`, `ACTIVE`, `PASSED`, or
  `CERTIFIED`;
- editing `governance/compat/*.py`, hooks, tests, resolver source, generator
  source, Web/runtime source, provider/live paths, public-sync files,
  `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, or handoff files;
- creating external CLI/MCP adapter behavior;
- copying upstream package text as CVF runtime authority without adaptation;
- running providers, browser automation, package execution, shell hooks,
  installs, benchmarks, public export, or push;
- editing non-AGSK-R2 ASSF registry entries except through generated aggregate
  regeneration.

Risk ceiling: R1 documentation/package-root proposal and metadata source-state
work. Any runtime behavior or external action is out of scope.

## Scope / Target / Owner Boundary

Target: AGSK-R2's 24 upstream skill candidates, their package-root proposal
surfaces, matching registry entries, regenerated index, and one worker-return
packet.

Owner boundary:

- worker owns only allowed-scope files and must not commit;
- reviewer owns acceptance, material commit, and any later session sync;
- operator owns any scope expansion or runtime activation decision.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch-authoring`, role=`dispatcher`,
lifecyclePhase=`pre-dispatch`, surfaceSelector=`docs/work_orders`,
riskCeiling=`HIGH`, maxResults=`20`

Returned defects: NONE_RETURNED

Disclosure note: the read-only ADIF resolver returned no matching defects for
this work-order authoring query.

## 5. Required First Reads

Before editing, read:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V27_2026-06-29.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- `docs/baselines/CVF_GC018_AGSK_R3_RUNTIME_PACKAGE_ACTIVATION_2026-06-29.md`
- this work order
- `docs/reviews/CVF_AGSK_R2_AGENT_SKILLS_SOURCE_MIRROR_FULL_PACKAGE_BACKFILL_2026-06-29.md`
- `.private_reference/source_mirrors/INDEX.md`
- all 24 upstream `SKILL.md` files under `.private_reference/source_mirrors/addyosmani__agent-skills/skills/`
- all 24 matching registry entries under `docs/reference/agent_system_skills/registry/entries/`
- `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`
- `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md`
- `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md`
- `docs/reference/agent_system_skills/registry/README.md`
- `governance/compat/generate_assf_skill_index.py`
- `governance/compat/check_assf_skill_index_drift.py`
- `governance/compat/check_assf_package_candidate_anatomy.py`
- `governance/compat/run_assf_skill_resolver.py`

## 6. Pre-Flight Checks

Run before implementation:

```powershell
git rev-parse --short HEAD
git status --short
Test-Path docs/reference/agent_system_skills/packages
Get-ChildItem -LiteralPath ".private_reference/source_mirrors/addyosmani__agent-skills/skills" -Directory | Measure-Object
python governance/compat/check_assf_skill_index_drift.py
python governance/compat/check_assf_package_candidate_anatomy.py --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

Expected results:

- executionBaseHead and worktree state are recorded;
- source mirror skill directory count is 24;
- generated index starts in sync;
- package candidate anatomy starts PASS;
- pre-implementation gate passes or allowed-scope failures are repaired.

## 6A. Source-Fidelity Pass

### Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| AGSK-R2 package inventory contains 24 upstream `skills/*/SKILL.md` candidates | `docs/reviews/CVF_AGSK_R2_AGENT_SKILLS_SOURCE_MIRROR_FULL_PACKAGE_BACKFILL_2026-06-29.md` | Upstream Skill Package Backfill Ledger | `24 upstream skills/*/SKILL.md` | AGSK-R2 review | VALUE_SET | ACCEPT |
| AGSK-R2 generated index owner is `docs/reference/agent_system_skills/generated/skill-index.json` | `docs/reviews/CVF_AGSK_R2_AGENT_SKILLS_SOURCE_MIRROR_FULL_PACKAGE_BACKFILL_2026-06-29.md` | Owner-Surface Map; Machine Closure Package | `docs/reference/agent_system_skills/generated/skill-index.json` | AGSK-R2 review | VALUE_SET | ACCEPT |
| `CANDIDATE` is not active package state | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Package lifecycle states | `CANDIDATE` | ASSF package contract | VALUE_SET | ACCEPT |
| package topology permits future `packages/<skill-id>/SKILL.md` and `skill.source.json` | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Storage Topology | `packages/<skill-id>/SKILL.md`; `skill.source.json` | ASSF package contract | DOC_ONLY_NEW | ACCEPT |
| no process may set `APPROVED` or `ACTIVE` without reviewer decision and UAT path | `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md` | No-Self-Activation Invariant | `APPROVED`; `ACTIVE`; `UAT` | ASSF composition contract | LITERAL_INVARIANT | ACCEPT |
| registry sources are authoritative and generated index must not be hand-edited | `docs/reference/agent_system_skills/registry/README.md` | Purpose; Adding A New Entry | `entries`; `generate_assf_skill_index.py --generate` | ASSF registry source family | LITERAL_INVARIANT | ACCEPT |
| generator writes generated index from registry entries | `governance/compat/generate_assf_skill_index.py` | `generate_index` | `generate_index` | ASSF index generator | EXISTS | ACCEPT |
| generated-index drift checker is available | `governance/compat/check_assf_skill_index_drift.py` | module | `check` | ASSF drift checker | EXISTS | ACCEPT |
| resolver is read-only metadata and not activation evidence | `governance/compat/run_assf_skill_resolver.py` | module docstring; `resolve_skill_packet` | `resolve_skill_packet` | ASSF resolver | RUNTIME_BEHAVIOR | ACCEPT |
| AGSK activation resolver runtime is conditionally parked | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md` | Candidate Index | `AGSK-activation-resolver-runtime` | external absorption reopen index | VALUE_SET | ACCEPT |

### Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`; `docs/reference/agent_system_skills/CVF_ASSF_COMPOSITION_CONTROL_CONTRACT.md`; `docs/reference/agent_system_skills/registry/README.md`; `governance/compat/generate_assf_skill_index.py`; `governance/compat/run_assf_skill_resolver.py` |
| Package roots at dispatch | N/A with reason: package-root proposals are AGSK-R3 output, not existing source authority |
| Existing candidates | AGSK-R2 review records 24 upstream metadata candidates |
| Runtime behavior claimed | N/A_WITH_REASON: no runtime resolver source mutation or package execution is authorized |
| Live/provider proof claimed | N/A_WITH_REASON: no provider/API/model behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized |

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake route | operator-directed AGSK-R3 package activation enablement dispatch |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | dispatcher -> no-commit worker -> reviewer/closer |
| scope classification | package-root proposal and metadata lifecycle source-state update |
| risk sensitivity | R1; runtime, provider, public, and external adapter work are forbidden |
| escalation condition | escalate for lifecycle state above `PROPOSED`, runtime resolver mutation, external adapter behavior, provider/live proof, public-sync, or non-target registry/source changes |
| Dispatcher role | Codex dispatcher |
| Worker route | `WORKER_MUST_NOT_COMMIT` |
| Reviewer/closer route | Codex reviewer/closer after worker return is accepted |
| Runtime route | `DEFERRED_WITH_REASON`: no runtime resolver mutation or package execution in AGSK-R3 |
| External-agent route | `DEFERRED_WITH_REASON`: no CLI/MCP adapter behavior in AGSK-R3 |

### Negative Search And Collision Discipline

| Search target | Required command | Required result | Action if collision appears |
|---|---|---|---|
| package root base | `Test-Path docs/reference/agent_system_skills/packages` | record actual state | if present, enumerate and avoid overwriting non-AGSK-R3 paths |
| each package root | `Test-Path docs/reference/agent_system_skills/packages/<skill-id>` | absent before create, or same AGSK-R3-owned path after create | block on pre-existing non-owned package root |
| registry target set | JSON read of 24 AGSK-R2 entries | only 24 matching entries updated | revert or block any non-target registry edit |
| lifecycle ceiling | JSON read after edits | no `APPROVED`, `ACTIVE`, `PASSED`, or `CERTIFIED` values | repair before return |

## 6B. Roadmap-To-Work-Order Trace Matrix

| Roadmap or review requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| AGSK-R2 converted 24 upstream skills into metadata candidates | Mission; Source Verification | 24-candidate activation coverage table | compare AGSK-R2 ledger with worker return | PASS |
| AGSK runtime/package activation remained parked after AGSK-R2 | Scope; Forbidden scope; Conditional reopen handling | worker return activation boundary | inspect worker return claim boundary | PASS |
| ASSF package contract defines package-root topology | Allowed scope; Source Verification | package-root proposal files | file existence and source readback | PASS |
| generated ASSF skill index must be regenerated from sources | Allowed scope; Evidence Requirements | generated index | generator output and drift check | PASS |
| no direct runtime activation is allowed | Forbidden scope; Claim Boundary | no resolver/runtime source changed | `git diff --name-status` | PASS |

## 6C. Worker Autonomy / No-Question Rule

The worker proceeds without operator confirmation for non-destructive actions
inside Allowed scope, including file reads, package-root proposal authoring,
registry metadata edits within the 24-entry target set, generator execution,
gate remediation inside scope, and worker-return completion.

Escalate only for lifecycle state above `PROPOSED`, resolver/runtime mutation,
CLI/MCP adapter behavior, provider/live proof, public-sync, session-state
edits, destructive actions, or non-target registry/source changes.

## 7. Write Ownership

Owned files or modules:

- `docs/reference/agent_system_skills/packages/<24 target skill ids>/`
- the 24 AGSK-R2 registry entry files listed by the worker's coverage table
- `docs/reference/agent_system_skills/generated/skill-index.json`
- `docs/reviews/CVF_AGSK_R3_RUNTIME_PACKAGE_ACTIVATION_WORKER_RETURN_2026-06-29.md`

Forbidden paths:

- all `governance/compat/*.py` files;
- `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, and `AGENT_HANDOFF*.md`;
- Web/runtime/provider/live/public-sync paths;
- `.private_reference/source_mirrors/**` edits;
- non-AGSK-R2 registry entries except generated aggregate output.

Write mode: create package roots, modify-listed registry entries, regenerate
generated index, and create worker return.

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | dispatcher authors; no-commit worker executes; reviewer/closer accepts and commits |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE |
| baseHeadFor(phase) | dispatchBaseHead=`3e53eba5`; executionBaseHead=captured by worker; closureBaseHead=captured by reviewer |
| changedSetScope(phase) | dispatch changes baseline/work order only; execution changes package proposals, target registry entries, generated index, worker return; closure commits accepted material only |
| traceScope(phase, actor) | dispatcher AOT in this work order; worker AOT in worker return; reviewer AOT in closure evidence |
| commitOwner(phase) | dispatcher may commit dispatch; worker must not commit; reviewer/closer owns material commit |
| crossBatchIsolation | worker starts from current clean worktree or records pre-existing dirty paths and does not edit them |
| nextMoveSurfaces | session-sync surfaces are reviewer-owned only when an accepted AGSK-R3 material commit exists |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_AGSK_R3_RUNTIME_PACKAGE_ACTIVATION_COMPLETION_2026-06-29.md` |
| reviewerOwnedClosurePaths | package-root proposals, target registry entries, generated index, worker return, and optional completion review if created by reviewer |

## 8. Execution Plan

| Step | Action | Output | Stop condition |
|---|---|---|---|
| 1 | Capture `executionBaseHead`, status, and pre-flight checks | worker return pre-flight evidence | stop if source mirror or registry is unreadable |
| 2 | Build 24-candidate coverage table from AGSK-R2 ledger and registry sources | coverage table | stop if any candidate mapping is missing |
| 3 | For each candidate, read upstream `SKILL.md` and write CVF-adapted package-root proposal when safe | package `SKILL.md` and `skill.source.json` | leave candidate at `CANDIDATE` if adaptation is blocked |
| 4 | Update matching registry source to `PROPOSED` only for candidates with package roots | registry source diff | stop if lifecycle ceiling would be exceeded |
| 5 | Run generator and drift/anatomy checks | generated index and PASS evidence | repair inside scope or return blocked |
| 6 | Write worker return with evidence and claim boundary | worker return | stop if worker-return fast gate cannot pass inside scope |

## Work-Order Fulfillment Manifest

| Required output | Path or evidence | Owner | Status |
|---|---|---|---|
| Worker return | `docs/reviews/CVF_AGSK_R3_RUNTIME_PACKAGE_ACTIVATION_WORKER_RETURN_2026-06-29.md` | worker | REQUIRED |
| Package-root proposal set | `docs/reference/agent_system_skills/packages/<skill-id>/` | worker | REQUIRED unless candidate blocked with reason |
| Target registry source updates | 24 AGSK-R2 registry entries | worker | REQUIRED for package-root proposals only |
| Generated index | `docs/reference/agent_system_skills/generated/skill-index.json` | worker via generator | REQUIRED if any registry entry changes |
| Runtime activation decision | worker return conditional reopen handling | worker | REQUIRED, no code mutation |

## Required Artifact Manifest

| Artifact | Path | Required literal | Required at handoff |
|---|---|---|---|
| Dispatch baseline | `docs/baselines/CVF_GC018_AGSK_R3_RUNTIME_PACKAGE_ACTIVATION_2026-06-29.md` | `Status: PROPOSED` | Yes |
| Dispatch work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_R3_RUNTIME_PACKAGE_ACTIVATION_FOR_WORKER_2026-06-29.md` | `Status: DISPATCH_READY` | Yes |
| Worker return | `docs/reviews/CVF_AGSK_R3_RUNTIME_PACKAGE_ACTIVATION_WORKER_RETURN_2026-06-29.md` | `Status: COMPLETE_PENDING_REVIEW` | Yes |
| Package roots | `docs/reference/agent_system_skills/packages/` | `Status: PROPOSED` | Yes |
| Registry entries | `docs/reference/agent_system_skills/registry/entries/` | `PROPOSED` | Yes |
| Generated skill index | `docs/reference/agent_system_skills/generated/skill-index.json` | generated index in sync with registry | Yes |

## Required Proof Manifest

| Proof | Path | Required literal | Required at handoff |
|---|---|---|---|
| Dispatch status | `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_R3_RUNTIME_PACKAGE_ACTIVATION_FOR_WORKER_2026-06-29.md` | `DISPATCH_READY` | Yes |
| Commit mode | `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_R3_RUNTIME_PACKAGE_ACTIVATION_FOR_WORKER_2026-06-29.md` | `WORKER_MUST_NOT_COMMIT` | Yes |
| Lifecycle ceiling in worker return | `docs/reviews/CVF_AGSK_R3_RUNTIME_PACKAGE_ACTIVATION_WORKER_RETURN_2026-06-29.md` | `PROPOSED` | Yes |
| Approved-state prohibition | `docs/reviews/CVF_AGSK_R3_RUNTIME_PACKAGE_ACTIVATION_WORKER_RETURN_2026-06-29.md` | `APPROVED` | Yes |
| Active-state prohibition | `docs/reviews/CVF_AGSK_R3_RUNTIME_PACKAGE_ACTIVATION_WORKER_RETURN_2026-06-29.md` | `ACTIVE` | Yes |
| Drift proof | `docs/reviews/CVF_AGSK_R3_RUNTIME_PACKAGE_ACTIVATION_WORKER_RETURN_2026-06-29.md` | `python governance/compat/check_assf_skill_index_drift.py` PASS | Yes |

## Worker Return Packet Shape Contract

Create:

`docs/reviews/CVF_AGSK_R3_RUNTIME_PACKAGE_ACTIVATION_WORKER_RETURN_2026-06-29.md`

Required sections:

- Purpose
- Target / Source
- Scope / Methodology
- Findings / Position
- Risk / Corrective Action
- Worker Status
- Source Inventory
- Source Verification Block
- executionBaseHead
- git status --short
- 24-Candidate Package Activation Coverage Table
- Package Root Proposal Evidence
- Registry Source-State Update Evidence
- Generated Index Drift Proof
- Resolver Runtime Activation Boundary
- Current Runtime Freshness Verification
- Corpus Completeness And Report Integrity
- External Knowledge Intake Routing
- Rescan Intelligence Hardening
- Conditional Reopen Index Handling
- Finding-To-Governance Learning Disposition
- Epistemic Process Block
- Delta Execution Claim Boundary Control Block
- Agent Operation Trace Block
- Machine Closure Package
- Public Export Disposition
- Claim Boundary

Required status token: `COMPLETE_PENDING_REVIEW`,
`COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, or `BLOCKED_WITH_REASON`.

Conditional blocks that do not apply must remain present with `N/A with reason`
or `NOT_APPLICABLE_WITH_REASON`; do not omit them.

## Evidence Requirements

| Evidence | Required result |
|---|---|
| `git rev-parse --short HEAD` | executionBaseHead recorded |
| `git status --short` | actual pending paths recorded |
| 24 upstream source reads | every source path accounted |
| JSON parse/readback | registry lifecycle ceiling verified |
| `python governance/compat/generate_assf_skill_index.py --generate` | generated index updated when registry entries change |
| `python governance/compat/check_assf_skill_index_drift.py` | PASS |
| `python governance/compat/check_assf_package_candidate_anatomy.py --enforce` | PASS after registry edits |
| `python governance/compat/run_worker_return_fast_gate.py` | PASS or blocker recorded |

## Acceptance Criteria

| ID | Criterion | Required evidence |
|---|---|---|
| AC1 | All 24 AGSK-R2 upstream skill candidates are accounted | coverage table with terminal disposition for each candidate |
| AC2 | Package-root proposals are CVF-adapted and source-verified | package files plus source inventory |
| AC3 | Registry updates stop at `PROPOSED` and do not claim UAT/certification | JSON readback |
| AC4 | Generated index matches sources | generator and drift PASS |
| AC5 | Runtime resolver activation remains a blocked follow-on | worker return boundary and no resolver source diff |

Fail conditions:

| Condition | Required action |
|---|---|
| Any candidate needs `APPROVED`, `ACTIVE`, provider/live proof, CLI/MCP, or resolver mutation | return `BLOCKED_WITH_REASON` for that candidate |
| Package root would copy upstream authority without CVF adaptation | leave candidate at `CANDIDATE` and record blocker |
| Non-target registry entry must be edited | stop and return to orchestrator |
| Generated index or anatomy checker fails outside allowed scope | return blocked |

## Review Gate

Implementation may proceed only after:

- this work order and paired GC-018 are present;
- pre-implementation autorun passes on the worker execution range.

Worker handoff is not closure. The reviewer/closer must inspect the worker
return, verify changed files, rerun gates, and commit only accepted material.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | source mirror -> AGSK-R2 candidate backfill -> AGSK-R3 package-root proposal and metadata lifecycle source-state update |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_source_mirror_migration.py` |
| Owner surface | ASSF package roots, registry entries, generated index, and worker return |
| Disposition | ADAPT upstream skill package fronts into CVF-owned package proposals |
| Claim boundary | no runtime execution, CLI/MCP adapter, provider/live proof, public-sync, or production claim |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | ASSF package-root proposals and generated metadata | internal agents may review proposed packages after reviewer acceptance; no execution authority is granted | package files, registry source-state evidence, generated-index drift proof | no runtime loader or resolver source mutation in AGSK-R3 | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future adapter readout | external agents have no mutation, activation, or execution authority in AGSK-R3 | external fields remain deferred | separate adapter work order required | `DEFERRED_WITH_REASON` |

## Finding-To-Governance Learning Disposition

| Field | Required worker value |
|---|---|
| Defect class | `VALUE_CONVERSION_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Disposition | `PACKAGE_ROOT_PROPOSALS_CREATED_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| Runtime/provider/cost lane | `N/A_WITH_REASON` |
| Next control action | state whether a later runtime resolver activation tranche is eligible after reviewer outcome |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: The 24 AGSK-R2 metadata-only candidates can be
source-verified for package-root proposal work, but they cannot be safely moved
to `ACTIVE` or runtime resolver behavior in this tranche.

Evidence Comparison Requirement: worker return compares actual package-root and
registry outcomes against all 24 planned candidates.

Contradiction Handling Requirement: if a candidate lacks enough source support,
leave it at `CANDIDATE` and record the contradiction or gap.

Claim Update Requirement: worker return records whether package activation
enablement is confirmed, narrowed, or blocked.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | AGSK-R3 package activation enablement work order |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT - worker must provide source reads, package-root evidence, registry readback, generated-index drift proof, and gate results |
| actionEvidence | ACTION_EVIDENCE_PRESENT - worker must provide package proposal files, bounded registry updates, generated index, and worker return |
| invocationBoundary | governed local package proposal and metadata editing only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, Web, or runtime interception claim |
| claimLanguage | create package-root proposals and bounded `PROPOSED` metadata updates for AGSK-R2 candidates |
| forbiddenExpansion | no `APPROVED` or `ACTIVE` state, resolver source mutation, runtime behavior, package execution, automatic invocation, CLI/MCP adapter, provider/live proof, public-sync, push, session sync, or production-readiness claim |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher |
| Provider or surface | local workspace |
| Session or invocation | AGSK-R3 work order authoring, 2026-06-29 |
| Working directory | repository root |
| Command or tool surface | PowerShell reads, rg searches, apply_patch |
| Target paths | paired GC-018 baseline and this work order |
| Allowed scope source | operator request to open runtime/package activation for the 24 AGSK-R2 upstream skill candidates |
| Before status evidence | clean worktree at HEAD `3e53eba5` |
| After status evidence | dispatch artifacts pending gate/commit |
| Diff evidence | `git diff --name-status` before dispatch closure |
| Approval boundary | dispatch authoring only; no AGSK-R3 execution by dispatcher |
| Claim boundary | repo-local trace only; no runtime/provider/public claim |
| Agent type | dispatcher |
| Invocation ID | `agsk-r3-runtime-package-activation-work-order-2026-06-29` |
| Expected manifest | this work order plus paired GC-018 baseline |
| Actual changed set | this work order plus paired GC-018 baseline |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this work order cites private source mirror and private provenance
metadata. Public-safe publication requires separate redaction and public-sync
authorization.

## Closure Checklist

| Checklist item | Required disposition |
|---|---|
| Acceptance criteria satisfied | reviewer verifies after worker return |
| Required evidence commands run | worker records command/result/path evidence |
| Commit mode recorded | `WORKER_MUST_NOT_COMMIT` |
| Changed files inside Allowed scope | reviewer verifies with `git diff --name-status` |
| Generator used | worker records command/result evidence |
| Drift checker passes | worker records PASS or blocker |
| Anatomy checker passes | worker records PASS or blocker |
| Worker return fast gate | worker runs or records blocker |
| Runtime activation boundary | no resolver source mutation and no `ACTIVE` lifecycle state |
| Public export disposition | `DEFERRED_PRIVATE_ONLY` |

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` without continuing if:

- pre-implementation autorun fails outside Allowed scope;
- any of the 24 source mirror skills or matching registry entries cannot be
  read;
- package-root adaptation would require direct upstream runtime import;
- lifecycle state above `PROPOSED` is needed;
- resolver/runtime source mutation is needed;
- generated index or anatomy checks fail and cannot be repaired inside scope;
- public-sync, provider/live proof, CLI/MCP adapter, session-sync, or
  production claim becomes necessary.

## Operator Checkpoint

Operator approval is already recorded for opening this package-activation
enablement lane. A new operator checkpoint is required before any runtime
resolver mutation, automatic invocation, `APPROVED`/`ACTIVE` lifecycle state,
CLI/MCP adapter behavior, provider/live proof, public-sync, or production
readiness claim.

## Claim Boundary

This work order authorizes only no-commit package activation enablement:
package-root proposals, bounded `PROPOSED` registry source updates, generated
ASSF skill index regeneration, and worker-return evidence. It does not
authorize runtime activation, package execution, automatic skill invocation,
external adapter implementation, provider/live proof, public-sync, session
sync, production readiness, or worker commit.
