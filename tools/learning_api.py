from __future__ import annotations

import json
import shlex
import subprocess
import time
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

WORKSPACE = Path("/workspace")
MAX_OUTPUT = 12_000
MAX_FILE_PREVIEW = 16_000
TIMEOUT_SECONDS = 90

ALLOWED_EXACT = {
    "python --version",
    "ruff check .",
    "black --check .",
    "mypy src",
    "uv run lint",
    "uv run fmt",
    "uv run fmt --fix",
    "uv run build",
}


class RunRequest(BaseModel):
    command: str = Field(min_length=1, max_length=300)


class RunResponse(BaseModel):
    command: str
    exit_code: int
    duration_ms: int
    stdout: str
    stderr: str


class StepReference(BaseModel):
    step: str
    comment: str
    urls: list[str]


class FileCompare(BaseModel):
    exercise_path: str
    solution_path: str
    exercise: str
    solution: str
    has_solution: bool


app = FastAPI(title="Python Master Learning API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/step-references", response_model=list[StepReference])
def step_references() -> list[StepReference]:
    json_path = WORKSPACE / "docs" / "step_references.json"
    if json_path.exists():
        return [
            StepReference.model_validate(item)
            for item in json.loads(json_path.read_text(encoding="utf-8"))
        ]
    path = WORKSPACE / "docs" / "STEP_REFERENCES.md"
    if not path.exists():
        raise HTTPException(status_code=404, detail="STEP_REFERENCES.md が見つかりません")
    return _parse_step_references(path.read_text(encoding="utf-8"))


@app.get("/api/solution-compare", response_model=FileCompare)
def solution_compare(exercise_path: str) -> FileCompare:
    exercise_file = _safe_workspace_path(exercise_path)
    solution_path = _solution_path_for(exercise_path)
    solution_file = _safe_workspace_path(solution_path)
    if not exercise_file.exists():
        raise HTTPException(status_code=404, detail="対象ファイルが見つかりません")
    return FileCompare(
        exercise_path=exercise_path,
        solution_path=solution_path,
        exercise=_read_preview(exercise_file),
        solution=_read_preview(solution_file) if solution_file.exists() else "",
        has_solution=solution_file.exists(),
    )


@app.post("/api/run", response_model=RunResponse)
def run_command(request: RunRequest) -> RunResponse:
    command = request.command.strip()
    if not _is_allowed(command):
        raise HTTPException(status_code=400, detail="このコマンドはUIから実行できません")

    args = shlex.split(command)
    started = time.perf_counter()
    try:
        completed = subprocess.run(
            args,
            cwd=WORKSPACE,
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        duration_ms = int((time.perf_counter() - started) * 1000)
        return RunResponse(
            command=command,
            exit_code=124,
            duration_ms=duration_ms,
            stdout=_trim(exc.stdout or ""),
            stderr=_trim((exc.stderr or "") + "\nTimeout: 90秒を超えました"),
        )

    duration_ms = int((time.perf_counter() - started) * 1000)
    return RunResponse(
        command=command,
        exit_code=completed.returncode,
        duration_ms=duration_ms,
        stdout=_trim(completed.stdout),
        stderr=_trim(completed.stderr),
    )


def _is_allowed(command: str) -> bool:
    if command in ALLOWED_EXACT:
        return True
    if command.startswith("pytest "):
        return _does_not_use_shell_features(command)
    if command.startswith("uv run pytest "):
        return _does_not_use_shell_features(command)
    return False


def _does_not_use_shell_features(command: str) -> bool:
    blocked = [";", "&&", "||", "|", ">", "<", "$(", "`"]
    return not any(token in command for token in blocked)


def _trim(value: str) -> str:
    if len(value) <= MAX_OUTPUT:
        return value
    return value[:MAX_OUTPUT] + "\n... output truncated ..."


def _safe_workspace_path(value: str) -> Path:
    if Path(value).is_absolute():
        raise HTTPException(status_code=400, detail="絶対パスは指定できません")
    normalized = Path(value)
    if ".." in normalized.parts:
        raise HTTPException(status_code=400, detail="親ディレクトリ参照は指定できません")
    if normalized.parts[:1] not in {
        ("tests",),
        ("steps",),
        ("src",),
        ("review_tasks",),
        ("failure_patterns",),
    }:
        raise HTTPException(status_code=400, detail="このパスはプレビューできません")
    path = (WORKSPACE / normalized).resolve()
    if not path.is_relative_to(WORKSPACE.resolve()):
        raise HTTPException(status_code=400, detail="workspace外は読めません")
    return path


def _solution_path_for(exercise_path: str) -> str:
    marker = "/implementation/exercises/"
    if exercise_path.startswith("steps/") and marker in exercise_path:
        step_prefix, relative_path = exercise_path.split(marker, 1)
        return f"{step_prefix}/solutions/{relative_path}"
    return "solutions/" + Path(exercise_path).name


def _read_preview(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    if len(text) <= MAX_FILE_PREVIEW:
        return text
    return text[:MAX_FILE_PREVIEW] + "\n... file truncated ..."


def _parse_step_references(text: str) -> list[StepReference]:
    references: list[StepReference] = []
    for line in text.splitlines():
        if not line.startswith("| `"):
            continue
        columns = [column.strip() for column in line.strip("|").split("|")]
        if len(columns) != 3:
            continue
        step = columns[0].strip("`")
        urls = [url.strip() for url in columns[2].split(" / ") if url.strip()]
        references.append(StepReference(step=step, comment=columns[1], urls=urls))
    return references
