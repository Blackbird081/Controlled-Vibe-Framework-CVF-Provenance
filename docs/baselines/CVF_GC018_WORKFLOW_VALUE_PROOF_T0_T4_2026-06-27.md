# GC-018 - Workflow Value Proof T0-T4

Memory class: GC_018_BASELINE

Status: CLOSED_PASS_BOUNDED

Owner: Codex

Date: 2026-06-27

Base head: `452414a4`

## Baseline Decision

Decision: authorize and close a bounded workflow value proof batch.

## Purpose

Authorize CVF Workflow Value Proof T0 through T4 using representative current
workflows, one fresh live release gate run, and a skeptical value verdict.

## Scope / Methodology

Scope: roadmap, GC-018, work order, completion review, current source
verification, and one live release gate command.

Methodology: select 2-3 representative workflows, verify from CVF-owned
surfaces, run one secret-safe live command, record evidence and limits, then
commit material separately from session-sync.

## Findings / Position

CVF workflow value is currently strongest in governed lifecycle continuity,
release-quality live proof, and read-model orientation. The value proof also
shows remaining friction: evidence packets are still paperwork-heavy, and
productization should wait for a specific next roadmap rather than broad
runtime expansion.

## Proposed Tranche

| Tranche | Scope | Disposition |
|---|---|---|
| WVP-T0 | Workflow selection proof | COMPLETE |
| WVP-T1 | Governed work lifecycle proof | COMPLETE |
| WVP-T2 | Live governance/provider proof | COMPLETE |
| WVP-T3 | Workspace read-model usefulness proof | COMPLETE |
| WVP-T4 | Value verdict | COMPLETE |

## Source Inventory

