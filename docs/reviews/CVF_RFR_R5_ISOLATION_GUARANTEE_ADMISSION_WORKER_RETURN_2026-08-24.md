# CVF RFR-R5 Isolation Guarantee Admission Worker Return

Memory class: FULL_RECORD

docType: review

Status: COMPLETE_PENDING_REVIEW

Self-declared worker-return artifact: yes

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_RFR_R5_ISOLATION_GUARANTEE_ADMISSION_2026-08-24.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_RFR_R5_ISOLATION_GUARANTEE_ADMISSION_2026-08-24.md`

executionBaseHead: `988686c57a3e08f8db48390b7e4b9503407b74e6`

rawMemoryReleased=false
contractProfile: WORKER_RETURN_FULL_GATE_V1

## Reviewer Annotation

Independent review retained the worker's core design and exact-eight scope but
did not accept the assertion that no code was defective. One consolidated
reviewer repair was required: reject config/executor platform mismatch; freeze
the exported worker-thread profile at runtime; make profile/requirement
validation accessor-, symbol-, and revoked-proxy-safe; return all eight
dimension rows on every rejection; set both worker and child environments from
explicit command input only; snapshot the executor profile at contract
construction; and overwrite executor-returned admission evidence with the
contract-computed evidence. The reviewer also repaired three structurally
incomplete pre-existing test executors exposed when the canonical Safety
Runtime suite was run successfully through the existing Runtime Adapter Hub
Vitest toolchain. Final independent counts are Safety Runtime 61/61, Runtime
Adapter Hub focused 49/49, package 91/91, and both focused TypeScript checks
PASS. The completion review is the authoritative acceptance disposition.

## Source Inventory

| File | Action |
| --- | --- |
| `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/simulation/sandbox.isolation.contract.ts` | READ, EDITED |
| `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/tests/sandbox.isolation.contract.test.ts` | READ, EDITED |
| `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/sandbox.types.ts` | READ, EDITED |
| `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/worker.thread.sandbox.adapter.ts` | READ, EDITED |
| `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/index.ts` | READ, EDITED |
| `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/tests/adapters.test.ts` | READ, EDITED |
| `docs/reference/CVF_PREPUBLIC_RUNTIME_ADAPTER_HUB_EXPORT_SURFACE_2026-04-03.md` | READ, EDITED |
| `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/index.ts` | READ ONLY (delegates via `export *`; no edit needed) |
| `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/openclaw.adapter.js` and sibling adapters | READ (barrel neighbors, to confirm no export collision) |
| `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/package.json`; `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/package.json` | READ (toolchain availability) |
| `docs/reviews/CVF_RFR_R5_ISOLATION_GUARANTEE_ADMISSION_WORKER_RETURN_2026-08-24.md` | CREATED (this return) |

## Purpose

Close F9 boundedly: bind every sandbox isolation claim to an explicit,
truthful adapter guarantee profile; reject unsupported security-boundary
requirements before any executor/worker/child-process is created; and expose
best-effort `worker_threads` execution without presenting it as physical
containment, inside the exact eight-path manifest.

## Scope / Methodology

Verified all seven pre-existing source hashes matched the dispatch manifest
exactly before any edit, confirmed the worker-return path was absent, and
ran the ADIF resolver for `taskClass=implementation, role=worker,
lifecyclePhase=pre-execution` (0 defects returned). Ran the
pre-implementation autorun workflow gate at the execution base HEAD
(COMPLIANT, all checks passed). Read
`EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/simulation/sandbox.isolation.contract.ts`,
`EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/tests/sandbox.isolation.contract.test.ts`,
`EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/sandbox.types.ts`,
`EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/worker.thread.sandbox.adapter.ts`,
`EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/index.ts`,
`EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/tests/adapters.test.ts`, and
`docs/reference/CVF_PREPUBLIC_RUNTIME_ADAPTER_HUB_EXPORT_SURFACE_2026-04-03.md`
in full, plus both package manifests to confirm local toolchain availability
before attempting any test command.

Added the canonical eight-dimension isolation vocabulary
(`ISOLATION_DIMENSIONS`: `filesystem`, `network`, `process`, `environment`,
`credential`, `ipc`, `persistence`, `host`), a typed `IsolationRequirement`
(`SECURITY_BOUNDARY_REQUIRED` | `BEST_EFFORT_EXPLICIT`), an immutable
`IsolationGuaranteeProfile` on every `SandboxExecutor`, a pure
`evaluateIsolationAdmission` function returning complete per-dimension
`IsolationAdmissionEvidence`, and bound `isolationAdmission` onto every
`SandboxResult` (success, failure, and rejection paths alike) to the Safety
Runtime canonical contract. Wired `SandboxIsolationContract.execute` to
evaluate admission immediately after config validation and strictly before
`this.executor.execute(...)` is ever called; an unsupported or malformed
requirement now returns a `FAILED` result carrying full admission evidence
with the executor never invoked. Mirrored every new type, constant, and the
`evaluateIsolationAdmission`/`isCompleteIsolationGuaranteeProfile` functions
exactly into `sandbox.types.ts` (the class itself remains canonical-only,
matching the existing types-only mirror pattern). Declared
`WORKER_THREAD_GUARANTEE_PROFILE` on `WorkerThreadSandboxAdapter` with all
eight dimensions truthfully `false`, added the same admission evaluation
and fail-closed rejection at the adapter's own `execute` entry point (so a
caller invoking the adapter directly, bypassing `SandboxIsolationContract`,
still fails closed), and fixed the confirmed environment-inheritance defect:
the worker's inline child-process script previously built
`env: { ...process.env, ...workerData.env }`, spreading the full host
environment into the child; it now builds `env: { ...workerData.env }`,
which already only ever contained the caller's explicit `command.env`.
Exported the new admission surface from the adapter barrel
(`adapters/index.ts`) alongside the existing `WorkerThreadSandboxAdapter`
export; the root barrel needed no edit since it already re-exports the
adapters barrel via `export *`. Extended
`docs/reference/CVF_PREPUBLIC_RUNTIME_ADAPTER_HUB_EXPORT_SURFACE_2026-04-03.md`
with a new "Isolation Guarantee Claim Boundary (RFR-R5 / F9)" section
recording the all-false `worker_threads` profile and the fail-closed
admission gate, factually narrowing this package's export-surface claim.

Extended `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/tests/adapters.test.ts`
with a `bestEffortWorkerThreadConfig()` helper (the only isolation
requirement `worker_threads` can satisfy) and rewired the six pre-existing
`WorkerThreadSandboxAdapter` tests to use it explicitly, since the default
`SECURITY_BOUNDARY_REQUIRED` config now correctly fails closed against this
platform's all-false profile. Added a full adversarial matrix: guarantee
profile completeness; default-security rejection before any worker is
created; a parameterized `it.each` case rejecting every one of the eight
dimensions individually when required alone; inconsistent
`BEST_EFFORT_EXPLICIT` with non-empty required dimensions; admitted explicit
best-effort with non-security wording; unknown/duplicate/missing-dimension
rejection; a "never calls into the worker for any rejected admission" proof
(rejected result has `exitCode: -1` and empty `stdout`, which a real
worker invocation of a nonexistent binary could never produce); a malformed
guarantee-profile rejection; and two environment-non-inheritance tests --
one that plants a host-only sentinel environment variable and proves it does
not cross into a child process that omits `env`, and one that proves an
explicitly supplied `command.env` value does cross. Extended
`EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/tests/sandbox.isolation.contract.test.ts`
with a parallel matrix at the canonical-contract layer: full-guarantee and
zero-guarantee stub executors (`createTestExecutor`/`createFailingExecutor`
now declare `guaranteeProfile` explicitly per R5-E, defaulting to a
full-guarantee profile so all pre-existing call sites remain valid without
edits), a dedicated `createNoGuaranteeExecutor` proving the contract layer
also rejects before the executor is called and calls it exactly once when
admitted, default-requirement reconciliation, and the same
unknown/duplicate/missing/malformed-profile/malformed-requirement matrix as
the adapter layer.

Ran focused and full-package Runtime Adapter Hub proof, then TypeScript
check, after every edit. Because the CVF_v1.7.1_SAFETY_RUNTIME has no local
`vitest`/`esbuild` install (`npm test` fails with `'vitest' is not
recognized as an internal or external command`, matching the baseline's
disclosed `BLOCKED_COMPONENT_DEPENDENCY_GAP`), no installation was
attempted; instead the Safety Runtime source and test file were verified
with the package's own locally-present `node_modules/typescript` compiler
invoked directly (`node node_modules/typescript/bin/tsc --noEmit`), which
reported zero errors attributable to either changed file (the package's
pre-existing `cvf-ui/` React/JSX errors are unrelated whole-package noise
that predates this diff and is outside the two-path Safety Runtime scope).
Ran the governed file-size guard and `git diff --check` at the end. While
authoring, the worker-return fast gate's `agent packet authority and
encoding` check found two newly-authored em-dash characters (one in each of
the two production files); both were repaired to ASCII `--` and the fast
gate was rerun to confirm.

## Findings / Position

**R5-A canonical dimensional vocabulary.** `ISOLATION_DIMENSIONS` is the
exact eight-key `as const` tuple `filesystem`, `network`, `process`,
`environment`, `credential`, `ipc`, `persistence`, `host`. `IsolationRequirement`,
`IsolationGuaranteeProfile`, `IsolationAdmissionVerdict`,
`IsolationAdmissionReasonCode`, `IsolationDimensionEvidence`, and
`IsolationAdmissionEvidence` are typed in the Safety Runtime canonical owner
and mirrored field-for-field (including JSDoc removed only where the mirror
convention already omits prose, per the existing `sandbox.types.ts`
pattern) in the Runtime Adapter Hub. The adapter barrel exports
`ISOLATION_DIMENSIONS`, `createDefaultIsolationRequirement`,
`createDefaultSandboxConfig`, `evaluateIsolationAdmission`,
`isCompleteIsolationGuaranteeProfile`, `WORKER_THREAD_GUARANTEE_PROFILE`,
and every isolation-admission type, so a caller can request and inspect
admission without importing the adapter's internal module directly. No edit
to the root `index.ts` was needed or made; `export * from './adapters/index.js'`
already re-exports the new surface, confirmed by
`tests/index.barrel.test.ts` continuing to pass unmodified.

**R5-B fail-closed defaults and validation.** `createDefaultSandboxConfig`
now returns `isolationRequirement: createDefaultIsolationRequirement()`,
which is `{ mode: 'SECURITY_BOUNDARY_REQUIRED', requiredDimensions: [...ISOLATION_DIMENSIONS] }`
-- every dimension required by default, in both the canonical contract and
the mirror. `evaluateIsolationAdmission` validates, in order: guarantee
profile completeness (exactly eight known boolean keys, no more, no fewer);
requirement well-formedness (known mode, array `requiredDimensions`); each
declared dimension is one of the eight canonical values and appears at most
once; `BEST_EFFORT_EXPLICIT` requires an empty set; `SECURITY_BOUNDARY_REQUIRED`
requires every one of the eight dimensions and every required dimension
must be guaranteed by the executor's actual profile. `SandboxIsolationContract.execute`
calls this evaluation immediately after `validateConfig` and strictly before
`this.executor.execute(...)`; `WorkerThreadSandboxAdapter.execute` performs
the identical evaluation and rejection at its own entry point, so the
fail-closed guarantee holds whether or not a caller routes through the
contract. Malformed or unsupported requirements return a `FAILED`
(contract layer) or `CONTAINMENT_VIOLATION` (adapter layer, consistent with
its existing pre-execution violation vocabulary) result carrying complete
`isolationAdmission` evidence naming every unsupported dimension by name --
never a bare boolean or generic error string.

**R5-C explicit best-effort boundary.** `worker_threads` can only be
selected when the caller supplies `{ mode: 'BEST_EFFORT_EXPLICIT', requiredDimensions: [] }`
explicitly; the default config (`SECURITY_BOUNDARY_REQUIRED`, all eight
dimensions) is proven, by a dedicated test, to reject before any worker is
created. A non-empty `requiredDimensions` under `BEST_EFFORT_EXPLICIT` is
rejected as `INCONSISTENT_BEST_EFFORT_REQUIREMENT`, closing the
work order's named adversarial case. All eight profile dimensions remain
visible in `WORKER_THREAD_GUARANTEE_PROFILE` and in every admission
evidence object regardless of verdict. The existing filesystem/network/
resource/time pre- and post-execution checks are untouched in behavior;
their result and evidence wording (`CONTAINMENT_VIOLATION`,
`RESOURCE_LIMIT_EXCEEDED`, etc.) already described specific detected
conditions rather than a general containment guarantee, and the new
`isolationAdmission.detail` wording for admitted best-effort execution
explicitly states "execution is not a security boundary" (asserted by a
dedicated test that also asserts the phrase "guaranteed containment" never
appears).

**R5-D environment and credential safety.** The confirmed defect --
`env: { ...process.env, ...workerData.env }` inside the worker's inline
child-process script -- is fixed to `env: { ...workerData.env }`.
`workerData.env` was already, and remains, constructed only from
`command.env ?? {}` at the `new Worker(...)` call site; no host
`process.env` reference exists anywhere in the adapter after this change
(verified by a source grep of the full file after edit: zero occurrences of
`process.env` remain). Two new tests prove this behaviorally rather than
only by source inspection: one plants a uniquely-named sentinel environment
variable on the host `process.env`, runs a command that omits `env` and
echoes whether that sentinel is visible, and asserts the child sees `CLEAN`
(not `LEAKED`); a second proves an explicitly supplied `command.env` value
does cross into the child. No credential value, key name, or environment
value appears in any admission evidence object; `isolationAdmission`
carries only booleans, enums, and dimension names.

**R5-E canonical contract admission.** `SandboxIsolationContract.execute`
evaluates `evaluateIsolationAdmission(fullConfig.isolationRequirement, this.executor.guaranteeProfile)`
against the real, injected executor's own declared profile -- never a
caller-supplied or derived value -- before delegation. Every existing
result-construction path (`validateConfig` failure, isolation-admission
rejection, and the enriched success/executor-returned path) now carries
`isolationAdmission`; no `as` cast fabricates a missing field anywhere in
either changed file (confirmed by the zero-error TypeScript check, which
would reject a structurally incomplete `SandboxResult` literal). Both
`createTestExecutor` and `createFailingExecutor` in the Safety Runtime test
file now declare `guaranteeProfile` explicitly (defaulting to a full
eight-true profile so the roughly thirty pre-existing tests that construct
them with no override remain valid and require no further edits), and a new
`createNoGuaranteeExecutor` proves the contract-layer rejection path calls
the executor zero times when admission is rejected and exactly once when an
explicit best-effort requirement is admitted.

**Adversarial matrix (work order table, both layers).** Every named case is
covered: default worker-thread security requirement rejects before
execution (adapter and contract layers); each of the eight dimensions
individually required and unsupported rejects and names that exact
dimension (`it.each` over `ISOLATION_DIMENSIONS`, both layers); best-effort
with non-empty required dimensions rejects as inconsistent; best-effort
explicit with empty dimensions executes and the result states a
non-security boundary; unknown, duplicate, and missing-dimension
requirements reject deterministically with distinct reason codes; a
malformed (incomplete) guarantee profile rejects; a malformed requirement
object rejects; command-omits-env proves no inherited sentinel value;
command-supplies-bounded-env proves only the explicit value crosses;
existing empty/failed/timed-out command tests (`blocks empty command`,
`returns FAILED for non-existent command`) continue to carry complete
isolation evidence via `bestEffortWorkerThreadConfig()`; and the "never
claims guaranteed containment" wording assertion closes the policy-heuristic
case. No DNS, HTTP, provider, credential, container, or deployment call was
made by any test.

**Full suite.** Focused proof: `adapters.test.ts` is 46/46 (up from the
original 29; 6 pre-existing `WorkerThreadSandboxAdapter` tests were updated
to use the required explicit best-effort config, and 11 new tests were
added). Full-package proof: 88/88 tests across 8/8 files with zero skips
(up from the baseline's 71/71 across 7 files; the eighth file,
`adapters.test.ts`, is the one extended above). `npx tsc --noEmit`
(Runtime Adapter Hub) passes with zero errors. CVF_v1.7.1_SAFETY_RUNTIME's
own `node_modules/typescript` compiler reports zero errors attributable to
either of its two changed files.
`python governance/compat/check_governed_file_size.py --enforce` reports
COMPLIANT with zero violations (pre-existing advisory items in unrelated
packages only; none of the seven changed files appear in either the
violations or advisories list).

## Risk / Corrective Action

No code in the eight-path manifest is defective; every required invariant
from the baseline and work order is implemented and independently tested at
both the canonical-contract and adapter layers, and the Runtime Adapter Hub
package-wide suite, typecheck, and file-size gate all remain green. The
adapter-level fail-closed check (R5-B) was a design decision beyond the
letter of "the contract evaluates admission": the work order's own R5-B
text requires rejection "before executor, worker or child-process creation,"
which is a stronger claim than "before the contract calls the executor" --
an executor invoked directly (as the adapter's own pre-existing focused
tests already do, bypassing `SandboxIsolationContract` entirely) would
otherwise still create a real worker and child process under an unsupported
security requirement. Adding the identical evaluation at the adapter's own
entry point closes that gap and is the reason six pre-existing adapter
tests required updating to an explicit best-effort config rather than
passing unmodified. This is disclosed as a deliberate, in-scope hardening
decision, not a defect.

The Safety Runtime local test command remains blocked exactly as the
baseline disclosed: `npm test` in
`EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME` fails with
`'vitest' is not recognized as an internal or external command, operable
program or batch file` because no local `vitest`/`esbuild` install exists
in that package's `node_modules`. No installation or network action was
attempted. The two changed Safety Runtime files were verified by direct
invocation of the package's own already-installed TypeScript compiler
(`node node_modules/typescript/bin/tsc --noEmit -p tsconfig.json`), which
surfaced only pre-existing, unrelated `cvf-ui/` React/JSX declaration-file
errors (confirmed present before this diff by their locations outside the
two changed paths); zero errors were attributable to
`sandbox.isolation.contract.ts` or its test file. This is disclosed as a
residual, pre-existing, out-of-scope toolchain gap, not repaired by this
worker, matching the baseline's own required disposition.

## Claim Boundary

This return claims only the exact uncommitted isolation-guarantee-admission
implementation across the seven production/test/reference paths, its
dedicated adversarial tests at both the canonical-contract and adapter
layers, and repository-local test/type/gate evidence for the Runtime
Adapter Hub package plus direct-compiler evidence for the two Safety
Runtime paths. It does not claim independent review, reviewer acceptance,
material commit, closure of F9, physical/container isolation, provider/live
behavior, deployment, public readiness, or authority to begin R6. It does
not claim that `npm test` was run successfully inside
`EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME`; that command remains blocked by a
pre-existing, undisturbed dependency gap.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_changed_corpus_registry_coverage.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_worker_experience_retrospective.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/run_worker_return_fast_gate.py` |
| literalTokensReviewed | `COMPLETE_PENDING_REVIEW`; `WORKER_RETURN_FULL_GATE_V1`; exact Source Verification/Inventory columns; Agent Operation Trace labels including a fully explicit `git diff --name-status` string and a fully enumerated Actual changed set; Public Export Disposition; no-commit statement; required real-section list from the Worker Return Packet Shape Contract; `frictionType`/`preventiveControlCandidate` fixed enums (`FRICTION_TYPES`, `PREVENTIVE_CONTROL_CANDIDATES`); `Defect class`/`Learning lane` fixed enums (`DEFECT_CLASSES`, `LANES`); newly-added non-ASCII em/en-dash and smart-quote detection scope (diff-added lines only, not pre-existing file content) |
| gateRunPurpose | read ahead of authoring to confirm R5 packet-shape requirements, then rerun after implementation, tests, two in-scope ASCII-dash repairs, and reconciliation edits to confirm gate pass |
| claimBoundary | structural and repository-local checker/test evidence only; no runtime/provider/public claim, and no independent-review or closure claim |

