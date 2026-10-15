"""Owned Windows process identities and one failure-preserving cleanup collector."""
from __future__ import annotations

import csv
import ctypes as C
import io
import json
import os
import re
import shutil
import subprocess
import time
from pathlib import Path
from ctypes import wintypes as W


class Collector:
    def __init__(self, custody: Path, runner=None):
        self.custody, self.runner, self.events = custody, runner or subprocess.run, []
        self.deadline = None

    def remaining(self, requested):
        remaining = requested if self.deadline is None else min(requested, self.deadline - time.monotonic())
        if remaining <= 0:
            raise TimeoutError("owned invocation deadline exhausted before command/start")
        return remaining

    def command(self, kind, argv, *, timeout=10, data=None):
        started = time.monotonic()
        timeout = self.remaining(timeout)
        event = {"kind": kind, "argv": list(argv), "timeoutSeconds": timeout}
        try:
            p = self.runner(argv, input=data, capture_output=True, text=True,
                            encoding="utf-8", errors="replace", timeout=timeout)
            event.update(exitCode=p.returncode, stdout=p.stdout, stderr=p.stderr, timedOut=False)
        except subprocess.TimeoutExpired:
            event.update(exitCode=None, stdout="", stderr="", timedOut=True)
        event["elapsedSeconds"] = round(time.monotonic() - started, 4)
        self.events.append(event)
        self.flush()
        if event["timedOut"] or event["exitCode"] != 0:
            raise RuntimeError(f"{kind}: command failed or timed out; evidence retained")
        return event["stdout"]

    def flush(self):
        self.custody.mkdir(parents=True, exist_ok=True)
        (self.custody / "commands.json").write_text(json.dumps(self.events, indent=2), encoding="utf-8")


def parse_tasklist(raw):
    rows = list(csv.reader(io.StringIO(raw)))
    if not rows or any(len(r) != 5 or not r[1].isdigit() for r in rows):
        raise RuntimeError("tasklist query was malformed, not proof of absence")
    return {int(r[1]) for r in rows}


def parse_docker_ids(raw):
    rows = raw.splitlines()
    if any(not re.fullmatch(r"[a-f0-9]{64}", r) for r in rows):
        raise RuntimeError("Docker query was malformed, not proof of absence")
    return set(rows)


def no_reparse(path: Path):
    if path.is_symlink() or (path.exists() and getattr(path.lstat(), "st_file_attributes", 0) & 0x400):
        raise RuntimeError(f"reparse path refused: {path.name}")


def remove_disposable(stage: Path, namespace: Path, dependency=None):
    no_reparse(namespace)
    no_reparse(stage)
    if stage.resolve() != namespace.resolve() / "source" or not (namespace / "owner.json").is_file():
        raise RuntimeError("unsafe disposal target")
    if dependency:
        link, target = dependency
        if link.exists():
            if link.resolve() != target.resolve() or not link.is_relative_to(stage):
                raise RuntimeError("dependency link identity changed")
            os.rmdir(link)  # exact junction only; never traverse the installed dependency target
    if stage.exists():
        for base, dirs, files in os.walk(stage, followlinks=False):
            for name in dirs + files:
                no_reparse(Path(base) / name)
        shutil.rmtree(stage)


