# CVF Legacy Scope Absorption Audit Matrix

Memory class: FULL_RECORD
Status: INITIAL CROSS-SCOPE LEGACY ABSORPTION MATRIX

## Purpose

Record the bounded 2026-05-18 legacy absorption audit for the four operator-approved
source scopes:

- `.private_reference/legacy/CVF 16.5`
- `.private_reference/legacy/CVF 17.05`
- `.private_reference/legacy/CVF ADD`
- `.private_reference/legacy/CVF Edit`

The purpose is not to import external repositories into CVF. The purpose is to
classify which knowledge has been absorbed, which knowledge remains only
partially absorbed, and which knowledge must stay deferred until a fresh
GC-018-backed implementation tranche names the consuming runtime slice.

## Reviewed Source

Inventory snapshot:

| Scope | Reviewed source count | Main source role |
|---|---:|---|
| CVF 16.5 | 100 files across 12 source folders | external repo knowledge summaries and absorption proposals |
| CVF 17.05 | 31 files across external capability intake and review folder | converged remediation roadmap and capability intake packet |
| CVF ADD | 167 files across 15 source folders | doctrine and runtime-pattern absorption studies |
| CVF Edit | 10 files | architecture gap, failure simulation, and system-hardening critique |

This matrix summarizes source-level meaning. It does not quote or promote
private reference content into public canon.

## Scope

In scope:

- classify source concepts into CVF owner surfaces;
- distinguish `absorbed`, `partially_absorbed`, `not_absorbed`, and
  `rejected_or_reference_only`;
- record claim boundaries for the public catalog;
- open follow-up gaps without interrupting the completed bounded 17.05 roadmap.

Out of scope:

- runtime implementation;
- public claim expansion beyond existing live evidence;
- copying external repo code, tools, manifests, hooks, agents, or skill packs;
- reopening F-1 output-quality parity tuning;
- expanding the audit outside the four approved source scopes.

## Methodology

The audit used file inventory plus source-summary extraction from each approved
legacy folder. Each source concept was mapped to the closest existing CVF owner
surface before considering new work. Concepts that were valuable but not yet
owned by a runtime, contract, guard, or evidence path were recorded as deferred
gaps.

Disposition vocabulary:

| Disposition | Meaning |
|---|---|
| `absorbed` | CVF already has a canonical doc/runtime/control surface with evidence-backed posture |
| `partially_absorbed` | CVF has pieces, but the pieces do not yet compose into the legacy claim |
| `doc_only` | CVF has doctrine/docs, but no enforceable runtime binding |
| `not_absorbed` | valuable source knowledge exists, but there is no CVF owner surface yet |
| `rejected_or_superseded` | source pattern is reference-only, rejected, or replaced by a safer CVF surface |
| `needs_gc018` | concept is ready for a future tranche, but must not be implemented without GC-018 |

Correction note:

- The first version of this matrix used four dispositions and was folder-axis
  oriented. Claude's five-axis rebuttal correctly found that this was not
  enough to satisfy the operator's concept-trace requirement.
- The companion concept-axis correction matrix is now:
  `docs/reviews/CVF_LEGACY_CONCEPT_AXIS_MATRIX_2026-05-18.md`.

## Findings

### Cross-Scope Pattern

The four source scopes converge on the same diagnosis:

```text
CVF has many strong governance parts.
The remaining gap is composition into enforceable product capability systems.
```

The recurring missing composition is:

```text
Outcome -> Workflow -> Certified Capability -> Policy -> Runtime ->
Validation -> Receipt -> Noncoder Deliverable
```

The bounded 17.05 roadmap delivered a narrow, evidence-backed slice of this
chain. The broader legacy sources still contain many valid runtime, memory,
role, tool, context, and observability patterns that must be absorbed in later
tranches.

### CVF 16.5

