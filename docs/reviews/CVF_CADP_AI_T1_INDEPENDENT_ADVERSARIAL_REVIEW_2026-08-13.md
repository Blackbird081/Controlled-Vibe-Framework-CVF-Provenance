# CVF CADP-AI-T1 Independent Adversarial Review

Memory class: governed-review

Status: REVIEWER_ACCEPTED_BOUNDED

Original round-1 status: RETURN_FOR_REPAIR. Round-2 status was
REREVIEW_ACCEPTED_BOUNDED_PENDING_CLOSURE. Round 3 returned R13-R18, round 4
returned R19-R25, and round 5 returned R26-R28 for repair. All earlier
dispositions are superseded by the Round-6 Independent Review Addendum at the
end of this file; earlier evidence is retained unedited so the repair history
remains auditable.

docType: review

Date: 2026-08-13

Reviewer role: independent reviewer/adversarial reviewer (no commit authority
exercised)

Responds to work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_CADP_AI_T1_CVF_NATIVE_CONTRACT_KERNEL_2026-08-13.md`

Responds to worker return:
`docs/reviews/CVF_CADP_AI_T1_CVF_NATIVE_CONTRACT_KERNEL_WORKER_RETURN_2026-08-13.md`

executionBaseHead: `7402b083ec614ab6511fc7e579094b36a7089428`

Commit mode: `REVIEWER_NO_COMMIT_THIS_ARTIFACT`

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/run_worker_return_fast_gate.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_equivalence_claim_evidence.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_review_cost_control.py` |
| literalTokensReviewed | review-type structural heading groups (target/source, scope/methodology, findings/position, risk/corrective action, decision/disposition); Epistemic Process Block required fields; equivalence-claim disposition tokens (`MATCH`, `NOT_LITERAL_WITH_REASON`); non-ASCII text scan on newly added lines; absorption-artifact section triggers on external-source path citations |
| gateRunPurpose | confirm this review's own structural shape after drafting, since it cites the same private-reference source paths the CADP-AI packet already governs and could otherwise be misclassified as a new absorption artifact |
| claimBoundary | passing structure and literal-token checks do not replace the substantive adversarial findings recorded below; this block is shape-confirmation only |

## Purpose

Record an independent adversarial review of the CADP-AI-T1 CVF-native
capability admission/distribution contract kernel: verify the F01-F13
disposition claims, owner placement, canonical-serialization and receipt
determinism claims, evidence-authenticity (F11) claims, and locate any
type-safety or fail-open gap the worker-return positive-path tests did not
exercise. This review does not commit, push, run live provider calls, use
credentials, deploy CLI/MCP, or open T2-T7.

## Target / Source

- Target code under review:
  - `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-admission-distribution-profile.contract.ts`
  - `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-admission-distribution-profile.contract.test.ts`
  - `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/index.ts`
- Governing packet:
  - `docs/roadmaps/CVF_CADP_FULL_KNOWLEDGE_AND_IMPLEMENTATION_ABSORPTION_ROADMAP_2026-08-13.md`
  - `docs/baselines/CVF_GC018_CADP_AI_T1_CVF_NATIVE_CONTRACT_KERNEL_2026-08-13.md`
  - `docs/work_orders/CVF_AGENT_WORK_ORDER_CADP_AI_T1_CVF_NATIVE_CONTRACT_KERNEL_2026-08-13.md`
  - `docs/reviews/CVF_CADP_AI_T1_CVF_NATIVE_CONTRACT_KERNEL_WORKER_RETURN_2026-08-13.md`
- Private reference evidence only, not CVF authority: the corpus root
  recorded as `corpusRoot` in
  `docs/corpus-intelligence/manifests/cadp-r1-cvf-13-08-capability-admission-distribution-profile.json`
  (same source the CADP-AI roadmap's own External Absorption Core section
  already governs; not repeated here as a literal path)

## Scope / Methodology

