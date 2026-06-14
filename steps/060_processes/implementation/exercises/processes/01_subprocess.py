"""subprocess の練習。"""

from __future__ import annotations

import subprocess


def run_command(command: list[str], timeout: int = 5) -> subprocess.CompletedProcess[str]:
    """コマンドを実行し、stdout/stderrを文字列で受け取る。"""
    # TODO
    raise NotImplementedError


def get_stdout(command: list[str]) -> str:
    """成功したコマンドのstdoutをstripして返す。失敗時はCalledProcessError。"""
    # TODO
    raise NotImplementedError


def command_succeeded(command: list[str]) -> bool:
    """returncodeが0ならTrue。例外は出さない。"""
    # TODO
    raise NotImplementedError


def explain_result(result: subprocess.CompletedProcess[str]) -> str:
    """成功ならok、失敗ならfailed: <returncode>。"""
    # TODO
    raise NotImplementedError
