# CVF Agent Work Order: ASSF Web Projection Implementation

Memory class: FULL_RECORD
Status: CLOSED_PASS_BOUNDED
Date: 2026-06-26
docType: work_order
Batch ID: ASSF-WEBPROJ-T1
dispatchBaseHead: cf50a81f
executionBaseHead: cf50a81f
closureBaseHead: cf50a81f
Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Codex single-agent multi-role worker/reviewer/closer for a bounded Web
projection implementation tranche.

executionBaseHead: `cf50a81f`

Required first actions: read the paired GC-018 baseline, read all Required
First Reads, run the pre-flight checks, and stop before any forbidden package,
adapter, provider, public-sync, or ASSF registry/index/resolver mutation.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_WEB_PROJECTION_IMPLEMENTATION_FOR_CODEX_2026-06-26.md`

Paired GC-018 baseline:
`docs/baselines/CVF_GC018_ASSF_WEB_PROJECTION_IMPLEMENTATION_2026-06-26.md`

Commit mode: `WORKER_MUST_NOT_COMMIT` for worker execution. Codex may later
review, repair allowed-scope defects, close, and commit as reviewer/closer only
once worker-return and gates pass.

Current-time notes: active handoff is `AGENT_HANDOFF_V23_2026-06-26.md`;
current HEAD before dispatch authoring is `cf50a81f`; this packet authorizes
implementation work-order dispatch only, not implementation before this packet
is committed.

Do-not-misread notes: implementation means bounded Web source and generated
Web public-index changes inside Write Ownership only; no ASSF registry,
generated-index source, resolver, package instance, certification decision,
CLI/MCP adapter, provider/live proof, public-sync, push, activation, package
execution, or session-sync is authorized in the material implementation range.

Return contract: produce a worker return and completion review. Return
`BLOCKED_WITH_REASON` if implementation requires forbidden mutation or cannot
preserve the claim boundary.

## Purpose

Implement read-only projection of certified ASSF package metadata into the CVF
Web skill index, following the ASSF-WEBPROJ-T0 decision review. The work must
keep ASSF certification state separate from Web corpus governance state and
must preserve the no-activation and adapter-separation invariants.

## Scope / Target / Owner Boundary

Target: Web read-model, generator, generated public index, display, tests,
worker return, and completion review for ASSF Web projection.

Owner boundary: the worker may edit only the Write Ownership paths in this work
order. The worker must not mutate ASSF registry source, ASSF generated-index
source, resolver source, package roots, package lifecycle state, adapter
surfaces, provider/live proof surfaces, public-sync surfaces, or session
surfaces in the material execution commit.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator next move | open ASSF Web projection implementation GC-018 and source-verified work order | ACCEPT |
| Active front door | `CVF_SESSION_MEMORY.md` | ACCEPT |
| Bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | ACCEPT |
| Active state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V23_2026-06-26.md` | ACCEPT |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_ASSF_WEB_PROJECTION_IMPLEMENTATION_2026-06-26.md` | ACCEPT |
| T0 decision review | `docs/reviews/CVF_ASSF_WEB_PROJECTION_SCHEMA_MAPPING_DECISION_2026-06-26.md` | ACCEPT |
| T0 completion review | `docs/reviews/CVF_ASSF_WEB_PROJECTION_SCHEMA_MAPPING_DECISION_COMPLETION_2026-06-26.md` | ACCEPT |
| Web projection contract | `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | ACCEPT |
| Lifecycle guard contract | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | ACCEPT |

## Agent Roles

| Role | Owner |
|---|---|
| Operator | approves next-move lane and later scope expansion |
| Dispatcher | Codex |
| Worker | Codex, no commit during worker execution |
| Reviewer | Codex once worker return exists |
| Closer | Codex once reviewer acceptance is recorded |
| Session-sync steward | Codex in a separate commit if next move changes |

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | active next allowed move from ASSF-WEBPROJ-T0 completion at material commit `a408c13e` |
| Scope classification | bounded Web implementation work order |
| Intake role | Codex dispatches; Codex worker executes without commit |
| Reviewer role | Codex reviewer/closer validates worker return, gates, changed paths, and boundaries |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; single-agent multi-role with reviewer closure conversion |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `SINGLE_AGENT_MULTI_ROLE` |
| selected role route | Codex dispatch author to Codex no-commit worker to Codex reviewer/closer |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if implementation requires ASSF registry/index/resolver mutation, package lifecycle mutation, adapter behavior, provider/live proof, public-sync, push, package activation, or package execution |

