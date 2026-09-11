# Committed Evidence Fingerprint Contract Worker Return

Memory class: FULL_RECORD

docType: review

Status: COMPLETE_PENDING_REVIEW

## Operator-Authorized Local Scope Amendment - 2026-09-12

Operator explicitly approved the Local reviewer's request to add only `docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json` for the two SOURCE_DRIFT fingerprints, with
amendment/evidence in this existing packet. This narrowly supersedes the original registry prohibition for this Local action only. The dispatched worker manifest and dispatch
packet hashes stay frozen. Current pending scope is twelve paths: eleven worker paths plus the named map. No other registry, semantic verdict, continuity, pilot, staging,
commit or push change is authorized by this amendment.

Bounded source review: `git diff -- governance/compat/run_agent_autorun_workflow_gate.py governance/compat/agent_autorun_machine_verification.py` shows additive
committed-evidence admission and integrity-covered validation. The first source retains CLI PASS/FAIL and the v3 JSON receipt writer; the second retains canonical receipt
composition/digest/integrity ownership. Neither delta adds a unified Web inventory or changes the lane's operator visibility gap. These two evidence roles remain
source-supported. The PARTIAL posture and PARTIAL_OPERATOR_VISIBILITY_BY_ENFORCEMENT_CLASS verdict are preserved; historical testedBy counts are not promoted to current proof.
This is acceptance of the two source-role mappings for freshness only, not whole-tranche closure, a five-lane re-audit or live-proof acceptance.

Fingerprint evidence: `Get-FileHash` with SHA256 over the two source files:

| Source | Previous SHA256 | Reviewed SHA256 |
|---|---|---|
| governance/compat/run_agent_autorun_workflow_gate.py | cee3f8e20f626f2105219d8aa7189b92ef03f646a67e0f7eebb85ce3d284a77b | 03a2f035478841ea6359c983850dca59bcb5692e77d64dca72e621a922a2625e |
| governance/compat/agent_autorun_machine_verification.py | 8280a95e0985bd1273aa359afff455be1d18346e8b49cb92e9746922d835d022 | 8f12da95ddbdaf8974c9d18b3bac3d2ee99ea480bc44c0af3095f80b7e95ab06 |

Only those two hash values change in the map. lastVerifiedDate remains
2026-09-01; no blanket freshness-age renewal is claimed. Rollback is limited
to restoring those two prior values and recording rejection of this amendment; do not revert worker implementation. Checker source read-ahead completed for
check_system_chain_map_freshness.py: REQUIRED_TOP_KEYS, REQUIRED_LANE_KEYS, TOP_LEVEL_FINGERPRINT_KEYS and the read-only SHA256 validation path.
Actor: Local reviewer; invocation: mfrp-fingerprint-map-refresh-2026-09-12.
Verification: `python governance/compat/check_system_chain_map_freshness.py --enforce`
returned exit 0, CURRENT, zero violations on 2026-09-12. `python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return
--base 9abb0bdfe --head HEAD --enforce` returned exit 0: 68/68 reviewer-fast checks PASS; worker-return fast gate PASS in 4.79 seconds; diff
hygiene PASS. The 172 focused test result above is reused because this amendment changes metadata and report only. SOURCE_DRIFT is resolved for the reviewed pending bytes, not
waived. Three previously disclosed consumer failures remain outside this amendment; no full-suite-green or closure claim. HEAD remains 9abb0bdfe, staging empty.

## Local Repair Verification - 2026-09-12

Current repair record supersedes generation 3 admission and gate claims. Operator explicitly authorized Local reviewer to repair the two findings. No new tranche, staging,
commit, registry or continuity edit is authorized.

Before repair, isolated real-writer/finality chain probes admitted both a NUL-containing binary CRLF/LF change and a `-text` CRLF/LF change at a clean later commit.
Unconditional two-sided normalization was the cause. Admission now uses exact bytes by default; its checkout exception requires the index blob to match target, metadata to
authorize CRLF checkout, no unsupported transform, and a control-free LF target whose expansion matches disk exactly. Neither fingerprint recipe changes. Unsupported cases
reject.

Contract/schema/path/authority/test/range/commit-plan matrix: existing v3 schema and raw identity preserved; existing eleven-path authority retained; historical index drift
and binary/-text differences rejected; legitimate checkout and continuity tests retained; base remains
9abb0bdfe; no commit or closure planned in this repair. MFRP safety contradiction justifies the focused rerun; no per-row evidence recreation or
broad consumer rerun.

Command evidence: `python -m pytest governance/compat/test_committed_evidence_fingerprint.py governance/compat/test_run_agent_autorun_workflow_gate.py
governance/compat/test_agent_autorun_machine_verification.py governance/compat/test_mfrp_shadow_canary_autocollect.py -q` returned exit 0, 172 passed in 66.68 seconds. The
added `test_real_chain_newline_semantic_drift_is_rejected` covers both reviewer counterexamples using the existing isolated chain fixture. Production gate commands remain
isolated; no provider/live proof or closure is claimed.

EQC correction: removed the unsupported byte-equivalence assertions from two historical gate rows and marked those reports superseded. Prior Local preflight observed both
SOURCE_DRIFT and EQC failures, not SOURCE_DRIFT only. Post-edit command: `python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return --base
9abb0bdfe --head HEAD --enforce`.
Result: exit 1; 67/68 reviewer-fast checks pass, EQC passes, sole failing
checker is system-chain freshness (two SOURCE_DRIFT source hashes). Fast gate duration: 4.96 seconds. `git diff --check` passes; Git reports an LF-to-CRLF checkout warning for
the edited chain-test file, not a whitespace violation. HEAD remains 9abb0bdfe2123bccd5749cd0f90148d44cbe0424, staging empty, eleven pending paths. The three previously
reported consumer failures were not rerun or claimed repaired. No closure acceptance issued.

Checker read-ahead: `governance/compat/check_equivalence_claim_evidence.py` constants EQUIVALENCE_PHRASES, DISPOSITION_TOKENS and EVIDENCE_WINDOW read before report repair.
Existing protected-path authorization remains in force.
Actor: Local reviewer; invocation: mfrp-fingerprint-local-repair-2026-09-12.
Scope: helper, existing chain-test file, contract and this return only.
Diff evidence: `git diff --name-status`; aggregate pending manifest remains eleven paths. Status remains COMPLETE_PENDING_REVIEW, not accepted/closed.

