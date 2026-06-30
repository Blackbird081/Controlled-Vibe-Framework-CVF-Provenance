# CVF Agent Work Order - CGE-R3 CodeGraph Upstream Source Mirror Absorption

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-30

docType: work_order

Batch ID: CGE-R3

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: 3ef56ead

External absorption core: REQUIRED

## Dispatch Prompt Envelope

Role: no-commit worker for CGE-R3 CodeGraph upstream source mirror absorption.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_CGE_R3_CODEGRAPH_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-06-30.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

Base: capture `executionBaseHead` with `git rev-parse --short HEAD` before
edits. Expected dispatch base is `3ef56ead` or the reviewer-provided current
dispatch commit if this packet is committed first.

Current-time notes: current date is 2026-06-30; upstream CodeGraph is pinned at
`da72946d25e112f662f5a60c6b69f363aec60f16`; do not substitute older CGE-R1/R2
snapshot facts for current mirror facts.

Required first actions: read startup surfaces, this work order, the GC-018
baseline, external absorption standards, source mirror index, conditional
reopen index, CGE-R1 owner matrix, CGE-R2 correction, then enumerate the pinned
upstream source mirror before writing conclusions.

Return contract: return `COMPLETE_PENDING_REVIEW`,
`COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, or `BLOCKED_WITH_REASON` with
actual changed paths, executionBaseHead, source mirror commit, manifest count,
manifest hash, processing ledger, value-conversion matrix, gate results, and
HEAD unchanged.

Do-not-misread notes: this work order does not authorize CodeGraph install,
`codegraph init`, `.codegraph/`, MCP server, watcher, daemon, SQLite index,
benchmark, package activation, checker implementation, provider/live proof,
public-sync, direct import, or production-readiness claims.

## Purpose

Run a source-mirror-backed CodeGraph absorption pass against the current
upstream repository, not the old 89-file legacy snapshot. The worker must
produce a file-level review and CVF-owned owner-surface delta that compares
current upstream value against CGE-R1/CGE-R2 without activating runtime.

## Mission

Read and disposition the pinned upstream mirror:

`.private_reference/source_mirrors/colbymchenry__codegraph/`

Pinned commit:

`da72946d25e112f662f5a60c6b69f363aec60f16`

Create:

1. `docs/reviews/CVF_CGE_R3_CODEGRAPH_UPSTREAM_SOURCE_MIRROR_ABSORPTION_REVIEW_2026-06-30.md`
2. `docs/reference/CVF_CGE_R3_CODEGRAPH_UPSTREAM_OWNER_SURFACE_DELTA_2026-06-30.md`

The worker must not commit.

## Authority Chain

| Authority | Path or source | Disposition |
|---|---|---|
| Operator instruction | chat request on 2026-06-30 to return to external repo absorption for CodeGraph | ACCEPT |
| GC-018 baseline | `docs/baselines/CVF_GC018_CGE_R3_CODEGRAPH_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-06-30.md` | ACCEPT |
| Active session front door | `CVF_SESSION_MEMORY.md` | ACCEPT |
| Bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | ACCEPT |
| Active state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V29_2026-06-30.md` | ACCEPT |
| Guard orientation | `docs/reference/guard_orientation/README.md` | ACCEPT |
| External absorption front door | `docs/reference/external_agent_review/README.md` | ACCEPT |
| External absorption chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | ACCEPT |
| External absorption core standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | ACCEPT |
| Source mirror index | `.private_reference/source_mirrors/INDEX.md` | ACCEPT |
| Conditional reopen index | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md` | ACCEPT |
| Prior CGE-R1 owner matrix | `docs/reference/CVF_CGE_R1_CODE_INTELLIGENCE_OWNER_SURFACE_MATRIX_2026-06-29.md` | ACCEPT |
| Prior CGE-R2 correction | `docs/reviews/CVF_CGE_R2_CODEGRAPH_RESCAN_VALUE_AUDIT_AND_CORRECTION_2026-06-29.md` | ACCEPT |

Authority boundary:

- External CodeGraph source is advisory input only.
- The pinned source mirror is preferred for upstream facts.
- Prior CGE-R1/CGE-R2 artifacts are CVF-owned comparison surfaces.
- Any runtime, package activation, checker, resolver, CLI/MCP adapter,
  public output, provider/live proof, or benchmark requires a later fresh
  governed tranche.

## Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | author source-verified dispatch packet and run pre-dispatch gates |
| Worker | no-commit worker role | produce the review and owner-surface delta without committing |
| Reviewer/closer | Codex | review returned artifacts, repair allowed-scope defects, and commit if accepted |
| Session-sync steward | Codex after material acceptance | update active continuity only after accepted material commit if next move changes |
| Operator checkpoint | operator | required for runtime, package activation, checker implementation, public-sync, CodeGraph install/init, benchmark, or live proof |

## Scope

Allowed write scope for worker:

- `docs/reviews/CVF_CGE_R3_CODEGRAPH_UPSTREAM_SOURCE_MIRROR_ABSORPTION_REVIEW_2026-06-30.md`
- `docs/reference/CVF_CGE_R3_CODEGRAPH_UPSTREAM_OWNER_SURFACE_DELTA_2026-06-30.md`

Allowed read scope:

- startup files and current handoff;
- this work order and GC-018 baseline;
- external absorption standards and source mirror index;
- the pinned CodeGraph source mirror;
- prior CGE-R1/CGE-R2/AECG owner and closure artifacts;
- ASSF package contract and existing `cvf-code-intelligence-context-review` registry entry for package-candidate comparison only.

Forbidden scope:

- no edits to source mirror payload, `.private_reference/legacy/`, `EXTENSIONS/`,
  runtime source, `governance/compat/`, hooks, CI, scripts, active session
  state, active handoff, or public-sync files;
- no CodeGraph install, init, index, sync, query, MCP, watcher, daemon,
  benchmark, npm install, provider call, or `.codegraph/` creation;
- no package root, `SKILL.md`, ASSF registry mutation, generated index mutation,
  resolver mutation, checker implementation, or direct source import;
- no commit by the worker.

Risk ceiling: R0 documentation/reference only.

## Pre-Flight Checks

Before implementation, the worker must verify the source mirror exists, the
mirror commit matches this packet, the worktree status is captured, and the
pre-implementation autorun gate either passes or returns a classified blocker.

## Write Ownership

Worker write ownership is limited to the two planned output files named in the
Mission section. Reviewer/closer owns any accepted material commit. Session-sync
steward owns later continuity updates only after material acceptance.

## Evidence Requirements

The worker return must include command-backed source mirror commit, remote, file
count, manifest hash, file-level or grouped processing ledger, value conversion
matrix, owner-surface delta, gate outputs, actual `git status --short`, and
HEAD unchanged evidence.

## Closure Checklist

- [x] Dispatch packet names authority, source mirror, scope, and worker outputs.
- [x] Dispatch packet forbids runtime, package, checker, public, provider, and direct-import work.
- [x] Worker must return manifest reconciliation or a classified blocker.
- [x] Reviewer must run review gates before closure or commit.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when all required worker artifacts and
gate evidence are present. Return `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`
only when limitations are explicit and reconciled. Return `BLOCKED_WITH_REASON`
when source, scope, or gate blockers prevent bounded completion.

## Operator Checkpoint

Operator checkpoint is required before any runtime execution, CodeGraph
install/init, package activation, checker implementation, public-sync, provider
proof, benchmark, or scope expansion beyond the two planned worker files.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, surfaceSelector=`docs/work_orders`, riskCeiling=`HIGH`, maxResults=`20`

Returned defects: NONE_RETURNED

Disclosure note: dispatcher invoked the resolver with the query above and it
returned `totalCandidates=0`.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Active mode permits operator lane selection and requires fresh governed work for broader expansion | `CVF_SESSION_MEMORY.md` | Startup Acknowledgment; Next Allowed Move | `scpl_web_t1_skill_control_plane_web_projection_closed_pending_operator_next_lane_selection` | active session front door | VALUE_SET | ACCEPT |
| Active handoff is V29 and records SCPL-WEB-T1 closure boundary | `AGENT_HANDOFF_V29_2026-06-30.md` | Startup Acknowledgment; Latest Work / Changes | `AGENT_HANDOFF_V29_2026-06-30.md` | active handoff | VALUE_SET | ACCEPT |
| External repo intake must route through manifest, ledger, owner map, and value conversion | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | Central Core; Required Artifact Block; Required Value Conversion Matrix | `External Absorption Core` | external absorption core standard | VALUE_SET | ACCEPT |
| High-value upstream repo absorption should use a source mirror when available | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | Source Mirror Discipline | `.private_reference/source_mirrors/` | external absorption core standard | LITERAL_INVARIANT | ACCEPT |
| Source mirror index records the CodeGraph pinned mirror | `.private_reference/source_mirrors/INDEX.md` | Mirror Ledger | `colbymchenry__codegraph` | source mirror index | VALUE_SET | ACCEPT |
| Local mirror is pinned to upstream HEAD | `.private_reference/source_mirrors/INDEX.md` | Mirror Ledger | `colbymchenry__codegraph` | source mirror index | VALUE_SET | ACCEPT |
| Local mirror contains 409 non-git files | `.private_reference/source_mirrors/INDEX.md` | Mirror Ledger | `Tracked file count` | source mirror index | VALUE_SET | ACCEPT |
| CodeGraph package identity and CLI bin are visible | `.private_reference/source_mirrors/colbymchenry__codegraph/package.json` | line 2; line 3; line 7 | `@colbymchenry/codegraph`; `1.1.6`; `bin.codegraph` | package.json | VALUE_SET | ACCEPT |
| Upstream source exposes CLI/MCP/index/watch surfaces that remain runtime candidates only | `.private_reference/source_mirrors/colbymchenry__codegraph/README.md` | command and MCP usage sections | `codegraph mcp`; `codegraph watch`; `codegraph index` | upstream README | VALUE_SET | ACCEPT |
| Current conditional reopen index parks CodeGraph runtime, package, and checker candidates | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md` | Candidate Index | `CGE-R2-code-intelligence-runtime-value-probe`; `CGE-code-intelligence-package-candidate`; `CGE-code-intelligence-checker-candidates` | conditional reopen index | VALUE_SET | ACCEPT |

