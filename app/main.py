"""FastAPI application entrypoint."""

from fastapi import FastAPI

from app.core.config import settings
from app.presentation.api.v1 import api_router

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
)

app.include_router(api_router, prefix=settings.API_V1_PREFIX)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
