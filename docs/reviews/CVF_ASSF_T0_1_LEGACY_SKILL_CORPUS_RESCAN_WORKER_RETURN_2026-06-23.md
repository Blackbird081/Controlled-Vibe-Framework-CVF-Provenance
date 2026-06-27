# CVF ASSF-T0.1 Legacy Skill Corpus Rescan Worker Return

Memory class: FULL_RECORD

Status: ACCEPTED_BY_REVIEWER

Date: 2026-06-23

docType: review

Batch ID: ASSF-T0.1

Commit mode: WORKER_MUST_NOT_COMMIT

executionBaseHead: `3f51a4cc`

closureBaseHead: PENDING_REVIEWER_CAPTURE

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_FOR_WORKER_2026-06-23.md`

## Purpose

Return the ASSF-T0.1 legacy skill corpus rescan and absorption candidate
ledger to the Codex reviewer/closer, per
`docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_FOR_WORKER_2026-06-23.md`,
without committing.

## Target / Source

Target: `.private_reference/legacy/` (629 files, full root). Source authority:
`docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_FOR_WORKER_2026-06-23.md`
and `docs/baselines/CVF_GC018_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_2026-06-23.md`.

## Scope / Methodology

Read the active session front door, active session state, active handoff,
guard orientation index, this work order, the GC-018 baseline, and the ASSF
roadmap. Ran the pre-implementation autorun gate at current clean HEAD.
Enumerated the full `.private_reference/legacy/` root with
`rg --files --hidden --no-ignore` (629 files). Ran the required keyword
search (`skill|skills|package|toolset|formation|lifecycle|normalization|memento|adapter|mcp|cli|adk|governed evolution`,
case-insensitive) over the full legacy root (4855 hits across 422 files) and
over the named current-surface roots (`governance/skill-library/`,
`docs/roadmaps/`, `docs/reference/`, `EXTENSIONS/`). Ran a basename-collision
scan against the legacy manifest. Read the highest-signal candidate files
directly (content excerpts recorded in the audit ledger) and diff-verified
the two basename-collision pairs found. Authored the audit ledger and this
return packet; ran the worker-return fast gate and reviewer-fast hook chain.

## Findings / Position

The legacy corpus is much broader than the four ASSF-T0 seed folders: 422 of
629 files (67%) carry at least one required keyword, across 9 top-level
families, only 4 of which were previously seeded. The audit ledger
(`docs/audits/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_AUDIT_2026-06-23.md`)
classifies the highest-signal candidates with source-backed dispositions,
finds two basename-collision pairs inside legacy itself
(`CVF_SKILL_MODEL.md` x2, `CVF_SKILL_NORMALIZATION_SCHEMA.md` x2 with an
`HF_` prefix variant), and confirms `governance/skill-library/` as the
existing CVF-owned current surface that legacy candidates must reconcile
against, not duplicate. The strongest concrete inputs for a future ASSF-T1
canonical package contract are `CVF_HF_SKILL_NORMALIZATION_SCHEMA.md` (21
named fields) and `CVF_HERMES_SKILL_PACKAGE_MODEL.md` (a distinct,
complementary field set); the strongest lifecycle-resolver input is
`CVF_SKILL_ACTIVATION_PROFILE_SPEC.md`.

## Risk / Corrective Action

Risk: treating the T0 seed folders as sufficient legacy coverage would have
caused ASSF-T1 to miss the schema and resolver candidates above, plus the
CLI/MCP-relevant registry/adapter candidates (`CVF_SKILL_REGISTRY.md`'s
`cvf skill publish/install/search` verb set; `CLI-Anything`'s CLI-as-agent-
interface argument). Corrective action taken: this return and the paired
audit explicitly reject seed-only and memory-only corpus claims (see
Adversarial Verification in the audit's Corpus Completeness section) and
flag 6 high-keyword-hit files as `BLOCKED_UNVERIFIED_SOURCE` for priority
follow-up reads rather than silently omitting them.

## Worker Status

`ACCEPTED_BY_REVIEWER`

No Stop Condition was triggered. All Required Execution Steps in the work
order were completed within Allowed Scope.

## Required Artifact Manifest

| Required output | Path | Status |
|---|---|---|
| T0.1 audit ledger | `docs/audits/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_AUDIT_2026-06-23.md` | CREATED |
| T0.1 worker return | `docs/reviews/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_WORKER_RETURN_2026-06-23.md` | CREATED (this file) |
| T0.1 completion review | a reviewer-created completion review under the reviews directory, named to mirror this return | REVIEWER_OWNED_AFTER_RETURN, not created by worker |
| Material commit | N/A | REVIEWER_OWNED_AFTER_RETURN, not performed by worker |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Worker evidence produced | Disposition |
|---|---|---|---|
| Full legacy-root scan before T1 | run full enumeration and keyword search | 629-file manifest; 4855-hit/422-file keyword search; both command-backed | SATISFIED |
| Seed folders included but not treated as complete | inspect named seed paths and compare against broader scan | Seed Folder Coverage table in audit (24 of 629 files, under 4%) | SATISFIED |
| Candidate absorption ledger | classify candidates into allowed dispositions | 24-row Absorption Candidate Ledger in audit, all using allowed disposition values | SATISFIED |
| Legacy stays non-canonical until re-expressed | claim boundary and source-fidelity notes | audit's Claim Boundary and Source-Fidelity Notes sections; this return's Claim Boundary | SATISFIED |
| No implementation/migration | forbidden scope and changed-set evidence | `git status --short` below shows only the two allowed new files | SATISFIED |
| Dual-agent accounting | internal and external CLI/MCP implications | Dual Agent Surface Matrix in audit plus per-row ledger columns | SATISFIED |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | future ASSF package loader, generated index, and resolver design (T1/T4) | this return produces classified candidates only; no internal loader behavior, package authority, or schema freeze | audit's Absorption Candidate Ledger `Internal-agent implication` column | no adapter implemented; no loader code written | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future external CLI/MCP package discovery/load adapter (T7-class) | several candidates are explicitly CLI/MCP-relevant but none are exposed or implemented as an adapter | audit's Absorption Candidate Ledger `External-agent CLI/MCP implication` column | adapter implementation explicitly out of scope; deferred to a separate later tranche | `DEFERRED_WITH_REASON` |

## Corpus Completeness And Report Integrity

- Corpus task class: LEGACY_RESCAN_WORKER_RETURN.
- Corpus root: `.private_reference/legacy/`.
- Snapshot time: 2026-06-23, local session.
- Enumeration command: `rg --files --hidden --no-ignore .private_reference/legacy` -> 629 files.
- Manifest artifact or inline manifest: inline summary in the paired audit's
  Legacy Manifest Summary section; raw 629-line command output retained in
  this session's scratch directory only, not a committed governed artifact.
- Manifest hash: N/A with reason: text-only inline manifest, no binary to hash.
- Processing ledger artifact or inline ledger: the paired audit's Absorption
  Candidate Ledger section (24 rows).
- Allowed terminal statuses: READ used for content-verified rows;
  SKIPPED_WITH_REASON used for seed-adjacent sibling files not re-read this
  session; DEFERRED not used; BLOCKED_UNREADABLE not encountered (0 unreadable
  files).
- Reconciliation: manifest=629; keyword_hits=4855 across 422 files; ledger_terminal=24 ledger rows covering all distinct skill-relevant families; exclusions=binary assets (none found), generic per-folder seed notes beyond their family row, ~207 zero-keyword-hit files; unresolved=0.
- Unresolved files: 0
- Declared exclusions: see audit's Corpus Completeness section; no
  migration/package/index/runtime/public/adapter surface created.
- Unreadable or unsupported files: 0.
- Aggregation check: N/A with reason: no generated aggregate created.
- Drift check: N/A with reason: no generated aggregate created.
- Output traceability: every ledger row maps to a manifest path; rows with a
  non-`REFERENCE_ONLY`/`BLOCKED_UNVERIFIED_SOURCE` disposition cite a content
  excerpt read in this session.
- Adversarial verification: explicitly rejected seed-only coverage (seed
  folders are under 4% of total legacy files and a minority of keyword-hit
  files) and memory-only coverage (every disposition traces to a command run
  or file read in this session).
- Corpus verdict: PARTIAL

## Legacy Spec Scan Block

| Field | Worker evidence |
|---|---|
| Scan root | `.private_reference/legacy/` |
| Required seed paths | all 4 covered; see audit's Seed Folder Coverage table |
| Search roots outside legacy | `governance/skill-library/`, `docs/roadmaps/`, `docs/reference/`, `EXTENSIONS/` all searched |
| Required query terms | all 13 terms searched in one combined regex pass |
| Negative evidence rule | `CVF 25.05/`, `CVF 28.05/` confirmed present in manifest with zero keyword hits |
| Collision evidence rule | two basename-collision pairs found, diff-verified, and ledgered (not dropped) |

## Knowledge Absorption Blind-Spot Control Block

| Required control | Worker evidence |
|---|---|
| Open tabs are not corpus coverage | full-root command enumeration used, not the opened-tab seed set alone |
| T0 owner audit is not corpus completeness | T0's completion review confirmed (by full-text grep) to contain zero mentions of `governance/skill-library/` reconciliation against legacy beyond the 4 seeds; T0.1 closes that specific gap |
| Name-only search is insufficient | 18 of 24 ledger rows are content-verified, not name-only; 6 are explicitly labeled `BLOCKED_UNVERIFIED_SOURCE` rather than guessed |
| Legacy direct adoption is forbidden | every ledger row uses a candidate-class disposition; Claim Boundary sections in both artifacts restate this |
| External-agent disposition is mandatory | every ledger row has a non-empty `External-agent CLI/MCP implication` cell |

## Negative Search And Collision Evidence

- Negative evidence: `CVF 25.05/` (2 files) and `CVF 28.05/` (5 files) are
  present in the manifest with zero keyword hits; ruled out as a missing-path
  artifact.
- Collision evidence: `governance/skill-library/` confirmed as an existing,
  substantial current-surface skill system (specs, 34 `agent-skills` plus 149
  `user-skills` registry entries, UAT, dedupe pipeline, external-intake
  script) already source-verified by ASSF-T0; this return's ledger is written
  to feed reconciliation against that surface, not to compete with it.
- Internal legacy collision: `CVF_SKILL_MODEL.md` (2 files, materially
  different content per diff) and `CVF_SKILL_NORMALIZATION_SCHEMA.md` (2
  files, one HF-source-specific and field-level, one plane-level and generic)
  both ledgered as distinct candidates with an explicit collision note.

## External Knowledge Intake Routing

| Field | Worker evidence |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` cited in the paired audit |
| Input type | Legacy source family |
| Chain map route | legacy source family -> absorption blind-spot control -> ASSF candidate ledger -> reviewer decision; this return is the candidate-ledger-to-reviewer-decision handoff point |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | ASSF-T0.1 audit and future ASSF-T1/T4 normalization decisions |
| Disposition | candidate intake only; no direct canonical authority or activation claimed |
| Route | applied per the Knowledge Absorption Blind-Spot Control Block above |
| Boundary | candidate input only |
| External-agent disposition | present in matrix and in every ledger row |
| Claim boundary | legacy and external skills remain candidate inputs, not CVF authority |

