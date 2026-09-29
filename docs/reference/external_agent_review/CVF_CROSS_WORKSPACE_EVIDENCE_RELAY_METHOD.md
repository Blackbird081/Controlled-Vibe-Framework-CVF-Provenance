# CVF Cross-Workspace Evidence Relay Method

Memory class: governed-method

Status: ACTIVE_REFERENCE

docType: reference

Date: 2026-09-10

## Purpose

Define the CVF coordination method used when repository research happens on a
Web or other remote agent surface that cannot share the Local Agent's
filesystem, Git state, private continuity, or governed workspace.

The method transports task-bound evidence across that boundary without making
the transport operator a reviewer or making the remote result CVF authority.

## Scope / Applies To

Apply this method when all of the following are true:

- a Local Agent owns current private-CVF reconciliation;
- one or more remote agents work outside the local workspace;
- the operator must copy/paste text or transfer files between the surfaces;
- the remote work studies a third-party repository for possible CVF value;
- the returned material must be checked against current local/private CVF.

The number of remote agents is task-specific. One, two, or more may be used.
Agent count, provider, model, and chat identity are not trust anchors.

## Program Scope Versus Task Scope

Cross-workspace transport cardinality and absorption-program cardinality are
different facts:

```text
REMOTE_RETURN_SCOPE := LOCAL_DISPATCH_SCOPE
ONE_REPOSITORY_RETURN != ONE_REPOSITORY_ABSORPTION_PROGRAM
CHILD_TASK_COMPLETION != UMBRELLA_CORPUS_COMPLETION
```

A Local Agent may issue a task capsule for one exact repository even when the
owning absorption program contains many repositories or domain groups. A remote
agent that returns only that repository has followed the task correctly; it has
not omitted the other program sources. Responsibility for that narrowing stays
with the Local dispatch boundary.

No single-repository capsule, return, validation receipt, or Local disposition
silently supersedes an umbrella source ledger. Supersession requires an explicit
Operator scope decision recorded in Local CVF continuity. When a multi-repository
program is active, every source remains traceable to a child task, terminal
filter disposition, or explicit blocked state before any program-complete claim.

Use `CVF_CROSS_WORKSPACE_DOMAIN_FUNNEL_ABSORPTION_METHOD.md` when multiple
repositories are grouped and filtered by domain before CVF comparison. This
relay method remains the transport and responsibility layer for every funnel
stage that crosses the Web/Local workspace boundary.

## Canonical Method

Method identifier: `cvf.cross-workspace-evidence-relay@1.0.0`

Short form:

```text
LOCAL_CONTEXT_AND_TASK_BINDING
-> OPERATOR_RELAY_OUT
-> REMOTE_SOURCE_RESEARCH
-> OPERATOR_RELAY_IN
-> LOCAL_INTEGRITY_VALIDATION
-> LOCAL_SEMANTIC_RECONCILIATION
-> LOCAL_FINAL_TECHNICAL_DISPOSITION
-> EXTERNAL_RESEARCH_PHASE_CLOSED
-> INTERNAL_WORK_ORDER_IF_SELECTED
```

This method composes the existing `cvf.external-agent-round-trip` protocol. It
does not change that protocol's task-capsule schema, return schema, status
vocabulary, or validation commands.

## Relay Termination And Internal Handoff

This relay method ends at the research-to-execution boundary. External agents
may help research sources and converge on an advisory shortlist; only the Local
Agent selects the final technical disposition. If Local then issues a governed
work order, the selected task becomes `INTERNAL_AGENT` work in the shared Local
workspace.

The internal work order must not represent the Local worker as a detached
external agent merely because the worker uses a different model or chat. Its
evidence travels through governed workspace artifacts and worktree state. The
operator does not relay worker instructions or returns between Web and Local
surfaces for that execution. External agents do not implement, review, close,
stage, or commit the internal work order.

Reopening Web research later creates a separately bound external research loop;
it does not silently move internal execution back across the workspace boundary.

## Role-Neutral Responsibility Model

| Responsibility | Required behavior | Authority boundary |
|---|---|---|
| Local Agent | Prepare or verify task context, validate the return, inspect current private CVF owners, challenge novelty, and issue the final technical disposition. | Final technical absorption decision only; implementation and external effects still require their governed authority. |
| Remote research agent | Read the supplied orientation packet and pinned public CVF source before researching the task-pinned repository; return source-backed advisory evidence. | No private-CVF knowledge, final owner decision, promotion, implementation, or readiness authority. |
| Operator relay | Move the packet, questions, repair requests, and returns between workspace-separated surfaces without semantic editing or adjudication. | Transport only during the relay loop; any new operator instruction must be labeled separately from relayed agent content. |
| Internal shared-workspace worker | Execute only a Local-issued governed work order after the external research phase closes. | Same-workspace worker evidence only; no independent scope expansion, final review, or closure authority. |

