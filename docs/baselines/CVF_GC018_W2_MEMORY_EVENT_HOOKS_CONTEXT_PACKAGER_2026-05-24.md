# GC-018: W2 Memory Event Hooks And Context Packager Hardening

Memory class: FULL_RECORD

Status: AUTHORIZED

docType: baseline

Date: 2026-05-24

Roadmap: `docs/roadmaps/CVF_WC_WORKFLOW_CHAIN_AND_PAIN_POINT_ROADMAP_2026-05-24.md`

Work Order: `docs/work_orders/CVF_WO_W2_MEMORY_EVENT_HOOKS_CONTEXT_PACKAGER_2026-05-24.md`

---

## Purpose

Authorize WC-3 Candidate 2 as W2: add bounded memory event-hook evaluation and
context-packager hardening so CVF can classify memory capture/read context
events and package summary-only memory evidence without opening raw
reinjection.

## Scope / Target / Owner Boundary

In scope:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-event-hooks.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts`
- focused LPF tests for memory hooks and context packaging
- LPF index export
- W2 completion review, WC roadmap, session state, and handoff updates

Out of scope:

- `/api/execute` route changes;
- provider behavior, model routing, or live provider semantics;
- governance evidence receipt envelope changes;
- durable/cloud memory persistence;
- raw memory prompt injection;
- `canReinject=true`;
- autonomous memory promotion;
- MCP/tool memory bypass;
- public-sync or production-readiness claims.

Owner surface: Learning Plane Foundation memory/context contract helpers only.

## Depth Audit

Depth score: 8/10.

Rationale:

- WC-3 ranks memory event hooks and context packaging as Candidate 2 because
  they turn WC-1 from a manual proof into a repeatable governed loop pattern.
- Existing LPF already has `controlled-memory-gateway.ts`,
  `memory-context-packager.ts`, retrieval/lifecycle helpers, and AIF preview
  packaging, so W2 can harden owner surfaces instead of inventing a new memory
  runtime.
- The highest risk is accidentally widening "reinjection" into raw prompt
  authority. W2 therefore restricts proof to summary-only packaging and hook
  receipts with `canReinject=false`.

## Source / Predecessor Evidence

- WC roadmap:
  `docs/roadmaps/CVF_WC_WORKFLOW_CHAIN_AND_PAIN_POINT_ROADMAP_2026-05-24.md`
- WC-3 map:
  `docs/reference/CVF_LEGACY_HARVEST_SCAN_MAP_2026-05-24.md`
- WC-4 blind-spot standard:
  `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- W1 completion:
  `docs/reviews/CVF_W1_WORKFLOW_STATE_MACHINE_ENFORCEMENT_COMPLETION_2026-05-24.md`
- Existing LPF memory surfaces:
  `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts`
  and
  `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts`

## Decision / Baseline / Proposed Tranche

Decision: continue with W2 as the second W-series implementation tranche.

Baseline: memory read/write and context packaging exist, but memory-event hook
classification is not first-class and context packages do not yet carry a
compact, machine-readable packaging receipt that makes inclusion/exclusion,
token budget, and `canReinject=false` explicit.

Proposed tranche:

- add a deterministic memory event-hook evaluator;
- allow only approved capture/read/context event types;
- privacy-filter or deny risky events before storage/reuse;
- harden context package metadata so evidence readers can see source ids,
  included/excluded counts, token budget posture, and `canReinject=false`;
- keep raw memory release false.

## Knowledge Absorption Blind-Spot Control Block

