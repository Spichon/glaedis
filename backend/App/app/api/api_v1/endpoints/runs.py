from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()


@router.get("/{id}", response_model=List[schemas.Run])
def read_runs_by_portfolio_id(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        skip: int = 0,
        limit: int = 100,
        current_user: schemas.User = Depends(deps.get_current_user)
) -> Any:
    """
    Retrieve runs for a given portfolio.
    """
    portfolio = crud.portfolio.get(db=db, id=id)
    if not portfolio:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    if portfolio.account.owner_id != current_user["id"]:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    runs = crud.run.get_multi_by_portfolio(db, id, skip=skip, limit=limit)
    return runs
