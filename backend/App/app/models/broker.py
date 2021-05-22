from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String
from app.db.base_class import Base
from sqlalchemy.ext.associationproxy import association_proxy
import pandas as pd
import ccxt

if TYPE_CHECKING:
    from app.models.association_table.asset_broker import Asset_broker  # noqa: F401


class Broker(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    broker_id = Column(String)
    logo = Column(String)
    assets = association_proxy("assets_broker", "asset")

    def get_api(self, api_key: str = "", secret_key: str = ""):
        return getattr(ccxt, self.broker_id)({
            'apiKey': api_key,
            'secret': secret_key,
        })

    def public_status(self) -> bool:
        try:
            api = self.get_api()
            if api.fetch_status()['status'] == 'ok':
                return True
            return False
        except:
            return False

    def private_status(self, api_key: str = "", secret_key: str = "") -> bool:
        try:
            api = self.get_api(api_key=api_key, secret_key=secret_key)
            api.fetch_balance()
            return True
        except Exception as e:
            print(e)
            return False

    def get_available_assets(self) -> {}:
        try:
            api = self.get_api()
            assets = api.fetchCurrencies()
            relevant_assets = dict((k, v) for k, v in assets.items() if not ('.' in v['code']))
            return relevant_assets
        except:
            return {}

    def get_tradable_asset_pairs(self) -> [{}]:
        try:
            api = self.get_api()
            relevant_assets_pairs = api.fetchMarkets()
            return relevant_assets_pairs
        except:
            return {}

    def get_balance(self, api_key: str = "", secret_key: str = "") -> {}:
        try:
            api = self.get_api(api_key=api_key, secret_key=secret_key)
            balance = api.fetch_balance()
            return balance
        except:
            return {}

    def get_asset_balance(self, api_key: str = "", secret_key: str = "", asset_symbol: str = "") -> float:
        try:
            balance = self.get_balance(api_key=api_key, secret_key=secret_key)
            balance_asset = balance[asset_symbol]['total']
            return balance_asset
        except:
            return 0

    def get_ticker(self, assets: [str]) -> {}:
        try:
            api = self.get_api()
            if (api.has['fetchTickers']):
                tickers = api.fetch_tickers(assets)
                return tickers
            return {}
        except:
            return {}

    def get_last_values(self, assets: [str]) -> [dict]:
        try:
            tickers = self.get_ticker(assets)
            to_return = [
                {ticker: {"current_price": tickers[ticker]['close'], "opening_price": tickers[ticker]['open']}} for
                ticker
                in tickers]
            return to_return
        except:
            return []

    def fetch_ohlcv(self, assets: [str], ticker: int):
        try:
            api = self.get_api()
            if (api.has['fetchOHLCV']):
                for asset in assets:
                    tickers = api.fetch_ohlcv(asset, ticker)
                    return tickers
            return {}
        except:
            return {}
