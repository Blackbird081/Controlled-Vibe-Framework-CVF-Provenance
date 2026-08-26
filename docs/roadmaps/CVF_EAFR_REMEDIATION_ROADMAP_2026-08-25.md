# CVF EAFR Remediation Roadmap

Memory class: SUMMARY_RECORD

Status: ACTIVE_R9_DISPATCHED_PENDING_WORKER_RETURN

Date: 2026-08-25

Roadmap ID: EAFR

Decision owner: operator through explicit 2026-08-25 orchestrator authority

Reviewer/closer: current independent orchestrator/reviewer

## Authorization Decision

The operator explicitly authorized the current orchestrator on 2026-08-25 to
prioritize and govern this sequence before returning to the parked checkpoint.

## Purpose

Close the source-verified safety and truthfulness gaps accepted into EAFR while
the earlier RFR final-reconciliation checkpoint remains parked. Execute small,
dependency-ordered tranches and require independent review before each closure.

## Source Evidence

| Source | Current verified fact | Disposition |
| --- | --- | --- |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/aif-memory-reinjection.ts` | omitted item provenance currently defaults to `1` before eligibility | ACCEPT |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/aif-memory-reinjection.test.ts` | existing adversarial coverage omits missing and non-finite provenance cases | ACCEPT |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | the decision prompt block is composed into the execute system prompt | ACCEPT |
| archive-hygiene commit `0fcc1dc20` | advisory inputs preserved as history without authority status | ACCEPT_AS_LINEAGE_ONLY |

## Scope

In scope: AIF reinjection provenance admission, durable-memory write authority
and omission behavior, as-built memory map reconciliation, provider-current
claim inventory, retrieval evidence semantics, and final EAFR reconciliation.

Out of scope: public sync, push, deployment, unrelated product work, automatic
use of credentials, and resuming the parked RFR checkpoint before EAFR closes.

## Non-Goals

This roadmap does not combine tranches, pre-approve live calls, treat advisory
history as authority, or permit a worker to review, close, commit, or publish
its own work.

## Proposed Tranches

