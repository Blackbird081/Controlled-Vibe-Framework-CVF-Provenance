# CVF GC-018 DSCP-T11F Profile Selection Adapter Baseline

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: baseline

Date: 2026-06-10

---

## Authorization

Authorized by operator instruction on 2026-06-10: check and commit DSCP-T11E,
then audit and create the next roadmap and work order for Claude.

Active state:

`CVF_SESSION/ACTIVE_SESSION_STATE.json`

Active handoff:

`AGENT_HANDOFF_V17_2026-06-07.md`

## Decision

Open DSCP-T11F as a bounded deterministic CPF source/test tranche.

T11F consumes the closed DSCP-T10 domain profile contract, DSCP-T11 local
profile-aware harness, and DSCP-T11E registry/selector. It adds an adapter that
selects a domain profile and applies it to descriptor input only when exactly
one eligible profile is selected and profile gate application does not block.

## Purpose

Centralize scan-layer profile-selection stop semantics before any external
PolicyLocal integration. Future domain integrations should consume one local
adapter result contract instead of duplicating no-match, ambiguous-match, and
`BLOCKED_UNTIL_*` handling.

## Predecessor Evidence

| Predecessor | Closure evidence | Disposition |
|---|---|---|
| DSCP-T10 domain profile contract | `docs/reviews/CVF_DSCP_T10_DOMAIN_PROFILE_AND_SCAN_ADAPTER_CONTRACT_COMPLETION_2026-06-10.md`; material commit `0afa8737` | ACCEPT |
| DSCP-T11 profile-aware pipeline harness | `docs/reviews/CVF_DSCP_T11_PROFILE_AWARE_PIPELINE_HARNESS_COMPLETION_2026-06-10.md`; material commit `4c39ce77` | ACCEPT |
| DSCP-T11E domain profile registry | `docs/reviews/CVF_DSCP_T11E_DOMAIN_PROFILE_REGISTRY_COMPLETION_2026-06-10.md`; material commit `8a7cd134` | ACCEPT |
| Post-T11E audit | `docs/audits/CVF_DSCP_POST_T11E_NEXT_ROADMAP_AUDIT_2026-06-10.md` | ACCEPT |

## Scope / Target / Owner Boundary

In scope:

- Add a deterministic CPF profile selection adapter.
- Use `DscpDomainProfileRegistry.select` for local selection.
- Use `applyDomainProfileToDescriptorInput` only after exactly one profile
  matches.
- Return explicit stop diagnostics for no match, ambiguous match, and blocked
  profile application.
- Export the adapter through the CPF barrel.
- Add focused CPF tests.
- Register new source and test files in GC-051 JSON and Markdown.
- Produce a worker return packet under `WORKER_MUST_NOT_COMMIT`.

Out of scope:

- No external `Policy_Local` workspace edits.
- No corpus ingestion, OCR, body extraction, vector search, semantic ranking,
  T12 authoring, provider calls, API key use, cvf-web route changes,
  public-sync, hosted readiness, production readiness, public readiness, or
  legal advice quality claims.

## Source Verification Summary

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| EXISTS: selection criteria contract | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.registry.ts` | line 10 | `DomainProfileSelectionCriteria` | `DomainProfileSelectionCriteria` | ACCEPT |
| EXISTS: selection result contract | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.registry.ts` | line 22 | `DomainProfileSelectionResult` | `DomainProfileSelectionResult` | ACCEPT |
| EXISTS: profile registry class | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.registry.ts` | line 46 | `DscpDomainProfileRegistry` | `DscpDomainProfileRegistry` | ACCEPT |
| RUNTIME_BEHAVIOR: registry selection | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.registry.ts` | line 90 | `select` | `DscpDomainProfileRegistry.select` | ACCEPT |
| EXISTS: registry factory | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.registry.ts` | line 169 | `createDscpDomainProfileRegistry` | `createDscpDomainProfileRegistry` | ACCEPT |
| EXISTS: domain profile contract | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 23 | `DscpDomainProfile` | `DscpDomainProfile` | ACCEPT |
| RUNTIME_BEHAVIOR: profile application helper | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 92 | `applyDomainProfileToDescriptorInput` | `applyDomainProfileToDescriptorInput` | ACCEPT |
| EXISTS: registry barrel export | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.context.barrel.ts` | line 86 | `DscpDomainProfileRegistry` | `control.plane.context.barrel.ts` | ACCEPT |

New T11F implementation symbols are authorized outputs of this tranche, not
pre-existing source facts. They must be verified after implementation by
focused tests and completion evidence.

## Evidence / Verification

| Evidence | Required result |
|---|---|
| CPF package check | PASS |
| Focused DSCP-T11F vitest | PASS |
| Reviewer-fast gate | PASS, current chain count |
| GC-051 registry coverage | PASS |
| Forbidden paths | none modified |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`roadmap-status-reconciliation`, role=`reviewer`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T11F_PROFILE_SELECTION_ADAPTER_FOR_CLAUDE_2026-06-10.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_DSCP_T11F_PROFILE_SELECTION_ADAPTER_COMPLETION_2026-06-10.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_DSCP_T11F_PROFILE_SELECTION_ADAPTER_ROADMAP_2026-06-10.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Adapter source | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.profile.selection.adapter.ts` | source exists and current typecheck PASS | PASS |
| Focused tests | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.profile.selection.adapter.test.ts` | 14/14 focused tests PASS | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | GC-051 aggregate drift check PASS | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | DSCP-T11F quick lookup rows present | PASS |
| External evidence digest | N/A with reason: no external evidence digest | no external digest | N/A with reason |
| System loop interlock | N/A with reason: no system-loop mutation | no system-loop path in changed set | N/A with reason |
| Session continuity | active front door/state/handoff after material commit | session-sync follows material commit | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| DSCP-T11F-GC018-STATUS | this baseline | top-level `Status:` | CLOSED_PASS_BOUNDED | CLOSED_PASS_BOUNDED | PASS |
| DSCP-T11F-COMPLETION | completion review | top-level `Status:` | CLOSED_PASS_BOUNDED | CLOSED_PASS_BOUNDED | PASS |
| DSCP-T11F-FOCUSED-TESTS | current command output | tests count | 14 passed | 14 passed | PASS |

## Claim Boundary

This baseline authorizes only a local deterministic CPF profile selection
adapter and focused tests. It does not claim provider behavior, live governance
proof, retrieval quality, semantic correctness, corpus ingestion, OCR, vector
search, PolicyLocal T12 readiness, current-law status, legal advice quality,
public readiness, hosted readiness, production readiness, public-sync, memory
reinjection, high-risk promotion, Learning Orchestrator runtime behavior, or
autonomous mutation.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance baseline; not public-synced.