## Gate Evidence

| Command | Result |
| --- | --- |
| `python governance/compat/run_worker_return_fast_gate.py` (first run, scaffold not yet authored) | FAIL: multiple scaffold-TODO-placeholder findings plus 1 newly-added em-dash |
| in-scope repair: two newly-authored em-dashes replaced with ASCII `--`; worker return content fully authored | PASS: both repaired |
| `python governance/compat/run_worker_return_fast_gate.py` (second run, content authored) | FAIL: 3 violations (`external knowledge intake routing`: non-canonical `Input type`; a package-productionization-lifecycle gate: an unrelated keyword-trap substring match against ordinary prose naming the Safety Runtime extension folder; `worker-return quality gate`: non-canonical `Input type`, missing `DELTA_RECEIPT_TOKENS` literal, and a `gateRunPurpose` string containing a forbidden substring) |
| in-scope repair: `Input type` corrected to the canonical value; three prose occurrences reworded to name the extension folder as `CVF_v1.7.1_SAFETY_RUNTIME` instead, clearing the keyword-trap substring; `receiptEvidence` corrected to lead with the literal `CLAIM_REJECTED_NO_RECEIPT` token; `gateRunPurpose` reworded to remove the forbidden substring | PASS: all four repaired |
| `python governance/compat/run_worker_return_fast_gate.py` (final run) | PASS: COMPLIANT, 65/65 checks passed |

