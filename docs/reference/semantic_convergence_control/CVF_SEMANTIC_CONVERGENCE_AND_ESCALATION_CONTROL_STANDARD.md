# CVF Semantic Convergence And Escalation Control Standard

Memory class: governed-standard

Status: ACTIVE_STANDARD

docType: reference

Date: 2026-08-31

Batch ID: SCEC-T1

EPISTEMIC_PROCESS_NA_WITH_REASON: canonical control standard; it fixes a
machine-readable schema, invariant list, and claim-to-proof mapping, and does
not itself make a new evidence-comparison or hypothesis-testing claim beyond
the historical replay section, which cites concrete source packets directly.

## Purpose

Define one forward-only Semantic Convergence And Escalation Control (SCEC)
contract that binds a declared problem chain's progression to a stable
problem identity, blocker-set reconciliation, and claim-specific executable
proof. The control decides only whether a problem chain has enough declared
evidence to continue, must consolidate into an integrated root contract, or
must stop for architectural reassessment. It never inspects private
reasoning, chain-of-thought, or reasoning-trace content, never scores prose
quality, and never claims to determine semantic truth. It validates only
declared evidence shape: hashes, set algebra, schema fields, and dispositions.

## Scope / Applies To

Applies to any CVF-governed baseline, work order, or worker return that
declares an SCEC block using schema `cvf.semanticConvergenceControl.v1`.
Every new or changed governed work order and worker return must carry exactly
one active block after this standard's activation commit. Applies
forward-only: unchanged historical artifacts are not reopened, and committed
range checks use the standard's actual addition commit as the activation
boundary. Does not apply to product/runtime source, provider/live execution,
or public-sync artifacts.

Owner: CVF governance control plane
(`docs/reference/semantic_convergence_control/`). Neighboring plane:
`docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md`,
which governs dispatch/review invocation economics and explicitly does not
decide semantic progression. This standard does not add risk/value
classification, and the review-cost standard does not add semantic
progression logic.

## Machine-Readable Block Schema

An SCEC block is a fenced JSON object using schema
`cvf.semanticConvergenceControl.v1` with at least these fields:

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "stable-kebab-case-identity",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {
    "prior": [],
    "resolved": [],
    "retained": [],
    "new": [],
    "reopened": [],
    "current": []
  },
  "resolutionEvidence": {},
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0,
    "nonDecreasingBlockerTransitions": 0
  },
  "claims": [
    {
      "claimId": "string",
      "claimClass": "CONCURRENCY_EXACTLY_ONCE",
      "proofClass": "EXECUTABLE_ADVERSARIAL_CONCURRENCY_TEST",
      "evidenceRef": "string"
    }
  ],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

Field notes:

- `schemaVersion` must equal `cvf.semanticConvergenceControl.v1`.
- `problemKey` is a stable, non-empty identity string that must not change
  across a successor chain for the same declared problem.
- `chainMode` is `INITIAL` for the first block in a chain, or `SUCCESSOR` for
  any block naming a predecessor.
- `chainOrdinal` is a non-negative integer. `INITIAL` requires ordinal `0`.
  Each `SUCCESSOR` must strictly increase the ordinal by exactly `1` over its
  declared predecessor's ordinal.
- `predecessor` is `null` for `INITIAL`, or an object
  `{"path": "<repo-relative path>", "sha256": "<64 lowercase hex chars>"}` for
  `SUCCESSOR`. The declared hash must match the SHA-256 content hash of the
  predecessor artifact file at the cited path, recomputed by the checker, not
  trusted from the declaration.
- `blockerDelta` holds six blocker-ID arrays: `prior`, `resolved`, `retained`,
  `new`, `reopened`, `current`. See Set Reconciliation below.
- `resolutionEvidence` is an object keyed by blocker ID whose keys must equal
  `blockerDelta.resolved` exactly. Each value binds an `evidenceClass`
  (`ACCEPTED_REVIEW` or `EXECUTABLE_PROOF`), a normalized repository-relative
  `evidencePath`, an immutable `sha256`, a canonical non-empty `locator` that
  occurs exactly once in the hash-bound content, and an optional `claimId`
  that links an `EXECUTABLE_PROOF` resolution to a claim in this same block.
  An empty `resolved` requires an empty evidence map; the scaffold generators
  emit that safe default. See Resolution Evidence below.
