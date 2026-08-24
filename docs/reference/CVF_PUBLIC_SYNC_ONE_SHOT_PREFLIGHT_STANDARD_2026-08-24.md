# CVF Public-Sync One-Shot Preflight Standard

Memory class: governed-standard

Status: ACTIVE

Date: 2026-08-24

## Purpose

Prevent a public GitHub push from turning into a long sequence of predictable
projection repairs. Public-sync safety is evaluated once against the complete
pending candidate before reviewer handoff, commit, or push.

## Scope / Applies To

Applies to the private provenance exporter, the sibling public-sync candidate,
and agents acting as public-sync worker, reviewer, closer, or session-sync
steward. The provenance repository owns the rule and checker; the public clone
is only the bounded projection target. Public commit, push, live/provider
execution, and unrelated historical debt repair remain outside this authority.

## Incident Learning

The 2026-08-24 public sync required several serial repair rounds even though
the network push itself completed in seconds. The avoidable latency came from
using an inapplicable private hook, discovering related dependency defects one
at a time, running an over-broad web suite in the real public worktree, and
allowing generated runtime residue to reach the staging boundary.

Classification: `WORKER_EXECUTION_ERROR`, `ORCHESTRATOR_PACKET_GAP`,
`MACHINE_GATE_GAP`, and `PHASE_GATE_PLACEMENT_GAP`.

## Binding Rules

1. Use the public-sync exporter and its current-candidate preflight. Do not use
   a private-repository hook or a range-pinned projection policy when its
   declared base, head, branch, or repository identity does not match.
2. Build the full projection before review, then evaluate pending-path
   ownership, generated/runtime residue, diff hygiene, and relative source
   dependency closure in one machine pass.
3. A failed preflight returns one consolidated violation set. Repair that set
   as one bounded batch and rerun once; do not ask a reviewer to discover each
   predictable downstream edge serially.
4. Run project suites only in a disposable clean clone or worktree made from
   the exact candidate. Exclude live/provider-named tests unless a separate
   live-proof authorization explicitly selects them. Never rely on ambient
   credentials for public-sync verification.
5. `-NoCommit` is a review boundary, not a bypass: the one-shot preflight must
   pass before the exporter returns a candidate for human or agent review.
6. `git add -A`, commit, and push remain downstream of the same preflight.
   Unowned pending paths fail closed.
7. Dependency defects already present in the exact public `HEAD` are reported
   as non-blocking baseline debt. A candidate that adds a missing edge or
   removes a previously present target fails; the gate must not turn unrelated
   historical cleanup into an unbounded prerequisite for the current push.
8. A public `main` update must carry the server-side
   `public-sync-preflight` status for the exact commit SHA. The exporter pushes
   a candidate branch first, waits for that GitHub Actions result, and only
   then promotes the identical commit. Branch protection applies to admins;
   local `--no-verify` cannot bypass the server requirement.

## Machine Binding

`scripts/check_cvf_public_sync_candidate.py` is the candidate preflight.
`scripts/cvf-public-sync.ps1` invokes it after projection-owned generation and
before the `-NoCommit` return or staging. Focused tests live at
`scripts/test_check_cvf_public_sync_candidate.py`.
`scripts/cvf-public-pre-push-hook.sh` is mapped to public
`.githooks/pre-push` and supplies local fail-fast enforcement;
`.github/workflows/public-sync-preflight.yml` supplies the server status.

Required failure codes include `UNOWNED_PENDING_PATH`,
`GENERATED_OR_RUNTIME_RESIDUE`, `DIFF_HYGIENE`,
`MISSING_RELATIVE_DEPENDENCY`, `WRONG_REMOTE`, and `WRONG_BRANCH`.
The JSON receipt separately reports `baselineDebtCount` and `baselineDebt`.

## Verification

```powershell
python -m pytest scripts/test_check_cvf_public_sync_candidate.py
powershell -ExecutionPolicy Bypass -File scripts/cvf-public-sync.ps1 -NoCommit
```

The second command intentionally updates the public candidate and is used only
when public-sync work is authorized. A successful preflight is not permission
to commit or push.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Batch status |
|---|---|---|---|---|---|
| Public push latency was dominated by serial, predictable projection repair | ORCHESTRATOR_PACKET_GAP; PHASE_GATE_PLACEMENT_GAP | GOVERNANCE_CONTROL_PLANE | STANDARD_ADDED; MACHINE_CHECK_ADDED | keep one-shot candidate preflight before review and staging | handled |
| Full/live-named tests ran in the real public worktree and produced residue | WORKER_EXECUTION_ERROR; MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | RULE_ADDED; MACHINE_CHECK_ADDED | disposable verification plus residue rejection | handled |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance public-sync operating control; the public exporter
and its internal repository boundary are not public artifacts.

## Claim Boundary

This standard and preflight prevent the named local projection defects from
passing the pre-review boundary. They do not prove semantic completeness of
all public artifacts, authorize live/provider execution, or authorize a public
commit or push.