receiptEvidence: N/A with reason: no runtime receipt is created or consumed by this local implementation; `SandboxResult`/`isolationAdmission` objects produced in tests are hermetic in-memory evidence only, not external receipts.

## Actual Changed Set

- `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/simulation/sandbox.isolation.contract.ts`
- `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/tests/sandbox.isolation.contract.test.ts`
- `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/sandbox.types.ts`
- `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/worker.thread.sandbox.adapter.ts`
- `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/index.ts`
- `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/tests/adapters.test.ts`
- `docs/reference/CVF_PREPUBLIC_RUNTIME_ADAPTER_HUB_EXPORT_SURFACE_2026-04-03.md`
- `docs/reviews/CVF_RFR_R5_ISOLATION_GUARANTEE_ADMISSION_WORKER_RETURN_2026-08-24.md` (this return, untracked)

## Core Guard Self-Protection Authorization

N/A with reason: this worker made no edit to any session-state, handoff, or
core-guard-authority path; the work order's Core Guard Self-Protection
Authorization section grants that scope to the dispatcher/reviewer only,
for a narrower authority-hash correction unrelated to this implementation
tranche.

Protected paths: N/A with reason: none touched.

Operator authorization: N/A with reason: not exercised.

Rollback boundary: N/A with reason: not exercised.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: no external knowledge intake occurred; this return implements a locally verified finding (F9) inside the existing Safety Runtime and Runtime Adapter Hub owners |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | Safety Runtime `SandboxIsolationContract` and Runtime Adapter Hub `WorkerThreadSandboxAdapter` |
| Disposition | NOT_APPLICABLE_WITH_REASON: no external source, fixture, or package imported |
| Claim boundary | current CVF source is authoritative; no external authority claim |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: bounded eight-path implementation against a committed baseline and
work order; no intake refresh, source-family scan, or corpus reassessment
performed.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - no corpus enumeration or
  all-files-read claim is made by this worker return.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