- `counters` holds three cumulative non-negative integers
  (`partialReadyClosures`, `reviewerScopeExpansions`,
  `sameClaimCorrections`) plus the current consecutive streak of
  `nonDecreasingBlockerTransitions`. A successor may not decrease a
  cumulative counter. The non-decreasing streak must equal predecessor streak
  plus one when `|current| >= |prior|`, and must reset to zero when blockers
  decrease.
- `claims` is an array of claim records, each with `claimId` (non-empty
  string), `claimClass` (one of the six classes in Claim-To-Proof Mapping),
  `proofClass` (the matching minimum proof class or stronger), and
  `evidenceRef` (a non-empty pointer to the executable or documentary
  evidence, such as a test path or file path).
- `requiredDisposition` is one of the four allowed progression dispositions.
- `successorScope` is one of the four allowed successor scopes.

## Activation Sentinel

A governed artifact opts into SCEC validation by containing a fenced code
block whose content, once parsed as JSON, has
`"schemaVersion": "cvf.semanticConvergenceControl.v1"` as a real field value
(not a quoted example inside prose, a table cell, or a `literalTokensReviewed`
citation). The checker treats only a real parseable JSON object with that
field as an active block; a backtick-wrapped mention of the schema string
without valid enclosing JSON is not an activation and produces no failure per
invariant 11 below.

## Enforcement Invariants

The checker enforces exactly these thirteen invariants for every active block:

1. **Stable identity and monotonic ordinal.** The checker reads the actual
   predecessor artifact's single active SCEC block. `problemKey` must match
   it and `chainOrdinal` must equal predecessor ordinal plus exactly `1`,
   starting at `0` for `INITIAL`.
2. **Exact predecessor path/hash evidence.** A `SUCCESSOR` block's
   `predecessor.path` must exist in the repository and its recomputed
   SHA-256 must equal `predecessor.sha256` exactly. A missing file, unreadable
   file, or hash mismatch fails closed.
3. **Set reconciliation.**
   `prior = resolved union retained` and
   `current = retained union new union reopened`, both as exact set
   equality (no extra or missing IDs on either side).
4. **Valid disjointness and no silent blocker disappearance.** `resolved` and
   `retained` must be disjoint; `retained`, `new`, and `reopened` must be
   pairwise disjoint. Every ID in `prior` must appear in exactly one of
   `resolved` or `retained` - an ID present in `prior` but absent from both
   `resolved` and `retained` (silent disappearance) fails closed. A successor's
   `prior` must equal its actual predecessor's `current`; blocker arrays may
   not contain duplicate IDs.
5. **`ROOT_CONTRACT_REQUIRED` triggers.** `requiredDisposition` must be
   `ROOT_CONTRACT_REQUIRED`, `STOP_REASSESS_ARCHITECTURE` (a stronger
   escalation), or `READY_WITH_EXECUTABLE_PROOF` (the fully-resolved
   downstream state after a consolidated root contract ships with executable
   proof) whenever any of: cumulative `counters.partialReadyClosures >= 2`,
   cumulative `counters.reviewerScopeExpansions >= 1`, or cumulative
   `counters.sameClaimCorrections >= 2` (a repeated same-claim correction).
6. **`STOP_REASSESS_ARCHITECTURE` triggers.** `requiredDisposition` must be
   `STOP_REASSESS_ARCHITECTURE` whenever the consecutive streak
   `counters.nonDecreasingBlockerTransitions >= 2` (two consecutive
   transitions where `|current| >= |prior|` with no net blocker reduction).
7. **No narrow successor after escalation.** Once a block's
   `requiredDisposition` is `ROOT_CONTRACT_REQUIRED` or
   `STOP_REASSESS_ARCHITECTURE`, its own `successorScope` must not be
   `INITIAL_BOUNDED`; only `INTEGRATED_ROOT_CONTRACT`, `NO_SUCCESSOR`, or
   `EXECUTABLE_IMPLEMENTATION` (when paired with `READY_WITH_EXECUTABLE_PROOF`)
   are allowed. There is deliberately no post-escalation narrow-gap token.
   A predecessor at `STOP_REASSESS_ARCHITECTURE` cannot have another
   successor in the same problem chain. A predecessor at
   `ROOT_CONTRACT_REQUIRED` cannot have its escalation or integrated scope
   reset by a successor.
