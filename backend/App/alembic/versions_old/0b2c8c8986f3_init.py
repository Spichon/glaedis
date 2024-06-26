"""Init

Revision ID: 0b2c8c8986f3
Revises: 
Create Date: 2021-05-03 09:25:38.227405

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b2c8c8986f3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('owner_id', sa.String(), nullable=True),
    sa.Column('api_key', sa.String(), nullable=False),
    sa.Column('hashed_secret_key', sa.String(), nullable=False),
    sa.Column('private_status', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_account_id'), 'account', ['id'], unique=False)
    op.create_index(op.f('ix_account_name'), 'account', ['name'], unique=False)
    op.create_index(op.f('ix_account_owner_id'), 'account', ['owner_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_account_owner_id'), table_name='account')
    op.drop_index(op.f('ix_account_name'), table_name='account')
    op.drop_index(op.f('ix_account_id'), table_name='account')
    op.drop_table('account')
    # ### end Alembic commands ###
