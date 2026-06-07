"""FastAPI + AI app entrypoint."""

from __future__ import annotations

from fastapi import FastAPI

from .router import create_router
from .service import FakeTextGenerator


def create_app() -> FastAPI:
    app = FastAPI(title="Python Master AI API")
    app.include_router(create_router(FakeTextGenerator()))
    return app


app = create_app()
