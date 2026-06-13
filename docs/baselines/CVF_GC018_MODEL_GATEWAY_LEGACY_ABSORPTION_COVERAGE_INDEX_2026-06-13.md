# CVF GC-018 Model Gateway Legacy Absorption Coverage Index - 2026-06-13

Memory class: POINTER_RECORD

Status: DISPATCH_READY

Owner: Codex Orchestrator

Worker target: Claude

Commit mode: WORKER_MUST_NOT_COMMIT

rawMemoryReleased=false

Base head: 86d9e46d

dispatchBaseHead: `86d9e46d`

executionBaseHead: `86d9e46d`

closureBaseHead: `86d9e46d`

## Purpose

Authorize a bounded worker pass to resolve the active Model Gateway legacy
absorption hold and seed the broader CVF plane/workflow-chain legacy coverage
index.

The first priority is `MGW-001` in:

`docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md`

The worker must compare prior LHW17 Model Gateway advisory evidence, current
gateway-family legacy path inventory, and current Model Gateway / EPF owner
surfaces before C-02 planning can resume.

The second priority is coverage-index discipline: record the initial Memory /
Knowledge / Scan layer recheck rows without broad legacy content reading.

## Decision Baseline

Dispatch the bounded `MGW-001` legacy absorption coverage recheck to Claude.
The worker may read gateway-family legacy content inside the named scope,
update the legacy absorption coverage index, and create a recheck plan plus
worker-return packet. The worker must not implement Model Gateway, resume C-02,
call providers, mutate runtime/source/test files, or claim readiness.

## Scope / Target / Owner Boundary

In scope:

- bounded Model Gateway legacy absorption recheck for gateway-related legacy
  families under `.private_reference/legacy/CVF_Important/`;
- coverage-index updates for `MGW-001`, `MEM-001`, `SCAN-001`, `FPC-001`,
  `AOT-001`, and `SLI-001` when evidence supports a change;
- comparison against prior LHW17 T2 Model Gateway advisory evidence;
- comparison against current `EXTENSIONS/CVF_MODEL_GATEWAY/src/` and
  `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/` owner surfaces;
- worker-return packet with claim boundary and duplicate-prevention ledger.

Out of scope:

- runtime/source/test mutation;
- provider/API or live proof;
- public-sync;
- package install;
- registry mutation outside the index file named above;
- external Document Translator, Policy_Local, OCR, retrieval, EC, Redis, DEP2,
  or T12 work;
- broad memory/scan legacy content re-reading beyond governed evidence review
  and path-level recheck.

## Source Authority Table

