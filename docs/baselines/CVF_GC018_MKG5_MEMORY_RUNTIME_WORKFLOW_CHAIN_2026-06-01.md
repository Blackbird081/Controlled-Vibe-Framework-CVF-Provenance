# CVF GC-018 - MKG5 Memory Runtime Workflow Chain

Memory class: FULL_RECORD

Status: AUTHORIZED_FOR_IMPLEMENTATION

docType: baseline

Date: 2026-06-01

## Purpose

Authorize the first bounded runtime-system tranche for the Memory/Knowledge
plane after MKG1-MKG4 established doc-only owner mapping and worker evidence
discipline.

MKG5-T1 turns existing Memory runtime contracts into one deterministic workflow
chain: memory retrieval event hook -> controlled memory gateway -> retrieval
policy -> summary-only context packager -> context-packaged event receipt.

## Scope / Target / Owner Boundary

Target owner surface:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/memory-runtime-workflow-chain.test.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/index.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-activation.barrel.ts`

Boundary:

- Learning Plane Foundation runtime contract only;
- same-package LPF barrel split required by GC-023 maintainability remediation;
- no web route or provider execution wiring;
- no raw memory release or prompt reinjection;
- no graph persistence mutation.

## Decision

Decision: operator explicitly requested that Memory become a real system, not
only a documentation/governance surface.

MKG5-T1 is authorized for Learning Plane Foundation runtime contract code and
focused tests only. It does not authorize web route wiring, live provider
proof, prompt injection, raw memory release, graph persistence mutation,
public-sync, push, or autonomous mutation.

## Runtime Owner Surface

| Owner surface | Source path | Disposition |
| --- | --- | --- |
| Memory event hooks | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-event-hooks.ts` | ACCEPT |
| Controlled memory gateway | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | ACCEPT |
| Memory retrieval policy | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | ACCEPT |
| Memory context packager | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts` | ACCEPT |
| Runtime memory hierarchy | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts` | ACCEPT |

## Source / Predecessor Evidence

Predecessors:

- MKG1 mapped 47 Memory/Knowledge/Graph authority assets and deferred runtime
  candidates that lacked owner verification.
- MKG2 triaged the deferred runtime candidate set.
- MKG3 confirmed current non-Legacy negative owner evidence for cortex,
  governed skill evolution, and graph runtime groups.
- MKG4 hardened worker gate-evidence consistency before returning to runtime
  Memory work.

Current source evidence:

- Learning Plane Foundation already owns Memory event hooks, controlled gateway,
  retrieval policy, context packaging, runtime hierarchy, durable memory store,
  and graph-advisory contracts.
- MKG5-T1 composes existing owner modules instead of inventing a new memory tier
  or new provider route.

## Required Evidence

- add one runtime workflow-chain module under Learning Plane Foundation;
- add focused tests proving allowed, denied, and no-match fail-closed behavior;
- prove `rawMemoryReleased=false` and `canReinject=false` across the chain;
- run focused test, TypeScript check, dispatch-quality gate, and pre-dispatch
  autorun gate;
- leave route/live/provider wiring for a later GC-018 tranche.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private runtime-foundation tranche only. No public-sync remote, public
repository commit, or public artifact path is included.

## Claim Boundary

MKG5-T1 authorizes a deterministic Memory runtime workflow contract and focused
tests. It does not authorize `/api/execute` route wiring, live provider proof,
prompt reinjection, raw memory release, graph retrieval persistence mutation,
hosted readiness, production readiness, public readiness, public-sync, push, or
autonomous mutation.
