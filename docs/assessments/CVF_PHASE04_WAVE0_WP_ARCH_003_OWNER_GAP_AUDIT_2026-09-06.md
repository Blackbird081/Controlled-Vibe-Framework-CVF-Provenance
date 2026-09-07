# CVF Phase-04 Wave 0 WP-ARCH-003 Owner Gap Audit Assessment

Memory class: governed-worker-audit

docType: baseline

Status: COMPLETE_PENDING_REVIEW

Date: 2026-09-06

Batch ID: P04-W0-ARCH003-T0

reworkGeneration: 1

rootCauseClusterId: P04_W0_ARCH003_CANONICAL_OWNER_VS_COMPATIBILITY_SURFACE

executionBaseHead: dcdd34094bce61fe68deb620abb70563edaab0fd

Commit mode: WORKER_MUST_NOT_COMMIT

## Purpose

Perform the mandatory high-risk pre-implementation gate for `WP-ARCH-003`
(Principal, Scope, Delegation & Version-Bound Grant Contract). Reconcile the
three retained acceptance obligations (`ARCH-ABS-007`, `ARCH-ABS-017`,
`ARCH-ABS-021`) against current owner contracts and tests, and freeze the
smallest truthful successor manifest. This assessment does not implement the
WP. This is the Rework Round 1 correction of the initial audit, closing four
independent-reviewer findings (`R1-01` through `R1-04`) recorded in
`docs/work_orders/CVF_AGENT_WORK_ORDER_PHASE04_WAVE0_WP_ARCH_003_OWNER_GAP_AUDIT_AMENDMENT_1_2026-09-06.md`.

## Scope / Applies To

Bounded named-source audit against the accepted Phase-03R planning contract
for `WP-ARCH-003` and the current committed state of
`EXTENSIONS/CVF_GUARD_CONTRACT/`, `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/`,
`EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/`, and `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/`
at `executionBaseHead`. No source, test, runtime, governance, session, or
public artifact is mutated by this assessment.

## Source / Predecessor Evidence

Predecessor evidence: `docs/reviews/CVF_PHASE03R_CANONICAL_PLANNING_MATERIALIZATION_COMPLETION_2026-09-05.md`
(`CLOSED_PASS_BOUNDED`, material `0b8398f6e67c1fe48eb95fdfee8fd22c9524b7d6`)
accepted the `WP-ARCH-003` `COLLAPSE_INTO_EXISTING_OWNER` disposition and its
11 exact baseline-symbol replacements as a documentation-only planning
materialization. Source contract:
`.private_reference/legacy/CVF 05.09/03R_CVF_IMPLEMENTATION_WORK_PACKAGE_LEDGER.md`
lines 412-520 (`WP-ARCH-003` full contract block; the Local Phase-03R
Correction note there states the 11 original downstream WP-to-WP edges are
each replaced by a direct consumer obligation against an exact existing
baseline symbol). Wave placement and baseline-symbol mapping:
`03R_CVF_GLOBAL_IMPLEMENTATION_PLAN.md` Wave 0 list and Section 4;
`03R_CVF_IMPLEMENTATION_DEPENDENCY_MAP.md` Section 4 exact edge-to-symbol
table. Acceptance/security/compatibility rows:
`03R_CVF_IMPLEMENTATION_ACCEPTANCE_MATRIX.md`.

Rework Round 1 correction to this section: **Phase-03R already selected
`EXTENSIONS/CVF_GUARD_CONTRACT/` as the canonical owner of `AuthorityGateGuard`
and `ScopeGuard`.** The Local Phase-03R Correction note explicitly names the
owning files as `EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/authority-gate.guard.ts`,
`EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/scope.guard.ts`, and
`EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-owner-binding.contract.ts`.
No operator/reviewer re-selection of the owner is required or requested by
this corrected audit.

## Decision / Baseline / Proposed Tranche

Terminal decision: `BOUNDED_DELTA_REQUIRED`.

