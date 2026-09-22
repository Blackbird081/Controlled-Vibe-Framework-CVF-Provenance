# CVF GC-018 Baseline - ACEL G1 T3D-C1 Group 4 Issuer Registry And Lookup Tooling

Memory class: governed-dispatch-baseline

docType: baseline

Status: DISPATCH_READY

Date: 2026-09-22

Batch ID: ACEL-G1-T3D-C1-GROUP4-ISSUER-REGISTRY-LOOKUP-TOOLING

Dispatch base HEAD: `72f769e5d`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Local.

Reviewer owner: Local reviewer/closer.

Worker target: shared-workspace `INTERNAL_AGENT` worker.

## Purpose

Authorize one hermetic tooling-only implementation for the Group 4 issuer
registry and lookup-response contract accepted at T3D-C0. The tranche creates
two principal-bound PowerShell tools, one independent Python checker, its
focused tests, and one worker return; it creates no real Group 4 source.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-G1-T3D-C1-GROUP4-ISSUER-REGISTRY-LOOKUP-TOOLING --title "ACEL G1 T3D-C1 Group 4 Issuer Registry And Lookup Tooling" --date 2026-09-22 --base 72f769e5d --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic worker dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | populated exact T3D-C0 byte, identity, principal, transaction, negative-test and lifecycle controls |
| checkerReadAheadConfirmation | dispatch-quality, closeability, high-risk transaction, core-guard, structural, trace and public-export checker sources reviewed |
| docOnlyNewFields | none; tooling implements the accepted Group 4 schema without extending it |
| claimBoundary | dispatch baseline only; no source, principal execution, lookup, consumer binding or admission effect |

## Scope / Target / Owner Boundary

The worker owns exactly five new uncommitted paths: Party C registry writer,
Party B response writer, read-only checker, checker tests, and worker return.
Disposable temporary fixtures are allowed. Local owns review, independent
probes, launchers, source acceptance, staging, commits and continuity.

Party C is exact SID `S-1-5-21-1644666849-912006174-747199667-1010` and may
own/write only `REGISTRY.json`. Party B is exact SID
`S-1-5-21-1644666849-912006174-747199667-1009`, may read the registry, and may
own/append only `LOOKUP_RESPONSES.jsonl`. The worker may not authenticate or
execute as either principal.

## Decision / Baseline / Proposed Tranche

Decision: `AUTHORIZE_HERMETIC_TOOLING_ONLY_SOURCE_NOT_CREATED`.

The accepted T2F Group 4 section and T3D-C0 completion are controlling. This
baseline also freezes adapter-level idempotency, call-shape, JSONL framing and
first-failure rules needed to implement that contract without changing its
closed schemas. C1 may reach only `TOOLING_ACCEPTED_SOURCE_NOT_CREATED` after
Local review. Real registry creation, response-log initialization, a second
Party B observation, and any lookup remain separate operator-gated work.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Group 4 exact envelope, row, response and lifecycle contract | CURRENT_AUTHORITY | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Source Group 4; T3D-C0 amendment; T2C Consumer-Binding Table | `REGISTRY.json`; `LOOKUP_RESPONSES.jsonl` | Source Group 4 contract | ACCEPT |
| Four implementation-blocking gaps are closed | TERMINAL_REVIEW | `docs/reviews/CVF_ACEL_G1_T3D_C0_GROUP4_CONTRACT_COHERENCE_AMENDMENT_COMPLETION_2026-09-22.md` | Findings / Position; Decision / Disposition | T3D-C0 accepted amendment | Local reviewer/closer | ACCEPT |
| Party C exact local principal is verified | LOCAL_VERIFICATION | `docs/audits/CVF_ACEL_G1_T3D_PARTY_C_PRINCIPAL_LOCAL_VERIFICATION_2026-09-22.md` | Findings / Position; Claim Boundary | SID ending `-1010` | Party C principal | ACCEPT |
| Party B exact local principal and immutable observation boundary are verified | LOCAL_VERIFICATION | `docs/audits/CVF_ACEL_G1_T3C_C2_GROUP3_SOURCE_LOCAL_VERIFICATION_2026-09-22.md` | Findings / Position; Claim Boundary | SID ending `-1009`; Group 3 log | Party B observer | ACCEPT |
| T3D-C1 dispatch authoring is the next allowed move | CURRENT_SESSION_AUTHORITY | `AGENT_HANDOFF_V63_2026-09-18.md` | Next Allowed Move | T3D-C1 tooling dispatch | Local orchestrator | ACCEPT |