Self-declared worker-return artifact: yes

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_FINGERPRINT_T1_2026-09-11.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_FINGERPRINT_T1_2026-09-11.md`

executionBaseHead: `9abb0bdfe2123bccd5749cd0f90148d44cbe0424`

rawMemoryReleased=false
contractProfile: WORKER_RETURN_FULL_GATE_V1

## Rework Notice (Generation 1)

This is a consolidated rework of the original worker return, not a new tranche. `executionBaseHead` is unchanged from the original submission
(`9abb0bdfe2123bccd5749cd0f90148d44cbe0424`); no reset, stash, or overwrite of the prior implementation occurred -- the original nine-path delta was read and extended in
place. This rework addresses four findings (F1-F4) raised against the original submission. See "Rework Findings F1-F4" below for the finding-by-finding record. The original
submission's own recorded results (Gate Evidence, Command Evidence, Return-Time Closeability Recheck below this notice) are preserved unedited as historical record; this
notice and the new "Rework Findings F1-F4" / "Rework Verification" /
"Rework Return-Time Closeability Recheck" sections below record what
changed and the current (post-rework) actual results. Where the two disagree, the rework sections are current; the original sections are historical-only and are not silently
upgraded to PASS.

## Rework Notice (Generation 2)

This is a second consolidated rework, addressing two Local-review findings raised against generation 1's implementation: F1 (historical-target admission was still insufficient
-- a pure before/after worktree-stability comparison cannot distinguish a worktree that reflects `headSha` from one that is merely stable while parked at a later commit whose
evidence paths have already drifted) and F4 (the end-to-end test class mocked `_write_receipt`, `_closure_worktree_finality_failures`, and `_range_shape_preflight` beyond the
declared gate-command-only isolation, and its isolation declaration and minimum test matrix were incomplete). `executionBaseHead` remains unchanged at
`9abb0bdfe2123bccd5749cd0f90148d44cbe0424`; no reset, stash, or overwrite occurred. Generation 1's own sections (Findings / Position, Risk / Corrective Action, Rework Findings
F1-F4, Gate Evidence, Rework Verification, both Return-Time Closeability Recheck sections) are preserved unedited as historical record. This notice and the new "Rework
Findings F1 And F4 (Generation 2)" / "Rework-2 Verification" / "Rework-2 Return-Time Closeability Recheck" sections below record what changed in this second round and the
current actual results. Where sections disagree, the generation-2 sections are current.

## Rework Notice (Generation 3)

This is a third consolidated rework, addressing one Local-review finding raised against generation 2's implementation: F1 (clean-filter equivalence does not imply semantic
equivalence). Generation 2's `verify_worktree_matches_committed_target` decided worktree-vs-committed equivalence via `git hash-object`, which executes whatever `clean` filter
`.gitattributes`/`filter.<name>.clean` configures. Local review reproduced a real Git fixture where a `clean` filter configured to always emit the fixed bytes `target` let a
worktree file containing completely different, genuinely drifted content still hash identically to the committed target
-- `git status` reported clean, `verify_worktree_matches_committed_target`
returned `True`, and the producer bound `committedEvidence` for content the gate never actually verified. The governing byte-recipe contract explicitly forbids clean/smudge
filter execution anywhere in this admission path, which generation 2's guard violated. `executionBaseHead` remains unchanged at `9abb0bdfe2123bccd5749cd0f90148d44cbe0424`; no
reset, stash, or overwrite occurred. Generations 1 and 2's own sections are preserved unedited as historical record. This notice and the new "Rework Findings F1 (Generation
3)" / "Rework-3 Verification" / "Rework-3 Return-Time Closeability
Recheck" sections below record what changed in this third round and the current actual results. Where sections disagree, the generation-3 sections are current.

## Purpose

Repair the recurring worktree/Git-object fingerprint contradiction (the rejected `ATTEMPT-a4ec8bfaa9c112ca` CRLF/LF representation mismatch) while preserving raw worktree
cache-invalidation identity, receipt integrity, and P4-C1 collector safety exactly as authorized by the paired work order and baseline.

## Target / Source

`docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_FINGERPRINT_T1_2026-09-11.md` and its paired baseline `docs/baselines/CVF_GC018_MFRP_FINGERPRINT_T1_2026-09-11.md` are the sole
dispatch authority. `dispatchBaseHead=a6823f497` is a proven ancestor of `executionBaseHead=9abb0bdfe2123bccd5749cd0f90148d44cbe0424` (`git merge-base --is-ancestor a6823f497
9abb0bdfe` exit 0; two intervening dispatch/continuity commits: `cda03fa14`, `9abb0bdfe`). Worktree and staging were clean at `executionBaseHead` before any edit.

## Scope / Methodology

Read the four existing owners (`run_agent_autorun_workflow_gate.py`, `agent_autorun_machine_verification.py`, `mfrp_shadow_canary_autocollect.py`, and their existing focused
tests) before writing any new code. Confirmed the exact defect mechanism: the P4 collector's `_reconstruct_fingerprint_from_commit` reads committed Git blobs (LF after
`core.autocrlf` clean-filter conversion at commit time) while the P2 producer's `_worktree_fingerprint` reads checked-out disk bytes (CRLF under `core.autocrlf=true`); the
collector then compared these two representations directly, which is the root cause of `UNSAFE_FINGERPRINT_MISMATCH` for any legitimate line-ending checkout difference.

Created one new shared helper, `governance/compat/committed_evidence_fingerprint.py`, owning the explicitly versioned deterministic Git-blob path/byte recipe
(`git-diff-no-renames-name-only-nul-delimited-v1`) plus the closed `cvf.committedEvidenceFingerprint.v1` object shape and its shape validator. Added an additive, opt-in
`committedEvidence` binding to the existing P2 receipt (bound into `machineVerification` and `receiptDigest`, mirrored at top level with strict equality enforced by the
canonical validator). The producer computes and binds it only for a successful `pre-closure` pass on a clean worktree with a non-empty resolvable committed range. The P4-C1
collector now validates through this shared helper exclusively for receipts that declare the binding, and explicitly skips (never rehashes or upgrades) legacy v3 receipts that
omit it. The collector never again compares committed Git-blob bytes against `worktreeFingerprint`.

The raw `worktreeFingerprint`/`changedPathPlanDigest` identity, its producer, its digest/validator shape for receipts without the new object, and the P2 fixed-JCS-vector
regression test are all unchanged and unweakened; existing tests for those (`test_machine_verification_fixed_jcs_vector_match`,
`test_worktree_fingerprint_changes_with_file_content`, etc.) still pass unmodified.

## Findings / Position

Reproduced the exact defect mechanism in an isolated temporary Git repository with `core.autocrlf=true`: committed CRLF-normalized blob bytes differ from checked-out worktree
bytes for the same file (`worktree bytes == blob bytes` is `False` in the reproduction). The new `committedEvidence` fingerprint computes cleanly and deterministically from
committed blobs only, entirely independent of worktree state or line-ending checkout representation, and is provably unaffected by a subsequently dirtied worktree file
(`test_mutable_worktree_bytes_cannot_substitute_for_committed_blob` and the equivalent test in the new helper's own suite).

All work-order Test And Acceptance Matrix rows are covered with executable
proof: CRLF/LF representation independence under both
`core.autocrlf=true/false`; binary bytes; Unicode/space-containing paths; added/modified/deleted paths with the explicit missing-entry sentinel; `--no-renames` old/new path
independence for a renamed file; dirty tracked/staged/untracked drift producing no cache/committed-evidence substitution; non-ancestor range, short-SHA, and unresolved-ref
explicit failure (never a fake deletion or silent fallback); symlink (mode `120000`) and gitlink (mode `160000`) entries explicitly rejected via real Git tree entries
constructed through `git update-index --cacheinfo` (no OS-level symlink dependency, so the proof is not host-conditionally skipped);
malformed/one-sided/extra-key/unknown-profile `committedEvidence` rejected at the canonical P2 validator; legacy v3 receipts without the object explicitly skipped, never
rehashed, by the P4-C1 collector.

## Risk / Corrective Action

Two consumer test files outside this eleven-path manifest were run for compatibility per the work order's Execution Plan step 4 and Evidence Reuse/Encoding Plan:
`test_agent_automation_machine_verification_readout.py` and `test_mfrp_shadow_canary_core.py`, plus the existing `test_mfrp_shadow_canary.py`. 125 of their combined tests pass
unmodified. Three pre-existing failures were found and are **not** caused by this change; they reproduce identically at `executionBaseHead` before any edit in this tranche
(verified via `git stash`):

- `test_mfrp_shadow_canary.py::ActualP2SeamTests::test_module_uses_real_p2_owner_hashes_consistent_with_pinned_identities`
  pins an exact SHA-256 of `agent_autorun_machine_verification.py`'s bytes
  that was already stale against the file's pre-existing content at
  `executionBaseHead`, independent of any edit in this tranche.
- `test_mfrp_shadow_canary.py::P4RV4CreationOrderDerivationTests::test_stale_receipt_before_trusted_commit_is_ineligible_end_to_end`
  and the identically named test in `test_mfrp_shadow_canary_core.py` assert
  that the on-disk `pre-implementation.json` receipt's filesystem mtime
  precedes a pinned historical commit's committer time; this environment's
  receipt mtime is newer than that pin, independent of any edit here.

Per the work order's instruction ("If proof requires a consumer outside this manifest to change, return the exact source-backed dependency to Local reviewer before modifying
it"), these three pre-existing, out-of-manifest findings are returned to Local reviewer rather than repaired by this worker.

A fourth, expected out-of-manifest dependency: the read-only `python governance/compat/check_system_chain_map_freshness.py` gate reports `SOURCE_DRIFT` for
`governance/compat/run_agent_autorun_workflow_gate.py` and `governance/compat/agent_autorun_machine_verification.py`, because
`docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json` fingerprints their pre-edit SHA-256 and this tranche legitimately changed both files' bytes. This registry file is
outside the eleven-path Required Artifact Manifest and this checker is strictly read-only (it never writes the map itself), so its refresh is Local reviewer/closer's
post-acceptance action, not a worker edit.

## Decision / Disposition

`COMPLETE_PENDING_REVIEW`. The eleven-path implementation is complete: the hostile matrix is fully covered, 121/121 focused tests across the four manifest test files pass,
`git diff --check` is clean, and every gate whose mutation surface is the exact manifest passes. The aggregate `worker_return_fast` gate is NOT fully green: it is blocked by
the read-only `check_system_chain_map_freshness.py` reporting expected `SOURCE_DRIFT` for the two in-manifest files this tranche legitimately changed, against a registry file
outside the eleven-path manifest. Three separately pre-existing, out-of-manifest test failures (named above) are also disclosed. Neither is claimed as resolved, suppressed, or
absent; both are handed to Local reviewer for disposition alongside the exact diff.

## Source Inventory

| File | Action |
| --- | --- |
| `governance/compat/run_agent_autorun_workflow_gate.py` | MODIFY |
| `governance/compat/agent_autorun_machine_verification.py` | MODIFY |
| `governance/compat/mfrp_shadow_canary_autocollect.py` | MODIFY |
| `governance/compat/committed_evidence_fingerprint.py` | CREATE |
| `governance/compat/test_run_agent_autorun_workflow_gate.py` | unchanged (regression proof only) |
| `governance/compat/test_agent_autorun_machine_verification.py` | unchanged (regression proof only) |
| `governance/compat/test_mfrp_shadow_canary_autocollect.py` | MODIFY |
| `governance/compat/test_committed_evidence_fingerprint.py` | CREATE |
| `docs/reference/review_cost_control/CVF_COMMITTED_EVIDENCE_FINGERPRINT_CONTRACT.md` | CREATE |
| `docs/reference/review_cost_control/README.md` | MODIFY |
| this worker return | CREATE |

`test_run_agent_autorun_workflow_gate.py` and `test_agent_autorun_machine_verification.py` needed no new or changed test: their existing hostile/fixed-vector suites already
fully regression-cover the unchanged raw-fingerprint identity, and both pass unmodified against the additive change.

## Rework Convergence Self-Proof

rootCauseClusterId: MFRP_FINGERPRINT_WORKTREE_VS_COMMITTED_BLOB_CONTRADICTION
reworkGeneration: 0
consolidatedDefectClassSweep: COMPLETE_ALL_KNOWN_DEPENDENCIES
productionBindingEvidence: DETERMINISTIC_METADATA_ROUTING_NO_PRODUCTION_BINDING_CLAIMED
adversarialRegressionDisposition: PASS_TARGETED_DEFECT_CLASS
successorTrancheOpened: NO
implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY
internalAgentInvocationCount: 1
externalAgentInvocationCount: 0
providerCallCount: 0
tokenOrQuotaUsage: NOT_AVAILABLE_WITH_REASON: local agent surface has no governed usage meter
terminalReadinessVerdict: READY_FOR_REVIEW

## Semantic Convergence Outcome

Standard: `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "committed-evidence-fingerprint",
  "chainMode": "SUCCESSOR",
  "chainOrdinal": 1,
  "predecessor": {
    "path": "docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_FINGERPRINT_T1_2026-09-11.md",
    "sha256": "4d119ab3472fdd37909637c3e6f34f0390dfd76d513f35e54e925e72752b5936"
  },
  "blockerDelta": {
    "prior": ["worktree-versus-committed-bytes"],
    "resolved": ["worktree-versus-committed-bytes"],
    "retained": [],
    "new": [],
    "reopened": [],
    "current": []
  },
  "resolutionEvidence": {
    "worktree-versus-committed-bytes": {
      "evidenceClass": "EXECUTABLE_PROOF",
      "evidencePath": "governance/compat/test_committed_evidence_fingerprint.py",
      "sha256": "328c5038c2c8c51f345f468f65bdc9e4b739564f6f4c0f1e9b17dbf8dde5c180",
      "locator": "test_admission_check_never_invokes_configured_filter_at_all",
      "claimId": "legacy-and-additive-fingerprint-contract"
    }
  },
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0,
    "nonDecreasingBlockerTransitions": 0
  },
  "claims": [
    {
      "claimId": "legacy-and-additive-fingerprint-contract",
      "claimClass": "SCHEMA_COMPATIBILITY",
      "proofClass": "EXECUTABLE_BUILDER_VALIDATOR_CONTRACT_TEST",
      "evidenceRef": "governance/compat/test_agent_autorun_machine_verification.py"
    }
  ],
  "requiredDisposition": "READY_WITH_EXECUTABLE_PROOF",
  "successorScope": "EXECUTABLE_IMPLEMENTATION"
}
```

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | `Self-declared worker-return artifact`; `Responds to work order`; `WORKER_MUST_NOT_COMMIT`; `Core Guard Self-Protection Authorization`; `Text Encoding Exception`; `closeabilityContractVersion`; `COMPLETE_PENDING_REVIEW`; `committedEvidence` |
| gateRunPurpose | confirm final worker-return shape and additive contract behavior after implementation |
| claimBoundary | checker conformance and recorded command evidence only; reviewer acceptance remains separate |

## Rework Findings F1-F4

Consolidated rework of the original implementation in one round, addressing all four findings raised in review together, per the operator's instruction to treat the four
findings as one regression group rather than four sequential fixes.

### F1 -- Historical evidence bound only to content the gate actually verified

**Defect.** The original producer resolved `full_base_sha`/`full_head_sha` via `committed_evidence.resolve_full_sha(resolved_base)` / `resolve_full_sha(head)` strictly *after*
all gate commands had already run, with no check that those freshly-resolved full SHAs still matched the short SHAs (`base_sha`/`head_sha`) captured *before* the gate ran. A
ref that moved between those two points (e.g. a concurrent commit landing on a mutable branch such as literal `HEAD`) would silently bind `committedEvidence` to a target the
just-run gate commands never actually verified. Git-object identity alone was being treated as sufficient proof that the gate ran against that identity, which the paired
baseline explicitly forbids.

**Fix location.** `governance/compat/run_agent_autorun_workflow_gate.py`, inside `_run_phase`'s pre-closure committed-evidence binding block (the `if phase == "pre-closure"
and base_sha != head_sha:` branch). Two new guards were added before `build_committed_evidence` is called:

1. **Ref-movement guard**: after resolving `full_base_sha`/`full_head_sha`,
   assert `full_base_sha.startswith(base_sha)` and
   `full_head_sha.startswith(head_sha)` (the short SHAs captured before the
   gate ran). A mismatch raises `CommittedEvidenceUnavailable` and no
   binding is produced -- never a binding for the stale target, never one
   for the moved target.
2. **Evidence-content replay guard**: after the ref-movement guard passes,
   replay `_worktree_fingerprint(resolved_base, head)` and compare it
   against the `worktreeFingerprint` this run's own `_receipt_context`
   already computed (`observed_fingerprint`). A mismatch means the target's
   evidence paths changed content or existence between the gate's own
   fingerprint computation and the committed-evidence resolution step, and
   the binding is withheld rather than certifying semantic drift as
   historical execution. A later **continuity-only** commit (touching only
   paths outside the material range already under evaluation) does not
   change this replay's result for the *same* `resolved_base..head` range,
   so the continuity case remains supportable exactly as the finding
   requires.

No normalization of the checkout and no clean/smudge filter invocation was introduced; both guards operate purely on already-existing Git plumbing (`resolve_full_sha`,
`_worktree_fingerprint`) the producer already called.

**Proof.** `governance/compat/test_run_agent_autorun_workflow_gate.py`, new tests using a real temporary Git repository (`_TempRepo` fixture, `temp_repo` pytest fixture):

- `test_committed_evidence_bound_for_stable_range` -- control: an ordinary
  range with no drift still binds exactly as before.
- `test_committed_evidence_withheld_when_head_ref_moves_after_gate_run` --
  a concurrent commit lands on the checked-out branch between
  `resolve_full_sha` calls; no binding is produced.
- `test_committed_evidence_withheld_when_evidence_path_content_changes_after_gate_run`
  -- the replay fingerprint is forced to differ from the observed one; no
  binding is produced.
- `test_committed_evidence_bound_for_continuity_only_later_head` -- a
  continuity-only commit outside the material range does not block a
  binding for the original range.

**Result.** All 4 new tests pass; all 50 tests in `test_run_agent_autorun_workflow_gate.py` pass (was 43 before this rework). A genuine bug was found and fixed during test
authoring: the first draft of these tests silently patched the wrong `REPO_ROOT` (only `autorun.REPO_ROOT`, not `autorun.steward.REPO_ROOT` -- the path-plan module the
producer's `_worktree_fingerprint` depends on has its own separate module-level `REPO_ROOT`) and produced a false pass by measuring this actual repository's state instead of
the temp fixture; this is recorded here rather than silently corrected without disclosure, per the work order's honesty requirement.

### F2 -- Validator must distinguish omission from malformed

**Defect, part A (omission-vs-null conflation).** The original validator used `(top_committed_evidence is None) != (nested_committed_evidence is None)` where both values came
from `.get("committedEvidence")`. Since `.get()` returns `None` both when a key is genuinely absent and when a key is present with an explicit JSON `null` value, a receipt
with `"committedEvidence": null` at the top level and no nested key at all was being treated as "both None" (never distinguished from true two-sided omission) in some
branches, and the one-sided/null distinction the finding required was not made at all.

**Defect, part B (TypeError on wrong-typed fields).** `validate_committed_evidence_shape` called `_is_full_commit_sha(value.get("baseSha", ""))`. When `baseSha` is present
with a non-string value (e.g. the integer `123`), `.get(key, default)` returns `123` (the key *is* present, so the default is never used), and `_FULL_SHA_RE.fullmatch(123)`
raises `TypeError: expected string or bytes-like object`, escaping the shape validator uncaught.

**Fix location, part A.** `governance/compat/agent_autorun_machine_verification.py`, `_validate_receipt_integrity`. Replaced the `is None` comparison with explicit
`"committedEvidence" in payload` / `"committedEvidence" in machine_verification` presence checks:

- Both keys absent -> legacy omission, falls through unchanged (old v3
  behavior preserved byte-for-byte).
- Key presence differs between the two locations -> one-sided, rejected.
- Both keys present but either value is `None` -> rejected as "present
  with null value", never treated as omission.
- Both present and non-null -> proceeds to shape/range validation exactly
  as before.

**Fix location, part B.** `governance/compat/committed_evidence_fingerprint.py`, `validate_committed_evidence_shape`. Every field (`baseSha`, `headSha`, `fingerprint`) is now
explicitly `isinstance(..., str)`-checked before any regex/string operation is applied to it, so a non-string value of any kind (int, list, `None` under an existing key, bool)
is rejected with a structured `(False, reason)` tuple, never a raised `TypeError`. The same `isinstance` guard was added to `agent_autorun_machine_verification.py`'s own
`baseSha`/`headSha` `.startswith()` calls on the receipt-context cross-check.

**Proof.** `governance/compat/test_agent_autorun_machine_verification.py`, 22 new
tests: legacy two-sided omission is valid; a valid matching binding is
accepted; top-only null, both-null, one-sided top-only, one-sided nested-only, top/nested mismatch are all rejected; `baseSha`/`headSha`/ `fingerprint` each set to the integer
`123` (via post-signing mutation, so the hostile value survives receipt construction) are rejected without a raised exception; missing field, extra field, unknown profile, and
base/head-context mismatch are rejected; and a 24-case hostile sweep (`test_no_json_input_shape_raises_type_error_through_validator`) asserts no `TypeError` escapes for any of
`None`, `123`, `"not-a-dict"`, `[]`, `True`, and three internally-malformed dict shapes.

**Result.** All 27 tests in `test_agent_autorun_machine_verification.py` pass (was 0 committedEvidence-specific tests in this file before this rework; the file existed only as
regression proof for the unrelated raw v3 hostile matrix). `test_committed_evidence_fingerprint.py`'s existing
27 shape tests (already covering the non-TypeError contract at the helper level) continue to pass unmodified.

### F3 -- Collector must not downgrade a declared-but-malformed binding to benign skip

**Defect.** In `validate_and_reconcile_receipt`, the very first step calls `read_receipt_readonly`, which delegates to the canonical `_validate_receipt_integrity`. If that
canonical validator rejects the receipt (`valid=False`) for *any* reason -- including a specifically declared-but-malformed/one-sided/tampered `committedEvidence` binding --
the collector immediately raised `CollectionSkipped("SKIPPED_INVALID_ RECEIPT", reason)`. This is the correct outcome for a receipt that is simply not a valid receipt at all
(wrong schema, unreadable, tampered unrelated field), but it silently absorbed a *declared* malformed binding into the same benign-skip bucket, before the later
`UNSAFE_COMMITTED_EVIDENCE_MALFORMED` branch (further down the function, reached only when `read_receipt_readonly` returns `valid=True`) ever had a chance to classify it
correctly.

**Fix location.** `governance/compat/mfrp_shadow_canary_autocollect.py`, new function `_fail_closed_if_declared_binding_caused_rejection`, called immediately when
`read_receipt_readonly` returns `valid=False`, before the `CollectionSkipped` fallback. It performs one independent, read-only raw JSON parse of the receipt bytes (never
trusting the already-rejected structured `payload`, which may not even be a dict) and asks only: does `"committedEvidence"` appear as a key in the raw top-level object, or in
its raw nested `machineVerification` object? If either is true, it raises `CollectionUnsafe("UNSAFE_COMMITTED_EVIDENCE_MALFORMED", ...)` instead of letting the caller fall
through to the benign skip. The canonical P2 validator remains the sole source of the pass/fail verdict; this addition only re-classifies an already-failed verdict's
*severity*, and does not create a second validator, does not skip digest verification (the canonical validator's digest check already ran and already produced the rejection
this function is classifying), and does not touch any production journal or safety-marker-clearing logic.

**Proof.** `governance/compat/test_mfrp_shadow_canary_autocollect.py`, three new tests exercising `autocollect.validate_and_reconcile_receipt` directly (the real collector
entry point, not a standalone reproduction of the P2 validator call):

- `test_declared_malformed_binding_is_unsafe_not_downgraded_to_benign_skip`
  -- a receipt with `committedEvidence: {"profile": "wrong-profile"}`
  (independently confirmed to fail the canonical validator first) reaches
  `CollectionUnsafe`/`UNSAFE_COMMITTED_EVIDENCE_MALFORMED` through
  `validate_and_reconcile_receipt`, not `CollectionSkipped`.
- `test_legacy_receipt_with_unrelated_defect_still_skips_benignly` --
  control: a receipt with no committedEvidence declaration at all, invalid
  for an unrelated reason (wrong schema), still takes the benign
  `SKIPPED_INVALID_RECEIPT` path, proving the new check is narrowly scoped
  to declared bindings and does not reclassify every legacy-shape defect
  as unsafe.
- `test_nested_only_declared_binding_rejection_is_also_unsafe` -- a
  binding declared only under the nested `machineVerification` copy (never
  at top level) is also caught as a declared binding, not just the
  top-level case.

**Result.** All 46 tests in `test_mfrp_shadow_canary_autocollect.py` pass. The classification is proven through the actual collector function, not a reimplementation.

### F4 -- Integration proof through the real chain; corrected coverage claim

**Defect.** The original test suite's `committedEvidence` proofs used either (a) a test-constructed fixture receipt signed through the real P2 object builders (correct helper
hashing, but never exercising the producer's own admission logic), or (b) `validate_and_reconcile_receipt` with `committed_evidence.compute_committed_evidence_fingerprint`
mocked to a canned return value (proving the collector's control flow, but not that the shared fingerprint helper's real Git-blob computation agrees with what the real
producer bound). No test exercised the full producer-admission -> canonical-validator -> collector-reconciliation chain through one continuous real Git history. The original
worker return's
"all matrix rows covered" framing did not disclose this gap.

**Fix location.** `governance/compat/test_mfrp_shadow_canary_autocollect.py`, new class `ProducerValidatorCollectorEndToEndTests` (temporary real Git repositories,
`setUp`/`tearDown` create and remove a fresh repo per test). Its helper `_run_real_pre_closure` invokes the actual `run_agent_autorun_workflow_gate._run_phase("pre-closure",
...)` against the temp repo (only gate-command *execution* is stubbed to one trivial always-passing command -- declared explicitly in the class docstring as the isolated
surface, not claimed as full production-gate proof -- because this repository's real governed gate bundle cannot be meaningfully re-run inside a disposable fixture);
`resolve_full_sha` and `build_committed_evidence` are rebound only to the temp repo's `cwd` (never mocked to a canned value), so the fingerprint the producer emits is the real
Git-blob computation. `_reconcile_through_real_collector` feeds the resulting receipt into the real `mfrp_shadow_canary_autocollect.validate_and_reconcile_receipt`, with
`compute_committed_evidence_fingerprint` similarly rebound only to `cwd`, never mocked to a value.

Seven new tests, none of which mock the shared fingerprint helper or substitute a hand-built dict for the binding:

- `test_real_chain_crlf_autocrlf_true_and_false_agree_on_committed_evidence`
  -- `core.autocrlf` true and false, independently-computed expected
  Git-blob hash (direct `git cat-file blob` in the test body, never the
  helper compared with itself).
- `test_real_chain_binary_and_unicode_space_paths` -- binary content
  (`bytes(range(256))`) at a Unicode/space-containing path
  (`"dir 中文/binary file éè.dat"`), independent expected hash.
- `test_real_chain_dirty_tracked_staged_untracked_does_not_change_binding`
  -- dirty tracked, staged, and untracked worktree state at the moment the
  real producer runs.
- `test_real_chain_legacy_receipt_without_binding_is_skipped_by_real_collector`
  -- the real producer legitimately takes its own no-binding branch
  (`resolve_full_sha` forced to fail, reproducing an unresolvable-range
  condition rather than a hand-constructed legacy payload); the real
  collector skips it.
- `test_real_chain_tampered_binding_after_producer_emission_is_unsafe` --
  a genuinely producer-emitted binding, tampered post-emission.
- `test_real_chain_null_committed_evidence_is_rejected_end_to_end` -- a
  genuinely producer-emitted binding overwritten with `null` at both
  locations post-emission.
- `test_real_chain_raw_byte_cache_invalidation_still_regresses` --
  regression guard: two different real producer runs over different
  content at the same path produce different `worktreeFingerprint` *and*
  different `committedEvidence.fingerprint`, proving this rework did not
  weaken the pre-existing raw-byte cache-invalidation identity.

**Genuine defects found and fixed while authoring these tests** (disclosed per the work order's honesty requirement, not silently corrected):

1. A recursion bug in the test helpers themselves: `run_agent_autorun_
   workflow_gate.py` and `mfrp_shadow_canary_autocollect.py` each try a
   bare `import committed_evidence_fingerprint as committed_evidence`
   before falling back to the dotted `governance.compat.` import. When a
   test file has already put `governance/compat` on `sys.path` (as
   `test_mfrp_shadow_canary_autocollect.py` already did, pre-existing),
   the bare import succeeds and creates a **second, distinct module
   object** in `sys.modules` under the bare name, separate from the
   dotted-path module the test file itself imports. A naive scoped-`cwd`
   wrapper that referenced the module-level name at call time (`return
   committed_evidence.resolve_full_sha(ref, cwd=self._repo)`) therefore
   patched and called *the same object it was itself assigned to*,
   recursing until `RecursionError`. Fixed by capturing the real function
   object as a local variable (`real_resolve_full_sha = committed_evidence
   .resolve_full_sha`) *before* `mock.patch.object` replaces the module
   attribute, and calling that captured reference instead of the module
   attribute inside each scoped wrapper.
2. `compute_committed_evidence_fingerprint`'s `cwd` parameter, like
   `resolve_full_sha`'s, defaults to the module-level `REPO_ROOT` at
   function-definition time, so patching `REPO_ROOT` after import does not
   redirect it; the collector-side reconciliation helper needed the same
   scoped-wrapper treatment as the producer-side one.
3. `run_agent_commit_steward_preflight.py` (imported as `autorun.steward`)
   owns its own separate module-level `REPO_ROOT`, independent of
   `run_agent_autorun_workflow_gate.REPO_ROOT`; `_worktree_fingerprint`
   depends on `steward.build_path_plan`, so `autorun.steward.REPO_ROOT`
   also had to be patched to the temp repo, not just `autorun.REPO_ROOT`.
   Missing this in an early draft produced a false-passing test that
   silently measured this actual repository's changed-path state instead
   of the fixture's.

**Corrected coverage claim.** The original worker return's Findings / Position section stated "All work-order Test And Acceptance Matrix rows are covered with executable
proof." That claim is corrected here: prior to this rework, the matrix row "Tests vs live measurement... hermetic end-to-end proof" and the "producer/canonical
validator/collector integration, not just isolated dict helpers" requirement in the Test And Acceptance Matrix's closing paragraph were **not** met by real end-to-end proof --
only by isolated-unit and validator-only proof. This rework adds the missing real end-to-end coverage (7 new tests, `Producer ValidatorCollectorEndToEndTests`) and this
section documents the gap honestly rather than silently patching the old claim without disclosure.

**Result.** All 7 new end-to-end tests pass; all 46 tests in `test_mfrp_shadow_canary_autocollect.py` pass.

## Rework Findings F1 And F4 (Generation 2)

### F1 (rework-2) -- Historical-target admission was still insufficient

**Defect.** Generation 1's historical-target check compared two `_worktree_fingerprint(resolved_base, head)` reads against each other (one taken before the gate commands ran,
one taken after). This proves the worktree was *stable* across the one execution, but never proves the worktree's content actually *equals* `headSha`'s own committed content.
Local review reproduced the gap with a real temporary Git fixture: commit `A` (base), commit `B` (target, changes `evidence.txt`), commit `C` (a further commit that changes
`evidence.txt`'s content again -- semantic drift), worktree clean and stable at `C` for the whole run, then `_run_phase("pre-closure", base=A, head=B)`. Both generation-1
guards pass in this scenario (the ref never moves; the worktree never moves during the run), so generation 1 incorrectly bound `committedEvidence` for `B` even though the gate
commands' worktree reads reflected `C`'s content, not `B`'s.

**Fix location.** New function `committed_evidence_fingerprint.verify_worktree_matches_committed_target` (and its private helper `_worktree_blob_sha`). For every path in the
`base..head` changed-path set, it compares the worktree file's blob SHA (via `git hash-object`, which applies the exact same clean filter `git add` would -- respecting
`core.autocrlf`/`.gitattributes`, so a legitimate CRLF/LF checkout difference still produces the same blob SHA while any real content or binary difference does not) against
the blob SHA already committed at `head_sha` for that path. A path `head_sha` deletes must have no regular-file content in the worktree either. No bytes are read or compared
directly in Python; the equivalence decision is entirely delegated to `git`, so no independent normalization is introduced that could mask a genuine difference.
`run_agent_autorun_workflow_gate._run_phase` now calls this as a third guard, in addition to (not instead of) the existing ref-movement guard and during-run drift guard from
generation 1 -- all three remain active. The raw `worktreeFingerprint` producer/validator and the immutable `compute_committed_evidence_fingerprint` recipe are both unchanged;
this is a new, additive admission precondition only.

**Proof.**

- `governance/compat/test_committed_evidence_fingerprint.py`, new class
  `WorktreeMatchesCommittedTargetTests` (9 tests): the exact reviewer A/B/C
  counterexample (`test_reviewer_counterexample_a_b_c_drift_is_rejected`);
  continuity-only admission
  (`test_continuity_only_later_head_still_admits`); clean-at-head control
  (`test_clean_worktree_exactly_at_head_admits`); CRLF checkout tolerance
  (`test_crlf_checkout_representation_still_admits`); binary semantic-drift
  rejection (`test_binary_semantic_change_at_head_target_is_rejected`);
  deletion consistency both ways
  (`test_deletion_at_head_requires_worktree_absence`,
  `test_deletion_at_head_with_worktree_absence_admits`); helper-invariance
  vs. producer-admission distinction
  (`test_dirty_worktree_can_still_incidentally_match_committed_target`);
  and multi-path partial-drift rejection
  (`test_multiple_changed_paths_only_drifted_one_is_rejected`).
- `governance/compat/test_run_agent_autorun_workflow_gate.py`, 3 new
  integration-level tests reproducing the counterexample through the real
  `_run_phase` entry point (not just the helper in isolation):
  `test_committed_evidence_withheld_for_historical_target_semantic_drift`
  (the exact reviewer scenario -- fails without the fix, confirmed by
  temporarily monkeypatching `verify_worktree_matches_committed_target` to
  always return `True` and observing the test then fails, proving this is
  a genuine regression proof, not vacuous),
  `test_committed_evidence_bound_for_historical_target_with_continuity_only_head_c`
  (companion positive case), and
  `test_committed_evidence_bound_with_crlf_checkout_representation`.
- `governance/compat/test_mfrp_shadow_canary_autocollect.py`,
  `ProducerValidatorCollectorEndToEndTests`, 2 new tests carrying the same
  counterexample and continuity-only case through the full real
  producer -> real validator -> real collector chain:
  `test_real_chain_historical_target_semantic_drift_is_rejected` and
  `test_real_chain_historical_target_with_continuity_only_head_admits`.

**Result.** All 9 new helper-level tests, all 3 new producer-level tests, and both new E2E-level tests pass. The counterexample-sensitivity check (disabling the fix and
re-running the producer-level counterexample test) confirms the test would have failed against generation 1's code, proving this is not a vacuous regression test.

### F4 (rework-2) -- Chain-test proof and isolation declaration did not match

**Defect.** `ProducerValidatorCollectorEndToEndTests._run_real_pre_closure` mocked `autorun._write_receipt` (hand-reconstructing the receipt payload inline, duplicating the
real writer's logic instead of exercising it), `autorun._closure_worktree_finality_failures` (always returning `0`, never actually checking `git status --short` against the
fixture repo), and `autorun._range_shape_preflight` (always returning `0`, never actually running `steward.build_path_plan` against the fixture repo) -- three production
functions beyond the class's own declared isolation boundary ("only gate *command execution* is stubbed"). The class's docstring did not disclose these three additional mocks,
so its "isolated surface" declaration did not match what the tests actually ran.

**Fix location.** `governance/compat/test_mfrp_shadow_canary_autocollect.py`, `ProducerValidatorCollectorEndToEndTests`:

- `_write_receipt` is no longer mocked. `_run_phase`'s existing
  `receipt_dir` parameter is pointed at a fresh per-call directory (under
  a real `.gitignore`-covered path inside the fixture repo, mirroring this
  actual repository's own `.cvf/runtime/` gitignore entry, so repeated
  real producer runs against the same fixture never see a leftover
  receipt directory as untracked drift in `git status`); the receipt is
  read back from the real on-disk file the real writer produced.
- `_closure_worktree_finality_failures` and `_range_shape_preflight` are
  no longer mocked; both run for real against the fixture repo (`REPO_ROOT`
  and `steward.REPO_ROOT` are still redirected to the fixture, which is
  the pre-existing, declared `cwd`-redirection isolation, not a behavior
  mock).
- The real `_closure_worktree_finality_failures` genuinely rejects a dirty
  fixture worktree once unmocked, which is correct production behavior
  and was a real gap in generation 1's "dirty worktree" test (which had
  assumed the real producer would still bind evidence for a dirty
  worktree -- it does not, and must not). That test was replaced by two
  tests that correctly separate the two guarantees (see point 5 below):
  `test_real_producer_refuses_binding_outright_on_dirty_worktree` and
  `test_helper_invariance_is_narrower_than_producer_admission`.
- The CRLF true/false comparison test could no longer flip
  `core.autocrlf` mid-test in one worktree once the real closure-finality
  check was unmocked (flipping the config without a fresh checkout
  leaves the worktree's raw disk bytes unchanged while Git's own
  interpretation of them changes, which `git status` itself correctly
  reports as a dirty file -- confirmed independently). It now uses a
  genuine fresh `git clone --config core.autocrlf=<value>` per setting,
  each with its own real checkout, matching what a CRLF/LF
  checkout-representation claim actually describes.
- The class docstring now names the *exact* current isolation surface:
  only gate-command *execution* (`_common_commands`/`_execute`) is
  stubbed; `resolve_full_sha`/`build_committed_evidence`/
  `verify_worktree_matches_committed_target` are rebound only to redirect
  their `cwd` default (a late-bound-default workaround, not a behavior
  change) -- their real bodies still run. It explicitly states this is
  not full production-gate proof (this repository's actual checker bundle
  is not exercised) and not live/runtime proof.

**Minimum regression matrix added** (point 4 of the finding), all through the real producer -> real validator -> real collector chain in
`ProducerValidatorCollectorEndToEndTests` unless noted:

- current target, clean worktree -> binding accepted (pre-existing tests,
  now running through the real writer/finality/preflight);
- historical B, clean HEAD C evidence semantic drift -> no binding
  (`test_real_chain_historical_target_semantic_drift_is_rejected`, new);
- historical B, later continuity-only HEAD -> binding valid
  (`test_real_chain_historical_target_with_continuity_only_head_admits`,
  new);
- ref moved during run -> no binding
  (`test_real_chain_ref_movement_during_run_withholds_binding`, new --
  generation 1 only had this at the isolated producer-test level, not
  through the full E2E chain);
- evidence changed during run -> no binding (covered at the E2E level by
  the historical-target-drift test above, which is a stricter superset of
  the during-run-drift case);
- LF/CRLF equivalent, binary semantic change not overlooked
  (`test_real_chain_crlf_autocrlf_true_and_false_agree_on_committed_evidence`,
  redesigned this round; `test_real_chain_binary_and_unicode_space_paths`,
  pre-existing).

**Point 5 (helper invariance vs. producer admission), explicitly addressed.** Two tests now make the distinction the finding requires explicit rather than implicit:
`test_real_producer_refuses_binding_outright_on_dirty_worktree` proves the real producer's `_closure_worktree_finality_failures` rejects a dirty worktree outright, before any
binding is ever considered. `test_helper_invariance_is_narrower_than_producer_admission` proves that even when the shared helper alone would say "matches" for a dirty-but-
content-reverted worktree (verified directly via `verify_worktree_matches_committed_target`), the real producer still refuses to bind anything for that same dirty worktree --
the helper's narrower byte-equivalence invariance is never mistaken for, or treated as equivalent to, the producer's own separate admission control.

**Result.** All 11 tests in `ProducerValidatorCollectorEndToEndTests` pass (up from 7 in generation 1: 2 replaced for correctness, 6 added: 2 for the F1
historical-target/continuity matrix rows, 1 for ref-movement at the E2E level, 2 replacing the incorrect dirty-worktree test, and the CRLF test's internal redesign does not
add a new test method).

## Rework Findings F1 (Generation 3)

### Root cause

`committed_evidence_fingerprint._worktree_blob_sha` (generation 2) computed worktree-side equivalence via `git hash-object -- <path>`. This command applies the exact same
`clean` filter pipeline `git add` would: any `.gitattributes`-configured `filter.<name>.clean` driver, plus `core.autocrlf` conversion. A `clean` filter is an arbitrary
external command; nothing constrains it to be a pure, information-preserving transform of its input. Local review configured `filter.reviewprobe.clean` to unconditionally emit
the fixed bytes `target` regardless of what it was given, then demonstrated: commit A (`evidence.txt` = `base`), configure the filter, commit B (`evidence.txt`
= `target`, filtered through the same fixed-output filter so the
committed blob is also `target`), overwrite the worktree file with `totally different malicious content`, `git add evidence.txt` (the filter converts the staged content back
to `target`, so `git status --short` is genuinely clean and the real, unmocked `_closure_worktree_finality_failures` does not block the run) --
`verify_worktree_matches_committed_target` then called `git hash-object` on the same file, which ran the same filter, producing the same laundered `target` bytes, and returned
`True`. The producer went on to bind `committedEvidence` for content it never actually verified. **Filter equivalence is not semantic equivalence**; the governing byte-recipe
contract's Section 4 ("No text decoding, newline translation, or clean/smudge filter execution occurs anywhere in this recipe") already forbade exactly this, and generation
2's guard violated it without that being caught until this review round.

### Fix

`governance/compat/committed_evidence_fingerprint.py`: `_worktree_blob_sha` (which returned a `git hash-object`-computed blob SHA) is replaced by two functions:

- `_read_worktree_bytes`: reads the worktree file's raw disk bytes via
  `Path.read_bytes()` -- no `git` invocation at all, so no filter of any
  kind, configured or built-in, can execute.
- `_worktree_bytes_match_committed_blob`: decides equivalence with exact
  byte comparison first (covers the overwhelming majority of cases,
  including all binary content); only when bytes are not exactly equal
  does it try one fixed, fallback: does replacing every `\r\n` with `\n`
  on **both** sides (the worktree bytes and the already-fetched committed
  blob bytes, via the pre-existing filter-free `_blob_bytes`/`git cat-file
  blob` path) make them equal? This is a total, deterministic, one-
  directional Python byte transform -- never an external command, never a
  repository-configurable filter, never a generic text-encoding
  transform, and never an approximate/fuzzy comparison -- so no
  repository configuration can redirect or launder it the way
  `git hash-object` could. `verify_worktree_matches_committed_target` was
  updated to call these two functions instead of the removed
  `_worktree_blob_sha`; its public signature and return shape
  (`tuple[bool, str]`) are unchanged, so no caller needed to change.

### Supported equivalence and fail-closed boundaries

Explicitly supported (with executable proof): exact byte equality (current target, all binary content); the fixed CRLF-to-LF substitution, which covers both
`core.autocrlf`-driven and `.gitattributes` `eol=crlf`/`eol=lf`-driven checkout representation, since both produce the identical byte-pattern difference the substitution
resolves, regardless of which Git mechanism caused it.

Explicitly NOT supported, and verified to fail closed rather than being silently treated as equivalent: any configured `clean`/`smudge`/`process` filter's output (the
counterexample); `ident` keyword expansion (a legitimate, non-malicious Git checkout transform this governing contract does not name anywhere -- proven with a real fixture to
produce a genuine disk-vs-blob byte difference that this check correctly rejects, disclosed as a known, deliberate limitation rather than claimed as covered). No attempt was
made to special-case `ident` or any other attribute-driven transform beyond CRLF/LF: doing so would require either expanding the contract's tolerated-equivalence set (not
authorized by this work order) or executing the same class of configurable transform this fix removes. Per the work order's instruction, this is disclosed as the current
boundary rather than silently patched by broadening scope.

### Proof

- `governance/compat/test_committed_evidence_fingerprint.py`, new class
  `CleanFilterCannotMaskSemanticDriftTests` (2 tests):
  `test_reviewer_clean_filter_counterexample_is_rejected` reproduces the
  exact Local-review fixture (steps 1-7) and asserts both that admission
  is rejected and that the filter's sentinel-file run count does not
  increase beyond what fixture setup alone produced (distinguishing
  "filter ran during `git add` setup" from "filter ran because the
  admission check invoked it"); `test_admission_check_never_invokes_configured_filter_at_all`
  proves the same zero-additional-invocations property for a legitimately
  matching target, independent of the counterexample's pass/fail outcome.
- New class `SimilarTransformSurveyTests` (2 tests):
  `test_eol_attribute_driven_crlf_is_still_tolerated` proves the `eol`
  attribute case is covered by the same CRLF substitution;
  `test_ident_keyword_expansion_is_explicitly_not_covered_and_fails_closed`
  proves `ident` expansion is correctly rejected (disclosed limitation,
  not silently accepted).
- `governance/compat/test_mfrp_shadow_canary_autocollect.py`,
  `ProducerValidatorCollectorEndToEndTests`, new test
  `test_real_chain_clean_filter_masked_drift_is_rejected`: the same
  clean-filter counterexample reproduced through the real producer (real
  `_write_receipt`, real unmocked `_closure_worktree_finality_failures`,
  real `_range_shape_preflight`) -> real validator -> real collector
  chain, using the real, unpatched
  `verify_worktree_matches_committed_target` and
  `compute_committed_evidence_fingerprint` (only their `cwd` default is
  rebound to the fixture repo, per this class's existing, unchanged
  isolation declaration).
- **Sensitivity check (both levels):** for both the new helper-level and
  the new E2E-level counterexample test, the fix was temporarily replaced
  with a monkeypatched reproduction of generation 2's `git hash-object`-based
  logic and the test suite re-run; both counterexample tests failed
  against that reproduction with `committedEvidence` incorrectly bound
  (confirming genuine, non-vacuous regression proof), then passed again
  against the actual fix.
- A genuine test-authoring defect was found and fixed while writing these
  tests, disclosed per the work order's honesty requirement: the first
  draft placed the filter script and sentinel file under
  `self._repo.parent`, which for this test file's existing
  `_TempRepoTestCase.setUp` (`self._repo = Path(self._tmp)` directly, not
  a subdirectory) is the *shared system temp root*, not a directory unique
  to that test -- causing cross-test sentinel-file collisions and a
  spuriously-failing precondition assertion. Fixed by giving
  `CleanFilterCannotMaskSemanticDriftTests` its own dedicated
  `setUp`/`tearDown`-managed scratch directory. A second defect: `git
  commit` itself was observed to invoke the configured filter at least
  once even when the blob was staged via `git hash-object --no-filters -w`
  plus a direct `git update-index` (visible as the sentinel already
  existing immediately after `git commit` returned, before the function
  under test was ever called); the isolated no-filter-execution test was
  redesigned to use the same before/after invocation-count technique as
  the counterexample test, which correctly isolates "invocations the
  function under test adds" from whatever baseline Git's own commit
  machinery independently produces.

### Result

All 4 new tests pass (2 helper-level clean-filter tests, 2 transform-survey tests); the new E2E-level test passes; all 171 tests across the four manifest test files pass (up
from 166 before this round). F2/F3 regressions re-confirmed intact.

## Gate Evidence

| Command | Result |
| --- | --- |
| CRLF reproduction in isolated temp Git repo (`core.autocrlf=true`) | confirmed `worktree bytes != blob bytes` for the identical committed file, matching the paired baseline's diagnostic |
| `python -m pytest governance/compat/test_committed_evidence_fingerprint.py governance/compat/test_run_agent_autorun_workflow_gate.py governance/compat/test_agent_autorun_machine_verification.py governance/compat/test_mfrp_shadow_canary_autocollect.py -q` | 121 passed (27 + 43 + 12 + 39) |
| `python -m pytest governance/compat/test_agent_automation_machine_verification_readout.py governance/compat/test_mfrp_shadow_canary.py governance/compat/test_mfrp_shadow_canary_core.py -q` | 125 passed, 3 pre-existing failures (named in Risk / Corrective Action) reproduced identically before any edit via `git stash` |
| `git diff --check` | PASS, no output |
| `python governance/compat/check_agent_packet_authority_and_encoding.py` | COMPLIANT |
| `python governance/compat/check_core_guard_self_protection.py` | COMPLIANT (verified after this return's Core Guard Self-Protection Authorization block was written) |
| `python governance/compat/check_semantic_convergence_control.py` | PASS |
| `python governance/compat/check_gate_to_role_closeability.py` | COMPLIANT |
| `python governance/compat/check_finding_to_governance_learning.py` | COMPLIANT |
| `python governance/compat/check_worker_experience_retrospective.py` | PASS |
| `python governance/compat/check_review_cost_control.py` | PASS |
| `python governance/compat/run_worker_return_fast_gate.py` | NOT fully green: blocked by `check_system_chain_map_freshness.py` reporting `SOURCE_DRIFT` for the two legitimately-modified source files; this is a read-only registry-freshness gate outside the eleven-path manifest, disclosed above, not repaired here |

receiptEvidence: CVF_RECEIPT_PRESENT - 121/121 focused manifest tests pass; 125/128 wider-consumer compatibility tests pass with 3 disclosed pre-existing out-of-manifest failures

**Historical note (generation 0, superseded by Rework Verification below):** at the time this table was first written, `test_run_agent_autorun_workflow_gate.py` and
`test_agent_autorun_machine_verification.py` had not yet been edited; the
121-count and the "unchanged" characterization below reflect that
pre-rework state and are not re-stated as current. See "Rework Verification" immediately below for the post-rework actual counts and gate results.

## Rework Verification

Actual results after the F1-F4 rework (generation 1), same `executionBaseHead` as recorded above; no additional commit occurred between generation 0 and this rework.

| Command | Result |
| --- | --- |
| `python -m pytest governance/compat/test_committed_evidence_fingerprint.py governance/compat/test_run_agent_autorun_workflow_gate.py governance/compat/test_agent_autorun_machine_verification.py governance/compat/test_mfrp_shadow_canary_autocollect.py -q` | 150 passed (27 + 50 + 27 + 46) |
| `python -m pytest governance/compat/test_agent_automation_machine_verification_readout.py governance/compat/test_mfrp_shadow_canary.py governance/compat/test_mfrp_shadow_canary_core.py -q` | 125 passed, same 3 pre-existing failures reproduced identically via `git stash` immediately before this rework's edits (re-verified at this rework's start, not merely carried forward from generation 0's claim) |
| `git diff --check` | PASS, no output |
| `python governance/compat/check_agent_packet_authority_and_encoding.py` | COMPLIANT (one non-ASCII literal introduced by the new F4 Unicode-path end-to-end test required adding a Text Encoding Exception declaration to `test_mfrp_shadow_canary_autocollect.py`'s module docstring; found and repaired within this rework) |
| `python governance/compat/check_core_guard_self_protection.py` | COMPLIANT |
| `python governance/compat/check_semantic_convergence_control.py` | PASS |
| `python governance/compat/check_gate_to_role_closeability.py` | COMPLIANT |
| `python governance/compat/check_finding_to_governance_learning.py` | COMPLIANT |
| `python governance/compat/check_worker_experience_retrospective.py` | PASS |
| `python governance/compat/check_review_cost_control.py` | PASS |
| `python governance/compat/run_worker_return_fast_gate.py` | NOT fully green: blocked by exactly the same `check_system_chain_map_freshness.py` `SOURCE_DRIFT` finding for `governance/compat/run_agent_autorun_workflow_gate.py` and `governance/compat/agent_autorun_machine_verification.py` -- both files' hashes changed further during this rework (F1 and F2 edits respectively), so the recorded map hashes drift further still; this remains a read-only registry-freshness gate outside the eleven-path manifest, owned by dispatcher/reviewer per the operator's stated boundary, not repaired here |

receiptEvidence: CVF_RECEIPT_PRESENT - 150/150 focused manifest tests pass
(29 new tests added across the F1/F2/F3/F4 findings: 4 in `test_run_agent_autorun_workflow_gate.py`, 15 in `test_agent_autorun_machine_verification.py`, 10 in
`test_mfrp_shadow_canary_autocollect.py` of which 7 are the new real end-to-end chain class);
125/128 wider-consumer compatibility tests pass with the same 3 disclosed pre-existing out-of-manifest failures, confirmed unchanged by this
rework.

**Aggregate PASS claim boundary:** the aggregate `worker_return_fast` gate is not claimed as fully green. It is blocked solely by the disclosed `SOURCE_DRIFT` finding against
a registry file (`docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json`) outside the eleven-path Required Artifact Manifest, which this worker has no authority to edit per
the operator's explicit instruction. No other gate in the aggregate bundle fails.

## Rework-2 Verification

Actual results after the F1/F4 generation-2 rework, same `executionBaseHead` as recorded above; no additional commit occurred. Baseline comparison for the 3 pre-existing
failures used read-only Git object inspection (`git show HEAD:<path>`), not `git stash`, per this round's explicit instruction.

| Command | Result |
| --- | --- |
| `python -m pytest governance/compat/test_committed_evidence_fingerprint.py -q -k WorktreeMatchesCommittedTargetTests` (new tests, run first to record the counterexample before the fix, then after) | before fix (guard disabled via monkeypatch): counterexample test fails as expected, confirmed on the isolated producer-level test; after fix: 9 passed |
| `python -m pytest governance/compat/test_committed_evidence_fingerprint.py governance/compat/test_run_agent_autorun_workflow_gate.py governance/compat/test_agent_autorun_machine_verification.py governance/compat/test_mfrp_shadow_canary_autocollect.py -q` | 166 passed (36 + 53 + 27 + 50) |
| `python -m pytest governance/compat/test_agent_autorun_machine_verification.py -q -k "committed_evidence or omission or null or one_sided or wrong_type or malformed"` (F2 regression re-check) | 12 passed |
| `python -m pytest governance/compat/test_mfrp_shadow_canary_autocollect.py -q -k "malformed_binding or unrelated_defect or nested_only"` (F3 regression re-check) | 3 passed |
| `python -m pytest governance/compat/test_agent_automation_machine_verification_readout.py governance/compat/test_mfrp_shadow_canary.py governance/compat/test_mfrp_shadow_canary_core.py -q` | 125 passed, same 3 pre-existing failures, same reasons, re-confirmed via read-only Git object inspection (`git show HEAD:governance/compat/agent_autorun_machine_verification.py` recomputes to the same pinned-mismatch hash the tests already report; the other two depend on `git_commit_time(TRUSTED_COMMIT)` against the current wall clock, independent of any working-tree edit) |
| `git diff --check` | PASS, no output |
| `python governance/compat/check_agent_packet_authority_and_encoding.py` | COMPLIANT |
| `python governance/compat/check_core_guard_self_protection.py` | COMPLIANT |
| `python governance/compat/check_semantic_convergence_control.py` | PASS (required one repair this round: the `worktree-versus-committed-bytes` resolution-evidence `sha256` in the Semantic Convergence Outcome block below had gone stale against `test_committed_evidence_fingerprint.py`'s new content; recomputed and updated in place, locator updated to a literal substring that still occurs in the file) |
| `python governance/compat/check_gate_to_role_closeability.py` | COMPLIANT |
| `python governance/compat/check_finding_to_governance_learning.py` | COMPLIANT |
| `python governance/compat/check_worker_experience_retrospective.py` | PASS |
| `python governance/compat/check_review_cost_control.py` | PASS |
| `python governance/compat/check_markdown_structural_completeness.py` | COMPLIANT |
| `python governance/compat/run_worker_return_fast_gate.py` | NOT fully green: blocked by exactly the same `check_system_chain_map_freshness.py` `SOURCE_DRIFT` finding for `governance/compat/run_agent_autorun_workflow_gate.py` and `governance/compat/agent_autorun_machine_verification.py` (both files' hashes changed further this round with the new F1 guard); same read-only registry-freshness gate outside the eleven-path manifest, not repaired here |

receiptEvidence: CVF_RECEIPT_PRESENT - 166/166 focused manifest tests pass
(16 new tests added this round: 9 in `test_committed_evidence_fingerprint.py` (`WorktreeMatchesCommittedTargetTests`), 3 in `test_run_agent_autorun_workflow_gate.py`, 4 net
new in `test_mfrp_shadow_canary_autocollect.py`'s `ProducerValidatorCollectorEndToEndTests` -- 2 replacing the incorrect dirty-worktree test with 2 correct ones, plus 2 for
the historical-target matrix rows and 1 for E2E-level ref-movement, for a net class total of 11 up from 7); 125/128 wider-consumer compatibility tests pass with the same
3 disclosed pre-existing out-of-manifest failures, confirmed unchanged by
this round via read-only Git object inspection rather than `git stash`.

**Aggregate PASS claim boundary (unchanged from generation 1):** the aggregate `worker_return_fast` gate is not claimed as fully green. It remains blocked solely by the
disclosed `SOURCE_DRIFT` finding against `docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json`, outside the eleven-path Required Artifact Manifest, which this worker has no
authority to edit. No other gate in the aggregate bundle fails.

## Rework-3 Verification

Actual results after the F1 generation-3 rework (clean-filter equivalence correction), same `executionBaseHead` as recorded above; no additional commit occurred. Baseline
comparison for the 3 pre-existing failures again used `python -m pytest` directly against this environment's current state (read-only; no `git stash`), per this round's
explicit instruction.

| Command | Result |
| --- | --- |
| `python -m pytest governance/compat/test_committed_evidence_fingerprint.py -q -k "CleanFilterCannotMaskSemanticDriftTests or SimilarTransformSurveyTests"` (new tests, counterexample recorded first against a monkeypatched reproduction of generation 2's `git hash-object`-based logic, then against the actual fix) | before fix (monkeypatched reproduction): `test_reviewer_clean_filter_counterexample_is_rejected` fails with `committedEvidence` incorrectly accepted, confirming the counterexample; after fix: 4 passed |
| `python -m pytest governance/compat/test_mfrp_shadow_canary_autocollect.py -q -k test_real_chain_clean_filter_masked_drift_is_rejected` (E2E-level counterexample, same before/after check against the real producer/validator/collector chain) | before fix (monkeypatched reproduction): fails with `committedEvidence` incorrectly bound in the real receipt; after fix: 1 passed |
| `python -m pytest governance/compat/test_committed_evidence_fingerprint.py governance/compat/test_run_agent_autorun_workflow_gate.py governance/compat/test_agent_autorun_machine_verification.py governance/compat/test_mfrp_shadow_canary_autocollect.py -q` | 171 passed (40 + 53 + 27 + 51) |
| `python -m pytest governance/compat/test_agent_autorun_machine_verification.py -q -k "committed_evidence or omission or null or one_sided or wrong_type or malformed"` (F2 regression re-check) | 12 passed |
| `python -m pytest governance/compat/test_mfrp_shadow_canary_autocollect.py -q -k "malformed_binding or unrelated_defect or nested_only"` (F3 regression re-check) | 3 passed |
| `python -m pytest governance/compat/test_agent_automation_machine_verification_readout.py governance/compat/test_mfrp_shadow_canary.py governance/compat/test_mfrp_shadow_canary_core.py -q` | 125 passed, same 3 pre-existing failures, same reasons, unchanged |
| `git diff --check` | PASS, no output |
| `python governance/compat/check_agent_packet_authority_and_encoding.py` | COMPLIANT |
| `python governance/compat/check_core_guard_self_protection.py` | COMPLIANT |
| `python governance/compat/check_semantic_convergence_control.py` | PASS (required one repair this round: the `worktree-versus-committed-bytes` resolution-evidence `sha256` had gone stale against `test_committed_evidence_fingerprint.py`'s new content again; recomputed and updated in place; the locator also had to be changed to one that occurs exactly once in the file, since the first candidate locator's own name appeared twice -- once in its definition, once referenced in another test's docstring) |
| `python governance/compat/check_gate_to_role_closeability.py` | COMPLIANT |
| `python governance/compat/check_finding_to_governance_learning.py` | COMPLIANT |
| `python governance/compat/check_worker_experience_retrospective.py` | PASS |
| `python governance/compat/check_review_cost_control.py` | PASS |
| `python governance/compat/check_markdown_structural_completeness.py` | COMPLIANT |
| `python governance/compat/run_worker_return_fast_gate.py` | Historical worker report, superseded by Local repair verification: SOURCE_DRIFT plus EQC findings were observed on reviewer rerun. |

receiptEvidence: CVF_RECEIPT_PRESENT - 171/171 focused manifest tests pass
(4 new tests in `test_committed_evidence_fingerprint.py`: `CleanFilterCannotMaskSemanticDriftTests` (2) and `SimilarTransformSurveyTests` (2); 1 new test in
`test_mfrp_shadow_canary_autocollect.py`'s `ProducerValidatorCollectorEndToEndTests`, now 12 tests in that class);
125/128 wider-consumer compatibility tests pass with the same 3 disclosed
pre-existing out-of-manifest failures, confirmed unchanged this round.

**Aggregate PASS claim boundary (unchanged from generations 1-2):** the aggregate `worker_return_fast` gate is not claimed as fully green. It remains blocked solely by the
disclosed `SOURCE_DRIFT` finding, outside the eleven-path Required Artifact Manifest, which this worker has no authority to edit. No other gate in the aggregate bundle fails.

## Actual Changed Set

- `governance/compat/run_agent_autorun_workflow_gate.py` (MODIFY, further edited this rework: F1 ref-movement and evidence-replay guards)
- `governance/compat/agent_autorun_machine_verification.py` (MODIFY, further edited this rework: F2 omission-vs-null/one-sided distinction)
- `governance/compat/mfrp_shadow_canary_autocollect.py` (MODIFY, further edited this rework: F3 declared-binding-aware classification)
- `governance/compat/committed_evidence_fingerprint.py` (further edited this rework: F2 TypeError-safe shape validation)
- `governance/compat/test_run_agent_autorun_workflow_gate.py` (MODIFY this rework: F1 regression tests; was unedited in generation 0)
- `governance/compat/test_agent_autorun_machine_verification.py` (MODIFY this rework: F2 regression tests; was unedited in generation 0)
- `governance/compat/test_mfrp_shadow_canary_autocollect.py` (MODIFY, further edited this rework: F3 and F4 regression/integration tests)
- `governance/compat/test_committed_evidence_fingerprint.py` (unedited this rework; F2's helper-level TypeError-safety proof already lived here from generation 0 and needed no change)
- `docs/reference/review_cost_control/CVF_COMMITTED_EVIDENCE_FINGERPRINT_CONTRACT.md` (unedited this rework)
- `docs/reference/review_cost_control/README.md` (unedited this rework)
- this worker return (MODIFY this rework: Rework Notice, Rework Findings F1-F4, Rework Verification, Rework Return-Time Closeability Recheck)

Exactly the eleven Required Artifact Manifest paths; no path outside the manifest was touched by this rework.

## Actual Changed Set (Generation 3)

- `governance/compat/committed_evidence_fingerprint.py` (MODIFY this round: F1 clean-filter-execution removal -- `_worktree_blob_sha` replaced by `_read_worktree_bytes`/`_worktree_bytes_match_committed_blob`; module and function docstrings corrected)
- `governance/compat/test_committed_evidence_fingerprint.py` (MODIFY this round: new `CleanFilterCannotMaskSemanticDriftTests` and `SimilarTransformSurveyTests` classes, 4 tests)
- `governance/compat/test_mfrp_shadow_canary_autocollect.py` (MODIFY this round: new E2E-level `test_real_chain_clean_filter_masked_drift_is_rejected`)
- `docs/reference/review_cost_control/CVF_COMMITTED_EVIDENCE_FINGERPRINT_CONTRACT.md` (MODIFY this round: historical-target admission guard's equivalence description corrected to name the byte-comparison mechanism, not `git hash-object`)
- this worker return (MODIFY this round: Rework Notice Generation 3, Rework Findings F1 (Generation 3), Rework-3 Verification, this section, Rework-3 Return-Time Closeability Recheck)
- `governance/compat/run_agent_autorun_workflow_gate.py`, `governance/compat/agent_autorun_machine_verification.py`, `governance/compat/mfrp_shadow_canary_autocollect.py`, `governance/compat/test_run_agent_autorun_workflow_gate.py`, `governance/compat/test_agent_autorun_machine_verification.py`, `docs/reference/review_cost_control/README.md` (unedited this round; unchanged from generation 2's byte content)

Exactly the eleven Required Artifact Manifest paths; no path outside the manifest was touched this round.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: only the eleven worker targets in the paired work order's Required Artifact Manifest; preserve raw cache invalidation, receipt integrity,
full gate selection, and P4 safety, exactly as stated in the paired baseline's Core Guard Self-Protection Authorization, reproduced here for this changed set.

Operator authorization: explicit yes on 2026-09-11 to dispatch internal worker repair of the fingerprint contract and regression tests before any pilot (paired baseline Core
Guard Self-Protection Authorization section).

Protected paths:

- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/agent_autorun_machine_verification.py`
- `governance/compat/mfrp_shadow_canary_autocollect.py`
- `governance/compat/committed_evidence_fingerprint.py`
- `governance/compat/test_run_agent_autorun_workflow_gate.py`
- `governance/compat/test_agent_autorun_machine_verification.py`
- `governance/compat/test_mfrp_shadow_canary_autocollect.py`
- `governance/compat/test_committed_evidence_fingerprint.py`

