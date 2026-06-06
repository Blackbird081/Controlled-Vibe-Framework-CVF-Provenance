# CVF CI1-T9 Legacy Partial Scan Triage Packet

Status: TRIAGE_COMPLETE_PENDING_REVIEW
Date: 2026-06-05
Memory Class: EVIDENCE_RECORD
Scope: `.private_reference/legacy/CVF ADD/` and `.private_reference/legacy/CVF_Important/`
Mode: legacy partial scan routing, not runtime implementation
Public boundary: private provenance only

## Purpose

Create a reusable legacy partial-root triage foundation for rescan plus delta
plus routing plus adversarial sampling, with memory/learning candidates
prioritized for deep scan.

## Scope/Methodology

This packet uses filesystem-backed folder and file enumeration, current corpus
scan registry state, keyword/folder signal audit, prior CI1 absorption evidence,
and bounded adversarial sampling requirements. It does not deep-read all files
or dispatch implementation.

## Risk/Corrective Action

Main risk: a broad triage packet can be mistaken for deep semantic absorption.
Corrective action: all accepted implementation value must move through a fresh
GC-018 deep scan packet with file-level ledger, source hashes, delta routing,
and adversarial review before roadmap or runtime work.

## Objective

CI1-T9 reopens the two highest-priority partial legacy roots after the scan
hardening upgrade. The purpose is not to absorb every file in this packet. The
purpose is to create a durable triage layer that:

- proves the bounded roots and counts with filesystem-backed inventory;
- records deltas against the prior scan registry;
- routes high-value memory, learning, graph, context, and knowledge clusters;
- selects the next deep scan tranche on evidence, with adversarial sampling
  requirements already attached.

## Source Evidence

| Evidence item | Command or source | Result |
|---|---|---|
| CVF ADD root folders | `Get-ChildItem -LiteralPath '.private_reference/legacy/CVF ADD' -Directory -Force` | 15 top-level folders |
| CVF_Important root folders | `Get-ChildItem -LiteralPath '.private_reference/legacy/CVF_Important' -Directory -Force` | 24 top-level folders |
| CVF ADD file inventory | `rg --files --hidden --no-ignore '.private_reference/legacy/CVF ADD'` | 167 files |
| CVF_Important file inventory | `rg --files --hidden --no-ignore '.private_reference/legacy/CVF_Important'` | 230 files |
| CVF ADD path manifest | sorted path manifest | `f3fc93f632b727fb6fec57015943d643d8e346ff92987a146edcaaa3f1182d11` |
| CVF ADD content manifest | sorted path plus per-file SHA-256 manifest | `deecf5e4fa7ae80f9ef717f5c5469c741f98d878936290c4f75681cd7d37a7a2` |
| CVF_Important path manifest | sorted path manifest | `30639c25eedb642582a2f27590664b9fdce4063ffd511e44853a21d8eb2fcc1e` |
| CVF_Important content manifest | sorted path plus per-file SHA-256 manifest | `84c84f874a58e6bc501cb80ac3699acb9470d8ae9e3f11996a3995d5a05979f1` |
| Current registry state | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | both roots remain `PARTIALLY_SCANNED`; `legacy-cvf-add` still pointed at CI1-T3 candidate already completed |

## Original-Intake Delta Ledger

| Corpus | Prior state | CI1-T9 delta | Disposition | Reason |
|---|---|---|---|---|
| `legacy-cvf-add` | `PARTIALLY_SCANNED`; next scan recommended `CVF ADD/code-review-graph/` | stale recommendation found because CI1-T3 already completed code-review-graph | ACCEPT | registry should now point to memory/learning candidate rather than completed graph tranche |
| `legacy-cvf-add` | broad LHW-RESCAN-C routing only | 167-file root contains multiple memory, context, agent, workflow, graph, and knowledge candidates | DEFER | deep scan must proceed per folder; broad scan does not prove semantic absorption |
| `legacy-cvf-important-broad` | `PARTIALLY_SCANNED`; 24-folder inventory | 230-file root contains direct Learning Plane, Memory Architecture, Knowledge Palace, RAG, audit-memory, and planner-memory clusters | DEFER | deep scan must prioritize memory/learning owner surfaces first |
| `legacy-cvf-important-broad` | Graphify already absorbed in CI1-T2 | next recommendation still mentions Graphify/code-review path as possible next subfamily | ACCEPT_SUMMARY_ONLY | Graphify/code-review are no longer the best next target after CI1-T8 and external-review scan hardening |
| both roots | broad scan predates hardened rescan layer | CI1-T9 adds delta ledger, routing matrix, and adversarial sampling plan | ACCEPT | this becomes the reusable scan foundation for legacy partial roots |

