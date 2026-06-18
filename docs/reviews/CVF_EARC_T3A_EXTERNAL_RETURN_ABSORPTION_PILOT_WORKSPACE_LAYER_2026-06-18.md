# CVF EARC-T3A External Return Absorption Pilot - Workspace Layer Package

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-18

docType: review

## Purpose

Run the first bounded EARC-T3 absorption pilot on the operator-copied
workspace-layer production handoff package.

## Scope / Target / Owner Boundary

Target: classify selected package observations through the EARC-T3 absorption
workflow and update the CVF-owned workspace package absorption map.

Owner boundary: Codex owns this absorption review and session-sync. This packet
does not authorize public-sync, MCP implementation, provider/live calls,
workspace runtime mutation, raw package import, checker implementation, or
readiness claims.

## Evidence Trace Block

| Evidence item | Path | Role |
|---|---|---|
| Absorption workflow | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md` | Required table and disposition rules |
| Existing absorption map | `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md` | Prior CVF-owned map for package concepts |
| Package README | workspace-layer package README under the copied root folder | Authority/projection and completion-state claims |
| MCP API | workspace-layer package MCP API document under the copied root folder | State-first/proposal/receipt MCP pattern |
| MCP contract | workspace-layer package MCP contract under the copied root folder | Non-bypass and precondition/postcondition pattern |
| State projection contract | workspace-layer package state projection contract under the copied root folder | Generated state projection pattern |
| Workflow schema | workspace-layer package workflow schema under the copied root folder | Hard-coded public/simple workflow enum |
| Smoke result | workspace-layer package smoke-result JSON under the copied root folder | Local package smoke evidence only |
| Root lifecycle registry | `governance/compat/CVF_ROOT_FOLDER_LIFECYCLE_REGISTRY.json` | Package root is frozen internal reference |

## External Artifact Hash Manifest

| External artifact | sha256 |
|---|---|
| workspace-layer package README | `a267edd4f9702daa1047034520f3e24b0c7321b17d1451a858b12a2845b7cd82` |
| workspace-layer package MCP API document | `b3897e04801b6fdadf70c0ca46be579e3e64149eef40b74778fb4942d6cff3d7` |
| workspace-layer package MCP contract | `545ca7842f447c5de5f17ca0788e05b29748770bb450d808a9bd6e30b4297e93` |
| workspace-layer package state projection contract | `52b458d57fc443cf579196db5517811718bdf84e2ad6b84896c92cbc1e182956` |
| workspace-layer package workflow schema | `4b74d469effcafe1d0cc2993e4479f4f9431cda3c62963084df860f07cb8a9b5` |
| workspace-layer package smoke-result JSON | `1900be01745d5568c4040108938fc8b79a0b7eb6248a4805253578eecb41de6f` |

## Target / Source

Target: the CVF-owned absorption decision for the copied workspace-layer
package.

Source: external raw package files listed in the Evidence Trace Block and hash
manifest, constrained by CVF-governed workflow, roadmap, and root lifecycle
surfaces.

## Findings / Position

Position: absorb/adapt only the projection, proposal-before-execution,
receipt-backed evidence, and non-bypass vocabulary that aligns with existing
CVF foundations. Reject the hard-coded workflow enum as authority and treat the
package smoke result as advisory only.

## Risk / Corrective Action

Risk: external package wording can be mistaken for CVF runtime or public
readiness.

Corrective action: this packet records explicit claim boundaries, updates the
CVF-owned absorption map, and leaves checker hardening to EARC-T3B with fresh
GC-018.

## Required Absorption Table

| External item ID | External claim summary | Source basis | CVF verification surface | CVF disposition | Owner artifact | Next action | Claim boundary |
|---|---|---|---|---|---|---|---|
| EARC-T3A-E01 | CVF Core remains authority; workspace state is projection. | external reference aligned with CVF-governed map | `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md` `## Useful Patterns`; package `README.md` `## Authority Rule` | `PATTERN_ABSORB_ADAPT_DEFER_REJECT`: `ABSORB` | workspace absorption map | handled now by pilot note reinforcing projection-not-authority | Does not authorize workspace runtime implementation. |
| EARC-T3A-E02 | Workspace MCP should be state-first, proposal-before-execution, CVF-authorized, receipt-backed, and human-auditable. | external reference | `docs/reference/mcp_gateway/CVF_MODEL_GATEWAY_MCP_RUNTIME_BRIDGE_BOUNDARY.md`; package `WORKSPACE_MCP_API.md` `## MCP Design Principles` | `PATTERN_ABSORB_ADAPT_DEFER_REJECT`: `ADAPT` | workspace absorption map; future EARC-T4 decision input | handled now as decision input; implementation deferred to explicit MCP/runtime authorization | Does not add MCP tools or runtime behavior. |
| EARC-T3A-E03 | MCP non-bypass rule blocks raw dangerous tools and forces proposal, governance validation, approval or receipt, and CVF-controlled execution. | external reference | package `WORKSPACE_MCP_CONTRACT.md` `## Non-Bypass Rule`; AHB and autorun standards remain CVF authority | `PATTERN_ABSORB_ADAPT_DEFER_REJECT`: `ADAPT` | workspace absorption map; future MCP/workspace guard design | handled now as guard vocabulary candidate | Does not prove the denylist is complete CVF policy. |
| EARC-T3A-E04 | State projection contract lists five generated state files with deterministic/minimal/blocked-on-invalid rules. | external reference | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`; package `STATE_PROJECTION_CONTRACT.md` | `PATTERN_ABSORB_ADAPT_DEFER_REJECT`: `ADAPT` | workspace absorption map; future workspace state local-view design | handled now as mapping input to existing generated state topology | Does not create new state files. |
| EARC-T3A-E05 | Workflow schema uses `INTAKE`, `DESIGN`, `SPEC`, `WORK_ORDER`, `BUILD`, `REVIEW`, and `FREEZE`. | public/simple or external package vocabulary | `docs/reference/external_agent_review/CVF_WORKFLOW_CHAIN_PUBLIC_REVIEW_CONTEXT.md`; EARC roadmap non-goal | `QUESTION_OR_HYPOTHESIS` plus `PATTERN_ABSORB_ADAPT_DEFER_REJECT`: `REJECT_AS_AUTHORITY` | workspace absorption map | handled now: display vocabulary only, not internal CVF workflow-chain authority | Does not redefine CVF roadmap/AHB/autorun state. |
| EARC-T3A-E06 | Package smoke result says local demo approved a safe proposal, blocked a dangerous one, and created evidence. | external reference evidence | package `tests/PRODUCTION_HANDOFF_SMOKE_RESULT.json`; EARC roadmap runtime boundaries | `BLOCKED_UNTIL_CVF_PROOF` for any CVF runtime claim; `NON_CANONICAL_ADVISORY` for package-local test value | absorption review packet | handled now as local package evidence only | Does not prove CVF runtime, MCP, provider, release, public, or production readiness. |
| EARC-T3A-E07 | Package says it is ready for controlled handoff into CVF but not production-complete until wired to real CVF Core and production MCP server. | external reference plus own caveat | package `README.md` `## Production Handoff Additions`; root lifecycle registry | `RETURN_TO_OPERATOR_OR_REVIEWER` for implementation authorization; `NON_CANONICAL_ADVISORY` for readiness wording | EARC roadmap parked boundaries | handled now: no implementation opens without explicit operator authorization | Does not authorize EARC-T4. |
| EARC-T3A-E08 | The first real external-return packet exercised the Required Absorption Table shape. | CVF-governed review evidence | this packet `## Required Absorption Table` | `GOVERNANCE_LEARNING_REQUIRED` | EARC-T3 checker candidate | future tranche may add checker for absorption review packets | Does not implement the checker in T3A. |

