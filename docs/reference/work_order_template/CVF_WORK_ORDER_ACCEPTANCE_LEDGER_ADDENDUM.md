# CVF Work Order Acceptance Ledger Addendum

Memory class: STANDARD_ADDENDUM

Status: ACTIVE_ADDENDUM

docType: reference

providerExecutionAuthority: FORBIDDEN

## Purpose

Define the machine-readable join from dispatcher-owned requirements to actual
artifacts, proof, and a deterministically reduced worker terminal status.

## Scope / Applies To

This addendum applies to changed executable implementation work orders, their
worker returns, dispatch/return scaffolds, and the gates that admit them.
Dispatcher, implementation worker, reviewer, and closer retain their existing
phase authorities; this contract adds no provider or external-effect authority.

## Contract

Executable work orders use one fenced `acceptance-ledger-json` object with
`schemaVersion: cvf.workOrderAcceptanceLedger@1.0.0`, a nonempty
`requirements` array and a nonempty `proofCatalog`. Each requirement has a
unique `requirementId`, boolean `mandatory`, nonempty repo-relative
`expectedArtifacts`, and nonempty `requiredProofIds`. Each proof has a unique
`proofId`, `kind` and nonempty `locator`.

Worker returns use one fenced `acceptance-evidence-json` object with
`schemaVersion: cvf.workOrderAcceptanceEvidence@1.0.0`, `executionBaseHead`,
and exactly one result per requirement. Each result binds `requirementId`,
`actualArtifacts`, `proofRefs`, and `status` (`PASS` or `BLOCKED`).

## Oracle And Reducer Rules

- Expected artifacts come only from the committed work-order ledger.
- Actual artifacts come from Git observation from `executionBaseHead`, not worker prose.
- Returned, expected, and Git-observed artifact unions must agree exactly.
- Every required proof ID must be bound by the matching evidence row.
- Missing, duplicate, unknown, malformed or unparseable rows fail closed.
- `COMPLETE_PENDING_REVIEW` is valid only when every mandatory row is `PASS`.
- Any mandatory row not `PASS` requires `BLOCKED_WITH_REASON`.

Machine check: `governance/compat/check_work_order_acceptance_ledger.py`.

## Near-Threshold And Fulfillment Manifest Rules

When an active owner is inside the GC-023 near-hard margin, name the path,
current count, hard threshold, extraction/split target, new helper path,
`Minimum shrink target: 50 lines`, post-change count command and write
ownership. The entrypoint cannot simultaneously be forbidden.

The acceptance ledger is the canonical Required Artifact and Required Proof
manifest. Human-readable tables may summarize it but cannot change its rows.
Forbidden paths, forbidden filesystem state and pre-existing dirty exemptions
remain explicit prose tables. A non-N/A expected manifest that yields no
concrete repo path is invalid, not an instruction to skip comparison.

## Epistemic Process Block

Expected Result / Prediction: an exact dispatcher/worker/Git join rejects every
missing, extra, unknown, malformed, proof-unbound, or terminally contradictory row.

Evidence Comparison: positive and hostile fixtures exercise each rejection
class through the dedicated checker and worker-return fast gate.

Contradiction Or Gap Disposition: any union or reducer mismatch is a hard
violation; prose cannot waive it.

Claim Update: acceptance is now an explicit machine-reduced chain rather than
a worker self-report.

## Claim Boundary

This addendum governs repository packet acceptance. It does not observe files
outside Git, prove semantic correctness by itself, control external tools, or
authorize runtime/provider/public effects.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