Rollback boundary: only the newly introduced `committedEvidence` binding behavior and its tests/reference, exactly as stated in the paired baseline. Never rewrite old receipts
or journals, clear safety markers automatically, normalize the checkout, amend history, or restore unrelated work.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator method requirement -> existing P2/P4 fingerprint owners -> internal implementation review |
| Matching local-view guard | `governance/compat/check_core_guard_self_protection.py` |
| Owner surface | existing receipt producer/validator/collector plus one new shared helper |
| Disposition | ADAPT the operator-approved fingerprint requirement; no source-value acceptance |
| Claim boundary | routing/implementation maintenance only; no source acquisition or absorption execution performed |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: no repository survey or rescan was performed; this is deterministic
Git-object identity contract maintenance only.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - no corpus was processed; deterministic Git-blob fingerprint metadata and tests only.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
| --- | --- | --- | --- | --- | --- |
| P4 collector compared committed Git-blob bytes directly against a mutable worktree fingerprint, causing false-positive `UNSAFE_FINGERPRINT_MISMATCH` under legitimate CRLF/LF checkout representation differences | RUNTIME_SIGNAL_GAP | GOVERNANCE_CONTROL_PLANE | TEMPLATE_UPDATED | additive `committedEvidence` binding computed and validated exclusively through immutable Git-blob bytes, never compared with `worktreeFingerprint` | handled |
| Three consumer tests outside this manifest carry stale pinned hashes/mtimes unrelated to this tranche | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | N/A_WITH_REASON: outside this worker's authorized scope; returned to Local reviewer per work order instruction rather than repaired here | reviewer disposition of the three named pre-existing failures | deferred |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: an additive, immutable-blob-only identity computed and validated identically by the P2 producer and the P4-C1 collector removes the
CRLF/LF-driven false-positive mismatch without weakening the existing raw worktree cache identity or receipt integrity for any manifest that omits the new object.

