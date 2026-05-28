# CVF Legacy Spec Absorption Blindspot Audit

Memory class: FULL_RECORD

Status: AUDIT_FILED

docType: audit

Date: 2026-05-23

Auditor: Claude (external quality assessor role)

---

## Purpose

Record a structural gap in CVF's audit methodology: every pain-point
audit and delivery-gap audit conducted to date has audited closure
reviews and runtime surfaces but has never audited `.private_reference/legacy/`
spec files for absorption status. As a result, detailed implementation
specs written into CVF legacy folders have been repeatedly overlooked
when pain points were reviewed, even after multiple rounds of auditing
by both Claude and Codex.

This audit is triggered by operator discovery on 2026-05-23 that two
folders — `agentmemory` (CVF 16.5) and `code-review-graph` (CVF ADD) —
contain detailed, actionable specs for Pain H (Memory Hierarchy) and the
organizational intelligence layer, but were never referenced in any audit,
roadmap, tranche, or work order.

---

## Owner / Source

Owner: Claude (external quality assessor role), 2026-05-23.

Source authority:

- `.private_reference/legacy/CVF 16.5/agentmemory/` — 10 spec files (read directly)
- `.private_reference/legacy/CVF ADD/code-review-graph/` — 5 spec files + README (read directly)
- `docs/audits/archive/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_GAP_AUDIT_2026-05-22.md` — grep verified: zero matches for `agentmemory`, `code-review-graph`, `CVF 16.5`, `CVF ADD`
- `docs/reviews/archive/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_CODEX_REVIEW_2026-05-22.md` — grep verified: zero matches for same terms
- Operator discovery statement on 2026-05-23 (direct session input)

---

## Scope / Target / Owner Boundary

Target under audit:

- `.private_reference/legacy/CVF 16.5/agentmemory/` — 10 spec files
- `.private_reference/legacy/CVF ADD/code-review-graph/` — 5 spec files + README
- `docs/audits/archive/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_GAP_AUDIT_2026-05-22.md`
  — predecessor audit that missed these specs
- `docs/reviews/archive/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_CODEX_REVIEW_2026-05-22.md`
  — Codex review that missed these specs
- `docs/roadmaps/archive/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_V2_2026-05-22.md`
  — roadmap whose T5 (memory) was scoped without consulting these specs

Owner boundary:

- Audit only. Does not authorize implementation, does not file GC-018,
  does not change posture, does not lift any freeze or blocked-work class.
- Does not reopen T1–T5 closures. Their bounded contracts remain valid.
- Records that T5 was scoped without awareness of `agentmemory` specs,
  and that the graph knowledge layer has no tranche at all.

---

## The Core Finding

### Finding 1 — Audit methodology structurally excluded legacy specs

**Severity: SYSTEMIC.**

Every audit and review in the pain-point closure chain used the
following methodology:

1. Read active session state.
2. Read closure reviews from `docs/reviews/`.
3. Read runtime surfaces from `EXTENSIONS/`.
4. Compare against `Review CVF.md` deliverable list.

No step in this methodology reads `.private_reference/legacy/`. The
legacy folder is present in the repo and contains implementation-ready
specs, but the `requiredFirstReads` list in
`CVF_SESSION/ACTIVE_SESSION_STATE.json` does not include it, and no
audit template requires it.

Result: agents and Codex completed multiple rounds of auditing — Gap
Audit (2026-05-22), Codex Blocking Review (2026-05-22), V2 Roadmap,
T1–T5 implementation — without ever reading the two most relevant spec
folders for Pain H and the organizational intelligence layer.

---

### Finding 2 — Pain H (Memory Hierarchy) was scoped against a thin spec

**Severity: BLOCKING for next memory tranche.**

Pain H from Review CVF.md asked for:

```text
MEMORY GOVERNANCE MODEL
working / task / skill / organizational / audit / long-term / receipt tiers
+ retention policy + injection policy + retrieval policy
+ privacy scope + contamination boundary
```

T5 in the V2 roadmap was scoped to:

```text
ephemeral in-memory task store + retention policy enforcement
canReinject=false preserved
memoryCaptureMode/Reason readout
```

The actual spec for Pain H is in
`.private_reference/legacy/CVF 16.5/agentmemory/` — 10 files:

