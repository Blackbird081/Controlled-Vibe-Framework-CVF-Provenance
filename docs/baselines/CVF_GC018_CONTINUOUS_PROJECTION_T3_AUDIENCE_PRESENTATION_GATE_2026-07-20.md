# CVF GC-018 Baseline - Continuous Projection T3 Audience And Presentation Gate

Memory class: governed-dispatch-baseline

Status: CLOSED_PASS_WITH_REVIEWER_REPAIRS

Batch ID: CVF-CONTINUOUS-PROJECTION-T3

Dispatch base head: `c060fc7a5`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer/closer: Codex reviewer/closer

Worker target: delegated worker role through manual copy/paste only

## Purpose

Release the roadmap T3 audience and presentation gate as a bounded read-only
implementation. The gate validates source-freshness evidence together with a
reviewer-owned audience evidence packet; it does not decide semantic quality,
edit projection surfaces, scan real roots, or invoke any provider.

## Decision / Baseline / Proposed Tranche

The operator explicitly reopened Continuous Projection T3 and T4 on
2026-07-20. Only T3 implementation is released now. T4 remains dependency-held
until independent T3 review and closure provide a committed release receipt.

T3 adds exactly one read-only PowerShell gate, one focused disposable-fixture
proof suite, and one worker-return packet. All README, cvf-web, public-sync,
projection mapper, receipt, review-packet, policy, session, and governance
source files remain read-only to the worker.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-CONTINUOUS-PROJECTION-T3 --title "Continuous Projection T3 Audience And Presentation Gate" --date 2026-07-20 --base c060fc7a5 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "T2 completion review docs/reviews/CVF_CONTINUOUS_PROJECTION_T2_COMPLETION_REVIEW_2026-07-20.md commit f350b925a REVIEWER_ACCEPTED_WITH_REPAIRS" --stdout` |
| generatedProfile | web-ui-dashboard plus `WORKER_MUST_NOT_COMMIT` no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced all scaffold fields with source-verified T3 scope, frozen interfaces, evidence schema, dependency evidence, manifests, and role-neutral boundaries. |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_markdown_structural_completeness.py` |
| docOnlyNewFields | `audienceEvidenceSchemaVersion`; `assessmentStatus`; `audienceGateSchemaVersion`; `gateStatus`; `sourceFreshnessStatus`; `audiencePresentationStatus`; `authorizesMutation` |
| claimBoundary | Dispatch-authoring provenance and frozen T3 contract only; no runtime/provider/live/public mutation, Web edit, MCP/CLI adapter, or production claim. |

## Scope / Target / Owner Boundary

Target: deterministic evidence validation for public README, cvf-web, and the
external-agent context route after source freshness has already been measured.

Semantic ownership remains with the reviewer. The worker implements validation
and deterministic output only. A `PASS` proves that the required reviewer-owned
evidence rows were present and internally consistent; it is not independent
proof that presentation quality is good.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| T2 governed review-packet drafting | `docs/reviews/CVF_CONTINUOUS_PROJECTION_T2_COMPLETION_REVIEW_2026-07-20.md`; material commit `f350b925a`; status `REVIEWER_ACCEPTED_WITH_REPAIRS` | T3 may dispatch only after T2 accepted output and roadmap T3 definition are source-verified | ACCEPT |
| UX remediation evidence | `docs/reviews/CVF_WEB_UX_T4_COMPLETION_2026-07-20.md`; material commit `d757fe5ac`; bounded localhost disposition | T3 reuses its evidence vocabulary and must not claim hosted or public freshness | ACCEPT |
| Operator release | direct operator instruction on 2026-07-20 to finish Continuous Projection T3 and T4 | release T3 now; keep T4 held for T3 closure | ACCEPT |

## Frozen T3 Audience Evidence Contract

Input JSON schema version:
`cvf.continuousProjectionAudienceEvidence.t3.v1`.

Each assessment has exactly these fields: `ordinal`, `surface`, `criterion`,
`audience`, `status`, `evidenceLocator`, `observation`, and `reviewerOwned`.
`reviewerOwned` must be Boolean `true`. `status` is exactly one of `PASS`,
`FAIL`, or `REVIEW_REQUIRED`.

