# CVF Agent Work Order - PINT-R1 Full Corpus Content Rescan And MCP Value Reconciliation

Memory class: POINTER_RECORD

Status: DISPATCH_READY

Batch ID: PINT-R1

Dispatch base head: 23f4e1657

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated documentation worker

Reviewer/closer: independent reviewer/closer

Worker return path: `docs/reviews/CVF_PINT_R1_FULL_CORPUS_CONTENT_RESCAN_WORKER_RETURN_2026-07-23.md`

## Dispatch Prompt Envelope

Role: delegated no-commit documentation worker. A separate independent
reviewer/closer owns acceptance.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_PINT_R1_FULL_CORPUS_CONTENT_RESCAN_AND_MCP_VALUE_RECONCILIATION_2026-07-23.md`.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: capture `git rev-parse --short HEAD` before edits; it must
equal the exact execution head supplied by the operator with this prompt.

Current-time notes: no live key, provider, account, subscription, network,
browser, external CLI/MCP invocation, or process-control action is authorized.

Do-not-misread notes: this is a file-by-file local knowledge rescan, not
authorization to build or test MCP/CLI control runtime. Internal Explore,
Read, Grep, and Glob helpers inside the parent worker session are allowed and
inherit the parent internal-agent boundary.

Required first actions: read `CVF_SESSION_MEMORY.md`, resolve
`CVF_SESSION/ACTIVE_SESSION_STATE.json`, read its active handoff,
`docs/reference/guard_orientation/README.md`, the paired GC-018 baseline, this
work order, literal gotchas, and all checker sources in the read-ahead block;
then verify HEAD, clean worktree, and the 50-file corpus.

Return contract: return `COMPLETE_PENDING_REVIEW` only with exact changed paths,
executionBaseHead, 50-row reconciliation, gate results, empty staged diff, and
unchanged HEAD. Otherwise return `BLOCKED_WITH_REASON`.

## Purpose

Read and semantically classify every file in the retained Provider Intelligence
corpus, recover useful doctrine missed by the predecessor representative scan,
and produce a reviewer-auditable reconciliation. Particular care is required
for every file in `docs/absorptions`; folder-level summaries are forbidden.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind source-intake --batch-id PINT-R1 --title "Provider Intelligence Full Corpus Content Rescan And MCP Value Reconciliation" --date 2026-07-23 --base 23f4e1657 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | source-intake plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled current source, rescan, corpus, handoff, role, output, and claim-boundary evidence |
| checkerReadAheadConfirmation | all checker paths listed in the read-ahead block |
| docOnlyNewFields | semantic locator, EAIC relevance, actual-usage distinction, receipt-layer disposition |
| claimBoundary | dispatch provenance only; no runtime/provider/live/public/MCP behavior |

## Authority Chain

- Operator instruction: 2026-07-23 full file-content rescan request.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: resolved from the active session state.
- Paired GC-018:
  `docs/baselines/CVF_GC018_PINT_R1_FULL_CORPUS_CONTENT_RESCAN_AND_MCP_VALUE_RECONCILIATION_2026-07-23.md`.
- Predecessor roadmap:
  `docs/roadmaps/CVF_PINT_T0_PROVIDER_INTELLIGENCE_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md`.
- Existing doctrine owner:
  `docs/reference/CVF_PINT_T2_PROVIDER_INTELLIGENCE_CLAIM_BOUNDARY_AND_RECEIPT_ADVISORY_2026-06-28.md`.
- Existing checker decision:
  `docs/reviews/CVF_PINT_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md`.
- Current MCP/CLI knowledge-gap owner:
  `docs/reference/external_agent_invocation_control/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_GAP_AND_SOURCE_ACQUISITION_MAP.md`.

## Worker Autonomy / No-Question Rule

Proceed autonomously with local reads, safe enumeration, hashing, JSON parsing,
documentation edits in Allowed Outputs, and allowed-scope checker remediation.
Escalate only for corpus drift, unreadable source without a safe parser,
contradictory authority, or a required edit/action outside Allowed scope.

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| Intake summary | operator request to rescan a retained legacy copied folder |
| Scope classification | bounded documentation-only four-output allowed scope |
| Risk sensitivity | provider, live, secret, production, public-sync, and runtime actions are forbidden |
| Selected role route | `MULTI_AGENT_MULTI_ROLE` |
| Role separation basis | delegated worker; separate dispatcher, independent reviewer, and closer |
| Escalation condition | stop and return blocked on corpus drift, authority conflict, or forbidden-scope need |
| Decision | execute bounded source-intake rescan |

## Agent Roles

- Dispatcher: dispatcher role.
- Worker: delegated worker role.
- Reviewer/closer and commit owner: independent reviewer/closer role.
- Operator owns any future runtime, CLI/MCP invocation, provider, public,
  package, checker, or moratorium decision.

## Required First Reads

1. Startup and guard-orientation files named in the envelope.
2. Paired PINT-R1 GC-018 and this work order.
3. External absorption core, corpus completeness, corpus-to-knowledge,
   rescan-hardening, dual-agent, handoff, and worker-return standards.
4. PINT-T0, PINT-T2, PINT-T3, and the EAIC knowledge-gap map.
5. Checker sources listed in Checker Source Read-Ahead Block.

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short --untracked-files=all
Get-ChildItem -LiteralPath '.private_reference/legacy/CVF_PROVIDER_INTELLIGENCE' -Recurse -File
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 23f4e1657 --head HEAD
```

