"""Tests for Skill Control Plane inventory generation and drift checks."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

from generate_assf_skill_index import generate_index
from generate_skill_control_plane_inventory import (
    build_inventory,
    validate_inventory_matches_sources,
)


def _write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _entry(skill_id: str, *, cert: str = "NOT_STARTED", uat: str = "NOT_STARTED") -> dict[str, object]:
    return {
        "registryOrder": 1,
        "skillId": skill_id,
        "name": skill_id,
        "status": "CANDIDATE",
        "canonicalRoot": f"docs/reference/agent_system_skills/registry/entries/{skill_id}.json",
        "certificationState": cert,
        "uatState": uat,
        "internalAgentDisposition": "CANDIDATE",
        "externalCliMcpDisposition": "DEFERRED_WITH_REASON",
    }


def _web_payload(skill_id: str, *, cert: str = "CERTIFIED", uat: str = "PASSED") -> dict[str, object]:
    return {
        "categories": [
            {
                "id": "agent_system_skills",
                "name": "Agent System Skills",
                "skills": [
                    {
                        "id": skill_id,
                        "title": skill_id,
                        "domain": "Agent System Skills",
                        "path": f"docs/reference/agent_system_skills/registry/entries/{skill_id}.json",
                        "assfProjectionClass": "CERTIFIED_PACKAGE_PROJECTION",
                        "canonicalRoot": f"docs/reference/agent_system_skills/registry/entries/{skill_id}.json",
                        "certificationState": cert,
                        "uatState": uat,
                    }
                ],
            }
        ]
    }


class SkillControlPlaneInventoryTests(unittest.TestCase):
    def test_web_certified_projection_passes_when_registry_certified(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            entries_dir = root / "entries"
            index_path = root / "skill-index.json"
            truth_path = root / "truth-index.json"
            web_path = root / "skills-index.json"
            template_path = root / "skill-template-map.json"
            _write_json(entries_dir / "skill-one.json", _entry("skill-one", cert="CERTIFIED", uat="PASSED"))
            _write_json(truth_path, {"entries": []})
            _write_json(web_path, _web_payload("skill-one"))
            _write_json(template_path, {"templateToSkillMap": {}})
            generate_index(index_path, entries_dir)

            inventory = build_inventory(
                entries_dir=entries_dir,
                index_path=index_path,
                package_roots_dir=root / "packages",
                truth_index_path=truth_path,
                web_skill_index_path=web_path,
                web_template_map_path=template_path,
            )

            self.assertEqual(inventory["summary"]["crossSurfaceDriftViolationCount"], 0)
            self.assertEqual(inventory["records"][0]["webProjection"]["assfProjectionClass"], "CERTIFIED_PACKAGE_PROJECTION")

    def test_web_certified_projection_fails_without_registry_certification(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            entries_dir = root / "entries"
            index_path = root / "skill-index.json"
            truth_path = root / "truth-index.json"
            web_path = root / "skills-index.json"
            template_path = root / "skill-template-map.json"
            _write_json(entries_dir / "skill-one.json", _entry("skill-one"))
            _write_json(truth_path, {"entries": []})
            _write_json(web_path, _web_payload("skill-one"))
            _write_json(template_path, {"templateToSkillMap": {}})
            generate_index(index_path, entries_dir)

            inventory = build_inventory(
                entries_dir=entries_dir,
                index_path=index_path,
                package_roots_dir=root / "packages",
                truth_index_path=truth_path,
                web_skill_index_path=web_path,
                web_template_map_path=template_path,
            )

            self.assertIn(
                "WEB_CERTIFIED_PROJECTION_WITHOUT_REGISTRY_CERTIFICATION",
                inventory["records"][0]["drift"]["violations"],
            )

    def test_missing_generated_inventory_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            entries_dir = root / "entries"
            index_path = root / "skill-index.json"
            truth_path = root / "truth-index.json"
            web_path = root / "skills-index.json"
            template_path = root / "skill-template-map.json"
            _write_json(entries_dir / "skill-one.json", _entry("skill-one"))
            _write_json(truth_path, {"entries": []})
            _write_json(web_path, {"categories": []})
            _write_json(template_path, {"templateToSkillMap": {}})
            generate_index(index_path, entries_dir)

            violations = validate_inventory_matches_sources(
                inventory_path=root / "missing.json",
                entries_dir=entries_dir,
                index_path=index_path,
                package_roots_dir=root / "packages",
                truth_index_path=truth_path,
                web_skill_index_path=web_path,
                web_template_map_path=template_path,
            )

            self.assertTrue(any("not found" in v for v in violations))


if __name__ == "__main__":
    unittest.main()
