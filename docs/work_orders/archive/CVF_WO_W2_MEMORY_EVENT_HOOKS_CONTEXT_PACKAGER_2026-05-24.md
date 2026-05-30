# CVF Work Order: W2 Memory Event Hooks And Context Packager

Memory class: FULL_RECORD

Status: AUTHORIZED

docType: work_order

Date: 2026-05-24

Tranche: W2

Roadmap: `docs/roadmaps/CVF_WC_WORKFLOW_CHAIN_AND_PAIN_POINT_ROADMAP_2026-05-24.md`

GC-018: `docs/baselines/CVF_GC018_W2_MEMORY_EVENT_HOOKS_CONTEXT_PACKAGER_2026-05-24.md`

---

## Purpose

Close WC-3 Candidate 2 with a bounded Learning Plane proof: CVF should classify
memory event hooks and package memory context evidence in a way that is
traceable, summary-only, and incapable of raw prompt reinjection.

## Agent Roles

| Role | Responsibility |
| --- | --- |
| Orchestrator | Keep W2 scoped to LPF helper contracts and commit separately. |
| Legacy Source Extractor | Pull only agentmemory/tolaria/Workflow GoClaw patterns that fit existing CVF owner surfaces. |
| Implementer | Add memory event-hook evaluator and context-package evidence metadata. |
| QA | Run focused LPF tests, LPF check, and docs/session guards. |
| Skeptic/Auditor | Reject route/provider/receipt-envelope and `canReinject=true` expansion. |
| Safety/Boundary Owner | Confirm capture is observation and packaged context is not authority. |

## Authority Chain

- Operator instruction: continue through the roadmap in priority order and
  commit after each part.
- W1 closure:
  `docs/reviews/CVF_W1_WORKFLOW_STATE_MACHINE_ENFORCEMENT_COMPLETION_2026-05-24.md`
- WC roadmap:
  `docs/roadmaps/CVF_WC_WORKFLOW_CHAIN_AND_PAIN_POINT_ROADMAP_2026-05-24.md`
- WC-3 map:
  `docs/reference/CVF_LEGACY_HARVEST_SCAN_MAP_2026-05-24.md`
- WC-4 standard:
  `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- GC-018:
  `docs/baselines/CVF_GC018_W2_MEMORY_EVENT_HOOKS_CONTEXT_PACKAGER_2026-05-24.md`

## Scope / Target / Owner Boundary

Allowed files:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-event-hooks.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/aif-operational-context-preview.ts`
  only if compatibility typing requires it
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/index.ts`
- focused LPF tests
- W2 baseline, work order, completion review
- WC roadmap/session/handoff progress updates

Forbidden files/classes:

- `/api/execute` route and provider adapters;
- `GovernanceEvidenceReceipt` envelope types;
- auth/RBAC;
- durable/cloud memory persistence;
- public-sync;
- MCP/tool runtime hooks;
- raw prompt reinjection or `canReinject=true`.

## Required First Reads

- `docs/reference/CVF_LEGACY_HARVEST_SCAN_MAP_2026-05-24.md`
- `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- `docs/baselines/CVF_GC018_W2_MEMORY_EVENT_HOOKS_CONTEXT_PACKAGER_2026-05-24.md`
- `.private_reference/legacy/CVF 16.5/agentmemory/Thong_tin.md`
- `.private_reference/legacy/CVF 16.5/agentmemory/CVF_MEMORY_CAPTURE_ADAPTER.md`
- `.private_reference/legacy/CVF 16.5/agentmemory/CVF_MEMORY_REINJECTION_PROTOCOL.md`
- `.private_reference/legacy/CVF ADD/REVIEW FOLDER/CVF_ADD_OWNER_SURFACE_PROMOTION_MAP_2026-05-06.md`
- `.private_reference/legacy/CVF ADD/REVIEW FOLDER/CVF_ADD_GOVERNED_CONTEXT_PROFILE_OVERLAP_AUDIT_2026-05-07.md`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts`

## Pre-Flight Checks

- Confirm W1 is closed pass bounded.
- Confirm W2 GC-018 includes the Knowledge Absorption Blind-Spot Control Block.
- Confirm implementation stays in LPF helper contracts.
- Confirm no live route claim is made from local helper tests.
- Confirm any failed live/API proof, if later added, follows the V3 live-run
  diagnostic standard before rerun.

## Write Ownership

Implementation ownership:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-event-hooks.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/index.ts`
- focused LPF tests

Documentation ownership:

- W2 GC-018, work order, completion review
- WC roadmap status update
- active session state, front door, and handoff sync

## Knowledge Absorption Blind-Spot Control Block

