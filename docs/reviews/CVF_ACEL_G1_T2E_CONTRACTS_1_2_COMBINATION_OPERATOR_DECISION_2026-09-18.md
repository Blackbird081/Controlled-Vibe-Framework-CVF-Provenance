# CVF ACEL G1 T2E Contracts 1+2 Combination Operator Decision

Memory class: governed-local-decision

docType: review

Status: OPERATOR_TOPOLOGY_APPROVED_IDENTITY_PENDING

Date: 2026-09-18

Decision owner: operator for responsibility combination and actual-party appointment; Local orchestrator/reviewer for technical recording

Decision base HEAD: `2e3d3a226d1118be4f758879619a99e9be7ae784`

## Purpose

Record the operator's explicit approval to combine Contract 1,
`VerifierKeyAndRegistryControlOwner`, with Contract 2,
`VerificationAuthoritySpecificationOwner`, under one future actual accountable
party. Preserve the independence rules for Contracts 3 and 4 and distinguish
topology approval from actual-party appointment.

## Target / Source

| Source | Verified locator | Use |
|---|---|---|
| `docs/audits/CVF_ACEL_G1_T2E_FOUR_OWNER_SOURCE_CONTRACT_DESIGN_2026-09-18.md` | Cross-Contract Separation Matrix, Case 10; Contracts 1-4 | authoritative design boundary for the permitted combination |
| `docs/reviews/CVF_ACEL_G1_T2E_FOUR_OWNER_SOURCE_CONTRACT_DESIGN_COMPLETION_2026-09-18.md` | Decision / Disposition; Findings / Position | accepted bounded design and Local repairs |
| operator instruction, 2026-09-18 | affirmative approval to combine Contracts 1+2 | topology authority; not identity or operational-source evidence |

## Scope / Methodology

Role: Local orchestrator/reviewer. Phase: operator architecture-decision
recording. The operator owns combination and appointment decisions; Local owns
technical consistency and later packet authoring. No external research or
shared-workspace worker is used in this decision.

Per reviewer non-duplication, Local consumed the accepted T2E design and its
Case 10 conflict-of-duty analysis. No new source scan or contract redesign was
needed. Local tested the operator choice against all separation cases before
recording the resulting three-party minimum topology.

## Findings / Position

The operator-approved combination is permitted by Case 10 because signing-key
custody and authority-specification authorship do not by themselves create the
writer/observer or specification-author/issuer self-attestation loops rejected
elsewhere in the design.

The resulting topology has three independently accountable party positions:

| Party position | Responsibilities | Independence requirement | Current identity state |
|---|---|---|---|
| Combined Party A | Contract 1 plus Contract 2 | must not independently approve its own specification activation; must not act as Contract 3 observer for the key registry; must remain distinct from Contract 4 | `IDENTITY_PENDING_OPERATOR_APPOINTMENT` |
| Party B | Contract 3 | must remain distinct from Party A for key-registry observation and from Party C for issuer-registry observation | `IDENTITY_PENDING_OPERATOR_APPOINTMENT` |
| Party C | Contract 4 | must remain distinct from Contract 2 authorship and from Party B's independent observation role | `IDENTITY_PENDING_OPERATOR_APPOINTMENT` |

Combining Contracts 1+2 does not combine their evidence stores or eliminate
their separate lifecycle duties. Party A still needs distinguishable records
for key-registry mutation and specification proposal/publication. Activation
approval for Contract 2 remains an operator decision until a distinguishable
approval authority is appointed.

## Decision / Disposition

Decision: `APPROVE_CONTRACTS_1_2_COMBINATION_IDENTITY_PENDING`.

The operator approves one future actual party to hold Contracts 1+2. Contracts
3 and 4 remain separate party positions. The following combinations remain
rejected:

- Contract 1 + Contract 3 for the key registry;
- Contract 4 + Contract 3 for the issuer registry;
- Contract 2 + Contract 4;
- any self-approval, self-observation, self-revocation, or emergency bypass.

This instruction supplies the topology choice only. No person, team,
organization, service account, repository module, registry, key, or source
path was named. Actual-party identity therefore remains pending, operational
sources remain `BLOCKED_SOURCE_NOT_FOUND`, and candidate admission remains
`UNVERIFIED`.

