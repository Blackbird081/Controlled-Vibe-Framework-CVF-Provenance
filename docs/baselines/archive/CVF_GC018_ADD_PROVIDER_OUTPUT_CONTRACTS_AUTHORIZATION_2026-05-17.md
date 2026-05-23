Memory class: SUMMARY_RECORD

# CVF GC-018 ADD Provider Output Contracts Authorization - 2026-05-17

Status: AUTHORIZED FOR LOCAL IMPLEMENTATION.

## Purpose

Authorize CD-3 Step 5 from the final unabsorbed-knowledge consensus roadmap:
absorb the provider/runtime output contract patterns from the OpenRouter CLI
reference into the CVF Model Gateway.

## Scope

Owner surface:

- `EXTENSIONS/CVF_MODEL_GATEWAY/`

Permitted implementation:

- machine-readable provider output envelope parsing;
- newline-delimited stream chunk parsing;
- stdout/stderr boundary validation;
- provider exit-code classification;
- tests for malformed, retryable, and contract-violation cases.

## Source

- `.private_reference/legacy/CVF ADD/openrouter-cli.git/execution/command_runtime/`
- `docs/roadmaps/CVF_UNABSORBED_KNOWLEDGE_FINAL_CONSENSUS_ROADMAP_2026-05-17.md`

## Decision

Approved direction: implement provider output contracts in the existing Model
Gateway as interpretation primitives, not as a new provider adapter.

## Non-Goals

- no new provider;
- no direct OpenRouter integration;
- no provider routing change;
- no live provider claim;
- no public output-quality claim.

## Evidence / Verification

Required before closure:

- Model Gateway typecheck;
- focused tests for JSON envelope parsing, NDJSON stream parsing, stdout
  policy rejection, and exit-code classification.

## Claim Boundary

This authorization standardizes how provider command output is interpreted by
CVF. It does not change which provider is selected or how providers execute.