The worktree must be clean at worker start and corpus count must be 50. If the
operator supplies a later committed execution head, use it for the unchanged
HEAD assertion while preserving `23f4e1657` as the dispatch-authoring base.

## Write Ownership

Exactly these four Allowed Outputs:

1. create
   `docs/audits/CVF_PINT_R1_FULL_CORPUS_CONTENT_RESCAN_AND_MCP_VALUE_RECONCILIATION_2026-07-23.md`;
2. create
   `docs/corpus-intelligence/registry/entries/pint-r1-provider-intelligence-full-content-rescan.json`;
3. regenerate
   `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` only through
   `governance/compat/generate_corpus_scan_registry.py`;
4. create
   `docs/reviews/CVF_PINT_R1_FULL_CORPUS_CONTENT_RESCAN_WORKER_RETURN_2026-07-23.md`.

No other path may change. Do not stage or commit.

## Scope / Methodology

1. Enumerate with filesystem truth, including hidden and ignored paths.
2. Recompute the 50-file path and content manifest digests using the paired
   baseline recipes.
3. Create exactly one ledger row per file. Do not group a folder into one row.
4. Open or parse all 44 non-bytecode files.
5. For each of the 16 files in
   `docs/absorptions/openrouter-provider-intelligence`, record an exact section
   or semantic region and either extracted value or a specific no-new-value
   reason.
6. Parse all seven hidden JSON receipts individually and distinguish advisory
   or estimated fields from actual observed invocation/session usage.
7. Read all six Python source/test files. Reject direct checker import while
   testing whether a CVF-native invariant is genuinely novel.
8. Inventory all six bytecode files and record generated/binary status plus
   readable sibling source evidence. Do not decompile them.
9. Compare every useful concept against current PINT and EAIC owner surfaces.
10. Route accepted documentation deltas, candidates, rejections, and exact
    no-new-value dispositions without claiming runtime sufficiency.

## Execution Plan

1. Verify startup state, execution head, clean worktree, and 50-file inventory.
2. Recompute both deterministic digests and build the per-file ledger.
3. Read or parse each authorized content file and classify every binary file.
4. Compare extracted value against PINT-T2, PINT-T3, and EAIC owner surfaces.
5. Author the audit and registry source entry, then regenerate the aggregate.
6. Author the worker return, run gates, repair allowed-scope defects, and stop
   with the required return token.

Each step stops on unexplained drift, unreadable source, authority conflict, or
need for a forbidden action.

## Evidence Requirements

Evidence must include exact path counts, extension counts, deterministic hash
recipes and values, one terminal row per file, semantic locators for all
readable files, sibling-source reasons for bytecode, owner comparisons, honest
gap statements, registry generation evidence, exact before/after Git status,
empty staged diff, unchanged HEAD, and command-backed gate outcomes.

## Required Per-File Ledger Shape

Every row must include:

| Field | Requirement |
| --- | --- |
| path | corpus-relative forward-slash path |
| extension and bytes | current filesystem evidence |
| processing status | one canonical terminal status |
| parser or read method | exact local method |
| semantic locator | section, JSON field path, Python symbol, or binary reason |
| extracted value | specific value or `NO_NEW_VALUE` with reason |
| predecessor overlap | PINT-T0/T2/T3 relation |
| EAIC relevance | exact gap or `N/A with reason` |
| disposition | canonical absorption disposition |
| CVF owner | existing owner, conditional index, or explicit owner gap |
| claim boundary | no inferred runtime authority |

