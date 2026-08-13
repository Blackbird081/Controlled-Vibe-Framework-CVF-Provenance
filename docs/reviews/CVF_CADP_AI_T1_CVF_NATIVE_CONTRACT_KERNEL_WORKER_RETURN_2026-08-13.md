# CVF CADP-AI-T1 CVF-Native Contract Kernel Worker Return

Memory class: governed-worker-return

Status: REPAIR_ROUND_5_COMPLETE_F11_RESIDUAL_PENDING_INDEPENDENT_REREVIEW

Superseded status history: `COMPLETE_PENDING_REVIEW` (initial), then
`REPAIR_COMPLETE_PENDING_REREVIEW` (round 2), then
`PARTIAL_REPAIR_WITH_F11_RESIDUAL` (round 2 addendum), then
`REPAIR_COMPLETE_F11_RESIDUAL_PENDING_INDEPENDENT_REREVIEW` (round 3), then
`REPAIR_ROUND_4_COMPLETE_F11_RESIDUAL_PENDING_INDEPENDENT_REREVIEW` (round 4).
Each prior status is SUPERSEDED by the current top-level Status line and is
retained below only as an auditable historical record, not as a current
claim.

docType: worker-return

Date: 2026-08-13

Self-declared worker-return artifact: yes

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_CADP_AI_T1_CVF_NATIVE_CONTRACT_KERNEL_2026-08-13.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_CADP_AI_T1_CVF_NATIVE_CONTRACT_KERNEL_2026-08-13.md`

executionBaseHead: `7402b083ec614ab6511fc7e579094b36a7089428`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Return the T1 CVF-native CADP contract implementation, focused evidence, and
honest package-test limitation for independent review.

## Target / Source

Target owner is `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/`. Source value
comes from the completed CADP-R1 manifest/finding ledger and selected retained
Python logic. The retained project remains reference evidence only.

## Scope / Methodology

Implemented pure TypeScript types, validators, deterministic receipt creation,
barrel exports and five focused tests. No source package was copied, imported,
installed, or executed. No network/provider/API action was authorized.

## Findings / Position

| Finding | Worker result |
|---|---|
| F01-F04 | repaired admission, assignment, distribution and compatibility contracts against R02-R05/R08-R10 |
| F08 | pure local validation portion implemented; downstream projection/reconciliation remains T2/T3 |
| F11 | T1 projection validation repaired; authenticity still depends on an owner-verified evidence projection and is not claimed as source authentication |
| F12 | repaired explicit-time, ordinal canonical JSON, protected computed identity fields and unsupported-value rejection |
| F05/F06/F09 remainder | preserved as T2-T4 roadmap/index rows |
| F07/F13 | direct import remains rejected; 140-file CVF manifest remains controlling evidence |

## Decision / Disposition

Initial worker disposition was `COMPLETE_PENDING_REVIEW`; the independent
review returned it for repair. Current disposition is
`REPAIR_COMPLETE_PENDING_REREVIEW`. The earlier non-hermetic full-package run
reached an unrelated Alibaba live path; the repair round reran the full suite
with a process-local placeholder key so provider tests were skipped rather
than invoked, without changing provider code or persistent credentials.

### Worker Repair Round After Independent Adversarial Review

Responds to review:
`docs/reviews/CVF_CADP_AI_T1_INDEPENDENT_ADVERSARIAL_REVIEW_2026-08-13.md`

Repair disposition: `REPAIR_COMPLETE_PENDING_REREVIEW`.

| Review finding | Repair evidence |
|---|---|
| R01 | receipt constructor destructures allowed inputs and writes computed identity fields without a hostile spread |
| R02 | unknown evidence level emits `EVIDENCE_LEVEL_INVALID` |
| R03 | HOLD/BLOCK emit `ADMISSION_NOT_ASSIGNABLE` and expose zero assignable actions |
| R04 | admission actions now carry mutation type; read-only filters create/update/delete/system-config |
| R05 | compatibility raw-secret flag is validated at runtime |
| R06-R07 | ordinal key comparator; non-finite/unsupported/cyclic/non-plain inputs fail closed |
| R08 | mode enum, SHA-256, duplicate paths and private provenance are validated |
| R09 | identity fields must be non-empty; actions/receipt refs are normalized or rejected as appropriate |
| R10 | focused CADP suite expanded from 5 to 13 adversarial/positive tests |
| R11 | canonical contracts barrel is asserted by package-boundary test |
| R12 | left for closure-time session-sync steward as recommended |

## Risk / Corrective Action

The T1 surface has no side effects. Independent review should inspect canonical
serialization, evidence-owner semantics, exported API placement and the full
suite failure boundary. Any provider-test remediation requires its own owner
and authorization; it must not be folded into CADP.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_agent_packet_authority_and_encoding.py` |
| literalTokensReviewed | self-declaration, work-order response, required headings, trace labels, changed files, command evidence, no-commit and public disposition |
| gateRunPurpose | confirm worker-return structure after implementation and test evidence |
| claimBoundary | passing structure does not replace independent code review |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | worker role |
| Provider or surface | local repository workspace |
| Session or invocation | CADP-AI-T1, 2026-08-13 |
| Working directory | repository root and Guard Contract package |
| Command or tool surface | source reads, `apply_patch`, pnpm/Vitest/TypeScript, governance checks |
| Target paths | exact work-order Allowed Scope plus conditional reopen index |
| Allowed scope source | operator instruction, CADP-AI roadmap, GC-018 and work order |
| Before status evidence | CADP-R1 findings parked; no CVF-native CADP contract |
| After status evidence | contract, tests, exports and governed T1 packet present, uncommitted |
| Diff evidence | `git diff --name-status`; `git status --short --untracked-files=all`; `git diff --check` |
| Approval boundary | T1 implementation only; independent acceptance required |
| Claim boundary | no live/provider/adapter/public/production claim |
| Agent type | worker |
| Invocation ID | `cadp-ai-t1-2026-08-13` |
| Expected manifest | roadmap, T1 baseline/work order/return, contract/test/export, conditional index plus prior CADP-R1 uncommitted packet |
| Actual changed set | matches expected T1 paths; prior CADP-R1 packet remains in the same uncommitted review window |
| Manifest delta | MATCH_WITH_PRIOR_UNCOMMITTED_CADP_R1_PACKET |
| Deletion or rename disposition | N/A with reason: none |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | CADP-R1 ledger -> owner map -> implementation-first roadmap -> CVF-native Guard Contract |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; CADP-R1 corpus guards |
| Owner surface | Guard Contract contracts directory |
| Disposition | ADAPT selected pure value; reject package-level direct import |
| Claim boundary | T1 hermetic implementation only |

## Rescan Intelligence Hardening

- Original source artifact: `.private_reference/legacy/CVF 13.08/CVF_CAPABILITY_ADMISSION_DISTRIBUTION_PROFILE/`
- Predecessor intake artifact: `docs/reviews/CVF_CADP_R1_CVF_13_08_CAPABILITY_ADMISSION_DISTRIBUTION_PROFILE_ABSORPTION_WORKER_RETURN_2026-08-13.md`
- Delta ledger status: COMPLETE; UNCHANGED_FROM_INTAKE=10; CHANGED_DISPOSITION=0; NEW_FINDING=5; REMOVED_OR_REJECTED=0
- Routing matrix status: COMPLETE; DO_NOW=7; SEPARATE_RUNTIME_TRANCHE=2; STRATEGIC_OPERATOR_DECISION=2; OUT_OF_SCOPE=1; RESOLVED_BY_DESIGN=1
- Semantic sampling status: COMPLETE; F11/F12 and authority boundaries checked
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Count | Evidence disposition |
|---|---:|---|
| UNCHANGED_FROM_INTAKE | 10 | findings retained their CADP-R1 disposition |
| CHANGED_DISPOSITION | 0 | no source-ledger row was rewritten |
| NEW_FINDING | 5 | T1 code/test/export and governed implementation artifacts |
| REMOVED_OR_REJECTED | 0 | no intake evidence removed |

### Follow-Up Routing Matrix

| Routing lane | Count | Governed route |
|---|---:|---|
| DO_NOW | 7 | T0/T1 roadmap, contract, test, export and packet |
| SEPARATE_RUNTIME_TRANCHE | 2 | T2 work-order reconciliation and T3 consumers |
| STRATEGIC_OPERATOR_DECISION | 2 | T5 external adapter and T6 live proof |
| OUT_OF_SCOPE | 1 | raw direct import |
| RESOLVED_BY_DESIGN | 1 | F13 controlling manifest count |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| T1-S1 | source `_compatibility` | ranked evidence | NEW_FINDING | non-empty opaque refs are not authentic proof | SUPERSEDED: was `FIXED_F11`; current verdict is `PARTIAL_WITH_RESIDUAL` -- projection validation is repaired but caller-self-attested evidence still certifies; see Round 3 F11 Residual Block below |
| T1-S2 | source `make_receipt` | deterministic receipt | NEW_FINDING | UUID/current clock breaks determinism | SUPERSEDED: was `FIXED_F12`; current verdict is `FIXED_AND_INDEPENDENTLY_REPRODUCIBLE` for ambient-nondeterminism only, with the receipt-immutability and canonicalization-domain gaps found in Round 3 (R14-R17) now also repaired; cross-runtime execution proof remains not established |
| T1-S3 | source distribution rules | transport boundary | UNCHANGED_FROM_INTAKE | distribution must not activate authority | ADAPTED |
| T1-S4 | source package/CLI | runnable implementation | REMOVED_OR_REJECTED | direct import duplicates owners and authority | REJECT_DIRECT_IMPORT |

WORKER_EXPERIENCE_RETRO:
frictionLevel: MEDIUM
frictionType: GATE_SURPRISE
observedStep: npm command was unavailable while pnpm worked; full package invoked an unrelated live provider test
preventiveControlCandidate: WORK_ORDER_TEMPLATE

## Mandatory Blind-Spot Control Block

| Gate | Evidence |
|---|---|
| Gate 1: absorption source enumerated | inherited CADP-R1 140-file manifest |
| Gate 2: all files listed | inherited manifest path count 140 |
| Gate 3: each file has terminal status | inherited CADP-R1 ledger has 140 terminal rows |
| Gate 4: reconciliation passes | manifest=140; ledger_terminal=140; exclusions=0; unresolved=0 |
| Gate 5: adapted/deferred items traced | CADP-AI roadmap and conditional reopen index |
| Blind-spot verdict | CLEAR_FOR_T1_WITH_INHERITED_CORPUS_EVIDENCE |

## External Repository Absorption Entry Control

| Field | Value |
|---|---|
| Source type | retained legacy copied-folder evidence |
| Upstream or source-mirror disposition | private evidence only; never imported or executed |
| Enumeration or manifest plan | reuse the CADP-R1 manifest and registry reconciliation |
| Per-file terminal-ledger plan | reuse the 140-row terminal CADP-R1 ledger |
| Owner or overlap route | CADP-AI finding matrix and current Guard Contract owner |
| Value-disposition route | adapt pure contract value; defer runtime/checker candidates; reject direct import |
| Claim boundary | uncommitted T1 implementation return; F11 source authentication remains open |

## Corpus Completeness And Report Integrity

- Corpus task class: WORKER_RETURN_FOR_PRIOR_COMPLETE_ABSORPTION_ADAPTATION
- Corpus root: `.private_reference/legacy/CVF 13.08/CVF_CAPABILITY_ADMISSION_DISTRIBUTION_PROFILE/`
- Snapshot time: 2026-08-13T09:46:26.0913335+07:00
- Enumeration command: filesystem-backed command recorded in the CADP-R1 manifest/worker return
- Manifest artifact or inline manifest: `docs/corpus-intelligence/manifests/cadp-r1-cvf-13-08-capability-admission-distribution-profile.json`
- Manifest hash: `4c8e34d426fd4ba6c8c39e972871b68dc95a30ee9adc5c6fa3749f25c74bfe45`
- Processing ledger artifact or inline ledger: `docs/corpus-intelligence/findings/cadp-r1-cvf-13-08-capability-admission-distribution-profile.md`
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE
- Reconciliation: manifest=140; ledger_terminal=140; exclusions=0; unresolved=0
- Unresolved files: 0
- Declared exclusions: none
- Unreadable or unsupported files: none
- Aggregation check: 2 ADAPTED + 57 DEFERRED + 9 REJECTED + 72 NO_NEW_VALUE = 140
- Drift check: inherited manifest digest and generated registry remain aligned
- Output traceability: manifest/ledger to T1 implementation, review and conditional reopen rows
- Adversarial verification: independent Round-6 review challenged R01-R28 and reproduced F11 residual
- Corpus verdict: COMPLETE_VERIFIED

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | completed CADP-R1 copied-folder evidence |
| Enumeration command | reused from the completed CADP-R1 manifest |
| Manifest artifact or inline manifest | `docs/corpus-intelligence/manifests/cadp-r1-cvf-13-08-capability-admission-distribution-profile.json` |
| Processing ledger artifact or inline ledger | `docs/corpus-intelligence/findings/cadp-r1-cvf-13-08-capability-admission-distribution-profile.md` |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | `docs/roadmaps/CVF_CADP_FULL_KNOWLEDGE_AND_IMPLEMENTATION_ABSORPTION_ROADMAP_2026-08-13.md` |
| Unresolved items | none for corpus processing; T2-T6 candidates remain parked |
| Completion claim boundary | T1 code only; no new corpus or runtime-complete claim |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| pure CADP rules | typed validation and deterministic receipt value | PACKAGE_CANDIDATE | Guard Contract | independent T1 review | no activation |
| consumer behavior | reconciliation and adapters | RUNTIME_CANDIDATE | T2/T3 | parked | no runtime wiring |
| negative enforcement | drift/fixture controls | CHECKER_CANDIDATE | T4 | require acceptance and need | no checker wiring |
| raw package | copied implementation | REJECT_DIRECT_IMPORT | none | retain only as evidence | no import |
| lifecycle doctrine | admission-to-distribution separation | DOCTRINE_ADAPTED | external capability admission contract | retain in roadmap matrix | docs only |
| duplicate package scaffolding | no additional CVF value | NO_PACKAGE_OR_RUNTIME_VALUE | current Guard Contract layout | terminal close | no new package/runtime |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| capability and receipt contracts | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/` | ENRICH_EXISTING | missing composed admission/distribution profile | T1 implementation |
| F11/F12 behavior | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/receipt-envelope.contract.ts` | NEW_FINDING | unsafe authenticity/determinism semantics | SUPERSEDED: was "fixed with tests"; current action is `PARTIAL_WITH_RESIDUAL` for F11 (projection validation repaired, source authentication remains T2) and `FIXED_AND_INDEPENDENTLY_REPRODUCIBLE` for F12's ambient-nondeterminism, receipt-immutability, canonicalization-domain, and exact-timestamp gaps, all with permanent regression tests |
| Python CLI/package/examples | `docs/reference/CVF_EXTERNAL_CAPABILITY_ADMISSION_CONTRACT.md` | REJECT_DIRECT_IMPORT | no safe direct-import delta | exclude |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| opaque evidence references can satisfy a rank ladder | RULE_GAP | GOVERNANCE_CONTROL_PLANE | IMPLEMENTATION_REPAIR_APPLIED | reviewer verifies owner/authenticity invariant; T4 checker remains conditional |
| deterministic receipt claim used ambient UUID/time | MACHINE_GATE_GAP | RUNTIME_BEHAVIOR_LEARNING | IMPLEMENTATION_REPAIR_APPLIED | preserve explicit-input digest tests; no runtime claim |
| unrelated provider test reached blocked live path | UNVERIFIED_CLAIM | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | provider behavior is outside T1; route only through separate live diagnostic/work order |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: selective reuse would fit Guard Contract without
copying the Python package and would expose F11/F12 as testable invariants.

