<!-- Memory class: FULL_RECORD -->
# CVF CI2 Hosted Live Gate Operator Dispatch Runbook

**Date:** 2026-05-09
**Track:** CI2-H1 - Manual Hosted Run
**Status:** OPERATOR OR GITHUB-ENABLED AGENT ACTION REQUIRED

## Prerequisites

- The latest commits are on `origin/main`.
- GitHub environment `cvf-live-release-gate` exists.
- At least one DashScope-compatible secret is configured in that environment:
  `DASHSCOPE_API_KEY`, `ALIBABA_API_KEY`, `CVF_ALIBABA_API_KEY`, or
  `CVF_BENCHMARK_ALIBABA_KEY`.
- Do not print secret values. Secret-name metadata is enough.

## Metadata Sanity

```bash
gh repo view --json owner,name,url
gh api repos/{owner}/{repo}/environments/cvf-live-release-gate
gh api repos/{owner}/{repo}/environments/cvf-live-release-gate/secrets --jq '.secrets[].name'
```

Expected:

- environment lookup succeeds;
- at least one DashScope-compatible secret name is listed;
- no secret values are printed.

## Dispatch

```bash
gh workflow run cvf-protected-live-release-gate.yml \
  --ref main \
  -f confirm_live_provider_cost=RUN_LIVE_GATE
```

Then watch:

```bash
gh run list --workflow cvf-protected-live-release-gate.yml --branch main --limit 5
gh run watch <run-id> --exit-status
```

Download the result artifact:

```bash
mkdir -p .cvf/runtime/ci2h-hosted
gh run download <run-id> \
  -n cvf-protected-live-release-gate-result \
  -D .cvf/runtime/ci2h-hosted
```

## PASS Artifact Requirements

File a follow-up review artifact only after the hosted run completes:

- run ID and GitHub run URL;
- head SHA;
- workflow conclusion;
- artifact name and local download path;
- release gate `gate_result`;
- 7-check breakdown from `cvf-protected-live-release-gate-result.json`;
- explicit statement that no raw provider key is present in the artifact.

## Claim Sync If PASS

Only after hosted PASS:

- update `AGENT_HANDOFF_POST_RC2_GA_READINESS_2026-05-08.md`;
- update `docs/reviews/CVF_GA_READINESS_DECISION_2026-05-08.md`;
- update `docs/reviews/CVF_GA_READINESS_EVIDENCE_INDEX_2026-05-08.md`;
- change CI2-H from deferred/blocked to hosted PASS;
- change decision from `GA_LOCAL_FIRST_APPROVED_WITH_LIMITS` to
  `GA_LOCAL_FIRST_APPROVED`.

## Failure Path

If the hosted run fails, file a failure artifact instead of retrying silently.
Classify the failure as one of:

- missing environment;
- missing secret metadata;
- environment approval not granted;
- live provider quota or auth failure;
- release gate failure;
- hosted infrastructure failure.