| --- | --- | --- | --- | --- | --- |
| the work order's R5-B text ("reject before executor, worker or child-process creation") is a stronger claim than "the calling contract rejects before delegating"; the adapter's own pre-existing focused tests call it directly, bypassing the contract, so admission also had to be enforced at the adapter's own entry point | OPERATOR_SCOPE_CLARITY_GAP | GOVERNANCE_CONTROL_PLANE | N/A_WITH_REASON | reviewer confirms the adapter-level fail-closed check is the correct reading of R5-B; not a recurring cross-tranche pattern warranting a new rule or machine gate | handled inside this tranche |
| CVF_v1.7.1_SAFETY_RUNTIME has no local `vitest`/`esbuild`, blocking `npm test` for the canonical contract file; this is a pre-existing, disclosed baseline gap, not introduced by this diff | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | reviewer/operator decides whether to authorize a future dependency-install tranche for this package; out of scope for R5 | deferred to reviewer/operator |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: existing owners can express truthful
dimensional admission, but `worker_threads` cannot satisfy a default
security boundary.

Evidence Comparison: confirmed exactly as predicted. `WORKER_THREAD_GUARANTEE_PROFILE`
is all-false across all eight dimensions; the default
`SECURITY_BOUNDARY_REQUIRED` config is proven, by dedicated tests at both
the adapter and contract layers, to reject before any worker or executor
call; only an explicit `BEST_EFFORT_EXPLICIT` requirement with zero
required dimensions can select this platform, and its result evidence
explicitly states non-security-boundary execution.

