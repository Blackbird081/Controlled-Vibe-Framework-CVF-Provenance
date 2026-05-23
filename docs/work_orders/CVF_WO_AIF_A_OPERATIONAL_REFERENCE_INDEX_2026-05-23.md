# CVF Work Order: AIF-A Operational Reference Index

Memory class: FULL_RECORD

Status: READY_FOR_IMPLEMENTATION

docType: work_order

Date: 2026-05-23

Tranche: AIF-A

Roadmap: `docs/roadmaps/CVF_AGENT_INTELLIGENCE_FOUNDATIONS_ROADMAP_2026-05-23.md`

---

## Purpose

Create `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` — a
"when task X → read document Y" lookup table that solves agent discoverability.

This is the Fast Lane corrective action CA-1 from the legacy spec absorption
blindspot audit and the first tranche in the Agent Intelligence Foundations
roadmap.

---

## Authority Chain

Operator → Claude (roadmap author) → Codex (implementer).

Authorization: AIF-A is Fast Lane eligible (GC-021) — documentation only,
no GC-018 required. Parent roadmap:
`docs/roadmaps/CVF_AGENT_INTELLIGENCE_FOUNDATIONS_ROADMAP_2026-05-23.md`.

---

## Agent Roles

- Codex: implementer — creates the reference file, adds wiring pointers
- Claude: reviewer — confirms structural completeness and required rows
- Operator: authorizer — AIF-A is pre-authorized under Fast Lane

---

## Required First Reads

Before implementing:

- `docs/audits/CVF_LEGACY_SPEC_ABSORPTION_BLINDSPOT_AUDIT_2026-05-23.md`
- `docs/reviews/CVF_LEGACY_SPEC_ABSORPTION_BLINDSPOT_CODEX_REVIEW_2026-05-23.md`
- `docs/reference/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md`

---

## Owner / Source

Owner: Codex (implementer), Claude (reviewer).

Predecessor evidence (read before implementing):

- `docs/audits/CVF_LEGACY_SPEC_ABSORPTION_BLINDSPOT_AUDIT_2026-05-23.md`
- `docs/reviews/CVF_LEGACY_SPEC_ABSORPTION_BLINDSPOT_CODEX_REVIEW_2026-05-23.md`
- `docs/reference/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md`

---

## Scope / Target / Owner Boundary

Target surfaces:

