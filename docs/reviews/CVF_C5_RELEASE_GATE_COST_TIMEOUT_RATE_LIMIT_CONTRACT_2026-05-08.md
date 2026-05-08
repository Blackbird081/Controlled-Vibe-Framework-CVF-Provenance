<!-- Memory class: FULL_RECORD -->
# CVF C5 Release Gate Cost, Timeout, And Rate-Limit Contract

**Date:** 2026-05-08  
**Track:** RC2 Pre-GA / C5.1  
**Status:** ACCEPTED DESIGN INPUT  

## Contract

C5 implementation must enforce the following controls before Web can trigger
the full live release gate.

## Trigger Authorization

Allowed roles:

- `owner`;
- `admin`;
- `operator` mapped from current `developer` session role.

Blocked roles:

- `reviewer`;
- `viewer`;
- `anonymous_local`;
- unknown role;
- unknown auth mode.

## Local Concurrency

Only one active full release gate may run at a time on this local CVF
installation.

Do not use `workspace` or `org` semantics in the local C5 implementation. When
Track M2 later introduces managed multi-tenant scope, extend this rule to
workspace/org-scoped rate limits.

## Fixed Command

The only command allowed for the C5 job type is:

```bash
python scripts/run_cvf_release_gate_bundle.py --json
```

No browser-provided argv may be appended.

## Timeout

The full gate must use a bounded timeout. The implementation may expose a lower
timeout override only if it reduces the default, never expands it.

Minimum implementation default:

```text
timeoutMs = 900000
```

## Cost Warning

The Web UI must show explicit warning copy before trigger:

```text
This runs the full live release gate and may consume provider quota. It is not
a dry readiness check.
```

## Missing-Key Behavior

If no DashScope-compatible live key is available through accepted env aliases,
the job must fail closed and must not print key values.

Accepted aliases:

- `DASHSCOPE_API_KEY`;
- `ALIBABA_API_KEY`;
- `CVF_ALIBABA_API_KEY`;
- `CVF_BENCHMARK_ALIBABA_KEY`.

## Redaction Positive Test

C5.4 evidence must use this fake key value:

```text
test_invalid_cvf_redaction_probe_20260508
```

The value must not appear in:

- stdout;
- stderr;
- JSON result artifact;
- persisted Web job state;
- browser-visible API response;
- HAR/network capture or equivalent browser evidence.

## Claim Boundary

Allowed:

> C5 full live release-gate Web trigger controls are specified.

Forbidden:

- C5 runtime is implemented.
- Web can trigger the full release gate.
- Any PR CI run proves live governance.
