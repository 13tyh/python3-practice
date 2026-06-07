import sqlite3
from importlib import import_module

target = import_module("exercises.sql_basics.01_sqlite")


def test_sqlite() -> None:
    conn = sqlite3.connect(":memory:")
    target.create_table(conn)
    user_id = target.insert_user(conn, "Aki")
    assert user_id == 1
    assert target.list_users(conn) == [(1, "Aki")]
