# CVF Agent Work Order: MEOR-RDA-T3 Cross-Domain Conformance

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-12

Worker: Codex (operator override; originally Claude)

Reviewer: Codex

Commit mode: WORKER_MUST_NOT_COMMIT

Operator override: Codex self-executed the worker role and retained
reviewer-owned closure/commit responsibility on 2026-06-12.

dispatchBaseHead: `ae3f3386`

executionBaseHead: `81db3560`

closureBaseHead: `81db3560`

GC-018:
`docs/baselines/CVF_GC018_MEOR_RDA_T3_CROSS_DOMAIN_CONFORMANCE_2026-06-12.md`

Parent roadmap:
`docs/roadmaps/CVF_MEOR_REGULATED_DOMAIN_ADAPTER_ROADMAP_2026-06-12.md`

## Purpose

Implement focused conformance tests for the MEOR regulated-domain adapter.

The tests must prove that regulated lifecycle requirements remain
profile-scoped and do not bleed into non-regulatory profiles.

## Authority Chain

| Authority | Path | Status |
| --- | --- | --- |
| Operator direction | 2026-06-12 continue with RDA-T3 using RDA-T2 closure commit `1c47d125` and sync commit `ae3f3386` | ACCEPT |
| Post-T2 audit | `docs/audits/CVF_MEOR_RDA_POST_T2_NEXT_TRANCHE_AUDIT_2026-06-12.md` | CLOSED_PASS_BOUNDED |
| Parent roadmap | `docs/roadmaps/CVF_MEOR_REGULATED_DOMAIN_ADAPTER_ROADMAP_2026-06-12.md` | ACTIVE_RDA_T3_DISPATCHED |
| RDA-T2 completion | `docs/reviews/CVF_MEOR_RDA_T2_DETERMINISTIC_ADAPTER_IMPLEMENTATION_COMPLETION_2026-06-12.md` | CLOSED_PASS_BOUNDED |
| RDA-T3 GC-018 | `docs/baselines/CVF_GC018_MEOR_RDA_T3_CROSS_DOMAIN_CONFORMANCE_2026-06-12.md` | AUTHORIZED |
| Operator override | 2026-06-12 instruction for Codex to do the Claude work directly | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order requirement | Output | Verification |
| --- | --- | --- | --- |
| Cross-domain conformance | add focused CPF conformance tests | test file | focused tests |
| Non-regulatory profiles do not inherit regulated fields | company/technical/governance/mixed fixtures | assertions | focused tests |
| Legal-policy support flag is explicit | legal profile without flag rejected | assertions | focused tests |
| Prevent cross-profile bleed | attach regulated requirements to foreign profile | bridge failure | focused tests |
| Keep Policy_Local out of scope | forbid external paths | changed-path proof | git status/diff |

## Intake Role Routing Decision

- Intake summary: prove RDA-T2 adapter isolation using deterministic helper
  closure commit `1c47d125`.
- Scope classification: bounded local deterministic conformance tranche.
- Risk sensitivity: medium, because it exercises regulated-domain foundation
  behavior before downstream use-case work.
- routeMode: `MULTI_AGENT_MULTI_ROLE`;
- reason: Claude implements tests and Codex reviews/commits.
- Escalation condition: stop if conformance cannot be proven without runtime
  source mutation, external Policy_Local data, EC activation, OCR, retrieval,
  provider/API-key use, public-sync, or readiness claim expansion.

## Agent Roles

| Role | Actor | Responsibility |
| --- | --- | --- |
| Worker | Codex | implement allowed CPF conformance tests under operator override |
| Reviewer | Codex | verify scope, run gates, commit if accepted |
| Continuity updater | Codex | update roadmap/state/handoff during reviewer-owned closure sync |

## Worker Autonomy / No-Question Rule

Repair allowed-scope test, formatting, registry, and gate failures without
asking the operator. Escalate only when the repair would exceed Allowed Scope
or touch Forbidden Scope.

