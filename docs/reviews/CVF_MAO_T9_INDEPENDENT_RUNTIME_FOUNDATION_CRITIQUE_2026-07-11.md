# CVF MAO-T9 Independent Runtime Foundation Critique

Memory class: FULL_RECORD

docType: review

Status: CRITIQUE_RECORDED

Date: 2026-07-11

Batch ID: MAO-T9

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_T9_INDEPENDENT_CRITIQUE_RECONCILIATION_AND_CLOSURE_2026-07-11.md`

executionBaseHead: `4dbfba72c`

## Purpose

Independently source-verify every material claim made across MAO-T0 through
T8 (source, tests, completion reviews) without treating prior completion
summaries as final authority. This packet records the critic's own
verification method and results, not a restatement of what the completion
reviews already say about themselves.

## Target / Source

Target: nine execution tranches (`T0`-`T8`) implementing
`docs/roadmaps/CVF_MULTI_AGENT_ORCHESTRATION_RUNTIME_FOUNDATION_ROADMAP_2026-07-11.md`.

Source re-read at this execution base:

- the roadmap itself (Work Plan And Dependencies, Acceptance Criteria,
  Negative And Fail Conditions, Roadmap-To-Work-Order Trace Matrix);
- all nine T0-T8 completion reviews under `docs/reviews/`;
- current source for every cited symbol: `task.graph.contract.ts`,
  `event.ledger.contract.ts`, `read.model.contract.ts`,
  `role.resolver.contract.ts` (control-plane package),
  `delegation.adapter.contract.ts`, `reviewer.isolation.contract.ts`,
  `dissent.revision.contract.ts`, `closer.interlock.contract.ts`,
  `lifecycle.controller.contract.ts`, `evidence.readout.contract.ts`,
  `representative.pilot.contract.ts`;
- `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_SCHEMA.json`
  and its companion contract document;
- the GC-051 corpus scan registry
  (`docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`).

## Scope / Methodology

For every T0-T8 completion review, the critic independently reran the
review's own claimed verification commands (focused Vitest per package,
TypeScript typecheck per package) from a clean execution base, rather than
accepting the review's reported pass counts as given. For claims a
completion review made about a specific source-code repair (e.g. "atomic
duplicate admission," "monotonic revision timestamps," "cross-graph
admission rejection"), the critic grepped and read the current source to
confirm the described code actually exists at the claimed location and
behaves as described, not only that a test with a matching name exists.
For structural claims (root-barrel non-wiring, file-size compliance, GC-051
registry coverage, JSON Schema validity), the critic ran the underlying
tool or governance gate directly rather than trusting a completion review's
summary sentence.

## Independent Verification Log

### T0 - Source Inventory, Architecture Decisions, And Schemas

| Claim | Independent verification | Result |
|---|---|---|
| Four reference/schema files exist under `docs/reference/multi_agent_orchestration/` | `ls docs/reference/multi_agent_orchestration/` | CONFIRMED: `CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md`, `CVF_MAO_RUNTIME_FOUNDATION_SCHEMA.json`, `CVF_MAO_T0_SOURCE_INVENTORY_AND_OVERLAP_DECISIONS.md`, `README.md` |
| Schema is valid Draft 2020-12 JSON | parsed `CVF_MAO_RUNTIME_FOUNDATION_SCHEMA.json` directly with `node -e "JSON.parse(...)"` | CONFIRMED: parses cleanly; `$schema` is literally `https://json-schema.org/draft/2020-12/schema` |
| Base-head wording defect (dispatch `f42195d20` vs actual session-sync child `209a9b4b3`) was corrected | read the T0 completion review's Reviewer Base-Head Correction section | CONFIRMED as a documented, resolved correction; no open discrepancy found in later tranches' base-head fields |

### T1 - Task Graph And State Contract

| Claim | Independent verification | Result |
|---|---|---|
| Serialized-overlap repair (`dependencyOrdersPair`) exists | grepped `task.graph.contract.ts` for `dependencyOrdersPair` and `OVERLAPPING_WRITE_SCOPE` | CONFIRMED at lines 232 and 337 of the current file; overlap is rejected only when the pair is not dependency-ordered |
| Focused suite is 39/39 | reran `npx vitest run --config vitest.config.ts tests/mao.task.graph.state.contract.test.ts` from `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION` | CONFIRMED: 39/39 PASS |
| `src/mao/` is not wired into the root execution-plane barrel | grepped `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/index.ts` for any `mao` reference | CONFIRMED: zero matches |
| GC-051 registry covers T1's module and test | inspected `CVF_CORPUS_SCAN_REGISTRY.json` for `mao-t1-task-graph-state-source-surfaces` | CONFIRMED: scopePaths cover `src/mao/` and the T1 test file |

