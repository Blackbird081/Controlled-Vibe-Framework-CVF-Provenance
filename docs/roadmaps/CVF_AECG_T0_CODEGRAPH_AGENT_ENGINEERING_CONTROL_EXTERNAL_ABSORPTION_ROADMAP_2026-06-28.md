# CVF AECG-T0 CodeGraph And Agent Engineering Control External Absorption Roadmap

Memory class: FULL_RECORD

Status: ROADMAP_READY_FOR_AECG_T1_SOURCE_VERIFIED_TRIAGE

docType: roadmap

Date: 2026-06-28

Batch ID: AECG-T0

External knowledge intake routing: REQUIRED

## Purpose

Audit the current upstream `colbymchenry/codegraph` repository and the
operator-provided `CVF_Agent_Engineering_Control_Standard/` folder, then select
the next governed CVF tranche.

Decision:
`OPEN_AECG_T1_SOURCE_VERIFIED_AGENT_ENGINEERING_CONTROL_TRIAGE`

Recommended next:
`AUTHOR_AECG_T1_GC018_FOR_AGENT_ENGINEERING_CONTROL_TRIAGE_AND_CODEGRAPH_DELTA`

## Target / Source

Reviewed sources:

- upstream repository clone:
  `colbymchenry/codegraph` at commit `c5bd6e2`
- operator-provided external folder, retained after audit under:
  `.private_reference/legacy/CVF_Agent_Engineering_Control_Standard/`
- prior CVF CodeGraph triage and adaptation surfaces:
  `docs/reviews/CVF_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_COMPLETION_2026-06-20.md`
- prior CVF CodeGraph adaptation contract:
  `docs/reference/CVF_CGE_T2_CODEGRAPH_LPF_KGR_ADAPTATION_CONTRACT_2026-06-20.md`
- root frozen-reference relocation record:
  `docs/reviews/CVF_FROZEN_REFERENCE_ROOT_RELOCATION_COMPLETION_2026-06-28.md`
- external-intake chain map:
  `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`

Roadmap base head: `5939800e`.

## Scope / Methodology

1. Read CVF startup, active state, active handoff, guard orientation, literal
   format guidance, and external knowledge intake chain map.
2. Clone the current upstream CodeGraph repository and inspect current
   README, MCP reference, affected-test guide, agent adoption design note,
   MCP tool implementation, worktree mismatch detection, and watcher policy.
3. Read the operator-provided Agent Engineering Control folder beyond file
   names, including README, tree view, master standard, absorption mapping,
   manifest, claim-boundary checker, workflow-artifact checker, and a receipt
   schema.
4. Compare the current CodeGraph delta against prior CGE-T1/CGE-T2 outcomes.
5. Select a documentation and triage-only next tranche that source-verifies the
   folder content, maps useful gates to existing CVF owner surfaces, and
   rejects direct package/runtime import.

No runtime source, generated aggregate, checker, provider call, public-sync,
adapter, package activation, certification, CodeGraph install/init,
`.codegraph/` creation, MCP wiring, watcher/daemon, benchmark, PR merge
automation, or universal governed-coding-control claim is authorized by
AECG-T0.

## Authorization / Decision

Operator authorization: continue the existing external-absorption rule for
`colbymchenry/codegraph` and the operator-provided
`CVF_Agent_Engineering_Control_Standard/` folder.

Roadmap decision:
`OPEN_AECG_T1_SOURCE_VERIFIED_AGENT_ENGINEERING_CONTROL_TRIAGE`

This authorizes only a roadmap and next-tranche selection. It does not
authorize implementation.

## Non-Goals

- No direct import of CodeGraph runtime, MCP server, installer, watcher,
  daemon, SQLite index, telemetry worker, benchmark harness, or agent hook.
- No direct import of the Agent Engineering Control package as a canonical CVF
  extension.
- No merge automation, PR automation, managed-hook repair, or runtime
  enforcement.
- No public-sync export.
- No provider/live proof.
- No replacement of existing CVF work-order, review, closure, handoff,
  autorun, or graph-owner surfaces.

## Design Control Gate

| Control | Required disposition |
|---|---|
| Prior CodeGraph absorption | Treat CGE-T1/CGE-T2 as binding; only evaluate current upstream delta |
| External-source handling | CodeGraph and AEC folder stay source inputs only |
| Existing CVF owner surfaces | AECG-T1 must map each gate to existing CVF standards/checkers before any new checker proposal |
| Runtime boundary | CodeGraph MCP/runtime and AEC package runtime remain parked |
| Claim boundary | Agent engineering control must not claim CVF replaces coding agents or guarantees engineering safety |

## Work Plan

