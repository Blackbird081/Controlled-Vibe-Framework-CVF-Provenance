# CVF ACEL G1 T3B Group 2 Approval Local Verification

Memory class: governed-audit

Status: APPROVED_LOCAL_VERIFIED_PENDING_ACTIVATION

Date: 2026-09-21

Owner: Local orchestrator/reviewer

successorTrancheOpened: NO

## Purpose

Record Local's independent verification of the operator-executed Approver
`APPROVED` append for Group 2 specification version 1 and authorize only the
later, separately executed `ACTIVATED` event.

## Scope / Methodology

The operator executed the committed decision writer as the exact non-admin
Approver principal. Local then inspected the durable decision row, rebuilt its
closed canonical preimage without using the writer, recomputed its SHA-256
digest, ran the read-only operational checker against the real source pair,
and inspected the decision file owner plus every explicit DACL rule.

Local did not access the Approver password and did not run as the Approver.
No activation, candidate admission, T3E consumer wiring, provider call,
public sync or deployment occurred.

## Target / Source

| Source | Authority | Use |
|---|---|---|
| `governance/sources/verification_authority_spec/SPEC_v1.json` | Local-verified Party A Group 2 specification | immutable target and independently recomputed policy hash |
| `governance/sources/verification_authority_spec/ACTIVATION_DECISIONS.jsonl` | Approver-owned append-only decision source | exact event, chain, principal and digest validation |
| `docs/audits/CVF_ACEL_G1_T3B_GROUP2_SPEC_LOCAL_VERIFICATION_2026-09-21.md` | prior Local phase receipt | authority to append exactly one `APPROVED` event |
| `governance/compat/check_acel_g1_verification_authority_spec.py` | Local read-only verifier | closed-schema, per-version hash, chain and state-machine validation |

## Approval Evidence

| Field | Verified value |
|---|---|
| event type | `APPROVED` |
| target spec version | `1` |
| decision event ID | `bda918b1-02e8-49c3-b720-35b1ef6a61d0` |
| Approver SID | `S-1-5-21-1644666849-912006174-747199667-1008` |
| decided at | `2026-09-21T04:15:46.9856421Z` |
| prior entry hash | JSON `null` (genesis) |
| recomputed spec hash | `e571ec25e17d8c3fd3f24a865be40777c63862c6aa695444acaa3bc54b599c6b` |
| entry hash | `30a6717c42d198c28743e54ed3304bd48c2769b606ea6f80d270afbbfbe8ba58` |
| decision file SHA-256 | `95cb198679e8036bf3ea44e43ace03e434d62f74701ca3162e7c5e73a6039135` |
| decision file shape | one compact JSON line; 461 bytes; terminal LF |
| spec file SHA-256 | `25920dc62d97b21cc2243356b25834218faf71e40d9ca3a91deac0f3e89226cc` (unchanged) |

## Independent Verification Evidence

| Check | Result |
|---|---|
| operational Python checker | `PASS [VALIDATED]`; one event; v1 first decision `APPROVED`; activated `False`; currently active `False`; active set empty |
| independent canonical preimage | injected exact profile/domain plus the nine closed event fields; compact sorted UTF-8 length 460 bytes |
| independent SHA-256 | `30a6717c42d198c28743e54ed3304bd48c2769b606ea6f80d270afbbfbe8ba58`, exactly matching the stored entry hash |
| chain genesis | `priorEntryHashHex=null`; no preceding or duplicate event |
| per-version binding | event `recomputedHashHex` exactly matches the independently verified v1 spec content hash |
| principal separation | Approver SID suffix `-1008` differs from Party A author SID suffix `-1006`; self-approval absent |
| Approver account posture | enabled, password required and not a member of local Administrators |
| NTFS owner SID | `S-1-5-21-1644666849-912006174-747199667-1008` |
| inheritance | disabled (`AreAccessRulesProtected=True`) |
| Approver ACE | Allow FullControl; SID suffix `-1008` |
| Local ACE | Allow Read/Synchronize only; SID suffix `-1001` |
| Party A ACE | absent; Party A has no explicit modification right on the decision source |

The initially attempted ad-hoc digest used only stored JSON members and
therefore omitted the canonical preimage's injected `profile` and `domain`.
It was rejected, not treated as evidence. The corrected independent
calculation followed the closed-preimage contract and matched the durable
digest exactly. This distinction is recorded to prevent a false mismatch or
an accidental relaxation of the canonicalization contract.

## Findings / Position

The sole durable decision row is structurally valid, cryptographically bound
to the unchanged v1 specification, authored and owned by the verified
Approver, and protected by the required principal-separated DACL. The state
machine correctly reports an approved but inactive version with an empty
active set.

There are no approval-phase rework findings. The source advances to
`APPROVED_LOCAL_VERIFIED_PENDING_ACTIVATION`.

## Risk / Corrective Action

| Risk | Control |
|---|---|
| approval mistaken for activation | retain an empty active set and authorize a separate `ACTIVATED` append only after this receipt |
| duplicate approval or rejection | writer and checker reject a second first-decision event for v1 |
| decision detached from spec bytes | every event carries the independently recomputed v1 spec hash |
| Party A mutates Approver history | decision DACL contains no Party A ACE and is protected from inheritance |
| canonical hash recomputed from stored shape alone | inject canonical profile/domain and use the exact closed field list before hashing |

## Decision / Disposition

Decision: `ACCEPT_GROUP2_APPROVAL_EVENT`.

Spec disposition: `SPEC_CREATED_LOCAL_VERIFIED`.

Approval disposition: `APPROVED_LOCAL_VERIFIED_PENDING_ACTIVATION`.

Activation disposition: `NOT_YET_CREATED`.

Candidate evaluation disposition: `UNVERIFIED`.

T3E disposition: `NOT_OPEN`.

The next governed move is exactly one separate Approver `ACTIVATED` append
targeting spec version 1, followed by Local verification. No candidate or
consumer action is authorized by this approval receipt.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_acel_g1_verification_authority_spec.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | `APPROVED_LOCAL_VERIFIED_PENDING_ACTIVATION`; `successorTrancheOpened: NO`; `## Agent Operation Trace Block`; `DEFERRED_PRIVATE_ONLY` |
| gateRunPurpose | validate the approval receipt and exact source pair before activation is opened |
| claimBoundary | approval validation cannot replace a later activation event or Local activation verification |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: one genesis `APPROVED` event would bind to v1,
be signed by identity through the Approver SID and filesystem boundary, leave
the active set empty, and grant mutation rights only to the Approver.

Evidence Comparison: the real source pair and OS ACL matched every prediction.
The independent closed-preimage digest matched the stored event digest.

Contradiction Or Gap Disposition: the first ad-hoc calculation omitted the
canonical injected fields and was invalid evidence; applying the documented
closed preimage resolved the discrepancy without changing source data or
checker behavior.

Claim Update: Group 2 v1 is approved and Local-verified but remains inactive;
all downstream claims remain withheld.

## Finding-To-Governance Learning Disposition

Disposition: NO_NEW_RULE_REQUIRED.

The discarded ad-hoc hash attempt was a reviewer procedure correction already
covered by the closed-preimage contract and checker. It did not reveal a
source or tooling defect and does not justify a new governance surface.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer |
| Provider or surface | private CVF workspace plus operator-executed Approver writer |
| Session or invocation | `acel-g1-t3b-group2-approval-local-verification-20260921` |
| Working directory | repository root |
| Command or tool surface | operational checker, independent standard-library canonical hash, Get-LocalUser, local Administrators membership probe, Get-Acl, Get-FileHash and Git status |
| Target paths | `governance/sources/verification_authority_spec/ACTIVATION_DECISIONS.jsonl`; this verification audit |
| Allowed scope source | prior Local spec receipt, accepted T3B tooling and operator approval checkpoint |
| Before status evidence | HEAD `9ffb81f88`; v1 spec committed and decision path absent |
| After status evidence | one Approver-owned `APPROVED` row independently verified; thirteen parked paths unchanged |
| Diff evidence | Git status contains exactly the decision source and this audit beyond the unchanged thirteen parked paths |
| Approval boundary | Local approval verification, material commit and opening of the separate activation checkpoint only |
| Claim boundary | no activation, admission, T3E, provider/live, public or deployment claim |
| Agent type | Local reviewer/closer |
| Invocation ID | `acel-g1-t3b-group2-approval-verify-20260921` |
| Expected manifest | decision source plus this approval audit |
| Actual changed set | exact expected two-path manifest plus thirteen unchanged parked paths |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: principal-bound operational decision evidence remains private
provenance; no public artifact or public-sync action is authorized.

## Claim Boundary

This audit proves only that the single Group 2 v1 `APPROVED` event present on
2026-09-21 satisfies the decision-event schema, digest chain, principal and
DACL contract and leaves v1 approved but inactive. It does not prove
activation, candidate admission, T3E consumer wiring, production readiness,
public export or deployment.
