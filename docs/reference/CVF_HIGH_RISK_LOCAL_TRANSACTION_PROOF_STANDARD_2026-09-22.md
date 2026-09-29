# CVF High-Risk Local Transaction Proof Standard

Memory class: governed-standard

Status: ACTIVE_REFERENCE

docType: reference

Date: 2026-09-22

## Purpose

Require an explicit, machine-checkable proof contract when a current work
order authorizes high-risk local transactions. The contract binds real peer
exclusion, exception-safe guard ownership, semantic security rollback, and
final evidence integrity to observable acceptance outcomes.

## Scope / Applies To

The owner is the CVF governance control chain. This standard applies to new
or changed work orders authorizing cross-process locking, durable append or
write with rollback, ownership/DACL mutation, or post-acquire failure handling.
Any one risk family is sufficient; multiple families are not required.

The changed-file checker reads executable-scope declarations in operational
sections such as Allowed Scope, Implementation Contract, and Execution Plan.
Quoted examples, fenced teaching material, historical descriptions, and
forbidden-scope statements are not authorization. Reference documents and
unchanged historical work orders are outside this forward-only adoption.
A static guard-authoring task that merely describes these risks must identify
its documentation/checker-only boundary clearly; it does not authorize the
target transactions described by its fixtures.

## Applicability Declaration

An applicable work order carries exactly one standalone, unfenced declaration:

```text
High-Risk Local Transaction Proof Applicability: REQUIRED
```

An author may instead declare the following only when the work order has no
authorized high-risk operation:

```text
High-Risk Local Transaction Proof Applicability: NOT_APPLICABLE_WITH_REASON - documentation-only correction; no target transaction is authorized
```

Replace that example reason with the actual scope justification. A risk
trigger plus non-applicability is a contradiction and fails closed. Omitting
the declaration from a triggered work order also fails. An explicit REQUIRED
declaration opts into all contract requirements even without a risk trigger.
Duplicate declarations, placeholders, and partial contracts are invalid.

## Contract Shape

A REQUIRED work order contains exactly one section named
`High-Risk Local Transaction Proof Contract`, at heading level two, containing
one fenced JSON object with the nine keys in the example below. JSON duplicate
keys, unknown keys, wrong value types, missing fields, placeholder strings,
and unsupported enum values fail. Nested objects have the exact key sets
shown; arrays identify the exact complete members without duplicates. Their
order is immaterial except for the barrier event array, which fixes the order.

The example is a contract plan, not evidence that its named fixture exists
or any test has passed. Replace `transactionTarget`, `invocationPath`, and
`mutationPath` with task-specific, source-verified targets before dispatch.

```json
{
  "transactionTarget": "local observation append and security rollback",
  "productionPathPeer": {
    "kind": "REAL_SECOND_PROCESS",
    "invocationPath": "scripts/acel_g1_party_b_group3_observation_writer.ps1",
    "mutationPath": "guarded observation append transaction"
  },
  "deterministicBarrierProtocol": {
    "events": ["READY", "START_ATTEMPT", "ATTEMPTING", "PARENT_RELEASE", "ENTERED", "COMPLETE"],
    "timeoutRole": "DEADLOCK_SAFETY_ONLY"
  },
  "enteredBeforeReleaseOracle": "REJECT_ENTRY_BEFORE_PARENT_RELEASE",
  "postAcquireFailureInjection": {
    "point": "AFTER_ACQUIRE_BEFORE_MUTATION",
    "cleanupProof": "SUBSEQUENT_PEER_ACQUIRES"
  },
  "semanticSecurityTuple": {
    "fields": ["ownerSid", "protectionState", "inheritanceState", "aces"],
    "aceFields": ["sid", "rights", "accessType", "isInherited", "inheritanceFlags", "propagationFlags"],
    "normalization": "SORT_COMPLETE_ACE_TUPLES"
  },
  "rollbackExactness": {
    "comparison": "SEMANTIC_PRESTATE_EQUALS_POST_ROLLBACK",
    "adversaries": ["EXTRA_ALLOW", "DENY", "INHERITED", "WRONG_OWNER"]
  },
  "finalEvidenceHashBinding": {
    "algorithm": "SHA256",
    "scope": "EXACT_RETURN_BYTES",
    "capture": "BEFORE_AND_AFTER_FINAL_REQUIRED_GATE",
    "equality": "REQUIRED",
    "postGateMutation": "FORBIDDEN"
  },
  "independentProbeRequired": {
    "required": true,
    "owner": "LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER",
    "workerReturnDisposition": "PENDING_REVIEWER_EXECUTION"
  }
}
```

## Evidence Semantics

