# CVF Agent Work Order: MEOR-RDA-T2 Deterministic Adapter Implementation

Memory class: FULL_RECORD

Status: DISPATCHED

docType: work_order

Date: 2026-06-12

Worker: Claude

Reviewer: Codex

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `6a9a5703`

executionBaseHead: `6a9a5703`

closureBaseHead: `6a9a5703`

GC-018:
`docs/baselines/CVF_GC018_MEOR_RDA_T2_DETERMINISTIC_ADAPTER_IMPLEMENTATION_2026-06-12.md`

Parent roadmap:
`docs/roadmaps/CVF_MEOR_REGULATED_DOMAIN_ADAPTER_ROADMAP_2026-06-12.md`

## Purpose

Implement the bounded local deterministic regulated-domain adapter helper
authorized by RDA-T2.

The helper must convert a `DscpDomainProfile` into profile-owned regulated
MEOR metadata requirements when and only when the profile explicitly supports
regulated document lifecycle metadata.

## Authority Chain

| Authority | Path | Status |
| --- | --- | --- |
| Operator direction | 2026-06-12 continue following MEOR/RDA foundation closure | ACCEPT |
| Parent roadmap | `docs/roadmaps/CVF_MEOR_REGULATED_DOMAIN_ADAPTER_ROADMAP_2026-06-12.md` | ACTIVE_RDA_T2_DISPATCHED |
| RDA-T1 completion | `docs/reviews/CVF_MEOR_RDA_T1_REGULATED_DATE_ADAPTER_CONTRACT_COMPLETION_2026-06-12.md` | CLOSED_PASS_BOUNDED |
| RDA-T2 GC-018 | `docs/baselines/CVF_GC018_MEOR_RDA_T2_DETERMINISTIC_ADAPTER_IMPLEMENTATION_2026-06-12.md` | AUTHORIZED |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order requirement | Output | Verification |
| --- | --- | --- | --- |
| Implement local deterministic adapter | add CPF helper and tests | source/test files | focused tests |
| Keep lifecycle fields profile-scoped | require `supportsDocumentStatus=true` | helper logic | failure tests |
| Preserve MEOR evidence basis | use allowed DSCP evidence values | generated requirements | bridge validation |
| Prevent Policy_Local mutation | forbid external paths | changed-path proof | git status/diff |
| Prepare conformance tranche | record RDA-T3 readiness boundary | completion review | claim boundary |

## Intake Role Routing Decision

- Intake summary: implement the adapter contract after RDA-T1 closed.
- Scope classification: bounded local deterministic implementation tranche.
- Risk sensitivity: medium, because implementation touches CPF source/tests.
- routeMode: `MULTI_AGENT_MULTI_ROLE`;
- reason: worker implements and Codex reviews/commits to preserve separation.
- Escalation condition: stop if runtime gate activation, external workspace
  edits, provider use, public-sync, or readiness claim expansion becomes
  necessary.

## Agent Roles

| Role | Actor | Responsibility |
| --- | --- | --- |
| Worker | Claude | implement allowed CPF helper/tests and return uncommitted |
| Reviewer | Codex | verify scope, run gates, commit if accepted |
| Continuity updater | Codex | update roadmap/state/handoff during reviewer-owned closure sync |

## Worker Autonomy / No-Question Rule

Repair allowed-scope implementation, test, formatting, and gate failures
without asking the operator. Escalate only when the repair would exceed
Allowed Scope or touch Forbidden Scope.

## Required First Reads

1. RDA roadmap.
2. RDA-T2 GC-018 baseline.
3. RDA-T1 contract and JSON semantics.
4. DSCP domain profile contract.
5. DSCP metadata requirement bridge.
6. GC-051 corpus scan registry standard and nearby CPF registry entries.

