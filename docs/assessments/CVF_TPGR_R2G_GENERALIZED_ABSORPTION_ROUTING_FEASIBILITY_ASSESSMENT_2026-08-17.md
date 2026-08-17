# CVF TPGR-R2G Generalized Absorption Routing Feasibility Assessment

Memory class: governed-planning-assessment

docType: baseline

Status: COMPLETE_PENDING_REVIEW

Batch ID: TPGR-R2G

Date: 2026-08-17

executionBaseHead: `c18f6907f1ccee5e9f459611de780dbfc126c561`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Responds to work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_TPGR_R2G_GENERALIZED_ABSORPTION_ROUTING_FEASIBILITY_ASSESSMENT_2026-08-17.md`

Paired baseline authority:
`docs/baselines/CVF_GC018_TPGR_R2G_GENERALIZED_ABSORPTION_ROUTING_FEASIBILITY_ASSESSMENT_2026-08-17.md`

## Purpose

Assess whether TPGR (Task-Proportional Governance Routing) can route CVF's
existing knowledge-lifecycle owners across six representative source
archetypes (A1-A6) with bounded net value, without duplicating Layer A
evidence, weakening any first-intake or always-on control, or promoting any
outside source to CVF authority. This is a non-implementation planning
assessment. It changes no standard, checker, registry, catalog, hook, or
source corpus.

## Source / Predecessor Evidence

| Source | Identity | Authority use |
| --- | --- | --- |
| paired baseline | `docs/baselines/CVF_GC018_TPGR_R2G_GENERALIZED_ABSORPTION_ROUTING_FEASIBILITY_ASSESSMENT_2026-08-17.md` | complete execution authority for this assessment |
| paired work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_TPGR_R2G_GENERALIZED_ABSORPTION_ROUTING_FEASIBILITY_ASSESSMENT_2026-08-17.md` | task manifest, archetype matrix, acceptance criteria |
| R2G reconciliation and rescope | `docs/reviews/CVF_TPGR_SECOND_UPGRADE_GENERALIZATION_CRITIQUE_RECONCILIATION_AND_R2_RESCOPE_2026-08-17.md` | Conditional Lifecycle Route Graph, Scoped Claim Vocabulary Candidate, R2 Deliverables And Exit, stop conditions |
| TPGR routing standard | `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | TPGR-T0 Legacy Full-Gate Interlock; shadow-only current state |
| absorption chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | Central Core, Enforcement Gap (no universal router yet) |
| A1 primary evidence | `docs/audits/CVF_EAIC_KR_R1_CVF_23_07_EXTERNAL_REPOSITORY_INTAKE_AUDIT_2026-07-23.md` | first-intake controls, 231-file dual-pack intake, `COMPLETE_VERIFIED` |
| A2 primary evidence | `docs/audits/CVF_RSPB_AI_T0_DUAL_CORPUS_INTAKE_AUDIT_2026-08-15.md` | 764-file mixed-origin dual-corpus intake, `STOP_COST_EXCEEDS_VALUE`, superseded framing per its own Supersession Notice |
| A3 primary evidence | `docs/reviews/CVF_RSPB_AI_T11_CAPABILITY_WORKSPACE_PROFILE_AND_BOOTSTRAP_POLICY_BUNDLE_VALIDATION_KERNEL_COMPLETION_2026-08-17.md` | accepted-cluster completion review; actual reviewer-cost telemetry |
| A4 primary evidence | `docs/audits/CVF_PPMCP_R1_PINNED_UPSTREAM_AND_LEGACY_DELTA_REINTAKE_2026-07-25.md` | 107-file pinned-upstream-plus-legacy delta re-intake |
| A5 primary evidence | `docs/reviews/CVF_TPGR_SECOND_UPGRADE_GENERALIZATION_EXTERNAL_CRITIQUE_2026-08-17.md` | one advisory-critique-shaped small named input, no corpus ceremony |
| A6 primary evidence | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` Rule 5; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | project-source registration rule; current `PROJECT_SOURCE` entries |

## Scope / Methodology

The worker captured `executionBaseHead` = `c18f6907f1ccee5e9f459611de780dbfc126c561`
and confirmed a clean worktree before any edit (`git status --short
--untracked-files=all` returned no output). The worker read in full: the
paired baseline, the paired work order, `CVF_SESSION_MEMORY.md`, the
bootstrap read model, `AGENT_HANDOFF_V59_2026-08-11.md`, the guard
orientation index, the literal-format gotchas reference, the R2G
reconciliation review, the TPGR routing standard, the external knowledge
absorption chain map, and all six archetype primary evidence documents named
above (A1, A2, A3, A4, A5 in full; A6 via the corpus registry standard's
Mandatory Agent Rules section and a direct JSON parse of the current
generated registry). The worker also read the applicable
`governance/compat/check_*.py` checker sources listed in the Checker Source
Read-Ahead Block before authoring either output file, per the work order's
Worker Output Checker Read-Ahead Mandate.

No new source corpus was scanned, cloned, or registered. No standard,
checker, registry, catalog, hook, or router was modified. All registry and
command counts below were independently recomputed against current HEAD
using the commands recorded in the Command Evidence section of the paired
worker return, not carried over from any prior document's stated numbers.

## Verified As-Is Layer A Owner Map

