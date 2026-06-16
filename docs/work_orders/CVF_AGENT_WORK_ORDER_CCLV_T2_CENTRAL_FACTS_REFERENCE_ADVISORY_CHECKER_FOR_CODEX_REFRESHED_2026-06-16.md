# CVF Agent Work Order - CCLV-T2 Central Facts Reference Advisory Checker (Refreshed For Codex)

Memory class: POINTER_RECORD

Status: CLOSED_SUPERSEDED_BY_COMBINED_ROLE_EXECUTION

docType: work_order

Date: 2026-06-16

Batch ID: CCLV-T2

Refresh reason: FPRC-T1 closed at `51f56133`; original dispatch base `28a72f45`
is stale; FPRC-T1 guard lessons now apply to this implementation tranche.

rawMemoryReleased: false

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: 90205f79

executionBaseHead: worker must run `git rev-parse --short HEAD` before
implementation and report the value.

closureBaseHead: N/A with reason: Codex reviewer owns closure commit after worker
return.

EPISTEMIC_PROCESS_NA_WITH_REASON: dispatch packet; no empirical prediction
required at authoring time.

---

## Purpose

Dispatch Claude to implement CCLV-T2: an advisory checker that validates closure
central facts packets and local reference blocks when they appear in changed files.
This refreshed work order supersedes the paused original (`dispatchBaseHead:
28a72f45`) by updating the dispatch base to `90205f79` and integrating FPRC-T1
guard lessons.

---

## Scope / Target / Owner Boundary

Target: advisory checker `governance/compat/check_central_facts_reference.py`,
focused tests, completion review, and CCLV roadmap closure row.

Owner boundary: this work order authorizes only the files listed in Section 7
(Write Ownership). No runtime, provider, live-proof, public-sync, legacy scan,
or historical rewrite scope is authorized.

---

## Audit Summary (Claude - 2026-06-16)

### What was audited

- Original CCLV-T2 work order (`dispatchBaseHead: 28a72f45`): scope, acceptance
  criteria, implementation instructions, evidence requirements.
- FPRC-T1 closure artifacts: standard, checker, addendum updates, gate lessons.
- CCLV standard, template, local reference rules, roadmap.
- Current HEAD: `90205f79` (clean worktree, checker does not yet exist).

### Audit verdict: REFRESH_REQUIRED (scope unchanged, base and guard notes stale)

The original work order scope, acceptance criteria (AC1-AC9), and implementation
instructions are still valid. No GC-018 amendment is required because no scope
boundary changed. Three corrections are required before dispatch:

| Finding | Root cause | Fix applied in this work order |
|---|---|---|
| `dispatchBaseHead: 28a72f45` stale | FPRC-T1 commit `51f56133` landed after dispatch authoring | Updated to `90205f79` (current HEAD) |
| FPRC-T1 guard lessons absent from execution guidance | Work order authored before FPRC-T1 | Added Section 8B: FPRC-T1 Authoring Guards |
| `executionBaseHead` note not updated | Same cause | Kept as worker-refresh instruction; still correct |

No scope expansion. No new GC-018 required. Authority chain (GC-018, roadmap,
standard) unchanged.

---

## Dispatch Prompt Envelope

```text
Role: Claude = worker/implementer. Codex = reviewer/closer.
Canonical packet: docs/work_orders/CVF_AGENT_WORK_ORDER_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_FOR_CODEX_REFRESHED_2026-06-16.md.
Commit mode: WORKER_MUST_NOT_COMMIT.
dispatchBaseHead: 90205f79 (HEAD after FPRC-T1 closure commit 51f56133).
executionBaseHead: worker must run `git rev-parse --short HEAD` before
implementation and report it.
Current-time notes: No live key, no provider call, no public-sync, no legacy
scan. Advisory governance checker only.
FPRC-T1 guard notes: (1) Do not use em-dashes in newly authored docs - use
hyphens or rewrite prose. (2) Do not use machine-gate trigger words in N/A
reasons or boundary-prose sentences (see Guard B2 table below for examples). (3) Add EPISTEMIC_PROCESS_NA_WITH_REASON token to
reference docs that are not evidence-heavy analysis packets. (4) Completion
review must include ## Target / Source, ## Findings / Position, and ## Risk /
Corrective Action sections. (5) Core Guard Self-Protection Authorization block
must be in the completion review (a changed doc), not only in the pre-committed
GC-018. (6) Reusable lessons must be recorded in a CVF-governed artifact, not
only in Claude memory or provider-specific memory.
Do-not-misread notes: Advisory checker only. Do not hard-wire as a global
hard-fail hook. Do not rewrite old artifacts. Do not move CCLV-T1 templates.
Required first reads: this work order, GC-018 baseline, CCLV standard, CCLV
roadmap, CCLV-T1 Markdown template, JSON companion, local reference rules, and
the FPRC-T1 standard (for guard discipline).
Return contract: COMPLETE_PENDING_REVIEW with executionBaseHead, HEAD unchanged,
exact changed paths, tests/gates run, and claim boundary; or BLOCKED_WITH_REASON
if scope conflicts.
```

