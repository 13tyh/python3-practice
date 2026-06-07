from __future__ import annotations

import argparse
import subprocess
import sys


def _run(command: list[str]) -> int:
    print(f"$ {' '.join(command)}")
    return subprocess.run(command, check=False).returncode


def _run_all(commands: list[list[str]]) -> int:
    for command in commands:
        code = _run(command)
        if code != 0:
            return code
    return 0


def lint() -> None:
    code = _run_all(
        [
            ["ruff", "check", "."],
            ["mypy", "src"],
        ]
    )
    raise SystemExit(code)


def fmt() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fix", action="store_true", help="format files in place")
    args = parser.parse_args()

    if args.fix:
        commands = [
            ["ruff", "check", ".", "--fix"],
            ["ruff", "format", "."],
            ["black", "."],
        ]
    else:
        commands = [
            ["ruff", "format", ".", "--check"],
            ["black", ".", "--check"],
        ]

    raise SystemExit(_run_all(commands))


def build() -> None:
    code = _run_all(
        [
            ["ruff", "format", ".", "--check"],
            ["black", ".", "--check"],
            ["ruff", "check", "."],
            ["mypy", "src"],
            ["pytest", "-q"],
        ]
    )
    raise SystemExit(code)


if __name__ == "__main__":
    command = sys.argv[1] if len(sys.argv) > 1 else ""
    if command == "lint":
        lint()
    elif command == "fmt":
        sys.argv = [sys.argv[0], *sys.argv[2:]]
        fmt()
    elif command == "build":
        build()
    else:
        raise SystemExit("usage: python -m tools.dev_commands [lint|fmt|build]")