The same human may retain normal operator authority outside the relay loop.
That authority must be exercised explicitly as a new instruction or checkpoint,
not inferred from the act of copying content between agents.

## Context Before Remote Research

The operator-local packet root convention is:

`D:\UNG DUNG AI\EXTERNAL_AGENT_READ`

The packet root is a transport surface, not CVF source of truth. For each task,
the operator sends the exact task relay or bounded file set selected from that
root. The remote agent reads the supplied bootstrap, context brief, public
snapshot, return contract, owner index, task capsule, and refresh receipt before
research begins.

The remote agent also reads the public repository at the task-pinned commit:

`https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF`

The public repository is orientation and preliminary owner-discovery context.
It cannot prove what current private/local CVF contains. The task capsule's
public-CVF pin remains the reproducible comparison anchor; a newer live head is
reported as freshness context and never substituted silently.

## Source And Decision Authority

| Claim class | Required source |
|---|---|
| Third-party repository behavior | Task-pinned upstream commit, immutable paths/symbols, and license evidence |
| Public CVF architecture or owner hint | Task-pinned public CVF commit and supplied public owner index |
| Current private-CVF ownership, overlap, or absence | Local Agent inspection of current governed private/local surfaces |
| Final technical disposition | Local reconciliation artifact backed by verified remote evidence and current local evidence |
| Implementation, provider use, publication, deployment, or destructive effect | Separate governed authority and required checkpoint |

Remote output may say `public evidence suggests`, `candidate for Local
verification`, or `current private owner unresolved`. It must not convert a
public search miss into a current private-CVF absence claim.

## Relay Integrity Contract

Every transfer must preserve these bindings:

- task ID and objective;
- task-capsule identity and digest when present;
- source repository and immutable source pin;
- public-CVF comparison pin;
- working mode and effect boundary;
- artifact filenames and content;
- return status and claim boundary.

For a binary packet or return, the sender and receiver record SHA-256. For
copy/pasted text, preserve the complete labeled block. If the transport changes
formatting, filenames, archive structure, or content, disclose the
transformation rather than claiming byte identity.

A minimal relay record contains:

| Field | Required value |
|---|---|
| Method | `cvf.cross-workspace-evidence-relay@1.0.0` |
| Task ID | Stable task identifier |
| Direction | `LOCAL_TO_REMOTE` or `REMOTE_TO_LOCAL` |
| Artifact identity | Filename, message label, or bounded artifact list |
| Integrity | SHA-256 for files, or `TEXT_RELAY_NOT_BYTE_STABLE` with reason |
| Relay mutation | `NONE` or an explicit transformation description |
| Relay state | `SENT`, `RECEIVED`, `RETURN_FOR_REPAIR`, or `ACCEPTED_FOR_LOCAL_RECONCILIATION` |

## Remote Return Contract

The remote return is advisory candidate evidence. It must remain bound to the
task and use the required return shape from
`CVF_EXTERNAL_AGENT_RETURN_CONTRACT.md`.

For each material candidate, the remote agent provides source path and symbol,
immutable source link, producer-to-verifier-to-consumer path, positive and
fail-closed behavior, operating conditions, license note, preliminary public
owner overlap, uncertainty, and a bounded preliminary disposition.

The remote agent stops at the task's expected return status. It does not decide
current private ownership, final absorption, implementation, verification,
freeze, public release, or production readiness.

## Local Final Reconciliation

The Local Agent is the final technical decision owner because it can inspect
the current private repository, active continuity, governed owner surfaces,
prior absorbed value, parked candidates, and implementation history.

The Local Agent must:

1. preserve the received return and verify its integrity;
2. verify task, source, license, public pin, manifest, inventory, exclusions,
   and claim boundary;
3. split mixed claims into atomic observations;
4. compare each candidate with current private CVF owners;
5. actively attempt to disprove novelty and avoid duplicate owners;
6. assign the final technical disposition: `ABSORB`, `ADAPT`, `DEFER`,
   `REJECT`, `BLOCK`, or `NO_NEW_VALUE`;
7. keep knowledge value, direct import, runtime activation, package/checker
   promotion, and authority promotion as separate decisions;
8. stop before implementation unless a separate governed authority opens it.

A structurally valid return may still be rejected semantically. A damaged or
wrong-task return may be returned for repair without discarding any separately
verified useful evidence.

### Repository-Absorption Closure Eligibility

External-return reconciliation and repository absorption are different
completion claims. A Local reviewer may reconcile a packet without being
eligible to close the source repository or the owning multi-repository
program. For every repository-absorption closure, Local must record these
decisions independently:

1. architecture novelty -- whether a new owner or layer is required;
2. existing-owner overlap -- whether a current owner already covers part of
   the responsibility;