- `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` (new)
- `CVF_SESSION_MEMORY.md` (pointer addition only)
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` (`nextAllowedMove` update)
- Active handoff Latest Work section (pointer addition)
- `docs/roadmaps/CVF_AGENT_INTELLIGENCE_FOUNDATIONS_ROADMAP_2026-05-23.md`
  (Progress Tracker AIF-A row → `CLOSED_PASS`)

Out of scope:

- No source code change
- No runtime, provider, receipt, or schema change
- No public-sync update
- No freeze release

---

## Pre-Flight Checks

Before creating the new file:

1. Verify `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` does not already exist
2. Check `CVF_SESSION_MEMORY.md` current line count — hard cap 1200 lines (pointer addition must stay within bounds)
3. Check `ACTIVE_SESSION_STATE.json` — confirm `nextAllowedMove` field is writable
4. Verify `docs/roadmaps/CVF_AGENT_INTELLIGENCE_FOUNDATIONS_ROADMAP_2026-05-23.md` Progress Tracker AIF-A row shows `WORK_ORDER_READY`

---

## Write Ownership

- Codex owns: `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` (new)
- Codex adds one pointer line to: `CVF_SESSION_MEMORY.md`
- Codex appends one sentence to: `ACTIVE_SESSION_STATE.json` `nextAllowedMove`
- Codex adds one line to: active handoff Latest Work section
- Codex updates: `docs/roadmaps/CVF_AGENT_INTELLIGENCE_FOUNDATIONS_ROADMAP_2026-05-23.md` AIF-A row

No other files may be modified.

---

## Execution Plan

1. Read all Required First Reads
2. Create `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` with all required sections and rows per the Deliverable Specification below
3. Verify Test-Path equivalent for every path referenced in the lookup table
4. Add pointer to `CVF_SESSION_MEMORY.md` Required First Reads section
5. Update `ACTIVE_SESSION_STATE.json` `nextAllowedMove`
6. Update active handoff Latest Work section
7. Update AIF-A row in roadmap Progress Tracker to `CLOSED_PASS`
8. File completion review at `docs/reviews/CVF_AIF_A_OPERATIONAL_REFERENCE_INDEX_COMPLETION_2026-05-23.md`
9. Commit with descriptive message

---

## Evidence Requirements

- `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` exists and passes GC-045 structural completeness
- All paths in the lookup table verified to exist (Test-Path equivalent)
- Completion review filed
- Wiring pointers confirmed in all 4 target files
- GC-023 line count pre-flight passed for all modified files

---

## Review Gate

Claude reviews the completed reference file for:

- structural completeness (GC-045)
- all required rows present
- all path references valid
- `Memory class: POINTER_RECORD` present
- no runtime or source code claim

---

## Governance

Governance class: Fast Lane (GC-021).

Eligibility:

- additive only: YES — new reference file
- no physical merge: YES
- no ownership transfer: YES
- no runtime authority change: YES
- no target-state claim expansion: YES
- no concept-to-module creation: YES
- documentation only: YES

No GC-018 required. No blocked-work override required.

---

## Deliverable Specification

### File: `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`

**Required sections:**

1. **Purpose** — one paragraph explaining "when task X → read document Y"
2. **How to use** — two sentences max
3. **Lookup Table** — the main artifact (see schema below)
4. **Maintenance rule** — how to keep it current
5. **Claim Boundary**

**Lookup table schema:**

```markdown
| Task / Situation | Required reading | Why |
| --- | --- | --- |
| ...             | ...              | ... |
```

**Required rows (minimum — Codex may add more based on repo state):**

| Task / Situation | Required reading |
| --- | --- |
| Scoping any memory / hierarchy tranche | `agentmemory` specs (CVF 16.5) + registry + blindspot audit + Codex correction |
| Scoping any graph / context-builder tranche | `code-review-graph` specs (CVF ADD) + registry + blindspot audit |
| Any new Qwen3 or Alibaba hosted proof | `CVF_QWEN3_HOSTED_PROOF_PREREQUISITES_2026-05-23.md` |
| Adding a new provider or model | `providers.ts` + `provider-router-adapter.ts` + `PROVIDER_CAPABILITY_REGISTRY` |
| Any pain-point closure or Review-CVF successor | Review CVF.md + gap audit + Codex correction review + registry |
| Filing a new GC-018 touching legacy-adjacent scope | GC-018 template + Legacy Spec Scan Block + registry |
| Public-sync update | CLAUDE.md public-sync rule + catalog update rule + Test-Path verification |
| Scoping T-H2 (memory gateway phase 2) | AIF-C work order + registry agentmemory row + blindspot audit |
| Scoping T-GRAPH (graph knowledge phase 1) | AIF-B work order + registry code-review-graph row + blindspot audit |
| New session start / agent handoff | `CVF_SESSION_MEMORY.md` → `ACTIVE_SESSION_STATE.json` → active handoff |
| GC-023 file size pre-flight | `CVF_GOVERNED_FILE_SIZE_GUARD.md` + exception registry |
| Checking Pain H memory status | H2 completion review + T5 completion review + registry agentmemory row |
| Checking graph knowledge status | registry code-review-graph row + `ScopedKnowledgeProvider` boundary doc |

**Memory class:** `POINTER_RECORD` (reference doc taxonomy rule).

**GC-045 required sections:** Purpose, Owner/Source, Scope/Target/Owner Boundary,
Lookup Table (main body), Maintenance Rule, Claim Boundary.

---

## Wiring Requirements

After creating the reference file, Codex must also:

### 1. CVF_SESSION_MEMORY.md — add pointer in Required First Reads section

Add one line pointing to the new index file. Do not exceed 1200-line hard
threshold (current: ~878 lines — safe).

### 2. ACTIVE_SESSION_STATE.json — update nextAllowedMove

Append one sentence to `nextAllowedMove`:
> "AIF-A Operational Reference Index is WORK_ORDER_READY at
> `docs/work_orders/CVF_WO_AIF_A_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`;
> read `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` when
> scoping any memory, graph, provider, or pain-point tranche."

### 3. Active handoff — add Latest Work pointer

One line: `[AIF-A] Operational Reference Index created at docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md.`

### 4. Roadmap Progress Tracker — update AIF-A row

Change Status from `WORK_ORDER_READY` to `CLOSED_PASS` and add the completion
review path once filed.

---

## Acceptance Criteria

- [ ] `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` exists
      and passes GC-045 structural completeness
- [ ] File has `Memory class: POINTER_RECORD`
- [ ] Lookup table contains all required rows (at minimum)
- [ ] All path references in the table verified to exist (Test-Path equivalent)
- [ ] `CVF_SESSION_MEMORY.md` has pointer to new index
- [ ] `ACTIVE_SESSION_STATE.json` `nextAllowedMove` updated
- [ ] Active handoff has Latest Work pointer
- [ ] Roadmap Progress Tracker AIF-A row shows `CLOSED_PASS`
- [ ] `docs/roadmaps/CVF_AGENT_INTELLIGENCE_FOUNDATIONS_ROADMAP_2026-05-23.md`
      AIF-A Completion review path filled in
- [ ] Fast Lane audit filed (one file) — can be inline with the work order
      closure or as a separate `docs/reviews/` file
- [ ] GC-023 line count pre-flight passed for all modified files
- [ ] Commit SHA recorded in handoff

---

## Closure Checklist

- [ ] `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` created and GC-045 compliant
- [ ] All required lookup table rows present and path-verified
- [ ] Pointer added to `CVF_SESSION_MEMORY.md`
- [ ] `ACTIVE_SESSION_STATE.json` `nextAllowedMove` updated
- [ ] Active handoff Latest Work pointer added
- [ ] AIF-A roadmap Progress Tracker row → `CLOSED_PASS`
- [ ] Completion review filed at `docs/reviews/CVF_AIF_A_OPERATIONAL_REFERENCE_INDEX_COMPLETION_2026-05-23.md`
- [ ] Commit SHA recorded

---

## Return-To-Orchestrator Conditions

Return to Claude (reviewer) when:

- The reference file exists and all acceptance criteria above are met
- OR: a structural blocker is encountered (e.g., a required path does not exist and Codex cannot verify it)

Do not return partial work. File the completion review before returning.

---

## Operator Checkpoint

operator.checkpoint.waiver: AIF-A is documentation-only Fast Lane work with no runtime, source code, provider, or governance semantics change — operator pre-authorized this tranche under the AIF roadmap directive on 2026-05-23.

---

## Completion Review

After implementation, file a completion review at:
`docs/reviews/CVF_AIF_A_OPERATIONAL_REFERENCE_INDEX_COMPLETION_2026-05-23.md`

Minimum sections: Purpose, Deliverables Verified, Acceptance Criteria (checklist),
Claim Boundary.

---

## Claim Boundary

This work order authorizes only the creation of one reference document and
pointer additions in session-continuity files. It does not authorize runtime
change, source code change, provider change, receipt schema change, memory
tier expansion, graph engine work, public-sync update, or freeze release.