Evidence Comparison Requirement: compare old-behavior reproduction (raw worktree bytes vs. committed blob bytes differ under CRLF checkout) against the new binding's
independence from worktree state; compare receipts with and without `committedEvidence` for byte-identical legacy shape.

Contradiction Handling Requirement: any test asserting the collector still compares committed bytes with `worktreeFingerprint`, or asserting a legacy receipt without the
binding is silently upgraded or rehashed, blocks review.

Claim Update Requirement: none; no prior claim is revised by this tranche.

## Worker Experience Retrospective

WORKER_EXPERIENCE_RETRO_NA_WITH_REASON: no friction beyond normal gates; no gate surprise, no helper gap, no worktree contamination this return

## Worker Return Jurisdiction Block

| Field | Disposition |
| --- | --- |
| capturedArtifacts | nine implementation/test/doc paths plus this worker return |
| capturedOperations | local source edits, focused tests, wider-consumer compatibility run, diff hygiene, core-guard/encoding checker runs |
| deferredOperations | independent Local review, disposition of three disclosed pre-existing out-of-manifest test failures, material commit, continuity sync |
| outOfScopeRequests | N/A with reason: none |
| reviewerActionNeeded | evaluate returned evidence, decide disposition of the three named pre-existing failures, optionally author a completion review, commit accepted material |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Internal Agent implementation role |
| Provider or surface | local private CVF workspace |
| Session or invocation | MFRP-FINGERPRINT-T1 implementation, 2026-09-11 |
| Working directory | repository root |
| Command or tool surface | governed reads, direct file edits, pytest, Python diagnostics, Git read-only and disposable-temp-repo commands |
| Target paths | exact eleven-path Required Artifact Manifest |
| Allowed scope source | committed work order and paired baseline at dispatch |
| Before status evidence | clean worktree and empty staging at executionBaseHead `9abb0bdfe2123bccd5749cd0f90148d44cbe0424` |
| After status evidence | nine worker paths changed plus this worker return; staging remains empty |
| Diff evidence | `git diff --name-status 9abb0bdfe..HEAD` plus working-tree status |
| Approval boundary | exact MFRP-FINGERPRINT-T1 fingerprint repair only |
| Claim boundary | local implementation and test evidence; no provider/live/public or production proof |
| Agent type | worker |
| Invocation ID | `mfrp-fingerprint-t1-worker-2026-09-11` |
| Expected manifest | eleven Required Artifact Manifest paths |
| Actual changed set | nine paths touched or created (two existing test files needed no change) |
| Manifest delta | MATCH_WORKER_LANE; two manifest paths correctly required no edit |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | deterministic additive committed-evidence identity implementation only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: 121/121 focused manifest tests; 125/128 wider-consumer tests with 3 disclosed pre-existing failures |
| actionEvidence | ACTION_EVIDENCE_PRESENT: 27 new focused tests for the shared helper, updated collector tests, real temporary-Git-repository hostile matrix, and full pre-existing regression suite |
| invocationBoundary | internal workspace; no provider or external execution |
| interceptionBoundary | no interception, wrapper, or sandbox claim |
| claimLanguage | proposed and implemented bounded additive identity contract; no runtime enforcement claimed |
| forbiddenExpansion | no runtime, provider, public, package, MCP, or pilot execution; no historical receipt rewrite, marker clearing, or sample promotion |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private internal fingerprint-repair implementation and review; no
public export authorized by this tranche.