## Required First Reads

| Source | Action | Reason |
|---|---|---|
| `CVF_SESSION_MEMORY.md` | READ | active front door |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ | compact startup facts |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ | active state registry |
| `AGENT_HANDOFF_V23_2026-06-26.md` | READ | active handoff |
| `docs/reference/guard_orientation/README.md` | READ | role and guard orientation |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ | literal-format checklist |
| `docs/baselines/CVF_GC018_ASSF_WEB_PROJECTION_IMPLEMENTATION_2026-06-26.md` | READ | paired authorization baseline |
| `docs/reviews/CVF_ASSF_WEB_PROJECTION_SCHEMA_MAPPING_DECISION_2026-06-26.md` | READ | implementation decision evidence |
| `docs/reviews/CVF_ASSF_WEB_PROJECTION_SCHEMA_MAPPING_DECISION_COMPLETION_2026-06-26.md` | READ | closure recommendation evidence |
| `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | READ | canonical projection boundary |
| `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | READ | bridge preconditions |
| `docs/reference/agent_system_skills/generated/skill-index.json` | SOURCE_VERIFIED | ASSF metadata source |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | SOURCE_VERIFIED | generator invocation |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/scripts/build-skill-index.js` | SOURCE_VERIFIED | Web skill-index generator |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/types/skill.ts` | SOURCE_VERIFIED | Web read-model target |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SkillLibrary.tsx` | SOURCE_VERIFIED | Web library display |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SkillDetailView.tsx` | SOURCE_VERIFIED | Web detail display |

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/check_assf_skill_index_drift.py
python governance/compat/check_assf_certified_metadata_admission.py --require-certified
```

## Worker Return Packet Shape Contract

The worker-return artifact must be scaffold-first and must retain or complete
the sections listed below so reviewer-fast and pre-closure gates can diagnose
issues before material commit:

- `Status`
- `dispatchWorkOrder`
- `Purpose`
- `Source Inventory`
- `Scope / Methodology`
- `Findings / Position`
- `Risk / Corrective Action`
- `Claim Boundary`
- `Source Verification Block`
- `Agent Operation Trace Block`
- `Delta Execution Claim Boundary Control Block`
- `Public Export Disposition`
- `External Knowledge Intake Routing`
- `Rescan Intelligence Hardening`
- `Corpus Completeness And Report Integrity`
- `Finding-To-Governance Learning Disposition`
- `Epistemic Process Block`
- `Worker Return Scaffold Effectiveness Measurement`
- `Machine Closure Package`
- `Acceptance Receipt Assertion Matrix`
- actual `executionBaseHead`
- actual `git status --short`
- `Actual changed set` listing real paths
- command evidence
- no commit statement

If a conditional section is not applicable, include the section with
`N/A with reason` or `NOT_APPLICABLE_WITH_REASON` and a short reason instead
of omitting it. The worker return must include
`receiptEvidence: CVF_RECEIPT_PRESENT - ...` when execution produced local
command or diff evidence.

## Worker Autonomy / No-Question Rule

Within Allowed scope, the worker must repair machine-check, source-inventory,
packet-shape, focused-command, worker-return fast-gate, and allowed UI/test
failures and rerun the required checks without asking the operator. Ask the
operator only if remediation would exceed Allowed scope, change the claim
boundary, require ASSF registry/generated-index/resolver mutation, package
instance creation, lifecycle mutation, certification decision, CLI/MCP adapter
behavior, provider/live proof, public-sync, push, destructive action, or a
separate roadmap batch.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Web predev/prebuild scripts generate the skill index | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | lines 7-8 | `build-skill-index.js` | Web package scripts | RUNTIME_BEHAVIOR | ACCEPT |
| Web generator reads legacy skill roots and corpus governance | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/scripts/build-skill-index.js` | lines 8-12 and 277-280 | `buildSkillIndex` | Web skill-index generator | EXISTS | ACCEPT |
| Web generator builds current skill records | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/scripts/build-skill-index.js` | lines 337-364 | `skillRecord` | Web skill-index generator | EXISTS | ACCEPT |
| Web generator writes public skill index | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/scripts/build-skill-index.js` | lines 412-437 | `writeIndex` | Web skill-index generator | RUNTIME_BEHAVIOR | ACCEPT |
| Web `Skill` type is current target schema | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/types/skill.ts` | lines 7-34 | `Skill` | CVF Web Skill type | EXISTS | ACCEPT |
| Web `SkillIndexMeta` type is current meta schema | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/types/skill.ts` | lines 42-50 | `SkillIndexMeta` | CVF Web Skill index payload | EXISTS | ACCEPT |
| Web library loads public index before fallback | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SkillLibrary.tsx` | lines 23-44 | `SkillLibrary` | Web SkillLibrary component | EXISTS | ACCEPT |
| Web detail view renders skill metadata | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SkillDetailView.tsx` | lines 11-92 | `SkillDetailView` | Web SkillDetailView component | EXISTS | ACCEPT |
| Web front-door search reads public index | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/frontdoor-skills.ts` | lines 28-36 | `fetchFrontDoorSkillRecords` | Web front-door reader | EXISTS | ACCEPT |
| ASSF projection vocabulary is canonical | `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | lines 80-91 | `CERTIFIED_PACKAGE_PROJECTION` | ASSF Web projection contract | VALUE_SET | ACCEPT |
| Projection must not activate packages | `docs/reference/agent_system_skills/CVF_ASSF_WEB_PROJECTION_CONTRACT.md` | lines 113-128 | `frontDoorTier` | ASSF Web projection contract | LITERAL_INVARIANT | ACCEPT |
| Web bridge requires separate schema work | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | lines 176-184 | `certificationState` | ASSF lifecycle guard contract | LITERAL_INVARIANT | ACCEPT |
| ASSF generated index is metadata-only | `docs/reference/agent_system_skills/generated/skill-index.json` | lines 1-5 | `claimBoundary` | ASSF generated skill index | LITERAL_INVARIANT | ACCEPT |
| ASSF generated index carries certified package fields | `docs/reference/agent_system_skills/generated/skill-index.json` | lines 14-16 and 55-70 | `certificationState` | ASSF generated skill index | VALUE_SET | ACCEPT |
| ASSF generated index carries UAT pass state | `docs/reference/agent_system_skills/generated/skill-index.json` | lines 92-94 | `uatState` | ASSF generated skill index | VALUE_SET | ACCEPT |
| Existing Web test reads generated public index | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/skill-corpus-governance.test.ts` | lines 10-24 and 72-83 | `loadSkillIndex` | Web corpus governance tests | EXISTS | ACCEPT |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: this tranche does not absorb, reclassify, or claim
completion of legacy source families. It uses the existing Web generator and
legacy skill roots only as current Web data-production inputs.

| Field | Disposition |
|---|---|
| Coverage index applicability | NOT_APPLICABLE_WITH_REASON: no legacy absorption coverage update is authorized |
| Legacy source mutation | N/A with reason: no legacy skill-library source mutation is authorized |
| Owner surface | ASSF Web projection implementation work order |

## New Doc-Only Fields

| Field | Target surface | Purpose | Boundary |
|---|---|---|---|
| `assfProjectionClass` | Web `Skill` | projection classification | read-only display |
| `certificationState` | Web `Skill` | projected ASSF certification state | display only |
| `uatState` | Web `Skill` | projected ASSF UAT state | display only |
| `reviewArtifacts` | Web `Skill` | projected evidence paths | display/link only |
| `canonicalRoot` | Web `Skill` | source trace path | display trace only |
| `externalCliMcpDisposition` | Web `Skill` | adapter disposition | no adapter implementation |
| `adapterContract` | Web `Skill` | adapter contract text/path | display only |
| `projectionClaimBoundary` | Web `Skill` | no-activation/no-authority boundary | display only |
| `assfProjectedSkills` | Web `SkillIndexMeta` | ASSF projection count | informational |
| `certifiedPackageProjections` | Web `SkillIndexMeta` | certified projection count | informational |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

API invocation used: `resolve_defect_packet(task_class="Work-order authoring / dispatch", role="dispatcher", lifecycle_phase="pre-dispatch")`

Returned defects:

- ADIF-0001: Exhaustive directory claim omits actual children
- ADIF-0002: Provider-local interaction accepted as authority
- ADIF-0007: Gate marker in boundary prose triggers wrong evidence class
- ADIF-0006: Source Verification symbol cell contains a value/type

Remediation applied: use bounded manifests, CVF-governed/runtime sources only,
source symbols without value/type assignments, and explicit control blocks for
boundary language.

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | Codex dispatches, executes no-commit worker implementation, reviews, and closes if evidence supports closure |
| phase | DISPATCH_AUTHORING; IMPLEMENTATION; REVIEWER_CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=cf50a81f`; `executionBaseHead=cf50a81f`; closure base recorded in completion review |
| changedSetScope(phase) | dispatch packet first; later implementation/review paths only; session-sync separate |
| traceScope(phase, actor) | worker return and completion review record Agent Operation Trace Block |
| commitOwner(phase) | Codex reviewer/closer owns material commit once worker return passes gates |
| crossBatchIsolation | no ASSF registry/index/resolver, package, adapter, provider, public-sync, or session-sync mutation in worker material commit |
| Before status evidence | dispatchBaseHead `cf50a81f`; clean worktree evidence before dispatch authoring |
| nextMoveSurfaces | updated only in a separate session-sync commit paired to the accepted material commit |
| Closer designation | Codex reviewer/closer |

