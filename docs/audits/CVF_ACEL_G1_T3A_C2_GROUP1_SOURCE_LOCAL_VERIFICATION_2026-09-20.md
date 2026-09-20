# CVF ACEL G1 T3A-C2 Group 1 Source Local Verification

Memory class: governed-audit

Status: SOURCE_CREATED_LOCAL_VERIFIED

Date: 2026-09-20

Owner: Local orchestrator/reviewer

successorTrancheOpened: NO

## Purpose

Record Local's independent verification of the operator-executed Party A
Group 1 source write and close only the T3A-C2 source-establishment checkpoint.

## Scope / Methodology

The operator executed the accepted writer as the exact non-admin Party A
principal. Local then read the two governed public source files, ran the
independent Python verifier, recomputed the two canonical preimage digests
with a separate Node implementation, decoded and hashed the public key, and
reconciled the resulting worktree against the thirteen parked paths.

Local did not access the password, DPAPI blob or private key and did not run
as Party A. No key promotion, T3E consumer wiring, candidate admission,
provider call, public sync or deployment occurred.

## Target / Source

| Source | Authority | Use |
|---|---|---|
| `governance/sources/verifier_key_registry/REGISTRY.json` | Party A operational Group 1 registry source | exact envelope, row, key and digest validation |
| `governance/sources/verifier_key_registry/LIFECYCLE_LOG.jsonl` | Party A append-only Group 1 lifecycle source | genesis transition and chain validation |
| `docs/audits/CVF_ACEL_G1_T3A_C2_CEREMONY_PRODUCT_LOCAL_VERIFICATION_2026-09-19.md` | previously verified public ceremony product | exact key, principal and timestamp authority |
| `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Group 1 schema and lifecycle contract | canonical preimages and tranche boundary |
| `governance/compat/check_acel_g1_verifier_key_registry.py` | Local read-only verifier | independent schema, topology, time and digest checks |

## Created Source Evidence

| Field | Verified value |
|---|---|
| registry file SHA-256 | `87594cdcf8a1e0c3c4b439434aeda39444ff54a432674d97403f1980c995d883` |
| lifecycle file SHA-256 | `dfaa1c175ee31b489550fe675aebbe79b10d782b48fe76c556d95880d3146579` |
| registry snapshot version | `1` |
| registry row count | `1` |
| key ID | `partya-44853ea9a690452c` |
| principal / actor | `LAM-RUBY\cvf-g1-party-a` |
| principal SID authority | `S-1-5-21-1644666849-912006174-747199667-1006` from the verified ceremony product |
| algorithm / role / status | `Ed25519` / `verificationAuthority` / `ACTIVE` |
| decoded public-key length | `32` bytes |
| public-key SHA-256 | `5ae2ddf8433e5eab54001d6fa59586389b9c3ae6956e1155dac811a3cbbcab01` |
| row hash | `4e94882407c73ab779ead5c2b05d6f67041ad5e9f138ef034e7c152dbe2229f9` |
| lifecycle entry hash | `dbda6b1cc20b77186f5f1c1896f60dc87cff8aab7ab35ed225ed417d06e19fae` |
| lifecycle edge | version `0 -> 1`; `NOT_PRESENT -> ACTIVE`; null prior hash |

The registry and lifecycle timestamps are identical at
`2026-09-20T01:17:10.1292599Z`. The row retains the exact verified ceremony
issuance and expiry strings. The public key bytes and digest match the prior
ceremony verification exactly.

## Independent Verification Evidence

| Check | Result |
|---|---|
| Local Python verifier over default governed paths | `PASS [VALIDATED]` |
| Node canonical registry-row recomputation | exact match: `4e94882407c73ab779ead5c2b05d6f67041ad5e9f138ef034e7c152dbe2229f9` |
| Node canonical lifecycle-entry recomputation | exact match: `dbda6b1cc20b77186f5f1c1896f60dc87cff8aab7ab35ed225ed417d06e19fae` |
| Node public-key decode and hash | 32 bytes; exact digest `5ae2ddf8433e5eab54001d6fa59586389b9c3ae6956e1155dac811a3cbbcab01` |
| topology | exactly one registry envelope row and one genesis lifecycle entry |
| worktree reconciliation | exactly two new source files in addition to the unchanged thirteen parked paths |

## Findings / Position

The two operational Group 1 sources are structurally valid, mutually
consistent, bound to the verified Party A ceremony product and cryptographically
self-authenticating under the T2F canonicalization contract. Group 1 therefore
advances from `SOURCE_NOT_CREATED` to `SOURCE_CREATED_LOCAL_VERIFIED`.

The first real attempt failed closed before output because PowerShell 7.5 date
coercion altered the comparison representation. Local repaired the parser and
real-parser regression at material commit `9846ca092`; its 56/56 PowerShell,
84/84 Python and 89/89 pre-commit results passed before the successful retry.

## Risk / Corrective Action

| Risk | Control |
|---|---|
| source creation mistaken for key promotion | retain key-promotion and candidate-evaluation dispositions as unverified/not authorized |
| Group 1 treated as sufficient for consumer wiring | T3E remains closed until T3A through T3D are independently verified |
| later lifecycle append breaks the chain | require the same Local checker and prior-entry hash continuity before accepting any transition |
| operational source bytes drift after verification | the two file hashes above are the closure anchors; any byte change reopens verification |
| runtime parser variance recurs | exact-date parsing now uses `-DateKind String` and the positive self-test traverses the real parser |

## Decision / Disposition

Decision: `ACCEPT_GROUP1_SOURCE_ESTABLISHMENT`.

Source disposition: `SOURCE_CREATED_LOCAL_VERIFIED`.

Candidate evaluation disposition: `UNVERIFIED`.

Key promotion disposition: `NOT_AUTHORIZED`.

T3E disposition: `NOT_OPEN`; T3B, T3C and T3D remain unverified.

The next governed move is a Local T3B readiness audit and route proposal.
Actual T3B creation still requires its separately named operator checkpoint;
this audit does not open that tranche automatically.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_acel_g1_verifier_key_registry.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | `PASS [VALIDATED]`; `SOURCE_CREATED_LOCAL_VERIFIED`; `successorTrancheOpened: NO`; `## Agent Operation Trace Block`; `DEFERRED_PRIVATE_ONLY` |
| gateRunPurpose | confirmation evidence after source inspection and independent recomputation |
| claimBoundary | checker evidence proves Group 1 source validity only, not promotion, admission or consumer wiring |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: the Party A writer would create exactly one
registry row and one genesis receipt whose independent recomputations matched.

Evidence Comparison: the successful retry matched that prediction exactly;
the earlier date-coercion attempt produced no files and was repaired before
the retry.

Contradiction Or Gap Disposition: the environment-specific parser gap was
encoded into the real-parser regression and closed before source acceptance.

Claim Update: Group 1 is now source-created and Local-verified; every downstream
promotion, admission and consumer-wiring claim remains withheld.

## Finding-To-Governance Learning Disposition

Disposition: ABSORB_INTO_EXISTING_OWNER.

The PowerShell date-coercion finding is absorbed in the existing T3A-C2 writer
and its hermetic self-test. It does not justify a new governance owner.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer |
| Provider or surface | private CVF workspace plus operator-executed Party A writer |
| Session or invocation | `acel-g1-t3a-c2-group1-source-local-verification-20260920` |
| Working directory | repository root |
| Command or tool surface | source reads, Local Python verifier, independent Node canonical recomputation, SHA-256 file hashing, Git status |
| Target paths | two Group 1 source files and this verification audit |
| Allowed scope source | active Party A operator checkpoint, T3A-C2 accepted tooling and T2F Group 1 contract |
| Before status evidence | material HEAD `9846ca092`; two governed source paths absent; thirteen parked paths unchanged |
| After status evidence | two governed source paths present and independently verified; thirteen parked paths unchanged |
| Diff evidence | `git status --short` shows only the two source files plus this audit beyond the same thirteen parked paths |
| Approval boundary | Local verification, bounded learning capture and material commit only |
| Claim boundary | Group 1 source establishment only; no promotion, admission, T3E, provider/live, public or deployment claim |
| Agent type | Local reviewer/closer |
| Invocation ID | `acel-g1-t3a-c2-source-verify-20260920` |
| Expected manifest | `governance/sources/verifier_key_registry/REGISTRY.json`; `governance/sources/verifier_key_registry/LIFECYCLE_LOG.jsonl`; this audit |
| Actual changed set | exact expected three-path manifest plus thirteen unchanged parked paths |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: principal-bound operational source evidence remains private provenance;
no public artifact or public-sync action is authorized.

## Claim Boundary

This audit proves only that the exact Group 1 registry and genesis lifecycle
source files present on 2026-09-20 satisfy the T2F contract and match the
verified Party A public product. It does not prove private-key possession by
Local, later lifecycle integrity, key promotion, candidate admission, T3E
consumer wiring, production readiness, public export or deployment.
