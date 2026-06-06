# CVF Memory Method Legacy Rescan Audit

Memory class: FULL_RECORD

Status: PARTIAL_MEMORY_METHOD_RESCAN

docType: audit

Date: 2026-06-01

## Purpose

Reopen the Legacy corpus specifically for Memory and knowledge-storage method
discovery before GC-048 is designed. This audit tests the hypothesis that
`.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/` is one useful
storage and retrieval technique, but not the complete CVF Memory method.

The result is a bounded method map. It is not a claim that every Legacy file
has been semantically read or absorbed.

## Scope / Claim Boundary

Scope:

- enumerate the full `.private_reference/legacy/` filesystem from source truth;
- identify broad Memory, graph, knowledge, retrieval, context, sync, drift,
  compilation, provenance, and reinjection candidate regions;
- read representative high-signal source families;
- compare those families with current CVF owner surfaces;
- record the design boundary that must be resolved before GC-048.

Boundary:

- no runtime implementation is authorized by this audit;
- no autonomous memory mutation, provider prompt mutation, or public-sync is
  authorized;
- filename and keyword discovery route later reading but do not prove semantic
  understanding;
- a file-level terminal processing ledger remains required before any complete
  Legacy absorption claim.

## Filesystem Evidence

Authoritative enumeration command:

```powershell
$roots = Get-ChildItem ".private_reference/legacy" -Directory | Sort-Object Name
$rows = foreach ($root in $roots) {
  $files = Get-ChildItem $root.FullName -Recurse -File
  [pscustomobject]@{
    Root = $root.Name
    Files = $files.Count
    Markdown = ($files | Where-Object Extension -eq ".md").Count
    Other = ($files | Where-Object Extension -ne ".md").Count
  }
}
$rows | Format-Table -AutoSize
```

| Legacy root | Files | Markdown | Other |
| --- | ---: | ---: | ---: |
| `App onboarding` | 10 | 0 | 10 |
| `CVF 16.5` | 100 | 78 | 22 |
| `CVF 17.05` | 31 | 31 | 0 |
| `CVF 25.05` | 2 | 2 | 0 |
| `CVF 28.05` | 5 | 3 | 2 |
| `CVF ADD` | 167 | 137 | 30 |
| `CVF Edit` | 10 | 9 | 1 |
| `CVF_Important` | 230 | 218 | 12 |
| `CVF_Restructure` | 74 | 74 | 0 |
| **Total** | **629** | **552** | **77** |

## Discovery Evidence

The discovery pass used both filename and content routing signals:

```powershell
rg --files ".private_reference/legacy" | Measure-Object
# 315

rg --files --hidden --no-ignore ".private_reference/legacy" | Measure-Object
# 629

$pattern = "memory|graph|knowledge|context|retriev|rag|vector|semantic|episodic|working memory|long.term|sync|consolidat|decay|palace|compile|provenance|citation|drift|orphan"
rg -l --hidden --no-ignore -i $pattern ".private_reference/legacy" -g "*.md" |
  Measure-Object
# 474

Get-ChildItem ".private_reference/legacy" -Recurse -File |
  Where-Object {
    $_.Name -match "(?i)memory|graph|knowledge|context|retriev|rag|semantic|palace|compile|sync|decay|drift|citation|vector"
  } |
  Measure-Object
# 92
```

Finding: default `rg --files` is not an authoritative corpus enumerator in this
workspace because ignore rules reduce visibility from `629` to `315` files.
Corpus work must use filesystem enumeration or an explicit ignore-safe
equivalent such as `rg --files --hidden --no-ignore`.

## Memory Method Source-Family Map