## Single-Agent Multi-Role Control Block

| Field | Control |
|---|---|
| Role separation ledger | dispatch packet, worker return, completion review, material commit, and session-sync are separate steps |
| Evidence basis | source verification, focused Web tests, generated index diff evidence, pre-closure gates, commit steward preflight |
| Self-review boundary | Codex may review its own worker return only against this work order and machine gates |
| Gate sequence | pre-dispatch for packet, pre-implementation for worker start, reviewer-fast/pre-closure for closure, session-sync gates only in the dedicated session-sync phase |
| Escalation conditions | any required ASSF registry/index/resolver mutation, package lifecycle mutation, adapter behavior, provider/live proof, public-sync, or push |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| workerReturnPath | `docs/reviews/CVF_ASSF_WEB_PROJECTION_IMPLEMENTATION_WORKER_RETURN_2026-06-26.md` |
| completionReviewPath | `docs/reviews/CVF_ASSF_WEB_PROJECTION_IMPLEMENTATION_COMPLETION_2026-06-26.md` |
| reviewerOwnedClosurePaths | worker return, completion review, and allowed implementation paths listed in Write Ownership |
| workerReturnStatus | `COMPLETE_PENDING_REVIEW` expected |
| closer | Codex |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | Web projected skill index and display components | internal agents may read display metadata; no package mutation, certification authority, activation, or instruction execution is granted | ASSF Web projection contract and this work order | no internal route activates a package | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future external adapter or programmatic readout | external agents cannot use Web projection as adapter, certification source, package executor, or mutation channel | adapter-separation invariant | adapter remains deferred; separate source-verified adapter work order required | `DEFERRED_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator next-move direction to governed GC-018/source-verified work order |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this work order |
| Disposition | no external material absorbed |
| Claim boundary | repository-local source and command evidence only |

## Roadmap-To-Work-Order Trace Matrix

| Requirement | Work-order instruction | Expected closure evidence | Disposition |
|---|---|---|---|
| Implement T0 decision | Required Outputs and Implementation Plan | worker return and completion review | PASS |
| Keep certification separate from corpus class | Implementation Requirements | tests and generated data diff | PASS |
| Use generator, not hand-edit only | Implementation Plan and Verification Commands | `node scripts/build-skill-index.js` evidence | PASS |
| Preserve adapter boundary | Dual Agent Surface Matrix and Claim Boundary | completion review | PASS |

## Execution Plan

1. Confirm startup sources, paired GC-018 baseline, T0 decision evidence, and
   Web/ASSF source inputs.
2. Run the pre-flight checks and record the actual `executionBaseHead`.
3. Extend the Web read model with optional ASSF projection fields and counters.
4. Extend the Web skill-index generator to read ASSF generated metadata and
   emit read-only certified package projection records.
5. Update Web display components only when projection metadata is present.
6. Regenerate `public/data/skills-index.json` by running the Web generator.
7. Add or update focused tests covering generator output, public-index loading,
   and UI display.
8. Create scaffold-first worker return, then reviewer completion review if the
   worker return is accepted.
9. Run verification commands, pre-closure gates, commit steward preflight, and
   `git diff --check` before any material commit.

## Evidence Requirements

| Evidence | Required form |
|---|---|
| Base evidence | actual `executionBaseHead`, `git status --short`, and changed-path list |
| Source verification | updated worker-return Source Inventory and Source Verification Block |
| Generated output | command evidence from `node scripts/build-skill-index.js` |
| Focused tests | command output for listed Web tests and `npm run check`, or exact blocker if unrelated |
| Governance gates | pre-closure autorun, reviewer-return commit steward, and `git diff --check` |
| Boundary evidence | explicit no ASSF registry/generated-index source/resolver, adapter, provider, public-sync, activation, or package execution claim |

## Acceptance Criteria

| Criterion | Required evidence |
|---|---|
| AC1 | Web `Skill` and `SkillIndexMeta` include optional ASSF projection fields without removing existing fields |
| AC2 | Web generator reads ASSF generated metadata and emits certified package projection records or bounded zero-match evidence |
| AC3 | Generated Web public skill index is updated only through the generator |
| AC4 | UI displays projected certification metadata only when present and keeps adapter/deferred boundary visible |
| AC5 | Focused Web tests, governance gates, and diff check pass or record allowed unrelated blockers |

## Review Gate

Reviewer closure requires:

- worker return status `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`;
- actual changed paths within Write Ownership only;
- generated Web public index changed only by the generator;
- no forbidden ASSF registry/generated-index source/resolver, adapter,
  provider/live, public-sync, push, activation, package execution, or
  session-sync mutation in the material range;
- completion review with Machine Closure Package and Acceptance Receipt
  Assertion Matrix;
- passing pre-closure autorun, reviewer-return commit steward preflight, and
  `git diff --check`.

## Closure Checklist

| Item | Closure disposition required |
|---|---|
| Source verification refreshed | PASS or BLOCKED_WITH_REASON |
| Web generator execution recorded | PASS or BLOCKED_WITH_REASON |
| Focused tests recorded | PASS, BLOCKED_WITH_REASON, or N/A with reason for unrelated blocker |
| Forbidden paths absent | PASS or BLOCKED_WITH_REASON |
| Worker return packet shape complete | PASS or BLOCKED_WITH_REASON |
| Completion review complete | PASS or BLOCKED_WITH_REASON |
| Material/session-sync separation preserved | PASS or BLOCKED_WITH_REASON |

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` when all implementation requirements are met,
evidence is recorded, and the worker has not committed. Return
`BLOCKED_WITH_REASON` if the work needs forbidden scope, cannot preserve the
claim boundary, or cannot produce deterministic local evidence.

