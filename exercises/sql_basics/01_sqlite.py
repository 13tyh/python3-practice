"""SQLite の基礎。"""

from __future__ import annotations

import sqlite3


def create_table(conn: sqlite3.Connection) -> None:
    # TODO
    raise NotImplementedError


def insert_user(conn: sqlite3.Connection, name: str) -> int:
    # TODO
    raise NotImplementedError


def list_users(conn: sqlite3.Connection) -> list[tuple[int, str]]:
    # TODO
    raise NotImplementedError