class Native:
    """Job membership owns descendants; retained process handles pin creation identity."""
    def __init__(self, collector, docker_prefix, stage, namespace):
        if os.name != "nt":
            raise RuntimeError("this admitted native profile requires Windows")
        self.c, self.docker = collector, docker_prefix
        self.stage, self.namespace, self.dependency = stage, namespace, None
        self.roots, self.container, self.container_identity, self.ports = [], None, None, []
        self.container_identity_pending = False
        self.retained = {}
        self.k = C.WinDLL("kernel32", use_last_error=True)
        signatures = {
            "CreateJobObjectW": ([C.c_void_p, W.LPCWSTR], W.HANDLE),
            "OpenProcess": ([W.DWORD, W.BOOL, W.DWORD], W.HANDLE),
            "GetProcessTimes": ([W.HANDLE, C.c_void_p, C.c_void_p, C.c_void_p, C.c_void_p], W.BOOL),
            "QueryFullProcessImageNameW": ([W.HANDLE, W.DWORD, W.LPWSTR, C.POINTER(W.DWORD)], W.BOOL),
            "AssignProcessToJobObject": ([W.HANDLE, W.HANDLE], W.BOOL),
            "QueryInformationJobObject": ([W.HANDLE, C.c_int, C.c_void_p, W.DWORD, C.c_void_p], W.BOOL),
            "WaitForSingleObject": ([W.HANDLE, W.DWORD], W.DWORD),
            "CloseHandle": ([W.HANDLE], W.BOOL),
            "CreateToolhelp32Snapshot": ([W.DWORD, W.DWORD], W.HANDLE),
            "OpenThread": ([W.DWORD, W.BOOL, W.DWORD], W.HANDLE),
            "ResumeThread": ([W.HANDLE], W.DWORD),
        }
        for name, (args, result) in signatures.items():
            getattr(self.k, name).argtypes, getattr(self.k, name).restype = args, result
        self.job = self.k.CreateJobObjectW(None, None)
        if not self.job:
            raise C.WinError(C.get_last_error())

    def identity(self, pid, handle=None):
        h = handle or self.k.OpenProcess(0x1000 | 0x100000, False, pid)
        if not h:
            raise RuntimeError(f"process identity unavailable: {pid}")
        try:
            values = [C.c_ulonglong() for _ in range(4)]
            name, size = C.create_unicode_buffer(32768), W.DWORD(32768)
            if not self.k.GetProcessTimes(h, *(C.byref(v) for v in values)) or not self.k.QueryFullProcessImageNameW(h, 0, name, C.byref(size)):
                raise C.WinError(C.get_last_error())
            return {"pid": pid, "creation100ns": values[0].value, "image": name.value}
        finally:
            if not handle:
                self.k.CloseHandle(h)

    def launch(self, argv, *, cwd, env, stdout, stdin=None):
        self.c.remaining(1)
        p = subprocess.Popen(argv, cwd=cwd, env=env, stdout=stdout, stderr=subprocess.STDOUT,
                             stdin=stdin, creationflags=0x00000004,  # Windows CREATE_SUSPENDED; not exported by subprocess
                             text=stdin is not None, encoding="utf-8" if stdin is not None else None)
        root = {"p": p, "identity": None, "argv": list(argv)}
        self.roots.append(root)
        try:
            if not self.k.AssignProcessToJobObject(self.job, int(p._handle)):
                raise RuntimeError("cannot assign suspended owned process to descendant job")
            root["identity"] = self.identity(p.pid, int(p._handle))
            (self.c.custody / "process-roots.json").write_text(json.dumps(
                [{k: v for k, v in x.items() if k != "p"} for x in self.roots], indent=2), encoding="utf-8")
            self._resume_owned(p)
        except BaseException:
            # Popen retains the exact creation handle even when identity capture fails.
            # Never leave an unregistered suspended child or kill a recycled PID.
            if p.poll() is None:
                p.kill()
            p.wait(timeout=5)
            raise
        return p

    def _resume_owned(self, p):
        self.c.remaining(1)
        # Resume only this suspended process's main thread, after ownership has been persisted.
        class ThreadEntry(C.Structure):
            _fields_ = [("size", W.DWORD), ("usage", W.DWORD), ("tid", W.DWORD),
                        ("pid", W.DWORD), ("priority", W.LONG), ("delta", W.LONG), ("flags", W.DWORD)]
        snap, entry = self.k.CreateToolhelp32Snapshot(4, 0), ThreadEntry()
        entry.size = C.sizeof(entry)
        self.k.Thread32First.argtypes = self.k.Thread32Next.argtypes = [W.HANDLE, C.POINTER(ThreadEntry)]
        try:
            ok, resumed = self.k.Thread32First(snap, C.byref(entry)), 0
            while ok:
                if entry.pid == p.pid:
                    thread = self.k.OpenThread(2, False, entry.tid)
                    if not thread:
                        raise RuntimeError("owned suspended thread could not resume")
                    try:
                        if self.k.ResumeThread(thread) == 0xFFFFFFFF:
                            raise RuntimeError("owned suspended thread could not resume")
                    finally:
                        self.k.CloseHandle(thread)
                    resumed += 1
                ok = self.k.Thread32Next(snap, C.byref(entry))
            if resumed != 1:
                raise RuntimeError("unexpected suspended thread count")
        finally:
            self.k.CloseHandle(snap)

    def members(self):
        raw = C.create_string_buffer(65536)
        if not self.k.QueryInformationJobObject(self.job, 3, raw, len(raw), None):
            raise RuntimeError("descendant job query failed")
        assigned, count = C.cast(raw, C.POINTER(W.DWORD))[:2]
        if count != assigned:
            raise RuntimeError("descendant query was truncated")
        ids = (C.c_size_t * count).from_buffer(raw, 8)
        return list(ids)

    def prepare_kill(self):
        owned = set(self.members())
        for x in self.roots:
            p = x["p"]
            if p.poll() is None and self.identity(p.pid) != x["identity"]:
                raise RuntimeError("root process creation identity changed")
        identities = []
        for pid in sorted(owned):
            handle = self.k.OpenProcess(0x1000 | 0x100000, False, pid)
            if not handle:
                raise RuntimeError("descendant identity handle unavailable")
            self.retained[pid] = handle
            identities.append(self.identity(pid, handle))
        (self.c.custody / "descendants-before-cleanup.json").write_text(json.dumps(identities, indent=2), encoding="utf-8")
        return identities

    def kill(self, identity):
        if self.k.WaitForSingleObject(self.retained[identity["pid"]], 0) == 0:
            return  # retained creation handle proves this exact owned process already exited
        if self.identity(identity["pid"]) != identity:
            raise RuntimeError("identity changed before taskkill")
        self.c.command("taskkill", ["taskkill", "/PID", str(identity["pid"]), "/F"], timeout=5)

    def remove_container(self):
        if self.container:
            actual = json.loads(self.c.command("container-identity", [*self.docker, "inspect", self.container]))[0]
            if [actual["Id"], actual["Image"], actual["Name"]] != self.container_identity:
                raise RuntimeError("container identity changed before removal")
            self.c.command("container-remove", [*self.docker, "rm", "-f", self.container], timeout=15)

    def query_processes(self):
        return parse_tasklist(self.c.command("tasklist", ["tasklist", "/NH", "/FO", "CSV"], timeout=10))

    def query_containers(self):
        return parse_docker_ids(self.c.command("docker-ps", [*self.docker, "ps", "-a", "--no-trunc", "--format", "{{.ID}}"], timeout=10))

    def listeners(self):
        raw = self.c.command("netstat", ["netstat", "-ano", "-p", "tcp"], timeout=10)
        rows = [r.split() for r in raw.splitlines() if r.strip().startswith("TCP")]
        if any(len(r) != 5 or not r[4].isdigit() for r in rows):
            raise RuntimeError("native listener query malformed")
        return [{"address": r[1], "pid": int(r[4])} for r in rows if r[3] == "LISTENING" and int(r[1].rsplit(":", 1)[1]) in self.ports]

    def dispose(self):
        remove_disposable(self.stage, self.namespace, self.dependency)

    def close(self):
        for handle in self.retained.values():
            self.k.CloseHandle(handle)
        self.k.CloseHandle(self.job)


