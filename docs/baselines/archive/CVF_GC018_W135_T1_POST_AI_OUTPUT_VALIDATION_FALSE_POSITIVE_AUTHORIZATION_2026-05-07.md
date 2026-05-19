# CVF GC-018 — W135-T1 Authorization

> Date: 2026-05-07  
> Tranche: W135-T1 — Post-AI Output Validation False-Positive Hardening  
> Status: AUTHORIZED

## Decision

**AUTHORIZED.** W135-T1 may begin immediately.

W135 is authorized because W134 closed the pre-AI HTTP 400 blocker but surfaced
a distinct residual failure: `competitor_review` can reach enforcement ALLOW and
provider execution, then return HTTP 422 after output validation retries due to
an `UNSAFE_CONTENT` false positive.

## Scope Lock

W135 is limited to:

- Removing self-conflicting unsafe wording from the trusted
  `competitor_review` template output shape.
- Making output validation context-aware for ambiguous business terms such as
  `exploit`, while preserving blocks for technical abuse content.
- Adding targeted regression coverage for both safe business usage and unsafe
  security-abuse usage.
- Running one targeted live `competitor_review` proof on Alibaba.

W135 must not:

- Disable output validation globally.
- Remove credential/destructive-command detection.
- Add new trusted forms or broaden noncoder claims beyond the tested path.
- Treat the W134 timeout residuals as solved unless separately proven.
- Print or commit raw provider keys.

## Closure Criteria

W135 can close as delivered only when:

- Targeted unit coverage proves safe competitor-analysis language is not flagged
  as `UNSAFE_CONTENT`.
- Targeted unit coverage proves technical exploit/credential/destructive-command
  content is still flagged.
- A live Alibaba `competitor_review` request returns a governance receipt without
  HTTP 422 output-validation exhaustion.