## Claim Boundary

This return proves bounded local deterministic Git-object identity behavior only. It does not accept itself, does not authorize selective execution or legacy gate suppression,
does not clear the recoverably archived `ADJUDICATED_REJECTED_OBSERVATION_2026-09-11_TPGR.json` marker, does not promote any historical sample, and does not open the parked
pilot nominees.

## git status --short

Working tree contains only the eight worker-lane implementation/test/doc paths plus this worker return; staging is empty.

## Changed Files

`git diff --name-status` reconciles exactly to the nine paths under Actual Changed Set; no other path is present in `git status --short`.

## Command Evidence

| Command | Result |
| --- | --- |
| CRLF/LF defect reproduction (isolated temp Git repo) | confirmed worktree bytes differ from committed blob bytes for the identical file under `core.autocrlf=true` |
| `python -m pytest governance/compat/test_committed_evidence_fingerprint.py governance/compat/test_run_agent_autorun_workflow_gate.py governance/compat/test_agent_autorun_machine_verification.py governance/compat/test_mfrp_shadow_canary_autocollect.py -q` | 121 passed |
| `python -m pytest governance/compat/test_agent_automation_machine_verification_readout.py governance/compat/test_mfrp_shadow_canary.py governance/compat/test_mfrp_shadow_canary_core.py -q` | 125 passed, 3 pre-existing failures disclosed (not caused by this tranche) |
| `git diff --check` | PASS |
| `python governance/compat/check_agent_packet_authority_and_encoding.py` | COMPLIANT |
| `python governance/compat/check_core_guard_self_protection.py` | requires this return's authorization block; expected COMPLIANT once this file is present in the changed set |

