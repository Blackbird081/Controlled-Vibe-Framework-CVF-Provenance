# CVF Agent Work Order: ASSF-PIC-T2 Manual UAT And Certification Review

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-26

docType: work_order

Batch ID: ASSF-PIC-T2

dispatchBaseHead: 61ad760c

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Worker. Reviewer/closer is Codex for returned worker artifacts.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_FOR_CLAUDE_2026-06-26.md`

Paired GC-018 baseline:
`docs/baselines/CVF_GC018_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_2026-06-26.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: record with `git rev-parse --short HEAD` at worker start.

Current-time notes: ASSF-PIC-T0 selected `cvf-dispatch-quality-reviewer`;
ASSF-PIC-T1 mapped its evidence skeleton; work-order dispatch scaffold
optimization and GC-020 bootstrap read-model classifier hotfix are closed. This
ASSF-PIC-T2 task is a manual UAT/certification evidence review, not package
instance creation and not worker-owned certification.

Do-not-misread notes: do not create package roots, `SKILL.md`,
`skill.source.json`, registry entries, generated index changes, resolver
changes, Web runtime changes, CLI/MCP adapter behavior, provider/live proof,
public-sync, push, package activation, lifecycle state mutation, session-sync,
or commits.

Required first actions: read this work order, read the paired GC-018 baseline,
read `CVF_SESSION_MEMORY.md`, read
`CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`, resolve
`CVF_SESSION/ACTIVE_SESSION_STATE.json`, read `AGENT_HANDOFF_V22_2026-06-22.md`,
read `docs/reference/guard_orientation/README.md`, read
`docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`,
then record actual `executionBaseHead` and `git status --short`.

Return contract: return `COMPLETE_PENDING_REVIEW` with uncommitted artifacts
only, actual `executionBaseHead`, actual `git status --short`, changed paths,
source inventory, local UAT command evidence, recommended lifecycle
disposition, and no commit. If blocked, return `BLOCKED_WITH_REASON` and name
the exact source, scope, or gate that blocks completion.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | operator request to issue ASSF-PIC-T2 work order |
| Scope classification | bounded manual UAT/certification evidence review |
| Intake role | worker authors review artifact and scaffold-first worker return |
| Reviewer role | Codex reviewer/closer validates artifacts, gates, boundaries, and commits accepted material |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; worker returns uncommitted artifacts |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | worker return to reviewer/closer closure conversion |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if completion would require package instance creation, registry mutation, lifecycle state advancement, generated-index mutation, resolver mutation, Web runtime, CLI/MCP adapter, provider/live proof, public-sync, push, package activation, destructive action, or broader ASSF roadmap change |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | dispatcher creates packet; worker executes ASSF-PIC-T2 documentation/review tranche and returns no-commit evidence; reviewer/closer reviews returned evidence, commits accepted material, and records any dedicated session-sync with material SHA evidence |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=61ad760c`; `executionBaseHead` recorded by worker; `closureBaseHead` set by reviewer before closure commit |
| changedSetScope(phase) | execution changes only Write Ownership paths; closer owns status conversion, reviewer artifact, accepted material commit, roadmap update if accepted, and later session-sync |
| traceScope(phase, actor) | worker-return trace covers pending ASSF-PIC-T2 artifacts only; reviewer trace covers review/closure; session-sync trace covers continuity only |
| commitOwner(phase) | worker commits nothing (`WORKER_MUST_NOT_COMMIT`); reviewer/closer owns any material, closure, or session-sync commit |
| crossBatchIsolation | do not mix this tranche with package instance creation, generated-index/resolver/Web/runtime/adapter/provider/public-sync work, or another dispatch batch |
| Before status evidence | dispatchBaseHead `61ad760c`; clean worktree evidence: `git status --short` returned no paths before dispatch authoring |
| nextMoveSurfaces | reviewer/closer updates next-move surfaces only in a dedicated session-sync commit with the accepted material SHA if mode or next allowed move changes |
| Closer designation | Codex reviewer/closer role is the designated closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_COMPLETION_2026-06-26.md` |
| reviewerOwnedClosurePaths | this work order; paired GC-018 baseline; worker review; worker-return artifact; ASSF-PIC roadmap status rows if accepted; reviewer completion review; optional session-sync surfaces if accepted |
| workerReturnStatus | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| closer | Codex reviewer/closer role |

