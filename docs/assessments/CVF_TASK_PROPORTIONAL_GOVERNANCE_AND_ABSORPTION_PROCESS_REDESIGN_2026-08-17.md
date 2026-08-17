# CVF Task-Proportional Governance And Absorption Process Redesign

Memory class: FULL_RECORD

Status: DESIGN_COMPLETE_PENDING_IMPLEMENTATION

docType: assessment

Date: 2026-08-17

Decision: `ADOPT_TASK_PROPORTIONAL_GOVERNANCE_ROUTING`

## Purpose

Redesign CVF governance so control strength follows the task's authority,
external effects, reversibility, uncertainty, and blast radius. The number of
guards executed or sections written is not a safety metric. The same routing
model applies to external-source absorption and future project delivery.

## Scope / Target / Owner Boundary

This artifact defines the target operating model and migration sequence. It
does not yet change autorun commands, checker applicability, hook wiring,
current work orders, or T11 worker authority. The future owner is the CVF
orchestration and guard-routing layer; domain checkers remain owned by their
current standards.

## Operator Decision

The operator requires cost control through task discrimination: many guards
are not inherently correct, and a guard is valuable only when its protected
risk is present in the task. CVF must preserve fail-closed escalation without
making low-risk local work carry evidence designed for corpus-scale, runtime,
provider, public, or destructive operations.

## Current-State Evidence

| Observation | Source | Finding |
| --- | --- | --- |
| task-first orientation already exists | `docs/reference/guard_orientation/README.md`, Task Class Guard Map | task classes are documented but do not select the autorun command set |
| autorun builds a broad common bundle | `governance/compat/agent_autorun_command_catalog.py`, `_common_commands` | pre-dispatch currently invokes a near-global checker list and relies on each checker to self-filter |
| one standard states universal applicability | `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md`, Scope and Standard Workflow | documentation, runtime, public, live and connector work share the same four phase gates |
| review cost is recognized only late | `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md` | telemetry controls reviewer loops but does not prevent an oversized dispatch packet or gate bundle |
| T11 source-to-packet ratio is disproportionate | seven selected template files; commit `8996a4e0e` | 3,163 source bytes led to 1,012 added baseline/work-order lines before implementation |

## Source / Predecessor Evidence

The predecessor evidence is the active task-first Guard Orientation, autorun
workflow standard, command catalog, workflow runner, review-cost standard, and
the committed T11 dispatch packet identified in Current-State Evidence. These
sources establish the current routing, execution and observed-cost facts; this
assessment does not treat its proposed model as already implemented.

## Finding / Position

CVF has a task map but not a task-routing control plane. Applicability is
distributed across checker regexes, paths, status tokens, and keyword triggers.
That architecture has three costs:

1. every phase starts a large common command bundle even when most guards are
   semantically irrelevant;
2. authors repeat proof blocks so downstream checkers can infer applicability;
3. accidental words or paths activate unrelated evidence requirements.

The redesign moves applicability ahead of execution. A task declares one
machine-readable governance manifest. A deterministic router selects guard
families. Each selected guard enforces its own rule; each omitted guard is
recorded with a reason. Unknown or contradictory risk signals escalate rather
than silently selecting a lighter profile.

## Design Principles

1. **Risk first, artifact second.** File type helps routing but never defines
   risk by itself.
2. **One fact, one owner.** Corpus identity, hashes and provenance are recorded
   once and referenced by later clusters.
3. **Guard relevance is explicit.** A checker does not infer its own
   applicability from incidental prose when the routing manifest exists.
4. **Minimum sufficient evidence.** Every task carries core scope and result
   evidence; conditional evidence appears only for a present risk.
5. **Escalation is monotonic.** A task may move to a stronger profile when new
   evidence appears; it may not self-downgrade after dispatch.
6. **No guard-count target.** Selected, skipped, passed and failed guards are
   reported separately. A large selected count is neither success nor safety.
7. **Semantic review stays human/agent-owned.** The router selects controls; it
   does not judge whether an implementation or absorbed idea is good.
8. **Compatibility before replacement.** Existing full gates remain available
   as the elevated fallback until profile routing proves equivalent on
   high-risk tasks.

## Task Classification Contract

