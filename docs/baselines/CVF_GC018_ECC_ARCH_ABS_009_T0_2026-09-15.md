# CVF GC-018 - ECC Cross-Harness Adapter Profile Intake

Memory class: governed-dispatch-baseline
docType: baseline
Status: APPROVED_FOR_EXECUTION
Date: 2026-09-15
Batch ID: ECC-ARCH-ABS-009-T0
Commit mode: WORKER_MUST_NOT_COMMIT
dispatchBaseHead: f8fc0810c5f57bc3d475f9c6f0f1584008709a3c

## Purpose

Authorize one bounded, source-level comparison of the pinned
`Blackbird081/everything-claude-code` fork and `affaan-m/ECC` upstream for the
single `ARCH-F-023` hypothesis: host-neutral adapter/profile semantics that may
improve cross-harness portability. This is intake and value classification,
not runtime implementation and not `WP-ARCH-006`.

## Decision / Baseline

Local review decision: `APPROVED_FOR_INITIAL_INTAKE`. The operator asked Local
to continue as orchestrator/reviewer and will relay the packet to Claude as an
internal same-workspace worker. The worker may read the two already-acquired,
ignored mirrors and create only the two named evidence outputs in the paired
work order. Local remains final decision, commit and continuity owner.

`ARCH-F-024` deterministic hook enforcement is excluded because the accepted
umbrella reconciliation already classifies it as existing/no-change. Installer
layout, Claude-specific hooks and direct code import are not candidate value.
`WP-ARCH-003` remains `PARK_NO_TRUTHFUL_AUTHORITY_ROOT`; therefore this baseline
cannot open `WP-ARCH-006`, runtime profile selection, or any authority-bearing
adapter behavior.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| ARCH-ABS-009 is linked to ARCH-F-023 and SKILL-SRC-004 | `docs/audits/CVF_UMBRELLA_SEED_RECONCILIATION_2026-09-13.json` | obligation joins and nextCandidates | `ARCH-ABS-009`; `ARCH-F-023`; `SKILL-SRC-004` | umbrella seed reconciliation | ACCEPT |
| The next Local action is independent admission with two identities preserved | `docs/reviews/CVF_THREE_REPO_PATTERN_COMPARISON_LOCAL_REVIEW_2026-09-13.md` | Next Local action | lines 119-124 | Local selection review | ACCEPT |
| WP-ARCH-003 is terminal parked | `docs/roadmaps/CVF_WP_ARCH_003_ROOT_AUTHORITY_AND_PRINCIPAL_SCOPE_ARCHITECTURE_REASSESSMENT_ROADMAP_2026-09-08.md` | Status; Decision / Baseline | `PARK_NO_TRUTHFUL_AUTHORITY_ROOT` | WP-ARCH-003 RABA owner | ACCEPT |
| Fork and upstream are pinned as distinct ignored mirrors | `.private_reference/source_mirrors/INDEX.md` | Blackbird081 and affaan-m rows | exact URL, commit and tree fields | source mirror index | ACCEPT |

## Scope / Target / Owner Boundary

Allowed: deterministic inventories at the two pinned commits; bounded reading
of adapter, profile, configuration, command, skill and integration surfaces;
fork/upstream path and semantic delta; license evidence; comparison with
current CVF ASSF/package, CLI, MCP and profile owners; and advisory atomic
dispositions `ADAPT`, `DEFER`, or `NO_NEW_VALUE`.

Forbidden: install/build/test or execute upstream payload; run source hooks,
skills, MCP servers or CLIs; mutate either mirror; import foreign code; edit
CVF runtime/source/test/checker/registry/session surfaces; provider/live calls;
credentials, public sync, push, deployment, direct runtime integration, or an
automatic successor.

## Negative Search And Collision Discipline

Before authoring, all three planned artifact paths returned `False` from
`Test-Path`. Exact search for `ECC-ARCH-ABS-009-T0|ECC Cross-Harness Adapter
Profile Intake` under `docs` and `CVF_SESSION` returned no match. Existing ECC
and ARCH-ABS-009 records are authority inputs, not packet-name collisions.

