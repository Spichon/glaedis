from typing import Any, List

# from app.schemas.assets_broker import AssetBroker
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

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


# @router.get("/{id}/available_assets", response_model=schemas.AssociationList)
# def available_assets(
#         *,
#         db: Session = Depends(deps.get_db),
#         id: int,
#         current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Get account by ID.
#     """
#     broker = crud.broker.get(db=db, id=id)
#     return broker.assets
#
#
# @router.get("/{id}/quote_assets", response_model=List[AssetBroker])
# def quote_assets(
#         *,
#         db: Session = Depends(deps.get_db),
#         id: int,
#         current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Get account by ID.
#     """
#     return crud.broker.get_quote_assets(db=db, id=id)
#
#
# # id is not the broker but the asset_broker
# @router.get("/{id}/tradable_asset_pairs", response_model=List[schemas.AssetBrokerPair])
# def tradable_asset_pairs(
#         *,
#         db: Session = Depends(deps.get_db),
#         id: int,
#         current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Get account by ID.
#     """
#     return crud.broker.get_tradable_asset_pairs(db=db, id=id)