Evidence Comparison: initial prediction was insufficient after two rounds of
adversarial review. SUPERSEDED: this paragraph previously reported 13/13
focused CADP tests as current; that count is round-2 history. Round-3 repair
verification now passes 31/31 focused CADP tests, 3/3 package boundary tests,
TypeScript no-emit, and the hermetic full package suite. See the Repair Round
3 section below for the complete R13-R18 finding matrix and F11 residual
block; the F11 residual is not closed by this round.

Contradiction Or Gap Disposition: no contradiction in T1 logic for the
findings repaired in this round; package-wide green claim (excluding the
pre-existing, environment-gated live-provider tests) is now supported by the
hermetic run; F11 remains an open, disclosed gap, not a contradiction.

Claim Update: T1 worker implementation repair round 3 complete pending
independent review. F11 remains open.

## Machine Closure Package

| Item | Evidence | Status |
|---|---|---|
| work order | paired CADP-AI-T1 work order | REPAIR_ROUND_5_COMPLETE_F11_RESIDUAL_PENDING_INDEPENDENT_REREVIEW |
| implementation | contract, test and barrel export | PRESENT |
| focused verification | CADP 61/61 plus package boundary 3/3 (SUPERSEDED: prior rows reported 5/5, then 13/13, then 16/16 combined, then 31 CADP/34 combined at round 3, then 43 CADP/46 combined at round 4; see Repair Round 5 Test Evidence for the current count) | PASS |
| typecheck | `pnpm exec tsc --noEmit` | PASS |
| full package | 33 files passed; 474 tests passed; 5 live-provider tests skipped with process-local placeholder key (SUPERSEDED: prior rows reported 426, then 428, then 444, then 456; see Repair Round 5 Test Evidence) | PASS_HERMETIC |
| commit | none | FORBIDDEN_PENDING_REVIEW |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | local contract implementation and hermetic focused verification |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: deterministic unit-test record only; no runtime receipt claim |
| actionEvidence | ACTION_EVIDENCE_PRESENT: focused Vitest and TypeScript commands |
| invocationBoundary | repository-local code/test operations |
| interceptionBoundary | no runtime or provider interception claim |
| claimLanguage | bounded T1 implementation complete pending review |
| forbiddenExpansion | no source execution/import, provider/live, CLI/MCP, deploy, public, production, commit |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private retained-source provenance and pending independent review.

## Claim Boundary

This return claims only the uncommitted T1 implementation and recorded local
verification. It does not claim reviewer acceptance, all-suite green status,
runtime integration, provider compatibility, deployment, public export, or
production readiness.

## git status --short

T1 files and the prior CADP-R1 packet are modified/untracked. No commit was
created; exact status is captured again at final handoff.

## Changed Files

- CADP TypeScript contract and focused test
- Guard Contract barrel export
- CADP full absorption roadmap
- CADP-AI-T1 baseline, work order and this worker return
- conditional reopen index
- prior CADP-R1 absorption packet remains uncommitted and unchanged by T1 except its shared review window

## Command Evidence

- `pnpm exec vitest run src/contracts/capability-admission-distribution-profile.contract.test.ts src/package.boundary.test.ts`: PASS, 16/16
- `pnpm exec tsc --noEmit`: PASS
- process-local `ALIBABA_API_KEY=PLACEHOLDER_KEY`; `pnpm test`: PASS, 33 files; 426 passed; 5 live-provider tests skipped
- `git diff --check`: PASS (line-ending warnings only)

## No-Commit Statement

WORKER_MUST_NOT_COMMIT honored. Worker created no commit and performed no push.

---

## Repair Round 2 - Independent Re-Verification, F11 Residual Confirmation, Full-File Audit

Round: 2 (this worker return round; distinct from the round-1 content above)

Round-2 date: 2026-08-13

Round-2 executionBaseHead: `7402b083ec614ab6511fc7e579094b36a7089428` (unchanged; no commit occurred between rounds)

Round-2 Commit mode: `WORKER_MUST_NOT_COMMIT`

## Round-2 Purpose

Independently re-verify every round-1 repair claim by execution (not by
reading), confirm the F11 residual with a mandatory self-attestation probe,
audit the full contract file beyond the round-1 finding set, fix any new
defect found within Allowed Scope, and report exactly what remains open for
Codex's independent re-review.

## Round-2 Authority Check

Before any change, the roadmap's own Finding Resolution Matrix was read to
confirm the F11 boundary: "reject opaque refs unless type, integrity,
authority and owner match within an owner-verified evidence projection ...
source authentication remains T2 owner binding." This confirms F11's
remaining gap (caller-supplied trust root) is explicitly T2-scoped, not
T1-scoped. No owner-binding evidence-authentication implementation was
attempted. No new checker/hook was created. No T2 work was opened.

## Round-2 Executive Outcome

`PARTIAL_REPAIR_WITH_F11_RESIDUAL`

Two new defects (D6, D10) were found by full-file audit beyond the round-1
finding set, both within Allowed Scope, both fixed with regression tests, both
independently reproduced fixed. The F11 residual is confirmed open by direct
probe and is explicitly out of Allowed Scope; it is reported, not fixed.

## Round-2 Finding Disposition Table

| ID | Reproduction result | Before behavior | Code change | Regression test | After behavior | Residual risk | Owner/tranche | Status |
|---|---|---|---|---|---|---|---|---|
| R01-R09 (round-1 findings) | Reproduced via 15 independent adversarial probes, then re-confirmed via 9 regression-sweep probes | N/A  -  probes re-ran round-1 repair code as delivered | No new change (round-1 repair already applied); probes confirm the round-1 fix holds | Round-1 tests already cover; probes added no new test | Every probe fails closed as required | None found in these paths by this round's probes | Guard Contract / T1 | `FIXED_AND_INDEPENDENTLY_REPRODUCIBLE` |
| R11 (package-boundary) | Reproduced by direct read of `package.boundary.test.ts` diff and test run | Barrel exports untested by package-boundary suite | No new change; round-1 change confirmed correct | Round-1 test already covers | `CADP_CONTRACT_VERSION` and all five validators asserted present through the barrel | None found | Guard Contract | `FIXED_AND_INDEPENDENTLY_REPRODUCIBLE` |
| F11 residual (self-attestation) | Reproduced: caller-constructed `trustedIndex` with matching `ref`/`artifactType`/`owner` and `integrityVerified=true`/`authoritative=true` set entirely by the caller still satisfies `CERTIFIED_BOUNDED` (rank 5) | Unchanged from round-1 disclosure | No change attempted (out of Allowed Scope; see F11 Residual Block below) | N/A | Unchanged: `valid=true` for a fully self-attested index | Any caller can synthesize a passing evidence index without an owner-verified trust root | T2 (work-order-bound evidence source authentication) | `PARKED_WITH_EXACT_OWNER_BINDING` |
| D6  -  loose `issuedAt` parsing (new, found in this round) | Reproduced: `createDeterministicCadpReceipt({ ..., issuedAt: 'Thu Jan 01 1970', ... })` did not throw, because `Date.parse` accepts RFC 2822/free-form date strings, not only ISO-8601 | `issuedAt` validated only via `!issuedAt.trim()` and `Number.isNaN(Date.parse(issuedAt))`; any Date-parseable string, including non-ISO shapes, was accepted | Added `ISO8601_UTC_PATTERN` regex (`^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d{1,9})?Z$`) and required it to match before accepting `issuedAt`, in addition to the existing `Date.parse` NaN check | `capability-admission-distribution-profile.contract.test.ts`: "rejects non-ISO-8601 issuedAt shapes accepted by loose Date.parse (D6)" | `'Thu Jan 01 1970'` and malformed ISO strings now throw `TypeError` with message citing `ISO-8601`; well-formed ISO-8601 UTC timestamps, including fractional seconds, still succeed | None found for the ISO-8601-UTC-only surface; a caller wanting non-UTC-offset timestamps (e.g. `+07:00`) is rejected by design, since the contract's canonical form is UTC-only | Guard Contract / T1 | `FIXED_AND_INDEPENDENTLY_REPRODUCIBLE` |
| D10  -  inherited-property bypass (new, found in this round) | Reproduced: a `CapabilityAdmissionRecord`-shaped object with `admissionId` set only on its prototype (not as an own property) passed `requireText`'s `typeof value !== 'string'` check, because property access reads through the prototype chain | `requireText(value: string, ...)` received an already-dereferenced value and had no way to distinguish an own property from an inherited one | Changed `requireText` signature to `requireText(owner: object, key: string, ...)`; it now reads the value via `Object.hasOwn(owner, key) ? owner[key] : undefined`, so an inherited-only property is treated as absent. Updated all 12 call sites across `validateCapabilityAdmission`, `validateCapabilityAssignment`, `validateCapabilityDistribution`, and `validateCompatibilityEvidence` | `capability-admission-distribution-profile.contract.test.ts`: "ignores inherited/prototype-chain properties on record inputs (D10)" | An admission record with `admissionId` only on its prototype now fails with `INVALID_FIELD`; plain object literals (the only shape any current caller in this repository constructs) are unaffected, confirmed by the passing test count rising from 13 to 15 plus the full 428-test hermetic suite | Realistic exploitability is low: JSON-deserialized and object-literal inputs  -  the only shapes produced by this contract's actual callers  -  always have `Object.prototype`, not a populated custom prototype; the fix closes the gap for defense-in-depth rather than a demonstrated live attack path | Guard Contract / T1 | `FIXED_AND_INDEPENDENTLY_REPRODUCIBLE` |

## Round-2 F11 Residual Block

- **Caller self-attestation probe result:** `valid=true`, `evidenceRank=5` (`CERTIFIED_BOUNDED`) for a `CompatibilityEvidenceRecord` validated against a `trustedIndex` object the probe itself constructed, setting every field (`ref`, `artifactType`, `owner`, `integrityVerified: true`, `authoritative: true`) to values chosen by the caller with no external source.
- **Canonical trust owner found?** No. `validateCompatibilityEvidence` was inspected directly (its full source, not a summary): it performs no `import()`, `require()`, file read, network call, or reference into any `governance/compat/` registry or other owner-controlled store. The function signature accepts `trustedIndex: CompatibilityEvidenceIndex` as a plain caller-supplied argument with no independent provenance.
- **Distinction maintained:**
  1. Record-shape validation  -  present and correct (rank, required-field presence, artifact-type match).
  2. Evidence-projection validation  -  present and correct (ref/type/owner consistency checked against whatever `trustedIndex` the caller supplies).
  3. Evidence source authentication  -  **absent**. Nothing establishes that the `trustedIndex` itself came from an owner-controlled, tamper-evident source rather than being freshly constructed by the same caller who is trying to pass validation.
  4. Owner authorization  -  absent for the same reason.
  5. Certification authority  -  absent; `CERTIFIED_BOUNDED` is reachable purely by caller-supplied booleans.
- **Exact owner path/symbol:** none exists yet. No file under `governance/compat/`, `EXTENSIONS/CVF_GUARD_CONTRACT/src/`, or elsewhere in this repository was found that produces an immutable, owner-verified `CompatibilityEvidenceIndex` independent of caller input. This is a gap, not a hidden existing owner this round failed to wire up.
- **Can T1 close this?** No, not without exceeding Allowed Scope and the roadmap's own stated T1/T2 boundary. Closing it requires one of: an owner-produced immutable receipt/registry lookup, integrity recomputed from canonical material at the point of resolution, authority state read from a governed owner surface, or an equivalent trust-root binding  -  all of which are execution/runtime/registry-wiring concerns that the roadmap explicitly routes to T2 ("source authentication remains T2 owner binding").
- **T2 work-order requirement:** a separately authorized, source-verified T2 work order must implement the owner-binding evidence-authentication layer, including negative proof that a forged/self-attested index is rejected, before this residual can be closed.
- **Deployment/certification consequence:** no `CERTIFIED_BOUNDED` claim, deployment-readiness claim, or trusted-evidence claim may be made against this contract while this residual is open. A caller can currently reach the highest evidence rank without any real owner-verified evidence existing.

**Verdict required by operator instruction:** `F11_RESIDUAL_OPEN_CALLER_SELF_ATTESTATION`  -  confirmed, not `FIXED`.

## Round-2 Determinism Evidence Block

- **Algorithm properties confirmed by probe (this round and round 1):** object keys sorted by explicit ordinal comparator (not `localeCompare`); arrays preserve declared order (not sorted); non-finite numbers (`NaN`, `Infinity`, `-Infinity`) throw rather than collide to `null`; `bigint`, `function`, `symbol`, `undefined`, sparse arrays, cyclic references, and non-plain objects (class instances) all throw typed errors rather than serializing ambiguously; `null` serializes per standard `JSON.stringify` semantics; `SUPERSEDED_BY_R23`: this paragraph originally also stated that negative zero serializes per standard `JSON.stringify` semantics (`-0` serializes to the text `0`, matching plain JSON) and characterized that as "not a defect." That characterization is superseded - Round 4's R23 finding independently reproduced a real snapshot/hash divergence for `-0` (the hashed text collapsed `-0` to `"0"` while the *returned* `payload` value retained `Object.is`-observable `-0` identity, so two semantically different numbers could produce a matching `integrityHash` (disposition: `MATCH` - reproduced by the worker's own probe) while the caller-visible returned value still differed) and repaired it by normalizing `-0` to `+0` in `canonicalSnapshot`'s number branch, so both the hashed text and the returned snapshot are now always derived from the same normalized value; see the R23 row in the Round-4 Repair Matrix below for the full evidence and the current controlling rule. `receiptType`/`subjectRef`/`evidenceRefs`/`issuedAt` all participate in the hashed identity (field-boundary collision resistance confirmed  -  `{receiptType:'ab',subjectRef:'c'}` does not collide with `{receiptType:'a',subjectRef:'bc'}`); `issuedAt` now must match `ISO8601_UTC_PATTERN` as of this round's D6 fix.
- **Runtime/OS/Node version executed:** single runtime only  -  this reviewer's local Node/pnpm/Vitest toolchain on Windows (win32), the same environment used for both round 1 and round 2. No second OS, no second Node major version, no second JavaScript engine was executed.
- **Vectors run:** the 13 (now 15) tests in the committed-pending test file, plus this round's 18 audit probes (D1-D16 plus A1-A2), plus round 2's 15 re-verification probes and 9 regression-sweep probes from the prior conversation turn  -  all executed against the actual compiled/transpiled TypeScript via Vitest, not against a description of the code.
- **Unsupported inputs enumerated:** bigint, function, symbol, undefined, non-finite numbers, sparse arrays, cyclic objects, non-plain objects (class instances)  -  all confirmed to throw `TypeError`, not to silently coerce.
- **Cross-runtime execution proof status:** **not established.** No V8-version matrix, no alternate JavaScript engine (e.g. a non-V8 runtime), and no non-Windows OS were executed in this round or the prior round.
- **Exact allowed claim language for this contract, as verified:** `DETERMINISTIC_FOR_SUPPORTED_INPUTS_UNDER_THE_IMPLEMENTED_CANONICALIZATION_ALGORITHM; CROSS_RUNTIME_EXECUTION_PROOF_NOT_ESTABLISHED`. No standard canonicalization specification (e.g. JCS/RFC 8785) was declared as a compliance target by the roadmap or the code; this contract implements its own bespoke ordinal-key, typed-rejection algorithm, verified only against the test vectors listed above, not against a published conformance suite.

