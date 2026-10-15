# NCR HTML Semantic State-Machine Design

Memory class: governed-design-baseline
docType: baseline
Status: ACTIVE_REFERENCE
Date: 2026-10-15
Batch ID: CVF-NCR-HTML-SEMANTIC-DESIGN-20261015
sourceHead: 5a18075c93d935d1cecf492dfde856c3566aa3f1
rawMemoryReleased=false
providerExecutionAuthority: FORBIDDEN

## Purpose

Lock one constructively achievable protocol for the same rejected HTML root
before preparing another source implementation order. This document resolves
phase admission, time ownership, in-flight uncertainty and child/parent evidence
ownership. It is a design reference, not an executable work order or new grant.

## Scope / Target / Owner Boundary

Local INTERNAL_AGENT owns design and technical disposition under operator next
and persistent Local maintenance authority. Two INTERNAL_AGENT advisers read
without Git/tests/writes. No source implementation, test-control program, actual
native/API/browser/product/network/delete or provider invocation is admitted.
The design uses existing owners; no new checker, hook, global schema or workflow.

## Source / Predecessor Evidence

Consume `docs/reviews/CVF_NCR_HTML_ROOT_RECOVERY_R4_COMPLETION_2026-10-15.md` and `docs/reviews/evidence/ncr-html-root-recovery-local-r4-20261015.json`:
17 completed independent assertions,7 PASS/10 FAIL; original114 Python/7 Node
and26 inert starts retained. The extra Local synthetic Node rejection is not a
product observation. R4 preparation and Local packaging/sync defects remain.

The restored six working files are pre-R4 source. Every R4 implementation fact
here names the rejected8 byte snapshots in Local proof, not those working files.
Proposed labels/fields/methods below are DOC_ONLY_NEW semantic requirements, not
current runtime symbols, canonical governance enums or implemented capabilities.
The companion binds exact source identities and observation IDs.

## Decision / Baseline

SPEC_LOCKED_FOR_PROSPECTIVE_SOURCE_WORK_ORDER; IMPLEMENTATION_NOT_RELEASED.
The admission cutoff closes new normal work. It cannot guarantee that a syscall,
native API, filesystem operation or pipe write already in flight physically
stops at that instant. Unobserved completion becomes UNKNOWN, cannot authorize
follow-on work and prevents acceptance. No claim of hard thread preemption.

Same root NCR_HTML_CONFIGURED_RECEIPT_CONTROL_PROOF, actual rework4/generation4
and finding digest35447819f0e8d9b8b07dcf461cac9db68d87f656726e83dd0fefa4f85d576ac4
remain. No new SCEC transition: ordinal2/counters2,0,2,0/two blockers/freeze and
retired profiles retained. R4 allowances are consumed historical evidence.

## Protocol / State Transitions

One parent monotonic owner controls phase, immutable work cutoff and operation
IDs/generation. Do not hold its admission lock across blocking I/O. Every normal
effect has a final admission check after preceding persistence/serialization.
Under the parent lock, this operation-specific grant atomically changes
revocable QUEUED to committed DISPATCHED. Release the lock before adapter
execution. Closing revokes QUEUED operations, but a committed operation remains
tracked even if closing precedes physical adapter entry. Unconfirmed completion
is UNKNOWN and prevents acceptance; admission does not promise hard preemption.

| State | Transition / allowed action | Failure postcondition |
|---|---|---|
| PREPARED | validate input/control/source; fix work cutoff; no effect before admission | no launch on invalid/missing prerequisites |
| WORK | reserve/debit; persist prelaunch evidence; sample fresh phase/time; admit one operation | failed persist or exhausted time prevents invocation/resume |
| CLOSING | irreversible fence on success, failure or expiry; revoke queued normal work before waits | no new normal admission or generation reuse |
| CLEANUP | one separate cutoff; only stop/query/close/joins/evidence within remainder | unresolved operation/action is UNKNOWN or not attempted; stage retained |
| TERMINAL_FROZEN | completed/failed/skipped/unknown outcomes serialized once | later completion cannot mutate bytes or clear uncertainty |
| ACKNOWLEDGED or UNKNOWN | exact write/readback plus separate acknowledgment tied to hash | missing/mismatch/timeout means not accepted |
| RETAINED | stage retained; model eligibility only if every required condition confirmed | actual deletion belongs to a future separately admitted action |

These are proposed source-policy states, not new SCEC or global CVF states.

## Time And Effect Requirements

