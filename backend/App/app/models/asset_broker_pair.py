from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, ForeignKey, String, UniqueConstraint, Float, ARRAY, orm, Boolean
from app.db.base_class import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.mutable import MutableList

if TYPE_CHECKING:
    from app.models.association_table.asset_broker import Asset_broker  # noqa: F401


class Asset_broker_pair(Base):
    id = Column(Integer, primary_key=True, index=True)
    base_id = Column(Integer, ForeignKey('asset_broker.id'))
    quote_id = Column(Integer, ForeignKey('asset_broker.id'))
    base = relationship("Asset_broker", uselist=False, foreign_keys=[base_id], lazy='selectin')
    quote = relationship("Asset_broker", uselist=False, foreign_keys=[quote_id], lazy='selectin')
    symbol = Column(String(20))
    active = Column(Boolean, default=False)

    __table_args__ = (UniqueConstraint('base_id', 'quote_id', name='_base_quote_uc'),
                      )