No worker order is released from this decision. The next operator checkpoint
is to name or explicitly defer the actual party for Party A, Party B and Party
C. Only then may Local prepare a separately governed source-establishment or
implementation packet.

## Risk / Corrective Action

| Risk | Control |
|---|---|
| topology approval is misread as an appointment | retain `IDENTITY_PENDING_OPERATOR_APPOINTMENT` until exact party identity and acceptance evidence exist |
| Party A self-approves its own specification | operator remains activation decision owner until a distinguishable approval authority is appointed |
| a registry writer claims independent observation | Party B must be distinct from Party A for the key registry and Party C for the issuer registry |
| Contract 2 author also becomes issuer authority | Contract 2 + Contract 4 remains hard-rejected |
| another paper-only tranche hides the missing identities | preserve `STOP_REASSESS_ARCHITECTURE`; require actual-party decision before dispatch |

## Negative Search And Collision Discipline

This decision does not claim a new exhaustive search. It reuses the accepted
T2E negative-search evidence. Exact prior search command or query:

```
rg -n --hidden --no-ignore -i 'ACEL-G1-T2E|VerifierKeyAndRegistryControlOwner|VerificationAuthoritySpecificationOwner|RegistryObservationOwner|IssuerRegistryAuthorityOwner|PROPOSED_OPERATOR_DECISION|BLOCKED_SOURCE_NOT_FOUND|UNVERIFIED' docs governance EXTENSIONS ECOSYSTEM CVF_SESSION -g '*.md' -g '*.json' -g '*.py' -g '*.ts'
```

Search roots and coverage were `docs`, `governance`, `EXTENSIONS`,
`ECOSYSTEM`, and `CVF_SESSION` across Markdown, JSON, Python and TypeScript.
External evidence was inapplicable because this is an internal operator
decision. Absent-versus-collision disposition: the search established no
operational owner/source binding within the bounded roots; matching design and
status tokens are non-authoritative collisions, not appointments.

- Same-token collision `ACEL-G1-T2E`: tranche identifier in its governed
  packet and continuity state; non-authoritative for actual-party identity.
- Same-token collision `VerifierKeyAndRegistryControlOwner`: proposed contract
  name in the accepted design; non-authoritative for Party A appointment.
- Same-token collision `VerificationAuthoritySpecificationOwner`: proposed
  contract name in the accepted design; non-authoritative for Party A
  appointment.
- Same-token collision `RegistryObservationOwner`: proposed contract name;
  non-authoritative for Party B appointment or an observation store.
- Same-token collision `IssuerRegistryAuthorityOwner`: proposed contract
  name; non-authoritative for Party C appointment or an issuer registry.
- Same-token collision `PROPOSED_OPERATOR_DECISION`: generic planning status
  in the accepted design; non-authoritative for an actual appointment.
- Same-token collision `BLOCKED_SOURCE_NOT_FOUND`: generic governed status;
  its other occurrences are non-authoritative for this decision.
- Same-token collision `UNVERIFIED`: generic admission posture; its other
  occurrences are non-authoritative for an appointed or verified owner.
- Same-token collision `CVF_SESSION` and `ECOSYSTEM`: bounded search-root
  names; their other occurrences are non-authoritative for G1 ownership.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | `internal governed input (no external intake)` |
| Chain map route | accepted T2E design -> operator topology choice -> Local decision record |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this Local decision |
| Internal source | `docs/audits/CVF_ACEL_G1_T2E_FOUR_OWNER_SOURCE_CONTRACT_DESIGN_2026-09-18.md` |
| Disposition | `NOT_APPLICABLE_INTERNAL_ONLY_WITH_REASON`: no external evidence was admitted |
| Claim boundary | internal decision evidence does not create an operational owner or source |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: operator approval of Case 10 would reduce four
responsibility positions to three party positions without satisfying any
identity or operational-source requirement.

Evidence Comparison: confirmed. Contracts 1+2 can share Party A, while the
accepted design still requires independent activation approval and separation
from Contracts 3 and 4.

Contradiction Or Gap Disposition: no topology contradiction remains. Exact
party identities, acceptance records and source artifacts remain unresolved
operator inputs.

