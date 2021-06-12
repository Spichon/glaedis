from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.transaction import Transaction
from app.models.run import Run
from app.schemas.transaction import TransactionCreate, TransactionUpdate
from typing import List


class CRUDTransaction(CRUDBase[Transaction, TransactionCreate, TransactionUpdate]):
    def get_multi_by_portfolio(self, db: Session, id: int, skip: int = 0, limit: int = 100) -> List[Transaction]:
        return db.query(Transaction).join(Run).filter(Run.portfolio_id == id, Transaction.run_id == Run.id).offset(skip).limit(limit).all()


transaction = CRUDTransaction(Transaction)
