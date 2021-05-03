from fastapi import FastAPI, Depends
from mangum import Mangum

from app.api.api_v1.api import router as api_router
from app.core.config import settings
from app.core.auth import auth

app = FastAPI(
    title=settings.PROJECT_NAME,
    # if not custom domain
    # openapi_prefix="/prod"
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