## Source Verification Table

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Fact class | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| DSCP metadata requirement interface exists | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 16 | `DscpMetadataRequirement` | DSCP domain profile contract | EXISTS | ACCEPT |
| DSCP evidence basis values exist | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 10 values `SOURCE_EMBEDDED`, `OPERATOR_SUPPLIED`, `DERIVED_HINT`, `NONE` | `MetadataEvidenceBasis` | DSCP domain profile contract | VALUE_SET | ACCEPT |
| Regulated support flag exists | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 67 | `supportsDocumentStatus` | `DscpDomainProfile` | EXISTS | ACCEPT |
| Profile metadata requirements field exists | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 71 | `metadataRequirements` | `DscpDomainProfile` | EXISTS | ACCEPT |
| Existing profile apply function is local deterministic | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 114 | `applyDomainProfileToDescriptorInput` | TypeScript function | EXISTS | ACCEPT |
| Existing boundary rule block logic exists | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | lines 122-130 | `boundaryRules` | `applyDomainProfileToDescriptorInput` | RUNTIME_BEHAVIOR | ACCEPT |
| Requirement bridge result exists | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.metadata.requirement.bridge.ts` | line 18 | `DscpMetadataRequirementBridgeResult` | TypeScript interface | EXISTS | ACCEPT |
| Requirement bridge function exists | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.metadata.requirement.bridge.ts` | line 68 | `buildDscpMetadataRequirementBridge` | TypeScript function | EXISTS | ACCEPT |
| Bridge detects owner mismatch | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.metadata.requirement.bridge.ts` | line 97 | `OWNER_PROFILE_MISMATCH` | bridge failure token | EXISTS | ACCEPT |
| Bridge detects duplicate requirements | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.metadata.requirement.bridge.ts` | line 104 | `DUPLICATE_REQUIREMENT_ID` | bridge failure token | EXISTS | ACCEPT |
| RDA adapter semantics version exists | `docs/reference/CVF_MEOR_REGULATED_DOMAIN_ADAPTER_SEMANTICS_2026-06-12.json` | line 2 | `adapterVersion` | RDA-T1 semantics JSON | VALUE_SET | ACCEPT |
| RDA regulated mappings exist | `docs/reference/CVF_MEOR_REGULATED_DOMAIN_ADAPTER_SEMANTICS_2026-06-12.json` | line 10 | `regulatedConceptMappings` | RDA-T1 semantics JSON | EXISTS | ACCEPT |
| RDA profile eligibility exists | `docs/reference/CVF_MEOR_REGULATED_DOMAIN_ADAPTER_SEMANTICS_2026-06-12.json` | line 5 | `profileEligibility` | RDA-T1 semantics JSON | EXISTS | ACCEPT |
| RDA invalid combinations exist | `docs/reference/CVF_MEOR_REGULATED_DOMAIN_ADAPTER_SEMANTICS_2026-06-12.json` | line 71 | `invalidCombinations` | RDA-T1 semantics JSON | EXISTS | ACCEPT |
| RDA contract defines adapter eligibility | `docs/reference/CVF_MEOR_REGULATED_DOMAIN_ADAPTER_CONTRACT_2026-06-12.md` | section `Adapter Eligibility`, required profile posture includes `supportsDocumentStatus=true` | `supportsDocumentStatus` | RDA-T1 contract | LITERAL_INVARIANT | ACCEPT |
| RDA contract defines regulated concept mapping | `docs/reference/CVF_MEOR_REGULATED_DOMAIN_ADAPTER_CONTRACT_2026-06-12.md` | section `Regulated Concept Mapping` | `documentStatus`, `promulgationDate`, `effectiveDate`, `jurisdiction` | RDA-T1 contract | EXISTS | ACCEPT |

## New Runtime Fields Or Symbols

| Proposed symbol | Owner | Purpose | Runtime status |
| --- | --- | --- | --- |
| `buildRegulatedDomainMetadataRequirements` | CPF RDA-T2 source | deterministic helper to generate regulated requirements | NEW_ALLOWED |
| `RegulatedDomainAdapterResult` | CPF RDA-T2 source | result envelope with generated requirements/failure token | NEW_ALLOWED |
| `REGULATED_DOMAIN_REQUIREMENT_MAPPINGS` | CPF RDA-T2 source | local mapping table mirroring RDA-T1 semantics | NEW_ALLOWED |