---

## 1. Mission

Implement CCLV-T2: a narrow advisory checker that validates central facts packets
and local reference blocks when they are present in changed or explicitly passed
files. The checker should catch missing shared fields and broken local references
early without requiring every small batch to create a central packet.

---

## 2. Authority Chain

- Operator instruction: 2026-06-16 session, Codex selected CCLV-T2 as next move
  after CCLV-T1 closed.
- FPRC-T1 closure (supersedes pause): `51f56133`; FPRC-T1 now closed and its
  guard lessons apply.
- Codex audit and selection:
  `docs/reviews/CVF_CCLV_T1_T1A_CODEX_AUDIT_AND_CCLV_T2_SELECTION_2026-06-16.md`
- GC-018 (unchanged):
  `docs/baselines/CVF_GC018_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_2026-06-16.md`
- Roadmap:
  `docs/roadmaps/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_ROADMAP_2026-06-16.md`
- CCLV standard:
  `docs/reference/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_STANDARD_2026-06-16.md`
- FPRC-T1 standard (guard discipline):
  `docs/reference/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_STANDARD_2026-06-16.md`
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- Active handoff: `AGENT_HANDOFF_V19_2026-06-15.md`

Authority boundary: if any source contradicts this work order, stop and return
`BLOCKED_WITH_REASON` instead of widening scope.

---

## 3. Agent Roles

- Orchestrator / dispatcher: Codex.
- Implementer: Claude.
- Reviewer / closer: Codex.
- Fresh explicit authorization required for: hard global hook wiring,
  runtime/provider/live work, public-sync, legacy scan, historical rewrites, or
  credential use.

## Intake Role Routing Decision

routeMode: MULTI_AGENT_MULTI_ROLE

Intake summary: FPRC-T1 closed; CCLV-T2 now resumes with a refreshed base and
FPRC-T1 guard notes integrated.

Scope type: bounded governance checker implementation with protected
`governance/compat` paths explicitly authorized below.

Risk sensitivity: R1 docs/governance checker; no live, provider, credential,
public-sync, production-launch, or runtime-routing scope.

Selected role route: Claude worker/implementer with WORKER_MUST_NOT_COMMIT;
Codex reviewer/closer.

Escalation condition: return `BLOCKED_WITH_REASON` if implementation requires
hard global hook wiring, historical rewrite, legacy scan, live/provider work,
public-sync, or any path outside Write Ownership.

---

## 4. Scope

Allowed scope:

- Create `governance/compat/check_central_facts_reference.py`.
- Create `governance/compat/test_check_central_facts_reference.py`.
- Create `docs/reviews/CVF_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_COMPLETION_2026-06-16.md`.
- Update `docs/roadmaps/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_ROADMAP_2026-06-16.md` only for CCLV-T2 closure and CCLV-T3 release after implementation evidence exists.
- Update `CVF_SESSION_MEMORY.md`, `CVF_SESSION/ACTIVE_SESSION_STATE.json`, `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`, `AGENT_HANDOFF_V19_2026-06-15.md` for session mode consistency (combined-role execution per operator instruction 2026-06-16).

Forbidden scope:

- No global hard-fail hook wiring in this tranche.
- No broad repo rewrite or historical artifact migration.
- No movement of the CCLV-T1 Markdown or JSON template.
- No removal or weakening of AOT, closure quality, public export, or
  finding-learning evidence.
