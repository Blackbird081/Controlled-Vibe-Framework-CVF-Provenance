from pathlib import Path

import pytest

from scripts.external_agent_snapshot_projection import (
    SnapshotProjectionError,
    project_current_public_posture,
)


STALE_SNAPSHOT = """## 3. Public product posture at this commit

The public front door describes CVF as:

- a governance-first control plane for AI-assisted work;
- local-first release candidate `4.0.0-rc.1`, not hosted SaaS;

## 5. Provider boundary

At this commit, the public README identifies:

- Alibaba `qwen-turbo`: `CERTIFIED` public lane;
- DeepSeek `deepseek-chat`: `CERTIFIED` public lane;
- OpenAI: model-specific historical canary evidence but `EXPERIMENTAL` under
  the reviewed public boundary.

These are lane-specific evidence statements.
"""


def _write_public_sources(root: Path, *, include_openai: bool = True) -> None:
    (root / "CHANGELOG.md").write_text(
        "# Changelog\n\n## [v4.0.0] - GA Release\n\nStatus: GA_LOCAL_FIRST_APPROVED\n",
        encoding="utf-8",
    )
    matrix = root / "docs/reference/CVF_PROVIDER_LANE_READINESS_MATRIX.md"
    matrix.parent.mkdir(parents=True)
    rows = [
        "| Alibaba | `qwen-flash` | `EXPERIMENTAL` | evidence | gate | notes |",
        "| DeepSeek | `deepseek-chat` | `CERTIFIED` | evidence | gate | notes |",
    ]
    if include_openai:
        rows.append("| OpenAI | `gpt-4o-mini` | `EXPERIMENTAL` | evidence | gate | notes |")
    matrix.write_text("\n".join(rows) + "\n", encoding="utf-8")


def test_projection_replaces_stale_release_and_provider_claims(tmp_path: Path) -> None:
    _write_public_sources(tmp_path)
    projected = project_current_public_posture(STALE_SNAPSHOT, tmp_path)
    assert "`v4.0.0` GA release (`GA_LOCAL_FIRST_APPROVED`)" in projected
    assert "Alibaba `qwen-flash`: `EXPERIMENTAL` public lane" in projected
    assert "DeepSeek `deepseek-chat`: `CERTIFIED` public lane" in projected
    assert "OpenAI `gpt-4o-mini`: `EXPERIMENTAL` public lane" in projected
    assert "4.0.0-rc.1" not in projected
    assert "qwen-turbo" not in projected
    assert project_current_public_posture(projected, tmp_path) == projected


def test_projection_fails_closed_when_required_provider_is_missing(tmp_path: Path) -> None:
    _write_public_sources(tmp_path, include_openai=False)
    with pytest.raises(SnapshotProjectionError, match="OpenAI"):
        project_current_public_posture(STALE_SNAPSHOT, tmp_path)


def test_projection_fails_closed_when_snapshot_shape_drifts(tmp_path: Path) -> None:
    _write_public_sources(tmp_path)
    with pytest.raises(SnapshotProjectionError, match="public product release posture"):
        project_current_public_posture("unexpected template", tmp_path)