## Current Runtime Freshness Verification

| Claim checked | Verification command | Observed result | Disposition |
|---|---|---|---|
| CVF root has no active CodeGraph project index | `Test-Path '.codegraph'` | `False` | ACCEPT |
| CVF runtime extension is not present | `Test-Path 'EXTENSIONS/CVF_CODE_INTELLIGENCE_CAPABILITY'` | `False` | ACCEPT |
| Code intelligence ASSF package root is not present | `Test-Path 'docs/reference/agent_system_skills/packages/cvf-code-intelligence-context-review/SKILL.md'` | `False` | ACCEPT |
| CodeGraph-specific checker is not present | `Test-Path 'governance/compat/check_codegraph_staleness.py'` | `False` | ACCEPT |
| Metadata-only ASSF candidate exists but remains candidate state | `Get-Content -Raw 'docs/reference/agent_system_skills/registry/entries/cvf-code-intelligence-context-review.json'` | `status` is `CANDIDATE`; `candidateState` is `CANDIDATE`; `externalCliMcpDisposition` is `DEFERRED_WITH_REASON` | ACCEPT |

Freshness boundary: these checks support only the negative runtime/package/
checker claim boundary for CGE-R3 dispatch. They do not prove absence of every
possible future CodeGraph-related string, and they do not authorize runtime
activation.

