from typing import Optional
import pydantic
from pydantic import BaseModel
from app.schemas import Run
from enum import Enum
from datetime import datetime
from app.schemas.asset_broker_pair import AssetBrokerPair


# from app.schemas.periodic_task import PeriodicTask

class TransactionEnum(str, Enum):
    buy = "buy"
    sell = "sell"


class TransactionBase(BaseModel):
    date: datetime = datetime.utcnow()


# Properties to receive on item creation
class TransactionCreate(TransactionBase):
    asset_broker_pair_id: int
    run_id: int
    order_id: str
    qty: Optional[float] = 0
    price: Optional[float] = 0
    side: TransactionEnum

# Properties to receive on item update
class TransactionUpdate(TransactionBase):
    price: Optional[float] = 0


# Properties shared by models stored in DB
class TransactionInDBBase(TransactionBase):
    id: int
    order_id: str
    date: datetime
    price: float
    qty: float

    class Config:
        orm_mode = True


# Properties to return to client
class Transaction(TransactionInDBBase):
    side: TransactionEnum

    @pydantic.validator('side', pre=True)
    def validate_enum_field(cls, side: str):
        return TransactionEnum(side.name)

    asset_broker_pair: AssetBrokerPair
    run: Run


# Properties properties stored in DB
class TransactionInDB(TransactionInDBBase):
    pass