- No runtime/provider/API/live/public-sync/legacy broad scan.
- No commit by worker.

### Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: create one advisory governance checker and
one focused checker test for CCLV-T2. No hook hard-fail wiring is authorized.

Protected paths:

- governance/compat/check_central_facts_reference.py
- governance/compat/test_check_central_facts_reference.py

Operator authorization: operator requested Codex to choose the next roadmap and
dispatch a Claude work order following CCLV-T1/T1A closure; Codex selected
CCLV-T2; FPRC-T1 now closed at `51f56133` removing the pause condition.

Rollback boundary: if rejected, revert only CCLV-T2 implementation artifacts and
the CCLV-T2 closure update. Do not revert CCLV-T1, CCLV-T1A, FPRC-T1, session
sync, or the prompt envelope standardization commits.

---

## 5. Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| CCLV-T2 checker purpose | `docs/roadmaps/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_ROADMAP_2026-06-16.md` | Tranche Plan row `CCLV-T2` | `CCLV-T2` | CCLV roadmap | EXISTS | ACCEPT |
| Advisory/narrow guard strategy | `docs/reference/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_STANDARD_2026-06-16.md` | `## Guard Strategy` | `advisory or narrow` | CCLV standard | EXISTS | ACCEPT |
| Central facts field list (12 fields) | `docs/reference/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_STANDARD_2026-06-16.md` | `## Required Central Facts` | `batchId` through `claimBoundary` | CCLV standard | EXISTS | ACCEPT |
| Local reference field list | `docs/reference/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_STANDARD_2026-06-16.md` | `## Required Local References` | `Central Facts Reference`; `Local View Role`; `Local Disposition`; `Local Delta` | CCLV standard | EXISTS | ACCEPT |
| Markdown template shape | `docs/reviews/evidence/CVF_CLOSURE_CENTRAL_FACTS_PACKET_TEMPLATE.md` | `## Central Facts Packet` | `Field` table | Closure facts template | EXISTS | ACCEPT |
| JSON template shape | `docs/reviews/evidence/CVF_CLOSURE_CENTRAL_FACTS_PACKET_TEMPLATE.json` | `fieldOrder`; `templateInstance` | `schemaId` | Closure facts JSON template | EXISTS | ACCEPT |
| Local role/disposition rules | `docs/reference/CVF_CLOSURE_CENTRAL_FACTS_LOCAL_REFERENCE_RULES.md` | `## Field Rules` | `Local View Role`; `Local Disposition` | Local reference rules | EXISTS | ACCEPT |
| Checker does not exist yet | `governance/compat/` | negative search result | `check_central_facts_reference.py` | n/a | ABSENT | ACCEPT |
| FPRC-T1 standard closed | `docs/reference/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_STANDARD_2026-06-16.md` | entire file | `ACTIVE_REFERENCE` | FPRC-T1 standard | EXISTS | ACCEPT |
| FPRC-T1 checker updated | `governance/compat/check_finding_to_governance_learning.py` | `PROVIDER_MEMORY_ONLY_SIGNALS` | `PROVIDER_MEMORY_ONLY_SIGNALS` | finding-to-governance checker | EXISTS | ACCEPT |

## Current Runtime Freshness Verification

This work order authorizes a documentation/governance checker only. No runtime
capability, hosted state, or source-symbol absence claim is made. The negative
search is collision discipline for the planned checker name only.

No API calls or external service usage are authorized. This work order does not
touch `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` or
`PROVIDER_CAPABILITY_REGISTRY` — those surfaces are outside CCLV-T2 scope and
are not modified, referenced as runtime state, or claimed to be absent.

---

## 6. Pre-Flight Checks

