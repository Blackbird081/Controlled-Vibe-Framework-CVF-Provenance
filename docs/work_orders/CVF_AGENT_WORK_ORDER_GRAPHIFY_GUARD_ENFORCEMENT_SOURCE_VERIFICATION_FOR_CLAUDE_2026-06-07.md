# CVF Agent Work Order - Graphify Guard Enforcement Source Verification For Claude - 2026-06-07

Status: DISPATCH_READY_FOR_CLAUDE
Memory class: FULL_RECORD
Risk ceiling: R1_DOC_ONLY_SOURCE_VERIFICATION
Dispatch base head: 74ba8033
dispatchBaseHead: 74ba8033
executionBaseHead: worker-captures-before-edits
closureBaseHead: reviewer-captures-after-worker-return
Worker: Claude
Worker commit mode: WORKER_MUST_NOT_COMMIT
Commit mode: WORKER_MUST_NOT_COMMIT
Reviewer / closer: Codex or operator-designated reviewer
Public export disposition: DEFERRED_PRIVATE_ONLY

## Purpose

This work order dispatches Claude to produce a bounded, source-backed Graphify guard enforcement source map and completion packet after CI1 identified `F2-guard-spec-absent`.

## Scope

Scope is private provenance documentation only. The target owner surfaces are the current Graphify/KGR policy registry, memory retrieval policy, tests, CLI registry evidence, and the post-CI1 Graphify guard roadmap.

## Claim Boundary

This work may claim only source verification, mapping, and follow-up recommendation. It may not claim runtime enforcement, CLI readiness, provider behavior, public readiness, production readiness, release readiness, or benchmark improvement.

## Authority Chain

Claude must read these files before material work:

| Authority item | Path | Required use |
|---|---|---|
| Agent instructions | `AGENTS.md` | Governing process, boundary, autorun, knowledge absorption rules |
| Session front door | `CVF_SESSION_MEMORY.md` | Current continuity routing |
| Machine state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Active handoff and current state |
| Active handoff | `AGENT_HANDOFF_V16_2026-06-06.md` | Latest operator/session context |
| Work-order template | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | Source verification discipline |
| Graphify guard roadmap | `docs/roadmaps/CVF_GRAPHIFY_GUARD_ENFORCEMENT_ROADMAP_2026-06-02.md` | Source roadmap for this task |
| Knowledge absorption blind-spot standard | `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md` | Required absorption control block |
| Corpus completeness standard | `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md` | Required bounded-source proof |

Startup acknowledgment required before work:

`Startup acknowledged: current mode=graphify_guard_source_verification_for_claude; active handoff=AGENT_HANDOFF_V16_2026-06-06.md; next allowed move=doc-only source verification and enforcement mapping for Graphify guard policies G-GM-01 through G-GM-08; parked checkpoint=product lanes Redis, DEP2, and receipt-anchor remain parked or blocked outside this work order.`

Operator authorization: On 2026-06-07, the operator moved the session away from the three parked product lanes and approved creation of a knowledge-absorption work order for Claude.

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Orchestrator | Codex | Dispatch packet author and scope owner |
| Worker | Claude | Create the two required source-verification artifacts without committing |
| Reviewer / closer | Codex or operator-designated reviewer | Verify evidence, decide closure, and perform any later session sync |

## Required First Reads

Claude must read the authority files listed in the Authority Chain before editing. Claude must also read each source file named in the Source Verification Block before finalizing the source map.

## Worker Autonomy / No-Question Rule

Claude must proceed autonomously inside Allowed Scope. In-scope documentation, evidence, and gate failures are worker-owned. Claude must stop only when an action would exceed Allowed Scope, touch forbidden paths, consume secrets/quota, alter risk level, or require public-sync/live-provider behavior.

## 1. Mission

Create a source-verified Graphify guard enforcement mapping packet that refreshes the post-CI1 `F2-guard-spec-absent` finding against current source.

The work must distinguish:

| Surface | Required distinction |
|---|---|
| Guard policy registry | Current source may define `G-GM-*` IDs and policy metadata |
| Guard enforcement | Current source must be separately proven before any enforcement claim |
| Retrieval policy advisory behavior | Current source may route `graph_search` through advisory local policy |
| CLI product surface | `cvf graph` command work is out of scope and belongs to a separate roadmap |

