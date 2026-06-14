from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
_STEPS = _ROOT / "steps"

__path__ = [
    str(path) for path in sorted(_STEPS.glob("*/implementation/exercises")) if path.is_dir()
]