Let workEnd be fixed at admitted start plus work allowance. At the first close
transition, set cleanupEnd=min(observedClose+cleanupAllowance,workEnd+cleanupAllowance)
once. Never overwrite workEnd or let cleanup renew normal work. The prior900/120
parameters may be carried into a prospective packet; they authorize no run here.

Sample a monotonic clock once per allowance computation. Return a finite,
strictly positive wait no greater than requested cap and current remainder.
At zero/exhaustion invoke nothing new. If an adapter requires integer units,
quantize down and refuse a sub-unit remainder; never turn it into unlimited0.
No minimum drain/teardown floor and no fresh per-step cleanup window.

Prelaunch persistence may itself block. After it returns, resample phase/time
before invocation. Native ordering is suspended create -> assign -> exact
identity -> persist identity -> fresh WORK check -> resume. At failed check,
do not resume; attempt only admitted cleanup of the exact owned handle.
Unknown completion codes are failures, not success. Original primary failures
survive later persistence failures; no repeat module query or fallback.

JS helpers receive lazy operations. Compute allowance before calling control,
browser setup/action, HTTP/body/download or teardown code. Passing an already
started Promise is not before-effect admission. A timeout limits the wait;
record whether cancellation was requested and whether completion was observed.
An unresolved operation remains UNKNOWN even if a later callback returns.

## Ingress, IPC And Cancellation Requirements

Fence normal ingress before waiting for proxy threads, closing listeners or
joining readers. A pending body does not reserve future forwarding authority.
Recheck phase/time after body acquisition and immediately before engine forward.
Proposed body cap64KiB is DOC_ONLY_NEW; reject invalid/oversized Content-Length
before allocation/read, and bound every read/chunk by the original work cutoff.

After a controller queue wait, recheck WORK before processing a normal line,
granting export or dispatching a reply. Replies still queued at CLOSING are
discarded. A write committed DISPATCHED is tracked as in flight, including
the interval before adapter entry: a timeout cannot certify that
its daemon thread was killed. Track its identity/outcome, fence follow-on work,
request bounded owned cancellation and keep UNKNOWN/retained-stage disposition.

Distinguish revocable queued work from a committed transport operation. Do
not promise physical prevention of every late frame or browser syscall. A stale
frame never grants new controller work; an unproven in-flight child effect
blocks acceptance. Child clocks are advisory and may only shorten waits;
startup delay or wall-clock rollback never extends parent authority. No assumed
shared parent/child clock origin. Actual cross-process cancellation/clock behavior
remains a future native/browser proof obligation, not a source-model result.

The existing entry wrapper passes a control callback and dynamic helper path.
Its controlChannel prefix check is transport handling, not reply authenticity.
The helper must validate complete reply identity/generation/operation, including
unexpected tails. Implement this inside the admitted helper family; both legacy
entrypoint files remain read-only in the proposed source phase.

Cleanup begins with fence/cancellation requests to owned work, then bounded
stop/query/joins/custody as permitted. The admission lock cannot be blocked by
a pipe writer or a slow filesystem call. Track pending operations separately
from completed actions; timed-out/unknown work cannot be silently dropped from
the terminal registry. No late completion reopens WORK or upgrades acceptance.

## Child And Parent Terminal Evidence Requirements

Child: independently attempt context close and stdin teardown while cleanup
time remains. Record a confirmed result, failure, or explicit not-attempted /
UNKNOWN for each; then freeze the child snapshot and serialize once. At exhausted
cleanup time, do not start a new write and pretend it succeeded.

Child save/readback acknowledgment is separate from its own snapshot content.
The parent verifies child bytes/hash and observes bounded child exit; missing,
mismatched, failed or unresolved evidence prevents acceptance. A snapshot cannot
certify its own save outcome, and parent query/exit evidence must not be inferred
from a child label. Stdout/IPC may report diagnostics but does not replace readback.

Parent: record child observations, native stop/query/close results and pending
operations, then freeze its terminal bytes once. Persist/read back those bytes
within cleanup remainder and return a separate ACK bound to their hash. A
late writer may still finish; an earlier UNKNOWN stays authoritative and the
frozen bytes are never rewritten to manufacture an ACK.

Acceptance requires no primary failure, required queries absent, all required
closes/child outcomes confirmed, no relevant pending/unknown work, retained stage,
and exact parent terminal write/readback acknowledgment. Model disposal eligibility
only from that conjunction. No actual stage deletion or self-referential last save.

## Secret-Safe Evidence Requirements

