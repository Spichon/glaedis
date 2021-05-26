from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class UserBase(BaseModel):
    id: Optional[str] = None


class UserInDBBase(UserBase):
    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass
