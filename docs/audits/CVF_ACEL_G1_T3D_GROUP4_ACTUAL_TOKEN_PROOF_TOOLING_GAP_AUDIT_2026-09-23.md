# CVF ACEL G1 T3D Group 4 Actual-Token Proof Tooling Gap Audit

Memory class: FULL_RECORD

docType: audit

Status: BLOCKED_ACTUAL_TOKEN_PROOF_PENDING_TOOLING_CORRECTION

Date: 2026-09-23

Decision base HEAD: `641d4ced9`

providerExecutionAuthority: FORBIDDEN

successorTrancheOpened: NO

## Purpose

Check whether the accepted T3D-C1 writers can execute the post-C0-R1
disposable-root actual-token proof without modifying real Group 4 sources.
The answer is no. This audit prevents a premature proof dispatch and selects
the smallest safe correction boundary.

## Target / Source

| Source | Relevant observed region |
|---|---|
| `scripts/acel_g1_party_c_group4_registry_writer.ps1` | `Assert-ExactExecutionBoundary`, `Publish-RegistryTransaction`, `Remove-OrphanTemps`, `PeerMode` and `CrashMode` |
| `scripts/acel_g1_party_b_group4_lookup_response_writer.ps1` | `Assert-PrincipalAndPaths`, `Write-CopyOnWriteTransaction`, `Remove-OrphanTemps`, `InitializeResponseLog`, `PeerMode` and `CrashMode` |
| `docs/audits/CVF_ACEL_G1_T3D_C0_R1_GROUP4_OPERATIONAL_BOUNDARY_AMENDMENT_2026-09-23.md` | protected parent, two zero-byte reservations, own-target replacement, ledger-bound recovery, actual-token matrix |
| `docs/reviews/CVF_ACEL_G1_T3D_C0_R1_GROUP4_OPERATIONAL_BOUNDARY_AMENDMENT_COMPLETION_2026-09-23.md` | contract-only acceptance and C1-R2/actual-token hold |
| `docs/audits/CVF_ACEL_G1_T3D_GROUP4_DISPOSABLE_ROOT_PROOF_PACKET_2026-09-23.md` | static proof ledger and isolation checkpoint, not implementation acceptance |

## Scope / Methodology

Role: `LOCAL_REVIEWER`; phase: pre-dispatch proof-tooling compatibility;
decision owner: Local. I compared the two accepted writer entrypoints and
transaction branches to the C0-R1 reservation/recovery contract. The method
was source inspection only. No account, credential, ACL, disposable fixture,
real source, subagent, staging change or runtime proof was used.

## Findings / Position

| ID | Source observation | Contract conflict | Disposition |
|---|---|---|---|
| G4-PROOF-01 | Party C's real boundary rejects any existing registry; its transaction also rejects an existing target and moves with overwrite disabled | C0-R1 requires a pre-owned zero-byte `REGISTRY.json` and a hardened own-target replacement | BLOCKING |
| G4-PROOF-02 | Party B's real initializer calls `Write-CopyOnWriteTransaction` with `RequireAbsent` | C0-R1 requires a pre-owned zero-byte `LOOKUP_RESPONSES.jsonl` and an atomic zero-byte claim | BLOCKING |
| G4-PROOF-03 | both transactions call `Remove-OrphanTemps` and delete pattern-matched old temporary files | C0-R1 reserves prior-transaction cleanup for exact ledger-bound Administrator recovery; unknown residue must remain untouched | BLOCKING |
| G4-PROOF-04 | real modes bind to the canonical Git root and governed source paths, while peer/crash modes use disposable test paths with test security policy and no exact Party B/C identity check | neither route is an accepted disposable-root test of the exact production descriptors under both non-elevated principals | BLOCKING |

The prior T3D-C1 `TOOLING_ACCEPTED_SOURCE_NOT_CREATED` disposition remains
valid for its original hermetic/target-absent scope. This audit finds a new
join contradiction introduced by the later accepted C0-R1 operational model;
it does not retroactively claim that the C1 tests failed.

## Selected Route

Decision: `SELECT_C1_R2_RESERVATION_COMPATIBLE_HERMETIC_TOOLING_CORRECTION_FIRST`.

Before any actual-token proof order, a separately governed correction must
make both writers and their disposable entrypoints honor the exact two-file
reservation model, target-specific replacement, no cross-target mutation,
and fail-closed unknown residue. Durable ledger-bound recovery must have a
separate Administrator owner; no ordinary writer may sweep old temps. The
correction must prove positive own-target operation, negative cross-target
and parent operations, rollback and real-peer exclusion in hermetic fixtures.
It may prepare a principal-bound disposable entrypoint, but must not invoke
Party B/C, mutate the real source, or claim Windows actual-token success.

After Local accepts that correction, a distinct operator-checkpointed proof
may run on a validated disposable root. If the actual tokens then fail the
exact C0-R1 matrix, route to a new split-path or privileged-mediator contract,
not silent ACE widening. No C1-R2 worker is dispatched by this audit.

## Risk / Corrective Action

Running the current real modes would either reject the required reservations
or target the real source paths. Reusing test modes would supply a false
principal/security oracle. A broad cleanup could delete evidence outside the
current transaction. Keep execution on hold; close all four mismatches in
one bounded tooling correction before issuing an actual-token proof order.

## Decision / Disposition

`BLOCKED_ACTUAL_TOKEN_PROOF_PENDING_TOOLING_CORRECTION`.

The next allowed action is Local preparation of a bounded C1-R2 correction
baseline and work order, without subagent dispatch. The actual-token proof,
Group 4 source creation, Party B issuer observation, lookup response, T3E,
promotion and admission remain closed.

## Claim Boundary

This is a static source/contract comparison. It does not demonstrate Windows
permission behavior, completed correction, principal execution, source
establishment, live provider behavior, public export or deployment readiness.
