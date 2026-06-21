# CVF MPI Memory Plane Integration Roadmap - Codex Rebuttal

Memory class: FULL_RECORD

Status: REVIEWER_REBUTTAL_COMPLETE_RECOMMEND_MPI_T1_FIRST

docType: review

Date: 2026-06-21

## Purpose

Review the Claude-authored draft roadmap
`docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md`
without converting it into dispatch authority. The operator explicitly
recognized the value of this Memory Plane Integration proposal and stated that
Memory Plane is important enough to implement. The review therefore recommends
implementation sequencing, not rejection.

## Scope / Methodology

Scope: review the draft roadmap as external-agent returned output, compare its
claims against active session state and source files, and produce a Codex
rebuttal. This review does not edit the Claude roadmap, create a GC-018, create
a work order, or dispatch implementation.

Methodology:

- Read the active session front door, generated state registry, active handoff,
  and guard orientation index.
- Read the Claude MPI roadmap draft in full.
- Verify selected source claims against current source paths.
- Classify the draft as valuable but not current dispatch authority.
- Record required revisions and first-tranche sequencing.

## Startup And State Acknowledgment

Startup acknowledged: current mode=`lsc_t5_t7_learning_plane_bridge_latency_guard_closed_operator_checkpoint`; active handoff=`AGENT_HANDOFF_V20_2026-06-19.md`; next allowed move=operator checkpoint to select the next governed lane or explicitly authorize a fresh governed work order; parked checkpoint=AAF-T6, AAF-T7, CGE-T3, ACE-R1, MLW7, MLW8, runtime/provider/live/public-sync/direct-interception/actual CLI-MCP adapter/ledger-generator-durable-store work.

## Review Decision

Decision: `ACCEPT_VALUE_RECOMMEND_MPI_T1_FIRST`.

MPI is a useful and important integration lane. It should be implemented, but
not as one broad assignment and not by jumping straight into runtime projection
or external adapter behavior. It must still go through operator selection,
fresh GC-018, source-verified work order, and per-tranche gates.

Recommended near-term disposition:

- Revise the roadmap to `DRAFT_FOR_OPERATOR_SELECTION`.
- If the operator selects MPI as the next lane, dispatch only MPI-T1 first.
- Keep MPI-T2, MPI-T3, and MPI-T4 on hold until MPI-T1 closes and the operator
  confirms the next risk step.

## External Knowledge Intake Routing

Chain map: `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`

| Field | Disposition |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | REVIEW_AND_CLASSIFY_BEFORE_ABSORPTION |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; Guard Orientation external knowledge absorption row; active session next-move boundary |
| Owner surface | `docs/reviews/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_CODEX_REBUTTAL_2026-06-21.md` |
| Disposition | ABSORB_AS_REVIEW_INPUT_RECOMMEND_MPI_T1_FIRST |
| Claim boundary | Rebuttal only; no implementation, runtime route change, provider/live proof, public-sync, adapter build, or work-order dispatch |

## Source Verification Snapshot

