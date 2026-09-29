# CVF GC-018 Baseline - NCR Q001 Local Transaction Store

Memory class: governed-dispatch-baseline

docType: baseline

Status: DISPATCH_READY

Batch ID: CVF-NCR-Q001-LOCAL-TRANSACTION-STORE

Decision owner: Local reviewer/closer

Dispatch base head: `bbce6e07b6861d4b86893a94bff5c2d850661a99`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Packet Correction

The paired work order now carries the acceptance requirement ledger required by its worker-return fast gate. This dispatch amendment changes no implementation or closure claim.

## Purpose

Bound the repair of the confirmed Q001 JSON-ledger failure to a local, single-host transaction store. Implementation starts only when the paired packet is committed, current authority is synchronized, and bound pre-dispatch admission passes.

## Authority And Source

The operator directed continued Q001 completion. Roadmap D028/Q001 and `docs/reference/CVF_NCR_Q001_LEDGER_DURABILITY_FAILURE_PROFILE_2026-09-29.md` identify the observed truncation and read-window defect. The prior probe is bounded application-fault evidence, not a power-loss, hosted, or production proof.

## Source / Predecessor Evidence

The fault profile is committed at `1722db834`; the current JSON implementation is `EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/ledger_layer/immutable_ledger.py`. Earlier quiescent restore and snapshot reconciliation do not close the observed failure.

## Decision / Baseline / Proposed Tranche

Decision: SQLite for the local single-host candidate only. Baseline: JSON rewrite is `REPAIR_REQUIRED`. Proposed tranche: transactional append, validated migration, exact-ID lookup and clean local restore. `DISPATCH_READY` describes authored packet content; final worker release still requires the committed continuity and bound pre-dispatch PASS.

## Scope / Target / Owner Boundary

The target is the Q001 local engine ledger. Dispatcher owns this packet; worker implementation requires later release; a distinct Local reviewer owns the independent probe and acceptance. Operator retains pilot, hosted and cost decisions.

## Technical Boundary

Use Python standard-library SQLite as the selected candidate for the local single-host profile. Keep the existing block schema/hash and `ImmutableLedger` consumer contract compatible. A new database may be built from a fully verified JSON chain, but the source file must remain byte-identical and cutover must be explicit. No operation against the current GitHub eight-block runtime ledger is authorized by this packet.

The store must expose complete committed snapshots and exact request-ID lookup. Append must serialize tip selection and insert in one transaction; a duplicate ID with the same event must resolve to the existing block, while a conflicting event fails closed. This controls duplicate ledger blocks only: it does not prove exactly-once behavior of earlier registry, routing, or approval operations in `CoreOrchestrator`.

## Acceptance Invariants

1. Injected failure before commit preserves prior committed chain and exposes no partial block.
2. Two real processes using the production append path cannot lose a block; an explicit barrier proves attempted entry before parent release and complete entry afterward. Timeout expiry is never positive exclusion evidence.
3. The append return and `ledger_attached` occur only after the transaction reports commit. A crash after commit but before HTTP response resolves by exact request ID without automatic replay.
4. Bad hash/link, duplicate/conflicting ID, incompatible schema, and interrupted migration fail without overwriting the input or presenting a success receipt.
5. A consistent online backup restores into a clean instance and reconciles block count, tip hash, request IDs, and relevant artifact references. The drill is local only; off-machine encryption, key recovery, retention schedule, RPO/RTO, and hosted/multi-host store choice remain separate gates.
6. The Local reviewer runs an independent probe and owns acceptance. The worker returns the probe as pending and leaves all changes uncommitted.

## Forbidden Scope

No mutation of the live GitHub ledger, OAuth secret/configuration, Web UI, external agent/runtime, provider call, pilot effect, artifact acceptance, P11, public sync, deployment, or production cutover. No claim that an `ALLOW` decision approves the HTML artifact.

## Evidence / Verification

At dispatch authoring, source inspection and static contract checks are the only evidence. Worker proof must later include real peer barriers, fault rollback, duplicate-ID behavior, clean restore and final-return hash. Reviewer acceptance requires a separately executed probe.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Internal governed input (no external intake) |
| Internal source | `docs/reference/CVF_NCR_Q001_LEDGER_DURABILITY_FAILURE_PROFILE_2026-09-29.md` |
| Chain map route | Local source-derived repair under the existing ledger owner |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/ledger_layer/immutable_ledger.py` |
| Disposition | INTERNAL_ONLY_NO_EXTERNAL_PROMOTION |
| Claim boundary | Public/external absence does not establish private-CVF absence. |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Command: `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json`; returned 0 items, `truncated=false`. No ADIF item supplies execution authority; release is gated separately.

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_high_risk_local_transaction_proof.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_gate_to_role_closeability.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; `High-Risk Local Transaction Proof Applicability: REQUIRED`; nine-key contract; closeability graph |
| gateRunPurpose | Confirmation of authored source and contract evidence, not first discovery of gate shape; no implementation or runtime truth follows from a static pass. |
| claimBoundary | This baseline authorizes a bounded later worker tranche only after final dispatch release. |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --help` inspected during authoring; no scaffold output was used |
| generatedProfile | manually authored GC-018 Q001 local transaction baseline |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | prior HOLD baseline amended from source and acceptance invariants |
| checkerReadAheadConfirmation | dispatch, high-risk, closeability, release-readiness and scaffold-provenance checker sources inspected |
| docOnlyNewFields | exact local SQLite scope and bounded proof semantics |
| claimBoundary | packet provenance only; no runtime transaction proof |

## Claim Boundary

No transaction-store implementation, restore drill, RPO/RTO result, provider-governance proof, or Q001/R0 closure is claimed.