### T2 - Risk-Based Role Resolver

| Claim | Independent verification | Result |
|---|---|---|
| Dispatch symbol drift (`MaoCompiledTaskGraph` -> `MaoTaskGraph`) was corrected | grepped the current T2 work order for `MaoTaskGraph`/`MaoCompiledTaskGraph` | CONFIRMED: current work order cites only `MaoTaskGraph`, the correct symbol |
| `admittedRoles`, `maxConcurrentRoles`, `riskLevel` bindings exist in the resolver | grepped `role.resolver.contract.ts` | CONFIRMED at lines 56, 139, 149, 300, 307, 327 (exact matches for admitted-role membership, concurrency-ceiling check, and risk-level aggregation) |
| Focused suite is 22/22 | reran `npx vitest run --config vitest.config.ts tests/mao.role.resolver.contract.test.ts` from `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION` | CONFIRMED: 22/22 PASS |
| Control-plane package typechecks clean | reran `npx tsc -p tsconfig.json --noEmit` from `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION` | CONFIRMED: clean exit, no errors |

### T3 - Provider-Neutral Delegation Adapter

| Claim | Independent verification | Result |
|---|---|---|
| Focused suite is 21/21 | reran `npx vitest run --config vitest.config.ts tests/mao.delegation.adapter.contract.test.ts` | CONFIRMED: 21/21 PASS |
| Fake/local only, no network/provider import | read full `delegation.adapter.contract.ts` import list | CONFIRMED: imports only `computeDeterministicHash` and local MAO-T1 symbols; no network or provider SDK import |

### T4 - Reviewer Isolation, Dissent, And Revision Loop

| Claim | Independent verification | Result |
|---|---|---|
| Revision sequencing is enforced (`expectedRevision` check) | grepped `dissent.revision.contract.ts` for `recordReviewInLedger`/`expectedRevision`/`non-sequential` | CONFIRMED at lines 259-267; a non-sequential `revisionNumber` is rejected |
| Focused suite is 78/78 | reran `npx vitest run --config vitest.config.ts tests/mao.reviewer.isolation.revision.contract.test.ts` | CONFIRMED: 78/78 PASS |

### T5 - Designated Closer And Commit/Session Interlock

| Claim | Independent verification | Result |
|---|---|---|
| Blank/empty closer and actor identities are rejected | grepped `closer.interlock.contract.ts` for `trim().length === 0` | CONFIRMED at lines 75, 90, 161; every identity-bearing check rejects empty/whitespace-only identity strings |
| Focused suite is 54/54 | reran `npx vitest run --config vitest.config.ts tests/mao.closer.interlock.contract.test.ts` | CONFIRMED: 54/54 PASS |

### T6 - Timeout, Heartbeat, Cancel, Retry, And Recovery

| Claim | Independent verification | Result |
|---|---|---|
| Focused suite is 58/58 | reran `npx vitest run --config vitest.config.ts tests/mao.lifecycle.controller.contract.test.ts` | CONFIRMED: 58/58 PASS |
| Atomic duplicate-claim protection exists (`claim()` single-call semantics) | read `createIdempotencyGuard` in `lifecycle.controller.contract.ts` | CONFIRMED: `claim(key)` checks-and-sets in one call; no split `seen()`+`record()` race remains in the current source |

### T7 - Evidence, Observability, And Operator Readout

| Claim | Independent verification | Result |
|---|---|---|
| Cross-graph admission is rejected (`TASK_GRAPH_ID_MISMATCH`) | read `evidence.readout.contract.ts` `MaoIngestEvidenceFailureReason` and `MaoEvidenceLedger.ingest` | CONFIRMED: `TASK_GRAPH_ID_MISMATCH` is a declared failure reason and `ingest` rejects any `taskGraphId` not matching the ledger's bound graph |
| Focused suite is 35/35 | reran `npx vitest run --config vitest.config.ts tests/mao.evidence.readout.contract.test.ts` | CONFIRMED: 35/35 PASS |
| Workspace milestone projection excludes every `INVOCATION` receipt | read `milestoneForReceiptKind` | CONFIRMED: the `INVOCATION` case returns `null` unconditionally |

