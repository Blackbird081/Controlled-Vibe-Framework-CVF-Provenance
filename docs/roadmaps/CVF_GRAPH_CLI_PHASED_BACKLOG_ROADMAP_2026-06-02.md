# CVF Graph CLI Phased Backlog Roadmap

Memory class: FULL_RECORD

Status: PARKED_POST_CI1

docType: roadmap

Date: 2026-06-02

Related finding: `F3-cli-commands-absent`

Related registry: `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`

---

## Purpose

This roadmap parks the post-CI1 follow-up for Graphify CLI commands.

CI1-T2 verified that legacy Graphify docs describe `cvf graph` commands, while
current CVF runtime does not expose those commands in the CLI registry. That is
a valid phased backlog item, not a CI1-T2 closure blocker.

---

## Authorization / Decision

Decision: `PARKED_POST_CI1`.

Authorization boundary: this document records the phased CLI backlog for future
dispatch. It does not authorize adding commands. A later operator-authorized
work order must source-verify the current CLI and KGR runtime before
implementation.

---

## Scope Boundary

This roadmap does not authorize implementation by itself.

Before implementation, open a fresh work order with source verification against
the current CLI registry, command client pattern, and KGR runtime surfaces.

Out of scope for this parking roadmap:

- adding CLI commands now;
- wiring backend routes without source verification;
- claiming `cvf graph` is available;
- implementing graph build/visualize/export before query/status foundations.

---

## Non-Goals

- Do not add `cvf graph` commands in this batch.
- Do not assume the legacy Graphify command spec matches current CVF CLI
  architecture.
- Do not implement destructive commands such as `purge` before read-only query
  and status paths are proven.
- Do not claim production chatbot or retrieval readiness from CLI presence
  alone.

---

## Finding Disposition

| Finding | Disposition | Follow-up |
| --- | --- | --- |
| `F3-cli-commands-absent` | `DEFER_PHASED` | Use this roadmap as the backlog reference before opening a bounded `cvf graph` work order |

---

## Work Plan

The future CLI implementation should proceed in bounded phases:

1. Source-verify current CLI registry, command client pattern, and KGR runtime
   query surface.
2. Implement the smallest read-only command first: `cvf graph query`.
3. Add `cvf graph status` only after query receipt/provenance behavior is clear.
4. Defer build/validate/export/visualize/purge into separate tranches.
5. Close each phase with command tests, receipt evidence, and claim boundaries.

---

## Phase 1 — `cvf graph query`

Highest-value first command.

Candidate behavior:

- route user query input into the KGR retrieval request surface;
- preserve provenance/evidence pointers in output;
- refuse direct-answer claims when retrieval evidence is absent.

Required source verification before dispatch:

- CLI command registry path and command registration pattern;
- KGR query/evaluation function name and owning interface;
- expected output receipt structure or explicit doc-only boundary.

---

## Phase 2 — `cvf graph status`

Low-risk visibility command after query source surfaces are verified.

Candidate behavior:

- report graph store availability;
- report index/build freshness when such metadata exists;
- avoid claiming full graph coverage unless backed by scan registry evidence.

---

## Phase 3 — Build/Validate/Export/Visualize/Purge

These commands require a larger implementation tranche because they touch graph
construction, persistence, derived views, destructive state, or visualization.

They must not be bundled into the first CLI work order unless a later roadmap
explicitly expands scope.

---

## Claim Boundary

This roadmap records a phased CLI backlog. It does not prove that any `cvf
graph` command currently exists in CVF runtime.

---

## Acceptance Criteria

- A future work order cites this roadmap and the CI1-T2 finding packet.
- Phase 1 source verification identifies the current CLI command registration
  files and KGR query/evaluation symbol.
- The first CLI tranche is read-only unless explicitly expanded.
- CLI output preserves provenance or abstains when evidence is missing.
- No build/export/purge command is bundled into Phase 1 without a new decision.

---

## Verification / Evidence

Parking evidence for this roadmap:

- Registry finding: `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
- Finding packet: `docs/corpus-intelligence/findings/legacy-cvf-important-graphify.md`
- CI1-T2 audit packet: `docs/audits/CVF_CI1_T2_GRAPHIFY_READINESS_PACKET_2026-06-02.md`
- CI1-T2 completion review: `docs/reviews/CVF_CI1_T2_GRAPHIFY_LEGACY_RESCAN_PILOT_COMPLETION_2026-06-02.md`

Future implementation evidence must include source verification, tests, and
the applicable autorun phase gates.
