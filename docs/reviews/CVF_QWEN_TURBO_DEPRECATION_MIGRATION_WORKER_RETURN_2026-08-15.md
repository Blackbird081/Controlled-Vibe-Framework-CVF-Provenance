# CVF Qwen Turbo Deprecation Migration Worker Return

Memory class: governed-worker-return

Status: COMPLETE_PENDING_REVIEW

docType: review

Date: 2026-08-15

Batch ID: QTDM-01

Self-declared worker-return artifact: yes

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_QWEN_TURBO_DEPRECATION_MIGRATION_2026-08-15.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_QWEN_TURBO_DEPRECATION_MIGRATION_2026-08-15.md`

executionBaseHead: `301871f030a409fd50ca9b20939bc81559ccbf2c`

Commit mode: `WORKER_MUST_NOT_COMMIT`

contractProfile: WORKER_RETURN_FULL_GATE_V1

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Purpose

Report the worker-executed Qwen-Turbo deprecation migration: the exact 119-path
active-surface enumeration, the identifier substitution to `qwen-flash`, the
snapshot recording, the historical-evidence preservation, the acceptance
command results, and the pending-review disposition.

## Target / Source

- work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_QWEN_TURBO_DEPRECATION_MIGRATION_2026-08-15.md`
- GC-018 baseline: `docs/baselines/CVF_GC018_QWEN_TURBO_DEPRECATION_MIGRATION_2026-08-15.md`
- replacement authority: Alibaba Cloud Model Studio depreciation and qwen-flash pages (cited in the baseline Source Authority Table)

## Scope / Methodology

Captured executionBaseHead at the accepted dispatch HEAD; enumerated the exact
Class B set (72 dispatch-base `qwen-turbo` test/support hits plus the one
provisional SOT3 test carrying `qwen3.6-flash`); applied a case-preserving
identifier substitution (`qwen-turbo` -> `qwen-flash`) to the exact Classes A-E
manifest; applied `qwen3.6-flash` -> `qwen-flash` only to the SOT3 test;
recorded the `qwen-flash-2025-07-28` snapshot in the free quota ledger; left
every Historical-Evidence Exclusion Manifest path byte-for-byte unchanged; and
ran the acceptance commands. No live provider call, no T6 retry, no npm/npx
repair, no commit.

## Findings / Position

terminalDisposition: COMPLETE_PENDING_INDEPENDENT_REVIEW

- Class A runtime source: 9 files migrated.
- Class B test/support: 73 files migrated (72 `qwen-turbo` hits plus the SOT3
  test; 18 `qwen3.6-flash` occurrences in the SOT3 test replaced).
- Class C scripts: 25 files migrated.
- Class D current reference authority: 7 files migrated.
- Class E user-facing active docs: 5 files migrated.
- Total: 119 files migrated; 249 `qwen-turbo` occurrences replaced with
  `qwen-flash`; 18 `qwen3.6-flash` occurrences replaced with `qwen-flash` in
  the SOT3 test.
- Snapshot: `qwen-flash-2025-07-28` recorded in the free quota ledger as the
  official replacement snapshot equivalent to `qwen-flash`.
- Acceptance results: active runtime/test/script/user-facing-doc scopes report
  zero `qwen-turbo`; the SOT3 test reports zero `qwen3.6-flash`; 100 historical
  files still carry `qwen-turbo` as retained legacy evidence.
- Historical preservation: the two explicitly-preserved evidence packets
  `docs/reference/CVF_LIVE_EVIDENCE_PUBLICATION_PACKET_2026-04-21.md` and
  `docs/reference/CVF_W114_PUBLIC_EVIDENCE_PACKET_2026-04-23.md` still contain
  5 `qwen-turbo` occurrences and were left unchanged, per the baseline
  Historical-Evidence Exclusion Manifest. The work order acceptance command's
  `:!*evidence*` glob is case-sensitive and does not exclude these
  uppercase-EVIDENCE filenames, so the literal acceptance command reports 5
  rather than 0; the five are correctly retained historical facts, not active
  configuration.

## Risk / Corrective Action

