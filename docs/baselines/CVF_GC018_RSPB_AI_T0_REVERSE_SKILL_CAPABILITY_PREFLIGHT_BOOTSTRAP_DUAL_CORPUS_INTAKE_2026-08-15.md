# CVF GC-018 Baseline - RSPB-AI-T0 Reverse-Skill And Capability Preflight Bootstrap Dual-Corpus Intake

Memory class: governed-dispatch-baseline

Status: ACTIVE_DISPATCH_BASELINE

docType: baseline

Date: 2026-08-15

Batch ID: RSPB-AI-T0

Dispatch base head: 427a52639

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: independent reviewer/closer

Worker target: one documentation-only corpus-intake worker through operator manual copy/paste

## Purpose

Authorize a bounded, provider-free, read-only semantic intake of the pinned
`reverse-skill` upstream corpus and the separate CVF Capability Preflight &
Bootstrap proposal pack. The tranche must determine what value is already
owned, what safely enriches CVF, what merits a later package/runtime/checker
lane, and whether expected consumer value exceeds integration and maintenance
cost.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind source-intake --batch-id RSPB-AI-T0 --title "Reverse-Skill And Capability Preflight Bootstrap Pinned Dual-Corpus Intake" --date 2026-08-15 --base 427a52639 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | source-intake plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced stubs with pinned dual-corpus authority, exact boundaries, outputs, value/cost gate, and worker-return requirements |
| checkerReadAheadConfirmation | external absorption, corpus completeness, source mirror, dispatch, ADIF, handoff, trace, public export, and structural guard families were reviewed through guard orientation, current standards, scaffold output, and accepted source-intake precedent |
| docOnlyNewFields | `corpusRole`; `upstreamValueClass`; `proposalMaturity`; `valueCostDecision` |
| claimBoundary | dispatch authoring provenance only; no runtime, provider, public, security-target, package, CLI, MCP, or production behavior claim |

## Authorization / Decision

The operator selected the new repository and clarified that
`.private_reference/legacy/CVF 13.08/CVF_CAPABILITY_PREFLIGHT_BOOTSTRAP/` is
the new local proposal corpus. This baseline authorizes intake only. It does
not authorize implementation or execution of either corpus.

## Scope / Methodology

Allowed:

- filesystem-backed enumeration and direct reading of both pinned corpora;
- deterministic manifests, hashes, and per-file terminal ledgers;
- comparison with existing CVF owner surfaces;
- documentation-only value, cost, risk, overlap, and reopen classification;
- local CVF governance checks that do not execute source-corpus code.

Forbidden:

- running any script, test, installer, hook, CLI, MCP server, skill, toolchain,
  binary, or target workflow from either corpus;
- dependency installation, network activity beyond the already completed Git
  clone, credentials, provider calls, or live proof;
- security-target, penetration-test, reverse-engineering, CTF, browser, or
  external-account activity;
- copying external or proposal runtime code into active CVF source;
- runtime, checker, hook, registry-package, public-sync, deployment, or
  production mutation;
- staging or committing worker output.

Risk ceiling: R1 documentation and source-authority risk only.

## Corpus Accounting Target

| Corpus | Authority role | Dispatch snapshot | Required treatment |
| --- | --- | ---: | --- |
| `.private_reference/source_mirrors/zhaoxuya520__reverse-skill/` | pinned upstream authority for repository facts at `dd7c50dc38e778373cd037b3f47d5e132ef43a2f` | 559 Git-tracked files | exhaustive manifest and file-level semantic ledger |
| `.private_reference/legacy/CVF 13.08/CVF_CAPABILITY_PREFLIGHT_BOOTSTRAP/` | secondary CVF-shaped proposal pack | 205 filesystem files | separate exhaustive manifest and file-level semantic ledger |