The seven ordered assessment identities are:

| Ordinal | Surface | Criterion | Audience |
| --- | --- | --- | --- |
| 1 | `public-readme` | `progressive_disclosure` | `end_user` |
| 2 | `public-readme` | `language_clarity` | `end_user` |
| 3 | `public-readme` | `first_action` | `end_user` |
| 4 | `cvf-web` | `progressive_disclosure` | `end_user` |
| 5 | `cvf-web` | `navigation_clarity` | `end_user` |
| 6 | `cvf-web` | `developer_depth` | `developer` |
| 7 | `external-agent-context` | `evidence_route` | `external_agent` |

Every `evidenceLocator` and `observation` must be non-empty ASCII text. The
gate must reject missing, extra, duplicate, reordered, renamed, or type-invalid
assessment rows.

## Frozen T3 Gate Interface And Output Contract

Command interface:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/get_cvf_projection_audience_gate.ps1 -ReceiptPath <receipt.json> -ReviewPacketPath <draft.json> -AudienceEvidencePath <evidence.json>
```

The script accepts no root, output, apply, copy, commit, push, browser,
provider, or network parameter. It reads three explicit local files and emits
one JSON object to stdout.

Output schema version:
`cvf.continuousProjectionAudienceGate.t3.v1`.

Required output fields: `schemaVersion`, `gateStatus`,
`sourceFreshnessStatus`, `audiencePresentationStatus`, `authorizesMutation`,
`inputReceiptId`, `assessments`, `summary`, `errors`, and `claimBoundary`.

`authorizesMutation` is Boolean `false`. `gateStatus` is `PASS` only when:

- the T1 receipt schema is accepted, `summary.reconciliationMatch` is Boolean
  `true`, `errors` is empty, and its no-target-write confirmation is exact;
- the T2 draft has `draftStatus=REVIEW_REQUIRED_UNCOMMITTED`, Boolean
  `authorizesDecision=false`, the frozen no-mutation claim boundary, and a
  source receipt identity matching the T1 receipt;
- all seven audience assessments are valid and have `status=PASS`.

Any assessment `FAIL` produces `gateStatus=FAIL`. Any
`REVIEW_REQUIRED` produces `gateStatus=REVIEW_REQUIRED`. Malformed or
contradictory input exits nonzero and emits no success object.

Frozen claim boundary:
`READ_ONLY_EVIDENCE_GATE_NO_SEMANTIC_DECISION_NO_APPLY_COPY_COMMIT_PUBLIC_MUTATION`.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T3 requires audience and presentation checks in addition to freshness | VALUE_SET | `docs/roadmaps/CVF_CONTINUOUS_PROJECTION_DRIFT_DETECTION_AND_REVIEW_PACKET_AUTOMATION_ROADMAP_2026-07-19.md` | Work Plan, T3 | `T3 - Audience And Presentation Gate` | continuous-projection roadmap | ACCEPT |
| T2 draft is review-required and authorizes no decision | VALUE_SET | `scripts/get_cvf_projection_review_packet.ps1` | final draft assembly | `draftStatus`; `authorizesDecision` | T2 review-packet output schema | ACCEPT |
| T1 receipt carries reconciliation and no-write evidence | EXISTS | `scripts/get_cvf_projection_drift_receipt.ps1` | receipt assembly | `reconciliationMatch`; `noTargetWriteConfirmation` | T1 receipt output schema | ACCEPT |
| automatic semantic approval is forbidden | VALUE_SET | `scripts/cvf_projection_policy.json` | `semanticReviewBoundary` | `autoApproveForbidden` | projection policy schema | ACCEPT |
| Web/UI work must read the root design contract | LITERAL_INVARIANT | `AGENTS.md` | UI / Web Design Contract | `DESIGN.md` | CVF agent instructions | ACCEPT |
| accepted UX evidence is bounded to current-source localhost | LITERAL_INVARIANT | `docs/reviews/CVF_WEB_UX_T4_COMPLETION_2026-07-20.md` | Claim Boundary | `current-source localhost` | UX completion review | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Runtime/source status |
| --- | --- | --- |
| `audienceEvidenceSchemaVersion` | identify reviewer evidence input | new T3 contract; not claimed as existing source |
| `assessmentStatus` | freeze PASS/FAIL/REVIEW_REQUIRED vocabulary | new T3 contract; not claimed as existing source |
| `audienceGateSchemaVersion` | identify gate output | new T3 contract; not claimed as existing source |
| `authorizesMutation` | preserve no-mutation boundary | new T3 output field fixed to Boolean false |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`continuous projection T3 audience presentation gate`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Command: `python governance/compat/run_adif_defect_resolver.py --task-class "continuous projection T3 audience presentation gate" --role dispatcher --lifecycle-phase pre-dispatch --json`

Disclosed defectIds: NONE. Resolver result count: `0`.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | local PowerShell gate consuming explicit evidence files | read-only validation; no semantic, commit, public, browser, or provider authority | frozen contract and focused fixtures | internal local script only | `IMPLEMENTED` |
| `EXTERNAL_AGENT_CLI_MCP` | no external adapter is authorized | no ingress, authentication, raw-data release, mutation, or public authority | CLI/MCP moratorium and this packet boundary | separate future source-verified adapter work order required | `DEFERRED_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | `NOT_APPLICABLE_WITH_REASON`: no external repository, critique, or provider output is absorbed |
| Matching local-view guard | N/A with reason: source verification and local tests remain authority |
| Owner surface | paired T3 baseline and work order |
| Disposition | `NOT_APPLICABLE_WITH_REASON` |
| Claim boundary | no outside input is promoted or absorbed |