| File | Action |
|---|---|
| `CVF_SESSION_MEMORY.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V23_2026-06-26.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |
| `docs/CVF_ARCHITECTURE_DECISIONS.md` | SOURCE_VERIFIED |
| `scripts/run_cvf_release_gate_bundle.py` | SOURCE_VERIFIED |
| `docs/reviews/CVF_WLFA_T0_T4_FULL_PACKAGE_ABSORPTION_FOUNDATION_COMPLETION_2026-06-27.md` | SOURCE_VERIFIED |
| `docs/reviews/CVF_LWPRM_T0_T4_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_FOUNDATION_COMPLETION_2026-06-27.md` | SOURCE_VERIFIED |
| `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_FULL_PACKAGE_ABSORPTION_INVENTORY.md` | SOURCE_VERIFIED |
| `docs/reference/agent_workspace/CVF_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_DECISION.md` | SOURCE_VERIFIED |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Current next allowed move permits a fresh high-value foundation roadmap before implementation | `CVF_SESSION_MEMORY.md` | Startup Acknowledgment; Next Allowed Move | `local_workspace_projection_read_model_closed_pass_bounded_pending_next_foundation_selection` | active session front door | ACCEPT |
| Product value proof must be governed before heavy capability expansion | `docs/CVF_ARCHITECTURE_DECISIONS.md` | ADR-032 | `Product Value Proof Must Be Governed Before Heavy Capability Expansion` | architecture decision record | ACCEPT |
| Full live release gate command is canonical release-quality proof command | `scripts/run_cvf_release_gate_bundle.py` | Usage; `main` | `scripts/run_cvf_release_gate_bundle.py --json` | release gate bundle | ACCEPT |
| Live governance E2E requires a DashScope-compatible live key before passing | `scripts/run_cvf_release_gate_bundle.py` | `check_e2e` | `DASHSCOPE_API_KEY` | release gate bundle | ACCEPT |
| WLFA closed with T0 through T4 package absorption evidence and no runtime expansion | `docs/reviews/CVF_WLFA_T0_T4_FULL_PACKAGE_ABSORPTION_FOUNDATION_COMPLETION_2026-06-27.md` | Findings / Position; Claim Boundary | `WLFA-T0 through WLFA-T4` | WLFA completion review | ACCEPT |
| LWPRM closed with read-model foundation evidence and separate session-sync requirement | `docs/reviews/CVF_LWPRM_T0_T4_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_FOUNDATION_COMPLETION_2026-06-27.md` | Scope / Methodology; Machine Closure Package | `LWPRM-T0-T4` | LWPRM completion review | ACCEPT |
| Package inventory parks runtime, provider, and public scope after read-model recommendation | `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_FULL_PACKAGE_ABSORPTION_INVENTORY.md` | Next-Roadmap Recommendation | `Runtime, MCP, CLI, IDE bridge, provider/live proof, and public-sync remain parked` | package absorption inventory | ACCEPT |
| Read-model decision maps closure and evidence readiness to governed artifacts and gates | `docs/reference/agent_workspace/CVF_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_DECISION.md` | Projection Sections | `closureReadiness`; `requiredEvidence` | local workspace projection read model | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`workflow_value_proof`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

## Roadmap-To-Work-Order Trace Matrix

| Roadmap item | Work order section | Completion evidence |
|---|---|---|
| WVP-T0 workflow selection | Representative Workflow Matrix | roadmap and completion review |
| WVP-T1 lifecycle proof | Workflow Value Evidence Matrix | WLFA/LWPRM evidence |
| WVP-T2 live proof | Live Governance Proof | release gate PASS |
| WVP-T3 read-model proof | Workspace Read-Model Usefulness Proof | inventory and read-model reference |
| WVP-T4 verdict | Value Verdict | completion review |

## Allowed Scope

- Add this GC-018 baseline.
- Add the matching roadmap.
- Add the matching work order.
- Add the matching completion review.
- Run one fresh full release gate command.
- Run governance gates and commit material after gates pass.

## Forbidden Scope

- DICE work.
- Package activation.
- Package certification decision.
- Runtime, MCP, CLI, or IDE bridge implementation.
- Generated workspace state mutation.
- Resolver or adapter mutation.
- Public-sync or push.
- Broad live rerun loop.
- Mixing material commit with session-sync commit.

## Live Run Diagnostics

| Command | Stage | Result | Diagnostic |
|---|---|---|---|
| `python scripts/run_cvf_release_gate_bundle.py --json` | release-quality live governance proof | PASS | N/A with reason: no failed, partial, timed-out, empty-output, or rerun-triggering live run occurred |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | workflow value proof artifacts | internal agents may cite the verdict for future roadmap selection only | source verification and completion review | N/A with reason: no adapter created | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | future external-agent workflow execution support remains deferred | no executable external-agent support or CLI/MCP ingress claim | claim boundary | deferred adapter owner; fresh GC-018 required | DEFERRED_WITH_REASON |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator instruction is authorization context only; source facts are re-verified against CVF-governed surfaces |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | governed roadmap, baseline, work-order, and review artifact surfaces |
| Disposition | ADAPT operator-approved value-proof scope into CVF-owned artifacts |
| Claim boundary | the attached prompt is not used as source proof for runtime fields, package facts, live results, or public claims |

## Current Runtime Freshness Verification

| Runtime claim | Current evidence | Disposition |
|---|---|---|
| Runtime implementation | no runtime path is in Allowed Scope | NOT_IMPLEMENTED_WITH_REASON |
| MCP or CLI adapter | no MCP or CLI adapter path is in Allowed Scope | NOT_IMPLEMENTED_WITH_REASON |
| Provider/live proof | one release gate command was run and passed | PASS_WITH_CURRENT_COMMAND_EVIDENCE |
| Generated workspace state mutation | generated workspace state is outside Allowed Scope | NOT_IMPLEMENTED_WITH_REASON |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | GC-018 authorization for workflow value proof |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: source verification, live release gate output, completion review, and gate output |
| actionEvidence | ACTION_EVIDENCE_PRESENT: planned material manifest and completion evidence |
| invocationBoundary | local source reads, governed markdown edits, and one live release gate command |
| interceptionBoundary | no runtime interception or adapter behavior changed |
| claimLanguage | workflow value proof only |
| forbiddenExpansion | no DICE, package activation, certification decision, runtime, MCP, CLI, IDE bridge, generated workspace state mutation, resolver mutation, adapter mutation, public-sync, push, or broad live rerun loop |

## Acceptance Criteria

| Criterion | Evidence |
|---|---|
| Representative workflows selected | Representative Workflow Matrix |
| Lifecycle evidence source-verified | Source Verification Block |
| Live proof fresh and secret-safe | release gate PASS summary |
| Read-model usefulness evaluated | completion review |
| Value verdict records both value and friction | completion review |
| Forbidden expansion remains blocked | claim boundaries |

## Evidence / Verification

Required verification before material commit:

- `python scripts/run_cvf_release_gate_bundle.py --json`
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 452414a4 --head HEAD`
- `python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base 452414a4 --head HEAD --enforce`
- `git diff --check`

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_WORKFLOW_VALUE_PROOF_T0_T4_FOR_CODEX_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_WORKFLOW_VALUE_PROOF_T0_T4_COMPLETION_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_WORKFLOW_VALUE_PROOF_T0_T4_ROADMAP_2026-06-27.md` | `Status: ROADMAP_CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | no corpus registry source edit required | N/A | BLOCKED with reason: no corpus registry source edit authorized |
| Registry Markdown | no registry Markdown edit authorized | N/A | BLOCKED with reason: no registry Markdown edit authorized |
| External evidence digest | no external evidence file is promoted as CVF source authority | operator authorization reverified against CVF-governed source rows | BLOCKED with reason: no external evidence artifact is promoted |
| System loop interlock | no system-loop registry mutation in scope | `governance/compat/check_system_loop_interlock.py` via autorun | PASS |
| Live governance proof | current command output | `python scripts/run_cvf_release_gate_bundle.py --json` returned PASS | PASS |
| Session continuity | session-sync required after material commit | active session state and handoff after material commit | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance value proof. No public-sync batch is authorized.

## Claim Boundary

This GC-018 authorizes only workflow value proof documentation and one live
release gate command. It does not authorize DICE, package activation, package
certification decision, runtime/MCP/CLI/IDE bridge implementation, generated
workspace state mutation, resolver mutation, adapter mutation, public-sync,
push, production readiness, or public readiness.