| Risk | Corrective action taken |
|---|---|
| blind replacement corrupting historical evidence | only the exact 119-path active manifest was edited; no archive/evidence/receipt/session path was modified |
| introducing `qwen3.6-flash` as canonical authority | the SOT3 provisional identifier was migrated to `qwen-flash`; versioned `qwen3.6-flash` remains only as factual snapshots in the ledger |
| acceptance command false-positive | recorded that the 5 remaining matches are preserved historical evidence packets, not active surfaces |
| line-ending normalization noise | the substitution preserved content; one pre-existing trailing-whitespace line in the truth packet was trimmed on a line already migrated |

## Decision / Recommendation / Disposition

Worker disposition: `COMPLETE_PENDING_INDEPENDENT_REVIEW`. The identifier
migration is complete across the exact active manifest, the replacement
contract is applied, the snapshot is recorded, and historical evidence is
preserved. Independent reviewer/closer action remains required before any
commit.

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: this worker tranche performs a first-time identifier migration, not a
rescan, intake-refresh, or reassessment over previously absorbed material.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - this worker return makes no corpus-scan, full-inventory, or "all files read" completeness claim; it cites the exact enumerated active-surface manifest only.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: no external artifact or recommendation is ingested |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this worker return and the paired QTDM-01 work order/baseline |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | only CVF-governed repository sources plus the cited official lifecycle pages support this return |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| literalTokensReviewed | `Status: COMPLETE_PENDING_REVIEW`; `Self-declared worker-return artifact: yes`; `Responds to work order:`; `contractProfile: WORKER_RETURN_FULL_GATE_V1`; `Delta Execution Claim Boundary Control Block` field-row table; `docs/reviews/` structural review section groups; `WORKER_MUST_NOT_COMMIT honored` |
| gateRunPurpose | confirm this worker-return packet satisfies its own full-gate structural profile before the bundled fast gate runs |
| claimBoundary | structural read-ahead confirms packet shape only; it does not itself validate migration correctness |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | worker (migration role) |
| Provider or surface | local repository tools |
| Session or invocation | QTDM-01 worker execution, 2026-08-15 |
| Working directory | repository root |
| Command or tool surface | PowerShell enumeration, Python identifier-substitution script, `git grep`, governed Markdown authoring, ADIF resolver, worker-return fast gate |
| Target paths | 119 active manifest paths across Classes A-E plus this worker return |
| Allowed scope source | work order Active-Surface Migration Manifest and Replacement Contract |
| Before status evidence | clean worktree at HEAD `301871f030a409fd50ca9b20939bc81559ccbf2c` |
| After status evidence | 119 modified active files plus this untracked worker return; HEAD unchanged; staging empty |
| Diff evidence | `git diff --name-status`; `git diff --stat` shows 119 files changed, 264 insertions, 256 deletions |
| Approval boundary | bounded migration worker tranche; independent review pending |
| Claim boundary | identifier migration and gate evidence only; no live call, no commit |
| Agent type | single migration worker role |
| Invocation ID | `qtdm-01-worker-2026-08-15` |
| Expected manifest | 119 active files (A=9, B=73, C=25, D=7, E=5) plus one worker return |
| Actual changed set | 119 active files plus one worker return |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename occurred; all changes are content edits and one new addition |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | Qwen-Turbo deprecation identifier migration worker tranche |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, interception, or provider compatibility is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime, provider, or live action occurred |
| invocationBoundary | local identifier substitution and governed Markdown authoring only |
| interceptionBoundary | no direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized |
| claimLanguage | identifier migration evidence only, pending independent review |
| forbiddenExpansion | no live provider call, no T6 retry, no npm/npx repair, no guard implementation, no session mutation, no public export, no production |

## Epistemic Process Block

Expected Result: the exact 119-path active manifest would migrate `qwen-turbo`
to `qwen-flash` with zero residual active occurrences and zero historical
mutation.

Evidence Comparison: 119 files migrated (249 `qwen-turbo` plus 18 provisional
`qwen3.6-flash` replacements); active scopes report zero `qwen-turbo`; the SOT3
test reports zero `qwen3.6-flash`; 100 historical files retain `qwen-turbo` as
legacy evidence; the snapshot is recorded in the ledger.