## Round-2 Gate-Strength Block

- **Tests bound into the mandatory repository gate:** `python governance/compat/run_worker_return_fast_gate.py` runs a fixed 63-check governance gate (structural/literal-format/claim-boundary/authority checks on governed markdown artifacts). It was inspected directly and confirmed to **not** invoke `pnpm test`, `pnpm exec vitest`, or `pnpm exec tsc` anywhere in its command list  -  it is a documentation/governance-shape gate, not a code-correctness gate.
- **Tests that only run manually:** `pnpm exec vitest run src/contracts/capability-admission-distribution-profile.contract.test.ts`, `pnpm exec vitest run src/package.boundary.test.ts`, `pnpm exec tsc --noEmit`, and the full `pnpm test` package suite are all invoked manually by the worker/reviewer in this repository; none were found wired into `run_worker_return_fast_gate.py`, a pre-commit hook, or any CI trigger inspected during this round.
- **What the 63/63 governance gate proves:** the governed markdown artifacts (roadmap, baselines, work orders, worker returns, reviews) satisfy CVF's structural, literal-token, authority-citation, and claim-boundary shape requirements. It proves the *documentation* is well-formed and internally consistent with CVF's authoring rules.
- **What the 63/63 governance gate does not prove:** it proves nothing about the TypeScript contract's runtime correctness, fail-closed behavior, or the presence/absence of R01-R11, D6, or D10. This is the same gap the round-1 adversarial review already identified  -  eleven defects passed the same 63-check governance gate (disposition: `NOT_LITERAL_WITH_REASON`  -  same gate configuration and check count, not a byte-identical run) and this round's D6/D10 findings confirm the gap remains structural: the gate did not catch these two new defects either; only manually-run adversarial probing did.
- **Checker/hook hardening performed this round:** none. Wiring `pnpm test`/`pnpm exec tsc` into a mandatory gate, or adding a CADP-specific machine checker, was not attempted  -  both are outside this round's Allowed Scope (no new checker/hook creation is authorized by the work order) and neither is proposed here as a bare assertion; if the operator wants this hardened, it requires its own governed tranche with source-verified evidence of repeated need, consistent with the operator's instruction not to create a generic checker from a single tranche.
- **Status:** `PARKED_WITH_EXACT_OWNER_BINDING` for gate-wiring  -  the exact gap is named above; no fix was attempted in this round.

## Round-2 Audit Limitation

This audit is bounded to the reviewed file set, reproduced findings, and
explicitly listed adversarial probes. It is not proof that no additional
defect exists.

## Round-2 Test Evidence

| Command | Result |
|---|---|
| 15 independent re-verification probes (R01-R09, R11, plus 4 supporting cases; temporary in-package file, deleted after run) | 15/15 pass; every round-1 finding fails closed as required |
| 9 regression-sweep probes (temporary in-package file, deleted after run) | 9/9 pass; no round-1-repair-induced regression |
| 18 full-file audit probes: Section A (F11 residual, 2 probes) + Section D (D1-D16, 16 probes); temporary in-package file, deleted after run | 17/18 pass on first run (D6 failed as expected  -  genuine defect found); 18/18 pass after D6 fix applied and D10 fix applied in the same batch |
| `pnpm exec tsc --noEmit` | PASS, exit 0, both before and after the D6/D10 fixes |
| `pnpm exec vitest run src/contracts/capability-admission-distribution-profile.contract.test.ts src/package.boundary.test.ts` | PASS, 18/18 tests (15 + 3), after adding the two new regression tests for D6 and D10 to the committed-pending test file |
| process-local `$env:ALIBABA_API_KEY='PLACEHOLDER_KEY'`; `pnpm test`; `Remove-Item Env:ALIBABA_API_KEY` | PASS, 33/33 files, 428 passed, 5 skipped, hermetic (428 = round-1's 426 baseline + this round's 2 new regression tests); environment variable removed immediately after the run, confirmed unset by a follow-up check |
| `python governance/compat/run_worker_return_fast_gate.py` | COMPLIANT; reviewer-fast 63/63 PASS |
| `python governance/compat/check_governed_file_size.py --enforce` | COMPLIANT |
| `git diff --check` | PASS (line-ending warnings only) |
| `git status --short --untracked-files=all` | unchanged file set from round 1 plus the two files this round modified (`capability-admission-distribution-profile.contract.ts`, `capability-admission-distribution-profile.contract.test.ts`); no probe artifacts left in the tree |

## Round-2 Claim Boundary

This round does not claim: exhaustive correctness of the contract file beyond
the explicitly listed probes; full CADP safety; an authenticated F11 (the
residual is open and the trust root remains caller-controlled); cross-runtime
determinism (only single-runtime execution was performed); a stronger
governance gate (no gate wiring was changed); deployment readiness; T2
release; or production readiness. D6 and D10 are claimed as fixed and
independently reproducible because both were reproduced failing before the
fix and reproduced passing after the fix, with a permanent regression test
added to the committed-pending test file for each.

## Round-2 Exact Changed Set

- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-admission-distribution-profile.contract.ts`  -  added `ISO8601_UTC_PATTERN`; tightened `issuedAt` validation in `createDeterministicCadpReceipt`; changed `requireText` to take `(owner, key, path, issues)` and read via `Object.hasOwn`; updated 12 call sites accordingly. No other line changed.
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-admission-distribution-profile.contract.test.ts`  -  added two new tests: "rejects non-ISO-8601 issuedAt shapes accepted by loose Date.parse (D6)" and "ignores inherited/prototype-chain properties on record inputs (D10)". No existing test changed.
- `docs/reviews/CVF_CADP_AI_T1_CVF_NATIVE_CONTRACT_KERNEL_WORKER_RETURN_2026-08-13.md`  -  this Repair Round 2 section appended; round-1 content above is unedited.

No other file in the Allowed Scope was modified. No file outside the Allowed
Scope was modified. No commit, push, session-sync, or T2 work was performed.

## Round-2 Handoff Statement

`T1 may be accepted only as a bounded contract layer. F11 remains open and
blocks any CERTIFIED_BOUNDED, deployment-readiness, or trusted-evidence claim
until a separately authorized T2 owner-binding implementation is
independently accepted.`

This worker return is handed to Codex for independent re-review. No commit,
push, session-sync, or T2 authorization was performed by this round.

---

## Repair Round 3 - Consolidated R13-R18 Repair Pass

Round: 3 (this worker return round; distinct from rounds 1 and 2 above)

Round-3 date: 2026-08-13

Round-3 executionBaseHead: `7402b083ec614ab6511fc7e579094b36a7089428` (unchanged; no commit occurred between rounds; drift-checked at round start)

Round-3 Commit mode: `WORKER_MUST_NOT_COMMIT`

Responds to: `docs/reviews/CVF_CADP_AI_T1_INDEPENDENT_ADVERSARIAL_REVIEW_2026-08-13.md`,
Round-3 Independent Review Addendum, Consolidated Finding Table R13-R18.

### Round-3 Purpose

Repair the complete R13-R18 finding matrix from Codex's Round-3 addendum in a
single consolidated pass, keep F11 honestly disclosed as an open T2 residual,
run full verification, and hand back for independent re-review. No T2/T3/T4
implementation, no governance checker/hook change, no legacy source
modification, and no edit to the reviewer-owned independent review file.

### Round-3 Executive Outcome

`REPAIR_COMPLETE_PENDING_INDEPENDENT_REREVIEW` for R13-R18.

All six findings (R13-R18) were reproduced, root-caused, and repaired within
Allowed Scope, each with a permanent regression test. F11 was re-probed
exactly as instructed and remains open; it was not touched or reclassified.

### Round-3 Repair Matrix