## Rescan Intelligence Hardening

- Original source artifact: `docs/reviews/CVF_ASSF_T0_SKILL_SURFACE_OWNER_LEGACY_ABSORPTION_COMPLETION_2026-06-23.md`
- Predecessor intake artifact: `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md`
- Delta ledger status: REFRESHED (see Original-Intake Delta Ledger below)
- Routing matrix status: REFRESHED (see Follow-Up Routing Matrix below)
- Semantic sampling status: 3 samples included below
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Delta category | Worker finding |
|---|---|
| `UNCHANGED_FROM_INTAKE` | T0's finding that `governance/skill-library/` is the existing current-surface owner remains valid and unchanged |
| `CHANGED_DISPOSITION` | legacy corpus status changes from "4 seeded folders" (T0 framing) to "422 keyword-hit files across 9 families, 24 classified in this ledger" (T0.1 framing) |
| `NEW_FINDING` | 2 basename-collision pairs inside legacy; 5 non-seed families with strong skill-relevant content (Hugging Face, Hermes Agent, Workflow GoClaw, caveman, gridex) |
| `REMOVED_OR_REJECTED` | open-tab-only and memory-only corpus claims rejected; `App onboarding/` UI mockups and ~207 zero-keyword-hit files rejected as out-of-domain for ASSF |