| Method layer | High-signal Legacy family | Representative sources | Reconciled value |
| --- | --- | --- | --- |
| Source-of-truth intake | `CVF 16.5/tolaria/` | `CVF_KNOWLEDGE_VAULT_INTAKE.md`, `CVF_KNOWLEDGE_PROVENANCE_RECEIPT.md`, `CVF_KNOWLEDGE_DRIFT_SIGNAL.md` | Original assets remain inputs; governed registry and receipts become authority; derived views must be rebuildable. |
| Controlled memory gateway | `CVF 16.5/agentmemory/` | `CVF_CONTROLLED_MEMORY_GATEWAY.md`, `CVF_MEMORY_ACCESS_POLICY.md`, `CVF_MEMORY_PRIVACY_FILTER_POLICY.md`, `CVF_MEMORY_REINJECTION_PROTOCOL.md` | Memory capture, retrieval, lifecycle, privacy, and reinjection must pass policy gates and issue receipts. |
| Memory lifecycle | `CVF_Important/ADDING_LEARNING PLANE/` | `CVF_MEMORY_ARCHITECTURE.md` | Working, episodic, semantic, and procedural memory require consolidation, decay, confidence, and quality control. |
| Retrieval routing and fusion | `CVF_Important/ADDING_RAG ARCHITECTURE/` | `AI_KNOWLEDGE_LAYER_MODEL.md`, `AI_KNOWLEDGE_ROUTER_SPEC.md`, `AI_CONTEXT_FUSION_ENGINE.md`, `AI_MEMORY_SYNC_PROTOCOL.md` | Retrieval, Memory, and Knowledge Graph are distinct capabilities routed through a Knowledge Layer and fused into bounded context. |
| Structural graph index | `CVF_Important/Knowledge Base_Graphify/`, `CVF ADD/code-review-graph/` | `CVF_GRAPH_MEMORY_DATA_MODEL.md`, `CVF_GRAPH_MEMORY_LAYER_SPEC.md`, `CVF_GRAPH_KNOWLEDGE_SPEC.md`, `CVF_GRAPH_CONTEXT_RESOLUTION_SPEC.md` | Graphify supplies structural and semantic relations, provenance, impact analysis, and graph-informed context resolution. It is a supporting index, not the entire Memory system. |
| Compiled knowledge artifacts | `CVF_Important/Knowledge Base_LLM-Powered/` | `CVF_KNOWLEDGE_COMPILATION_POLICY.md`, `CVF_COMPILED_CONTEXT_POLICY.md`, `CVF_KNOWLEDGE_LINT_ENGINE_SPEC.md` | Derived context artifacts should be compiled, linted, traceable, maintainable, and refactorable. |
| Hierarchical placement | `CVF_Important/Knowledge Base_Palace/` | `CVF_MEMPALACE_ABSORPTION_SPEC.md`, `cvf_mem_context_mapper.py`, `cvf_memory_evaluator.py` | Palace vocabulary adds hierarchical routing and evidence-preserving placement; it must not become a parallel runtime or replace canonical evidence. |
| Context continuity and learning | `CVF ADD/caveman/`, `CVF ADD/Workflow GoClaw/`, `CVF ADD/Agent Harnesses/`, `CVF_Important/ADDING_AUDIT AGENT LAYER/`, `CVF_Important/ADDING_Multi_Agent/` | `CVF_CONTEXT_COMPACTION_PROTOCOL.md`, `CVF_CONTEXT_PACKAGING_POLICY.md`, `CVF_ARTIFACT_MEMORY_MODEL.md`, `CVF_AUDIT_MEMORY_LOOP.md`, `CVF_PLANNER_MEMORY_LOOP.md` | Context budgets, compaction, profile learning, artifact promotion, audit feedback, and offline planner updates complete the method boundary. |

## Current CVF Owner-Surface Reconciliation

