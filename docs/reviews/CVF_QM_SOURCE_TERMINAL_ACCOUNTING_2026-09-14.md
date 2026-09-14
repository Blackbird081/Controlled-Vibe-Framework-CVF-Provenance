# QM Source Terminal Accounting

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: review

Date: 2026-09-14

Decision owner: Local reviewer

## Purpose

Complete bounded source-level accounting for `yc-software__qm` after Local
acceptance of the R1-R4 evidence ledgers, output-redaction conversion and
service-token replay-deduplication conversion. Decide the only remaining
admission question: whether R1 M4 has a concrete unsatisfied current consumer.

## Target / Source

| Evidence | Accepted identity | Review use |
|---|---|---|
| `docs/audits/CVF_QM_RUNTIME_VALUE_R1_2026-09-14.json` | SHA-256 `b3912cfe1a6e861abf78a579d50192bb0711f0fdf8e230be371950a618604889`; QM pin `51bf455ea414a58f70274284ce212142518e556a` | auth, credential and sandbox mechanisms; M4/M5 |
| `docs/audits/CVF_QM_RUNTIME_VALUE_R2_2026-09-14.json` | SHA-256 `744ec9b7fc627b40aa0104708a73922af28fe58e8a3b19ee9a86955f31c58fd6`; QM pin `51bf455ea414a58f70274284ce212142518e556a` | run, session and process mechanisms |
| `docs/audits/CVF_QM_RUNTIME_VALUE_R3_2026-09-14.json` | SHA-256 `da72f5c9879d24e9977e34b08da141c838de431c86e3b6d5b8057e376490765d`; QM pin `59cf6554faadcd06494782190c3ecae1829dd381` | policy, ACL and redaction mechanisms |
| `docs/audits/CVF_QM_RUNTIME_VALUE_R4_2026-09-14.json` | SHA-256 `ad6d8c7e4c7f58428035104f55aead5bad169dd4e34b24fa0410e37e5b034d7b`; QM pin `361a6c0095dcd3d156aca91353f3ffba0bb8b69b` | memory mechanisms |
| `docs/reviews/CVF_OUTPUT-REDACTION-T1_COMPLETION_2026-09-14.md` | accepted bounded conversion | final disposition of R3 M9 |
| `docs/reviews/CVF_QM_SERVICE_TOKEN_REPLAY_DEDUPE_T1_COMPLETION_2026-09-14.md` | material commit `74b30b725ab4f95def0a2679943f4ce6bcbd385d` | final disposition of R1 M5 |

## Scope / Methodology

`EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION`. Local reused the
accepted R1-R4 ledgers and inspected only the current CVF-Web M4 consumer
contract: the service-token verifier, its environment declaration, and named
production callers. No QM mirror rescan, upstream execution, provider call,
live proof, dependency installation or implementation occurred.

## Findings / Position

The four accepted ledgers contain 56 mechanism records: eight source-side
`ADAPT_CANDIDATE`, 36 `DEFER_WITH_TRIGGER`, and 12
`REJECT_NO_ACTIONABLE_VALUE`. Final Local conversion accounting is disjoint:

| Final disposition | Count | Records |
|---|---:|---|
| `ADAPTED_ACCEPTED_BOUNDED` | 2 | R1 M5 replay deduplication; R3 M9 known-value output redaction |
| `DEFERRED_WITH_TRIGGER` | 42 | six unselected adapt candidates plus the 36 already-deferred records |
| `REJECTED_NO_ACTIONABLE_VALUE` | 12 | the twelve rejected records retained as evidence |
| Total | 56 | `2 + 42 + 12 = 56` |

### R1 M4 Current-Consumer Decision

R1 M4 proposes structured per-actor capability claims, audiences and
`kid`-based multi-secret rotation. The current CVF-Web contract does not
establish demand for that expansion:

- `.env.example` declares one `CVF_SERVICE_TOKEN` value;
- `service-token-auth.ts` verifies one configured token and derives identity
  from that token; it exposes no principal registry, audience requirement,
  `kid` selector or old/new overlap configuration;
- current signed callers pass the same deployment environment value into the
  same verifier; existing actor attribution does not consume capability-token
  claims or audience entitlements;
- the break-glass guide's mandatory rotation applies to the separate
  `CVF_BREAK_GLASS_TOKEN`, so it is not evidence of an unsatisfied M4
  service-token consumer.