### Follow-Up Routing Matrix

| Routing lane | Worker disposition |
|---|---|
| `DO_NOW` | scan and classify completed within this T0.1 return |
| `SEPARATE_RUNTIME_TRANCHE` | any CLI/MCP adapter, runtime, or migration work stays out of scope, routed to a future T7-class tranche |
| `STRATEGIC_OPERATOR_DECISION` | `gridex`'s W7-coupled skill-formation terminology needs an explicit operator/T1 decision since W7 is a current, not legacy-only, surface |
| `OUT_OF_SCOPE` | package creation, generated index, resolver, public-sync remain out of scope |
| `RESOLVED_BY_DESIGN` | the no-commit worker-return lane itself prevented any premature legacy-authority promotion in this tranche |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| ASSF-T0.1-WR-S1 | `CVF_HF_SKILL_ABSORPTION_SPEC.md` Non-Negotiable Invariants | "no skill executable before normalization, classification, approval, publication" | `ABSORB_AS_LIFECYCLE_INPUT`, not `ABSORB_AS_TOOL_ADAPTER_INPUT` | could this spec be read as authorizing direct execution since it is detailed and CVF-native? | rejected - spec explicitly states it grants no execution authority |
| ASSF-T0.1-WR-S2 | basename-collision pair `CVF_SKILL_MODEL.md` | two files, same name, different content | both ledgered as distinct candidates rather than treating the second as a stale duplicate of the first | could the second file be silently dropped as "probably the same thing"? | rejected - full diff performed, content materially differs, both kept |
| ASSF-T0.1-WR-S3 | `CVF_SKILL_REGISTRY.md` `cvf skill publish/install/search` | explicit CLI verb set | `EXTERNAL_AGENT_CLI_MCP` implication marked present, not "none stated" | could this be read as internal-only since the file does not say "external agent"? | rejected - a CLI verb surface is inherently an external-agent-facing interface design, ledgered as CLI/MCP-relevant |

