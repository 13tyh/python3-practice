from pathlib import Path

from exercises.docs_pdf.pdf_export import build_output_paths, chunk_to_text
from exercises.docs_pdf.split_docs import DocChunk


def test_chunk_to_text() -> None:
    assert chunk_to_text(DocChunk("Title", "Body")) == "Title\n\nBody"


def test_build_output_paths(tmp_path: Path) -> None:
    paths = build_output_paths(tmp_path, [DocChunk("A/B", "x"), DocChunk("C", "y")])
    assert paths == [tmp_path / "01_A_B.pdf", tmp_path / "02_C.pdf"]

