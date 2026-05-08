<!-- Memory class: FULL_RECORD -->
# CVF RC2 Module Runtime Classification Audit

Date: 2026-05-08

Status: CLOSED BASELINE FOR TRACK B

## Scope

This audit classifies the core modules named in RC2 Foundation V3. It does not
add Web endpoints, module registry code, health UI, or facades.

## Classification Legend

Runtime class:

- `PRESENT_DOCS_ONLY`: module exists but no current runnable/runtime code was
  found.
- `HAS_RUNTIME_CODE`: module contains runtime/source code.
- `RUNNABLE_CLI_ONLY`: module has package scripts/tests/checks but no current
  Web visibility as a module.
- `WEB_VISIBLE_READ_ONLY`: Web can inspect it but cannot run module actions.
- `WEB_RUNNABLE`: Web can run or directly exercise this surface today.

Web exposure:

- `WEB_RUNNABLE`: already exercised through the Web app.
- `NOT_EXPOSED`: no dedicated Web module visibility/control surface.
- `PARTIAL_INHERITED`: used by Web indirectly, but not exposed as an operator
  module surface.

## Audit Matrix

| Module | Path | Runtime Evidence | Runtime Class | Web Exposure | B1/B2 Treatment |
|---|---|---|---|---|---|
| `cvf-web` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web` | Next app, API routes, 519 source files, 218 tests, `dev/build/start/test/e2e` scripts | `WEB_RUNNABLE` | `WEB_RUNNABLE` | Health source of truth for Web app readiness |
| `guard-contract` | `EXTENSIONS/CVF_GUARD_CONTRACT` | package, `src/index.ts`, 42 source files, 16 tests, `check/test` scripts | `RUNNABLE_CLI_ONLY` | `NOT_EXPOSED` | List in registry as runnable package, not Web-controlled |
| `phase-governance-runtime` | `EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL` | governance/runtime TS files, guard runtime, CLI/API/MCP adapters, 14 tests, `build/test/check` scripts | `RUNNABLE_CLI_ONLY` | `NOT_EXPOSED` | List as governance runtime; no facade until specific action is proven |
| `control-plane-foundation` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION` | package, `src/index.ts`, 159 source files, 122 tests, `check/test` scripts | `RUNNABLE_CLI_ONLY` | `PARTIAL_INHERITED` | Web may depend on parts, but module status is not Web-visible yet |
| `execution-plane-foundation` | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION` | package, `src/index.ts`, 67 source files, 54 tests, `check/test` scripts | `RUNNABLE_CLI_ONLY` | `NOT_EXPOSED` | Registry read-only first |
| `governance-expansion-foundation` | `EXTENSIONS/CVF_GOVERNANCE_EXPANSION_FOUNDATION` | package, `src/index.ts`, 41 source files, 35 tests, `check/test` scripts | `RUNNABLE_CLI_ONLY` | `NOT_EXPOSED` | Registry read-only first |
| `learning-plane-foundation` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION` | package, `src/index.ts`, 66 source files, 45 tests, `check/test` scripts | `RUNNABLE_CLI_ONLY` | `PARTIAL_INHERITED` | Web knowledge features may use related ideas, but no module surface yet |
| `model-gateway` | `EXTENSIONS/CVF_MODEL_GATEWAY` | package, `src/index.ts`, wrapper/re-export merge, 2 tests | `HAS_RUNTIME_CODE` | `NOT_EXPOSED` | Mark as wrapper/coordination package, not full gateway UI |
| `policy-engine` | `EXTENSIONS/CVF_POLICY_ENGINE` | package, `src/index.ts`, policy compiler re-exports/coordination, 2 tests | `HAS_RUNTIME_CODE` | `NOT_EXPOSED` | Mark as coordination package until direct policy surface exists |
| `trust-sandbox` | `EXTENSIONS/CVF_TRUST_SANDBOX` | package, `src/index.ts`, guard/safety coordination re-exports, 2 tests | `HAS_RUNTIME_CODE` | `NOT_EXPOSED` | Mark as coordination package until sandbox action is proven |

## Abort Clause Results

No listed module is `PRESENT_DOCS_ONLY`. However, three modules are thin
wrapper/coordination packages:

- `model-gateway`
- `policy-engine`
- `trust-sandbox`

B1/B2 may include these in a read-only module registry, but must not mark them
`WEB_RUNNABLE` unless a real Web action is implemented and tested.

## B1/B2 Implementation Guidance

B1 health should start with system-level readiness:

- Web app readiness
- provider/env readiness from A1 scripts
- dependency/install readiness from A1/A2
- gate command availability

B2 module registry should be read-only first. Recommended fields:

- id
- display name
- repo path
- runtime class
- Web exposure
- package scripts
- evidence owner
- allowed next action

## Claim Boundary

Allowed after B0:

> CVF core modules have been classified for runtime presence and current Web
> exposure.

Not allowed after B0:

- CVF Web exposes runtime health.
- CVF Web exposes module registry.
- CVF Web controls runtime modules.
- CVF Web can trigger governance jobs.