## Required First Reads

1. RDA roadmap.
2. RDA-T3 GC-018 baseline.
3. RDA-T2 completion review.
4. RDA-T2 adapter source.
5. CPF context barrel export.
6. DSCP domain profile contract.
7. DSCP metadata requirement bridge.
8. GC-051 corpus scan registry standard and nearby CPF registry entries.

## Source Verification Table

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Fact class | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| RDA-T2 adapter helper exists | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.regulated.domain.adapter.ts` | line 67 | `buildRegulatedDomainMetadataRequirements` | TypeScript function | EXISTS | ACCEPT |
| RDA-T2 mapping table exists | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.regulated.domain.adapter.ts` | line 35 | `REGULATED_DOMAIN_REQUIREMENT_MAPPINGS` | TypeScript constant | EXISTS | ACCEPT |
| RDA-T2 support flag gate exists | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.regulated.domain.adapter.ts` | line 82 | `supportsDocumentStatus` | adapter helper | RUNTIME_BEHAVIOR | ACCEPT |
| RDA-T2 helper is exported through CPF context barrel | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.context.barrel.ts` | lines 94-100 | `buildRegulatedDomainMetadataRequirements` | CPF context barrel | EXISTS | ACCEPT |
| DSCP profile family type exists | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 37 | `DscpDomainProfile` | TypeScript interface | EXISTS | ACCEPT |
| Regulated support flag exists | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 67 | `supportsDocumentStatus` | `DscpDomainProfile` | EXISTS | ACCEPT |
| Metadata requirement bridge exists | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.metadata.requirement.bridge.ts` | line 68 | `buildDscpMetadataRequirementBridge` | TypeScript function | EXISTS | ACCEPT |
| Bridge owner mismatch failure exists | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.metadata.requirement.bridge.ts` | line 97 | `OWNER_PROFILE_MISMATCH` | bridge failure token | EXISTS | ACCEPT |
| RDA-T3 roadmap row is released | `docs/roadmaps/CVF_MEOR_REGULATED_DOMAIN_ADAPTER_ROADMAP_2026-06-12.md` | line 147 | `RDA-T3` | parent roadmap | VALUE_SET | ACCEPT |

## New Runtime Fields Or Symbols

No new runtime fields or symbols are authorized. RDA-T3 may create a focused
test file only.

## Current Runtime Freshness Verification

