# CVF RSPB-AI-T5-R1 Fail-Closed Repair Independent Review

Memory class: governed-completion-review

Status: REVIEWER_ACCEPTED_PENDING_CLOSER

Date: 2026-08-16

## Purpose

Independent, distinct re-review of the bounded RSPB-AI-T5-R1 repair applied
to the RSPB-AI-T5 capability case and domain-evidence projection kernel. The
original worker return was superseded by a reviewer-owned repair after the
prior independent review found eight material fail-closed and determinism
defects (recorded in
`docs/reviews/CVF_RSPB_AI_T5_R1_FAIL_CLOSED_REPAIR_EVIDENCE_2026-08-16.md`).
This review verifies the repaired state independently, without trusting the
repair's own reported counts.

## Target / Source

Target: the uncommitted five-path RSPB-AI-T5 tranche at execution base
`2133f5cb9b0583655a785d4e41f5005fe4763212`. Source authority: the canonical
work order and paired GC-018 baseline, the original worker return (retained
unchanged as historical evidence), the R1 repair evidence packet, and the
actual current source of the three reviewed implementation paths.

## Scope / Methodology

Read `AGENTS.md`, the active session bootstrap read model, session memory
front door, guard orientation index, literal-format gotchas checklist, the
canonical work order, the paired GC-018 baseline, the original worker
return, and the R1 repair evidence, in that order, before inspecting source.
Read the complete current content of all three reviewed implementation
paths line by line rather than relying on the repair evidence's prose
summary. Independently reproduced every required hermetic command.
Authored sixteen adversarial probes in a git-ignored scratch directory
(`EXTENSIONS/CVF_GUARD_CONTRACT/node_modules/.cvf-t5r1-probe/`, removed
after use) targeting sparse arrays, nested (not just top-level) collection
bounds, secret-signal false positives on ordinary safe prose, authority-
literal tampering on route/readiness lookalikes, cross-binding forgery
between route and readiness, Proxy-shaped optional-evidence references,
three-way digest determinism (not only the repair's own two-item
reversal), a genuine three-item permutation, STALE/INVALID distinctness
under combined issues, a null-prototype record, and an `Array` subclass
input. Confirmed the barrel export surface and the absence of any
filesystem, network, clock, or credential API in the implementation file.

## Findings / Position

No material defect was found in the repaired state. All eight defects
recorded in the R1 repair evidence are independently confirmed fixed by
direct source inspection and adversarial reproduction, not merely by
rerunning the repair's own test file. One informational, non-blocking
observation is recorded below; it does not affect the verdict.

**Informational (non-blocking):** an `Array` subclass instance (e.g.
`class MyArray extends Array {}`) passes `isBoundedPlainArray` and is
accepted as a normal collection (probe P13). This is correct behavior, not
a defect: `Array.isArray` recognizes exotic array objects regardless of
their prototype chain per the ECMAScript specification, the subclass in
the probe defines no additional fields or overridden semantics, and
nothing in the kernel trusts array *identity*, only its element and
own-indexed-property shape, which `isBoundedPlainArray` still verifies
(lines 182-188). Recorded for completeness because it was an edge case the
repair's own 27-test suite did not exercise.

## Risk / Corrective Action

None required. No repair, edit, stage, commit, or file modification was
performed by this review; the one informational observation requires no
corrective action.

## Decision / Disposition

`REVIEWER_ACCEPTED_PENDING_CLOSER`. The repaired implementation is
independently verified fail-closed, secret-safe, deterministic, and
non-authority-granting. Commit, closure, continuity promotion, runtime
activation, and public export remain unauthorized by this review; those
are reviewer/closer actions.

## Reviewer Independence

- This reviewer did not author the original T5 worker implementation, the
  R1 repair, or either evidence packet reviewed here.
- No file was modified, staged, committed, reverted, or stashed by this
  reviewer. Sixteen adversarial probes were written to and executed from
  the git-ignored `EXTENSIONS/CVF_GUARD_CONTRACT/node_modules/.cvf-t5r1-probe/`
  directory and deleted after use; this directory never touched a tracked
  path.
- Starting and ending HEAD: `2133f5cb9b0583655a785d4e41f5005fe4763212`
  (unchanged throughout this review).
- `git status --short`, MATCH before and after this review:

```text
 M EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/index.ts
?? EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-case-evidence-projection.contract.test.ts
?? EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-case-evidence-projection.contract.ts
?? docs/reviews/CVF_RSPB_AI_T5_CAPABILITY_CASE_AND_DOMAIN_EVIDENCE_PROJECTION_KERNEL_WORKER_RETURN_2026-08-16.md
?? docs/reviews/CVF_RSPB_AI_T5_R1_FAIL_CLOSED_REPAIR_EVIDENCE_2026-08-16.md
```

