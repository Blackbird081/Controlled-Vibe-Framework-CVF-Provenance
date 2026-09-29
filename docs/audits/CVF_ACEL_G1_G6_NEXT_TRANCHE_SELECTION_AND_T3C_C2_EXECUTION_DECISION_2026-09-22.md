# CVF ACEL G1-G6 Next-Tranche Selection And T3C-C2 Execution Decision

Memory class: POINTER_RECORD

Status: OPERATOR_EXECUTION_READY

Date: 2026-09-22

Decision owner: Local orchestrator/reviewer

Execution owner: operator-mediated `LAM-RUBY\cvf-g1-party-b`

Review owner: Local reviewer, after the Party B ceremony

## Purpose

Select the next source-verified tranche in the active ACEL G1-G6 program and
open exactly one bounded real action: create the genesis Group 3 observation
of the existing Group 1 verifier-key registry as the verified Party B
principal. This packet does not delegate implementation and does not authorize
Claude, another worker, Local, Party A, or the activation approver to perform
the observation.

## Authority Chain

- operator instruction on 2026-09-22: record the MCP/MUO discussion and return
  to the G1-G6 tranche;
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`;
- `AGENT_HANDOFF_V63_2026-09-18.md`;
- `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md`;
- `docs/audits/CVF_ACEL_G1_T3C_GROUP3_SOURCE_READINESS_ROUTE_2026-09-21.md`;
- `docs/reviews/CVF_ACEL_G1_T3C_C1_GROUP3_OBSERVATION_LOG_TOOLING_WORKER_RETURN_2026-09-21.md`;
- material tooling closure commit `db78c87df`;
- high-risk proof foundation accepted before this decision, as recorded by the
  active handoff.

This packet is the fresh governed authority required by the active handoff for
Party B execution and first Group 3 source creation. Its authority ends after
one successful genesis append or any failed attempt.

## Scope / Methodology

Local compared the six retained gap lanes against the active handoff, then
re-verified the exact Party B account posture, Group 1 source validity, Group
3 target absence, accepted tooling commit and remaining downstream holds. The
selection favors the nearest unresolved dependency with a source-verifiable
input and a bounded reversible failure boundary.

The review did not recreate the accepted T3C-C1 implementation. It consumed
its frozen evidence, reran only the hermetic checker/writer probes needed to
confirm execution readiness, and tested the new launcher in non-mutating
`--check` mode.

## Findings / Position

T3C-C2 is ready for an operator-mediated first observation. The tooling and
input source are valid, the target remains absent, and the exact Party B
principal is enabled, password-bound and non-admin. Full Group 3 establishment
is not ready because the issuer-registry side and T3E consumer remain absent.

The MCP/MUO discussion is orthogonal and remains deferred under the existing
external-invocation moratorium. It supplies no runtime authority to this lane.

## G1-G6 Selection Matrix

| Gap | Current bounded state | Immediate information gain | Dependency position | Decision |
|---|---|---|---|---|
| G1 empirical execution calibration | ADAPT; Groups 1 and 2 are locally verified, Group 3 tooling is accepted, real Group 3 source is absent | high: converts accepted tooling into one independently reviewable source fact | next unresolved dependency in the active chain | SELECT T3C-C2 |
| G2 runtime topology | ADAPT; bounded topology and calibration work already completed | lower until the active G1 source chain advances | parallel but not the nearest blocker | RETAIN |
| G3 behavioral evaluation owner | ADAPT; contract implementation already closed/parked | no new source fact without later consumer work | downstream | RETAIN |
| G4 incremental value | ADAPT; owner design closed/parked | no immediate dependency closure | downstream | RETAIN |
| G5 resume/external-side-effect safety | WATCH; not yet verified | useful later, but does not close the current ACEL source dependency | separate safety lane | WATCH |
| G6 impact-derived verification | ADAPT; bounded experiment closed signal-only | further work would not create the missing Group 3 source | parallel | RETAIN |

Decision: `SELECT_ACEL_G1_T3C_C2_FIRST_GROUP3_OBSERVATION`.

The choice is based on dependency order and expected information gain, not a
claim that G1 is more important than all other gaps. T3C-C2 has a concrete
principal, accepted tooling, a validated input source, and one absent target.

## Source Verification Block

| Claimed fact | Verified source or command | Result | Disposition |
|---|---|---|---|
| Party B identity and posture | `Get-LocalUser cvf-g1-party-b`; Administrators membership query, 2026-09-22 | enabled, password required, non-admin, SID `S-1-5-21-1644666849-912006174-747199667-1009`, bounded expiry | ACCEPT |
| Group 1 registry and lifecycle source | `check_acel_g1_verifier_key_registry.py` against both governed paths | `PASS [VALIDATED]`; row and lifecycle hashes independently validated | ACCEPT |
| Group 3 tooling | `scripts/acel_g1_party_b_group3_observation_writer.ps1`; closure `db78c87df` | principal-bound writer plus read-only checker; hermetic transaction proof accepted | ACCEPT |
| Group 3 target | `Test-Path governance/sources/registry_observation_log/LOG.jsonl` | `False` | ACCEPT_EXPECTED_ABSENCE |
| Party C / Group 4 source | current T2F and handoff state | not established | DEFER; does not block a Group 1-only first observation |
| T3E consumer binding | active handoff | unopened | DEFER; no consumer or admission claim permitted |

## Execution Boundary

Authorized action:

1. run `scripts\run_as_cvf_g1_party_b.cmd --check` from the repository root;
2. if and only if it reports `READY`, run
   `scripts\run_as_cvf_g1_party_b.cmd`;
3. enter the Party B password only into the Windows `runas` prompt;
4. in the Party B PowerShell window, type exactly
   `EXECUTE GROUP 3 OBSERVATION WRITE`;
5. stop after the writer reports
   `OBSERVATION_APPENDED_PENDING_LOCAL_VERIFICATION` and return its six
   non-secret result fields to Local review.

The launcher is a one-time genesis launcher. It fails closed if the log already
exists, Party B posture/SID differs, PowerShell 7 is unavailable, or the Group
1 registry is missing.

## Risk / Corrective Action

| Risk | Control / corrective action |
|---|---|
| wrong or elevated principal performs the write | exact name/SID, enabled/password-required/non-admin checks plus writer-side non-elevated principal guard |
| accidental second append | launcher rejects an existing real log; later appends require a new packet |
| partial write or DACL failure | transaction rollback and fail-closed identifiers; Local inspects exact state before any retry |
| tooling success mistaken for establishment | pending-verification token and explicit Party C/T3E hold |
| reviewer repeats implementation | consume accepted T3C-C1 evidence; run only the named real-source independent probe |

Forbidden actions:

- do not paste or persist the Party B password;
- do not run the writer as Local, administrator, Party A or the approver;
- do not retry after a partial or failed real-mode attempt without Local
  diagnosis of the target path, bytes and security state;
- do not append a second observation;
- do not edit the Group 1 registry or lifecycle log;
- do not open Party C, Group 4, T3D, T3E, key promotion, candidate evaluation,
  provider/live API, public-sync or deployment work.

## High-Risk Transaction Evidence Binding

The real action exercises the transaction implementation already accepted at
`db78c87df`: real second-process exclusion, deterministic barriers, cleanup
after post-acquire failure, complete semantic ACL tuple comparison, exact
rollback adversaries, final-evidence binding and a pending independent Local
probe. Static acceptance does not prove this real append succeeded.

After the ceremony, Local must independently:

- run the observation-log checker against the real log and expected Party B
  SID;
- recompute the Group 1 snapshot hash from exact registry bytes;
- verify the genesis chain (`priorEntryHashHex == null`) and stored entry hash;
- read back owner, protected DACL, inheritance state and complete ACE tuples;
- verify one record and one unique `snapshotId`;
- compare the reported fields to the durable record;
- record whether rollback or recovery is required if any check fails.

Until that probe passes, the only allowed source disposition is
`OBSERVATION_APPENDED_PENDING_LOCAL_VERIFICATION`.

## Stop Conditions

Stop immediately and return the exact error identifier/output if any launcher
check fails, `runas` rejects the password, the principal check fails, the
Group 1 checker fails, confirmation is mistyped, the transaction reports a
write/DACL/rollback error, or the expected pending-verification token is absent.
Do not transform any failure into a success claim or rerun automatically.

## First-Attempt Diagnostic And Retry Disposition

The first operator attempt stopped before `Append-ObservationTransaction`
because the Party B `runas` profile could not resolve `python` while invoking
the mandatory Group 1 checker. Local verified that
`governance/sources/registry_observation_log/LOG.jsonl` remained absent; no
transaction, durable record or partial source state existed.

Root cause: the launcher projected the DELL-owned Node path but omitted the
machine's per-user Python installation from Party B's process environment.
Bounded correction: Party B received Read and Execute only (no write) on the
pinned Python 3.11 runtime, and the launcher now verifies that executable and
ACL binding before adding its directory to the Party B process `PATH`.

Retry disposition: `AUTHORIZED_ONCE_AFTER_CORRECTED_LAUNCHER_CHECK_PASS`.
Any further failure returns to Local diagnosis; no automatic third attempt is
authorized.

## Review And Success Criteria

T3C-C2 may be accepted only when the operator-mediated append succeeds and
Local's separate read-only probe passes every item above. Success establishes
one locally verified Group 1 observation record. It does not establish full
Group 3 coverage because Party C/Group 4 observation is absent, and it does
not establish T3E consumer binding or candidate admission.

Next move after acceptance: Local files the T3C-C2 verification completion and
selects the next source-verified tranche. Next move after failure: Local
diagnoses the exact transaction state before any retry.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| checkerPath | `governance/compat/check_acel_g1_registry_observation_log.py` |
| checkerMode | real-log explicit path plus expected Party B observer SID |
| passMeaning | schema, canonical bytes, hash chain, identity and record invariants pass |
| nonMeaning | does not prove account posture, ACL semantics, consumer binding or admission |
| claimBoundary | checker PASS is one input to Local verification, never self-acceptance |

## Agent Operation Trace Block

| Field | Value |
|---|---|
| role | LOCAL_REVIEWER_ORCHESTRATOR |
| phase | NEXT_TRANCHE_SELECTION_AND_OPERATOR_EXECUTION_AUTHORIZATION |
| modelSelectionSource | OPERATOR_UI |
| reviewBoundary | source-state audit and execution control; no Party B impersonation |
| beforeState | Group 3 log absent; Party B verified; accepted tooling at `db78c87df` |
| mutationAuthorized | one Party B-owned genesis observation through the reviewed writer |
| decisionOwner | Local reviewer after independent verification |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Chain map route | active handoff to local source verification to bounded operator execution decision |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this execution decision and the later Local completion review |
| Internal source | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` |
| Disposition | `NOT_APPLICABLE_INTERNAL_ONLY_WITH_REASON`: no external source is admitted |
| Claim boundary | no external shortlist, public absence claim or remote-agent evidence is admitted |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Finding-To-Governance Learning Disposition

No new cross-case governance defect is asserted. The packet applies the
already accepted high-risk local transaction proof rule and the earlier
principal-first route. Any real-run failure will be classified from evidence
before deciding whether it is an implementation defect, environment-specific
operation issue, or reusable governance learning.

## Public Export Disposition

`DEFERRED_PRIVATE_ONLY`

Reason: this is a private local-principal execution decision and contains
machine-specific identity/path facts. No public artifact is authorized.

## Claim Boundary

This decision selects and authorizes one bounded local ceremony. It does not
claim the ceremony has run, the Group 3 source exists, full Group 3 is
established, a consumer is wired, a candidate is admissible, or any provider,
public, deployment, MCP or MUO runtime is ready.
