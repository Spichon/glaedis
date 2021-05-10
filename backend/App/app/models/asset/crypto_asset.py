from app.models import Asset
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column, Integer, Float


class Crypto_asset(Asset):
    __mapper_args__ = {
        'polymorphic_identity': 'crypto_asset'
    }
    cmc_rank = Column(Integer, index=True)
    circulating_supply = Column(Float)
    total_supply = Column(Float)

    @declared_attr
    def cmc_id(cls):
        "cmc_id column, if not present already."
        return Asset.__table__.c.get('cmc_id', Column(Integer, unique=True))

    @declared_attr
    def __tablename__(cls) -> str:
        return None

    def __init__(self, cmc_id, name, type, symbol, slug, circulating_supply, total_supply, cmc_rank):
        self.cmc_rank = cmc_rank
        self.cmc_id = cmc_id
        self.circulating_supply = circulating_supply
        self.total_supply = total_supply

        super().__init__(name=name, type=type, symbol=symbol, slug=slug)