## Follow-Up Routing Matrix

| Route | Target | Disposition | Evidence basis | Next action |
|---|---|---|---|---|
| Do now | CI1-T9 triage packet and registry recommendation refresh | ACCEPT | current inventory, prior registry, keyword/folder audit | record triage and select next deep scan |
| Next deep scan | `.private_reference/legacy/CVF ADD/cortex-hub/` | DEFER | strong memory/knowledge/MCP/learning language and explicit governance boundary: persistent memory must be queried, ranked, packaged, and governed before reinjection | open CI1-T10 with fresh GC-018 and full file-level corpus blocks |
| Immediate follow-up | `.private_reference/legacy/CVF_Important/ADDING_LEARNING PLANE/` | DEFER | direct Learning Plane files including memory architecture, evaluation, truth model, reputation model, failure analysis, adaptation policy | open CI1-T11 unless CI1-T10 proves the same value is already fully absorbed |
| Separate runtime tranche | Cortex/MCP-backed memory or adapter behavior | DEFER | current packet is source triage only; no live route or runtime integration proof | require a later runtime roadmap/work order if deep scan accepts implementation value |
| Strategic operator decision | external memory backend, MCP provider, public-facing memory claims | DEFER | may affect product boundary, cost, privacy, and public claims | do not implement from triage alone |
| Resolved by design | Graphify and code-review-graph as first scan families | ACCEPT_SUMMARY_ONLY | CI1-T2 and CI1-T3 already exist | keep as prior absorption evidence, not next target |
| Out of scope | public README/catalog claims | REJECT | this is private legacy absorption | route separately through public-sync only after accepted value becomes public-safe |

## Candidate Ranking

| Rank | Candidate folder | Files | Signals | Fit to current CVF planes | CI1-T9 decision |
|---|---:|---:|---|---|---|
| 1 | `.private_reference/legacy/CVF ADD/cortex-hub/` | 11 | memory, knowledge, MCP, code graph, learning, governance boundary | strongest bridge across Memory, Knowledge, Context Builder, and Learning Plane | CI1-T10 selected |
| 2 | `.private_reference/legacy/CVF_Important/ADDING_LEARNING PLANE/` | 14 | learning, memory architecture, failure analysis, evaluation, truth, reputation, policy | direct owner-surface match to Learning Plane foundation | CI1-T11 candidate |
| 3 | `.private_reference/legacy/CVF_Important/Knowledge Base_Palace/` | 11 | memory schema, adapter, evaluator, absorption spec | implementation-like memory substrate | queue after Learning Plane unless cortex-hub points here first |
| 4 | `.private_reference/legacy/CVF ADD/Agent Harnesses/` | 11 | artifact memory, execution memory, reinjection, context continuity | relevant to handoff, memory reinjection, execution receipts | queue after owner-surface scans |
| 5 | `.private_reference/legacy/CVF_Important/Knowledge Base_LLM-Powered/` | 6 | knowledge compilation and linting | useful for Knowledge Plane and retrieval durability | queue after memory/learning |
| 6 | `.private_reference/legacy/CVF ADD/Workflow GoClaw/` | 11 | learning loop, context profile, guardrail rulebook, workflow | overlaps Context Builder and workflow hardening | sample after memory/learning |
| 7 | `.private_reference/legacy/CVF_Important/ADDING_RAG ARCHITECTURE/` | 11 | memory sync, RAG orchestration, context bridge | useful but less central than memory/learning foundation | later CI1 scan |