This work order is documentation and source verification only. Claude must not implement runtime guard checks, CLI commands, provider flows, live proof, or public-facing changes.

## 2. Required Output Artifacts

Claude must create these artifacts:

| Artifact | Path | Required content |
|---|---|---|
| Source map | `docs/reference/CVF_GRAPHIFY_GUARD_ENFORCEMENT_SOURCE_MAP_2026-06-07.md` | Current source map for `G-GM-01` through `G-GM-08`, owner surfaces, enforcement evidence, and disposition |
| Completion packet | `docs/reviews/CVF_GRAPHIFY_GUARD_ENFORCEMENT_SOURCE_VERIFICATION_COMPLETION_2026-06-07.md` | Evidence, blind-spot block, corpus completeness block, claim boundary, and follow-up recommendation |

Optional artifacts are not allowed unless the reviewer explicitly expands scope.

## 3. Allowed Scope

Claude may:

| Scope item | Disposition |
|---|---|
| Read current Graphify, KGR, retrieval-policy, CLI registry, roadmap, finding, and CI1-T2 artifacts | ALLOWED |
| Create the two required markdown artifacts named above | ALLOWED |
| Propose a later implementation work order or machine-check candidate | ALLOWED |
| Record `ACCEPT`, `DEFER`, or `REJECT` mapping dispositions for each guard policy | ALLOWED |
| Record that old CI1-T2 negative-search evidence is historical when current source proves newer guard registry presence | ALLOWED_AND_EXPECTED |

## 4. Forbidden Scope

Claude must not:

| Forbidden action | Boundary |
|---|---|
| Edit runtime/source/test files under `EXTENSIONS/` | FORBIDDEN |
| Edit `governance/compat/` machine checks | FORBIDDEN |
| Implement or modify `cvf graph` CLI command behavior | FORBIDDEN |
| Edit `.private_reference/legacy/` source material | FORBIDDEN |
| Edit public-sync clone or make public-facing claims | FORBIDDEN |
| Run live provider/service/API proof or consume secrets/quota | FORBIDDEN |
| Touch QBS, output-quality parity, L4/L5 score, release readiness, production readiness, or provider behavior claims | FORBIDDEN |
| Edit session front doors or active handoff files | FORBIDDEN_FOR_WORKER |
| Commit, push, or stage unrelated files | FORBIDDEN_FOR_WORKER |

## Pre-Flight Checks

Before edits, Claude must capture:

```powershell
git rev-parse --short HEAD
git status --short
```

Claude must record the base head it used as `worker-base-head` in the completion packet. The expected dispatch base from this packet is `74ba8033`, but Claude must use the actual local pre-edit head if the reviewer provides a newer checkout.

## Write Ownership

| Path | Ownership |
|---|---|
| `docs/reference/CVF_GRAPHIFY_GUARD_ENFORCEMENT_SOURCE_MAP_2026-06-07.md` | Claude may create |
| `docs/reviews/CVF_GRAPHIFY_GUARD_ENFORCEMENT_SOURCE_VERIFICATION_COMPLETION_2026-06-07.md` | Claude may create |
| `AGENT_HANDOFF_V16_2026-06-06.md` | Claude must not edit |
| `CVF_SESSION_MEMORY.md` | Claude must not edit |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Claude must not edit |
| `EXTENSIONS/` | Claude must not edit |
| `governance/compat/` | Claude must not edit |
| public-sync sibling clone | Claude must not edit |

## 5. Pre-Existing Dirty Path Exemption

The dispatching workspace had this pre-existing modified path before this work order:

| Path | Status | Ownership |
|---|---|---|
| `AGENT_HANDOFF_V16_2026-06-06.md` | Modified before this work order | Operator/session-continuity edit; Claude must not edit, stage, commit, or claim this file |

Claude must report any additional dirty paths before writing files. If a dirty path intersects this work order's required output artifacts, stop and return to reviewer.

## 6. Source Verification Block