| Source | Authority use | Disposition |
| --- | --- | --- |
| `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` | Coverage index to update | ACCEPT |
| `docs/reviews/CVF_MODEL_GATEWAY_LEGACY_ABSORPTION_GAP_DISPATCH_CORRECTION_2026-06-13.md` | Active C-02 hold and gateway-family gap | ACCEPT |
| `docs/reference/archive/CVF_LHW17_T2_MODEL_GATEWAY_UNIFICATION_ADVISORY_CONNECTOR_SPEC_2026-05-30.md` | Prior Model Gateway legacy advisory | ACCEPT |
| `docs/baselines/archive/CVF_GC018_LHW17_CVF_IMPORTANT_ABSORPTION_WAVE_2026-05-30.md` | Prior LHW17 legacy scan block and source list | ACCEPT |
| `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md` | Required blind-spot control | ACCEPT |
| `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` | Registry and prior absorption lookup rules | ACCEPT |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | Human lookup for scan/memory corpus evidence | ACCEPT |
| `docs/audits/CVF_MEMORY_METHOD_LEGACY_RESCAN_AUDIT_2026-06-01.md` | Memory/knowledge method recheck boundary | ACCEPT |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS: current active next move is legacy absorption before C-02 resumes | `CVF_SESSION_MEMORY.md` | `## Latest Continuity Note` | `fresh GC-018 for bounded Model Gateway legacy absorption` | active session front door | ACCEPT |
| EXISTS: C-02 planning dispatch is held | `docs/reviews/CVF_MODEL_GATEWAY_LEGACY_ABSORPTION_GAP_DISPATCH_CORRECTION_2026-06-13.md` | `## Corrective Decision` | `HOLD_PENDING_LEGACY_ABSORPTION` | C-02 correction review | ACCEPT |
| EXISTS: LHW17 T2 Model Gateway advisory is prior evidence | `docs/reference/archive/CVF_LHW17_T2_MODEL_GATEWAY_UNIFICATION_ADVISORY_CONNECTOR_SPEC_2026-05-30.md` | header and `## Source` | `cvf.modelGatewayUnificationAdvisory.lhw17.t2.v1` | LHW17 T2 connector spec | ACCEPT |
| EXISTS: LHW17 baseline listed gateway-related legacy folders | `docs/baselines/archive/CVF_GC018_LHW17_CVF_IMPORTANT_ABSORPTION_WAVE_2026-05-30.md` | `## Legacy Spec Scan Block` | `ADDING_MODEL GATEWAY`; `ADDING_MODEL_ROUTER`; `ADDING_MINI_MODEL GATEWAY`; `ADDING_AI GATEWAY` | LHW17 baseline | ACCEPT |
| EXISTS: blind-spot standard requires control block for legacy scoping | `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md` | `## Mandatory Blind-Spot Control Block` | `Knowledge Absorption Blind-Spot Control Block` | knowledge absorption standard | ACCEPT |
| EXISTS: corpus registry standard has prior absorption lookup field | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` | `## Required Registry Entry Fields` | `priorAbsorption` | corpus scan registry standard | ACCEPT |
| EXISTS: memory method legacy rescan is partial | `docs/audits/CVF_MEMORY_METHOD_LEGACY_RESCAN_AUDIT_2026-06-01.md` | header | `PARTIAL_MEMORY_METHOD_RESCAN` | memory method audit | ACCEPT |
| EXISTS_PATH_ONLY: Model Gateway legacy family exists | `.private_reference/legacy/CVF_Important/ADDING_MODEL GATEWAY/` | path inventory | `ADDING_MODEL GATEWAY` | legacy path inventory | ACCEPT |
| EXISTS_PATH_ONLY: Model Router legacy family exists | `.private_reference/legacy/CVF_Important/ADDING_MODEL_ROUTER/` | path inventory | `ADDING_MODEL_ROUTER` | legacy path inventory | ACCEPT |
| EXISTS_PATH_ONLY: Mini Model Gateway legacy family exists | `.private_reference/legacy/CVF_Important/ADDING_MINI_MODEL GATEWAY/` | path inventory | `ADDING_MINI_MODEL GATEWAY` | legacy path inventory | ACCEPT |
| EXISTS_PATH_ONLY: AI Gateway legacy family exists | `.private_reference/legacy/CVF_Important/ADDING_AI GATEWAY/` | path inventory | `ADDING_AI GATEWAY` | legacy path inventory | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Runtime authority |
| --- | --- | --- |
| `Legacy Absorption Coverage Index` | Tracks plane/workflow-chain legacy coverage | DOC_ONLY_NEW |
| `Coverage status` | Uses bounded status vocabulary to prevent false complete claims | DOC_ONLY_NEW |
| `Duplicate prevention key` | Links accepted legacy value to owner surface and prior evidence | DOC_ONLY_NEW |
| `MGW-001` | Index row for Model Gateway legacy coverage | DOC_ONLY_NEW |

## Roadmap-To-Work-Order Trace Matrix

| Source requirement | Source | Dispatch handling | Status |
| --- | --- | --- | --- |
| C-02 planning is held until legacy absorption evidence exists | C-02 correction review | Dispatch bounded Model Gateway legacy absorption recheck | SATISFIED_FOR_DISPATCH |
| Avoid duplicate legacy absorption | Corpus registry standard and operator instruction | Create index with duplicate prevention keys and prior evidence rows | SATISFIED_FOR_DISPATCH |
| Recheck scan/memory layer without over-broad latency | Operator instruction and memory method audit boundary | Worker must reconcile registry/evidence first and avoid broad memory/scan content reread | SATISFIED_FOR_DISPATCH |
| Keep foundation-plane work ahead of use cases | FPC roadmap and active session state | Work order excludes Policy_Local, Document Translator, provider/live proof, runtime mutation, and public-sync | SATISFIED_FOR_DISPATCH |

## Knowledge Absorption Blind-Spot Control Block

- Standard read:
  `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md`
- Source inventory:
  - `.private_reference/legacy/CVF_Important/ADDING_MODEL GATEWAY/`
  - `.private_reference/legacy/CVF_Important/ADDING_MODEL_ROUTER/`
  - `.private_reference/legacy/CVF_Important/ADDING_MINI_MODEL GATEWAY/`
  - `.private_reference/legacy/CVF_Important/ADDING_AI GATEWAY/`
- Prior absorption evidence resolved:
  - LHW17 T2 Model Gateway advisory exists and must be reconciled.
  - C-02 correction found active planning omitted this reconciliation.
- Detailed source files authorized:
  - gateway-related legacy files under the four gateway-family paths above;
  - prior LHW17 T2 advisory and completion evidence;
  - current governed Model Gateway / EPF owner surfaces.
- Source families skipped:
  - broad memory/scan legacy families, except governed registry/audit evidence
    and path-level checks needed to update the index.
- File-level accepted value:
  - worker must provide accept/defer/reject rows; none accepted by this
    dispatch alone.
