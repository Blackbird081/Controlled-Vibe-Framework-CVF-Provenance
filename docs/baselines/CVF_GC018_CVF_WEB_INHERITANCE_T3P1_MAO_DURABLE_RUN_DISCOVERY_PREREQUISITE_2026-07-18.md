# CVF GC-018 Baseline - MAO Durable Run Discovery Prerequisite

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: CVF-WEB-INHERITANCE-T3P1

Dispatch base head: `0e7904349`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator under standing roadmap-continuation authority

Reviewer owner: CVF independent reviewer/closer

Worker target: delegated implementation worker

## Purpose

Close only the first prerequisite identified by accepted T3A: add a
deterministic, read-only, fail-closed run-discovery method to the existing
`MaoFileRunStore` without adding Web, evidence, heartbeat, configuration, or
execution behavior.

## Scope / Target / Owner Boundary

The execution-plane durable store remains the sole owner of snapshot
validation and replay. This tranche may extend that owner, its local barrel,
and its two focused tests. It may not edit cvf-web or invent a second store.

## Dependency Release Evidence

| Dependency | Artifact | Material commit | Disposition |
|---|---|---|---|
| T3A accepted | `docs/reviews/CVF_WEB_INHERITANCE_T3A_COMPLETION_REVIEW_2026-07-18.md` | `c0d88ff34` | ACCEPT |
| T3P1 roadmap row | `docs/roadmaps/CVF_WEB_CAPABILITY_INHERITANCE_AND_OPERATOR_PROJECTION_ROADMAP_2026-07-18.md` | dispatcher material commit for this packet | ACCEPT |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| run snapshots use SHA-256 filenames derived from task-graph IDs | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | `snapshotFileNameFor` | `snapshotFileNameFor` | durable run store | ACCEPT |
| resume validates schema, graph identity, authority, sequence, and replay | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | `loadAndReplay` | `loadAndReplay` | `MaoFileRunStore` | ACCEPT |
| durable store currently exposes no discovery method | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | `MaoFileRunStore` public methods | `MaoFileRunStore` | durable run store | ACCEPT |
| local MAO barrel owns durable-store type and value exports | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts` | durable run store export block | `MaoDurableRunResumeSuccess`; `MaoFileRunStore` | MAO local barrel | ACCEPT |
| package root forwards the local MAO barrel | LITERAL_INVARIANT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/index.ts` | final export line | `./mao` | execution-plane package root | ACCEPT |
| focused durable-store test already owns isolated filesystem cases | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.durable.run.store.test.ts` | `MaoFileRunStore` suite | `MaoFileRunStore` | focused vitest suite | ACCEPT |
| package-root test owns MAO discoverability proof | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.package.root.exports.test.ts` | package-root discoverability suite | `execution package root MAO discoverability` | focused vitest suite | ACCEPT |

## New Doc-Only Fields

| Field | Required value boundary |
|---|---|
| `discoveryReadContract` | proposed API and exact fail-closed behavior |
| `canonicalSnapshotPolicy` | canonical snapshot, temporary file, and unrelated entry handling |
| `mutationProof` | before/after filesystem evidence that discovery writes nothing |

## Proposed Source Contract

The following symbols are new proposals, not existing-source claims:

- `MaoDurableRunListSuccess` with `ok: true` and
  `taskGraphIds: readonly string[]`;
- `MaoFileRunStore.listRunIds()` returning the list-success type or the
  existing `MaoDurableRunStoreFailure` union.

The method must return an empty successful list when the root does not exist,
inspect only canonical lowercase 64-hex `.json` snapshot names, ignore known
atomic temporary files and unrelated noncanonical entries, fully validate and
replay every canonical snapshot, fail closed on any invalid canonical
snapshot, verify filename-to-graph-ID hash agreement, sort IDs
lexicographically, and perform no write or directory creation.

## Baseline Decision

Dispatch the narrow execution-plane prerequisite. Existing full replay
validation remains authoritative; discovery adds identity enumeration only.

## Verification / Evidence

Evidence requires focused and full package tests, TypeScript checking,
missing-root and byte-preservation proof, package-root import proof, exact
five-path status, empty cached diff, unchanged execution HEAD, worker-return
fast gate, and governed file-size enforcement.

## Current Runtime Freshness Verification

At dispatch base `0e7904349`, direct source re-read confirms that
`MaoFileRunStore` has create, resume, and append methods but no discovery
method. Snapshot names are lowercase SHA-256 digests plus `.json`, full trust
is owned by `loadAndReplay`, and the package root forwards the local MAO
barrel. These facts are current dispatch evidence, not carried-forward memory.

## Allowed Scope

1. `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts`
2. `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts`
3. `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.durable.run.store.test.ts`
4. `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.package.root.exports.test.ts`
5. `docs/reviews/CVF_WEB_INHERITANCE_T3P1_WORKER_RETURN_2026-07-18.md`

## Forbidden Scope

- no cvf-web package, lockfile, source, test, page, route, or configuration;
- no evidence-ledger persistence, heartbeat persistence, operator projection,
  worker launch, provider call, run creation, event append, or new storage
  root convention;
- no weakening, bypass, or duplication of `loadAndReplay` validation;
- no registry, generated aggregate, session, public-sync, push, release, or
  production mutation; and
- no staging, stash, or worker commit.

## Acceptance Criteria

- AC-01: missing root returns `{ ok: true, taskGraphIds: [] }` without creating
  the root.
- AC-02: one and multiple valid snapshots return unique graph IDs in stable
  lexicographic order through full existing replay validation.
- AC-03: temporary and unrelated noncanonical entries are ignored; any corrupt,
  mismatched, or replay-invalid canonical snapshot fails closed using an
  existing failure reason.
- AC-04: repeated discovery is deeply equal and leaves directory entries and
  canonical snapshot bytes unchanged.
- AC-05: the new success type is exported through the local and package-root
  barrels and focused root-import proof passes.
- AC-06: focused tests, full package tests, TypeScript, worker-return fast gate,
  and governed file-size enforcement pass.
- AC-07: exactly five allowed paths change; nothing is staged; execution HEAD
  is unchanged.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`backend`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class backend --role dispatcher --lifecycle-phase pre-dispatch --surface-selector execution-plane --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Status; Scope / Target / Owner Boundary; Dependency Release Evidence; Source Verification Block; New Doc-Only Fields; Allowed Scope; Forbidden Scope; Acceptance Criteria; ADIF Defect Registry Disclosure; Public Export Disposition; Claim Boundary |
| gateRunPurpose | dispatch confirmation after direct source verification |
| claimBoundary | structural conformance does not prove the proposed method |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-WEB-INHERITANCE-T3P1 --title "MAO Durable Run Discovery Prerequisite" --date 2026-07-18 --base 0e7904349 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled exact source contract, five-path boundary, tests, and no-Web prerequisite scope |
| checkerReadAheadConfirmation | checker paths listed above |
| docOnlyNewFields | three fields listed in New Doc-Only Fields |
| claimBoundary | dispatch-authoring provenance only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance prerequisite dispatch; no public-sync action.

## Claim Boundary

This baseline authorizes one read-only run-discovery extension and focused
tests only. It does not authorize Web adoption, evidence or heartbeat
persistence, execution, provider/live, public, push, release, production, or
session mutation.