| Spec file | What it defines |
| --- | --- |
| `CVF_CONTROLLED_MEMORY_GATEWAY.md` | Gateway interface, entry/exit contract |
| `CVF_MEMORY_ACCESS_POLICY.md` | Read/write policy per tier and actor |
| `CVF_MEMORY_CAPTURE_ADAPTER.md` | Capture adapter, event-driven capture |
| `CVF_MEMORY_CONTEXT_PACKAGER.md` | `[MEMORY_CONTEXT]` output block format |
| `CVF_MEMORY_EVENT_HOOKS.md` | Event hooks for capture triggers |
| `CVF_MEMORY_GUARD_CONTRACT.md` | Guard contract for memory operations |
| `CVF_MEMORY_LIFECYCLE_POLICY.md` | Lifecycle decay: working → episodic → semantic → procedural |
| `CVF_MEMORY_PRIVACY_FILTER_POLICY.md` | Privacy filter before reinject |
| `CVF_MEMORY_REINJECTION_PROTOCOL.md` | Reinjection protocol (canReinject gate) |
| `CVF_MEMORY_RETRIEVAL_POLICY.md` | Retrieval methods: keyword / semantic / graph / recency / audit_trust |

T5 delivered the reinjection gate (`canReinject=false`) and tier
classifier. It did not deliver the gateway interface, lifecycle decay,
semantic retrieval, context packager, or guard contract — all of which
have detailed specs already written.

---

### Finding 3 — Graph Knowledge has no tranche and no roadmap entry

**Severity: GAP NOT YET TRACKED.**

`.private_reference/legacy/CVF ADD/code-review-graph/` contains:

| Spec file | What it defines |
| --- | --- |
| `CVF_GRAPH_KNOWLEDGE_SPEC.md` | 5-phase plan; module tree for `knowledge/graph/` |
| `CVF_GRAPH_CONTEXT_RESOLUTION_SPEC.md` | Task-to-query mapper; blast-radius resolver |
| `CVF_GRAPH_IMPLEMENTATION_PLAN.md` | Phase 1 (AST foundation) → Phase 5 (review surface) |
| `CVF_GRAPH_INTEGRATION_SURFACE_SPEC.md` | Integration adapter contracts |
| `CVF_GRAPH_SCORING_SPEC.md` | Relevance scoring for context packs |

This spec set maps directly to:

- Review CVF.md Phase 4 "Operational Intelligence" → organizational memory + adaptive execution
- Pain H retrieval policy `graph_search` method (consumer of this layer)
- The CVF Knowledge Layer and Context Builder in the agent platform

No existing audit, roadmap, tranche, or work order references this spec
set. The capability is entirely unbuilt and not on any roadmap.

---

### Finding 4 — The meta-gap: audit chain is self-referential

**Severity: STRUCTURAL.**

The 2026-05-22 Gap Audit identified Systemic Cause #6:

> *"No standing artifact tracked Review CVF.md's original deliverable
> list against shipped output."*

But the Gap Audit itself committed the same error for a different layer:
it tracked pain-point deliverables against closure reviews and runtime
surfaces, but did not check whether detailed implementation specs existed
in `.private_reference/legacy/` that had never been absorbed.

The audit chain — Gap Audit → Codex Review → V2 Roadmap → T1–T5 — is
internally consistent and self-confirming. No step in the chain was
designed to ask: *"Does a more detailed spec already exist somewhere in
this repo that we have not read?"*

This is the same failure mode as Systemic Cause #5 in the Gap Audit:

> *"Reviewer-implementer-auditor chain inside a single Codex session
> tends to converge on what the orchestrator scoped initially."*

Applied recursively: the audit itself converged on what the first
auditor scoped, without external verification against legacy content.

---

### Finding 5 — Discovery was operator-driven, not system-driven

**Severity: PROCESS.**

The two folders were discovered on 2026-05-23 because the operator
said: *"Chúng ta đã từng hấp thu không ít kiến thức về vấn đề memory
cho agent, nhưng có vẻ GAP của CVF vẫn còn rất nhiều? Ví dụ, folder
agentmemory trong CVF 16.5?"*

The operator suspected a gap and asked the agent to check. The agent
then found the folders. No audit had surfaced them previously.

This means CVF's audit system cannot self-detect absorption gaps in
legacy specs. Detection requires operator suspicion or accidental
discovery.

---

## Inventory of Unabsorbed Legacy Specs

### agentmemory (CVF 16.5)

Path: `.private_reference/legacy/CVF 16.5/agentmemory/`