- Standard read:
  `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- Source inventory:
  - `.private_reference/legacy/CVF 16.5/agentmemory/` — 11 files
  - `.private_reference/legacy/CVF ADD/Workflow GoClaw/` — context profile family
  - `.private_reference/legacy/CVF ADD/Agent Harnesses/` — context and memory handoff family
  - `.private_reference/legacy/CVF ADD/REVIEW FOLDER/` — owner-surface and context-overlap review files
  - active LPF files under `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/`
- Prior absorption evidence resolved:
  - `docs/reference/CVF_LEGACY_HARVEST_SCAN_MAP_2026-05-24.md`
  - `docs/reference/archive/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md`
  - `docs/reviews/archive/CVF_LEGACY_SPEC_ABSORPTION_BLINDSPOT_CODEX_REVIEW_2026-05-23.md`
  - `docs/reviews/CVF_AIF_C_MEMORY_GATEWAY_PHASE2_COMPLETION_2026-05-24.md`
  - `docs/reviews/CVF_O1_AIF_OPERATIONAL_CONTEXT_PREVIEW_COMPLETION_2026-05-24.md`
  - `docs/reviews/CVF_R2_EXECUTE_ROUTE_DURABLE_MEMORY_WIRING_COMPLETION_2026-05-24.md`
- Detailed source files used:
  - `.private_reference/legacy/CVF 16.5/agentmemory/Thong_tin.md`
  - `.private_reference/legacy/CVF 16.5/agentmemory/CVF_MEMORY_CAPTURE_ADAPTER.md`
  - `.private_reference/legacy/CVF 16.5/agentmemory/CVF_MEMORY_REINJECTION_PROTOCOL.md`
  - `.private_reference/legacy/CVF ADD/REVIEW FOLDER/CVF_ADD_OWNER_SURFACE_PROMOTION_MAP_2026-05-06.md`
  - `.private_reference/legacy/CVF ADD/REVIEW FOLDER/CVF_ADD_GOVERNED_CONTEXT_PROFILE_OVERLAP_AUDIT_2026-05-07.md`
  - `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts`
  - `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts`
- Source families skipped:
  - tool/MCP/database action families: Candidate 3.
  - operational benchmark scorecard: Candidate 4.
  - provider method normalization: Candidate 5.
- File-level accepted value:
  - `CVF_MEMORY_CAPTURE_ADAPTER.md`: approved events only, no raw secrets,
    audit receipt required, capture is observation not permission.
  - `CVF_MEMORY_REINJECTION_PROTOCOL.md`: if memory is reintroduced, it must be
    summary-only/citation-backed, packaged, filtered, token-budgeted, and
    receive context not authority.
  - `CVF_ADD_OWNER_SURFACE_PROMOTION_MAP_2026-05-06.md`: context builder and
    packager are the owner surface; do not create a new prompt-mode subsystem.
  - existing LPF files: keep `rawMemoryReleased=false` and `canReinject=false`
    as hard output evidence for this tranche.
- Owner-surface normalization:
  - event hook evaluation -> new LPF `memory-event-hooks.ts`;
  - context package receipt -> `memory-context-packager.ts`;
  - export surface -> LPF `index.ts`;
  - proof -> focused LPF tests and completion review.
- Accept/defer/reject matrix:
  - ACCEPT_NOW: deterministic hook classification and summary-only package
    receipt metadata.
  - ACCEPT_NOW: explicit denial for direct terminal/clipboard/browser/private
    reasoning capture classes.
  - DEFER_DEMAND_GATED: route integration, UI readout, durable promotion,
    memory write automation, MCP/tool hooks.
  - REJECT_DIRECT: raw prompt memory reinjection, separate AgentMemory server,
    autonomous semantic promotion, and `canReinject=true`.
- Adversarial roles completed:
  - Implementer: LPF helper contracts and tests are enough for a bounded proof.
  - Skeptic/Auditor: no live route/provider claim should be made from local
    helper tests.
  - Product/Operator Advocate: this reduces future "we do not know what was
    captured/read/packaged" failures.
  - Safety/Boundary Owner: capture is observation only; context is evidence,
    not authority.
- Thin proof target:
  - approved hook event returns a capture/read receipt with raw memory false;
    disallowed hook is denied; context package receipt reports budget and
    inclusion/exclusion while preserving `canReinject=false`.
- Blind-spot verdict: CLEAR

## Authorized Change

Implement W2 as a bounded LPF contract hardening:

- create deterministic memory event hook types and evaluator;
- classify approved, privacy-filtered, and denied hook events;
- attach a secret-safe hook receipt;
- extend context packages with machine-readable packaging evidence;
- preserve summary-only packaging, `rawMemoryReleased=false`, and
  `canReinject=false`.

## Evidence Plan

- `npm test -- --run tests/memory-event-hooks.test.ts tests/memory-context-packager.test.ts tests/aif-operational-context-preview.test.ts`
- `npm run check` in `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION`
- markdown/session governance guards
- release gate if W2 touches live governance route behavior; otherwise N/A
  with explicit local-contract boundary

## Acceptance Criteria

- [ ] Approved memory events produce a secret-safe hook receipt.
- [ ] Disallowed direct/private capture events are denied.
- [ ] Sensitive events require privacy filtering.
- [ ] Context package evidence includes included/excluded counts, source ids,
      token budget, `rawMemoryReleased=false`, and `canReinject=false`.
- [ ] Existing AIF operational context preview remains compatible.
- [ ] Focused LPF tests PASS.
- [ ] LPF TypeScript check PASS.
- [ ] Completion review filed and session/handoff updated.

## Claim Boundary

W2 may claim only local Learning Plane memory event-hook classification and
summary-only context-package evidence hardening. It does not claim live route
integration, raw reinjection, autonomous memory reuse, hosted/cloud memory,
provider behavior, MCP/tool hooks, public capability graduation, production
readiness, or freeze release.
