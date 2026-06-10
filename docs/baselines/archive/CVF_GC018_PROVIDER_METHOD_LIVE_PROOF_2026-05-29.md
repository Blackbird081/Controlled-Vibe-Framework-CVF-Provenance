# CVF GC-018 — Provider Method Live Proof

Memory class: FULL_RECORD

Status: ACTIVE

docType: gc018_baseline

Date: 2026-05-29

---

## Purpose

Authorize Provider Method Live Proof tranches PM-1 (json_mode), PM-2
(streaming), PM-3 (tool_call). Closes CVF 25.05 Gop_y.md Gap 3: provider
method contracts are schema-defined; no structured live evidence packets exist
beyond `complete` method already proven in D-wave.

Operator direction 2026-05-29: API keys for Alibaba, DeepSeek, OpenAI are
available locally in `.env`; may be used for testing at any time.

---

## Scope

Three live-proof evidence collection tranches:

- PM-1 — json_mode live proof (DeepSeek deepseek-chat + OpenAI gpt-4o)
- PM-2 — streaming live proof (Alibaba qwen-turbo)
- PM-3 — tool_call boundary documentation (no provider currently supports
  tool_call in CVF registry; PM-3 documents this gap formally and defines
  the unlock path)

Each tranche produces: evidence packet(s) in `docs/evidence/provider-methods/`,
GC-018 reference, work order, completion review. No runtime code change required
for PM-1/PM-2. PM-3 is documentation-only (tool_call unsupported in current
registry).

---

## Source / Predecessor Evidence

- Provider capability registry:
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`
  — `json_mode` at lines 80, 93; `stream` at line 52; `tool_call` declared
    at line 10 but absent from all `supportedMethods` arrays
- W5 completion: `docs/reviews/CVF_W5_PROVIDER_METHOD_FALLBACK_NORMALIZATION_COMPLETION_2026-05-24.md`
- D-wave provider scale proof: `docs/reviews/archive/CVF_D_PROVIDER_SCALE_LIVE_VI_PROOF_COMPLETION_2026-05-25.md`
  — proves `complete` method on DeepSeek + OpenAI; does NOT cover json_mode/stream
- CVF 25.05 review: `.private_reference/legacy/CVF 25.05/CLAUDE_REVIEW_OF_GOP_Y_2026-05-25.md`
  — GAP 3 section
- Provider Method Live Proof Roadmap:
  `docs/roadmaps/CVF_PROVIDER_METHOD_LIVE_PROOF_ROADMAP_2026-05-29.md`

Confirmed provider/method pairs at HEAD `a8d2a0eb`:

| Provider | Model | Method | Registry line | Status |
| --- | --- | --- | --- | --- |
| deepseek | deepseek-chat | json_mode | line 80 | Supported — no live receipt yet |
| openai | gpt-4o | json_mode | line 93 | Supported — no live receipt yet |
| alibaba | qwen-turbo | stream | line 52 | Supported — no live receipt yet |
| (none) | (none) | tool_call | line 10 type only | Declared but unsupported in all models |

---

## Decision / Baseline

PM-1, PM-2, PM-3 are authorized. PM-1 and PM-2 require live API calls using
existing keys plus a source-verified executable method path. A generic
`/api/execute` receipt is not valid method proof unless the route is
source-verified to execute the named method. PM-3 is documentation-only (gap
boundary record).

Sequencing: PM-1 → PM-2 → PM-3.

Blocked-work-class list in `ACTIVE_SESSION_STATE.json` remains in force.
This authorization does not lift any governance boundary around memory
reinjection, new receipt envelope schema, or provider routing changes.

---

## Required Evidence Per Tranche

Each evidence packet must contain:

- `provider` and `model`
- `method` tested
- `input` payload description (secret-safe, no raw API key)
- CVF `cvfRiskLevel` applied
- `receipt_id` (from live call)
- `http_status` and `duration_ms`
- `pass_fail` verdict
- `limitation` notes
- `rawSecretPrinted: false` assertion

Live diagnostic standard: `docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`

---

## Verification

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base a8d2a0eb --head <pm-commit> --enforce
python governance/compat/check_markdown_structural_completeness.py --base a8d2a0eb --head <pm-commit> --enforce
```

---

## Claim Boundary

This GC-018 authorizes bounded evidence collection for three specific method/
provider pairs. It does not claim broad provider stability, universal method
support, new provider adapters, route behavior changes, hosted readiness,
production readiness, or public release readiness.