## Full Root Triage Inventory

### CVF ADD

| Folder | Files | Initial signal | Triage disposition |
|---|---:|---|---|
| `AGENT ENGINEER` | 10 | agent engineering | DEFER |
| `Agent Harnesses` | 11 | memory, context, agent | DEFER |
| `AI-first vs Human-first` | 9 | feedback | DEFER |
| `caveman` | 11 | context, skill | DEFER |
| `CLI-Anything` | 11 | agent tooling | DEFER |
| `code-review-graph` | 7 | graph, context, knowledge | ACCEPT_SUMMARY_ONLY |
| `cortex-hub` | 11 | memory, knowledge, MCP, learning | ACCEPT |
| `deepagents` | 8 | context, agent | DEFER |
| `gridex` | 9 | skill, workflow | DEFER |
| `Hermes Agent` | 11 | memory, skill, agent | DEFER |
| `Hugging Face` | 11 | context, knowledge, skill | DEFER |
| `Human System Harness` | 11 | harness design | DEFER |
| `openrouter-cli.git` | 23 | provider CLI | DEFER |
| `REVIEW FOLDER` | 13 | context, knowledge | DEFER |
| `Workflow GoClaw` | 11 | learning, context, workflow | DEFER |

### CVF_Important

| Folder | Files | Initial signal | Triage disposition |
|---|---:|---|---|
| `ADDING_AGENT DEFINITION` | 9 | memory, agent | DEFER |
| `ADDING_AI Constitutional Layer` | 20 | plane, agent | DEFER |
| `ADDING_AI GATEWAY` | 12 | context, agent | DEFER |
| `ADDING_AUDIT AGENT LAYER` | 6 | memory, agent | DEFER |
| `ADDING_CONTEXT CONTROL` | 5 | context, agent | DEFER |
| `ADDING_CONTEXT ENGINE` | 6 | context | DEFER |
| `ADDING_CVF_Skill Formation Layer` | 6 | skill | DEFER |
| `ADDING_LEARNING PLANE` | 14 | memory, learning, plane, agent | ACCEPT |
| `ADDING_MINI_MODEL GATEWAY` | 7 | gateway | DEFER |
| `ADDING_MODEL GATEWAY` | 12 | feedback | DEFER |
| `ADDING_MODEL_ROUTER` | 6 | router | DEFER |
| `ADDING_Multi_Agent` | 10 | memory, agent | DEFER |
| `ADDING_RAG ARCHITECTURE` | 11 | memory, context, knowledge, RAG, agent | DEFER |
| `ADDING_Skill Creator` | 11 | skill, agent | DEFER |
| `ADDING_System Reality Layer` | 4 | system reality | DEFER |
| `ADDING_TRUST & ISOLATION LAYER` | 8 | agent safety/isolation | DEFER |
| `ADK SkillToolset` | 3 | knowledge, skill | DEFER |
| `Claude how to` | 10 | provider notes | DEFER |
| `HowtoClaude` | 6 | skill | DEFER |
| `Knowledge Base_Graphify` | 5 | memory, graph, knowledge | ACCEPT_SUMMARY_ONLY |
| `Knowledge Base_LLM-Powered` | 6 | context, knowledge | DEFER |
| `Knowledge Base_Palace` | 11 | memory, context, knowledge, palace | DEFER |
| `REVIEW FOLDER` | 35 | learning, context, RAG, plane, skill, agent | DEFER |
| `Windows_Skill_Normalization` | 7 | skill | DEFER |

## Adversarial Sampling Plan

CI1-T10 must not trust the folder title alone. The next deep scan must sample
both positive and negative paths:

- Positive sample: `CVF ADD/cortex-hub/Thong_tin.md`, because it explicitly maps
  persistent memory to CVF Knowledge Layer, Context Builder, MCP Bridge, Guard
  Engine, and Learning Plane while warning that memory is not truth.
