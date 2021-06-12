from app.db.base_class import Base
from sqlalchemy import Column, Integer, String


class Optimizer(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'optimizer',
        'polymorphic_on': name
    }

    def get_weights(self, **kwargs):
        pass