| Step | Output | Status |
|---|---|---|
| AECG-T0.1 | inspect current CodeGraph delta after prior CGE absorption | COMPLETE |
| AECG-T0.2 | inspect Agent Engineering Control folder beyond filenames | COMPLETE |
| AECG-T0.3 | classify direct runtime/package import as blocked | COMPLETE |
| AECG-T0.4 | select AECG-T1 source-verified triage/adaptation matrix | COMPLETE |

## Acceptance Criteria

| Criterion | Evidence | Status |
|---|---|---|
| Upstream CodeGraph reviewed at fixed commit | External Artifact Hash Manifest | PASS |
| Local folder reviewed beyond filenames | External Artifact Hash Manifest and Absorption Classification | PASS |
| Prior CodeGraph absorption considered | Source Verification Block | PASS |
| Runtime/package work not authorized | Non-Goals and Claim Boundary | PASS |
| Next tranche selected | Proposed Roadmap | PASS |

## Verification / Evidence

| Evidence item | Result |
|---|---|
| `git rev-parse --short HEAD` before material edit | `5939800e` |
| upstream CodeGraph clone commit | `c5bd6e2` |
| local Agent Engineering Control folder status | operator-provided external source folder moved to ignored legacy reference storage after audit |
| external hash capture | recorded in External Artifact Hash Manifest |
| expected changed set | this roadmap only |

## External Artifact Hash Manifest

| Artifact | Source class | Commit or local source | SHA256 |
|---|---|---|---|
| `README.md` | upstream CodeGraph | `colbymchenry/codegraph@c5bd6e2` | `74F0714059D48ED75B2CF93916317F3DF1C2A6C5977635FDA6989FBDA07F31DA` |
| `docs/design/agent-codegraph-adoption.md` | upstream CodeGraph | `colbymchenry/codegraph@c5bd6e2` | `BCE54C9780D22FDA507993282424E69643E9212ED81892B85D4B03C566D1C81A` |
| `site/src/content/docs/reference/mcp-server.md` | upstream CodeGraph | `colbymchenry/codegraph@c5bd6e2` | `8CE0001A5C7A56FF26332B51EAEB2BC65ABBC404446791FEAEF49767970C2F72` |
| `site/src/content/docs/guides/affected-tests.md` | upstream CodeGraph | `colbymchenry/codegraph@c5bd6e2` | `6C59D51A07FA06A30188BD384BB6E56809BA1E614E4BBF508F91BF0DC0909EFE` |
| `src/mcp/tools.ts` | upstream CodeGraph | `colbymchenry/codegraph@c5bd6e2` | `2F02A890DCDA337FBD58ED7CD299F441D4972C47B851133BE7155E0FDE2797FE` |
| `src/sync/worktree.ts` | upstream CodeGraph | `colbymchenry/codegraph@c5bd6e2` | `73DAD70337A3FD59252C6B52965D384C225493BC5611BA37DF8784214D3EA92E` |
| `.private_reference/legacy/CVF_Agent_Engineering_Control_Standard/README.md` | operator-provided folder | local external folder | `D0753E373D3B0446D2C7EB9670FE1E5D7DBC8633D51C9D8D31C88E4F5A6636B0` |
| `.private_reference/legacy/CVF_Agent_Engineering_Control_Standard/docs/standards/CVF_AGENT_ENGINEERING_CONTROL_STANDARD_2026-06-20.md` | operator-provided folder | local external folder | `683975280C84121751DCEF661605DC43FAAA78CC0CB94BAA97A948DD1A866B64` |
| `.private_reference/legacy/CVF_Agent_Engineering_Control_Standard/docs/reference/CVF_CLAUDEKIT_ENGINEER_ABSORPTION_MAPPING_2026-06-20.md` | operator-provided folder | local external folder | `4DD4B00BCEAE0E9ED193BFBAE20888A25AA371F8C2D2F6B14E7F81BC43183618` |
| `.private_reference/legacy/CVF_Agent_Engineering_Control_Standard/EXTENSIONS/CVF_AGENT_ENGINEERING_CONTROL_STANDARD/standard.manifest.json` | operator-provided folder | local external folder | `9858153008C3181F5765E8E0ED4B66F4C3B84B60BBBE51468BFB49BADE63476B` |
| `.private_reference/legacy/CVF_Agent_Engineering_Control_Standard/tools/agent-control/check-agent-claim-boundary.ts` | operator-provided folder | local external folder | `4F2FD8B24AAEA102DB51039AFA01E09705926C8FD9A14C149CB743836A3C5A73` |
| `.private_reference/legacy/CVF_Agent_Engineering_Control_Standard/tools/agent-control/check-agent-workflow-artifacts.ts` | operator-provided folder | local external folder | `7A5FC2510293755C989C95BA34B9A578077246E1FB2FD6B2127A897D9C80101C` |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| CodeGraph prior absorption is already governed | `docs/reviews/CVF_CGE_T1_CODEGRAPH_EXTERNAL_ABSORPTION_TRIAGE_MATRIX_COMPLETION_2026-06-20.md` | Purpose; Triage Matrix; CodeGraph vs KGR Dedupe Decision | CGE-T1 | CVF CodeGraph triage owner | EXISTS | ACCEPT |
| CodeGraph adapted value is currently bounded to LPF/KGR advisory graph language | `docs/reference/CVF_CGE_T2_CODEGRAPH_LPF_KGR_ADAPTATION_CONTRACT_2026-06-20.md` | Purpose; LPF/KGR Owner Surface Map; No-Authority Rule | CGE-T2 | CVF CodeGraph adaptation owner | EXISTS | ACCEPT |
| CodeGraph root material was already moved to legacy after absorption | `docs/reviews/CVF_FROZEN_REFERENCE_ROOT_RELOCATION_COMPLETION_2026-06-28.md` | Findings / Position; Decision / Disposition | RELOCATE_TO_LEGACY_REFERENCE | root lifecycle completion | VALUE_SET | ACCEPT |
| External-intake chain treats external repo or copied folder as advisory until promoted through CVF owner surfaces | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | Central Core; Input Type Router | External repo or copied folder | external knowledge chain map | LITERAL_INVARIANT | ACCEPT |

