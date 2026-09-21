# CVF ACEL G1 T3B Group 2 Activation Local Verification

Memory class: governed-audit

Status: ACTIVATED_LOCAL_VERIFIED_PENDING_CONSUMER_BINDING

Date: 2026-09-21

Owner: Local orchestrator/reviewer

successorTrancheOpened: NO

## Purpose

Record Local's independent verification of the separately executed Group 2
v1 `ACTIVATED` decision and close T3B's principal-bound creation ceremony
without overstating the T2F source-establishment checklist.

## Scope / Methodology

The operator executed the committed decision writer as the exact non-admin
Approver principal. Local then replayed both durable decision rows, rebuilt
both closed canonical preimages without using the writer, recomputed both
SHA-256 digests and their link, ran the read-only operational checker against
the real source pair, and re-inspected the decision file owner and DACL.

Local did not access the Approver password and did not run as the Approver.
No consumer was wired, no candidate was evaluated, and no provider, live,
runtime, public-sync or deployment action occurred.

## Target / Source

| Source | Authority | Use |
|---|---|---|
| `governance/sources/verification_authority_spec/SPEC_v1.json` | Local-verified Party A Group 2 specification | active version content and exact policy hash |
| `governance/sources/verification_authority_spec/ACTIVATION_DECISIONS.jsonl` | Approver-owned append-only decision source | approval/activation chain, state and digest validation |
| `docs/audits/CVF_ACEL_G1_T3B_GROUP2_APPROVAL_LOCAL_VERIFICATION_2026-09-21.md` | prior Local phase receipt | authority to append exactly one `ACTIVATED` event |
| `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Group 2 lifecycle and establishment contract | unique-active replay and remaining consumer-binding condition |
| `governance/compat/check_acel_g1_verification_authority_spec.py` | Local read-only verifier | closed schema, per-version hash, chain and full state-machine validation |

## Activation Evidence

| Field | Verified value |
|---|---|
| event type | `ACTIVATED` |
| target spec version | `1` |
| decision event ID | `be990b0e-f7d4-4ae5-9f7c-8ef39df6d203` |
| Approver SID | `S-1-5-21-1644666849-912006174-747199667-1008` |
| decided at | `2026-09-21T04:42:34.1201717Z` |
| prior entry hash | `30a6717c42d198c28743e54ed3304bd48c2769b606ea6f80d270afbbfbe8ba58` |
| recomputed spec hash | `e571ec25e17d8c3fd3f24a865be40777c63862c6aa695444acaa3bc54b599c6b` |
| activation entry hash | `a29535f9c71a2dabbe9dae041bcc731db02b67005df6fbca837263d1f7dc7805` |
| decision file SHA-256 | `a5646713ec8641c2339e3e8c5ca49c9dbb2e234487337db36c222fa3f10351ed` |
| decision file shape | two compact JSON lines; 985 bytes; terminal LF |
| active set after replay | exactly `{1}` |

## Independent Verification Evidence

| Check | Result |
|---|---|
| operational Python checker | `PASS [VALIDATED]`; two events; v1 first decision `APPROVED`; activated `True`; superseded `False`; currently active `True`; active set `[1]` |
| approval preimage/digest | independent 460-byte compact sorted UTF-8 preimage recomputed to `30a6717c42d198c28743e54ed3304bd48c2769b606ea6f80d270afbbfbe8ba58` |
| activation preimage/digest | independent 523-byte compact sorted UTF-8 preimage recomputed to `a29535f9c71a2dabbe9dae041bcc731db02b67005df6fbca837263d1f7dc7805` |
| exact chain link | activation `priorEntryHashHex` equals the recomputed/stored approval entry hash |
| event order and identity | exactly `APPROVED`, then `ACTIVATED`; two distinct event IDs; no rejected, duplicate or superseded event |
| per-version binding | both events bind to the independently verified v1 raw-content hash |
| principal separation | Approver SID suffix `-1008` differs from Party A author SID suffix `-1006` |
| NTFS owner | `LAM-RUBY\cvf-g1-approver` / SID suffix `-1008` |
| inheritance | disabled (`AreAccessRulesProtected=True`) |
| Approver ACE | Allow FullControl; SID suffix `-1008` |
| Local ACE | Allow Read/Synchronize only; SID suffix `-1001` |
| Party A ACE | absent; Party A has no explicit modification right on decision history |

## Establishment Checklist Reconciliation

| T2F Group 2 condition | Evidence | Disposition |
|---|---|---|
| spec document path exists | immutable `SPEC_v1.json`, independently verified and committed | SATISFIED |
| active event exists and approver differs from author | two-event chain above; SIDs `-1008` and `-1006` | SATISFIED |
| at least one verifier consumer binds to resulting hash | T3E consumer wiring remains unopened | PENDING_T3E |
| Local independently recomputes hash and confirms match | direct spec digest plus both event digests independently recomputed | SATISFIED |
| unique-active invariant holds | full replay yields exactly active set `{1}` | SATISFIED |

Therefore T3B's creation and activation ceremony is complete, but the broader
T2F `SOURCE_ESTABLISHED` claim remains withheld until T3E provides actual
consumer-binding evidence.

## Findings / Position

The activation event is valid and extends the previously accepted approval
row without mutation. Version 1 is the only active Group 2 specification and
is bound to the exact operator-approved policy hash.

There are no activation-phase rework findings. T3B closes as
`ACTIVATED_LOCAL_VERIFIED_PENDING_CONSUMER_BINDING`.

## Risk / Corrective Action

| Risk | Control |
|---|---|
| active event mistaken for full source establishment | retain the explicit `PENDING_CONSUMER_BINDING` qualifier until T3E reads and binds the active hash |
| a second ordinary activation creates conflicting active versions | full-history replay requires an empty active set before ordinary activation; future rotation requires atomic `SUPERSEDED` |
| chain history is rewritten | preserve append-only decision history and verify every prior hash before consuming it |
| activation treated as candidate admission | Groups 3/4 and T3E remain absent; candidate status remains `UNVERIFIED` |

## Decision / Disposition

Decision: `ACCEPT_GROUP2_ACTIVATION_EVENT`.

T3B disposition: `ACTIVATED_LOCAL_VERIFIED_PENDING_CONSUMER_BINDING`.

Active specification: version `1`, hash
`e571ec25e17d8c3fd3f24a865be40777c63862c6aa695444acaa3bc54b599c6b`.

T2F source-establishment disposition: `PENDING_T3E_CONSUMER_BINDING`.

Candidate evaluation disposition: `UNVERIFIED`.

Successor disposition: `NOT_AUTOMATICALLY_OPENED`; Local must separately
audit T3C readiness before any Group 3 work order or Party B execution.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_acel_g1_verification_authority_spec.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | `ACTIVATED_LOCAL_VERIFIED_PENDING_CONSUMER_BINDING`; `successorTrancheOpened: NO`; `## Agent Operation Trace Block`; `DEFERRED_PRIVATE_ONLY` |
| gateRunPurpose | validate the activation receipt and prevent a premature source-establishment claim |
| claimBoundary | valid active Group 2 history is necessary but not sufficient for T2F establishment without T3E binding |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: the separate activation append would preserve
the approval row, link to its exact digest, bind the same v1 content hash and
change the full-history active set from empty to exactly `{1}`.

Evidence Comparison: the durable file and two independent validation paths
matched every prediction; owner and DACL remained unchanged.

Contradiction Or Gap Disposition: no activation contradiction exists. The one
remaining T2F checklist gap is named consumer binding, which belongs to T3E
and is not fabricated here.

Claim Update: v1 is active and Local-verified; full Group 2 establishment,
consumer wiring and candidate admission remain withheld.

## Finding-To-Governance Learning Disposition

Disposition: NO_NEW_RULE_REQUIRED.

The activation behaved exactly as the corrected atomic state-machine contract
and existing machine checks require. No new defect class or repeated failure
was observed.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer |
| Provider or surface | private CVF workspace plus operator-executed Approver writer |
| Session or invocation | `acel-g1-t3b-group2-activation-local-verification-20260921` |
| Working directory | repository root |
| Command or tool surface | operational checker, independent standard-library canonical hash-chain replay, Get-Acl, Get-FileHash and Git status |
| Target paths | `governance/sources/verification_authority_spec/ACTIVATION_DECISIONS.jsonl`; this verification audit |
| Allowed scope source | prior Local approval receipt, committed activation launcher and T2F Group 2 contract |
| Before status evidence | material HEAD `961b7e17a` with one Local-verified APPROVED row and activation checkpoint routed at `b9f0e0928` |
| After status evidence | two-event APPROVED-to-ACTIVATED chain independently verified; exactly v1 active; thirteen parked paths unchanged |
| Diff evidence | Git status contains exactly the modified decision source and this audit beyond the unchanged thirteen parked paths |
| Approval boundary | Local activation verification and material commit only |
| Claim boundary | no T3E consumer binding, full source-establishment, admission, provider/live, public or deployment claim |
| Agent type | Local reviewer/closer |
| Invocation ID | `acel-g1-t3b-group2-activation-verify-20260921` |
| Expected manifest | updated decision source plus this activation audit |
| Actual changed set | exact expected two-path manifest plus thirteen unchanged parked paths |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: principal-bound operational activation evidence remains private
provenance; no public artifact or public-sync action is authorized.

## Claim Boundary

This audit proves that Group 2 version 1 has one valid approval followed by
one valid activation, is the unique active version, and satisfies the
principal, digest-chain and DACL contract. It does not prove T3E consumer
binding, complete T2F source establishment, candidate admission, production
readiness, public export or deployment.
