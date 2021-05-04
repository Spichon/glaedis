from pydantic import BaseModel
from typing import Optional


class BrokerBase(BaseModel):
    name: Optional[str] = None
    logo: Optional[str] = None
    broker_id: Optional[str] = None


# Properties to receive on item creation
class BrokerCreate(BrokerBase):
    name: str
    logo: Optional[str] = None
    broker_id: str


# Properties to receive on item update
class BrokerUpdate(BrokerBase):
    pass


# Properties shared by models stored in DB
class BrokerInDBBase(BrokerBase):
    id: int
    name: str
    logo: str
    broker_id: str

    class Config:
        orm_mode = True


# Properties to return to client
class Broker(BrokerInDBBase):
    pass


# Properties properties stored in DB
class BrokerInDB(BrokerInDBBase):
    pass