## Findings / Position

| Finding | Evidence | Disposition |
|---|---|---|
| Current CodeGraph repo is not a fresh unabsorbed root | CGE-T1/CGE-T2 plus frozen-reference relocation | REOPEN_ONLY_FOR_DELTA |
| CodeGraph current delta has useful patterns for affected-test routing, worktree-index mismatch warning, single strong MCP tool design, output budgeting, and stale/fallback discipline | current upstream docs/source sampled at `c5bd6e2` | ADAPT_AS_ADVISORY_INPUT |
| CodeGraph runtime/MCP install remains parked | prior CGE contract plus current parked lane rules | DEFER_WITH_REOPEN_CONDITION |
| Agent Engineering Control folder is high-signal but overlaps many existing CVF gates | README, master standard, manifest, guard scripts, schema | ADAPT_TO_EXISTING_GUARD_SURFACES |
| Direct package import would duplicate CVF governance structure | folder contains standards/protocols/guards/schemas/tools rather than a source-verified CVF owner map | REJECT_DIRECT_IMPORT |
| Best next move is a source-verified AECG-T1 triage/adaptation matrix | combined audit and prior CGE boundary | AECG_T1_READY |

Decision: `ROADMAP_READY_FOR_AECG_T1_SOURCE_VERIFIED_TRIAGE`

## Absorption Classification

| External item | Source | CVF disposition | Reason / next condition |
|---|---|---|---|
| `codegraph affected` affected-test routing | CodeGraph affected-tests guide and tests | ADAPT_AS_CANDIDATE_FOR_TEST_SELECTION_EVIDENCE | Useful for future CVF test selection, but no runtime CLI adoption without GC-018 |
| Worktree-index mismatch warning | CodeGraph `src/sync/worktree.ts` | ADAPT_AS_GRAPH_FRESHNESS_BOUNDARY_LANGUAGE | Fits CGE-T2 stale/fallback discipline |
| Single strong MCP tool by default | CodeGraph MCP docs and `src/mcp/tools.ts` | ADAPT_AS_AGENT_TOOL_SURFACE_DESIGN_INPUT | Useful for future MCP/tool UX only; no MCP wiring authorized |
| Adaptive explore budget | CodeGraph `getExploreBudget` and `getExploreOutputBudget` | ADAPT_AS_CONTEXT_BUDGETING_REFERENCE | Potentially useful for CVF context pack budgets; no runtime import |
| Watcher/daemon and auto-sync | CodeGraph watcher docs/source | DEFER_WITH_REOPEN_CONDITION | Runtime behavior; prior CGE boundary still blocks |
| CodeGraph performance claims | CodeGraph README | BLOCK_UNTIL_CVF_BENCHMARK | External benchmark claim only |
| Agent review evidence gate | AEC folder standard and schema | ADAPT_TO_EXISTING_REVIEW_EVIDENCE_SURFACES | High value; map to current review/closure gates before adding new schema |
| Debug root cause gate | AEC folder standard | ADAPT_TO_EXISTING_FINDING_AND_DEBUG_BOUNDARIES | High value, likely maps to finding/root-cause surfaces |
| Prior work discovery gate | AEC folder standard | ADAPT_TO_EXISTING_SOURCE_VERIFICATION_AND_SEARCH_DISCIPLINE | High value; avoid duplicate implementation |
| Parallel implementation guard | AEC folder standard | ADAPT_TO_EXISTING_PARALLEL_CORE_AND_OWNER_SURFACE_RULES | High value; many CVF lanes already use this doctrine |
| Maintenance cost gate | AEC folder standard | ADAPT_AS_DECISION_SURFACE | Useful as roadmap/value filter |
| AI slop and diff content lint gates | AEC folder standard and scripts | ADAPT_AS_STATIC_GUARD_CANDIDATES | Useful, but must be source-verified against current CVF checkers first |
| Governed PR merge and managed hooks | AEC folder protocols | DEFER_WITH_REOPEN_CONDITION | High-risk automation; no PR merge or hook repair authorized |
| Agent work journal | AEC folder standard/templates | ADAPT_TO_EXISTING_HANDOFF_AND_AOT_SURFACES | Useful only if not duplicating current handoff/session state |
| AEC package extension manifest, schemas, receipts, examples, tools | AEC folder | REJECT_DIRECT_IMPORT | Re-express only selected fields through CVF-owned artifacts |

