from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import text

from app.api.routes import health
from app.core.config import settings
from app.db.base import Base
from app.db.database import engine

# Import models so SQLAlchemy registers all tables.
from app import models


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create database tables during development.
    Base.metadata.create_all(bind=engine)

    yield

    # Nothing to clean up here yet.


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="AI Interview & Career Copilot backend",
    lifespan=lifespan,
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


@app.get("/api/v1/database/health")
def database_health():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    return {
        "status": "healthy",
        "database": "PostgreSQL",
    }