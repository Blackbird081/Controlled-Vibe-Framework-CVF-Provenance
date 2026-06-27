# CVF Delta Execution Control Capability Roadmap

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-19

Owner: Codex

Roadmap ID: DELTA-T5

## Purpose

Map the current Delta Execution Control capability stack after MCP to Model
Gateway Composition Proof and Delta-T1 through Delta-T4B. This roadmap keeps
completed invoked-control components separate from still-parked mandatory
runtime control, then names the release conditions for any future expansion.

The roadmap is a governance and planning artifact only. It does not implement
new MCP tools, launcher behavior, direct IDE/shell/git/filesystem interception,
provider/live calls, CVF Web action execution, queue/daemon work, public-sync,
or universal governed-coding control.

## Authorization / Decision

| Field | Disposition |
| --- | --- |
| Authorization source | Delta-T5 GC-018 and work order dispatched at `a47e185b` |
| Execution base | `c320ca36` after dispatch continuity sync |
| Decision | accept a planning-only capability roadmap for Delta Execution Control |
| Risk ceiling | R1 governance-control documentation |
| Runtime expansion | blocked until a later fresh GC-018 and source-verified work order |

## Scope

Allowed scope:

- create this roadmap;
- create the Delta-T5 completion review;
- create the Delta-T5 evidence JSON;
- convert status and continuity only through later closure/session-sync phases.

Forbidden scope:

- no runtime source changes;
- no new MCP tools;
- no launcher behavior changes;
- no Model Gateway, CVF Web, workspace state, provider/live, public-sync,
  queue, daemon, lockfile, generated registry, or external repo changes;
- no direct IDE/shell/git/filesystem interception claim;
- no universal governed-coding control claim.

## Non-Goals

Delta-T5 does not attempt to make current MCP tools mandatory, intercept direct
actions, execute EDIT or COMMIT operations, add durable audit storage, add
background services, prove provider behavior, publish public artifacts, or ship
runtime control.

## Design Control Gate

| Gate | Disposition |
| --- | --- |
| DESIGN.md | N/A with reason: no UI/frontend/web work is authorized |
| Workspace design standard | N/A with reason: no workspace state, queue, or agent workspace build is authorized |
| External knowledge intake | applied through chain-map citation and source-backed absorption of the external runtime-control finding |
| Delta T4B boundary checker | avoided runtime/profile expansion and kept this roadmap to capability planning |
| Public/provenance boundary | provenance-only, no public-sync |

## Source Authority

| Source | Verified fact | Roadmap use |
| --- | --- | --- |
| `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md`, line 79 | `MCP-GW-001` requires pre-action governance/preflight, no direct provider bypass, no raw MCP/tool bypass, durable audit/receipt, and no governed-coding claim without CVF receipt | sets the Delta control target |
| `docs/reviews/CVF_MCP_MODEL_GATEWAY_COMPOSITION_PROOF_COMPLETION_2026-06-19.md`, lines 221-224 | Composition Proof is closed bounded and does not prove mandatory MCP runtime, durable audit, wrapper/proxy enforcement, or Delta Execution Control | prevents overclaiming the upstream proof |
| `docs/reviews/CVF_MCP_GATEWAY_EXECUTION_CONTROL_LEGACY_RECHECK_COMPLETION_2026-06-19.md`, lines 185-186 | Delta must carry durable audit/preflight/no-receipt controls after Composition Proof | anchors the next control-plane direction |
| `docs/reviews/CVF_DELTA_T1_GOVERNANCE_ACTION_PREFLIGHT_RECEIPT_COMPLETION_2026-06-19.md`, lines 202-204 | Delta-T1 proves invoked deterministic MCP preflight receipt, not mandatory invocation or action execution | defines Level 1 |
| `docs/reviews/CVF_DELTA_T2_GOVERNANCE_ACTION_RECEIPT_CONSUMPTION_COMPLETION_2026-06-19.md`, lines 47 and 112 | Delta-T2 proves receipt consumption but no action execution or universal control | defines Level 2 |
| `docs/reviews/CVF_DELTA_T3_GOVERNED_COMMAND_LAUNCHER_COMPLETION_2026-06-19.md`, lines 55 and 128 | commands outside the launcher remain bypassable and external interception stays parked | defines Level 3 |
| `docs/reviews/CVF_DELTA_T4A_APPROVAL_BACKED_MUTATING_PROFILE_BOUNDARY_COMPLETION_2026-06-19.md`, lines 54 and 120 | T4A remains opt-in and does not intercept direct IDE/shell/git/filesystem actions | defines Level 4 |
| `docs/reviews/CVF_DELTA_T4B_MUTATING_PROFILE_BOUNDARY_GUARD_COMPLETION_2026-06-19.md`, lines 58-65 | T4B is a document/control-plane guard and cannot intercept an agent bypassing CVF tools | defines Level 4G |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts`, lines 445-471 | MCP server registers the Delta-T1 and Delta-T2 tools | records current runtime surface |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/package.json`, line 9 | package publishes `cvf-governed-exec` | records current launcher surface |