Verdict: `NO_CONCRETE_UNSATISFIED_CURRENT_CONSUMER`. M4 becomes
`DEFERRED_WITH_TRIGGER`, not an implementation tranche. Reopen only when a
named current owner requires either simultaneous old/new service-token overlap
or distinct service principals with enforceable audience/resource claims.

Plain-token equality in older route-local auth branches is not evidence for
M4's claims/audience/key-rotation expansion. Any consolidation of those native
CVF branches requires a separate current-owner security decision and cannot be
smuggled into this external-source accounting closure.

## Decision

`yc-software__qm` is `TERMINAL_ACCEPTED` within
`DOMAIN-PILOT-THREE-REPO-2026-09`. The accepted source value consists of two
bounded CVF-native conversions; every other R1-R4 record has a terminal defer
or reject disposition with its trigger preserved. No M4 work order or worker
dispatch opens. The program remains active because Agentgateway and DeepSeek
Harness are still `INCOMPLETE`; the next source is
`agentgateway__agentgateway` for bounded residual terminal accounting.

## Risk / Corrective Action

This is source accounting, not proof of whole-QM semantic coverage or deployed
security. Process-local replay remains process-local. Shared/durable replay,
ambient credentials, command-policy adoption, memory runtime, M4 token claims
and rotation, provider/live, public sync and deployment remain unopened.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_next_move_freshness.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_absorption_blindspot_control_presence.py` |
| literalTokensReviewed | `TERMINAL_ACCEPTED`; `INCOMPLETE`; `NEXT_SOURCE_ID`; `NEXT_ACTION_CLASS=CONTINUE_ACTIVE_PROGRAM`; `EXPANSION_ALLOWED=false`; `DEFERRED_PRIVATE_ONLY` |
| gateRunPurpose | confirm as evidence the terminal source state, retained active-program projection and governed review shape after their requirements were read; gates are not used for first discovery |
| claimBoundary | structural compliance does not prove whole-repository reading or deployment readiness |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | N/A with reason: Local terminal accounting consumes already-accepted work orders and opens no worker lane | R1-R4 completion reviews are closed | N/A with reason |
| Completion or reviewer artifact | `docs/reviews/CVF_QM_SOURCE_TERMINAL_ACCOUNTING_2026-09-14.md` | `Status: CLOSED_PASS_BOUNDED`; 56-record reconciliation | PASS |
| Roadmap state | N/A with reason: active three-source program continuity is the governing roadmap boundary | QM will be projected `TERMINAL_ACCEPTED` while the program stays active | N/A with reason |
| Registry JSON | `docs/audits/CVF_QM_RUNTIME_VALUE_R1_2026-09-14.json`; R2-R4 sibling audits | 56 mechanism records reconcile to 2 adapted, 42 deferred and 12 rejected | PASS |
| Registry Markdown | `docs/reviews/CVF_QM_SOURCE_TERMINAL_ACCOUNTING_2026-09-14.md` | human-readable terminal mapping and M4 decision | PASS |
| External evidence digest | four accepted audit SHA-256 values in Target / Source | SHA-256 `b3912cfe1a6e861abf78a579d50192bb0711f0fdf8e230be371950a618604889`, `744ec9b7fc627b40aa0104708a73922af28fe58e8a3b19ee9a86955f31c58fd6`, `da72f5c9879d24e9977e34b08da141c838de431c86e3b6d5b8057e376490765d`, `ad6d8c7e4c7f58428035104f55aead5bad169dd4e34b24fa0410e37e5b034d7b` | PASS |
| System loop interlock | N/A with reason: no system loop or runtime owner changes | documentation-only source accounting | N/A with reason |
| Session continuity | N/A with reason: material source decision precedes its dedicated session-sync commit | next source is recorded by the subsequent continuity projection | N/A with reason |

## Epistemic Process Block

- Expected Result / Prediction: no M4 implementation should open unless a
  current CVF owner supplies a concrete multi-key or capability-claim consumer.
- Evidence Comparison: the accepted R1 proposal is conditional; current source
  declares one environment token and no claim/audience/rotation consumer.
- Contradiction or Gap Disposition: no contradiction remains. Preserve the M4
  design as `DEFERRED_WITH_TRIGGER`; do not infer need from generic security
  preference or from the unrelated break-glass token.
- Claim Update: QM has terminal source accounting with two accepted bounded
  conversions; the three-repository program remains open.

## Corpus Completeness And Report Integrity

- Corpus task class: bounded terminal reconciliation over four accepted QM
  mechanism ledgers and named current CVF consumer files.
- Corpus root: the four R1-R4 audit artifacts and named CVF owner surfaces in
  Target / Source.
- Snapshot time: 2026-09-14 at pre-decision HEAD
  `19a2ab527480c231635ca6e93a6452857ff2eec9`.
- Enumeration command: filesystem-backed direct file reads of the accepted
  manifests, plus `rg --files --hidden --no-ignore
  EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web` as the safe current-consumer
  membership basis; no new source enumeration.
- Manifest artifact or inline manifest: R1-R4 manifests in the four accepted
  audits.
- Manifest hash: the four accepted audit SHA-256 values in Target / Source.
- Processing ledger artifact or inline ledger: R1-R4 `mechanismRecords`.
- Allowed terminal statuses: `READ`, `SKIPPED_WITH_REASON`, `DEFERRED`,
  `REJECTED`, `ADAPTED`, `NO_NEW_VALUE`, `BLOCKED_UNREADABLE`.
- Reconciliation: manifest=56; ledger_terminal=56; exclusions=0; unresolved=0;
  the 56 mechanism records equal 2 adapted plus 42 deferred plus 12 rejected.
- Unresolved files: 0 within the declared 56-record terminal ledger. Files
  outside the accepted R1-R4 manifests are excluded from this declared corpus,
  not asserted resolved for the QM repository.
- Declared exclusions: QM paths outside the accepted R1-R4 manifests; CVF
  files outside the named M4 consumer search; runtime and live behavior.
- Unreadable or unsupported files: none among the named decision inputs.
- Aggregation check: PASS for the 56-record terminal mechanism ledger.
- Drift check: no upstream refresh; each accepted audit remains bound to its
  recorded immutable pin.
- Output traceability: four audits, their completion reviews, two accepted
  conversions and this Local decision.
- Adversarial verification: reject any interpretation that terminal source
  accounting means all QM files were read or all deferred mechanisms were
  implemented.
- Corpus verdict: PARTIAL
- Verdict reason: bounded source use-case recovery is terminally accounted;
  no complete-corpus claim.

## Knowledge System Reconciliation

- Knowledge task class: terminal reconciliation of accepted source mechanisms.
- Source manifest: the four R1-R4 audit manifests.
- Source manifest hash: the four accepted audit SHA-256 values recorded in
  Target / Source; no combined synthetic hash is substituted.
- Enumeration safety: filesystem-backed direct file reads plus `rg --files --hidden --no-ignore EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`; no new external-source enumeration.
- Intake registry or ledger: 56 disjoint mechanism records.
- Derived views: final Local disposition view of 2 adapted, 42 deferred and 12
  rejected records.
- Semantic region ledger: R1 auth/credentials/sandbox; R2 run/session/process;
  R3 policy/ACL/redaction; R4 memory.
- Region reconciliation: assets=56; mapped=56; deferred=0; unmapped=0; all four
  accepted regions are represented once.
- Mapped: 56; deferred: 0; unmapped: 0 after final Local disposition mapping.
- Reconciliation: `56 + 0 + 0 = 56`.
- Orphan or unmapped assets: 0 within the declared 56-record map; unread QM
  files are outside this bounded knowledge-map claim, not orphaned map assets.
- Cross-region links: R1 M5 and R3 M9 link to their accepted CVF-native
  conversions; all remaining links resolve to preserved triggers or rejects.
- Drift check: PASS for identity of the four accepted immutable artifacts and
  their recorded pins; no claim of current upstream-head freshness.
- Rebuildability check: PASS from the four audit hashes, per-record IDs and the
  arithmetic recorded in this decision.
- Retrieval boundary: retrieve by source region, mechanism ID and final Local
  disposition; do not treat the mirror as a runtime dependency.
- Adversarial verification: reject whole-QM, all-files-read or implementation
  claims inferred from terminal source accounting.
- Knowledge-map verdict: PARTIAL
- Authority assets: the accepted audit/completion artifacts and this Local
  decision.
- Claim boundary: mapping a record to adapted/deferred/rejected does not make
  its source code a CVF runtime dependency.

## Mandatory Blind-Spot Control Block

Applied. Local sampled every raw disposition group, independently resolved all
eight adapt candidates through their accepted conversions or current triggers,
and retained the 36 defer plus 12 reject rows without treating filenames or
gate success as semantic proof. No whole-QM scan claim is made.

## External Repository Absorption Entry Control

| Field | Value |
|---|---|
| Source type | pinned external Git repository already present as a private reference mirror |
| Upstream or source-mirror disposition | reuse accepted QM pins; no network refresh or runtime dependency |
| Enumeration or manifest plan | reuse exact R1-R4 manifests; no new corpus enumeration |
| Per-file terminal-ledger plan | accepted per-audit processing ledgers remain authoritative for their bounded regions |
| Owner or overlap route | source mechanism -> current CVF owner -> Local final disposition |
| Value-disposition route | `ADAPT`, `DEFER`, or `REJECT`; no direct import |
| Claim boundary | terminal source use-case accounting, not whole-repository completeness or runtime activation |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| R1 M5 replay dedupe | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts` | `ENRICH_EXISTING` | exact valid-request replay rejection | `ADAPTED_ACCEPTED_BOUNDED` |
| R3 M9 known-value redaction | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/output-redaction.ts` | `ENRICH_EXISTING` | opt-in known-value layer | `ADAPTED_ACCEPTED_BOUNDED` |
| R1 M4 capability claims/rotation | service-token owner and current callers | `NEW_FINDING` | broader principal/audience/key model without current demand | `DEFERRED_WITH_TRIGGER` |
| other R1-R4 mechanisms | per-record owners in accepted audits | mixed `NEW_FINDING`, `OWNER_SURFACE_NOT_FOUND`, and `REJECT_DIRECT_IMPORT` | retained design or adverse evidence | preserve terminal defer/reject rows |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | accepted QM R1-R4 evidence -> current-owner comparison -> two bounded conversions -> Local terminal source accounting |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `docs/reference/external_agent_review/CVF_CROSS_WORKSPACE_DOMAIN_FUNNEL_ABSORPTION_METHOD.md` |
| Disposition | `TERMINAL_ACCEPTED` for QM; retain active three-source program |
| Claim boundary | source-terminal accounting only; no program exit until all three sources are terminal |

## External/Local Coordination Binding

```json
{
  "contractId": "cvf.external-local-absorption-coordination@1",
  "invariants": {
    "externalRole": "ADVISORY_RESEARCH_AND_PATTERN_MAPPING",
    "externalContext": "PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ",
    "localRole": "SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION",
    "finalDecisionOwner": "LOCAL",
    "localCoverageBasis": "SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST",
    "externalEvidenceAuthority": "INPUT_NOT_PRIVATE_CVF_PROOF"
  },
  "contractSha256": "92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c",
  "parentArtifact": "docs/reviews/CVF_QM_SERVICE_TOKEN_REPLAY_DEDUPE_T1_COMPLETION_2026-09-14.md"
}
```

## Finding-To-Governance Learning Disposition

Defect class: `N/A_WITH_REASON` - no new defect was found; this pass resolves a
pending admission decision. Learning lane: `DOCUMENTATION_ONLY_LEARNING`.
Disposition: `RULE_EXISTS`; current demand-gating, source accounting and
review-cost rules already require this outcome. No checker or doctrine change.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local reviewer/orchestrator |
| Provider or surface | internal shared workspace |
| Session or invocation | QM terminal accounting 2026-09-14 |
| Working directory | repository root |
| Command or tool surface | targeted governed-artifact reads, hashes, source search and Git status |
| Target paths | this review; later dedicated continuity projection |
| Allowed scope source | active next-allowed-move and Local final-decision ownership |
| Before status evidence | HEAD `19a2ab527480c231635ca6e93a6452857ff2eec9`; worktree clean |
| After status evidence | this material review only before continuity projection |
| Diff evidence | `git diff --name-status`; `git status --short --untracked-files=all` |
| Approval boundary | bounded source-terminal accounting; no worker implementation |
| Claim boundary | no full-corpus, provider/live, public, deploy or production claim |
| Agent type | reviewer/closer |
| Invocation ID | qm-source-terminal-accounting-20260914 |
| Expected manifest | `docs/reviews/CVF_QM_SOURCE_TERMINAL_ACCOUNTING_2026-09-14.md` |
| Actual changed set | `docs/reviews/CVF_QM_SOURCE_TERMINAL_ACCOUNTING_2026-09-14.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private source-accounting and active-program routing decision; no
public-sync action or public artifact was authorized.

## Claim Boundary

QM is terminally accounted only for the bounded use-case recovery program.
This does not claim complete semantic reading of the QM repository, adoption of
all source mechanisms, runtime/live readiness, public export, deployment or
completion of the three-repository program.
