# CVF Work Order — PM-2 Streaming Live Proof

Memory class: FULL_RECORD

Status: HOLD_UNTIL_PM1_PASS_AND_SOURCE_VERIFIED_PROOF_PATH

docType: work_order

Date: 2026-05-29

---

## Purpose

Prepare live receipt evidence for `stream` method on Alibaba `qwen-turbo`.
Produces evidence packet in `docs/evidence/provider-methods/streaming/`.
Closes the streaming half of CVF 25.05 Gap 3.

`stream` is declared in `provider-capability-registry.ts` for `qwen-turbo`
at line 52 but has no live receipt proof. The existing Alibaba receipts in CVF
all use `complete` method.

## Authority Chain

- PM GC-018: `docs/baselines/CVF_GC018_PROVIDER_METHOD_LIVE_PROOF_2026-05-29.md`
- PM Roadmap: `docs/roadmaps/CVF_PROVIDER_METHOD_LIVE_PROOF_ROADMAP_2026-05-29.md`
- Live run diagnostic standard: `docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`
- Capability registry: `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`
  — qwen-turbo stream at line 52
- **PM-1 gate: `docs/reviews/CVF_PM1_JSON_MODE_LIVE_PROOF_COMPLETION_2026-05-29.md`
  must be CLOSED_PASS before dispatch**

## Agent Roles

Implementer may proceed only after source-verifying an executable streaming
path for this provider/model. After that gate, implementer makes 1 live
streaming call (Alibaba qwen-turbo), collects first-token receipt, writes
evidence packet. Reviewer checks: `evidenceMode=live`;
`rawSecretPrinted=false`; streaming tokens received; `http_status=200`.
No self-review.

## Scope

**Allowed:**

- `docs/evidence/provider-methods/streaming/qwen-turbo.md` (new)
- `docs/reviews/CVF_PM2_STREAMING_LIVE_PROOF_COMPLETION_2026-05-29.md` (new)
- this work order (status update only)
- session continuity files

**Forbidden:** `EXTENSIONS/` source changes, receipt envelope schema, provider
routing changes, `governance/` changes, public-sync repo.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`
4. `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`
   — confirm qwen-turbo stream at line 52
5. `docs/reviews/CVF_PM1_JSON_MODE_LIVE_PROOF_COMPLETION_2026-05-29.md`
   — confirm PM-1 CLOSED_PASS (gate check)

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `stream` method name | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | line 9 | `stream` | `ProviderMethodName` | ACCEPT |
| `qwen-turbo` model id | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | line 51 | `qwen-turbo` | alibaba provider entry | ACCEPT |
| `qwen-turbo` supports `stream` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | line 52 | `stream` in supportedMethods | alibaba model capability | ACCEPT |
| Live run diagnostic standard | `docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md` | full document | diagnostic classification guide | CVF live run standard | ACCEPT |
| PM GC-018 authorization | `docs/baselines/CVF_GC018_PROVIDER_METHOD_LIVE_PROOF_2026-05-29.md` | full document | stream authorization | PM GC-018 | ACCEPT |
| Executable `stream` proof path | source path not yet verified | blocked before implementation | method-specific runtime path | provider method execution path | BLOCKED_SOURCE_NOT_FOUND |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| streaming evidence packet | Scope | 1 packet | `evidenceMode=live` | OPEN |
| first-token receipt | Evidence Requirements | receipt_id in packet | `rawSecretPrinted=false` | OPEN |
| streaming tokens documented | Evidence Requirements | token count or stream chunks noted | packet documents stream behavior | OPEN |
| PM-1 gate confirmed | Authority Chain | PM-1 completion review | Read PM-1 review | OPEN |
| Executable `stream` proof path source-verified | Pre-Dispatch | current runtime path | Generic `/api/execute` receipt is insufficient | BLOCKED |

## Evidence Packet Structure

`docs/evidence/provider-methods/streaming/qwen-turbo.md`:

```
# Provider Method Evidence — stream / alibaba / qwen-turbo

Date: 2026-05-29
Method: stream
Provider: alibaba
Model: qwen-turbo
Risk level: R1
rawSecretPrinted: false

## Input

<payload description — streaming request; no raw keys>

## CVF Policy Applied

cvfRiskLevel: R1
Guard contract result: ALLOW

## Output

http_status: 200
duration_ms: <first-token latency>
streaming_tokens_received: <count or first N chars>
receipt_id: <rcpt-env-...>

## Verdict

PASS / FAIL

## Limitation Notes

Bounded to single stream call on qwen-turbo; not broad streaming stability.
SSE stream response captured; full response not stored.
```

## Pre-Flight

- [ ] Working tree clean
- [ ] All required first reads done
- [ ] PM-1 gate and executable `stream` proof path checked

## Write Ownership

Implementer owns all new files. No file outside the Allowed list may be modified.

## Review Gate

Before committing: all source symbols verified; required evidence present; no forbidden files in diff.

## Execution Plan

1. Read all required first reads; confirm PM-1 gate.
2. Classify any prior diagnostic before attempting.
3. Source-verify the executable method path before any live call. A generic
   `/api/execute` request with an unsourced `method` flag is not valid proof.
   Use the verified model-gateway adapter path or a separately authorized
   runtime change; otherwise return BLOCKED.
4. Capture first-token latency, receipt_id, http_status.
5. Write evidence packet.
6. Write completion review.
7. Run governance gates.
8. Update session continuity.
9. Commit.

## Evidence Requirements

- 1 evidence packet with `evidenceMode=live` receipt id
- `rawSecretPrinted=false`
- Streaming tokens received and documented
- `http_status=200` (or FAIL with diagnostic class)
- Source-verified evidence that the live call actually executed `stream`
- No EXTENSIONS/ source modified

## Acceptance Criteria

- [ ] PM-1 CLOSED_PASS confirmed
- [ ] `docs/evidence/provider-methods/streaming/qwen-turbo.md` created
- [ ] Live receipt id present; `rawSecretPrinted=false`
- [ ] Streaming behavior documented
- [ ] Method-specific executable proof path cited in the packet
- [ ] No code file in diff
- [ ] Session continuity updated

## Closure Checklist

- [ ] PM-1 confirmed
- [ ] Evidence packet created with live receipt
- [ ] `rawSecretPrinted=false`
- [ ] Completion review written
- [ ] Governance gates PASS
- [ ] Session continuity updated

## Return-To-Orchestrator Conditions

Stop if: PM-1 gate not confirmed; executable `stream` proof path cannot be
source-verified; streaming API not supported by current route implementation;
failure classified as non-retryable after 2 attempts.

## PM-3 Gate Output

Is `tool_call` viable as a live proof target?

**Expected NO:** Registry declares `tool_call` at line 10 as a method type
but no provider/model in `supportedMethods` arrays includes it. PM-3 should
be a boundary documentation tranche, not a live proof tranche, until a
provider with tool_call support is added to the registry.

## Operator Checkpoint

operator.checkpoint.waiver: R1 live call; operator authorized API use.

## Claim Boundary

PM-2 produces bounded streaming evidence for Alibaba qwen-turbo. It does not
claim broad streaming stability, all-provider support, SSE route implementation,
hosted readiness, or public release readiness.
