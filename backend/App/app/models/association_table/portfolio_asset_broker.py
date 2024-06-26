from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, ForeignKey, String, ForeignKeyConstraint, UniqueConstraint, Float
from app.db.base_class import Base
from sqlalchemy.orm import relationship, backref
from app.models.association_table.asset_broker import Asset_broker  # noqa: F401

if TYPE_CHECKING:
    from app.models.asset_broker_pair import Asset_broker_pair  # noqa: F401
    from app.models.portfolio import Portfolio  # noqa: F401


class Portfolio_asset_broker(Base):
    id = Column(Integer, primary_key=True)
    asset_broker_pair_id = Column(Integer, ForeignKey('asset_broker_pair.id'))
    portfolio_id = Column(Integer, ForeignKey('portfolio.id'))
    portfolio = relationship("Portfolio", backref=backref("portfolio_asset_broker_pairs", cascade="all, delete-orphan"))
    asset_broker_pair = relationship("Asset_broker_pair", lazy='selectin')
    qty = Column(Float, default=0)

    __table_args__ = (UniqueConstraint('asset_broker_pair_id', 'portfolio_id', name='_asset_broker_pair_uc'),
                      )

    def __init__(self, asset_broker_pair_id, portfolio_id, qty):
        self.asset_broker_pair_id = asset_broker_pair_id
        self.portfolio_id = portfolio_id
        self.qty = qty

