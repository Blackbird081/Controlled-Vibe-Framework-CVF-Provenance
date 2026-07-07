# CVF Agent Work Order - MSEA R64 External Critique Intake And Public Drift Decision

Memory class: POINTER_RECORD

Status: DISPATCH_READY

dispatchBaseHead: 8492fc8c3

Commit mode: WORKER_MUST_NOT_COMMIT

## Dispatch Prompt Envelope

```text
Role: worker. Codex/operator remains reviewer/closer after return.
Canonical packet: docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R64_EXTERNAL_CRITIQUE_INTAKE_AND_PUBLIC_DRIFT_DECISION_2026-07-07.md.
Commit mode: WORKER_MUST_NOT_COMMIT.
Base: executionBaseHead must be captured with git rev-parse --short HEAD at worker start.
Current-time notes: operator supplied external critique folder Gop y CVF in the provenance workspace; treat it as advisory input, not CVF authority.
Do-not-misread notes: do not edit public-sync, do not copy the external pack into governed docs, do not run provider/live proof, do not implement checker/runtime work.
Required first actions: read this work order, the paired GC-018 baseline, the roadmap, the external-intake chain map, the external finding absorption workflow, the critical repository boundary, then run git status and rg --files "Gop y CVF".
Return contract: COMPLETE_PENDING_REVIEW with worker return, companion classification matrix, executionBaseHead, current HEAD unchanged, git status showing only owned pending artifacts plus Gop y CVF if still untracked, and required gate/evidence results; or BLOCKED_WITH_REASON.
```

## Purpose

Dispatch one bounded, no-commit worker tranche to classify the operator-provided
external critique folder as advisory input, verify public-facing drift against
the sibling public-sync clone, and recommend the next governed absorption
targets without changing public, runtime, source, test, checker, provider, or
private-output surfaces.

## Scope

This work order is limited to R64 external critique intake, source-verified
public drift confirmation, and next-target recommendation. It does not
authorize public-sync mutation, public push, source/test/runtime/checker edits,
provider/live/MCP proof, production Memory/RAG release,
retrieval/vectorization, private/generated MinerU output read, use-case/legal
workflow, direct external source import, worker commit, or hosted/public
readiness claims.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `governance/compat/build_dispatch_packet_scaffold.py` not used; manually authored from current CVF work-order template and checker read-ahead. |
| generatedProfile | manual-work-order-dispatch |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | full artifact authored and repaired against pre-dispatch gates |
| checkerReadAheadConfirmation | checker source read-ahead block is included in this work order |
| docOnlyNewFields | R64 classification matrix fields are worker-output requirements only |
| claimBoundary | no runtime, public-sync, source, test, checker, provider, or live-proof authority |

## 1. Mission

Classify the operator-provided external critique folder `Gop y CVF`, verify the
public drift candidates against the current sibling public-sync clone, and
return a bounded decision on whether to proceed with R65 public drift repair,
R66 agent-loop policy/schema admission, R67 trust/threat public surfaces, and
R68 validator feasibility.

Success means the worker produces a review-ready worker return and companion
classification matrix that split the external critique into atomic items,
source-classify each item, verify current public drift evidence, and preserve
all runtime/public/checker boundaries.

## 2. Authority Chain

- Operator instruction: operator approved roadmap/work-order authoring after audit of `Gop y CVF`.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Bootstrap state: `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`.
- Active handoff: `AGENT_HANDOFF_V38_2026-07-06.md`.
- Roadmap: `docs/roadmaps/CVF_MSEA_R64_R70_PUBLIC_TRUST_AGENT_LOOP_ABSORPTION_ROADMAP_2026-07-07.md`.
- GC-018 baseline: `docs/baselines/CVF_GC018_MSEA_R64_EXTERNAL_CRITIQUE_INTAKE_AND_PUBLIC_DRIFT_DECISION_2026-07-07.md`.
- External chain map: `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`.
- External finding workflow: `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md`.
- Public/provenance boundary: `docs/reference/CVF_AGENTS_CRITICAL_REPOSITORY_BOUNDARY_2026-06-23.md`.

Authority boundary:

- This work order does not authorize work outside the cited authority chain.
- If any authority artifact conflicts with this work order, stop and return
  `BLOCKED_WITH_REASON`.

## 3. Agent Roles

- Dispatcher: Codex reviewer/closer role.
- Worker: delegated worker under `WORKER_MUST_NOT_COMMIT`.
- Reviewer/closer: Codex or operator-selected reviewer after worker return.
- Operator approval required for: public-sync mutation, runtime/source/test
  edits, checker implementation, live/provider proof, external source import,
  public push, or claim-boundary widening.

## Intake Role Routing Decision

| Field | Decision |
| --- | --- |
| intakeRole | external-critique-intake worker |
| routingBasis | operator-provided external folder plus source-verified public drift check |
| selectedRoleRoute | dispatcher -> no-commit worker -> reviewer/closer |
| routeMode | MULTI_AGENT_MULTI_ROLE |
| canonicalRouteMode | multi-agent, no-commit worker route |
| scopeClassification | docs-only external-intake and public-drift decision |
| riskSensitivity | high: external advisory input, public/provenance boundary, and no public-sync mutation |
| escalationCondition | any request to edit public-sync, runtime, source, tests, checkers, provider/live proof, private output, or public push |
| workerOutputRole | classification matrix and worker return only |
| reviewerOutputRole | completion review artifact and material commit if accepted |
| downstreamOwner | fresh R65/R66/R67/R68 dispatcher packets only when reviewer acceptance records the R64 decision |

## 4. Scope

Allowed scope:

- read all files under `Gop y CVF`;
- read the current sibling public-sync clone for public drift verification;
- read the provenance standards and owner surfaces named in this work order;
- create exactly these worker-owned artifacts:
  - `docs/reviews/CVF_MSEA_R64_EXTERNAL_CRITIQUE_INTAKE_AND_PUBLIC_DRIFT_DECISION_WORKER_RETURN_2026-07-07.md`
  - `docs/reference/CVF_MSEA_R64_EXTERNAL_CRITIQUE_INTAKE_CLASSIFICATION_MATRIX_2026-07-07.md`
- run local documentation/governance gates needed to validate the worker return.

Forbidden scope:

- no public-sync edit, commit, or push;
- no source/test/runtime/checker edit;
- no provider/live/MCP proof;
- no production Memory/RAG release;
- no retrieval/vectorization release;
- no private/generated MinerU output read;
- no use-case/legal workflow;
- no direct import of external pack files as canonical CVF docs;
- no worker commit.

Risk ceiling:

- R1 documentation/intake decision only.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Disclosure disposition: no ADIF defect IDs were returned for this exact query.

## 5. Required First Reads

| Path | Reason |
| --- | --- |
| `docs/baselines/CVF_GC018_MSEA_R64_EXTERNAL_CRITIQUE_INTAKE_AND_PUBLIC_DRIFT_DECISION_2026-07-07.md` | dispatch baseline and scope boundary |
| `docs/roadmaps/CVF_MSEA_R64_R70_PUBLIC_TRUST_AGENT_LOOP_ABSORPTION_ROADMAP_2026-07-07.md` | lane plan and tranche split |
| `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | external input routing |
| `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md` | required absorption table shape |
| `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | value conversion and overlap discipline |
| `docs/reference/CVF_AGENTS_CRITICAL_REPOSITORY_BOUNDARY_2026-06-23.md` | public/provenance split |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | governed artifact literal traps |
| `Gop y CVF/CVF Fix Proposal.md` | external critique overview |
| `Gop y CVF/cvf_public_trust_agent_loop_fix_pack/README.md` | external pack purpose |
| `Gop y CVF/cvf_public_trust_agent_loop_fix_pack/APPLY_ORDER.md` | external pack proposed application order |
| `Gop y CVF/cvf_public_trust_agent_loop_fix_pack/manifest.json` | external pack file manifest |

## 6. Pre-Flight Checks

Run before writing worker artifacts:

```powershell
git rev-parse --short HEAD
git status --short --branch
rg --files "Gop y CVF"
git -C "D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync" status --short --branch
git -C "D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync" remote -v
```