Each governed task declares these dimensions before authoring its execution
packet:

| Dimension | Allowed values | Meaning |
| --- | --- | --- |
| `taskKind` | `READ_ONLY`, `DOC_CHANGE`, `PURE_LOCAL_IMPLEMENTATION`, `STATEFUL_LOCAL_IMPLEMENTATION`, `EXTERNAL_ABSORPTION`, `RUNTIME_INTEGRATION`, `LIVE_PROOF`, `PUBLIC_RELEASE`, `DESTRUCTIVE_OPERATION` | primary work class |
| `authorityImpact` | `NONE`, `USES_EXISTING_OWNER`, `ENRICHES_EXISTING_OWNER`, `CREATES_OR_CHANGES_AUTHORITY` | effect on CVF source of truth |
| `externalEffect` | `NONE`, `LOCAL_REVERSIBLE`, `NETWORK_READ`, `NETWORK_WRITE`, `PUBLIC_WRITE`, `DESTRUCTIVE` | strongest possible effect |
| `dataSensitivity` | `PUBLIC`, `PRIVATE_REPO`, `CREDENTIAL_REFERENCE`, `SECRET_VALUE`, `REGULATED` | strongest data handled |
| `reversibility` | `READ_ONLY`, `GIT_REVERSIBLE`, `STATEFUL_REVERSIBLE`, `PARTIALLY_REVERSIBLE`, `IRREVERSIBLE` | recovery posture |
| `sourceScale` | `NONE`, `NAMED_FILES`, `BOUNDED_CLUSTER`, `CORPUS` | evidence enumeration scale |
| `delegation` | `SINGLE_ROLE`, `MULTI_ROLE_NO_COMMIT`, `MULTI_ROLE_WITH_COMMIT` | handoff and commit topology |
| `novelty` | `KNOWN_PATTERN`, `OWNER_COMPOSITION`, `NEW_INTERFACE`, `NEW_AUTHORITY` | design uncertainty |

The manifest also lists exact changed-path families, claims, required proof,
operator checkpoints, and explicit forbidden effects.

## Governance Profiles

| Profile | Typical task | Required control posture | Default artifact |
| --- | --- | --- | --- |
| `P0_OBSERVE` | explanation, status, diagnosis, read-only inspection | startup when material; source evidence; no mutation | response or short assessment |
| `P1_LIGHT` | small docs change or pure local implementation using an accepted owner; no external effect | core scope/diff, owner/source check, focused verification, claim boundary | compact task card; no GC-018 baseline by default |
| `P2_BOUNDED` | delegated multi-file feature or selected absorption cluster; existing owner; Git-reversible | P1 plus exact manifest, no-commit handoff when delegated, independent review, domain guards | compact work order with referenced shared evidence |
| `P3_ELEVATED` | new interface/authority, persistence, dependency, auth, network read/write, migration | full baseline/work order, rollback, security/integrity, broad regression, independent closure | current full governed packet |
| `P4_CRITICAL` | live/provider, public write, deploy, destructive/irreversible, secret value, regulated data | P3 plus explicit operator checkpoint, real receipts, diagnostic/retry controls, release/public/destructive gates | full packet and release/operation receipt |

## Mandatory Escalation Triggers

Any one of these sets the minimum profile shown:

| Trigger | Minimum profile |
| --- | --- |
| external worker or cross-role no-commit handoff | `P2_BOUNDED` |
| corpus completeness or all-files claim | `P2_BOUNDED` plus corpus bundle |
| changes a canonical standard, checker, hook, registry generator, or authority contract | `P3_ELEVATED` |
| filesystem/environment write outside generated build output | `P3_ELEVATED` |
| new dependency, installation, credential binding, authentication, persistence, migration, or network operation | `P3_ELEVATED` |
| real provider/API call, paid quota, public sync, push, deploy, production, secret value, destructive or irreversible action | `P4_CRITICAL` |
| missing, contradictory, or unclassifiable manifest evidence | fail closed to `P3_ELEVATED` pending correction |

File count, byte count and apparent simplicity may lower cost only inside a
profile; they never override an escalation trigger.

## Guard Bundle Model

Guards are registered by protected risk rather than placed in one undifferentiated
common list:

| Bundle | Selected when | Examples |
| --- | --- | --- |
| `CORE_INTEGRITY` | every mutating task | base/status, exact scope, diff check, encoding, file size, claim boundary |
| `ARTIFACT_SHAPE` | governed artifact types actually changed | work-order, roadmap, review, reference, registry shape |
| `SOURCE_PROVENANCE` | external/mixed-origin input or source claims | source verification, mirror migration, overlap/value conversion |
| `CORPUS_ACCOUNTING` | `sourceScale=CORPUS` or a completeness claim | manifest, ledger, reconciliation, corpus-delta refresh, knowledge map |
| `DELEGATION_HANDOFF` | multi-role execution | handoff, return shape, commit ownership, cross-batch isolation |
| `CODE_QUALITY` | implementation source changed | focused tests, type/build, package regression selected by package owner |
| `STATE_AND_SECURITY` | state, auth, secret reference, persistence, dependency, install or mutation | rollback, secret discipline, integrity, approval and migration controls |
| `RUNTIME_LIVE` | runtime integration or live proof | real-call proof, diagnostics, retry, cost/quota and receipt controls |
| `PUBLIC_RELEASE` | public write, push, deploy or production claim | repository boundary, export disposition, release and public drift guards |
| `CONTINUITY` | current mode/authority/next move changes | state generator, active handoff and next-move freshness |
| `DOMAIN_*` | target owner declares a domain-specific bundle | Web/UI, ASSF, Model Gateway, Execution Plane, workspace, or other owner controls |

`CORE_INTEGRITY` is small and stable. All other bundles require a manifest
predicate. Global repository-health checks run on scheduled/pre-push lanes,
not on every P1/P2 edit unless the changed path intersects their owner.

## Routing Algorithm

1. Read changed/intended paths and the task manifest.
2. Validate classification values and detect escalation triggers.
3. Compute the minimum profile; reject any requested profile below it.
4. Select `CORE_INTEGRITY`, lifecycle bundles and domain bundles using the
   registry's explicit predicates.
5. Produce a routing receipt containing selected guards, skipped guards with
   reason codes, profile, triggers, estimated command count and evidence budget.
6. Run only selected guards for the phase.
7. If a guard discovers a new trigger, invalidate the receipt, escalate the
   profile and regenerate before continuing.
8. At pre-push, run the full repository/release bundle regardless of prior
   local profiles.

No checker may silently promote itself from skipped to applicable through a
keyword match once a valid routing receipt exists. Until migration completes,
legacy inference remains a compatibility fallback and discrepancies are
reported, not hidden.

## Evidence Budget And Cost Controls

| Profile | Dispatch evidence budget | Verification budget | Review/commit posture |
| --- | --- | --- | --- |
| `P0_OBSERVE` | none or one short assessment | targeted reads | no commit unless artifact requested |
| `P1_LIGHT` | one compact task card, normally 6-10 fields | focused check plus package-owner minimum | one material commit; review proportional to diff |
| `P2_BOUNDED` | one compact work order; shared provenance referenced, not copied | focused + composed/domain regression + selected gate bundle | independent review; one material and optional continuity commit |
| `P3_ELEVATED` | full baseline/work order | full affected-package and authority/security gates | independent review and explicit rollback |
| `P4_CRITICAL` | full packet plus operation/release envelope | P3 plus live/public/destructive receipts | operator checkpoint and separate release/operation closure |

Budgets are diagnostic ceilings, not permissions to omit critical evidence.
Exceeding a P1/P2 budget requires either consolidation or profile escalation
with a reason. Documentation line count is monitored as a cost signal but is
never used alone to select risk.

## Redesigned Absorption Flow

### Stage A - Corpus Intake Once

Enumerate, hash and create the terminal processing ledger once per immutable
corpus snapshot. Record whether each row received metadata parsing, semantic
sampling, or full semantic reading. Never equate a terminal ledger row with a
full semantic read.

### Stage B - Cluster Selection

Select a coherent owner/use-case cluster from the ledger. Recompute only its
hashes and fully read every selected file. Record cluster membership and the
selection reason in a small delta ledger.

### Stage C - Proportional Route

