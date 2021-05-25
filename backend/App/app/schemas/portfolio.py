from pydantic import BaseModel
from typing import Optional, List
from app.schemas.account import Account
from sqlalchemy.ext.associationproxy import _AssociationList
from app.schemas.assets_broker import AssetBroker
from app.schemas.asset_broker_pair import AssetBrokerPair
# from app.schemas.periodic_task import PeriodicTask


class AssociationList(_AssociationList):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v) -> List:
        if not isinstance(v, _AssociationList):
            raise TypeError("AssociationList required")
        return [AssetBrokerPair.from_orm(u) for u in v]

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(
            pattern="[{}]",
            examples="[{}] [{'name':'BTC'}]",
        )


class PortfolioBase(BaseModel):
    name: Optional[str] = None
    # percentage: Optional[str] = None
    quote_asset_id: Optional[int] = None
    ticker: Optional[str] = None


# Properties to receive on item creation
class PortfolioCreate(PortfolioBase):
    name: str
    # percentage: int
    account_id: int
    quote_asset_id: int
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
    # percentage: Optional[int] = None
    ticker: str
    # automation_task: Optional[PeriodicTask] = None

    class Config:
        orm_mode = True


# Properties to return to client
class Portfolio(PortfolioInDBBase):
    account: Account
    quote_asset: AssetBroker
    assets: Optional[AssociationList] = []


# Properties properties stored in DB
class PortfolioInDB(PortfolioInDBBase):
    pass