3. practical adaptation value -- whether source behavior, tests, examples,
   skills, fixtures, failure cases, or operating recipes improve that owner;
4. selected value conversion -- whether each accepted value is implemented,
   governed-deferred with a trigger, rejected with evidence, or still open.

`NO_NEW_ARCHITECTURE` and `OWNER_EXISTS` never imply `NO_NEW_VALUE`. An
external handoff, shortlist, or packet-only reconciliation cannot establish
source coverage. A closure claim requires a pinned Local source basis,
behavioral reads beyond filenames/README claims, terminal selected-value
accounting, and explicit deferred/unreviewed scope. Operator-authorized scope
exit remains possible, but must be declared as such rather than mislabeled
complete absorption.

## Research-Assisted Repository Absorption Profile

Profile identifier: `cvf.research-assisted-repository-absorption@1.0.0`

Use this profile when a Web/remote agent researches repositories while a Local
orchestrator/reviewer also receives shared-workspace worker returns. It extends
this relay method; it does not create a second absorption process or transfer
decision authority to the remote agent or operator.

The required sequence is:

1. `REFRESH_EXTERNAL_AGENT_READ_BEFORE_DISPATCH`: Local refreshes the bounded
   external brief with an as-of time, current program/tranche state, owner
   pointers, public/private boundary, exact question, source pins, return
   schema, and forbidden claims before the operator relays it.
2. `INDEPENDENT_AUDIT_QUESTION_LANES`: each audit question keeps its own task
   ID, package/return identity, digest or integrity receipt, evidence ledger,
   and Local disposition. Returns may be deduplicated only after each question
   has an independent disposition.
3. Remote work remains `ADVISORY_RESEARCH_AND_PATTERN_MAPPING`: it supplies
   source-backed mechanisms, paths, symbols, tests, licenses, limitations, and
   uncertainty. A proposed contract is advisory evidence, not a design mandate.
4. The operator transports packets and returns without adjudicating them.
5. `INTEGRITY_BEFORE_SEMANTICS`: Local validates task identity, archive/hash,
   manifest, per-file digests, source pins, exclusions, license, claim boundary,
   and return completeness before evaluating technical claims.
6. Local verifies upstream claims and then cross-checks current private CVF by
   exact paths, symbols/tests, enforcement level, mandatory path, bypasses, and
   fail behavior. `LOCAL_REPOSITORY_AUTHORITY_WINS`: contradictions are recorded
   explicitly and are not reconciled by inference.
7. Local assigns the audit-layer outcome below. An advisory contract is never
   accepted merely because it is complete or well formed.
8. Web research stops when Local has enough verified evidence to decide. It may
   reopen only for a named contradiction, missing pin/license/path, inaccessible
   source, or another decision-changing evidence gap.
9. If implementation is selected, external research closes first. Local issues
   a separate governed internal work order; shared-workspace worker evidence is
   reviewed on its own lane and is not merged with the external-return record.

Audit-layer dispositions map into the existing absorption taxonomy rather than
replacing it:

| Audit outcome | Required meaning | Existing absorption route |
|---|---|---|
| `NO_CHANGE` | CVF already owns and adequately enforces the responsibility. | `NO_NEW_VALUE` with exact owner evidence |
| `ADAPT` | An owner exists, but linkage, semantics, enforcement, or proof is incomplete. | `ADAPT` against that owner |
| `WATCH` | Only an evidence gap, demand-gated uncertainty, or observation trigger remains; no implementation is authorized. | `DEFER` or `BLOCK` with a named trigger/reason |
| `ADOPT` | A required architectural responsibility is genuinely absent and cannot map to an existing owner. | `ABSORB`, only after the high bar below is proved |

`ADOPT_HIGH_BAR` requires positive Local absence evidence across current owner
surfaces, an explicit responsibility and consumer, proof that `ADAPT` cannot
close the gap, and separate implementation authority. Public absence, an
external shortlist, or an advisory contract alone never satisfies this bar.

The machine-readable profile below protects these role, ordering, authority,
and disposition invariants. It does not claim semantic execution of a future
audit; its governed review must supply the question-specific evidence.

```json
{
  "profileId": "cvf.research-assisted-repository-absorption@1.0.0",
  "contextRefresh": "REFRESH_EXTERNAL_AGENT_READ_BEFORE_DISPATCH",
  "questionIsolation": "INDEPENDENT_AUDIT_QUESTION_LANES",
  "intakeOrder": "INTEGRITY_BEFORE_SEMANTICS",
  "contradictionAuthority": "LOCAL_REPOSITORY_AUTHORITY_WINS",
  "advisoryContract": "NOT_DEFAULT_DESIGN",
  "auditDispositions": ["NO_CHANGE", "ADAPT", "WATCH", "ADOPT"],
  "adoptThreshold": "ADOPT_HIGH_BAR",
  "implementationBoundary": "EXTERNAL_RESEARCH_CLOSED_BEFORE_INTERNAL_IMPLEMENTATION"
}
```

