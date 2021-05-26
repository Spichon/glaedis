from typing import Optional, List

from app.models import Crypto_asset
from app.schemas import CryptoAssetCreate
from app.tests.utils.utils import random_lower_string, random_integer
from sqlalchemy.orm import Session

from app import crud


def create_crypto_assets_from_api_referential(db: Session) -> Optional[List[Crypto_asset]]:
    return crud.crypto_asset.create_assets_from_api_referential(db)


def create_fiat_assets_from_api_referential(db: Session) -> Optional[List[Crypto_asset]]:
    return crud.fiat_asset.create_assets_from_api_referential(db)


def create_random_crypto_asset(db: Session) -> Crypto_asset:
    name = random_lower_string()
    cmc_id = random_integer()
    symbol = random_lower_string()
    slug = random_lower_string()
    cmc_rank = random_integer()
    circulating_supply = random_integer()
    total_supply = random_integer()
    asset_in = CryptoAssetCreate(name=name,
                                 cmc_id=cmc_id,
                                 symbol=symbol,
                                 slug=slug,
                                 cmc_rank=cmc_rank,
                                 circulating_supply=circulating_supply,
                                 total_supply=total_supply)
    return crud.crypto_asset.create(db=db, obj_in=asset_in)