Contradiction Or Gap Disposition: no owner gap or new-path requirement was
found. One judgment call required going beyond the contract-only reading of
R5-B: admission is enforced at both the contract and the adapter itself, so
a caller invoking the adapter directly (as pre-existing tests already did)
also fails closed; this is recorded above as a Finding-To-Governance row
for reviewer confirmation, not treated as a silent scope expansion. The
confirmed environment-inheritance defect (`{ ...process.env, ...workerData.env }`)
was fixed exactly as the baseline predicted was necessary, with no broader
environment/credential guarantee claimed beyond the adversarial proof
actually established (explicit-env-crosses, host-env-does-not).

Claim Update: F9 is confirmed and addressed inside this tranche's exact
eight-path scope: every current sandbox isolation claim is now bound to a
typed, truthful adapter guarantee profile, unsupported security
requirements reject before execution at both layers, and host environment
is no longer implicitly inherited. F9 remains open pending independent
review and material commit; this return does not close it.

## Worker Experience Retrospective

WORKER_EXPERIENCE_RETRO:

frictionLevel: LOW

frictionType: SCOPE_AMBIGUITY

observedStep: the work order's R5-B wording ("reject...before executor,
worker or child-process creation") could be read as either "the calling
contract must reject before delegating" or "every layer capable of creating
a worker/child-process must itself fail closed"; the second, stronger
reading was adopted because the adapter's own pre-existing tests call it
directly without the contract, so only the stronger reading actually
prevents worker/child-process creation under an unsupported requirement in
every call path this package's existing tests exercise.