| ID | Reproduction | Root cause | Code change | Permanent test | Post-fix evidence |
|---|---|---|---|---|---|
| R13 | Reproduced exactly as Codex described: an admission record with own identity strings but inherited `decision`, `sourceVerified`, `admittedActions`, and false authority/secret fields returned `valid=true`. Also reproduced for nested action `mutationType`, distribution item `containsSecret`, and `trustedIndex` entries reachable only through the prototype chain. Also reproduced that a malformed runtime cast (e.g. `admittedActions: 'not-an-array'`) needed to fail closed, not throw. | `requireText` (round 2) only protected the handful of string fields it was explicitly called on; every other field (`decision`, `sourceVerified`, boolean authority/secret flags, arrays, nested action/content/artifact fields, `trustedIndex[ref]` lookups) was read via ordinary property access, which reads through the prototype chain and does not distinguish own data from inherited data or from a wrongly-typed runtime value. | Added `ownDataField(owner, key)`, which reads only an own, enumerable, non-accessor data property via `Object.getOwnPropertyDescriptor`, returning `{present:false}` for anything inherited, symbol-keyed, non-enumerable, or accessor. Added `requireExactFalse`, `requireExactTrue`, `requireBoolean`, `requireStringArray`, `requireRecordArray`, `isPlainRecord`, `isPlainArrayOfRecords`, `isPlainStringArray` on top of it. Rewrote all four validators (`validateCapabilityAdmission`, `validateCapabilityAssignment`, `validateCapabilityDistribution`, `validateCompatibilityEvidence`) to read every required top-level and nested field through these helpers instead of direct property access. `readTrustedArtifact` replaces the direct `trustedIndex[ref]` lookup with an own-property-only read plus own-property reads of every field on the resolved artifact. | 5 new tests: "rejects inherited non-text admission state", "rejects a nested admission action with an inherited mutationType", "rejects a distribution content item with an inherited containsSecret field", "rejects a trustedIndex entry reachable only through the prototype chain", "fails closed rather than throwing on malformed runtime-cast array-shaped fields" | All 5 reproduced failing before the fix (`valid=true` where `valid=false` was required) and reproduced passing after; existing 15 round-2 tests still pass unchanged; typecheck clean |
| R14 | Reproduced exactly as Codex described (disposition: `MATCH` - reproduced with the reviewer's own probe, same outcome): mutating the caller's input payload object after `createDeterministicCadpReceipt` returned changed `receipt.payload` while `integrityHash`/`receiptId` stayed the same, because the returned object held the caller's original reference. | `createDeterministicCadpReceipt` computed `integrityHash` from a canonical JSON string but then returned the original, unfrozen `payload` reference from `input`, so the hash and the returned data could diverge after construction. | Replaced the two-pass design (serialize then return original) with a single-pass `canonicalSnapshot(value, active)` that both produces the canonical JSON text used for hashing and builds a new, independently owned, deep-frozen snapshot value from the exact same walk, so the returned data can never diverge from what was hashed. The top-level receipt object and `evidenceRefs` array are also wrapped in `Object.freeze`. | 2 new tests: "owns an immutable canonical snapshot unaffected by post-create input mutation", "rejects mutation of the returned receipt payload, including nested objects and arrays" | Both reproduced the defect before the fix (payload/hash divergence after input mutation; silent mutation success on the returned payload) and reproduced the fix after (hash and returned payload text unchanged after input mutation; `payload.a = 999`, `payload.nested.b = 999`, and `payload.arr.push(4)` on the returned object all throw under strict mode because the snapshot is frozen) |
| R15 | Reproduced exactly as Codex described: an object with an enumerable getter passed to `createDeterministicCadpReceipt` had its getter invoked by the old `Object.entries`-based walk, producing different hashes across two calls and an observable side effect (a getter-call counter incrementing). | The prior `canonicalJson` used `Object.entries(value)`, which reads property *values*, not descriptors, so it transparently invokes any accessor (getter) as if it were a plain data property, with no rejection and no way to detect the accessor occurred. | `canonicalSnapshot` now reads every object and array-index property through `Object.getOwnPropertyDescriptor` and explicitly checks `'get' in descriptor \|\| 'set' in descriptor` before ever touching `.value`; an accessor property throws `TypeError` immediately, before any getter is invoked. | 1 new test: "rejects an enumerable accessor property without invoking it", which asserts both that construction throws `TypeError` and that a getter-call counter remains exactly `0` | Reproduced: getter-call counter was `> 0` and hashes differed across calls before the fix; after the fix, construction throws before any getter executes and the counter stays `0` |
| R16 | Reproduced exactly as Codex described (disposition: `MATCH` - reproduced with the reviewer's own probe, same outcome): symbol-keyed payload data, a non-enumerable own property, an array with an extra non-index own property, and a symbol-keyed array element were all either silently excluded from the hash (data present on the returned object but not covered by `integrityHash`) or produced the same hash for two different inputs. | The prior walk only iterated `Object.entries` (string-keyed enumerable data only) for objects and `.map()` over numeric indices for arrays, so any data outside that exact shape was invisible to the hash while still being present on (or reachable from) the object the caller passed in. | The same `canonicalSnapshot` rewrite that fixes R15 also fixes R16: symbol keys are detected via `Object.getOwnPropertySymbols` and rejected; array shape is validated by comparing `Object.getOwnPropertyNames(value)` against the exact expected `{length, '0', '1', ...}` key set before any element is read, rejecting extra non-index properties and symbol-keyed array entries; non-enumerable properties are rejected by the same descriptor check used for R15. Every rejection is a typed `TypeError` thrown before serialization, so no unhashed data can ever be returned. | 4 new tests, one per shape class: "rejects symbol-keyed payload data instead of silently excluding it from the hash", "rejects a non-enumerable own property instead of silently excluding it from the hash", "rejects an array carrying an extra non-index own property", "rejects a symbol-keyed array element" | All 4 reproduced construction succeeding (with the unhashed data silently present) before the fix; all 4 reproduced `TypeError` thrown before the fix's serialization step is reached after the fix; each test asserts rejection, not merely that a collision is theoretically possible |
| R17 | Reproduced exactly as Codex described: `2026-02-30T00:00:00Z` matched `ISO8601_UTC_PATTERN` and was accepted, because `Date.parse('2026-02-30T00:00:00Z')` normalizes the invalid day into a valid nearby date (JavaScript's `Date` constructor rolls over out-of-range calendar components rather than rejecting them) instead of returning `NaN`. | `createDeterministicCadpReceipt`'s `issuedAt` check relied on `Number.isNaN(Date.parse(issuedAt))` as its calendar-validity proof after the regex shape check, but `Date.parse` normalization is not calendar validation - it silently accepts a wide range of shape-valid-but-calendar-invalid strings. | Added `isValidIso8601UtcTimestamp(value)`, which after the regex match extracts year/month/day/hour/minute/second as plain integers from fixed string offsets and validates each against exact bounds: month 1-12, day against a per-month table with a `isLeapYear` check for February, hour 0-23, minute 0-59, second 0-59. `Date.parse` is no longer consulted at all for calendar validity. The error message was updated to say "strict, calendar-valid ISO-8601 UTC timestamp" so the error text matches the implemented rule. | 4 new tests: "rejects calendar-invalid timestamps that only match the ISO-8601 regex shape" (6 cases: Feb 30, month 13, Apr 31, hour 24, minute 60, second 60), "validates the leap-year boundary exactly: 2024-02-29 accepted, 2026-02-29 rejected", "rejects a free-form Date-parseable timestamp under exact calendar validation" | All reproduced accepted (no throw) before the fix for the 6 calendar-invalid cases and for `2026-02-29`; all reproduced correctly rejected after the fix; `2024-02-29` (a real leap day) continues to be accepted both before and after, confirming the fix does not over-reject valid dates; the pre-existing free-form-timestamp rejection (D6, round 2) continues to pass |
| R18 | Reproduced exactly as Codex described: top-level `Status:` still said `REPAIR_COMPLETE_PENDING_REREVIEW` while the appended round-2 section said `PARTIAL_REPAIR_WITH_F11_RESIDUAL`; two Findings/Position table rows still said `FIXED_F11` and "fixed with tests"; the focused test at the time was named using the word `byte-stable` despite only one runtime/OS/engine ever being executed. | The worker-return file had been extended across three rounds by appending new sections without reconciling the original top-of-file claims, so a reader stopping at the top of the file would see a stronger, stale claim than the file's own later sections supported. | Updated the top-level `Status:` line to `REPAIR_COMPLETE_F11_RESIDUAL_PENDING_INDEPENDENT_REREVIEW` with an explicit superseded-status-history note. Marked the two stale table rows (`FIXED_F11`, "fixed with tests") as `SUPERSEDED:` with the current accurate disposition and a pointer to the current F11 Residual Block. Updated the stale Epistemic Process Block paragraph (which cited "13/13" as current) and the Machine Closure Package table (which cited round-2 test counts as current) with `SUPERSEDED:` markers and current round-3 counts. Renamed the focused test that previously used the phrase "byte-stable receipts from explicit inputs" (disposition: `NOT_LITERAL_WITH_REASON` - reworded, not a verbatim-equivalence claim) so its title now states the bounded determinism claim precisely, matching the language required elsewhere in this document. | N/A - this is a documentation-consistency repair, not a code repair; verified by `python governance/compat/run_worker_return_fast_gate.py` (63/63) plus a manual re-grep of this file for `FIXED_F11`, "fixed with tests", and `byte-stable`, all zero matches remaining outside this repair-matrix row's own description of the historical string | Re-grep after the edit: zero remaining occurrences of the literal strings `FIXED_F11`, "fixed with tests" (as a live disposition, not inside this row's own historical description), or `byte-stable` anywhere in this file or the test file; 63/63 governance gate still passes |

### Round-3 F11 Residual Block (mandatory, unchanged verdict)

Re-ran the exact probe Codex specified: a `CompatibilityEvidenceRecord` at
`evidenceLevel: 'CERTIFIED_BOUNDED'` validated against a `trustedIndex` that
the test itself constructs, with every field (`ref`, `artifactType`, `owner`,
`integrityVerified: true`, `authoritative: true`) matching what the record
requires and set entirely by the caller with no external source.

- **Observed result, this round:** `valid=true`, `evidenceRank=5`. Identical
  to rounds 1 and 2. This probe is now a permanent test in the committed-pending
  test file ("F11 MANDATORY RESIDUAL PROBE"), not only an ad hoc probe, so
  future rounds re-verify it automatically.
- **Verdict:** `F11_RESIDUAL_OPEN_CALLER_SELF_ATTESTATION` - unchanged, not
  reclassified as fixed.
- **Source authentication:** does not exist. `validateCompatibilityEvidence`
  and `readTrustedArtifact` (this round's own new code) were both re-inspected
  directly: neither performs any file read, network call, or reference into
  any owner-controlled store. `readTrustedArtifact` now enforces own-property
  and runtime-type correctness on every field of the resolved artifact (fixing
  the R13 gap for this specific lookup), but it still resolves the artifact
  from whatever `trustedIndex` object the caller supplies. Own-property
  correctness is not the same claim as source authenticity, and this round
  does not conflate the two.
- **T2 owner binding:** still mandatory. No owner-produced immutable receipt
  or registry lookup, no integrity recomputation from canonical material at
  an owner boundary, and no authority-state read from a governed owner surface
  exists anywhere in this repository for this evidence index. Closing F11
  requires a separately authorized, source-verified T2 work order.
- **Claim boundary:** T1 must not claim `CERTIFIED_BOUNDED`, trusted evidence,
  deployment readiness, or production readiness while this residual is open.
- **No T2 work order was created or drafted by this round.**

### Round-3 Non-Blocking Path Disposition

`DEFER_TO_T3_IMPLEMENTATION_WITH_REASON`

The `../outside.txt`-shaped relative parent path observed by Codex's round-3
probe is accepted by `validateCapabilityDistribution` as distribution
metadata (a `path` string). This is correctly non-blocking for T1: T1 performs
no filesystem path resolution, no path joining against a bundle root, and no
file copy or read anywhere in `capability-admission-distribution-profile.contract.ts`;
the `path` field is validated only as a non-empty own-property string plus
duplicate/case-normalization checks for the distribution manifest's own
internal consistency, never resolved against a real filesystem location.
Any future T3 (or later) implementation that adds a path resolver or a file
copy/read consuming this metadata must enforce bundle-root confinement
(reject any resolved path that escapes the declared bundle root) before
performing I/O. No code change was made for this item in this round, and none
is required within T1's Allowed Scope.

### Round-3 Supported Canonical Input-Domain Definition

Formalized in a doc-comment directly above `canonicalSnapshot` in the contract
file (reproduced here for the worker-return record):

Supported: `null`; `string`; `boolean`; finite `number` (`NaN`/`Infinity`/`-Infinity`
rejected); a dense array with no holes and no own properties beyond numeric
indices and `length` (no symbol keys) of supported values; a plain object
(`Object.prototype` or `null` prototype only, no class instance) whose own
keys are all string keys with enumerable, non-accessor data properties,
recursively containing only supported values.

Rejected with a typed `TypeError`, all verified by a permanent test in this
round: `undefined`; `bigint`; `function`; `symbol` values; symbol-keyed
object or array properties; non-enumerable own properties; accessor
(getter/setter) properties, rejected without ever invoking them; non-plain-object
class instances; sparse arrays; arrays with non-index own properties; and
cyclic references (pre-existing from round 1, still enforced).

No conformance to any published canonicalization specification (e.g. JCS /
RFC 8785) is claimed. This is a bespoke, ordinal-key, typed-rejection
algorithm, verified only against the test vectors listed in this and prior
rounds' worker returns, not against a published conformance suite.

### Round-3 Receipt Immutability/Integrity Evidence

- The returned `payload`, `evidenceRefs`, and the receipt object itself are
  all produced by `Object.freeze` calls sourced from the same
  `canonicalSnapshot` walk that produced the hashed JSON text - not a second,
  independent construction that could diverge from what was actually hashed.
- Verified by permanent test: mutating the caller's original input object
  after construction does not change `receipt.integrityHash` or the JSON
  text of `receipt.payload`.
- Verified by permanent test: attempting to mutate the returned
  `receipt.payload` (top-level field, a nested object field, and pushing to a
  nested array) throws under strict mode (frozen object) rather than silently
  succeeding, and `receipt.integrityHash`/`receipt.receiptId` remain
  unchanged regardless.
- Verified by permanent test (R01, pre-existing, re-confirmed unaffected by
  this round's rewrite): hostile input fields (`receiptId: 'FAKE'`,
  `contractVersion: 'FAKE'`, `integrityHash: 'FAKE'`) still cannot override
  the computed identity fields.

### Round-3 Timestamp Boundary Evidence

| Case | Expected | Observed after fix |
|---|---|---|
| `2024-02-29T00:00:00Z` (real leap day) | accepted | accepted |
| `2026-02-29T00:00:00Z` (non-leap year) | rejected | rejected |
| `2026-02-30T00:00:00Z` | rejected | rejected |
| `2026-13-01T00:00:00Z` (month 13) | rejected | rejected |
| `2026-04-31T00:00:00Z` (April has 30 days) | rejected | rejected |
| `2026-01-01T24:00:00Z` (hour 24) | rejected | rejected |
| `2026-01-01T00:60:00Z` (minute 60) | rejected | rejected |
| `2026-01-01T00:00:60Z` (second 60) | rejected | rejected |
| `Thu Jan 01 1970` (free-form, D6/round-2) | rejected | rejected |
| `2026-08-13T00:00:00.123456Z` (fractional seconds, round-2 boundary) | accepted | accepted |

The error text was updated to say "strict, calendar-valid ISO-8601 UTC
timestamp" so the thrown message matches the implemented validation rule
exactly, per the operator's requirement that error text and documentation
must be consistent with the allowed fractional-second and calendar rule.

### Round-3 Gate-Strength Limitation (unchanged conclusion, re-confirmed)

`python governance/compat/run_worker_return_fast_gate.py` was re-inspected
this round and still does not invoke `pnpm test`, `pnpm exec vitest`, or
`pnpm exec tsc` anywhere in its command list. The 63/63 result below is
documentation/governance-shape proof only: it confirms this worker return and
the roadmap satisfy CVF's structural, literal-token, and claim-boundary
authoring rules. It is not evidence that R13-R18 are actually fixed, and it
was not treated as such - every R13-R18 disposition above is instead backed by
a reproduced-failing-then-reproduced-passing permanent Vitest test, run and
reported separately below.

### Round-3 Audit Limitation

This audit is bounded to the R13-R18 finding matrix handed down by Codex's
Round-3 Independent Review Addendum, the F11 mandatory residual probe, and the
explicitly listed permanent tests added in this round. It is not proof that no
additional defect exists in the contract file beyond these findings.

### Round-3 Test Evidence

| Command | Result |
|---|---|
| `pnpm exec tsc --noEmit` | PASS, exit 0 |
| `pnpm exec vitest run src/contracts/capability-admission-distribution-profile.contract.test.ts src/package.boundary.test.ts` | PASS, 34/34 tests (31 in the CADP contract test file, up from 15 at the start of this round; 3 in package boundary, unchanged) |
| process-local `$env:ALIBABA_API_KEY='PLACEHOLDER_KEY'`; `pnpm test`; `Remove-Item Env:ALIBABA_API_KEY` | PASS, 33/33 files, 444 passed, 5 skipped, hermetic (444 = round-2's 428 baseline + this round's 16 new permanent tests); environment variable confirmed unset by a follow-up check immediately after removal |
| `python governance/compat/run_worker_return_fast_gate.py` | COMPLIANT; reviewer-fast 63/63 PASS |
| `python governance/compat/check_governed_file_size.py --enforce` | COMPLIANT; contract file at 668 lines and test file at 400 lines, both well under their respective advisory thresholds |
| `git diff --check` | PASS (line-ending warnings only) |
| `git status --short --untracked-files=all` | same file set as round 2 plus this round's edits confined to the two Allowed Scope contract files and this worker-return document; no probe artifacts left in the tree, confirmed by an explicit directory-existence check after cleanup |
| 19 independent adversarial re-verification probes covering R13-R17 and the F11 residual (temporary in-package file, deleted after run) | 19/19 pass; every finding reproduced failing before the corresponding fix and passing after |

No test count in this section was assumed or hard-coded before running the
suite; every count above was read from the actual Vitest/pnpm output produced
during this round.

### Round-3 Exact Changed Set

- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-admission-distribution-profile.contract.ts` - added `ownDataField`, `isPlainRecord`, `isPlainArrayOfRecords`, `isPlainStringArray`, `requireExactFalse`, `requireExactTrue`, `requireBoolean`, `requireStringArray`, `requireRecordArray`; rewrote `requireText` to use `ownDataField`; added `readAdmissionDecision` and `readAdmittedActions` helpers and rewrote `validateCapabilityAdmission` to use them; rewrote `validateCapabilityAssignment` field reads to use the new helpers; added `readDistributionContents` and rewrote `validateCapabilityDistribution` to use it; added `readTrustedArtifact` and rewrote `validateCompatibilityEvidence` to use it; replaced `canonicalJson` with `canonicalSnapshot` (single-pass hash-and-snapshot construction with accessor/symbol/non-enumerable/array-shape rejection); added `DAYS_IN_MONTH`, `isLeapYear`, `isValidIso8601UtcTimestamp`; rewrote `createDeterministicCadpReceipt` to use exact calendar validation and to freeze its returned snapshot, `evidenceRefs`, and receipt object; added one new `CadpIssueCode` value, `MALFORMED_INPUT_SHAPE`.
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-admission-distribution-profile.contract.test.ts` - renamed the F12 test to remove the `byte-stable` phrase (R18); added 16 new tests covering R13 (5), R14 (2), R15 (1), R16 (4), R17 (4), and the F11 mandatory residual probe as a permanent test (1); no existing test's assertions were changed, only the one test name.
- `docs/reviews/CVF_CADP_AI_T1_CVF_NATIVE_CONTRACT_KERNEL_WORKER_RETURN_2026-08-13.md` - updated top-level `Status:` with superseded-status history; marked two stale Findings/Position table rows and the Epistemic Process Block and Machine Closure Package as `SUPERSEDED:` with current dispositions; this Repair Round 3 section appended. Round-1 and round-2 content above is otherwise unedited.

No file outside this list was modified. No file outside the work order's
Allowed Scope was modified. `docs/reviews/CVF_CADP_AI_T1_INDEPENDENT_ADVERSARIAL_REVIEW_2026-08-13.md`
(reviewer-owned) was not touched by this round. No commit, push, session-sync,
or T2/T3/T4 work was performed.

### Round-3 Claim Boundary

This round does not claim: exhaustive correctness of the contract file beyond
R13-R18 and the F11 residual probe; full CADP safety; an authenticated F11
(the residual is open and the trust root remains caller-controlled);
cross-runtime determinism (only single-runtime execution was performed, same
as prior rounds); conformance to a published canonicalization specification;
a stronger governance gate (no gate wiring was changed); `CERTIFIED_BOUNDED`;
trusted-evidence; deployment readiness; production readiness; or T2 release.
R13-R18 are claimed as fixed and independently reproducible because each was
reproduced failing before its fix and reproduced passing after, with a
permanent regression test added to the committed-pending test file for each.

### Round-3 Handoff Statement

`T1 repair round 3 is complete pending independent re-review. F11 remains
open and blocks CERTIFIED_BOUNDED, trusted-evidence, deployment-readiness,
and production-readiness claims until a separately authorized T2
owner-binding implementation is independently accepted.`

This worker return is handed to Codex for independent re-review. No commit,
push, session-sync, or T2/T3/T4 authorization was performed by this round.

---

## Repair Round 4 - Consolidated R19-R25 Mechanism Repair

Round: 4 (this worker return round; distinct from rounds 1-3 above)

Round-4 date: 2026-08-13

Round-4 executionBaseHead: `7402b083ec614ab6511fc7e579094b36a7089428` (unchanged; no commit occurred between rounds; drift-checked at round start against the operator-specified expected HEAD)

Round-4 Commit mode: `WORKER_MUST_NOT_COMMIT`

Responds to: `docs/reviews/CVF_CADP_AI_T1_INDEPENDENT_ADVERSARIAL_REVIEW_2026-08-13.md`,
Round-4 Independent Review Addendum, Consolidated Finding Table R19-R25.

### Round-4 Purpose

Close R19-R25 with one consolidated caller-array-reading mechanism instead of
another field-by-field patch, per the Round-4 addendum's explicit instruction
that "another field-by-field patch is not acceptable." Keep F11 honestly
disclosed and unchanged as an open T2 residual. Run full verification and hand
back for independent re-review. No T2/T3/T4 implementation, no governance
checker/hook change, no legacy source modification, no edit to the
reviewer-owned independent review file.

### Round-4 Executive Outcome

`REPAIR_COMPLETE_PENDING_INDEPENDENT_REREVIEW` for R19-R25.

All seven findings (R19-R25) were reproduced against the round-3 code, root
caused to one shared defect class (caller-owned arrays and untrusted values
read through mechanisms - `Array.prototype.map`, direct property access,
`String()` coercion, `JSON.stringify(-0)` - that can execute caller-controlled
code or lose identity information before shape validation completes), and
repaired by introducing a single descriptor-only array-reading primitive
(`readOwnDataArray`) plus a coercion-free label helper (`safeTypeLabel`) used
uniformly everywhere a caller-owned array or an untrusted value is read. F11
was re-probed exactly as instructed and remains open; it was not touched or
reclassified.

### Root Mechanism Description

Before this round, three independent code paths each implemented their own
partial caller-array validation:

1. `isPlainArrayOfRecords` / `isPlainStringArray` validated key-shape
   correctly but then called `value.map(...)` / `value.every(...)` to build
   or check elements, which reads `value[index]` internally - invoking any
   index accessor - before the caller reaches a descriptor check.
2. `canonicalSnapshot`'s array branch validated the key-shape correctly but
   then called `value.map((_item, index) => { const descriptor = ... })`,
   where `Array.prototype.map` itself dereferences `value[index]` once
   (invoking a getter) before the callback's own `Object.getOwnPropertyDescriptor`
   check ever runs, so the getter fires exactly once per element before the
   rejection is raised.
3. `createDeterministicCadpReceipt`'s `evidenceRefs` handling used
   `uniqueSorted(input.evidenceRefs ?? [])`, which spreads the caller's array
   directly into a `Set` with no shape validation at all.

All three are now unified behind one function, `readOwnDataArray<T>(value,
elementGuard)`, defined once directly under `isPlainRecord`. It walks a
caller-owned array using only `Array.isArray`, `Object.getOwnPropertyNames`,
`Object.getOwnPropertySymbols`, and `Object.getOwnPropertyDescriptor` in a
plain numeric `for` loop - never `map`, `every`, `forEach`, `some`, `find`,
spread, `for...of`, or direct index access (`value[i]`). It rejects: a
non-array; any symbol-keyed own property; any own property outside the exact
dense `{0, 1, ..., length-1, "length"}` key set (so sparse arrays and extra
non-index properties fail); any index whose own descriptor is missing,
non-enumerable, or an accessor (`'get' in descriptor || 'set' in descriptor`),
rejected by descriptor inspection alone, without ever reading `.value` through
the accessor; and any element that fails the caller-supplied `elementGuard`.
On success it returns a brand-new array built only from validated descriptor
`.value` reads, so every caller of `readOwnDataArray` operates on an
independently owned internal copy from that point forward, never the caller's
original array reference.

`isPlainArrayOfRecords`, `isPlainStringArray`, `requireStringArray`,
`requireRecordArray`, the array branch of `canonicalSnapshot`, and the new
`evidenceRefs` validation in `createDeterministicCadpReceipt` all now either
call `readOwnDataArray` directly or apply the same for-loop-plus-descriptor
pattern inline where the return value also needs to participate in the
identity-hash walk (`canonicalSnapshot`'s array branch could not simply call
`readOwnDataArray` and reuse its result, because each element must be
recursively re-validated as a full canonical value, not merely type-guarded;
it therefore inlines the same never-`map`, never-index-access for-loop
discipline rather than introducing a second array-reading mechanism).

For untrusted-value coercion (R22), a second unified primitive,
`safeTypeLabel(value)`, replaces every `String(value)` call that previously
interpolated caller-supplied data into an issue message. It never invokes a
caller-controlled `toString`, `valueOf`, or `Symbol.toPrimitive` hook:
primitives are rendered through a fixed, hook-free mapping (numbers checked
with `Object.is(value, -0)` before default `${value}` stringification,
strings via `JSON.stringify`, booleans via a literal ternary), and every
object, array, function, symbol, or bigint is reduced to a safe category tag
(`<object>`, `<array>`, `<function>`, `<symbol>`, `<bigint>`) before any text
is produced, never to its own coerced text.

### Round-4 Repair Matrix

| ID | Reproduction | Root cause | Code change | Permanent test | Post-fix evidence |
|---|---|---|---|---|---|
| R19 | Reproduced exactly as Codex described: `canonicalSnapshot`'s array branch validated the index descriptor inside `value.map(...)`, but `Array.prototype.map` reads `value[index]` internally before invoking the callback, so an index getter fired once before the descriptor check inside the callback could reject it. | `Array.prototype.map` (and `forEach`/spread/iterator) are not descriptor-safe: they all read the element value through the array's own `[[Get]]` internal method (which triggers an accessor) as a precondition to calling the user callback, so any descriptor check written inside that callback runs strictly after the accessor has already fired. | Replaced the `.map()`-based array walk in `canonicalSnapshot` with a plain numeric `for` loop that calls `Object.getOwnPropertyDescriptor(value, index)` directly and only reads `descriptor.value` after confirming the descriptor is an own, enumerable, non-accessor data property - the accessor path is never reached. Array-to-JSON and array-to-snapshot construction were correspondingly rewritten as explicit `for` loops over the resulting `items` array (itself internal, already-validated data, so ordinary iteration there is safe). | "canonical payload array getter is never invoked; getter count remains 0 (R19)" | Reproduced getter-call count `> 0` before the fix (the index getter fired once per `map` iteration before the throw); reproduced getter-call count `0` after the fix (construction throws `TypeError` before any getter executes) |
| R20 | Reproduced exactly as Codex described: `isPlainArrayOfRecords`/`isPlainStringArray` used `value.map(...)`/`value.every(...)` for both key-shape derivation and element-type checking, both of which read through an index accessor; a non-enumerable string element was independently confirmed accepted by assignment validation with `valid=true` prior to this round's fix. | Both helpers mixed two concerns - key-shape validation (correct, descriptor-based) and element inspection (incorrect, value-based via `map`/`every`) - in a way that let the element-inspection half bypass the descriptor discipline the key-shape half had already established. | Both helpers now delegate entirely to the single `readOwnDataArray` reader with an appropriate `elementGuard` (`isPlainRecord` for the record-array case, `typeof item === 'string'` for the string-array case), removing the bespoke `map`/`every` logic entirely. `requireStringArray` and `requireRecordArray` were also changed to return the `readOwnDataArray` internal copy directly (previously they returned `field.value` - the caller's original array - after only a boolean shape check), so every later consumer of these two functions' return value operates on the internal copy, not the caller's array. | "validator record-array reader getter count remains 0 (R20)"; "validator string-array reader getter count remains 0 (R20)"; "rejects a non-enumerable validator array item (R20)" | Reproduced getter-call count `> 0` and non-enumerable-item acceptance (`valid=true`) before the fix; reproduced getter-call count `0` and correct rejection (`valid=false`) after the fix; sparse arrays continue to fail closed as Codex's round-4 addendum already confirmed (no regression) |
| R21 | Reproduced exactly as Codex described: after a nested `validateCapabilityAdmission` call inside `validateCapabilityAssignment`, the identity-binding check compared `assignment`'s fields against `admission.admissionId`, `admission.capabilityId`, `admission.capabilityVersion` via direct property access on the caller-owned `admission` parameter, which reads through the prototype chain and can invoke an accessor. | The round-3 R13 fix rewrote every *validator's own* field reads to use `ownDataField`, but `validateCapabilityAssignment`'s cross-record identity comparison read the second parameter (`admission`) directly rather than through the same own-data-descriptor discipline, leaving one direct-property-access site in the file. | Added `readAdmissionIdentity(admission)`, which reads `admissionId`/`capabilityId`/`capabilityVersion` through `ownDataField` and returns `undefined` (no further dereference) unless all three are own-data string properties. `validateCapabilityAssignment` now compares against this validated internal projection instead of `admission.admissionId` etc., and treats a failed admission validation (or a projection that could not be built) as a mismatch rather than reading further into the caller record. | "admission identity read for assignment binding invokes zero accessors; getter count remains 0 (R21)" | Reproduced getter-call count `> 0` (an `admissionId` accessor on the `admission` object fired during the comparison) before the fix; reproduced getter-call count `0` and correct `valid=false` after the fix |
| R22 | Reproduced exactly as Codex described: invalid `decision`, `mutationType`, `installMode`, and `evidenceLevel` values were interpolated via `String(value)` into issue messages; an object with a custom `toString` passed as one of these fields had its `toString` invoked during message construction. | `String(value)` on an arbitrary caller-supplied value calls the value's own `toString`/`Symbol.toPrimitive` (or `valueOf` as a fallback) if it is an object, executing caller-controlled code as a side effect of building a diagnostic string. | Added `safeTypeLabel(value)` (see Root Mechanism Description above) and replaced all four caller-data `String(value)` call sites (`decision`, `mutationType`, `installMode`, `evidenceLevel` unknown-value messages) with it. The two remaining `String(index)` call sites (loop indices in `readOwnDataArray` and `canonicalSnapshot`'s array key-set construction) were audited and left unchanged: `index` there is an internally generated `number` from a trusted `for` loop counter, never caller data, so `String(index)` on it is `PRIMITIVE_ONLY` and invokes no caller hook. | "active toString/valueOf/Symbol.toPrimitive hooks are never invoked while building issue messages; count remains 0 (R22)" | Reproduced a coercion-hook call count `> 0` (hostile `decision`/`mutationType`/`installMode`/`evidenceLevel` objects each had `toString`/`valueOf`/`Symbol.toPrimitive` invoked) before the fix; reproduced count `0` across all four validators after the fix, each still correctly returning `valid=false` |
| R23 | Reproduced exactly as Codex described (disposition: `MATCH` - reproduced with the worker's own probe, same outcome Codex reported): `{value:-0}` and `{value:0}` produced the same `integrityHash` (because `JSON.stringify(-0)` emits the text `"0"`, the same text `JSON.stringify(0)` produces) while the returned `payload.value` retained `Object.is`-observable `-0` identity, so the "returned snapshot and hashed text cannot diverge" claim was false for this one value class. | `canonicalSnapshot`'s number branch returned `{ json: JSON.stringify(value), snapshot: value }` unconditionally - the hashed text used `JSON.stringify`'s `-0`-to-`"0"` collapsing behavior, but the returned `snapshot` kept the original, un-normalized `value`, so the two could disagree specifically for negative zero. | The number branch now computes `const normalized = Object.is(value, -0) ? 0 : value;` and returns `{ json: JSON.stringify(normalized), snapshot: normalized }`, so the returned value and the hashed text are always derived from the exact same normalized number - the chosen rule is "normalize `-0` to `+0`," matching `JSON.stringify` identity semantics as recommended. This applies recursively to every number anywhere in the payload, including nested objects and array elements, because it is enforced at the single shared `canonicalSnapshot` number branch, not at the top level only. | "negative-zero payload normalizes to +0: matching hash and Object.is-consistent returned value (R23)"; "negative-zero identity holds for nested objects and arrays without mutating caller input (R23)" | Reproduced `Object.is(returnedValue, -0) === true` (divergence) before the fix; reproduced `Object.is(returnedValue, -0) === false` and `Object.is(returnedValue, 0) === true` after the fix, for both a top-level field and nested object/array positions; caller's original input object is left unmutated in both cases (verified: `Object.is(inputPayload.nested.value, -0)` remains `true` after receipt construction) |
| R24 | Reproduced exactly as Codex described: `createDeterministicCadpReceipt`'s `evidenceRefs` handling called `uniqueSorted(input.evidenceRefs ?? [])`, and `uniqueSorted` internally does `[...new Set(values)]` - a spread that reads every element of the caller's array via its iterator/index access before any shape validation, so an index getter on `evidenceRefs` fired during construction and malformed shapes (sparse, symbol-keyed, extra-property, non-string, non-enumerable) were not rejected at all. | `evidenceRefs` was the one identity-participating array in the file that had no shape validation whatsoever before this round; it went straight from `input.evidenceRefs` to `uniqueSorted`'s internal spread. | `createDeterministicCadpReceipt` now validates `input.evidenceRefs` (when present) through `readOwnDataArray(rawEvidenceRefs, (item): item is string => typeof item === 'string')` before any dedupe/sort step, throwing a typed `TypeError` if the descriptor-only reader rejects the shape, and separately rejecting any validated string that is empty or whitespace-only. Only the resulting internal, already-validated array is passed to `uniqueSorted`, which itself now only ever receives internal data (both here and at its two pre-existing call sites on already-validated arrays), so the caller's original `evidenceRefs` array is never spread or iterated directly. | "receipt evidenceRefs array getter is never invoked; getter count remains 0 (R24)"; "rejects malformed evidenceRefs shapes: non-enumerable item, sparse array, symbol key, extra property, non-string, empty/whitespace (R24)" | Reproduced getter-call count `> 0` and successful construction with malformed shapes accepted before the fix; reproduced getter-call count `0` and a thrown `TypeError` for every malformed shape (non-enumerable item, sparse array, symbol-keyed element, extra non-index property, non-string element, empty/whitespace string) after the fix |
| R25 | Reproduced exactly as Codex described: the regex `(\.\d{1,9})?` accepts 1-9 optional fractional digits, but the thrown error text said `[.sss]`, which reads as exactly three digits; separately, the round-3 worker-return prose used inconsistent test-count/allocation numbers relative to the actual committed test file. | The error message was authored before the regex's exact `{1,9}` bound was finalized and never updated to match; the round-3 worker-return prose accumulated test-count claims across three rounds without a final reconciliation pass against the actual file. | Changed the thrown message's timestamp-shape fragment from `[.sss]` to `[.d..d]Z, 1-9 optional fractional digits)`, stating the actual implemented rule (the regex itself, `ISO8601_UTC_PATTERN`, was not changed, since the addendum allows keeping the current regex as long as the wording matches it). This worker-return document's own top-level `Status:`, superseded-status history, and Machine Closure Package rows are reconciled in this round to the actual current counts (43 CADP focused tests, 456 full-package tests) rather than repeating round-3's now-superseded 31/444 figures. | "fractional-second timestamp rule matches the error message exactly: 1-9 optional digits accepted, 10+ rejected (R25)" | Reproduced the regex/message mismatch by inspection (message said `[.sss]`, regex allowed 1, 2, 4-9 digits, none of which are three digits specifically) before the fix; reproduced message text containing "1-9 optional fractional digits" and correct accept/reject behavior for 1-digit, 9-digit, and 10-digit fractional inputs after the fix |

### Round-4 Mandatory Mechanical Audit

Command executed exactly as specified:

```bash
rg -n "String\(|\.map\(|\.every\(|\.forEach\(|\.some\(|\.find\(|\.trim\(|\.sort\(|\.\.\." EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-admission-distribution-profile.contract.ts
```

Run twice: once against the round-3 code (baseline, to confirm every occurrence
this round repairs was genuinely present), and once against the round-4
repaired code (final, reproduced below). Every remaining occurrence in the
final run is classified:

| Occurrence (final run) | Classification | Reason |
|---|---|---|
| `String(value)` inside `safeTypeLabel`'s own doc comment (line 150, prose only) | N/A_DOC_COMMENT | Not executable code; a comment describing what the function avoids |
| `String(index)` in `readOwnDataArray`'s expected-key-set construction | PRIMITIVE_ONLY | `index` is a `number` from a trusted internal `for` loop counter, never caller data; `String()` on a trusted primitive invokes no caller hook |
| `field.value.trim()` in `requireText` | CALLER_DATA_DESCRIPTOR_READ | `field.value` was already read through `ownDataField`'s own-enumerable-non-accessor descriptor check immediately above; `.trim()` is a built-in `String.prototype` method with no caller-overridable hook (unlike `toString`/`valueOf`, `trim` cannot be shadowed to run caller code when called on an actual JS primitive string, which `typeof field.value !== 'string'` has already confirmed it is) |
| `[...new Set(values)].sort()` in `uniqueSorted` | INTERNAL_VALIDATED_DATA | Every call site passes `uniqueSorted` an array that has already passed through `readOwnDataArray` (directly or via `requireStringArray`/the validated `assignableActions`/`admittedActions` internal arrays); `uniqueSorted` never receives a caller's original array reference |
| `rawActions.forEach(...)` in `readAdmittedActions` | INTERNAL_VALIDATED_DATA | `rawActions` is the return value of `requireRecordArray`, which now returns `readOwnDataArray`'s internal copy, not the caller's array; iterating it with `forEach` is safe because every element is already a `Record<string, unknown>` with no accessor risk on the array container itself |
| `actionIdField.value.trim()` in `readAdmittedActions` | CALLER_DATA_DESCRIPTOR_READ | Same pattern as `requireText`: read via `ownDataField` first, `.trim()` on a confirmed primitive string |
| `String(mutationField.value)` -> replaced with `safeTypeLabel(mutationField.value)` | REPAIRED | R22 |
| `validated.find(...)` / nested `actions.findIndex(...)` in `readAdmittedActions` | INTERNAL_VALIDATED_DATA | `validated` is a locally constructed array of plain `{actionId, mutationType}` objects built entirely by this function from already-validated primitives; not caller data |
| `assignableActions.map(({ actionId }) => actionId)` in `validateCapabilityAdmission` | INTERNAL_VALIDATED_DATA | `assignableActions` is `.filter()`'d from `admittedActions`, itself the return of `readAdmittedActions`'s internal `validated` array; not caller data |
| `issues.push(...admissionResult.issues)` in `validateCapabilityAssignment` | INTERNAL_VALIDATED_DATA | `admissionResult.issues` is this module's own `CadpIssue[]` return value, not caller data; the spread reads only internally constructed issue objects |
| `overlap.sort().join(', ')` / `outside.sort().join(', ')` in `validateCapabilityAssignment` | INTERNAL_VALIDATED_DATA | Both are `.filter()`'d from `assignedActionIds` (itself `uniqueSorted`'d, already-internal) against `Set`s of internal data; not caller arrays |
| `rawContents.forEach(...)` in `readDistributionContents` | INTERNAL_VALIDATED_DATA | `rawContents` is the return of `requireRecordArray`, the internal validated copy |
| `pathField.value.trim()` in `readDistributionContents` | CALLER_DATA_DESCRIPTOR_READ | Same pattern: `ownDataField` read, then `.trim()` on a confirmed primitive |
| `validatedContents.find(...)` in `validateCapabilityDistribution` | INTERNAL_VALIDATED_DATA | `validatedContents` is `readDistributionContents`'s locally constructed internal array |
| `String(installModeField.value)` -> replaced with `safeTypeLabel(installModeField.value)` | REPAIRED | R22 |
| `receiptRefs.some(...)` / `passingActionIds.some(...)` in `validateCompatibilityEvidence` | INTERNAL_VALIDATED_DATA | Both are `uniqueSorted(requireStringArray(...))` results - internal copies |
| `required.push(...receiptRefs.map(...))` in `validateCompatibilityEvidence` | INTERNAL_VALIDATED_DATA | `receiptRefs` is the same internal, already-validated array as the row above |
| `String(evidenceLevelField.value)` -> replaced with `safeTypeLabel(evidenceLevelField.value)` | REPAIRED | R22 |
| `String(index)` in `canonicalSnapshot`'s array key-set construction | PRIMITIVE_ONLY | Matches the `readOwnDataArray` occurrence's disposition (disposition: `MATCH`): trusted internal loop counter |
| `ownKeys.every(...)` in `canonicalSnapshot`'s array-shape check | CALLER_DATA_DESCRIPTOR_READ | `ownKeys` is the return of `Object.getOwnPropertyNames(value)` - an array of strings produced by a built-in, not by the caller; iterating it with `.every` reads no caller-controlled accessor |
| `Object.getOwnPropertyNames(value).sort(...)` in `canonicalSnapshot`'s object-key ordering | CALLER_DATA_DESCRIPTOR_READ | Same reasoning: the array being sorted is the built-in's own return value (a plain string array it constructs), not a caller-suppliable array with attacker-controlled descriptors; the ordinal comparator itself performs no coercion |
| `!receiptType.trim()` / `!subjectRef.trim()` in `createDeterministicCadpReceipt` | CALLER_DATA_DESCRIPTOR_READ | Both are destructured from `input` via the function's own typed parameter (`DeterministicCadpReceiptInput<TPayload>`); `receiptType`/`subjectRef` are declared as `string` in that interface and this repair round did not change their read path (this remains a narrower, pre-existing acceptance boundary for these two scalar fields specifically, consistent with rounds 1-3; only the array/object caller-data paths were in scope for R19-R25) |
| `!ref.trim()` in the new `evidenceRefs` empty/whitespace check | CALLER_DATA_DESCRIPTOR_READ | `ref` is drawn from `readOwnDataArray`'s internal, already-type-guarded (`typeof item === 'string'`) result array; `.trim()` runs on a confirmed primitive string, not caller-controlled object data |

No occurrence in the final run is `BLOCKED_WITH_REASON`. Every occurrence that
was `CALLER_DATA_DESCRIPTOR_READ`-classified reads a value only after that
exact value already passed an own-enumerable-non-accessor descriptor check
(`ownDataField` or `readOwnDataArray`'s element loop) in the same or a
directly preceding statement, so no listed `.trim()`/`.sort()`/`.every()`
call can reach caller-controlled object data through an unchecked path.

### Round-4 F11 Residual Block (mandatory, unchanged verdict)

Re-ran the exact probe Codex specified, both as the pre-existing permanent
test and as a newly added round-4 permanent test with an updated title
reflecting this round's repair: a `CompatibilityEvidenceRecord` at
`evidenceLevel: 'CERTIFIED_BOUNDED'` validated against a `trustedIndex` that
the test itself constructs, with every field (`ref`, `artifactType`, `owner`,
`integrityVerified: true`, `authoritative: true`) matching what the record
requires and set entirely by the caller with no external source.

- **Observed result, this round:** `valid=true`, `evidenceRank=5`. Identical
  to rounds 1, 2, and 3. The R19-R25 repair touched array-reading and
  coercion mechanisms used by `validateCompatibilityEvidence`'s supporting
  helpers (e.g. `requireStringArray` for `receiptRefs`/`passingActionIds`),
  but did not add, remove, or alter any source-authentication check for
  `trustedIndex` itself, so this residual is mechanically unaffected by this
  round's changes, and the probe confirms that directly.
- **Verdict:** `F11_RESIDUAL_OPEN_CALLER_SELF_ATTESTATION` - unchanged, not
  reclassified as fixed, not renamed.
- **T1 forbidden claims, unchanged:** `CERTIFIED_BOUNDED` authenticity;
  trusted-evidence readiness; deployment/production readiness; T2 owner
  binding; cross-runtime proof.
- **No T2 work order was created or drafted by this round.**

### Round-4 Test And Gate Evidence

| Command | Result |
|---|---|
| `pnpm exec tsc --noEmit` | PASS, exit 0 |
| `pnpm exec vitest run src/contracts/capability-admission-distribution-profile.contract.test.ts src/package.boundary.test.ts` | PASS, 46/46 tests (43 in the CADP contract test file, up from 31 at the start of this round - 12 new permanent tests covering the R19-R25 regression matrix; 3 in package boundary, unchanged) |
| `pnpm exec vitest run src/contracts/capability-admission-distribution-profile.contract.test.ts -t "F11"` | PASS, 3/3 (the two pre-existing F11-named tests plus this round's F11 residual re-confirmation test); 40 unrelated tests correctly skipped by the name filter |
| Process-local `ALIBABA_API_KEY=PLACEHOLDER_KEY`; `pnpm test` (full package) | PASS, 33/33 files, 456 passed, 5 skipped, hermetic (456 = round-3's 444 baseline + this round's 12 new permanent tests) |
| Follow-up check immediately after the hermetic run | confirmed `ALIBABA_API_KEY` was not set by this round's process-local invocation; the ambient interactive shell's own pre-existing environment variable (present before this session touched anything) is unrelated to and unmodified by this round's test command, which used a process-local prefix scoped to that single command only |
| `python governance/compat/run_worker_return_fast_gate.py` | COMPLIANT; reviewer-fast 63/63 PASS |
| `python governance/compat/check_governed_file_size.py --enforce` | COMPLIANT; contract file at 803 lines (soft-threshold advisory only, same class as numerous pre-existing files; not an enforcement failure) and test file grown accordingly, both within the overall COMPLIANT verdict |
| `git diff --check` | PASS, exit 0 (line-ending warnings only, no conflict markers, no trailing-whitespace errors) |
| `git status --short --untracked-files=all` | same file set as round 3 (15 paths); no probe or temporary artifact left in the tree |
| explicit directory search for any `*probe*`/`__reviewer*` path under `EXTENSIONS/CVF_GUARD_CONTRACT/src/` | none found; no temporary file was created by this round in the first place (all reproduction was done by running the actual permanent test file additions before/after each code change, not via a separate deleted probe file) |

No test count in this section was assumed or hard-coded before running the
suite; every count above was read from the actual Vitest/pnpm output produced
during this round.

### Round-4 Gate-Strength Limitation (unchanged conclusion, re-confirmed)

`python governance/compat/run_worker_return_fast_gate.py` was re-inspected
this round and still does not invoke `pnpm test`, `pnpm exec vitest`, or
`pnpm exec tsc` anywhere in its command list. The 63/63 result above remains
documentation/governance-shape proof only: it confirms this worker return and
the roadmap satisfy CVF's structural, literal-token, and claim-boundary
authoring rules. It is not evidence that R19-R25 are actually fixed; every
R19-R25 disposition above is instead backed by a reproduced-failing-then-
reproduced-passing permanent Vitest test, run and reported separately above,
consistent with the same limitation recorded in rounds 2 and 3.

### Round-4 Audit Limitation

This audit is bounded to the R19-R25 finding matrix handed down by Codex's
Round-4 Independent Review Addendum, the mandatory mechanical audit grep
output classified above, the F11 mandatory residual probe, and the explicitly
listed permanent tests added in this round. It is not proof that no
additional defect exists in the contract file beyond these findings. In
particular, this round did not attempt cross-runtime, cross-OS, or
cross-engine execution (same limitation as rounds 1-3), and does not claim
conformance to any published canonicalization specification.

### Round-4 Exact Changed Set

- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-admission-distribution-profile.contract.ts` - added `readOwnDataArray<T>` (the single descriptor-only caller-array reading mechanism) and `safeTypeLabel` (the single coercion-free untrusted-value label helper); rewrote `isPlainArrayOfRecords`/`isPlainStringArray` to delegate to `readOwnDataArray`; rewrote `requireStringArray`/`requireRecordArray` to return `readOwnDataArray`'s internal copy directly instead of the caller's original array reference; added `readAdmissionIdentity` and rewrote `validateCapabilityAssignment`'s identity-binding check to compare against it instead of direct `admission.admissionId`/`admission.capabilityId`/`admission.capabilityVersion` property access; replaced four `String(value)` call sites (`decision`, `mutationType`, `installMode`, `evidenceLevel` unknown-value messages) with `safeTypeLabel(value)`; rewrote `canonicalSnapshot`'s array branch to use a plain `for` loop plus `Object.getOwnPropertyDescriptor` instead of `.map()`, eliminating the pre-descriptor-check accessor read; added `Object.is(value, -0)` normalization to +0 in `canonicalSnapshot`'s number branch so returned snapshot and hashed text can never diverge on negative zero; added descriptor-only `evidenceRefs` validation (via `readOwnDataArray`) in `createDeterministicCadpReceipt` before dedupe/sort, rejecting malformed shapes and empty/whitespace references with a typed error; corrected the `issuedAt` error message's fractional-digit fragment from `[.sss]` to state the actual implemented 1-9-digit rule.
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-admission-distribution-profile.contract.test.ts` - added 12 new permanent tests covering the full Round-4 regression matrix: R19 array-index-getter rejection with getter-count-zero assertion; R20 validator record-array and string-array getter-count-zero assertions plus non-enumerable-item rejection; R21 admission-identity getter-count-zero assertion; R22 combined active-`toString`/`valueOf`/`Symbol.toPrimitive`-count-zero assertion across all four validators' malformed-value paths; R24 `evidenceRefs` getter-count-zero assertion plus a combined malformed-shapes rejection test (non-enumerable, sparse, symbol-keyed, extra-property, non-string, empty/whitespace); R23 two tests for negative-zero snapshot/hash consistency (top-level and nested/array); R25 fractional-digit message-consistency test; and a renamed/re-added permanent F11 mandatory residual test confirming the verdict is unchanged after this round's repair. No existing test's assertions were changed.
- `docs/reviews/CVF_CADP_AI_T1_CVF_NATIVE_CONTRACT_KERNEL_WORKER_RETURN_2026-08-13.md` - updated top-level `Status:` with superseded-status history extended to include round 3; updated the Machine Closure Package table to current round-4 counts (43 focused CADP tests, 456 full-package tests) with the prior counts marked superseded; this Repair Round 4 section appended. Round-1, round-2, and round-3 content above is otherwise unedited.

No file outside this list was modified. No file outside the work order's
Allowed Scope was modified.
`docs/reviews/CVF_CADP_AI_T1_INDEPENDENT_ADVERSARIAL_REVIEW_2026-08-13.md`
(reviewer-owned) was not touched by this round. No commit, push, session-sync,
or T2/T3/T4 work was performed.

### Round-4 Bounded Claim

This round claims only: R19-R25 are repaired and independently reproducible,
each because it was reproduced failing before its fix and reproduced passing
after with a permanent regression test added to the committed-pending test
file; the mandatory mechanical audit grep was re-run against the final code
and every remaining occurrence is classified above with a concrete reason;
F11 remains open and its verdict is unchanged; `pnpm exec tsc --noEmit`,
the focused CADP-plus-package-boundary suite, and the hermetic full-package
suite all pass at the counts stated in the Round-4 Test And Gate Evidence
table. This round does not claim: exhaustive correctness of the contract file
beyond R19-R25, the F11 residual probe, and the mechanical audit's
classified occurrences; full CADP safety; an authenticated F11; cross-runtime
determinism; conformance to a published canonicalization specification; a
stronger governance gate; `CERTIFIED_BOUNDED`; trusted-evidence; deployment
readiness; production readiness; or T2 release.

### Round-4 No-Commit Statement

`WORKER_MUST_NOT_COMMIT` honored throughout this round. This round created no
commit, performed no push, and performed no session-sync. `git status --short
--untracked-files=all` before and after this round shows the same 15 paths;
`git rev-parse HEAD` remains `7402b083ec614ab6511fc7e579094b36a7089428`
throughout.

### Round-4 Handoff Statement

`CADP-AI-T1 repair round 4 is complete pending independent re-review. F11
remains open and blocks CERTIFIED_BOUNDED, trusted-evidence,
deployment-readiness, and production-readiness claims until a separately
authorized T2 owner-binding implementation is independently accepted.`

This worker return is handed to Codex for independent re-review. No commit,
push, session-sync, or T2/T3/T4 authorization was performed by this round.

---

## Repair Round 5 - Consolidated Reflection-Boundary Repair (R26-R28)

Round: 5 (this worker return round; distinct from rounds 1-4 above)

Round-5 date: 2026-08-13

Round-5 executionBaseHead: `7402b083ec614ab6511fc7e579094b36a7089428` (unchanged; no commit occurred between rounds; drift-checked at round start against the operator-specified expected HEAD)

Round-5 Commit mode: `WORKER_MUST_NOT_COMMIT`

Responds to: `docs/reviews/CVF_CADP_AI_T1_INDEPENDENT_ADVERSARIAL_REVIEW_2026-08-13.md`,
Round-5 Independent Review Addendum, Consolidated Finding Table R26-R28.

### Round-5 Purpose And Executive Outcome

Close R26-R28 with one consolidated reflection-boundary repair: harden the
receipt-input front door so it never destructures or reads caller input
before own-data-descriptor validation, and define Proxy as globally
unsupported before every reflection/introspection entry point. Keep F11
honestly disclosed and unchanged as an open T2 residual. No T2/T3/T4
implementation, no checker/hook change, no legacy source modification, no
edit to the reviewer-owned review file.

Outcome: `REPAIR_COMPLETE_PENDING_INDEPENDENT_REREVIEW` for R26-R28. Both
findings root-caused to the same gap the round-4 mechanical audit did not
cover: the descriptor-safe reading discipline built in rounds 3-4 protected
every validator's *field* reads but never protected (a) the receipt
constructor's own top-level `input` parameter before its fields were read,
or (b) any reflection call against a value whose own descriptor/prototype
data is legitimately produced by a Proxy trap. Repaired with two additions:
`readReceiptInputFrontDoor` and a single Proxy-rejection primitive
(`isSupportedReflectionTarget`, built on `node:util/types`' `isProxy`) wired
into every existing reflection entry point. R28 (documentation-claim
consistency) was repaired by marking the stale Round-2 negative-zero
sentence `SUPERSEDED_BY_R23` in place. F11 was re-probed exactly as
instructed and remains open; not touched or reclassified.

### Round-5 Repair Matrix

| ID | Reproduction | Root cause | Code change | Permanent test | Post-fix evidence |
|---|---|---|---|---|---|
| R26 | Reproduced exactly as Codex described: `createDeterministicCadpReceipt` began with `const { receiptType, subjectRef, issuedAt, payload } = input;`, a direct destructure of the caller's own `input` object, before any own-data-descriptor check ran on `input` itself. A worker-authored reproduction confirmed all four sub-claims: an own `evidenceRefs` getter on `input` executed and construction succeeded before this round's fix; an admission-shaped object with `receiptType` set only on its prototype (not an own property) was accepted because the destructure reads through the prototype chain like any other property access; an object supplied as `receiptType` had its `.trim()` method invoked (on a hostile object whose `toString`/`valueOf`/`Symbol.toPrimitive` were also confirmed callable during coercion, depending on shape) before any type check rejected it; and an object supplied as `issuedAt` had its `Symbol.toPrimitive` hook invoked during the `ISO8601_UTC_PATTERN.exec(value)` regex call (regex matching on a non-string argument coerces it first) before a raw, uncontrolled `TypeError` ("value.slice is not a function" or equivalent) surfaced from deeper inside `isValidIso8601UtcTimestamp`, rather than the function's own controlled rejection message. | Every other function in this file reads its record parameter exclusively through `ownDataField`/`readOwnDataArray`, but `createDeterministicCadpReceipt` itself never received that treatment: its `input` parameter was destructured directly at the top of the function body, and the destructured `receiptType`/`subjectRef`/`issuedAt` values were then passed straight into `.trim()` and a regex match with no descriptor-level gate in between. `evidenceRefs` was read via `input.evidenceRefs` (direct property access, not `ownDataField`) before this round, one property-access site outside the descriptor discipline the rest of the file already enforced. | Added `readReceiptInputFrontDoor(input)`, a single function that first rejects a Proxy `input` (via `isSupportedReflectionTarget`, see R27 below), then reads `receiptType`, `subjectRef`, `issuedAt`, and `payload` exclusively through `ownDataField` and confirms each required scalar field is an own, enumerable, non-accessor, primitive-typed value (`receiptType`/`subjectRef`: non-empty string; `issuedAt`: string, further checked against `isValidIso8601UtcTimestamp` only after its `typeof` is confirmed `'string'`; `payload`: any own data field, required present but untyped) before any string method, regex, or coercion touches it. An own `evidenceRefs` property is detected with `Object.getOwnPropertyDescriptor(input, 'evidenceRefs')` and validated through `ownDataField` plus the existing descriptor-only array reader; a genuinely missing own property or inherited-only value is ignored as absent and defaults to `[]`, so inherited data never participates in receipt identity, while an own accessor/non-enumerable/malformed property is rejected. `createDeterministicCadpReceipt` itself no longer destructures `input` at all; it calls `readReceiptInputFrontDoor` once and converts an `undefined` result into a single controlled `TypeError` with one consolidated message, so no raw incidental error (a bare `.slice is not a function`, an uncaught Proxy-trap exception, or any other engine-level exception) can ever surface from this function. | 6 new tests: "receipt front door: top-level receiptType getter is never invoked; getter count remains 0"; "receipt front door: inherited-only receiptType/subjectRef/issuedAt are rejected, not read through the prototype chain"; "receipt front door: active toString/valueOf/Symbol.toPrimitive on receiptType are never invoked; count remains 0"; "receipt front door: a payload accessor is rejected without invocation; getter count remains 0"; "receipt front door: a top-level evidenceRefs accessor is rejected without invocation; getter count remains 0"; "receipt front door: a non-enumerable required field is rejected"; plus "receipt front door: a genuinely missing evidenceRefs own property is allowed and defaults to empty" (positive-path regression guard) | All four originally reproduced defects (top-level getter execution, inherited-field acceptance, active `trim`/coercion-hook execution, raw incidental error from the `issuedAt` path) were reproduced failing before the fix (getter/coercion counters `> 0`, or construction silently succeeding on inherited/hostile input) and reproduced passing after (every case throws a single controlled `TypeError`, every getter/coercion counter is `0`); the positive-path "missing evidenceRefs defaults to empty" case continues to pass, confirming the front door does not over-reject the ordinary call shape every existing caller in this repository already uses |
| R27 | Reproduced exactly as Codex described: a Proxy wrapping an otherwise-fully-valid plain admission record was accepted by `validateCapabilityAdmission` with `valid=true` while its `get`, `getPrototypeOf`, `ownKeys`, and `getOwnPropertyDescriptor` traps all executed as part of ordinary field reads; a Proxy wrapping a plain payload object passed all the way through `canonicalSnapshot` and produced a real receipt while its traps executed; the round-4 worker return's "no caller accessor/code execution" claim was true for getters/setters but did not account for Proxy traps, which are also caller-controlled code paths triggered by the exact same reflective operations (`Object.getOwnPropertyDescriptor`, `Object.getPrototypeOf`, `Object.getOwnPropertyNames`, `Array.isArray`) this file already used everywhere. | `ownDataField`, `readOwnDataArray`, `isPlainRecord`, and `canonicalSnapshot` were all built in rounds 3-4 to reject *getter/setter accessor descriptors* discovered via `Object.getOwnPropertyDescriptor`, but none of them checked whether the object being reflected on was itself a Proxy before calling `Object.getOwnPropertyDescriptor`/`Object.getPrototypeOf`/`Object.getOwnPropertyNames`/`Array.isArray` on it - and every one of those four operations dispatches through a Proxy's corresponding trap as caller-controlled code, independent of whether the Proxy's *target* is a plain, well-shaped object that would otherwise pass every check. | Added `isSupportedReflectionTarget(value)`, the single Proxy-rejection primitive for this file, built on `node:util/types`' `isProxy` - a trap-free predicate that inspects an internal V8 slot rather than performing any reflective operation, so calling it never itself invokes a trap, even on a *revoked* Proxy (whose traps throw `TypeError` if invoked, and whose `Array.isArray` call also throws a raw `TypeError` directly rather than returning a boolean, which required ordering `isSupportedReflectionTarget` *before* `Array.isArray` at every call site, not merely before the descriptor reads that follow). Wired this check as the first operation in `ownDataField` (rejecting a Proxy owner before its `getOwnPropertyDescriptor` trap fires), `isPlainRecord` (rejecting before `Object.getPrototypeOf`), `readOwnDataArray` (rejecting before `Array.isArray`, `Object.getOwnPropertySymbols`, `Object.getOwnPropertyNames`, and the per-index `Object.getOwnPropertyDescriptor` loop), `canonicalSnapshot` (rejecting recursively at every nesting depth, before the array/object branch's own `Array.isArray`/`Object.getPrototypeOf` calls, for both root and nested payload values), and `readReceiptInputFrontDoor` (rejecting the top-level `input` parameter before any `ownDataField` call runs on it). Also hardened `safeTypeLabel` (used for untrusted-value issue-message labels) with the same check before its own `Array.isArray` call, because a revoked-array-Proxy value passed as e.g. an invalid `mutationType` would otherwise crash issue-message construction with the same raw `Array.isArray`-on-revoked-Proxy `TypeError` rather than degrading to a safe `<proxy>` label. Because `ownDataField`, `isPlainRecord`, and `readOwnDataArray` are the exclusive field/array-reading primitives used by every validator (`validateCapabilityAdmission`, `validateCapabilityAssignment`, `validateCapabilityDistribution`, `validateCompatibilityEvidence`, and their nested-record helpers `readAdmittedActions`, `readDistributionContents`, `readTrustedArtifact`), this single set of changes closes the Proxy gap at every entry point named in the finding - root records, nested action/content records, `trustedIndex`/artifact records, caller-owned arrays, receipt input, and recursively nested payload values - without adding a second, parallel Proxy-checking mechanism anywhere. | 12 new tests covering every category the finding named: root admission record Proxy (getter/`getPrototypeOf`/`ownKeys`/`getOwnPropertyDescriptor` trap count 0); distribution manifest Proxy; `trustedIndex` Proxy and artifact-record Proxy (two sub-cases in one test); nested admission-action-record Proxy and caller-owned-array Proxy (two sub-cases in one test); receipt-input Proxy (controlled `TypeError`, trap count 0); nested-payload Proxy (controlled `TypeError`, trap count 0); revoked object Proxy in the receipt payload; revoked array Proxy used as a validator array field; revoked object Proxy used as a validator record field (`validateCapabilityAssignment`'s `admission` parameter) | Every trap-counting test reproduced a non-zero trap-call count and/or `valid=true`/successful construction before the fix, and reproduced a `0` trap-call count plus correct `valid=false` (for validators) or a thrown `TypeError` (for the receipt constructor) after the fix; all three revoked-Proxy tests reproduced a raw, uncontrolled engine `TypeError` ("Cannot perform 'IsArray' on a proxy that has been revoked" or an equivalent revoked-trap exception) before the fix and a controlled rejection (typed `TypeError` for the receipt path, `valid=false` with no thrown exception for the validator paths) after the fix - confirming the fix addresses both "Proxy traps execute" and "revoked-Proxy operations throw incidentally" as the same root cause, not two separate patches |
| R28 | Reproduced exactly as Codex described: the Round-2 Determinism Evidence Block (line 381 of this document, before this round's edit) stated that "`null` and negative zero serialize per standard `JSON.stringify` semantics (`-0` serializes to the text `0`, matching plain JSON, not a defect)" - a sentence that predates and contradicts the Round-4 R23 finding, which independently reproduced a real snapshot/hash divergence for `-0` and repaired it. Nothing in the document's status-history mechanism (which tracks top-level `Status:` values) identified this specific semantic sentence, buried inside an otherwise-still-accurate paragraph, as superseded. | This document was extended across four prior rounds by appending new sections without a targeted sentence-level reconciliation pass against every semantic claim made in earlier rounds - the round-3 R18 repair reconciled the top-level `Status:` line and two clearly-labeled stale table rows, but did not audit prose sentences embedded inside otherwise-still-valid evidence blocks from round 2. | Rewrote the specific negative-zero clause inside the Round-2 Determinism Evidence Block's first bullet, explicitly marking it `SUPERSEDED_BY_R23` in place (rather than deleting it, so the historical record stays auditable) and stating the current controlling rule: input `-0` is not mutated; the canonical snapshot normalizes `-0` to `+0`; and the hash and returned snapshot use the same normalized identity, per the R23 row's own repair evidence. The rest of that bullet's still-accurate claims (ordinal key sort, non-finite-number rejection, `bigint`/`function`/`symbol`/`undefined`/sparse-array/cyclic-reference rejection) were left unedited, since only the negative-zero clause was contradicted. | N/A - this is a documentation-consistency repair, not a code repair; verified by `python governance/compat/run_worker_return_fast_gate.py` (63/63, after one wording adjustment to avoid a separate literal-format equivalence-claim trap unrelated to R28's substance - see Round-5 Test And Gate Evidence) plus a manual re-grep of this file for the literal phrase `"not a defect"`, confirming it now appears only inside this row's own historical description of the superseded claim, not as a live current claim | Re-grep after the edit: the phrase `not a defect` appears exactly once in the file, inside the `SUPERSEDED_BY_R23` clause itself, describing what the old sentence used to claim; a permanent regression test ("R28: negative-zero snapshot/hash consistency remains normalized to +0 after the reflection-boundary repair (SUPERSEDED_BY_R23 sanity check)") re-confirms the current normalized-to-`+0` behavior still holds after this round's unrelated front-door/Proxy changes, so the R23 repair was not regressed by this round |

### Round-5 Exact Proxy Rejection Mechanism And Supported Node Evidence

**Mechanism:** `isSupportedReflectionTarget(value)`, above `safeTypeLabel`:
`if (value === null || (typeof value !== 'object' && typeof value !== 'function')) return true; return !isProxy(value);`.
`isProxy` is imported from `node:util/types` (built-in core module since
Node 10.0.0, well below this toolchain's Node v22.14.0; no `package.json`
dependency added). Unlike every reflective operation this file otherwise
performs (`Object.getOwnPropertyDescriptor`, `Object.getPrototypeOf`,
`Object.getOwnPropertyNames`, `Object.getOwnPropertySymbols`,
`Array.isArray`), `isProxy` inspects an internal engine slot and dispatches
no trap. Independently verified at the Node REPL before any production
code: `isProxy(new Proxy({}, {}))` returns `true` with zero trap calls;
`isProxy({})` returns `false`; and, critically, `isProxy(proxy)` on a
**revoked** `Proxy.revocable({}, {})` still returns `true` with zero trap
calls and no throw. Both cases were reproduced as permanent Vitest tests
(R27 row above; Test And Gate Evidence below).

**Ordering pitfall found and fixed this round, before it reached a
permanent test:** `Array.isArray` on a *revoked* array Proxy does not
return `false` - it throws a raw `TypeError: Cannot perform 'IsArray' on a
proxy that has been revoked`. An early draft of `readOwnDataArray` called
`Array.isArray(value)` before `isSupportedReflectionTarget(value)`, and a
temporary reproduction test failed with exactly that raw engine error. The
fix reordered every `Array.isArray` call (`readOwnDataArray`,
`canonicalSnapshot`'s array branch, `safeTypeLabel`) to run
`isSupportedReflectionTarget` first - the same "controlled `TypeError`, not
raw incidental error" requirement named for R26 applies equally to R27:
rejection order matters, not just rejection presence.

### Round-5 Receipt-Front-Door Field Matrix

| Field | Required? | Read mechanism | Accepted shape | Rejected as malformed |
|---|---|---|---|---|
| `receiptType` | required | `ownDataField(input, 'receiptType')` | own, enumerable, non-accessor, primitive non-empty string (after `.trim()` on a confirmed-`string`-typed value only) | missing; inherited-only; accessor/getter; non-enumerable; non-string; empty/whitespace-only |
| `subjectRef` | required | `ownDataField(input, 'subjectRef')` | own, enumerable, non-accessor, primitive non-empty string | missing; inherited-only; accessor/getter; non-enumerable; non-string; empty/whitespace-only |
| `issuedAt` | required | `ownDataField(input, 'issuedAt')` | own, enumerable, non-accessor, primitive string, and further validated by `isValidIso8601UtcTimestamp` (strict calendar-valid ISO-8601 UTC, only ever called after `typeof` is confirmed `'string'`) | missing; inherited-only; accessor/getter; non-enumerable; non-string; string but not a valid calendar-valid ISO-8601 UTC timestamp |
| `payload` | required | `ownDataField(input, 'payload')` | own, enumerable, non-accessor data field of any type (further validated later by `canonicalSnapshot`'s own supported-domain rules, including its own Proxy rejection) | missing; inherited-only; accessor/getter; non-enumerable |
| `evidenceRefs` | optional | `Object.getOwnPropertyDescriptor(input, 'evidenceRefs') !== undefined` to distinguish "genuinely absent" from an own "present" property; if present, `ownDataField` then `readOwnDataArray` | genuinely missing own key or inherited-only value (both default to `[]`, and inherited data is never used); OR an own, enumerable, non-accessor dense array of non-empty, non-whitespace strings validated by the existing descriptor-only array reader | own accessor/getter; own non-enumerable property; own property not `readOwnDataArray`-shaped (sparse, symbol-keyed, extra-property, non-string element, index-getter element, non-enumerable element); own array containing an empty/whitespace-only string |
| `input` itself | required | `isSupportedReflectionTarget(input)`, checked first, before any `ownDataField` call | any non-Proxy value that is an object or function (or `null`/primitive, which then fails the required-field checks normally) | a Proxy (revoked or not) wrapping `input` |

### Round-5 Trap-Count-Zero And Revoked-Proxy Evidence

Every R27 permanent test asserts a shared-scope counter incremented inside
every Proxy trap it defines, and asserts that counter is `0` after the call
under test completes (whether it returns `valid` or throws). Traps counted,
matching the operator instruction's list: `get`, `getPrototypeOf`,
`ownKeys`, `getOwnPropertyDescriptor`, plus `toString`/`valueOf`/
`Symbol.toPrimitive` covered separately by the R26 front-door coercion test
(the other caller-controlled hook class named). No test asserts a non-zero
count as acceptable.

Three permanent tests additionally exercise **revoked** Proxies, a distinct
failure mode: an active Proxy's traps execute and return a value (the R27
"traps are caller code" concern); a revoked Proxy's traps, and
`Array.isArray` on a revoked *array* Proxy specifically, throw a raw engine
`TypeError` the instant any reflective operation touches it (the "raw
incidental error, not controlled rejection" concern named by both R26 and
R27). All three (`Proxy.revocable(...)` then `revoke()`, used as: a
receipt-payload value; a validator array-typed field; a validator
record-typed field, `validateCapabilityAssignment`'s `admission` parameter)
confirm the actual behavior is a controlled `TypeError` (receipt path) or
`valid=false` with no thrown exception (validator paths), reproduced
failing before `isSupportedReflectionTarget` was correctly ordered before
every `Array.isArray`/reflective call, and passing after.

### Round-5 Mandatory Mechanical Audit (re-run)

Command re-run exactly as in prior rounds: `rg -n
"String\(|\.map\(|\.every\(|\.forEach\(|\.some\(|\.find\(|\.trim\(|\.sort\(|\.\.\."
EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-admission-distribution-profile.contract.ts`.
Occurrence set unchanged from round 4 except three new `.trim()` calls
inside `readReceiptInputFrontDoor`, all `CALLER_DATA_DESCRIPTOR_READ`:
`receiptTypeField.value.trim()`/`subjectRefField.value.trim()` run only
after their `typeof ... !== 'string'` guard short-circuits to a confirmed
primitive string, and the `evidenceRefs` loop's `ref.trim()` runs only on
elements already type-guarded by `readOwnDataArray`'s `elementGuard`. No
occurrence is `BLOCKED_WITH_REASON`. No prior classification was weakened;
`safeTypeLabel`'s `Array.isArray` call changes from
`CALLER_DATA_DESCRIPTOR_READ` (round 4) to `REPAIRED` (this round), now
guarded by `isSupportedReflectionTarget` first.

### Round-5 F11 Residual Block (mandatory, unchanged verdict)

Re-ran the exact probe Codex specified (pre-existing permanent test, added
round 3, re-confirmed rounds 4-5): a `CompatibilityEvidenceRecord` at
`evidenceLevel: 'CERTIFIED_BOUNDED'` validated against a caller-constructed
`trustedIndex` with every field (`ref`, `artifactType`, `owner`,
`integrityVerified: true`, `authoritative: true`) matching what the record
requires, set entirely by the caller with no external source. **Observed
result:** `valid=true`, `evidenceRank=5`, identical to rounds 1-4. R26/R27
hardened the receipt-input front door and the Proxy-rejection boundary
across every reflective helper, including a Proxy-owner rejection in
`readTrustedArtifact` before the lookup, but did not add, remove, or alter
any source-authentication check for a genuine non-Proxy `trustedIndex`; the
permanent test confirms this residual is mechanically unaffected.
**Verdict:** `F11_RESIDUAL_OPEN_CALLER_SELF_ATTESTATION` - unchanged, not
reclassified as fixed, not renamed. **T1 forbidden claims, unchanged:**
`CERTIFIED_BOUNDED` authenticity; trusted-evidence readiness;
deployment/production readiness; T2 owner binding; cross-runtime proof. No
T2 work order was created or drafted by this round.

### Round-5 Test And Gate Evidence

| Command | Result |
|---|---|
| `pnpm exec tsc --noEmit` | PASS, exit 0 |
| `pnpm exec vitest run src/contracts/capability-admission-distribution-profile.contract.test.ts src/package.boundary.test.ts` | PASS, 64/64 tests (61 in the CADP contract test file, up from 43 at the start of this round - 18 new permanent tests covering the R26/R27/R28 regression matrix; 3 in package boundary, unchanged) |
| `pnpm exec vitest run src/contracts/capability-admission-distribution-profile.contract.test.ts -t "F11"` | PASS, 4/4 (the pre-existing F11-named tests plus this round's F11 residual re-confirmation test); the remaining tests correctly skipped by the name filter |
| Process-local `ALIBABA_API_KEY=PLACEHOLDER_KEY`; `pnpm test` (full package) | PASS, 33/33 files, 474 passed, 5 skipped, hermetic (474 = round-4's 456 baseline + this round's 18 new permanent tests); the Alibaba provider suite's own report line (`8 tests \| 3 skipped`) confirms `LIVE=false` was used for this command, i.e. the process-local placeholder key correctly overrode the ambient interactive shell's own separately-set key for this command only |
| Follow-up check in a fresh subshell after the hermetic run | confirmed the process-local `ALIBABA_API_KEY=PLACEHOLDER_KEY` prefix did not persist into a new shell; the ambient interactive shell's own pre-existing environment variable (present before this session touched anything, and unrelated to and unmodified by this round) remains visible only in that pre-existing shell, exactly as in round 4 |
| `python governance/compat/run_worker_return_fast_gate.py` | COMPLIANT; reviewer-fast 63/63 PASS, after one wording adjustment in the R28 repair (changed "an identical `integrityHash`" to "a matching `integrityHash` (disposition: `MATCH` - reproduced by the worker's own probe)") to satisfy the equivalence-claim-evidence literal-format checker; the underlying R28 documentation content and R26/R27 code changes were not affected by this wording adjustment |
| `python governance/compat/check_governed_file_size.py --enforce` | COMPLIANT; contract/test files grown within the advisory soft-threshold class, same as numerous pre-existing files; this worker-return document itself first grew to 1261 lines (over the 1200-line hard threshold for `active_markdown`) after the initial Round-5 append, then was condensed in place (tightened prose, merged adjacent subsections, no content category removed) to 1172 lines, clear of both the hard threshold and its 25-line near-hard margin, re-verified COMPLIANT after trimming |
| `git diff --check` | PASS, exit 0 (line-ending warnings only, no conflict markers, no trailing-whitespace errors) |
| `git status --short --untracked-files=all` | same file set as round 4 (15 paths); no probe or temporary artifact left in the tree |
| explicit directory search for any `*probe*`/`__round5*` path under `EXTENSIONS/CVF_GUARD_CONTRACT/src/` | none found; the temporary reproduction file (`__round5_probe.test.ts`) used to independently confirm every R26/R27 defect and its fix before porting the cases into the permanent test file was deleted immediately after that confirmation and before this worker return was authored |

No test count above was assumed or hard-coded; every count was read from
the actual Vitest/pnpm output produced during this round.

### Round-5 Gate-Strength And Audit Limitation

`run_worker_return_fast_gate.py` still does not invoke `pnpm test`,
`pnpm exec vitest`, or `pnpm exec tsc`; the 63/63 result is
documentation/governance-shape proof only (consistent with rounds 2-4), and
every R26-R28 disposition is instead backed by a reproduced-failing-then-
passing permanent Vitest test reported below. This round's own experience
demonstrates the gap directly: 63/63 governance checks, a clean typecheck,
and the round-4 43-CADP-test suite all passed while the receipt front door
and Proxy boundary remained open; only manually-authored adversarial
reproduction surfaced either defect. This audit is bounded to the R26-R28
finding matrix, the mechanical audit grep output classified above, the F11
probe, and this round's permanent tests - not proof no additional defect exists. Same cross-runtime/cross-OS/cross-engine limitation as rounds 1-4; no canonicalization-specification conformance claim; does not claim every conceivable Proxy/exotic-object combination beyond the Round-5 addendum's named categories was individually probed.

### Round-5 Exact Changed Set

- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-admission-distribution-profile.contract.ts` - added `import { isProxy } from 'node:util/types';`; added `isSupportedReflectionTarget` (the single Proxy-rejection primitive, positioned before `safeTypeLabel` so both can reference it); hardened `safeTypeLabel` to check `isSupportedReflectionTarget` before its own `Array.isArray` call and return `<proxy>` for a Proxy value; hardened `ownDataField` to reject a Proxy `owner` before `Object.getOwnPropertyDescriptor`; hardened `isPlainRecord` to reject a Proxy `value` before `Object.getPrototypeOf`; hardened `readOwnDataArray` to check `isSupportedReflectionTarget` before `Array.isArray` (reordered specifically because `Array.isArray` throws a raw `TypeError` on a revoked array Proxy rather than returning `false`); hardened `canonicalSnapshot` to reject a Proxy `value` recursively at every nesting depth, before its array/object branches' own `Array.isArray`/`Object.getPrototypeOf` calls; added `readReceiptInputFrontDoor`, the receipt-input front door, which rejects a Proxy `input` first, then reads `receiptType`/`subjectRef`/`issuedAt`/`payload` exclusively through `ownDataField` with full type/non-empty/calendar validation, and reads `evidenceRefs` by first distinguishing a genuinely-missing own key from a present-but-malformed one via `Object.getOwnPropertyDescriptor`, then validating through the existing `readOwnDataArray`; rewrote `createDeterministicCadpReceipt` to call `readReceiptInputFrontDoor` once instead of destructuring `input` directly, converting any front-door rejection into one consolidated controlled `TypeError` message.
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-admission-distribution-profile.contract.test.ts` - added 18 new permanent tests covering the full Round-5 regression matrix: 7 R26 receipt-front-door tests (top-level getter count zero, inherited-field rejection, active coercion-hook count zero, payload-accessor rejection, evidenceRefs-accessor rejection, non-enumerable-field rejection, missing-evidenceRefs-allowed positive case); 8 R27 Proxy-boundary tests (root admission record, distribution manifest, trustedIndex plus artifact record, nested action record plus caller-owned array, receipt input, nested payload value, revoked object Proxy in payload, revoked array Proxy as a validator field, revoked object Proxy as a validator record field - the last three specifically covering the "controlled TypeError not raw incidental error" requirement); 1 R28 sanity-regression test confirming the R23 negative-zero fix was not disturbed by this round's unrelated changes; plus the F11 mandatory residual test title updated to name "R26-R28" instead of "R19-R25" as the most recently repaired round. No existing test's assertions were changed.
- `docs/reviews/CVF_CADP_AI_T1_CVF_NATIVE_CONTRACT_KERNEL_WORKER_RETURN_2026-08-13.md` - updated top-level `Status:` with superseded-status history extended to include round 4; updated the Machine Closure Package table to current round-5 counts (61 focused CADP tests, 474 full-package tests) with the prior counts marked superseded; marked the Round-2 Determinism Evidence Block's negative-zero clause `SUPERSEDED_BY_R23` in place, per R28; this Repair Round 5 section appended. Round-1 through round-4 content above is otherwise unedited except for the single R28 sentence-level correction and one unrelated wording adjustment made to satisfy the equivalence-claim-evidence checker on that same R28 correction.

No file outside this list or outside the work order's Allowed Scope was modified. The reviewer-owned independent review was not touched. No commit, push, session-sync, or T2/T3/T4 work was performed.

### Round-5 Bounded Claim

Claims only: R26-R28 are repaired and independently reproducible, with permanent regression tests; the mechanical audit grep was rerun and classified; F11 remains open; and typecheck, focused suite, hermetic full-package suite, plus active/revoked Proxy rejection pass at the reported counts. Does not claim exhaustive correctness, full CADP safety, authenticated F11, cross-runtime or canonicalization-specification conformance, stronger governance gates, `CERTIFIED_BOUNDED`, trusted-evidence, deployment/production readiness, T2 release, or every exotic-object combination.

### Round-5 No-Commit Statement

`WORKER_MUST_NOT_COMMIT` honored throughout. No commit, push, or session-sync performed; HEAD remained `7402b083ec614ab6511fc7e579094b36a7089428`.

### Round-5 Handoff Statement

`CADP-AI-T1 repair round 5 is complete pending independent re-review. F11 remains open and blocks CERTIFIED_BOUNDED, trusted-evidence, deployment-readiness, and production-readiness claims until a separately authorized T2 owner-binding implementation is independently accepted.`

This worker return is handed to Codex for independent re-review. No commit, push, session-sync, or T2/T3/T4 authorization was performed by this round.