Canonical processing status and planning disposition are separate fields.

## High-Value Questions

The audit must answer, with per-file evidence:

- Which TTL, staleness, provider-health, fallback, approval, and fail-closed
  semantics enrich existing PINT doctrine?
- Which receipt fields distinguish dev MCP probe, routing decision, and
  cost/latency/quality layers?
- Which fields are estimates or declared observations rather than actual
  session-wide token, quota, subscription, retry, subagent, or spend evidence?
- Does the corpus add any evidence for launch admission, descendant identity,
  cumulative budget, unknown-usage fail-closed behavior, bypass resistance,
  cost-aware task compilation, or end-to-end reconciliation?
- Which useful concept belongs in an existing owner and which must remain
  conditionally parked?

Absence of evidence must not be converted into a capability claim.

## Required Audit Sections

The audit must contain real sections for:

- Target / Source;
- Manifest And Hash Recipe;
- Per-File Processing Ledger;
- Corpus Completeness And Report Integrity;
- Knowledge System Reconciliation;
- External Absorption Core;
- External Absorption Value Conversion Matrix;
- Overlap And Novelty Classification;
- Rescan Intelligence Hardening;
- MCP/CLI Knowledge Contribution;
- Receipt Layer Separation;
- Existing Owner Enrichment Proposals;
- Conditional Reopen Index Disposition;
- External Knowledge Intake Routing;
- Epistemic Process Block;
- Finding-To-Governance Learning Disposition;
- Agent Operation Trace Block;
- Public Export Disposition;
- Claim Boundary.

Do not write heading-prefixed checklist literals before the actual sections.

## Registry Requirements

Create one compact source entry under the generated registry source layout,
following current sibling entry schemas. Record the 50-file manifest count,
snapshot digest, audit path, source root, processing verdict, mapped/deferred/
unmapped totals, and bounded claim. Run the generator; do not hand-edit only
the aggregate.

The registry entry is a discoverability record, not proof that every semantic
claim is true and not runtime authorization.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| PINT predecessor is closed and bounded | VALUE_SET | `docs/roadmaps/CVF_PINT_T0_PROVIDER_INTELLIGENCE_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` | Machine Closure Package | `Status` | PINT roadmap | ACCEPT |
| PINT advisory owner exists | EXISTS | `docs/reference/CVF_PINT_T2_PROVIDER_INTELLIGENCE_CLAIM_BOUNDARY_AND_RECEIPT_ADVISORY_2026-06-28.md` | Owner Surface Matrix | provider intelligence advisory | PINT-T2 reference | ACCEPT |
| PINT checker decision exists | VALUE_SET | `docs/reviews/CVF_PINT_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | Decision | `CLOSE_PINT_ABSORPTION_LANE_NO_CHECKER_NOW` | PINT-T3 review | ACCEPT |
| EAIC is knowledge-gap parked | VALUE_SET | `docs/reference/external_agent_invocation_control/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_GAP_AND_SOURCE_ACQUISITION_MAP.md` | Position | `PARKED_KNOWLEDGE_GAP` | EAIC map | ACCEPT |
| corpus source exists | EXISTS | `.private_reference/legacy/CVF_PROVIDER_INTELLIGENCE` | recursive filesystem enumeration | corpus root | retained legacy source | ACCEPT |
| generated corpus registry layout exists | EXISTS | `docs/corpus-intelligence/registry/` | current source fragments | registry entries | corpus registry generator | ACCEPT |

## Mandatory Blind-Spot Control Block

ADIF-0014 and ADIF-0019 apply. Every manifest item must receive file-level
processing evidence. Gate success does not waive semantic review of deferred,
rejected, or no-new-value rows, especially under `docs/absorptions`.

## External Repository Absorption Entry Control

| Field | Value |
| --- | --- |
| Source type | retained legacy copied folder |
| Upstream or source-mirror disposition | LEGACY_REFERENCE_ONLY_WITH_REASON: no upstream repository completeness claim is made |
| Enumeration or manifest plan | hidden-aware filesystem enumeration of 50 files |
| Per-file terminal-ledger plan | one terminal row per file |
| Owner or overlap route | current PINT/EAIC owner or conditional reopen index |
| Value-disposition route | adapt, defer, reject, or close with exact reason |
| Claim boundary | no runtime, provider, network, public, or external invocation |

## New Doc-Only Fields

| Field | Purpose | Runtime status |
| --- | --- | --- |
| semantic locator | prove each file was content-reviewed | documentation only |
| EAIC relevance | map value to current knowledge gaps | documentation only |
| actual-usage distinction | prevent estimate/session telemetry conflation | documentation only |
| receipt-layer disposition | separate probe, routing, CLQ, and missing invocation receipt | documentation only |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| target baseline and work order collision | pre-authoring `Test-Path` returned false | ACCEPT |
| PINT-R1 token collision | exact search across docs and session state returned no existing target | ACCEPT |
| worker output collision | worker must run `Test-Path` before edit and block on unexplained existing content | ACCEPT |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact:
`docs/roadmaps/CVF_PINT_T0_PROVIDER_INTELLIGENCE_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md`

priorVerificationAnchor: accepted PINT-T0 through T3 owner decisions

recomputeReason: the predecessor scan did not prove current 50-file per-file
content coverage, including hidden JSON and generated binary paths

freshRecomputeRequired: YES; inventory, digests, every per-file semantic row,
overlap, and knowledge-map arithmetic

unicodePathHandling: use literal PowerShell paths and UTF-8-safe text/JSON
readers; do not normalize source filenames

extractedTextAuthority: AUXILIARY_ONLY

The local source files remain external evidence; CVF owner artifacts remain
canonical.

## Legacy Absorption Coverage Index Disposition

| Coverage item | Evidence | Disposition |
| --- | --- | --- |
| retained Provider Intelligence corpus | PINT-T0 through PINT-T3 plus this new 50-file rescan | full current rescan must be registered through the corpus scan registry |
| legacy coverage index | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` | NOT_APPLICABLE_WITH_REASON: this successor rescan uses the current corpus registry and does not create a competing legacy owner |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: execute the existing corpus-registry
generator so the worker changes the generated aggregate through its source
entry. No checker or generator source edit is authorized.

