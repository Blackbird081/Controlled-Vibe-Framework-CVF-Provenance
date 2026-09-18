# CVF ACEL G1 T2E Four-Owner Responsibility Local Decision

Memory class: governed-local-decision

docType: review

Status: APPROVED_FOR_BOUNDED_DESIGN_DISPATCH

Date: 2026-09-18

Decision owner: operator for accountable-role assignment; Local orchestrator/reviewer for technical dispatch

Decision base HEAD: `e47fad31191070bed9b57680118978e9a3973cce`

## Purpose

Record the operator's explicit approval of the four-responsibility owner model
identified by the reviewed T2D owner-option matrix, and authorize Local to
prepare one bounded internal work order for source-contract design. This does
not appoint a person or organization, create a key or registry, or authorize
runtime implementation.

## Target / Source

| Source | Verified locator | Use |
|---|---|---|
| `docs/audits/CVF_ACEL_G1_T2D_SOURCE_OWNER_OPTIONS_2026-09-18.md` | Owner-Option Matrix; Risk / Corrective Action | four distinct responsibility classes and proposed contract surfaces |
| `docs/reviews/CVF_ACEL_G1_T2D_SOURCE_OWNER_ESTABLISHMENT_LOCAL_REVIEW_2026-09-18.md` | Reviewer Verification And Remaining Closure Boundary; Decision | Local bounded acceptance and fail-closed limits |
| `docs/audits/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_2026-09-17.md` | Owner Ledger | consumer-side dependencies the owner contracts must eventually satisfy |
| operator instruction, 2026-09-18 | affirmative reply to the proposed four-responsibility model | approval to proceed with bounded design; not source proof or owner appointment |

## Scope / Methodology

Local mapped the operator decision to the four T2D rows without reopening the
bounded source search. Per reviewer non-duplication, the T2D search evidence is
consumed rather than recreated. The approved split is responsibility-level:

1. verifier signing-key custody, rotation, revocation, and public-key registry
   write authority;
2. independently trusted authority-specification ownership and
   `verificationAuthorityHash` decision binding;
3. registry-snapshot identity and append-only source-observation-log ownership;
4. issuer-registry content and lookup-semantics ownership.

These may later map to distinct accountable parties. Combining any two requires
a future explicit operator decision and conflict-of-duty analysis; this decision
does not combine them.

## Findings / Position

The operator approved the four-responsibility model. Because T2D found no
verified existing operational owner for any row, the next safe action is a
documentation-only source-contract design, not implementation. Each contract
must define decision rights, write boundaries, consumer interfaces, lifecycle,
durable evidence, correction/revocation behavior, independence requirements,
and fail-closed behavior. It must also state exactly what evidence would be
required before Local could treat a named owner as verified.

## Decision / Disposition

Decision: `APPROVE_FOUR_RESPONSIBILITY_MODEL_FOR_CONTRACT_DESIGN_ONLY`.

Local may author and commit a paired GC-018 baseline and no-commit internal
worker order. The worker may design proposed role contracts and evidence
admission criteria. The worker may not name or appoint an actual accountable
party, implement source or registry modules, generate/import keys, perform a
lookup, edit parked evidence, or change candidate admission from `UNVERIFIED`.

T2D committed-range closure remains pending because thirteen pre-existing
untracked G1 paths are parked outside T2D. This explicit operator decision
permits a separately bounded design packet; it does not relabel T2D closed.

## Risk / Corrective Action

Primary risk: treating a role-shaped contract as proof that an operational
owner or source exists. Corrective action: every proposed role and source uses
`PROPOSED_OPERATOR_DECISION`; operational promotion requires a later exact
party assignment, source artifact, control evidence, and independent Local
review. Any absent evidence remains `BLOCKED_SOURCE_NOT_FOUND`.

## Negative Search And Collision Discipline

This decision reuses the reviewed T2D search rather than claiming a new
complete scan. Targeted dispatch collision command:
`rg -n --hidden --no-ignore -i 'ACEL-G1-T2E|VerifierKeyAndRegistryControlOwner|VerificationAuthoritySpecificationOwner|RegistryObservationOwner|IssuerRegistryAuthorityOwner' docs governance EXTENSIONS ECOSYSTEM CVF_SESSION -g '*.md' -g '*.json' -g '*.py' -g '*.ts'`.
Search roots cover governed documentation, JSON state/evidence, checker/tests
and extension source. At authoring time, no T2E output path or proposed role
name existed; the ACEL G1 dependency concepts occur in authoritative T2C/T2D
documents and are accepted collisions, not proof of an appointed owner.
External evidence is excluded because this is internal-only intake; that
exclusion is a boundary, not an absence claim.

