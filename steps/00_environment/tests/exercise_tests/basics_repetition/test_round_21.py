from exercises.basics_repetition.round_21 import build_settings, database_url, is_debug


def test_round_21() -> None:
    settings = build_settings({"APP_ENV": "dev", "DEBUG": "true", "DB_PORT": "5432"})
    assert settings == {"env": "dev", "debug": True, "db_port": 5432}
    assert is_debug(settings)
    assert database_url(settings) == "postgresql://localhost:5432/app"
