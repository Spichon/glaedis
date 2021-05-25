# from app.models import Asset_broker
from app.schemas import BrokerCreate
# from app.tests.utils.asset import create_random_crypto_asset
from app.tests.utils.utils import random_integer, random_lower_string
from sqlalchemy.orm import Session

from app import crud, models


def create_broker(db: Session) -> models.Broker:
    name = random_lower_string()
    logo = random_lower_string()
    broker_id = random_lower_string()
    broker_in = BrokerCreate(
        name=name,
        logo=logo,
        broker_id=broker_id
    )
    broker = crud.broker.create(db=db, obj_in=broker_in)
    return broker

#
# def create_kraken_broker(db_session: Session) -> models.Broker:
#     name = 'Kraken'
#     logo = random_lower_string()
#     broker_id = 'kraken'
#     kraken_broker = crud.broker.get_by_key(db=db_session, broker_id=broker_id)
#     if kraken_broker is None:
#         broker_in = BrokerCreate(
#             name=name,
#             logo=logo,
#             broker_id=broker_id
#         )
#         kraken_broker = crud.broker.create(db=db_session, obj_in=broker_in)
#         return kraken_broker
#     return kraken_broker
#
#
# def broker_add_asset(db_session: Session) -> models.Asset_broker:
#     broker = create_broker(db_session)
#     asset = create_random_crypto_asset(db_session=db_session)
#     asset_broker_in = Asset_broker(name=random_lower_string(3))
#     return crud.broker.add_asset(db=db_session, asset_in=asset, broker_in=broker, obj_in=asset_broker_in)
#
#
# def create_asset_pair_without_quote_asset(db_session: Session) -> models.Asset_broker_pair:
#     broker = create_broker(db_session)
#     asset_1 = create_random_crypto_asset(db_session=db_session)
#     asset_broker_in_1 = Asset_broker(name=random_lower_string(3))
#     base = crud.broker.add_asset(db=db_session, asset_in=asset_1, broker_in=broker, obj_in=asset_broker_in_1)
#     asset_2 = create_random_crypto_asset(db_session=db_session)
#     asset_broker_in_2 = Asset_broker(name=random_lower_string(3))
#     quote = crud.broker.add_asset(db=db_session, asset_in=asset_2, broker_in=broker, obj_in=asset_broker_in_2)
#     asset_broker_pair_in = AssetBrokerPairCreate(altname=base.name + quote.name,
#                                                  symbol=base.name + quote.name,
#                                                  active=True
#                                                  )
#     asset_pair = crud.broker.add_asset_pair(db=db_session, base_asset_broker=base, quote_asset_broker=quote,
#                                             obj_in=asset_broker_pair_in)
#     return asset_pair
#
#
# def create_asset_pair_with_quote_asset(db_session: Session, quote: Asset_broker) -> models.Asset_broker_pair:
#     broker = create_broker(db_session)
#     asset_1 = create_random_crypto_asset(db_session=db_session)
#     asset_broker_in_1 = Asset_broker(name=random_lower_string(3))
#     base = crud.broker.add_asset(db=db_session, asset_in=asset_1, broker_in=broker, obj_in=asset_broker_in_1)
#     asset_broker_pair_in = AssetBrokerPairCreate(altname=base.name + quote.name,
#                                                  symbol=base.name + quote.name,
#                                                  active=True
#                                                  )
#     asset_pair = crud.broker.add_asset_pair(db=db_session, base_asset_broker=base, quote_asset_broker=quote,
#                                             obj_in=asset_broker_pair_in)
#     return asset_pair