Expected results:

- worker records executionBaseHead;
- public-sync remote points to the public repository, not provenance;
- external folder file count is recorded;
- no public-sync mutation is performed.

## 6A. Source-Fidelity Pass

The worker must verify source facts before accepting an external claim.

### Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| R64 baseline authorizes only intake/classification | `docs/baselines/CVF_GC018_MSEA_R64_EXTERNAL_CRITIQUE_INTAKE_AND_PUBLIC_DRIFT_DECISION_2026-07-07.md` | `## Baseline Decision` | `R64_EXTERNAL_CRITIQUE_INTAKE_AND_PUBLIC_DRIFT_DECISION_DISPATCH_READY` | R64 baseline | ACCEPT |
| External critique input type is allowed by chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | `## Input Type Router` | `operator-provided external comparison, critique, or recommendation` | external knowledge absorption chain map | ACCEPT |
| External finding workflow requires row-level classification | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md` | `## Required Absorption Table` | `External item ID`; `CVF disposition`; `Claim boundary` | external finding absorption workflow | ACCEPT |
| Public-facing changes must use sibling public-sync clone | `docs/reference/CVF_AGENTS_CRITICAL_REPOSITORY_BOUNDARY_2026-06-23.md` | `## Critical Repository Boundary - 2026-05-09` | `Controlled-Vibe-Framework-CVF-public-sync` | critical repository boundary reference | ACCEPT |
| Work order uses no-commit worker return mode | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | `## 11. Review Gate` | `WORKER_MUST_NOT_COMMIT` | work-order template | ACCEPT |

### Current Runtime Freshness Verification

R64 makes no runtime capability claim. The worker must not verify or run runtime
behavior. Any external item that claims runtime, provider, public, production,
MCP, checker, or cost behavior must be classified as proof-required unless
current CVF source evidence exists.

### Negative Search And Collision Discipline

If the worker records a missing owner surface, it must include exact search
commands and results in the worker return. Do not use guessed missing-source
language without command evidence.

## 6B. Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| R64 classifies external critique before action | Scope; Execution Plan | worker return and classification matrix | worker-return fast gate | PASS |
| Public drift evidence is recomputed | Evidence Requirements | public-sync verification table | `rg` commands recorded by worker | PASS |
| Public-sync remains held | Forbidden scope | claim boundary and public export disposition | reviewer check | PASS |
| Agent-loop policy/schema held for R66 | Acceptance Criteria | classification matrix routing rows | reviewer check | PASS |
| Runtime/checker work held | Forbidden scope | worker return boundary rows | reviewer check | PASS |

## 6C. Worker Autonomy / No-Question Rule

The worker proceeds without operator confirmation for non-destructive actions
inside Allowed scope: reading files, running `rg`, `git status`, public-sync
read-only verification, and repairing worker-return format issues.

Escalate only for scope expansion, public-sync edits, live/provider proof,
source/test/runtime/checker edits, public push, private-output access, or
destructive actions.

## 6C.1 System Loop Interlock Routing

- Upstream loop and output artifact: R60/R63 stop/checkpoint state plus this
  R64 roadmap.
- Downstream loop and input artifact: R65/R66/R67/R68 packets only after R64
  reviewer acceptance.
- Routing rule: accepted public drift items route to R65; accepted policy/schema
  items route to R66; trust/threat items route to R67; checker/runtime items
  route to R68 decision or hold.
- Claim boundary: no autonomous mutation.

## 6D. Pending Artifact Evidence Finality