| Layer A activity | Current owner(s) | Machine-checked? |
| --- | --- | --- |
| source registration and scan-state inheritance | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` (GC-051); `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | yes, `check_corpus_scan_registry.py` |
| manifest / hash / structural enumeration | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | yes, `check_external_absorption_core.py` |
| terminal processing ledger | same core standard | yes, same checker |
| overlap / novelty classification | same core standard | yes, `check_external_absorption_overlap_discipline.py` |
| value-conversion lanes (ABSORB/ADAPT/DEFER/REJECT/BLOCK/NO_NEW_VALUE) | same core standard | yes, `check_external_absorption_value_conversion.py` |
| mixed-origin provenance and evidence reuse | `docs/reference/external_agent_review/CVF_MIXED_ORIGIN_DERIVED_SYNTHESIS_ABSORPTION_STANDARD.md` | yes, `check_mixed_origin_derived_synthesis_absorption.py` |
| seven-gate blind-spot discipline | `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md` | yes, `check_absorption_blindspot_control_presence.py` |
| corpus completeness / report integrity | `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md` | yes, `check_corpus_completeness_report_integrity.py` |
| corpus-to-knowledge-map reconciliation | `docs/reference/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_STANDARD_2026-06-01.md` | yes, `check_corpus_to_knowledge_map_reconciliation.py` |
| external intake input-type routing | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | yes, `check_external_knowledge_intake_routing.py` |
| routing/control-selection (Layer B) | `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` (TPGR-T0) | yes, `check_task_governance_route.py`, shadow-only |

This assessment introduces no new proposed owner for any row above. The
chain map's own Enforcement Gap section states the remaining gap
verbatim: CVF has machine checks for each stage listed, but "does not yet
have one universal trigger/router that machine-enforces every external
repo, review, corpus, or legacy intake through this full chain." TPGR is
the candidate router for that gap; it is not a candidate owner for any Layer
A row above.

## Conditional Lifecycle Interface Candidate

Per the R2G reconciliation's Generalized Architecture Boundary, the
candidate interface binds Layer A (knowledge intake semantics) to Layer B
(TPGR control routing) by reference only, using exactly five facts per
active lifecycle node:

1. current lifecycle node (one of G0/C0/C1/C2/K0/K1/O1/V1/P1/D1 from the
   Conditional Lifecycle Route Graph);
2. valid predecessor receipt references (existing manifest, ledger,
   triage, or cluster-semantic evidence already owned by the standards in
   the table above);
3. exact claim requested (one token from the Scoped Claim Vocabulary
   Candidate);
4. actual target owner/effect class (existing CVF owner path or
   `OWNER_SURFACE_NOT_FOUND`);
5. earliest invalidated node when evidence drifts (used only by D1 delta
   reconciliation).

This candidate interface does not restate any manifest, ledger, value
matrix, origin graph, owner map, or checker command inventory. It cites
those surfaces by reference. It is not implemented by this assessment; it
remains a design candidate pending R3+ authorization.

## A1-A6 Worksheets

### A1 - New upstream corpus (first intake, no inherited receipt)

| Field | Value |
| --- | --- |
| Input class | pinned external Git mirror plus a separate copied legacy folder (dual source, no prior registry row) |
| Entry node | G0 INPUT_IDENTIFIED -> C0 CORPUS_REGISTERED -> C1 STRUCTURALLY_ENUMERATED -> C2 PROCESSING_LEDGER_RECONCILED |
| Inherited evidence | none; this is the no-inheritance case by design |
| Semantic scope | 231 files (18 Conversation-Resilient Governance + 213 Interaction Projection), full manifest and two terminal file ledgers, `COMPLETE_VERIFIED` corpus verdict |
| Current controls | GC-051 registration, full hidden/no-ignore enumeration, per-file terminal ledger, blind-spot seven-gate block, source-mirror migration control, overlap/novelty classification, value-conversion matrix |
| Proposed TPGR route | classify `sourceScale: CORPUS`, `authorityImpact: USES_EXISTING_OWNER` (or `ENRICHES_EXISTING_OWNER` if doctrine is adapted); this sets at least `P2_BOUNDED` plus `CORPUS_ACCOUNTING` per the TPGR standard's Mandatory Escalation rules; TPGR adds a routing receipt only, it does not skip any first-intake control |
| Always-on controls | GC-051 registration; C1 structural enumeration; C2 ledger reconciliation; blind-spot Gates 1-3 |
| Conditional controls | Gates 4-7 (deeper semantic/adversarial sampling) apply once C1-C3 receipts are valid, consistent with the reconciliation's stage-scaled blind-spot binding |
| Exact licensed claim | `INPUT_IDENTIFIED`, `CORPUS_REGISTERED`, `STRUCTURALLY_ENUMERATED`, `PROCESSING_LEDGER_RECONCILED` only; not `CLUSTER_SEMANTICALLY_READ` or any full-corpus semantic-absorption token |
| Invalidation trigger | none observed in this closed audit; a live A1 case would invalidate C1/C2 on manifest hash drift or upstream commit change |
| Authority boundary | no direct import; two-source authority separation was strictly kept (upstream mirror never cited as proof of proposal claims and vice versa) |
| Layer A cost | unavoidable: full enumeration, hashing, and per-file terminal-status ledger for 231 files; this is the mandatory first-intake floor, not TPGR overhead |
| TPGR overhead | one classification manifest plus one routing receipt; no observed duplicate ceremony in this audit's shape |
| Projected savings | none claimed for A1; the work order explicitly states A1 is not required to show inheritance savings |
| Uncertainty | PROJECTED - no live A1 TPGR receipt exists yet; this worksheet is evidence-shape analysis, not a runtime measurement |
| Disposition | TPGR adds no duplicate intake ceremony for A1 and preserves every first-intake control observed in the source audit; PASS on the A1 acceptance bar defined in the work order |

### A2 - Mixed-origin local synthesis (provenance-backed, owner-agent co-designed)

