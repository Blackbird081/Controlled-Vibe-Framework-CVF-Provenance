# CVF GC-018 AECG-T1 Source-Verified Agent Engineering Control Triage

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: gc018_baseline

Date: 2026-06-28

Owner: Codex

rawMemoryReleased: false

## Purpose

Execute AECG-T1 as a source-verified triage and adaptation matrix for the
operator-provided Agent Engineering Control source bundle and the current
CodeGraph delta recorded by AECG-T0.

Decision: `AUTHOR_AECG_T2_AGENT_ENGINEERING_CONTROL_OWNER_SURFACE_MATRIX`.

## Decision / Baseline / Proposed Tranche

Decision: `AUTHOR_AECG_T2_AGENT_ENGINEERING_CONTROL_OWNER_SURFACE_MATRIX`.

Baseline: AECG-T0 selected source-verified triage before any promotion,
checker implementation, package import, runtime work, MCP wiring, watcher,
daemon, benchmark, merge automation, hook repair, or public-sync claim.

Proposed next tranche: AECG-T2 should promote only the high-value, non-duplicated
control subset into one CVF-owned reference matrix.

## Scope / Target / Owner Boundary

Allowed material scope:

- source-verify AEC gate candidates against the retained source bundle;
- source-verify existing CVF owner surfaces for equivalent or overlapping
  controls;
- classify each candidate as absorbed, adapt-to-owner, defer, reject, or block;
- create this GC-018 baseline and the AECG-T2 reference matrix;
- close the roadmap only after AECG-T3 decides whether a checker is justified.

Forbidden material scope:

- no direct import of the Agent Engineering Control package, schemas, receipts,
  tools, guard registry, or examples;
- no CodeGraph install/init, MCP wiring, watcher, daemon, benchmark, or
  affected-test CLI adoption;
- no PR merge automation, managed-hook repair automation, public-sync,
  provider/live proof, runtime/source/test mutation, package activation,
  certification, generated aggregate mutation, or universal governed-coding
  control claim.

Risk ceiling: R1 documentation/reference only.

## Source Authority