Classify the intended conversion. A small pure cluster mapped to an existing
owner normally routes to `P2_BOUNDED` when delegated and `P1_LIGHT` when the
same authorized agent implements/reviews locally. Runtime, state, acquisition,
provider, public and authority triggers escalate independently.

### Stage D - Compact Absorption Card

For P1/P2, record only:

- corpus snapshot/ledger reference;
- selected paths and hashes;
- full-read confirmation for selected files;
- extracted value and existing owner overlap;
- adapt/defer/reject decision;
- exact changed paths and acceptance proof;
- authority and external-effect boundary.

Corpus completeness, corpus-delta and knowledge-map blocks are inherited from the
snapshot receipt unless corpus membership or a completeness claim changes.

### Stage E - Implement And Verify

Implement against current owner surfaces, run focused/domain verification and
the selected guard bundle, then perform proportional independent review.

### Stage F - Delta Closure

Append cluster disposition to the delta ledger and link accepted material.
Do not rewrite the 205-row base ledger or session continuity unless its owned
state actually changes. Periodic roll-up reconciles cluster deltas back to the
base corpus.

## Redesigned Project-Delivery Flow

The same router governs ordinary project construction:

| Project task | Expected route |
| --- | --- |
| typo, local copy or style repair | `P1_LIGHT` plus artifact/domain shape |
| pure utility or bounded component under an existing interface | `P1_LIGHT` or delegated `P2_BOUNDED` plus code-quality bundle |
| feature spanning several existing components | `P2_BOUNDED` plus affected domain bundles |
| database/state migration, auth, installer, dependency or network integration | `P3_ELEVATED` plus state/security/rollback |
| provider/live validation | `P4_CRITICAL` plus runtime/live receipt |
| release, public push or deployment | `P4_CRITICAL` plus public/release bundle |

A project does not become safer because every feature runs release, corpus,
provider and memory guards. It becomes safer when the router reliably selects
the controls protecting the feature's actual failure modes and escalates when
those failure modes change.

## Proposed Routing Receipt

The implementation should emit a small machine-readable receipt shaped like:

```json
{
  "schemaVersion": "cvf.taskGovernanceRoute.v1",
  "taskId": "example",
  "profile": "P2_BOUNDED",
  "classification": {
    "taskKind": "EXTERNAL_ABSORPTION",
    "authorityImpact": "ENRICHES_EXISTING_OWNER",
    "externalEffect": "NONE",
    "sourceScale": "BOUNDED_CLUSTER",
    "delegation": "MULTI_ROLE_NO_COMMIT"
  },
  "escalationTriggers": ["DELEGATED_NO_COMMIT"],
  "selectedBundles": ["CORE_INTEGRITY", "SOURCE_PROVENANCE", "DELEGATION_HANDOFF", "CODE_QUALITY"],
  "skippedBundles": {
    "CORPUS_ACCOUNTING": "INHERITED_IMMUTABLE_SNAPSHOT_NO_COMPLETENESS_CHANGE",
    "RUNTIME_LIVE": "NO_RUNTIME_OR_LIVE_EFFECT",
    "PUBLIC_RELEASE": "NO_PUBLIC_EFFECT"
  },
  "receiptStatus": "ROUTED"
}
```

The receipt contains no authority grant. It is a deterministic explanation of
which controls apply.

## Fail-Closed And Anti-Gaming Rules

- A manifest cannot declare `externalEffect=NONE` while allowed paths or
  commands include network, provider, deploy, installer or destructive owners.
- Changed paths are reconciled against declared path families before closure.
- Domain owners may add escalation triggers but may not silently remove core
  triggers.
- `P1_LIGHT` cannot change a standard, checker, hook, generator, authority
  registry, public surface, persistence schema, auth boundary or dependency.
- Splitting one change into several micro-tasks does not lower the aggregate
  profile when they share one authority/effect objective.
- Missing skipped-guard reasons invalidate the routing receipt.
- Router/legacy disagreement chooses the stronger route until reviewed.

## Migration Plan

### TPGR-T0 - Registry And Dry-Run Router

Create a canonical profile/bundle registry, schema, deterministic read-only
router and tests. Run it in shadow mode beside current autorun. No checker or
gate is skipped yet.

### TPGR-T1 - Compact P1/P2 Artifact Contract