Exactly this five-path changed set, matching the R1 repair evidence's own
declared manifest: the original worker return (`M` on `index.ts` plus two
new files) plus one new reviewer-owned repair-evidence file. No unexpected
deletion or rename occurred (`git diff --name-status` shows only `M` on
`index.ts`; the remaining four paths are additions).

- No provider, network, credential, subprocess-spawning, or live call was
  made at any point during this review.

## Exact Changed-Set Confirmation

`git diff --name-status` against HEAD shows exactly one modification:

```text
M       EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/index.ts
```

Combined with `git status --short` above, the full changed set is:

- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-case-evidence-projection.contract.ts` (new)
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-case-evidence-projection.contract.test.ts` (new)
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/index.ts` (modified: one added export block, confirmed by inspection to add only the T5 public surface)
- `docs/reviews/CVF_RSPB_AI_T5_CAPABILITY_CASE_AND_DOMAIN_EVIDENCE_PROJECTION_KERNEL_WORKER_RETURN_2026-08-16.md` (new, unchanged historical worker-time evidence)
- `docs/reviews/CVF_RSPB_AI_T5_R1_FAIL_CLOSED_REPAIR_EVIDENCE_2026-08-16.md` (new, reviewer-owned repair evidence)

No deletion and no rename anywhere in this set.

## Requirement-By-Requirement Verification

| # | Required verification | Result |
|---|---|---|
| 1 | Proxy, accessor/getter, malformed-object, sparse-array, oversized-array inputs fail closed without throwing | Confirmed. `isPlainRecord` (lines 165-173) rejects Proxies via `isProxy`, rejects any object carrying symbol keys, and rejects any object whose own-property descriptors include a `get`/`set` accessor rather than a plain `value`. `isPlainArray` (175-180) applies the equivalent checks to arrays. `isBoundedPlainArray` (182-188) additionally rejects arrays over 256 items and any array missing a dense own-indexed property at any index below its length, which rejects sparse arrays. Probes P1 (sparse array), P2 (nested 257-item array), P7 (Proxy as an optional-reference value), and the original throwing-getter tests in the repaired suite all confirm no throw and a fail-closed `issues` entry. |
| 2 | Route/readiness inputs require canonical schema, identity bindings, `authorityStatus` literals, `executionAuthorized=false`, bounded collections, and timestamps | Confirmed by direct source read (lines 427-474) and adversarial probes. `routeValid` checks `schemaVersion === CAPABILITY_ROUTE_DECISION_VERSION`, four identity-bound `validId` fields, `stage` against the real `ROUTE_STAGES` enum, a bounded `confidence`, five `isBoundedPlainArray` collection checks, `validUtc(generatedAt)`, the literal `authorityStatus === 'CANDIDATE_ONLY'`, the literal `executionAuthorized === false`, and cross-binding of `requestId`/`workspaceId` to the case input. `readinessValid` performs the parallel check plus binding `readinessDecision.routeDecisionId === routeDecision.routeDecisionId`. Probe P4 (tampered `executionAuthorized: true`) and P5 (tampered `authorityStatus`) are both rejected; probe P6 (readiness bound to a different route) is rejected; the repair's own "lookalikes" test is independently reproduced as PASS. |
| 3 | Optional acquisition authorization/receipt inputs require canonical result shape and an explicit source reference | Confirmed (lines 483-518). `hasAuthorization` requires `contractVersion === CONTROLLED_ACQUISITION_CONTRACT_VERSION`, a real `decision` enum value, and a bounded `issues` array; presence without a valid `acquisitionAuthorizationRef` (or a ref present without evidence) is rejected. The parallel check applies to the receipt. Probe P7 confirms a Proxy-shaped ref does not throw (short-circuited by `typeof value !== 'string'` in `normalizeNullableSafeString`, which never touches the Proxy's `get` trap) and is rejected as `INVALID_FIELD`. |
| 4 | Any non-staleness validation issue makes `currentDisposition` `INVALID` | Confirmed (line 582-587): `hasNonStalenessIssue = issues.some(({ code }) => code !== 'STALE_SOURCE')`; if true, `currentDisposition` is unconditionally `'INVALID'` regardless of the actual `staleness` value. Probe P10 (a combined secret-rejection issue plus expiry) shows `staleness: 'STALE'` but `currentDisposition: 'INVALID'`, confirming non-staleness issues take precedence in the disposition field while the staleness field itself stays accurate. |
| 5 | `STALE` remains distinct from `INVALID` | Confirmed. Probe P11 (pure expiry, no other issue) yields `staleness: 'STALE'` and `currentDisposition: 'STALE'` together; probe P10 (expiry plus a secret-rejection issue) yields `staleness: 'STALE'` but `currentDisposition: 'INVALID'` -- the two fields never collapse into one meaning, and `staleness` is never overwritten by the disposition logic. |
| 6 | Secret-like inputs are rejected without echoing values | Confirmed. The repaired `SECRET_SIGNAL` regex (line 149) requires an `sk-` prefixed token, a `bearer <token>` shape, a `key=value`/`key:value` assignment shape for a fixed set of secret-shaped field names, or a PEM private-key header -- not a bare keyword. The repaired suite's four secret-rejection tests (evidence observation, standalone `sk-*` value, finding claim, nested remediation) were independently reproduced as PASS, each asserting the rejected value string is absent from `JSON.stringify(result)`. |
| 7 | Ordinary safe prose such as "token budget" is not rejected merely for containing "token" | Confirmed by probe P3 (`"stayed within token budget for this projection"`) and P3b (`"the session ended normally after evaluation"`): both are accepted with zero `SECRET_LIKE_VALUE_REJECTED` issues, only the expected `UNVERIFIED_FINDING_REFERENCE` from the fixture's finding pointing at a differently-named evidence ID. This directly demonstrates the repaired regex is anchored to secret-shaped patterns, not bare keyword matching. |
| 8 | Multi-item permutations produce the same normalized output and digest | MATCH. Probe P9 constructs three independently-ordered three-item evidence permutations (not the repair's single two-item reversal) and confirms all three produce the same `projectionDigest` and normalized `evidence` order (`ev-a, ev-b, ev-c` in every case), driven by the `evidence.sort(...)`/`findings.sort(...)`/`paths.sort(...)`/`issues.sort(...)` calls (lines 544, 561, 578-579) before digesting. Probe P8 additionally confirms digest equality across three separately constructed (not array-derived) equivalent inputs. Probe P15 reproduces the exact original defect #6 scenario from the repair evidence and confirms it is now fixed. |
| 9 | Authority-relevant changes alter the digest | Confirmed by independently reproducing the repaired suite's `produces a different digest when an authority-relevant input changes` test (PASS) and by probe P4/P5, where tampering `executionAuthorized` or `authorityStatus` changes `issues` and `currentDisposition`, which are digested fields. |
| 10 | Findings with unresolved evidence cannot remain current/ready | Confirmed. `validateFinding` (lines 299-306) marks an unresolved-reference finding `UNVERIFIED`, and `UNVERIFIED_FINDING_REFERENCE` is a non-staleness issue, so per requirement 4 the overall `currentDisposition` becomes `INVALID`, never `READY` or any readiness-state passthrough. Independently reproduced via the repaired suite's corresponding test and via probes P3/P3b, which incidentally exercise this same path. |
| 11 | Unsupported `DEMONSTRATED` path steps cannot remain demonstrated | Confirmed. `validatePathStep` (lines 338-341) downgrades to `'INFERRED'` unless the declared `evidenceRef` both normalizes safely and resolves in the accumulated `evidenceIds` set. Independently reproduced via the repaired suite's downgrade test and its positive counterpart (a step that does resolve stays `DEMONSTRATED`). |
| 12 | The projection cannot grant execution or mutation authority | Confirmed. Every returned projection carries the literal `authorityNotice: 'PROJECTION_ONLY'` and literal `authorityMutation: false` (lines 595-596), both frozen at the top level (`Object.freeze` at line 612) and independently confirmed frozen against tampering via the repaired suite's mutation-resistance test, reproduced here as PASS. `JSON.stringify(result)` was independently checked to never match `"executionAuthorized":true` under any probe input, including the two adversarial forgery probes P4 and P5. |
| 13 | No filesystem, adapter, executor, ambient-clock, credential, network, provider/live, MCP/CLI, public-sync, or deployment behavior was introduced | Confirmed by direct source inspection: the file's only imports are `node:crypto` (`createHash`, used solely for the local digest), `node:util/types` (`isProxy`), and type-only imports from the two sibling T3/T4 contract files. A pattern scan for `fetch(`, `fs.`, `readFile`, `writeFile`, `process.env`, `new Date()`, `Date.now()`, `child_process`, and `http(s).request` found zero matches. `now` is accepted only as a required string parameter with no default, so no ambient clock read is possible. |
| 14 | Barrel exports expose only the intended T5 public surface | Confirmed. The `index.ts` diff adds exactly one export-type block (sixteen names: three enum-like unions, seven input interfaces, four output interfaces, one issue-code union, one issue interface, one top-level projection interface) and one export block (three version constants plus `projectCapabilityCaseEvidence`). A grep for every internal helper name (`isPlainRecord`, `isPlainArray`, `isBoundedPlainArray`, `compareText`, `canonicalJson`, `computeProjectionDigest`, `safeString`, `normalizeNullableSafeString`, `validateEvidence`, `validateFinding`, `validatePathStep`, `validatePath`, `evaluateStaleness`, `isSecretLike`, `validUtc`, `validId`) inside `index.ts` returned zero matches. |
| 15 | The original worker return remains unchanged historical evidence; the R1 repair evidence supersedes its test counts for the repaired state | MATCH. The worker-return file's `git status --short` marker is unchanged (`??`, untracked, same content as worker time). The R1 repair evidence explicitly states that final counts supersede worker-time counts only for the repaired state, and this review's independently reproduced counts (27/27, 104/104, 624/629) match the repair evidence's repaired-state counts. |

## Independently Reproduced Commands

| Command | Working directory | Result |
|---|---|---|
| `npx vitest run --pool forks src/contracts/capability-case-evidence-projection.contract.test.ts` | `EXTENSIONS/CVF_GUARD_CONTRACT` | PASS - 27/27 tests |
| `npx vitest run --pool forks` on the T5 kernel test plus `capability-route-readiness.contract.test.ts`, `controlled-acquisition.contract.test.ts`, `src/index.test.ts`, `src/package.boundary.test.ts`, `src/boundary.signals.test.ts` | `EXTENSIONS/CVF_GUARD_CONTRACT` | PASS - 104/104 tests across 6 files |
| `npm run check` (`tsc --noEmit`) | `EXTENSIONS/CVF_GUARD_CONTRACT` | PASS - no type errors |
| `npm test` (full package suite) with `ALIBABA_API_KEY`, `CVF_BENCHMARK_ALIBABA_KEY`, `CVF_ALIBABA_API_KEY`, `CVF_ALIBABA_LIVE_TEST`, `CVF_GEMINI_LIVE_TEST` explicitly cleared to null in the child process | `EXTENSIONS/CVF_GUARD_CONTRACT` | PASS - 624 passed, 5 skipped (all live-gated), 629 total, 40 test files, zero provider/network calls |
| `git diff --check` | repository root | PASS - exit 0, no whitespace/conflict errors |
| `python governance/compat/run_worker_return_fast_gate.py` | repository root | PASS - corpus scan registry, epistemic process packet, worker-return quality gate, and reviewer-fast (64/64) all COMPLIANT, `git diff --check` PASS |
| Sixteen independent adversarial probes (P1-P15 plus P3b), git-ignored temp directory, removed after use | `EXTENSIONS/CVF_GUARD_CONTRACT` | 16/16 probes PASS; all confirm correct fail-closed, non-throwing, secret-safe, deterministic, and non-authority-granting behavior |

Every worker/repair-reported count in the R1 repair evidence (27/27,
104/104, 624 passed/5 skipped/629 total, TypeScript PASS) matched
independent reproduction exactly.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/run_worker_return_fast_gate.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_epistemic_process_packet.py` |
| literalTokensReviewed | required structural headings for a `docs/reviews/` review artifact (Target/Source, Scope/Methodology, Findings/Position, Risk/Corrective Action, Decision/Disposition group); Agent Operation Trace field labels; Finding-To-Governance defect-class enum; Public Export Disposition allowed tokens; Epistemic Process required fields (Evidence Comparison, Contradiction Or Gap Disposition, Claim Update) |
| gateRunPurpose | confirmation and evidence after authoring from known checker shapes; this reviewer-owned file is created once, so no fast-gate rerun-and-repair cycle applies to it the way it did to the worker return |
| claimBoundary | read-ahead covers packet structure only; it does not substitute for the semantic adversarial verification performed above |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| reviewer packet initially omitted checker-required routing and learning enum literals | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | closer applied packet-shape normalization without changing the independent verdict or implementation |
| an `Array` subclass instance is accepted by `isBoundedPlainArray` | OPERATOR_SCOPE_CLARITY_GAP | DOCUMENTATION_ONLY_LEARNING | N/A_WITH_REASON | confirmed correct behavior per ECMAScript `Array.isArray` semantics and the kernel's own invariants; no implementation action required |

runtimeProviderCostLearningLane: N/A_WITH_REASON - all sixteen adversarial
probes and every reproduced command were local and hermetic; no provider or
live call occurred during this review.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | accepted local synthesis cluster -> governed T5 work order -> worker implementation -> reviewer repair -> distinct independent re-review |
| Matching local-view guard | `governance/compat/check_mixed_origin_derived_synthesis_absorption.py` |
| Owner surface | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-case-evidence-projection.contract.ts` |
| Disposition | ADAPT_TO_EXISTING_OWNER |
| Claim boundary | local candidate material remains evidence; the accepted projection kernel grants no runtime or execution authority |

## Closer Packet-Shape Normalization

After the independent reviewer returned its verdict, the closer replaced two
non-ASCII punctuation characters, added the checker-required routing and
learning literals, and clarified equivalence evidence with `MATCH`. These are
documentation-only gate-shape edits. They do not change the review findings,
test evidence, verdict, implementation, or reviewer-independence claim.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | independent reviewer (distinct from both the original worker and the R1 repair steward) |
| Provider or surface | local private provenance repository |
| Session or invocation | RSPB-AI-T5-R1 independent re-review, 2026-08-16 |
| Working directory | repository root and `EXTENSIONS/CVF_GUARD_CONTRACT` |
| Command or tool surface | governed reads, Vitest, TypeScript check, git, governance gates, sixteen adversarial probes in a git-ignored scratch directory |
| Target paths | the three reviewed implementation paths, the work order, the paired baseline, the original worker return, and the R1 repair evidence, all read-only; this file is the sole write |
| Allowed scope source | operator dispatch of the RSPB-AI-T5-R1 independent reviewer role |
| Before status evidence | five uncommitted paths at execution base `2133f5cb9`; R1 repair evidence status `COMPLETE_PENDING_INDEPENDENT_REVIEW` |
| After status evidence | same five uncommitted paths, byte-identical; this new reviewer-owned review file added |
| Diff evidence | `git diff --name-status` and `git status --short` reproduced above, both before and after this review |
| Approval boundary | independent review and verdict only; no repair, edit, stage, commit, or push |
| Claim boundary | local hermetic verification of pure projection behavior only |
| Agent type | independent reviewer |
| Invocation ID | `rspb-ai-t5-r1-independent-review-20260816` |
| Expected manifest | exactly one new reviewer-owned file |
| Actual changed set | exactly one new reviewer-owned file |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename performed by this review |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: the R1 repair should close all eight
previously-found defects without introducing a new fail-open path, and its
own 27-test suite, while much stronger than the original worker's, might
still leave some adversarial angle (nested bounds, forged authority
literals, cross-binding forgery, genuine multi-item permutation, Proxy
references, secret-signal false positives on safe prose) unexercised.

Evidence Comparison: all eight original defects are independently confirmed
fixed by direct source inspection and dedicated reproduction, matching each
finding in the R1 repair evidence to a specific code location. Sixteen
additional adversarial probes beyond the repair's own suite, covering
sparse arrays, nested collection bounds, two categories of secret-signal
false-positive safe prose, two categories of forged-authority-literal
route/readiness lookalikes, cross-binding forgery, a Proxy-shaped optional
reference, three-way and three-item-permutation digest determinism, and a
combined STALE-plus-other-issue case, all passed. One informational,
non-blocking observation (`Array` subclass acceptance) was found and
determined to be correct behavior, not a defect.

Contradiction Or Gap Disposition: no contradiction between the repair
evidence's claims and this review's independent findings. No gap remained
open after the sixteen additional probes.

Claim Update: the repaired RSPB-AI-T5 state is independently verified
fail-closed, secret-safe, deterministic, and non-authority-granting.
Acceptance is recorded as `REVIEWER_ACCEPTED_PENDING_CLOSER`; only a
reviewer/closer may promote this to commit or closure.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private, uncommitted independent review pending
reviewer/closer action. No public sync or push is authorized by this
review.

## Claim Boundary

This review authorizes no commit, staging, push, revert, or stash of any
file; the worktree remains exactly as found at HEAD `2133f5cb9b0`. It does
not close RSPB-AI-T5 or RSPB-AI-T5-R1; closure remains a separate
reviewer/closer action. It does not authorize any router, transport,
executor, filesystem case export, acquisition execution, mutation,
credential access, network fetch, provider/live call, MCP/CLI activation,
public sync, deployment, or production-readiness claim. It does not certify
runtime behavior beyond the hermetic Vitest/TypeScript evidence and the
sixteen local adversarial probes reproduced above. It does not repair or
modify the reviewed implementation; the one informational observation
recorded above requires no corrective action and does not block acceptance.
