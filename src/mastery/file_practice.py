from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("JSON root must be an object")
    return data


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def sum_csv_amounts(path: Path) -> int:
    with path.open(encoding="utf-8", newline="") as f:
        rows = csv.DictReader(f)
        return sum(int(row["amount"]) for row in rows)
