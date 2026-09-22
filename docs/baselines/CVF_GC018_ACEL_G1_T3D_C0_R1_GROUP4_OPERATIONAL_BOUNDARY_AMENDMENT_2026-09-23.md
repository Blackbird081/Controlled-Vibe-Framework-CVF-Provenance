# CVF GC-018 Baseline - ACEL G1 T3D-C0-R1 Group 4 Operational Boundary Amendment

Memory class: SUMMARY_RECORD

Status: DISPATCH_READY

docType: baseline

Date: 2026-09-23

Batch ID: ACEL-G1-T3D-C0-R1-GROUP4-OPERATIONAL-BOUNDARY-AMENDMENT

Dispatch base HEAD: `47a20fe89857a15b046df9679ae19bd205c0db1d`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Local.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-G1-T3D-C0-R1-GROUP4-OPERATIONAL-BOUNDARY-AMENDMENT --title "ACEL G1 T3D-C0-R1 Group 4 Operational Boundary Amendment" --date 2026-09-23 --base 47a20fe89857a15b046df9679ae19bd205c0db1d --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind REWORK --dispatch-surface INTERNAL_AGENT --stdout` |
| generatedProfile | GC-018 contract-only amendment baseline |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | populated exact shared-directory, reservation, fresh-input, observation-order and proof obligations |
| checkerReadAheadConfirmation | structural, dispatch-quality, closeability, dual-surface, learning and public-export checker sources reviewed |
| docOnlyNewFields | parent-directory reservation, fresh operational input and issuer-observation ordering clauses |
| claimBoundary | baseline and contract amendment only; no transaction, tooling or source execution |

## Purpose

Freeze the missing operational boundary that must exist between accepted C1
file-level tooling and any real Group 4 source creation. This baseline owns
only a bounded amendment to the existing T2F contract.

## Scope / Target / Owner Boundary

The worker may modify exactly the existing T2F contract and create exactly one
worker return. It may not edit any writer, checker, test, launcher, source,
session or handoff path. It may not use credentials or run as Party B/C.
Local remains reviewer and decision owner.

High-Risk Local Transaction Proof Applicability: NOT_APPLICABLE_WITH_REASON - contract-only documentation amendment; no target transaction, DACL mutation, durable write or executable tooling change is authorized.

## Decision / Baseline / Proposed Tranche

Decision: `AMEND_EXISTING_T2F_THEN_STOP_FOR_SEPARATE_C1_R2_AUTHORITY`.

Baseline: C1 remains accepted at `TOOLING_ACCEPTED_SOURCE_NOT_CREATED`, but
real T3D-C2 dispatch is blocked by the readiness audit.

Proposed tranche: C0-R1 freezes the complete operational directory/input/
observation contract. A separately reviewed C1-R2 may implement it. Real
source creation remains an operator checkpoint after C1-R2 acceptance.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Disposition |
|---|---|---|---|---|
| T3D-C2 has three blocking operational gaps | REVIEWED_DECISION | `docs/audits/CVF_ACEL_G1_T3D_C2_SOURCE_CREATION_READINESS_GAP_AUDIT_2026-09-23.md` | Findings / Position; Selected Route | ACCEPT |
| Existing Group 4 exact paths and file DACLs remain the accepted base being enriched | CURRENT_AUTHORITY | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Source Group 4; G4-GAP-03 and G4-GAP-04 | ACCEPT |
| C1 tooling is accepted only without real source | LOCAL_CLOSURE | `docs/reviews/CVF_ACEL_G1_T3D_C1_GROUP4_ISSUER_REGISTRY_LOOKUP_TOOLING_COMPLETION_2026-09-22.md` | Decision / Disposition; Claim Boundary | ACCEPT |
| Party B existing writer is Group 1-specific | EXECUTABLE_SOURCE | `scripts/acel_g1_party_b_group3_observation_writer.ps1` | description and real-mode constants | ACCEPT |

## Required Contract Decisions

### Protected parent and reserved targets

The amendment must define one exact owner and complete protected DACL for
`governance/sources/issuer_registry/`. It must explicitly address directory
`CreateFiles`, `CreateDirectories`, `DeleteChild`, `Delete`, `WriteDac`,
`WriteOwner`, inheritance, reparse points and same-directory rename/replace.

The preferred feasibility candidate is an Administrators-owned protected
directory with SYSTEM and Administrators FullControl; Party C and Party B only
`ReadAndExecute`, `CreateFiles`, and `Synchronize`; and Local traverse/read.
Party B/C receive no `CreateDirectories`, `DeleteChild`, directory `Delete`,
`WriteDac`, or `WriteOwner`. Before either principal receives execution
authority, an administrative reservation step creates exact zero-byte
`REGISTRY.json` and `LOOKUP_RESPONSES.jsonl` placeholders with their final
owners and exact file DACLs. The amendment must mark this candidate
`FEASIBLE_WITH_REQUIRED_WINDOWS_PROOF`, not proven runtime behavior.

The later C1-R2 must require writers to claim an exact reservation, reject a
missing or drifted target, publish only to the writer-owned target, and reject
unexpected siblings, reparse traversal, hardlink-count anomalies, stale temp
files or weakened directory/file security.

### Fresh operational input

The fixed positive vector remains hermetic only. Real mode must reject its
test snapshot identity and fixed timestamps. A future operator-approved input
must use a fresh globally unique `registrySnapshotId`, current internally
generated RFC3339 UTC timestamps, approved issuer content, exact RFC 8785 JCS
bytes, and independently recomputed content/snapshot hashes. No caller-supplied
digest or timestamp is trusted without recomputation and order checks.

### Ordered source lifecycle

The amendment must require: accepted contract; accepted C1-R2 tooling; Local
parent/reservation verification; fresh input; Party C registry publication;
Local byte/hash/DACL verification; Party B immutable `issuer_registry`
observation; Local exact-byte observation verification; Party B response-log
reservation verification/initialization; Local joint verification; then and
only then `SOURCE_CREATED_LOCAL_VERIFIED_PENDING_CONSUMER_BINDING`.
T3E alone owns the first real lookup/response append and consumer binding.

### Actual-token adversarial proof

Before source authority, real Party C/B tokens must prove own-target atomic
publication and cleanup while cross-target delete, rename, overwrite, replace,
owner/DACL change and directory mutation fail without residue. The proof must
also cover reparse/junction traversal, hardlinks, unexpected siblings,
inherited/extra/deny ACEs and crash/rollback boundaries.

## Acceptance Criteria

1. T2F receives one controlling amendment covering all four decision groups.
2. The candidate directory model is labeled conditional on real Windows proof.
3. Fixture literals cannot be mistaken for operational source input.
4. Issuer observation is an explicit prerequisite before C2 closure and T3E.
5. C1-R2 and real source execution remain separately authorized.
6. Exactly two worker paths are pending, staging remains empty, and thirteen
   parked paths retain their SHA-256 values.

## Evidence / Verification Boundary

The worker may prove only internal contract coherence and exact document
shape. It cannot prove NTFS runtime isolation, credential separation, real
principal behavior, source creation or consumer binding.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`DOC_CHANGE`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_high_risk_local_transaction_proof.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | baseline headings, source-verification path form, high-risk applicability declaration, dual-surface dispositions and private export token |
| gateRunPurpose | confirm dispatch shape; gate output is not operational proof |
| claimBoundary | contract-only amendment |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority/risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | shared-workspace contract worker | exact two-path no-commit scope | work order and return | no runtime adapter | `IMPLEMENTED` |
| `EXTERNAL_AGENT_CLI_MCP` | no external dispatch | credentials and filesystem mutation forbidden | explicit exclusion | separate future source-verified adapter work order required | `DEFERRED_WITH_REASON` |

## Finding-To-Governance Learning Disposition

Defect class: `ORCHESTRATOR_PACKET_GAP`.

Learning lane: `GOVERNANCE_CONTROL_PLANE`.

Disposition: `DESIGN_REVIEW_REQUIRED`.

Next action: accept or reject the bounded C0-R1 contract before C1-R2.

## Epistemic Process Block

### Expected Result / Prediction

A contract-only amendment can close the missing operational joins without
executing or changing implementation.

### Evidence Comparison

The cited sources identify exact file paths and principals but omit parent
directory rights, fresh-source discrimination and an issuer-observation route.

### Contradiction Or Gap Disposition

All gaps are routed to the existing T2F owner in one bounded amendment.

### Claim Update

The packet is dispatch-ready for documentation only; T3D-C2 remains blocked.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private operational security contract; no public-sync authority.

## Claim Boundary

This baseline authorizes only a two-path contract amendment return. It does
not change tooling, ACLs, accounts, credentials, source files, observations,
lookups, admission, provider/live behavior, public export or deployment.
