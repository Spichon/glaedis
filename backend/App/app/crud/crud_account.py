from typing import List, Union, Dict, Any, Optional

from app.core.security import encode_secret_key, decode_secret_key
# from app.models import Portfolio
from fastapi.encoders import jsonable_encoder
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.account import Account
from app.schemas.account import AccountCreate, AccountUpdate


class CRUDAccount(CRUDBase[Account, AccountCreate, AccountUpdate]):
    def create_with_owner(
            self, db: Session, *, obj_in: AccountCreate, owner_id: str
    ) -> Optional[Account]:
        if len(obj_in.api_key) < 4 or len(obj_in.secret_key) < 4 or len(obj_in.api_key) % 4 == 1 or len(
                obj_in.secret_key) % 4 == 1:
            return None
        db_obj = Account(
            broker_id=obj_in.broker_id,
            name=obj_in.name,
            api_key=obj_in.api_key,
            hashed_secret_key=encode_secret_key(obj_in.secret_key),
            owner_id=owner_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
            self, db: Session, *, db_obj: Account, obj_in: Union[AccountUpdate, Dict[str, Any]]
    ) -> Optional[Account]:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if len(update_data["secret_key"]) < 4 or len(update_data["secret_key"]) < 4 or len(
                update_data["secret_key"]) % 4 == 1 or \
                len(update_data["secret_key"]) % 4 == 1:
            return None
        if update_data["secret_key"]:
            hashed_secret_key = encode_secret_key(update_data["secret_key"])
            del update_data["secret_key"]
            update_data["hashed_secret_key"] = hashed_secret_key
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def get_multi_by_owner(
            self, db: Session, *, owner_id: str, skip: int = 0, limit: int = 100
    ) -> List[Account]:
        return (
            db.query(self.model)
                .filter(Account.owner_id == owner_id)
                .offset(skip)
                .limit(limit)
                .all()
        )

    # def get_available_percentage(self, db: Session, *, account_id: int) -> int:
    #     percentage_invested = (db.query(func.sum(Portfolio.percentage))
    #                            .join(Account)
    #                            .filter(Account.id == account_id)
    #                            .scalar()
    #                            ) or 0
    #     return 100 - percentage_invested
    #
    # def get_count_portfolios(self, db: Session, *, account_id: int) -> int:
    #     n_portfolios = (db.query(Portfolio)
    #                     .join(Account)
    #                     .filter(Account.id == account_id)
    #                     .count())
    #     return n_portfolios


account = CRUDAccount(Account)
