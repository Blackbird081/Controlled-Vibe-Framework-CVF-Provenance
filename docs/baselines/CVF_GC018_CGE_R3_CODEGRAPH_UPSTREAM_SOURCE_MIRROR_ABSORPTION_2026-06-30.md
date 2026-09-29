# CVF GC-018 - CGE-R3 CodeGraph Upstream Source Mirror Absorption

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: baseline

Date: 2026-06-30

Batch ID: CGE-R3

dispatchBaseHead: 3ef56ead

External absorption core: REQUIRED

## Purpose

Authorize a bounded upstream-source absorption lane for
`colbymchenry/codegraph` after the operator selected CodeGraph as the next
external knowledge absorption target.

CGE-R3 exists because prior CGE-R1/CGE-R2 work used a retained local snapshot,
while current external absorption rules prefer a pinned upstream source mirror
when the upstream repository is available. This baseline authorizes dispatch
only: a no-commit worker may read the pinned upstream mirror, produce a
manifest, processing ledger, value-conversion matrix, and comparison against
CGE-R1/CGE-R2 owner surfaces.

## Decision / Baseline / Proposed Tranche

Decision: dispatch CGE-R3 as a source-mirror-backed external absorption
worker tranche.

Baseline: CodeGraph is advisory external source material pinned in a private
source mirror. CVF-owned conclusions must be recorded in governed review and
reference artifacts, not imported from upstream source.

Proposed tranche: no-commit worker produces the CGE-R3 review and
owner-surface delta named in the planned worker fulfillment manifest.

## Scope / Target / Owner Boundary

Target source:

`https://github.com/colbymchenry/codegraph.git`

Pinned commit:

`da72946d25e112f662f5a60c6b69f363aec60f16`

Local mirror:

`.private_reference/source_mirrors/colbymchenry__codegraph/`

Allowed write scope:

- `.private_reference/source_mirrors/INDEX.md`
- `docs/baselines/CVF_GC018_CGE_R3_CODEGRAPH_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-06-30.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_CGE_R3_CODEGRAPH_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-06-30.md`
- planned worker output under `docs/reviews/` and `docs/reference/` named by the work order only

Forbidden scope:

- no CodeGraph install, init, `codegraph` CLI execution, `.codegraph/`
  creation, MCP server, watcher, daemon, SQLite index, benchmark, provider
  call, public-sync, package activation, resolver mutation, checker wiring, or
  direct external source import;
- no changes inside the cloned source mirror payload;
- no `EXTENSIONS/`, runtime source, hook-chain, CI, `scripts/`, or
  `governance/compat/` implementation changes in CGE-R3 dispatch;
- no session-state or active-handoff edits by the worker.

Risk ceiling: R0 documentation/reference and private source-mirror control
plane only.

## Authority Chain

