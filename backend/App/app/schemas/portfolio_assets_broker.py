from typing import List, Optional
from app.schemas.asset_broker_pair import AssetBrokerPair
from pydantic import BaseModel
from sqlalchemy.ext.associationproxy import _AssociationList


class PortfolioAssetBrokerBase(BaseModel):
    pass


# Properties to receive on item creation
class PortfolioAssetBrokerCreate(PortfolioAssetBrokerBase):
    pass


# Properties shared by models stored in DB
class PortfolioAssetBrokerInDBBase(PortfolioAssetBrokerBase):
    asset_broker_pair: AssetBrokerPair
    qty: float = 0
    current_price: float = 0
    opening_price: float = 0

    class Config:
        orm_mode = True


# Properties to return to client
class PortfolioAssetBroker(PortfolioAssetBrokerInDBBase):
    pass


# Properties properties stored in DB
class PortfolioAssetBrokerInDB(PortfolioAssetBrokerInDBBase):
    pass
