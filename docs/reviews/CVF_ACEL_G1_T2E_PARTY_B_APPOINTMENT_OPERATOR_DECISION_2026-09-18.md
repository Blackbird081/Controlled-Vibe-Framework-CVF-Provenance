# CVF ACEL G1 T2E Party B Appointment Operator Decision

Memory class: governed-local-decision

docType: review

Status: PARTY_B_APPOINTED_SOURCE_ESTABLISHMENT_PENDING

Date: 2026-09-18

Decision owner: operator for appointment; Local orchestrator/reviewer for technical recording

Decision base HEAD: `7bccba422ffd311adf31390bcc3dfeaa86abdd56`

## Purpose

Record the operator's appointment of `CVF Independent Registry Observer /
dedicated separate audit identity` as Party B, the
`RegistryObservationOwner`. Bind the role to independent observation of both
the verifier public-key registry and the future issuer registry while
preserving separation from every writer of either registry.

## Target / Source

| Source | Verified locator | Use |
|---|---|---|
| `docs/audits/CVF_ACEL_G1_T2E_FOUR_OWNER_SOURCE_CONTRACT_DESIGN_2026-09-18.md` | Contract 3; Cross-Contract Separation Matrix, Cases 1 and 3 | Party B duties, append-only evidence and writer/observer separation |
| `docs/reviews/CVF_ACEL_G1_T2E_PARTY_A_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` | Party A Appointment Contract; Decision / Disposition | establishes Party A as key-registry writer and forbids Party A from Party B |
| operator instruction, 2026-09-18 | affirmative approval of the recommended Party B identity | appointment authority; not operational-source evidence |

## Scope / Methodology

Role: Local orchestrator/reviewer. Phase: sequential actual-party appointment,
step 2 of 3. The operator owns appointment authority; Local checks role
separation, scope, claim boundaries and consistency with the accepted T2E
contract design. No external research or worker execution applies.

Local consumed the accepted T2E evidence rather than recreating the design.
The proposed Party B identity was checked against the appointed Party A and
the still-pending Party C boundary. The appointment is accepted only with the
credential, write-authority and append-only restrictions below.

## Findings / Position

`CVF Independent Registry Observer / dedicated separate audit identity` is an
appropriate accountable role for Contract 3 because its identity and future
credentials are required to remain distinct from Party A and Party C. One
Party B may cover both registries, as the design expressly permits, provided
it remains separate from both registry writers and the operator records that
scope explicitly. This decision records that two-registry scope.

T2H amendment note: the operator confirmed retaining this appointment while
replacing the same-`snapshotId` correction-chaining condition below with
immutable, write-once new-ID observation, per
`docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md`
(Immutable Snapshot Identity, T2G-01 through T2G-05) and
`docs/reviews/CVF_ACEL_G1_T2H_PARTY_B_IMMUTABLE_OBSERVATION_RECONCILIATION_WORKER_RETURN_2026-09-18.md`.
Party B's identity, two-registry scope and independence from Party A and
Party C are unchanged by this amendment.

Party B may append new original observation records, each under its own
freshly generated, globally unique `snapshotId`, to a future
observation-log store. If an earlier observation is later found erroneous or
the observed registry content genuinely changes, Party B records the new
observation under a brand-new `snapshotId` rather than correcting,
superseding, or in any way rewriting the earlier record; the earlier record
remains durable and unchanged. Party B may not write, rotate, revoke or
correct entries in either observed registry; mutate, delete, alias or
reclassify any existing observation record under any `snapshotId`; use
Party A or Party C write credentials; or treat its appointment as proof that
the observation store or any registry already exists.

The words `dedicated separate audit identity` are a binding identity and
credential-separation requirement. Before operational use, the later source-
establishment packet must identify the concrete account or principal and
prove that it cannot exercise either registry writer's permissions.

## Party B Appointment Contract

| Field | Appointment value |
|---|---|
| Actual party identity | `CVF Independent Registry Observer / dedicated separate audit identity` |
| Party position | Party B |
| Owned responsibility | Contract 3 `RegistryObservationOwner` |
| Observation scope | verifier public-key registry and future issuer registry |
| Allowed write surface | future append-only observation-log store only |
| Required independence | separate identity and credentials from Party A and Party C; no registry mutation permission |
| Forbidden combination | Party A; Party C; writer of either observed registry |
| Correction behavior | none for an existing `snapshotId`; a new observation, including after an error or content change, is always recorded under a brand-new `snapshotId` as a new original record; never rewrite, delete, alias, or reclassify a prior record (amended by T2H; supersedes the prior same-ID correction-chaining condition) |
| Required operational proof | concrete principal, governed log path, tamper evidence, consumer read, permission-separation evidence and Local verification |
| Contract 2 activation authority | not granted by this appointment; independent approver remains pending |
| Operational source state | `SOURCE_ESTABLISHMENT_PENDING` |
| Candidate admission state | `UNVERIFIED` |

Appointment acceptance is bounded by every row. A later change that gives
Party B mutation rights over an observed registry, merges it with either
registry writer, or removes append-only, write-once new-ID observation
integrity (for example by permitting an in-place rewrite, deletion, alias, or
same-`snapshotId` correction of an existing observation record) invalidates
this appointment for independent-observation evidence. The T2H amendment
removing the same-`snapshotId` correction-chaining condition, by contrast,
does not invalidate this appointment: the operator affirmatively confirmed
that specific replacement, and Party B's identity, independence and
append-only integrity are unchanged by it.

## Decision / Disposition

Decision: `APPOINT_DEDICATED_SEPARATE_AUDIT_IDENTITY_AS_PARTY_B_BOUNDED`.

Party B identity is no longer pending. Party A remains the appointed owner of
combined Contracts 1+2. Party C remains
`IDENTITY_PENDING_OPERATOR_APPOINTMENT`. The independent Contract 2
activation approver also remains pending and is not implied by this Party B
appointment.

Party B may participate in later governed source-establishment design and
accept accountable observation duties. It may not provision credentials,
create an observation store, observe a live registry, append a receipt, run a
lookup or admit a candidate without a separately authorized implementation
packet and the required operational evidence.

Operational sources remain `BLOCKED_SOURCE_NOT_FOUND`; appointment alone is
not source verification. The next sequential operator checkpoint is Party C,
the `IssuerRegistryAuthorityOwner`.

## Risk / Corrective Action

| Risk | Control |
|---|---|
| a role label is mistaken for a provisioned independent principal | require concrete principal and permission-separation evidence before operational use |
| Party B gains registry mutation permissions | invalidate observation independence and reject candidate admission |
| Party B and Party C become the same identity | prohibit the combination for issuer-registry observation |
| observation history is edited in place | require append-only, write-once new-ID observation (a fresh record under a brand-new `snapshotId`, never a same-ID correction) and tamper evidence |
| Party B appointment is mistaken for an existing log or live observation | keep source establishment pending and admission unverified |
| Party B is silently treated as Contract 2 activation approver | preserve that authority as separately pending |

## Negative Search And Collision Discipline

No new exhaustive search is claimed. This appointment reuses the accepted T2E
search evidence and the bounded Party A decision. Exact prior search command:

```
rg -n --hidden --no-ignore -i 'ACEL-G1-T2E|VerifierKeyAndRegistryControlOwner|VerificationAuthoritySpecificationOwner|RegistryObservationOwner|IssuerRegistryAuthorityOwner|PROPOSED_OPERATOR_DECISION|BLOCKED_SOURCE_NOT_FOUND|UNVERIFIED' docs governance EXTENSIONS ECOSYSTEM CVF_SESSION -g '*.md' -g '*.json' -g '*.py' -g '*.ts'
```

Search roots covered `docs`, `governance`, `EXTENSIONS`, `ECOSYSTEM` and
`CVF_SESSION`. External evidence was inapplicable. Absent-versus-collision
disposition: governed appointment evidence now exists for Party A and Party B.
Party C identity, operational sources and a provisioned observer principal
remain `IDENTITY_PENDING_OPERATOR_APPOINTMENT` or
`SOURCE_ESTABLISHMENT_PENDING`, as applicable. Design/status matches remain
non-authoritative for runtime proof.

- Same-token collision `ACEL-G1-T2E`: governed tranche identifier;
  non-authoritative for operational readiness.
- Same-token collision `VerifierKeyAndRegistryControlOwner`: Contract 1 name;
  it identifies Party A responsibility and grants Party B no registry-write
  authority.
- Same-token collision `VerificationAuthoritySpecificationOwner`: Contract 2
  name; it grants Party B no specification or activation authority.
- Same-token collision `RegistryObservationOwner`: Contract 3 name; this
  decision supplies the bounded appointment but not an observation-log source.
- Same-token collision `IssuerRegistryAuthorityOwner`: Party C contract name;
  non-authoritative for a Party C appointment or issuer registry.
- Same-token collision `PROPOSED_OPERATOR_DECISION`: earlier planning status;
  non-authoritative for operational source establishment.
- Same-token collision `BLOCKED_SOURCE_NOT_FOUND`: generic source status; its
  occurrences are non-authoritative for Party B operational evidence.
- Same-token collision `UNVERIFIED`: generic admission state; its occurrences
  are non-authoritative for candidate admission.
- Same-token collision `CVF_SESSION` and `ECOSYSTEM`: search-root names;
  non-authoritative for Party B operational evidence.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | `internal governed input (no external intake)` |
| Chain map route | accepted T2E contract -> Party A boundary -> operator Party B approval -> Local appointment record |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this Local appointment decision |
| Internal source | `docs/reviews/CVF_ACEL_G1_T2E_PARTY_A_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` |
| Disposition | `NOT_APPLICABLE_INTERNAL_ONLY_WITH_REASON`: no external source was admitted |
| Claim boundary | appointment evidence is not principal, log, registry, observation or runtime evidence |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: appointing a dedicated audit identity as Party B
would resolve Contract 3 accountability while leaving principal provisioning,
the append-only store, Party C, independent Contract 2 activation approval and
candidate admission unresolved.

Evidence Comparison: confirmed. The accepted design permits one observer for
both registries only when it is distinct from both writers, and the approved
identity expressly binds that separation.

Contradiction Or Gap Disposition: the role is appointed but its concrete
principal and permissions do not yet exist as governed evidence; the gap stays
fail-closed under `SOURCE_ESTABLISHMENT_PENDING`.

Claim Update: Party B is appointed for both-registry observation; operational
observation and every remaining authority claim stay pending.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_core_guard_self_protection.py` |
| literalTokensReviewed | review heading groups; routing table rows; epistemic comparison; trace labels; corpus reconciliation; protected-path authorization labels |
| gateRunPurpose | confirmation of bounded Party B appointment evidence, not operational observation proof |
| claimBoundary | checker conformity is not principal, store, registry, observation or admission evidence |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: read-only changed-set accounting for the
two pre-existing parked protected checker paths while recording Party B. No
checker mutation is authorized.