1. Read `AGENTS.md`, `CVF_SESSION_MEMORY.md`,
   `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`, the active handoff
   `AGENT_HANDOFF_V59_2026-08-11.md`, `docs/reference/guard_orientation/README.md`,
   and `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
   before touching the review packet.
2. Read the roadmap finding matrix, GC-018 baseline, work order, worker
   return, corpus manifest and finding ledger, and the conditional reopen
   index diff.
3. Read the reviewed TypeScript contract, its test file, and the barrel
   export diff line by line.
4. Cross-read the cited private-reference Python source
   (`admission.py`, `semantic_rules.py`, `receipts.py`, `io.py`) to verify
   every "adapted" and "defect-corrected" claim against what the source
   actually does, not just what the roadmap says it does.
5. Wrote ten adversarial probe cases (fail-open, boundary, determinism,
   forgery) as a temporary Vitest file inside the package, executed them,
   recorded output, then deleted the file. No tracked path was created or
   left behind by this step.
6. Ran the full command set below and independently re-derived the F10/F13
   corpus counts and manifest hash rather than trusting the packet's
   self-reported numbers.
7. Verified the Alibaba provider test failure is pre-existing and
   CADP-independent using `git log`/`git status` on that file, a source
   grep for CADP imports, and inspection of its `describe.skipIf(!LIVE)`
   gate plus the live API key present in this environment.

## Findings / Position

### Executive Verdict

**RETURN_FOR_REPAIR**

The governance packet (roadmap, GC-018, work order, worker return, corpus
ledger) is well-constructed: every gate passes, F10/F13 evidence is genuine
and independently reproducible, and no finding was closed by prose alone.
The defect is in the code: adversarial probing found one BLOCKER and four
HIGH-severity fail-open/forgery gaps that the shipped implementation does
not enforce, even though the roadmap and work order assert the corresponding
invariants as fixed. Accepting T1 as-is would record false acceptance
criteria as evidence.

### Finding Table

| ID | Severity | File / symbol | Evidence | Risk | Required correction | Owner/tranche | Blocks T1 acceptance |
|---|---|---|---|---|---|---|---|
| R01 | BLOCKER | `capability-admission-distribution-profile.contract.ts:266-282` `createDeterministicCadpReceipt` | Adversarial probe: `{ ...input, receiptId: 'FAKE', contractVersion: 'FAKE' }` passed as input. Because `...input` is spread after the computed `receiptId`/`contractVersion` fields in the returned object literal, the caller-supplied values win. Observed output: `receiptId=FAKE`, `contractVersion=FAKE`, while `integrityHash` was still genuinely computed from the canonical payload. | A forged receipt can carry a real, verifiable `integrityHash` under an attacker-chosen `receiptId`/`contractVersion`. The only invariant the worker's own test asserts (`receiptId === cadp-${integrityHash}`) is silently defeatable by a caller who does not go through the happy path. | Destructure only the explicit fields the function computes (`contractVersion`, `receiptId`, `evidenceRefs`, `integrityHash`, the three `receiptGrants*` booleans) after spreading `input`, so the computed identity fields cannot be overridden. Add a negative test asserting hostile keys in the input object cannot change `receiptId`/`contractVersion`/`integrityHash`. | T1 / Guard Contract | YES |
| R02 | HIGH | `capability-admission-distribution-profile.contract.ts:208-233` `validateCompatibilityEvidence` | `EVIDENCE_LEVELS.indexOf(record.evidenceLevel)` returns `-1` for any value outside the six-member enum. Every `rank >= N` gate is then false, so an invalid/typo'd `evidenceLevel` such as `'TOTALLY_BOGUS'` returns `valid: true` with zero issues. | Directly fail-open: the worst input (a malformed evidence level) is treated as the safest, bypassing the entire F11 evidence ladder. Contradicts the roadmap acceptance criterion "evidence rank cannot be satisfied by a non-empty opaque string alone." | Reject `rank < 0` explicitly with an `EVIDENCE_MISSING` or new `EVIDENCE_LEVEL_INVALID` issue before any ladder check runs. | T1 | YES |
| R03 | HIGH | `capability-admission-distribution-profile.contract.ts:125-143` `validateCapabilityAdmission` | Adversarial probe: an admission record with `decision: 'BLOCK'` and `sourceVerified: false` still returns `valid: true` and a non-empty `assignableActionIds`. A subsequent `validateCapabilityAssignment` against that BLOCKED admission also returns `valid: true` with zero issues. The retained source's `resolve_admission` (`admission.py`) explicitly emits `ADMISSION_NOT_ASSIGNABLE` whenever `decision` is not `ADMIT`/`ADMIT_READ_ONLY`  -  this rule exists in the cited defect-evidence source function itself and was dropped during the port. | A capability the admission layer marked HOLD or BLOCK can still be validly assigned. This defeats the central admission-to-assignment gate the whole contract exists to enforce. | Emit an issue (e.g. reuse `SOURCE_UNVERIFIED` or add `ADMISSION_NOT_ASSIGNABLE`) whenever `decision` is not `ADMIT` or `ADMIT_READ_ONLY`, and return an empty `assignableActionIds` set in that case. | T1 | YES |
| R04 | HIGH | `capability-admission-distribution-profile.contract.ts:37,135` `CapabilityAdmissionDecision`, `validateCapabilityAdmission` | The retained source's `resolve_admission` filters `ADMIT_READ_ONLY` actions to exclude anything whose `mutationType` is in `MUTATING_TYPES` (`create/update/delete/system_config`). The TS port has no `mutationType`/action-metadata concept at all; `ADMIT_READ_ONLY` returns the full `admittedActionIds` list unfiltered, matching `ADMIT` (disposition: `NOT_LITERAL_WITH_REASON` - the two decisions produce the same output by omission, not by a documented equivalence). | `ADMIT_READ_ONLY` is semantically inert in the TS contract: a read-only admission can admit and later assign a `delete` action. This is a named safety property from the source that was silently lost, not consciously deferred. | Either model action mutation classification and filter under `ADMIT_READ_ONLY`, or explicitly record this narrowing as a bounded, named T2 defer in the roadmap Finding Resolution Matrix rather than implying F04 is fully implemented. | T1 (or explicit roadmap defer) | YES |
| R05 | HIGH | `capability-admission-distribution-profile.contract.ts:98-108,208-233` `CompatibilityEvidenceRecord.rawSecretsRecorded` | Adversarial probe: `rawSecretsRecorded: true` on an otherwise-valid `CompatibilityEvidenceRecord` returns `valid: true`, zero issues. The field is typed `false` in the interface comment/intent but is never read by `validateCompatibilityEvidence`. The retained source's `_compatibility` rule does check the equivalent field and raises `RAW_SECRET_INCLUDED`. | The evidence record's raw-secret invariant does not fail closed, unlike the admission, assignment, and distribution validators, which all correctly check their own `rawSecrets*` fields. This is a regression relative to the cited source, not a parked scope item. | Add `if (record.rawSecretsRecorded !== false) issues.push(issue('RAW_SECRET_INCLUDED', ...))`, matching the pattern already used in the other three validators. | T1 | YES |
| R06 | MEDIUM | `capability-admission-distribution-profile.contract.ts:257-264` `canonicalJson` | Adversarial probe compared `['a','A','_','U+00E4','z'].sort()` (ordinal) against the same array sorted with `localeCompare`: `["_","a","A","U+00E4","z"]` vs `["A","_","a","z","U+00E4"]`  -  different orders (disposition: `NOT_LITERAL_WITH_REASON`, confirmed by the probe's own printed comparison, not a copied claim). `canonicalJson` sorts object keys with `left.localeCompare(right)`, which is locale/ICU-dependent and can differ across Node builds, OS locale, and ICU data. | The roadmap's "deterministic receipt output is identical for identical explicit input" claim is proven only same-process/same-runtime by this review, not cross-platform (disposition: `NOT_LITERAL_WITH_REASON`  -  same-input-same-runtime equality was verified with `pnpm exec vitest run`; cross-runtime equality was not verified and is not claimed). The retained source uses `json.dumps(..., sort_keys=True)`, a stable ordinal/code-point sort. This matches gotcha #45 in `CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` (non-reproducible hash recipe from unstated sort behavior). | Replace `left.localeCompare(right)` with an explicit ordinal comparator (`left < right ? -1 : left > right ? 1 : 0`) so key ordering is code-point-based and reproducible across runtimes/locales. | T1 | YES |
| R07 | MEDIUM | `capability-admission-distribution-profile.contract.ts:257-264` `canonicalJson` | Adversarial probe: a payload containing `NaN` and a payload containing `Infinity` both serialize to `"null"` via `JSON.stringify`, producing the same `integrityHash` value for semantically different inputs (disposition: `NOT_LITERAL_WITH_REASON` - confirmed by direct probe comparison of the two computed hashes, not by inspection alone). A `BigInt` value throws an uncaught `TypeError` from `JSON.stringify` rather than a contract-level validation issue. | Two distinct payloads collide into the same receipt identity (`NaN` vs `Infinity`), and an unsupported numeric type crashes instead of failing closed with a typed error. | Explicitly reject non-finite numbers (`Number.isFinite` check) and unsupported types (bigint, function, symbol) with a clear thrown error or issue before hashing, rather than relying on `JSON.stringify`'s silent coercions. | T1 | NO (bundle with R06) |
| R08 | MEDIUM | `capability-admission-distribution-profile.contract.ts:182-206` `validateCapabilityDistribution` | Adversarial probe: `installMode: 'TOTALLY_UNKNOWN'` (outside the declared union) with a content path containing `CVF_SESSION/` returns `valid: true`  -  the private-provenance-export check only runs `if (manifest.installMode === 'PUBLIC_EXPORT')`. A malformed `sha256: 'zzz'` and a duplicate `path` entry are also accepted without complaint. | An unknown or mistyped `installMode` value silently bypasses the private-provenance export protection entirely, which is the specific control this function exists to enforce for public export. | Validate `installMode` is one of the three declared literals and reject unknown values; run the private-path check independent of `installMode` (or at minimum also for any value that is not verifiably `LOCAL_PRIVATE`/`INTERNAL_SHARED`); validate `sha256` shape and reject duplicate `path` entries. | T1 | YES |
| R09 | MEDIUM | all four validators in `capability-admission-distribution-profile.contract.ts` | Adversarial probe: `admissionId: ''`, `capabilityId: ''`, `capabilityVersion: ''` is accepted as valid; `admittedActionIds: ['read', 'read']` is preserved as a duplicate in `assignableActionIds`. Because `REFERENCE_MISMATCH` is checked with `!==`, two empty-string identities on both sides compare equal (disposition: `NOT_LITERAL_WITH_REASON`  -  equal by JavaScript strict-equality on empty strings, not a meaningful identity match) and the check is vacuously satisfied. | Weakens the "exact admission ID, capability ID, version" binding objective: an all-empty-string identity is treated as a valid, exactly-matching identity. Duplicate action/receipt IDs are carried through without normalization. | Reject empty or whitespace-only `admissionId`/`capabilityId`/`capabilityVersion`/`assignmentId`/`distributionId` fields; de-duplicate action ID and receipt ref sets before use. | T1 | NO |
| R10 | MEDIUM | `capability-admission-distribution-profile.contract.test.ts` (5 tests) | None of the five tests exercise: invalid evidence level, HOLD/BLOCK admission, `rawSecretsRecorded: true`, unknown `installMode`, empty IDs, or receipt-field forgery. `validateCapabilityDistribution` has zero direct test coverage despite being exported from the barrel. Every defect R01-R09 above survived the existing suite unnoticed (disposition: `MATCH`  -  reviewer re-ran `pnpm exec vitest run src/contracts/capability-admission-distribution-profile.contract.test.ts` and confirmed 5/5 pass while all ten adversarial probes still triggered). | The worker-return "5/5 tests pass" claim is true but is not the same claim as "invariants are proven" (roadmap calls this contribution toward F09's "negative-case suite"). All eight fail-open/forgery paths found by this review needed adversarial, not happy-path, tests to surface. | Add one negative test per finding R01-R09 before the contract is re-submitted for acceptance; add positive+negative coverage for `validateCapabilityDistribution`. | T1 | YES |
| R11 | LOW | `EXTENSIONS/CVF_GUARD_CONTRACT/src/package.boundary.test.ts` | Grep of the package-boundary test file for `cadp`/`Capability` finds no match; the CADP contract is not referenced by the package-boundary/import-surface test. | The work order's evidence requirement ("package-boundary/import verification") is not actually exercised for the new contract, only implied by a passing but non-covering test file. | Add the CADP barrel exports to the package-boundary test's expected surface. | T1 | NO |
| R12 | LOW | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`, `AGENT_HANDOFF_V59_2026-08-11.md` | `currentAuthority` in the bootstrap read model still points at the LRA-SA-T0 baseline/work order; the active handoff records an unrelated mode (`local_retention_semantic_absorption_t0_accepted_t1_parked`). The entire CADP-AI-T1 tranche exists only as uncommitted working-tree state, not yet reflected in session-sync surfaces. | Not a code defect; a bookkeeping gap. Anyone resolving "current session state" from the front door alone would not discover the pending CADP-AI-T1 review. | Session-sync steward updates the front door/handoff only at closure, per `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md`; not a T1 code blocker. | Session-sync steward | NO |

## Risk / Corrective Action