## New Doc-Only Fields Table

| New doc-only file | Purpose | Runtime claim blocked? | Validation expectation |
|---|---|---|---|
| `docs/reviews/CVF_CGE_R3_CODEGRAPH_UPSTREAM_SOURCE_MIRROR_ABSORPTION_REVIEW_2026-06-30.md` | worker-return-style upstream mirror absorption review with manifest, ledger, and value conversion | Yes | worker-return fast gate plus external absorption/corpus guards |
| `docs/reference/CVF_CGE_R3_CODEGRAPH_UPSTREAM_OWNER_SURFACE_DELTA_2026-06-30.md` | CVF-owned delta surface for upstream CodeGraph concepts compared to CGE-R1/CGE-R2 | Yes | reviewer-fast and external intake/value-conversion guards |

## Roadmap-To-Work-Order Trace Matrix

| Prior requirement or operator instruction | Work order response | Output artifact | Status |
|---|---|---|---|
| Operator selected CodeGraph as next external repo absorption target | dispatch source-mirror-backed CGE-R3 worker review | CGE-R3 review | DISPATCHED_BY_THIS_PACKET |
| External absorption rules prefer upstream mirror for high-value repo facts | source mirror pinned and indexed before worker execution | source mirror index plus CGE-R3 review | DISPATCHED_BY_THIS_PACKET |
| CGE-R1/CGE-R2 used bounded legacy snapshot and parked runtime/package/checker value | require comparison against current upstream mirror and conditional reopen rows | owner-surface delta | DISPATCHED_BY_THIS_PACKET |
| Runtime/MCP/package/checker remain parked | forbid implementation and require candidate-only classification | claim boundary and value matrix | DISPATCHED_BY_THIS_PACKET |

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake type | external repo source-mirror absorption |
| Intake summary | operator selected CodeGraph upstream repo after SCPL-WEB-T1 session state; dispatch pins upstream source mirror before worker absorption |
| Scope classification | bounded documentation/reference worker; source mirror payload is read-only and ignored by git |
| Risk sensitivity | low runtime risk if forbidden scope is obeyed; high governance risk if worker overclaims runtime, MCP, package, checker, provider, public, or production value |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | worker returns uncommitted material artifacts to reviewer/closer; session-sync steward acts only after material acceptance |
| Worker role | no-commit documentation/reference worker |
| Reviewer role | reviewer/closer after worker return |
| Runtime role | NOT_APPLICABLE_WITH_REASON: runtime implementation is forbidden in CGE-R3 |
| Package role | NOT_APPLICABLE_WITH_REASON: package mutation is forbidden in CGE-R3; package value is classification only |
| Checker role | NOT_APPLICABLE_WITH_REASON: checker implementation is forbidden in CGE-R3; checker value is classification only |
| Escalation condition | return `BLOCKED_WITH_REASON` if source mirror is missing, pinned commit drifts, source authority files are missing, or completion would require forbidden scope |

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
|---|---|
| Coverage index status | NOT_APPLICABLE_WITH_REASON |
| Canonical coverage index | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` |
| Reason | CGE-R3 consumes a pinned upstream source mirror, not a legacy coverage-index closure wave |
| Controlling evidence | External Absorption Core, source mirror index, corpus completeness, and value conversion matrix in this work order |
| Required worker evidence | full upstream source-mirror manifest, processing ledger, value conversion matrix, and owner-surface delta |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation Storage Layout Block | N/A with reason: CGE-R3 dispatch does not split, relocate, refactor, or redesign durable foundation storage layout; it only updates the source mirror index and dispatch artifacts |
| Protected storage paths | N/A with reason: no foundation storage topology path is changed |
| Follow-up condition | separate governed work order required before any storage-layout implementation |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| contractSource | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | dispatcher -> worker -> reviewer/closer -> session-sync steward |
| phase | DISPATCH_AUTHORING; EXECUTION; REVIEWER_CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | dispatchBaseHead=`3ef56ead`; executionBaseHead=worker captures with `git rev-parse --short HEAD`; closureBaseHead=reviewer captures before material commit |
| changedSetScope(phase) | worker may change only the planned CGE-R3 review and owner-surface delta |
| traceScope(phase, actor) | worker return must include Agent Operation Trace Block with expected and actual manifest |
| commitOwner(phase) | worker must not commit; reviewer/closer owns material commit if accepted; session-sync steward owns separate session-sync commit if needed |
| crossBatchIsolation | worker material artifacts must not be mixed with session/handoff sync or runtime/package/checker work |
| nextMoveSurfaces | worker must not edit; reviewer/session-sync steward updates after accepted material commit if next move changes |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_CGE_R3_CODEGRAPH_UPSTREAM_SOURCE_MIRROR_ABSORPTION_COMPLETION_2026-06-30.md` |
| reviewerOwnedClosurePaths | worker review and owner-surface delta only; session-sync paths remain separate |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | CGE-R3 review and owner-surface delta | internal CVF agents may read reference output only; no action authority | this work order and baseline | N/A with reason: no internal runtime adapter is implemented | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | future CLI/MCP adapter owner, not CGE-R3 | external agent use requires separate source-verified adapter/runtime authorization | upstream CodeGraph has MCP surfaces; CVF has not implemented them | deferred adapter owner; no ingress, auth, mutation, raw-data, receipt, or public boundary is implemented here | DEFERRED_WITH_REASON |