The worker return must record actual `git status --short --untracked-files=all`
after both owned output files exist. It must not claim clean worktree while the
worker return or classification matrix is pending.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Disposition |
| --- | --- |
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher -> worker -> reviewer/closer |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead `8492fc8c3`; worker records executionBaseHead at start; reviewer records closureBaseHead if accepted |
| changedSetScope(phase) | worker may create only the two output artifacts named in Allowed scope |
| traceScope(phase, actor) | worker return and companion matrix must include Agent Operation Trace Block |
| commitOwner(phase) | reviewer/closer owns material commit upon acceptance |
| crossBatchIsolation | no public-sync, runtime, checker, or session-sync changes in worker batch |
| nextMoveSurfaces | session-sync steward updates front door/state only when reviewer acceptance changes mode or next allowed move |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R64_EXTERNAL_CRITIQUE_INTAKE_AND_PUBLIC_DRIFT_DECISION_COMPLETION_REVIEW_2026-07-07.md` |
| reviewerOwnedClosurePaths | worker return, classification matrix, and completion review artifact when reviewer accepts R64 |
| conversionRule | reviewer may repair allowed-scope format/evidence defects, then commit material paths; session-sync is separate if needed |

## Write Ownership

Worker-owned paths:

- `docs/reviews/CVF_MSEA_R64_EXTERNAL_CRITIQUE_INTAKE_AND_PUBLIC_DRIFT_DECISION_WORKER_RETURN_2026-07-07.md`
- `docs/reference/CVF_MSEA_R64_EXTERNAL_CRITIQUE_INTAKE_CLASSIFICATION_MATRIX_2026-07-07.md`

Reviewer/session-sync-owned paths:

- `docs/reviews/CVF_MSEA_R64_EXTERNAL_CRITIQUE_INTAKE_AND_PUBLIC_DRIFT_DECISION_COMPLETION_REVIEW_2026-07-07.md`
- active session state, front door, and handoff surfaces if closure changes
  mode or next allowed move.

## 8. Execution Plan

| Step | Input artifact | Output artifact | Validation / stop condition |
| --- | --- | --- | --- |
| 1 | R64 work order and baseline | executionBaseHead and preflight record | stop if public-sync remote is wrong or external folder unreadable |
| 2 | `Gop y CVF` file list | source inventory table | stop if manifest cannot be enumerated |
| 3 | external pack files | atomic external item ledger | stop if root proposal and phase/patch/reference files are not read |
| 4 | public-sync files | public drift verification table | stop if public-sync clone is missing |
| 5 | CVF owner surfaces | classification matrix | stop if a high-value item lacks owner/disposition |
| 6 | worker output files | worker-return fast gate evidence | repair allowed-scope failures and rerun |

## 8A. Design Control Carry-Forward

| Design control | Roadmap source | Work-order handling | Verdict |
| --- | --- | --- | --- |
| Scope boundary | roadmap Scope | no-commit intake/classification only | PASS |
| Non-goals | roadmap Non-Goals | forbidden scope blocks public-sync/runtime/checker | PASS |
| Lane split | roadmap Work Plan | R64 only | PASS |
| Dependency/source-verification plan | roadmap Design Control Gate | worker recomputes public drift evidence | PASS |
| Claim boundary | roadmap Claim Boundary | worker return must classify advisory external input | PASS |
| Acceptance criteria | roadmap Acceptance Criteria | observable worker artifacts and gates | PASS |
| Verification/evidence | roadmap Verification / Evidence | required commands and public-sync reads | PASS |
| Dispatch-readiness decision | roadmap Design Control Gate | R64 is docs-only and bounded | PASS |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | local workspace |
| Session or invocation | R64 dispatch authoring at base `8492fc8c3` |
| Agent type | Codex dispatcher |
| Invocation ID | local Codex session, no external invocation ID exposed |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, git, governance checkers, apply_patch |
| Target paths | R64 roadmap, GC-018 baseline, and work order |
| Allowed scope source | operator approved roadmap/work-order after external critique audit |
| Before status evidence | clean worktree for tracked governed files; `Gop y CVF/` is local-excluded advisory input |
| After status evidence | pending dispatch artifacts before commit |
| Diff evidence | `git diff --name-status` before material commit |
| Expected manifest | R64 roadmap, R64 GC-018 baseline, R64 work order |
| Actual changed set | the same three dispatch artifacts, with external folder excluded from git changed-set |
| Manifest delta | none beyond the three planned dispatch artifacts |
| Approval boundary | docs-only dispatch authoring |
| Claim boundary | no public-sync mutation, runtime, checker, provider/live, or source/test edit |
| Deletion or rename disposition | N/A with reason: no deletion or rename authorized |

## 8C. Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: public drift defects will likely be confirmed for
workflow wording, provider certification wording, and stale current-state
indexing; agent-loop discipline will likely be useful as policy/schema but not
runtime enforcement.

Evidence Comparison Requirement: worker return compares actual public-sync and
external-pack evidence against that prediction.

Contradiction Handling Requirement: contradictory evidence must revise or reject
the affected recommendation.

Claim Update Requirement: worker return records confirmed, revised, narrowed,
or invalidated claims.

## Evidence Requirements

Required worker evidence:

- `git rev-parse --short HEAD` at execution start;
- `git status --short --branch` in provenance;
- `rg --files "Gop y CVF"` output count and manifest;
- public-sync `git status --short --branch`;
- public-sync `git remote -v`;
- public-sync `rg` verification for workflow, provider, limitation, docs index,
  routing-guide, cost, governance, and threat/trust terms;
- Required Absorption Table with every atomic external item;
- External Absorption Value Conversion Matrix;
- Overlap And Novelty Classification;
- Public Export Disposition;
- worker-return fast gate result.

Base-anchor evidence:

- `dispatchBaseHead`: `8492fc8c3`
- `executionBaseHead`: worker records at start
- `closureBaseHead`: N/A with reason: reviewer closure follows worker return
- Commit mode: `WORKER_MUST_NOT_COMMIT`

## External Absorption Core

External absorption core: REQUIRED

| Field | Value |
| --- | --- |
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | `Gop y CVF` |
| Enumeration command | `rg --files --hidden --no-ignore "Gop y CVF"` |
| Manifest artifact or inline manifest | `docs/reviews/CVF_MSEA_R64_EXTERNAL_CRITIQUE_INTAKE_AND_PUBLIC_DRIFT_DECISION_WORKER_RETURN_2026-07-07.md`; `docs/reference/CVF_MSEA_R64_EXTERNAL_CRITIQUE_INTAKE_CLASSIFICATION_MATRIX_2026-07-07.md` |
| Processing ledger artifact or inline ledger | `docs/reference/CVF_MSEA_R64_EXTERNAL_CRITIQUE_INTAKE_CLASSIFICATION_MATRIX_2026-07-07.md` |
| Ledger terminal statuses | READ; ADAPTED; DEFERRED; REJECTED; NO_NEW_VALUE; BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB; ADAPT; DEFER; REJECT; BLOCK; NO_NEW_VALUE |
| Owner-surface map | worker maps every accepted/adapted item to public docs, policy/schema, trust/threat, or validator-decision surfaces |
| Unresolved items | worker lists unresolved items with command evidence |
| Completion claim boundary | R64 classifies advisory input only and creates no public/runtime authority |

## Corpus Completeness And Report Integrity

- Corpus task class: COMPARISON
- Corpus root: `Gop y CVF` plus bounded public-sync files named by worker.
- Snapshot time: worker execution time.
- Enumeration command: `rg --files --hidden --no-ignore "Gop y CVF"`
- Manifest artifact or inline manifest: worker return and classification matrix.
- Manifest hash: N/A with reason: no external source import.
- Processing ledger artifact or inline ledger: classification matrix.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=pending_worker ledger_terminal=pending_worker exclusions=pending_worker unresolved=0
- Unresolved files: 0
- Declared exclusions: worker records explicit paths or none.
- Unreadable or unsupported files: worker records explicit paths or none.
- Aggregation check: worker recomputes before return.
- Drift check: public-sync read-only evidence required.
- Output traceability: every actionable item maps to source and owner surface.
- Adversarial verification: at least three contradiction checks.
- Corpus verdict: PARTIAL

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
| --- | --- | --- | --- | --- | --- |
| public drift claims | trust repair value | DOCTRINE_ADAPTED | public README/catalog/limitations/index | R65 decision or repair packet | no runtime/package authority |
| agent-loop discipline claims | loop policy/schema value | DOCTRINE_ADAPTED | work-order/policy/schema docs | R66 admission packet | no runtime enforcement |
| package/template suggestions | possible reusable package value | PACKAGE_CANDIDATE | future package decision surface | hold for separate package packet | no package implementation in R64 |
| runtime-loop suggestions | possible runtime value | RUNTIME_CANDIDATE | future runtime decision surface | hold for separate runtime packet | no runtime implementation in R64 |
| validator/checker suggestions | possible checker value | CHECKER_CANDIDATE | future checker feasibility packet | R68 release-or-hold decision | no checker implementation in R64 |
| direct external file import | no governed value without adaptation | REJECT_DIRECT_IMPORT | N/A with reason | reject direct import | no package/runtime value |
| out-of-scope product claims | no immediate value | NO_PACKAGE_OR_RUNTIME_VALUE | parking or rejection row | R64 matrix disposition | no public readiness claim |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| public workflow wording | `README.md`; `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md` | ENRICH_EXISTING | likely drift to recompute | route to R65 if confirmed |
| provider certification wording | `docs/reference/CVF_PROVIDER_LANE_READINESS_MATRIX.md`; `docs/reference/CVF_KNOWN_LIMITATIONS_REGISTER_2026-04-21.md` | ENRICH_EXISTING | likely stale public limitation text | route to R65 if confirmed |
| agent-loop discipline | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`; `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | NEW_FINDING | candidate policy/schema extension | route to R66 if accepted |
| threat/trust public material | `docs/INDEX.md`; `docs/reference/CVF_BOUNDARY_FIRST_GOVERNANCE_DOCTRINE_2026-05-07.md` | NEW_FINDING | candidate public trust surface | route to R67 if accepted |
| unsupported article metrics | OWNER_SURFACE_NOT_FOUND | OWNER_SURFACE_NOT_FOUND | advisory-only until sourced | block or defer |

## Foundation Storage Layout Block

| Field | Disposition |
| --- | --- |
| storageClass | governed documentation dispatch artifacts |
| durablePathsCreated | R64 roadmap, R64 GC-018 baseline, R64 work order |
| generatedAggregateImpact | none |
| publicSyncImpact | none in R64 |
| runtimeStorageImpact | none |
| layoutBoundary | no relocation, split, source storage, memory/RAG, or private-output storage authority |

## Negative Search And Collision Discipline

The worker must treat missing or colliding terms as evidence, not as inference.
If a token, field, article claim, checker name, public-doc claim, or proposed
policy term has no authoritative source in a CVF-governed source or in the
current public-sync clone, the worker return must record:

- exact search command;
- searched repository or folder;
- term searched;
- exactSearchRoots: provenance workspace governed files, `Gop y CVF/`, and the
  sibling public-sync clone;
- sameTokenCollisionResult: if the same token appears outside the intended
  authority surface, record the collision and mark whether it is authoritative,
  advisory-only, or unrelated;
- resultDisposition: missing authoritative source, advisory-only source,
  public drift confirmed, or no current drift;
- recommended next action.

## Operator Checkpoint

operator.checkpoint.waiver: The operator selected this lane by asking to write
the roadmap and work order after the external critique audit. The worker must
return the classification and decision packet for reviewer closure before any
R65 public-sync or R66 policy/schema implementation can proceed.

## 10. Acceptance Criteria

| Criterion | Required evidence |
| --- | --- |
| External folder fully inventoried | file count and manifest from `rg --files "Gop y CVF"` |
| Every external item classified | Required Absorption Table in worker return |
| Public drift candidates recomputed | public-sync command evidence rows |
| R65/R66/R67/R68 routing recommended | companion matrix disposition rows |
| Boundaries preserved | Claim Boundary and Public Export Disposition in both outputs |
| Worker does not commit | HEAD unchanged and git status records pending owned files |

Fail conditions:

- public-sync edit, commit, or push attempted;
- runtime/source/test/checker file changed;
- provider/live proof run;
- external pack copied into canonical docs without adaptation;
- worker return omits classification table or source verification;
- worker claims runtime enforcement, cost reduction, UX improvement, provider
  parity, or public readiness without evidence.

## 11. Review Gate

Worker handoff is not closure. Reviewer must:

- run worker-return fast gate;
- verify changed paths are inside worker-owned scope;
- inspect semantic value, not only gate shape;
- decide ACCEPT, ACCEPT_WITH_REPAIR, RETURN_FOR_REWORK, or REJECT;
- commit accepted material paths only when reviewer-return steward passes.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Verification Commands

```powershell
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_external_knowledge_intake_routing.py --base 8492fc8c3 --head HEAD --enforce
python governance/compat/check_external_agent_absorption_table.py --base 8492fc8c3 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 8492fc8c3 --head HEAD
```

## 12. Closure Checklist

| Closure item | Required status |
| --- | --- |
| Acceptance criteria | PASS or N/A with reason |
| Worker-return fast gate | PASS before reviewer acceptance |
| Changed-file scope | only worker-owned artifacts |
| Public/provenance boundary | public-sync read-only in R64 |
| Commit mode | WORKER_MUST_NOT_COMMIT preserved |
| Session-sync | separate when material closure changes next move |

## 13. Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` if:

- `Gop y CVF` is missing or unreadable;
- public-sync clone is missing or remote is not public repo;
- worker cannot classify an external item without exceeding scope;
- a needed public-sync fix requires immediate mutation;
- a runtime/checker/provider proof is required to decide an item;
- any required gate fails outside allowed-scope repair.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator-provided critique -> external finding absorption workflow -> worker return and classification matrix -> later governed R65/R66/R67/R68 packets |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py` |
| Owner surface | this work order plus worker-owned output artifacts |
| Disposition | ADAPT as no-commit classification worker dispatch |
| Claim boundary | advisory external critique only; no external item is authority until accepted by reviewer closure |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | R64 worker return and classification matrix | internal agent may classify and recommend under no-commit work order | this work order and baseline | N/A with reason: internal docs decision only | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | future public docs or external-agent review guide if R65/R67 exports | no external adapter or CLI/MCP behavior authorized | future public-sync evidence if accepted | deferred adapter owner; no CLI/MCP runtime in R64 | DEFERRED_WITH_REASON |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R64 dispatch is private provenance work. Public-sync mutation is held
for a later authorized tranche from the sibling public-sync clone.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | R64 external critique intake and public drift decision worker dispatch |
| claimDisposition | N/A with reason: docs-only classification work order |
| receiptEvidence | N/A with reason: worker will create classification evidence, not runtime receipt |
| actionEvidence | N/A with reason: no runtime action authorized |
| invocationBoundary | local file reads, public-sync read-only verification, worker return authoring |
| interceptionBoundary | no IDE, shell, provider, public repository, or remote action interception claim |
| claimLanguage | classify external critique and verify public drift candidates only |
| forbiddenExpansion | public-sync mutation, source/test/runtime/checker edits, provider/live proof, production Memory/RAG, retrieval/vectorization, private-output read, use-case/legal workflow, direct external import, commit, and push remain forbidden |

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| literalTokensReviewed | Dispatch Prompt Envelope; Authority Chain; Agent Roles; Scope; Required First Reads; Pre-Flight Checks; Source Verification Block; Roadmap-To-Work-Order Trace Matrix; Worker Autonomy / No-Question Rule; System Loop Interlock Routing; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Write Ownership; Execution Plan; Evidence Requirements; Acceptance Criteria; Review Gate; Closure Checklist; Return-To-Orchestrator Conditions; External Knowledge Intake Routing; Dual Agent Surface Matrix; Public Export Disposition; Delta Execution Claim Boundary Control Block; DISPATCH_READY; WORKER_MUST_NOT_COMMIT; DEFERRED_PRIVATE_ONLY |
| gateRunPurpose | Gate runs are confirmation/evidence after checker source read-ahead, not first discovery. |
| claimBoundary | Read-ahead covers this R64 work order only. |

## Claim Boundary

This work order dispatches one no-commit docs-only worker classification task.
It does not authorize public-sync mutation, public push, source/test/runtime or
checker edits, provider/live/MCP proof, production Memory/RAG release,
retrieval/vectorization, private/generated MinerU output read, use-case/legal
workflow, direct external source import, runtime enforcement, measured UX/cost
claims, or public/hosted/production readiness claims.
