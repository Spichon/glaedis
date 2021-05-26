from pydantic import BaseModel
from typing import Optional, List


class AssetBase(BaseModel):
    name: Optional[str] = None
    slug: Optional[str] = None
    type: Optional[str] = None
    symbol: Optional[str] = None


# Properties to receive on item creation
class AssetCreate(AssetBase):
    name: str
    slug: str
    symbol: str


# Properties to receive on item update
class AssetUpdate(AssetBase):
    pass


# Properties shared by models stored in DB
class AssetInDBBase(AssetBase):
    name: str
    id: int
    type: str
    slug: str
    symbol: str
    cmc_rank: Optional[int] = None
    cmc_id: Optional[int] = None
    sign: Optional[str] = None

    class Config:
        orm_mode = True


# Properties to return to client
class Asset(AssetInDBBase):
    pass


# Properties properties stored in DB
class AssetInDB(AssetInDBBase):
    pass