Counts are dispatch-time expectations, not closure proof. The worker must
recompute them and stop on drift or unreadable files.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| upstream mirror is pinned and contains 559 tracked files | VALUE_SET | `.private_reference/source_mirrors/INDEX.md` | Mirror Ledger row `zhaoxuya520__reverse-skill` | `dd7c50dc38e778373cd037b3f47d5e132ef43a2f`; `559` | private source-mirror control plane | ACCEPT |
| upstream directs agents to immediate configuration and automatic tool handling | SOURCE_VISIBLE_BEHAVIOR | `.private_reference/source_mirrors/zhaoxuya520__reverse-skill/README_AI.md` | `0. First Instruction for the AI`; `Automatic Configuration Process` | immediate refresh/configuration and missing-tool bootstrap instructions | upstream agent bootstrap | ACCEPT |
| local proposal explicitly absorbs, adapts, and rejects selected upstream patterns | VALUE_SET | `.private_reference/legacy/CVF 13.08/CVF_CAPABILITY_PREFLIGHT_BOOTSTRAP/docs/reference/capability_preflight_bootstrap/README.md` | `5. Source absorption disposition` | `ABSORB`; `ADAPT`; `REJECT` | proposal profile | ACCEPT |
| local proposal remains unproven and reviewer disposition is unset | VALUE_SET | `.private_reference/legacy/CVF 13.08/CVF_CAPABILITY_PREFLIGHT_BOOTSTRAP/docs/reviews/capability_preflight_bootstrap/FINAL_CLOSURE_REVIEW.md` | status and disposition | `REVIEW_REQUIRED` | proposal review packet | ACCEPT |
| current CVF has existing likely owner surfaces | PATH_EXISTENCE | `docs/reference/agent_system_skills/README.md`; `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/`; `docs/reference/agent_workspace/README.md`; `docs/reference/mcp_gateway/README.md` | current paths | ASSF; Execution Plane; Agent Workspace; MCP Gateway | existing owner candidates | ACCEPT |

## External Repository Absorption Entry Control

| Field | Value |
| --- | --- |
| Source type | pinned external repository plus separate copied proposal folder |
| Upstream or source-mirror disposition | `MIGRATED_TO_SOURCE_MIRROR`; upstream facts must use the pinned mirror; proposal pack remains secondary interpretation |
| Enumeration or manifest plan | `git ls-files -z` for upstream and recursive hidden/no-ignore filesystem enumeration for the proposal pack; normalize repo-relative forward-slash paths |
| Per-file terminal-ledger plan | one row per manifest item with READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, or BLOCKED_UNREADABLE plus source-backed rationale |
| Owner or overlap route | ASSF, Execution Plane, Work Order, Guard Contract, Agent Workspace, MCP Gateway, interaction projection, learning owner, or `OWNER_SURFACE_NOT_FOUND` |
| Value-disposition route | doctrine adaptation, package candidate, runtime candidate, checker candidate, reject direct import, or no package/runtime value, with value/cost evidence |
| Claim boundary | documentation-only bounded intake; no implementation, execution, activation, public, provider, or production expansion |

## Mandatory Blind-Spot Control Block

The worker must keep the upstream and proposal corpora separate, enumerate
hidden and ignored files where applicable, account for every item, distinguish
processing status from value disposition, and preserve all deferred or blocked
value with a concrete next action. A summary or grouped directory count is not
complete corpus evidence.

## External Absorption Core

