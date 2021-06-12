from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.Optimizer])
def read_optimizers(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100
) -> Any:
    """
    Retrieve optimizers.
    """
    optimizers = crud.optimizer.get_multi(db, skip=skip, limit=limit)
    return optimizers