Claude must verify the following source facts directly and may correct line numbers if current files have drifted.

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Active Graphify guard roadmap is parked post-CI1 and requires later source verification before implementation | VALUE_SET | `docs/roadmaps/CVF_GRAPHIFY_GUARD_ENFORCEMENT_ROADMAP_2026-06-02.md` | lines 5, 30-34, 44-50 | `Status` | Roadmap | ACCEPT |
| Roadmap names guard policies `G-GM-01` through `G-GM-08` | EXISTS | `docs/roadmaps/CVF_GRAPHIFY_GUARD_ENFORCEMENT_ROADMAP_2026-06-02.md` | lines 19-24 | `G-GM-01` through `G-GM-08` | Roadmap guard policy list | ACCEPT |
| Roadmap requires mapping each `G-GM-*` ID before implementation | RUNTIME_BEHAVIOR | `docs/roadmaps/CVF_GRAPHIFY_GUARD_ENFORCEMENT_ROADMAP_2026-06-02.md` | lines 77-82, 90-120 | `source-verify`, `map each G-GM-*` | Roadmap phases | ACCEPT |
| Roadmap forbids current enforcement claims without source verification | LITERAL_INVARIANT | `docs/roadmaps/CVF_GRAPHIFY_GUARD_ENFORCEMENT_ROADMAP_2026-06-02.md` | lines 127-137 | `No current enforcement claim` | Claim boundary | ACCEPT |
| CI1 finding `F2-guard-spec-absent` was deferred into the Graphify guard enforcement roadmap | VALUE_SET | `docs/corpus-intelligence/findings/legacy-cvf-important-graphify.md` | lines 52, 82-115 | `F2-guard-spec-absent` | CI1 finding ledger | ACCEPT |
| CI1 finding lists `G-GM-01` through `G-GM-08` requirements | EXISTS | `docs/corpus-intelligence/findings/legacy-cvf-important-graphify.md` | lines 90-97 | `G-GM-01` through `G-GM-08` | Finding requirement table | ACCEPT |
| CI1 old negative-search claim for guard IDs is historical and must be refreshed against current source | DOC_ONLY_NEW | `docs/corpus-intelligence/findings/legacy-cvf-important-graphify.md` | line 99 | `0 results in current TS source` | Finding evidence note | ACCEPT |
| CI1-T2 read the Graph Memory guard spec and recorded eight guard policies | VALUE_SET | `docs/audits/CVF_CI1_T2_GRAPHIFY_READINESS_PACKET_2026-06-02.md` | lines 117, 152, 199, 406-407 | `CVF_GRAPH_MEMORY_GUARD_SPEC.md` | CI1-T2 readiness packet | ACCEPT |
| Current KGR source defines `KgrGuardPolicyId` for `G-GM-01` through `G-GM-08` | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge-graph-store.ts` | lines 75-83 | `KgrGuardPolicyId` | `knowledge-graph-store.ts` | ACCEPT |
| Current KGR source defines `KGR_GUARD_POLICIES` metadata for all eight guard policies | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge-graph-store.ts` | lines 191-239 | `KGR_GUARD_POLICIES` | `knowledge-graph-store.ts` | ACCEPT |
| Current KGR source exposes guard policy lookup | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge-graph-store.ts` | lines 246-247 | `getKgrGuardPolicy` | `knowledge-graph-store.ts` | ACCEPT |
| Current KGR tests cover guard policy registry presence, not full enforcement | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/knowledge-graph-store.test.ts` | lines 84-86 | `KGR_GUARD_POLICIES`, `getKgrGuardPolicy` | KGR unit tests | ACCEPT |
| Current memory retrieval policy includes `graph_search` request method | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | line 15 | `graph_search` | `MemoryRetrievalRequest.method` | ACCEPT |
| Current memory retrieval policy accepts optional `kgrStore` and evaluates graph search advisory routing | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | lines 39, 105, 124-157, 168-173, 200 | `evaluateRetrievalRequest` | `memory-retrieval-policy.ts` | ACCEPT |
| Current KGR retrieval tests cover local-only advisory graph-search policy behavior | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/memory-retrieval-policy.kgr.test.ts` | lines 38, 51, 62, 78 | `graph_search`, `kgr_graph_search_policy_applied_local_only` | KGR retrieval tests | ACCEPT |
| Current CLI registry does not prove a `cvf graph` product command | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts` | lines 39-42, 84-254 | `CommandRegistry` | CLI command registry | ACCEPT |
| CLI graph command belongs to a separate parked/backlog roadmap and is out of scope here | VALUE_SET | `docs/roadmaps/CVF_GRAPH_CLI_PHASED_BACKLOG_ROADMAP_2026-06-02.md` | current status and claim boundary sections | `CVF_GRAPH_CLI_PHASED_BACKLOG_ROADMAP_2026-06-02.md` | CLI roadmap | ACCEPT |
| KGR1 is closed bounded and does not prove public, production, web-route, or durable retrieval readiness | VALUE_SET | `docs/roadmaps/CVF_KGR1_KNOWLEDGE_GRAPH_RETRIEVAL_ROADMAP_2026-06-01.md` | status and claim boundary sections | `CLOSED_PASS_BOUNDED` | KGR1 roadmap | ACCEPT |