- Positive sample: `CVF ADD/cortex-hub/CVF_KNOWLEDGE_MEMORY_ADAPTER_SPEC.md`,
  because adapter semantics may define owner-surface contract value.
- Positive sample: `CVF ADD/cortex-hub/CVF_SHARED_KNOWLEDGE_SYNC_POLICY.md`,
  because shared memory may create governance, privacy, and reinjection risks.
- Negative sample: any file that only describes third-party product capability
  without CVF-specific governance mapping must be rejected or summary-only.
- Cross-check sample: compare accepted cortex-hub memory claims against the
  current Learning Signal Intake Bridge and corpus intelligence standards before
  proposing runtime changes.

## Rescan Intelligence Hardening

- Original source artifact: `.private_reference/legacy/CVF ADD/` and
  `.private_reference/legacy/CVF_Important/`
- Predecessor intake artifact:
  `docs/audits/CVF_LHW_RESCAN_A_CVF_IMPORTANT_CORPUS_RECONCILIATION_2026-06-01.md`;
  `docs/audits/CVF_LHW_RESCAN_C_LEGACY_PARTIAL_ROOTS_CORPUS_RECONCILIATION_2026-06-01.md`;
  `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
- Delta ledger status: COMPLETE - includes UNCHANGED_FROM_INTAKE,
  CHANGED_DISPOSITION, NEW_FINDING, and REMOVED_OR_REJECTED categories in the
  original-intake delta below.
- Routing matrix status: COMPLETE - includes DO_NOW,
  SEPARATE_RUNTIME_TRANCHE, STRATEGIC_OPERATOR_DECISION, OUT_OF_SCOPE, and
  RESOLVED_BY_DESIGN lanes in the follow-up matrix below.
- Semantic sampling status: COMPLETE - includes sampleId, source section,
  source claim, disposition checked, adversarial challenge, and verdict columns
  in the sampling review below.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| sampleId | Delta category | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|---|
| CI1-T9-D1 | UNCHANGED_FROM_INTAKE | `legacy-cvf-important-broad` registry entry | CVF_Important remains broad partial scan | keep `PARTIALLY_SCANNED` | Does triage overclaim deep absorption? | PASS - status remains partial |
| CI1-T9-D2 | CHANGED_DISPOSITION | `legacy-cvf-add` next recommendation | code-review-graph should be next | replace with cortex-hub | Was code-review-graph already handled? | PASS - CI1-T3 exists, recommendation was stale |
| CI1-T9-D3 | NEW_FINDING | current root inventory | memory/learning clusters remain high-value | route cortex-hub and ADDING_LEARNING PLANE | Are these just keywords? | PASS for triage only; deep scan required |
| CI1-T9-D4 | REMOVED_OR_REJECTED | public/runtime claim path | public or runtime action from triage | reject from this packet | Could operator assume implementation is authorized? | PASS - public/runtime work is explicitly out of scope |

### Follow-Up Routing Matrix

| Route lane | Target | Disposition | Evidence | Next action |
|---|---|---|---|---|
| DO_NOW | CI1-T9 packet and registry refresh | ACCEPT | stale registry and fresh inventory | record triage |
| SEPARATE_RUNTIME_TRANCHE | memory/MCP adapter behavior | DEFER | runtime and provider surfaces require live proof | only after deep scan |
| STRATEGIC_OPERATOR_DECISION | external memory backend or public memory claims | DEFER | product, privacy, cost, and public boundary impact | operator decision later |
| OUT_OF_SCOPE | public-sync README/catalog changes | REJECT | private legacy source only | no public action |
| RESOLVED_BY_DESIGN | Graphify/code-review-graph as first scan families | ACCEPT_SUMMARY_ONLY | CI1-T2 and CI1-T3 prior evidence | keep as absorption context |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| CI1-T9-S1 | `CVF ADD/cortex-hub/Thong_tin.md` | persistent memory should feed Knowledge, Context, MCP, Guard, and Learning with governance | select for CI1-T10 | Is this just third-party feature marketing? | PASS - source text maps directly to CVF control surfaces |
| CI1-T9-S2 | `CVF_Important/ADDING_LEARNING PLANE/` file set | Learning Plane has memory, evaluation, truth, reputation, failure analysis, and adaptation components | queue after CI1-T10 | Is this already fully absorbed? | PASS_WITH_LIMIT - likely partial, requires delta scan |
| CI1-T9-S3 | `CVF_Important/Knowledge Base_Palace/` file set | memory schema and adapter may be implementation value | defer | Could this bypass current Learning Signal Intake Bridge? | PASS_WITH_LIMIT - must be reconciled before runtime work |

## Corpus Completeness And Report Integrity

- Corpus task class: TRIAGE_INVENTORY_AND_ROUTING
- Corpus root: `.private_reference/legacy/CVF ADD/`;
  `.private_reference/legacy/CVF_Important/`
- Source root(s): `.private_reference/legacy/CVF ADD/`;
  `.private_reference/legacy/CVF_Important/`
- Snapshot time: 2026-06-05 local workspace snapshot before packet creation
- Enumeration command: `rg --files --hidden --no-ignore '.private_reference/legacy/CVF ADD'`
  and `rg --files --hidden --no-ignore '.private_reference/legacy/CVF_Important'`
- Enumeration method: `rg --files --hidden --no-ignore` plus top-level
  `Get-ChildItem -Directory -Force`
- Manifest artifact or inline manifest: inline folder inventory and hash table
  in this packet
- Manifest hash: CVF ADD content manifest
  `deecf5e4fa7ae80f9ef717f5c5469c741f98d878936290c4f75681cd7d37a7a2`;
  CVF_Important content manifest
  `84c84f874a58e6bc501cb80ac3699acb9470d8ae9e3f11996a3995d5a05979f1`
- Processing ledger artifact or inline ledger: `Full Root Triage Inventory`
  tables above
- Allowed terminal statuses: READ_DEEP, READ_SHALLOW, SKIPPED_WITH_REASON,
  DEFERRED, BLOCKED_UNREADABLE
- Reconciliation: manifest=397 files across two roots; ledger_terminal=39 top-level folders routed; exclusions=deep file-level semantic reading is excluded from this triage packet by design; unresolved=0 for inventory scope
- Unresolved files: 0
- Declared exclusions: deep file-level semantic classification of all 397 files;
  this packet selects the next bounded deep scan instead
- Unreadable or unsupported files: none encountered during inventory
- Aggregation check: 167 CVF ADD files + 230 CVF_Important files = 397 total
  files; 15 CVF ADD folders + 24 CVF_Important folders = 39 routed folders
- Drift check: current working-tree inventory was computed on 2026-06-05 before
  packet creation; future deep scans must refresh file count and manifest hash
- Output traceability: each routed folder is listed with count, signal, and
  triage disposition in this packet
- Adversarial verification: sample plan above requires positive, negative, and
  cross-owner checks before accepting implementation value
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Knowledge System Reconciliation

- Knowledge task class: FOLDER_LEVEL_TRIAGE_MAP
- Source manifest: inline folder inventory plus current sorted path/content
  manifests for `.private_reference/legacy/CVF ADD/` and
  `.private_reference/legacy/CVF_Important/`
- Source manifest hash: CVF ADD
  `deecf5e4fa7ae80f9ef717f5c5469c741f98d878936290c4f75681cd7d37a7a2`;
  CVF_Important
  `84c84f874a58e6bc501cb80ac3699acb9470d8ae9e3f11996a3995d5a05979f1`
- Enumeration safety: PASS - used `rg --files --hidden --no-ignore` and
  filesystem-backed top-level directory enumeration
- Intake registry or ledger: `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
  plus the `Full Root Triage Inventory` tables above