| Claimed item | Source file | Verified line/section | Verified path or symbol | Disposition |
| --- | --- | --- | --- | --- |
| MPI roadmap is a draft for reviewer rebuttal | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | line 5 | `Status` | ACCEPT |
| MPI roadmap says planning only | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` | lines 55-56 and 257-259 | `Authorization / Decision`; `Claim Boundary` | ACCEPT_WITH_REBUTTAL |
| Current session next move is operator checkpoint, not MPI dispatch | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | `nextAllowedMove` entry | `nextAllowedMove` | ACCEPT |
| Current parked scope includes runtime/provider/public/adapter boundaries | `AGENT_HANDOFF_V20_2026-06-19.md` | Startup Acknowledgment and Next Allowed Move sections | parked checkpoint and forbidden scope | ACCEPT |
| Memory readout route has service-token or session authentication | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | lines 3-4 and 136-160 | `verifyServiceTokenRequest`; `verifySessionCookie` | ACCEPT |
| Memory readout route preserves summary-only flags | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | lines 202-203 | `rawMemoryReleased`; `canReinject` | ACCEPT |
| Memory projection strips candidate content | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-runtime-readout.ts` | lines 11-20 and 41-50 | `MemoryRetrievalCandidate`; `rawMemoryReleased`; `canReinject` | ACCEPT |
| Corpus Scan Registry is generated from source entries | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` | lines 51-74 and 236-245 | registry aggregate; source layout | ACCEPT |
| Corpus finding discovery has an existing rule | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` | lines 304-314 | Finding Discovery Rule | ACCEPT |
| CI1-T11 already absorbed memory/learning legacy scans | `docs/roadmaps/CVF_CI1_T11_MEMORY_LEARNING_ABSORPTION_CONSOLIDATED_ROADMAP_2026-06-05.md` | Purpose, Source Intake, Tranche Plan, Closure Update | CI1-T11; MLW0; MLW1-MLW6 | ACCEPT |
| MLW0 maps legacy vocabulary to current CVF source authority | `docs/reference/CVF_MLW0_CURRENT_SOURCE_VERIFICATION_MAP_2026-06-05.md` | Purpose and source-verification map | current source mapping for CI1-T11 vocabulary | ACCEPT |
| MLW1-MLW6 core chain converted absorption into bounded contracts | `docs/reviews/CVF_MLW1_MLW6_MEMORY_LEARNING_CORE_WORKFLOW_CHAIN_COMPLETION_2026-06-05.md` | Closure evidence and authority assets | MLW1-MLW6 bounded artifacts | ACCEPT |
| KGR pre-review separates Memory Plane from Knowledge Graph Retrieval and records partial Graphify/KGR coverage | `docs/reference/CVF_KGR_ABSORPTION_PREREVIEW_2026-06-01.md` | Why This Is NOT Memory Plane; Prior Absorption History; Blocked Work | KGR partial recheck gap | ACCEPT_WITH_GAP |
| KGR1 bounded LPF local graph retrieval owner exists | `docs/roadmaps/CVF_KGR1_KNOWLEDGE_GRAPH_RETRIEVAL_ROADMAP_2026-06-01.md`; `docs/reviews/CVF_KGR1_KNOWLEDGE_GRAPH_RETRIEVAL_LOCAL_REVIEW_2026-06-02.md` | Work Plan; Source Verification; Claim Boundary | KGR store/builder/`graph_search` | ACCEPT |
| Graphify/KGR corpus registry entry exists | `docs/corpus-intelligence/registry/entries/legacy-cvf-important-graphify.json` | registry entry | `CVF_Important / Knowledge Base_Graphify` | ACCEPT_WITH_GAP |
| LSC-T6 is adapter-contract-only and does not implement an adapter | `docs/reference/learning_signal_chain/CVF_LSC_T6_EXTERNAL_AGENT_CLI_MCP_SIGNAL_CONTRACT.md` | lines 38-45 and 355-378 | `adapterContractOnly`; forbidden expansion | ACCEPT |
| LSC is already durable memory surface | LSC closure state and LSC-T5/T7 boundary | active state and handoff closure notes forbid ledger/source/generator/durable store | REJECT_REWORD |

## Findings / Position

Position: MPI should become a selectable next lane, with MPI-T1 as the first
implementation tranche. The draft has useful instincts around summary-only read
boundaries, GC-051 reuse, and external-agent read symmetry, but it initially
absorbed only the current Memory-plane surfaces. It must explicitly route the
CI1-T11/MLW legacy-absorption chain into MPI-T1 before dispatch, separate
doc-only mapping from runtime-bearing projection work, classify
human-reviewable governed records separately from fast retrieval/readout
surfaces, treat indexes as plane/layer management artifacts, keep KGR visible as
a structural graph/context index with partial legacy coverage, and correct LSC
durability language before any work order exists.

## Rebuttal Findings

### Finding 1 - MPI is implementation-worthy but the roadmap is not dispatch authority

The roadmap correctly says it authorizes planning only, but its Authorization
section also says the operator direction is to make the Memory plane coherent
and connect it to external CLI/MCP core value. That wording is too close to
dispatch authority. Current session state says the next move is an operator
checkpoint, not MPI implementation.

Required revision before any work order:

- Replace implementation-sounding authority with operator-selection wording.
- Add an explicit operator-selection / first-tranche sequence.
- State that Claude's draft is external-agent input, not source authority.

### Finding 2 - The "four durable-memory surfaces" claim overstates LSC

The roadmap calls LPF Memory runtime, Corpus Scan Registry, GC-022 records, and
Learning Signal Chain "four separate durable-memory surfaces." That is unsafe.
Recent LSC closure deliberately forbids ledger store, source directory,
generator, drift checker, durable store, and runtime Learning Plane mutation.

