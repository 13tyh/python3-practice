from importlib import import_module
import subprocess
import sys

import pytest

target = import_module("exercises.processes.01_subprocess")


def test_run_command() -> None:
    result = target.run_command([sys.executable, "-c", "print('hello')"])
    assert result.returncode == 0
    assert result.stdout.strip() == "hello"


def test_get_stdout() -> None:
    assert target.get_stdout([sys.executable, "-c", "print(123)"]) == "123"
    with pytest.raises(subprocess.CalledProcessError):
        target.get_stdout([sys.executable, "-c", "raise SystemExit(2)"])


def test_command_succeeded() -> None:
    assert target.command_succeeded([sys.executable, "-c", "print('ok')"])
    assert not target.command_succeeded([sys.executable, "-c", "raise SystemExit(1)"])


def test_explain_result() -> None:
    ok = subprocess.CompletedProcess(["x"], 0, "", "")
    ng = subprocess.CompletedProcess(["x"], 7, "", "error")
    assert target.explain_result(ok) == "ok"
    assert target.explain_result(ng) == "failed: 7"

