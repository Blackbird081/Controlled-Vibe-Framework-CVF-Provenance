# NCR - Intake Dispatch Repair

Memory class: FULL_RECORD
docType: baseline
Status: LOCAL_REPAIR_EVIDENCE_BOUNDED
Date: 2026-10-07

## Purpose

Finish the admitted initial-send and live-env defects together for the full-mode
INTAKE candidate reviewer. Existing continuation owner is
docs/baselines/CVF_GC018_NCR_LOCAL_CONSUMER_CONTINUATION_2026-10-07.md.
That owner is near its1000-line limit; this is its bounded continuation,
not a new program,work order,checker or pilot. Decision owner Local.

## Scope / Target / Owner Boundary

Operator next and standing Alibaba-only test authority; Local maintainer/reviewer,
no delegation or independent-oracle claim. Clean base 41e0d9f67f414a22cdbc5e24f275d09e053ba3b4.
Exact nine material paths fixed in the operation trace. Compatible scope extension
adds existing history initializer before edit to eliminate transient session mounts.
Outputs: session-bound dispatch,timer cleanup,Next env parity,focused regressions,
selected real-provider result and continuity. Stop at those outputs.
No guard bypass,credential edit,cap increase,model/default selection or phase approval.

## Source Verification Block

| Source | Disposition | Finding |
|---|---|---|
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/AgentChatWithHistory.tsx | ACCEPT | Current source at admission and final repaired bytes bound in companion |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/AgentChatWithHistory.test.tsx | ACCEPT | Current source at admission and final repaired bytes bound in companion |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/hooks/useAgentChat.ts | ACCEPT | Current source at admission and final repaired bytes bound in companion |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/hooks/useAgentChat.test.ts | ACCEPT | Current source at admission and final repaired bytes bound in companion |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/playwright.config.ts | ACCEPT | Current source at admission and final repaired bytes bound in companion |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/chat-history.tsx | ACCEPT | Current source at admission and final repaired bytes bound in companion |

## Source Runtime Freshness Verification

Targeted current reads of history wrapper,initializer,send hook,Playwright env
loader and rate limiter at the clean admission base. Previous live proof retained
two identical client requests132ms apart and API429 before dispatch.
Raw quoted Redis URL was invalid; Next-parsed URL valid,token outer quotes removed,
injected port preserved. Only secret-safe booleans retained,not credentials.
No assertion about real Redis availability follows from URL syntax alone.

## Decision / Implementation

Incoming brief session is created atomically by existing history state initializer.
Chat mounts only with a ready session; initial prompt belongs to that session,
and is omitted after history records messages. Other/new/historical chats do not
inherit that initial prompt. Ordinary empty-history recovery remains supported.
Initial-send timer marks handled only on dispatch and cleans up on unmount or
dependency replacement; StrictMode cleanup/reschedule retains exactly one send.
Playwright uses existing Next env loader for quotes,expansion and precedence.
Rate limiter,Redis backend,quotas,auth,provider and token caps are untouched.

## Evidence / Verification

Initial attempted red run hit Vitest worker startup timeout:no tests started.
Original runtime bytes subsequently exercised against new regressions in one
thread worker:3 failed,17 passed;two session-dispatch cases and unmount cancellation
failed for the expected reasons. Final bytes restored exactly before live effects.
Final focused45 tests PASS across wrapper,send hook and existing history suite.
Mocks isolate provider/enforcement in these hermetic tests;they are not live proof.
Final scoped lint and TypeScript noEmit PASS. No duplicate build/scan/SOT3 replay.
One selected Alibaba-only live invocation exit0,elapsed74875ms.

| Selected case | Status | Duration ms |
|---|---|---|
| full-mode API returns a governed live result and receipt | passed | 50753 |
| full-mode Idea Brief export reaches the client INTAKE gate on real Alibaba output | passed | 12298 |

Disposition: PASS. Exact safe attachments,source Git-normalized hashes,
command/results and ignored runtime artifact hashes in
docs/reviews/evidence/cvf-local-candidate-release-2026-10-07.json intakeDispatchRepair20261007.
Client UI proof is separate from server envelope/receipt;no DESIGN/BUILD approval.
Initial packaging gates rejected missing encoding exception and corpus verdict
bullet. Repairs add a bilingual-label exception comment and correct N/A syntax.
Post-live hook transpilation with comments removed matches execution source;
comment lint PASS,no provider replay. Execution and final identities are qualified.
Verified generated Next include additions restored;historical tracked reports untouched.
Earlier full-mode and original canonical bundle failures stay visible as history.
Selected PASS cannot replace a fresh canonical whole-bundle release gate.

## Epistemic Process Block