Required revision:

- Treat LSC as a bounded signal-chain reference/helper-readout surface, not a
  durable memory surface.
- If future MPI wants LSC durable behavior, it needs a separate GC-018 after
the parked ledger/generator/durable-store boundary is explicitly released.

### Finding 2A - Legacy absorption was only partial until CI1-T11/MLW alignment was added

The roadmap discussed MKG7, GC-051, GC-022, and LSC, but did not originally
require the worker to read the governed legacy memory/learning absorption chain.
That chain already exists through CI1-T11, MLW0, and MLW1-MLW6. Without those
rows, MPI risks re-solving already-absorbed memory, RAG/context, continuity, and
audit-feedback lessons or missing their non-negotiable boundaries.

Required revision:

- Add CI1-T11, MLW0, and MLW1-MLW6 to roadmap Current State and Source
  Verification.
- Add a legacy absorption gate to MPI-T1 before any worker dispatch.
- Keep legacy code/vocabulary non-authoritative unless mapped through MLW0 or
  current CVF source.

### Finding 2B - File reviewability and Memory Plane retrieval need separate classes

The operator's two concerns are compatible but must be classified separately.
CVF line limits and rotation rules exist so governed docs remain reviewable by
humans. A unified Memory Plane can later provide vector-DB-like fast retrieval
for agents, but only as bounded summary/pointer/index access back to governed
sources. Treating those as the same thing would either bloat docs into an index
or let retrieval summaries replace source review.

Required revision:

- MPI-T1 must classify each surface as human-reviewable governed source,
  generated episodic/semantic index, bounded runtime readout,
  contract/spec/parked architecture, or provider/private memory.
- GC-023 remains the reviewability control for governed files.
- MPI-T2/T3/T4 may improve fast access only after separate authorization and
  must preserve summary/pointer discipline.

### Finding 2C - KGR Graph Memory must be visible as partial coverage, not silently absorbed

The operator/Claude exchange identified KGR Graph Memory as a key missing
memory-architecture surface. Current CVF evidence is mixed: KGR1 has a bounded
LPF local graph retrieval owner, but the KGR pre-review and Graphify registry
entry preserve a gap around the legacy Graphify/KGR corpus. MPI must not treat
KGR as either "just Memory Plane" or "fully absorbed legacy."

Required revision:

- Add KGR as a structural graph/context index class adjacent to the Memory
  Plane.
- Cite KGR pre-review, KGR1 roadmap/review, and the Graphify registry entry.
- Mark Graphify/KGR legacy coverage `PARTIAL_RECHECK_REQUIRED` or equivalent
  until a dedicated KGR/Graphify recheck closes it.
- Do not authorize graph persistence, vector DB, web-route graph integration,
  CLI graph build, external graph dependencies, or KGR runtime expansion in
  MPI-T1.

### Finding 3 - MPI-T2 is materially higher risk than MPI-T1

MPI-T2 proposes exposing Corpus Scan Registry findings through the existing
Memory readout surface. Even if the projection is summary-only and
deterministic, it touches runtime route/readout semantics under runtime extension paths.
That is not the same risk class as a reference map.

Required sequencing:

- MPI-T1 may be doc/reference-only if later selected.
- MPI-T2 must have its own GC-018, exact source-verification rows, file-size
  review, local route tests, RAW sentinel tests, and no-write/no-reinjection
  tests.
- MPI-T2 must not claim provider/live behavior, hosted readiness, production
  readiness, or external-agent adapter behavior.

### Finding 4 - MPI-T3 should not use an internal route interface as a stable external contract without care

The roadmap says MPI-T3 should map external read requests to the existing
`MemoryRuntimeReadoutBody` schema. That symbol currently appears as a local
route interface, not as a public or shared contract module. A doc-only contract
may cite it, but a worker must not invent a parallel schema or imply a stable
external API without source-backed ownership.

Required revision:

- MPI-T3 should be contract-only unless a later runtime tranche extracts a
  shared schema.
- It must include `adapterContractOnly=true`.
- It must explicitly forbid MCP tool, CLI adapter, shell bridge, execution,
  public-sync, and provider/live proof.

### Finding 5 - MPI-T4 should be optional and likely deferred

