from app.models import Asset
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column, Integer, String


class Fiat_asset(Asset):
    __mapper_args__ = {
        'polymorphic_identity': 'fiat_asset'
    }
    sign = Column(String)

    @declared_attr
    def cmc_id(cls):
        "cmc_id column, if not present already."
        return Asset.__table__.c.get('cmc_id', Column(Integer, index=True, unique=True))

    @declared_attr
    def __tablename__(cls) -> str:
        return None

    def __init__(self, cmc_id, name, type, symbol, slug, sign):
        self.sign = sign
        self.cmc_id = cmc_id
        super().__init__(name=name, type=type, symbol=symbol, slug=slug)