Protected paths:

- `governance/compat/generate_corpus_scan_registry.py` is executable evidence
  only and must remain unchanged.

Operator authorization: the operator authorized full CVF-compliant corpus
scanning and absorption planning.

Rollback boundary: if the registry output is rejected, revert only the new
PINT-R1 registry source entry and its regenerated aggregate delta; do not
revert accepted PINT-T0 through PINT-T3 artifacts.

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| Durable owner | existing `docs/corpus-intelligence/registry/entries/` source layout |
| New stable folder | N/A with reason: no new foundation folder is created |
| Generated aggregate | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` |
| Generator | `governance/compat/generate_corpus_scan_registry.py` |
| Front door | existing corpus registry and PINT/EAIC owner surfaces |
| Maintainability boundary | audit and registry entry remain separate; no monolithic owner or runtime surface is opened |

## External Absorption Core

| Field | Value |
| --- | --- |
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | `.private_reference/legacy/CVF_PROVIDER_INTELLIGENCE` |
| Enumeration command | recursive `Get-ChildItem` with literal root and file filter |
| Manifest artifact or inline manifest | audit per-file table |
| Processing ledger artifact or inline ledger | audit per-file table |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | PINT-T2, PINT-T3, EAIC map, conditional reopen index, or explicit gap |
| Unresolved items | must be zero for full verdict or explicitly listed |
| Completion claim boundary | documentation-only bounded corpus value reconciliation |

## Corpus Completeness And Report Integrity

- Corpus task class: KNOWLEDGE_ABSORPTION.
- Corpus root: `.private_reference/legacy/CVF_PROVIDER_INTELLIGENCE`.
- Snapshot time: worker execution timestamp.
- Enumeration command: recursive filesystem enumeration including hidden and
  ignored files.
- Manifest artifact or inline manifest: audit per-file ledger.
- Manifest hash: worker-recomputed deterministic digest.
- Processing ledger artifact or inline ledger: audit per-file ledger.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED,
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=50; ledger_terminal=50; exclusions=0; unresolved=0.
- Unresolved files: 0 for `COMPLETE_VERIFIED`; otherwise list every path.
- Declared exclusions: none.
- Unreadable or unsupported files: none; bytecode is inventoried as generated
  binary with readable sibling evidence.
- Aggregation check: extension, folder, mapped, deferred, and unmapped totals
  sum to 50.
- Drift check: recompute after authoring.
- Output traceability: every row has semantic locator and disposition.
- Adversarial verification: worker samples highest-risk claims; reviewer
  independently recomputes and samples.
- Corpus verdict: PARTIAL

The worker may replace this with `COMPLETE_VERIFIED` only when the exact
reconciliation conditions are satisfied in the completed audit.

## Knowledge System Reconciliation

- Knowledge task class: CORPUS_ABSORPTION.
- Source manifest: audit per-file ledger.
- Source manifest hash: worker-recomputed deterministic digest.
- Enumeration safety: recursive filesystem truth, not bare ignore-sensitive
  listing.
- Intake registry or ledger: new PINT-R1 registry entry and audit.
- Authority assets: all 50 external source files as evidence only.
- Derived views: audit, registry entry, and generated aggregate.
- Semantic region ledger: audit per-file ledger.
- Region reconciliation: assets=50; mapped=0; deferred=50; unmapped=0 at
  dispatch, then worker recomputes the completed mapping.
- Orphan or unmapped assets: none for reconciled verdict.
- Cross-region links: receipt, provider-intelligence, EAIC, and checker/source
  relations in audit.
- Drift check: worker recomputation.
- Rebuildability check: audit and registry can be rebuilt from source root.
- Retrieval boundary: file-level knowledge map only; deeper implementation
  requires primary sources and fresh authorization.
- Adversarial verification: high-value questions and reviewer audit.
- Knowledge-map verdict: PARTIAL

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
| --- | --- | --- | --- | --- | --- |
| doctrine delta | source-backed provider/receipt boundary | DOCTRINE_ADAPTED | PINT or EAIC enrichment proposal | reviewer accepts or rejects | no runtime |
| reusable schema concept | conditional contract opportunity | PACKAGE_CANDIDATE | conditional reopen index | measurable future trigger | no activation |
| invocation-control concept | bounded future behavior candidate | RUNTIME_CANDIDATE | EAIC knowledge-gap owner | acquire missing primary source first | no build |
| concrete invariant | possible CVF-native guard | CHECKER_CANDIDATE | PINT-T3 owner | reopen only if genuinely novel and repeated | no checker |
| foreign code/dependency | direct import rejected | REJECT_DIRECT_IMPORT | audit | retain contrast only | no import |
| exact duplicate/generated artifact | no new semantic delta | NO_PACKAGE_OR_RUNTIME_VALUE | per-file ledger | close with reason | none |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| existing advisory doctrine | PINT-T2 | CONFIRMED_EXISTING | verify exact coverage | cite owner |
| detailed absorption docs and hidden receipts | PINT-T2 and EAIC map | ENRICH_EXISTING | extract bounded delta | propose owner enrichment |
| missing invocation/session receipt semantics | EAIC map | NEW_FINDING | preserve only if evidence is distinct | map or park |
| prototype package/checker | PINT-T3 | REJECT_DIRECT_IMPORT | evaluate CVF-native invariant separately | reject import |
| bytecode and exact duplicates | readable sibling owners | NO_NEW_VALUE | generated or redundant | close per file |

## Rescan Intelligence Hardening

- Original source artifact: retained Provider Intelligence corpus.
- Predecessor intake artifact: PINT-T0 roadmap.
- Delta ledger status: required in audit.
- Routing matrix status: required in audit.
- Semantic sampling status: required in worker return and reviewer audit.
- Rescan intelligence verdict: PARTIAL

### Original-Intake Delta Ledger

Use `UNCHANGED_FROM_INTAKE`, `CHANGED_DISPOSITION`, `NEW_FINDING`, and
`REMOVED_OR_REJECTED` across the audit's substantive groups.

### Follow-Up Routing Matrix

Use `DO_NOW`, `SEPARATE_RUNTIME_TRANCHE`, `STRATEGIC_OPERATOR_DECISION`,
`OUT_OF_SCOPE`, and `RESOLVED_BY_DESIGN`.

### Semantic Sampling / Adversarial Review

Rows must include `sampleId`, `source section`, `source claim`,
`disposition checked`, `adversarial challenge`, and `verdict`.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | retained source -> full manifest -> per-file content ledger -> overlap/value conversion -> current owner or conditional park -> reviewer closure |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; corpus, knowledge-map, rescan, absorption-core, value-conversion, overlap, ADIF, and worker-return gates |
| Owner surface | audit plus current PINT/EAIC owners |
| Disposition | ADAPT bounded doctrine; DEFER candidates; REJECT direct import |
| Claim boundary | no runtime/provider/public/production authority |

## Roadmap-To-Work-Order Trace Matrix

| Source requirement | Work-order instruction | Required evidence | Closure test | Status |
| --- | --- | --- | --- | --- |
| predecessor representative scan needs file-level validation | 50-row methodology | per-file ledger | 50 equals 50 | dispatch ready |
| PINT advisory boundary | overlap comparison | owner citations | no runtime overclaim | dispatch ready |
| PINT no-checker-now decision | Python/checker review | direct-import and invariant dispositions | no checker edit | dispatch ready |
| EAIC knowledge gaps remain visible | high-value questions | contribution/gap table | parked status retained | dispatch ready |
| operator emphasis on absorption docs | individual content requirement | 16 distinct rows and locators | no folder summary | dispatch ready |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| INTERNAL_AGENT | parent worker session using local read/search helpers | no commit or external action | worker trace and Git evidence | internal helpers inherit parent boundary | CONTRACT_ONLY |
| EXTERNAL_AGENT_CLI_MCP | future EAIC adapter owner | invocation explicitly forbidden | EAIC parked map | no adapter execution; fresh source-verified tranche required | DEFERRED_WITH_REASON |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Knowledge absorption`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defects: ADIF-0014