| Field | Value |
| --- | --- |
| Input class | dual corpus: 559-file pinned upstream Git mirror plus 205-file local CVF-shaped proposal folder (764 files total) |
| Entry node | G0 -> C0 -> C1 -> C2, with the local 205-file pack additionally routable through the mixed-origin standard's `semanticReviewUnit: CAPABILITY_CLUSTER` discipline |
| Inherited evidence | the audit's own manifests/hashes (upstream `74ef4330d0...`; proposal `c51ed5055e...`) are available for reuse by any later cluster review of the same 764-file corpus without re-enumeration, per the Absorption Cost Rule |
| Semantic scope | all 764 files reached a terminal ledger row (`READ`/`ADAPTED`/`DEFERRED`/`REJECTED`/`NO_NEW_VALUE`); zero unresolved; `Corpus verdict: COMPLETE_VERIFIED` |
| Current controls | dual-manifest separation (upstream never used as proof of proposal claims), adversarial sample verification (four highest-risk safety-bypass files fully read, not sampled), Value/Cost Rubric, Conditional Reopen Index update |
| Proposed TPGR route | classify `sourceScale: CORPUS`, `novelty: OWNER_COMPOSITION`; TPGR routes to the existing K1/O1 nodes for retained candidates without restating the Value/Cost Rubric |
| Always-on controls | dual-manifest separation control; adversarial sampling of the highest-risk safety-bypass instruction chain (Finding 2); blind-spot Gate 1-3 |
| Conditional controls | full semantic re-read of `NO_NEW_VALUE`/`REJECTED` groups is not required once the terminal ledger and adversarial spot-check are valid |
| Exact licensed claim | `STRUCTURALLY_ENUMERATED` and `PROCESSING_LEDGER_RECONCILED` for all 764 files; `CLUSTER_SEMANTICALLY_READ` only for the explicitly named adversarial-sample cluster; the audit's own note that this record is `SUPERSEDED_IN_DECISION_BY_MODS_T0_CORRECTION` for its value/cost framing must be preserved, not silently dropped |
| Invalidation trigger | none in this closed record; a live route would invalidate C1/C2 on either mirror's commit drift |
| Authority boundary | proposal folder retains `.private_reference/legacy/` classification; zero `ADAPTED` rows promote proposal material to CVF source in this audit |
| Layer A cost | unavoidable: 764-file enumeration/hashing/ledger, plus full reads of the four highest-risk safety-bypass files and two self-declaring foundation files - this is required semantic-intake work, not TPGR waste, per Measurement Protocol step 8 |
| TPGR overhead | one classification manifest; TPGR would add no second full-corpus pass |
| Projected savings | a later cluster review of the same 764-file corpus could route directly to K1 using the existing manifest/ledger receipts instead of re-enumerating; savings are bounded to the enumeration/ledger step, not semantic reading |
| Uncertainty | OBSERVED for the audit's own measured evidence; PROJECTED for any future TPGR-routed reuse of this corpus, since no such reuse has yet occurred |
| Disposition | claim-specific evidence and local-first semantic review are preserved; A2 acceptance bar met |

### A3 - Accepted-corpus cluster regression (fresh reusable-corpus evidence)

