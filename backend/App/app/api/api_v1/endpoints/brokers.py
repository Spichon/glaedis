from typing import Any, List, Union, Dict

from app.schemas.assets_broker import AssetBroker
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.models import Asset, Asset_broker, Crypto_asset, Fiat_asset

router = APIRouter()


@router.get("/", response_model=List[schemas.Broker])
def read_brokers(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100
) -> Any:
    """
    Retrieve brokers.
    """
    brokers = crud.broker.get_multi(db, skip=skip, limit=limit)
    return brokers


@router.get("/{id}/available_assets", response_model=List[schemas.Asset])
def available_assets(
        *,
        db: Session = Depends(deps.get_db),
        id: int
) -> Any:
    """
    Get account by ID.
    """
    assets = crud.broker.get_available_assets(db, id=id)
    return assets


@router.get("/{id}/quote_assets", response_model=List[AssetBroker])
def quote_assets(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
) -> Any:
    """
    Get account by ID.
    """
    return crud.broker.get_quote_assets(db=db, id=id)


# id is not the broker but the asset_broker
@router.get("/{id}/tradable_asset_pairs", response_model=List[schemas.AssetBrokerPair])
def tradable_asset_pairs(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
) -> Any:
    """
    Get account by ID.
    """
    return crud.broker.get_tradable_asset_pairs(db=db, id=id)


# id is not the broker but the asset_broker
@router.get("/{id}/get_timeframes", response_model=schemas.Timeframes)
def tradable_asset_pairs(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
) -> Any:
    """
    Get account by ID.
    """
    broker = crud.broker.get(db=db, id=id)
    if not broker:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    timeframes = crud.broker.get_timeframes(db_obj=broker)
    return {"timeframes": timeframes}