- Authority assets: 397 files across 39 top-level folders under the two scoped
  legacy roots
- Derived views: folder counts, keyword signals, candidate ranking, and routing
  matrix in this packet
- Source authority vs derived view: legacy files remain source authority; this
  packet is a rebuildable derived routing view
- Mapped assets: 39 folders mapped to an owner-surface-oriented triage
  disposition
- Deferred assets: 397 file-level semantic reads deferred to bounded deep scan
  tranches
- Unmapped assets: 0 top-level folders in this triage scope
- Semantic region ledger: memory, knowledge, context, graph, learning, agent,
  workflow, RAG, skill, provider CLI
- Region reconciliation: assets=39; mapped=39; deferred=0; unmapped=0 for the folder-level triage map; file-level semantic detail is a declared deep-scan gap outside this map
- Orphan or unmapped assets: none
- Cross-region links: memory, knowledge, context, graph, learning, agent,
  workflow, RAG, skill, provider CLI
- Drift check: PASS
- Rebuildability check: PASS using the commands recorded in `Source Evidence`
- Retrieval boundary: this packet is not a retrieval-readiness claim and
  must not be used for direct cited answers
- Adversarial verification: PASS for triage layer; semantic correctness remains
  deferred to the selected deep scan
- Knowledge-map verdict: RECONCILED_WITH_DECLARED_GAPS

