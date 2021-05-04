from pydantic import BaseModel
from typing import Optional
from app.schemas.broker import Broker


class AccountBase(BaseModel):
    name: Optional[str] = None

# Properties to receive on item creation
class AccountCreate(AccountBase):
    broker_id: int
    api_key: str
    secret_key: str


# Properties to receive on item update
class AccountUpdate(AccountBase):
    api_key: str
    secret_key: str


# Properties shared by models stored in DB
class AccountInDBBase(AccountBase):
    id: int
    name: Optional[str] = None
    private_status: Optional[bool] = None
    public_status: Optional[bool] = None

    class Config:
        orm_mode = True


# Properties to return to client
class Account(AccountInDBBase):
    owner_id: str
    broker: Broker
    pass


# Properties properties stored in DB
class AccountInDB(AccountInDBBase):
    api_key: str
    hashed_secret_key: str