Additional closure-semantic query returned: ADIF-0019.

| Field | Value |
| --- | --- |
| Resolver commands | `python governance/compat/run_adif_defect_resolver.py --task-class "Knowledge absorption" --role worker --lifecycle-phase pre-implementation --surface-selector ".private_reference/legacy" --risk-ceiling HIGH --max-results 20 --json`; closure query for external absorption worker returns |
| Returned defect count | 2 across two queries |
| Disclosed defectIds | ADIF-0014; ADIF-0019 |
| Dispatch impact | complete file-level accounting plus reviewer semantic audit after gates |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_absorption_blindspot_control_presence.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_corpus_to_knowledge_map_reconciliation.py`; `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | required corpus, knowledge-map, rescan, absorption, trace, handoff, prompt, no-commit, and worker-return fields |
| gateRunPurpose | confirmation and evidence after source/checker read-ahead |
| claimBoundary | structural compliance support; not semantic proof |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher/reviewer -> no-commit worker -> independent closer |
| phase | documentation execution released; review, commit, continuity, runtime, and external action held |
| baseHeadFor(phase) | dispatchBaseHead=`23f4e1657`; executionBaseHead=operator-supplied committed dispatch head; closureBaseHead=reviewer-captured |
| changedSetScope(phase) | exactly four Allowed Outputs |
| traceScope(phase, actor) | each actor records only its own reads, edits, helpers, commands, and gates |
| commitOwner(phase) | reviewer/closer only |
| crossBatchIsolation | no source, runtime, checker, hook, session, handoff, roadmap, public-sync, or unrelated absorption changes |
| nextMoveSurfaces | reviewer updates continuity only after accepted material commit |