## Package Skill Productionization Control Block

- SOP source: docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md
- Current phase: N/A with reason: CGE-R3 is an external absorption review dispatch, not a package-skill productionization phase.
- Target lifecycle state: CANDIDATE_ONLY_REFERENCE
- Prior phase evidence: existing `cvf-code-intelligence-context-review` registry entry remains `CANDIDATE`; worker may evaluate value only.
- Next forbidden skip: worker must not create package root, `SKILL.md`, generated package index, truth packet, ACTIVE state, certification, runtime eligibility, or activation evidence.
- Runtime/provider proof: N/A with reason: runtime/provider proof is forbidden in this work order.
- Claim boundary: package-related findings may be recorded only as candidate evidence for a future source-verified package work order.

## Worker Autonomy / No-Question Rule

The worker proceeds without operator confirmation for non-destructive actions
inside Allowed scope: reading files, enumerating the mirror, creating the two
planned artifacts, repairing format defects inside those artifacts, and rerun
of applicable gates.

Escalation is reserved for missing mirror, missing authority files, unreadable
source that prevents a bounded conclusion, request to install/run CodeGraph,
live/provider proof, public-sync, package/checker/runtime implementation,
session-state edits, destructive actions, or scope expansion.

## External Absorption Core

| Field | Value |
|---|---|
| Standard | docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md |
| Input root or repository | `https://github.com/colbymchenry/codegraph.git` at `da72946d25e112f662f5a60c6b69f363aec60f16`; local mirror `.private_reference/source_mirrors/colbymchenry__codegraph/` |
| Enumeration command | `Get-ChildItem -LiteralPath ".private_reference/source_mirrors/colbymchenry__codegraph" -Recurse -File -Force` excluding `.git` |
| Manifest artifact or inline manifest | inline `## Dispatch Source Mirror Manifest` table in this file; worker must create full manifest in planned review |
| Processing ledger artifact or inline ledger | planned worker review under `docs/reviews/CVF_CGE_R3_CODEGRAPH_UPSTREAM_SOURCE_MIRROR_ABSORPTION_REVIEW_2026-06-30.md` |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | planned `docs/reference/CVF_CGE_R3_CODEGRAPH_UPSTREAM_OWNER_SURFACE_DELTA_2026-06-30.md` |
| Unresolved items | 409 unresolved at dispatch; worker must reduce to 0 or return with limitations/blocker |
| Completion claim boundary | dispatch and source-mirror intake only; no runtime, provider/live, public, production, MCP, watcher, daemon, SQLite index, checker, or package activation |

