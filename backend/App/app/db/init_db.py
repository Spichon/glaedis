from sqlalchemy.orm import Session
from app.db import base  # noqa: F401
from app import crud, schemas
# from app.core.config import settings
# from app.models import IntervalSchedule

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)
    # crud.crypto_asset.create_assets_from_api_referential(db)  # noqa: F841
    # crud.fiat_asset.create_assets_from_api_referential(db)  # noqa: F841
    crud.broker.create_brokers_from_ccxt(db)  # noqa: F841
    # for e in [1, 5, 15, 30, 60, 240, 1440, 10080, 21600]:
    #     schedule = db.query(IntervalSchedule).filter_by(every=e, period=IntervalSchedule.MINUTES).first()
    #     if not schedule:
    #         schedule = IntervalSchedule(every=e, period=IntervalSchedule.MINUTES)
    #     db.add(schedule)
    #     db.commit()