| Field | Value |
| --- | --- |
| Input class | a named seven-file-scale cluster composed from an already-accepted corpus (T7/T11 pure Guard Contract kernel), reviewed under an existing work order/worker-return/completion-review cycle |
| Entry node | K1 CLUSTER_SEMANTICALLY_READ (inherits C0-C2 from the corpus's existing accepted receipts; does not re-run GC-051 registration or full enumeration) |
| Inherited evidence | T7 owner projection and prior accepted contract surface; no re-enumeration of the underlying corpus was performed for T11 |
| Semantic scope | one bundle validator module plus its focused test file, contracts barrel export, root barrel export, and one system-chain map hash-only refresh |
| Current controls | reviewer independent diff audit before first edit; hermetic proof only (no filesystem/environment/network/provider action); Review-Cost Telemetry block; Machine Closure Package |
| Proposed TPGR route | classify `sourceScale: NAMED_FILES` or `BOUNDED_CLUSTER`, `delegation: MULTI_ROLE_NO_COMMIT`; this is the archetype where TPGR routing should show the clearest bounded savings because C0-C2 evidence is already valid and unexpired |
| Always-on controls | independent reviewer diff audit; hermetic-proof boundary; review-cost stop disposition |
| Conditional controls | full corpus re-enumeration is explicitly not required; this is the intended reuse case |
| Exact licensed claim | `CLUSTER_SEMANTICALLY_READ` for the named T11 file set only; not any corpus-level absorption claim |
| Invalidation trigger | none observed; a live invalidation would fire on T7 owner-surface change or contract hash drift |
| Authority boundary | no new authority created; posture and verdict (`PARTIAL`, `PARTIAL_RUNTIME_CONNECTION_FULL_INVENTORY`) remained unchanged after the repair |
| Layer A cost | one bounded reviewer repair round (dense-array collection-limit ordering defect), 26/26 focused plus 52/52 composed regression, TypeScript, reviewer-fast 64/64, pre-commit 85/85 |
| TPGR overhead | the review record shows no observable irrelevant-guard ceremony beyond the standard hermetic proof and gate set; this is evidence the accepted-cluster route does not need a heavier TPGR wrapper on top of the existing work-order/worker-return/completion-review cycle |
| Projected savings | this is the archetype the prior (superseded) single-cell R2 measured; the reconciliation is correct that this alone cannot generalize, but within its own cell it does show the RSPB-pattern reuse removes repeated corpus-level ceremony without weakening semantic review, since only the named cluster - not the full corpus - was re-read |
| Uncertainty | OBSERVED for review-cost telemetry (`reviewRoundCount: 1`, `latencyDisposition: WITHIN_FAST_PATH_TARGET`); PROJECTED for any TPGR-specific overhead delta, since no TPGR receipt was actually attached to this review |
| Disposition | the RSPB-pattern seven-file-scale case removes repeated corpus-level work without weakening semantic review; A3 acceptance bar met, bounded to this one cell as the reconciliation requires |

### A4 - Upstream delta (pinned predecessor, changed source identity)

| Field | Value |
| --- | --- |
| Input class | 107-file bounded re-intake: 98-file pinned-upstream Git mirror (`pancake-pos-mcp`) plus 9 retained legacy interpretation files, compared against a prior `PARTIALLY_ABSORBED` disposition trail |
| Entry node | D1 DELTA_RECONCILED, routed back only to the earliest affected node (the 9-file legacy folder's disposition, not the entire historical LHW16-T2 closure) |
| Inherited evidence | prior LHW16-T2 closure narrative was checked, not assumed; the audit explicitly re-verified rather than trusted the prior narrow "doc-only" disposition |
| Semantic scope | all 107 files read in full (no sampling); aggregate manifest digest independently recomputed and matched exactly (`7deb1ef3b1...`) |
| Current controls | full field-by-field re-comparison against two current CVF owner surfaces (`mcp.business.adapter.contract.ts`, `tool-action-taxonomy.ts`); delta ledger explicitly separates `UNCHANGED_FROM_INTAKE`, `CHANGED_DISPOSITION`, `NEW_FINDING`, and `REMOVED_OR_REJECTED` |
| Proposed TPGR route | classify `sourceScale: BOUNDED_CLUSTER`, escalate on any `authorityImpact` change; TPGR's D1 node licenses only `DELTA_RECONCILED`, explicitly preserving unaffected historical evidence rather than invalidating the full 107-file history |
| Always-on controls | full delta re-comparison against the actual current owner surface (not the owner surface as it stood at the prior closure); adversarial sampling of the highest-risk claims (four samples in the Semantic Sampling table) |
| Conditional controls | none of the prior evidence was blindly inherited; every claim was independently re-checked, which the reconciliation requires for D1 |
| Exact licensed claim | `DELTA_RECONCILED`; the audit explicitly narrows rather than widens the prior claim ("confirmed accurate at the legacy-folder level but was incomplete at the upstream-repository level") |
| Invalidation trigger | upstream commit change (already exercised: this audit itself was triggered by re-intake need); two new legacy deltas and four new upstream findings surfaced that the prior closure had not captured |
| Authority boundary | direct import remains rejected for all 24 tool implementations and every transport entry point; only doctrine/pattern-level value is retained |
| Layer A cost | unavoidable: full 107-file re-read plus field-by-field comparison against live current source (not documentation) - this is the D1 stage's required minimum, since a terminal ledger row alone is explicitly not full-read proof per the TPGR standard |
| TPGR overhead | none beyond one delta-reconciliation classification; the audit shows the earliest-affected-node principle already applied without any TPGR receipt |
| Projected savings | bounded: D1 avoided re-litigating the 6-of-9 legacy files that were `CONFIRMED_EXISTING`, while still requiring full reads for the 2 files with real narrow deltas and the entire 98-file upstream mirror since it had never been compared before; savings apply only to already-settled sub-claims, not to the delta itself |
| Uncertainty | OBSERVED for the completed audit; PROJECTED for how a TPGR receipt would formally express "earliest affected node," since D1 is not yet implemented as a machine node |
| Disposition | the earliest-affected-node principle is achievable without invalidating unrelated history; A4 acceptance bar met |

### A5 - Small named item/file set (not necessarily a reusable corpus)

| Field | Value |
| --- | --- |
| Input class | one operator-provided external critique document (a single named review file, not a corpus) |
| Entry node | G0 INPUT_IDENTIFIED -> K1 CLUSTER_SEMANTICALLY_READ -> O1 OWNER_MAPPED, explicitly bypassing C0-C2 corpus registration per the Conditional Lifecycle Route Graph's stated exception for non-reusable small named inputs |
| Inherited evidence | none required; this document was read directly and dispositioned without GC-051 registration |
| Semantic scope | one review-shaped artifact; "Scope / Methodology" states it was read once for source verification and comparison purposes, with governed sources verified around it |
| Current controls | External Knowledge Intake Routing table with canonical `Input type` token (`operator-provided external comparison, critique, or recommendation`); explicit `Rescan Intelligence Hardening: NOT_APPLICABLE_WITH_REASON`; explicit `Corpus Completeness And Report Integrity: NOT_APPLICABLE_WITH_REASON` |
| Proposed TPGR route | classify `sourceScale: NAMED_FILES`, `authorityImpact: NONE` (advisory-only until CVF reconciliation); this is the cheapest legitimate route in the routing matrix and the archetype most exposed to over-ceremony risk if forced through GC-051 |
| Always-on controls | source verification of every named CVF standard the critique references; explicit claim boundary stating the critique is advisory, not authority, until independently reconciled |
| Conditional controls | no manifest, no per-file terminal ledger, no blind-spot seven-gate block - all correctly marked `N/A` rather than force-applied |
| Exact licensed claim | `INPUT_IDENTIFIED` plus `CLUSTER_SEMANTICALLY_READ` for this one named document; explicitly `ADVISORY_INPUT_PENDING_RECONCILIATION`, never CVF authority by itself |
| Invalidation trigger | none; a small named item's invalidation trigger would be a re-issued or corrected version of the same document |
| Authority boundary | the critique's own Claim Boundary states it "must not be cited as canonical authority in Source Authority tables, Source Verification ACCEPT rows, corpus manifests, closure proof, or roadmap/work-order evidence" |
| Layer A cost | minimal: one document read, source-verified against eight named canonical standards, normalized, and preserved; no corpus-scale ceremony was invoked |
| TPGR overhead | effectively zero beyond the existing External Knowledge Intake Routing table already required by the chain map |
| Projected savings | this archetype demonstrates the ceremony floor already works without TPGR: a small named input already skips GC-051, manifest, and ledger machinery under current rules. TPGR's marginal contribution here is a routing receipt confirming that skip was correct, not a new capability |
| Uncertainty | OBSERVED - this exact document exists and was processed exactly this way under current rules, with no TPGR receipt attached |
| Disposition | the minimum route is materially cheaper than corpus intake while remaining source-bound; A5 acceptance bar met |

### A6 - Downstream project source boundary (existing PROJECT_SOURCE evidence)

| Field | Value |
| --- | --- |
| Input class | project-owned source trees registered as `PROJECT_SOURCE` corpus-type entries in the current generated registry |
| Entry node | C0 CORPUS_REGISTERED under GC-051 Rule 5 ("This standard applies equally to CVF workspace project corpora... Add a `PROJECT_SOURCE` entry to the registry before scanning") |
| Inherited evidence | each existing `PROJECT_SOURCE` entry carries its own `scopePaths`; project findings are cross-referenced against CVF framework findings per Rule 5 item 3, not merged into CVF authority |
| Semantic scope | 37 `PROJECT_SOURCE` entries independently recomputed by direct JSON parse of `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` at current HEAD (see Recomputed Registry Counts below) |
| Current controls | GC-051 Rule 5 registration-before-scan; same schema as any other corpus type; explicit cross-reference requirement rather than authority merge |
| Proposed TPGR route | classify `dataSensitivity: PRIVATE_REPO` (or as declared per project), `authorityImpact: NONE` for pure project-source reads; a route that treats project material as promoting CVF authority must escalate, not fast-route |
| Always-on controls | GC-051 registration remains mandatory for project corpora exactly as for any other corpus type; no separate lighter-weight rule exists or is proposed |
| Conditional controls | none beyond the registration-before-scan rule; Rule 5 does not itself require the full seven-gate blind-spot block for every project read, but does not exempt CVF's own findings from being cross-referenced |
| Exact licensed claim | `CORPUS_REGISTERED` for the project scope path; explicitly not a CVF-authority promotion claim |
| Invalidation trigger | project source-tree change under an already-registered `scopePaths` entry; the registry does not currently express automatic drift detection for project sources as a distinct rule from other corpus types |
| Authority boundary | GC-051 Rule 5 itself is the boundary control: project registration is required, but registration is not authority promotion; this assessment does not add or remove that boundary |
| Layer A cost | one registry entry per project scope; unavoidable minimum already in force |
| TPGR overhead | none identified beyond the same routing receipt every other corpus-type entry would receive |
| Projected savings | none material identified; A6's question is a boundary-preservation question, not a cost-savings question, and the work order frames it that way |
| Uncertainty | OBSERVED for the recomputed 37-entry count; PROJECTED for how a TPGR receipt would mark the authority-boundary distinction machine-readably, since no such field exists in the current registry schema |
| Disposition | project knowledge can be used via existing GC-051 Rule 5 registration without promoting the project to CVF authority or claiming full project-governance activation; A6 acceptance bar met; no schema change is proposed by this assessment |

## Evidence / Verification

Before dispatch, both worker outputs were required to pass routing and
dispatch gates; the pre-implementation autorun gate (80/80 checks, PASS,
10.026s) and the TPGR shadow-route checker (`COMPLIANT`, 0 violations) were
both run once at `executionBaseHead` as required preflight, before any
edit. During execution, this assessment records source sections, command
counts, exact status/diff, and the no-commit boundary directly in its own
tables above (Source / Predecessor Evidence, Recomputed Registry Counts,
Canonical Autorun Command-Universe Count, Current Full-Gate Sample) and in
the paired worker return's Command Evidence section. Reviewer acceptance of
this evidence remains a separate, independent step owned by the
reviewer/closer.

## Recomputed Registry Counts

Independently recomputed by direct JSON parse of
`docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` at
executionBaseHead `c18f6907f1ccee5e9f459611de780dbfc126c561` (command and
exit code recorded in the paired worker return):

- total registry entries: 170
- `corpusType` distribution: `CVF_EXTENSION` 87, `PROJECT_SOURCE` 37,
  `POLICY_DOCUMENT` 18, `LEGACY_FOLDER` 17, `EXTERNAL_SOURCE` 5,
  `TEST_CORPUS` 6 (sums to 170; a seventh allowed type, `COMPANY_DOCS`,
  currently has zero entries, matching the R2G reconciliation's
  `ACCEPT_WITH_PRECISION` finding on the same claim)
- `status` distribution: `SCANNED` 129, `SCANNED_WITH_FINDINGS` 33,
  `PARTIALLY_SCANNED` 5, `DEEP_CLASSIFIED` 2, `NOT_STARTED` 1

These counts match the 170-entry figure independently verified by the R2G
reconciliation review and are recomputed fresh here rather than carried
forward, per the Measurement Protocol.

## Canonical Autorun Command-Universe Count

Independently recomputed at `executionBaseHead` by direct import of
`governance/compat/agent_autorun_command_catalog.py`:

- `check_*.py` files present under `governance/compat/`: 193 (recomputed by
  filesystem glob)
- pre-implementation autorun command universe: 80 total (78 common commands
  shared across phases plus 2 pre-implementation-only commands)
- pre-push-only additional commands: 2
- the actually-executed pre-implementation gate at this executionBaseHead
  ran exactly 80 checks, all `PASS`, in `10.026` measured seconds (receipt:
  `.cvf/runtime/autorun-receipts/pre-implementation.json`,
  `totalDurationSeconds: 10.026`)

The 193-file count and the 80-command executed count are different
measurements by design: 193 counts every checker script that exists on
disk; 80 counts only the commands the pre-implementation phase catalog
actually wires into its run. This is the `catalog-unwired` distinction the
R2G reconciliation and the external critique both required to be kept
exact rather than collapsed into a single "orphan checker" claim. This
worksheet does not attempt to enumerate the exact non-implementation
disposition of every one of the 113 catalog-unwired checkers; that is a
separate, larger classification task outside this assessment's bounded
scope.

## Current Full-Gate Sample

The pre-implementation gate was run once as required Pre-Flight Check
preflight for this dispatch (not repeated), producing the sample above:
80 checks, all `PASS`, `10.026` measured seconds at
executionBaseHead=headSha=`c18f6907f`. This is recorded as one current
full-gate sample for this repository state, not as a universal benchmark,
per Measurement Protocol step 5. No other repository, corpus size, or
future state can be assumed to reproduce this exact timing.

## Claim-Vocabulary Compatibility And Migration-Cost Assessment

| Scoped Claim Vocabulary Candidate token (R2G reconciliation) | Compatible existing vocabulary observed in A1-A6 evidence | Compatibility | Migration cost if adopted |
| --- | --- | --- | --- |
| `INPUT_IDENTIFIED` | "Target / Source" identification present in every archetype document (A1-A6) | COMPATIBLE | none; already the de facto first step everywhere |
| `CORPUS_REGISTERED` | GC-051 registry entries (A1, A2, A4, A6) | COMPATIBLE | none; GC-051 already performs this exact function |
| `STRUCTURALLY_ENUMERATED` | "manifest" / "ledger terminal statuses" language already present in A1, A2, A4 | COMPATIBLE | low; would formalize existing "Corpus verdict: COMPLETE_VERIFIED" language into one reserved token |
| `PROCESSING_LEDGER_RECONCILED` | terminal ledger rows already distinguished from semantic reading in A1, A2 ("READ" does not mean fully understood) | COMPATIBLE | low; the distinction already exists in prose, not yet as an enforced token |
| `TRIAGE_CLASSIFIED` | Overlap And Novelty Classification tables in A1, A2, A4 | COMPATIBLE | low |
| `CLUSTER_SEMANTICALLY_READ` | explicit "fully read, not sampled" language in A2's adversarial verification and A4's full 107-file read | COMPATIBLE | low; would need a machine-checked scope-list requirement, which the mixed-origin standard's `semanticReviewUnit` field partially already provides |
| `CAPABILITY_ADAPTED_INTO_CVF` (R2G) / `CAPABILITY_ABSORBED` (external critique) | the two reconciled documents use different token names for the same concept; R2G's reconciliation supersedes the critique's naming | NAME_CONFLICT_RESOLVED_BY_RECONCILIATION | none additional; R2G's naming already won this exact conflict, so no further migration decision is required by this assessment |
| `CORPUS_SEMANTICALLY_RECONCILED` | not observed as achieved in any of A1-A6; A2's own corpus explicitly records `gc050: NOT_RUN`, confirming this token is intentionally rare | COMPATIBLE_BUT_UNCLAIMED | none; correctly absent everywhere it would be an overclaim |
| `DELTA_RECONCILED` | A4's "Delta ledger status: COMPLETE" language is a direct prose analog | COMPATIBLE | low |

No token in the Scoped Claim Vocabulary Candidate table conflicts with any
vocabulary actually observed in the six archetype documents. The one naming
overlap (`CAPABILITY_ADAPTED_INTO_CVF` versus `CAPABILITY_ABSORBED`) was
already resolved by the R2G reconciliation choosing the CVF-corrected name;
this assessment does not reopen that naming decision. Adoption would be a
low-cost prose-to-token formalization exercise for six of nine tokens and a
zero-cost confirmation for the remaining three; no standard, checker, or
registry field is changed by this assessment.

## Cost Model - Layer A Versus TPGR Overhead

| Cost category | A1 | A2 | A3 | A4 | A5 | A6 |
| --- | --- | --- | --- | --- | --- | --- |
| Unavoidable Layer A evidence cost | full 231-file enumeration/hash/ledger | full 764-file enumeration/hash/ledger plus adversarial full-reads | none (inherits accepted corpus receipts) | full 107-file re-read and field-by-field comparison | one document read and source-verification | one registry entry per project scope |
| Current legacy guard command count / wall time | not separately timed in the source audit; bundled into the audit's own gate runs | same | 26/26 focused + 52/52 composed + package (789 tests) + reviewer-fast 64/64 + pre-commit 85/85, `WITHIN_FAST_PATH_TARGET` | not separately timed | 7 checkers named in its own Checker Source Read-Ahead Block | GC-051 checker only |
| Proposed TPGR classification/metadata overhead | one manifest field set plus one routing receipt | same | same | same | same (already minimal) | same |
| Inherited vs refreshed evidence | 0% inherited (by design, A1 is the no-inheritance case) | manifest/ledger inheritable for future clusters; adversarial-sample evidence not re-inherited without re-verification | ~100% inherited (T7 owner projection); only the new T11 file set was fresh | delta-specific: 6/9 legacy files inherited unchanged disposition; 98/98 upstream files freshly compared (0% inherited, never compared before) | 0% inherited; not a reusable-corpus case | scope-path inheritance across repeated project reads under the same registered entry |
| Controls always retained | GC-051, manifest, ledger, blind-spot Gates 1-3 | same, plus dual-manifest separation | independent reviewer diff audit, hermetic-proof boundary | full re-comparison against live current owner surface, not stale documentation | source verification of every cited standard | GC-051 registration-before-scan |
| Controls conditionally omitted | Gates 4-7 until C1-C3 valid | full semantic re-read of settled `NO_NEW_VALUE` groups | full corpus re-enumeration | none omitted (D1 requires full delta re-verification) | manifest, ledger, blind-spot block (all correctly N/A) | full seven-gate block (Rule 5 does not mandate it uniformly) |
| Recurring maintenance cost per relevant owner/catalog change | low; GC-051 schema changes propagate automatically via the generator | same | low; T7/T11 composition already regression-tested | low; delta re-intake is already the designed recurring case | near-zero | low; registry entry maintenance only |
| Net cost attributable to TPGR, separated from necessary semantic-intake work | effectively a routing-receipt marginal cost only; the dominant cost is the unavoidable 231-file first-intake floor | same; dominant cost is the 764-file floor plus adversarial sampling | TPGR's clearest positive case: near-zero marginal TPGR cost against an already-cheap accepted-cluster review | marginal TPGR cost only; dominant cost is the mandatory full delta re-verification, which TPGR must not skip | near-zero; A5 already has the cheapest legal route without TPGR | near-zero; TPGR adds no capability beyond the existing Rule 5 registration step |

Across all six archetypes, no evidence was found of TPGR overhead exceeding
or duplicating unavoidable Layer A cost. The clearest positive TPGR case is
A3 (accepted-cluster reuse); the clearest neutral cases are A1, A2, A4
(first-intake and delta cases where TPGR cannot and must not reduce
required semantic work); A5 and A6 show the existing ceremony floor is
already appropriately minimal without TPGR.

## Observed / Projected / Unknown Evidence Summary

| Evidence class | Label | Basis |
| --- | --- | --- |
| Registry entry count (170) and type/status distribution | OBSERVED | direct JSON parse at executionBaseHead, recorded in Command Evidence |
| Checker-shaped file count (193) | OBSERVED | filesystem glob at executionBaseHead |
| Autorun command-universe count (80 pre-implementation; 2 pre-push-only) | OBSERVED | direct Python import and count of the catalog module at executionBaseHead |
| Pre-implementation gate sample (80 checks, PASS, 10.026s) | OBSERVED | actual receipt file generated by the required preflight run |
| A1-A6 archetype evidence (file counts, verdicts, dispositions) | OBSERVED | direct full reads of the six primary archetype documents |
| TPGR marginal overhead in a live routed task | PROJECTED | no TPGR receipt has yet been attached to any of A1-A6; this assessment reasons from the TPGR standard's declared shadow-only mechanics, not from a measured routed run |
| Claim-vocabulary migration cost | PROJECTED | reasoned from prose-to-token gap analysis, not from an implemented migration |
| Whether a live TPGR router would reproduce this assessment's classification decisions automatically | UNKNOWN | TPGR-T2/T4 selective-execution equivalence evidence does not yet exist per the TPGR standard's own Rollback and Verification sections |
| Recurring maintenance cost of the conditional lifecycle interface candidate over time | UNKNOWN | the interface is a design candidate only; no maintenance history exists |

## Checker/Catalog Applicability Feasibility

The canonical autorun command universe (80 pre-implementation commands, 2
additional pre-push-only commands, 193 total checker files on disk) is the
only command inventory this assessment cites. No new command list,
duplicate catalog, or shadow inventory is proposed. A deterministic
classification distinguishing "corpus route" from "item route" is feasible
in principle using the existing `sourceScale` enum (`NONE`, `NAMED_FILES`,
`BOUNDED_CLUSTER`, `CORPUS`) already defined in the TPGR standard's
Mandatory Classification table; this assessment did not observe any A1-A6
case where that four-value enum failed to classify the archetype
correctly. Selective command closure - actually skipping catalog commands
for a routed task - remains explicitly unauthorized during T0 shadow
enforcement and is not evaluated here as a present capability; the TPGR
standard's own TPGR-T0 Legacy Full-Gate Interlock section states this
directly (`selectiveExecutionAuthorized: false`,
`legacyGateDisposition: RUN_FULL_LEGACY_BUNDLE`).

## Proposed Authority-Delta Manifest (Zero Current Edits)

The following paths are named as exact candidate edit targets for a future
R3+ tranche only. None is edited, drafted, or scaffolded by this
assessment. Each row states the smallest change the evidence above
supports; larger changes are explicitly out of scope.

| Candidate path | Candidate change | Justifying evidence | Authorization state |
| --- | --- | --- | --- |
| `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | add one "Layer A Interface" section naming the five-fact conditional lifecycle interface candidate by reference | Conditional Lifecycle Interface Candidate section above; R2G reconciliation's Generalized Architecture Boundary | UNAUTHORIZED; requires R3+ and independent review |
| `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` (GC-051 `corpusType` enum) | evaluate (not adopt) two additional enum values for derived-synthesis and named-file-set corpora | external critique's Authority Placement table; this assessment's A2/A5 worksheets found no case where the existing enum values were insufficient to classify the observed archetypes | UNAUTHORIZED; R2G reconciliation already marked this `DEFER` pending a test of whether existing types plus metadata suffice; this assessment's evidence is consistent with continuing that deferral |
| `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` (Scoped Claim Vocabulary) | adopt the nine-token Scoped Claim Vocabulary Candidate as enforced tokens | Claim-Vocabulary Compatibility And Migration-Cost Assessment section above | UNAUTHORIZED; low-cost per this assessment's compatibility analysis, but still requires R3+ authorization and a machine-checker change |
| any `governance/compat/check_*.py` file | none proposed by this assessment | no A1-A6 evidence showed a checker gap requiring a new or modified checker | NOT_PROPOSED |

No path above is edited by this worker. This table exists to satisfy the
work order's requirement for "exact proposed authority-delta paths with
zero current edits," not to pre-approve any future change.

## Stop-Condition Evaluation

The R2G reconciliation's Generalized R2 Feasibility Assessment section
defines six stop/narrow conditions. Each is evaluated against the A1-A6
evidence above:

| Stop condition | Evaluation | Result |
| --- | --- | --- |
| the interface duplicates Layer A evidence rather than referencing it | the Conditional Lifecycle Interface Candidate cites existing owners by reference only (five facts, no restated manifest/ledger/matrix); no duplication observed | NOT TRIGGERED |
| deterministic classification cannot distinguish corpus and item routes | the existing `sourceScale` enum correctly classified all six archetypes in this assessment without ambiguity | NOT TRIGGERED |
| metadata maintenance plus escalation cost exceeds removed irrelevant-guard cost for an activation candidate | no archetype showed TPGR overhead exceeding Layer A cost; A1/A2/A4 show TPGR cannot reduce mandatory first-intake or delta-verification cost, and correctly does not attempt to | NOT TRIGGERED |
| a repeated/reuse route produces no bounded savings after maintenance | A3 shows a positive bounded case (near-zero marginal TPGR cost against an already-cheap accepted-cluster review); this is the one required positive case per R2 Deliverables And Exit item 7 | NOT TRIGGERED |
| any material false negative, authority contamination, or completion-claim laundering appears | A2's proposal folder retains zero `ADAPTED` rows and its `.private_reference/legacy/` classification; A6's Rule 5 explicitly separates registration from authority promotion; no laundering observed | NOT TRIGGERED |
| selective command closure cannot be maintained from one canonical catalog | selective closure is not evaluated as a present capability (T0 remains shadow-only); this assessment cites only the one canonical 80-command pre-implementation catalog and proposes no second catalog | NOT TRIGGERED |

No stop condition is triggered by the evidence gathered in this assessment.

## Findings / Position

The as-is Layer A owner map is complete and machine-checked across every
lifecycle activity named in the R2G reconciliation's Generalized
Architecture Boundary. No archetype required a new Layer A owner. The
one recorded gap - "no universal trigger/router... machine-enforces every
external repo, review, corpus, or legacy intake through this full chain" -
is exactly the gap TPGR is positioned to fill as a router, not an owner.

Across A1-A6, TPGR's candidate marginal cost never exceeded or duplicated
mandatory Layer A evidence cost. A3 supplies the one required positive
bounded case for a repeated/reuse route (near-zero marginal TPGR cost on
top of an already lightweight accepted-cluster review, with review-cost
telemetry showing `WITHIN_FAST_PATH_TARGET` and zero avoidable delay). A1,
A2, and A4 correctly show TPGR cannot and does not attempt to reduce
unavoidable first-intake or delta-reconciliation cost - which is the
correct outcome, not a finding against TPGR, per the R2G reconciliation's
explicit instruction that A1 is not required to show inheritance savings.
A5 and A6 show the existing ceremony floor for small named inputs and
project-source use is already appropriately minimal without TPGR; TPGR's
marginal contribution in those two archetypes is a routing receipt
confirming the existing minimal route was correct, which is real but
modest value.

The claim-vocabulary compatibility analysis found no conflicts between the
R2G reconciliation's nine-token Scoped Claim Vocabulary Candidate and any
vocabulary actually observed across the six archetypes; the one naming
disagreement between the R2G reconciliation and the external critique
(`CAPABILITY_ADAPTED_INTO_CVF` versus `CAPABILITY_ABSORBED`) was already
resolved by the reconciliation and is not reopened here.

None of the six R2G stop conditions is triggered by this evidence.

## Risk / Corrective Action

Primary risk: a future R3+ tranche could still recreate a duplicate
absorption mega-standard inside the TPGR owner if the "Layer A Interface"
section grows beyond the five-fact reference contract this assessment
evaluated. Corrective action: any R3+ implementation of the interface
candidate must be reviewed against exactly the five-fact scope defined in
the R2G reconciliation and in this assessment's Conditional Lifecycle
Interface Candidate section; a design that adds a sixth fact, restates a
manifest/ledger field, or introduces a second registry should be treated as
a stop-condition trigger even if this assessment did not observe one.

Secondary risk: the 113 catalog-unwired checkers (193 total minus 80 wired
into the pre-implementation phase) were not individually classified by this
bounded assessment. A future R3+ or catalog-maintenance tranche should not
assume every catalog-unwired checker is either dead code or a phase-gap;
that determination is out of this assessment's scope and must not be
inferred from the counts recorded here.

Tertiary risk: this assessment's A2 and A3 worksheets both cite prior
audits whose own status lines record supersession or pending-closer state
(`SUPERSEDED_IN_DECISION_BY_MODS_T0_CORRECTION` for A2;
`REVIEWER_ACCEPTED_PENDING_CLOSER` for A3). This assessment treats both as
valid evidence sources for their own recorded facts (file counts, ledger
statuses, review-cost telemetry) while explicitly not treating either
document's own top-level value/cost or closure verdict as re-litigated or
overridden by this assessment. A future reader must not cite this
assessment as having closed or superseded either underlying record.

## Decision

`PROCEED_TO_THRESHOLD_DESIGN`

## Final Disposition

`PROCEED_TO_THRESHOLD_DESIGN`

Rationale: across all six required archetypes, TPGR's candidate marginal
cost never exceeded or duplicated unavoidable Layer A evidence cost, one
archetype (A3) supplied the required positive bounded case for a
repeated/reuse route without weakening semantic review, no archetype showed
authority contamination or completion-claim laundering, the claim
vocabulary is compatible with observed evidence at low migration cost, and
none of the six R2G stop conditions was triggered. The router remains
smaller than the lifecycle it routes (a five-fact reference interface, not
a restated manifest/ledger/matrix), and it creates no second truth store.
This satisfies the R2G Deliverables And Exit passing bar. The next
authorized step is R3 (pre-register per-archetype proof, cost, divergence,
and rollback floors), which remains unauthorized by this assessment and
requires a fresh operator decision and governed dispatch.

## Claim Boundary

This assessment is a documentation-only, non-implementation feasibility
evaluation over existing governed evidence. It does not implement TPGR
routing, does not modify any standard, checker, registry, catalog, hook, or
router, does not intake or register any new source corpus, does not
authorize selective execution (`selectiveExecutionAuthorized` remains
`false` per the TPGR standard), and does not open R3-R9, T15, or any
runtime, provider/live, public-sync, deployment, or production action. The
`PROCEED_TO_THRESHOLD_DESIGN` disposition authorizes only a future operator
decision to open R3 under a fresh governed dispatch; it does not itself
authorize R3 work.
