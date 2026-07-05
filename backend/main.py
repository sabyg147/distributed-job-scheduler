from fastapi import FastAPI

from app.auth.routes import router as auth_router
from app.config.settings import settings
from app.organization.routes import router as organization_router
from app.project.routes import router as project_router
from app.queue.routes import router as queue_router

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
)

app.include_router(auth_router)
app.include_router(organization_router)
app.include_router(project_router)
app.include_router(queue_router)


@app.get("/")
async def root():
    return {
        "message": f"Welcome to {settings.app_name}"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "environment": settings.app_env,
        "version": settings.app_version,
    }