Contradiction or Gap Disposition: the work order acceptance command's
`:!*evidence*` glob is case-sensitive and does not exclude the two
uppercase-EVIDENCE historical packets, producing 5 residual matches that are
correctly preserved historical facts, not active configuration.

Claim Update: `Claim confirmed with bounded reviewer correction` - active
configuration surfaces target `qwen-flash` and historical evidence is
preserved, but prior Alibaba certification evidence is not transferred to the
new model; fresh T6 live proof remains required.

## Worker Experience Retrospective

WORKER_EXPERIENCE_RETRO:

frictionLevel: LOW

frictionType: KEYWORD_TRAP

observedStep: the acceptance command's case-sensitive `:!*evidence*` glob did
not exclude uppercase-EVIDENCE historical filenames, and a pre-existing
trailing-whitespace line surfaced under `git diff --check` after migration

preventiveControlCandidate: HELPER_DIAGNOSTIC

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next action |
|---|---|---|---|---|
| acceptance command case-sensitive pathspec leaves uppercase-EVIDENCE historical packets unmatched | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | consider a case-insensitive historical-exclusion pathspec in future acceptance commands |
| pre-existing trailing whitespace flagged after migration on a touched line | N/A_WITH_REASON | DOCUMENTATION_ONLY_LEARNING | RULE_EXISTS | trimmed the touched line; no governance rule change required |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance migration worker-return packet; no public artifact
or public-sync action is authorized or performed.

## git status --short

```text
119 files modified (Classes A-E), all ` M `:
  M ARCHITECTURE.md
  M README.md
  M docs/CVF_CORE_KNOWLEDGE_BASE.md
  M docs/CVF_INCREMENTAL_TEST_LOG.md
  M docs/guides/CVF_DEMO_SCRIPT_2026-04-21.md
  M docs/reference/CVF_KNOWN_LIMITATIONS_REGISTER_2026-04-21.md
  M docs/reference/CVF_LHW23_T1_MODEL_REGISTRY_SERVICE_ADVISORY_CONNECTOR_SPEC_2026-05-31.md
  M docs/reference/CVF_PROVIDER_LANE_READINESS_MATRIX.md
  M docs/reference/CVF_RELEASE_CANDIDATE_TRUTH_PACKET_2026-04-21.md
  M docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_USE_PROOF_ADAPTER_STANDARD.md
  M docs/reference/model_gateway/CVF_ALIBABA_FREE_QUOTA_MODEL_LEDGER.json
  M docs/reference/model_gateway/CVF_ALIBABA_FREE_QUOTA_MODEL_LEDGER.md
  M governance/compat/test_run_assf_package_use_proof_adapter.py
  M scripts/cvf_provider_check.py
  M scripts/evaluate_cvf_provider_lane_certification.py
  ... (119 total modified; full list enumerated in the work order manifests)
?? docs/reviews/CVF_QWEN_TURBO_DEPRECATION_MIGRATION_WORKER_RETURN_2026-08-15.md
```

## Changed Files

```text
119 files modified (Classes A-E: 9 runtime + 73 test/support + 25 scripts + 7 reference + 5 user-facing docs), no historical/archive/evidence/session path modified.
docs/reviews/CVF_QWEN_TURBO_DEPRECATION_MIGRATION_WORKER_RETURN_2026-08-15.md (new, untracked)
```

## Command Evidence

| Command | Disposition |
|---|---|
| `git rev-parse HEAD` | PASS: `301871f030a409fd50ca9b20939bc81559ccbf2c` |
| Class B enumeration | PASS: 72 dispatch-base hits, plus 1 SOT3 = 73 |
| active-surface deprecated-identifier scan | PASS: 0 matches across the three exact active scopes listed in the governed manifest |
| SOT3 `qwen3.6-flash` scan | PASS: 0 matches |
| historical `qwen-turbo` count | PASS: 100 files retained as legacy evidence |
| worker substitution count | PASS: worker replaced 249 active `qwen-turbo` occurrences with `qwen-flash` before reviewer wording corrections |
| `qwen-flash-2025-07-28` snapshot | PASS: recorded in free quota ledger |
| `git diff --check` | PASS (trailing whitespace trimmed) |
| `python governance/compat/run_adif_defect_resolver.py --task-class dispatch --role worker --lifecycle-phase pre-implementation --surface-selector qwen --risk-ceiling HIGH --max-results 20 --json` | PASS: 0 defects returned |