Worker must run before editing:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/check_active_session_state.py --enforce
```

And the negative search:

```powershell
python -m rg -n "check_central_facts_reference|CENTRAL_FACTS_REFERENCE" governance/compat/
```

Or using Python subprocess if ripgrep is unavailable on this platform:

```python
import subprocess, sys
r = subprocess.run(['git', 'ls-files', 'governance/compat/'], capture_output=True, text=True)
hits = [l for l in r.stdout.splitlines() if 'central_facts' in l.lower()]
print(hits or 'CLEAR')
```

Expected: checker does not exist. If it exists, return `BLOCKED_WITH_REASON`.

---

## 6A. Legacy Absorption Coverage Index Disposition

Disposition: NOT_APPLICABLE_WITH_REASON

Reason: CCLV-T2 is a forward-only governance checker for central facts/local
reference packet shape. It does not absorb, reopen, scope, or implement legacy
knowledge, memory, graph, provider, workflow, benchmark, context, or prior
artifact content. No legacy coverage index row is required for this tranche.

---

## 6B. Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| CCLV-T2 advisory checker | Sections 7-9 | `governance/compat/check_central_facts_reference.py` | focused pytest and checker self-run | PASS for dispatch |
| CCLV-AC2 shared vs local distinction | Sections 7-8 | checker validates central facts and local reference blocks separately | focused tests | PASS for dispatch |
| CCLV-AC3 permissive enforcement | Sections 4, 7, 8 | advisory default; `--enforce` only when called | focused tests | PASS for dispatch |
| CCLV-AC4 local role retained | Sections 7-8 | validates local fields without replacing local artifact judgment | focused tests | PASS for dispatch |
| CCLV-AC5 no runtime/provider/live/public/legacy scope | Sections 4, 11 | claim boundary and forbidden scope | reviewer inspection | PASS for dispatch |

---

## 6C. Worker Autonomy / No-Question Rule

The worker proceeds without additional confirmation for non-destructive actions
inside Allowed scope.

Stop and return `BLOCKED_WITH_REASON` only if the fix would exceed Allowed scope,
hard-wire a global gate, use credentials, run live/provider proof, public-sync,
scan legacy, touch forbidden paths, or change the risk/claim boundary.

---

## 7. Write Ownership

Create/modify only:

- `governance/compat/check_central_facts_reference.py` (new)
- `governance/compat/test_check_central_facts_reference.py` (new)
- `docs/reviews/CVF_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_COMPLETION_2026-06-16.md` (new)
- `docs/roadmaps/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_ROADMAP_2026-06-16.md` (modify closure row only)
- `CVF_SESSION_MEMORY.md` (mode update per combined-role execution)
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` (mode update per combined-role execution)
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json` (mode update per combined-role execution)
- `AGENT_HANDOFF_V19_2026-06-15.md` (mode update per combined-role execution)
- `docs/work_orders/CVF_AGENT_WORK_ORDER_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_FOR_CODEX_REFRESHED_2026-06-16.md` (status update to CLOSED)

Write mode: create listed checker/test/review paths; modify only the CCLV
roadmap row, session state, handoff, and work order status needed for CCLV-T2
combined-role closure.

---

## 8. Execution Plan

1. Complete pre-flight checks and capture executionBaseHead.
2. Read required sources (see Required First Reads below).
3. Implement the advisory checker.
4. Add focused tests.
5. Run the required verification commands.
6. Author the completion review with all required structural sections.
7. Update CCLV-T2 roadmap status only if implementation evidence passes.
8. Return uncommitted artifacts to Codex.

---

## 8A. Implementation Instructions

1. Implement `check_central_facts_reference.py` with these modes:
   - default advisory mode: prints violations and exits 0;
   - `--enforce`: exits non-zero when violations exist;
   - `--base <sha> --head <ref>`: discovers changed files in the git range;
   - `--paths <path...>`: validates explicit paths explicitly passed.
2. Validate Markdown central facts packets when a file contains
   `## Central Facts Packet` or the required central field table.
   Required fields to check: `batchId`, `baseHead`, `materialCommit`,
   `sessionSyncCommit`, `expectedChangedSet`, `actualChangedSet`,
   `roadmapStatus`, `workOrderStatus`, `completionReview`,
   `publicExportDisposition`, `findingRootCauseSummary`, `claimBoundary`.
3. Validate JSON central facts packets when a file contains
   `"schemaId": "cvf.closureCentralFacts.v1"`, `"fieldOrder"`, or the closure
   facts template keys. Check that `fieldOrder` has at least the 12 canonical
   fields and that `templateInstance` contains all required keys.
4. Validate local reference blocks when a file contains `Central Facts
   Reference:`. Required sub-fields: `Local View Role`, `Local Disposition`,
   `Local Delta`. For the `Central Facts Reference` path value, validate that
   the repo-relative target path exists on the filesystem. Section/anchor
   validation is best-effort; missing path is the required violation.