## Current Runtime Freshness Verification

Runtime/source freshness checked at base `6a9a5703` using direct source files
listed in the Source Verification Table. RDA-T2 must not rely on handoff or
memory summaries for source contracts.

## Reviewer Closure Conversion

completionReviewPath:
`docs/reviews/CVF_MEOR_RDA_T2_DETERMINISTIC_ADAPTER_IMPLEMENTATION_COMPLETION_2026-06-12.md`

reviewerOwnedClosurePaths:

- `docs/reviews/CVF_MEOR_RDA_T2_DETERMINISTIC_ADAPTER_IMPLEMENTATION_COMPLETION_2026-06-12.md`
- `docs/roadmaps/CVF_MEOR_REGULATED_DOMAIN_ADAPTER_ROADMAP_2026-06-12.md`
- `docs/baselines/CVF_GC018_MEOR_RDA_T2_DETERMINISTIC_ADAPTER_IMPLEMENTATION_2026-06-12.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_MEOR_RDA_T2_DETERMINISTIC_ADAPTER_IMPLEMENTATION_FOR_CLAUDE_2026-06-12.md`
- active session state, memory, and handoff continuity files.

Reviewer conversion rule: worker returns uncommitted artifacts only. Codex
performs closure review, converts the worker packet into committed closure if
accepted, and records any findings before commit.

## Evidence Reuse And Encoding Plan

verificationMode: `REUSE_PRIOR_VERIFICATION`

priorVerificationArtifact:
`docs/reviews/CVF_MEOR_RDA_T1_REGULATED_DATE_ADAPTER_CONTRACT_COMPLETION_2026-06-12.md`

priorVerificationAnchor: `6a6b343f`

freshRecomputeRequired: NO

unicodePathHandling: `N/A with reason - RDA-T2 targets repo-local ASCII source/test paths only.`

extractedTextAuthority: `N/A with reason`

Encoding rule: all agent-authored artifacts and code comments default to ASCII.

