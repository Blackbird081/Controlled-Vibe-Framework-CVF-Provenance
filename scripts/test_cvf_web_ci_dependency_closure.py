"""Workflow dependency closure only; no install, network or release claim."""
import json
import re
import shlex
import subprocess
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
    target = Path(default)
    installed = set()
    for step in job["steps"]:
        directory = Path(step.get("working-directory", default))
        for line in step.get("run", "").splitlines():
            args = shlex.split(line.strip())
            if len(args) < 2 or args[:2] not in (["npm", "ci"], ["npm", "install"]):
                continue
            package_dir = directory
            if "--prefix" in args:
                package_dir = (ROOT / directory / args[args.index("--prefix") + 1]).resolve().relative_to(ROOT.resolve())
            if not (ROOT / package_dir / "package.json").is_file():
                raise AssertionError(f"{package_dir}: missing package at install path")
            missing = local_dependencies(package_dir) - installed
            if missing:
                raise AssertionError(f"{package_dir}: unresolved predecessors {sorted(map(str, missing))}")
            if args[1] != "ci":
                raise AssertionError(f"{package_dir}: unlocked install")
            if not (ROOT / package_dir / "package-lock.json").is_file():
                raise AssertionError(f"{package_dir}: missing lockfile")
            lock_path = (package_dir / "package-lock.json").as_posix()
            tracked = subprocess.run(["git", "ls-files", "--error-unmatch", "--", lock_path],
                                     cwd=ROOT, capture_output=True, check=False)
            if tracked.returncode:
                raise AssertionError(f"{package_dir}: lockfile not tracked in candidate index")
            installed.add(package_dir)
    if target == WEB and Path("EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER") not in installed:
        raise AssertionError("Web source consumer MCP dependency install missing")
    if target not in installed:
        raise AssertionError(f"{target}: target install missing")


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

    def test_related_guard_mcp_execution_jobs(self):
        selected = {"ci.yml": ["guard-contract-tests"],
                    "cvf-ci.yml": ["test-guard-contract", "test-mcp-server", "test-epf"]}
        for name, jobs in selected.items():
            data = yaml.safe_load((ROOT / ".github/workflows" / name).read_text(encoding="utf-8"))
            for job_name in jobs:
                with self.subTest(workflow=name, job=job_name):
                    validate_job(data["jobs"][job_name])

    def test_invalid_prefix_is_rejected(self):
        job = {"defaults": {"run": {"working-directory": "EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER"}},
               "steps": [{"run": "npm ci --prefix ../../CVF_TRUTH_KERNEL"}]}
        with self.assertRaisesRegex(AssertionError, "missing package"):
            validate_job(job)

    def test_prefix_resolves_from_step_directory(self):
        job = {"defaults": {"run": {"working-directory": "EXTENSIONS/CVF_TRUTH_FLOW"}},
               "steps": [{"run": "npm ci --prefix ../CVF_TRUTH_KERNEL"}, {"run": "npm ci"}]}
        validate_job(job)

    def test_build_steps_use_canonical_structural_auth_profile(self):
        from cvf_release_web_runtime_isolation import WEB_BUILD_STRUCTURAL_ENV
        count = 0
        for name in WORKFLOWS:
            data = yaml.safe_load((ROOT / ".github/workflows" / name).read_text(encoding="utf-8"))
            for job in data["jobs"].values():
                if job.get("defaults", {}).get("run", {}).get("working-directory") != WEB.as_posix():
                    continue
                for step in job["steps"]:
                    if step.get("run") == "npm run build":
                        count += 1
                        self.assertEqual(step.get("env"), WEB_BUILD_STRUCTURAL_ENV)
        self.assertEqual(count, 4)
        bindings = json.loads(WEB_BUILD_STRUCTURAL_ENV["CVF_OAUTH_IDENTITY_BINDINGS_JSON"])
        self.assertEqual(WEB_BUILD_STRUCTURAL_ENV["CVF_OAUTH_PROVIDER"], "github")
        self.assertEqual(bindings[0]["provider"], "github")
        self.assertEqual(bindings[0]["role"], "viewer")

    def test_dependency_changes_trigger_dedicated_web_workflow(self):
        # BaseLoader preserves YAML 'on' rather than interpreting it as YAML1.1 bool.
        data = yaml.load((ROOT / ".github/workflows/cvf-web-ci.yml").read_text(encoding="utf-8"), Loader=yaml.BaseLoader)
        required = {"EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/**", WEB.as_posix() + "/**", *(p.as_posix() + "/**" for p in local_dependencies(WEB))}
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
