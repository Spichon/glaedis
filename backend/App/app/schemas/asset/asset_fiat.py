from app.schemas.asset.asset import AssetBase, AssetCreate, AssetUpdate, AssetInDBBase
from typing import Optional


# Properties to receive on item creation
class FiatAssetBase(AssetBase):
    sign: Optional[str] = None
    cmc_id: Optional[int] = None


# Properties to receive on item creation
class FiatAssetCreate(FiatAssetBase, AssetCreate):
    sign: str
    cmc_id: int


# Properties to receive on item update
class FiatAssetUpdate(FiatAssetBase, AssetUpdate):
    pass


# Properties shared by models stored in DB
class FiatAssetInDBBase(AssetInDBBase, FiatAssetBase):
    sign: str
    cmc_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class FiatAsset(FiatAssetInDBBase):
    pass


# Properties properties stored in DB
class FiatAssetInDB(FiatAssetInDBBase):
    pass