Protected paths: `governance/compat/check_task_class_calibration_owner_evidence.py`;
`governance/compat/test_check_task_class_calibration_owner_evidence.py`.

Operator authorization: affirmative approval of the recommended Party B.
Rollback boundary: revert only this appointment record if rejected; preserve
prior T2E material, continuity and all thirteen parked paths.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer |
| Provider or surface | private CVF workspace |
| Session or invocation | sequential Party B appointment, 2026-09-18 |
| Working directory | repository root |
| Command or tool surface | governed reads, Git status, `apply_patch`, governance gates and Git |
| Target paths | this Party B appointment decision |
| Allowed scope source | operator affirmative Party B appointment instruction |
| Before status evidence | HEAD `7bccba422`; thirteen parked untracked paths; staging empty |
| After status evidence | Party B appointment record only; parked paths unchanged |
| Diff evidence | exact one-path material manifest before staging |
| Approval boundary | Party B appointment only |
| Claim boundary | no principal provisioning, source establishment, registry mutation, observation, activation, implementation, runtime or public effect |
| Agent type | Local decision recorder/reviewer |
| Invocation ID | `acel-g1-t2e-party-b-appointment-20260918` |
| Expected manifest | this Party B appointment record |
| Actual changed set | `docs/reviews/CVF_ACEL_G1_T2E_PARTY_B_APPOINTMENT_OPERATOR_DECISION_2026-09-18.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | none |

## Corpus Completeness And Report Integrity

- Corpus task class: bounded appointment decision over two named governed
  inputs and one operator instruction; no complete-repository claim.
- Corpus root: the two governed paths in Target / Source.
- Snapshot time: 2026-09-18 at decision base HEAD.
- Enumeration command: filesystem-backed direct reads of the two governed
  paths listed in Target / Source.
- Manifest artifact or inline manifest: Target / Source table.
- Manifest hash: N/A with reason: bounded named-input decision.
- Processing ledger artifact or inline ledger: both governed paths READ;
  operator instruction classified SCOPE_AUTHORITY_NOT_SOURCE_PROOF.
- Allowed terminal statuses: `READ`, `SKIPPED_WITH_REASON`, `DEFERRED`,
  `BLOCKED_UNREADABLE`.
- Reconciliation: manifest=2; ledger_terminal=2; exclusions=0; unreadable=0; unresolved=0.
- Unresolved files: zero among the two named governed inputs.
- Declared exclusions: all other repository paths and external sources.
- Unreadable or unsupported files: none.
- Aggregation check: 2 = 2 + 0 + 0.
- Drift check: exact decision base recorded.
- Output traceability: this appointment record.
- Adversarial verification: Party B appointment cannot count as a principal,
  append-only store, registry snapshot or independent observation receipt.
- Corpus verdict: PARTIAL

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | Party B actual-role appointment for both-registry observation |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: no runtime or observation receipt is claimed |
| actionEvidence | ACTION_EVIDENCE_PRESENT: operator appointment and Local recording only |
| invocationBoundary | governed local documentation and Git workflow |
| interceptionBoundary | no IDE, provider, CLI/MCP or runtime interception claim |
| claimLanguage | Party B appointed; principal, sources and observations remain fail-closed |
| forbiddenExpansion | registry mutation, Party A or Party C identity, Contract 2 activation, source creation, live observation, lookup, admission, runtime, public sync, deployment |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private appointment record with no public-sync authorization.

## Claim Boundary

This record appoints `CVF Independent Registry Observer / dedicated separate
audit identity` as Party B for Contract 3 and scopes it to both future
registries. It establishes no concrete principal, credentials, permission
boundary, observation-log store, registry, snapshot, observation receipt,
Contract 2 activation, candidate admission, implementation, runtime or public
authority. Party C and an independent Contract 2 activation approver remain
pending.
