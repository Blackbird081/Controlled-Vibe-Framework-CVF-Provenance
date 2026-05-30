# CVF GC-018 C7B Candidate 7 External Skill Source Screening Matrix

Memory class: SUMMARY_RECORD

Status: AUTHORIZED_C7B_CANDIDATE7_EXTERNAL_SKILL_SOURCE_SCREENING_MATRIX

docType: gc018_baseline

Date: 2026-05-25

---

## Purpose

Authorize C7B as a docs-only Candidate 7 source-family screening matrix. C7B
will audit the highest-value local legacy external-skill families and decide
which concepts may be accepted as CVF patterns, merged into existing owner
surfaces, deferred for later runtime gates, or rejected.

## Scope / Target / Owner Boundary

Allowed owner files:

- `docs/reference/CVF_CANDIDATE7_EXTERNAL_SKILL_SOURCE_SCREENING_MATRIX_2026-05-25.md`
- C7B completion/session/handoff files

Forbidden:

- importing external skills or copying external skill packages into CVF;
- creating or modifying certified product skill packs;
- creating runtime adapters, registry entries, marketplace entries, or public
  claims;
- executing external tools, MCP servers, CLIs, scripts, models, providers,
  browsers, or databases;
- fetching live external repositories;
- touching `/api/execute`, receipt envelopes, auth/RBAC, hosted readiness,
  production readiness, public-sync, or freeze release.

## Source / Predecessor Evidence

Predecessors:

- `docs/reference/CVF_EXTERNAL_SKILL_INTAKE_SCREENING_PACKET_2026-05-25.md`
- `docs/reference/CVF_GOVERNED_CAPABILITY_INTAKE_DOCTRINE_2026-05-07.md`
- `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
- `docs/reviews/CVF_ES1_EXTERNAL_SKILL_INTAKE_SCREENING_PACKET_COMPLETION_2026-05-25.md`
- `docs/reviews/CVF_C7A_PRODUCT_SKILL_PACK_TOP10_COMPLETION_2026-05-25.md`
- `docs/reviews/CVF_C8_PRODUCT_SKILL_PACK_SELECTION_READOUT_COMPLETION_2026-05-25.md`
- `docs/reviews/CVF_TA1_TOOL_ACTION_APPROVAL_READOUT_COMPLETION_2026-05-25.md`

Detailed source files authorized for local read-only audit:

- `.private_reference/legacy/CVF ADD/Hugging Face/CVF_HF_SKILL_ABSORPTION_SPEC.md`
- `.private_reference/legacy/CVF ADD/Hugging Face/CVF_HF_SKILL_NORMALIZATION_SCHEMA.md`
- `.private_reference/legacy/CVF ADD/Hermes Agent/CVF_HERMES_SKILL_PACKAGE_MODEL.md`
- `.private_reference/legacy/CVF 16.5/Memento-Skills/GOVERNED_SKILL_EVOLUTION_SPEC.md`
- `.private_reference/legacy/CVF ADD/AGENT ENGINEER/CVF_AGENT_ENGINEERING_CONTRACT.md`
- local external-source catalogs already present in the repository, if needed,
  as evidence only.

## Knowledge Absorption Blind-Spot Control Block

- Standard read:
  `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- Source inventory:
  - Hugging Face family: local skill absorption/normalization docs
  - Hermes Agent family: local package model docs
  - Memento-Skills family: local governed evolution docs
  - Agent Engineer family: local strict contract docs
  - ES1/C7A/C8/TA1/LH1 packets: prior disposition and owner boundaries
- Prior absorption evidence resolved:
  - ES1 closed the pre-import screening standard.
  - C7A/C8 closed the current ten-pack product inventory and selector.
  - TA1 closed action approval readout while preserving no-execution posture.
  - LH1 kept external skill/model ingestion demand-gated.
- Detailed source files used:
  - `.private_reference/legacy/CVF ADD/Hugging Face/CVF_HF_SKILL_ABSORPTION_SPEC.md`
  - `.private_reference/legacy/CVF ADD/Hugging Face/CVF_HF_SKILL_NORMALIZATION_SCHEMA.md`
  - `.private_reference/legacy/CVF ADD/Hermes Agent/CVF_HERMES_SKILL_PACKAGE_MODEL.md`
  - `.private_reference/legacy/CVF 16.5/Memento-Skills/GOVERNED_SKILL_EVOLUTION_SPEC.md`
  - `.private_reference/legacy/CVF ADD/AGENT ENGINEER/CVF_AGENT_ENGINEERING_CONTRACT.md`
- Source families skipped:
  - live external repositories: skipped because C7B is local/docs-only.
  - concrete third-party skill folders not already present locally: skipped
    until the operator names a candidate source/use case.
- File-level accepted value:
  - Hugging Face -> no direct trust, lifecycle, normalization fields,
    provenance, risk/side-effect/trace requirements.
  - Hermes -> skill package identity, maturity, registry status, enable/disable
    scope, policy binding.
  - Memento -> proposal/verification/approval loop for skill evolution.
  - Agent Engineer -> strict schemas, no implicit assumptions, no unbounded
    outputs.
- Owner-surface normalization:
  - accepted concepts must map to reference docs, certified pack selector,
    governance/contracts, future registry validator, or proposal-only evolution
    lane.
- Accept/defer/reject matrix:
  - accept docs-only patterns that improve screening clarity.
  - defer runtime adapters, live fetch, registry publication, skill mutation,
    MCP/tool/provider execution, and new pack creation.
  - reject direct import, self-trusting external packages, and popularity as
    evidence.
- Adversarial roles completed:
  - Implementer: smallest proof is a source-family matrix over existing local
    evidence.
  - Skeptic/Auditor: the matrix must not become hidden ingestion or registry
    publication.
  - Product/Operator Advocate: value is reducing skill-library dilution while
    preserving reusable high-value patterns.
  - Safety/Boundary Owner: no execution, import, registry publication, public
    claim, or provider call is authorized.
- Thin proof target:
  - one docs/reference matrix with source-family dispositions and next most
    valuable bounded tranches.
- Blind-spot verdict: CLEAR

## Decision / Baseline / Proposed Tranche

Decision: AUTHORIZE_C7B_CANDIDATE7_EXTERNAL_SKILL_SOURCE_SCREENING_MATRIX.

Baseline:

- ES1 gives a required external skill screening packet.
- Candidate 7 still needs source-family ranking so future agents know which
  parts are valuable without importing everything.
- Product value remains: keep a small set of powerful workflows while adding
  enough governed skill intelligence for future LLM/Agent selection.

Proposed tranche:

- audit local Candidate 7 source families at file level;
- record value, risk, owner surface, duplicate/dilution outcome, and
  disposition;
- recommend the next highest-value bounded follow-up without opening runtime.

## Acceptance Criteria

- matrix covers the high-value local Candidate 7 families;
- every source family has accept/defer/reject disposition and reason;
- accepted concepts map to existing CVF owner surfaces;
- runtime/tool/provider/registry/public claims remain explicitly blocked;
- next tranche recommendation prioritizes value over breadth.

## Verification Plan

Verification is docs/governance only:

```bash
python governance/compat/check_active_session_state.py
python governance/compat/check_agent_handoff_guard_compat.py
```

Live proof N/A because C7B is a local documentation/source-screening matrix.

## Claim Boundary

C7B may claim only a docs-only source-family screening matrix for Candidate 7.
It must not claim external skill ingestion, registry admission, runtime
execution, live tool/MCP/database/provider behavior, public marketplace
readiness, hosted readiness, production readiness, or freeze release.