| Authority | Path or source | Disposition |
|---|---|---|
| Operator instruction | chat request on 2026-06-30 to return to external repo absorption for CodeGraph | ACCEPT |
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

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Active mode permits operator lane selection and requires fresh governed work for broader expansion | `CVF_SESSION_MEMORY.md` | Startup Acknowledgment; Next Allowed Move | `scpl_web_t1_skill_control_plane_web_projection_closed_pending_operator_next_lane_selection` | active session front door | VALUE_SET | ACCEPT |
| Active handoff is V29 and records SCPL-WEB-T1 closure boundary | `AGENT_HANDOFF_V29_2026-06-30.md` | Startup Acknowledgment; Latest Work / Changes | `AGENT_HANDOFF_V29_2026-06-30.md` | active handoff | VALUE_SET | ACCEPT |
| External repo intake must route through manifest, ledger, owner map, and value conversion | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | Central Core; Required Artifact Block; Required Value Conversion Matrix | `External Absorption Core` | external absorption core standard | VALUE_SET | ACCEPT |
| High-value upstream repo absorption should use a source mirror when available | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | Source Mirror Discipline | `.private_reference/source_mirrors/` | external absorption core standard | LITERAL_INVARIANT | ACCEPT |
| Current source mirror index has a CodeGraph row after this dispatch update | `.private_reference/source_mirrors/INDEX.md` | Mirror Ledger | `colbymchenry__codegraph` | source mirror index | VALUE_SET | ACCEPT |
| CodeGraph upstream HEAD was verified before mirror creation | `.private_reference/source_mirrors/INDEX.md` | Mirror Ledger | `da72946d25e112f662f5a60c6b69f363aec60f16` | source mirror index | VALUE_SET | ACCEPT |
| Local mirror is pinned to upstream HEAD | `.private_reference/source_mirrors/INDEX.md` | Mirror Ledger | `colbymchenry__codegraph` | source mirror index | VALUE_SET | ACCEPT |
| Local mirror contains 409 non-git files | `.private_reference/source_mirrors/INDEX.md` | Mirror Ledger | `Tracked file count` | source mirror index | VALUE_SET | ACCEPT |
| CodeGraph package identity is visible in upstream package metadata | `.private_reference/source_mirrors/colbymchenry__codegraph/package.json` | line 2; line 3; line 7 | `@colbymchenry/codegraph`; `1.1.6`; `bin.codegraph` | package.json | VALUE_SET | ACCEPT |
| Upstream source exposes CLI/MCP/index/watch surfaces that remain runtime candidates only | `.private_reference/source_mirrors/colbymchenry__codegraph/README.md` | command and MCP usage sections | `codegraph mcp`; `codegraph watch`; `codegraph index` | upstream README | VALUE_SET | ACCEPT |
| CodeGraph runtime/package/checker candidates already have parked reopen conditions | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md` | Candidate Index | `CGE-R2-code-intelligence-runtime-value-probe`; `CGE-code-intelligence-package-candidate`; `CGE-code-intelligence-checker-candidates` | conditional reopen index | VALUE_SET | ACCEPT |

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

## Evidence / Verification

Dispatch verification is bounded to source mirror creation, source mirror index
control-plane update, runtime-freshness negative checks, and pre-dispatch
governance gates. Absorption completion evidence is assigned to the worker
review and must not be claimed by this dispatch baseline.

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
| Owner-surface map | planned update or supplement to `docs/reference/CVF_CGE_R3_CODEGRAPH_UPSTREAM_OWNER_SURFACE_DELTA_2026-06-30.md` |
| Unresolved items | 409 unresolved at dispatch; worker must reduce to 0 or return `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
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

## Rescan Intelligence Hardening

- Original source artifact:
  `docs/reference/CVF_CGE_R1_CODE_INTELLIGENCE_OWNER_SURFACE_MATRIX_2026-06-29.md`
- Predecessor intake artifact:
  `docs/reviews/CVF_CGE_R2_CODEGRAPH_RESCAN_VALUE_AUDIT_AND_CORRECTION_2026-06-29.md`
- Delta ledger status: PARTIAL - dispatch identifies that prior 89-file
  snapshot conclusions must be challenged against the 409-file upstream mirror.
- Routing matrix status: DO_NOW for no-commit source-mirror absorption review;
  SEPARATE_RUNTIME_TRANCHE for runtime/package/checker implementation;
  OUT_OF_SCOPE for public-sync and direct import.
- Semantic sampling status: PARTIAL - dispatch samples mirror identity,
  package metadata, and runtime-boundary claims; worker must complete full
  manifest review.
- Rescan intelligence verdict: PARTIAL

### Original-Intake Delta Ledger

| Delta category | Status |
|---|---|
| UNCHANGED_FROM_INTAKE | CodeGraph remains advisory external source material, not CVF source of truth. |
| CHANGED_DISPOSITION | Source authority changes from retained legacy snapshot to pinned upstream mirror for CGE-R3. |
| NEW_FINDING | Current upstream mirror contains 409 non-git files and requires fresh worker reconciliation. |
| REMOVED_OR_REJECTED | Direct source import, runtime execution, MCP, watcher, daemon, SQLite index, and package activation remain rejected for this dispatch. |

### Follow-Up Routing Matrix

