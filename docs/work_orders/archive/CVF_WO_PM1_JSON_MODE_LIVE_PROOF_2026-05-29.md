# CVF Work Order — PM-1 json_mode Live Proof

Memory class: FULL_RECORD

Status: HOLD_SOURCE_VERIFIED_PROOF_PATH_REQUIRED

docType: work_order

Date: 2026-05-29

---

## Purpose

Prepare live receipt evidence for `json_mode` method on DeepSeek
`deepseek-chat` and OpenAI `gpt-4o`. Produces structured evidence packets in
`docs/evidence/provider-methods/json-mode/`. Closes the `json_mode` half of
CVF 25.05 Gap 3.

`json_mode` is declared in `provider-capability-registry.ts` for both providers
but has no live receipt proof. D-wave used `complete` method only.

## Authority Chain

- PM GC-018: `docs/baselines/CVF_GC018_PROVIDER_METHOD_LIVE_PROOF_2026-05-29.md`
- PM Roadmap: `docs/roadmaps/CVF_PROVIDER_METHOD_LIVE_PROOF_ROADMAP_2026-05-29.md`
- Live run diagnostic standard: `docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`
- Capability registry source: `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`
  — `deepseek-chat` json_mode at line 80; `gpt-4o` json_mode at line 93
- Operator authorization: 2026-05-29 — "API Keys available in .env local,
  can use for testing at any time"

## Agent Roles

Implementer may proceed only after source-verifying an executable `json_mode`
path. After that gate, implementer makes 2 live calls (DeepSeek + OpenAI),
collects receipts, writes
evidence packets. Reviewer checks: `evidenceMode=live` on both receipts;
`rawSecretPrinted=false`; response validates as JSON; `http_status=200`.
Auditor confirms boundary: no provider routing change, no receipt envelope
extension. No self-review.

## Scope

**Allowed:**

- `docs/evidence/provider-methods/json-mode/deepseek-chat.md` (new)
- `docs/evidence/provider-methods/json-mode/gpt-4o.md` (new)
- `docs/reviews/CVF_PM1_JSON_MODE_LIVE_PROOF_COMPLETION_2026-05-29.md` (new)
- this work order (status update only)
- session continuity files

**Forbidden:** `EXTENSIONS/` source changes, receipt envelope schema change,
provider routing changes, `governance/` changes, public-sync repo.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`
   — mandatory before any live proof attempt
4. `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`
   — confirm `deepseek-chat` json_mode at line 80; `gpt-4o` json_mode at line 93
5. `docs/baselines/CVF_GC018_PROVIDER_METHOD_LIVE_PROOF_2026-05-29.md`
   — confirm authorization scope

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `json_mode` method name | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | line 12 | `json_mode` | `ProviderMethodName` | ACCEPT |
| `deepseek-chat` model id | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | line 79 | `deepseek-chat` | deepseek provider entry | ACCEPT |
| `deepseek-chat` supports `json_mode` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | line 80 | `json_mode` in supportedMethods | deepseek model capability | ACCEPT |
| `gpt-4o` model id | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | line 92 | `gpt-4o` | openai provider entry | ACCEPT |
| `gpt-4o` supports `json_mode` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | line 93 | `json_mode` in supportedMethods | openai model capability | ACCEPT |
| Live run diagnostic standard | `docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md` | full document | diagnostic classification guide | CVF live run standard | ACCEPT |
| PM-1 GC-018 authorization | `docs/baselines/CVF_GC018_PROVIDER_METHOD_LIVE_PROOF_2026-05-29.md` | full document | json_mode authorization | PM GC-018 | ACCEPT |
| Executable `json_mode` proof path | source path not yet verified | blocked before implementation | method-specific runtime path | provider method execution path | BLOCKED_SOURCE_NOT_FOUND |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| json_mode evidence packets per provider | Scope | 2 `.md` packets | Reviewer checks `evidenceMode=live` | OPEN |
| Live receipt on each call | Evidence Requirements | receipt_id in each packet | `rawSecretPrinted=false` | OPEN |
| JSON response validation | Evidence Requirements | response validates as JSON | packet documents validation | OPEN |
| No provider routing change | Scope Forbidden | git diff | `git diff --name-only` | OPEN |
| Executable `json_mode` proof path source-verified | Pre-Dispatch | current runtime path | Generic `/api/execute` receipt is insufficient | BLOCKED |

## Evidence Packet Structure

Each packet at `docs/evidence/provider-methods/json-mode/<model>.md` must
follow this template:

```
# Provider Method Evidence — json_mode / <provider> / <model>