## Proposed Roadmap

| Tranche | Status | Objective | Boundary |
|---|---|---|---|
| AECG-T0 | ROADMAP_READY_FOR_AECG_T1_SOURCE_VERIFIED_TRIAGE | Audit CodeGraph delta plus Agent Engineering Control folder and select next move | documentation-only |
| AECG-T1 | RECOMMENDED_NEXT | Author GC-018 and source-verified triage/adaptation matrix mapping AEC gates and CodeGraph delta to current CVF owner surfaces | no runtime/checker/import |
| AECG-T2 | PARKED | Promote the highest-value AEC subset into one CVF-owned agent engineering control reference or matrix | requires AECG-T1 closure |
| AECG-T3 | PARKED | Decide whether one static checker candidate is worth implementing, likely diff-content overclaim or agent-review evidence | requires AECG-T2 and fresh GC-018 |
| AECG-RUNTIME | PARKED | CodeGraph MCP/runtime, affected-test CLI, watchers, hook repair, PR merge automation, package import | fresh operator authorization, GC-018, source verification, and live/runtime proof when behavior is claimed |

## Risk / Corrective Action

| Risk | Corrective action | Status |
|---|---|---|
| Reopening already-closed CodeGraph absorption without new evidence | Treat CGE-T1/CGE-T2 as binding and only evaluate current delta | PASS |
| External package replaces CVF authority | AECG-T1 must create CVF-owned triage/adaptation artifact before any promotion | PASS |
| Direct package copy duplicates existing CVF governance | Reject direct import in T0 | PASS |
| Runtime/MCP/hook/merge automation opens parked lanes | Keep runtime and automation parked behind fresh GC-018 | PASS |
| Agent engineering control overclaims CVF as a coding agent | Carry claim boundary from AEC folder and CVF external-intake rules | PASS |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External repo or copied folder |
| Chain map route | External repo or copied folder -> prior-absorption check -> source-verified triage/adaptation matrix -> future GC-018/work order only if implementation is separately authorized |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `docs/roadmaps/CVF_AECG_T0_CODEGRAPH_AGENT_ENGINEERING_CONTROL_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` |
| Disposition | ADAPT selected CodeGraph delta and Agent Engineering Control ideas into an AECG-T1 source-verified triage/adaptation matrix |
| Claim boundary | external repo and folder are source inputs only; AECG-T0 creates no runtime, package, public, provider, adapter, MCP, watcher, daemon, merge automation, hook repair, or checker support |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | AECG-T0 external absorption roadmap only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | no wrapper, proxy, mandatory invocation, direct IDE/shell/git/filesystem interception, arbitrary command execution, or EDIT/COMMIT execution |
| interceptionBoundary | no direct interception claim |
| claimLanguage | roadmap and external-intake selection only |
| forbiddenExpansion | no runtime, MCP, watcher/daemon, benchmark, provider/live, public-sync, merge automation, hook repair, package activation, certification, checker implementation, or universal governed-coding-control claim |

## Claim Boundary

This roadmap authorizes audit, classification, and next-tranche selection only.
It does not authorize CodeGraph install/init, `.codegraph/` creation, MCP
wiring, watcher/daemon behavior, affected-test CLI use, benchmark proof,
provider/live proof, public-sync, PR merge automation, managed-hook repair,
package activation, certification, checker implementation, generated aggregate
mutation, or a claim that CVF replaces coding agents or guarantees engineering
safety.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance external absorption roadmap. No public-sync remote,
public commit, public artifact path, or public claim is authorized.