### T8 - Representative End-To-End Pilot

This tranche received the most scrutiny because its completion review
reported the most consequential defect of the nine tranches: a worker
proof that was accepted by 24/24 passing tests but was, per the reviewer,
a **false freshness proof** (the worker's original test harness moved the
revision-review evaluation clock backward from `+999999ms` to `+2500ms`
without adding new evidence, which "regenerated" a fresh classification
from stale data rather than proving a real repair). This is exactly the
class of claim this critique must not accept on the reviewer's word alone.

| Claim | Independent verification | Result |
|---|---|---|
| Monotonic-timestamp guard exists in `runPilotChain` | read `representative.pilot.contract.ts` lines 377-386 | CONFIRMED: `revisedAtMs < firstReviewMs \|\| secondReviewMs < revisedAtMs` throws `"revision and second review timestamps must be monotonic"` before any regeneration occurs |
| A real new `OUTPUT` receipt is appended before regenerating the readout (not just a `generatedAt` change) | read lines 388-401 | CONFIRMED: `ledger.ingest({ ..., receiptKind: "OUTPUT", fields: { revision: "1", repair: "fresh-readout-regenerated" }, recordedAt: revisedGeneratedAt })` is called, and its `ok` result is checked, before `buildEvidenceReadout` is called again |
| A backward-time negative test exists and passes | grepped the test file for `monotonic`/`backward` | CONFIRMED: `"rejects a revision that moves the proof clock backwards"` exists and asserts the exact thrown message |
| Focused suite is 25/25 (not 24/24 as the original worker return claimed) | reran `npx vitest run --config vitest.config.ts tests/mao.representative.pilot.contract.test.ts` | CONFIRMED: 25/25 PASS |
| Budget-ceiling negative rejects "before any task executes," matching roadmap wording literally | read `runBudgetCeilingNegative` | CONFIRMED: it only calls `compilePilotGraph`, never any task-execution function; rejection is a compile-time-only path |

## Findings / Position

Nine tranches (T0-T8) were independently re-verified against current source,
not against completion-review prose. Every specific factual claim checked
above (source-code repair location, test count, structural boundary) was
confirmed accurate at this execution base. One material accuracy gap was
found that survived through the T8 closure and remains open in the T8
baseline/work order artifacts (not the pilot source code itself):

### Finding T9-F1: `PILOT_MAX_CONCURRENT_ROLES` is cited as a directly-verified `LITERAL_INVARIANT` symbol but is not exported