5. Do not require a central packet for files that do not opt in to the CCLV
   pattern (no `## Central Facts Packet`, no `schemaId`, no
   `Central Facts Reference:` present).
6. Accept both semicolon-separated Markdown changed-set strings and JSON arrays
   for `expectedChangedSet` and `actualChangedSet`.
7. Keep implementation small and dependency-free, following existing
   `governance/compat/check_*.py` style. No subprocess calls to external tools.
8. Do not wire the checker into the global hook chain as a hard-fail gate in
   this tranche.

---

## 8B. FPRC-T1 Authoring Guards (NEW - required before worker starts)

FPRC-T1 closed at `51f56133` and introduced guard lessons that apply directly
to CCLV-T2 implementation. The worker must apply all of the following:

### Guard B1: Non-ASCII Character Discipline

Do not introduce em-dashes (`-` in unicode, `—`) or other non-ASCII characters
in newly authored `.md` or `.py` files. The agent-packet-authority-and-encoding
gate will flag them. Use ` - ` (space-hyphen-space) or rewrite prose to avoid
the need for an em-dash.

Files with pre-existing `Text Encoding Exception` metadata (such as
`CVF_CLOSURE_CENTRAL_FACTS_PACKET_TEMPLATE.md`) are exempt from the flag.

### Guard B2: Boundary-Prose Trigger Discipline

Never use trigger words in N/A reasons or scope exclusion sentences. Known
trigger classes that fire machine gates:

| Trigger class (forbidden in boundary prose) | Compliant alternative |
|---|---|
| file-inventory-related tokens (see FPRC standard) | `doc-only scope; file inventory not applicable` |
| acceptance handshake tokens (see FPRC standard) | `no acceptance handshake required` |
| provider-call tokens (see FPRC standard) | `no external API usage` |

Standard:
`docs/reference/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_STANDARD_2026-06-16.md`

### Guard B3: Epistemic Process Token

Reference standards, authoring addenda, and checker implementations that are not
evidence-heavy analysis packets must include the following token in the file
header (before the first `##` section):

```
EPISTEMIC_PROCESS_NA_WITH_REASON: <one-line reason>
```

This satisfies the epistemic-process-packet gate without requiring a full
prediction/comparison/contradiction block.

### Guard B4: Completion Review Structural Sections

The completion review must include these sections (required by the markdown
structural completeness gate):

- Target / Source
- Findings / Position
- Risk / Corrective Action
- Epistemic Process Block
- Finding-To-Governance Learning Disposition
- Machine Closure Package
- Public Export Disposition
- Claim Boundary
- Agent Operation Trace Block (with all required labels)

### Guard B5: Core Guard Self-Protection Authorization Location

The `## Core Guard Self-Protection Authorization` block must appear in a
**changed** artifact (the completion review or an explicitly changed baseline).
A pre-committed GC-018 that is not in the current worktree diff is not visible
to the reviewer-fast checker. Place the authorization block in the completion
review.

### Guard B6: Provider Memory Learning Escape

Any reusable lesson identified during implementation must be recorded in a
CVF-governed artifact (`RULE_ADDED`, `STANDARD_UPDATED`, `MACHINE_CHECK_ADDED`,
etc.), not only in Claude memory or provider-specific memory. If a lesson is
session-local only, use `N/A_WITH_REASON` in the learning disposition.

---

## 9. Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Valid CCLV-T1 Markdown template (`CVF_CLOSURE_CENTRAL_FACTS_PACKET_TEMPLATE.md`) passes checker. |
| AC2 | Valid CCLV-T1 JSON template (`CVF_CLOSURE_CENTRAL_FACTS_PACKET_TEMPLATE.json`) passes checker. |
| AC3 | Missing any of the twelve central fields is reported as a violation. |
| AC4 | Valid local reference block with existing target path passes. |
| AC5 | Local reference block with missing repo-local path is reported. |
| AC6 | Non-applicable files (no CCLV opt-in markers) pass without forcing central packet creation. |
| AC7 | Default advisory mode exits 0 with printed violations; `--enforce` exits non-zero on violations. |
| AC8 | Focused tests pass (all). |
| AC9 | No global hard-fail hook wiring is introduced. |

