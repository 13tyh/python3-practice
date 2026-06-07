from pathlib import Path


def load_prompt(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def render_prompt(template: str, values: dict[str, str]) -> str:
    return template.format(**values)