def finalize(ops, failures, *, seconds=120):
    """Always query after action errors; deletion is conditional on successful native absence."""
    until = time.monotonic() + seconds
    result = {"errors": [], "ownedIdentities": [], "processQuery": "UNKNOWN", "containerQuery": "UNKNOWN",
              "descendantQuery": "UNKNOWN", "listenerQuery": "UNKNOWN", "stageRemoved": False}
    if getattr(ops, "container_identity_pending", False):
        result["errors"].append("container identity unresolved after creation attempt; preserve stage")
    def attempt(label, fn):
        try:
            if time.monotonic() >= until:
                raise TimeoutError("cleanup deadline exhausted")
            return fn()
        except Exception as error:
            result["errors"].append(f"{label}: {type(error).__name__}: {str(error)[:180]}")
    try:
        identities = attempt("identity", ops.prepare_kill)
        if identities is not None:
            result["ownedIdentities"] = identities
            # Individual exact PID actions keep creation checks immediately before each effect.
            for identity in reversed(identities):
                attempt("taskkill", lambda x=identity: ops.kill(x))
        attempt("container-remove", ops.remove_container)
        pids, containers, members, listeners = (attempt("tasklist", ops.query_processes),
            attempt("docker-ps", ops.query_containers), attempt("descendants", ops.members), attempt("listeners", ops.listeners))
        if pids is not None:
            result["processQuery"] = "ABSENT" if not (set(pids) & {x["pid"] for x in result["ownedIdentities"]}) else "LIVE"
        if containers is not None and not getattr(ops, "container_identity_pending", False):
            result["containerQuery"] = "ABSENT" if ops.container not in containers else "LIVE"
        if members is not None:
            result["descendantQuery"] = "ABSENT" if not members else "LIVE"
        if listeners is not None:
            result["listenerQuery"] = "ABSENT" if not listeners else "LIVE"
        if not result["errors"] and all(result[k] == "ABSENT" for k in ("processQuery", "containerQuery", "descendantQuery", "listenerQuery")):
            attempt("disposal", ops.dispose)
            result["stageRemoved"] = not ops.stage.exists()
        result["disposition"] = "ACCEPTED_CLEANUP" if not failures and not result["errors"] and result["stageRemoved"] else "NOT_ACCEPTED_UNKNOWN"
        return result
    finally:
        ops.close()