| Method area | Current owner surface | Disposition |
| --- | --- | --- |
| Governed vault intake, derived graph, snapshot packaging, drift, reinjection proposal, tool-call guard | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/knowledge.vault.intake.contract.ts` | `LANDED_BOUNDED` |
| Palace hierarchy record | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/w7.memory.record.contract.ts` | `LANDED_BOUNDED` |
| Controlled capture, retrieval, privacy filter, lifecycle access, reinjection packaging | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled.memory.gateway.contract.ts`, `controlled-memory-gateway.ts` | `LANDED_BOUNDED` |
| Tier classification | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-tier-classifier.contract.ts` | `LANDED_CONTRACT_ONLY` |
| Durable summary-only persistence | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | `LANDED_BOUNDED` |
| Runtime hierarchy and task memory | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts`, `task-memory/` | `LANDED_BOUNDED` |
| Memory lifecycle, retrieval ranking, context packaging, event hooks | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-lifecycle-policy.ts`, `memory-retrieval-policy.ts`, `memory-context-packager.ts`, `memory-event-hooks.ts` | `LANDED_BOUNDED` |
| TypeScript AST graph, symbol index, optional SQLite graph store, graph authority gate | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/` | `LANDED_STRUCTURAL_GRAPH` |
| Structural index, compiled artifacts, context assembly, maintenance, refactor proposals | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/knowledge.*.contract.ts` | `LANDED_BOUNDED` |
| Learning signal intake and advisory adaptation policy | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts`, `adaptation-policy-engine.ts` | `LANDED_ADVISORY_ONLY` |

## Priority Findings

### F1 - Graphify is necessary but insufficient

`Knowledge Base_Graphify` describes a valuable graph index and context
resolution technique. It does not replace governed source intake, memory
lifecycle, retrieval routing, fusion, compilation, hierarchical placement,
context budgets, drift detection, or learning disposition.

### F2 - CVF already contains many method fragments

Current CVF owner surfaces have absorbed substantial Legacy value. The gap is
not an empty implementation surface. The gap is the absence of one canonical
CVF Memory Method that defines how the fragments compose and which artifacts
are authoritative versus derived.

### F3 - Corpus-to-memory reconciliation is missing

GC-047 proves corpus evidence discipline, but current graph and Memory owner
surfaces do not yet prove:

- which manifest files were ingested, deferred, skipped, or unreadable;
- which files became registry assets, graph nodes, compiled artifacts, or
  retrieval candidates;
- which assets yielded no extractable signal;
- whether the derived map is stale after corpus drift;
- whether graph, Palace, compilation, and retrieval views reconcile back to
  the same governed source manifest.

### F4 - Ignore-sensitive enumeration is a general control-plane risk

Default `rg --files` omitted `314` visible Legacy files in this workspace.
Any future corpus guard that accepts ignore-sensitive enumeration without an
explicit declaration can reproduce the original blind spot.

## Proposed CVF-Native Memory Method

The Legacy sources support a CVF-native method with this bounded flow:

```text
filesystem-backed corpus manifest
  -> governed intake registry + provenance receipts
  -> memory lifecycle classification and policy filters
  -> derived structural graph + semantic region map + compiled artifacts
  -> retrieval router
  -> deterministic context fusion and token-bounded snapshot
  -> governed use, drift signals, audit receipts, and learning disposition
  -> reviewed maintenance or reinjection proposal