Date: 2026-05-29
Method: json_mode
Provider: <provider>
Model: <model>
Risk level: R1
rawSecretPrinted: false

## Input

<describe payload — schema-constrained JSON request; no raw keys>

## CVF Policy Applied

cvfRiskLevel: R1
Guard contract result: ALLOW / BLOCK / CLARIFY

## Output

http_status: 200
duration_ms: <value>
response_validates_as_json: true / false
receipt_id: <rcpt-env-...>

## Verdict

PASS / FAIL

## Limitation Notes

<boundary note: e.g. "bounded to single json_mode call; not broad stability claim">
```

## Pre-Flight

- [ ] Working tree clean
- [ ] All required first reads done
- [ ] Executable `json_mode` proof path source-verified; generic `/api/execute` receipt not accepted as method proof

## Write Ownership

Implementer owns all new files. No file outside the Allowed list may be modified.

## Execution Plan

1. Read all required first reads and live run diagnostic standard.
2. Source-verify the executable method path before any live call. A generic
   `/api/execute` request with an unsourced `method` flag is not valid proof.
   Use the verified model-gateway adapter path or a separately authorized
   runtime change; otherwise return BLOCKED.
3. Record receipt_id, http_status, duration_ms for each call.
4. Classify any failure per live run diagnostic standard before re-attempting.
5. Write 2 evidence packets.
6. Write completion review.
7. Run governance gates.
8. Update session continuity.
9. Commit.

## Evidence Requirements

- 2 evidence packets with `evidenceMode=live` receipt ids
- `rawSecretPrinted=false` on both
- JSON response validated (response is parseable JSON, not free-form text)
- `http_status=200` on both (or FAIL documented with diagnostic class)
- No provider routing change in diff
- No `EXTENSIONS/` source file modified
- Source-verified evidence that the live call actually executed `json_mode`

## Acceptance Criteria

- [ ] `docs/evidence/provider-methods/json-mode/deepseek-chat.md` created
- [ ] `docs/evidence/provider-methods/json-mode/gpt-4o.md` created
- [ ] Both packets have live receipt ids and `rawSecretPrinted=false`
- [ ] JSON validation documented in each packet
- [ ] No code file in diff
- [ ] Method-specific executable proof path cited in each packet
- [ ] Session continuity updated

Fail conditions:
- `rawSecretPrinted=true` anywhere
- Receipt id is synthetic/placeholder rather than live
- Provider routing or EXTENSIONS/ source modified
- Evidence relies only on generic `/api/execute` with an unverified `method` flag

## Review Gate

Both packets present; `evidenceMode=live`; `rawSecretPrinted=false`; JSON
response validated; no code file; no provider routing change.

## Closure Checklist

- [ ] 2 evidence packets created with live receipts
- [ ] `rawSecretPrinted=false` on both
- [ ] JSON validation documented
- [ ] No EXTENSIONS/ source modified
- [ ] Completion review written
- [ ] Governance gates PASS
- [ ] Session continuity updated

## Return-To-Orchestrator Conditions

Stop if: executable `json_mode` proof path cannot be source-verified; live run
fails 2× with non-retryable diagnostic class; API key is
invalid or quota exhausted; `json_mode` method returns non-JSON response that
cannot be classified as provider behavior gap.

## PM-2 Gate Output

Was streaming method confirmed as next viable proof target?

**Expected YES:** Registry confirms Alibaba qwen-turbo supports `stream` at
line 52. PM-2 targets that pair. No PM-1 completion dependency for PM-2
dispatch — PM-2 can proceed after PM-1 CLOSED_PASS.

## Operator Checkpoint

Operator has authorized live API key use 2026-05-29. No additional checkpoint
required for standard R1 calls.

## Claim Boundary

PM-1 produces bounded evidence for `json_mode` method on 2 providers. It does
not claim broad json_mode stability, all-model support, provider routing
changes, receipt envelope extension, hosted readiness, production readiness,
or public release readiness.