If Claude cannot verify any `ACCEPT` row from source, Claude must change that row in the output artifact to `REJECT` or `BLOCKED_SOURCE_NOT_FOUND` and explain the corrected source fact.

## 7. New Doc-Only Fields

These terms may appear only in the new documentation artifacts. They are not runtime fields or existing source contracts:

| New doc-only field | Meaning | Runtime claim boundary |
|---|---|---|
| `graphifyGuardEnforcementSourceMap` | The markdown source map created by this work order | No runtime field |
| `guardPolicyImplementationDisposition` | Per-policy mapping decision in the source map | No runtime field |
| `firstEnforcementCandidate` | Recommended later implementation candidate | No runtime field |
| `policyRegistryExists` | Documentation label for source-proven registry presence | No runtime field |
| `enforcementProven` | Documentation label for whether enforcement is source-proven | No runtime field |

## 8. Knowledge Absorption Blind-Spot Control Block

The completion packet must include a `Knowledge Absorption Blind-Spot Control Block` with:

| Required item | Minimum requirement |
|---|---|
| Prior absorption evidence | Cite roadmap, CI1-T2 packet, finding file, and current KGR/retrieval/CLI sources |
| Detailed source read | Include file-level ledger for each authority file read |
| Accepted value | Identify what current source proves |
| Deferred value | Identify what remains unsupported or implementation-bound |
| Rejected value | Identify stale or overbroad claims, including stale negative-search evidence if current source contradicts it |
| Owner surface normalization | Map accepted value to current CVF owner surfaces |
| Adversarial review | Include at least one skeptical check against overclaiming enforcement |
| Blind-spot delta | State what is now clearer than before and what remains unknown |

Allowed verdicts: `COMPLETE`, `PARTIAL_WITH_LOW_RISK`, or `BLOCKED`.

## 9. Corpus Completeness And Report Integrity Block

Because this task produces a source-derived report, the completion packet and source map must include a `Corpus Completeness And Report Integrity` block with:

| Required item | Minimum requirement |
|---|---|
| Bounded corpus | Enumerate exact files reviewed |
| File-level processing ledger | Mark each file as read, sampled, excluded, or blocked |
| Reconciliation | Account for each source listed in this work order |
| Unresolved files | Declare none, or list exact unresolved paths |
| Exclusions | Explain why runtime implementation and CLI command work are excluded |
| Drift check | Include command-backed current-source refresh for `G-GM-0`, `KgrGuardPolicy`, `graph_search`, and `cvf graph` |
| Traceability | Each conclusion must point to source path and line or section |
| Adversarial verification | Include a no-enforcement-overclaim review |

Allowed verdicts: `COMPLETE_VERIFIED`, `COMPLETE_WITH_DECLARED_EXCLUSIONS`, `PARTIAL`, `BLOCKED`, or `STALE_SNAPSHOT`.