The helper fast-path risks expanding the already-busy governance helper surface
or creating a second readout vocabulary. The roadmap's `N/A_WITH_REASON`
escape hatch is good and should be strengthened.

Required revision:

- Make MPI-T4 default to `DEFER_UNLESS_T1_T2_T3_CLOSE_WITH_NEED`.
- If implemented later, prefer a separate narrow helper over expanding the AAF
  worker-return helper unless the work order proves that reuse is safer.
- The helper must never block closure or mutate registry, Memory runtime, LSC,
  session state, or handoff state.

## Proposed Priority Order

| Priority | Candidate | Disposition |
| --- | --- | --- |
| 1 | Operator checkpoint after LSC closure | REQUIRED_NOW |
| 2 | MPI roadmap | RECOMMEND_SELECT |
| 3 | MPI-T1 | RECOMMEND_FIRST_TRANCHE |
| 4 | MPI-T2/T3 | HOLD_AFTER_T1 |
| 5 | MPI-T4 | OPTIONAL_AFTER_T2_T3_NEED |
| 6 | AAF-T6 / AAF-T7 / CGE-T3 / ACE-R1 / MLW7 / MLW8 | Remain parked unless separately selected |

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Draft roadmap is mistaken for dispatch authority | Keep status as operator-selection draft; require explicit operator selection and fresh GC-018 |
| LSC is overstated as durable memory | Reword LSC as bounded signal-chain reference/helper-readout surface |
| MPI-T2 runtime projection expands scope silently | Split MPI-T2 from MPI-T1; require separate work order, route tests, RAW sentinel tests, no-write tests |
| MPI-T3 implies actual external adapter behavior | Keep `adapterContractOnly` and forbid MCP tool, CLI adapter, shell bridge, and execution |
| MPI-T4 expands helper surface before need is proven | Default defer until T1/T2/T3 closure evidence shows need |

## Finding-To-Governance Learning Disposition

defect class: `OPERATOR_SCOPE_CLARITY_GAP`

learning lane: `GOVERNANCE_CONTROL_PLANE`

runtime/provider/cost learning lane: `N/A_WITH_REASON` - no runtime, provider,
live, cost, token-budget, or public-sync behavior changed or claimed.

| Finding or lesson | Disposition | Learning lane | Next action |
| --- | --- | --- | --- |
| MPI roadmap has value and should be selectable | RECOMMEND_MPI_T1_FIRST | GOVERNANCE_CONTROL_PLANE | operator selection before any GC-018 |
| LSC durable-memory wording is unsafe | REJECT_REWORD | GOVERNANCE_CONTROL_PLANE | reword before work order |
| MPI roadmap did not explicitly route CI1-T11/MLW absorption | PARTIAL_ABSORPTION_FIX_REQUIRED | GOVERNANCE_CONTROL_PLANE | add legacy absorption gate before MPI-T1 dispatch |
| Memory Plane classification was missing | CLASSIFICATION_FIX_REQUIRED | GOVERNANCE_CONTROL_PLANE | separate human-reviewable governed source from fast retrieval/readout surfaces |
| KGR Graph Memory partial legacy coverage was not visible enough | PARTIAL_RECHECK_REQUIRED | GOVERNANCE_CONTROL_PLANE | add structural graph/context index row and KGR partial-coverage boundary |
| MPI-T2/T3/T4 carry runtime or adapter risk | DEFERRED_TO_SEPARATE_GC018 | GOVERNANCE_CONTROL_PLANE | split from MPI-T1 |

## Required Revisions To Claude Roadmap

1. Change the roadmap status to `DRAFT_FOR_OPERATOR_SELECTION`, not a
   dispatch-ready status.
2. Add operator-selection, first-tranche, and design-control sections.
3. Reword LSC from "durable-memory surface" to "bounded signal-chain reference
   and helper-readout surface."
4. Add explicit CI1-T11, MLW0, and MLW1-MLW6 legacy absorption alignment to
   roadmap, GC-018, and MPI-T1 work order.
5. Add Memory Plane classification that separates human-reviewable governed
   source from generated index, runtime readout, contract/spec, and
   provider/private memory classes.
6. Add plane/layer indexing as a first-class MPI-T1 map goal, including KGR as
   structural graph/context index.
7. Mark Graphify/KGR legacy coverage as partial recheck; do not claim complete
   KGR legacy absorption from CI1-T11 or KGR1 alone.
