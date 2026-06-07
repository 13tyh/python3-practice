"""JSON / CSV の追加練習。"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any


def dumps_pretty(data: dict[str, Any]) -> str:
    # TODO
    raise NotImplementedError


def loads_dict(text: str) -> dict[str, Any]:
    # TODO
    raise NotImplementedError


def read_csv_names(path: Path) -> list[str]:
    # TODO
    raise NotImplementedError


def write_csv_rows(path: Path, rows: list[dict[str, str]]) -> None:
    # TODO
    raise NotImplementedError