Claim Update: combination is approved; appointment and implementation remain
pending and fail-closed.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | review heading groups; negative-search command, roots and collision disposition; internal-only routing; epistemic comparison; operation-trace fields |
| gateRunPurpose | confirmation of a bounded operator decision record, not first discovery or owner proof |
| claimBoundary | checker conformity is not an actual-party appointment or operational-source receipt |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: read-only changed-set accounting for the
two pre-existing parked protected checker paths while recording this operator
decision. No checker mutation is authorized.

Protected paths: `governance/compat/check_task_class_calibration_owner_evidence.py`;
`governance/compat/test_check_task_class_calibration_owner_evidence.py`.

Operator authorization: explicit approval to combine Contracts 1+2.
Rollback boundary: revert only this decision record if rejected; preserve the
accepted T2E material, continuity commits and all thirteen parked paths.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer |
| Provider or surface | private CVF workspace |
| Session or invocation | T2E Contracts 1+2 operator decision, 2026-09-18 |
| Working directory | repository root |
| Command or tool surface | governed source reads, Git status, `apply_patch`, governance gates and Git |
| Target paths | this Local operator-decision record |
| Allowed scope source | operator instruction approving Contracts 1+2 combination |
| Before status evidence | HEAD `2e3d3a226`; thirteen parked untracked paths; staging empty |
| After status evidence | one topology-decision record; parked paths unchanged |
| Diff evidence | exact one-path material manifest before staging |
| Approval boundary | Contracts 1+2 combination only; actual identities remain pending |
| Claim boundary | no appointment, key, registry, lookup, implementation, runtime or public effect |
| Agent type | Local decision recorder/reviewer |
| Invocation ID | `acel-g1-t2e-contracts-1-2-combination-decision-20260918` |
| Expected manifest | this Local decision record |
| Actual changed set | verified before material commit |
| Manifest delta | pending exact-path staging confirmation |
| Deletion or rename disposition | none |

## Corpus Completeness And Report Integrity

- Corpus task class: bounded decision over two named governed inputs and one
  operator instruction; no complete-repository claim.
- Corpus root: the two governed paths in Target / Source.
- Snapshot time: 2026-09-18 at decision base HEAD.
- Enumeration command: filesystem-backed direct reads using `Get-Content -LiteralPath 'docs/audits/CVF_ACEL_G1_T2E_FOUR_OWNER_SOURCE_CONTRACT_DESIGN_2026-09-18.md'` and `Get-Content -LiteralPath 'docs/reviews/CVF_ACEL_G1_T2E_FOUR_OWNER_SOURCE_CONTRACT_DESIGN_COMPLETION_2026-09-18.md'`.
- Manifest artifact or inline manifest: Target / Source table.
- Manifest hash: N/A with reason: bounded named-input decision.
- Processing ledger artifact or inline ledger: both governed paths READ;
  operator instruction classified SCOPE_AUTHORITY_NOT_SOURCE_PROOF.
- Allowed terminal statuses: `READ`, `SKIPPED_WITH_REASON`, `DEFERRED`,
  `BLOCKED_UNREADABLE`.
- Reconciliation: manifest=2; ledger_terminal=2; exclusions=0; unreadable=0; unresolved=0.
- Unresolved files: zero among the two named governed inputs.
- Declared exclusions: all other repository paths and all external sources.
- Unreadable or unsupported files: none.
- Aggregation check: 2 = 2 + 0 + 0.
- Drift check: exact decision base recorded.
- Output traceability: this decision record.
- Adversarial verification: combination approval cannot count as appointment.
- Corpus verdict: PARTIAL

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | operator approval to combine Contracts 1+2 |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: no runtime receipt is claimed |
| actionEvidence | ACTION_EVIDENCE_PRESENT: operator topology choice and Local recording only |
| invocationBoundary | governed local documentation and Git workflow |
| interceptionBoundary | no IDE, provider, CLI/MCP or runtime interception claim |
| claimLanguage | combination approved; identities and operational sources pending |
| forbiddenExpansion | appointment inference, keys, implementation, lookup, admission, runtime, public sync, deployment |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private architecture decision with no public-sync authorization.

## Claim Boundary

This record approves only the combination of Contracts 1+2 under one future
actual party. It neither names nor appoints Party A, Party B or Party C and
does not establish any registry, key, specification, observation log, lookup,
candidate admission, runtime or public authority.