```

Authority rule:

```text
source asset + governed registry + receipts = authority
graph, Palace, compiled context, cache, and snapshot = derived rebuildable views
```

This method preserves the useful parts of Graphify, Palace, LLM-powered
compilation, Tolaria, agentmemory, RAG architecture, and context continuity
without creating a parallel runtime or authorizing autonomous mutation.

## GC-048 Design Implication

GC-048 should not be designed as a graph-only enhancement. Its bounded design
target should be a `Corpus-To-Memory-Map Reconciliation And Semantic Region
Guard`.

Before any GC-048 implementation is dispatched, a fresh GC-018 packet must:

1. define the canonical CVF Memory Method owner document;
2. define the manifest-to-registry-to-derived-view reconciliation ledger;
3. define semantic region classification without claiming deep understanding;
4. distinguish authoritative assets from rebuildable derived views;
5. require drift detection and stale-map disposition;
6. forbid ignore-sensitive enumeration defaults unless declared and bounded;
7. preserve `autonomousMutationAuthorized=false`;
8. retain the existing LHW-RESCAN-A requirement for file-level terminal
   coverage before any complete Legacy absorption claim.

## Owner / Source

Owner: CVF governance and Learning Plane design surface.

Primary source: filesystem-backed enumeration of `.private_reference/legacy/`
plus the representative Legacy families named in `Memory Method Source-Family
Map`.

Current implementation comparison sources:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/knowledge.vault.intake.contract.ts`
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/w7.memory.record.contract.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled.memory.gateway.contract.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-tier-classifier.contract.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/`

## Protocol / Contract / Requirements

Before GC-048 implementation, use filesystem-backed enumeration, preserve all
visible file formats, keep an explicit terminal ledger, trace important method
claims to Legacy sources and current owner surfaces, and retain the honest
`PARTIAL` verdict until every file-level disposition reconciles.

## Enforcement / Verification

Verification commands for this audit:

```powershell
python governance/compat/check_corpus_completeness_report_integrity.py --base <baseHead> --head HEAD --enforce
python governance/compat/check_finding_to_governance_learning.py --base <baseHead> --head HEAD --enforce
python governance/compat/run_local_governance_hook_chain.py --hook pre-commit --parallel
```

GC-048 prerequisite work must promote the ignore-safe enumeration requirement
into the earliest applicable corpus phase gate before any complete claim.

## Corpus Completeness And Report Integrity

- Corpus task class: `KNOWLEDGE_ABSORPTION`
- Corpus root: `.private_reference/legacy/`
- Snapshot time: `2026-06-01`
- Enumeration command: filesystem-backed `Get-ChildItem ".private_reference/legacy" -Directory` plus recursive `Get-ChildItem $root.FullName -Recurse -File`; see `Filesystem Evidence`
- Manifest artifact or inline manifest: root-level inline manifest in `Filesystem Evidence`; full file-level manifest remains required for LHW-RESCAN-A
- Manifest hash: `N/A with reason: this is a bounded routing audit; GC-048 prerequisite work must create a file-level manifest artifact and stable hash`
- Processing ledger artifact or inline ledger: family-level high-signal routing ledger in `Memory Method Source-Family Map`; full file-level terminal ledger remains open
- Allowed terminal statuses: `READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE`
- Reconciliation: `manifest=629; ledger_terminal=0; exclusions=0; unresolved=629`
- Unresolved files: `629 file-level terminal statuses remain to be reconciled by LHW-RESCAN-A/B/C; 92 filename candidates and 474 Markdown content candidates were routed, not terminal-ledgered`
- Declared exclusions: `none`
- Unreadable or unsupported files: `77 non-Markdown files remain visible; format-specific processing is not claimed by this audit`
- Aggregation check: `PASS for root-level filesystem totals: 552 Markdown + 77 other = 629 files`
- Drift check: `PASS at publication: enumeration rerun returned 629 files`
- Output traceability: source-family table names representative Legacy files and current CVF owner surfaces
- Adversarial verification: default `rg --files` count independently compared with filesystem and ignore-safe enumeration: `315 != 629`, while `rg --files --hidden --no-ignore = 629`
- Corpus verdict: PARTIAL

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| Graphify alone is not a complete Memory method | `RULE_GAP` | `GOVERNANCE_CONTROL_PLANE` | `DESIGN_REVIEW_REQUIRED` | Require a canonical CVF Memory Method owner document before GC-048 implementation. |
| Memory fragments exist without manifest-to-view reconciliation | `ORCHESTRATOR_PACKET_GAP` | `RUNTIME_BEHAVIOR_LEARNING` | `MACHINE_CHECK_CANDIDATE` | Design GC-048 around corpus-to-memory-map reconciliation and stale-map detection. |
| Default `rg --files` omitted 314 Legacy files | `MACHINE_GATE_GAP` | `GOVERNANCE_CONTROL_PLANE` | `MACHINE_CHECK_CANDIDATE` | Upgrade corpus enumeration rules to require filesystem listing or explicit ignore-safe enumeration. |
| This audit does not terminal-ledger every Legacy file | `OPERATOR_SCOPE_CLARITY_GAP` | `DOCUMENTATION_ONLY_LEARNING` | `N/A_WITH_REASON`: honest PARTIAL verdict retained | Execute LHW-RESCAN-A/B/C before any complete absorption claim. |
| Runtime/provider/cost behavior | `RUNTIME_SIGNAL_GAP` | `RUNTIME_BEHAVIOR_LEARNING` | `N/A_WITH_REASON`: this audit performs source analysis only | No runtime, provider, or cost control mutation in this batch. |

## Public Export Disposition

`DEFERRED_PRIVATE_ONLY`

Reason: this is a private provenance audit of Legacy material. No matching
public artifact or public-sync claim is authorized.

## Claim Boundary

This audit is a source-analysis and design-routing artifact. It does not prove
complete Legacy semantic absorption, runtime behavior, provider behavior,
production readiness, public readiness, or autonomous Memory mutation safety.

## Related Artifacts

- `docs/audits/CVF_LEGACY_SCAN_COMPLETENESS_FAILURE_AUDIT_2026-06-01.md`
- `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md`
- `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md`
- `.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/CVF_GRAPH_MEMORY_DATA_MODEL.md`
- `.private_reference/legacy/CVF_Important/ADDING_RAG ARCHITECTURE/AI_KNOWLEDGE_LAYER_MODEL.md`
- `.private_reference/legacy/CVF 16.5/agentmemory/CVF_CONTROLLED_MEMORY_GATEWAY.md`
- `.private_reference/legacy/CVF 16.5/tolaria/CVF_KNOWLEDGE_VAULT_INTAKE.md`