Keep one safe serializer for command events, identity/argv records and errors.
Recognized authorization/credential values must be removed before truncation,
including quoted/escaped bearer values and adjacent sensitive argv values across
the admitted dash/slash forms. An ambiguous recognized credential field is
redacted as a whole; preserve useful kind/basename/counts without a secret tail.
Do not claim universal detection of arbitrary unidentified secret text.

## Proposed Readable Capacity / Not Current Write Authority

Prospective source10/output12: R4source8 plus NEW protocol.py/test_protocol.py
and future return/proof2. Those new files are absent and are not created here.
Current working source has six files. execution.py and test_execution.py are
also absent: a future manifest must classify their reintroduction as NEW and
verify the pinned, rejected R4 snapshots as unaccepted starting material.
One new production owner holds phase/clock/admission/pending policy; existing
execution/controller/native/journey responsibilities remain separate. Private
algorithms are the future worker's choice within these observable boundaries.

| Proposed path basename | Frozen R4 lines | Prospective planning ceiling | Responsibility / capacity action |
|---|---|---|---|
| __init__.py | 301 | 329 | controller and existing proxy; fence before shutdown; phase checks after body/queue acquisition |
| lifecycle.py | 269 | 329 | exact process/handle identity; fresh check after identity persistence before resume |
| profile.py | 294 | 329 | case-specific receipts and source/oracle joins; retain schema/UTF16 logic |
| execution.py | 310 | 329 | serializer, command lifecycle and immutable terminal bytes; delegate phase/clock policy |
| protocol.py | NEW | 299 | NEW sole phase/clock/admission owner and pending-operation accounting |
| test_control.py | 294 | 296 | nine inert-control matrix and canonical fixtures; do not expand here |
| test_execution.py | 346 | 286 | move coherent protocol schedules before adding coverage; shrink at least60 |
| test_protocol.py | NEW | 299 | NEW deterministic composed clock/phase/late-completion tests |
| journey.cjs | 229 | 329 | lazy child calls, local wait clamps, child snapshot and complete reply validation |
| journey.test.cjs | 114 | 299 | fresh VM input, timing, close/stdin/snapshot controls |

Hard ceiling remains349/source; no minification or tests in production modules.
Minimum shrink target: 60 lines for recovered test_execution.py346, target286;
test_control.py stays<=296. The work-order author must bind the actual manifest,
source/oracle hashes and readable allocation before release. If allocation does
not fit, hold/redesign scope before dispatch rather than silently omit cases.

## Evidence / Verification

The companion contains all17 observed case IDs with their historical result and
future acceptance meaning. Preserve the seven positive results. Each of the ten
negative observations must reject/refuse or return truthful UNKNOWN as specified;
a renamed status or count/hash alone is insufficient. Add composed schedules:
- MODEL-PENDING-BODY: close work while a bounded body read is pending -> after return, refuse forward; retain pending read uncertainty.
- MODEL-QUEUED-REPLY: close before atomic admission commit -> revoke queued reply; never call its adapter or admit follow-on work.
- MODEL-INFLIGHT-WRITE: close between atomic admission commit and adapter entry, and separately during an invoked write -> retain pending identity/UNKNOWN; no cancellation claim, follow-on grant or acceptance upgrade on late completion.
- MODEL-CLEANUP-EXHAUSTION: first cleanup step consumes remainder -> record later steps NOT_ATTEMPTED/UNKNOWN; no timeout0, floor or replenished wait.
- MODEL-CHILD-CLOCK: child startup delay or wall clock rollback -> child estimate cannot extend parent authority; parent fence/unknown remain controlling.
- MODEL-CHILD-ACK: child snapshot missing, wrong bytes, unresolved exit or readback failure -> parent acceptance false; retained stage; no self-referential save success.

These are planned source-model cases, NOT_RUN here. Future Local probes use
fresh clocks/objects/VM selectors and serialized/read-back copies, never worker
assertion helpers. No broad rerun of R4 or real native/browser proof is needed
to establish this design decision. Grammar PASS will not prove implementation.

## Design Control Gate / Dispatch Boundary

Local locks the semantic choices above and the bounded proposed topology. This
finishes the selected design reassessment. A next work-order proposal must join
this baseline to fresh source-only authority, finite source/test/Git/time caps,
full mapped named reads, phase-specific mandatory requirement/proof rows, exact
pins and actual canonical readiness. It may recover rejected8 snapshots only
after hash verification as unaccepted starting material. No automatic worker.

