from typing import List, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session, with_polymorphic

from app.crud.base import CRUDBase
from app.models.broker import Broker
from app.schemas.asset.asset import AssetCreate, AssetUpdate
from app.models.asset.base_asset import Asset
from app.models.asset.crypto_asset import Crypto_asset


class CRUDAsset(CRUDBase[Asset, AssetCreate, AssetUpdate]):
    def create(self, db: Session, obj_in: AssetCreate) -> Optional[Asset]:
        obj_in.type = self.model.__mapper_args__['polymorphic_identity']
        return super().create(db=db, obj_in=obj_in)


asset = CRUDAsset(Asset)
