from typing import List, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session, with_polymorphic

from app.crud.base import CRUDBase
from app.schemas.asset.asset_crypto import CryptoAssetCreate, CryptoAssetUpdate
from app.models.asset.crypto_asset import Crypto_asset
from app.core.config import settings
from coinmarketcapapi import CoinMarketCapAPI
from sqlalchemy import or_

class CRUDAsset(CRUDBase[Crypto_asset, CryptoAssetCreate, CryptoAssetUpdate]):
    def create(self, db: Session, obj_in: CryptoAssetCreate) -> Optional[Crypto_asset]:
        obj_in.type = self.model.__mapper_args__['polymorphic_identity']
        return super().create(db=db, obj_in=obj_in)

    def create_assets_from_api_referential(self, db: Session) -> Optional[List[Crypto_asset]]:
        try:
            cmc = CoinMarketCapAPI(settings.COIN_MARKET_CAP_API_KEY)
            index = 1
            limit = 5000
            list_result = []
            iterate = True
            while iterate:
                payload = cmc.cryptocurrency_listings_latest(start=index, limit=limit).data
                if len(payload) == 0:
                    iterate = False
                else:
                    list_result = list_result + payload
                    index = index + limit
            for result in list_result:
                result['slug'] = result['name'].replace(" ", "_").lower()
                result['cmc_id'] = result["id"]
                asset_in = CryptoAssetCreate(**result)
                instance = db.query(self.model).filter(or_(Crypto_asset.slug==asset_in.slug, Crypto_asset.cmc_id==asset_in.cmc_id)).first()
                if instance:
                    pass
                else:
                    instance = self.create(db=db, obj_in=asset_in)
                    db.add(instance)
                    db.commit()
            return self.get_multi(db=db, skip=0, limit=100)
        except Exception as e:
            print(e)
            return []


crypto_asset = CRUDAsset(Crypto_asset)