## Operator Checkpoint

No operator checkpoint is required for allowed-scope repair, focused test
updates, or packet-shape remediation. A fresh operator checkpoint is required
before any package instance, certification decision, ASSF registry/generated-
index source mutation, resolver mutation, CLI/MCP adapter behavior,
provider/live proof, public-sync, push, activation, package execution, or
roadmap change outside this tranche.

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/types/skill.ts` | worker | may edit |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/scripts/build-skill-index.js` | worker | may edit |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/public/data/skills-index.json` | worker | generated output only |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SkillLibrary.tsx` | worker | may edit if list display needs projection badge |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SkillDetailView.tsx` | worker | may edit for detail projection display |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/__fixtures__/skills-index.fixture.json` | worker | may edit for focused tests |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SkillLibrary.test.tsx` | worker | may edit |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SkillDetailView.test.tsx` | worker | may edit |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/skill-corpus-governance.test.ts` | worker | may edit |
| `docs/reviews/CVF_ASSF_WEB_PROJECTION_IMPLEMENTATION_WORKER_RETURN_2026-06-26.md` | worker | create |
| `docs/reviews/CVF_ASSF_WEB_PROJECTION_IMPLEMENTATION_COMPLETION_2026-06-26.md` | reviewer/closer | create |

## Implementation Requirements

1. Extend Web `Skill` with optional ASSF projection fields listed in the New
   Doc-Only Fields section.
2. Extend Web `SkillIndexMeta` with optional ASSF projection counters.
3. Extend `scripts/build-skill-index.js` to read
   `docs/reference/agent_system_skills/generated/skill-index.json`.
4. Add read-only projected records for ASSF entries with
   `certificationState: CERTIFIED` and `uatState: PASSED`. If a record has no
   legacy Web skill match, create a bounded `agent_system_skills` presentation
   category rather than mutating legacy skill-library source.
5. Set `assfProjectionClass` to `CERTIFIED_PACKAGE_PROJECTION` only for
   certified projected ASSF records backed by generated ASSF metadata.
6. Keep `corpusClass` unchanged for legacy Web skills; do not use it as
   certification state.
7. Display projection metadata only when the fields are present.
8. Keep adapter fields visibly deferred when `externalCliMcpDisposition` is
   deferred.
9. Do not add any route, API, CLI/MCP adapter, provider call, package execution
   path, or certification mutation.

## Verification Commands

Run from repository root unless noted:

```powershell
python governance/compat/check_assf_skill_index_drift.py
python governance/compat/check_assf_certified_metadata_admission.py --require-certified
Push-Location EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
node scripts/build-skill-index.js
npm test -- --run src/lib/skill-corpus-governance.test.ts src/components/SkillLibrary.test.tsx src/components/SkillDetailView.test.tsx
npm run check
Pop-Location
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base cf50a81f --head HEAD
python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return --base cf50a81f --head HEAD --enforce
git diff --check
```

If `npm run check` is blocked by pre-existing unrelated type failures, record
the exact blocker and still run focused tests.

## Required Outputs

| Output | Required content |
|---|---|
| Worker return | `COMPLETE_PENDING_REVIEW`, exact changed paths, Source Inventory, Source Verification, tests, claim boundary |
| Completion review | reviewer disposition, closure diff gate, Machine Closure Package, Acceptance Receipt Assertion Matrix, next-control recommendation |
| Generated Web public index | generated by `node scripts/build-skill-index.js`, not hand-edited only |
| Focused tests | evidence that projection fields and UI display are deterministic |

## Forbidden Changed Paths And Actions

Forbidden in worker material execution:

- `docs/reference/agent_system_skills/registry/`
- `docs/reference/agent_system_skills/generated/`
- `governance/compat/run_assf_skill_resolver.py`
- `governance/compat/generate_assf_skill_index.py`
- package roots and package instruction bodies;
- `CVF_SESSION/`, `CVF_SESSION_MEMORY.md`, and `AGENT_HANDOFF*.md`;
- public-sync clone paths and push operations.

Forbidden actions:

- package instance creation;
- certification decision;
- lifecycle mutation;
- ASSF registry-source mutation;
- ASSF generated-index source mutation;
- resolver mutation;
- CLI/MCP adapter behavior;
- provider/live proof;
- public-sync or push;
- package activation, package instruction execution, or package integration;
- session-sync inside the material implementation commit.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Durable governance files created by worker | worker return and completion review under the reviews directory |
| New generated aggregate | Web public skills index may be regenerated by the Web generator |
| New source layout | N/A with reason: no new state source layout or ASSF package source layout |
| Index or registry mutation | Web public skill-index output may change; ASSF registry and generated ASSF index remain read-only inputs |
| Storage owner | Web source tree for implementation; reviews for evidence |
| Closure disposition required | reviewer verifies generated output and changed paths exactly match Write Ownership |

## Current Runtime Freshness Verification

| Runtime claim | Verification command or source | Observed value | Disposition |
|---|---|---|---|
| Web skill-index production path is generated | `package.json` and `scripts/build-skill-index.js` | `predev`/`prebuild` invoke generator; generator writes public skills-index artifact | PASS |
| ASSF source index is metadata-only | `docs/reference/agent_system_skills/generated/skill-index.json` | `claimBoundary` states metadata-only | PASS |
| Adapter is not implemented by this work order | Web projection contract and generated ASSF adapter fields | adapter remains deferred | PASS |

## Commit Prompt Readiness

Commit prompt once dispatch gates pass:

`Dispatch ASSF Web projection implementation`

Expected dispatch material paths:

- `docs/baselines/CVF_GC018_ASSF_WEB_PROJECTION_IMPLEMENTATION_2026-06-26.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_WEB_PROJECTION_IMPLEMENTATION_FOR_CODEX_2026-06-26.md`

## Pre-Dispatch Gate Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base cf50a81f --head HEAD
python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base cf50a81f --head HEAD --enforce
git diff --check
```

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order; no public-sync authorization.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_WEB_PROJECTION_IMPLEMENTATION_COMPLETION_2026-06-26.md` | reviewer closure artifact in material changed set | PASS |
| Roadmap state | N/A with reason: this tranche was dispatched from session next move, not by closing a roadmap file | no roadmap status mutation in changed set | N/A with reason |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | GC-051 coverage generated from source entry for the Web projection public skill-index surfaces | PASS |
| Registry Markdown | BLOCKED with reason: registry Markdown mutation was forbidden and out of scope for this Web projection tranche | no registry Markdown in changed set | BLOCKED with reason |
| External evidence digest | N/A with reason: no external evidence artifact was absorbed | local source and command evidence only | N/A with reason |
| System loop interlock | N/A with reason: no runtime loop, provider route, package activation, adapter, or execution interlock changed | Web projection is read-only metadata display | N/A with reason |
| Session continuity | N/A with reason: material implementation closure only; session-sync is separate after material commit | no session path in changed set | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Acceptance criterion | Receipt evidence | Disposition |
|---|---|---|
| AC1 Web type surface includes optional ASSF projection metadata | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/types/skill.ts` diff | PASS |
| AC2 Web generator reads certified ASSF metadata and emits bounded projections | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/scripts/build-skill-index.js` diff | PASS |
| AC3 generated Web public skill index is regenerated by command | Web-root `node scripts/build-skill-index.js` closure evidence | PASS |
| AC4 UI renders projection metadata only for projected records | focused component tests closure evidence | PASS |
| AC5 forbidden boundary remains intact | completion review claim boundary and changed set exclude package, adapter, provider, public-sync, and session-sync mutations | PASS |
| AC6 GC-051 coverage exists for Web projection review path mentions | corpus registry source entry and generated aggregate | PASS |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF Web projection implementation work order |
| claimDisposition | N/A with reason: dispatch artifact only; implementation happens later under this work order |
| receiptEvidence | N/A with reason: no runtime receipt is produced by dispatch |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source verification, dependency release evidence, and future closure gate requirements |
| invocationBoundary | governed local repository artifact authoring only |
| interceptionBoundary | no provider, CLI, MCP, adapter, package execution, or interception claim |
| claimLanguage | work order for read-only Web projection implementation |
| forbiddenExpansion | package instance, certification decision, lifecycle mutation, ASSF registry mutation, ASSF generated-index mutation, resolver mutation, CLI/MCP adapter, provider/live proof, public-sync, push, activation, and package instruction execution remain out of scope |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatch author |
| Provider or surface | local repository tools |
| Session or invocation | ASSF-WEBPROJ-T1 work order dispatch, 2026-06-26 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, Python resolver API, source reads, apply_patch |
| Target paths | this work order; paired GC-018 baseline |
| Allowed scope source | active next allowed move from ASSF-WEBPROJ-T0 completion at material commit `a408c13e` |
| Before status evidence | HEAD `cf50a81f`; clean worktree before dispatch authoring |
| After status evidence | pending dispatch packet changed set |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | GC-018 and source-verified work order only |
| Claim boundary | dispatch packet only; no implementation, package, adapter, provider, public-sync, generated-index source, resolver, registry, or session mutation |
| Agent type | dispatch author |
| Invocation ID | ASSF-WEBPROJ-T1-WORK-ORDER-DISPATCH-2026-06-26 |
| Expected manifest | this work order; paired GC-018 baseline |
| Actual changed set | this work order; paired GC-018 baseline |
| Manifest delta | MATCH |

## Claim Boundary

This work order authorizes bounded Web implementation only within the listed
Write Ownership paths. It does not certify packages, create package instances,
mutate ASSF registry/generated/resolver sources, implement adapters, run
providers, public-sync, push, activate packages, or execute package instruction
bodies. Session-sync remains a separate post-material step.
