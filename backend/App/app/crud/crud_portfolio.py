from typing import List, Optional, Union, Dict, Any
from app.core.security import decode_secret_key
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
from app.schemas.portfolio_assets_broker import PortfolioAssetBroker
from app.schemas.run import RunCreate, RunUpdate
from app.schemas.transaction import TransactionCreate, TransactionUpdate
import pandas as pd
import numpy as np
import datetime

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
        portfolio = self.update_asset_broker_from_asset_pair_ids(db=db, db_obj=portfolio,
                                                                 asset_broker_pair_ids=[asset_pair.id for asset_pair in
                                                                                        asset_broker_pairs])
        portfolio = self.update_quote_asset_balance(db, portfolio)
        return portfolio

    def update(self, db: Session, *, db_obj: Portfolio, obj_in: Union[PortfolioUpdate, Dict[str, Any]]) -> Optional[
        Portfolio]:
        asset_broker_pairs = obj_in.asset_broker_pairs
        del obj_in.asset_broker_pairs
        # if obj_in.ticker:
        #     obj_in.ticker = obj_in.ticker.value
        portfolio = super().update(db, db_obj=db_obj, obj_in=obj_in)
        portfolio = self.update_asset_broker_from_asset_pair_ids(db=db, db_obj=portfolio,
                                                                 asset_broker_pair_ids=[asset_pair.id for asset_pair in
                                                                                        asset_broker_pairs])
        portfolio = self.update_quote_asset_balance(db, portfolio)
        return portfolio

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

    def update_asset_broker_from_asset_pair_ids(self, db: Session, db_obj: Portfolio,
                                                asset_broker_pair_ids: List[int]) -> Portfolio:
        portfolio_balances = self.get_held_balance(db_obj)
        portfolio_asset_ids = [asset.id for asset in db_obj.assets]
        portfolio_asset_ids = set(portfolio_asset_ids)
        wish_asset_ids = asset_broker_pair_ids
        wish_asset_ids = set(wish_asset_ids)
        remove_assets_from_portfolio_ids = list(portfolio_asset_ids.difference(wish_asset_ids))
        db.query(Portfolio_asset_broker).filter(
            Portfolio_asset_broker.asset_broker_pair_id.in_(remove_assets_from_portfolio_ids)).delete()
        add_assets_in_portfolio_ids = list(wish_asset_ids.difference(portfolio_asset_ids))
        market = db_obj.account.broker.load_market()
        assets_to_add = db.query(Asset_broker_pair).filter(Asset_broker_pair.id.in_(add_assets_in_portfolio_ids))
        for asset in assets_to_add:
            try:
                qty = portfolio_balances[asset.base.asset.symbol]['total']
                qty = round(qty, market[asset.symbol]['precision']['amount'])
            except KeyError:
                qty = 0
            temp = Portfolio_asset_broker(asset_broker_pair_id=asset.id, portfolio_id=db_obj.id, qty=qty)
            db.add(temp)
            db.flush()
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update_quote_asset_balance(self, db: Session, db_obj: Portfolio, portfolio_balance=None) -> Portfolio:
        if portfolio_balance is None:
            portfolio_balances = self.get_held_balance(db_obj)
        qty = portfolio_balances[db_obj.quote_asset.asset.symbol]['total']
        db_obj.quote_asset_balance = qty
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_portfolio_equity_balance(self, db: Session, db_obj: Portfolio) -> float:
        portfolio_assets = self.get_portfolio_assets(db, db_obj)
        eb = sum(obj.current_price * obj.qty for obj in portfolio_assets)
        return eb

    def get_held_balance(self, db_obj: Portfolio) -> {}:
        api_key = db_obj.account.api_key
        secret_key = decode_secret_key(db_obj.account.hashed_secret_key)
        held_balance = db_obj.account.broker.get_balance(api_key, secret_key)
        return held_balance

    def get_portfolio_assets(self, db: Session, db_obj: Portfolio) -> List[PortfolioAssetBroker]:
        portfolio_assets = db.query(Portfolio_asset_broker) \
            .filter(Portfolio_asset_broker.portfolio_id == db_obj.id).all()
        assets_symbol = [portfolio_asset.asset_broker_pair.symbol for portfolio_asset in portfolio_assets]
        last_values = db_obj.account.broker.get_last_values(assets_symbol)
        for asset in portfolio_assets:
            asset.opening_price = last_values[asset.asset_broker_pair.symbol]['opening_price']
            asset.current_price = last_values[asset.asset_broker_pair.symbol]['current_price']
        return portfolio_assets

    def optimize(self, db: Session, db_obj: Portfolio) -> Any:
        if db_obj.account.private_status:
            run_in = RunCreate(date=datetime.datetime.utcnow(),
                               state="created",
                               portfolio_id=db_obj.id,
                               optimizer_id=db_obj.optimizer.id)
            run = crud.run.create(db=db, obj_in=run_in)
            try:
                dfs = []
                api_key = db_obj.account.api_key
                secret_key = decode_secret_key(db_obj.account.hashed_secret_key)
                assets = self.get_portfolio_assets(db, db_obj)
                if len(assets) > 0:
                    for asset in assets:
                        result = db_obj.account.broker.fetch_ohlcv(assets=[asset.asset_broker_pair.symbol],
                                                                   ticker=db_obj.ticker)
                        result['{}'.format(asset.asset_broker_pair.symbol)] = result['close']
                        dfs.append(result['{}'.format(asset.asset_broker_pair.symbol)])
                    if len(dfs) > 0:
                        dfs = reduce(lambda df1, df2: pd.merge(df1, df2, left_index=True, right_index=True), dfs)
                    returns = (dfs - dfs.shift(1)) / dfs.shift(1)
                    weights = db_obj.optimizer.get_weights(portfolio=db_obj, returns=returns)
                    weights = weights.round(2)
                    run_update = RunUpdate(date=datetime.datetime.utcnow(),
                                    state="running")
                    run = crud.run.update(db=db, db_obj=run, obj_in=run_update)
                    percent_wish = pd.DataFrame(weights, [asset.asset_broker_pair.symbol for asset in assets],
                                                columns=['percent_wish'])
                    last_values = pd.DataFrame([x.current_price for x in assets], columns=['last_value'],
                                               index=[x.asset_broker_pair.symbol for x in assets])

                    equity_balance = self.get_portfolio_equity_balance(db, db_obj)
                    quote_asset_balance = db_obj.quote_asset_balance
                    total_balance = equity_balance + quote_asset_balance
                    total_balance = total_balance * 0.95
                    wish_balance = percent_wish.mul(total_balance)['percent_wish'] / last_values['last_value']
                    wish_balance = pd.DataFrame(wish_balance, columns=["wish_balance"]).fillna(0)
                    held_balance = pd.DataFrame([x.qty for x in assets], columns=['quantity_held'],
                                                index=[x.asset_broker_pair.symbol for x in assets])
                    state = pd.merge(wish_balance, held_balance, left_index=True, right_index=True, how="outer")
                    state['diff'] = np.subtract(state['wish_balance'], state['quantity_held'])
                    state = state.sort_values(by=['diff'])
                    market = db_obj.account.broker.load_market()
                    for asset in assets:
                        sub_df = state.loc[asset.asset_broker_pair.symbol, :]
                        qty = sub_df['diff']
                        qty = round(qty, market[asset.asset_broker_pair.symbol]['precision']['amount'])
                        ordermin = market[asset.asset_broker_pair.symbol]['limits']['amount']['min']
                        print(asset.asset_broker_pair.symbol, qty, ordermin)
                        if qty < 0 and -qty > ordermin:
                            print("Sell asset : {}, qty : {}".format(asset.asset_broker_pair.symbol, qty))
                            result = db_obj.account.broker.create_order(api_key=api_key,
                                                                        secret_key=secret_key,
                                                                        symbol=asset.asset_broker_pair.symbol,
                                                                        qty=-qty,
                                                                        type="market",
                                                                        side="sell")
                            asset.qty = 0
                            print(result)
                            transaction_in = TransactionCreate(date=datetime.datetime.utcnow(),
                                                       side="sell",
                                                       asset_broker_pair_id=asset.asset_broker_pair.id,
                                                       run_id=run.id,
                                                       order_id=result['id'],
                                                       qty=result['amount'])
                            crud.transaction.create(db=db, obj_in=transaction_in)
                    for asset in assets:
                        sub_df = state.loc[asset.asset_broker_pair.symbol, :]
                        qty = sub_df['diff']
                        qty = round(qty, market[asset.asset_broker_pair.symbol]['precision']['amount'])
                        ordermin = market[asset.asset_broker_pair.symbol]['limits']['amount']['min']
                        print(asset.asset_broker_pair.symbol, qty, ordermin)
                        if qty > 0 and qty >= ordermin:
                            print("Buy asset : {}, qty : {}".format(asset.asset_broker_pair.symbol, qty))
                            result = db_obj.account.broker.create_order(api_key=api_key,
                                                                        secret_key=secret_key,
                                                                        symbol=asset.asset_broker_pair.symbol,
                                                                        qty=qty,
                                                                        type="market",
                                                                        side="buy")
                            asset.qty = qty
                            print(result)
                            transaction_in = TransactionCreate(date=datetime.datetime.utcnow(),
                                                               side="buy",
                                                               asset_broker_pair_id=asset.asset_broker_pair.id,
                                                               run_id=run.id,
                                                               order_id=result['id'],
                                                               qty=result['amount'])
                            crud.transaction.create(db=db, obj_in=transaction_in)
                    self.update_quote_asset_balance(db, db_obj)
                    run_update = RunUpdate(date=datetime.datetime.utcnow(),
                                           state="achieved")
                    run = crud.run.update(db=db, db_obj=run, obj_in=run_update)
                    return True
                else:
                    return []
            except Exception as e:
                self.update_quote_asset_balance(db, db_obj)
                run_update = RunUpdate(date=datetime.datetime.utcnow(),
                                       state="failed")
                crud.run.update(db=db, db_obj=run, obj_in=run_update)
        return {'msg': "No private access to your account. Check your private key"}


portfolio = CRUDPortfolio(Portfolio)