Current source proves the canonical owner (`EXTENSIONS/CVF_GUARD_CONTRACT/`)
already implements `AuthorityGateGuard`, `ScopeGuard`, and the full
version-bound capability-grant chain, and that the live MCP production
composition roots (`src/index.ts`, `src/sdk.ts`, and every other production
composition file named in the canonical-adoption regression test) import the
guard engine and factory from the canonical `cvf-guard-contract` package, not
from a local fork. Two of the three acceptance criteria nonetheless remain
`PARTIAL`/`MISSING` for consumer/test-evidence reasons unrelated to any owner
dispute. This audit therefore freezes an exact bounded successor manifest
below rather than declaring the WP already satisfied or blocked on an owner
conflict.

## Terminal Finding Disposition Table (Rework Round 1)

| ID | Reviewer finding | Corrected disposition in this assessment |
|---|---|---|
| R1-01 | `BLOCKED_OWNER_CONFLICT` rested on a false unresolved-owner premise | RETRACTED. Phase-03R already names `EXTENSIONS/CVF_GUARD_CONTRACT/` as the sole canonical owner of `AuthorityGateGuard`/`ScopeGuard`. The `CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL` and `CVF_ECO_v2.5_MCP_SERVER` package-local classes are recorded below as compatibility/backward-compatible surfaces, not as a live owner dispute requiring a fresh operator selection. |
| R1-02 | The prior return called the MCP package-local guard classes a live production engine | CORRECTED. Direct read of `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` line 38 confirms `createGuardEngine` and `GuardRuntimeEngine` are imported from `cvf-guard-contract`, and the module-level singleton `engine` at line 57 is built from that canonical import, not from `./guards/index.js`. `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/sdk.ts` lines 17-36 re-export the same canonical `GuardRuntimeEngine`/`createGuardEngine` from `cvf-guard-contract`, while separately re-exporting the package-local guard classes and constants as backward-compatible SDK surfaces. `createUnifiedRegistry` in `src/registry/guard-registry.ts` has zero non-test in-repository callers (only `src/integration/e2e-pipeline.test.ts` and `src/registry/guard-registry.test.ts` call it; `sdk.ts` only re-exports the symbol, it does not invoke it). |
| R1-03 | The prior return omitted the exact future manifest by choosing the wrong terminal branch | CORRECTED. Terminal decision is now `BOUNDED_DELTA_REQUIRED`. See the Required Compatibility, Migration, Rollback, And Fixture Plan and Exact Future Manifest sections below for the frozen successor scope. |
| R1-04 | Evidence accounting was internally inconsistent and readiness fields remained pending | CORRECTED. The 11 downstream WP-to-WP edges (WP-ARCH-003's own Local Phase-03R Correction count) are now kept distinct from the unrelated 18-edge count that appears in `03R_CVF_GLOBAL_IMPLEMENTATION_PLAN.md` (18 removed `WP-ARCH-003 -> *` **and** `WP-MCP-001 -> *` edges combined across two WPs) and from the 18 exact baseline replacements reported in the Phase-03R completion review's aggregate reconciliation across all 38 work packages. This assessment cites only the 11-edge count that applies to `WP-ARCH-003` itself. The companion worker return corrects its test-file count from a miscounted 9 to the actual enumerated 8 named test files. No `PENDING_BEFORE_READY` or other nonterminal readiness token remains in either output. |

## Required Criterion Matrix

| Criterion | Disposition | Evidence |
|---|---|---|
| Delegation preserves or narrows authority unless explicit higher-authority approval expands it | PARTIAL | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/delegation.boundary.guard.contract.ts` `evaluateDelegatedWriteBoundary` fails closed on forbidden/unowned paths and allows only `ownedFiles`/`ownedModules` (positive test: `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/delegation.boundary.guard.contract.test.ts`). No authority-expansion approval primitive exists in this file or in `capability-owner-binding.contract.ts`; expansion is only implicitly prevented by absence, not by an explicit approval-gated widening path with a negative test proving a request to expand authority is rejected without approval evidence. This gap is independent of the R1-01/R1-02 owner-identity correction above. |
| Every governed execution resource receives the same principal/scope identity and cross-scope access fails closed | MISSING | The canonical owner's `ScopeGuard` (`EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/scope.guard.ts`) checks only a static `PROTECTED_PATHS` string list and a per-call `context.role`; it carries no principal identity, no workspace/tenant identifier, and no comparison between a resource's owning scope and the caller's scope. `role.resolver.contract.ts` `resolveRole` verifies authority-hash integrity and role/route admission, but never compares a caller identity against a resource's bound scope either. No cross-scope or cross-tenant negative test exists anywhere in the named owner packages (see Negative Search below). This gap exists in the canonical owner itself and is unrelated to the retracted duplicate-owner finding. |
| A capability grant becomes invalid when its bound version/trust state changes unless explicitly re-approved | SATISFIED | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/repository-capability-owner.source.ts` `loadCommittedRepositoryCapabilityGrant`/`registerGrant` fail closed with `GRANT_ID_REBOUND` if a grant ID is rebound to different committed bytes, and `capability-owner-binding.contract.ts` `reconcileGrantWithObservation` fails closed on `EVALUATION_EXPIRED`/`EVALUATION_NOT_YET_VALID`/`GRANT_MISMATCH`. Positive and negative coverage exists in `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/repository-capability-owner.source.test.ts` and `capability-owner-binding.contract.test.ts` (duplicate/ordered retry enforcement, hostile observation rejection). |

A symbol name without consumer/test evidence cannot receive `SATISFIED`; the
first two rows are held at `PARTIAL`/`MISSING` on that basis even though the
canonical owner files exist, compile, and are correctly identified as sole
owner per the R1-01 correction above.

## Required Owner And Overlap Matrix

| Concern | Canonical owner (selected by Phase-03R; not reopened by this audit) | Current implementation | Compatibility/legacy surfaces | Disposition |
|---|---|---|---|---|
| Principal identity / phase-role-risk authority | `AuthorityGateGuard` at `EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/authority-gate.guard.ts` | Full `AUTHORITY_MATRIX` (10 roles x 5 phases), tested by `authority-gate.operator.test.ts` and `index.test.ts`; imported live at every production composition root proven by `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/integration/canonical-guard-contract-adoption.test.ts` (28/28 PASS, reproduced in this rework) | `EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/governance/guard_runtime/guards/authority.gate.guard.ts` (5-role/5-phase matrix, earlier governance-protocol generation) and `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/guards/authority-gate.guard.ts` (a bare `RESTRICTED_ACTIONS` denylist keyed by only 4 roles, re-exported from `src/sdk.ts` as a named backward-compatible SDK symbol alongside the canonical engine, but not consumed by any production composition root per the regression test above) | CONFIRMED_EXISTING; canonical owner is settled; compatibility copies are a documentation/migration note, not an open owner dispute |
| Protected-scope / workspace isolation | `ScopeGuard` at `EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/scope.guard.ts` | Static `PROTECTED_PATHS` + builder-class role check, tested by two cases in `index.test.ts`; consumed live via the same canonical-engine import path as `AuthorityGateGuard` | Same compatibility surfaces as above (`CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL` and the MCP package's re-exported, non-production-wired local copy) | CONFIRMED_EXISTING; canonical owner is settled |
| Delegation inheritance/override | `MaoAuthorityEnvelope`, `MaoTaskDefinition.fileScope`, `MaoAtomicDelegationLifecycleCoordinator` at `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts` | `computeAuthorityHash`/`verifyAuthorityEnvelope`/`buildAuthorityEnvelope`; consumed by `resolveRole` in Control Plane | none found | CONFIRMED_EXISTING, single owner; authority-hash tamper detection exists, but no primitive proves "delegation narrows, never expands, unless an explicit higher-authority approval record exists" as a distinct evaluable state - trace only, feeds criterion 1's PARTIAL |
| File scope / delegated-write boundary | `ExecutionDelegationBoundary`, `evaluateDelegatedWriteBoundary` at `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/delegation.boundary.guard.contract.ts` | Deny-by-default allow-list evaluator; tested | `FileScopeGuard` (`EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/file-scope.guard.ts`) is a separate, already-existing file-scope enforcement surface not named by the Phase-03R correction at all | ENRICH_EXISTING; `FileScopeGuard` and `ExecutionDelegationBoundary` are two independently maintained file-scope deny/allow evaluators with no documented reconciliation; a note for future compatibility bookkeeping, not a WP-ARCH-003 blocker |
| Version-bound grant lifecycle | `bindCommittedCapabilityOwnerGrant`, `VerifiedRepositoryGrant`, `evaluateCapabilityReadiness` | Fully implemented, git-object-backed, SQLite-anti-rebind-protected | none found | CONFIRMED_EXISTING, single owner; no gap |
| Cross-domain propagation (MAO authority envelope -> Control Plane role resolver) | `MaoAuthorityEnvelope` -> `resolveRole` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/mao/role.resolver.contract.ts` | `resolveRole` calls `verifyAuthorityEnvelope` and fails closed with `REJECTED_AUTHORITY_HASH_INVALID` | none found | CONFIRMED_EXISTING, single owner within MAO; proves authority-hash integrity, not principal/scope identity consistency - does not satisfy criterion 2 |

## Required Threat And Failure Matrix

| Threat | Current mitigation | Remaining gap | Negative fixture | Closure evidence |
|---|---|---|---|---|
| Escalation (role gains disallowed action/risk) | `AuthorityGateGuard` (canonical, live at every production composition root) blocks disallowed action/risk per role+phase cell | None found against the canonical live path itself; the two compatibility-only copies (frozen-adjacent layer and MCP package-local re-export) are not wired into production composition and therefore do not create a live escalation path per the reproduced regression evidence | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/integration/canonical-guard-contract-adoption.test.ts` (28/28 PASS) | CLOSED for the live path; compatibility-copy consolidation remains a documentation note only |
| Confused deputy (one component acts using another's authority) | `MaoAuthorityEnvelope.closerActorId` plus `resolveRole`'s designated-closer checks | No principal-identity check ties a `GuardRequestContext.role` call to a specific accountable actor id; `AuthorityGateGuard`/`ScopeGuard` accept `role` as a bare caller-supplied string with no binding to a verified identity | No test constructs a forged-role request and asserts rejection | Not closed; feeds criterion 2's MISSING disposition |
| Scope spoofing (caller claims a scope it does not own) | None found | `ScopeGuard` and `FileScopeGuard` both trust `context.fileScope`/`context.targetFiles` as caller-supplied; neither cross-checks against an independently verified owner/scope record such as `MaoTaskDefinition.fileScope` | No test asserts that a caller-declared `fileScope` mismatching its `MaoTaskDefinition.fileScope` is rejected | Not closed; feeds criterion 2's MISSING disposition |
| Cross-tenant access | None found | No component in the four named packages carries a tenant/workspace identity field; `CapabilityCandidateSet.workspaceId` in `capability-route-readiness.contract.ts` is validated for shape only, never compared across two callers | No cross-tenant negative test exists in any of the 8 test files inventoried in the companion worker return | Not closed; feeds criterion 2's MISSING disposition |
| Stale grant | `repository-capability-owner.source.ts` `GRANT_ID_REBOUND`, `EVALUATION_EXPIRED` | None; well covered | `repository-capability-owner.source.test.ts`, `capability-owner-binding.contract.test.ts` | CLOSED |
| Version/trust mutation | Same as above; `ARTIFACT_HASH_MISMATCH` on any drifted artifact | None found for this specific criterion | Same test files | CLOSED |
| Replay/rebind | `consumeRepositoryGrantInvocation` retry-ordinal contiguity plus `DUPLICATE_INVOCATION_REJECTED` | None found | `repository-capability-owner.source.test.ts` ("persists duplicate and ordered retry enforcement across independent binds") | CLOSED |
| Partial migration | The canonical engine is confirmed live at every production composition root; the compatibility copies are not migration-blocking | Documentation/registry consolidation for the two non-production-wired compatibility copies remains a future bookkeeping item, not a runtime threat | `canonical-guard-contract-adoption.test.ts` static import-guard assertions | CLOSED for runtime purposes; DEFERRED as a documentation-only cleanup item |
| Legacy consumer bypass | `canonical-guard-contract-adoption.test.ts` statically asserts all seven named production composition files import the engine/factory from `cvf-guard-contract`, not the local fork | None found; the MCP package's re-exported local guard classes and `createUnifiedRegistry` factory have zero non-test in-repository callers | Static import-guard assertions plus dynamic mandatory-core admission proof (both reproduced 28/28 PASS in this rework) | CLOSED |
| Rollback failure | Not yet applicable; the two acceptance-criteria gaps below have not begun implementation | Rollback rehearsal is appropriately deferred to the implementation work order named in the Exact Future Manifest, once source/test changes for criteria 1 and 2 exist | None yet; correctly deferred, not blocked | DEFERRED_TO_SUCCESSOR |

## Required Compatibility And Migration Matrix

| Consumer surface | Classification | Evidence |
|---|---|---|
| Guard Contract (`EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts`) | NO_CHANGE | Canonical owner already in place; exported and tested via `src/index.test.ts` |
| Execution Plane (`EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/`) | NO_CHANGE | `delegation.boundary.guard.contract.ts` and `mao/task.graph.contract.ts` are independent owners already consumed by their own tests |
| Control Plane (`EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/`) | NO_CHANGE | `role.resolver.contract.ts` consumes `MaoAuthorityEnvelope` only |
| MCP (`EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/`) | COMPATIBILITY_TEST_ONLY | `src/index.ts`, `src/sdk.ts`, and every other production composition file listed in `canonical-guard-contract-adoption.test.ts` import the guard engine/factory from `cvf-guard-contract`. The package-local `AuthorityGateGuard`/`ScopeGuard` classes and `createUnifiedRegistry` remain exported for backward-compatible SDK consumers with zero non-test in-repository production callers found; existing regression coverage (28/28 PASS) already guards this boundary, so no migration action is required by this WP |
| Memory | OUT_OF_SCOPE_WITH_REASON | No named memory-domain consumer of `AuthorityGateGuard`/`ScopeGuard` was found in this bounded audit; the WP's cross-domain interface list names `MEMORY scope` but no current source symbol was located to verify or refute in the time-boxed named-file scope of this audit |
| Skill | OUT_OF_SCOPE_WITH_REASON | Same as Memory; the WP names `SKILL permissions` as a cross-domain interface but no current Skill-domain consumer symbol was located in the named owner packages read for this audit |
| CLI/SDK | COMPATIBILITY_TEST_ONLY | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/sdk.ts` re-exports the canonical engine/factory and, separately, the package-local compatibility classes; both are covered by the same regression test as the MCP row above |
| Web (`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/`) | NO_CHANGE | `src/lib/guard-runtime-adapter.ts` imports from the canonical `CVF_GUARD_CONTRACT` package |
| Workspace/bootstrap (`scripts/new-cvf-workspace.ps1`) | OUT_OF_SCOPE_WITH_REASON | Named as a repository anchor in the WP contract but not a runtime consumer of the guard classes; out of scope for a source/test reconciliation audit |
| Frozen-adjacent layer (`EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/`) | OUT_OF_SCOPE_WITH_REASON | `AGENTS.md` marks `v1.0/` and `v1.1/` frozen and maintenance-only; `CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL` sits alongside those frozen layers as an earlier governance-protocol generation with its own independent authority/scope classes. This audit records the classes as a documentation/compatibility note; no consolidation action is required for `WP-ARCH-003` because the frozen-adjacent layer is not a live consumer of the canonical Guard Contract path |

Version strategy: the canonical owner is settled (`EXTENSIONS/CVF_GUARD_CONTRACT/`);
no migration is required for the guard-identity question. The remaining
version/migration/rollback work applies only to the two `PARTIAL`/`MISSING`
acceptance criteria and is scoped in the Exact Future Manifest below.

## Negative Search And Collision Discipline

| Check | Search root or command | Result | Disposition |
|---|---|---|---|
| assessment collision | exact `Test-Path -LiteralPath docs/assessments/CVF_PHASE04_WAVE0_WP_ARCH_003_OWNER_GAP_AUDIT_2026-09-06.md` | present (this rework edits it in place) | EXPECTED_IN_PLACE_EDIT |
| worker-return collision | exact `Test-Path -LiteralPath docs/reviews/CVF_PHASE04_WAVE0_WP_ARCH_003_OWNER_GAP_AUDIT_WORKER_RETURN_2026-09-06.md` | present (this rework edits it in place) | EXPECTED_IN_PLACE_EDIT |
| stale terminal-decision token | `Grep pattern:"BLOCKED_OWNER_CONFLICT"` over both output files after correction | zero remaining occurrences outside the Rework Round 1 finding-disposition narrative explaining the retraction | REPAIRED |
| false live-wiring language | `Grep pattern:"live runtime guard chain"` and similar phrasing over both output files after correction | zero remaining occurrences asserting the MCP package-local classes are production-wired | REPAIRED |
| parallel `AuthorityGateGuard`/`ScopeGuard` copies | `Grep pattern:"AuthorityGateGuard"` / `"\bScopeGuard\b"` path:EXTENSIONS glob:*.ts (reproduced from the initial audit) | three same-named class declarations still exist across `CVF_GUARD_CONTRACT` (canonical), `CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL` (compatibility/legacy), and `CVF_ECO_v2.5_MCP_SERVER` (re-exported compatibility surface, not production-wired) | ACCEPT_AS_COMPATIBILITY_SURFACES_NOT_OWNER_CONFLICT |
| live production import proof | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/integration/canonical-guard-contract-adoption.test.ts` executed via `npm test -- --run src/integration/canonical-guard-contract-adoption.test.ts` from `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER` | 28/28 tests passed | CONFIRMED_LIVE_CANONICAL_IMPORT |
| `createUnifiedRegistry` non-test caller search | `Grep pattern:"createUnifiedRegistry"` path:`EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER` glob:*.ts | matches only in `src/registry/guard-registry.ts` (definition), `src/sdk.ts` (re-export only, not invoked), `src/registry/guard-registry.test.ts`, and `src/integration/e2e-pipeline.test.ts` | CONFIRMED_ZERO_NON_TEST_CALLERS |
| single-owner confirmation for grant/readiness/delegation primitives | direct reads of `capability-owner-binding.contract.ts`, `repository-capability-owner.source.ts`, `capability-route-readiness.contract.ts`, `delegation.boundary.guard.contract.ts`, `task.graph.contract.ts`, `role.resolver.contract.ts` | exactly one implementation of each cited symbol was found; no duplicate | ACCEPT_NO_COLLISION |
| cross-tenant / cross-scope negative test presence | targeted read of `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.test.ts` `ScopeGuard` block (2 cases), `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/mao.role.resolver.contract.test.ts` (19 cases, all authority-hash/route/budget/role focused), `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/delegation.boundary.guard.contract.test.ts` | zero tests assert cross-scope or cross-tenant identity-mismatch rejection anywhere in the named owner packages | GAP_CONFIRMED_NOT_COLLISION |
| provider or live requirement | none invoked during this audit or its rework | zero provider/network calls made | FORBIDDEN_RESPECTED |

## Exact Future Manifest

Because the terminal decision is `BOUNDED_DELTA_REQUIRED`, this audit freezes
the following exact successor scope for a separately authorized implementation
work order. Every cell below names either a real existing repository path
(verified present by direct `Test-Path`/`Read` in this rework) or an exact
new repository-relative path this audit selects and freezes now; no cell
defers naming to a future design step. No path below is created, edited, or
mutated by this audit itself.

### Criterion 1 - Authority-expansion approval (`ARCH-ABS-007`)

| Field | Exact value |
|---|---|
| Existing source to extend | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/delegation.boundary.guard.contract.ts` (add an `evaluateAuthorityExpansionApproval` export alongside the existing `evaluateDelegatedWriteBoundary`); `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-owner-binding.contract.ts` (extend `CapabilityOwnerBindingIssueCode` with an `AUTHORITY_EXPANSION_UNAPPROVED` member) |
| New source (exact path to create) | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/authority-expansion-approval.contract.ts` (new file; exports an `AuthorityExpansionApprovalRecord` type and an `evaluateAuthorityExpansionApproval` fail-closed evaluator, following the existing `bindCommittedCapabilityOwnerGrant` git-object-verification pattern in `repository-capability-owner.source.ts`) |
| New tests (exact path to create) | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/authority-expansion-approval.contract.test.ts` (new file; positive case: an expansion request with a verified approval record is allowed; negative cases: an expansion request with no approval record, an expired approval record, and an approval record bound to a different grant hash are each rejected) |
| Extended tests (exact path to edit) | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/delegation.boundary.guard.contract.test.ts` (add one negative case: a write request outside `ownedFiles`/`ownedModules` that also carries no `AuthorityExpansionApprovalRecord` is rejected by the existing deny-by-default path, proving the new evaluator does not weaken current behavior) |
| Documentation (exact path to create) | `docs/reference/CVF_WP_ARCH_003_PRINCIPAL_SCOPE_DELEGATION_GRANT_CONTRACT_MIGRATION_NOTE.md` (new file; states the new evaluator's version, the exact approval-record schema, and the claim boundary that existing callers without an expansion request are unaffected) |
| Migration input/output | Input: none (no existing data store holds authority-expansion state today). Output: none (`NONE_WITH_REASON` - the new evaluator is additive and stateless like `evaluateDelegatedWriteBoundary`; it introduces no new persisted schema requiring a data migration) |
| Rollback target/command boundary | Revert exactly `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/authority-expansion-approval.contract.ts`, its test file, the `AUTHORITY_EXPANSION_UNAPPROVED` addition to `capability-owner-binding.contract.ts`, and the new negative case in `delegation.boundary.guard.contract.test.ts`; the existing `evaluateDelegatedWriteBoundary` deny-by-default path requires no rollback because it is not modified |
| Evidence output path | `docs/reviews/CVF_WP_ARCH_003_IMPLEMENTATION_CRITERION_1_RECEIPT_<date>.md` (new file; the successor work order's worker-return path, to be dated at that dispatch) |

### Criterion 2 - Principal/scope identity propagation (`ARCH-ABS-017`)

| Field | Exact value |
|---|---|
| Existing source to extend | `EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/scope.guard.ts` (add a principal-identity comparison branch to `ScopeGuard.evaluate` alongside the existing `PROTECTED_PATHS` check); `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/mao/role.resolver.contract.ts` (extend `resolveRole` to surface the caller's verified scope identity to the new guard) |
| New source (exact path to create) | `EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/principal-scope-identity.guard.ts` (new file; exports a `PrincipalScopeIdentityGuard` class implementing the existing `Guard` interface from `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts`, comparing a resource's declared owning scope against the caller's verified `MaoTaskDefinition.fileScope` from `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts`) |
| New tests (exact path to create) | `EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/principal-scope-identity.guard.test.ts` (new file; positive case: matching principal/scope identity is allowed; negative cases: cross-scope access is denied, cross-tenant access is denied, and a caller-declared `fileScope` that mismatches its `MaoTaskDefinition.fileScope` is rejected) |
| Extended tests (exact path to edit) | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/mao.role.resolver.contract.test.ts` (add one case proving `resolveRole` surfaces the verified scope identity unchanged, so `PrincipalScopeIdentityGuard` receives an unforgeable value, not a bare caller-supplied string) |
| Documentation (exact path to create) | Reuse `docs/reference/CVF_WP_ARCH_003_PRINCIPAL_SCOPE_DELEGATION_GRANT_CONTRACT_MIGRATION_NOTE.md` (same new file as criterion 1; add a distinct section documenting the new guard's version and principal/scope propagation contract) |
| Migration input/output | Input: `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts`'s existing `MaoTaskDefinition.fileScope` field (already present, read-only for this delta). Output: none (`NONE_WITH_REASON` - the new guard reads existing task-graph state; it persists no new data) |
| Rollback target/command boundary | Revert exactly `EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/principal-scope-identity.guard.ts`, its test file, and the `resolveRole` extension in `role.resolver.contract.ts`; the existing `ScopeGuard.evaluate` static-path check requires no rollback because it is not removed, only supplemented |
| Evidence output path | `docs/reviews/CVF_WP_ARCH_003_IMPLEMENTATION_CRITERION_2_RECEIPT_<date>.md` (new file; the successor work order's worker-return path, to be dated at that dispatch) |

### Criterion 3 - Version-bound grant invalidation (`ARCH-ABS-021`)

| Field | Exact value |
|---|---|
| Disposition | NONE_WITH_REASON - already `SATISFIED`. `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/repository-capability-owner.source.ts` and `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-owner-binding.contract.ts` already implement and test this criterion in full; no new source, test, documentation, migration, rollback, or evidence path is required |

## Required Terminal Decision

`BOUNDED_DELTA_REQUIRED`.

At least one criterion (in fact two: cross-scope/cross-tenant identity
propagation and authority-expansion-approval evidence) is partial or missing
without an owner conflict. The exact successor scope is frozen in the Exact
Future Manifest above for one later, separately authorized implementation
work order. No hybrid or fourth decision is selected.

## Risk / Corrective Action

Primary risk of the original R1 defect: the initial audit conflated a
same-named backward-compatible export with a live production wiring path,
which would have caused the operator/reviewer to spend effort re-litigating
an owner decision Phase-03R had already made, and would have delayed the
correct `BOUNDED_DELTA_REQUIRED` successor scoping by at least one extra
review round. Corrective action taken in this rework: every claim about
"live" wiring is now backed by either a direct source-line citation
(`src/index.ts` line 38, `src/sdk.ts` lines 17-36) or a reproduced automated
test result (28/28 PASS), not by reading only the package-local
`src/guards/index.ts` and `src/registry/guard-registry.ts` files in isolation
as the initial audit did.

Residual risk: the two acceptance criteria marked `PARTIAL`/`MISSING` still
require the bounded implementation delta frozen in the Exact Future Manifest;
this audit does not claim they are satisfied merely because the owner
conflict was retracted.

## Evidence / Verification

- `git rev-parse HEAD` confirmed `executionBaseHead`
  `dcdd34094bce61fe68deb620abb70563edaab0fd` matches the amendment's expected
  HEAD before this rework began.
- `git status --short` confirmed only the two existing untracked worker
  outputs were pending, with no unrelated change.
- Direct `Read` of `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` and
  `src/sdk.ts` in full, confirming the canonical `cvf-guard-contract` import
  and re-export.
- `npm test -- --run src/integration/canonical-guard-contract-adoption.test.ts`
  executed from `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER`: 28/28 PASS (real
  execution evidence, recorded in the companion worker return's Command
  Evidence section).
- Targeted `Grep` for `createUnifiedRegistry` across
  `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER` confirmed zero non-test
  in-repository callers.
- Zero provider, network, or credential calls were made during this rework.
- No source, test, runtime, governance, session, amendment, parent work
  order, or public artifact was modified while gathering this evidence; only
  the two exact worker outputs named in the amendment's Exact Worker Manifest
  were edited.

## Claim Boundary

This assessment performs a bounded, named-file, current-source-only audit for
`WP-ARCH-003`, corrected per Rework Round 1 review findings R1-01 through
R1-04. It does not implement, edit, or propose editing any source, test,
runtime, governance, session, or public-sync artifact; does not authorize a
successor tranche; and does not claim `WP-ARCH-003` is implemented, verified,
or ready for freeze. The Exact Future Manifest above requires a separate
operator-authorized governed work order before any implementation begins.
Independent reviewer/closer acceptance of this correction remains required.