8. Split MPI-T1 from runtime-bearing MPI-T2/T3/T4 risk.
9. Strengthen MPI-T2 acceptance criteria with route tests, RAW sentinel tests,
   `rawMemoryReleased=false`, `canReinject=false`, no registry write, and no
   aggregate hand-edit.
10. Strengthen MPI-T3 with `adapterContractOnly=true` and no actual CLI/MCP
   behavior.
11. Make MPI-T4 default-deferred.

## Live Run Position

No live provider run is needed for this rebuttal or for a future doc-only
MPI-T1 map. MPI-T2/T3 route or contract tests should be local deterministic
tests unless a later work order makes a release/public/provider governance
claim. Any actual live provider/governance behavior claim requires the live
proof standard and failure diagnostics.

## Rescan Intelligence Hardening

Original source artifact: `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md`

Predecessor intake artifact: N/A with reason: this is the first Codex rebuttal
for the MPI draft.

Delta ledger status: COMPLETE_WITH_DECLARED_LIMITS.

Routing matrix status: COMPLETE_WITH_DECLARED_LIMITS.

Semantic sampling status: COMPLETE_WITH_DECLARED_LIMITS.

- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Delta category | Current finding | Predecessor finding | New disposition | Reason |
| --- | --- | --- | --- | --- |
| UNCHANGED_FROM_INTAKE | MPI has useful integration value | Claude roadmap proposes Memory plane integration | ACCEPT_VALUE | Operator stated Memory Plane is important |
| CHANGED_DISPOSITION | MPI should be selectable, with MPI-T1 first | Claude roadmap says planning only but contains implementation-shaped direction | RECOMMEND_MPI_T1_FIRST | Need first-tranche safety |
| NEW_FINDING | LSC is overstated as durable memory | N/A | REJECT_REWORD | LSC closure forbids ledger/source/generator/durable-store expansion |
| NEW_FINDING | CI1-T11/MLW legacy absorption must be explicit | N/A | REQUIRE_ALIGNMENT | Prevents MPI from bypassing existing legacy absorption outputs |
| NEW_FINDING | Human-reviewable docs and fast retrieval memory need separate classes | N/A | REQUIRE_CLASSIFICATION | Prevents file-size guard and vector-DB-like retrieval goals from being conflated |
| NEW_FINDING | KGR Graph Memory is structural index layer with partial legacy coverage | N/A | REQUIRE_KGR_GAP_VISIBILITY | Prevents false complete-absorption claim |
| REMOVED_OR_REJECTED | Immediate MPI-T2/T3/T4 implementation | N/A | REJECT_NOW | Runtime and adapter-bearing work requires separate future authorization |

### Follow-Up Routing Matrix

| Routing lane | Item | Disposition |
| --- | --- | --- |
| DO_NOW | Preserve rebuttal and make roadmap operator-selection ready | COMPLETE |
| DO_NOW | Add CI1-T11, MLW0, and MLW1-MLW6 alignment to MPI-T1 dispatch surfaces | REQUIRED_BEFORE_WORKER |
| DO_NOW | Add Memory Plane classification to MPI roadmap and MPI-T1 dispatch packet | REQUIRED_BEFORE_WORKER |
| DO_NOW | Add KGR structural index classification and Graphify/KGR partial-recheck status | REQUIRED_BEFORE_WORKER |
| SEPARATE_RUNTIME_TRANCHE | MPI-T2 route/readout projection and any runtime schema extraction | DEFER_TO_FRESH_GC018 |
| STRATEGIC_OPERATOR_DECISION | Whether MPI-T1 becomes the next dispatch lane | REQUIRED_BEFORE_DISPATCH |
| OUT_OF_SCOPE | Provider/live proof, public-sync, adapter implementation, raw release, reinjection, durable writes | REJECTED_FOR_THIS_REBUTTAL |
| RESOLVED_BY_DESIGN | MPI-T1 can be doc-only map if selected | ACCEPT_AS_FIRST_TRANCHE |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| MPI-RS1 | Purpose | Four durable-memory surfaces include LSC | REJECT_REWORD | Does recent LSC closure authorize a durable ledger? | PASS |
| MPI-RS2 | Tranche Plan MPI-T2 | Scan registry findings can be read through Memory readout | DEFER_SEPARATE_RUNTIME_TRANCHE | Does this silently alter runtime route/readout semantics? | PASS |
| MPI-RS3 | Tranche Plan MPI-T3 | External agents can receive summary-only memory readout | DEFER_CONTRACT_ONLY | Does this imply actual CLI/MCP adapter behavior? | PASS |
| MPI-RS4 | Claim Boundary | Planning only | ACCEPT_WITH_REBUTTAL | Could roadmap wording be mistaken for dispatch authority? | PASS |
| MPI-RS5 | Legacy absorption | CI1-T11/MLW chain exists before MPI | REQUIRE_ALIGNMENT | Could MPI miss already-absorbed memory/RAG/continuity lessons? | PASS |
| MPI-RS6 | Memory classification | governed docs and retrieval/index surfaces have different purposes | REQUIRE_CLASSIFICATION | Could fast retrieval undermine human source review or line-limit discipline? | PASS |
| MPI-RS7 | KGR structural index | KGR1 exists but Graphify/KGR legacy remains partial coverage | REQUIRE_KGR_GAP_VISIBILITY | Could MPI falsely claim all related legacy has been absorbed? | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private provenance rebuttal. No public-sync remote, public
commit, public artifact path, hosted proof, or public README/catalog claim is
included.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | MPI roadmap rebuttal only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no runtime receipt is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | local reviewer reads draft roadmap and source references |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | review, priority, and boundary rebuttal only |
| forbiddenExpansion | implementation, adapter behavior, provider/live, public-sync, runtime mutation, durable write, raw release, reinjection, queue/daemon, watcher, readiness, full-hook equivalence, and universal control remain out of scope |

