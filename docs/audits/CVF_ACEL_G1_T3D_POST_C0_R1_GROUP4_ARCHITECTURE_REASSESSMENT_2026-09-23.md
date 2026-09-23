# CVF ACEL G1 T3D Post-C0-R1 Group 4 Architecture Reassessment

Memory class: FULL_RECORD

docType: audit

Status: STATIC_FEASIBILITY_SPEC_SELECTED_NOT_DISPATCHED

Date: 2026-09-23

Decision base HEAD: `39397408f`

providerExecutionAuthority: FORBIDDEN

successorTrancheOpened: NO

## Purpose

Make the fresh Local architecture decision required after the T3D-C0-R1
`STOP_REASSESS_ARCHITECTURE` disposition. This decision identifies the next
bounded design artifact; it does not dispatch C1-R2 or authorize Windows
principal execution.

## Target / Source

| Source | Authority used |
|---|---|
| `docs/reviews/CVF_ACEL_G1_T3D_C0_R1_GROUP4_OPERATIONAL_BOUNDARY_AMENDMENT_COMPLETION_2026-09-23.md` | accepted contract ceiling, convergence stop, and remaining Windows proof obligation |
| `docs/audits/CVF_ACEL_G1_T3D_C0_R1_GROUP4_OPERATIONAL_BOUNDARY_AMENDMENT_2026-09-23.md` | exact candidate security, reservation, transaction, recovery and fallback conditions |
| `docs/audits/CVF_ACEL_G1_T3D_C2_SOURCE_CREATION_READINESS_GAP_AUDIT_2026-09-23.md` | original three operational gaps and source-creation block |
| `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Group 4 owner contract and lifecycle boundary |
| `docs/reviews/evidence/cvf-acel-g1-t2-rejected-parked-evidence-archive-2026-09-23.json` | rejected T2/T2A/T2B evidence remains archival, not active authority |

## Scope / Methodology

Role: `LOCAL_REVIEWER`; phase: post-C0-R1 architecture reassessment; decision
owner: Local. This is a read-only comparison of the accepted contract and its
closure against the next proof dependency. No subagent, credential, alternate
principal, ACL mutation, source creation or live call was used.

## Findings / Position

1. C0-R1 has closed the three named contract gaps, but its shared-parent
   candidate is `FEASIBLE_WITH_REQUIRED_WINDOWS_PROOF`, not proven feasible.
   The missing evidence is effective behavior under both exact non-elevated
   Party B and Party C tokens, including positive own-target publication and
   negative cross-target/parent mutations.
2. Repeating another prose-level correction to the accepted contract would
   not reduce this blocker. Nor would a test under an elevated Local token
   substitute for the two principal-specific observations.
3. A split-path design or privileged mediator would change the accepted owner
   contract and authorization boundary. Neither is justified merely because
   the shared-parent candidate has not yet been tested; either becomes a new
   contract choice only if the exact candidate fails or cannot be safely
   tested.
4. The 13 rejected T2/T2A/T2B paths have been archived with hash-verified
   recovery. They are not an alternative implementation source and do not
   lower the Group 4 proof requirement.

## Architecture Option Decision

| Option | Current evidence | Decision |
|---|---|---|
| bounded shared-parent feasibility specification | accepted C0-R1 design defines exact descriptors, asymmetric access and a disposable-root actual-token matrix; observed execution is still absent | SELECT as the next static artifact only |
| immediate split protected parents | no failed shared-parent probe or accepted revised path/lifecycle contract | HOLD as a conditional fallback |
| privileged mediator | no accepted mediator threat model, privilege boundary or operational owner | HOLD as a conditional fallback |
| direct C1-R2 implementation or real Group 4 source | convergence stop and proof gap remain | FORBID |

## Selected Route

Decision: `SELECT_GROUP4_SHARED_PARENT_STATIC_FEASIBILITY_SPEC_FIRST`.

The next separately governed packet may specify a disposable-root proof
procedure for the exact C0-R1 candidate. It must freeze the two principal
identities and token preconditions; exact parent and reserved-file security
descriptors; allowed own-target and forbidden cross-target operations;
pre/post identity, byte, hash, DACL, owner and residue observations; peer
concurrency; crash/recovery cases; and a fail-closed cleanup and evidence
ledger. It must name a rollback/recovery owner and protect unrelated workspace
paths. The packet must make actual-token execution an explicit operator
checkpoint, not an implied consequence of this decision.

If a later authorized disposable-root proof fails or is inconclusive, stop at
`TOOLING_ACCEPTED_SOURCE_NOT_CREATED` and return to a new Local-reviewed
contract selecting split paths or a narrowly scoped mediator. Do not widen an
ACE, silently change paths, or treat a thrown exception as a verified denial.

## Risk / Corrective Action

The main residual risk is confusing a contract-complete Windows design with a
working access-control configuration. A static feasibility specification can
reduce ambiguity and command/operator error, but cannot establish the
principal-specific result. Real Group 4 source creation, issuer observation,
lookup response, T3E consumer binding, promotion and admission remain closed.

## Decision / Disposition

`STATIC_FEASIBILITY_SPEC_SELECTED_NOT_DISPATCHED`. This audit is the fresh
Local architecture selection after C0-R1, not an automatic continuation of
the stopped correction chain. `successorTrancheOpened: NO` remains true.

## Claim Boundary

No Windows actual-token proof, account access, Group 4 source, T3E consumer,
provider behavior, public export or deployment readiness is claimed.