## Purpose

Create the first manual UAT/certification evidence review for the selected
candidate `cvf-dispatch-quality-reviewer`, using current local gate evidence
that matches the candidate's declared acceptance evidence. The worker must
produce an honest recommended lifecycle disposition for Codex review without
mutating lifecycle state or claiming final certification.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-26 request: ASSF-PIC-T2 work order | ACCEPT |
| Active session front door | `CVF_SESSION_MEMORY.md` | ACCEPT |
| Active session bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | ACCEPT |
| Active session state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V22_2026-06-22.md` | ACCEPT |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_2026-06-26.md` | ACCEPT |
| ASSF-PIC roadmap | `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` | ACCEPT |
| PIC-T0 audit | `docs/audits/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_AUDIT_2026-06-25.md` | ACCEPT |
| PIC-T1 audit | `docs/audits/CVF_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_AUDIT_2026-06-26.md` | ACCEPT |
| Selected candidate registry entry | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | ACCEPT |
| ASSF package contract | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | ACCEPT |
| ASSF certification lifecycle guard | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | ACCEPT |

## Agent Roles

| Role | Owner |
|---|---|
| Operator | project authority and scope approval |
| Dispatcher | Codex dispatch author role |
| Worker | Claude documentation/review and no-commit return role |
| Reviewer | Codex reviewer role for returned worker artifacts |
| Closer | Codex closer role after acceptance |
| Session-sync steward | Codex session-sync role in a dedicated continuity commit if next move changes |

## Required First Reads

| Source | Action | Reason |
|---|---|---|
| `docs/baselines/CVF_GC018_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_2026-06-26.md` | READ | authorization, scope, and claim boundary |
| `CVF_SESSION_MEMORY.md` | READ | active front door and current next allowed move |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ | compact startup read model |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ | current generated aggregate and active handoff pointer |
| `AGENT_HANDOFF_V22_2026-06-22.md` | READ | active handoff and current session continuity |
| `docs/reference/guard_orientation/README.md` | READ | task-first guard orientation |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ | pre-write checklist for gate-parsed artifacts |
| `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` | READ | ASSF-PIC sequence and T2 boundary |
| `docs/audits/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_AUDIT_2026-06-25.md` | READ | selected-candidate source inventory |
| `docs/audits/CVF_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_AUDIT_2026-06-26.md` | READ | evidence skeleton and open UAT/certification gaps |
| `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | READ | selected candidate source entry |
| `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | READ | package evidence and lifecycle fields |
| `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | READ | certification/UAT/drift/adapter claim boundaries |
| `governance/compat/run_worker_return_scaffold.py` | READ | required worker-return scaffold generator |
| `governance/compat/run_worker_return_fast_gate.py` | READ | required early worker-return gate |

## Pre-Flight Checks

The worker must run these before editing. For commands using
`<executionBaseHead>`, replace it with the exact value returned by
`git rev-parse --short HEAD` at worker start.

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
Test-Path docs/reviews/CVF_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_2026-06-26.md
Test-Path docs/reviews/CVF_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_WORKER_RETURN_2026-06-26.md
```

If a command fails before edits because of a pre-existing out-of-scope
violation, record it in the worker return and continue only when the violation
does not affect the allowed changed paths. Do not repair out-of-scope material.

## Worker Return Packet Shape Contract

The worker-return artifact must be scaffold-first. The scaffold helper supplies
the starting shape, and the completed worker return must retain or complete
the sections listed below so reviewer-fast can diagnose issues before closure:

- `Status`
- `dispatchWorkOrder`
- `Purpose`
- `Source Inventory`
- `Scope / Methodology`
- `Findings / Position`
- `Risk / Corrective Action`
- `Claim Boundary`
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
- actual `executionBaseHead`
- actual `git status --short`
- changed-path list
- command evidence
- no commit statement

If any section is not applicable, include the section with `N/A with reason`
or `NOT_APPLICABLE_WITH_REASON` and a short reason instead of omitting it.

### Worker Return Scaffold-First Requirement

