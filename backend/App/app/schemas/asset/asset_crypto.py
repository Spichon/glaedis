from app.schemas.asset.asset import AssetBase, AssetCreate, AssetUpdate, AssetInDBBase
from typing import Optional


# Properties to receive on item creation
class CryptoAssetBase(AssetBase):
    cmc_rank: Optional[int] = None
    cmc_id: Optional[int] = None
    circulating_supply: Optional[float] = None
    total_supply: Optional[float] = None


# Properties to receive on item creation
class CryptoAssetCreate(CryptoAssetBase, AssetCreate):
    cmc_rank: int
    cmc_id: int


# Properties to receive on item update
class CryptoAssetUpdate(CryptoAssetBase, AssetUpdate):
    pass


# Properties shared by models stored in DB
class CryptoAssetInDBBase(AssetInDBBase, CryptoAssetBase):
    cmc_rank: int
    cmc_id: int
    circulating_supply: Optional[float]
    total_supply: Optional[float]

    class Config:
        orm_mode = True


# Properties to return to client
class CryptoAsset(CryptoAssetInDBBase):
    pass


# Properties properties stored in DB
class CryptoAssetInDB(CryptoAssetInDBBase):
    pass
