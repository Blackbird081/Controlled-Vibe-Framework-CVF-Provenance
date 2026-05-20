# CVF 16.5 External Knowledge Intake Review - 2026-05-16

Memory class: REVIEW_PACKET

Status: absorbed (docs-only); Claude rebuttal accepted and amended.

Primary private review packet:
`.private_reference/legacy/CVF 16.5/REVIEW FOLDER/CVF_16_5_EXTERNAL_KNOWLEDGE_INTAKE_REVIEW_2026-05-16.md`

Independent rebuttal:
`docs/reviews/archive/CVF_16_5_EXTERNAL_KNOWLEDGE_INTAKE_REVIEW_CLAUDE_REBUTTAL_2026-05-16.md`

Codex disposition:
`docs/reviews/archive/CVF_16_5_EXTERNAL_KNOWLEDGE_INTAKE_REVIEW_CODEX_RESPONSE_TO_CLAUDE_2026-05-16.md`

Reviewed source bundle:
`.private_reference/legacy/CVF 16.5`

## Scope

This review evaluates the legacy CVF 16.5 knowledge bundle as external intake
material. The goal is not to import another framework. The goal is to identify
which already-written drafts are useful enough to normalize into CVF docs, and
which ideas must stay deferred or rejected.

## Bottom Line

The bundle is valuable, but only as governed boundary material.

Accepted now:

- knowledge/vault intake as candidate context, not source authority;
- memory and skill evolution as governed proposal loops, not self-writing
  runtime;
- agent/tool/MCP/proxy/provider surfaces as adapter-bound capabilities that
  require risk, approval, validation, and receipt;
- observability and artifact rendering as visibility/presentation surfaces, not
  policy or execution authority.

Not accepted now:

- new parallel apps or runtimes;
- free-provider or proxy-bypass narratives;
- direct raw vault/memory/MCP/provider access by agents;
- any live governance claim without the repository's live proof policy.

## Fit Classification

| Source | Fit | Intake decision |
|---|---:|---|
| Tolaria | High | Absorb knowledge intake/provenance/drift/reinjection patterns |
| agentmemory | High | Absorb controlled memory governance; defer runtime |
| Claude Kit | High | Absorb agent registry/permissions/handoff/audit semantics |
| OpenAgentd | High/Medium | Absorb tool trace, sandbox, telemetry, scheduler policy; defer cockpit OS |
| abtop | High/Medium | Absorb observe-only runtime signals; do not grant intervention authority |
| md2html | Medium/High | Absorb document artifact rendering policy and verification checklist |
| OpenSpec | Medium/High | Absorb change-packet/delta/archive boundary semantics |
| pancake-pos-mcp | High for generic MCP adapter pattern; defer Pancake profile | Absorb 7 generic MCP business adapter primitives as future adoption candidates; defer `pancake-pos-mcp.profile.ts` |
| free Claude Code | Medium | Absorb proxy/translator boundary; reject bypass branding |
| freellmapi | Medium/High | Surface 8 existing `.ts` gateway artifacts as future `EXTENSIONS/CVF_MODEL_GATEWAY/` adoption candidates; reject free-tier production claim |
| Memento-Skills | Medium | Absorb governed skill-evolution proposal loop; defer self-mutating runtime |

## CVF Docs Created From Reusable Drafts

- `docs/reference/archive/CVF_LEGACY_16_5_EXTERNAL_KNOWLEDGE_ABSORPTION_MAP_2026-05-16.md`
- `docs/reference/archive/CVF_MODEL_GATEWAY_PROXY_PROVIDER_BOUNDARY_SPEC_2026-05-16.md`
- `docs/reference/archive/CVF_AGENT_TOOL_MEMORY_OBSERVABILITY_BOUNDARY_SPEC_2026-05-16.md`
- `docs/reference/archive/CVF_GOVERNED_DOCUMENT_ARTIFACT_RENDERING_SPEC_2026-05-16.md`

These docs intentionally merge and normalize the strongest existing drafts
instead of copying every legacy file into CVF canon.

## Claude Rebuttal Disposition

Claude's rebuttal is accepted as materially correct. The original Codex tranche
had the right governance posture but collapsed too much path and schema
information from the source bundle.

Amendments applied:

- added explicit source-destination and existing-surface maps to the boundary
  specs;
- surfaced `freellmapi/*.ts` as priority adoption candidates for a future Model
  Gateway roadmap;
- reclassified `pancake-pos-mcp` as high-fit for generic MCP adapter primitives
  and deferred only for the Pancake-specific profile;
- repositioned the new specs as delta/boundary docs over existing EXTENSIONS
  surfaces, not standalone runtime owners;
- answered the open counter-review questions below.

## Counter-Review Questions Answered

1. Are accepted values too broad?

Yes for runtime implementation. The docs absorption can stay bundled, but the
next implementation tranche must pick exactly one owner surface. Recommended
first candidates are Model Gateway, Agent/Tool Boundary, or Memory Boundary.

2. Does any promoted draft duplicate existing canonical docs?

Yes. The Model Gateway spec overlaps `EXTENSIONS/CVF_MODEL_GATEWAY/README.md`.
It is now positioned as a delta/boundary spec for that existing surface, not as
a new gateway owner.

3. Should `pancake-pos-mcp` remain fully deferred?

No. The generic MCP adapter primitives are high-fit and reusable. The
Pancake-specific profile remains deferred and must not be hardcoded into CVF
core.

4. Is document artifact rendering high enough value after F-1 closure?

Only as docs-only presentation boundary. Runtime rendering should not start
without a fresh roadmap, and it must not be used to mask the closed F-1 output
quality boundary.

5. Should Observability Plane reuse v1.8.1?

Yes. The observability material should be treated as a delta on
`EXTENSIONS/CVF_v1.8.1_ADAPTIVE_OBSERVABILITY_RUNTIME/`, not as a new
Observability Plane unless a later roadmap proves a separate surface is needed.

## Claim Boundary

This packet proves docs absorption and counter-review amendment only. It does
not prove runtime behavior, live provider routing, MCP tool enforcement, memory
governance, observability enforcement, or artifact rendering execution.

Any future runtime claim must use a fresh roadmap and the repository's mandatory
live governance proof rule.
