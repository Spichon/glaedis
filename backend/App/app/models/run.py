from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum
from app.db.base_class import Base
from sqlalchemy.orm import relationship
import datetime
import enum

if TYPE_CHECKING:
    from .optimizer.base_optimizer import Optimizer  # noqa: F401
    from .transaction import Transaction  # noqa: F401


class RunStateEnum(enum.Enum):
    created = 1
    running = 2
    achieved = 3
    failed = 4


class Run(Base):
    id = Column(Integer, primary_key=True, index=True)
    optimizer_id = Column(Integer, ForeignKey("optimizer.id"))
    optimizer = relationship("Optimizer", lazy='select')
    portfolio_id = Column(Integer, ForeignKey("portfolio.id"))
    portfolio = relationship("Portfolio", back_populates="runs", lazy='select')
    date = Column(DateTime, default=datetime.datetime.utcnow)
    state = Column(Enum(RunStateEnum))
    transactions = relationship("Transaction", back_populates="run", cascade="all, delete-orphan", lazy='selectin')
