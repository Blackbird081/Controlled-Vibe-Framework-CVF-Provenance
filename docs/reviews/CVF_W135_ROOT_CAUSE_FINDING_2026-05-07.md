<!-- Memory class: FULL_RECORD -->
# CVF W135 Root Cause Finding — Competitor Review Output Validation

**Date:** 2026-05-07  
**Tranche:** W135-T1 — Post-AI Output Validation False-Positive Hardening

## Finding

The W134 Alibaba residual `competitor_review` HTTP 422 was a post-AI output
validation false positive, not a provider-routing or pre-AI governance failure.

The route returned:

- HTTP status: 422
- enforcement: ALLOW
- output validation issue: `UNSAFE_CONTENT`
- evidence receipt decision: BLOCK

## Root Cause

The trusted `competitor_review` template output shape included this line:

```text
- How to exploit:
```

The output validator also treated standalone `exploit` as unsafe content. That
made normal competitor-analysis language collide with the safety detector.

## Fix

- Reworded the template output shape from `How to exploit` to `How to capture`.
- Made the output validator context-aware for ambiguous terms such as
  `exploit`, `inject`, and `hack`; these now require nearby technical-abuse
  context such as CVE, SQL, XSS, token, auth, payload, endpoint, or
  vulnerability.
- Preserved destructive-command, exposed-credential, and technical exploit
  detection.

## Boundary

This finding only addresses W135's `competitor_review` HTTP 422 false positive.
It does not close the W134 execute-route timeout residuals.