| Source | Path | Role |
|---|---|---|
| AECG-T0 roadmap | `docs/roadmaps/CVF_AECG_T0_CODEGRAPH_AGENT_ENGINEERING_CONTROL_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` | roadmap and boundaries |
| AEC source standard | `.private_reference/legacy/CVF_Agent_Engineering_Control_Standard/docs/standards/CVF_AGENT_ENGINEERING_CONTROL_STANDARD_2026-06-20.md` | external advisory source |
| AEC mapping | `.private_reference/legacy/CVF_Agent_Engineering_Control_Standard/docs/reference/CVF_CLAUDEKIT_ENGINEER_ABSORPTION_MAPPING_2026-06-20.md` | external advisory mapping |
| External intake chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | routing authority |
| Work order template | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | source verification and work-order control owner |
| Closure quality standard | `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md` | closure, evidence, and diff gate owner |
| Commit steward standard | `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md` | commit-shape and handoff split owner |
| Governed lifecycle standard | `docs/reference/CVF_GOVERNED_WORK_LIFECYCLE_AND_DESIGN_CONTROL_STANDARD_2026-06-11.md` | lifecycle owner |
| Truth foundation claim guard | `governance/compat/check_truth_foundation_claim_guard.py` | existing static claim-overreach guard pattern |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| AECG-T0 authorizes T1 triage only and parks runtime/package/checker work | `docs/roadmaps/CVF_AECG_T0_CODEGRAPH_AGENT_ENGINEERING_CONTROL_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` | Proposed Roadmap; Claim Boundary | `AUTHOR_AECG_T1_GC018_FOR_AGENT_ENGINEERING_CONTROL_TRIAGE_AND_CODEGRAPH_DELTA` | AECG-T0 roadmap | VALUE_SET | ACCEPT |
| AEC source positions CVF as control layer, not coding-agent replacement | `.private_reference/legacy/CVF_Agent_Engineering_Control_Standard/docs/standards/CVF_AGENT_ENGINEERING_CONTROL_STANDARD_2026-06-20.md` | Non-Negotiable Positioning; Claim Boundary | `CVF controls scope, gates, evidence, receipts, review, freeze, and claim boundary` | external AEC standard | DOC_ONLY_NEW | ACCEPT |
| AEC source lists twelve controlled behavior candidates | `.private_reference/legacy/CVF_Agent_Engineering_Control_Standard/docs/standards/CVF_AGENT_ENGINEERING_CONTROL_STANDARD_2026-06-20.md` | Controlled Behaviors | `Controlled Behaviors` | external AEC standard | DOC_ONLY_NEW | ACCEPT |
| AEC mapping routes review evidence, debug, prior work, parallel implementation, maintenance, slop, diff lint, artifact gates, merge, hooks, and work journal into control knowledge | `.private_reference/legacy/CVF_Agent_Engineering_Control_Standard/docs/reference/CVF_CLAUDEKIT_ENGINEER_ABSORPTION_MAPPING_2026-06-20.md` | Mapping Table; Final Mapping Statement | `Engineering harness knowledge becomes CVF control knowledge` | external AEC mapping | DOC_ONLY_NEW | ACCEPT |
| External repo or copied folder input must map to a CVF-owned owner surface before promotion | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | Central Core; Mandatory Chain; Input Type Router | `External repo or copied folder` | external intake chain map | LITERAL_INVARIANT | ACCEPT |
| Work orders already own source verification, allowed scope, forbidden scope, evidence requirements, claim boundary, and closure checklist requirements | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | Enforcement / Verification; Source Verification Block; Claim Boundary | `Source Verification Table`; `Closure Diff Gate`; `Agent Operation Trace Block` | work-order template | VALUE_SET | ACCEPT |
| Closure quality already requires roadmap trace, closure diff, changed-file evidence, resolved checklist, and session continuity updates | `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md` | Purpose; Scope; Machine Closure Package | `Closure Diff Gate`; `Machine Closure Package` | closure quality standard | VALUE_SET | ACCEPT |
| Commit steward already owns split between material commits, handoff sync, and session sync | `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md` | Scope; Protocol / Contract / Requirements | `run_agent_commit_steward_preflight.py` | commit steward standard | VALUE_SET | ACCEPT |
| Governed lifecycle already owns design, spec, work order, build, review, freeze sequencing | `docs/reference/CVF_GOVERNED_WORK_LIFECYCLE_AND_DESIGN_CONTROL_STANDARD_2026-06-11.md` | Purpose; Lifecycle; Enforcement | `INTAKE`; `DESIGN`; `SPEC`; `WORK ORDER`; `BUILD`; `REVIEW`; `FREEZE` | lifecycle standard | VALUE_SET | ACCEPT |
| Existing truth-foundation checker already guards an important class of external-input and hard-claim overreach | `governance/compat/check_truth_foundation_claim_guard.py` | `CLAIM_RULES`; `diagnose_truth_foundation_claims`; `main` | `diagnose_truth_foundation_claims` | truth foundation claim guard | RUNTIME_BEHAVIOR | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0007, ADIF-0006

## Triage Matrix

