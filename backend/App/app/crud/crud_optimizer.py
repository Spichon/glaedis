from app.crud.base import CRUDBase
from app.models import Optimizer
from app.models.optimizer.markov_sharpe_optimizer import Markov_sharpe_optimizer
from app.models.optimizer.markov_volatility_optimizer import Markov_volatility_optimizer
from app.schemas.optimizer import OptimizerCreate, OptimizerUpdate
from sqlalchemy.orm import Session
from typing import Optional


class CRUDBroker(CRUDBase[Optimizer, OptimizerCreate, OptimizerUpdate]):
    def get_or_create(self, db: Session) -> Optional[Optimizer]:
        name = self.model.__mapper_args__['polymorphic_identity']
        optimizer = super().get_by_key(db=db, name=name)
        if optimizer is None:
            obj_in = OptimizerCreate(
                name=self.model.__mapper_args__['polymorphic_identity']
            )
            return super().create(db=db, obj_in=obj_in)
        return None


optimizer = CRUDBroker(Optimizer)
markov_sharpe_optimizer = CRUDBroker(Markov_sharpe_optimizer)
markov_volatility_optimizer = CRUDBroker(Markov_volatility_optimizer)
