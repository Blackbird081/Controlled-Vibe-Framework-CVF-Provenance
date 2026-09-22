# CVF GC-018 Baseline - ACEL G1 T3C-C1 AR1 Transaction Architecture Reopen

Memory class: governed-dispatch-baseline

docType: baseline

Status: DISPATCH_READY

Date: 2026-09-22

Batch ID: ACEL-G1-T3C-C1-AR1-TRANSACTION-ARCHITECTURE-REOPEN

Dispatch base head: `6e85f0b9ab2c031ec4ccf4efa21a19e8fd1ad8da`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: Local orchestrator/reviewer

providerExecutionAuthority: FORBIDDEN

successorTrancheOpened: NO

## Purpose

Record the fresh operator-authorized architecture reassessment required by the
T3C-C1 R2 terminal review and authorize one new-chain implementation attempt.
This is AR1, not a bounded R3 continuation of the stopped repair chain.

## Scope / Target / Owner Boundary

Target: one fresh architecture contract and one four-path no-commit internal
implementation return.

Owner boundary: the operator authorizes reopening; Local owns architecture,
dispatch, independent review and closure; the worker owns only the four paths
named by the work order. Real Party B execution and durable source creation
remain operator checkpoints outside this baseline.

## Source / Predecessor Evidence

The predecessor evidence is the committed terminal review at
`docs/reviews/CVF_ACEL_G1_T3C_C1_R2_TRANSACTION_LIFETIME_AND_SECURITY_VERIFICATION_COMPLETION_2026-09-21.md`,
SHA-256 `e1ae83b3b601e138dd8a903d2b45736159b7aad091d7fcbc7237c1735de29086`.
It remains terminal for the old chain; this baseline consumes its findings as
input to a new operator-authorized architecture chain.

## Decision / Baseline / Proposed Tranche

The prior problem chain remains terminal at `STOP_REASSESS_ARCHITECTURE`.
Operator instruction on 2026-09-22 authorizes a fresh architecture contract and
new implementation order. AR1 may repair the same four pending worker paths but
must satisfy the replacement proof architecture below as one indivisible unit.

The replacement architecture has four controls:

1. a real second `pwsh` process and named synchronization barriers prove
   transaction exclusion across DACL verification, final validation and
   rollback; mutex identity/type inspection is not proof;
2. acquisition and release are exception-safe, including failures after an OS
   mutex is acquired but before the caller receives a guard object;
3. applied and restored security are verified by semantic read-back of owner,
   protection and the complete explicit ACE multiset; and
4. final evidence is bound to the one canonical return path by pre/post SHA-256
   equality around the final gate, with no later return mutation and no
   alternate return artifact.

No real Party B execution or Group 3 source creation is authorized.

## Architecture Contract

### Deterministic peer-process proof

The writer self-test must launch a genuine second PowerShell 7 process using
the same script in a test-only peer mode. Parent and peer coordinate through
uniquely named `EventWaitHandle` barriers derived from a random test run ID.
No correctness assertion may depend on `Start-Sleep`, elapsed-time guesses or
mutex type/name inspection.

The parent exposes a disposable hook only in self-test mode after stream close
and while the outer guard remains held. The peer signals `ATTEMPTING`, then
attempts the same transaction. `ENTERED` must remain unsignaled while the
parent performs DACL read-back and final validation. On injected parent
failure, rollback completes before guard release; the peer then enters,
re-reads current bytes, appends, validates and exits zero. Final bytes must
contain the peer append exactly once and a valid chain.

### Exception-safe guard lifetime

The caller initializes the guard to null and places acquisition plus every
fallible snapshot/read/mutation step inside the protected `try/finally`.
The acquisition helper must release and dispose internally if any failure
occurs after OS acquisition but before successful return. A deterministic
injection proves a second process can acquire immediately after that failure.

### Exact security proof

Security comparison uses a canonical semantic descriptor: owner SID,
`AreAccessRulesProtected`, and a multiset of explicit filesystem ACE tuples
containing identity SID, allow/deny type, numeric rights, inheritance flags and
propagation flags. Order-only canonicalization is ignored; missing, additional
or changed tuples reject. Successful policy accepts only Party B, SYSTEM and
Administrators allow entries with the required rights and no deny/inherited or
unexpected entry.

Rollback must re-read and compare the complete prior semantic descriptor plus
exact prior bytes. A restoration mismatch is a rollback failure retaining both
primary and rollback context.