Before status evidence: worktree clean at dispatch authoring base
`23f4e1657`; worker must independently prove a clean worktree before edits.

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_PINT_R1_FULL_CORPUS_CONTENT_RESCAN_COMPLETION_2026-07-23.md` |
| reviewerOwnedClosurePaths | paired baseline, this work order, accepted worker outputs, reviewer-owned conventional completion artifact, and separate continuity sync |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| PINT-R1 audit | create 50-row content ledger and all required reconciliation/value blocks |
| registry source entry | create compact current discovery record |
| generated registry aggregate | regenerate from source fragments |
| worker return | create complete no-commit evidence packet |

## Worker Return Packet Shape Contract

workerReturnPath:
`docs/reviews/CVF_PINT_R1_FULL_CORPUS_CONTENT_RESCAN_WORKER_RETURN_2026-07-23.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Before authoring, generate or inspect the current checker-safe worker-return
skeleton and read checker sources as applied to both worker-owned Markdown
outputs.

## Verification Commands

```powershell
python governance/compat/generate_corpus_scan_registry.py
python governance/compat/check_corpus_scan_registry.py --enforce
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_governed_file_size.py --enforce
git diff --check
git diff --cached --name-status
git status --short --untracked-files=all
git rev-parse --short HEAD
```

Do not run pre-closure, commit steward closure mode, push, provider, API, or
external invocation commands.

