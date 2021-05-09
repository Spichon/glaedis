from pydantic import BaseModel
from typing import List, Optional
from app.schemas.assets_broker import AssetBroker


class AssetBrokerPairBase(BaseModel):
    pass


# Properties to receive on item creation
class AssetBrokerPairCreate(AssetBrokerPairBase):
    symbol: str
    active: bool


# Properties to receive on item update
class AssetBrokerPairUpdate(AssetBrokerPairBase):
    pass


# Properties shared by models stored in DB
class AssetBrokerPairInDBBase(AssetBrokerPairBase):
    id: int
    symbol: str
    active: bool
    base: AssetBroker
    quote: AssetBroker

    class Config:
        orm_mode = True

    pass


# Properties to return to client
class AssetBrokerPair(AssetBrokerPairInDBBase):
    pass


# Properties properties stored in DB
class AssetBrokerPairInDB(AssetBrokerPairInDBBase):
    pass