Runtime/source freshness checked at base `ae3f3386` using direct source files
listed in the Source Verification Table. RDA-T3 must not rely on handoff or
memory summaries for source contracts.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| RDA-T2 closed | material commit `1c47d125` | SATISFIED |
| RDA-T2 sync | session sync commit `ae3f3386` | SATISFIED |
| RDA-T2 pre-closure | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 6a9a5703 --head HEAD` PASS at `ae3f3386` | SATISFIED |
| Parent roadmap release | RDA-T3 row `READY_FOR_FRESH_AUTHORIZATION` before this dispatch | SATISFIED |

## Negative Search And Collision Discipline

Search roots:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src`;
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests`;
- `docs/roadmaps/CVF_MEOR_REGULATED_DOMAIN_ADAPTER_ROADMAP_2026-06-12.md`.

Required worker checks:

- search for existing `dscp.regulated.domain.adapter.conformance.test.ts`;
- search for `documentStatus`, `promulgationDate`, `effectiveDate`, and
  `jurisdiction` collisions in the new test assertions;
- record whether each occurrence is adapter-owned, synthetic fixture-owned, or
  non-authoritative collision.

Disposition rule: same-token collisions are allowed only when the test labels
them as synthetic fixture values or expected regulated requirement keys.

## Reviewer Closure Conversion

completionReviewPath:
`docs/reviews/CVF_MEOR_RDA_T3_CROSS_DOMAIN_CONFORMANCE_COMPLETION_2026-06-12.md`

reviewerOwnedClosurePaths:

- `docs/reviews/CVF_MEOR_RDA_T3_CROSS_DOMAIN_CONFORMANCE_COMPLETION_2026-06-12.md`
- `docs/roadmaps/CVF_MEOR_REGULATED_DOMAIN_ADAPTER_ROADMAP_2026-06-12.md`
- `docs/baselines/CVF_GC018_MEOR_RDA_T3_CROSS_DOMAIN_CONFORMANCE_2026-06-12.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_MEOR_RDA_T3_CROSS_DOMAIN_CONFORMANCE_FOR_CLAUDE_2026-06-12.md`
- active session state, memory, and handoff continuity files.

Reviewer conversion rule: worker returns uncommitted artifacts only. Codex
performs closure review when the worker packet is returned, converts the
worker packet into committed closure if accepted, and records any findings
before commit.

## Evidence Reuse And Encoding Plan

verificationMode: `REUSE_PRIOR_VERIFICATION`

priorVerificationArtifact:
`docs/reviews/CVF_MEOR_RDA_T2_DETERMINISTIC_ADAPTER_IMPLEMENTATION_COMPLETION_2026-06-12.md`

priorVerificationAnchor: `1c47d125`

freshRecomputeRequired: NO

unicodePathHandling: `N/A with reason - RDA-T3 targets repo-local ASCII source/test paths only.`

extractedTextAuthority: `N/A with reason`

Encoding rule: all agent-authored artifacts and code comments default to ASCII.

## Allowed Scope

- focused CPF conformance test file, preferred:
  `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.regulated.domain.adapter.conformance.test.ts`;
- GC-051 registry JSON/Markdown rows for the new conformance test file;
- worker return packet if the worker records one under `docs/reviews/`;
- no source change unless the worker returns `BLOCKED_SOURCE_FIX_REQUIRED`
  with evidence and does not implement the source change.

## Forbidden Scope

- external Policy_Local paths;
- RDA-T2 adapter source edits without returning blocked;
- DSCP profile value updates for Policy_Local;
- `QUERY_CLASS_GATED` runtime activation;
- retrieval, OCR, corpus ingestion, provider/API-key use;
- public-sync, production readiness, public readiness;
- memory reinjection, high-risk promotion, autonomous mutation.

## Required Artifact Manifest

| Artifact | Required action | Notes |
| --- | --- | --- |
| focused CPF conformance tests | CREATE | synthetic profile fixtures only |
| GC-051 registry JSON/Markdown | UPDATE | cover new test file |
| worker return packet | CREATE or N/A with reason | summarize commands and boundaries |
| completion review | CODEX_REVIEWER_OWNED | close or block bounded |
| parent roadmap update | CODEX_REVIEWER_OWNED | close or block RDA-T3 |
| active continuity | CODEX_REVIEWER_OWNED | next allowed move |

## Work-Order Fulfillment Manifest

| Required artifact | Fulfillment rule | Closure status before execution |
| --- | --- | --- |
| Focused CPF conformance tests | must be created and passing or explicitly blocked | BLOCKED |
| GC-051 registry JSON/Markdown | must cover new test file or closure is blocked | BLOCKED |
| Worker return packet | worker records command evidence or N/A with reason | BLOCKED |
| Completion review | Codex-owned when worker packet is returned | BLOCKED |
| Parent roadmap update | must close or block RDA-T3 | BLOCKED |
| Continuity update | Codex-owned when material commit exists | BLOCKED |

## Pre-Flight Checks

1. Confirm RDA-T2 material commit `1c47d125` and sync commit `ae3f3386`.
2. Confirm RDA-T3 GC-018 and this work order are present at worker start.
3. Confirm preferred conformance test path is absent before creation.
4. Confirm no external Policy_Local path is modified.
5. Run focused tests and CPF TypeScript check before closure.

## Write Ownership

| Path | Action |
| --- | --- |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.regulated.domain.adapter.conformance.test.ts` | CREATE preferred |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | UPDATE if new test file is created |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | UPDATE if new test file is created |
| Worker return packet under `docs/reviews/` | CREATE allowed |
| Completion review, roadmap, baseline, work order, active continuity | CODEX_REVIEWER_OWNED |
| external Policy_Local paths | FORBIDDEN |