The eight code-level findings (R01-R05, R08 primarily; R06/R07/R09 secondary)
share one root cause: every validator in this file was written and tested
against its intended happy path, and none of the four positive-path/two
negative-path existing tests exercised an out-of-enum, empty-string,
non-`ADMIT` decision, or hostile-spread input. The fix pattern is uniform:
add the missing explicit check (never rely on an unmatched enum or unset
boolean defaulting to "safe"), then add one adversarial test per finding so
regressions are caught mechanically going forward. None of these require
runtime, provider, or credential access to fix or test  -  all are pure
TypeScript logic changes plus Vitest cases, well within the existing T1
Allowed Scope.

## F01-F13 Disposition Audit

| Finding | Roadmap disposition | Reviewer-verified state | Missing or overclaimed value |
|---|---|---|---|
| F01 capability assignment record | IMPLEMENTED_T1_PENDING_REVIEW | Partially implemented | Exact ID/version binding works; R03 (BLOCK still assignable) and R09 (empty-ID identity match) defeat the "exact binding" claim in edge cases |
| F02 distribution manifest enrichment | IMPLEMENTED_T1_PENDING_REVIEW | Partially implemented | R08: unknown `installMode` bypasses the private-export check entirely; zero direct test coverage |
| F03 compatibility evidence ladder | IMPLEMENTED_T1_PENDING_REVIEW | Partially implemented | R02: invalid `evidenceLevel` bypasses the entire ladder (fail-open on the worst input) |
| F04 admission schema enrichment | IMPLEMENTED_T1_PENDING_REVIEW | Partially implemented | R03/R04: HOLD/BLOCK non-assignability and `ADMIT_READ_ONLY` mutation-filtering from the cited source were both dropped in the port |
| F05 work-order capability binding | T2_PLANNED | Correctly parked | Reopen index row present with `PARKED_UNTIL_T1_ACCEPTED_AND_OPERATOR_RELEASE`; no implicit authority opened |
| F06 SaaS/remote side-effect discipline | T3_PLANNED_NO_LIVE_PROOF | Correctly parked | Correctly parked; no live/provider scope touched by T1 |
| F07 direct import/authority | TERMINAL_REJECT | Correctly terminal | Verified: no Python import, no dependency addition, no source execution anywhere in the diff |
| F08 local validator/projection/reconciliation | PARTIAL_T1; T2/T3_PLANNED | Partially implemented (honest split) | Split is accurately described; the T1 portion inherits R01-R09 |
| F09 negative-case suite | PARTIAL_T1; T2/T3_PLANNED | Overclaimed for the T1 portion | Five tests are not equivalent to a ported negative-case suite; see R10 |
| F10 source inventory evidence | COMPLETE_PENDING_REVIEW | Verified independently | 140 files / 36 directories / 230204 bytes and the manifest hash `4c8e34d426fd4ba6c8c39e972871b68dc95a30ee9adc5c6fa3749f25c74bfe45` were independently recomputed from the corpus root and matched exactly |
| F11 evidence authenticity gap | FIXED_T1_PENDING_REVIEW | Partially implemented, overclaimed as FIXED | Type/ref-identity/integrity-flag/authority-flag/owner checks are real improvements over the source's presence-only check, but the trusted index is caller-supplied, so `integrityVerified`/`authoritative` are asserted booleans, not verified facts; combined with R02 the ladder is bypassable outright |
| F12 non-deterministic receipt | FIXED_T1_PENDING_REVIEW | Partially implemented, overclaimed as FIXED | Ambient UUID/clock nondeterminism is genuinely fixed (explicit `issuedAt`, no `Date.now()`/`crypto.randomUUID()`); but R01 (identity forgeable), R06 (locale-dependent key order), R07 (NaN/Infinity collision) mean the "identical output for identical input" claim does not hold across all cases or runtimes |
| F13 evidence-count ambiguity | RESOLVED_BY_NARROWED_CLAIM | Verified | CVF's 140-file manifest count independently reproduced as controlling; the source's self-reported 133 is correctly treated as non-authoritative |

No finding in this table was closed by prose alone: every row has a concrete
code location, an owner, and either a passing verification or a named gap.
The systemic issue is that four rows (F04, F09, F11, F12) describe
guarantees the shipped code does not actually enforce in all cases.

## Test And Gate Evidence

Commands executed by this review, from repository root unless noted:

| Command | Result |
|---|---|
| `pnpm exec vitest run src/contracts/capability-admission-distribution-profile.contract.test.ts` (in `EXTENSIONS/CVF_GUARD_CONTRACT`) | PASS, 5/5 tests |
| `pnpm exec tsc --noEmit` (in `EXTENSIONS/CVF_GUARD_CONTRACT`) | PASS, exit 0 |
| `pnpm test` (in `EXTENSIONS/CVF_GUARD_CONTRACT`, full package) | 32 of 33 test files passed; 419 passed, 1 failed, 2 skipped  -  reproduces the worker-return's reported numbers exactly |
| `python governance/compat/run_worker_return_fast_gate.py` | COMPLIANT; reviewer-fast governance checks 63/63 PASS |
| `python governance/compat/check_governed_file_size.py --enforce` | COMPLIANT; no CADP file flagged (advisories listed are pre-existing, unrelated files) |
| `git diff --check` | PASS (CRLF-conversion warnings only, no conflict markers or trailing whitespace errors) |
| Independent manifest-hash recomputation (PowerShell SHA-256 over ordinal-sorted corpus-relative paths, UTF-8 no BOM, LF-joined, trailing LF) | MATCH: `4c8e34d426fd4ba6c8c39e972871b68dc95a30ee9adc5c6fa3749f25c74bfe45` |
| Independent file/dir/byte recount of the corpus root named in `corpusRoot` above | MATCH: 140 files, 36 directories, 230204 bytes |
| 10 adversarial Vitest probes (reviewer-authored, run from a temporary in-package file, then deleted) | 8 of 10 probes surfaced a defect (R01-R05, R08, plus the R06/R07/R09 supporting evidence); probe file left no trace in the tracked tree |

### Alibaba provider test failure: independently adjudicated as pre-existing and out of CADP scope

- `git log --oneline -1 -- EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/providers/alibaba-dashscope-provider.test.ts` shows the file's last change was commit `579b742b0` (well before this session); `git status --short` for that path is empty (unmodified).
- The file contains no import of any CADP symbol; `src/index.ts` and `src/runtime/agent-execution-runtime.ts` (the runtime/guard-engine import graph) contain no reference to `capability-admission` or `cadp`.
- The failing block is `describe.skipIf(!LIVE)(...)`, where `LIVE = API_KEY !== 'PLACEHOLDER_KEY'`. It only executes because `ALIBABA_API_KEY` is set as a real value in this environment, exercising a genuine live-provider network round trip that returned `BLOCKED` instead of `COMPLETED`.
- Conclusion: this is a pre-existing, environment-triggered live-provider test outcome, unrelated to any CADP import or global-state change. It is correctly out of CADP-AI-T1 scope and was not modified by this review, consistent with the forbidden-scope boundary (no provider/live remediation performed).
- A stronger clean-baseline A/B run (detached worktree at the pre-CADP commit) was attempted for additional certainty but failed with a Windows `Filename too long` error on an unrelated deeply nested legacy path; the failed worktree was fully removed and pruned (`git worktree remove --force`, `git worktree prune`), leaving no residue. The evidence above (unmodified file, no import, live-gated block, key present) is considered sufficient independent confirmation without it.

## Claim-Boundary Audit

**Proven by this review:**

- F10/F13 corpus evidence: independently recomputed and matched exactly (file
  count, directory count, byte count, manifest hash).
- No direct source import, no dependency addition, no source-package
  execution anywhere in the reviewed diff.
- T1 code has no filesystem, network, provider, credential, or process side
  effect (verified by reading every line of the reviewed file; no such API is
  called).
- Typecheck and the five focused tests pass as claimed.
- Owner placement is correct: the CADP contract lives inside the existing
  `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/` barrel; no duplicate
  canonical owner was created.
- T2-T7 remain correctly parked; the conditional reopen index diff opens no
  implicit authority beyond `REOPENED_BY_OPERATOR_T1_PENDING_REVIEW` for the
  T1 row itself.
- The Alibaba provider test failure is unrelated to CADP (see above).

**Not proven, and currently overclaimed in the governed packet:**

1. Roadmap acceptance criterion "evidence rank cannot be satisfied by a
   non-empty opaque string alone" is false as shipped (R02).
2. Roadmap acceptance criterion "assignment cannot exceed admitted action
   scope" does not hold when the admission decision is HOLD or BLOCK (R03).
3. Roadmap acceptance criterion "distribution cannot grant authority or
   export private provenance" does not hold when `installMode` is outside
   the declared union (R08).
4. Roadmap acceptance criterion "deterministic receipt output is identical
   for identical explicit input" is proven only same-runtime in this review,
   not cross-platform/cross-locale (R06), and is separately defeatable by
   direct forgery of the identity fields (R01).
5. F11 and F12 dispositions of `FIXED_T1_PENDING_REVIEW` should read
   `PARTIALLY_FIXED_PENDING_REPAIR` until R01/R02/R05/R06/R07 are corrected.
