# CVF P1-P5 Small Debt Remediation Audit

Memory class: POINTER_RECORD

Status: BOUNDED_REMEDIATION_COMPLETE

## Purpose

Close the small, source-confirmed P1-P5 review gaps now and route larger
runtime/infra/methodology fixes into source-verified backlog packets.

## Operator Request

Handle P1-P5 after audit, use live keys when needed, and push for external
agent review.

## Source

Current repository source, npm metadata refreshed on 2026-06-06, and archived
QBS review packets cited in the verification table.

## Protocol

Each item is classified as immediate remediation, source-verified backlog, or
blocked implementation. Runtime production claims require direct source and
test evidence, not review prose alone.

## Enforcement

Required gates for this batch include markdown structural completeness,
work-order dispatch quality, finding-to-governance learning, `git diff
--check`, autorun workflow gates, and live proof only when a governance
behavior claim is made.

## Source Verification

| Item | Source file | Verified line/section | Verified path or symbol | Owning surface | Disposition |
| --- | --- | --- | --- | --- | --- |
| `next-auth` declared as v5 beta | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | line 30 | `next-auth` | cvf-web package manifest | ACCEPT |
| `next-auth` lock root keeps beta range | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package-lock.json` | line 21 | `next-auth` | cvf-web lockfile | ACCEPT |
| Runtime uses Auth.js v5-style handler export | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.ts` | line 113 | `NextAuth(nextAuthConfig)` | auth runtime | ACCEPT |
| App route delegates to Auth.js handlers | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/auth/[...nextauth]/route.ts` | line 3 | `handlers` | auth route | ACCEPT |
| Web CI already runs audit, lint, unit tests, and coverage | `.github/workflows/cvf-web-ci.yml` | lines 38-46 | `npm audit`, `npm run lint`, `npm run test:coverage` | GitHub Actions | ACCEPT |
| Protected live release gate exists | `.github/workflows/cvf-protected-live-release-gate.yml` | lines 1-17 | `CVF Protected Live Release Gate` | GitHub Actions | ACCEPT |
| Targeted live gate flag exists | `scripts/run_cvf_release_gate_bundle.py` | lines 15, 22, 347 | `--e2e-live` | release gate script | ACCEPT |
| CSV audit signing hook exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | lines 92, 264-271 | `computeAuditCsvSignature` | web audit export | ACCEPT |
| Rate limiter is process-local memory | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | lines 6, 11-12 | `buckets`, `CVF_RATE_LIMIT`, `CVF_PROVIDER_QUOTA_PER_MIN` | runtime rate limiter | ACCEPT |
| QBS 48-task corpus is aggregate-only | `docs/reviews/archive/CVF_QBS_PUBLIC_METHODOLOGY_INDEPENDENT_REVIEW_2026-05-09.md` | lines 88-95 | `48-task corpus` | benchmark methodology review | ACCEPT |
| Ordinal reviewer reliability should use weighted/ordinal statistic at 0.60 | `docs/reviews/archive/CVF_QBS_PUBLIC_METHODOLOGY_INDEPENDENT_REVIEW_2026-05-09.md` | lines 237-243 | `quadratic-weighted Cohen's kappa` | benchmark methodology review | ACCEPT |
| Later QBS proposal lowered aggregate gate to 0.55 and withdrew per-family gate | `docs/reviews/archive/CVF_QBS_RERUN_REMEDIATION_PROPOSAL_2026-05-11.md` | lines 584-587, 695-704 | `aggregate kappa`, `per-family kappa` | benchmark remediation proposal | ACCEPT_WITH_CONFLICT |

## P1-P5 Disposition

| Priority | External finding | Current disposition | Batch action |
| --- | --- | --- | --- |
| P1 | `next-auth` beta in production | Real technical debt. Stable v5 is not available from npm on 2026-06-06; latest stable is v4.24.14 and beta is v5.0.0-beta.31. Forced downgrade would be an auth-runtime migration, not a small fix. | Created source-verified DEP2 backlog work order with migration triggers. |
| P2 | Harden CI and add live scheduled job | Partly already covered by web CI and protected manual release gate. Missing low-budget scheduled live smoke. | Added `.github/workflows/cvf-scheduled-live-governance-smoke.yml`. |
| P3 | Signed receipts, immutable anchor, third-party rerun | HMAC CSV signing exists, but no generic manifest/rerun packet for live evidence. External immutability remains a separate anchor requirement. | Added manifest script and standard. |
| P4 | Reduce operational debt with distributed rate limiter and enterprise backend | Process-local limiter is source-confirmed. Real Redis/PostgreSQL/SSO requires infra/package choice and cannot be honestly completed as a small fix. | Created source-verified distributed rate limiter backlog work order. |
| P5 | Reviewer agreement and benchmark corpus reliability | Structural benchmark-method issue remains. 48 tasks support aggregate claims only; family-level claims need expanded corpus. | Created source-verified benchmark reliability backlog work order. |