## Corpus Intelligence Classification

- Classification task class: TRIAGE_ROUTING
- Source corpus evidence: filesystem-backed root inventory and manifest hashes
  in `Source Evidence`
- Knowledge map evidence: folder-level triage inventory and candidate ranking in
  this packet
- Classification ledger: inline `Corpus Intelligence Classification Ledger`
  below
- Legal/policy corpus: NO
- Domain fields: N/A - legacy engineering and architecture corpus, not
  legal/policy authority
- Response Boundary: DIRECT_CITED_ANSWER is not allowed from this shallow triage; SUMMARY_WITH_SOURCE is allowed for this packet; PROCEDURAL_GUIDANCE is limited to the next-scan routing recorded here; ESCALATE_OR_ABSTAIN applies to runtime implementation or public claims
- Adversarial sampling plan: positive/negative/cross-owner plan recorded above
- Classification verdict: CLASSIFIED_STRUCTURAL_PASS_WITH_DEFERRED_DEEP_SCAN

### Corpus Intelligence Classification Ledger

| sourcePath | processingStatus | knowledgeRegion | ownerSurface | disposition | evidencePointer | answerClass |
|---|---|---|---|---|---|---|
| `.private_reference/legacy/CVF ADD/cortex-hub/` | READ_SHALLOW | MEMORY_KNOWLEDGE_LEARNING | Knowledge Layer; Memory; Learning Plane; Context Builder | ACCEPT | `Source Evidence`; `Candidate Ranking` rank 1 | SUMMARY_WITH_SOURCE |
| `.private_reference/legacy/CVF_Important/ADDING_LEARNING PLANE/` | READ_SHALLOW | LEARNING_PLANE | Learning Plane | ACCEPT | `Source Evidence`; `Candidate Ranking` rank 2 | SUMMARY_WITH_SOURCE |
| `.private_reference/legacy/CVF_Important/Knowledge Base_Palace/` | READ_SHALLOW | MEMORY_ARCHITECTURE | Memory; Knowledge Layer | DEFER | `Candidate Ranking` rank 3 | SUMMARY_WITH_SOURCE |
| `.private_reference/legacy/CVF ADD/Agent Harnesses/` | READ_SHALLOW | MEMORY_REINJECTION | Agent Handoff; Runtime Governance | DEFER | `Candidate Ranking` rank 4 | SUMMARY_WITH_SOURCE |
| `.private_reference/legacy/CVF_Important/Knowledge Base_LLM-Powered/` | READ_SHALLOW | KNOWLEDGE_OPERATIONS | Knowledge Layer | DEFER | `Candidate Ranking` rank 5 | SUMMARY_WITH_SOURCE |
| `.private_reference/legacy/CVF ADD/Workflow GoClaw/` | READ_SHALLOW | CONTEXT_LEARNING_WORKFLOW | Context Builder; Workflow Chain | DEFER | `Candidate Ranking` rank 6 | SUMMARY_WITH_SOURCE |
| `.private_reference/legacy/CVF_Important/ADDING_RAG ARCHITECTURE/` | READ_SHALLOW | RAG_CONTEXT_MEMORY | Knowledge Layer; Context Builder | DEFER | `Candidate Ranking` rank 7 | SUMMARY_WITH_SOURCE |
| `.private_reference/legacy/CVF ADD/code-review-graph/` | READ_SHALLOW | GRAPH_KNOWLEDGE_MODEL | Knowledge Layer; Graph Governance | ACCEPT_SUMMARY_ONLY | CI1-T3 prior absorption noted in `Original-Intake Delta Ledger` | SUMMARY_WITH_SOURCE |