| Candidate | AEC source basis | Current CVF owner | Disposition | Reason |
|---|---|---|---|---|
| Agent review evidence | AEC review-evidence standard, protocol, guard, schema, and README gate | closure quality standard; reviewer-fast gate; work-order evidence requirements | ADAPT_TO_EXISTING_REVIEW_EVIDENCE_SURFACES | High value, but CVF already requires evidence-backed review and closure artifacts. Promote as matrix language, not schema import. |
| Debug root cause certainty | AEC debug root-cause standard and protocol | finding-to-governance learning flow; work-order fail conditions; ADIF | ADAPT_TO_EXISTING_FINDING_BOUNDARIES | Useful as review vocabulary. Do not add a duplicate debug schema before a concrete recurring defect requires it. |
| Prior work discovery | AEC prior-work standard, protocol, guard, and template | source verification; prior absorption checks; external intake chain map | ABSORB_AS_SOURCE_VERIFICATION_DISCIPLINE | Already central to CVF. T2 should name it explicitly as a pre-write discipline. |
| Parallel implementation prevention | AEC parallel implementation control standard | owner-surface mapping; no parallel core rules; commit steward split | ADAPT_TO_OWNER_SURFACE_MATRIX | Useful for preventing duplicate lanes; express through owner matrix and rejection rows. |
| Roadmap alignment | AEC roadmap alignment standard/protocol | governed lifecycle design-control gate; roadmap closure freshness | ABSORB_AS_EXISTING_LIFECYCLE_RULE | CVF already controls this through roadmap and closure gates. |
| Maintenance cost gate | AEC maintenance cost standard and report | value-parked lane reopen discipline; roadmap acceptance criteria | ADAPT_AS_VALUE_FILTER | Useful for closeout and next-lane decisions. T2 should add value-now and reopen-condition columns. |
| AI slop control | AEC AI slop standard/protocol | structural completeness, literal-format gotchas, truth claim guard, closure quality | ADAPT_AS_REVIEW_LANGUAGE_ONLY | Valuable as a plain-language defect class, but too broad for a new checker now. |
| Diff content lint | AEC diff-content standard/protocol and checker script | truth foundation claim guard; Delta claim boundary guard; markdown structural guard | DEFER_CHECKER_DECISION_TO_AECG_T3 | Candidate is plausible, but needs T3 value decision against existing guards. |
| Workflow artifact gate | AEC workflow artifact standard/protocol | work-order template; closure quality gate; machine closure package | ABSORBED_BY_EXISTING_CLOSURE_GATES | Existing CVF gates already block missing closure artifacts. |
| Governed PR merge | AEC governed PR merge protocol | public/provenance boundary; commit steward; push-readiness preview | DEFER_WITH_REOPEN_CONDITION | High-risk automation; no PR merge or push behavior authorized. |
| Managed hooks health | AEC managed hooks manifest protocol | autorun workflow control; local hook catalogs; push-readiness preview | DEFER_WITH_REOPEN_CONDITION | Useful as future hygiene, but hook repair automation remains parked. |
| Agent work journal | AEC work-journal protocol/template | active handoff; Agent Operation Trace; session state | ADAPT_TO_HANDOFF_AND_AOT_SURFACES | Useful only as continuity vocabulary; do not duplicate active handoff/session state. |
| CodeGraph affected-test routing | AECG-T0 CodeGraph delta | future test-selection evidence owner | DEFER_WITH_REOPEN_CONDITION | No CodeGraph CLI or runtime adoption authorized. |
| CodeGraph worktree/index mismatch warning | AECG-T0 CodeGraph delta | source-read fallback and graph freshness discipline from CGE-T2 | ADAPT_AS_BOUNDARY_LANGUAGE | Already fits prior CGE stale/fallback discipline. |
| CodeGraph MCP/tool surface design | AECG-T0 CodeGraph delta | future MCP gateway or adapter contract only | DEFER_WITH_REOPEN_CONDITION | No MCP wiring or agent config mutation authorized. |

## T1 Decision

Decision: `PROMOTE_AECG_T2_OWNER_SURFACE_MATRIX`.

