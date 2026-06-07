"""CSV export の練習。"""

from __future__ import annotations

import csv
from pathlib import Path


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    # TODO
    raise NotImplementedError


def read_csv(path: Path) -> list[dict[str, str]]:
    # TODO
    raise NotImplementedError


def export_documents_to_csv(
    path: Path,
    documents: list[dict[str, object]],
    fieldnames: list[str],
) -> None:
    # TODO
    raise NotImplementedError