## Corpus Completeness And Report Integrity

- Corpus task class: upstream external repository absorption dispatch.
- Corpus root: `.private_reference/source_mirrors/colbymchenry__codegraph/`.
- Snapshot time: 2026-06-30 local session.
- Enumeration command: `Get-ChildItem -LiteralPath ".private_reference/source_mirrors/colbymchenry__codegraph" -Recurse -File -Force` excluding `.git`.
- Manifest artifact or inline manifest: dispatch preflight count and hash recorded here; full manifest required in worker review.
- Manifest hash: `sha256:7ada7481a4a5cb63417fb839c852b62011aa46cfbdc598a3332d61ae4029de17`.
- Processing ledger artifact or inline ledger: planned worker review.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE
- Reconciliation: manifest=409; ledger_terminal=0 at dispatch; exclusions=0; unresolved=409.
- Unresolved files: 409 at dispatch.
- Declared exclusions: none at dispatch.
- Unreadable or unsupported files: none known at dispatch.
- Aggregation check: dispatch proves source mirror availability, not absorption completion.
- Drift check: worker must recompute count, commit, and manifest hash before processing.
- Output traceability: worker maps accepted value to CVF owner surfaces or returns blocked source gaps.
- Adversarial verification: prior CGE-R1/CGE-R2 snapshot conclusions must be challenged against the current 409-file upstream mirror.
- Corpus verdict: PARTIAL

## Mandatory Blind-Spot Control Block

| Field | Disposition |
|---|---|
| Trigger source | `.private_reference/source_mirrors/colbymchenry__codegraph/` |
| Control disposition | APPLICABLE |
| Corpus completeness section | PRESENT |
| Completeness trigger model | scope-triggered upstream external source mirror absorption |
| Blind-spot prevention action | worker must enumerate and reconcile all non-git source mirror files before accepting or rejecting value |
| Residual gap | worker must return `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW` or `BLOCKED_WITH_REASON` if any manifest item cannot receive a terminal disposition |

## Dispatch Source Mirror Manifest

