from fastapi import FastAPI

from app.api.routes import health
from app.core.config import settings


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="AI Interview & Career Copilot backend",
)


app.include_router(
    health.router,
    prefix="/api/v1",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to InterviewIQ API",
        "version": settings.app_version,
    }