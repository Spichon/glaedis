from typing import List, Optional
from app.schemas.asset.asset import Asset
from app.schemas.broker import Broker
from pydantic import BaseModel
from sqlalchemy.ext.associationproxy import _AssociationList


class AssociationList(_AssociationList):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v) -> List:
        if not isinstance(v, _AssociationList):
            raise TypeError("AssociationList required")
        return [Asset.from_orm(u) for u in v]

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(
            pattern="[{}]",
            examples="[{}] [{'name':'BTC'}]",
        )


class AssetBrokerBase(BaseModel):
    pass


# Properties to receive on item creation
class AssetBrokerCreate(AssetBrokerBase):
    name: Optional[str] = ""


# Properties shared by models stored in DB
class AssetBrokerInDBBase(AssetBrokerBase):
    id: int
    name: Optional[str] = ""
    class Config:
        orm_mode = True


# Properties to return to client
class AssetBroker(AssetBrokerInDBBase):
    asset: Asset
    pass


# Properties properties stored in DB
class AssetBrokerInDB(AssetBrokerInDBBase):
    pass