8. **No runtime readiness from documentation-only proof.** A block whose
   `requiredDisposition` is `READY_WITH_EXECUTABLE_PROOF` must not contain any
   claim whose `proofClass` is `PROPOSAL_ONLY_NO_RUNTIME_READINESS`.
9. **Claim-to-proof minimums.** Every claim's `proofClass` must equal the
   mapping for its `claimClass`, including exact
   `OTHER -> NAMED_OBSERVABLE_PROOF`. `READY_WITH_EXECUTABLE_PROOF` requires
   at least one claim and pairs only with `EXECUTABLE_IMPLEMENTATION`; that
   scope is invalid under every other disposition.
10. **Forward-only activation.** The checker validates artifacts changed in
    the given `--base..--head` range or working-tree/staged diff. New or
    changed governed work orders and worker returns after activation fail if
    their required block is absent. An unchanged historical artifact is never
    re-validated or reopened by a later run that does not touch it.
11. **Quoted/example marker immunity.** A schema string or field name
    appearing only inside backticks, inside a markdown table cell describing
    the schema, or inside prose citing the standard, without a real enclosing
    parseable JSON object containing that field, must never be treated as an
    active block and must never produce a false-positive violation.
12. **Fail-closed on malformed or incomplete active blocks.** Once a fenced
    block parses as JSON and contains the `schemaVersion` field with the
    exact SCEC value, any missing required field, wrong JSON type, invalid
    enum value, or structural violation of invariants 1-9 or 13 is a hard
    failure. A block that is present but cannot be fully validated is never
    treated as passing by default.
13. **Per-resolved-blocker evidence binding.** Every blocker ID in
    `blockerDelta.resolved` must have exactly one `resolutionEvidence` record;
    no missing, extra, or duplicate binding passes. Each record must bind an
    `evidenceClass` (`ACCEPTED_REVIEW` or `EXECUTABLE_PROOF`), a normalized
    repository-relative `evidencePath` (no absolute, drive, backslash, or
    traversal path), an immutable 64-character lowercase hex `sha256`, and a
    canonical non-empty `locator` equal to its own trimmed form. The checker
    reads each referenced path once per validation tree as bytes and uses that
    cached snapshot for both the SHA-256 comparison and strict-UTF-8 locator resolution. It
    rejects a missing or unreadable path, an unsafe path, a hash mismatch, an
    empty or non-canonical locator, non-UTF-8 content, a locator that does not
    occur, a locator that occurs more than once, and an invalid claim link.
    A locator's unique textual occurrence is an addressability check within the
    cited file only; it does not establish relevance, correctness, or semantic
    truth. An `EXECUTABLE_PROOF` binding must link a `claimId` to a claim in
    the same block whose `proofClass` satisfies the claim-to-proof mapping
    (that is, not `PROPOSAL_ONLY_NO_RUNTIME_READINESS`). An `ACCEPTED_REVIEW`
    binding exposes the declared reviewer authority for inspection. An empty
    `resolved` requires an empty evidence map. When a successor consumes its
    predecessor, the checker revalidates the predecessor's resolution-evidence
    hashes and locators against the current referenced files; evidence or
    locator drift cannot inherit trust silently.

## Claim-To-Proof Mapping

| Claim class | Required minimum proof class |
|---|---|
| `CONCURRENCY_EXACTLY_ONCE` | `EXECUTABLE_ADVERSARIAL_CONCURRENCY_TEST` |
| `CRASH_RECOVERY` | `EXECUTABLE_STATE_TRANSITION_CRASH_TEST` |
| `ORDERING` | `EXECUTABLE_SEQUENCE_ASSERTION` |
| `SCHEMA_COMPATIBILITY` | `EXECUTABLE_BUILDER_VALIDATOR_CONTRACT_TEST` |
| `DOCUMENTATION_ONLY` | `PROPOSAL_ONLY_NO_RUNTIME_READINESS` |
| `OTHER` | `NAMED_OBSERVABLE_PROOF` |

