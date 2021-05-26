from typing import List, Optional, Dict, Any, Union

from app.models import Asset
from app import schemas
from fastapi import Body
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session, with_polymorphic

from app.crud.base import CRUDBase
from app.models.broker import Broker
from app.models.association_table.asset_broker import Asset_broker
from app.models.asset_broker_pair import Asset_broker_pair
from app.schemas.broker import BrokerCreate, BrokerUpdate
from app.schemas.assets_broker import AssetBrokerCreate
from app.schemas.asset_broker_pair import AssetBrokerPairCreate
from app import crud
import json
import ccxt


class CRUDBroker(CRUDBase[Broker, BrokerCreate, BrokerUpdate]):
    def add_asset(self, db: Session, asset_in: Asset, broker_in: Broker, obj_in: AssetBrokerCreate) -> Asset_broker:
        db_obj = db.query(Asset_broker) \
            .filter(Asset_broker.asset_id == asset_in.id) \
            .filter(Asset_broker.broker_id == broker_in.id).first()
        if db_obj is None:
            obj_in_data = jsonable_encoder(obj_in)
            db_obj = Asset_broker(asset=asset_in, broker=broker_in, **obj_in_data)
            broker_in.assets_broker.append(db_obj)
            db.commit()
        return db_obj

    def remove_asset(self, db: Session, broker_in: Broker, asset_in: Asset) -> Asset_broker:
        broker = broker_in
        db_obj = db.query(Asset_broker) \
            .filter(Asset_broker.asset_id == asset_in.id) \
            .filter(Asset_broker.broker_id == broker.id).first()
        if db_obj:
            broker.assets_broker.remove(db_obj)
            db.commit()
        return db_obj

    def add_asset_pair(self, db: Session, quote_asset_broker: Asset_broker_pair, base_asset_broker: Asset_broker_pair,
                       obj_in: AssetBrokerPairCreate) -> Asset_broker_pair:
        db_obj = db.query(Asset_broker_pair) \
            .filter(Asset_broker_pair.quote_id == quote_asset_broker.id) \
            .filter(Asset_broker_pair.base_id == base_asset_broker.id).first()
        if db_obj is None:
            obj_in = jsonable_encoder(obj_in)
            db_obj = Asset_broker_pair(base_id=base_asset_broker.id, quote_id=quote_asset_broker.id,
                                       **obj_in)
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
        return db_obj

    # def remove_asset(self, db: Session, asset_in: Asset) -> Broker:
    #     broker = self.get_or_create(db=db)
    #     asset_broker = db.query(Asset_broker) \
    #         .filter(Asset_broker.asset_id == asset_in.id) \
    #         .filter(Asset_broker.broker_id == broker.id).first()
    #     if asset_broker:
    #         broker.assets_broker.remove(asset_broker)
    #     db.add(broker)
    #     db.commit()
    #     db.refresh(broker)
    #     return broker

    def update_asset_broker(self, db: Session, db_obj: Broker) -> Broker:
        broker = db_obj
        assets = broker.get_available_assets().items()
        for key, asset_element in assets:
            try:
                symbol = asset_element["code"]
                asset = crud.asset.get_by_key(db=db, symbol=symbol)
                if asset:
                    asset_broker_in = AssetBrokerCreate(name=asset_element["id"])
                    self.add_asset(db=db, asset_in=asset, broker_in=broker, obj_in=asset_broker_in)
            except KeyError:
                pass
        self.update_tradable_asset_pairs(db=db, db_obj=broker)
        return broker

    def get_quote_assets(self, db: Session, id: int) -> List[Asset_broker]:
        quote_assets = db.query(Asset_broker) \
            .join(Asset_broker_pair.quote) \
            .filter(Asset_broker_pair.quote_id == Asset_broker.id) \
            .filter(Asset_broker.broker_id == id).distinct().all()
        return quote_assets

    def get_tradable_asset_pairs(self, db: Session, id: int) -> List[Asset_broker_pair]:
        tradable_asset_pairs = db.query(Asset_broker_pair).filter(Asset_broker_pair.quote_id == id).distinct().all()
        return tradable_asset_pairs

    def get_available_assets(self, db: Session, id: int) -> List[schemas.Asset]:
        assets = db.query(Asset).join(Asset_broker).filter(Asset.id == Asset_broker.asset_id).filter(
            Asset_broker.broker_id == id).all()
        return assets

    def update_tradable_asset_pairs(self, db: Session, db_obj: Broker):
        broker = db_obj
        asset_pairs = broker.get_tradable_asset_pairs()
        for asset_element in asset_pairs:
            try:
                obj_in = AssetBrokerPairCreate(
                    symbol=asset_element['symbol'],
                    active=asset_element['active']
                )
                base = asset_element['base']
                quote = asset_element['quote']
                base_asset_broker = None
                quote_asset_broker = None
                base_asset_broker = db.query(Asset_broker) \
                    .join(Asset) \
                    .filter(Asset.symbol == base) \
                    .filter(Asset_broker.broker_id == broker.id).first()
                if base_asset_broker is None:
                    asset_b = crud.asset.get_by_key(db=db, symbol=base)
                    if asset_b:
                        asset_broker_in = AssetBrokerCreate(name=asset_element["baseId"])
                        base_asset_broker = self.add_asset(db=db, asset_in=asset_b, broker_in=broker,
                                                           obj_in=asset_broker_in)
                quote_asset_broker = db.query(Asset_broker) \
                    .join(Asset) \
                    .filter(Asset.symbol == quote) \
                    .filter(Asset_broker.broker_id == broker.id).first()
                if quote_asset_broker is None:
                    asset_q = crud.asset.get_by_key(db=db, symbol=quote)
                    if asset_q:
                        asset_broker_in = AssetBrokerCreate(name=asset_element["quoteId"])
                        quote_asset_broker = self.add_asset(db=db, asset_in=asset_q, broker_in=broker,
                                                            obj_in=asset_broker_in)
                if base_asset_broker and quote_asset_broker:
                    self.add_asset_pair(db=db, quote_asset_broker=quote_asset_broker,
                                        base_asset_broker=base_asset_broker, obj_in=obj_in)

            except KeyError:
                pass

    def create_brokers_from_ccxt(self, db: Session):
        print('CCXT Version:', ccxt.__version__)
        with open('app/db/ccxt_available_broker.txt') as f:
            available_brokers = f.read().splitlines()
        for broker_id in available_brokers:
            try:
                broker = getattr(ccxt, broker_id)()
                obj_in = BrokerCreate(
                    name=broker.name,
                    broker_id=broker_id,
                    logo=broker.urls['logo']
                )
                existing_broker = self.get_by_key(db=db, broker_id=broker_id)
                if existing_broker is None:
                    existing_broker = self.create(db=db, obj_in=obj_in)
                self.update_asset_broker(db=db, db_obj=existing_broker)
            except Exception as e:
                print(e)

    def get_timeframes(self, db_obj: Broker) -> schemas.Timeframes:
        return db_obj.get_timeframes()


broker = CRUDBroker(Broker)
