from app.models import Asset_broker
from app.schemas import AssetBrokerCreate
from app.schemas.broker import BrokerCreate
from app.tests.utils.asset import create_random_crypto_asset, create_crypto_assets_from_api_referential
from app.tests.utils.utils import random_integer, random_lower_string
from sqlalchemy.orm import Session
from app.tests.utils.broker import create_broker
from app import crud


def test_create_broker(db: Session) -> None:
    name = random_lower_string()
    logo = random_lower_string()
    broker_id = random_lower_string()
    broker_in = BrokerCreate(
        name=name,
        logo=logo,
        broker_id=broker_id
    )
    broker = crud.broker.create(db=db, obj_in=broker_in)
    assert broker.name == name
    assert broker.broker_id == broker_id
    assert broker.logo == logo


def test_broker_status_public(db: Session) -> None:
    name = random_lower_string()
    logo = random_lower_string()
    broker_id = random_lower_string()
    broker_in = BrokerCreate(
        name=name,
        logo=logo,
        broker_id=broker_id
    )
    broker = crud.broker.create(db=db, obj_in=broker_in)
    status = broker.public_status()
    assert type(status) == bool
    assert status is False


def test_broker_add_asset(db: Session) -> None:
    broker = create_broker(db=db)
    asset = create_random_crypto_asset(db=db)
    name = random_lower_string(10)
    asset_broker_in = AssetBrokerCreate(name=name)
    crud.broker.add_asset(db=db, asset_in=asset, broker_in=broker, obj_in=asset_broker_in)
    asset_broker = broker.assets
    assert asset_broker
    assert asset in asset_broker


def test_broker_double_add_asset(db: Session) -> None:
    broker = create_broker(db)
    name_1 = random_lower_string(10)
    name_2 = random_lower_string(10)
    asset_1 = create_random_crypto_asset(db=db)
    asset_broker_in_1 = AssetBrokerCreate(name=name_1)
    asset_2 = create_random_crypto_asset(db=db)
    asset_broker_in_2 = AssetBrokerCreate(name=name_2)
    crud.broker.add_asset(db=db, asset_in=asset_1, broker_in=broker, obj_in=asset_broker_in_1)
    crud.broker.add_asset(db=db, asset_in=asset_2, broker_in=broker, obj_in=asset_broker_in_2)
    asset_broker = broker.assets
    assert asset_broker
    assert asset_1 in asset_broker
    assert asset_2 in asset_broker


def test_kraken_broker_double_add_asset_fail(db: Session) -> None:
    broker = create_broker(db)
    asset = create_random_crypto_asset(db=db)
    name = random_lower_string(10)
    asset_broker_in = AssetBrokerCreate(name=name)
    crud.broker.add_asset(db=db, asset_in=asset, broker_in=broker, obj_in=asset_broker_in)
    crud.broker.add_asset(db=db, asset_in=asset, broker_in=broker, obj_in=asset_broker_in)
    asset_broker = broker.assets
    assert asset_broker
    assert asset in asset_broker


def test_kraken_broker_remove_asset(db: Session) -> None:
    broker = create_broker(db)
    asset = create_random_crypto_asset(db=db)
    name = random_lower_string(10)
    asset_broker_in = AssetBrokerCreate(name=name)
    crud.broker.add_asset(db=db, asset_in=asset, broker_in=broker, obj_in=asset_broker_in)
    crud.broker.remove_asset(db=db, broker_in=broker, asset_in=asset)
    asset_broker = broker.assets
    assert asset not in asset_broker


def test_kraken_broker_remove_missing_asset(db: Session) -> None:
    broker = create_broker(db)
    asset = create_random_crypto_asset(db=db)
    crud.broker.remove_asset(db=db, broker_in=broker, asset_in=asset)
    asset_broker = broker.assets
    assert asset not in asset_broker
