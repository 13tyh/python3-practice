from exercises.basics_repetition.round_38 import first_char, hello, lower_text, text_length, upper_text


def test_round_38() -> None:
    assert hello("Aki") == "Hello, Aki"
    assert upper_text("abc") == "ABC"
    assert lower_text("ABC") == "abc"
    assert text_length("python") == 6
    assert first_char("abc") == "a"
    assert first_char("") is None

