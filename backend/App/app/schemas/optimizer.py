from pydantic import BaseModel
from typing import Optional


class OptimizerBase(BaseModel):
    name: Optional[str] = None


# Properties to receive on item creation
class OptimizerCreate(OptimizerBase):
    name: str


# Properties to receive on item update
class OptimizerUpdate(OptimizerBase):
    pass


# Properties shared by models stored in DB
class OptimizerInDBBase(OptimizerBase):
    name: str
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Optimizer(OptimizerInDBBase):
    pass


# Properties properties stored in DB
class OptimizerInDB(OptimizerInDBBase):
    pass
