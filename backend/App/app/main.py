from fastapi import FastAPI, Depends
from mangum import Mangum

from app.api.api_v1.api import router as api_router
from app.core.config import settings
from app.core.auth import auth
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    title=settings.PROJECT_NAME,
    # if not custom domain
    # openapi_prefix="/prod"
)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


app.include_router(api_router, prefix=settings.API_V1_STR, dependencies=[Depends(auth)])


@app.get("/test")
def pong():
    """
    Sanity check.

    This will let the user know that the service is operational.

    And this path operation will:
    * show a lifesign

    """
    return "ok"


handler = Mangum(app)
