# CVF ACEL G1 T3D-C2 Source-Creation Readiness Gap Audit

Memory class: FULL_RECORD

docType: audit

Status: BLOCKED_T3D_C2_DISPATCH

Date: 2026-09-23

Batch ID: ACEL-G1-T3D-C2-SOURCE-CREATION-READINESS-GAP

Decision base HEAD: `47a20fe89857a15b046df9679ae19bd205c0db1d`

providerExecutionAuthority: FORBIDDEN

successorTrancheOpened: NO

## Purpose

Decide whether the accepted T3D-C1 Group 4 tooling can safely enter real
Party C and Party B source creation. The answer is no: three operational
joins remain unowned and must be fixed in the contract before executable
tooling or credentials are used.

## Target / Source

| Source | Authority used |
|---|---|
| `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Group 4 paths, file DACLs, canonical bytes and T3D/T3E lifecycle |
| `docs/reviews/CVF_ACEL_G1_T3D_C1_GROUP4_ISSUER_REGISTRY_LOOKUP_TOOLING_COMPLETION_2026-09-22.md` | accepted C1 tooling hashes and `TOOLING_ACCEPTED_SOURCE_NOT_CREATED` ceiling |
| `scripts/acel_g1_party_c_group4_registry_writer.ps1` | target-absent, same-directory atomic registry publication behavior |
| `scripts/acel_g1_party_b_group4_lookup_response_writer.ps1` | target-absent response initialization and observation dependency |
| `scripts/acel_g1_party_b_group3_observation_writer.ps1` | production path is hard-bound to `verifier_key_registry`, not `issuer_registry` |

## Scope / Methodology

Local reconciled the accepted file-level security contract with Windows
parent-directory delete/replace semantics, inspected the real-mode writer
preconditions, and commissioned two independent read-only internal probes.
No credentials, alternate-principal session, source mutation, staging or
commit was used.

## Findings / Position

| ID | Finding | Impact | Disposition |
|---|---|---|---|
| T3D-C2-GAP-01 | T2F freezes exact file DACLs but no owner/DACL or effective-rights model for their shared parent directory | `DELETE_CHILD`, create-file, rename or replacement rights can bypass the intended cross-principal separation | AMEND_CONTRACT |
| T3D-C2-GAP-02 | the accepted 618-byte vector uses test identity, test snapshot ID and fixed 2026-09-22 timestamps | it is a hermetic fixture, not admissible operational-source input; real publication needs fresh identity/timestamps and recomputed bytes/hashes | AMEND_CONTRACT |
| T3D-C2-GAP-03 | no accepted production route appends a Party B observation for `issuer_registry` to the existing Group 3 log | T3E cannot bind a lookup response to exact published registry bytes; the Group 1-only writer/launcher must not be repurposed | AMEND_THEN_IMPLEMENT |

The C1 tooling remains accepted within its prior hermetic boundary. This audit
does not reopen that evidence; it finds an operational readiness boundary that
was not exercised by C1.

## Selected Route

Decision: `SELECT_ACEL_G1_T3D_C0_R1_GROUP4_OPERATIONAL_BOUNDARY_AMENDMENT`.

T3D-C0-R1 is contract-only and must amend the existing T2F owner rather than
create a second contract. It must freeze:

1. a protected shared-directory or privileged-mediation model that prevents
   Party B from deleting/replacing Party C's registry and prevents Party C
   from deleting/replacing Party B's response log;
2. a reservation or equivalent name-ownership mechanism that closes initial
   precreation races while retaining crash-safe publication;
3. fresh operational `registrySnapshotId`, timestamps, canonical input bytes
   and recomputed hashes; the published positive vector remains test-only;
4. an ordered Party C publication, Local verification, Party B issuer
   observation, Local verification, response-log initialization, and final
   Local verification sequence;
5. actual-token adversarial proof requirements for cross-delete,
   cross-replace, DACL/owner mutation, reparse/hardlink and residue cases.

Only after Local accepts C0-R1 may a separate T3D-C1-R2 work order change
writers/checkers or add the issuer-observation route. Real source creation
remains a later operator checkpoint.

## Risk / Corrective Action

| Risk | Corrective action |
|---|---|
| file DACL evidence is mistaken for complete path isolation | require parent-directory owner, protected DACL, rights and real-token negative probes |
| test fixture becomes a durable identity | require fresh operational identity/time generation and reject fixture literals in real mode |
| empty response log is treated as consumer binding | keep issuer observation and T3E lookup as separately verified ordered checkpoints |
| implementation invents contract choices | close C0-R1 before dispatching C1-R2 |

## Finding-To-Governance Learning Disposition

Defect class: `ORCHESTRATOR_PACKET_GAP`.

Learning lane: `GOVERNANCE_CONTROL_PLANE`.

Disposition: `DESIGN_REVIEW_REQUIRED`.

Next action: dispatch one contract-only T3D-C0-R1 amendment, then perform a
separate Local review before any implementation correction. The repeated
source-ceremony preflight pattern remains queued for post-ACEL foundation
learning; this audit does not widen the active tranche to that foundation.

Runtime behavior learning, provider output learning and cost economics
learning are `N/A_WITH_REASON`: no runtime, provider call, quota or priced
usage is asserted by this read-only audit.

## Epistemic Process Block

### Expected Result / Prediction

Accepted C1 tooling was expected to be sufficient for a bounded two-file
source-creation checkpoint.

### Evidence Comparison

The writers prove file-level transactions, but the shared parent directory
has no accepted security contract; the published positive vector is explicitly
test data; and no production Party B issuer-observation route exists.

### Contradiction Or Gap Disposition

The readiness expectation is contradicted. The complete dependency class is
routed to one C0-R1 contract amendment, not patched piecemeal in launchers.

### Claim Update

T3D remains `TOOLING_ACCEPTED_SOURCE_NOT_CREATED`; T3D-C2 real execution is
blocked until C0-R1 and its separately governed C1-R2 successor are accepted.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | governed audit headings, accepted defect class/lane/disposition, Evidence Comparison, Contradiction Or Gap Disposition, Claim Update, trace labels and private export token |
| gateRunPurpose | confirm the bounded readiness decision; machine shape is not source evidence |
| claimBoundary | read-only route selection only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | CVF Local orchestrator/reviewer |
| Provider or surface | local private provenance workspace with two read-only internal probes |
| Session or invocation | ACEL G1 T3D-C2 readiness audit, 2026-09-23 |
| Working directory | repository root |
| Command or tool surface | governed reads, `rg`, exact-hash checks, read-only sub-agent review, `apply_patch`, governance gates and Git |
| Target paths | this audit only |
| Allowed scope source | current handoff next move authorizes Local audit/selection of T3D-C2 |
| Before status evidence | HEAD `47a20fe89857a15b046df9679ae19bd205c0db1d`; C1 accepted; Group 4 source paths absent; thirteen parked paths present |
| After status evidence | three gaps consolidated; C0-R1 selected; no source or executable correction created |
| Diff evidence | exact one-path audit delta before dispatch packet completion |
| Approval boundary | readiness audit and route selection only |
| Claim boundary | no credential, principal execution, source, lookup, provider/live, public or deployment effect |
| Agent type | Local orchestrator/reviewer |
| Invocation ID | `acel-g1-t3d-c2-readiness-gap-audit-20260923` |
| Expected manifest | this audit |
| Actual changed set | this audit |
| Manifest delta | MATCH |
| Deletion or rename disposition | none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private machine-specific source-authority and ACL design evidence; no
public-sync authority exists.

## Claim Boundary

This audit blocks real T3D-C2 execution and selects a contract-only correction.
It does not modify the T2F contract, change tooling, create a launcher or source,
use a credential, run as Party B/C, append an observation or response, perform
a lookup, open T3E, promote or admit a candidate, call a provider, export
publicly or deploy.