## Absorption Decisions

| Decision | Result |
|---|---|
| Projection-not-authority | `ABSORB`: aligned with existing CVF workspace state topology. |
| MCP proposal/evidence/receipt boundary | `ADAPT`: useful for future EARC-T4, but must bind to CVF AHB, autorun, receipt, and Model Gateway/MCP boundaries. |
| Non-bypass dangerous action denylist | `ADAPT`: useful vocabulary, not a complete CVF policy engine. |
| Five state files | `ADAPT`: use as local-view projection input, not a replacement for generated CVF state aggregates. |
| Hard-coded workflow enum | `REJECT_AS_AUTHORITY`: display vocabulary only. |
| Smoke test result | `NON_CANONICAL_ADVISORY`: local package evidence only. |
| Package handoff readiness wording | `BLOCKED_UNTIL_CVF_PROOF`: no CVF runtime/readiness claim. |

## Checker Readiness Decision

Verdict: `CHECKER_READY_FOR_FRESH_GC018`.

Reason: T3A provides the first real absorption review shape using the Required
Absorption Table. A future checker can require this table for changed
external-return absorption reviews and should remain range-aware so it does not
retroactively fail historical reviews.

Do not implement the checker in this tranche.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_FOR_CODEX_2026-06-18.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| GC-018 | `docs/baselines/CVF_GC018_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_2026-06-18.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_EXTERNAL_AGENT_REVIEW_CONTEXT_SYSTEMIZATION_ROADMAP_2026-06-18.md` | EARC-T3A row and closure note | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | generated from source entries | PASS |
| Registry Markdown | BLOCKED with reason: no separate markdown registry is required for this reference family | no path changed | BLOCKED with reason |
| External evidence digest | this file | Required Absorption Table plus External Artifact Hash Manifest; representative sha256 `a267edd4f9702daa1047034520f3e24b0c7321b17d1451a858b12a2845b7cd82` | PASS |
| System loop interlock | BLOCKED with reason: no runtime interlock implementation changed | no path changed | BLOCKED with reason |
| Session continuity | separate session-sync follows material commit | active session surfaces update after material commit | N/A with reason |
| Runtime proof | BLOCKED with reason: runtime/provider/MCP proof is out of scope | no runtime proof required | BLOCKED with reason |
| Public export disposition | `DEFERRED_PRIVATE_ONLY` | private provenance absorption pilot | PASS |

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance absorption pilot. Public-facing versions require
separate public-sync authorization.

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| External smoke result is not accepted as CVF runtime proof | no CVF proof claim | advisory-only disposition in Required Absorption Table | PASS |
| Receipt-backed MCP pattern is only an absorbed vocabulary candidate | no MCP implementation or receipt claim | EARC-T4 deferred; no runtime path changed | PASS |
| CVF acceptance receipt for this tranche | material commit plus gates, not external package receipt | pending material commit at review-authoring time | N/A with reason |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-18 EARC-T3A external return absorption pilot |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch |
| Target paths | EARC-T3A GC-018; work order; absorption review packet; completion review; workspace-layer absorption map; EARC roadmap; GC-051 registry entry and aggregate |
| Allowed scope source | operator authorization after EARC-T3 closure and GC-018 |
| Before status evidence | base `0f6d54e8`; clean worktree |
| After status evidence | EARC-T3A material closure pending commit |
| Diff evidence | `git diff --name-status 0f6d54e8..HEAD` |
| Approval boundary | bounded reference absorption pilot only |
| Claim boundary | no public-sync, MCP implementation, provider/live call, workspace runtime mutation, raw package import, checker implementation, readiness claim |
| Agent type | Codex implementer/closer |
| Invocation ID | `earc-t3a-external-return-absorption-pilot-2026-06-18` |
| Expected manifest | `docs/baselines/CVF_GC018_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_2026-06-18.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_FOR_CODEX_2026-06-18.md`; `docs/reviews/CVF_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_WORKSPACE_LAYER_2026-06-18.md`; `docs/reviews/CVF_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_COMPLETION_2026-06-18.md`; `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md`; `docs/roadmaps/CVF_EXTERNAL_AGENT_REVIEW_CONTEXT_SYSTEMIZATION_ROADMAP_2026-06-18.md`; `docs/corpus-intelligence/registry/entries/earc-t3a-external-return-absorption-pilot.json`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` |
| Actual changed set | `docs/baselines/CVF_GC018_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_2026-06-18.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_FOR_CODEX_2026-06-18.md`; `docs/reviews/CVF_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_WORKSPACE_LAYER_2026-06-18.md`; `docs/reviews/CVF_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_COMPLETION_2026-06-18.md`; `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md`; `docs/roadmaps/CVF_EXTERNAL_AGENT_REVIEW_CONTEXT_SYSTEMIZATION_ROADMAP_2026-06-18.md`; `docs/corpus-intelligence/registry/entries/earc-t3a-external-return-absorption-pilot.json`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Finding-To-Governance Learning Disposition

| Field | Disposition |
|---|---|
| Finding | The first real external-return absorption packet proves the Required Absorption Table is a stable enough surface for a future checker. |
| Defect class | `RULE_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Escalation state | `MACHINE_CHECK_CANDIDATE_READY` |
| Governance action | Ran EARC-T3A pilot and updated absorption map with CVF-owned conclusions. |
| Machine-check action | `MACHINE_CHECK_CANDIDATE`: open EARC-T3B with fresh GC-018 to require the Required Absorption Table for changed external-return absorption reviews. |
| Next action | EARC-T3B checker hardening is the next highest-value EARC foundation tranche if the operator continues. |
| Runtime/provider/cost learning lane | `N/A_WITH_REASON`: no runtime/provider/cost behavior was changed or measured. |

## Epistemic Process Block

### Expected Result / Prediction

The external workspace-layer package should yield useful MCP/workspace patterns
while also exposing claims that must stay blocked or advisory.

### Evidence Comparison

The package supplies useful projection, proposal, receipt, event, and non-bypass
patterns. It also carries a hard-coded workflow enum and local smoke evidence
that cannot be treated as CVF runtime proof.

### Contradiction Or Gap Disposition

The pilot confirms the T3 absorption workflow is usable. The remaining gap is a
machine checker for future absorption reviews.

### Claim Update

CVF has now absorbed the external package through a real governed review packet
without importing package code or opening runtime/public scope.

## Claim Boundary

This packet is a private provenance absorption review. It does not publish,
public-sync, implement MCP, mutate workspace runtime state, run providers,
import raw external packages, add a checker, or claim readiness.
