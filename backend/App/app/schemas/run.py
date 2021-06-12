import pydantic
from pydantic import BaseModel, Field
from app.schemas import Optimizer
import datetime
from enum import Enum
from datetime import datetime

# from app.schemas.periodic_task import PeriodicTask

class RunEnum(str, Enum):
    created = "created"
    running = "running"
    achieved = "achieved"
    failed = "failed"


class RunBase(BaseModel):
    date: datetime = datetime.utcnow()
    state: RunEnum


# Properties to receive on item creation
class RunCreate(RunBase):
    optimizer_id: int
    portfolio_id: int


# Properties to receive on item update
class RunUpdate(RunBase):
    pass


# Properties shared by models stored in DB
class RunInDBBase(RunBase):
    id: int
    date: datetime

    class Config:
        orm_mode = True


# Properties to return to client
class Run(RunInDBBase):
    optimizer: Optimizer
    state: RunEnum
    @pydantic.validator('state', pre=True)
    def validate_enum_field(cls, state: str):
        return RunEnum(state.name)

# Properties properties stored in DB
class RunInDB(RunInDBBase):
    pass
