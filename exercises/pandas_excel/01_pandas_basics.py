"""pandas 基礎。"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def load_csv(path: Path) -> pd.DataFrame:
    # TODO
    raise NotImplementedError


def total_by_category(df: pd.DataFrame) -> pd.DataFrame:
    # TODO
    raise NotImplementedError


def export_excel(path: Path, sheets: dict[str, pd.DataFrame]) -> None:
    # TODO
    raise NotImplementedError