6. F09's "negative-case suite" framing overstates five tests that do not
   cover any of the eight findings in this review.
7. The worker return's "no side effects" and "focused verification pass"
   statements are accurate on their own terms but were read by this review
   as stronger evidence of correctness than the code supports; they do not
   claim invariant completeness and are not being corrected, only flagged
   as insufficient alone.

## Decision / Recommendation

**RETURN_FOR_REPAIR.** Required repair list, all within the existing T1
Allowed Scope (`capability-admission-distribution-profile.contract.ts` and
its test file):

1. R01 (BLOCKER) - stop caller input from overriding computed `receiptId`
   and `contractVersion` in `createDeterministicCadpReceipt`.
2. R02 - reject `evidenceLevel` values that do not resolve to a known rank.
3. R03 - emit a non-assignable issue and empty assignable set when the
   admission decision is not `ADMIT`/`ADMIT_READ_ONLY`.
4. R04 - implement or explicitly, narrowly defer `ADMIT_READ_ONLY` mutation
   filtering in the roadmap Finding Resolution Matrix.
5. R05 - validate `rawSecretsRecorded` on the compatibility evidence record.
6. R06/R07 - use an ordinal key comparator in `canonicalJson`; reject
   non-finite numbers and unsupported types explicitly.
7. R08 - validate `installMode` against its declared union and run the
   private-provenance check independent of that value; validate SHA-256
   shape and reject duplicate content paths.
8. R09 - reject empty/whitespace identity fields; de-duplicate action and
   receipt ID sets.
9. R10 - add one negative test per finding above; add coverage for
   `validateCapabilityDistribution`.
10. R11 - extend the package-boundary test to cover the CADP barrel exports.
11. Update the roadmap Finding Resolution Matrix: F11 and F12 to
    `PARTIALLY_FIXED_PENDING_REPAIR`, F09 to accurately describe current
    test coverage, and correct the four overclaimed acceptance-criteria
    statements identified in the Claim-Boundary Audit.

These changes alter validation semantics and add a substantive negative-test
suite; they exceed bounded reviewer-applied repair and belong to a worker
repair round under the existing CADP-AI-T1 work order, not to in-review
reviewer edits.

**T2 status:** remains PARKED. Its entry condition ("accepted T1") is not
met. The conditional reopen index already correctly records
`PARKED_UNTIL_T1_ACCEPTED_AND_OPERATOR_RELEASE`; no change to that row is
required by this review.

**Commit status:** FORBIDDEN. `WORKER_MUST_NOT_COMMIT` remains in force for
the work order, and this review's own `Commit mode` is
`REVIEWER_NO_COMMIT_THIS_ARTIFACT`. No commit, push, stash, or destructive
git operation was performed by this review. `HEAD` remains
`7402b083ec614ab6511fc7e579094b36a7089428`; the operator's pre-existing
uncommitted working-tree state (15 paths) is unchanged; pre-existing stash
entries were not touched or created.

## Finding-To-Governance Learning Disposition