## Epistemic Process Block

| Field | Disposition |
| --- | --- |
| Evidence Comparison | Compared Claude roadmap claims against active session state, active handoff, memory readout route, readout projection, Corpus Scan Registry standard, LSC-T6 contract, CI1-T11 roadmap, MLW0 map, MLW1-MLW6 closure, KGR pre-review, KGR1 roadmap/review, and Graphify registry entry |
| Contradiction or Gap Disposition | LSC durable-memory wording rejected; legacy absorption gap identified and routed into MPI-T1; Memory Plane classification added; KGR partial coverage gap added; MPI dispatch authority sequenced through operator selection; runtime-bearing tranches separated from doc-only map |
| Claim Update | MPI is valuable and recommended for implementation via MPI-T1 first after operator selection, explicit CI1-T11/MLW alignment, reviewability/retrieval classification, and KGR partial-gap visibility |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | reviewer |
| Provider or surface | local workspace |
| Session or invocation | MPI roadmap Codex rebuttal, 2026-06-21 |
| Working directory | repository root |
| Command or tool surface | direct file reads, source search, apply_patch |
| Target paths | `docs/reviews/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_CODEX_REBUTTAL_2026-06-21.md` |
| Allowed scope source | operator request for Codex rebuttal of Claude draft; active session operator checkpoint |
| Before status evidence | HEAD `acb2b980`; `git status --short` showed untracked Claude roadmap draft |
| After status evidence | rebuttal artifact updated and roadmap revised for operator selection; no implementation, runtime, provider/live, public-sync, or session-sync change |
| Diff evidence | new review artifact only |
| Approval boundary | rebuttal/roadmap revision only; no dispatch, work order, runtime source edit, or commit requested |
| Claim boundary | implementation recommendation and boundary review only |
| Agent type | single reviewer |
| Invocation ID | `mpi-roadmap-codex-rebuttal-2026-06-21` |
| Expected manifest | `docs/reviews/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_CODEX_REBUTTAL_2026-06-21.md` |
| Actual changed set | `docs/roadmaps/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_2026-06-21.md` untracked from Claude; `docs/reviews/CVF_MPI_MEMORY_PLANE_INTEGRATION_ROADMAP_CODEX_REBUTTAL_2026-06-21.md` created by Codex |
| Manifest delta | ACCEPT with reason: Claude roadmap draft was pre-existing untracked input, not authored by this rebuttal |

## Claim Boundary

This rebuttal does not authorize MPI implementation, runtime route edits,
provider/live proof, public-sync, actual CLI/MCP adapter behavior, raw Memory
release, Memory reinjection, durable write changes, registry write authority,
new memory tiers, vector or embedding stores, graph persistence, production
readiness, or autonomous mutation.
