"""index

Revision ID: bd7eae91b168
Revises: b2f9a070cb5f
Create Date: 2021-05-10 20:52:09.565001

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd7eae91b168'
down_revision = 'b2f9a070cb5f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_asset_cmc_id', table_name='asset')
    op.drop_index('ix_asset_name', table_name='asset')
    op.drop_index('ix_asset_slug', table_name='asset')
    op.create_unique_constraint(None, 'asset', ['slug'])
    op.create_unique_constraint(None, 'asset', ['cmc_id'])
    op.create_index(op.f('ix_asset_broker_asset_id'), 'asset_broker', ['asset_id'], unique=False)
    op.create_index(op.f('ix_asset_broker_broker_id'), 'asset_broker', ['broker_id'], unique=False)
    op.drop_index('ix_broker_broker_id', table_name='broker')
    op.drop_index('ix_broker_name', table_name='broker')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_broker_name', 'broker', ['name'], unique=False)
    op.create_index('ix_broker_broker_id', 'broker', ['broker_id'], unique=False)
    op.drop_index(op.f('ix_asset_broker_broker_id'), table_name='asset_broker')
    op.drop_index(op.f('ix_asset_broker_asset_id'), table_name='asset_broker')
    op.drop_constraint(None, 'asset', type_='unique')
    op.drop_constraint(None, 'asset', type_='unique')
    op.create_index('ix_asset_slug', 'asset', ['slug'], unique=True)
    op.create_index('ix_asset_name', 'asset', ['name'], unique=False)
    op.create_index('ix_asset_cmc_id', 'asset', ['cmc_id'], unique=True)
    # ### end Alembic commands ###