Every one of the eleven code-level findings (R01-R11) passed 63/63 governance
checks, a clean TypeScript compile, and the existing 5/5 focused test suite.
The gate stack validated the packet's structural shape, not the code's
runtime semantics. This matches the pattern already recorded in
`docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
item 31 (gate-shape fixes are not absorption/correctness proof) and the
guard-orientation "Worker-return fast gates pass but ... value-conversion
gap" failure pattern.

| Finding | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| shipped code claimed an invariant (F11/F12 `FIXED`) that adversarial probing defeats (R01-R05, R08) | RULE_GAP | GOVERNANCE_CONTROL_PLANE | RUNTIME_LEARNING_CANDIDATE | worker repair round adds the missing checks plus one negative test per finding, per the Decision / Recommendation section above; whether a reusable machine checker for this class of gate-shape/semantics gap is warranted is left to the reviewer/closer completing the repair round |
| happy-path-only test suite let eight fail-open/forgery defects through 63/63 governance gates undetected (R10) | MACHINE_GATE_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no existing CVF checker targets test-suite adversarial coverage of a specific contract file; recording here as observation only, not proposing a new generic checker from a single tranche |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | independent reviewer / adversarial reviewer |
| Provider or surface | local private provenance workspace |
| Session or invocation | CADP-AI-T1 independent adversarial review, 2026-08-13 |
| Working directory | repository root |
| Command or tool surface | file reads, `git`, `pnpm`/Vitest/TypeScript, `python governance/compat/*`, temporary in-package adversarial probe file (deleted) |
| Target paths | CADP-AI-T1 review packet listed under Target / Source; reviewed contract/test/barrel files; private-reference source files cited in findings |
| Allowed scope source | operator instruction to review CADP-AI-T1 as independent/adversarial reviewer, no commit/push/live/CLI/MCP/T2-T7 |
| Before status evidence | CADP-AI-T1 worker return `COMPLETE_PENDING_REVIEW`; F11/F12 claimed `FIXED_T1_PENDING_REVIEW`; no independent adversarial verification recorded |
| After status evidence | eleven findings recorded with file/symbol/evidence/correction; F10/F13 independently verified; Alibaba failure independently adjudicated as pre-existing/out-of-scope |
| Diff evidence | `git status --short` before and after review shows the same 15 paths; no new tracked path added by this review step other than this file at commit time |
| Approval boundary | adversarial review and finding record only; no commit, push, live provider call, credential use, CLI/MCP deployment, or T2-T7 authority exercised |
| Claim boundary | findings are proposals for a worker repair round; no reviewer-applied code repair was made in this pass |
| Agent type | independent reviewer/adversarial reviewer |
| Invocation ID | `cadp-ai-t1-independent-adversarial-review-2026-08-13` |
| Expected manifest | this review file only |
| Actual changed set | this review file only |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename; the temporary adversarial probe file was created and deleted entirely within `EXTENSIONS/CVF_GUARD_CONTRACT/src/__reviewer_probe__/`, a path never committed or tracked |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | already-governed CADP-R1 intake and CADP-AI-T1 implementation, reviewed here for defect evidence; no new intake item is introduced by this file |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | Guard Contract contracts directory (unchanged; this review proposes no new owner) |
| Disposition | REVIEW_ONLY: adversarial defect findings against already-adapted code; no new ADAPT/DEFER/REJECT/NO_NEW_VALUE classification is made here |
| Claim boundary | this review makes no new absorption, ownership, or corpus claim; see Absorption Scope Note below |

## Absorption Scope Note

This file is an independent adversarial review of the already-completed
CADP-AI-T1 tranche, not a new external-knowledge-absorption artifact, so the
absorption-shape sections used by roadmap/work-order/worker-return packets
(source-and-authority core fields, corpus completeness, intake routing rows,
and overlap/novelty classification) do not apply here and are intentionally
omitted rather than restated. This review performs no new corpus scan,
enumeration, or manifest; adds no new intake row; and proposes no new CVF
owner surface. It cross-reads the already-governed CADP-R1 manifest and
finding ledger
(`docs/corpus-intelligence/manifests/cadp-r1-cvf-13-08-capability-admission-distribution-profile.json`,
`docs/corpus-intelligence/findings/cadp-r1-cvf-13-08-capability-admission-distribution-profile.md`)
and independently re-verifies that evidence under Test And Gate Evidence
above (manifest hash and file/directory/byte recomputation) without
rescanning or expanding the corpus. All private-reference source citations
in the findings above point to Python source already routed and disposed by
the CADP-AI roadmap's own Finding Resolution Matrix, Source Verification
Block, and External Absorption Core section; this review adds only defect
evidence against code already accepted into that owner surface, not a new
routing or ownership decision. Owner placement itself was reviewed and found
correct (see Claim-Boundary Audit above), not re-classified.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: given that the worker return recorded only
5/5 happy-path-oriented focused tests and two narrow negative assertions for
a fail-closed governance contract, adversarial probing of enum boundaries,
non-ADMIT decisions, unset boolean invariants, and receipt-field spread
order was expected to surface at least one fail-open or forgery gap the
existing suite did not cover.

Evidence Comparison: prediction confirmed and exceeded. Ten adversarial
probes were run; eight surfaced a concrete defect (R01-R05, R08, plus R06/R07
locale and numeric-collision evidence, and R09 empty-identity evidence). Two
probes (P6 collision-domain check, P10 prototype-key check) returned negative
results, i.e. no defect found for those specific attack shapes.

Contradiction Or Gap Disposition: no contradiction between the roadmap's
claimed dispositions and the observed code for F01, F02 (partially), F03
(partially), F07, F10, F13. A material gap exists between the roadmap's
`FIXED_T1_PENDING_REVIEW` disposition for F11/F12 and the observed fail-open/
forgery behavior in R01/R02/R05/R06/R07; this gap is the basis for the
RETURN_FOR_REPAIR verdict, not a contradiction requiring re-scoping of the
roadmap's finding taxonomy itself.

Claim Update: CADP-AI-T1 is not accepted. F11 and F12 should be reclassified
from `FIXED_T1_PENDING_REVIEW` to `PARTIALLY_FIXED_PENDING_REPAIR` pending a
worker repair round against findings R01-R10 in this review.

## Re-Review Disposition

Re-review date: 2026-08-13 (round 2, same independent reviewer role)

Re-review verdict: ACCEPT_WITH_BOUNDED_SCOPE

The worker repair round was independently re-verified, not accepted on report.
The reviewer re-ran the original adversarial probe set plus new probes against
the repaired contract; every round-1 finding that blocked acceptance now fails
closed as required.

### Round-1 Finding Re-Verification

| ID | Round-1 severity | Re-verified behavior | Disposition |
|---|---|---|---|
| R01 | BLOCKER | Hostile input carrying `receiptId`/`contractVersion`/`integrityHash`/`receiptGrantsExecution` no longer overrides computed identity; `createDeterministicCadpReceipt` now destructures only declared inputs and emits `receiptId === cadp-${integrityHash}` with `contractVersion` `cvf.cadp.v1` and all three `receiptGrants*` false | FIXED_VERIFIED |
| R02 | HIGH | Unknown `evidenceLevel` now yields `EVIDENCE_LEVEL_INVALID` and `valid: false` instead of silently satisfying the ladder | FIXED_VERIFIED |
| R03 | HIGH | `BLOCK` and `HOLD` both emit `ADMISSION_NOT_ASSIGNABLE`, return an empty assignable set, and propagate failure into assignment validation | FIXED_VERIFIED |
| R04 | HIGH | `ADMIT_READ_ONLY` now filters mutating actions via an explicit `CapabilityMutationType` model; assigning a `delete` action under read-only admission is rejected with `ACTION_OUTSIDE_ADMISSION` | FIXED_VERIFIED |
| R05 | HIGH | `rawSecretsRecorded: true` on a compatibility evidence record now emits `RAW_SECRET_INCLUDED` | FIXED_VERIFIED |
| R06 | MEDIUM | Object key ordering uses an explicit ordinal comparator rather than `localeCompare`; verified insertion-order independence and stable nested/deep ordering | FIXED_VERIFIED |
| R07 | MEDIUM | Non-finite numbers, bigint, undefined, symbol, function, class instances, sparse arrays and cyclic payloads now throw typed errors instead of colliding or hanging | FIXED_VERIFIED |
| R08 | MEDIUM | Unknown `installMode` emits `INSTALL_MODE_INVALID` and still runs the private-provenance check; malformed digests emit `DIGEST_INVALID`; duplicate content paths emit `DUPLICATE_VALUE` | FIXED_VERIFIED |
| R09 | MEDIUM | Empty/whitespace identity fields emit `INVALID_FIELD`; duplicate admission actions emit `DUPLICATE_VALUE`; receipt refs and action IDs are de-duplicated before hashing | FIXED_VERIFIED |
| R10 | MEDIUM | Focused CADP suite grew from 5 to 13 tests with finding-labeled negative cases (R01-R09), including previously untested `validateCapabilityDistribution` positive and negative paths | FIXED_VERIFIED |
| R11 | LOW | `package.boundary.test.ts` now imports the CADP surface through the canonical contracts barrel and asserts `CADP_CONTRACT_VERSION` plus all five exported validators | FIXED_VERIFIED |
| R12 | LOW | Session-sync surfaces still record the pre-CADP mode; unchanged and correct, since closure has not occurred and the tranche remains uncommitted | DEFERRED_TO_CLOSURE_AS_DESIGNED |

### Round-2 Regression Sweep

Nine additional probes were run to confirm the repairs introduced no new
defect: suppressed-assignable-set interaction with scope checks, assigned/
excluded overlap, invalid-rank short-circuit, nested-payload determinism,
array-order significance (order correctly remains significant and is not
sorted away), null-value stability, receiptType/subjectRef field-boundary
collision resistance, `issuedAt` participation in identity, and `__proto__`
payload keys leaving `Object.prototype` unpolluted. All nine passed with no
regression.

### Overclaim Correction Verification

All four acceptance criteria identified as false in the round-1 Claim-Boundary
Audit are now precisely scoped in the roadmap: determinism is stated for
supported JSON input under ordinal canonicalization with unsupported values
failing closed; the evidence-rank claim is bounded to the supplied
owner-verified evidence projection; HOLD/BLOCK non-assignability and
read-only-filtered scope are stated explicitly; and distribution fail-closed
behavior now names invalid modes, malformed digests, duplicate paths and
unknown-mode private provenance.

The F11 narrowing is accurate and is the single most important correction in
this round. Round-1 probe evidence showed a caller-fabricated trusted index
can still self-certify to `CERTIFIED_BOUNDED`; the reviewer re-confirmed this
residual behavior in round 2. The repaired roadmap now states F11 as
`PARTIAL_T1_PROJECTION_VALIDATION_REPAIRED_PENDING_REREVIEW` with source
authentication explicitly remaining a T2 owner-binding obligation. That is an
honest description of what the code does: T1 validates the projection it is
given; it does not authenticate the projection's origin. This residual is
disclosed rather than hidden, so it is accepted as a bounded, named limitation
rather than treated as an outstanding defect.

### Round-2 Test And Gate Evidence

| Command | Result |
|---|---|
| Reviewer adversarial re-verification probes (15 cases, temporary in-package file, deleted after run) | 15/15 pass; every round-1 blocking finding fails closed as required |
| Reviewer regression sweep probes (9 cases, temporary in-package file, deleted after run) | 9/9 pass; no repair-induced regression |
| `pnpm exec vitest run src/contracts/capability-admission-distribution-profile.contract.test.ts` | PASS, 13/13 tests |
| `pnpm exec vitest run src/contracts/capability-admission-distribution-profile.contract.test.ts src/package.boundary.test.ts` | PASS, 16/16 tests |
| `pnpm exec tsc --noEmit` | PASS, exit 0 |
| `pnpm test` (full package, hermetic; live provider key unset) | PASS, 33/33 files, 426 passed, 5 skipped |
| `pnpm test` (full package, reviewer shell with a live provider key present) | 428 passed, 1 failed, 2 skipped; the single failure is the same pre-existing live-gated provider case adjudicated in round 1 |
| `python governance/compat/run_worker_return_fast_gate.py` | COMPLIANT; reviewer-fast 63/63 PASS |
| `python governance/compat/check_governed_file_size.py --enforce` | COMPLIANT |
| `git diff --check` | PASS (line-ending warnings only) |

The hermetic full-suite figure reported by the repair round (426 passed, 5
skipped) was reproduced exactly by the reviewer after unsetting the live
provider key, then the key was restored. The reviewer's own shell has that key
set, which is why the same suite reports 428 passed with one live-gated
failure there. This confirms the reported figure is accurate and honestly
scoped, and re-confirms that the single failing case is environmental and
unrelated to CADP.

### Residual Bounded Limitations Accepted

1. Evidence-projection authentication remains an owner-binding obligation for
   T2; a caller-supplied trusted index is validated structurally, not
   authenticated at its source. Explicitly disclosed in the roadmap F11 row
   and acceptance criteria.
2. Cross-runtime byte-stability of the canonical serializer is now sound by
   construction (ordinal ordering, typed rejection of ambiguous values) but
   was executed on a single Node runtime in this review; multi-runtime
   execution is not claimed.
3. No runtime, provider, live, CLI/MCP, deployment, public-sync, or production
   behavior is proven by this tranche, and none is claimed.

### Re-Review Recommendation

T1 code is accepted as bounded and correct against the round-1 finding set and
the round-2 regression sweep. Remaining moves belong to the reviewer/closer and
operator, not to this review:

- closure commit of the material CADP paths, followed by a separate
  session-sync commit updating the front door, bootstrap read model, and
  active handoff, which still record the pre-CADP mode (R12);
- roadmap and work-order status conversion from
  `T1_REPAIR_COMPLETE_PENDING_REREVIEW` to the accepted-closure token chosen by
  the closer;
- T2 remains PARKED and requires explicit operator release plus a fresh
  authority packet; this acceptance does not release it.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this review concerns private, uncommitted CADP-AI-T1 implementation
evidence and the retained private-reference source; no public-sync surface
is touched.

## Claim Boundary

This review records an independent adversarial finding set for CADP-AI-T1
across two rounds. Round 2 accepts the T1 code as bounded and correct against
the round-1 finding set and the round-2 regression sweep; it does not itself
close or commit the tranche, does not perform the session-sync update, and
does not authorize T2-T7; does not claim runtime, provider, live, deployment, public-sync, or
production readiness; and does not claim that the eleven findings above are
exhaustive of every possible defect, only that they were found by the
adversarial methodology described in Scope / Methodology and independently
reproduced where marked.

## Round-3 Independent Review Addendum

### Round-3 Decision / Disposition

**RETURN_FOR_REPAIR**

The worker's `PARTIAL_REPAIR_WITH_F11_RESIDUAL` conclusion is correct about
F11 and correctly narrows the cross-runtime and governance-gate claims. It is
not sufficient for T1 acceptance. A new nine-case temporary Vitest probe
independently reproduced F11, D6 and the narrow D10 repair, then exposed four
receipt/integrity defects and one broader prototype-chain defect inside the
same T1 acceptance graph. The probe file was deleted after execution and is
not present in the changed set.

### Round-3 Consolidated Finding Table

| ID | Severity | File / symbol | Independently reproduced evidence | Required correction | Disposition |
|---|---|---|---|---|---|
| R13 | HIGH | `capability-admission-distribution-profile.contract.ts`; record validators | D10 checks own properties only for the text fields routed through `requireText`. An admission with own identity strings but inherited `decision`, `sourceVerified`, `admittedActions`, and false authority/secret fields still returns `valid=true`. The worker-return sentence that prototype-chain properties on record inputs are ignored is therefore false as written. | Validate own-property presence and runtime shape for every required top-level field and every nested action/content/evidence artifact field used by all four validators. Invalid casts must fail closed through issues or a consistently documented typed error, not be accepted through the prototype chain. Add negative tests covering inherited non-text fields and nested fields. | `BLOCKS_T1_ACCEPTANCE` |
| R14 | HIGH | `createDeterministicCadpReceipt` | The returned receipt retains the caller's original payload reference. Mutating the input payload after construction changes `receipt.payload` while `integrityHash` and `receiptId` remain unchanged. | Produce an owned canonical snapshot and prevent post-hash mutation of the returned payload/receipt, without freezing or mutating caller-owned input. Test both input-after-create mutation and attempted returned-payload mutation. | `BLOCKS_T1_ACCEPTANCE` |
| R15 | HIGH | `canonicalJson` | An enumerable getter on an otherwise plain object is executed by `Object.entries`. Two calls with the same object produced different hashes and observable getter side effects. | Reject accessor properties before reading values, or normalize through a side-effect-free own-data-property traversal. Align the supported-input claim and tests with the implemented rule. | `BLOCKS_T1_ACCEPTANCE` |
| R16 | HIGH | `canonicalJson`; returned receipt payload | Symbol-keyed payload data is returned to the caller but excluded from canonical serialization. Two payloads with different symbol-keyed values produced the same integrity hash. The same integrity-domain question applies to non-enumerable properties and non-index array properties. | Reject all own keys/properties outside the explicitly supported JSON data-property domain, including symbol keys, non-enumerable properties, accessors, and unexpected array properties, or ensure no unhashed data is returned. Add one negative test per shape class. | `BLOCKS_T1_ACCEPTANCE` |
| R17 | MEDIUM | `createDeterministicCadpReceipt`; `ISO8601_UTC_PATTERN` plus `Date.parse` | `2026-02-30T00:00:00Z` is accepted because the runtime normalizes the calendar-invalid date. This contradicts the function's strict-timestamp error language. | Validate calendar components exactly, including leap-year/day, hour, minute and second bounds; do not rely on normalization by `Date.parse`. Add boundary tests. | `BLOCKS_T1_ACCEPTANCE` |
| R18 | MEDIUM | T1 worker return and focused test names | The worker return header still says `REPAIR_COMPLETE_PENDING_REREVIEW`, old rows still say `FIXED_F11` and `fixed with tests`, while the appended section correctly says `PARTIAL_REPAIR_WITH_F11_RESIDUAL`. The focused test still uses the phrase `byte-stable` although only one runtime/OS/engine was executed. | Reconcile the whole worker return and test descriptions to one current bounded claim. Historical claims may be retained only when explicitly marked superseded. | `BLOCKS_HONEST_REREVIEW_PACKET` |

F11 remains `F11_RESIDUAL_OPEN_CALLER_SELF_ATTESTATION`. It is not reclassified
as fixed by this addendum and continues to block `CERTIFIED_BOUNDED`, trusted-
evidence, deployment-readiness, and production-readiness claims until a fresh
T2 owner-binding work order is implemented and independently accepted.

### Single-Pass Dependency-Closure Matrix

| Review dimension | Round-3 result | Closure route |
|---|---|---|
| contract/schema fields | R13 shows incomplete own-property/runtime-shape enforcement across the validators | consolidate all required and nested fields in one repair, not one field per turn |
| authority/source | F11 remains caller-self-attested; R13 permits inherited source/admission state | F11 stays T2; R13 is T1 |
| receipt identity/integrity | R14-R16 show mutable or unhashed returned state and accessor-driven nondeterminism | repair the canonical snapshot/input-domain implementation in T1 |
| timestamp contract | R17 shows calendar normalization accepted as strict input | repair in T1 |
| path/repository boundary | `../outside.txt` remains accepted as local distribution metadata, but T1 performs no filesystem resolution or copy | `DEFER_TO_T3_IMPLEMENTATION_WITH_REASON`; any consumer that resolves paths must enforce bundle-root confinement before I/O |
| negative tests | worker added D6/D10 tests, but they cover only a free-form timestamp and one inherited text field | add permanent R13-R17 regression tests and retain prior tests |
| gate strength | 63-check governance gate remains documentation-shape proof only and is not a code-correctness gate | keep explicitly parked for a separately authorized checker/gate tranche; do not cite 63/63 as runtime proof |
| closure/range | HEAD remains `7402b083ec614ab6511fc7e579094b36a7089428`; no T1 material commit exists | no closure or session sync while this decision is open |
| commit plan | worker must not commit; reviewer has not committed | one material plus at most one continuity commit only after independent acceptance |

### Round-3 Probe Evidence

| Command / probe | Result |
|---|---|
| `pnpm exec vitest run src/contracts/cadp.codex.r3.review-probe.test.ts` | PASS, 9/9 observation probes on Vitest 1.6.1; the passing assertions deliberately recorded current residual/defective behavior rather than asserting desired behavior |
| F11 caller-self-attestation | reproduced `valid=true`, evidence rank 5 |
| D6 free-form timestamp and D10 inherited `admissionId` | narrow repairs independently confirmed |
| inherited non-text admission state | reproduced `valid=true` |
| post-hash payload mutation | reproduced changed returned payload with unchanged receipt identity |
| enumerable accessor | reproduced two getter executions and two different hashes from the same object input |
| symbol-keyed payload data | reproduced different returned data with identical hash |
| calendar-invalid timestamp | reproduced acceptance of `2026-02-30T00:00:00Z` |
| relative parent distribution path | observed accepted metadata; classified non-blocking for T1 because this tranche has no path resolver or I/O |
| temporary probe cleanup | probe file deleted; no probe artifact remains in the worktree |

### Review Cost Telemetry And Stop Disposition

| Field | Value |
|---|---|
| reviewRoundCount | 3 |
| workerRepairTurnCount | 2 |
| newRootCauseCountThisRound | 3 |
| dependentFindingCountThisRound | 3 |
| elapsedReviewMinutes | NOT_AVAILABLE_WITH_REASON: cross-turn wall-clock telemetry is not exposed reliably |
| providerCallCount | 0 |
| tokenOrQuotaUsage | NOT_AVAILABLE_WITH_REASON: provider-neutral token accounting is not exposed |
| valueDelta | New critical integrity evidence shows the receipt can diverge from its hash and the canonicalization path accepts active or unhashed object state; acceptance would therefore be false. |
| stopDisposition | CONTINUE_NEW_CRITICAL_EVIDENCE |
| preRepairAuditDisposition | COMPLETE_BEFORE_FIRST_REPAIR |
| materialCommitCount | 0 |
| continuityCommitCount | 0 |
| commitPlanDisposition | NO_COMMIT_REVIEW |
| latencyDisposition | NOT_MEASURED_WITH_REASON: reliable cross-turn elapsed time is unavailable |
| avoidableDelayClass | SEQUENTIAL_FINDING_CASCADE |

Round three is continued only because R14-R16 are newly evidenced integrity
contradictions. This does not waive the round-three stop rule and does not
authorize an open-ended sequence: the worker must repair the complete matrix
above in one consolidated pass and return once for independent re-review.

### Round-3 Claim Update

The controlling claim is now: CADP-AI-T1 remains unaccepted and uncommitted.
F11 is honestly disclosed but open. D6 and the narrow text-field part of D10
are repaired, while R13-R17 remain open and R18 makes the worker packet
internally inconsistent. No `CERTIFIED_BOUNDED`, trusted-evidence, deployment,
runtime, provider/live, CLI/MCP, public-sync, production, or cross-runtime
determinism claim is permitted.

## Round-4 Independent Review Addendum

### Round-4 Decision / Disposition

**RETURN_FOR_REPAIR**

Round 3 materially improves the implementation: the permanent suite grew to
31 CADP tests, R14 object-snapshot immutability works for ordinary supported
objects, object accessors and hidden/symbol object properties are rejected,
calendar-invalid timestamps are rejected, and F11 remains honestly disclosed.
However, R13-R17 are not fully closed. Two temporary reviewer probe files ran
eight observation cases: seven reproduced residual behavior and one disproved
the reviewer's sparse-array hypothesis. Both probe files were deleted after
execution and no temporary artifact remains in the worktree.

### Round-4 Consolidated Finding Table

| ID | Severity | Dependency | Independently reproduced evidence | Required correction | Disposition |
|---|---|---|---|---|---|
| R19 | HIGH | R15/R16 canonical array traversal | `canonicalSnapshot` validates an array index descriptor inside `value.map(...)`, but `Array.prototype.map` reads the element first. An index getter executes once before the function throws. The statement that no accessor is ever invoked is false for arrays. | Walk caller arrays by numeric `for` loop and `Object.getOwnPropertyDescriptor` only. Do not call `map`, `every`, `forEach`, spread, iterator, or direct index access on an untrusted caller array before producing an internal snapshot. Add an array-index getter test asserting getter count remains zero. | `BLOCKS_T1_ACCEPTANCE` |
| R20 | HIGH | R13 validator array-shape validation | `isPlainArrayOfRecords` and `isPlainStringArray` use caller-array `map/every`. Accessors execute, and a non-enumerable string element was accepted by assignment validation with `valid=true`. Sparse arrays were independently confirmed to fail closed and are not a finding. | Replace both helpers with one descriptor-only dense-array reader that checks exact keys, enumerability, data descriptors and element type, and returns a new internal array. Use that internal array for all later loops. Cover record-array and string-array accessors plus non-enumerable elements. | `BLOCKS_T1_ACCEPTANCE` |
| R21 | HIGH | R13 assignment identity binding | After `validateCapabilityAdmission`, `validateCapabilityAssignment` still compares against `admission.admissionId`, `admission.capabilityId`, and `admission.capabilityVersion` through direct property access. An invalid accessor field was invoked during comparison. | Read admission identity only through validated own-data descriptors or a validated internal admission projection. No direct read from the caller record may occur after a failed validation. Add a getter-count-zero test. | `BLOCKS_T1_ACCEPTANCE` |
| R22 | HIGH | R13 side-effect-free malformed-input handling | Invalid decision/mutation/install/evidence values are interpolated with `String(value)`. A caller-controlled object with custom `toString` executed code during issue construction. | Never stringify an untrusted object/symbol through caller hooks. Emit a safe primitive/type label derived without coercion. Audit every error-message interpolation in the file. Add a coercion-counter-zero test. | `BLOCKS_T1_ACCEPTANCE` |
| R23 | HIGH | R14/R16 receipt snapshot-to-hash identity | Payloads `{value:-0}` and `{value:0}` return observably different numbers (`Object.is`) but receive the same JSON and integrity hash. The supported domain includes all finite numbers, so the claim that returned snapshot and hashed text cannot diverge is false. | Either normalize the returned snapshot's `-0` to `+0` to match the chosen `JSON.stringify` identity semantics, or serialize `-0` distinctly and document that algorithm. The returned payload and hash domain must agree. Add collision/normalization tests. | `BLOCKS_T1_ACCEPTANCE` |
| R24 | MEDIUM | R15/R16 receipt identity inputs | `evidenceRefs` is consumed by spread/sort before descriptor-safe canonicalization. An array-index getter executed and construction succeeded. | Validate and snapshot `evidenceRefs` with the same descriptor-only string-array rule before sorting/deduplication. Reject accessors, hidden/symbol/extra properties, sparse entries, non-strings and empty references without invoking caller code. | `BLOCKS_T1_ACCEPTANCE` |
| R25 | LOW | R17/R18 claim consistency | The regex accepts 1-9 fractional digits but the error text says `[.sss]`; the round-3 return allocates R17 four new tests although the test file has three R17 `it` cases, and its per-finding allocation sums to 17 while the actual delta is 16. | Make timestamp text state the actual 1-9-digit rule or enforce exactly three digits. Correct the worker-return test allocation/count without changing the verified totals of 31 focused and 444 package tests. | `BLOCKS_HONEST_REREVIEW_PACKET` |

### Round-4 Independent Evidence

| Command / probe | Result |
|---|---|
| reviewer temporary probe A | 6 cases: 5 observation cases passed, sparse-array observation failed because the implementation correctly rejected the sparse array; after correcting that reviewer assertion, 6/6 passed |
| reviewer temporary probe B | 2/2 observation cases passed: untrusted `toString` and `evidenceRefs` getter both executed |
| `pnpm exec tsc --noEmit` | PASS, exit 0 |
| focused CADP plus package-boundary suite | PASS, 34/34: CADP 31 plus package boundary 3 |
| hermetic full package suite | PASS, 33 files; 444 passed; 5 skipped |
| temporary probe cleanup | both reviewer probe files deleted; no probe artifact remains |

Passing current permanent tests does not contradict these findings: none of
the 31 CADP tests covers an array-index accessor, non-enumerable validator
array element, post-validation direct admission getter, active `toString`,
active `evidenceRefs`, or negative-zero snapshot normalization.

### Round-4 Review Cost Telemetry And Stop Disposition

| Field | Value |
|---|---|
| reviewRoundCount | 4 |
| workerRepairTurnCount | 3 |
| newRootCauseCountThisRound | 1 |
| dependentFindingCountThisRound | 6 |
| elapsedReviewMinutes | NOT_AVAILABLE_WITH_REASON: reliable cross-turn wall-clock telemetry is not exposed |
| providerCallCount | 0 |
| tokenOrQuotaUsage | NOT_AVAILABLE_WITH_REASON: provider-neutral token accounting is not exposed |
| valueDelta | The new negative-zero integrity contradiction and the reproduced accessor/coercion side effects show that accepting Round 3 would still make the snapshot-to-hash and side-effect-free claims false. |
| stopDisposition | CONTINUE_NEW_CRITICAL_EVIDENCE |
| preRepairAuditDisposition | COMPLETE_BEFORE_FIRST_REPAIR |
| materialCommitCount | 0 |
| continuityCommitCount | 0 |
| commitPlanDisposition | NO_COMMIT_REVIEW |
| latencyDisposition | LATENCY_BUDGET_EXCEEDED_WITH_REASON: connected array and coercion branches were not closed in the prior consolidated repair |
| avoidableDelayClass | SEQUENTIAL_FINDING_CASCADE |

Round 4 continues only because R23 is a new integrity contradiction and
R19-R24 demonstrate that earlier accepted repair statements remain false.
The next repair must replace the common unsafe-read mechanism once and add the
complete negative matrix; another field-by-field patch is not acceptable.

### Round-4 Claim Update

CADP-AI-T1 remains unaccepted, uncommitted, and not ready for closure. F11
remains `F11_RESIDUAL_OPEN_CALLER_SELF_ATTESTATION`. Round 3 repairs are useful
but incomplete against R13-R17. No `CERTIFIED_BOUNDED`, trusted-evidence,
deployment, runtime, provider/live, CLI/MCP, public-sync, production, or cross-
runtime determinism claim is permitted.

## Round-5 Independent Review Addendum

### Round-5 Decision / Disposition

**RETURN_FOR_REPAIR**

Round 4 closes the named R19-R25 array, coercion-message, negative-zero and
timestamp-text findings. Independent execution reproduced its reported 43
focused CADP tests, 46 combined focused tests, and 456-test hermetic package
result. T1 is nevertheless not acceptable because the descriptor-safe model
still begins after an unsafe receipt-input front door, and Proxy inputs remain
inside the claimed supported/plain-object domain while executing caller traps.

### Round-5 Consolidated Finding Table

| ID | Severity | File / symbol | Independently reproduced evidence | Required correction | Disposition |
|---|---|---|---|---|---|
| R26 | HIGH | `createDeterministicCadpReceipt` input front door | The constructor destructures `input` and later reads `input.evidenceRefs` directly. An own `evidenceRefs` getter executed and construction succeeded; inherited required `receiptType`/`subjectRef`/`issuedAt` fields were accepted; a caller object supplied as `receiptType` executed its `trim` method before rejection; an object supplied as `issuedAt` executed `Symbol.toPrimitive` during regex matching before a raw `value.slice is not a function` failure. | Read the input object itself through own-enumerable-data descriptors before any destructure, property access, string method, regex or coercion. Required scalar fields must be own primitive strings; `payload` must be an own data field; optional `evidenceRefs` must distinguish missing from malformed/accessor and use the existing descriptor-safe array reader. Inherited required fields and all active scalar/input accessors must be rejected without execution. | `BLOCKS_T1_ACCEPTANCE` |
| R27 | HIGH | all descriptor/introspection helpers and `canonicalSnapshot` | A Proxy payload around a plain object executed `getPrototypeOf`, `ownKeys` and descriptor traps, was accepted, and produced a receipt. A Proxy admission executed descriptor traps and returned `valid=true`. The code and worker return currently claim no caller accessor/code execution, but Proxy traps are caller code and the supported domain does not exclude them. | Define Proxy as unsupported. Reject Proxy values before every reflection/introspection entry point, including root/nested validator records, arrays, trusted-index artifacts, receipt input and recursively nested payload values. Use a trap-free runtime Proxy predicate available in the supported Node owner, then return validation issues for validators and typed errors for receipt construction. Add revoked-Proxy cases so rejection itself does not execute or throw from Proxy traps. | `BLOCKS_T1_ACCEPTANCE` |
| R28 | LOW | worker-return historical determinism block | The older Round-2 block still states negative zero is `not a defect`, while Round 4 correctly records R23 as a real snapshot/hash divergence that was repaired. Status history alone does not identify this semantic sentence as superseded. | Mark the older negative-zero sentence/block explicitly superseded by R23 and keep the current normalized-to-`+0` rule as controlling. | `BLOCKS_HONEST_REREVIEW_PACKET` |

### Round-5 Independent Evidence

| Command / probe | Result |
|---|---|
| temporary reviewer boundary probe | 4/4 observation cases passed after correcting one expected-throw shape: top-level getter execution, active scalar method/coercion, inherited receipt fields, and Proxy trap execution all reproduced |
| `pnpm exec tsc --noEmit` | PASS, exit 0 |
| focused CADP plus package-boundary suite | PASS, 46/46: CADP 43 plus package boundary 3 |
| hermetic full package suite | PASS, 33 files; 456 passed; 5 skipped |
| F11 | unchanged by source inspection and the passing permanent residual test; caller-self-attestation remains open |
| temporary probe cleanup | reviewer probe deleted; no probe artifact remains |

The initial boundary-probe run had one failed observation assertion because
the active `issuedAt` object executed its coercion hook and then threw during
the subsequent direct `.slice` call rather than completing. The corrected
assertion requires the throw and separately verifies that caller coercion was
already executed. This is evidence of the unsafe boundary, not a failed
reproduction.

### Round-5 Review Cost Telemetry And Stop Disposition

| Field | Value |
|---|---|
| reviewRoundCount | 5 |
| workerRepairTurnCount | 4 |
| newRootCauseCountThisRound | 2 |
| dependentFindingCountThisRound | 1 |
| elapsedReviewMinutes | NOT_AVAILABLE_WITH_REASON: reliable cross-turn wall-clock telemetry is not exposed |
| providerCallCount | 0 |
| tokenOrQuotaUsage | NOT_AVAILABLE_WITH_REASON: provider-neutral token accounting is not exposed |
| valueDelta | The receipt front door and Proxy domain are newly evidenced caller-code execution paths that contradict the side-effect-free contract and permit active objects to be accepted as valid/supported data. |
| stopDisposition | CONTINUE_NEW_CRITICAL_EVIDENCE |
| preRepairAuditDisposition | COMPLETE_BEFORE_FIRST_REPAIR |
| materialCommitCount | 0 |
| continuityCommitCount | 0 |
| commitPlanDisposition | NO_COMMIT_REVIEW |
| latencyDisposition | LATENCY_BUDGET_EXCEEDED_WITH_REASON: the reflection trust boundary was not included in earlier mechanism audits |
| avoidableDelayClass | SEQUENTIAL_FINDING_CASCADE |

Round 5 continues only for the new critical caller-code execution evidence.
The next repair must close the reflection boundary globally, not add special
cases for the four probe shapes.

### Round-5 Claim Update

CADP-AI-T1 remains unaccepted, uncommitted, and not ready for closure. Round 4
correctly repairs R19-R25, but R26-R28 remain open. F11 remains
`F11_RESIDUAL_OPEN_CALLER_SELF_ATTESTATION`; no `CERTIFIED_BOUNDED`, trusted-
evidence, deployment, runtime, provider/live, CLI/MCP, public-sync, production,
or cross-runtime determinism claim is permitted.

## Round-6 Independent Review Addendum

### Round-6 Decision / Disposition

**ACCEPT_WITH_BOUNDED_SCOPE**

Round 5 closes R26-R28. The receipt front door now validates own data before
using scalar or payload fields; active and revoked Proxy values are rejected
before reflection; caller accessors, coercion hooks and Proxy traps remained
at zero in the independent probe; and the negative-zero historical claim is
explicitly superseded. No new contract-blocking defect was found in the
bounded round-6 review matrix.

This is acceptance of the hermetic T1 contract layer against the accumulated
R01-R28 finding set and the listed independent probes. It is not acceptance of
F11 source authentication, full CADP safety, deployment readiness, production
readiness, or an exhaustive absence-of-defects claim.

### Round-6 Independent Evidence

| Command / probe | Result |
|---|---|
| temporary independent reflection-boundary probe | 4/4 pass: active receipt fields rejected with zero caller-hook calls; inherited required fields rejected; inherited optional `evidenceRefs` ignored without invocation; active/revoked Proxy values rejected with zero traps; F11 self-attestation reproduced |
| `pnpm exec tsc --noEmit` | PASS, exit 0 |
| focused CADP plus package-boundary suite | PASS, 64/64: CADP 61 plus package boundary 3 |
| hermetic full package suite | PASS, 33 files; 474 passed; 5 skipped |
| reviewer-fast governance gate | PASS, 63/63 |
| governed file-size guard | COMPLIANT; contract file remains advisory-only, not a violation |
| temporary probe cleanup | probe deleted; no temporary probe artifact remains |

### Reviewer-Owned Non-Behavioral Repair

The independent probe confirmed that inherited optional `evidenceRefs` is
ignored as absent and never participates in receipt identity. This behavior is
safe and matches the operator prompt's non-use requirement, but two worker
descriptions incorrectly said the inherited optional value was rejected. The
reviewer corrected only the inline comment and matching worker-return wording;
no executable behavior or test assertion changed.

### Residual F11 Boundary

The independent probe again produced `valid=true` and evidence rank 5 from a
caller-created, fully self-attested evidence index. Therefore:

- verdict remains `F11_RESIDUAL_OPEN_CALLER_SELF_ATTESTATION`;
- T1 validates a supplied projection but does not authenticate its source;
- `CERTIFIED_BOUNDED`, trusted-evidence, deployment-readiness and production-
  readiness claims remain blocked;
- closing F11 requires a fresh, separately authorized T2 owner-binding work
  order and another independent acceptance;
- this T1 acceptance does not release T2, commit, session sync, public sync,
  runtime/provider/live execution, deployment, or production work.

### Round-6 Review Cost Telemetry And Stop Disposition

This telemetry is voluntary because this artifact declares `docType: review`,
not `docType: completion_review`.

| Field | Value |
|---|---|
| reviewRoundCount | 6 |
| workerRepairTurnCount | 5 |
| newRootCauseCountThisRound | 0 |
| dependentFindingCountThisRound | 0 |
| elapsedReviewMinutes | NOT_AVAILABLE_WITH_REASON: reliable cross-turn wall-clock telemetry is not exposed |
| providerCallCount | 0 |
| tokenOrQuotaUsage | NOT_AVAILABLE_WITH_REASON: provider-neutral token accounting is not exposed |
| valueDelta | R26-R28 are independently closed; the remaining F11 gap is accurately isolated behind a fresh T2 owner-binding boundary. |
| stopDisposition | COMPLETE_REVIEW |
| preRepairAuditDisposition | COMPLETE_BEFORE_FIRST_REPAIR |
| materialCommitCount | 0 |
| continuityCommitCount | 0 |
| commitPlanDisposition | NO_COMMIT_REVIEW |
| latencyDisposition | LATENCY_BUDGET_EXCEEDED_WITH_REASON: the contract required repeated adversarial repair rounds before the complete reflection and integrity boundary was closed |
| avoidableDelayClass | SEQUENTIAL_FINDING_CASCADE |

### Round-6 Claim Update

CADP-AI-T1 is accepted only as a bounded, hermetic contract layer
against R01-R28 and the recorded probes. F11 remains open. Cross-runtime
execution proof remains not established. Closure/commit and continuity sync
remain reviewer/closer actions. The operator explicitly released T2 on
2026-08-13; implementation remains prohibited until its fresh governed work
order is committed and dispatched.