| Source folder | Primary concept | CVF owner surface | Current disposition | Follow-up |
|---|---|---|---|---|
| `abtop` | observability plane for sessions, tokens, context, processes, ports, and receipts | Web governance operations, runtime observability, operational metrics | `partially_absorbed` | define read-only observability plane contract before claiming full operator observability |
| `agentmemory` | governed persistent memory lifecycle, retrieval policy, reinjection, privacy filter | knowledge store, context builder, memory governance, audit trail | `partially_absorbed` | converge memory write/read/reinjection policy across web, worker, and external capability paths |
| `Claude Kit` | agent registry, role catalog, permission profile, handoff contract, allowed outputs | guard contract, agent registry, handoff guard, role taxonomy | `partially_absorbed` | role permissions and `allowed_outputs` need enforceable runtime binding |
| `free Claude Code` | model gateway proxy/translator/provider routing boundary | provider gateway, runtime adapters, provider readiness | `partially_absorbed` | unify proxy/provider translation claims with provider method demand gates |
| `freellmapi` | provider registry, health, quota, routing, fallback, sticky session, credential vault | provider lane readiness, quota/cost guard, provider policy engine | `partially_absorbed` | separate certified lane proof from broader provider hub runtime |
| `md2html` | governed Markdown-to-HTML artifact renderer | artifacts/export, deliverable packs, docs surface | `not_absorbed` | decide whether document artifact rendering is product runtime or documentation tooling |
| `Memento-Skills` | governed skill evolution loop | learning plane, skill registry, external capability intake | `partially_absorbed` | self-improvement must be proposal/gate/receipt based, not direct self-rewrite |
| `OpenAgentd` | local agent cockpit, scheduler, sandbox, tool trace, MCP, fallback, telemetry | web operations, sandbox worker, MCP bridge, runtime observability | `partially_absorbed` | cockpit and scheduler remain fragmented |
| `OpenSpec` | change-spec adapter and delta grammar | roadmap/review governance, GC-018, spec gate | `not_absorbed` | create change-spec adapter only after owner map is stable |
| `pancake-pos-mcp` | MCP business tool action taxonomy and risk classes | tool registry, tool policy guard, approval store, audit receipts | `partially_absorbed` | MCP action classes need a canonical tool/action governance vocabulary |
| `tolaria` | knowledge vault, Markdown graph, provenance, drift, governed reinjection | knowledge governance, context continuity, memory classification | `partially_absorbed` | graph/vault provenance must join memory tier map |

### CVF 17.05

| Source cluster | Primary concept | CVF owner surface | Current disposition | Follow-up |
|---|---|---|---|---|
| Final converged roadmap | eight problems, four phases, stabilization-first sequence | 17.05 Phase 0-4 artifacts and completion packets | `partially_absorbed` | bounded Phase 2.B/2.C/3.E done; Phase 4 remains demand-gated |
| External capability intake | intake, manifest, risk profile, certification, authority binding, security scan, workflow composition, install state | external asset governance, asset registry, provider/capability metadata | `partially_absorbed` | finish runtime certification chain before exposing external capability workflows as product claim |
| Agent orchestrator role gap | ORCHESTRATOR overreach, delegation contract, reverse brief, role boundary | anti-collusion doctrine, role taxonomy, worker delegation | `partially_absorbed` | ORCHESTRATOR remains doc-bound until enforceable runtime role contract exists |
| Agent handoff and memory gap | continuity, single session front door, memory/handoff survival | session memory, active handoff, memory governance | `partially_absorbed` | single memory front door has procedure; runtime memory authority still fragmented |
| Provider method extension | stream, tool call, JSON mode, vision, embedding, reasoning methods | model gateway/provider output contract | `not_absorbed` | demand gate only; no method without consuming slice |

### CVF ADD