- Owner-surface normalization:
  - worker must map any accepted gateway value to current `EXTENSIONS` owner
    surfaces or defer it to a later planning/implementation tranche.
- Accept/defer/reject matrix:
  - `MGW-001`: DO_NOW in this worker pass.
  - `MEM-001` and `SCAN-001`: RECONCILE_EVIDENCE_ONLY unless a separate fresh
    GC-018 authorizes deeper content reading.
  - runtime/provider/live/public claims: REJECT_DIRECT.
- Adversarial roles required:
  - Implementer: identify what must change in C-02 planning.
  - Skeptic/Auditor: challenge whether prior LHW17 T2 already covers the item
    or whether new files require recheck.
  - Product/Operator Advocate: prevent broad slow gates and preserve foundation
    value.
  - Safety/Boundary Owner: prevent provider/runtime/public overclaim.
- Thin proof target:
  - updated index row plus worker return with source-verified evidence.
- Blind-spot verdict:
  - READY_FOR_BOUNDED_RECHECK

## Rescan Intelligence Hardening

- Original source artifact: active C-02 hold correction plus path-level
  gateway-family legacy inventory.
- Predecessor intake artifact:
  `docs/reviews/CVF_MODEL_GATEWAY_LEGACY_ABSORPTION_GAP_DISPATCH_CORRECTION_2026-06-13.md`
- Delta ledger status: CHANGED_DISPOSITION because C-02 changes from held
  correction to a bounded recheck dispatch.
- Routing matrix status: DO_NOW for `MGW-001`; STRATEGIC_OPERATOR_DECISION for
  any future broad scan/memory legacy reread; SEPARATE_RUNTIME_TRANCHE for any
  runtime/provider work; OUT_OF_SCOPE for implementation; RESOLVED_BY_DESIGN
  for prior LHW17 evidence reuse.
- Semantic sampling status: PARTIAL for gateway-family files
  only.
- Rescan intelligence verdict: PARTIAL

### Original-Intake Delta Ledger

| Current finding | Predecessor finding | New disposition | Reason |
| --- | --- | --- | --- |
| `MGW-001` needs bounded legacy recheck | C-02 dispatch omitted gateway-family legacy inventory | CHANGED_DISPOSITION | This GC-018 authorizes a bounded worker recheck rather than leaving the hold as documentation only |
| Prior LHW17 T2 advisory exists | LHW17 T2 already absorbed Model Gateway advisory content | UNCHANGED_FROM_INTAKE | Worker must reconcile prior value before accepting new value |
| Extra gateway-family files may exist beyond prior LHW17 T2 source list | Path inventory found gateway-family roots and operator opened `CVF_ARCHITECTURE.md` | NEW_FINDING | Worker must inventory and disposition allowed gateway files |
| No prior current-source evidence is rejected | Current Model Gateway source surfaces remain valid | REMOVED_OR_REJECTED | N/A with reason: no current-source evidence is removed by this dispatch |

### Follow-Up Routing Matrix

| Item | Route | Reason |
| --- | --- | --- |
| `MGW-001` bounded recheck | DO_NOW | Active C-02 hold requires legacy coverage decision |
| Broad memory/scan legacy reread | STRATEGIC_OPERATOR_DECISION | Operator concern is valid, but broad content reread needs separate authorization |
| Runtime/provider implementation | SEPARATE_RUNTIME_TRANCHE | This work order is documentation/index only |
| Model Gateway implementation | OUT_OF_SCOPE | C-02 itself is still planning-only and held |
| Prior LHW17 T2 evidence | RESOLVED_BY_DESIGN | Reuse and reconcile prior advisory evidence before duplicating absorption |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| MG-LACI-001 | C-02 correction | gateway-family legacy sources were omitted from C-02 dispatch | DO_NOW | Does this justify broad legacy reread? | READY_FOR_BOUNDED_RECHECK only for gateway scope |
| MG-LACI-002 | LHW17 T2 advisory | Model Gateway advisory already exists | RESOLVED_BY_DESIGN | Is new work duplicative? | Worker must reconcile prior evidence first |

## Evidence / Verification

Dispatch verification before commit:

| Gate | Command | Expected result |
| --- | --- | --- |
| Dispatch quality | `python governance/compat/check_work_order_dispatch_quality.py --base 86d9e46d --head HEAD --enforce` | PASS |
| Pre-dispatch autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 86d9e46d --head HEAD` | PASS |
| Reviewer-fast | `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` | PASS |
| Diff hygiene | `git diff --check` | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance dispatch. Public-sync is not authorized.

## Claim Boundary

This baseline authorizes a worker to perform bounded legacy absorption recheck
for Model Gateway and to update a coverage index. It does not authorize runtime
mutation, source/test mutation, provider/API use, live proof, public-sync,
production readiness, public readiness, cost/quality claims, or broad legacy
absorption outside the named scope.
