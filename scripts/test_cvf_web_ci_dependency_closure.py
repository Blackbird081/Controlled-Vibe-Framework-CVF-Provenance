"""Workflow dependency closure only; no install, network or release claim."""
import json
import re
import unittest
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
WEB = Path("EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web")
WORKFLOWS = ("ci.yml", "cvf-ci.yml", "cvf-web-ci.yml")


def local_dependencies(directory):
    package = json.loads((ROOT / directory / "package.json").read_text(encoding="utf-8"))
    return {(directory / value[5:]).resolve().relative_to(ROOT.resolve())
            for value in package.get("dependencies", {}).values() if value.startswith("file:")}


def validate_job(job):
    default = job["defaults"]["run"]["working-directory"]
    installed = set()
    for step in job["steps"]:
        directory = Path(step.get("working-directory", default))
        for line in step.get("run", "").splitlines():
            if not re.fullmatch(r"npm (?:ci|install)(?: --no-audit --no-fund)?", line.strip()):
                continue
            if directory == WEB or directory in local_dependencies(WEB):
                missing = local_dependencies(directory) - installed
                if missing:
                    raise AssertionError(f"{directory}: unresolved predecessors {sorted(map(str, missing))}")
                if line.strip() != "npm ci":
                    raise AssertionError(f"{directory}: unlocked install")
                if not (ROOT / directory / "package-lock.json").is_file():
                    raise AssertionError(f"{directory}: missing lockfile")
                installed.add(directory)
    if WEB not in installed:
        raise AssertionError("Web install missing")


class WebCiDependencyClosureTests(unittest.TestCase):
    def test_all_web_jobs_follow_actual_dependency_graph(self):
        count = 0
        for name in WORKFLOWS:
            data = yaml.safe_load((ROOT / ".github/workflows" / name).read_text(encoding="utf-8"))
            for job_name, job in data["jobs"].items():
                if job.get("defaults", {}).get("run", {}).get("working-directory") != WEB.as_posix():
                    continue
                count += 1
                with self.subTest(workflow=name, job=job_name):
                    validate_job(job)
        self.assertEqual(count, 6)

    def test_dependency_changes_trigger_dedicated_web_workflow(self):
        # BaseLoader preserves YAML 'on' rather than interpreting it as YAML1.1 bool.
        data = yaml.load((ROOT / ".github/workflows/cvf-web-ci.yml").read_text(encoding="utf-8"), Loader=yaml.BaseLoader)
        required = {WEB.as_posix() + "/**", *(p.as_posix() + "/**" for p in local_dependencies(WEB))}
        for event in ("push", "pull_request"):
            with self.subTest(event=event):
                self.assertTrue(required <= set(data["on"][event]["paths"]))

    def test_missing_dependency_is_rejected(self):
        job = {"defaults": {"run": {"working-directory": WEB.as_posix()}},
               "steps": [{"run": "npm ci"}]}
        with self.assertRaisesRegex(AssertionError, "unresolved predecessors"):
            validate_job(job)

    def test_predecessor_order_is_enforced(self):
        job = {"defaults": {"run": {"working-directory": WEB.as_posix()}},
               "steps": [{"working-directory": "EXTENSIONS/CVF_MODEL_GATEWAY", "run": "npm ci"}]}
        with self.assertRaisesRegex(AssertionError, "unresolved predecessors"):
            validate_job(job)

    def test_unlocked_install_is_rejected_after_valid_predecessors(self):
        steps = [{"working-directory": "EXTENSIONS/" + name, "run": "npm ci"}
                 for name in ("CVF_CONTROL_PLANE_FOUNDATION", "CVF_GUARD_CONTRACT")]
        steps.append({"working-directory": "EXTENSIONS/CVF_MODEL_GATEWAY",
                      "run": "npm install --no-audit --no-fund"})
        job = {"defaults": {"run": {"working-directory": WEB.as_posix()}}, "steps": steps}
        with self.assertRaisesRegex(AssertionError, "unlocked install"):
            validate_job(job)


if __name__ == "__main__":
    unittest.main()