Do not reuse R4 spending, grant, PASS rows or ordinal as a new admission. No R5
implementation artifact is released by this design. Actual Windows ABI/native,
product/browser/container, stage deletion, provider/live and parent custody
remain deferred; data/business/send/B2/P11/public/deploy checkpoints retained.

## Risk / Exception Boundary

If the desired promise becomes no physical completion after cutoff, arbitrary
hard thread preemption, or a snapshot proving its own successful save, the
contract is infeasible: return to Local design rather than weaken a test oracle.
Unsupported runtime clock/cancellation behavior prevents future runtime admission,
not truthful source-model work. A material scope/effect change needs its own grant.

## Related Owner Surfaces

Active source-verification and acceptance-ledger addenda own constructive
closeability/capacity; lifecycle owns phase feasibility and outcome truth; Review
Cost owns independent probes and same-root escalation. SOP Worker Preparation
Reminder owns timely mapped reads and byte/fixture discipline. This task creates
no parallel governance owner, checker or learning registry.

## Epistemic Process Block

Expected Result / Prediction: phase fence and acyclic evidence ownership remove
the contradictory guarantees that let a matching helper stand in for behavior.
Evidence Comparison: map retained17 observations to the requirements above;
advisory design review finds the admission/UNKNOWN interpretation constructible.
Contradiction Or Gap Disposition: accept design only; all implementation and actual
runtime proof remains unperformed; no historical R4 result is upgraded.
Claim Update: locked prospective source design, not execution readiness.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | governance/compat/check_markdown_structural_completeness.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_agent_operation_trace.py; governance/compat/check_finding_to_governance_learning.py; governance/compat/check_external_knowledge_intake_routing.py; governance/compat/check_corpus_completeness_report_integrity.py; governance/compat/check_core_guard_self_protection.py; governance/compat/check_machine_closure_package.py |
| literalTokensReviewed | baseline/review sections; trace17labels; RULE_EXISTS; all eight routing table rows; same-line corpus N/A reason; no unsupported knowledge-map N/A section; split material/continuity ranges |
| gateRunPurpose | confirmation of documentary design and source-evidence joins, not first discovery or implementation proof |
| claimBoundary | operative predicates and previously read owner sections reused; no all-checker-body or every-file-read claim |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Reviewer-return review`, role=`reviewer`, lifecyclePhase=`pre-implementation`.

Actual command: `python -B governance/compat/run_adif_defect_resolver.py --task-class "Reviewer-return review" --role reviewer --lifecycle-phase pre-implementation --max-results 100 --json`.

Returned defects: ADIF-0020, ADIF-0021, ADIF-0026, ADIF-0028, ADIF-0029, ADIF-0030, ADIF-0034, ADIF-0035, ADIF-0037, ADIF-0038, ADIF-0040, ADIF-0042, ADIF-0044, ADIF-0045, ADIF-0047, ADIF-0048, ADIF-0050, ADIF-0051, ADIF-0054, ADIF-0055, ADIF-0056, ADIF-0057, ADIF-0061, ADIF-0062, ADIF-0007, ADIF-0022, ADIF-0023, ADIF-0024, ADIF-0025, ADIF-0031, ADIF-0032, ADIF-0036, ADIF-0039, ADIF-0043, ADIF-0049. Total candidates35; returned35; truncated=false.
Raw packet retained in owned design custody. Query was late: first material
validation failed this missing disclosure, before any commit. Preparation is
PARTIAL; later grammar correction does not retroactively prove timely reads
or comprehension of every returned entry. No new checker or implementation.

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md |
| Input type | internal governed input (no external intake) |
| Internal source | docs/reviews/CVF_NCR_HTML_ROOT_RECOVERY_R4_COMPLETION_2026-10-15.md |
| Chain map route | negative source review -> Local semantic design -> prospective work-order preparation |
| Matching local-view guard | governance/compat/check_external_knowledge_intake_routing.py |
| Owner surface | existing NCR HTML helper family and Local design contract |
| Disposition | N/A with reason: internal design reconciliation, no external absorption |
| Claim boundary | source-only proposed behavior; no external evidence promoted to private proof |

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - selected source snapshots, retained observations and operative owner sections; no corpus scan.

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
Reason: internal design reconciliation, no rescan/intake refresh.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
Reason: private source-only protocol design; no public-sync claim.

## Claim Boundary

Written semantic design and source/evidence joins only. No source code changed,
new test program, native/product/browser/API call, deletion or runtime admission.
Future implementation effectiveness, whole root acceptance and agent adoption
are unproved. No fresh worker or profile allowance follows from this document.
