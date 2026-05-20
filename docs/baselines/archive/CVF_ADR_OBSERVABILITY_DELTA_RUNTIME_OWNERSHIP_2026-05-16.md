Memory class: SUMMARY_RECORD

# CVF ADR Observability Delta Runtime Ownership - 2026-05-16

Status: ACCEPTED.

## Purpose

Record the ownership decision for adopting Observability Delta knowledge into
CVF as executable observe-only runtime behavior.

## Scope

This ADR covers the first bounded Observability Delta tranche inside:

- `EXTENSIONS/CVF_v1.8.1_ADAPTIVE_OBSERVABILITY_RUNTIME/`

## Context

`abtop` defines an observability plane that monitors agent sessions, token and
context pressure, rate limits, process/port state, dashboard streams, and UI
contracts.

CVF already has an Adaptive Observability Runtime. The high-fit absorption is a
delta to that owner surface, not a new independent runtime plane.

## Decision

Implement a CVF-owned `observe.only.signal.contract` in the existing
observability runtime.

The contract owns:

- token/context usage threshold mapping;
- trusted measurement-source boundary;
- provider rate/quota pressure mapping;
- process/port anomaly mapping;
- deterministic observability receipt creation;
- explicit intervention blocking.

## Alternatives

Alternative 1: copy the full `abtop` plane into CVF.

Rejected because CVF already owns an observability runtime and should absorb the
behavior as a delta, not duplicate a plane.

Alternative 2: let observability perform corrective actions directly.

Rejected because the source boundary says observability may observe, summarize,
alert, emit receipts, and recommend escalation, but must not approve, kill,
reroute, mutate policy, truncate context, or inject prompts.

Alternative 3: keep the material as docs-only.

Rejected because the operator requires selected high-fit absorption lanes to
become alive inside CVF.

## Consequences

Positive:

- CVF now has tested token/context pressure thresholds;
- untrusted token estimates are flagged;
- rate/quota and process/port risks become deterministic signals;
- receipts show what observability can and cannot do.

Costs:

- this is local deterministic signal behavior, not live dashboard streaming;
- no process or provider intervention is claimed.

## Verification

Verification must include:

- Adaptive Observability package typecheck;
- focused vitest coverage for observe-only signals;
- governance markdown and file-size checks before commit;
- full pre-push chain before provenance push.

## Claim Boundary

This ADR claims runtime ownership of observe-only signal behavior. It does not
claim live provider routing, process control, dashboard streaming, or governance
enforcement through observability alone.
