# CVF PD-2 External Capability Admission Contract — Completion Review

Memory class: FULL_RECORD

Status: CLOSED_PASS

docType: completion_review

Date: 2026-05-29

---

## Purpose

Completion review for PD-2 External Capability Admission Contract (Phase A).
Verifies that the contract extends ES1 screening scope to MCP servers, CLI
tools, external repositories, and database sources with type-specific
admission gates.

This closes CVF 25.05 Gap 6: ES1/C7B/C7C covered skill-only admission;
MCP, tool, repo, and database admission were undefined.

## Artifacts Delivered

| Artifact | Path | Status |
| --- | --- | --- |
| Admission contract | `docs/contracts/CVF_EXTERNAL_CAPABILITY_ADMISSION_CONTRACT.md` (new) | CLOSED_PASS |

## Acceptance Criteria Verification

- [x] Contract defines admission gates for 5 source types:
  - External skill pack → ES1 + C7B/C7C (already exists)
  - MCP server → New: MCP admission gate (S3)
  - CLI tool → LHW6-T2 governed (S4)
  - External repo → New: Repo admission gate (S5)
  - Database source → LHW5-T1 governed (S6)
- [x] Each gate defines blocked scenarios
- [x] Each gate defines admission flow
- [x] External capability inventory fields defined (S7)
- [x] Phase B explicitly deferred with per-type requirements
- [x] Risk classification per source type
- [x] Existing surface references verified:
  - ES1 + C7B/C7C — skill packs
  - LHW9-T1 `mcpApprovalAdvisoryType` — MCP
  - LHW6-T2 `cliToolOnboardingGovernanceConnector` — CLI
  - LHW5-T1 `databaseActionBoundaryConnector` — database
- [x] No runtime enforcement claimed

## Changed Files

```
A  docs/contracts/CVF_EXTERNAL_CAPABILITY_ADMISSION_CONTRACT.md
```

## Governance Gate Status

- Pre-dispatch authority: PD GC-018 ACTIVE
- All source paths verified
- No cvf-web UI changes
- No runtime enforcement
- No public-sync changes

## CVF 25.05 Gap 6 Status

CLOSED_PASS at Phase A. Gap 6 required admission contract extension for MCP
and repo scope — delivered. Phase B (runtime enforcement) is product depth
beyond gap closure.

## Source Coverage Summary

| Source type | Governing contract | Risk class | Admission decision |
| --- | --- | --- | --- |
| External skill pack | ES1 + C7B/C7C | R1 | Operational |
| MCP server | This contract S3 | R2 | Doc-only gate |
| CLI tool | LHW6-T2 | R1 | Operational |
| External repo | This contract S5 | R2 | Doc-only (read-only only) |
| Database source | LHW5-T1 | R2 | Operational (read-only only) |

## Fail Conditions

| Condition | Result |
| --- | --- |
| Missing MCP admission gate | PASS — S3 defines 5-step gate |
| Missing repo admission gate | PASS — S5 defines 5-step gate |
| Missing blocked scenarios | PASS — each gate lists blocked scenarios |
| Missing capability inventory fields | PASS — S7 defines 11 fields |
| LHW9-T1 prerequisite | PASS — CLOSED_PASS_BOUNDED |

## Claim Boundary

PD-2 Phase A delivers a governance contract extension. It does not claim:
runtime enforcement, MCP server execution, tool execution, repo scanning,
database access, live admission workflow, provider behavior changes, hosted
readiness, production readiness, or public release readiness.