## Gate Run Evidence

| Command | Disposition |
|---|---|
| `python governance/compat/run_worker_return_fast_gate.py` | initial worker run exposed reviewer-owned system-chain SOURCE_DRIFT; final reviewer rerun PASS after semantic review and fingerprint refresh |
| `git diff --check` | PASS |
| `git diff --cached --name-only` | PASS (empty; staging is empty) |

Reviewer-owned closure action: the system chain map freshness checker reports
SOURCE_DRIFT on two fingerprinted sources (`ARCHITECTURE.md` and
`docs/CVF_CORE_KNOWLEDGE_BASE.md`) because this migration legitimately changed
those files. The checker states semantic verdicts are never auto-rewritten by
the worker; the reviewer refreshes `lastVerifiedDate` and the recorded hashes
only after governed review, which is a closure step, not a worker step.

## Independent Reviewer Closure

Independent reviewer disposition: `CLOSED_PASS_BOUNDED_AFTER_REPAIR`.

| Review finding | Reviewer action | Final disposition |
|---|---|---|
| seven encoding-exception lines reintroduced the deprecated literal and three TypeScript plus one Python line were not comments | removed the literal from the exception wording and converted source-file annotations to valid comments | CLOSED |
| two active identifiers retained Qwen-Turbo names with underscore/constant spelling | renamed the stream capability constant and Python test method to Qwen-Flash identifiers | CLOSED |
| mechanical documentation replacement transferred historical certification/PASS claims to `qwen-flash` without a live receipt | rewrote current authority to `EXPERIMENTAL` / `PENDING_LIVE_REVALIDATION`; historical Alibaba evidence remains non-transferable and T6 remains required | CLOSED |
| free-quota diagnostic ledger projected a historical PASS onto `qwen-flash` | changed the active alias result to `NOT_RUN_PENDING_T6` | CLOSED |
| system-chain source fingerprints drifted after reviewed architecture wording changes | reviewed the `DOCTRINE_TO_CONTRACT` lane semantics, retained its posture/verdict unchanged, refreshed only the two hashes and `lastVerifiedDate` | CLOSED |
| touched `ai-providers.ts` reached the GC-023 hard threshold and retained a compressed statement | extracted the existing system-prompt function into `cvf-system-prompt.ts`, preserved the original export surface, and reduced the provider module from 1000 to 863 lines | CLOSED |
| one stale dated advisory connector remained active after its governed identifier refresh | registered the still-referenced connector as a binding active-window reference | CLOSED |
| worker-return scan wording was parsed as an unregistered synthetic corpus path | replaced the slash-concatenated shorthand with a bounded reference to the three exact manifest scopes; no corpus completeness claim was added | CLOSED |

Reviewer validation evidence:

- Model Gateway TypeScript check: PASS.
- Model Gateway hermetic suite: 32 files, 252 tests PASS.
- CVF Web TypeScript check: PASS.
- GC-023 governed file-size check: PASS after maintainability extraction.
- Focused changed non-live Web suite: 17 files, 251 tests PASS.
- Focused Qwen-Flash denial test: 1/1 PASS.
- Worker-return fast gate and reviewer-fast governance: PASS, 63/63.
- System-chain freshness: CURRENT/PASS.
- Active changed-set scan for `qwen-turbo`, `qwen_turbo`, or `qwen turbo`:
  zero matches outside the deprecation review/evidence chain.

Bounded validation anomalies:

- the default full Web non-live suite timed out after 244 seconds without a
  summary; the serialized focused changed set passed 251/251;
- one first focused invocation ran root Vitest without the Web alias config and
  produced import-resolution failures; the corrected project-local invocation
  passed 251/251;
