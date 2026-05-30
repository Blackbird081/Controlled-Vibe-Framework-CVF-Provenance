# CVF GC-018 C7C External Skill Candidate Record Validator

Memory class: SUMMARY_RECORD

Status: AUTHORIZED_C7C_EXTERNAL_SKILL_CANDIDATE_RECORD_VALIDATOR

docType: gc018_baseline

Date: 2026-05-25

---

## Purpose

Authorize C7C as a deterministic local validator/readout for one external
skill candidate screening record. C7C turns the ES1/C7B rules into a small
machine-checkable contract before any external skill can be imported,
published, or executed.

## Scope / Target / Owner Boundary

Allowed owner files:

- `governance/contracts/external-skill-candidate-screen.ts`
- `governance/contracts/external-skill-candidate-screen.test.ts`
- C7C completion/session/handoff files

Forbidden:

- parsing remote skill contents or fetching external repositories;
- importing external skills or modifying certified product packs;
- registry publication, marketplace/public-sync claims, or UI work;
- runtime adapters or external tool/MCP/CLI/script/model/provider/browser/
  database execution;
- `/api/execute`, receipt envelopes, auth/RBAC, hosted readiness, production
  readiness, or freeze release.

## Source / Predecessor Evidence

Predecessors:

- `docs/reference/CVF_EXTERNAL_SKILL_INTAKE_SCREENING_PACKET_2026-05-25.md`
- `docs/reference/CVF_CANDIDATE7_EXTERNAL_SKILL_SOURCE_SCREENING_MATRIX_2026-05-25.md`
- `docs/reviews/CVF_C7B_CANDIDATE7_EXTERNAL_SKILL_SOURCE_SCREENING_MATRIX_COMPLETION_2026-05-25.md`
- `docs/reviews/CVF_TA1_TOOL_ACTION_APPROVAL_READOUT_COMPLETION_2026-05-25.md`

## Knowledge Absorption Blind-Spot Control Block

- Standard read:
  `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- Source inventory:
  - ES1 screening packet;
  - C7B source-family matrix;
  - governance/contracts TA1 pattern.
- Prior absorption evidence resolved:
  - ES1 defines required record fields and stop conditions.
  - C7B adds source family, duplicate target pack, dilution risk, and registry
    readiness fields.
  - TA1 proves local deterministic readout style with no runtime execution.
- Detailed source files used:
  - `docs/reference/CVF_EXTERNAL_SKILL_INTAKE_SCREENING_PACKET_2026-05-25.md`
  - `docs/reference/CVF_CANDIDATE7_EXTERNAL_SKILL_SOURCE_SCREENING_MATRIX_2026-05-25.md`
  - `governance/contracts/tool-action-taxonomy.ts`
- Source families skipped:
  - concrete external skill contents and live repositories; not needed for a
    local record validator.
- File-level accepted value:
  - ES1 -> required screening fields, value/duplicate/risk/owner checks.
  - C7B -> dilution and registry-readiness posture.
  - TA1 -> readout-only contract shape.
- Owner-surface normalization:
  - implement as `governance/contracts` local contract and tests.
- Accept/defer/reject matrix:
  - accept record validation and deterministic readout.
  - defer YAML/CLI parser, registry publication, candidate import, runtime
    adapters, and live proof.
  - reject any validator output that grants execution authority.
- Adversarial roles completed:
  - Implementer: smallest proof is a pure TypeScript evaluator plus tests.
  - Skeptic/Auditor: validator must not become registry admission.
  - Product/Operator Advocate: clear readout prevents wasted time/token on
    low-value or unsafe skill candidates.
  - Safety/Boundary Owner: `runtimeExecutionAuthorized=false` must be
    invariant.
- Thin proof target:
  - one local contract module with focused tests.
- Blind-spot verdict: CLEAR

## Decision / Baseline / Proposed Tranche

Decision: AUTHORIZE_C7C_EXTERNAL_SKILL_CANDIDATE_RECORD_VALIDATOR.

Baseline:

- C7B concluded the highest-value next move is an enforceable screening record,
  not more skills.
- Governance contracts already host deterministic local action/readout
  contracts.

Proposed tranche:

- add a local evaluator for `external_skill_screen` records;
- report missing fields, value/duplicate/risk/owner outcomes, disposition, next
  safe action, and boundaries;
- preserve no execution/import/registry authority.

## Acceptance Criteria

- evaluator requires ES1 minimum fields;
- evaluator recognizes C7B source-family and dilution/readiness fields;
- high-risk runtime/import/provider/tool/database/browser cases are blocked or
  deferred;
- direct bulk import and unknown side effects are rejected;
- tests prove pass, incomplete, duplicate, runtime-gated, and direct-import
  cases;
- no runtime execution authority is exported.

## Verification Plan

```bash
cd governance/contracts
npm test -- external-skill-candidate-screen.test.ts
npm test
python ../../governance/compat/check_active_session_state.py
python ../../governance/compat/check_agent_handoff_guard_compat.py
```

Live proof N/A because C7C is a local deterministic contract only.

## Claim Boundary

C7C may claim only a local candidate-record validator/readout. It must not
claim external skill ingestion, registry admission, runtime execution, live
tool/MCP/database/provider behavior, marketplace readiness, hosted readiness,
production readiness, or freeze release.