Rationale: the highest-value portion of the source bundle is not the package or
its local tools. It is the control taxonomy: review evidence, root-cause
certainty, prior-work discovery, parallel implementation prevention,
maintenance cost, diff/claim discipline, workflow artifact completeness, and
continuation evidence. Most of these already have CVF owner surfaces. AECG-T2
should therefore create one CVF-owned reference matrix that names the mapping,
accepted vocabulary, rejected imports, and future checker candidates.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | AECG-T2 owner-surface reference matrix | Internal agents may use the matrix as planning and review guidance only | this baseline and AECG-T0 roadmap | N/A with reason: documentation/reference only | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future CLI/MCP adapter owner, if separately authorized | no ingress, authentication, mutation, raw-data release, public claim, or adapter support is authorized | AECG-T0 and this baseline forbid adapter/runtime work | deferred adapter owner; no current adapter | `DEFERRED_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External repo or copied folder |
| Chain map route | External repo or copied folder -> source-verified triage -> CVF-owned owner-surface matrix -> future GC-018 only if implementation is separately authorized |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this GC-018 baseline |
| Disposition | ADAPT selected AEC taxonomy and CodeGraph delta into AECG-T2 owner-surface matrix |
| Claim boundary | no runtime, package import, CodeGraph runtime/MCP/watcher/daemon, public-sync, provider/live proof, merge automation, hook repair, checker implementation, or universal governed-coding-control claim |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | AECG-T1 source-verified triage and adaptation decision |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no runtime receipt is created or consumed |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source verification, triage matrix, and governance gate evidence only |
| invocationBoundary | local private provenance documentation and source verification |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, Web runtime, adapter, package, watcher, or daemon interception claim |
| claimLanguage | triage and owner-surface selection only |
| forbiddenExpansion | no runtime, provider/live proof, public-sync, package activation, CodeGraph install/init, MCP wiring, watcher/daemon, merge automation, hook repair, checker implementation, certification, generated aggregate mutation, or universal governed-coding-control claim |

## Acceptance Criteria

| ID | Criterion | Disposition |
|---|---|
| AC1 | AEC source bundle is treated as external advisory input only | PASS |
| AC2 | each AEC candidate is mapped to an existing CVF owner or parked condition | PASS |
| AC3 | direct package import is rejected | PASS |
| AC4 | CodeGraph prior CGE-T1/CGE-T2 boundaries remain binding | PASS |
| AC5 | AECG-T2 reference matrix is selected | PASS |
| AC6 | runtime/provider/public/MCP/checker claims remain out of scope | PASS |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| source bundle remains advisory | external source rows use advisory/input disposition | PASS |
| T1 decision | `PROMOTE_AECG_T2_OWNER_SURFACE_MATRIX` | PASS |
| direct import decision | direct package import rejected | PASS |
| checker implementation | no checker implemented by T1 | PASS |
| public export | `DEFERRED_PRIVATE_ONLY` | PASS |
| runtime/live proof | N/A with reason: no runtime/provider governance behavior is asserted | N/A with reason |

## Evidence / Verification

| Evidence item | Command or artifact | Required result |
|---|---|---|
| base head | `git rev-parse --short HEAD` | `29b63b87` before material edit |
| source bundle inventory | `rg --files .private_reference\legacy\CVF_Agent_Engineering_Control_Standard` | source files present under ignored legacy reference storage |
| AEC source grep | `rg -n "Agent Review Evidence|Debug Root Cause|Prior Work|Parallel Implementation|Maintenance Cost|AI Slop|Diff Content"` | source candidates found |
| CVF owner grep | `rg -n "Source Verification|Closure Diff Gate|Agent Operation Trace|commit steward|claim boundary"` | owner surfaces found |
| governance gates | pre-implementation, structural, external-intake, closure, commit-steward | PASS before commit |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | AECG-T0 roadmap, external source bundle, CVF work-order/closure/lifecycle/commit-steward references, and current static claim guards |
| Runtime behavior claimed | N/A_WITH_REASON: this baseline performs documentation/source verification only |
| Live/provider proof claimed | N/A_WITH_REASON: no live governance behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized or performed |
| Freshness disposition | PASS - current source evidence supports reference/triage closeout only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance external absorption triage. No public-sync remote,
public commit, public artifact path, or public claim is authorized.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | N/A with reason: direct single-agent source-verification tranche | N/A with reason | N/A with reason |
| Completion or reviewer artifact | `docs/reviews/CVF_AECG_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | `Status: CLOSED_PASS_BOUNDED` after this batch | PASS |
| Roadmap state | `docs/roadmaps/CVF_AECG_T0_CODEGRAPH_AGENT_ENGINEERING_CONTROL_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` | `Status: CLOSED_PASS_BOUNDED` after this batch | PASS |
| Reference matrix | `docs/reference/CVF_AECG_T2_AGENT_ENGINEERING_CONTROL_OWNER_SURFACE_MATRIX_2026-06-28.md` | `Status: ACTIVE_REFERENCE` | PASS |
| Checker implementation | N/A with reason: AECG-T3 decides no checker now | no checker path changed | N/A with reason |
| Checker tests | N/A with reason: no checker implementation | no test path changed | N/A with reason |
| Registry JSON | BLOCKED with reason: no registry JSON mutation is authorized | no registry path changed | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown mutation is authorized | no registry path changed | BLOCKED with reason |
| External evidence digest | N/A with reason: external source hashes were recorded by AECG-T0 | no new digest path required | N/A with reason |
| System loop interlock | N/A with reason: local documentation/reference only | Claim Boundary | N/A with reason |
| Public sync | N/A with reason: no public-sync is authorized | `DEFERRED_PRIVATE_ONLY` | N/A with reason |
| Runtime/live proof | N/A with reason: no runtime/provider governance behavior is claimed | no live run required | N/A with reason |
| Session continuity | active session/front-door sync planned after material commit | separate session-sync commit required | PASS |

## Claim Boundary

AECG-T1 is a documentation and source-verification baseline only. It does not
authorize or claim CodeGraph runtime, MCP wiring, watcher/daemon behavior,
benchmark proof, affected-test CLI use, Agent Engineering Control package
import, schema import, receipt runtime, guard registry import, merge automation,
managed-hook repair, provider/live proof, public-sync, package activation,
certification, generated aggregate mutation, production readiness, hosted
readiness, or universal governed-coding control.
