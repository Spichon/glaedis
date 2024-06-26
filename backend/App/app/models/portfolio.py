from typing import TYPE_CHECKING

from app.core.security import decode_secret_key
from sqlalchemy import Column, Integer, ForeignKey, String, orm, TypeDecorator, Enum, Float
from app.db.base_class import Base
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship
import enum
from .association_table.portfolio_asset_broker import Portfolio_asset_broker

if TYPE_CHECKING:
    from .account import Account  # noqa: F401
    from .user import User  # noqa: F401
    from .association_table.asset_broker import Asset_broker  # noqa: F401
    from .asset_broker_pair import Asset_broker_pair  # noqa: F401
    from .optimizer.base_optimizer import Optimizer  # noqa: F401
    from .run import Run  # noqa: F401
    # from .celery_beat import Periodic_task  # noqa: F401


class Portfolio(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    account_id = Column(Integer, ForeignKey("account.id"))
    quote_asset_id = Column(Integer, ForeignKey("asset_broker.id"))
    account = relationship("Account", back_populates="portfolios", lazy='select')
    quote_asset = relationship("Asset_broker", lazy='select')
    assets = association_proxy("portfolio_asset_broker_pairs", "asset_broker_pair")
    ticker = Column(String)
    risk_free = Column(Integer, nullable=True)
    optimizer_id = Column(Integer, ForeignKey("optimizer.id"))
    optimizer = relationship("Optimizer", lazy='select')
    quote_asset_balance = Column(Float, default=0)
    runs = relationship("Run", back_populates="portfolio", cascade="all, delete-orphan", lazy='selectin')
    # automation_task_id = Column(Integer, ForeignKey("periodic_task.id"))
    # automation_task = relationship("Periodic_task", lazy='subquery')