### Final-return evidence binding

The existing canonical worker-return file is updated in place and is the only
return. After its content is final, the worker computes SHA-256, runs the exact
active-work-order fast gate, recomputes SHA-256, requires equality, and makes
no subsequent file edit. The chat return reports canonical path, digest,
command and exit code. Local recomputes the digest before review. Self-hash
inside the file is neither required nor accepted as a substitute.

## Evidence / Verification

| Evidence source | Baseline disposition |
|---|---|
| `docs/reviews/CVF_ACEL_G1_T3C_C1_R2_TRANSACTION_LIFETIME_AND_SECURITY_VERIFICATION_COMPLETION_2026-09-21.md` | five defects and terminal stop accepted as the architecture input |
| four pending T3C-C1 worker paths | non-authoritative implementation evidence; exact starting hashes pinned in the work order |
| Group 3 real log | must remain absent |
| R2 aggregate tests | retained only as regression evidence; not concurrency proof |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id ACEL-G1-T3C-C1-AR1-TRANSACTION-ARCHITECTURE-PROOF-CLOSURE --title "ACEL G1 T3C-C1 AR1 Transaction Architecture Proof Closure" --date 2026-09-22 --base 6e85f0b9a --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 0 --new-independent-critical-evidence NONE --scec-problem-key acel-g1-t3c-c1-transaction-architecture-v2-problem --scec-chain-mode INITIAL --scec-chain-ordinal 0 --scec-required-disposition ROOT_CONTRACT_REQUIRED --scec-successor-scope INTEGRATED_ROOT_CONTRACT --no-evidence-readiness-applicable --stdout` |
| generatedProfile | protected-governance-path plus no-commit internal worker profile |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | replaced placeholders with the fresh AR1 architecture, four-path ownership and five proof contracts |
| checkerReadAheadConfirmation | dispatch, convergence, route, closeability, protection, trace and structural checker sources read |
| docOnlyNewFields | none |
| claimBoundary | dispatch provenance only; no implementation or real-source proof |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`CODE_CHANGE`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

The exact resolver query returned zero candidates on 2026-09-22.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | exact four AR1 worker outputs | hermetic local repair only | baseline, work order, disposable process probes | shared workspace PowerShell/Python | IMPLEMENTED |
| `EXTERNAL_AGENT_CLI_MCP` | no AR1 adapter | no ingress, mutation or decision authority | none | fresh governed adapter required | DEFERRED_WITH_REASON |

## Finding-To-Governance Learning Disposition

| Finding group | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| mutex presence substituted for peer exclusion | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | RULE_ADDED | AR1 requires a real peer process with deterministic barriers |
| final gate claim not bound to final return | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | AR1 uses a bounded hash-before/hash-after protocol; reusable checker remains a separate foundation candidate |
| acquisition-to-try and rollback security gaps | WORKER_EXECUTION_ERROR | GOVERNANCE_CONTROL_PLANE | RULE_ADDED | exception-safe acquisition and exact semantic restoration are mandatory AR1 acceptance controls |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_task_governance_route.py` |
| literalTokensReviewed | dispatch status; source verification; protected paths; initial convergence; no-commit return; trace; public disposition |
| gateRunPurpose | confirm the fresh architecture packet before dispatch |
| claimBoundary | packet structure and proof design only; no implementation acceptance or real-source authority |

## External/Local Coordination Binding

Role: `INTERNAL_AGENT`; phase: AR1 implementation; decision owner: Local.
External research is closed and has no implementation or review authority.

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: the replacement architecture will make all five
R2 findings observable through deterministic process, exception and security
oracles plus exact final-return identity.

Evidence Comparison Requirement: the worker and Local reviewer compare each
oracle with this prediction; aggregate pass counts alone are insufficient.

Contradiction Handling Requirement: any missing peer, timing-based assertion,
unverified DACL restoration or return-hash drift invalidates the result.

Claim Update Requirement: Local records confirmed, revised, narrowed or
invalidated for each of the five R2 findings.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private architecture and implementation dispatch; no public-sync
authority.

## Claim Boundary

This baseline authorizes a fresh, hermetic implementation attempt against four
pending files. It does not reopen the stopped R2 chain, accept existing worker
code, authorize credentials or alternate-user execution, touch the real Group
1/Group 3 sources, create Party C/Group 4, open T3E, evaluate a candidate, call
a provider, publish, deploy, stage or commit worker changes.