| Source folder | Primary concept | CVF owner surface | Current disposition | Follow-up |
|---|---|---|---|---|
| `AGENT ENGINEER` | agent engineering as system design, eval, observability, safety, product thinking | doctrine and engineering process | `absorbed` as doctrine | do not inflate into a new runtime layer |
| `Agent Harnesses` | handoff, checkpoint, worker continuity, artifact-to-memory | continuity, worker/runtime records | `partially_absorbed` | async worker lifecycle contract still needed |
| `AI-first vs Human-first` | avoid path-driven overconstraint; outcome contract plus bounded authorization | governance doctrine, product UX | `partially_absorbed` | needs explicit anti-overconstraint claim boundary |
| `caveman` | token/context/output efficiency | context builder, provider routing, output policy | `partially_absorbed` | efficiency guard/eval not yet a first-class product metric |
| `CLI-Anything` | agent-native command surfaces, JSON I/O, 7-phase harness lifecycle, catalog/install | command runtime, tool registry, external capability intake | `partially_absorbed` | command surface contract remains broader than current runtime |
| `code-review-graph` | Tree-sitter graph, dependency/impact context narrowing | knowledge layer, context builder | `not_absorbed` | graph context resolver is future code-intelligence tranche |
| `cortex-hub` | persistent memory, AST code intelligence, shared MCP endpoint, quality hooks | memory, knowledge, MCP bridge, guard engine | `partially_absorbed` | shared memory/code-intelligence provider requires contamination policy |
| `deepagents` | async subagent/worker lifecycle, work tickets, context quarantine | sandbox worker, execution lifecycle, W7 trace | `partially_absorbed` | worker delegation is not yet a canonical runtime protocol |
| `gridex` | governed database execution surface and DB action taxonomy | UX/noncoder, execution plane, policy vocabulary | `not_absorbed` | database action model needs separate GC-018 |
| `Hermes Agent` | gateway, scheduler, skill lifecycle, backend abstraction, sandbox/subagent limits | AI gateway, execution plane, skill registry, learning plane | `partially_absorbed` | scheduler/backend/subagent contracts remain fragmented |
| `Hugging Face` | capability/skill catalog and portability pattern | skill registry, external capability intake | `partially_absorbed` | use as catalog pattern, not public skill claim |
| `Human System Harness` | reverse brief, orchestrator delegation boundary, solution-bias guard | role taxonomy, anti-collusion, intake protocol | `partially_absorbed` | strong evidence for ORCHESTRATOR gap |
| `openrouter-cli.git` | provider-facing CLI envelope, NDJSON stream, exit codes, async jobs | provider gateway, command runtime | `partially_absorbed` | align with Phase 4 provider method demand gate |
| `Workflow GoClaw` | memory tiers and eight-stage agent pipeline | memory tier map, execution lifecycle | `partially_absorbed` | do not create a second AI OS; map into CVF canonical lifecycle |
| `REVIEW FOLDER` | accepted/rejected ADD doctrine synthesis | reference doctrine | `absorbed` as bounded doctrine | runtime activation remains bounded to already completed ADD tranches |

### CVF Edit

| Source file/cluster | Primary concept | CVF owner surface | Current disposition | Follow-up |
|---|---|---|---|---|
| `CVF_EDIT_ANALYSIS.md` | CVF as safety runtime plus governance framework, but governance runtime incomplete | public claim boundary, architecture roadmap | `partially_absorbed` | keep public catalog honest: control framework, not complete Agent OS |
| `Review CVF*` | state machine, role permissions, guard runtime enforcement, context stability, observability | phase governance, guard contract, role taxonomy, observability | `partially_absorbed` | convert critique into enforceable state/permission/runtime specs |
| `Failure Simulation cho CVF.md` | failure scenarios: architecture drift, wrong spec, weak self-review, context instability | review gates, spec gate, human checkpoint, validation | `partially_absorbed` | add deterministic failure simulation suite before stronger Agent OS claim |
| `De_xuat.md` | formal state machine, mandatory guard enforcement, permission model, verifiable self-review | governance runtime hardening | `partially_absorbed` | feeds the next hardening roadmap |
| `CVF AUDIT LOG_md` | audit continuity | evidence and review retention | `partially_absorbed` | reconcile with active evidence index and public catalog anchors |

## Risk

The main risk is not that CVF lacks valuable knowledge. The main risk is
premature claim convergence:

- treating doc-level absorption as runtime enforcement;
- treating source summaries as public product proof;
- treating provider adapters as certified provider behavior;
- treating role names as enforced role permissions;
- treating memory concepts as governed reinjection.

This risk is exactly why the next work should be a bounded absorption roadmap,
not direct broad implementation.

## Decision

The operator-approved decision remains:

- finish already-authorized roadmap work first;
- record additional legacy gaps during source scans;
- defer broad legacy absorption until after the bounded roadmap closes;
- use this matrix and the gap ledger as the input for the next roadmap.

## Recommendation

Open the next continuation as:

`docs/roadmaps/CVF_LEGACY_ABSORPTION_AND_PUBLIC_CATALOG_ROADMAP_2026-05-18.md`

That roadmap should first stabilize the knowledge map and public claim catalog,
then implement high-value gaps in narrow, evidence-backed slices.

## Claim Boundary

This matrix does not authorize implementation and does not change public CVF
claims. It is a review artifact. Public-facing language must be taken from a
curated catalog that separates proven capabilities from roadmap candidates.
