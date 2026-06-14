from exercises.docs_pdf.split_docs import (
    DocChunk,
    safe_filename,
    split_markdown_by_heading,
    split_text_by_chars,
)


def test_split_markdown_by_heading() -> None:
    text = "# One\nbody1\n# Two\nbody2"
    assert split_markdown_by_heading(text) == [
        DocChunk("One", "body1"),
        DocChunk("Two", "body2"),
    ]


def test_split_text_by_chars() -> None:
    assert split_text_by_chars("abcdef", 2) == ["ab", "cd", "ef"]


def test_safe_filename() -> None:
    assert safe_filename("A/B:C*D?") == "A_B_C_D_"