| File | Absorbed into CVF? | Notes |
| --- | --- | --- |
| `CVF_CONTROLLED_MEMORY_GATEWAY.md` | NO | Gateway interface not implemented |
| `CVF_MEMORY_ACCESS_POLICY.md` | NO | No per-tier read/write policy in runtime |
| `CVF_MEMORY_CAPTURE_ADAPTER.md` | PARTIAL | Event-driven capture partially wired via CDH-H readout |
| `CVF_MEMORY_CONTEXT_PACKAGER.md` | NO | `[MEMORY_CONTEXT]` block format not implemented |
| `CVF_MEMORY_EVENT_HOOKS.md` | NO | No event hooks in `CVF_LEARNING_PLANE_FOUNDATION` |
| `CVF_MEMORY_GUARD_CONTRACT.md` | PARTIAL | `canReinject=false` implements one guard; full contract absent |
| `CVF_MEMORY_LIFECYCLE_POLICY.md` | NO | No lifecycle decay (working → episodic → semantic → procedural) |
| `CVF_MEMORY_PRIVACY_FILTER_POLICY.md` | NO | Privacy filter before reinject not implemented |
| `CVF_MEMORY_REINJECTION_PROTOCOL.md` | PARTIAL | Gate exists; protocol details absent |
| `CVF_MEMORY_RETRIEVAL_POLICY.md` | NO | No semantic, graph, or recency retrieval in runtime |

### code-review-graph (CVF ADD)

Path: `.private_reference/legacy/CVF ADD/code-review-graph/`

| File | Absorbed into CVF? | Notes |
| --- | --- | --- |
| `CVF_GRAPH_KNOWLEDGE_SPEC.md` | NO | `knowledge/graph/` module does not exist |
| `CVF_GRAPH_CONTEXT_RESOLUTION_SPEC.md` | NO | No task-to-query mapper or blast-radius resolver |
| `CVF_GRAPH_IMPLEMENTATION_PLAN.md` | NO | None of 5 phases started |
| `CVF_GRAPH_INTEGRATION_SURFACE_SPEC.md` | NO | No integration adapters for graph layer |
| `CVF_GRAPH_SCORING_SPEC.md` | NO | No relevance scoring for context packs |

---

## Systemic Cause Analysis

| Cause | Description |
| --- | --- |
| SC-1: No legacy scan step in audit templates | Audit methodology reads `docs/reviews/` and `EXTENSIONS/` but never scans `.private_reference/legacy/` for unabsorbed specs |
| SC-2: `requiredFirstReads` does not include legacy spec paths | Session state only lists 17.05 REVIEW FOLDER files; CVF 16.5 and CVF ADD are not listed |
| SC-3: No absorption registry | There is no artifact that tracks "which legacy specs have been absorbed into which tranche" |
| SC-4: Pain point closure uses Review CVF.md as sole comparator | The Gap Audit compared closure against Review CVF.md deliverables only — not against implementation specs in legacy |
| SC-5: Agent audit chain is self-confirming | Once scope is set by the first auditor, downstream roles do not expand scope to include unseen folders |
| SC-6: Operator is the only detection mechanism | Gaps surface only when the operator suspects something is missing and explicitly asks for verification |

---

## What Must Change

Three corrective actions are required. None are implementation work —
they are process changes only, and each is Fast Lane eligible.

### CA-1 — Add legacy spec scan to audit methodology (Fast Lane)

Every future pain-point audit, delivery-gap audit, or tranche GC-018
must include a step:

> "Read `.private_reference/legacy/` folder list and confirm whether
> any spec files exist that are relevant to the tranche scope. If yes,
> read those files before scoping the tranche."

This step should be added to:

- `docs/reference/CVF_GC018_CONTINUATION_CANDIDATE_TEMPLATE.md`
- Any future pain-point audit template

### CA-2 — Create a Legacy Spec Absorption Registry (Fast Lane)

Create `docs/reference/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md`
listing every spec folder in `.private_reference/legacy/` with:

- absorption status (absorbed / partial / not-absorbed)
- which tranche absorbed it (if any)
- which pain point or roadmap it maps to

This registry becomes a required read for any future memory, graph,
or intelligence-layer tranche.

### CA-3 — Add T-H2 and T-GRAPH to the V2 Roadmap as successor tranches

The V2 roadmap currently ends at T5 (ephemeral task store). Two
successor tranches are now visible from the legacy specs:

- **T-H2** — Memory Gateway Phase 2: lifecycle decay + semantic retrieval
  + context packager, sourced from `agentmemory` specs. Requires fresh
  GC-018; blocked by `new_memory_tiers_beyond_lane_h_scope` until
  explicitly lifted.

- **T-GRAPH** — Graph Knowledge Phase 1: AST foundation + dependency
  graph + SQLite storage, sourced from `code-review-graph` specs.
  Requires fresh GC-018 AND PBR-04 persistence-block lift (currently
  deferred — no current path without operator decision).