These are exact mappings; no additional narrow-gap or synonym proof token is
authorized outside this table without a fresh, source-verified revision of
this standard.

## Allowed Progression Dispositions

- `CONTINUE_BOUNDED`
- `ROOT_CONTRACT_REQUIRED`
- `STOP_REASSESS_ARCHITECTURE`
- `READY_WITH_EXECUTABLE_PROOF`

## Allowed Successor Scopes

- `INITIAL_BOUNDED`
- `INTEGRATED_ROOT_CONTRACT`
- `NO_SUCCESSOR`
- `EXECUTABLE_IMPLEMENTATION`

There is deliberately no post-escalation narrow-gap successor token.

## Resolution Evidence

Each resolved blocker binds exactly one record under `resolutionEvidence`,
keyed by blocker ID. Example accepted-review binding:

```json
{
  "BLOCKER_ID": {
    "evidenceClass": "ACCEPTED_REVIEW",
    "evidencePath": "docs/reviews/CVF_EXAMPLE_WORKER_RETURN_2026-08-31.md",
    "sha256": "0000000000000000000000000000000000000000000000000000000000000000",
    "locator": "Independent Reviewer Correction"
  }
}
```

For an executable resolution, use `EXECUTABLE_PROOF` and add a `claimId` that
names a claim in the same block whose `proofClass` satisfies the claim-to-proof
mapping:

```json
{
  "BLOCKER_ID": {
    "evidenceClass": "EXECUTABLE_PROOF",
    "evidencePath": "governance/compat/test_check_semantic_convergence_control.py",
    "sha256": "0000000000000000000000000000000000000000000000000000000000000000",
    "locator": "ResolutionEvidenceBindingTests",
    "claimId": "SCEC-T1-R2-CHECKER-AND-REPLAY-HARDENING"
  }
}
```

The checker reads each `evidencePath` once per validation tree as bytes; the
same cached snapshot is used to recompute the SHA-256 and resolve every locator
bound to that path. The locator must be a
canonical non-empty string that occurs exactly once in the strict-UTF-8-decoded
content. A missing or unreadable file, unsafe path, wrong hash, empty or
non-canonical locator, non-UTF-8 content, absent locator, or ambiguous locator
fails closed with a stable violation code. Unique textual occurrence proves
addressability only, never that the located statement is relevant, correct, or
true; reviewer authority still decides semantic truth. Successor validation
revalidates each predecessor binding against the same bytes, so a later
evidence-target change or locator drift fails the predecessor validity check.
No broad retroactive scan of unchanged artifacts is introduced.

## Historical Regression Replay

`governance/compat/fixtures/semantic_convergence_control/gc010_t1j_r1_r3_replay.json`
encodes the corrected GC-010 T1J-R1-through-R3 history as accepted states and
worker/reviewer candidate variants built from the accepted worker
returns at
`docs/reviews/CVF_GC010_SCR_R2_T1J_R2_APPROVAL_RESUME_ATOMIC_CLAIM_DURABLE_OWNER_DECISION_WORKER_RETURN_2026-08-31.md`
and
`docs/reviews/CVF_GC010_SCR_R2_T1J_R3_PENDING_RUNTIME_ROUTE_INTEGRATION_INTERFACE_DECISION_WORKER_RETURN_2026-08-31.md`.
It proves: the stable problem chain identity across R1/R2/R3; R2's narrowed
single remaining gap (connection-lifetime/storage-path ownership) and the
reviewer's scope expansion that added payload/environment/policy
requirements; R3's exactly-once claim (an `ApprovalStore.delete()`-based
single-winner assumption) and the reviewer's correction rejecting it; and,
under this standard, why a fourth narrow R4-style continuation would be
rejected once one reviewer scope expansion has already been recorded - the
required disposition first escalates to `ROOT_CONTRACT_REQUIRED`. The
accepted R1-to-R2 and R2-to-R3 blocker counts are also two consecutive
non-decreasing transitions, so the corrected R3 state reaches the stronger
`STOP_REASSESS_ARCHITECTURE` / `NO_SUCCESSOR` terminal. A same-problem R4
successor is therefore rejected rather than pre-declared implementation
ready. This fixture is regression evidence only;
it does not rewrite, reopen, or activate the historical T1J-R1/R2/R3 work
orders themselves.

