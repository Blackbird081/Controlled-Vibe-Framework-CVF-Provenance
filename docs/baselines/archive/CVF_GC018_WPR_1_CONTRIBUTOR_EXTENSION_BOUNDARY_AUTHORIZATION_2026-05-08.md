<!-- Memory class: FULL_RECORD -->
# CVF GC-018 - WPR-1 Authorization

> Date: 2026-05-08
> Tranche: WPR-1 - Contributor / Extension Author Boundary
> Status: AUTHORIZED

## Decision

WPR-1 is authorized as a documentation-only public-release packaging tranche.

The operator request on 2026-05-08 accepts the WPR replacement roadmap and
starts WPR-1 first.

## Scope Lock

Allowed:

- Correct the W153-W160 rebuttal replacement packet so it reflects current
  state without overstating Codex's earlier assumptions.
- Create one stable contributor boundary reference for extension, template,
  provider-lane, skill, and guard authors.
- Cross-link the new reference from `README.md`, `CONTRIBUTORS.md`, and the
  reference docs index.
- Create WPR-1 roadmap and closure records.
- Run docs checks and the release gate.

Not allowed:

- Change runtime behavior, trusted-form corpus entries, provider behavior,
  governance policy, or CI hook behavior.
- Rewrite existing architecture, public claim, RC truth, or live evidence
  packets.
- Add a new provider lane, skill, template, or guard implementation.
- Touch frozen doctrine or legacy baseline roots outside documentation links.

## Exit Criteria

- `docs/reference/CVF_EXTENSION_AUTHOR_BOUNDARY.md` exists and is under 200
  lines.
- README and CONTRIBUTORS point contributor authors to the boundary reference.
- The Claude rebuttal replacement packet is corrected for WPR-3/WPR-4
  operational nuance.
- `git diff --check` passes.
- `python scripts/run_cvf_release_gate_bundle.py --json` passes.