The T8 GC-018 baseline
(`docs/baselines/CVF_GC018_MAO_T8_REPRESENTATIVE_END_TO_END_PILOT_2026-07-11.md`)
and work order
(`docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_T8_REPRESENTATIVE_END_TO_END_PILOT_2026-07-11.md`)
Source Verification Blocks both cite `PILOT_MAX_CONCURRENT_ROLES` in
`task.graph.contract.ts` with claim type `LITERAL_INVARIANT` and
disposition `ACCEPT`. Independent verification confirms the constant
exists (line 111, value `3`) but it is a private, non-exported
module-scope `const`. A `LITERAL_INVARIANT` disposition of `ACCEPT`
implies the cited symbol is directly usable/verifiable as named; a
private constant cannot be imported by name from another module, which
the T8 worker return itself already disclosed as its own Finding 2 (the
pilot harness verifies the ceiling behaviorally through
`compileTaskGraph`'s rejection path instead of importing the constant).
The dispatch-time Source Verification claim was technically imprecise
(it should have been `EXISTS` with a note on non-export, not
`LITERAL_INVARIANT` implying direct symbol access), though the
downstream implementation correctly worked around the gap and no
behavioral defect resulted.

Independent source location: `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts:111`
(`const PILOT_MAX_CONCURRENT_ROLES = 3;` - no `export` keyword).

### No other material findings

No other source-code defect, test-count discrepancy, undisclosed scope
mutation (root barrel, workspace state, session state, public-sync, ASC
aggregate, gap registry), or contradicted completion-review claim was
found across T0-T8. All nine completion reviews' pass counts, repair
descriptions, and structural-boundary claims were independently
reproduced.

## Risk / Corrective Action

Finding T9-F1 does not require any source-code change: the pilot harness
already verifies the ceiling correctly via behavioral rejection. The
corrective action is a documentation-accuracy note for future GC-018/work-
order Source Verification Blocks: a private (non-exported) constant should
be cited with claim type `EXISTS` plus an explicit non-export note, not
`LITERAL_INVARIANT`, since `LITERAL_INVARIANT` in this repository's
convention (see other T0-T8 Source Verification Block rows) is otherwise
used for symbols a citing module can directly reference.

No runtime, provider, public-sync, ASC aggregate, or gap-registry risk is
introduced by this finding; it is a source-verification-table precision
gap only.

## Decision / Recommendation / Disposition

Disposition: CRITIQUE_RECORDED. One finding (T9-F1) is classified CALIBRATE
in the paired reconciliation candidate packet. No other finding rises above
the threshold of a material, source-backed defect. Recommend the reviewer/
closer accept T0-T8 as source-verified and proceed to roadmap closure
diff review using this critique as independent confirmation, not as a new
blocking condition.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`multi-agent orchestration runtime`,
role=`worker`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_roadmap_closure_freshness.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | review-docType heading groups (target/source, scope/methodology, findings/position, risk/corrective action, decision/recommendation/disposition); full Agent Operation Trace Block label set; Epistemic Process Block four subsections; `ALLOWED_DISPOSITIONS` enum in the public export checker |
| gateRunPurpose | confirmation ahead of worker-return fast gate |
| claimBoundary | independent critique record only; no roadmap, runtime, session, public-sync, ASC aggregate, or gap-registry mutation |

## Epistemic Process Block

### Expected Result / Prediction

Independent re-verification of nine already-reviewer-accepted tranches
would find the completion reviews' claims largely accurate (since each was
already independently reviewed once), with a small chance of at least one
residual documentation-precision gap given the volume of Source
Verification Block rows across nine tranches.

### Evidence Comparison

Confirmed: every rerun test suite matched its claimed pass count exactly
(39, 22, 21, 78, 54, 58, 35, 25 for T1-T8 respectively), and every claimed
source-code repair was found present and behaviorally correct at its cited
location. One documentation-precision gap (T9-F1) was found, matching the
predicted "small residual gap" expectation rather than contradicting the
overall accuracy prediction.

### Contradiction Or Gap Disposition

No contradiction of any completion review's substantive technical claim was
found. The one gap found (T9-F1) is a source-verification-table claim-type
precision issue, not a runtime or test-result contradiction, and does not
change the accepted status of any T0-T8 tranche.

### Claim Update

T0-T8 are independently confirmed source-accurate at this execution base,
with one calibrated documentation-precision finding. This critique does not
itself claim runtime, provider, public, or production readiness for MAO;
it claims only that the nine tranches' technical evidence is accurate as
reported.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | independent critic worker |
| Provider or surface | private workspace |
| Session or invocation | MAO-T9 independent critique 2026-07-11 |
| Working directory | repository root and per-package subdirectories for test/typecheck reruns |
| Command or tool surface | Read, Grep, Bash (git, npx vitest, npx tsc, node -e, governance gates) |
| Target paths | this critique packet |
| Allowed scope source | MAO-T9 work order Work-Order Fulfillment Manifest |
| Before status evidence | clean execution HEAD `4dbfba72c` |
| After status evidence | nine tranches independently re-verified; one calibrated finding recorded |
| Diff evidence | `git diff --name-status` |
| Approval boundary | T9 independent critique only; no roadmap/runtime/session/public/ASC/gap mutation |
| Claim boundary | independent source-verification record only |
| Agent type | independent critic worker |
| Invocation ID | `mao-t9-independent-critique-2026-07-11` |
| Expected manifest | this critique packet |
| Actual changed set | this critique packet |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | NOT_APPLICABLE_WITH_REASON: no external input |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | reviewer/closer |
| Disposition | no absorption |
| Claim boundary | CVF source only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

This packet records an independent source-verification critique only. It
does not itself close the roadmap, mutate runtime source, session state,
public-sync, the ASC aggregate, or the gap registry, and does not claim
provider, live, UI, or production readiness. Finding classification,
repair authorization, and roadmap closure remain reviewer/closer-owned per
the work order's Reviewer Closure Conversion block.
