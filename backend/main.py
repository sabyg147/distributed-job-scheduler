from fastapi import FastAPI

from app.config.settings import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
)


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