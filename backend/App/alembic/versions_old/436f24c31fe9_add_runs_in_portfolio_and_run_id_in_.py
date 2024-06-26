"""add runs in portfolio and run_id in transaction

Revision ID: 436f24c31fe9
Revises: 007d42b2ff11
Create Date: 2021-06-07 17:37:51.687370

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '436f24c31fe9'
down_revision = '007d42b2ff11'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transaction', sa.Column('run_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'transaction', 'run', ['run_id'], ['id'])
    op.drop_column('transaction', 'date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transaction', sa.Column('date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'transaction', type_='foreignkey')
    op.drop_column('transaction', 'run_id')
    # ### end Alembic commands ###