## Current Runtime Freshness Verification

| Runtime fact | Source | Disposition |
| --- | --- | --- |
| Delta-T1 and Delta-T2 MCP tools are registered | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts`, lines 445-471 | source-visible |
| `cvf-governed-exec` is published as a package binary | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/package.json`, line 9 | source-visible |
| current source does not prove mandatory invocation | Delta-T1 and Composition Proof completion claim boundaries | not implemented in this tranche |
| current source does not prove direct interception | Delta-T3, T4A, and T4B completion claim boundaries | not implemented in this tranche |
| current source does not prove durable execution audit | MCP-GW recheck and Composition Proof completion claim boundaries | not implemented in this tranche |

## Capability Level Ledger

| Level | Current status | Proof surface | Allowed claim | Not proven |
| --- | --- | --- | --- | --- |
| L0 Guidance only | historical baseline | instructions, handoffs, and docs | agents are instructed to follow CVF | runtime control or receipt evidence |
| L1 Preflight receipt | `CLOSED_PASS_BOUNDED` in Delta-T1 | invoked MCP preflight tool | a cooperating caller can request deterministic governance preflight receipt | mandatory invocation, action execution, durable execution control |
| L2 Receipt consumption | `CLOSED_PASS_BOUNDED` in Delta-T2 | invoked MCP receipt consumer | a cooperating caller can submit a receipt for bounded admission checks | executing the action, forcing every agent action through CVF |
| L3 Governed launcher | `CLOSED_PASS_BOUNDED` in Delta-T3 | `cvf-governed-exec` launcher path | a bounded local launcher can own an opt-in command path | direct command interception, arbitrary shell coverage |
| L4 Local marker path | `CLOSED_PASS_BOUNDED` in Delta-T4A | fixed local marker profile | one explicit local marker path can require receipt-backed admission | broad mutation coverage, edit/commit execution, IDE interception |
| L4G Future-packet guard | `CLOSED_PASS_BOUNDED` in Delta-T4B | governed Markdown checker | future applicable packets must disclose boundary evidence | runtime enforcement or bypass prevention |
| L5 Capability roadmap | this Delta-T5 tranche | this roadmap and completion evidence | CVF has a source-backed map of capability levels, claim boundaries, and release conditions | new runtime behavior or mandatory action control |

## No-Receipt No-Claim Rule

CVF must not claim governed coding or governed action execution for a specific
action unless that action path has:

| Required evidence | Required meaning |
| --- | --- |
| CVF preflight receipt | the action was submitted to a CVF governance preflight path before execution |
| Receipt consumption or admission evidence | the receipt was accepted or rejected by a CVF-owned admission/consumer path |
| Execution or marker evidence | the executed path or recorded marker is owned by a CVF-controlled launcher/profile or a later authorized equivalent |
| Durable audit evidence | the action leaves a secret-safe record sufficient for later review |

If the action happens outside that evidence chain, the allowed disposition is
`NOT_CVF_GOVERNED_ACTION` or `UNGOVERNED_DIRECT_ACTION`, not governed coding.

## Claim Language Boundary

| Claim class | Allowed wording | Forbidden wording |
| --- | --- | --- |
| MCP tools | invoked MCP preflight or receipt-consumption path | MCP automatically controls all agent actions |
| Launcher | opt-in CVF launcher path with bounded receipt checks | CVF intercepts all shell commands |
| Local marker profile | one bounded local marker path with receipt-backed admission | broad edit, commit, or filesystem enforcement |
| T4B checker | document/control-plane packet guard | runtime bypass prevention |
| Delta overall | bounded Delta Execution Control foundation and roadmap | universal governed-coding control |
| Composition Proof | MCP and Model Gateway can compose at a bounded proof layer | durable runtime enforcement or provider-independent action control |

## Work Plan

| Step | Scope | Status |
| --- | --- | --- |
| 1 | Run pre-implementation from `c320ca36` | PASS |
| 2 | Author roadmap/completion/evidence only | COMPLETE |
| 3 | Run implementation steward and local gates | PASS |
| 4 | Commit material set | PASS at `f2ac570f` |
| 5 | Convert closure status and evidence | PASS in closure conversion |
| 6 | Sync active session continuity separately | POST_CLOSURE_SESSION_SYNC |

## Parked Capability Classes

| Capability class | Current disposition | Release condition |
| --- | --- | --- |
| Durable execution audit | PARKED | fresh GC-018, source-verified work order, explicit storage/audit schema, secret-safe retention rules, and local gate evidence |
| Wrapper/proxy enforcement | PARKED | fresh explicit authorization, threat model, command boundary, bypass claim boundary, and rollback plan |
| Direct IDE/shell/git/filesystem interception | PARKED | fresh runtime design authorization and proof that CVF owns the action path |
| EDIT and COMMIT action paths | PARKED | separate risk review, receipt chain, exact target policy, and closure-quality evidence |
| Provider/live proof | PARKED | live-governance authorization, key-handling plan, diagnostic standard compliance, and release-gate proof |
| CVF Web action execution | PARKED | WWU-T1 audit, fresh GC-018, DESIGN.md read for UI work, and fresh scope release |
| Queue, daemon, or background runtime | PARKED | runtime state topology authorization, generated-state guard plan, and operational failure model |
| Public-sync | PARKED | public export disposition update and sibling public-sync clone only |