Before writing long report content, create the worker return from the scaffold:

```powershell
python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_WORKER_RETURN_2026-06-26.md --title "CVF ASSF-PIC-T2 Manual UAT And Certification Review Worker Return"
```

Then fill the scaffold completely. Do not leave `TODO` strings in the returned
artifact. The worker return must include:

- `dispatchWorkOrder: ` followed by this work order path in backticks;
- `## Source Inventory` with real paths and bare action tokens;
- `receiptEvidence: CVF_RECEIPT_PRESENT - ...`;
- `Corpus verdict: NOT_APPLICABLE_WITH_REASON - ...`;
- `Defect class:` with a valid value used by the finding-to-governance guard;
- `Actual changed set` listing real changed paths, not shorthand prose;
- worker-return scaffold measurement fields.

## Worker Autonomy / No-Question Rule

Within Allowed scope, the worker must repair machine-check, source-inventory,
packet-shape, focused-command, and worker-return fast-gate failures and rerun
the required checks without asking the operator. Ask the operator only if
remediation would exceed Allowed scope, change the claim boundary, require
package instance creation, lifecycle state advancement, generated-index
mutation, resolver mutation, Web runtime, adapter work, provider/live proof,
public-sync, push, destructive action, or another roadmap batch.

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| `docs/reviews/CVF_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_2026-06-26.md` | worker | create manual UAT/certification evidence review |
| `docs/reviews/CVF_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_WORKER_RETURN_2026-06-26.md` | worker | create scaffold-first no-commit worker return |
| `docs/reviews/CVF_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_COMPLETION_2026-06-26.md` | Codex reviewer/closer | create only when Codex accepts the worker return |
| this work order | Codex reviewer/closer | status conversion only when Codex accepts the worker return |
| paired GC-018 baseline | Codex reviewer/closer | status conversion only when Codex accepts the worker return |
| ASSF-PIC roadmap | Codex reviewer/closer | status conversion only with accepted completion path and material commit SHA |
| session-sync surfaces | Codex session-sync steward | update only in a dedicated continuity commit with material SHA evidence |

Worker may create or modify only these execution paths:

- `docs/reviews/CVF_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_2026-06-26.md`
- `docs/reviews/CVF_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_WORKER_RETURN_2026-06-26.md`

## Forbidden Changed Paths And Actions

The worker must not change:

- `docs/reference/agent_system_skills/registry/entries/*.json`
- `docs/reference/agent_system_skills/generated/skill-index.json`
- `governance/compat/run_assf_skill_resolver.py`
- `governance/compat/generate_assf_skill_index.py`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/**`
- `CVF_SESSION/**`
- `AGENT_HANDOFF_V22_2026-06-22.md`
- `CVF_SESSION_MEMORY.md`
- public-sync clone files or remotes.

The worker must not commit, push, run live/provider proof, create package
roots, create `SKILL.md`, create `skill.source.json`, activate a package,
advance `uatState`, advance `certificationState`, or claim final certification.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Durable governance files created by worker | one review file and one worker-return file only |
| New generated aggregate | N/A with reason: no generated aggregate or generated-index mutation is authorized |
| New source layout | N/A with reason: no source-layout split, package root, registry source family, resolver source, Web source, or adapter source is authorized |
| Index or registry mutation | N/A with reason: ASSF generated index and registry entries remain out of scope |
| Storage owner | documentation evidence under the planned review paths |
| Closure disposition required | reviewer verifies changed paths exactly match Write Ownership before any material commit |

## Required UAT Review Shape

Create:

`docs/reviews/CVF_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_2026-06-26.md`

Required sections:

- `Status: COMPLETE_PENDING_REVIEW`
- `Selected Candidate`
- `Source Inventory`
- `Manual UAT Evidence`
- `Certification Evidence Review`
- `Lifecycle Disposition Recommendation`
- `Generated Index And Resolver Drift Disposition`
- `Dual Agent Surface Matrix`
- `Source Verification Block`
- `Claim Boundary`
- `Public Export Disposition`
- `Delta Execution Claim Boundary Control Block`
- `Agent Operation Trace Block`

The review must recommend exactly one lifecycle disposition for Codex review:

- `CERTIFICATION_HELD_WITH_REASON`
- `CERTIFICATION_REJECTED`
- `CERTIFIED_RECOMMENDATION_FOR_REVIEWER_ONLY`

Use `CERTIFIED_RECOMMENDATION_FOR_REVIEWER_ONLY` only if UAT evidence commands
pass and the review clearly states that no registry lifecycle mutation or final
certification occurs in the worker handoff. If evidence is incomplete,
contradictory, or out-of-scope, use `CERTIFICATION_HELD_WITH_REASON` or
`CERTIFICATION_REJECTED`.

## Manual UAT Evidence Commands

Run and record results:

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base 61ad760c --head HEAD --enforce
python governance/compat/run_dispatch_packet_author_fast_gate.py --base 61ad760c --head HEAD --enforce
python governance/compat/check_assf_skill_index_drift.py
Test-Path docs/baselines/CVF_GC018_ASSF_T2_GENERATED_INDEX_AND_PROGRESSIVE_RESOLVER_2026-06-23.md
Test-Path governance/compat/check_work_order_dispatch_quality.py
Test-Path governance/compat/run_dispatch_packet_author_fast_gate.py
Test-Path docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json
```

These commands are local read-only UAT evidence for the selected candidate's
declared acceptance evidence. They are not provider/live proof, not package
activation, and not certification by themselves.

## Execution Plan

1. Complete all Required First Reads and Pre-Flight Checks.
2. Create the worker-return scaffold with `run_worker_return_scaffold.py
   --write` before drafting the long return.
3. Create the manual UAT/certification review under Write Ownership.
4. Run Manual UAT Evidence Commands and record exact outputs.
5. Fill the worker return from the scaffold and record actual changed paths.
6. Run required return commands, repair allowed-scope packet defects, and rerun
   `run_worker_return_fast_gate.py`.
7. Return `COMPLETE_PENDING_REVIEW` with no commit when all allowed-scope
   checks pass, or `BLOCKED_WITH_REASON` with exact blocker evidence.

## Evidence Requirements

The worker-return artifact must record:

- actual `executionBaseHead`;
- actual `git status --short`;
- exact changed paths;
- source inventory for every file read or changed;
- scaffold command and scaffold-created result;
- first and final `run_worker_return_fast_gate.py` results;
- manual format repairs after first fast gate, or `NONE`;
- Manual UAT Evidence Commands and results;
- recommended lifecycle disposition;
- `git diff --check`;
- `git diff --name-status`;
- explicit no-commit statement;
- explicit statement that no package instance, lifecycle mutation, generated
  index, resolver, Web runtime, CLI/MCP adapter, provider/live proof,
  public-sync, push, activation, session-sync, or final certification occurred.

## Closure Checklist

| Check | Required resolution |
|---|---|
| Worker status | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| Changed paths | stay inside Write Ownership |
| Worker return | created through `run_worker_return_scaffold.py --write` |
| UAT/certification review | records all Manual UAT Evidence Commands |
| Lifecycle disposition | recommendation is present and bounded to reviewer review |
| Required commands | recorded with PASS or blocking reason |
| Worker boundary | no commit, push, public-sync, provider/live proof, registry mutation, generated-index mutation, resolver mutation, Web mutation, adapter mutation, active session state mutation, or lifecycle mutation |

## Required Commands Before Return

Run and record results:

```powershell
git status --short
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git diff --name-status
```

If `run_worker_return_fast_gate.py` fails because the worker-return artifact is
still malformed, repair the artifact and rerun it. If it fails because of an
out-of-scope pre-existing violation, record the exact failing command and
return `BLOCKED_WITH_REASON`.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| ASSF-PIC-T2 is manual UAT and certification review | `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` | lines 205-223 | `ASSF-PIC-T2` | ASSF-PIC roadmap | LITERAL_INVARIANT | ACCEPT |
| PIC-T0 selected `cvf-dispatch-quality-reviewer` | `docs/audits/CVF_ASSF_PIC_T0_PILOT_CANDIDATE_SELECTION_SOURCE_INVENTORY_AUDIT_2026-06-25.md` | lines 13-15 | `Selected candidate` | ASSF-PIC-T0 audit | VALUE_SET | ACCEPT |
| PIC-T1 mapped the selected candidate evidence skeleton | `docs/audits/CVF_ASSF_PIC_T1_PACKAGE_INSTANCE_EVIDENCE_SKELETON_HARDENING_AUDIT_2026-06-26.md` | lines 130-137 | `EVIDENCE_SKELETON_MAPPED` | ASSF-PIC-T1 audit | VALUE_SET | ACCEPT |
| Candidate acceptance evidence names dispatch-quality gates | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | line 58 | `acceptanceEvidence` | ASSF-T2 registry source entry | VALUE_SET | ACCEPT |
| Candidate UAT and certification states are not started | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | lines 67-68 | `uatState` | ASSF-T2 registry source entry | VALUE_SET | ACCEPT |
| Candidate external adapter disposition is deferred | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | lines 79-82 | `externalCliMcpDisposition` | ASSF-T2 registry source entry | VALUE_SET | ACCEPT |
| T7 lifecycle guard blocks certification without passed UAT | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | lines 89-91 | `MISSING_UAT` | ASSF-T7 certification lifecycle guard | LITERAL_INVARIANT | ACCEPT |
| T7 adapter claim honesty rules require real adapter evidence | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | lines 132-149 | `adapterEvidence` | ASSF-T7 certification lifecycle guard | LITERAL_INVARIANT | ACCEPT |
| Worker-return scaffold helper writes one new worker-return scaffold | `governance/compat/run_worker_return_scaffold.py` | lines 209-232 | `write_scaffold` | worker-return scaffold helper | RUNTIME_BEHAVIOR | ACCEPT |
| Dispatch packet author fast gate is current source for the selected candidate's acceptance evidence | `governance/compat/run_dispatch_packet_author_fast_gate.py` | lines 119-134 | `main` | dispatch packet author fast gate | EXISTS | ACCEPT |

## Current Runtime Freshness Verification

| Runtime surface | Freshness action | Evidence | Disposition |
|---|---|---|---|
| Selected ASSF registry entry | read current source entry | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` lines 67-82 | lifecycle states remain `NOT_STARTED`; external adapter remains deferred |
| ASSF generated index drift | ran current drift check before dispatch authoring | `python governance/compat/check_assf_skill_index_drift.py` | PASS |
| Candidate source artifacts | verified current paths exist | `Test-Path` for ASSF-T2 baseline, `check_work_order_dispatch_quality.py`, and `run_dispatch_packet_author_fast_gate.py` returned `True` | source artifacts present |
| Model gateway provider registry | checked current provider registry surface only because provider-registry trigger words appear in forbidden-scope prose | `Test-Path EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` returned `True`; `rg -n "PROVIDER_CAPABILITY_REGISTRY" EXTENSIONS/CVF_MODEL_GATEWAY/src -g "*.ts"` found `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` line 70 | N/A with reason: this work order makes no provider registry absence claim and authorizes no provider/runtime change |
| External CLI/MCP adapter | read current candidate and T7 adapter fields | registry entry lines 79-82; T7 lines 132-149 | adapter remains deferred; no implementation claim |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001: Exhaustive directory claim omits actual children
- ADIF-0002: Provider-local interaction accepted as authority
- ADIF-0007: Gate keyword in exclusion prose triggers wrong evidence class
- ADIF-0006: Source Verification symbol cell contains a value/type

Remediation applied:

- ADIF-0001: This work order cites bounded files and exact planned artifacts
  only; worker must list real changed paths.
- ADIF-0002: ACCEPT rows cite CVF-governed repository files only.
- ADIF-0007: Scope exclusions are boundaries, not evidence claims.
- ADIF-0006: Verified path or symbol cells contain only paths, fields,
  functions, sections, or tokens.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator request routed to governed work-order/source-verification/autorun lane |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this ASSF-PIC-T2 work order and paired GC-018 baseline |
| Disposition | local manual UAT/certification evidence review only; no external material absorbed |
| Claim boundary | source facts must cite CVF-governed files and command evidence |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap or checkpoint requirement | Work-order coverage | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| PIC-T2 runs manual UAT/certification review | Required UAT Review Shape | UAT/certification review artifact | reviewer diff and worker return | READY |
| Generated metadata and Web display are not certification evidence | Forbidden Changed Paths And Actions; Claim Boundary | review claim boundary | reviewer closure | READY |
| Lifecycle disposition is one of the allowed T2 outcomes | Required UAT Review Shape | `Lifecycle Disposition Recommendation` | reviewer closure | READY |
| Explicit external adapter disposition is required | Dual Agent Surface Matrix | external row `DEFERRED_WITH_REASON` | reviewer-fast | READY |
| T3 remains held until T2 accepted | Reviewer Closure Conversion | roadmap update only with accepted completion path and material commit SHA | dedicated session-sync with material SHA evidence | READY |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | ASSF-PIC-T2 UAT/certification review and worker return for `cvf-dispatch-quality-reviewer` | internal agents may run read-only local gate evidence and recommend a lifecycle disposition for Codex review; no registry mutation, package instance, generated-index update, resolver behavior, Web projection, commit authority, activation, package execution, or final certification is granted to the worker | this work order, paired baseline, PIC-T0 audit/completion, PIC-T1 audit/completion, ASSF package contract, T7 lifecycle guard | no internal loader, resolver, generator, Web bridge, or package root is implemented | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future external package readout or adapter claim | external agents cannot mutate, certify, activate, execute, or consume packages through this tranche | Dual Agent Surface Accounting Standard and T7 adapter honesty contract | adapter implementation is deferred to a separate source-verified work order | `DEFERRED_WITH_REASON` |

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Worker return is created through `governance/compat/run_worker_return_scaffold.py --write` before manual filling. |
| AC2 | UAT/certification review records `check_work_order_dispatch_quality.py --base 61ad760c --head HEAD --enforce`. |
| AC3 | UAT/certification review records `run_dispatch_packet_author_fast_gate.py --base 61ad760c --head HEAD --enforce`. |
| AC4 | UAT/certification review records `check_assf_skill_index_drift.py`. |
| AC5 | Review records one lifecycle disposition recommendation without registry or generated-index mutation. |
| AC6 | Review and worker return include exact changed paths and command-backed evidence. |
| AC7 | Worker returns uncommitted artifacts only under `WORKER_MUST_NOT_COMMIT`. |

## Review Gate

Codex reviewer/closer must verify the worker return against Write Ownership,
review the UAT/certification artifact for source-backed evidence and honest
disposition, run reviewer-fast or committed-range gates as appropriate, confirm
no lifecycle mutation occurred, and only then convert accepted material into a
completion review and material commit.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` when the UAT/certification review and worker
return are present, the worker-return fast gate passes, required evidence is
recorded, and changed files remain inside Write Ownership.

Return `BLOCKED_WITH_REASON` when a required source is missing, a required gate
cannot pass inside Allowed scope, the selected candidate proves unsuitable for
review, or the repair would require forbidden package, runtime, provider,
public, session-sync, lifecycle, or adapter scope.

## Operator Checkpoint

No operator checkpoint is required for routine allowed-scope remediation inside
this work order. Operator checkpoint is required only if execution would
require package instance creation, lifecycle state advancement, generated-index
mutation, resolver mutation, Web runtime, CLI/MCP adapter behavior,
provider/live proof, public-sync, push, package activation, secrets/quota,
destructive action, or a change to the claim boundary.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_FOR_CLAUDE_2026-06-26.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_COMPLETION_2026-06-26.md` | `Reviewer verdict: CLOSED_PASS_BOUNDED`; `Lifecycle disposition: CERTIFICATION_HELD_WITH_REASON` | PASS |
| Roadmap state | `docs/roadmaps/CVF_ASSF_PACKAGE_INSTANCE_CERTIFICATION_PILOT_ROADMAP_2026-06-25.md` | T2 `Status: CLOSED_PASS_BOUNDED`; T3 `Status: HOLD_CERTIFICATION_HELD_BY_PIC_T2` | PASS |
| Registry JSON | N/A with reason: no registry JSON mutation is authorized by ASSF-PIC-T2 | worker review confirms no lifecycle registry mutation | BLOCKED with reason: out of scope |
| Registry Markdown | N/A with reason: no registry Markdown mutation is authorized by ASSF-PIC-T2 | no registry documentation mutation in changed set | BLOCKED with reason: out of scope |
| External evidence digest | N/A with reason: no external evidence artifact is created by this local documentation tranche | no external artifact hash applies | N/A with reason |
| System loop interlock | closure review | no package activation, runtime loop, provider call, public-sync, or worker commit occurred | PASS |
| Session continuity | N/A with reason: session-sync is separate after material closure | active session paths excluded from material changed set | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| No runtime/provider/adapter receipt required for this documentation-only closure | `receiptEvidence` remains N/A with reason; reviewer-fast and worker-return fast gate evidence recorded in completion review | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance dispatch; no public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | ASSF-PIC-T2 manual UAT/certification review work order |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- dispatch work order only |
| receiptEvidence | N/A with reason: no runtime execution, provider call, adapter receipt, or worker return exists at dispatch |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- Source Verification Block, dependency release evidence, ADIF disclosure, and planned manifest |
| invocationBoundary | governed local documentation and read-only local gate evidence only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, Web runtime, or adapter interception claim |
| claimLanguage | authorizes bounded no-commit manual UAT/certification evidence review by worker |
| forbiddenExpansion | no package instance, lifecycle mutation, generated-index mutation, resolver mutation, Web runtime change, CLI/MCP adapter, provider/live proof, public-sync, push, activation, package instruction execution, session-sync, or worker commit |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author role |
| Provider or surface | Codex local workspace |
| Session or invocation | ASSF-PIC-T2 dispatch authoring, 2026-06-26 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | startup reads, source reads, rg, ADIF resolver import, apply_patch |
| Target paths | this work order; paired GC-018 baseline |
| Allowed scope source | operator request to issue ASSF-PIC-T2 work order |
| Before status evidence | dispatchBaseHead `61ad760c`; clean worktree evidence: `git status --short` returned no paths before dispatch authoring |
| After status evidence | dispatch artifacts pending gate and commit |
| Diff evidence | `git diff --name-status` before material dispatch commit |
| Approval boundary | dispatch packet only; worker execution follows the committed dispatch packet |
| Claim boundary | repo-local dispatch evidence only; no runtime/provider/live/public claim |
| Agent type | dispatcher |
| Invocation ID | `assf-pic-t2-manual-uat-certification-review-dispatch-2026-06-26` |
| Expected manifest | `docs/baselines/CVF_GC018_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_2026-06-26.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_FOR_CLAUDE_2026-06-26.md` |
| Actual changed set | `docs/baselines/CVF_GC018_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_2026-06-26.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_FOR_CLAUDE_2026-06-26.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Handoff Prompt For Claude

You are Claude in the CVF repo:
`D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF`

Read this work order first:
`docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_FOR_CLAUDE_2026-06-26.md`

Then execute exactly the bounded ASSF-PIC-T2 worker task. You are
`WORKER_MUST_NOT_COMMIT`.

Required output paths:

- `docs/reviews/CVF_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_2026-06-26.md`
- `docs/reviews/CVF_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_WORKER_RETURN_2026-06-26.md`

Before writing the worker return, run:

```powershell
python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_ASSF_PIC_T2_MANUAL_UAT_CERTIFICATION_REVIEW_WORKER_RETURN_2026-06-26.md --title "CVF ASSF-PIC-T2 Manual UAT And Certification Review Worker Return"
```

No commits. No package instance creation. No registry lifecycle mutation. No
generated-index mutation. No resolver mutation. No Web runtime change. No
CLI/MCP adapter. No provider/live proof. No public-sync/push.

Return `COMPLETE_PENDING_REVIEW` only after the worker-return fast gate passes,
or `BLOCKED_WITH_REASON` with the exact blocking command/scope reason.

## Claim Boundary

This work order authorizes the worker to produce ASSF-PIC-T2 manual UAT and
certification evidence review plus a scaffold-first worker return only. It
does not authorize package creation, final certification, lifecycle mutation,
generated-index mutation, resolver mutation, Web runtime changes, adapter
implementation, live/provider calls, public-sync, push, session-sync, or
commits.