## No-Commit Statement

WORKER_MUST_NOT_COMMIT honored: HEAD remains `9abb0bdfe2123bccd5749cd0f90148d44cbe0424` and staging is empty. Only the Local closer may stage and commit after independent
reviewer acceptance.

## Return-Time Closeability Recheck

closeabilityDisposition: UNCLOSEABLE_PACKET_CONTRADICTION
outsideAuthorityBlockers: SYSTEM_CHAIN_MAP_SOURCE_DRIFT_REGISTRY_REFRESH_OUTSIDE_MANIFEST
nextRepairRoute: REVIEWER_LOCAL_REPAIR
workerRedispatchAllowed: NO

The `focused_checker_tests`, `adif_integrity`, and `pre_implementation_autorun` gates, which mutate only this exact eleven-path manifest, all pass. The aggregate
`worker_return_fast` gate is blocked by `check_system_chain_map_freshness.py`, a strictly read-only gate that reports `SOURCE_DRIFT` because this tranche legitimately changed
the bytes of two in-manifest source files (`governance/compat/run_agent_autorun_workflow_gate.py`, `governance/compat/agent_autorun_machine_verification.py`) that
`docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json` fingerprints. That registry file is outside the eleven-path Required Artifact Manifest and the checker itself never
writes the map; refreshing its recorded fingerprints after review acceptance is Local reviewer/closer's action, not a worker edit, so this is honestly recorded as
`UNCLOSEABLE_PACKET_CONTRADICTION` for the aggregate gate rather than `CLOSEABLE`, per the checker's binary contract (`closeabilityDisposition: CLOSEABLE` requires
`outsideAuthorityBlockers: NONE`, which would misstate the known blocker). The three disclosed pre-existing failures in `test_mfrp_shadow_canary.py` and
`test_mfrp_shadow_canary_core.py` are a separate, independently pre-existing finding (confirmed via `git stash` at `executionBaseHead`), also handed to Local reviewer rather
than silently absorbed into this tranche's scope. No foreseeable file split is required under the current size budget for the eleven-path implementation itself.