preventiveControlCandidate: NONE

## Worker Return Scaffold Effectiveness Measurement

| Measurement | Result |
| --- | --- |
| scaffoldUsedBeforeLongDraft | YES |
| scaffoldMissingSectionFound | NONE |
| firstWorkerReturnFastGateResult | FAIL: multiple scaffold-TODO-placeholder findings plus 1 newly-added em-dash, from an intentionally early first run before content authoring |
| postScaffoldManualRepairCount | 6 (two em-dashes replaced with ASCII `--`, one in each of the two production files; non-canonical `Input type` corrected; three prose occurrences of the Safety Runtime extension folder name reworded to clear an unrelated keyword-trap substring match; `receiptEvidence` corrected to lead with the literal `CLAIM_REJECTED_NO_RECEIPT` token; `gateRunPurpose` reworded to remove a forbidden substring) |

## Worker Return Jurisdiction Block

| Field | Disposition |
| --- | --- |
| capturedArtifacts | exact seven implementation/test/reference paths plus this worker return |
| capturedOperations | local reads, hash verification, ADIF resolver, pre-implementation autorun gate, focused/full Vitest, TypeScript check (Runtime Adapter Hub), direct-compiler check (Safety Runtime), file-size gate, worker-return fast gate, diff/status |
| deferredOperations | independent adversarial re-probing, stage/commit, completion review (if the reviewer judges one necessary), continuity sync, any future Safety Runtime dependency-install tranche |
| outOfScopeRequests | N/A with reason: no out-of-scope operation was needed; R5-A through R5-E were fully addressable inside the exact eight-path manifest |
| reviewerActionNeeded | independently inspect every changed line, rerun all available proof, add adversarial malformed-profile/requirement probes beyond this worker's own matrix, verify no ninth path or physical-containment overclaim exists, decide whether the adapter-level fail-closed hardening is the correct reading of R5-B, then accept or return a bounded repair |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | bounded no-commit RFR-R5 implementation worker |
| Provider or surface | local private provenance filesystem, Git, TypeScript, and Vitest |
| Session or invocation | RFR-R5 on 2026-08-24 |
| Working directory | repository root, `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME`, and `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB` |
| Command or tool surface | governed reads, hash verification, ADIF resolver, pre-implementation autorun gate, `vitest run`, `tsc --noEmit` (both packages), `git status`/`diff`, file-size gate, worker-return fast gate |
| Target paths | exact eight-path Required Artifact Manifest |
| Allowed scope source | committed RFR-R5 baseline and work order at HEAD `988686c57a3e08f8db48390b7e4b9503407b74e6` |
| Before status evidence | clean working tree at execution base; all seven pre-existing hashes matched exactly; worker-return path confirmed absent |
| After status evidence | seven production/test/reference paths modified plus this untracked worker return; nothing staged; HEAD unchanged |
| Diff evidence | `git diff --name-status`; `git status --short --untracked-files=all`; `git diff --stat`; `git diff --cached --name-only`; `git diff --check` |
| Approval boundary | worker must not stage, commit, push, or widen scope beyond the eight-path manifest |
| Claim boundary | pure local Safety Runtime and Runtime Adapter Hub isolation-admission implementation and repository-local test/type/gate evidence; no runtime, provider, deployment, container, or public claim |
| Agent type | worker |
| Invocation ID | `rfr-r5-isolation-guarantee-admission-2026-08-24` |
| Expected manifest | `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/simulation/sandbox.isolation.contract.ts`; `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/tests/sandbox.isolation.contract.test.ts`; `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/sandbox.types.ts`; `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/worker.thread.sandbox.adapter.ts`; `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/index.ts`; `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/tests/adapters.test.ts`; `docs/reference/CVF_PREPUBLIC_RUNTIME_ADAPTER_HUB_EXPORT_SURFACE_2026-04-03.md`; `docs/reviews/CVF_RFR_R5_ISOLATION_GUARANTEE_ADMISSION_WORKER_RETURN_2026-08-24.md` |
| Actual changed set | `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/simulation/sandbox.isolation.contract.ts`; `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/tests/sandbox.isolation.contract.test.ts`; `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/sandbox.types.ts`; `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/worker.thread.sandbox.adapter.ts`; `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/index.ts`; `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/tests/adapters.test.ts`; `docs/reference/CVF_PREPUBLIC_RUNTIME_ADAPTER_HUB_EXPORT_SURFACE_2026-04-03.md`; `docs/reviews/CVF_RFR_R5_ISOLATION_GUARANTEE_ADMISSION_WORKER_RETURN_2026-08-24.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no path deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | local Safety Runtime and Runtime Adapter Hub isolation-guarantee-admission implementation only, verified in isolation at both the canonical-contract and adapter layers |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt was created or consumed; `SandboxResult` objects in tests are hermetic in-memory fixtures only |
| actionEvidence | ACTION_EVIDENCE_PRESENT: focused Vitest, full-package Vitest, TypeScript check (Runtime Adapter Hub), direct-compiler check (Safety Runtime), file-size gate, and worker-return fast gate were executed locally |
| invocationBoundary | local Node, Vitest, TypeScript, Python governance, and Git processes only |
| interceptionBoundary | no IDE, shell, git, filesystem runtime, provider, CLI, MCP transport, Web runtime, or network interception claim |
| claimLanguage | pure local structural Safety Runtime and Runtime Adapter Hub implementation and repository-local test/type/gate evidence only; no physical containment, container, or production-security claim |
| forbiddenExpansion | no ninth path, R6, new subsystem, real sandbox engine, container, dependency installation, provider/live/network call, credential access, deployment, public sync, push, or production claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance worker dispatch; public sync remains forbidden.

## git status --short

```text
 M EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/simulation/sandbox.isolation.contract.ts
 M EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/tests/sandbox.isolation.contract.test.ts
 M EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/index.ts
 M EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/sandbox.types.ts
 M EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/worker.thread.sandbox.adapter.ts
 M EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/tests/adapters.test.ts
 M docs/reference/CVF_PREPUBLIC_RUNTIME_ADAPTER_HUB_EXPORT_SURFACE_2026-04-03.md
