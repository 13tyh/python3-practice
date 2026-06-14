import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "frontend" / "src" / "data"


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _ordered_ids() -> list[str]:
    return re.findall(r'"([^"]+)"', _read(DATA_DIR / "stepOrder.ts"))


def _phase_sources() -> list[str]:
    return [_read(path) for path in sorted(DATA_DIR.glob("phase*Steps.ts"))]


def _step_reference_json() -> list[dict[str, object]]:
    return json.loads(_read(ROOT / "docs" / "step_references.json"))


def test_step_order_matches_phase_step_ids() -> None:
    order_ids = _ordered_ids()
    step_ids = [
        match for source in _phase_sources() for match in re.findall(r'id: "([^"]+)"', source)
    ]

    assert step_ids == order_ids
    assert len(step_ids) == len(set(step_ids))


def test_step_referenced_files_exist() -> None:
    missing: list[str] = []
    for source in _phase_sources():
        for files_block in re.findall(r"files:\s*\[([^\]]*)\]", source, re.S):
            for file_path in re.findall(r'"([^"]+)"', files_block):
                if not (ROOT / file_path).exists():
                    missing.append(file_path)

    assert missing == []


def test_step_references_cover_all_steps() -> None:
    refs = _step_reference_json()

    assert [str(item["step"]) for item in refs] == _ordered_ids()
    assert all(str(item["comment"]).strip() for item in refs)
    assert all(item["urls"] for item in refs)


def test_step_reference_markdown_matches_json() -> None:
    markdown_ids = re.findall(r"\| `([^`]+)` \|", _read(ROOT / "docs" / "STEP_REFERENCES.md"))
    json_ids = [str(item["step"]) for item in _step_reference_json()]

    assert set(markdown_ids) == set(json_ids)
    assert len(markdown_ids) == len(json_ids)


def test_no_empty_optional_step_directories() -> None:
    empty_dirs: list[str] = []
    for step_dir in (ROOT / "steps").glob("[0-9][0-9][0-9]_*"):
        for name in ("references", "solutions"):
            optional_dir = step_dir / name
            has_files = any(path.is_file() for path in optional_dir.rglob("*"))
            if optional_dir.exists() and not has_files:
                empty_dirs.append(str(optional_dir.relative_to(ROOT)).replace("\\", "/"))

    assert empty_dirs == []