## Allowed Scope

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.regulated.domain.adapter.ts`
  or same-domain equivalent new helper file;
- focused CPF tests for the new helper;
- CPF exports if required by local pattern;
- GC-051 registry JSON/Markdown rows for new CPF source/test surfaces;
- RDA-T2 completion review;
- RDA roadmap, work order, GC-018, and continuity updates.

## Forbidden Scope

- external Policy_Local paths;
- DSCP profile value updates for Policy_Local;
- `QUERY_CLASS_GATED` runtime activation;
- retrieval, OCR, corpus ingestion, provider/API-key use;
- public-sync, production readiness, public readiness;
- memory reinjection, high-risk promotion, autonomous mutation.

## Required Artifact Manifest

| Artifact | Required action | Notes |
| --- | --- | --- |
| CPF adapter source | CREATE | local deterministic helper |
| focused CPF tests | CREATE | regulated/non-regulatory/failure cases |
| GC-051 registry JSON/Markdown | UPDATE | cover new source/test files |
| completion review | CREATE | close or block bounded |
| parent roadmap | UPDATE | RDA-T2 closure state |
| active continuity | UPDATE | next allowed move |

## Work-Order Fulfillment Manifest

| Required artifact | Fulfillment rule | Closure status before execution |
| --- | --- | --- |
| CPF adapter source | must be created or explicitly blocked | BLOCKED |
| Focused CPF tests | must be created and passing or explicitly blocked | BLOCKED |
| GC-051 registry JSON/Markdown | must cover new source/test files or closure is blocked | BLOCKED |
| Completion review | Codex-owned after worker return | BLOCKED |
| Parent roadmap update | must close or block RDA-T2 | BLOCKED |
| Continuity update | Codex-owned after commit | BLOCKED |

## Pre-Flight Checks

1. Confirm RDA-T1 material commit `6a6b343f` and sync commit `6a9a5703`.
2. Confirm RDA-T2 GC-018 and this work order are present and unchanged at
   worker start.
3. Confirm target CPF source/test paths are absent before creation unless the
   worker chooses a same-domain existing export file for minimal wiring.
4. Confirm no external Policy_Local path is modified.
5. Run local focused tests before returning.

## Write Ownership

| Path | Action |
| --- | --- |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.regulated.domain.adapter.ts` | CREATE preferred |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.regulated.domain.adapter.test.ts` | CREATE preferred |
| CPF export file if required by local pattern | UPDATE allowed |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | UPDATE if new source/test files are created |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | UPDATE if new source/test files are created |
| Completion review, roadmap, baseline, work order, active continuity | CODEX_REVIEWER_OWNED |
| external Policy_Local paths | FORBIDDEN |

## Execution Plan

1. Read CPF profile and bridge source.
2. Implement deterministic adapter helper in a new same-domain file.
3. Add focused tests for regulated, non-regulatory, duplicate/owner mismatch,
   and no runtime activation behavior.
4. Update GC-051 registry surfaces for new files.
5. Run focused tests and relevant CPF check command.
6. Return uncommitted packet to Codex.

## Evidence Requirements

- focused test command and result;
- changed-path list;
- GC-051 registry evidence;
- no external Policy_Local path evidence;
- explicit claim boundary in worker return.

## Acceptance Criteria

1. Helper returns generated regulated requirements only for
   `supportsDocumentStatus=true`.
2. Non-regulatory profile returns no generated regulated lifecycle fields.
3. Generated requirements are owner-profile scoped.
4. Bridge validation passes for generated valid requirements.
5. Failure tokens cover unsupported profile posture and ownership mismatch.
6. Focused tests pass.
7. Changed paths stay inside Allowed Scope.

## Review Gate

Reject closure if the worker claims metadata truth, current-law status,
Policy_Local readiness, EC activation, retrieval readiness, provider behavior,
production readiness, or public readiness.

## Closure Checklist

- [ ] Source helper implemented.
- [ ] Focused tests implemented and passing.
- [ ] GC-051 registry updated for new source/test files.
- [ ] No external Policy_Local or EC activation changes.
- [ ] Reviewer-fast and pre-closure pass.
- [ ] Continuity sync completed after Codex commit.

## Return-To-Orchestrator Conditions

Return if RDA-T2 cannot close without external Policy_Local edits,
operator/source metadata evidence, EC activation, retrieval changes, OCR,
provider/API-key use, public-sync, or claim-boundary expansion.

## Operator Checkpoint

operator.checkpoint.waiver: operator instructed Codex to continue into the
next governed roadmap. No additional checkpoint is required inside this
bounded RDA-T2 dispatch scope. Any scope expansion listed in
Return-To-Orchestrator Conditions requires a fresh operator checkpoint.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | `Status: DISPATCHED` | PASS |
| Completion or reviewer artifact | RDA-T2 completion review | absent before execution | BLOCKED |
| Roadmap state | parent roadmap | RDA-T2 dispatched | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | update required if new source/test files are created | BLOCKED with reason |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | update required if new source/test files are created | BLOCKED with reason |
| External evidence digest | N/A with reason: repo-local implementation | no external evidence expected | N/A with reason |
| System loop interlock | N/A with reason: no loop mutation | no system-loop registry update expected | N/A with reason |
| Session continuity | active state/memory/handoff | RDA-T2 execution next | PASS |

## Claim Boundary

This work order authorizes local deterministic CPF adapter implementation
only. It does not authorize Policy_Local mutation, metadata correction, EC
activation, retrieval, OCR, corpus ingestion, provider use, public-sync,
production readiness, public readiness, or autonomous correction.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private RDA-T2 implementation dispatch; no public-sync authorized.