## Rework Return-Time Closeability Recheck

closeabilityDisposition: UNCLOSEABLE_PACKET_CONTRADICTION (unchanged from
generation 0's determination above; re-verified, not assumed carried forward)
outsideAuthorityBlockers: SYSTEM_CHAIN_MAP_SOURCE_DRIFT_REGISTRY_REFRESH_OUTSIDE_MANIFEST
nextRepairRoute: REVIEWER_LOCAL_REPAIR
workerRedispatchAllowed: NO
reworkGeneration: 1
findingsAddressedThisGeneration: F1, F2, F3, F4 (all four, consolidated in one round)

Re-verification performed at the start of this rework: `git stash` (all uncommitted rework changes) followed by re-running the three named pre-existing failing tests confirmed
byte-identical failure reasons at `executionBaseHead`, then `git stash pop` restored the rework changes with HEAD and staging unchanged
(`9abb0bdfe2123bccd5749cd0f90148d44cbe0424`, empty staging). No historical FAIL recorded above has been silently reclassified as PASS by this rework; the same `SOURCE_DRIFT`
blocker and the same three pre-existing consumer-test failures persist, now against this rework's further-modified byte content of the two in-manifest source files. This
worker return's own closeability claim remains `UNCLOSEABLE_PACKET_CONTRADICTION` at the aggregate-gate level for exactly the reason recorded above; it is not converted to
`CLOSEABLE` by this rework, because the outside-manifest blocker is unchanged and still outside this worker's authority to repair.

## Rework-2 Return-Time Closeability Recheck

closeabilityDisposition: UNCLOSEABLE_PACKET_CONTRADICTION (unchanged;
re-verified, not assumed carried forward)
outsideAuthorityBlockers: SYSTEM_CHAIN_MAP_SOURCE_DRIFT_REGISTRY_REFRESH_OUTSIDE_MANIFEST
nextRepairRoute: REVIEWER_LOCAL_REPAIR
workerRedispatchAllowed: NO
reworkGeneration: 2
findingsAddressedThisGeneration: F1 (historical-target admission), F4 (chain-test proof and isolation declaration)

Re-verification this round used read-only Git object inspection (`git show HEAD:<path>` recomputation) rather than `git stash`, per this round's explicit instruction not to
stash for baseline comparison. HEAD (`9abb0bdfe2123bccd5749cd0f90148d44cbe0424`) and staging (empty) are unchanged from generation 0 and generation 1. No historical FAIL
recorded in this document has been reclassified as PASS by this round; the same `SOURCE_DRIFT` blocker and the same three pre-existing consumer-test failures persist, now
against this round's further-modified byte content of the affected in-manifest source files. This worker return's own closeability claim remains
`UNCLOSEABLE_PACKET_CONTRADICTION` at the aggregate-gate level for exactly the reason recorded in generation 0's Return-Time Closeability Recheck; it is not converted to
`CLOSEABLE` by this round, because the outside-manifest blocker is unchanged and still outside this worker's authority to repair.

## Rework-3 Return-Time Closeability Recheck

closeabilityDisposition: UNCLOSEABLE_PACKET_CONTRADICTION (unchanged;
re-verified, not assumed carried forward)
outsideAuthorityBlockers: SYSTEM_CHAIN_MAP_SOURCE_DRIFT_REGISTRY_REFRESH_OUTSIDE_MANIFEST
nextRepairRoute: REVIEWER_LOCAL_REPAIR
workerRedispatchAllowed: NO
reworkGeneration: 3
findingsAddressedThisGeneration: F1 (clean-filter equivalence is not semantic equivalence)

Baseline comparison for the 3 pre-existing wider-consumer failures this round used direct `python -m pytest` re-execution against this environment's current, unstashed state
(no `git stash` at any point this round). HEAD (`9abb0bdfe2123bccd5749cd0f90148d44cbe0424`) and staging (empty) are unchanged from all prior generations. No historical FAIL
recorded anywhere in this document has been reclassified as PASS by this round; the same `SOURCE_DRIFT` blocker (against byte content this round did not further modify -- only
`committed_evidence_fingerprint.py` and test files changed) and the same three pre-existing consumer-test failures persist unchanged. This worker return's own closeability
claim remains `UNCLOSEABLE_PACKET_CONTRADICTION` at the aggregate-gate level for exactly the reason recorded in generation 0's Return-Time Closeability Recheck; it is not
converted to `CLOSEABLE` by this round, because the outside-manifest blocker is unchanged and still outside this worker's authority to repair. No authority contradiction was
encountered this round that this worker could not resolve within the existing contract: the fix stayed strictly within the byte-comparison mechanism already implied by the
governing contract's own CRLF/LF-only tolerated-equivalence language, required no expansion of that language, and required no weakening of the validator, collector, or
historical-target guard.

## Machine Closure Package

| Artifact | Evidence | Disposition |
| --- | --- | --- |
| Worker return status | `Status: COMPLETE_PENDING_REVIEW` | READY_FOR_REVIEW_WITH_DISCLOSED_BLOCKER |
| Work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_FINGERPRINT_T1_2026-09-11.md` | ACCEPT |
| Changed set | Actual Changed Set, Actual Changed Set (Generation 3) | MATCH (eleven of eleven manifest paths touched across generations 0+1+2+3) |
| Eleven-path implementation gates (focused tests: 150/150 at generation 1, 166/166 at generation 2, 171/171 at generation 3, `adif_integrity`, `pre_implementation_autorun`, `git diff --check`, `check_agent_packet_authority_and_encoding.py`) | Rework Verification, Rework-2 Verification, Rework-3 Verification, Gate Evidence | PASS |
| F1-F4 finding-specific regression proof (generation 1) | Rework Findings F1-F4 | PASS (29 new tests, 7 of which are real end-to-end producer/validator/collector chain proof) |
| F1/F4 finding-specific regression proof (generation 2) | Rework Findings F1 And F4 (Generation 2) | PASS (16 new/net-new tests: 9 helper-level, 3 producer-level, 4 net-new E2E-level) |
| F1 finding-specific regression proof (generation 3, clean-filter equivalence correction) | Rework Findings F1 (Generation 3) | PASS (5 new tests: 4 helper-level -- 2 clean-filter, 2 transform-survey -- and 1 new E2E-level; sensitivity confirmed via monkeypatched pre-fix reproduction at both levels) |
| Aggregate `worker_return_fast` gate | Rework Verification, Rework-2 Verification, Rework-3 Verification, Rework-3 Return-Time Closeability Recheck | Historical report superseded by Local repair verification; reviewer observed SOURCE_DRIFT and EQC findings. |
| Pre-existing out-of-manifest test failures | Risk / Corrective Action, Rework-3 Verification | UNCHANGED: same 3 failures, same reasons, re-confirmed this round without `git stash` |
