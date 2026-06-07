"""FastAPI app entrypoint."""

from __future__ import annotations

from fastapi import FastAPI

from .router import create_router
from .service import create_store


def create_app() -> FastAPI:
    app = FastAPI(title="Python Master API")
    store = create_store()
    app.include_router(create_router(store))
    return app


app = create_app()