## Architecture Contract

### Registry writer

The Party C tool defaults to non-mutating self-test. Its real mode is an
initial-create-only, exclusive no-overwrite operation and must require
the exact Party C account/SID, exact confirmation, canonical repository root,
and exact target `governance/sources/issuer_registry/REGISTRY.json`. It writes
one no-BOM/no-newline RFC 8785 JCS envelope atomically, validates every closed
row and canonical-content byte/hash rule before mutation, and applies/read-backs
the exact protected five-ACE registry DACL from T3D-C0. The same-directory temp
is owned, protected, ordered, and read back before atomic publication; the
target name is never visible with an ambient descriptor. Correction, rotation,
revocation and replacement transactions are deferred.

The C1 issuer-authority content profile is closed to exactly three fields:
`authority`=`ACEL_G1_DECISION_OWNER`; `issuerIdentity` matching the row and
ASCII pattern `[A-Za-z0-9._:-]+`; and positive integer `policyVersion` no
greater than 2147483647. No other key/type/value shape is admitted. This makes
the accepted JCS domain explicit without claiming a general-purpose RFC 8785
engine; any future content schema requires a separate contract amendment.

### Lookup-response writer

The Party B tool defaults to non-mutating self-test. Its real modes must bind
the exact Party B account/SID and exact paths. Initialization may create only
an empty protected response log. Lookup append is reserved for later explicit
T3E authority and must validate exact published registry bytes, strict Group 3
snapshot binding, closed response fields, receipt eligibility, and the entire
existing hash chain before one durable append. It applies/read-backs the exact
protected four-ACE response-log DACL. Initialization and append use a
same-directory, pre-hardened copy-on-write temp containing exact prior bytes
plus the new row, flush and full validation before atomic replace, then target
read-back. Direct in-place append is forbidden.

### Checker and tests

The independent checker validates files read-only and never repairs them. It
must verify exact schema, strict base64url/JCS/UTF-8 bytes, both content and
snapshot hashes, version/status rules, response-chain integrity, receipt
semantics, principal separation, owner and complete semantic DACL tuples.
Focused tests use disposable paths and cover all positive vectors plus malformed
encoding, hash drift, schema drift, duplicate/ambiguous active versions, chain
breaks, authority collision, extra/deny/inherited ACEs, wrong owner, concurrent
writers, post-acquire failure and exact rollback.

### Lookup Adapter, Idempotency And Framing

The pure T2C evaluator remains
`lookup(issuerIdentity, issuerAttestedHash, snapshot_content)`. A separate
durable wrapper accepts a T3E-minted UUID `lookupId`, `consumerIdentity`, and
`observedSnapshotId`; it resolves exactly one Group 3 record itself and supplies
that record's strictly decoded `snapshot_content` to the evaluator. Caller
snapshot bytes, result, digest, version and chain fields are never authoritative.

Under the response-log guard, `lookupId` is the idempotency key. An existing ID
with the identical immutable request tuple (`issuerIdentity`,
`claimedIssuerHash`, `consumerIdentity`, `observedSnapshotId`) returns the
validated stored row without append. The same ID with any tuple difference
fails closed with no mutation. Concurrent identical retries produce one row.

An empty log is zero bytes. Every stored response is exactly one compact JCS
object including `entryHashHex`, UTF-8 without BOM, followed by one LF byte.
There is no CRLF, blank line, partial line, leading separator or alternate
serialization; append preserves all previous bytes as an exact prefix.

Malformed/incomplete request, unavailable/invalid source, missing issuer,
ambiguous active version or lookup-ID conflict is an in-memory no-append
failure. Schema-complete cryptographic/status mismatch produces one
`IDENTITY_REJECTED` row with null `errorCode`. A complete lookup whose row and
snapshot fields are derivable but whose observation freshness, authority or
policy binding is unresolved produces one `IDENTITY_UNRESOLVED` row with only
`OBSERVATION_BINDING_UNRESOLVED`, `FRESHNESS_UNRESOLVED`, or
`AUTHORITY_UNRESOLVED`. Confirmed rows also have null `errorCode`.
Classification stops at the first failed validation step.