| Manifest item | Evidence |
|---|---|
| Upstream repository | `https://github.com/colbymchenry/codegraph.git` |
| Pinned commit | `da72946d25e112f662f5a60c6b69f363aec60f16` |
| Local mirror path | `.private_reference/source_mirrors/colbymchenry__codegraph/` |
| Non-git file count | 409 |
| Manifest hash | `sha256:7ada7481a4a5cb63417fb839c852b62011aa46cfbdc598a3332d61ae4029de17` |
| Full file-level manifest | REQUIRED in planned worker review |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | external repo or copied folder -> pinned source mirror -> external absorption core -> full manifest and processing ledger -> value conversion matrix -> CVF owner-surface delta -> future package/runtime/checker work order only if separately authorized |
| Matching local-view guard | `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_source_mirror_migration.py` |
| Owner surface | `docs/reviews/CVF_CGE_R3_CODEGRAPH_UPSTREAM_SOURCE_MIRROR_ABSORPTION_REVIEW_2026-06-30.md`; `docs/reference/CVF_CGE_R3_CODEGRAPH_UPSTREAM_OWNER_SURFACE_DELTA_2026-06-30.md` |
| Disposition | DISPATCH upstream source-mirror absorption review |
| Claim boundary | dispatch only; no runtime, package activation, checker wiring, provider/live proof, public-sync, MCP server, watcher, daemon, benchmark, or production-readiness claim |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| Upstream source mirror control plane | Current CodeGraph source authority is now pinned for future absorption. | DOCTRINE_ADAPTED | `.private_reference/source_mirrors/INDEX.md` | Use upstream mirror as source authority for CGE-R3 facts. | No runtime or package behavior |
| Upstream README, docs, and design notes | New upstream material may refine code-intelligence doctrine and value-probe design beyond the 89-file legacy snapshot. | DOCTRINE_ADAPTED | planned CGE-R3 owner-surface delta | Worker reads and maps deltas to CVF language. | Documentation/reference only |
| `package.json`, CLI, MCP, installer, sync, graph, db, and tests | CodeGraph is a real package and runtime candidate, but activation remains parked. | RUNTIME_CANDIDATE | conditional reopen index CGE rows and planned CGE-R3 review | Worker may classify value; implementation requires fresh runtime work order. | No install, init, MCP server, watcher, daemon, SQLite index, or provider/live proof |
| Package identity and agent-facing usage model | Package candidate may enrich existing `cvf-code-intelligence-context-review` metadata after value proof. | PACKAGE_CANDIDATE | existing ASSF candidate plus planned CGE-R3 delta | Worker may recommend metadata changes only; mutation needs separate package work order. | No package root, `SKILL.md`, ACTIVE state, resolver, or activation |
| Staleness, scope, security, response-shape, and trace tests | Checker candidates may harden future graph-assisted work if real misses appear. | CHECKER_CANDIDATE | conditional reopen index and planned CGE-R3 review | Worker may record candidate evidence and reopen condition. | No Python checker or hook-chain wiring |
| Upstream implementation files and workflows | Direct import remains unsafe and non-authoritative. | REJECT_DIRECT_IMPORT | CVF-native rewrite lanes only | Worker rejects direct copy/wiring and records reasons. | No direct source import |
| Duplicate or marketing-only files after full read | Some files may add no CVF-native doctrine/package/runtime/checker delta. | NO_PACKAGE_OR_RUNTIME_VALUE | worker ledger | Worker records explicit no-new-value reason. | No runtime or package behavior |

## Execution Plan

1. Capture `executionBaseHead`, `git status --short`, source mirror commit,
   source mirror remote, file count, and manifest hash.
2. Read required CVF authority and prior CGE artifacts.
3. Enumerate all non-git files in the pinned source mirror.
4. Read or terminally disposition every manifest item.
5. Produce the upstream absorption review with manifest, processing ledger,
   value conversion, conditional reopen handling, and claim boundary.
6. Produce the owner-surface delta in CVF language.
7. Run worker gates and return without committing.

## Required First Reads

Before editing worker output, read:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V29_2026-06-30.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- this work order
- `docs/baselines/CVF_GC018_CGE_R3_CODEGRAPH_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-06-30.md`
- `docs/reference/external_agent_review/README.md`
- `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`
- `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md`
- `.private_reference/source_mirrors/INDEX.md`
- `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md`
- `docs/reference/CVF_CGE_R1_CODE_INTELLIGENCE_OWNER_SURFACE_MATRIX_2026-06-29.md`
- `docs/reviews/CVF_CGE_R2_CODEGRAPH_RESCAN_VALUE_AUDIT_AND_CORRECTION_2026-06-29.md`
- `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md`
- `docs/reference/agent_system_skills/registry/entries/cvf-code-intelligence-context-review.json`

