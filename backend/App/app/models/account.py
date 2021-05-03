from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, ForeignKey, String, orm, Boolean
from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401
    from .portfolio import Portfolio  # noqa: F401


class Account(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    owner_id = Column(String, index=True)
    # portfolios = relationship("Portfolio", back_populates="account", cascade="all, delete-orphan")
    # broker_id = Column(Integer, ForeignKey("broker.id"))
    # broker = relationship("Broker", lazy='subquery')
    api_key = Column(String, nullable=False)
    hashed_secret_key = Column(String, nullable=False)
    private_status = Column(Boolean, nullable=False, default=False)

    # @orm.reconstructor
    # def init_on_load(self):
    #     self.public_status = self.broker.public_status()
    #
    # @classmethod
    # def update_private_status(cls, mapper, connection, target):
    #     """
    #     :param mapper: the Mapper which is the target of this event
    #     :param connection: the Connection being used
    #     :param target: the mapped instance being persisted
    #     """
    #     s = connection.execute(select([Account]).
    #                            where(Account.id == target.id).limit(1))
    #     if not s:
    #         pass
    #     else:
    #         for row in s:
    #             api_key = row.api_key
    #             secret_key = decode_secret_key(row.hashed_secret_key)
    #             db = SessionLocal()
    #             broker = db.query(Broker).filter(Broker.id == row.broker_id).first()
    #             if broker:
    #                 private_status = broker.private_status(api_key, secret_key)
    #                 s = connection.execute(update(Account).
    #                                        where(Account.id == target.id).
    #                                        values(private_status=private_status))


# listen(Account, 'after_insert', Account.update_private_status)
# listen(Account, 'after_update', Account.update_private_status)
