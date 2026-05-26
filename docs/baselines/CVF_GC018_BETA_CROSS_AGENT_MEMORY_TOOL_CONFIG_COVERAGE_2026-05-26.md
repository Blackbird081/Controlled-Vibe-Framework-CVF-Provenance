# CVF GC-018 Beta Cross-Agent Memory Tool Config Coverage

Memory class: BASELINE_RECORD

docType: baseline

Date: 2026-05-26

Status: AUTHORIZED_BY_OPERATOR_FOR_BETA_CONFIG_COVERAGE

## Purpose

Authorize Beta from the cross-agent memory progression roadmap: per-tool startup
config coverage for Gemini, Cursor, and Aider using the Alpha mandatory startup
acknowledgment pattern.

## Source / Predecessor

- `docs/roadmaps/CVF_CROSS_AGENT_MEMORY_PROGRESSION_ROADMAP_2026-05-26.md`
- Alpha implementation commit `910043af`
- Progression sync commit `b79bb0d9`

## Decision / Baseline

The operator authorized proceeding with the roadmap after reviewing Claude's
progression packet. This GC-018 opens Beta only.

Beta target: extend the Alpha soft startup acknowledgment pattern to supported
AI coding tools through per-tool config files.

## Knowledge Absorption Blind-Spot Control Block

Verdict: CLEAR_FOR_BETA_CONFIG_COVERAGE.

1. Source map resolved: Alpha front-door docs, cross-agent memory progression
   roadmap, official Gemini CLI `GEMINI.md` documentation, official Cursor rules
   documentation, and official Aider config/conventions documentation.
2. Prior evidence resolved: Alpha is closed bounded and remains the canonical
   soft-accountability bridge.
3. Detailed source read: official tool docs were checked before selecting file
   names and config mechanisms.
4. Accepted value normalized: one shared startup acknowledgment contract across
   Gemini, Cursor, and Aider.
5. Defer/reject recorded: MCP/Gamma, runtime auto-load, provider behavior, GUI
   launch proof, and production hardening remain out of Beta.
6. Adversarial role review: risk is config sprawl and false hard-enforcement
   claims; mitigated by explicit soft-accountability boundary in every file.
7. Blind-spot delta: static config coverage can be proven now; actual tool
   compliance requires operator/tool launch verification because Gemini, Cursor,
   and Aider are not installed in this shell environment.

## Scope

In scope:

- Add `GEMINI.md`.
- Add `.cursor/rules/cvf-startup-acknowledgment.mdc`.
- Add `.aider.conf.yml` and `CONVENTIONS.md`.
- Record static verification and operator/tool verification boundary.

Out of scope:

- Running GUI Cursor verification.
- Installing or invoking Gemini/Aider.
- MCP server work.
- Provider/API/runtime/receipt/route changes.
- Public-sync, hosted readiness, production readiness, or freeze release.

## Evidence / Verification

Expected evidence:

- Config files exist at the documented locations.
- Each file carries the same startup acknowledgment contract.
- Docs/session governance gates pass.
- Tool launch verification is explicitly recorded as pending if the tool is not
  available locally.

## Claim Boundary

This GC-018 authorizes Beta config coverage only. It cannot claim hard auto-load,
universal tool compliance, MCP availability, provider behavior, hosted readiness,
production readiness, public release readiness, or freeze release.
