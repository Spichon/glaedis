from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()


@router.get("/{id}", response_model=List[schemas.Transaction])
def read_transactions_by_portfolio_id(
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
    transactions = crud.transaction.get_multi_by_portfolio(db, id, skip=skip, limit=limit)
    return transactions


@router.post("/{id}", response_model=schemas.Transaction)
def create_transaction(
        *,
        db: Session = Depends(deps.get_db),
        transaction_in: schemas.TransactionCreate,
        current_user: schemas.User = Depends(deps.get_current_user),
) -> Any:
    """
    Create a transaction.
    """
    transaction = crud.transaction.create(db=db, obj_in=transaction_in)
    return transaction

@router.put("/{id}", response_model=schemas.Transaction)
def update_run(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        transaction_in: schemas.TransactionUpdate,
        current_user: schemas.User = Depends(deps.get_current_user),
) -> Any:
    """
    Update an transaction.
    """
    transaction = crud.transaction.get(db=db, id=id)
    transaction = crud.transaction.update(db=db, db_obj=transaction, obj_in=transaction_in)
    return transaction