## Findings

| Finding | Severity | Evidence | Disposition | Follow-up |
|---|---|---|---|---|
| T9-F1 stale ADD next recommendation | Moderate | registry still pointed `legacy-cvf-add` at code-review-graph after CI1-T3 | ACCEPT | refresh recommendation to cortex-hub deep scan |
| T9-F2 memory/learning blind spot remains in partial roots | High | cortex-hub, ADDING_LEARNING PLANE, Knowledge Base_Palace, Agent Harnesses all contain memory or learning signals | DEFER | open CI1-T10 and CI1-T11 sequence |
| T9-F3 broad scan cannot prove semantic absorption | High | LHW broad scans route folders but do not normalize file-level dispositions | DEFER | require fresh GC-018 and file-level ledger for each chosen folder |
| T9-F4 runtime/public overclaim risk | Moderate | several candidates mention MCP, adapters, memory, provider CLI, or shared knowledge | REJECT | do not implement or public-claim from triage alone |
| T9-F5 scan-hardening layer should be reusable | Moderate | this packet applies delta ledger, routing matrix, and adversarial sampling to legacy roots | ACCEPT | use this pattern for future partial-root scans |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
|---|---|---|---|---|
| T9-F1 | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | registry stale-next-scan detection should be considered for future corpus registry guard work |
| T9-F2 | RULE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | require memory/learning-first audit when partial legacy roots contain multiple owner-surface candidates |
| T9-F3 | RULE_EXISTS | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | GC-047/048/050 already require file-level evidence before deep absorption claims |
| T9-F4 | OPERATOR_SCOPE_CLARITY_GAP | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | runtime/public boundaries already require separate live proof and public-sync routing |
| T9-F5 | RULE_GAP | GOVERNANCE_CONTROL_PLANE | TEMPLATE_UPDATED | this packet becomes the working pattern for rescan plus delta plus routing plus adversarial sampling |

Runtime/provider/cost learning lane: N/A_WITH_REASON for
RUNTIME_BEHAVIOR_LEARNING, PROVIDER_OUTPUT_LEARNING, and
COST_ECONOMICS_LEARNING because CI1-T9 does not execute a provider, runtime
route, MCP adapter, cost path, or live governance behavior. Those lanes become
applicable only after a deep scan accepts runtime implementation value and a
separate runtime tranche is authorized.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this packet reads `.private_reference/legacy/` source material and
selects private-provenance deep scan candidates. No public-sync artifact,
public README/catalog claim, public setup claim, runtime proof, or live
governance proof is created here.

Next public action: N/A until a later accepted value is converted into a
public-safe artifact in the public-sync clone with explicit export evidence.

## Claim Boundary

CI1-T9 proves that the two selected partial legacy roots were freshly
inventoried, routed, and prioritized under the upgraded scan hardening pattern.
It does not prove deep semantic correctness for every file, runtime integration,
MCP/provider behavior, public readiness, legal/policy authority, or live CVF
governance behavior.

Next selected tranche: CI1-T10 deep scan of
`.private_reference/legacy/CVF ADD/cortex-hub/`, with fresh GC-018, file-level
hash ledger, original-intake delta ledger, follow-up routing matrix, and
adversarial sampling.