## Evidence / Verification

The worker must prove deterministic repeated output, all seven positive rows,
each terminal status, source-identity mismatch, missing/extra/duplicate/reordered
rows, enum casing, Boolean type errors, empty locators, receipt/draft contract
violations, and absence of write or network parameters. All fixtures must be
created under a disposable temporary directory.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | `DISPATCH_READY`; `ACCEPT`; Source Verification columns; ADIF query labels; scaffold fields; dual-agent rows; public disposition |
| gateRunPurpose | confirm dispatch structure and frozen source facts before worker handoff |
| claimBoundary | checker compliance proves packet structure only; cited source and later tests support behavior claims |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_CONTINUOUS_PROJECTION_T3_AUDIENCE_PRESENTATION_GATE_2026-07-20.md` | `Status: CLOSED_PASS_WITH_REVIEWER_REPAIRS` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_CONTINUOUS_PROJECTION_T3_COMPLETION_REVIEW_2026-07-20.md` | `Status: REVIEWER_ACCEPTED_WITH_REPAIRS` | PASS |
| Roadmap state | continuous-projection roadmap | T3 closed; T4 packet authoring next | PASS |
| Implementation evidence | two scripts plus worker return | 144/144 focused proof | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | generated aggregate check unchanged and clean | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | no entry change required; registry unchanged | PASS |
| External evidence digest | N/A with reason: repository-local fixture proof | no external bundle | N/A with reason |
| System loop interlock | N/A with reason: no interlock owner changed | no mutation | N/A with reason |
| Session continuity | protected continuity surfaces | separate post-material sync | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
| --- | --- | --- | --- | --- | --- |
| T3-SCHEMA | fixture gate output | `schemaVersion` | frozen T3 version | exact | PASS |
| T3-ROWS | fixture gate output | `summary.rowCount` | 7 | 7 | PASS |
| T3-NO-MUTATION | fixture gate output | `authorizesMutation` | Boolean false | Boolean false | PASS |
| T1-SOURCE-ROWS | fixture T1 receipt | `summary.rowCount` and `rows` | 16 and 16 | 16 and 16 | PASS |

## Current Runtime Freshness Verification

T3 closure independently recomputed 144/144 disposable-fixture assertions
after reviewer repair of the upstream source-freshness boundary. No real-root
scan, browser run, provider call, or public mutation occurred.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private provenance dispatch packet. T3 authorizes no
public-sync mutation or public claim.

## Claim Boundary

This baseline closes only T3 read-only evidence-gate implementation and
focused disposable-fixture proof. It does not release T4 execution, real-root scanning,
semantic adjudication, README/Web edits, public-sync, copy/apply, commit by the
worker, push, deployment, browser automation, provider/API use, MCP/CLI calls,
or production readiness.
