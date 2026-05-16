<!-- Memory class: SUMMARY_RECORD -->

# CVF Controlled Memory Source Adoption Matrix - 2026-05-16

Status: ACCEPTED SOURCE MAPPING.

## Purpose

Map the reusable `agentmemory` source drafts into the CVF Controlled Memory
runtime tranche.

## Source

Source folder:

- `.private_reference/legacy/CVF 16.5/agentmemory/`

## Baseline

| Source file | Adopted value | CVF runtime representation | Disposition |
|---|---|---|---|
| `CVF_CONTROLLED_MEMORY_GATEWAY.md` | single governed memory gateway | `ControlledMemoryGatewayContract` | adopted |
| `CVF_MEMORY_ACCESS_POLICY.md` | actor/scope/sensitivity access gate | `ControlledMemoryPolicyContext` | adopted |
| `CVF_MEMORY_CAPTURE_ADAPTER.md` | event-to-memory capture | `capture()` | adopted |
| `CVF_MEMORY_CONTEXT_PACKAGER.md` | packaged context, no raw dump | `ControlledMemoryContextSegment` | adopted |
| `CVF_MEMORY_EVENT_HOOKS.md` | source event lineage | `sourceEvent`, `sourcePath`, provenance | adopted |
| `CVF_MEMORY_GUARD_CONTRACT.md` | fail-closed policy result | `policyResult` deny/approval behavior | adopted |
| `CVF_MEMORY_LIFECYCLE_POLICY.md` | active/stale/expired/blocked/contradicted | `ControlledMemoryLifecycleState` | adopted |
| `CVF_MEMORY_PRIVACY_FILTER_POLICY.md` | PII/secret masking before persistence | `ControlledMemoryPrivacyReport` | adopted |
| `CVF_MEMORY_REINJECTION_PROTOCOL.md` | explicit reinjection authorization | `reinject()` | adopted |
| `CVF_MEMORY_RETRIEVAL_POLICY.md` | scoped/budgeted retrieval | `retrieve()` | adopted |

## Evidence

Runtime evidence:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled.memory.gateway.contract.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/controlled.memory.gateway.contract.test.ts`

## Verification

The focused test covers policy denial, approval pause, restricted memory,
privacy masking, lifecycle filtering, token budget, and reinjection packaging.

## Claim Boundary

CVF absorbed the memory-governance pattern. CVF did not adopt `agentmemory` as a
runtime dependency or public product claim.