## Acceptance Criteria

- exact clean start and executionBaseHead evidence;
- 50 manifest rows and 50 terminal processing rows;
- all 44 readable content files individually opened or parsed;
- 16 distinct absorption-doc rows with semantic locators;
- seven hidden JSON rows with field-level evidence;
- six Python rows with symbol or behavior evidence;
- six bytecode rows with generated-artifact and sibling-source evidence;
- arithmetic and digests independently reproducible;
- accepted value mapped to current CVF owners or conditionally parked;
- all critical EAIC gaps remain honestly stated;
- no actual-usage claim from estimated receipt fields;
- exactly four Allowed Outputs, nothing staged, HEAD unchanged;
- required worker gates pass.

## Review Gate

The independent reviewer must recompute inventory/digests, inspect all 16 absorption documents,
all seven hidden receipts, every adapted/deferred/rejected row, and a bounded
sample of no-new-value rows. Machine gates are necessary but not semantic
acceptance.

## Closure Checklist

- [x] source root and predecessor authority are explicit;
- [x] complete hidden-aware enumeration is required;
- [x] every file receives one row;
- [x] documentation value is separable from runtime sufficiency;
- [x] internal helper autonomy is preserved;
- [x] external invocation and runtime implementation remain forbidden;
- [x] worker no-commit and reviewer closure ownership are explicit.

## Fail Conditions

Return `BLOCKED_WITH_REASON` for corpus count/digest drift that cannot be
explained, unreadable non-bytecode source, owner contradiction, missing
registry schema authority, required change outside Allowed Outputs, or any
need for forbidden runtime/external action. Do not force a complete verdict.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when all four Allowed Outputs exist,
every other path is unchanged, all 50 files have terminal ledger rows, the
registry aggregate is regenerated from its source entry, the staged diff is
empty, HEAD is unchanged, and required worker gates pass. Otherwise return
`BLOCKED_WITH_REASON` with the exact path, evidence, or gate blocker.

## Operator Checkpoint

No further operator question is needed for this documentation rescan. Fresh
operator authorization is mandatory before runtime construction, MCP/CLI
invocation, provider/API/account use, process control, checker implementation,
package activation, public sync, or lifting the existing moratorium.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher/reviewer role |
| Provider or surface | local provenance workspace |
| Session or invocation | PINT-R1 dispatch authoring, 2026-07-23 |
| Working directory | repository root |
| Command or tool surface | local reads, filesystem enumeration, hashing, apply_patch, governance gates |
| Target paths | paired PINT-R1 baseline and work order |
| Allowed scope source | operator instruction to rescan every Provider Intelligence file and retain useful MCP-related knowledge |
| Before status evidence | clean worktree at HEAD `23f4e1657` |
| After status evidence | dispatch packet pending gate confirmation and material commit |
| Diff evidence | `git diff --name-status` and pre-dispatch gates |
| Approval boundary | documentation-only source intake and worker dispatch |
| Claim boundary | no runtime/provider/live/public/CLI/MCP invocation or implementation claim |
| Agent type | dispatcher and future independent reviewer |
| Invocation ID | `pint-r1-dispatch-2026-07-23` |
| Expected manifest | paired PINT-R1 baseline and work order |
| Actual changed set | paired PINT-R1 baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | local documentation corpus rescan |
| claimDisposition | CLAIM_REJECTED: no execution-control or runtime-enforcement behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: external sample receipts are evidence inputs only |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is claimed |
| invocationBoundary | no external agent invocation is authorized |
| interceptionBoundary | no wrapper, proxy, launch gate, process interception, or cancellation behavior |
| claimLanguage | knowledge enrichment and gap sharpening only |
| forbiddenExpansion | no runtime, provider, live, public, package, checker, or MCP/CLI behavior without fresh authorization |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance absorption work; no public-sync batch is authorized.

## Claim Boundary

This work order authorizes a complete local file-content rescan and bounded
knowledge reconciliation only. It does not authorize worker invocation through
CLI/MCP, provider or account use, runtime construction, process control,
checker implementation, package activation, public sync, or a claim that CVF
has enough evidence to build the MCP/CLI control runtime.
