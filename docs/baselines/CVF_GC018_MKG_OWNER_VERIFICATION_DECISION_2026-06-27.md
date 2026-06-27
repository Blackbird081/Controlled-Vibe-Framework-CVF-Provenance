# GC-018 - MKG Owner Verification Decision

Memory class: GC_018_BASELINE

Status: CLOSED_PASS_BOUNDED

Owner: Codex

Date: 2026-06-27

Base head: `e761e590`

## Baseline Decision

Decision: authorize and close a bounded `REFERENCE_ONLY` MKG owner-verification
decision for the three deferred MKG groups.

## Purpose

Clarify the current owner-surface status of cortex runtime/bridge, governed
skill evolution, and graph implementation plan candidates after MPFR closed
the stale pending-finality ambiguity.

## Scope / Methodology

Scope: roadmap, GC-018, work order, stable owner decision reference, and
completion review.

Methodology: source-verify prior MKG evidence and current owner surfaces, write
a stable routing decision, run governance gates, and keep session-sync separate
after material commit.

## Findings / Position

MKGOV closes the owner-routing ambiguity while keeping runtime authority
blocked. It distinguishes metadata intake, package contract, and local advisory
graph owner surfaces from runtime, mutation, adapter, live, and public claims.

## Proposed Tranche

| Tranche | Scope | Disposition |
|---|---|---|
| MKGOV-T0 | Source-verify prior MKG evidence | COMPLETE |
| MKGOV-T1 | Verify current owner surfaces | COMPLETE |
| MKGOV-T2 | Add stable owner decision | COMPLETE |
| MKGOV-T3 | Record next-control rule | COMPLETE |
| MKGOV-T4 | Closure and gates | COMPLETE |

## Source Inventory