| Field | Required meaning and acceptance evidence |
| --- | --- |
| `transactionTarget` | Name the actual protected operation and its transaction boundary, including write, security update/readback, final validation, and rollback where applicable. |
| `productionPathPeer` | A real second OS process invokes the actual guarded mutation path. A mutex-only helper, source-shape assertion, in-process thread, or simulated contender does not establish this obligation. Bind the invocation to the production entrypoint and show the peer reaches its protected mutation boundary. |
| `deterministicBarrierProtocol` | READY establishes peer readiness; START_ATTEMPT releases the attempt; ATTEMPTING establishes the attempt while the parent owns the guard; PARENT_RELEASE marks release; ENTERED records peer entry; COMPLETE records completion. Explicit handshakes and observed events prove ordering. A timeout is only deadlock safety and its expiry is never evidence of exclusion. |
| `enteredBeforeReleaseOracle` | A peer entry observed before parent release is a failing result. The test must exercise the negative oracle as well as observing post-release entry; lack of an event during a delay is insufficient. |
| `postAcquireFailureInjection` | Inject failure after successful guard acquisition and before mutation, exercising the owning production path. A subsequent peer acquisition demonstrates cleanup. Constructor/initialization failure must not strand ownership when the caller has not yet received a guard handle. |
| `semanticSecurityTuple` | Read back owner SID, protection and inheritance state, and every ACE. Normalize complete ACE tuples with SID, rights, allow/deny access type, inherited status, inheritance flags, and propagation flags. Preserve multiplicity; sorting must not drop deny, inherited, or extra entries. Textual ACL/SDDL equality or a permitted-SID subset is insufficient. |
| `rollbackExactness` | Compare captured semantic pre-state to read-back post-rollback state, plus exact content/existence state relevant to the transaction. Exercise EXTRA_ALLOW, DENY, INHERITED, and WRONG_OWNER adversaries. Restore the captured state rather than silently substituting a preferred ACL. |
| `finalEvidenceHashBinding` | Hash the exact final return bytes using SHA-256 immediately before and after the final required gate. Both values must match; any change invalidates the receipt and requires finalization and the required gate again. Do not normalize line endings, omit fields, or hash a semantic projection. |
| `independentProbeRequired` | The Local reviewer performs a separately executed probe with an independent assertion path. The worker returns PENDING_REVIEWER_EXECUTION and cannot self-certify reviewer execution. Model identity alone does not establish independence. |

These are evidence outcomes, not instructions for the worker's internal
reasoning or a mandatory language/library. The chosen mechanism must make the
declared ordering and security comparisons observable. If a platform cannot
represent the required security state, disclose the limitation for a governed
contract amendment; do not replace missing fields with empty success values.

## Final Evidence Capture Procedure

Finish all material edits, test results, return text, and pending-probe
disposition before capture. The return names the gate command and the detached
receipt destination or command-output channel. Capture `preGateReturnSha256`,
run the final required gate, capture `postGateReturnSha256`, and compare them.
The receipt records the exact return path, gate command/result, both digests,
and `NO_POST_GATE_MUTATION`. Preserve it outside the frozen return in an
authorized evidence path or execution transcript.

A file cannot truthfully embed its own exact-byte digest by editing itself
after capture. Do not insert the newly computed hashes back into that return.
The return may reference the detached receipt before freezing. Any required
content correction starts a fresh capture/gate/capture sequence; the earlier
receipt stays superseded evidence. Reviewer repairs also require renewed
validation and a new binding before acceptance.

## Enforcement / Verification

Machine checker: `governance/compat/check_high_risk_local_transaction_proof.py`.
Focused regression owner:
`governance/compat/test_check_high_risk_local_transaction_proof.py`.

The checker accepts `--base`, `--head`, and `--enforce`, operates on changed
work orders including pending worktree artifacts, and emits path-specific,
actionable diagnostics. Findings return exit 1 under `--enforce`; advisory
mode reports them without asserting success. Malformed or incomplete required
contracts fail closed. Non-applicability cannot override an authorized risk.

The checker is wired once into reviewer-fast, pre-commit, and pre-push through
the extracted local hook catalogs. Reviewer-fast is the earliest relevant
admission point in this bounded integration. Existing guards remain in force.
The checker does not execute target transactions, inspect OS security state,
or establish that declared runtime evidence is true.

Positive coverage includes complete required contracts, reasoned safe
non-applicability, and quoted/forbidden/historical non-authorization. Negative
coverage includes omitted applicability, each missing field, false
non-applicability, duplicate/unknown JSON fields, a shape-only peer,
timeout-as-proof, incomplete security tuples, incomplete rollback adversaries,
and weakened final-digest requirements. Unchanged history remains untouched.

## Roles And Review Boundary

The dispatcher classifies the operation and binds this contract before
implementation. The worker supplies task-specific command/file evidence and
retains pending reviewer status. The Local reviewer consumes valid returned
evidence, executes the independent probe, resolves contradictions, and owns
acceptance. A contract passing static admission is only a checked declaration.

## Related Artifacts

- `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md`
- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
- `docs/reference/guard_orientation/README.md`
- `docs/baselines/CVF_GC018_HIGH_RISK_LOCAL_TRANSACTION_PROOF_FOUNDATION_T1_2026-09-22.md`

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance foundation; public export is separate.

## Claim Boundary

This standard defines static authoring admission and evidence obligations.
Its declarations do not prove concurrency safety, rollback correctness,
Windows ACL behavior, completed independent review, provider/live governance,
source establishment, candidate admission, deployment, or production readiness.