## Next-Tranche Release Conditions

| Candidate tranche | Value | Required before dispatch |
| --- | --- | --- |
| Delta-T6 Execution Claim Boundary Checker | high | fresh GC-018 and work order for a machine guard that rejects universal execution-control claims without receipt/action evidence |
| Delta-T7 Receipt-To-Execution Evidence Auditor | high | source-verified schema for receipt, admission, execution marker, audit record, and expected changed set |
| Delta-T8 Wrapper/Proxy Pilot | medium to high | fresh runtime authorization, bounded command scope, bypass disclosure, and rollback evidence |
| Delta-T9 Durable Audit Store | high after T7 | storage contract, privacy boundary, retention/disposal rule, and machine drift check |
| CVF Web action path | high but parked | WWU-T1 surface audit and fresh Web Workspace work order |

No candidate above is implementation-ready from this roadmap alone.

## Acceptance Criteria

| ID | Criterion | Status |
| --- | --- | --- |
| AC1 | map completed Delta-T1 through Delta-T4B capabilities with source-backed claim boundaries | PASS |
| AC2 | name still-parked runtime expansion classes and release conditions | PASS |
| AC3 | include a no-receipt/no-claim rule for governed-coding control | PASS |
| AC4 | distinguish invoked MCP/wrapper control from mandatory external action interception | PASS |
| AC5 | name future tranche candidates without marking them implementation-ready | PASS |
| AC6 | avoid runtime/source/provider/public-sync changed files | PASS |

## Verification / Evidence

| Evidence | Status |
| --- | --- |
| Pre-implementation autorun gate from `c320ca36` | PASS |
| Implementation changed set | roadmap, completion review, evidence JSON only |
| Implementation steward | PASS |
| Pre-closure autorun gate | PASS in closure conversion range |
| Closure steward | PASS in closure conversion range |
| Public-sync | N/A with reason: not authorized |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | external runtime-control finding is adapted into CVF-owned roadmap, completion review, and evidence JSON |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | Delta-T5 roadmap |
| Disposition | `ABSORBED_AS_GOVERNANCE_BOUNDARY` |
| Claim boundary | no runtime/provider/live/public-sync/direct interception/universal governed-coding control claim |

External review correctly identified that current MCP and launcher work is not
mandatory runtime control. This roadmap absorbs that finding into CVF-owned
authority by converting it into claim language, capability levels, parked
runtime classes, and release conditions. The finding is not stored only in
agent memory.

## Closure Diff Expectations

| Requirement | Expected evidence |
| --- | --- |
| Allowed changed set | this roadmap, Delta-T5 completion review, Delta-T5 evidence JSON, then closure/status conversion |
| No runtime mutation | `git diff --name-status` and commit evidence show no runtime/source/provider/public paths |
| No overclaim | completion review confirms no mandatory invocation, runtime interception, provider behavior, public readiness, or universal control claim |
| Gate evidence | pre-implementation, implementation steward, pre-closure, closure steward, and hook evidence captured in completion/evidence artifacts |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | Delta-T5 work order | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_DELTA_T5_EXECUTION_CONTROL_CAPABILITY_ROADMAP_COMPLETION_2026-06-19.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | BLOCKED with reason: no corpus or runtime registry edit authorized | no registry path changed | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown edit authorized | no registry path changed | BLOCKED with reason |
| External evidence digest | N/A with reason: no new external source consumed beyond governed review artifacts | repo-local sources only | N/A with reason |
| System loop interlock | N/A with reason: no system loop registry edit authorized | no registry path changed | N/A with reason |
| Session continuity | active session state | separate post-closure session-sync commit required | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
| --- | --- | --- |
| status | `CLOSED_PASS_BOUNDED` | PASS |
| material commit | `f2ac570f` | PASS |
| closure base | `fb9bf935` | PASS |
| runtime scope added | false | PASS |
| provider/live scope added | false | PASS |
| public-sync performed | false | PASS |
| direct interception claimed | false | PASS |
| universal governed-coding claimed | false | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is private provenance governance planning. No public-sync is
authorized or performed from this workspace.

## Claim Boundary

Delta-T5 proves only a source-backed capability roadmap and claim boundary for
Delta Execution Control. It does not prove mandatory tool invocation, direct
IDE/shell/git/filesystem interception, provider behavior, hosted freshness,
public readiness, production readiness, release readiness, durable execution
audit, wrapper/proxy enforcement, or universal governed-coding control.
