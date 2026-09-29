"""Bounded provider-execution grant composition for governed live runners.

Pure environment-shape helper: it performs no I/O and never handles API-key
material. The caller remains responsible for obtaining operator authority and
for binding its own one-use runner permit to the live evidence path.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone


def build_provider_execution_grant_env(
    *,
    grant_id: str,
    subject_agent_id: str,
    delegation_id: str,
    provider: str,
    max_calls: int,
    expires_at_epoch_ms: int,
) -> dict[str, str]:
    if not all(value.strip() for value in (grant_id, subject_agent_id, delegation_id, provider)):
        raise ValueError("provider execution grant identifiers must be non-empty")
    if max_calls < 1:
        raise ValueError("provider execution max_calls must be positive")

    expires_at = datetime.fromtimestamp(expires_at_epoch_ms / 1000, tz=timezone.utc).isoformat()
    grant = {
        "authority": "ORCHESTRATOR_GRANT_REQUIRED",
        "grantId": grant_id,
        "authorizedBy": "ORCHESTRATOR",
        "subjectAgentId": subject_agent_id,
        "delegationId": delegation_id,
        "allowedProviders": [provider],
        "maxCalls": max_calls,
        "expiresAt": expires_at,
    }
    return {
        "CVF_AGENT_ID": subject_agent_id,
        "CVF_DELEGATION_ID": delegation_id,
        "CVF_PROVIDER_EXECUTION_GRANT_ID": grant_id,
        "CVF_PROVIDER_EXECUTION_GRANT_JSON": json.dumps(grant, sort_keys=True, separators=(",", ":")),
    }
