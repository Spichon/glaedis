from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Account])
def read_accounts(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
        current_user: schemas.User = Depends(deps.get_current_user),
) -> Any:
    """
    Retrieve accounts.
    """
    accounts = crud.account.get_multi_by_owner(
        db=db, owner_id=current_user["id"], skip=skip, limit=limit
    )
    return accounts


@router.post("/", response_model=schemas.Account)
def create_account(
        *,
        db: Session = Depends(deps.get_db),
        account_in: schemas.AccountCreate,
        current_user: schemas.User = Depends(deps.get_current_user),
) -> Any:
    """
    Create new account.
    """
    account = crud.account.create_with_owner(db=db, obj_in=account_in, owner_id=current_user["id"])
    return account


@router.put("/{id}", response_model=schemas.Account)
def update_account(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        account_in: schemas.AccountUpdate,
        current_user: schemas.User = Depends(deps.get_current_user),
) -> Any:
    """
    Update an account.
    """
    account = crud.account.get(db=db, id=id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    if account.owner_id != current_user["id"]:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    account = crud.account.update(db=db, db_obj=account, obj_in=account_in)
    return account


@router.get("/{id}", response_model=schemas.Account)
def read_account(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        current_user: schemas.User = Depends(deps.get_current_user),
) -> Any:
    """
    Get account by ID.
    """
    account = crud.account.get(db=db, id=id)
    if account.owner_id != current_user["id"]:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return account


@router.get("/{id}/available_percentage", response_model=int)
def available_percentage(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        current_user: schemas.User = Depends(deps.get_current_user),
) -> Any:
    """
    Get account by ID.
    """
    account = crud.account.get(db=db, id=id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    if not crud.user.is_superuser(current_user) and (account.owner_id != current_user["id"]):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return crud.account.get_available_percentage(db=db, account_id=account.id)


@router.delete("/{id}", response_model=schemas.Account)
def delete_account(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        current_user: schemas.User = Depends(deps.get_current_user),
) -> Any:
    """
    Delete an account.
    """
    account = crud.account.get(db=db, id=id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    if account.owner_id != current_user["id"]:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    account = crud.account.remove(db=db, id=id)
    return account
