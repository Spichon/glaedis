from sqlalchemy import Column, Integer, String
from app.db.base_class import Base


class Asset(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String,)
    symbol = Column(String)
    slug = Column(String, unique=True)
    type = Column(String(20))

    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'asset',
        'with_polymorphic': '*'
    }

    def __init__(self, name, type, symbol, slug):
        self.name = name
        self.type = type
        self.symbol = symbol
        self.slug = slug
