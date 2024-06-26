"""index

Revision ID: 369501290d20
Revises: bd7eae91b168
Create Date: 2021-05-16 13:50:29.061999

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '369501290d20'
down_revision = 'bd7eae91b168'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_asset_cmc_rank', table_name='asset')
    op.drop_index('ix_asset_id', table_name='asset')
    op.drop_index('ix_asset_broker_asset_id', table_name='asset_broker')
    op.drop_index('ix_asset_broker_broker_id', table_name='asset_broker')
    op.drop_index('ix_asset_broker_id', table_name='asset_broker')
    op.drop_index('ix_broker_id', table_name='broker')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_broker_id', 'broker', ['id'], unique=False)
    op.create_index('ix_asset_broker_id', 'asset_broker', ['id'], unique=False)
    op.create_index('ix_asset_broker_broker_id', 'asset_broker', ['broker_id'], unique=False)
    op.create_index('ix_asset_broker_asset_id', 'asset_broker', ['asset_id'], unique=False)
    op.create_index('ix_asset_id', 'asset', ['id'], unique=False)
    op.create_index('ix_asset_cmc_rank', 'asset', ['cmc_rank'], unique=False)
    # ### end Alembic commands ###
