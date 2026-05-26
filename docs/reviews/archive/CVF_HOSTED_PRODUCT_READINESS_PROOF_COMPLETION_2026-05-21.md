# CVF Hosted Product Readiness Proof Completion

Memory class: FULL_RECORD

Status: CLOSED_LOCAL_PRODUCTION_PROOF

docType: review

Date: 2026-05-21

---

## Purpose

Close the bounded hosted/product-readiness proof workflow at the honest
evidence boundary reached on 2026-05-21.

---

## Authority Chain

- Roadmap:
  `docs/roadmaps/CVF_HOSTED_PRODUCT_READINESS_PROOF_ROADMAP_2026-05-21.md`
- GC-018:
  `docs/baselines/CVF_GC018_HOSTED_PRODUCT_READINESS_PROOF_2026-05-21.md`
- Work order:
  `docs/work_orders/CVF_WO_HOSTED_PRODUCT_READINESS_PROOF_2026-05-21.md`
- Deploy guide:
  `docs/guides/CVF_DEPLOY_GUIDE.md`
- Active session state:
  `CVF_SESSION/ACTIVE_SESSION_STATE.json`

---

## Scope / Target / Owner Boundary

Target:

- HPR-01 local production build proof.
- HPR-02 local production server live `/api/execute` governance proof.
- HPR-03 service-token and live-key diagnostic boundary.
- HPR-04 mandatory release gate.

Owner boundary:

- Evidence-only product-readiness proof.
- No source-code changes, public deployment, public-sync update, provider
  runtime change, persistence/database work, Maika proof, kernel-owner change,
  or freeze release.

---

## Target / Source Under Review

Local production-mode target:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`
- build command: `npm run build`
- start command: `npm run start -- --hostname 127.0.0.1 -p 3235`
- live route: `http://127.0.0.1:3235/api/execute`

---

## Methodology

Codex executed the bounded roles:

1. Orchestrator opened the roadmap, GC-018, and work order.
2. Reviewer constrained the scope to local production-mode proof only.
3. Implementer ran production build/start and signed service-token proof.
4. Auditor ran the mandatory release gate and classified the result without
   tuning the runner or expanding source ownership.

---

## Evidence Trace Block

| Claim | Evidence | Result |
| --- | --- | --- |
| HPR-01 production build | `npm run build` in `cvf-web` | PASS; build completed in about 468s |
| HPR-02 production server | `npm run start -- --hostname 127.0.0.1 -p 3235` | PASS; Next.js ready on `127.0.0.1:3235` |
| HPR-02 live governed route | signed service-token POST to `/api/execute` | PASS; HTTP 200, `success=true`, ALLOW |
| HPR-03 fail-closed diagnostics | first probe with risky wording and second incomplete-template probe | PASS diagnostic; BLOCK receipt and CLARIFY receipt were live, not mock |
| HPR-04 release gate | `python scripts/run_cvf_release_gate_bundle.py --json` | FAIL; build subcheck timed out at 300s, remaining 6/7 checks PASS |
| Server cleanup | stopped npm and child Next.js processes | PASS; port `3235` returned to 0 listeners |
| Secret handling | redacted env loading and result-only proof output | PASS; raw secrets not printed |

---

## Live Production-Mode Proof Result

Proof schema: `hosted-product-readiness-proof-result-1`

Final successful journey:

- server mode: `next-start-production-local`;
- base URL: `http://127.0.0.1:3235`;
- HTTP status: `200`;
- success: `true`;
- decision: `ALLOW`;
- routing decision: `ALLOW`;
- evidence mode: `live`;
- provider: `alibaba`;
- model: `qwen-turbo`;
- receipt id: `rcpt-env-mpflcxex-1zkxan`;
- trace id: `env-mpflcxex-1zkxan`;
- route id: `/api/execute`;
- output length: `4507`;
- latency: `18225ms`;
- raw secret printed: `false`.

Diagnostic non-pass probes:

- HTTP `400`, decision `BLOCK`, receipt `rcpt-env-mpflbhac-76hkxh`, trace
  `env-mpflbhac-76hkxh`; this confirmed fail-closed live governance behavior
  for risk wording.
- HTTP `422`, decision `CLARIFY`, receipt `rcpt-env-mpflc7k2-fg382i`, trace
  `env-mpflc7k2-fg382i`; this confirmed live clarification behavior for an
  incomplete template payload.

---

## Release Gate Result

Mandatory command:

```powershell
python scripts/run_cvf_release_gate_bundle.py --json
```

Result: `FAIL`.

Failure class: `release_gate_build_timeout`.

Details:

- `Web build (npm run build)`: FAIL, `Command timed out`.
- `TypeScript check (guard contract)`: PASS.
- `Provider readiness`: PASS, `CERTIFIED lanes: 3`.
- `Secrets scan`: PASS.
- `Docs governance`: PASS.
- `E2E Playwright UI (mock)`: PASS, `6 passed`.
- `E2E Playwright Governance (live)`: PASS.

Interpretation:

The product-like local production path passed, but this tranche cannot close a
release-quality hosted/product readiness claim because the mandatory release
gate returned non-zero. The build itself passed when run directly; the gate
runner's current 300s build timeout is below the observed build duration.

---

## Post-Maintenance Addendum

The release-gate timeout blocker was retired by:

`docs/reviews/CVF_RELEASE_GATE_BUILD_TIMEOUT_MAINTENANCE_COMPLETION_2026-05-21.md`

That maintenance changed only the release-gate web build timeout from 300s to
900s and reran:

```powershell
python scripts/run_cvf_release_gate_bundle.py --json
```

Result: PASS `7/7`.

Updated disposition: `CLOSED_LOCAL_PRODUCTION_PROOF`.

The claim boundary remains unchanged: this is still local production-mode
proof only, not external hosted SaaS readiness.

---

## Findings / Position

Position: CLOSED_LOCAL_PRODUCTION_PROOF after timeout maintenance.

The useful product evidence is real but bounded:

- local production-mode build works;
- local production-mode server can return a live governed receipt;
- service-token signing and live provider execution work on that path.

The originally blocking release-gate timeout has now been retired by the
separate maintenance tranche. The local production-mode proof is closed.

---

## Risk / Corrective Action

Residual risk:

- The proof is local production-mode only, not an external hosted deployment.
- A public or hosted-readiness claim would overstate the evidence.

Corrective action:

- Keep the result as a useful local production-mode proof only.
- Open a separate external deployment proof only if the operator asks for it.

---

## Decision / Recommendation / Disposition

Disposition: close local production-mode proof, do not claim external
hosted/product readiness.

Recommended next move:

- Stop here unless an external hosted deployment proof is explicitly requested.

---

## Claim Boundary

This completion proves only that CVF can run from a local production-mode build
and return one live governed `/api/execute` receipt. It does not prove hosted
SaaS readiness, public deployment readiness, multi-tenant readiness,
persistence/database readiness, Maika readiness, broad provider stability,
public product readiness, or any freeze release.
