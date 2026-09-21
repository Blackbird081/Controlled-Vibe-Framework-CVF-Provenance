# CVF ACEL G1 T3B Group 2 Spec Local Verification

Memory class: governed-audit

Status: SPEC_CREATED_LOCAL_VERIFIED_PENDING_APPROVAL

Date: 2026-09-21

Owner: Local orchestrator/reviewer

successorTrancheOpened: NO

## Purpose

Record Local's independent verification of the operator-executed Party A
Group 2 `SPEC_v1.json` write and authorize only the later Approver `APPROVED`
decision checkpoint.

## Scope / Methodology

The operator executed the committed writer as the exact non-admin Party A
principal. Local then read the governed spec, decoded the fixed policy bytes,
recomputed the direct content digest, invoked the read-only Python record
validator for the closed-preimage digest and inspected the owner plus every
explicit DACL rule.

Local did not access the Party A password and did not run as Party A. The
Approver principal was not executed. No approval, activation, candidate
admission, T3E consumer wiring, provider call, public sync or deployment
occurred.

## Target / Source

| Source | Authority | Use |
|---|---|---|
| `governance/sources/verification_authority_spec/SPEC_v1.json` | Party A operational Group 2 spec source | exact record, policy bytes, author and digest validation |
| `docs/reviews/CVF_ACEL_G1_T3B_PRINCIPAL_POLICY_OPERATOR_DECISION_2026-09-20.md` | operator-approved principal and fixed policy | expected Party A, Approver and policy values |
| `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Group 2 schema and lifecycle contract | canonical preimage and source-state boundary |
| `governance/compat/check_acel_g1_verification_authority_spec.py` | Local read-only verifier | independent closed-schema and digest validation |

## Created Source Evidence

| Field | Verified value |
|---|---|
| spec file SHA-256 | `25920dc62d97b21cc2243356b25834218faf71e40d9ca3a91deac0f3e89226cc` |
| profile / domain | `cvf.source-record-canonicalization@1` / `cvf.specFile` |
| spec version | `1` |
| author SID | `S-1-5-21-1644666849-912006174-747199667-1006` |
| proposed at | `2026-09-21T04:05:45.4393129Z` |
| decoded policy length | `325` UTF-8 bytes |
| direct content hash | `e571ec25e17d8c3fd3f24a865be40777c63862c6aa695444acaa3bc54b599c6b` |
| closed record hash | `176c6450a0462a36686fdd1efa3fe2aa9c3ecf734598704483c2bcc66e26dd7e` |
| NTFS owner SID | `S-1-5-21-1644666849-912006174-747199667-1006` |
| inheritance | disabled (`AreAccessRulesProtected=True`) |
| Party A ACE | Allow FullControl; SID suffix `-1006` |
| Local ACE | Allow Read/Synchronize only; SID suffix `-1001` |
| Approver ACE | Allow Read/Synchronize only; SID suffix `-1008` |

The decoded policy is exactly:

```json
{"admissionRequiredLookupResult":"IDENTITY_CONFIRMED","authorityId":"ACEL_G1_DECISION_OWNER","authoritySpecSchema":"cvf.acel.g1.verificationAuthoritySpec@1","freshnessThresholdSeconds":86400,"issuerVerificationRequirement":"VERIFIED_BY_LIVE_REGISTRY_LOOKUP","receiptDomain":"cvf.verifierReceipt","receiptProfileVersion":"v1"}
```

## Independent Verification Evidence

| Check | Result |
|---|---|
| Python `validate_spec_file_record` with operational expected authorities | exact direct and record hashes returned |
| separate standard-library base64url decode plus SHA-256 | exact direct content hash match |
| fixed-policy byte comparison | exact operator-approved compact JSON; no BOM or trailing newline in decoded content |
| author and version | exact Party A SID; version `1` |
| DACL owner | exact Party A SID |
| DACL topology | protected and exactly three Allow ACEs; no unexpected or deny ACE |
| cross-principal rights | Local and Approver read-only; neither has write, append, delete, ownership or permission-change authority |
| decision source | absent, as required before the first Approver action |
| worktree reconciliation | exactly this new spec and verification audit beyond the unchanged thirteen parked paths |

The full operational checker intentionally remains fail-closed until
`ACTIVATION_DECISIONS.jsonl` exists. This receipt validates the spec-only phase;
it does not fabricate a full-source pass before the Approver chain begins.

## Findings / Position

The Group 2 v1 specification is structurally valid, byte-bound to the exact
operator-approved policy, authored and owned by the verified Party A principal,
and protected by the required cross-principal read-only DACL. The spec advances
to `SPEC_CREATED_LOCAL_VERIFIED_PENDING_APPROVAL`.

The first real attempt failed closed at a redundant owner rewrite. Local
verified complete rollback, corrected both writers at material commit
`5121004d4`, and the successful retry proves the corrected standard-principal
DACL path on this host. The correction is recorded in the R2 completion review.

## Risk / Corrective Action

| Risk | Control |
|---|---|
| spec creation mistaken for approval | permit only one `APPROVED` event after this receipt; activation remains closed |
| Approver receives mutation authority over Party A spec | DACL grants Approver read-only access and Local independently enumerated every ACE |
| policy or record bytes drift after verification | the file SHA-256 and both semantic digests above are closure anchors; any byte change reopens verification |
| full checker invoked before decision history exists | retain spec-only receipt now; run the full checker after each Approver append |
| prior standard-principal privilege defect recurs | both writers contain a machine regression rejecting `.SetOwner(` and verify the existing owner before DACL mutation |

## Decision / Disposition

Decision: `ACCEPT_GROUP2_SPEC_CREATION`.

Spec disposition: `SPEC_CREATED_LOCAL_VERIFIED_PENDING_APPROVAL`.

Approval disposition: `NOT_YET_CREATED`.

Activation disposition: `NOT_AUTHORIZED`.

Candidate evaluation disposition: `UNVERIFIED`.

T3E disposition: `NOT_OPEN`.

The next governed move is exactly one Approver `APPROVED` append targeting
spec version 1, followed by Local verification. `ACTIVATED` must not be appended
in the same operator step.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_acel_g1_verification_authority_spec.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | `SPEC_CREATED_LOCAL_VERIFIED_PENDING_APPROVAL`; `successorTrancheOpened: NO`; `## Agent Operation Trace Block`; `DEFERRED_PRIVATE_ONLY` |
| gateRunPurpose | confirmation evidence after source inspection and independent digest/DACL recomputation |
| claimBoundary | spec-only validation cannot replace decision-history approval or activation validation |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: the corrected Party A writer would create one
v1 spec with the exact fixed policy, two matching digests, Party A ownership
and read-only Local/Approver grants.

Evidence Comparison: the successful retry matched every predicted field,
digest and DACL rule. The earlier privilege failure left no durable output.

Contradiction Or Gap Disposition: the environment-specific owner-rewrite gap
is absorbed into both writers and their machine regressions; the real retry
closes the host-specific proof gap for the Party A writer.

Claim Update: the Group 2 spec is created and Local-verified; approval,
activation and every downstream claim remain withheld.

## Finding-To-Governance Learning Disposition

Disposition: ABSORB_INTO_EXISTING_OWNER.

The standard-principal owner-rewrite finding is absorbed into both existing
Group 2 writers and their self-tests. The root rule is machine-enforced where
the defect occurred: verify creator ownership and mutate only the DACL.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer |
| Provider or surface | private CVF workspace plus operator-executed Party A writer |
| Session or invocation | `acel-g1-t3b-group2-spec-local-verification-20260921` |
| Working directory | repository root |
| Command or tool surface | source read, standard-library decode/hash, Local Python record validator, Get-Acl SID/right inspection, SHA-256 file hash and Git status |
| Target paths | `governance/sources/verification_authority_spec/SPEC_v1.json`; this verification audit |
| Allowed scope source | active Party A operator checkpoint, accepted T3B tooling and T2F Group 2 contract |
| Before status evidence | material HEAD `5121004d4`; both governed Group 2 source paths absent after failed-attempt rollback |
| After status evidence | v1 spec present and independently verified; decisions path absent; thirteen parked paths unchanged |
| Diff evidence | `git status --short` shows only the spec and this audit beyond the same thirteen parked paths |
| Approval boundary | Local spec verification, bounded learning capture and material commit only |
| Claim boundary | spec creation only; no approval, activation, admission, T3E, provider/live, public or deployment claim |
| Agent type | Local reviewer/closer |
| Invocation ID | `acel-g1-t3b-group2-spec-verify-20260921` |
| Expected manifest | spec plus this audit |
| Actual changed set | exact expected two-path manifest plus thirteen unchanged parked paths |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: principal-bound operational source evidence remains private provenance;
no public artifact or public-sync action is authorized.

## Claim Boundary

This audit proves only that the exact Group 2 v1 spec present on 2026-09-21
satisfies the T2F spec contract, matches the approved policy and has the required
owner/DACL boundary. It does not prove approval, activation, later decision-chain
integrity, candidate admission, T3E consumer wiring, production readiness,
public export or deployment.
