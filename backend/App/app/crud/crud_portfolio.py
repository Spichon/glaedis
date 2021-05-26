import json
from typing import List, Optional, Union, Dict, Any

from app.core.security import decode_secret_key
from app.core.utils import findMaxSharpeRatioPortfolio, findMinVariancePortfolio
from app.models import Asset_broker_pair
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from functools import reduce
from app.crud.base import CRUDBase
from app import crud
from app.models.portfolio import Portfolio
from app.models.account import Account
from app.schemas.portfolio import PortfolioCreate, PortfolioUpdate
from app.models.association_table.portfolio_asset_broker import Portfolio_asset_broker
from app.schemas.portfolio_assets_broker import PortfolioAssetBrokerCreate
import pandas as pd
import numpy as np


class CRUDPortfolio(CRUDBase[Portfolio, PortfolioCreate, PortfolioUpdate]):

    # def create(self, db: Session, *, obj_in: PortfolioCreate) -> Optional[Portfolio]:
    #     available_percentage = crud.account.get_available_percentage(db=db, account_id=obj_in.account_id)
    #     if (available_percentage - obj_in.percentage) >= 0:
    #         asset_broker_pairs = obj_in.asset_broker_pairs
    #         del obj_in.asset_broker_pairs
    #         portfolio = super().create(db, obj_in=obj_in)
    #         return self.update_asset_broker_from_asset_pair_ids(db=db, db_obj=portfolio,
    #                                                             asset_broker_pair_ids=[asset_pair.id for asset_pair in
    #                                                                                    asset_broker_pairs])
    #     return None
    #
    # def update(self, db: Session, *, db_obj: Portfolio, obj_in: Union[PortfolioUpdate, Dict[str, Any]]) -> Optional[
    #     Portfolio]:
    #     if obj_in.percentage:
    #         if float(obj_in.percentage) >= db_obj.percentage:
    #             available_percentage = crud.account.get_available_percentage(db=db, account_id=db_obj.account_id)
    #             if (available_percentage - float(obj_in.percentage)) < 0:
    #                 obj_in.percentage = available_percentage
    #                 n_portfolios = crud.account.get_count_portfolios(db=db, account_id=db_obj.account_id)
    #                 if n_portfolios == 1:
    #                     obj_in.percentage = obj_in.percentage + float(db_obj.percentage)
    #     asset_broker_pairs = obj_in.asset_broker_pairs
    #     del obj_in.asset_broker_pairs
    #     if obj_in.ticker:
    #         obj_in.ticker = obj_in.ticker.value
    #         portfolio = crud.portfolio_automation_task.update_automation(db, db_obj=db_obj, ticker=obj_in.ticker)
    #     portfolio = super().update(db, db_obj=db_obj, obj_in=obj_in)
    #     return self.update_asset_broker_from_asset_pair_ids(db=db, db_obj=portfolio,
    #                                                         asset_broker_pair_ids=[asset_pair.id for asset_pair in
    #                                                                                asset_broker_pairs])

    def create(self, db: Session, *, obj_in: PortfolioCreate) -> Optional[Portfolio]:
        asset_broker_pairs = obj_in.asset_broker_pairs
        del obj_in.asset_broker_pairs
        portfolio = super().create(db, obj_in=obj_in)
        return self.update_asset_broker_from_asset_pair_ids(db=db, db_obj=portfolio,
                                                            asset_broker_pair_ids=[asset_pair.id for asset_pair in
                                                                                   asset_broker_pairs])

    def update(self, db: Session, *, db_obj: Portfolio, obj_in: Union[PortfolioUpdate, Dict[str, Any]]) -> Optional[
        Portfolio]:
        asset_broker_pairs = obj_in.asset_broker_pairs
        del obj_in.asset_broker_pairs
        # if obj_in.ticker:
        #     obj_in.ticker = obj_in.ticker.value
        portfolio = super().update(db, db_obj=db_obj, obj_in=obj_in)
        return self.update_asset_broker_from_asset_pair_ids(db=db, db_obj=portfolio,
                                                            asset_broker_pair_ids=[asset_pair.id for asset_pair in
                                                                                   asset_broker_pairs])

    def get_multi_by_owner(
            self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[Portfolio]:
        return (db.query(Portfolio)
                .join(Account)
                .filter(Account.owner_id == owner_id)
                .offset(skip)
                .limit(limit)
                .all()
                )

    def add_asset_broker_pair(self, db: Session, db_obj: Portfolio, asset_broker_pair_in: Asset_broker_pair,
                              obj_in: PortfolioAssetBrokerCreate) -> Optional[Portfolio_asset_broker]:
        portfolio_asset_broker = db.query(Portfolio_asset_broker) \
            .filter(Portfolio_asset_broker.portfolio_id == db_obj.id) \
            .filter(Portfolio_asset_broker.asset_broker_pair_id == asset_broker_pair_in.id).first()
        if db_obj.quote_asset_id == asset_broker_pair_in.quote_id and portfolio_asset_broker is None:
            obj_in_data = jsonable_encoder(obj_in)
            obj_in_obj = Portfolio_asset_broker(asset_broker_pair=asset_broker_pair_in, portfolio=db_obj,
                                                **obj_in_data)
            db_obj.portfolio_asset_broker_pairs.append(obj_in_obj)
            db.commit()
            return obj_in_obj
        return None

    def remove_asset_broker_pair(self, db: Session, db_obj: Portfolio,
                                 portfolio_asset_broker_in: Portfolio_asset_broker) -> Portfolio:
        try:
            db_obj.portfolio_asset_broker_pairs.remove(portfolio_asset_broker_in)
            db.commit()
        except ValueError:
            pass
        return db_obj

    def update_asset_broker_from_asset_pair_ids(self, db: Session, db_obj: Portfolio,
                                                asset_broker_pair_ids: List[int]) -> Portfolio:
        portfolio_asset_broker_list = db.query(Portfolio_asset_broker) \
            .filter(~Portfolio_asset_broker.asset_broker_pair_id.in_(asset_broker_pair_ids)).all()
        # Remove if portfolio_asset_broker_pair_id not in asset_broker_pair_ids
        for portfolio_asset_broker in portfolio_asset_broker_list:
            self.remove_asset_broker_pair(db=db, db_obj=db_obj, portfolio_asset_broker_in=portfolio_asset_broker)
        # Add asset_broker_pair from asset_broker_pair_ids
        asset_broker_pair = db.query(Asset_broker_pair) \
            .filter(Asset_broker_pair.id.in_(asset_broker_pair_ids)).all()
        for asset_broker in asset_broker_pair:
            asset_broker_pair_in = PortfolioAssetBrokerCreate()
            self.add_asset_broker_pair(db=db, db_obj=db_obj, asset_broker_pair_in=asset_broker,
                                       obj_in=asset_broker_pair_in)
        db.refresh(db_obj)
        return db_obj

    def get_assets_last_values(self, db_obj: Portfolio) -> List[dict]:
        if len(db_obj.assets) > 0:
            return db_obj.account.broker.get_last_values([asset.symbol for asset in db_obj.assets])
        else:
            return []

    def get_asset_balance(self, db_obj: Portfolio) -> float:
        api_key = db_obj.account.api_key
        secret_key = decode_secret_key(db_obj.account.hashed_secret_key)
        asset_balance = db_obj.account.broker.get_asset_balance(api_key, secret_key, db_obj.quote_asset.asset.symbol)
        return asset_balance

    def get_weights(self, db_obj: Portfolio) -> Any:
        dfs = []
        if len(db_obj.assets) > 0:
            for asset in db_obj.assets:
                result = db_obj.account.broker.fetch_ohlcv(assets=[asset.symbol],
                                                           ticker=db_obj.ticker)
                result['{}'.format(asset.symbol)] = result['close']
                dfs.append(result['{}'.format(asset.symbol)])
            if len(dfs) > 0:
                dfs = reduce(lambda df1, df2: pd.merge(df1, df2, left_index=True, right_index=True), dfs)

            # Calculate simple linear returns
            returns = (dfs - dfs.shift(1)) / dfs.shift(1)

            # Calculate individual mean returns and covariance between the stocks
            meanDailyReturns = returns.mean()
            covMatrix = returns.cov()
            riskFreeRate = 0.1

            # Find portfolio with maximum Sharpe ratio
            maxSharpe = findMaxSharpeRatioPortfolio(meanDailyReturns, covMatrix, riskFreeRate)
            # Find portfolio with minimum variance
            # minVar = findMinVariancePortfolio(meanDailyReturns, covMatrix)
            return maxSharpe['x']


        else:
            return []


portfolio = CRUDPortfolio(Portfolio)