Define the compact task/absorption card and inheritance references. Add tests
proving small pure work no longer needs unrelated corpus/runtime/public blocks.

### TPGR-T2 - Selective Autorun

Make autorun consume a valid routing receipt and execute selected bundles.
Keep legacy full-gate fallback for missing/invalid receipts and all P3/P4 work.

### TPGR-T3 - Project-Delivery Adoption

Bind package/domain owners to `DOMAIN_*` bundles and migrate common feature,
bugfix, refactor, state, runtime and release task templates.

### TPGR-T4 - Equivalence And Cost Acceptance

Replay representative historical P1-P4 tasks. Require zero missed applicable
failures, deterministic escalation, measurable command/packet reduction for
P1/P2, and unchanged P3/P4 release protection before retiring legacy inference.

## Baseline Decision / Proposed Tranche

Decision: `ADOPT_TASK_PROPORTIONAL_GOVERNANCE_ROUTING` as the target design.
The first implementation tranche is TPGR-T0 only: registry, schema, dry-run
router, focused tests and shadow receipts. It must not skip or reorder any
current gate. Selective execution remains unauthorized until TPGR-T2 and its
equivalence evidence are independently accepted.

## Acceptance Criteria For Implementation

1. The same manifest always produces the same profile and selected bundles.
2. Every mandatory trigger escalates to at least its required profile.
3. Unknown, contradictory and path-mismatched manifests fail closed.
4. P1/P2 examples omit unrelated guards with explicit machine reasons.
5. P3/P4 examples retain current high-risk controls.
6. Selected-file absorption requires full semantic read; corpus intake records
   its actual read depth separately.
7. Full pre-push/release checking remains available and mandatory when invoked.
8. Shadow replay shows no previously caught relevant defect is lost.
9. Cost evidence reports command count, elapsed time, artifact lines and repair
   rounds without converting those metrics into authority.
10. Rollback to legacy full routing is deterministic and documented.

## Risks / Corrective Action

| Risk | Corrective action |
| --- | --- |
| under-classification omits a necessary guard | mandatory triggers, changed-path reconciliation and stronger-route fallback |
| profiles become another bureaucracy | keep five profiles, stable dimensions and generated receipts; prohibit per-task custom profile invention |
| cost optimization weakens security | security/state/live/public triggers set profile floors that byte/file budgets cannot override |
| domain guards disappear from the common bundle | domain-owner registry and shadow equivalence tests |
| inherited corpus evidence becomes stale | snapshot/hash binding and cluster hash recomputation |
| agents game tasks by splitting them | objective/effect aggregation rule and reviewer merge of dependent micro-tasks |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/agent_autorun_command_catalog.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/check_review_cost_control.py`; current task-first Guard Orientation source |
| literalTokensReviewed | assessment structural headings, status, source paths, Public Export Disposition and Claim Boundary |
| gateRunPurpose | validate this design artifact without activating its proposed routing behavior |
| claimBoundary | design evidence only; checker/router changes require a separate authorized implementation tranche |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- N/A with reason: this artifact designs a future routing process and does not
  refresh, reclassify, or claim completeness for any corpus. Existing T0
  manifests and ledgers are cited only as observed process evidence.

## Epistemic Process Block

### Expected Result / Prediction

Moving applicability to a pre-gate routing manifest should reduce P1/P2 packet
and command cost while retaining or strengthening P3/P4 protection.

### Evidence Comparison

Current sources show a task-class map and cost telemetry, but autorun still
constructs a broad common bundle. T11 demonstrates that this gap produces
large evidence overhead for a small pure cluster.

### Contradiction Or Gap Disposition

The redesign is accepted as the target architecture. Runtime equivalence and
cost reduction remain unproven until TPGR-T0 through TPGR-T4 execute.

### Claim Update

CVF should measure safety by relevant-risk coverage and fail-closed escalation,
not by raw guard count or packet length.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private governance design; no public-sync action is authorized.

## Claim Boundary

This artifact completes the process design only. It does not activate a lighter
gate, skip an existing guard, change current T11 authority, modify runtime,
perform provider/live work, alter public-sync behavior, deploy, or claim that
the proposed router has passed equivalence testing.