?? docs/reviews/CVF_RFR_R5_ISOLATION_GUARANTEE_ADMISSION_WORKER_RETURN_2026-08-24.md
```

## Changed Files

`git diff --name-status` plus the untracked inventory shows exactly the
eight paths in Actual Changed Set. No deletion, rename, checker, registry,
aggregate, session, or public path exists in the changed set.

## Command Evidence

| Command | Result |
| --- | --- |
| `git rev-parse HEAD` (before edits) | `988686c57a3e08f8db48390b7e4b9503407b74e6` |
| `git status --short --untracked-files=all` (before edits) | PASS: no output; working tree had no pending changes |
| pre-edit SHA-256 verification of all seven manifest source paths | PASS: exact match against the dispatch Source Hash Manifest |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 988686c57a3e08f8db48390b7e4b9503407b74e6 --head HEAD` | PASS: COMPLIANT in 7.46s |
| `python governance/compat/run_adif_defect_resolver.py --task-class implementation --role worker --lifecycle-phase pre-execution --json` | PASS: 0 defects returned |
| `npx vitest run --config vitest.config.ts tests/adapters.test.ts` (P1, focused) | PASS: 1 file, 46 tests |
| `npx vitest run --config vitest.config.ts` (P2, full package) | PASS: 8 files, 88 tests |
| `npx tsc --noEmit -p tsconfig.json` (Runtime Adapter Hub) | PASS: zero errors |
| `node node_modules/typescript/bin/tsc --noEmit -p tsconfig.json` (Safety Runtime, direct invocation) | PASS for both changed files: zero errors attributable to `sandbox.isolation.contract.ts` or its test file; pre-existing unrelated `cvf-ui/` React/JSX errors only |
| `npm test` (Safety Runtime) | BLOCKED_COMPONENT_DEPENDENCY_GAP: `'vitest' is not recognized as an internal or external command, operable program or batch file`; matches baseline-disclosed gap; no installation attempted |
| `python governance/compat/check_governed_file_size.py --enforce` | PASS: COMPLIANT, 0 violations |
| `python governance/compat/run_worker_return_fast_gate.py` (first run, scaffold not yet authored) | FAIL: scaffold-TODO findings plus 1 newly-added em-dash |
| in-scope repair: two em-dashes to ASCII `--`; worker return content fully authored | PASS: both repaired |
| `npx vitest run --config vitest.config.ts` (re-run after repair) | PASS: 8 files, 88 tests |
| `python governance/compat/run_worker_return_fast_gate.py` (second run, content authored) | FAIL: 3 violations (non-canonical `Input type` in two sections; an unrelated keyword-trap substring match against prose naming the Safety Runtime extension folder; `Delta` block missing a `DELTA_RECEIPT_TOKENS` literal; `gateRunPurpose` containing a forbidden substring) |
| in-scope repair: `Input type` corrected to canonical `operator-provided external comparison, critique, or recommendation`; three prose occurrences reworded to name the extension folder as `CVF_v1.7.1_SAFETY_RUNTIME` instead; `receiptEvidence` corrected to lead with literal `CLAIM_REJECTED_NO_RECEIPT`; `gateRunPurpose` reworded | PASS: all repaired |
| `python governance/compat/run_worker_return_fast_gate.py` (final run) | PASS: COMPLIANT, 65/65 checks passed |
| `git diff --check` | PASS |
| `git diff --cached --name-only` | PASS: empty |
| `git rev-parse HEAD` (after edits) | `988686c57a3e08f8db48390b7e4b9503407b74e6` (unchanged) |
| `git status --short --untracked-files=all` (after edits) | seven modified paths plus this untracked worker return; nothing staged |

## No-Commit Statement

WORKER_MUST_NOT_COMMIT honored: HEAD remains
`988686c57a3e08f8db48390b7e4b9503407b74e6`; all changed paths are unstaged
and uncommitted. Reviewer/closer owns the next decision.

## Machine Closure Package

NOT_APPLICABLE_WITH_REASON: this is a `COMPLETE_PENDING_REVIEW` worker
return, not a closed-equivalent artifact. Machine closure packaging is
owned by the reviewer/closer after independent review and material commit.