| Field | Value |
| --- | --- |
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | upstream URL and pinned mirror at `dd7c50dc38e778373cd037b3f47d5e132ef43a2f`; local proposal root named above |
| Enumeration command | filesystem-backed Git NUL listing for upstream and recursive direct filesystem enumeration for proposal files |
| Manifest artifact or inline manifest | `docs/audits/CVF_RSPB_AI_T0_REVERSE_SKILL_UPSTREAM_MANIFEST_2026-08-15.json`; `docs/audits/CVF_RSPB_AI_T0_CAPABILITY_PREFLIGHT_BOOTSTRAP_PROPOSAL_MANIFEST_2026-08-15.json` |
| Processing ledger artifact or inline ledger | `docs/audits/CVF_RSPB_AI_T0_REVERSE_SKILL_UPSTREAM_FILE_LEDGER_2026-08-15.json`; `docs/audits/CVF_RSPB_AI_T0_CAPABILITY_PREFLIGHT_BOOTSTRAP_PROPOSAL_FILE_LEDGER_2026-08-15.json` |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | inline `## Overlap And Novelty Classification`; `docs/reference/agent_system_skills/README.md`; `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/` |
| Unresolved items | must be zero for complete verdict or listed explicitly with a non-complete verdict |
| Completion claim boundary | bounded intake and recommendation only; no runtime/provider/public/production expansion |

## Corpus Completeness And Report Integrity

- Corpus task class: dual-corpus external repository and copied-folder intake.
- Corpus root: the two roots in Corpus Accounting Target.
- Snapshot time: worker execution start on 2026-08-15 or later.
- Enumeration command: filesystem-backed `rg --files --hidden --no-ignore -g '!.git/**'` against each corpus root; exact commands must be recorded by the worker.
- Manifest artifact or inline manifest: two output JSON manifests.
- Manifest hash: deterministic SHA-256 recipe with normalized relative paths,
  ordinal ordering, UTF-8 without BOM, LF separators, and trailing LF.
- Processing ledger artifact or inline ledger: two output JSON ledgers.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=764; ledger_terminal=0; exclusions=0; unresolved=764 at dispatch planning time.
- Unresolved files: 764 pending worker file-level processing.
- Declared exclusions: none for a complete verdict.
- Unreadable or unsupported files: none for a complete verdict.
- Aggregation check: upstream and proposal totals must remain separate and also sum correctly.
- Drift check: recompute HEAD, file counts, paths, sizes, and manifest hashes before return.
- Output traceability: every audit finding cites ledger selectors and direct source paths.
- Adversarial verification: reviewer rechecks high-risk, deferred, rejected, and no-value samples.
- Corpus verdict: PARTIAL

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
| --- | --- | --- | --- | --- | --- |
| deterministic routing and capability discovery | candidate-selection evidence | DOCTRINE_ADAPTED or PACKAGE_CANDIDATE | ASSF | compare with current resolver before proposing delta | no package activation |
| environment/tool inventory and freshness | readiness evidence | RUNTIME_CANDIDATE | Execution Plane plus ASSF binding | value/cost decision before implementation tranche | no scanner execution |
| approval-bound acquisition and receipt | controlled bootstrap transaction | RUNTIME_CANDIDATE | Execution Plane, Work Order, Guard Contract | preserve only if owner gap and measurable consumer value are proven | no install or mutation |
| repair-stop, provenance, integrity, and secret invariants | fail-closed verification | CHECKER_CANDIDATE | existing guard owners | identify non-duplicate invariant and future source-verified checker scope | no checker edit or wiring |
| upstream automatic configuration, rule injection, auto-install, and security workflows | unsafe direct behavior | REJECT_DIRECT_IMPORT | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | retain contrast evidence | no execution or import |
| duplicate domain playbooks or already-owned doctrine | no additional foundation value | NO_PACKAGE_OR_RUNTIME_VALUE | cited current owner | close with source-backed reason | no future action unless new demand appears |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| skill identity, resolution, and composition | `docs/reference/agent_system_skills/README.md` | ENRICH_EXISTING | environment-readiness evidence may improve selection without granting authority | audit exact delta |
| action authority and approved mutation envelope | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | CONFIRMED_EXISTING | upstream shortcuts conflict; proposal may add plan-digest binding | retain only bounded delta |
| scanning, acquisition, verification, and receipts | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/` | ENRICH_EXISTING | candidate seam exists but is unproven in active CVF | value/cost gate before runtime |
| external CLI/MCP projections | `docs/reference/mcp_gateway/README.md`; `docs/reference/agent_workspace/README.md` | REJECT_DIRECT_IMPORT | contract ideas may remain, but external runtime is not authorized | defer adapter implementation |
| direct upstream agent rules and security-domain runtime | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | REJECT_DIRECT_IMPORT | conflicts with CVF authority and task scope | reject |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | pinned source mirror plus proposal pack -> manifests and ledgers -> owner/overlap/value-cost decision -> reviewer disposition -> fresh implementation work order only if justified |
| Matching local-view guard | `governance/compat/check_external_absorption_core.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_source_mirror_migration.py`; `governance/compat/check_absorption_blindspot_control_presence.py` |
| Owner surface | this baseline and paired RSPB-AI-T0 work order |
| Disposition | ADAPT selected patterns; REJECT direct import; DEFER runtime/package/checker decisions to evidence |
| Claim boundary | intake routing only; no runtime, provider, public, package activation, security-target, or production claim |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`external-knowledge-absorption`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class external-knowledge-absorption --role dispatcher --lifecycle-phase pre-dispatch --surface-selector reverse-skill --risk-ceiling HIGH --max-results 20 --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | no returned packet changes the explicit blind-spot, authority, and no-execution controls |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_source_mirror_migration.py`; `governance/compat/check_absorption_blindspot_control_presence.py` |
| literalTokensReviewed | required headings and terminal status, disposition, overlap, no-commit, public-export, and worker-return tokens |
| gateRunPurpose | final gates confirm the packet; they are not used as the first source of requirements |
| claimBoundary | structural read-ahead only; semantic quality remains reviewer-owned |

