from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas import User

router = APIRouter()


@router.get("/me", response_model=User)
def read_user_me(
        db: Session = Depends(deps.get_db),
        current_user: User = Depends(deps.get_current_user),
) -> Any:
    """
    Get current user.
    """
    print(db)
    return current_user

@router.get("/test", response_model=User)
def test() -> Any:
    """
    Get current user.
    """
    return 'ok'
