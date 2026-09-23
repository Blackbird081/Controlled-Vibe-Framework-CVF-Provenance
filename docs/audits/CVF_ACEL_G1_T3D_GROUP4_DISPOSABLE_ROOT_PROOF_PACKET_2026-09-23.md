# CVF ACEL G1 T3D Group 4 Disposable-Root Proof Packet

Memory class: FULL_RECORD

docType: audit

Status: STATIC_PACKET_READY_EXECUTION_HOLD

Date: 2026-09-23

Packet base HEAD: `ae4ee3870`

providerExecutionAuthority: FORBIDDEN

successorTrancheOpened: NO

## Purpose

Freeze the evidence and safety boundary for a later Windows actual-token
feasibility proof of the accepted Group 4 shared-parent candidate. This is a
static packet, not a run authorization, executable work order, C1-R2 dispatch,
or real-source ceremony.

## Target / Source

| Source | Binding |
|---|---|
| `docs/audits/CVF_ACEL_G1_T3D_POST_C0_R1_GROUP4_ARCHITECTURE_REASSESSMENT_2026-09-23.md` | fresh Local architecture selection, conditional fallback route |
| `docs/audits/CVF_ACEL_G1_T3D_C0_R1_GROUP4_OPERATIONAL_BOUNDARY_AMENDMENT_2026-09-23.md` | controlling parent/file candidate, reservations, transaction, recovery and actual-token proof matrix |
| `docs/reviews/CVF_ACEL_G1_T3D_C0_R1_GROUP4_OPERATIONAL_BOUNDARY_AMENDMENT_COMPLETION_2026-09-23.md` | contract accepted bounded; Windows proof and C1-R2 not authorized |

## Scope / Methodology

Role: `LOCAL_REVIEWER`; phase: Group 4 proof-packet preparation; decision
owner: Local. This packet records what a later operator-authorized experiment
must prove and what it may touch. No script, account, token, directory,
security descriptor or source was created or changed for this packet.

## Findings / Position

The accepted contract already contains the complete operation matrix, but
there is no observation under the exact Party B and Party C tokens. A later
proof must be isolated from the real source path, capture both allowed and
denied results, and preserve enough pre/post evidence for Local to adjudicate
the full matrix. This packet fills that execution-evidence boundary only.

## Isolation And Entry Gate

The later proof must use a newly created disposable root outside
`governance/sources/issuer_registry/`, never the real Group 4 parent. Record
its resolved absolute path and confirm that it is not the repository root,
home directory, live source directory, or an ancestor of either. All setup,
mutation, recovery and cleanup targets must be descendants of that verified
root. No proof invocation may begin until a separately reviewed execution
order and operator checkpoint identify the disposable root, exact Party C SID
ending `-1010`, exact Party B SID ending `-1009`, Local verifier SID ending
`-1001`, privilege/elevation state, and rollback owner. The two principals
must be independent non-elevated processes with the actual effective groups;
an Administrator/Local run is not a substitute.

The candidate must copy the exact parent owner, protected DACL and zero-byte
reserved-file setup from the controlling C0-R1 amendment. Compare semantic
ACE sets and resolved effective access masks, not display names alone. If
setup is partial, remove only the verified disposable setup before either
principal runs, then restart; do not normalize an ambiguous prestate.

This packet does not certify the accepted T3D-C1 writers as compatible with
those reservations. The post-packet Local source audit at
`docs/audits/CVF_ACEL_G1_T3D_GROUP4_ACTUAL_TOKEN_PROOF_TOOLING_GAP_AUDIT_2026-09-23.md`
controls that prerequisite: the currently accepted real modes require absent
targets, while the C0-R1 model requires both targets pre-reserved. A later
actual-token dispatch must first cite accepted reservation-compatible tooling
and independent Local review. Test-only peer/crash modes are not substitutes
for the real-principal proof.

## Required Proof Ledger

For every matrix row in the controlling amendment's `Required Actual-Token
Proof Matrix`, the later ledger must record: operation, actor name/SID/token
groups/elevation, target and resolved path, expected allow/deny, observed
result, pre/post file ID, exact bytes/hash, owner, DACL protection and semantic
ACE set, link count, reparse state, parent state and residue inventory. Record
the exact command/tool version and exit code. A thrown exception counts as a
negative result only when postconditions prove the non-target and parent were
unchanged. Log both positive own-target publication and every negative
cross-target/parent/security mutation attempt; do not select only successful
rows.

The ledger must also bind each temporary and recovery action to a durable
transaction ID, target identity, expected prestate and phase. Crash cases must
distinguish exact prestate from exact complete poststate. Unknown residue is
preserved and blocks proof acceptance; it is not opportunistically deleted.
Tests must cover the distinct Party C registry and Party B response targets,
including peer contention, hard termination and the recovery owner, exactly
as the controlling matrix requires. The proof is all-or-nothing: a missing
row, unavailable token, uncertain access mask, incomplete poststate, or
ambiguous cleanup returns `INCONCLUSIVE_OR_FAILED`, not `PASS`.

## Ordered Review And Stop Conditions

1. Local first verifies the disposable-root containment, exact candidate
   descriptors, two zero-byte reservations and complete prestate ledger.
2. Only after the separate execution checkpoint may each real principal run
   the bounded probes. Local independently verifies each pre/post state and
   token identity; the principal does not self-certify its own denial.
3. Local reviews the complete ledger against every controlling matrix row and
   exact cleanup/recovery evidence before selecting `PASS_ACTUAL_TOKEN_PROOF`
   or `INCONCLUSIVE_OR_FAILED`.
4. Any failed positive, succeeded forbidden operation, drift, unknown residue,
   or incomplete evidence stops further proof and leaves real Group 4 at
   `TOOLING_ACCEPTED_SOURCE_NOT_CREATED`. A split-path or mediator fallback
   requires a new contract; no automatic ACE widening or live-path reuse.

The packet does not supply credentials, ask the operator to disclose a
password, authorize account switching, or specify a command that mutates the
real source directory. It is safe to review now and executable only after a
separate order has bounded the actual-token actions and their cleanup.

## Risk / Corrective Action

The primary risk is false confidence from a successful setup or exception
without principal-specific poststate proof. A second risk is a disposable
test accidentally targeting the real source or leaving ambiguous residue.
The separate execution order must fail closed on either condition and keep
real Group 4 authority blocked until Local accepts the complete ledger.

## Decision / Disposition

`STATIC_PACKET_READY_EXECUTION_HOLD`. The next Local action is to close the
reservation/tooling mismatch in a separate documentation and hermetic tooling
correction tranche. Only after its independent acceptance may Local consider
a disposable-root actual-token proof order and operator checkpoint. Until
then C1-R2 real execution and Group 4 source creation remain unopened.

## Claim Boundary

This packet is not evidence of Windows feasibility, source establishment,
issuer observation, lookup response, T3E consumer binding, key promotion,
candidate admission, public export or deployment readiness.
