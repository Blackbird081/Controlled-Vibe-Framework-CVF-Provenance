#!/usr/bin/env python3
"""Environment normalization and platform argv support for release proof."""

from __future__ import annotations

import os
import shutil

from _local_env import bootstrap_repo_env


def bootstrap_live_provider_env() -> None:
    bootstrap_repo_env()
    if os.environ.get("DASHSCOPE_API_KEY"):
        return
    for alias in ("ALIBABA_API_KEY", "CVF_ALIBABA_API_KEY", "CVF_BENCHMARK_ALIBABA_KEY"):
        value = os.environ.get(alias, "").strip()
        if value:
            os.environ["DASHSCOPE_API_KEY"] = value
            return


def platform_cmd(cmd: list[str]) -> list[str]:
    if os.name != "nt" or not cmd:
        return cmd
    executable = shutil.which(cmd[0]) or shutil.which(f"{cmd[0]}.cmd")
    return [executable, *cmd[1:]] if executable else cmd
