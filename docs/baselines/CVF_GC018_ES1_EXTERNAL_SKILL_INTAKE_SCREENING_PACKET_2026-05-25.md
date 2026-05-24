# CVF GC-018 ES1 External Skill Intake Screening Packet

Memory class: SUMMARY_RECORD

Status: AUTHORIZED_ES1_EXTERNAL_SKILL_INTAKE_SCREENING_PACKET

docType: gc018_baseline

Date: 2026-05-25

---

## Purpose

Authorize ES1 as a docs-only external skill intake screening packet for
Candidate 7. ES1 prevents future agents from importing external skills,
models, tools, or skill folders directly by requiring a value/risk/owner
screen first.

## Scope / Target / Owner Boundary

Allowed owner files:

- `docs/reference/CVF_EXTERNAL_SKILL_INTAKE_SCREENING_PACKET_2026-05-25.md`
- ES1 completion/session/handoff files

Forbidden:

- importing external skills;
- creating or modifying product skill packs;
- executing external tools, MCP servers, CLIs, scripts, models, or providers;
- fetching live external repositories;
- runtime adapters, registry publication, marketplace claims, or public-sync;
- `/api/execute`, receipt envelopes, auth/RBAC, hosted readiness, production
  readiness, or freeze release.

## Source / Predecessor Evidence

Predecessors:

- `docs/reference/CVF_GOVERNED_CAPABILITY_INTAKE_DOCTRINE_2026-05-07.md`
- `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
- `docs/reviews/CVF_C7A_PRODUCT_SKILL_PACK_TOP10_COMPLETION_2026-05-25.md`
- `docs/reviews/CVF_C8_PRODUCT_SKILL_PACK_SELECTION_READOUT_COMPLETION_2026-05-25.md`
- `docs/reviews/CVF_TA1_TOOL_ACTION_APPROVAL_READOUT_COMPLETION_2026-05-25.md`

Detailed source files read:

- `.private_reference/legacy/CVF ADD/Hugging Face/CVF_HF_SKILL_ABSORPTION_SPEC.md`
- `.private_reference/legacy/CVF ADD/Hugging Face/CVF_HF_SKILL_NORMALIZATION_SCHEMA.md`
- `.private_reference/legacy/CVF ADD/Hermes Agent/CVF_HERMES_SKILL_PACKAGE_MODEL.md`
- `.private_reference/legacy/CVF 16.5/Memento-Skills/GOVERNED_SKILL_EVOLUTION_SPEC.md`
- `.private_reference/legacy/CVF ADD/AGENT ENGINEER/CVF_AGENT_ENGINEERING_CONTRACT.md`
- `governance/toolkit/02_POLICY/CVF_MASTER_POLICY.md`

## Knowledge Absorption Blind-Spot Control Block

- Standard applied:
  `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- Prior absorption evidence resolved: LH1 ledger, C7A/C8, W3/TA1, governed
  capability intake doctrine.
- Accepted value:
  - external skills are knowledge/capability candidates, not runtime authority;
  - normalization must re-express external skills in CVF-native terms;
  - provenance, task intent, tools, side effects, risk, policy bindings, and
    trace requirements are mandatory;
  - skill evolution must be proposal/verification/approval first, never
    self-mutation into production;
  - strict schemas and no implicit assumptions are required.
- Deferred value:
  - registry publication;
  - actual import of any external skill;
  - live repository refresh;
  - runtime adapters, MCP/tool execution, model execution, provider calls;
  - UI marketplace or public claim.
- Rejected value:
  - direct import of SKILL.md or external package contents;
  - external skill as CVF law;
  - self-trusting skills because they are popular or useful.
- Owner normalization:
  - reference packet only, under `docs/reference`.
- Adversarial role review:
  - Implementer: a screening packet reduces future intake ambiguity without
    opening runtime.
  - Skeptic/Auditor: screening must not be disguised ingestion.
  - Product/Operator Advocate: value screen must prefer a few high-value
    workflows over many thin skills.
  - Safety/Boundary Owner: no external execution, import, registry publication,
    or public claim is authorized.
- Blind-spot delta: reduced; Candidate 7 gets a concrete pre-import filter.
- Verdict: CLEAR.

## Decision / Baseline / Proposed Tranche

Decision: AUTHORIZE_ES1_EXTERNAL_SKILL_INTAKE_SCREENING_PACKET.

Baseline:

- C7A/C8 closed a practical top-10 static pack inventory and selector.
- Candidate 7 external skill/model ingestion remains demand-gated.
- TA1 closed action approval readout, but runtime execution remains closed.

Proposed tranche:

- create one reference screening packet for future external skill intake;
- include value, risk, owner-surface, duplicate, normalization, and dispatch
  decisions;
- close without importing or executing anything.

## Acceptance Criteria

- packet requires concrete source and non-coder use case;
- packet screens against existing ten certified packs;
- packet distinguishes accept/defer/reject/direct-import prohibition;
- packet includes minimum normalized fields and no-execution boundary;
- packet includes mandatory stop conditions before any future import.

## Verification Plan

Verification is docs/governance only:

```bash
python governance/compat/check_active_session_state.py
python governance/compat/check_agent_handoff_guard_compat.py
```

Live proof N/A because ES1 is a reference screening packet only.

## Claim Boundary

ES1 may claim only a docs-only screening packet for future external skill
intake. It must not claim external skill ingestion, registry publication,
runtime execution, live provider behavior, public marketplace readiness, hosted
readiness, production readiness, or freeze release.