## Acceptance Criteria

- both corpora have reproducible manifests and one terminal row per file;
- upstream and proposal authority roles never merge;
- direct import and all source execution remain rejected;
- every retained concept maps to an existing owner or visible missing-owner decision;
- the audit gives a concrete `PROCEED_SELECTIVELY`, `STOP_COST_EXCEEDS_VALUE`,
  or `BLOCKED_INSUFFICIENT_EVIDENCE` decision;
- any retained package/runtime/checker candidate has measurable value,
  estimated integration cost, risk, and reopen evidence;
- worker output is uncommitted and independently reviewable.

## Baseline Decision

`AUTHORIZED_FOR_DOCUMENTATION_ONLY_DUAL_CORPUS_INTAKE`.

No implementation tranche is authorized by this decision.

## Verification / Evidence

The paired work order owns exact commands and output paths. Reviewer acceptance
must include current Git status, manifest/ledger reconciliation, semantic
sampling, and applicable governance gate results.

## Machine Closure Package

| Surface | Disposition |
| --- | --- |
| baseline and work order | dispatcher-owned and committed before worker execution |
| manifests, ledgers, audit, registry source, generated registry, conditional reopen index if needed, worker return | worker-owned pending outputs |
| completion decision and commit | reviewer/closer-owned |
| continuity update | separate reviewer/closer session-sync action after acceptance |

## Acceptance Receipt Assertion Matrix

| Assertion | Required evidence | Current status |
| --- | --- | --- |
| pinned upstream identity | mirror index plus Git HEAD | SATISFIED at dispatch |
| corpus completeness | two manifests and two ledgers | PENDING_WORKER |
| semantic value conversion | audit plus reviewer sampling | PENDING_WORKER_AND_REVIEW |
| runtime readiness | live integrated proof | NOT_AUTHORIZED |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is private provenance intake authority and contains private local
paths, internal owner mapping, and unreviewed external-source classifications.

## Claim Boundary

This baseline authorizes documentation-only intake of two bounded corpora. It
does not prove absorption completion, source safety, package quality, runtime
integration, external-agent support, CLI/MCP availability, provider behavior,
public readiness, security-task authority, deployment, or production value.
