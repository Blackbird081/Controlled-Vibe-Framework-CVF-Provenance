# CVF GC-018 - W149-T1 Authorization

> Date: 2026-05-08
> Tranche: W149-T1 - Trusted Form Full-Corpus Live Value Gate
> Status: AUTHORIZED

## Decision

**AUTHORIZED.** W149-T1 may begin immediately.

W149 is authorized because W142-W147 expanded `TRUSTED_FORM_MAP` from the
original W126 trusted subset to the full non-wizard form corpus, and W148 closed
lint to `0 errors / 0 warnings`. That routing expansion is unit-clean, but the
stronger product claim that the expanded trusted-form surface is live-usable for
non-coders requires provider-backed evidence.

## Scope Lock

W149 is limited to:

- Locking the 40 trusted-form corpus and its prompt expectations.
- Running a live Alibaba direct `/api/execute` matrix for all 40 forms.
- Running a live Alibaba browser UI matrix for all 40 forms with route and
  request-lifecycle diagnostics.
- Running a DeepSeek confirmatory subset if the local key is available.
- Publishing evidence and a claim boundary that distinguishes live-proven,
  routed-only, and needs-hardening templates.
- Running the release gate after evidence is collected.

W149 must not:

- Add new trusted forms.
- Change provider behavior or bypass CVF governance.
- Claim provider parity.
- Promote CVF ADD private files or reopen CVF ADD absorption.
- Print or commit raw provider keys.

## Closure Criteria

W149 may close when:

- The corpus lock records exactly 40 trusted-form entries.
- Alibaba direct API matrix attempts all 40 forms and reaches at least `34/40`
  accepted with governance evidence receipts, or classifies each failure.
- Alibaba UI matrix attempts all 40 forms and records no wizard-shadow or
  execute-request-not-sent recurrence above the release threshold.
- DeepSeek confirmatory subset reaches at least `8/12` if `DEEPSEEK_API_KEY` is
  available; otherwise it must be recorded as skipped, not failed.
- Release gate bundle passes:

```bash
python scripts/run_cvf_release_gate_bundle.py --json
```
