from fastapi import APIRouter

from app.api.api_v1.endpoints import users
from app.api.api_v1.endpoints import accounts
from app.api.api_v1.endpoints import brokers
from app.api.api_v1.endpoints import portfolios
from app.api.api_v1.endpoints import optimizers
from app.api.api_v1.endpoints import runs
from app.api.api_v1.endpoints import transactions

router = APIRouter()
router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(accounts.router, prefix="/accounts", tags=["accounts"])
router.include_router(brokers.router, prefix="/brokers", tags=["brokers"])
router.include_router(portfolios.router, prefix="/portfolios", tags=["portfolios"])
router.include_router(optimizers.router, prefix="/optimizers", tags=["optimizers"])
router.include_router(runs.router, prefix="/runs", tags=["runs"])
router.include_router(transactions.router, prefix="/transactions", tags=["transactions"])
