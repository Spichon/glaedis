from fastapi import APIRouter

from app.api.api_v1.endpoints import users
from app.api.api_v1.endpoints import accounts
from app.api.api_v1.endpoints import brokers
from app.api.api_v1.endpoints import portfolios

router = APIRouter()
router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(accounts.router, prefix="/accounts", tags=["accounts"])
router.include_router(brokers.router, prefix="/brokers", tags=["brokers"])
router.include_router(portfolios.router, prefix="/portfolios", tags=["portfolios"])