- the full ASSF package-use-proof adapter unit file produced 7/9 failures
  because its synthetic free-quota entries expired before the current date;
  the migration-specific renamed denial test passed 1/1. Fixture-date repair is
  outside QTDM-01 and no live/provider claim depends on that suite.

Reviewer-owned material scope expansion:

- `docs/reference/system_chain/CVF_SYSTEM_CHAIN_MAP.json`, required to close
  reviewed source-fingerprint drift; no semantic verdict was auto-rewritten;
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/cvf-system-prompt.ts`,
  required by GC-023 to split the touched near-threshold provider module while
  preserving its export surface;
- `governance/compat/CVF_ACTIVE_WINDOW_REGISTRY.json`, required to retain the
  still-referenced dated advisory connector after its identifier refresh.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch`, role=`worker`, lifecyclePhase=`pre-implementation`, surfaceSelector=`qwen`, riskCeiling=`HIGH`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class dispatch --role worker --lifecycle-phase pre-implementation --surface-selector qwen --risk-ceiling HIGH --max-results 20 --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | no additional ADIF constraint on this worker tranche |

## No-Commit Statement

WORKER_MUST_NOT_COMMIT honored. No `git add`, `git commit`, or staging action
of any kind was performed. All 119 active files remain unstaged modifications
and the worker return remains untracked. HEAD remains
`301871f030a409fd50ca9b20939bc81559ccbf2c`, identical to executionBaseHead.
Independent reviewer/closer owns all staging and commit actions from here.

## Core Guard Self-Protection Authorization

Protected paths:

- `docs/CVF_CORE_KNOWLEDGE_BASE.md`
- `governance/compat/test_run_assf_package_use_proof_adapter.py`

Authorized guard-maintenance scope: identifier-only deprecation migration of
`qwen-turbo` to `qwen-flash` on the two protected paths, per the QTDM-01 work
order Active-Surface Migration Manifest. No guard, checker, hook, autorun, CI,
or governance-compat source semantics are changed.

Operator authorization: the operator directed Qwen-Turbo removal after the
blocked CADP-AI-T6 proof and environment repair, recorded in the active
handoff and session next-move.

Rollback boundary: revert this exact QTDM-01 material migration batch together
with the worker return; do not separate the identifier substitution from the
migration evidence.

## Large-Scope Change Authorization

Changed-file ceiling: 123 files (119 worker migration edits, one worker return,
and three reviewer-owned closure paths), exceeding the 40-file safe-agent
limit.

Rename/delete ceiling: 0 renames or deletions, within the 10-file limit.

Operator authorization: the operator directed a repository-wide active-surface
deprecation migration; the exact 119-path manifest is enumerated in the paired
baseline Active-Surface Migration Manifest.

Rollback boundary: revert this exact QTDM-01 material batch; the migration is a
mechanical identifier substitution with no semantic change and is reversible
by restoring the pre-migration HEAD content.

## Package Skill Productionization Control Block

SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`

Current phase: N/A with reason: QTDM-01 changes only a deprecated provider
model identifier in an existing ASSF adapter test and does not change any
package-skill lifecycle state.

Target lifecycle state: N/A with reason: no package skill is created,
promoted, activated, deprecated, or retired by this tranche.

Prior phase evidence: N/A with reason: no package-skill phase transition is
requested or claimed.

Next forbidden skip: do not use this migration or its adapter-test evidence to
promote, activate, load, project, or claim runtime eligibility for any package
skill without the source-backed SOP evidence required by the cited standard.

Runtime/provider proof: N/A with reason: this tranche made no provider API
call and transfers no historical live receipt to `qwen-flash`.

Claim boundary: the ASSF adapter test reference is validation context only; it
does not productionize a package skill or establish runtime/provider fitness.

## Claim Boundary

This worker-return packet records worker-executed identifier-migration evidence
only. It does not implement or promote a machine guard, does not perform or
prove any live provider call, does not authorize T6 retry or environment
repair, and does not claim provider compatibility, production readiness, or
cross-runtime determinism. Historical receipts, archives, evidence JSON,
handoffs, and prior session-state entries remain immutable. The replacement
snapshot `qwen-flash-2025-07-28` is recorded as a version reference only.