Collision disposition: `ACEL`, `T2D`, and `T2E` occur elsewhere as program
and tranche identifiers and are non-authoritative for owner appointment.
Same-token collision `PROPOSED_OPERATOR_DECISION` occurs in the reviewed T2D
matrix and denotes planning status, not an actual owner. The structured query
therefore separates absent proposed role names from disclosed, non-authoritative
occurrences.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | proposed four-owner source-contract design packet | document design only; worker cannot appoint or commit | T2D matrix plus this decision | no runtime adapter | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no selected owner or adapter | no ingress, mutation, credentials, or public claim | explicit exclusion | adapter work deferred | `DEFERRED_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | `internal governed input (no external intake)` |
| Chain map route | current governed T2D audit and Local review -> operator design choice -> Local internal work order |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this Local decision and paired internal work order |
| Internal source | `docs/audits/CVF_ACEL_G1_T2D_SOURCE_OWNER_OPTIONS_2026-09-18.md` |
| Disposition | `NOT_APPLICABLE_INTERNAL_ONLY_WITH_REASON`: only governed private-CVF evidence and operator scope choice are used |
| Claim boundary | no remote source is admitted; internal routing does not prove an operational owner |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: a four-contract design can expose the evidence
and separation requirements without pretending that an owner already exists.

Evidence Comparison Requirement: the worker must compare each proposed field
and boundary against T2C consumers and T2D missing-source findings.

Contradiction Handling Requirement: any located current authority or overlap
must be reported to Local and must not be silently overwritten.

Claim Update Requirement: the worker records each dependency as confirmed,
revised, narrowed, or still blocked.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_epistemic_process_packet.py` |
| literalTokensReviewed | review heading groups; internal-only routing disposition; epistemic comparison, contradiction and claim-update fields |
| gateRunPurpose | confirmation/evidence before release, not first discovery and not proof of source ownership |
| claimBoundary | checker conformity is not owner appointment or runtime evidence |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer |
| Provider or surface | private CVF workspace |
| Session or invocation | operator four-responsibility approval disposition, 2026-09-18 |
| Working directory | repository root |
| Command or tool surface | governed source reads, Git status/hash checks, patch authoring, governance gates |
| Target paths | this Local decision and the paired T2E dispatch packet |
| Allowed scope source | operator affirmative reply to the four-responsibility proposal |
| Before status evidence | HEAD `e47fad31191070bed9b57680118978e9a3973cce`; thirteen parked untracked paths; staging empty |
| After status evidence | bounded decision packet only; parked paths unchanged and outside ownership |
| Diff evidence | exact intended Local decision/baseline/work-order set before commit |
| Approval boundary | four-responsibility contract design only |
| Claim boundary | no actual owner, key, registry, lookup, candidate admission, runtime, public sync, or deployment |
| Agent type | Local decision owner for technical dispatch |
| Invocation ID | `acel-g1-t2e-four-owner-decision-20260918` |
| Expected manifest | this decision plus paired T2E baseline and work order |
| Actual changed set | verified before dispatch commit |
| Manifest delta | pending exact-path verification |
| Deletion or rename disposition | none |

## Corpus Completeness And Report Integrity

- Corpus task class: bounded decision over three named governed inputs and one
  operator scope instruction; no complete-repository claim.
- Corpus root: the three exact governed paths in Target / Source.
- Snapshot time: 2026-09-18 at decision base HEAD.
- Enumeration command: filesystem-backed direct file reads of the three named
  paths; no directory enumeration was required.
- Manifest artifact or inline manifest: inline Target / Source table, three
  governed files plus the separately labeled operator instruction.
- Manifest hash: N/A with reason: bounded named-input decision, not a generated
  corpus manifest.
- Processing ledger artifact or inline ledger: all three governed paths READ;
  operator instruction classified SCOPE_AUTHORITY_NOT_SOURCE_PROOF.
- Allowed terminal statuses: `READ`, `SKIPPED_WITH_REASON`, `DEFERRED`,
  `BLOCKED_UNREADABLE`.
- Reconciliation: manifest=3; ledger_terminal=3; exclusions=all paths outside the named inputs; unresolved=0; operator instruction=1 separately accounted.
- Unresolved files: zero among the named inputs.
- Declared exclusions: all other repository paths and all external sources.
- Unreadable or unsupported files: none.
- Aggregation check: 3 = 3 + 0 + 0.
- Drift check: exact decision base recorded; later worker execution must capture
  its own base.
- Output traceability: this Local decision and paired T2E packet.
- Adversarial verification: proposed role names cannot count as appointments.
- Corpus verdict: PARTIAL - complete only for the named decision inputs; no
  repository-wide or operational-source completeness claim.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | four-responsibility owner source-contract design authorization |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: no runtime receipt is claimed |
| actionEvidence | ACTION_EVIDENCE_PRESENT: operator decision and Local packet authoring only |
| invocationBoundary | governed local documentation and dispatch preparation |
| interceptionBoundary | no IDE, shell, filesystem, provider, or runtime interception claim |
| claimLanguage | the model is approved for design; actual owners remain unappointed |
| forbiddenExpansion | key material, live lookup, implementation, candidate admission, public sync, deployment |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private governance/design decision with no public artifact authorization.

## Claim Boundary

This decision approves a responsibility topology and bounded design dispatch.
It is not appointment evidence, operational source evidence, implementation
authority, or proof that any registry, key, lookup, or observation log exists.
