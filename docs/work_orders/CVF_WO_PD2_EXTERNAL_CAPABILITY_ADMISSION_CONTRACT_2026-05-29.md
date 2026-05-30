# CVF Work Order — PD-2 External Capability Admission Contract Expansion

Memory class: FULL_RECORD

Status: READY_FOR_IMPLEMENTATION

docType: work_order

Date: 2026-05-29

---

## Purpose

Create `docs/contracts/CVF_EXTERNAL_CAPABILITY_ADMISSION_CONTRACT.md` —
extending ES1/C7B/C7C (skill-only) to define admission gates for MCP server,
tool, and repo source types. Closes CVF 25.05 Gap 6 at Phase A.

Gap 6: ES1 defines skill admission. MCP server, CLI tool, external repo, and
database source admission remain undefined — not allowed, not forbidden, not
governed. Phase A closes this with a documentation contract.

This is documentation only. No runtime enforcement. Phase B (runtime wiring)
requires a separate GC-018.

## Authority Chain

- PD GC-018: `docs/baselines/CVF_GC018_PRODUCT_DEPTH_2026-05-29.md`
- PD Roadmap: `docs/roadmaps/CVF_PRODUCT_DEPTH_ROADMAP_2026-05-29.md`
- ES1: `docs/reference/archive/CVF_EXTERNAL_SKILL_INTAKE_SCREENING_PACKET_2026-05-25.md`
- C7C validator: `governance/contracts/external-skill-candidate-screen.ts`
  — `ExternalSkillCandidateScreenRecord`; `ExternalSkillCandidateScreenReadout`
    literal false fields
- LHW9-T1 MCP approval: `docs/reference/CVF_LHW9_T1_MCP_TOOL_APPROVAL_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
- LHW6-T2 CLI onboarding: `docs/reference/CVF_LHW6_CLI_TOOL_ONBOARDING_GOVERNANCE_CONNECTOR_SPEC_2026-05-28.md`

## Agent Roles

Implementer writes admission contract for 4 source types. Reviewer checks:
each source type has intake/provenance/risk/boundary sections; ES1 is cited as
precedent; `externalFetchAuthorized=false` and `runtimeExecutionAuthorized=false`
explicit for all types. No self-review.

## Scope

**Allowed:**

- `docs/contracts/CVF_EXTERNAL_CAPABILITY_ADMISSION_CONTRACT.md` (new — create
  `docs/contracts/` directory if needed)
- `docs/reviews/CVF_PD2_EXTERNAL_CAPABILITY_ADMISSION_CONTRACT_COMPLETION_2026-05-29.md` (new)
- this work order (status update only)
- session continuity files

**Forbidden:** Any `EXTENSIONS/` source change, `governance/contracts/` runtime
file change, receipt envelope schema, MCP execution, public-sync repo.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `docs/reference/archive/CVF_EXTERNAL_SKILL_INTAKE_SCREENING_PACKET_2026-05-25.md`
   — ES1 template: intake metadata, source check, risk classification, capability
   boundary, allowed roles, sandbox requirement, evidence requirement
4. `governance/contracts/external-skill-candidate-screen.ts`
   — confirm `ExternalSkillCandidateScreenRecord`; confirm
   `ExternalSkillCandidateScreenReadout.runtimeExecutionAuthorized`,
   `registryPublicationAuthorized`, and `externalFetchAuthorized` literal
   false fields
5. `docs/reference/CVF_LHW9_T1_MCP_TOOL_APPROVAL_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
   — MCP boundary pattern: approval advisory, `runtimeExecutionAuthorized=false`
6. `docs/reference/CVF_LHW6_CLI_TOOL_ONBOARDING_GOVERNANCE_CONNECTOR_SPEC_2026-05-28.md`
   — CLI tool onboarding classification pattern

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| ES1 admission template | `docs/reference/archive/CVF_EXTERNAL_SKILL_INTAKE_SCREENING_PACKET_2026-05-25.md` | full document | intake screening template | ES1 | ACCEPT |
| `ExternalSkillCandidateScreenRecord` | `governance/contracts/external-skill-candidate-screen.ts` | interface definition | `ExternalSkillCandidateScreenRecord` | C7C contract | ACCEPT |
| LITERAL_INVARIANT: `externalFetchAuthorized=false` | `governance/contracts/external-skill-candidate-screen.ts` | `ExternalSkillCandidateScreenReadout` field | `externalFetchAuthorized` | `ExternalSkillCandidateScreenReadout` | ACCEPT |
| LITERAL_INVARIANT: `runtimeExecutionAuthorized=false` | `governance/contracts/external-skill-candidate-screen.ts` | `ExternalSkillCandidateScreenReadout` field | `runtimeExecutionAuthorized` | `ExternalSkillCandidateScreenReadout` | ACCEPT |
| MCP approval boundary pattern | `docs/reference/CVF_LHW9_T1_MCP_TOOL_APPROVAL_ADVISORY_CONNECTOR_SPEC_2026-05-28.md` | S4 boundary table | MCP execution not authorized | LHW9-T1 | ACCEPT |
| CLI onboarding classification | `docs/reference/CVF_LHW6_CLI_TOOL_ONBOARDING_GOVERNANCE_CONNECTOR_SPEC_2026-05-28.md` | S2 mapping | `onboardingClassification` values | LHW6-T2 | ACCEPT |
| PD GC-018 authorization | `docs/baselines/CVF_GC018_PRODUCT_DEPTH_2026-05-29.md` | full document | PD-2 authorization | PD GC-018 | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| Admission gates for MCP, tool, repo, database | Deliverable | contract doc | All 4 source types covered | OPEN |
| ES1 cited as precedent | Deliverable | contract doc | ES1 path in Authority Chain | OPEN |
| `externalFetchAuthorized=false` for all types | Deliverable | contract doc | Invariant explicit | OPEN |
| Phase B explicitly deferred | Deliverable | claim boundary | Runtime enforcement not claimed | OPEN |
| No EXTENSIONS/ source change | Scope Forbidden | git diff | `git diff --name-only` | OPEN |