## Cardinality And Independence

This method works with `1..N` remote agents. Cardinality is not a maturity or
trust score.

When a task explicitly requires independent returns, the operator withholds
the other returns until each designated remote agent finishes. Otherwise,
iterative repair, critique, or evidence enrichment may be relayed between the
remote agent and Local Agent. Every return keeps a distinct artifact identity
and validation receipt.

Local verification is required in every case. Additional remote agents add
perspectives or contradiction tests; they never replace local final
reconciliation.

## Failure And Repair States

| Condition | Required result |
|---|---|
| Wrong task, repository, commit, working mode, or forbidden effect | `TASK_CAPSULE_DRIFT` and `RETURN_FOR_REPAIR` |
| Missing or mismatched file integrity | `BLOCKED_INTEGRITY` |
| Missing source/license evidence | `RETURN_FOR_REPAIR` or source-bounded `BLOCK` |
| Public-CVF absence presented as private/local absence | downgrade to hypothesis and require Local verification |
| Remote claim presented as CVF authority or final acceptance | reject the authority claim and retain only independently verifiable evidence |
| Operator relay altered content without disclosure | `RELAY_TRANSFORMATION_UNDISCLOSED` and re-establish the binding |
| Evidence is valid but duplicates a current owner | `NO_NEW_VALUE` or `CONFIRMED_EXISTING`, as applicable |

## Continuity And New-Chat Recovery

Any Local Agent resuming this task class reads, in order:

1. `AGENTS.md` and the active session front door;
2. `docs/reference/external_agent_review/README.md`;
3. this method;
4. the task capsule and outbound relay identity;
5. the exact remote return and its validation receipt;
6. current private-CVF owner and continuity surfaces needed for reconciliation.

Chat history and provider memory may aid discovery but are not continuity or
source authority. The latest relay state, artifact digest, unresolved repair,
and local disposition must be recorded in a governed task or handoff surface
when the work continues across sessions.

## Relationship To Existing CVF Owners

| Existing owner | Relationship |
|---|---|
| `CVF_EXTERNAL_AGENT_PROTOCOL_REPRESENTATION_CONTRACT.md` | Owns portable protocol identity, precedence, freshness, and return-validation semantics. |
| `CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md` | Owns atomic returned-finding classification. |
| `CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | Owns the end-to-end intake route from evidence to governed CVF surfaces. |
| `CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | Owns corpus, value, owner, maturity, and completion evidence for actual absorption work. |
| `CVF_CROSS_WORKSPACE_DOMAIN_FUNNEL_ABSORPTION_METHOD.md` | Owns multi-repository domain grouping, evidence filters, shortlist convergence, and delayed CVF comparison. |
| This method | Owns the operator-mediated transport and responsibility boundary between non-shared workspaces. |

## Required Read Trigger

Read this method whenever:

- repository research is performed on a Web or remote surface without access
  to the Local Agent's workspace;
- the operator carries a packet, prompt, question, repair request, or return
  between those surfaces;
- a Local Agent receives a remote research return for current private-CVF
  reconciliation;
- a resumed chat must recover who owns transport, research, verification, and
  final technical disposition.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external knowledge intake routing guard implementation |
| Chain map route | local task binding -> operator relay -> remote source research -> operator relay -> Local validation and reconciliation -> bounded final technical disposition |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py` |
| Owner surface | `docs/reference/external_agent_review/CVF_CROSS_WORKSPACE_EVIDENCE_RELAY_METHOD.md` |
| Disposition | ADAPT the existing round-trip and returned-finding owners with a transport-neutral cross-workspace coordination profile |
| Claim boundary | coordination and evidence-relay method only; no remote output promotion, implementation, provider use, publication, deployment, or production claim |

## Epistemic Process Block

Epistemic Process Applicability: EPISTEMIC_PROCESS_NA_WITH_REASON: this method
records the operator-selected coordination and authority boundary. It does not
claim measured quality uplift, runtime behavior, provider behavior, or complete
absorption of any particular source.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this bounded change establishes the private/local coordination method.
Portable packet or public projection refresh requires a separately verified
and authorized synchronization step.

## Claim Boundary

This method standardizes evidence transport across non-shared workspaces. It
does not prove that a remote agent read the packet, that a relay was byte-stable
without a recorded digest, that a returned claim is correct, that any source
has been absorbed, or that implementation is authorized. Local technical
disposition does not bypass the separate governance required for code, runtime,
provider use, public mutation, deployment, destructive effects, or production.
