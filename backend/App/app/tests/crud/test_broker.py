from app.models import Asset_broker
from app.schemas import AssetBrokerCreate
from app.schemas.broker import BrokerCreate
from app.tests.utils.asset import create_random_crypto_asset, create_crypto_assets_from_api_referential
from app.tests.utils.utils import random_integer, random_lower_string
from sqlalchemy.orm import Session
from app.tests.utils.broker import create_kraken_broker, create_broker
from app import crud


def test_create_broker(db_session: Session) -> None:
    name = random_lower_string()
    logo = random_lower_string()
    broker_id = random_lower_string()
    broker_in = BrokerCreate(
        name=name,
        logo=logo,
        broker_id=broker_id
    )
    broker = crud.broker.create(db=db_session, obj_in=broker_in)
    assert broker.name == name
    assert broker.broker_id == broker_id
    assert broker.logo == logo


def test_broker_status_public(db_session: Session) -> None:
    name = random_lower_string()
    logo = random_lower_string()
    broker_id = random_lower_string()
    broker_in = BrokerCreate(
        name=name,
        logo=logo,
        broker_id=broker_id
    )
    broker = crud.broker.create(db=db_session, obj_in=broker_in)
    status = broker.public_status()
    assert type(status) == bool
    assert status is False


def test_broker_get_available_assets(db_session: Session) -> None:
    kraken_broker = create_kraken_broker(db_session=db_session)
    assets = kraken_broker.get_available_assets()
    assert type(assets) == dict
    assert len(assets) > 0


def test_broker_add_asset(db_session: Session) -> None:
    broker = create_broker(db_session=db_session)
    asset = create_random_crypto_asset(db_session=db_session)
    name = random_lower_string(10)
    asset_broker_in = AssetBrokerCreate(name=name)
    crud.broker.add_asset(db=db_session, asset_in=asset, broker_in=broker, obj_in=asset_broker_in)
    asset_broker = broker.assets
    assert asset_broker
    assert asset in asset_broker


def test_broker_double_add_asset(db_session: Session) -> None:
    broker = create_broker(db_session)
    name_1 = random_lower_string(10)
    name_2 = random_lower_string(10)
    asset_1 = create_random_crypto_asset(db_session=db_session)
    asset_broker_in_1 = AssetBrokerCreate(name=name_1)
    asset_2 = create_random_crypto_asset(db_session=db_session)
    asset_broker_in_2 = AssetBrokerCreate(name=name_2)
    crud.broker.add_asset(db=db_session, asset_in=asset_1, broker_in=broker, obj_in=asset_broker_in_1)
    crud.broker.add_asset(db=db_session, asset_in=asset_2, broker_in=broker, obj_in=asset_broker_in_2)
    asset_broker = broker.assets
    assert asset_broker
    assert asset_1 in asset_broker
    assert asset_2 in asset_broker


def test_kraken_broker_double_add_asset_fail(db_session: Session) -> None:
    broker = create_broker(db_session)
    asset = create_random_crypto_asset(db_session=db_session)
    name = random_lower_string(10)
    asset_broker_in = AssetBrokerCreate(name=name)
    crud.broker.add_asset(db=db_session, asset_in=asset, broker_in=broker, obj_in=asset_broker_in)
    crud.broker.add_asset(db=db_session, asset_in=asset, broker_in=broker, obj_in=asset_broker_in)
    asset_broker = broker.assets
    assert asset_broker
    assert asset in asset_broker


def test_kraken_broker_remove_asset(db_session: Session) -> None:
    broker = create_broker(db_session)
    asset = create_random_crypto_asset(db_session=db_session)
    name = random_lower_string(10)
    asset_broker_in = AssetBrokerCreate(name=name)
    crud.broker.add_asset(db=db_session, asset_in=asset, broker_in=broker, obj_in=asset_broker_in)
    crud.broker.remove_asset(db=db_session, broker_in=broker, asset_in=asset)
    asset_broker = broker.assets
    assert asset not in asset_broker


def test_kraken_broker_remove_missing_asset(db_session: Session) -> None:
    broker = create_broker(db_session)
    asset = create_random_crypto_asset(db_session=db_session)
    crud.broker.remove_asset(db=db_session, broker_in=broker, asset_in=asset)
    asset_broker = broker.assets
    assert asset not in asset_broker
