from exercises.basics_repetition.round_12 import apply_all, fallback, make_prefixer


def test_round_12() -> None:
    assert apply_all(" hello ", [str.strip, str.upper]) == "HELLO"
    prefixer = make_prefixer("user:")
    assert prefixer("1") == "user:1"
    assert fallback(lambda: "ok", "ng") == "ok"
    assert fallback(lambda: (_ for _ in ()).throw(RuntimeError()), "ng") == "ng"
