from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, ForeignKey, String, UniqueConstraint
from app.db.base_class import Base
from sqlalchemy.orm import relationship, backref

if TYPE_CHECKING:
    from app.models.broker.base_broker import Broker  # noqa: F401
    from app.models.asset.base_asset import Asset  # noqa: F401


class Asset_broker(Base):
    id = Column(Integer, primary_key=True)
    broker_id = Column(Integer, ForeignKey('broker.id'))
    asset_id = Column(Integer, ForeignKey('asset.id'))
    broker = relationship("Broker", backref=backref("assets_broker", cascade="all, delete-orphan"))
    asset = relationship("Asset")
    name = Column(String(20))

    __table_args__ = (UniqueConstraint('broker_id', 'asset_id', name='_asset_broker_uc'),
                      )