## Pre-Implementation Commands

Worker must run and record:

```powershell
git rev-parse --short HEAD
git status --short
git -C ".private_reference/source_mirrors/colbymchenry__codegraph" rev-parse HEAD
git -C ".private_reference/source_mirrors/colbymchenry__codegraph" remote -v
(Get-ChildItem -LiteralPath ".private_reference/source_mirrors/colbymchenry__codegraph" -Recurse -File -Force | Where-Object { $_.FullName -notmatch "\\.git\\" }).Count
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

Worker must stop if the mirror is missing or if the pinned commit differs from
the work-order value without a reviewer update.

## Worker Execution Requirements

The worker must:

1. enumerate all source mirror files with a filesystem-backed command;
2. read every manifest file or mark it `BLOCKED_UNREADABLE` with reason;
3. produce a processing ledger with terminal rows or explicit grouped rows
   whose counts reconcile to the manifest;
4. compare upstream value against CGE-R1/CGE-R2 and name changed, added,
   duplicate, rejected, or still-parked value;
5. classify doctrine, package, runtime, checker, direct-import rejection, and
   no-package/runtime opportunities explicitly;
6. update or cite conditional reopen rows when package/runtime/checker value
   remains parked;
7. keep all accepted value in CVF-owned language;
8. return with no commit and actual `git status --short`.

## Worker Return Packet Shape Contract

Path:

`docs/reviews/CVF_CGE_R3_CODEGRAPH_UPSTREAM_SOURCE_MIRROR_ABSORPTION_REVIEW_2026-06-30.md`

Required sections:

- Purpose
- Target
- Scope / Methodology
- Findings / Position
- Risk / Corrective Action
- Decision / Disposition
- Worker Status
- Source Inventory
- Corpus Manifest
- Processing Ledger
- Absorption Disposition Ledger
- External Absorption Core
- Corpus Completeness And Report Integrity
- External Knowledge Intake Routing
- External Absorption Value Conversion Matrix
- Owner-Surface Map
- Package Candidate Evaluation
- Runtime Candidate Evaluation
- Checker Candidate Evaluation
- Direct Import Rejection Ledger
- Conditional Reopen Index Disposition
- Source Verification Block
- Roadmap-To-Work-Order Trace Matrix
- Rescan Intelligence Hardening
- Finding-To-Governance Learning Disposition
- Epistemic Process Block
- Delta Execution Claim Boundary Control Block
- Agent Operation Trace Block
- Public Export Disposition
- Claim Boundary

Required status token: `COMPLETE_PENDING_REVIEW`,
`COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW`, or `BLOCKED_WITH_REASON`.

The worker return must record `executionBaseHead`, actual `git status --short`,
the `Machine Closure Package` section, and explicit `N/A with reason` or
`NOT_APPLICABLE_WITH_REASON` for non-applicable conditional blocks.

## Owner-Surface Delta Contract

Path:

`docs/reference/CVF_CGE_R3_CODEGRAPH_UPSTREAM_OWNER_SURFACE_DELTA_2026-06-30.md`

Required content:

- status `ACTIVE_REFERENCE_PENDING_REVIEW` or `DRAFT_PENDING_REVIEW`;
- Source Authority table that keeps CodeGraph advisory and source-mirror based;
- delta table against CGE-R1/CGE-R2;
- doctrine additions or confirmations;
- package/runtime/checker candidate delta;
- rejected direct import delta;
- Dual Agent Surface Matrix;
- External Knowledge Intake Routing;
- External Absorption Value Conversion Matrix;
- Public Export Disposition;
- Claim Boundary.

## Acceptance Criteria

| Criterion | Evidence |
|---|---|
| worker verifies source mirror commit and count | command output in worker return |
| worker enumerates pinned upstream corpus | manifest count and hash |
| every manifest item reaches terminal ledger status or explicit limitation | reconciliation row |
| useful value is converted into CVF language | owner-surface delta |
| package/runtime/checker opportunities are evaluated | value conversion matrix includes all required lane tokens |
| direct import remains rejected | rejection ledger and claim boundary |
| no forbidden path changed | `git status --short`; reviewer diff |
| worker does not commit | HEAD unchanged from executionBaseHead |
| gates run or blockers are classified | worker-return fast gate and external absorption/corpus guards recorded |

## Fail Conditions

| Fail condition | Required action |
|---|---|
| source mirror missing | return `BLOCKED_WITH_REASON` |
| mirror commit differs without reviewer update | return `BLOCKED_WITH_REASON` |
| worker reads only filenames or samples without reconciled ledger | return `BLOCKED_WITH_REASON` or `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW` |
| worker creates runtime/source/checker/package/session/public files | return `BLOCKED_WITH_REASON`; reviewer rejects |
| worker runs CodeGraph or creates `.codegraph/` | return `BLOCKED_WITH_REASON`; reviewer rejects |
| worker promotes external source as CVF authority | return `BLOCKED_WITH_REASON` |
| gate failure cannot be repaired inside allowed scope | return `BLOCKED_WITH_REASON` |

## Review Gate

Reviewer validation should run at minimum:

```powershell
python governance/compat/check_external_absorption_core.py --base <closureBaseHead> --head HEAD --enforce
python governance/compat/check_external_absorption_value_conversion.py --base <closureBaseHead> --head HEAD --enforce
python governance/compat/check_external_knowledge_intake_routing.py --base <closureBaseHead> --head HEAD --enforce
python governance/compat/check_corpus_completeness_report_integrity.py --base <closureBaseHead> --head HEAD --enforce
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return --base <closureBaseHead> --head HEAD --enforce
```

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher |
| Provider or surface | local workspace |
| Session or invocation | CGE-R3 CodeGraph upstream source mirror absorption dispatch, 2026-06-30 |
| Working directory | repository root |
| Command or tool surface | git, Get-ChildItem, Select-String, rg, apply_patch, governance gates |
| Target paths | `.private_reference/source_mirrors/INDEX.md`; `docs/baselines/CVF_GC018_CGE_R3_CODEGRAPH_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-06-30.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CGE_R3_CODEGRAPH_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-06-30.md` |
| Allowed scope source | operator instruction to return to external repo absorption for CodeGraph under new rules |
| Agent type | dispatcher |
| Invocation ID | CGE-R3-dispatch-2026-06-30 |
| Expected manifest | `.private_reference/source_mirrors/INDEX.md`; `docs/baselines/CVF_GC018_CGE_R3_CODEGRAPH_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-06-30.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CGE_R3_CODEGRAPH_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-06-30.md` |
| Actual changed set | `.private_reference/source_mirrors/INDEX.md`; `docs/baselines/CVF_GC018_CGE_R3_CODEGRAPH_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-06-30.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CGE_R3_CODEGRAPH_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-06-30.md` |
| Manifest delta | MATCH |
| Before status evidence | clean worktree at `3ef56ead` before source mirror and dispatch edits |
| After status evidence | dispatch artifacts pending gate verification |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | source mirror control-plane and dispatch authoring only |
| Claim boundary | no runtime, provider/live, public, production, package activation, checker wiring, MCP server, watcher, daemon, SQLite index, or direct import |
| Deletion or rename disposition | N/A with reason: no tracked deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | CGE-R3 source-mirror-backed external absorption dispatch only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT - dispatch records source mirror commit, count, manifest hash, and required worker receipts |
| actionEvidence | ACTION_EVIDENCE_PRESENT - source mirror index row, GC-018 baseline, and work order created |
| invocationBoundary | local documentation and private source-mirror control-plane authoring only |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | upstream source-mirror absorption dispatch and planned worker review |
| forbiddenExpansion | no CodeGraph install/init/MCP/watcher/daemon/SQLite index, package activation, checker implementation, provider/live proof, public-sync, benchmark, CI mutation, direct import, or production-readiness claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: CGE-R3 uses a private source mirror and private provenance comparison
surfaces. Public-safe export requires separate public-sync authorization.

## Claim Boundary

This work order authorizes only a no-commit documentation/reference worker
tranche for upstream CodeGraph source-mirror absorption review and owner-surface
delta. It does not authorize runtime code, package root creation, ASSF registry
mutation, generated index mutation, checker implementation, CLI/MCP adapter
work, provider/live proof, public-sync, benchmark claims, CodeGraph install,
init, watcher, daemon, merge automation, hook repair, package activation,
certification, or production readiness.