Expected Result / Prediction: source repairs eliminate orphan initial sends and
quoted-env rejection without weakening guards or single-send checks.
Evidence Comparison: original-source3 negatives and final45 passes; selected live
case statuses and safe attachments evaluated at recorded execution bytes.
Contradiction Or Gap Disposition: keep any selected failure,diagnose before replay;
do not turn client modal visibility into server receipt or phase progression proof.
Claim Update: PASS for this selected repair scope only; production,whole release
and general worker/reviewer lifecycle remain unproved.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | governance/compat/check_epistemic_process_packet.py; governance/compat/check_finding_to_governance_learning.py; governance/compat/check_markdown_structural_completeness.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_agent_packet_authority_and_encoding.py; governance/compat/check_agent_operation_trace.py; governance/compat/check_adif_defect_registry_disclosure.py; governance/compat/check_public_export_disposition.py; governance/compat/check_core_guard_self_protection.py; governance/compat/check_corpus_completeness_report_integrity.py |
| literalTokensReviewed | Source/Decision/Evidence/Claim Boundary; read-ahead fields; trace labels; Resolver query; Returned defects; Public Export Disposition |
| additionalCheckersRead | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_external_knowledge_intake_routing.py; governance/compat/check_raw_memory_release_invariant.py |
| gateRunPurpose | Confirm authored bounded scope and evidence; not first discovery of literals |
| claimBoundary | Structural packet admission only |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`review`, role=`reviewer`, lifecyclePhase=`review`

Returned defects: NONE_RETURNED. Zero candidates and no truncation.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local intake dispatch maintainer/reviewer |
| Provider or surface | Local canonical bundle; Alibaba-only synthetic live lane |
| Session or invocation | intake-dispatch-repair-20261007 |
| Working directory | repository root |
| Command or tool surface | original-source negatives;45 hermetic tests;typecheck/lint;two selected Alibaba live cases;governance gates |
| Target paths | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/AgentChatWithHistory.tsx; EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/AgentChatWithHistory.test.tsx; EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/hooks/useAgentChat.ts; EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/hooks/useAgentChat.test.ts; EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/playwright.config.ts; EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/chat-history.tsx; docs/baselines/CVF_GC018_NCR_LOCAL_CONSUMER_CONTINUATION_2026-10-07.md; docs/baselines/CVF_GC018_NCR_INTAKE_DISPATCH_REPAIR_2026-10-07.md; docs/reviews/evidence/cvf-local-candidate-release-2026-10-07.json |
| Allowed scope source | operator next,continuous Local work and Alibaba test authorization |
| Before status evidence | clean 41e0d9f67f414a22cdbc5e24f275d09e053ba3b4 |
| After status evidence | nine material paths;selected full-mode PASS;initial bundle FAIL preserved |
| Diff evidence | exact staged manifest;source Git hashes and runtime artifact hashes |
| Approval boundary | synthetic Local candidate proof; data/public/deploy effects parked |
| Claim boundary | current canonical Local observation;not remote CI,whole NCR or production acceptance |
| Agent type | INTERNAL_AGENT |
| Invocation ID | intake-dispatch-repair-20261007 |
| Expected manifest | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/AgentChatWithHistory.tsx; EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/AgentChatWithHistory.test.tsx; EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/hooks/useAgentChat.ts; EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/hooks/useAgentChat.test.ts; EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/playwright.config.ts; EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/chat-history.tsx; docs/baselines/CVF_GC018_NCR_LOCAL_CONSUMER_CONTINUATION_2026-10-07.md; docs/baselines/CVF_GC018_NCR_INTAKE_DISPATCH_REPAIR_2026-10-07.md; docs/reviews/evidence/cvf-local-candidate-release-2026-10-07.json |
| Actual changed set | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/AgentChatWithHistory.tsx; EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/AgentChatWithHistory.test.tsx; EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/hooks/useAgentChat.ts; EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/hooks/useAgentChat.test.ts; EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/playwright.config.ts; EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/chat-history.tsx; docs/baselines/CVF_GC018_NCR_LOCAL_CONSUMER_CONTINUATION_2026-10-07.md; docs/baselines/CVF_GC018_NCR_INTAKE_DISPATCH_REPAIR_2026-10-07.md; docs/reviews/evidence/cvf-local-candidate-release-2026-10-07.json |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |


## Next Allowed Move

Consume this repaired-source disposition and the existing candidate phase owners.
If a required selected case remains failed, use its diagnostic for a finite
compatible repair;no blind rerun or unrelated endpoint expansion.
Full release requires its canonical bundle under separate admitted scope.
Actual-data,R2/R3,P11,public and deployment checkpoints remain parked.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - targeted source/test inspection and
synthetic tests only; no full scan,inventory or all-files-read claim.

## Claim Boundary

Local selected synthetic proof only. No remote CI,real-data,whole-program closure,
production/public/deploy acceptance or independent reviewer guarantee.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
Reason: private Local repair/evidence. No public export,push or deployment.