| Tranche | Objective | Dependency | Status |
| --- | --- | --- | --- |
| EAFR-R1 | reject missing or non-finite AIF item provenance before prompt composition | archive hygiene `0fcc1dc20` | REVIEWER_ACCEPTED_CLOSED_PASS_BOUNDED_BY_EXPLICIT_OPERATOR_WAIVER: focused implementation accepted; three non-green package criteria preserved as R1C debt |
| EAFR-R1A | make the package non-live test runner exclude both `.live.test.ts` and `.live.test.tsx`, then reconcile the R1 incident | R1 implementation accepted | REVIEWER_ACCEPTED_COMPLETE_BOUNDED at `ef142bfb2` |
| EAFR-R1B | adjudicate exact execution-base variance against the parent R1 acceptance authority | R1A accepted and prior A/B evidence committed | REVIEWER_ACCEPTED_FAIL_CLOSED_ADJUDICATION at `fc10c8e65`; subsequent explicit operator waiver closes R1 without changing R1B's evidence finding |
| EAFR-R2 | make durable-memory HTTP writes and authority inputs fail closed | R1 bounded waiver closure, R1A accepted, and R1B adjudication accepted | REVIEWER_ACCEPTED_CLOSED_PASS_BOUNDED; 26/26 focused; package/typecheck debt remains R1C-owned |
| EAFR-R3 | reconcile the memory-plane map to accepted as-built behavior | R2 accepted | REVIEWER_ACCEPTED_CLOSED_PASS_BOUNDED; 46/46 focused; worker-return fast and reviewer-fast 65/65 PASS |
| EAFR-R4 | replace partial provider-current claims with a complete private manifest | R3 accepted | REVIEWER_ACCEPTED_CLOSED_PASS_BOUNDED; 29 classified active entries, zero unmapped; focused 17/17 and reviewer-fast 65/65 PASS; broad debt remains R1C-owned |
| EAFR-R5 | decide and prove retrieval evidence semantics without weakening admission | R4 accepted | REVIEWER_ACCEPTED_CLOSED_PASS_BOUNDED; focused LPF 66/66 and Web 20/20; safe LPF package 1943/1943; six unintended provider calls disclosed and excluded from acceptance |
| EAFR-R1C | repair or freshly adjudicate the waived typecheck, full non-live-suite, and build debt | explicit R1 waiver and R5 accepted | REVIEWER_ACCEPTED_CLOSED_PASS_BOUNDED; typecheck green; safe suite 3525 pass/2 named BuildAuthority failures; build freshly blocked; five OpenAI calls disclosed and excluded |
| EAFR-R1D | make the cvf-web non-live runner exclude ambient-key real-provider integration tests and reconcile the R1C five-call incident | R1C accepted bounded | REVIEWER_ACCEPTED_CLOSED_PASS_BOUNDED; selection and activation barriers pass; focused guard 6/6; safe suite 3525 pass/2 named fail; one worker OpenAI call disclosed and excluded |
| EAFR-R1E | separate live-test selection from provider execution authority and make every worker/subagent provider call require an orchestrator-issued bounded grant | second accidental worker provider call after R1D | REVIEWER_ACCEPTED_CLOSED_PASS_BOUNDED; default deny contract, pre-network guard, list-only live script, 42/42 plus 12/12 focused tests and reviewer-fast 66/66 PASS; zero provider calls |
| EAFR-R6 | independently reconcile closures, including the BuildAuthority Web gap and provider-call incidents, and decide whether parked RFR may resume | R1/R1A/R1B, R2-R5, R1C, R1D and R1E accepted | REVIEWER_ACCEPTED_CLOSED_BLOCKED; four unresolved P1 provider-authority bypass classes; RFR resume blocked |
| EAFR-R7 | repair provider-execution authority coverage across endpoint constants, configurable/caller endpoints and out-of-process harness boundaries | R6 accepted blocked | REVIEWER_ACCEPTED_CLOSED_BLOCKED; fail-closed repair retained; Upstash non-live egress and adapter injection residual keep RFR parked |
| EAFR-R8 | isolate ambient external datastore configuration from non-live tests and close the unguarded adapter fetch-injection residual | R7 accepted blocked | REVIEWER_ACCEPTED_CLOSED_BLOCKED; ambient datastore isolation and injected-fake proofs accepted after reviewer repair; live-store grant and adapter injection residual remain blocked |
| EAFR-R9 | source-verify and govern bounded external-store execution authority plus the shared adapter destination-policy owner | R8 accepted blocked | REVIEWER_REPAIRED_DISPATCHED at `85a6f809e`; mutable-roadmap hash trap removed; existing cvf-web to cvf-model-gateway edge makes gateway-local ownership the leading candidate; worker decides without implementing |

## Design Controls

- Each implementation tranche owns the smallest source/test surface that can
  prove its invariant.
- Missing evidence at a safety boundary fails closed.
- A worker never closes its own tranche and never commits in this roadmap.
- Provider/live proof is used only when a later work order explicitly requires
  it and carries diagnostic, secret, quota, and external-effect controls.
- Worker/subagent provider execution defaults to `FORBIDDEN`; API keys and
  live-test selection are not authority. Any exception requires a bounded,
  expiring grant issued by the orchestrator and enforced before network I/O.
- Documentation is updated only after corresponding runtime behavior is
  accepted; documentation never substitutes for runtime proof.

## Design Control Gate

Each tranche must have a source-verified GC-018 baseline, committed no-commit
work order, exact ownership manifest, negative proof, and independent closure.

## Work Plan

Execute the Proposed Tranches table strictly in dependency order. Only the
current `DISPATCH_READY` row may enter worker execution.

## Acceptance Criteria

- R1 proves omitted, explicit-undefined, and non-finite provenance cannot enter
  selected memory or the generated system prompt.
- R2 proves unauthorized or incomplete durable writes are rejected with no
  storage mutation.
- R3 maps only accepted as-built components and clearly marks absent behavior.
- R4 has a complete, source-backed private provider manifest without a public
  export claim.
- R5 records a bounded design verdict plus executable proof for any admitted
  retrieval evidence.
- R6 contains no unresolved P0/P1 row before the parked roadmap can resume.
- R7 removes or explicitly fail-closes every R6 P1 provider-authority bypass
  class before RFR can be reconsidered.
- R8 proves non-live tests cannot use ambient external datastore credentials,
  exercises Redis behavior through an injected fake, and closes or explicitly
  blocks the adapter's unguarded fetch-injection residual.
- R9 must preserve R8 non-live isolation while source-verifying a bounded,
  orchestrator-issued external-store grant and a non-duplicated owner for
  adapter destination policy; selection flags remain non-authoritative.

## Risk / Corrective Action