| File | Action |
|---|---|
| `CVF_SESSION_MEMORY.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V23_2026-06-26.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |
| `docs/reference/CVF_MKG_PENDING_FINALITY_RECONCILIATION_DECISION.md` | SOURCE_VERIFIED |
| `docs/reviews/CVF_MKG1_MEMORY_KNOWLEDGE_GRAPH_OWNER_SURFACE_REVIEW_COMPLETION_2026-06-01.md` | SOURCE_VERIFIED |
| `docs/reviews/CVF_MKG2_DEFERRED_RUNTIME_CANDIDATE_TRIAGE_REVIEW_2026-06-01.md` | SOURCE_VERIFIED |
| `docs/reviews/CVF_MKG3_CURRENT_OWNER_NEGATIVE_SEARCH_EVIDENCE_REVIEW_2026-06-01.md` | SOURCE_VERIFIED |
| `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | SOURCE_VERIFIED |
| `docs/reference/CVF_MEMORY_PLANE_MAP.md` | SOURCE_VERIFIED |
| `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | SOURCE_VERIFIED |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mlw7-external-capability-ingestion.ts` | SOURCE_VERIFIED |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Current next allowed move permits MKG owner-verification lane | `CVF_SESSION_MEMORY.md` | Next Allowed Move | `nextAllowedMove` | active session front door | ACCEPT |
| MPFR says MKG owner-verification needs fresh GC-018 | `docs/reference/CVF_MKG_PENDING_FINALITY_RECONCILIATION_DECISION.md` | Routing Rule | `Routing Rule` | MPFR decision reference | ACCEPT |
| MKG2 carries 21 deferred candidates in three groups | `docs/reviews/CVF_MKG2_DEFERRED_RUNTIME_CANDIDATE_TRIAGE_REVIEW_2026-06-01.md` | Candidate Group Summary | `Candidate Group Summary` | MKG2 review | ACCEPT |
| Graph/context-builder work has current owner surfaces | `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | Lookup Table | `Scoping graph or context-builder work` | operational reference index | ACCEPT |
| KGR1 local graph status is running and bounded | `docs/reference/CVF_MEMORY_PLANE_MAP.md` | KGR1 Structural Graph Context Index | `KGR1 Structural Graph Context Index` | memory plane map | ACCEPT |
| ASSF package contract absorbs Memento skill evolution as lifecycle input | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | ASSF-T0.1 Ledger Consumption Table | `ASSF-T0.1 Ledger Consumption Table` | ASSF package contract | ACCEPT |
| Cortex external-capability candidate class exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mlw7-external-capability-ingestion.ts` | type declaration | `ExternalCapabilityCandidateClass` | MLW7 external capability ingestion | ACCEPT |
| Cortex intake blocks install, execute, authority, delegation, publication, adapter runtime | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mlw7-external-capability-ingestion.ts` | readout invariant | `noInstallNoExecuteInvariant` | MLW7 external capability ingestion | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`mkg_owner_verification`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

## Allowed Scope

- Add this GC-018 baseline.
- Add the matching roadmap.
- Add the matching work order.
- Add `docs/reference/CVF_MKG_OWNER_VERIFICATION_DECISION.md`.
- Add the matching completion review.
- Run governance gates and commit material after gates pass.

## Forbidden Scope

- Runtime, MCP, CLI, or IDE bridge implementation.
- UI or dashboard implementation.
- Checker implementation.
- Further provider/live proof.
- Generated workspace state mutation.
- Resolver, adapter, interlock registry, corpus registry, or package registry
  mutation.
- Package activation or certification decision.
- Public-sync or push.
- DICE work.
- Rewriting original MKG1/MKG2/MKG3/MKG4 artifacts.
- Mixing material commit with session-sync commit.

## Current Runtime Freshness Verification

| Runtime claim | Current evidence | Disposition |
|---|---|---|
| Runtime implementation | no runtime path is in Allowed Scope | NOT_IMPLEMENTED_WITH_REASON |
| UI or dashboard implementation | no UI path is in Allowed Scope | NOT_IMPLEMENTED_WITH_REASON |
| Checker implementation | no checker path is in Allowed Scope | NOT_IMPLEMENTED_WITH_REASON |
| MCP or CLI adapter | no MCP or CLI adapter path is in Allowed Scope | NOT_IMPLEMENTED_WITH_REASON |
| Provider/live proof | no provider/live proof is authorized or run | NOT_IMPLEMENTED_WITH_REASON |
| Generated workspace state mutation | generated workspace state is outside Allowed Scope | NOT_IMPLEMENTED_WITH_REASON |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | MKGOV decision reference | internal agents may use it for MKG routing only | source verification rows | N/A with reason: no adapter created | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | external owner readout support remains deferred | no executable external-agent support | claim boundary | deferred adapter owner; fresh GC-018 required | DEFERRED_WITH_REASON |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator continuation is authorization context only; source facts are re-verified against CVF-governed surfaces |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | governed roadmap, baseline, work-order, reference, and review artifact surfaces |
| Disposition | ADAPT continuation into CVF-owned owner-verification artifacts |
| Claim boundary | no external prompt is used as source proof for runtime fields, package facts, live results, or public claims |

## Claim Boundary

This baseline authorizes only a reference owner-verification decision. It does
not authorize runtime behavior, UI, checker, MCP, CLI, IDE bridge,
provider/live proof, public-sync, generated workspace state mutation, resolver
mutation, adapter mutation, registry mutation, package activation,
certification decision, DICE, production readiness, public readiness, or push.

## Evidence / Verification

Required verification before material commit:

- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base e761e590 --head HEAD`
- `python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base e761e590 --head HEAD --enforce`
- `git diff --check`

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_MKG_OWNER_VERIFICATION_DECISION_FOR_CODEX_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_MKG_OWNER_VERIFICATION_DECISION_COMPLETION_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_MKG_OWNER_VERIFICATION_DECISION_ROADMAP_2026-06-27.md` | `Status: ROADMAP_CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | no registry source edit required | N/A | BLOCKED with reason: registry mutation not authorized |
| Registry Markdown | no registry Markdown edit required | N/A | BLOCKED with reason: registry mutation not authorized |
| External evidence digest | no external evidence file promoted | all claims reverified against CVF-governed source rows | BLOCKED with reason: no external evidence artifact is promoted |
| System loop interlock | no system-loop registry mutation in scope | autorun gate output | PASS |
| Session continuity | session-sync required after material commit | active session state and handoff after material commit | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance owner-verification work. No public-sync batch is
authorized.