## 10. Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order action | Required output |
|---|---|---|
| Source-verify current KGR/runtime/guard surfaces before implementation | Read current KGR, retrieval-policy, tests, CLI registry, finding, CI1-T2, KGR1, and roadmap files | Source map with line-backed evidence |
| Map each `G-GM-*` ID to an owner surface and disposition | Create per-policy table for `G-GM-01` through `G-GM-08` | `guardPolicyImplementationDisposition` table |
| Do not implement from roadmap prose alone | Keep this batch doc-only | Completion packet claim boundary |
| Select smallest first enforcement candidate when evidence supports it | Recommend one later candidate or return blocked | `firstEnforcementCandidate` section |
| Avoid CLI/product-surface conflation | Exclude `cvf graph` implementation | Explicit CLI boundary section |
| Avoid runtime/provider/public readiness claims | Keep claim limited to source verification and mapping | Claim boundary section |

## Execution Plan

| Step | Required action |
|---|---|
| 1 | Complete startup acknowledgment and first reads |
| 2 | Refresh current-source searches for guard policy IDs, KGR policy registry, retrieval policy, and CLI graph command evidence |
| 3 | Create the source map with one row per `G-GM-*` policy |
| 4 | Create the completion packet with corpus completeness, blind-spot, evidence, and claim boundary blocks |
| 5 | Run required gates and return evidence without committing |

## Acceptance Criteria

| Criterion | Acceptance rule |
|---|---|
| Required artifacts exist | Both output artifacts are created at the exact paths listed in this work order |
| Source verification complete | Each `G-GM-*` policy has source-backed registry and enforcement-disposition evidence |
| Stale CI1 evidence handled | The old negative-search claim is labeled historical if current source proves newer registry presence |
| Scope held | No runtime, CLI, governance checker, public-sync, session front-door, or secret-bearing files are edited |
| Claim boundary held | Completion packet makes no runtime enforcement, public, production, release, or provider claim |
| Gates reported | Required command evidence is present with pass/fail status |

## 11. Required Source Map Shape

The source map must include a table with one row per policy:

| Policy ID | Policy name | Registry source | Enforcement source | Retrieval-policy interaction | Implementation disposition | Evidence pointer | Later action |
|---|---|---|---|---|---|---|
| `G-GM-01` | source-verified by Claude | source-verified by Claude | source-verified by Claude | source-verified by Claude | `ACCEPT_FOR_NEXT_IMPLEMENTATION`, `DEFER_NO_ENFORCEMENT_SOURCE`, or `REJECT_SCOPE_MISMATCH` | path plus line or section | bounded next action |
| `G-GM-02` | source-verified by Claude | source-verified by Claude | source-verified by Claude | source-verified by Claude | `ACCEPT_FOR_NEXT_IMPLEMENTATION`, `DEFER_NO_ENFORCEMENT_SOURCE`, or `REJECT_SCOPE_MISMATCH` | path plus line or section | bounded next action |
| `G-GM-03` | source-verified by Claude | source-verified by Claude | source-verified by Claude | source-verified by Claude | `ACCEPT_FOR_NEXT_IMPLEMENTATION`, `DEFER_NO_ENFORCEMENT_SOURCE`, or `REJECT_SCOPE_MISMATCH` | path plus line or section | bounded next action |
| `G-GM-04` | source-verified by Claude | source-verified by Claude | source-verified by Claude | source-verified by Claude | `ACCEPT_FOR_NEXT_IMPLEMENTATION`, `DEFER_NO_ENFORCEMENT_SOURCE`, or `REJECT_SCOPE_MISMATCH` | path plus line or section | bounded next action |
| `G-GM-05` | source-verified by Claude | source-verified by Claude | source-verified by Claude | source-verified by Claude | `ACCEPT_FOR_NEXT_IMPLEMENTATION`, `DEFER_NO_ENFORCEMENT_SOURCE`, or `REJECT_SCOPE_MISMATCH` | path plus line or section | bounded next action |
| `G-GM-06` | source-verified by Claude | source-verified by Claude | source-verified by Claude | source-verified by Claude | `ACCEPT_FOR_NEXT_IMPLEMENTATION`, `DEFER_NO_ENFORCEMENT_SOURCE`, or `REJECT_SCOPE_MISMATCH` | path plus line or section | bounded next action |
| `G-GM-07` | source-verified by Claude | source-verified by Claude | source-verified by Claude | source-verified by Claude | `ACCEPT_FOR_NEXT_IMPLEMENTATION`, `DEFER_NO_ENFORCEMENT_SOURCE`, or `REJECT_SCOPE_MISMATCH` | path plus line or section | bounded next action |
| `G-GM-08` | source-verified by Claude | source-verified by Claude | source-verified by Claude | source-verified by Claude | `ACCEPT_FOR_NEXT_IMPLEMENTATION`, `DEFER_NO_ENFORCEMENT_SOURCE`, or `REJECT_SCOPE_MISMATCH` | path plus line or section | bounded next action |

