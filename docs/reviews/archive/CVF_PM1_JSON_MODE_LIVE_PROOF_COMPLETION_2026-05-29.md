# CVF PM-1 json_mode Live Proof — Completion Review

Memory class: FULL_RECORD

Status: CLOSED_PASS

docType: completion_review

Date: 2026-05-29

---

## Purpose

Completion review for PM-1 json_mode Live Proof. Verifies live json_mode
evidence packets for DeepSeek deepseek-chat and OpenAI gpt-4o.

## Artifacts Delivered

| Artifact | Path | Status |
| --- | --- | --- |
| Live proof script | `scripts/run_pm1_json_mode_live_proof.py` (new) | CLOSED_PASS |
| DeepSeek evidence | `docs/evidence/provider-methods/json-mode/deepseek-chat.md` (new) | CLOSED_PASS |
| OpenAI evidence | `docs/evidence/provider-methods/json-mode/gpt-4o.md` (new) | CLOSED_PASS |
| Raw results | `docs/evidence/provider-methods/json-mode/pm1-live-results.json` (new) | CLOSED_PASS |

## Live Receipts

| Provider | Model | HTTP Status | Receipt ID | Decision |
| --- | --- | --- | --- | --- |
| DeepSeek | deepseek-chat | 200 | rcpt-pm1-deepseek-9bef6e2a3cbd | ALLOW |
| OpenAI | gpt-4o | 200 | rcpt-pm1-openai-15cc031a716b | ALLOW |

Both receipts:
- `evidenceMode=live`
- `rawSecretPrinted=false`
- Response validated as parseable JSON

## Changed Files

```
A  scripts/run_pm1_json_mode_live_proof.py
A  docs/evidence/provider-methods/json-mode/deepseek-chat.md
A  docs/evidence/provider-methods/json-mode/gpt-4o.md
A  docs/evidence/provider-methods/json-mode/pm1-live-results.json
```

## PM-2 Gate Output

PM-2 (streaming) is authorized to proceed. PM-2 requires Alibaba qwen-turbo
streaming with SSE response capture.

## Claim Boundary

PM-1 proves json_mode on two specific providers with two bounded live calls.
It does not claim: all-provider json_mode stability, schema-contract enforcement,
production throughput, or broad provider method parity.