## Claim-Boundary And Non-Goals

- The checker validates only declared evidence shape: hashes, set algebra,
  schema fields, enum tokens, and dispositions.
- It never inspects chain-of-thought, private reasoning, or reasoning-trace
  content.
- It never scores prose quality, writing style, or "how good" an argument is.
- It never determines semantic truth; a claim's `proofClass` being present
  and matching the minimum mapping is a shape check, not a correctness
  verdict. Reviewer judgment remains the authority on whether the cited
  evidence is actually sound.
- It grants no GC-010 product/runtime, provider/live, public-sync, or
  deployment authority.

## Adoption Rule

New governed work orders and worker returns emit an initial or successor SCEC
block by default via
`governance/compat/build_dispatch_packet_scaffold.py` (dispatch side) and
`governance/compat/build_worker_return_skeleton_scaffold.py` /
`governance/compat/run_worker_return_scaffold.py` (return side). Defaults
must never fabricate a predecessor hash, proof evidence, or readiness;
missing successor facts must fail closed or emit an explicit unresolved
sentinel (`SCEC_PREDECESSOR_HASH_UNRESOLVED`) that this standard's checker
rejects pre-dispatch.

Worker-return skeletons must emit an unresolved `SUCCESSOR` state by default,
not a fresh valid `INITIAL` state, so authors cannot reset a chain by leaving
scaffold defaults unchanged. Any internal scaffold opt-out exists only for
legacy golden-fixture generation; the public CLI does not expose a SCEC
omission flag, and the checker rejects missing blocks on governed outputs.

## Verification

```powershell
python -m unittest governance.compat.test_check_semantic_convergence_control
python governance/compat/check_semantic_convergence_control.py
```

## Rollback

Remove the checker from `_common_commands` and the three local hook catalogs;
retain the standard as historical reference. Rolling back does not reopen or
invalidate any already-accepted governed artifact's other, non-SCEC content.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | delegated governance implementation worker |
| Provider or surface | local private provenance workspace |
| Session or invocation | SCEC-T1-R2 blocker resolution evidence binding and historical replay correction, 2026-08-31 |
| Working directory | repository root |
| Command or tool surface | governed reads, local shell verification, and local file edits; no provider or network call |
| Target paths | this standard; `governance/compat/check_semantic_convergence_control.py`; its focused tests; the replay fixture; both worker-return scaffold producers; ADIF-0055; the worker return |
| Allowed scope source | `docs/work_orders/CVF_AGENT_WORK_ORDER_SCEC_T1_R2_BLOCKER_RESOLUTION_EVIDENCE_BINDING_AND_HISTORICAL_REPLAY_CORRECTION_2026-08-31.md` |
| Before status evidence | the standard had no per-resolved-blocker evidence binding; set algebra alone validated `resolved` transitions |
| After status evidence | `resolutionEvidence` field, field notes, invariant 13, and a Resolution Evidence section are added |
| Diff evidence | `git diff --name-status` shows this standard among the eleven SCEC-T1-R2 paths |
| Approval boundary | SCEC foundation hardening only; no product/runtime, provider/live, public-sync, deployment, or production claim |
| Claim boundary | declared-evidence-shape control only; no semantic-truth-scoring or reasoning-trace-inspection claim |
| Agent type | worker |
| Invocation ID | `scec-t1-r2-resolution-evidence-binding-2026-08-31` |
| Expected manifest | the eleven-path SCEC-T1-R2 fulfillment manifest |
| Actual changed set | the eleven-path SCEC-T1-R2 fulfillment manifest |
| Manifest delta | MATCH |

## Claim Boundary

This standard defines a declared-evidence-shape control only. It does not
claim semantic-truth scoring, reasoning-trace inspection, GC-010 product
readiness, provider/live execution, public-sync, or deployment authority.
Passing this standard's checker proves the declared SCEC contract's shape is
valid, not that the underlying engineering decision is correct.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance foundation standard. Public export, if
ever desired, requires a separate reviewed public-sync batch.