### Transaction proof

Each writer must hold one cross-process guard from before the first possible
filesystem/security mutation through final byte/security read-back or verified
rollback. A real second `pwsh` process and deterministic barriers prove peer
exclusion. Tests must prove cleanup after acquisition failure and semantic
restoration of content/existence, owner, protection and complete ACE state.
Verification preserves both the exact canonical ordered ACE vector (including
multiplicity) and a separately sorted semantic tuple multiset for effective
access. No sort may erase the order oracle. Termination at prepublish,
post-temp-flush and pre-replace barriers must leave no target with a partial row
or non-final descriptor and must support deterministic recovery/cleanup.

## Acceptance Criteria

1. Exactly five worker paths exist and no real source or launcher is created.
2. Both tools default to non-mutating self-test and fail closed outside their
   exact principal/path/confirmation boundaries.
3. Positive vectors recompute, never copy, the accepted content and registry
   hashes and prove strict Party B snapshot byte identity.
4. Full adversarial coverage proves schema, encoding, hash, authority, chain,
   concurrency, DACL and rollback behavior with stable error classes.
5. UUID idempotency, three-argument evaluator adaptation, exact LF JSONL
   framing and receipt/no-receipt classification are deterministic and tested.
6. Publication is pre-hardened and response writes are copy-on-write crash
   atomic; ordered ACE and semantic effective-access checks both pass.
7. The exact three-field issuer-content profile is enforced; unsupported inner
   shapes fail closed without a broad RFC 8785 capability claim.
8. Local later performs a distinct independent process/security probe; worker
   return remains `PENDING_REVIEWER_EXECUTION`.
9. Acceptance reaches only `TOOLING_ACCEPTED_SOURCE_NOT_CREATED`.

## Evidence / Verification Boundary

Tool self-tests, Python tests, checker self-test, exact changed-set evidence,
parked-path hash equality and a final return hash binding are required. Static
or hermetic success is not evidence of real Party C/Party B execution, source
creation, observation, lookup, consumer binding or establishment.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`CODE_CHANGE`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_high_risk_local_transaction_proof.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | dispatch status, source-verification columns, closeability graph, high-risk applicability/JSON keys, protected-path authorization, trace labels and private export token |
| gateRunPurpose | confirm authored contract and packet shape; never substitute for runtime evidence |
| claimBoundary | baseline and tooling dispatch only |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | exact five worker paths | hermetic implementation/tests; no credentials, real source, staging or commit | this baseline and work order | local PowerShell/Python tooling | IMPLEMENTED |
| `EXTERNAL_AGENT_CLI_MCP` | no owner | no external ingress, auth, mutation, receipt or runtime claim | no authority | fresh source-verified packet required | DEFERRED_WITH_REASON |

## Finding-To-Governance Learning Disposition

Defect class: `ORCHESTRATOR_PACKET_GAP`. Learning lane:
`GOVERNANCE_CONTROL_PLANE`. Disposition: `RULE_EXISTS`. The C0 amendment and
high-risk transaction standard now prevent the earlier implicit byte,
authority and rollback decisions. No new foundation change is opened here.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: one five-path hermetic tooling packet can
implement the now-closed Group 4 contract without source effects.

Evidence Comparison Requirement: the worker compares every accepted positive
and adversarial vector with actual tool/checker/test evidence.

Contradiction Handling Requirement: any contract/tool mismatch is returned as
a named gap and no source or completion claim is made.

Claim Update Requirement: Local may confirm, narrow or reject tooling
acceptance only after independent review.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private local-principal and source-security tooling; no public-sync authority.

## Claim Boundary

This baseline authorizes only five uncommitted hermetic tooling outputs. It
does not create either Group 4 file, create a launcher, use credentials, run as
Party B/C, append a second observation or lookup response, perform T3E, bind a
consumer, establish a source, promote, admit, invoke a provider, export, deploy
or claim production readiness.