## Changed Artifacts

- `.github/workflows/cvf-scheduled-live-governance-smoke.yml`
- `scripts/build_cvf_live_evidence_manifest.py`
- `docs/reference/CVF_LIVE_EVIDENCE_MANIFEST_AND_RERUN_STANDARD_2026-06-06.md`
- `docs/work_orders/CVF_WO_DEP2_NEXT_AUTH_STABLE_MIGRATION_DECISION_2026-06-06.md`
- `docs/work_orders/CVF_WO_ERH_RL1_DISTRIBUTED_RATE_LIMITER_BOUNDARY_2026-06-06.md`
- `docs/work_orders/CVF_WO_QBS_METHOD_RELIABILITY_REMEDIATION_2026-06-06.md`

## Verification

| Command | Result | Notes |
| --- | --- | --- |
| `npm view next-auth version dist-tags --json` | PASS | 2026-06-06 metadata: `latest=4.24.14`, `beta=5.0.0-beta.31`; stable v5 unavailable. |
| `python scripts/build_cvf_live_evidence_manifest.py --evidence docs/reference/CVF_LIVE_EVIDENCE_MANIFEST_AND_RERUN_STANDARD_2026-06-06.md --command "python scripts/run_cvf_release_gate_bundle.py --e2e-live --json" --output %TEMP%/cvf-live-evidence-manifest-test.json` | PASS | Manifest script produced secret-safe JSON with sha256 and unsigned status when no signing key is set. |
| `python governance/compat/check_markdown_structural_completeness.py --base 2b39dc47 --head HEAD --enforce` | PASS | New governed Markdown files satisfy GC-045 structure. |
| `python governance/compat/check_work_order_dispatch_quality.py --base 2b39dc47 --head HEAD --enforce` | PASS | Backlog work-order packets pass source/dispatch hygiene. |
| `python governance/compat/check_finding_to_governance_learning.py --base 2b39dc47 --head HEAD --enforce` | PASS | Findings include reusable learning dispositions. |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 2b39dc47 --head HEAD` | PASS | Autorun pre-implementation gate passed. |
| `python scripts/run_cvf_release_gate_bundle.py --e2e-live --json` | PASS | Live run passed: web build, guard-contract typecheck, provider readiness with 3 certified lanes, secrets scan, RC docs, and Playwright live governance suite. |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Batch status |
| --- | --- | --- | --- | --- | --- |
| Beta auth dependency can be repeatedly reported without a stable migration target | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | Keep DEP2 behind source-verified package metadata and Auth.js API review. | HANDLED |
| Live governance proof existed only as protected manual release gate | PHASE_GATE_PLACEMENT_GAP | GOVERNANCE_CONTROL_PLANE | STANDARD_UPDATED | Add scheduled low-budget live smoke plus manifest standard. | HANDLED |
| Signed CSV export did not give generic third-party rerun packet | RUNTIME_SIGNAL_GAP | GOVERNANCE_CONTROL_PLANE | STANDARD_ADDED | Use live evidence manifest for future live proof artifacts. | HANDLED |
| Process-local rate limiting is not multi-instance safe | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | DESIGN_REVIEW_REQUIRED | Implement Redis-backed limiter only after infra/package decision. | DEFERRED |
| Reviewer agreement/corpus concerns recur across QBS reviews | RULE_GAP | PROVIDER_OUTPUT_LEARNING | DESIGN_REVIEW_REQUIRED | Reopen QBS method reliability with kappa 0.60 and aggregate-only public claim gate. | DEFERRED |

## Claim Boundary

This batch closes small, source-confirmed debt and creates implementation-ready
follow-up packets where small local edits would create false production claims.
It does not claim stable Auth.js production migration, Redis deployment,
PostgreSQL/SSO readiness, independent third-party certification, benchmark
quality parity, or family-level benchmark power.

## Related Artifacts

- `docs/reference/CVF_LIVE_EVIDENCE_MANIFEST_AND_RERUN_STANDARD_2026-06-06.md`
- `docs/work_orders/CVF_WO_DEP2_NEXT_AUTH_STABLE_MIGRATION_DECISION_2026-06-06.md`
- `docs/work_orders/CVF_WO_ERH_RL1_DISTRIBUTED_RATE_LIMITER_BOUNDARY_2026-06-06.md`
- `docs/work_orders/CVF_WO_QBS_METHOD_RELIABILITY_REMEDIATION_2026-06-06.md`
