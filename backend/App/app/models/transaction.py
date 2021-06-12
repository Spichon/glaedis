from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum, Float, String
from app.db.base_class import Base
from sqlalchemy.orm import relationship
import datetime
import enum

if TYPE_CHECKING:
    from .optimizer.base_optimizer import Optimizer  # noqa: F401
    from .run import Run  # noqa: F401
    from .transaction import Transaction  # noqa: F401
    from app.models.asset_broker_pair import Asset_broker_pair  # noqa: F401


class TransactionEnum(enum.Enum):
    buy = 1
    sell = 2


class Transaction(Base):
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(String, nullable=False)
    asset_broker_pair_id = Column(Integer, ForeignKey('asset_broker_pair.id'))
    asset_broker_pair = relationship("Asset_broker_pair", lazy='selectin')
    run_id = Column(Integer, ForeignKey('run.id'))
    run = relationship("Run", back_populates="transactions")
    qty = Column(Float, default=0)
    price = Column(Float, default=0)
    side = Column(Enum(TransactionEnum))
    date = Column(DateTime, default=datetime.datetime.utcnow)
