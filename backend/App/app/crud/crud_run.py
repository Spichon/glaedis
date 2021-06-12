from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.run import Run
from app.schemas.run import RunCreate, RunUpdate
from typing import List


class CRUDRun(CRUDBase[Run, RunCreate, RunUpdate]):
    def get_multi_by_portfolio(self, db: Session, id: int, skip: int = 0, limit: int = 100) -> List[Run]:
        return db.query(Run).filter(Run.portfolio_id == id).offset(skip).limit(limit).all()


run = CRUDRun(Run)