## Source-Intake Decision Packet Fields

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Negative search performed | exact packet token/path search recorded above |
| Disposition | ADAPT/DEFER/NO_NEW_VALUE must be decided per atomic item by Local after worker return |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | pinned local mirror evidence -> internal worker survey -> Local review -> separate authorization if value survives |
| Matching local-view guard | `governance/compat/check_task_governance_route.py` |
| Owner surface | `docs/reference/external_agent_review/CVF_CROSS_WORKSPACE_DOMAIN_FUNNEL_ABSORPTION_METHOD.md` |
| Disposition | INITIAL_EVIDENCE_COLLECTION_ONLY |
| Claim boundary | no source acceptance or runtime conversion |

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
  "parentArtifact": "docs/reviews/CVF_THREE_REPO_PATTERN_COMPARISON_LOCAL_REVIEW_2026-09-13.md"
}
```

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| ARCH-F-024 hooks | `governance/compat/run_local_governance_hook_chain.py` | CONFIRMED_EXISTING | no new value admitted | exclude |
| ARCH-F-023 adapter/profile semantics | `docs/reference/agent_system_skills/CVF_ASSF_CLI_MCP_ADAPTER_PROJECTION_STANDARD.md` | ENRICH_EXISTING | host-neutral delta unverified | bounded survey before final classification |

## Evidence / Verification

At authoring HEAD `f8fc0810c5f57bc3d475f9c6f0f1584008709a3c`,
the worktree was clean, all three planned output paths were absent, the two
indexed mirrors resolved to their frozen commits and trees, and read-only
`git ls-remote --symref` at `2026-09-15T02:26:32.8510192Z` observed each
selected pin at `refs/heads/main`. Pre-dispatch must pass after packet authoring.

## Corpus Completeness And Report Integrity

- Corpus task class: intake preparation; no semantic survey executed.
- Corpus root: the two exact mirror roots named in the paired work order.
- Snapshot time: `2026-09-15T02:26:32.8510192Z`.
- Enumeration command: future `rg --files --hidden --no-ignore` plus pinned `git ls-tree -r`; not executed here.
- Manifest artifact or inline manifest: two identities in the paired work order; zero executed corpus rows.
- Manifest hash: NOT_PRODUCED; worker output is not yet created.
- Processing ledger artifact or inline ledger: planned intake JSON; not yet created.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=0; ledger_terminal=0; exclusions=0; unresolved=0 for executed rows.
- Unresolved files: 0 executed rows; source-region totals remain UNKNOWN.
- Declared exclusions: all semantic source reading during packet authoring.
- Unreadable or unsupported files: not assessed.
- Aggregation check: not executed.
- Drift check: remote HEAD and selected pins matched at snapshot time.
- Output traceability: paired work order only.
- Adversarial verification: reject any complete-scan or absorption interpretation.
- Corpus verdict: PARTIAL - preparation only.

## Mandatory Blind-Spot Control Block

SKIPPED_WITH_REASON: authoring did not perform the source survey. The worker
must inspect operational consumers, failures, tests/examples and unread regions;
the external shortlist cannot define Local coverage.

## External Repository Absorption Entry Control

COMPARISON_ONLY_NO_ABSORPTION: the paired work order defines identities, pins,
inventory and terminal-ledger requirements before any Local value decision.

## Acceptance Criteria

Both pins are reconciled independently; manifest and terminal processing totals
match; read depth and exclusions are explicit; fork-only/upstream-only/shared
items are separated; every candidate names source path/symbol, current CVF
owner/collision, producer-verifier-consumer evidence and one disposition; the
hook finding and parked architecture dependency remain excluded; no forbidden
effect occurs; worker-return fast gate passes with an unchanged HEAD.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_gate_to_role_closeability.py`; source-intake checks through reviewer-fast catalog |
| literalTokensReviewed | dispatch-ready status, exact source-verification columns, initial-intake boundary, no-commit return shape, gate IDs |
| gateRunPurpose | confirm authored packet shape and evidence before relay |
| claimBoundary | checker read-ahead proves form awareness, not source value |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`external-absorption`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.
Command: `python governance/compat/run_adif_defect_resolver.py --task-class external-absorption --role dispatcher --lifecycle-phase pre-dispatch --risk-ceiling MEDIUM --json`.
Returned defect count: 0. Returned defects: NONE_RETURNED. Truncated: false.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind source-intake --batch-id ECC-ARCH-ABS-009-T0 --title "ECC Cross-Harness Adapter Profile Intake" --date 2026-09-15 --base f8fc0810c --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-surface INTERNAL_AGENT --include-worker-return-skeleton --stdout` |
| generatedProfile | source-intake plus no-commit worker |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with exact identities, pins, exclusions, owners and return contract |
| checkerReadAheadConfirmation | recorded above |
| docOnlyNewFields | none |
| claimBoundary | authoring provenance only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Private intake evidence only; no public artifact requested.

## Claim Boundary

This baseline releases only the paired bounded source survey. It neither accepts
ECC value nor authorizes runtime/profile behavior, architecture reopening,
provider use, public export or implementation.