Claude may add columns only if needed for evidence clarity. Claude must not leave unfinished values in the final source map.

## Evidence Requirements

Claude must report command evidence in the completion packet:

```powershell
git rev-parse --short HEAD
git status --short
git diff --name-status <worker-base-head> HEAD
rg -n "G-GM-0|KgrGuardPolicy|KGR_GUARD_POLICIES|getKgrGuardPolicy" EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests
rg -n "graph_search|kgr_graph_search_policy_applied_local_only|graph_search_policy_applied_advisory_only" EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests
rg -n "cvf graph|graph command|CommandRegistry|registerBuiltInCommands" EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src docs/roadmaps
python governance/compat/check_markdown_structural_completeness.py --base <worker-base-head> --head HEAD --enforce
python governance/compat/check_public_export_disposition.py --base <worker-base-head> --head HEAD --enforce
python governance/compat/check_finding_to_governance_learning.py --base <worker-base-head> --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <worker-base-head> --head HEAD
```

If a command is unavailable or fails, Claude must record the exact failing command, failure class, whether it is retryable, and whether the failure blocks closure.

## Review Gate

Reviewer may close only if the two required artifacts exist, the changed-file set remains inside Write Ownership, command evidence is present, and every completion claim stays inside the Claim Boundary.

## Closure Checklist

| Item | Required close state |
|---|---|
| Startup acknowledgment | RECORDED |
| Required first reads | RECORDED |
| Source map artifact | PRESENT |
| Completion packet artifact | PRESENT |
| Corpus completeness block | PRESENT |
| Knowledge absorption blind-spot block | PRESENT |
| No forbidden path edits | VERIFIED |
| No commits or pushes by Claude | VERIFIED |
| Gates | PASS_OR_REPORTED_BLOCKER |

## Return-To-Orchestrator Conditions

Return to orchestrator if current source contradicts this work order, a required source file is missing, a required gate blocks closure, a dirty path intersects the output artifacts, or any needed action exceeds Allowed Scope.

## Operator Checkpoint

Human checkpoint status: none for Claude's doc-only source verification. Separate human authorization is needed before any later runtime implementation, public-sync, live proof, secret use, CLI implementation, or session-state rewrite.

## 13. Completion Claim Boundary

Allowed final claim:

`Graphify guard enforcement source verification and mapping are complete for the bounded source corpus, with each G-GM policy mapped to current registry evidence, enforcement evidence, and a later implementation disposition.`

Forbidden final claims:

| Claim | Status |
|---|---|
| Runtime Graphify guard enforcement implemented | FORBIDDEN |
| `cvf graph` CLI implemented or ready | FORBIDDEN |
| Knowledge graph product readiness | FORBIDDEN |
| Public readiness or production readiness | FORBIDDEN |
| Live provider behavior proven | FORBIDDEN |
| Release readiness | FORBIDDEN |
| F-1 output-quality parity, QBS parity, L4/L5 score, or benchmark improvement | FORBIDDEN |

## 14. Return Packet

Claude must return:

| Return item | Required |
|---|---|
| Files changed | Exact paths only |
| Source map summary | One paragraph |
| Per-policy disposition summary | Counts by disposition |
| First enforcement candidate | One bounded recommendation, or `BLOCKED` with reason |
| Gates run | Commands and pass/fail |
| Dirty path status | Include pre-existing handoff exemption and any new dirty paths |
| Claim boundary | Restate allowed and forbidden claims |

Claude must not commit or push. Reviewer will decide whether to close, sync session state, or open a later implementation work order.