These tranches should be added to the roadmap as `DEMAND_GATED` entries,
not as authorized work. Authorization requires a separate GC-018 per
tranche.

---

## Risk / Defect / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Future audits repeat the same blindspot | CA-1: add legacy scan to audit methodology |
| Legacy specs continue to be forgotten | CA-2: create absorption registry |
| T-H2 and T-GRAPH remain invisible to future agents | CA-3: add demand-gated entries to V2 roadmap |
| Operator remains the only detection mechanism | CA-1 + CA-2 together create a system-level detection step |
| New legacy specs added without tracking | Absorption registry must be updated whenever `.private_reference/legacy/` receives new content |

---

## Decision / Recommendation / Disposition

Disposition: `AUDIT_FILED`.

Recommendations:

1. File CA-1 as a Fast Lane update to GC-018 template.
2. File CA-2 as a Fast Lane new reference doc
   (`CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md`).
3. File CA-3 as a Fast Lane update to V2 roadmap (demand-gated entries
   only — no implementation authorization).
4. When any future agent or Codex receives a memory or graph tranche,
   this audit must be in its `requiredFirstReads`.

---

## Verification

Static verification:

- `.private_reference/legacy/CVF 16.5/agentmemory/` — 10 files confirmed
  present.
- `.private_reference/legacy/CVF ADD/code-review-graph/` — 5 spec files
  + README confirmed present.
- `docs/audits/archive/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_GAP_AUDIT_2026-05-22.md`
  — grep for "agentmemory", "code-review-graph", "CVF 16.5", "CVF ADD"
  returns no matches. Confirmed: these folders were not referenced.
- `docs/reviews/archive/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_CODEX_REVIEW_2026-05-22.md`
  — same grep: no matches.
- HEAD at time of filing: `e5a1d26d`.

---

## Claim Boundary

This audit claims only:

- Two legacy spec folders (`agentmemory` CVF 16.5, `code-review-graph`
  CVF ADD) were present in the repo during the entire pain-point closure
  chain but were never referenced in any audit, roadmap, or tranche.
- T5 was scoped without reading the `agentmemory` specs; its bounded
  closure remains valid but incomplete relative to Pain H's full ask.
- The audit methodology has a structural gap that prevented this
  discovery.
- Three Fast Lane corrective actions are recommended.

Does not claim:

- That T1–T5 closures are wrong or should be reopened.
- That T-H2 or T-GRAPH are authorized.
- That any freeze, posture, or blocked-work class is changed.
- That any source code should be modified.

---

## Protocol / Contract / Requirements

Any future agent, Codex session, or tranche GC-018 that touches memory
hierarchy (Pain H) or graph knowledge (Phase 4 Operational Intelligence)
must comply with the following protocol before scoping:

1. Read this audit in full.
2. Read `.private_reference/legacy/CVF 16.5/agentmemory/` (10 files)
   before scoping any memory tranche.
3. Read `.private_reference/legacy/CVF ADD/code-review-graph/` (5 files)
   before scoping any graph knowledge or context-builder tranche.
4. Cross-check tranche scope against the absorption inventory table in
   this audit. Every `NO` row that the tranche intends to address must
   be explicitly named in the tranche GC-018.
5. If scoping Pain H work, the tranche must declare which of the 10
   `agentmemory` spec files it absorbs and which it defers.

Failure to follow this protocol reproduces the exact blindspot this
audit was filed to correct.

---

## Related Artifacts

- `docs/audits/archive/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_GAP_AUDIT_2026-05-22.md`
  — predecessor gap audit; does not reference legacy specs (verified)
- `docs/reviews/archive/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_CODEX_REVIEW_2026-05-22.md`
  — Codex blocking review; does not reference legacy specs (verified)
- `docs/roadmaps/archive/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_V2_2026-05-22.md`
  — V2 roadmap; T5 scoped without `agentmemory` specs; T-H2/T-GRAPH
  demand-gated entries to be added per CA-3
- `.private_reference/legacy/CVF 16.5/agentmemory/` — 10 spec files,
  Pain H full scope
- `.private_reference/legacy/CVF ADD/code-review-graph/` — 5 spec files,
  graph knowledge layer
- `.private_reference/legacy/CVF 17.05/Review CVF.md` — original 8
  pain points (A–H); Pain H and Phase 4 defined here
- `CVF_SESSION_MEMORY.md` — pointer to this audit added 2026-05-23
