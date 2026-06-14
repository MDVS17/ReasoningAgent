"""FastAPI entrypoint for the cinematic Syntrix demo."""

from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from backend.api.routes_analysis import router as analysis_router
from backend.api.routes_blueprint import router as blueprint_router
from backend.api.routes_health import router as health_router
from backend.api.routes_iq import router as iq_router

BASE_DIR = Path(__file__).resolve().parents[1]
FRONTEND_DIR = BASE_DIR / "frontend"

app = FastAPI(
    title="Syntrix — Copilot Agent Architect API",
    description="AI Agent Factory API for turning Microsoft 365-style synthetic work patterns into review-ready Copilot Agent Blueprints.",
    version="0.2.0",
)

app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

app.include_router(health_router)
app.include_router(analysis_router)
app.include_router(blueprint_router)
app.include_router(iq_router)


@app.get("/", include_in_schema=False)
def index() -> FileResponse:
    return FileResponse(FRONTEND_DIR / "index.html")