## Deliverable — Contract Doc

File: `docs/contracts/CVF_EXTERNAL_CAPABILITY_ADMISSION_CONTRACT.md`

The contract must define admission gates for 4 source types, each modeled on
ES1 but with source-type-specific boundaries:

**MCP Server:**
- Intake: server origin URL, tool list, scope declaration
- Provenance: operator-supplied or registry-listed only
- Risk: R2 — server may execute code on behalf of CVF
- Boundary: `runtimeExecutionAuthorized=false` until Phase B wiring
- Allowed roles: Orchestrator advisory only; no auto-install
- Sandbox: required before any tool execution
- Evidence: LHW9-T1 approval advisory record per tool call

**CLI Tool:**
- Intake: tool name, version, install source
- Provenance: follow LHW6-T2 onboarding classification
- Risk: R1–R2 per LHW6-T2 `onboardingClassification`
- Boundary: `runtimeExecutionAuthorized=false` until Phase B
- Reference: LHW6-T2 `onboardingClassification` values already defined

**External Repo:**
- Intake: repo URL, license, dependency manifest
- Provenance: public repo with verifiable license
- Risk: R2 — repo may contain executable code
- Boundary: read-only reference only; no import or execution
- Evidence: provenance check record + license scan result

**Database Source:**
- Intake: connection type, read/write scope, owner
- Provenance: operator-owned or explicitly authorized
- Risk: R2 read-only / R3 write
- Boundary: W3/LHW5-T1 taxonomy applies; mutation remains blocked per LHW5-T1
- Evidence: LHW5-T1 `databaseActionBoundaryAdvisoryType` record

All source types: `externalFetchAuthorized=false`; `runtimeExecutionAuthorized=false`;
Phase B required for any execution.

## Pre-Flight

- [ ] Working tree clean
- [ ] All required first reads done
- [ ] Gate confirmations checked

## Write Ownership

Implementer owns all new files. No file outside the Allowed list may be modified.

## Return-To-Orchestrator Conditions

Stop if: required gate evidence missing; a cited source file cannot be found; implementing the deliverable requires a forbidden file change.

## Execution Plan

1. Read all required first reads.
2. Write contract with 4 source type sections.
3. Write completion review with Gap 6 overall closure note.
4. Run governance gates.
5. Update session continuity.
6. Commit.

## Evidence Requirements

- Contract with 4 source type sections
- ES1 cited as skill-type precedent
- `externalFetchAuthorized=false` explicit for all types
- Phase B deferred
- No EXTENSIONS/ source changed

## Acceptance Criteria

- [ ] `docs/contracts/CVF_EXTERNAL_CAPABILITY_ADMISSION_CONTRACT.md` created
- [ ] All 4 source types (MCP, CLI tool, repo, database) covered
- [ ] ES1 cited as precedent for skill type
- [ ] `externalFetchAuthorized=false` explicit for all types
- [ ] Phase B deferred explicitly
- [ ] No code file in diff
- [ ] Session continuity updated

## Review Gate

All 4 types covered; ES1 cited; `externalFetchAuthorized=false`; Phase B
deferred; no code file.

## Closure Checklist

- [ ] Contract created with 4 source types
- [ ] `externalFetchAuthorized=false` for all types
- [ ] Completion review with Gap 6 overall closure note
- [ ] Governance gates PASS
- [ ] Session continuity updated

## Operator Checkpoint

operator.checkpoint.waiver: Documentation-only; no MCP execution; no runtime
change; R0 risk.

## Claim Boundary

PD-2 Phase A produces a documentation contract only. It does not claim MCP
execution, external repo import, database write access, runtime enforcement
of admission gates, hosted readiness, production readiness, or public release
readiness.