## Execution Plan

1. Import adapter, bridge, mapping table, and profile type from the CPF context
   barrel.
2. Create synthetic profiles for legal-policy, company-docs, technical-project,
   governance-docs, and mixed-corpus.
3. Assert the legal-policy profile with `supportsDocumentStatus=true` produces
   exactly four regulated requirements.
4. Assert all non-regulatory profiles and a legal-policy profile without the
   support flag produce zero generated requirements.
5. Assert cross-profile attachment fails with `OWNER_PROFILE_MISMATCH`.
6. Assert no test reads external Policy_Local files or writes gate values.
7. Update GC-051 registry for the new test file.
8. Run focused tests and CPF `npm run check`.
9. Return uncommitted packet to Codex.

## Evidence Requirements

- focused test command and result;
- `npm run check` result;
- changed-path list;
- GC-051 registry evidence;
- no external Policy_Local path evidence;
- explicit claim boundary in worker return.

## Acceptance Criteria

1. Tests import the adapter surface through `control.plane.context.barrel.ts`.
2. Regulated legal-policy profile with `supportsDocumentStatus=true` produces
   exactly four regulated requirements.
3. Non-regulatory profiles produce no generated regulated lifecycle fields.
4. Legal-policy profile without the support flag produces no generated
   regulated lifecycle fields.
5. Cross-profile regulated requirement attachment fails closed with
   `OWNER_PROFILE_MISMATCH`.
6. Tests remain synthetic and do not read external Policy_Local files.
7. Focused tests and CPF TypeScript check pass.
8. Changed paths stay inside Allowed Scope.

## Review Gate

Reject closure if the worker claims metadata truth, legal/current status,
Policy_Local readiness, EC activation, retrieval readiness, provider behavior,
production readiness, public readiness, or uses real Policy_Local corpus files.

## Closure Checklist

- [x] Focused conformance tests implemented.
- [x] Focused tests and CPF TypeScript check passing.
- [x] GC-051 registry updated for new test file.
- [x] No external Policy_Local or EC activation changes.
- [x] Reviewer-fast and pre-closure pass.
- [x] Continuity sync completed after Codex commit.

## Return-To-Orchestrator Conditions

Return if RDA-T3 cannot close without runtime source mutation, external
Policy_Local edits, operator/source metadata evidence, EC activation,
retrieval changes, OCR, provider/API-key use, public-sync, or claim-boundary
expansion.

## Operator Checkpoint

operator.checkpoint.waiver: operator instructed Codex to continue into the
next governed roadmap. No additional checkpoint is required inside this
bounded RDA-T3 dispatch scope. Any scope expansion listed in
Return-To-Orchestrator Conditions requires a fresh operator checkpoint.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | RDA-T3 completion review | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | parent roadmap | RDA-T3 closed; RDA-T4 ready for fresh authorization | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | RDA-T3 conformance test entry present | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | RDA-T3 conformance test row present | PASS |
| External evidence digest | N/A with reason: repo-local synthetic conformance tests | no external evidence expected | N/A with reason |
| System loop interlock | N/A with reason: no loop mutation | no system-loop registry update expected | N/A with reason |
| Session continuity | active state/memory/handoff | material closure sync commit records next move | PASS |

## Claim Boundary

This work order authorizes local deterministic CPF conformance tests only. It
does not authorize Policy_Local mutation, metadata correction, EC activation,
retrieval, OCR, corpus ingestion, provider use, public-sync, production
readiness, public readiness, or autonomous correction.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private RDA-T3 conformance dispatch; no public-sync authorized.
