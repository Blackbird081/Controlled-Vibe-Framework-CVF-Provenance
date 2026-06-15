import governance.compat.run_agent_autorun_workflow_gate as autorun
import governance.compat.run_agent_commit_steward_preflight as steward


def test_range_shape_preflight_blocks_exact_manifest_session_mix(monkeypatch) -> None:
    plan = steward.PathPlan(
        changed_paths=(
            "docs/reviews/example.md",
            "AGENT_HANDOFF_V19_2026-06-15.md",
        ),
        material_paths=("docs/reviews/example.md",),
        protected_session_paths=("AGENT_HANDOFF_V19_2026-06-15.md",),
        trace_artifact_paths=("docs/reviews/example.md",),
        mixed_material_and_session=True,
        exact_manifest_collision_risk=True,
        handoff_sync_only=False,
    )
    monkeypatch.setattr(autorun.steward, "build_path_plan", lambda base, head: plan)

    assert autorun._range_shape_preflight("pre-closure", "base", "head") == 1


def test_range_shape_preflight_allows_split_material_range(monkeypatch) -> None:
    plan = steward.PathPlan(
        changed_paths=("docs/reviews/example.md",),
        material_paths=("docs/reviews/example.md",),
        protected_session_paths=(),
        trace_artifact_paths=("docs/reviews/example.md",),
        mixed_material_and_session=False,
        exact_manifest_collision_risk=False,
        handoff_sync_only=False,
    )
    monkeypatch.setattr(autorun.steward, "build_path_plan", lambda base, head: plan)

    assert autorun._range_shape_preflight("pre-closure", "base", "head") == 0


def test_range_shape_preflight_ignores_pre_dispatch(monkeypatch) -> None:
    monkeypatch.setattr(
        autorun.steward,
        "build_path_plan",
        lambda base, head: (_ for _ in ()).throw(AssertionError("not called")),
    )

    assert autorun._range_shape_preflight("pre-dispatch", "base", "head") == 0