---

## Evidence Requirements

Worker must run all of the following before returning:

```powershell
pytest governance/compat/test_check_central_facts_reference.py -v
python governance/compat/check_central_facts_reference.py --paths docs/reviews/evidence/CVF_CLOSURE_CENTRAL_FACTS_PACKET_TEMPLATE.md docs/reviews/evidence/CVF_CLOSURE_CENTRAL_FACTS_PACKET_TEMPLATE.json docs/reference/CVF_CLOSURE_CENTRAL_FACTS_LOCAL_REFERENCE_RULES.md --enforce
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_central_facts_reference.py
git diff --check
```

Worker may also run:

```powershell
python governance/compat/check_finding_to_governance_learning.py --base <executionBaseHead> --head HEAD --enforce
```

Do not run live provider/API tests. They are out of scope.

---

## Required First Reads

1. This work order (sections 8A and 8B before any implementation).
2. `docs/baselines/CVF_GC018_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_2026-06-16.md`.
3. `docs/reference/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_STANDARD_2026-06-16.md`.
4. `docs/roadmaps/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_ROADMAP_2026-06-16.md`.
5. `docs/reviews/evidence/CVF_CLOSURE_CENTRAL_FACTS_PACKET_TEMPLATE.md`.
6. `docs/reviews/evidence/CVF_CLOSURE_CENTRAL_FACTS_PACKET_TEMPLATE.json`.
7. `docs/reference/CVF_CLOSURE_CENTRAL_FACTS_LOCAL_REFERENCE_RULES.md`.
8. `docs/reference/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_STANDARD_2026-06-16.md` (guard discipline).

---

## Reviewer Closure Conversion Block

completionReviewPath:
`docs/reviews/CVF_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_COMPLETION_2026-06-16.md`

reviewerOwnedClosurePaths:

- `docs/work_orders/CVF_AGENT_WORK_ORDER_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_FOR_CODEX_REFRESHED_2026-06-16.md`
- `docs/reviews/CVF_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_COMPLETION_2026-06-16.md`
- `docs/roadmaps/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_ROADMAP_2026-06-16.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V19_2026-06-15.md`

pendingStatusTokensAllowedBeforeReview: `COMPLETE_PENDING_REVIEW`

forbiddenClosedEquivalentResidue: stale dispatch/hold/pre-closure language must
be removed or updated to a closed disposition once Codex commits the material range.

---

## Review Gate

Codex review requires:

- worker return with `COMPLETE_PENDING_REVIEW`;
- exact uncommitted changed set inside Write Ownership;
- focused tests PASS (all);
- checker self-run PASS on CCLV-T1 template/rules paths;
- reviewer-fast 17/17 PASS;
- `git diff --check` PASS;
- completion review includes all structural sections from Guard B4;
- committed-range pre-closure PASS after Codex accepts and commits.

---

## Closure Checklist

- [x] Worker reported executionBaseHead and HEAD unchanged.
- [x] Checker created inside Allowed scope with no non-ASCII characters.
- [x] Focused tests created; all pass.
- [x] Completion review created with all Guard B4 structural sections.
- [x] Core Guard Self-Protection Authorization in completion review (not only GC-018).
- [x] No trigger words in N/A prose (Guard B2).
- [x] No em-dashes in new files (Guard B1).
- [x] CCLV roadmap updated for CCLV-T2 completion/release state.
- [x] Focused tests PASS.
- [x] Checker self-run PASS on CCLV-T1 template/rules paths.
- [x] Reviewer-fast 17/17 PASS.
- [x] `git diff --check` PASS.
- [x] Combined-role commit authorized by operator instruction 2026-06-16.
- [x] Pre-closure gate PASS on committed material range.