Primary risk is a compatibility repair that silently weakens admission. Every
runtime tranche therefore requires negative tests, unchanged-path hashes, a
no-commit worker return, and independent reviewer closure. Any need to change
the claim boundary, use live credentials, or touch a forbidden path returns
`BLOCKED_WITH_REASON`.

## Verification Evidence

Roadmap verification consists of tranche-specific focused/full tests,
governance phase gates, exact manifests, reviewer decisions, committed hashes,
and a final reconciliation before the parked checkpoint is reconsidered.

## Current Runtime Freshness Verification

Current source was independently reviewed on 2026-08-25 after R1C worker return
and bounded reviewer repair. Web TypeScript is green and twenty-seven of the
twenty-nine suite failures are repaired without production edits. The corrected
provider-excluded suite passes 3525 tests and retains two failures caused by a
single named BuildAuthority Web evidence gap; build remains documentarily
blocked by parked environment authority. The nominal non-live runner selected
one ambient-key OpenAI integration case in five R1C lifecycle runs; those calls
are disclosed, excluded and grant no repeat-live authority. This is bounded
local source/test acceptance, not provider, build, deployment or production
proof.

R1E now separates live selection from provider execution. Worker/subagent
provider authority defaults to forbidden, and CVF-owned provider traffic needs
an orchestrator-issued subject/delegation/provider/call/expiry-bound grant.
Focused contract and web tests, TypeScript, list-only discovery and the 66-check
reviewer-fast gate pass with zero R1E provider calls. This remains bounded to
CVF-owned execution paths and is not universal host network isolation.

R6 independently re-derived all ten closures and accepted the worker's blocked
verdict after one reviewer matrix repair. Fresh Web proof is 313 files and 3533
tests with exactly 20 PVV pre-network denials plus two named BuildAuthority
failures. Four P1 bypass classes remain: mainland DashScope, endpoint env
overrides, caller-supplied adapter endpoints and out-of-process harnesses.
RFR remained parked and released R7 repair only.

R7 retains the inverted fail-closed egress control after independent reviewer
repair of a protocol-relative bypass. Focused proof is 26/26 and TypeScript is
green. Full non-live proof is 313 files and 3553 tests: 3465 pass and 88 fail;
66 additional failures all expose a pre-existing Upstash datastore call loaded
from ambient local environment. R7 closes blocked, the adapter injection
residual remains, and R8 source verification/dispatch authoring is next.

R8 unconditionally clears ambient Upstash selectors and credentials from the
non-live test process, retains the R7 default deny, and proves rate-limit plus
storage Redis seams with injected in-process fakes. Independent proof is 97/97
focused, both package typechecks pass, and the full non-live suite selects 314
files and 3560 tests with 3538 passing and 22 named residual failures. The
worker's second return still omitted injected storage operation proof; the
reviewer repaired that test before acceptance. R8 closes blocked because the
guard has no bounded external-store execution grant and the gateway adapter
still accepts an unobserved injected fetch. RFR remains parked; only R9 source
verification and dispatch authoring is released.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_core_guard_self_protection.py` |
| literalTokensReviewed | roadmap status; dependency rows; public export disposition; checker read-ahead confirmation language |
| gateRunPurpose | confirm and record evidence for the already source-verified roadmap shape; not first discovery |
| claimBoundary | checker conformance does not prove runtime remediation or release readiness |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private provenance remediation sequence; public sync is not
authorized.

## Claim Boundary

This roadmap authorizes bounded dispatch authoring and dependency sequencing.
It does not itself implement, test, live-prove, deploy, publish, push, or close
any runtime behavior.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | EAFR tranche packets | R1-R5 and R1C committed dispatch authority | PASS |
| Completion or reviewer artifact | R1C completion review | bounded closure, named residuals and incident recorded | PASS |
| Roadmap state | this file | R8 accepted blocked; R9 source verification next; RFR parked | PASS |
| Registry JSON | system-chain map | `ARCHITECTURE.md` fingerprint refreshed; freshness CURRENT | PASS |
| Registry Markdown | N/A with reason: no registry projection | no applicability | BLOCKED |
| External evidence digest | archived corrected external report | input only, not authority | N/A with reason |
| System loop interlock | R1D incident -> R1E authority control -> R6 blocked -> R7 blocked -> R8 blocked -> R9 | fail-closed dependencies explicit | PASS |
| Session continuity | separate post-material sync | required after material commit | PASS |