## Finding-To-Governance Learning Disposition

| Field | Worker value |
|---|---|
| Defect class | `RULE_GAP` (work-order-local label: legacy scan coverage gap) |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Disposition | `MACHINE_CHECK_CANDIDATE` |
| Runtime/provider/cost lane | N/A_WITH_REASON: this finding is a documentation-and-evidence-coverage gap, not a runtime, provider, or cost-economics finding |
| Next control action | T1 (or a dedicated future ASSF gate) should require a manifest line count and keyword-hit file count in the Source Verification Block of any work order whose roadmap trace lists legacy absorption as a precondition. See Machine-Check Candidate Notes in the paired audit for two concrete candidate-guard shapes. |

## Epistemic Process Block

EPISTEMIC_PROCESS_NA_WITH_REASON: this return classifies and reports on
filesystem-backed legacy content; it does not assert a new factual claim
about CVF runtime or provider behavior beyond what the cited files and
commands directly show. All claims trace to a command output or a direct
file read recorded in the paired audit's Agent Operation Trace Block.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | this worker return and the paired audit's legacy scan and candidate ledger only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - no-commit worker-return dispatch only |
| receiptEvidence | CVF_RECEIPT_PRESENT - command outputs and gate run captured below |
| actionEvidence | ACTION_EVIDENCE_PRESENT - manifest counts, ledger rows, collision diffs |
| invocationBoundary | governed local filesystem scan and documentation return |
| interceptionBoundary | no provider/runtime/API/browser interception claim |
| claimLanguage | scan and classify legacy skill candidates |
| forbiddenExpansion | no commit, package root, generated index, resolver, runtime, CLI/MCP adapter, public-sync, or active skill claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance scan over `.private_reference/legacy/`. Public-safe
skill architecture output requires later redaction and public-sync authority.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Roadmap state | `docs/roadmaps/CVF_AGENT_SYSTEM_SKILLS_FOUNDATION_ROADMAP_2026-06-23.md` | unchanged by worker; reviewer owns roadmap status update | N/A with reason: reviewer-owned |
| GC-018 status | `docs/baselines/CVF_GC018_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_2026-06-23.md` | `Status: DISPATCH_READY` (unchanged by worker) | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_FOR_WORKER_2026-06-23.md` | `Status: DISPATCH_READY` (unchanged by worker) | PASS |
| Worker return | this file | `Status: ACCEPTED_BY_REVIEWER` | PASS |
| Audit ledger | `docs/audits/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_AUDIT_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion review | `docs/reviews/CVF_ASSF_T0_1_LEGACY_SKILL_CORPUS_RESCAN_COMPLETION_2026-06-23.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | N/A with reason | no GC-051 registry update authorized by this work order | N/A with reason |
| Registry Markdown | N/A with reason | no GC-051 registry update authorized by this work order | N/A with reason |
| Session continuity | active session sync after material commit if next move changes | reviewer-owned separate sync lane | PENDING |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |
| Runtime/provider/live | N/A with reason | no runtime/provider/live claim | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Worker commit mode | `WORKER_MUST_NOT_COMMIT` | no commit performed by worker | PASS |
| Allowed output paths | audit and worker-return only | only those two files created | PASS |
| External-agent disposition required | yes | present in matrix and every ledger row | PASS |
| Package/root/index/resolver implementation | forbidden | none created | PASS |
| Legacy root edited | forbidden | zero edits under `.private_reference/legacy/` | PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | ASSF-T0.1 worker (Claude) |
| Provider or surface | local workspace |
| Session or invocation | ASSF-T0.1 worker execution, 2026-06-23 |
| Working directory | repository root |
| Command or tool surface | `rg --files --hidden --no-ignore`, `rg -n -i` keyword search, Python dup-scan and summary scripts in session scratch directory, direct file reads, `git status --short`, `git rev-parse --short HEAD`, governance gate invocations |
| Target paths | `.private_reference/legacy/` (read-only); this file and the paired audit (write) |
| Allowed scope source | work order Allowed Scope section |
| Before status evidence | clean worktree at HEAD `3f51a4cc` |
| After status evidence | this file and the paired audit created; `git status --short` shows exactly those two untracked files |
| Diff evidence | `git status --short` output below |
| Approval boundary | worker execution only; no commit |
| Claim boundary | candidate ledger and scan evidence only |
| Agent type | worker |
| Invocation ID | `cvf-assf-t0-1-legacy-skill-corpus-rescan-worker-2026-06-23` |
| Expected manifest | this file; the paired audit |
| Actual changed set | this file; the paired audit |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

This worker return and the paired audit provide a legacy skill corpus scan
and absorption candidate ledger only. They do not migrate any legacy file,
create a canonical package root, generate an index, implement a resolver,
implement a CLI/MCP adapter, claim runtime/provider/live/public behavior, or
authorize ASSF-T1. Codex reviewer accepted this packet in the paired
completion review; ASSF-T1 still requires separate operator selection and
fresh source-verified dispatch.