| Routing lane | Status |
|---|---|
| DO_NOW | Dispatch no-commit worker absorption review and owner-surface delta. |
| SEPARATE_RUNTIME_TRANCHE | Any CodeGraph install/init, runtime integration, MCP adapter, checker implementation, package mutation, or provider/live proof. |
| STRATEGIC_OPERATOR_DECISION | Operator must select whether later CodeGraph value becomes runtime, package, checker, or roadmap work. |
| OUT_OF_SCOPE | Public-sync, benchmark, production-readiness claim, direct import, and session-state mutation. |
| RESOLVED_BY_DESIGN | Private source mirror is read-only and ignored; CVF-owned outputs carry conclusions. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| CGE-R3-B-RS1 | source mirror index | upstream commit is pinned | DO_NOW | Could worker rely on stale local snapshot instead of current mirror? | PASS_PINNED_MIRROR_REQUIRED |
| CGE-R3-B-RS2 | package metadata | CodeGraph is a real package with CLI identity | SEPARATE_RUNTIME_TRANCHE | Could package identity be mistaken for CVF activation authority? | PASS_RUNTIME_BOUNDARY_EXPLICIT |
| CGE-R3-B-RS3 | scope boundary | runtime/MCP/package/checker work is forbidden | OUT_OF_SCOPE | Could dispatch be read as implementation permission? | PASS_BOUNDARY_EXPLICIT |

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
| Owner surface | `docs/baselines/CVF_GC018_CGE_R3_CODEGRAPH_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-06-30.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CGE_R3_CODEGRAPH_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-06-30.md` |
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

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | planned CGE-R3 review and owner-surface delta | internal CVF agents may read documentation/reference output only; no action authority | this baseline and work order | N/A with reason: no internal runtime adapter is implemented | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | future CLI/MCP adapter owner, not this dispatch | external agent use requires separate source-verified adapter/runtime authorization | CodeGraph upstream has MCP surfaces, but CVF has not implemented them | deferred adapter owner; no ingress, auth, mutation, raw-data, receipt, or public boundary is implemented here | DEFERRED_WITH_REASON |

## Package Skill Productionization Control Block

- SOP source: docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md
- Current phase: N/A with reason: CGE-R3 dispatch does not create, approve, activate, or mutate a package skill.
- Target lifecycle state: CANDIDATE_ONLY_REFERENCE
- Prior phase evidence: existing `cvf-code-intelligence-context-review` registry entry remains `CANDIDATE`; no package root exists.
- Next forbidden skip: no package root, `SKILL.md`, generated index mutation, truth packet, activation, certification, or runtime eligibility claim may be created in CGE-R3.
- Runtime/provider proof: N/A with reason: package productionization and runtime/provider proof are forbidden by this dispatch boundary.
- Claim boundary: package value may be classified only as future candidate evidence for a separately authorized package work order.

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| contractSource | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | dispatcher -> worker -> reviewer/closer -> session-sync steward |
| phase | DISPATCH_AUTHORING; EXECUTION; REVIEWER_CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | dispatchBaseHead=`3ef56ead`; executionBaseHead=worker captures with `git rev-parse --short HEAD`; closureBaseHead=reviewer captures before material commit |
| changedSetScope(phase) | worker may change only planned CGE-R3 review/reference output paths named by the work order |
| traceScope(phase, actor) | worker return must include Agent Operation Trace Block and actual manifest |
| commitOwner(phase) | worker must not commit; reviewer/closer owns material commit if accepted; session-sync steward owns separate session-sync commit if mode or next move changes |
| crossBatchIsolation | source-mirror dispatch, worker material output, and session-sync must not be mixed with runtime/package/checker implementation |
| nextMoveSurfaces | worker must not edit; reviewer/session-sync steward updates only after material acceptance |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | N/A with reason: worker return review artifact is the planned material evidence carrier |
| reviewerOwnedClosurePaths | planned worker review/reference artifacts only; session-sync surfaces remain separate |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, surfaceSelector=`docs/work_orders`, riskCeiling=`HIGH`, maxResults=`20`

Returned defects: NONE_RETURNED

Disclosure note: dispatcher invoked the resolver with the query above and it
returned `totalCandidates=0`.

## Planned Worker Fulfillment Manifest

| Required output | Path | Owner | Status |
|---|---|---|---|
| Upstream source-mirror absorption review | `docs/reviews/CVF_CGE_R3_CODEGRAPH_UPSTREAM_SOURCE_MIRROR_ABSORPTION_REVIEW_2026-06-30.md` | worker | REQUIRED |
| CodeGraph upstream owner-surface delta | `docs/reference/CVF_CGE_R3_CODEGRAPH_UPSTREAM_OWNER_SURFACE_DELTA_2026-06-30.md` | worker | REQUIRED |
| Material commit | accepted worker outputs committed by reviewer only | reviewer | PENDING_REVIEW |
| Session sync | update front door/state/handoff after material acceptance if next move changes | session-sync steward | PENDING_REVIEW |

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

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this baseline references private source mirror and prior private
provenance artifacts. Public-safe publication requires a separate public-sync
authorization from the sibling public-sync clone.

## Claim Boundary

This baseline authorizes only CGE-R3 source-mirror-backed dispatch and
no-commit documentation/reference absorption review. It does not authorize
CodeGraph install/init, `.codegraph/`, MCP server, watcher, daemon, SQLite
index, runtime execution, package activation, package root creation, checker
implementation, CI mutation, provider/live proof, benchmark, public-sync, or
production-readiness claim.