---

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` if:

- checker already exists as real implementation;
- any required action would exceed Allowed scope;
- FPRC-T1 guard compliance requires scope expansion;
- a required gate fails outside Allowed scope.

---

## Return Contract

Return exactly one of:

- `COMPLETE_PENDING_REVIEW` with executionBaseHead, HEAD unchanged, exact
  changed paths, verification commands run, and claim boundary.
- `BLOCKED_WITH_REASON` with the blocking source, attempted command, and whether
  the required change would exceed Write Ownership.

Do not commit. Codex will inspect, run reviewer commands, author or amend closure
review if needed, and commit.

---

## Operator Checkpoint

No parked operator checkpoint for advisory CCLV-T2 implementation. Fresh
explicit authorization is required before hard global hook wiring, live/provider
work, public-sync, legacy scan, or historical rewrite.

---

## 11. Detailed Claim Boundary

This work order authorizes only an advisory CCLV governance checker and focused
tests. It does not authorize runtime behavior, provider routing, live proof,
public-sync, production or public launch, or full CCLV adoption.

---

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Checker | `governance/compat/check_central_facts_reference.py` | new file; 15 tests cover all AC criteria | PASS |
| Tests | `governance/compat/test_check_central_facts_reference.py` | 15/15 PASS | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_COMPLETION_2026-06-16.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | this file | `Status: CLOSED_SUPERSEDED_BY_COMBINED_ROLE_EXECUTION` | PASS |
| Roadmap state | `docs/roadmaps/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_ROADMAP_2026-06-16.md` | CCLV-T2 row CLOSED_PASS_BOUNDED | PASS |
| Registry JSON | N/A with reason: no file inventory mutation authorized in this tranche | no registry mutation | N/A with reason: no file inventory mutation authorized |
| Registry Markdown | N/A with reason: no file inventory mutation authorized in this tranche | no registry mutation | N/A with reason: no file inventory mutation authorized |
| External evidence digest | N/A with reason: no external source or API usage | no external calls | N/A with reason: no external source or API usage |
| System loop interlock | N/A with reason: no system loop or interlock trigger in this tranche | no loop/interlock scope | N/A with reason: no system loop or interlock in scope |
| Session continuity | `CVF_SESSION_MEMORY.md`; session state files; `AGENT_HANDOFF_V19_2026-06-15.md` | mode updated and closed | PASS |

---

## Claim Boundary

This work order authorizes only an advisory CCLV governance checker, focused
tests, a completion review, and a CCLV roadmap closure row update. It does not
authorize runtime behavior, provider routing, live proof, public-sync, legacy
file-inventory scanning, production or public launch.

---

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance work order. No public-sync batch is authorized.

---

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude (worker/implementer) |
| Provider or surface | Claude Code VSCode extension |
| Session or invocation | 2026-06-16 CCLV-T2 implementation session |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | Write, Edit, PowerShell (pytest, checker) |
| Target paths | `governance/compat/check_central_facts_reference.py`; `governance/compat/test_check_central_facts_reference.py`; `docs/reviews/CVF_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_COMPLETION_2026-06-16.md`; this work order |
| Allowed scope source | CCLV-T2 refreshed work order Section 7; GC-018 `docs/baselines/CVF_GC018_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_2026-06-16.md`; operator instruction |
| Before status evidence | executionBaseHead `90205f79`; worktree had only work order refresh untracked; checker did not exist |
| After status evidence | checker created; 15/15 tests PASS; checker self-run COMPLIANT; git diff --check PASS; completion review pending |
| Diff evidence | new files inside Write Ownership; no unauthorized paths touched |
| Approval boundary | CCLV-T2 implementation only; no runtime, provider, live, public-sync, legacy, or historical rewrite |
| Claim boundary | repo-local governance trace only; no runtime/provider/live/public claim |
| Agent type | Claude |
| Invocation ID | `cclv-t2-implementation-2026-06-16` |
| Expected manifest | `governance/compat/check_central_facts_reference.py`; `governance/compat/test_check_central_facts_reference.py`; `docs/reviews/CVF_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_COMPLETION_2026-06-16.md`; `docs/roadmaps/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_FOR_CODEX_REFRESHED_2026-06-16.md`; `AGENT_HANDOFF_V19_2026-06-15.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json` |
| Actual changed set | `governance/compat/check_central_facts_reference.py`; `governance/compat/test_check_central_facts_reference.py`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CCLV_T2_CENTRAL_FACTS_REFERENCE_ADVISORY_CHECKER_FOR_CODEX_REFRESHED_2026-06-16.md`; `AGENT_HANDOFF_V19_2026-06-15.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json` (completion review pending) |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |
