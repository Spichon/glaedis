# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.account import Account  # noqa
from app.models.broker import Broker  # noqa
from app.models.asset.base_asset import Asset  # noqa
from app.models.asset.crypto_asset import Crypto_asset  # noqa
from app.models.asset.fiat_asset import Fiat_asset  # noqa
from app.models.asset_broker_pair import Asset_broker_pair  # noqa
from app.models.portfolio import Portfolio  # noqa
