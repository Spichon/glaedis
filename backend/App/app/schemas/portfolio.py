from pydantic import BaseModel
from typing import Optional, List
from app.schemas.account import Account
from sqlalchemy.ext.associationproxy import _AssociationList
from app.schemas.assets_broker import AssetBroker
from app.schemas.asset_broker_pair import AssetBrokerPair
from app.schemas import Optimizer

# from app.schemas.periodic_task import PeriodicTask


class PortfolioBase(BaseModel):
    name: Optional[str] = None
    quote_asset_id: Optional[int] = None
    ticker: Optional[str] = None
    optimizer_id: Optional[str] = None
    risk_free: Optional[int] = None


# Properties to receive on item creation
class PortfolioCreate(PortfolioBase):
    name: str
    account_id: int
    quote_asset_id: int
    optimizer_id: int
    asset_broker_pairs: Optional[List[AssetBrokerPair]] = []
    ticker: str


# Properties to receive on item update
class PortfolioUpdate(PortfolioBase):
    asset_broker_pairs: Optional[List[AssetBrokerPair]] = []
    pass


# Properties shared by models stored in DB
class PortfolioInDBBase(PortfolioBase):
    id: int
    name: Optional[str] = None
    ticker: str
    optimizer: Optional[Optimizer] = None
    risk_free: Optional[int] = None
    quote_asset_balance: Optional[float] = 0

    class Config:
        orm_mode = True


# Properties to return to client
class Portfolio(PortfolioInDBBase):
    account: Account
    quote_asset: AssetBroker
    # assets: Optional[AssociationList] = []


# Properties properties stored in DB
class PortfolioInDB(PortfolioInDBBase):
    pass