- Standard read:
  `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- Source inventory:
  - `.private_reference/legacy/CVF 16.5/agentmemory/`
  - `.private_reference/legacy/CVF ADD/Workflow GoClaw/`
  - `.private_reference/legacy/CVF ADD/Agent Harnesses/`
  - `.private_reference/legacy/CVF ADD/REVIEW FOLDER/`
  - active LPF memory/context files
- Prior absorption evidence resolved:
  - WC-3 map
  - legacy spec absorption registry and Codex review
  - AIF-C memory gateway closure
  - O1 operational context preview closure
  - R2 durable memory route wiring closure
- Detailed source files used:
  - source files listed in Required First Reads
- Source families skipped:
  - tool/MCP/database, provider, benchmark, and public artifact families.
- File-level accepted value:
  - approved events only;
  - no raw secrets;
  - audit receipt required;
  - packaged summary-only context;
  - memory provides context, not authority.
- Owner-surface normalization:
  - LPF memory hook evaluator and LPF context packager metadata.
- Accept/defer/reject matrix:
  - ACCEPT_NOW: hook classification, receipt metadata, package evidence.
  - DEFER_DEMAND_GATED: route integration, UI display, durable promotion,
    MCP/tool hooks.
  - REJECT_DIRECT: AgentMemory server, raw memory dump, autonomous semantic
    promotion, `canReinject=true`.
- Adversarial roles completed:
  - Implementer: narrow LPF helper proof.
  - Skeptic/Auditor: no live route/provider claim.
  - Product/Operator Advocate: reduces unclear memory capture/read packaging.
  - Safety/Boundary Owner: context does not become authority.
- Thin proof target:
  - tests prove approved/denied/privacy-filtered events and package evidence
    with `canReinject=false`.
- Blind-spot verdict: CLEAR

## Execution Plan

1. Add `memory-event-hooks.ts` with approved event taxonomy and evaluator.
2. Add tests for approved, privacy-filtered, denied, and missing-field events.
3. Harden `memory-context-packager.ts` with package evidence metadata.
4. Keep the existing context block text backward-compatible.
5. Export new types/helpers through LPF `index.ts`.
6. Run focused tests and LPF check.
7. File completion review and update roadmap/session/handoff.
8. Commit W2 closure.

## Acceptance Criteria

- [ ] Approved event hook returns an `allow_capture` or `allow_context_read`
      decision with receipt metadata.
- [ ] Disallowed direct/private capture classes are denied.
- [ ] Sensitive events require privacy filtering.
- [ ] Context package evidence records source ids, inclusion/exclusion counts,
      token budget, `rawMemoryReleased=false`, and `canReinject=false`.
- [ ] Existing AIF operational context preview remains compatible.
- [ ] Focused tests PASS.
- [ ] LPF TypeScript check PASS.
- [ ] Completion review, roadmap, session state, and handoff are updated.

## Evidence Requirements

- Focused LPF tests PASS.
- LPF TypeScript check PASS.
- Markdown/docs/session guards PASS.
- Completion review records claim boundary and public catalog N/A unless a
  public-safe capability claim is explicitly added.

## Review Gate

Reject W2 pass if:

- any output exposes raw memory;
- `canReinject` can be true in W2 package evidence;
- a disallowed event is allowed;
- implementation changes `/api/execute`, providers, auth/RBAC, or receipt
  envelope types;
- completion claims live memory route behavior without live proof.

## Closure Checklist

- [ ] GC-018 and work order committed before runtime implementation.
- [ ] Memory event hook evaluator implemented.
- [ ] Context package evidence metadata implemented.
- [ ] Focused LPF tests PASS.
- [ ] LPF TypeScript check PASS.
- [ ] Markdown/docs/session guards PASS.
- [ ] Completion review filed.
- [ ] WC roadmap/session/handoff updated.
- [ ] Final tranche commit created.

## Return Conditions

Return to orchestrator instead of closing if:

- the useful Candidate 2 value requires route integration or provider behavior;
- context packager changes require changing the governance evidence receipt
  envelope;
- preserving `canReinject=false` blocks the desired implementation;
- the implementation would create an AgentMemory-like parallel runtime.

## Operator Checkpoint

No additional operator checkpoint is required for local LPF helper-contract
W2. A new checkpoint is required before route integration, MCP/tool hooks,
public-sync, hosted/cloud persistence, production claims, or any
`canReinject=true` behavior.

## Claim Boundary

This work order authorizes only local memory event hook classification and
summary-only context-package evidence hardening. It does not authorize raw
memory reinjection, autonomous memory reuse, provider/runtime changes,
public capability claims, production readiness, or freeze release.
