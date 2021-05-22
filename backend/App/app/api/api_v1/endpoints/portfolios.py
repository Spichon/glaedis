from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Portfolio])
def read_portfolios(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
        current_user: schemas.User = Depends(deps.get_current_user),
) -> Any:
    """
    Retrieve portfolios.
    """
    portfolios = crud.portfolio.get_multi_by_owner(
        db=db, owner_id=current_user["id"], skip=skip, limit=limit
    )
    return portfolios


@router.post("/", response_model=schemas.Portfolio)
def create_portfolio(
        *,
        db: Session = Depends(deps.get_db),
        portfolio_in: schemas.PortfolioCreate,
        current_user: schemas.User = Depends(deps.get_current_user),
) -> Any:
    """
    Create new portfolio.
    """
    account = crud.account.get(db=db, id=portfolio_in.account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    if account.owner_id != current_user["id"]:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    portfolio = crud.portfolio.create(db=db, obj_in=portfolio_in)
    return portfolio


@router.get("/{id}", response_model=schemas.Portfolio)
def read_portfolio(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        current_user: schemas.User = Depends(deps.get_current_user),
) -> Any:
    """
    Get portfolio by ID.
    """
    portfolio = crud.portfolio.get(db=db, id=id)
    if not portfolio:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    if portfolio.account.owner_id != current_user["id"]:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return portfolio


@router.get("/{id}/get_assets_last_values", response_model=List[dict])
def get_assets_last_values(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        current_user: schemas.User = Depends(deps.get_current_user),
) -> Any:
    """
    Get last values of assets in portfolios
    """
    portfolio = crud.portfolio.get(db=db, id=id)
    if not portfolio:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    if portfolio.account.owner_id != current_user["id"]:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    assets_last_values = crud.portfolio.get_assets_last_values(db_obj=portfolio)
    return assets_last_values


@router.put("/{id}", response_model=schemas.Portfolio)
def update_portfolio(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        portfolio_in: schemas.PortfolioUpdate,
        current_user: schemas.User = Depends(deps.get_current_user),
) -> Any:
    """
    Update an portfolio.
    """
    portfolio = crud.portfolio.get(db=db, id=id)
    if not portfolio:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    if portfolio.account.owner_id != current_user["id"]:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    portfolio = crud.portfolio.update(db=db, db_obj=portfolio, obj_in=portfolio_in)
    return portfolio


@router.delete("/{id}", response_model=schemas.Portfolio)
def delete_portfolio(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        current_user: schemas.User = Depends(deps.get_current_user),
) -> Any:
    """
    Delete an portfolio.
    """
    portfolio = crud.portfolio.get(db=db, id=id)
    if not portfolio:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    if portfolio.account.owner_id != current_user["id"]:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    portfolio = crud.portfolio.remove(db=db, id=id)
    return portfolio


# @router.get("/{id}/start_automation", response_model=schemas.Portfolio)
# def start_automation(
#         *,
#         db: Session = Depends(deps.get_db),
#         id: int,
#         current_user: schemas.User = Depends(deps.get_current_user),
# ) -> Any:
#     """
#     Test Celery worker.
#     """
#     portfolio = crud.portfolio.get(db=db, id=id)
#     if not portfolio:
#         raise HTTPException(status_code=404, detail="Portfolio not found")
#     if not crud.user.is_superuser(current_user) and (portfolio.account.owner_id != current_user["id"]):
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     portfolio = crud.portfolio_automation_task.start_automation(db=db, db_obj=portfolio)
#     return portfolio
#
#
# @router.get("/{id}/pause_automation", response_model=schemas.Portfolio)
# def pause_automation(
#         *,
#         db: Session = Depends(deps.get_db),
#         id: int,
#         current_user: schemas.User = Depends(deps.get_current_user),
# ) -> Any:
#     """
#     Test Celery worker.
#     """
#     portfolio = crud.portfolio.get(db=db, id=id)
#     if not portfolio:
#         raise HTTPException(status_code=404, detail="Portfolio not found")
#     if not crud.user.is_superuser(current_user) and (portfolio.account.owner_id != current_user["id"]):
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     portfolio = crud.portfolio_automation_task.pause_automation(db=db, db_obj=portfolio)
#     return portfolio
#
#
# @router.get("/{id}/delete_automation", response_model=schemas.Portfolio)
# def delete_automation(
#         *,
#         db: Session = Depends(deps.get_db),
#         id: int,
#         current_user: schemas.User = Depends(deps.get_current_user),
# ) -> Any:
#     """
#     Test Celery worker.
#     """
#     portfolio = crud.portfolio.get(db=db, id=id)
#     if not portfolio:
#         raise HTTPException(status_code=404, detail="Portfolio not found")
#     if not crud.user.is_superuser(current_user) and (portfolio.account.owner_id != current_user["id"]):
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     portfolio = crud.portfolio_automation_task.delete_automation(db=db, db_obj=portfolio)
#     return portfolio


@router.get("/{id}/get_quote_asset_balance", response_model=float)
def get_quote_asset_balance(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        current_user: schemas.User = Depends(deps.get_current_user),
) -> Any:
    """
    Get quote asset balance
    """
    portfolio = crud.portfolio.get(db=db, id=id)
    if not portfolio:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    if portfolio.account.owner_id != current_user["id"]:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    asset_balance = crud.portfolio.get_asset_balance(db_obj=portfolio)
    return asset_balance
